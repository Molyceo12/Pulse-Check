# Pulse Check — Sprint Plan

## Product Vision
Pulse Check is a high-reliability monitoring system that tracks remote device heartbeats and triggers critical alerts when communication falls silent. Built with Django REST Framework, Celery, and Redis, it registers devices, accepts periodic heartbeats to reset watchdog timers, and automatically fires email alerts when a device misses its communication window. It also provides a status API for real-time health checks and supports pausing monitoring for maintenance.

---

## Product Backlog

| ID | Story | Priority | Points |
|---|---|---|---|
| US1 | As a system operator, I want to register a new device monitor so that the system knows which devices to track. | Must | 5 |
| US2 | As a system operator, I want to send device heartbeats so that the watchdog timer is reset and alerts are prevented. | Must | 5 |
| US3 | As a system operator, I want to check a device's real-time status so that I can verify health without waiting for an alert. | Must | 3 |
| US4 | As a system operator, I want to pause monitoring for a device during maintenance so that false alerts are not triggered. | Should | 3 |
| US5 | As a system operator, I want a `/health/` endpoint so that infrastructure can verify the API is running. | Should | 2 |
| US6 | As a system operator, I want structured console logging so that requests and errors are visible for debugging. | Should | 2 |
| US7 | As a system operator, I want alert emails to be sent via a real backend so that operators are notified of silent devices. | Could | 3 |

---

## Acceptance Criteria

### US1 — Register Monitor
- **Given** I POST to `/register_monitor` with a valid `id`, `timeout`, and `alert_email`
- **When** the request is processed
- **Then** the device is created with status `active` and `last_heartbeat` is `null`

- **Given** I POST with a negative `timeout`
- **When** the request is processed
- **Then** a `400` error is returned and no device is created (error case)

### US2 — Device Heartbeat
- **Given** a registered device exists
- **When** I POST to `/monitors/{id}/heartbeat`
- **Then** the device's `last_heartbeat` is updated and `{"success": true}` is returned

- **Given** a device that does not exist
- **When** I POST a heartbeat for it
- **Then** a `404` error is returned (error case)

### US3 — Check Device Status
- **Given** a registered device exists
- **When** I GET `/monitors/{id}/status`
- **Then** the current status, timeout, last heartbeat, and alert email are returned

### US4 — Pause Monitoring
- **Given** an active device exists
- **When** I POST to `/monitors/{id}/pause`
- **Then** monitoring is paused and `{"success": true, "message": "Monitoring paused."}` is returned

### US5 — Health Endpoint
- **Given** the API is running
- **When** I GET `/health/`
- **Then** `{"status": "ok"}` is returned with HTTP 200

### US6 — Console Logging
- **Given** logging is configured
- **When** any request is handled
- **Then** a log line is printed to the console with the request method and path
- **And** when an error occurs, an error-level log is printed

### US7 — Alert Email Backend
- **Given** a device misses its heartbeat window
- **When** the watchdog timer fires
- **Then** an email is sent to the device's `alert_email` using a real email backend (e.g., SMTP or console for testing)

---

## Definition of Done (DoD)

- [ ] All acceptance criteria for the story are met
- [ ] Unit and/or integration tests pass locally
- [ ] CI pipeline runs green on the feature branch
- [ ] A pull request is opened and merged into `main`
- [ ] Code follows existing style; no lint errors
- [ ] No hardcoded secrets or credentials
- [ ] Documentation (README, API docs) is updated if needed
- [ ] Changes are committed in small, logical increments (no big-bang commits)

---

## Sprint 1 Plan

**Sprint Goal:** Deliver core device monitoring API with register, heartbeat, and status endpoints, plus CI pipeline.

| Story | Points | Tasks |
|---|---|---|
| US1 — Register Monitor | 5 | Write tests, implement register view, add validation for negative timeout |
| US2 — Device Heartbeat | 5 | Write tests, implement heartbeat view, add 404 for unknown device |
| US3 — Check Device Status | 3 | Write tests, implement status view |

**Total: 13 points**

---

## Sprint 2 Plan

**Sprint Goal:** Add monitoring, logging, and operational visibility with health endpoint, console logging, and alert email backend.

| Story | Points | Tasks |
|---|---|---|
| US5 — Health Endpoint | 2 | Write tests, implement `/health/` view |
| US6 — Console Logging | 2 | Configure `LOGGING` in settings, write test for log output |
| US4 — Pause Monitoring | 3 | Write tests, implement pause view |
| US7 — Alert Email Backend | 3 | Configure email backend, write test for alert email |

**Total: 10 points**

---

## Sprint 1 Review

*(To be filled after Sprint 1)*

## Sprint 1 Retrospective

*(To be filled after Sprint 1)*

## Sprint 2 Review

*(To be filled after Sprint 2)*

## Sprint 2 Retrospective

*(To be filled after Sprint 2)*