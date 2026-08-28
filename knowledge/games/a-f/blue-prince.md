---
game_id: GAME-0173
slug: blue-prince
game_title: Blue Prince
analysis_status: reviewed
reviewed: 2026-08-28
combination_ids:
  - COMB-0171
gene_ids:
  action:
    - ACT-008
    - ACT-087
    - ACT-089
    - ACT-130
    - ACT-131
    - ACT-299
    - ACT-300
  system:
    - SYS-523
    - SYS-524
    - SYS-525
    - SYS-526
  constraint:
    - CON-188
    - CON-403
    - CON-447
    - CON-448
  information:
    - INF-012
    - INF-180
    - INF-211
    - INF-212
    - INF-213
  objective:
    - OBJ-026
  time:
    - TIM-002
---

# Game: Blue Prince

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: Steam public build `24149240`, hotfix `1.7.2` published
  `2026-07-21`; new profile; ordinary base-game manor route from the first
  morning in the Entrance Hall through the first entry into Room 46.
- Primary decision loop: inspect the current room, map, resources and three
  room plans behind an unopened door; draft one plan that fits the vacant
  manor cell and available resources; traverse and search the instantiated
  room; collect, buy or apply useful items and evidence; continue while steps
  and routes permit, or Call it a Day and rebuild the manor next morning while
  retaining declared estate progress.
- Entry and exit: begins with a fresh profile at the Entrance Hall and the
  day's `50` steps; ends at the first successful transition into Room 46.
- Included: the `5 × 9` manor plan; three-plan room offers; common and rare
  rooms; doorway compatibility and occupied-cell rules; steps, keys, gems and
  coins; inventory items, trunks, locks, shops and ordinary room effects;
  clues and revisitable evidence; daily reset and explicitly retained estate
  state; alternative routes toward Room 46.
- Excluded: every event after first Room 46 entry, challenge modes, future
  patches, achievements, speedruns, platform-specific features, merchandise,
  exhaustive story resolution and every hidden permanent-estate puzzle as a
  separate module.
- Potential scoped modules: post-Room-46 progression; challenge modes; the
  permanent estate puzzle network; platform-specific interface differences;
  one complete clue-chain reconstruction.
- Direct-play status: not conducted. Official developer descriptions establish
  the room draft, changing daily floorplan, `50`-step morning and Room 46
  objective; official Xbox guidance establishes the ordinary resource and item
  economy; current unmodified `1.7.2` recordings were inspected only to
  corroborate the bounded map/HUD and transition sequence.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BLP-001` | Steam build `24149240` is the current public package and includes hotfix `1.7.2` | Observation | Corroborated | High | P4, S1 |
| `BLP-002` | Each unopened door presents exactly three possible rooms and one drafted room joins the current floorplan | Confirmed | Direct | High | P1, P2 |
| `BLP-003` | The manor contains 45 plan cells and the declared objective is the hidden Room 46 | Confirmed | Direct | High | P1, P2 |
| `BLP-004` | A new morning begins with 50 steps; traversing between rooms consumes steps, while room time itself is unmetered | Confirmed | Direct | High | P2 |
| `BLP-005` | Calling the day rebuilds the changing floorplan while declared permanent discoveries and upgrades can persist | Confirmed | Direct | High | P1, P2 |
| `BLP-006` | Keys open locks, gems pay room costs, coins buy shop goods and held tools enable compatible interactions | Confirmed | Direct | High | P3 |
| `BLP-007` | Room position, doorway topology, occupancy and resource costs constrain which offered plan is legal | Observation | Corroborated | High | P1, P2, S2 |
| `BLP-008` | The map, room view, offer cards and HUD expose the current route, doors, room facts and resources | Observation | Corroborated | High | P2, S2 |
| `BLP-009` | Clues are distributed across changing rooms and no single puzzle is mandatory for every route to Room 46 | Confirmed | Direct | High | P2, P3 |
| `BLP-010` | Hotfix `1.7.2` removes a first-door key-choice softlock without changing the scoped core loop | Confirmed | Direct | High | P4 |

## Basic data

- Release / origin: `2025`, Dogubomb / Raw Fury; current Steam state observed
  `2026-08-28`.
- Platform or physical form: Windows PC via Steam; single-player digital manor.
- Puzzle family: procedural room drafting, spatial route construction,
  resource-limited exploration, daily reset and retained knowledge.
- Primary sources:
  - `P1` — [official Blue Prince site](https://www.blueprincegame.com/), for the
    changing manor, room drafting and Room 46 premise; observed SHA-256
    `79c9d8d3b1ee292551dff898c3e970923328912c9b9a81821ac4a61a4c86b17c`.
  - `P2` — [developer-authored PlayStation Blog](https://blog.playstation.com/?p=403457),
    for three-room offers, the 45-room plan, 50 steps, daily rebuilding and
    clue structure; observed SHA-256
    `b2333541d70ce16b686e50aebac1d110071b7255d4f2bcc386873a7e714d09ef`.
  - `P3` — [official Xbox Wire guide](https://news.xbox.com/en-us/2025/04/07/blue-prince-game-pass-xbox/),
    for keys, gems, coins, shops, tools and alternative progression; observed
    SHA-256
    `ea5b73b7d7db7f5c52f9f184aef3bc22e8a0fc56b482d404cf653a44c46a7dd5`.
  - `P4` — [official Steam news feed](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1569580&count=200&maxlength=0&format=json),
    including hotfix `1.7.2`; observed SHA-256
    `efd70d564299a54d624b20bb42021f8bd8eee414264d135059002c1cd0dbda61`.
- Secondary sources:
  - `S1` — [Steam app-info mirror](https://api.steamcmd.net/v1/info/1569580),
    observed `2026-08-28`, build `24149240`, SHA-256
    `c238460faf8612a7d0cc77cbb1560ea40316d36f9a1d36ab24c9f321c0459523`.
  - `S2` — current unmodified `1.7.2` recordings and interface captures,
    inspected `2026-08-28`, used only for `5 × 9` plan, HUD and Room 46
    transition corroboration.
- Claim IDs: `BLP-001`–`BLP-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, traverse between connected drafted rooms;
  `ACT-087`, apply a held key or tool to a compatible fixture; `ACT-089`, take
  an addressed room item; `ACT-130`, buy one offered shop asset; `ACT-131`,
  consume one immediate-effect item.
- New genes: `ACT-299`, choose one of the three offered room plans behind the
  addressed door; `ACT-300`, Call it a Day and request a fresh manor layout.
- Parameters: current cell, chosen door, offer member, room type, cost,
  orientation, held item, fixture, shop price and day state.
- Claim IDs: `BLP-002`, `BLP-004`–`BLP-008`.

### System Behaviour Genes

- New genes: `SYS-523`, sample a position-conditioned three-room offer from the
  authored pool; `SYS-524`, instantiate the chosen room and propagate its
  doors, effects and graph edges; `SYS-525`, update day-local steps, keys,
  gems, coins and inventory; `SYS-526`, rebuild daily manor state while
  retaining only declared estate progress and knowledge.
- Resolution order: address an unopened door; filter the authored room pool by
  position and state; expose three plans; validate the chosen plan, cell,
  topology and cost; instantiate it; apply room/resource effects; permit
  traversal and interaction; settle Room 46 or the next daily reset.
- Claim IDs: `BLP-002`–`BLP-010`.

### Constraint Genes

- Existing genes: `CON-188`, one three-plan offer permits exactly one persistent
  choice for that doorway; `CON-403`, typed finite keys, gems and coins gate
  compatible interactions.
- New genes: `CON-447`, a drafted room must fit a vacant manor cell and connect
  legally through its entry doorway; `CON-448`, remaining steps gate each
  traversal between rooms.
- Scarce resources: steps, keys, gems, coins, room cells, compatible doorways,
  offer opportunities and the current day's reachable route.
- Claim IDs: `BLP-002`, `BLP-004`, `BLP-006`, `BLP-007`.

### Information Genes

- Existing genes: `INF-012`, revisitable room evidence retains its scene
  address; `INF-180`, the explored map retains the current room graph and room
  roles.
- New genes: `INF-211`, each draft card exposes room topology, type, cost and
  effect; `INF-212`, the manor HUD exposes steps, resources and held items;
  `INF-213`, the current room exposes its doors, interactables and clues.
- Claim IDs: `BLP-002`, `BLP-006`–`BLP-009`.

### Objective Genes

- Existing gene: `OBJ-026`, reach the designated traversable location, here
  the first valid entry into Room 46.
- Success and failure: Room 46 entry completes the scope; a blocked route or
  exhausted step budget ends only the current day and invites another layout.
- Claim IDs: `BLP-003`–`BLP-005`, `BLP-009`.

### Time Genes

- Existing gene: `TIM-002`, choices and traversal resolve sequentially at the
  player's pace; time spent inspecting a room does not consume steps.
- Claim IDs: `BLP-004`, `BLP-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First morning begins in the Entrance Hall | Inspect HUD and map | The manor exposes the current cell and `50` available steps | explicit daily state | `BLP-004`, `BLP-008` |
| An unopened door borders a vacant cell | Open the room draft | Three eligible plans expose their topology, type, cost and effect | bounded offer contract | `BLP-002`, `BLP-007`, `BLP-008` |
| One offered plan fits and its cost is payable | Draft that plan | The room occupies the cell, joins the graph and applies declared effects | draft-to-layout mutation | `BLP-002`, `BLP-006`, `BLP-007` |
| A connected adjacent room exists and at least one step remains | Traverse its doorway | Position changes and one step is removed | step-gated route traversal | `BLP-004` |
| A locked trunk and matching key are present | Apply the key | The typed key is consumed and the compatible fixture opens | finite typed interaction | `BLP-006` |
| The route is blocked or steps are no longer useful | Call it a Day | Daily rooms/resources reset and a new morning begins with declared retained state | loop reset boundary | `BLP-005` |
| A valid route reaches the hidden target | Enter Room 46 | The scoped objective settles at first entry | bounded terminal | `BLP-003`, `BLP-009` |

## Strategic and experiential structure

- Local decision: compare three room plans against current exits, cost,
  immediate resources and the next useful direction.
- Medium-term planning: preserve steps and scarce keys/gems, avoid sealing the
  route, create compatible door chains and sequence rooms whose effects support
  later drafts.
- Long-term structure: convert discoveries and retained estate changes into
  better future-day route choices until a valid Room 46 path emerges.
- Common heuristics: value flexible multi-exit rooms early; avoid expensive
  dead ends without a payoff; inspect clues before resetting; keep a resource
  reserve for late rare rooms; treat each offer as irreversible for that cell.
- Failure attribution: the offer is explicit, but later authored samples and
  incomplete clue knowledge can reveal that an earlier locally plausible draft
  closed the day's route.
- Player-trust factors: visible offer cards, map edges, resource counters and
  discrete step changes make the current decision state auditable.
- Claim IDs: `BLP-002`–`BLP-009`.

## Replay and variation

- What changes between sessions: sampled room offers, drafted topology, room
  effects, resource distribution, clue access and retained estate state.
- Randomness or procedural generation: the system samples from authored rooms;
  it does not freely generate arbitrary room mechanics.
- Multiple viable strategies: different room chains, resource economies and
  clue routes can reach Room 46; no single puzzle is mandatory in every run.
- Typical replay motive: use retained knowledge, improve draft sequencing and
  exploit newly exposed estate options in another daily layout.
- Claim IDs: `BLP-002`, `BLP-005`, `BLP-009`.

## Adjacent systems and history

- Direct predecessors: tabletop deck drafting, roguelite run resets and spatial
  tile-laying are mechanical lineages, not evidence for this implementation.
- Variants: challenge modes, post-Room-46 systems and platform-specific changes
  remain separate scopes.
- Similar games: Carto and The Pedestrian share direct route construction and
  designated-location travel; OneShot shares revisitable evidence and a target
  route; The Binding of Isaac: Rebirth shares generated room graphs, shops and
  finite pickups.
- Important differences: Blue Prince makes each doorway a visible exclusive
  three-plan draft, binds placement to a finite manor grid and doorway topology,
  charges steps for traversal, then resets the drafted layout while retaining
  declared cross-day progress.
- Claim IDs: `BLP-002`–`BLP-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-087`, `ACT-089`, `ACT-130`, `ACT-131`, `ACT-299`, `ACT-300` | traversal, item use, collection, purchase, consumption, draft and daily reset |
| System Behaviour | `SYS-523`–`SYS-526` | offer sampling, room instantiation, daily resources and retained reset |
| Constraint | `CON-188`, `CON-403`, `CON-447`, `CON-448` | exclusive offer, typed resources, cell/topology fit and step gate |
| Information | `INF-012`, `INF-180`, `INF-211`–`INF-213` | evidence, map, draft cards, HUD and room state |
| Objective | `OBJ-026` | first entry into Room 46 |
| Time | `TIM-002` | self-paced sequential manor decisions |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `172` (`GAME-0001`–`GAME-0172`).
- Exact genome matches: none.
- Tied near matches: `GAME-0040` — Carto (`3 / 27 = 0.111111`); `GAME-0107` — The Pedestrian (`3 / 27 = 0.111111`); `GAME-0117` — OneShot (`3 / 27 = 0.111111`); `GAME-0164` — The Binding of Isaac: Rebirth (`5 / 45 = 0.111111`).
- Supported combination subsets: `COMB-0171`.
- Scan date: 2026-08-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Carto (`GAME-0040`) | `ACT-008`, `OBJ-026`, `TIM-002` | Carto directly rearranges owned map tiles; Blue Prince makes irreversible sampled room drafts, charges traversal steps and resets the layout by day. | Near, `0.111111` |
| The Pedestrian (`GAME-0107`) | `ACT-008`, `OBJ-026`, `TIM-002` | The Pedestrian rewires fixed sign panels; Blue Prince samples authored rooms with costs, inventory, effects and retained cross-day state. | Near, `0.111111` |
| OneShot (`GAME-0117`) | `ACT-008`, `OBJ-026`, `TIM-002` | OneShot follows authored scenes and evidence; Blue Prince builds the route through three-plan drafts under cell, doorway and step constraints. | Near, `0.111111` |
| The Binding of Isaac: Rebirth (`GAME-0164`) | `ACT-008`, `ACT-130`, `ACT-131`, `CON-403`, `INF-180` | Both expose generated rooms, shops and finite pickups; Isaac resolves real-time combat, while Blue Prince explicitly drafts rooms and repeatedly rebuilds the manor. | Near, `0.111111` |

## Taxonomy impact

- Registry changes: eleven new Active definitions plus Blue Prince support for
  eleven existing genes.
- Taxonomy-change record: `CON-403` support is broadened from room pickups to
  include gems and coins as typed finite interaction/payment resources; its
  core typed-resource gate remains unchanged.
- Candidate terms affected: room plan, authored draft pool, manor cell,
  doorway topology, daily resource state and retained manor reset.

## Negative results

- The room sample is not treated as unconstrained procedural generation: plans
  come from an authored pool and obey location/state eligibility.
- Calling it a Day is not failure or save reload; it is an explicit player
  action in the ordinary progression loop.
- `TIM-016` is rejected because no automatic fixed-duration terminal advances
  the day; step depletion and player choice determine the reset.
- Post-Room-46 systems and deep permanent-estate chains do not enter this
  bounded first-entry signature.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Every addressed unopened door exposes three room
  plans, and one valid selection becomes part of the current manor graph
  (`BLP-002`, `BLP-007`).
- [Confirmed | Direct | High] A morning begins with 50 steps and the player can
  replace the drafted layout while retaining only declared estate progress
  (`BLP-004`, `BLP-005`).

## Нові гени

- [Observation/Confirmed | Direct/Corroborated | High] Eleven genes isolate
  room-plan drafting, authored offer sampling, graph instantiation, daily
  resources, retained resets, placement/step gates and visible draft/HUD/room
  state (`BLP-002`–`BLP-010`).

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0171` описує щоденне створення
  маршруту через винятковий вибір кімнат, скінченну топологію та ресурси
  (`BLP-002`–`BLP-009`).

## Нові зв'язки

- [Observation | Corroborated | High] `COMB-0171` links one-of-three room
  drafting to finite-grid topology, resource/step pressure and a player-called
  daily reset on the route to Room 46 (`BLP-002`–`BLP-009`).

## Зміни таксономії

- [Observation | Corroborated | High] Межу `CON-403` розширено підтримкою
  самоцвітів і монет Blue Prince як типізованих скінченних ресурсів; її
  визначальна умова сумісності типу та взаємодії не змінилася (`BLP-006`).

## Джерела

- [Confirmed | Direct | High] Official developer and platform publications
  define the scoped loop; the current Steam package and recordings only pin and
  corroborate the reviewed implementation (`BLP-001`–`BLP-010`).

## Що перевірено востаннє

- [Observation | Corroborated | High] On `2026-08-28`, Steam build `24149240`
  and hotfix `1.7.2` were the latest located public state (`BLP-001`,
  `BLP-010`).

## Ризики

- [Inference | Corroborated | Medium] Later patches may adjust the authored
  room pool or post-goal progression; this record therefore stops at first
  Room 46 entry and pins the public build.
