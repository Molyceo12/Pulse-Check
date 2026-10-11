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

## Acceptance criteria

### US1 — Unit tests for register monitor endpoint
- **Given** a POST request to `/register_monitor` with valid data
- **When** the endpoint is called
- **Then** a `201` response is returned and the device is saved in the database
- **Given** a POST request with a negative `timeout`
- **When** the endpoint is called
- **Then** a `400` error is returned and no device is created (error case)

### US2 — Validation for negative timeouts and invalid emails
- **Given** a POST request with `timeout` set to `-5`
- **When** the endpoint is called
- **Then** a `400` error is returned with a clear validation message (error case)
- **Given** a POST request with an invalid `alert_email`
- **When** the endpoint is called
- **Then** a `400` error is returned and the device is not saved (error case)

### US3 — Unit tests for heartbeat endpoint
- **Given** a registered device exists
- **When** a POST request is sent to `/monitors/{id}/heartbeat`
- **Then** the device's `last_heartbeat` is updated and a `200` response is returned
- **Given** a device that does not exist
- **When** a POST request is sent to its heartbeat endpoint
- **Then** a `404` error is returned (error case)

### US4 — Health endpoint
- **Given** the API is running
- **When** a GET request is sent to `/health/`
- **Then** `{"status": "ok"}` is returned with HTTP `200` (error case: endpoint must always respond)

### US5 — Console logging for requests and errors
- **Given** logging is configured in Django settings
- **When** any request is handled
- **Then** a log line with the request method and path is printed to the console
- **Given** an error occurs during request handling
- **Then** an error-level log line is printed to the console (error case)

### US6 — Unit tests for pause monitoring endpoint
- **Given** an active device exists
- **When** a POST request is sent to `/monitors/{id}/pause`
- **Then** the device status is changed to `paused` and a success response is returned
- **Given** a device that is already paused
- **When** a pause request is sent
- **Then** a `400` error is returned because the device is not active (error case)

### US7 — Unit tests for status endpoint
- **Given** a registered device exists
- **When** a GET request is sent to `/monitors/{id}/status`
- **Then** the device's current status, timeout, last heartbeat, and alert email are returned
- **Given** a device that does not exist
- **When** a GET request is sent to its status endpoint
- **Then** a `404` error is returned (error case)

### US8 — Alert email backend
- **Given** a device misses its heartbeat window
- **When** the watchdog timer fires
- **Then** an email is sent to the device's `alert_email` using a real backend (error case: email must not crash the worker)