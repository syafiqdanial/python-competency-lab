# Intermediate 3 — Async Service Monitor

## What I am going to build

I will build an asynchronous service monitor that checks multiple configured HTTP endpoints concurrently, records latency and availability, and emits structured reports. All examples will use public or local demonstration endpoints rather than private infrastructure.

## Skills I will practise

- coroutines, tasks, and `asyncio`;
- concurrency limits and semaphores;
- timeouts, cancellation, and retries;
- structured logging;
- configuration validation;
- dependency injection for testability; and
- testing asynchronous code.

## Acceptance criteria

- Check multiple services concurrently with a configurable limit.
- Apply explicit connect and response timeouts.
- Retry only appropriate failures with bounded backoff.
- Shut down cleanly after cancellation.
- Produce text and JSON reports.
- Test success, timeout, cancellation, and partial failure.

## Stretch work

Expose Prometheus metrics and compare asynchronous performance with a synchronous baseline.
