---
game_id: GAME-0059
slug: kami
game_title: KAMI
analysis_status: reviewed
reviewed: 2026-08-13
combination_ids:
  - COMB-0059
gene_ids:
  action:
    - ACT-071
  system:
    - SYS-102
  constraint:
    - CON-001
  information:
    - INF-001
  objective:
    - OBJ-037
    - OBJ-038
  time:
    - TIM-001
---

# Game: KAMI

## Analysis scope

- Version / ruleset: State of Play's original KAMI, restricted to the complete
  nine-puzzle first Classic set, `A1`-`A9`.
- Included: one fixed rectangular paper-cell field; its complete visible colour
  assignment; the visible level palette; selection of one replacement colour
  and one differently coloured addressed cell; maximal orthogonally connected
  same-colour-region recolouring; immediate coalescence with every adjacent
  region of the replacement colour; completion when the whole field has one
  colour; displayed move accounting, authored Perfect target, restart and
  consequence-free self-paced retries.
- Excluded: Classic sets B-E; every Extra / Premium colour or pattern set;
  purchasable and daily hint accounting; unlock progression; KAMI 2, its
  triangular geometry, Journey, Daily Challenge and level builder;
  achievements, speedrunning, sound, paper animation and presentation.
- Direct-play status: not conducted. The developer's product page fixes the
  one-colour and fewest-moves objectives. The preserved official description
  defines palette selection, orthogonal same-colour propagation and move
  ratings. Three contemporary hands-on reviews independently establish the
  selected-region effect, automatic enlargement, no timer, Perfect evaluation,
  restart and the nine-puzzle first-set boundary.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `KAM-001` | The first complete Classic set contains nine authored puzzles and precedes the later Classic and Premium sets | Confirmed | Corroborated | High | P2, S2, S4 |
| `KAM-002` | Every scoped puzzle exposes the complete fixed paper-cell field and its available replacement colours | Confirmed | Direct | High | P2, S1-S3 |
| `KAM-003` | One move chooses a palette colour and an addressed field cell of another current colour | Confirmed | Direct | High | P2, S1-S3 |
| `KAM-004` | The chosen cell and every orthogonally connected cell in its maximal current-colour region change together | Confirmed | Direct | High | P2, S1, S3 |
| `KAM-005` | Recolouring automatically coalesces the changed region with all adjacent regions already carrying the replacement colour | Confirmed | Corroborated | High | P2, S1-S3 |
| `KAM-006` | Functional completion requires the entire field to become one colour; the surviving colour is player-chosen | Confirmed | Direct | High | P1, P2, S1-S3 |
| `KAM-007` | Each recolour consumes one counted move, while matching the authored move target earns Perfect as a separate optimisation result | Confirmed | Corroborated | High | P1, P2, S1-S3 |
| `KAM-008` | Exceeding the Perfect target does not create a time-driven loss; a non-Perfect completion remains separately rated | Confirmed | Corroborated | High | P2, S1-S3 |
| `KAM-009` | Restart restores the authored field and retries have no persistent mechanical cost | Confirmed | Corroborated | High | S1, S2 |
| `KAM-010` | Scoped state transitions are deterministic and no random event or forced clock changes the field | Observation | Corroborated | High | P1, P2, S1-S3 |

## Basic data

- Release / origin: State of Play Games developed and published the original
  KAMI, first released on iOS on 9 October 2013 and subsequently on Android,
  Windows, macOS and Nintendo 3DS.
- Platform or physical form: deterministic single-player digital region-
  recolouring puzzle represented as a fixed field of paper cells.
- Puzzle family: connected-region contraction to a monochromatic field.
- Primary and official sources:
  - **[P1]** [State of Play - KAMI](https://www.stateofplaygames.com/kami),
    for the original game's developer boundary, whole-screen colour objective
    and fewest-moves optimisation.
  - **[P2]** [Preserved official KAMI description](https://www.mobygames.com/game/66652/kami/),
    for fixed coloured or patterned cells, the visible palette, orthogonal
    same-colour propagation, counted moves, Perfect / Good / Failed ratings,
    gradual unlocking and five basic sets of nine.
- Contemporary hands-on corroboration:
  - **[S1]** Harry Slater,
    [KAMI Review](https://www.pocketgamer.com/kami/review/), for three- or
    four-colour palettes, region-wide recolouring, arbitrary final colour,
    Perfect solutions, self-paced play and lack of time pressure.
  - **[S2]** Yishian Yao,
    [KAMI review](https://www.macworld.com/article/222257/kami-review-origami-puzzle-game-soothes-the-ios-gamer.html),
    for uniform-field completion, cascading region fill, passing versus
    Perfect results, consequence-free restart and nine-puzzle grouping.
  - **[S3]** [Nintendo Life KAMI review](https://www.nintendolife.com/reviews/3ds-eshop/kami),
    for palette selection, region expansion into matching neighbours, five
    Classic groups of nine and fewest-moves replay.
  - **[S4]** [The Smiling Dutchman KAMI review](https://www.thesmilingdutchman.com/in-the-loop/2013/12/31/kami-review),
    for the first nine-puzzle trial boundary and no-timer play.
- Claim IDs: `KAM-001`-`KAM-010`.

## Mechanical decomposition

### Action Genes

- `ACT-071` - select a region seed and replacement class. The player chooses
  one colour from the displayed palette, then addresses a field cell whose
  current colour differs from that selection. The cell identifies its complete
  current connected component rather than one independent assignment.
- Parameters: palette size, colour / pattern identity, input order, seed-cell
  geometry and same-colour no-op handling.
- Claim IDs: `KAM-002`, `KAM-003`.

### System Behaviour Genes

- `SYS-102` - component-wide recolour and equal-class coalescence. The system
  finds the seed's maximal orthogonally connected current-colour component,
  changes every member to the selected class, then treats it and all adjacent
  components of that class as one component for subsequent moves.
- Resolution order: identify the pre-action component; replace its class as one
  atomic logical effect; coalesce new equal-class boundaries; increment the
  move count; test whole-field uniformity and the Perfect threshold.
- Parameters: neighbourhood topology, component maximality, replacement
  atomicity, merge transitivity and animation duration.
- Claim IDs: `KAM-004`, `KAM-005`, `KAM-007`, `KAM-010`.

### Constraint Genes

- `CON-001` - fixed occupancy capacity. Every scoped puzzle preserves one
  finite authored lattice of separately addressed paper cells; recolouring
  changes cell classes and region boundaries without adding or removing cells.
- `CON-020` is absent. The authored move number is an optimisation threshold,
  not a consumable allowance whose exhaustion terminates the attempt.
- Scarce strategic resource: the number of component-changing recolours needed
  to eliminate all boundaries, not a terminal inventory.
- Claim IDs: `KAM-002`, `KAM-007`, `KAM-008`.

### Information Genes

- `INF-001` - fully visible current state. The complete current cell colouring,
  every region boundary, the replacement palette and move accounting are
  available before a choice; there is no hidden or random board content.
- Claim IDs: `KAM-002`, `KAM-007`, `KAM-010`.

### Objective Genes

- `OBJ-037` - make a fixed field monochromatic. Functional success occurs when
  every field cell carries one common player-selected colour, independent of
  which available colour survives.
- `OBJ-038` - match an authored optimal action count. Perfect is an additional
  solution-quality objective earned by completing within the displayed target
  number of recolours; a completed but longer solution remains mechanically
  distinct from failure to make the field uniform.
- Claim IDs: `KAM-006`-`KAM-008`.

### Time Genes

- `TIM-001` - discrete turn with automatic resolution. One palette-and-seed
  commitment fully recolours the component, merges its new same-colour
  neighbours, increments the counter and evaluates completion before another
  decision is accepted.
- The absence of a forced clock is a parameter; visual paper folding does not
  create real-time strategy.
- Claim IDs: `KAM-003`-`KAM-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| One red region consists of several orthogonally connected red cells | Select blue and address any cell in that red region | Every red cell in that maximal component becomes blue together | A cell is a seed for region-wide recolouring, not a single-cell assignment | `KAM-003`, `KAM-004` |
| Two blue regions touch opposite sides of one red region | Recolour the red region blue | All three former regions become one larger blue component | Replacement also changes future component topology | `KAM-005` |
| Two red areas meet only at a corner | Recolour one of them blue | The other diagonal red area is unaffected | Connectivity is orthogonal, not diagonal | `KAM-004` |
| More than one colour remains after the displayed Perfect count | Continue with another legal recolour | The puzzle remains playable, but the Perfect result is no longer met on that attempt | Perfect is optimisation rather than terminal exhaustion | `KAM-007`, `KAM-008` |
| Every cell belongs to one blue component | Resolve the last recolour | The level completes; rating depends on the counted moves | Uniformity and efficiency are separate objectives | `KAM-006`, `KAM-007` |
| A poor early recolour enlarged the wrong component | Activate restart | The original authored colouring and move count return | Recovery is deterministic and consequence-free | `KAM-009` |

## Strategic and experiential structure

- Local decision: choose which current component changes class and which
  adjacent components it will absorb immediately.
- Medium-term planning: build one growing component that can encounter several
  regions of the next selected colour in a single later move.
- Long-term structure: contract the current region-adjacency graph to one node
  while minimising the recolour sequence, not merely eliminate colour names.
- Common heuristics: reason over connected components rather than individual
  cells; favour a seed touching several components of one colour; preserve a
  colour as an intermediate bridge when it can merge separated regions; avoid
  spending a move on a component that absorbs nothing.
- Failure attribution: every non-Perfect result follows from a visible choice
  of component and colour; no refill, opponent or concealed state intervenes.
- Player-trust factors: region boundaries, selected palette class, counted move
  and complete post-fold result must remain legible despite the paper animation.
- Claim IDs: `KAM-002`-`KAM-010`.

## Replay and variation

- What changes between scoped puzzles: authored cell colouring, connected-
  component graph, palette size and Perfect move target.
- Randomness or procedural generation: none in the nine scoped puzzles.
- Multiple viable strategies: the final colour and move sequence can differ;
  some layouts admit more than one Perfect solution.
- Typical replay motive: improve a completed Good / Failed-rated route to the
  authored Perfect move count or test another surviving colour.
- Claim IDs: `KAM-001`, `KAM-006`-`KAM-010`.

## Adjacent systems and history

- Direct successor: KAMI 2 retains connected-region recolouring but changes the
  geometry, campaign and surrounding modes; it requires its own record.
- Similar games: Flood-It and flood-fill graph contraction, though KAMI permits
  selecting any current region rather than only expanding one fixed origin.
- Important difference from match removal: changing a region never deletes its
  cells or collapses the board. Important difference from inbento: the action
  rewrites one current connected component by class, not a chosen geometric
  footprint whose covered cells are independent of their current classes.
- Premium patterned puzzles remain excluded because pattern identity and their
  later release boundary would broaden the selected first-set claim.
- Claim IDs: `KAM-001`-`KAM-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-071` | replacement class and seed cell |
| System Behaviour | `SYS-102` | maximal component recolour and transitive coalescence |
| Constraint | `CON-001` | field size and cell topology |
| Information | `INF-001` | complete colouring, palette and move accounting |
| Objective | `OBJ-037`, `OBJ-038` | uniform final class and Perfect threshold |
| Time | `TIM-001` | complete post-selection folding resolution |

Canonical signature:

`ACT-071; SYS-102; CON-001; INF-001; OBJ-037,OBJ-038; TIM-001`

## Corpus comparison

- Indexed games scanned: every prior record `GAME-0001`-`GAME-0058`.
- Exact genome matches: none.
- Existing combination subsets: none. Every verified `COMB-0001`-`COMB-0058`
  gene set was tested as a proper subset and rejected.
- Unique near match: `GAME-0057` - Golf Peaks at intersection `3`, union `12`,
  `3 / 12 = 0.250000`. Water Sort, Can of Wormholes and inbento tie next at
  `3 / 13 = 0.230769`.
- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `3 / 18 = 0.166667`; `GAME-0002`: `2 / 12 = 0.166667`;
    `GAME-0003`: `2 / 14 = 0.142857`; `GAME-0004`: `2 / 20 = 0.100000`;
    `GAME-0005`: `2 / 12 = 0.166667`; `GAME-0006`: `2 / 14 = 0.142857`;
    `GAME-0007`: `1 / 14 = 0.071429`; `GAME-0008`: `2 / 12 = 0.166667`;
    `GAME-0009`: `3 / 20 = 0.150000`; `GAME-0010`: `3 / 13 = 0.230769`.
  - `GAME-0011`: `2 / 18 = 0.111111`; `GAME-0012`: `2 / 14 = 0.142857`;
    `GAME-0013`: `3 / 17 = 0.176471`; `GAME-0014`: `2 / 20 = 0.100000`;
    `GAME-0015`: `3 / 18 = 0.166667`; `GAME-0016`: `2 / 20 = 0.100000`;
    `GAME-0017`: `1 / 19 = 0.052632`; `GAME-0018`: `1 / 25 = 0.040000`;
    `GAME-0019`: `3 / 14 = 0.214286`; `GAME-0020`: `2 / 19 = 0.105263`.
  - `GAME-0021`: `1 / 15 = 0.066667`; `GAME-0022`: `1 / 18 = 0.055556`;
    `GAME-0023`: `0 / 17 = 0.000000`; `GAME-0024`: `1 / 18 = 0.055556`;
    `GAME-0025`: `1 / 17 = 0.058824`; `GAME-0026`: `1 / 18 = 0.055556`;
    `GAME-0027`: `2 / 17 = 0.117647`; `GAME-0028`: `2 / 22 = 0.090909`;
    `GAME-0029`: `2 / 17 = 0.117647`; `GAME-0030`: `1 / 20 = 0.050000`.
  - `GAME-0031`: `1 / 17 = 0.058824`; `GAME-0032`: `2 / 16 = 0.125000`;
    `GAME-0033`: `1 / 19 = 0.052632`; `GAME-0034`: `1 / 20 = 0.050000`;
    `GAME-0035`: `1 / 24 = 0.041667`; `GAME-0036`: `1 / 18 = 0.055556`;
    `GAME-0037`: `2 / 14 = 0.142857`; `GAME-0038`: `1 / 22 = 0.045455`;
    `GAME-0039`: `2 / 14 = 0.142857`; `GAME-0040`: `1 / 14 = 0.071429`.
  - `GAME-0041`: `1 / 17 = 0.058824`; `GAME-0042`: `1 / 15 = 0.066667`;
    `GAME-0043`: `3 / 18 = 0.166667`; `GAME-0044`: `3 / 14 = 0.214286`;
    `GAME-0045`: `3 / 18 = 0.166667`; `GAME-0046`: `1 / 16 = 0.062500`;
    `GAME-0047`: `2 / 19 = 0.105263`; `GAME-0048`: `2 / 19 = 0.105263`;
    `GAME-0049`: `2 / 14 = 0.142857`; `GAME-0050`: `3 / 19 = 0.157895`.
  - `GAME-0051`: `1 / 22 = 0.045455`; `GAME-0052`: `1 / 16 = 0.062500`;
    `GAME-0053`: `3 / 13 = 0.230769`; `GAME-0054`: `3 / 15 = 0.200000`;
    `GAME-0055`: `3 / 14 = 0.214286`; `GAME-0056`: `2 / 13 = 0.153846`;
    `GAME-0057`: `3 / 12 = 0.250000`; `GAME-0058`: `3 / 13 = 0.230769`.
- Scan date: 2026-08-13.
- New genes: `ACT-071`, `SYS-102`, `OBJ-037`, `OBJ-038`.
- Reused genes: `CON-001`, `INF-001`, `TIM-001`.
- Classification result: four `New gene` records and one new verified
  interaction; no novelty claim.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0057` - Golf Peaks | `CON-001`, `INF-001`, `TIM-001` | finite cards route one ball through height geometry versus repeatable region-class rewrite and graph contraction | Unique top near match, `0.250000` |
| `GAME-0010` - Water Sort | `CON-001`, `INF-001`, `TIM-001` | maximal liquid transfer into bounded stacks versus component-wide colour replacement on a fixed field | Tied next match, `0.230769` |
| `GAME-0053` - Can of Wormholes | `CON-001`, `INF-001`, `TIM-001` | ordered-body reshaping into one trace versus region-graph contraction into one class | Tied next match, `0.230769` |
| `GAME-0058` - inbento | `CON-001`, `INF-001`, `TIM-001` | finite footprint overwrite toward an exact recipe versus renewable component recolours toward any uniform class | Tied next match, `0.230769` |

## Combination record

- `COMB-0059` captures player-seeded connected-component recolouring whose
  automatic same-class coalescence contracts a visible region graph until one
  class remains.
- Exhaustive supporter scan: only `GAME-0059` contains the complete proper
  subset; no previous verified combination is a subset of this genome.

## Taxonomy impact

- Added direct class-and-seed selection separately from the automatic maximal-
  component propagation it triggers.
- Added uniform-field completion and one-metric authored optimum separately:
  neither exact target reconstruction nor the multi-metric machine objective
  states whether the final class is free or one action threshold is Perfect.
- No prior signature changes and no taxonomy-change record.
- Candidate terms affected: promote connected-component class replacement,
  equal-class component coalescence, player-chosen monochromatic completion and
  authored optimal action-count matching.

## Negative results

- `SYS-101` rejected: KAMI selects a maximal current component by class and
  rewrites all its cells, not an independently shaped incoming footprint.
- `ACT-013` rejected: the action changes a current region's class; it does not
  remove a contiguous group or cause gravity and refill.
- `CON-020` rejected: exceeding the Perfect count changes evaluation but does
  not terminate forward play at zero remaining moves.
- `OBJ-004` rejected: no exact target arrangement or mandatory final colour is
  declared; every cell merely needs one shared surviving class.
- `OBJ-016` rejected: KAMI optimises one move count, not two or more independent
  persistent machine-resource metrics.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Усі дев’ять задач Classic A використовують
  одну граматику: перефарбування максимальної зв’язної області, злиття з
  сусідніми областями нового кольору та приведення всього поля до одного
  довільно вибраного кольору (`KAM-001`-`KAM-010`).

## Нові гени

- [Observation | Direct | High] `ACT-071` - вибір початкової клітинки області
  та нового класу.
- [Observation | Direct | High] `SYS-102` - перефарбування всього компонента й
  злиття суміжних компонентів однакового класу.
- [Observation | Direct | High] `OBJ-037` - зробити фіксоване поле одноколірним.
- [Observation | Corroborated | High] `OBJ-038` - вкластися в авторську
  оптимальну кількість дій.

## Нові комбінації

- [Confirmed | Direct | High] `COMB-0059` - скорочення графа областей
  перефарбуванням і автоматичним злиттям.

## Зміни таксономії

- Немає. Додано чотири операційно відмінні межі без зміни попередніх записів.

## Нові питання

- Чи повторюється `SYS-102` у грі з неколірними класами, де одна дія також
  змінює весь поточний компонент і перебудовує граф суміжності?
- Чи потребуватиме `OBJ-038` розділення, якщо майбутня гра вимагає не рівності
  авторському порогу, а довільного глобального мінімуму без показаної норми?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] HOOK.
- Optimisation criterion: maximise distance from region recolouring by testing
  dependency-ordered retraction of linked line mechanisms.
- Expected information gain: distinguish direct switch activation, propagation
  along a visible wire and obstruction-clearing order from path drawing,
  component merging and prepared command queues.
- Backlog impact: retain KAMI 2 for a later scope rather than projecting its
  triangular fields and generated content into the original KAMI record.

## Чому саме вона

- [Hypothesis | Corroborated | High] HOOK presents a compact visible dependency
  graph whose elements must retract only after crossing hooks and blockers are
  cleared, testing a sequential causal grammar absent from the current Atlas.
