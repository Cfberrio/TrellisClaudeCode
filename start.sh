#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$HOME/Documents/CLAUDE CODE"
cd "$PROJECT_DIR"

if [ ! -d ".venv" ]; then
  echo "❌ No existe .venv en $PROJECT_DIR"
  echo "Crea el entorno con:"
  echo "python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt"
  exit 1
fi

source .venv/bin/activate

if [ ! -f ".env" ]; then
  echo "❌ No existe .env en $PROJECT_DIR"
  echo "Copia el template y llénalo:"
  echo "cp .env.example .env"
  exit 1
fi

set -a
source .env
set +a

echo "✅ Entorno listo"
echo "📁 Proyecto: $PROJECT_DIR"
echo "🐍 Python: $(which python)"
echo "🎯 Customer ID: ${GOOGLE_ADS_CUSTOMER_ID:-MISSING}"
echo "🧠 Abriendo Claude Code..."

exec claude
