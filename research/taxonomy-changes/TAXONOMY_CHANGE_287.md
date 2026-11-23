# Taxonomy Change 287 — Afterplace touch controls and reactive instruction

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-11-17.
- Trigger: [GAME-0540](../../knowledge/games/a-f/afterplace.md),
  full launch-era iPhone Afterplace from the glade to the stream and back.

| Addition | Reviewed boundary | Counterexample |
| --- | --- | --- |
| `ACT-737` | Drag from a flexible origin to steer or tap the same play surface to act on context. | `ACT-008` does not constrain the input surface. `ACT-588` commits discrete turn or obstacle responses while forward motion is automatic. |
| `SYS-1561` | An added touch allows independent action while the first touch is steering. | Permanent move and attack controls do not adapt to touch count. `CON-031` applies to shared control of multiple actors. |
| `SYS-1562` | Successful repetitions of the explained action can elicit different authored replies from the same local tutor. | `SYS-736` exposes a next required step after a completion predicate. `INF-268` supplies current objective information. |

Eight existing definitions transfer. The gesture recognizer and
context choice are distinct from the weapon impact itself. The
recorded return is an analysis boundary, so it adds no mandatory
combat clearance or scenario objective. No verified combination
is a proper subset.
