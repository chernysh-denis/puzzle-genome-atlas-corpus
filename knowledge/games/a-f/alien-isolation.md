---
game_id: GAME-0257
slug: alien-isolation
game_title: "Alien: Isolation"
analysis_status: reviewed
reviewed: 2026-09-05
combination_ids:
  - COMB-0255
gene_ids:
  action:
    - ACT-008
    - ACT-123
    - ACT-164
    - ACT-199
    - ACT-341
    - ACT-406
    - ACT-409
    - ACT-432
    - ACT-433
  system:
    - SYS-057
    - SYS-112
    - SYS-222
    - SYS-369
    - SYS-578
    - SYS-780
    - SYS-791
    - SYS-792
  constraint:
    - CON-210
    - CON-282
    - CON-296
    - CON-297
    - CON-601
    - CON-602
  information:
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-132
    - INF-311
  objective:
    - OBJ-155
  time:
    - TIM-003
    - TIM-007
---

# Game: Alien: Isolation

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `214490`, base package `51156`, public branch content Build ID `4940658`,
  built and published 2020-04-24; checked 2026-09-05. The later Steam metadata
  changenumber is not treated as a new executable build or publisher semantic
  version.
- Platform, input and difficulty: Windows, English interface, audio and
  subtitles installed, keyboard and mouse, base-game Story Mode, `Hard`. Sound
  is a documented game input/output rule, but no audio was played, heard or
  analysed for this record. macOS, Linux, consoles, controller input and other
  difficulties are separate packets.
- Entry: `Load Mission Save` for reached Mission 5, `The Quarantine`, from a
  fresh local Story Mode campaign whose retained mission-entry snapshot
  records the actual carried inventory and includes the earlier Noisemaker
  blueprint plus sufficient compatible components to craft one Noisemaker.
  Begin at first ordinary SciMed Tower control with `Go to Samuels and Taylor`
  active. Creating that declared snapshot is an entry precondition, not part
  of the admitted Mission 5 trace; exact carried quantities are run parameters.
- Primary decision loop: read the current objective, explored map and motion
  tracker; choose walking, crouching, sprinting, peeking, vents or a hiding
  place; search and collect finite components and batteries; craft one
  Noisemaker while world pressure continues; select and throw it toward a
  reachable point so the reactive hunter investigates a different route;
  manage tracker beeps, visibility, movement noise, flashlight charge, health
  and exposed save interactions; obtain the authored code and keycard, open
  their dependent route gates and reach the elevator to the successor mission.
- Positive terminal: use Morley's keycard at the Lower Hospital elevator,
  allow Mission 6, `The Outbreak`, to begin, retain first ordinary control with
  `Find a Trauma Kit` active, exit to the main menu and verify that `Load
  Mission Save` for Mission 6 restores its beginning. No movement or
  interaction after that restored first-control state is admitted.
- Negative terminal: lethal hostile contact or exhausted Health closes the
  current attempt and `Load Current Save` or `Load Previous Save` restores an
  authored save snapshot; this is recovery, not completion. Being detected,
  hiding successfully, crafting or throwing the Noisemaker, obtaining the
  passcode or keycard, reaching the elevator or entering Mission 6 without the
  exit/reload check is not positive settlement.
- Included: direct embodied traversal, crouch, sprint, vent and peek choices;
  authored doors, terminals, access-tuner interaction, searches, pickups,
  passcode and keycard gates; map/objective state; local sight and documented
  spatial sound; motion-only portable sensing with directional and distance
  feedback; authored hiding places and close breath/lean response; one
  blueprint-and-component Noisemaker craft and one non-damaging thrown
  diversion; finite component inventory; flashlight toggle, charge drain and
  battery refill; Health, lethal failure, designated save stations, save
  exposure/cooldown, checkpoint restoration and retained mission handoff.
- Excluded: Survivor Mode, Crew Expendable, Last Survivor and every other DLC;
  macOS/Linux port-launcher behaviour, every console release, all other
  difficulty or input packets; all Mission 6 play after the retained terminal
  and every earlier/later campaign mission; combat, Revolver or other weapon
  firing, ammunition, damaging devices, melee, hostile killing, synthetic or
  human combat, medical-item recovery, exhaustive crafting and blueprint
  collection, optional logs and collectibles, achievements, challenge scores,
  secrets, speedrun skips, mods, cheats, debug tools, sequel or franchise
  unions; screenshots, official artwork, third-party assets, video and audio.
- Reproducible parameterisation: install Steam app `214490` from package
  `51156`, select English, keyboard/mouse and Hard, then create the declared
  fresh-campaign Mission 5 snapshot while recording its incoming inventory.
  Reload `The Quarantine`; follow only the current objective chain; use the
  motion tracker against moving local actors, enter and leave at least one
  authored hiding place, drain and refill some flashlight charge, use one ready
  save station and observe that saving consumes live exposed time, craft one
  Noisemaker from the retained blueprint and compatible components, throw it
  to divert the hunter after the quarantine alarm, obtain the authored code
  and Morley keycard and perform the stated Mission 6 reload terminal. Exact
  walking line, hiding place, tracker readings, stimulus point, hunter route,
  damage, collected resources, save station and elapsed time remain parameters.
- Potential scoped modules: one fresh full-campaign route; one Survivor Mode
  map; one named DLC mission; one bounded combat or synthetic encounter; one
  alternative difficulty; or one named non-Windows release each requires its
  own entry, loop, terminal and evidence review.
- Direct-play status: not conducted. Valve application/package data and the
  Steam product page establish lawful availability and exact base-product
  separation. The publisher-linked Feral manual establishes Story/Survivor
  separation, difficulty, controls, HUD, map, tracker, hiding, crafting,
  flashlight and save semantics. Three static written routes establish the
  exact Mission 5 transitions and Mission 6 boundary. This is an evidence-
  backed rules reconstruction, not a claimed captured playthrough or
  entitlement. No video or audio was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `AI-001` | The lawfully available selected product is current English Windows Steam app `214490` from one-app base package `51156`, not its DLC or Collection bundle | Confirmed | Direct | High | P1–P3 |
| `AI-002` | Public content Build `4940658` is the observed Windows distribution boundary; later store metadata does not establish a different executable build | Observation | Corroborated | High | S1 |
| `AI-003` | Story Mode and Survivor Mode are separate, and this packet fixes Story Mode, Hard and keyboard/mouse control | Confirmed | Direct | High | P3 |
| `AI-004` | The motion tracker reports nearby moving actors through bounded directional sectors and nearest-movement distance, while stationary actors cease to be reported | Confirmed | Direct | High | P3 |
| `AI-005` | Tracker signalling, running, equipment and impacts can create local stimuli that the reactive hunter perceives, while crouching, occlusion and hiding reduce exposure without granting invisibility | Confirmed | Direct | High | P2, P3 |
| `AI-006` | The hunter uses local senses, changes its current route in response to player movement or an explicit decoy and can abandon the diversion under its live search state | Confirmed | Direct | High | P1–P3 |
| `AI-007` | A reachable hiding place temporarily replaces free traversal; close hunter inspection admits a held-breath and lean-back response rather than guaranteed safety | Confirmed | Direct | High | P3 |
| `AI-008` | A known personal recipe requires its displayed components; crafting remains exposed to the advancing world, and a selected crafted Noisemaker can be thrown as a non-damaging diversion | Confirmed | Direct | High | P2, P3 |
| `AI-009` | The flashlight is manually toggled, drains a separate charge and consumes one carried battery to refill that charge | Confirmed | Direct | High | P3 |
| `AI-010` | The explored map, objective and authored fixture symbols expose only discovered route state, while pickups and crafting surfaces expose current item, component and capacity state | Confirmed | Direct | High | P3 |
| `AI-011` | Saving is limited to designated stations, requires live exposed interaction time and cannot be repeated at the same station until its cooldown clears | Confirmed | Direct | High | P3 |
| `AI-012` | Mission 5 requires the authored office terminal/passcode route, quarantine alarm, Morley search and keycard before the Lower Hospital elevator admits Mission 6 | Observation | Corroborated | High | S2–S4 |
| `AI-013` | Current, previous and mission saves restore authored snapshots; reaching Mission 6 creates a selectable Mission 6 start that makes the positive terminal reproducible | Confirmed | Corroborated | High | P3, S2–S4 |
| `AI-014` | The bounded identity is partial motion sensing whose self-revealing signal, finite light/crafting resources and live save exposure feed one reactive-hunter evasion route into retained successor control | Strong Pattern | Corroborated | High | `AI-004`–`AI-013` |

## Basic data

- Release / origin: Creative Assembly; SEGA; original Windows release
  2014-10-06 on the current Steam record. Feral Interactive supplies the
  publisher-linked current web manual used only for shared game rules and
  keyboard semantics, not Windows installation or port-specific behaviour.
- Platform or physical form: lawfully offered English Windows single-player
  Steam application `214490`; one retained Hard Story Mode mission packet.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-05:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=214490&cc=ua&l=english),
    for exact title/application, Windows and English support, single-player and
    Steam Cloud categories, developer/publisher, package relation, DLC list,
    current Ukraine offer and official reactive-hunter/resource description.
  - **[P2]** [current Steam product page](https://store.steampowered.com/app/214490/Alien_Isolation/?l=english),
    for current base-game identity, lawful Windows offer, Story premise,
    scavenging, hacking, crafting, evasion, distraction, reactive hunter and
    the separately sold Collection and seven DLC items.
  - **[P3]** [publisher-linked Alien: Isolation web manual](https://www.feralinteractive.com/en/manuals/alienisolation/latest/steam/),
    for Story/Survivor separation, difficulty, default keyboard/mouse controls,
    HUD, explored map and objective symbols, designated saving and cooldown,
    current/previous/mission saves, crouch/noise/peek/hiding rules, tracker
    motion/direction/distance and signalling risk, flashlight batteries,
    blueprint/component crafting and the non-pausing radial interface. Its
    macOS launcher and path instructions are not imported into this packet.
  - **[P4]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=51156&cc=ua&l=english),
    for package `51156` containing only app `214490`, its Windows/macOS/Linux
    platforms and current Ukraine offer.
- Corroborating textual sources, accessed 2026-09-05:
  - **[S1]** [SteamDB public depots](https://steamdb.info/app/214490/depots/),
    for public Build `4940658`, the 2020-04-24 build/public timestamp and
    Windows English base-game depot observation. SteamDB is not treated as the
    publisher, and its later metadata changenumber is not imported as a build.
  - **[S2]** [GameFAQs static campaign route](https://gamefaqs.gamespot.com/xboxone/751153-alien-isolation/faqs/70566),
    for the Mission 5 entry/objective, office access, code, save station,
    quarantine alarm, hunter release, authored hiding and distraction options,
    room identification, keycard acquisition, elevator and Mission 6 handoff.
    Controller glyphs, narrative interpretation and later play are excluded.
  - **[S3]** [GosuNoob static Mission 5 route](https://www.gosunoob.com/alien-isolation/the-quarantine-mission-5/),
    for independent textual corroboration of the office passcode, save station,
    hunter search, room search, Morley keycard and elevator sequence.
  - **[S4]** [Portforward static Mission 5 route](https://portforward.com/games/walkthroughs/Alien-Isolation/The-Quarantine.htm),
    for independent textual corroboration of the mapped office, passcode,
    saving, search region, keycard and Mission 6 transition. Images and embedded
    media were not opened or used.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P4` and `S1`–`S4` under the declared app, build, platform, difficulty,
  snapshot, exclusions and reload terminal; rules reasoning, not direct play.
- Claim IDs: `AI-001`–`AI-014`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly walk, crouch, sprint, peek and traverse vents
  through the authored hospital geometry; `ACT-341`: use the access tuner,
  terminals, save station, passcode/keycard fixtures and elevator; `ACT-199`:
  collect compatible components, batteries and route items; `ACT-164`: select
  the crafted Noisemaker from the radial carried-item interface.
- Existing `ACT-123`: select the known Noisemaker recipe and commit its output
  from compatible carried components; `ACT-406`: aim and throw that non-
  damaging carried diversion toward a reachable world point; wording-
  generalised `ACT-409`: toggle a finite-charge personal flashlight whose
  refill behaviour is supplied separately by `SYS-791` and `CON-601`.
- New `ACT-432`: raise or lower a portable local-motion sensor while retaining
  direct locomotion; new `ACT-433`: enter, remain attached to and deliberately
  leave one reachable authored hiding place.
- Product, mission, room, tool, item, actor, code and exact quantity names
  remain game-scoped parameters. Claims: `AI-004`–`AI-012`.

### System Behaviour Genes

- Wording-generalised `SYS-057`: an autonomous hostile replaces its current
  search or patrol route when it perceives the actor or explicit thrown
  stimulus, pursues or investigates that target and later abandons it under
  the live memory/distraction rule; `SYS-112`: accepted code, keycard or tuner
  interaction changes its dependent fixture and route state.
- Existing `SYS-222`: eligible visible items enter compatible carried stock up
  to capacity; `SYS-578`: contact or attack damage reduces continuous Health
  and zero Health ends the current attempt; `SYS-369`: retry restores an
  authored current or previous save snapshot rather than failed transient
  positions.
- Wording-generalised `SYS-780`: completing the required Mission 5 chain
  settles its objective/save boundary and admits retained Mission 6 control.
- New `SYS-791`: active portable illumination drains its internal charge and a
  legal refill consumes one finite carried battery; new `SYS-792`: the raised
  sensor samples eligible moving actors, selects the nearest reading and
  converts its relative position into direction-sector and distance feedback,
  dropping stationary actors from that channel.
- Resolution order: objective/map exposes the next gate; navigation or
  interaction changes reach, inventory and authored flags; sensor and local
  sight/sound expose only current cues; light, movement, tracker signal or the
  thrown decoy becomes perception input; the hunter pursues or diverts;
  crafting, battery use and save interaction remain exposed to live time;
  passcode and keycard open the ordered route; the elevator settles the mission
  and writes the successor save boundary.
- Claims: `AI-004`–`AI-014`.

### Constraint Genes

- Existing `CON-210`: carried component and item stacks obey compatible finite
  inventory capacity; `CON-282`: office access, code discovery, alarm, Morley
  search, keycard and elevator require their authored predecessor states;
  `CON-296`: secured doors and elevator accept only the matching current code,
  keycard or authorised state.
- Wording-generalised `CON-297`: one personal craft is legal only while its
  blueprint is known, every compatible component is carried and output
  capacity exists; this instance requires no station.
- New `CON-601`: personal portable illumination is available only with positive
  internal charge, and a refill requires one finite compatible carried battery;
  new `CON-602`: an authored save is legal only at a ready designated fixture,
  requires completion while world time and exposure continue and cannot repeat
  at that fixture until cooldown clears.
- Scarce strategic resources: Health, safe distance, occlusion, quiet time,
  tracker exposure, flashlight charge, carried batteries, component capacity,
  one craftable Noisemaker, save-station readiness and the current retained
  snapshot. Exact counts, radii and durations are parameters.
- Claims: `AI-004`–`AI-013`.

### Information Genes

- Existing `INF-115`: avatar-centred current sight and documented spatial sound
  expose only local actor/action state; `INF-119`: Health, flashlight battery
  and current equipment/resource state remain visible; `INF-125`: explored map,
  current position, authored symbols and objective expose the next known route
  without revealing unexplored rooms.
- Existing `INF-128`: pickups and carried inventory expose item identity,
  compatible stack and remaining capacity; `INF-132`: known recipes expose
  required components and current craftability.
- New `INF-311`: the raised portable sensor exposes bounded direction sectors
  and nearest eligible moving-actor distance while withholding identity,
  stationary actors, exact route and future position. Its documented emitted
  signal remains a hostile-perception input rather than safe omniscience.
- Claims: `AI-004`, `AI-005`, `AI-008`–`AI-012`.

### Objective Genes

- Wording-generalised `OBJ-155`: survive and complete one ordered authored
  survival-action segment through its explicit mission/save boundary and
  retain ordinary control in the immediate successor segment.
- Success, evaluation and failure: success requires the Mission 6 first-control
  state plus mission-save reload; death/checkpoint recovery, detection,
  distraction, crafting, passcode/keycard acquisition or reaching the elevator
  remain intermediate. Combat, collection and later-story outcomes are not
  objectives.
- Claims: `AI-011`–`AI-014`.

### Time Genes

- Existing `TIM-003`: hunter movement, perception, pursuit, damage, crafting
  exposure, tracker sound and save-station interaction advance in real time
  while the player retains eligible input.
- Existing `TIM-007`: current, previous and mission saves retain prior authored
  world states that can be restored and continued through a different movement,
  distraction, resource or save sequence; this does not claim an in-world
  rewind command.
- Claims: `AI-005`–`AI-013`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| The declared Hard Mission 5 snapshot exists | Load `The Quarantine` Mission Save and accept first SciMed control | The campaign restores its recorded incoming inventory and `Go to Samuels and Taylor` objective without importing later progress | fixed retained entry | `AI-001`–`AI-003`, `AI-013` |
| An eligible local actor is moving within tracker range | Raise the motion tracker, then let that actor stop | Direction and nearest-movement distance appear while eligible movement persists and clear when no eligible motion remains | motion-only partial information | `AI-004` |
| Positive flashlight charge remains in a dark route | Toggle the flashlight on, observe charge drain, toggle off and perform one legal battery refill | Local illumination exists only while active charge remains; refill consumes one carried battery | finite information resource | `AI-009` |
| A reachable authored hiding place is available | Enter it, remain concealed and leave when the route is safer | Free traversal is replaced by attached hiding state; close inspection may require held breath and lean without guaranteeing safety | conditional embodied concealment | `AI-005`, `AI-007` |
| The Noisemaker blueprint, compatible components and capacity are present | Open the radial crafting surface, commit every required component and craft one copy | Components leave carried stock, the Noisemaker enters compatible inventory and world pressure does not pause | exposed personal crafting | `AI-008`, `AI-010` |
| The quarantine alarm has released the hunter and a reachable diversion point exists | Select and throw the Noisemaker away from the intended route | Its non-damaging local stimulus can replace the hunter's current search route with investigation of the landing region | explicit decoy reroutes autonomous pressure | `AI-005`, `AI-006`, `AI-008` |
| One designated station is ready while the hunter remains active | Hold the save interaction until it completes | Current state is retained only after live exposed time; immediate reuse is unavailable until cooldown | vulnerable manual persistence | `AI-011` |
| The required office terminal is accessible | Read its fixed code and apply that authority to the secured route | The matching authored seal opens while an incorrect or absent credential cannot provide access | information-to-fixture gate | `AI-010`, `AI-012` |
| Morley's room is identified and reachable | Search the authored body and collect its keycard | The exact route item enters inventory and supplies authority for the Lower Hospital elevator | finite keycard dependency | `AI-010`, `AI-012` |
| Health reaches zero before the elevator transition | Accept `Load Current Save` or `Load Previous Save` | Failed transient position, hunter and resource state are replaced by an authored saved snapshot | reproducible negative recovery | `AI-013` |
| Morley's keycard is carried at the Lower Hospital elevator | Use the keycard and enter the elevator | Mission 5 closes and Mission 6 begins with `Find a Trauma Kit` at first ordinary control | explicit successor transition | `AI-012`, `AI-013` |
| First Mission 6 control has been retained | Exit to main menu and load Mission 6 Mission Save | The beginning of Mission 6 is restored; stop before any subsequent movement or interaction | reproducible positive terminal | `AI-013`, `AI-014` |

## Strategic and experiential structure

- Planning horizon: the explored map and objective identify authored gates,
  but local hunter position remains partial. Tracker use narrows that uncertainty
  only for movement while its signal can worsen the same perception problem.
- Local tactics: choose crouched occluded movement over noisy speed, raise the
  tracker briefly rather than continuously, use flashlight charge only where
  it creates enough route information, keep one hiding option and place the
  crafted stimulus away from the intended exit.
- Medium-term structure: convert scarce components into one explicit diversion,
  preserve battery and Health, use exposed save opportunities when current
  search pressure permits and carry the fixed code/keycard discoveries through
  the hospital's ordered access chain.
- Reversible versus irreversible: route, hiding and tracker timing vary live;
  a thrown device, battery refill and crafting inputs spend finite stock;
  checkpoint load replaces failed transient state; the elevator and Mission 6
  mission-save boundary retain authored progress.
- Failure attribution: Health, tracker, inventory, crafting requirements,
  objective, map and save-station feedback distinguish missing authority or
  resources from a perception error, unsafe interaction window or lethal
  route. The hunter's future path remains intentionally uncertain.
- Player trust: moving-only tracker readings and local sensory cues disclose
  the basis of immediate risk without claiming exact omniscience; a completed
  save and successor mission label make retention externally testable.
- Claim IDs: `AI-004`–`AI-014`.

## Replay and variation

- What changes between attempts: hunter location and search path, tracker
  readings, stimulus response, movement line, hiding timing, damage, pickups,
  crafted-component allocation, flashlight use, save timing and elapsed time.
- Randomness or procedural generation: hospital topology, passcode, keycard and
  mission order are authored; the reactive hunter and resource route create
  bounded live variation rather than a generated world.
- Multiple viable strategies: restrained tracker use, light use, hiding and
  one crafted diversion can be sequenced differently around the same mandatory
  gates; combat routes and additional crafted devices are outside this packet.
- Typical replay motive: refine low-exposure routing and scarce-resource timing
  against a hunter whose current response is not reduced to a fixed patrol.
- Claims: `AI-004`–`AI-013`.

## Adjacent systems and history

- Resident Evil 4 (2023) shares embodied authored traversal, finite inventory,
  health, contextual interaction, checkpoint recovery and retained successor
  control, but its first chapter centres weapon pressure and combat settlement
  rather than motion-only observation and reactive-hunter evasion.
- Project Zomboid shares local sight/sound, noise-driven hostile routing,
  inventory, crafting and vulnerable real time, but expands them into a seeded
  persistent survival history with bodily conditions and permanent death.
- Dishonored shares authored stealth gates, partial local perception and
  checkpoint recovery, but adds supernatural relocation, target disposition
  and conduct evaluation while this packet adds portable movement sensing,
  hiding, finite light and decoy-driven hunter search.
- Dead by Daylight shares hiding-and-pursuit pressure and partial threat
  information, but its pursuer is another human in a 4v1 match and its
  Generator/Hook/Gate economy is absent here.
- Claims: `AI-004`–`AI-014`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-123`, `ACT-164`, `ACT-199`, `ACT-341`, `ACT-406`, `ACT-409`, `ACT-432`, `ACT-433` | mission, tool, item, hiding-place and input identities are parameters |
| System Behaviour | `SYS-057`, `SYS-112`, `SYS-222`, `SYS-369`, `SYS-578`, `SYS-780`, `SYS-791`, `SYS-792` | hunter route, stimulus, sensor range, charge and checkpoint values are parameters |
| Constraint | `CON-210`, `CON-282`, `CON-296`, `CON-297`, `CON-601`, `CON-602` | code, keycard, component, capacity and cooldown values are parameters |
| Information | `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-132`, `INF-311` | HUD art, tracker sectors and distance presentation are parameters |
| Objective | `OBJ-155` | mission names and exact save slot are parameters |
| Time | `TIM-003`, `TIM-007` | frame rate and save-load duration are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `256` (`GAME-0001`–`GAME-0256`).
- Exact genome matches: none.
- Tied near matches: `GAME-0231` — Fallout 4 (`11 / 43 = 0.255814`).
- Supported combination subsets: `COMB-0255`.
- Scan date: 2026-09-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0231` — Fallout 4 | `ACT-008`, `ACT-199`, `ACT-341`, `SYS-369`, `CON-282`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `TIM-003`, `TIM-007` | Fallout 4's reviewed Vault route adds a fixed character-stat allocation, direct weapon combat, staged tutorial guidance and a retained open-world exterior. Alien: Isolation instead adds moving-only portable sensing, authored hiding, decoy-driven autonomous pursuit, finite-battery light, exposed crafting and cooldown-gated live saving before the retained successor mission. | Near, `0.255814` |

### Preserved research notes

- New genes: `ACT-432`, `ACT-433`, `SYS-791`, `SYS-792`, `CON-601`,
  `CON-602` and `INF-311`.
- Reused genes: `ACT-008`, `ACT-123`, `ACT-164`, `ACT-199`, `ACT-341`,
  `ACT-406`, `ACT-409`, `SYS-057`, `SYS-112`, `SYS-222`, `SYS-369`,
  `SYS-578`, `SYS-780`, `CON-210`, `CON-282`, `CON-296`, `CON-297`,
  `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-132`, `OBJ-155`,
  `TIM-003` and `TIM-007`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: existing navigation, personal crafting, inventory,
  distraction, perception, health, access, ordered mission and persistence
  boundaries fit after narrow wording generalisation where noted. New atoms
  are limited to portable motion-sensor use and feedback, authored hiding-
  place occupancy, finite-battery illumination and exposed cooldown-gated save
  stations. No room, mission, character, device, code or quantity enters a
  canonical label.

## Taxonomy impact

- Registry changes: add seven bounded Active genes and `COMB-0255`; add
  independent evidence to fitting reused genes. Wording-generalise `ACT-409`,
  `SYS-057`, `SYS-780`, `CON-297` and `OBJ-155` only enough to admit the same
  portable boundary with this game's refill, autonomous-hunter, no-station
  craft and mission terminology. Every earlier signature and lifecycle state
  remains unchanged.
- Taxonomy-change record: none; the generalisations do not split, merge,
  deprecate or change any earlier game's signature.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; Alien,
  `The Quarantine`, SciMed, Samuels, Taylor, Kuhlman, Morley, Noisemaker,
  access tuner, motion tracker, passcode `1702`, keycard, elevator, `Hard`, app,
  package and build identifiers remain parameters or evidence tokens.

## Negative results

- No video or audio evidence was needed. Static primary text establishes the
  portable mechanics, and independent written routes establish mission order.
- `SYS-373` is rejected: the scoped hunter changes search/pursuit from
  perception and decoy stimuli under `SYS-057`, not a conventional suspicion
  meter that necessarily escalates into ordinary combat.
- `SYS-754` is rejected: this flashlight does not automatically recharge while
  inactive; a refill consumes finite carried battery stock.
- `CON-077` and `CON-305` are rejected: one is sight-only and one remains the
  Project Zomboid zombie/route gate. This packet needs neither to restate the
  already admitted multi-stimulus autonomous diversion boundary.
- Weapons, attacks and hostile clearance are excluded rather than inferred
  from items carried in the entry snapshot. The terminal is route escape and
  retained successor control, not killing the hunter or every local actor.

## Delta summary

## New facts

- [Confirmed/Observation | Direct/Corroborated | High] `AI-001`–`AI-014`:
  one fixed hospital mission couples moving-only sensor information, a self-
  revealing signal, finite light/crafting resources, hiding and deliberate
  distraction to a reactive autonomous hunter and retained mission handoff.

## New genes

- [Observation | Direct/Corroborated | High] Added `ACT-432`, `ACT-433`,
  `SYS-791`, `SYS-792`, `CON-601`, `CON-602` and `INF-311`.

## New combinations

- [Confirmed | Corroborated | High] `COMB-0255` — motion-only local sensing and
  finite preparation feed a reactive-hunter evasion route through vulnerable
  saving into retained successor control.

## Taxonomy changes

- [Observation | Direct/Corroborated | High] Seven portable genes are added.
  `ACT-409`, `SYS-057`, `SYS-780`, `CON-297` and `OBJ-155` receive only
  boundary-preserving wording and independent support; no earlier signature or
  lifecycle state changes.

## New questions

- Does Prey (2017)'s bounded opening reuse the same first-person inventory,
  perception and retained-segment skeleton while replacing a persistent hunter
  with station exploration, object mimicry and ability acquisition?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0258` — Prey (2017).
- Optimisation criterion: preserve one bounded authored first-person survival
  packet while changing its information ambiguity, route tools and hostile
  structure.
- Expected information gain: distinguish motion-only threat sensing and live
  hiding from object-identity uncertainty and station-route capability gates.
- Backlog impact: advances the approved batch-014 ordered horizon.

## Why this game

- [Hypothesis | Limited | High] Prey keeps embodied scarcity and spatial
  uncertainty but moves the central inference from where a moving hunter is to
  which apparently ordinary objects and routes are currently safe or usable.
