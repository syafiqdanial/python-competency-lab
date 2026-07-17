#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

if [[ ! -d .venv ]]; then
  python3 -m venv .venv
fi

. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt

printf '\nSetup complete. Activate the environment with:\n'
printf '  source .venv/bin/activate\n\n'
./scripts/check.sh
