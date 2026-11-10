---
game_id: GAME-0464
slug: jet-set-radio-future
game_title: "Jet Set Radio Future"
analysis_status: reviewed
reviewed: 2026-10-01
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
  system:
    - SYS-036
    - SYS-222
    - SYS-578
    - SYS-974
    - SYS-975
    - SYS-976
    - SYS-1214
    - SYS-1215
  constraint:
    - CON-659
  information:
    - INF-443
  objective:
    - OBJ-263
  time:
    - TIM-003
---

# Game: Jet Set Radio Future

Use the canonical [vocabulary and comparison rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). YoYo, Beat, Dogenzaka Hill, spray colours and the district route are parameters, not gene names. The original Jet Set Radio is a different game, not a source of inherited Future rules.

## Analysis scope

- Version / ruleset: original North American English Jet Set Radio Future retail disc for the original Xbox, published by SEGA in 2002. The original instruction booklet establishes controller, graffiti, skating, stock, stamina and map rules; a contemporary Xbox route establishes the named first-district sequence. The disc revision and console executable were not obtained or hashed.
- Structured analysis target: `PLAT-XBOX` in [platform coverage](../../platforms/games.json), not the Dreamcast Jet Set Radio, the 2012 Xbox 360 remaster of that predecessor, a later compatibility wrapper or an emulated modification.
- Entry: YoYo has passed Gum's Garage admission test and first enters Dogenzaka Hill under ordinary story control with its graffiti quota unfinished. The Garage test is fixed entry context, not a newly analysed tutorial.
- Primary decision loop: skate through accessible street and rail geometry, use the map and graffiti marks to choose the next reachable target, collect finite spray, cover each required mark, then locate and repeatedly catch up to Beat as he moves between meeting points before winning his district challenge.
- Positive terminal: the ordinary Dogenzaka Hill graffiti quota is complete, Beat's successive encounters have led to his race challenge, and the player wins that challenge so Beat joins the GGs. Stop before the subsequently announced Rokkaku Police encounter.
- Negative terminal: if stamina is depleted or the mandatory rival challenge is lost, the attempt enters Game Over rather than awarding Beat. The sources do not establish a general countdown for this story street packet or an exact recovery checkpoint; neither is invented.
- Included: direct skating, jumping, automatic compatible rail/wall travel, connected trick scoring, contact spray-can pickups, finite spray, individually marked graffiti points, direct right-trigger marking without a directional trace, required quota, stamina and damage, current HUD and pause-map location cues, Beat's authored relocation after contact, one rival race and its win/loss settlement.
- Excluded: the played Garage tutorial, the later police battle, Shibuya Terminal and further districts, optional Graffiti Souls and Mystery Tape, secret challenges, score optimisation, graffiti editor, VS-mode races and Tagger's Tag, custom art, later unlocks, exact district mark count, race lap/checkpoint geometry, frame timings, live play claims, other releases and the original Jet Set Radio's timed directional-tag stage. These are not assertions that the product lacks those systems.
- Reproducible parameterisation: start after Gum's test, follow the pause map's orange graffiti locations, collect yellow/blue spray cans as needed, approach and mark the required Dogenzaka points, find Beat on the map, approach and talk to him until his race offer appears, then win the offered challenge. The sources do not pin an exact route, quota count or race timing; this is a documentary transition reconstruction rather than a deterministic input transcript.
- Potential scoped modules: the Garage admission test, the following police knockdown-and-tag battle, a later district, VS-mode race rules, direct executable capture, precise race course validation and score arithmetic each need their own evidence packet.
- Direct-play status: not conducted. No original Xbox disc, executable, console, save, controller trace, gameplay screenshot, video or audio was inspected. The original manual and contemporary written route support only the stated rule relations.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `JSRF-001` | The scoped product is original-Xbox Jet Set Radio Future, not its Dreamcast predecessor or Xbox 360 HD port | Confirmed | Direct | High | P1, P2 |
| `JSRF-002` | Compatible rail contact carries a grind; jump and connected trick inputs can build a breakable score chain | Confirmed | Direct | High | P1 |
| `JSRF-003` | Yellow and blue spray pickups supply one and five units; a marked graffiti point spends one unit per circular mark by right trigger, without the earlier game's directional trace | Confirmed | Direct | High | P1 |
| `JSRF-004` | HUD exposes stamina, spray and current graffiti/quota, while the paused map distinguishes remaining graffiti points and actor positions | Confirmed | Direct | High | P1 |
| `JSRF-005` | Stamina depletion ends the attempt; the manual does not assign a general countdown to this story street packet | Confirmed | Direct | High | P1 |
| `JSRF-006` | After the first Dogenzaka graffiti clear, Beat appears, moves away after repeated contacts and offers a race; winning recruits him, losing the mandatory challenge is Game Over | Observation | Corroborated | High | P1, S1, S2 |
| `JSRF-007` | The police battle follows Beat's recruitment and is outside the positive terminal of this packet | Observation | Corroborated | High | S1, S2 |
| `JSRF-008` | The fourteen-gene signature models the bounded street-to-rival sequence without importing a directional command, countdown, police wave or unverified race checkpoint layout | Observation | Direct | High | P1, S1, V1 |

## Basic data

- Release / origin: SEGA/Smilebit, original Xbox retail game, 2002. The original booklet explicitly limits its instructions to Xbox; Xbox Wire independently lists the title among original-Xbox backward-compatibility entries, which is identification context, not proof of later rendering parity.
- Puzzle family: traversal geometry, real-time system pressure and ordered dependency sequencing.
- **[P1]** [original North American Xbox instruction manual](https://manuals.plus/m/1c07ef7ed2a0e9f88a3c92f577c36649612bf68466e795eafd7f891129c772a6.pdf), printed pp. 8–9, 13–14 and 22–24 for skating, graffiti, HUD, map, spray stock, stamina and battles; accessed 2026-10-01. Text was inspected; the remote PDF renderer timed out on image retrieval, so no visual-page or layout claim is made.
- **[P2]** [Xbox Wire's original-Xbox compatibility list](https://news.xbox.com/en-us/2007/07/12/july-2007-back-compat-update/), which names Jet Set Radio Future separately from Jet Set Radio; accessed 2026-10-01.
- **[S1]** [JPereira's 2002 original-Xbox walkthrough](https://gamefaqs.gamespot.com/xbox/475263-jsrf-jet-set-radio-future/faqs/17063), Chapter 1/Dogenzaka Hill, for the order from graffiti quota through Beat's chase, race and later police battle; accessed 2026-10-01. It is a contemporary player account, not a publisher rule sheet.
- **[S2]** [SuperHappy's 2002 spoiler-free Xbox walkthrough](https://gamefaqs.gamespot.com/xbox/475263-jsrf-jet-set-radio-future/faqs/16336), first Dogenzaka route, as independent written-route corroboration; accessed 2026-10-01.
- **[V1]** Source-model transition table below; no executable or first-hand gameplay is claimed.

## Mechanical decomposition

### Action Genes

- `ACT-008` moves, jumps and steers YoYo across street and compatible rail approach geometry.
- `ACT-341` commits the currently legal right-trigger interaction with one marked world point or reachable Beat encounter. It is not `ACT-492`: Future's ordinary mark is a direct spray request, not a directional graffiti trace.

### System Behaviour Genes

- `SYS-036` resolves live motion, gravity and collision; `SYS-974` separately carries the body along compatible grind/wall contact until release. `SYS-975` holds a temporary connected trick-score chain; no exact multiplier is claimed.
- `SYS-222` adds one or five spray units from a touched yellow or blue can. `SYS-976` debits one per eligible graffiti circle and records the addressed mark's completion. It does not create a free-form wall editor or reuse the original game's command trace.
- `SYS-578` applies damage to the current stamina pool and terminates the attempt at zero.
- `SYS-1214` advances the authored local rival: clearing the required district marks reveals Beat; successive reachable contacts make him depart for the next disclosed position; the final contact opens his mandatory race. It does not claim arbitrary NPC pathfinding or a police escalation wave.
- New `SYS-1215` moves the single authored rival toward the disclosed race finish and compares his arrival against the player. The guide names City Rush but does not establish its exact checkpoints or lap policy; vehicle-field `SYS-515`, ordered-checkpoint `SYS-516` and open-road `SYS-1020` are not imported.

### Constraint Genes

- `CON-659` gates each graffiti attempt on an unfinished marked point in range and sufficient spray for its remaining circles. An empty can stock cannot mark a point. `CON-068` is rejected: the manual gives a countdown for VS Graffiti Wars, not this story route.

### Information Genes

- New `INF-443` exposes the current graffiti quota, spray and stamina during the street phase, while the pause map reveals remaining marked positions and Beat's currently disclosed position after he appears. It does not reveal a future race path or hidden next actor location.

### Objective Genes

- New `OBJ-263` closes the bounded district in order: cover its required marks, catch up to Beat until his challenge is available, win that challenge and retain Beat as an ally. Tagging the last wall alone does not settle the district, and the later police fight is outside this terminal.

### Time Genes

- `TIM-003` keeps movement, opponent behaviour and stamina threats live while the player acts. The paused map and settled race result are not decision ticks.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A compatible rail is in the current route | Jump onto it | Contact attaches the skater and carries a grind until release or edge | Surface-bound traversal differs from free steering | `JSRF-002` |
| One yellow or blue spray can is reachable | Cross the pickup | Spray stock rises by one or five, up to current capacity | Spatial stock acquisition precedes tagging | `JSRF-003` |
| An unfinished mark is in range with no spray | Pull right trigger | The mark remains incomplete and quota does not advance | Consumable legality | `JSRF-003` |
| An unfinished single circle is in range with spray | Pull right trigger | One spray unit is spent; that circle settles without a directional-input trace | Future differs from the predecessor | `JSRF-003` |
| More than one circle remains at the point | Hold right trigger while eligible | Each completed circle spends its own unit and advances the point toward completion | The cost follows marks, not arbitrary wall size | `JSRF-003` |
| A required mark remains elsewhere | Pause and inspect the map | Current mark positions are exposed without a future route solution | In-game locational information | `JSRF-004` |
| All required Dogenzaka marks settle | Continue story control | Beat becomes the next disclosed encounter rather than the final district result | Tag quota opens a rival phase | `JSRF-006` |
| Beat is at a disclosed reachable position | Skate to him and talk | He departs for another authored encounter; repeated contact eventually offers a race | Encounter pursuit is staged, not a police wanted meter | `JSRF-006` |
| Beat's race is offered | Finish behind Beat | The mandatory challenge fails and does not recruit him | Win/loss is consequential | `JSRF-006` |
| Beat's race is offered | Beat him to its finish | The race settles as won and Beat joins; stop before the police fight | Positive terminal | `JSRF-006`, `JSRF-007` |
| Stamina reaches zero before completion | Take terminal damage | Game Over replaces local progress | Survival failure, not an invented timer | `JSRF-005` |

## Strategic and experiential structure

- Local decision: choose a reachable point while carrying enough spray, then preserve travel speed through rails and jumps.
- Medium-term planning: use the map to avoid missing required marks; save stock when several circles share a point; distinguish Beat's current location from a future one not yet disclosed.
- Long-term structure: a completed territorial quota converts a street-navigation task into repeated rival pursuit and a mandatory win, without collapsing these into one surface interaction.
- Common heuristics: collect spray along the route, use rails for access and momentum, check the pause map before revisiting cleared surfaces, then approach Beat at each new location.
- Failure attribution: visible stock explains a rejected tag; quota explains a remaining wall; stamina explains survival failure; race outcome explains recruitment or Game Over.
- Player trust: one can must debit once per completed circle, quota must not advance for a rejected point, and Beat must not be recruited from wall clearance alone.

## Replay and variation

- Route order, can pickups, trick chain and mistakes can vary. The authored district geometry and required mark set are not asserted to regenerate.
- Beat's scripted encounters are staged; no random relocation or procedural course is claimed.
- The packet does not infer optional scoring rewards or exact fastest routes from the written walkthrough.

## Adjacent systems and history

- Earlier `GAME-0350` Jet Set Radio shares rail contact, spray pickup, mark legality and surface replacement, but its bounded Shibuya GG route has a countdown, directional graffiti trace and progress-triggered police waves while Future's Dogenzaka story sequence has direct marking and an after-quota rival chase/race.
- Earlier race genes bind vehicle fields, validated checkpoint courses or verified checkpoint-free roads. This packet establishes only a single authored skating rival, an offered race and consequential win/loss; exact Dogenzaka course validation remains unmeasured.
- Graffiti style, Tokyo setting, game music and character appearance are not mechanical genes.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-341` | YoYo, right trigger and Beat are parameters |
| System Behaviour | `SYS-036`, `SYS-222`, `SYS-578`, `SYS-974`, `SYS-975`, `SYS-976`, `SYS-1214`, `SYS-1215` | rail, stock, quota and meeting points are parameters |
| Constraint | `CON-659` | remaining circles and available paint are parameters |
| Information | `INF-443` | map colours and HUD placement are presentation |
| Objective | `OBJ-263` | district, rival and membership are parameters |
| Time | `TIM-003` | exact update cadence is unmeasured |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `463` (`GAME-0001`–`GAME-0463`).
- Exact genome matches: none.
- Tied near matches: `GAME-0350` — Jet Set Radio (`9 / 23 = 0.391304`).
- Supported combination subsets: none.
- Scan date: 2026-10-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0350` — Jet Set Radio | `ACT-008`, `SYS-036`, `SYS-222`, `SYS-578`, `SYS-974`, `SYS-975`, `SYS-976`, `CON-659`, `TIM-003` | Both packets make rail-bound skating, finite spray, marked-surface replacement and live stamina matter. The predecessor's Shibuya GG stage adds a deadline, directional graffiti input, live police escalation and tag-only stage result. Future's bounded Dogenzaka sequence uses direct mark-by-mark spray, reveals a relocatable rival only after graffiti completion and requires a won skating challenge before recruitment; neither shared art direction nor nine overlapping mechanics makes the two terminals interchangeable. | Tied near, `9 / 23 = 0.391304` |

### Preserved research notes

- New genes: `SYS-1214`, `SYS-1215`, `INF-443`, `OBJ-263`.
- Reused genes: `ACT-008`, `ACT-341`, `SYS-036`, `SYS-222`, `SYS-578`, `SYS-974`, `SYS-975`, `SYS-976`, `CON-659`, `TIM-003`.
- Classification result: `New genes`.
- Evidence and reasoning: earlier skate, pickup, damage, contact-bound traversal, trick-chain, marked surface and stock boundaries transfer. No lower-ID gene joins an after-quota moving rival's repeated encounter gate, this source-limited one-rival skating race, the Future-specific street map/HUD without a stage timer or an authored tag-to-rival-recruitment terminal.

## Taxonomy impact

- Registry changes: add four Active boundaries without modifying earlier signatures or the original Jet Set Radio rules. Existing `SYS-976` expressly permits no directional trace; `ACT-492`, `INF-367`, `OBJ-204`, `CON-068` and `SYS-977` are rejected for this scope.
- Taxonomy-change record: [`TAXONOMY_CHANGE_201`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_201.md).

## Negative results

- No original Xbox disc, executable, save, direct play, video or audio trace; no measured physics, exact graffiti quota, race course, score, frame timing or police battle.
- The remote manual's text was accessible, but its PDF image renderer timed out. Page-layout details are not used as evidence.
- Original Jet Set Radio's timed directional traces and early police pressure are not transferred to Future merely because its theme, publisher and some locomotion rules resemble it.
- Later original-Xbox compatibility entries do not prove byte-for-byte rendering or timing parity with the disc target.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original Xbox manual defines direct mark-by-mark spray, pickup stock, stamina and skating controls (`JSRF-001`–`JSRF-005`).
- [Observation | Corroborated | High] A contemporary Dogenzaka route moves from graffiti clear through Beat's repeated encounters to a mandatory winning race (`JSRF-006`, `JSRF-007`).

## New genes

- [Observation | Corroborated | High] `SYS-1214`, `SYS-1215`, `INF-443` and `OBJ-263` isolate the after-quota pursuit and result without importing the predecessor's timer or graffiti trace.

## New combinations

- [Observation | Direct | High] None; verified-subset scan is recorded in Corpus comparison.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_201` records four new boundaries and the exact lower-ID transfer test.

## New questions

- Can direct original-Xbox capture fix the Dogenzaka race checkpoints, timing and precise quota count without importing VS-mode rules?

## Next recommended game

- [Hypothesis | Corroborated | High] `GAME-0465` — Boom Blox for original Wii.
- Optimisation criterion: test motion-controlled throw trajectories and destructible tower scoring against currently isolated physics and spatial-action boundaries.
- Expected information gain: contrast a bounded Wii puzzle stage with live skating, stock-gated painting and a moving rival.
- Backlog impact: fifth of nine selected games completed; four units remain.

## Why this game

- [Hypothesis | Corroborated | High] Boom Blox replaces a continuously navigated street with a compact motion-input physical-object puzzle whose result should be bounded to one named stage.
