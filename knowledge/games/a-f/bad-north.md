---
game_id: GAME-0027
slug: bad-north
game_title: Bad North: Jotunn Edition
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0027
gene_ids:
  action:
    - ACT-014
    - ACT-019
  system:
    - SYS-020
    - SYS-045
    - SYS-051
    - SYS-052
  constraint:
    - CON-001
    - CON-071
  information:
    - INF-001
    - INF-016
  objective:
    - OBJ-020
  time:
    - TIM-003
---

# Game: Bad North: Jotunn Edition

## Analysis scope

- Version / ruleset: Jotunn Edition, scoped to one ordinary single-player
  island battle in which a class ability is available.
- Included: squad selection and relocation; autonomous member navigation and
  combat; a targeted class ability and its displacement effect; visible Viking
  longship approach, landing and disembarkation; terrain positioning; houses;
  successive assault waves; battle victory, loss and optional squad flight.
- Excluded: campaign-map routing, fog advance, gold economy, commander
  progression and permanent campaign loss, item / trait acquisition, difficulty
  modes and claims about the distribution of procedurally generated islands.
- Direct-play status: not conducted. Developer and publisher descriptions are
  combined with developer patch notes, a developer interview, Apple editorial
  observation and contemporary hands-on reporting.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BN-001` | The player selects and relocates a commander-led squad at high command granularity rather than steering each soldier | Confirmed | Direct | High | P1, P2 |
| `BN-002` | Individual squad members navigate toward the ordered destination and engage appropriate nearby enemies without per-step or per-strike commands | Confirmed | Direct | High | P1, P2, S1 |
| `BN-003` | Context, class and target priorities determine autonomous formation and combat response after the high-level order | Confirmed | Direct | High | P1, P3 |
| `BN-004` | Optional class abilities let the player select a squad and target area, after which damage, launch, stun or knockback resolves automatically | Confirmed | Direct | High | P3 |
| `BN-005` | Vikings approach in visible longships, land at an island edge and disembark into the live battle | Confirmed | Corroborated | High | P3, S1, S2 |
| `BN-006` | The visible carrier gives actionable advance information about a future landing region but does not expose every disembarked unit's exact later target, effect or execution order | Confirmed | Corroborated | High | S1, S2 |
| `BN-007` | Battle state advances in real time, with pronounced slowdown during squad selection rather than a separate committed-intent resolution phase | Confirmed | Corroborated | High | P1, S1, S3 |
| `BN-008` | The bounded battle is won by repelling the finite arriving Viking force; preserved houses improve the result but are not the same shared failure pool as Into the Breach's Grid | Confirmed | Corroborated | High | P1, S1, C1 |
| `BN-009` | A squad may be ordered to flee through an eligible ship, converting relocation into terminal withdrawal rather than a distinct moment-to-moment control grammar | Confirmed | Corroborated | High | P1, P4, C1 |
| `BN-010` | Island squares, elevation, cliffs, beaches and narrow approaches make destination choice and class counters mechanically consequential | Confirmed | Corroborated | High | P1, P2, S1 |
| `BN-011` | A longship is not an `SYS-022` emergence marker: its approach is continuous, its landing is not prevented by occupying a marked cell and it carries a group rather than scheduling one blockable unit spawn | Confirmed | Corroborated | High | BN-005, BN-006, P3 |

## Basic data

- Release / origin: Plausible Concept developed Bad North; Raw Fury published
  the original release in 2018 and the Jotunn Edition update in 2019.
- Platform or physical form: real-time single-player tactical videogame on a
  small, tile-like three-dimensional island.
- Puzzle family: high-level squad-positioning defence against telegraphed
  carrier-borne assault waves.
- Primary and publisher sources:
  - **[P1]** [Official Bad North site](https://www.badnorth.com/), identifying
    the real-time tactics form, loyal-subject command and island-shape use.
  - **[P2]** [Apple App Store publisher description](https://apps.apple.com/us/app/bad-north/id1441005816),
    explicitly stating that the player positions / relocates troops while
    soldiers navigate and engage intuitively.
  - **[P3]** [Jotunn Edition developer version history](https://apps.apple.com/us/app/bad-north/id1441005816),
    documenting ability targeting / launch effects, combat target priorities,
    ship knock-off and landing stun.
  - **[P4]** [Developer release and patch notes](https://www.badnorth.com/news/2018/8/24/release-bugs-patching-plan),
    corroborating squad flight, ships, disembarkation and the deploy phase.
  - **[P5]** [Nintendo developer interview](https://www.nintendo.com/en-gb/News/2018/April/Interview-Taking-on-hordes-of-invading-Vikings-in-Bad-North-1368315.html),
    corroborating small-island defence and squad command.
- Secondary and editorial sources:
  - **[S1]** [PC Gamer hands-on](https://www.pcgamer.com/bad-north-is-easy-to-pick-up-but-its-a-fiendish-strategy-game/),
    describing live waves about to land, beach repositioning, class counters
    and real-time play.
  - **[S2]** [Apple editorial overview](https://apps.apple.com/af/mac/story/id1446938667),
    describing automatic fighting and longboat arrival.
  - **[S3]** [Faction Calculus first impressions](https://factioncalculus.blogspot.com/2018/12/first-impressions-bad-north.html),
    used only to corroborate strong time slowdown during squad selection.
  - **[C1]** [Bad North community basic-rules summary](https://bad-north.fandom.com/wiki/Bad_North%27s_Basic_Rules),
    used only as community corroboration for waves, house rewards, replenish
    and flee; no canonical boundary rests on it alone.
- Claim IDs: `BN-001`–`BN-011`.

## Mechanical decomposition

### Action Genes

- `ACT-014` — relocate selected controlled board piece. The addressed piece is
  the commander-led squad; the player chooses a legal island destination, not
  each soldier's path or final formation.
- `ACT-019` — select unit ability and target. An available class ability is
  aimed at a position or area; its damage, launch, stun and collision effects
  are automatic.
- Flee is a terminal destination / withdrawal parameter of squad command. The
  scoped evidence does not establish a separate general action grammar beyond
  selecting the squad and committing it to an eligible escape carrier.
- Claim IDs: `BN-001`, `BN-004`, `BN-009`.

### System Behaviour Genes

- `SYS-045` — continuous autonomous agent locomotion. Squad members navigate
  across the island toward the ordered destination without per-step steering.
- `SYS-051` — context-triggered autonomous combat engagement. Eligible soldiers
  acquire, approach or hold against nearby enemies and perform class-bounded
  attacks according to situation and target priority.
- `SYS-052` — carrier-mediated hostile landing. A longship progresses through
  the live scene, makes shore contact and releases its transported group.
- `SYS-020` — attack-induced displacement and collision resolution. Targeted
  abilities can launch or knock units, and Jotunn combat explicitly supports
  enemies being knocked from ships and landing stun.
- Resolution order: player order or carrier approach; member pathfinding / ship
  motion; formation or landing; context target selection; automatic attacks;
  damage, stun, displacement and defeat.
- Claim IDs: `BN-002`–`BN-005`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The battle uses persistent addressable
  island positions, paths, elevations and shoreline approaches.
- `CON-071` — squad-level command granularity. The player can address the
  commander-led group but cannot issue independent destinations or strikes to
  each ordinary member; this is the constraint that makes automatic member
  response strategically central rather than cosmetic assistance.
- Scarce strategic resources: simultaneous squad coverage, travel time between
  shores, healthy members, class counter availability and safe escape access.
- `CON-011` is absent: contacts and formations involve multi-member squads, not
  Sokoban-style one-object-per-cell exclusivity.
- Claim IDs: `BN-001`–`BN-003`, `BN-009`, `BN-010`.

### Information Genes

- `INF-001` — fully visible current state. Current terrain, squads, enemies,
  houses, carriers and battle effects are inspectable.
- `INF-016` — visible carrier-arrival telegraph. An approaching longship is a
  world object that discloses a future landing region before it releases its
  occupants, allowing squads to reposition; exact later hostile intents remain
  unresolved.
- This is not `INF-009`, because no complete acting-unit / target / effect /
  order tuple is committed and shown for every Viking.
- Claim IDs: `BN-005`, `BN-006`, `BN-010`, `BN-011`.

### Objective Genes

- `OBJ-020` — repel finite hostile assault. The island battle completes when
  the bounded arriving Viking force has been neutralised while the defence has
  not collapsed or withdrawn.
- Preserving houses is strategically and economically valuable but does not
  instantiate `OBJ-011`: houses are individual outcomes, not one shared
  infrastructure resource whose non-zero threshold is the documented battle
  horizon condition.
- Claim IDs: `BN-008`, `BN-009`.

### Time Genes

- `TIM-003` — real-time input during forced progression. Ships, soldiers,
  combat and fire continue on the simulation clock; selection slowdown changes
  the rate, not the real-time dependency.
- `TIM-005` is absent because hostile attacks are not all committed, exactly
  previewed and then resolved in a separate ordered phase.
- Claim IDs: `BN-005`–`BN-007`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| One squad is selected away from the threatened beach | Choose a legal destination near that shore | Members path toward the destination and reform without individual movement inputs | high-level relocation and member locomotion are separate | `BN-001`, `BN-002` |
| The relocated squad comes within class-appropriate engagement context | Give no per-soldier attack command | Members select and engage targets according to class and current situation | combat is autonomous rather than an implicit repeated Action | `BN-002`, `BN-003` |
| A longship is visible offshore | Wait while repositioning another squad | The carrier advances, lands, stuns locally and releases its group | approach, landing and release form a continuous carrier transition | `BN-005`–`BN-007` |
| A defender occupies the expected beach position | Let the ship land | Landing still occurs and combat follows; the occupied area does not cancel a marked spawn | rejects `SYS-022` rather than generalising it beyond its blockable marker rule | `BN-011` |
| An available launch ability has a legal target area | Select the ability and target | The effect applies damage / displacement and any contact consequence without another input | reuses `ACT-019` plus `SYS-020` | `BN-004` |
| A squad is ordered toward an eligible escape ship | Commit Flee | Members navigate aboard and the carrier withdraws them from the battle | terminal withdrawal is a destination-specific command outcome | `BN-009` |
| The final hostile group has landed | Eliminate its remaining members | The bounded assault ends and the island result is evaluated, including surviving houses | defines the battle objective independently of campaign progression | `BN-008` |

## Strategic and experiential structure

- Local decision: place a whole squad where its persistent class can exploit
  elevation, shore timing, formation space or a choke point.
- Medium-term planning: read simultaneous carrier approaches, reserve travel
  time and avoid committing every counter to the first landing.
- Long-term structure: survive the complete finite wave sequence with enough
  squad coverage to repel the last arrivals and preserve useful houses.
- Common heuristics: intercept vulnerable boats with archers, hold narrow
  approaches with pikes, keep infantry mobile, and begin cross-island movement
  before the carrier touches shore.
- Failure attribution: the interface makes current approach pressure visible,
  but autonomous micro-resolution means poor terrain, class match-up or late
  repositioning can matter as much as one direct command.
- Player-trust factors: simple destinations produce legible member behaviour;
  the lack of exact hostile intent prevents deterministic Into-the-Breach-style
  calculation while retaining actionable arrival warning.
- Claim IDs: `BN-001`–`BN-011`.

## Replay and variation

- What changes between sessions: island topology, elevations, houses, available
  squads / abilities and the arriving enemy mix.
- Randomness or procedural generation: islands are procedurally generated in
  the wider product, but generation occurs before the scoped live battle and is
  not an in-play gene.
- Multiple viable strategies: squad selection, shore allocation, timing,
  counter usage, ability targets, house triage and evacuation decisions vary.
- Typical replay motive: defend more houses, retain squads and solve a different
  island / force composition; campaign rewards are outside the signature.
- Claim IDs: `BN-003`, `BN-004`, `BN-008`–`BN-010`.

## Adjacent systems and history

- Into the Breach also uses `ACT-014`, `ACT-019` and `SYS-020`, but alternates a
  planning phase with exact committed hostile intents, blockable spawn markers
  and a shared Grid resource. Bad North instead runs continuously and exposes
  carrier approach without exact post-landing intent.
- Lemmings also uses autonomous locomotion in real time, but addresses
  individual agents with temporary roles from a finite skill stock. Bad North
  addresses persistent squads and delegates member navigation and combat.
- World of Goo delegates movement over a live player-built elastic network.
  Bad North supplies fixed terrain and delegates squad member behaviour after a
  destination order; no extraction quota or structural construction is shared.
- Claim IDs: `BN-001`–`BN-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-014`, `ACT-019` | squad destination; available class ability and target |
| System Behaviour | `SYS-020`, `SYS-045`, `SYS-051`, `SYS-052` | displacement, pathfinding, autonomous engagement, carrier landing |
| Constraint | `CON-001`, `CON-071` | island topology and squad-only command authority |
| Information | `INF-001`, `INF-016` | current state and visible arrival telegraph |
| Objective | `OBJ-020` | repel the finite assault |
| Time | `TIM-003` | live simulation with selection slowdown |

Canonical signature:

`ACT-014,ACT-019; SYS-020,SYS-045,SYS-051,SYS-052; CON-001,CON-071; INF-001,INF-016; OBJ-020; TIM-003`

## Corpus comparison

- Indexed games scanned: `GAME-0001`–`GAME-0026`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0026`.
- Exact genome matches: none.
- Existing combination subsets: none.
- Jaccard scores against complete genomes:
  - `GAME-0001`: shared `CON-001`, `INF-001`; `2 / 24 = 0.083333`.
  - `GAME-0002`: shared `CON-001`, `INF-001`; `2 / 17 = 0.117647`.
  - `GAME-0003`: shared `CON-001`; `1 / 20 = 0.050000`.
  - `GAME-0004`: shared `CON-001`, `INF-001`, `TIM-003`; `3 / 24 = 0.125000`.
  - `GAME-0005`: shared `CON-001`, `INF-001`; `2 / 17 = 0.117647`.
  - `GAME-0006`: shared `CON-001`, `INF-001`; `2 / 19 = 0.105263`.
  - `GAME-0007`: shared `INF-001`; `1 / 19 = 0.052632`.
  - `GAME-0008`: shared `CON-001`, `INF-001`; `2 / 17 = 0.117647`.
  - `GAME-0009`: shared `CON-001`, `INF-001`; `2 / 26 = 0.076923`.
  - `GAME-0010`: shared `CON-001`, `INF-001`; `2 / 19 = 0.105263`.
  - `GAME-0011`: shared `ACT-014`, `CON-001`, `INF-001`; `3 / 22 = 0.136364`.
  - `GAME-0012`: shared `CON-001`, `INF-001`; `2 / 19 = 0.105263`.
  - `GAME-0013`: shared `CON-001`, `INF-001`; `2 / 23 = 0.086957`.
  - `GAME-0014`: shared `ACT-014`, `ACT-019`, `SYS-020`, `CON-001`, `INF-001`; `5 / 22 = 0.227273`.
  - `GAME-0015`: shared `CON-001`, `INF-001`; `2 / 24 = 0.083333`.
  - `GAME-0016`: shared `CON-001`, `INF-001`, `TIM-003`; `3 / 24 = 0.125000`.
  - `GAME-0017`: shared none; `0 / 25 = 0.000000`.
  - `GAME-0018`: shared `INF-001`, `TIM-003`; `2 / 29 = 0.068966`.
  - `GAME-0019`: shared `ACT-014`, `CON-001`, `INF-001`; `3 / 19 = 0.157895`.
  - `GAME-0020`: shared `INF-001`; `1 / 25 = 0.040000`.
  - `GAME-0021`: shared `INF-001`, `TIM-003`; `2 / 19 = 0.105263`.
  - `GAME-0022`: shared `INF-001`; `1 / 23 = 0.043478`.
  - `GAME-0023`: shared none; `0 / 22 = 0.000000`.
  - `GAME-0024`: shared `CON-001`, `TIM-003`; `2 / 22 = 0.090909`.
  - `GAME-0025`: shared `SYS-045`, `INF-001`, `TIM-003`; `3 / 20 = 0.150000`.
  - `GAME-0026`: shared `INF-001`, `TIM-003`; `2 / 22 = 0.090909`.
- Mathematically selected near match: `GAME-0014` — Into the Breach at
  `5 / 22 = 0.227273`.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0014` — Into the Breach | `ACT-014`, `ACT-019`, `SYS-020`, `CON-001`, `INF-001` | exact committed intents, rounds, blockable markers and shared infrastructure versus live autonomous squad combat and carrier landings | Near match only |
| `GAME-0025` — Lemmings | `SYS-045`, `INF-001`, `TIM-003` | individual role assignment and rescue quota versus squad-level destinations, contextual combat and assault repulsion | Required boundary comparison; not formal near match |
| `GAME-0026` — World of Goo | `INF-001`, `TIM-003` | live elastic route construction and extraction versus fixed-terrain tactical defence | Required boundary comparison; not formal near match |

- New genes: `SYS-051`, `SYS-052`, `CON-071`, `INF-016`, `OBJ-020`.
- Classification result: `New gene` and a new verified combination.
- Evidence and reasoning: tactical relocation, targeted abilities,
  displacement, fixed addressed terrain, current visibility, autonomous
  locomotion and real-time scheduling survive existing definitions. Neither
  context combat, physical carrier landing, squad-only authority, in-world
  arrival telegraph nor assault repulsion fits a prior boundary.

## Combination record

- Registered [`COMB-0027`](../../combinations/COMB-0027.md), an eight-gene
  proper subset describing squad-level repositioning against visibly
  approaching carrier waves whose members navigate and fight autonomously.
- Targeted abilities, displacement, generic fixed capacity and generic current
  visibility remain in the full genome but are not required for the central
  combination.

## Taxonomy impact

- Registry changes: five stable genes added; seven existing genes reused.
- Taxonomy-change record: none. Player authority, automatic resolution,
  command restrictions, disclosed arrival, terminal condition and live timing
  remain separable under the six current types.
- Candidate terms affected: autonomous contextual engagement, carrier-mediated
  landing, squad-level command granularity, visible arrival telegraph and
  finite-assault repulsion are promoted.

## Negative results

- `ACT-036` and `SYS-046` are absent: class and squad identity persist; the
  player does not assign one temporary behavioural role to an individual agent.
- `SYS-021` is absent: landing is a moving carrier transition, not a fixed-phase
  battlefield hazard applied to predeclared cells.
- `SYS-022` is absent: there is no one-round marker whose occupancy blocks
  hostile emergence and applies a blocking consequence.
- `SYS-050` is absent: soldiers traverse fixed island geometry, not a live
  player-built structure toward extraction.
- `INF-009` is absent: a carrier forecasts arrival but not every hostile unit's
  exact target, effect and execution order.
- `TIM-005` is absent: the battle does not separate planning from an ordered
  committed-hostile resolution phase.
- No structured negative-result record is required; no prior novelty or
  taxonomy proposal was disproven.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Bad North delegates navigation and combat of
  individual soldiers after squad-level relocation (`BN-001`–`BN-003`).
- [Confirmed | Corroborated | High] Visible longship arrival is actionable
  advance information but fails the blockable-marker test for `SYS-022`
  (`BN-005`, `BN-006`, `BN-011`).

## Нові гени

- [Observation | Corroborated | High] Added `SYS-051`, `SYS-052`, `CON-071`,
  `INF-016` and `OBJ-020`; reused seven existing genes.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0027` captures squad-level
  repositioning against visible carrier landings with autonomous member combat.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; all five new
  boundaries fit the existing six types.

## Нові питання

- Does `INF-016` recur when a carrier's path is visible but its exact payload
  composition is concealed?
- Can `CON-071` be reused by games that allow formations or stances but still
  deny direct member-level destinations?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0028` — Loop Hero.
- Optimisation criterion: avoid a third consecutive crowd-routing subject while
  testing autonomous traversal plus player-authored threat creation.
- Expected information gain: test `SYS-045` against a single autonomous hero
  and distinguish world-loop progression from squad or population command.
- Backlog impact: retain HUMANITY and Tin Hearts after Loop Hero.

## Чому саме вона

- [Hypothesis | Limited | High] Loop Hero is mechanically distant from the
  just-added carrier defence grammar but directly tests whether autonomous
  locomotion reuses cleanly when the player edits future encounters rather than
  commanding the moving agent.
