# Taxonomy Change 199: physical shooter branch and vehicle authority

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Direct
- Confidence: High
- Date: 2026-10-01.
- Trigger: `GAME-0462`, original Neo Geo MVS *Metal Slug 3* first mission's boat branch.
- Scope: three new Active definitions among eighteen uses. No earlier signature, verified combination or published corpus revision changes.

## Evidence and boundary tests

The [canonical game ledger](../../knowledge/games/m-r/metal-slug-3.md) uses original SNK operations, crossroads and item pages archived from the period. No cabinet, ROM or direct play was inspected. Written routes corroborate the first boss and tank approach but do not establish exact cabinet timings.

- `ACT-613` is a physical entry at a live stage crossroads. It excludes `ACT-127`, which chooses a visible successor on an abstract route map, and `ACT-530`, which chooses an edge while a board token spends one die roll.
- `SYS-1212` describes the boat's authored downstream movement while a passenger still fights. Neither `ACT-201` nor `SYS-320` fits the boat because it is not directly steered. Those existing genes do fit the later driven Metal Slug tank.
- `ACT-614` is an explicit A+B self-destruct assault, sacrificing an occupied vehicle. It differs from `ACT-379`'s recoverable vehicle ram and `SYS-320`'s hostile-caused damage/explosion.

## Reuse and disposition

Fifteen other uses fit direct movement, attack and posture; live enemies/combat, typed contact bonuses, vehicle handling and life respawn; finite ammunition; local viewport/HUD; first-stage boss and real-time pressure. The zero timer costs a life and is therefore not `CON-068`'s whole-attempt terminal deadline while lives remain. The existing `FAM-009` and `FAM-010` cover this packet without a single-game family. New definitions receive full Ukrainian review in the same unit.
