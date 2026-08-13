---
game_id: GAME-0028
slug: loop-hero
game_title: Loop Hero
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0028
gene_ids:
  action:
    - ACT-039
    - ACT-040
    - ACT-041
  system:
    - SYS-004
    - SYS-035
    - SYS-045
    - SYS-051
    - SYS-053
    - SYS-054
  constraint:
    - CON-001
    - CON-072
    - CON-073
    - CON-074
  information:
    - INF-001
    - INF-002
  objective:
    - OBJ-021
  time:
    - TIM-003
---

# Game: Loop Hero

## Analysis scope

- Version / ruleset: the 2021 base game, scoped to one ordinary resource-
  gathering expedition on an already generated loop, ending in voluntary
  retreat or defeat before a chapter boss.
- Included: autonomous forward traversal and combat; random dawn spawning;
  enemy-derived cards and equipment; selecting and placing road, roadside or
  landscape cards; equipping loot; placed-tile enemy production; loop passage
  and escalation; campfire passage; voluntary retreat, death and resource
  retention.
- Excluded: pre-expedition deck construction, hero-class unlocks, survivor-camp
  construction and upgrades, traits, narrative, chapter bosses and their meter,
  late-game tile exceptions, mobile-port presentation and exact balance values.
- Direct-play status: not conducted. A developer postmortem and publisher
  description are combined with Nintendo's platform editorial and two
  contemporary hands-on analyses.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `LH-001` | The hero advances forward around a predetermined closed route without player movement commands | Confirmed | Direct | High | P1, S1, S2 |
| `LH-002` | Contact with enemies starts combat whose target selection and attacks resolve without player-issued strikes | Confirmed | Direct | High | P1, S1, S2 |
| `LH-003` | Defeating enemies can supply equipment and cards; the player may equip loot and place selected cards while the expedition continues | Confirmed | Direct | High | P1, P2, S1 |
| `LH-004` | Card type restricts legal placement to road, roadside or off-road landscape regions, and the resulting tile changes future traversal conditions | Confirmed | Corroborated | High | P1, P2, C1 |
| `LH-005` | Some placed tiles periodically or conditionally produce enemies on nearby route positions, so the player authors later encounters rather than spawning a unit directly | Confirmed | Direct | High | P1, S1 |
| `LH-006` | Dawn and combat rewards include unresolved random outcomes, including monster appearance, card opportunity and loot | Confirmed | Corroborated | High | P1, S1 |
| `LH-007` | Completing another circuit strengthens future enemies, making each voluntary continuation an escalation commitment | Confirmed | Direct | High | P2 |
| `LH-008` | At campfire passage the player may return with accumulated resources or continue; retreat mid-loop and death preserve progressively less | Confirmed | Corroborated | High | P2, S1 |
| `LH-009` | The loop, current enemies, hero state, equipment inventory, cards and resources are visible, but future random drops and dawn spawns are not exact previews | Confirmed | Corroborated | High | P1, S1 |
| `LH-010` | Hero motion and day time advance on a live clock, while pause permits card and equipment planning without converting the expedition into a pre-run program | Confirmed | Corroborated | High | P1, S1 |
| `LH-011` | The expedition's immediate controllable objective is to accumulate and safely bank resources before escalation or defeat destroys a larger share | Confirmed | Corroborated | High | P2, S1 |

## Basic data

- Release / origin: Four Quarters developed Loop Hero; Devolver Digital
  published it on 4 March 2021.
- Platform or physical form: a real-time, pauseable digital strategy RPG with a
  fixed-per-expedition cyclic route, automatic hero and a card-placement map.
- Puzzle family: player-authored risk escalation around an autonomous expedition
  circuit.
- Primary and publisher sources:
  - **[P1]** Four Quarters,
    [“Postmortem: Loop Hero”](https://www.gamedeveloper.com/design/postmortem-loop-hero),
    a developer account of the self-walking / self-fighting hero, equipment,
    inventory overflow, cards and a roadside mausoleum spawning skeletons.
  - **[P2]** [Steam developer / publisher listing](https://store.steampowered.com/app/1282730/Loop_Hero/?l=english),
    documenting placement of enemies, buildings and terrain, generated loop
    paths, equippable loot and resource / survival balance.
- Platform-holder editorial:
  - **[N1]** [Nintendo Indie World overview](https://www.nintendo.com/jp/topics/article/c203d1d4-6df2-4fba-b4d8-dd76d44db432),
    visually explaining automatic walking and combat, map-card intervention,
    per-loop enemy strengthening, camp return and resource loss on defeat.
- Contemporary corroboration:
  - **[S1]** [GameSpot hands-on](https://www.gamespot.com/articles/i-appreciate-how-loop-hero-breaks-down-a-roguelike-into-approachable-tasks/1100-6486073/),
    describing automatic forward traversal / combat, random dawn spawns,
    enemy-derived card chances, pausable placement, fixed direction and
    location-dependent retreat loss.
  - **[S2]** [GameSpot review](https://www.gamespot.com/reviews/loop-hero-review/1900-6417656/),
    corroborating indirect control, automated battle and risk / reward.
  - **[C1]** [Community card taxonomy](https://loophero.fandom.com/wiki/Cards),
    used only to corroborate road / roadside / landscape placement categories
    and not as the sole source of a canonical mechanic.
- Claim IDs: `LH-001`–`LH-011`.

## Mechanical decomposition

### Action Genes

- `ACT-039` — place selected held world card. The player selects one available
  card and one type-compatible map position, committing a road, roadside or
  landscape tile that changes later expedition conditions.
- `ACT-040` — replace equipped item from current loot. The player selects an
  inventory item for a compatible hero slot, replacing the current equipment
  and thereby changing stats used by automatic combat.
- `ACT-041` — commit voluntary expedition retreat. The player terminates the
  expedition and banks the resource share allowed at the hero's current route
  position; campfire passage provides the safest decision point.
- `ACT-026` is absent: the card comes from a visible selectable hand rather
  than a mandatory supply head, and rotation is not the defining choice.
- Claim IDs: `LH-003`, `LH-004`, `LH-008`.

### System Behaviour Genes

- `SYS-045` — continuous autonomous agent locomotion. The hero advances in one
  direction along the loop without destination or step commands.
- `SYS-051` — context-triggered autonomous combat engagement. Encountering an
  enemy starts automatic target selection and attacks; the player's upstream
  card and equipment decisions shape the result.
- `SYS-053` — placed-tile recurring encounter production. Eligible placed
  world tiles cause enemies to be introduced on their own or nearby route
  positions according to day, loop or tile-specific cadence.
- `SYS-054` — circuit-completion difficulty escalation. Crossing the campfire
  to begin another circuit increments loop progression and strengthens later
  enemies.
- `SYS-035` — earned action-supply replenishment. Defeating enemies can add new
  playable world cards to the currently available hand.
- `SYS-004` — random outcome selection. Dawn monster positions, whether an
  enemy yields a card and equipment / reward identities include unresolved
  random choices.
- Claim IDs: `LH-001`–`LH-007`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Once generated, the expedition exposes
  persistent route and surrounding map positions addressed by card placement.
- `CON-072` — card-type map-zone eligibility. Road cards occupy route positions,
  roadside cards require adjacency to the route, and landscape cards occupy
  the remaining eligible map region; individual cards may add narrower rules.
- `CON-073` — fixed cyclic traversal route. During the expedition the hero's
  movement path is one closed circuit with predetermined direction; placed
  world cards modify positions and encounters but do not branch or redirect the
  route.
- `CON-074` — location-conditioned retreat retention. Voluntary expedition exit
  banks a resource share determined by whether the hero is at the campfire or
  mid-loop, while defeat retains less than safe camp retreat.
- Scarce strategic resources: current health, equipment / card inventory
  capacity, safe route distance to camp, encounter density and accumulated
  resources at risk.
- Claim IDs: `LH-001`, `LH-004`, `LH-008`, `LH-011`.

### Information Genes

- `INF-001` — fully visible current state. Current loop tiles, hero position and
  health, known enemies, cards, equipment and collected resources are exposed.
- `INF-002` — unpreviewed random future event. The exact next random dawn spawn,
  dropped card opportunity or loot identity is not disclosed before selection.
- Claim IDs: `LH-006`, `LH-009`.

### Objective Genes

- `OBJ-021` — secure accumulated expedition resources. The scoped expedition
  objective is to gather resources through authored risk and end the attempt by
  banking them, preferably at the safe campfire boundary before death or a
  mid-loop retreat penalty destroys a larger share.
- Boss defeat is excluded from this resource-run signature; it can be tested as
  a later objective instance without redefining ordinary expedition decisions.
- Claim IDs: `LH-008`, `LH-011`.

### Time Genes

- `TIM-003` — real-time input during forced progression. The hero walks, the
  day clock advances and encounters occur while player map and equipment
  decisions remain available between combat locks; pause provides planning time.
- `TIM-006` is absent: the player edits the world during the same live run,
  rather than completing a machine design before a resettable automatic test.
- Claim IDs: `LH-001`, `LH-002`, `LH-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Hero occupies an ordinary route tile with no enemy | Give no movement input | Hero advances forward to the next route position | locomotion is autonomous and route direction is fixed | `LH-001` |
| Hero reaches a route position containing an enemy | Give no attack input | Automated combat resolves attacks until the encounter ends | reuses contextual autonomous engagement beyond squad combat | `LH-002` |
| A roadside enemy-producing card is in hand | Place it at a legal route-adjacent position | The tile becomes persistent and later produces enemies on eligible nearby route positions | player authors a generator rather than spawning one enemy directly | `LH-004`, `LH-005` |
| The same roadside card is aimed at a non-adjacent landscape position | Attempt placement | The placement is rejected until a type-compatible zone is chosen | zone eligibility is a Constraint, not card presentation | `LH-004` |
| An enemy is defeated | No reward-selection command | Equipment and a chance of card supply resolve; any obtained card becomes a later placement option | reward generation is separate from card placement | `LH-003`, `LH-006` |
| Hero crosses the campfire after one circuit | Continue rather than retreat | Loop count advances and later enemies become stronger | another circuit is a difficulty commitment, not repeated identical motion | `LH-007`, `LH-008` |
| Hero reaches campfire with collected resources | Commit retreat | Expedition ends and the safe retained share is banked | resource security is a location-sensitive terminal decision | `LH-008`, `LH-011` |
| Hero dies before retreat | No further input | Expedition ends and most carried resources are lost | failure pressure acts on banked outcome rather than route legality | `LH-008`, `LH-011` |

## Strategic and experiential structure

- Local decision: choose whether one card's immediate benefit, future enemy
  production or placement synergy improves survival enough to justify its risk.
- Medium-term planning: sequence dangerous tiles relative to healing, campfire
  support and the time needed to obtain better equipment before reaching them.
- Long-term structure: increase encounter density enough to earn cards, loot
  and resources while keeping a viable path to safe retreat before per-loop
  escalation overtakes the build.
- Common heuristics: cluster manageable enemies before recovery; delay high-
  cadence generators; keep equipment current; treat each camp passage as a
  fresh risk decision rather than automatically continuing.
- Failure attribution: combat micro is automatic, so defeat primarily traces to
  prior map density, placement geometry, equipment replacement and one-loop-too-
  many escalation rather than missed attack inputs.
- Player-trust factors: current stats and map consequences are inspectable, but
  random drops and some tile synergies require probabilistic planning and
  learned system knowledge.
- Claim IDs: `LH-001`–`LH-011`.

## Replay and variation

- What changes between sessions: generated route geometry, available deck,
  card / equipment rewards, random spawns and the player's placed world.
- Randomness or procedural generation: route generation occurs before the
  scoped loop; dawn spawns and reward selection continue during play.
- Multiple viable strategies: placement location and timing, encounter density,
  equipment stat tradeoffs, pause cadence and retreat threshold vary.
- Typical replay motive: bank more resources, test tile interactions, survive
  another circuit or prepare a later boss attempt.
- Claim IDs: `LH-003`–`LH-011`.

## Adjacent systems and history

- Lemmings supplies many autonomous walkers and lets the player assign scarce
  roles that alter agents or terrain. Loop Hero supplies one permanently
  autonomous hero and lets the player place persistent world conditions that
  create future encounters.
- Bad North also delegates locomotion and combat, but the player relocates whole
  squads against external carrier arrivals. Loop Hero never commands the hero's
  destination and authors threats on the fixed cyclic route.
- World of Goo's loose agents traverse a live player-built force network toward
  extraction. Loop Hero's route is fixed before the expedition and world cards
  alter encounter content rather than structural reachability.
- Dorfromantik also earns placement supply through play, but commits a mandatory
  supply head to expand terrain for score. Loop Hero chooses from a hand and
  modifies a fixed loop to balance autonomous survival and resource risk.
- Claim IDs: `LH-001`–`LH-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-039`, `ACT-040`, `ACT-041` | card placement, equipment replacement and retreat |
| System Behaviour | `SYS-004`, `SYS-035`, `SYS-045`, `SYS-051`, `SYS-053`, `SYS-054` | random rewards, card supply, autonomous hero, encounter production and loop escalation |
| Constraint | `CON-001`, `CON-072`, `CON-073`, `CON-074` | addressed map, placement zones, fixed cycle and retreat retention |
| Information | `INF-001`, `INF-002` | visible current run and unpreviewed random outcomes |
| Objective | `OBJ-021` | accumulate and bank expedition resources |
| Time | `TIM-003` | live progression with pause |

Canonical signature:

`ACT-039,ACT-040,ACT-041; SYS-004,SYS-035,SYS-045,SYS-051,SYS-053,SYS-054; CON-001,CON-072,CON-073,CON-074; INF-001,INF-002; OBJ-021; TIM-003`

## Corpus comparison

- Indexed games scanned: `GAME-0001`–`GAME-0027`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0027`.
- Exact genome matches: none.
- Existing combination subsets: none.
- Jaccard scores against complete genomes:
  - `GAME-0001`: shared `SYS-004`, `CON-001`, `INF-001`, `INF-002`; `4 / 27 = 0.148148`.
  - `GAME-0002`: shared `CON-001`, `INF-001`; `2 / 22 = 0.090909`.
  - `GAME-0003`: shared `CON-001`; `1 / 25 = 0.040000`.
  - `GAME-0004`: shared `SYS-004`, `CON-001`, `INF-001`, `TIM-003`; `4 / 28 = 0.142857`.
  - `GAME-0005`: shared `CON-001`, `INF-001`; `2 / 22 = 0.090909`.
  - `GAME-0006`: shared `CON-001`, `INF-001`; `2 / 24 = 0.083333`.
  - `GAME-0007`: shared `INF-001`; `1 / 24 = 0.041667`.
  - `GAME-0008`: shared `CON-001`, `INF-001`; `2 / 22 = 0.090909`.
  - `GAME-0009`: shared `SYS-004`, `CON-001`, `INF-001`, `INF-002`; `4 / 29 = 0.137931`.
  - `GAME-0010`: shared `CON-001`, `INF-001`; `2 / 24 = 0.083333`.
  - `GAME-0011`: shared `CON-001`, `INF-001`; `2 / 28 = 0.071429`.
  - `GAME-0012`: shared `CON-001`, `INF-001`; `2 / 24 = 0.083333`.
  - `GAME-0013`: shared `CON-001`, `INF-001`; `2 / 28 = 0.071429`.
  - `GAME-0014`: shared `CON-001`, `INF-001`; `2 / 30 = 0.066667`.
  - `GAME-0015`: shared `SYS-004`, `CON-001`, `INF-001`; `3 / 28 = 0.107143`.
  - `GAME-0016`: shared `SYS-004`, `CON-001`, `INF-001`, `TIM-003`; `4 / 28 = 0.142857`.
  - `GAME-0017`: shared none; `0 / 30 = 0.000000`.
  - `GAME-0018`: shared `SYS-004`, `INF-001`, `INF-002`, `TIM-003`; `4 / 32 = 0.125000`.
  - `GAME-0019`: shared `CON-001`, `INF-001`; `2 / 25 = 0.080000`.
  - `GAME-0020`: shared `SYS-004`, `SYS-035`, `INF-001`; `3 / 28 = 0.107143`.
  - `GAME-0021`: shared `INF-001`, `TIM-003`; `2 / 24 = 0.083333`.
  - `GAME-0022`: shared `INF-001`; `1 / 28 = 0.035714`.
  - `GAME-0023`: shared none; `0 / 27 = 0.000000`.
  - `GAME-0024`: shared `CON-001`, `TIM-003`; `2 / 27 = 0.074074`.
  - `GAME-0025`: shared `SYS-045`, `INF-001`, `TIM-003`; `3 / 25 = 0.120000`.
  - `GAME-0026`: shared `INF-001`, `TIM-003`; `2 / 27 = 0.074074`.
  - `GAME-0027`: shared `SYS-045`, `SYS-051`, `CON-001`, `INF-001`, `TIM-003`; `5 / 24 = 0.208333`.
- Mathematically selected near match: `GAME-0027` — Bad North at
  `5 / 24 = 0.208333`.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0027` — Bad North | `SYS-045`, `SYS-051`, `CON-001`, `INF-001`, `TIM-003` | squad destinations and carrier defence versus no hero destination control, world-card encounter authorship and retreat banking | Near match only |
| `GAME-0025` — Lemmings | `SYS-045`, `INF-001`, `TIM-003` | individual skill assignment, population release and rescue quota versus persistent world placement around one cyclic hero | Required boundary comparison; not formal near match |
| `GAME-0026` — World of Goo | `INF-001`, `TIM-003` | live force-network construction and population extraction versus fixed-cycle encounter authorship | Required boundary comparison; not formal near match |

- New genes: `ACT-039`, `ACT-040`, `ACT-041`, `SYS-053`, `SYS-054`,
  `CON-072`, `CON-073`, `CON-074`, `OBJ-021`.
- Classification result: `New gene` and a new verified combination.
- Evidence and reasoning: random selection, earned action supply, autonomous
  locomotion / engagement, fixed positions, current visibility, hidden future
  outcomes and live scheduling reuse cleanly. The player's upstream world-card
  authority and location-sensitive expedition exit require nine bounded genes.

## Combination record

- Registered [`COMB-0028`](../../combinations/COMB-0028.md), a ten-gene proper
  subset centred on authoring increasingly dangerous encounters for one
  autonomous cyclic hero and deciding when to bank the run.
- Equipment replacement, random outcome, earned card supply, generic fixed
  capacity and both information genes remain in the full genome but are not
  required to identify that core interaction.

## Taxonomy impact

- Registry changes: nine stable genes added; eight existing genes reused.
- Taxonomy-change record: none. Player card / equipment / retreat authority,
  automatic motion / spawning / escalation, spatial / exit restrictions,
  uncertainty, resource objective and live timing fit the current six types.
- Candidate terms affected: held world-card placement, expedition equipment
  replacement, voluntary retreat, tile-authored encounter production, circuit
  escalation, placement zones, fixed cyclic traversal, retreat retention and
  expedition-resource banking are promoted.

## Negative results

- `ACT-026` and `CON-039` are absent because the player selects from a hand,
  not a mandatory supplied head.
- `SYS-022` is absent because ordinary placed generators create encounters by
  their own cadence without a one-round blockable emergence marker.
- `SYS-047` is absent because the system produces hostile encounters from world
  state rather than releasing members of one finite waiting population.
- `SYS-050` is absent because the hero traverses a fixed generated route, not a
  live player-built structure toward extraction.
- `TIM-006` is absent because placement and equipment changes occur inside the
  same live expedition, not in a separate editor before automatic execution.
- No structured negative-result record is required; no prior novelty or
  taxonomy claim was disproven.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Loop Hero moves decision authority upstream: the
  player authors future encounters while hero motion and combat remain
  autonomous (`LH-001`–`LH-005`).
- [Confirmed | Corroborated | High] Each extra circuit strengthens enemies, and
  retreat location determines how safely accumulated resources are banked
  (`LH-007`, `LH-008`, `LH-011`).

## Нові гени

- [Observation | Corroborated | High] Added nine genes; reused `SYS-004`,
  `SYS-035`, `SYS-045`, `SYS-051`, `CON-001`, `INF-001`, `INF-002` and
  `TIM-003`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0028` captures authored recurring
  danger around an autonomous escalating circuit with a voluntary banking exit.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; upstream world
  authorship remains expressible through the existing six types.

## Нові питання

- Does `SYS-053` recur where placed generators create neutral or beneficial
  encounters rather than hostile ones?
- Should a later boss-scoped Loop Hero record reuse `OBJ-020`, or does meter-
  triggered guardian defeat require a distinct objective boundary?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0029` — HUMANITY.
- Optimisation criterion: test the first plausible cross-game combination reuse
  after two mechanically independent autonomy records.
- Expected information gain: compare placed crowd commands with Lemmings role
  assignment and test population rescue without copying its per-agent grammar.
- Backlog impact: retain Tin Hearts as the closer Lemmings-like control.

## Чому саме вона

- [Hypothesis | Limited | High] HUMANITY has strong official sources and can
  determine whether the autonomous rescue motif generalises to persistent
  route commands; Tin Hearts remains available if the boundary still needs a
  closer falsification test.
