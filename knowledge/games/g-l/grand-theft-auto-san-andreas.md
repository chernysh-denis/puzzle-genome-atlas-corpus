---
game_id: GAME-0357
slug: grand-theft-auto-san-andreas
game_title: "Grand Theft Auto: San Andreas"
analysis_status: reviewed
reviewed: 2026-09-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-201
  system:
    - SYS-320
    - SYS-342
    - SYS-365
    - SYS-366
    - SYS-578
  constraint:
    - CON-282
    - CON-288
    - CON-328
  information:
    - INF-119
    - INF-125
    - INF-371
  objective:
    - OBJ-207
  time:
    - TIM-003
---

# Game: Grand Theft Auto: San Andreas

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). CJ, Grove Street,
Sweet, Ryder, Big Smoke, the Ballas, BMX, Johnson House and the exact Los
Santos streets are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: original North American English PlayStation 2 black-label
  retail release, serial `SLUS-20946`, executable version `1.03`, on a fresh New
  Game with default controls. It is not version `3.00`, Greatest Hits, Special
  Edition, The Trilogy, a later console/mobile/PC port, Definitive Edition,
  modification, cheat or save from a later mission.
- Structured analysis target: the opening playable sequence from first ordinary
  CJ control after the C.R.A.S.H. police drop-off in Rollin' Heights through
  completion of `Sweet & Kendl`, Johnson House becoming usable and first
  ordinary control on Grove Street before entering the next `Ryder` mission.
- Entry: CJ is on foot with fresh opening state, no bicycle skill earned in
  this save, no mission completed and the radar points toward the family home.
- Fixed reproducible route: walk to the nearby BMX; mount it; pedal through the
  authored route to Grove Street and enter the red marker; accept `Big Smoke`
  and its automatic ride to the cemetery; begin `Sweet & Kendl`; after the
  Ballas destroy Big Smoke's car, mount the supplied bicycle; follow Sweet
  through the first moving route; after the group splits, follow Ryder through
  the second moving route; reach the Grove Street marker; accept mission
  completion, Respect gain, the `Ryder` successor and Johnson House safehouse;
  stop at first ordinary control without entering another mission.
- Primary decision loop: read the radar, world markers, current health, bicycle
  state, leader position and traffic; alternate direct on-foot movement with
  direct pedal/steer/brake bicycle control; keep the currently named leader
  close enough to advance; react to vehicles, Ballas pressure and collisions;
  cross the next authored marker while preserving health and bicycle access.
- Bounded wanted-state control: on a duplicate fresh opening before entering
  Grove Street, provoke one ordinary observed offence, record the displayed
  wanted-star tier, leave direct police perception without committing another
  offence and stop when the low wanted level clears. This control establishes
  the ordinary open-city law loop but does not alter the accepted mission run.
- Positive terminal: `Sweet & Kendl` has settled, Respect is awarded, Johnson
  House is usable, `Ryder` is unlocked and ordinary CJ control is restored on
  Grove Street. Reaching the house before the cemetery, merely mounting a BMX,
  reaching Sweet, reaching Ryder or viewing the final cutscene alone is not the
  retained terminal.
- Failure paths: health reaching zero produces `Wasted` and ends the current
  mission attempt; arrest produces `Busted`; losing bicycle access or failing
  the live route requires recovery/restart rather than success. The bounded
  wanted control succeeds only if sight is broken and the star clears; renewed
  police perception resumes pursuit.
- Included: direct foot movement; bicycle entry, pedalling, steering, braking
  and dismount; collision/ejection consequences; activity-earned Cycling
  progress; ambient traffic and pedestrians; one continuous health pool;
  low-tier observed crime, police pursuit/search and clearance; HUD health,
  radar, mission marker and wanted stars; ordered `Big Smoke` / `Sweet & Kendl`
  gates; two consecutive moving-leader stages; Respect/safehouse/successor
  settlement.
- Reproducible parameterisation: exact street line, pedal cadence, traffic,
  police position, incidental collisions, health remaining, Cycling progress
  and leader spacing may vary. The BMX acquisition, Grove Street marker,
  cemetery transition, Sweet-then-Ryder order, final marker and retained
  unlocks do not.
- Excluded: optional combat, weapons, food, armour, shopping, clothing, money,
  manual saving inside Johnson House, side activities, tags, girlfriends,
  territory, later missions, other cities, other vehicle classes, full skill
  progression, six-star testing, Pay 'n' Spray, bribes, cheats, speedrun skips,
  exploits, 100% completion, multiplayer and every later release.
- Direct-play status: not conducted. No disc, image, console, emulator,
  controller trace, save, screenshot, video or audio was obtained or inspected.
  The official booklet, release records and independent written routes support
  a bounded source reconstruction rather than a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GSA-001` | The packet targets the original North American English PS2 black-label `SLUS-20946` executable version `1.03` | Confirmed | Corroborated | High | P1, R1, R2 |
| `GSA-002` | CJ is directly movable on foot and can mount, pedal, steer, brake and leave a bicycle | Confirmed | Direct | High | P1, S1 |
| `GSA-003` | Repeated bicycle use raises retained Cycling skill and changes declared bicycle performance | Confirmed | Corroborated | High | P1, S1 |
| `GSA-004` | Ordinary traffic and pedestrians continue through the authored city route and collisions can damage or eject CJ | Confirmed | Direct | High | P1 |
| `GSA-005` | Observed offences raise wanted stars into police pursuit; at low tiers, breaking perception and avoiding new crime allows the wanted level to clear | Confirmed | Corroborated | High | P1, S1 |
| `GSA-006` | The HUD exposes health, current wanted-star tier, radar position and the active authored destination or leader cue | Confirmed | Direct | High | P1, S1 |
| `GSA-007` | The opening route requires the Grove Street marker, automatic `Big Smoke` transition, then the `Sweet & Kendl` bicycle sequence in authored order | Observation | Corroborated | High | S1, S2, S3 |
| `GSA-008` | `Sweet & Kendl` requires mounting the supplied bicycle, following Sweet, then following Ryder and reaching the final Grove Street marker | Observation | Corroborated | High | S1, S2, S3 |
| `GSA-009` | Completion grants Respect, makes Johnson House usable and unlocks the `Ryder` mission | Observation | Corroborated | High | S2, S3 |
| `GSA-010` | Zero health or arrest ends the current attempt rather than satisfying the mission terminal | Confirmed | Corroborated | High | P1, S1 |
| `GSA-011` | The repository state model reconstructs the ordered bicycle route, skill gain, wanted search, health failure and retained unlocks without running the game | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Rockstar North / Rockstar Games, original North American
  PlayStation 2 release dated 26 October 2004.
- Platform or physical form: licensed English North American PlayStation 2 DVD,
  black-label/original edition, `SLUS-20946`, version `1.03`; no disc image or
  executable was acquired, hashed or executed.
- Puzzle family: spatial logic and topology; real-time system pressure; ordered
  dependency sequencing; agent routing and coordination.
- Primary sources, accessed 2026-09-22:
  - **[P1]** [Rockstar's English PlayStation 2 instruction
    booklet](https://media-rockstargames-com.akamaized.net/rockstargames-newsite/img/manuals/en_us/GTATrilogy_GTASA_PS2_Manual_M01.pdf),
    pp. 3–4, 7 and related HUD/rule pages, for on-foot, bicycle and vehicle
    controls, health, police/wanted, traffic, radar, statistics and hospital
    recovery rules. Preserved local SHA-256:
    `4965f59162a0c65952f9fd97b435979fa3c87e0458b14f9d076c4b8f9da625a4`.
  - **[P2]** [Rockstar's official San Andreas product
    page](https://www.rockstargames.com/games/SANANDREAS), used only for stable
    title, developer/publisher and original-product identity, not later-port
    mechanical parity.
- Reproducible sources:
  - **[R1]** [Redump's PlayStation 2 disc
    index](https://redump.org/discs/system/ps2/region/Am/sort/edition/), for the
    USA, English, original-edition `SLUS 20946` release identity.
  - **[R2]** [SerialStation's `SLUS-20946` disc
    record](https://serialstation.com/discs/5393349b-8e6e-4c53-be18-765dc7e47c49),
    for executable version `1.03` and the original serial.
  - **[S1]** [TwistidSoul's contemporary PlayStation 2 text
    guide](https://gamefaqs.gamespot.com/ps2/914983-grand-theft-auto-san-andreas/faqs/33175),
    for the first Rollin' Heights BMX, pedal controls, Cycling gain, wanted and
    health behaviour, `Big Smoke`, `Sweet & Kendl`, Sweet/Ryder route and
    mission reward.
  - **[S2]** [GTA Base's `Sweet & Kendl` mission
    record](https://www.gtabase.com/gta-san-andreas/missions/sweet-kendl), for
    main-story identity, moving-leader objectives, Respect and Johnson House.
  - **[S3]** [Grand Theft Wiki's `Sweet & Kendl`
    record](https://www.grandtheftwiki.com/Sweet_%26_Kendl), for chronological
    placement, Sweet/Ryder follow stages, Respect, Johnson House and `Ryder`
    unlock.
- Validation source: **[V1]**
  [`verify_grand_theft_auto_san_andreas_control.py`](../../../scripts/verify_grand_theft_auto_san_andreas_control.py),
  an executable source-model reconstruction of the bounded state relations. It
  does not execute Grand Theft Auto: San Andreas.
- Claim IDs: `GSA-001`–`GSA-011`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly walk/run CJ from the police drop-off to the BMX,
  into markers and through Grove Street after the mission.
- Existing `ACT-201`: enter the BMX's rider position, directly pedal, steer and
  brake it, and choose when to dismount.
- Claims: `GSA-002`, `GSA-007`, `GSA-008`.

### System Behaviour Genes

- Existing `SYS-320`: integrate bicycle steering, pedal acceleration, road
  contact, collisions and rider consequences.
- Existing `SYS-342`: eligible bicycle use adds Cycling progress and applies
  the corresponding performance modifiers.
- Existing `SYS-365`: route ordinary vehicles and pedestrians through the same
  streets and resolve their local collision/reaction state.
- Existing `SYS-366`: convert an observed offence into a bounded wanted tier,
  police pursuit and, after sight is broken, a search that can clear.
- Existing `SYS-578`: attacks, collisions and falls reduce CJ's one continuous
  health pool; zero closes the current attempt as `Wasted`.
- Claims: `GSA-003`–`GSA-005`, `GSA-010`.

### Constraint Genes

- Existing `CON-282`: the opening marker, `Big Smoke` transition, cemetery,
  Sweet follow stage, Ryder follow stage and final Grove Street marker must
  settle in authored order.
- Existing `CON-288`: BMX control requires accessible rider position, usable
  bicycle state, compatible geometry and safe enough mounting/dismounting.
- Existing `CON-328`: the ordinary low wanted level clears only after police
  perception is broken and remains clear of reacquisition/new offence for the
  required interval.
- Scarce route state: health, bicycle access, current leader, leader spacing,
  current marker, police perception and wanted-clear interval.
- Claims: `GSA-002`, `GSA-005`, `GSA-007`, `GSA-008`, `GSA-010`.

### Information Genes

- Existing `INF-119`: health and Cycling/stat state are visible before survival
  or movement decisions.
- Existing `INF-125`: radar, world markers and current mission instructions
  expose the authored destination/leader gate without automating bicycle input.
- New `INF-371`: filled wanted stars expose the current police-pressure tier;
  their changing/cleared state distinguishes active pursuit/search from
  restored ordinary travel without revealing future police positions.
- Claims: `GSA-003`, `GSA-005`, `GSA-006`, `GSA-008`.

### Objective Genes

- New `OBJ-207`: mount the supplied bicycle, follow Sweet and then Ryder through
  their consecutive authored routes, reach Grove Street and retain Respect,
  Johnson House availability and the `Ryder` successor mission.
- A first marker, one leader reached, cleared wanted level or final cutscene
  without settled unlocks is intermediate. `Wasted`, `Busted` or restart is not
  success.
- Claims: `GSA-007`–`GSA-010`.

### Time Genes

- Existing `TIM-003`: bicycle motion, leaders, Ballas pressure, traffic,
  collision, health, police pursuit/search and player input resolve on one
  shared real-time clock outside authored transitions and pause.
- Claims: `GSA-004`, `GSA-005`, `GSA-008`, `GSA-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| First Rollin' Heights control | walk to the nearby BMX and press Triangle | CJ enters the rider position and bicycle control replaces foot movement | vehicle handoff | `GSA-002` |
| CJ occupies the BMX | hold/tap X, steer and brake | pedal cadence and road contact advance the bike; eligible riding adds Cycling progress | direct motion plus retained skill | `GSA-002`, `GSA-003` |
| Traffic crosses the chosen line | steer or brake around it | vehicles/pedestrians continue independently; contact can change speed, position and health | shared city simulation | `GSA-004` |
| Police observe an eligible ordinary offence | remain in view | a visible wanted star activates matching police pursuit | law escalation | `GSA-005`, `GSA-006` |
| A low wanted tier is active | break police perception and commit no new offence | search time advances; reacquisition resumes pursuit, while a completed interval clears the star | evasion gate | `GSA-005` |
| Grove Street marker is reached before the cemetery | enter the red marker | `Big Smoke` begins and automatically carries the story to the cemetery | ordered opening gate | `GSA-007` |
| Big Smoke's car is destroyed | mount the supplied bicycle | `Follow Sweet` becomes the current moving-route instruction | first leader stage | `GSA-008` |
| Sweet reaches the authored split | remain with the group | the active instruction changes from Sweet to Ryder | ordered leader handoff | `GSA-008` |
| Ryder is followed to Grove Street | cross the final marker alive | mission settlement grants Respect, Johnson House and `Ryder`; ordinary control returns | scoped positive terminal | `GSA-009` |
| CJ's health reaches zero or arrest completes | accept failure | the current attempt ends as `Wasted` or `Busted`; no mission terminal is retained | negative control | `GSA-010` |

## Strategic and experiential structure

- Local decision: choose a line through traffic, vary pedal cadence, brake before
  contact, recover the leader after a turn and decide when breaking police sight
  is safer than continuing straight toward the next marker.
- Medium-term planning: preserve health and the supplied bicycle through two
  moving-leader segments whose route authority transfers from Sweet to Ryder.
- Long-term structure: the opening teaches that free movement, transport,
  ambient city systems and wanted pressure remain available around an authored
  mission spine whose completion changes the persistent home/mission state.
- Decision texture: the route marker gives destination and the leader gives a
  moving local reference, but neither steers the bicycle. Traffic and police can
  perturb the same line while Cycling progress slowly changes performance.
- Failure attribution: health, wanted stars, radar, current instruction and
  leader position distinguish collision/combat attrition, police escalation,
  route loss and successful authored progress.

## Replay and variation

- What changes between attempts: exact street line, pedal cadence, traffic,
  collisions, police contact, remaining health and Cycling gain may vary.
- Randomness or procedural generation: opening missions, markers, leader order
  and unlocks are authored; ambient traffic and local pursuit positioning vary.
- Multiple viable strategies: different lines and pacing can preserve the same
  leader chain; the accepted run need not provoke a wanted level because that
  law loop is isolated in a duplicate fresh control.
- Typical replay motive: cleaner lines, fewer collisions, closer leader spacing
  or faster completion. Later campaign optimisation is outside the packet.

## Adjacent systems and history

- Direct series relation: `GAME-0145` Grand Theft Auto V shares foot/vehicle
  authority, traffic, wanted escalation, health, authored missions and real
  time, but its packet adds three persistent protagonists, special abilities,
  heist planning and a terminal campaign branch absent from this opening.
- Similar games: `GAME-0214` Mafia (2002) shares direct road travel, traffic,
  police search and authored urban gates but adds tickets, arrest-state choices
  and five passenger deliveries. `GAME-0333` Sonic the Hedgehog shares
  continuous route control and health/failure pressure but has no open city,
  vehicle handoff, police search or moving-leader mission.
- Important difference: the scoped terminal is not arrival at a static point
  alone. It requires two successive moving references and settles into a newly
  usable home plus a successor story mission.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-201` | CJ, BMX, bindings, pedal cadence and camera are parameters |
| System Behaviour | `SYS-320`, `SYS-342`, `SYS-365`, `SYS-366`, `SYS-578` | handling, traffic, Cycling gain, stars, search duration and health values are parameters |
| Constraint | `CON-282`, `CON-288`, `CON-328` | marker order, rider state, leader spacing and police perception are parameters |
| Information | `INF-119`, `INF-125`, `INF-371` | HUD art, radar scale, markers and star rendering are presentation parameters |
| Objective | `OBJ-207` | leaders, route, Respect, safehouse and successor mission are parameters |
| Time | `TIM-003` | frame cadence and authored transition duration are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `356` (`GAME-0001`–`GAME-0356`).
- Exact genome matches: none.
- Tied near matches: `GAME-0214` — Mafia (2002) (`11 / 26 = 0.423077`).
- Supported combination subsets: none.
- Scan date: 2026-09-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0214` — Mafia (2002) | `ACT-008`, `ACT-201`, `SYS-320`, `SYS-365`, `SYS-366`, `CON-282`, `CON-288`, `CON-328`, `INF-119`, `INF-125`, `TIM-003` | Both packets join foot/vehicle authority, traffic, police pursuit/search, ordered urban gates, visible health/objectives and real time. San Andreas adds Cycling progression, continuous mission health, compact wanted stars and a Sweet-to-Ryder bicycle terminal that unlocks a home; Mafia adds speed-limiter input, passenger/fare settlement, typed citation-to-arrest law, checkpoint recovery and an unarmed alley escape. | Near, `11 / 26 = 0.423077` |

### Preserved research notes

- New genes: `INF-371` and `OBJ-207`.
- Classification result: new gene plus reused open-city, vehicle, skill,
  survival, mission-order and real-time boundaries.
- Evidence and reasoning: no lower-ID information gene isolates a compact
  wanted-star tier without requiring a calculated GPS route or Mafia's
  citation/arrest classes, and no objective joins consecutive moving-leader
  bicycle stages to the first persistent home/successor unlock.

## Taxonomy impact

- Registry changes: add `INF-371` and `OBJ-207`; add this game as evidence to
  `ACT-008`, `ACT-201`, `SYS-320`, `SYS-342`, `SYS-365`, `SYS-366`, `SYS-578`,
  `CON-282`, `CON-288`, `CON-328`, `INF-119`, `INF-125` and `TIM-003` without
  changing their causal boundaries.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_096`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_096.md).
- Candidate terms affected: none.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original booklet separates direct bicycle
  control, health/stat display and wanted-star law feedback while preserving
  continuous city traffic (`GSA-002`–`GSA-006`, `GSA-010`).
- [Observation | Corroborated | High] The opening story hands its moving route
  from Sweet to Ryder and settles only with Respect, Johnson House and `Ryder`
  retained (`GSA-007`–`GSA-009`).

## New genes

- [Observation | Corroborated | High] Add `INF-371` and `OBJ-207` under
  `TAXONOMY_CHANGE_096`.

## New combinations

- [Observation | Direct | High] No verified combination is registered from one
  new carrier.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_096` adds two separate
  boundaries and preserves every earlier signature and lifecycle state.

## Gene reuse and novelty notes

- Reused genes: `ACT-008`, `ACT-201`, `SYS-320`, `SYS-342`, `SYS-365`,
  `SYS-366`, `SYS-578`, `CON-282`, `CON-288`, `CON-328`, `INF-119`, `INF-125`
  and `TIM-003`.
- New genes: `INF-371` and `OBJ-207`.
- Generalised definitions: none. Existing vehicle, police, health, mission and
  information boundaries already admit the sourced carrier as parameterised.
- Rejected candidates: CJ, BMX, Sweet, Ryder, Grove Street, Respect, Johnson
  House, exact star count, traffic seed, marker colour, pedal cadence and route
  geometry are parameters; cutscene composition, music and dialogue are not
  genes; weapons, food, clothing, money and later cities are outside scope.
- Novelty conclusion: accept one compact wanted-tier information boundary and
  one two-leader opening terminal; reuse the established open-city substrate.

## Negative results

- `INF-144` is rejected: the original opening radar supplies a marker and local
  map, not the gene's calculated road route plus wanted-search surface.
- `INF-273` is rejected: San Andreas wanted stars do not expose Mafia's
  stoppable citation versus handcuff/arrest classes.
- `SYS-215` and weapon actions are rejected: the accepted bicycle escape does
  not require CJ to command an attack.
- `CON-330` is rejected: the sources establish following and marker order, but
  do not justify importing every GTA V critical-asset failure class.
- `SYS-369` is rejected: this packet does not establish a retained authored
  checkpoint restore distinct from restarting the early mission.

## Open questions

- Exact internal leader-distance thresholds, wanted-search seconds, Cycling
  increments, traffic seeds, collision damage and mission-script coordinates
  remain parameters because no executable or direct trace was inspected.
- A later bounded module could isolate food/body statistics, weapon skill,
  territory, vehicle schools or another city, but none is inferred here.

## Reproducibility notes

- Start only from the original English North American PS2 `SLUS-20946` version
  `1.03` New Game. Record edition/serial before applying route claims.
- Preserve the accepted run separately from the wanted-state control so police
  variance cannot silently change the story route.
- Stop after `Sweet & Kendl` settlement and first ordinary Grove Street control;
  do not enter Johnson House to save or start `Ryder`.
- Treat the repository verifier as a state-transition proof over cited rules,
  not an emulator, timing measurement or proof of original binary execution.

## Localisation review

- Ukrainian profile, scope, direct-play statement, presentation, two new gene
  definitions and all plain-language cards are reviewed in this same unit under
  [`UKRAINIAN_LOCALISATION_POLICY`](../../../docs/UKRAINIAN_LOCALISATION_POLICY.md).
- `verified`: Grand Theft Auto: San Andreas, Rockstar North, Rockstar Games,
  PlayStation 2, `SLUS-20946`, `1.03`, CJ, Sweet, Ryder, Big Smoke, Ballas, BMX,
  Grove Street, Johnson House, `Big Smoke`, `Sweet & Kendl`, `Ryder`, Respect,
  `Wasted` and `Busted` remain official names, literal labels or stable IDs.
- `corrected`: all explanatory Ukrainian prose is authored naturally and keeps
  action, prerequisite, result, failure and exclusion boundaries.
- `retained-with-reason`: remaining Latin-script terms are only the official
  entities and evidence-critical labels above; no generic English prose is
  deferred to a later batch.
