"""
instagram/extractor.py — Instagram organic metrics extractor.

Uses the validated IG Graph API endpoints. All calls use the brand's
Page Access Token, which is valid for linked Instagram Business accounts.

Critical failure (None return): account call returns 401/403.
Partial failures: logged as warnings, field set to None/empty, pipeline continues.
"""

import logging
import urllib.parse
from typing import Any

from src.common.http import APIError, get
from src.config.meta_config import BrandConfig

logger = logging.getLogger(__name__)

BASE_URL = "https://graph.facebook.com"


def _extract_metric_value(item: dict) -> int | float | None:
    """Extract the scalar value from a Graph API insights metric dict."""
    if "value" in item:
        return item["value"]
    values = item.get("values", [])
    if values and isinstance(values, list):
        return values[0].get("value")
    return None


def extract(
    brand: BrandConfig,
    start_date: str,
    end_date: str,
    api_version: str = "v25.0",
) -> dict[str, Any] | None:
    """
    Extract Instagram organic metrics for a brand over a calendar month.

    Args:
        brand: Brand credentials and identifiers.
        start_date: ISO date string (YYYY-MM-DD), first day of month.
        end_date: ISO date string (YYYY-MM-DD), last day of month.
        api_version: Meta Graph API version string.

    Returns:
        Dict with keys: account, media, account_insights, media_insights.
        Returns None only on critical auth failure (cannot proceed without account data).
    """
    token = brand.page_access_token
    ig_id = brand.ig_id
    base = f"{BASE_URL}/{api_version}"

    # ── Account (critical) ────────────────────────────────────────────────────
    try:
        account = get(
            f"{base}/{ig_id}",
            {"fields": "id,username,name,followers_count,follows_count,media_count"},
            token,
        )
    except APIError as e:
        logger.error(f"[{brand.slug}] IG: critical failure on account call — {e}")
        return None

    # ── Media (all pages, filtered to month window) ───────────────────────────
    media_items: list[dict] = []
    try:
        resp = get(
            f"{base}/{ig_id}/media",
            {
                "fields": (
                    "id,caption,media_type,media_product_type,"
                    "permalink,timestamp,like_count,comments_count"
                ),
                "limit": "100",
            },
            token,
        )
        for item in resp.get("data", []):
            ts = item.get("timestamp", "")
            if ts and start_date <= ts[:10] <= end_date:
                media_items.append(item)

        # Paginate while there are more pages and posts are within the window
        while resp.get("paging", {}).get("next"):
            next_url = resp["paging"]["next"]
            parsed = urllib.parse.urlparse(next_url)
            params = dict(urllib.parse.parse_qsl(parsed.query))
            params.pop("access_token", None)
            resp = get(
                f"{parsed.scheme}://{parsed.netloc}{parsed.path}", params, token
            )
            stop_paginating = True
            for item in resp.get("data", []):
                ts = item.get("timestamp", "")
                if ts and ts[:10] >= start_date:
                    if ts[:10] <= end_date:
                        media_items.append(item)
                    stop_paginating = False
            # Media comes newest-first; if all items are before window, stop
            if stop_paginating:
                break

    except APIError as e:
        logger.warning(f"[{brand.slug}] IG: media fetch failed — {e}")

    # ── Account insights (reach time series) ─────────────────────────────────
    account_insights: dict | None = None
    try:
        account_insights = get(
            f"{base}/{ig_id}/insights",
            {
                "metric": "reach",
                "period": "day",
                "metric_type": "time_series",
                "since": start_date,
                "until": end_date,
            },
            token,
        )
    except APIError as e:
        logger.warning(f"[{brand.slug}] IG: account insights failed — {e}")

    # ── Media insights (top 50 items in window) ───────────────────────────────
    media_insights: dict[str, dict] = {}
    for item in media_items[:50]:
        mid = item["id"]
        try:
            resp = get(
                f"{base}/{mid}/insights",
                {"metric": "views,reach,saved,likes,comments,shares"},
                token,
            )
            media_insights[mid] = {
                m["name"]: _extract_metric_value(m)
                for m in resp.get("data", [])
            }
        except APIError as e:
            logger.debug(f"[{brand.slug}] IG: media insights for {mid} failed — {e}")

    return {
        "account": account,
        "media": media_items,
        "account_insights": account_insights,
        "media_insights": media_insights,
    }
