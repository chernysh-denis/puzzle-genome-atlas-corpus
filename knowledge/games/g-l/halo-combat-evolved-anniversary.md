---
game_id: GAME-0340
slug: halo-combat-evolved-anniversary
game_title: "Halo: Combat Evolved Anniversary"
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-199
    - ACT-202
    - ACT-409
  system:
    - SYS-215
    - SYS-222
    - SYS-348
    - SYS-369
    - SYS-749
    - SYS-754
    - SYS-780
    - SYS-851
    - SYS-913
  constraint:
    - CON-262
    - CON-282
    - CON-578
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-268
    - INF-349
  objective:
    - OBJ-155
  time:
    - TIM-003
---

# Game: Halo: Combat Evolved Anniversary

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Master Chief,
Cortana, Captain Keyes, Pillar of Autumn, Covenant, Bumblebee and every weapon,
enemy or room name are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: the original North American English standalone Xbox 360
  release of Halo: Combat Evolved Anniversary dated 2011-11-15, restricted to
  the campaign rules available on the retail disc. This is not the 2001 Xbox
  original, Halo: The Master Chief Collection, its PC port, a backward-
  compatible wrapper or the distinct 2026 Halo: Campaign Evolved remake.
- Structured analysis target: fresh solo Campaign on `Normal`, default
  controller layout, no skulls and no title-update-dependent Kinect features;
  see `GAME-0340` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: follow the authored ship route, read local sight,
  sound, prompts, motion contacts and navigation feedback, then move, crouch,
  aim, fire, melee, throw grenades, reload, swap or replace one of two weapons,
  withdraw for shield recovery and continue through finite boarding groups
  until the last escape pod becomes reachable.
- Entry: first ordinary Master Chief control after the cryogenic wake-up
  cutscene, before the `Normal` targeting, look-pitch and shield tutorial.
- Positive terminal: Master Chief has received Cortana, crossed the complete
  ordered ship route and entered the last Bumblebee escape pod; `The Pillar of
  Autumn` completes and the ordinary campaign continuation reaches first
  controllable state in `Halo` after the pod crash.
- Included: the `Normal` targeting, pitch-choice, shield and movement tutorial;
  direct walking, jumping and crouching under the half-raised hatch; aimed
  firearm and melee attacks; magazine reload; two carried weapons, finite
  compatible ammunition and typed grenades; prompted weapon replacement and
  contact ammunition, grenade and health-pack pickup; shield before underlying
  health and delayed shield recharge; flashlight toggle, active charge drain
  and inactive automatic recharge; local sight and sound; navigation point,
  authored instructions and prompts; moving-contact Motion Tracker; finite
  authored Covenant groups; automatic checkpoint restoration after lethal
  failure; Cortana retrieval, the escape-pod route and the named successor.
- Anniversary presentation boundary: the Back button switches immediately
  between the synchronized original and remastered visual presentations while
  ordinary campaign world state continues. The feature is established and may
  be exercised in the packet, but it adds no genome gene because it changes
  rendering rather than a legal action, simulation transition, constraint,
  disclosed rule state, objective or time authority.
- Excluded: co-op, split screen, Xbox LIVE, multiplayer and the bundled Halo:
  Reach maps; skull activation, terminals and achievements; Kinect voice or
  Analyse Mode, because the manual requires a title update for them; stereoscopic
  3D; non-`Normal` tuning; later missions, vehicles, Overshields and full-
  campaign completion; title updates, DLC, MCC playlists, scoring, par times,
  later ports, mods and the 2026 remake.
- Reproducible parameterisation: start fresh solo `Normal` Campaign without
  skulls; complete the cryo-bay instructions; follow the crew to the bridge;
  receive Cortana and Keyes's unloaded pistol; take reachable ammunition and
  an Assault Rifle; follow the only admitted route through the mess hall,
  corridors, maintenance access and final airlock; enter the last pod. Exact
  weapon pair, grenade use, ammunition spend, flashlight timing, shield breaks,
  health damage, optional pickups, deaths and surviving Marines may vary.
- Potential scoped modules: performed disc/build identification, title-update
  Kinect state, skulls, terminals, co-op, 3D, save/quit/relaunch equality,
  later missions, multiplayer and MCC each require their own entry, loop and
  evidence.
- Direct-play status: not conducted. No Xbox 360 console, disc, title update,
  entitlement, installed executable, campaign save, controller trace,
  screenshot, video or audio was available or analysed. The result is a
  source-bounded reconstruction, not a claimed playthrough or reload test.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HCEA-001` | Microsoft released the standalone Xbox 360 Halo: Combat Evolved Anniversary on 2011-11-15 as a remade and remastered tenth-anniversary campaign | Confirmed | Direct | High | P1, P2 |
| `HCEA-002` | The standalone manual separates solo campaign from co-op and Halo: Reach multiplayer maps and makes Kinect features dependent on a title update | Confirmed | Direct | High | P1 |
| `HCEA-003` | Default controls expose movement, crouch, jump, aim/fire, melee, reload, weapon and grenade switching, grenade throw, contextual pickup/action, flashlight and visual-mode toggle | Confirmed | Direct | High | P1, P3 |
| `HCEA-004` | The HUD exposes weapon/ammunition, grenade, health, shield, flashlight, navigation and moving-contact Motion Tracker state | Confirmed | Direct | High | P1, P3 |
| `HCEA-005` | Damage reaches the rechargeable personal shield before finite underlying health, while health packs restore health and the inactive flashlight restores its own charge | Observation | Corroborated | High | P3, S1 |
| `HCEA-006` | Master Chief carries at most two weapons with finite compatible ammunition and finite typed grenades, replacing a carried weapon through a prompted pickup | Observation | Corroborated | High | P1, P3, S1 |
| `HCEA-007` | The `Normal` opening teaches look calibration, shield state, crouch, melee, motion sensing and grenades through authored progressive instructions | Observation | Corroborated | High | P1, S1 |
| `HCEA-008` | The Anniversary visual toggle replaces rendering without restarting or advancing the synchronized campaign simulation | Confirmed | Direct | High | P1, P2 |
| `HCEA-009` | The first mission advances from cryo control to Keyes and Cortana, then through authored combat corridors to the final Bumblebee escape pod | Observation | Corroborated | High | S1, S2, P4 |
| `HCEA-010` | Entering the pod completes `The Pillar of Autumn` and the successor `Halo` resumes after the pod crash | Observation | Corroborated | High | S1–S3, P4 |
| `HCEA-011` | No original-console run, disc inspection or save/relaunch comparison was performed, so exact stored checkpoint fields remain unobserved | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: 343 Industries, Bungie, Certain Affinity and Saber
  Interactive / Microsoft Studios; North American Xbox 360 release on
  2011-11-15.
- Platform or physical form: original English standalone Xbox 360 retail-disc
  campaign, source-bounded disc rules, fresh solo `Normal`.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; world topology and perspective; ordered
  dependency sequencing.
- Primary and official sources, accessed 2026-09-21:
  - **[P1]** [official Halo: Combat Evolved Anniversary Xbox 360
    manual](https://download.microsoft.com/download/f/9/9/f99ab8f0-5191-4edd-b312-7a9b9e4784fa/haloanniversary_mnl_en-us.pdf),
    pp. 1–5, for product authorship, campaign/co-op separation, new features,
    title-update Kinect boundary, HUD and default controls including the visual
    toggle.
  - **[P2]** [Xbox Wire Halo Fest announcement](https://news.xbox.com/en-us/2011/08/26/news-from-halo-fest/),
    for the standalone 2011-11-15 release date.
  - **[P3]** [original Microsoft Halo: Combat Evolved Xbox manual
    transcript](https://www.manualslib.com/manual/378766/Microsoft-Halo-Combat-Evolved.html),
    for inherited controller, weapon, HUD, shield/health, navigation, motion-
    tracker and flashlight rules retained by the Anniversary manual's original
    campaign framing.
  - **[P4]** [official Halo timeline article](https://www.halowaypoint.com/news/thats-so-raven),
    for the cryogenic awakening aboard Pillar of Autumn and the opening
    campaign chronology.
- Corroborating written sources, accessed 2026-09-21:
  - **[S1]** [The Pillar of Autumn level transcript](https://www.halopedia.org/Pillar_of_Autumn_%28Halo%3A_Combat_Evolved_level%29),
    for original/Anniversary route events, `Normal` tutorial differences,
    Cortana retrieval, authored groups and the final pod.
  - **[S2]** [The Pillar of Autumn written walkthrough](https://www.halopedia.org/CE%3AThe_Pillar_of_Autumn/Walkthrough),
    for reproducible route order from cryo bay through the bridge and corridors
    to the pod.
  - **[S3]** [`Halo` successor-level reference](https://www.halopedia.org/CE%3AHalo),
    for first ordinary successor control after the Bumblebee crash.
- Research record: **[R1]** local preflight found no original Xbox 360 disc,
  console, build, title update or save; no audiovisual or direct-play evidence
  was used.
- Claim IDs: `HCEA-001`–`HCEA-011`.

## Mechanical decomposition

### Action Genes

- `ACT-008` owns direct traversal and jumping; `ACT-202` the required crouch
  under the half-raised hatch; `ACT-161` aimed firearm and melee attacks;
  `ACT-164` carried-weapon selection; `ACT-183` magazine reload; `ACT-184` one
  finite grenade throw; `ACT-199` prompted weapon pickup or replacement; and
  `ACT-409` the reversible personal flashlight command. The rendering-only
  classic/remastered toggle is recorded but rejected from the canonical
  genome. Claims: `HCEA-003`, `HCEA-006`–`HCEA-009`.

### System Behaviour Genes

- `SYS-215` resolves direct live combat; `SYS-222` transfers eligible contact
  pickups; `SYS-348` routes incoming damage through shield and health;
  `SYS-913` restores ordinary shield after a damage-free interval; `SYS-754`
  converts active flashlight charge into local illumination and `SYS-851`
  restores inactive flashlight charge; `SYS-749` instantiates finite authored
  encounter groups; `SYS-369` restores an accepted checkpoint after lethal
  failure; and `SYS-780` carries the completed mission into the documented
  successor.
- Resolution order: a shot or strike resolves weapon, ammunition, reach,
  defence and damage; incoming damage spends shield before health while a
  quiet interval admits shield recovery; active flashlight spends its own
  charge while off-state time restores it; route position admits encounter and
  checkpoint state; entering the final pod settles the mission and successor.
  Claims: `HCEA-004`–`HCEA-011`.

### Constraint Genes

- `CON-262` owns two weapon slots, typed grenade caps and finite carried
  ammunition; `CON-578` requires compatible remaining ammunition or charge to
  fire; and `CON-282` requires the ordered cryo, bridge, Cortana, ship-route and
  escape-pod gates. `CON-402` is rejected because written routes allow some
  incidental fights to be bypassed rather than requiring every spawned actor
  to die. Claims: `HCEA-006`, `HCEA-009`, `HCEA-010`.

### Information Genes

- `INF-073` exposes active weapon, ammunition and grenade state; `INF-119`
  shield, health and flashlight readiness; `INF-115` local sight and sound;
  `INF-125` navigation and mission gates; `INF-268` progressive tutorial and
  route instructions; and `INF-349` the passive allegiance-coded tracker for
  eligible nearby moving contacts. Claims: `HCEA-004`–`HCEA-009`.

### Objective Genes

- `OBJ-155` owns completion of the authored survival-action mission into
  ordinary successor control. The parameters are Cortana retrieval, ordered
  ship traversal, entering the last pod, mission completion and first control
  after its crash; optional collectibles and hostile total clearance are not
  required. Claims: `HCEA-009`–`HCEA-011`.

### Time Genes

- `TIM-003` owns continuous movement, combat, tutorial actors, flashlight and
  shield intervals, encounter pressure and escape inputs. Visual switching is
  immediate presentation, not separate simulation time. Claims: `HCEA-003`,
  `HCEA-005`, `HCEA-008`–`HCEA-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| The `Normal` targeting panel is active | Aim at each flashing panel and accept normal or inverted pitch | the chosen pitch remains active and the tutorial advances to shield testing | progressive authored instruction and a retained control parameter | `HCEA-007` |
| Shield has been charged and the route hatch is half raised | Crouch and move through | the same controlled body adopts compact posture and crosses otherwise blocked geometry | posture is a route action, not cosmetic animation | `HCEA-003`, `HCEA-007` |
| Keyes has supplied an unloaded pistol after Cortana enters the armour | Leave the bridge and touch compatible ammunition | accepted rounds enter the pistol reserve and it becomes fire-ready | contact pickup and compatible finite ammunition | `HCEA-006`, `HCEA-009` |
| Two weapons are carried and a third is reachable | Hold the pickup/swap input | the selected carried weapon is replaced while the displaced weapon returns to world state | a two-slot keep-or-replace decision | `HCEA-003`, `HCEA-006` |
| Active magazine is empty but compatible reserve remains | Commit reload | fire readiness is temporarily lost and reserve transfers into the magazine | reload is distinct from firing and weapon switching | `HCEA-003`, `HCEA-006` |
| Shield remains after a compatible hit | Receive damage | shield falls before underlying health becomes exposed | layered defence precedes lethal failure | `HCEA-004`, `HCEA-005` |
| Shield is below cap and no new damage arrives | Stay out of damage | after its delay the shield refills; another hit interrupts recovery | withdrawal converts safe time into protection | `HCEA-005` |
| Flashlight has positive charge in a dark corridor | Toggle it on, observe drain, then toggle it off | local light exists only while active charge remains; off-state time restores charge | a reversible self-restoring information resource | `HCEA-003`–`HCEA-005` |
| An eligible nearby actor moves | Observe the Motion Tracker | a relative friendly or hostile contact appears while stationary identity and elevation remain withheld | partial local sensor knowledge | `HCEA-004` |
| Campaign world state is active | Press Back | classic and remastered renderings switch while the synchronized route, actors and resources remain unchanged | Anniversary presentation is real but genome-neutral | `HCEA-003`, `HCEA-008` |
| Master Chief dies after an accepted automatic checkpoint | Continue | the latest eligible authored checkpoint is restored rather than the failed transient fight | failure restoration is not a finite life | `HCEA-011` |
| The final Bumblebee is reachable | Enter the pod | the mission completes and the campaign advances to first `Halo` control after the crash | authored escape and successor control | `HCEA-009`–`HCEA-011` |

## Strategic and experiential structure

- Local decision: balance exposed firing against shield recovery, select a
  two-weapon pair for the next corridor, spend finite ammunition or grenades,
  and treat motion contacts as incomplete rather than omniscient information.
- Medium-term planning: follow navigation and Cortana instructions, replace an
  empty or poorly ranged weapon before the next group and preserve enough
  health after shield breaks to reach a health pack.
- Long-term structure: a guided combat tutorial becomes one ordered evacuation
  route, with automatic checkpoints bounding loss until the pod transfers the
  campaign to the ring.
- Common heuristics: reload and recover shield behind cover; use the tracker
  for bearing, not elevation; crouch when instructed; collect compatible stock;
  do not mistake the visual toggle for a pause or different ruleset.
- Failure attribution: empty ammunition, an exposed reload, broken shield,
  missed route instruction, stationary unseen contact and failed checkpoint
  segment remain distinguishable through HUD, local feedback and restoration.
- Player-trust factors: weapon, ammunition, grenades, shield, health,
  flashlight, navigation, prompts, tracker contacts and visual mode are
  inspectable before their next relevant commitment.
- Claim IDs: `HCEA-003`–`HCEA-011`.

## Replay and variation

- What changes between sessions: weapon pair, pickup and grenade use, combat
  positions, hostile/ally survival, health, shield breaks, flashlight timing,
  deaths, checkpoint restores and chosen visual presentation.
- Randomness or procedural generation: no procedural room or encounter layout
  is evidenced; live combat cadence and actor outcomes vary inside authored
  groups.
- Multiple viable strategies: different weapon replacements, grenade spends,
  cover positions and bypasses can reach the same final pod.
- Typical replay motive: difficulty, skull, co-op, collectibles, achievements,
  visual comparison and speed are known product motives but excluded here.
- Claim IDs: `HCEA-006`–`HCEA-011`.

## Adjacent systems and history

- Direct predecessors: Halo: Combat Evolved (2001) supplies the inherited
  campaign simulation; Anniversary adds a synchronized remastered presentation
  and standalone Xbox 360 wrapper.
- Variants: classic/remastered rendering is admitted; Kinect, 3D, MCC, PC,
  later console wrappers and the 2026 remake are excluded.
- Similar games: `GAME-0315` Halo 3 reuses the two-weapon, shield, motion-
  tracker, checkpoint and authored-combat substrate in a different mission.
- Important differences: this packet includes the cryo tutorial, crouch hatch,
  health-pack-backed underlying health and automatically recharging flashlight;
  Halo 3 instead ends in a captive release, counterattack and Pelican extraction.
- Claim IDs: `HCEA-001`–`HCEA-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-199`, `ACT-202`, `ACT-409` | Master Chief, weapon and flashlight names are parameters |
| System Behaviour | `SYS-215`, `SYS-222`, `SYS-348`, `SYS-369`, `SYS-749`, `SYS-754`, `SYS-780`, `SYS-851`, `SYS-913` | shield, health pack, checkpoint and encounter identities are parameters |
| Constraint | `CON-262`, `CON-282`, `CON-578` | exact weapon, grenade and ammunition caps are parameters |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-268`, `INF-349` | HUD placement, contact colours and labels are parameters |
| Objective | `OBJ-155` | mission, Cortana, pod and successor names are parameters |
| Time | `TIM-003` | live rates and intervals are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `339` (`GAME-0001`–`GAME-0339`).
- Exact genome matches: none.
- Tied near matches: `GAME-0315` — Halo 3 (`23 / 31 = 0.741935`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0315` — Halo 3 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-199`, `SYS-215`, `SYS-222`, `SYS-348`, `SYS-369`, `SYS-749`, `SYS-780`, `SYS-913`, `CON-262`, `CON-282`, `CON-578`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-268`, `INF-349`, `TIM-003` | Both run a real-time authored campaign route with a two-weapon finite-ammunition loadout, grenades, layered rechargeable shield, partial moving-contact sensing, finite combat groups, checkpoint restoration and a named successor. Halo 3 adds explicit fixture interaction, complete required-group clearance and a captive-release/counterattack/Pelican terminal. Anniversary instead requires crouching under the tutorial hatch, exposes a charge-priced self-restoring flashlight and ends through the generic survival-segment escape-pod handoff; its synchronized rendering toggle remains genome-neutral. | Near, `23 / 31 = 0.741935` |

### Preserved research notes

- New genes: none.
- Classification result: `New combination of known genes`.
- Evidence and reasoning: every causal boundary transfers from prior analysed
  carriers. The Anniversary visual toggle is retained as a sourced product
  distinction but rejected as genome-neutral presentation. `CON-402` is
  rejected because incidental corridor hostiles may be bypassed; `OBJ-183` is
  rejected because no captive release or mandatory counterattack defines this
  terminal.

## Taxonomy impact

- Registry changes: add GAME-0340 support to twenty-eight compatible existing
  genes; no definition or prior signature changes.
- Taxonomy-change record: none.
- Candidate terms affected: Halo: Combat Evolved Anniversary, Xbox 360, Master
  Chief, Cortana, Captain Keyes, Pillar of Autumn, Bumblebee, Covenant,
  `Normal`, Motion Tracker, Classic Viewer and visual-mode labels remain
  product or instance parameters.

## Negative results

- No console, disc, build, title-update, controller, direct-play, screenshot,
  video, audio or save/relaunch evidence was available. Checkpoint and mission
  transfer are source-backed, not locally measured persistence equality.
- The visual toggle changes synchronized presentation and supports no new
  canonical gene. Kinect features are excluded because the manual makes them
  title-update-dependent; 3D, skulls, terminals, achievements, co-op and
  multiplayer are available outside this packet but are not inferred inward.
- `CON-402`, `OBJ-183` and an Overshield gene do not fit the bounded route.

## Delta summary

## New facts

- [Confirmed | Direct | High] The standalone 2011 Anniversary product exposes
  an immediate classic/remastered visual switch without changing the running
  campaign state (`HCEA-001`, `HCEA-008`).
- [Observation | Corroborated | High] The scoped first mission joins its
  cryo-bay tutorial, two-weapon shield combat, rechargeable flashlight and
  partial Motion Tracker to one escape-pod successor transition
  (`HCEA-003`–`HCEA-010`).

## New genes

- [Observation | Corroborated | High] No new genes; all twenty-eight causal
  rules reuse reviewed boundaries, and the Anniversary rendering toggle is
  deliberately genome-neutral.

## New combinations

- [Observation | Corroborated | High] No verified combination is a proper
  subset of the complete signature.

## Taxonomy changes

- [Confirmed | Direct | High] No earlier definition or game signature changed.

## New questions

- Which exact weapon, ammunition, health, shield and checkpoint fields survive
  a standalone Xbox 360 save/quit/relaunch after the final ship checkpoint?
- Did any standalone title update alter scoped solo `Normal` campaign rules
  beyond the explicitly update-dependent Kinect feature layer?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0341` Ninja Gaiden Black, as reserved
  by selection 023.
- Optimisation criterion: freeze one exact original-Xbox-compatible ruleset and
  a bounded early route rather than importing Ninja Gaiden Sigma or sequel state.
- Expected information gain: test committed attack recovery, guard, evasion and
  authored encounter pressure against the completed shooter packet.
- Backlog impact: advances unit 7/9; `GAME-0341` remains reserved but unstarted.

## Why this game

- [Hypothesis | Limited | Medium] Anniversary supplies a recognisable legacy
  Xbox campaign whose inherited two-weapon shield loop and distinctive
  synchronized visual presentation can be separated cleanly from MCC and the
  2026 remake.

## Research checklist

- [x] exact standalone Xbox 360 product, mode, difficulty and title-update boundary declared
- [x] primary loop, entry, terminal, parameters and exclusions declared
- [x] official manual, release evidence and written route reviewed
- [x] direct-play and persistence limitations disclosed
- [x] complete six-type signature and lower-ID comparison prepared
- [x] visual toggle classified without decorative taxonomy inflation
- [x] reviewed Ukrainian localisation and bilingual presentation completed
- [x] original artwork and responsive browser checks completed
- [x] repository and web quality gates completed
