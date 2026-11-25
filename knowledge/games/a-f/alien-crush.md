---
game_id: GAME-0704
slug: alien-crush
game_title: "Alien Crush"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-895
    - ACT-896
    - ACT-921
  system:
    - SYS-146
    - SYS-1983
  constraint:
    - CON-894
  information:
    - INF-642
  objective:
    - OBJ-002
  time:
    - TIM-003
---

# Game: Alien Crush

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Launch a pinball from the lower lane and keep it moving with the flippers.
Pass through four upper gates to qualify a bonus, then route the same
ball into the separate lock to claim it.

## Analysis scope

- Version / ruleset: the original English North American NEC
  TurboGrafx-16 TurboChip, TGX020005, 1989. Solo main-table rules.
  Use the original English booklet and capture material showing the
  NEC title. Exact cartridge bytes and input hardware are unverified.
- Structured analysis target: PLAT-TURBOGRAFX-16 in
  [platform coverage](../../platforms/games.json).
- Entry: the initial stationary silver ball in the right-hand plunger
  lane on the lower main field, before the first upward serve.
- Primary decision loop: set the launch strength with the plunger, then
  time the active side's flippers against the moving ball. Route it
  through the upper gates while tracking the separate lamps. When the
  set qualifies and the Tentacloid Lock accepts, send the ball into
  that receiver for the upper-table bonus.
- Positive terminal: observe the `BONUS` display settle and the
  same ball move on the upper main field with cleared upper lamps.
  Stop before any separate bonus room.
- Included: plunger, flipper redirection, documented table nudge,
  continuous ball motion, lower-to-upper handoff, gate lamps, lock
  qualification, pending bonus and its same-field settlement.
- Excluded: the lower target bonus, actual drain and its stock
  settlement, all four bonus-room routes and perfect outcomes, score
  cap, the post-last-ball number match, score entry and later editions.
  The manual documents bottom drain as a risk to the scoped ball.
- Potential scoped module: start with one known ball-speed setting
  and trace the first lower-field drain into the next serve.
- Direct-play status: no personal TurboGrafx-16 run, input telemetry
  or cartridge inspection. The English booklet documents control,
  threshold and release rules. Two independent recordings were
  inspected as short silent frame sequences. The actual press duration,
  ball-speed setting in the reference run and contact coordinates
  are not recoverable from those frames.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| ALC-001 | The North American NEC TurboChip is TGX020005, dated 1989. Retronomicon's witness shows the NEC title marking. | Confirmed | Corroborated | High | P1, P2, R1; W2 0:08 |
| ALC-002 | Holding Button I compresses the plunger for the initial serve. Button I controls the right flipper and the Direction Key the left thereafter. Button II is a distinct board nudge. No exact nudge or press duration can be assigned to the observed frames. | Confirmed | Direct | High | P1 pp. 2–5; W1 0:31–0:35; W2 0:18–0:25 |
| ALC-003 | The two screens are regions of the same main field. At the first upward serve, the ball travels along the right lane and the view switches from the lower to the upper region. The silver ball continues there; later impacts yield different paths. | Observation | Corroborated | High | P1 pp. 4–5; P2; W1 0:32.5–0:39; W2 0:21–0:30 |
| ALC-004 | Passages through the upper gate lanes light their lamps. All four must be lit together to qualify its bonus. The separate Tentacloid Lock sometimes opens or closes; all four lamps alone do not add the bonus. | Observation | Corroborated | High | P1 pp. 4, 6; W1 1:08–1:12; W2 1:35–1:51 |
| ALC-005 | A live-ball approach with four lamps lit is followed by the lock's active purple state, the `BONUS` display and a rising total on the upper field. Later the lamps are dark, the local display is 1,000 again and ordinary ball motion continues above the lower field. | Observation | Corroborated | High | P1 p. 6; W1 1:11–1:18 |
| ALC-006 | The witnessed tally shows 2,000 and multiplier ×1 beside a changing aggregate. It does not establish the entire award formula. The exact lock-opening schedule and the trigger-frame contact are not isolated. | Observation | Direct | Medium | W1 1:11.5–1:16 |

## Basic data

- Release / origin: 1989 NEC North American release, ©1989 HUDSON SOFT
  in the English booklet. Konami's retrospective distinguishes its title
  from the earlier PC Engine edition.
- Families: FAM-007 for flipper contact, gravity and rebound control;
  FAM-010 for live interception and keeping a moving ball in play.
- P1: [Original English TurboGrafx-16 booklet, hosted by Konami](https://dds.konami.com/games/manual/pcemini/en_Alien.pdf).
  Printed pp. 2–3 give the controls and selection, pp. 4–5 map the fields
  and serve, p. 6 names the Upper Gate and Tentacloid Lock, and pp. 7–8
  distinguish bonus rooms and score objectives from this on-table award.
- P2: [Konami's product history and edition note](https://www.konami.com/games/pcemini/lineup/jp/en/).
  Describes two main screens and identifies the 1989 North American game.
  Konami states the regional title is different. This research does not
  infer exact capture or cartridge bytes from that statement.
- R1: [North American TurboChip product listing](https://gamefaqs.gamespot.com/tg16/588890-alien-crush/data).
  Reports NEC carrier TGX020005 and year 1989.
- W1: [LongplayArchive, Retro Game Spacko, TurboGrafx-16 longplay](https://www.youtube.com/watch?v=cFQnecMKBoE&t=31s).
  The bounded segment uses the first start through the on-table
  award. The recorder labels it NTSC TurboGrafx-16.
- W2: [Retronomicon's PC Engine/TurboGrafx-16 capture](https://www.youtube.com/watch?v=PDbqLFZ9M08&t=8s).
  The title at 0:08 displays `FROM NEC` and 1989. Initial frames show
  the right lane, light activation and both regions of the main field.
  Some open-lock frames show a still-incomplete gate-lamp set.
- Claim IDs: ALC-001–ALC-006.

### Reproducible fixture evidence

1. Start a solo session and send the ball from the right lane with
   Button I. The booklet documents the strength relation. W1
   at 0:32.5 shows the ball near the plunger; at 0:33.0 it is higher
   in the right lane, and at 0:34.0 it appears on the upper screen.
   W2 repeats that lower-to-upper path near 0:22–0:24.
2. Keep the live ball above the lower drain by timing a flipper on
   its side of approach. The gates lie along the top of the upper
   field. W1 shows two green gate lamps at 1:08, three at 1:09
   and four at 1:11. They show qualification separately from the
   ball's continually changing position.
3. Direct the live ball to the intermittently accepting Tentacloid
   Lock on the upper right. W1 at about 1:11.5 changes the receiver
   to its purple state. The `BONUS` overlay is visible by 1:13 and
   shows 2,000 ×1. Its aggregate reads 30,600 at 1:13 and 52,600
   at 1:15. Those values establish the observed increase, not a
   one-off 2,000-point transfer formula.
4. The overlay is gone by 1:16. The four gate lamps are dark and the
   local counter reads 1,000. From 1:17 to 1:18 the ball is visibly
   moving on the upper main field again. This is the endpoint.
5. W2 enters the same upper region but has only partial qualification
   during a nearby open-lock interval. This contrast supports treating
   lamp completion separately from the receiver's visual opening.

## Mechanical decomposition

### Action Genes

- ACT-895: time the left or right flipper when the live ball enters reach.
- ACT-896: independently nudge the table as documented. No exact
  trajectory sample is attributed to a particular Button II press.
- ACT-921: hold the plunger command to choose the mechanical strength
  of the serve from the stationary right-hand lane.

### System Behaviour Genes

- SYS-146: the released silver ball moves under gravity and contact;
  side impacts, flippers and bumpers change its physical course.
- SYS-1983: the qualified main-field lock gives the bonus and restores
  the live ball to the same playfield. Local qualifier lamps reset as
  the running score continues.

### Constraint Genes

- CON-894: the gate-lamp set and entry into the eligible receiver are
  separate prerequisites for the upper award.

### Information Genes

- INF-642: distinguish the four upper gate lamps, the lock's local
  appearance and the pending bonus amount from the changing total.

### Objective Genes

- OBJ-002: increase the ongoing score. The upper-gate bonus is one
  reachable award in that open scoring objective.

### Time Genes

- TIM-003: choose flipper or nudge timing while the ball and the local
  receiver conditions continue to change.

### Parameters

Plunger hold, ball-speed preset, flipper side and reach, nudge timing,
rollover route, total lamps, lock location and eligibility, the pending
tally, multiplier and lower drain boundary are fixture parameters.

## Reproducible transitions

| Entry state | Input or event | Expected next state | Evidence |
| --- | --- | --- | --- |
| Ball staged in the right-hand lower lane | Hold the plunger command and serve | One physical ball traverses the right lane and camera switches to the upper field | ALC-002–ALC-003 |
| Upper ball moves and some gate lamps are dark | Route the ball through unlit lanes | Individual lamp activation accumulates toward the full set | ALC-004 |
| Four upper gate lamps lit | Route the live ball into the eligible Tentacloid Lock | Receiver captures the ball and the same-field bonus tally appears | ALC-004–ALC-006 |
| Same-field bonus tally is displayed | Let the local tally finish | Upper lamps clear, local count returns to 1,000 and live motion resumes | ALC-005 |

## Strategic and experiential structure

A reflexive ball save and the choice to aim for a particular lamp work
on different timescales. When the four lamps are lit, the lock shot
still needs a playable path and an eligible opening. An open receiver
alone is not a successful upper-gate route.

## Replay and variation

Two launch witnesses give different contact sequences and timing.
Only W1 reproduces this exact upper-gate award within the inspected
interval. A repeated, controlled comparison of hold duration and
same-speed launch paths remains open.

## Adjacent systems and history

Konami distinguishes the commercial North American and Japanese title
screens and identifies the version on the mini console. The original
booklet enumerates four separate bonus rooms; their entries and
settlements are outside this main-field award. Devil's Crush is a
separate game with different table and bonus predicates.

## Normalised genome

- Action: ACT-895, ACT-896, ACT-921.
- System Behaviour: SYS-146, SYS-1983.
- Constraint: CON-894.
- Information: INF-642.
- Objective: OBJ-002.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `703` (`GAME-0001`–`GAME-0703`).
- Exact genome matches: none.
- Tied near matches: `GAME-0672` — Devil's Crush (`4 / 15 = 0.266667`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Devil's Crush (GAME-0672)](devils-crush.md) | ACT-895, ACT-896, SYS-146, TIM-003 | Both time flipper contact and allow a separate table nudge while the ball remains physical. The scoped Devil's Crush pocket opens after head hits and leads to a separate five-target bonus chamber. Alien Crush qualifies a same-field award with four upper gates and settles it into live main-table play. | Near, `0.266667`. |

## Taxonomy impact

Reuse the flipper, nudge, ballistic motion, live timing and open-ended
score definitions. Admit a variable plunger serve, a plural-lamp
qualification with a separate physical receiver, the status cues and
the main-field bonus-and-resume behaviour.

## Negative results

- Opening the lock without completing the gate-lamp set does not
  establish the qualified upper-gate bonus.
- Neither witness confirms a deterministic opening schedule or an exact
  points formula from the short animated tally.
- The qualifying upper lock settles on the main field in this trace.
  The observed award is separate from a later bonus-room visit.

## Delta summary

This bounded route isolates the main table's transition from a timed
physical serve to individually qualified lamps and an on-table award.

## New facts

- The original booklet specifies a hold-dependent plunger.
- The lamp set becomes complete before the receiver's active state.
- After the bonus settles, the active ball resumes on the upper field.

## Principles and design implications

Give a physical launcher an initial decision, then make the rolling
ball continuously actionable through contact. Put small goals into its
route, but require a separately aimed capture to turn qualification into
a reward. Show both states so the player can plan the next shot.

## Puzzle or game generation potential

Use an original two-region physical table and a single ball. Each
reached lane lights one indicator. Send the qualified ball to an open
receiver, tally the site reward on the main field and resume with a
clear set of indicators.

## New genes

- ACT-921
- CON-894
- INF-642
- SYS-1983

## New combinations

None. None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 450](../../../research/taxonomy-changes/TAXONOMY_CHANGE_450.md).

## New questions

- Does the lock follow an independent periodic or event-triggered opening?
- Which events contribute to the entire animated aggregate increase?
- What is reset after a confirmed lower-field drain?

## Next recommended game

Continue Selection 061 with Contraband Police on the English Windows
Steam release. Follow a documented first checkpoint discrepancy to
a scored admission or rejection.

## Why this game

A single pinball can link several clearly visible route objectives
to an independently enabled physical capture without ending the run.
