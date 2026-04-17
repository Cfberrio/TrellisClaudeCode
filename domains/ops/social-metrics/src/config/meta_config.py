"""
meta_config.py — Runtime configuration loader for the Meta Social Metrics pipeline.

Responsibilities:
- Reads credentials from environment variables (loaded from .env).
- Groups config by brand using the canonical brand map below.
- Validates all required variables at startup — fails fast before any API call.
- Never exposes full token values in error messages or logs.

Usage:
    from src.config.meta_config import validate_all, load_brand_config, load_app_config

    validate_all()  # call once at pipeline entry point
    app = load_app_config()
    brand = load_brand_config("discipline_rift")
"""

import os
from dataclasses import dataclass


# ─── Token masking ────────────────────────────────────────────────────────────

def _mask(value: str) -> str:
    """Return a safe, masked representation of a secret for logging/errors."""
    if not value:
        return "<empty>"
    if len(value) <= 8:
        return "***"
    return value[:4] + "..." + value[-4:]


# ─── Config dataclasses ───────────────────────────────────────────────────────

@dataclass(frozen=True)
class MetaAppConfig:
    """App-level Meta credentials, shared across all brands."""
    app_id: str
    app_secret: str
    configuration_id: str
    user_access_token: str


@dataclass(frozen=True)
class BrandConfig:
    """Per-brand Meta credentials and identifiers."""
    slug: str
    display_name: str
    page_id: str
    page_access_token: str
    ig_id: str


# ─── Brand map ────────────────────────────────────────────────────────────────
# Maps brand slugs to their env variable names.
# Values here are KEY NAMES, not secrets.

BRAND_ENV_MAP: dict[str, dict[str, str]] = {
    "cheese_to_share": {
        "display_name": "Cheese To Share",
        "page_id_key":    "SOCIAL_METRICS_CHEESE_TO_SHARE_PAGE_ID",
        "page_token_key": "SOCIAL_METRICS_CHEESE_TO_SHARE_PAGE_ACCESS_TOKEN",
        "ig_id_key":      "SOCIAL_METRICS_CHEESE_TO_SHARE_IG_ID",
    },
    "discipline_rift": {
        "display_name": "Discipline Rift",
        "page_id_key":    "SOCIAL_METRICS_DISCIPLINE_RIFT_PAGE_ID",
        "page_token_key": "SOCIAL_METRICS_DISCIPLINE_RIFT_PAGE_ACCESS_TOKEN",
        "ig_id_key":      "SOCIAL_METRICS_DISCIPLINE_RIFT_IG_ID",
    },
    "dr_volleyball_club": {
        "display_name": "DR Volleyball Club",
        "page_id_key":    "SOCIAL_METRICS_DR_VOLLEYBALL_CLUB_PAGE_ID",
        "page_token_key": "SOCIAL_METRICS_DR_VOLLEYBALL_CLUB_PAGE_ACCESS_TOKEN",
        "ig_id_key":      "SOCIAL_METRICS_DR_VOLLEYBALL_CLUB_IG_ID",
    },
}

# App-level required vars (not brand-specific)
# Prefixed with SOCIAL_METRICS_ to avoid collision with other Meta projects in the workspace.
REQUIRED_APP_VARS: list[str] = [
    "SOCIAL_METRICS_META_APP_ID",
    "SOCIAL_METRICS_META_APP_SECRET",
    "SOCIAL_METRICS_META_CONFIGURATION_ID",
    "SOCIAL_METRICS_META_USER_ACCESS_TOKEN",
]


# ─── Internal helpers ─────────────────────────────────────────────────────────

def _require(key: str) -> str:
    """Get a required env var or raise with a safe, non-exposing error."""
    value = os.getenv(key, "").strip()
    if not value:
        raise EnvironmentError(
            f"Missing required environment variable: {key}\n"
            f"Set it in your .env file. See .env.example for all required keys."
        )
    return value


# ─── Public API ───────────────────────────────────────────────────────────────

def validate_all() -> None:
    """
    Validate all required environment variables without returning their values.

    Call this once at pipeline entry point to fail fast before making API calls.
    Raises EnvironmentError with a clear, non-exposing message listing every
    missing variable.
    """
    errors: list[str] = []

    missing_app = [k for k in REQUIRED_APP_VARS if not os.getenv(k, "").strip()]
    if missing_app:
        errors.append(f"App credentials: {', '.join(missing_app)}")

    for slug, mapping in BRAND_ENV_MAP.items():
        missing_brand = [
            mapping[k]
            for k in ("page_id_key", "page_token_key", "ig_id_key")
            if not os.getenv(mapping[k], "").strip()
        ]
        if missing_brand:
            errors.append(f"Brand '{slug}': {', '.join(missing_brand)}")

    if errors:
        raise EnvironmentError(
            "Configuration validation failed. Missing environment variables:\n"
            + "\n".join(f"  • {e}" for e in errors)
            + "\n\nCopy .env.example to .env and fill in all required values.\n"
            + "See docs/setup.md for step-by-step instructions."
        )


def load_app_config() -> MetaAppConfig:
    """Load and return Meta app-level credentials from environment."""
    return MetaAppConfig(
        app_id=_require("SOCIAL_METRICS_META_APP_ID"),
        app_secret=_require("SOCIAL_METRICS_META_APP_SECRET"),
        configuration_id=_require("SOCIAL_METRICS_META_CONFIGURATION_ID"),
        user_access_token=_require("SOCIAL_METRICS_META_USER_ACCESS_TOKEN"),
    )


def load_brand_config(slug: str) -> BrandConfig:
    """
    Load and return credentials for a specific brand.

    Args:
        slug: One of 'cheese_to_share', 'discipline_rift', 'dr_volleyball_club'

    Raises:
        ValueError: If the slug is not recognized.
        EnvironmentError: If any required env var for the brand is missing.
    """
    if slug not in BRAND_ENV_MAP:
        raise ValueError(
            f"Unknown brand slug: '{slug}'. "
            f"Valid options: {', '.join(BRAND_ENV_MAP.keys())}"
        )
    mapping = BRAND_ENV_MAP[slug]
    return BrandConfig(
        slug=slug,
        display_name=mapping["display_name"],
        page_id=_require(mapping["page_id_key"]),
        page_access_token=_require(mapping["page_token_key"]),
        ig_id=_require(mapping["ig_id_key"]),
    )


def load_all_brands() -> dict[str, BrandConfig]:
    """Load and return credentials for all brands defined in BRAND_ENV_MAP."""
    return {slug: load_brand_config(slug) for slug in BRAND_ENV_MAP}
