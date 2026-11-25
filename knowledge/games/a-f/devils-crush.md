---
game_id: GAME-0672
slug: devils-crush
game_title: "Devil's Crush"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-895
    - ACT-896
  system:
    - SYS-146
    - SYS-1926
    - SYS-1927
    - SYS-1928
  constraint:
    - CON-885
  information:
    - INF-619
  objective:
    - OBJ-029
  time:
    - TIM-003
---

# Game: Devil's Crush

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Target counts, result values, controller bindings and ball colours are instance
parameters.

## Analysis scope

- Version / ruleset: original English North American Devil's Crush TurboChip
  for TurboGrafx-16, NEC TGX030038, 1990. Ordinary solo pinball as recorded
  before the use of any later completion password. Exact carrier bytes,
  capture equipment and input preset are unverified.
- Structured analysis target: PLAT-TURBOGRAFX-16 in
  `knowledge/platforms/games.json`. Reference is the original North
  American rules, not the Japanese, Genesis or later download edition.
- Entry: bring a live ball to the lower main field while the left Dragon's
  Head has opened its mouth. Redirect the ball into the active mouth.
  Begin Bonus Stage 1 as this entry transitions into the five-headed chamber.
  The manual documents earlier head contacts for opening it. The reference
  footage starts with the entrance already eligible.
- Primary decision loop: track the ball's motion and the remaining heads.
  Time the flipper on the side of approach to send the ball back toward
  an exposed target while managing its rebound and drain risk. The
  documented board nudge offers a separate trajectory adjustment.
  A broken egg can reopen a lane briefly before it regenerates.
- Exit: destroy the fifth required head, observe the perfect result and
  two awards, then verify live blue-ball control on the lower main field
  with the returned score and the same displayed ball count.
- Included: the eligible physical entry, live flippers, documented nudge,
  gravity and rebounds, local shielding eggs, the finite target clear,
  the separated bonus tally and score-colour state at return.
- Excluded: the exact launch procedure from a fresh game, counting the
  pre-entry contacts in this footage, routes through other pockets, the
  other bonus tables, full main-table score economy and extra balls,
  passwords and backup memory, the pink-ball trigger, ending progression,
  and later port differences. A drain can close a bonus visit without
  the required clear. A full BS-1 drain settlement was not reproduced.
- Potential scoped modules: a clean ordinary-ball attempt with a
  known capture preset, the BS-1 drain branch, or an unbroken trial
  from a fresh serve to a verified entry.

## Direct-play status

No personal hardware, cartridge-byte inspection or direct play. The
original North American manual documents controls, the Dragon's Head
entry and Blue Ball. The early World of Longplays passage shows the
entry from the lower field, the target set, both payouts and live
return. The producer says save states may be used and discloses a
completion code in a later part. Only the earlier observed transition
is admitted here. The independent two-flipper capture corroborates
target exhaustion and the local perfect result, but edits away the
return. Static frames were inspected in the background without audio.
Physical button telemetry, hitboxes, nudge timing, exact temporary
multiplier duration and carrier identity were not verified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DCR-001 | The original English NEC TurboChip was released in North America in 1990. The named bonus stage is present in the original rules. | Observation | Corroborated | High | P1, R1, W1 09:21, W2 00:35 |
| DCR-002 | The Dragon's Head in the lower main field has a hit-conditioned open mouth that can take a live ball to BS-1. The open state and actual entry are separate. | Observation | Corroborated | High | P1 pp. 5–6 nos. 7, W1 09:16–09:21, R2 Dragon |
| DCR-003 | Direction Key and Button I time the left and right flipper sides. Button II nudges the table. The ball travels and collides without continual aim control. Four flippers are present in W1 and two in W2. | Observation | Corroborated | High | P1 pp. 2, 4, W1 09:21–09:48, W2 00:36–01:58 |
| DCR-004 | BS-1 starts with five vulnerable heads and defensive eggs. A contacted egg can deflect the ball and disappear with subsequent reappearance. Destroyed heads go away for the observed visit. | Observation | Corroborated | High | R2 Bonus Stage 1, W1 09:21–09:48, W2 00:36–01:58 |
| DCR-005 | Exhausting the head set ends local play with a perfect result. The reference settlement credits 968,000 bonus points then 4,000,000 special points, moving 19,804,900 to 24,772,900 before new main-table hits. | Observation | Corroborated | High | W1 09:46–10:01, W2 01:56–02:00, R2 Bonus Stage 1 |
| DCR-006 | The blue ball resumes lower main play with the settled score and `BALL 02` retained. The original manual associates perfect clears with Blue Ball and fourfold scoring while blue. W1 entered with blue already active, so this trace does not isolate its first activation. | Observation | Corroborated | High | P1 pp. 4–5, W1 09:17–10:03, R2 Blue Ball |
| DCR-007 | The displayed score increases in two separate transfers. Reference frames preserve the main score through the transition and show the blue ball moving again without a new serve. Neither exact unboosted tally nor all main-field reset rules are established by this instance. | Observation | Direct | High | W1 09:18, 09:52–10:05 |

## Basic data

- Release / origin: 1990, NAXAT/RED title attribution, NEC North American
  TurboChip edition. The record concerns an original-rules single-player visit.
- Families: FAM-007 because contacts, flipper timing and rebounds
  manipulate a free physical body; FAM-010 because the opportunity to
  intervene continues while the ball and shields change.
- P1: [North American TurboGrafx-16 instruction booklet](https://www.digitpress.com/library/manuals/turbografx/devil%27s%20crush.pdf).
  Pages 2 and 4 give input and scoring rules. Pages 5–6 locate the lower
  Dragon's Head, describe the head contacts and identify its BS-1 mouth.
  The booklet is the source for the Blue Ball's fourfold rule.
- R1: [NEC North American edition listing](https://gamefaqs.gamespot.com/tg16/588942-devils-crush/data).
  Identifies carrier TGX030038 and UPC 092218009951.
- R2: [Crush_d, original TurboGrafx-16 field notes](https://gamefaqs.gamespot.com/tg16/588942-devils-crush/faqs/51483).
  Screen 1's Dragon, Blue Ball and Bonus Stage 1 describe the distinctive
  entry, five targets, refreshing eggs and award. This is secondary to
  the manual and actual trace for settled values.
- W1: [World of Longplays, SCHLAUCHI, North American rules](https://www.youtube.com/watch?v=47rfZxa7UKY&t=556s).
  Use 09:16–10:03 from the first part, before the later completion code.
  This is the continuous observed entry, perfect tally and return.
- W2: [LaggyVania, TurboGrafx-16 bonus showcase](https://www.youtube.com/watch?v=xtJ3HniPwd0&t=33s).
  Use 00:35–02:00. Two-flipper variant with a visible `PERFECT` at 01:58.
  The edited segment omits the exact entry setup and the main-table return.
- Claim IDs: DCR-001–DCR-007.

### Reproducible route evidence

1. On the lower main field, find the left Dragon's Head. Normal
   contacts build its opening condition. The manual lists eight
   hits for the larger head-hit event and identifies the mouth entry
   afterward. In W1 near 09:17 the green entrance arrow is visible,
   the ball is blue and the reserve counter reads `02`.
2. Direct the ball into the open Dragon's Head. W1 at about 09:18
   shows the ball approaching the mouth and the fade from the
   lower main table at 19,804,900 points. The fixed bonus board
   appears at 09:20–09:21 with five heads and five egg positions.
3. Use the relevant near flipper as the ball descends. Do not
   confuse a glowing egg or a contact flash with the single ball.
   Watch gaps after an egg disappears. In W1 two heads remain
   around 09:40 and one near 09:46. The last target and associated
   egg sprites disappear by approximately 09:48.
4. Read the two awards in sequence. At 09:52 the ordinary bonus is
   968,000. Around 09:54 the main score is 20,772,900 and the separate
   perfect award shows 4,000,000. After the award transfer the score
   is 24,772,900 and the counter still reads `02`.
5. At 10:00–10:03 the blue ball is back in motion on the lower main
   field. The score remains 24,772,900 until the next main-field hits.
   W2 independently reaches the perfect flag before its edit.

## Mechanical decomposition

### Action Genes

- ACT-895: time the side's pivoting flippers to intercept and redirect
  the currently descending ball. DCR-003, DCR-004.
- ACT-896: use the discrete documented table nudge to alter the
  ball's course. The presence of the input is documented. The trace
  cannot allocate an exact visible impulse to a specific press. DCR-003.

### System Behaviour Genes

- SYS-146: advance the released ball through gravity and collisions.
  DCR-003, DCR-004.
- SYS-1926: settle the optional bonus playfield into the ongoing main
  session. Credit the local tally and the perfect award as distinct
  amounts before resuming on the main field. DCR-005–DCR-007.
- SYS-1927: a hit can break a local intercepting egg. Its later
  reappearance can reclose the shooting line, while already defeated
  heads stay absent within the attempt. DCR-004.
- SYS-1928: use the perfect-clear Blue Ball state to multiply eligible
  subsequent scoring while the state lasts. W1 already has this
  colour when it enters. DCR-005, DCR-006.

### Constraint Genes

- CON-885: the head's qualifying prior hits permit an eligible
  mouth entry. Opening and physical routing are both required for
  this particular entrance. DCR-002.

### Information Genes

- INF-619: distinguish the bonus table's two settlement amounts from
  the main run score and persistent ball-count display. DCR-005, DCR-007.
  The green opening signal, remaining head positions and blue colour
  are in-world feedback for the defined entry, target and scoring rules.

### Objective Genes

- OBJ-029: incapacitate all five required hostile heads before
  the local ball is lost down a drain. DCR-004, DCR-005.

### Time Genes

- TIM-003: choose interception while the ball advances and temporarily
  disrupted shields can return. No exact cycle period is assumed.
  DCR-003, DCR-004.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| The lower Dragon's Head still blocks entry | Accumulate qualifying head hits | Mouth becomes eligible for physical entry | DCR-002 |
| Open lower mouth, live main-field ball | Send the ball into the mouth | Live play switches to Bonus Stage 1 | DCR-002, DCR-003 |
| The ball approaches a reachable flipper | Time the side input | Local contact redirects the ball upward | DCR-003 |
| Head shooting line is obstructed by an egg | Contact the egg and aim at the next opening | Deflection, temporary disappearance and later replacement possible | DCR-004 |
| Last head remains | Hit the last required head before draining | Local play settles and the perfect result qualifies | DCR-004, DCR-005 |
| Bonus chamber settled | Watch both awards transfer | Score moves to 24,772,900 before new main-table hits, blue ball and `02` retained in live return | DCR-005–DCR-007 |

## Strategic and experiential structure

The mouth opening makes entry possible but does not transport the
ball by itself. On the bonus board the player protects the live ball
and trades a safe rebound against a short line through the eggs.
Removing an egg helps create a shot without itself reducing the five-head
clear threshold. The separately shown perfect award and fourfold
Blue Ball condition tie the local finish to subsequent scoring.

## Replay and variation

The reference visit has four flippers. The independent perfect
visit has two, yet its five heads, egg barriers and success flag
remain. Neither selected shot includes a controller trace or shows the
configuration choice that caused that layout. Exact timing of egg
reappearance, previously active blue-state renewal and the missed
attempt's return state remain unmeasured here.

## Adjacent systems and history

The original booklet documents several routes to bonus play. This
scope uses the lower Dragon's Head. Only the tested entry and one
completed bonus visit are attributed to the selected rules.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-895, ACT-896 | Flip by side and nudge the table |
| System Behaviour | SYS-146, SYS-1926, SYS-1927, SYS-1928 | Physical contacts, bonus return, renewing shields and blue score state |
| Constraint | CON-885 | Head hits open a mouth which still requires ball entry |
| Information | INF-619 | Separate award rows, score and ball count |
| Objective | OBJ-029 | Clear the five living head targets |
| Time | TIM-003 | Choose while the ball and shields advance |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `671` (`GAME-0001`–`GAME-0671`).
- Exact genome matches: none.
- Tied near matches: `GAME-0110` — Angry Birds Classic (`3 / 15 = 0.200000`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Angry Birds Classic (GAME-0110)](angry-birds-classic.md) | OBJ-029, SYS-146, TIM-003 | Both resolve a moving body through gravity and impacts and require the complete local hostile set. Angry Birds starts from an aimed slingshot release and spends a finite queue of birds. Devil's Crush repeatedly redirects the same live ball with flippers, threads renewing egg shields and pays a separate bonus before resuming the main playfield. | Near, `0.200000` |

## Taxonomy impact

Seven boundaries add side-specific flippers, table nudging, a
hit-conditioned physical entrance, separate settlement visibility,
continuing bonus return, renewable shot shields and a visible
multiplying ball state. Three prior definitions remain unchanged.

## Negative results

- Opening the entrance supplies an opportunity, not the actual
  transfer. The live ball still has to reach the mouth.
- Substituting an egg hit for a head hit will not satisfy the
  finite hostile target condition. The egg can return.
- The observed bonus clear did not reduce the displayed ball count.
  This is evidence for the successful return only.
- A blue ball was already active in W1 before entry. The trace does
  not establish a fresh blue conversion, its expiry time or a
  successive-clear formula for this reward.

## Delta summary

Ten genes, seven admitted here and three reused. One original
TurboGrafx-16 bonus visit from the live lower-table mouth to the
successful return.

## New facts

- Both the local bonus and the completed target-set award are
  visible before the run resumes.
- The returned score and ball count can be tied across the
  complete observed settlement.

## Principles and design implications

Tie a bonus entrance to a changed physical target so the player
must both expose and reach the route. Show what the local risk
earned in separate categories when returning control to the
same ongoing attempt.

## Puzzle or game generation potential

Use a pair of time-sensitive redirected shots to expose and then
enter a local branch. Keep the branch target set finite and
restore its exact payout to the continuing main run.

## New genes

- ACT-895
- ACT-896
- CON-885
- INF-619
- SYS-1926
- SYS-1927
- SYS-1928

## New combinations

None. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[TAXONOMY_CHANGE_418](../../../research/taxonomy-changes/TAXONOMY_CHANGE_418.md).

## New questions

- What precedes the two-flipper and four-flipper layouts in each capture?
- How long does one egg stay absent at either start speed?
- Which state and stock transitions follow a drained BS-1 attempt?

## Next recommended game

Citizen Sleeper 2: Starward Vector on Xbox Series X|S. Trace one
contract through its actual resolved result.

## Why this game

The completed target set produces a separate payout, then
changes the context of another shot on the same ongoing table.
