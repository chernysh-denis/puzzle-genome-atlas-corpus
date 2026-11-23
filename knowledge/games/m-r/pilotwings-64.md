---
game_id: GAME-0602
slug: pilotwings-64
game_title: "Pilotwings 64"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-803
  system:
    - SYS-1772
    - SYS-1773
    - SYS-1774
  constraint:
    - CON-847
  information:
    - INF-565
  objective:
    - OBJ-326
  time:
    - TIM-003
---

# Game: Pilotwings 64

Comparison uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The island, pilot and point allocations belong to this flight test.

## Analysis scope

- Version / ruleset: the original English North American Nintendo 64
  cartridge, NUS-NPWE-USA. The US cartridge catalogue lists version
  1.0 and 29 September 1996. The US instruction booklet establishes
  controls and guideposts. The cartridge revision of sampled play
  was not independently authenticated.
- Structured analysis target: PLAT-NINTENDO-64 in
  `knowledge/platforms/games.json`. Nintendo’s later Switch Online
  announcement identifies the original launch game and legal modern
  availability. The Switch edition is not an observation of the cartridge.
- Primary decision loop: align the hang glider with the next ring,
  budget speed against altitude, then judge where to start and hold
  the landing flare. The result combines passed-ring credit and two
  separately displayed landing qualities.
- Entry and exit: at vehicle and class selection on a new file,
  choose Hang Glider, Beginner Class, an eligible pilot such as Ibis,
  and Albatross Nest, the sole test for this vehicle and class on
  Holiday Island. Review the briefing and start the airborne test.
  Stop at the settled result and return to the class grid.
- Included: pilot and test preparation, optional map before start,
  direct airborne navigation, speed and lift, ring credit, live
  instruments, landing flare and contact, grade and ordinary retry.
- Excluded: other tests, vehicles and classes, photographs, optional
  view changes, timing leaderboards, exact physics coefficients,
  other editions, completion of the full Beginner class and the full
  badge hierarchy across vehicles.
- Potential scoped modules: the Beginner Rocket Belt precision task,
  a timed higher-class glider test, or a deliberate ring omission
  with an otherwise valid landing.
- Direct-play status: no direct play. The original manual and sampled
  still frames establish the ordinary route and 96-point result.
  Published firsthand notes describe an early, short landing and a
  successful retry. The independent, pinned code reconstruction
  supplements boundary details. No cartridge boot, binary match,
  deliberately forced fault or video and audio playback was done.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PW-001 | The original US Nintendo 64 release is catalogued NUS-NPWE-USA, version 1.0, 29 September 1996. | Observation | Corroborated | High | P1, P2, H1. Capture hashes unavailable. |
| PW-002 | Hang Glider Beginner opens the sole test Albatross Nest on Holiday Island, with three rings, a pad and a 70-point bronze threshold. | Confirmed | Corroborated | High | P1 pp.6–9, H2, W1 0:30–0:40, W2 0:40 and 2:10. |
| PW-003 | Stick pitch trades speed and height in an unpowered glide; local rising air helps recover height. A/B supplies a held flare, and A near contact is the manual’s advice. | Confirmed | Corroborated | High | P1 pp.9–10 and 19, R1, H2, W1 0:40–1:20. |
| PW-004 | There are two normal yellow rings worth ten each and a red ring worth twenty. Ring passage consumes a ring's attempt credit; yellow and red lack the blue/white sequence mechanic. | Observation | Corroborated | High | P1 p.21, H2, R1, W1 1:00–1:10, W2 1:50 for the category total. |
| PW-005 | The instruments expose current speed, altitude, the relative direction and height of targets and marked thermal areas. Radar overlap with a thermal need not mean the pilot is at its height. | Confirmed | Corroborated | High | P1 pp.19–20, W1 0:40–1:20, W2 1:10–1:40. |
| PW-006 | Scored touchdown checks the designated surface and contact conditions. A low approach speed is useful, but does not by itself certify the target, flare or contact. Early braking can put the pilot down short. | Observation | Corroborated | High | P1 pp.10, 22, W1 1:20, W2 1:40–1:50, H3 minutes 2–4, R1. Exact native boundaries were not measured. |
| PW-007 | One completed Ibis run records 40/40 rings, 40/40 landing accuracy and 16/20 landing impact, totaling 96/100. No time category appears in that result. | Observation | Corroborated | High | W2 0:40, 1:40–1:50 and 2:10, H2, R1. |
| PW-008 | Beginner Hang Glider badges use 70, 80 and 90 for bronze, silver and gold. A successive graded attempt can replace a poor result; one cleared vehicle does not establish completion of all vehicles in the class. | Observation | Corroborated | High | P1 pp.6–7, H2, H3 minutes 2–5, W2 1:50–2:10. |

## Basic data

- Release / origin: Nintendo and Paradigm, Nintendo 64 launch title.
- Platform or physical form: original North American Nintendo 64
  cartridge, single player, N64 Controller.
- Puzzle family: physics and object manipulation (FAM-007). Where
  the wing reaches depends on speed, height, local air and contact.
  The test tracks elapsed time but its demonstrated grade rewards
  spatial sampling and touchdown rather than a deadline.
- P1: [Nintendo’s US instruction booklet](https://www.videogamemanual.com/n64/Pilotwings%2064%20%28USA%29.pdf),
  original first-party text mirrored as a scanned booklet. Printed
  pp.6–10 cover entry and piloting; pp.19–22 cover readouts and objects.
- P2: [Nintendo’s Pilotwings 64 overview](https://www.nintendo.com/us/whatsnew/nintendo-switch-online-expansion-pack-pilotwings-64-is-now-available/),
  confirms the 1996 origin and separately describes modern availability.
- H1: [US cartridge catalogue](https://www.nintendo64ever.com/Nintendo-64-Game,644,Pilotwings-64.html),
  the dated release, serial and version listing.
- H2: [CWall's player route, Hang Glider Beginner](https://gamefaqs.gamespot.com/n64/198292-pilotwings-64/faqs/24097),
  confirms the target, thresholds, weighted ring points and landing advice.
- H3: [Greg Noe’s firsthand session](https://firsthour.net/first-hour-review/pilotwings-64/),
  minutes 0–5 describe Ibis, an early flare ending short despite
  clearing all three rings, then a 94-point retry and gold.
- R1: [Pinned independent code reconstruction](https://github.com/n64decomp/pw64/tree/cb66cb2a3b093412285d381829c8ab7787660298),
  chiefly `hang_glider1.c` for flare input, `hang_glider2.c` for
  ground and pad contact, `rings.c` for passage and one-time points
  and `code_B2900.c` for score settlement. Reverse-engineered code
  corroborates causal boundaries without certifying an individual cartridge.
- W1: [English NTSC-attributed longplay](https://www.youtube.com/watch?v=mkTwxzdb7HY),
  0:30–1:30. Still frames show briefing transition, flight, ring
  acknowledgment, a successful pad contact and replay.
- W2: [Mutch Games’ Nintendo 64 run](https://www.youtube.com/watch?v=37-YJUZCD2Q),
  0:40–2:10. Still frames show Ibis, ring approach, touchdown,
  category settlement and return to the vehicle and class grid.
- Claim IDs: PW-001–PW-008.

### Reproducible route evidence

1. At vehicle and class selection, select Hang Glider on Beginner
   Class and Ibis as an eligible example. Open Albatross Nest on
   Holiday Island. The briefing allows a map and preflight reference
   for controls, scoring and hints. Use the map to see the start
   offshore, the route toward the island and the landing point.
   P1 pp.7, 9 and W2 0:40 ground the preparation. Start the test with A.
2. Take over the already airborne glider. Steer horizontally and
   ease the nose down to recover speed or up to gain a little height
   at a speed cost. Aim into a rising current when suitable. A thermal
   is a volume, so consult both radar and height. W1 0:40 already shows
   live flight and the current speed. P1 p.10 describes the input,
   and p.19 explains the distinct instrument cues.
3. Approach the three ring openings in the direction that leaves
   a workable approach to the ground target. W1 1:00 approaches a
   normal ring and 1:10 shows red spatial markers and the passage
   notice. Use both world position and radar. H2 reports two ten-point
   yellow rings and one twenty-point red ring. There is no blue/white
   sequence ring in this test. R1 shows passage geometry and retained
   state, so already registered credit does not repeat on a loop back.
4. Plan the final line toward the marked red-and-white pad while
   still keeping enough forward movement to reach it. Slow to a
   controllable approach. The booklet advises around or below
   50 km/h and A for putting the pilot’s legs down. Use held flare
   near the pad. W1 1:20 shows the pilot standing after a successful
   landing. H3 minutes 2–4 supplies the counterexample of an early
   flare settling short despite all three rings, followed by a better
   attempt. R1 uses both contact conditions and pad state rather
   than the scalar reading alone.
5. The W2 1:50 result displays 40/40 for Rings, 40/40 for
   Landing Accuracy, 16/20 for Landing Impact, and 96 total.
   This exceeds the 90-point gold threshold. The 2:10 grid marks
   Hang Glider in Beginner with a badge while the two other
   Beginner vehicles remain available and Class A is closed.
   Finish there. A replay of the graded result or selecting the
   test again belongs to this settlement, not the second test.

Claim IDs: PW-001–PW-008. Timestamps identify sampled evidence rather
than checkpoints to be reached at preset times.

## Mechanical decomposition

### Action Genes

- ACT-008: directly navigate the pilot and wing through the ring
  openings and down to the pad. Steering sets local motion.
- ACT-803: hold the flare to trade forward travel for slowing and
  prepare the pilot for ground contact. It can be initiated too early.
- Claim IDs: PW-003, PW-004, PW-006.

### System Behaviour Genes

- SYS-1772: the wing exchanges forward speed and height through
  pitch; local rising air can restore height without a motor.
- SYS-1773: an eligible ring crossing adds that ring's points once.
  Normal and bonus rings give different values.
- SYS-1774: the flight result measures ring points, landing accuracy
  and contact severity as separate contributions.
- Claim IDs: PW-003–PW-007.

### Constraint Genes

- CON-847: treat pad placement and actual touchdown conditions as
  separate from ring success. Landing short or making a hard contact
  can affect the result despite an excellent aerial line.
- Claim IDs: PW-006, PW-008.

### Information Genes

- INF-565: the HUD and radar expose speed, altitude, relative target
  height, heading and thermal areas. Passing a ring gives immediate
  acknowledgment.
- Claim IDs: PW-004, PW-005.

### Objective Genes

- OBJ-326: produce a settled scored flight. The Beginner threshold
  is 70 and higher thresholds reach silver at 80 and gold at 90.
- Claim IDs: PW-002, PW-007, PW-008.

### Time Genes

- TIM-003: the pilot can adjust throughout the continuously
  progressing glide. A delayed or early control can change the
  eventual contact state while the craft continues to advance.
- Claim IDs: PW-003, PW-005, PW-006.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| New-file vehicle and class grid | Select Hang Glider, Beginner, Ibis and Albatross Nest | Read the map or briefing, then start in flight | The mission has a specific entry and a bounded score | PW-002 |
| Airborne near the shore | Adjust pitch, turn or steer through lift | Speed and altitude change while the craft advances | Glide energy determines the route and approach | PW-003, PW-005 |
| In front of an eligible ring | Traverse its opening | Register its distinct value and show the acknowledgment | Ring credit is per passage and consumed once | PW-004 |
| Rings passed, pad still ahead | Refine descent and hold flare near the pad | Prepare the pilot's legs and slow before contact | The take-up point uses remaining distance as well as speed | PW-003, PW-006 |
| Flared approach intersects the pad | Make a controllable touchdown | Land and proceed to measured result | Surface and contact are distinct from airborne route credit | PW-006, PW-007 |
| Flare held too early, all rings already cleared | Descend short of the pad | The cited player's run lands short, then a retry scores 94 | Ring completion does not resolve the flight | PW-006, PW-008 |
| 96-point example on the results panel | Advance through results to the grid | Gold is retained for Beginner Hang Glider | The grade pertains to this vehicle and test | PW-007, PW-008 |

## Strategic and experiential structure

The route has two coupled decisions. Pitch and thermals determine
whether the pilot can reach the ring openings and still line up with
the pad. Flare placement turns a flyable line into a controlled stop
on the target. The centered contact in W2 gives full accuracy and
less than full impact. Cutting engine thrust is not part of this
unpowered approach. Claim IDs: PW-003–PW-007.

## Replay and variation

The test remains the same authored target on retry. Pilot handling
and the point of flare may vary. The firsthand retry and the second
scored trace show 94 and 96 as valid gold results without establishing
the exact formula. The documented score allocations do not establish
whether every missing-ring count can qualify for a badge or how
all invalid landings are scored. Claim IDs: PW-002, PW-006–PW-008.

## Adjacent systems and history

Published controls also cover a gyroplane, a rocket belt and other
glider tests with photography, ordered rings or time targets.
Those are separate loops. The Beginner stage timer is visible,
but no time category appears in its observed result. Class A
cannot be inferred merely from one vehicle badge. Claim IDs:
PW-001, PW-002, PW-007, PW-008.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-803 | Navigate, then flare for contact |
| System Behaviour | SYS-1772, SYS-1773, SYS-1774 | Live gliding, weighted ring credit and multi-part scoring |
| Constraint | CON-847 | Pad and controlled-touchdown eligibility |
| Information | INF-565 | Flight instruments, radar and ring feedback |
| Objective | OBJ-326 | Settle the route and landing into a grade |
| Time | TIM-003 | Direct input while gliding and descending |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `601` (`GAME-0001`–`GAME-0601`).
- Exact genome matches: none.
- Tied near matches: `GAME-0391` — Uncharted 2: Among Thieves (`2 / 12 = 0.166667`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| Uncharted 2: Among Thieves (GAME-0391) | ACT-008, TIM-003 | Both have direct navigation amid live progression. Nathan Drake moves through an authored climbing escape. Albatross Nest manages glider speed and altitude, one-time ring credit and the accuracy and impact of landing on a pad. | 2 shared of 12, Jaccard 0.166667 |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_348](../../../research/taxonomy-changes/TAXONOMY_CHANGE_348.md)
  records seven Active boundaries. Prior definitions remain stable.

## Negative results

- ACT-321 and SYS-556 describe powered, fixed-wing runway cycles.
  The observed glider starts airborne and has no throttle, rolling
  takeoff or wheel braking.
- ACT-680 requires deploying a gliding capability in the air.
  This pilot already enters under a deployed wing.
- CON-438 imposes ordered checkpoint and lap completion. It does
  not follow from the weights of two normal rings and one bonus ring.
- INF-424 and OBJ-133 have discipline-specific balance/gate and
  finish-time roles, respectively. Neither describes the flight
  instruments and separate touchdown qualities here.

## Delta summary

## New facts

- [Observation | Corroborated | High] Albatross Nest credits two
  ordinary rings and one more valuable bonus ring. PW-004.
- [Observation | Corroborated | High] Early flare can bring the pilot
  down short after all three rings, while a completed centered landing
  can still lose impact points. PW-006–PW-008.
- [Observation | Corroborated | High] The 96-point Ibis result
  splits 40, 40 and 16, then retains gold for this test. PW-007, PW-008.

## New genes

- [Observation | Corroborated | Medium] ACT-803, SYS-1772,
  SYS-1773, SYS-1774, CON-847, INF-565 and OBJ-326.

## New combinations

- [Observation | Direct | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_348.

## New questions

- What grade can a confirmed pad landing earn with each ring omitted?
- Does a borderline touchdown on the pad resolve differently for pilots?
- How does the retry path retain a previous badge after a worse run?

## Next recommended game

- [Hypothesis | Limited | Medium] Wheel World on the full Windows
  Steam release. Reconstruct one complete first cycle race under
  Selection 049.

## Why this game

- [Hypothesis | Limited | Medium] The bounded opening flight makes
  propulsion-free glide control, one-time target credit, pad eligibility
  and graded contact independently observable.
