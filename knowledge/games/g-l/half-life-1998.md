---
game_id: GAME-0239
slug: half-life-1998
game_title: Half-Life (1998)
analysis_status: reviewed
reviewed: 2026-09-03
combination_ids:
  - COMB-0237
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-199
    - ACT-341
    - ACT-408
    - ACT-409
  system:
    - SYS-215
    - SYS-339
    - SYS-348
    - SYS-369
    - SYS-752
    - SYS-753
    - SYS-754
    - SYS-755
  constraint:
    - CON-262
    - CON-282
    - CON-285
    - CON-305
    - CON-580
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Half-Life (1998)

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: original **Half-Life**, current unmodified English Windows
  Steam app `70`, default public 25th Anniversary branch, public Build ID
  `15961492`, built 2024-10-08 and published 2024-10-09, checked 2026-09-03;
  one fresh base single-player campaign on `Medium`, original non-HD models,
  mouse and keyboard, and only the complete `Unforeseen Consequences` chapter
  packet across `c1a0c`, `c1a1`, `c1a1a`, `c1a1f`, `c1a1b`, `c1a1c` and
  `c1a1d` into the ordinary `Office Complex` successor.
- Primary decision loop: read local hazards, hostiles, health, HEV protection,
  flashlight reserve, current weapon and ammunition; move, crouch, jump, climb
  and swim through the damaged authored facility; toggle a reachable friendly
  scientist or guard between follow and wait so role-specific help can open a
  gate, heal or add autonomous fire; activate doors, scanners, lifts, buttons
  and the final elevator; toggle finite self-recharging light; hold use at a
  finite wall health station when missing health; collect the crowbar, pistol,
  ammunition, health and batteries; break eligible glass or grating and survive
  live alien combat until the next chapter loads.
- Entry and exit: a fresh `Medium` New Game and the preceding `Black Mesa
  Inbound` / `Anomalous Materials` route are setup only. Entry is the first
  retained direct control in the ruined test chamber at the beginning of
  `c1a0c` after the resonance cascade. Positive exit is the completed final
  elevator transit and first controllable `Office Complex` state, immediately
  retained in an ordinary manual save. Zero health ends the attempt; loading
  the latest retained auto/manual save is recovery, not an alternate terminal.
- Included: first-person locomotion and stance; authored ladders, water and
  suspended-box traversal; scientist/guard use, follow/wait and local
  role-specific assistance; direct crowbar and pistol combat; weapon switching,
  magazine reload and finite ammunition; health kits, batteries, health
  charger and HEV protection; flashlight toggle, drain and automatic recharge;
  doors, scanners, lifts, buttons and elevator; breakable route glass/grating;
  local headcrab, zombie, houndeye, bullsquid and barnacle threats; electrical,
  laser, fall, water and machinery hazards; ordered map gates, save/load, death
  and chapter transition.
- Excluded: all playable actions before first `Unforeseen Consequences` control
  and after first `Office Complex` control; the full campaign, Hazard Course,
  Uplink, Deathmatch and multiplayer; `steam_legacy`, HD models, Half-Life:
  Source, Black Mesa, Opposing Force, Blue Shift and every mod; achievements,
  exhaustive secrets, enemy/weapon/pickup catalogues, narrative union,
  speedruns, skips, glitches, cheats, console commands and manual map loading;
  other difficulties, languages, controllers, Steam Deck, Linux, macOS, console
  ports and later franchise games.
- Reproducible parameterisation: on a fresh local profile select `New Game` and
  `Medium`, keep the default 25th Anniversary public branch and original model
  option, use mouse/keyboard, complete only the required setup route, then save
  at first `c1a0c` control. Record one scientist follow-to-scanner transition,
  one follow/wait toggle, one flashlight drain/recharge cycle, one held wall-
  station transfer when naturally reachable, one crowbar break, one pistol
  shot and reload, one resource pickup, one death/reload if naturally reached,
  the final elevator and an immediate save at first `Office Complex` control.
  Exact health, HEV charge, light reserve, ammunition, friendly actor, hostile
  positions, optional pickups, save timing and completion time are parameters.
- Potential scoped modules: `Black Mesa Inbound`; `Anomalous Materials`; one
  later base chapter; the complete base campaign; Hazard Course; Uplink; one
  Deathmatch map; the pre-anniversary `steam_legacy` branch; or a named official
  expansion. None is silently combined here.
- Direct-play status: not conducted. Current Valve product/update material,
  Valve's published Half-Life SDK, a preserved original Valve manual and
  independent written chapter traces establish the declared rules, build,
  entry, mechanisms and terminal. The transitions below are evidence-based
  rules reconstruction, not a claimed captured playthrough. No video or audio
  was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HL1-001` | The lawfully sold original Half-Life is Steam app `70`; Valve calls the default 25th Anniversary version definitive and future-supported | Confirmed | Direct | High | P1, P2 |
| `HL1-002` | The scoped Windows public branch is Build ID `15961492`, while `steam_legacy` is a separately labelled pre-anniversary build | Confirmed | Corroborated | High | P2, S1 |
| `HL1-003` | A fresh game exposes `Easy`, `Medium` and `Difficult`; the control route fixes `Medium`, original models and mouse/keyboard | Confirmed | Direct | High | P2, P8 |
| `HL1-004` | `Unforeseen Consequences` begins at the ruined test chamber, spans the declared seven-map packet and precedes `Office Complex` | Observation | Corroborated | High | S2–S5 |
| `HL1-005` | The player directly moves, crouches, jumps, climbs, swims, aims, attacks, selects weapons, reloads, collects resources and uses authored objects | Observation | Corroborated | High | P3, P7, P8, S3–S5 |
| `HL1-006` | Use on an eligible scientist or guard toggles following; the actor paths locally and can supply role-specific door, healing or combat help | Confirmed | Direct | High | P5–P8, S3 |
| `HL1-007` | The early required control-room gate needs a living scientist brought to its scanner before the authored route opens | Observation | Corroborated | High | P8, S3–S5 |
| `HL1-008` | Holding use at a reachable wall health station transfers a finite reservoir into missing health while eligibility remains true | Confirmed | Direct | High | P4, P8 |
| `HL1-009` | The HEV flashlight is manually toggled, drains its visible reserve while active and recharges automatically while inactive | Confirmed | Direct | High | P3, P8 |
| `HL1-010` | Eligible glass or other breakable world objects accumulate accepted damage and are removed at their break threshold, changing local passage or contents | Confirmed | Direct | High | P7, P8, S3 |
| `HL1-011` | Local hostile perception/pursuit, direct combat, environmental hazards, health and HEV protection resolve concurrently into survival or death | Observation | Corroborated | High | P3, P6, P8, S3–S5 |
| `HL1-012` | The final elevator carries the player to first `Office Complex` control; manual save/load can retain that state and recover failed attempts | Observation | Corroborated | High | P8, S2–S5, V1 |
| `HL1-013` | The bounded structure joins actor-gated access, damage-gated topology, finite light/restoration and live combat in one fixed successor route | Observation | Corroborated | High | P3–P8, S2–S5, V1 |

## Basic data

- Release / origin: developed and published by Valve; released for Windows on
  1998-11-19 and retained as the current Steam product **Half-Life**.
- Platform or physical form: authored single-player first-person action game;
  only the current unmodified English Windows base-campaign packet declared
  above is admitted.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  spatial logic and topology; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/70/HalfLife/),
    for original product identity, Valve authorship, 1998 release, lawful
    Windows sale, single-player and separately excluded online PvP.
  - **[P2]** [official Half-Life 25th Anniversary page](https://www.half-life.com/en/halflife/25th),
    for definitive/future-supported status, original models as default,
    `steam_legacy`, Uplink, multiplayer additions, UI/flashlight fixes and the
    boundaries excluded from this base single-player packet.
  - **[P3]** [Valve Half-Life SDK `player.cpp`](https://github.com/ValveSoftware/halflife/blob/master/dlls/player.cpp),
    for health/HEV damage, death, flashlight toggle and battery update, movement
    state, continuous-use state and player HUD data.
  - **[P4]** [Valve Half-Life SDK `healthkit.cpp`](https://github.com/ValveSoftware/halflife/blob/master/dlls/healthkit.cpp),
    for touch health kits and the wall charger's player/suit/reservoir checks,
    held-use transfer cadence, finite depletion and single-player behaviour.
  - **[P5]** [Valve Half-Life SDK `scientist.cpp`](https://github.com/ValveSoftware/halflife/blob/master/dlls/scientist.cpp),
    for scientist use, follow/stop schedules, door-use capability, fear and
    eligible healing behaviour.
  - **[P6]** [Valve Half-Life SDK `barney.cpp`](https://github.com/ValveSoftware/halflife/blob/master/dlls/barney.cpp),
    for guard use, following, local perception, firearm response and defeat.
  - **[P7]** [Valve Half-Life SDK `func_break.cpp`](https://github.com/ValveSoftware/halflife/blob/master/dlls/func_break.cpp),
    plus [weapons](https://github.com/ValveSoftware/halflife/blob/master/dlls/weapons.cpp),
    [buttons](https://github.com/ValveSoftware/halflife/blob/master/dlls/buttons.cpp)
    and [doors](https://github.com/ValveSoftware/halflife/blob/master/dlls/doors.cpp),
    for damage-threshold breakage, material/trigger rules, ammunition/reload and
    authored fixture activation.
  - **[P8]** [preserved original Valve Half-Life: Day One manual](https://valvearchive.com/archive/Half-Life/Half-Life/Guides/Half-Life%20Day%20One%20Manual/Half-LifeD1.PDF),
    pp. 5, 9–10 and 13–18, for difficulty labels, save/load, locomotion, Use on
    people/objects, held charger use, breakable glass, weapon/ammunition HUD,
    HEV protection and flashlight drain/automatic recharge. Day One's bounded
    content is not used as chapter evidence; its shared shipped rules are
    corroborated by Valve's SDK.
- Secondary and reproducible textual sources:
  - **[S1]** [SteamDB Half-Life depots](https://steamdb.info/app/70/depots/),
    observed 2026-09-03, for app `70`, current Windows public Build ID
    `15961492`, its build/update timestamps and separate `steam_legacy` branch;
    SteamDB identifies itself as unaffiliated with Valve.
  - **[S2]** [Combine OverWiki chapter record](https://www.combineoverwiki.net/wiki/Unforeseen_Consequences),
    for the seven retail maps, ruined-chamber entry, suspended-box traversal and
    `Office Complex` successor; development and port variants are excluded.
  - **[S3]** [StrategyWiki written chapter route](https://strategywiki.org/wiki/Half-Life/Unforeseen_Consequences),
    for scanner assistance, live hazards, crowbar/glass, local allies, combat,
    pickups, water and authored route order. Embedded media was not loaded.
  - **[S4]** [Stanley E. Dunigan written walkthrough](https://media.runthinkshootlive.com/pdf/half-life-walkthrough.pdf),
    pp. 11–16, for an independent original-game route through `c1a0c`–`c1a1d`
    and the final interior elevator control into `Office Complex`.
  - **[S5]** [Danny Cox written chapter route](https://halflife.dannycox.me.uk/halfLife/walkthrough/03.html),
    for an independent scanner, laser, crowbar, combat and chapter-exit trace.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P8` and `S1`–`S5` under the fixed product, public branch, difficulty,
  entry, map packet, successor and exclusions; no direct-play or audiovisual
  claim.
- Claim IDs: `HL1-001`–`HL1-013`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly walk/run, crouch, jump, climb and swim through
  the authored first-person facility route; `ACT-161`: aim and commit a crowbar
  or pistol attack; `ACT-164`: select an owned weapon; `ACT-183`: reload a
  magazine-fed weapon; `ACT-199`: collect compatible weapons, ammunition,
  health and batteries; `ACT-341`: activate or hold use on a reachable scanner,
  door, lift, button, health station or elevator control.
- New `ACT-408`: use one reachable eligible allied actor to toggle that actor
  between following the controlled avatar and waiting in place.
- New `ACT-409`: toggle a personal portable illumination device between active
  and inactive states without replacing the current movement or weapon action.
- Exact actor, weapon, charger, scanner, fixture, map and input labels are
  parameters, not genes.
- Claim IDs: `HL1-005`–`HL1-010`, `HL1-013`.

### System Behaviour Genes

- Existing `SYS-215`: resolve directly commanded combat; `SYS-339`: route local
  hostiles from eligible perception into pursuit/attack; `SYS-348`: apply
  compatible damage across HEV protection and health into death; `SYS-369`:
  replace a failed attempt with a selected retained save.
- New `SYS-752`: after an accepted follow request, route the living allied actor
  toward the player and execute that actor's local role-specific assistance —
  fixture access, healing or autonomous fire — until wait, refusal, defeat or
  route separation ends the relation.
- New `SYS-753`: while legal use is held, transfer units from a finite fixed
  station reservoir into the matching missing personal meter, stop at either
  capacity or depletion, and retain the reduced station state.
- New `SYS-754`: while personal illumination is active, emit its local visible
  field and drain the separate reserve; while inactive, remove the field and
  automatically restore reserve toward its cap.
- New `SYS-755`: apply eligible damage or a declared trigger to a breakable
  world object's retained durability and, at its threshold, remove its blocking
  body while resolving declared debris, target or contents state.
- Resolution order: expose current local scene/resources; accept movement,
  light, ally, fixture, pickup or attack input; validate role, reach, equipment,
  station and authored prerequisites; route allies and hostiles; update live
  light and station reserves; resolve attacks, hazards, protection, health and
  breakable objects; propagate door/map gates; save/load on request or failure;
  and settle the final elevator transition into the successor chapter.
- Claim IDs: `HL1-005`–`HL1-013`.

### Constraint Genes

- Existing `CON-262`: magazines and carried reserve ammunition are finite;
  `CON-282`: scanner, hazard, breakable, lift, canal, crate and final-elevator
  gates follow authored dependency order; `CON-285`: firing, switching and
  reload require compatible live equipment/ammunition state; `CON-305`: a
  hostile may pursue/attack only after eligible perception and along a usable
  local route.
- New `CON-580`: continuous transfer from a fixed personal-resource station is
  legal only while the user remains in reach holding the interaction, the actor
  and target meter are compatible, capacity is missing and the station retains
  transferable stock.
- Friendly actor reach, living state, disposition, current follower state and
  role capability are parameters of `ACT-408` / `SYS-752`; the required
  scientist scanner order is already represented by `CON-282` rather than a
  quest-named constraint.
- Scarce strategic resources: health, HEV protection, wall-station reservoir,
  flashlight reserve, loaded and reserve ammunition, living ally access, safe
  routes, hazard timing and retained save progress.
- Claim IDs: `HL1-006`–`HL1-013`.

### Information Genes

- Existing `INF-073`: active weapon, magazine and reserve ammunition are
  visible; `INF-115`: first-person local sight and spatial effects expose only
  nearby allies, hostiles, hazards, pickups and route geometry; `INF-119`:
  health, HEV protection and flashlight reserve are visible; `INF-125`: chapter
  titles, actor gestures and visible fixture/route changes expose the current
  authored gate without revealing the full future route.
- Audio is not evidence for this unit. Exact HUD art, colour, reticle, screen
  position and run-specific quantities remain presentation parameters.
- Claim IDs: `HL1-005`–`HL1-013`.

### Objective Genes

- Existing `OBJ-026`: make the bounded authored chapter route traversable and
  reach its designated successor location, first `Office Complex` control,
  then retain that state in an ordinary manual save.
- A scanner opening, crowbar pickup, combat encounter, canal exit, suspended-
  box crossing or elevator entry is intermediate. Campaign completion is out of
  scope; death/load is attempt recovery rather than positive settlement.
- Claim IDs: `HL1-004`, `HL1-007`, `HL1-012`, `HL1-013`.

### Time Genes

- Existing `TIM-003`: player inputs, friendly/hostile actors, projectiles,
  hazards, flashlight drain/recharge, charger transfer and moving machinery
  resolve concurrently in real time. Pause/save menus and loads do not create a
  turn system.
- Claim IDs: `HL1-005`–`HL1-013`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh local profile on the default public anniversary branch | Select `New Game`, then `Medium`; complete setup until first post-cascade control and save | `c1a0c` starts in the ruined test chamber with authored HEV state; preceding chapters remain setup | exact product, mode and entry | `HL1-001`–`HL1-004` |
| An eligible living scientist is reachable and not following | Face the actor and press Use once | The actor accepts or refuses by current disposition; acceptance targets the player and begins local following | explicit follower command | `HL1-006` |
| The same accepted follower is still eligible and near | Press Use on that actor again | The actor drops the player as follow target and waits under its local schedule | reversible follow/wait state | `HL1-006` |
| The required scanner is closed and a suitable scientist has been brought to it | Approach the scanner with the follower | The scientist performs the role-capable use and the authored control-room route opens | actor capability gates topology | `HL1-006`, `HL1-007` |
| A guard follows while an eligible hostile becomes locally perceivable | Keep the guard within route reach and expose the hostile | The guard independently acquires and fires while player control remains separate; loss or separation removes that help | commanded ally has autonomous role-specific effect | `HL1-006`, `HL1-011` |
| The HEV flashlight reserve is positive in a dark local route | Toggle illumination on, observe drain, then toggle it off | A local light field exists while active and reserve falls; inactive state restores reserve automatically toward cap | finite reversible information resource | `HL1-009` |
| A wall health station has stock and the player has eligible missing health | Stay in reach and hold Use | Health rises in repeated units while station stock falls; release, full health, lost reach or depletion stops transfer | continuous finite fixture transfer | `HL1-008` |
| The same station is empty or the player lacks compatible missing capacity | Hold the same interaction | No further personal resource is transferred and the station retains its exhausted/ineligible state | station legality is separate from input | `HL1-008` |
| The crowbar is collected and an eligible glass pane blocks the route | Aim and strike until its threshold is crossed | Accepted damage reduces object durability; threshold removes its solid body and exposes the intended passage | damage changes topology | `HL1-005`, `HL1-010` |
| A loaded pistol and visible hostile are in legal attack relation | Aim, fire and later reload from reserve | A round leaves the magazine; hit/damage and hostile response resolve live; reload transfers compatible reserve into the magazine | ordinary finite firearm kernel | `HL1-005`, `HL1-011` |
| A hostile perceives an eligible cue and has a local route | Move, hide, attack or change geometry | Pursuit and attack update concurrently with hazards, ally action and personal resource state | opposition is local and real-time | `HL1-011` |
| Health reaches zero before the successor | Load the latest retained save | Position, actors, hazards, resources and authored fixtures are replaced by the saved state | reproducible failed-attempt recovery | `HL1-011`, `HL1-012` |
| The route through `c1a1d` and back to the final elevator is open | Enter, activate its interior control and accept the map transition | Elevator transit loads `Office Complex`; first control is immediately preserved in a manual save | reproducible positive terminal | `HL1-004`, `HL1-012`, `HL1-013` |

## Strategic and experiential structure

- Local decision: spend scarce pistol ammunition or use the crowbar; bring a
  role-capable ally through danger or leave them safe; illuminate now or bank
  flashlight reserve; remain exposed long enough to draw health from a station;
  cross a timed hazard, break a route object or seek another authored opening.
- Medium-term planning: preserve health, HEV protection, light and ammunition
  across several maps while recognising which gates depend on a living actor,
  a world-object state, safe traversal or a fixed fixture sequence.
- Long-term structure: the destroyed laboratory first teaches actor-gated
  access, then shifts authority to the player's tools and resource management,
  repeatedly changing the navigable route until one fixed elevator produces a
  retained successor chapter.
- Common heuristics: keep a scientist near until the required scanner resolves;
  switch followers to wait before avoidable hazards; turn light off outside dark
  areas; use finite wall health before abandoning a one-way section; break only
  visibly eligible material; reload behind cover rather than during pursuit.
- Failure attribution: health/HEV/light/ammunition displays, visible follower
  motion, scanner/door change, station depletion, breakable removal and save
  replacement distinguish resource, order, timing and combat failures. Exact
  hostile positions and concurrent action keep local outcomes bounded rather
  than fully predetermined.
- Player-trust factors: the manual and SDK disclose each admitted resource and
  use rule; required world-state changes are visible before the player advances;
  and named first control in the next chapter replaces arbitrary sandbox stop.
- Claim IDs: `HL1-005`–`HL1-013`.

## Replay and variation

- What changes between attempts: optional follower use, guard survival,
  flashlight timing, station use, health/HEV state, ammunition spend, pickups,
  hostile position, damage, hazard timing, save placement and completion time.
- What remains fixed: app/build branch, original base campaign, `Medium`, the
  seven-map packet, required scientist scanner, authored topology and final
  `Office Complex` successor.
- Multiple viable strategies: cautious crowbar conservation, more pistol use,
  ally-assisted combat, different optional pickup routes and different light or
  healing timing can converge on the same fixed terminal.
- Typical replay motive: improve survival/resource efficiency, preserve allies,
  discover a cleaner route or reduce completion time; exhaustive secrets and
  speedrun techniques remain outside the unit.
- Claim IDs: `HL1-003`–`HL1-013`.

## Adjacent systems and history

- Direct franchise corridor: Half-Life: Source, Black Mesa and Half-Life 2
  preserve related places or names but replace engine, physics, level details
  and product boundaries; expansions use other protagonists and routes.
- Similar lower-ID games: Half-Life 2 shares direct first-person combat,
  equipment, local hostile pursuit, authored fixtures, protection/health,
  checkpoints and fixed chapter transitions, but its Ravenholm packet centres
  remote rigid-body selection and launch. Max Payne (2001) shares firearms,
  finite resources, authored fixtures, save replacement and a fixed successor,
  but adds slow time, delayed carried medicine and adaptive opposition.
- Important difference: this original packet makes a transient world NPC's
  toggled follow state causally necessary for route access, then composes it
  with finite continuous wall restoration, a separately draining/recharging
  personal light and damage-removable world barriers.
- Claim IDs: `HL1-001`–`HL1-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-341`, `ACT-408`, `ACT-409` | scientist, guard, scanner, flashlight, crowbar and weapon names are parameters |
| System Behaviour | `SYS-215`, `SYS-339`, `SYS-348`, `SYS-369`, `SYS-752`, `SYS-753`, `SYS-754`, `SYS-755` | actor roles, rates, reserves, material and damage values are parameters |
| Constraint | `CON-262`, `CON-282`, `CON-285`, `CON-305`, `CON-580` | map order, reach, capacities and exact fixture predicates are parameters |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125` | HUD art, colour, labels and positions are presentation |
| Objective | `OBJ-026` | chapter and successor names are parameters |
| Time | `TIM-003` | frame rate, update intervals and load duration are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `238` (`GAME-0001`–`GAME-0238`).
- Exact genome matches: none.
- Tied near matches: `GAME-0212` — Half-Life 2 (`18 / 33 = 0.545455`).
- Supported combination subsets: `COMB-0237`.
- Scan date: 2026-09-03.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0212` — Half-Life 2 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-341`, `SYS-215`, `SYS-339`, `SYS-348`, `SYS-369`, `CON-262`, `CON-285`, `CON-305`, `INF-073`, `INF-115`, `INF-119`, `OBJ-026`, `TIM-003` | Half-Life 2's Ravenholm unit adds remote rigid-prop pull, collision-bounded hold and attributed launch damage. Half-Life (1998) instead adds a reversible transient ally command whose role opens the route, finite held-use station transfer, separate toggled light drain/recharge, damage-threshold world-object removal and explicit authored-order cues. | Near, `0.545455` |

### Preserved research notes

- New genes: `ACT-408`, `ACT-409`, `SYS-752`, `SYS-753`, `SYS-754`,
  `SYS-755`, `CON-580`.
- Reused genes: `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`,
  `ACT-341`, `SYS-215`, `SYS-339`, `SYS-348`, `SYS-369`, `CON-262`,
  `CON-282`, `CON-285`, `CON-305`, `INF-073`, `INF-115`, `INF-119`,
  `INF-125`, `OBJ-026`, `TIM-003`.
- Classification result: `New gene` and `New combination of known and new
  genes`.
- Evidence and reasoning: generic movement, combat, equipment, local pursuit,
  ordered route, save replacement, presentation and terminal boundaries fit
  unchanged. The new names isolate portable command, assistance, station,
  illumination and breakage transitions; no character, facility, chapter,
  quest, map, weapon, device, reward or numeric value enters a canonical label.

## Taxonomy impact

- Registry changes: seven new Active genes with portable names and game-scoped
  examples; no prior definition, lifecycle or reviewed signature changes.
- Taxonomy-change record: none.
- Candidate terms affected: transient ally follow/wait, role-specific local
  assistance, held finite station transfer, portable light drain/recharge and
  damage-threshold world-object removal are accepted. Scientist, guard, HEV,
  scanner, charger, flashlight, crowbar and map names remain local parameters.

## Negative results

- `SYS-308` and `SYS-407` are rejected: they describe a deployed or persistent
  owned combat companion. The admitted actors are transient authored world
  allies toggled directly between follow/wait and differentiated by local role;
  no party roster, deployment, skill loadout or persistent ownership exists.
- `ACT-189` is rejected: Use does not issue a selected destination or attack-
  move order. `ACT-408` changes only the ally's follow relation.
- `ACT-236` and `SYS-593` are rejected: the flashlight is neither a discrete
  rechargeable combat-item charge nor a fuelled light/heat field with darkness
  survival authority. `ACT-409` / `SYS-754` retain only toggle, local light,
  drain and automatic recharge.
- `ACT-407`, `SYS-750` and `CON-579` are rejected for the wall station: no
  carried restorative is consumed and recovery is continuous only while held
  use and station stock remain legal.
- `SYS-705` / `SYS-706` are rejected: no Ravenholm Gravity Gun pull, hold or
  player-launched rigid-prop resolver occurs in this packet. Ordinary glass
  breakage belongs to `SYS-755`.
- Day One content, source ports, audio, optional secrets and whole-campaign
  narrative do not enter the genome. No previous reviewed signature changes.

## Combination subset scan

- Every verified pre-unit combination was tested as a proper subset of the
  complete 27-gene signature; none qualified.
- `COMB-0237` is reserved for the strict transient-ally / finite-station /
  rechargeable-light / breakable-route chapter core and excludes ordinary
  equipment and presentation support.
- Comparison and subset scan date: 2026-09-03.
