# Taxonomy Change 115: Size-gated rolling collection

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-09-23
- Trigger: `GAME-0376` Katamari Damacy REROLL, ordinary PS4 replay of
  `Make a Star 1` after unlock.
- Scope: five additive Active genes; no prior signature, lifecycle or
  verified combination changes.

## Problem

The player steers a collecting ball, not merely a character that receives
an abstract pickup score. Each eligible object physically joins the body and
increases the set of collectable objects. Too-large items initially block
pickup; hard impacts can detach gathered material. A target diameter must be
met before a fixed stage deadline. Existing consumable-terrain growth, cell
feeding and generic contact-collection genes cannot jointly express this
reversible, size-gated body accumulation.

## Accepted change

- `SYS-1022` retains eligible touched objects on a growing moving body.
- `SYS-1023` allows hard impacts to shed attached objects.
- `CON-680` gates pickup by current size relative to the object.
- `INF-383` exposes current diameter, target and remaining time.
- `OBJ-218` settles a sufficient-diameter ball as a star.

## Lower-ID transfer and rejection test

- `ACT-008` transfers local steering, `CON-068` transfers fixed failure
  deadline, and `TIM-003` transfers live progression. Their definitions stay
  unchanged.
- `SYS-037` credits contact collection without making the object part of the
  moving body; `SYS-080` advances a snowball on a finite terrain-state ladder;
  `SYS-1014` converts mouth-compatible food into Spore DNA/progress;
  `SYS-1015` changes a cell's size with food milestones. None is widened to
  cover retained heterogeneous world objects on one rolling ball.
- `CON-677` is a diet and mouth gate for living prey, not object-specific
  katamari adhesion. `INF-067` combines task requirements and rewards, not
  the live physical-body diameter/target/countdown triad.
- Every lower-ID genome and verified combination is scanned deterministically
  before acceptance. Theme alone cannot establish a subset combination.

## Evidence and limits

Bandai Namco's REROLL descriptions establish the collecting ball and
star-making premise; the PS4 listing confirms edition identity. Namco's
contemporary original-game description establishes the timed-size loop, while
first-hand REROLL reports document the first stage's four-minute display,
size-gated items and impact-related loss. The older PS2 three-minute figure
is not copied to the remaster. No PS4 executable or direct-play trace was
inspected, so the exact PS4 timer and hidden collision coefficients remain
replication targets rather than independently verified facts.
