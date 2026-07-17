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

## Stretch work

Support multiple formats through pluggable parsers and compare two time windows.
