# Product Backlog

Priority: MoSCoW. Estimates: Fibonacci story points (1, 2, 3, 5, 8). Reference story (= 2 points): Health endpoint — a small, self-contained feature with a single view and one test, easy to size reliably.

| ID | Story | Priority | Points | Sprint |
|---|---|---|---|---|
| US1 | As a tester, I want unit tests for the register monitor endpoint so that I can verify it creates devices correctly and rejects bad input. | Must | 3 | Sprint 1 |
| US2 | As a developer, I want validation that rejects negative timeouts and invalid emails so that corrupted data never enters the system. | Must | 2 | Sprint 1 |
| US3 | As a tester, I want unit tests for the heartbeat endpoint so that I can verify the watchdog timer is reset and unknown devices return 404. | Must | 2 | Sprint 1 |
| US4 | As an operator, I want a `/health/` endpoint returning `{"status": "ok"}` so that infrastructure can verify the API is running. | Should | 2 | Sprint 2 |
| US5 | As a developer, I want console logging for requests and errors so that debugging is easier during development. | Should | 2 | Sprint 2 |
| US6 | As a tester, I want unit tests for the pause monitoring endpoint so that I can verify devices are correctly paused. | Should | 2 | Sprint 2 |
| US7 | As a tester, I want unit tests for the status endpoint so that I can verify device health is returned correctly. | Should | 2 | Sprint 2 |
| US8 | As a developer, I want alert emails sent through a real backend so that operators are notified when devices go silent. | Could | 3 | Backlog |

## Sprint 1

| ID | Story | Points |
|---|---|---|
| US1 | Unit tests for register monitor endpoint | 3 |
| US2 | Validation for negative timeouts and invalid emails | 2 |
| US3 | Unit tests for heartbeat endpoint | 2 |

**Sprint 1 total: 7 points**

## Sprint 2

| ID | Story | Points |
|---|---|---|
| US4 | Health endpoint (`/health/`) | 2 |
| US5 | Console logging for requests and errors | 2 |
| US6 | Unit tests for pause monitoring endpoint | 2 |
| US7 | Unit tests for status endpoint | 2 |

**Sprint 2 total: 8 points**

## Backlog (not planned)

| ID | Story | Points |
|---|---|---|
| US8 | Alert email backend | 3 |

## Prioritisation rationale

- **Must first**: Tests and validation protect the existing app from regressions and bad data, which is essential before adding new features.
- **Should next**: Health endpoint and logging are low-effort, high-value operational improvements that work for every future feature.
- **Could last**: Alert email backend depends on external infrastructure (SMTP) and is lower priority for a first working prototype.