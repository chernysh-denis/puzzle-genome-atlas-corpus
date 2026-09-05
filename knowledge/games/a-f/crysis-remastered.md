---
game_id: GAME-0246
slug: crysis-remastered
game_title: Crysis Remastered
analysis_status: reviewed
reviewed: 2026-09-04
combination_ids:
  - COMB-0244
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-202
    - ACT-403
    - ACT-405
    - ACT-420
  system:
    - SYS-215
    - SYS-222
    - SYS-369
    - SYS-373
    - SYS-737
    - SYS-747
    - SYS-771
  constraint:
    - CON-262
    - CON-282
    - CON-285
    - CON-590
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-287
    - INF-296
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Crysis Remastered

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1715130`, public Build ID `8139684`, built 2022-02-03, made public
  2022-02-08 and checked 2026-09-04. Crytek identifies that release as the last
  PC patch. Only a fresh single-player Campaign on `Normal`, default
  mouse/keyboard input and the explicitly restored `Classic Nanosuit menu` are
  admitted.
- Entry: choose Single Player, New Game and `Normal` on a clean profile. The
  packet begins at first retained control during the opening parachute descent
  in the first mission, `Contact`; its landing, suit recalibration, rendezvous,
  weapon-customisation, movement and binocular instructions are part of this
  fresh route rather than imported progression.
- Primary decision loop: read the current objective, terrain, weapon and
  magazine/reserve ammunition, health, active suit mode and shared energy,
  marked actors and directional detection state; walk, swim, sprint, jump,
  crouch, go prone or lean; select Speed, Strength, Armor or Cloak in the
  classic menu; allow the common energy reserve to recover; tag a visible
  hostile with binoculars; attach or remove the compatible silencer; aim,
  fire, switch, reload and collect compatible ammunition; trade concealment,
  protection and stronger traversal against mode-dependent energy drain; then
  follow the required authored gates to the mission transition.
- Positive terminal: follow the required route beyond the roadblock, use
  Strength-assisted jumps to reach the frozen ship sequence, regain control
  for `Find Jester`, reach the authored high ledge and allow `Contact` to
  transition. Retain the first ordinary `Recovery` control with `Capture the
  Communications Trailer` active, then stop before acting on it.
- Negative terminal: health reaching zero ends the current attempt. Continue
  from the latest authored mission checkpoint so failed transient position,
  energy, health, ammunition, perception, hostile and route state is replaced
  by the checkpoint state. Original-Crysis manual or quick saves are not
  imported into ordinary Crysis Remastered.
- Included: direct first-person traversal and posture; required Speed sprint
  and Strength jump demonstrations; deliberate Armor and Cloak use on the
  ordinary route; one shared suit-energy reserve with mode/action-dependent
  drain and automatic recharge; cloak loss on weapon fire; binocular marking
  and retained actor position; suspicion, detection and live firearm combat;
  compatible silencer switching; weapon switching, finite magazine/reserve
  ammunition, reload and compatible pickup; delayed health regeneration;
  authored checkpoints, objective order and the complete first-mission exit.
- Excluded: the optional GPS jammer and North Korean Command Post secondary
  objectives; boats, cars and other vehicle operation; exhaustive kills,
  pickups, weapons, attachments, grenades, thrown objects, destructible-world
  optimisation and exact enemy counts; night vision and its independent power;
  manual/quick saves from the original 2007 PC release; alternate controls and
  difficulties; Ray Tracing, DLSS and graphics modes; achievements; every
  `Recovery` action after retained entry, every later mission and the whole
  campaign; the original Crysis package, Warhead, Crysis 2/3, Trilogy bundles,
  consoles, mods, community save tools, cheats and the whole franchise.
- Reproducible parameterisation: use the English Windows public Steam branch,
  default mouse/keyboard bindings, a clean profile, `Normal` and the Classic
  Nanosuit menu. Follow only primary objectives. Deliberately select each of
  the four modes once in an eligible situation, let the shared reserve begin
  recharging, tag at least one visible hostile through binoculars, equip or
  remove the compatible silencer once, and complete required combat and route
  gates on foot. Exact approach, target, ammunition use, posture, mode timing,
  energy level, damage and completion time are run parameters.
- Potential scoped modules: one optional jammer objective, one command-post
  approach, one vehicle route, another mission, another difficulty or the
  alternate control scheme each requires a separate unit.
- Direct-play status: not conducted. Current Steam and Crytek textual sources
  establish the sold Windows product, final PC update, single-player/remaster
  boundary and restored Classic Nanosuit menu. Crytek's current product account
  and the official original PC manual together constrain inherited suit,
  weapon, HUD and checkpoint rules; static written route sources constrain the
  exact `Contact` transitions. No feature known to differ in Remastered is
  imported by analogy. This is evidence-backed rules reconstruction, not a
  claimed captured playthrough or local entitlement. No video or audio was
  opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CRYSISR-001` | The admitted product is Crytek's currently sold Windows Crysis Remastered Steam app `1715130`, not original Crysis or the Trilogy | Confirmed | Direct | High | P1, P2, P3 |
| `CRYSISR-002` | The public Windows branch is Build `8139684`, built 2022-02-03 and published 2022-02-08; Crytek calls the corresponding release the last PC patch | Observation | Corroborated | High | P3, S1 |
| `CRYSISR-003` | The remaster focuses the original single-player campaign and the current PC program includes original controls and the Classic Nanosuit menu as explicit options | Confirmed | Direct | High | P4, P5 |
| `CRYSISR-004` | The Nanosuit offers Speed, Strength, Armor and Cloak through one mode selection surface | Confirmed | Direct | High | P2, P5, P6 |
| `CRYSISR-005` | Mode and compatible action determine how a shared suit-energy reserve drains, while the reserve regenerates over time | Confirmed | Corroborated | High | P5, P6 |
| `CRYSISR-006` | Speed changes movement, Strength changes jump/aim/force, Armor spends energy before health and moving Cloak drains faster; firing while cloaked empties the reserve and exposes the actor | Confirmed | Corroborated | High | P5, P6 |
| `CRYSISR-007` | Binocular focus can bind a tracked position to a visible actor, while detection-risk and alert gauges expose local perception progress | Confirmed | Corroborated | High | P6 |
| `CRYSISR-008` | Compatible attachments can be changed in a live weapon-customisation surface, and firing, reload and pickup obey weapon/ammunition compatibility | Confirmed | Corroborated | High | P5, P6 |
| `CRYSISR-009` | Mission progress is autosaved at authored checkpoints and failure can replace the failed attempt with a saved route state | Confirmed | Corroborated | High | P6, S2 |
| `CRYSISR-010` | `Contact` begins with the parachute/tutorial route, requires rendezvous, landing-zone, roadblock, Strength-jump and frozen-ship gates, then ends after `Find Jester` at a high ledge | Observation | Corroborated | High | S2, S3, S4 |
| `CRYSISR-011` | The successor is retained first control in `Recovery` with `Capture the Communications Trailer` active | Observation | Corroborated | High | S2, S3 |
| `CRYSISR-012` | The bounded identity is a marked stealth/combat route whose four mutually exclusive capabilities compete for one visible rechargeable reserve | Strong Pattern | Corroborated | High | CRYSISR-004–CRYSISR-011 |

## Basic data

- Release / origin: Crytek, Crysis Remastered; Steam release 2021-09-17; the
  scoped public branch received its final PC patch 2022-02-08.
- Platform or physical form: lawfully available English Windows Steam
  distribution, application `1715130`; no direct entitlement is claimed.
- Puzzle family: tactical forecast and counterplay, real-time system pressure
  and ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-04:
  - `P1` — [Steam product](https://store.steampowered.com/app/1715130/CrysisRemastered/),
    for the current Windows sale, single-player product identity and exclusion
    of the separately offered Remastered Trilogy bundle.
  - `P2` — [Crytek: Crysis Remastered coming to Steam](https://www.crytek.com/news/crysis-remastered-coming-to-steam-next-month),
    for the Windows Steam product and its four named Nanosuit abilities.
  - `P3` — [Crytek: last Crysis Remastered PC patch](https://www.crytek.com/news/crysis-remastered-pc-patch-is-now-live),
    for the 2022-02-08 final PC patch, Steam availability and its stability and
    performance scope.
  - `P4` — [Crytek: Crysis Remastered announcement](https://www.crytek.com/news/crytek-announces-crysis-remastered),
    for the original single-player-campaign focus and remaster boundary.
  - `P5` — [Crytek: original controls and Classic Nanosuit menu](https://www.crytek.com/news/crysis-remastered-adds-dlss-support-for-pc),
    for those restored current PC options; graphics additions remain excluded.
  - `P6` — [official original Windows Crysis manual](https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/17300/manuals/manual_english.pdf?t=1736347865),
    used only as an inherited-mechanics reference corroborated by `P2`, `P4`
    and `P5`: Normal entry, movement/posture, four suit modes, shared energy,
    HUD, detection, binocular tags, weapon attachments/ammunition and authored
    checkpoints. Its manual/quick-save and multiplayer passages are excluded.
- Corroborating textual sources, accessed 2026-09-04:
  - `S1` — [SteamDB public depots](https://steamdb.info/app/1715130/depots/),
    for Windows depot `1715131`, public Build `8139684` and timestamps. SteamDB
    is a secondary distribution mirror, not the publisher.
  - `S2` — [GameFAQs Crysis Remastered written route](https://gamefaqs.gamespot.com/ps4/288051-crysis-remastered/faqs/51145),
    for required `Contact` objectives, high-ledge endpoint, `Recovery` handoff
    and successor objective; platform-specific controls are not admitted.
  - `S3` — [GameFAQs Crysis Remastered guide](https://gamefaqs.gamespot.com/switch/288049-crysis-remastered/faqs/63282),
    for the same mission/successor order; platform-specific controls are not
    admitted.
  - `S4` — [Gamepressure Contact route, part 7](https://www.gamepressure.com/crysis/mission-1-part-7/z1f5f),
    for the Strength-gated final approach and final target area.
  - `S5` — [GameSpot Crysis walkthrough](https://www.gamespot.com/articles/crysis-walkthrough/1100-6182906/),
    for independent written corroboration of the roadblock and final route.
- Claim IDs: `CRYSISR-001`–`CRYSISR-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly walk, swim, sprint and jump through the authored
  island route; `ACT-161`: aim and fire the active firearm at a reachable
  hostile; `ACT-164`: select a carried weapon; `ACT-183`: reload its magazine
  from compatible reserve; `ACT-202`: change standing, crouched, prone or lean
  posture; `ACT-403`: replace one compatible live weapon attachment; `ACT-405`:
  hold binocular focus on a visible actor to request a retained mark.
- New `ACT-420`: select one available powered personal capability mode during
  live control, replacing the previously active mode before the next movement,
  protection or concealment decision.
- Grenades, object throwing, vehicles, night vision and optional destruction
  are outside the packet. Suit, mode, weapon, attachment and target names are
  parameters. Claims: `CRYSISR-004`, `CRYSISR-007`, `CRYSISR-008`,
  `CRYSISR-010`.

### System Behaviour Genes

- Existing `SYS-215`: resolve live hostile perception, movement, aimed fire,
  damage and defeat; `SYS-222`: transfer compatible ammunition from a reachable
  weapon/pickup into carried reserve; `SYS-369`: replace a failed attempt with
  the latest authored mission checkpoint; `SYS-373`: escalate visible movement,
  bodies, sound or harm from suspicion through search to combat; `SYS-737`:
  reduce health under damage and begin automatic recovery after its quiet
  interval; `SYS-747`: retain a deliberately acquired actor-bound tactical mark
  through ordinary occlusion.
- New `SYS-771`: convert the selected powered mode and one shared rechargeable
  reserve into its temporary movement, strength, protection or concealment
  effect, applying the mode/action-dependent drain and later automatic refill.
- Resolution order: accept movement, posture, mode, optical, attachment,
  weapon or attack input; validate reach, visibility, compatibility and shared
  reserve; apply the selected temporary capability and energy debit; update
  marks and perception; resolve live combat, ammunition, health and quiet
  regeneration; save or restore checkpoints; then settle the ordered mission
  transition and retained successor.
- Claims: `CRYSISR-005`–`CRYSISR-011`.

### Constraint Genes

- Existing `CON-262`: carried weapon slots, magazines, reserve ammunition and
  any admitted equipment counts are finite; `CON-282`: rendezvous, landing
  zone, roadblock, Strength-jump, frozen ship, `Find Jester` and successor
  follow authored order; `CON-285`: fire, reload and attachment replacement
  require compatible current weapon, ammunition, slot and action state.
- New `CON-590`: a powered mode effect requires sufficient shared reserve and
  its compatible current action; exhaustion or a declared disqualifying action
  ends or changes the effect. In particular, movement changes Cloak drain and
  firing while cloaked exhausts the reserve and reveals the actor.
- Scarce strategic resources: suit energy, health, compatible magazine/reserve
  ammunition, concealment time, local cover and checkpoint-local progress.
  Exact rates, values and names remain parameters. Claims: `CRYSISR-005`,
  `CRYSISR-006`, `CRYSISR-008`–`CRYSISR-010`.

### Information Genes

- Existing `INF-073`: active weapon, magazine/reserve and attachment state are
  visible; `INF-115`: avatar-centred sight and explicit spatial effects expose
  only local hostiles; `INF-119`: health and current personal status are
  visible; `INF-125`: terrain, current objective and authored route markers are
  inspectable; `INF-287`: binocular marks and directional detection progress
  distinguish tracked, suspicious and detected actors.
- New `INF-296`: the personal capability interface exposes the currently
  selected mode and common energy reserve, including ongoing depletion and
  recharge, before the next mode/action choice.
- Exact icon, colour, number, gauge placement and official mode names are
  presentation parameters. Claims: `CRYSISR-004`–`CRYSISR-008`,
  `CRYSISR-010`.

### Objective Genes

- Existing `OBJ-026`: traverse the required authored route to the designated
  high-ledge exit and retain first control plus the active successor objective.
- One tag, combat victory, roadblock, optional jammer or arbitrary quiet
  location is not success. Death/checkpoint retry closes the failed attempt;
  `Recovery` entry after the complete first-mission transition is the positive
  terminal. Claims: `CRYSISR-009`–`CRYSISR-011`.

### Time Genes

- Existing `TIM-003`: movement, energy drain/recharge, perception, hostile
  action, firing, health recovery and mode opportunities progress continuously
  while the player chooses actions.
- Menu/loading boundaries do not add another decision clock. Claims:
  `CRYSISR-005`–`CRYSISR-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Clean profile, New Game and `Normal` are selected | Accept first retained control during the parachute descent | `Contact` begins with its authored tutorial state and no imported equipment history | fixed entry and product scope | `CRYSISR-001`, `CRYSISR-003`, `CRYSISR-010` |
| One powered mode is active and another is available | Open the Classic Nanosuit menu and select the other mode | The selected mode replaces the previous one and changes the next compatible capability | direct mutually exclusive mode authority | `CRYSISR-003`, `CRYSISR-004` |
| Speed is selected with available energy | Sprint, then stop enhanced use | Movement accelerates while the shared reserve drains; eligible inactivity begins its refill | mode-dependent movement exchange | `CRYSISR-005`, `CRYSISR-006` |
| Strength is selected before a required high ledge | Commit an eligible high jump | The stronger jump spends shared energy and crosses the otherwise unavailable height relation | powered traversal gate | `CRYSISR-005`, `CRYSISR-006`, `CRYSISR-010` |
| Armor is selected before eligible incoming damage | Remain exposed to one bounded hit | Suit energy absorbs the eligible damage before health until the reserve is insufficient | common reserve as temporary protection | `CRYSISR-006` |
| Cloak is selected with available energy | Move unseen, then fire once | Movement accelerates drain; firing empties the reserve and immediately removes concealment | action-qualified stealth commitment | `CRYSISR-006`, `CRYSISR-007` |
| One eligible hostile is clearly visible through binoculars | Hold focus until the tag settles | A tracked marker binds to the actor and remains available through ordinary occlusion | observation changes later information | `CRYSISR-007` |
| A compatible silencer slot is available on the current weapon | Replace its current muzzle attachment in the live customisation surface | The weapon immediately gains the chosen compatible attachment state for later shots | live loadout reconfiguration | `CRYSISR-008` |
| A hostile perceives visible movement, sound, a body or harm | Remain exposed, move, hide or attack | Suspicion progresses into search/combat or decays according to local perception and concealment | recoverable stealth-to-combat transition | `CRYSISR-007` |
| Health reaches zero before the mission transition | Continue from the latest authored checkpoint | The failed transient state is replaced by the authored retry state | reproducible negative terminal | `CRYSISR-009` |
| `Find Jester` is active after the frozen-ship event | Follow the objective marker to the high ledge and let the transition settle | `Contact` closes and first controllable `Recovery` state exposes `Capture the Communications Trailer` | reproducible positive terminal | `CRYSISR-010`, `CRYSISR-011` |

## Strategic and experiential structure

- Planning horizon: choose whether limited shared energy is more valuable for
  a faster crossing, stronger jump, damage interception or concealment before
  the next sightline, then preserve enough recovery time for the following
  gate.
- Local tactics: mark before committing, fit the silencer when quiet fire is
  useful, move slowly under Cloak, switch to Armor when detection completes,
  and manage reload and health-recovery windows without assuming invisibility
  survives a shot.
- Medium-term structure: the authored route alternates tutorial gates, open
  approaches, perception/combat pockets and powered traversal, then settles a
  named mission transition rather than an arbitrary sandbox pause.
- Failure attribution: visible mode/energy, health, ammunition, tags,
  directional detection and objective markers distinguish reserve exhaustion,
  exposure, poor combat state, incompatible equipment and route confusion.
- Player-trust factors: one visible reserve governs every admitted mode; the
  same qualifying action has the same drain/reveal consequence; the authored
  checkpoint replaces failure and the successor objective confirms completion.
- Claim IDs: `CRYSISR-004`–`CRYSISR-012`.

## Replay and variation

- What changes between attempts: movement path, approach posture, marked
  actors, mode order and duration, detection, target/weapon choice, ammunition,
  damage, health-recovery timing and checkpoint use.
- Randomness or procedural generation: the mission geometry, primary gates and
  transition are authored; continuous patrol/perception/combat trajectories
  vary within that fixed route.
- Multiple viable strategies: remain mostly concealed, use open firearm
  combat, or alternate them while the same primary gates and terminal remain.
- Typical replay motive: optional objectives, vehicles, difficulty and
  destructible-world experimentation are real surfaces but excluded here.
- Claim IDs: `CRYSISR-005`–`CRYSISR-011`.

## Adjacent systems and history

- Direct predecessor: original Crysis supplies the inherited campaign design,
  but its package, manual saves and implementation are not silently merged
  into the remaster.
- Variants: the remaster's original/current control options and graphics modes
  change interaction or rendering configuration; this packet fixes Classic
  Nanosuit menu and excludes graphical benchmarking.
- Similar lower-ID games: Far Cry 3 shares optical actor marking, retained
  marks, posture, local suspicion and live gun combat; DOOM (2016), Serious Sam
  HD and Half-Life share authored first-person mission routes and checkpoint or
  resource pressure.
- Important differences: one rechargeable reserve dynamically selects among
  traversal, protection and concealment effects, and firing under Cloak is a
  visible resource-and-detection commitment rather than generic stealth.
- Claim IDs: `CRYSISR-001`, `CRYSISR-003`–`CRYSISR-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-202`, `ACT-403`, `ACT-405`, `ACT-420` | route, posture, weapon, attachment, actor and mode names |
| System Behaviour | `SYS-215`, `SYS-222`, `SYS-369`, `SYS-373`, `SYS-737`, `SYS-747`, `SYS-771` | energy rates, perception, combat, health and checkpoint |
| Constraint | `CON-262`, `CON-282`, `CON-285`, `CON-590` | compatibility, gate order, energy and disqualifying action |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-287`, `INF-296` | HUD art, mode, reserve, marks, threat and objective |
| Objective | `OBJ-026` | final high ledge and retained successor control |
| Time | `TIM-003` | continuous unpaused simulation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `245` (`GAME-0001`–`GAME-0245`).
- Exact genome matches: none.
- Tied near matches: `GAME-0236` — Far Cry 3 (`19 / 38 = 0.500000`).
- Supported combination subsets: `COMB-0244`.
- Scan date: 2026-09-04.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0236` — Far Cry 3 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-202`, `ACT-405`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-747`, `CON-262`, `CON-282`, `CON-285`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-287`, `TIM-003` | Far Cry 3 adds inert diversion, unaware takedown, finite carried healing, mission-critical ally risk and persistent hostile-site conversion. Crysis instead adds live attachment replacement, compatible ammunition collection, delayed health regeneration, four mutually exclusive powered capabilities drawing on one visible shared reserve and a fixed first-mission route terminal. | Near, `0.500000` |

### Preserved research notes

- New genes: `ACT-420`, `SYS-771`, `CON-590`, `INF-296`.
- Reused genes: `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-202`,
  `ACT-403`, `ACT-405`, `SYS-215`, `SYS-222`, `SYS-369`, `SYS-373`,
  `SYS-737`, `SYS-747`, `CON-262`, `CON-282`, `CON-285`, `INF-073`,
  `INF-115`, `INF-119`, `INF-125`, `INF-287`, `OBJ-026`, `TIM-003`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: lower-ID labels already cover embodied traversal,
  posture, firearm/equipment operations, actor marking, suspicion, live combat,
  health/checkpoint state and authored completion. The new boundaries isolate
  the live mutually exclusive mode command, its shared rechargeable reserve
  and temporary capability conversion, its action/resource legality and the
  specific visible mode/reserve state. Mission, character, mode and rate names
  remain parameters.
- Lower-ID scan: reject `ACT-393` and `SYS-724` because they continuously
  allocate starfighter power across three simultaneous subsystems rather than
  selecting one personal mode; reject `SYS-237` because it joins mecha travel,
  construction, fabrication and combat to a fuel/charger economy; reject
  `SYS-368` because it models one protagonist-specific activated ability, not
  four mutually exclusive effects sharing a reserve; reject `ACT-370` because
  a sensory mode is not selected; reject `SYS-655` because ordinary armour
  capacity/restoration is not the mode-selected shared reserve; reject manual
  saves, night-vision power, vehicle, destruction and optional-objective genes.

## Taxonomy impact

- Registry changes: add `ACT-420`, `SYS-771`, `CON-590` and `INF-296` with
  portable capability/resource language and game-scoped examples; no existing
  definition, lifecycle or reviewed signature changes.
- Taxonomy-change record: none.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; Crysis,
  Nanosuit, Speed, Strength, Armor, Cloak, Contact, Recovery, actor, weapon,
  rate, energy quantity, difficulty and objective names remain parameters.

## Negative results

- No direct play or local entitlement claim; no video/audio evidence.
- No optional jammer, command-post, vehicle, grenade, destruction, manual-save,
  graphics, achievement, later-mission or whole-campaign gene is admitted.
- No earlier reviewed signature, definition or lifecycle state changes.

## Combination subset scan

- Every verified combination in the pre-unit registry was tested as a proper
  subset of the 27-gene signature. None fit completely. `COMB-0244` is added as
  the strict marked-approach/shared-mode-energy core and omits general weapon,
  health, checkpoint and route-support information.
- Comparison and subset scan date: 2026-09-04.

## Delta summary

## New facts

- [Confirmed | Direct | High] Current lawful product, final PC branch and
  explicit Classic Nanosuit menu are fixed in `CRYSISR-001`–`CRYSISR-003`.
- [Confirmed | Corroborated | High] Four selected capabilities, one common
  energy reserve, marking, perception, weapon compatibility and checkpoint
  rules are bounded in `CRYSISR-004`–`CRYSISR-009`.
- [Observation | Corroborated | High] The complete `Contact` route and retained
  `Recovery` objective form the terminal in `CRYSISR-010`–`CRYSISR-011`.

## New genes

- [Confirmed | Corroborated | High] `ACT-420`, `SYS-771`, `CON-590` and
  `INF-296` isolate portable mode-selection, shared-resource, legality and
  information boundaries without branded canonical labels.

## New combinations

- [Observation | Corroborated | High] `COMB-0244` captures a marked live
  approach in which mutually exclusive traversal, protection and concealment
  capabilities compete for one rechargeable reserve.

## Taxonomy changes

- [Observation | Corroborated | High] None; no prior signature, definition or
  lifecycle state changes.

## New questions

- Does Dishonored's bounded first-mission packet reuse detection-aware authored
  traversal while replacing shared powered modes with mana, vertical access
  and irreversible objective consequences?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0247` — Dishonored (2012).
- Optimisation criterion: hold first-person stealth/combat and authored mission
  order near-constant while testing a different capability and consequence
  economy.
- Expected information gain: distinguish rechargeable mode substitution from
  learned powers, mana use and mission-state settlement.
- Backlog impact: advances the approved batch-013 ordered horizon.

## Why this game

- [Hypothesis | Limited | High] Dishonored preserves embodied infiltration and
  local awareness while changing the resource, route and terminal grammar.
