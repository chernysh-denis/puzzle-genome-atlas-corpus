---
game_id: GAME-0381
slug: goldeneye-007
game_title: GoldenEye 007
analysis_status: reviewed
reviewed: 2026-09-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-341
  system:
    - SYS-057
    - SYS-215
    - SYS-222
    - SYS-578
  constraint:
    - CON-578
    - CON-688
  information:
    - INF-115
    - INF-119
    - INF-388
  objective:
    - OBJ-223
  time:
    - TIM-003
---

# Game: GoldenEye 007

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Bond, Dam, PP7,
KF7, the four red alarm boxes and the bungee platform are scenario parameters,
not portable gene names.

## Analysis scope

- Version / ruleset: the original English 1997 Nintendo 64 single-player
  GoldenEye 007 rules, represented by Nintendo's licensed Nintendo 64 Classics
  application for Nintendo Switch Online + Expansion Pack. The original 1997
  instruction booklet is the rules source. The installed Classics wrapper,
  emulation build and cartridge bytes were not inspected.
- Scenario: one fresh Secret Agent attempt in Mission 1, Part I: Dam, from
  first ordinary control near the entrance to mission-result settlement after
  the bungee-platform exit. Secret Agent requires both neutralising all four
  alarms and jumping from the platform; Agent's single-objective route and 00
  Agent's modem and data-backup tasks are outside this packet.
- Entry: the Dam mission has just begun, the four alarm fixtures remain live,
  the mission-objective checklist is available, and Bond controls his starting
  weapon. Exact health, ammunition and guard placements are not inferred from
  the booklet and remain bounded attempt parameters.
- Primary decision loop: read the local first-person view, sound, health,
  ammunition and mission checklist; move through the authored gates and towers;
  aim and fire at guards, breakable locks or the four alarms; choose an acquired
  weapon and pick up compatible ammunition or body armour; prevent guards from
  triggering an alarm when possible; confirm that all four alarm objectives
  are complete; then reach and leave from the bungee platform.
- Positive terminal: after every alarm is neutralised, stepping from the
  designated platform completes the bungee objective and settles the Dam
  mission as successful. Facility play is outside the packet.
- Failure terminal: zero life ends the attempt; leaving from the platform
  before the alarm objective is complete closes the mission with an incomplete
  required objective instead of satisfying Secret Agent success. The player
  can retry from a fresh Dam attempt.
- Included: direct first-person traversal and aimed fire, opening the authored
  doors, breaking the required lock, four breakable alarm fixtures, local guard
  pursuit or alarm response, finite ammunition, optional weapon and body-armour
  pickups, health/armour survival, the mission-objective watch, and the
  objective-before-departure decision.
- Reproducible parameterisation: select Secret Agent and fresh Dam; follow a
  normal gate-and-tower route; destroy the alarm near the satellite structure
  and the three tower alarms; reach the platform after the checklist confirms
  alarm completion; step off to settle. Guard shots, pickups, health remaining
  and time are bounded variables, not required exact traces.
- Excluded: 00 Agent's covert modem and data backup, any optional sniper-rifle
  tactic, speed-run time or Paintball reward, complete guard extermination,
  multiplayer, later campaign missions, cheats, custom 007 difficulty, Xbox
  rerelease controls, Switch online multiplayer, rewind/save-state effects and
  any wrapper-specific input latency or audiovisual enhancements.
- Direct-play status: not conducted. No original cartridge, licensed Switch
  installation, ROM, executable, controller trace, save, screenshot, video or
  audio was examined. This is a source-bounded reconstruction from Nintendo's
  booklet and independent original-N64 Dam guides.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GE-001` | Nintendo's licensed Classics edition presents the 1997 Nintendo 64 game; the packet models original N64 single-player rules | Confirmed | Corroborated | High | P1, P2 |
| `GE-002` | Mission and difficulty are chosen before play; Secret Agent is the middle difficulty | Confirmed | Direct | High | P2 |
| `GE-003` | The mission briefing and pause watch disclose mandatory objectives, current equipment, ammunition and life/armour | Confirmed | Direct | High | P2 |
| `GE-004` | The original combat interface permits local movement, aimed weapon fire, weapon selection, contextual use and finite ammunition | Confirmed | Direct | High | P2 |
| `GE-005` | Secret Agent Dam asks for all alarms to be neutralised and a bungee jump, with four alarm fixtures on the ordinary route | Observation | Corroborated | High | S1, S2 |
| `GE-006` | The alarm near the gated satellite structure and the three tower alarms are breakable by gunfire; a guard can run toward the first alarm | Observation | Corroborated | High | S1, S2 |
| `GE-007` | The platform ends the Dam mission; departing before all mandatory alarms are resolved yields an incomplete-objective failure, not Secret Agent success | Observation | Corroborated | Medium | S1–S3 |
| `GE-008` | A fatal hit closes the attempt; armour can protect the life reserve, and a new attempt returns to the mission setup | Confirmed | Direct | High | P2 |
| `GE-009` | The admitted signature does not inherit 00 Agent's modem/data tasks or later-mission mechanics | Observation | Corroborated | High | P2, S1–S3, V1 |

## Basic data

- Release / origin: Rare-developed, Nintendo-published GoldenEye 007, original
  Nintendo 64 release 1997. Nintendo distributes the original game in its
  Nintendo 64 Classics library on Switch through Expansion Pack membership.
- Platform or physical form: licensed Nintendo Switch access to the Nintendo
  64 Classics edition. The analysed rules are original N64 Secret Agent Dam;
  no wrapper behaviour is claimed.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-24:
  - **[P1]** [Nintendo: GoldenEye 007 returns for Switch Online + Expansion
    Pack](https://www.nintendo.com/en-ca/whatsnew/goldeneye-007-returns-for-nintendo-switch-online-expansion-pack-members/),
    for licensed 1997-N64 identity, availability and stealth/action framing.
  - **[P2]** [Nintendo/Rare original 1997 instruction booklet,
    transcription](https://www.world-of-nintendo.com/manuals/nintendo_64/goldeneye_007.shtml),
    for three difficulties, objectives, pause watch, controls, weapons, ammo,
    life/armour and retry. It is original-publisher text hosted by an archive;
    exact booklet pages should be checked against the preserved scan in a
    future direct-source audit.
- Independent original-N64 route descriptions, accessed 2026-09-24:
  - **[S1]** [GameFAQs Dam Secret Agent route by
    Reptile](https://gamefaqs.gamespot.com/n64/197462-goldeneye-007/faqs/23689),
    for the two-objective list, gate/tower sequence, first guard alarm run,
    four alarm destructions and platform terminal.
  - **[S2]** [GameFAQs 1998 route by
    liukang](https://gamefaqs.gamespot.com/n64/197462-goldeneye-007/faqs/3215),
    for difficulty-specific objectives and independent four-alarm/platform
    corroboration. The guide's time-cheat tactic is not adopted as the route.
  - **[S3]** [StrategyWiki Dam objective
    reference](https://strategywiki.org/wiki/GoldenEye_007/Dam), for the
    warning that the jump ends the mission even when higher-difficulty
    objectives are unfinished. The page was search-index readable but directly
    opening it was blocked; this particular failure detail remains Medium.
- Validation source: **[V1]** repository-side transition reconstruction from
  P1–P2 and S1–S3 only, not direct gameplay.
- Claim IDs: `GE-001`–`GE-009`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly steer Bond through the gatehouse, dam-top towers and
  platform route instead of assigning an automatic destination.
- `ACT-161`: aim and fire the active weapon at a reachable guard, breakable
  gate lock or red alarm box. Destroying the alarm is mission progress, not
  merely a kill tally.
- `ACT-164`: switch between the starting weapon and any legally acquired
  weapon; the sniper rifle is optional, not a required signature item.
- `ACT-341`: operate reachable doors and gate controls to continue along the
  authored route.
- Claims: `GE-004`–`GE-006`.

### System Behaviour Genes

- `SYS-057`: an eligible guard responds to local sight or sound and may run
  toward an alarm rather than remaining a static target.
- `SYS-215`: aimed shots and enemy return fire resolve while the world remains
  live; the player can move, change cover and continue attacking.
- `SYS-222`: compatible dropped weapons, ammunition or body armour can be
  collected into the current attempt's carried resources.
- `SYS-578`: hostile damage depletes one continuous life reserve; zero life
  ends the attempt. Armour protection is a source-confirmed buffer but its
  exact damage formula is not assigned a separate gene here.
- Resolution order: movement and guard response update the local encounter;
  accepted shots consume ammunition and may destroy an alarm; destroyed alarms
  update the checklist; the platform closes the mission and evaluates the
  mandatory objective state.
- Claims: `GE-004`–`GE-008`.

### Constraint Genes

- `CON-578`: consuming firearm attacks require compatible finite rounds;
  collected ammunition refills the relevant stock. No exact starting count is
  required by this packet.
- New `CON-688`: the platform departure is available before all alarms are
  necessarily neutralised, but successful Secret Agent settlement requires
  completion of the full declared alarm set; early departure ends an
  incomplete mission rather than being physically blocked.
- Scarce state: life, armour, ammunition, guard exposure, remaining alarms
  and safe access to the departure platform.
- Claims: `GE-004`, `GE-005`, `GE-007`, `GE-008`.

### Information Genes

- `INF-115`: first-person sight and spatial sound reveal only local guards,
  fire and nearby alarm fixtures rather than a global enemy map.
- `INF-119`: the mission watch and HUD expose the current life/armour and
  equipped ammunition needed to judge survival.
- New `INF-388`: the briefing and watch expose the fixed Secret Agent Dam
  objective list and its current completion state, separating alarm progress
  from mere route traversal.
- Claims: `GE-003`, `GE-005`.

### Objective Genes

- New `OBJ-223`: neutralise the finite set of four declared alarm fixtures,
  then depart from the designated bungee platform to settle the Dam mission
  successfully on Secret Agent.
- Claims: `GE-005`, `GE-007`.

### Time Genes

- `TIM-003`: Bond's inputs, guard motion, alarm attempts and combat resolve in
  live time while the next action remains available. The optional Paintball
  speed threshold is excluded.
- Claims: `GE-004`, `GE-006`, `GE-008`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Fresh Secret Agent Dam, four alarms live | inspect briefing or Q Watch | the two required objectives, current equipment, ammo and life/armour are inspectable | explicit mission state | `GE-002`, `GE-003`, `GE-005` |
| A guard is visible beyond cover | move and fire the active weapon | valid aim spends compatible rounds, may defeat the guard, and may provoke live response | direct combat with finite stock | `GE-004`, `GE-006` |
| A guard is moving toward the first alarm | intercept or evade while approaching its fixture | guard response can change local pressure; alarm neutralisation still requires destruction of the fixture | tactical alarm pressure | `GE-006` |
| One reachable alarm remains live | aim and shoot its box | the fixture is destroyed and that member of the required set becomes complete | finite objective progress | `GE-005`, `GE-006` |
| Four alarms have been destroyed | inspect objectives | the alarm objective is complete; the bungee departure remains | visible order before exit | `GE-003`, `GE-005` |
| All alarms complete and Bond reaches the bungee platform alive | step from the designated edge | bungee objective and Dam success settle; Facility is only the next mission | positive terminal | `GE-005`, `GE-007` |
| A required alarm remains live at platform departure | step from the designated edge | the level ends with an incomplete Secret Agent requirement, not mission success | non-blocking exit condition | `GE-007` |
| Life reaches zero before a successful jump | accept mission failure and retry | the failed attempt closes; a new attempt begins from the Dam setup | failure boundary | `GE-008` |

## Strategic and experiential structure

- Local decision: choose whether to shoot a guard, conserve ammunition, collect
  a dropped weapon or press ahead while alarm and return-fire risks continue.
- Medium-term planning: track the one compound-area alarm and three dam-top
  tower alarms; a visible route to the platform is not evidence that the
  Secret Agent objective is complete.
- Long-term structure: the mission couples a finite destruction checklist to
  an independently reachable departure. Neither every guard's death nor a
  speed-run reward is a success requirement.
- Failure attribution: life/armour and ammo are visible; the mission checklist
  distinguishes missing alarms from physical inability to find the platform.
- Player-trust factors: the booklet explicitly instructs players to read
  objectives, while this record marks the early-exit failure as secondary-
  source corroboration rather than claiming direct play.
- Claim IDs: `GE-003`–`GE-009`.

## Replay and variation

- What changes: guard response, shots, pickups, remaining life, ammunition and
  route timing. The four required alarm locations and platform do not
  randomise in this packet.
- Viable approaches: controlled shots and optional cover/weapon pickups can
  differ, but all accepted Secret Agent routes must resolve the same alarm set
  before departing.
- Claim IDs: `GE-005`–`GE-008`.

## Adjacent systems and history

- Metal Gear Solid's opening also combines direct infiltration and guards,
  but it models staged alert recovery and radar cones; this Dam packet does
  not infer those systems. DOOM's E1M1 shares direct combat and finite ammo,
  but its exit switch lacks this four-alarm mission checklist.
- The 2023 Xbox rerelease and Nintendo Classics wrapper make the title
  available today; neither establishes altered original-N64 Dam mechanics in
  this source-bounded packet.
- Claim IDs: `GE-001`–`GE-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-008, ACT-161, ACT-164, ACT-341 | Direct movement, fire, equip and use |
| System Behaviour | SYS-057, SYS-215, SYS-222, SYS-578 | Guard response, live combat, pickups and life |
| Constraint | CON-578, CON-688 | Ammunition and non-blocking objective-before-exit rule |
| Information | INF-115, INF-119, INF-388 | Local cues, personal state and objective checklist |
| Objective | OBJ-223 | Four alarms then bungee departure |
| Time | TIM-003 | Live mission clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `380` (`GAME-0001`–`GAME-0380`).
- Exact genome matches: none.
- Tied near matches: `GAME-0352` — DOOM (1993) (`12 / 19 = 0.631579`).
- Supported combination subsets: none.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0352` DOOM (1993) | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-341`, `SYS-057`, `SYS-215`, `SYS-222`, `SYS-578`, `CON-578`, `INF-115`, `INF-119`, `TIM-003` | Both have direct real-time firearm combat, pickups and finite ammunition. DOOM's E1M1 closes through a single route exit with automap and armour-split rules; GoldenEye's Secret Agent Dam exposes a four-alarm checklist and lets an early bungee departure terminate unsuccessfully. Neither game transfers the other's objective boundary. | Near, `0.631579` |

### Preserved research notes

- New genes: CON-688, INF-388, OBJ-223.
- Classification result: additive new-gene boundaries plus established direct
  combat, navigation and information genes.
- Evidence and reasoning: Nintendo's manual establishes a readable mission
  contract; two original-N64 route descriptions establish the exact Dam
  checklist and alarm locations.

## Taxonomy impact

- Registry changes: three additive Active IDs; prior signatures unchanged.
- Taxonomy-change record: TAXONOMY_CHANGE_120.
- Candidate terms affected: non-blocking early exit, objective checklist,
  declared alarm-set completion.

## Negative results

- No direct-play observation. A live alarm's reinforcement details and exact
  damage values are not accepted beyond the local guard-response boundary.
- The optional modem/data route is not part of Secret Agent Dam.

## Delta summary

## New facts

- [Confirmed | Direct | High] `GE-001`–`GE-004`, `GE-008` establish product,
  briefing, controls, watch and failure affordances from Nintendo material.
- [Observation | Corroborated | High] `GE-005`–`GE-006` establish Secret Agent
  Dam's four alarms, guard pressure and platform route from original-N64 guides.

## New genes

- [Observation | Corroborated | Medium] Three additive IDs distinguish the
  checklisted finite alarm target, visible progress and failure on an early but
  physically reachable departure.

## New combinations

- [Observation | Corroborated | High] No verified combination is introduced.

## Taxonomy changes

- [Confirmed | Corroborated | High] TAXONOMY_CHANGE_120 adds three boundaries
  without changing earlier game signatures.

## New questions

- Does the current licensed Classics build present any wrapper-specific
  control, save-state or input timing differences from a physical N64 attempt?
- What precise objective and result text appears after a Secret Agent jump
  with a single alarm intact?

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0382 Ōkami HD, the next recorded
  genre-alternating subject.
- Optimisation criterion: contrast checklisted live infiltration with an
  authored brush-and-world-state puzzle.
- Expected information gain: isolate brush affordances and divine-power
  gates without inheriting GoldenEye's combat objectives.
- Backlog impact: preserves the selected nine-game order.

## Why this game

- [Hypothesis | Limited | Medium] GoldenEye is a recognisable N64 espionage
  game with a mechanically distinctive mission contract beyond gunplay.
