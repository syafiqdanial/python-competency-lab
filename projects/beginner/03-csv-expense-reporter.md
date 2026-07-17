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

## Suggested working steps

1. Define a small synthetic CSV schema and create a few sample rows.
2. Parse one row into a validated record.
3. Prove with a test why `Decimal` is preferable for currency.
4. Group records by category, then by month.
5. Render a deterministic report separately from calculations.
6. Add row-specific errors for invalid dates, amounts, and missing values.

**Think about:** Should one bad row invalidate the whole import? How will the caller know which row failed?

## Stretch work

Add budgets, variance reporting, and a small HTML report.
