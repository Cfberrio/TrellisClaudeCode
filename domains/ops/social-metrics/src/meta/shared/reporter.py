"""
reporter.py — Writes the 8 output files for a brand/month from a BrandResult.

Output location: output/meta/{brand_slug}/{YYYY-MM}/

Files written:
    account_summary.json
    content_summary.json
    audience_summary.json
    messages_summary.json
    top_content.json
    monthly_metrics_flat.csv
    monthly_metrics_pretty.xlsx
    monthly_analysis.md
"""

from pathlib import Path
from typing import Any

from src.common.io import (
    FLAT_FIELDNAMES,
    output_dir,
    write_csv,
    write_json,
    write_md,
    write_xlsx,
)
from src.config.meta_config import BrandConfig


def _fmt(value: Any, suffix: str = "", default: str = "Not available") -> str:
    """Format a value for display in the markdown report."""
    if value is None:
        return default
    if isinstance(value, float):
        return f"{value:.1%}{suffix}"
    if isinstance(value, int):
        return f"{value:,}{suffix}"
    return str(value)


def _build_md_report(result: dict, brand: BrandConfig, month_str: str) -> str:
    """Generate the human-readable monthly_analysis.md content."""
    acc = result.get("account_summary") or {}
    con = result.get("content_summary") or {}
    aud = result.get("audience_summary") or {}
    top = result.get("top_content") or []

    fb_acc = acc.get("facebook") or {}
    ig_acc = acc.get("instagram") or {}
    consolidated = acc.get("consolidated") or {}
    fb_con = con.get("facebook") or {}
    ig_con = con.get("instagram") or {}
    con_con = con.get("consolidated") or {}

    year, month = month_str.split("-")
    import calendar
    month_name = calendar.month_name[int(month)]
    _, last_day = calendar.monthrange(int(year), int(month))

    lines = [
        f"# {brand.display_name} — Meta Monthly Report — {month_str}",
        "",
        f"**Period:** {month_name} 1–{last_day}, {year}",
        f"**Generated:** {month_str}",
        "**Platforms:** Facebook + Instagram",
        "",
        "---",
        "",
        "## Executive Summary",
        "",
        (
            f"{brand.display_name} published **{_fmt(con_con.get('total_posts'))} pieces** "
            f"across Meta in {month_name} {year}. "
            f"Combined reach: **{_fmt(consolidated.get('total_reach'))}**. "
            f"Total audience: **{_fmt(consolidated.get('total_followers'))} followers** "
            f"({_fmt(fb_acc.get('followers'))} Facebook, {_fmt(ig_acc.get('followers'))} Instagram)."
        ),
        "",
        "---",
        "",
        "## Cross-Platform Snapshot",
        "",
        "| Metric | Facebook | Instagram | Combined |",
        "|---|---|---|---|",
        f"| Followers | {_fmt(fb_acc.get('followers'))} | {_fmt(ig_acc.get('followers'))} | {_fmt(consolidated.get('total_followers'))} |",
        f"| Monthly Reach | {_fmt(fb_acc.get('reach'))} | {_fmt(ig_acc.get('monthly_reach'))} | {_fmt(consolidated.get('total_reach'))} |",
        f"| Posts Published | {_fmt(fb_con.get('posts_published'))} | {_fmt(ig_con.get('posts_published'))} | {_fmt(con_con.get('total_posts'))} |",
        f"| Avg Engagement Rate | {_fmt(fb_con.get('avg_engagement_rate'))} | {_fmt(ig_con.get('avg_engagement_rate'))} | — |",
        "",
        "---",
        "",
        "## Facebook Summary",
        "",
        "**Account KPIs**",
        f"- Followers: {_fmt(fb_acc.get('followers'))}",
        f"- Fan Count: {_fmt(fb_acc.get('fan_count'))}",
        f"- Monthly Reach: {_fmt(fb_acc.get('reach'))}",
        f"- Monthly Impressions: {_fmt(fb_acc.get('impressions'))}",
        f"- Engaged Users: {_fmt(fb_acc.get('engaged_users'))}",
        "",
        "**Content**",
        f"- Posts published: {_fmt(fb_con.get('posts_published'))}",
        f"- Total likes: {_fmt(fb_con.get('total_likes'))}",
        f"- Total comments: {_fmt(fb_con.get('total_comments'))}",
        f"- Total shares: {_fmt(fb_con.get('total_shares'))}",
        f"- Avg engagement rate: {_fmt(fb_con.get('avg_engagement_rate'))}",
        "",
        "---",
        "",
        "## Instagram Summary",
        "",
        "**Account KPIs**",
        f"- Followers: {_fmt(ig_acc.get('followers'))}",
        f"- Monthly Reach: {_fmt(ig_acc.get('monthly_reach'))}",
        "",
        "**Content**",
        f"- Posts published: {_fmt(ig_con.get('posts_published'))}",
        f"- Reels published: {_fmt(ig_con.get('reels_published'))}",
        f"- Total likes: {_fmt(ig_con.get('total_likes'))}",
        f"- Total comments: {_fmt(ig_con.get('total_comments'))}",
        f"- Total saves: {_fmt(ig_con.get('total_saves'))}",
        f"- Total reach: {_fmt(ig_con.get('total_reach'))}",
        f"- Avg engagement rate: {_fmt(ig_con.get('avg_engagement_rate'))}",
        "",
        "---",
        "",
        "## Top Content Across Meta",
        "",
    ]

    if top:
        lines += [
            "| Rank | Platform | Type | Reach | Engagement | Link |",
            "|---|---|---|---|---|---|",
        ]
        for post in top:
            eng = (
                (post.get("likes") or 0)
                + (post.get("comments") or 0)
                + (post.get("shares") or 0)
                + (post.get("saved") or 0)
            )
            content_type = post.get("media_product_type") or post.get("media_type") or "—"
            permalink = post.get("permalink") or "—"
            link = f"[link]({permalink})" if permalink != "—" else "—"
            lines.append(
                f"| {post['rank']} | {post['platform'].title()} | {content_type} "
                f"| {_fmt(post.get('reach'))} | {_fmt(eng)} | {link} |"
            )
    else:
        lines.append("No content data available.")

    lines += [
        "",
        "---",
        "",
        "## Audience Signals",
        "",
        f"**Facebook:** {_fmt(fb_acc.get('followers'))} followers. "
        f"Fan adds this period: {_fmt(fb_acc.get('fan_adds', None))}.",
        "",
        f"**Instagram:** {_fmt(ig_acc.get('followers'))} followers.",
        "",
        "_Demographic breakdowns (age, gender, location) require additional API permissions. Not available in Phase 1._",
        "",
        "---",
        "",
        "## Messaging / Inbox Signals",
        "",
        "_Facebook and Instagram inbox metrics require additional API permissions. Planned for Phase 2._",
        "",
        "---",
        "",
        "## Key Takeaways",
        "",
        "1. <!-- Fill in after reviewing data -->",
        "2. <!-- Fill in after reviewing data -->",
        "3. <!-- Fill in after reviewing data -->",
        "",
        "---",
        "",
        "## Recommended Next Steps",
        "",
        "- [ ] <!-- Action 1 — Owner — Due date -->",
        "- [ ] <!-- Action 2 -->",
        "- [ ] <!-- Action 3 -->",
    ]

    return "\n".join(lines)


def _build_xlsx_sheets(result: dict, brand: BrandConfig, month_str: str) -> dict[str, list[dict]]:
    """Build the 5 sheets for the xlsx workbook."""
    acc = result.get("account_summary") or {}
    con = result.get("content_summary") or {}
    fb_acc = acc.get("facebook") or {}
    ig_acc = acc.get("instagram") or {}
    consolidated = acc.get("consolidated") or {}
    fb_con = con.get("facebook") or {}
    ig_con = con.get("instagram") or {}
    con_con = con.get("consolidated") or {}

    overview = [
        {"Metric": "Brand", "Facebook": brand.display_name, "Instagram": brand.display_name, "Combined": brand.display_name},
        {"Metric": "Month", "Facebook": month_str, "Instagram": month_str, "Combined": month_str},
        {"Metric": "Followers", "Facebook": fb_acc.get("followers"), "Instagram": ig_acc.get("followers"), "Combined": consolidated.get("total_followers")},
        {"Metric": "Monthly Reach", "Facebook": fb_acc.get("reach"), "Instagram": ig_acc.get("monthly_reach"), "Combined": consolidated.get("total_reach")},
        {"Metric": "Posts Published", "Facebook": fb_con.get("posts_published"), "Instagram": ig_con.get("posts_published"), "Combined": con_con.get("total_posts")},
        {"Metric": "Avg Engagement Rate", "Facebook": fb_con.get("avg_engagement_rate"), "Instagram": ig_con.get("avg_engagement_rate"), "Combined": None},
    ]

    facebook_rows = [
        {"Metric": "Followers", "Value": fb_acc.get("followers")},
        {"Metric": "Fan Count", "Value": fb_acc.get("fan_count")},
        {"Metric": "Monthly Reach", "Value": fb_acc.get("reach")},
        {"Metric": "Monthly Impressions", "Value": fb_acc.get("impressions")},
        {"Metric": "Engaged Users", "Value": fb_acc.get("engaged_users")},
        {"Metric": "Impressions Unique", "Value": fb_acc.get("impressions_unique")},
        {"Metric": "Fan Adds", "Value": fb_acc.get("fan_adds")},
        {"Metric": "Posts Published", "Value": fb_con.get("posts_published")},
        {"Metric": "Avg Engagement Rate", "Value": fb_con.get("avg_engagement_rate")},
    ]

    instagram_rows = [
        {"Metric": "Followers", "Value": ig_acc.get("followers")},
        {"Metric": "Follows Count", "Value": ig_acc.get("follows")},
        {"Metric": "Monthly Reach", "Value": ig_acc.get("monthly_reach")},
        {"Metric": "Posts Published", "Value": ig_con.get("posts_published")},
        {"Metric": "Reels Published", "Value": ig_con.get("reels_published")},
        {"Metric": "Total Likes", "Value": ig_con.get("total_likes")},
        {"Metric": "Total Comments", "Value": ig_con.get("total_comments")},
        {"Metric": "Total Saves", "Value": ig_con.get("total_saves")},
        {"Metric": "Total Reach", "Value": ig_con.get("total_reach")},
        {"Metric": "Avg Engagement Rate", "Value": ig_con.get("avg_engagement_rate")},
    ]

    top_rows = []
    for post in result.get("top_content") or []:
        top_rows.append({
            "Rank": post.get("rank"),
            "Platform": post.get("platform"),
            "Type": post.get("media_product_type") or post.get("media_type"),
            "Timestamp": post.get("timestamp"),
            "Reach": post.get("reach"),
            "Likes": post.get("likes"),
            "Comments": post.get("comments"),
            "Shares": post.get("shares"),
            "Saved": post.get("saved"),
            "Views": post.get("views"),
            "Caption": post.get("caption_snippet"),
            "Permalink": post.get("permalink"),
        })

    return {
        "Overview": overview,
        "Facebook": facebook_rows,
        "Instagram": instagram_rows,
        "Top Content": top_rows,
        "Flat Data": result.get("flat_rows") or [],
    }


def write_outputs(
    result: dict,
    brand: BrandConfig,
    month_str: str,
    base_dir: Path,
) -> None:
    """Write all 8 output files for a brand/month."""
    out = output_dir(base_dir, brand.slug, month_str)

    write_json(out / "account_summary.json", result["account_summary"])
    write_json(out / "content_summary.json", result["content_summary"])
    write_json(out / "audience_summary.json", result["audience_summary"])
    write_json(out / "messages_summary.json", result["messages_summary"])
    write_json(
        out / "top_content.json",
        {"brand": brand.slug, "month": month_str, "top_posts": result["top_content"]},
    )
    write_csv(out / "monthly_metrics_flat.csv", result["flat_rows"], FLAT_FIELDNAMES)
    write_xlsx(out / "monthly_metrics_pretty.xlsx", _build_xlsx_sheets(result, brand, month_str))
    write_md(out / "monthly_analysis.md", _build_md_report(result, brand, month_str))
