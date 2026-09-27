---
game_id: GAME-0415
slug: crazy-taxi
game_title: Crazy Taxi
analysis_status: reviewed
reviewed: 2026-09-26
combination_ids: []
gene_ids:
  action:
    - ACT-290
  system:
    - SYS-320
    - SYS-365
    - SYS-1102
    - SYS-1103
    - SYS-1104
  constraint:
    - CON-700
    - CON-701
  information:
    - INF-408
  objective:
    - OBJ-002
  time:
    - TIM-003
---

# Game: Crazy Taxi — Dreamcast Arcade rules

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Driver, passenger, route, starting clock, fare amount and traffic position are parameters rather than separate genes.

## Analysis scope

- Version / ruleset: original English Dreamcast *Crazy Taxi* (2000), `ARCADE` course with `PLAY BY ARCADE RULES`, default one-player controller. This selects the arcade course and the rule packet that grants time bonuses; it is not the separate `ORIGINAL` course or the fixed three-, five- or ten-minute modes. Exact disc revision and option values were not inspected, so the initial clock and traffic setting are not asserted numerically.
- Structured analysis target: `PLAT-DREAMCAST` in [`knowledge/platforms/games.json`](../../platforms/games.json). The historical arcade machine is the course/rule origin, not the platform claimed for this record.
- Primary decision loop: choose an available street customer, stop inside their pickup circle, steer the occupied taxi toward the assigned destination while weighing direct speed against manoeuvre tips and collision risk, stop inside the green arrival zone before that customer's deadline, take the fare and any Arcade-rule time extension, then choose another customer while the overall game clock remains positive.
- Entry and exit: begin after choosing a driver and gaining control of the taxi on the Arcade course; stop at the results screen when the overall game-time counter reaches zero. The displayed customer count, total money and class evaluate that run; an S class is not required.
- Included: direct steering, accelerator, brake and Drive/Reverse sequences including the manual's Crazy Dash and Crazy Drift; active road traffic and collision; choice among simultaneously visible customers; full-stop pickup and destination zones; assigned destination and per-customer deadline; base fare, manoeuvre tips, remaining-customer-time bonus fare, collision-breakable tip combo, Arcade-rule extension of the overall timer, and visible route, clock and earnings cues.
- Excluded: `ORIGINAL` course geometry, fixed-duration modes without time bonus, Crazy Box challenges, Rally Wheel specifics, save/load, leaderboard persistence, character biography, branded businesses, precise collision damage, exact traffic behaviour beyond witnessed obstruction/collision, numerical fare formula beyond the manual and unmeasured option settings. The driver cannot exit the taxi on foot in this packet.
- Potential scoped modules: `ORIGINAL` course with its distinct layout, a named Crazy Box challenge, or one fixed-duration mode without extensions.
- Direct-play status: none. No Dreamcast console, disc, controller trace, gameplay video or audio was inspected. The original Sega Dreamcast manual's 21-page PDF was downloaded and its rules pages text-extracted and visually checked. A contemporary Dreamcast review corroborates the time-extension loop. Exact frame timing, starting options and traffic simulation remain unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CT-001` | Dreamcast Arcade and Original choose different courses but share a rules menu; Arcade Rules alone permits delivered-fare time bonuses. | Confirmed | Direct | High | M1 printed pp. 5–6, 11 |
| `CT-002` | Direct steering, throttle, brake and Drive/Reverse sequences include Crazy Dash and Crazy Drift. | Confirmed | Direct | High | M1 pp. 2–4 |
| `CT-003` | A waiting customer is selected by a full taxi stop inside the pickup circle; the assigned destination has an arrow, distance cue and personal deadline. | Confirmed | Direct | High | M1 pp. 7, 9–10 |
| `CT-004` | Full stop inside the destination zone before personal expiry pays the fare; expiry makes the customer leave unpaid. | Confirmed | Direct | High | M1 pp. 7, 9–10 |
| `CT-005` | Base fare depends on distance, tricks add tips, leftover customer time adds a bonus fare, and a collision breaks the consecutive-tip combo. | Confirmed | Direct | High | M1 pp. 10–11 |
| `CT-006` | Under Arcade Rules, a delivered fare can add time to the overall game clock, and that clock reaching zero ends the score run. | Confirmed | Direct | High | M1 pp. 7–8, 11; R1 |
| `CT-007` | The exact original disc revision, options, physical road collision integration and numeric tip formula are not established by this packet. | Observation | Limited | High | M1; R1 |

## Basic data

- Release / origin: Sega's original Dreamcast manual identifies the product and distinguishes its arcade-derived course from the Dreamcast-specific Original course. The original arcade game preceded the Dreamcast port; no arcade cabinet revision is treated as evidence for Dreamcast option values.
- Platform or physical form: original Dreamcast disc, one player using the standard controller.
- Mechanical families: real-time system pressure (`FAM-010`). Its boundary covers intervention in a changing traffic system while the passenger and overall clocks limit decisions; a hostile enemy is not required.
- Sources accessed 2026-09-26:
  - **M1** — [Sega's original Dreamcast Crazy Taxi instruction manual, scanned](https://www.digitpress.com/library/manuals/dreamcast/crazy_taxi.pdf), printed pp. 2–11. Downloaded 21-page PDF, SHA-256 `c368607fd24ce9a448023345236486d3c84810545f41f5fb3c4ac4ccd8297c21`; printed pp. 6–11 were text-extracted, with fare pages visually inspected. This is a publisher-authored primary rules source, hosted as a scan by DigitPress, not a licensed play copy.
  - **R1** — [GameSpot's contemporary Dreamcast review](https://www.gamespot.com/reviews/crazy-taxi-review/1900-2540233/), corroborating the delivery-for-time loop. A review is not used for exact fare or control rules.
- Claim IDs: `CT-001`–`CT-007`.

## Mechanical decomposition

### Action Genes

- `ACT-290`: directly steer, accelerate, brake and shift the dedicated taxi. The manual's Crazy Dash and Crazy Drift are ordered input sequences within those controls; there is no finite boost stock to spend and no on-foot entry/exit action. A dash changes forward speed, while a drift sustains a sliding turn.
- Claim IDs: `CT-002`.

### System Behaviour Genes

- `SYS-320`: integrates taxi motion and road contact under steering, traction and collision. Vehicle damage or fuel is not inferred from the manual.
- `SYS-365`: populated road traffic supplies moving obstacles and vehicle collisions; generic witness/police escalation is not admitted.
- `SYS-1102`: after a chosen passenger boards, the game assigns a destination and customer clock. A timely full-stop arrival settles base fare plus accrued tips and remaining-time fare; personal expiry makes that passenger jump out unpaid, leaving the overall run active if its clock remains.
- `SYS-1103`: airborne jumps, close non-contact passes and sustained drifts add tips during a passenger trip. Successive tip events grow a combo and tip value; vehicle collision breaks its running count. Exact multiplier values are unknown.
- `SYS-1104`: only a successful delivery under `PLAY BY ARCADE RULES` converts the passenger's promptness into added overall run time. The manual lists Speedy +5 seconds, Normal +2, Slow no bonus and Bad for the unpaid departure; no such extension is assigned to fixed-duration modes.
- Resolution order: waiting customer and circle are visible → full-stop pickup boards them and reveals assignment/clock → driving motion and traffic continue → tricks may credit tips and collision may clear the combo → full-stop arrival before personal expiry settles fare and any run-clock extension; otherwise personal expiry ejects them unpaid → overall clock reaching zero displays the final result.
- Claim IDs: `CT-002`–`CT-007`.

### Constraint Genes

- `CON-700`: boarding or paid drop-off requires the taxi to be completely stopped inside the respective marked pickup or assigned destination zone. Passing through a circle at speed does not satisfy the transition; the destination zone's size and customer are parameters.
- `CON-701`: the passenger's own countdown gates that fare's payment independently of the overall run clock. Personal expiry loses that customer without itself ending the entire run; overall expiry closes the run even if money was already earned.
- Claim IDs: `CT-003`, `CT-004`, `CT-006`.

### Information Genes

- `INF-408`: customer icon colour gives relative trip distance and pickup-zone size gives difficulty; after pickup the HUD shows destination direction/distance, personal and overall timers, current and total fares, combo and time-bonus cues. The arrow indicates a general direction, not a guaranteed fastest road route.
- Claim IDs: `CT-003`, `CT-005`, `CT-006`.

### Objective and Time Genes

- `OBJ-002`: maximise total earned fare over the run, with delivered-customer count and cumulative earnings shown at its result. Class S is an evaluation, not a compulsory positive terminal.
- `TIM-003`: steer and choose passengers under continuously advancing traffic and overall clock; the game does not wait for turns. The manual says the game clock continues while a boarding or departing passenger disables control.
- Claim IDs: `CT-003`–`CT-006`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Several waiting customers show coloured icons and circles | Brake fully inside one chosen circle | That customer boards, receives a destination and begins their personal deadline; other customers were not a fixed next stage | choice plus legal pickup | `CT-003` |
| Taxi passes a destination marker without stopping | Continue driving | No paid drop-off is credited until a complete stop inside the assigned green zone | zone and rest predicate | `CT-004` |
| Customer aboard and personal time remains | Drift or pass closely without colliding | Tips and combo can rise while the base fare remains pending | manoeuvre scoring before settlement | `CT-005` |
| A tip combo is running | Collide with another car | Combo counter resets even though the run and passenger service continue | local risk and combo break | `CT-005` |
| Customer aboard and personal timer expires first | Continue toward the destination | Customer leaves without paying; overall taxi run can continue while its own timer remains | independent deadlines | `CT-004`, `CT-006` |
| Customer aboard and time remains | Stop inside assigned destination zone | Base fare, accrued tips and leftover-time fare credit; Arcade-rule promptness may add overall run seconds | paid settlement plus time extension | `CT-004`–`CT-006` |
| Overall game clock reaches zero | Read results | Run ends with customers delivered, earned total and class; no S threshold is mandatory | terminal evaluation | `CT-006` |

## Strategic and experiential structure

- Local decision: pick a visible customer's distance/difficulty trade-off, then choose a driving line that preserves both safety and earning opportunities.
- Medium-term planning: accept a longer fare only when its deadline and the remaining overall clock plausibly permit it; a quick delivery may buy more run time.
- Long-term structure: repeated fares accumulate money and customer count until the global clock stops the run.
- Common heuristics: use the general destination arrow as orientation, but learn road geometry; drift or pass traffic for tips only while preserving an on-time full-stop arrival.
- Failure attribution: a bad line or crash can reset the tip combo, missed arrival loses a fare, and spending too long at pickups consumes the global timer even with no active passenger.
- Player-trust factors: the two clocks, destination cue, fare and combo feedback expose why a trip succeeds or fails. Exact handling and numerical tip conversion were not measured.
- Claim IDs: `CT-002`–`CT-007`.

## Replay and variation

- Available customers, chosen order and traffic state can yield different observed routes; this record does not assert a random spawn distribution.
- Crazy Dash and drift are repeatable control techniques, not consumable powers; no finite stock is inferred.
- The chosen customer, driving line, trick sequence and arrival speed can change money and run length. The target is a better score rather than an authored mission exit.

## Adjacent systems and history

- *Mafia* (2002) also uses player-driven taxi fares, but its `The Running Man` route is an authored sequence of five designated fares followed by escape, not an unbounded selection-and-score loop. `SYS-708`, `CON-557` and `OBJ-132` must not be applied to Crazy Taxi.
- *Euro Truck Simulator 2* and *American Truck Simulator* settle employer cargo with damage, road law and parking; a Crazy Taxi passenger has a personal timer, accrued stunt tips and Arcade-rule time extension instead.
- The fixed three-, five- and ten-minute Crazy Taxi modes use the same course and service loop but explicitly omit the delivery time extension. Crazy Box has separate challenges.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-290` | steering, pedals, shift, Crazy Dash/Drift input timing |
| System Behaviour | `SYS-320`, `SYS-365`, `SYS-1102`, `SYS-1103`, `SYS-1104` | traction, traffic, fare value, combo, time award |
| Constraint | `CON-700`, `CON-701` | stop-zone geometry, passenger and run clock values |
| Information | `INF-408` | icon colour/zone size, arrow, earnings and clock layout |
| Objective | `OBJ-002` | session total money and class evaluation |
| Time | `TIM-003` | live road/clock progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `414` (`GAME-0001`–`GAME-0414`).
- Exact genome matches: none.
- Tied near matches: `GAME-0316` — Gran Turismo (`3 / 17 = 0.176471`).
- Supported combination subsets: none.
- Scan date: 2026-09-26.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0316` — Gran Turismo | `ACT-290`, `SYS-320`, `TIM-003` | Both directly control a dedicated road car under continuous vehicle motion. Gran Turismo's B-1 licence test requires one timed straight-line full stop for a medal; Crazy Taxi repeatedly chooses passengers, settles personally timed fares and earns trick tips plus more global run time from prompt deliveries. The shared car control does not make the goals or clock rules interchangeable. | Near, `0.176471` |

## Taxonomy impact

- [`TAXONOMY_CHANGE_153`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_153.md) admits `SYS-1102`, `SYS-1103`, `SYS-1104`, `CON-700`, `CON-701` and `INF-408`. No earlier game signature or verified combination changes.

## Negative results

- `SYS-708`, `CON-557` and `OBJ-132` rejected: Mafia's fixed five-fare, story-gated passenger chain is not the selectable open score service here.
- `ACT-201` rejected: no exit from or entry into an embodied world vehicle occurs inside this packet; `ACT-290` covers the dedicated cab.
- `CON-068` rejected: expiry ends a scored run with a class result, not an unsuccessful attempt at a fixed mandatory finish.
- `ACT-309` rejected: Crazy Dash is an input sequence, not expenditure of finite vehicle acceleration stock.
- Fixed-duration modes and Crazy Box excluded; their absence is not evidence that the Arcade-rule clock lacks extension.

## Delta summary

An available-customer fare loop, stunt-tip combo, two distinct deadlines and a delivery-for-more-time rule differentiate this score run from both scripted taxi missions and ordinary road races. Six new boundaries are admitted; vehicle control, motion, traffic, score objective and live time are reused.

## New facts

- [Confirmed | Direct | High] Sega's manual separates Arcade-rule time extension from fixed-duration modes (`CT-001`, `CT-006`).
- [Confirmed | Direct | High] A personal deadline can forfeit one unpaid fare without equating it to the overall game-over timer (`CT-004`, `CT-006`).

## New genes

- [Observation | Direct | High] `SYS-1102`–`SYS-1104`, `CON-700`–`CON-701` and `INF-408` isolate the fare, tip, deadline, zone and live guidance boundaries.

## New combinations

- [Observation | Limited | High] No new verified combination is asserted from this single game; proper-subset validation remains deterministic.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_153` documents six typed additions and the scripted-taxi reuse rejection.

## New questions

- What exact initial time, traffic difficulty and numerical tip multipliers appear on a known original Dreamcast disc with fixed options?
- What is the precise timing order if the personal and overall clocks reach zero in the same frame?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0416` *Advance Wars*, the next approved cross-platform unit, only after this one is validated and the Goal stop window elapses.
- Optimisation criterion: contrast continuous passenger service with turn-based tactical orders and terrain.
- Expected information gain: test whether existing tactical attack and capture genes transfer to one bounded GBA battle.
- Backlog impact: retain the remaining approved 416–432 order without starting a second game in this unit.

## Why this game

- [Hypothesis | Corroborated | Medium] A Dreamcast arcade-score service loop brings a passenger-selection and two-clock trade-off absent from the preceding Kinect body-contact activity while testing the scripted-taxi boundaries already in the corpus.
