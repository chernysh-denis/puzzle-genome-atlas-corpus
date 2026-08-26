---
game_id: GAME-0094
slug: superliminal
game_title: Superliminal
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0094
gene_ids:
  action:
    - ACT-008
    - ACT-048
  system:
    - SYS-036
    - SYS-061
    - SYS-124
  constraint:
    - CON-145
  information:
    - INF-001
    - INF-044
  objective:
    - OBJ-022
  time:
    - TIM-003
---

# Game: Superliminal

## Analysis scope

- Version / ruleset: Pillow Castle's 2019 base game, bounded to the Induction
  room in which one chess piece is taken through the left opening, aimed toward
  the opposite side, dropped onto the pressure plate and left there while the
  sole player character passes through the linked exit. A one-dimensional
  executable control isolates the same pickup-to-sightline-to-scale-to-plate
  chain with two background depths.
- Included: first-person walking; one portable rigid chess piece; pickup;
  camera-sightline aiming while held; constant projected extent; proportional
  physical rescaling with camera depth; farthest collision-free placement;
  live held-pose feedback; release; gravity and collision; occupancy-sustained
  plate and exit; fixed room exit; real-time simulation.
- Excluded: the rest of Induction; cheese ramps, boxes and movable signs;
  rotation input; trompe-l'œil projection; cloning; portals and player scaling;
  Dollhouse, Labyrinth, Whitespace and later chapters; collectibles, developer
  commentary mode, challenge mode, multiplayer, level editor, story,
  achievements and platform-specific control assistance.
- Direct-play status: not conducted. Pillow Castle's press kit and Steam page
  establish the first-person forced-perspective premise. Graphics programmer
  Phil Fortier and game director Albert Shih directly establish invariant
  screen extent, proportional world scale, farthest collision-free depth and
  footprint ray sampling. A creator interview and two independent walkthroughs
  corroborate the bounded chess-piece / plate / exit sequence. The local
  control proves a normalised sightline model, not production geometry.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SUP-001` | Superliminal is Pillow Castle's 2019 first-person puzzle built around forced perspective and depth ambiguity | Confirmed | Direct | High | P1, P2 |
| `SUP-002` | A held object keeps the same apparent screen size while its physical distance and scale change | Confirmed | Direct | High | P3, P4 |
| `SUP-003` | Doubling held-object distance doubles physical scale, preserving the pickup projection | Confirmed | Direct | High | P3, P4 |
| `SUP-004` | The system continually chooses the farthest placement that remains physically collision-free | Confirmed | Direct | High | P3, P4 |
| `SUP-005` | Dense rays sample the visible object surface against irregular background geometry rather than testing one centre ray | Confirmed | Direct | High | P3, P4 |
| `SUP-006` | Release commits the currently previewed object as a physically enlarged or reduced collidable body | Confirmed | Direct | High | P3, P4 |
| `SUP-007` | The scoped Induction room requires moving one chess piece from the left opening onto the opposite pressure plate | Confirmed | Corroborated | High | S1, S2, A1 |
| `SUP-008` | Plate occupancy holds the linked door open; taking the piece away returns the door to its closed state | Confirmed | Corroborated | High | A1, S1, V1 |
| `SUP-009` | The room completes by leaving the piece on the plate and walking the sole controlled character through the fixed exit | Confirmed | Corroborated | High | S1, S2, V1 |
| `SUP-010` | The control preserves one apparent extent across near and far backstops while producing a more-than-fourfold final world scale | Observation | Direct | High | V1, SUP-002–SUP-005 |
| `SUP-011` | The control rejects an interpenetrating far-wall pose, a non-overlapping near release and exit traversal after plate vacancy | Observation | Direct | High | V1, SUP-004, SUP-008 |
| `SUP-012` | Superliminal retains and resizes one existing object; it neither stamps image geometry like Viewfinder nor rewires nodes like Monument Valley | Observation | Corroborated | High | P3, GAME-0041, GAME-0093 |
| `SUP-013` | No random transition, finite consumable, turn boundary or automatic route choice changes the scoped decision | Observation | Corroborated | High | P3, P4, S1, V1 |

## Basic data

- Release / origin: Pillow Castle developed and published Superliminal,
  launching the original PC release in November 2019; later platform releases
  and added modes are outside the bounded record.
- Platform or physical form: single-player first-person three-dimensional
  puzzle simulation with held objects whose physical scale is governed by
  their camera-relative projection.
- Puzzle family: collision-bounded forced-perspective object rescaling.
- Primary and creator sources:
  - **[P1]** [Pillow Castle press kit](https://pillowcastle.org/presskits/superliminal/),
    for developer, 2019 launch, forced perspective, depth ambiguity and
    manipulation of objects in physical space according to perspective.
  - **[P2]** [Pillow Castle's Steam product record](https://store.steampowered.com/app/1049410/Superliminal/),
    for the first-person impossible-puzzle premise and the use of depth and
    perspective to escape the dream world.
  - **[P3]** [PlayStation Blog — Breaking down the tech behind Superliminal](https://blog.playstation.com/2020/06/30/breaking-down-the-tech-behind-superliminals-mind-bending-illusions/),
    by Pillow Castle graphics programmer Phil Fortier, for constant apparent
    size, small-to-giant chess-piece release, continuous farthest valid
    placement, dense visible-surface raycasts and changed physical properties.
  - **[P4]** [Game Developer — Designing the mind-bending perspective puzzles of Superliminal](https://www.gamedeveloper.com/design/designing-the-mind-bending-perspective-puzzles-of-i-superliminal-i-),
    reporting lead designer Albert Shih's proportional distance / size rule,
    collision-bounded farthest placement, dense raycast solution and discrete-
    state design rationale.
- Reproducible corroboration:
  - **[S1]** [Pro Game Guides — Superliminal walkthrough](https://progameguides.com/superliminal/superliminal-walkthrough-full-guide/),
    for taking the chess piece through the left opening, placing it on the
    pressure plate in the opposite opening and continuing through the door.
  - **[S2]** [TrueAchievements — Superliminal story walkthrough](https://www.trueachievements.com/game/Superliminal/walkthrough/3),
    for the Induction chess-piece transfer and pressure-button progression.
  - **[A1]** [Transcription of Superliminal's creator commentary](https://superliminal.fandom.com/wiki/Developer_Commentary),
    used as a specialist secondary record for the opposite-wall chess room,
    plate-key design and the production proportional-scaling explanation.
  - **[V1]**
    [`verify_superliminal_control.py`](../../../scripts/verify_superliminal_control.py),
    an executable two-backstop model of projection preservation, proportional
    world scaling, collision clearance, plate occupancy and six rejected
    invalid transitions.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. The player directly walks the sole
  first-person character between the two openings and through the fixed exit.
- `ACT-048` — pick up and release portable rigid object. The chess piece is one
  retained body: the player takes it, aims while it remains held and releases
  it back into the current physical room.
- A separate abstract size action is absent. The player changes view direction
  and available background depth; `SYS-124` derives scale continuously from
  that sightline rather than accepting a number or size category.

### System Behaviour Genes

- `SYS-036` — continuous force-constrained body dynamics. The released piece
  falls, collides and rests at its committed physical dimensions while player
  movement remains live.
- `SYS-061` — occupancy-sustained linked mechanism state. The eligible piece
  holds the plate and door active only while its collision body occupies the
  pressure region.
- `SYS-124` — perspective-preserving collision-bounded object rescaling. While
  held, the system maximises collision-free depth along the camera sightline
  and changes world scale proportionally so the chess piece retains its pickup
  screen extent. Release preserves the resulting world pose and scale.
- Resolution order: acquire the visible piece; retain pickup projection; sample
  its visible footprint toward the aimed background; choose the farthest
  collision-free depth; derive proportional scale; render the live physical
  candidate; release; resolve gravity and collision; evaluate plate occupancy;
  update the door; accept direct exit traversal.

### Constraint Genes

- `CON-145` — held perspective placement must remain collision-free. A
  candidate object may grow only at a depth where its complete sampled volume
  clears the blocking background. A centre point behind or inside the wall is
  not a legal release pose.
- The pressure plate is a separate physical target. Preserving screen extent
  does not guarantee plate overlap; camera direction and background choice
  determine whether the committed footprint actually occupies it.
- Scarce strategic resources: none consumed. The chess piece remains reusable
  and can be picked up again, which also removes plate occupancy.

### Information Genes

- `INF-001` — fully visible current state. The bounded decision exposes the
  piece, openings, current held pose, plate, linked door and local exit path.
- `INF-044` — live perspective-held physical placement preview. The rendered
  chess piece is the current pending collidable pose and scale. Its apparent
  extent remains stable, while background relation, shading and overlap expose
  where the enlarged body will exist after release.
- No numeric size or depth value is required or shown by this classification;
  the sightline preview itself is the decision-bearing information.

### Objective Genes

- `OBJ-022` — evacuate every required controlled actor through fixed exits.
  The sole dreamer must leave the chess piece sustaining the plate and walk
  through the now-open fixed room exit.
- Plate activation is a prerequisite, not a separate terminal score or
  collectible objective.

### Time Genes

- `TIM-003` — real-time input during forced progression. Camera motion updates
  the held pose continuously, released bodies fall under live physics, and the
  player moves while the plate-door relation remains active.
- There is no authored deadline in the scoped room, but absence of a deadline
  does not make the live physics sequence turn-based or self-paced atomic.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Chess piece rests at distance `2`, scale `1` | pick it up | the held projection ratio becomes `1 / 2` | pickup fixes apparent extent | `SUP-002`, `SUP-003` |
| Held ratio is `0.5`; near backstop is at `5` | aim at the near surface | the control chooses centre depth `4.444…`, scale `2.222…`, and a far edge exactly at `5` | proportional collision-bounded preview | `SUP-003`–`SUP-005`, `SUP-010` |
| Same held ratio; far backstop is at `10` | aim at the far surface | centre depth becomes `8.888…`, scale `4.444…`, while apparent extent remains `0.5` | distance changes physical scale, not screen extent | `SUP-002`–`SUP-005`, `SUP-010` |
| Far wall is at `10` | force centre depth `10` at preserved projection | enlarged half-extent pushes the far edge to `11.25`; the pose is rejected | collision clearance governs depth | `SUP-004`, `SUP-005`, `SUP-011` |
| Preview remains at the near backstop | release toward the remote plate | no target overlap exists and the plate action is rejected | visual resizing alone is not success | `SUP-007`, `SUP-011` |
| Far preview overlaps the plate | release | the enlarged piece becomes a physical body, settles on the plate and opens the linked door | committed scale plus occupancy | `SUP-006`–`SUP-008` |
| Door is open | pick the piece up again | plate occupancy ends and the door closes | linked state is sustained, not latched | `SUP-008`, `SUP-011` |
| Piece is replaced on the plate | walk through the exit | the door stays open and the sole required actor completes the bounded room | fixed-exit objective | `SUP-009` |

The executable control separately rejects aiming or releasing before pickup,
entering the initially closed exit, forcing the interpenetrating far-wall pose,
crediting a near non-overlapping release and entering after the piece is removed
from the plate. Its analytic clearance equation is deliberately simpler than
the production multi-ray object-shape solver.

## Strategic and experiential structure

- Local decision: select a background depth and sightline that produce a useful
  physical size while placing the piece's pending footprint over the plate.
- Medium-term planning: distinguish apparent size from committed world size;
  the piece must remain on the target while the avatar takes the separate exit.
- Long-term structure: later chapters reuse scale alongside projection,
  cloning, portals and player-size changes, all excluded from this minimal
  packet.
- Common heuristics: pick up a known movable object; aim toward a distant clean
  background to enlarge it; watch target overlap rather than apparent size;
  release only when the candidate clears geometry; do not retrieve a required
  plate occupant before crossing.
- Failure attribution: rejection follows current collision clearance, target
  overlap or plate occupancy, not randomness.
- Player-trust factors: the held silhouette, collision boundary, release pose,
  resting body, plate state and door state must agree continuously.

## Replay and variation

- What changes between rooms: object shape, available background depth, target,
  required size, orientation, traversal use and later illusion family.
- Randomness or procedural generation: none in the scoped authored room.
- Multiple viable strategies: the continuous sightline admits a tolerance
  region of physical poses; the causal requirement remains plate occupancy.
- Typical replay motive: revisit perceptual transformations, developer
  commentary, collectibles, challenge targets or later multiplayer/editor
  content outside this record.

## Adjacent systems and history

- Portal is the nearest complete genome. Both directly move one avatar and one
  portable physical object, simulate gravity, use sustained plate occupancy and
  end through a fixed exit. Portal's cube retains its size at a controlled
  offset; Superliminal derives physical scale and depth from the camera image.
- Viewfinder also uses first-person perspective, live physics and a fixed exit,
  but commits a held 2D image that instantiates and destructively overwrites
  geometry. Superliminal retains one existing rigid body and changes its scale.
- Fez changes a global cardinal collision frame around fixed triles.
  Superliminal keeps ordinary first-person perspective and changes the held
  object's physical pose every frame.
- Monument Valley physically rotates one marked architecture component to a
  snap pose, then rebuilds a navigation graph. Superliminal has no snap graph
  or automatic destination route.
- Bonfire Peaks shares portable rigid-object handling, but its crate retains a
  fixed footprint in a discrete spatial grammar.

## Normalised genome

| Type | IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048` | direct first-person movement; take, aim and release one chess piece |
| System | `SYS-036`, `SYS-061`, `SYS-124` | live physics; sustained plate; projection-preserving physical rescale |
| Constraint | `CON-145` | candidate volume must clear sampled background geometry |
| Information | `INF-001`, `INF-044` | visible room state; exact live pending physical pose |
| Objective | `OBJ-022` | move the sole actor through the fixed opened exit |
| Time | `TIM-003` | live held-pose updates and body physics |

Compact signature:

`ACT-008,ACT-048; SYS-036,SYS-061,SYS-124; CON-145; INF-001,INF-044; OBJ-022; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `93` (`GAME-0001`–`GAME-0093`).
- Exact genome matches: none.
- Tied near matches: `GAME-0033` — Portal (`7 / 16 = 0.437500`).
- Supported combination subsets: `COMB-0094`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0033`.

## Coverage decision

- Reuse direct navigation, portable rigid-object handling, live body physics,
  sustained pressure mechanisms, visible state, fixed-exit completion and
  real-time progression.
- Add only the missing causal boundaries: projection-preserving physical
  rescaling, collision-bounded held placement and exact live pose preview.
- Keep camera-only topology, image instantiation, snap-state architecture,
  global scale and later Superliminal illusion families outside the packet.

## Confidence and open questions

### Assumptions

- The control treats the chess piece as one symmetric bounded volume and uses
  one analytic backstop; production samples arbitrary visible surfaces with
  many rays and shape-specific collision.
- The walkthrough descriptions identify the same ordinary Induction room
  across releases despite later controller assistance and added modes.

### Unknowns

- Production ray density, safety margin, concavity approximation, release
  impulse and plate collider tolerance were not measured.
- Whether the exact retail piece must change size materially before the plate
  accepts it is not claimed; the scoped gene requires the available resizing
  system and the control proves its causal distinction.

### Confidence

- High for constant projected extent, proportional scale, farthest valid
  placement, physical release and the chess-piece / plate / exit sequence.
- Medium-high for exact production plate-reversal timing because it is
  corroborated by creator commentary and ordinary pressure-plate behaviour but
  not instrumented directly.

## Combination candidate

- Candidate ID: `COMB-0094`.
- Gene set: `ACT-048`, `SYS-061`, `SYS-124`, `CON-145`, `INF-044`, `OBJ-022`.
- Supporting game: `GAME-0094`.
- Proper-subset rationale: direct avatar navigation, generic world visibility,
  body physics and live scheduling support execution but do not define the
  perspective-resize-to-sustained-exit interaction.
- Novelty claim: not assessed.

## Outcome

- Reused genes: `ACT-008`, `ACT-048`, `SYS-036`, `SYS-061`, `INF-001`,
  `OBJ-022`, `TIM-003`.
- Added genes: `SYS-124`, `CON-145`, `INF-044`.
- Added combination: `COMB-0094`.
- Evidence gate: passed with two Pillow Castle records, two developer technical
  accounts, two independent walkthroughs, one creator-commentary transcription
  and one executable verifier.
- Nearest prior genome: Portal; see `Corpus comparison` for the current result.
- Next falsification target: a game that changes the player's gravity frame or
  repeats world space without deriving object scale from a held projection.

## Taxonomy impact

- A held object's persistent physical rescaling is separated from camera zoom,
  global world scaling and image-instantiated geometry.
- The player's sightline is a parameter of ordinary rigid-object handling; the
  system-owned projection-to-scale transform is the new behaviour.
- Live preview is separated from post-release observation because it exposes
  the exact collision-bounded candidate before commitment.

## Negative results

- No structured negative-result record added. The comparison rejects merging
  Superliminal with Viewfinder, Fez, Echochrome or Monument Valley solely
  because all use perspective.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Утримувана фігура зберігає екранний розмір, а
  система пропорційно змінює її фізичний масштаб і ставить у найдальшу
  безколізійну позу (`SUP-002`–`SUP-006`).
- [Confirmed | Corroborated | High] Фігура на плиті утримує вихід відкритим,
  доки єдиного керованого персонажа не проведено крізь нього (`SUP-007`–`SUP-009`).

## Нові гени

- [Observation | Direct | High] `SYS-124` — перспективно-сталий collision-
  bounded фізичний ресайз об'єкта.
- [Observation | Direct | High] `CON-145` — утримувана перспективна поза має
  лишатися безколізійною.
- [Observation | Direct | High] `INF-044` — живий preview майбутньої фізичної
  пози й масштабу.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0094` — перетворити глибину погляду
  на фізичний масштаб, утримати плиту й відкрити фіксований вихід.

## Зміни таксономії

- [Observation | Direct | High] Нові межі відділяють ресайз наявного тіла від
  створення геометрії з картинки та зміни глобального кадру.

## Нові питання

- Яка точна production-похибка між raycast-кандидатом і collider-позою на
  нерівному тлі?
- Як різні форми з отворами змінюють sampling і максимальну допустиму глибину?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] Manifold Garden.
- Optimisation criterion: isolate player-commanded gravity-frame changes and
  translationally repeating world space after four perspective-heavy games.
- Expected information gain: distinguish changing gravity and recursive
  spatial wrap from held-object scale, camera topology and snap architecture.
- Backlog impact: retain Maquette as a later direct scale-recursion comparator;
  move Manifold Garden to `GAME-0095`.

## Чому саме вона

- [Hypothesis | Limited | Medium] Manifold Garden should reuse direct
  first-person navigation and live physics while replacing sightline-derived
  object scale with a discrete gravity orientation and repeating geometry,
  making it a strong falsification target rather than another cosmetic
  perspective example.
