# Beginner 1 — CLI Task Tracker

## What I am going to build

I will build a command-line task tracker that can add, list, complete, edit, and delete tasks. Tasks will persist in a JSON file so they survive between runs. The interface will validate input and return clear errors instead of failing with raw tracebacks.

## Skills I will practise

- variables, functions, loops, and conditionals;
- lists and dictionaries;
- command-line argument handling;
- JSON file I/O and context managers;
- exceptions and input validation;
- separation of business logic from terminal output; and
- unit testing with temporary files.

## Acceptance criteria

- Add a task with a title and optional due date.
- List pending and completed tasks.
- Complete, edit, and delete a task by stable identifier.
- Preserve valid data across executions.
- Reject malformed files and invalid commands clearly.
- Test normal operations, missing IDs, and corrupted storage.

## Stretch work

Add priorities, filtering, export, and atomic file replacement to avoid partial writes.
