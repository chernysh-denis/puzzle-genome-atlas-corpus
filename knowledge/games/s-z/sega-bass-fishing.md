---
game_id: GAME-0598
slug: sega-bass-fishing
game_title: "Sega Bass Fishing"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-199
    - ACT-794
    - ACT-795
    - ACT-796
  system:
    - SYS-1759
    - SYS-1760
    - SYS-1761
  constraint:
    - CON-068
  information:
    - INF-561
  objective:
    - OBJ-324
  time:
    - TIM-003
---

# Game: Sega Bass Fishing

Vocabulary and comparison follow the [canonical architecture](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Shown weights,
time awards and controller bindings are instance parameters.

## Analysis scope

- Version / ruleset: Full 1999 North American Dreamcast release,
  original Sega of America product 51006, English, Arcade Mode,
  first Lodge area on Lake Paradise. The US capture uses original
  Dreamcast hardware with an optical-drive substitute. The 51006
  printed manual identifies the retail product. Exact disc revision,
  original-disc provenance in that capture and setting names beyond
  observed initial values are unverified. Report the year rather
  than choosing between late-September and early-October catalogue dates.
- Structured analysis target: PLAT-DREAMCAST, recorded separately in
  `knowledge/platforms/games.json`. This review covers
  the home-port Arcade Mode. Arcade board parity is unverified.
- Primary decision loop: choose a lure by its indicated depth and
  handling, place the cast point near likely fish, cast and work
  the lure. Strike on a bite. Independently vary reeling and rod
  direction to shorten the tether without breaking it. Add settled
  catch weight until it meets the Lodge norm within the clock.
- Entry and exit: start Arcade Mode without a continued credit and
  reach the opening Lodge lure and cast controls. For the reference
  run expect 2:00, zero catch weight and a 9 lb clear norm. Select
  and confirm an offered lure or retain the opening choice, then cast
  toward the Lodge front with the standard controller. End at Lodge
  Area Clear and the handoff to Cape before another cast, or at the
  Lodge Time Up boundary without taking the continue. The initial
  clock and norm are configurable, as documented in the booklet.
- Included: opening lure choice and placement, live underwater
  retrieval, approach, bite, hook, post-hook fight with its own
  failure edge, separate time awards, catch weight and rank, area
  progress and the clock failure. Standard controller with normal
  vertical rod controls is the documented reproduction setting.
- Excluded: switchable hardware bindings, save format and records,
  continues beyond Time Up, later areas, lure unlocks, Original
  Tournament and Practice Mode, the 1997 arcade hardware, other
  regions, ports and the sequel. No complete lure list or game
  physics coefficients are implied.
- Potential scoped modules: first Original Mode amateur session
  through its standings, an entire Arcade campaign to the bonus
  area, and input-equivalence testing for the physical rod.
- Direct-play status: no direct play. Read the North American Sega
  manual and inspected muted static storyboards from one labelled
  US Dreamcast run and one separately reported Dreamcast GD-ROM
  playthrough. No audio or motion playback, input injection, disc
  acquisition or binary inspection. The physical playthrough
  provides mechanical corroboration at a different displayed norm
  and does not identify the exact disc region.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| BF-001 | Sega sold the first game as English Dreamcast product 51006 in 1999. The day differs between later entries. | Observation | Direct | High | M1 front cover and copyright. P1 and P2 disagree on the calendar day. |
| BF-002 | Lodge opens the reference run with zero tally and 2:00, exposes the cast point and has selectable lure properties. Time and first norm are configurable. | Confirmed | Corroborated | High | M1 pp. 5, 8–9, 15. W1 0:15–0:25. W2 1:20–1:40. |
| BF-003 | A cast puts the lure in reachable water on a line. Reeling and rod movement work it before any hook, and a fish can approach and bite. | Confirmed | Corroborated | High | M1 pp. 6, 8–10. W1 0:20–0:30. W2 1:30–1:50. |
| BF-004 | The default downward hook input after the bite opens the fight, and Arcade adds a distinct hit-time award without yet crediting weight. | Confirmed | Corroborated | High | M1 pp. 6, 10. W1 0:30–0:35. W2 3:10–3:20. |
| BF-005 | Reeling and steering a connected rod govern retrieval and line strain. Red warns of excessive strain; correction can save the catch and uncorrected trouble can break the line. | Observation | Corroborated | High | M1 pp. 10–11. W1 0:30–0:45 and W2 1:50–2:20, 3:20–3:40 support the changing gauge. The break rule is from M1. |
| BF-006 | A landed fish is weighed, ranked and included in the area tally, with a separate weight-related time award. The displayed landing award can be zero. | Confirmed | Corroborated | High | M1 pp. 5 and 11. W1 0:45–0:50. W2 2:20–2:30, 3:00–3:10, 3:50. |
| BF-007 | The manual sets an at-least-weight clear rule and a countdown expiry. W1 shows first-catch clear; W2 shows several settlements and Cape. | Observation | Corroborated | High | M1 pp. 5, 11–12, 15. W1 0:45–1:00. W2 2:30–4:00. |
| BF-008 | Timing durations and internal weight, bite and strain math remain unresolved. The frame samples best establish phases and changes of displayed values. | Observation | Limited | Medium | W1, W2 static sampling plus document granularity. |

## Basic data

- Release / origin: SIMS's Sega Dreamcast home adaptation of Sega's
  earlier arcade fishing game. North American retail target, 1999.
- Platform or physical form: one player on Dreamcast. Sega
  documents standard gamepad and optional Fishing Controller on
  pp. 6–7. Only gamepad reproduction is specified here.
- Puzzle family: real-time system pressure (FAM-010). Before and
  after a bite, the fish moves and the area timer runs while the player
  chooses, adjusts and reacts.
- M1: [Sega of America 51006 instruction booklet](https://segaretro.org/images/archive/9/9b/20241126204842%21SegaBassFishing_DC_US_Manual.pdf)
  with [readable mirror](https://manualzz.com/doc/24682270/sega-bass-fishing-instruction-manual).
  Inspected the cover and printed pp. 6–12 and 15 in the archival scan.
- W1: [Yoffer's US Dreamcast run](https://www.youtube.com/watch?v=Oiv60--eZiI); [submission and
  configuration](https://www.speedrun.com/sega_bass_fishing/runs/y6q4gn1z).
  Author identifies US Dreamcast hardware and GDEMU. Read the
  first Lodge segment as stills, spaced five seconds apart.
- W2: [G4EVER's Dreamcast GD-ROM trace](https://www.youtube.com/watch?v=EWTJ-tOrqfk). Original hardware and
  disc are the player's report. Selected first-area stills use
  ten-second spacing. Do not transfer its starting target to W1.
- P1: [1999 boxed product and October 6 entry](https://gamefaqs.gamespot.com/dreamcast/198570-sega-bass-fishing/data).
  P2: [September 30 catalogue entry](https://www.timeextension.com/games/dreamcast/sega_bass_fishing).
  Neither independently establishes the exact release day.
- Claim IDs: BF-001, BF-002, BF-007, BF-008.

### Reproducible route evidence

1. Enter Arcade and wait for the opening at Lodge. W1 0:15
   has 2:00 and a zero total. At 0:25 the camera shows the green
   lure in the water and 32 ft of line out with 1:50 remaining.
   The setup menu identifies depth and use; it does not expose a
   deterministic catch forecast. The exact lure label is not
   readable in W1's opening frames.
2. With normal rod controls, press A to cast at the currently
   selected point. Work the lure using either trigger and the
   analogue stick. Take the downward hook action at the bite.
   W1 0:30 shows the bass and an active green strain meter;
   at 0:35 the time reads 1:46 after 1:45 five wall seconds
   earlier and the hooked fish still has zero credited weight.
   W2 3:20 directly shows Hit Bonus 4 sec with the old total
   still on screen. The manual assigns this event to hooking.
3. Shorten line while following the current pull and strain. Red
   at W1 0:35 and 0:40 precedes the same fish being lifted at
   0:45. Red is a warning from which the player can recover.
   Restrain winding and adjust the rod while the fish is still
   attached. The booklet identifies red, possible line break
   and on-screen rod commands. Its manual branch for a missed
   bite describes escape before this contest even begins.
4. Observe the lift and result before casting again. W1 at
   0:45 has Line Out 0 ft with the tally still zero in the
   lifting animation; at 0:50 it shows Lodge Area Clear with
   the fish displayed. The next location is live by 1:00.
   W2 at 2:30 shows a settled 5 lb 07 oz total and Time Bonus
   0 sec, below its shown 11 lb norm. Later frames show a
   second settlement and another fish being weighed at 3:50,
   with Cape by 4:00. The sampled display is mid-update at
   3:50. The observed partial totals and weight labels do not
   prove exact arithmetic for that transition.

Use the documented state order to reproduce a catch. The
annotations do not promise the same fish at the same frame
or enough weight from the first fish on a fresh attempt.
Claim IDs: BF-002–BF-008.

## Mechanical decomposition

### Action Genes

- ACT-199: select an available lure to replace the one used on the
  rod. The selected lure remains the single active choice for
  casting. Press Y to open lure selection while ready to cast,
  choose and confirm with A. This is a loadout change; its
  in-water effects are resolved separately.
- ACT-794: move the cast indicator and then commit the tethered
  lure with A. It remains controlled after delivery.
- ACT-795: make the distinct hook-setting input after the bite.
  With normal controls the analogue stick goes down; the
  reversal setting changes that binding, not the rule.
- ACT-796: wind and manipulate the rod independently to work the
  lure or deal with a hooked fish. Use either trigger for winding
  and steer with the stick. Release winding when necessary.
- Claim IDs: BF-002–BF-005.

### System Behaviour Genes

- SYS-1759: eligible fish can close on the moving lure, bite and
  expose a brief strike opportunity. A miss can lose that fish.
- SYS-1760: a hooked fish now pulls on the tether. Winding and
  the rod affect retrieval and strain. Take corrective action
  or risk a break. A successful fight leads to landing, with
  settlement separate from both the initial hook and the instant
  the displayed Line Out reaches zero in the lift animation.
- SYS-1761: Arcade can increase remaining time at two distinct
  events. Hooking yields Hit Bonus. The separate Time Bonus is
  resolved after landing in relation to catch weight and can be
  zero. Only the second event has a landed fish to credit.
- Claim IDs: BF-003–BF-008.

### Constraint Genes

- CON-068: live remaining time constrains the current Lodge attempt,
  with explicitly earned time additions. Exhausting it without
  clearing ends the scoped attempt. Continuing the credit is beyond
  the exit. The tie order at zero with a simultaneous hook or
  landing was not tested.
- Claim IDs: BF-004, BF-006, BF-007, BF-008.

### Information Genes

- INF-561: Line Out and the tension display are separate. Read
  both alongside the fish's pull and contextual warnings. The
  right-edge gauge makes a threatened break distinguishable
  from measured progress toward the boat.
- The lure menu exposes depth and operation hints. Visible local
  shadows and a closer view of the lure help choose a working
  route. The stage HUD shows the tally and its clear norm.
  Frame sampling cannot reveal unseen spawn states.
- Claim IDs: BF-002, BF-003, BF-005, BF-007, BF-008.

### Objective Genes

- OBJ-324: land bass until their combined credited weight meets
  the local clear norm before the timer expires. A hooked fish
  contributes nothing until settled. An individual size rank is
  feedback and does not replace the area tally.
- Claim IDs: BF-004, BF-006, BF-007.

### Time Genes

- TIM-003: the countdown and fish continue in real time while
  the player casts, works the lure, strikes and steers. Input
  cannot be treated as blocking turns. Exact reel input rate,
  bite duration and presentation pauses were not measured.
- Claim IDs: BF-002–BF-008.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Live surface view; no deployed lure | Select the offered lure, reposition left/right and press A | Lure enters the water on a line at the chosen point | Loadout, aim and cast are separate commitments | BF-002, BF-003 |
| Unhooked lure in the water | Reel intermittently and steer | The player can work the lure while a bass approaches; the approach alone yields no catch | One may reel before any hook | BF-003 |
| Bass takes the lure | Pull the stick down under normal controls | Accepted hook begins the fight and can extend the Arcade clock | Attachment differs from settlement | BF-004 |
| Hook opportunity still live | Miss the strike | The manual reports escape without a held catch | Bite alone is insufficient | BF-004 |
| Hooked; strain rises toward red | Release winding and correct rod direction | Strain can fall; ignoring warnings can break the line | Red can be recoverable, with no verified numeric break threshold | BF-005 |
| Attached fish nears the boat | Complete retrieval | Lift and catch settlement expose rank and weight; possible landing-time award | The tally changes after attachment and fighting | BF-006 |
| Settled tally below norm | Return to the next cast with time remaining | Previously credited weight still contributes to the area | Multiple landed weights can count | BF-006, BF-007 |
| New settled weight reaches or clears the norm | Observe the clear and transition | Lodge ends; next area is Cape in the traces | Area progress is a total-weight threshold | BF-007 |
| Unfinished at zero | Allow the clock to expire | Time Up ends normal Lodge control; taking Continue is outside scope | Authoritative local failure edge | BF-007, BF-008 |

## Strategic and experiential structure

Casting toward a visible shadow and choosing an appropriate lure
trade search time against a possible bite. Reeling can help obtain
one, yet winding without regard for strain after the hook risks
losing a catch already being fought. The tension gauge gives
specific corrective feedback. Extending the clock at a hook is
compatible with losing the attached fish before weight is credited.
An adequate landed fish ends area decisions even with time left.
Claim IDs: BF-002–BF-007.

## Replay and variation

The option menu exposes difficulty, time and first norm. The reviewed
traces present different norms and take different numbers of catches.
Depth, fish response and lure choice can vary the route. The available
evidence does not describe seeding, deterministic respawns, the
conversion of weight to seconds, exact line-strain math or ties near
expiry. Claim IDs: BF-002, BF-003, BF-006–BF-008.

## Adjacent systems and history

The same booklet describes a separate Dreamcast tournament mode,
with standings and later tournament eligibility, and timed play
differs from the Practice configuration. The sequel's landing
meter requires its own evidence and must not be imported here.
Related visual subjects like shoreline collecting can share a rod
without sharing a post-hook pressure or cumulative-weight rule.
Claim IDs: BF-001, BF-005–BF-008.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-199, ACT-794, ACT-795, ACT-796 | Equip lure, aim and cast, hook, then work the rod and reel |
| System Behaviour | SYS-1759, SYS-1760, SYS-1761 | Approach and bite, line strain and separate time awards |
| Constraint | CON-068 | A live authoritative deadline |
| Information | INF-561 | Separate progress and tether condition |
| Objective | OBJ-324 | Minimum settled catch weight |
| Time | TIM-003 | Live decisions during forced progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `597` (`GAME-0001`–`GAME-0597`).
- Exact genome matches: none.
- Tied near matches: `GAME-0376` — Katamari Damacy REROLL (`2 / 17 = 0.117647`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| GAME-0376 Katamari Damacy REROLL | CON-068, TIM-003 | Both allow continuous decisions under an authoritative clock. Katamari clears by growing a rolling body through contact collection; Lodge clears on cumulative landed mass after a separate lure, strike and tether fight. | 2 shared of 17, Jaccard 0.117647 |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_344](../../../research/taxonomy-changes/TAXONOMY_CHANGE_344.md)
  adds eight boundaries. Earlier signatures remain intact.

## Negative results

- ACT-476 and SYS-1444 do not express this active lure-and-hook
  sequence. Their authored examples depend on waiting through
  passive contact cues and successful reeling after a bite.
  The separate hook motion, active lure control and line fight
  establish different causal steps.
- SYS-1556 and SYS-1204 award time for a pickup or course
  checkpoint. This stage awards time at fishing events while
  its current locality remains live.
- A sample at zero line out does not prove weight settlement,
  and a red gauge does not equal immediate breakage.

## Delta summary

## New facts

- [Confirmed | Corroborated | High] A separate hook may extend
  Arcade time before the bass earns any stage weight. BF-004.
- [Observation | Corroborated | High] Strain and line length
  vary independently while hooked. Catch credit appears after
  retrieval and lift. BF-005, BF-006.

## New genes

- [Observation | Corroborated | Medium] ACT-794–ACT-796,
  SYS-1759–SYS-1761, INF-561 and OBJ-324.

## New combinations

- [Observation | Direct | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_344.

## New questions

- What delay or grace governs hook timing and strain breakage
  in this exact NTSC-U revision?
- How do resolved weight, tally animation and landing time
  awards account for the values sampled around the physical
  trace's third landing?

## Next recommended game

- [Hypothesis | Limited | Medium] Sword of the Sea on PlayStation 5
  under Selection 049.
- The board's momentum, route choice and environmental renovation
  contrast with managing the deployed lure and tethered fish.

## Why this game

- [Hypothesis | Limited | Medium] A timer extended by a provisional
  hook is a distinct use of resource credit before the principal
  objective has settled. The explicit line strain gives a
  source-backed midpoint between cast and weight tally.
