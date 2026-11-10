---
game_id: GAME-0507
slug: motorstorm
game_title: MotorStorm
analysis_status: reviewed
reviewed: 2026-10-06
combination_ids: []
gene_ids:
  action:
    - ACT-290
    - ACT-293
    - ACT-308
    - ACT-350
    - ACT-379
    - ACT-609
    - ACT-610
    - ACT-694
    - ACT-695
    - ACT-696
  system:
    - SYS-036
    - SYS-215
    - SYS-320
    - SYS-515
    - SYS-516
    - SYS-519
    - SYS-1421
    - SYS-1422
    - SYS-1423
    - SYS-1424
  constraint:
    - CON-437
    - CON-438
    - CON-784
  information:
    - INF-205
    - INF-206
    - INF-208
    - INF-491
  objective:
    - OBJ-150
  time:
    - TIM-003
---

# Game: MotorStorm — first Grizzly Festival ticket

Use the canonical [vocabulary and signature](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Class names, model, controller, race position, route geometry, heat rates and
medal payout are parameters, not additional genes.

## Analysis scope

- Version / ruleset: original English PlayStation 3 base MotorStorm Festival
  rules reconstructed from Sony's US booklet printed 2007-01-18 and attributed
  original-PS3 recording R1 published 2019-06-02. The captured installed patch,
  disc region and language-dependent parity were not independently established.
  This is a dated documentary packet, not verified launch-binary execution or
  a declaration that later updates have identical rules.
- Structured analysis target: PLAT-PLAYSTATION-3; original English retail base
  edition, first Festival ticket In at the Deep End, A Taste Of Violence on The
  Grizzly, Level 1 / Anything. DLC and sequels are not this target.
- Primary decision loop: choose one admitted unlocked class and offered vehicle;
  steer, accelerate, brake and orient it through class-dependent rejoining
  routes against live autonomous rivals; hold or release boost against engine
  heat, choose local contact or an eligible rider attack, and recover from a
  wreck or requested track reset; complete the course within the accepted
  top-three places and return to the ticket menu with medal and respect retained.
- Entry and exit: begin at the unlocked first ticket's event/class/vehicle
  commitment. Include every offered choice among all seven classes, not only
  R1's Patriot Surger rally car. End positively only after the classified
  top-three finish and returned menu retaining the medal/respect. A lower
  classified result or abandonment is non-completion and may lead to retry.
  R1's Gold example completes three physical circuits while HUD laps read
  0/2, 1/2 and 2/2, with fifteen participants including the player, then retains
  60/60 ticket points. Neither first crossing nor results animation alone is
  the terminal. Silver/Bronze exact amounts and repeat-credit policy are not
  inferred from that one Gold return.
- Included: unlocked ticket and offered class/model choice; class-specific
  traction, clearance, mass and control; the complete first authored course
  with connected high/dry and lower/muddy alternatives; throttle, steering,
  rear brake/handbrake, reverse, aerial orientation and bike/ATV weight shift;
  live mixed rivals, vehicle collision and dynamic environmental bodies;
  documented class-dependent soft-ground ruts; nearby contextual MX attacks;
  initial boost warm-up, held boost, cooling, warnings and explosive overheat;
  local wreck replacement and manual track recovery; forward/chase viewpoint
  changes for the five four-wheel classes, live look-around and ordinary pause;
  current place/lap/time, event terms, classified medal and respect settlement.
- Excluded: later Festival races as playable packets, online fields/Fame,
  Time Attack, Revenge Weekend, Eliminator, additional DLC inventory, Complete
  editions and sequels; unlock cheats and the historical infinite-boost exploit;
  player-directed flaming wrecks, finite recovery lives, on-foot play, purchased
  garage/tuning or selectable manual transmission; exact unmeasured heat,
  collision, attack, rut, difficulty, respawn and protection coefficients;
  native checkpoint shapes, route-shortcut rejection and save-file bytes.
  Secondary camera-dirt clearing and explosive-finish hints remain unverified
  for this exact installed offline packet rather than creating hidden guarantees.
- Potential scoped modules: later restricted-class tickets, online, Time Attack
  and DLC Eliminator require separately bounded rules and terminal evidence.
  No module IDs or exhaustive product-union signature are introduced.
- Direct-play status: no original PS3, disc, executable or own controller input
  was run. Original converted manual pages, creator accounts and attributed
  paused muted frames reconstruct the rules. R1 does not prove exact patch,
  region, native timing, each alternative class or save/reload fidelity. Media
  inspection was headless/background, muted and paused without foreground,
  fullscreen, focus, user-window or system-sound changes. Art is original
  interpretation, not an official asset or source screenshot.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| MS-001 | The first ticket offers A Taste Of Violence on The Grizzly at Level 1 / Anything; the Grizzly exception admits all seven classes. | Observation | Corroborated | High | P1 pp. 6–9; R1 180/210; indexed S1 |
| MS-002 | Class handling and surface/route fit differ; local alternatives rejoin the authored course rather than permanently removing the other route. | Observation | Corroborated | High | P1 pp. 14–15, 18–19; P2; R1 277 |
| MS-003 | The original controls expose direct driving, rear brake, vehicle-air orientation, weight shift, fixed four-wheel viewpoints and live panning. | Observation | Direct | High | P1 pp. 4–5, 12–15 |
| MS-004 | Boost first warms up, then held use raises acceleration/speed and engine heat; release permits recovery, while overuse explodes the engine. | Observation | Corroborated | High | P1 pp. 12–13; R1 290/495 |
| MS-005 | Destroyed vehicles rejoin locally stationary and briefly invulnerable, needing renewed acceleration; recovery is not whole-event elimination. | Observation | Direct | High | P1 pp. 18–19; R1 390 records a wreck, not recovery timing |
| MS-006 | The MX Bike shared action attacks a nearby eligible bike; without the attack context it performs a different action. Exact attack effect and cadence are unmeasured. | Observation | Direct | High | P1 pp. 12–13 |
| MS-007 | Vehicle properties affect soft-ground tyre ruts; subsequent contact changes steering. This is documentary evidence, not measured native deformation or cross-save persistence. | Observation | Corroborated | Medium | P4 creator statement; P5 publisher release |
| MS-008 | The manual supplies Reset to track; its local-return meaning is adopted, but placement, heat, immunity and clock treatment are not natively verified. | Observation | Limited | Medium | P1 pp. 4–5 |
| MS-009 | R1 shows fifteen total participants, zero-based three-circuit lap display, a classified Gold finish and returned first-ticket completion with 60/60 points. | Observation | Corroborated | High | R1 290/495/610/645/680; indexed S1 |
| MS-010 | Top-three results earn medals/respect; original Play progression uses ticket difficulty and retained respect. Later playable tickets are excluded here. | Observation | Corroborated | High | P1 pp. 8–9; R1 645/680 |
| MS-011 | Running rivals, physics and race clock continue while commands are accepted; the ordinary pause is a planning parameter, not a turn system. | Observation | Corroborated | High | P1 controls/HUD; R1 290–610 |
| MS-012 | Original manual and developer statements support vehicle dynamics and environmental body interaction; precise native solver and destructible-prop thresholds are unmeasured. | Observation | Corroborated | Medium | P1; P3 interview; P5 collision-part account; R1 390 |
| MS-013 | DLC Eliminator's guided flaming wreck is a different mode and must not be transferred into this base Festival race. | Observation | Direct | High | P2 |
| MS-014 | Exact installed patch, disc-region parity, native timing, Silver/Bronze payout and reset-state treatment remain unverified. | Observation | Limited | High | Source-review boundary |

## Basic data

- Release / origin: Evolution Studios / Sony Computer Entertainment, original
  PlayStation 3 MotorStorm; this target uses the English 2007 retail rule
  documentation rather than the earlier Japanese edition or a later sequel.
- Platform or physical form: original PlayStation 3 base Festival offline
  racing packet; the structured target owns platform identity, not an inferred
  catalogue of equivalent ports.
- Mechanical families: existing FAM-007 for momentum, terrain and collision;
  FAM-010 for racing under live rival and thermal pressure. Authored track
  choice is not constructing a transport network; view changes do not transform
  physical world topology. No new family is required.
- P1: [Sony original English MotorStorm PS3 booklet, converted preserved pages](https://www.manuals.ca/sony/motorstorm-ps3/manual).
  Printed mark MSps3MAN_11_mb, 2007-01-18. Actually inspected viewer pages 4,
  5, 6, 8, 9 and 11 correspond to printed pp. 4–9, 12–15 and 18–19.
  Controller glyph conversion is not independent button-label proof; page 10
  contains no extracted rule text and its images were not inspected.
- P2: [Evolution's MotorStorm Revenge Weekend description](https://blog.playstation.com/2007/09/06/motorstorm-revenge-weekend/),
  Jed Ashforth, 2007-09-06. Creator evidence distinguishes seven-class track
  design from update-2.0-dependent DLC and online Eliminator; that update
  requirement does not identify the installed patch in R1.
- P3: [Beyond3D interview with Evolution technical director Scott Kirkland](https://www.beyond3d.com/content/interviews/38/),
  2007-05-10. The attributed technical answers support Havok vehicle dynamics,
  suspension and environmental interaction. Editorial introduction is not a
  creator quote, and rendered-body count is not participant count.
- P4: [Contemporary report with designer Paul Rustchynsky's terrain account](https://www.wired.com/2007/04/ridin-dirty/),
  Chris Kohler, 2007-04-01. Class-dependent tyre ruts and later steering
  consequences support MS-007 with documentary qualification. Its online
  nuisance example does not independently prove every offline camera effect.
- P5: [Sony's original North American MotorStorm release announcement](https://sony.mediaroom.com/2007-03-06-MotorStorm-Delivers-the-Ultimate-Brutal-Off-Road-Racing-Experience-for-PLAYSTATION-3-System),
  2007-03-06. Publisher evidence establishes the regional release and supports
  racing-surface changes, collision-part loss and situational rival response.
  Promotional language does not prove exact physics or guaranteed unique laps.
- R1: [Paragleiber, MotorStorm PS3 first hour](https://www.youtube.com/watch?v=N5nzPqg6nsw),
  published 2019-06-02. Exact video ID and metadata duration 3795 seconds were
  checked. Actually inspected muted paused frames: 180, 210, 277, 290, 390,
  495, 610, 645, 655, 665 and 680 seconds. Captured 695, 730 and 770 concern
  the next selection and do not add later-race rules to this genome. No sound
  was played/analyzed and no claim of continuous direct play is made.
- S1: [Morpork's contemporary written guide](https://gamefaqs.gamespot.com/ps3/928393-motorstorm/faqs/48448),
  ver. 1.21, updated 2007-08-14. Only indexed passages were accessible after
  direct HTTP 403. Its first-ticket table corroborates total participants and
  the zero-based lap distinction; complete-guide inspection is not claimed.
- S2: [Contemporary MotorStorm hints](https://www.psu.com/news/motorstorm-cheats/),
  2007-04-08. View-dirt clearing and finish-overheat advice are secondary,
  unverified target hints. Listed cheats and guaranteed explosive advantage
  are excluded. Evidence checked 2026-10-06.
- Claim IDs: MS-001–MS-014.

## Mechanical decomposition

### Action Genes

- Reuse ACT-290 for direct driving, braking, reverse, rear brake and declared
  bike/ATV weight-shift input; ACT-293 for unlocked ticket/event commitment;
  ACT-308 for eligible in-air orientation; ACT-350 for requested track recovery;
  ACT-379 for deliberate vehicle-body contact with a rival.
- Reuse ACT-609 for the declared fixed Front Cam versus Chase Cam on buggy,
  rally car, racing truck, mudplugger and big rig. The original gene's Driver's
  Eye support is a forward driving view, not a requirement to render an actual
  cabin. No visible dashboard or four-wheel viewpoint switch on MX/ATV is
  invented. ACT-610 separately covers live look-around, not a rule-changing
  projection or a free camera teleport.
- New ACT-694 commits an unlocked offered class/model without a garage
  ownership transaction or selectable manual/automatic transmission.
- New ACT-695 holds/releases boost against accumulating heat rather than
  spending stored thrust. New ACT-696 issues the contextual mounted MX attack,
  with no guaranteed knock-off or asserted exact attack interval.
- Parameters: seven classes and offered models, current route, mass/traction,
  input device, boost duration, heat, local rival and viewing frame.
- Claim IDs: MS-001–MS-006, MS-008, MS-011.

### System Behaviour Genes

- Reuse SYS-320 for vehicle handling, surface traction and physical contact;
  SYS-036 for separately dynamic environmental bodies/wreck pieces, not a
  second steering model or unverified fragile-barrel durability threshold.
  SYS-215 resolves eligible mounted attack effects; incidental crash damage
  remains outside that combat gene. Native hit damage and rider-ejection
  conditions are not asserted from the action command alone.
- Reuse SYS-515 for the fixed-Level-1 autonomous mixed racing field, SYS-516
  for circuit/lap and classified finish validation, and SYS-519 for retained
  medal/respect. Internal checkpoint geometry is not exposed by the HUD alone.
- New SYS-1421 couples held boost to heat, cooling and destructive overuse;
  SYS-1422 replaces a destroyed racer locally with a stationary, briefly
  protected vehicle in the ongoing race. This is not an Eliminator guided
  wreck, own-side arena spawn or finite-life recovery.
- New SYS-1423 retains documentary class-dependent soft-ground ruts affecting
  later contact. No native rut-depth formula or cross-save persistence is
  inferred. New SYS-1424 records requested local track recovery without
  inventing its exact heat, clock, immunity or placement treatment.
- Resolution order: event/class admission → direct driving/contact/air input
  and eligible boost or contextual attack → running rival/body/contact and
  thermal response → wreck replacement or requested local recovery → valid
  circuit/lap finish and classification → medal/respect and menu return.
  Same-frame finish, explosion, impact and attack priority are not measured.
- Claim IDs: MS-002–MS-012.

### Constraint Genes

- Reuse CON-437 for first-event class/vehicle admission; Anything admits all
  seven classes here, not an arbitrary locked model or later DLC inventory.
  Reuse CON-438 for course/lap completion before valid finish. Rejoining local
  branches do not imply that any shortcut can bypass required course progress.
- New CON-784 prevents manual boost until initial warm-up completes even
  though ordinary driving already works. The captured CHARGING09 at clock1sec
  is not an independently measured universal warm-up constant.
- Heat safety, class capability and contact exposure parameterise the coupled
  system; no fuel tank, finite recovery stock or new per-class gene is added.
- Claim IDs: MS-001–MS-005, MS-009, MS-014.

### Information Genes

- Reuse INF-206 for ticket/course/class entry terms. Its existing cup/event
  transfer does not require an invented open-world map. Reuse INF-205 for
  current place, zero-based lap display, elapsed time and visible local rivals;
  INF-208 for classified performance and returned medal/respect state.
- New INF-491 exposes initial charging and thermal warning phases, not a
  consumed fuel/nitro quantity. It does not predict safe lines or future hits.
- A later vehicle-selection frame does not establish a disclosed threshold
  successor, so INF-207 is not assigned. Secondary dirt-clearing claims remain
  questions rather than native offline visibility guarantees.
- Claim IDs: MS-001, MS-004, MS-009–MS-010, MS-014.

### Objective Genes

- Reuse OBJ-150: valid finite race finish within the disclosed top-three
  accepted places followed by retained medal/respect and ticket-menu return.
  First place earns the observed Gold but is not the sole allowed progression
  result. Avoiding all crashes, knocking off a rider or using every class is
  not an independent required victory condition.
- Failure/non-completion: a lower classified result or abandonment; individual
  wrecks recover inside the race and do not permanently eliminate the player.
- Claim IDs: MS-005, MS-009–MS-010.

### Time Genes

- Reuse TIM-003: physics, rivals, heat and race time evolve while commands are
  accepted. Ordinary pause is its declared planning parameter, not a combat
  command-queue pause, reversible timeline or scheduled player-turn system.
- Claim IDs: MS-003–MS-005, MS-011.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Unlocked first Anything ticket | Choose an offered class/model and commit | Vehicle's handling/contact profile enters the same first course | class choice is causal, not only a livery | MS-001–MS-002 |
| Light bike approaches a rejoining route split | Steer toward a high narrow line | Different clearance/terrain tradeoff from a heavy lower-mud line | routes parameterise physical driving, not authored network construction | MS-002 |
| Already moving at race clock1sec, CHARGING09 visible | Request boost before readiness | Initial warm-up still prohibits boost, ordinary steering remains usable | movement and boost permission differ | MS-004 |
| Warm-up complete, engine below destructive heat | Hold boost | Acceleration/speed benefit and rising heat | inverse heat budget, not stored fuel | MS-004 |
| Heat approaches critical | Release boost | Eligible non-boost time permits recovery | release is a safety decision | MS-004 |
| Continue beyond destructive heat boundary | Keep boosting | Engine explosion invokes local wreck recovery | depletion is not merely no extra speed | MS-004–MS-005 |
| Vehicle destroyed | Await documented recovery then accelerate | Stationary briefly protected replacement resumes the ongoing race | no permanent elimination; exact delay unmeasured | MS-005 |
| Stranded/spun but event unfinished | Request Reset to track | Documented local course return, exact restored state unmeasured | recovery differs from full-grid retry | MS-008 |
| MX Bike with another eligible bike close by | Issue shared Action | Context-qualified attack resolves in live racing | mounted command differs from ramming | MS-006 |
| Same shared command without attack context | Issue Action | A different action is performed, not a remote guaranteed hit | proximity/context is material | MS-006 |
| Eligible soft racing ground | A class's tyres pass over it | Documentary ruts affect later contact | ground state differs from a cosmetic decal | MS-007 |
| Five-four-wheel-class driving | Switch fixed view or pan separately | Same vehicle authority remains, visible frame changes | no world-topology rewrite | MS-003 |
| HUDLAP0/2, then1/2, then2/2 | Complete the final physical circuit | R1 reaches a classified finish after three circuits | do not mistake zero-based display for two physical laps | MS-009 |
| Classified Gold in R1 | Continue to returned ticket menu | First ticket complete,60/60 respect visible | finish animation alone is not retained terminal | MS-009–MS-010 |

## Strategic and experiential structure

- Local decision: trade a class-fitting line, contact risk and boost time against
  heat, immediate rival spacing and the physical road ahead.
- Medium-term planning: heat left after one straight constrains the next
  opportunity; surface and rival interference can make the same local branch
  less useful on a later circuit. Exact rut or opponent-seed reproducibility
  is not claimed.
- Long-term structure: within this packet, a retained top-three medal/respect
  outcome is the target. Later ticket unlocking is context, not an analysed
  campaign decision union.
- Common heuristics: keep a light vehicle away from deep mud; do not copy that
  line blindly in a heavy rig; release boost before destructive overuse and
  accelerate again after stationary recovery. These are source-grounded
  recommendations, not proof of a universally fastest route.
- Failure attribution: terrain and heat warnings explain many local losses;
  tight contacts, opaque native recovery placement and hidden impact/finish
  ordering limit exact attribution. No quantitative fairness claim is made.
- Player-trust factors: the visible warning state distinguishes risky boost
  from free speed; class/route advice distinguishes a strategic choice from
  cosmetic vehicle selection. No monetisation/retention finding is inferred.
- Claim IDs: MS-002–MS-014; heuristics are Hypothesis, Limited, Medium and are
  rejected if controlled original-PS3 tests show contrary route/heat behavior.

## Replay and variation

- What changes between attempts: selected offered class/model, chosen rejoining
  line, boost/contact history and live rival interactions. Soft-ground history
  is scoped to the race, not assumed persistent across saves.
- Randomness or procedural generation: no track generation or specific seed
  model is established; live rival interaction is not proof of random route
  topology or a new unpreviewed-random-event gene.
- Multiple viable strategies: class-fit high/dry and lower/muddy paths;
  conservative cooling versus longer risky boost; optional nearby rider attack
  versus preserving line. Exact best strategy is not measured.
- Typical replay motive: improve classified result with another class/line
  while meeting the same medal terminal, not a mandatory collected vehicle set.
- Claim IDs: MS-001–MS-014; replay motives remain Hypothesis, Limited, Medium.

## Adjacent systems and history

- Direct predecessors: no predecessor-to-rule lineage is proved by this packet.
- Variants: Pacific Rift, Apocalypse, DLC Eliminator and Time Attack have
  separate boundaries and are not source substitutes for the first Festival.
- Similar games: corpus-selected comparisons appear below, not a narrative
  handpicked score list.
- Important differences: no stored nitro reserve, Takedown-fed boost extension,
  finite recovery unit, permanent elimination or player-directed flaming wreck
  is imported merely because another racing game has it.
- Claim IDs: MS-004–MS-005, MS-008–MS-010, MS-013–MS-014.

## Normalised genome

| Type | Active gene IDs | Parameters or exclusions |
|---|---|---|
| Action | ACT-290, ACT-293, ACT-308, ACT-350, ACT-379, ACT-609, ACT-610, ACT-694, ACT-695, ACT-696 | class/model, input, local target, thermal boost and view |
| System Behaviour | SYS-036, SYS-215, SYS-320, SYS-515, SYS-516, SYS-519, SYS-1421, SYS-1422, SYS-1423, SYS-1424 | contact, live field, heat, recovery, documentary ruts and settlement |
| Constraint | CON-437, CON-438, CON-784 | event eligibility, course/laps and initial boost warm-up |
| Information | INF-205, INF-206, INF-208, INF-491 | current race, ticket/result terms and thermal warnings |
| Objective | OBJ-150 | top-three classified medal/respect and returned menu |
| Time | TIM-003 | simultaneous running simulation with ordinary pause |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `506` (`GAME-0001`–`GAME-0506`).
- Exact genome matches: none.
- Tied near matches: `GAME-0217` — Need for Speed Underground (`11 / 32 = 0.343750`).
- Supported combination subsets: none.
- Scan date: 2026-10-06.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| GAME-0217, Need for Speed Underground | ACT-290, ACT-293; SYS-320, SYS-515, SYS-516, SYS-519; CON-438; INF-205, INF-206, INF-208; TIM-003 | Both retain live directly steered course racing, an autonomous field, current race/entry/result information and settled progression. Its Easy Olympic Square packet fixes a stock starter and two laps, admits automatic driving assistance and requires first place with Bank. MotorStorm includes seven offered classes, class-fitting rejoining terrain, documentary tyre-rut history, destructive thermal boost with initial warm-up, mounted contextual attacks and local recovery; top-three medal/respect return is accepted. No owned garage, finite nitro tank, guided wreck or first-place-only rule transfers. | Near 0.343750; sole positive non-exact maximum. Exact fraction belongs only to this Corpus comparison section. |

- New genes: nine evidenced boundaries, ACT-694–ACT-696, SYS-1421–SYS-1424,
  CON-784 and INF-491; no earlier definition or signature rewrite.
- Classification result: New gene.
- Evidence and reasoning: complete first-ticket packet separates thermal boost,
  initial readiness, local recovery and class-dependent surface history from
  existing reserve-boost and arena-demolition contracts.

### Preserved research notes

- New genes: nine evidenced boundaries, ACT-694–ACT-696, SYS-1421–SYS-1424,
  CON-784 and INF-491; no earlier definition or signature rewrite.
- Classification result: New gene.
- Evidence and reasoning: complete first-ticket packet separates thermal boost,
  initial readiness, local recovery and class-dependent surface history from
  existing reserve-boost and arena-demolition contracts.

## Taxonomy impact

- Registry changes: nine prospective additions; twenty unchanged transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_244](../../../research/taxonomy-changes/TAXONOMY_CHANGE_244.md),
  prospective operational boundaries and source limitations; full game-unit
  delivery still requires all acceptance gates.
- Candidate terms affected: no inherited candidate promotion or external
  novelty claim is justified by one racing packet.

## Negative results

- No separate negative-result record. Proposed fuel-reserve, whole-event
  elimination, arena spawn, DLC wreck steering, first-place-only objective,
  finite recovery lives, exact initial ten-second constant and universal
  offline dirt clearing are rejected before admission; limitations remain
  explicit rather than silently changing a prior gene.

## Delta summary

The following sections own this unit's compact canonical changes rather than
repeating the complete analysis. Ukrainian research views are generated from
the independently reviewed localisation layer.

## New facts

- [Observation | Corroborated | High] First Anything Grizzly event admits seven
  classes; R1's fifteen-participant field includes fourteen rivals, and its
  zero-based 0/2–2/2 display spans three physical circuits. MS-001, MS-009.
- [Observation | Direct | High] Held boost heats toward destruction; stationary
  protected replacement resumes the same race. MS-004–MS-005.
- [Observation | Corroborated | Medium] Soft-ground mutation retains the
  developer/publisher qualification rather than native coefficient proof.
  Requested recovery separately remains Limited/Medium. MS-007–MS-008.

## New genes

- [Observation | Corroborated | Medium] Nine proposed boundaries above; exact
  evidence grades remain independent per record. No external novelty claim.

## New combinations

- [Observation | Direct | High] No new combinations; all 274 verified
  combinations were tested as proper subsets and none applies. No recurring
  cross-family claim is inferred from one packet.

## Taxonomy changes

- [Observation | Corroborated | Medium] Prospective TAXONOMY_CHANGE_244;
  no earlier definition, signature, platform registry or public release rewrite.

## New questions

- Which original patch/region does R1 execute, and do warm-up, recovery and
  camera-dirt state differ across the original retail updates?
- What state does manual reset preserve for lap/time/heat and protection?
- What are original native heat, rut, attack and collision coefficients, and
  same-frame finish/explosion priority?
- Which offline view-dirt clearing claims can be reproduced without cheats?
- How do Silver/Bronze and repeat completion settle exact first-ticket points?

## Next recommended game

- [Hypothesis | Limited | Medium] Approved Windows full-release Ready or Not,
  GAME-0508, not Schedule I Early Access.
- Optimisation criterion: preserve the mixed-era/platform order and contrast
  racing pressure with tactical team, restraint and mission evaluation.
- Expected information gain: test sourced command and compliance boundaries;
  no signature is predicted or admitted before evidence review.
- Backlog impact: retain later MotorStorm modes and displaced Early Access
  subjects as separate unadmitted leads, not automatic next units.

## Why this game

- [Hypothesis | Limited | Medium] Class-fitting rejoining routes, destructive
  thermal boost and ongoing-race recovery may distinguish this packet from
  reserve-boost racing. Reject that expectation if full-corpus comparison and
  operational boundary review show no genuine distinction.
