---
game_id: GAME-0380
slug: professor-layton-and-the-curious-village
game_title: Professor Layton and the Curious Village
analysis_status: reviewed
reviewed: 2026-09-24
combination_ids: []
gene_ids:
  action:
    - ACT-521
    - ACT-522
  system:
    - SYS-1034
    - SYS-1035
  constraint:
    - CON-687
  information:
    - INF-387
  objective:
    - OBJ-222
  time:
    - TIM-002
---

# Game: Professor Layton and the Curious Village

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). A puzzle's
specific drawing, answer, coin balance and picarat value are parameters, not
separate genes.

## Analysis scope

- Version / ruleset: the original North American English Nintendo DS release,
  restricted to opening puzzle 001, Where's the Town?. The manual describes
  the puzzle interface and general scoring. A puzzle-specific illustrated
  walkthrough identifies the opening answer gesture and its result; that
  narrower point is secondary corroboration, not an observed play trace.
- Structured analysis target: from the opening road conversation presenting
  the village map puzzle to accepted submission of its correct circled map
  location, credited picarats and continuation toward St. Mystere. The bounded
  packet includes optional purchased hints and a wrong-answer retry branch.
  No exact initial coin balance is assumed in the model.
- Primary decision loop: read the fixed map question, optionally spend an
  available hint coin to expose the next clue, circle one pictured village
  with the stylus and submit. An incorrect submission offers another attempt
  but reduces the puzzle's obtainable picarats; the accepted answer credits
  the remaining value and advances the story gate.
- Entry and exit: enter when puzzle 001's prompt and map are available on the
  touchscreen. Exit positively when the circled north-west village is accepted,
  the puzzle is marked solved and the road narrative can continue. Repeated
  wrong guesses are not a terminal loss, but cannot count as completion.
- Included: visible fixed puzzle prompt and candidate map, stylus circle plus
  Submit, ordered optional hint purchase with a finite coin balance, authored
  answer validation, wrong-answer picarat reduction, retained puzzle reward
  and story continuation, self-paced decision time.
- Excluded: exploration after village entry; hidden scene-object coin searches;
  later puzzles, optional side puzzles, item rewards, complete collection or
  story mystery; touch gestures for other puzzle types; download puzzles;
  mobile HD remaster; invented exact penalty amounts or hint coin stock.
- Potential scoped modules: scene exploration and dialogue-triggered puzzle
  discovery, later puzzle types, the full mystery, and collection rewards.
- Direct-play status: none. No DS cartridge, emulator, build hash, save,
  screenshot, audio, video or input trace was examined. The Nintendo-authored
  manual and official publisher description support the general rules; the
  named first-puzzle answer and reward are corroborated by independent
  walkthroughs. The transition table is a rule reconstruction, not measured
  execution.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| LAY-001 | The original DS adventure embeds authored puzzles in Layton and Luke's route toward St. Mystere. | Confirmed | Direct | High | P1; P2 |
| LAY-002 | A puzzle displays an explanation and takes a stylus-formatted answer followed by Submit. | Confirmed | Direct | High | P2 pp. 8–9 |
| LAY-003 | One hint coin buys one of up to three ordered puzzle hints. | Confirmed | Direct | High | P2 pp. 9–10 |
| LAY-004 | A correct solution credits picarats and records the puzzle as solved; an incorrect submission reduces the picarats obtainable on a later correct solution and permits retry. | Confirmed | Direct | High | P2 pp. 9–10 |
| LAY-005 | Opening puzzle 001 is a map-location question answered by circling the upper-left village; the unreduced award is ten picarats. | Confirmed | Corroborated | Medium | S1; S2 |
| LAY-006 | The exact initial coin stock, penalty steps, lower reward floor and executable feedback timing were not directly verified for this packet. | Observation | Limited | High | P2; direct-play limit |

## Basic data

- Release / origin: LEVEL-5 first released the Japanese Nintendo DS game on
  15 February 2007; this packet uses the original English North American DS
  puzzle wording rather than the later mobile remaster. Nintendo released its
  European DS edition on 7 November 2008; this date is not represented as the
  North American launch date.
- Platform or physical form: single-player Nintendo DS Game Card, touchscreen
  and stylus; PLAT-NINTENDO-DS.
- Puzzle family: authored clue-and-answer progression with a finite hint
  currency and a retry-sensitive point award.
- **[P1]** [Nintendo's game
  page](https://www.nintendo.com/en-gb/Games/Nintendo-DS/Professor-Layton-and-the-Curious-Village-272563.html),
  checked 2026-09-24, for the DS product, publisher, village adventure and
  puzzle-gated progression. [LEVEL-5's product
  register](https://www.level5.co.jp/products/) confirms the 2007 Japanese
  original and developer identity.
- **[P2]** [Nintendo's original English instruction booklet, preserved by
  ManualsLib](https://www.manualslib.com/manual/111807/Nintendo-Professor-Layton-And-The-Curious-Village-64327a.html),
  pp. 8–10, reviewed 2026-09-24. The primary text is publisher-authored; its
  mirror host is not the publisher. Nintendo's [DS manual
  index](https://en-americas-support.nintendo.com/app/answers/detail/a_id/16905/)
  still identifies this title, but its PDF link was unavailable when checked.
- **[S1]** [Illustrated first-puzzle
  walkthrough](https://professorlaytonwalkthrough.blogspot.com/2008/02/puzzle001.html),
  for the US/UK puzzle name, upper-left answer and ten-picarat value.
- **[S2]** [StrategyWiki's first-puzzle
  register](https://strategywiki.org/wiki/Professor_Layton_and_the_Curious_Village/Puzzles_1-25),
  independently corroborating the stylus circle, Submit and ten-picarat
  puzzle value. Neither walkthrough is a substitute for direct play.
- Claim IDs: LAY-001–LAY-006.

## Mechanical decomposition

### Action Genes

- ACT-521: draw a circle around one village symbol in the pictured map and
  press Submit; the drawing is a spatial answer, not avatar movement.
- ACT-522: optionally spend one available hint coin to reveal the next
  authored hint for this unsolved puzzle.
- Parameters: circled region, submit input, available coins and next hint.
- Claim IDs: LAY-002, LAY-003, LAY-005.

### System Behaviour Genes

- SYS-1034: compare the submitted circled location with the fixed accepted
  answer; reject a mismatch and retain retry access, or mark the puzzle
  solved and release the story gate on a match.
- SYS-1035: reduce obtainable picarats after an incorrect submitted answer;
  credit the remaining displayed award on a correct solution. Hint purchase
  itself is not asserted to cause that reduction.
- Resolution order: commit marked region; answer validation; on mismatch,
  reduce available reward and return to puzzle choices; on match, award the
  current value and continue. Hint purchase instead reveals a clue before
  another answer is submitted.
- Claim IDs: LAY-003–LAY-005.

### Constraint Genes

- CON-687: the next hint can be unlocked only if an unspent hint remains and
  at least one hint coin is available; each purchase consumes a coin and does
  not skip directly to the last hint.
- Scarce resources: hint coins and maximum remaining picarats. The road
  narrative has no ticking countdown in this scoped puzzle.
- Claim IDs: LAY-003, LAY-004.

### Information Genes

- INF-387: puzzle text, candidate village locations, current picarat value
  and purchased hints are shown, but the correct map village is not marked
  for the player before solving.
- Claim IDs: LAY-002–LAY-005.

### Objective Genes

- OBJ-222: solve the fixed opening map question by submitting its accepted
  circled village, so the first story gate opens and the road scene continues.
  More picarats are desirable, but a perfect score is not the exit condition.
- Claim IDs: LAY-001, LAY-004, LAY-005.

### Time Genes

- TIM-002: the displayed puzzle waits for the player's reading, hint purchase
  and answer submission. The scope has no forced timer or autonomous world
  tick while deciding.
- Claim IDs: LAY-002–LAY-004.

## Reproducible transitions

| Before | Action | Rule-grounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Opening map prompt is visible with no chosen location | Read the question and circle a pictured village | One candidate area becomes the pending answer; no story gate opens yet | Marking is separate from validation | LAY-002, LAY-005 |
| At least one coin and an unrevealed next hint are available | Purchase that hint | One coin is spent and the next fixed clue appears | Hint information is resource-gated | LAY-003 |
| A wrong village is circled | Press Submit | The answer is rejected; a retry remains possible and obtainable picarats decline | Wrong answers are informative but costly | LAY-004 |
| The upper-left village is circled | Press Submit | The fixed answer is accepted, the puzzle is recorded solved, remaining picarats are credited and the road story proceeds | Correctness, reward and gate are separate outcomes | LAY-004, LAY-005 |

The exact wrong-answer reward decrement and feedback animation cannot be
reconstructed without a recorded build. These rows describe documented rules,
not a claim that this unit was played.

## Strategic and experiential structure

- Local decision: distinguish the correct village from the map's distractors
  before committing a spatial answer. A purchased hint can reduce uncertainty
  at the cost of a finite coin.
- Medium-term planning: preserve picarats by avoiding speculative submissions;
  retry allows eventual progress despite a reduced reward.
- Long-term structure: only this first gate is admitted. Puzzle-index
  completion and later village investigation are outside the terminal.
- Failure attribution: a wrong submitted location is rejected visibly, but
  precise scoring loss needs build-specific confirmation.
- Player-trust factors: the game discloses the puzzle, hint option and current
  value rather than treating a wrong answer as an unannounced game over.
- Claim IDs: LAY-002–LAY-006.

## Replay and variation

- What changes between attempts: player-selected region, bought hints and
  remaining obtainable picarats. The authored answer does not randomise.
- Multiple viable strategies: solve unaided, buy one or more hints, or retry
  after a wrong submission. These have the same correct-answer gate but may
  differ in coin use and credited picarats.
- Claim IDs: LAY-003–LAY-005.

## Adjacent systems and history

- The first DS game integrates stand-alone riddles into a framed village
  mystery. Later Layton versions and mobile remasters are not used to infer
  this original DS puzzle's exact rules.
- The map-circle input is unlike the entire-grid completion of Sudoku or the
  staged physical mechanisms in The Room. Those games remain comparison
  candidates only where an exact gene boundary transfers.
- Claim IDs: LAY-001–LAY-006.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-521, ACT-522 | Circle and submit; optionally purchase hint |
| System Behaviour | SYS-1034, SYS-1035 | Fixed answer, retry gate and picarat award |
| Constraint | CON-687 | Ordered hints require coins |
| Information | INF-387 | Prompt, map, reward and bought clues |
| Objective | OBJ-222 | Solve first map gate |
| Time | TIM-002 | Self-paced puzzle |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `379` (`GAME-0001`–`GAME-0379`).
- Exact genome matches: none.
- Tied near matches: `GAME-0064` — SET (`1 / 12 = 0.083333`).
- Supported combination subsets: none.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0064` SET | `TIM-002` | Both allow an unhurried visual decision; SET selects a valid three-card relation from one public field, whereas Layton circles one authored map answer, may buy clues and trades wrong submissions against picarats to open a story route. | Tied near, `0.083333` |

### Preserved research notes

- New genes: ACT-521, ACT-522, SYS-1034, SYS-1035, CON-687, INF-387,
  OBJ-222.
- Classification result: New gene.
- Evidence and reasoning: the publisher manual defines the answer, hint and
  reward rules. Puzzle-specific walkthroughs isolate this opening map target.

## Taxonomy impact

- Registry changes: seven additive Active IDs; earlier signatures unchanged.
- Taxonomy-change record: TAXONOMY_CHANGE_119.
- Candidate terms affected: circled-map answer, hint purchase, retry-sensitive
  picarats and authored story gate.

## Negative results

- none; no prior accepted mechanic is disproved. Later content is excluded
  from this bounded analysis, not absent from the product.

## Delta summary

## New facts

- [Confirmed | Direct | High] LAY-001–LAY-004 establish original DS puzzle
  presentation, hints and picarat feedback; LAY-005 specifies the first map
  question with independent secondary corroboration.

## New genes

- [Observation | Corroborated | Medium] Seven additive IDs distinguish
  answer-marking, clue purchase, validation, score penalty and story gating.

## New combinations

- [Observation | Direct | High] No verified combination is introduced.

## Taxonomy changes

- [Confirmed | Corroborated | High] TAXONOMY_CHANGE_119 records additive
  boundaries without modifying an earlier signature.

## New questions

- What exact initial hint-coin stock and picarat penalty schedule does an
  original North American cartridge display for puzzle 001?
- What are the frame-by-frame feedback and save transitions after Submit?

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0381 GoldenEye 007, the next recorded
  genre-alternating subject.
- Optimisation criterion: contrast a self-paced authored clue gate with a
  timed spatial mission and objectives.
- Expected information gain: distinguish puzzle acceptance from stealth and
  combat mission settlement.
- Backlog impact: preserves the remaining selected horizon in order.

## Why this game

- [Hypothesis | Limited | Medium] Professor Layton contributes a recognisable
  touchscreen clue-and-answer puzzle to the selected nine-game mix.
