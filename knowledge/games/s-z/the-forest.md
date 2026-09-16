---
game_id: GAME-0292
slug: the-forest
game_title: The Forest
analysis_status: reviewed
reviewed: 2026-09-13
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-093
    - ACT-148
    - ACT-161
    - ACT-214
    - ACT-245
    - ACT-341
  system:
    - SYS-312
    - SYS-313
    - SYS-327
    - SYS-591
    - SYS-755
  constraint:
    - CON-210
    - CON-292
    - CON-312
    - CON-496
    - CON-621
  information:
    - INF-073
    - INF-075
    - INF-128
    - INF-131
    - INF-132
    - INF-136
  objective:
    - OBJ-171
  time:
    - TIM-003
    - TIM-007
---

# Game: The Forest

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Product labels,
resource counts, crash position, item quantities, day phase and save-slot
identity parameterise the genes but do not enter their canonical labels.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `242760`, one-app base package `28497`, default public branch Build ID
  `20229486`, published 2025-10-03; checked 2026-09-13. Endnight exposes no
  separate semantic version for this build, so none is invented.
- Product boundary: The Forest base game by Endnight Games, not Sons of the
  Forest, a console edition, soundtrack, modification or user-authored map.
- Platform, input and difficulty: English interface, Windows, keyboard and
  mouse, offline single player, fresh New Game on `Normal`; multiplayer and
  every other difficulty remain excluded.
- Entry: first ordinary control immediately after the fresh plane crash, before
  leaving the wreck and before collecting materials for a shelter.
- Primary decision loop: inspect the survivor's health, hunger, thirst, energy,
  stamina, carried stacks and current day conditions; navigate the local forest;
  take reachable ground sticks and use the Plane Axe to strike eligible bushes
  or saplings for sticks and leaves; open the Survival Guide, select the known
  Temporary Shelter, rotate and commit its outline on clear ground; repeatedly
  transfer compatible carried sticks and leaves into the visible unfinished
  requirements, revisiting nearby sources when the ten-stick base capacity
  prevents carrying all fourteen at once; receive the usable shelter when all
  requirements are filled; then commit its separate save interaction into a
  new slot while the intact shelter and current world changes remain the
  intended snapshot.
- Positive terminal: one completed intact Temporary Shelter exists at the
  chosen legal position and its manual save command has accepted a new slot.
  The survivor's inventory and survival meters, elapsed day state, harvested
  local sources and built shelter are snapshot parameters. Because no local
  application or save existed, quit/load comparison was not performed and no
  returned values are claimed as observed.
- Diagnostic negative branch: from the completed-shelter state, once sleep is
  available, choosing sleep rather than stopping at the save terminal advances
  time and restores energy but consumes the Temporary Shelter on waking. That
  branch cannot satisfy a terminal requiring the same shelter to remain. A
  subsequent load of a pre-sleep slot would restore an earlier branch, not
  prove retention of the slept future. This corrects the selection hypothesis
  in [`NEGATIVE_RESULT_004`](../../../research/negative-results/NEGATIVE_RESULT_004.md).
- Included: the fresh plane-crash start; local direct movement; the Plane Axe
  as the available starting harvesting tool; ground-stick collection;
  bush/sapling strikes and typed stick/leaf yields; finite typed inventory;
  visible survival state and running world pressure; Survival Guide building
  requirements; free outline placement, rotation and clear-footprint feedback;
  partial material contributions; outline-to-shelter completion; the distinct
  save and sleep interactions; one-use sleep collapse as a diagnostic branch;
  fixture-bound manual saving and branchable retained world history.
- Excluded: combat with cannibals or mutants; killing animals; caves, Timmy,
  story progression and endings; fires, cooking, water purification, medicine,
  armour, weapon crafting, tree felling, logs and permanent buildings; player
  defeat and cave capture; multiplayer ownership or host/client persistence;
  Peaceful, Hard, Hard Survival and Creative differences; console rules,
  modifications, achievements, screenshots, official artwork, third-party
  images, video and audio.
- Reproducible parameterisation: install Steam app `242760` from base package
  `28497`, verify public Build ID `20229486`, use English Windows keyboard and
  mouse, remain offline, and begin a fresh single-player `Normal` game. Leave
  the crash site with the Plane Axe, gather at least fourteen sticks and twenty-
  six leaves from ordinary nearby sources, and open the Survival Guide's
  shelter section. Place one Temporary Shelter outline on unobstructed land.
  Add carried materials until every displayed count is filled; because the
  initial stick capacity is ten, contribute a partial batch before collecting
  the remainder. Face the completed shelter, hold the displayed save input and
  select a new slot. Do not sleep on the positive route. Crash location,
  exact source identities, walking path, resource overage, meter values,
  weather, hostile proximity and elapsed wall-clock time remain parameters.
- Potential scoped modules: one performed save/quit/reload comparison; one
  sleep-and-collapse observation; permanent shelter, fire and weather
  protection; combat and ordinary death/capture; cave exploration; multiplayer
  persistence; or the complete story each requires a separate entry, loop,
  terminal and evidence review.
- Direct-play status: not conducted. No installed The Forest application,
  Steam manifest, local save or matching Steam userdata was found. Valve and
  Endnight establish product, package, platform, release and broad survival-
  construction boundaries. The Official The Forest Wiki and two independent
  written routes corroborate the exact Temporary Shelter materials, outline
  filling, save/sleep separation and one-use collapse. This is an evidence-
  backed reconstruction, not a claimed playthrough, entitlement or reload. No
  audiovisual source was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FOR-001` | Steam app `242760` and one-app base package `28497` identify the released Windows product developed and published by Endnight Games | Confirmed | Direct | High | P1, P2 |
| `FOR-002` | The default public branch projects Build ID `20229486`, published 2025-10-03; no publisher semantic version is exposed for it | Observation | Corroborated | Medium | P1, S1 |
| `FOR-003` | A fresh game begins after a plane crash in an open survival world whose ordinary loop includes scavenging, harvesting and shelter construction | Confirmed | Direct | High | P3, S2 |
| `FOR-004` | The Survival Guide exposes a Temporary Shelter plan that can be positioned and rotated before its materials are supplied | Observation | Corroborated | High | S2, S4 |
| `FOR-005` | The current Temporary Shelter requirement is fourteen sticks and twenty-six leaves, supplied into the unfinished outline | Observation | Corroborated | High | S2, S3, S4 |
| `FOR-006` | Ground pickup and Plane Axe strikes on eligible small vegetation produce the required sticks and leaves | Observation | Corroborated | Medium | S5, S6, S7 |
| `FOR-007` | The initial ten-stick capacity is below the fourteen-stick shelter cost, so at least one partial contribution permits the bounded route without a Stick Bag | Observation | Corroborated | High | S3, S5 |
| `FOR-008` | Health, hunger, thirst, energy, stamina, carried state and time/day conditions remain live and inspectable during collection and building | Observation | Corroborated | Medium | S8, S9, S10 |
| `FOR-009` | Completing every visible material requirement replaces the outline with a usable Temporary Shelter | Observation | Corroborated | High | S2, S4 |
| `FOR-010` | Saving and sleeping are separate shelter commands; saving can preserve the intact structure without advancing time | Observation | Corroborated | High | S2, S3, S11 |
| `FOR-011` | Sleeping when eligible advances time, restores energy and destroys the Temporary Shelter on waking; enemies may interrupt night sleep | Observation | Corroborated | High | S3, S11, S12 |
| `FOR-012` | No local executable or save was available, so accepted save and reload contents are reproducible evidence boundaries rather than executed observations | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Endnight Games, Windows release 2018-04-30; public Build ID
  `20229486` checked 2026-09-13.
- Platform or physical form: lawfully offered English Windows Steam app
  `242760`, one-app base package `28497`; fresh offline single-player `Normal`.
- Puzzle family: inventory and fixture dependencies; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-13:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=242760&cc=ua&l=english),
    for app, developer, publisher, release, Windows support, single-player and
    Steam Cloud capability.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=28497&cc=ua&l=english),
    for the one-app base package and current Ukraine offer.
  - **[P3]** [official Endnight product page](https://endnightgames.com/games/the-forest/),
    for plane-crash survival, open-world harvesting, shelter construction and
    day/night danger boundaries.
- Corroborating textual sources, accessed 2026-09-13:
  - **[S1]** [SteamCMD public-branch projection](https://api.steamcmd.net/v1/info/242760),
    for Build ID and timestamps; secondary distribution data.
  - **[S2]** [PC written route](https://gamefaqs.gamespot.com/pc/393887-the-forest/faqs/80762),
    for Survival Guide selection, outline movement/rotation, per-item supply and
    distinct completed-shelter prompts.
  - **[S3]** [Temporary Shelter reference](https://theforest.fandom.com/wiki/Temporary_Shelter),
    for current cost, save, sleep, one-use collapse, exposure and history.
  - **[S4]** [building reference](https://theforest.fandom.com/wiki/Building),
    for plan placement, resource filling, completion and shelter comparison.
  - **[S5]** [stick reference](https://theforest.fandom.com/wiki/Stick), for
    ground pickup, small-tree yield and initial ten-stick capacity.
  - **[S6]** [leaf reference](https://theforest.fandom.com/wiki/Leaf), for
    automatic leaf yield from eligible vegetation strikes.
  - **[S7]** [Plane Axe reference](https://theforest.fandom.com/wiki/Plane_Axe),
    for the starting tool and its small-tree, bush and case interactions.
  - **[S8]** [energy reference](https://theforest.fandom.com/wiki/Energy), for
    energy's relation to available stamina and sleep recovery.
  - **[S9]** [fullness reference](https://theforest.fandom.com/wiki/Fullness)
    and [hydration reference](https://theforest.fandom.com/wiki/Hydration), for
    hunger, thirst and their health consequences.
  - **[S10]** [Survival Guide reference](https://theforest.fandom.com/wiki/Survival_Guide),
    for the carried guide, construction catalogue and stats presentation.
  - **[S11]** [save reference](https://theforest.fandom.com/wiki/Save), for
    fixture-bound single-player save slots and retained position/inventory.
  - **[S12]** [sleeping reference](https://theforest.fandom.com/wiki/Sleeping),
    for eligibility, time advance, energy restoration and separate save rule.
- Research record: **[R1]** local preflight on 2026-09-13 found no installed
  application, app manifest, local save or matching Steam userdata.
- Claim IDs: `FOR-001`–`FOR-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008` owns local first-person traversal; `ACT-245` direct
  reachable ground-stick collection; `ACT-161` aimed Plane Axe strikes against
  eligible small vegetation; `ACT-148` selecting, rotating and placing the
  material-backed shelter outline; `ACT-093` each irreversible stick or leaf
  contribution; `ACT-341` the completed shelter's save interaction; and
  `ACT-214` the separate optional sleep commitment in the diagnostic branch.
- No new Action is needed after `TAXONOMY_CHANGE_069` removes first-carrier
  wording from `ACT-093`, `ACT-148` and `ACT-341` without changing their
  command boundaries. Claims: `FOR-003`–`FOR-011`.

### System Behaviour Genes

- Existing `SYS-313` owns the persistent explorable survival world; `SYS-591`
  typed harvesting yields and changed sources; `SYS-327` continuous survival-
  meter and exposure updates; `SYS-312` the outline's accumulated requirements
  and final conversion into a usable shelter; and `SYS-755` the declared sleep
  trigger that removes that shelter in the diagnostic branch.
- Resolution order: movement and reach establish an eligible source; collection
  or a compatible strike yields typed materials subject to capacity; legal
  outline placement creates persistent displayed requirements; each accepted
  contribution consumes one carried item and lowers the remaining count;
  completing all counts emits the shelter; save writes the current state; the
  sibling sleep branch advances time and destroys the one-use structure.
  Claims: `FOR-003`–`FOR-011`.

### Constraint Genes

- Existing `CON-496` owns target, reach and compatible-tool harvesting;
  `CON-210` the ten-stick carried cap and typed stacks; `CON-292` legal clear-
  footprint placement; `CON-621` the completed shelter as a designated save
  fixture; and `CON-312` eligible sleep plus possible hostile interruption.
- Scarce resources are fourteen sticks, twenty-six leaves, ten initial stick
  capacity, sufficient living-survivor state, a legal footprint, the intact
  shelter and a free save slot. Claims: `FOR-004`–`FOR-012`.

### Information Genes

- Existing `INF-073` owns visible carried stacks and active Plane Axe;
  `INF-075` current personal survival capacity; `INF-128` reachable resource
  identity and inventory fit; `INF-131` outline legality, incomplete state and
  completed fixture prompts; `INF-132` the known shelter's declared material
  dependencies; and `INF-136` current day/time and inspectable survival-guide
  state. Claims: `FOR-004`–`FOR-011`.

### Objective Genes

- New `OBJ-171` owns the bounded chain from local materials through one
  completed freely positioned survival shelter to its accepted manual save.
  An outline, an unsaved shelter or the post-sleep destroyed state is not the
  positive terminal. Claims: `FOR-004`–`FOR-012`.

### Time Genes

- Existing `TIM-003` owns the continuously advancing world and survival state
  during movement, harvesting, building and shelter interaction. Existing
  `TIM-007` owns the documented branchable manual-save history; no local reload
  was performed. Sleep's accelerated interval belongs to `ACT-214` and its
  interruption predicate, not a separate turn schedule. Claims: `FOR-008`,
  `FOR-010`–`FOR-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Reachable loose stick and free compatible capacity | Collect the stick | Item enters the carried stick stack | direct field collection is capacity-bounded | `FOR-006`, `FOR-007` |
| Eligible bush or sapling is in Plane Axe reach | Strike it | Source changes and produces stick and/or leaf yield | tool-gated harvesting is separate from pickup | `FOR-006` |
| Temporary Shelter is selected in the Survival Guide | Rotate and commit on clear land | A persistent unfinished outline with visible requirements appears | plan placement precedes material supply | `FOR-004`, `FOR-005` |
| Outline needs sticks; survivor carries ten | Repeatedly contribute sticks | Ten are consumed and four remain required | partial filling bridges the lower carried cap | `FOR-005`, `FOR-007` |
| Every stick and leaf requirement is filled | Contribute the final compatible item | Outline becomes a usable Temporary Shelter with save/sleep prompts | completion is a System settlement | `FOR-009`, `FOR-010` |
| Completed intact shelter is reachable | Hold save and accept a new slot | Current survivor and world snapshot is written without sleeping | positive fixture-bound terminal | `FOR-010`, `FOR-012` |
| Completed shelter is sleep-ready on diagnostic branch | Commit sleep | Time advances, energy is restored and the shelter collapses on waking | save and sleep cannot form one retained intact successor | `FOR-011` |
| Pre-sleep slot exists after the sleep branch | Load that earlier slot | History returns to the pre-sleep branch rather than retaining the slept future | branch restoration is not forward persistence | `FOR-010`–`FOR-012` |

## Strategic and experiential structure

- Local decision: choose reachable stick and vegetation sources, preserve
  carried room, and place the shelter on unobstructed land near enough to
  finish repeated supply trips.
- Medium-term planning: contribute the first ten sticks before gathering the
  remaining four, while monitoring health, hunger, thirst, energy, stamina and
  the running day.
- Long-term structure: one altered persistent world turns harvested local
  material into a player-positioned save fixture; later base and story play is
  deliberately outside the packet.
- Common heuristics: collect plane supplies before leaving; keep the Plane Axe
  available; strike small vegetation rather than commit to log-scale trees;
  place close to remaining sources; save before any optional sleep.
- Failure attribution: distinguish an out-of-reach source, full stick stack,
  blocked footprint, wrong material, unfinished outline, unavailable sleep and
  the irreversible one-use collapse.
- Player-trust factors: visible carried counts, guide requirements, ghost
  outline, remaining material counters, completed prompts and separate save/
  sleep icons explain each transition.
- Claim IDs: `FOR-003`–`FOR-011`.

## Replay and variation

- What changes between sessions: crash site, nearby source positions, walking
  route, incidental loot, weather, hostile proximity, survival meters, shelter
  position and save slot.
- Randomness or procedural generation: the island is persistent but the fresh
  crash selects among start locations and ordinary local encounters vary; no
  exact seed or encounter sequence is required.
- Multiple viable strategies: sticks may be taken from the ground or suitable
  small vegetation, material batches may be contributed in different orders,
  and any legal nearby shelter footprint is accepted.
- Typical replay motive: longer shelter networks, caves, combat, base building
  and the story; all require wider scopes.
- Claim IDs: `FOR-003`–`FOR-011`.

## Adjacent systems and history

- Direct predecessors: Endnight's public early-access updates progressively
  separated saving from sleeping and made Temporary Shelter sleep one-use; the
  current public build is the only admitted ruleset.
- Variants: multiplayer, other difficulties, permanent shelters and building-
  destruction settings can change ownership, pressure or persistence and are
  excluded.
- Similar games: 7 Days to Die and Don't Starve Together share live survival,
  harvesting, typed inventory and construction dependencies; Valheim shares
  free world placement and survival-building feedback; The Long Dark shares
  fatigue, sleep and visible exposure but not this construction terminal.
- Important differences: The Forest places an unfinished free-world outline,
  fills it across capacity-bounded trips, turns the completed object into the
  manual-save fixture and makes sleep consume that same temporary structure.
- Claim IDs: `FOR-003`–`FOR-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-093`, `ACT-148`, `ACT-161`, `ACT-214`, `ACT-245`, `ACT-341` | route, source, tool, outline, contribution, save and sleep |
| System Behaviour | `SYS-312`, `SYS-313`, `SYS-327`, `SYS-591`, `SYS-755` | world, survival update, yield, completion and collapse |
| Constraint | `CON-210`, `CON-292`, `CON-312`, `CON-496`, `CON-621` | stack cap, footprint, harvesting, sleep and save fixture |
| Information | `INF-073`, `INF-075`, `INF-128`, `INF-131`, `INF-132`, `INF-136` | carried state, meters, resources, plan, costs and day state |
| Objective | `OBJ-171` | completed intact shelter and accepted save |
| Time | `TIM-003`, `TIM-007` | live world and branchable history |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `291` (`GAME-0001`–`GAME-0291`).
- Exact genome matches: none.
- Tied near matches: `GAME-0280` — Resident Evil 2 (2019 remake) (`10 / 43 = 0.232558`).
- Supported combination subsets: none.
- Scan date: 2026-09-13.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0280` — Resident Evil 2 (2019 remake) | `ACT-008`, `ACT-161`, `ACT-341`, `CON-210`, `CON-621`, `INF-073`, `INF-075`, `INF-128`, `TIM-003`, `TIM-007` | Both directly traverse a live survival world, strike reachable objects, manage capacity-bounded visible inventory and personal condition, and end through a physical manual-save fixture whose retained slot permits another branch. Resident Evil 2 follows an authored police-station route with weapons, keys, healing, hostiles and a nearby-enemy predicate at a fixed typewriter. The Forest instead harvests renewable local material, freely places and incrementally fills a player-created shelter, and makes its optional sleep consume that same fixture. | Tied near, `10 / 43 = 0.232558` |

- New genes: `OBJ-171`.
- Classification result: `New gene`.
- Evidence and reasoning: earlier owners cover survival-world generation,
  harvesting, material-plan placement and completion, visible state, fixture-
  bound save and branchable history after the product-neutral generalisations
  in `TAXONOMY_CHANGE_069`. No Objective makes one player-positioned shelter
  both the bounded material target and the fixture for the retained terminal.

### Preserved research notes

- New genes: `OBJ-171`.
- Classification result: `New gene`.
- Evidence and reasoning: earlier owners cover survival-world generation,
  harvesting, material-plan placement and completion, visible state, fixture-
  bound save and branchable history after the product-neutral generalisations
  in `TAXONOMY_CHANGE_069`. No Objective makes one player-positioned shelter
  both the bounded material target and the fixture for the retained terminal.
- Evidence and reasoning: the selected packet is neither indefinite survival
  nor a long base. It closes one capacity-bounded gather/place/supply chain at
  the save accepted through the constructed object, while separately rejecting
  the impossible post-sleep intact-shelter hypothesis.

## Taxonomy impact

- Registry changes: one new Active Objective, plus product-neutral wording and
  The Forest support for `ACT-093`, `ACT-148`, `ACT-341`, `SYS-312` and
  `CON-621`; no earlier signature or lifecycle changes.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_069`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_069.md).
- Candidate terms affected: Temporary Shelter, Survival Guide, Plane Axe,
  stick, leaf, ghost outline, sleep, save, Normal, Steam app/package/build and
  input labels remain parameters rather than canonical IDs.

## Negative results

- [`NEGATIVE_RESULT_004`](../../../research/negative-results/NEGATIVE_RESULT_004.md)
  rejects the selection hypothesis that one Temporary Shelter can be slept in,
  saved and then remain in that post-sleep retained successor. The accepted
  terminal saves the intact pre-sleep world; a load was not performed.
- `ACT-338` is rejected because the shelter is not already crafted when placed;
  `ACT-204` because placement does not immediately spend one connected block;
  `CON-602` because no live save exposure interval or cooldown is evidenced;
  `CON-629` because legality follows a local fixture rather than campaign
  context; `SYS-416` because the packet does not require a time-conditioned
  spawn or despawn claim.

## Delta summary

## New facts

- [Observation | Corroborated | High] Fourteen sticks and twenty-six leaves are
  contributed to a freely positioned outline, which becomes the Temporary
  Shelter and exposes distinct save and sleep commands (`FOR-004`–`FOR-011`).
- [Confirmed | Direct | High] App `242760` and package `28497` define the
  released Windows product; no local play or reload is claimed (`FOR-001`,
  `FOR-002`, `FOR-012`).

## New genes

- [Observation | Corroborated | High] `OBJ-171` isolates one constructed
  survival shelter whose own manual-save interaction creates the retained
  terminal.

## New combinations

- [Observation | Direct | High] No new combination; no verified combination is
  a strict proper subset of the twenty-six-gene genome.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_069` generalises five
  lower-ID first-carrier wordings without changing any earlier signature.

## New questions

- Does a performed current-build save/quit/reload preserve the incomplete
  material counts of a partially supplied shelter outline?
- Does sleep interruption destroy the Temporary Shelter only after a completed
  wake, or can an interrupted sleep retain it?
- Which permanent shelter supplies the smallest independent
  weather-protection-and-save module without importing base defence?

## Next recommended game

- [Hypothesis | Limited | High] Ori and the Will of the Wisps.
- Optimisation criterion: replace first-person persistent survival construction
  with authored ability-gated traversal and a bounded boss/escape checkpoint.
- Expected information gain: test movement-ability composition, environmental
  redirection and retained traversal unlocks without carrying the survival,
  inventory or fixture-save cluster.
- Backlog impact: retain V Rising, DARK SOULS™: REMASTERED, Noita and MONSTER
  HUNTER RISE in selection-018 order.

## Why this game

- [Hypothesis | Limited | High] The Forest tests whether a freely placed,
  incrementally supplied shelter and its save function reuse established
  construction and persistence boundaries, while the one-use sleep rule
  exposes a false retained-successor assumption before the later action games.
