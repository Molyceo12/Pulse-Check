# Sprint 2 Retrospective

## What Went Well
- The shared base test class (`BaseMonitorTestCase`) eliminated the per-test patch decorators that slowed Sprint 1. New tests inherit mocking automatically.
- The smoke test (`test_smoke.py`) verified the environment before any real tests ran, catching issues immediately.
- All 4 stories were delivered with tests written first, and every test passed on the first run after the base class was in place.

## What Did Not Go Well
- The error logging test was difficult to write because `get_object_or_404` swallows exceptions and returns 404. Testing the logger directly was simpler and more reliable.
- The PowerShell environment made saving test output noisy. A small Python script would have been cleaner.

## Were Sprint 1 Improvements Effective?
- **Yes.** The shared base class removed the repetitive `@patch` decorators from every test. New tests in Sprint 2 had no mocking boilerplate at all.
- **Mostly.** The smoke test caught the environment early, but it only verified the happy path. A test that deliberately triggers a mocked failure would have been more thorough.

## Lessons Learned
- A shared base test class pays for itself after the second test file — it saves more than it costs.
- Testing the logger directly is more reliable than trying to force an exception through Django's request pipeline.

## Further Improvements for Sprint 3
1. Add a CI linting step (e.g., flake8 or ruff) to catch style issues before they reach the test phase.
2. Create a small service layer for Redis and Celery calls so views stay thin and even easier to mock.