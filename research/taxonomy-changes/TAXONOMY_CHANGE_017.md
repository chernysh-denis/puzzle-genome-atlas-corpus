# Taxonomy Change 017: Generalise the bounded rival-race objective

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: `2026-09-02`
- Trigger: maintainer review found that `OBJ-134` encoded one named Need for
  Speed Underground event and its parameter values as the canonical boundary.

## Current classification

- Exact wording or stable ID: `OBJ-134` — Win and retain the opening
  Underground Circuit.
- Files and entries affected: Objective registry, Ukrainian gene localisation,
  `GAME-0217`, candidate-term disposition, deterministic language and taxonomy
  artifacts, research log and web contract tests.
- Original evidence or rationale: `GAME-0217` supplied a reproducible positive
  terminal at first place in `Jose's Got Your Back`, followed by `375` Bank and
  retained Race 1 completion.

## Detected problem

- The old label and definition embedded the named event, two laps, Easy
  difficulty, reward currency and first-career-event identity even though the
  record itself classified those values as parameters.
- The problem was found on the public GAME-0217 gene card, where the canonical
  label read as a task walkthrough rather than a transferable objective.
- The decision-relevant boundary is not the proper noun or reward amount. It is
  the requirement to beat autonomous rivals in a finite ordered race and then
  retain the accepted result and disclosed completion reward.

## Evidence

- Primary sources: the reviewed GAME-0217 source ledger and reproduced
  transitions remain the evidence for first-place classification, Bank credit
  and retained Race 1 completion.
- Reproducible transitions: complete the ordered course; cross the valid finish
  while leading; accept the result transition; observe the event result and
  reward retained. A lower place does not satisfy the objective.
- Analysed games checked: every canonical carrier of `ACT-290` and every
  carrier of ordered-race constraint `CON-438`, including `GAME-0171`,
  `GAME-0195`, `GAME-0199`, `GAME-0208`, `GAME-0216` and `GAME-0217`.
- External systems or literature checked: no new external claim is required;
  the change narrows the abstraction to mechanics already evidenced in the
  accepted corpus.
- Counterevidence: Trackmania and BeamNG accept a valid solo timed finish
  without rival victory; Need for Speed Unbound accepts any classified place
  and requires a later pursuit/garage terminal; Forza Horizon 6 pursues a
  multi-event Festival qualification; Need for Speed Payback pursues an
  authored vehicle delivery. None is a valid additional carrier.

## Proposed change

- Old classification: win and retain the named opening Underground Circuit.
- Proposed classification: win a bounded race against autonomous rivals and
  retain its persistent event result and disclosed completion reward.
- Definitions and boundaries: first place, finite ordered course, rival field
  and retained result/reward remain essential. Event, route, vehicle, lap
  count, rival count, difficulty, reward type/amount and career flag become
  parameters. Solo time trials, any-place classification, multi-event gates,
  post-race pursuit/garage settlement and vehicle-delivery missions remain
  excluded.
- Lifecycle effects: `OBJ-134` remains `Active`; no alias, merge, split or new
  stable ID is created.
- What does not change: GAME-0217 scope, 14-gene signature, `COMB-0215` set,
  family memberships, comparison scores, artwork and public title.

## Genome and combination impact

- Genes added, deprecated, merged or split: none; one Active boundary is
  generalised in place under its immutable ID.
- Games requiring annotation: `GAME-0217` only.
- Combinations affected: `COMB-0215` retains the same strict gene set and
  supporting game; its mechanic now references the generalised boundary.
- Novelty claims affected: the original new-gene claim is retained as history,
  but novelty belongs to the reusable rival-race terminal rather than its
  Underground parameter values.

## Decision

- Decision: `Accepted` and implemented.
- Decided by: Puzzle Genome Atlas maintainer in response to the rendered
  GAME-0217 gene card.
- Rationale: the transfer test preserves the evidenced decision boundary while
  removing game content and numeric parameters from canonical comparison.
- Implementation links: `OBJ-134`, `GAME-0217`, `COMB-0215` and the reviewed
  Ukrainian `OBJ-134` localisation.

## Change history

- `2026-09-02`: accepted after the full racing-objective transfer scan; no
  signature or combination membership changed.
