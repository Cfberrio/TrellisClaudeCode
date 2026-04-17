import json
import urllib.error
from io import BytesIO
from unittest.mock import MagicMock, call, patch

import pytest

from src.common.http import APIError, _mask_token, get


def _mock_response(data: dict, status: int = 200):
    """Create a mock urlopen response."""
    body = json.dumps(data).encode()
    mock = MagicMock()
    mock.read.return_value = body
    mock.__enter__ = lambda s: s
    mock.__exit__ = MagicMock(return_value=False)
    return mock


def _mock_http_error(status: int, body: dict = None):
    body_bytes = json.dumps(body or {}).encode()
    return urllib.error.HTTPError(
        url="http://x", code=status, msg="err",
        hdrs=None, fp=BytesIO(body_bytes)
    )


# ── mask_token ────────────────────────────────────────────────────────────────

def test_mask_token_normal():
    assert _mask_token("EAABcdef12345678") == "EAAB...5678"


def test_mask_token_short():
    assert _mask_token("abc") == "***"


def test_mask_token_empty():
    assert _mask_token("") == "***"


# ── get — happy path ─────────────────────────────────────────────────────────

def test_get_success():
    with patch("urllib.request.urlopen", return_value=_mock_response({"id": "123"})) as mock_open:
        result = get("https://graph.facebook.com/v25.0/123", {}, "token123")
    assert result == {"id": "123"}
    assert mock_open.called


def test_get_passes_access_token_in_url():
    with patch("urllib.request.urlopen", return_value=_mock_response({"id": "1"})) as mock_open:
        get("https://graph.facebook.com/v25.0/123", {"fields": "name"}, "mytoken")
    url_called = mock_open.call_args[0][0].full_url
    assert "access_token=mytoken" in url_called
    assert "fields=name" in url_called


# ── get — auth failures ───────────────────────────────────────────────────────

def test_get_401_raises_api_error_no_retry():
    with patch("urllib.request.urlopen", side_effect=_mock_http_error(401)) as mock_open:
        with pytest.raises(APIError) as exc_info:
            get("https://graph.facebook.com/v25.0/123", {}, "badtoken")
    assert "401" in str(exc_info.value)
    assert mock_open.call_count == 1  # no retry


def test_get_403_raises_api_error_no_retry():
    with patch("urllib.request.urlopen", side_effect=_mock_http_error(403)) as mock_open:
        with pytest.raises(APIError):
            get("https://graph.facebook.com/v25.0/123", {}, "badtoken")
    assert mock_open.call_count == 1


def test_get_auth_error_token_is_masked():
    with patch("urllib.request.urlopen", side_effect=_mock_http_error(401)):
        with pytest.raises(APIError) as exc_info:
            get("https://graph.facebook.com/v25.0/123", {}, "EAABcdef12345678")
    assert "EAABcdef12345678" not in str(exc_info.value)
    assert "EAAB...5678" in str(exc_info.value)


# ── get — rate limit retries ──────────────────────────────────────────────────

def test_get_429_retries_then_succeeds():
    rate_limit_err = _mock_http_error(429)
    success_resp = _mock_response({"id": "123"})
    with patch("urllib.request.urlopen", side_effect=[rate_limit_err, success_resp]):
        with patch("time.sleep") as mock_sleep:
            result = get("https://graph.facebook.com/v25.0/123", {}, "token", max_retries=3)
    assert result == {"id": "123"}
    assert mock_sleep.called


# ── get — network errors retry ───────────────────────────────────────────────

def test_get_network_error_retries():
    import urllib.error
    net_err = urllib.error.URLError("connection refused")
    success_resp = _mock_response({"id": "ok"})
    with patch("urllib.request.urlopen", side_effect=[net_err, success_resp]):
        with patch("time.sleep"):
            result = get("https://graph.facebook.com/v25.0/123", {}, "token", max_retries=3)
    assert result == {"id": "ok"}


def test_get_exhausted_retries_raises_api_error():
    import urllib.error
    net_err = urllib.error.URLError("always fails")
    with patch("urllib.request.urlopen", side_effect=[net_err, net_err, net_err]):
        with patch("time.sleep"):
            with pytest.raises(APIError, match="3 attempts"):
                get("https://graph.facebook.com/v25.0/123", {}, "token", max_retries=3)
