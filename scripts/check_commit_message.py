from __future__ import annotations

import re
import subprocess
import sys

PATTERN = re.compile(
    r"^(feat|fix|test|docs|refactor|chore|ci|perf)(\([a-z0-9-]+\))?: [a-z0-9].{4,71}$"
)


def main() -> int:
    message = subprocess.check_output(["git", "log", "-1", "--pretty=%s"], text=True).strip()
    if PATTERN.fullmatch(message):
        print(f"Valid commit message: {message}")
        return 0
    print(f"Invalid commit message: {message}", file=sys.stderr)
    print("Expected: type(scope): concise imperative summary", file=sys.stderr)
    print("Example: feat(task-tracker): add task creation", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
