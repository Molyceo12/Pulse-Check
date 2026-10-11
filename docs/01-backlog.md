<div align="center">

# Product Backlog

<img src="https://img.shields.io/badge/Priority-MoSCoW-orange" />
<img src="https://img.shields.io/badge/Estimates-Fibonacci%20points-orange" />

</div>

<details>
<summary><b>📐 Estimating Method</b></summary>

<p>Priority: <b>MoSCoW</b> (Must / Should / Could / Won't). Estimates: Fibonacci story points (1, 2, 3, 5, 8). Reference story (= 2 points): <b>Health endpoint</b> — a small, self-contained feature with a single view and one test, easy to size reliably.</p>

</details>

<details open>
<summary><b>📊 Story Table</b></summary>

<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:0.9em;">
<thead>
<tr style="background:#1e293b;color:#f8fafc;">
<th style="padding:10px;text-align:left;">ID</th>
<th style="padding:10px;text-align:left;">Story</th>
<th style="padding:10px;text-align:left;">Priority</th>
<th style="padding:10px;text-align:center;">Points</th>
<th style="padding:10px;text-align:center;">Sprint</th>
</tr>
</thead>
<tbody>

<tr style="background:#fef2f2;"><td style="padding:8px;"><b>US1</b></td><td style="padding:8px;">Unit tests for register monitor endpoint</td><td style="padding:8px;"><span style="background:#fee2e2;color:#991b1b;padding:2px 8px;border-radius:12px;font-size:0.8em;">Must</span></td><td style="padding:8px;text-align:center;">3</td><td style="padding:8px;text-align:center;">✅ Sprint 1</td></tr>

<tr style="background:#fef2f2;"><td style="padding:8px;"><b>US2</b></td><td style="padding:8px;">Validation for negative timeouts and invalid emails</td><td style="padding:8px;"><span style="background:#fee2e2;color:#991b1b;padding:2px 8px;border-radius:12px;font-size:0.8em;">Must</span></td><td style="padding:8px;text-align:center;">2</td><td style="padding:8px;text-align:center;">✅ Sprint 1</td></tr>

<tr style="background:#fef2f2;"><td style="padding:8px;"><b>US3</b></td><td style="padding:8px;">Unit tests for heartbeat endpoint</td><td style="padding:8px;"><span style="background:#fee2e2;color:#991b1b;padding:2px 8px;border-radius:12px;font-size:0.8em;">Must</span></td><td style="padding:8px;text-align:center;">2</td><td style="padding:8px;text-align:center;">✅ Sprint 1</td></tr>

<tr style="background:#dbeafe;"><td style="padding:8px;"><b>US4</b></td><td style="padding:8px;">Health endpoint (<code>/health/</code>)</td><td style="padding:8px;"><span style="background:#dbeafe;color:#1e40af;padding:2px 8px;border-radius:12px;font-size:0.8em;">Should</span></td><td style="padding:8px;text-align:center;">2</td><td style="padding:8px;text-align:center;">✅ Sprint 2</td></tr>

<tr style="background:#dbeafe;"><td style="padding:8px;"><b>US5</b></td><td style="padding:8px;">Console logging for requests and errors</td><td style="padding:8px;"><span style="background:#dbeafe;color:#1e40af;padding:2px 8px;border-radius:12px;font-size:0.8em;">Should</span></td><td style="padding:8px;text-align:center;">2</td><td style="padding:8px;text-align:center;">✅ Sprint 2</td></tr>

<tr style="background:#dbeafe;"><td style="padding:8px;"><b>US6</b></td><td style="padding:8px;">Unit tests for pause monitoring endpoint</td><td style="padding:8px;"><span style="background:#dbeafe;color:#1e40af;padding:2px 8px;border-radius:12px;font-size:0.8em;">Should</span></td><td style="padding:8px;text-align:center;">2</td><td style="padding:8px;text-align:center;">✅ Sprint 2</td></tr>

<tr style="background:#dbeafe;"><td style="padding:8px;"><b>US7</b></td><td style="padding:8px;">Unit tests for status endpoint</td><td style="padding:8px;"><span style="background:#dbeafe;color:#1e40af;padding:2px 8px;border-radius:12px;font-size:0.8em;">Should</span></td><td style="padding:8px;text-align:center;">2</td><td style="padding:8px;text-align:center;">✅ Sprint 2</td></tr>

<tr style="background:#f1f5f9;"><td style="padding:8px;"><b>US8</b></td><td style="padding:8px;">Alert email backend</td><td style="padding:8px;"><span style="background:#e2e8f0;color:#475569;padding:2px 8px;border-radius:12px;font-size:0.8em;">Could</span></td><td style="padding:8px;text-align:center;">3</td><td style="padding:8px;text-align:center;">⏳ Backlog</td></tr>

</tbody>
</table>

</details>

<details>
<summary><b>🧮 Sprint Totals</b></summary>

<ul>
<li><b>Sprint 1:</b> 7 points (US1, US2, US3) — <span style="color:#16a34a;">complete</span></li>
<li><b>Sprint 2:</b> 8 points (US4, US5, US6, US7) — <span style="color:#16a34a;">complete</span></li>
<li><b>Backlog:</b> 3 points (US8) — <span style="color:#64748b;">not planned</span></li>
</ul>

</details>

<details>
<summary><b>💡 Prioritisation Rationale</b></summary>

<ol>
<li><b>Must first:</b> Tests and validation protect the existing app from regressions and bad data, which is essential before adding new features.</li>
<li><b>Should next:</b> Health endpoint and logging are low-effort, high-value operational improvements that work for every future feature.</li>
<li><b>Could last:</b> Alert email backend depends on external infrastructure (SMTP) and is lower priority for a first working prototype.</li>
</ol>

</details>

<details open>
<summary><b>📝 Acceptance Criteria</b></summary>

<div style="background:#fef2f2;border-left:4px solid #ef4444;padding:12px 16px;border-radius:6px;margin:10px 0;">
<b>US1 — Unit tests for register monitor endpoint</b><br>
<b>Given</b> a POST request to <code>/register_monitor</code> with valid data<br>
<b>When</b> the endpoint is called<br>
<b>Then</b> a <code>201</code> response is returned and the device is saved in the database<br>
<b>Given</b> a POST request with a negative <code>timeout</code><br>
<b>When</b> the endpoint is called<br>
<b>Then</b> a <code>400</code> error is returned and no device is created <span style="color:#ef4444;">(error case)</span>
</div>

<div style="background:#fef2f2;border-left:4px solid #ef4444;padding:12px 16px;border-radius:6px;margin:10px 0;">
<b>US2 — Validation for negative timeouts and invalid emails</b><br>
<b>Given</b> a POST request with <code>timeout</code> set to <code>-5</code><br>
<b>When</b> the endpoint is called<br>
<b>Then</b> a <code>400</code> error is returned with a clear validation message <span style="color:#ef4444;">(error case)</span><br>
<b>Given</b> a POST request with an invalid <code>alert_email</code><br>
<b>When</b> the endpoint is called<br>
<b>Then</b> a <code>400</code> error is returned and the device is not saved <span style="color:#ef4444;">(error case)</span>
</div>

<div style="background:#fef2f2;border-left:4px solid #ef4444;padding:12px 16px;border-radius:6px;margin:10px 0;">
<b>US3 — Unit tests for heartbeat endpoint</b><br>
<b>Given</b> a registered device exists<br>
<b>When</b> a POST request is sent to <code>/monitors/{id}/heartbeat</code><br>
<b>Then</b> the device's <code>last_heartbeat</code> is updated and a <code>200</code> response is returned<br>
<b>Given</b> a device that does not exist<br>
<b>When</b> a POST request is sent to its heartbeat endpoint<br>
<b>Then</b> a <code>404</code> error is returned <span style="color:#ef4444;">(error case)</span>
</div>

<div style="background:#dbeafe;border-left:4px solid #0ea5e9;padding:12px 16px;border-radius:6px;margin:10px 0;">
<b>US4 — Health endpoint</b><br>
<b>Given</b> the API is running<br>
<b>When</b> a GET request is sent to <code>/health/</code><br>
<b>Then</b> <code>{"status": "ok"}</code> is returned with HTTP <code>200</code> <span style="color:#0ea5e9;">(error case: endpoint must always respond)</span>
</div>

<div style="background:#dbeafe;border-left:4px solid #0ea5e9;padding:12px 16px;border-radius:6px;margin:10px 0;">
<b>US5 — Console logging for requests and errors</b><br>
<b>Given</b> logging is configured in Django settings<br>
<b>When</b> any request is handled<br>
<b>Then</b> a log line with the request method and path is printed to the console<br>
<b>Given</b> an error occurs during request handling<br>
<b>Then</b> an error-level log line is printed to the console <span style="color:#0ea5e9;">(error case)</span>
</div>

<div style="background:#dbeafe;border-left:4px solid #0ea5e9;padding:12px 16px;border-radius:6px;margin:10px 0;">
<b>US6 — Unit tests for pause monitoring endpoint</b><br>
<b>Given</b> an active device exists<br>
<b>When</b> a POST request is sent to <code>/monitors/{id}/pause</code><br>
<b>Then</b> the device status is changed to <code>paused</code> and a success response is returned<br>
<b>Given</b> a device that is already paused<br>
<b>When</b> a pause request is sent<br>
<b>Then</b> a <code>400</code> error is returned because the device is not active <span style="color:#0ea5e9;">(error case)</span>
</div>

<div style="background:#dbeafe;border-left:4px solid #0ea5e9;padding:12px 16px;border-radius:6px;margin:10px 0;">
<b>US7 — Unit tests for status endpoint</b><br>
<b>Given</b> a registered device exists<br>
<b>When</b> a GET request is sent to <code>/monitors/{id}/status</code><br>
<b>Then</b> the device's current status, timeout, last heartbeat, and alert email are returned<br>
<b>Given</b> a device that does not exist<br>
<b>When</b> a GET request is sent to its status endpoint<br>
<b>Then</b> a <code>404</code> error is returned <span style="color:#0ea5e9;">(error case)</span>
</div>

<div style="background:#fef3c7;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:6px;margin:10px 0;">
<b>US8 — Alert email backend</b><br>
<b>Given</b> a device misses its heartbeat window<br>
<b>When</b> the watchdog timer fires<br>
<b>Then</b> an email is sent to the device's <code>alert_email</code> using a real backend <span style="color:#f59e0b;">(error case: email must not crash the worker)</span>
</div>

</details>