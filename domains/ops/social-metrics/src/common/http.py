"""
http.py — HTTP client for the Meta Graph API.

Uses stdlib urllib only. Implements retry with exponential backoff.
Masks access tokens in all log output and error messages.
"""

import json
import logging
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

logger = logging.getLogger(__name__)


def _ssl_context() -> ssl.SSLContext:
    """Return an SSL context using certifi's CA bundle when available."""
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()

# Meta Graph API error codes that indicate rate limiting
_RATE_LIMIT_CODES = {4, 17, 32, 613}

# Meta Graph API error codes that indicate auth failure
_AUTH_ERROR_CODES = {102, 190, 10}


class APIError(Exception):
    """Unrecoverable API error (auth failure, exhausted retries, etc.)."""

    def __init__(self, message: str, status_code: int | None = None):
        super().__init__(message)
        self.status_code = status_code


def _mask_token(token: str) -> str:
    """Return a masked representation of an access token for safe logging."""
    if not token or len(token) <= 8:
        return "***"
    return token[:4] + "..." + token[-4:]


def get(
    url: str,
    params: dict[str, str],
    access_token: str,
    timeout: int = 30,
    max_retries: int = 3,
) -> dict[str, Any]:
    """
    Make a GET request to the Meta Graph API.

    Appends access_token to params. Retries on transient errors (5xx, network
    timeouts, rate limits) with exponential backoff. Raises APIError on auth
    failures (401/403) or after exhausting retries.

    The access_token is never logged or included in error messages.
    """
    all_params = {**params, "access_token": access_token}
    full_url = url + "?" + urllib.parse.urlencode(all_params)
    req = urllib.request.Request(full_url)

    last_error: Exception | None = None

    ctx = _ssl_context()

    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                return json.loads(resp.read().decode("utf-8"))

        except urllib.error.HTTPError as e:
            body: dict = {}
            try:
                body = json.loads(e.read().decode("utf-8"))
            except Exception:
                pass

            error = body.get("error", {})
            code = error.get("code", 0)
            msg = error.get("message", str(e))

            # Auth failures — never retry
            if e.code in (401, 403) or code in _AUTH_ERROR_CODES:
                masked = _mask_token(access_token)
                raise APIError(
                    f"Auth error {e.code} (token: {masked}): {msg}",
                    status_code=e.code,
                )

            # Rate limit — back off and retry
            if e.code == 429 or code in _RATE_LIMIT_CODES:
                wait = 5 * (2 ** attempt)
                logger.warning(
                    f"Rate limit hit (attempt {attempt + 1}/{max_retries}), "
                    f"backing off {wait}s"
                )
                time.sleep(wait)
                last_error = e
                continue

            # Other 4xx — don't retry
            if 400 <= e.code < 500:
                raise APIError(
                    f"Client error {e.code}: {msg}",
                    status_code=e.code,
                )

            # 5xx — retry
            logger.warning(f"Server error {e.code} (attempt {attempt + 1}/{max_retries})")
            time.sleep(2 ** attempt)
            last_error = e

        except (urllib.error.URLError, TimeoutError, OSError) as e:
            logger.warning(f"Network error (attempt {attempt + 1}/{max_retries}): {e}")
            time.sleep(2 ** attempt)
            last_error = e

    raise APIError(
        f"Request failed after {max_retries} attempts for {url}: {last_error}"
    )
