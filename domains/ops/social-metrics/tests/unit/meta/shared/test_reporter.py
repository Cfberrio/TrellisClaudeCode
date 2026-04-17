import json
from pathlib import Path

import pytest

from src.config.meta_config import BrandConfig
from src.meta.shared.reporter import write_outputs

BRAND = BrandConfig(
    slug="discipline_rift",
    display_name="Discipline Rift",
    page_id="111",
    page_access_token="token",
    ig_id="444",
)

RESULT = {
    "account_summary": {
        "brand": "discipline_rift",
        "display_name": "Discipline Rift",
        "month": "2026-04",
        "date_range": {"start": "2026-04-01", "end": "2026-04-30"},
        "facebook": {"followers": 1200, "reach": 22000, "impressions": 45000, "engaged_users": 3400},
        "instagram": {"followers": 5000, "monthly_reach": 15000},
        "consolidated": {"total_followers": 6200, "total_reach": 37000},
    },
    "content_summary": {
        "brand": "discipline_rift",
        "month": "2026-04",
        "facebook": {"posts_published": 10, "avg_engagement_rate": 0.025},
        "instagram": {"posts_published": 8, "reels_published": 3, "avg_engagement_rate": 0.038},
        "consolidated": {"total_posts": 21, "total_reach": 37000},
    },
    "audience_summary": {
        "brand": "discipline_rift",
        "month": "2026-04",
        "facebook": {"followers_end_of_period": 1200},
        "instagram": {"followers_end_of_period": 5000},
        "note": "Demographics not available in Phase 1.",
    },
    "messages_summary": {
        "brand": "discipline_rift",
        "month": "2026-04",
        "facebook": {"status": "pending"},
        "instagram": {"status": "pending"},
    },
    "top_content": [
        {
            "rank": 1,
            "platform": "instagram",
            "media_id": "media_1",
            "media_type": "IMAGE",
            "media_product_type": "FEED",
            "permalink": "https://instagram.com/p/abc/",
            "timestamp": "2026-04-10T15:00:00+0000",
            "caption_snippet": "Great session today!",
            "likes": 150,
            "comments": 20,
            "shares": 8,
            "saved": 34,
            "views": None,
            "reach": 3500,
            "ranking_score": 3500,
        }
    ],
    "flat_rows": [
        {
            "brand": "discipline_rift",
            "month": "2026-04",
            "platform": "instagram",
            "source_type": "post",
            "entity_id": "media_1",
            "entity_name": "Discipline Rift",
            "media_id": "media_1",
            "media_type": "IMAGE",
            "media_product_type": "FEED",
            "metric_name": "reach",
            "metric_value": 3500,
            "date": "2026-04-10",
            "permalink": "https://instagram.com/p/abc/",
            "timestamp": "2026-04-10T15:00:00+0000",
            "caption_snippet": "Great session today!",
        }
    ],
}


def test_all_8_files_are_written(tmp_path):
    write_outputs(RESULT, BRAND, "2026-04", tmp_path)
    out = tmp_path / "output" / "meta" / "discipline_rift" / "2026-04"
    expected = [
        "account_summary.json",
        "content_summary.json",
        "audience_summary.json",
        "messages_summary.json",
        "top_content.json",
        "monthly_metrics_flat.csv",
        "monthly_metrics_pretty.xlsx",
        "monthly_analysis.md",
    ]
    for fname in expected:
        assert (out / fname).exists(), f"Missing: {fname}"


def test_account_summary_json_content(tmp_path):
    write_outputs(RESULT, BRAND, "2026-04", tmp_path)
    out = tmp_path / "output" / "meta" / "discipline_rift" / "2026-04"
    data = json.loads((out / "account_summary.json").read_text())
    assert data["brand"] == "discipline_rift"
    assert data["consolidated"]["total_followers"] == 6200


def test_top_content_json_wraps_list(tmp_path):
    write_outputs(RESULT, BRAND, "2026-04", tmp_path)
    out = tmp_path / "output" / "meta" / "discipline_rift" / "2026-04"
    data = json.loads((out / "top_content.json").read_text())
    assert "brand" in data
    assert "month" in data
    assert "top_posts" in data
    assert isinstance(data["top_posts"], list)


def test_monthly_analysis_md_has_required_sections(tmp_path):
    write_outputs(RESULT, BRAND, "2026-04", tmp_path)
    out = tmp_path / "output" / "meta" / "discipline_rift" / "2026-04"
    content = (out / "monthly_analysis.md").read_text()
    required_sections = [
        "Executive Summary",
        "Cross-Platform Snapshot",
        "Facebook Summary",
        "Instagram Summary",
        "Top Content Across Meta",
        "Audience Signals",
        "Messaging / Inbox Signals",
        "Key Takeaways",
        "Recommended Next Steps",
    ]
    for section in required_sections:
        assert section in content, f"Missing section: {section}"


def test_monthly_analysis_md_has_brand_and_month(tmp_path):
    write_outputs(RESULT, BRAND, "2026-04", tmp_path)
    out = tmp_path / "output" / "meta" / "discipline_rift" / "2026-04"
    content = (out / "monthly_analysis.md").read_text()
    assert "Discipline Rift" in content
    assert "2026-04" in content


def test_flat_csv_has_header_row(tmp_path):
    write_outputs(RESULT, BRAND, "2026-04", tmp_path)
    out = tmp_path / "output" / "meta" / "discipline_rift" / "2026-04"
    content = (out / "monthly_metrics_flat.csv").read_text()
    assert "brand" in content
    assert "metric_name" in content
    assert "metric_value" in content
