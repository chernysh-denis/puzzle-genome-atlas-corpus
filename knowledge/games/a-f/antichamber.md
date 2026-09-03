---
game_id: GAME-0097
slug: antichamber
game_title: Antichamber
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0097
gene_ids:
  action:
    - ACT-008
    - ACT-098
  system:
    - SYS-129
  constraint:
    - CON-148
  information:
    - INF-001
    - INF-047
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Antichamber

## Analysis scope

- Version / ruleset: Alexander Bruce's original 2013 release, bounded to the
  `Now You See It` blue-cube doorway lesson. The packet starts with the doorway
  in its original destination state and the blue cube on its pedestal. It keeps
  two controlled routes: collect the cube while continuously watching the door
  to preserve the original room, or collect it and look through the glass
  window so the unobserved threshold reconnects to the changed room before the
  player returns and crosses it.
- Included: direct first-person walking; mouse free-look; one stable local
  doorway; one cube-collection trigger; doorway visibility; one authored
  off-screen destination replacement; revealed traversal into the changed
  room; current local geometry; a concealed remote adjacency; live input.
- Excluded: cube-gun manipulation beyond collecting the scoped cube, staircase
  loops, dark mazes, nine view-dependent cubes, eyes, lasers, trampolines,
  collapsing paths, map teleports, the ending, secrets, achievements,
  speedruns, platform bindings and every other room transition.
- Direct-play status: not conducted. The official product record and two
  developer interviews establish reconfiguring space, unconventional authored
  spatial relations and arbitrary room connections. A contemporary complete
  walkthrough fixes the exact watched-door and glass-window alternatives. The
  executable control proves the bounded causal rule, not production frustum
  code, room coordinates, animation timing or the complete world graph.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ANT-001` | Antichamber launched in 2013 as Alexander Bruce's first-person exploration puzzle | Confirmed | Direct | High | P1, P2 |
| `ANT-002` | Its authored world uses unconventional spatial relations in which hallways wrap and spaces reconfigure | Confirmed | Direct | High | P1–P3 |
| `ANT-003` | Bruce deliberately connected otherwise separate spaces to create a flowing non-Euclidean route | Confirmed | Direct | High | P3 |
| `ANT-004` | In `Now You See It`, taking the blue cube and looking through the glass window changes the room behind the doorway | Confirmed | Corroborated | High | S1 |
| `ANT-005` | Keeping the doorway continuously in view prevents that change and preserves its usable original destination | Confirmed | Corroborated | High | S1 |
| `ANT-006` | Walking and camera direction are both decision-bearing inputs in the bounded route | Confirmed | Corroborated | High | S1, S2 |
| `ANT-007` | The control distinguishes one stable local threshold from two authored remote destinations | Observation | Direct | High | V1, ANT-003–ANT-005 |
| `ANT-008` | The control rejects visible replacement, unarmed replacement, an unauthored destination and premature goal credit | Observation | Direct | High | V1 |
| `ANT-009` | The scoped change is neither a visible paired aperture, periodic translation nor simultaneous recursive instance | Observation | Corroborated | High | P2, P3, GAME-0033, GAME-0095, GAME-0096 |

## Basic data

- Release / origin: Alexander Bruce developed Antichamber; Demruth published
  it on Steam on 31 January 2013.
- Platform or physical form: single-player real-time first-person exploration
  puzzle in a three-dimensional authored world.
- Puzzle family: observation-gated authored doorway remapping.
- Creator and official sources:
  - **[P1]** [Antichamber on Steam](https://store.steampowered.com/app/219890/Antichamber/),
    for developer, publisher, date, first-person exploration and the official
    description of wrapping hallways and reconfiguring spaces.
  - **[P2]** [Adventure Classic Gaming — Alexander Bruce interview](https://www.adventureclassicgaming.com/index.php/site/interviews/817/),
    where Bruce defines the game's non-Euclidean label as space that does not
    follow ordinary navigational rules and contains impossible 3D situations.
  - **[P3]** [Engadget — On The Fringe: Alexander Bruce's Antichamber](https://www.engadget.com/2012-05-02-on-the-fringe-part-one-alexander-bruces-antichamber.html),
    where Bruce explains deliberately and arbitrarily connecting authored
    spaces to remove dead ends and produce the final flowing world.
- Reproducible corroboration:
  - **[S1]** [Jay Is Games — Antichamber walkthrough](https://jayisgames.com/review/antichamber.php),
    for the named `Now You See It` route: take the blue cube, look through the
    glass window and return to a changed room, or keep staring at the door to
    stop it changing.
  - **[S2]** [ABC Good Game — Antichamber](https://www.abc.net.au/tv/goodgame/stories/s3693740.htm),
    contemporaneous corroboration that looking through windows can change a
    room when the player steps back.
  - **[V1]**
    [`verify_antichamber_control.py`](../../../scripts/verify_antichamber_control.py),
    an executable two-destination doorway control with six rejected invalid
    transitions.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. The player walks between the cube,
  doorway and glass window, then crosses the currently mapped threshold.
- `ACT-098` — direct free-look toward or away from rule-bearing geometry. The
  player either keeps the doorway in view to preserve it or deliberately faces
  the window so the doorway leaves view and may change.
- Collecting the cube arms this bounded lesson but is not classified as
  general rigid-object carrying: no carried-object placement or physics is
  necessary to the chosen causal packet.

### System Behaviour Genes

- `SYS-129` — observation-gated authored doorway destination remapping. Once
  the cube trigger is armed and the doorway becomes unobserved, the system
  replaces its fixed destination from the original room to the authored changed
  room without moving or duplicating the visible threshold.
- Resolution order: collect cube; arm replacement; sample doorway visibility;
  preserve the destination while watched; otherwise select the authored changed
  destination; retain that mapping on reobservation; resolve traversal; test
  arrival at the changed room.
- The control records logical destinations, not production coordinates. A
  seamless implementation may teleport or stream the avatar, but implementation
  technique is not promoted into a separate gene without direct evidence.

### Constraint Genes

- `CON-148` — spatial replacement requires the affected threshold to be
  unobserved. An armed change cannot resolve while the doorway remains in view.
- The changed destination must belong to the authored two-state control graph;
  a procedural third room is rejected.
- The cube must be collected before looking away can arm this exact lesson.
  Looking away from an unarmed door does not itself force the scoped change.

### Information Genes

- `INF-001` — fully visible current state. The cube, local doorway, window,
  current facing and revealed room geometry are directly inspectable at their
  respective decision moments.
- `INF-047` — stable local threshold with concealed remote destination. The
  doorway's local shape does not expose a persistent map edge to the current
  remote room; the changed adjacency is learned only after the viewpoint event
  and return or traversal.
- The wall lesson and room change provide qualitative feedback, not a numeric
  destination label or live cross-threshold view.

### Objective Genes

- `OBJ-026` — reach designated traversable world location. The bounded success
  condition is entering the newly connected changed room after making that
  destination traversable through the same doorway.
- Retaining the original room is a falsification control, not completion of the
  selected changed-room route.

### Time Genes

- `TIM-003` — real-time input during forced progression. Walking, free-look,
  visibility sampling and threshold traversal occur continuously.
- There is no authored deadline. The decisive order is causal, not a score for
  fast execution.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Cube is present; door maps to original room | collect cube while keeping door visible | replacement arms but original destination persists | collection alone does not remap a watched threshold | `ANT-004`, `ANT-005` |
| Watched control remains armed | traverse the watched doorway | player reaches original room | stable observation is a valid falsification route | `ANT-005` |
| Fresh control has original destination | collect blue cube | replacement becomes armed | bounded trigger precedes visibility condition | `ANT-004` |
| Armed doorway is visible | turn and look through glass window | doorway leaves view and destination becomes changed room | observation loss permits authored remapping | `ANT-004`, `ANT-005` |
| Doorway now maps to changed room | turn back toward the same local threshold | changed mapping persists and new room becomes revealable | local threshold identity survives remote replacement | `ANT-004`, `ANT-007` |
| Changed destination is active | cross doorway | player arrives in designated changed room | nonlocal adjacency is traversal-authoritative | `ANT-003`, `ANT-007` |

The executable control separately rejects changing a watched doorway, claiming
the changed room early, changing an unarmed doorway, assigning an unauthorised
third destination, crediting the original room and granting arrival through an
unchanged control. It omits rendering, collision meshes, streaming and every
other Antichamber spatial trick.

## Strategic and experiential structure

- Local decision: treat looking direction as an input to world state rather
  than merely a means of inspection.
- Medium-term planning: distinguish the useful watched-door control from the
  changed-room route and order cube collection before looking away.
- Long-term structure: the wider game teaches many different spatial rules;
  none is inferred from this one room.
- Common heuristic: when an apparently fixed route stalls, test whether the
  relevant threshold changes only outside observation.
- Failure attribution: returning to the original room follows continued
  observation or missing trigger state, not randomness.
- Player-trust factor: local doorway form may stay stable while remote
  adjacency changes, so feedback must make the new destination discoverable.

## Replay and variation

- The bounded lesson is deterministic and has two controlled outcomes. Input
  angle and movement path may vary, but destination selection depends only on
  trigger and visibility state in the model.
- No procedural room generation or random destination is in scope.
- Exact peripheral-vision threshold, occlusion tolerance and replacement delay
  remain implementation parameters.

## Adjacent systems and history

- Portal presents two explicit apertures and a live view of the paired endpoint;
  Antichamber retains one ordinary-looking local doorway and conceals its
  authored remote destination until the observation rule resolves.
- Manifold Garden maps a body across a fixed translational period while
  preserving local pose. Antichamber changes which fixed room a threshold
  reaches and does not repeat one lattice cell.
- Maquette simultaneously exposes homologous instances sharing object state.
  Antichamber exposes one local threshold whose remote graph edge is replaced.
- Fez rotates a fixed world into a new screen-space collision slice.
  Antichamber neither rotates the world nor derives adjacency from projection.
- Viewfinder commits a held image as replacement geometry. Antichamber's
  player supplies no geometry asset; the destination state is pre-authored.

## Normalised genome

| Gene type | IDs | Scope meaning |
|---|---|---|
| Action | `ACT-008`, `ACT-098` | walk and deliberately change rule-bearing view direction |
| System Behaviour | `SYS-129` | remap one unobserved doorway to an authored destination |
| Constraint | `CON-148` | preserve the current destination while the door is watched |
| Information | `INF-001`, `INF-047` | visible local state but concealed remote adjacency |
| Objective | `OBJ-026` | enter the newly connected changed room |
| Time | `TIM-003` | live walking, looking and visibility resolution |

Full signature:
`ACT-008,ACT-098; SYS-129; CON-148; INF-001,INF-047; OBJ-026; TIM-003`.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `96` (`GAME-0001`–`GAME-0096`).
- Exact genome matches: none.
- Tied near matches: `GAME-0091` — Fez (`4 / 13 = 0.307692`).
- Supported combination subsets: `COMB-0097`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0091`.

### Preserved research notes

- Exhaustive combination comparison finds no prior combination equal to,
  contained by or containing the candidate.

## Coverage decision

- Reuse direct navigation, complete current local visibility, location arrival
  and real-time scheduling.
- Add only the missing causal boundaries: rule-bearing free-look, authored
  doorway remapping, an unobserved-only eligibility constraint and concealed
  remote adjacency.
- Do not generalise from one doorway to every Antichamber perception puzzle.

## Confidence and open questions

### Assumptions

- The control represents the changed destination as one persistent state after
  the door leaves view. The observable route is established; production may
  stage replacement through streaming or a hidden teleport volume.
- The blue-cube pickup is retained as the bounded trigger because the
  walkthrough explicitly orders it before the two viewpoint alternatives.

### Unknowns

- Exact camera-frustum test, peripheral tolerance, occlusion policy, trigger
  volume, reset boundary and destination coordinates were not measured.
- Whether the production door remaps its graph edge before or during the return
  camera turn is not visible and does not alter this taxonomy boundary.

### Confidence

- High for the watched versus unobserved outcomes and authored nonlocal
  connectivity; medium-high for the normalised state-machine implementation.

## Combination candidate

- Candidate ID: `COMB-0097`.
- Gene set: `ACT-098`, `SYS-129`, `CON-148`, `INF-047`, `OBJ-026`.
- Supporting game: `GAME-0097`.
- Proper-subset rationale: walking, complete local visibility and live time
  support execution but do not define the observation-gated room relation.
- Novelty claim: not assessed.

## Outcome

- Reused genes: `ACT-008`, `INF-001`, `OBJ-026`, `TIM-003`.
- Added genes: `ACT-098`, `SYS-129`, `CON-148`, `INF-047`.
- Added combination: `COMB-0097`.
- Evidence gate: passed with one official product record, two creator
  interviews, two contemporary route descriptions and one executable verifier.
- Nearest prior genome: Fez; see `Corpus comparison` for the current result.
- Next falsification target: Hyperbolica, to test continuously curved spatial
  navigation without an off-screen doorway replacement.

## Taxonomy impact

- Free-look is separated from camera orbit that makes projection itself
  authoritative and from passive evidence inspection.
- Hidden authored adjacency is separated from explicit portals, periodic
  boundaries, recursive homologues and procedural room choice.
- Observation is represented twice only where causally distinct: a player
  action changes facing, while a constraint prevents replacement during view.

## Negative results

- `SYS-059` is absent because no player-placed paired aperture exists.
- `SYS-126` is absent because no fixed spatial period or pose-preserving wrap
  defines the route.
- `SYS-127` is absent because the rooms are not simultaneous scale-linked
  representations of one state.
- `ACT-095` is absent because the player does not orbit an immutable stage to
  make apparent contact authoritative.
- No generic randomness, teleport action or procedural-generation gene is
  introduced.
