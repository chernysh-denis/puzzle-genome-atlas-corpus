# Taxonomy Change 047: Generalise the two-round duel objective to the required round count

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-09
- Trigger: Claude transfer-test initial pass for `GAME-0283` TEKKEN 8, under
  the authority granted by `docs/CLAUDE_GAME_ANALYST_QUALITY_PROTOCOL_V2.md`.

## Current classification

- Exact wording or stable IDs: `OBJ-099` — Win two rounds against one fixed
  opposing fighter, whose definition read "in one fixed One on One match,
  earn the required two round wins through KO or favourable time-over before
  the opposing fighter does".
- Files and entries affected: the Objective registry; the Ukrainian gene
  localisation for `OBJ-099`; the `GAME-0283` decomposition; generated
  indexes and research artifacts.
- Original evidence or rationale: the gene was first isolated for
  `GAME-0172` Street Fighter 6, whose default One on One match is won at two
  round wins. The label and definition encoded that count, although the
  parameter list already named `required wins`.

## Detected problem

- What is incorrect, ambiguous or at the wrong type: TEKKEN 8's default
  offline Versus match is won at three round wins. The objective — earn the
  required round wins against one fixed opponent before it does — is the
  objective `OBJ-099` isolates; the count is a parameter that the entry
  already listed. Under the old wording the second carrier needed a
  duplicate Objective differing only in a number.
- How the problem was found: the `GAME-0283` lower-ID scan of the match
  objective against `OBJ-099`, `OBJ-121`, `OBJ-071` and `OBJ-105`.
- Why this changes decision structure rather than terminology or theme: the
  count changes how many rounds a comeback can span but not the decision to
  win rounds by KO or time-over before the opponent; both carriers share
  that structure.

## Evidence

- Primary sources: the Street Fighter 6 evidence already cited by
  `GAME-0172`; for TEKKEN 8, Bandai Namco's official starting guide ("Win
  the match by winning the required number of rounds", `T8-008a`,
  `Confirmed | Direct | High`) and its 2026 Tekken World Tour rules naming
  the default settings with three rounds (`T8-007b`,
  `Corroborated | Medium`).
- Reproducible transitions: the `GAME-0172` second-marker row and the
  `GAME-0283` third-marker row.
- Analysed games checked: `GAME-0172` and `GAME-0283`; `GAME-0198` keeps
  `OBJ-121` because it settles by stocks.
- External systems or literature checked: none beyond the carriers.
- Counterevidence: none.

## Proposed change

- Old classification: the required two round wins.
- Proposed classification: `OBJ-099` — Win the required round count against
  one fixed opposing fighter: in one fixed one-on-one match, earn the
  declared required number of round wins through KO or favourable time-over
  before the opposing fighter does.
- Definitions and boundaries: the label is widened from `Win two rounds
  against one fixed opposing fighter`; the includes list names both carriers'
  instances with their counts; the excludes list and parameters are
  unchanged.
- Lifecycle effects: none.
- What does not change: the `GAME-0172` signature, every earlier reviewed
  signature, every lifecycle state and every stable ID.

## Genome and combination impact

- Genes added, deprecated, merged or split: none by this record.
- Games requiring annotation: `GAME-0283` reuses the generalised ID;
  `GAME-0172` remains a carrier with its wording valid under the wider
  boundary.
- Combinations affected: `COMB-0170` keeps the same gene set and its sole
  carrier `GAME-0172`.
- Novelty claims affected: the `GAME-0172` novelty note remains true.

## Decision

- Decision: `Accepted`.
- Definitions and boundaries carrier audit: for Street Fighter 6 the
  objective (two round wins by KO or favourable time-over before Luke)
  remains true sentence by sentence with two as the required count. For
  TEKKEN 8 the same objective reads three.
- Decided by: the reuse-first comparison recorded in the `GAME-0283` record
  and pass checkpoint.
- Rationale: a count that the entry already parameterised must not sit in
  the label and definition as if it were the boundary.
- Implementation links: `OBJ-099`, `GAME-0172`, `GAME-0283`.

## Ukrainian review

- `OBJ-099` receives a corrected Ukrainian label, definition and inclusion
  for the widened boundary in the same unit, under the range batch
  `UK-GAME-0172-0283`.

## Change history

- 2026-09-09 — created and accepted during Claude transfer-test initial pass
  for `GAME-0283`, before that draft's independent audit.
