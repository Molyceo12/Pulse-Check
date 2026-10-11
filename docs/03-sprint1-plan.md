# Sprint 1 Plan

## Sprint Goal

Deliver unit tests for the register and heartbeat endpoints, add input validation, and set up the CI pipeline.

## Capacity

7 points. First sprint with no velocity history, so we use a conservative estimate based on story size.

## Stories and Tasks

| Story | Points | Tasks |
|---|---|---|
| US1 — Unit tests for register monitor endpoint | 3 | Write test for successful device creation; write test for negative timeout rejection; run tests and fix issues |
| US2 — Validation for negative timeouts and invalid emails | 2 | Add serializer validation for negative timeout; add serializer validation for invalid email; run tests and fix issues |
| US3 — Unit tests for heartbeat endpoint | 2 | Write test for successful heartbeat reset; write test for 404 on unknown device; run tests and fix issues |
| CI pipeline | — | Create `.github/workflows/ci.yml` with Django test job; push and verify the run is green |

## Sprint Total

7 points

## Out of Scope

- Health endpoint (`/health/`)
- Console logging
- Pause monitoring tests
- Status endpoint tests
- Alert email backend