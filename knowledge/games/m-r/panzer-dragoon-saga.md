---
game_id: GAME-0647
slug: panzer-dragoon-saga
game_title: Panzer Dragoon Saga
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-860
  system:
    - SYS-822
    - SYS-1867
    - SYS-1868
    - SYS-1869
  constraint:
    - CON-634
  information:
    - INF-600
  objective:
    - OBJ-029
  time:
    - TIM-003
    - TIM-046
---

# Game: Panzer Dragoon Saga

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: original North American English Sega Saturn retail
  disc 1, Sega product 81307, documented disc program MK-81307 V1.000, 1998.
  The North American disc identity is corroborated separately from the
  recordings, which do not show hashes or their full hardware setup.
- Entry: after the captain scene and the optional battle explanation, fly
  through Excavation Site #4 in the Valley until the first live Pattergo
  encounter shown in both runs. The actual formation differs between runs.
- Primary decision loop: move between sectors around the hostile group,
  hold one position to fill Synchronicity, inspect or choose a payable
  command during the paused window, and finish the enemy formation.
- Exit: see the actual Close Call evaluation and credited EXP and Dyne,
  then regain direct field flight at the excavation crossing.
- Included: the initial dragon, sector selection and danger radar, finite
  readiness segments, the paused command window, targeted gun and homing
  laser, incoming attack consequences, grade and payout, and resumed flight.
- Excluded: the ground prologue, the tutorial simulations as combat results,
  later fights, morphing, later Berserks and laser ranks, exact frame costs and
  grade thresholds, field radar prediction formulas, and save or reload rules.
- Suggested later scope: compare different grades against the same Pattergo
  formation at matched character state and count the isolated effect of delay.

## Direct-play status

No direct play was performed. Sega's original English booklet identifies
product 81307 and describes the combat, positioning, pause and evaluation.
A documented retail disc inspection provides the region and program identity.
Wounded Turtle attributes the second recording to US disc 1. LongplayArchive
labels the first recording NTSC and shows the same English opening, with a
different formation variant. Neither video shows an authenticated disc hash
or has verified input or capture hardware. Frames were inspected in the
background without audio. The result ledger uses the recorded screen values.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PDS-001 | The scoped release is the North American English Saturn disc 1 of Sega product 81307, documented as MK-81307 V1.000. | Confirmed | Direct | High | P1 cover/catalogue marking, P2 verified disc record. W2 attributes the playthrough to US disc 1. |
| PDS-002 | The first live fight in both scoped traces occurs after the return to the excavation area and shows a Pattergo title. Combat replaces navigable field flight. | Observation | Corroborated | High | W1 32:23–32:43 and W2 42:06–42:17. W2's separate tutorial closes before the observed live result. |
| PDS-003 | Left or right movement changes the dragon's combat position about the hostile formation by one quarter-turn. The four-sector radar distinguishes safe green, uncolored ordinary danger and red high danger. | Observation | Corroborated | High | P1 pp. 17–18. W1 32:43–33:03 and W2 42:24–42:27 show relative changes around the group and the radar. Exact input timing and every reachable sector were not tested. |
| PDS-004 | Standing in a combat position with no current action allows up to three readiness segments to fill. No progress occurs during repositioning, execution or the opened Command window. The opened window suspends both sides. Gun and homing laser each use one ready segment. | Observation | Corroborated | High | P1 pp. 16–19, W1 32:51–33:08 and 33:20–33:28, W2 42:16–42:21 and 42:34–42:39. The footage shows menus and changing segment states. It does not measure exact refill rates. |
| PDS-005 | The laser command applies homing fire to multiple nearby eligible opponents. The gun takes one selected target. The enemy alternates actions with a response window, and Green Orb visibly reduces the dragon from 400 HP to 352 in both encounters. | Observation | Corroborated | High | P1 pp. 19–20. W1 33:00–33:21 shows four laser hits, gun selection and the HP debit. W2 42:19–42:35 shows a four-target volley and the same debit. W1 also shows Regenerate before the final clear. |
| PDS-006 | Eliminating the required formation awards Close Call and separate payouts. W1 shows 17 EXP and 31 Dyne. W2 shows 16 EXP and 28 Dyne. The grade and payout are distinct. | Observation | Corroborated | High | P1 p. 20 describes the evaluation and performance-based rewards. W2 39:24–39:30 explains speed and damage criteria. Live results are W1 33:30–33:39 and W2 42:40–42:48. Formation and route differ, so no isolated grade coefficient is inferred. |
| PDS-007 | After the result, the controllable dragon is back in the excavation canyon and can navigate from the crossing. W1 interacts with an ordinary field target. W2 flies past scaffolding before a separate encounter. | Observation | Corroborated | High | W1 33:41–33:53 and W2 42:50–42:55. No save or reload is used to establish this immediate continuation. |

## Basic data

- Analysis target: `PLAT-SEGA-SATURN`, original North American 81307 disc 1.
- Developer: Team Andromeda. Publisher: Sega.
- Mechanical family: `FAM-010`, real-time system pressure.
- Checked: 2026-11-22.
- P1: [Sega's original North American instruction booklet](https://www.digitpress.com/library/manuals/saturn/panzer_dragoon_saga.pdf),
  cover and printed pp. 16–21. The booklet explains release controls,
  and its evaluation terminology is kept separate from the observed grade.
- P2: [Verified US retail disc 1 record](https://redump.info/disc/20344).
  Disc serial 81307, internal program MK-81307 V1.000.
- W1: [LongplayArchive, NTSC-labelled Saturn playthrough](https://www.youtube.com/watch?v=Txks9hG21qs&t=1943s).
  First Pattergo fight and settlement.
- W2: [Wounded Turtle, USA disc 1 playthrough](https://www.youtube.com/watch?v=UP_gW-ZLEOM&t=2526s).
  First live fight. The earlier on-disc explanation at 39:24 is separate.

## Mechanical decomposition

### Action Genes

- ACT-008: directly fly past scaffolding and over the crossing once the
  field camera and navigation return.
- ACT-161: aim the gun at one Pattergo target and fire.
- ACT-860: advance left or right into an adjacent combat quadrant around
  the target group.

### System Behaviour Genes

- SYS-822: settle the bounded fight into a conduct-sensitive evaluation.
- SYS-1867: accumulate discrete ready battle segments only while stationary
  and free of execution. Spend a ready segment on one ordinary attack.
- SYS-1868: one paid homing command resolves against multiple selected
  nearby targets without manually acquiring each one.
- SYS-1869: the encounter produces separate EXP and currency awards that
  depend on its evaluation as well as the combat settlement.

### Constraint Genes

- CON-634: an ordinary attack requires sufficient completed readiness and
  a compatible command and targeting state.

### Information Genes

- INF-600: compare the dragon's position with the safe, ordinary and
  high-danger quadrants on the battle radar.

### Objective Genes

- OBJ-029: eliminate the live Pattergo formation and reach a valid victory
  before the dragon is defeated.

### Time Genes

- TIM-003: change position and decide when to spend readiness while the
  live encounter advances.
- TIM-046: the combat command window stops enemy and player advancement
  as well as gauge growth until the command or cancel returns to the fight.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| Controllable dragon crossing the excavation | Enter the live encounter after the optional explanations | Pattergo title, combat formation, battle position and gauge replace field flight | PDS-002 |
| Dragon facing the group with insufficient ready segments | Move to an adjacent sector, then hold position | The radar marker settles relative to the enemy and stationary time accrues readiness | PDS-003, PDS-004 |
| At least one segment ready | Open Command and select the gun or laser | Battle and gauge stop while the choice is inspected. Commitment spends one completed segment | PDS-004 |
| Formation remains active | Fire homing laser, or aim the gun at one target | The paid laser attacks several targets. The gun damages a selected target | PDS-005 |
| Position remains exposed on enemy resolution | Enemy uses Green Orb | In both traces HP decreases from 400 to 352 | PDS-005 |
| Required hostiles are removed | Let the battle settle | Close Call with the recorded EXP and Dyne amounts | PDS-006 |
| Evaluation has ended | Resume flight past the excavation structures | Field navigation returns with a new independent encounter possible | PDS-007 |

## Strategic and experiential structure

Changing sectors may avoid a dangerous attack or expose a better target,
but repositioning delays the next completed command segment. Holding a safe
sector makes readiness valuable. The paused decision window protects
inspection time without supplying free charge. The gun can concentrate
damage on one target, while the laser can spend one segment on several.

## Replay and variation

The first trace has one visually distinct purple target and three other
Pattergo targets. Regenerate is visible before the finish. The second trace
shows four ordinary-looking units and uses two homing volleys. Both take
48 damage from Green Orb and clear at Close Call. They restore field
control with different EXP and Dyne payouts. These observations do not
identify a formula for either the grade or the reward amounts.

## Adjacent systems and history

The earlier Panzer Dragoon and Panzer Dragoon II Zwei use an advancing
flight corridor and quarter-turn attack views. Here the dragon moves relative
to an established hostile formation instead. The manual describes later
laser capacity and dragon morphology. Those rules are not needed for the
first observed complete encounter.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-161, ACT-860 | Fly directly on the field, aim one shot, or shift the battle quadrant |
| System Behaviour | SYS-822, SYS-1867, SYS-1868, SYS-1869 | Grade the encounter, earn and spend readiness, resolve homing fire and credit payouts |
| Constraint | CON-634 | Gate a command by ready shared segments and context |
| Information | INF-600 | Show the relative danger and the dragon's current sector |
| Objective | OBJ-029 | Clear the bounded hostile formation |
| Time | TIM-003, TIM-046 | Advance live unless the command window stops both sides and the gauge |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `646` (`GAME-0001`–`GAME-0646`).
- Exact genome matches: none.
- Tied near matches: `GAME-0277` — Cuphead (`5 / 21 = 0.238095`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Cuphead (GAME-0277)](../a-f/cuphead.md) | ACT-008, ACT-161, OBJ-029, SYS-822, TIM-003 | Both use aimed fire during a live bounded fight, then grade the clear. Cuphead requires continuous platform positioning and avoidance while attacking. Saga instead orbits a formation, trades repositioning time for stationary accrual and suspends combat for a paid command choice. | Near, `0.238095` |

## Taxonomy impact

Six additions isolate enemy-relative movement, idle-only segment accrual,
automatic nearby multi-target homing, grade-sensitive rewards, danger
radar and the paused combat-order window. ACT-690 rotates the aim view over
an advancing route. ACT-691 and SYS-1411 require held reticle acquisition and
release. Those are different acquisition rules. TIM-026 covers concurrent
actor-local readiness yielding one command when an individual gauge fills.
This packet needs the same acting dragon to bank several costs while
stationary. TIM-027 is scoped to a held squad radial and TIM-030 to reversible
ship order pause. This brief battle-window pause is tied to affordability in
the active combatant's banked command gauge.

## Negative results

- Moving around the enemy does not earn more command segments.
- Waiting inside the Command window does not recharge Synchronicity.
- Laser capacity, exact targeting order and grade thresholds were not measured.
- Close Call was consistent with a completed fight in both traces.
- The observed flight successor does not establish persistence after reload.

## Delta summary

Twelve scoped genes, six additions and six reuses. The record ends with
the first completed Pattergo encounter and the returned field input.

## New facts

- Live repositioning changes safety without building readiness.
- The same command window freezes enemy threats and the readiness clock.
- One paid homing burst can damage several members of the formation.
- The clear grade and the credited reward values remain distinct.

## Principles and design implications

Trade some time to reach a safer position, then reward staying there
with a paid decision. Pause inspection and command choice without
advancing readiness. Separate the reported battle grade from the exact
amounts the encounter awards.

## Puzzle or game generation potential

Build an enemy group surrounded by four adjacent positions. Give each
position a safety state. Refill an action bank only during live waiting
and stop it on the command screen. Contrast one targeted shot with one
nearby multi-target volley, then report grade and rewards separately.

## New genes

- ACT-860
- SYS-1867
- SYS-1868
- SYS-1869
- INF-600
- TIM-046

## New combinations

None. No verified combination is a subset of the scoped genome.

## Taxonomy changes

[TAXONOMY_CHANGE_393](../../../research/taxonomy-changes/TAXONOMY_CHANGE_393.md).

## New questions

How do grade and payout change when only the time to defeat the exact
same formation is varied?

## Next recommended game

Analyse the first completed town errand in the native commercial Nintendo
Switch release of Thank Goodness You're Here!

## Why this game

A short flight encounter exposes the cost of changing position, the
choice of a paid command, repeatable result feedback and field continuation.
