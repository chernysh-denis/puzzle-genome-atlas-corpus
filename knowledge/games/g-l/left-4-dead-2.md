---
game_id: GAME-0192
slug: left-4-dead-2
game_title: Left 4 Dead 2
analysis_status: reviewed
reviewed: 2026-08-29
combination_ids:
  - COMB-0190
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-199
    - ACT-200
    - ACT-241
    - ACT-260
    - ACT-341
  system:
    - SYS-208
    - SYS-215
    - SYS-292
    - SYS-348
    - SYS-618
    - SYS-619
    - SYS-620
    - SYS-621
    - SYS-622
  constraint:
    - CON-262
    - CON-381
    - CON-390
    - CON-512
    - CON-513
  information:
    - INF-073
    - INF-115
    - INF-116
    - INF-119
    - INF-246
  objective:
    - OBJ-115
  time:
    - TIM-003
---

# Game: Left 4 Dead 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodded Windows Steam client, public build
  `23990068`, built and updated `2026-06-30`, checked `2026-08-29`; Campaign in
  Single Player, `Dead Center` chapter `The Hotel` (`c1m1_hotel`), Normal
  difficulty, controlling Coach with Rochelle, Ellis and Nick as stock bots.
- Primary decision loop: inspect personal and team health, carried slots,
  ammunition and local sight/sound cues; move, aim, fire or shove, reload,
  switch or collect equipment, use or share restorative items and revive an
  eligible bot; stay close enough for autonomous teammates to support and be
  supported; traverse the burning hotel's authored route while the AI Director
  varies threats and supplies; survive the elevator panic event and seal the
  terminal safe room.
- Entry and exit: begins at first retained Coach control on the hotel roof,
  before leaving the opening checkpoint door. It ends when every living
  Survivor is inside the ground-floor terminal safe room, the door closes and
  the stock chapter transition settles; stop before any retained control in
  `The Streets`.
- Included: the fixed four-Survivor Single Player party and bot substitution;
  Normal Campaign health, temporary health, incapacitation, bleed-out,
  teammate revival and ordinary campaign restart on controlled-player death;
  firearms, melee/shove, ammunition, first-aid, temporary-health items and
  possible throwables; friendly fire; common and Special Infected, including
  teammate-disabling attacks; Director-selected enemy and item population,
  intensity-sensitive pacing and stock route/object variation; the authored
  upper-floor descent, elevator trigger, burning lobby and final checkpoint.
- Reproducible parameterisation: choose Campaign / Single Player, Dead Center,
  The Hotel, Normal and Coach; use no add-ons or console changes. The route and
  safe-room terminal are authored. Exact item identities, Director population,
  Special Infected, blocked side paths, damage, bot decisions and completion
  time are legal run parameters rather than alternate signatures.
- Excluded: the remaining Dead Center chapters and campaign finale; every
  other campaign; online co-op, public or community servers, Versus, Scavenge,
  Survival, Realism and Mutations; Expert/Advanced/Easy differences; Workshop,
  add-ons, console commands, speedrun skips and exploits; achievements, stats,
  rankings, awards, account state, DLC/content history and exhaustive weapon or
  infected balance tables.
- Potential scoped modules: one later campaign chapter, one finale, one
  declared online co-op party, Versus, Survival, Realism or a named Mutation.
- Direct-play status: no fresh authenticated playthrough was conducted. Valve's
  current product/update material pins the public client; Valve's GDC design
  paper and developer documentation establish Director, cooperative and panic-
  event boundaries. Valve's archived internal notes and independent route/control
  references corroborate the exact checkpoint and interaction trace. The
  repository transition trace is rules reasoning, not direct play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `L4D2-001` | The current Valve Steam product is Left 4 Dead 2 and the Windows public branch is build `23990068` after Valve's `2026-06-30` security update | Confirmed | Corroborated | High | P1, P2, S1 |
| `L4D2-002` | The scoped ruleset is one player-controlled Survivor with three stock AI Survivors under ordinary Campaign rules | Confirmed | Corroborated | High | P1, S2, S5 |
| `L4D2-003` | Direct movement, aimed firearm/melee combat, shove, switching, reloading, world-item pickup and carried restorative/throwable use form the live action surface | Observation | Corroborated | High | P1, P3, S3, S4 |
| `L4D2-004` | Damage can create incapacitation and bleed-out; a reachable teammate can revive the victim, while direct traumatic or later damage can kill | Confirmed | Direct | High | P3, P4, S3 |
| `L4D2-005` | Friendly fire and Special Infected disabling attacks make spacing and rapid teammate release decision-relevant | Confirmed | Direct | High | P3, P4 |
| `L4D2-006` | The AI Director tracks Survivor intensity, creates peaks and valleys and procedurally populates wanderers, mobs, Special Infected, bosses, weapons and scavenge items | Confirmed | Direct | High | P1, P3 |
| `L4D2-007` | The Hotel follows an authored roof-to-elevator-to-burning-lobby route and the elevator sequence produces a bounded mass attack before the terminal safe room | Observation | Corroborated | High | P5, S6–S8 |
| `L4D2-008` | A chapter transition requires every living Survivor in the checkpoint and a closed safe-room door, preserving carried and Survivor state into the next map | Confirmed | Direct | High | P4 |
| `L4D2-009` | Local visual/audio cues, automatic vocalisations and the Survivor HUD disclose threats, teammate danger, carried equipment and current resources without revealing the next Director population exactly | Observation | Corroborated | High | P3, S3, S4 |
| `L4D2-010` | The repository trace reproduces roof entry, bot-supported traversal, Director variation, elevator panic, incapacitation/recovery and safe-room settlement | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Valve; Windows release in 2009 and currently maintained on
  Steam.
- Platform or physical form: local unmodded Windows PC client with three
  autonomous Survivor bots.
- Puzzle family: cooperative route survival; adaptive encounter pressure;
  teammate-state rescue; authored checkpoint progression.
- Primary sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/550/Left_4_Dead_2/),
    for the current title, Valve identity, Single Player support, four new
    Survivors, weapons/items, five campaigns and AI Director 2.0, checked
    2026-08-29.
  - **[P2]** [official Valve Steam announcements](https://store.steampowered.com/news/posts/?appgroupname=Valve&appids=5724%2C550%2C220%2C440%2C400%2C420%2C380%2C240%2C500%2C70%2C10%2C5489%2C4000%2C5268%2C300%2C30%2C5305%2C80%2C5260%2C5112%2C5091%2C5090%2C5073%2C5063%2C5062%2C5058%2C5059%2C5056%2C5057%2C5051%2C410%2C5032%2C5033%2C5034%2C5035%2C5036%2C5016%2C5015%2C997%2C994%2C987%2C985%2C0&enddate=1783552424&feed=steam_community_announcements),
    for the `2026-06-30` revised Linux security update and immediately prior
    `2026-06-26` crash/exploit fix establishing the current update boundary.
  - **[P3]** [Valve GDC 2009 — Replayable Cooperative Game Design](https://cdn.akamai.steamstatic.com/apps/valve/2009/GDC2009_ReplayableCooperativeGameDesign_Left4Dead.pdf),
    especially pp. 15–26 and 33–58, for cooperative enemy design, disabling
    attacks, sharing, helplessness, automatic vocalisations, intensity-sensitive
    pacing and procedurally populated enemies/items.
  - **[P4]** [Valve archived development notes](https://store.steampowered.com/news/posts/?appids=550&enddate=1383084342&feed=steam_community_announcements),
    for all-living-Survivor checkpoint closure, retained transition state,
    incapacitation, bleed-out, friendly fire and teammate revival.
  - **[P5]** [Valve Developer Community panic-event guide](https://developer.valvesoftware.com/wiki/L4D_Level_Design%3Azh-cn/Panic_Events%3Azh-cn),
    for an authored elevator/button relay requesting a one-shot Director panic
    event independently of the adaptive ambient population.
- Secondary and reproducible sources:
  - **[S1]** [SteamDB Left 4 Dead 2 depots](https://steamdb.info/app/550/depots/),
    observed 2026-08-29, for public build `23990068`, built and updated
    2026-06-30; Steam/Valve sources independently establish product identity
    and the corresponding update boundary.
  - **[S2]** [Left 4 Dead Wiki gameplay modes](https://left4dead.fandom.com/wiki/Gameplay_Modes),
    for one controlled Survivor, bot-filled Single Player and controlled-player
    death restarting the Campaign chapter.
  - **[S3]** [StrategyWiki controls](https://strategywiki.org/wiki/Left_4_Dead_2/Controls),
    for PC movement, aim, fire/swing, shove, heal/revive and item-giving inputs.
  - **[S4]** [StrategyWiki weapons](https://strategywiki.org/wiki/Left_4_Dead_2/Weapons),
    for carried slot/ammunition and equipment behaviour.
  - **[S5]** [GameFAQs character-selection answer](https://gamefaqs.gamespot.com/pc/359377-left-4-dead-2/answers/171857-how-to-change-characters),
    for selecting campaign, map, difficulty and controlled character in the
    ordinary single-player entry interface.
  - **[S6]** [StrategyWiki The Hotel](https://strategywiki.org/wiki/Left_4_Dead_2/The_Hotel),
    for upper-floor descent, elevator, burning ground floor and terminal
    safehouse route.
  - **[S7]** [Prima eGuide — Vannah Hotel Floor 8](https://primagames.com/eguides/left-4-dead-2-eguide/walkthrough/dead-center/vannah-hotel-floor-8),
    for the upper-floor route into the elevator.
  - **[S8]** [Prima eGuide — Vannah Hotel Lobby](https://primagames.com/eguides/left-4-dead-2-eguide/walkthrough/dead-center/vannah-hotel-lobby),
    for the elevator mass attack, fire-filled route and first safe room.
  - **[V1]** repository-side transition trace derived from `P1`–`P5` and
    `S2`–`S8`; executable rules reasoning, not direct play.
- Claim IDs: `L4D2-001`–`L4D2-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate Coach; `ACT-161`, aim and attack with the
  current firearm, melee weapon or shove; `ACT-164`, switch the active carried
  slot; `ACT-183`, reload; `ACT-184`, throw an eligible pipe bomb, Molotov or
  bile jar; `ACT-199`, collect/replace compatible world equipment; `ACT-200`,
  use a carried restorative on self; `ACT-241`, revive one reachable
  incapacitated teammate; `ACT-260`, channel a first-aid kit on a living
  teammate; `ACT-341`, open a reachable route door or activate the elevator.
- New genes: none; every player-issued command has an already active boundary.
- Parameters: movement, aim, weapon, slot, magazine, throwable, item, target,
  health state, channel, interruption, route object and interaction state.
- Claim IDs: `L4D2-003`–`L4D2-005`, `L4D2-007`, `L4D2-010`.

### System Behaviour Genes

- Existing genes: `SYS-208`, resolve firearm aim, obstruction and body hit;
  `SYS-215`, resolve directly commanded real-time combat; `SYS-292`, resolve a
  thrown tactical item's flight and area effect; `SYS-348`, apply damage,
  permanent/temporary health, incapacitation, bleed-out, revival and death.
- New genes: `SYS-618`, run stock autonomous Survivor bots around the controlled
  player; `SYS-619`, modulate encounter population and pacing from team
  intensity; `SYS-620`, resolve a Special Infected's isolating hold until
  release or victim defeat; `SYS-621`, launch a one-shot authored panic event
  from a route trigger; `SYS-622`, settle a chapter when the living party seals
  the exit safe room.
- Resolution order: the party leaves the roof checkpoint; movement, equipment
  and combat resolve continuously while bots follow/fight/support; the Director
  observes intensity and populates unseen reachable areas; a disabling Special
  Infected can transfer one Survivor into teammate-dependent danger; damage may
  enter incapacitation and revival; the elevator trigger requests an authored
  panic population; reaching and sealing the final checkpoint settles the map.
- Claim IDs: `L4D2-003`–`L4D2-010`.

### Constraint Genes

- Existing genes: `CON-262`, weapon/item slots and ammunition are finite;
  `CON-381`, compatible attacks can damage allies; `CON-390`, first-aid and
  revival channels require a reachable compatible Survivor state and may be
  interrupted.
- New genes: `CON-512`, incapacitated or Special-Infected-held Survivors lose
  ordinary self-rescue authority and depend on a legal teammate intervention;
  `CON-513`, the next chapter cannot load until every living Survivor is inside
  the terminal checkpoint and its door is closed.
- Scarce strategic resources: health and temporary health, living mobile
  teammates, recovery time, ammunition, carried slot capacity, throwables,
  first-aid, safe firing lines, positional cohesion and low-intensity windows.
- Claim IDs: `L4D2-003`–`L4D2-008`.

### Information Genes

- Existing genes: `INF-073`, active weapon, magazine/reserve and carried slots
  are visible; `INF-115`, local sight, spatial sound and effects expose partial
  hostile state; `INF-116`, Survivor frames and shared chapter condition are
  visible; `INF-119`, Coach's health and status are visible.
- New gene: `INF-246`, automatic Survivor vocalisations, outlines and adaptive
  music disclose teammate danger, nearby Special Infected and short-term route
  pressure without revealing the exact next population.
- Claim IDs: `L4D2-003`–`L4D2-010`.

### Objective Genes

- Existing genes: none.
- New gene: `OBJ-115`, bring every living Survivor into The Hotel's ground-
  floor safe room and close the door to complete the chapter.
- Success, evaluation and failure: the safe-room transition is the positive
  terminal. Reaching the elevator, defeating a horde or entering the terminal
  corridor is intermediate. Controlled-player death restarts the chapter and
  therefore fails that attempt without becoming a separate campaign ending.
- Claim IDs: `L4D2-007`, `L4D2-008`, `L4D2-010`.

### Time Genes

- Existing gene: `TIM-003`, the controlled Survivor, bots, Infected, health,
  item channels and Director pressure evolve concurrently in real time.
- New genes: none.
- Claim IDs: `L4D2-003`–`L4D2-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Single Player / Dead Center / Hotel / Normal / Coach selected | Start the chapter and accept first roof control | Coach is directly controlled and three other Survivors enter as stock bots | fixed local party and entry state | `L4D2-002`, `L4D2-010` |
| Opening checkpoint stocked; exterior door closed | Collect compatible equipment, select a slot and open the door | Carried slot state changes and the authored hotel route becomes traversable | finite loadout joined to route commitment | `L4D2-003`, `L4D2-007` |
| A reachable Infected is visible or audible | Move, aim, fire/shove and reload as required | Hits, damage, ammunition and hostile state resolve while bots continue acting | direct combat inside concurrent party pressure | `L4D2-003`, `L4D2-005` |
| Director observes current team state and unseen reachable areas | Continue traversing | Exact wanderers, mobs, Specials and supplies are selected under intensity/population rules | structured variation without changing the authored terminal | `L4D2-006` |
| A Special Infected pins or drags one Survivor | Another living party member attacks or shoves the captor | The hold ends if the rescuer resolves a legal release before victim defeat | enforced proximity and rescue authority | `L4D2-005` |
| Teammate is incapacitated and reachable | Hold the revive interaction without interruption | Teammate returns to mobile control with the configured post-revive health state | downed state is recoverable only through another body | `L4D2-004` |
| Coach or a living bot lacks permanent health; first-aid kit is held | Channel self-use or teammate healing | Completion consumes the kit and restores eligible permanent health; interruption cancels completion | support-item timing competes with live danger | `L4D2-003`, `L4D2-004` |
| Party reaches the working hotel elevator trigger | Activate the authored control and remain viable | The elevator transition requests its one-shot mass attack before the burning-lobby route | panic event is authored, not merely a random Director peak | `L4D2-007` |
| Every living Survivor is inside the ground-floor safe room | Close the terminal door | Chapter-complete transition settles and retained state is prepared for The Streets | reproducible positive terminal | `L4D2-008`, `L4D2-010` |

## Strategic and experiential structure

- Local decision: aim versus shove, advance versus regroup, spend ammunition or
  throwable, collect a replacement, heal now or preserve the channel window,
  and free a captured/downed teammate before pressure compounds.
- Medium-term planning: maintain cohesion through narrow rooms and fire, keep
  complementary weapons/items across the four bodies, anticipate a panic event
  at the elevator and reserve health/ammunition for the exposed lobby route.
- Long-term structure: convert a variable Director-populated descent into four
  living, mutually rescuable bodies at the fixed safe-room checkpoint.
- Common heuristics: do not outrun bot rescue range; listen for Special cues;
  keep firing lanes clear because allies are valid targets; use lower-intensity
  intervals to heal; clear the area before committing a long revive or first-
  aid channel; enter and seal the safe room together.
- Failure attribution: missed aim, unsafe friendly fire, separation, ignored
  audio cues, item-slot waste, healing at peak intensity or late rescue can be
  distinguished from an unusually harsh legal Director population.
- Player-trust factors: stable authored landmarks and endpoint, explicit party
  frames/outlines, distinctive Special audio, automatic warnings, visible
  ammunition/items and intensity music make hidden population pressure legible
  without exposing its exact future sample.
- Claim IDs: `L4D2-003`–`L4D2-010`.

## Replay and variation

- What changes between sessions: enemy/item population, Special/Boss timing,
  permitted route/object details, bot positions and support choices, damage,
  held equipment and completion time.
- Randomness or procedural generation: the Director selects constrained runtime
  populations and some world objects/routes, and adapts pacing to team
  intensity. The chapter order, major Hotel route, elevator event and exit
  checkpoint remain authored.
- Multiple viable strategies: yes; cautious clearing, faster coordinated
  movement, ranged/melee emphasis, throwable use and different healing timing
  can all reach the same safe-room terminal.
- Typical replay motive: improve team cohesion, threat recognition, resource
  preservation and safe progress through different Director populations.
- Claim IDs: `L4D2-006`–`L4D2-010`.

## Adjacent systems and history

- Direct predecessor: Left 4 Dead established the four-Survivor Director-
  paced cooperative campaign form.
- Variants: other chapters, finales, online players, difficulty levels,
  Realism, Versus, Survival, Scavenge and Mutations are separate bounded
  signatures.
- Similar games: Helldivers 2, Warframe, Back 4 Blood, Deep Rock Galactic and
  other real-time cooperative route shooters.
- Important differences: unlike Helldivers 2, The Hotel has no orbit-selected
  loadout, stratagem code, reinforcement stock or optional extraction after
  mission success; its positive boundary is all-living checkpoint closure.
  Unlike Warframe's Solo opening, L4D2 does not build persistent equipment or
  solve terminal ciphers; it continuously reshapes population from team
  intensity and makes disabling enemies demand immediate ally intervention.
- Claim IDs: `L4D2-002`–`L4D2-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-199`, `ACT-200`, `ACT-241`, `ACT-260`, `ACT-341` | movement, weapon, item, healing, rescue and route-interaction parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-292`, `SYS-348`, `SYS-618`–`SYS-622` | combat, health, bots, Director, capture, panic and transition parameters |
| Constraint | `CON-262`, `CON-381`, `CON-390`, `CON-512`, `CON-513` | capacity, friendly fire, channel, rescue and checkpoint gates |
| Information | `INF-073`, `INF-115`, `INF-116`, `INF-119`, `INF-246` | equipment, hostile, party, personal and cooperative cue state |
| Objective | `OBJ-115` | seal The Hotel terminal safe room with every living Survivor inside |
| Time | `TIM-003` | simultaneous party, hostile, channel and Director time |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `191` (`GAME-0001`–`GAME-0191`).
- Exact genome matches: none.
- Tied near matches: `GAME-0159` — Helldivers 2 (`15 / 49 = 0.306122`).
- Supported combination subsets: `COMB-0190`.
- Scan date: 2026-08-29.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0159` — Helldivers 2 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `SYS-208`, `SYS-215`, `SYS-292`, `CON-262`, `CON-381`, `INF-073`, `INF-115`, `INF-116`, `INF-119`, `TIM-003` | both couple direct squad movement, firearm/grenade combat, friendly fire, finite carried equipment and partial team/local HUD state in real time, but Left 4 Dead 2 fills three same-authority Survivor slots with autonomous bots, adapts population to team intensity, lets Special Infected remove one member's self-authority, launches a route-triggered panic and ends only when every living Survivor seals the safe room; Helldivers instead prepares orbit-selected stratagems, escalates patrol alarms, spends shared Reinforce stock and separates main-objective success from optional extraction | Near, `0.306122` |

### Preserved research notes

- New genes: `SYS-618`–`SYS-622`, `CON-512`, `CON-513`, `INF-246` and
  `OBJ-115`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: direct combat, carried items, teammate channels,
  downed health, friendly fire, partial local information and real time reuse
  safely. Same-role autonomous bots, intensity-modulated population, disabling
  capture, authored panic dispatch, all-living checkpoint settlement and the
  associated rescue/information/terminal boundaries require narrower records.

## Combination status

- `COMB-0190` is a verified strict twenty-nine-gene subset of the thirty-one-
  gene genome, coupling bot-supported route combat, adaptive population,
  teammate-dependent rescue, authored panic and safe-room settlement. The
  optional throwable action/resolution pair remains outside the core.
- Every earlier verified combination is tested deterministically after
  registration; none is a proper subset of this genome.

## Taxonomy impact

- Registry changes: nine new Active genes, evidence links on reused genes,
  `COMB-0190` and existing family memberships.
- Taxonomy-change record: none; no prior lifecycle or reviewed-game signature
  changes.
- Candidate terms affected: autonomous Survivor bot, team-intensity Director,
  disabling Special hold, authored panic event, all-living safe-room closure
  and cooperative danger cue.

## Negative results

- `SYS-602` and `CON-503` are not reused: Sastasha supplies a fixed role-
  complete Tank/Healer/DPS Duty Support party; Hotel bots are same-authority
  Survivors who substitute for human co-op slots and share combat/rescue work.
- `SYS-394` and `SYS-529` are not reused: their terminal death consumes team
  tickets or finalises one competitive round; L4D2 Single Player instead
  restarts the chapter when the controlled Survivor dies.
- `SYS-444` and `CON-391` are not reused: their Healthy/Injured/Dying/Hooked
  catalogue belongs to Dead by Daylight, not permanent/temporary health,
  incapacitation and Special-Infected holds.
- Director-selected supplies and enemies do not make the authored Hotel route
  or safe-room terminal procedural; nor does the fixed elevator panic event
  become an ordinary adaptive peak.
- Online co-op, Versus, other chapters, difficulty modifiers and Workshop
  content are not inherited merely because the current client exposes them.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Current stock Left 4 Dead 2 supports one
  reproducible Normal Single Player Hotel chapter in which Coach and three bots
  survive Director-shaped pressure, an elevator panic event and teammate-
  dependent incapacitation before sealing the terminal safe room
  (`L4D2-001`–`L4D2-010`).

## Нові гени

- [Observation | Corroborated | High] Added nine genes for stock Survivor bots,
  adaptive encounter population, disabling Special holds, authored panic
  dispatch, safe-room settlement, rescue dependence, checkpoint closure,
  cooperative danger cues and the Hotel chapter terminal.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0190` isolates the bot/Director/
  rescue/panic/safe-room interaction that converts a variable combat route into
  one authored chapter result.

## Зміни таксономії

- [Observation | Corroborated | High] No lifecycle migration or reviewed-game
  signature change; established generic genes gain Left 4 Dead 2 evidence only.

## Нові питання

- Which later cooperative shooter keeps adaptive population pacing but replaces
  same-role bot substitution or all-living safe-room closure?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0193` — Destiny 2.
- Optimisation criterion: continue the recorded demand-led Goal in exact order.
- Expected information gain: contrast this authored cooperative checkpoint
  with one current live-service mission and its separately bounded reward
  terminal.
- Backlog impact: fourth of nine authorised game units.

## Чому саме вона

- [Confirmed | Direct | High] It is the next immutable subject in
  `SEARCH_DEMAND_GAME_SELECTION_007`.

## Localisation status

- Ukrainian game, new-gene and combination entries are reviewed in this unit.
- The canonical brand title remains `Left 4 Dead 2`; the explanatory Ukrainian
  title is presentation-only.

## Open questions

- Recheck the Steam public build, latest Valve update and stock Single Player
  menu before later review-on-touch; keep other modes, chapters and add-ons out
  unless a separate bounded scope is authorised.
