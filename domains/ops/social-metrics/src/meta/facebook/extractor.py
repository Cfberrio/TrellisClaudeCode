"""
facebook/extractor.py — Facebook Page organic metrics extractor.

All extraction is best-effort except the initial page call.
page_impressions_unique and page_fan_adds are optional — None if unavailable.

Critical failure (None return): page call returns 401/403 (bad token).
"""

import logging
from typing import Any

from src.common.http import APIError, get
from src.config.meta_config import BrandConfig

logger = logging.getLogger(__name__)

BASE_URL = "https://graph.facebook.com"


def _extract_insights_values(data: list[dict]) -> dict[str, Any]:
    """Parse a list of insights metric dicts into {metric_name: value}."""
    result: dict[str, Any] = {}
    for item in data:
        name = item.get("name")
        if not name:
            continue
        values = item.get("values", [])
        if values and isinstance(values[0].get("value"), (int, float)):
            # Sum all values in the window (handles period=day cases)
            result[name] = sum(
                v.get("value", 0) for v in values
                if isinstance(v.get("value"), (int, float))
            )
        elif "value" in item:
            result[name] = item["value"]
    return result


def extract(
    brand: BrandConfig,
    start_date: str,
    end_date: str,
    api_version: str = "v25.0",
) -> dict[str, Any] | None:
    """
    Extract Facebook Page organic metrics for a brand over a calendar month.

    Args:
        brand: Brand credentials and identifiers.
        start_date: ISO date string (YYYY-MM-DD), first day of month.
        end_date: ISO date string (YYYY-MM-DD), last day of month.
        api_version: Meta Graph API version string.

    Returns:
        Dict with keys: page, insights, posts, post_insights.
        Returns None only on critical auth failure on the page call.
    """
    token = brand.page_access_token
    page_id = brand.page_id
    base = f"{BASE_URL}/{api_version}"

    # ── Page base (critical) ──────────────────────────────────────────────────
    try:
        page = get(
            f"{base}/{page_id}",
            {"fields": "id,name,fan_count,followers_count,about"},
            token,
        )
    except APIError as e:
        logger.error(f"[{brand.slug}] FB: critical failure on page call — {e}")
        return None

    # ── Page insights (best-effort) ───────────────────────────────────────────
    insights: dict | None = None
    try:
        resp = get(
            f"{base}/{page_id}/insights",
            {
                "metric": (
                    "page_impressions,page_reach,page_engaged_users,"
                    "page_impressions_unique,page_fan_adds"
                ),
                "period": "month",
                "since": start_date,
                "until": end_date,
            },
            token,
        )
        insights = _extract_insights_values(resp.get("data", []))
    except APIError as e:
        logger.warning(f"[{brand.slug}] FB: page insights failed — {e}")

    # ── Posts in window (best-effort) ─────────────────────────────────────────
    posts: list[dict] = []
    try:
        resp = get(
            f"{base}/{page_id}/posts",
            {
                "fields": (
                    "id,message,story,created_time,permalink_url,"
                    "attachments{media_type},"
                    "likes.summary(true),comments.summary(true),shares"
                ),
                "since": start_date,
                "until": end_date,
                "limit": "100",
            },
            token,
        )
        posts = resp.get("data", [])
    except APIError as e:
        logger.warning(f"[{brand.slug}] FB: posts fetch failed — {e}")

    # ── Per-post insights (top 25, best-effort) ───────────────────────────────
    post_insights: dict[str, dict] = {}
    for post in posts[:25]:
        pid = post["id"]
        try:
            resp = get(
                f"{base}/{pid}/insights",
                {
                    "metric": (
                        "post_impressions,post_impressions_unique,"
                        "post_engaged_users,post_clicks"
                    )
                },
                token,
            )
            post_insights[pid] = _extract_insights_values(resp.get("data", []))
        except APIError as e:
            logger.debug(f"[{brand.slug}] FB: post insights for {pid} failed — {e}")

    return {
        "page": page,
        "insights": insights,
        "posts": posts,
        "post_insights": post_insights,
    }
