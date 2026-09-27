---
game_id: GAME-0416
slug: advance-wars
game_title: Advance Wars
analysis_status: reviewed
reviewed: 2026-09-26
combination_ids: []
gene_ids:
  action:
    - ACT-014
    - ACT-019
    - ACT-554
  system:
    - SYS-537
    - SYS-1105
  constraint:
    - CON-001
    - CON-011
    - CON-034
    - CON-702
  information:
    - INF-409
  objective:
    - OBJ-029
  time:
    - TIM-018
---

# Game: Advance Wars — Terrain Intel

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Infantry count, terrain ratings and map geometry are parameters, not separate genes.

## Analysis scope

- Version / ruleset: original North American English *Advance Wars* Game Boy Advance cartridge (2001), Field Training mission 2, `Terrain Intel`, against computer-controlled Olaf. Nintendo's European English booklet is a rules witness rather than proof of North American binary identity; the exact cartridge revision was not inspected.
- Structured analysis target: `PLAT-GAME-BOY-ADVANCE` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: inspect the four Orange Star infantry, enemy infantry and mechanised infantry, available paths and defensive terrain; choose one available unit, pay its movement cost to reach an eligible cell, attack an adjacent target or wait, then end the Orange Star day and respond to the Blue Moon army's moves on the next day. Use mountain cover despite its slower infantry traversal to survive counterfire and eliminate the finite hostile force.
- Entry and exit: begin at the playable start of `Terrain Intel` with Nell's tutorial directions; succeed when every enemy unit in this mission is defeated. If all Orange Star units are lost first, the route fails. The game may show a mission evaluation after success, but no particular rank is required.
- Included: fixed square-grid map; one occupying unit per cell; infantry movement, Fire and Wait; each unit's spent-order state; mountain and plain movement costs and defensive cover; unit HP, HP-conditioned attack strength, surviving-target counterfire and removal at zero; commander-controlled Orange Star orders, AI Blue Moon orders, explicit End command, changing days; terrain/unit intel and movement highlighting; Nell's compulsory opening tutorial orders before freer play.
- Excluded: preceding `Troop Orders`; following `Base Capture` and its property income and capture rules; HQ capture, production, supply, CO Powers, fog of war, naval or air units, multiplayer, War Room, the campaign, later missions, optional mid-battle save/reload, exact hidden damage calculation and uncertain enemy opening count. The booklet explains some of those general rules, but this packet does not make them active mechanics of `Terrain Intel`.
- Potential scoped modules: the third Field Training mission's city/HQ capture and repair loop; a campaign map with factories, CO Powers or fog.
- Direct-play status: no cartridge, emulator, input trace, gameplay video or audio was inspected. Nintendo's original booklet was downloaded and its relevant English spreads visually read; a transcription of the original mission dialogue and two contemporaneous player accounts bound the scenario. Exact AI branch choices and numeric damage rolls are not established by this packet.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `AW-001` | `Terrain Intel` is Field Training mission 2, starts with four allied infantry and requires eliminating the hostile units; it is not the later base-capture lesson. | Confirmed | Corroborated | High | D1; G1; G2 |
| `AW-002` | A selected infantry moves to an eligible highlighted cell, then may Fire at an adjacent enemy or Wait; committed units become unavailable until the next friendly day. | Confirmed | Direct | High | M1 pp. 4–7; D1 |
| `AW-003` | Mountain traversal costs ordinary infantry more than plain movement, while mountain defence reduces incoming damage; in the mission dialogue mountain cover is rated four versus plain one. | Confirmed | Direct | High | M1 pp. 26, 30; D1 |
| `AW-004` | Attack damage reduces displayed HP; a surviving direct target can answer with damage, and a unit at zero HP leaves the field. | Confirmed | Direct | High | M1 pp. 7–8; D1 |
| `AW-005` | End transfers the army's active day to Blue Moon, whose computer-controlled units move and attack before the next Orange Star day. | Confirmed | Direct | High | M1 pp. 6, 12; D1; G1 |
| `AW-006` | R-button terrain/unit intel exposes present terrain and defensive information, while highlighted movement range reveals reachable cells under the cost rules; neither shows Olaf's precise next orders. | Confirmed | Direct | High | M1 pp. 4–7, 26, 30; D1 |
| `AW-007` | The exact original cartridge revision, enemy opening roster and hidden damage/AI details are not determined by the inspected materials. | Observation | Limited | High | M1; D1; G1; G2 |

## Basic data

- Release / origin: Nintendo's original Game Boy Advance *Advance Wars*; the European manual is publisher-authored but does not prove the North American binary matches its every option. The `Terrain Intel` identity and mission dialogue are cross-checked against original-game player transcription and 2001 reporting.
- Platform or physical form: original Game Boy Advance cartridge, one player versus the game's Blue Moon side.
- Mechanical families: tactical forecast and counterplay (`FAM-009`) and agent routing and coordination (`FAM-015`). The player positions several units against later opposing orders on shared terrain; the enemy action is not an exact preview.
- Sources accessed 2026-09-26:
  - **M1** — [Nintendo's official Game Boy Advance *Advance Wars* instruction booklet](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/game_boy_advance_8/Manual_GameBoyAdvance_AdvanceWars_EN_DE_FR_ES_IT.pdf), English printed pp. 4–9, 12, 26 and 30. The 79-page multilingual scan has SHA-256 `41cabe7d49c741f42d4b3a4787d4bd1f9e2702e4cac63ef19bba2d35f2d546a6`. Relevant spreads were rendered and inspected; OCR was auxiliary and its errors were not treated as rules.
  - **D1** — [Original-game Field Training dialogue transcription](https://gamefaqs.gamespot.com/gba/471043-advance-wars/faqs/36404), mission 2, recording Nell's terrain demonstration and day handoff. This is a player transcription, not the cartridge itself.
  - **G1** — [Nintendo World Report's 2001 Field Training account](https://www.nintendoworldreport.com/feature/1889/advance-wars-guide-field-training), identifying the `Terrain Intel` lesson and enemy response.
  - **G2** — [Contemporary Game Boy Advance mission guide](https://gamefaqs.gamespot.com/gba/471043-advance-wars/faqs/13909), describing four friendly infantry, enemy infantry/mechs and terrain-oriented attacks. The two written guides disagree on an exact enemy opening count; that count is not asserted.
- Claim IDs: `AW-001`–`AW-007`.

## Mechanical decomposition

### Action Genes

- `ACT-014`: choose an unspent Orange Star infantry and relocate it to a reachable, unoccupied square. This is a selected unit's order, not direct real-time steering of a permanent avatar.
- `ACT-019`: choose the moved or stationary eligible infantry's Fire command and adjacent hostile target. Automatic damage and counterfire are system effects, not separate player actions.
- `ACT-554`: explicitly end the current Orange Star tactical day, forfeiting any remaining optional infantry orders and handing decision authority to Blue Moon. This is not a single soldier's Wait command.
- Claim IDs: `AW-002`, `AW-005`.

### System Behaviour Genes

- `SYS-537`: after Orange Star's End, the computer selects and resolves legal Blue Moon unit orders before restoring the next player day. No exact future enemy intent is promised.
- `SYS-1105`: resolve a direct unit attack from current HP and unit type, reducing the defender's damage by its terrain cover; surviving direct targets can counterfire under the same board state, and zero-HP units are removed. Exact hidden percentage and luck terms remain unmeasured.
- Resolution order: selected unit receives movement range → player commits destination and Fire or Wait → damage and possible counterfire update HP and occupancy → spent unit darkens → player may order other unspent units → End transfers the day → Blue Moon moves and attacks → surviving Orange Star units refresh unless terminal defeat has settled.
- Claim IDs: `AW-002`–`AW-005`.

### Constraint Genes

- `CON-001`: the authored mission map has stable, individually addressable square positions.
- `CON-011`: units cannot finish in the same occupied square; terrain and occupied positions bound legal routes.
- `CON-034`: one friendly unit's day permits at most one relocation followed by one Fire or Wait commitment; an already spent unit cannot act again that day.
- `CON-702`: a route must fit the selected unit's daily movement allowance after charging each entered terrain by that unit's movement type. In this mission ordinary infantry pays more to enter mountains than plains, even though the mountain gives better defensive cover.
- Claim IDs: `AW-002`, `AW-003`.

### Information Genes

- `INF-409`: the grid, unit HP, active/spent state, highlighted movement range and R-button terrain/unit details expose reachability, terrain type and defensive-cover ratings. The movement-cost chart is in the booklet; the interface is not claimed to show every numeric cost. Neither source exposes Olaf's future choice or exact hidden damage terms.
- Claim IDs: `AW-002`, `AW-003`, `AW-006`.

### Objective and Time Genes

- `OBJ-029`: defeat the bounded hostile contingent before the friendly contingent is routed. Capturing a base is not an alternate win in this mission.
- `TIM-018`: Orange Star and computer-controlled Blue Moon take sequential whole-army turns; each side can issue several unit orders before End hands over authority and the day advances. A unit command is not itself the entire faction turn.
- Claim IDs: `AW-001`, `AW-005`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| An Orange Star infantry has an unspent order | Select it and inspect range | Eligible destinations highlight according to unit type and terrain cost | explicit unit and cost visibility | `AW-002`, `AW-006` |
| Two reachable lines differ by mountain entry | Move one infantry onto a mountain | Movement spends more allowance than comparable plain traversal; the unit gains stronger defensive cover on that cell | cost-versus-cover trade-off | `AW-003` |
| A friendly infantry is adjacent to a hostile | Commit Fire on the hostile | Hostile HP drops; if it survives and can answer, cover reduces the friendly unit's received damage; a zero-HP unit disappears | direct exchange and health | `AW-004` |
| One friendly unit has already attacked or waited | Try to order that same unit again | It remains spent until the next Orange Star day | per-unit order exhaustion | `AW-002` |
| Some friendly units remain unspent | Select End | Remaining optional orders lapse and the Blue Moon side moves or attacks before friendly refresh | whole-army handoff | `AW-005` |
| The last required Blue Moon unit reaches zero HP | Inspect mission result | `Terrain Intel` completes without any base capture | terminal rout objective | `AW-001` |

## Strategic and experiential structure

- Local decision: favour a mountain firing position that protects one infantry during counterfire, despite the higher movement cost to reach it.
- Medium-term planning: sequence several infantry attacks so healthier units initiate exchanges and weakened allies finish targets when safe.
- Long-term structure: spend each friendly day positioning and attacking, then absorb a Blue Moon response before the next day; eliminate all hostile units before losing the allied contingent.
- Common heuristics: use R-button intel and the movement highlight before committing, and avoid assuming the enemy AI repeats one fixed route.
- Failure attribution: moving onto exposed plain terrain can increase incoming damage; spending a unit's action poorly or ending early forfeits that day's tactical options.
- Player-trust factors: terrain ratings, HP, unit state and day handoff make the main trade-off visible, while exact enemy choices and damage internals remain uncertain without direct play.
- Claim IDs: `AW-002`–`AW-007`.

## Replay and variation

- The same authored map and teaching order recur; this record does not infer procedural terrain or randomized enemy rosters.
- After Nell's compulsory opening instructions, player-selected attack order and terrain positions can differ. Written accounts warn that AI movement may not follow an identical day-by-day script.
- Replays can improve losses and completion speed; no particular rank is mandatory for this scope.

## Adjacent systems and history

- *Into the Breach* shares selected-piece movement and limited unit actions, but its hostile attacks are telegraphed before a player planning phase. `Terrain Intel` instead gives Blue Moon a later decision-making turn.
- *XCOM 2* shares an AI-controlled enemy squad phase, yet its Action Point economy, concealment, probabilistic ranged cover and objective interaction are outside this simple infantry training map.
- *Civilization VI* supports reuse of a whole-faction multi-command turn, not its hex, city, production, research or diplomacy systems. The relevant *Advance Wars* terrain is square-grid and the packet has no economy.
- The third *Advance Wars* lesson introduces base capture and repair. Those are not silently projected backward into `Terrain Intel`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-014`, `ACT-019`, `ACT-554` | selected infantry, route, Fire target, End |
| System Behaviour | `SYS-537`, `SYS-1105` | opposing AI orders, HP, terrain-scaled direct exchange |
| Constraint | `CON-001`, `CON-011`, `CON-034`, `CON-702` | fixed squares, occupancy, unit order, movement costs |
| Information | `INF-409` | HP, range, R-button unit and terrain intel |
| Objective | `OBJ-029` | hostile contingent removal |
| Time | `TIM-018` | alternating army days with multiple unit orders |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `415` (`GAME-0001`–`GAME-0415`).
- Exact genome matches: none.
- Tied near matches: `GAME-0048` — Tactical Breach Wizards (`5 / 21 = 0.238095`).
- Supported combination subsets: none.
- Scan date: 2026-09-26.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Tactical Breach Wizards (`GAME-0048`) | selected-unit relocation and targeted attack, fixed grid and exclusive occupancy, finite hostile clearance | Advance Wars uses unit-type terrain movement cost, terrain-protected health exchanges, inspectable map intel and alternating whole-army days; Tactical Breach Wizards previews hostile reactions, supports rewinds and resolves a small room with different order constraints | Near, `0.238095` |

## Taxonomy impact

- [`TAXONOMY_CHANGE_154`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_154.md) admits `ACT-554`, `SYS-1105`, `CON-702` and `INF-409`; eight other genes are reused. No earlier signature is changed.

## Negative results

- `INF-009` rejected: the next Blue Moon attack is not an exact committed preview before Orange Star acts.
- `TIM-005` rejected: the enemy chooses orders after the player's End, rather than resolving previously telegraphed commitments.
- `CON-410` rejected: its Civilization VI hex movement, rivers, embarkation and zones of control do not define this square infantry lesson; `CON-702` isolates unit-type terrain cost.
- `SYS-944` rejected: no speed-ranked troop activation, Wait-deferral queue or first-melee-only retaliation governs this army day.
- Base capture, property income, factory production, CO Powers and Fog of War rejected for this mission even though they appear elsewhere in the manual or game.

## Delta summary

This lesson couples chosen infantry order and a whole-army day handoff to unit-specific mountain cost, terrain-protected direct exchanges and visible tactical intel. Four typed boundaries are admitted; selected-unit movement, Fire, per-unit exhaustion, grid occupancy, rout and multi-command turns are reused.

## New facts

- [Confirmed | Direct | High] The mission's dialogue contrasts mountain movement cost and defence, so a slower tile can be the safer attack position (`AW-003`).
- [Confirmed | Corroborated | High] `Terrain Intel` ends on the finite hostile rout, not the property capture introduced in the following lesson (`AW-001`).

## New genes

- [Observation | Direct | High] `ACT-554`, `SYS-1105`, `CON-702` and `INF-409` isolate tactical-day commitment, terrain-protected direct combat, unit-type movement cost and inspectable terrain/unit state.

## New combinations

- [Observation | Limited | High] No new combination is asserted merely from one game's observed conjunction; proper-subset validation remains deterministic.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_154` records the four new boundaries and rejects importing later lesson mechanics.

## New questions

- Which exact North American cartridge revision and difficulty settings reproduce the displayed tutorial HP exchange?
- Do any Blue Moon decision branches or small damage variations alter the teaching script while leaving the same victory predicate?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0417` *Sly Cooper and the Thievius Raccoonus*, only after validation, a local commit and the Goal stop window.
- Optimisation criterion: move from discrete army-level terrain decisions to one authored stealth and traversal route.
- Expected information gain: test whether existing detection, stealth and route-gating genes transfer without importing a whole open-world stealth system.
- Backlog impact: preserve the approved 417–432 order; do not start another subject in this unit.

## Why this game

- [Hypothesis | Corroborated | Medium] The game provides a classic handheld tactical counterpoint to the preceding real-time taxi run, and its named tutorial map lets terrain cost and protective cover be reconstructed without importing the full campaign.
