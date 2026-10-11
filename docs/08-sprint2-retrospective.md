<div align="center">

# Sprint 2 Retrospective

<img src="https://img.shields.io/badge/Retrospective-Sprint%202-blue" />

</div>

<details>
<summary><b>✅ What Went Well</b></summary>

<ul>
<li>The shared base test class (<code>BaseMonitorTestCase</code>) eliminated per-test patch decorators that slowed Sprint 1. New tests inherit mocking automatically.</li>
<li>The smoke test (<code>test_smoke.py</code>) verified the environment before any real tests ran, catching issues immediately.</li>
<li>All 4 stories were delivered with tests written first, and every test passed on the first run after the base class was in place.</li>
</ul>

</details>

<details>
<summary><b>❌ What Did Not Go Well</b></summary>

<ul>
<li>The error logging test was difficult to write because <code>get_object_or_404</code> swallows exceptions and returns 404. Testing the logger directly was simpler and more reliable.</li>
<li>The PowerShell environment made saving test output noisy. A small Python script would have been cleaner.</li>
</ul>

</details>

<details>
<summary><b>🔍 Were Sprint 1 Improvements Effective?</b></summary>

<ol>
<li><b>Yes.</b> The shared base class removed the repetitive <code>@patch</code> decorators from every test. New tests in Sprint 2 had no mocking boilerplate at all.</li>
<li><b>Mostly.</b> The smoke test caught the environment early, but it only verified the happy path. A test that deliberately triggers a mocked failure would have been more thorough.</li>
</ol>

</details>

<details>
<summary><b>📚 Lessons Learned</b></summary>

<ul>
<li>A shared base test class pays for itself after the second test file — it saves more than it costs.</li>
<li>Testing the logger directly is more reliable than trying to force an exception through Django's request pipeline.</li>
</ul>

</details>

<details>
<summary><b>🚀 Further Improvements for Sprint 3</b></summary>

<ol>
<li>Add a CI linting step (e.g., flake8 or ruff) to catch style issues before they reach the test phase.</li>
<li>Create a small service layer for Redis and Celery calls so views stay thin and even easier to mock.</li>
</ol>

</details>