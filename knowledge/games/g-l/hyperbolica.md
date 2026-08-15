---
game_id: GAME-0098
slug: hyperbolica
game_title: Hyperbolica
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0098
gene_ids:
  action:
    - ACT-008
  system:
    - SYS-130
  constraint:
    - CON-149
  information:
    - INF-001
    - INF-048
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Hyperbolica

## Analysis scope

- Version / ruleset: CodeParade's 2022 desktop release, bounded to one
  reproducible `Maze of Apeirogon` crystal route after obtaining the overworld
  map. The packet starts at the maze entrance, follows the eleven intersection
  choices `R, L, R, L, L, L, L, R, L, L, R`, reaches the hexahedron at the
  end and credits that Platonic Crystal.
- Included: direct first-person walking and looking; continuous traversal in a
  constant-negative-curvature world; order-five square incidence; curved
  distance and direction rendering; the authored maze; one fixed route; one
  crystal arrival; visible current local state; real time.
- Excluded: the Oracle conversation, map acquisition, Giant Pin assistance,
  lost child, lore lecterns, chocolate bar, other crystals, spherical worlds,
  drone race, shooting, platforming, Infinity Café, trebuchet, final encounter,
  VR implementation, achievements, speed timing and quit/continue skips.
- Direct-play status: not conducted. The official product record establishes
  the continuously hyperbolic world, exponential spatial growth, non-parallel
  lines, accumulated rotations and the non-Euclidean labyrinth. CodeParade's
  rendering devlog establishes the creator's hyperbolic world construction. A
  maintained beginner route fixes the exact eleven decisions, and a community
  location record corroborates the hexahedron at the maze end. The executable
  control proves the bounded geometry invariants and route, not production
  coordinates, shaders, collision meshes or undocumented curvature scale.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HYP-001` | Hyperbolica released on 14 March 2022, developed and published by CodeParade | Confirmed | Direct | High | P1 |
| `HYP-002` | The game uses true non-Euclidean worlds for first-person exploration and includes a non-Euclidean labyrinth | Confirmed | Direct | High | P1 |
| `HYP-003` | Its hyperbolic space grows exponentially, does not preserve parallel lines and may accumulate unexpected rotation during traversal | Confirmed | Direct | High | P1 |
| `HYP-004` | CodeParade built and rendered the game world using hyperbolic-space operations rather than only a flat visual illusion | Confirmed | Direct | High | P2 |
| `HYP-005` | The Maze of Apeirogon route uses eleven fixed left/right intersection choices ending `R, L, R, 4L, R, 2L, R` | Confirmed | Corroborated | High | S1 |
| `HYP-006` | A hexahedron Platonic Crystal lies at the end of the maze | Confirmed | Corroborated | High | S2 |
| `HYP-007` | Five regular 72-degree square sectors close one `{4,5}` hyperbolic vertex whereas four do not satisfy the scoped incidence | Observation | Direct | High | M1, V1 |
| `HYP-008` | At radius two, hyperbolic circumference exceeds the flat control by `1.813430×` | Observation | Direct | High | V1 |
| `HYP-009` | The control preserves the hyperboloid norm, distinguishes translation order and rejects six invalid geometry or route controls | Observation | Direct | High | V1 |

## Basic data

- Release / origin: CodeParade developed and published Hyperbolica on 14 March
  2022.
- Platform or physical form: single-player real-time first-person exploration
  adventure for desktop and optional VR.
- Puzzle family: continuous hyperbolic-metric maze traversal.
- Creator and official sources:
  - **[P1]** [Hyperbolica on Steam](https://store.steampowered.com/app/1256230/Hyperbolica/),
    for creator, publisher, release date, first-person non-Euclidean worlds,
    the labyrinth, exponential volume, divergent parallels and traversal
    rotation.
  - **[P2]** [CodeParade — Rendering Hyperbolic Spaces, Hyperbolica Devlog #3](https://www.youtube.com/watch?v=pXWRYpdYc7Q),
    the creator's technical account of building and rendering hyperbolic worlds.
- Reproducible corroboration:
  - **[S1]** [Hyperbolica Any% Beginner Guide](https://gist.github.com/shenef/a8c97f3dc54f9f22080a536b572958df),
    for the named Maze of Apeirogon and exact eleven intersection decisions.
  - **[S2]** [Hyperbolica Wiki — The Maze](https://hyperbolica.fandom.com/wiki/The_Maze),
    for the map prerequisite, Platonic Crystal and hexahedron at the maze end.
  - **[M1]** [David E. Joyce — Hyperbolic Tessellations](https://aleph0.clarku.edu/~djoyce/poincare/poincare.html),
    an independent mathematical reference defining the dual `{4,5}` tiling as
    squares with five meeting at every vertex.
  - **[V1]**
    [`verify_hyperbolica_control.py`](../../../scripts/verify_hyperbolica_control.py),
    an executable metric-and-route control with six rejected invalid cases.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. The player continuously walks and
  turns through the maze, choosing one branch at each bounded intersection.
- Free-look is ordinary first-person orientation here. Unlike Antichamber's
  `ACT-098`, taking geometry out of view does not arm or block a world-state
  transition.

### System Behaviour Genes

- `SYS-130` — continuous constant-negative-curvature pose integration. Each
  movement composes the avatar/world relation through hyperbolic isometries;
  the local step remains smooth while metric distance, angular relation and
  accumulated orientation differ from Euclidean translation.
- Resolution order: sample movement and facing; integrate one curved-metric
  pose increment; preserve metric normalisation; resolve collision in that
  pose; render the new curved view; expose the next intersection; test crystal
  contact.
- The verifier uses Lorentz boosts on the unit hyperboloid. Their preserved
  Minkowski norm checks metric consistency, while different `x→y` and `y→x`
  compositions falsify a commuting flat-translation substitute.

### Constraint Genes

- `CON-149` — order-five square incidence governs local route adjacency. Five
  regular quadrilateral sectors with 72-degree interior angles meet at one
  hyperbolic vertex, producing local route structure impossible for a flat
  square grid.
- The rule is metric rather than decorative. Replacing it with four 90-degree
  Euclidean squares collapses the chosen geometric boundary.
- The exact production maze need not place an intersection at every tiling
  vertex; authored walls restrict which metric adjacencies become choices.

### Information Genes

- `INF-001` — fully visible current state. Nearby walls, floor, current facing,
  accessible branch mouths and the crystal at arrival are directly rendered at
  their relevant decision moments.
- `INF-048` — continuous curvature-rendered distance and direction cues. The
  live view uses the traversed curved geometry: horizons bend, spatial volume
  expands faster than flat intuition predicts and direction can accumulate
  rotation along a route.
- The bounded route notation is corroboration, not an in-game full-route
  forecast. Giant Pin guidance is explicitly excluded.

### Objective Genes

- `OBJ-026` — reach designated traversable world location. The bounded success
  condition is reaching the maze's final hexahedron location and collecting its
  Platonic Crystal.
- A wrong branch or partial sequence does not receive proxy completion in the
  control.

### Time Genes

- `TIM-003` — real-time input during forced progression. Walking, turning,
  collision and curved-pose integration update continuously.
- There is no deadline in scope; speedrun timing and quit/continue skips are
  excluded.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Unit hyperboloid pose | walk one fixed distance on the first axis | Lorentz boost preserves Minkowski norm `1` | locomotion stays on the curved metric | `HYP-004`, `HYP-009` |
| Same origin and step size | compose orthogonal steps in opposite orders | endpoints differ while both norms remain `1` | translation order is structurally relevant | `HYP-003`, `HYP-009` |
| Radius `2` in curvature `−1` | compare `2π sinh(r)` with `2πr` | ratio is `1.813430` | available circumference grows faster than flat space | `HYP-003`, `HYP-008` |
| One regular `{4,5}` vertex | place five equal square corners of `72°` | angles close exactly to `360°` | five-way square incidence is metric-valid | `HYP-007` |
| Maze entrance | choose `R, L, R, 4L, R, 2L, R` | all eleven authored decisions are accepted | route reproduces the documented maze traversal | `HYP-005` |
| Complete route at final chamber | contact hexahedron | Platonic Crystal is credited | designated-location objective is reached | `HYP-006` |

The control separately rejects a flat four-square vertex, zero-radius growth
claim, wrong first turn, unknown branch symbol, early crystal claim and
truncated route. It does not emulate production rendering or claim that this
one intersection sequence uniquely characterises every hyperbolic maze.

## Strategic and experiential structure

- Local decision: identify the next visible left/right branch despite
  unfamiliar angular and distance cues.
- Medium-term planning: retain an ordered turn sequence rather than assuming a
  Euclidean overhead layout will remain intuitive.
- Long-term structure: the wider collection route spans different geometries
  and activities; only one hyperbolic maze crystal is in scope.
- Common heuristic: use stable local landmarks and branch order instead of
  estimating flat-map direction or parallel corridors.
- Failure attribution: a wrong arrival follows a wrong branch sequence, not a
  random room mapping.
- Player-trust factor: the geometry may violate flat intuition, but movement,
  collision and rendering must agree on one continuous metric.

## Replay and variation

- The bounded route and geometry are deterministic. Walking line, camera path
  and timing may vary while the intersection sequence stays fixed.
- No procedural maze generation, shuffled destination or random curvature is
  in scope.
- Exact curvature magnitude, collision tolerance and projection parameters
  remain implementation details unless directly measured.

## Adjacent systems and history

- Antichamber replaces a hidden authored doorway destination after the
  threshold leaves view. Hyperbolica changes neither room identity nor graph
  edge off-screen; continuous travel itself follows a curved metric.
- Manifold Garden repeats one Euclidean-looking 3D cell by whole-period
  translation. Hyperbolica has exponential metric growth without crossing a
  periodic seam or returning through a translated copy.
- Portal maps pose and momentum through two explicit apertures. Hyperbolica
  requires no aperture and integrates ordinary walking everywhere.
- Fez and Echochrome make a projection authoritative for collision or
  traversal. Hyperbolica's projection visualises a separately consistent
  curved metric instead of manufacturing an adjacency from screen overlap.
- HyperRogue is retained as the next falsification target because its discrete
  hyperbolic tiling can test whether `CON-149` transfers while `SYS-130` does
  not.

## Normalised genome

| Gene type | IDs | Scope meaning |
|---|---|---|
| Action | `ACT-008` | continuously walk and turn through the maze |
| System Behaviour | `SYS-130` | integrate pose in constant negative curvature |
| Constraint | `CON-149` | five regular squares may meet at one metric vertex |
| Information | `INF-001`, `INF-048` | visible local geometry and continuous curvature cues |
| Objective | `OBJ-026` | reach and collect the maze crystal |
| Time | `TIM-003` | live locomotion and metric resolution |

Full signature:
`ACT-008; SYS-130; CON-149; INF-001,INF-048; OBJ-026; TIM-003`.

## Corpus comparison

The comparison scans every complete prior signature (`GAME-0001` through
`GAME-0097`) with canonical Jaccard intersection over union.

- Near match: `GAME-0097` Antichamber is uniquely nearest at
  `4 / 11 = 0.363636`, sharing direct navigation, current local visibility,
  designated-location arrival and real time.
- `GAME-0091` Fez follows at `4 / 12 = 0.333333` on the same four reusable
  traversal genes. Carto follows at `3 / 12 = 0.250000`, while Superliminal
  and Maquette each score `3 / 14 = 0.214286`.
- Manifold Garden scores `3 / 16 = 0.187500` and Portal scores
  `3 / 17 = 0.176471`; neither shares curved-metric integration, order-five
  incidence or curvature-rendered cues.
- The five-gene candidate `ACT-008, SYS-130, CON-149, INF-048, OBJ-026` is a
  proper subset of the seven-gene full signature.
- Exhaustive combination comparison finds no prior combination equal to,
  contained by or containing the candidate.

- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `1 / 20 = 0.050000`; `GAME-0002`: `1 / 13 = 0.076923`; `GAME-0003`: `0 / 16 = 0.000000`; `GAME-0004`: `2 / 20 = 0.100000`; `GAME-0005`: `1 / 13 = 0.076923`; `GAME-0006`: `2 / 14 = 0.142857`; `GAME-0007`: `1 / 14 = 0.071429`; `GAME-0008`: `1 / 13 = 0.076923`.
  - `GAME-0009`: `1 / 22 = 0.045455`; `GAME-0010`: `1 / 15 = 0.066667`; `GAME-0011`: `1 / 19 = 0.052632`; `GAME-0012`: `1 / 15 = 0.066667`; `GAME-0013`: `1 / 19 = 0.052632`; `GAME-0014`: `1 / 21 = 0.047619`; `GAME-0015`: `1 / 20 = 0.050000`; `GAME-0016`: `2 / 20 = 0.100000`.
  - `GAME-0017`: `0 / 20 = 0.000000`; `GAME-0018`: `2 / 24 = 0.083333`; `GAME-0019`: `1 / 16 = 0.062500`; `GAME-0020`: `1 / 20 = 0.050000`; `GAME-0021`: `2 / 14 = 0.142857`; `GAME-0022`: `1 / 18 = 0.055556`; `GAME-0023`: `0 / 17 = 0.000000`; `GAME-0024`: `1 / 18 = 0.055556`.
  - `GAME-0025`: `2 / 16 = 0.125000`; `GAME-0026`: `2 / 17 = 0.117647`; `GAME-0027`: `2 / 17 = 0.117647`; `GAME-0028`: `2 / 22 = 0.090909`; `GAME-0029`: `3 / 16 = 0.187500`; `GAME-0030`: `2 / 19 = 0.105263`; `GAME-0031`: `1 / 17 = 0.058824`; `GAME-0032`: `1 / 17 = 0.058824`.
  - `GAME-0033`: `3 / 17 = 0.176471`; `GAME-0034`: `3 / 18 = 0.166667`; `GAME-0035`: `3 / 22 = 0.136364`; `GAME-0036`: `2 / 17 = 0.117647`; `GAME-0037`: `1 / 15 = 0.066667`; `GAME-0038`: `3 / 20 = 0.150000`; `GAME-0039`: `1 / 15 = 0.066667`; `GAME-0040`: `3 / 12 = 0.250000`.
  - `GAME-0041`: `3 / 15 = 0.200000`; `GAME-0042`: `1 / 15 = 0.066667`; `GAME-0043`: `2 / 19 = 0.105263`; `GAME-0044`: `2 / 15 = 0.133333`; `GAME-0045`: `2 / 19 = 0.105263`; `GAME-0046`: `1 / 16 = 0.062500`; `GAME-0047`: `1 / 20 = 0.050000`; `GAME-0048`: `1 / 20 = 0.050000`.
  - `GAME-0049`: `0 / 16 = 0.000000`; `GAME-0050`: `2 / 20 = 0.100000`; `GAME-0051`: `2 / 21 = 0.095238`; `GAME-0052`: `1 / 16 = 0.062500`; `GAME-0053`: `2 / 14 = 0.142857`; `GAME-0054`: `3 / 15 = 0.200000`; `GAME-0055`: `2 / 15 = 0.133333`; `GAME-0056`: `1 / 14 = 0.071429`.
  - `GAME-0057`: `1 / 14 = 0.071429`; `GAME-0058`: `1 / 15 = 0.066667`; `GAME-0059`: `1 / 13 = 0.076923`; `GAME-0060`: `1 / 13 = 0.076923`; `GAME-0061`: `1 / 16 = 0.062500`; `GAME-0062`: `1 / 14 = 0.071429`; `GAME-0063`: `1 / 13 = 0.076923`; `GAME-0064`: `1 / 11 = 0.090909`.
  - `GAME-0065`: `0 / 14 = 0.000000`; `GAME-0066`: `0 / 17 = 0.000000`; `GAME-0067`: `0 / 15 = 0.000000`; `GAME-0068`: `0 / 15 = 0.000000`; `GAME-0069`: `1 / 14 = 0.071429`; `GAME-0070`: `1 / 14 = 0.071429`; `GAME-0071`: `1 / 13 = 0.076923`; `GAME-0072`: `1 / 14 = 0.071429`.
  - `GAME-0073`: `1 / 13 = 0.076923`; `GAME-0074`: `1 / 15 = 0.066667`; `GAME-0075`: `1 / 15 = 0.066667`; `GAME-0076`: `1 / 13 = 0.076923`; `GAME-0077`: `1 / 13 = 0.076923`; `GAME-0078`: `1 / 13 = 0.076923`; `GAME-0079`: `1 / 13 = 0.076923`; `GAME-0080`: `1 / 13 = 0.076923`.
  - `GAME-0081`: `1 / 14 = 0.071429`; `GAME-0082`: `1 / 14 = 0.071429`; `GAME-0083`: `1 / 14 = 0.071429`; `GAME-0084`: `1 / 16 = 0.062500`; `GAME-0085`: `0 / 18 = 0.000000`; `GAME-0086`: `1 / 19 = 0.052632`; `GAME-0087`: `2 / 15 = 0.133333`; `GAME-0088`: `1 / 15 = 0.066667`.
  - `GAME-0089`: `1 / 15 = 0.066667`; `GAME-0090`: `2 / 20 = 0.100000`; `GAME-0091`: `4 / 12 = 0.333333`; `GAME-0092`: `2 / 15 = 0.133333`; `GAME-0093`: `2 / 14 = 0.142857`; `GAME-0094`: `3 / 14 = 0.214286`; `GAME-0095`: `3 / 16 = 0.187500`; `GAME-0096`: `3 / 14 = 0.214286`.
  - `GAME-0097`: `4 / 11 = 0.363636`.

## Coverage decision

- Reuse direct navigation, complete current local visibility,
  designated-location arrival and real-time scheduling.
- Add only the missing boundaries: continuous hyperbolic pose integration,
  order-five square incidence and metric-consistent curvature rendering.
- Do not promote the route mnemonic, maze name, crystal shape or unusual art
  direction into genes.

## Confidence and open questions

### Assumptions

- The order-five square control is a bounded analytic witness for the game's
  documented hyperbolic construction, not a claim that every visible maze wall
  follows one exposed square edge.
- The speedrun route is used only to reproduce the intersection sequence;
  speed tactics and reset shortcuts remain excluded.

### Unknowns

- Production curvature radius, coordinate representation, collision solver,
  numerical recentering and VR comfort transforms were not measured.
- The exact point at which the crystal autosave resolves and whether later
  versions changed incidental maze props are not material to the genome.

### Confidence

- High for continuous hyperbolic traversal and the official spatial
  consequences; high for the fixed route; medium-high for the exact maze-end
  hexahedron corroboration.

## Combination candidate

- Candidate ID: `COMB-0098`.
- Gene set: `ACT-008`, `SYS-130`, `CON-149`, `INF-048`, `OBJ-026`.
- Supporting game: `GAME-0098`.
- Proper-subset rationale: complete local visibility and real-time scheduling
  support execution but do not define the curved-route decision structure.
- Novelty claim: not assessed.

## Outcome

- Reused genes: `ACT-008`, `INF-001`, `OBJ-026`, `TIM-003`.
- Added genes: `SYS-130`, `CON-149`, `INF-048`.
- Added combination: `COMB-0098`.
- Evidence gate: passed with one official product record, one creator technical
  devlog, one maintained route, one community location record, one independent
  mathematical reference and one executable verifier.
- Nearest prior genome: Antichamber at `4 / 11 = 0.363636`.
- Next falsification target: HyperRogue, to test discrete hyperbolic adjacency
  against Hyperbolica's continuous curved pose.

## Taxonomy impact

- Curved metric integration is separated from camera projection, teleportation,
  periodic wrap and authored adjacency replacement.
- A topological incidence constraint is separated from its visual presentation:
  `CON-149` governs available local geometry while `INF-048` governs what the
  player can continuously perceive about it.
- The next game can reuse the incidence rule without automatically inheriting
  the continuous first-person system.

## Negative results

- `SYS-129` and `CON-148` are absent because no off-screen doorway remap is
  required.
- `SYS-126` is absent because traversal crosses no fixed repeating-cell seam.
- `SYS-059` is absent because there are no paired apertures.
- `ACT-095` and `SYS-121` are absent because camera projection does not create
  a screen-space path.
- No randomness, teleport, map-memory or speedrun-reset gene is introduced.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Hyperbolica офіційно описує безперервний
  гіперболічний простір з експоненційним ростом і неевклідовим лабіринтом
  (`HYP-002`, `HYP-003`).
- [Confirmed | Corroborated | High] Відтворюваний маршрут Maze of Apeirogon
  має одинадцять фіксованих рішень і завершується кристалом (`HYP-005`,
  `HYP-006`).

## Нові гени

- `SYS-130` відокремлює безперервну позу в метриці сталої від’ємної кривини
  від teleport, periodic wrap і camera-only projection.
- `CON-149` фіксує метричне правило `{4,5}` з п’ятьма квадратами навколо
  вершини.
- `INF-048` фіксує живе відображення кривої відстані й напряму тією самою
  геометрією, що керує рухом.

## Нові комбінації

- `COMB-0098` поєднує безперервну навігацію, гіперболічне інтегрування,
  order-five incidence, curvature cues і прибуття до кристала.

## Зміни таксономії

- Просторову кривину розкладено на автоматичне метричне інтегрування,
  обмеження локальної інцидентності та інформаційне відображення; вони можуть
  перевикористовуватися незалежно.
- HyperRogue обрано наступним контрольним випадком, щоб перевірити перенесення
  дискретної інцидентності без автоматичного успадкування `SYS-130`.
