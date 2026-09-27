---
game_id: GAME-0424
slug: star-fox-64
game_title: "Star Fox 64"
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-161
    - ACT-496
    - ACT-562
  system:
    - SYS-215
    - SYS-1119
    - SYS-1120
  constraint:
    - CON-706
  information:
    - INF-416
  objective:
    - OBJ-245
  time:
    - TIM-003
---

# Game: Star Fox 64 — Corneria route decision

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The seven arches, boss identities, route colours and controller buttons are parameters, not additional genes.

## Analysis scope

- Version / ruleset: original North American 1997 Nintendo 64 single-player *Star Fox 64*, first Corneria stage from its ordinary fresh Main Game start. Exact cartridge revision was not inspected.
- Structured analysis target: `PLAT-NINTENDO-64` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: steer Fox's Arwing within the advancing 3D Scroll corridor, aim lasers or a finite Smart Bomb at approaching threats, respond to Falco's distress by removing his pursuers, choose whether to fly through all seven stone arches, then fight the boss reached by that route while preserving Fox's shield. Boost, brake and roll can alter immediate timing and exposure; they do not grant unrestricted open-space flight.
- Entry and exit: start Main Game at Corneria with the initial team available. The bounded packet ends after defeating the encountered Corneria boss and seeing the map successor: ordinary course clear goes to Meteo; keeping Falco available and flying through all seven arches opens the alternate boss and Sector Y. An Arwing crash before the clear consumes a life and may restart at a reached checkpoint, not count as success. This is not a claim to defeat Andross or finish the campaign.
- Included: automatic forward stage progress with player-controlled two-axis placement, cursor aiming and basic/lock-on laser, optional finite bomb and manoeuvres, live incoming damage and shield gauge, Falco rescue and availability, seven-arch traversal gate, alternate-boss selection, stage-clear successor, and the visible teammate/route feedback relevant to those decisions.
- Excluded: later stages, map-level Retry Course or Change Course after this packet, All-Range Mode, Landmaster and Blue-Marine control, medal grind, score-record retention, exact boss attack frame data, laser-upgrade carryover, multiplayer and 3DS remake rules.
- Potential scoped modules: Sector Y's 100-hit branch, later campaign route choices, medal eligibility, original-cartridge frame-accurate combat or replay from a saved checkpoint.
- Direct-play status: no cartridge, emulator, input trace, screenshot, video or audio was examined. Nintendo's original manual, preserved as a third-party transcription, directly states the controls, stage mode, team status, seven-arch condition and map successors. The source is a rules reconstruction, not a measured playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SF64-001` | Main Game starts at Corneria; its normal clear leads to Meteo, while a condition-qualified alternative boss leads to Sector Y. | Confirmed | Direct | High | N1 pp. 11–13 |
| `SF64-002` | 3D Scroll Mode permits movement in the screen's directions but bounds the craft at an edge and advances through a checkpoint. | Confirmed | Direct | High | N1 p. 14 |
| `SF64-003` | Steering, laser/lock-on fire, finite Smart Bomb, boost, brake and double-tap roll are active Arwing controls. | Confirmed | Direct | High | N1 pp. 8–9, 21 |
| `SF64-004` | Teammates under attack can leave if not helped; their damage/down state is inspectable and Falco's survival matters to harder route access. | Confirmed | Direct | High | N1 pp. 18–19 |
| `SF64-005` | Corneria's alternate branch requires keeping Falco alive and flying through seven stone archways. | Confirmed | Direct | High | N1 p. 24 |
| `SF64-006` | Fox's shield depletion crashes the Arwing; a reached scroll-mode checkpoint changes the retry origin. | Confirmed | Direct | High | N1 pp. 14–15 |
| `SF64-007` | The manual does not enumerate every intermediate enemy, boss hit phase, arch collision tolerance or exact cartridge revision. | Observation | Limited | High | N1 |

## Basic data

- Release / origin: Nintendo's original North American *Star Fox 64* Nintendo 64 release, 1997.
- Platform or physical form: Nintendo 64 single-player Main Game; the structured target identifies this version, not every later port or remake.
- Mechanical families: real-time system pressure (`FAM-010`) for advancing live combat and agent routing and coordination (`FAM-015`) for the protected wingmate whose state participates in route access.
- Primary source accessed 2026-09-27: **N1** — [Nintendo, original *Star Fox 64* instruction booklet, transcription](https://world-of-nintendo.com/manuals/nintendo_64/star_fox_64.shtml), especially printed pp. 8–9, 11–15, 18–19, 21 and 24. The third-party HTML preserves manual text; original page images and cartridge were not independently inspected. Its explicit seven-arch condition is used instead of an inferred play-guide route.

## Mechanical decomposition

### Action Genes

- Reused `ACT-161`: aim the Arwing cursor and fire at a currently reachable pursuer, ordinary enemy or boss; holding laser fire can acquire a lock-on, but homing is not universal. `SF64-003`.
- Reused `ACT-496`: request the authored boost or roll manoeuvre during direct craft control; braking is a separate velocity control parameter of the new rail-flight action rather than an unlimited retreat. `SF64-003`.
- New `ACT-562`: continuously steer the Arwing horizontally and vertically inside an automatically advancing 3D Scroll corridor, adjusting local path to threats and arches without choosing an unrestricted world destination. `SF64-002`, `SF64-005`.

### System Behaviour Genes

- Reused `SYS-215`: directly fired lasers/bombs and hostile fire resolve in real time, reducing target and craft shields. `SF64-003`, `SF64-006`.
- New `SYS-1119`: advance the authored Corneria corridor and its encounters while allowing bounded two-axis craft placement, including checkpoint and edge restrictions. This is neither six-degree free flight nor a side-view walker camera. `SF64-002`, `SF64-006`.
- New `SYS-1120`: carry Falco's rescued/available state and all-seven-arch traversal into the alternate Corneria boss and next-map edge; without that joint qualification, ordinary clearance follows the Meteo branch. The map result is not a discretionary selection of any destination. `SF64-001`, `SF64-004`, `SF64-005`.
- Resolution order: live corridor progression and enemy exposure → player movement, fire or manoeuvre → combat/contact and shield changes → Falco help/down outcome → cumulative arch qualification → selected boss → boss clear and route result. `SF64-001`–`SF64-006`.

### Constraint Genes

- New `CON-706`: in the scoped Corneria branch, the harder route is eligible only while Falco remains available and the player crosses every one of the seven authored arches; missing a required condition leaves the ordinary boss and Meteo successor. This is an eligibility gate, not a separate selectable mission-menu option. `SF64-001`, `SF64-005`.

### Information Genes

- New `INF-416`: local aiming cursor, shield/boost gauges, teammate distress and pause-state damage/down indicators expose the current combat and wingmate condition; the result map exposes the reached branch. They do not reveal future unseen enemies or show a complete arch-count forecast. `SF64-003`, `SF64-004`, `SF64-006`.

### Objective and Time Genes

- New `OBJ-245`: defeat the encountered Corneria boss and retain the corresponding Meteo or Sector Y map successor; the alternate route is a qualified outcome, not mandatory for an ordinary stage clear. `SF64-001`, `SF64-005`.
- Reused `TIM-003`: threats, corridor, projectiles, teammate peril and shield damage continue while the player steers or aims. `SF64-002`–`SF64-006`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Main Game enters Corneria | Steer and fire as the view advances | Arwing remains in the 3D Scroll corridor; targets and hazards arrive under live time | player steering within forced route | `SF64-001`–`SF64-003` |
| Fox reaches the stage checkpoint with shield remaining | Pass the checkpoint | Shield partly recovers; later crash restarts at checkpoint rather than the beginning | retry boundary is not stage victory | `SF64-002`, `SF64-006` |
| Falco is pursued | Shoot his attackers before he leaves | Falco remains available for the route qualification | wingmate state matters beyond optional score | `SF64-004`, `SF64-005` |
| Falco remains available; water arches approach | Pilot under each of seven stone arches | Complete traversal set qualifies the alternate boss; merely passing beside one fails that condition | compound physical route gate | `SF64-005` |
| Falco unavailable or at least one arch missed | Clear the ordinary boss | Corneria result goes to Meteo | default branch | `SF64-001`, `SF64-005` |
| Falco available and all seven arches crossed | Clear the alternate boss | Corneria result goes to Sector Y | condition-selected successor | `SF64-001`, `SF64-005` |
| Fox's shield reaches zero before boss clear | Continue the attempt after crash if lives remain | Life is consumed and a reached checkpoint may be the retry origin; no positive route clear yet | survival failure is separate from branch choice | `SF64-006` |

## Strategic and experiential structure

- Local decision: steer for a safe line and a usable firing angle; spend a finite bomb or use boost/brake/roll when an approaching pattern warrants it.
- Medium-term planning: intercept Falco's pursuers before committing to each visible arch, because survival and traversal jointly control the boss/route outcome.
- Long-term structure: the resulting map edge selects Meteo or Sector Y. Later path planning and medal optimisation are outside this bounded first-stage packet.
- Common heuristic: save Falco first, then favour arch alignment over optional kills if pursuing the alternate route.
- Failure attribution: a downed Falco or missed arch explains loss of the Sector Y qualification; zero Fox shield explains a crash. No exact arch hitbox or enemy timing is asserted.
- Player-trust factors: distress cues, teammate status, shield gauge and result map expose current or settled consequences, though the original manual does not establish a live seven-arch progress counter.

## Replay and variation

Corneria's authored corridor and seven arch locations are fixed in this scope. Target order, steering line, shield damage, bomb use, Falco rescue and chosen branch can differ between attempts. The guidebook's medal threshold is not an obligatory win condition here; no procedural corridor generation is claimed.

## Adjacent systems and history

*STAR WARS: Squadrons* shares direct hostile fire and live craft combat, but its Mission 1 supports unrestricted three-dimensional cockpit travel and subsystem power management rather than a forward-imposed corridor. *Geometry Dash* also advances an authored course, but its single vertical input and fixed beat do not offer two-axis craft steering, aim and a wingmate-gated boss branch. The 3DS remake and later Star Fox missions require their own scope.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-161`, `ACT-496`, `ACT-562` | laser/bomb aiming, manoeuvre, bounded two-axis steering |
| System Behaviour | `SYS-215`, `SYS-1119`, `SYS-1120` | live combat, advancing corridor, joint branch selection |
| Constraint | `CON-706` | Falco available and seven arches crossed |
| Information | `INF-416` | combat, wingmate and result feedback |
| Objective | `OBJ-245` | boss clear and next-map successor |
| Time | `TIM-003` | concurrent progress and threats |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `423` (`GAME-0001`–`GAME-0423`).
- Exact genome matches: none.
- Tied near matches: `GAME-0359` — Crimson Skies: High Road to Revenge (`4 / 26 = 0.153846`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Crimson Skies: High Road to Revenge (`GAME-0359`) | `ACT-161`, `ACT-496`, `SYS-215`, `TIM-003`: aimed shots and player-triggered craft manoeuvres resolve during live flight combat | Crimson Skies directly steers an aircraft in a mission with finite missiles and a recaptured objective; Corneria automatically advances a bounded corridor, and protecting Falco plus crossing every arch selects a different boss and next-map route | Near, `0.153846` |

## Taxonomy impact

[`TAXONOMY_CHANGE_162`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_162.md) admits two-axis rail-craft steering, advancing 3D Scroll, compound Falco/arch route selection and eligibility, route-relevant feedback and a boss-to-map terminal. No earlier signature or verified combination changes.

## Negative results

- `ACT-392` and `SYS-723` rejected: Corneria is bounded 3D Scroll, not direct six-degree free-space flight. All-Range Mode is outside this packet.
- `CON-168` rejected: its narrative branch is chosen by entering an open route; this alternate boss requires a living teammate and all seven live traversal checks.
- `INF-062` rejected: the map names route destinations, but this packet does not offer a preflight Slay the Spire-style visible node-choice graph.
- Medal and total-hit genes rejected: optional scoring does not define an ordinary Corneria clear. Boss phases and precise arch collision tolerances remain unmeasured.

## Delta summary

The first-stage flight advances without waiting for Fox. Rescuing Falco and physically crossing seven arches changes the encountered boss and the map successor, whereas ordinary boss clearance proceeds to Meteo.

## New facts

- [Confirmed | Direct | High] Nintendo's original manual explicitly joins Falco's survival and seven stone arches to Corneria's alternate route (`SF64-001`, `SF64-005`).

## New genes

- [Confirmed | Direct | High] `ACT-562`, `SYS-1119`, `SYS-1120`, `CON-706`, `INF-416` and `OBJ-245` distinguish the bounded flight, conditional boss/route and visible feedback.

## New combinations

- [Observation | Direct | High] None created; verified prior combinations are checked against the complete ten-gene signature.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_162` admits six new typed boundaries without revising earlier signatures.

## New questions

- How tolerant are the seven individual arch crossing volumes in the original cartridge, and at which exact update does the alternate boss flag become final?
- Which cartridge revisions alter enemy timing, Falco's damage or checkpoint behaviour?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0425` *Black & White* only after this unit's full validation, one local commit and Goal stop window; retain the recorded selection order.
- Optimisation criterion: contrast live rail combat and compound route qualification with divine commands and creature learning in a bounded task.
- Expected information gain: different timing, information and objective boundaries.
- Backlog impact: no successor is started in this unit.

## Why this game

- [Confirmed | Direct | High] The original manual gives an unusually explicit two-condition route gate and stage-result change, allowing a reproducible first-stage packet without claiming direct play or an entire campaign.
