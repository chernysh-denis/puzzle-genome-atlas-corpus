---
game_id: GAME-0033
slug: portal
game_title: Portal
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0033
gene_ids:
  action:
    - ACT-008
    - ACT-047
    - ACT-048
  system:
    - SYS-036
    - SYS-059
    - SYS-060
    - SYS-061
  constraint:
    - CON-078
    - CON-079
  information:
    - INF-001
    - INF-019
  objective:
    - OBJ-022
  time:
    - TIM-003
---

# Game: Portal

## Analysis scope

- Version / ruleset: the original 2007 Portal, scoped to one ordinary test
  chamber after the handheld portal device can create both colours and where a
  Weighted Storage Cube and floor button are available.
- Included: first-person navigation; blue / orange portal placement; surface
  validity and same-colour replacement; bidirectional avatar and cube transit;
  cross-portal view; gravity, collision and momentum redirection; cube pickup /
  release; occupancy-held button / door state; hazards and fixed chamber exit.
- Excluded: narrative, escape sequence, advanced / challenge chambers, Portal:
  Still Alive additions, Portal 2, co-op, editor, achievements, speedrun
  exploits and platform-specific controls.
- Direct-play status: not conducted. Valve product material and in-game creator
  commentary are triangulated with contemporary hands-on reports and a formal
  mechanical account. Engine-specific partial-body and collision edge cases
  remain parameters.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PRT-001` | The player directly walks and jumps through a continuous three-dimensional chamber | Confirmed | Corroborated | High | P1, P2, S1 |
| `PRT-002` | The fully powered device independently fires one blue and one orange endpoint onto eligible chamber surfaces | Confirmed | Corroborated | High | P2, S1, S2, S3 |
| `PRT-003` | A valid shot of one colour replaces that colour's prior endpoint; traversal becomes available through the complementary pair | Confirmed | Corroborated | High | S1, S2, R1 |
| `PRT-004` | A player or portable cube crossing either aperture emerges from the other under a transformed pose | Confirmed | Direct | High | P2, P3, S1, R1 |
| `PRT-005` | Entry momentum is carried through and redirected relative to the exit, permitting gravity-powered flings | Confirmed | Direct | High | P3, S1, S2, S3 |
| `PRT-006` | Portal surfaces show a live view from the paired endpoint before traversal | Confirmed | Direct | High | P3, S1 |
| `PRT-007` | The player can pick up, carry and release a Weighted Storage Cube, including transporting it through portals | Confirmed | Corroborated | High | P2, P3, S2, A1 |
| `PRT-008` | A player or cube occupying a floor button holds its linked door active; removing the occupant reverses that state | Confirmed | Corroborated | High | P3, S4, A1 |
| `PRT-009` | Portal placement is limited by surface material, planarity and available aperture footprint | Confirmed | Corroborated | High | S1, R1 |
| `PRT-010` | Chamber completion requires bringing the sole controlled test subject through the fixed exit after arranging access | Confirmed | Corroborated | High | P3, S4, A1 |
| `PRT-011` | Gravity and body physics continue in real time while the player moves, aims, fires, carries or releases objects | Confirmed | Corroborated | High | P3, S1, S2 |
| `PRT-012` | Portal is not a route-drawing or network-editing system: the player positions two apertures and the system maps traversal directly between them | Confirmed | Corroborated | High | P2, P3, PRT-002–PRT-006 |

## Basic data

- Release / origin: Valve released Portal on 10 October 2007.
- Platform or physical form: real-time first-person three-dimensional puzzle
  simulation with a portal-placement device and physics-enabled objects.
- Puzzle family: paired-portal spatial and momentum transformation.
- Creator and official sources:
  - **[P1]** [Valve — Portal on Steam](https://store.steampowered.com/app/400/Portal/),
    confirming Valve, the 2007 release and the single-player spatial-puzzle
    premise.
  - **[P2]** [Valve / Nintendo — Portal: Companion Collection](https://www.nintendo.com/au/games/nintendo-switch/portal-companion-collection/),
    describing use of the portal device to solve physical puzzles by moving the
    player and objects through space.
  - **[P3]** [Portal developer commentary transcript](https://theportalwiki.com/wiki/Portal_developer_commentary),
    a specialist transcription of Valve's in-game creator commentary: paired
    traversal, live views, box / button training, portal physics, momentum
    flings and chamber endpoints.
- Contemporary corroboration:
  - **[S1]** [GameSpot GDC 2007 hands-on](https://www.gamespot.com/articles/gdc-07-portal-hands-on/1100-6166975/),
    reporting two portals on eligible flat surfaces, bidirectional viewing and
    traversal, and fall-momentum flings.
  - **[S2]** [Ars Technica E3 2007 hands-on](https://arstechnica.com/gaming/2007/07/ars-at-e3-hands-on-with-portal-ps3/),
    documenting one control per portal, object manipulation and momentum-based
    exit from a paired aperture.
  - **[S3]** [Wired — Games Frontiers 2007](https://www.wired.com/2007/10/gamesfrontiers-1008/),
    describing connected portals on walls, floors or ceilings and momentum
    flinging to distant ledges.
  - **[S4]** [Macworld — Portal](https://www.macworld.com/article/203893/portal_mac.html),
    corroborating retained momentum, Weighted Storage Cubes, buttons and
    environmental hazards.
- Formal / specialist mechanical accounts:
  - **[A1]** [Demaine, Lockhart and Lynch — The Computational Complexity of Portal](https://dspace.mit.edu/server/api/core/bitstreams/4f37888c-26d6-4789-8ef1-ef2dc271a146/content),
    formalising weighted floor buttons, cubes, doors, portals and chamber
    reachability.
  - **[R1]** [Portal Wiki — Portals](https://www.theportalwiki.com/wiki/Portals),
    used for endpoint replacement and invalid-surface boundary corroboration.
- Claim IDs: `PRT-001`–`PRT-012`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. The player locally walks and jumps
  Chell through continuous chamber geometry; crossing an aperture is an
  automatic consequence of that navigation, not a separately selected
  teleport destination.
- `ACT-047` — place replaceable paired-portal endpoint. A blue or orange shot
  targets one eligible surface region and replaces the prior endpoint of that
  colour.
- `ACT-048` — pick up and release portable rigid object. A reachable cube can
  be held at a controlled offset while navigating, then dropped or thrown back
  into the live simulation.
- `ACT-016` and `ACT-023` are absent: the player selects aperture endpoints,
  neither traces intermediate cells nor edits an ordered route. `ACT-043` is
  absent because the aperture is not a solid device agents later collide with.
- `ACT-009` is absent: carrying is not an adjacency push that displaces both
  agent and object one cell. `ACT-014` is absent because a cube is not moved
  directly to an abstract legal destination; it remains physically held.
- Claim IDs: `PRT-001`–`PRT-003`, `PRT-007`, `PRT-012`.

### System Behaviour Genes

- `SYS-036` — continuous force-constrained body dynamics. Gravity, velocity and
  collisions continue for Chell and released cubes between inputs.
- `SYS-059` — bidirectional paired-aperture traversal. Crossing either portal
  maps the body's relative position and orientation to the other endpoint.
- `SYS-060` — portal-relative velocity reorientation. Incoming speed is
  transformed into the exit frame, making falling momentum usable as a fling.
- `SYS-061` — occupancy-sustained linked mechanism state. A cube or Chell on a
  floor button holds the associated door open; vacating it closes the door.
- Portal topology is not encoded as a transit-network gene: no vehicle chooses
  among service nodes or follows an authored multi-edge path. The linkage has
  exactly two replaceable apertures and body crossing resolves immediately.
- Resolution order: live forces and movement update; a body crossing a portal
  plane is pose-mapped and its velocity reoriented; collision continues in the
  exit geometry; button occupancy is then reflected in the linked mechanism.
- Claim IDs: `PRT-004`, `PRT-005`, `PRT-008`, `PRT-011`, `PRT-012`.

### Constraint Genes

- `CON-078` — surface-bounded portal endpoint eligibility. Material, usable
  planar area and full aperture footprint decide whether a shot creates an
  endpoint.
- `CON-079` — one replaceable endpoint per portal channel. Only one blue and
  one orange endpoint persist; replacing either changes the shared shortcut,
  and an incomplete pair cannot transport bodies.
- Hazard contact and unreachable chamber geometry are level-instance failure /
  reachability conditions, not separately admitted genes in this scope.
- Scarce strategic resources: the two endpoint locations, portal-conductive
  surface area, safe trajectories, cube position and maintained button access.
- Claim IDs: `PRT-002`, `PRT-003`, `PRT-009`, `PRT-010`.

### Information Genes

- `INF-001` — fully visible current state. From navigable viewpoints the player
  can inspect chamber geometry, cube, button, linked door, hazards and current
  portals; viewpoint rotation is an inspection parameter, not hidden state.
- `INF-019` — live cross-portal scene view. Each active aperture visibly shows
  the paired endpoint's current scene, allowing exit-side inspection before a
  commitment to traversal or a fling.
- The view conveys current spatial state, not an exact prediction of the future
  ballistic trajectory.
- Claim IDs: `PRT-006`, `PRT-009`–`PRT-011`.

### Objective Genes

- `OBJ-022` — evacuate every required controlled actor through fixed exits.
  The required actor set has cardinality one: the controlled test subject must
  reach the chamber's fixed endpoint, usually after sustaining access through
  the cube / button arrangement. No partial quota or actor loss is permitted.
- The cube is an enabling tool rather than the final delivered payload, so
  `OBJ-014` is absent.
- Claim IDs: `PRT-008`, `PRT-010`.

### Time Genes

- `TIM-003` — real-time input during forced progression. The player may aim,
  fire, move and release a cube while gravity, velocity and collisions continue
  to advance; waiting during a fall changes the resulting state.
- This is not `TIM-002`: although the player can stand safely to plan, a
  completed input does not suspend continuous body dynamics during active
  movement or a fling.
- Claim IDs: `PRT-005`, `PRT-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| No blue endpoint, valid white wall under crosshair | Fire blue portal | Blue aperture appears at the valid footprint | endpoint placement is a direct action filtered by surface eligibility | `PRT-002`, `PRT-009` |
| Blue already exists elsewhere | Fire blue at another valid surface | Old blue disappears and new blue becomes the sole endpoint of that channel | channel capacity and replacement are one persistent constraint | `PRT-003` |
| Blue and orange are active | Walk or carry a cube across orange plane | Body emerges from the corresponding blue-relative position and orientation | traversal is bidirectional spatial mapping, not route following | `PRT-004`, `PRT-007` |
| Chell falls toward a floor portal paired with a wall portal | Continue through the floor aperture | Fall speed becomes outward wall-relative velocity and carries Chell toward a ledge | force dynamics and portal velocity transform are independently required | `PRT-005`, `PRT-011` |
| Exit side is not directly visible | Look into the nearby active portal | Surface shows the live remote scene before entry | cross-portal view is decision-relevant information | `PRT-006` |
| Closed linked door and free cube | Carry and release cube onto floor button | Sustained occupancy opens the door; removing the cube closes it | held-object action and occupancy mechanism are distinct | `PRT-007`, `PRT-008` |
| Door access is maintained and route is safe | Navigate Chell through fixed chamber exit | Chamber reaches its terminal completion boundary | objective is actor exit, not cube delivery | `PRT-010` |

## Strategic and experiential structure

- Local decision: choose which colour to place, which visible surface footprint
  should host it and whether to traverse, inspect, carry or build momentum.
- Medium-term planning: reserve one endpoint as access while repeatedly moving
  the other; transport the cube without losing the only route back; arrange a
  button state that leaves the exit path usable.
- Long-term structure: reinterpret chamber geometry as one space with a mutable
  two-aperture adjacency, then couple that topology to real-time velocity.
- Common heuristics: look through before entering, separate endpoint colour
  roles, test safe walking links before flings, trace the exit-facing normal,
  and place the cube only after preserving a return portal.
- Failure attribution: invalid surfaces reject portal shots visibly; the live
  remote view exposes endpoint orientation; trajectories remain attributable
  to entry speed, exit normal and collision geometry.
- Player-trust factors: portal placement footprint, replacement colour,
  bidirectionality, view transform, velocity transform, held-cube traversal and
  button release must remain consistent.
- Claim IDs: `PRT-001`–`PRT-012`.

## Replay and variation

- What changes between chambers: fixed geometry, portalable materials, hazards,
  cube / button placement, linked mechanisms and required traversal sequence.
- Randomness or procedural generation: none in the scoped chamber.
- Multiple viable strategies: later ordinary chambers can admit different
  endpoint orders, cube routes or fling setups even when the exit is fixed.
- Typical replay motive: reduce portals or time in challenge variants, which
  are excluded from the canonical scope; otherwise replay tests alternate
  spatial solutions.
- Claim IDs: `PRT-002`–`PRT-011`.

## Adjacent systems and history

- Cut the Rope shares continuous physics and live input, but its player removes
  supports around one indirectly controlled payload and never rewires space
  through a visible bidirectional aperture pair.
- Tin Hearts shares continuous motion and live intervention, but redirects
  autonomous agents by moving solid devices and exposes projected routes; it
  neither preserves entry momentum through spatial mapping nor directly
  navigates the required actor.
- Sokoban shares direct navigation and movable-object reasoning, but its crates
  are adjacency-pushed on a fixed grid under self-paced discrete time.
- Timelie supplies the reused all-required-actors exit objective with two
  scheduled actors; Portal uses one locally navigated actor and live physics.
- Claim IDs: `PRT-001`–`PRT-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-047`, `ACT-048` | local navigation, paired endpoint placement, cube carry |
| System Behaviour | `SYS-036`, `SYS-059`, `SYS-060`, `SYS-061` | force dynamics, traversal, velocity and button linkage |
| Constraint | `CON-078`, `CON-079` | portal surface and channel capacity |
| Information | `INF-001`, `INF-019` | visible chamber and live remote view |
| Objective | `OBJ-022` | sole required actor reaches fixed exit |
| Time | `TIM-003` | live input and continuous dynamics |

Canonical signature:

`ACT-008,ACT-047,ACT-048; SYS-036,SYS-059,SYS-060,SYS-061; CON-078,CON-079; INF-001,INF-019; OBJ-022; TIM-003`

## Corpus comparison

- Indexed games scanned: `GAME-0001`–`GAME-0032`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0032`.
- Exact genome matches: none.
- Existing combination subsets: none.
- Jaccard scores against complete genomes:
  - `GAME-0001`: shared `INF-001`; `1 / 26 = 0.038462`.
  - `GAME-0002`: shared `INF-001`; `1 / 19 = 0.052632`.
  - `GAME-0003`: shared none; `0 / 22 = 0.000000`.
  - `GAME-0004`: shared `INF-001`, `TIM-003`; `2 / 26 = 0.076923`.
  - `GAME-0005`: shared `INF-001`; `1 / 19 = 0.052632`.
  - `GAME-0006`: shared `ACT-008`, `INF-001`; `2 / 20 = 0.100000`.
  - `GAME-0007`: shared `INF-001`; `1 / 20 = 0.050000`.
  - `GAME-0008`: shared `INF-001`; `1 / 19 = 0.052632`.
  - `GAME-0009`: shared `INF-001`; `1 / 28 = 0.035714`.
  - `GAME-0010`: shared `INF-001`; `1 / 21 = 0.047619`.
  - `GAME-0011`: shared `INF-001`; `1 / 25 = 0.040000`.
  - `GAME-0012`: shared `INF-001`; `1 / 21 = 0.047619`.
  - `GAME-0013`: shared `INF-001`; `1 / 25 = 0.040000`.
  - `GAME-0014`: shared `INF-001`; `1 / 27 = 0.037037`.
  - `GAME-0015`: shared `INF-001`; `1 / 26 = 0.038462`.
  - `GAME-0016`: shared `INF-001`, `TIM-003`; `2 / 26 = 0.076923`.
  - `GAME-0017`: shared none; `0 / 26 = 0.000000`.
  - `GAME-0018`: shared `INF-001`, `TIM-003`; `2 / 30 = 0.066667`.
  - `GAME-0019`: shared `INF-001`; `1 / 22 = 0.045455`.
  - `GAME-0020`: shared `INF-001`; `1 / 26 = 0.038462`.
  - `GAME-0021`: shared `SYS-036`, `INF-001`, `TIM-003`; `3 / 19 = 0.157895`.
  - `GAME-0022`: shared `INF-001`; `1 / 24 = 0.041667`.
  - `GAME-0023`: shared none; `0 / 23 = 0.000000`.
  - `GAME-0024`: shared `TIM-003`; `1 / 24 = 0.041667`.
  - `GAME-0025`: shared `INF-001`, `TIM-003`; `2 / 22 = 0.090909`.
  - `GAME-0026`: shared `SYS-036`, `INF-001`, `TIM-003`; `3 / 22 = 0.136364`.
  - `GAME-0027`: shared `INF-001`, `TIM-003`; `2 / 23 = 0.086957`.
  - `GAME-0028`: shared `INF-001`, `TIM-003`; `2 / 28 = 0.071429`.
  - `GAME-0029`: shared `ACT-008`, `INF-001`, `TIM-003`; `3 / 22 = 0.136364`.
  - `GAME-0030`: shared `SYS-036`, `INF-001`, `TIM-003`; `3 / 24 = 0.125000`.
  - `GAME-0031`: shared `INF-001`, `OBJ-022`; `2 / 22 = 0.090909`.
  - `GAME-0032`: shared `INF-001`; `1 / 23 = 0.043478`.
- Mathematically selected near match: `GAME-0021` — Cut the Rope at
  `3 / 19 = 0.157895`.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0021` — Cut the Rope | `SYS-036`, `INF-001`, `TIM-003` | direct avatar / cube control and replaceable paired spatial mapping versus cutting supports around one indirectly controlled payload | Near match only; no existing combination recurs |

- New genes: `ACT-047`, `ACT-048`, `SYS-059`, `SYS-060`, `SYS-061`,
  `CON-078`, `CON-079`, `INF-019`.
- Reused genes: `ACT-008`, `SYS-036`, `INF-001`, `OBJ-022`, `TIM-003`.
- Classification result: `New gene`; no exact or existing-combination match.
- Evidence and reasoning: the five reused genes establish continuous embodied
  navigation and exit structure. The new boundaries remain independently
  decision-relevant: endpoint authority, spatial mapping, velocity transform,
  occupancy linkage, placement eligibility, channel capacity and remote view
  cannot be reduced to generic physics or parameters of route editing.

## Combination hypothesis

- `COMB-0033` — paired-portal momentum traversal.
- Central interaction: player-placed replaceable endpoints create a visible
  bidirectional spatial mapping whose exit-relative velocity transform turns
  continuous gravity into a traversal resource under real-time control.
- Falsification boundary: fixed teleporters, route graphs, solid redirectors or
  portals that discard incoming motion do not instantiate the combination.

## Taxonomy impact

- Registry changes: eight stable genes added; five existing genes reused.
- `OBJ-022` gains a one-actor parameter instance. Its invariant remains that
  every member of the declared required actor set must reach a fixed exit, so
  cardinality one does not require a new objective.
- `SYS-036` continues to encode generic force integration; portal traversal
  and the velocity-frame transform are separate automatic transitions rather
  than parameters of gravity.
- Taxonomy-change record: none; no previous lifecycle or signature changed.

## Negative results

- Route drawing (`ACT-016`), transit-line editing (`ACT-023`) and solid-device
  repositioning (`ACT-043`) do not describe endpoint placement.
- Adjacent pushing (`ACT-009`) and direct board-piece relocation (`ACT-014`)
  do not describe continuously carrying a physics object.
- `OBJ-014` is absent because the cube only enables access; chamber success is
  the controlled actor reaching the exit.
- `TIM-002` is absent because body state advances continuously during falls,
  throws and flings even though safe observation intervals may be unpressured.
- No older combination is a proper subset of the Portal genome.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Two replaceable, surface-limited apertures map
  bodies bidirectionally and expose a live view of the paired endpoint
  (`PRT-002`–`PRT-006`, `PRT-009`).
- [Confirmed | Corroborated | High] Portal combines this mapping with live body
  physics, cube carrying, sustained pressure controls and a fixed actor exit
  (`PRT-007`–`PRT-011`).

## Нові гени

- [Observation | Corroborated | High] Added eight genes: `ACT-047`, `ACT-048`,
  `SYS-059`–`SYS-061`, `CON-078`, `CON-079` and `INF-019`; reused five.

## Нові комбінації

- [Observation | Corroborated | High] Registered `COMB-0033`, an eight-gene
  paired-portal momentum-traversal structure supported by Portal.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; `OBJ-022` safely
  accepts a required actor set of one and generic physics stays distinct from
  portal-specific spatial and velocity transforms.

## Нові питання

- Will another first-person physics puzzler reuse `ACT-048` without paired
  portals and thereby validate its independent boundary?
- Does Braid reuse reversible-time genes while separating avatar-relative time
  exceptions from Timelie's editable authoritative timeline?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] `GAME-0034` — Braid, Anniversary Edition.
- Optimisation criterion: revisit the retained time candidate after two
  intervening non-time units and test whether `TIM-007` recurs without
  `TIM-008`.
- Expected information gain: distinguish global rewind, object-specific time
  immunity and shadow replay from timestamped command editing and exact future
  seeking.
- Backlog impact: retain Pikmin 4 for a later population carrying / command
  boundary test.

## Open questions

- Engine-specific partial-body collision and portal-edge behaviour remain
  parameters and should be direct-play tested if implementation fidelity
  becomes relevant.
- A later game should test whether `ACT-048` generalises cleanly to other
  first-person carry-and-release physics puzzles.
- A later portal game should test whether gel, co-op ownership or moving portal
  surfaces require splits rather than parameters; none is inferred here.

## Sources consulted

- Valve Steam and Valve / Nintendo product descriptions.
- Valve in-game developer commentary through a specialist transcript.
- Contemporary GameSpot, Ars Technica, Wired and Macworld accounts.
- Demaine, Lockhart and Lynch's formal Portal model.
- Portal Wiki endpoint reference for narrow implementation boundaries.
