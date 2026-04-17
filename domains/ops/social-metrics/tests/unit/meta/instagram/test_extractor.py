from unittest.mock import MagicMock, patch

import pytest

from src.common.http import APIError
from src.config.meta_config import BrandConfig
from src.meta.instagram.extractor import extract

BRAND = BrandConfig(
    slug="discipline_rift",
    display_name="Discipline Rift",
    page_id="111222333",
    page_access_token="PAGE_TOKEN_TEST",
    ig_id="444555666",
)

MOCK_ACCOUNT = {
    "id": "444555666",
    "username": "disciplinerift",
    "name": "Discipline Rift",
    "followers_count": 5000,
    "follows_count": 120,
    "media_count": 80,
}

MOCK_MEDIA_RESP = {
    "data": [
        {
            "id": "media_1",
            "caption": "Great practice today!",
            "media_type": "IMAGE",
            "media_product_type": "FEED",
            "permalink": "https://www.instagram.com/p/abc123/",
            "timestamp": "2026-04-10T15:00:00+0000",
            "like_count": 45,
            "comments_count": 8,
        },
        {
            "id": "media_2",
            "media_type": "VIDEO",
            "media_product_type": "REELS",
            "permalink": "https://www.instagram.com/reel/xyz789/",
            "timestamp": "2026-03-28T12:00:00+0000",  # outside April window
            "like_count": 200,
            "comments_count": 30,
        },
    ],
    "paging": {},
}

MOCK_ACCOUNT_INSIGHTS = {
    "data": [
        {
            "name": "reach",
            "period": "day",
            "values": [
                {"value": 300, "end_time": "2026-04-02T07:00:00+0000"},
                {"value": 450, "end_time": "2026-04-03T07:00:00+0000"},
            ],
        }
    ]
}

MOCK_MEDIA_INSIGHTS = {
    "data": [
        {"name": "reach", "value": 1200},
        {"name": "saved", "value": 34},
        {"name": "likes", "value": 45},
        {"name": "comments", "value": 8},
        {"name": "shares", "value": 5},
    ]
}


def test_extract_returns_expected_keys():
    with patch("src.meta.instagram.extractor.get") as mock_get:
        mock_get.side_effect = [
            MOCK_ACCOUNT,
            MOCK_MEDIA_RESP,
            MOCK_ACCOUNT_INSIGHTS,
            MOCK_MEDIA_INSIGHTS,  # for media_1 only (media_2 filtered out)
        ]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result is not None
    assert "account" in result
    assert "media" in result
    assert "account_insights" in result
    assert "media_insights" in result


def test_extract_filters_media_to_month():
    with patch("src.meta.instagram.extractor.get") as mock_get:
        mock_get.side_effect = [
            MOCK_ACCOUNT,
            MOCK_MEDIA_RESP,
            MOCK_ACCOUNT_INSIGHTS,
            MOCK_MEDIA_INSIGHTS,
        ]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    # media_2 is from March, should be filtered out
    assert len(result["media"]) == 1
    assert result["media"][0]["id"] == "media_1"


def test_extract_account_data_correct():
    with patch("src.meta.instagram.extractor.get") as mock_get:
        mock_get.side_effect = [
            MOCK_ACCOUNT,
            MOCK_MEDIA_RESP,
            MOCK_ACCOUNT_INSIGHTS,
            MOCK_MEDIA_INSIGHTS,
        ]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result["account"]["followers_count"] == 5000
    assert result["account"]["username"] == "disciplinerift"


def test_extract_critical_failure_returns_none():
    with patch("src.meta.instagram.extractor.get") as mock_get:
        mock_get.side_effect = APIError("Auth error 401 (token: PAGE...TEST): Invalid token", 401)
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result is None


def test_extract_media_failure_returns_result_with_empty_media():
    with patch("src.meta.instagram.extractor.get") as mock_get:
        mock_get.side_effect = [
            MOCK_ACCOUNT,
            APIError("403 Forbidden", 403),  # media call fails
            MOCK_ACCOUNT_INSIGHTS,           # account insights still attempted
            # no media_insights calls — media list is empty
        ]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    # Should not return None — media failure is non-critical
    assert result is not None
    assert result["media"] == []


def test_extract_media_insights_failure_continues():
    with patch("src.meta.instagram.extractor.get") as mock_get:
        mock_get.side_effect = [
            MOCK_ACCOUNT,
            MOCK_MEDIA_RESP,
            MOCK_ACCOUNT_INSIGHTS,
            APIError("Error getting insights", 400),  # per-media insights fails
        ]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result is not None
    # media_insights for media_1 should be empty dict (failed gracefully)
    assert result["media_insights"].get("media_1") is None or result["media_insights"].get("media_1") == {}
