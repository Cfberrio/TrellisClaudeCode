#!/bin/bash
# run_meta_phase1_extract.sh — Phase 1 read-only Meta Ads extraction for Discipline Rift.
# Pulls the full decision pack: insights (campaign/adset/ad/placement) + object snapshots.
# Uses only ads_read permission. No ads_management. No mutations.
#
# Usage:
#   ./domains/ads/meta/discipline-rift/scripts/run_meta_phase1_extract.sh

set -euo pipefail

# ── Paths ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOMAIN_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PROJECT_ROOT="$(cd "$DOMAIN_ROOT/../../../.." && pwd)"
OUT_DIR="$DOMAIN_ROOT/data/raw"
RUNNER="$SCRIPT_DIR/run_meta_insights.py"
OBJECTS_RUNNER="$SCRIPT_DIR/run_meta_objects.py"

# ── Resolve .env: domain-local first, then root fallback ──────────────────────
if [ -f "$DOMAIN_ROOT/.env" ]; then
  ENV_FILE="$DOMAIN_ROOT/.env"
  echo "Env source  : domain ($ENV_FILE)"
elif [ -f "$PROJECT_ROOT/.env" ]; then
  ENV_FILE="$PROJECT_ROOT/.env"
  echo "Env source  : root fallback ($ENV_FILE)"
else
  echo "ERROR: No .env found. Tried:" >&2
  echo "  $DOMAIN_ROOT/.env" >&2
  echo "  $PROJECT_ROOT/.env" >&2
  exit 1
fi

# ── Python interpreter ────────────────────────────────────────────────────────
if [ -f "$PROJECT_ROOT/.venv/bin/python" ]; then
  PYTHON="$PROJECT_ROOT/.venv/bin/python"
else
  PYTHON="python3"
fi

# ── Timestamp ─────────────────────────────────────────────────────────────────
TS=$(date +%Y%m%d_%H%M%S)
mkdir -p "$OUT_DIR"

echo "Phase 1 extraction — Meta Ads — Discipline Rift"
echo "Timestamp   : $TS"
echo "Output dir  : $OUT_DIR"
echo "────────────────────────────────────────────────────────────────"

ERRORS=""
GENERATED=""
FAIL=0

# ── SSL cert resolution ───────────────────────────────────────────────────────
CERTIFI=""
if [ -f "$PROJECT_ROOT/.venv/bin/python" ]; then
  CERTIFI=$("$PROJECT_ROOT/.venv/bin/python" -c "import certifi; print(certifi.where())" 2>/dev/null || true)
fi

# ── Helper: run insights ──────────────────────────────────────────────────────
run_insights() {
  local LEVEL="$1"
  local OUTFILE="$2"
  local EXTRA_ARGS="${3:-}"

  OUTPUT=$(SSL_CERT_FILE="${CERTIFI:-}" "$PYTHON" "$RUNNER" \
    --level "$LEVEL" \
    --out "$OUTFILE" \
    --env-file "$ENV_FILE" \
    $EXTRA_ARGS 2>&1) && STATUS=0 || STATUS=$?

  if [ "$STATUS" -ne 0 ]; then
    ERR_MSG=$(echo "$OUTPUT" | grep -i "error" | head -1 || echo "unknown error")
    ERRORS="$ERRORS\n  $LEVEL insights: $ERR_MSG"
    printf "  FAIL  %s insights\n" "$LEVEL"
    FAIL=1
  else
    ROWS=$(echo "$OUTPUT" | grep -oE 'Exported [0-9]+ rows' | grep -oE '[0-9]+' || echo "?")
    GENERATED="$GENERATED\n  $(basename "$OUTFILE")  ($ROWS rows)"
    printf "  OK    %-60s  %s rows\n" "$(basename "$OUTFILE")" "$ROWS"
  fi
}

# ── Helper: run objects ───────────────────────────────────────────────────────
run_objects() {
  local TYPE="$1"
  local OUTFILE="$2"

  OUTPUT=$(SSL_CERT_FILE="${CERTIFI:-}" "$PYTHON" "$OBJECTS_RUNNER" \
    --type "$TYPE" \
    --out "$OUTFILE" \
    --env-file "$ENV_FILE" 2>&1) && STATUS=0 || STATUS=$?

  if [ "$STATUS" -ne 0 ]; then
    ERR_MSG=$(echo "$OUTPUT" | grep -i "error" | head -1 || echo "unknown error")
    ERRORS="$ERRORS\n  $TYPE objects: $ERR_MSG"
    printf "  FAIL  %s objects\n" "$TYPE"
    FAIL=1
  else
    ROWS=$(echo "$OUTPUT" | grep -oE 'Exported [0-9]+ rows' | grep -oE '[0-9]+' || echo "?")
    GENERATED="$GENERATED\n  $(basename "$OUTFILE")  ($ROWS rows)"
    printf "  OK    %-60s  %s rows\n" "$(basename "$OUTFILE")" "$ROWS"
  fi
}

# ── Performance base: campaign / adset / ad insights ─────────────────────────
run_insights "campaign" "$OUT_DIR/meta_campaign_insights_${TS}.csv"
run_insights "adset"    "$OUT_DIR/meta_adset_insights_${TS}.csv"
run_insights "ad"       "$OUT_DIR/meta_ad_insights_${TS}.csv"

# ── Decision layer: ad insights by placement breakdown ────────────────────────
run_insights "ad" "$OUT_DIR/meta_ad_insights_by_placement_${TS}.csv" \
  "--breakdowns publisher_platform,platform_position"

# ── Decision layer: campaign and adset object snapshots ───────────────────────
run_objects "campaigns" "$OUT_DIR/meta_campaign_objects_${TS}.csv"
run_objects "adsets"    "$OUT_DIR/meta_adset_objects_${TS}.csv"

# ── Summary ───────────────────────────────────────────────────────────────────
echo ""
echo "════════════════════════════════════════════════════════════════"
echo "FILES GENERATED"
echo "────────────────────────────────────────────────────────────────"
printf "%b\n" "$GENERATED"

if [ -n "$ERRORS" ]; then
  echo ""
  echo "ERRORS"
  echo "────────────────────────────────────────────────────────────────"
  printf "%b\n" "$ERRORS"
  exit 1
fi

echo ""
echo "Phase 1 complete. No errors."
