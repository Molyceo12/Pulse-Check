<div align="center">

# Sprint 1 Review

<img src="https://img.shields.io/badge/Status-Complete-brightgreen" />
<img src="https://img.shields.io/badge/Points-7%2F7-brightgreen" />
<img src="https://img.shields.io/badge/Tests-8%20Passing-brightgreen" />
<img src="https://img.shields.io/badge/CI-Green-success" />

</div>

<details>
<summary><b>📋 Sprint Goal</b></summary>

Deliver unit tests for the register and heartbeat endpoints, add input validation, and set up the CI pipeline.

</details>

<details>
<summary><b>✅ Completed Stories — 7 of 7 points</b></summary>

<br>

<div style="background:#fef2f2;border-left:4px solid #ef4444;padding:12px 16px;border-radius:6px;margin:10px 0;">
<b>US1 — Register Monitor Tests</b> <span style="color:#ef4444;">· 3 points</span><br>
Tests: <code>test_register_creates_device_successfully</code>, <code>test_register_rejects_negative_timeout</code><br>
<b>Acceptance criteria: MET</b>
</div>

<div style="background:#fef2f2;border-left:4px solid #ef4444;padding:12px 16px;border-radius:6px;margin:10px 0;">
<b>US2 — Validation Tests</b> <span style="color:#ef4444;">· 2 points</span><br>
Tests: <code>test_negative_timeout_rejected</code>, <code>test_empty_id_rejected</code>, <code>test_invalid_email_rejected</code>, <code>test_endpoint_rejects_invalid_email</code><br>
<b>Acceptance criteria: MET</b>
</div>

<div style="background:#fef2f2;border-left:4px solid #ef4444;padding:12px 16px;border-radius:6px;margin:10px 0;">
<b>US3 — Heartbeat Tests</b> <span style="color:#ef4444;">· 2 points</span><br>
Tests: <code>test_heartbeat_resets_timer_and_updates_status</code>, <code>test_heartbeat_returns_404_for_unknown_device</code><br>
<b>Acceptance criteria: MET</b>
</div>

<div style="background:#f0f9ff;border-left:4px solid #0ea5e9;padding:12px 16px;border-radius:6px;margin:10px 0;">
<b>CI Pipeline</b> <span style="color:#0ea5e9;">· GitHub Actions</span><br>
<code>.github/workflows/ci.yml</code> — runs on push and PR with Redis service container<br>
<b>Acceptance criteria: MET</b>
</div>

</details>

<details>
<summary><b>🧪 Test Results</b></summary>

<pre style="background:#0f172a;color:#e2e8f0;padding:16px;border-radius:8px;overflow-x:auto;font-size:13px;line-height:1.5;"><code>Ran 8 tests in 0.089s

OK

System check identified no issues (0 silenced).</code></pre>

Full output: <code>docs/evidence/sprint1-test-results.txt</code>

</details>

<details>
<summary><b>🔗 Files Changed</b></summary>

<ul>
<li><code>.github/workflows/ci.yml</code> — CI workflow</li>
<li><code>app/tests/test_register.py</code> — US1 tests</li>
<li><code>app/tests/test_heartbeat.py</code> — US3 tests</li>
<li><code>app/tests/test_validation.py</code> — US2 tests</li>
<li><code>pulse_check/test_settings.py</code> — SQLite test settings</li>
<li><code>docs/04-sprint1-review.md</code> — this file</li>
<li><code>docs/05-sprint1-retrospective.md</code> — retro</li>
</ul>

</details>

<details>
<summary><b>⚠️ Out of Scope</b></summary>

Health endpoint, console logging, pause/status tests, and alert email backend were not started.

</details>