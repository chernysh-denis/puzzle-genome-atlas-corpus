---
game_id: GAME-0343
slug: the-secret-of-monkey-island
game_title: The Secret of Monkey Island
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-087
    - ACT-089
    - ACT-091
    - ACT-096
    - ACT-130
    - ACT-232
  system:
    - SYS-112
    - SYS-362
  constraint:
    - CON-136
    - CON-657
  information:
    - INF-001
    - INF-117
    - INF-365
  objective:
    - OBJ-200
  time:
    - TIM-002
---

# Game: The Secret of Monkey Island

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Guybrush,
Mêlée Island, Pieces o' Eight, the pot, shovel, treasure map, forest branches,
the fixed X and the proof T-shirt are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: the original English 1990 DOS EGA/16-colour floppy
  release, not a VGA, CD-ROM, Special Edition, console or fan-modified build.
  The exact executable was not available; the identity is reconstructed from
  Lucasfilm's history, the original manual family and ScummVM's DOS EGA
  detector boundary.
- Structured analysis target: one single-player Treasure Huntery trial on
  `PLAT-DOS`; see `GAME-0343` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: select a visible destination or a verb with one or
  two addressed nouns; collect the kitchen pot; offer it as the circus helmet
  to earn fixed currency; unlock and buy the map, buy the shovel, inspect the
  map's disguised direction sequence, follow its nine forest branches and use
  the shovel on the fixed X to acquire the trial's proof T-shirt.
- Entry: ordinary control immediately after the three pirate leaders have
  assigned all Three Trials, with Treasure Huntery incomplete, the kitchen pot
  still in its scene, no scoped trial item held and no scoped currency awarded.
- Positive terminal: the treasure-huntery T-shirt enters inventory after the
  shovel is used on the X at the final clearing. The packet stops before
  leaving that clearing or reporting any other trial.
- Negative terminal: none inside the packet. Unsupported verb-object pairs,
  an unaccepted seller response, unaffordable purchases and a wrong forest
  branch fail to advance the required chain but do not consume a life or end
  the game. Loading, restarting and rare deaths elsewhere are excluded.
- Included: point-selected walking and scene transitions; SCUMM verb/noun
  sentences; visible named scene objects and inventory; pot collection; the
  circus dialogue and pot hand-in; fixed 478-Piece payment; seller response;
  100-Piece map purchase; 75-Piece shovel purchase; persistent inventory and
  balance; map inspection; the first word of each line as nine ordered branch
  directions; the final X, shovel operation and T-shirt acquisition.
- Excluded: acquiring unrelated items; sword training, insult collection and
  Sword Master; mansion theft; all later acts; flavour dialogue except the
  map-offer response; arbitrary forest exploration; saving/loading; deaths;
  copy protection; audiovisual, timing or pathfinding implementation detail;
  VGA, CD-ROM, Amiga, Atari ST, Macintosh, FM Towns, Sega CD, Special Edition,
  modern storefront wrappers, unofficial talkie builds and fan translations.
- Reproducible parameterisation: after accepting the trials, collect the pot
  under the kitchen table; travel to the clearing and give it as the circus
  helmet; retain the 478 Pieces o' Eight; satisfy the map seller's response,
  buy the map for 100 and the shovel for 75; look at the map; at the forest
  fork take `back, left, right, left, right, back, right, left, back`; use the
  shovel on the X and stop when the T-shirt is held.
- Potential scoped modules: either other pirate trial, their combined Three
  Trials settlement, the complete act, later acts, any independently verified
  port/build, performed DOS play and save/reload behaviour require separate
  evidence, entry and terminals.
- Direct-play status: not conducted. No original disks, verified executable,
  DOS machine, DOSBox/ScummVM run, save, input trace, screenshot, video or
  audio was available or analysed. The executable control below validates only
  the sourced state graph and fixed values, not production code or route reset.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MI1-001` | Lucasfilm's 2D 16-colour adventure released in 1990; later CD-ROM and 2009 Special Edition releases are distinct | Confirmed | Direct | High | P1 |
| `MI1-002` | The original interface forms commands from one verb and one or two nouns, labels usable objects and stores acquired objects in an inventory | Confirmed | Direct | High | P2 |
| `MI1-003` | The pirate leaders assign three trials, including finding Mêlée Island's buried treasure | Confirmed | Direct | High | P1, P2 |
| `MI1-004` | The kitchen pot can be handed over as the circus helmet; the stunt awards 478 Pieces o' Eight | Observation | Corroborated | High | S1, S2 |
| `MI1-005` | The map seller's accepted response exposes a 100-Piece treasure-map offer and the store sells a shovel for 75 | Observation | Corroborated | High | S1, S2 |
| `MI1-006` | Looking at the purchased map exposes disguised dance lines whose first words encode nine forest directions | Observation | Corroborated | High | S1, S2 |
| `MI1-007` | The fixed direction sequence is back, left, right, left, right, back, right, left, back | Observation | Corroborated | High | S1, S2 |
| `MI1-008` | Using the shovel on the X at the destination grants the treasure-huntery T-shirt | Observation | Corroborated | High | S1, S2 |
| `MI1-009` | Ordinary wrong dialogue is recoverable, and the scoped trial has no sourced hard-failure terminal | Confirmed | Corroborated | High | P2, S1 |
| `MI1-010` | The local control proves 17 ordered milestones, fixed 478/100/75 economy, nine branches and eight rejected prerequisite or route violations | Observation | Direct | High | V1, MI1-004–MI1-008 |
| `MI1-011` | No verified executable or direct play was inspected | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: created and designed by Ron Gilbert with Dave Grossman and
  Tim Schafer; Lucasfilm identifies the 2D 16-colour release as 1990.
- Platform or physical form: original English DOS EGA floppy adventure,
  single-player point-selected walking with visible SCUMM verbs, sentence line
  and inventory.
- Puzzle family: knowledge and evidence progression; inventory and fixture
  dependencies; ordered dependency sequencing.
- Primary and technical sources, accessed 2026-09-21:
  - **[P1]** [Lucasfilm Games Rewind](https://www.lucasfilm.com/news/lucasfilm-games-rewind-the-secret-of-monkey-island/),
    for creators, 1990 16-colour identity, later-edition separation, Three
    Trials and the original SCUMM interaction/inventory premise.
  - **[P2]** [preserved original UK manual](https://www.mocagh.org/lucasfilm/miuk-manual.pdf),
    for the animation window, sentence-line grammar, verbs, named objects,
    inventory, point-selected walking, dialogue choices, Three Trials and the
    publisher's recoverable-mistake design statement.
  - **[P3]** [ScummVM detector source](https://doxygen.scummvm.org/de/d66/detection__internal_8h_source.html),
    for the separate English EGA DOS program family; it is a technical product-
    identity aid, not evidence of a run.
- Reproducible secondary sources, accessed 2026-09-21:
  - **[S1]** [Walkthrough Wizard — Finding the Treasure](https://walkthroughwizard.com/all-posts/adventure-games/monkey-island/the-secret-of-monkey-island-finding-the-treasure/),
    for the pot, prices, seller response, map interpretation, ordered forest
    path, X and shovel terminal.
  - **[S2]** [preserved DOS walkthrough](https://www.abandonwaredos.com/docawd.php?idg=1082&sf=secretmonkeyislandwalkthrough.txt&sg=The+Secret+of+Monkey+Island&st=walkthrough),
    independently corroborating pot, 478 payment, 100-Piece map, shovel,
    explicit nine-direction list, X and T-shirt.
  - **[V1]**
    [`verify_secret_of_monkey_island_control.py`](../../../scripts/verify_secret_of_monkey_island_control.py),
    an executable control for the bounded dependency, economy, route and proof
    acquisition.
- Research record: **[R1]** local preflight found no original or verified DOS
  program and no audiovisual or input evidence.
- Claim IDs: `MI1-001`–`MI1-011`.

## Mechanical decomposition

### Action Genes

- `ACT-096` selects reachable local and island destinations while the system
  moves Guybrush to them. `ACT-089` collects the kitchen pot. `ACT-091` gives
  it to the circus brothers as the required helmet. `ACT-232` commits the
  seller response that unlocks the map offer. `ACT-130` buys the map and
  shovel. `ACT-087` applies the shovel to the compatible fixed X.
- The SCUMM sentence line is the presentation and addressing grammar for these
  operations, not one additional generic “verb selection” gene. Claims:
  `MI1-002`, `MI1-004`–`MI1-008`.

### System Behaviour Genes

- `SYS-362` grants the bounded fixed 478-Piece payment only after the accepted
  cannon-stunt prop is supplied. `SYS-112` converts the accepted shovel-on-X
  operation into the exposed/acquired proof T-shirt.
- The cut-scene, comic impact and exact currency/item identities are
  parameters. Claims: `MI1-004`, `MI1-008`.

### Constraint Genes

- `CON-136` owns the persistent prerequisite graph: accepted trials before the
  packet, pot before the stunt, payment before purchases, map and inspection
  before clue-led routing, full route and shovel before the terminal.
- New `CON-657` requires the exact clue-encoded branch order to reach the
  concealed destination; partial or wrong sequences do not satisfy the route.
  Claim: `MI1-006`–`MI1-008`.

### Information Genes

- `INF-001` exposes the current scene, named usable objects, current inventory
  and available verbs; `INF-117` exposes retained Pieces o' Eight and current
  100/75-Piece offers before purchase.
- New `INF-365` exposes a fixed ordered route inside an inspectable carried
  clue whose surface wording must be interpreted as branch directions. It is
  not a waypoint, automatic route or external walkthrough. Claims:
  `MI1-002`, `MI1-005`–`MI1-007`.

### Objective Genes

- New `OBJ-200` completes one authored qualification trial by acquiring its
  designated proof token. Digging at the X is insufficient until the T-shirt
  enters inventory; the other two pirate trials are not required. Claim:
  `MI1-003`, `MI1-008`.

### Time Genes

- `TIM-002` owns self-paced command, dialogue, purchase, inspection and route
  progression. No scoped item, price or branch deadline advances between
  inputs. Claim: `MI1-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Accepted trials; kitchen pot present | pick up the addressed pot | pot leaves the scene and enters inventory | persistent scene-to-inventory transfer | `MI1-002`, `MI1-004` |
| Pot held; circus offer active | accept the stunt and give the pot as helmet | stunt settles and 478 Pieces o' Eight are credited | held prop gates fixed payment | `MI1-004` |
| Seller conversation active | choose the accepted barber response | 100-Piece treasure-map offer becomes available | dialogue response changes transaction state | `MI1-005` |
| Sufficient balance and each offer | buy map and shovel | 175 Pieces are spent; both identities persist in inventory | explicit economy gates later tools | `MI1-005` |
| Treasure map held | look at the map | disguised lines expose nine ordered direction words | carried clue contains the route, not a marker | `MI1-006`, `MI1-007` |
| Map read; forest fork active | take all nine encoded branches in order | the authored treasure clearing becomes reachable | branch order is a route prerequisite | `MI1-006`, `MI1-007` |
| Clearing reached; shovel held | use shovel on the fixed X | buried result resolves and the proof T-shirt enters inventory | trial terminal is an acquired proof item | `MI1-008` |

The control also rejects stunt without the pot, a duplicate stunt, map purchase
before its dialogue gate, either purchase without money, map inspection before
ownership, an incorrect seller response, digging before arrival and a wrong
first branch. It does not claim the production game's exact wrong-route reset.

## Strategic and experiential structure

- Local: infer which verb/noun or dialogue response changes state rather than
  producing flavour, and preserve the tool/economy prerequisites.
- Medium term: convert the non-obvious pot into currency, then choose purchases
  that jointly provide both information and execution capability.
- Long term: interpret a joke “dance” artefact as a route, execute its ordered
  branches and turn the reached X into retained proof of one pirate trial.
- Failure recovery: wrong inputs and branches are recoverable within this
  source-bounded packet; no finite life, deadline or consumable attempt exists.
- Player trust: named hotspots, persistent inventory/balance and fixed clue
  words must stay consistent even though the semantic mapping is comic.

## Replay and variation

- The pot, fixed payment, two prices, clue wording, branch order, destination
  and proof item are authored and deterministic.
- Walking lines, optional conversation choices and the order of buying map and
  shovel may vary. The other trials may be interleaved in a full playthrough
  but are excluded from this packet.
- No procedural map, random seller stock, route shuffle or timed forest state
  is admitted.

## Adjacent systems and history

- Day of the Tentacle shares addressed inventory pickup/hand-in, visible state,
  persistent prerequisites and self-paced interaction. Its NPC accumulates an
  exact three-item set and constructs a device; this packet instead converts
  one prop to currency, buys two tools and interprets an ordered route clue.
- Machinarium and The Longest Journey share persistent inventory-to-fixture
  dependencies, but neither bounded record couples a purchased disguised map
  to exact branch traversal and a proof-of-qualification token.
- Sea of Thieves also uses a treasure map and shovel. Its map must be matched
  against a separate ship chart, its dig point has spatial tolerance and the
  physical chest must survive a shared-world return and sale. Here one carried
  text clue states the branch sequence and one fixed X immediately settles the
  local trial proof.
- Special Edition, CD-ROM and other releases are adjacent products, not
  evidence of exact executable parity with this EGA target.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-087`, `ACT-089`, `ACT-091`, `ACT-096`, `ACT-130`, `ACT-232` | pot, seller, prices, map, shovel and X are parameters |
| System Behaviour | `SYS-112`, `SYS-362` | fixed payment and proof identity are parameters |
| Constraint | `CON-136`, `CON-657` | dependency graph and nine directions are parameters |
| Information | `INF-001`, `INF-117`, `INF-365` | SCUMM layout and clue wording are presentation/parameters |
| Objective | `OBJ-200` | Treasure Huntery and T-shirt are parameters |
| Time | `TIM-002` | self-paced; no scoped deadline |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `342` (`GAME-0001`–`GAME-0342`).
- Exact genome matches: none.
- Tied near matches: `GAME-0086` — Machinarium (`7 / 21 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0086` — Machinarium | `ACT-087`, `ACT-089`, `ACT-091`, `SYS-112`, `CON-136`, `INF-001`, `TIM-002` | Both use self-paced addressed pickup, item hand-in, compatible fixture use, visible persistent scene state and ordered prerequisites. Machinarium combines inventory parts and restores a disassembled avatar through a requested doll exchange; this trial instead converts a prop into money, buys clue/tool identities, interprets nine locomotion branches and ends at a retained qualification proof. | Near, `7 / 21 = 0.333333` |

### Preserved research notes

- New genes: `CON-657`, `INF-365`, `OBJ-200`.
- Classification result: `Three new genes`.
- Evidence and reasoning: addressed item pickup/use/give, point-selected
  navigation, transaction, dialogue response, reward settlement, fixture
  reveal, prerequisite graph, visible state/economy and self-paced action all
  transfer. No lower-ID boundary makes one carried encoded route both the
  ordered branch gate and the source of a qualification-proof terminal.

## Taxonomy impact

- Registry changes: append three Active boundaries and GAME-0343 support to
  compatible existing genes; no lifecycle, earlier signature, combination or
  family-definition change.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_085`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_085.md).
- Candidate terms affected: SCUMM, Three Trials, Treasure Huntery, Pieces o'
  Eight, pot, helmet, map, dance instructions, branch sequence, shovel, X and
  T-shirt remain product, interface or instance parameters.

## Negative results

- No verified executable or direct play was available. This record does not
  claim program checksums, pathfinding, animation timing, exact wrong-route
  reset, save-state behaviour or port parity.
- The first words of the map lines are information, not an external player
  instruction or a symbolic directional code entered without locomotion.
- The fixed X is an addressed fixture; this packet does not inherit Sea of
  Thieves' free spatial digging tolerance or shared-world custody.
- The circus payout is one authorised bounded reward, not a recurring job,
  random loot table or economy loop.

## Delta summary

## New facts

- [Observation | Corroborated | High] One pot-gated stunt deterministically
  funds the map and shovel that jointly gate Treasure Huntery (`MI1-004`,
  `MI1-005`).
- [Observation | Corroborated | High] A joke map's first words encode nine
  locomotion branches leading to a fixed X and proof T-shirt (`MI1-006`–
  `MI1-008`).

## New genes

- [Observation | Corroborated | High] `CON-657`, `INF-365` and `OBJ-200`
  isolate clue-ordered traversal and its qualification-proof terminal.

## New combinations

- [Observation | Corroborated | High] No verified combination is expected;
  deterministic subset validation remains required.

## Taxonomy changes

- [Observation | Corroborated | High] Three Active boundaries are appended
  without changing an earlier signature or lifecycle.

## New questions

- Does performed original English EGA DOS play confirm the precise wrong-path
  reset and whether the pot persists after the cannon sequence?
- Which verified EGA program revision should anchor a future direct execution?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0344` — Prince of Persia: The Sands of
  Time, the next reserved unit in `SEARCH_DEMAND_GAME_SELECTION_024`.
- Optimisation criterion: contrast self-paced item/clue dependency with live
  acrobatic route commitment and consumable rewind.
- Expected information gain: movement-chain, arena, time-resource and retained
  Dagger boundaries.
- Backlog impact: advances unit 1/9; eight reserved games remain.

## Why this game

- [Hypothesis | Limited | High] A highly recognisable adventure adds an exact
  carried-clue route and proof-trial terminal without importing its full
  campaign or insult-swording system.

## Research checklist

- [x] exact EGA target, bounded trial, entry, terminal and exclusions declared
- [x] official history, original manual and two written routes reviewed
- [x] direct-play and executable limitations disclosed
- [x] six-type signature and executable dependency control authored
- [x] Ukrainian localisation and bilingual presentation authored
- [ ] deterministic comparison and research artifacts regenerated
- [ ] artwork, repository, build, browser and accessibility gates completed

## Review outcome

- Accepted: 1990 EGA identity, SCUMM command/inventory grammar, pot-to-payment,
  two purchases, map interpretation, fixed branch sequence, X and T-shirt.
- Deferred: other trials, complete act/game, direct execution, wrong-route
  implementation, save/reload and release parity.
- Rejected: importing Special Edition presentation, treating walkthrough as
  direct play or generalising product nouns into genes.
- Taxonomy: three new boundaries; all other mechanics reuse Active genes.
- Confidence: high for the bounded sourced chain, medium for original-program
  implementation details because the executable was not inspected.
