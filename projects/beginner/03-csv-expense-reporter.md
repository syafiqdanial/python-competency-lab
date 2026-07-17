# Beginner 3 — CSV Expense Reporter

## What I am going to build

I will build a reporting tool that imports synthetic expense transactions from CSV, validates them, groups spending by category and month, and exports a concise summary. The repository will contain generated sample data only—never real financial records.

## Skills I will practise

- the `csv`, `datetime`, and `decimal` modules;
- dataclasses for validated records;
- comprehensions and grouping;
- deterministic sorting and formatting;
- domain validation; and
- testing numeric and date edge cases.

## Acceptance criteria

- Parse a documented CSV schema.
- Use `Decimal` rather than binary floats for currency.
- Reject invalid dates, amounts, and missing fields with row context.
- Produce totals by month and category.
- Export a summary without modifying the source file.
- Test rounding, empty files, and malformed rows.

## Stretch work

Add budgets, variance reporting, and a small HTML report.
