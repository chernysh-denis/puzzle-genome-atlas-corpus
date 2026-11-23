# Taxonomy Change 315 — Temporary route edits and outstanding gold

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-11-20.
- Trigger: [GAME-0569](../../knowledge/games/g-l/lode-runner.md), level 001 of
  the original Apple II Lode Runner, ending at level 002 entry.

| Addition | Accepted boundary | Rejected substitution |
| --- | --- | --- |
| ACT-772 | Select and fully dig one eligible lower diagonal brick. | ACT-303 applies general targeted breach. The separate dig controls choose a fixed adjacent relation to the runner, with a side-clearance gate and no freely aimed damage. |
| SYS-1665 | A dug cell times its return and resolves occupants. | SYS-1662 retains surrounding solid after a local voxel edit. It does not restore the removed cell or close onto its occupants. |
| SYS-1666 | A held pursuer is temporary safe footing, with escape and replacement branches. | SYS-983 treats a living guardian as changing climb topology. A locally trapped guard has a specific safe crossing window and later ordinary pursuit or replacement. |
| SYS-1667 | Pursuers reselect approaches on live horizontal and vertical routes. | SYS-057 concerns detection response. Here guard pursuit uses current reachable platform links and is not gated by a perception trigger. |
| SYS-1668 | Carried gold is out of view and still outstanding, with drop and retirement branches. | SYS-037 remains the player pickup. Taking gold as a guard changes its custody and visibility without giving player credit. |
| SYS-1669 | The resolved count installs authored ladder cells. | Marking an exit alone supplies no new climb affordance. The world state changes before the runner's terminal check. |
| OBJ-311 | A resolved outstanding set plus a live upper-boundary arrival advances the level. | OBJ-018 requires receiving its staged tokens. OBJ-154 additionally needs a retained rated terminal report. OBJ-310 needs timed escape. |

The six reused definitions retain their published boundaries. Contact pickup,
life consumption, whole-board restoration and real-time progression remain
distinct. Six chests, three guards, four ladder cells and five original lives
are scope parameters. Archival code supports the blocked-release and burial
exceptions, without a native measurement of whether each case can be forced
on level 001. No predecessor definition, signature or release is rewritten.

All seven newly introduced definitions have reviewed Ukrainian labels,
definitions, inclusions and exclusions. All thirteen game genes have reviewed
bilingual examples and named salience.
