---
game_id: GAME-0355
slug: metroid-prime
game_title: Metroid Prime
analysis_status: reviewed
reviewed: 2026-09-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-190
    - ACT-202
    - ACT-313
    - ACT-494
  system:
    - SYS-215
    - SYS-578
    - SYS-972
    - SYS-982
  constraint:
    - CON-068
    - CON-269
    - CON-402
    - CON-578
  information:
    - INF-073
    - INF-119
    - INF-125
    - INF-368
  objective:
    - OBJ-205
  time:
    - TIM-003
---

# Game: Metroid Prime

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Samus Aran,
Frigate Orpheon, Tallon IV, Parasite Queen, Meta Ridley, Scan Visor, Combat
Visor, Power Beam, Charge Beam, Missile Launcher, Morph Ball, Grapple Beam and
Varia Suit are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: the original North American English Nintendo GameCube
  revision `DOL-GM8E-0-00`, represented in the pinned PrimeDecomp
  `GM8E01_00` configuration. It is not later North American revision `0-01` or
  `0-02`, the Japanese or PAL release, Metroid Prime Trilogy, Metroid Prime
  Remastered, a randomizer, sequence-break ruleset or later Metroid title.
- Structured analysis target: one fresh English New Game from first ordinary
  control after Samus docks at Frigate Orpheon's exterior air lock through the
  first ordinary player-controlled state after her gunship lands in Tallon
  Overworld on Tallon IV; see `GAME-0355` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: the new file supplies the authored prologue loadout: Power and Varia
  suit state, Power and Charge Beams, Combat and Scan Visors, missiles, Morph
  Ball, Morph Ball Bombs, Grapple Beam and Space Jump Boots. No earlier scan,
  damage, pickup, timer, save or route state exists.
- Fixed reproducible route: release the exterior force field by shooting its
  four points and scanning the control; enter the ship; scan the first mapped
  terminals that operate lifts and doors; use Morph Ball at the required
  hologram and compact ventilation route; use Power Beam, one charged shot and
  finite missiles against required turrets and Parasite Queen; scan the Queen
  so the head weakness and corresponding target lock are disclosed; keep the
  Queen locked while orbiting and side-dashing around the rotating reactor
  field; defeat it; escape under the visible `07:00` countdown; scan the
  required elevator and turret controls; roll through the revealed ventilation
  path; lock to Grapple nodes and swing over the gap; survive the authored
  hull collision that disables Varia Suit, Charge Beam, missiles, Morph Ball,
  Morph Ball Bombs, Grapple Beam and Space Jump Boots while retaining the base
  Power Suit, Power Beam, Combat Visor and Scan Visor; leave the air lock,
  board the gunship and regain control after landing on Tallon IV.
- Primary decision loop: read the first-person HUD and local map; choose Combat
  or Scan Visor; hold a valid target long enough to obtain information or
  settle its typed fixture response; navigate by direct movement, jumping or
  temporary compact form; lock a hostile or Grapple node; move, orbit, dash,
  fire the beam or spend a missile; preserve Energy and escape time; then
  continue with the reduced capability set produced by the authored accident.
- Positive terminal: the Orpheon escape has settled, the authored equipment
  malfunction is retained, the gunship transition has finished and ordinary
  control begins in Tallon Overworld with Power Suit, Power Beam, Combat Visor
  and Scan Visor usable. Taking a first Tallon IV step is sufficient; scanning,
  saving, fighting or collecting anything there is outside the packet.
- Failure paths: Energy reaching zero causes Game Over; letting the escape
  countdown reach zero before exiting the frigate fails the attempt. Loading,
  Continue and Save Station recovery are not exercised and add no genes.
- Included: first-person movement, jumping and free look; Combat/Scan Visor
  switching; target lock, orbit and side dash; beam fire, one charge/release
  and finite missile use; direct hostile damage; Energy and zero-Energy
  failure; Morph Ball configuration; one Grapple traversal; held scans whose
  completed target determines information, weak-point lock or a fixture
  response; local radar/HUD/map state; Parasite Queen clearance; seven-minute
  evacuation; the scripted reduced-loadout event and landed successor control.
- Reproducible parameterisation: ordinary enemy contacts, damage, remaining
  Energy and missiles, scan order beyond the required fixtures, Queen attack
  timing and exact movement line may vary. The required controls, Queen defeat,
  seven-minute escape, Grapple crossing, malfunction set, retained base set and
  Tallon IV landing do not.
- Excluded: optional Log Book completion, optional Map and Save Stations,
  optional pickups and refills, 100% scans, speedrun missile-cancel technique,
  out-of-bounds and sequence breaks; Chozo Ruins and all later Tallon IV areas,
  reacquisition of lost abilities, artefacts, later bosses and final ending;
  Fusion bonuses, later revisions, ports, remasters, cheats, mods and
  randomizers.
- Direct-play status: not conducted. No disc, image, GameCube, emulator,
  controller trace, save, screenshot, video or audio was obtained or inspected.
  The official manual, pinned reverse-engineered source and independent written
  route support a bounded rules reconstruction rather than a claimed
  playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MPR-001` | The packet targets original North American GameCube revision `DOL-GM8E-0-00`, represented by PrimeDecomp configuration `GM8E01_00`, not a later revision or remaster | Confirmed | Corroborated | High | P1, R1, R2 |
| `MPR-002` | Holding Scan Visor focus on an eligible in-range locked target advances scan progress to completion | Confirmed | Direct | High | P1, R1 |
| `MPR-003` | A completed scan may disclose ordinary data, retarget Parasite Queen to its head weakness, or trigger the addressed terminal's door, lift or turret response | Observation | Corroborated | High | P1, R1, S1 |
| `MPR-004` | Combat lock maintains one target while movement becomes target-relative orbiting and the jump input becomes a lateral dash | Confirmed | Direct | High | P1, R1 |
| `MPR-005` | Missiles consume finite reserve and home toward a current lock; a held Power Beam shot charges before release | Confirmed | Direct | High | P1, R1 |
| `MPR-006` | Morph Ball changes Samus into a compact directly moved body, while Grapple Beam requires a specific reachable energy node and carries a swing across the prologue gap | Confirmed | Corroborated | High | P1, S1 |
| `MPR-007` | Defeating Parasite Queen starts a visible seven-minute authoritative evacuation whose expiry fails the attempt | Observation | Corroborated | High | S1, V1 |
| `MPR-008` | The escape route reuses scans, Morph Ball, combat and Grapple Beam before an unavoidable collision disables seven declared capabilities but preserves Power Suit, Power Beam and both starting visors | Observation | Corroborated | High | R1, S1, V1 |
| `MPR-009` | The bounded prologue closes only when Tallon IV landing restores ordinary control with the reduced capability set | Observation | Corroborated | High | P2, S1, V1 |
| `MPR-010` | HUD and maps expose Energy, missiles, radar threats, active visor/weapon and explored room state without revealing unscanned facts or the future route | Confirmed | Direct | High | P1, R1 |
| `MPR-011` | The signature admits only transitions causally exercised by the fixed air-lock-to-landing route | Observation | Direct | High | P1, P2, R1, R2, S1, V1 |

## Basic data

- Release / origin: Retro Studios / Nintendo, original North American
  Nintendo GameCube action-adventure. Nintendo's preserved product page names
  Retro Studios and the Combat/Scan Visor, weapon, Morph Ball and capability-
  led exploration premise.
- Platform or physical form: original licensed North American English
  Nintendo GameCube optical-disc ruleset, revision `GM8E 0-00`; no disc image
  was acquired or executed.
- Puzzle family: real-time system pressure; inventory and fixture dependencies;
  world topology and perspective; ordered dependency sequencing.
- Primary sources, accessed 2026-09-22:
  - **[P1]** [Nintendo of America's original English Metroid Prime
    manual](https://csassets.nintendo.com/noaext/image/private/t_KA_PDF/GCN_Metroid_Prime?_a=DATC1RAAZAA0),
    pp. 5–14, for New Game and Save boundaries, controls, target lock, HUD,
    visors, map, Power/Charge Beam, Morph Ball, Grapple Beam and finite homing
    missiles. Local PDF SHA-256:
    `4b7b0a918fb8cdbd158f71177eb4e0309ae82a2285960f45aa2262b4bfd4c3b0`.
  - **[P2]** [Nintendo's preserved Metroid Prime product
    page](https://www.nintendo.com/en-gb/Games/Nintendo-GameCube/Metroid-Prime-268423.html),
    for GameCube/Retro Studios identity and the official Combat/Scan Visor,
    weapons, Morph Ball, Tallon IV and ability-led exploration description.
- Reproducible sources:
  - **[R1]** [`PrimeDecomp/prime` at commit
    `c6f63949`](https://github.com/PrimeDecomp/prime/tree/c6f63949ed08a08fbf1cec458479358a1721a9a0),
    configuration `GM8E01_00`, for exact target identity; player power-up,
    visor, scan-progress, orbit, Grapple, charge and finite-missile rules. This
    is community reverse engineering and contains no copyrighted game assets.
  - **[R2]** [metroid2002 version-number
    record](https://www.metroid2002.com/version_differences_version_number.php),
    for `DOL-GM8E-0-00` as the original North American `0-00` revision rather
    than later `0-01`/`0-02` builds.
  - **[S1]** [Omega Metroid's written Frigate Orpheon
    route](https://omegametroid.com/metroid-prime-walkthrough/frigate-orpheon/),
    for the required force-field/terminal scans, Morph Ball gates, Parasite
    Queen weak-point retargeting, seven-minute escape, Grapple crossing,
    declared malfunction set and return to the exterior air lock.
- Validation source: **[V1]**
  [`verify_metroid_prime_control.py`](../../../scripts/verify_metroid_prime_control.py),
  an executable source-model reconstruction of the bounded state relations. It
  does not run Metroid Prime.
- Claim IDs: `MPR-001`–`MPR-011`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly move, jump, free-look and steer the temporary compact
  body through the authored frigate geometry. Camera and avatar are parameters.
- `ACT-161`: aim and fire the Power Beam, hold and release one charged shot or
  spend a missile against an eligible turret, hostile, Queen weak point or
  force-field point.
- `ACT-190`: commit the currently available Grapple Beam to one legal node and
  hold the resulting swing channel until release across the required gap.
- Generalised `ACT-202`: change between ordinary and Morph Ball body
  configurations while that capability remains enabled.
- Generalised `ACT-313`: switch to Scan Visor, keep one eligible world target
  locked and in range, then hold the scan command to advance target-specific
  progress.
- New `ACT-494`: hold one eligible target lock so movement or dash input is
  interpreted relative to that target instead of free facing.
- Claims: `MPR-002`–`MPR-006`.

### System Behaviour Genes

- `SYS-215`: resolve directly commanded beam, charge, missile and contact
  combat while enemies, reactor barriers and hazards continue in real time.
- `SYS-578`: enemy attacks and hazards reduce one continuous Energy pool; zero
  is terminal. Optional refill pickups are excluded from the fixed route.
- Generalised `SYS-972`: the authored hull collision removes a declared set of
  acquired capability states while preserving the living character, base
  loadout, ordinary control and the later reacquisition model.
- New `SYS-982`: completion of an eligible held scan commits the target's typed
  response: disclose stored information, change a supported combat lock to a
  disclosed weak point, or apply the addressed door/lift/turret control state.
- Resolution order: scan fixture or target; traverse and fight with the current
  loadout; Queen defeat starts evacuation; required scans, compact traversal
  and Grapple resolve under the deadline; the scripted collision replaces the
  capability set; escape and gunship transition restore control on Tallon IV.
- Claims: `MPR-002`–`MPR-010`.

### Constraint Genes

- `CON-068`: the authoritative evacuation allowance begins at `07:00` and
  reaching zero before the frigate exit ends the attempt unsuccessfully.
- `CON-269`: Scan, Morph Ball, Grapple, charge and missile requests require the
  corresponding enabled capability plus their legal target, range, resource or
  body context; lost capabilities reject later input after the collision.
- `CON-402`: Parasite Queen remains the finite hostile clearance required to
  settle the reactor encounter and begin the escape phase.
- `CON-578`: missiles may fire only while compatible finite reserve pays each
  shot; the default Power Beam remains ammunition-free.
- Scarce route state: Energy, missiles, remaining escape time, enabled
  capability set, scan completion/fixture flags, Queen state and exit state.
- Claims: `MPR-003`, `MPR-005`–`MPR-009`.

### Information Genes

- `INF-073`: the HUD exposes current missile reserve and whether the missile
  launcher or compatible ordinary weapon state is active.
- `INF-119`: Energy, current visor/beam and retained suit capabilities are
  visible or inspectable before combat and traversal decisions.
- `INF-125`: radar, local minimap and full map expose current position, nearby
  threats, visited rooms and known exits without disclosing unvisited topology.
- New `INF-368`: Scan Visor highlights eligible targets, exposes held progress
  and presents the completed target's authored data, weakness or fixture
  consequence without disclosing unscanned targets in advance.
- Claims: `MPR-002`, `MPR-003`, `MPR-010`.

### Objective Genes

- New `OBJ-205`: clear Parasite Queen, reach the frigate exit before the
  evacuation deadline, survive the authored capability malfunction and regain
  ordinary control after Tallon IV landing with the declared reduced loadout.
- Success, evaluation and failure: Queen defeat or exiting the ship alone is
  insufficient; landing control with the reduced set must settle. Zero Energy
  or escape-time expiry fails the attempt.
- Claims: `MPR-007`–`MPR-009`.

### Time Genes

- `TIM-003`: movement, target lock, scan progress, charge, combat, hazards and
  evacuation countdown all advance on the shared real-time clock.
- Claims: `MPR-002`, `MPR-004`, `MPR-005`, `MPR-007`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| An eligible control symbol is visible in Scan Visor | lock it and hold scan to completion | target progress reaches its threshold and the addressed force field, lift, door or turret response settles | scan-gated fixture | `MPR-002`, `MPR-003` |
| Parasite Queen is unscanned | complete its creature scan | the head weakness is disclosed and later target lock defaults to that supported weak point | scan changes combat information and lock | `MPR-003` |
| Queen is locked and a barrier gap is moving | steer around the lock or tap lateral dash, then fire through a legal gap | Samus keeps target-relative facing; accepted beam or missile damage reduces the Queen's finite state | target-relative combat | `MPR-004`, `MPR-005` |
| Queen reaches defeat | settle the encounter | reactor failure begins and the visible evacuation allowance becomes `07:00` | deadline phase transition | `MPR-007` |
| Escape route reaches the ventilation opening | enter Morph Ball and roll through | compact body clearance makes the authored path traversable | temporary capability-gated topology | `MPR-006`, `MPR-007` |
| Reachable Grapple nodes span the escape gap | lock a node, hold Grapple and release beyond the gap | the beam constrains a swing about the legal node and crossing continues | ability-target traversal | `MPR-006` |
| The scripted hull explosion occurs | continue through the unavoidable collision | Varia Suit, Charge Beam, missiles, Morph Ball, Bombs, Grapple and Space Jump become disabled; Power Suit, Power Beam and both starting visors remain | authored nonterminal capability reset | `MPR-008` |
| Air lock is reached before zero | cross outside and board the gunship | frigate escape settles and the authored flight transition begins | escape terminal precursor | `MPR-007`, `MPR-009` |
| Gunship reaches Tallon Overworld | finish the landing transition | ordinary control resumes with the reduced capability set still authoritative | scoped positive terminal | `MPR-009` |

## Strategic and experiential structure

- Local decision: choose visor; distinguish a scan point from a combat target;
  maintain range and lock; orbit or dash around an attack and moving barrier;
  spend a missile or use the unlimited beam; align compact or Grapple movement.
- Medium-term planning: reserve enough Energy and missiles for Queen, remember
  which coloured scan points operate the return route and execute scan, Morph
  Ball and Grapple steps without wasting the seven-minute allowance.
- Long-term structure: the prologue first exposes a broad traversal/combat
  vocabulary, then removes most of it and lands the same character in an open
  successor where reacquisition can structure the later game. That later
  reacquisition is outside this packet.
- Decision texture: alternating Combat and Scan Visors changes what can be
  targeted and learned; lock-on makes three-dimensional combat legible through
  target-relative motion; the evacuation reuses taught abilities under time;
  the forced reset makes capability loss, not reward growth, the terminal.

## Replay and variation

- What changes between attempts: ordinary enemy positions, damage, remaining
  Energy and missiles, scan order outside required fixtures, Queen attack
  timing and the exact escape movement line may vary.
- Randomness or procedural generation: the frigate rooms, required terminals,
  Queen arena, seven-minute evacuation, Grapple gap, collision event and Tallon
  landing are authored. No procedural layout or random objective is claimed.
- Multiple viable strategies: the bounded route permits different beam,
  missile, orbit and dash timing, plus optional scans and pickups, but every
  accepted completion still clears the Queen, traverses the same required
  capability gates and reaches Tallon IV after the same declared loss event.
- Typical replay motive: faster evacuation, fewer hits, lower missile spend or
  additional Log Book entries. None changes the packet terminal or creates a
  score or completion-percentage gene.
- Claims: `MPR-003`–`MPR-010`.

## Adjacent systems and history

- Direct series relation: the reviewed *Super Metroid* packet shares direct
  movement, beam combat, Morph Ball, finite missiles, health, maps and
  capability-gated traversal, but not this first-person visor scan, held target
  relation or authored prologue loadout removal.
- Variants: later North American GameCube revisions, Japanese and PAL builds,
  Trilogy, Remastered and randomizers are not assumed mechanically identical.
  Their control, content and wrapper changes require separate evidence.
- Similar games: the reviewed *Halo: Combat Evolved Anniversary* packet shares
  first-person live combat, finite ammunition, health information and local
  navigation, while *Castlevania: Symphony of the Night* supplies the earlier
  authored equipment-removal boundary. Neither combines them with this typed
  held-scan result and target-relative movement.
- Important difference: Scan Visor progress is an action on one eligible world
  target whose completed authored result may be information, target remapping
  or fixture control. It is not merely a decorative codex entry or a pulse
  that instantly reveals every nearby object.
- Claims: `MPR-001`–`MPR-006`, `MPR-008`, `MPR-010`.

## Edge cases and exceptions

- Scan progress is target- and range-dependent. Dropping a valid lock or
  leaving range interrupts the current attempt according to the selected build;
  a completed scan is not equivalent to merely highlighting the target.
- Parasite Queen's head retargeting is admitted only after the fixed route
  completes its scan. External knowledge of the weakness does not set that
  state.
- A Grapple node is a legal ability target, not evidence that arbitrary
  geometry can be tethered. Falling into the small pit does not end the attempt
  while the node remains reachable.
- Missiles are finite and homing under lock, but the unlimited Power Beam can
  still settle ordinary shots. Optional missile/health drops add no signature
  because the fixed route does not depend on taking them.
- The accident is unavoidable and nonterminal. It does not erase the character
  or every capability, and it is not voluntary unequipping, death-drop,
  durability break or temporary debuff expiry.
- The terminal is the first controllable Tallon IV state, not the preceding
  cinematic, the air-lock exit, a save write or later Chozo Ruins progress.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-202`, `ACT-313`, `ACT-494` | Samus, beam names, visor names, Grapple nodes and exact inputs are parameters |
| System Behaviour | `SYS-215`, `SYS-578`, `SYS-972`, `SYS-982` | enemy types, Energy values, removed capabilities and scan response class are parameters |
| Constraint | `CON-068`, `CON-269`, `CON-402`, `CON-578` | seven minutes, range, Queen health, missile count and enabled capability set are parameters |
| Information | `INF-073`, `INF-119`, `INF-125`, `INF-368` | HUD styling, map projection, marker colour and target text are presentation parameters |
| Objective | `OBJ-205` | guardian, ship exit, removed set and successor landing are parameters |
| Time | `TIM-003` | frame cadence and exact event timing are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `354` (`GAME-0001`–`GAME-0354`).
- Exact genome matches: none.
- Tied near matches: `GAME-0337` — Super Metroid (`12 / 29 = 0.413793`).
- Supported combination subsets: none.
- Scan date: 2026-09-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0337` — Super Metroid | `ACT-008`, `ACT-161`, `ACT-202`, `SYS-215`, `SYS-578`, `CON-068`, `CON-402`, `CON-578`, `INF-073`, `INF-119`, `INF-125`, `TIM-003` | Both packets combine direct movement, beam combat, Morph Ball, finite missiles, one health reserve, a deadline, finite hostile clearance, HUD state, local threats/maps and shared real time. Metroid Prime adds Grapple traversal, held visor analysis, target-relative lock movement, typed scan results, authored capability removal and the complete reduced-loadout landing objective; Super Metroid adds weapon selection, contact pickup, directional attack gates, room refresh, save restoration, full boss-area clearance and a different terminal. | Near, `12 / 29 = 0.413793` |

- New genes: `ACT-494`, `SYS-982`, `INF-368` and `OBJ-205`.
- Classification result: New gene and generalised gene.
- Evidence and reasoning: no lower-ID boundary owns retained target-relative
  movement, one held scan branching by target-authored result or an objective
  that requires both forced capability loss and reduced successor control.
  `ACT-313` and `SYS-972` broaden without changing their operational identity.

### Preserved research notes

- New genes: `ACT-494`, `SYS-982`, `INF-368` and `OBJ-205`.
- Classification result: New gene and generalised gene.
- Evidence and reasoning: no lower-ID boundary owns retained target-relative
  movement, one held scan branching by target-authored result or an objective
  that requires both forced capability loss and reduced successor control.
  `ACT-313` and `SYS-972` broaden without changing their operational identity.
- Generalised genes: `ACT-313` now covers a held in-range analyser whose
  completed result is typed rather than only blueprint-resumable; `SYS-972`
  now covers an authored removal of equipped items or acquired capabilities
  while living control and the replacement/reacquisition model continue.

## Taxonomy impact

- Registry changes: add four Active definitions, generalise two existing
  definitions and add complete reviewed Ukrainian coverage while preserving
  every earlier signature and lifecycle.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_094`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_094.md).
- Candidate terms affected: retain Samus, visor, beam, suit, Queen, frigate,
  Tallon IV, exact timer and exact removed loadout as carrier parameters.

## Negative results

- No generic “metroidvania”, “first-person adventure”, “boss”, “tutorial” or
  “ability gate” gene is created. Every admitted boundary owns a reproducible
  state transition.
- Charge Beam, missiles, Morph Ball and Grapple Beam reuse existing command or
  constraint genes; their product names and exact controls remain parameters.
- Scan result is not split into separate data, weak-point and terminal genes:
  one target-authored typed settlement owns the common completed-scan event.
- The collision does not create seven loss genes. One authored set-removal
  system owns the declared disabled and retained capability sets.
- Optional Log Book completion, Map/Save Stations, pickups, speedrun
  techniques, sequence breaks, later reacquisition and whole-game completion
  are excluded and add no genes.
- No direct play, disc, image, emulator, screenshot, video, audio or port
  parity is claimed.

## Delta summary

## New facts

- [Confirmed | Direct | High] Held Scan Visor analysis and Combat Visor lock
  have distinct progress and target-relative movement semantics in the exact
  original North American revision (`MPR-002`, `MPR-004`).
- [Observation | Corroborated | High] The prologue composes Queen clearance,
  seven-minute evacuation, required capability reuse, a forced capability-set
  loss and reduced-loadout Tallon IV control (`MPR-003`, `MPR-007`–`MPR-009`).

## New genes

- [Observation | Corroborated | High] Add `ACT-494`, `SYS-982`, `INF-368` and
  `OBJ-205` under `TAXONOMY_CHANGE_094`.

## New combinations

- [Observation | Direct | High] No verified combination is registered from one
  new carrier.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_094` generalises
  `ACT-313` and `SYS-972`, adds four separate boundaries and preserves every
  earlier signature.

## New questions

- Which later game reuses target-relative movement outside a combat lock?
- Does a second reviewed scan system reuse all three typed completion results,
  or force the information and fixture branches to split?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0356` — *Shadow of the Colossus*, the
  exact PlayStation 2 target and bounded route recorded in selection 025.
- Optimisation criterion: contrast target-relative scanning and prologue
  capability reset with large-body traversal, grip and one-colossus clearance.
- Expected information gain: high across moving-surface attachment, stamina,
  climb topology and authored guardian settlement.
- Backlog impact: continue research selection 025 without changing its order.

## Why this game

- [Hypothesis | Limited | High] Metroid Prime adds a recognisable first-person
  packet in which observation, targeting, combat and traversal share one
  authored escape route, then closes by removing rather than granting most of
  the demonstrated capabilities.

## Localisation notes

- Preserve official names and literal labels: Metroid Prime, Samus Aran,
  Frigate Orpheon, Tallon IV, Parasite Queen, Meta Ridley, Scan Visor, Combat
  Visor, Power Beam, Charge Beam, Missile Launcher, Morph Ball, Morph Ball
  Bombs, Grapple Beam, Space Jump Boots, Varia Suit, Power Suit, GameCube,
  `DOL-GM8E-0-00`, `GM8E01_00`, New Game, HUD, Log Book and Save Station.
- Translate explanatory prose naturally while preserving the distinction among
  target lock, held scan, capability malfunction and reduced loadout.
- Do not translate code identifiers, hashes, source configuration names or
  stable gene IDs.

## Review status

- Analysis status: reviewed.
- Novelty search: complete against every lower-ID canonical game and all
  verified combinations after the final signature was fixed.
- Direct-play status: not conducted; source-bounded reconstruction only.
- Next review trigger: primary original script/resource evidence for the exact
  Orpheon object graph, a contradiction in the `0-00` malfunction set or scan
  retention, or a later independent carrier that requires splitting the typed
  scan-resolution or target-relative-lock boundaries.
