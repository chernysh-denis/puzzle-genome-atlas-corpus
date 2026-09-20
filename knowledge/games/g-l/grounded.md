---
game_id: GAME-0314
slug: grounded
game_title: Grounded
analysis_status: reviewed
reviewed: 2026-09-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-093
    - ACT-123
    - ACT-148
    - ACT-161
    - ACT-245
    - ACT-341
  system:
    - SYS-312
    - SYS-313
    - SYS-327
    - SYS-591
    - SYS-912
  constraint:
    - CON-210
    - CON-292
    - CON-297
    - CON-496
    - CON-646
  information:
    - INF-073
    - INF-075
    - INF-128
    - INF-131
    - INF-132
    - INF-268
  objective:
    - OBJ-182
  time:
    - TIM-003
    - TIM-007
---

# Game: Grounded

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Teen, yard,
material, recipe, quest, station and save labels are parameters, not gene
names.

## Analysis scope

- Version / ruleset: current unmodified Xbox Series X|S Standard Edition base
  product under Obsidian's released `Fully Yoked` line through publisher hotfix
  `1.4.7.4815`, dated 2025-05-12 and checked 2026-09-19. No installed-console
  build identifier was available, so the semantic hotfix is a publisher ruleset
  boundary rather than a claimed observation of local Xbox binaries.
- Structured analysis target: English Xbox Series X|S Standard Edition, one
  fresh local solo Survival world on `Medium`, controller, no custom settings;
  see `GAME-0314` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: begin at the Kid Case; gather Pebblet, Plant Fiber and
  Sprig samples; spend the fresh Field Station Resource Analyzer's three
  charges on Pebblet, Plant Fiber and Clover Leaf; use the revealed hand
  recipes to make Crude Rope and a Pebblet Axe; chop Clover, place and fill one
  Lean-To; complete `Build Shelter`, assign that Lean-To as the respawn point
  for `Settling In`, then accept one manual save.
- Entry: first ordinary control after the fresh-game intro at the illuminated
  Kid Case, before any resource pickup, analysis, crafting or shelter work.
- Positive terminal: `Build Shelter` and `Settling In` are complete, one intact
  Lean-To is the assigned respawn point, and the current playthrough has
  accepted one manual save. Publisher evidence establishes retained bases,
  recipes, unlocks and inventory in saves and a ten-manual-save limit, but no
  local save was created or loaded; exact post-load values are not claimed.
- Included: first-person movement; reachable loose-resource gathering; the
  first Field Station; three finite analyzer charges; sample-to-recipe and
  Brainpower resolution; known hand crafting; the Pebblet Axe's compatible
  Clover harvest; finite carried stacks; live health, hunger, thirst and
  stamina; Lean-To placement, material counters and completion; tutorial quest
  feedback; respawn assignment; manual-save history; and real-time yard state.
- Excluded: multiplayer and Shared Worlds; cross-play; `Mild`, `Whoa!`, Custom
  and Creative differences; Playgrounds; New Game+ and the REMIX.D Yard;
  sleeping through the night; death and an executed respawn; combat, armour,
  food, water, torches and Workbench construction; laboratories beyond the
  starting Field Station; MIX.R events; faction raids; wider bases; structure
  damage; story progression, bosses and ending. The Lean-To's documented
  health and shelter role are not converted into damage mechanics without an
  observed or separately scoped attack transition.
- Reproducible parameterisation: select local solo Survival and `Medium` in a
  fresh Standard Edition world. From the Kid Case, take at least two Pebblets,
  six Sprigs and three Plant Fibers while preserving inventory capacity. At
  the first Field Station, analyze one Pebblet and one Plant Fiber; make one
  Crude Rope from three Plant Fibers, then hand-craft one Pebblet Axe from
  three Sprigs, two Pebblets and that rope. Chop eligible Clover, collect at
  least four Clover Leaves, analyze one leaf with the third initial charge,
  then retain three leaves and two Sprigs. After `Build Shelter` appears after
  17:00, place a Lean-To plan on legal flat ground, supply its three leaves and
  two Sprigs, and confirm quest completion. Interact with it, choose set
  respawn rather than sleep, confirm `Settling In`, then create a manual save.
  Exact pickup identities, walk path, incidental food/water loss, daylight,
  nearby creatures, extra resources and save-slot identity remain parameters.
- Potential scoped modules: performed save/quit/reload equality; death and
  Lean-To respawn; sleep and day advance; creature combat and structural
  damage; Workbench and base construction; multiplayer ownership; later labs,
  story, MIX.R and New Game+ each require their own entry, loop and evidence.
- Direct-play status: not conducted. No Xbox console session, entitlement,
  installed build, controller trace or Grounded save was available. Xbox and
  Obsidian establish product, solo/shared boundaries, version, new-game
  guidance and save limits; the official community wiki corroborates the
  exact analyzer, recipe, quest and Lean-To transitions. This is a
  source-bounded reconstruction, not a claimed playthrough or reload test. No
  video or audio was opened, played or analysed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GRD-001` | Xbox identifies the Series-optimised Standard Edition as a full-release product with separate solo, multiplayer and Shared Worlds use | Confirmed | Direct | High | P1 |
| `GRD-002` | Obsidian's current released line reaches hotfix `1.4.7.4815`; the exact installed Xbox binary was not observed | Confirmed | Direct | High | P2, P3 |
| `GRD-003` | A fresh game starts at the Kid Case and its first-day guidance points `Build Shelter` toward nearby Clover and Sprig after 17:00 | Confirmed | Direct | High | P4 |
| `GRD-004` | A Resource Analyzer accepts an eligible carried sample only while a charge is available; it starts with three charges and replenishes one after one in-game hour | Observation | Corroborated | High | S1 |
| `GRD-005` | Analyzing Pebblet and Plant Fiber reveals the Pebblet Axe and Crude Rope paths; analyzing Clover Leaf reveals Lean-To and related recipes | Observation | Corroborated | High | S1–S4 |
| `GRD-006` | Crude Rope costs three Plant Fibers and the hand-crafted Pebblet Axe costs three Sprigs, two Pebblets and one Crude Rope | Observation | Corroborated | High | S2, S3 |
| `GRD-007` | The Pebblet Axe can chop Clover into Clover Leaves; loose Pebblets, Plant Fibers and Sprigs are reachable local materials | Observation | Corroborated | Medium | S2–S5 |
| `GRD-008` | A Lean-To is a freely placed world construction costing three Clover Leaves and two Sprigs; merely placing its plan does not complete it | Observation | Corroborated | High | S4–S7 |
| `GRD-009` | `Build Shelter` completes when the Lean-To is built, then `Settling In` asks the player to assign it as the respawn point | Observation | Corroborated | High | S6–S8 |
| `GRD-010` | Only one bed is the assigned respawn point at a time; sleeping is a separate interaction and is unnecessary for this terminal | Observation | Corroborated | High | S7, S8 |
| `GRD-011` | Released playthroughs permit at most ten manual saves, while publisher migration notes identify bases, recipes, unlocks and inventory as retained save state | Confirmed | Direct | High | P4 |
| `GRD-012` | No console run or save/load comparison was performed, so exact saved or respawned state is not observed | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Obsidian Entertainment / Xbox Game Studios; full release
  2022-09-27; current publisher hotfix `1.4.7.4815`, 2025-05-12.
- Platform or physical form: Xbox Series X|S Standard Edition digital base
  product, English, fresh local solo Survival world on `Medium`.
- Puzzle family: inventory and fixture dependencies; ordered dependency
  sequencing; real-time system pressure.
- Primary and official sources, accessed 2026-09-19:
  - **[P1]** [Xbox Grounded product page](https://www.xbox.com/en-us/games/grounded),
    for Standard Edition identity, Series X|S optimisation, full release and
    distinct solo, multiplayer and Shared Worlds boundaries.
  - **[P2]** [Obsidian Patch 1.4.7 notes](https://grounded.obsidian.net/news/grounded/grounded-patch-147),
    for the current `Fully Yoked` release line and present platform-wide rules.
  - **[P3]** [Obsidian Hotfix 1.4.7.4815 notes](https://grounded.obsidian.net/news/grounded/grounded-patch-1471),
    for the latest publisher-labelled semantic version and date.
  - **[P4]** [Obsidian Grounded 1.0 release notes](https://grounded.obsidian.net/news/grounded/grounded-1-0-release),
    for new-game entry, first-day Lean-To guidance, retained bases/recipes/
    unlocks/inventory and the ten-manual-save limit.
  - **[P5]** [official Grounded game page](https://grounded.obsidian.net/game),
    for the solo yard, scale, survival, tools and shelter/product boundaries.
- Corroborating textual sources, accessed 2026-09-19:
  - **[S1]** [Resource Analyzer reference](https://grounded.wiki.gg/wiki/Resource_Analyzer),
    for three charges, recharge, sample analysis, Brainpower and mapped recipe
    unlocks.
  - **[S2]** [Pebblet Axe reference](https://grounded.wiki.gg/wiki/Pebblet_Axe),
    for analysis unlock, hand-crafting bill and Clover compatibility.
  - **[S3]** [Crude Rope reference](https://grounded.wiki.gg/wiki/Crude_Rope),
    for Plant Fiber analysis and hand-crafting conversion.
  - **[S4]** [Clover Leaf reference](https://grounded.wiki.gg/wiki/Clover_Leaf),
    for compatible harvesting and Lean-To recipe unlock.
  - **[S5]** [Pebblet reference](https://grounded.wiki.gg/wiki/Pebblet), for
    ground availability, analysis and recipe use.
  - **[S6]** [`Build Shelter` quest](https://grounded.wiki.gg/wiki/Build_Shelter_%28Quest%29),
    for its trigger, objective and analysis-to-construction walkthrough.
  - **[S7]** [Lean-To and beds reference](https://grounded.wiki.gg/wiki/Lean-To),
    for material bill, placement, sleep and respawn assignment.
  - **[S8]** [Grounded quest registry](https://grounded.wiki.gg/wiki/Quests_%28Grounded%29),
    for `Build Shelter`, `Settling In`, `Rock Bottom`, `Lucky Find` and their
    explicit tutorial predicates.
- Research record: **[R1]** local 2026-09-19 preflight found no Xbox session,
  installed product or save; no direct play or reload was performed.
- Claim IDs: `GRD-001`–`GRD-012`.

## Mechanical decomposition

### Action Genes

- `ACT-008` owns local traversal; `ACT-245` reachable loose-material
  collection; `ACT-161` compatible Pebblet Axe chopping; `ACT-123` the Crude
  Rope and axe hand-craft requests; `ACT-148` Lean-To plan placement;
  `ACT-093` each accepted Clover Leaf or Sprig contribution; and `ACT-341`
  Resource Analyzer use plus the later contextual Lean-To respawn assignment.
  Manual saving is a menu command represented through retained-history time,
  not falsely assigned to a world fixture. Claims: `GRD-003`–`GRD-012`.

### System Behaviour Genes

- `SYS-313` owns the retained explorable survival yard; `SYS-327` live
  personal survival reserves; `SYS-591` Clover chopping and source update;
  new `SYS-912` sample analysis into persistent recipe/Brainpower results; and
  `SYS-312` material-backed Lean-To completion.
- Resolution order: an eligible sample and available charge permit analysis;
  consuming Pebblet and Plant Fiber reveals the two personal craft paths;
  their ingredients settle immediately into rope and axe; compatible axe
  strikes yield Clover Leaves; the third analysis reveals Lean-To; legal plan
  placement creates visible counts; supplying the last compatible item emits
  the intact fixture; its assignment settles `Settling In`; manual save accepts
  the continuation. Claims: `GRD-004`–`GRD-012`.

### Constraint Genes

- `CON-210` owns finite typed carrying; `CON-297` requires known recipes,
  ingredients and output capacity for rope and axe; `CON-496` requires reach
  and a compatible chopping tool for Clover; `CON-292` requires a legal clear
  Lean-To footprint; and new `CON-646` requires an eligible unanalyzed carried
  sample and an available analyzer charge. The fresh three charges exactly
  cover Pebblet, Plant Fiber and Clover Leaf if no unrelated sample is spent;
  an accidental fourth request must wait for recharge. Claims: `GRD-004`–`GRD-008`.

### Information Genes

- `INF-073` owns carried stacks and active axe state; `INF-075` health,
  hunger, thirst and stamina; `INF-128` reachable resources and inventory fit;
  `INF-132` analyzer/crafting known status, ingredients, charge and outputs;
  `INF-131` footprint legality, plan counts and finished-fixture prompts; and
  `INF-268` the current tutorial instruction and its completion transition.
  Claims: `GRD-003`–`GRD-011`.

### Objective Genes

- New `OBJ-182` owns the complete sample-analysis-to-first-shelter chain,
  respawn assignment and accepted retained continuation. An unanalyzed leaf,
  an unfinished outline, a built Lean-To without `Settling In`, or a save made
  before those quest states is not the declared terminal. Claims:
  `GRD-004`–`GRD-012`.

### Time Genes

- `TIM-003` owns the live day, survival and yard state while the route is
  performed. `TIM-007` owns the documented manual-save history that permits a
  prior state to be restored and continued differently; exact loaded values
  remain unobserved. Claims: `GRD-003`, `GRD-004`, `GRD-011`, `GRD-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A reachable loose Pebblet, Plant Fiber or Sprig is visible and capacity remains | Gather it | the matching carried stack increases and the world source is taken | typed local collection precedes analysis and crafting | `GRD-007` |
| Field Station has a charge and carried Pebblet is eligible | Analyze Pebblet | one sample and one charge are consumed; its mapped recipes, including Pebblet Axe, become known and analysis rewards settle | sample identity determines the unlock bundle | `GRD-004`, `GRD-005` |
| Second charge and carried Plant Fiber are available | Analyze Plant Fiber | the Crude Rope recipe becomes known and another charge is consumed | recipe knowledge is not granted merely by possession | `GRD-004`, `GRD-005` |
| Three Plant Fibers are carried and Crude Rope is known | Craft one Crude Rope | ingredients are consumed and one rope enters eligible carried state | stationless personal conversion | `GRD-006` |
| Three Sprigs, two Pebblets and one rope are carried and the axe recipe is known | Craft Pebblet Axe | the ingredients convert into one usable chopping tool | recipe, bill and output capacity jointly gate crafting | `GRD-006` |
| Equipped Pebblet Axe reaches an eligible Clover | Strike it until harvested | the source changes and Clover Leaves become collectable | typed tool authority differs from loose pickup | `GRD-007` |
| Third charge and one Clover Leaf are available | Analyze Clover Leaf | the sample and final fresh charge are consumed and Lean-To becomes known | wrong earlier charge spending can impose a recharge wait | `GRD-004`, `GRD-005` |
| Lean-To is known and a legal clear position is selected | Commit its plan | a persistent outline with three-leaf and two-sprig requirements appears | plan placement is not construction completion | `GRD-008` |
| A compatible carried leaf or sprig remains | Supply it to the outline | the item is consumed and its visible remaining count decreases | partial work persists across trips | `GRD-008` |
| The final required material is supplied after `Build Shelter` is active | Allow completion | the outline becomes an intact Lean-To and `Build Shelter` completes | an authored result follows actual construction | `GRD-008`, `GRD-009` |
| `Settling In` is active and the Lean-To exists | Choose set respawn | this fixture becomes the assigned respawn point and the tutorial completes | sleeping and dying are not required | `GRD-009`, `GRD-010` |
| Both tutorial quests are complete and a manual slot is available | Create a manual save | the playthrough accepts a retained continuation state | source-backed terminal, not an observed reload | `GRD-011`, `GRD-012` |

## Strategic and experiential structure

- Local decision: choose nearby samples and preserve the three fresh analyzer
  charges for the Pebblet, Plant Fiber and Clover Leaf dependency chain.
- Medium-term planning: craft the tool before seeking all Clover Leaves, retain
  three leaves after analysis and choose a safe legal Lean-To footprint before
  night pressure increases.
- Long-term structure: the route converts discovered material identities into
  recipe knowledge, a harvesting capability, a built fixture and an assigned
  continuation anchor without entering the wider story.
- Common heuristics: gather exact bills plus small overage; read the current
  tutorial instruction; avoid spending analyzer charges on unrelated samples;
  distinguish plan placement, completion, respawn assignment and saving.
- Failure attribution: full inventory, missing recipe, depleted analyzer,
  wrong tool, blocked footprint, incomplete counts and choosing sleep instead
  of respawn are separately visible reasons the packet may stall.
- Player-trust factors: analyzer charges and results, crafting bills, harvest
  compatibility, build outline/counts and quest completion are surfaced before
  each irreversible commitment.
- Claim IDs: `GRD-003`–`GRD-012`.

## Replay and variation

- What changes between sessions: chosen teen, local pickup identities, route,
  incidental creature proximity, survival meters, time, shelter position,
  material overage and save slot.
- Randomness or procedural generation: the authored backyard persists, while
  roaming creatures and local conditions vary; the packet does not claim a
  generated world seed or fixed encounter sequence.
- Multiple viable strategies: source order and footprint differ, but the
  analysis dependency and exact material bills remain; waiting for an analyzer
  recharge can recover an unrelated early scan.
- Typical replay motive: alternate bases, combat, labs, story, multiplayer and
  New Game+ all exceed this first shelter terminal.
- Claim IDs: `GRD-003`–`GRD-012`.

## Adjacent systems and history

- Direct predecessors: The Forest and Sons Of The Forest also gather typed
  materials into freely placed shelters; Grounded inserts sample analysis and
  recipe discovery before its smaller Lean-To plan, then assigns respawn and
  saves from the playthrough rather than saving at the shelter itself.
- Variants: multiplayer, Shared Worlds, Custom parameters and later New Game+
  change ownership, persistence or difficulty and are not inferred from solo
  Medium.
- Similar games: Valheim shares survival meters, tool-gated harvesting,
  recipes and material-backed structures, but this packet's analyzer charge
  budget and tutorial respawn assignment are different boundaries.
- Important differences: the teen's small scale and giant backyard are
  presentation and parameter context; they do not become a gene without a
  measured causal rule. Lean-To durability is documented but excluded because
  no structure-damage transition belongs to this route.
- Claim IDs: `GRD-001`–`GRD-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-093`, `ACT-123`, `ACT-148`, `ACT-161`, `ACT-245`, `ACT-341` | route, sample, craft quantity, plan position and respawn choice |
| System Behaviour | `SYS-312`, `SYS-313`, `SYS-327`, `SYS-591`, `SYS-912` | yard, meters, harvest yields, analysis rewards and build completion |
| Constraint | `CON-210`, `CON-292`, `CON-297`, `CON-496`, `CON-646` | carried capacity, footprint, recipes, tool reach and analyzer charges |
| Information | `INF-073`, `INF-075`, `INF-128`, `INF-131`, `INF-132`, `INF-268` | inventory, meters, sources, plan, recipes and tutorial state |
| Objective | `OBJ-182` | analysed first shelter, respawn assignment and accepted save |
| Time | `TIM-003`, `TIM-007` | live yard and branchable manual-save history |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `313` (`GAME-0001`–`GAME-0313`).
- Exact genome matches: none.
- Tied near matches: `GAME-0292` — The Forest (`20 / 32 = 0.625000`).
- Supported combination subsets: none.
- Scan date: 2026-09-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0292` — The Forest | `ACT-008`, `ACT-093`, `ACT-148`, `ACT-161`, `ACT-245`, `ACT-341`, `SYS-312`, `SYS-313`, `SYS-327`, `SYS-591`, `CON-210`, `CON-292`, `CON-496`, `INF-073`, `INF-075`, `INF-128`, `INF-131`, `INF-132`, `TIM-003`, `TIM-007` | Both gather typed materials, harvest with a compatible tool, fill a freely placed shelter plan and retain the result in a live survival world. Grounded inserts hand crafting plus charged sample-to-recipe analysis, tutorial instruction, separate respawn assignment and a dependency-chain terminal; The Forest instead includes a survival guide, shelter-bound save gate and its distinct built-shelter terminal. | Near, `0.625000` |

### Preserved research notes

- New genes: `SYS-912`, `CON-646`, `OBJ-182`.
- Classification result: `New gene`; no verified combination is expected.
- Evidence and reasoning: existing recipe, crafting, harvesting and building
  boundaries fit their commands and results. No existing system converts a
  consumed material sample plus a finite station charge into that sample's
  recipe bundle and Brainpower result. No existing constraint jointly tests
  unanalyzed sample eligibility and the analyzer's replenishing charge. The
  terminal also differs from fixture-bound `OBJ-171`: Grounded separately
  builds the Lean-To, assigns it as respawn and saves through playthrough
  history rather than at the shelter.

## Taxonomy impact

- Registry changes: add one System Behaviour, one Constraint and one Objective
  boundary; add Grounded support to twenty-three compatible existing genes.
- Taxonomy-change record: none; no earlier definition or signature changes.
- Candidate terms affected: Grounded, Kid Case, SCA.B, Field Station, Resource
  Analyzer, Brainpower, Pebblet, Plant Fiber, Crude Rope, Pebblet Axe, Clover
  Leaf, Lean-To, `Build Shelter`, `Settling In`, Medium, Fully Yoked and all
  version/material quantities remain product or instance parameters.

## Negative results

- No installed Xbox product, controller trace, save, reload or death/respawn
  trace was available. The accepted manual save and assigned point are
  source-backed terminal states, not observed post-load equality.
- `ACT-208` is rejected because Grounded does not deploy and assign the fixture
  in one action: placement and material completion precede a separate Lean-To
  interaction. `CON-299` is rejected because this packet does not execute a
  death return or fixture cooldown. `CON-621` is rejected because Grounded's
  manual save is not gated by the Lean-To world fixture.
- Character scale, shelter health and giant-creature threat are not genes in
  this route. They require a separate measured collision, damage, defence or
  attack transition rather than descriptive comparison alone.

## Delta summary

## New facts

- [Observation | Corroborated | High] Three fresh analyzer charges can resolve
  the exact Pebblet, Plant Fiber and Clover Leaf knowledge chain needed for the
  first Lean-To (`GRD-004`–`GRD-008`).
- [Observation | Corroborated | High] Building the Lean-To and assigning it as
  respawn are two tutorial settlements before the accepted manual save
  (`GRD-008`–`GRD-012`).

## New genes

- [Observation | Corroborated | High] `SYS-912`, `CON-646` and `OBJ-182`
  isolate charged sample analysis, its legality gate and the distinct
  analysis-to-shelter-to-respawn retained terminal.

## New combinations

- [Observation | Corroborated | High] No new verified combination is asserted.

## Taxonomy changes

- [Confirmed | Direct | High] No earlier taxonomy boundary or signature
  changed.

## New questions

- Which exact inventory, quest, Lean-To, respawn and clock values return after
  a performed Xbox manual save/quit/reload comparison under `1.4.7.4815`?
- How does the Lean-To's documented health resolve under a first creature
  attack on `Medium`? That transition is outside this shelter-setup packet.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0315` — Halo 3, original Xbox 360
  campaign, solo.
- Optimisation criterion: contrast an authored shield-and-checkpoint combat
  mission with this open survival dependency chain.
- Expected information gain: determine the original release's exact first
  mission, shield recovery, finite weapon carrying and retained checkpoint
  boundaries without importing Master Chief Collection rules.
- Backlog impact: final unit of the active nine-game Goal; no later game starts
  without a new selection after its completion.

## Why this game

- [Hypothesis | Limited | Medium] Grounded adds an early recipe-discovery and
  shelter dependency chain to the Xbox side of the horizon while preserving a
  narrowly reproducible terminal and explicit source-only evidence limit.

## Research checklist

- [x] exact platform, edition, version boundary, mode and difficulty declared
- [x] primary loop, entry, positive terminal and exclusions declared
- [x] direct-play, reload and audiovisual limitations disclosed
- [x] analyzer, crafting, harvesting, building and tutorial transitions sourced
- [x] scale and shelter-damage overreach rejected
- [x] complete six-type gene scan performed
- [x] deterministic lower-ID comparison and combination scan completed
- [x] reviewed Ukrainian localisation and bilingual presentation completed
- [x] original artwork and responsive browser checks completed
