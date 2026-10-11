# Sprint 1 Retrospective

## What Went Well

- Tests were written first for each story, which meant failures were caught
  immediately and the code under test was clear.
- Each story was committed separately with conventional messages, making the
  history easy to read and review.
- The CI pipeline was set up early, so the test command was standardised from
  day one.

## What Did Not Go Well

- The first test run failed because `APITestClient` does not exist in DRF 3.18
  — it was renamed to `APIClient`. This cost a few minutes of debugging.
- The register endpoint depends on Redis and Celery, so the test had to mock
  those or it would crash. This was unexpected and added complexity to what
  should have been a simple test.

## Improvements for Sprint 2

1. Write tests first, then check the environment. Before writing a single test,
   verify the test client, settings, and mocking strategy work with a trivial
   test. This would have caught the `APIClient` rename immediately.
2. Isolate external dependencies earlier. The views call Redis and Celery
   directly. For Sprint 2, wrap those calls behind a shared test base class with
   mocks already configured, so new tests do not need to repeat the patch
   decorators.