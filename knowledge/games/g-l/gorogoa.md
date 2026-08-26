---
game_id: GAME-0024
slug: gorogoa
game_title: Gorogoa
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0024
gene_ids:
  action:
    - ACT-033
    - ACT-034
    - ACT-035
  system:
    - SYS-043
    - SYS-044
  constraint:
    - CON-001
    - CON-065
    - CON-066
  information:
    - INF-014
  objective:
    - OBJ-018
  time:
    - TIM-002
    - TIM-003
---

# Game: Gorogoa

## Analysis scope

- Version / ruleset: the main four-panel puzzle grammar of Jason Roberts'
  original 2017 Gorogoa release across the five-colour collection journey.
- Included: the fixed two-by-two panel slots; intact panel dragging; panel-
  internal zoom, back-out and pan transitions; detachable foreground or frame
  layers; stacking, overlay and adjacency; authored visual compatibility;
  automatic character, object, light or mechanism continuation across a valid
  composition; self-paced puzzles and the developer-identified isolated timing
  sequence; staged acquisition of the five required coloured tokens.
- Excluded: narrative and religious interpretation; illustration style,
  animation and music except where timing changes input; optional hints,
  achievements, speedrunning, platform gestures and accessibility settings.
- Direct-play status: not conducted for this record. The publisher description
  is combined with the designer's GDC rules account and contemporary reviews;
  examples remain structural and avoid solution-level spoilers.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GOR-001` | Gorogoa's core play consists of arranging and combining illustrated panels | Confirmed | Direct | High | F1, P1, S1–S4 |
| `GOR-002` | The top-level playfield is a fixed two-by-two grid holding at most four current panel positions | Confirmed | Corroborated | High | S2–S4 |
| `GOR-003` | A panel can remain in its slot while the player zooms into, backs out of or pans to another linked illustrated view | Confirmed | Corroborated | High | P1, S1, S3, S4 |
| `GOR-004` | Some panels permit a framed or foreground layer to be lifted away, revealing a persistent underlay and allowing the detached layer to move elsewhere | Confirmed | Corroborated | High | S3, S4 |
| `GOR-005` | Panels can be composed by compatible adjacency or overlay at a particular crop, scale and visual alignment | Confirmed | Corroborated | High | P1, S1–S4 |
| `GOR-006` | A valid composition can automatically join represented spaces or mechanisms so a character, object, light or motion continues across panels | Confirmed | Corroborated | High | P1, S1–S4 |
| `GOR-007` | The player cannot directly manipulate the represented world; puzzle-world change must be caused by combining at least two panels | Confirmed | Direct | High | P1 |
| `GOR-008` | Panel-view transitions and composition results are authored and deterministic, with no random puzzle state | Observation | Corroborated | High | GOR-001–GOR-007, P1 |
| `GOR-009` | Most panel reasoning is self-paced, but the designer identifies one genuine timing puzzle requiring dexterity | Confirmed | Direct | High | P1 |
| `GOR-010` | The panel system can make one-time, one-way state transitions as soon as the required panels connect | Confirmed | Direct | High | P1 |
| `GOR-011` | The current four views expose only selected nodes of deeper illustrated spaces, so useful scenes must be found through navigation | Observation | Corroborated | High | P1, S1, S4 |
| `GOR-012` | The journey is staged around collecting five coloured fruits or offerings through successive panel puzzles | Confirmed | Corroborated | High | S2, S4 |

## Basic data

- Release / origin: designer and illustrator Jason Roberts developed Gorogoa
  under Buried Signal; Annapurna Interactive published the full game in 2017.
- Platform or physical form: digital point-and-click / touch puzzle presented
  as four illustrated panel containers; crop, layer and slot are mechanical
  state rather than presentation alone.
- Puzzle family: nested visual-panel composition and spatial illusion.
- Publisher source:
  - **[F1]** [Annapurna Interactive — Gorogoa](https://annapurnainteractive.com/games/gorogoa),
    identifying the game as illustrated panels that players arrange and
    combine to solve puzzles.
- Designer primary source:
  - **[P1]** Jason Roberts,
    [“Gorogoa: The Design of a Cosmic Acrostic”](https://media.gdcvault.com/gdc2018/presentations/Roberts_Jason_Gorogoa_design_of.pdf),
    GDC 2018 slides describing movable and stackable interactive panels,
    literal connections, zoom, the prohibition on direct world interaction,
    composition-triggered one-way transitions and the sole timing puzzle.
- Contemporary corroboration:
  - **[S1]** [Slant Magazine review](https://www.slantmagazine.com/games/gorogoa/),
    zoom, pan, overlay, adjacency and composition-triggered animation.
  - **[S2]** [The Washington Post review and creator interview](https://www.washingtonpost.com/news/comic-riffs/wp/2017/12/18/gorogoa-a-rare-combination-of-accessible-but-strange-and-intuitive-but-mind-bending/),
    four-slot grid, drag and zoom controls, fused scenes, traversal and the
    five-colour collection structure.
  - **[S3]** [Ars Technica review](https://arstechnica.com/gaming/2017/12/gorogoa-review-video-games-now-have-their-first-classic-childrens-book/),
    detachable layers, underlays, stacking, aligned seams and combined paths.
  - **[S4]** [Stuff review](https://www.stuff.tv/review/app-of-the-week-gorogoa-review/),
    nested panel navigation, removable frames, overlay and alignment examples.
- Claim IDs: `GOR-001`–`GOR-012`.

## Mechanical decomposition

### Action Genes

- `ACT-033` — rearrange intact panel among fixed slots. The panel keeps its
  current illustrated viewpoint while its container moves to a new top-level
  relation with the other panels.
- `ACT-034` — traverse illustrated panel viewpoint. A click selects a visible
  focus, back or pan affordance, not an object manipulation inside the world.
- `ACT-035` — detach and relocate illustrated panel layer. A separable frame or
  foreground becomes its own movable layer while the former underlay remains
  available.
- These actions respectively change container position, view-node selection
  and layer ownership. Treating all three as generic “move image” would hide
  different search spaces and reversibility.
- Claim IDs: `GOR-001`–`GOR-005`, `GOR-011`.

### System Behaviour Genes

- `SYS-043` — selected panel-view substitution. The requested zoom or pan
  changes one panel's displayed node while preserving its slot and the other
  panels' current views.
- `SYS-044` — compatible panel-composition continuation. Once an authored seam
  or overlay relation is satisfied, the system temporarily treats separated
  scenes as continuous and advances an in-world element or mechanism without a
  direct object command.
- Composition may cause a one-time state transition whose resulting scene does
  not simply reset when panels separate. That is a parameter of `SYS-044`, not
  a generic irreversible-action gene because the player's panel arrangement
  may itself remain reversible.
- Claim IDs: `GOR-003`, `GOR-005`, `GOR-006`, `GOR-008`, `GOR-010`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Four persistent top-level slots form
  the complete two-by-two panel workspace; overlay adds layer order inside a
  slot without adding another top-level position.
- `CON-065` — visual seam-or-overlay composition compatibility. Proximity alone
  is insufficient: current crops, scales, apertures or boundary features must
  satisfy a specific authored relation.
- `CON-066` — cross-panel-only represented-world mutation. The player can
  navigate and curate images but cannot click a depicted crank, character or
  object to change it directly; a second panel must supply the causal relation.
- `CON-058` is absent. Dorfromantik compares typed edges on newly committed
  tiles; Gorogoa tests authored image content and can compose by full overlay,
  not a reusable edge-type vocabulary.
- Claim IDs: `GOR-002`, `GOR-005`–`GOR-007`, `GOR-010`.

### Information Genes

- `INF-014` — navigable nested panel scene graph. Each slot displays one
  current illustrated node and its available focus or navigation affordances;
  deeper, surrounding and panned views are not simultaneously visible.
- `INF-001` is absent. The need to locate compatible crops inside hidden
  view-depth is part of the problem, so the four current images do not expose
  every decision-relevant element before action.
- This is not `INF-012`: Obra Dinn indexes stable evidence scenes for
  cross-reference, whereas Gorogoa changes one active panel's composable view
  by traversing an illustrated scene graph.
- Claim IDs: `GOR-003`, `GOR-004`, `GOR-008`, `GOR-011`.

### Objective Genes

- `OBJ-018` — complete finite staged token collection. Panel compositions
  repeatedly open a route or causal interaction through which the represented
  boy obtains the five coloured fruits / offerings structuring the journey.
- Individual local puzzles may pursue a door, light, falling object or machine
  state, but these are intermediate transitions toward the finite staged set,
  not separate score or route-completion objectives.
- Claim IDs: `GOR-006`, `GOR-010`, `GOR-012`.

### Time Genes

- `TIM-002` — self-paced sequential action governs almost all view exploration,
  layer separation and panel composition; waiting alone normally changes
  nothing decision-relevant.
- `TIM-003` — real-time input during forced progression applies to the one
  developer-identified timing puzzle, where a moving illustrated state must be
  composed at the required moment.
- The isolated `TIM-003` instance is included because it changes the legal
  timing of panel actions, while decorative animation is excluded.
- Claim IDs: `GOR-008`, `GOR-009`.

## Reproducible transitions

| Before | Player action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| One intact panel occupies the upper-left slot | Drag it to an empty lower slot | Current internal view is preserved at the new top-level position | Container rearrangement is distinct from view traversal | `GOR-001`, `GOR-002` |
| A panel displays a visible framed detail | Select that detail | The same slot now shows the linked closer illustrated view | Zoom is scene-graph traversal | `GOR-003`, `GOR-011` |
| A separable window layer covers another image | Lift and drag the foreground to another slot | Underlay remains visible and foreground becomes an independent layer | Separation preserves both layers | `GOR-004` |
| Doorway layer and destination scene are in different slots | Overlay the doorway at the compatible crop and scale | Character can cross into the destination scene automatically | Overlay creates represented continuity | `GOR-005`–`GOR-007` |
| Two panels show complementary scene edges | Place them in adjacent slots with matching boundaries | An object or character continues across the joined seam | Adjacency and overlay share a composition family | `GOR-005`, `GOR-006` |
| Same panels are adjacent at incompatible zoom levels | Leave or move them together | No cross-panel continuation occurs | Visual compatibility is a predicate, not mere proximity | `GOR-005` |
| A depicted crank is visible in one isolated panel | Click or inspect it without another panel relation | No direct represented-world mutation is available | Panel combination supplies causality | `GOR-007` |
| Required panels connect around a prepared mechanism | Complete the composition | Mechanism advances once and may retain the new scene state | Continuation can be one-way | `GOR-010` |
| Isolated moving sequence is active | Reposition or compose its panel during the motion window | Outcome depends on the selected real-time moment | One bounded puzzle instantiates `TIM-003` | `GOR-009` |

## Strategic and experiential structure

- Local decision: inspect the current crop for focus targets, detachable layers
  and visual features that could match another panel.
- Medium-term planning: preserve useful view nodes while exploring another
  panel, then choose whether the required relation is adjacency, overlay or a
  causal chain through a third panel.
- Long-term structure: successively re-curate the same four slots so nested
  scenes and one-way continuations deliver the next coloured token.
- Common heuristics: compare apertures and edges at several scales; treat
  depicted books, windows and paintings as possible portals; separate a layer
  when dragging reveals retained content; distinguish visual rhyme from a
  mechanically exact alignment.
- Failure attribution: most experiments are reversible and non-terminal. A
  non-response usually means wrong crop, scale, slot relation or view node;
  one-way transitions and the timing sequence require more care.
- Player-trust factors: draggable layers, hit targets, stack order, seam
  tolerances, automatic transfer and back-navigation must be visually legible.
- Claim IDs: `GOR-001`–`GOR-012`.

## Replay and variation

- What changes between sessions: exploration order, retained panel views and
  unsuccessful composition experiments.
- What remains stable: scene graph, detachable layers, compatibility relations,
  automatic transitions and token sequence.
- Randomness or procedural generation: none in the scoped puzzles.
- Multiple viable strategies: local search order may vary, but authored
  composition gates strongly constrain the successful panel states.
- Typical replay motive: re-experience the visual transformations or solve
  with fewer exploratory clicks; the fixed puzzle graph provides little
  systemic outcome variation after its relations are known.
- Claim IDs: `GOR-001`, `GOR-008`–`GOR-012`.

## Adjacent systems and history

- Flow Free and Dorfromantik compose visible spatial pieces, but their paths or
  landscapes occupy one geometric world. Gorogoa makes separate depictions
  continuous only at selected crop, layer and scale states.
- Baba Is You changes world rules by moving syntax objects inside the world.
  Gorogoa forbids direct world mutation and changes causality by re-curating
  frames outside it.
- Return of the Obra Dinn also navigates selectively visible scenes, but its
  scenes are immutable evidence indexed for semantic inference. Gorogoa views
  are active compositional operands whose pairing changes represented events.
- Claim IDs: `GOR-001`–`GOR-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-033`, `ACT-034`, `ACT-035` | slot drag, view graph and detachable layers |
| System Behaviour | `SYS-043`, `SYS-044` | view substitution and continuation effects |
| Constraint | `CON-001`, `CON-065`, `CON-066` | four slots and authored visual compatibility |
| Information | `INF-014` | scene depth and visible navigation affordances |
| Objective | `OBJ-018` | five-token stage order |
| Time | `TIM-002`, `TIM-003` | dominant self-paced play and one timing puzzle |

Canonical signature:

`ACT-033,ACT-034,ACT-035; SYS-043,SYS-044; CON-001,CON-065,CON-066; INF-014; OBJ-018; TIM-002,TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `23` (`GAME-0001`–`GAME-0023`).
- Exact genome matches: none.
- Tied near matches: `GAME-0002` — Rubik’s Cube (`2 / 17 = 0.117647`); `GAME-0005` — Sudoku (`2 / 17 = 0.117647`); `GAME-0008` — Nonogram (`2 / 17 = 0.117647`).
- Supported combination subsets: `COMB-0024`.
- Scan date: 2026-08-12.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0002` — Rubik's Cube | `CON-001`, `TIM-002` | Rubik's Cube reversibly permutes one fixed physical object under global invariants; Gorogoa searches nested views and composes separate image layers into causal continuity | Near, `0.117647` |
| `GAME-0005` — Sudoku | `CON-001`, `TIM-002` | Sudoku assigns numbers to fixed cells under simultaneous constraints; Gorogoa moves panel containers and viewpoints until authored visual relations trigger world transitions | Near, `0.117647` |
| `GAME-0008` — Nonogram | `CON-001`, `TIM-002` | Nonogram reconstructs one binary image from line clues; Gorogoa treats images themselves as layered, navigable operands and includes one real-time exception | Near, `0.117647` |

### Preserved research notes

- New genes: `ACT-033`, `ACT-034`, `ACT-035`, `SYS-043`, `SYS-044`,
  `CON-065`, `CON-066`, `INF-014`, `OBJ-018`.
- Classification result: `New gene` and a new verified combination.
- Evidence and reasoning: four fixed slots and the two applicable scheduling
  modes reuse existing boundaries. Panel-container motion, view traversal,
  layer separation, visual composition and cross-panel causality are absent
  from the first twenty-three genomes.

## Combination record

- Registered [`COMB-0024`](../../combinations/COMB-0024.md), a proper
  nine-gene subset centred on discovering and combining nested illustrated
  panel states into causal continuity.
- Fixed slot count, staged token objective and the isolated timing exception
  remain in the full genome but are not required to identify the core panel
  grammar.

## Taxonomy impact

- Registry changes: nine stable genes added; `CON-001`, `TIM-002` and
  `TIM-003` reused.
- Taxonomy-change record: none. Container and view commands remain Actions;
  automatic illustrated-state changes remain System Behaviour; visual
  compatibility and the ban on direct world input remain Constraints.
- Candidate terms affected: panel rearrangement, nested view traversal, layer
  separation, view substitution, composition continuation, visual alignment,
  cross-panel causality, nested scene graphs and staged collection are promoted.

## Negative results

- `ACT-014` is absent because the represented character is not directly moved
  to a selected destination.
- `CON-058` is absent because matching depends on authored visual crop and
  overlay, not typed tile edges.
- `INF-001` is absent because relevant nested views are not simultaneously
  displayed.
- `OBJ-010` is absent because no directly controlled `YOU` object or mutable
  rule-defined `WIN` property exists.
- No structured negative-result record is required; no prior concrete novelty
  or taxonomy claim was rejected.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] The player cannot directly change the depicted
  world; valid multi-panel composition supplies every puzzle-world mutation
  (`GOR-005`–`GOR-007`).
- [Confirmed | Corroborated | High] Container position, current view node and
  detachable layer are independent player-controlled state (`GOR-002`–`GOR-005`).

## Нові гени

- [Observation | Corroborated | High] Added `ACT-033`, `ACT-034`, `ACT-035`,
  `SYS-043`, `SYS-044`, `CON-065`, `CON-066`, `INF-014` and `OBJ-018`;
  reused `CON-001`, `TIM-002` and `TIM-003`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0024` captures nested panel states
  whose compatible spatial composition creates represented-world causality.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; external panel
  actions and internal automatic continuation fit the existing cross-type
  boundary.

## Нові питання

- Does another panel puzzle reuse `CON-065` while allowing direct interaction
  and therefore rejecting `CON-066`?
- Can `INF-014` describe a non-illustrated nested interface without becoming a
  generic menu-navigation gene?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0025` — Lemmings.
- Optimisation criterion: move from self-paced panel composition to live
  indirect control of many autonomous agents.
- Expected information gain: separate skill assignment from agent execution,
  population rescue quotas, finite role inventory and global release / time
  pressure while testing reuse of `TIM-003`.
- Backlog impact: remove Lemmings from the retained pool; preserve World of Goo
  for `GAME-0026` unless the next comparison changes priority.

## Чому саме вона

- [Hypothesis | Limited | High] Lemmings supplies the remaining uncovered
  indirect-agent control structure and contrasts with both Gorogoa's external
  panel causality and Cut the Rope's single physical payload.
