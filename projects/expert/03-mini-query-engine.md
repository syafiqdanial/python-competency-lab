# Expert 3 — Mini Query Engine

## What I am going to build

I will build a small query engine that parses a deliberately limited expression language and evaluates filters, projections, sorting, and grouping over records. The project will emphasize correctness, lazy evaluation, and explicit complexity trade-offs.

## Skills I will practise

- tokenization and recursive-descent parsing;
- abstract syntax trees;
- iterators and generators;
- data structures and algorithmic complexity;
- clear syntax and evaluation errors;
- property-based testing; and
- profiling before optimization.

## Acceptance criteria

- Define and document a small query grammar.
- Tokenize and parse valid expressions into an AST.
- Reject invalid syntax with source positions.
- Evaluate filters and projections lazily where possible.
- Support deterministic sorting and grouping.
- Test parser invariants and evaluator edge cases.
- Profile representative workloads before making optimization claims.

## Stretch work

Add a query planner, indexes for selected fields, and benchmark comparisons between execution strategies.
