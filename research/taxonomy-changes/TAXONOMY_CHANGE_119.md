# Taxonomy Change 119: Authored map answer with paid hints and retry-sensitive picarats

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-09-24
- Trigger: GAME-0380 Professor Layton and the Curious Village, original North
  American English Nintendo DS opening map puzzle 001.
- Scope: seven additive Active genes; no earlier game signature, lifecycle or
  verified combination change.

## Problem

The Nintendo-authored booklet describes a puzzle prompt, stylus answer and
Submit, purchased hint tiers, retry after incorrect submission and a reduced
picarat award. Two independent puzzle-specific guides identify the first map
question's circled target. Existing self-paced decision time (TIM-002) transfers.
Whole-board solution, score-maximisation or scene navigation genes do not
capture this one pictured answer and its narrative continuation.

## Accepted change

- ACT-521 captures circling and submitting one visual region; ACT-522
  captures optional one-coin purchase of the next authored hint.
- SYS-1034 validates the region and releases the road story gate on success;
  SYS-1035 reduces the later picarat award after a wrong submission.
- CON-687 requires an available coin and next unrevealed tier; INF-387 shows
  the prompt, map, available reward and purchased hints without the solution.
- OBJ-222 requires acceptance of the fixed first answer, not a perfect score.

## Lower-ID transfer and rejection test

- TIM-002 fits the puzzle's self-paced read/submit rhythm without redefining
  time for earlier games.
- ACT-004 marks a hidden cell as a protective hypothesis, not one illustrated
  answer to submit. OBJ-041 seeks a concealed ordered sequence, OBJ-043 opens
  a physical multi-stage enclosure, and OBJ-002 maximises score rather than
  requiring this specific authored narrative gate.
- The deterministic lower-ID scan and all maximum-score ties are recorded in
  the canonical game packet after index generation. Mathematical proximity is
  not treated as evidence that another game's story structure is equivalent.

## Evidence and limits

The [Nintendo-authored original
manual](https://www.manualslib.com/manual/111807/Nintendo-Professor-Layton-And-The-Curious-Village-64327a.html)
is preserved by a third-party host. [Nintendo's product
page](https://www.nintendo.com/en-gb/Games/Nintendo-DS/Professor-Layton-and-the-Curious-Village-272563.html)
confirms DS identity and puzzle-gated adventure. The first map location is
corroborated by an [illustrated walkthrough](https://professorlaytonwalkthrough.blogspot.com/2008/02/puzzle001.html)
and [independent puzzle register](https://strategywiki.org/wiki/Professor_Layton_and_the_Curious_Village/Puzzles_1-25).
No cartridge was played, so exact opening coin stock and reward decrement are
not asserted. Hint purchase and wrong-submission penalty are kept distinct.
