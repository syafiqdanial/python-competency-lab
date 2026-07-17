# Commit Guide

Use this format:

```text
type(scope): concise imperative summary
```

## Types

| Type | Use |
| --- | --- |
| `feat` | Add user-visible behavior |
| `fix` | Correct incorrect behavior |
| `test` | Add or improve tests |
| `docs` | Change documentation only |
| `refactor` | Restructure without intended behavior change |
| `chore` | Maintain tools or dependencies |
| `ci` | Change continuous-integration automation |
| `perf` | Improve measured performance |

## Good examples

```text
feat(task-tracker): persist tasks as JSON
fix(expense-reporter): reject negative row numbers
test(api-client): cover rate-limit response
docs(query-engine): document grammar
```

## Avoid

```text
update
changes
fix stuff
final version
working now
feat: Added a bunch of things and fixed tests and changed docs
```

A commit should contain one coherent idea. Use `git add -p` to avoid mixing unrelated changes.

Before committing:

```bash
./scripts/check.sh
git diff --check
git diff --cached
```
