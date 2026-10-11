# Sprint 1 Review

## Sprint Goal
Deliver unit tests for the register and heartbeat endpoints, add input validation, and set up the CI pipeline.

## Completed Stories

### US1 — Unit tests for register monitor endpoint (3 points)
- `app/tests/test_register.py` — 2 tests
  - Valid registration returns 201 and creates the device
  - Negative timeout returns 400 and no device is created
- **Acceptance criteria: MET**

### US2 — Validation for negative timeouts and invalid emails (2 points)
- `app/tests/test_validation.py` — 4 tests
  - Serializer rejects timeout <= 0
  - Serializer rejects blank device ID
  - Serializer rejects malformed email
  - API returns 400 for invalid email via register endpoint
- **Acceptance criteria: MET**

### US3 — Unit tests for heartbeat endpoint (2 points)
- `app/tests/test_heartbeat.py` — 2 tests
  - Heartbeat updates last_heartbeat and returns success
  - Unknown device returns 404
- **Acceptance criteria: MET**

### CI Pipeline
- `.github/workflows/ci.yml` — GitHub Actions workflow
  - Runs on push and pull request to `main`
  - Installs dependencies and runs all tests
  - Redis service container provided
- **Acceptance criteria: MET**

## Test Results
```
Ran 8 tests in 0.089s
OK
```

Full output: `docs/evidence/sprint1-test-results.txt`

## Total: 7 of 7 points delivered

## Out of Scope (not started)
- Health endpoint (`/health/`)
- Console logging
- Pause monitoring tests
- Status endpoint tests
- Alert email backend