---
game_id: GAME-0443
slug: time-crisis
game_title: Time Crisis
analysis_status: reviewed
reviewed: 2026-09-28
combination_ids: []
gene_ids:
  action:
    - ACT-202
    - ACT-490
  system:
    - SYS-215
    - SYS-915
    - SYS-1160
    - SYS-1161
  constraint:
    - CON-068
    - CON-183
    - CON-717
  information:
    - INF-179
    - INF-428
  objective:
    - OBJ-029
  time:
    - TIM-003
---

# Game: Time Crisis — first arcade Story Game combat view

Use the [canonical vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Castle dressing, gun recoil and exact operator-selected clock settings are parameters or presentation, not separate active genes.

## Analysis scope

- Version / ruleset: original one-player Namco *Time Crisis* arcade cabinet, Story Game, with its physical Action Pedal and calibrated gun. The North American 50-inch operator manual establishes this hardware and mode; no cabinet ROM revision or particular operator time-limit setting was inspected. The 1997 PlayStation port, its Hotel mission and later series entries are excluded.
- Primary decision loop: keep the pedal released to duck behind authored cover and refill a six-shot magazine, press it to rise, aim the physical gun and spend shots on visible enemies, then duck again before incoming fire or an empty magazine leaves the exposed actor vulnerable. The stage countdown continues through both stances.
- Entry: after starting Story Game at Stage 1, begin at the first combat view in Area 1 as the initial three enemies become shootable. This is the castle's receiving-basement opening described by a contemporary arcade walkthrough, not a claim that the entire Area 1 or campaign is modelled.
- Positive local exit: defeat the three required opening enemies and observe the authored camera/viewpoint advance to the next part of Area 1. Stop before choosing shots in that successor view. A time bonus is possible for prioritising the designated right-side enemy; it is not required for clearance.
- Negative run exit: the authoritative countdown reaches zero, or the finite Story Game lives are exhausted before local clearance. A paid continue, if offered, is outside this packet.
- Included: the pedal's cover/exposure choice; protective ducking that disables fire; automatic six-round refill on ducking; physically aimed gunfire and spatial hit/miss; hostile return fire while exposed; visible local enemy and cover state; countdown, magazine and lives; one designated enemy's time bonus; mandatory first-group clearance and authored forward view; real-time clock and encounter advancement.
- Excluded: later parts of Area 1, stages 2–3, bosses, shields, grenades, exploding targets, optional score optimisation, entire rescue ending, arcade Timed Game with unlimited lives, PlayStation-only modes, exact hitboxes, enemy accuracy, score formula, initial clock seconds, target-light sampling algorithm and any claimed direct observation of a cabinet.
- Reproducible parameterisation: on an original working cabinet calibrated according to the operator manual, start Story Game; at the first Area 1 encounter, release the pedal to cover/reload, press it to expose, fire at the right soldier and the other two visible soldiers, and release again for refill or protection as needed. Record the clock before and after the eligible target, then clear the required three and stop at the next authored camera view. The written sources reconstruct this procedure; it was not executed here.
- Potential scoped modules: later Area 1 enemy types and hazards, the whole three-area rescue route, operator timing variants, Timed Game and PlayStation Special Mission.
- Direct-play status: no cabinet, arcade PCB, original monitor/gun, ROM, video, audio or gameplay capture was inspected or run. The illustration is original interpretive art and not a screenshot. Hardware sampling details and exact operator settings remain unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TC-001` | The original one-player arcade cabinet uses a physical gun and dual-purpose Action Pedal; Story Game has limited time and lives, unlike Timed Game. | Confirmed | Direct | High | P1 |
| `TC-002` | Releasing the pedal ducks into protection, disables firing and automatically refills six bullets; pressing permits exposed shooting. | Observation | Corroborated | High | P1, P2, P3 |
| `TC-003` | Time continues while the player hides; expiry ends the attempt even if lives remain, while enemy shots can cost lives during exposure. | Observation | Corroborated | High | P1, P2, P3 |
| `TC-004` | The first Stage 1 Area 1 combat part presents three soldiers; the right-side soldier can yield a two-second bonus if shot first. | Observation | Limited | Medium | P3 |
| `TC-005` | Required enemy clearance advances to the next authored view, rather than granting free walking control. | Observation | Corroborated | High | P2, P3 |
| `TC-006` | Arcade life and time settings are operator-configurable; the selected unit asserts no fixed initial clock or ROM revision. | Confirmed | Direct | High | P1 |

## Basic data

- Release / origin: original Namco arcade *Time Crisis*; the cited North American cabinet manual identifies a 50-inch single-player installation. A particular ROM revision was not tested; the manual's displayed service example is not substituted for an inspected board.
- Platform or physical form: arcade cabinet with 50-inch display, calibrated solenoid gun and foot-operated Action Pedal.
- Mechanical families: tactical forecast and counterplay (`FAM-009`) for exposing the player only when a shot is worth the risk; real-time system pressure (`FAM-010`) for the continuing deadline and hostile fire.
- **P1:** [Namco America original *Time Crisis* operator manual](https://manualzz.com/doc/994451/namco-time-crisis-arcade-game-operator%E2%80%99s-manual), pp. 2–3 and game-options screen, accessed 2026-09-28. Primary hardware, pedal, six-shot refill, Story/Timed distinction and configurable life/time evidence. The manual describes special-enemy time rewards but not the exact first-area target.
- **P2:** [Donny Chan, first-hand arcade observations](https://gamefaqs.gamespot.com/arcade/583641-time-crisis/faqs/1081), dated 20 April 1996, accessed 2026-09-28. Contemporary confirmation of pedal release/press, six-shot counting, enemy pressure and target-based time extensions; one player's observations are not a software specification.
- **P3:** [Mark Kim, first-hand arcade FAQ and route](https://gamefaqs.gamespot.com/arcade/583641-time-crisis/faqs/1079), updated 2000, accessed 2026-09-28. Distinguishes arcade Story Game from PlayStation additions and describes the first Stage 1 Area 1 three-soldier view, bonus ordering and onward view. Exact bonus is a single-source route observation.
- Claim IDs: `TC-001`–`TC-006`.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-202` for the pedal's decision-relevant duck/stand posture, although the actor cannot relocate freely along cover. Reuse `ACT-490` for physically pointing the calibrated display-sensing arcade gun and requesting a shot. Do not replace either with a mouse-cursor action or the contextual mobile-cover action `ACT-226`.

### System Behaviour Genes

- Reuse `SYS-215` for real-time exchange of player and hostile shots. Reuse `SYS-915` for holding the forward camera until the finite local group is defeated, then releasing the next authored combat slice.
- Add `SYS-1160` for the coupled cover transition and automatic six-round refill. Add `SYS-1161` for a designated hostile hit increasing the running countdown. These are separate from the physical pedal/gun inputs and from the deadline itself.
- Order: expose → eligible gunshot and possible hostile reply → target defeat or player life loss → duck and refill → re-expose; defeating the required local group releases the next view. Clock expiry can terminate the attempt at any point.

### Constraint Genes

- Reuse `CON-068` for the live terminal countdown and `CON-183` for finite Story Game lives. Add `CON-717` for fire being legal only while exposed with at least one of six rounds left. A protected state prevents enemy-shot harm and player gunfire but does not freeze `CON-068`.

### Information Genes

- Reuse `INF-179` for the current view's enemies, cover and immediate threat cues, without claiming future views are visible. Add `INF-428` for the live clock, loaded rounds and remaining life stock needed for the cover-versus-exposure decision.

### Objective Genes

- Reuse `OBJ-029` for incapacitating all three required local enemies before run failure. The packet stops at the next view, so it does not claim the full three-area rescue objective or final score optimisation.

### Time Genes

- Reuse `TIM-003`: countdown and hostile attacks advance while the player can act. Hiding changes exposure, not the clock's authority.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Player exposed with rounds remaining | Release the pedal | Player ducks, gunfire becomes illegal, magazine refills to six | cover and reload are linked | `TC-002` |
| Player hidden with full magazine | Keep hiding | Hostile shots cannot hit the protected actor, but countdown continues | protection does not stop the deadline | `TC-002`, `TC-003` |
| Player hidden with a visible enemy | Press pedal, aim and fire | Player rises, spends one round and receives hit/miss and possible hostile reply | physically aimed offensive window | `TC-002`, `TC-003` |
| First view, designated right soldier present | Defeat him before other two | First-hand route reports two extra clock seconds | target-specific time budget, not universal reward | `TC-004` |
| Three required enemies defeated before expiry | Wait for authored transition | Camera advances to the next Area 1 view; analysis stops | finite encounter exit | `TC-005` |
| Countdown reaches zero while behind cover | No offensive action | Story Game ends regardless of unspent lives | terminal timer | `TC-003` |

## Strategic and experiential structure

- Local: the player trades safe observation and six fresh rounds against exposure to return fire; shooting from cover is impossible. The right soldier offers an optional time-saving priority, but attacking him too late may lose the bonus.
- Medium term: the finite magazine encourages short exposed volleys followed by a duck/refill cycle. A player cannot wait indefinitely in safety because the clock runs through cover.
- Failure attribution: an empty magazine means the player missed a duck/refill opportunity; a lost life reflects exposure to hostile fire; time expiry can occur even with lives intact. No exact enemy accuracy or timing window is inferred.

## Replay and variation

Shot accuracy, cover timing, enemy attack timing and the operator-configured starting clock/lives can vary this encounter. The guide's right-target bonus is a route observation, not proof of one universal timing constant across every board revision.

## Adjacent systems and history

*Duck Hunt* (`GAME-0345`) also uses a physically aimed display gun, but its NES Game A round gives each flying duck a three-shot/time opportunity and evaluates a ten-target pass line. It has no pedal-gated cover or automatic cover refill. The NES-specific darkness/target-light adjudication `SYS-967` is not imported into this Namco cabinet without evidence of identical sampling.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-202`, `ACT-490` | pedal posture and calibrated physical gun |
| System Behaviour | `SYS-215`, `SYS-915`, `SYS-1160`, `SYS-1161` | real-time shots, authored view release, cover refill, target time bonus |
| Constraint | `CON-068`, `CON-183`, `CON-717` | countdown, lives and exposed six-shot window |
| Information | `INF-179`, `INF-428` | current targets/cover and resource display |
| Objective | `OBJ-029` | clear the three-enemy local set |
| Time | `TIM-003` | live countdown and return fire |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `442` (`GAME-0001`–`GAME-0442`).
- Exact genome matches: none.
- Tied near matches: `GAME-0360` — Space Invaders (`4 / 23 = 0.173913`).
- Supported combination subsets: none.
- Scan date: 2026-09-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0360` Space Invaders | `SYS-215`, `CON-183`, `OBJ-029`, `TIM-003` | Both have live shot exchange, finite lives and a bounded hostile set. Space Invaders moves a cannon under a descending formation with one projectile at a time and eroding fortresses; Time Crisis uses a physically aimed arcade gun, a pedal that trades exposure for cover/refill, a continuous deadline and clearance-gated camera viewpoints. The shared genes do not make the player's control loop interchangeable. | Sole tied-near maximum, not exact (`4 / 23 = 0.173913`). |

## Taxonomy impact

`TAXONOMY_CHANGE_180` admits the cover-refill, designated-target time bonus, exposed-magazine gate and live resource display boundaries. Earlier signatures and verified combinations do not change.

## Negative results

- Do not import `SYS-967`: its NES-specific darkness and target-local light sequence was not verified for the Namco arcade gun.
- Do not import `ACT-226`: the player does not choose a traversal position along cover in this bounded gunfight.
- Do not equate Story Game's finite lives with Timed Game's unlimited lives, nor the arcade opening with PlayStation-only Special Mission.
- Exact ROM revision, operator clock setting, sensor algorithm, enemy accuracy and frame timing were not measured.

## Delta summary

## New facts

- [Observation | Corroborated | High] The Action Pedal couples cover and automatic six-shot refill while the deadline continues (`TC-001`–`TC-003`).

## New genes

- [Observation | Corroborated | High] Four typed boundaries in `TAXONOMY_CHANGE_180` distinguish the cover/reload and target-time decisions from generic gunfire.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed; proper-subset support is recomputed in the comparison section.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_180`; no older signature is edited.

## New questions

- Would a documented original arcade PCB trace clarify the gun sensor protocol and first-target bonus condition without changing the cover/time boundary?

## Next game

`GAME-0444` *Harvest Moon: Back to Nature* is the next recorded unit, only after this unit's acceptance and the Goal stop window. No push, public publication or deployment is authorised.
