---
game_id: GAME-0259
slug: dead-space-2023
game_title: "Dead Space (2023 remake)"
analysis_status: reviewed
reviewed: 2026-09-05
combination_ids:
  - COMB-0257
gene_ids:
  action:
    - ACT-008
    - ACT-131
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-190
    - ACT-199
    - ACT-341
    - ACT-434
  system:
    - SYS-112
    - SYS-208
    - SYS-215
    - SYS-369
    - SYS-380
    - SYS-578
    - SYS-755
    - SYS-780
    - SYS-794
    - SYS-795
  constraint:
    - CON-210
    - CON-262
    - CON-269
    - CON-282
    - CON-285
    - CON-579
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-313
    - INF-314
  objective:
    - OBJ-155
  time:
    - TIM-003
    - TIM-007
---

# Game: Dead Space (2023 remake)

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1693980`, one-app Standard package `805029`, public Windows Build ID
  `10602756`, built 2023-02-21 and published 2023-02-27; checked 2026-09-05.
  The build identifier and dates are secondary distribution observations, not
  a publisher semantic version. This is Motive's 2023 remake rebuilt in
  Frostbite, not Dead Space (2008), a sequel, another platform or a franchise
  union.
- Platform, input and difficulty: Windows, English interface and subtitles,
  keyboard and mouse, fresh base-game `New Game`, default `Medium`. Aim assist,
  automatic weapon swapping and other gameplay assists remain at their stated
  defaults. Controllers, consoles and other difficulty or accessibility
  configurations are separate packets.
- Entry: begin a clean profile with no completed-game state, New Game Plus
  unlocks or Deluxe cosmetics. Follow the mandatory landing sequence without
  optional collection until first ordinary control in the Flight Lounge. The
  packet admits only Chapter 1, `New Arrivals`, and records actual incoming
  Health and carried state rather than importing later equipment.
- Primary decision loop: inspect the current objective, Locator path, local
  sight, Health, Stasis and carried item/ammunition state; walk or sprint
  through the authored tram route; select the Plasma Cutter; aim its horizontal
  or vertical three-beam line at an eligible hostile body region, fire and
  reload finite Plasma Energy; use exposed tissue and intact limbs to decide
  the next regional shot; spend Stasis on the malfunctioning door and unstable
  tram claw; operate circuit breakers within their local power limit; engage
  both claws, replace the tram, recover and install the Data Board, restart
  tram control, return to the damaged shuttle and proceed to Medical.
- Positive terminal: after `New Arrivals` closes and Chapter 2, `Intensive
  Care`, appears, retain the automatic chapter-boundary state. Quit immediately
  without collecting the Kinesis Module or moving the Chapter 2 route, reload
  the newest retained state and verify first ordinary `Intensive Care` control
  with its initial objective. Use the final Chapter 1 Save Station before the
  handoff so the boundary can be replayed if needed; that fallback replay is
  not a substitute for the successor-state check.
- Negative terminal: zero Health closes the current attempt and a chosen load
  restores the last retained checkpoint or Save Station state; that recovery
  is not success. Cutting one limb, replacing the tram, installing the Data
  Board, restarting the tram or reaching Medical without the stated reload
  check is not positive settlement.
- Included: direct over-the-shoulder traversal and sprint; Locator objective
  guidance; Plasma Cutter selection, aim, orientation toggle, shot and reload;
  finite Plasma Energy; required melee or stomp; regional hostile damage,
  layered visual degradation, limb severance and resulting movement/attack/
  defeat changes; Stasis targeting, finite energy and temporary slowdown;
  malfunctioning-door and tram-claw timing; fuse, claw, breaker, Data Board,
  tram-console, Save Station and route interactions; local limited power;
  route pickups, finite inventory, one restorative, Health, lethal failure,
  checkpoint restoration and retained Chapter 2 handoff.
- Excluded: Deluxe suits/textures; New Game Plus, Impossible and every other
  difficulty; consoles, controller input and non-Windows builds; Store
  purchase, sale or storage; Bench upgrades, Power Nodes, Semiconductor/credit
  economy, optional rooms, logs, collectibles and side routes; Kinesis, Pulse
  Rifle, security-clearance progression, zero-G and all Chapter 2/later
  mechanics; Intensity Director-specific variation not independently
  established inside this trace; achievements, mods, cheats, debug tools,
  speedrun skips, the 2008 original, sequels, screenshots, official artwork,
  third-party assets, video and audio evidence.
- Reproducible parameterisation: install English app `1693980` from Standard
  package `805029`; choose fresh New Game and Medium with stated defaults;
  record actual entry resources; follow only mandatory objectives; acquire the
  Plasma Cutter, toggle both line orientations and sever at least one leg or
  arm from an eligible Chapter 1 hostile; reload once after spending compatible
  ammunition; acquire Stasis, slow the malfunctioning door and right tram claw;
  latch the left claw, slow and latch the unstable claw, repair the tram;
  power the Maintenance Bay elevator and office while lights are off, collect
  and install the Data Board, restart the tram, return to the shuttle and
  perform the stated chapter-boundary reload check. Exact path, hostile,
  region, ammunition, Health, pickups and timing remain parameters.
- Potential scoped modules: one later named chapter; one exact Store/Bench
  economy packet; one Kinesis combat/route packet; one Impossible run; New Game
  Plus; or the 2008 original each requires its own version, entry, loop,
  terminal and evidence review.
- Direct-play status: not conducted. Valve application/package data and EA's
  product page establish lawful availability and Standard/Deluxe separation.
  Official EA control, gameplay and developer articles establish Medium,
  controls, the Plasma Cutter boundary and layered dismemberment. Three
  independent static written routes corroborate the Chapter 1 door, claw,
  breaker, Data Board, tram and Chapter 2 transitions. This is an evidence-
  backed rules reconstruction, not a claimed playthrough or entitlement. No
  video or audio was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DSR-001` | Steam app `1693980` is the current English Windows base game and Standard package `805029` contains only that app, distinct from Deluxe cosmetics | Confirmed | Direct | High | P1–P3 |
| `DSR-002` | The public Windows branch reports Build ID `10602756`, built 2023-02-21 and published 2023-02-27 | Observation | Direct | High | S1 |
| `DSR-003` | Medium is the default baseline-damage difficulty; keyboard/mouse exposes movement, interaction, Locator, inventory, map, aim, fire, alternate fire, reload, Stasis and melee/stomp controls | Confirmed | Direct | High | P4–P6 |
| `DSR-004` | The Chapter 1 Plasma Cutter spends compatible ammunition, reloads and changes its three-beam cutting line between horizontal and vertical orientations | Confirmed | Corroborated | High | P4, S2–S4 |
| `DSR-005` | Damage accumulates on a targeted hostile region, may sever its attached limb and changes the hostile's remaining movement or attack capability before final defeat | Confirmed | Corroborated | High | P2, P7, P8, S2–S4 |
| `DSR-006` | Layered skin, flesh and bone damage exposes which region is weakened without relying on a conventional hostile health bar | Confirmed | Direct | High | P7, P8 |
| `DSR-007` | The acquired Stasis Module spends finite personal energy to slow eligible moving targets, including the malfunctioning door and unstable tram claw | Confirmed | Corroborated | High | P4, S2–S4 |
| `DSR-008` | The Maintenance Bay breaker admits only two of three local branches, so elevator and office power require the lights branch to be disabled | Observation | Corroborated | High | S2, S4 |
| `DSR-009` | Replacing the tram requires latching the stable claw and slowing the retracting claw long enough to latch it and commit repair | Observation | Corroborated | High | S2–S4 |
| `DSR-010` | Tram replacement, Data Board recovery/installation, tram restart and shuttle return form the ordered mandatory chain into Medical and Chapter 2 | Observation | Corroborated | High | S2–S5 |
| `DSR-011` | Health, carried resources and pickups are visible; a med pack restores missing Health and finite inventory constrains retained stock | Confirmed | Corroborated | High | P4, S2–S4 |
| `DSR-012` | Save Stations retain progress, while lethal failure and load replace failed transient combat/resource state with a retained state | Observation | Corroborated | High | S2–S5 |
| `DSR-013` | Medical arrival closes `New Arrivals`, starts `Intensive Care` and exposes a retained boundary reloadable before successor play | Observation | Corroborated | Medium | S2, S3, S5 |
| `DSR-014` | The bounded identity is readable regional degradation converting precise cutting into capability loss while temporary machine slowdown and scarce local power complete one retained repair chapter | Strong Pattern | Corroborated | High | `DSR-004`–`DSR-013` |

## Basic data

- Release / origin: Motive Studio and Electronic Arts; Steam records release on
  2023-01-27. EA describes this product as rebuilt from the ground up.
- Platform or physical form: lawfully offered English Windows single-player
  Steam application `1693980`; one fresh Medium Chapter 1 packet.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-05:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=1693980&cc=ua&l=english),
    for exact title/app, Windows and English support, single-player, release,
    developer/publisher, package relations and current Ukraine offer.
  - **[P2]** [current Steam product page](https://store.steampowered.com/app/1693980/Dead_Space/?l=english),
    for current lawful Windows availability, remake identity, engineering-tool
    combat and strategic precision. Embedded media was not opened or used.
  - **[P3]** [EA Dead Space product page](https://www.ea.com/games/dead-space/dead-space),
    for Motive/EA identity, rebuilt-remake boundary, Windows/Steam offer and
    Standard/Deluxe separation. Gallery media was not opened or used.
  - **[P4]** [EA PC controls](https://www.ea.com/able/resources/dead-space/dead-space/pc/controls),
    for movement, sprint, interaction, med pack, Locator, RIG inventory/map,
    melee, stomp, aim, shoot, alternate fire, reload and Stasis input.
  - **[P5]** [EA PC gameplay settings](https://www.ea.com/able/resources/dead-space/dead-space/pc/gameplay),
    for Medium baseline damage, default-disabled automatic weapon swap,
    aim-assist options, Locator orientation and tutorial prompts.
  - **[P6]** [EA PC initial settings](https://www.ea.com/able/resources/dead-space/dead-space/pc/initial),
    for default English, subtitles and Medium selection.
  - **[P7]** [Motive, Inside Dead Space #1](https://www.ea.com/inside-ea/news/inside-dead-space-1-remaking-a-classic),
    for Frostbite rebuild, seamless ship and peeling/dismemberment as direct
    damage feedback and strategic choice.
  - **[P8]** [Motive, Inside Dead Space #2](https://careers.ea.com/ea-studios/motive/news/inside-dead-space-2-new-necromorph-nightmare),
    for layered tissue/bone state, weakened-region inspection, limb severance
    and weapon-dependent regional effects.
- Corroborating textual sources, accessed 2026-09-05:
  - **[S1]** [SteamDB public depots](https://steamdb.info/app/1693980/depots/),
    for Build `10602756`, its dates and Windows English depot observation.
    SteamDB is not treated as the publisher.
  - **[S2]** [VULKK static Chapter 1 route](https://vulkk.com/2023/02/08/dead-space-remake-chapter-1-walkthrough/),
    for first control, cutter orientation, targeted limbs, Stasis door, claws,
    breakers, Data Board, tram restart, Save Station and Medical transition.
    Images were not opened or used.
  - **[S3]** [Neoseeker static `New Arrivals` route](https://www.neoseeker.com/dead-space-2023/walkthrough/New_Arrivals),
    for independent Chapter 1 objective order, saving and `Intensive Care`.
  - **[S4]** [Gamer Guides static Data Board route](https://earth.gamerguides.com/dead-space-remake/guide/walkthrough/chapter-1-new-arrivals/where-to-find-the-data-board),
    for two-of-three breaker capacity, the elevator/office/light trade-off,
    region-severing guidance and Data Board access. Images were not opened.
  - **[S5]** [Game8 static Chapter 1 route](https://game8.co/games/Dead-Space-Remake/archives/402113),
    for remake-specific Chapter 1 equipment and its transition to Chapter 2.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P8` and `S1`–`S5` under the declared app, package, build, platform,
  difficulty, clean entry, exclusions and retained terminal; rules reasoning,
  not direct play.
- Claim IDs: `DSR-001`–`DSR-014`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: walk/sprint through the ship; `ACT-161`: aim and commit a
  cutter shot or required close strike; `ACT-164`: select the cutter;
  `ACT-183`: reload it from compatible Plasma Energy.
- Existing `ACT-190`: apply Stasis to an eligible door or claw; `ACT-131`:
  consume a med pack after Health loss; `ACT-199`: transfer a compatible route
  resource into carried stock; `ACT-341`: operate fuses, claws, breaker
  branches, Data Board socket, tram console, Save Station and route fixtures.
- New `ACT-434`: reorient the cutter's linear firing pattern between horizontal
  and vertical planes before the next shot. Names and exact inputs remain
  parameters. Claims: `DSR-003`, `DSR-004`, `DSR-007`–`DSR-012`.

### System Behaviour Genes

- Existing `SYS-208`: ranged damage resolves against the struck body region;
  `SYS-215`: attacks continue in real time; `SYS-578`: damage/healing change
  continuous Health and zero ends the attempt; `SYS-369`: load restores a
  retained checkpoint.
- Existing `SYS-380`: Stasis applies finite targeted slowdown; `SYS-755`:
  accepted damage removes a fuse or breakable container; `SYS-112`: claw, Data
  Board and console interactions expose dependent state; `SYS-780`: the final
  route closes Chapter 1 and admits retained Chapter 2.
- New `SYS-794`: cumulative damage peels one body region, may sever it and
  removes the movement/attack capability carried by that region. New `SYS-795`:
  a local limited circuit transfers power among fixture branches and
  deactivates a competitor when capacity is reached.
- Resolution order: objective/Locator exposes the gate; movement changes reach;
  equipment and orientation define the hit; a shot spends ammunition and
  resolves regional damage; visible layers update and severance changes
  capability; Stasis spends energy for a door/claw window; breaker selection
  changes powered reach; tram/Data Board interactions advance the route; the
  chapter handoff retains successor control. Claims: `DSR-004`–`DSR-014`.

### Constraint Genes

- Existing `CON-210`: carried stacks obey typed capacity; `CON-262`: weapon,
  magazine and reserve are finite; `CON-285`: fire/orientation/reload require
  compatible cutter, ammunition and action state; `CON-269`: Stasis requires
  eligible target, range and positive energy/readiness.
- Existing `CON-282`: door, claws, repair, breaker, Data Board, tram restart,
  shuttle return and Medical transition require authored predecessors;
  `CON-579`: a med pack requires missing Health and carried stock.
- Scarce resources: Health, safe distance, cutter magazine/reserve, line
  orientation, intact hostile capabilities, Stasis energy/duration, breaker
  capacity, inventory slots and retained progress. Exact values are parameters.
  Claims: `DSR-004`, `DSR-007`–`DSR-013`.

### Information Genes

- Existing `INF-073`: active tool/ammunition are visible; `INF-115`: current
  sight/effects expose nearby threats, with no imported audio evidence;
  `INF-119`: Health, Stasis and personal resources are visible; `INF-125`:
  Locator/map/objective show the known route; `INF-128`: pickups/inventory show
  identity, compatibility and capacity.
- New `INF-313`: intact limbs and layered tissue/bone degradation expose which
  region is closer to severance and what capability remains without an enemy
  health bar. New `INF-314`: a breaker exposes branch identity, current power
  and fixed capacity before selection. Claims: `DSR-003`–`DSR-013`.

### Objective Genes

- Existing `OBJ-155`: survive the mandatory Chapter 1 repair/return chain,
  close `New Arrivals` and retain first `Intensive Care` control after reload.
  Tram repair or one encounter alone is not completion. Claims: `DSR-009`–`DSR-014`.

### Time Genes

- Existing `TIM-003`: enemies, damage, reload, Stasis duration and claw motion
  advance in real time; `TIM-007`: a retained state can be restored and another
  target, expenditure or timing can replace the failed future.
- Claims: `DSR-004`–`DSR-014`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Medium route reaches the escaped workshop | Collect the Plasma Cutter | Cutter becomes active with actual starting Plasma Energy | reproducible equipment entry | `DSR-001`, `DSR-003`, `DSR-004` |
| Cutter is readied and an elongated hostile region is exposed | Toggle alternate fire, align the beam line and shoot | Ammunition decreases and damage is attributed to that region | deliberate regional attack | `DSR-004`, `DSR-005` |
| The region remains attached | Inspect layers and commit additional aligned shots | Tissue/bone exposure increases until severance or defeat | readable regional progress | `DSR-005`, `DSR-006` |
| A leg or attack limb reaches severance | Resolve the accepted cut while the hostile remains viable | Corresponding locomotion or attack option is removed | capability-changing dismemberment | `DSR-005`, `DSR-006` |
| Cutter magazine is empty but reserve remains | Reload | Reserve enters the magazine during lost fire readiness | finite ammunition loop | `DSR-003`, `DSR-004` |
| The malfunctioning door cycles too quickly | Aim/apply Stasis, then cross before expiry | Energy decreases and door motion slows temporarily | machine-control window | `DSR-007` |
| Stable claw is latched; second claw retracts | Apply Stasis, latch it and use central console | Slowed hold lets both claws replace the tram | timed maintenance | `DSR-007`, `DSR-009` |
| Breaker exposes office, lights and elevator with capacity two | Power elevator and office, leaving lights off | Two route fixtures work while the room is dark | local power trade-off | `DSR-008` |
| Data Board is recovered | Install it and restart tram control | Tram route becomes active and objective advances | authored fixture chain | `DSR-010` |
| Health reaches zero | Load the retained state | Failed positions, damage and spending are replaced | negative recovery | `DSR-011`, `DSR-012` |
| Shuttle sequence is complete | Proceed to Medical and accept transition | `New Arrivals` closes; `Intensive Care` begins | segment handoff | `DSR-010`, `DSR-013` |
| First Chapter 2 control is retained | Quit and reload without collecting successor equipment | Chapter title, initial objective and control return | reproducible positive terminal | `DSR-012`–`DSR-014` |

## Strategic and experiential structure

- Planning horizon: Locator fixes the next gate, but cutter ammunition must be
  allocated among body regions, Stasis preserved for machinery and breaker
  capacity traded between visibility and reach.
- Local tactics: choose cutter orientation to intersect a long limb, read
  exposed layers, remove the most dangerous capability and reload before the
  threat closes distance.
- Medium-term structure: Stasis creates a crossing or claw-latch window;
  limited power trades light for route access; tram and Data Board convert
  those decisions into chapter progress.
- Reversible versus irreversible: aim/orientation can change; shots, Stasis,
  damage, healing and breaker state change the attempt; severance removes a
  capability; load replaces failure; chapter completion persists.
- Failure attribution: visible ammunition, Health, Stasis, body layers, limb
  presence, branch power and objective state separate wrong target geometry,
  exhausted resources, missed timing, missing dependency and lethal exposure.
- Player trust: damage predicts severance, detachment has a functional result,
  panel state reflects power and a reloaded chapter title verifies the terminal.

## Replay and variation

- What changes: encounter position, target region, cutter orientation,
  ammunition/reload/Stasis timing, Health, pickups, breaker order and time.
- Randomness or procedural generation: topology, fixtures and objectives are
  authored. Encounter timing and drops may vary, but no Intensity Director-
  specific claim enters this packet.
- Multiple strategies: other limbs, avoidance lines, melee and optional stock
  may work; this trace requires one observed severance, both Stasis machine uses
  and the direct elevator/office breaker allocation.
- Typical replay motive: improve region selection and conserve resources while
  shortening the same maintenance chain.

## Adjacent systems and history

- Resident Evil 4 (2023) shares over-the-shoulder authored combat, finite
  ammunition, health, pickups and a Chapter 1-to-2 terminal. It adds aim focus,
  stagger, parry and case packing; Dead Space exposes regional degradation and
  severs capabilities.
- DOOM (2016) shares direct ranged combat, finite resources, authored locks and
  visible damage, but turns stagger into a close finisher rather than choosing
  a limb plane to alter threat anatomy.
- CONTROL shares third-person traversal, selected live effects, Health and
  fixture gates. Its reserves regenerate and launched props dominate its route;
  Dead Space spends ammunition/Stasis across anatomy and timed machinery.
- Tomb Raider (2013) shares third-person authored movement, resource pressure,
  combat and checkpoint continuation, but not regional severance information
  or limited local breaker allocation.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-190`, `ACT-199`, `ACT-341`, `ACT-434` | cutter, Stasis, fixture and input names are parameters |
| System Behaviour | `SYS-112`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-380`, `SYS-578`, `SYS-755`, `SYS-780`, `SYS-794`, `SYS-795` | layers, limbs, capabilities, branches and durations are parameters |
| Constraint | `CON-210`, `CON-262`, `CON-269`, `CON-282`, `CON-285`, `CON-579` | quantities, ranges, capacity, order and compatibility are parameters |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-313`, `INF-314` | HUD art, branch labels and tissue appearance are parameters |
| Objective | `OBJ-155` | chapter, repairs, successor and retained state are parameters |
| Time | `TIM-003`, `TIM-007` | frame rate, durations and load time are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `258` (`GAME-0001`–`GAME-0258`).
- Exact genome matches: none.
- Tied near matches: `GAME-0258` — Prey (2017) (`22 / 39 = 0.564103`).
- Supported combination subsets: `COMB-0257`.
- Scan date: 2026-09-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0258` — Prey (2017) | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-341`, `SYS-112`, `SYS-215`, `SYS-369`, `SYS-380`, `SYS-578`, `CON-210`, `CON-262`, `CON-282`, `CON-285`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `TIM-003`, `TIM-007` | Prey makes ordinary-prop identity uncertain and sequences finite foam control into a Wrench follow-up before an office-objective handoff. Dead Space exposes regional hostile damage, changes cutter-line orientation, severs embodied capabilities and routes finite Stasis plus limited local power through a complete tram-repair chapter. | Near, `0.564103` |

### Preserved research notes

- New genes: `ACT-434`, `SYS-794`, `SYS-795`, `INF-313`, `INF-314`.
- Reused genes: `ACT-008`, `ACT-131`, `ACT-161`, `ACT-164`, `ACT-183`,
  `ACT-190`, `ACT-199`, `ACT-341`, `SYS-112`, `SYS-208`, `SYS-215`,
  `SYS-369`, `SYS-380`, `SYS-578`, `SYS-755`, `SYS-780`, `CON-210`,
  `CON-262`, `CON-269`, `CON-282`, `CON-285`, `CON-579`, `INF-073`,
  `INF-115`, `INF-119`, `INF-125`, `INF-128`, `OBJ-155`, `TIM-003`, `TIM-007`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Lower-ID scan: reject `SYS-402`/`INF-156`, whose wounds feed a Focus strike
  rather than detach a region; reject `ACT-393`/`SYS-724`, which tune
  starfighter performance; reject `SYS-158`, an economic grid; reject
  `INF-303`/`SYS-776`, whose reticle focus changes shot advantage.

## Taxonomy impact

- Registry changes: add five Active genes, `ACT-434`, `SYS-794`, `SYS-795`,
  `INF-313`, `INF-314`, plus `COMB-0257`; add independent support to reused
  genes. No existing definition, lifecycle or earlier signature changes.
- Taxonomy-change record: none; no split, merge, deprecation or broadening.
- Candidate terms: recorded in `CANDIDATE_TERMS.md`; all product, actor, tool,
  room, chapter, app, package and build names remain parameters.

## Negative results

- No video or audio evidence was used; only official static pages and static
  written routes support this packet.
- Kinesis, Pulse Rifle, Store, Bench, upgrades, credits and every Chapter 2
  action are excluded; the terminal stops before successor equipment use.
- `ACT-393`, `SYS-724` and `SYS-158` do not fit the local breaker boundary.
- `SYS-208` retains ordinary hit location; `SYS-794` enters only because
  accumulated regional damage detaches a region and removes its capability.
- A severed limb, repaired tram or installed Data Board is not the terminal;
  the reload-verified Chapter 2 handoff is required.

## Delta summary

## New facts

- [Confirmed/Observation | Direct/Corroborated | High] `DSR-001`–`DSR-014`:
  one repair chapter couples visible regional degradation, functional cuts,
  temporary machine slowdown and limited local power.

## New genes

- [Confirmed/Observation | Direct/Corroborated | High] Added `ACT-434`,
  `SYS-794`, `SYS-795`, `INF-313` and `INF-314`.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0257` — oriented regional
  cutting and functional severance feed Stasis/power-gated tram repair into
  retained successor control.

## Taxonomy changes

- [Observation | Direct/Corroborated | High] Five portable genes are added; no
  prior definition, lifecycle or reviewed signature changes.

## New questions

- Does Metro Exodus preserve the finite survival-action resource skeleton
  while replacing anatomical severance and local breaker capacity with
  light/pressure-sensitive stealth and another retained chapter gate?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0260` — Metro Exodus.
- Optimisation criterion: retain bounded authored survival-action pressure but
  vary sensing, environmental resources and route terminal.
- Expected information gain: distinguish explicit regional targeting from
  light/visibility and equipment-maintenance decisions.
- Backlog impact: advances the approved batch-014 ordered horizon.

## Why this game

- [Hypothesis | Limited | High] Metro Exodus preserves first-person finite-
  resource pressure while changing the information source and maintenance loop.
