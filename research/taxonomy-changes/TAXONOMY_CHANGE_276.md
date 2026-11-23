# Taxonomy Change 276 — Tetris Effect placement and Zone

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-11-17.
- Trigger: [GAME-0529](../../knowledge/games/s-z/tetris-effect.md), pre-Connected
  PlayStation 4 release, first Normal Journey stage.

| Addition | Reviewed boundary | Counterexample |
| --- | --- | --- |
| `ACT-722` | Commit instantly at the last unobstructed pose along the current drop path. | `ACT-006` changes the speed of continuing descent. |
| `ACT-723` | Hold one shape, replacing the active piece with the reserved shape or the queue head and allowing another exchange after settlement. | `SYS-009` introduces the successor after normal lock. |
| `ACT-724` | Choose when to spend earned gauge for the playable placement mode. | `ACT-236` activates a rechargeable equipped combat item. |
| `SYS-1520` | Convert eligible normal clears into a spendable interval that suspends gravity while placement remains live. | `TIM-007` goes back to a previously lived state. |
| `SYS-1521` | Completed rows occupy a new position at the bottom. Exit removes the band for score outside the ordinary quota. | `SYS-008` removes and collapses ordinary rows during lock settlement. |
| `SYS-1522` | Resolve rotation against a declared order of offset candidates rather than only the unshifted pose. | `CON-007` requires a permitted pose but does not pick the order of alternate poses. |
| `INF-514` | Show where the current shape on its current path would be stopped. | `INF-005` reveals what comes into play next. |

Seventeen definitions transfer. Seven-bag composition, the stage target,
score table, hold capacity and duration thresholds are parameters. Early
write-ups establish the temporary row band. No executable timing or
exact offset table is asserted for the original PS4 release. The ordered
rotation correction alone is assessed at Medium confidence.

The new signature also supports the existing `COMB-0004` subset during
ordinary play. Zone receives no new verified combination from this single
scoped witness.
