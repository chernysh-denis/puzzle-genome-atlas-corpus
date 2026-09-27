---
game_id: GAME-0418
slug: ftl-faster-than-light
game_title: 'FTL: Faster Than Light'
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-393
    - ACT-482
    - ACT-555
    - ACT-556
  system:
    - SYS-724
    - SYS-1107
    - SYS-1108
    - SYS-1109
    - SYS-1110
  constraint:
    - CON-578
    - CON-703
    - CON-704
  information:
    - INF-411
  objective:
    - OBJ-243
  time:
    - TIM-003
    - TIM-030
---

# Game: FTL: Faster Than Light — one Kestrel hostile beacon

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Kestrel, the Artemis launcher, Burst Laser II, named rooms and first-sector layout are carriers or parameters, not gene names.

## Analysis scope

- Version / ruleset: original English Windows PC *FTL: Faster Than Light* released by Subset Games on 14 September 2012, before the 2014 *Advanced Edition* additions. A precise executable checksum or patch revision was not obtained. The packet conditionally follows the starting Kestrel Type A from selecting one connected first-sector beacon until an ordinary hostile-ship encounter there is resolved; the selected beacon is not claimed to be a fixed scripted fight.
- Structured analysis target: `PLAT-WINDOWS-PC` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: select a reachable beacon and spend fuel to jump; when its event yields a hostile ship, read both vessels' visible state, pause to reassign crew, allocate finite reactor power and target the enemy's functional rooms, then resume so weapons, shields, damage, repairs and FTL charge advance. Decide whether to defeat the hostile or jump away once the drive is ready and a legal destination remains.
- Entry and exit: begin on the Kestrel's first-sector starmap with a legal connected destination and fuel, before committing the chosen jump. This conditional packet continues only if arrival yields an ordinary hostile vessel. It ends when that vessel is destroyed and the encounter closes, or when the still-living Kestrel performs a legal escape jump. Loss of the player's ship or crew before either is failure. An empty, merchant or text-only beacon falls outside the condition rather than being reclassified as this fight.
- Included: connected-beacon navigation and fuel cost, variable arrival event, Kestrel's initial laser and finite-missile choices, reactor allocation to weapons, shields, engines, oxygen or medical support, room-directed crew staffing or repair, charged room-targeted fire, weapon-specific shield interaction, room/system and hull damage, oxygen or fire exposure when present, live FTL readiness and optional escape, and reversible tactical pause.
- Excluded: the eight-sector campaign, Rebel Flagship, purchases or upgrades, unlocking ships, boarding, drones, cloaking, special environmental beacons, crew hiring, specific enemy class or fixed reward, surrender text as a required outcome, Advanced Edition hacking, mind control, clone bay or Lanius, exact random weights, hidden hit chances, room-damage formula, frame-level timing and UI hotkeys introduced by later patches.
- Potential scoped modules: a named branching text event, the advancing Rebel fleet across multiple jumps, boarding and oxygen-venting tactics, a complete run to the Flagship, or a separately pinned Advanced Edition encounter.
- Direct-play status: no executable, Steam installation, input trace, screenshot, gameplay video or audio was inspected. Subset Games' own product description establishes the command and pause loop; firsthand launch-era reports on its forum bound the Kestrel loadout, fuel, ship repair, shields and jump escape. Exact revision, enemy roll and quantitative combat timings remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FTL1-001` | The original Windows release dates to September 2012; current storefront copy explicitly separates the later free Advanced Edition. | Confirmed | Direct | High | P1; P2 |
| `FTL1-002` | Ship power, crew orders, weapon targets, mid-combat pause and varied encounters are core developer-described rules. | Confirmed | Direct | High | P1 |
| `FTL1-003` | Kestrel A has Burst Laser II and Artemis at the start of the original game; their availability and ammunition shape distinct attack choices. | Confirmed | Corroborated | High | R1; R2 |
| `FTL1-004` | A connected beacon jump spends fuel, while a running encounter may be abandoned once a viable FTL drive charges. | Confirmed | Corroborated | High | R3; R4; P1 |
| `FTL1-005` | Laser fire interacts with shields, whereas missiles can bypass them; targeted room hits can disable systems, but evasion and damage outcomes are not guaranteed. | Confirmed | Corroborated | High | R4; R5 |
| `FTL1-006` | Crew can be sent into damaged rooms to repair system function; this does not directly restore outer hull, and oxygen/fire hazards can endanger a repairer. | Confirmed | Corroborated | High | R6; R7; R8 |
| `FTL1-007` | The sector's event and enemy vary between runs; no inspected source guarantees a hostile ship at a specified first jump. | Observation | Direct | High | P1 |
| `FTL1-008` | The exact 2012 binary revision, probabilities, initial encounter identity, quantitative charge and repair ticks were not measured. | Observation | Limited | High | P1; R3–R8 |

## Basic data

- Release / origin: Subset Games, Windows PC original release of 14 September 2012. The current product page also offers *Advanced Edition*, which is excluded rather than projected into 2012.
- Platform or physical form: original English PC keyboard/mouse ship-command game. The structured target specifies Windows; later ports and other original PC operating systems are not inferred to be mechanically identical by this packet.
- Mechanical families: real-time system pressure (`FAM-010`) and ordered dependency sequencing (`FAM-017`). Simultaneous ship systems change under time pressure; a fuel-paid beacon choice leads into an encounter where shields, weapons, room repairs and escape readiness constrain one another.
- Sources accessed 2026-09-27:
  - **P1** — [Subset Games' official Steam product page](https://store.steampowered.com/app/212680/FTL_Faster_Than_Light/), original date, crew orders, power routing, targeting, pause, randomized events, permadeath, explicit Advanced Edition separation and a legal product destination. Storefront text has evolved, so it does not pin a 2012 executable.
  - **P2** — [Subset Games' press sheet](https://subsetgames.com/presskit/sheet.php?p=fTL), release identity and date.
  - **R1** — [2012 Kestrel A completion account](https://subsetgames.com/forum/viewtopic.php?t=2332), firsthand original-game discussion of initial Artemis and Burst Laser II.
  - **R2** — [2012 Kestrel system recreation discussion](https://subsetgames.com/forum/viewtopic.php?t=9821), independent launch-year description of the same two starting weapons; not a substitute for game data.
  - **R3** — [2012 beacon-jump fuel discussion](https://www.subsetgames.com/forum/viewtopic.php?t=2269), direct player account that an A-to-B jump spends one fuel.
  - **R4** — [2012 core tactics guide on the developer forum](https://www.subsetgames.com/forum/viewtopic.php?t=1887), firsthand tactics for engine/helm-dependent charged escape, system targeting and power switching.
  - **R5** — [2012 shield and missile discussion](https://subsetgames.com/forum/viewtopic.php?p=7048), firsthand claim that missiles pass shields. No hidden accuracy formula is taken from it.
  - **R6** — [2012 damaged-room and oxygen account](https://subsetgames.com/forum/viewtopic.php?t=2197), firsthand sequence of sending crew to repair a failed oxygen room under exposure.
  - **R7** — [2012 hull-repair clarification](https://subsetgames.com/forum/viewtopic.php?t=1923), firsthand developer-forum distinction between crew system repair and shop/event hull repair.
  - **R8** — [2012 repair-versus-hazard tactics](https://subsetgames.com/forum/viewtopic.php?t=1889), player discussion of fire, oxygen and withdrawing crew from stations to repair.
- Claim IDs: `FTL1-001`–`FTL1-008`.

## Mechanical decomposition

### Action Genes

- `ACT-482`: select one linked first-sector beacon on the sector map and commit travel; selection is not manual piloting through space.
- `ACT-393`: redistribute available live power among engines, shields and weapons, with oxygen or medbay power as other Kestrel system choices. No permanent upgrade is bought in this packet.
- `ACT-555`: send one crewmember from a station to a reachable damaged room or back; this changes personnel placement, not ship direction.
- `ACT-556`: select a charged, powered laser or missile and designate an enemy room, for example weapons or shields. Selection does not guarantee a hit.
- Claim IDs: `FTL1-002`–`FTL1-006`.

### System Behaviour Genes

- `SYS-1110`: the committed beacon resolves into its variable event; this packet follows the branch that produces an ordinary hostile vessel.
- `SYS-724`: current live power permits or limits shield, engine and weapon performance, including weapon readiness.
- `SYS-1107`: each attack resolves evasion, laser/shield or missile-bypass interaction, then any eligible room, system, crew and hull damage.
- `SYS-1108`: a crew member in a damaged room repairs its system over live time while oxygen depletion or fire can threaten the same room.
- `SYS-1109`: a viable powered drive builds FTL escape readiness during combat; a ready drive permits retreat if the jump gate also holds.
- Resolution order: commit beacon → reveal event → if hostile, assign power and orders (possibly under pause) → resume fire, damage, crew work and FTL charging → destroy enemy, jump out or lose the ship. Different projectile and repair events interleave while live; no fixed turn order is claimed.
- Claim IDs: `FTL1-002`–`FTL1-008`.

### Constraint Genes

- `CON-703`: live systems share finite reactor bars and cannot be powered above their own surviving capacity.
- `CON-578`: Artemis fire requires a remaining compatible missile; the laser does not pay that missile cost.
- `CON-704`: beacon travel requires a linked destination and fuel; escape additionally requires a ready viable drive.
- Scarce resources: fuel governs route and retreat, missiles price shield-bypassing offence, and reactor bars force simultaneous function trade-offs. Exact starting counts and event rewards are not part of a new gene.
- Claim IDs: `FTL1-003`–`FTL1-005`.

### Information Genes

- `INF-411`: read the room/system view, crew, hull, shields, charged weapons, missile stock, enemy-visible systems, FTL readiness and reachable sector graph. Future beacon rolls and hidden hit probabilities are not previewed.
- Claim IDs: `FTL1-002`, `FTL1-007`, `FTL1-008`.

### Objective and Time Genes

- `OBJ-243`: leave this one hostile encounter with a living ship by enemy destruction or legal charged jump; no whole-campaign win is implied.
- `TIM-003`: combat shots, crew movement, hazards, repair and FTL charge advance while the simulation runs.
- `TIM-030`: pause that live clock to inspect state and issue tactical orders, then resume their resolution.
- Claim IDs: `FTL1-002`, `FTL1-004`, `FTL1-006`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A connected beacon and fuel are available | Select and jump to that beacon | Fuel decreases and the destination's event is revealed; only a hostile result enters this packet | map choice does not predetermine the enemy | `FTL1-004`, `FTL1-007` |
| A hostile ship is active and the Kestrel is intact | Pause and divert one reactor bar toward an eligible system | The selected allocation changes without weapon or crew movement advancing until resume | finite power plus reversible tactical pause | `FTL1-002` |
| A laser and Artemis are both ready | Target an enemy system with either weapon | A fired laser must overcome applicable shielding; Artemis pays one missile and can bypass shields, but either can miss | weapon-specific attack paths and finite ammo | `FTL1-003`, `FTL1-005` |
| A Kestrel system room is damaged | Send a crew member from a staffed station to repair it | The room regains function only after the crew member reaches it and repair progresses; the vacated station may lose its benefit | time-exposed crew allocation | `FTL1-006` |
| An oxygen room is damaged or on fire | Assign repair and supply power while crew remain exposed | Room function can return, but the hazard can still injure crew before that resolution | repair is not instant or hazard-free | `FTL1-006` |
| An enemy persists and the Kestrel's helm/engines work | Let the FTL drive charge, then choose a legal destination | The player leaves without defeating the hostile; no enemy-kill reward is assumed | charged retreat is a distinct terminal branch | `FTL1-004` |
| The hostile hull reaches destruction before retreat | Continue the encounter closeout | The hostile ship is defeated and this packet succeeds if the Kestrel survives | combat victory is the other terminal branch | `FTL1-005` |
| The Kestrel loses all viable hull or crew before victory or escape | Continue live resolution | The run fails; a later free retry is not part of the original permadeath rules | bounded failure | `FTL1-002` |

## Strategic and experiential structure

- Local decision: direct limited shots toward a dangerous enemy room or protect the Kestrel long enough to bring its own systems online.
- Medium-term planning: preserve missiles and fuel while balancing shields, engines, weapons and life support; pulling a crew member from a station to repair a room has an opportunity cost.
- Long-term structure: one route choice can yield a different event on another run, while hull damage and spent supplies persist beyond this isolated encounter in the full campaign.
- Failure attribution: visible system bars, room state and FTL readiness identify many immediate causes. The inspected material does not establish exact random-hit odds for any selected enemy.
- Player-trust factors: pause gives unlimited deliberation before resuming the live battle; the selected beacon does not promise its future event.
- Claim IDs: `FTL1-002`–`FTL1-008`.

## Replay and variation

- The starting Kestrel Type A and its two initial weapon types stay fixed for this packet; the chosen connected route, resulting ordinary opponent, its equipment, event and damage sequence need not.
- Destroying the hostile and fleeing after FTL charge are distinct supported endings, not guaranteed equal rewards.
- No deterministic first-beacon enemy, scrap result, hit chance or precise repair timing is invented from the source-bounded reconstruction.

## Adjacent systems and history

- *STAR WARS: Squadrons* and *Starfield* also redistribute live craft power, but their direct piloting and respective fighter/Frontier travel rules do not represent FTL's room-directed crew labour and beacon event.
- *Slay the Spire* can finish a finite encounter by defeating all hostiles; this packet also permits powered travel away before the enemy is defeated.
- *Mass Effect 2* pauses a held radial command wheel; FTL freezes a ship-command overview accepting power, crew and target orders. The distinction is time-interface causality, not a new turn system.
- Advanced Edition adds later rules and equipment and is not treated as the original 2012 version.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-393`, `ACT-482`, `ACT-555`, `ACT-556` | reactor bars, reachable beacon, assigned room, chosen target |
| System Behaviour | `SYS-724`, `SYS-1107`, `SYS-1108`, `SYS-1109`, `SYS-1110` | power effect, shield bypass, room repair, FTL charge, sampled event |
| Constraint | `CON-578`, `CON-703`, `CON-704` | missile stock, reactor output, fuel and drive gate |
| Information | `INF-411` | current systems and map, not future roll |
| Objective | `OBJ-243` | survive by victory or charged retreat |
| Time | `TIM-003`, `TIM-030` | live clock and tactical pause |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `417` (`GAME-0001`–`GAME-0417`).
- Exact genome matches: none.
- Tied near matches: `GAME-0331` — Starfield (`4 / 46 = 0.086957`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Starfield (`GAME-0331`) | starmap destination command, live craft-power allocation and its subsystem response, continuous time | FTL selects a connected fuel-paid beacon that reveals an uncertain encounter, then commands crew between damageable ship rooms, aims charged weapons at enemy systems and can escape after FTL charge; Starfield directly pilots the Frontier and traverses a broader fixed opening route with grav-drive and planetary landing gates, without FTL's room-repair combat or general tactical pause | Near, `0.086957` |

## Taxonomy impact

- [`TAXONOMY_CHANGE_156`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_156.md) admits eleven typed boundaries. Five genes are reused; no earlier signature or verified combination is changed.

## Negative results

- `CON-565` rejected: its fixed starfighter engine/laser/shield emphasis is not the Kestrel's individually powered room system budget.
- `SYS-940` rejected: its unconditional shield-before-hull description would misstate shield-bypassing missiles and room damage.
- `INF-277` rejected: FTL supplies a shipwide command view, not a directly piloted cockpit instrument cluster.
- `TIM-027` rejected: FTL's general pause does not require holding Mass Effect's radial squad power wheel.
- A fixed first-beacon opponent, guaranteed post-fight reward, precise hit roll and Advanced Edition-specific equipment are unverified or outside scope.

## Delta summary

One variable first-sector beacon becomes a live ship fight in which finite reactor power and ammunition compete, crew physically move to repair damaged rooms, charged weapons address enemy systems, and FTL readiness permits survival without enemy defeat. The route and broad power-allocation actions transfer; room-level orders, shield-specific damage, repair, escape, event reveal, shipwide information and tactical pause are newly typed.

## New facts

- [Confirmed | Direct | High] Subset Games explicitly describes crew orders, ship power, target selection and combat pause in the original product's core rules (`FTL1-002`).
- [Confirmed | Corroborated | High] A fuel-paid route and charged escape are distinct from destroying the hostile ship (`FTL1-004`).

## New genes

- [Observation | Corroborated | High] `ACT-555`, `ACT-556`, `SYS-1107`–`SYS-1110`, `CON-703`, `CON-704`, `INF-411`, `OBJ-243` and `TIM-030` isolate the ship-command, damage, repair, event and retreat boundaries.

## New combinations

- [Observation | Limited | High] No verified combination is introduced from one conditional encounter alone; proper-subset validation remains authoritative.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_156` documents eleven new typed boundaries and rejects starfighter-only power, unconditional shield damage and cockpit-only information for this packet.

## New questions

- What exact original Windows binary revision and input trace reproduce one named first-sector hostile beacon event?
- How do its measured enemy equipment, evasion, FTL charge, room repair and event reward differ from later Advanced Edition versions?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0419` *Nintendogs*, only after this unit's validation, local commit and Goal stop window.
- Optimisation criterion: move from paused multi-system combat to touch/voice pet-care feedback on Nintendo DS.
- Expected information gain: test whether command recognition, care state and short-session evaluation require distinct information and time boundaries.
- Backlog impact: preserve approved `GAME-0419`–`GAME-0432` order; do not start another subject in this unit.

## Why this game

- [Hypothesis | Corroborated | Medium] The original PC ship-command loop contrasts the prior authored Sly stage's direct avatar traversal. Its conditional beacon entry and two encounter exits keep the research boundary reproducible without pretending that one randomized first jump is scripted.
