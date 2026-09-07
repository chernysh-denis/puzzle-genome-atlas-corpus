---
game_id: GAME-0267
slug: kerbal-space-program
game_title: Kerbal Space Program
analysis_status: reviewed
reviewed: 2026-09-06
combination_ids:
  - COMB-0265
gene_ids:
  action:
    - ACT-028
    - ACT-392
    - ACT-444
  system:
    - SYS-036
    - SYS-811
    - SYS-812
  constraint:
    - CON-610
  information:
    - INF-324
  objective:
    - OBJ-161
  time:
    - TIM-002
    - TIM-003
---

# Game: Kerbal Space Program

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `220200`, sole one-app package `27437`, on the default public branch carrying
  build `10132464`, whose branch record was updated 2023-01-11; checked
  2026-09-06. The publisher's own announcement `Kerbal Space Program 1.12.5 is
  live` is dated 2023-01-11, the same day the branch was updated, so unlike the
  two preceding units in this batch the semantic version is unambiguous:
  `1.12.5`. The later 2023-01-25 announcement changed only the separate
  launcher and did not move the public branch.
- Product boundary: this is **Kerbal Space Program** on Windows, not Kerbal
  Space Program 2, which is a separate application. The two listed DLC apps
  `283740` and `982970` are separate products outside this packet, as are all
  Steam Workshop contents and every third-party modification. The application
  also publishes opt-in legacy version branches; this packet uses only the
  default public branch.
- Platform, input and difficulty: English interface, Windows, keyboard and
  mouse, single-player. The declared configuration is a new `Sandbox` save, in
  which every part is unlocked, parts cost no funds and may be used without
  limit, and the science system does not function.
- Setup-only predecessor: creating the `Sandbox` save and entering the assembly
  building with an empty workspace. Nothing is carried in from another save.
- Entry: accept first ordinary control in the assembly building with an empty
  craft, before the first part is attached.
- Primary decision loop: place and orient parts against the compatible
  attachment points of the growing craft, so that the assembly's own topology
  decides which reservoirs each engine can draw from; distribute those parts
  across an ordered list of activation steps and reorder that list until it
  matches the intended sequence; launch, then continuously command the craft's
  throttle, pitch, yaw and roll while the simulation integrates thrust,
  changing mass, atmospheric drag and gravity into a continuous trajectory;
  advance the activation list by one step whenever a spent element must be
  released or the next engine lit; read the projected path's labelled highest
  and lowest points in the map view and compare them against the declared
  atmospheric boundary; and act on that comparison until the projection closes
  into a repeating orbit.
- Positive terminal: bring the projected path to a closed repeating orbit about
  the home body whose lowest point lies above the body's declared atmospheric
  depth, then save the game, load that save and verify that the same closed
  orbit and its labelled extremes return. Stop without leaving the home body's
  influence.
- Negative terminal: the attempt fails when the craft is destroyed, when it
  returns to the surface, or when the projected lowest point remains inside the
  atmospheric boundary so the path decays instead of repeating. Reaching a high
  point above the boundary while the low point stays inside it is a suborbital
  trajectory and is not success.
- Included: part placement and orientation against compatible attachment
  points; the attachment topology that decides propellant connectivity;
  authoring and advancing the ordered activation sequence; direct throttle and
  three-axis attitude command; continuous integration of thrust, mass,
  atmospheric drag, gravity and collision; propellant drawn through the
  assembled topology with the resulting continuous mass loss; resolution of the
  present motion into a projected conic path with labelled extremes; the
  atmospheric boundary that decides whether that path closes; the untimed
  assembly phase and the real-time flight phase; and the reload-verified orbit.
- Excluded: Kerbal Space Program 2; both DLC apps; Steam Workshop content and
  every third-party modification; the opt-in legacy version branches; `Science`
  and `Career` modes with their funds, science, reputation, contracts and
  technology tree; crewed extravehicular activity, docking, rendezvous,
  manoeuvre-node planning and every destination beyond the home body's
  influence; recovery, reverting and the flight-scene time-warp controls, which
  the declared route does not require; the in-assembly derived performance
  readout, excluded as a bounded evidence gap because only community prose
  attests it; all inputs and platforms not declared above; screenshots,
  official artwork, third-party assets, video and audio evidence.
- Reproducible parameterisation: install English app `220200` from package
  `27437`, confirm the default public branch and version `1.12.5`, and create a
  new `Sandbox` save. In the assembly building, attach a command part, at least
  one propellant reservoir and at least one engine, and add at least one
  separating part so the activation list contains at least two steps; reorder
  that list at least once. Launch, advance the sequence at least twice, command
  throttle and all three rotational axes, and use the map view's labelled
  extremes to raise the lowest point above the declared atmospheric depth.
  Then save, reload and confirm the retained orbit. Exact parts, masses,
  altitudes, burn timings and the resulting orbit are parameters.
- Potential scoped modules: `Science` or `Career` mode with its economy; a
  docking or rendezvous task; a transfer beyond the home body's influence; a
  DLC part set; or an aircraft flight in the other assembly building requires
  its own version, entry, loop, terminal and evidence.
- Direct-play status: not conducted. Valve application and package data plus
  the current Steam product record establish lawful availability, exact product
  identity, Windows support, the sole package, the single-player category,
  Steam Workshop support and the two separate DLC apps. The publisher's own
  dated announcement establishes version `1.12.5` and the public SteamCMD info
  projection confirms the matching branch date and the existence of opt-in
  legacy branches. No publisher documentation of the assembly building's
  placement-refusal rule could be obtained: the community wiki tutorial the
  previous unit mistook for the product's manual is user-editable and outdated,
  the publisher's own patch notes cover EVA construction mode instead, and the
  in-game KSPedia cannot be read without direct play. Wiki material, reached
  through search because the wiki host refuses direct retrieval from this
  environment, corroborates the
  `Sandbox` mode rules, the assembly building's staging list and its reordering,
  the single input that advances the list by one step, separating parts creating
  steps, attachment-point crossfeed, the home body's declared atmospheric depth,
  the requirement that a low orbit's lowest point clear that depth, and the map
  view's labelled highest and lowest points. This is an evidence-backed rules
  reconstruction, not a claimed playthrough or entitlement. No video or audio
  was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `KSP-001` | Steam app `220200` and its sole one-app package `27437` identify the currently lawfully offered English Windows product, which has two separate DLC apps and Steam Workshop support | Confirmed | Direct | High | P1, P2 |
| `KSP-002` | The publisher's announcement of version `1.12.5` is dated 2023-01-11 and the public branch record was updated the same day, so the semantic version is unambiguous | Confirmed | Corroborated | High | P3, S1 |
| `KSP-003` | The 2023-01-25 announcement changed only the separate launcher and did not move the public branch | Observation | Corroborated | High | P4, S1 |
| `KSP-004` | The application publishes opt-in legacy version branches alongside the default public branch | Observation | Limited | Medium | S1 |
| `KSP-005` | In `Sandbox` mode all parts start unlocked, cost no funds and may be used without limit, and the science system does not function | Observation | Corroborated | High | S2 |
| `KSP-006` | Staging is managed by adding steps and rearranging icons in a list in the assembly building, and a new step is created when a separating part is placed | Observation | Limited | Medium | S3 |
| `KSP-007` | A single repeated input advances the craft to the next activation step, and separating parts irreversibly detach the components they hold | Observation | Limited | Medium | S3 |
| `KSP-008` | Propellant crossfeed is configured per attachment point, so the assembly's connectivity determines which reservoirs an engine can draw from | Observation | Limited | Low | S4 |
| `KSP-009` | The home body's atmosphere has a declared depth of 70,000 metres in the reviewed version line | Observation | Limited | Medium | S5 |
| `KSP-010` | A low orbit's lowest point must stay above that declared depth to remain clear of atmospheric drag | Observation | Limited | Medium | S5, S6 |
| `KSP-011` | The map view exposes the projected path's highest and lowest points, conventionally abbreviated in the interface | Observation | Limited | Medium | S6 |
| `KSP-012` | Symmetry in the assembly building is used so that the centre of mass and centre of thrust remain on the craft's main axis | Observation | Limited | Low | S3 |
| `KSP-013` | The bounded identity is a craft whose flight behaviour is a direct consequence of how the player connected and ordered it, judged against a published altitude the interface already projects | Strong Pattern | Corroborated | Medium | `KSP-005`–`KSP-012` |
| `KSP-014` | Player discussion and one outdated community wiki tutorial both report that the editor marks a colliding part red and refuses to attach it; no publisher documentation retrievable here states the stock assembly building's placement-rejection rule | Observation | Limited | Low | S7, S8 |
| `KSP-016` | Publisher patch notes for `1.12.2` record making non-surface-placeable items refuse placement while intersecting other parts in EVA construction mode, a mode this packet excludes | Observation | Direct | Medium | P5 |
| `KSP-015` | The cheat menu's part-clipping option removes both refusals and makes all nodes active | Observation | Limited | Medium | S7 |

## Basic data

- Release / origin: Squad; published on Windows by Private Division and
  released 2015-04-27.
- Platform or physical form: lawfully offered English Windows single-player
  Steam application `220200`; one `Sandbox` assemble-launch-orbit task about
  the home body.
- Puzzle family: spatial assembly and packing; physics and object manipulation;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-06:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=220200&cc=ua&l=english),
    for the exact title, app, Windows support, developer and publisher, release
    date, the `Indie` and `Simulation` genres with no Early Access marker, the
    single-player-only category list, Steam Workshop support, the two DLC apps,
    the sole package and the current Ukraine offer.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=27437&cc=ua&l=english),
    for package `27437` containing only app `220200` and its current Ukraine
    offer.
  - **[P3]** [the publisher's own `Kerbal Space Program 1.12.5 is live` announcement](https://store.steampowered.com/news/app/220200),
    dated 2023-01-11, for the current semantic version and its change log.
  - **[P4]** [the publisher's own `Small Patch` announcement](https://store.steampowered.com/news/app/220200),
    dated 2023-01-25, stating that the update applied to the launcher, that the
    launcher would no longer remain running during play and that an optional
    account login flow was added. Embedded media was not opened or used.
- Corroborating textual sources, accessed 2026-09-06:
  - **[P5]** [the publisher's own patch-note feed for app
    `220200`](https://steamcommunity.com/games/220200/rss/), fetched in full on
    2026-09-07, for the `1.12.2` lines "Fix parts being able to attach in
    construction mode when colliding with ground" and "Non-surface placeable
    items can no longer be dropped or placed while intersecting other parts".
    Both concern EVA construction mode, which this packet excludes, so they
    establish `KSP-016` and nothing about the assembly building's own rule.
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/220200),
    for public branch build `10132464`, its 2023-01-11 branch update and the
    list of opt-in legacy version branches. This mirrors Valve's public product
    data and is treated as a secondary distribution observation, not a
    publisher claim.
  - **[S2]** [product wiki, Sandbox](https://wiki.kerbalspaceprogram.com/wiki/Sandbox),
    for all parts starting unlocked, costing no funds, being usable without
    limit, and the science system not functioning in this mode. The wiki host
    refuses direct retrieval from this environment, so its content was reached
    through search indexing rather than by fetching the page.
  - **[S3]** [product wiki, Stage](https://wiki.kerbalspaceprogram.com/wiki/Stage),
    together with its linked `Decoupler and separator` and
    `Asparagus staging` pages, for the staging list and its rearrangement in
    the assembly building, a new step being created when a separating part is
    placed, the single input that advances to the next step, separating parts
    irreversibly detaching what they hold, and symmetry being used to keep the
    centre of mass and centre of thrust on the craft's main axis.
  - **[S4]** [product wiki version notes on crossfeed](https://wiki.kerbalspaceprogram.com/index.php?title=1.2),
    for crossfeed being configurable per attachment point, so the assembly's
    connectivity decides which reservoirs feed which engine.
  - **[S5]** [product wiki, Kerbin](https://wiki.kerbalspaceprogram.com/wiki/Kerbin),
    together with its linked `Atmosphere` page, for the home body's declared
    atmospheric depth of 70,000 metres.
  - **[S6]** [product wiki, Orbit](https://wiki.kerbalspaceprogram.com/wiki/Orbit),
    together with its linked `Basic maneuvers` page, for a low orbit's lowest
    point needing to clear the declared atmospheric depth and for the map
    view's labelled highest and lowest points.
  - **[S7]** [player discussion thread on the editor's refusal
    behaviour](https://steamcommunity.com/app/220200/discussions/0/558747287304253472/),
    retrieved in full on 2026-09-06, for parts appearing red and refusing to
    attach because of collision with an already placed part, and for the cheat
    menu's part-clipping option removing that refusal and making all nodes
    active. This is player discussion, not documentation, so it supports the
    refusal boundary only as corroboration of `S8`, and it is the sole support
    for `KSP-015`, which is why that claim stays at `Limited` evidence.
  - **[S8]** [community wiki tutorial,
    `Tutorial:Game Manual`](https://wiki.kerbalspaceprogram.com/wiki/Tutorial:Game_Manual),
    accessed 2026-09-06, for the statement that a selected part glowing green
    may be placed while one glowing red may not, "because either there is no
    node to attach it to (if it requires nodes), or it is currently 'clipping'
    (colliding) with a previously placed part". **This is not the product's own
    manual.** Review finding `R-08` established that it is a user-editable
    article in the wiki's `Tutorial:` namespace, last edited in 2016 and
    carrying the wiki's `Outdated` template; the official site links to the wiki
    as a community destination, which does not make its articles publisher
    documentation. It belongs to the same host and the same corroborating family
    as `S2`–`S6`, so it is not independent of them, and the host refuses direct
    retrieval from this environment, so the passage was reached through search
    indexing rather than read in full. It corroborates the mechanic; it
    establishes nothing.
- Source-class and retrieval limitation, recorded for
  `BATCH_015_GENE_AUDIT_001` finding `A-08`: `S2` through `S6` are pages of one
  wiki and are one corroborating family, not five independent sources. That host
  refuses direct retrieval from this environment behind a challenge page, so
  none of them was fetched; their content was reached only through search
  indexing. The wiki is hosted on the product's own domain, but this unit found
  no statement of publisher ownership, so it is described as the product wiki
  rather than as publisher documentation. Repeated attempts to replace it with
  fetchable material failed: the mirrored fan wiki refuses retrieval outright,
  and the one fetchable static planet reference states an atmospheric height of
  `69,077.553` metres, which is the pre-1.0 model and therefore contradicts the
  `70,000` figure for the reviewed version line rather than corroborating it.
  Every claim resting on that family — `KSP-006` through `KSP-012` — is
  therefore downgraded to `Limited` evidence with `Medium` or `Low` confidence,
  and `KSP-013` to `Medium` confidence. No claim in this record is presented as
  though a complete page was read when it was not.
- Editor-legality evidence, recorded for review findings `R-03` and `R-08`: the
  packet has never had documentation for the assembly building's
  placement-rejection rule. `S8` was described in the previous unit as the
  product's own manual and regraded on that basis; that was wrong. It is a
  user-editable community wiki tutorial, last edited in 2016 and marked
  `Outdated`, on the same host and in the same corroborating family as
  `S2`–`S6`, so it neither is publisher documentation nor corroborates them
  independently. `S7` is a separate family but is player discussion. `P5` is
  genuinely publisher-authored but describes EVA construction mode, which this
  packet excludes. `KSP-014` is therefore graded `Limited` and `Low`, `KSP-015`
  stays `Limited` and `Medium`, and the `CON-062` reuse they were supporting is
  removed rather than retained on evidence of this grade.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P5` and `S1`–`S8` under the declared app, package, branch, version,
  platform, input, mode, clean save, exclusions and terminal; rules reasoning,
  not direct play.
- Claim IDs: `KSP-001`–`KSP-016`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-028`: during the untimed assembly phase, place, remove and
  orient persistent components whose relative geometry determines what the
  later flight can do. The Opus Magnum, Infinifactory and Railbound boundary
  already covers an editable design phase whose geometry governs a later
  execution, so no assembly gene was created; symmetry and attachment-point
  choice are its declared placement-topology and orientation parameters.
- Existing `ACT-392`: continuously command the craft's throttle, pitch, yaw and
  roll through open three-dimensional space. The boundary already covered
  direct four-axis flight control and only its wording was product-specific, so
  it was generalised rather than duplicated. `ACT-321` was rejected because it
  resolves fixed-wing flight through runway take-off, control surfaces and
  wheel braking, and `ACT-290` was rejected as ground driving.
- New `ACT-444`: distribute the craft's parts across an ordered activation list,
  reorder it freely at rest, and advance it one irreversible step at a time in
  flight. `ACT-028` explicitly excludes editing the commands that control a
  placed mechanism, `ACT-046` writes a spatial instruction field and `ACT-120`
  configures one entity's local operating rule; none covers one ordered list
  authored at rest and consumed under pressure.
- Part, engine, body and exact quantity names remain parameters. Claims:
  `KSP-005`–`KSP-012`.

### System Behaviour Genes

- Existing `SYS-036`: while simulation time runs, the craft continuously changes
  position and velocity under thrust, gravity, atmospheric drag and collision,
  including between player commands.
- New `SYS-811`: an operating engine draws propellant from the reservoirs the
  player's own assembly made reachable, following attachment-point connectivity
  rather than a global pool, and the consumed propellant leaves the craft so its
  mass falls continuously. `SYS-158` pools a network and throttles consumers,
  `SYS-237` debits a shared reserve restored by charging, and none ties
  consumption to a player-authored connectivity graph or to continuous mass
  loss.
- New `SYS-812`: the present position and velocity relative to the dominant
  attracting body are continuously converted into the conic path the craft would
  follow unpowered, and that path's extreme altitudes are exposed. No existing
  system gene converts a live physical state into a projected closed-or-open
  path the player is expected to steer toward.
- Resolution order: the assembly's attachment topology fixes which reservoirs
  feed which engine; a launched craft integrates thrust, current mass, drag and
  gravity into continuous motion; propellant consumption lowers the mass that
  the same integration uses next; the resulting state is projected into a conic
  path whose extremes are exposed; and each advance of the activation list
  irreversibly changes which parts are attached and which engine is lit. Claims:
  `KSP-006`–`KSP-011`.

### Constraint Genes

- `CON-062` is **not** carried by this packet.
  [`TAXONOMY_CHANGE_032`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_032.md)
  removed the reuse, because after three attempts this record still cannot
  evidence the gene's boundary — a placement refused when a declared footprint
  overlaps an incompatible placed component, and refused when the required
  anchor or port is unavailable — for the declared stock assembly building.
  `BATCH_015_GENE_AUDIT_001` finding `A-02` first asked whether the record had
  confused attachment topology with collision legality; review finding `R-03`
  held that one player thread was not enough; and review finding `R-08`
  established that the wiki tutorial the previous unit then relied on is a
  user-editable community article carrying an `Outdated` template, not the
  product's own manual. No publisher-hosted PC manual or KSPedia export is
  retrievable, the in-game KSPedia cannot be read without direct play, which
  this packet declares it did not conduct, and silent direct visual
  verification was not available in this environment. The nearest publisher
  evidence — the 1.12.2 patch notes in `P5` — concerns EVA construction mode,
  which this packet excludes, and describes fixes to intersecting placement
  there rather than the assembly building's general rule. The honest result is
  removal: the assembly phase keeps `ACT-028` for the placement itself, and the
  packet simply does not claim a placement-legality Constraint.
- New `CON-610`: a stable closed orbit is legal only when the projected lowest
  point lies above the attracting body's declared atmospheric depth, because a
  path whose lowest point stays inside that depth decays instead of repeating.
- Scarce resources: propellant in each connected reservoir, the ordered
  activation steps once advanced, craft mass, and the margin between the
  projected lowest point and the atmospheric boundary. Exact values are
  parameters. Claims: `KSP-008`–`KSP-011`.

### Information Genes

- New `INF-324`: a dedicated view draws the path the craft would follow under
  its current motion alone and labels that path's highest and lowest points, so
  both can be compared with the declared boundary before acting. `INF-226`
  reports only present attitude, speed, altitude and engine state; `INF-322`
  draws a static reach at a candidate position; neither projects the player's
  own uncorrected future.
- Exact map projection, icons, abbreviations and units are presentation
  parameters. Claims: `KSP-010`, `KSP-011`.

### Objective Genes

- New `OBJ-161`: bring the projected path to a closed repeating orbit about the
  declared body with its lowest point above the atmospheric boundary, and retain
  that state through a persistence check. Every existing bounded objective in
  the corpus resolves against a place, a target set, a quota, a schedule or an
  opponent; none is satisfied by a property of a trajectory.
- A high point above the boundary with the low point still inside it is a
  suborbital trajectory and is not success. Claims: `KSP-010`, `KSP-013`.

### Time Genes

- Existing `TIM-002`: the assembly phase imposes no time-driven system step, so
  the player may pause indefinitely between placements and reorderings.
- Existing `TIM-003`: once launched, the simulation advances on a real-time
  schedule while throttle, attitude and staging inputs remain accepted.
- The packet therefore carries two time structures, because the same craft is
  authored without pressure and then flown under it. Claims: `KSP-006`,
  `KSP-007`, `KSP-011`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A new `Sandbox` save is open with an empty workspace | Accept first control in the assembly building | Every part is available, none costs funds and no science system is active | fixed clean entry | `KSP-005` |
| A part is held over an incompatible position | Attempt to attach it | The attachment is refused | anchor-and-port legality | `KSP-006` |
| A separating part is placed on the craft | Observe the activation list | A new step appears holding that part | assembly authors the sequence | `KSP-006` |
| The activation list holds several steps | Drag one step to another position | The order changes and the craft is unaffected until launch | untimed reordering | `KSP-006` |
| An engine is attached through a chain of connected reservoirs | Run it | It draws from those reservoirs and not from unconnected ones | topology decides flow | `KSP-008` |
| An engine runs for a period | Observe the craft | Its total mass falls continuously as propellant leaves it | continuous mass loss | `KSP-008` |
| The craft is in flight and the next step must fire | Give the advance input once | The list advances exactly one step and its parts are irreversibly released or lit | one-step irreversible advance | `KSP-007` |
| The craft is under thrust inside the atmosphere | Command throttle and attitude | Thrust, current mass, drag and gravity integrate into a continuously changing trajectory | continuous integration | `KSP-009` |
| The craft has left the dense atmosphere | Open the map view | The projected path is drawn with its highest and lowest points labelled | projected extremes | `KSP-011` |
| The projected high point is above the boundary and the low point is inside it | Stop thrusting | The path does not repeat; it returns to the surface | suborbital is not orbit | `KSP-010` |
| The projected low point is inside the boundary | Thrust near the high point | The low point rises and the projection approaches closure | boundary-directed correction | `KSP-010` |
| The projected low point clears the declared atmospheric depth | Stop thrusting | The path closes into a repeating orbit | closed-orbit legality | `KSP-009`, `KSP-010` |
| A closed orbit is established | Save, quit and load that save | The same closed orbit and its labelled extremes return | reproducible positive terminal | `KSP-013` |

## Strategic and experiential structure

- Planning horizon: the assembly decides what the flight can possibly do, so
  the untimed phase carries almost all of the risk; the flight is mostly the
  discovery of whether that judgement was right.
- Local tactics: keep the connected reservoirs feeding the engine that needs
  them, put separating parts where the ordered list will release dead mass
  rather than live propellant, raise the projected high point first and then
  return to it to lift the low point clear of the boundary.
- Medium-term structure: mass falls as propellant burns, so the same throttle
  produces more acceleration later, and the activation list converts a craft
  that could not lift itself into a sequence of lighter craft that can.
- Reversible versus irreversible: every assembly decision is freely reversible
  until launch and none is reversible afterwards; each advance of the activation
  list is irreversible; propellant never returns.
- Failure attribution: the projected extremes make a failure traceable to a
  specific shortfall, a step advanced too early or a connection the assembly
  never made, rather than to hidden state.
- Player trust: the boundary is a published altitude, the projection is drawn
  before it is needed, the activation list is authored by the player and shown
  in order, and the reloaded save reproduces the settled orbit exactly.

## Replay and variation

- What changes: the parts chosen, how they are connected, how the activation
  list is ordered, the ascent profile and how much margin the final orbit keeps
  above the boundary.
- Randomness or procedural generation: the body, its atmospheric depth, the
  parts and the physics are fixed. Nothing in this packet is randomised.
- Multiple strategies: the task admits a single large step, several small ones
  or a connectivity that feeds one engine from many reservoirs. The control
  demonstrates at least two steps and one reordering rather than making a
  minimum-part or minimum-propellant craft the terminal.
- Typical replay motive: reach the same closed orbit with less propellant, or
  with an activation list that discards dead mass earlier.

## Adjacent systems and history

- Human: Fall Flat shares continuous force-constrained body dynamics under
  real-time control, but its bodies are not assembled by the player and its
  objectives are places rather than trajectories.
- Infinifactory shares the untimed editable design phase and the same
  anchor-and-port placement legality, but its committed run executes
  automatically and is judged by delivered product rather than by the player
  flying the result.
- STAR WARS: Squadrons shares the direct four-axis flight boundary this unit
  generalised, but its craft is fixed by the mission and neither its mass nor
  its connectivity is a player decision.
- Microsoft Flight Simulator 2024 shares continuous atmospheric flight, but
  resolves it through fixed-wing aerodynamics, runway operations and cockpit
  instruments rather than through staged assembly and projected orbital
  extremes.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-028`, `ACT-392`, `ACT-444` | part, engine, symmetry mode and step count are parameters |
| System Behaviour | `SYS-036`, `SYS-811`, `SYS-812` | masses, flow rates, drag model and conic maths are parameters |
| Constraint | `CON-610` | the declared atmospheric depth and the required margin are parameters |
| Information | `INF-324` | projection style, abbreviations and units are parameters |
| Objective | `OBJ-161` | body, boundary and required margin are parameters |
| Time | `TIM-002`, `TIM-003` | assembly pace and flight timestep are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `266` (`GAME-0001`–`GAME-0266`).
- Exact genome matches: none.
- Tied near matches: `GAME-0112` — Human: Fall Flat (`2 / 17 = 0.117647`).
- Supported combination subsets: `COMB-0265`.
- Scan date: 2026-09-06.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0112` — Human: Fall Flat | `SYS-036`, `TIM-003` | Both resolve a physical body's motion continuously under forces, collisions and constraints while the player keeps issuing real-time commands. Human: Fall Flat gives the player a fixed body it did not build and asks it to reach places; every property of the body is authored in advance. This packet makes the body itself the player's construction: its attachment topology decides which reservoirs feed which engine, its ordered activation list is authored at rest and consumed irreversibly under pressure, its mass falls continuously as propellant leaves it, and success is not a place at all but a property of the projected trajectory measured against a published altitude. The very low score reflects that only the physics substrate is shared. | Near, `0.117647` |

### Preserved research notes

- New genes: `ACT-444`, `SYS-811`, `SYS-812`, `CON-610`, `INF-324`, `OBJ-161`.
- Reused genes: `ACT-028`, `ACT-392`, `SYS-036`, `TIM-002`, `TIM-003`.
  `CON-062` was reused here at acceptance and was removed by
  `TAXONOMY_CHANGE_032`.
- Classification result: `New gene`.
- Lower-ID scan: reuse `ACT-028` for the assembly phase rather than creating an
  assembly gene, because the Opus Magnum, Infinifactory and Railbound boundary
  already covers an editable design phase whose geometry governs a later
  execution; `CON-062` was reused alongside it at acceptance and has since been
  removed by `TAXONOMY_CHANGE_032` for want of evidence; reuse `SYS-036` for the physical integration;
  reuse `TIM-002` and `TIM-003` for the two time structures rather than forcing
  one. Generalise `ACT-392` rather than adding a rocket-piloting gene, because a
  different vehicle is a parameter and not a new action; reject `ACT-321` and
  `ACT-290` on their stated boundaries. Reject `TIM-006` and `TIM-009` because
  both require the committed run to execute automatically, while this flight is
  piloted throughout. Reject `SYS-158` and `SYS-237` for propellant flow.
  Reject a part-, engine-, body- or mode-named gene.

## Taxonomy impact

- Registry changes: add `ACT-444`, `SYS-811`, `SYS-812`, `CON-610`, `INF-324`,
  `OBJ-161` and `COMB-0265`, plus independent evidence for six reused genes.
  Generalise only the wording of `ACT-392` from a product-specific cockpit
  starfighter label to the same portable throttle-and-three-axis-attitude
  boundary; its control semantics, lifecycle and the `GAME-0225` carrier
  signature remain unchanged. The signature this record was accepted with held
  twelve genes; it now holds eleven.
- Registry changes recorded by `BATCH_015_GENE_AUDIT_001` findings `A-02` and
  `A-08` and by review findings `R-03` and `R-08`: the `CON-062` assignment is
  **removed** under
  [`TAXONOMY_CHANGE_032`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_032.md),
  because no source of the required class establishes the boundary here.
  `KSP-014` is restated as what its sources actually support and regraded
  `Limited`/`Low`, `KSP-015` stays `Limited`/`Medium`, and the publisher patch
  notes admitted as `KSP-016` describe a mode this packet excludes. `CON-062`
  keeps its definition, lifecycle and nineteen other carriers, and its Ukrainian
  record loses only the Kerbal Space Program clause; `GAME-0265` is unaffected. The six genes this record introduced
  — `ACT-444`, `SYS-811`, `SYS-812`, `CON-610`, `INF-324` and `OBJ-161` — are
  downgraded from `Corroborated`/`High` to `Limited`/`Medium`, because their
  support is the one wiki family this environment cannot fetch. Boundaries,
  lifecycles, this signature and `COMB-0265` are unchanged.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_032`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_032.md)
  removed the `CON-062` reuse from this signature. No split, merge, deprecation
  or lifecycle change followed, and no other record's signature moved. The
  `A-02` and `A-08` corrections remain evidence, confidence and wording changes
  with no lifecycle effect.
- Candidate terms: recorded in `CANDIDATE_TERMS.md`; all product, part, body,
  mode, app, package and build names remain parameters.

## Negative results

- No video or audio evidence was used; only official product data, the
  publisher's own announcements, product wiki material and one retrieved player
  discussion thread support this packet.
- The product wiki host refuses direct retrieval from this environment behind a
  challenge page. Its content was therefore reached through search indexing and
  is cited with that limitation stated, rather than presented as a page this
  unit fetched. `BATCH_015_GENE_AUDIT_001` finding `A-08` required either
  fetchable replacement evidence or an honest downgrade; the replacement attempt
  failed, so the downgrade is applied and recorded in the source list above.
  The wiki is also relabelled from `official wiki` to `product wiki`, because
  this unit found no statement of publisher ownership for it, and its five cited
  pages count as one corroborating family rather than five sources.
- **No placement-legality Constraint is claimed for this packet, and the
  previous claim was withdrawn.** `CON-062` requires a refusal on footprint
  overlap with an incompatible placed component and a refusal on an unavailable
  or incompatible anchor or port. Three attempts failed to evidence that for the
  declared stock assembly building: a player discussion thread (`S7`) is not
  documentation; the wiki tutorial (`S8`) that the follow-up run described as
  the product's own manual is a user-editable community article marked
  `Outdated`, which review finding `R-08` established; and the publisher's own
  patch notes (`P5`) speak to EVA construction mode, which this packet excludes.
  No publisher-hosted PC manual or KSPedia export exists to retrieve, and the
  in-game KSPedia would require direct play, which this packet did not conduct.
  Silent direct visual verification was not available in this environment. The
  mechanic very probably exists in the product; this record simply may not
  assert it, so the gene was removed rather than retained on evidence of that
  grade. Obtaining it remains an open research task.
- The in-assembly derived performance readout is excluded as a bounded evidence
  gap: only community prose attests it, which the batch's evidence rules treat
  as limited, so the packet does not admit an information gene for it. This is a
  recorded uncertainty, not a claim that the readout does not exist.
- Unlike `GAME-0265` and `GAME-0266`, this product's named version and public
  branch date agree exactly, and the one later announcement is documented as a
  launcher-only change. The version is therefore asserted rather than left as a
  discrepancy, which shows the earlier two records were reporting a real
  difference and not a methodological artefact.
- Manoeuvre-node planning, docking, rendezvous, time warp, revert and recovery
  are excluded because the declared route does not require them.
- A suborbital trajectory whose high point clears the boundary is not the
  terminal.

## Delta summary

## New facts

- [Observation | Corroborated | High] `KSP-001`–`KSP-013`: one bounded Sandbox
  task makes the craft's flight behaviour a direct consequence of how the
  player connected and ordered it, and settles against a published altitude the
  interface already projects.

## New genes

- [Observation | Corroborated | High] `ACT-444`, `SYS-811`, `SYS-812`,
  `CON-610`, `INF-324`, `OBJ-161` — the ordered activation list authored at
  rest and consumed under pressure, propellant drawn through the player's own
  connectivity with continuous mass loss, the projected conic resolution, the
  atmospheric boundary that decides closure, the projected extremes disclosure
  and the trajectory-property objective.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0265` — a player-assembled craft
  whose connectivity and ordered activation decide a trajectory judged against
  a published altitude.

## Taxonomy changes

- [Observation | Direct/Corroborated | High] `ACT-392` receives a
  boundary-preserving portable label and wording generalisation; no prior
  signature or lifecycle changes. `TAXONOMY_CHANGE_032` later removed the
  `CON-062` reuse from this signature, which falls from twelve genes to eleven,
  leaving that gene's definition, lifecycle and nineteen other carriers unchanged.

## New questions

- Does a second constructed-vehicle packet reuse `SYS-811` and `ACT-444`, or is
  connectivity-determined propellant flow specific to this product's part
  model?
- What source class can establish this product's assembly-building placement
  rules at all, given that the publisher hosts no PC manual, the in-game
  KSPedia requires direct play and the community wiki is not documentation?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0268` — Undertale.
- Optimisation criterion: leave the constructed-vehicle corridor entirely and
  test whether a turn-based selection phase and a real-time projectile-dodging
  defence can share one packet.
- Expected information gain: the first corpus packet whose defence phase is
  real-time inside an otherwise turn-based encounter.
- Backlog impact: advances the recorded 261-to-270 horizon by one unit.

## Why this game

- [Hypothesis | Limited | High] The selection asked whether continuous
  orbital-physics resolution requires genes beyond assembly, staging and vehicle
  control. The completed scan answers yes: assembly, placement legality, physics
  and flight control were all reused or generalised, while propellant
  connectivity, the projected conic and its boundary test required new
  boundaries no existing gene covered.
