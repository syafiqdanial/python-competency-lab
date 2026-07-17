# Python Competency Lab

A progressive, project-based Python practice repository for strengthening interview readiness and demonstrating engineering growth from beginner fundamentals to expert-level design.

> Coding workspace: Raspberry Pi `~/Projects/python-competency-lab`
>
> Begin with [START_HERE.md](START_HERE.md).

## Purpose

This repository is both a learning log and a portfolio artifact. I will complete each project in sequence, write tests before or alongside implementation, document important decisions, and use issues and pull requests to preserve evidence of my progress.

## How I will work

For every project I will:

1. Restate the requirements and define acceptance criteria.
2. create an issue and a dedicated feature branch;
3. implement the smallest correct solution;
4. add automated tests for normal, boundary, and failure cases;
5. run formatting, linting, type checking, and tests;
6. document design choices and trade-offs;
7. open a pull request and review my own diff; and
8. record what I learned before merging.

## Progress

| Level | Project | Primary focus | Status |
| --- | --- | --- | --- |
| Beginner | [CLI Task Tracker](projects/beginner/01-cli-task-tracker.md) | Functions, collections, file I/O, exceptions | Not started |
| Beginner | [Text and Log Analyzer](projects/beginner/02-text-log-analyzer.md) | Strings, regular expressions, `collections` | Not started |
| Beginner | [CSV Expense Reporter](projects/beginner/03-csv-expense-reporter.md) | CSV, dates, decimal arithmetic, reporting | Not started |
| Intermediate | [Typed API Client](projects/intermediate/01-typed-api-client.md) | HTTP, dataclasses, typing, packaging | Not started |
| Intermediate | [Job Tracker API](projects/intermediate/02-job-tracker-api.md) | FastAPI, persistence, validation, testing | Not started |
| Intermediate | [Async Service Monitor](projects/intermediate/03-async-service-monitor.md) | `asyncio`, concurrency, retries, observability | Not started |
| Expert | [Plugin Workflow Engine](projects/expert/01-plugin-workflow-engine.md) | Protocols, decorators, plugins, architecture | Not started |
| Expert | [Durable Job Queue](projects/expert/02-durable-job-queue.md) | Workers, idempotency, retries, concurrency | Not started |
| Expert | [Mini Query Engine](projects/expert/03-mini-query-engine.md) | Parsing, iterators, algorithms, optimization | Not started |

## Competency map

| Stage | Python skills I will demonstrate |
| --- | --- |
| Beginner | Variables, control flow, functions, collections, comprehensions, modules, exceptions, file handling, standard library use, basic tests |
| Intermediate | Object-oriented design, dataclasses, type hints, generators, decorators, context managers, API integration, mocking, packaging, database access, async I/O |
| Expert | Protocol-oriented design, plugin systems, concurrency safety, idempotency, performance analysis, parsing, architecture trade-offs, observability, failure recovery |

## Quality gates

Every completed project must have:

- clear setup and usage documentation;
- automated tests covering success and failure paths;
- `ruff` formatting and linting;
- `mypy` type checking where appropriate;
- no committed credentials or private data;
- meaningful commit messages; and
- a short retrospective describing what I learned.

## Interview preparation

The projects are supported by an [interview competency checklist](INTERVIEW_CHECKLIST.md). I will not treat a topic as complete merely because I can define it; I should be able to explain it, implement it, test it, and discuss its trade-offs.

## Repository structure

```text
python-competency-lab/
├── projects/
│   ├── beginner/
│   ├── intermediate/
│   └── expert/
├── solutions/              # Implementations added incrementally
├── tests/                  # Automated tests added with each solution
├── docs/retrospectives/    # What I learned from each project
├── INTERVIEW_CHECKLIST.md
├── CONTRIBUTING.md
└── pyproject.toml
```

## Local quality commands

```bash
python -m pytest
python -m ruff format --check .
python -m ruff check .
python -m mypy solutions
```

The repository begins as a curriculum. Implementations will be added through focused pull requests so the commit history shows genuine progression.
