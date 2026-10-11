# Sprint 1 Plan

## Sprint Goal

Deliver unit tests for the register and heartbeat endpoints, add input
validation, and set up the CI pipeline.

## Capacity

7 points. First sprint with no velocity history, so we use a conservative
estimate based on story size.

## Stories and Tasks

| Story                                   | Points | Tasks                                                                 |
|-----------------------------------------|--------|-----------------------------------------------------------------------|
| US1 — Register Monitor Tests            | 3      | Write test for successful device creation                             |
|                                         |        | Write test for negative timeout rejection                             |
|                                         |        | Run tests and fix issues                                              |
| US2 — Validation                        | 2      | Add serializer validation for negative timeout                         |
|                                         |        | Add serializer validation for invalid email                            |
|                                         |        | Run tests and fix issues                                              |
| US3 — Heartbeat Tests                   | 2      | Write test for successful heartbeat reset                             |
|                                         |        | Write test for 404 on unknown device                                  |
|                                         |        | Run tests and fix issues                                              |
| CI Pipeline                             | —      | Create `.github/workflows/ci.yml` with Django test job                |
|                                         |        | Push and verify the run is green                                      |

## Sprint Total

7 points

## Out of Scope

- Health endpoint (`/health/`)
- Console logging
- Pause monitoring tests
- Status endpoint tests
- Alert email backend