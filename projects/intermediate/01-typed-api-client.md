# Intermediate 1 — Typed API Client

## What I am going to build

I will create an installable Python client for a public HTTP API. It will convert JSON responses into typed models, handle pagination and rate limits, and expose a small, predictable interface independent of the HTTP library.

## Skills I will practise

- HTTP requests and response semantics;
- dataclasses, enums, and type hints;
- protocols and dependency injection;
- pagination, timeouts, retries, and rate limits;
- custom exception design;
- packaging with `pyproject.toml`; and
- mocking external boundaries in tests.

## Acceptance criteria

- Configure base URL, timeout, and authentication safely.
- Parse successful responses into typed objects.
- Handle pagination without exposing transport details.
- Distinguish validation, authentication, rate-limit, and server errors.
- Unit-test behavior without requiring network access.
- Provide one opt-in integration test against the real public API.

## Stretch work

Add caching, synchronous and asynchronous transports, and generated API documentation.
