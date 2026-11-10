---
game_id: GAME-0481
slug: out-run
game_title: Out Run
analysis_status: reviewed
reviewed: 2026-10-02
combination_ids: []
gene_ids:
  action:
    - ACT-290
  system:
    - SYS-045
    - SYS-320
    - SYS-1029
    - SYS-1204
    - SYS-1256
    - SYS-1257
    - SYS-1258
  constraint:
    - CON-745
  information:
    - INF-204
    - INF-456
  objective:
    - OBJ-002
    - OBJ-270
  time:
    - TIM-003
---

# Game: Out Run — original Sega arcade branching drive

Use the [canonical genome vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Course names, scenery, radio tracks, traffic density and time allowances are parameters, not separate genes.

## Analysis scope

- Version / ruleset: original 1986 Sega arcade *Out Run*, one ordinary standalone credit with the two-position manual gearbox and declared Normal time and enemy-density settings from the upright manual. World Revision B is the reconstruction's declared target, not a verified ROM identity. Exact original binary, regional course ordering, traffic random state and frame timings were not inspected. The original/unfixed countdown and off-road response are retained; Cannonball's optional fixes, automatic gears, turbo, time trial, continuous fifteen-stage mode and custom courses are excluded.
- Structured analysis target: `PLAT-ARCADE-CABINET`; see [platform coverage](../../platforms/games.json). The original upright operator manual establishes controls/settings; Sega's own retrospective establishes the branching original. The pinned modern rewrite is limited evidence for reconstructed transitions, not execution of Sega's binary.
- Primary decision loop: read the road, traffic, speed, gear and remaining time; steer, accelerate, brake or shift to preserve momentum; choose a branch by driving into it before commitment; reach a checkpoint to add time and repeat across five sections toward one selected goal while building speed, passing and finish-time score.
- Entry: one paid original-mode credit after the cosmetic music choice, at the first driving start, in the fixed red two-seat car. Normal time and Normal traffic settings are declared operator context, not asserted numeric defaults. No linked competitor, garage or selectable owned car is present in this packet.
- Exit: the selected fifth-section goal and its score/route result, original countdown underflow, or abandonment, before another credit or initials entry. Intermediate forks/checkpoints are not terminal races. Reaching a goal precedes its finish-bonus phase; other traffic is not a ranked opponent field.
- Included: continuous wheel/pedal/two-gear input, vehicle motion and road contact, collision/spin recovery with lost time, autonomous traffic, four live fork commitments, checkpoint time carry/addition, original zero-countdown interval, speed-on-road and completed-pass score, remaining-time finish bonus, current driving/HUD/route information and the finite route-completion and score objectives.
- Excluded: home ports, Japanese/prototype course parity, later franchise games, performance-unlocked sixth course, police, nitro, fuel or persistent health, damage upgrades, race-place competition, radio as a causal driving mechanic, operator maintenance as a player action, high-score initials, modern rewrite enhancements and exact unmeasured traffic, handling, timer or scoring constants. The gearbox technique is included because Sega explicitly documents its off-road consequence; its exact duration and execution window are not asserted.
- Reproducible parameterisation: legally pin the original World Revision B cabinet/ROM and operator settings, record steering/pedals/gears and a full credit, compare both choices at one fork, preserve time through a checkpoint, compare on-road/shoulder scoring and gear transitions, collide and recover, observe the displayed-zero interval, then complete one goal or expire. The documentary/source transitions below are conditional predictions, not fabricated original measurements.
- Direct-play status: no cabinet, ROM, emulator, original executable, input trace, gameplay video or audio was opened or played. The original manual's scanned controls, DIP table and input-test material were visually inspected; Sega's retrospective and pinned Cannonball source were read. Cannonball is a modern rewrite of disassembled original logic, not the original binary or an emulator. Source transfer is explicitly Medium confidence where no independent original rule text confirms it. Artwork is original interpretive art, not a capture.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `OR-001` | The original upright has steering, accelerator, brake and a two-position gear lever; time and enemy density each have separately declared Normal settings. | Confirmed | Direct | High | P1 printed pp. 5, 13, 18–19 |
| `OR-002` | Fifteen branching courses form sixteen paths to five goals; one credit traverses five sections with four branch choices. | Observation | Corroborated | High | P2; P3 `oinitengine.cpp`, `ostats.hpp` |
| `OR-003` | In the reconstruction's original-mode split, live lateral car position commits the next authored branch; the unselected road disappears after commitment. | Observation | Limited | Medium | P3 `init_split3`, `init_split_next_level` |
| `OR-004` | A reached eligible checkpoint adds route/setting-dependent time to the remainder, capped by the original-mode counter; no fixed universal seconds are claimed. | Observation | Limited | Medium | P3 `OStats::init_next_level`, `TIME` |
| `OR-005` | Sega documents repeated gear changes allowing shoulder travel without ordinary slowdown; the rewrite's gear-transition response explains that exception without making the car immune to collision. | Observation | Corroborated | Medium | P2; P3 `OFerrari::tick_gear_change`, `car_acc_brake` |
| `OR-006` | The rewrite's original/unfixed timer terminates on signed BCD underflow, not its first displayed zero; at zero acceleration input is suppressed while residual motion can continue. Its optional fixed timer instead ends at zero and is excluded. | Observation | Limited | Medium | P3 `Outrun::decrement_timers`, `OFerrari::move`, `outils::bcd_sub`, `ostats.hpp` |
| `OR-007` | Original-mode source credits speed while wheels are on-road and completed traffic passes; a goal converts remaining time into finish score. Exact coefficients, fractional timer behaviour and zero-time goal settlement need an original trace. | Observation | Limited | Medium | P3 `do_sound_score_slip`, `convert_speed_score`, `otraffic.cpp` overtake branch, `OBonus::init_bonus_text`, `decrement_bonus_secs` |
| `OR-008` | Traffic advances autonomously and contact affects motion/recovery. Time, score, stage, speed/gear/revs and route feedback support the live drive without revealing future traffic or a race rank. | Observation | Limited | Medium | P3 `otraffic.cpp`, `oferrari.cpp`, `ohud.cpp`, `ostats.cpp` |
| `OR-009` | Original control ends at goal/bonus result or deadline; crashes consume time rather than a claimed stock of lives, and no direct binary verification was performed. | Observation | Limited | Medium | P3 original game-state/bonus paths; documentary method |

## Basic data

- Release / origin: Sega's original arcade title, September 1986 according to Sega's history page. Later home ports and *OutRun 2* are different targets.
- Platform or physical form: standalone arcade driving cabinet; the inspected original upright documentation names a wheel, pedals and gear lever. Cabinet motion or force-feedback information is not inferred from a different cabinet model.
- Mechanical families: physics and object manipulation (`FAM-007`) for continuously steering a momentum-bearing vehicle and contact; real-time system pressure (`FAM-010`) for moving traffic and a replenishable deadline. Driving into a fork is not building a transport network.
- Sources accessed 2026-10-02:
  - **P1:** [Sega original upright owner's manual NV 420-5305-02](https://www.arcade-museum.com/manuals-videogames/O/outrun_manual.pdf), first printing 1986. Printed p. 5 controls, p. 13 DIP settings and input-test material pp. 18–19 establish hardware and declared settings. This service manual is not used as a full gameplay or physics description.
  - **P2:** [Sega original Out Run retrospective](https://www.sega.jp/history/arcade/product/9321/), publisher material establishing the date, fifteen courses, sixteen paths, five goals, red car/two occupants, two gears and the historical shoulder-driving gear technique. Radio is cosmetic context, not an admitted mechanic.
  - **P3:** [Chris White's Cannonball source at immutable commit `27493ebf62be3498dff93ed6a45e8e2db819bae1`](https://github.com/djyt/cannonball/tree/27493ebf62be3498dff93ed6a45e8e2db819bae1). Read original-mode branches in `src/main/engine/{oinitengine,ostats,oferrari,otraffic,outrun,obonus,ohud,outils}.cpp` and `ostats.hpp`; the [creator's manual](https://github.com/djyt/cannonball/wiki/Cannonball-Manual) identifies it as a rewrite requiring original graphics/data ROMs. No ROM was obtained or executed. Optional fixes and modern modes are not transferred; documented reconstruction is not an original-binary measurement.
- Claim IDs: `OR-001`–`OR-009`. Evidence confidence remains bounded per claim rather than inheriting publisher authority for unrelated source-only details.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-290`: directly steer the assigned car, modulate accelerator/brake and select low/high gear. There is no embodied seat-entry action, purchased car choice or nitro input (`OR-001`).

### System Behaviour Genes

- Reuse `SYS-045`: traffic cars advance continuously under autonomous movement/collision rules; they are obstacles, not scored race-position rivals. `SYS-365`'s civilian reactions and `SYS-515`'s competitive racing field are not imported (`OR-008`).
- Reuse `SYS-320`: integrate the occupied car's motion, traction, off-road deceleration and collision/recovery. As already admitted for Trackmania, damage/fuel parameters can be absent; Out Run does not acquire a persistent health bar or fuel reserve (`OR-005`, `OR-008`).
- Reuse `SYS-1029`: a positive remaining clock at a reached goal contributes finish score. Zero-time and fractional settlement remain unmeasured, not presumed to follow a different carrier's exact formula (`OR-007`).
- Reuse `SYS-1204`: eligible checkpoint credit adds to the remaining deadline instead of replacing it with a full clock; original-mode route and setting values remain parameters (`OR-004`).
- New `SYS-1256`: commit the next authored section from car position in a live fork, update route history and remove the rejected continuation after commitment. This is not a paused dialogue choice or a performance-awarded bonus race (`OR-002`, `OR-003`).
- New `SYS-1257`: a gear-transition response temporarily suppresses ordinary off-road speed loss, enabling the documented repeated-shift shoulder technique. Collision still applies and off-road speed score is not granted merely because speed is preserved (`OR-005`, `OR-007`).
- New `SYS-1258`: accumulate speed-dependent score while on-road and credit completed traffic passes. These are declared driving-score predicates, not collectible contact, damage or drift-chain rewards (`OR-007`).

### Constraint Genes

- New `CON-745`: the original reconstructed countdown ends the drive on signed underflow; its displayed-zero interval already suppresses acceleration but does not itself terminate residual motion. Goal/completion ordering and checkpoint credit remain explicit dependencies. Reject `CON-068` because its authoritative-zero terminal does not fit this admitted branch (`OR-006`).

### Information Genes

- Reuse `INF-204`: live speed, gear/revs and visible road/route cues inform braking and steering. The minimap exposes the current route, not future traffic or every handling variable (`OR-008`).
- New `INF-456`: show remaining deadline, score, stage and route-progress/result feedback without implying rival race position, lives or complete hidden state. Current information and final route result belong to the same bounded credit (`OR-008`, `OR-009`).

### Objective Genes

- Reuse `OBJ-002`: increase the credit's speed/pass/finish score; this can vary among completed drives (`OR-007`).
- New `OBJ-270`: reach one authored terminal of a checkpoint-timed branching driving route before original deadline failure. Four fork choices select one of five goals; no competitive place or performance-unlocked extra course is required. `OBJ-260`'s classified ordinary/awarded-bonus racing chain does not transfer unchanged (`OR-002`, `OR-009`).

### Time Genes

- Reuse `TIM-003`: traffic, vehicle and deadline advance during deliberation and crash recovery. A service/test interruption is not a player pause mechanic; the original clock's exact wall-time rate is unmeasured (`OR-006`, `OR-008`).

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First driving start, fixed car, low gear | Accelerate and steer | Car moves continuously; brake and shift change motion | Dedicated driving input, not vehicle acquisition | `OR-001`, `OR-008` |
| Road begins splitting, commitment not yet reached | Position car into either branch | Original-mode source commits one successor and later removes the other road | Live spatial branch commitment | `OR-003` |
| Time remains, next eligible checkpoint | Cross it | Add the next route/settings allowance to the remainder with its cap | Time credit is not full reset | `OR-004` |
| Car leaves normal road contact without a gear transition | Keep accelerating | Ordinary off-road response reduces usable speed | Contact-dependent motion | `OR-005` |
| Car on shoulder, applicable shift transition | Shift repeatedly | Documented technique avoids ordinary slowdown; neither collision immunity nor off-road score follows | Exception with independent scoring predicate | `OR-005`, `OR-007` |
| Clock reaches first displayed zero | Keep accelerator pressed | Reconstructed original branch suppresses acceleration but retains residual movement until terminal underflow | Zero display differs from terminal condition | `OR-006` |
| Deadline counter reaches underflow before goal | Timer event | Original-mode game state exits controlled driving | Finite-credit failure boundary | `OR-006`, `OR-009` |
| Player moves fast on road then on shoulder | Compare score response | Source's continuous speed credit requires on-road wheel state | Preserving speed does not preserve every reward | `OR-007` |
| Traffic car ahead | Pass its rear threshold without contact | Completed-pass event adds score; mere approach is insufficient | Event credit separate from continuous speed credit | `OR-007` |
| Car meets traffic or roadside obstacle | Contact and recovery | Motion/control interruption loses live time, without an asserted life stock | Collision penalty is not terminal by itself | `OR-008`, `OR-009` |
| Fifth section completed with positive time | Reach selected goal | Goal starts remaining-time score conversion and selected-route result | Completion plus secondary performance | `OR-002`, `OR-007`, `OR-009` |

These are source-based conditionals. No original input recording, measured collision box, precise seconds or numerical score experiment is fabricated.

## Strategic and experiential structure

Fast road travel preserves deadline and gains speed score, but traffic/contact can waste the same time needed for the next checkpoint. Each fork selects a later road while driving continues. Checkpoints preserve unspent allowance, so earlier efficiency matters later. The gear technique changes shoulder slowdown without automatically changing the on-road score predicate; avoiding traffic on the shoulder can trade scoring for continued speed. Completion and score are different outcomes: one selected goal can be reached with different remaining time and pass scores. No place leaderboard among traffic cars substitutes for those decisions.

## Replay and variation

Four binary fork commitments produce sixteen paths through a fifteen-section course tree and five endings, as Sega documents. A new credit can change route and traffic outcomes. Exact World/Japanese ordering, random seed, Normal allowance values and shift windows require a pinned original trace. Their uncertainty does not authorise importing Cannonball's corrected clock or continuous fifteen-stage mode.

## Adjacent systems and history

Sega's retrospective explicitly recognises the gear technique; it is not a modern nitro item. The service booklet and open rewrite serve different evidential roles. The latter's original-mode source is reproducible to inspect, but translated logic, bug toggles and modified display paths prevent declaring all of it original binary truth. The scope therefore retains those source-only claims as Limited/Medium and isolates the modern fixed countdown from this original reconstruction.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
|---|---|---|
| Action | `ACT-290` | wheel, pedals and low/high gearbox |
| System Behaviour | `SYS-045`, `SYS-320`, `SYS-1029`, `SYS-1204`, `SYS-1256`–`SYS-1258` | traffic, vehicle contact, time score/credit, live forks, shifting and driving score |
| Constraint | `CON-745` | original underflow terminal and zero acceleration suppression |
| Information | `INF-204`, `INF-456` | driving readouts, clock/score/stage and route feedback |
| Objective | `OBJ-002`, `OBJ-270` | score and one finite branching goal |
| Time | `TIM-003` | live driving, traffic and recovery |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `480` (`GAME-0001`–`GAME-0480`).
- Exact genome matches: none.
- Tied near matches: `GAME-0316` — Gran Turismo (`4 / 19 = 0.210526`).
- Supported combination subsets: none.
- Scan date: 2026-10-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0316` *Gran Turismo* | `ACT-290`, `SYS-320`, `INF-204`, `TIM-003`: dedicated driving input, vehicle motion/contact, driving readouts and live time. | Gran Turismo's reviewed B-1 licence packet requires the complete car stationary in a fixed stopping zone within its elapsed limit. Out Run instead carries and adds checkpoint time, selects live road branches, resolves autonomous traffic and score, and reaches one fifth-section goal under the original reconstructed underflow policy; no licence, parked target or ranked race transfers. | `4 / 19 = 0.210526`; nearest non-exact prior signature, not identical driving objectives. |

## Taxonomy impact

`TAXONOMY_CHANGE_218` admits six bounded genes and reuses eight unchanged boundaries. No earlier genome, definition or verified combination changes. The named salience review partitions fourteen uses after reading the complete scoped credit; rarity does not assign weights.

## Negative results

- Reject `SYS-365` civilian fear/reporting and `SYS-515` ranked rivals: use `SYS-045` for autonomous traffic and existing vehicle contact for collision.
- Reject `CON-068` for the original/unfixed source branch: displayed zero and signed underflow differ. Do not import the rewrite's fixed timer or precise original wall-time claim.
- Reject `OBJ-260`: no performance-awarded extra race/classified rival result is established here. Use the bounded branching-route objective instead of silently generalising an earlier definition.
- Reject `ACT-608`, `ACT-609`, `INF-205`, `INF-439`, garage, race-place and assumed force-feedback mechanisms. Fixed car, original upright controls and this HUD do not prove them.
- Reject one gene per fork, road theme or radio track, and shoulder speed preservation as collision immunity or off-road speed-score entitlement.

## Delta summary

## New facts

- [Confirmed | Direct | High] Sega documents the two-gear controls, branching course structure and historical shoulder technique (`OR-001`, `OR-002`, `OR-005`).
- [Observation | Limited | Medium] The pinned rewrite separates live fork commitment, checkpoint credit, on-road/pass score and the original zero/underflow policy; original execution remains unverified.

## New genes

- [Observation | Corroborated | Medium] Six boundaries cover fork commitment, shift-mediated shoulder response, driving score, original deadline policy, credit information and finite branching-goal completion.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed; proper subsets are recomputed against the complete signature.

## Taxonomy changes

- [Observation | Limited | Medium] `TAXONOMY_CHANGE_218`; earlier signatures and definitions remain unchanged.

## New questions

- Pin and trace the original World Revision B binary to test traffic, checkpoint/goal ordering at displayed zero, gear-transition windows, numeric score and timer-rate details. No optional rewrite fix supplies that missing evidence.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0482` *LocoRoco*, original PSP, follows full acceptance and the Goal stop window.
- Optimisation criterion: move from continuous car steering and fork commitments to terrain tilt, jumping and controlled body splitting on another platform.
