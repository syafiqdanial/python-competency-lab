# Python Interview Competency Checklist

Use this as an explanation-and-implementation checklist. For each item, be able to give a concise definition, show a small example, identify a common mistake, and explain when it should or should not be used.

## Beginner fundamentals

- [ ] Explain Python's core scalar and collection types.
- [ ] Explain mutability and aliasing with lists and dictionaries.
- [ ] Choose appropriately among list, tuple, set, and dictionary.
- [ ] Write comprehensions without sacrificing readability.
- [ ] Explain positional, keyword, default, `*args`, and `**kwargs` parameters.
- [ ] Explain local, enclosing, global, and built-in scope.
- [ ] Handle exceptions narrowly and preserve useful error information.
- [ ] Read and write text, JSON, and CSV using context managers.
- [ ] Split code into importable modules and avoid import side effects.
- [ ] Write unit tests for normal, boundary, and invalid inputs.

## Intermediate Python

- [ ] Explain equality versus identity.
- [ ] Explain shallow versus deep copying.
- [ ] Use dataclasses and know when a plain function or dictionary is simpler.
- [ ] Apply type hints, unions, generics, and protocols appropriately.
- [ ] Explain iterables, iterators, and generators.
- [ ] Implement and explain decorators without hiding behavior unnecessarily.
- [ ] Create a context manager and explain resource cleanup.
- [ ] Explain instance, class, and static methods.
- [ ] Use composition and inheritance deliberately.
- [ ] Mock an external HTTP dependency without over-mocking internal code.
- [ ] Structure and package a Python application with `pyproject.toml`.
- [ ] Explain synchronous, threaded, process-based, and asynchronous execution.

## Expert-level discussion

- [ ] Explain the GIL accurately and its practical consequences.
- [ ] Design idempotent operations and retry policies.
- [ ] Identify race conditions and protect shared state.
- [ ] Explain cancellation, timeouts, backpressure, and graceful shutdown.
- [ ] Use profiling evidence before optimizing.
- [ ] Compare eager collections with lazy iterator pipelines.
- [ ] Design stable interfaces using abstract base classes or protocols.
- [ ] Explain descriptors and Python's attribute lookup at a practical level.
- [ ] Discuss memory, algorithmic complexity, and data-structure trade-offs.
- [ ] Design logs and metrics that make failures diagnosable.
- [ ] Explain architectural trade-offs rather than presenting one pattern as universal.

## Interview rehearsal

For each completed project:

- [ ] Give a two-minute project explanation.
- [ ] Walk through one important function without notes.
- [ ] Explain one rejected design alternative.
- [ ] Describe one bug and how evidence localized it.
- [ ] Extend one requirement while speaking through the reasoning.
- [ ] Identify security, performance, and maintainability risks.
