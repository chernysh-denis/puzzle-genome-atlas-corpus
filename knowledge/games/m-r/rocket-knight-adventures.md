---
game_id: GAME-0643
slug: rocket-knight-adventures
game_title: "Rocket Knight Adventures"
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-295
    - ACT-856
  system:
    - SYS-215
    - SYS-910
    - SYS-1856
    - SYS-1857
    - SYS-1858
    - SYS-1859
  constraint:
    - CON-869
  information:
    - INF-597
  objective:
    - OBJ-329
  time:
    - TIM-003
---

# Game: Rocket Knight Adventures

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: original English North American NTSC-U Sega
  Genesis cartridge, Konami 1993, package designation T-95046.
  The primary trace is the USA/NTSC Easy run on a disclosed JVC
  X'Eye. Its physical cartridge and program hash were not inspected.
- Primary decision loop: navigate the live route and choose between
  normal sword attacks and preparing a rocket lunge, then choose the
  launch direction for the next hazard, passage or attack opening.
- Entry: start a fresh Stage 1, Kingdom of Zebulos, on Easy and
  reach controllable movement at the beginning of the outdoor route.
- Exit: defeat the segmented castle boss, settle the two bonus
  counters, pass the interlude and resume controllable play in
  Stage 2, Mountain range.
- Included: real-time terrain and sword actions, rocket charge,
  launch and rebound, flight mode within the bridge-to-castle
  route, current vitality and typed pickups, castle boss exposure
  and the subsequent score and stage handoff.
- Excluded: international cartridges and difficulty comparisons,
  sequels, the later Re-Sparked collection, exact frame timings
  and damage coefficients, route optimisation, full stock and
  Continue accounting, and Stage 2 combat outcomes.
- Suggested later scope: reproduce an early release and full release
  from the same position and isolate the effect of one versus two
  wall contacts on the resulting path.

## Direct-play status

No direct play was performed. Konami's North American instruction
booklet establishes the controls, including the full-charge release,
down or neutral spin, and the temporary flight pickup. Packaging
evidence identifies the commercial cartridge. A USA/NTSC leaderboard
entry links the Easy recording made on JVC X'Eye. A separate NTSC
longplay corroborates the charge and castle sequence, tally, and
actual successor. Frames were inspected in the background without
audio. Neither exact program revision nor the video authors'
physical inputs were inspected. The harder USA tool-assisted trace
corroborates specific route geometry only.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| RK-001 | Rocket Knight Adventures is a 1993 commercial English North American Sega Genesis cartridge, T-95046. The native primary trace is labelled USA/NTSC Easy. Konami's later collection is separately identified and outside scope. | Confirmed | Direct | High | P1 cover and back cover, P2 package inspection, P3 publisher rerelease notice, W1 submission and capture disclosure. |
| RK-002 | On the ordinary route, move, jump and use the sword directly while enemies and hazards continue. A sword swing can produce a visible travelling crescent. | Observation | Corroborated | High | P1 pp. 8–13. W1 0:10–0:16 and 2:38–2:50. W2 4:34–4:44 shows jumps and crescents moving away from the body. |
| RK-003 | Holding attack fills a separate Energy Gauge. Once full, release while selecting the direction for a rocket attack. The manual documents an in-place spin under down or neutral input. The launch is distinct from a usual jump. | Observation | Corroborated | High | P1 pp. 10–13. W2 4:48–4:51 shows charge fill and diagonal ascent. W1 2:43–2:45 also shows a charged ascent. The spin input branch is documented and was not isolated in these captures. |
| RK-004 | The castle has rising passages where a powered diagonal launch can reach higher footing or rebound off solid surfaces. Rebound can redirect the current lunge without selecting a separate wall-jump input. | Observation | Corroborated | High | P1 pp. 12–13 describes rebounds. W1 2:33–2:36 and 2:43–2:45. W2 4:49–4:51. R1 Stage 1-3 corroborates the route use without establishing Easy damage or duration values. |
| RK-005 | Visible current vitality, REST stock and score are separate from rocket charge. Enemy contact or attacks can subtract vitality. Under the scoped difficulty fruit can refill it and gems credit score. Ordinary movement and attacks remain possible through the hazard phase. | Observation | Corroborated | High | P1 pp. 8–9 and 14–15. W2 HUD and bonuses at 4:34–4:47. W1 shaft at 2:44 and pre-tally at 3:18 show different amounts of charge, score and vitality. |
| RK-006 | A power pack starts the sustained flight section after the bridge sequence. Steering and attack remain available during scrolling flight, while the manual excludes ordinary jump and rocket attack. Ground control returns after the water route. | Observation | Corroborated | High | P1 pp. 14–15. W2 3:20–3:24 flight entry, 3:25–3:40 rising, descending and striking, 4:29–4:35 wall transition and ordinary grounded stage state. W1 shows the same order. |
| RK-007 | The castle boss occupies different wall and ceiling openings. An exposed head can be attacked. The segmented sweep remains a separate positional threat. The defeat sequence begins with explosions and ends the live encounter. | Observation | Corroborated | High | W1 2:57–3:13 and W2 6:30–7:40. R1 Stage 1-3 and R2 head and tail account. Exact health, hit registration windows and vulnerability of each segment remain unmeasured. |
| RK-008 | Castle-boss defeat leads directly to a clear and life bonus tally, then a scene on the ledge and actual Stage 2 play with retained total score and replenished vitality. The two runs show the same clear bonus and different life bonuses. | Observation | Corroborated | High | W1 3:10–3:38 and W2 7:37–8:36. P1 pp. 8–9 and 16–17 distinguish the end-boss result and Mountain range successor. |

## Basic data

- Analysis target: `PLAT-SEGA-GENESIS`.
- Developer and regional publisher: Konami, with Konami (America)
  identified on the North American release.
- Mechanical family: `FAM-010`, real-time system pressure.
- Checked: 2026-11-22.
- P1: [Konami's North American Genesis instruction booklet](https://segaretro.org/images/3/34/Rocket_Knight_Adventures_MD_US_Manual.pdf).
- P2: [CGC inspection of a 1993 Genesis clamshell, T-95046](https://www.cgcvideogames.com/en-US/cert-lookup/results?certNumber=1012535007).
- P3: [Konami's Re-Sparked compilation announcement](https://www.konami.com/games/ca/en/topics/2535/),
  used for the exclusion of added features.
- W1: [01Garland01, 28:09 run recorded on JVC X'Eye](https://www.youtube.com/watch?v=jCFw5ST164A&t=136s)
  and [USA/NTSC Genesis Easy submission](https://www.speedrun.com/rka/runs/mrk4j18y).
  The timer on its left is external to the game.
- W2: [Retro Game Spacko, NTSC Genesis longplay](https://www.youtube.com/watch?v=WGI17AxJMuo&t=264s).
  The recording's console setup and difficulty are not independently
  established. Its life bonus is an observed result only.
- R1: [upthorn, USA Genesis input trace and route notes](https://tasvideos.org/1670S),
  consulted for Stage 1-3 propulsion geometry. Its hard difficulty
  and optimised inputs do not define the Easy run.
- R2: [El_Seph's firsthand Genesis route notes](https://gamefaqs.gamespot.com/genesis/563338-rocket-knight-adventures/faqs/24897),
  limited to the castle boss head and tail relationship.

## Mechanical decomposition

### Action Genes

- ACT-008: walk and jump along directly traversed terrain.
- ACT-295: use a normal sword attack on a legal contact or at range.
- ACT-856: prepare a rocket action by holding attack. Select the
  direction and release.

### System Behaviour Genes

- SYS-215: resolve real-time exchanges with enemies. Vitality
  and attack position can change during one traversal.
- SYS-910: apply typed stage pickups on contact, such as fruit
  restoring vitality and the power pack changing local mobility.
- SYS-1856: redirect a committed lunge at solid geometry.
- SYS-1857: maintain flight across the water section under its
  distinct steering and attack controls.
- SYS-1858: expose an attackable boss head at shifting openings
  while the travelling segments threaten the rest of the room.
- SYS-1859: score clear and remaining vitality separately, then
  start the successor with the new total and replenished vitality.

### Constraint Genes

- CON-869: a rocket release needs the full held charge. A normal
  attack remains a separate available action.

### Information Genes

- INF-597: read rocket energy together with separate vitality,
  score and remaining stock while the scene remains active.

### Objective Genes

- OBJ-329: defeat the required final castle adversary to trigger a
  clear directly, after reaching its room through the earlier route.

### Time Genes

- TIM-003: prepare, steer, move or strike while threats and the
  scrolling flight scene continue on their own schedule.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| Opening outdoor terrain with enemies | Walk, jump or use the ordinary attack while threats move | Live traversal and short-range or travelling attack effects | RK-002, RK-005 |
| Ordinary state beside castle shaft | Hold attack until the gauge is full, set the diagonal input and release | The active rocket lunge climbs from the lower footing. A wall contact can redirect it | RK-003, RK-004 |
| Water-side pickup after the bridge fight | Contact the power pack | Sustained scrolling flight with steering and attacks. Castle entry restores ground traversal | RK-006 |
| Castle boss exposes head through an opening | Jump or strike at the exposed head and move clear of the sweep | A hit can register while the head remains exposed. The boss can otherwise continue through another opening | RK-007 |
| Decisive boss hit | Let the defeat sequence and tally resolve | The clear and life counters both transfer to score. No separate clear item is needed | RK-008 |
| Settled result and ledge scene | Transition to Stage 2 | Control resumes in Mountain range with replenished vitality and the settled score | RK-008 |

## Strategic and experiential structure

Charge changes both what can be reached and how the body commits.
An ordinary slash can be taken promptly or projected from a different
position. A lunge requires prior preparation and can carry the body
along a new path at a wall. The flight section preserves sword
attacks while removing the ordinary jump and burst options. At the
castle boss, move for the head without intersecting the tail lane.

## Replay and variation

The main path has an outdoor approach and bridge encounter before
flight over the water and the sequence of castle rooms. W1 advances
quickly through the castle and enters the final boss near 2:57.
W2 uses more exchanges and enters at about 6:25. W1 displays a
23,110 pre-tally score, 9,000 clear bonus and 1,200 life bonus near
3:18. W2 shows 26,280, 9,000 and 12,800 respectively near 7:44.
The resulting totals are 33,310 and 48,080. The cases establish
separate bonus fields and a vitality-linked difference, without
establishing a coefficient or difficulty comparison.

## Adjacent systems and history

The booklet documents mode-dependent lives, extra units and
continues. The recorded scope uses the current vitality and charge
in a successful path. The exact failure and retry stock accounting,
the optional tail hang and later underwater controls remain
outside the admitted genome. Pause, save states, rewind and
Boss Rush do not determine the original settlement described here.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-295, ACT-856 | Move, use normal attack or prepare and release directional propulsion |
| System Behaviour | SYS-215, SYS-910, SYS-1856, SYS-1857, SYS-1858, SYS-1859 | Exchange damage, apply local pickups, rebound, fly, respond to boss geometry and settle both bonuses |
| Constraint | CON-869 | Require a full held charge for rocket release |
| Information | INF-597 | Disclose charge readiness separately from vitality, score and lives |
| Objective | OBJ-329 | Clear the required adversary directly |
| Time | TIM-003 | Act while threats and hazards progress |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `642` (`GAME-0001`–`GAME-0642`).
- Exact genome matches: none.
- Tied near matches: `GAME-0641` — Bushido Blade (`4 / 22 = 0.181818`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Bushido Blade (GAME-0641)](../a-f/bushido-blade.md) | ACT-008, ACT-295, OBJ-329, TIM-003 | Both use directly controlled movement and attacks to defeat a required opponent in real time. Bushido Blade settles a continuous duel through stance-dependent weapon contact and a decisive body hit. Rocket Knight Adventures uses charged trajectory through a multi-section route, shifting boss attack openings and a score tally before the next stage. | Near, `0.181818` |

## Taxonomy impact

Seven new definitions distinguish the held input and full threshold,
visible readiness, rebound, scoped flight substitution, the
segmented boss and the bonus handoff. Six existing definitions
are reused. See Taxonomy Change 389 for the boundary review.

## Negative results

- A ready gauge does not imply that ordinary rocket attack is allowed
  in the sustained flight section.
- A rocket lunge can change its path on contact. It is not a free
  midflight jump or a permanently equipped flight mode.
- The displayed life bonus is distinct from the REST counter.
  The consumed vitality indicators during the tally do not count
  as losing the current attempt.
- The final score and transition were observed. No clear-time
  grading or permanent save is established by the display.

## Delta summary

Thirteen admitted genes, with the rocket decision linked to
terrain, an alternate flight mode and a separate stage settlement.

## New facts

- A visible full held charge is used for the default rocket release.
- The scoped castle path gives diagonal propulsion and terrain
  rebounds distinct value beyond direct damage.
- The boss's head and its trailing segments pose different decisions.
- Clear and life bonus counters transfer into the next stage's score.

## Principles and design implications

Make readiness readable during live movement. One committed lunge
can have different reach based on directional selection and solid
geometry. Distinct local movement kits can preserve shared actions
while changing their adjacent options.

## Puzzle or game generation potential

Prototype a vertical route with one full-charge lunge, asymmetric
walls and a high ledge. Compare a direct approach and a rebound
route. Put the charge and allowed movement mode in separate cues.

## New genes

ACT-856, CON-869, INF-597, SYS-1856, SYS-1857, SYS-1858 and SYS-1859.

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_389](../../../research/taxonomy-changes/TAXONOMY_CHANGE_389.md).

## New questions

Can a matched Easy run isolate the permitted ricochet count
and reveal which contact consumes the remaining lunge?

## Next recommended game

Analyse the commercial native iPhone edition of WHAT THE CAR?
through one completed run and its visible reward or next state.

## Why this game

The same attack input can prepare a traversal decision. The
level makes that distinction visible through shafts, airborne
sections and a settled boss result.
