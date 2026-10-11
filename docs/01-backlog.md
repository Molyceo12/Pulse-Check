# Product Backlog

Priority: MoSCoW. Estimates: Fibonacci story points (1, 2, 3, 5, 8). Reference
story (= 2 points): Health endpoint — a small, self-contained feature with a
single view and one test, easy to size reliably.

## Story Table

| ID  | Story                                              | Priority | Points | Sprint     |
|-----|----------------------------------------------------|----------|--------|------------|
| US1 | Unit tests for register monitor endpoint           | Must     | 3      | Sprint 1   |
| US2 | Validation for negative timeouts and invalid emails | Must     | 2      | Sprint 1   |
| US3 | Unit tests for heartbeat endpoint                  | Must     | 2      | Sprint 1   |
| US4 | Health endpoint (`/health/`)                       | Should   | 2      | Sprint 2   |
| US5 | Console logging for requests and errors            | Should   | 2      | Sprint 2   |
| US6 | Unit tests for pause monitoring endpoint           | Should   | 2      | Sprint 2   |
| US7 | Unit tests for status endpoint                     | Should   | 2      | Sprint 2   |
| US8 | Alert email backend                                | Could    | 3      | Backlog    |

## Sprint Totals

- Sprint 1: 7 points (US1, US2, US3) — complete
- Sprint 2: 8 points (US4, US5, US6, US7) — complete
- Backlog: 3 points (US8) — not planned

## Prioritisation Rationale

1. Must first: Tests and validation protect the existing app from regressions
   and bad data, which is essential before adding new features.
2. Should next: Health endpoint and logging are low-effort, high-value
   operational improvements that work for every future feature.
3. Could last: Alert email backend depends on external infrastructure (SMTP)
   and is lower priority for a first working prototype.

## Acceptance Criteria

### US1 — Unit tests for register monitor endpoint

- Given a POST request to `/register_monitor` with valid data
- When the endpoint is called
- Then a 201 response is returned and the device is saved in the database
- Given a POST request with a negative `timeout`
- When the endpoint is called
- Then a 400 error is returned and no device is created (error case)

### US2 — Validation for negative timeouts and invalid emails

- Given a POST request with `timeout` set to `-5`
- When the endpoint is called
- Then a 400 error is returned with a clear validation message (error case)
- Given a POST request with an invalid `alert_email`
- When the endpoint is called
- Then a 400 error is returned and the device is not saved (error case)

### US3 — Unit tests for heartbeat endpoint

- Given a registered device exists
- When a POST request is sent to `/monitors/{id}/heartbeat`
- Then the device's `last_heartbeat` is updated and a 200 response is returned
- Given a device that does not exist
- When a POST request is sent to its heartbeat endpoint
- Then a 404 error is returned (error case)

### US4 — Health endpoint

- Given the API is running
- When a GET request is sent to `/health/`
- Then `{"status": "ok"}` is returned with HTTP 200
- Error case: endpoint must always respond

### US5 — Console logging for requests and errors

- Given logging is configured in Django settings
- When any request is handled
- Then a log line with the request method and path is printed to the console
- Given an error occurs during request handling
- Then an error-level log line is printed to the console (error case)

### US6 — Unit tests for pause monitoring endpoint

- Given an active device exists
- When a POST request is sent to `/monitors/{id}/pause`
- Then the device status is changed to `paused` and a success response is returned
- Given a device that is already paused
- When a pause request is sent
- Then a 400 error is returned because the device is not active (error case)

### US7 — Unit tests for status endpoint

- Given a registered device exists
- When a GET request is sent to `/monitors/{id}/status`
- Then the device's current status, timeout, last heartbeat, and alert email are returned
- Given a device that does not exist
- When a GET request is sent to its status endpoint
- Then a 404 error is returned (error case)

### US8 — Alert email backend

- Given a device misses its heartbeat window
- When the watchdog timer fires
- Then an email is sent to the device's `alert_email` using a real backend
- Error case: email must not crash the worker