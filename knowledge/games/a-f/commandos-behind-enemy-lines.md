---
game_id: GAME-0429
slug: commandos-behind-enemy-lines
game_title: Commandos: Behind Enemy Lines
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-048
    - ACT-161
    - ACT-189
    - ACT-202
    - ACT-341
    - ACT-380
    - ACT-491
  system:
    - SYS-057
    - SYS-215
    - SYS-755
  constraint:
    - CON-076
    - CON-077
    - CON-330
  information:
    - INF-420
  objective:
    - OBJ-185
  time:
    - TIM-003
---

# Game: Commandos: Behind Enemy Lines — cross the river and sabotage the relay

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Patrol locations, exact travel times, barrel blast radius and ammunition are parameters or unmeasured facts, not additional genes.

## Analysis scope

- Version / ruleset: original 1998 English Windows PC *Commandos: Behind Enemy Lines*. The bounded first mission is `Baptism of Fire`, after optional tutorials. The original Pyro/Eidos manual establishes core control, sight, specialist and objective rules; two written first-mission routes corroborate the boat, island and radio-relay sequence. Exact disc revision and direct play were not inspected.
- Structured analysis target: `PLAT-WINDOWS-PC` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: select the Green Beret, Marine or Driver; inspect one guard's displayed view; issue contextual movement while the patrol moves; change posture to limit detection; have the Marine acquire and deploy the inflatable boat, ferry all three across, move an explosive barrel into useful position with the Green Beret, and shoot it to destroy the radio relay while all three survive.
- Entry and exit: begin with those three specialists separated on the starting bank in the first mission, before acquiring the boat. End after all three have crossed to the north-west island and the designated relay has been destroyed, with all mission-critical commandos alive. This is a source-bounded mission objective, not a claim of a witnessed successful run or measured route.
- Included: selected-unit contextual orders; standing/crouched/crawling movement and near-versus-far sight; one inspected guard's cone versus all active guards' unseen cones; specialist-specific boat and barrel handling; boat boarding and landing; optional knife/body concealment as part of one documented route; live guard response and combat; destructible fuel barrel and linked relay; all-commandos-survive condition.
- Excluded: later missions, other three specialist classes, global alert or reinforcement behaviour not established for this first mission, multiplayer, score/merit optimisation, exact enemy counts and routes, patch-specific timings, unobserved mission geometry and a claim that the documented route is the only solution.
- Potential scoped modules: other specialists' equipment, alarm escalation in later missions, diverging routes and merit evaluation.
- Direct-play status: no original disc, executable, direct inputs, screenshot, video or audio was inspected. The original manual is the primary rules evidence; independent route authors supply the first-mission sequence. Exact ranges, blast radius and the installed version remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CBE-001` | Selected specialists take point-and-click movement and tool orders; each has distinct permitted actions. | Confirmed | Direct | High | P1 |
| `CBE-002` | One selected enemy's cone is displayed, while other enemies still see; its farther dark region can miss a crawling commando, the bright near region does not, and terrain blocks sight. | Confirmed | Direct | High | P1 |
| `CBE-003` | The Marine can acquire and deploy the inflatable boat; the Green Beret can carry barrels and bodies; the Driver can operate vehicles and heavy weapons. | Confirmed | Direct | High | P1 |
| `CBE-004` | All required commandos must survive, and a mission's main objective must be met to advance. | Confirmed | Direct | High | P1 |
| `CBE-005` | In `Baptism of Fire`, Green Beret, Marine and Driver use a boat to reach the north-west island and destroy a radio relay with an explosive barrel. | Observation | Corroborated | Medium | S1, S2 |
| `CBE-006` | Guards react to eligible sight, sound or a discovered body, while a shot fuel barrel explodes. | Confirmed | Direct | High | P1 |
| `CBE-007` | One documented route knives a machine gunner, moves his body, positions a barrel and shoots it; this is a route example, not a compulsory kill sequence. | Observation | Corroborated | Medium | S1, S2 |

## Basic data

- Release / origin: 1998 Pyro Studios / Eidos original, Windows PC.
- Platform or physical form: mouse-directed real-time tactical mission with a separated specialist team.
- Mechanical families: agent routing and coordination (`FAM-015`), tactical forecast and counterplay (`FAM-009`) and real-time system pressure (`FAM-010`).
- Sources accessed 2026-09-27: **P1** — [original Pyro/Eidos manual distributed through Steam](https://cdn.akamai.steamstatic.com/steam/apps/6800/manuals/commandos_manual.pdf), pp. 3–10 on orders, specialists, enemy sight, mission survival and objectives; **S1** — [independent first-mission guide](https://gamefaqs.gamespot.com/pc/63451-commandos-behind-enemy-lines/faqs/81342), `Baptism of Fire` route; **S2** — [independent first-mission route](https://www.metamud.org/~eggie/commandos/mis1/), boat and relay-barrel corroboration. The secondary routes do not prove an exact original-disc patch or exclusive solution.

## Mechanical decomposition

### Action Genes

- Reused `ACT-189`: order the selected specialist to a destination or target; do not model this as direct per-step steering. `CBE-001`.
- Reused `ACT-202`: crouch or crawl to change movement and sight exposure. `CBE-002`.
- Reused `ACT-341`: acquire and deploy the mission's eligible inflatable boat as a stateful world interaction. This is not a free-form crafting system. `CBE-003`, `CBE-005`.
- Reused `ACT-380`: board and disembark the available boat with eligible selected specialists. Movement of the occupied boat is ordered through `ACT-189`. `CBE-005`.
- Reused `ACT-048`: lift, carry and put down the portable fuel barrel. `CBE-003`, `CBE-005`.
- Reused `ACT-161`: use the selected specialist's available knife or gun against an eligible target, including shooting the positioned barrel. `CBE-006`, `CBE-007`.
- Reused `ACT-491`: a documented route carries and places the fallen gunner's body to manage discovery. This is not required by the mission objective. `CBE-007`.

### System Behaviour Genes

- Reused `SYS-057`: a guard diverts from patrol on eligible perception; the exact alert duration is unmeasured. `CBE-006`.
- Reused `SYS-215`: commanded hostile contact resolves while patrols and other commandos continue moving. `CBE-001`, `CBE-006`.
- Reused `SYS-755`: a shot destroys the eligible fuel barrel and its declared blast can resolve the relay target. The exact blast radius is not claimed. `CBE-005`, `CBE-006`.
- Resolution order: inspect selected guard → time posture and orders around all active observers → acquire/deploy and board boat → land all three → position barrel and optionally conceal hostile body → strike barrel → check relay and team survival.

### Constraint Genes

- Reused `CON-076`: only the specialist with the relevant tool or permission performs each boat, barrel or vehicle action; teammates are not interchangeable. `CBE-001`, `CBE-003`.
- Reused `CON-077`: guard perception depends on current facing and occlusion; far/near sight and crawling are parameters of the permitted region. `CBE-002`.
- Reused `CON-330`: losing any required commando invalidates the mission even if the relay is destroyed. `CBE-004`.

### Information Genes

- New `INF-420`: inspecting one guard exposes that guard's current moving, near/far sight cone, not every simultaneous observer or a future patrol script. `CBE-002`.

### Objective and Time Genes

- Reused `OBJ-185`: destroy one designated hostile structure and retain the successor while all declared mission-critical actors survive. The radio relay is the structure. `CBE-004`, `CBE-005`.
- Reused `TIM-003`: patrols, sight, movement and combat advance in real time as the player issues commands. `CBE-001`, `CBE-006`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A guard patrols with no cone currently displayed | Inspect that guard | Its near and far sight regions are shown; other guards remain active | a selected-cone information limit | `CBE-002` |
| A commando is in the far dark region without cover | Crawl behind an opaque obstacle | Crawling can avoid far detection; near sight still threatens him | posture and occlusion are separate sight conditions | `CBE-002` |
| Marine reaches the mission boat | Acquire/deploy it, then board eligible teammates | An occupied transport can cross and unload on reachable shore | specialist gating and transport are not ordinary walking | `CBE-003`, `CBE-005` |
| Team has landed and a barrel is movable | Green Beret carries and places the barrel by the relay | The target and an explosive prop are now in a linked blast arrangement | placement precedes damage resolution | `CBE-003`, `CBE-005` |
| Positioned barrel can be shot | Order an eligible gunshot into it | Explosion can destroy the relay; team survival is checked separately | objective destruction and survivor gate both matter | `CBE-004`–`CBE-006` |

## Strategic and experiential structure

- Local decision: choose which specialist to command and when one guard's displayed cone leaves a safe route.
- Medium-term planning: route the non-swimming teammates across by boat while preserving the Marine's ability to deploy and recover it.
- Long-term structure: reach the single sabotage target with a movable explosive prop and keep all three essential specialists viable.
- Common heuristic: check the selected guard's cone but assume unselected patrols still perceive; a dark far zone is not equivalent to cover in the bright near zone.
- Failure attribution: a discovered body or noisy engagement can redirect a guard; a lost specialist ends the mission even after structure damage.
- Player-trust factor: the manual explicitly distinguishes displayed one-guard sight information from the still-operative sight of others, preventing a false omniscient interpretation.

## Replay and variation

The secondary guides show a viable boat-and-barrel plan with different local combat choices. They do not prove it is the only route or provide measured timing, ammunition and blast geometry.

## Adjacent systems and history

Other real-time tactics and RTS games reuse directed orders and patrol response; this original mission makes three specialists non-interchangeable and couples a boat crossing to a movable explosive and an all-survive gate. The later *Commandos* missions can add alert rules outside this packet.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-048`, `ACT-161`, `ACT-189`, `ACT-202`, `ACT-341`, `ACT-380`, `ACT-491` | barrel, selected specialist, posture, boat, optional body |
| System Behaviour | `SYS-057`, `SYS-215`, `SYS-755` | patrol response, live combat, barrel blast |
| Constraint | `CON-076`, `CON-077`, `CON-330` | specialist permissions, sight, team survival |
| Information | `INF-420` | one selected guard's near/far sight cone |
| Objective | `OBJ-185` | relay destroyed and team intact |
| Time | `TIM-003` | live patrol and action resolution |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `428` (`GAME-0001`–`GAME-0428`).
- Exact genome matches: none.
- Tied near matches: `GAME-0339` — Metal Gear Solid (`8 / 25 = 0.320000`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0339` *Metal Gear Solid* | `ACT-161` aimed strike, `ACT-202` posture, `ACT-341` world interaction, `SYS-057` perception-driven pursuit, `SYS-215` live hostile combat, `CON-077` directed sight, `CON-330` critical-actor survival and `TIM-003` real time | *Metal Gear Solid* moves one directly steered infiltrator through a fixed dock/heliport route with Soliton Radar and an escape objective. *Commandos* delegates contextual orders among three non-interchangeable specialists, crosses by boat, moves a barrel and destroys one relay while showing only one selected guard's cone. | Tied-near maximum, `0.320000`; not exact or a verified combination match. |

## Taxonomy impact

[`TAXONOMY_CHANGE_167`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_167.md) admits the selected-guard cone information boundary. No earlier signature or verified combination changes.

## Negative results

- `ACT-008` rejected: commands target destinations; the player does not steer each walking step.
- `INF-287` rejected: no retained per-actor marker or accumulating directional detection meter is established for this mission.
- `SYS-434` rejected: neither the first-mission guide nor manual establishes reinforcements in this bounded route.
- No claim of a successful directly observed run, exact barrel blast radius, compulsory gunner kill or unique solution.

## Delta summary

Specialist-gated transport and prop positioning produce a sabotage route, while a displayed sight cone reveals only one guard in an otherwise live, multi-observer mission.

## New facts

- [Confirmed | Direct | High] The manual separates selected-guard sight display from all active observers, near and far visibility, specialist equipment and survival rules (`CBE-001`–`CBE-004`, `CBE-006`).
- [Observation | Corroborated | Medium] Two independent guides align on the first mission's boat crossing and relay-barrel objective, not an exclusive route (`CBE-005`, `CBE-007`).

## New genes

- [Confirmed | Direct | High] `INF-420` describes the one-selected-guard information boundary; the other fifteen genes are reused.

## New combinations

- [Observation | Direct | High] None created; verified combinations are tested against the complete signature.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_167` admits one information boundary without revising earlier games.

## New questions

- On an original pinned executable, what are the measurable near/far cone distances, exact barrel blast radius and response delay to a discovered body?
- Which alternate first-mission route avoids moving the machine gunner's body while preserving all three specialists?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0430` *Silent Hill* only after this unit's validation, local commit and Goal stop window.
- Optimisation criterion: contrast squad infiltration against solo clue and threat navigation.
- Backlog impact: no successor is started in this unit.

## Why this game

- [Hypothesis | Limited | Medium] First-mission stealth offers specialist-dependent orders and bounded perception, mechanically distinct from the prior course editor.
