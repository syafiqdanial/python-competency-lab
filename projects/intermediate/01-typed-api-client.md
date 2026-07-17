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

## Suggested working steps

1. Choose a harmless public API and record one example response.
2. Design the smallest public client interface before selecting an HTTP library.
3. Convert one response into a typed model.
4. Inject the transport so unit tests do not require network access.
5. Add pagination, then timeout and error mapping.
6. Add one opt-in integration test after unit behavior is stable.

**Think about:** Which HTTP details should callers see? Which failures should be retryable?

## Stretch work

Add caching, synchronous and asynchronous transports, and generated API documentation.
