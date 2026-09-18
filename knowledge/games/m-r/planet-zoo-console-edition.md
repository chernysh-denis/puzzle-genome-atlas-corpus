---
game_id: GAME-0298
slug: planet-zoo-console-edition
game_title: 'Planet Zoo: Console Edition'
analysis_status: reviewed
reviewed: 2026-09-18
combination_ids: []
gene_ids:
  action:
    - ACT-006
    - ACT-130
    - ACT-455
    - ACT-456
    - ACT-457
    - ACT-458
  system:
    - SYS-736
    - SYS-866
    - SYS-867
  constraint:
    - CON-635
  information:
    - INF-341
  objective:
    - OBJ-175
  time:
    - TIM-003
---

# Game: Planet Zoo: Console Edition

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: the unmodified English Xbox Series X|S base product
  `9NZ038KZ68B7`, released 2024-03-26. The latest official console note located
  at review is `1.9.2`, dated 2025-08-27; the Xbox storefront does not expose
  an installed executable build number, so `1.9.2` is a documented public
  rules reference, **not** a claim that a local Xbox was patched or played.
  The exact Goodwin House Bronze objective list is reconstructed from two
  written secondary pages derived from the original scenario; console-specific
  objective parity remains unverified by direct play.
- Product boundary: the base Console Edition on Xbox Series X|S. Deluxe and
  Ultimate upgrades, Season Pass, animal packs, their additional career
  scenarios, cloud-streamed play and the Windows edition are excluded.
- Platform, mode and entry: one new offline, single-player Career scenario at
  Goodwin House, from the first playable tutorial instruction. Retain the
  scenario's supplied buildings, staff, animals, funds and default difficulty;
  do not substitute Sandbox or Franchise settings. Note the initial state and
  the console-visible task text before acting in any future direct test.
- Primary decision loop: read the currently taught task and animal requirements,
  inspect the relevant habitat, adopt the requested animals, complete the
  barrier/gate/path connection, place feeding, water and enrichment facilities
  plus the viewing-side donation box, and let eligible staff move assigned
  animals into their valid habitat. Live care and welfare update while the
  simulation runs. The next taught predicate appears only when the current
  one has been satisfied; repeat until the Bronze award is registered.
- Reproducible route: inspect the Grizzly Bear habitat and animal camera, West
  African Lion habitat and empty habitat; adopt two Common Warthogs and equip
  their existing habitat with feeding, water and toy enrichment; then complete
  the highlighted Common Ostrich habitat with a closed barrier, exactly one
  gate connected to a path, a glass viewing section and nearby donation box.
  Adopt four Common Ostriches and equip that habitat with feeding, water and
  food enrichment. Where a task merely locates an object, camera inspection is
  navigation and information access, not a new physical-state gene. The named
  counts and sequence are **secondary-source route parameters awaiting Xbox
  verification**, not an invented direct observation.
- Positive terminal: the Goodwin House Bronze scenario award becomes visible
  after all currently listed Bronze predicates settle. Stop before building the
  Silver-stage Keeper Hut. The award is a finite authored terminal under
  ADR-007; saving, exiting and reloading are not claimed as performed.
- Failure and asymmetry: this Career packet is not a timed scenario. An invalid
  enclosure or disconnected gate blocks animal assignment; absent care can
  degrade welfare while time advances. No authored loss screen for this opening
  was established, so indefinite non-progress or animal-care deterioration is
  a negative boundary, not a claimed formal defeat state.
- Included: Goodwin House opening tutorial, the two requested base species,
  habitat barriers and gate, one required path connection, animal adoption and
  delivery, feed/water/enrichment facilities, glass viewing section, donation
  box placement, animal-welfare feedback, task progression and Bronze award.
- Excluded: Silver/Gold objectives, new tiger habitat, later Career scenarios,
  breeding, genetics, research, conservation-credit optimisation, keeper
  work zones, loans, ticket policy, guest-economy optimisation, zoo complexity
  saturation, online Franchise, Challenge, Sandbox, Workshop, downloadable
  species, user-made blueprints, platform achievements and audiovisual content.
- Direct-play status: not conducted. No Xbox Series X|S console, entitlement,
  installation, save or captured task list was available in this workspace.
  Microsoft and Frontier establish the product, console controls, habitat,
  adoption, delivery, welfare and medal rules. Two written secondary lists
  agree on the Bronze steps, but may share a source; they do **not** establish
  exact current Xbox task parity. This is a bounded evidence reconstruction,
  not a claimed playthrough or earned medal. No video or audio was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PZ-001` | Xbox base Console Edition targets Series X and Series S, released 2024-03-26, with Career single-player support and separately sold upgrades | Confirmed | Direct | High | P1 |
| `PZ-002` | Frontier's last located official console update is `1.9.2` on 2025-08-27; no local Xbox build was inspected | Observation | Direct | Medium | P2 |
| `PZ-003` | Career scenarios award Bronze, Silver and Gold; Goodwin House is the console-aware beginner tutorial | Confirmed | Direct | High | P3 |
| `PZ-004` | The reconstructed Bronze tasks request two Warthogs, four Ostriches, care fixtures, a closed gated and path-connected Ostrich enclosure, glass and a donation box | Observation | Limited | Medium | S1, S2, S3 |
| `PZ-005` | A valid habitat has a continuous barrier loop, exactly one keeper gate and outward path connection; wrong enclosure topology blocks placement | Confirmed | Direct | High | P4 |
| `PZ-006` | Adopted animals enter Trade Centre storage; a caretaker or vet moves an assigned animal to a destination habitat | Confirmed | Direct | High | P4, P5 |
| `PZ-007` | Nutrition, social, habitat and enrichment factors update animal welfare; species requirements and current welfare are inspectable | Confirmed | Direct | High | P6 |
| `PZ-008` | Keepers autonomously clean, feed and water habitats, subject to reachable facilities | Confirmed | Direct | High | P5 |
| `PZ-009` | A console complexity meter can eventually prohibit new elements, but this opening packet does not require reaching that cap | Confirmed | Direct | High | P4 |
| `PZ-010` | No local Xbox play, medal settlement or save/reload was performed | Confirmed | Direct | High | R1 |

## Basic data

- Origin: Frontier Developments developed and published the console product;
  Xbox Series X|S release 2024-03-26.
- Physical or platform form: Xbox digital base Console Edition, Career Goodwin
  House opening through Bronze, not a general claim about every release.
- Mechanical families: connected route construction, live system pressure,
  autonomous-agent coordination and ordered dependency sequencing.
- Primary official sources, checked 2026-09-18:
  - **[P1]** [Microsoft Xbox base-product listing](https://www.xbox.com/en-US/games/store/planet-zoo-console-edition/9NZ038KZ68B7),
    for SKU, platform, release, base/upgrade distinction and Career mode.
  - **[P2]** [Frontier console `1.9.2` notes](https://www.planetzoogame.com/update-notes/console/1-9-2),
    for the last located dated official console update.
  - **[P3]** [Frontier beginner basics](https://www.planetzoogame.com/help-centre/player-guides/the-basics),
    for console-aware Career, Goodwin House, three awards, difficulty and controls.
  - **[P4]** [Frontier building guide](https://www.planetzoogame.com/help-centre/player-guides/building-your-zoo),
    for habitat topology, paths, Trade Centre, barriers, facilities and the
    console complexity meter.
  - **[P5]** [Frontier staff and guests guide](https://www.planetzoogame.com/help-centre/player-guides/staff-and-guests),
    for keepers, caretakers, vets and guest-facing operation.
  - **[P6]** [Frontier animal guide](https://www.planetzoogame.com/help-centre/player-guides/the-animals),
    for adoption, habitat assignment, welfare factors and Zoopedia feedback.
- Corroborating written sources, checked 2026-09-18:
  - **[S1]** [Neoseeker Goodwin House guide](https://www.neoseeker.com/planet-zoo/walkthrough/Goodwin_House),
    for the detailed Bronze checklist; its original-PC context is explicit.
  - **[S2]** [Planet Zoo Wiki scenario checklist](https://planetzoo.fandom.com/wiki/Stately_Home_Schooling),
    for the same checklist; independence from S1 is not established.
  - **[S3]** [SuperSoluce Career overview](https://www.supersoluce.com/soluce/planet-zoo/le-mode-carriere),
    for Goodwin House as first tutorial and the Bronze-to-next-scenario gate.
- **[R1]** Workspace access audit: no Xbox hardware, playable installation or
  save was available. No audiovisual material was opened or analysed.

## Mechanical decomposition

### Actions

- Reused `ACT-006` owns optional simulation acceleration; `ACT-130` owns each
  currently offered animal adoption paid from the scenario's permitted funds.
- New `ACT-455` owns editing the persistent branching guest/staff path graph;
  `ACT-456` owns authoring the animal barrier loop and its one keeper gate.
- New `ACT-457` owns discrete feeding, water, enrichment and donation-fixture
  placement; `ACT-458` owns assigning a stored animal to a chosen habitat.
  Merely moving the camera to a tutorial highlight changes no zoo state.

### Systems, constraint, information, objective and time

- Reused `SYS-736` owns staged tutorial predicate advancement. New `SYS-866`
  owns autonomous staff transport from Trade Centre to an assigned legal
  habitat; `SYS-867` owns ongoing animal welfare as care and habitat factors
  change. `CON-635` rejects an enclosure without a continuous barrier, exactly
  one gate and connected access. `INF-341` exposes welfare, species needs and
  the current task. `OBJ-175` names the finite Goodwin House Bronze award.
  `TIM-003` owns the live simulation while the player makes decisions.

## Reproducible transitions

| Before | Player action | Bounded resolution | Claim |
|---|---|---|---|
| Fresh Goodwin House tutorial opens | Inspect marked Grizzly Bear, Lion and empty habitat | The location/camera predicates advance without a zoo-state action gene | `PZ-003`, `PZ-004` |
| Two Warthog offers are legal | Adopt two Common Warthogs | Purchases place two animals in Trade Centre storage | `PZ-004`, `PZ-006` |
| Existing Warthog habitat lacks required fixtures | Place feeding, water and toy enrichment | Current taught predicates clear and nutrition/enrichment conditions can improve | `PZ-004`, `PZ-007` |
| Highlighted Ostrich area is incomplete | Close barrier, add its single gate, connect a path and make a glass viewing section | The habitat becomes topologically eligible for animal placement | `PZ-004`, `PZ-005` |
| Viewing path exists | Place the donation box by the Ostrich view | The authored placement predicate clears; actual guest donations are outside this packet | `PZ-004` |
| Four offered Ostriches can be adopted | Purchase and assign four to the eligible habitat | Trade Centre stores them, then staff transport them when the simulation runs | `PZ-004`, `PZ-006` |
| Ostrich habitat lacks care fixtures | Place feeding, water and food enrichment; allow eligible delivery and task settlement | Bronze predicates finish and the scenario award becomes visible | `PZ-003`, `PZ-004`, `PZ-007` |
| Habitat loop is open or has no connected keeper gate | Attempt destination assignment | Placement is rejected or delivery cannot complete; Bronze remains unearned | `PZ-005`, `PZ-006` |

## Strategic and experiential structure

- The player edits containment and reachability first, then converts Trade
  Centre stock into housed animals; buying an animal is not the same transition
  as delivering it. Fixture placement improves needs but does not bypass an
  invalid enclosure. Tutorial stages expose the next required predicate, so
  the early planning horizon is narrower than a free-form zoo.
- The simulation can continue while the player inspects menus or edits a
  habitat, allowing animals and staff to change state between commitments.
  Pausing or accelerating modifies that cadence, not objective legality.
- A glass barrier and donation box form the guest-facing side of a valid
  habitat, but guest revenue is not a required terminal measure for Bronze.

## Replay and variation

- Animal offers, individual traits, finances, exact path geometry, staff
  arrival timing and welfare values can differ without changing the named
  objective classes. The scenario's prebuilt habitat and supplied staff are
  fixed as the reproducible starting context, not newly authored actions.
- Console objective wording and exact task sequence must be recorded during
  future direct reproduction. A mismatch with the older written checklists
  requires a scoped correction before treating those counts as observed.

## Adjacent systems and history

- Cities: Skylines II also constructs a path-like network under live
  simulation, but its `ACT-068` is explicitly a vehicle road graph used by
  traffic. Planet Zoo's guest/staff paths, animal barrier topology and Trade
  Centre deliveries are different causal owners, not a relabelled city road.
- The Sims 4 models individual and household needs, but does not have this
  tutorial's keeper-gated habitat, staff delivery or species-specific
  enrichment requirements. No earlier welfare gene was broadened on title
  similarity alone.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-130`, `ACT-455`, `ACT-456`, `ACT-457`, `ACT-458` | speed, offers, paths, enclosure, fixtures, destination |
| System Behaviour | `SYS-736`, `SYS-866`, `SYS-867` | tutorial stages, delivery and welfare |
| Constraint | `CON-635` | closed loop, one gate and connected access |
| Information | `INF-341` | task, species requirements and welfare |
| Objective | `OBJ-175` | Goodwin House Bronze award |
| Time | `TIM-003` | live zoo simulation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `297` (`GAME-0001`–`GAME-0297`).
- Exact genome matches: none.
- Tied near matches: `GAME-0092` — Echochrome (`2 / 21 = 0.095238`).
- Supported combination subsets: none.
- Scan date: 2026-09-18.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0092` — Echochrome | `ACT-006`, `TIM-003` | Both permit input while an autonomous clock continues and let the player accelerate that clock. Echochrome manipulates a projection-governed Walker to a spatial exit; Planet Zoo edits persistent habitats and paths, purchases and transfers animals, then satisfies species-care tutorial predicates. | Near, `0.095238` |

## Taxonomy impact

- New genes: `ACT-455`–`ACT-458`, `SYS-866`–`SYS-867`, `CON-635`,
  `INF-341` and `OBJ-175`.
- Existing definitions and signatures: unchanged. No taxonomy-change record.
- No new combination is proposed without a verified recurring strict-subset
  interaction; deterministic subset validation found no supported combination.

## Negative results

- `ACT-068` is vehicle-road editing, not guest/staff footpath construction.
  `ACT-139` is an ordinary owned building, not feeding, water, enrichment or
  donation-fixture placement. Both boundaries are retained.
- Guest donation flow, breeding, genetics, researched enrichment, staff work
  zones and the console complexity cap exist in the broader product but are
  not required before the selected Bronze terminal.

## Delta summary

## New facts

- [Observation | Limited | Medium] `PZ-001`–`PZ-010` bound the console product,
  Goodwin House Bronze reconstruction and the habitat-to-delivery dependency.

## New genes

- [Observation | Direct | High] Nine new portable owners separate zoo paths,
  barriers, fixtures, animal placement, staff delivery, welfare, habitat
  validity, requirements and the finite Bronze objective.

## New combinations

- [Observation | Limited | Medium] None proposed; subset validation decides
  whether an existing verified combination is supported.

## Taxonomy changes

- None; the vehicle-road and ordinary-building boundaries remain unchanged.

## Inferences

- [Strong Pattern | Corroborated | Medium] The opening puzzle is not just
  choosing animals: a purchased animal must pass a spatial legality check and
  a staff-delivery delay before it can satisfy a staged objective.

## Open questions

- The precise current Xbox task wording, any post-`1.9.2` local build, exact
  offered animal traits and direct Bronze settlement await a lawful console
  run. The two detailed written lists may not be independent.

## Contradictions

- None within the reconstructed base-game boundary; console-specific
  checklist parity remains an explicit uncertainty rather than a contradiction.

## New questions

- Does a later Challenge or Franchise packet require a distinct typed economy
  for breeding, research and conservation, beyond this tutorial's care loop?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0299` Nioh 2 on PS4, the next selected
  platform target, only after this complete unit passes every gate.
- Optimisation criterion: contrast welfare-driven spatial management with
  stance, Ki and recovery commitments in a bounded action packet.
- Expected information gain: test whether the existing close-combat owners
  transfer without flattening Nioh 2's distinct resource and death systems.

## Why this game

- [Hypothesis | Limited | Medium] It adds a console-first management boundary
  with enclosure topology, animal delivery and species care after the prior
  hunt-heavy horizon, while exercising the exact-platform discipline.

## Confidence and unresolved questions

- High for Microsoft product identity and Frontier's general console-aware
  habitat, staff, welfare and Career rules; Medium for the older Goodwin House
  Bronze checklist; Low for any claim of current local Xbox execution, which
  is therefore not made.
- Resolution path: use the base Xbox product on a fresh Career profile, record
  displayed build and task text, trace each objective through Bronze, then
  compare the actual console predicates with this secondary reconstruction.
