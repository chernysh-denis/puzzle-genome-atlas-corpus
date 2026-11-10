---
game_id: GAME-0488
slug: wipeout
game_title: wipEout
analysis_status: reviewed
reviewed: 2026-10-03
combination_ids: []
gene_ids:
  action:
    - ACT-190
    - ACT-290
    - ACT-308
    - ACT-609
  system:
    - SYS-045
    - SYS-320
    - SYS-380
    - SYS-516
    - SYS-1300
    - SYS-1301
    - SYS-1302
  constraint:
    - CON-269
    - CON-438
  information:
    - INF-205
    - INF-465
  objective:
    - OBJ-257
  time:
    - TIM-003
---

# Game: wipEout — one original PlayStation Single Race

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Speed class, craft, pilot, course, weapon types and thrust thresholds are
parameters, not separate genes.

## Analysis scope

- Version / ruleset: original 1995 English North American PlayStation wipEout,
  reconstructed from its US longbox instruction booklet. One complete
  single-player Single Race, Venom class, Altima VII, FEISAR with Paul Jackson,
  standard digital controller/default mapping and initial exterior chase view.
  This configuration is an explicit analytical declaration, not a claim of a
  measured default opening. Exact disc revision and regional binary parity
  were not inspected. Structured target: `PLAT-PLAYSTATION` in
  `knowledge/platforms/games.json`.
- Primary decision loop: prepare thrust for the start signal; steer, choose
  thrust and separate left/right airbrakes, adjust pitch over crests and ramps,
  choose whether to cross a dash pad, cross a weapons grid to enable one
  function, and commit its legal deployment while seven computer rivals keep
  racing. Read place, lap, clock, speed and readiness; revise the line and
  deployment timing through three complete laps to the classified finish.
- Entry and exit: start at the pre-race countdown of the declared selected
  field. End at the first three-lap classified result, or abort on quit/restart.
  First place is the local positive target; another classified place ends the
  attempt without satisfying that target. No Championship qualification,
  trophy, points, retained currency or Rapier unlock follows this packet.
- Included: continuous hovercraft motion and course contact, seven autonomous
  rivals, direct steering/thrust/airbrakes, pitch authority, source-reported
  conditional start boost, immediate fixed dash-pad acceleration, one enabled
  grid function, all six documented one-player weapon/power-up types, temporary
  effect expiry and active-shield deployment gating, current race/control
  feedback, fixed-view toggle, declared pause and finite race settlement.
- Excluded: Championship's point table, three lives per track and six-course
  Rapier unlock; Time Trial with weapons disabled; other tracks or secret
  Firestar; two-machine link play, two-player-only RevCon and unexplained ECM;
  record/configuration saving; further races; neGcon-specific mappings; Saturn,
  DOS, sequels, Omega Collection or a modern rewrite. One ready function plus
  an ongoing shield is not an asserted two-slot item queue. No precise weapon
  selection/replacement policy, health gauge, airbrake coefficient, native
  frame window, internal checkpoint geometry, AI difficulty scaling or
  simultaneous terminal precedence is claimed.
- Potential scoped modules: a full Championship through the Venom points
  table; weapon-free Time Trial; original linked two-player supply/effects.
  These require independent admission, not silent inheritance into this race.
- Direct-play status: no executable, disc, emulator, save, game screenshot,
  video, audio or input trace was run or inspected. The complete relevant
  original booklet and its mode/control/HUD/shield/weapon pages were read,
  including visual checks of PDF leaves 11–12 and 16–18. S1 is a contemporary
  writer's own play account, not ours; its pitch, pad and start observations
  remain source-limited and its preferred tactics are not optimality proofs.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `WO-001` | Single Race permits one selected course, team and pilot; three laps run against the full eight-pilot field, distinct from Championship and weapon-free Time Trial | Observation | Direct | High | P1 printed 0.09–0.10 |
| `WO-002` | Default steering, thrust, separate airbrakes and view toggle directly control the same hovercraft; vertical directional input supplies source-reported pitch control over crests/ramps | Observation | Corroborated | Medium | P1 printed 0.14; S1 preliminary notes |
| `WO-003` | Fixed dash-pad contact adds immediate speed and its placement can make the next corner harder; it is not the weapons grid or a stored turbo reserve | Observation | Direct | Medium | S1 preliminary notes and Altima route |
| `WO-004` | A weapons grid enables one function for later deployment; an active shield permits another pickup but blocks another deployment until protection ends | Observation | Direct | High | P1 printed 0.15–0.16 |
| `WO-005` | Six one-player functions include straight rocket, homing missile, five short-lived mines, control-disturbing shockwave, temporary protective shield and turbo burst | Observation | Corroborated | High | P1 printed 0.15–0.16; S1 function descriptions |
| `WO-006` | Current lap/place/time, speed and weapon identity are displayed; applicable local target cues are reported without a guaranteed future hit | Observation | Corroborated | Medium | P1 printed 0.14; S1 function descriptions |
| `WO-007` | A qualifying thrust state at the start signal can grant a launch acceleration advantage; exact native timing has not been measured | Observation | Direct | Medium | S1 preliminary notes |
| `WO-008` | Race motion and temporary effects continue under live control except at declared pause; the finite single-race result does not award Championship qualification | Observation | Direct | High | P1 printed 0.09–0.10, 0.14–0.16 |
| `WO-009` | The guide's uncertain grid-colour observation does not prove an original RNG policy, and its unlock shorthand differs from the manual's complete points-table condition | Observation | Conflicting | Medium | P1 printed 0.09; S1 objectives and supply |
| `WO-010` | No original program, direct play, native timing, exact state/seed or full-slot replacement policy was inspected | Confirmed | Direct | High | R1 |

## Basic data

- Origin: Psygnosis's original 1995 anti-gravity racing game, not wipEout 2097,
  XL, Wip3out or a later collection. Sony's historical page supports product
  and PlayStation identity, not detailed original mechanics.
- Mechanical families: `FAM-007` through momentum, pitch and course contact;
  `FAM-009` through positional weapon/protection decisions against live rivals;
  `FAM-010` through continuously changing race and temporary-effect state.
  Every other family boundary was tested; no route construction, inventory
  delivery, agent-role coordination or persistent dependency campaign applies.
- **P1:** [original US longbox PlayStation instruction booklet](https://www.videogamemanual.com/ps1/Wipeout%20%28LB%29%20%28USA%29.pdf),
  publisher-authored artifact on a third-party manual archive, inspected
  2026-10-03. Twenty-four PDF leaves; printed 0.08–0.10, 0.14–0.17 cover the
  admitted rules and excluded modes. Download SHA-256
  `3a694240b231b37aa38632a65d410306413d07883ba6c208da73d9a68b46c581`.
  It is a scanned manual, not an original executable or an authorised game copy.
- **S1:** [Game Zero's dated original-game strategy account](https://www.gamezero.com/team-0/pro_page/faq/wipeout.html),
  edited/posted by Bryan aka R.I.P., dated 1995-10-23, inspected 2026-10-03.
  Its primary firsthand observations supply pitch, fixed pad contact and
  conditional launch; numerical contact thresholds are not independently
  measured. Course spelling follows P1 where S1 has transcription errors.
- **P2:** [Sony's PlayStation history](https://www.playstation.com/en-gb/playstation-history/1994-ps-one/),
  inspected 2026-10-03; official product/history destination, not an available
  original game download or proof of remake/port equivalence.
- **R1:** source-only preflight and manual visual inspection for this unit.
  Modern rewrite, DOS and later-sequel manuals were not rule authorities.

## Mechanical decomposition

### Action Genes

- `ACT-290`: directly steer and apply thrust/left-right airbrakes to the
  assigned craft. Gearbox and seat-entry are not admitted parameters here.
- `ACT-308`: nose pitch beyond ground steering is supported by S1; no player
  jump button or Rocket League dodge stock is invented.
- `ACT-190`: deploy the current enabled limited race function with its legal
  directional, target or no-target form. It is not an ordinary unlimited gun.
- `ACT-609`: toggle cockpit/exterior viewpoint while preserving craft state.
  It changes visibility, not traversable geometry. Claims: `WO-002`, `WO-004`.

### System Behaviour Genes

- `SYS-320` integrates craft motion, momentum and track/contact response;
  losing speed does not establish vehicle health or an energy reserve.
  `SYS-045` supplies autonomous rival locomotion and `SYS-516` the three-lap
  progress and classification. No independently difficulty-scaled AI field is
  asserted from the Venom speed-class label.
- `SYS-1301` applies a dash pad's immediate acceleration without banking it;
  `SYS-1302` supplies a source-reported conditional pre-start launch. These
  have distinct triggers from each other and from the activated turbo function.
- `SYS-1300` enables a grid function for later deployment, not automatic attack
  on contact. The manual allows pickup under an active shield; replacement
  when a function is already ready and the exact selection algorithm are open.
- `SYS-380` transfers typed limited active effects. Rocket follows the road
  forward without homing; missile seeks a target; a five-mine batch remains
  briefly before expiry; shockwave stalls/shakes and impairs control; shield
  temporarily prevents weapon slowdown; turbo adds a short speed burst.
  This effect layer is distinct from availability and player commitment.
  No RevCon, ECM, persistent HP depletion or total collision immunity enters.
  Claims: `WO-001`–`WO-005`, `WO-007`–`WO-009`.

### Constraint Genes

- `CON-269` gates deployment by the enabled function and disabling/protective
  state; another pickup during shield does not permit another deployment.
- `CON-438` requires the declared three complete course laps before a valid
  finish. Exact internal checkpoint shape and reverse-line exploit response
  remain uninspected, not asserted from a booklet diagram.
  Claims: `WO-001`, `WO-004`, `WO-008`.

### Information Genes

- `INF-205` discloses place, lap progress, current lap time/record and locally
  visible competitors. `INF-465` separately discloses speed, enabled function
  and applicable local targeting cue. The native future supply, opponent input,
  exact remaining shield time and guaranteed impact are not thereby visible.
  Claims: `WO-006`, `WO-009`.

### Objective Genes

- `OBJ-257` is first place at this single finite race's classified finish,
  without subsequent career award or cup points. `TAXONOMY_CHANGE_225` removes
  the original carrier's downhill-only parameter from the general boundary;
  SSX Tricky's Garibaldi remains unchanged. A lower place is an ended attempt,
  not the selected positive target or implicit Championship qualification.
  Claims: `WO-001`, `WO-008`.

### Time Genes

- `TIM-003` retains continuous live craft/rival/effect state while decisions
  remain open. Explicit pause/Continue does not turn racing into discrete turns.
  Restart and quit abort this first-attempt packet; the manual's restart
  life-cost wording does not establish a Single Race three-life economy.
  Claims: `WO-008`, `WO-010`.

## Reproducible transitions

These are source-bounded transition recipes, not an executed native trace.
Reproduction must retain the declared original disc, controller mapping,
course/craft/pilot, starting state, frame inputs and any item-selection state.

| State | Intervention | Source-supported result | Boundary / limitation | Claims |
|---|---|---|---|---|
| Declared craft at pre-start countdown | Meet the guide's qualifying thrust condition at signal | Source-reported acceleration advantage at launch | No exact native-frame window or guarantee from holding maximum throughout | WO-007 |
| Craft approaches a crest or ramp | Adjust vertical directional pitch input | Nose orientation changes traversal/landing opportunity | Not a free jump or open three-axis flight | WO-002 |
| Craft contacts a fixed dash pad | Continue the racing line through contact | Immediate speed burst | No saved turbo reserve; extra speed may harm corner entry | WO-003 |
| No enabled function, eligible weapons grid | Cross the coloured region | Function becomes available for later use | Exact random/colour selection policy remains unresolved | WO-004, WO-009 |
| Enabled function and legal deployment | Commit the function | Its typed projectile, mine, shield, control or turbo effect resolves | Not an unlimited ordinary attack | WO-005 |
| Temporary shield active | Cross a weapons grid, then request another function | Pickup is possible, deployment remains gated until protection expires | An active effect is not an asserted reserve item slot | WO-004 |
| Projectile approaches protected craft | Resolve eligible shield interaction | Weapon does not produce its ordinary slowdown during protection | All wall contact immunity and health restoration are unproved | WO-005 |
| Mines remain behind the craft | Wait or a rival reaches contact | Source-described contact slowdown or automatic short-lived expiry | No exact lifetime coefficient or persistent obstacle claim | WO-005 |
| Current craft view is cockpit/exterior | Toggle view | Same race and craft state, different fixed viewpoint | No changed physical track or controlled actor | WO-002 |
| Current race under live control | Pause then Continue | Declared pause suspends racing; Continue returns to live input | Not timed-turn scheduling | WO-008 |
| One or two complete laps | Cross a valid lap finish | Progress continues rather than final classification | Internal checkpoint code is uninspected | WO-001, WO-008 |
| Third complete lap ends | Accept classified result | First wins local target; lower place still ends the attempt | No Championship points, three-life assertion or Rapier unlock | WO-001, WO-008 |

## Strategic and experiential structure

Higher speed shortens traversal but makes bend preparation and landing harder.
Airbrakes, early steering and pitch can trade a clean line against raw speed.
Crossing a dash pad and selecting a weapons grid are different interventions;
one alters speed now, the other prepares a later effect. An attack may disturb
the rival ahead while shield or turbo offers a different timing opportunity.
Protection blocks spending the next ready function even though pickup remains
possible. No guide's preferred line, airbrake avoidance or launch trick is
promoted to a proven dominant policy.

## Replay and variation

The declared craft/course configuration can be varied only as a new recorded
entry. Ready-function outcome, rival positions, pitch and deployment timing
change decisions within this attempt. Other speed classes, unlock paths or
regional implementations require further evidence. Hidden supply policy and
simultaneous expiry/contact precedence remain open questions.

## Adjacent systems and history

The original Single Race differs from Championship qualification and from
weapon-free Time Trial. Later sequels and a modern source rewrite are not
binary evidence for the original PS1 mechanics. The primary booklet governs
mode names and unlock conditions where the contemporary guide abbreviates
them. A circuit race and a downhill descent can share a classified-first
objective without proving historical influence or equal experience.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
|---|---|---|
| Action | `ACT-190`, `ACT-290`, `ACT-308`, `ACT-609` | function deployment, driving, pitch, fixed view |
| System Behaviour | `SYS-045`, `SYS-320`, `SYS-380`, `SYS-516`, `SYS-1300`–`SYS-1302` | autonomous rivals, motion/contact, typed function, finish, grid, pad, launch |
| Constraint | `CON-269`, `CON-438` | readiness/shield, required circuit laps |
| Information | `INF-205`, `INF-465` | place/lap/time, speed/function/target |
| Objective | `OBJ-257` | one standalone race first place |
| Time | `TIM-003` | live race except explicit pause |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `487` (`GAME-0001`–`GAME-0487`).
- Exact genome matches: none.
- Tied near matches: `GAME-0216` — Trackmania (`6 / 22 = 0.272727`).
- Supported combination subsets: none.
- Scan date: 2026-10-03.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0216` Trackmania | `ACT-290`, `SYS-320`, `SYS-516`, `CON-438`, `INF-205`, `TIM-003`: direct vehicle control, contact motion, valid course/lap result, progress feedback and live input. | Trackmania's fixed CarSport time trial has a timed target and resets without a rival field. wipEout adds pitch, seven autonomous rivals, conditional launch, immediate dash pads and a ready grid weapon with shield gating; classified first place is this standalone positive target. No quick-reset authority, exact Trackmania gates or CarSport controls transfer. | Near; `6 / 22 = 0.272727`. |

## Taxonomy impact

Four bounded additions and thirteen reuses are admitted by
[`TAXONOMY_CHANGE_225`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_225.md).
One objective is generalised by removing a carrier/course parameter, without
changing any earlier signature. Named causal-role and all-role plain-language
review partition the complete seventeen-use genome, not an automatic rarity
classification. No verified combination is invented for a single carrier.

## Negative results

- Reject a proven original RNG policy or weighted two-slot weapon queue from
  the guide's uncertain colour observations or from active shield plus pickup.
- Reject health damage, contact immunity, infinite ordinary fire, kart-specific
  coin/drift effects, difficulty scaling and precise uninspected native timings.
- Reject Championship progression, three-life Single Race economy, linked
  two-player RevCon/ECM and modern port equivalence.

## Delta summary

## New facts

- [Observation | Corroborated | Medium] A complete single race separates immediate road-pad speed, later grid-function deployment and conditional start thrust; an active shield allows pickup but blocks another deployment. `WO-001`–`WO-009`.

## New genes

- [Observation | Corroborated | Medium] Four additions isolate distinct contact, launch, supply and disclosure boundaries; thirteen existing boundaries transfer.

## New combinations

- [Observation | Limited | Medium] No new verified combination is proposed; every existing proper subset is checked against the complete admitted signature.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_225` generalises the standalone first-place objective without changing an earlier signature.

## New questions

- What original disc/revision and precise control/physics values reproduce this
  source packet? What differs across regions or subsequent releases?
- What enables or replaces a grid function when one is already ready? Is the
  guide's observed colour association causal, deterministic or merely apparent?
- What are native pad/contact, thrust-start and temporary-effect windows?
- How are missed-course progress, simultaneous shield expiry and weapon impact
  resolved in the native program? No unobserved answer is admitted.

## Next recommended game

- [Hypothesis | Limited | Medium] Original Game Boy Advance Golden Sun, `GAME-0489`, is next after complete acceptance.
- Optimisation criterion: preserve the approved platform and decision-structure diversity.
- Expected information gain: a source-bounded party encounter with elemental resource and target decisions rather than hover-race supply.
- Backlog impact: seven approved subjects remain; no next unit begins in this commit.

## Why this game

- [Hypothesis | Limited | Medium] Original PlayStation anti-gravity racing tests transfer of vehicle, live ability and classified-result boundaries without importing a championship or sequel mechanics.

## Research outcome

- Outcome: one full source-bounded original Single Race, not Championship,
  Time Trial, a later rewrite or an artwork-only initial state.
- Acceptance: [`GAME_0488_ACCEPTANCE`](../../../research/checkpoints/GAME_0488_ACCEPTANCE.md)
  owns complete bilingual/artwork/browser/gate and advisory evidence.
- Next unit: `GAME-0489` original Game Boy Advance Golden Sun, only after
  final acceptance, one local commit and the 30-second Goal stop window.
- No push, public corpus revision, mapping change or deployment authorised.
