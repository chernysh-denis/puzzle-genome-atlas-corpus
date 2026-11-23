---
game_id: GAME-0623
slug: blue-lightning
game_title: "Blue Lightning"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-161
    - ACT-496
    - ACT-562
  system:
    - SYS-911
    - SYS-987
    - SYS-1824
  constraint:
    - CON-863
  information:
    - INF-179
    - INF-580
  objective:
    - OBJ-002
    - OBJ-334
  time:
    - TIM-003
---

# Game: Blue Lightning

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The mission name, code and displayed scores are instances of the rules.

## Analysis scope

- Version / ruleset: English 1989 commercial Atari Lynx game card
  PA2020, single-player Dog Fight. Hardware and cartridge revision of
  the captured sessions are unverified.
- Primary decision loop: steer the aircraft across the moving view,
  choose when to fire the cannon or expend guided missiles, and use
  short committed speed or roll actions as threats approach. Complete
  the assigned airborne encounter and let the game land automatically.
- Entry: the Mission 1 briefing for Dog Fight with the initial code
  AAAA. Commit the ordinary runway launch to enter the authored course.
- Exit: the visible completion, automatic landing and Mission 2
  Bombing Run briefing with code PLAN. Subsequent launch corroborates
  access; no Mission 2 combat rules enter the genome.
- Included: bounded arcade flight, primary and guided fire, finite guided
  stock, afterburner and roll, terrain floor and protruding obstacles,
  live indicators and points, documented reserve aircraft on failure,
  mission settlement and successor code disclosure.
- Excluded: later sorties, including manual landings in Courier, later
  ground objectives, night detection, campaign ending, game-card hardware,
  other releases, the Jaguar CD game, predefined frame or distance
  measurements, exact score formulas and unauthenticated code variants.
- Suggested later scope: one Courier airstrip and its actual landing and
  relaunch, with a separate control-boundary review.

## Direct-play status

No direct play. The Epyx title note, physical catalogue and Atari
instruction booklet identify the retail Lynx game. Two attributed
Lynx recordings independently show the opening and the actual
successor. Hardware, byte identity, timing and input logs have not been
authenticated. Only rendered stills and written sources were inspected,
without video or audio playback. The reference sorties do not show a
crash. The replacement and refit rule is documented by Atari.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| BL-001 | The 1989 Lynx commercial card PA2020 is a single-player arcade flight game. The initial AAAA briefing identifies Dog Fight and the task of destroying enemy aircraft. | Confirmed | Corroborated | High | P1, P2, P3, W1 0:30 and W2 1:30. |
| BL-002 | Launch is requested at the runway. Ordinary forward progression is automatic while steering changes horizontal position and altitude, and aircraft advance into the encounter. | Confirmed | Corroborated | High | P1 Getting Started and Playing the Game; W1 0:30–0:50 and 2:00–2:20; W2 1:30–2:10. |
| BL-003 | The cannon is available without spending the separate missile stock. Guided fire expends that stock and can follow an acquired aircraft. A square cue and red lock cue are distinct. The launch load is documented as 40; the screenshot symbols represent stock, not a guaranteed one-icon-per-shot numeric display. | Confirmed | Corroborated | High | P1 Weapons and Flight Computer; W1 0:50, 1:40–2:00 and 2:40–2:50; W2 2:30 and 4:20–4:40. No exact guidance formula is inferred. |
| BL-004 | A ready afterburner runs for ten seconds and then needs ten seconds of recharge. The blue ready signal and yellow active signal differ. A separate instructed roll changes orientation and may defeat a pursuing missile lock, without promising immunity. | Confirmed | Corroborated | High | P1 Afterburners and Barrel Rolls; W1 1:00, 1:40, 2:20 and 2:40; W2 2:50 and 3:30. Durations and command boundaries are manual facts, not frame measurements. |
| BL-005 | Ordinary descent is bounded by the flight computer. Above-ground obstacles are still collision hazards. A crash or shot-down aircraft uses one of a finite group of six prototypes and brings a loaded replacement back to the same mission start while another remains. | Confirmed | Direct | High | P1 Playing the Game, Flight Computer and Missions; P2 independently states the reserve. W1 and W2 show low and high flight but neither provides a failure trace. |
| BL-006 | Points rise during combat. W1 reaches 20,100 and W2 reaches 21,500. Each sees a prepare-to-land cue, mission completion and automatic landing. The point totals are results, not known clear predicates. | Observation | Corroborated | High | W1 2:50–3:20; W2 4:40–5:00; P1 Missions. |
| BL-007 | The next briefing announces Mission 2 Bombing Run, code PLAN. The missile display is stocked again and the running score carries across the boundary. A new session can begin at an already learned mission code. | Confirmed | Corroborated | High | W1 3:30–3:40, W2 5:10–5:20; P1 Getting Started and Missions. No exact rules for score reset on password entry are claimed. |

## Basic data

- Analysis target: `PLAT-ATARI-LYNX`.
- Developer: Epyx. Publisher: Atari.
- Mechanical family: `FAM-010`, intervention during advancing
  encounters and timed recovery.
- Checked: 2026-11-21.
- P1: [Atari's 1989 English instruction booklet, transcribed by AtariAge](https://atariage.com/manual_html_page.php?SoftwareID=2411&SystemID=LYNX&itemTypeID=HTMLMANUAL).
- P2: [Epyx title record](https://epyxgames.com/titles/blue-lightning/).
- P3: [Physical cartridge catalogue](https://www.computinghistory.org.uk/det/70860/Blue-Lightning/)
  and [PA2020 label](https://atariage.com/software_page.php?SoftwareLabelID=2007&SystemID=LYNX).
- W1: [Retro Game Spacko, LongplayArchive](https://www.youtube.com/watch?v=_7EP_vAcukw&t=30s),
  explicitly Atari Lynx. The runway, completion and next briefing
  are visible at 0:30, 3:10 and 3:30.
- W2: [Randomised Gaming, Atari Lynx opening](https://www.youtube.com/watch?v=jJRWZ4XkNmw&t=90s).
  The same first mission is visible at 1:30, terminal at 5:00 and
  successor at 5:10. The displays confirm different final scores.

## Mechanical decomposition

### Action Genes

- ACT-562: position the jet along the two controlled screen axes of
  an advancing flight route.
- ACT-161: direct the cannon or available missile fire at an enemy.
- ACT-496: deliberately commit a ready afterburner burst or an authored
  roll during ordinary flight.

### System Behaviour Genes

- SYS-987: debit a finite shot and guide it toward the currently
  acquired target under the game rule.
- SYS-911: debit a prototype on lethal failure and return to the
  same mission start with a stocked replacement if available.
- SYS-1824: finish the committed afterburner duration, then recover
  readiness only after the separate cooldown.

### Constraint Genes

- CON-863: limit ordinary descent while leaving collisions with
  raised features and objects possible.

### Information Genes

- INF-179: show the current aircraft, approach space and visible threats.
- INF-580: distinguish acquisition and guidance markers, the
  afterburner lamp, missiles, replacement aircraft and points.

### Objective Genes

- OBJ-334: complete Dog Fight to automatic recovery and a named
  successor briefing with its reusable entry code.
- OBJ-002: improve the combat score independently of the evidenced
  mission settlement, with no presumption of a fixed threshold.

### Time Genes

- TIM-003: choose steering, fire and bursts as encounters advance.

## Reproducible transitions

| State | Input or event | Result | Evidence |
| --- | --- | --- | --- |
| AAAA runway briefing | Start the sortie | The jet rolls and becomes controllable in the moving encounter | BL-001, BL-002 |
| Ready boost during normal flight | Request afterburner | A committed fast interval precedes a distinct recharge lockout | BL-004 |
| Eligible enemy in an acquired relation | Fire a guided shot with stock | Resolve one spending and guided-flight attempt | BL-003 |
| Low flight, or lethal collision | Descend farther, or lose the prototype | Ordinary ground descent stops. When destroyed, a surviving reserve grants the current mission restart | BL-005 |
| Assigned encounter reaches success | Prepare to land and allow closeout | Scripted landing supersedes normal flight control | BL-006 |
| Landed after Dog Fight | Accept the new briefing | PLAN is disclosed, missile stock refreshed and the score remains | BL-007 |

## Strategic and experiential structure

The craft keeps moving forward even when no attack is committed.
Horizontal placement and altitude affect shot opportunities and
survival. The boost changes the pace for longer than the input,
so activating it before a difficult approach commits the player
through that interval. The cannon and guided supply provide separate
options; the square does not itself spend a missile.

## Replay and variation

The reference complete attempt and the second trace reach the same
briefing with different scores. The book describes the loss branch
and the explicit later-code path, which preserve different states.
There is no supported claim that each enemy wave must be destroyed,
that simply waiting completes the mission or that a particular point
total is required.

## Adjacent systems and history

The cartridge's later missions use other target and flight rules.
The Courier mission's player-controlled airstrip use is different
from the automatic settlement of Dog Fight. The code can be recorded
outside the game. It is distinct from saved internal mission
progress and no password-entry score carryover is inferred.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-161, ACT-496, ACT-562 | Direct attack, boost or roll, and bounded steering |
| System Behaviour | SYS-911, SYS-987, SYS-1824 | Finite replacement, guided shot and timed boost cycle |
| Constraint | CON-863 | Ground-related lower bound with residual collision |
| Information | INF-179, INF-580 | Current encounter, target cues and distinct counters |
| Objective | OBJ-002, OBJ-334 | Independent score and complete sortie handoff |
| Time | TIM-003 | Live decisions during automatic course advance |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `622` (`GAME-0001`–`GAME-0622`).
- Exact genome matches: none.
- Tied near matches: `GAME-0424` — Star Fox 64 (`4 / 18 = 0.222222`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Star Fox 64 (GAME-0424)](../s-z/star-fox-64.md) | ACT-161, ACT-496, ACT-562, TIM-003 | Both use bounded live steering and deliberate attacks or flight bursts. Corneria in Star Fox 64 couples advancement to its corridor and supports an alternate route through wingmate protection. Dog Fight instead ends in automatic landing and a successor code, with a fixed afterburner cycle and a separate finite missile supply. | Near, `0.222222` |

## Taxonomy impact

[TAXONOMY_CHANGE_369](../../../research/taxonomy-changes/TAXONOMY_CHANGE_369.md)
adds a committed independent boost cycle, the terrain-floor exclusion,
a pursuit display, and the coded automatic landing objective.

## Negative results

- SYS-988 spends a common manoeuvre reserve. The afterburner instead
  has a fixed active interval and independent recharge.
- SYS-1434 requires sustained aim and a measured lock-loss window.
  The booklet and W1 do not establish that condition. SYS-987 covers
  the finite guided shot without importing that additional predicate.
- SYS-369 restores a checkpoint state. The rule here debits one
  prototype from finite stock before a refitted same-mission restart.
- OBJ-288 requires a boss. Dog Fight credits a coded mission landing;
  the captures do not establish a terminal boss or score threshold.

## Delta summary

Admits a complete first commercial Lynx sortie from the runway
assignment to the credited landing and successor access.

## New facts

- A single readiness lamp distinguishes the boost cycle from reserve stock.
- The game can cap descent without eliminating collision with raised objects.
- An actual automatic landing precedes the PLAN briefing in two recordings.

## New genes

SYS-1824, CON-863, INF-580 and OBJ-334.

## New combinations

None. No verified combination is a subset of the bounded mission genome.

## Taxonomy changes

[TAXONOMY_CHANGE_369](../../../research/taxonomy-changes/TAXONOMY_CHANGE_369.md).

## New questions

A separate Courier packet can test which side of an airstrip landing is
player controlled and when the next takeoff becomes available.

## Next recommended game

Continue with Paradise Killer on PlayStation 5 and follow an early
inquiry through acquisition and its visible case entry.

## Why this game

A real-time flight corridor with a committed burst, finite airframes
and explicit code-bearing settlement differs from free-space flight
and from a terminal boss or time-only score chase.
