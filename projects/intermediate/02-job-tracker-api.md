# Intermediate 2 — Job Tracker API

## What I am going to build

I will build a REST API for tracking synthetic job applications through stages such as saved, applied, interviewing, offered, and closed. It will persist records, validate state changes, and expose filtered summaries.

## Skills I will practise

- FastAPI request and response models;
- relational data modeling and migrations;
- service and repository boundaries;
- validation and HTTP error semantics;
- fixtures, integration tests, and test isolation;
- configuration through environment variables; and
- Docker-based local development.

## Acceptance criteria

- Create, read, update, and archive synthetic applications.
- Validate allowed status transitions.
- Filter and paginate results.
- Store timestamps consistently.
- Return stable error responses.
- Test API, service, and persistence behavior.
- Publish OpenAPI documentation without exposing secrets.

## Suggested working steps

1. Model a synthetic job application and its allowed statuses.
2. Implement one create-and-read path using an in-memory repository.
3. Add service-level rules for status transitions.
4. Replace the repository with persistent storage without changing API behavior.
5. Add filtering and pagination.
6. Test validation, conflicts, missing records, and persistence isolation.

**Think about:** Which rules belong in HTTP handlers, services, or persistence? What should happen during two conflicting updates?

## Stretch work

Add optimistic concurrency, audit history, and a minimal browser interface.
