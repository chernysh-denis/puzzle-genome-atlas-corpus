---
game_id: GAME-0090
slug: the-talos-principle
game_title: The Talos Principle
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0090
gene_ids:
  action:
    - ACT-008
    - ACT-070
  system:
    - SYS-037
    - SYS-118
    - SYS-119
  constraint:
    - CON-001
    - CON-104
    - CON-105
    - CON-136
    - CON-141
  information:
    - INF-001
    - INF-040
  objective:
    - OBJ-025
    - OBJ-048
  time:
    - TIM-002
---

# Game: The Talos Principle

## Analysis scope

- Version / ruleset: original 2014 PC edition of The Talos Principle, restricted
  to the first World A1 green-sigil gate. The packet begins after the internal
  obstacle puzzles have been solved but before their three exposed green
  sigils are collected, and ends when the gate's 4 × 3 arranger is exactly
  covered and the linked passage opens.
- Included: avatar contact with the distinct green `L`, `J` and `Z`
  tetrominoes; persistent collection credit; the gate-specific requirement
  display; entry to its arranger only after all three are present; selection,
  quarter-turn orientation and placement; 4 × 3 containment; no overlap; no
  uncovered cell; immediate persistent gate opening; self-paced revision.
- Excluded: solving Only the Two of Us, A Switch Out of Reach and Outnumbered;
  jammer, mine, turret and switch rules; every later A1 puzzle; yellow, red,
  gray, star and DLC sigils; terminals, story, endings, achievements, hints,
  speedrunning, Reawakened changes and platform-specific controls.
- Direct-play status: not conducted. The official Steam record establishes the
  original product and non-linear puzzle structure. Croteam's official editor
  reference states that original Tetromino Doors require a specific collected
  set and expose a bounded arranger. The A1 record and two independent
  walkthroughs agree on three green sigils, the first gate and immediate route
  access. The local verifier formalises only that bounded transition.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TAL-001` | The Talos Principle is a first-person puzzle game developed by Croteam and released on PC on 11 December 2014 | Confirmed | Direct | High | F1 |
| `TAL-002` | Main puzzles award tetromino-shaped sigils and progression permits a non-linear choice among available puzzles | Confirmed | Corroborated | High | F1, S1 |
| `TAL-003` | Original Tetromino Doors require a specific set of collected tetrominoes; their arranger boards range from 1 × 1 through 8 × 8 | Confirmed | Direct | High | F2 |
| `TAL-004` | A1 has one sigil puzzle that must be completed to reach its exit and additional puzzles | Confirmed | Corroborated | High | S2, S3 |
| `TAL-005` | The first A1 gate uses exactly three green four-cell pieces, `L`, `J` and `Z`, on a 4 × 3 board | Confirmed | Corroborated | High | S3, S4 |
| `TAL-006` | All three shapes must be collected before arrangement; they may be rotated and placed but cannot overlap or leave the board, and success uses all twelve cells | Confirmed | Corroborated | High | F2, S3, S4 |
| `TAL-007` | A valid exact cover opens the linked passage immediately, with no overnight or other time boundary | Confirmed | Corroborated | High | S2, S3, S4 |
| `TAL-008` | The executable control proves three distinct credits, one 4 × 3 exact cover, immediate persistent access and six rejected invalid transitions | Observation | Direct | High | V1, TAL-003–TAL-007 |
| `TAL-009` | The gate is not Stardew Valley's collection family: its three indivisible shape identities become manipulable spatial pieces and must jointly tile a board | Observation | Corroborated | High | F2, S1, S3 |

## Basic data

- Release / origin: developed by Croteam, published by Devolver Digital and
  Croteam, released on 11 December 2014.
- Platform or physical form: first-person, directly navigated 3D puzzle game
  with persistent campaign collectibles and embedded 2D arrangers.
- Puzzle family: challenge-earned polyomino exact cover into persistent access.
- Primary sources:
  - **[F1]** [The Talos Principle on Steam](https://store.steampowered.com/app/257510/?l=english),
    for developer, publisher, release, first-person puzzle framing and
    non-linear route choice.
  - **[F2]** [Croteam — Reawakened Puzzle Editor device reference](https://taloseditor.croteam.com/device_reference/),
    for the original game's Tetromino Door semantics, available shapes,
    colour-specific requirements and 1 × 1 through 8 × 8 arranger boards.
- Reproducible corroboration:
  - **[S1]** [The Talos Principle Wiki — Sigil](https://taloswiki.org/wiki/Sigil),
    for four-square sigils, challenge rewards, colour roles and later arranger
    use.
  - **[S2]** [The Talos Principle Wiki — A1](https://taloswiki.org/wiki/A1),
    for the first world's puzzle list and its mandatory sigil gate.
  - **[S3]** [Walkthrough King — The Talos Principle](https://www.walkthroughking.com/text/talosprinciple.aspx),
    for the three initial green rewards, gate solution boundary and immediate
    access to the terminal, exit and temple route.
  - **[S4]** [Mystery Manor — World A1 walkthrough](https://mysterymanor.net/walkthroughs/Talos_Principle_1/World_A/World_A_1/A_1a_eng.htm),
    for the photographed 4 × 3 lock, exact `L`/`J`/`Z` roster, collection marks
    and gate-opening arranger interaction.
  - **[V1]**
    [`verify_talos_principle_control.py`](../../../scripts/verify_talos_principle_control.py),
    an executable model of distinct collection, orientation, containment,
    overlap rejection, exact cover and immediate gate access.

## Mechanical decomposition

### Player actions

- `ACT-008` — navigate controllable agent. The player walks the avatar into
  each already-exposed sigil and returns to the physical gate.
- `ACT-070` — select, orient and place finite footprint piece. In the arranger,
  the player chooses one available tetromino, rotates it by quarter turns and
  places its complete four-cell footprint at an addressed board offset.

### System behaviours

- `SYS-037` — contact-triggered collectible acquisition. Avatar contact removes
  the exposed world sigil and credits that exact identity to campaign progress.
- `SYS-118` — persistent collectible identity populates addressed arranger.
  Each credited `L`, `J` or `Z` is retained, crossed off at its source and made
  available only to the gate whose requirement roster names it.
- `SYS-119` — gapless arranger completion immediately opens persistent gate.
  After every board cell belongs to exactly one required footprint, the system
  accepts the arrangement and changes the linked barrier to open before the
  next world-navigation decision.

### Constraints

- `CON-001` — fixed occupancy capacity. The arranger contains twelve addressed
  cells in a fixed 4 × 3 rectangle.
- `CON-104` — finite all-used construction inventory. The exact three collected
  identities form the complete non-renewing piece multiset, and success uses
  each once.
- `CON-105` — complete footprint contained by placement boundary. All four
  cells of a rotated tetromino must remain inside the rectangle.
- `CON-136` — persistent prerequisite-gated mechanism dependency. Collection
  precedes arranger availability, and accepted exact cover precedes access.
- `CON-141` — gapless non-overlapping finite-footprint exact cover. No two
  pieces may own one cell and no board cell may remain uncovered at acceptance.

### Information

- `INF-001` — fully visible current state. The required roster, available
  pieces, board boundary, orientations, placements and remaining gaps are
  inspectable during each arranger decision.
- `INF-040` — visible gate-specific shape roster and arranger occupancy. Before
  entry, the lock names missing coloured identities; during arrangement it
  exposes the exact finite piece set and live addressed footprint layout.

### Objectives

- `OBJ-025` — acquire fixed puzzle-gated progress token. Each already-solved
  A1 challenge is credited by contacting its one authored green sigil.
- `OBJ-048` — unlock persistent traversal gate through collected exact cover.
  The bounded packet ends when every required collected footprint exactly
  covers the arranger and the linked A1 passage becomes traversable.

### Time

- `TIM-002` — self-paced sequential action. Collection and arranger edits have
  no forced deadline or autonomous state change between inputs.

## Reproducible transitions

The executable control begins with all three source puzzles solved but their
sigils uncredited:

1. Contact and credit the distinct green `L`, `J` and `Z` sigils.
2. Enter the addressed arranger after its exact roster is complete.
3. Place `L` along the left side of the 4 × 3 board.
4. Rotate `J` and place it across the upper-right cells.
5. Place `Z` across the remaining lower-right cells.
6. Observe all twelve cells covered exactly once and the gate opening
   immediately.

Six controls reject a foreign `T`, duplicate credit, early arranger entry,
out-of-bounds placement, footprint overlap and partial-board gate activation.
An incomplete two-piece layout is separately asserted not to open the gate.

## Strategic and experiential structure

- Challenge order is flexible, but gate membership is exact: an unrelated
  yellow or later green sigil cannot substitute for one missing A1 identity.
- Collection narrows the remaining world-search problem; the arranger then
  changes the representation from distributed challenge rewards to a fully
  visible finite spatial packing problem.
- Piece identities matter twice: first as persistent progress tokens, then as
  rigid footprints whose chirality and rotation constrain the exact cover.
- The final reward is capability rather than inventory. Success removes the
  access barrier immediately, so the player can continue without a calendar,
  turn or scripted repair boundary.

## Replay and variation

- The three source challenges may be completed in different orders.
- The arranger permits reversible trial and revision before acceptance; valid
  solutions may differ by board symmetry where the interface permits them.
- The original 2014 gate is scoped. Reawakened editor affordances, later gate
  rosters and different board dimensions are separate rulesets or instances.

## Adjacent systems and history

- inbento is the nearest prior genome because both expose a finite all-used
  footprint inventory, quarter-turn placement, a fixed container and boundary
  containment. inbento intentionally overwrites food cells to reconstruct a
  typed recipe; Talos forbids overlap and asks only for gapless coverage whose
  accepted result opens a world gate.
- Snakebird also turns exhaustive collection into access, but fruit identities
  have no reusable spatial footprints and the exit activates automatically
  when the final fruit disappears.
- Stardew Valley retains typed progress toward capability, but quantities fill
  fixed semantic slots and a nested room aggregate schedules a next-day
  service rather than launching a spatial exact-cover arranger.

## Normalised genome

| Type | IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-070` | avatar contact route; selectable quarter-turn footprint placement |
| System | `SYS-037`, `SYS-118`, `SYS-119` | contact credit; addressed arranger roster; immediate gate opening |
| Constraint | `CON-001`, `CON-104`, `CON-105`, `CON-136`, `CON-141` | 4 × 3 capacity; all three used; containment; prerequisite chain; exact cover |
| Information | `INF-001`, `INF-040` | visible state; gate roster and live occupancy |
| Objective | `OBJ-025`, `OBJ-048` | credit three challenge rewards; unlock traversal gate |
| Time | `TIM-002` | self-paced revision |

Compact signature:

`ACT-008,ACT-070; SYS-037,SYS-118,SYS-119; CON-001,CON-104,CON-105,CON-136,CON-141; INF-001,INF-040; OBJ-025,OBJ-048; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `89` (`GAME-0001`–`GAME-0089`).
- Exact genome matches: none.
- Tied near matches: `GAME-0058` — inbento (`5 / 19 = 0.263158`).
- Supported combination subsets: `COMB-0090`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0058`.

## Coverage decision

- Reuse the mature finite-footprint grammar from inbento rather than creating
  Talos-specific placement, capacity or boundary genes.
- Promote only the four boundaries that the corpus lacks: addressed arranger
  population, exact-cover-triggered access, non-overlap/gaplessness and the
  resulting world-access objective.
- Do not reuse `SYS-085`: collection alone does not activate the exit; the
  player must still solve an independently editable spatial arranger.

## Confidence and open questions

### Assumptions

- The original PC interaction semantics are scoped; the official Reawakened
  editor documentation is used only where it explicitly describes the
  original Tetromino Door.
- The photographed pieces are normalised as standard `L`, mirrored `J` and `Z`
  tetromino identities; display orientation does not change identity.

### Unknowns

- Platform-specific drag, click and controller gestures were not inspected.
- The exact save/checkpoint persistence boundary of an arrangement in progress
  was not tested; only collected identity and opened-gate persistence are used.

### Confidence

- High for roster size, piece geometry, board capacity, exact-cover predicate
  and immediate access consequence.
- Medium-high for interaction presentation because direct play was not
  conducted.

## Combination candidate

- Candidate ID: `COMB-0090`.
- Gene set: `ACT-070`, `SYS-118`, `SYS-119`, `CON-104`, `CON-141`, `INF-040`,
  `OBJ-048`, `TIM-002`.
- Supporting game: `GAME-0090`.
- Proper-subset rationale: `ACT-008`, `SYS-037`, `CON-001`, `CON-105`,
  `CON-136`, `INF-001` and `OBJ-025` support acquisition and generic spatial
  legality but do not define the gate-specific exact-cover interaction.
- Novelty claim: not assessed.

## Outcome

- Reused genes: `ACT-008`, `ACT-070`, `SYS-037`, `CON-001`, `CON-104`,
  `CON-105`, `CON-136`, `INF-001`, `OBJ-025`, `TIM-002`.
- Added genes: `SYS-118`, `SYS-119`, `CON-141`, `INF-040`, `OBJ-048`.
- Added combination: `COMB-0090`.
- Evidence gate: passed with the official product record, official device
  reference, two corpus references, two walkthrough controls and one
  executable verifier.
- Nearest prior genome: inbento; see `Corpus comparison` for the current
  result.
- Next falsification target: a collected rigid-footprint gate whose target is
  not a blank exact cover, or whose pieces remain reusable across gates.

## Taxonomy impact

- A collected progress token can later become a player-manipulated spatial
  object; collection and construction are therefore separate system stages.
- Exact coverage is separated from inbento's overwrite semantics and from
  Dominosa's fixed two-cell edge cover: footprint sizes and orientations are
  variable but each board cell still has exactly one owner.
- Immediate persistent access is separated from automatic threshold activation
  and from Stardew Valley's delayed service restoration.

## Negative results

- Jammer, mine, turret and switch behaviours belong to the excluded source
  puzzles and do not support the arranger genome.
- Three collected sigils are not a quantity stack or scalar price; their
  individual shapes and chirality remain decision-relevant.
- Merely holding all three pieces does not open the gate, falsifying exhaustive
  collection as the terminal trigger.
- The verifier establishes one valid exact cover, not solution uniqueness or
  every platform's interaction gesture.

## Delta summary

- Added one reviewed game record and one verified combination.
- Added two System Behaviour genes, one Constraint, one Information and one
  Objective gene.
- Extended ten reused genes with The Talos Principle evidence.
- Added an executable three-collection, 4 × 3 exact-cover gate control.

## Нові факти

- Перші ворота A1 вимагають три конкретні зелені тетроміно `L`, `J` і `Z`.
- Після збирання ці ідентичності стають скінченним набором фігур дошки 4 × 3.
- Усі фігури треба розмістити без виходу за межі, накладань і порожніх клітин.
- Правильне покриття одразу й назавжди відкриває прохід — без ночі чи ремонту.
- Контроль перевірив три отримання, одне exact-cover і шість відхилень.

## Нові гени

- `SYS-118` — стійка ідентичність колекційного токена наповнює адресований arranger.
- `SYS-119` — безпрогальне завершення arranger одразу відкриває постійні ворота.
- `CON-141` — точне покриття скінченними footprint-фігурами без накладань.
- `INF-040` — видимий специфічний для воріт список форм і заповнення arranger.
- `OBJ-048` — відкрити постійні ворота через exact-cover зібраних фігур.

## Нові комбінації

- `COMB-0090` — зібрані тетроміно у точне покриття для негайного доступу.

## Зміни таксономії

- Розміщення, all-used набір і межа контейнера повторно використовують граматику
  inbento; новими є non-overlap exact-cover і наслідок у світовому доступі.
- `SYS-085` не застосовано: останній токен лише дозволяє відкрити arranger, а не
  активує вихід автоматично.

## Український підсумок

Перші ворота The Talos Principle перетворюють розподілені нагороди за три
головоломки на окрему просторову задачу. Зелені `L`, `J` і `Z` не зливаються в
лічильник: їхні форми зберігаються, потрапляють у видимий arranger 4 × 3 і мають
закрити кожну клітину рівно один раз. Найближча гра — inbento, бо вона вже має
скінченні поворотні footprint-п’єси, але там накладання навмисно перезаписує
рецепт. У Talos накладання заборонено, а правильне покриття одразу відкриває
прохід; актуальний числовий результат наведено в `Corpus comparison`.

## Research log

- 2026-08-14: selected as `GAME-0090` to test immediate persistent access after
  visible collection without inventory-stack contribution or calendar delay.
- Bounded the first A1 green gate and excluded the internal jammer puzzles.
- Verified the official product framing and original Tetromino Door semantics,
  then corroborated the exact gate instance and route consequence.
- Added an executable distinct-roster and exact-cover control.
- Classified fifteen genes and confirmed `COMB-0090` as a proper subset.
- Exhaustively compared the full signature with all 89 prior genomes; inbento
  is uniquely nearest, with the current result owned by `Corpus comparison`.
