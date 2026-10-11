# Sprint 2 Plan

## Sprint Goal

Add a health endpoint, structured console logging, and tests for the pause
and status endpoints.

## Capacity

8 points. Sprint 2 builds on the shared base test class and smoke test
improvements from the Sprint 1 retrospective.

## Stories and Tasks

| Story                          | Points | Tasks                                                                 |
|--------------------------------|--------|-----------------------------------------------------------------------|
| US4 — Health Endpoint          | 2      | Create `HealthView` returning `{"status": "ok"}`                      |
|                                |        | Register `/health` route in `app/urls.py`                             |
|                                |        | Write test for 200 response                                          |
| US5 — Console Logging          | 2      | Add `LOGGING` config in `pulse_check/settings.py`                     |
|                                |        | Add INFO logs for requests in `app/views.py`                         |
|                                |        | Write test for INFO and ERROR log output                             |
| US6 — Pause Monitoring Tests   | 2      | Write test for pause sets status to `paused`                         |
|                                |        | Write test for pause already paused device                           |
|                                |        | Write test for 404 on unknown device                                 |
| US7 — Status Endpoint Tests    | 2      | Write test for status returns device details                         |
|                                |        | Write test for 404 on unknown device                                 |

## Sprint Total

8 points

## Out of Scope

- Alert email backend (US8)