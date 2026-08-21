---
game_id: GAME-0146
slug: cyberpunk-2077
game_title: Cyberpunk 2077
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0144
gene_ids:
  action:
    - ACT-008
    - ACT-107
    - ACT-123
    - ACT-130
    - ACT-140
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-191
    - ACT-199
    - ACT-201
    - ACT-202
    - ACT-227
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
    - SYS-320
    - SYS-342
    - SYS-365
    - SYS-366
    - SYS-369
    - SYS-372
    - SYS-373
    - SYS-374
    - SYS-375
    - SYS-376
    - SYS-377
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
    - CON-288
    - CON-332
    - CON-333
    - CON-334
    - CON-335
    - CON-336
    - CON-337
  information:
    - INF-073
    - INF-115
    - INF-117
    - INF-119
    - INF-125
    - INF-128
    - INF-132
    - INF-144
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
  2026-08-21; one fresh single-player save on `Normal`, from a selected Nomad
  lifepath and initial attribute allocation through the first completion of
  `Where Is My Mind?` via the always-available Arasaka route.
- Included: direct first-person movement, stance, combat and vehicles; firearm,
  melee, grenade, stealth, grapple and takedown play; scanning, quickhacks, RAM,
  upload queue and hostile tracing; loot, inventory, vendors and crafting;
  character XP, levels, attributes, perks, activity skills and Street Cred;
  cyberware slots, capacity, armour and attunement; authored main jobs,
  lifepath/contextual dialogue and retained choices; NCPD Heat, checkpoints,
  manual/autosave restoration and the first Devil ending.
- Reproducible checkpoint: create a Nomad V, record the starting attribute
  budget and one lifepath-marked response, then advance the critical path. In a
  repeatable hostile area scan one target, upload a legal quickhack, observe RAM
  and any trace, break sight, crouch behind cover and neutralise an unaware
  reachable target. Fire and reload one weapon, spend and observe a health-item
  or grenade charge, install capacity-legal cyberware at a ripperdoc, allocate a
  legal perk, craft one known item, purchase one offer, drive to a personal
  waypoint, trigger and clear low NCPD Heat, and restore a save or checkpoint.
  Continue the required jobs, choose Hanako's offer at `Nocturne OP55N1`, finish
  `Last Caress`, `Totalimmortal` and `Where Is My Mind?`, and record the first
  completed ending response.
- Excluded: Phantom Liberty, Dogtown, the Relic tree and Tower ending; optional
  side jobs, gigs and ending-unlock questlines; alternate endings as the first
  terminal branch; post-credits `One More Gig`, New Game Plus, mods, cheats,
  achievements, cosmetics, romance, collectibles and exhaustive weapons,
  vehicles, cyberware, dialogue or open-world activities.
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
| `CP-007` | XP, levels, attributes, perks, skills and Street Cred form distinct persistent progression channels | Confirmed | Direct | High | P2, P4 |
| `CP-008` | Character level scales enemies, loot and vendor tiers while Street Cred unlocks additional offered-world content | Confirmed | Direct | High | P2 |
| `CP-009` | Main jobs advance through authored prerequisites and retained responses; failure can restore bounded checkpoint state | Observation | Corroborated | High | P4, S1, S2 |
| `CP-010` | The Arasaka choice at Nocturne OP55N1 leads through Last Caress and Totalimmortal to Where Is My Mind? without optional ending unlocks | Confirmed | Corroborated | High | S2, S3, S4 |

## Basic data

- Release / origin: CD PROJEKT RED; original release 2020, Update 2.0 in 2023
  and reviewed at Patch 2.31 on 2026-08-21.
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
- Claim IDs: `CP-001`–`CP-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, direct navigation; `ACT-107`, acquire an
  operational fact in dialogue; `ACT-123`, hand-craft a known item; `ACT-130`,
  buy a vendor offer; `ACT-140`, commit the terminal route and final response;
  `ACT-161`, aim and strike; `ACT-164`, select an active weapon; `ACT-183`,
  reload; `ACT-191`, spend an attribute or perk point; `ACT-199`, transfer and
  equip loot; `ACT-201`, enter and operate a vehicle; `ACT-202`, change stance;
  `ACT-227`, set a personal waypoint.
- New genes: `ACT-231`, commit lifepath and initial attributes; `ACT-232`,
  commit an authored dialogue or quest response; `ACT-233`, scan and upload a
  quickhack; `ACT-234`, configure installed cyberware; `ACT-235`, grapple and
  neutralise an unaware target; `ACT-236`, activate a rechargeable combat item.
- Claim IDs: `CP-002`–`CP-010`.

### System Behaviour Genes

- Existing genes: `SYS-208`, resolve ranged attacks through cover and body;
  `SYS-215`, resolve live combat; `SYS-292`, resolve grenade flight and effect;
  `SYS-299`, convert XP into levels and build points; `SYS-320`, simulate
  vehicle motion and damage; `SYS-342`, accumulate activity skill progress;
  `SYS-365`, simulate traffic and civilians; `SYS-366`, escalate and clear
  wanted pursuit; `SYS-369`, restore an authored mission checkpoint.
- New genes: `SYS-372`, apply lifepath to contextual content; `SYS-373`,
  escalate suspicion into detection and combat; `SYS-374`, resolve quickhack
  upload, queue and trace; `SYS-375`, derive protection and abilities from
  cyberware; `SYS-376`, recharge spent combat-item charges; `SYS-377`, convert
  Street Cred into offered-world unlocks; `SYS-378`, scale enemies, loot and
  vendor tiers to character level; `SYS-379`, advance authored quest state from
  retained choices.
- Resolution order: retained build and quest state gate the current interface;
  scanning and perception expose legal targets; stealth, hacking or weapon
  input resolves in live time; resources, detection and Heat update; rewards
  update level, skills and Street Cred; jobs retain choices and unlock their
  successors; failure can restore a prior bounded state.
- Claim IDs: `CP-002`–`CP-010`.

### Constraint Genes

- Existing genes: `CON-136`, persistent prerequisites gate later mechanisms;
  `CON-188`, terminal offer permits one persistent choice; `CON-269`, active
  abilities require target, resource and readiness; `CON-270`, build choices
  obey level and branch gates; `CON-282`, main jobs require authored order;
  `CON-284`, carry weight and slots bound loot; `CON-285`, weapon operation
  requires compatible live state; `CON-288`, vehicle operation requires a
  viable seat, operating state and geometry.
- New genes: `CON-332`, initial build obeys lifepath and attribute budget;
  `CON-333`, cyberware obeys slot and capacity limits; `CON-334`, quickhack
  requires access, target, RAM and readiness; `CON-335`, stealth neutralisation
  requires an unaware reachable target; `CON-336`, retained quest state gates
  later branches; `CON-337`, contextual interaction requires its attribute
  threshold.
- Scarce strategic resources: health, stamina, ammunition, RAM, item charges,
  cyberware capacity, carry weight, money, attribute and perk points, stealth
  time before detection, Street Cred and retained branch availability.
- Claim IDs: `CP-002`–`CP-010`.

### Information Genes

- Existing genes: `INF-073`, weapon and ammunition state; `INF-115`, partial
  hostile perception; `INF-117`, money, price and purchase state; `INF-119`,
  health, RAM, level and build state; `INF-125`, map and job gates; `INF-128`,
  loot and inventory compatibility; `INF-132`, crafting dependencies;
  `INF-144`, GPS and wanted-search state.
- New genes: `INF-147`, scanner target state and available quickhacks;
  `INF-148`, contextual response gates in dialogue; `INF-149`, cyberware
  capacity and implant effects.
- Claim IDs: `CP-002`–`CP-010`.

### Objective Genes

- Existing gene: `OBJ-077`, complete the required main-story graph through one
  committed terminal branch and first ending; this scope uses the Arasaka route
  and first completion of `Where Is My Mind?`.
- Claim IDs: `CP-009`, `CP-010`.

### Time Genes

- Existing genes: `TIM-003`, movement, detection, combat, hacking, traffic and
  pursuit advance in real time; `TIM-007`, manual saves, autosaves and mission
  checkpoints can restore prior state and permit a different continuation.
- Claim IDs: `CP-003`–`CP-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| New-game setup exposes lifepath and a fixed attribute budget | Choose Nomad and allocate every available point | The opening changes and the legal initial build persists | Origin and build are rule-bearing initial state | `CP-002` |
| Reachable device or hostile is visible to the scanner | Scan and upload one legal quickhack | RAM is spent, upload/queue resolves and hostile trace may begin | Hacking is target- and resource-bounded action | `CP-004` |
| Hostile has not detected V and is reachable from behind | Crouch, approach, grapple and choose a neutralisation | Target is restrained and resolved without ordinary open fire | Stealth depends on perception and geometry | `CP-005` |
| Ripperdoc interface exposes a legal implant and enough capacity | Install or replace the implant | Capacity, armour, attunement and granted abilities update together | Cyberware is a configured build system | `CP-006` |
| XP crosses a level and one perk is currently legal | Spend the resulting point | The selected bounded build node changes future actions or modifiers | Progression becomes committed capability | `CP-007` |
| V commits an observed crime without current Heat | Evade responding NCPD and remain unseen | Pressure escalates, changes to search and clears after evasion | Law pressure is perception- and time-dependent | `CP-003`, `CP-008` |
| A manual save predates a dialogue or combat choice | Restore it and choose differently | Earlier retained state returns and subsequent state diverges | Campaign history is player-branchable | `CP-009` |
| Nocturne OP55N1 exposes Hanako's offer | Accept it and complete the resulting three jobs | The Arasaka route reaches Where Is My Mind? and records the first ending | Optional ending unlocks are not required | `CP-010` |

## Strategic and experiential structure

- Local decision: interpret scanner, sight and sound; choose stealth, quickhack,
  firearm, melee, grenade or retreat; decide whether to spend RAM, ammunition,
  charge readiness or expose V to trace and detection.
- Medium-term planning: specialise attributes and perks, fit cyberware within
  slots and capacity, preserve money and components, improve relevant skills
  and Street Cred, and sequence main jobs while retaining useful responses.
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
- Claim IDs: `CP-002`–`CP-010`.

## Replay and variation

- What changes between sessions: lifepath, initial and later build, dialogue,
  stealth/combat route, quickhack deck, cyberware, equipment, vehicle and final
  branch; this scope records only one first ending.
- Randomness or procedural generation: Night City and the required job graph
  are authored; traffic, civilians, loot details, enemy activity and combat
  execution vary without regenerating the campaign world.
- Multiple viable strategies: stealth takedown, netrunning, direct firearms or
  melee; specialised or hybrid build; bought, looted or crafted equipment.
- Typical replay motive: compare lifepaths, builds, quest responses and excluded
  terminal routes without treating every variant as part of one genome.

## Adjacent systems and history

- Grand Theft Auto V is the structural near neighbour through direct urban
  traversal, combat, vehicles, traffic, wanted pursuit, authored mission gates,
  checkpoints, vendors, GPS and a terminal choice. Cyberpunk replaces the
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
| Action | `ACT-008`, `ACT-107`, `ACT-123`, `ACT-130`, `ACT-140`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-191`, `ACT-199`, `ACT-201`, `ACT-202`, `ACT-227`, `ACT-231`–`ACT-236` | content identities, controls and balance are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-292`, `SYS-299`, `SYS-320`, `SYS-342`, `SYS-365`, `SYS-366`, `SYS-369`, `SYS-372`–`SYS-379` | exact damage, progression and timing are parameters |
| Constraint | `CON-136`, `CON-188`, `CON-269`, `CON-270`, `CON-282`, `CON-284`, `CON-285`, `CON-288`, `CON-332`–`CON-337` | numeric caps and thresholds are parameters |
| Information | `INF-073`, `INF-115`, `INF-117`, `INF-119`, `INF-125`, `INF-128`, `INF-132`, `INF-144`, `INF-147`–`INF-149` | HUD styling is presentation |
| Objective | `OBJ-077` | selected first ending is the scoped parameter |
| Time | `TIM-003`, `TIM-007` | save availability and live timing are parameters |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-008,ACT-107,ACT-123,ACT-130,ACT-140,ACT-161,ACT-164,ACT-183,ACT-191,ACT-199,ACT-201,ACT-202,ACT-227,ACT-231,ACT-232,ACT-233,ACT-234,ACT-235,ACT-236; SYS-208,SYS-215,SYS-292,SYS-299,SYS-320,SYS-342,SYS-365,SYS-366,SYS-369,SYS-372,SYS-373,SYS-374,SYS-375,SYS-376,SYS-377,SYS-378,SYS-379; CON-136,CON-188,CON-269,CON-270,CON-282,CON-284,CON-285,CON-288,CON-332,CON-333,CON-334,CON-335,CON-336,CON-337; INF-073,INF-115,INF-117,INF-119,INF-125,INF-128,INF-132,INF-144,INF-147,INF-148,INF-149; OBJ-077; TIM-003,TIM-007`.
- Indexed games scanned: all 145 earlier canonical games.
- Indexed combinations scanned: all 143 earlier verified combinations.
- Exact genome matches: none.
- Mathematical near match: Grand Theft Auto V (`GAME-0145`),
  `30 / 82 = 0.365854`.
- Comparison context: PUBG: BATTLEGROUNDS (`GAME-0140`),
  `18 / 89 = 0.202247`; Counter-Strike 2 (`GAME-0137`),
  `11 / 83 = 0.132530`.
- Supported earlier combination subsets: none; new
  `COMB-0144` is a strict subset of this 64-gene genome.
- Scan date: 2026-08-21.

Exhaustive prior-game ledger:

<!-- EXHAUSTIVE_LEDGER -->

- GAME-0001: 0 / 78 = 0.000000; GAME-0002: 0 / 71 = 0.000000; GAME-0003: 0 / 73 = 0.000000; GAME-0004: 1 / 78 = 0.012821.
- GAME-0005: 0 / 71 = 0.000000; GAME-0006: 1 / 72 = 0.013889; GAME-0007: 0 / 72 = 0.000000; GAME-0008: 0 / 71 = 0.000000.
- GAME-0009: 0 / 80 = 0.000000; GAME-0010: 0 / 73 = 0.000000; GAME-0011: 0 / 77 = 0.000000; GAME-0012: 0 / 73 = 0.000000.
- GAME-0013: 0 / 77 = 0.000000; GAME-0014: 0 / 79 = 0.000000; GAME-0015: 0 / 78 = 0.000000; GAME-0016: 1 / 78 = 0.012821.
- GAME-0017: 0 / 77 = 0.000000; GAME-0018: 1 / 82 = 0.012195; GAME-0019: 0 / 74 = 0.000000; GAME-0020: 0 / 78 = 0.000000.
- GAME-0021: 1 / 72 = 0.013889; GAME-0022: 0 / 76 = 0.000000; GAME-0023: 0 / 74 = 0.000000; GAME-0024: 1 / 75 = 0.013333.
- GAME-0025: 1 / 74 = 0.013514; GAME-0026: 1 / 75 = 0.013333; GAME-0027: 1 / 75 = 0.013333; GAME-0028: 1 / 80 = 0.012500.
- GAME-0029: 2 / 74 = 0.027027; GAME-0030: 2 / 76 = 0.026316; GAME-0031: 1 / 74 = 0.013514; GAME-0032: 0 / 75 = 0.000000.
- GAME-0033: 2 / 75 = 0.026667; GAME-0034: 3 / 75 = 0.040000; GAME-0035: 3 / 79 = 0.037975; GAME-0036: 1 / 75 = 0.013333.
- GAME-0037: 0 / 73 = 0.000000; GAME-0038: 2 / 78 = 0.025641; GAME-0039: 0 / 73 = 0.000000; GAME-0040: 1 / 71 = 0.014085.
- GAME-0041: 3 / 72 = 0.041667; GAME-0042: 0 / 73 = 0.000000; GAME-0043: 1 / 77 = 0.012987; GAME-0044: 1 / 73 = 0.013699.
- GAME-0045: 1 / 77 = 0.012987; GAME-0046: 0 / 74 = 0.000000; GAME-0047: 0 / 78 = 0.000000; GAME-0048: 0 / 78 = 0.000000.
- GAME-0049: 0 / 73 = 0.000000; GAME-0050: 1 / 78 = 0.012821; GAME-0051: 1 / 79 = 0.012658; GAME-0052: 0 / 74 = 0.000000.
- GAME-0053: 1 / 72 = 0.013889; GAME-0054: 1 / 74 = 0.013514; GAME-0055: 1 / 73 = 0.013699; GAME-0056: 0 / 72 = 0.000000.
- GAME-0057: 0 / 72 = 0.000000; GAME-0058: 0 / 73 = 0.000000; GAME-0059: 0 / 71 = 0.000000; GAME-0060: 0 / 71 = 0.000000.
- GAME-0061: 0 / 74 = 0.000000; GAME-0062: 0 / 72 = 0.000000; GAME-0063: 0 / 71 = 0.000000; GAME-0064: 0 / 69 = 0.000000.
- GAME-0065: 0 / 71 = 0.000000; GAME-0066: 0 / 74 = 0.000000; GAME-0067: 0 / 72 = 0.000000; GAME-0068: 0 / 72 = 0.000000.
- GAME-0069: 0 / 72 = 0.000000; GAME-0070: 0 / 72 = 0.000000; GAME-0071: 0 / 71 = 0.000000; GAME-0072: 0 / 72 = 0.000000.
- GAME-0073: 0 / 71 = 0.000000; GAME-0074: 0 / 73 = 0.000000; GAME-0075: 0 / 73 = 0.000000; GAME-0076: 0 / 71 = 0.000000.
- GAME-0077: 0 / 71 = 0.000000; GAME-0078: 0 / 71 = 0.000000; GAME-0079: 0 / 71 = 0.000000; GAME-0080: 0 / 71 = 0.000000.
- GAME-0081: 0 / 72 = 0.000000; GAME-0082: 0 / 72 = 0.000000; GAME-0083: 0 / 72 = 0.000000; GAME-0084: 0 / 74 = 0.000000.
- GAME-0085: 1 / 74 = 0.013514; GAME-0086: 1 / 76 = 0.013158; GAME-0087: 2 / 72 = 0.027778; GAME-0088: 1 / 72 = 0.013889.
- GAME-0089: 1 / 72 = 0.013889; GAME-0090: 2 / 77 = 0.025974; GAME-0091: 2 / 71 = 0.028169; GAME-0092: 1 / 73 = 0.013699.
- GAME-0093: 0 / 73 = 0.000000; GAME-0094: 2 / 72 = 0.027778; GAME-0095: 2 / 74 = 0.027027; GAME-0096: 2 / 72 = 0.027778.
- GAME-0097: 2 / 70 = 0.028571; GAME-0098: 2 / 69 = 0.028986; GAME-0099: 1 / 71 = 0.014085; GAME-0100: 1 / 74 = 0.013514.
- GAME-0101: 0 / 74 = 0.000000; GAME-0102: 0 / 71 = 0.000000; GAME-0103: 0 / 73 = 0.000000; GAME-0104: 1 / 72 = 0.013889.
- GAME-0105: 3 / 71 = 0.042254; GAME-0106: 0 / 71 = 0.000000; GAME-0107: 1 / 71 = 0.014085; GAME-0108: 1 / 73 = 0.013699.
- GAME-0109: 0 / 80 = 0.000000; GAME-0110: 1 / 71 = 0.014085; GAME-0111: 2 / 69 = 0.028986; GAME-0112: 2 / 70 = 0.028571.
- GAME-0113: 2 / 76 = 0.026316; GAME-0114: 1 / 70 = 0.014286; GAME-0115: 0 / 70 = 0.000000; GAME-0116: 2 / 68 = 0.029412.
- GAME-0117: 1 / 71 = 0.014085; GAME-0118: 1 / 79 = 0.012658; GAME-0119: 2 / 85 = 0.023529; GAME-0120: 1 / 92 = 0.010870.
- GAME-0121: 1 / 86 = 0.011628; GAME-0122: 1 / 78 = 0.012821; GAME-0123: 2 / 100 = 0.020000; GAME-0124: 4 / 107 = 0.037383.
- GAME-0125: 2 / 104 = 0.019231; GAME-0126: 1 / 106 = 0.009434; GAME-0127: 2 / 110 = 0.018182; GAME-0128: 2 / 78 = 0.025641.
- GAME-0129: 7 / 92 = 0.076087; GAME-0130: 3 / 114 = 0.026316; GAME-0131: 6 / 104 = 0.057692; GAME-0132: 1 / 114 = 0.008772.
- GAME-0133: 1 / 108 = 0.009259; GAME-0134: 1 / 114 = 0.008772; GAME-0135: 1 / 111 = 0.009009; GAME-0136: 3 / 121 = 0.024793.
- GAME-0137: 11 / 83 = 0.132530; GAME-0138: 8 / 91 = 0.087912; GAME-0139: 9 / 109 = 0.082569; GAME-0140: 18 / 89 = 0.202247.
- GAME-0141: 12 / 103 = 0.116505; GAME-0142: 12 / 103 = 0.116505; GAME-0143: 12 / 101 = 0.118812; GAME-0144: 10 / 89 = 0.112360.
- GAME-0145: 30 / 82 = 0.365854.

## Taxonomy impact

- Registry changes: 23 new bounded genes and `COMB-0144`; 41 existing genes
  gain an independently sourced open-world action-RPG example without changing
  their lifecycle or causal boundary.
- New family: none; existing `FAM-009`, `FAM-010`, `FAM-012`, `FAM-013` and
  `FAM-017` fit.
- Taxonomy-change record: none.

## Negative results

- Phantom Liberty and every optional ending-unlock path were tested as scope
  candidates and excluded because they are not required for the reproducible
  first Arasaka ending.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Scanner access, RAM, upload queue and hostile
  trace form one coupled offensive-information system (`CP-004`).
- [Confirmed | Direct | High] Cyberware slots and capacity jointly bound armour,
  active abilities and attribute attunement (`CP-006`).

## Нові гени

- [Observation | Corroborated | High] 23 bounded genes cover initial origin,
  authored responses, scanning/quickhacks, cyberware, stealth neutralisation,
  rechargeable combat items, detection, Street Cred, level scaling and quest
  retention.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0144` — capacity-bound cybernetic
  build and hacking into retained quest branches.

## Зміни таксономії

- [Observation | Corroborated | High] Five existing families absorb the game;
  no new family or lifecycle change is needed.

## Нові питання

- Should a later expansion distinguish enemy-network trace propagation from a
  generic hostile trace when another netrunning game supplies a second example?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0147` — Marvel Rivals.
- Optimisation criterion: continue the recorded demand-led tranche in order.
- Expected information gain: hero swapping, destructible team arenas, role
  synergies and round/objective structure against the current combat corpus.
- Backlog impact: advances the 17-game Goal without skipping.

## Чому саме вона

- [Hypothesis | Limited | High] It preserves live hero combat for comparison
  while replacing persistent open-world build and quests with team composition,
  objective rounds and environment destruction.
