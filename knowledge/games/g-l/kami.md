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

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `58` (`GAME-0001`–`GAME-0058`).
- Exact genome matches: none.
- Tied near matches: `GAME-0057` — Golf Peaks (`3 / 12 = 0.250000`).
- Supported combination subsets: `COMB-0059`.
- Scan date: 2026-08-13.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0057` - Golf Peaks | `CON-001`, `INF-001`, `TIM-001` | finite cards route one ball through height geometry versus repeatable region-class rewrite and graph contraction | Near, `0.250000` |

### Preserved research notes

- New genes: `ACT-071`, `SYS-102`, `OBJ-037`, `OBJ-038`.
- Reused genes: `CON-001`, `INF-001`, `TIM-001`.
- Classification result: four `New gene` records and one new verified
  interaction; no novelty claim.

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
