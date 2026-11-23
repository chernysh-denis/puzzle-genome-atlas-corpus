# Taxonomy Change 324 — Redirect a braking drift during a timed road route

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-11-20.
- Trigger: [GAME-0578](../../knowledge/games/m-r/outrun-2.md),
  one original Xbox OutRun Mode drive with automatic transmission.

| Addition | Accepted boundary | Rejected substitution |
| --- | --- | --- |
| SYS-1698 | Release acceleration, brake and steer into the bend, then reapply acceleration in a controllable slide. Opposite steering with a further release and reapplication redirects the active slide. | SYS-1595 uses released-throttle steering to prepare a tail slide and ties slip strength to how long the input is held. ACT-468 and SYS-892 charge a boost settled on release. SYS-1257 suppresses off-road slowing during a gear transition. |

The original Xbox printed instructions establish ordinary inputs and both
slide states. Native stills corroborate the trajectory but do not show
input timings. Existing steering, contact, moving traffic, live fork,
checkpoint time, deadline, driving telemetry, route result, score, final
goal and real-time boundaries apply with local parameters. The absence of
an independently measured score formula or last-tick timer policy leaves
SYS-1029, SYS-1258 and CON-745 outside this signature.

The Ukrainian definition and all twelve bilingual player explanations
were reviewed. No prior signature, original definition or verified
combination was changed.
