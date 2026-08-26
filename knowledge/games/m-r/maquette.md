---
game_id: GAME-0096
slug: maquette
game_title: Maquette
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0096
gene_ids:
  action:
    - ACT-008
    - ACT-048
  system:
    - SYS-036
    - SYS-127
    - SYS-128
  constraint:
    - CON-147
  information:
    - INF-001
    - INF-046
  objective:
    - OBJ-022
  time:
    - TIM-003
---

# Game: Maquette

## Analysis scope

- Version / ruleset: Graceful Decay's original 2021 release, bounded to the
  closing “Entering the House” sequence of the chapter “The Maquette”, with
  the preceding red-block lesson retained as a control. The packet starts with
  the golden key available: use it on the locked route door, place it across a
  gap in the central model so its larger counterpart becomes a bridge, cross
  to the overlook, return the key to normal scale, leave it outside the dome,
  collect its tiny model representation, unlock the spawned house, restore a
  bridge-sized representation and enter the house.
- Included: first-person walking; one central small model and its normal and
  outer homologous scales; one authoritative object pose propagated across
  visible scale instances; pickup and release of reachable rigid objects;
  avatar-relative pickup-size limits; carrying one object across adjacent
  recursion layers; scale reindexing without identity replacement; the golden
  key as key and traversable bridge; fixed house exit; live physics.
- Excluded: The Gardens, The Gateways and later chapters; ticket, fair,
  fortune-teller and narrative scenes except as route provenance; later
  player-scale changes, darkness, shattered worlds, moving whole recursive
  environments, achievements, speedrun paths, platform hints and adaptive
  trigger presentation.
- Direct-play status: not conducted. The creator's PlayStation explanation
  establishes simultaneous same-world instances, bidirectional state updates
  and size-relative manipulation. Two creator interviews establish copied
  physical motion and carrying objects between scales. A reproducible chapter
  walkthrough fixes the exact key / bridge / tiny-key / house order. The local
  control proves a three-level ratio model, not production coordinates,
  collider dimensions, physics interpolation or recursion depth.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MAQ-001` | Maquette launched in 2021 as a first-person recursive puzzle by Graceful Decay and Annapurna Interactive | Confirmed | Direct | High | P1, P2 |
| `MAQ-002` | The small model and surrounding world are simultaneous instances of one recursively nested world, not independent scenes | Confirmed | Direct | High | P2, P3 |
| `MAQ-003` | Moving or opening one instance propagates the same state to its homologous instances at other scales | Confirmed | Direct | High | P2–P4 |
| `MAQ-004` | An object too large to manipulate at normal scale can be moved through its smaller model representation | Confirmed | Direct | High | P2, P4, S1 |
| `MAQ-005` | Carrying an object from one world scale into another makes the same object accessible at a different relative size | Confirmed | Direct | High | P3, P4 |
| `MAQ-006` | In the scoped chapter, placing the golden key across the model gap produces a traversable large-scale key bridge | Confirmed | Direct | High | P3, S1 |
| `MAQ-007` | Leaving the key outside the dome exposes a tiny model key that opens the house; restoring the key bridge then permits entry | Confirmed | Direct | High | S1 |
| `MAQ-008` | The control keeps one object identity across inner, normal and outer representations at a fixed ratio | Observation | Direct | High | V1, MAQ-002–MAQ-005 |
| `MAQ-009` | The control rejects an oversized pickup, nonadjacent transfer, wrong bridge scale or pose and entry before both prerequisites | Observation | Direct | High | V1 |
| `MAQ-010` | Maquette's scale follows recursion-layer transfer rather than camera depth, periodic translation or mutable containment parentage | Observation | Corroborated | High | P2–P4, GAME-0036, GAME-0094, GAME-0095 |

## Basic data

- Release / origin: Graceful Decay developed Maquette; Annapurna Interactive
  published the original PC, PlayStation 4 and PlayStation 5 release on
  2 March 2021.
- Platform or physical form: single-player first-person three-dimensional
  traversal puzzle in a live recursive physical world.
- Puzzle family: recursive same-state propagation and cross-scale object
  reindexing.
- Primary and creator sources:
  - **[P1]** [Maquette on Steam](https://store.steampowered.com/app/762840/Maquette/),
    for developer, publisher, date, first-person format and simultaneously tiny
    and huge recursive world.
  - **[P2]** [PlayStation Blog — The recursive world simulation & puzzle-making process in Maquette](https://blog.playstation.com/2020/07/01/the-recursive-world-simulation-puzzle-making-process-in-maquette/),
    by creative director Hanford Lemoore, for one world in simultaneous nested
    instances, bidirectional door state and moving a large object through its
    small representation.
  - **[P3]** [Push Square — interview with Maquette creative director](https://www.pushsquare.com/news/2021/03/interview_maquettes_creative_director_on_building_a_recursive_world_puzzle_game_for_ps5),
    for copied physical motion at different scale and seamless carrying between
    scales, including the key-as-bridge example.
  - **[P4]** [TheXboxHub — interview with Hanford Lemoore](https://www.thexboxhub.com/an-interview-within-an-interview-with-hanford-lemoore-maker-of-maquette/),
    for one model / normal / outer world, oversized-object access through a
    smaller scale and deliberate scale change by moving an object between
    worlds.
- Reproducible corroboration:
  - **[S1]** [PlayStation Universe — The Maquette walkthrough](https://www.psu.com/news/maquette-the-maquette-walkthrough-and-puzzle-solutions/),
    for the red-block control and exact golden-key bridge, tiny-key unlock,
    restored bridge and house-entry sequence.
  - **[S2]** [80 Level — The Story and Development of Maquette](https://80.lv/articles/the-story-and-developement-of-maquette),
    for Lemoore's prototype account of a carried small-world object producing a
    giant counterpart and the need for visually recognisable homologous
    architecture.
  - **[V1]**
    [`verify_maquette_control.py`](../../../scripts/verify_maquette_control.py),
    an executable three-layer object-identity control with six rejected invalid
    transitions.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. The player walks between the dome,
  doors, gap and house and crosses the solid key bridge by direct first-person
  steering.
- `ACT-048` — pick up and release portable rigid object. The player repeatedly
  lifts, carries and places the golden key or its reachable scaled
  representation; its recursion behaviour does not make carrying a remote
  board move.

### System Behaviour Genes

- `SYS-036` — continuous force-constrained body dynamics. Released objects
  settle and remain collidable, and the avatar walks over the bridge while live
  collision and gravity continue.
- `SYS-127` — recursive homologous-instance state propagation. The model,
  normal courtyard and surrounding larger world expose scale-transformed
  representations of one authoritative state; moving one representation
  updates the homologous pose at every rendered recursion level.
- `SYS-128` — cross-layer carried-object scale reindexing. Carrying a reachable
  representation across an adjacent nested-world boundary changes which scale
  exponent is ordinary for the avatar while retaining object identity and
  state, so the golden key can become tiny, standard or bridge-sized.
- Resolution order: acquire a reachable representation; preserve its identity;
  update the canonical pose; propagate scale-transformed poses to homologous
  instances; if a recursion boundary was crossed, reindex the scale exponent;
  resolve collision; test key compatibility or bridge span; then test the
  unlocked-house and traversable-gap exit prerequisites.

### Constraint Genes

- `CON-147` — rigid-object pickup requires avatar-relative manageable scale. A
  representation larger than the current pickup envelope cannot be acquired,
  although a homologous smaller representation of that same object can be.
- Scale instances cannot diverge independently: moving the small red block
  while keeping the large gate blocker in place is not a legal state.
- Only adjacent recursion layers are crossed by one carried transfer in the
  bounded control; skipping directly from inner to outer is rejected.
- Scarce strategic resources: the golden key is persistent and reusable. It is
  neither consumed by the door nor duplicated into independently spendable
  copies.

### Information Genes

- `INF-001` — fully visible current state. The relevant dome, model, homologous
  courtyard, key pose, gaps, doors and house are inspectable before each move.
- `INF-046` — simultaneous nested-scale correspondence display. Recognisable
  architecture and object silhouettes show the model and surrounding worlds
  together as scale-transformed instances, so a change in one can be matched
  to its causally linked counterpart without a hidden layer selector.
- No numeric scale label is required. The geometry itself communicates which
  representation is manageable, lock-sized or bridge-sized.

### Objective Genes

- `OBJ-022` — evacuate every required controlled actor through fixed exits.
  The sole avatar must unlock the spawned house, restore the key bridge across
  its fixed approach gap and enter the house to end the bounded chapter.
- The overlook is an intermediate route location; it is not a collectible,
  score target or alternate terminal objective.

### Time Genes

- `TIM-003` — real-time input during forced progression. Carry pose, gravity,
  collision and avatar movement update continuously while the player walks,
  lifts, reindexes, places and crosses the key.
- There is no authored deadline in the packet. Live spatial simulation rather
  than time pressure distinguishes it from atomic board turns.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Red block is too large at normal scale but reachable in the model | move its inner representation to the courtyard corner | every homologous block pose changes and the normal garden entrance clears | small-scale access changes one authoritative state | `MAQ-003`, `MAQ-004` |
| Standard golden key is available; route door is locked | carry the key to the matching door | door unlocks while the persistent key remains available | key is reusable route equipment | `MAQ-006` |
| Full-size gap is unbridgeable | place the key across the homologous model gap | its large representation aligns across the normal-world gap | same-state propagation creates traversable geometry | `MAQ-003`, `MAQ-006` |
| Large key spans the gap | walk across it | avatar reaches the overlook | propagated object state is physically authoritative | `MAQ-006` |
| Key representation is accessible in the model | carry it out and leave the standard key outside the dome | a tiny homologous key appears at the corresponding model location | crossing scale restores a different accessible exponent | `MAQ-005`, `MAQ-007` |
| Tiny key is reachable; house is locked | carry the tiny key to the house lock | house door unlocks without creating an independent key identity | reindexed scale satisfies a size-specific fixture | `MAQ-005`, `MAQ-007` |
| House is open but approach gap remains | return the key through the model and align its large representation across the gap | same key becomes a traversable bridge again | scale reindexing is reversible and identity-preserving | `MAQ-005`, `MAQ-007` |
| House is open and bridge aligned | cross and enter | sole required avatar leaves the bounded chapter | fixed-exit completion requires both states | `MAQ-007` |

The executable control uses ratio `4` across inner, normal and outer layers.
It separately rejects normal-scale red-block pickup, giant-key pickup,
nonadjacent transfer, an undersized bridge, a wrong bridge pose and locked-house
entry. It deliberately omits retail collision meshes, animations, audio delay,
story triggers and arbitrary recursion depth.

## Strategic and experiential structure

- Local decision: choose which visible representation of the same object is
  currently manipulable and where its homologous pose will land.
- Medium-term planning: preserve the one key through door use, bridge use and
  scale transfer; unlock state and bridge state must coexist at the end.
- Long-term structure: later chapters change the player's scale, displace whole
  recursive worlds and weaken familiar correspondence, all excluded here.
- Common heuristics: compare distinctive architecture across the dome; if an
  object is too large, seek its smaller homolog; place bridge candidates in the
  model, then inspect the surrounding gap; treat scale transfer as reindexing,
  not duplication.
- Failure attribution: pickup rejection follows relative size; route failure
  follows pose, span or lock state rather than randomness.
- Player-trust factors: silhouette, pose, orientation, collision and timing
  must agree across every visible representation.

## Replay and variation

- The bounded route is deterministic. Variation comes from object approach,
  placement tolerance and the order in which corresponding scales are
  inspected.
- The key can be placed at many irrelevant poses, but only the authored gap and
  lock relations complete the causal packet.
- There is no procedural layout or random object scale in scope. The fixed
  recursion ratio makes mistakes reproducible.
- Accessibility-relevant variance includes input device and PS5 trigger
  feedback; neither changes the classified state propagation.

## Adjacent systems and history

- Superliminal changes one held object's physical scale from camera depth and
  a collision-bounded sightline. Maquette changes relative scale by moving one
  identity across nested world layers; the camera is not authoritative.
- Patrick's Parabox reparents enterable containers in a mutable containment
  graph. Maquette's homologous worlds remain fixed scale instances and share
  object state rather than changing parent ownership.
- Manifold Garden translates a body across a periodic boundary while
  preserving its scale and local pose. Maquette propagates one canonical pose
  to simultaneously visible representations at different scales.
- Viewfinder instantiates replacement 3D geometry from a committed image.
  Maquette retains one persistent physical object identity.
- The red-block lesson resembles remote manipulation, but it has no detached
  control panel: the small block is a physical homolog inside the same world.

## Normalised genome

| Gene type | IDs | Scope meaning |
|---|---|---|
| Action | `ACT-008`, `ACT-048` | walk and carry the current reachable key representation |
| System Behaviour | `SYS-036`, `SYS-127`, `SYS-128` | live bodies, recursive pose propagation, scale reindexing |
| Constraint | `CON-147` | pickup depends on avatar-relative representation size |
| Information | `INF-001`, `INF-046` | visible route and recognisable simultaneous scale correspondence |
| Objective | `OBJ-022` | unlock, bridge and enter the fixed house exit |
| Time | `TIM-003` | live carrying, collision and traversal |

Full signature:
`ACT-008,ACT-048; SYS-036,SYS-127,SYS-128; CON-147; INF-001,INF-046; OBJ-022; TIM-003`.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `95` (`GAME-0001`–`GAME-0095`).
- Exact genome matches: none.
- Tied near matches: `GAME-0094` — Superliminal (`6 / 14 = 0.428571`).
- Supported combination subsets: `COMB-0096`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0094`.

## Coverage decision

- Reuse direct navigation, rigid-object carrying, live body physics, complete
  current-state visibility, fixed-exit completion and real-time scheduling.
- Add only the missing recursive causal boundaries: homologous-instance state
  propagation, cross-layer scale reindexing, relative-size pickup eligibility
  and visible scale correspondence.
- Keep perspective-derived scaling, periodic translation, mutable containment,
  image instantiation and later whole-world transformations outside the packet.

## Confidence and open questions

### Assumptions

- The control uses a constant ratio of four between adjacent layers; production
  may use a different ratio or presentation-dependent limits.
- The red-block control and house route are joined because creator sources
  explicitly teach them as consequences of the same recursive simulation.

### Unknowns

- Exact retail scale ratio, pickup volume, bridge-span tolerance, propagation
  interpolation, recursion culling and collision ownership were not measured.
- Whether the golden key door animation briefly suppresses a homologous
  representation is not classified; persistent identity is established by its
  immediate reuse after unlocking.

### Confidence

- High for simultaneous instances, bidirectional propagation, size-relative
  pickup, cross-scale carry and the walkthrough's key sequence.
- Medium-high for the normalised “scale exponent” implementation model because
  creator evidence proves the observable rule but not production data layout.

## Combination candidate

- Candidate ID: `COMB-0096`.
- Gene set: `ACT-048`, `SYS-127`, `SYS-128`, `CON-147`, `INF-046`, `OBJ-022`.
- Supporting game: `GAME-0096`.
- Proper-subset rationale: walking, generic body physics, full visibility and
  live time support execution but do not define the one-object recursive
  bridge-to-key transformation.
- Novelty claim: not assessed.

## Outcome

- Reused genes: `ACT-008`, `ACT-048`, `SYS-036`, `INF-001`, `OBJ-022`,
  `TIM-003`.
- Added genes: `SYS-127`, `SYS-128`, `CON-147`, `INF-046`.
- Added combination: `COMB-0096`.
- Evidence gate: passed with two official product / creator records, two direct
  creator interviews, one reproducible chapter walkthrough, one development
  interview and one executable verifier.
- Nearest prior genome: Superliminal; see `Corpus comparison` for the current
  result.
- Next falsification target: Antichamber, to distinguish authored
  discontinuous spatial transitions from recursive, periodic and
  perspective-derived mappings.

## Taxonomy impact

- Recursive scale instances are separated from copies that can diverge, from
  periodic translations and from containment nodes that change parentage.
- Scale reindexing across a world boundary is separated from Superliminal's
  camera-to-physical-scale transform.
- Relative size is classified as manipulation eligibility, not merely visual
  presentation.

## Negative results

- No generic “recursion” gene was added: state propagation, scale reindexing,
  pickup constraint and correspondence display have separate falsifiable
  boundaries.
- `SYS-124` is rejected because camera distance does not determine key size.
- `SYS-070` is rejected because the model does not reparent the key inside a
  mutable containment graph.
- No independent-copy multiplication is recorded; visible homologues share one
  authoritative state and cannot be spent separately.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Модель і навколишній двір є одночасними
  масштабними представленнями одного стану (`MAQ-002`, `MAQ-003`).
- [Confirmed | Direct | High] Перенесення ключа між рівнями рекурсії змінює
  його доступний відносний масштаб без заміни ідентичності (`MAQ-005`–`MAQ-007`).

## Нові гени

- [Observation | Direct | High] `SYS-127` — поширювати один авторитетний стан
  на гомологічні масштабні представлення.
- [Observation | Direct | High] `SYS-128` — переіндексовувати фізичний масштаб
  об'єкта під час перенесення між сусідніми рівнями рекурсії.
- [Observation | Direct | High] `CON-147` — дозволяти підняття лише у
  керованому відносному масштабі.
- [Observation | Direct | High] `INF-046` — одночасно показувати впізнавану
  відповідність вкладених масштабів.

## Нові комбінації

- [Observation | Direct | High] `COMB-0096` — переіндексувати один рекурсивний
  об'єкт у міст, малий ключ і знову міст до фіксованого виходу.

## Зміни таксономії

- [Observation | Direct | High] Рекурсивну синхронізацію відділено від
  незалежних копій, containment-reparenting і перспективного рескейлу.

## Нові питання

- Який точний production-коефіцієнт масштабу та як система передає колізії між
  гомологічними представленнями?
- Чи потребує пізніше переміщення всього recursive world окремого системного
  гена, якщо його буде взято як самостійний causal packet?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] Antichamber.
- Optimisation criterion: test discontinuous authored room transitions after
  recursive scale, periodic translation and camera-derived scaling are
  separately represented.
- Expected information gain: distinguish viewpoint-triggered replacement or
  nonlocal adjacency from all current continuous spatial transforms.
- Backlog impact: move Antichamber to `GAME-0097`; retain The Witness as a
  later environment-panel rule projection candidate.

## Чому саме вона

- [Hypothesis | Limited | Medium] Antichamber can reuse first-person navigation
  and visible world state while forcing the taxonomy to decide whether a
  discontinuous room change is traversal, state replacement or authored graph
  remapping.
