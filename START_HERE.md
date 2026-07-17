# Start Here — Raspberry Pi Phone Workflow

This repository is prepared for coding from a phone connected to the Raspberry Pi terminal.

## Workspace

```text
/home/syafiqdanial/Projects/python-competency-lab
```

## First-time setup

```bash
cd ~/Projects/python-competency-lab
./scripts/setup-pi.sh
```

The setup script creates `.venv`, installs the development tools, and runs an initial check. Activate the environment whenever a new terminal session begins:

```bash
cd ~/Projects/python-competency-lab
source .venv/bin/activate
```

## Begin the first project

Open the project brief:

```bash
less projects/beginner/01-cli-task-tracker.md
```

Then create a branch:

```bash
git pull --ff-only
git switch -c beginner/cli-task-tracker
```

Do not attempt the whole project in one sitting. Pick one acceptance criterion, write a small test, implement it, and run:

```bash
./scripts/check.sh
```

## Save progress

```bash
git status
git add -p
git diff --cached
git commit -m "feat(task-tracker): add task creation"
git push -u origin HEAD
```

After pushing, message Ultima:

```text
Review the latest commit in python-competency-lab.
```

The review will cover commit naming, code quality, tests, and whether the implementation is moving in the right direction.

## If stuck

Before asking for the solution, write down:

1. what you expected;
2. what actually happened;
3. the exact command or test that failed;
4. one hypothesis; and
5. the smallest experiment that could test it.

Ask for a hint first. The goal is to preserve the useful struggle without leaving you trapped.
