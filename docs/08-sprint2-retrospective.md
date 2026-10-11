# Sprint 2 Retrospective

## What Went Well

- The shared base test class removed the repetitive patch decorators from every test. New tests in Sprint 2 had no mocking boilerplate at all.
- The smoke test verified the test environment before any real tests ran, catching issues early.
- All 4 stories were delivered with tests written first, and every test passed on the first run.

## What Did Not Go Well

- The error logging test was hard to write because `get_object_or_404` swallows exceptions and returns 404. Testing the logger directly was simpler.
- The PowerShell environment made saving test output noisy. A small Python script would have been cleaner.

## Were Sprint 1 Improvements Effective?

1. Yes. The shared base class removed the repetitive `@patch` decorators from every test. New tests in Sprint 2 had no mocking boilerplate at all.
2. Mostly. The smoke test caught the environment early, but it only verified the happy path. A test that deliberately triggers a mocked failure would have been more thorough.

## Lessons Learned

- A shared base test class pays for itself after the second test file. It saves more than it costs.
- Testing the logger directly is more reliable than trying to force an exception through Django's request pipeline.

## Further Improvements for Sprint 3

1. Add a CI linting step (e.g., flake8 or ruff) to catch style issues before they reach the test phase.
2. Create a small service layer for Redis and Celery calls so views stay thin and even easier to mock.