---
game_id: GAME-0457
slug: sega-rally-championship
game_title: Sega Rally Championship
analysis_status: reviewed
reviewed: 2026-09-30
combination_ids: []
gene_ids:
  action:
    - ACT-290
    - ACT-608
    - ACT-609
  system:
    - SYS-320
    - SYS-515
    - SYS-516
    - SYS-1204
    - SYS-1205
  constraint:
    - CON-068
    - CON-438
    - CON-736
  information:
    - INF-204
    - INF-205
    - INF-439
  objective:
    - OBJ-260
  time:
    - TIM-003
---

# Game: Sega Rally Championship

Use the canonical [vocabulary and signature](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Car, gearbox, road material, lap count and allowance seconds are parameters, not rally-theme genes.

## Analysis scope

- Version / ruleset: Original 1995 Sega Rally Championship, English export twin-cabinet documentary rules, NOT LINK, Normal difficulty and Normal lap setting; one solo Championship credit. Select Celica Manual, then drive the authored Desert, Forest and Mountain chain, one lap each under the selected twin manual, followed by the hyper course only when its superior-result gate actually awards it. Include steering, throttle, brake, four-position manual shifter, optional cockpit/chase view, vehicle motion and road contact, autonomous rivals, ordered checkpoints and course finish, remaining-time credit, terminal clock expiry, live speed/gear/revs/navigation/position/progress/mirror information and wheel feedback. The exact bonus criterion and tie handling are not independently measured; the museum account calls the branch first-place Lakeside, whereas the primary manual says superior result. Stop at the complete ordinary or awarded-bonus result, timeout or deliberate abandonment, before another credit. Exclude Practice, linked VS, operator maintenance as player action, secret selection codes, home ports, Rally 2, career, garage, buying/tuning, nitro, persistent damage, and exact traction/bonus-time coefficients. The July 1995 upright manual reports two Desert Championship laps rather than the twin manual’s one; no blanket cabinet parity is asserted.
- Structured analysis target: PLAT-ARCADE-CABINET, exact standalone twin target in [platform coverage](../../platforms/games.json).
- Primary decision loop: read the road, navigation icon, revs, gear, time and place; steer, accelerate, brake or shift to preserve a useful racing line; timely checkpoints replenish remaining time; a course finish advances the authored chain; ordinary-chain performance decides bonus access before final settlement.
- Entry and exit: enter with one credit, no linked competitor, Normal settings, Championship and Celica Manual. Begin at car-choice commitment; exit at time expiry, abandonment, or the final classified ordinary/awarded-bonus result before the next credit. Intermediate Desert or Forest completion is not a terminal. A lower classified result can finish the ordinary chain without gaining the bonus.
- Included: all causally necessary car-choice, driving, checkpoint, ordered-course, bonus-gate, information and deadline rules of this credit.
- Excluded: Practice, linked VS ballot, ports, operator maintenance decisions, exact unmeasured coefficients and persistent career rewards.
- Potential scoped modules: Practice, one evidenced linked race, explicit firmware comparison, bonus eligibility and tie experiment, or licensed Saturn/PC rules separately.
- Direct-play status: Not conducted. No cabinet, ROM, executable, input trace, gameplay video or audio was opened or played. Original Sega twin manual printed pp. 14–16 and 28 and upright pp. 12–15 were visually inspected. The upright/twin lap discrepancy is retained rather than silently reconciled. Museum gameplay details are secondary corroboration, not direct execution. Exact bonus qualification, opponent pace, handling coefficients and firmware are unmeasured. The artwork is a new illustration, not a game capture.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| SR-001 | One solo credit selects Championship or Practice, then a supplied Celica/Delta manual/automatic option by wheel and accelerator. | Observation | Direct | High | P1, P2 |
| SR-002 | Twin Championship proceeds through one Desert, Forest and Mountain lap; upright instead reports two Desert laps. No universal cabinet parity follows. | Observation | Direct | High | P1 p. 15, P2 p. 13 |
| SR-003 | A timely checkpoint preserves remaining time and adds the next allowance; failure to reach it before expiry ends the attempt. | Observation | Direct | High | P1 p. 15, P2 p. 13 |
| SR-004 | Superior ordinary-chain results grant a hyper-course branch. Museum documentation calls it first-place Lakeside; exact firmware predicate, ties and branch clock allocation remain unmeasured. | Observation | Corroborated | Medium | P1, P2, S1 |
| SR-005 | Wheel, pedals, four-position shifts, fixed viewpoints, tachometer, gear, speed, navigation, mirror, place and progress support real-time driving; wheel feedback responds to road and motion. | Observation | Direct | High | P1 pp. 15–16, P2 pp. 14–15 |
| SR-006 | Normal difficulty/lap settings and NOT LINK are operator-fixed context, not player actions; the solo account has fourteen rivals but their pace scaling is unmeasured. | Observation | Corroborated | Medium | P1 p. 28, S1 |
| SR-007 | No original cabinet, ROM, firmware, handling curve, bonus threshold or player input trace was inspected. | Observation | Limited | High | Documentary method |

## Basic data

- Release / origin: Sega's original 1995 arcade title, not Sega Rally 2 or a home-port arcade-labelled mode.
- Platform or physical form: original arcade twin driving cabinet in NOT LINK; exact firmware and region beyond English export documentation uninspected.
- Mechanical families: FAM-007 physics/object manipulation for steering a momentum-bearing vehicle through contact; FAM-010 real-time pressure for rivals and replenishable deadline. Route construction, evidence deduction and points-cup membership are not inferred from road scenery.
- Sources accessed 2026-09-30:
  - P1: [Sega original twin operator manual](https://www.arcade-museum.com/manuals-videogames/S/Sega-Rally-Championship.pdf), printed pp. 14–16 and 28, visually inspected: modes, car/shift, checkpoint clock, chain/hyper branch, controls/HUD/force feedback, Normal and NOT LINK. The scan's right margin is clipped; complete upright wording independently corroborates the shared claims without overriding its lap difference.
  - P2: [Sega July 1995 preliminary upright manual](https://www.arcade-museum.com/manuals-videogames/S/SEGA.pdf), visually inspected printed pp. 12–15: standalone modes, car choice, timer, stated two/one/one Championship laps, superior-result hyper course, view switch, wheel reaction and shifting guidance.
  - S1: [Museum of the Game original arcade record](https://www.arcade-museum.com/Videogame/sega-rally-championship), bounded secondary corroboration for fourteen rivals and first-place Lakeside. It is not used to replace operator-manual lap evidence, admit cheats or assert measured firmware.
- Claim IDs: SR-001–SR-007.

## Mechanical decomposition

### Action Genes

`ACT-290` — Direct wheel, throttle, brake and manual shifts control one assigned car. Brake before the bend rather than inventing a nitro input.

`ACT-608` — A supplied car and manual or automatic transmission are committed before the run. Choose Celica Manual without buying it or unlocking a garage.

`ACT-609` — The view button alternates cockpit and chase views without replacing the car. Use the exterior view to judge the car’s angle at a bend.

- Parameters and claim IDs: SR-001–SR-007; car, settings, course and force calibration do not create additional genes.

### System Genes

`SYS-320` — The same vehicle model resolves acceleration, steering and surface contact; exact traction coefficients are unmeasured. Changing the steering input changes the line, not the road geometry.

`SYS-515` — The solo attempt has an autonomous rival field; Normal is fixed cabinet context. A rival can stay ahead while you lose time at a bend.

`SYS-516` — Required checkpoints and laps are validated before a course finish counts. The selected twin documentation uses one lap per ordinary Championship course.

`SYS-1204` — A timely checkpoint adds the next allowance to the time still available. A faster approach preserves more of the previous allowance.

`SYS-1205` — An intermediate finish continues the same attempt, with a performance-gated bonus at its end. Desert is followed by Forest, then Mountain, not freely chosen practice races.

- Parameters and claim IDs: SR-001–SR-007; car, settings, course and force calibration do not create additional genes.

### Constraint Genes

`CON-068` — The authoritative remaining clock can end the run before its route is completed. Do not treat the countdown as a harmless elapsed-time score.

`CON-438` — Only the declared checkpoint sequence and required laps qualify the finish. Reaching a visible finish is insufficient if required progress is missing.

`CON-736` — The manual reserves the hyper course for superior results; exact ties remain unmeasured. Do not promise Lakeside to every Mountain finisher.

- Parameters and claim IDs: SR-001–SR-007; car, settings, course and force calibration do not create additional genes.

### Information Genes

`INF-204` — Speed, gear, engine revs and navigation icons help choose braking and shifts. The manual recommends an upshift before the red rev zone.

`INF-205` — Live place, achievement meter, rear mirror and time distinguish passing from merely surviving. A good place cannot replace a timely checkpoint crossing.

`INF-439` — Documented physical wheel reactions supplement the visible road; calibration is not measured here. Changing surface can change wheel feel without displaying the entire future route.

- Parameters and claim IDs: SR-001–SR-007; car, settings, course and force calibration do not create additional genes.

### Objective Genes

`OBJ-260` — Complete the ordinary chain and any awarded bonus before expiry, then reach the final result. The first course finish is not the end of the whole credit.

- Parameters and claim IDs: SR-001–SR-007; car, settings, course and force calibration do not create additional genes.

### Time Genes

`TIM-003` — Vehicle input, competing cars and the remaining clock run together in real time. Waiting at a bend still spends the attempt’s time.

- Parameters and claim IDs: SR-001–SR-007; car, settings, course and force calibration do not create additional genes.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| One standalone credit, no waiting linked entrant | Choose Championship and Celica Manual | A supplied car/profile starts the authored chain | Not an owned-garage selection | SR-001 |
| Car approaches a bend at a chosen speed and gear | Brake, steer or shift | Vehicle motion and current contact resolve the line | No nitro, weapon or measured traction constant | SR-005 |
| Current tachometer near red zone | Shift upward before it | Manual recommends efficient acceleration | Gear number is a parameter; no invented clutch | SR-005 |
| Positive remaining time before next required point | Cross point in time | Retain remainder and add next allowance | Credit is not fixed full-clock reset | SR-003 |
| No valid checkpoint before clock reaches zero | Continue driving | Attempt ends unsuccessfully | Place alone cannot save expiry | SR-003 |
| Ordinary twin Desert lap validated | Cross its finish | Continue to Forest, then Mountain after its own lap | Intermediate finish is not whole-credit completion | SR-002 |
| Ordinary chain completed with qualifying result | Accept automatic awarded extension | Hyper-course branch continues this credit | Bonus criterion is bounded, ties unmeasured | SR-004 |
| Ordinary chain completed without qualification | Reach final ordinary classification | No promised bonus | A completion need not win every place test | SR-004 |
| Already awarded bonus | Complete it before expiry | Final attempt result, not another practice selection | Include awarded extension before stopping | SR-004 |
| Cockpit view selected | Press View Change | Chase view with same car state | Visibility, not topology editing | SR-005 |
| Road/contact state changes | Feel current wheel reaction | Tactile feedback complements visible state | No future omniscient prediction | SR-005 |
| Upright document instead of selected twin | Read its Desert lap statement | Reports two rather than one | Edition evidence cannot silently migrate | SR-002 |

## Strategic and experiential structure

Line and shift decisions trade passage speed against contact and overtaking. Every delay consumes a deadline, but reaching a checkpoint preserves unused time, coupling early efficiency to later room for error. Course clearance and performance qualification are different boundaries. The final optional course is not assumed for every result. The observed interfaces support decisions without promising an exact force model, known future opponent trajectory or measured optimal racing line. Claim IDs SR-003–SR-007.

## Replay and variation

Keep twin export documentary rules, Normal and NOT LINK fixed; car/profile choice, live line, gears, braking, place and resulting bonus branch can vary between credits. No random-generator or rubber-banding implementation is inferred. This packet includes its first chosen attempt rather than a persistent tuning economy.

## Adjacent systems and history

Practice course choice and lap counts are a separate loop. Linked VS course voting, alternative code-selected handling, optional record initials, cabinet bookkeeping and home-port Time Attack or garage settings are outside the primary driving decision loop. The preserved upright discrepancy warrants future firmware/cabinet study rather than a global historical-equivalence claim.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| action | `ACT-290`, `ACT-608`, `ACT-609` | scoped documentary action rules |
| system | `SYS-320`, `SYS-515`, `SYS-516`, `SYS-1204`, `SYS-1205` | scoped documentary system rules |
| constraint | `CON-068`, `CON-438`, `CON-736` | scoped documentary constraint rules |
| information | `INF-204`, `INF-205`, `INF-439` | scoped documentary information rules |
| objective | `OBJ-260` | scoped documentary objective rules |
| time | `TIM-003` | scoped documentary time rules |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `456` (`GAME-0001`–`GAME-0456`).
- Exact genome matches: none.
- Tied near matches: `GAME-0276` — Forza Horizon 5 (`8 / 20 = 0.400000`).
- Supported combination subsets: none.
- Scan date: 2026-09-30.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0276` — Forza Horizon 5 | Dedicated car control, vehicle motion, autonomous rivals, ordered progress, racing HUD and live time | This arcade credit replenishes a terminal deadline at checkpoints, chains courses and gates a bonus; Horizon Mexico is one first-place race with a retained reward and no replenishable attempt clock | Near match: `8 / 20 = 0.400000`; same driving core, different completion authority and progression |

## Taxonomy impact

Seven new boundaries in [TAXONOMY_CHANGE_194](../../../research/taxonomy-changes/TAXONOMY_CHANGE_194.md), nine unchanged reuses. Named GAME-0457 salience review partitions all sixteen uses and provides every bilingual plain-language card. No new combination is inferred merely from another vehicle theme.

## Negative results

- No ACT-291: supplied options are not an owned collection. No player ACT-292 difficulty configuration: operator settings are entry context.
- No SYS-519 or OBJ-134: this is neither retained campaign reward nor one isolated first-place race. No OBJ-180/SYS-895: no points-based Cup trophy.
- No SYS-1161: time comes from a route checkpoint, not a designated gunfight target. No new gear/surface gene duplicating ACT-290 or SYS-320.
- No ACT-095 rule-bearing orbit or topology family for ordinary view switching. No full-information INF-001, declared damage/fuel meter, nitro, automatic pause, exact future path or full-product/port genome.
- Exact first-place bonus ties, clock equality, opponent count by firmware and force curves remain unmeasured; documentary qualification is not represented as an independently played experiment.

## Delta summary

## New facts

- [Observation | Direct | High] Twin and upright original manuals disagree on Championship Desert lap count; the selected twin packet retains its own target.

## New genes

- [Observation | Direct | Medium] Seven bounded supply/view/credit/chain/bonus/haptic/terminal definitions; no external novelty claim.

## New combinations

- [Observation | Direct | High] Complete scan finds no verified proper-subset combination; no earlier combination edited.

## Taxonomy changes

- [Observation | Direct | High] TAXONOMY_CHANGE_194; earlier boundaries and signatures unchanged.

## New questions

- What lawful exact original cabinet/firmware observation resolves bonus qualification, tie handling and the documented lap discrepancy?

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0458 The Legend of Zelda: Link's Awakening, original Game Boy, only after complete acceptance and the stop window.
- Optimisation criterion: approved platform order, one complete unit/one local commit; no push or public release.

## Why this game

- [Hypothesis | Limited | Medium] Original arcade checkpoint replenishment and conditional chain closure test decision boundaries that a modern retained-reward race does not cover.
