#!/usr/bin/env bash
# run_phase1_extract.sh — Phase 1 read-only Google Ads extraction for OEV.
# Runs all 8 GAQL queries and exports CSVs to data/raw/ with a shared timestamp.
#
# Usage:
#   ./scripts/run_phase1_extract.sh              # uses GOOGLE_ADS_CUSTOMER_ID from .env
#   ./scripts/run_phase1_extract.sh 3123559470   # override customer ID

set -euo pipefail

# ── Paths ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
ENV_FILE="$PROJECT_ROOT/.env"
QUERIES_DIR="$PROJECT_ROOT/queries"
OUT_DIR="$PROJECT_ROOT/data/raw"
RUNNER="$PROJECT_ROOT/scripts/run_gaql.py"

# ── Load .env ─────────────────────────────────────────────────────────────────
if [ -f "$ENV_FILE" ]; then
  set -a
  # shellcheck source=/dev/null
  source "$ENV_FILE"
  set +a
else
  echo "ERROR: .env not found at $ENV_FILE" >&2
  exit 1
fi

# ── Python interpreter ────────────────────────────────────────────────────────
if [ -f "$PROJECT_ROOT/.venv/bin/python" ]; then
  PYTHON="$PROJECT_ROOT/.venv/bin/python"
else
  PYTHON="python3"
fi

# ── Customer ID ───────────────────────────────────────────────────────────────
CUSTOMER_ID="${1:-${GOOGLE_ADS_CUSTOMER_ID:-}}"
if [ -z "$CUSTOMER_ID" ]; then
  echo "ERROR: No customer ID. Set GOOGLE_ADS_CUSTOMER_ID in .env or pass as first argument." >&2
  exit 1
fi

# ── Timestamp ─────────────────────────────────────────────────────────────────
TS=$(date +%Y%m%d_%H%M%S)
mkdir -p "$OUT_DIR"

echo "Phase 1 extraction — OEV"
echo "Customer ID : $CUSTOMER_ID"
echo "Timestamp   : $TS"
echo "Output dir  : $OUT_DIR"
echo "────────────────────────────────────────────────────────────────"

# ── Query list ────────────────────────────────────────────────────────────────
QUERIES=(
  "campaigns_last_30_days"
  "pmax_asset_groups_last_30_days"
  "conversion_actions"
  "campaign_conversions_by_action_last_30_days"
  "campaign_search_terms_last_30_days"
  "landing_pages_last_30_days"
  "geographic_performance_last_30_days"
  "call_conversions_last_30_days"
)

# ── Run queries ───────────────────────────────────────────────────────────────
ERRORS=()
GENERATED=()
HAS_ERROR=0

for Q in "${QUERIES[@]}"; do
  QFILE="$QUERIES_DIR/${Q}.sql"
  OUTFILE="$OUT_DIR/${Q}_${TS}.csv"

  if [ ! -f "$QFILE" ]; then
    ERRORS+=("$Q: query file not found at $QFILE")
    printf "  FAIL  %s\n" "$Q"
    HAS_ERROR=1
    continue
  fi

  OUTPUT=$("$PYTHON" "$RUNNER" \
    --query-file "$QFILE" \
    --out "$OUTFILE" \
    --customer-id "$CUSTOMER_ID" 2>&1) && STATUS=0 || STATUS=$?

  if [ "$STATUS" -ne 0 ]; then
    ERR_MSG=$(echo "$OUTPUT" | grep -i "error" | head -1 || echo "unknown error")
    ERRORS+=("$Q: $ERR_MSG")
    printf "  FAIL  %s\n" "$Q"
    HAS_ERROR=1
    continue
  fi

  ROWS=$(echo "$OUTPUT" | grep -oE 'Exported [0-9]+ rows' | grep -oE '[0-9]+' || echo "?")
  GENERATED+=("${OUTFILE##*/}  ${ROWS} rows")
  printf "  OK    %-52s  %s rows\n" "$Q" "$ROWS"
done

# ── Summary ───────────────────────────────────────────────────────────────────
echo ""
echo "════════════════════════════════════════════════════════════════"
echo "FILES GENERATED"
echo "────────────────────────────────────────────────────────────────"
for ENTRY in "${GENERATED[@]}"; do
  printf "  %s\n" "$ENTRY"
done

if [ "$HAS_ERROR" -ne 0 ]; then
  echo ""
  echo "ERRORS"
  echo "────────────────────────────────────────────────────────────────"
  for ERR in "${ERRORS[@]}"; do
    echo "  $ERR"
  done
  exit 1
fi

echo ""
echo "Phase 1 complete. No errors."
