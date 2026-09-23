---
game_id: GAME-0373
slug: spore
game_title: Spore
analysis_status: reviewed
reviewed: 2026-09-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-510
    - ACT-511
  system:
    - SYS-045
    - SYS-1014
    - SYS-1015
    - SYS-1016
    - SYS-1017
    - SYS-1018
    - SYS-1019
  constraint:
    - CON-677
    - CON-678
  information:
    - INF-380
  objective:
    - OBJ-216
  time:
    - TIM-003
---

# Game: Spore

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Body size, DNA
amount, part cost, diet selection and difficulty are parameters, not extra
genes.

## Analysis scope

- Version / ruleset: original 2008 English Windows PC base-game Cell-stage
  rules documented by Electronic Arts' retail manual. The current official EA
  listing confirms product identity and distribution, but no current build,
  patch or executable was inspected. No Creepy & Cute or Galactic Adventures
  expansion rules are admitted.
- Structured analysis target: original Windows PC base-game Cell stage;
  `GAME-0373` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: steer a cell among food, other cells and part sources;
  place its mouth on compatible food to gain DNA and growth; avoid or use
  contact parts in the live water; collect a discovered part; call and reach a
  mate, then spend DNA on a legal cell-body revision; return with the revised
  capabilities and continue feeding until advancement becomes available.
- Entry and exit: start a fresh English Cell-stage game on a chosen planet at
  ordinary difficulty, select a starting herbivore or carnivore mouth as a
  recorded parameter, and accept first ordinary cell control after the
  introductory meteor sequence. A positive terminal is a filled stage
  Progress Bar, the player's chosen advance and retained first ordinary
  Creature-stage control on land. Stopping at a full bar without advancing is
  not this packet's terminal. Contact damage and death risk are included, but
  the manual does not specify a Cell-stage death/retry trace; no particular
  retry or irreversible-failure rule is asserted.
- Included: direct aquatic steering, moving peer and predator cells,
  mouth-specific feeding, DNA and growth, size-relative edible prey,
  discoverable cell parts, mating call and partner approach, Cell Creator
  placement/removal and affordability, legal geometry and complexity limit,
  saved part abilities, contact attack/defence, health/progress/part display,
  recorded Cell-stage diet path and the transfer to Creature-stage entry.
- Excluded: Creature-stage movement, socialisation, nests and creature editor
  after first land control; Tribe, Civilization and Space stages; separate
  standalone Creature Creator, Sporepedia exchange, online content, custom
  parts, expansions, cheats, exact hidden DNA thresholds, numerical collision
  damage and patch-specific balancing.
- Potential scoped modules: a named Creature-stage route, later Tribe or
  Civilization packet, standalone editor, online content or expansion rules
  each require their own version, entry, loop, terminal and evidence.
- Direct-play status: none. No installed PC game, save, controller log, video,
  audio or screenshot was inspected. This is a source-bounded reconstruction
  from EA's original instructions, not a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SPO-001` | A new game starts in Cell and the five product stages are separate. | Confirmed | Direct | High | EA manual pp. 3–5; official EA product page |
| `SPO-002` | Mouth contact with suitable food gives DNA and growth; a carnivorous cell's prey is no larger than itself. | Confirmed | Direct | High | EA manual pp. 18–19, 30–31 |
| `SPO-003` | Discovered parts become usable at a later Cell Creator visit reached by calling and approaching a mate. | Confirmed | Direct | High | EA manual pp. 18–19, 30–31 |
| `SPO-004` | DNA, part availability, legal placement and complexity constrain edits; saved functional parts change abilities or health. | Confirmed | Direct | High | EA manual pp. 12–13, 18–19 |
| `SPO-005` | A cell's contact geometry makes attacking and defensive parts consequential while other cells continue moving. | Confirmed | Direct | High | EA manual pp. 30–31 |
| `SPO-006` | The Progress Bar can be filled and then the player may advance; the Cell-stage path reaches land, with feeding history influencing successor traits. | Confirmed | Direct | High | EA manual pp. 6–8, 30–31 |
| `SPO-007` | The exact Cell-stage death/retry transition and hidden numerical coefficients are not established by this booklet. | Observation | Limited | High | bounded manual review |

## Basic data

- Release / origin: Maxis / Electronic Arts, original Spore base game, 2008.
- Platform or physical form: English Windows PC, original retail-manual Cell
  rules; current official listing is not proof of a particular installed patch.
- Puzzle family: real-time system pressure (`FAM-010`), because food sources,
  other cells and contact hazards continue to change during steering.
- Primary sources: [original EA PC manual distributed with the licensed Steam
  listing](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/17390/manuals/manual.pdf?t=1642702281),
  pp. 3–8, 12–13, 18–19 and 30–31;
  [EA product page](https://www.ea.com/games/spore/spore);
  [official Spore controls](https://www.spore.com/comm/tutorials/controls).
- Secondary sources: none needed for the accepted mechanic claims.
- Claim IDs: `SPO-001`–`SPO-007`.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: `ACT-008` for direct cell steering.
- Candidate genes: `ACT-510` for call-and-approach editor entry; `ACT-511`
  for saved part placement and removal.
- Parameters: selected food path, water direction, mate location, part,
  placement, rotation and cost.
- Claim IDs: `SPO-002`, `SPO-003`, `SPO-004`.

### System Behaviour Genes

- Existing gene IDs: `SYS-045` for independently moving cells.
- Candidate genes: `SYS-1014` food-to-DNA/growth, `SYS-1015` size-tier
  change, `SYS-1016` world-part discovery, `SYS-1017` saved body abilities,
  `SYS-1018` part contact combat and `SYS-1019` successor trait carryover.
- Resolution order: movement and peer response continue in water; eligible
  mouth contact credits food, DNA and progress; a milestone changes body size;
  a touched part marker unlocks the editor palette; a mate approach enters
  Cell Creator; a legal saved design changes the active body; a full progress
  state offers advancement and records the Cell-stage path.
- Parameters: food type and credit, cell size, part drop, ability values,
  relative contact, trait and successor state.
- Claim IDs: `SPO-002`–`SPO-006`.

### Constraint Genes

- Existing gene IDs: none.
- Candidate genes: `CON-677` mouth/size feeding restriction and `CON-678`
  part availability, DNA budget, legal placement and complexity cap.
- Scarce strategic resources: DNA available for editor parts and current
  health under contact threat. Food, part and health quantities are parameters.
- Claim IDs: `SPO-002`, `SPO-004`, `SPO-005`.

### Information Genes

- Existing gene IDs: none.
- Candidate genes: `INF-380` separates live DNA, growth, health and
  collected-part availability.
- Claim IDs: `SPO-002`–`SPO-004`, `SPO-006`.

### Objective Genes

- Existing gene IDs: none.
- Candidate genes: `OBJ-216` for stage progress, chosen advance and retained
  Creature-stage entry.
- Success, evaluation and failure: the Cell stage advances by filling its
  Progress Bar and choosing the next stage; the path taken affects the
  successor. A specific Cell-stage death/retry rule is not claimed from the
  booklet, so lethal contact is a local risk, not an invented permanent loss.
- Claim IDs: `SPO-006`, `SPO-007`.

### Time Genes

- Existing gene IDs: `TIM-003` for live world progression while steering.
- Candidate genes: none.
- Claim IDs: `SPO-002`, `SPO-005`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A cell has a herbivorous mouth and a plant fragment is reachable | Steer the mouth into the plant | Eligible contact consumes the food, increases DNA and growth progress | Food is collected by mouth, not by arbitrary body contact | `SPO-002` |
| A carnivorous cell sees another cell larger than itself | Steer toward it | The larger cell is not edible under the declared prey rule | Relative size gates carnivorous feeding | `SPO-002` |
| A marked part or meteor fragment is reachable | Swim over the part | Its type joins the collected palette for the next editor visit | Discovering a part does not immediately mount it | `SPO-003` |
| The first part has been found and the mate call is available | Call, then swim to the mate | Live Cell control yields to the Cell Creator | Editor access has a world-state and positional gate | `SPO-003` |
| A discovered part is visible in the editor and sufficient DNA remains | Place it at a valid location, then save | The cost is applied and the next active cell has the saved ability or health change | Body design alters later live decisions | `SPO-004` |
| An invalid location is highlighted red | Try to place the part there | Placement cannot be committed at that location | Part ownership does not override geometry | `SPO-004` |
| A predatory mouth or defensive spike meets another cell | Steer the functional part into contact | Contact is resolved through that part and relative position | Attack and defence are not generic whole-body collision | `SPO-005` |
| Food-driven progress fills the Cell-stage bar | Choose to advance | The saved lineage enters the next evolutionary stage on land | A full bar alone is not the declared terminal | `SPO-006` |

These transitions specify category and ordering, not unverified numerical DNA,
damage, growth or respawn values. A reproducible direct-play test would record
chosen starting diet, difficulty, edible targets, part collection and cost,
editor saves, progress milestones, advance choice and successor trait.

## Strategic and experiential structure

- Local decision: steer the mouth to edible food while avoiding dangerous
  contact, or use an equipped offensive/defensive part deliberately.
- Medium-term planning: collect a useful part, obtain enough DNA and return to
  the mate before spending it on a legal ability configuration.
- Long-term structure: repeated feeding and saved revisions drive growth and
  eventually a chosen stage transition; the feeding history matters later.
- Common heuristics: an initially herbivorous route can favour reachable
  plants, while a carnivorous route must compare prey size and danger. These
  are possible strategies, not a claim of optimal play.
- Failure attribution: contact part, cell size, current health, food
  eligibility and the growth bar are inspectable; exact lethal/retry behaviour
  remains untested.
- Player-trust factors: the editor exposes part availability, cost,
  complexity and invalid red placement before saving a revision.
- Claim IDs: `SPO-002`–`SPO-007`.

## Replay and variation

- What changes between sessions: starting diet choice, chosen parts, edited
  body and encountered food and cells.
- Randomness or procedural generation: this packet does not infer a seed or
  quantified distribution for cell encounters from the manual.
- Multiple viable strategies: the manual documents herbivore, carnivore and
  omnivore diets; exact relative difficulty is not established here.
- Typical replay motive: alter diet path and cell-part build before landfall.
- Claim IDs: `SPO-002`–`SPO-006`.

## Adjacent systems and history

- Direct predecessors: no genealogy claim is required for this packet.
- Variants: later Spore stages, optional packs and standalone creator are
  separate scope candidates.
- Similar games: full-corpus signature comparison is owned below.
- Important differences: this packet's editor is reached from an active cell
  through mate approach; it is not a detached character-customisation menu.
- Claim IDs: `SPO-001`, `SPO-003`, `SPO-004`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-510`, `ACT-511` | Mouth steering, mate, chosen part and body geometry |
| System Behaviour | `SYS-045`, `SYS-1014`, `SYS-1015`, `SYS-1016`, `SYS-1017`, `SYS-1018`, `SYS-1019` | Food credit, growth, unlock, saved ability, contact and history |
| Constraint | `CON-677`, `CON-678` | Mouth, prey size, DNA, availability and complexity |
| Information | `INF-380` | Live progress, DNA, health and parts |
| Objective | `OBJ-216` | Cell-to-Creature advance |
| Time | `TIM-003` | Live aquatic progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `372` (`GAME-0001`–`GAME-0372`).
- Exact genome matches: none.
- Tied near matches: `GAME-0029` — HUMANITY (`3 / 24 = 0.125000`).
- Supported combination subsets: none.
- Scan date: 2026-09-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0029` HUMANITY | `ACT-008`, `SYS-045`, `TIM-003` | Both have direct movement amid autonomous actors on a live clock. HUMANITY places persistent route commands for a recurrent human stream and fills a rescue goal; Spore feeds and edits one growing lineage before a stage succession, with no command field or rescue quota. | Tied near, score 0.125000 |

## Taxonomy impact

- Registry changes: twelve new Active genes across five types; no existing
  definition or earlier game signature changes.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_112`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_112.md).
- Candidate terms affected: none accepted from an unsourced lead.

## Negative results

- none. No prior accepted claim or candidate is being rejected.

## Delta summary

The headings below are the compact canonical delta ledger. Keep this source
record in English; reviewed Ukrainian research views are generated from the
separate localisation layer.

## New facts

- [Confirmed | Direct | High] A fresh Cell-stage lineage feeds and grows,
  collects parts, can revise its body through mate access and may advance to
  Creature after its stage bar fills (`SPO-002`–`SPO-006`).

## New genes

- [Observation | Direct | High] Twelve bounded cell-feeding, body-editor,
  contact and transition genes (`TAXONOMY_CHANGE_112`).

## New combinations

- [Observation | Direct | High] No new combinations; no previously verified
  combination is a proper subset of this signature.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_112` admits twelve new IDs
  without changing earlier signatures.

## New questions

- A future direct-play trace could test the Cell-stage defeat/retry state,
  exact food credits and patch-specific balance without silently inserting
  those claims into this source-bounded packet.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0374` Burnout Paradise, reserved in
  [`SEARCH_DEMAND_GAME_SELECTION_027`](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_027.md).
- Optimisation criterion: alternate the Cell-stage growth/editor loop with
  open-city vehicle routing and collision decisions.
- Expected information gain: distinguish freely selected race routes and
  crash resolution from direct aquatic feeding and lineage revision.
- Backlog impact: this is the next reserved unit, not an implied start here.

## Why this game

- [Hypothesis | Limited | Medium] A Cell-to-Creature Spore packet offers a
  recognisable, visually different primary loop with a clearly bounded
  evolutionary transition. The manual supports its rule claims but no direct
  play or cross-product novelty proof is asserted.
