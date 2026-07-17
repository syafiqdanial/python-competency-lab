# Beginner 2 — Text and Log Analyzer

## What I am going to build

I will build a tool that reads application log files and produces a summary of severity levels, frequent messages, timestamps, and error patterns. It will accept files from the command line and support human-readable and JSON reports.

## Skills I will practise

- strings, slicing, and regular expressions;
- dictionaries, sets, and `collections.Counter`;
- generators for line-by-line processing;
- defensive parsing and malformed-input handling;
- sorting and aggregation; and
- parameterized tests.

## Acceptance criteria

- Parse a documented log format without loading the whole file into memory.
- Count messages by severity.
- Report the most frequent errors.
- Handle blank and malformed lines predictably.
- Produce deterministic text and JSON output.
- Include tests for representative and edge-case logs.

## Suggested working steps

1. Write five representative log lines, including one malformed line.
2. Parse one line into a small record before reading a whole file.
3. Turn the parser into a generator that processes lines lazily.
4. Count severity levels, then add frequent-message reporting.
5. Separate parsing from report formatting.
6. Test blank files, malformed timestamps, and deterministic ordering.

**Think about:** Which malformed lines should be skipped, and which should stop the program? Why process lazily?

## Stretch work

Support multiple formats through pluggable parsers and compare two time windows.
