<div align="center">

# Sprint 1 Retrospective

<img src="https://img.shields.io/badge/Retrospective-Sprint%201-blue" />

</div>

<details>
<summary><b>✅ What Went Well</b></summary>

<ul>
<li>Tests were written first for each story, which meant failures were caught immediately and the code under test was clear.</li>
<li>Each story was committed separately with conventional messages, making the history easy to read and review.</li>
<li>The CI pipeline was set up early, so the test command was standardised from day one.</li>
</ul>

</details>

<details>
<summary><b>❌ What Did Not Go Well</b></summary>

<ul>
<li>The first test run failed because <code>APITestClient</code> does not exist in DRF 3.18 — it was renamed to <code>APIClient</code>. This cost a few minutes of debugging.</li>
<li>The register endpoint depends on Redis and Celery, so the test had to mock those or it would crash. This was unexpected and added complexity to what should have been a simple test.</li>
</ul>

</details>

<details>
<summary><b>🚀 Improvements for Sprint 2</b></summary>

<ol>
<li><b>Write tests first, then check the environment.</b> Before writing a single test, verify the test client, settings, and mocking strategy work with a trivial test. This would have caught the <code>APIClient</code> rename immediately.</li>
<li><b>Isolate external dependencies earlier.</b> The views call Redis and Celery directly. For Sprint 2, consider wrapping those calls behind a small service layer or using a shared test base class with mocks already configured, so new tests do not need to repeat the patch decorators.</li>
</ol>

</details>