---
game_id: GAME-0337
slug: super-metroid
game_title: Super Metroid
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-202
    - ACT-270
  system:
    - SYS-215
    - SYS-222
    - SYS-398
    - SYS-417
    - SYS-470
    - SYS-578
  constraint:
    - CON-068
    - CON-282
    - CON-349
    - CON-402
    - CON-578
  information:
    - INF-073
    - INF-119
    - INF-125
  objective:
    - OBJ-198
  time:
    - TIM-003
---

# Game: Super Metroid

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Samus, Ceres,
Zebes, Crateria, Blue Brinstar, Ridley, Morphing Ball, Missile Tank, Bombs and
Bomb Torizo are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: the original English NTSC Japan/USA Super NES program,
  reproducibly identified as `supermetroid-ntsc.sfc` with SHA-1
  `da957f0d63d14cb441d215462904c4fa8519c613`. It is not the PAL release,
  Nintendo Switch Online wrapper, SNES Classic wrapper, a randomizer, ROM hack,
  sequence-break ruleset or later Metroid title.
- Structured analysis target: original licensed Super NES cartridge behaviour
  reconstructed from Nintendo's 1994 manual and an exact-ROM disassembly build,
  with the annotated room and object source pinned independently; see
  `GAME-0337` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Scenario: one fresh single-player New Game from first ordinary control on
  Ceres Station through the first closed retained-capability loop on Zebes.
- Entry: no Zebes item, missile capacity, map progress, defeated Bomb Torizo or
  retained save state exists. Ceres begins with the base beam and Energy state
  supplied by the authored opening.
- Fixed reproducible route: traverse Ceres to the scripted Ridley encounter;
  survive its settlement and escape to the elevator before the visible `01:00`
  self-destruct timer expires; land on Zebes; descend through Crateria's old
  Tourian shaft into Blue Brinstar; collect Morphing Ball; use the compact form
  to leave its recess and reach the first Missile Tank; collect its five-missile
  capacity; return upward; select and spend five missiles on the red door;
  collect Bombs from the Chozo orb; defeat the triggered Bomb Torizo; roll and
  place Bombs to destroy the compatible exit blocks; return to the main
  Crateria vertical shaft.
- Primary decision loop: navigate a fixed room graph while enemies and hazards
  remain live; aim beam or finite missiles; preserve Energy and missile supply;
  acquire a persistent capability; recognise an earlier low passage, typed
  door or bomb block that now accepts it; backtrack through the reopened edge;
  repeat until the Bomb Torizo room and its bomb-block exit reconnect to the
  parent shaft.
- Positive terminal: Bomb Torizo is defeated, the room's exit is usable, the
  bomb-compatible blocks have been destroyed with retained Bombs, and ordinary
  control returns in the main Crateria vertical shaft with Morphing Ball,
  Missile capacity and Bombs still recorded. Content after that return is
  outside the packet.
- Failure paths: expiry of the Ceres countdown ends that escape; Energy reaching
  zero causes Game Over. Reload, Continue and save-station consequences are not
  exercised and do not enter the signature.
- Included: direct running, jumping, crouching and rolling; aiming and firing
  the base beam or selected missiles; live hostile contact and attacks; one
  Energy pool; compatible Energy/Missile drops; the Ceres deadline; visited-room
  minimap/pause map; retained Morphing Ball and Bomb abilities; +5 Missile Tank
  capacity; five-missile red door; Bomb placement and blast; Bomb Torizo room
  closure; ordered route flags and the bomb-block return edge.
- Reproducible parameterisation: movement path, ordinary enemy contact, damage,
  drops, remaining Energy/missiles and exact combat timing may vary. The Ceres
  settlement, one-minute escape allowance, room graph, three acquisitions, red
  door cost, Bomb Torizo gate and terminal return edge do not.
- Excluded: later Crateria, Brinstar, Norfair, Wrecked Ship, Maridia and Tourian
  progression; Energy Tanks, Map Station, Save Station, Super Missiles, Power
  Bombs, Charge Beam, suits, Grapple, X-Ray and later upgrades; later bosses,
  Metroids, Mother Brain, endings and item-percentage completion; wall-jump,
  mockball, damage boosting, bomb-jump sequence breaks, glitches, passwords,
  save states, emulation modifications, randomizers, ports and remakes.
- Direct-play status: not conducted. No cartridge, ROM, emulator, console,
  entitlement, save, screenshot, video, audio or input trace was used. The
  official manual and pinned reverse-engineered source support a bounded rules
  reconstruction rather than a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SME-001` | The packet targets the original English NTSC Japan/USA ROM identity and not a wrapper, port or modified route | Confirmed | Direct | High | P1, P2, R1 |
| `SME-002` | Ceres closes its scripted Ridley encounter into a visible one-minute real-time escape whose expiry is terminal | Confirmed | Direct | High | R2 |
| `SME-003` | The fixed Zebes opening places Morphing Ball, the first Missile Tank, a five-missile red door, Bombs and Bomb Torizo on one ordered route | Confirmed | Direct | High | P1, R2 |
| `SME-004` | Morphing Ball is retained and changes Samus's collision envelope so narrow authored passages become traversable | Confirmed | Direct | High | P1, R2 |
| `SME-005` | The first Missile Tank increases both current and maximum missile supply by five; each standard missile shot spends compatible finite reserve | Confirmed | Direct | High | P1, R2 |
| `SME-006` | A red door accepts five standard missile impacts, so the first tank's full capacity is sufficient for the scoped gate | Confirmed | Direct | High | P1, R2 |
| `SME-007` | Retained Bombs may be placed only from the compact form; their delayed blast damages enemies and compatible floors or walls | Confirmed | Direct | High | P1, R2 |
| `SME-008` | Taking the Bomb item activates the bounded Bomb Torizo encounter and the room's route exit remains unavailable until clearance | Confirmed | Direct | High | R2 |
| `SME-009` | Energy, selected special equipment, missile reserve, retained abilities and visited-room map state are inspectable before local decisions | Confirmed | Direct | High | P1, R2 |
| `SME-010` | The bomb-block exit after Bomb Torizo returns the now-upgraded avatar to the earlier main Crateria traversal network | Confirmed | Direct | High | R2 |
| `SME-011` | The signature admits only transitions causally available on the fixed Ceres-to-first-Bombs route | Observation | Direct | High | P1, P2, R1, R2, V1 |

## Basic data

- Release / origin: Nintendo R&D1 / Intelligent Systems / Nintendo; 1994 Super
  NES action-adventure. Nintendo's official archive identifies the 1994 title
  and the found-item expansion of movement and attack options.
- Platform or physical form: original licensed Super NES cartridge program;
  the exact NTSC Japan/USA build is identified by a reproducible SHA-1.
- Puzzle family: real-time system pressure; inventory and fixture dependencies;
  world topology and perspective; ordered dependency sequencing.
- Primary sources, accessed 2026-09-21:
  - **[P1]** [Nintendo of America original manual](https://www.nintendo.co.jp/clvs/manuals/common/pdf/CLV-P-SAAHE.pdf),
    pp. 8, 13–16 and 20–26, for controls, Morphing Ball posture, Bomb use, HUD
    and map disclosure, Energy, Missile Tank capacity, enemy drops and coloured
    door rules.
  - **[P2]** [official Nintendo product archive](https://www.nintendo.co.jp/clvs/soft/s_metroid.html),
    for original 1994 Super Famicom/Super NES identity and the retained
    movement/attack-option progression premise.
- Reproducible sources:
  - **[R1]** [`strager/supermetroid` at commit `b7785a19`](https://github.com/strager/supermetroid/tree/b7785a19024454ef366500243648cb64e687164b),
    whose documented NTSC Japan/USA build produces `supermetroid-ntsc.sfc` with
    SHA-1 `da957f0d63d14cb441d215462904c4fa8519c613`; this anchors exact program
    identity but is community reverse engineering, not original developer
    source.
  - **[R2]** [`InsaneFirebat/sm_disassembly` at commit `5320bff7`](https://github.com/InsaneFirebat/sm_disassembly/tree/5320bff78f3bd57da2ecf3c913570f715b276981),
    for labelled Ceres timer/Ridley state, Morph Ball, first Missile and Bomb
    Torizo room headers and PLMs, equipment collection, coloured-door and bomb-
    block resolution. This too is annotated community reverse engineering.
- Validation source:
  - **[V1]** repository-side transition reconstruction from P1, P2, R1 and R2;
    source and rules reasoning only, with no direct play or audiovisual claim.
- Claim IDs: `SME-001`–`SME-011`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly run, jump, crouch and roll through the authored Ceres,
  Crateria and Blue Brinstar room geometry.
- `ACT-161`: aim and fire the base beam or selected missiles at reachable route
  creatures, Bomb Torizo and compatible door targets.
- `ACT-164`: cycle to missiles as the active special equipment before the next
  compatible shot, then cancel or pass through the configured door behaviour.
- Generalised `ACT-202`: change between standing/crouched body states and the
  retained compact Morphing Ball configuration, which changes clearance and
  enables Bomb placement.
- Generalised `ACT-270`: while rolled into Morphing Ball form after the Bomb
  acquisition, place one reusable local Bomb and start its fuse.
- Claims: `SME-003`–`SME-007`, `SME-010`.

### System Behaviour Genes

- `SYS-215`: resolve directly controlled beam, missile and Bomb combat against
  live hostiles while movement, hostile actions and hazards continue.
- `SYS-222`: contact with an eligible Energy or Missile drop accepts only the
  amount that fits the corresponding current maximum.
- `SYS-398`: collecting Morphing Ball and Bombs sets persistent equipment state
  that remains usable at every compatible later passage or block.
- `SYS-417`: the first Missile Tank raises maximum missiles and current missiles
  by five without changing terrain by itself.
- Generalised `SYS-470`: after a placed Bomb's fuse expires, apply its bounded
  blast to overlapping enemies and compatible bomb blocks, then remove the
  temporary bomb object.
- `SYS-578`: hostile contact or attacks reduce one continuous Energy pool,
  compatible drops restore missing Energy to its cap and zero is terminal.
- Resolution order: Ceres encounter state triggers escape and the timer; escape
  transfers to Zebes; route traversal reaches one authored item PLM; collection
  sets retained equipment or missile capacity; the compatible posture, shot or
  blast opens the next edge; Bomb collection activates Bomb Torizo and the room
  gate; guardian defeat and bomb-block resolution restore the parent route.
- Claims: `SME-002`–`SME-010`.

### Constraint Genes

- `CON-068`: Ceres grants a visible `01:00` authoritative countdown; reaching
  zero before the elevator ends the attempt.
- `CON-282`: Ceres settlement/escape, Zebes landing, Morphing Ball, first
  Missile Tank, red door, Bombs, Bomb Torizo and bomb-block exit form an ordered
  authored progression chain.
- `CON-349`: low clearance requires retained Morphing Ball, the red door needs
  the acquired missile capability plus five compatible shots, and exit blocks
  require retained Bombs at their locus.
- `CON-402`: the Bomb Torizo room's grey route exit remains unavailable until
  the finite guardian encounter is cleared.
- `CON-578`: missiles fire only while the compatible finite reserve can pay one
  shot; refill drops cannot exceed the retained maximum.
- Scarce route state: Energy, current/max missiles, remaining Ceres time,
  retained ability flags, item/guardian events and opened route edges.
- Claims: `SME-002`, `SME-003`, `SME-005`–`SME-010`.

### Information Genes

- `INF-073`: the HUD exposes selected missiles and current compatible reserve
  before a shot.
- `INF-119`: Energy, missile supply and the acquired Morphing Ball/Bomb build
  are visible or inspectable before route and combat decisions.
- `INF-125`: the HUD minimap and pause map expose Samus's current position and
  visited room geometry; unvisited and hidden topology remains undisclosed.
- Claims: `SME-009`.

### Objective Genes

- New `OBJ-198`: acquire Morphing Ball, first Missile capacity and Bombs in
  dependency order, clear Bomb Torizo, then use retained Bombs to reopen the
  route into the main Crateria vertical shaft.
- Success, evaluation and failure: possession of Bombs or guardian defeat alone
  is insufficient; the bomb-block edge must be opened and crossed with all
  three acquisition states retained. Ceres timeout or zero Energy is failure.
- Claims: `SME-003`, `SME-008`, `SME-010`.

### Time Genes

- `TIM-003`: navigation, aim, combat, body configuration and Bomb placement are
  accepted while enemies, hazards and the Ceres countdown advance in real time.
- Claims: `SME-002`, `SME-007`, `SME-008`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Ceres Ridley encounter is active | survive the scripted combat settlement | the encounter transfers into station self-destruct state and the visible timer is set to `01:00` | forced real-time escape | `SME-002` |
| Self-destruct time remains and the Ceres elevator is reachable | traverse back to the elevator | reaching it before zero completes escape and transfers the opening to Zebes; zero instead terminates the attempt | deadline-gated route | `SME-002`, `SME-003` |
| Morphing Ball PLM remains uncollected in Blue Brinstar | contact the item | the retained Morphing Ball equipment bit is set and ordinary control resumes | persistent compact capability | `SME-004` |
| A low passage blocks standing clearance | crouch, enter Morphing Ball and move through it | collision envelope becomes compact and the authored passage is traversable; leaving the form restores ordinary body configuration | capability-gated topology | `SME-004` |
| First Missile Tank Chozo orb remains | break the orb and contact the item | current and maximum missiles each increase by five and the HUD reflects the reserve | permanent capacity booster | `SME-005` |
| The scoped red door is closed and five missiles remain | select missiles and land five shots | each shot spends one missile; the fifth compatible impact opens the door | typed finite-resource gate | `SME-005`, `SME-006` |
| Bombs Chozo orb remains in the Bomb Torizo room | break the orb and collect Bombs | Bomb equipment is retained and the authored Bomb Torizo activation sequence begins | acquisition-triggered encounter | `SME-007`, `SME-008` |
| Bomb Torizo is active and the exit is unavailable | move, aim and fire while preserving Energy | bounded hostile health reaches defeat, the encounter flag settles and the grey-door restriction clears | finite hostile-clearance gate | `SME-008` |
| Compatible bomb blocks still seal the return edge | enter Morphing Ball, place Bomb and wait for fuse | the blast damages overlapping eligible targets, destroys compatible blocks and removes the Bomb object | reusable timed room-state change | `SME-007`, `SME-010` |
| Bomb blocks are absent and all three acquisition states remain | cross the opened edge | ordinary control returns to the main Crateria vertical shaft with retained Morphing Ball, missile capacity and Bombs | scoped positive terminal | `SME-010` |

## Strategic and experiential structure

- Local decision: align a jump or compact roll with current room geometry;
  choose beam versus scarce missiles; preserve Energy while reading hostile
  motion; position a delayed Bomb where its radius overlaps a compatible block.
- Medium-term planning: remember low passages and coloured doors, collect the
  exact capacity their gate needs, backtrack without wasting missiles, and
  enter Bomb Torizo with enough Energy to preserve the acquired route state.
- Long-term structure: turn three authored pickups into permanent changes to
  the set of usable edges: compact clearance, typed projectile access and
  delayed local destruction. The route deliberately folds back into its parent
  shaft to demonstrate that acquisition changes topology rather than merely
  advancing a linear corridor.
- Common heuristics: inspect the map for visited branches; preserve missiles for
  the red door; test newly acquired capabilities on nearby geometry; place
  Bombs from a safe offset; do not treat Bomb acquisition as terminal before
  the guardian and exit blocks are resolved.
- Failure attribution: HUD Energy/missiles, selected-item state, timer, map,
  item message, door colour, room closure and bomb-block response distinguish
  depleted reserve, wrong capability, incomplete clearance and missed deadline.
  Enemy drops remain bounded uncertainty.
- Claims: `SME-002`–`SME-011`.

## Replay and variation

- What changes between attempts: movement timing, ordinary hostile contact,
  shot count against enemies, drops, Energy and missile remainder, Bomb
  placement and the time left after Ceres escape.
- Randomness or procedural generation: the room graph, item positions, doors,
  guardian and route events are authored; eligible enemy drops may vary.
- Multiple viable strategies: the commercial game permits sequence breaks and
  later routing choices, but this evidence packet fixes the intended early
  capability order so its transitions remain reproducible.
- Typical replay motive: faster routing, higher survival margin, item
  completion or sequence breaking. Only the ordinary fixed early route enters
  this record.
- Claims: `SME-003`–`SME-011`.

## Adjacent systems and history

- Direct predecessors: Metroid established ability-gated side-view exploration;
  Super Metroid makes the early retained-capability/backtrack loop explicit
  through readable item, map, door and room-state feedback.
- Variants: PAL timing, later official wrappers, randomizers and ROM hacks need
  their own version evidence; they do not inherit this exact packet.
- Similar games: Hollow Knight: Silksong shares retained traversal capabilities,
  capability-gated edges, live combat, personal resources and explored-map
  route planning.
- Important difference: Silksong's accepted route crosses a long Act 1 chain
  into the Citadel, while this packet closes much earlier by using Bombs to
  reopen an edge into an already traversed Crateria network.

## Normalised genome

The front matter is canonical. The complete signature contains 21 Active
genes: five Action, six System Behaviour, five Constraint, three Information,
one Objective and one Time gene. Character, room, item, enemy and numeric gate
labels remain carrier parameters.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `336` (`GAME-0001`–`GAME-0336`).
- Exact genome matches: none.
- Tied near matches: `GAME-0272` — Serious Sam 4 (`11 / 26 = 0.423077`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0272` — Serious Sam 4 | `ACT-008`, `ACT-161`, `ACT-164`, `SYS-215`, `SYS-222`, `SYS-578`, `CON-402`, `CON-578`, `INF-073`, `INF-119`, `TIM-003` | Both packets directly navigate and aim through live hostile rooms, select weapons, spend finite missiles, collect world pickups and monitor Energy/ammunition. Serious Sam 4 uses magazine reload, perceived pursuit, finite-group clearance and an authored level exit. Super Metroid instead retains compact form and Bombs, uses them to alter previously visited topology and destroy compatible blocks, exposes an area map and closes on a capability-chain return rather than clearance. | Near, `11 / 26 = 0.423077` |

## Taxonomy impact

`OBJ-198` is new. `TAXONOMY_CHANGE_080` generalises `ACT-202`, `ACT-270` and
`SYS-470` so a retained compact body configuration and reusable bomb capability
fit the same configuration, placed-fuse and bounded-blast boundaries as their
earlier carriers. Stable support is added to `ACT-008`, `ACT-161`, `ACT-164`,
`SYS-215`, `SYS-222`, `SYS-398`, `SYS-417`, `SYS-578`, `CON-068`, `CON-282`,
`CON-349`, `CON-402`, `CON-578`, `INF-073`, `INF-119`, `INF-125` and `TIM-003`
without changing their boundaries. No earlier signature changes.

## Negative results

- No verified combination is registered from one new carrier.
- No direct play, ROM possession, emulation, audiovisual observation, save or
  cartridge parity test is claimed.
- Community disassemblies are identified as reverse engineering and never
  represented as Nintendo or original developer source.
- The route does not infer later item abilities, boss rules, regions, endings,
  item completion, save/continue restoration or sequence-break techniques.
- Morphing Ball and Bombs are not inventory objects consumed on use; they are
  retained capabilities under `SYS-398`.
- Bomb placement reuses `ACT-270` only after generalising finite stock to a
  supply-model parameter; no fictitious bomb inventory is assigned.
- `OBJ-080` is rejected because the packet reconnects to an earlier parent
  network rather than crossing a guardian-opened threshold into a new region.

## Delta summary

## New facts

- [Confirmed | Direct | High] Nintendo's manual and pinned exact-ROM source
  close a one-minute escape, three ordered acquisitions, one typed missile
  gate, one finite guardian and one bomb-block return edge.
- [Confirmed | Direct | High] The Bomb and Morphing Ball rules change the set of
  usable authored edges while Energy, missiles and hostile rooms continue in
  real time.

## New genes

- [Confirmed | Direct | High] `OBJ-198` isolates the terminal in which an
  ordered retained capability chain clears its guardian and reopens a route
  into the parent traversal network.

## New combinations

- [Observation | Direct | High] None; recurrence remains evidence-driven.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_080` generalises three
  configuration/bomb boundaries without changing their causal tests or any
  earlier signature.

## New questions

- Which later bounded game independently closes a route by applying a newly
  retained capability to an earlier authored edge rather than only proceeding
  forward?
- Does a later Super Metroid packet require separate sequence-break genes, or
  are those techniques versioned route parameters outside ordinary rules?

## Next recommended game

- `GAME-0338` Final Fantasy VII, as reserved by selection 023.

## Why this game

- Super Metroid is a recognisable console anchor whose opening demonstrates in
  one short loop that permanent abilities are changes to navigable topology:
  collect, remember, backtrack, reopen and return under live combat pressure.
