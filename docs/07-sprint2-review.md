# Sprint 2 Review

## Sprint Goal
Add health endpoint, console logging, and tests for pause and status endpoints.

## Completed Stories

### US4 — Health endpoint (2 points)
- `app/views.py` — `HealthView` returns `{"status": "ok"}` on `GET /health`
- `app/urls.py` — route registered
- `app/tests/test_health_logging.py` — 1 test
  - `test_health_returns_ok` — GET /health returns 200 with status ok
- **Acceptance criteria: MET**

### US5 — Console logging (2 points)
- `pulse_check/settings.py` — `LOGGING` config with console handler
- `app/views.py` — INFO logs on register, heartbeat, pause, and health requests
- `app/tests/test_health_logging.py` — 2 tests
  - `test_health_endpoint_logs_request` — GET /health produces an INFO log line
  - `test_error_log_emits_at_error_level` — the app logger emits ERROR-level messages
- **Acceptance criteria: MET**

### US6 — Pause monitoring tests (2 points)
- `app/tests/test_pause.py` — 3 tests
  - `test_pause_sets_status_to_paused`
  - `test_pause_already_paused_returns_success`
  - `test_pause_unknown_device_returns_404`
- **Acceptance criteria: MET**

### US7 — Status endpoint tests (2 points)
- `app/tests/test_status.py` — 2 tests
  - `test_status_returns_device_details`
  - `test_status_returns_404_for_unknown_device`
- **Acceptance criteria: MET**

## Retrospective Improvements Applied
1. **Smoke test first** — `app/tests/test_smoke.py` verifies the test environment before any real tests run.
2. **Shared base test class** — `app/tests/test_base.py` centralises Redis/Celery mocking, so new tests inherit it instead of repeating patch decorators.

## Test Results
```
Ran 17 tests in 0.101s
OK
```

Full output: `docs/evidence/sprint2-test-results.txt`

## Total: 8 of 8 points delivered

## Out of Scope
- Alert email backend (US8) — remains in the backlog, not planned for Sprint 2