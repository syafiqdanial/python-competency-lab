# Expert 1 — Plugin Workflow Engine

## What I am going to build

I will build a workflow engine that executes configurable steps through independently registered plugins. A workflow will be validated before execution, each step will receive an explicit context, and failures will produce traceable results.

## Skills I will practise

- protocols and abstract interfaces;
- decorators and registries;
- dynamic discovery without unsafe arbitrary imports;
- dependency graphs and validation;
- immutable result models;
- architectural boundaries; and
- contract and integration testing.

## Acceptance criteria

- Register plugins through a documented interface.
- Parse and validate a workflow definition.
- Detect unknown steps and dependency cycles.
- Execute steps in valid order.
- Capture outputs, duration, and structured failures.
- Test plugins against a reusable contract suite.

## Suggested working steps

1. Define one tiny plugin protocol and implement two example plugins.
2. Register plugins explicitly before attempting discovery.
3. Parse a linear workflow and return immutable step results.
4. Add dependency validation and cycle detection.
5. Add structured failure reporting and contract tests.
6. Introduce discovery or parallelism only after the core model is clear.

**Think about:** What makes a plugin interface stable? How will a bad plugin be isolated and diagnosed?

## Stretch work

Add parallel independent steps, checkpoints, and a dry-run execution plan.
