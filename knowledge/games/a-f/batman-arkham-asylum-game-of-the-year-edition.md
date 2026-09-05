---
game_id: GAME-0255
slug: batman-arkham-asylum-game-of-the-year-edition
game_title: "Batman: Arkham Asylum Game of the Year Edition"
analysis_status: reviewed
reviewed: 2026-09-05
combination_ids:
  - COMB-0253
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-235
    - ACT-341
    - ACT-370
    - ACT-419
    - ACT-429
    - ACT-430
  system:
    - SYS-112
    - SYS-215
    - SYS-369
    - SYS-373
    - SYS-578
    - SYS-680
    - SYS-749
    - SYS-779
    - SYS-789
  constraint:
    - CON-077
    - CON-282
    - CON-335
    - CON-402
    - CON-589
    - CON-599
  information:
    - INF-115
    - INF-119
    - INF-125
    - INF-268
    - INF-295
    - INF-298
    - INF-309
    - INF-310
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Batman: Arkham Asylum Game of the Year Edition

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `35140`, sold through standalone package `4109`, public Windows Build ID
  `597963`, built and published 2015-04-22, checked 2026-09-05. The build and
  timestamp are secondary distribution observations, not an invented
  publisher semantic version. The current product title is exactly `Batman:
  Arkham Asylum Game of the Year Edition`.
- Platform, input and difficulty: Windows, English interface and subtitles,
  keyboard and mouse, fresh local profile, `Story Mode`, `New Game`, `Normal`
  difficulty and default gameplay/camera options. Controller, console,
  alternate difficulty and Challenge Mode define different packets.
- Entry: after the fresh-story opening finishes, retain the first ordinary
  controlled escort state inside Intensive Treatment, before the Joker escape
  and first mandatory unarmed inmate group. No earlier cinematic or menu input
  belongs to the admitted decision trace.
- Primary decision loop: follow the current authored objective and map through
  the facility; directly run, crouch, climb, glide, use vents and grapple to
  eligible elevated anchors; in unarmed encounters choose strikes, prompted
  counters, cape stuns, evades, knockdowns and ground finishers while
  preserving an uninterrupted FreeFlow chain; use Detective Mode to classify
  occluded actors, equipment and highlighted evidence; rescue required actors
  and remotely strike the decontamination control with the Batarang; survive
  the required charging Titan pressure; inspect the mandatory evidence and
  follow its forensic trail; use vantage points, sightline breaks, glide kicks
  and silent takedowns against the first armed predator group; complete the
  mandatory portrait scan and leave through the utility route.
- Positive terminal: exit Intensive Treatment, grapple to the island surface,
  allow `Escape from Intensive Treatment to the island surface` to complete
  and `Protect the Batmobile` to become current, wait for the authored
  checkpoint save, then quit and select the same profile with `Continue`.
  Success requires ordinary retained control in Arkham Island East with the
  successor objective active; do not advance toward the Batmobile.
- Negative terminal: health loss and ordinary retry restore the latest
  authored checkpoint without completing the bounded route. A failed hostage
  or decontamination intervention follows its available authored recovery.
  Clearing one fight, seeing one autosave, defeating the Titan, finding the
  forensic trail, clearing the predator room or merely stepping outside before
  the successor/checkpoint/reload test is not positive settlement.
- Included: direct on-foot traversal; running, crouching, climbing, gliding and
  vent use; permanent grapnel traversal only to eligible highlighted elevated
  anchors; local hostile sight and alert; the first taught unarmed FreeFlow
  encounters; strikes, prompted counters, cape stuns, evasion, knockdown,
  ground takedown and end-encounter experience/health restoration; Detective
  Mode actor, threat and evidence classification; required rescue and authored
  interactions; the initial Batarang as a reusable typed tool; the
  decontamination control/fan dependency; the required charging Titan survival
  encounter; mandatory forensic evidence and trail following; the first armed
  predator room, including its finite reinforcement and clearance gate;
  gargoyle/vantage, glide-kick and silent-takedown routes; the mandatory
  portrait scan; objective/map/tutorial surfaces; checkpoint retry and the
  retained exterior successor-objective test.
- Excluded: all four extra GOTY Challenge Maps, Challenge Mode, scores,
  medals and leaderboards; every later base-story objective, room, boss and
  island route; the Batmobile interaction, Explosive Gel and every later
  gadget or upgrade; WayneTech spending, exact combo maximisation, optional
  Riddler challenges, trophies, interview tapes, collectibles and secrets;
  every other Arkham game, DLC/content union, console/controller/macOS/Linux,
  another difficulty or build, mods, trainers, debug commands and speedrun
  skips; screenshots, official art, third-party assets, video and audio.
- Reproducible parameterisation: install the stated Windows package, select
  English text, keyboard/mouse, a fresh profile, Story Mode, New Game and
  Normal. From first escort control, follow only the current main objective;
  clear mandatory unarmed groups with at least one prompted counter and ground
  takedown; reach the first hostage; grapple, glide and complete the required
  takedown; rescue every required decontamination actor and strike the control;
  survive the Titan using evasion and a compatible Batarang response; inspect
  the required evidence and follow its trail; clear the armed room with at
  least one silent takedown from a legal unaware/reachable state; perform the
  mandatory portrait scan, speak to the required guard, leave through the
  utility route and perform the declared checkpoint/Continue terminal test.
  Leave the first WayneTech point unspent. Exact route, aim, hostile order,
  attack rhythm, combo value, damage and checkpoint timing remain parameters.
- Potential scoped modules: one later named Story Mode objective, one declared
  Challenge Map with its scoring rules, one alternative difficulty or one
  non-Windows release each requires its own entry, primary loop, terminal and
  evidence review.
- Direct-play status: not conducted. Current Valve application/package data,
  the Steam product page and its publisher-supplied PC manual establish lawful
  availability, exact product/mode boundaries, controls, difficulty,
  checkpoints, FreeFlow, Detective Mode, grapnel, Batarang, map and experience
  rules. Independent static written walkthroughs establish the exact admitted
  route and transitions. This is an evidence-backed rules reconstruction, not
  a claimed captured playthrough or entitlement. No video or audio was opened,
  played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BAA-001` | The current lawful product is Windows Steam app `35140`, standalone package `4109`, with the exact GOTY title and a current Ukraine offer | Confirmed | Direct | High | P1–P3 |
| `BAA-002` | Public Windows Build `597963` is the observed current distribution boundary; no publisher version is inferred from it | Observation | Corroborated | Medium | S1 |
| `BAA-003` | Story Mode offers Easy, Normal and Hard, remains distinct from Challenge Mode, and saves at authored checkpoints | Confirmed | Direct | High | P3 |
| `BAA-004` | The PC control surface admits direct traversal, crouch, glide, grapnel, Batarang, Detective Mode, map and contextual interaction | Confirmed | Direct | High | P3 |
| `BAA-005` | Successful FreeFlow attacks extend a live multiplier, and encounter closure awards experience for chain and combat variety; experience can replenish health | Confirmed | Direct | High | P3 |
| `BAA-006` | A visual cue identifies an eligible incoming close attack, allowing one reactive counter distinct from sustained guard or weapon parry | Confirmed | Direct | High | P3 |
| `BAA-007` | Detective Mode performs continuous visual analysis, highlights evidence and classifies nearby actors by current threat/equipment through ordinary occlusion | Confirmed | Direct | High | P3 |
| `BAA-008` | Grapnel traversal is limited to eligible highlighted higher anchors and moves the controlled body along the accepted attachment route | Confirmed | Direct | High | P3 |
| `BAA-009` | The decontamination rescue uses a Batarang-compatible control to activate ventilation and clear the persistent gas gate | Observation | Corroborated | High | S2, S3 |
| `BAA-010` | The required Titan encounter settles after bounded live survival/evasion and compatible interruption rather than total ordinary hostile clearance | Observation | Corroborated | High | S2, S3 |
| `BAA-011` | Inspecting the required object creates a forensic trail that Detective Mode exposes and advances through the authored route | Observation | Corroborated | High | S2, S3 |
| `BAA-012` | The first armed predator room combines local perception, elevated traversal, silent takedowns, finite reinforcement and a clearance-gated exit | Observation | Corroborated | High | S2, S3 |
| `BAA-013` | Leaving the facility completes the escape objective and exposes `Protect the Batmobile` at the immediate island successor state | Observation | Corroborated | High | S2, S3 |
| `BAA-014` | The bounded route keeps FreeFlow crowd combat and predator information separable in phase, but joins them through one ordered, checkpointed facility escape | Strong Pattern | Corroborated | High | `BAA-005`–`BAA-013` |

## Basic data

- Release / origin: developed by Rocksteady Studios and published by Warner
  Bros. Interactive Entertainment; the current Windows GOTY product was
  released on Steam 2010-03-26.
- Platform or physical form: lawfully offered English Windows single-player
  application; one fresh Normal Story Mode opening packet.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  spatial logic and topology; stealth and information control; ordered
  dependency sequencing.
- Primary and official sources, accessed 2026-09-05:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=35140&cc=ua&l=english),
    for exact current title, app identity, Windows platform, single-player
    category, package relation, current Ukraine offer and release date.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=4109&cc=ua&l=english),
    for standalone package `4109`, application membership, Windows support and
    lawful current offer.
  - **[P3]** [publisher-supplied English PC manual](https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/35140/manuals/BAA_G4W_man_inners_uk_v4.pdf?t=1745966724),
    linked from the current Steam product, for Story/Challenge separation,
    difficulty, profile/checkpoint behaviour, keyboard/mouse controls,
    FreeFlow, counter cue, ground takedown, Detective Mode, threat analysis,
    grapnel eligibility, Batarang, map and experience/health rules. Historical
    disc and Games for Windows Live assumptions are not imported.
  - **[P4]** [current Valve product page](https://store.steampowered.com/app/35140/Batman_Arkham_Asylum_Game_of_the_Year_Edition/?l=english),
    for developer/publisher identity, current Windows product, FreeFlow,
    forensic and Invisible Predator premises, traversal and the four separate
    GOTY Challenge Maps excluded here.
- Corroborating textual sources, accessed 2026-09-05:
  - **[S1]** [SteamDB public depots](https://steamdb.info/app/35140/depots/),
    for public Build `597963`, Windows depot `35141` and the secondary build
    timestamp. SteamDB is not treated as the publisher.
  - **[S2]** [GameFAQs Intensive Treatment text route](https://gamefaqs.gamespot.com/mac/641637-batman-arkham-asylum/faqs/81480/intensive-treatment),
    for the first controlled escort, mandatory combat, hostage, gas-control,
    Titan, forensic-trail, armed-predator, scan and facility-exit sequence;
    platform-specific input glyphs and optional collection are not imported.
  - **[S3]** [GameSpot text walkthrough](https://www.gamespot.com/articles/batman-arkham-asylum-walkthrough/1100-6216207/),
    for independent corroboration of FreeFlow actions, hostage and ventilation
    transitions, Titan settlement, evidence trail, predator traversal, required
    guard/vent route, island exit and immediate Batmobile successor objective.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P4` and `S1`–`S3` under the declared package, build, input, difficulty,
  entry, exclusions and `Continue` terminal; rules reasoning, not direct play.
- Claim IDs: `BAA-001`–`BAA-014`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly run, crouch, climb, glide and traverse vents;
  `ACT-161`: aim and commit ordinary strikes, stuns, Batarang throws or other
  directly controlled attacks against a reachable target; `ACT-235`: seize and
  neutralise an unaware reachable hostile with a silent takedown; `ACT-341`:
  rescue, speak, open, scan or operate each required authored object or actor;
  `ACT-370`: focus the investigative mode, follow its local trail and inspect
  highlighted evidence.
- Existing `ACT-419`: commit the taught contextual ground finisher while a
  living knocked-down hostile remains reachable and eligible.
- New `ACT-429`: respond to one visually announced incoming close attack with
  a timed unarmed counter. New `ACT-430`: select an eligible elevated anchor
  and commit grapnel-assisted body traversal to it.
- Character, villain, gadget, room, named move, exact combo and objective names
  remain game-scoped parameters. Claims: `BAA-004`–`BAA-013`.

### System Behaviour Genes

- Existing `SYS-215`: resolve directly commanded close, ranged-tool and
  predator combat in real time; `SYS-369`: replace a failed attempt with the
  latest authored checkpoint; `SYS-373`: escalate an observer from suspicion
  through detection, search and combat; `SYS-578`: apply hostile damage and
  compatible experience-triggered healing to one continuous health pool.
- Existing `SYS-112`: after the compatible remote control is struck, expose
  its persistent ventilation state and clear the gas gate; `SYS-680`: convert
  the examined object into an authored forensic trail and route progress;
  `SYS-749`: release the finite armed reinforcement associated with the first
  predator-room trigger; `SYS-779`: settle the required charging-hostile
  pressure after its bounded survival/performance threshold while the
  controlled actor remains alive.
- New `SYS-789`: extend the live FreeFlow chain with accepted attack, counter,
  stun and takedown actions, reset broken continuity and settle chain/variation
  experience when the finite encounter closes.
- Resolution order: current objective and local information expose the next
  gate; direct traversal changes route/anchor reach; hostile perception changes
  suspicion and combat state; accepted attacks, counters and finishers update
  health and chain continuity; finite clearance settles encounter experience
  and opens its route; compatible authored interactions rescue actors or
  activate the fan; the pressure encounter settles on its threshold; evidence
  inspection creates a trail; armed clearance exposes the exit; the exterior
  transition writes checkpoint and successor-objective state.
- Claims: `BAA-005`–`BAA-014`.

### Constraint Genes

- Existing `CON-077`: hostile sight remains directed, distance- and occlusion-
  bounded; `CON-282`: every encounter, rescue, clue, scan and exit requires its
  authored predecessor; `CON-335`: silent neutralisation requires an unaware,
  reachable legal target; `CON-402`: a locked encounter exit remains closed
  until the finite required hostile set is resolved.
- Existing `CON-589`: a ground finisher requires the living hostile's current
  knocked-down opportunity and reachable context. New `CON-599`: grapnel
  traversal requires a compatible elevated anchor, selectable relation and
  clear attachment/body route.
- Scarce strategic resources: health, safe geometry, current hostile awareness,
  uninterrupted chain, legal finisher/counter intervals, available anchors,
  rescue state, forensic evidence state and latest checkpoint. The permanent
  Batarang/grapnel are not modelled as finite ammunition.
- Claims: `BAA-004`–`BAA-013`.

### Information Genes

- Existing `INF-115`: ordinary avatar-centred sight and local effects expose
  only partial current hostile state; `INF-119`: health, experience and
  available character-development state are visible; `INF-125`: map, current
  objective and authored route gates are inspectable; `INF-268`: tutorial
  surfaces teach the current movement, combat or investigative action before
  advancing.
- Existing `INF-295`: a living hostile's visible knocked-down state exposes
  the temporary ground-finisher opportunity; `INF-298`: local awareness cues
  expose incoming detection and current alert escalation.
- New `INF-309`: focused tactical vision exposes current occluded actor,
  equipment/threat and evidence classifications without persistent marking.
  New `INF-310`: the incoming close-attack cue identifies the current counter
  opportunity without guaranteeing a successful response.
- Audio cues are neither necessary nor evidence for this packet. Exact colours,
  icon shape, actor, equipment, clue and control glyph remain parameters.
- Claims: `BAA-004`–`BAA-013`.

### Objective Genes

- Existing `OBJ-026`: make the bounded facility route traversable through its
  mandatory combat, rescue, forensic and predator gates, then navigate the
  controlled avatar to the declared island-surface location and retain the
  successor objective after `Continue`.
- Any single fight, clue, rescue, scan, door, autosave or exterior step before
  the declared checkpoint/reload test is intermediate. Death/checkpoint retry
  is failure of the current attempt, not a second positive terminal.
- Claims: `BAA-009`–`BAA-014`.

### Time Genes

- Existing `TIM-003`: traversal, hostile perception, incoming attacks,
  FreeFlow chain continuity, damage, pressure settlement and predator routing
  advance continuously outside blocking menus and authored transitions.
- Claims: `BAA-005`, `BAA-006`, `BAA-010`, `BAA-012`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Current Windows package; fresh profile; English; keyboard/mouse; Story Mode Normal | Reach the first controlled escort state | Ordinary control begins before the first required inmate group | exact bounded entry | `BAA-001`–`BAA-004` |
| An unarmed hostile commits an eligible close attack | Read the local cue and commit counter during its interval | Accepted timing interrupts or redirects the attack; missed timing leaves ordinary contact resolution | prompted reactive counter | `BAA-005`, `BAA-006` |
| A finite unarmed group remains and the route is locked | Chain strikes, counters, stuns, evades and eligible ground finishers | Accepted actions extend the current multiplier; broken continuity resets it; closure awards chain/variation experience and reopens the route | FreeFlow encounter settlement | `BAA-005`, `BAA-006` |
| A hostile is living, knocked down and reachable | Commit the ground-takedown command | The contextual finisher resolves before opportunity recovery or interruption | temporary close finisher | `BAA-005` |
| An elevated compatible anchor is highlighted and unobstructed | Address it and commit grapnel traversal | The line attaches and the body travels to the anchor; incompatible scenery rejects | anchor-gated traversal | `BAA-004`, `BAA-008` |
| Detective Mode is active near actors or evidence | Inspect the focused overlay | Current actor category, weapon/threat state and clue highlight become visible through ordinary occlusion only while the mode applies | tactical information boundary | `BAA-007` |
| The first hostage encounter is active below an eligible vantage | Grapple, position, glide-kick and complete the reachable finisher | The required aggressor is neutralised and the protected actor remains available | taught traversal-combat gate | `BAA-004`, `BAA-008` |
| Decontamination gas and required actors remain | Traverse the room, rescue the required actors and strike the compatible control with the Batarang | The accepted fixture activates ventilation and persistently clears the gas route | remote fixture dependency | `BAA-009` |
| The charging Titan pressure encounter is active | Preserve distance, evade charges and use the compatible interrupt while surviving | Once the authored survival/performance threshold is met with health above zero, the hostile settles and onward route authority returns | non-clearance pressure settlement | `BAA-010` |
| The required local object is unexamined | Focus Detective Mode and inspect it | The evidence is registered and an authored forensic trail becomes available | investigation progress | `BAA-011` |
| The forensic trail is current | Follow its locally exposed route through climb and vent geometry | The path reaches the first armed predator area without revealing all future route state | bounded trace following | `BAA-011` |
| Armed guards are active in the first predator room | Use tactical classification, legal anchors, sightline breaks, glide kicks and silent takedowns | Awareness, search and combat update continuously; a finite reinforcement may enter after its trigger | predator information/action loop | `BAA-007`, `BAA-008`, `BAA-012` |
| The complete required armed set is neutralised | Complete the mandatory portrait scan and speak to the required guard | The authored utility/vent continuation becomes legal | clearance and scan gate | `BAA-012` |
| The utility exit route is connected | Traverse the vent, exterior threshold and cliff grapple | The facility-escape objective completes and `Protect the Batmobile` becomes current | declared successor transition | `BAA-013` |
| The successor objective is current and no later route progress is made | Wait for checkpoint, quit and use `Continue` on the same profile | Ordinary control resumes in Arkham Island East with the same successor objective | retained positive terminal | `BAA-013`, `BAA-014` |
| Health reaches zero before terminal settlement | Accept ordinary retry | The latest authored checkpoint replaces transient position, health, hostile and chain state | negative boundary | `BAA-003` |

## Strategic and experiential structure

- Planning horizon: read the next authored gate, distinguish unarmed crowd
  pressure from armed predator risk and choose whether immediate progress needs
  close-combat timing, a traversal anchor, tactical classification, a rescue,
  a compatible tool response or an unseen route around sightlines.
- Local tactics: FreeFlow rewards maintaining action continuity while watching
  distinct incoming-counter and ground-finisher opportunities. Armed opponents
  reverse the safe relation: direct crowd engagement is displaced by occlusion,
  elevated anchors, silent reach and alert-state management.
- Medium-term structure: the opening alternates combat tutorial, rescue/fixture,
  pressure survival, forensic investigation and predator clearance without
  merging them into one universal combat rule. Ordered gates bind those phases
  into one traversable escape.
- Reversible versus irreversible: aim, position, alert, damage, chain state and
  hostile order are attempt-local and checkpoint-recoverable; rescued actors,
  cleared route gates, registered evidence, escape completion and successor
  objective form the authored retained path.
- Failure attribution: counter cue, prone-state finisher opportunity, Detective
  classification, hostile awareness, grapple highlight, objective/map text,
  checkpoint state and successor label distinguish timing, reach, perception,
  dependency, clearance and terminal mistakes.
- Player trust: an ineligible anchor rejects before body travel; the tactical
  overlay classifies current rather than future state; route barriers remain
  until their required closure; the positive terminal survives `Continue`.

## Replay and variation

- The facility order, required rescues, pressure encounter, evidence trail,
  predator gate, portrait scan and island transition are authored. Exact route,
  attack sequence, combo value, anchor choice, takedown order, alert recovery
  and checkpoint use can vary within the same ruleset.
- The bounded route permits both detected recovery and silent predator play,
  but does not require an optimal no-detection performance or exact experience
  total. Normal is fixed; Easy or Hard would change combat pressure and belongs
  in another packet.
- Challenge Maps, WayneTech builds, optional riddles and later gadgets provide
  replay value but are excluded because their scoring, progression or route
  systems do not causally enter this opening terminal.

## Adjacent systems and history

- DOOM (2016) shares direct real-time combat, finite clearance, triggered
  hostile groups, ground-level contextual finishers, health pressure and one
  retained authored route. Its first mission converts damage-created stagger
  into resource-dropping executions; this packet adds prompted unarmed
  counters, uninterrupted variation experience, Detective classification,
  grapnel anchors and a separate armed-predator phase.
- Far Cry 3 shares stealth perception, direct weapon combat, unaware-target
  takedowns, finite hostile clearance and retained authored world progress. Its
  reviewed outpost relies on optical persistent hostile marking, diversion and
  service-node conversion; this packet uses reversible occlusion-through-wall
  classification, counter-based crowd combat and an ordered facility escape.
- Dishonored (2012) shares local alert escalation, unaware-target takedowns,
  authored route gates and a retained mission transition. Dishonored previews
  a short instantaneous supernatural relocation and records mission conduct;
  this packet traverses a legal grapnel path and settles no conduct score.
- Tomb Raider (2013) shares third-person traversal, contextual takedowns,
  bounded sensing, clearance and an authored location terminal. Its reviewed
  ascent centres on contextual cover and environmental traversal; this packet
  classifies armed threats through occlusion and alternates FreeFlow with an
  explicit predator room.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-235`, `ACT-341`, `ACT-370`, `ACT-419`, `ACT-429`, `ACT-430` | traversal, attack, stealth, evidence, finisher, counter and grapnel |
| System Behaviour | `SYS-112`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-578`, `SYS-680`, `SYS-749`, `SYS-779`, `SYS-789` | fixture, combat, retry, alert, health, evidence, reinforcement, pressure and chain settlement |
| Constraint | `CON-077`, `CON-282`, `CON-335`, `CON-402`, `CON-589`, `CON-599` | perception, order, stealth, clearance, finisher and grapnel eligibility |
| Information | `INF-115`, `INF-119`, `INF-125`, `INF-268`, `INF-295`, `INF-298`, `INF-309`, `INF-310` | local, personal, route, tutorial, finisher, awareness, tactical and counter cues |
| Objective | `OBJ-026` | reach and retain the bounded exterior successor location |
| Time | `TIM-003` | continuous traversal, combat, perception and pressure |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `254` (`GAME-0001`–`GAME-0254`).
- Exact genome matches: none.
- Tied near matches: `GAME-0245` — DOOM (2016) (`17 / 39 = 0.435897`).
- Supported combination subsets: `COMB-0253`.
- Scan date: 2026-09-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0245` — DOOM (2016) | `ACT-008`, `ACT-161`, `ACT-341`, `ACT-419`, `SYS-215`, `SYS-369`, `SYS-578`, `SYS-749`, `CON-282`, `CON-402`, `CON-589`, `INF-115`, `INF-119`, `INF-125`, `INF-295`, `OBJ-026`, `TIM-003` | Both traverse a clearance-gated authored route, resolve finite triggered hostile groups in real time, use a temporary ground-finisher opportunity, apply one continuous health pool and recover from checkpoints before a retained location terminal. DOOM creates finishers from damage stagger and converts them into spatial resource recovery. This packet instead joins visually prompted unarmed counters and encounter-settled chain experience to occlusion-through-wall threat classification, anchor-gated grapnel traversal, forensic evidence and a separate armed-predator phase. | Near, `17 / 39 = 0.435897` |

### Preserved research notes

- New genes: `ACT-429`, `ACT-430`, `SYS-789`, `CON-599`, `INF-309` and
  `INF-310`.
- Reused genes: `ACT-008`, `ACT-161`, `ACT-235`, `ACT-341`, `ACT-370`,
  `ACT-419`, `SYS-112`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-578`,
  `SYS-680`, `SYS-749`, `SYS-779`, `CON-077`, `CON-282`, `CON-335`,
  `CON-402`, `CON-589`, `INF-115`, `INF-119`, `INF-125`, `INF-268`,
  `INF-295`, `INF-298`, `OBJ-026` and `TIM-003`.
- Classification result: `New combination of known and new genes`.
- Evidence and reasoning: ordinary direct traversal, attacks, stealth
  neutralisation, contextual interaction, investigation, ground finishers,
  combat, checkpoint, alert, health, evidence, finite reinforcement, pressure
  settlement, directed perception, authored order, clearance, local state,
  objective and time reuse established portable boundaries. Six additions
  isolate the counter cue/action, grapnel command/eligibility, focused tactical
  classification and encounter-settled action-chain experience.
- Lower-ID scan: reject `ACT-425`, `SYS-777` and `CON-594`, because the counter
  does not require a usable close weapon or spend its durability; reject
  `ACT-421` and `SYS-772`, because the body traverses the accepted grapnel path
  instead of being placed immediately at a supernatural endpoint; reject
  `INF-287`, because tactical classifications are reversible and no acquired
  actor mark must persist; reject `OBJ-155`, because the terminal is an
  objective/location handoff rather than explicit chapter completion; reject
  upgrades, exact reward numbers, Challenge scoring and later gadgets as
  unreachable or optional parameters.

## Taxonomy impact

- Registry changes: six additive Active portable boundaries; no earlier gene
  wording, semantic boundary, lifecycle or reviewed game signature changes.
- Taxonomy-change record: none; all additions are ordinary game-unit taxonomy.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; every product,
  actor, room, gadget, mode, quest, exact combo and reward label remains a
  game-scoped parameter.

## Negative results

- No direct play, entitlement, local-build, screenshot, video, audio, acting
  or audiovisual-analysis claim. Build ID and timestamps remain secondary.
- No Challenge Mode, DLC, complete-campaign, later-island, upgrade, collectible,
  platform, input, difficulty or series union.
- No earlier reviewed signature, lifecycle state or conclusion changes.

## Combination subset scan

- Every verified pre-unit combination is tested as a proper subset of this
  thirty-three-gene signature. `COMB-0253` records the strict counter,
  tactical-vision, grapnel, predator and route-terminal core; supported earlier
  subsets, if any, are listed after deterministic regeneration.
- Comparison and subset scan date: 2026-09-05.

## Delta summary

## New facts

- [Confirmed | Direct | High] The current Windows product, Story/Challenge
  boundary, fresh Normal settings and official input/information rules are
  fixed in `BAA-001`–`BAA-008`.
- [Observation | Corroborated | High] The rescue, pressure, evidence, predator
  and retained island transitions are fixed in `BAA-009`–`BAA-014`.

## New genes

- [Observation | Corroborated | High] `ACT-429` and `INF-310` separate one
  visible incoming-attack opportunity from the committed unarmed counter;
  `ACT-430` and `CON-599` separate grapnel commitment from anchor legality;
  `SYS-789` settles one uninterrupted combat chain into encounter experience;
  `INF-309` exposes reversible occluded tactical classifications.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0253` joins prompted counter
  timing, grapnel anchor routing, reversible threat classification, forensic
  progress and finite predator clearance inside one retained facility escape.

## Taxonomy changes

- [Observation | Corroborated | High] Six Active portable genes are added; no
  existing boundary, lifecycle or reviewed signature changes.

## New questions

- Does BioShock Remastered's bounded opening require a new chamber-mediated
  resource transformation, or can its weapon/plasmid loop reuse established
  dual-authority and authored-route genes without merging resource rules?

## Next recommended unit

- [Hypothesis | Limited | High] `GAME-0256` — BioShock Remastered.
- Optimisation criterion: isolate one current lawful remastered Windows
  opening packet through a retained early objective/checkpoint terminal.
- Expected information gain: test weapon/plasmid resource coupling, authored
  environmental gates and revival/checkpoint semantics.
- Backlog impact: fourth game unit in the ordered Batch 014 horizon.

## Why this unit

- [Hypothesis | Limited | High] It is the next fixed ID after the selected
  counter-and-predator route and preserves the ordered horizon.
