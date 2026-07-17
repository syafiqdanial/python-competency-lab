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

## Suggested working steps

1. Write a correct synchronous checker as a behavior baseline.
2. Convert one check into a coroutine and test it.
3. Schedule several checks concurrently.
4. Add an explicit concurrency limit before adding retries.
5. Add timeout, cancellation, and graceful-shutdown behavior.
6. Compare measured behavior with the synchronous baseline.

**Think about:** What must be cancelled when the program stops? Why can unlimited concurrency be harmful?

## Stretch work

Expose Prometheus metrics and compare asynchronous performance with a synchronous baseline.
