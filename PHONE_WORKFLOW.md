# Phone-Friendly Development Workflow

## Start a session

```bash
cd ~/Projects/python-competency-lab
source .venv/bin/activate
git status
git pull --ff-only
```

## Work in small pieces

Use one branch for one coherent change:

```bash
git switch -c beginner/short-description
```

A comfortable phone-terminal loop is:

1. Read one acceptance criterion.
2. Inspect only the files relevant to it.
3. Write or update one test.
4. Run that test and observe the failure.
5. Implement the smallest useful change.
6. Run `./scripts/check.sh`.
7. Review the diff before committing.

Useful commands:

```bash
git status
git diff
git diff --cached
python -m pytest -q
python -m pytest tests/path_to_test.py -q
```

## Commit and push

```bash
git add -p
git diff --cached
git commit -m "type(scope): concise imperative summary"
git push -u origin HEAD
```

Examples:

```text
feat(task-tracker): add task creation
fix(log-analyzer): skip malformed timestamps
test(expense-reporter): cover invalid currency rows
docs(api-client): explain retry policy
refactor(service-monitor): isolate timeout handling
```

## End a session

Leave the repository in one of these states:

- committed and pushed; or
- intentionally unfinished with a short note in the relevant issue.

Avoid leaving important work only in the phone terminal without a commit or backup.
