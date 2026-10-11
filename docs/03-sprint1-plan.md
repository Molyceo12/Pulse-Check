<div align="center">

# Sprint 1 Plan

<img src="https://img.shields.io/badge/Sprint-1-7%20points-brightgreen" />
<img src="https://img.shields.io/badge/Status-Complete-success" />

</div>

<details open>
<summary><b>🎯 Sprint Goal</b></summary>

Deliver unit tests for the register and heartbeat endpoints, add input validation, and set up the CI pipeline.

</details>

<details>
<summary><b>📐 Capacity</b></summary>

<p><b>7 points.</b> First sprint with no velocity history, so we use a conservative estimate based on story size.</p>

</details>

<details open>
<summary><b>📋 Stories and Tasks</b></summary>

<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:0.9em;">
<thead>
<tr style="background:#1e293b;color:#f8fafc;">
<th style="padding:10px;text-align:left;">Story</th>
<th style="padding:10px;text-align:center;">Points</th>
<th style="padding:10px;text-align:left;">Tasks</th>
</tr>
</thead>
<tbody>

<tr style="background:#fef2f2;">
<td style="padding:8px;"><b>US1 — Register Monitor Tests</b></td>
<td style="padding:8px;text-align:center;">3</td>
<td style="padding:8px;">
<ol>
<li>Write test for successful device creation</li>
<li>Write test for negative timeout rejection</li>
<li>Run tests and fix issues</li>
</ol>
</td>
</tr>

<tr style="background:#fef2f2;">
<td style="padding:8px;"><b>US2 — Validation</b></td>
<td style="padding:8px;text-align:center;">2</td>
<td style="padding:8px;">
<ol>
<li>Add serializer validation for negative timeout</li>
<li>Add serializer validation for invalid email</li>
<li>Run tests and fix issues</li>
</ol>
</td>
</tr>

<tr style="background:#fef2f2;">
<td style="padding:8px;"><b>US3 — Heartbeat Tests</b></td>
<td style="padding:8px;text-align:center;">2</td>
<td style="padding:8px;">
<ol>
<li>Write test for successful heartbeat reset</li>
<li>Write test for 404 on unknown device</li>
<li>Run tests and fix issues</li>
</ol>
</td>
</tr>

<tr style="background:#dbeafe;">
<td style="padding:8px;"><b>CI Pipeline</b></td>
<td style="padding:8px;text-align:center;">—</td>
<td style="padding:8px;">
<ol>
<li>Create <code>.github/workflows/ci.yml</code> with Django test job</li>
<li>Push and verify the run is green</li>
</ol>
</td>
</tr>

</tbody>
</table>

</details>

<details>
<summary><b>🧮 Sprint Total</b></summary>

<p><b>7 points</b></p>

</details>

<details>
<summary><b>⚠️ Out of Scope</b></summary>

<ul>
<li>Health endpoint (<code>/health/</code>)</li>
<li>Console logging</li>
<li>Pause monitoring tests</li>
<li>Status endpoint tests</li>
<li>Alert email backend</li>
</ul>

</details>