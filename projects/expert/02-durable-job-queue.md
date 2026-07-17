# Expert 2 — Durable Job Queue

## What I am going to build

I will build a small durable job queue with producers, workers, retries, visibility timeouts, and idempotency protection. The goal is to reason about failure recovery rather than imitate a production message broker feature for feature.

## Skills I will practise

- concurrency and worker coordination;
- database transactions and locking;
- idempotency keys;
- retry policies and dead-letter handling;
- graceful shutdown and recovery;
- metrics and structured logs; and
- deterministic concurrency testing.

## Acceptance criteria

- Enqueue and claim jobs atomically.
- Prevent two workers from completing the same claim.
- Recover jobs abandoned by failed workers.
- Bound retries and preserve terminal failures.
- Handle repeated idempotency keys safely.
- Expose queue depth, latency, and failure metrics.
- Test crashes and races rather than only the happy path.

## Stretch work

Add scheduled jobs, priorities, and a comparison document against established queue systems.
