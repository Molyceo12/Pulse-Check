<div align="center">

# Sprint 2 Review

<img src="https://img.shields.io/badge/Status-Complete-brightgreen" />
<img src="https://img.shields.io/badge/Points-8%2F8-brightgreen" />
<img src="https://img.shields.io/badge/Tests-17%20Passing-brightgreen" />
<img src="https://img.shields.io/badge/CI-Green-success" />

</div>

<details>
<summary><b>📋 Sprint Goal</b></summary>

Add a health endpoint, structured console logging, and tests for the pause and status endpoints.

</details>

<details>
<summary><b>✅ Completed Stories — 8 of 8 points</b></summary>

<br>

<div style="background:#f0f9ff;border-left:4px solid #0ea5e9;padding:12px 16px;border-radius:6px;margin:10px 0;">
<b>US4 — Health Endpoint</b> <span style="color:#0ea5e9;">· 2 points</span><br>
<code>GET /health</code> → <code>{"status": "ok"}</code> with HTTP 200<br>
Tests: <code>test_health_returns_ok</code>
</div>

<div style="background:#f0f9ff;border-left:4px solid #0ea5e9;padding:12px 16px;border-radius:6px;margin:10px 0;">
<b>US5 — Console Logging</b> <span style="color:#0ea5e9;">· 2 points</span><br>
<code>LOGGING</code> configured in <code>settings.py</code> with a console handler<br>
Tests: <code>test_health_endpoint_logs_request</code>, <code>test_error_log_emits_at_error_level</code>
</div>

<div style="background:#f0f9ff;border-left:4px solid #0ea5e9;padding:12px 16px;border-radius:6px;margin:10px 0;">
<b>US6 — Pause Monitoring Tests</b> <span style="color:#0ea5e9;">· 2 points</span><br>
Tests: <code>test_pause_sets_status_to_paused</code>, <code>test_pause_already_paused_returns_success</code>, <code>test_pause_unknown_device_returns_404</code>
</div>

<div style="background:#f0f9ff;border-left:4px solid #0ea5e9;padding:12px 16px;border-radius:6px;margin:10px 0;">
<b>US7 — Status Endpoint Tests</b> <span style="color:#0ea5e9;">· 2 points</span><br>
Tests: <code>test_status_returns_device_details</code>, <code>test_status_returns_404_for_unknown_device</code>
</div>

</details>

<details>
<summary><b>🛠️ Retrospective Improvements Applied</b></summary>

<ol>
<li><b>Smoke test first</b> — <code>app/tests/test_smoke.py</code> verifies the test environment before any real tests run.</li>
<li><b>Shared base test class</b> — <code>app/tests/test_base.py</code> centralises Redis/Celery mocking so new tests inherit it with zero boilerplate.</li>
</ol>

</details>

<details>
<summary><b>🧪 Test Results</b></summary>

<pre style="background:#0f172a;color:#e2e8f0;padding:16px;border-radius:8px;overflow-x:auto;font-size:13px;line-height:1.5;"><code>Ran 17 tests in 0.101s

OK

System check identified no issues (0 silenced).</code></pre>

Full output: <code>docs/evidence/sprint2-test-results.txt</code>

</details>

<details>
<summary><b>⚠️ Out of Scope</b></summary>

Alert email backend (US8) remains in the backlog and was not planned for Sprint 2.

</details>

<details>
<summary><b>🔗 Files Changed</b></summary>

<ul>
<li><code>app/views.py</code> — HealthView + logging</li>
<li><code>app/urls.py</code> — /health route</li>
<li><code>pulse_check/settings.py</code> — LOGGING config</li>
<li><code>app/tests/test_base.py</code> — shared base class</li>
<li><code>app/tests/test_smoke.py</code> — environment smoke test</li>
<li><code>app/tests/test_health_logging.py</code> — US4 + US5 tests</li>
<li><code>app/tests/test_pause.py</code> — US6 tests</li>
<li><code>app/tests/test_status.py</code> — US7 tests</li>
</ul>

</details>

<details>
<summary><b>📝 Commit History</b></summary>

<pre style="background:#0f172a;color:#e2e8f0;padding:16px;border-radius:8px;overflow-x:auto;font-size:13px;line-height:1.5;"><code>55240f2 fix(tests): mock cache.delete and cancel_monitor_timer in base test class
0788d01 docs: add Sprint 2 review and retrospective
6ac2e01 test(US6,US7): pause and status endpoint tests
991519a test(US4,US5): health endpoint and logging tests
78f4f0a feat(US4,US5): add health endpoint and console logging</code></pre>

</details>