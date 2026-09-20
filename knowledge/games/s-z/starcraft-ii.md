---
game_id: GAME-0317
slug: starcraft-ii
game_title: StarCraft II
analysis_status: reviewed
reviewed: 2026-09-20
combination_ids: []
gene_ids:
  action:
    - ACT-189
  system:
    - SYS-215
    - SYS-297
    - SYS-305
    - SYS-821
  constraint:
    - CON-273
    - CON-330
  information:
    - INF-125
    - INF-224
    - INF-225
  objective:
    - OBJ-185
  time:
    - TIM-003
---

# Game: StarCraft II

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Raynor, Marines,
Normal difficulty and the Logistics Headquarters are carrier parameters rather
than separate genes.

## Analysis scope

- Version / ruleset: current unmodified English Windows Battle.net application,
  checked 2026-09-20, using the free original *Wings of Liberty* campaign under
  the StarCraft II 5.x client family. Blizzard exposes no stable public client
  build identifier on the reviewed pages, so no more precise binary number is
  asserted. The packet covers only the first campaign mission, `Liberation
  Day`, on Normal difficulty from a fresh campaign.
- Structured analysis target: English Windows Battle.net StarCraft II,
  *Wings of Liberty*, fresh campaign, Normal, `Liberation Day`; see
  `GAME-0317` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: select Raynor and the available Marines; inspect their
  health, current commands, terrain, minimap, fog and mission objective; issue
  move, attack-move or focused-attack orders along the authored road; let
  pathing, sight, target acquisition and fire resolve in real time; regroup the
  scripted reinforcements and keep Raynor alive until the Logistics
  Headquarters is destroyed.
- Entry: the first ordinary controllable frame of `Liberation Day`, with Jim
  Raynor and five Marines on the Mar Sara road before the player issues an
  order.
- Positive terminal: the designated Logistics Headquarters is destroyed while
  Raynor remains alive, the mission reports completion and the fresh campaign
  retains access to its successor mission, `The Outlaws`.
- Negative terminal: Raynor reaches his defeat state before the Headquarters is
  destroyed; the current attempt cannot reach the declared mission terminal.
- Included: rectangular and additive unit selection; move, attack-move, focused
  attack, stop and hold-position commands; automatic pathing and basic attack
  acquisition; current unit health and command-card state; current allied
  sight, explored terrain, fog and minimap; finite authored Dominion groups;
  scripted friendly Marine reinforcements placed under player command; Raynor's
  mission-critical survival; the designated-structure terminal and retained
  successor mission.
- Excluded: optional destruction of six Dominion holoboards and its achievement;
  exhaustive enemy clearance; preservation or command of civilian allies;
  tutorial prompts as a required progression system; production, minerals,
  gas, supply, workers, buildings, upgrades and research, because `Liberation
  Day` exposes none of those player economies; campaign choices, Hyperion
  upgrades, later missions, Challenge Missions, Arcade, Co-op, Versus, AI,
  multiplayer, editor, custom campaigns, achievements, account progression,
  replays, saves and reload verification; *Heart of the Swarm*, *Legacy of the
  Void* and *Nova Covert Ops*.
- Reproducible parameterisation: install the current English Windows client
  through Battle.net, start a fresh free *Wings of Liberty* campaign on Normal,
  enter `Liberation Day`, leave the optional holoboard objective incomplete if
  encountered, group Raynor with the Marines, follow the authored road, absorb
  the scripted Marine reinforcements, focus hostile groups only as required to
  reach the outpost, destroy the Logistics Headquarters and stop at the first
  completed mission state that exposes `The Outlaws`. Exact group geometry,
  damage distribution, surviving Marine count and command timing remain run
  parameters.
- Potential scoped modules: the same mission with all six holoboards; `The
  Outlaws`, which first adds a base economy and unit production; one later
  mission with campaign upgrades; one fixed multiplayer ruleset.
- Direct-play status: not conducted. No Windows installation, Battle.net
  session, account trace, input log, campaign save or executable build was
  available. Blizzard's release, free-campaign, controls, manual and 5.0
  materials establish the product and command vocabulary; complete written
  mission references establish the opening roster, reinforcements, objectives
  and terminal. No video or audio was opened, played or analysed. This is a
  source-bounded reconstruction, not a claimed playthrough or reload test.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SC2-001` | Blizzard released *StarCraft II: Wings of Liberty* on 2010-07-27 and now offers its original campaign free through StarCraft II | Confirmed | Direct | High | P1, P2 |
| `SC2-002` | Blizzard's reviewed current campaign line is compatible with the 5.x client family, but the public pages do not expose a stable install build number | Observation | Direct | Medium | P2, P5 |
| `SC2-003` | The official command guide supports rectangular/additive selection, move, attack-move, focus fire, stop, hold, queued orders, control groups and camera movement | Confirmed | Direct | High | P3 |
| `SC2-004` | `Liberation Day` is the first *Wings of Liberty* mission and starts with Raynor plus five Marines | Observation | Corroborated | High | S1, S2 |
| `SC2-005` | The required objectives are to destroy the Logistics Headquarters and keep Raynor alive | Observation | Corroborated | High | S1–S3 |
| `SC2-006` | Authored drop-pod events add controllable Marine reinforcements during the road advance | Observation | Corroborated | High | S1, S2 |
| `SC2-007` | The mission uses selected-unit pathing, sight, health and continuous ranged combat but does not expose a player production or resource economy | Observation | Corroborated | High | P3, S1, S2 |
| `SC2-008` | Destroying the designated Headquarters while Raynor survives settles the mission and advances the campaign to `The Outlaws` | Observation | Corroborated | High | S1–S3 |
| `SC2-009` | Six Dominion holoboards are an optional objective and are not required for the ordinary mission terminal | Observation | Corroborated | High | S1–S3 |

## Basic data

- Release / origin: developed and published by Blizzard Entertainment;
  *StarCraft II: Wings of Liberty* released on 2010-07-27.
- Platform or physical form: current English Windows Battle.net application;
  one free single-player campaign mission on Normal is scoped.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  agent routing and coordination; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-20:
  - **[P1]** [Blizzard's fifth-anniversary notice](https://news.blizzard.com/en-us/article/19831343/5th-anniversary-of-starcraft-ii),
    for the 2010-07-27 public release date and product identity.
  - **[P2]** [Blizzard's free-to-play announcement](https://news.blizzard.com/en-us/article/21173629/starcraft-ii-going-free-to-play-explained),
    for free access to the original *Wings of Liberty* campaign and separation
    from later campaign products.
  - **[P3]** [Blizzard's simplified controls guide](https://news.blizzard.com/en-us/article/6640645/game-guide-simplified-controls),
    for selection, movement, attack-move, focus fire, stop, hold, queued orders,
    control groups and camera commands.
  - **[P4]** [official *Wings of Liberty* quick-start guide](https://dist.blizzard.com.edgesuite.net/sc2/WoL_enSG_Manual.pdf),
    for the English Windows product, Battle.net client identity and original
    campaign context.
  - **[P5]** [official StarCraft II 5.0 patch notes](https://news.blizzard.com/en-us/article/23482838/starcraft-ii-5-0-patch-notes),
    for continued first-party support of *Wings of Liberty* missions inside the
    5.x client family; this does not establish a current binary build number.
- Corroborating textual sources, accessed 2026-09-20:
  - **[S1]** [IGN's written *Liberation Day* guide](https://www.bazicenter.com/features/starcraft2_ignpdf.pdf),
    pages 13–14, for the opening roster, selection-and-movement route, scripted
    reinforcements, primary target and optional holoboards.
  - **[S2]** [Liquipedia `Liberation Day` record](https://liquipedia.net/starcraft2/Campaign/Liberation_Day),
    for the first-mission identity, five Marines plus Raynor, reinforcements,
    main objectives and successor campaign context.
  - **[S3]** [StarCraft Wiki `Liberation Day` record](https://starcraft.fandom.com/wiki/Liberation_Day),
    for the required outpost objective, Raynor survival condition, six optional
    holoboards and ordinary mission completion.
- Research record: **[R1]** local preflight on 2026-09-20 found no installed
  Windows client, Battle.net session, campaign save, input trace or lawful
  direct-play environment. No audiovisual evidence was used.
- Claim IDs: `SC2-001`–`SC2-009`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-189`: select Raynor, one Marine or a multi-unit group and
  commit a movement, attack-move, focused-attack, stop or hold-position order.
  Control-group assignment is a selection shortcut inside this boundary, not a
  distinct mechanical action gene. Claims: `SC2-003`, `SC2-004`, `SC2-007`.

### System Behaviour Genes

- Existing `SYS-215`: resolve ranged fire, health loss and defeat continuously;
  `SYS-297`: execute committed paths and acquire ordered legal targets;
  `SYS-305`: update current allied sight and fog from unit positions;
  `SYS-821`: place authored Marine reinforcements under player command without
  production or cost.
- Resolution order: accept a group order; resolve pathing and current sight;
  acquire an eligible target when the order permits; exchange live fire and
  update health/defeat; apply authored reinforcements at their mission event;
  evaluate Raynor viability and then the Headquarters terminal. Claims:
  `SC2-003`–`SC2-008`.

### Constraint Genes

- Existing `CON-273`: an ordinary hostile position and direct target are
  actionable only while current allied sight exposes them; `CON-330`: the
  mission remains viable only while its declared critical actor, Raynor, is
  alive.
- Scarce resources: finite initial and scripted Marine bodies, each unit's
  health, current sight, frontage, travel time and Raynor's non-replaceable
  mission viability. There are no player resource stockpiles or production
  queues in scope. Claims: `SC2-005`–`SC2-007`.

### Information Genes

- Existing `INF-125`: the current objective panel and authored target expose the
  mission gate; `INF-224`: the command view exposes current selection, health
  and available commands where economy/production fields are absent;
  `INF-225`: explored terrain remains legible while current hostile state is
  hidden outside allied sight.
- The optional holoboard counter and tutorial instructions do not enter the
  required information signature. Claims: `SC2-003`, `SC2-005`, `SC2-007`,
  `SC2-009`.

### Objective Genes

- New `OBJ-185`: destroy the one designated hostile mission structure while
  the declared critical actor remains viable, accept mission completion and
  retain the next campaign mission.
- This is not `OBJ-166`: hostile Marines may remain, and the ordinary terminal
  is triggered by the Logistics Headquarters rather than elimination of every
  declared hostile. Optional holoboards and achievements are not required.
  Claims: `SC2-005`, `SC2-008`, `SC2-009`.

### Time Genes

- Existing `TIM-003`: movement, pathing, fog, firing, health, reinforcements and
  mission evaluation advance in real time while the player continues issuing
  orders. Claims: `SC2-006`–`SC2-008`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Raynor and five Marines are controllable on the opening road | Drag-select the group and issue a destination | Every selected unit follows a navigable path while its sight updates | multi-unit selection, command and fog | `SC2-003`, `SC2-004`, `SC2-007` |
| A Dominion patrol becomes visible | Issue focus fire or attack-move | Eligible units approach or hold range, fire by cadence and update target health until defeat or a replacement order | commanded real-time combat | `SC2-003`, `SC2-007` |
| The group reaches the authored reinforcement event | Continue along the road | Drop pods place additional Marines under player command without cost or a queue | scripted force growth, not production | `SC2-006` |
| A hostile leaves current allied sight | Continue or reposition | Explored terrain remains, but current unit state and direct targeting cease until vision returns | current fog differs from terrain memory | `SC2-007` |
| Raynor reaches zero health before the Headquarters falls | Continue the attempt | the mission's required-actor predicate fails and the declared positive terminal is unavailable | mission-critical survival gate | `SC2-005` |
| The Logistics Headquarters is visible and Raynor lives | Focus the controlled group on the structure | pathing and fire reduce the structure to destruction; the required objective settles and the successor mission becomes available | designated-structure campaign terminal | `SC2-005`, `SC2-008` |
| One or more optional holoboards remain intact when the Headquarters falls | Accept mission completion | ordinary mission progression still settles; only optional credit is incomplete | optional content is not a terminal prerequisite | `SC2-009` |

## Strategic and experiential structure

- Local decision: choose a group, destination, engagement range and focus
  target while hostile fire continues.
- Medium-term planning: preserve Raynor and enough Marines for the outpost by
  avoiding fragmented pathing, concentrating fire and regrouping scripted
  reinforcements.
- Long-term structure: none beyond the single road-to-outpost mission; the
  campaign economy and mission graph are excluded.
- Common heuristics: keep ranged units together, focus one visible hostile,
  withdraw damaged ordinary Marines when space permits, place Raynor where he
  can contribute without taking unrecoverable concentrated fire, and do not
  confuse optional holoboards with the required Headquarters.
- Failure attribution: selection highlights, health bars, command feedback,
  fog, objective text and Raynor's declared survival condition make losses and
  target progress legible; exact hostile AI decisions remain bounded live
  counterplay.
- Player-trust factors: the required target and critical actor are named before
  terminal evaluation, while reinforcements arrive at authored mission events
  rather than through an undisclosed player economy.
- Claim IDs: `SC2-003`–`SC2-009`.

## Replay and variation

- What changes between attempts: selection grouping, path geometry, focus-fire
  order, damage distribution, surviving Marine count and whether optional
  holoboards are attacked.
- Randomness or procedural generation: the mission path, target and scripted
  reinforcement events are authored; no generated map or production economy is
  claimed.
- Multiple viable strategies: the player can vary group geometry, focus order
  and optional detours while preserving Raynor and eventually destroying the
  Headquarters.
- Typical replay motive: reduce losses, complete optional achievements or use a
  higher difficulty; those post-first-terminal goals are outside this packet.

## Adjacent systems and history

- Direct predecessors: the original *StarCraft* established the series' RTS
  command vocabulary, but no mechanical identity across releases is assumed.
- Variants: later campaign missions, 2010 launch binaries, other difficulty
  settings, expansions, multiplayer balance and custom campaigns are separate
  rulesets.
- Similar games: `GAME-0275` *Command & Conquer Remastered Collection* shares
  selected-unit orders, pathing, fog, scripted reinforcements and a retained
  campaign successor; `GAME-0179` *Age of Empires II: Definitive Edition* adds a
  full worker economy, production, technology and civilization-wide terminal.
- Important differences: `Liberation Day` begins and ends with a supplied
  combat group. It has no harvesting, building, training, supply or research;
  victory depends on one designated structure and Raynor survival rather than
  total hostile elimination.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-189` | Raynor; Marines; selection; move; attack-move; focus fire |
| System Behaviour | `SYS-215`, `SYS-297`, `SYS-305`, `SYS-821` | pathing; ranged cadence; fog; drop-pod reinforcements |
| Constraint | `CON-273`, `CON-330` | current sight; Raynor survival |
| Information | `INF-125`, `INF-224`, `INF-225` | objective panel; health; command card; minimap; explored terrain |
| Objective | `OBJ-185` | destroy Logistics Headquarters; retain `The Outlaws` |
| Time | `TIM-003` | live movement, combat and event progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `316` (`GAME-0001`–`GAME-0316`).
- Exact genome matches: none.
- Tied near matches: `GAME-0275` — Command & Conquer Remastered Collection (`9 / 21 = 0.428571`).
- Supported combination subsets: none.
- Scan date: 2026-09-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0275` — Command & Conquer Remastered Collection | `ACT-189`, `SYS-215`, `SYS-297`, `SYS-305`, `SYS-821`, `CON-273`, `INF-224`, `INF-225`, `TIM-003` | Both command supplied real-time groups through pathing, combat, sight and fog, and both receive authored reinforcements before a retained campaign successor. Command & Conquer converts its supplied construction vehicle and credits into power, buildings and a unit queue, then eliminates a declared hostile set. StarCraft II's opening instead has no player economy or production: it preserves Raynor and destroys one designated Headquarters while ordinary hostiles may remain. | Near, `0.428571` |

### Preserved research notes

- New genes: `OBJ-185`.
- Classification result: `New gene`.
- Evidence and reasoning: existing campaign objectives either clear a complete
  hostile set, resolve a character target through a separate exit, or require a
  route/encounter terminal. None covers one designated hostile structure whose
  destruction directly settles the mission while a named critical actor must
  remain viable and a successor mission is retained.

## Taxonomy impact

- Registry changes: add `OBJ-185`; extend supporting evidence for eleven reused
  RTS, mission and real-time genes.
- Taxonomy-change record: none.
- Candidate terms affected: Raynor, Marines, `Liberation Day`, Logistics
  Headquarters, holoboards, Normal and Battle.net remain carrier parameters,
  labels or exclusions rather than new genes.

## Negative results

- No separate negative-result record. `ACT-316`, `SYS-551`, `CON-467` and
  `OBJ-166` were tested and rejected. `Liberation Day` exposes no player
  production queue, prerequisites or stockpiles, and its ordinary terminal does
  not require eliminating the complete hostile set.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original *Wings of Liberty* campaign remains
  a free StarCraft II campaign, and Blizzard documents the RTS unit-command
  vocabulary (`SC2-001`–`SC2-003`).
- [Observation | Corroborated | High] `Liberation Day` supplies Raynor, five
  Marines and scripted reinforcements, then requires the Logistics Headquarters
  to be destroyed while Raynor survives (`SC2-004`–`SC2-008`).

## New genes

- [Observation | Corroborated | High] `OBJ-185` isolates the first-mission
  designated-structure terminal with critical-actor survival and retained
  campaign succession.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Direct | High] No taxonomy changes.

## New questions

- Which economy genes first become necessary when `The Outlaws` adds workers,
  minerals, supply, structures and Marine production?
- Does completing all optional `Liberation Day` holoboards retain its
  achievement identically after a clean client relaunch?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0318` Battletoads.
- Optimisation criterion: move from mouse-directed group combat to a fixed NES
  side-scrolling opening stage with direct body control and partner-compatible
  encounter pressure.
- Expected information gain: test whether Battletoads' opening-stage combat,
  mounted transition and level-clear boundary reuse current arcade genes or
  require a distinct vehicle handoff.
- Backlog impact: `GAME-0318` remains next; no later unit starts in this commit.

## Why this game

- [Hypothesis | Limited | High] StarCraft II is a recognisable RTS anchor whose
  first mission cleanly separates command, fog, reinforcements and mission
  settlement from the production economy often assumed to define the genre.
