---
game_id: GAME-0667
slug: saros
game_title: "SAROS"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-223
    - ACT-341
    - ACT-719
    - ACT-888
  system:
    - SYS-215
    - SYS-456
    - SYS-578
    - SYS-1915
    - SYS-1916
  constraint:
    - CON-882
  information:
    - INF-119
    - INF-613
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: SAROS

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The arena, boss, projectile colours and DualSense labels are parameters.

## Analysis scope

- Version / ruleset: English commercial PlayStation 5 base game,
  released April 30, 2026. Ordinary solo combat with the default
  shield cost, the Power Weapon already acquired and no Carcosan
  modifiers in the reference recipe. The capture's exact patch,
  controller telemetry and complete modifier sheet are unverified.
- Structured analysis target: PLAT-PLAYSTATION-5 in
  `knowledge/platforms/games.json`. W1 is attributed to PS5 Pro.
  Sony identifies the same commercial release for PS5 and PS5 Pro.
- Entry: after the Shattered Rise gate opens, cross the entrance to
  the Prophet arena with an ordinary gun, Soltari Shield and the
  acquired Carcosan Power Weapon. Begin with the first boss bar.
- Primary decision loop: steer to keep a line to the current plants
  or eye. Dash or jump over a threatening yellow pattern. Hold the
  shield through a reachable blue volley to refill Power, then lower
  it and use a fully pressed L2 and R2 to spend Power while the eye
  is open. Repeat across the two linked-target phases and the final
  confined corridor.
- Exit: the Prophet result settles, the boss bar disappears and the
  area beyond is traversable. Follow the opened exit, return to the
  Passage and use the World Dial to enter Ancient Depths. End at
  regained movement in the new biome before its first encounter.
- Included: aimed ordinary and powered attacks, protected dodge,
  shield hold and release, reserves and projectile classes, visible
  damage eligibility, linked-target gates, sustained live pressure,
  terminal clear and the first successor traversal.
- Excluded: the prologue Consort, the approach before the arena,
  build and loot optimisation, subsequent fighting in Ancient Depths,
  the later parry and opposed red-projectile rules, higher shield
  upgrades and corruption recovery routes, Second Chance, reset
  persistence, modifiers and New Game Plus. The exact gain, cost and
  damage coefficients are unmeasured.
- Potential scoped modules: a separate unlock of the greater shield,
  an upgraded shield's corruption-and-purge cycle or a biome restart
  with an explicitly verified loadout.

## Direct-play status

No personal installation or play. Sony's launch notice identifies the
final commercial release. Housemarque documents the control depths and
contact-to-Power loop. The broad hands-on account is used for its
documented input behaviour, corroborated by release-period frames.
W1 is a PS5 Pro-attributed launch-day clear and first successor entry.
W2 independently corroborates the phase order and successful result.
Static frames only were inspected in the background without audio.
Neither recording provides a verified build number or physical inputs.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SAR-001 | Housemarque's SAROS had its commercial PS5 launch on April 30, 2026. | Observation | Direct | High | P1 |
| SAR-002 | Holding R1 sustains a body-enclosing field while Power is available. Half-travel L2 readies the ordinary weapon mode and full travel readies the acquired Power Weapon. R2 commits the selected attack. | Observation | Corroborated | High | P2 weaponry, P3 controls, P4 shield modifier contrast, W1 1:16:39–1:16:52 |
| SAR-003 | A raised shield can remove eligible blue attacks and pool the energy. Yellow patterns in the chosen route use movement and dash, rather than the safe blue absorption rule. | Observation | Corroborated | High | P2 shield, P3 Power, W1 1:14:38–1:14:43, W2 1:15–1:30 |
| SAR-004 | The defender can spend the contact-funded pool on a separately aimed Power Weapon discharge. Shield maintenance also draws on that pool under ordinary rules. W1 holds the blue field, collects incoming shots, then visibly fires the transformed arm. | Observation | Corroborated | High | P2, P3, P4, W1 1:16:49–1:16:53 |
| SAR-005 | Early phases gate eye damage by linked plant targets. Visible projectile cues, centre exposure and the segmented protection bar inform different decisions. A later arena contraction makes the final corridor distinct. | Observation | Corroborated | High | W1 1:13:05–1:13:25 and 1:16:38–1:16:42, W2 0:50–1:20 and 4:50–5:10, G1 |
| SAR-006 | The final corridor allows ordinary direct damage to the exposed centre while yellow waves and blue volleys continue. The terminal defeat removes the boss bar and allows ordinary movement again. | Observation | Corroborated | High | W1 1:16:41–1:17:22, W2 5:40–6:00, G1 |
| SAR-007 | After the Prophet clear, the Passage and World Dial lead into the playable Ancient Depths, and ordinary movement resumes before the next fight. | Observation | Corroborated | High | W1 1:17:18–1:18:55 and 1:28:55–1:29:22, G1, P5 World Dial |

## Basic data

- Release / origin: Housemarque and Sony Interactive Entertainment,
  2026. Single-player third-person combat on native PS5.
- Families: FAM-009 for reading incoming trajectories, protection and
  attack windows. FAM-010 for decisions under moving projectile pressure.
- P1: [Sony Interactive Entertainment commercial launch](https://sonyinteractive.com/en/press-releases/2026/saros-launches-worldwide-exclusively-on-playstation5/).
- P2: [Housemarque's weaponry and abilities](https://blog.playstation.com/2025/09/24/saros-launches-march-20-on-ps5-first-look-at-gameplay-from-todays-state-of-play/).
  The work-in-progress visuals do not establish the exact retail fight.
  The developer describes holding R1, absorbing projectiles, selecting
  the Power Weapon with full L2 and releasing with R2.
- P3: [PlayStation hands-on account of combat and Power](https://blog.playstation.com/2026/03/26/saros-hands-on-report-intense-sci-fi-action-in-a-beautiful-deadly-alien-world/).
- P4: [Housemarque's launch accessibility and modifier documentation](https://blog.playstation.com/2026/04/23/saros-gameplay-modifiers-accessibility-options-and-more-detailed/).
  The separately selected Shield Power Enhancement eliminates the normal
  shield debit. That altered rule is excluded.
- P5: [Housemarque's World Dial and biome progression](https://blog.playstation.com/2026/02/12/saros-eclipse-escalation-gameplay-revealed-customization-options-detailed/).
- W1: [Esoterickk, PS5 Pro release-period trace](https://www.youtube.com/watch?v=0jLqJsrhgR4&t=4344s).
  The creator discloses a PlayStation-supplied copy. The clip is used
  for visible game states. It does not establish an exact initial patch.
- W2: [Tube Station Gaming, independent PS5-attributed clear](https://www.youtube.com/watch?v=fPSRtruqCqE).
  Documented on May 7, 2026. The early open arena, blue shield and final
  corridor settle at a visible defeat. Its exact PS5 model is unverified.
- G1: [VGC, Shattered Rise and Prophet route](https://www.videogameschronicle.com/guide/saros-shattered-rise-walkthrough-and-prophet-boss-guide/).
  A release-window corroboration for the linked targets, contrasting
  third phase and the name of the next biome.
- Claim IDs: SAR-001–SAR-007.

### Reproducible route evidence

1. Enter the Shattered Rise boss arena with the unlocked Shield and
   Power Weapon. W1 approaches around 1:12:24. Its first active fight
   after the intro exposes the plants and the current Prophet bar.
2. During the first two phases, prioritize the required plants before
   spending the stronger shot on the centre. The dashed bar and
   protected eye show the closed damage state. At open moments a
   shot on the centre can reduce the boss bar. A second phase adds
   plant threats in the arena. W2's open-arena sequence supplies
   a separate replay of this boundary.
3. Catch the blue volleys. W1 at 1:14:39–1:14:41 visibly surrounds the
   avatar with the shield, collects several blue shots and follows
   with a separate orange discharge. At 1:16:49–1:16:52 the same
   cycle is visible in the corridor: blue approach, maintained
   shield, contact with the field, lowered field and the arm shot.
   The developer identifies the controls. The footage supplies
   shield, projectiles and discharge, with no button overlay.
4. When the roots narrow the arena, use the still exposed centre and
   move through safe gaps in the yellow waves. At about 1:17:18 W1
   shows the Prophet trophy and replaces the boss bar with an
   updated route objective. Movement resumes among the aftermath
   effects and into the far exit. W2 shows a separate terminal clear
   at about 5:45.
5. W1 returns to the Passage around 1:18:34. After the interlude,
   choose Ancient Depths at the World Dial around 1:28:55. It loads
   around 1:29:08, and the player walks through the circular doorway
   around 1:29:22. Stop at this resumed movement.

## Mechanical decomposition

### Action Genes

- ACT-008: steer the same avatar in the arena and across the successor
  threshold. SAR-005–SAR-007.
- ACT-161: aim ordinary fire through reachable plants and fire the
  prepared weapon into the exposed centre. SAR-002, SAR-005, SAR-006.
- ACT-223: time a dodge or jump response to a moving wave rather
  than stand through all attacks with the shield. SAR-003, SAR-006.
- ACT-341: address the World Dial after the first biome clear to
  initiate the selected destination. SAR-007.
- ACT-719: the depth of L2 chooses an ordinary aimed mode or readies
  the Power Weapon, and R2 commits the attack. SAR-002.
- ACT-888: raise, hold and lower the body-enclosing shield by an
  independent requested input. SAR-002–SAR-004.

### System Behaviour Genes

- SYS-215: resolve direct movement, shooting and enemy attacks in
  the live arena. SAR-003, SAR-005, SAR-006.
- SYS-456: a timed eligible dash has a protected interval through
  attacking overlap, without protecting later standing exposure.
  SAR-003, SAR-006.
- SYS-578: accepted damage depletes the current armour condition and
  ordinary restorative pickups can replenish current integrity.
  SAR-003, SAR-006, G1.
- SYS-1915: remove a shielded eligible projectile and credit its
  energy to the spendable reserve. SAR-003, SAR-004.
- SYS-1916: held shield maintenance and a committed Power Weapon
  attack debit the same Power reserve. SAR-002, SAR-004.

### Constraint Genes

- CON-882: linked targets control the protected core in the early
  phases. A later corridor leaves the centre exposed. SAR-005, SAR-006.

### Information Genes

- INF-119: the combat view exposes personal armour and Power alongside
  live weapon state. SAR-002–SAR-004.
- INF-613: projectile appearance directs the defensive choice, while
  the segmented enemy bar and eye independently show current damage
  eligibility. SAR-003, SAR-005, SAR-006.

### Objective Genes

- OBJ-080: defeat Prophet as the route guardian and reach live
  movement in Ancient Depths after opening that route. SAR-006, SAR-007.

### Time Genes

- TIM-003: volleys and protection windows progress while inputs are
  accepted. Shield and shot timing matter during that live interval.
  SAR-003–SAR-006.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Locked eye and linked plants | Aim and destroy the current linked plant set | Eye admits damage | SAR-005 |
| Blue volley and usable Power | Hold the enclosing shield so the volley contacts it | Blue projectiles absorbed, Power credited | SAR-002–SAR-004 |
| Sufficient Power and open eye | Fully press L2, aim and fire with R2 | Separate Power Weapon discharge and reserve debit | SAR-002, SAR-004 |
| Advancing yellow wave | Jump or commit an eligible dodge into a safe path | Survive the wave without relying on blue absorption | SAR-003, SAR-006 |
| Late health substage | Continue live play after the roots close in | Narrow arena with sustained exposed centre | SAR-005, SAR-006 |
| Defeated Prophet | Cross the released route and choose Ancient Depths at the World Dial | Playable new biome | SAR-006, SAR-007 |

## Strategic and experiential structure

The moving blue projectiles are simultaneously threats and a potential
resource. Holding the field across empty space spends Power while
waiting. Aim the powered counterattack only when the protected core's
state admits a hit. The independent damage gate keeps a full reserve
from solving the encounter by itself. In the corridor, the decision
shifts from re-opening the eye to finding space in the available lane.

## Replay and variation

W2 settles the same result under a different visible sequence of hits
and health changes. The objective is the validated clear and playable
successor, with no exact required count of shots or shield pulses.
The selected resource costs exclude Shield Power Enhancement.

## Adjacent systems and history

Housemarque describes SAROS as an evolution of Returnal's active
bullet patterns. The half/full-trigger distinction is reused here,
while replenishment by successful shield contact differs from a
recharging alternate-fire branch.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-161, ACT-223, ACT-341, ACT-719, ACT-888 | Move, aim, evade, commit travel, select trigger depth and hold the barrier |
| System Behaviour | SYS-215, SYS-456, SYS-578, SYS-1915, SYS-1916 | Resolve live contact, dodge, armour, projectile credit and shared expenditure |
| Constraint | CON-882 | Open the core through its required linked targets |
| Information | INF-119, INF-613 | Show personal reserves, threat classes and damage eligibility |
| Objective | OBJ-080 | Clear the guardian and cross to playable Ancient Depths |
| Time | TIM-003 | Commit responses while hostile patterns continue |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `666` (`GAME-0001`–`GAME-0666`).
- Exact genome matches: none.
- Tied near matches: `GAME-0527` — Nine Sols (`9 / 25 = 0.360000`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Nine Sols (GAME-0527)](../m-r/nine-sols.md) | ACT-008, ACT-161, ACT-223, ACT-341, INF-119, OBJ-080, SYS-215, SYS-578, TIM-003 | Both use live defensive responses, state feedback and a guardian clear to continue. Nine Sols earns Qi by precision-graded parries and spends it through a marked target and sustained talisman hold. SAROS holds an enclosing field, converts eligible blue projectiles into shared Power and spends it on a separate aimed discharge against a conditionally exposed core. | Near, `0.360000` |

## Taxonomy impact

Five isolated definitions cover the body-enclosing hold, contact
credit, shared ongoing and committed debit, linked-target core gate
and distinct threat and vulnerability cues. Eleven definitions
retain their existing boundaries. The shield consumes the incoming
projectile and pools value for a later independently aimed attack.
It does not redirect the same moving object to its source.

## Negative results

- A raised shield in empty space does not supply the same credit as a
  blue collision. Aimed use of the Power Weapon also requires its
  separate commitment.
- The half-travel ordinary fire state does not spend the same
  Power reserve by default.
- Early protected core damage remains conditional even with a
  fully selected Power Weapon. The last corridor changes that state.
- The trace provides no measure of per-projectile gain, shield frame
  costs, exact corruption effect or reset behaviour.

## Delta summary

Sixteen admitted genes, including eleven reuses and five additions.

## New facts

- Defence and a separately aimed attack share the Power budget.
- Eligible contacts can make temporary defence a net resource gain.
- The encounter ends in a confirmed traversal boundary after the clear.

## Principles and design implications

Make attack eligibility independent of the visibility of a target.
A defence that costs a reserve can encourage moving toward one
telegraphed threat while moving away from another. Expose the shared
balance and the state that makes spending it productive.

## Puzzle or game generation potential

A new arena can combine a shield budget, absorbable hazards and
lockable vulnerable points. Vary the order of qualifying volleys
and window availability. Preserve independent defensive and offensive
commitments so collection remains a decision.

## New genes

- ACT-888
- SYS-1915
- SYS-1916
- CON-882
- INF-613

## New combinations

No verified combination is a proper subset of the sixteen-gene scope.

## Taxonomy changes

[TAXONOMY_CHANGE_413](../../../research/taxonomy-changes/TAXONOMY_CHANGE_413.md).

## New questions

How does upgrading the shield change yellow conversion and purge?
Does exhausting the ordinary reserve produce a measurable delay
before the next shield is allowed? Which costs are weapon-dependent?

## Next recommended game

Tomba! on the original North American PlayStation. Follow the
Clear the Fog event through the reopened path.

## Why this game

The early Prophet fight supplies a full example of a defensive
contact becoming a deliberate offensive resource.
