---
game_id: GAME-0349
slug: tom-clancys-splinter-cell
game_title: "Tom Clancy’s Splinter Cell"
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-107
    - ACT-161
    - ACT-202
    - ACT-341
    - ACT-344
    - ACT-491
  system:
    - SYS-057
    - SYS-215
    - SYS-369
    - SYS-373
    - SYS-578
    - SYS-780
    - SYS-797
  constraint:
    - CON-077
    - CON-282
    - CON-285
    - CON-330
    - CON-335
  information:
    - INF-073
    - INF-075
    - INF-115
    - INF-125
    - INF-316
  objective:
    - OBJ-155
  time:
    - TIM-003
    - TIM-007
---

# Game: Tom Clancy's Splinter Cell

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Sam Fisher, Third
Echelon, CIA Training Farm, Police Station, T'bilisi, OPSAT, Stealth Meter,
SC pistol, Lock Pick, Data Stick, Thomas Gurgenidze, Alison Madison, Robert
Blaustein, Vernon Wilkes, Xbox and `US-012` are carrier parameters, not gene
names.

## Analysis scope

- Version / ruleset: the first North American English Xbox retail release of
  *Tom Clancy's Splinter Cell*, original-Xbox product code `US-012`, released
  2002-11-17, with Xbox title ID `5553000C`. Create a fresh profile, select
  Normal difficulty and use the
  original base-disc Training Course and Police Station rules. The downloadable
  mission packs, later title updates where they alter rules, PC, PlayStation 2,
  GameCube, Game Boy Advance, mobile, PlayStation 3 HD, backward-compatible
  enhancement, remake, sequel, other region, cheat and modification are separate
  products or packets.
- Structured analysis target: the original Xbox booklet's stealth, control,
  interface, saving and security-fixture rules joined to two independent written
  original-Xbox routes from first Training Course control through the complete
  Police Station mission and a reload-verified first Defense Ministry
  checkpoint; see `GAME-0349` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Scenario and entry: create and save a new profile on Normal, choose its first
  available level and begin the Training Course. The packet starts at first
  ordinary movement control before the calibration and obstacle exercises; no
  mission checkpoint or later equipment is imported.
- Fixed reproducible route: complete calibration and the traversal course;
  enter covert-operations training; pick the practice lock; grab the designated
  trainee from behind, interrogate him for the keypad fact and enter the learned
  code; force another restrained trainee to operate the retinal scanner; shoot
  the light so the surveillance camera cannot acquire Sam; neutralise the
  designated guard without killing him and place his unconscious body fully in
  shadow; cross hanging chains and broken glass slowly and crouched; exit the
  course. Begin Police Station; reach the contact through the rooftop, burning
  building and apartment route; acquire the mandatory computer/data facts;
  traverse the balcony, zip line, lock-picked door and dead drop; use the learned
  `5929` precinct code; reach Madison and Blaustein in the morgue; access the
  security-surveillance computer; leave through the public-relations route and
  reach Wilkes's van. Accept Police Station completion, enter first ordinary
  Defense Ministry control, save its checkpoint to the same profile, quit, load
  that saved checkpoint and verify ordinary successor control.
- Primary decision loop: read current illumination on the Stealth Meter, local
  sight and sound, objective and selected item; choose analog speed and posture;
  remain behind opaque geometry or in shadow; interact with the current legal
  door, computer, lock, keypad or person; nonlethally neutralise an unaware
  reachable observer when necessary; move every scoped unconscious body into
  darkness before another patrol or body-check boundary can find it; and recover
  from a failed checkpoint without importing later transient state.
- Positive terminal: Police Station has settled at Wilkes's van, the successor
  Defense Ministry segment has instantiated, and reloading the freshly saved
  successor checkpoint restores ordinary control there. Merely finishing the
  Training Course, reaching the precinct or accessing surveillance does not
  complete the packet.
- Failure and recovery: Life reaching zero, violating a current critical
  mission condition or allowing an applicable alarm policy to abort the active
  objective ends the current attempt. Loading the latest saved Checkpoint
  replaces transient positions, awareness, bodies, damage and route progress
  with recorded checkpoint state. The fixed successful route raises no alarm.
- Included: analog movement speed; running, walking, crouching, climbing,
  mantling, zip line, wall jump and split jump; back-to-wall concealment;
  directed sight and occlusion; movement sound and local investigation;
  illumination-dependent acquisition; Stealth Meter; Life; selected pistol and
  ammunition; shooting a light; close nonlethal neutralisation; rear grab;
  interrogation for one operational code; forced cooperation at a retinal
  scanner; carrying and quietly placing an unconscious body; doors, computers,
  data facts, keypad codes, lock picking, camera, light switch and objective
  interactions; local suspicion, detection and combat; checkpoint saving,
  loading, mission settlement and successor control.
- Reproducible parameterisation: fresh English profile, Normal difficulty and
  the original Xbox base campaign. Patrol phase, exact analog speed, optional
  detours, Life and ammunition may vary. Use only the documented Training and
  Police Station objective chain, keep scoped neutralisations nonlethal, hide
  every scoped body in darkness, trigger no alarm, then save and reload the first
  successor checkpoint. The alarm-free route is a reproducibility constraint,
  not a claim that Police Station necessarily fails on its first alarm.
- Excluded: thermal vision, SC-20K, sticky/distraction cameras, camera jammer,
  gas, explosives, mines, ordinary lethal guard clearance, optional medkits and
  data sticks, alternate violent routes, alarm-count maximisation, scores or
  ranks, Defense Ministry play beyond the first reload check, every later
  mission, downloadable mission pack, multiplayer, Xbox Live download service,
  other platform or edition, and audiovisual criticism.
- Direct-play status: not conducted. No disc, console, controller, profile,
  checkpoint, executable, dump, emulator, screenshot, video or audio was used.
  This is a source-bounded reconstruction from the exact English Xbox booklet,
  contemporary product evidence and written original-Xbox routes, not a claimed
  playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SC-001` | The selected product is the first North American English original-Xbox `US-012` base release from 2002-11-17, not another platform, later enhancement or downloadable mission pack | Confirmed | Corroborated | High | P1, P2, P3, S1 |
| `SC-002` | Analog movement speed, crouching and back-to-wall posture change emitted sound or visual exposure rather than merely changing animation | Confirmed | Direct | High | P1 |
| `SC-003` | The Stealth Meter reports local light exposure, while shadow, slow movement and crouching reduce the danger of hostile visual acquisition without granting intrinsic invisibility | Confirmed | Direct | High | P1 |
| `SC-004` | Running, jumping, landing, chains and glass can emit local sound that causes an eligible patrol to investigate | Confirmed | Corroborated | High | P1, S2, S3 |
| `SC-005` | An eligible unaware person can be grabbed from behind, interrogated for an operational fact or dragged to a retinal scanner for forced cooperation | Confirmed | Direct | High | P1 |
| `SC-006` | A dead or unconscious body can be lifted, carried and quietly placed; leaving it exposed permits discovery and resulting alert pressure | Confirmed | Direct | High | P1 |
| `SC-007` | Surveillance cameras can directly trigger alarms; a selected light can be shot so darkness changes camera acquisition, while an incorrect keypad or retinal submission can alarm | Confirmed | Direct | High | P1 |
| `SC-008` | The Training Course deterministically exercises lock picking, interrogation, keypad entry, forced retinal cooperation, light/camera concealment, body hiding and quiet chain/glass traversal | Observation | Corroborated | High | S2, S3 |
| `SC-009` | Police Station orders the contact, apartment/data, dead drop, precinct code, agents, surveillance system and Wilkes extraction objectives before the next mission | Observation | Corroborated | High | S2, S3 |
| `SC-010` | The complete bounded signature ends only after Police Station settlement and a reload-verified first Defense Ministry checkpoint | Strong Pattern | Corroborated | High | `SC-001`–`SC-009`, V1 |

## Basic data

- Release / origin: Ubisoft Montreal; North American original-Xbox launch,
  2002-11-17.
- Platform or physical form: licensed original Xbox retail disc, product code
  `US-012`; manual part number `510130-MNL2`.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary sources, accessed 2026-09-21:
  - **[P1]** [original North American Xbox instruction
    booklet](https://datassette.s3.us-west-004.backblazeb2.com/manuais/tom_clancys_splinter_cell_usa.pdf?VersionId=4_zd2580b9b75789e418f390019_f1147e442b8430275_d20221005_m153217_c004_v0402011_t0056_u01664983937753),
    local SHA-256
    `ea54a27f52670aa0e91cd87b97bebf65de60a0bea6846f2b19fcdd00cd479aa6`,
    for original-disc identity, controls, analog stealth, Stealth Meter, sound,
    alarms, profiles/checkpoints, movement, body handling, interrogation,
    cooperation, OPSAT, weapons and security fixtures.
  - **[P2]** [Xbox product page](https://www.xbox.com/en-US/games/store/tom-clancys-splinter-cell/C46H5R7GT7X9),
    for Ubisoft Montreal identity, dynamic light and sound, lethal/nonlethal
    approaches, multiple routes, climbing, mantling and interrogation.
  - **[P3]** [Xbox preservation announcement](https://news.xbox.com/en-us/2019/06/10/e3-2019-whats-next-xbox-backward-compatibility/),
    for separation of the original Xbox game from its three downloadable
    mission packs in later backward-compatible availability.
- Corroborating textual sources, accessed 2026-09-21:
  - **[S1]** [GameSpot's contemporary ship
    notice](https://www.gamespot.com/articles/splinter-cell-ships-for-the-xbox/1100-2897852/),
    for the North American original-Xbox launch and light-driven concealment.
  - **[S2]** [GameFAQs original-Xbox guide by
    TwistidSoul](https://gamefaqs.gamespot.com/xbox/561102-tom-clancys-splinter-cell/faqs/23008),
    for complete Training and Police Station objective order, codes, body
    hiding, precinct surveillance and Wilkes extraction.
  - **[S3]** [GameFAQs original-Xbox guide by
    Adrenaline_SL](https://gamefaqs.gamespot.com/xbox/561102-tom-clancys-splinter-cell/faqs/32695),
    for an independent Training/Police Station route, alarm-check locations,
    passcodes and mandatory data sources.
  - **[S4]** [ConsoleMods Xbox title database](https://consolemods.org/wiki/Xbox:Title_Updates),
    for product code `US-012` and title ID `5553000C`; this community technical
    index corroborates identity but does not define mechanics.
- Validation source: **[V1]** repository-side executable state reconstruction
  derived from P1–P3 and S1–S4; it does not execute or inspect the commercial
  program.
- Claim IDs: `SC-001`–`SC-010`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly move Sam at analog speed through the authored route,
  including ladders, pipes, ledges and zip-line arrival.
- `ACT-107`: complete the eligible interrogation exchange that registers the
  exact training keypad fact for later entry.
- `ACT-161`: ready and fire the selected SC pistol at the documented training
  light; the fixed route does not require shooting a person.
- `ACT-202`: change between standing, crouched, wall-attached, hanging and
  split-jump body configurations to alter clearance, sound and exposure.
- `ACT-341`: commit the currently legal person, door, computer, light switch,
  keypad, retinal scanner, trap door or objective interaction.
- `ACT-344`: probe and turn the selected authored lock with the Lock Pick until
  its tumblers admit opening.
- New `ACT-491`: take one eligible dead or unconscious body into an exclusive
  carry state, move it and quietly place it at a chosen reachable position.
- Rejected `ACT-489`: the packet's sound pressure comes from locomotion,
  landing, chains, glass and gunfire; no deliberate wall tap is required.
- Claims: `SC-002`, `SC-004`–`SC-009`.

### System Behaviour Genes

- `SYS-057`: an eligible guard replaces patrol with investigation of current
  movement, landing, chain, glass or gunshot sound and may return if no target
  is acquired.
- `SYS-215`: movement, patrol, perception, interaction, pistol fire, attack and
  Life damage resolve in one advancing live state.
- `SYS-369`: death or declared critical failure followed by Load restores the
  latest saved Checkpoint rather than retaining failed transient state.
- `SYS-373`: visible movement, sound, exposed bodies or harmful effects raise
  local suspicion into detection, allied alert and combat.
- `SYS-578`: hostile attacks reduce Sam's one Life pool; zero Life ends the
  attempt. Scoped medkit use is excluded.
- `SYS-780`: Police Station settlement writes or accepts its result across the
  mission boundary and instantiates saved ordinary Defense Ministry control.
- `SYS-797`: local light exposure, movement and sight geometry jointly change
  hostile or camera acquisition; destroying the documented light reduces that
  exposure without granting a binary invisibility power.
- Resolution order: movement/posture and current light produce sound/exposure;
  observers investigate or acquire; legal interaction, fact, lock, keypad,
  body or shot input resolves; objective dependencies update; failure restores
  a checkpoint, while Wilkes extraction settles into the successor mission.
- Claims: `SC-002`–`SC-010`.

### Constraint Genes

- `CON-077`: a guard or camera visually acquires Sam only through its current
  directed region without a blocking opaque relation.
- `CON-282`: calibration, covert training, Police Station objectives, Wilkes
  extraction and successor save form an authored dependency order.
- `CON-285`: pistol fire requires the selected weapon, compatible ammunition
  and a legal aimed state; reloading consumes compatible carried rounds.
- `CON-330`: the active mission continues only while Sam, mandatory people,
  information, fixtures and the permitted area remain viable.
- `CON-335`: the chosen nonlethal rear grab or neutralisation requires one
  unaware eligible target in the supported reachable relation.
- Scarce route state: Life, ammunition, current light and sound exposure,
  observer awareness, body positions, acquired codes, objective flags and the
  latest saved Checkpoint.
- Claims: `SC-002`–`SC-010`.

### Information Genes

- `INF-073`: HUD and quick inventory expose the selected weapon/item and
  ammunition before the next commitment.
- `INF-075`: the Life bar exposes current survival capacity.
- `INF-115`: current camera view, spatial footsteps, voices, chains, glass,
  shots and body discovery expose only locally perceivable hostile state.
- `INF-125`: the OPSAT and live objective display expose current mandatory
  goals, new mission information and the legal authored gate without revealing
  future patrol policy.
- `INF-316`: the Stealth Meter reports Sam's current illumination exposure
  independently of whether one particular observer has already detected him.
- Claims: `SC-002`–`SC-009`.

### Objective Genes

- `OBJ-155`: complete the Training-supported ordered Police Station mission,
  reach Wilkes's extraction, accept mission settlement and retain ordinary
  control at a reload-verified first Defense Ministry checkpoint.
- Success, evaluation and failure: success is a retained authored mission
  handoff, not every guard defeated or every optional data stick collected.
  Life loss or critical-condition violation restores the latest checkpoint.
- Claims: `SC-009`, `SC-010`.

### Time Genes

- `TIM-003`: patrols, perception, sound investigation, camera sweeps, attacks
  and damage progress in real time while movement and interaction remain live.
- `TIM-007`: a saved Checkpoint can be loaded and continued with different
  movement, concealment or neutralisation choices, replacing the observed
  future from that point.
- Claims: `SC-002`–`SC-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Normal Training Course control | vary analog movement, stand/crouch and complete the obstacle sequence | speed and posture change movement, clearance, sound and exposure while authored calibration gates open in order | embodied stealth input | `SC-002`, `SC-008` |
| Practice lock is reachable and Lock Pick selected | rotate toward the current responsive tumbler until each admits progress | completed tumbler sequence unlocks the authored door | physical lock manipulation | `SC-008` |
| Designated trainee is unaware and reachable from behind | grab, choose Interrogate and finish the exchange | the operational keypad fact becomes known and can be entered at its matching fixture | information-bearing restraint | `SC-005`, `SC-008` |
| Retinal gate rejects Sam and an eligible trainee is restrained | drag him into scanner reach and choose Force Cooperate | his accepted identity opens the gate; an incorrect scan would alarm | person-mediated access | `SC-005`, `SC-007`, `SC-008` |
| Training camera watches a lit traversal region | select the pistol and shoot the documented light, then cross in shadow | illumination falls and camera acquisition pressure drops without changing Sam into an intrinsically invisible actor | light-dependent detection | `SC-003`, `SC-007`, `SC-008` |
| Designated guard is unaware and a dark alcove is reachable | neutralise nonlethally, pick up the unconscious body, carry it and place it in shadow | body position changes from exposed to concealed, preventing the expected discovery path | body relocation as stealth work | `SC-006`, `SC-008` |
| Chains and broken glass lie between Sam and the Training exit | crouch and move slowly around chains and across glass | sound remains below the exercise's investigation threshold and the exit admits completion | surface-sensitive sound | `SC-004`, `SC-008` |
| Police Station route is live | satisfy contact, apartment/data, dead drop, precinct-code, morgue and surveillance objectives in order | each completed predecessor exposes the next authored goal while checkpoint state advances | ordered mission chain | `SC-009` |
| Police Station objectives are complete and Wilkes's van is reachable | enter the extraction relation | Police Station settles and the Defense Ministry successor becomes available | mission handoff | `SC-009`, `SC-010` |
| First Defense Ministry control is saved | quit to profile, load the saved Checkpoint | ordinary successor control and recorded mission state return while discarded transient alternatives do not | retained terminal and branchability | `SC-010` |

## Strategic and experiential structure

- Local decisions: trade speed for quieter travel, compare the Stealth Meter
  with actual observer geometry, wait for a camera or patrol, choose shadow,
  and decide where an unconscious body can remain unseen.
- Medium-term planning: learn and retain codes before their keypads, preserve
  ammunition for a light rather than a person, hide every scoped body before a
  body-check boundary and follow the Police Station objective graph without
  importing later-mission assumptions.
- Long-term structure: Training explicitly teaches relations later composed by
  Police Station: light and motion determine acquisition, sound redirects local
  attention, people can be information or access authorities, and a neutralised
  observer remains a discoverable world object until relocated.
- Common heuristics: crouch before glass, use the Stealth Meter as exposure
  feedback rather than proof of omniscience, place bodies fully inside shadow,
  acquire each code from the admitted source and save at offered checkpoints.
- Failure attribution: Life, Stealth Meter, visible light boundary, spatial
  sound, observer reaction, alarm feedback, current objective and checkpoint
  location separate exposure, noise, body-placement, dependency and survival
  failures.
- Player-trust factors: the same illumination change must affect both meter and
  camera risk; a learned code must open only its fixture; an exposed body must
  remain discoverable; reload must replace failed transient state.
- Claims: `SC-002`–`SC-010`.

## Replay and variation

- What changes between attempts: patrol phase, analog speed, optional wait,
  selected concealment, exact body-placement point, detection, Life,
  ammunition, checkpoint timing and nonlethal route.
- Randomness or procedural generation: areas, objectives, codes, cameras,
  lights, checkpoint boundaries and extraction are authored. Variation comes
  from live observer timing and player-selected route, not procedural geometry.
- Multiple viable strategies: Police Station permits different violent and
  nonviolent local solutions, but the fixed corpus route chooses alarm-free
  nonlethal play so body handling and concealment remain causally exercised.
- Typical replay motive: complete a cleaner undetected route, reduce body risk
  or compare alternative routes. Later mission scoring and the rest of the
  campaign are outside scope.
- Claims: `SC-002`–`SC-010`.

## Adjacent systems and history

- Metal Gear Solid shares crouched authored infiltration, directed sight,
  local sound investigation, contextual fixtures, checkpoint recovery and
  live stealth pressure. It exposes observer cones on a radar and models a
  named Alert/Evasion/Infiltration countdown. Splinter Cell instead makes the
  actor's own continuous illumination legible, allows light destruction to
  change perception, turns restrained people into information/access
  authorities and makes unconscious bodies movable discovery hazards.
- Metro Exodus shares illumination-dependent hostile acquisition and a
  personal light-state indicator. Its `Moscow` packet adds filter time,
  environmental harm and a train escape, while this packet isolates direct
  body relocation, training-to-mission transfer, retinal cooperation and an
  explicit light meter.
- Dishonored shares local suspicion, nonlethal stealth neutralisation and a
  mission handoff but supplies directional awareness cues and supernatural
  traversal rather than this light/sound/body tutorial grammar.
- Important difference: `ACT-491` is not an inventory pickup or heavy loot
  bag. The relocated object is an incapacitated actor whose visibility can
  independently change future hostile perception.
- Claims: `SC-001`–`SC-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-107`, `ACT-161`, `ACT-202`, `ACT-341`, `ACT-344`, `ACT-491` | Sam, analog speed, trainee, pistol, lock and body are parameters |
| System Behaviour | `SYS-057`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-578`, `SYS-780`, `SYS-797` | observer, light, sound, alarm, checkpoint and mission are parameters |
| Constraint | `CON-077`, `CON-282`, `CON-285`, `CON-330`, `CON-335` | sight cone, ammunition, target relation and mission viability are parameters |
| Information | `INF-073`, `INF-075`, `INF-115`, `INF-125`, `INF-316` | OPSAT, Stealth Meter, Life and objective labels are parameters |
| Objective | `OBJ-155` | Police Station, Wilkes and Defense Ministry are parameters |
| Time | `TIM-003`, `TIM-007` | live stealth cadence and checkpoint branch are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `348` (`GAME-0001`–`GAME-0348`).
- Exact genome matches: none.
- Tied near matches: `GAME-0260` — Metro Exodus (`21 / 44 = 0.477273`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0260` — Metro Exodus | `ACT-008`, `ACT-161`, `ACT-202`, `ACT-341`, `SYS-057`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-578`, `SYS-780`, `SYS-797`, `CON-282`, `CON-285`, `CON-335`, `INF-073`, `INF-115`, `INF-125`, `INF-316`, `OBJ-155`, `TIM-003`, `TIM-007` | Both packets expose the actor's illumination, let light and sound alter hostile acquisition, preserve finite-ammunition live action through checkpoints and verify a reached mission state by reload. Metro Exodus adds environmental filter pressure, health recovery, freely controlled lights and a train escape. Splinter Cell instead centres analog-speed infiltration, restraint and interrogation, keypad and lock bypass, retinal cooperation, explicit alarm consequences and the relocation of an unconscious body to alter later discovery. | Tied near, `21 / 44 = 0.477273` |

### Preserved research notes

- New genes: `ACT-491`.
- Reused genes: `ACT-008`, `ACT-107`, `ACT-161`, `ACT-202`, `ACT-341`,
  `ACT-344`, `SYS-057`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-578`,
  `SYS-780`, `SYS-797`, `CON-077`, `CON-282`, `CON-285`, `CON-330`,
  `CON-335`, `INF-073`, `INF-075`, `INF-115`, `INF-125`, `INF-316`,
  `OBJ-155`, `TIM-003` and `TIM-007`.
- Classification result: `New gene`.
- Evidence and reasoning: all lower-ID boundaries transfer clause by clause.
  None permits an incapacitated actor to become an exclusive carried body,
  retain a recoverable world position and be quietly placed specifically to
  alter future discovery; heavy loot, living extraction subjects and ordinary
  inventory items are distinct rule objects.

## Taxonomy impact

- Registry changes: add Active `ACT-491`; add explicit carrier evidence to
  reused boundaries without changing their wording, lifecycle, earlier game
  signatures, combinations or family definitions.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_091`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_091.md).
- Candidate terms affected: Sam Fisher, Third Echelon, OPSAT, Stealth Meter,
  Training Course, Police Station, Defense Ministry, SC pistol, Lock Pick,
  Data Stick, keypad codes, retinal scanner, Wilkes, Xbox, `US-012` and
  `5553000C` remain product, actor, interface, item, place, serial or fixture
  parameters.

## Negative results

- No direct-play, disc, console, profile, checkpoint, executable, dump,
  emulator, screenshot, video or audio claim.
- The tempting claim that Police Station fails on its first alarm is rejected:
  the written evidence assigns that strict rule to the following Defense
  Ministry mission. The fixed Police Station route is alarm-free by choice.
- No special night-vision gene is added: the fixed route does not require a
  distinct information transformation beyond local sight/sound and the
  illumination meter.
- Interrogation reuses `ACT-107` because it registers an exact operational fact;
  retinal cooperation reuses contextual `ACT-341` because the restrained actor
  supplies the fixture prerequisite rather than a reusable new verb family.
- `ACT-359` is rejected because an unconscious person is neither bagged
  objective loot nor secured for payout. `ACT-466` is rejected because the body
  is not a living mission subject carried to extraction.
- No alarm-count, downloadable mission, thermal vision, SC-20K, lethal-clearance
  or later-campaign mechanics are inferred.

## Delta summary

## New facts

- [Confirmed | Direct | High] The Stealth Meter reports local light exposure,
  while analog speed, crouch, wall relation and shadow jointly alter stealth
  (`SC-002`, `SC-003`).
- [Confirmed | Direct | High] Dead or unconscious bodies retain a discoverable
  world position and can be carried and quietly placed (`SC-006`).
- [Observation | Corroborated | High] Training composes lock, code, retinal,
  camera/light, body and surface-noise lessons before Police Station uses them
  in one authored mission (`SC-008`, `SC-009`).

## New genes

- [Confirmed | Direct | High] `ACT-491` — carry and place one incapacitated
  world body.

## New combinations

- [Observation | Corroborated | High] No registered combination; this one new
  carrier does not independently establish recurrence for a shared subset.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_091` adds `ACT-491` and
  records complete lower-ID transfer decisions.

## New questions

- Does a later Splinter Cell mission justify a distinct finite alarm-budget
  constraint once the exact mission-specific threshold is bounded and tested?

## Next recommended game

- [Hypothesis | Corroborated | High] `GAME-0350` — Jet Set Radio.
- Optimisation criterion: test chained movement, tagging and territory pressure
  against the current traversal/action vocabulary.
- Expected information gain: distinguish authored rail/line momentum and
  graffiti-size input from generic platform movement and interaction.
- Backlog impact: seventh of nine selected games completed; two units remain.

## Why this game

- [Hypothesis | Corroborated | High] Jet Set Radio should replace patient
  concealment and body-state cleanup with expressive chained traversal, route
  scoring and pursuit pressure while preserving a strongly authored city route.
