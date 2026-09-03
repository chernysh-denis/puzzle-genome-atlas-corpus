---
game_id: GAME-0107
slug: the-pedestrian
game_title: The Pedestrian
analysis_status: reviewed
reviewed: 2026-08-15
combination_ids:
  - COMB-0107
gene_ids:
  action:
    - ACT-008
    - ACT-110
    - ACT-111
  system:
    - SYS-143
  constraint:
    - CON-161
  information:
    - INF-001
  objective:
    - OBJ-026
  time:
    - TIM-002
---

# Game: The Pedestrian

## Analysis scope

- Version / ruleset: Skookum Arts' 2020 base release, bounded to one early
  three-panel public-sign packet before keys, boxes, hazards, paint locks and
  later world-layer mechanics are introduced.
- Included: direct stick-figure walking, jumping and ladder movement; a finite
  set of intact panels; external panel repositioning without interior mutation;
  explicit pairing of compatible door and ladder endpoints across panels; one
  link per port; bidirectional cross-panel transfer; a visible target exit; and
  self-paced construction followed by direct route traversal.
- Excluded: keys, locked doors, boxes, switches, lifts, bounce pads, lasers,
  batteries, moving hazards, panel overlap, paint pumps / locked nodes, safe
  zones, disconnection resets, finale mechanics, story interpretation,
  achievements and platform-specific controls.
- Direct-play status: not conducted. The official Steam description establishes
  rearranging and reconnecting public signs; a creator interview identifies the
  node-link editor as the core loop. Contemporary reviews independently document
  separate layout and connector actions, compatible door / ladder endpoints and
  avatar traversal. A synthetic executable control reproduces the bounded graph.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PED-001` | The Pedestrian is a 2020 single-player 2.5D puzzle-platformer by Skookum Arts | Confirmed | Corroborated | High | P1, P2 |
| `PED-002` | The player directly controls a pedestrian pictogram inside fixed 2D sign interiors | Confirmed | Corroborated | High | P1, S1, S2 |
| `PED-003` | In overview mode the player can reposition intact sign panels without changing their interiors | Confirmed | Corroborated | High | P1, S1, S2, V1 |
| `PED-004` | Panel position alone does not create traversal: compatible endpoints must be connected separately | Confirmed | Corroborated | High | P1, P2, S1, S2, V1 |
| `PED-005` | Door endpoints pair with complementary doors and ladder endpoints with complementary ladders across panels | Confirmed | Corroborated | High | P2, S1, S2, V1 |
| `PED-006` | Entering a connected endpoint transfers the controlled pedestrian to its paired endpoint in another panel | Confirmed | Corroborated | High | S1, S2, V1 |
| `PED-007` | The bounded packet is solved by traversing the constructed panel graph to the designated exit | Confirmed | Corroborated | High | P1, S1, S2, V1 |
| `PED-008` | The scoped construction and traversal are deterministic and self-paced | Observation | Corroborated | High | P1, P2, S1, S2 |

## Basic data

- Release / origin: Skookum Arts developed and published The Pedestrian on
  29 January 2020.
- Platform or physical form: single-player digital puzzle-platformer whose
  directly controlled figure moves through two-dimensional public signs placed
  in a three-dimensional urban environment.
- Puzzle family: editable panel-port topology followed by avatar traversal.
- Primary / publisher sources:
  - **[P1]** [official Steam page](https://store.steampowered.com/app/466630/The_Pedestrian/),
    for release, developer / publisher, 2.5D form and the explicit description
    of play as rearranging and reconnecting public signs to advance.
  - **[P2]** [Game Developer interview with Daniel Lackey](https://www.gamedeveloper.com/design/how-skookum-arts-built-i-the-pedestrian-i-puzzles-out-of-urban-signage),
    for the creator's account of connecting separate pieces so doors link and
    of the resulting node-based editor becoming the core game loop.
- Contemporary corroboration:
  - **[S1]** [PC Gamer review](https://www.pcgamer.com/the-pedestrian-review/),
    documenting direct sign traversal, rearranged panels, separately connected
    doors and ladders and a critical path across them.
  - **[S2]** [GameSpot review](https://www.gamespot.com/reviews/the-pedestrian-review-walk-before-you-run/1900-6417408/),
    distinguishing field rearrangement from endpoint connection and confirming
    compatibility restrictions before the pedestrian can traverse the route.
  - **[V1]** [`verify_the_pedestrian_panel_route.py`](../../../scripts/verify_the_pedestrian_panel_route.py),
    an original three-panel control for placement, typed one-to-one links and
    direct traversal without copied level geometry.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. The player walks, jumps and climbs
  the pictogram through fixed interior platforms and toward a connected port.
- `ACT-110` — reposition intact traversal panel in edit plane. The player drags
  a whole sign to a new overview position while its interior and ports persist.
- `ACT-111` — pair compatible traversal-panel ports. The player explicitly
  links two compatible endpoints on different signs; this, not panel proximity,
  creates the cross-panel edge.
- `ACT-033` is absent because there is no fixed four-slot illustrated tableau.
  `ACT-056` is absent because a sign is not an authoritative map fragment whose
  location rebuilds the represented world by itself.

### System Behaviour Genes

- `SYS-143` — transfer controlled avatar across paired panel ports. Entering a
  linked door or ladder transfers the pedestrian to the paired endpoint, after
  which direct movement continues inside the destination sign.
- Resolution order: reposition intact panels; select two ports; validate type,
  polarity, cross-panel identity and unused capacity; create a visible
  bidirectional link; return to avatar control; traverse interior geometry;
  enter the port; emerge at its mate; continue toward the exit.
- `SYS-044` is absent because a visual seam does not automatically advance an
  uncontrolled represented figure. `SYS-074` is absent because panel placement
  alone does not propagate a new physical world topology.

### Constraint Genes

- `CON-161` — one-to-one typed directional panel-port pairing. Door connects to
  a complementary door, ladder to a complementary ladder, each port participates
  in at most one cross-panel link, and incompatible pairs are rejected.
- `CON-058` is absent: it compares typed boundaries of touching tiles, whereas
  The Pedestrian links explicitly selected remote ports on intact panels.
- `CON-065` is absent: exact image crop or seam composition is not the predicate.
- Scarce strategic resources: the fixed endpoint inventory and its one-link
  capacity; panel motion itself is revisable and does not consume a panel.

### Information Genes

- `INF-001` — fully visible current state. The scoped overview exposes every
  panel interior, port, connector, start and exit before construction, while
  avatar mode preserves the currently built route visibly around the figure.
- No hidden endpoint identity, random connection or nested scene graph is part
  of the early packet.

### Objective Genes

- `OBJ-026` — reach designated traversable world location. Success requires
  building a legal cross-panel route and directly moving the pedestrian through
  it to the fixed exit, not merely displaying a connected graph.

### Time Genes

- `TIM-002` — self-paced sequential action. The early overview and platforming
  packet has no advancing puzzle clock, move budget or autonomous opponent.

## Reproducible transitions

The synthetic packet uses original panel labels and geometry.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Panels A, B and C occupy their initial overview positions and no ports are linked | Move panel C below A | C keeps the same interior and endpoints; the link graph remains empty | panel layout and topology are separate state | `PED-003`, `PED-004` |
| A has a right-facing door; B has a left-facing door | Pair `A-R` with `B-L` | One bidirectional door edge is created | explicit compatible connection | `PED-004`, `PED-005` |
| B has a downward ladder; C has an upward ladder | Pair `B-D` with `C-U` | A second bidirectional ladder edge is created | type and polarity define eligibility | `PED-005` |
| A door and C ladder are both unused | Attempt to pair them | Link is rejected and both remain available | doors and ladders are not interchangeable | `PED-005` |
| `A-R` is already paired with `B-L` | Attempt to pair `A-R` again | Link is rejected | every port has capacity one | `PED-005` |
| Pedestrian stands in A before `A-R` | Walk into `A-R` | Pedestrian emerges at `B-L` and remains directly controlled | route use follows construction | `PED-002`, `PED-006` |
| Pedestrian reaches `B-D` and that port links to C | Enter the ladder | Pedestrian emerges at `C-U`, then walks to the visible exit | full constructed graph completes the packet | `PED-006`, `PED-007` |

## Strategic and experiential structure

- Local decision: choose which two compatible endpoints should form the next
  graph edge without consuming a port needed later.
- Medium-term planning: reason backward from the exit through port types, then
  place panels legibly and build a sequence the avatar can physically traverse.
- Long-term structure: later chapters layer objects and hazards onto the same
  grammar, but they are outside this early packet.
- Common heuristics: separate drawing readability from connectivity; count each
  port once; pair opposite door or ladder orientations; simulate the avatar's
  interior path before committing to traversal.
- Failure attribution: an invalid pair is rejected immediately; a connected
  dead end follows from visible endpoint capacity or an unreachable interior.
- Player-trust factors: compatible port types, occupied ports, connector lines,
  transfer direction and edit / avatar mode must remain unambiguous.

## Replay and variation

- Panels, interiors, ports, start and exit are authored and fixed. The player's
  panel positions, connection order and unsuccessful pairings may vary.
- No randomness or procedural generation occurs in the bounded packet.
- Several overview layouts can remain visually different while encoding the
  same successful graph; topology, not decorative spacing, determines passage.
- Replay chiefly reduces exploratory edits or tests a clearer layout.

## Adjacent systems and history

- Carto also alternates external editing with direct avatar traversal, but every
  legal fragment placement immediately moves an authoritative world region and
  derives boundary adjacency. The Pedestrian keeps sign interiors fixed and
  requires a separate port-pairing action.
- Gorogoa moves framed illustrations and can make authored crops or seams
  automatically continuous. The Pedestrian exposes explicit typed ports, a
  persistent connector line and a directly controlled avatar.
- Portal pairs two replaceable apertures placed on world surfaces and transforms
  crossing-body velocity. The Pedestrian pairs authored panel endpoints and
  resumes ordinary local movement without a momentum transform.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-110`, `ACT-111` | panel drag; endpoint selection; avatar controls |
| System Behaviour | `SYS-143` | transfer direction; emergence pose |
| Constraint | `CON-161` | endpoint type, polarity and capacity |
| Information | `INF-001` | overview zoom; link highlighting |
| Objective | `OBJ-026` | exit identity |
| Time | `TIM-002` | mode switch; pause policy |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `106` (`GAME-0001`–`GAME-0106`).
- Exact genome matches: none.
- Tied near matches: `GAME-0040` — Carto (`4 / 12 = 0.333333`).
- Supported combination subsets: `COMB-0107`.
- Scan date: 2026-08-15.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0040`.

### Preserved research notes

- New genes: `ACT-110`, `ACT-111`, `SYS-143`, `CON-161`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: the corpus already represented direct avatar movement,
  complete visible state, target-location access and self-paced editing. It did
  not represent freely repositioned intact traversal panels that remain inert
  until the player separately pairs typed one-to-one ports, nor controlled
  avatar transfer across those constructed panel edges.

## Taxonomy impact

- Registry changes: four Active IDs and four transfers to a new game.
- Taxonomy-change record: none; no previous gene is merged, split or retired.
- Candidate terms affected: traversal-panel repositioning, explicit panel-port
  pairing, paired-port avatar transfer and one-to-one typed port compatibility.

## Negative results

- `ACT-033` rejected: The Pedestrian panels move freely in an edit plane, not
  among a fixed set of illustrated slots.
- `ACT-056` / `SYS-074` rejected: panel relocation alone does not move an
  authoritative world region or derive new boundary adjacency.
- `SYS-044` / `CON-065` rejected: neither visual crop alignment nor automatic
  illustrated-scene continuation defines a link.
- `CON-058` rejected: ports need not be touching tile edges and are paired by a
  separate action.
- `ACT-047` / `SYS-059` rejected: endpoints are authored panel ports rather
  than replaceable surface apertures, and no momentum transformation occurs.
