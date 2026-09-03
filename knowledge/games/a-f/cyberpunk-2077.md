---
game_id: GAME-0146
slug: cyberpunk-2077
game_title: Cyberpunk 2077
analysis_status: reviewed
reviewed: 2026-08-22
combination_ids:
  - COMB-0144
gene_ids:
  action:
    - ACT-008
    - ACT-107
    - ACT-140
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-191
    - ACT-199
    - ACT-202
    - ACT-231
    - ACT-232
    - ACT-233
    - ACT-234
    - ACT-235
    - ACT-236
  system:
    - SYS-208
    - SYS-215
    - SYS-292
    - SYS-299
    - SYS-342
    - SYS-369
    - SYS-372
    - SYS-373
    - SYS-374
    - SYS-375
    - SYS-376
    - SYS-378
    - SYS-379
  constraint:
    - CON-136
    - CON-188
    - CON-269
    - CON-270
    - CON-282
    - CON-284
    - CON-285
    - CON-332
    - CON-333
    - CON-334
    - CON-335
    - CON-336
    - CON-337
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-147
    - INF-148
    - INF-149
  objective:
    - OBJ-077
  time:
    - TIM-003
    - TIM-007
---

# Game: Cyberpunk 2077

## Analysis scope

- Version / ruleset: base game on PC at public Patch `2.31`, reviewed
  2026-08-22; one fresh single-player save on `Normal`, from a selected Nomad
  lifepath and initial attribute allocation through the first completion of
  `Where Is My Mind?` via the always-available Arasaka route.
- Primary decision loop: prepare and express one persistent V build through
  critical-path traversal, stealth or combat encounters and retained quest
  choices until the first Arasaka ending.
- Entry condition: commit the Nomad lifepath and legal initial attribute budget
  on a fresh `Normal` save.
- Exit condition: complete `Where Is My Mind?` for the first time after choosing
  Hanako's offer at `Nocturne OP55N1`.
- Included: direct first-person traversal and stance; firearm, melee, grenade,
  stealth, grapple and takedown play; scanning, quickhacks, RAM, upload queue and
  hostile tracing; loot and inventory; character XP, levels, attributes, perks
  and activity skills; cyberware slots, capacity, armour and attunement;
  authored main jobs, lifepath/contextual dialogue and retained choices;
  checkpoints, manual/autosave restoration and the first Devil ending.
- Reproducible checkpoint: create a Nomad V, record the starting attribute
  budget and one lifepath-marked response, then advance the critical path. In a
  repeatable hostile area scan one target, upload a legal quickhack, observe RAM
  and any trace, break sight, crouch behind cover and neutralise an unaware
  reachable target. Fire and reload one weapon, spend and observe a health-item
  or grenade charge, install capacity-legal cyberware at a ripperdoc, allocate a
  legal perk, pick up and equip compatible loot, and restore a save or
  checkpoint.
  Continue the required jobs, choose Hanako's offer at `Nocturne OP55N1`, finish
  `Last Caress`, `Totalimmortal` and `Where Is My Mind?`, and record the first
  completed ending response.
- Excluded: hand-crafting and ordinary vendor-shopping loops; direct vehicle,
  personal-waypoint and traffic simulation; deliberate NCPD Heat play; Street
  Cred offer progression; Phantom Liberty, Dogtown, the Relic tree and Tower
  ending; optional side jobs, gigs and ending-unlock questlines; alternate
  endings as the first terminal branch; post-credits `One More Gig`, New Game
  Plus, mods, cheats, achievements, cosmetics, romance, collectibles and
  exhaustive weapons, vehicles, cyberware, dialogue or open-world activities.
- Potential scoped modules: crafting/vendor economy, vehicle/navigation,
  open-world law pressure and Street Cred offer progression remain established
  product systems but require separate bounded packets before re-admission.
- Direct-play status: no complete fresh paid-account campaign was conducted.
  Official current patch, 2.0 system notes, product material and build planner
  establish the maintained mechanical baseline; official and maintained route
  references corroborate the bounded critical path. Exact balance values and
  incidental mission-script outcomes remain parameters.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CP-001` | Patch 2.31 is the current reviewed public base-game PC baseline | Confirmed | Direct | High | P1 |
| `CP-002` | Lifepath and initial attributes configure the prologue and later contextual response availability | Confirmed | Corroborated | High | P2, P3 |
| `CP-003` | Direct combat couples weapons, armour, stamina, grenades and rechargeable health-item charges in real time | Confirmed | Direct | High | P2, P4 |
| `CP-004` | Scanning reveals targets and quickhacks; legal uploads consume RAM, may queue and may trigger hostile tracing | Confirmed | Direct | High | P2, P5 |
| `CP-005` | Suspicion escalates through detection into combat, while crouch, cover, grapple and takedown permit stealth resolution | Observation | Corroborated | High | P2, P4, S1 |
| `CP-006` | Installed cyberware is bounded by slots and capacity and supplies armour, abilities and attribute attunement | Confirmed | Direct | High | P2, P5 |
| `CP-007` | XP, levels, attributes, perks and activity skills form persistent progression channels inside the selected route | Confirmed | Direct | High | P2, P4 |
| `CP-008` | Character level scales enemies and loot encountered along the selected route | Confirmed | Direct | High | P2 |
| `CP-009` | Main jobs advance through authored prerequisites and retained responses; failure can restore bounded checkpoint state | Observation | Corroborated | High | P4, S1, S2 |
| `CP-010` | The Arasaka choice at Nocturne OP55N1 leads through Last Caress and Totalimmortal to Where Is My Mind? without optional ending unlocks | Confirmed | Corroborated | High | S2, S3, S4 |
| `CP-011` | Crafting/vendor, vehicle/navigation, NCPD Heat and Street Cred offer progression are separately described product systems and are not required transitions of the selected Arasaka route | Confirmed | Corroborated | High | P2, P4, S2 |

## Basic data

- Release / origin: CD PROJEKT RED; original release 2020, Update 2.0 in 2023
  and reviewed at Patch 2.31 on 2026-08-22.
- Platform or physical form: authored single-player first-person open-world
  action RPG; current PC base game is scoped.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  knowledge and evidence progression; inventory and fixture dependencies;
  ordered dependency sequencing.
- Primary sources:
  - **[P1]** [official Patch 2.31 notes](https://www.cyberpunk.net/en/news/51794/patch-2-31),
    for the current reviewed version boundary.
  - **[P2]** [official Update 2.0 notes](https://www.cyberpunk.net/en/news/49060/update-2-0),
    for police Heat, combat, quickhacks, rechargeable items, perks, skills,
    cyberware capacity, item tiers, scaling, map and HUD changes.
  - **[P3]** [official Ultimate Edition booklet](https://cdn-s-cyberpunk.cdprojektred.com/CP2077-UE-booklet-EN.pdf),
    for lifepaths, Night City, dialogue context and campaign framing.
  - **[P4]** [official Cyberpunk 2077 page](https://www.cyberpunk.net/cd/en/cyberpunk-2077),
    for authored choices, open-world missions, skills, weapons, hacking,
    implants, combat and stealth.
  - **[P5]** [official cyberware feature](https://www.cyberpunk.net/en/news/49129/whats-coming-in-2-0-cyberware),
    for capacity, armour, attunement and implant-driven abilities.
  - **[P6]** [official build planner](https://www.cyberpunk.net/en/news/48958/build-planner-craft-your-cyberpunk-2077-and-phantom-liberty-builds),
    for bounded attribute and perk planning.
- Secondary sources:
  - **[S1]** [Cyberpunk Wiki main jobs](https://cyberpunk.fandom.com/wiki/Cyberpunk_2077_Main_Jobs),
    for the ordered base-game job graph and critical-path naming.
  - **[S2]** [Push Square endings guide](https://www.pushsquare.com/guides/cyberpunk-2077-all-endings-and-how-to-unlock-them),
    for the always-available Hanako route and exact final job sequence.
  - **[S3]** [Cyberpunk Wiki endings](https://cyberpunk.fandom.com/wiki/Cyberpunk_2077_Endings),
    for base-game terminal routes and the Devil outcome boundary.
  - **[S4]** [PowerPyx endings guide](https://www.powerpyx.com/cyberpunk-2077-endings-guide-all-endings/),
    for independent route corroboration.
- Claim IDs: `CP-001`–`CP-011`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, direct traversal; `ACT-107`, acquire an
  operational fact in dialogue; `ACT-140`, commit the terminal route and final
  response; `ACT-161`, aim and strike; `ACT-164`, select an active weapon;
  `ACT-183`, reload; `ACT-191`, spend an attribute or perk point; `ACT-199`,
  transfer and equip loot; `ACT-202`, change stance.
- New genes: `ACT-231`, commit lifepath and initial attributes; `ACT-232`,
  commit an authored dialogue or quest response; `ACT-233`, scan and upload a
  quickhack; `ACT-234`, configure installed cyberware; `ACT-235`, grapple and
  neutralise an unaware target; `ACT-236`, activate a rechargeable combat item.
- Claim IDs: `CP-002`–`CP-011`.

### System Behaviour Genes

- Existing genes: `SYS-208`, resolve ranged attacks through cover and body;
  `SYS-215`, resolve live combat; `SYS-292`, resolve grenade flight and effect;
  `SYS-299`, convert XP into levels and build points; `SYS-342`, accumulate
  activity skill progress; `SYS-369`, restore an authored mission checkpoint.
- New genes: `SYS-372`, apply lifepath to contextual content; `SYS-373`,
  escalate suspicion into detection and combat; `SYS-374`, resolve quickhack
  upload, queue and trace; `SYS-375`, derive protection and abilities from
  cyberware; `SYS-376`, recharge spent combat-item charges; `SYS-378`, scale
  enemies and loot to character level; `SYS-379`, advance authored quest state
  from retained choices.
- Resolution order: retained build and quest state gate the current interface;
  scanning and perception expose legal targets; stealth, hacking or weapon
  input resolves in live time; resources and detection update; rewards update
  level and skills; jobs retain choices and unlock their successors; failure
  can restore a prior bounded state.
- Claim IDs: `CP-002`–`CP-011`.

### Constraint Genes

- Existing genes: `CON-136`, persistent prerequisites gate later mechanisms;
  `CON-188`, terminal offer permits one persistent choice; `CON-269`, active
  abilities require target, resource and readiness; `CON-270`, build choices
  obey level and branch gates; `CON-282`, main jobs require authored order;
  `CON-284`, carry weight and slots bound loot; `CON-285`, weapon operation
  requires compatible live state.
- New genes: `CON-332`, initial build obeys lifepath and attribute budget;
  `CON-333`, cyberware obeys slot and capacity limits; `CON-334`, quickhack
  requires access, target, RAM and readiness; `CON-335`, stealth neutralisation
  requires an unaware reachable target; `CON-336`, retained quest state gates
  later branches; `CON-337`, contextual interaction requires its attribute
  threshold.
- Scarce strategic resources: health, stamina, ammunition, RAM, item charges,
  cyberware capacity, carry weight, attribute and perk points, stealth time
  before detection and retained branch availability.
- Claim IDs: `CP-002`–`CP-011`.

### Information Genes

- Existing genes: `INF-073`, weapon and ammunition state; `INF-115`, partial
  hostile perception; `INF-119`, health, RAM, level and build state; `INF-125`,
  map and job gates; `INF-128`, loot and inventory compatibility.
- New genes: `INF-147`, scanner target state and available quickhacks;
  `INF-148`, contextual response gates in dialogue; `INF-149`, cyberware
  capacity and implant effects.
- Claim IDs: `CP-002`–`CP-011`.

### Objective Genes

- Existing gene: `OBJ-077`, complete the required main-story graph through one
  committed terminal branch and first ending; this scope uses the Arasaka route
  and first completion of `Where Is My Mind?`.
- Claim IDs: `CP-009`, `CP-010`.

### Time Genes

- Existing genes: `TIM-003`, movement, detection, combat and hacking advance in
  real time; `TIM-007`, manual saves, autosaves and mission
  checkpoints can restore prior state and permit a different continuation.
- Claim IDs: `CP-003`–`CP-011`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| New-game setup exposes lifepath and a fixed attribute budget | Choose Nomad and allocate every available point | The opening changes and the legal initial build persists | Origin and build are rule-bearing initial state | `CP-002` |
| Reachable device or hostile is visible to the scanner | Scan and upload one legal quickhack | RAM is spent, upload/queue resolves and hostile trace may begin | Hacking is target- and resource-bounded action | `CP-004` |
| Hostile has not detected V and is reachable from behind | Crouch, approach, grapple and choose a neutralisation | Target is restrained and resolved without ordinary open fire | Stealth depends on perception and geometry | `CP-005` |
| Ripperdoc interface exposes a legal implant and enough capacity | Install or replace the implant | Capacity, armour, attunement and granted abilities update together | Cyberware is a configured build system | `CP-006` |
| XP crosses a level and one perk is currently legal | Spend the resulting point | The selected bounded build node changes future actions or modifiers | Progression becomes committed capability | `CP-007` |
| A manual save predates a dialogue or combat choice | Restore it and choose differently | Earlier retained state returns and subsequent state diverges | Campaign history is player-branchable | `CP-009` |
| Nocturne OP55N1 exposes Hanako's offer | Accept it and complete the resulting three jobs | The Arasaka route reaches Where Is My Mind? and records the first ending | Optional ending unlocks are not required | `CP-010` |

## Strategic and experiential structure

- Local decision: interpret scanner, sight and sound; choose stealth, quickhack,
  firearm, melee, grenade or retreat; decide whether to spend RAM, ammunition,
  charge readiness or expose V to trace and detection.
- Medium-term planning: specialise attributes and perks, fit cyberware within
  slots and capacity, preserve compatible equipment, improve relevant skills
  and sequence main jobs while retaining useful responses.
- Long-term structure: the fixed authored world and job graph convert early
  origin/build choices, acquired equipment and retained quest state into
  available approaches and a final terminal branch.
- Common heuristics: scan before entering; isolate unaware enemies; use cover
  while RAM or charges recover; keep one reliable weapon supplied; install
  cyberware that supports the chosen attribute path; save before irreversible
  dialogue; track the critical job rather than optional map noise.
- Failure attribution: HUD resources, scanner gates, detection indicators,
  cyberware capacity, journal prerequisites and checkpoint restore explain most
  immediate failure, while enemy movement and authored consequences preserve
  bounded uncertainty.
- Claim IDs: `CP-002`–`CP-011`.

## Replay and variation

- What changes between sessions: lifepath, initial and later build, dialogue,
  stealth/combat route, quickhack deck, cyberware, equipment and final
  branch; this scope records only one first ending.
- Randomness or procedural generation: Night City and the required job graph
  are authored; loot details, enemy activity and combat execution vary without
  regenerating the campaign world.
- Multiple viable strategies: stealth takedown, netrunning, direct firearms or
  melee; specialised or hybrid build; different looted equipment.
- Typical replay motive: compare lifepaths, builds, quest responses and excluded
  terminal routes without treating every variant as part of one genome.

## Adjacent systems and history

- Grand Theft Auto V remains a structural near neighbour through direct
  traversal, combat, authored mission gates, checkpoints and a terminal choice.
  The separately excluded vehicle, wanted-state and economy loops explain the
  reduced overlap. Cyberpunk replaces the
  concurrent trio and crew-planned heists with one configurable protagonist,
  cyberware, quickhacks, stealth perception and retained dialogue state.
- Fallout 4 should be compared later for authored open-world RPG quests,
  character build, loot and dialogue, but Cyberpunk's scanner, RAM and
  capacity-bound implants form a distinct live tactical layer.
- Counter-Strike 2 shares aimed firearm resolution and partial hostile
  information but lacks persistent character, authored quest and world state.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-107`, `ACT-140`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-191`, `ACT-199`, `ACT-202`, `ACT-231`–`ACT-236` | content identities, controls and balance are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-292`, `SYS-299`, `SYS-342`, `SYS-369`, `SYS-372`–`SYS-376`, `SYS-378`, `SYS-379` | exact damage, progression and timing are parameters |
| Constraint | `CON-136`, `CON-188`, `CON-269`, `CON-270`, `CON-282`, `CON-284`, `CON-285`, `CON-332`–`CON-337` | numeric caps and thresholds are parameters |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-147`–`INF-149` | HUD styling is presentation |
| Objective | `OBJ-077` | selected first ending is the scoped parameter |
| Time | `TIM-003`, `TIM-007` | save availability and live timing are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `145` (`GAME-0001`–`GAME-0145`).
- Exact genome matches: none.
- Tied near matches: `GAME-0145` — Grand Theft Auto V (`21 / 79 = 0.265823`).
- Supported combination subsets: `COMB-0144`.
- Scan date: 2026-08-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0145` — Grand Theft Auto V | `ACT-008`, `ACT-140`, `ACT-161`, `ACT-164`, `ACT-183`, `SYS-208`, `SYS-215`, `SYS-292`, `SYS-342`, `SYS-369`, `CON-136`, `CON-188`, `CON-269`, `CON-282`, `CON-285`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `OBJ-077`, `TIM-003` | Both packets retain direct traversal, real-time combat, authored mission gates, checkpoint restoration and a terminal choice. The bounded Cyberpunk packet excludes the vehicle, wanted-state and ordinary economy loops that remain central to GTA V, and instead centres one persistent cyberware/quickhack character build with retained dialogue state. | Near, `0.265823` |

## Taxonomy impact

- Registry changes: the reviewed scope migration removes 12 genes from this
  carrier. Eleven keep their active lifecycle and other carriers; orphaned
  `SYS-377` becomes `Deprecated` under `TAXONOMY_CHANGE_016` without a boundary
  rewrite. `COMB-0144` contracts from 49 to 47 genes.
- New family: none; existing `FAM-009`, `FAM-010`, `FAM-012`, `FAM-013` and
  `FAM-017` remain justified by the retained tactical, real-time, progression,
  inventory and ordered-dependency mechanics.
- Taxonomy-change records: `GAME_SIGNATURE_MIGRATION_001` and
  `TAXONOMY_CHANGE_016`.

## Negative results

- Phantom Liberty and every optional ending-unlock path were tested as scope
  candidates and excluded because they are not required for the reproducible
  first Arasaka ending.
- Crafting/vendor, vehicle/navigation, NCPD Heat and Street Cred offer loops
  were re-audited against the selected Arasaka route. They remain valid product
  systems but do not change a required or recurrent transition inside this
  bounded packet.
