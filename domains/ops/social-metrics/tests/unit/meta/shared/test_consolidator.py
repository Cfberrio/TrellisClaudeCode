import pytest
from src.meta.shared.consolidator import consolidate
from src.config.meta_config import BrandConfig

BRAND = BrandConfig(
    slug="discipline_rift",
    display_name="Discipline Rift",
    page_id="111",
    page_access_token="token",
    ig_id="444",
)

FB = {
    "page": {"id": "111", "name": "Discipline Rift", "fan_count": 1200, "followers_count": 1180},
    "insights": {
        "page_impressions": 45000,
        "page_reach": 22000,
        "page_engaged_users": 3400,
        "page_impressions_unique": 18000,
        "page_fan_adds": 35,
    },
    "posts": [
        {
            "id": "post_1",
            "message": "Season starts now!",
            "created_time": "2026-04-05T14:00:00+0000",
            "permalink_url": "https://facebook.com/post_1",
            "attachments": {"data": [{"media_type": "photo"}]},
            "likes": {"summary": {"total_count": 34}},
            "comments": {"summary": {"total_count": 6}},
            "shares": {"count": 3},
        }
    ],
    "post_insights": {
        "post_1": {
            "post_impressions": 500,
            "post_impressions_unique": 420,
            "post_engaged_users": 40,
            "post_clicks": 15,
        }
    },
}

IG = {
    "account": {
        "id": "444",
        "username": "disciplinerift",
        "followers_count": 5000,
        "follows_count": 120,
        "media_count": 80,
    },
    "media": [
        {
            "id": "media_1",
            "caption": "Great session!",
            "media_type": "IMAGE",
            "media_product_type": "FEED",
            "permalink": "https://instagram.com/p/abc/",
            "timestamp": "2026-04-10T15:00:00+0000",
            "like_count": 150,
            "comments_count": 20,
        },
        {
            "id": "media_2",
            "media_type": "VIDEO",
            "media_product_type": "REELS",
            "permalink": "https://instagram.com/reel/xyz/",
            "timestamp": "2026-04-18T10:00:00+0000",
            "like_count": 300,
            "comments_count": 45,
        },
    ],
    "account_insights": {
        "data": [
            {
                "name": "reach",
                "values": [
                    {"value": 800, "end_time": "2026-04-02T07:00:00+0000"},
                    {"value": 950, "end_time": "2026-04-03T07:00:00+0000"},
                ],
            }
        ]
    },
    "media_insights": {
        "media_1": {"reach": 1200, "saved": 34, "likes": 150, "comments": 20, "shares": 8},
        "media_2": {"reach": 3500, "saved": 80, "likes": 300, "comments": 45, "shares": 22, "views": 8000},
    },
}


def test_consolidate_returns_all_keys():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    assert "account_summary" in result
    assert "content_summary" in result
    assert "audience_summary" in result
    assert "messages_summary" in result
    assert "top_content" in result
    assert "flat_rows" in result


def test_account_summary_has_brand_and_month():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    s = result["account_summary"]
    assert s["brand"] == "discipline_rift"
    assert s["month"] == "2026-04"


def test_account_summary_facebook_followers():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    assert result["account_summary"]["facebook"]["followers"] == 1180


def test_account_summary_instagram_followers():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    assert result["account_summary"]["instagram"]["followers"] == 5000


def test_account_summary_consolidated_total_followers():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    assert result["account_summary"]["consolidated"]["total_followers"] == 6180


def test_top_content_has_at_most_5_items():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    assert len(result["top_content"]) <= 5


def test_top_content_ranked_by_reach():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    top = result["top_content"]
    reaches = [p.get("reach") or 0 for p in top]
    assert reaches == sorted(reaches, reverse=True)


def test_top_content_has_platform_field():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    for post in result["top_content"]:
        assert post["platform"] in ("facebook", "instagram")


def test_consolidate_with_fb_none():
    result = consolidate(None, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    assert result is not None
    assert result["account_summary"]["facebook"] is None


def test_flat_rows_have_required_fields():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    assert len(result["flat_rows"]) > 0
    for row in result["flat_rows"]:
        assert "brand" in row
        assert "month" in row
        assert "platform" in row
        assert "metric_name" in row
        assert "metric_value" in row
