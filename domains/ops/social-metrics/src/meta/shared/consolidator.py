"""
consolidator.py — Merges Facebook + Instagram extractor results into a BrandResult.

BrandResult is a plain dict with these keys:
    account_summary   dict
    content_summary   dict
    audience_summary  dict
    messages_summary  dict
    top_content       list[dict]  — top 5 posts, ranked by reach→views→engagement→timestamp
    flat_rows         list[dict]  — one row per metric per post/account, for CSV

None inputs produce null-filled structures. No KeyErrors.
"""

from typing import Any

from src.config.meta_config import BrandConfig


def _ranking_score(post: dict) -> tuple:
    """Sort key: (reach, views, engagement, timestamp). All descending."""
    reach = post.get("reach") or 0
    views = post.get("views") or 0
    engagement = (
        (post.get("likes") or 0)
        + (post.get("comments") or 0)
        + (post.get("shares") or 0)
        + (post.get("saved") or 0)
    )
    ts = post.get("timestamp") or "0"
    return (reach, views, engagement, ts)


def _sum_ig_reach(account_insights: dict | None) -> int | None:
    """Sum daily reach values from the IG account insights time series."""
    if not account_insights:
        return None
    for item in account_insights.get("data", []):
        if item.get("name") == "reach":
            return sum(
                v.get("value", 0)
                for v in item.get("values", [])
                if isinstance(v.get("value"), (int, float))
            )
    return None


def _build_ig_posts(ig: dict) -> list[dict]:
    """Build a unified post list from IG media + media_insights."""
    posts = []
    for item in ig.get("media", []):
        mid = item["id"]
        ins = ig.get("media_insights", {}).get(mid) or {}
        posts.append({
            "platform": "instagram",
            "media_id": mid,
            "media_type": item.get("media_type"),
            "media_product_type": item.get("media_product_type"),
            "permalink": item.get("permalink"),
            "timestamp": item.get("timestamp"),
            "caption": item.get("caption", ""),
            "likes": item.get("like_count") or ins.get("likes"),
            "comments": item.get("comments_count") or ins.get("comments"),
            "shares": ins.get("shares"),
            "saved": ins.get("saved"),
            "views": ins.get("views"),
            "reach": ins.get("reach"),
        })
    return posts


def _build_fb_posts(fb: dict) -> list[dict]:
    """Build a unified post list from FB posts + post_insights."""
    posts = []
    for item in fb.get("posts", []):
        pid = item["id"]
        ins = fb.get("post_insights", {}).get(pid) or {}
        media_type = None
        attachments = item.get("attachments", {}).get("data", [])
        if attachments:
            media_type = attachments[0].get("media_type")
        posts.append({
            "platform": "facebook",
            "media_id": pid,
            "media_type": media_type,
            "media_product_type": None,
            "permalink": item.get("permalink_url"),
            "timestamp": item.get("created_time"),
            "caption": item.get("message") or item.get("story", ""),
            "likes": (item.get("likes") or {}).get("summary", {}).get("total_count"),
            "comments": (item.get("comments") or {}).get("summary", {}).get("total_count"),
            "shares": (item.get("shares") or {}).get("count"),
            "saved": None,
            "views": None,
            "reach": ins.get("post_impressions_unique") or ins.get("post_impressions"),
        })
    return posts


def _build_flat_rows(
    brand: BrandConfig,
    month_str: str,
    all_posts: list[dict],
    account_summary: dict,
) -> list[dict]:
    """Build flat rows for CSV export."""
    rows = []

    # Account-level rows
    fb_acc = account_summary.get("facebook") or {}
    ig_acc = account_summary.get("instagram") or {}

    for metric, value in {
        "fb_followers": fb_acc.get("followers"),
        "fb_reach": fb_acc.get("reach"),
        "fb_impressions": fb_acc.get("impressions"),
        "fb_engaged_users": fb_acc.get("engaged_users"),
        "ig_followers": ig_acc.get("followers"),
        "ig_monthly_reach": ig_acc.get("monthly_reach"),
    }.items():
        rows.append({
            "brand": brand.slug,
            "month": month_str,
            "platform": "facebook" if metric.startswith("fb_") else "instagram",
            "source_type": "account",
            "entity_id": fb_acc.get("page_id") if metric.startswith("fb_") else ig_acc.get("ig_id"),
            "entity_name": brand.display_name,
            "media_id": None,
            "media_type": None,
            "media_product_type": None,
            "metric_name": metric,
            "metric_value": value,
            "date": None,
            "permalink": None,
            "timestamp": None,
            "caption_snippet": None,
        })

    # Post-level rows
    post_metrics = ["reach", "views", "likes", "comments", "shares", "saved"]
    for post in all_posts:
        for metric in post_metrics:
            value = post.get(metric)
            if value is None:
                continue
            rows.append({
                "brand": brand.slug,
                "month": month_str,
                "platform": post["platform"],
                "source_type": "post",
                "entity_id": post["media_id"],
                "entity_name": brand.display_name,
                "media_id": post["media_id"],
                "media_type": post.get("media_type"),
                "media_product_type": post.get("media_product_type"),
                "metric_name": metric,
                "metric_value": value,
                "date": (post.get("timestamp") or "")[:10] or None,
                "permalink": post.get("permalink"),
                "timestamp": post.get("timestamp"),
                "caption_snippet": (post.get("caption") or "")[:100],
            })

    return rows


def consolidate(
    fb: dict | None,
    ig: dict | None,
    brand: BrandConfig,
    month_str: str,
    start_date: str,
    end_date: str,
) -> dict[str, Any]:
    """
    Merge Facebook and Instagram extractor results into a BrandResult.

    Either input may be None (e.g. FB critical failure). The result always has
    all 6 keys; None inputs produce null-filled sub-structures.
    """
    # ── Account summary ───────────────────────────────────────────────────────
    fb_acc = None
    if fb:
        page = fb.get("page") or {}
        ins = fb.get("insights") or {}
        fb_acc = {
            "page_id": page.get("id"),
            "page_name": page.get("name"),
            "followers": page.get("followers_count"),
            "fan_count": page.get("fan_count"),
            "reach": ins.get("page_reach"),
            "impressions": ins.get("page_impressions"),
            "engaged_users": ins.get("page_engaged_users"),
            "impressions_unique": ins.get("page_impressions_unique"),
            "fan_adds": ins.get("page_fan_adds"),
        }

    ig_acc = None
    if ig:
        acct = ig.get("account") or {}
        ig_acc = {
            "ig_id": acct.get("id"),
            "username": acct.get("username"),
            "followers": acct.get("followers_count"),
            "follows": acct.get("follows_count"),
            "media_count": acct.get("media_count"),
            "monthly_reach": _sum_ig_reach(ig.get("account_insights")),
        }

    total_followers = None
    if fb_acc and ig_acc:
        fb_f = fb_acc.get("followers") or 0
        ig_f = ig_acc.get("followers") or 0
        total_followers = fb_f + ig_f
    elif ig_acc:
        total_followers = ig_acc.get("followers")
    elif fb_acc:
        total_followers = fb_acc.get("followers")

    account_summary = {
        "brand": brand.slug,
        "display_name": brand.display_name,
        "month": month_str,
        "date_range": {"start": start_date, "end": end_date},
        "facebook": fb_acc,
        "instagram": ig_acc,
        "consolidated": {
            "total_followers": total_followers,
            "total_reach": (
                (fb_acc.get("reach") or 0 if fb_acc else 0)
                + (ig_acc.get("monthly_reach") or 0 if ig_acc else 0)
            ) or None,
        },
    }

    # ── All posts (combined) ──────────────────────────────────────────────────
    all_posts: list[dict] = []
    ig_posts: list[dict] = []
    fb_posts: list[dict] = []

    if ig:
        ig_posts = _build_ig_posts(ig)
        all_posts.extend(ig_posts)
    if fb:
        fb_posts = _build_fb_posts(fb)
        all_posts.extend(fb_posts)

    # ── Content summary ───────────────────────────────────────────────────────
    def _safe_sum(items, key):
        vals = [p.get(key) for p in items if p.get(key) is not None]
        return sum(vals) if vals else None

    def _avg_engagement(posts):
        rates = []
        for p in posts:
            reach = p.get("reach") or 0
            if not reach:
                continue
            eng = (
                (p.get("likes") or 0)
                + (p.get("comments") or 0)
                + (p.get("shares") or 0)
                + (p.get("saved") or 0)
            )
            rates.append(eng / reach)
        return round(sum(rates) / len(rates), 4) if rates else None

    ig_reels = [p for p in ig_posts if p.get("media_product_type") == "REELS"] if ig_posts else []

    content_summary = {
        "brand": brand.slug,
        "month": month_str,
        "facebook": {
            "posts_published": len(fb_posts),
            "total_likes": _safe_sum(fb_posts, "likes"),
            "total_comments": _safe_sum(fb_posts, "comments"),
            "total_shares": _safe_sum(fb_posts, "shares"),
            "total_reach": _safe_sum(fb_posts, "reach"),
            "avg_engagement_rate": _avg_engagement(fb_posts),
        } if fb_posts else None,
        "instagram": {
            "posts_published": len([p for p in ig_posts if p.get("media_product_type") != "REELS"]),
            "reels_published": len(ig_reels),
            "total_likes": _safe_sum(ig_posts, "likes"),
            "total_comments": _safe_sum(ig_posts, "comments"),
            "total_saves": _safe_sum(ig_posts, "saved"),
            "total_reach": _safe_sum(ig_posts, "reach"),
            "avg_engagement_rate": _avg_engagement(ig_posts),
        } if ig_posts else None,
        "consolidated": {
            "total_posts": len(all_posts),
            "total_reach": _safe_sum(all_posts, "reach"),
        },
    }

    # ── Audience summary ──────────────────────────────────────────────────────
    audience_summary = {
        "brand": brand.slug,
        "month": month_str,
        "facebook": {
            "followers_end_of_period": fb_acc.get("followers") if fb_acc else None,
            "fan_count": fb_acc.get("fan_count") if fb_acc else None,
            "fan_adds_in_period": fb_acc.get("fan_adds") if fb_acc else None,
            "demographics": None,
        } if fb_acc else None,
        "instagram": {
            "followers_end_of_period": ig_acc.get("followers") if ig_acc else None,
            "follows_count": ig_acc.get("follows") if ig_acc else None,
            "demographics": None,
        } if ig_acc else None,
        "note": (
            "Audience demographics (age, gender, location) require additional "
            "API permissions not available in Phase 1."
        ),
    }

    # ── Messages summary ──────────────────────────────────────────────────────
    messages_summary = {
        "brand": brand.slug,
        "month": month_str,
        "facebook": {
            "status": "pending",
            "note": (
                "Facebook inbox metrics require pages_messaging permission "
                "with additional setup. Planned for Phase 2."
            ),
        },
        "instagram": {
            "status": "pending",
            "note": (
                "Instagram DM metrics require business_management permission. "
                "Planned for Phase 2."
            ),
        },
    }

    # ── Top content ───────────────────────────────────────────────────────────
    ranked = sorted(all_posts, key=_ranking_score, reverse=True)[:5]
    top_content = []
    for i, post in enumerate(ranked, start=1):
        top_content.append({
            "rank": i,
            "platform": post["platform"],
            "media_id": post["media_id"],
            "media_type": post.get("media_type"),
            "media_product_type": post.get("media_product_type"),
            "permalink": post.get("permalink"),
            "timestamp": post.get("timestamp"),
            "caption_snippet": (post.get("caption") or "")[:150],
            "likes": post.get("likes"),
            "comments": post.get("comments"),
            "shares": post.get("shares"),
            "saved": post.get("saved"),
            "views": post.get("views"),
            "reach": post.get("reach"),
            "ranking_score": _ranking_score(post)[0],  # reach used for ranking
        })

    # ── Flat rows ─────────────────────────────────────────────────────────────
    flat_rows = _build_flat_rows(brand, month_str, all_posts, account_summary)

    return {
        "account_summary": account_summary,
        "content_summary": content_summary,
        "audience_summary": audience_summary,
        "messages_summary": messages_summary,
        "top_content": top_content,
        "flat_rows": flat_rows,
    }
