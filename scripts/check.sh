#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

if [[ -f .venv/bin/activate ]]; then
  . .venv/bin/activate
fi

printf '\n[1/4] Ruff formatting\n'
python -m ruff format --check .

printf '\n[2/4] Ruff linting\n'
python -m ruff check .

printf '\n[3/4] Mypy type checking\n'
if python3 - <<'PY'
from pathlib import Path
raise SystemExit(0 if any(Path("solutions").rglob("*.py")) else 1)
PY
then
  python -m mypy solutions
else
  echo "Skipped: no solution Python files yet"
fi

printf '\n[4/4] Pytest\n'
if python3 - <<'PY'
from pathlib import Path
raise SystemExit(0 if any(Path("tests").rglob("test_*.py")) else 1)
PY
then
  python -m pytest -q
else
  echo "Skipped: no tests yet"
fi

printf '\nAll quality checks completed successfully.\n'
