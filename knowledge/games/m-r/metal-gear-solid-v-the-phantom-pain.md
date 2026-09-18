---
game_id: GAME-0306
slug: metal-gear-solid-v-the-phantom-pain
game_title: METAL GEAR SOLID V: THE PHANTOM PAIN
analysis_status: reviewed
reviewed: 2026-09-18
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-202
    - ACT-218
    - ACT-235
    - ACT-247
    - ACT-405
    - ACT-466
  system:
    - SYS-057
    - SYS-208
    - SYS-215
    - SYS-369
    - SYS-373
    - SYS-737
    - SYS-747
    - SYS-773
    - SYS-888
  constraint:
    - CON-077
    - CON-262
    - CON-282
    - CON-285
    - CON-330
    - CON-335
    - CON-426
    - CON-644
  information:
    - INF-073
    - INF-075
    - INF-115
    - INF-125
    - INF-287
    - INF-299
  objective:
    - OBJ-178
  time:
    - TIM-003
---

# Game: METAL GEAR SOLID V: THE PHANTOM PAIN

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The mission,
rescue subject, horse, helicopters, weapon names and Skulls are parameters,
not gene labels.

## Analysis scope

- Version / ruleset: Konami's English Xbox One base product, separately listed
  from the Definitive Experience, released 2015-09-01; official Xbox One
  manual checked 2026-09-18. The installed executable and patch number were
  not observed. Xbox Series backward compatibility does not change the
  analysis target. Use a fresh, unmodified, offline single-player campaign,
  with no imported `GROUND ZEROES` save or online service.
- Structured analysis target: Xbox One base-game digital product, English
  interface and default Action Type controls; see `GAME-0306` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: select `GAME START` on a clean save and pass the mandatory hospital
  prologue as an authored incoming gate. The tactical packet starts at first
  ordinary horseback control in Afghanistan for Mission 1, `Phantom Limbs`,
  before finding Kazuhira Miller. This fresh first attempt does not grant the
  normal later-mission equipment, buddy or landing-zone planning surface.
- Primary decision loop: inspect the current objective and partial iDroid map,
  observe patrols through local sight and binoculars, hold the optics on
  visible soldiers to acquire actor-bound markers, and monitor directional
  detection; ride, dismount, crouch or crawl to route through cover; evade or
  non-lethally neutralise an eligible unaware guard, with ordinary firearms
  available if stealth breaks. Reach Miller in Da Ghwandai Khar, carry him
  under the restricted carried-body action state toward the indicated landing
  zone, respond when Skulls make that first pickup unavailable, route around
  them to the second live landing zone, load Miller into the helicopter and
  board it yourself. Inspect the mission's conduct and rank summary.
- Positive terminal: Miller and the protagonist board the second usable
  helicopter, `Phantom Limbs` completes, and its result screen reports the
  attempt's categories and aggregate rank. Stop at this mission settlement;
  first Mother Base arrival and Mission 2 training are successor material, not
  part of the analysed decision loop. No reload of the result was performed.
- Negative terminal: the protagonist dies or a mission-critical rescue state
  becomes invalid. Retry resumes from an authored automatic checkpoint; the
  failed transient actor, objective and patrol state is not treated as the
  successful terminal. Mere detection, combat or a blocked first landing zone
  is recoverable rather than immediate failure.
- Included: the mandatory prologue only as prerequisite; first-mission horse
  movement; direct on-foot traversal and posture; binocular actor marking and
  retained tags; local sight/sound, threat direction, suspicion, search and
  alert; automatic Reflex Mode at first detection and the short chance to
  prevent a report; CQC or legal finite-ammunition weapon use, reload and
  cover; damage followed by quiet-interval recovery; carrying Miller with a
  limited usable weapon channel; the first denied and second usable helicopter
  zones; checkpoint retry; mandatory two-person extraction and a scored
  mission report. Normal daylight, patrol timing and route remain parameters.
- Excluded: the later Mother Base management loop, Fulton extraction, staff
  recruitment, equipment research and upgrades, custom deployment loadouts,
  free-roam missions, Side Ops, FOB, METAL GEAR ONLINE, connected bonuses,
  imported `GROUND ZEROES` data, optional prisoners/intel/collectibles,
  secondary mission objectives, all later missions, replay rank optimisation,
  other platforms, Definitive Experience extras, mods and the campaign ending.
  A general game manual describing Fulton does not make it available on this
  first fresh mission.
- Reproducible parameterisation: choose the exact Xbox One base product and a
  clean offline `GAME START` with default Action Type controls. Complete the
  mandatory hospital route without imported data. On the first `Phantom
  Limbs` attempt, use the issued horse to reach a vantage point, mark at least
  one visible patrol with binoculars, enter Da Ghwandai Khar by a guarded
  route, avoid or subdue one unaware guard, locate Miller, carry him toward
  the announced first zone, and continue rather than treating the Skulls
  interruption as a completed extraction. Evade the Skulls, take Miller to
  the second live zone, put him aboard, then board and read the report. Route,
  detection, shots, damage, exact elapsed time, score and rank are variable.
- Potential scoped modules: a directly played Xbox One trace and exact
  installed-patch/reload comparison; later Fulton and staff development; a
  prepared repeat of Mission 1; Mother Base and FOB; combat against Skulls;
  alternate platforms or editions each needs its own evidence boundary.
- Direct-play status: not conducted. No Xbox One console, installed game,
  entitlement or save trace was available. The official Xbox One manual and
  Konami offline FAQ establish product, controls, patrol, marking, Reflex,
  checkpoint, carry and offline-story rules. Independent written Mission 1
  routes corroborate the two landing zones, Miller carry restriction and
  final boarding order. This is a source-bounded reconstruction, not a claim
  of console play, rank observation or reload verification. No video or audio
  was opened, played or analysed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MGSV-001` | The selected product is the separately sold Xbox One base game, and the story is playable offline | Confirmed | Direct | High | P1, P2 |
| `MGSV-002` | The Xbox One manual's fresh start uses `GAME START`, automatic checkpoints, one overwritten save and no independent save slots | Confirmed | Direct | High | P3 |
| `MGSV-003` | The first `Phantom Limbs` attempt follows mandatory prologue and lacks the later normal mission-preparation and Fulton workflow | Observation | Corroborated | Medium | P4, S1, S2 |
| `MGSV-004` | Binocular focus can mark a visible actor; the view shows objective, current equipment and directional incoming hostile awareness | Confirmed | Direct | High | P5, P6 |
| `MGSV-005` | Speed, stance, cover, sight and sound affect detection; first sight can trigger Reflex Mode, and neutralising the observer before its alarm prevents nearby notification | Confirmed | Direct | High | P7 |
| `MGSV-006` | D-Horse is directly steered, and ordinary on-foot controls support CQC, aimed weapons, reload and carrying a person lying nearby | Confirmed | Direct | High | P5, P6, P8 |
| `MGSV-007` | Mission 1 locates injured Miller at Da Ghwandai Khar; while carrying him the practical firearm channel is the pistol | Observation | Corroborated | Medium | S1, S3 |
| `MGSV-008` | Skulls prevent the first landing-zone pickup, after which a second designated helicopter zone permits loading Miller and boarding to complete the mission | Observation | Corroborated | Medium | S3, S4 |
| `MGSV-009` | Mission completion produces a report of categories, points and aggregate rank | Observation | Corroborated | Medium | S5 |
| `MGSV-010` | Damage can recover after quiet withdrawal; death or mission failure yields Game Over and checkpoint continuation | Confirmed | Direct | High | P3, P9 |
| `MGSV-011` | No installed Xbox One patch, direct route, settled rank or post-reload state was observed | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Kojima Productions / Konami, Xbox One base game released
  2015-09-01. Product and distribution are distinct from the separately
  bundled Definitive Experience.
- Platform or physical form: Xbox One digital base product, fresh offline
  single-player story, default Action Type controls.
- Puzzle family: tactical forecast and counterplay; real-time system
  pressure; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-18:
  - **[P1]** [Xbox base-product listing](https://www.xbox.com/en-us/games/store/metal-gear-solid-v-the-phantom-pain/C253HWJP0L18),
    for platform, release and separate product identity.
  - **[P2]** [Konami offline-story FAQ](https://www.konami.com/mg/mgs5/tpp/faq/item.php?id=2&lang=en&region=ac),
    for offline main-story completion and unavailable online features.
  - **[P3]** [official Xbox One manual: starting and saving](https://mgstpp-app.konamionline.com/manual/xb1/na/en/xb1_01.html),
    for clean start, checkpoints and save limits.
  - **[P4]** [official Xbox One manual: game flow](https://mgstpp-app.konamionline.com/manual/xb1/na/en/xb1_07.html),
    for Mother Base and later mission-planning order.
  - **[P5]** [official Xbox One manual: game screen](https://mgstpp-app.konamionline.com/manual/xb1/na/en/xb1_02.html)
    and [on-foot controls](https://mgstpp-app.konamionline.com/manual/xb1/na/en/xb1_03.html),
    for marking, threat direction, weapons, posture, carry and boarding icons.
  - **[P6]** [official Xbox One manual: horseback controls](https://mgstpp-app.konamionline.com/manual/xb1/na/en/xb1_04.html)
    and [iDroid](https://mgstpp-app.konamionline.com/manual/xb1/na/en/xb1_08.html),
    for steerable horse, partial map and live information device.
  - **[P7]** [official Xbox One manual: sneaking](https://mgstpp-app.konamionline.com/manual/xb1/na/en/xb1_10.html),
    for speed, cover, awareness, search and Reflex Mode.
  - **[P8]** [official Xbox One manual: tactics](https://mgstpp-app.konamionline.com/manual/xb1/na/en/xb1_12.html),
    for CQC, weapons, non-lethal outcomes, weather and later Fulton rules.
  - **[P9]** [official Xbox One manual: damage and Game Over](https://mgstpp-app.konamionline.com/manual/xb1/na/en/xb1_11.html),
    for quiet healing, critical wounds and failure.
- Corroborating written sources, accessed 2026-09-18:
  - **[S1]** [Mission 1 introduction](https://www.gamepressure.com/mgs5thephantompain/introuduction/z07b70),
    for the initial first-attempt constraints and objective.
  - **[S2]** [independent Mission 1 route](https://www.supercheats.com/metal-gear-solid-v-the-phantom-pain/walkthrough/mission-1-phantom-limbs),
    for early-mission equipment progression and target route.
  - **[S3]** [Miller rescue written route](https://www.gamepressure.com/mgs5thephantompain/rescuing-kazuhira-miller/z37b73),
    for approach, carrying and helicopter boarding.
  - **[S4]** [Mission 1 map](https://www.gamepressure.com/mgs5thephantompain/phantom-limbs-mission-map/z17b71),
    for the blocked and successor landing zones.
  - **[S5]** [mission-summary written reference](https://www.gamepressure.com/mgs5thephantompain/mission-summary/zc7b21),
    for post-mission statistics, points and rank; exact values are not claimed.
- Research record: **[R1]** 2026-09-18 local preflight found no Xbox
  hardware, installation, entitlement or saved trace. No console play or
  reload occurred.
- Claim IDs: `MGSV-001`–`MGSV-011`.

## Mechanical decomposition

### Action Genes

- `ACT-008` covers direct on-foot travel and `ACT-247` the first issued
  horse's mounting, steering and dismounting. `ACT-202` changes posture and
  exposure. `ACT-405` creates a visible patrol mark through binocular focus.
  `ACT-235` handles a valid unaware close neutralisation; `ACT-164`,
  `ACT-161` and `ACT-183` cover switching, striking and reloading if combat
  becomes necessary. New `ACT-466` owns taking an injured mission subject into
  embodied carry, moving him and handing him into the transport. `ACT-218`
  owns the player's separate final boarding of the live departure endpoint.
  Claim IDs: `MGSV-004`–`MGSV-008`.

### System Behaviour Genes

- `SYS-057` replaces patrol with pursuit or investigation after perception;
  `SYS-373` escalates local suspicion into shared alert and combat. New
  `SYS-888` inserts an automatic short slow-motion response when first
  detected and cancels that observer's alarm only if it is neutralised in the
  window. `SYS-747` preserves the acquired actor marker behind ordinary
  cover. `SYS-208` resolves an admitted ranged shot against cover/body;
  `SYS-215` resolves live hostile combat; `SYS-737` applies damage and
  quiet-interval recovery; `SYS-369` restores a failed attempt at an authored
  checkpoint. `SYS-773` aggregates bounded mission conduct into the displayed
  result. Claims: `MGSV-004`–`MGSV-010`.
- Resolution order: observe and mark patrols; approach or neutralise under
  directed perception; reach Miller; carry him toward the first indicated
  endpoint; the Skulls event withdraws that endpoint's availability;
  conceal or evade and move to the second; hand Miller to the helicopter;
  board separately; settle the mission report. No staff or Fulton extraction
  step is inserted into this first-attempt order.

### Constraint Genes

- `CON-077` bounds direct sight by facing and occlusion; `CON-335` requires
  an unaware reachable hostile for stealth neutralisation. `CON-262` bounds
  carried weapons and ammunition, and `CON-285` makes a shot/reload require a
  compatible current weapon, ammunition and action state. New `CON-644`
  restricts ordinary weapon and movement choices while carrying an injured
  human. `CON-282` represents authored first-to-second landing-zone order;
  `CON-426` requires the mandatory rescue state and active extraction region
  to settle the mission; `CON-330` keeps protagonist, rescued target and
  mission area viable. Claims: `MGSV-003`–`MGSV-010`.

### Information Genes

- `INF-115` gives only locally seen and heard patrol state. `INF-287` joins
  acquired actor marks with the directional detection warning, while
  `INF-125` shows the partial map and current objective. `INF-073` exposes
  current weapon and finite ammunition; `INF-075` exposes personal damage
  through screen condition rather than a numerical life bar. `INF-299`
  exposes terminal conduct categories and rank. Claims: `MGSV-004`,
  `MGSV-005`, `MGSV-009`, `MGSV-010`.

### Objective Genes

- New `OBJ-178` requires reaching the designated living subject, moving him
  physically to a usable extraction craft, loading him, then boarding and
  receiving mission completion. Finding Miller or reaching the blocked first
  zone alone does not meet it. Claim IDs: `MGSV-007`–`MGSV-009`.

### Time Genes

- `TIM-003` keeps patrol, sight, damage and extraction routing live while the
  player acts; iDroid use does not pause the world. Reflex Mode is an automatic
  temporary change in local action speed within that real-time loop, not a
  turn-based planning phase. Claims: `MGSV-004`–`MGSV-008`.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Clean Xbox One save | `GAME START`, complete mandatory hospital route | First ordinary horseback Mission 1 control appears without later loadout planning | exact first-attempt entry | `MGSV-002`, `MGSV-003` |
| Visible patrol from a vantage point | Focus binoculars on one soldier | Actor-bound marker remains available through ordinary occlusion | acquired knowledge differs from omniscience | `MGSV-004` |
| Guard has directed sight but protagonist is behind cover | Move low outside the sight region | Patrol does not receive an automatic full-detection event | posture and geometry change route risk | `MGSV-005` |
| Eligible guard first spots the protagonist | Respond during Reflex Mode | Neutralising that observer within the short window prevents its warning; otherwise alert can spread | automatic detection response is not a manually chosen power | `MGSV-005` |
| Miller is found in the village | Lift and carry him | Rescue subject travels with the protagonist; pistol-only practical weapon channel replaces ordinary two-handed use | human carry is not a loot bag or Fulton extraction | `MGSV-006`, `MGSV-007` |
| Miller is carried to the initial indicated pickup | Continue when Skulls block it | First landing zone cannot settle the rescue; a second becomes the operative route | arriving at any marker is not enough | `MGSV-008` |
| Second zone is live and both actors survive | Load Miller, then board separately | Helicopter departs and Mission 1 completes | required subject and player are distinct boarding predicates | `MGSV-008` |
| Mission has completed | Inspect summary | Conduct, points and aggregate rank are presented | accepted source-backed terminal, not observed values | `MGSV-009`, `MGSV-011` |
| Controlled body dies or mandatory rescue fails | Continue at authored checkpoint | Current failed transient state is replaced by the checkpoint | recoverable failure is not positive completion | `MGSV-002`, `MGSV-010` |

## Strategic and experiential structure

- Local decision: use vantage points and persistent marks to read partial
  patrol paths, then choose quiet low-profile entry or accept a live alert.
- Medium-term planning: clear or avoid the most exposed route *before*
  carrying Miller, because carrying narrows movement and weapon choices.
- Long-term structure: find, protect, transport and board with the subject;
  the first apparently valid endpoint is withdrawn by an authored threat and
  the mission ends only after the second extraction and report.
- Common heuristics: mark visible guards, route around directed sight, conceal
  when detected, let damaged health recover in safety and distinguish the
  subject's loading from the player's own boarding.
- Failure attribution: unseen observer, expired Reflex window, discovered
  body, depleted or incompatible ammunition, injured subject, blocked
  endpoint, protagonist death and missed final boarding are different causes.
- Player trust: objective marker, binocular tags, threat-direction cue,
  action icon, landing-zone update and summary make the critical changes
  legible without revealing every future patrol or the Skulls event in advance.
- Claim IDs: `MGSV-004`–`MGSV-011`.

## Replay and variation

- What changes: patrol positions and alert timing, chosen route, acquired
  marks, optional combat, health, ammunition, elapsed time, score and rank.
- Randomness or procedural generation: this first mission uses an authored
  route; the packet does not claim a procedural map or fixed enemy timing.
- Multiple viable strategies: reach Miller by avoiding or quietly disabling
  guards; evade the Skulls on foot or use the horse after the blocked pickup.
  The subject must still reach and board the usable helicopter.
- Replay motive: improve stealth/rank or optional objectives in later attempts;
  those replay systems are not included in the fresh-first-attempt signature.
- Claim IDs: `MGSV-003`–`MGSV-011`.

## Adjacent systems and history

- Nearby corpus cases: Far Cry 3 uses optical tagging and a first outpost's
  finite clearance; Dishonored uses a carried unconscious target but settles
  a different non-lethal assassination and report; HITMAN uses disguises and
  two targets. This route makes a living rescue subject's physical delivery
  and separate boarding the primary terminal instead.
- Later-series systems: Fulton, staff, procurement and FOB are prominent in
  the wider product but are not back-projected into the first fresh Mission 1
  attempt. The official manual documents their future availability; that is
  not proof they are available before Mother Base onboarding.
- Version caution: the official manual describes Xbox One controls and rules,
  not an observed installed 2026 patch. No parity claim for PC, PlayStation,
  Xbox Series execution or Definitive Experience follows.
- Claim IDs: `MGSV-001`–`MGSV-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-202`, `ACT-218`, `ACT-235`, `ACT-247`, `ACT-405`, `ACT-466` | traversal, horse, optics, stealth, carry, board |
| System Behaviour | `SYS-057`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-737`, `SYS-747`, `SYS-773`, `SYS-888` | patrol, combat, recovery, Reflex, result |
| Constraint | `CON-077`, `CON-262`, `CON-282`, `CON-285`, `CON-330`, `CON-335`, `CON-426`, `CON-644` | perception, ammunition, target, carry, exit |
| Information | `INF-073`, `INF-075`, `INF-115`, `INF-125`, `INF-287`, `INF-299` | map, sight, marks, danger, report |
| Objective | `OBJ-178` | living-subject delivery and joint boarding |
| Time | `TIM-003` | live patrol and rescue clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `305` (`GAME-0001`–`GAME-0305`).
- Exact genome matches: none.
- Tied near matches: `GAME-0236` — Far Cry 3 (`23 / 42 = 0.547619`).
- Supported combination subsets: none.
- Scan date: 2026-09-18.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0236` — Far Cry 3 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-202`, `ACT-235`, `ACT-405`, `SYS-057`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-747`, `CON-262`, `CON-282`, `CON-285`, `CON-330`, `CON-335`, `INF-073`, `INF-115`, `INF-125`, `INF-287`, `TIM-003` | Both routes inspect and tag guards, choose low-exposure movement, allow a quiet takedown or finite-ammunition firefight, and recover from authored checkpoints. Far Cry 3's first outpost requires finite hostile clearance and then converts the location into an allied service node. This Xbox One `Phantom Limbs` packet instead keeps a living injured subject viable, restricts the carrier's combat choices, changes the usable pickup zone and requires both subject and rescuer to board before a graded mission result. Reflex Mode is an automatic detection response absent from that Far Cry 3 signature. | Tied near, `23 / 42 = 0.547619` |

### Preserved research notes

- New genes: `ACT-466`, `SYS-888`, `CON-644`, `OBJ-178`.
- Classification result: new genes with reused stealth, mark, checkpoint,
  extraction, combat and report boundaries.
- Evidence and reasoning: an injured living person's physically restricted
  carry and handoff is not `ACT-359` bag handling or `OBJ-023` autonomous
  carrier delivery; Reflex is triggered by *being detected*, not the player's
  chosen Dead Eye action; the separate carried-body restriction is not ordinary
  weapon-slot compatibility. The required rescued subject plus player boarding
  is not a quota, hostile-target elimination or optional extraction bonus.

## Taxonomy impact

- Registry changes: four new Active definitions; no earlier signature,
  existing definition or gene lifecycle changes.
- Taxonomy-change record: none; no earlier boundary is rewritten.
- Candidate terms affected: Miller, Skulls, D-Horse, Reflex Mode, CQC, iDroid,
  `Phantom Limbs` and helicopter are instance labels, not reusable gene names.

## Negative results

- The originally selected broad hypothesis about first Mother Base, Fulton,
  personnel and resource persistence is not evidenced by this first-mission
  packet. The official flow puts Mother Base features after first arrival;
  secondary first-attempt routes say Fulton is not yet available. Neither is
  silently placed in the signature.
- No installed Xbox One patch, direct play, exact rank or save/reload trace
  was available. These evidence gaps do not mean the game lacks those systems.
- `ACT-359`, `OBJ-023`, `OBJ-087` and `SYS-479` are rejected here because they
  mean, respectively, a thrown loot bag, autonomous carriers, optional
  post-objective extraction assets and deliberately activated Dead Eye.

## Delta summary

## New facts

- [Confirmed | Direct | High] The Xbox One manual specifies binocular marks,
  directional threat cues, carry, live iDroid, Reflex response and automatic
  checkpoints (`MGSV-002`, `MGSV-004`–`MGSV-006`, `MGSV-010`).
- [Observation | Corroborated | Medium] The first fresh rescue carries Miller
  through a blocked first pickup to a second zone, where he and the player
  board separately (`MGSV-003`, `MGSV-007`–`MGSV-009`).

## New genes

- [Observation | Corroborated | Medium] `ACT-466`, `CON-644` and `OBJ-178`
  isolate physically constrained human rescue and two-person departure.
- [Confirmed | Direct | High] `SYS-888` isolates a detection-triggered brief
  response window that can prevent an observer's alarm.

## New combinations

- [Observation | Corroborated | Medium] No new verified combination is asserted;
  the final subset scan is recorded above.

## Taxonomy changes

- [Confirmed | Direct | High] No earlier canonical gene or game signature is
  changed by this addition.

## New questions

- Which exact Xbox One executable revision was installed, and does a direct
  first-attempt run reproduce the source-bounded checkpoint, first pickup and
  mission-result sequence?
- What exact state is retained after dismissing the rank screen and restarting
  the same offline save? This needs an observed console trace.

## Next recommended game

- [Hypothesis | Limited | Medium] No `GAME-0307` is selected by the completed
  298-to-306 horizon. The next separately authorised step is a nine-game
  batch acceptance/publication decision, not an implicit new game unit.
- Optimisation criterion: audit the nine local commits and publish only after
  the separately governed public-corpus and release gates.
- Backlog impact: the carried selection-018 reserves remain candidates, not
  pre-authorised next units.

## Why this game

- [Hypothesis | Limited | Medium] The Xbox One legacy target completes the
  amended `2+2+2+2+1` platform allocation. Its first authored stealth rescue
  tests whether tagging, perception response and carrying a living subject
  to a changing exit separate it from the corpus's clearance, assassination
  and optional-extraction cases.
