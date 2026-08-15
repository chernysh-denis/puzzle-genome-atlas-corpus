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

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `(ACT-008,ACT-110,ACT-111; SYS-143; CON-161; INF-001; OBJ-026; TIM-002)`.
- Indexed games scanned: 107, including this record.
- Indexed combinations scanned: 107.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0040` — Carto is uniquely nearest
  at `4 / 12 = 0.333333`, sharing direct avatar navigation, visible current
  state, target-location access and self-paced play while differing on how the
  edited overview becomes traversal topology.
- Supported combination subsets: `COMB-0107` only.
- Scan date: 2026-08-15.

### Full prior-game Jaccard scan

- `GAME-0001`: `1 / 21 = 0.047619`; `GAME-0002`: `2 / 13 = 0.153846`; `GAME-0003`: `0 / 17 = 0.000000`; `GAME-0004`: `1 / 22 = 0.045455`.
- `GAME-0005`: `2 / 13 = 0.153846`; `GAME-0006`: `3 / 14 = 0.214286`; `GAME-0007`: `2 / 14 = 0.142857`; `GAME-0008`: `2 / 13 = 0.153846`.
- `GAME-0009`: `1 / 23 = 0.043478`; `GAME-0010`: `1 / 16 = 0.062500`; `GAME-0011`: `2 / 19 = 0.105263`; `GAME-0012`: `2 / 15 = 0.133333`.
- `GAME-0013`: `1 / 20 = 0.050000`; `GAME-0014`: `1 / 22 = 0.045455`; `GAME-0015`: `1 / 21 = 0.047619`; `GAME-0016`: `1 / 22 = 0.045455`.
- `GAME-0017`: `0 / 21 = 0.000000`; `GAME-0018`: `1 / 26 = 0.038462`; `GAME-0019`: `1 / 17 = 0.058824`; `GAME-0020`: `1 / 21 = 0.047619`.
- `GAME-0021`: `1 / 16 = 0.062500`; `GAME-0022`: `1 / 19 = 0.052632`; `GAME-0023`: `1 / 17 = 0.058824`; `GAME-0024`: `1 / 19 = 0.052632`.
- `GAME-0025`: `1 / 18 = 0.055556`; `GAME-0026`: `1 / 19 = 0.052632`; `GAME-0027`: `1 / 19 = 0.052632`; `GAME-0028`: `1 / 24 = 0.041667`.
- `GAME-0029`: `2 / 18 = 0.111111`; `GAME-0030`: `1 / 21 = 0.047619`; `GAME-0031`: `1 / 18 = 0.055556`; `GAME-0032`: `1 / 18 = 0.055556`.
- `GAME-0033`: `2 / 19 = 0.105263`; `GAME-0034`: `2 / 20 = 0.100000`; `GAME-0035`: `2 / 24 = 0.083333`; `GAME-0036`: `3 / 17 = 0.176471`.
- `GAME-0037`: `1 / 16 = 0.062500`; `GAME-0038`: `2 / 22 = 0.090909`; `GAME-0039`: `2 / 15 = 0.133333`; `GAME-0040`: `4 / 12 = 0.333333`.
- `GAME-0041`: `2 / 17 = 0.117647`; `GAME-0042`: `1 / 16 = 0.062500`; `GAME-0043`: `2 / 20 = 0.100000`; `GAME-0044`: `2 / 16 = 0.125000`.
- `GAME-0045`: `2 / 20 = 0.100000`; `GAME-0046`: `2 / 16 = 0.125000`; `GAME-0047`: `1 / 21 = 0.047619`; `GAME-0048`: `1 / 21 = 0.047619`.
- `GAME-0049`: `0 / 17 = 0.000000`; `GAME-0050`: `2 / 21 = 0.095238`; `GAME-0051`: `1 / 23 = 0.043478`; `GAME-0052`: `1 / 17 = 0.058824`.
- `GAME-0053`: `2 / 15 = 0.133333`; `GAME-0054`: `3 / 16 = 0.187500`; `GAME-0055`: `2 / 16 = 0.125000`; `GAME-0056`: `1 / 15 = 0.066667`.
- `GAME-0057`: `1 / 15 = 0.066667`; `GAME-0058`: `1 / 16 = 0.062500`; `GAME-0059`: `1 / 14 = 0.071429`; `GAME-0060`: `1 / 14 = 0.071429`.
- `GAME-0061`: `2 / 16 = 0.125000`; `GAME-0062`: `2 / 14 = 0.142857`; `GAME-0063`: `2 / 13 = 0.153846`; `GAME-0064`: `2 / 11 = 0.181818`.
- `GAME-0065`: `1 / 14 = 0.071429`; `GAME-0066`: `1 / 17 = 0.058824`; `GAME-0067`: `0 / 16 = 0.000000`; `GAME-0068`: `1 / 15 = 0.066667`.
- `GAME-0069`: `2 / 14 = 0.142857`; `GAME-0070`: `1 / 15 = 0.066667`; `GAME-0071`: `2 / 13 = 0.153846`; `GAME-0072`: `2 / 14 = 0.142857`.
- `GAME-0073`: `2 / 13 = 0.153846`; `GAME-0074`: `2 / 15 = 0.133333`; `GAME-0075`: `2 / 15 = 0.133333`; `GAME-0076`: `2 / 13 = 0.153846`.
- `GAME-0077`: `2 / 13 = 0.153846`; `GAME-0078`: `2 / 13 = 0.153846`; `GAME-0079`: `2 / 13 = 0.153846`; `GAME-0080`: `2 / 13 = 0.153846`.
- `GAME-0081`: `2 / 14 = 0.142857`; `GAME-0082`: `2 / 14 = 0.142857`; `GAME-0083`: `2 / 14 = 0.142857`; `GAME-0084`: `2 / 16 = 0.125000`.
- `GAME-0085`: `1 / 18 = 0.055556`; `GAME-0086`: `2 / 19 = 0.105263`; `GAME-0087`: `1 / 17 = 0.058824`; `GAME-0088`: `2 / 15 = 0.133333`.
- `GAME-0089`: `1 / 16 = 0.062500`; `GAME-0090`: `3 / 20 = 0.150000`; `GAME-0091`: `3 / 14 = 0.214286`; `GAME-0092`: `1 / 17 = 0.058824`.
- `GAME-0093`: `3 / 14 = 0.214286`; `GAME-0094`: `2 / 16 = 0.125000`; `GAME-0095`: `2 / 18 = 0.111111`; `GAME-0096`: `2 / 16 = 0.125000`.
- `GAME-0097`: `3 / 13 = 0.230769`; `GAME-0098`: `3 / 12 = 0.250000`; `GAME-0099`: `2 / 14 = 0.142857`; `GAME-0100`: `0 / 19 = 0.000000`.
- `GAME-0101`: `2 / 16 = 0.125000`; `GAME-0102`: `1 / 14 = 0.071429`; `GAME-0103`: `1 / 16 = 0.062500`; `GAME-0104`: `3 / 14 = 0.214286`.
- `GAME-0105`: `2 / 16 = 0.125000`; `GAME-0106`: `1 / 14 = 0.071429`.

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

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Перестановка цілої панелі не створює
  прохід сама: гравець окремо сполучає сумісні порти, а потім безпосередньо
  проводить пішохода отриманим графом (`PED-003`–`PED-007`).

## Нові гени

- [Observation | Corroborated | High] `ACT-110` — перемістити цілу прохідну
  панель у площині редагування; `ACT-111` — спарувати сумісні порти панелей.
- [Observation | Corroborated | High] `SYS-143` — перенести керованого аватара
  крізь спаровані порти; `CON-161` — один-до-одного типізована й напрямна
  сумісність портів.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0107` — побудувати маршрут окремими
  портовими ребрами й пройти ним до виходу керованим аватаром.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Чи потребують пізні paint-locked nodes окремої межі незмінності частини графа
  під час редагування решти панелей?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] Cocoon.
- Optimisation criterion: contrast external flat graph editing with carried
  world-orbs whose contents can be entered and whose abilities alter traversal.
- Expected information gain: test object-as-world identity, nested world entry
  and carried-world ability reuse against existing container and portal genes.
- Backlog impact: preserve later The Pedestrian mechanics for a focused reuse
  audit rather than widening this early packet.

## Чому саме вона

- [Hypothesis | Limited | Medium] Cocoon should retain direct self-paced avatar
  traversal while replacing explicit panel edges with portable nested worlds,
  giving the final game of this batch high structural distance.
