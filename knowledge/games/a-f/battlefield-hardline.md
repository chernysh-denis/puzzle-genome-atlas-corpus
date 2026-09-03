---
game_id: GAME-0243
slug: battlefield-hardline
game_title: Battlefield Hardline
analysis_status: reviewed
reviewed: 2026-09-03
combination_ids:
  - COMB-0241
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-202
    - ACT-235
    - ACT-313
    - ACT-405
    - ACT-406
    - ACT-417
  system:
    - SYS-057
    - SYS-208
    - SYS-215
    - SYS-299
    - SYS-369
    - SYS-373
    - SYS-379
    - SYS-680
    - SYS-747
    - SYS-766
  constraint:
    - CON-262
    - CON-282
    - CON-285
    - CON-330
    - CON-335
    - CON-587
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-287
    - INF-293
  objective:
    - OBJ-151
  time:
    - TIM-003
---

# Game: Battlefield Hardline

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1238880`, public Build ID `10351826`, built 2023-01-18 and published to the
  public branch 2023-01-23, observed 2026-09-03. Steam currently sells the
  Ultimate Edition entitlement; only its base-game single-player campaign
  content is admitted, not the bundled Premium or expansion content.
- Service boundary: EA's current console sunset notice explicitly leaves PC
  availability and services unaffected. This packet uses only local campaign
  state after lawful EA-account activation; no multiplayer service is needed.
- Entry: start a fresh campaign, select `Officer`, finish the preceding
  Prologue/onboarding, choose Episode 1 `Back to School` from the Episode
  screen, and begin at its first controllable objective with default PC
  keyboard/mouse bindings and ordinary interface aids.
- Primary decision loop: read the objective, minimap, scanner classification,
  target marks, vision cones, awareness, health, ammunition, warrant/evidence
  and Expert progress; navigate and crouch; scan, analyse or tag one reachable
  target; throw a shell casing to redirect a patrol; issue `Freeze` while
  aiming and preserve coverage until an eligible suspect can be arrested, or
  use an unaware rear neutralisation; if detection completes, aim, fire,
  switch and reload under live pressure; advance the authored evidence,
  suspect, school and final partner-defence gates until the episode settles.
- Positive terminal: every mandatory Episode 1 gate is complete, including the
  final open firefight and partner defence; the episode-complete transition
  records its Expert, Case File and warrant outcomes and returns to an Episode
  surface with the successor exposed. Stop before entering Episode 2.
- Negative terminal: Nick's death, a mission-critical partner death or an
  authored area/objective violation fails the current attempt and offers an
  authored checkpoint retry. Detection, an escaped optional arrest bonus, a
  killed warrant suspect or incomplete optional evidence are evaluated route
  losses, not by themselves the packet's failure terminal.
- Included: first-person movement and crouch; scanner selection, held analysis
  and actor tagging; persistent markers, minimap contacts, vision cones and
  awareness; shell-casing diversion; unaware rear neutralisation; aimed
  `Freeze`, compliance maintenance and live arrest; finite weapon/ammunition
  state, switching, reload, firearm/CEW choices and open combat; mandatory
  evidence, one open-warrant suspect, Expert Score/Rank progress, authored
  checkpoints, mission-critical partner state, final defence and Episode 1
  settlement.
- Excluded: Prologue analysis, Episodes 2–10 and the whole campaign; replay,
  other difficulties, all-evidence/all-warrant optimisation, Tactical Gear
  optimisation and unlock shopping; multiplayer, Battlelog, online rank,
  Battlepacks and Premium; Criminal Activity, Robbery, Getaway, Betrayal,
  shortcut kits and every other Ultimate extra; other platforms, console
  sunset behaviour, mods, trainers, cheats and the wider Battlefield series.
- Reproducible parameterisation: lawful current English Windows install,
  Steam app `1238880` / public Build `10351826`, fresh campaign, `Officer`,
  default controls and interface aids, Episode 1 only. Analyse every mandatory
  evidence item; scan the named warrant suspect and attempt a living arrest;
  demonstrate one shell-casing diversion, one unaware rear neutralisation and
  one aimed `Freeze` arrest where the authored state permits them; accept the
  mandatory final firefight; stop at the first episode-complete successor
  surface. Exact paths, targets, cover, ammunition, score and combat duration
  are run parameters.
- Potential scoped modules: one later campaign episode, one higher-difficulty
  episode, one complete-evidence replay or one separately current multiplayer
  mode each requires its own build, entry, terminal and service evidence.
- Direct-play status: not conducted. The official PC manual establishes the
  campaign controls, scanner, evidence, warrants, arrest/compliance grammar,
  HUD and Episode interface. Official product, launch and current service
  notices establish product/mode boundaries; two maintained textual records
  corroborate build and Episode 1 order. This is evidence-backed rules
  reconstruction. No video or audio was opened, played, heard, analysed or
  used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BFH-001` | The current lawful Windows product is Steam app `1238880`, sold under an Ultimate Edition entitlement while retaining a separable base campaign | Confirmed | Direct | High | P1, P2 |
| `BFH-002` | Public Build `10351826` is the observed stable Windows Steam branch boundary | Observation | Corroborated | Medium | S1 |
| `BFH-003` | Campaign Episodes, multiplayer, Premium, Store and Battlelog are distinct product surfaces | Confirmed | Direct | High | P1, P2, P5 |
| `BFH-004` | EA's announced console sunset does not remove current PC availability or PC services | Confirmed | Direct | High | P3, P4 |
| `BFH-005` | The PC campaign exposes movement, crouch, firearms, reload, scanner, shell-casing diversion, `Freeze`, takedown and interaction controls | Confirmed | Direct | High | P1 |
| `BFH-006` | Scanner focus can tag living targets, analyse suspects/evidence and distinguish objective, interest and threat classes | Confirmed | Direct | High | P1, P6 |
| `BFH-007` | The HUD/minimap expose marked enemies, vision cones and awareness progress before full attack | Confirmed | Direct | High | P1 |
| `BFH-008` | `Freeze` can make a bounded nearby hostile group comply only while sufficient weapon/partner coverage is maintained | Confirmed | Direct | High | P1 |
| `BFH-009` | Living arrest of a scanned warrant target preserves a larger Expert payout than killing that target | Observation | Corroborated | High | P1, S2 |
| `BFH-010` | Examined evidence and objective activity contribute to Case File and Expert progression | Confirmed | Direct | High | P1 |
| `BFH-011` | Episode 1 orders diversion, scanning, stealth/arrest or combat, mandatory evidence, school traversal and a final partner defence before completion | Observation | Corroborated | High | S2 |
| `BFH-012` | Death or a mission-critical failure restores an authored checkpoint rather than settling the episode | Confirmed | Corroborated | High | P1, S2 |
| `BFH-013` | The bounded identity is scanner-led coercive stealth whose living-custody and evidence decisions are evaluated before an authored episode settlement | Strong Pattern | Corroborated | High | BFH-005–BFH-012 |

## Basic data

- Release / origin: Visceral Games / Electronic Arts; Windows release 2015;
  current PC availability and service boundary checked 2026-09-03.
- Platform or physical form: authored first-person action campaign on Windows;
  one complete early base-game episode under the current Ultimate entitlement.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  knowledge and evidence progression; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official EA PC manual](https://eaassets-a.akamaihd.net/eahelp/manuals/battlefield-hardline-manual_PC_us.pdf),
    for PC controls, campaign HUD, scanner, evidence, warrants, Expert Rank,
    arrest, `Freeze`, compliance, awareness, Episode screen and mode separation.
  - **[P2]** [official Steam product](https://store.steampowered.com/app/1238880/Hardline/),
    for current Windows sale, Ultimate entitlement, single-player/online split,
    EA-account activation and included Premium/expansion extras excluded here.
  - **[P3]** [official EA console sunset notice](https://forums.ea.com/blog/battlefield-game-info-hub-en/bf-comms-battlefield-hardline-on-consoles/13278624/replies/13291149),
    for the explicit statement that the 2026 console closure does not affect PC.
  - **[P4]** [official EA service updates](https://www.ea.com/legal/service-updates/a-h),
    for platform-specific Hardline service retirement rather than a PC delisting.
  - **[P5]** [official launch guide](https://www.ea.com/games/battlefield/news/battlefield-hardline-launch-all-you-need-to-know),
    for campaign/multiplayer separation and the campaign as controls practice.
  - **[P6]** [official single-player strategy article](https://www.ea.com/games/battlefield/news/the-unique-strategy-of-battlefield-hardline),
    for stealth, surveying, the campaign-exclusive Scanner, analysis and intel.
  - **[P7]** [official story article](https://www.ea.com/games/battlefield/news/the-unique-story-of-battlefield-hardline),
    for the ten-episode campaign structure. Its embedded video was not opened.
- Secondary and reproducible textual sources:
  - **[S1]** [SteamDB depots](https://steamdb.info/app/1238880/depots/), observed
    2026-09-03, for public Build `10351826`, its timestamps and separate Windows
    base/DLC depots. SteamDB is a secondary distribution mirror.
  - **[S2]** [Prima Episode 1 route](https://primagames.com/news/battlefield-hardline-episode-1-back-school-save-tyson),
    for `Back to School` ordering, shell-casing diversion, Tap analysis,
    warrant arrest, mandatory evidence, school routes and final open defence.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P7` and `S1`–`S2` under the fixed PC build, difficulty, episode and
  successor-terminal contract; no audiovisual playback or direct-play claim.
- Accessed: all sources 2026-09-03. Claim IDs: `BFH-001`–`BFH-013`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: navigate the first-person body; `ACT-161`: aim and commit
  a firearm, CEW or ordinary close attack; `ACT-164`: select a carried weapon;
  `ACT-183`: reload from finite reserve; `ACT-202`: enter or leave crouch;
  `ACT-235`: neutralise an eligible unaware target from valid rear reach.
- Existing `ACT-313`: hold the active scanner on an eligible evidence/suspect
  target until analysis completes; `ACT-405`: mark one visible living target;
  `ACT-406`: aim and throw one inert shell-casing diversion.
- New `ACT-417`: while aiming with legal authority, command eligible hostile
  suspects to comply and complete a living arrest once one is controlled and
  reachable. Target identities and the number frozen are parameters.
- Claims: `BFH-005`, `BFH-006`, `BFH-008`, `BFH-009`, `BFH-011`.

### System Behaviour Genes

- Existing `SYS-057`: a patrol redirects after perceiving the explicit casing
  stimulus; `SYS-208`: ranged fire resolves through aim, body and cover state;
  `SYS-215`: police, suspects and the protected partner exchange live attacks.
- Existing `SYS-299`: Expert awards cross rank thresholds into gear-unlock
  opportunities; `SYS-369`: accepted death/failure restores a checkpoint;
  `SYS-373`: sight, sound and actions escalate suspicion into attack;
  `SYS-379`: completed authored objectives advance the episode and successor;
  `SYS-680`: examined evidence becomes Case File/objective progress;
  `SYS-747`: completed scanner tags remain actor-bound through occlusion.
- New `SYS-766`: eligible armed hostiles enter compliance after an accepted
  authority command, remain controlled only under sufficient player or partner
  threat coverage, and leave that state through arrest, attack or lost control.
- Resolution order: accept movement, posture, scanner, diversion, command or
  attack input; validate sight, reach, equipment and awareness; update marks,
  evidence and perception; resolve compliance/arrest or live combat; update
  health, ammunition, Expert and objective state; restore failure; settle the
  final defence into episode completion and successor access.
- Claims: `BFH-006`–`BFH-012`.

### Constraint Genes

- Existing `CON-262`: carried weapon, magazine and reserve ammunition are
  finite; `CON-282`: episode encounters require authored predecessor,
  evidence, location and defence gates; `CON-285`: weapon operation requires
  compatible live equipment; `CON-330`: protagonist, partner and operation
  area must remain viable; `CON-335`: rear neutralisation requires an unaware,
  reachable eligible target.
- New `CON-587`: a living arrest requires an eligible alive suspect in valid
  reach and a legal unaware or compliant state; compliance itself requires
  sufficient continuing threat coverage until custody completes.
- Scarce resources: unseen approach time, cover, aim coverage, ammunition,
  health, partner viability and warrant/evidence opportunity.
- Claims: `BFH-008`, `BFH-009`, `BFH-011`, `BFH-012`.

### Information Genes

- Existing `INF-073`: active weapon and ammunition state are visible;
  `INF-115`: local sight and sound expose only partial hostile state;
  `INF-119`: protagonist/partner health are visible; `INF-125`: current
  objective, map route and successor gate are inspectable; `INF-287`: scanner
  marks, minimap/vision direction and awareness progress share a tactical view.
- New `INF-293`: scanner and Episode interfaces expose target classification,
  analysed evidence, warrant custody outcome, Expert score/rank and retained
  episode progress without revealing unexamined future targets.
- Exact colours, icons, layout, score values and names are parameters.
- Claims: `BFH-006`, `BFH-007`, `BFH-009`–`BFH-011`.

### Objective Genes

- New `OBJ-151`: complete one authored investigative episode by satisfying its
  required evidence, custody/combat and protection gates, reach episode
  settlement and retain its evaluated progress plus successor access.
- A killed warrant suspect may reduce evaluation without invalidating episode
  completion. A final firefight victory without the episode-complete transition
  is not yet positive; death/partner failure is negative and checkpoint-retryable.
- Claims: `BFH-009`–`BFH-012`.

### Time Genes

- Existing `TIM-003`: patrols, awareness, compliance coverage, aiming, combat,
  partner danger and objective windows advance in real time. Menu and Episode
  selection are setup/inspection surfaces, not a second time model.
- Claims: `BFH-007`, `BFH-008`, `BFH-011`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh `Officer` campaign has cleared the Prologue | Select Episode 1 and accept its first control | `Back to School` loads with campaign-only Scanner/Freeze grammar | exact entry | `BFH-003`, `BFH-005` |
| A visible eligible actor or evidence object is in scanner range | Hold scan or focus a mark | Identity/evidence analysis advances or an actor-bound mark is retained | acquired tactical knowledge | `BFH-006`, `BFH-007` |
| An eligible patrol can perceive a chosen landing point | Throw one shell casing | Patrol investigates the explicit non-damaging stimulus | route diversion | `BFH-005`, `BFH-011` |
| Up to the supported nearby hostile group is eligible and covered | Aim and issue `Freeze` | Hostiles surrender while sufficient player/partner coverage remains | coercive control state | `BFH-008` |
| A living warrant suspect is analysed, compliant/unaware and reachable | Complete arrest | Custody remains valid and grants the living-arrest Expert outcome | evaluated nonlethal branch | `BFH-009` |
| Evidence is eligible and scanner analysis completes | Inspect the evidence record | Case File and Expert/objective progress update | authored investigation | `BFH-010` |
| Detection completes or the authored final defence begins | Aim, fire, switch and reload | Live body/cover hits, health and ammunition resolve until the required threat ends | recoverable combat branch | `BFH-011` |
| Protagonist or mission-critical partner becomes non-viable | Accept failure | Current attempt ends and an authored checkpoint may restore | negative terminal | `BFH-012` |
| Every mandatory Episode 1 gate and final defence is complete | Accept episode settlement | Evaluation is recorded and the Episode surface exposes the successor | positive terminal | `BFH-009`–`BFH-012` |

## Strategic and experiential structure

- Local: decide whether new scanner knowledge supports diversion, rear
  approach, aimed compliance, custody or immediate firearm/CEW pressure.
- Medium-term: preserve unseen position and coverage long enough to convert
  risky hostiles into higher-value living arrests while still advancing every
  mandatory evidence and protection gate.
- Long-term: carry target/evidence evaluation through the authored school route
  and compulsory firefight into an episode-complete successor state.
- Heuristics: scan before entry; tag lines of sight; separate patrols with a
  casing; do not freeze more suspects than player/partner coverage can hold;
  prioritise living warrant custody when legal; change to combat when control
  collapses; do not stop before episode settlement.
- Failure attribution: marks/cones/awareness explain detection; compliance and
  reach explain failed arrest; weapon/health HUD explains combat loss; Case
  File, warrant and Expert surfaces explain evaluation; objectives and Episode
  screen explain route and terminal state.
- Trust: official control and interface descriptions, explicit authored gates,
  visible threat/evidence classification and discrete episode settlement make
  the bounded trace reviewable despite the absence of direct play.

## Replay and variation

- Attempts vary by patrol position, casing landing, mark order, arrest versus
  takedown/combat choice, coverage loss, exact damage/ammunition, checkpoint
  retries, optional warrant outcome, Expert score and duration.
- Episode locations and mandatory gates are authored rather than procedural;
  local hostile reactions and combat trajectories vary in real time.
- Stealth, living arrest and open combat can be mixed, but the final firefight
  remains mandatory. A replay may improve warrant/evidence/Expert evaluation;
  the canonical packet stops at the first valid episode completion.

## Adjacent systems and history

- Battlefield 2042 shares direct gunplay and mission information but its scoped
  Conquest match uses nested territory/ticket attrition, not evidence, custody
  or campaign settlement. Battlefield V's scoped multiplayer route likewise
  lacks scanner-led warrant evaluation.
- Far Cry 3 is the closest prior genome: both use optical actor marks, inert
  diversion, awareness transitions, rear neutralisation and recoverable
  firearm combat. Hardline adds aimed authority, coverage-dependent hostile
  compliance, living arrest, evidence/warrant scoring and a complete Episode
  terminal instead of converting an outpost into services.
- PAYDAY 2/3 manage compliant civilians or hostages inside heists. Hardline
  commands armed hostile suspects for living custody and Expert evaluation;
  it has no cable-tie stock, loot transport, alarm-phase economy or escape
  payout in this scope.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-202`, `ACT-235`, `ACT-313`, `ACT-405`, `ACT-406`, `ACT-417` | movement, combat, scanner, diversion and living arrest |
| System Behaviour | `SYS-057`, `SYS-208`, `SYS-215`, `SYS-299`, `SYS-369`, `SYS-373`, `SYS-379`, `SYS-680`, `SYS-747`, `SYS-766` | perception, combat, progress, evidence, marks and compliance |
| Constraint | `CON-262`, `CON-282`, `CON-285`, `CON-330`, `CON-335`, `CON-587` | finite gear, authored order, viability and arrest legality |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-287`, `INF-293` | gear, local state, objectives, recon and evaluation |
| Objective | `OBJ-151` | investigative episode settlement and successor |
| Time | `TIM-003` | continuous patrol, coverage and combat pressure |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `242` (`GAME-0001`–`GAME-0242`).
- Exact genome matches: none.
- Tied near matches: `GAME-0236` — Far Cry 3 (`25 / 39 = 0.641026`).
- Supported combination subsets: `COMB-0241`.
- Scan date: 2026-09-03.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0236` — Far Cry 3 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-202`, `ACT-235`, `ACT-405`, `ACT-406`, `SYS-057`, `SYS-208`, `SYS-215`, `SYS-369`, `SYS-373`, `SYS-747`, `CON-262`, `CON-282`, `CON-285`, `CON-330`, `CON-335`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-287`, `TIM-003` | Both support pre-contact marking, inert diversion, escalating detection, rear neutralisation and firearm recovery. Far Cry converts a finite hostile site into retained services; Hardline analyses evidence and warrants, maintains armed-suspect compliance, rewards living custody and settles a complete investigative episode | Near, `25 / 39 = 0.641026` |

### Preserved research notes

- New genes: `ACT-417`, `SYS-766`, `CON-587`, `INF-293`, `OBJ-151`.
- Reused genes: twenty-nine lower IDs; no earlier reviewed signature changed.
- Classification: `New gene` and `New combination of known and new genes`.
- Lower-ID scan retained `ACT-313` for held target analysis, `ACT-405` for
  living-actor marking, `ACT-406` for inert diversion, `SYS-680` for authored
  evidence progress and `SYS-299` for thresholded Expert progression. It
  rejected `ACT-358` / `SYS-646` / `CON-526`, whose heist grammar is civilian
  hostage control with finite restraints rather than hostile legal custody.

## Taxonomy impact

- Registry changes: five bounded Active genes and `COMB-0241`; no earlier
  reviewed game signature changes.
- Canonical labels describe transferable mechanics. Episode, warrant, suspect,
  school, partner, score, difficulty and build names/numbers remain parameters.
- Family placement: `FAM-009`, `FAM-010`, `FAM-012`, `FAM-017`.
- Combination-subset scan: no prior combination is an exact match for the
  scanner-mark/diversion/compliance/evidence/episode core; repository validation
  checks proper-subset and reciprocal links.

## Negative results

- Rejected `ACT-358`, `SYS-646` and `CON-526`: those genes require civilian
  hostage control and finite heist restraints, while this packet arrests armed
  hostile suspects through legal authority and continuing threat coverage.
- Rejected a game-specific “scan a warrant target” label. `ACT-313`, `ACT-405`
  and `SYS-680` already separate held analysis, actor marking and authored
  evidence conversion; warrant identity and payout stay parameters.
- Rejected multiplayer spotting, loadout, Battlepack and Premium genes because
  no multiplayer surface enters Episode 1.
- Rejected a generic kill-every-enemy objective: living custody may improve the
  evaluated result and the mandatory final defence is only one gate before the
  episode-complete terminal.
