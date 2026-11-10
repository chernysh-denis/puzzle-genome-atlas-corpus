---
game_id: GAME-0470
slug: burnout-3-takedown
game_title: "Burnout 3: Takedown"
analysis_status: reviewed
reviewed: 2026-10-01
combination_ids: []
gene_ids:
  action:
    - ACT-290
    - ACT-293
    - ACT-309
    - ACT-379
    - ACT-620
  system:
    - SYS-320
    - SYS-365
    - SYS-515
    - SYS-516
    - SYS-519
    - SYS-691
    - SYS-765
    - SYS-1225
    - SYS-1226
    - SYS-1227
  constraint:
    - CON-437
  information:
    - INF-205
    - INF-206
    - INF-446
  objective:
    - OBJ-134
  time:
    - TIM-003
---

# Game: Burnout 3: Takedown — first Silver Lake Race

Use the canonical [vocabulary and signature](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Compact model, two laps, boost amount and collision angle are parameters, not separate genes.

## Analysis scope

- Version / ruleset: original English 2004 PlayStation 2 base game, one-player World Tour's first available **Silver Lake Race** in the Compact series. This is not the Xbox control scheme, *Burnout Revenge*, *Burnout Paradise*, multiplayer or a whole campaign. Exact disc revision and region were not inspected.
- Structured analysis target: `PLAT-PLAYSTATION-2` in [platform coverage](../../platforms/games.json).
- Primary decision loop: select the available race and an eligible Compact car; steer, throttle and brake along the two-lap course against moving rivals and traffic; earn Boost from risky driving, decide when to spend it and when to ram a rival for a Takedown; after a self-crash, optionally steer the wreck in Impact Time toward a rival; regain racing control and reach the valid finish ahead of the field.
- Entry and exit: start with a fresh World Tour save at the first available Silver Lake Race and one of the offered Compact Type 1–3 cars. Begin at event/car commitment; stop after the two-lap classified finish and settled Gold first-place medal, or after a non-winning classified finish/abandonment. The analytical positive terminal is the first-place medal, not a fixed takedown quota. The guide reports additional events opening on completion; their play is outside this packet.
- Included: first event and Compact eligibility; directly controlled car,
  two-lap course, race rivals and road traffic; live collision;
  dangerous-driving Boost gains and manual spending; deliberate rival contact,
  Takedown, resulting gauge refill/extension; loss of an expanded gauge
  segment on an uncompensated crash and optional steerable wreck/Aftertouch
  Takedown; the original booklet describes segment retention after a
  successful race Aftertouch without specifying the atomic crash/reward order;
  course/position/Boost display; first-place result and retained medal.
- Excluded: Road Rage takedown target, Crash Mode score and Crashbreaker pick-ups, Face Off, Eliminator, Preview/Burning Lap time trial, Compact Grand Prix, later cars/tracks/unlocks as a decision loop, online or split-screen race, exact unverified collision coefficients, traffic patterns, opponent pace and reset timing. A Takedown here serves the race and Boost, not a Road Rage quota.
- Potential scoped modules: Road Rage, Crash Mode, Grand Prix and later race classes need their own packet and terminal evidence.
- Direct-play status: Direct play was not conducted. No PS2 game disc,
  console, executable, controller trace, gameplay screenshot, gameplay video
  or audio was inspected. This is a documentary reconstruction from the
  original PS2 instruction booklet, Criterion's own history and contemporary
  written routes. The illustration is original interpretive art, not a
  captured frame. During P5, direct booklet fetches returned 403; that is not
  a check of present availability. During P7, the previously archived original
  PS2 booklet spreads were hash-verified and visually reinspected at printed
  pages 2–3 and 6–7; the public manual web-reader text and Criterion page were
  read again. No native disc revision, matched success/failure trace, exact
  refill fraction or crash/reward ordering was established. The documented
  segment-retention qualification does not settle whether SYS-1227 is
  independently justified or composed from retained rules.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `B3-001` | The PS2 manual assigns direct steering, throttle, brake, R1 Boost and crash-only Impact Time controls. | Confirmed | Direct | High | P1 |
| `B3-002` | Dangerous driving fills Boost; a Takedown contributes more Boost. | Confirmed | Corroborated | High | P1, P2 |
| `B3-003` | The first World Tour Silver Lake Race is a two-lap Compact-car event; first place earns Gold. | Observation | Corroborated | Medium | S1, S2 |
| `B3-004` | A qualifying Takedown fills and can extend bounded temporary Boost; an uncompensated crash loses an expanded segment. The PS2 booklet describes successful race Aftertouch retaining a segment; exact update order and cap/minimum edge cases remain unmeasured. Its documented four-segment maximum is not a newly executed native measurement. | Observation | Limited | Medium | P1 original booklet; S1 |
| `B3-005` | During a crash, Impact Time lets the player direct the wreck into a rival for an Aftertouch Takedown. | Observation | Corroborated | Medium | P1, S1 |
| `B3-006` | Exact original-PS2 collision coefficients, car handling, traffic seeds, rival recovery and crash reset frames are not measured here. | Observation | Limited | High | Documentary boundary |

## Basic data

- Release / origin: Criterion Games and Electronic Arts, 2004 original PS2 *Burnout 3: Takedown*.
- Platform or physical form: original PS2 World Tour single-player, first Silver Lake Race with an offered Compact car. No claim about every licensed platform or edition.
- Mechanical families: `FAM-007` physics/object manipulation for momentum and deliberate collision; `FAM-010` real-time system pressure for live rivals, traffic, Boost decisions and racing position.
- **P1:** Electronic Arts original PlayStation 2 instruction booklet: [original-page rendering](https://manualmachine.com/gamesps2/burnout3takedown/1116322-user-manual/) and the [earlier preserved text/PDF mirror](https://manuals.plus/m/bc816e0d9c3ac412d64e9fb5376be34e519274dbdc88a0fe583820d8cc2d5c70), originally accessed 2026-10-01. Original scans archived before P7 were hash-verified and visually reread at printed pages 2–3 and 6–7 for controls, Boost, ordinary Takedowns and race Aftertouch segment retention. The earlier host's conversion summarises rather than exposes every scanned page; its summary is not substituted for the original pages or an identified executable. The booklet's capacity wording remains documentary, not a newly executed native measurement.
- **P2:** [Criterion Games' Burnout 3 retrospective](https://www.ea.com/ea-studios/criterion-games/games), developer/publisher account that dangerous driving grants Boost and Takedowns steal rival Boost; accessed 2026-10-01.
- **S1:** [Contemporary PS2-labelled Burnout 3 written route](https://gamefaqs.gamespot.com/ps2/919649-burnout-3-takedown/faqs/34370), sections 017–022: Silverlake Race, Compact eligibility, two laps, Boost segments, Aftertouch; accessed 2026-10-01. The route also describes Xbox buttons, so only event/rule claims corroborated elsewhere are adopted; PS2 buttons come solely from P1.
- **S2:** [Independent PS2 driving guide](https://gamefaqs.gamespot.com/ps2/919649-burnout-3-takedown/faqs/44255), medal placement and first-course context; accessed 2026-10-01.

## Mechanical decomposition

### Action Genes

- `ACT-293` selects the available World Tour event; `ACT-290` steers, accelerates and brakes the chosen dedicated Compact car. `ACT-309` spends a finite Boost reserve while driving; `ACT-379` deliberately aims vehicle contact at a rival rather than treating traffic contact as an attack.
- New `ACT-620` covers crash-only Impact Time steering of one's wreck toward a rival; normal vehicle control has ceased during this brief state. No exact frame window is asserted.

### System Behaviour Genes

- Reuse `SYS-320` for driven-car motion and collision, `SYS-365` for road traffic, `SYS-515` for a shared-course autonomous rival field, `SYS-516` for lap/finish order, and `SYS-519` for settled medal state. The first event's default opponent profile is not a measured difficulty curve.
- Reuse `SYS-765` for near-miss, drift and oncoming contributions to Boost and `SYS-691` for spending it on acceleration.
- New `SYS-1225` resolves a deliberate rival-car contact that actually wrecks the rival into a counted Takedown, without requiring a Road Rage quota or permanent rival removal. New `SYS-1226` refills or extends bounded temporary Boost after a qualifying Takedown and removes an expanded segment on an uncompensated crash. The original PS2 booklet describes successful race Aftertouch retaining that segment, without identifying skipped loss, cancellation, debit/reward order or exact resulting charge. New `SYS-1227` resolves directed wreck movement during Impact Time and an optional Aftertouch Takedown against a rival; it does not turn ordinary racing into Crash Mode scoring.

### Constraint Genes

- Reuse `CON-437`: this opening race admits the listed Compact types. A later class or unrestricted garage is not silently available. Boost charge and the four-segment cap are system state, not an invented pickup-pad gate.

### Information Genes

- Reuse `INF-206` for event identity, car eligibility and disclosed route before launch; `INF-205` for live place, lap and rival cues.
- New `INF-446` for the live segmented Boost bar and immediate Takedown/crash feedback. It does not expose future traffic or guarantee a safe collision.

### Objective Genes

- Reuse `OBJ-134`: win one finite rival Race and retain its first-place medal. A non-Gold completion may open later content, but is not this packet's positive terminal.

### Time Genes

- Reuse `TIM-003`: rivals, traffic, driving state and Boost decisions advance in real time.

## Reproducible transitions

| Before | Input or event | Source-derived resolution | Boundary | Claim |
|---|---|---|---|---|
| First World Tour event available | Select Silver Lake Race with an offered Compact car | The two-lap race begins with a competitive field | Not a freely chosen later class | `B3-003` |
| Boost below its current cap | Pass traffic closely, drift or take an oncoming line | Eligible dangerous driving adds charge | Risk and gain share a moving road | `B3-002` |
| Boost charge positive | Hold R1 while steering | Reserve is spent for acceleration until release or depletion | Throttle alone does not spend Boost | `B3-001`, `B3-002` |
| Rival beside a road barrier | Deliberately angle a contact | If the impact actually wrecks an eligible rival, register a Takedown with the documented refill and bounded-capacity response; a capacity increase is not guaranteed at the cap | Mere rubbing contact is not automatically a Takedown | `B3-002`, `B3-004` |
| Player car crashes | Hold R1 and steer the wreck during Impact Time | Direction may change; only an actual eligible rival wreck can yield Aftertouch Takedown. The booklet describes successful race Aftertouch segment retention without specifying atomic loss/reward order | Entry alone guarantees no Takedown; Crash Mode pickups and Crashbreaker stay excluded | `B3-004`, `B3-005` |
| Player crashes without a compensating Takedown and has an expanded segment available | Inspect the branch’s resulting Boost bar | Documentary uncompensated loss; successful race Aftertouch retention is a separate documented branch | Exact intermediate order, charge and cap/minimum behavior remain unmeasured | `B3-004`, `B3-006` |
| Two valid laps completed ahead of rivals | Cross finish and settle result | Gold first-place medal is retained | A Takedown count alone is not victory | `B3-003` |

These transitions are source-derived, not an executed local trace.

## Strategic and experiential structure

- Dangerous driving earns speed reserve while increasing collision risk. A qualifying rival Takedown can refill and extend the bounded reserve; an uncompensated crash loses an expanded segment. Successful race Aftertouch can preserve a segment according to the booklet, without proving the atomic sequence. A line toward a rival still competes with the fastest clean line around the bend.
- Aftertouch leaves the player in a crashed-car state and offers a short secondary steering opportunity. An actual eligible rival wreck may be recognised as an Aftertouch Takedown and preserve a Boost segment as described by the booklet; this does not prove an independent irreducible system beyond ACT-620, SYS-320 and SYS-1225. Exact window, reset and resource-update order remain unmeasured.
- Failure attribution is partly local: a wall impact, spent Boost and lost position are visible; rival pace and traffic pattern are not claimed to be fully predictable.

## Replay and variation

- Compact choice, overtaking line, rival contact, traffic near-misses and Boost timing can change a run. No random seed, AI model or exact opponent catch-up rule was inspected.

## Adjacent systems and history

- *Burnout Paradise*'s analysed Race is an open-city point-to-point event with route freedom; this packet is a closed two-lap Silver Lake course with Takedown-driven segmented Boost and post-crash Aftertouch.
- *Need for Speed Payback* shares deliberate vehicle ramming but makes hostile wrecks a heist-stage quota; the Silver Lake race uses Takedowns to change racing resources rather than advance a carrier-heist stage.
- Do not import *Burnout Revenge*'s Traffic Attack or later traffic-checking rule.

## Normalised genome

| Type | Active gene IDs | Boundary |
|---|---|---|
| Action | `ACT-290`, `ACT-293`, `ACT-309`, `ACT-379`, `ACT-620` | drive, choose, boost, ram, steer wreck |
| System Behaviour | `SYS-320`, `SYS-365`, `SYS-515`, `SYS-516`, `SYS-519`, `SYS-691`, `SYS-765`, `SYS-1225`, `SYS-1226`, `SYS-1227` | road/rivals/laps/result and Boost–Takedown–Aftertouch consequences |
| Constraint | `CON-437` | eligible Compact entry |
| Information | `INF-205`, `INF-206`, `INF-446` | race, event and Boost state |
| Objective | `OBJ-134` | first-place retained medal |
| Time | `TIM-003` | continuous live race |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `469` (`GAME-0001`–`GAME-0469`).
- Exact genome matches: none.
- Tied near matches: `GAME-0199` — Need for Speed Unbound (`14 / 32 = 0.437500`).
- Supported combination subsets: none.
- Scan date: 2026-10-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0199` — Need for Speed Unbound | `ACT-290`, `ACT-293`, `ACT-309`, `SYS-320`, `SYS-365`, `SYS-515`, `SYS-516`, `SYS-519`, `SYS-691`, `SYS-765`, `CON-437`, `INF-205`, `INF-206`, `TIM-003` | Both begin a car event with moving traffic and rivals, charge a finite speed reserve through driving technique, spend it, then settle an ordered race. Unbound's analysed Story race continues into police Heat and garage-gated reward; Burnout 3's first Silver Lake Race instead rewards destructive rival contact with temporary Boost capacity, lets the player guide a crashed wreck and closes on the two-lap Gold result without a pursuit. | Tied near, `14 / 32 = 0.437500` |

### Preserved research notes

- New genes: `ACT-620`, `SYS-1225`, `SYS-1226`, `SYS-1227`, `INF-446`.
- Classification result: five new bounded crash/Boost information and response genes, with sixteen reviewed reuses.
- Evidence and reasoning: existing race, direct-car and reserve-spend boundaries transfer; deliberate rival wreck and crash-conditional wreck steering require their own causal response.

## Taxonomy impact

- Registry changes: five new Active definitions; no earlier game signature or verified combination change.
- Taxonomy-change record: [`TAXONOMY_CHANGE_207`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_207.md).

## Negative results

- No PS2 direct play; no claim about exact traffic patterns, AI catch-up, post-crash reset frames or unobserved edition constants.

## Delta summary

## New facts

- [Observation | Corroborated | Medium] The first Silver Lake Race connects risky driving, rival wrecks and a segmented Boost reserve within one two-lap first-place attempt (`B3-002`–`B3-005`).

## New genes

- [Observation | Corroborated | Medium] Five new boundaries isolate wreck steering, Takedown recognition, Boost-segment response, Aftertouch resolution and visible Boost feedback.

## New combinations

- [Observation | Direct | High] No verified combination subset claimed after deterministic scan.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_207` adds five definitions, without migrating earlier signatures.

## New questions

- A captured original PS2 run could measure exact Boost refill/decay, rival return, crash reset and event-specific AI behaviour.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0471` *Trauma Center: Under the Knife*, original Nintendo DS. Its touch-surgery packet should test timed procedure and patient-vital boundaries rather than repeat a car or Nintendo racing loop.
- Optimisation criterion: platform and control-method diversity in this recorded horizon.
- Expected information gain: stylus operations, procedural order and critical patient state.
- Backlog impact: none; follow the approved order.

## Why this game

- [Hypothesis | Limited | Medium] Burnout 3 supplies original-PS2 aggressive racing and crash steering absent from the previous Windows RTS unit, while the next DS unit changes both platform and control method.
