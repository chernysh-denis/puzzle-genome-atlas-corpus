---
game_id: GAME-0450
slug: ssx-tricky
game_title: SSX Tricky
analysis_status: reviewed
reviewed: 2026-09-28
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-593
    - ACT-594
  system:
    - SYS-1181
    - SYS-1182
    - SYS-1183
    - SYS-1184
  constraint:
    - CON-726
  information:
    - INF-435
  objective:
    - OBJ-257
  time:
    - TIM-003
---

# Game: SSX Tricky — one Garibaldi Single Event Race

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Rider, board, opponent difficulty, trick names and boost amounts are parameters, not genes.

## Analysis scope

- Version / ruleset: the original 2001 *SSX Tricky* PlayStation 2 edition, one single-player Single Event Race on the initially available Garibaldi course, with an initially available rider and default board against the Amateur computer field. The exact PS2 disc revision and control mapping were not inspected. EA's original GameCube instruction booklet supplies cross-platform game rules; a contemporary first-hand PS2 guide corroborates Garibaldi and race-specific behaviour. Platform-specific button claims are excluded.
- Primary decision loop: read the descending course and rival position, carve or brake toward a faster safe line, crouch and jump where sufficient air is available, choose a grab or rotation and release it before landing, then spend the adrenaline earned from a successful trick to accelerate. Once the meter permits an Uber trick, a successful landing advances the TRICKY letters; completing that set makes boost unlimited for the rest of this descent. Repeat line, air, landing and boost decisions while the opponent field races to the finish.
- Entry and exit: accept the rider, Single Event Race, Amateur field and Garibaldi; the controllable packet starts when the start gate opens. It ends at the first classified finish of that descent. First place is the local positive target; another place is a completed race but not a win. No World Circuit medal or later venue unlock is claimed.
- Included: direct downhill steering and speed control, route/airtime tradeoff, rider field, aerial trick selection and landing, trick score and finite adrenaline, requested boost, the full-meter Uber window and successful-Uber TRICKY accumulation, ranked race finish and live speed/place/meter feedback.
- Excluded: Showoff's score objective, crystals and timed checkpoints; Time Challenge; World Circuit qualifying heats, medals and skill-point upgrades; Trick Book chapters, persistent customisation, two-player mode, record saving, exact board statistics, exact trick multipliers, exact course geometry, shortcuts or guaranteed winning line. Player attacks against rivals and specific button bindings are not asserted for this packet.
- Direct-play status: no PS2 disc, emulator execution, save, input trace, screenshot, video or completed run was inspected. A contemporaneous EA-authored GameCube manual describes the same named game and mode but does not prove PS2-only control details. A first-hand PS2 guide supports Garibaldi's alternate lines and trick-to-boost tactics. Exact physics, meter coefficients, CPU policy and a particular first-place result remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SSX-001` | Single Event offers a one-descent Race on initially available Garibaldi against selectable computer difficulty; World Circuit adds separate multi-heat progression. | Observation | Corroborated | High | P1, S1 |
| `SSX-002` | A rider descends an authored course against autonomous opponents, with line, turns, jumps and finish place affecting the Race result. | Observation | Corroborated | High | P1, S1 |
| `SSX-003` | A crouch-and-release jump permits a chosen aerial grab or rotation; the trick must be released and landed to credit points. | Observation | Direct | High | P1 |
| `SSX-004` | Successful tricks raise a spendable adrenaline meter, whereas time and falls can reduce it; boosting uses that reserve for speed. | Observation | Corroborated | High | P1, S1 |
| `SSX-005` | A full meter opens a temporary Uber opportunity; each successfully landed Uber fills one TRICKY letter, and the completed word grants unlimited adrenaline for the rest of the run. | Observation | Corroborated | Medium | P1, S1 |
| `SSX-006` | Garibaldi has a main racing line and alternate jump-rich route, but no exact fastest path or reliable win is established. | Observation | Limited | Medium | S1 |
| `SSX-007` | No PS2 disc execution, precise controls, race trace, physics coefficients or opponent schedule was inspected. | Confirmed | Direct | High | R1 |

## Basic data

- Origin: EA Canada / EA Sports BIG original *SSX Tricky*, not the first *SSX*, *SSX 3* or the 2012 reboot.
- Platform: original PlayStation 2 target in `knowledge/platforms/games.json`; the mechanically equivalent cross-platform booklet is identified as such, never passed off as the PS2 manual.
- Mechanical families: real-time system pressure (`FAM-010`) through a live rival race and physics/object manipulation (`FAM-007`) through speed, terrain contact and aerial landing.
- **P1:** [EA's original *SSX Tricky* GameCube instruction booklet](https://manualzz.com/doc/25168321/electronic-arts-ssx-tricky-video-game-instruction-booklet), original 2001 authored artifact in an OCR reproduction, inspected 2026-09-28; Single Event Race, Garibaldi availability, course reading, trick input/landing, score, adrenaline, Uber window, TRICKY letters and infinite reserve. OCR is noisy; only legible rule passages are used, and GameCube button mappings do not transfer to PS2.
- **S1:** [Wolf Feather's firsthand PlayStation 2 *SSX Tricky* guide](https://gamefaqs.gamespot.com/ps2/469884-ssx-tricky/faqs/14817), inspected 2026-09-28; describes Garibaldi alternate routes, jump opportunities, boost from landed tricks and completed TRICKY reserve during Race. Personal tactics are not treated as an optimal-route proof.
- **P2:** [EA's official SSX franchise page](https://www.ea.com/en-gb/games/ssx), inspected 2026-09-28; establishes the action-racing/trick series identity, not the original edition's detailed mechanics.
- **R1:** local preflight found no original PS2 execution or input record for this unit. A search result called “SSX Tricky manual” actually reproduces the first *SSX*'s booklet, and EA's 2012 SSX manual is a different ruleset; neither is rule authority here.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for directly steering the controlled rider through one traversable downhill space, including line changes and a timed jump. This does not choose a precomputed path or stop the rival field.
- `ACT-593` chooses and holds an eligible aerial grab or rotation after takeoff, then releases it for the attempted landing. The trick input is a separate decision from carving the racing line.
- `ACT-594` requests acceleration from the current adrenaline reserve while it is spendable. Ordinary downhill momentum and an unearned permanent boost are excluded.

### System Behaviour Genes

- `SYS-1181` advances the boarder's speed and trajectory over snow, turns, ramps, obstacles and landing contact. A shortcut can trade distance for difficult jumps; exact handling coefficients are unknown.
- `SYS-1182` advances the computer riders in the same downhill event and classifies each finisher by place at the course finish. It does not imply World Circuit qualification or medal award.
- `SYS-1183` credits successfully landed trick points and adrenaline by difficulty, applies repetition discount to score, and reduces a finite adrenaline reserve through spending, time or falls. The exact scoring and drain formula is not asserted.
- `SYS-1184` opens a time-limited Uber opportunity at a full meter; a successfully landed Uber fills the next TRICKY letter. Once the whole word is filled, the reserve no longer drains from requested boost during the rest of this run.

### Constraint Genes

- `CON-726` requires the airborne manoeuvre to finish with a valid landing before points, adrenaline or an Uber letter are credited. A fall forfeits the attempted trick and can also cost meter. The exact safe-angle threshold remains unmeasured.

### Information, Objective and Time Genes

- `INF-435` exposes current race place, speed, score, the adrenaline level, Uber eligibility and TRICKY-letter progression alongside the visible near-course and rivals. The complete future route and CPU plans are not disclosed.
- `OBJ-257` sets the local positive result as first place at the finish of this one Single Event Race; a lower classification ends the event without satisfying that target.
- Reuse `TIM-003`: rider, rivals and meter state continue advancing while the player chooses line, trick and boost inputs.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Why it matters | Claim ID |
|---|---|---|---|---|
| Amateur Garibaldi Single Event Race is accepted | Start gate opens | Rider and opponents begin a common downhill race | Defines one attempt, not a World Circuit heat | `SSX-001`, `SSX-002` |
| A turn and alternate ramp are visible ahead | Steer to a chosen line | Rider follows that terrain and trades route length against air opportunity | Route choice affects both position and future boost income | `SSX-002`, `SSX-006` |
| A ramp gives enough apparent air | Crouch, release to jump, choose a grab, release before snow contact | Clean landing credits trick points and adrenaline | Tricks can pay for later speed rather than only cosmetic score | `SSX-003`, `SSX-004` |
| A trick remains held at contact | Fail the landing | Attempted points and Uber credit are lost; reserve can fall | More ambitious air creates a measurable risk | `SSX-003`–`SSX-005` |
| Adrenaline is available on a clear straight | Request boost | Finite reserve is spent for speed while rivals continue | Timing the spend is separate from earning it | `SSX-004` |
| Meter is full and Uber window is open | Land an eligible Uber trick | One TRICKY letter becomes filled; completing all letters unlocks unlimited boost for this descent | The same trick economy can change its own late-race constraint | `SSX-005` |
| Rider crosses the finish after the field has contested the descent | Read classified place | First is local success; another place is a complete but unsuccessful attempt | Race rank, not Showoff score, is the terminal predicate | `SSX-001`, `SSX-002` |

## Strategic and experiential structure

The shortest visible line need not be the fastest eventual line: a ramp can add airtime for a landed trick, raising adrenaline that can be spent on the next straight. Holding a more complex trick longer risks losing its reward at touchdown. Repeated successful Uber landings can convert a finite boost economy into a lasting within-run advantage, but the sources do not establish a guaranteed route to that state or a first-place outcome. A live opponent field keeps time costly while the player makes these tradeoffs.

## Replay and variation

Garibaldi is an authored course rather than a procedurally generated descent. Rider choice, route, trick timing, landing success and opponent performance can differ between attempts. No PS2 seed, exact CPU trajectory, board coefficient or deterministic replay was obtained.

## Adjacent systems and history

*Tony Hawk's Pro Skater 1 + 2* also scores traversal tricks, but its Warehouse packet builds one breakable connected trick chain around an objective timer; this Race packet uses landed tricks to fund a spendable speed reserve and an Uber progression inside a downhill contest. *F-Zero GX* also exposes a speed-resource decision against rivals, but its energy is shared with damage survival and manual boost is lap-gated, whereas this reserve is earned through snowboard tricks. Neither existing boundary can replace the landed-trick-to-adrenaline transition.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-593`, `ACT-594` | line, jump, trick, boost timing |
| System Behaviour | `SYS-1181`–`SYS-1184` | snow contact, rivals, adrenaline, Uber letters |
| Constraint | `CON-726` | valid landing |
| Information | `INF-435` | place, speed, meter, visible course |
| Objective | `OBJ-257` | win one Single Event Race |
| Time | `TIM-003` | continuously advancing race |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `449` (`GAME-0001`–`GAME-0449`).
- Exact genome matches: none.
- Tied near matches: `GAME-0391` — Uncharted 2: Among Thieves (`2 / 14 = 0.142857`).
- Supported combination subsets: none.
- Scan date: 2026-09-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0391` Uncharted 2: Among Thieves | `ACT-008`, `TIM-003` | Both directly steer a character in continuously advancing play, but Uncharted's scoped authored action route has traversal, gunplay and scripted combat objectives; this descent settles rival race place through landed tricks and an adrenaline-to-speed economy. The small intersection does not imply the games share an aerial or boost rule. | Near, `2 / 14 = 0.142857` |

## Taxonomy impact

`TAXONOMY_CHANGE_187` admits nine source-supported boundaries while earlier signatures and combinations remain unchanged.

## Negative results

- The first *SSX* manual and the 2012 SSX manual are not evidence for this game's Uber progression; Showoff crystals/checkpoints and World Circuit medal rules do not belong to this Single Event Race.
- `SYS-975` and `SYS-998` require a connected skateboard-trick chain, not separate landed snowboard tricks that refill speed. `SYS-1040` makes vehicle energy also absorb damage and is not this adrenaline economy.
- No PS2-specific button, exact ramp line, airtime threshold, meter coefficient or guaranteed first-place technique was verified.

## Delta summary

## New facts

- [Observation | Corroborated | High] Garibaldi Single Event Race supplies one bounded downhill contest with route and jump choices.
- [Observation | Corroborated | Medium] Landed tricks feed a finite boost meter and successive Uber landings can unlock within-run unlimited boost.

## New genes

- [Observation | Corroborated | Medium] Nine new boundaries distinguish trick and boost commands, downhill and rival resolution, trick-to-reserve settlement, Uber progression, clean-landing legality, live race disclosure and first-place evaluation.

## New combinations

- [Observation | Limited | Medium] None proposed; proper subsets are recomputed by index generation.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_187`; no earlier game signature changes.

## New questions

- Can a controlled original PS2 replay measure Garibaldi's exact jump windows, meter drain and CPU line without importing rules from a later SSX edition?

## Next recommended game

- [Hypothesis | Limited | Medium] No next unit is reserved in `RESEARCH_PLAN.md` after this ninth game; a future candidate requires maintainer selection, not implicit expansion.
- Optimisation criterion: preserve reviewed cross-platform diversity and avoid adjacent lookalike sports-race subjects.
- Expected information gain: a separately selected packet can test whether landed stunt rewards transfer beyond one snowboard title.
- Backlog impact: none; the current nine-game batch ends here.

## Why this game

- [Hypothesis | Limited | Medium] *SSX Tricky* closes the approved cross-platform set with a distinct real-time race in which stunt execution changes the speed economy; exact PS2 execution remains a future falsification path.
