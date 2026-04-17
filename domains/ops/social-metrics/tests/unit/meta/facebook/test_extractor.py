from unittest.mock import patch

import pytest

from src.common.http import APIError
from src.config.meta_config import BrandConfig
from src.meta.facebook.extractor import extract

BRAND = BrandConfig(
    slug="discipline_rift",
    display_name="Discipline Rift",
    page_id="111222333",
    page_access_token="PAGE_TOKEN_TEST",
    ig_id="444555666",
)

MOCK_PAGE = {
    "id": "111222333",
    "name": "Discipline Rift",
    "fan_count": 1200,
    "followers_count": 1180,
    "about": "Youth sports.",
}

MOCK_INSIGHTS = {
    "data": [
        {
            "name": "page_impressions",
            "period": "month",
            "values": [{"value": 45000, "end_time": "2026-04-30T07:00:00+0000"}],
        },
        {
            "name": "page_reach",
            "period": "month",
            "values": [{"value": 22000, "end_time": "2026-04-30T07:00:00+0000"}],
        },
        {
            "name": "page_engaged_users",
            "period": "month",
            "values": [{"value": 3400, "end_time": "2026-04-30T07:00:00+0000"}],
        },
    ]
}

MOCK_POSTS = {
    "data": [
        {
            "id": "post_1",
            "message": "Season starts now!",
            "created_time": "2026-04-05T14:00:00+0000",
            "permalink_url": "https://www.facebook.com/permalink/post_1",
            "attachments": {"data": [{"media_type": "photo"}]},
            "likes": {"summary": {"total_count": 34}},
            "comments": {"summary": {"total_count": 6}},
            "shares": {"count": 3},
        }
    ],
    "paging": {},
}

MOCK_POST_INSIGHTS = {
    "data": [
        {"name": "post_impressions", "values": [{"value": 500}]},
        {"name": "post_impressions_unique", "values": [{"value": 420}]},
        {"name": "post_engaged_users", "values": [{"value": 40}]},
        {"name": "post_clicks", "values": [{"value": 15}]},
    ]
}


def test_extract_returns_expected_keys():
    with patch("src.meta.facebook.extractor.get") as mock_get:
        mock_get.side_effect = [
            MOCK_PAGE,
            MOCK_INSIGHTS,
            MOCK_POSTS,
            MOCK_POST_INSIGHTS,
        ]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result is not None
    assert "page" in result
    assert "insights" in result
    assert "posts" in result
    assert "post_insights" in result


def test_extract_page_data_correct():
    with patch("src.meta.facebook.extractor.get") as mock_get:
        mock_get.side_effect = [MOCK_PAGE, MOCK_INSIGHTS, MOCK_POSTS, MOCK_POST_INSIGHTS]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result["page"]["name"] == "Discipline Rift"
    assert result["page"]["fan_count"] == 1200


def test_extract_critical_failure_on_page_returns_none():
    with patch("src.meta.facebook.extractor.get") as mock_get:
        mock_get.side_effect = APIError("Auth error 401", 401)
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result is None


def test_extract_insights_failure_returns_result_with_none_insights():
    with patch("src.meta.facebook.extractor.get") as mock_get:
        mock_get.side_effect = [
            MOCK_PAGE,
            APIError("Insights unavailable", 400),  # insights fails
            APIError("Posts unavailable", 400),      # posts also fails (next call)
        ]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result is not None
    assert result["insights"] is None
    assert result["posts"] == []


def test_extract_post_insights_failure_continues():
    with patch("src.meta.facebook.extractor.get") as mock_get:
        mock_get.side_effect = [
            MOCK_PAGE,
            MOCK_INSIGHTS,
            MOCK_POSTS,
            APIError("Post insights unavailable", 400),
        ]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result is not None
    assert len(result["posts"]) == 1
    # Post insights for post_1 should be None or empty
    assert result["post_insights"].get("post_1") is None or result["post_insights"].get("post_1") == {}


def test_extract_insights_parses_metric_values():
    with patch("src.meta.facebook.extractor.get") as mock_get:
        mock_get.side_effect = [MOCK_PAGE, MOCK_INSIGHTS, MOCK_POSTS, MOCK_POST_INSIGHTS]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result["insights"]["page_impressions"] == 45000
    assert result["insights"]["page_reach"] == 22000
