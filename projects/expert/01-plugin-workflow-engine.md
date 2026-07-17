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

## Stretch work

Add parallel independent steps, checkpoints, and a dry-run execution plan.
