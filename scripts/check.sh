#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

if [[ -f .venv/bin/activate ]]; then
  . .venv/bin/activate
fi

python -m ruff format --check .
python -m ruff check .

if python3 - <<'PY'
from pathlib import Path
raise SystemExit(0 if any(Path("solutions").rglob("*.py")) else 1)
PY
then
  python -m mypy solutions
else
  echo "mypy: skipped (no solution Python files yet)"
fi

if python3 - <<'PY'
from pathlib import Path
raise SystemExit(0 if any(Path("tests").rglob("test_*.py")) else 1)
PY
then
  python -m pytest -q
else
  echo "pytest: skipped (no tests yet)"
fi
