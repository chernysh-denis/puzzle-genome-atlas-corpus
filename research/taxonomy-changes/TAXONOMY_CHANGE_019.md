# Taxonomy Change 019: Merge sport-specific control and broadcast-view duplicates

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-06
- Trigger: cards `C-02` and `C-03` of
  [`FULL_TAXONOMY_DUPLICATE_AUDIT_001`](../normalisation/FULL_TAXONOMY_DUPLICATE_AUDIT_001.md),
  both with disposition `CONFIRMED`

## Current classification

- Exact wording or stable IDs: `CON-398` — One direct-control locus governs an
  eleven-player side; `CON-582` — One direct-control locus governs a
  five-player on-court side; `INF-178` — Broadcast view identifies ball,
  control and local team shape; `INF-289` — Broadcast court view identifies
  ball, control and local team shape.
- Files and entries affected: Constraint and Information registries, Ukrainian
  gene localisation, `GAME-0241` signature and prose, `COMB-0239`, the
  generated game and combination indexes, gene salience, plain-language
  presentation, `GAME-0241`'s selected-neighbour comparison, the deterministic
  research artifacts and the web contract tests.
- Original evidence or rationale: `CON-398` and `INF-178` were isolated for
  `GAME-0163` EA SPORTS FC 26; `CON-582` and `INF-289` were isolated for
  `GAME-0241` NBA 2K26.

## Detected problem

- What is incorrect: each pair states one rule twice, separated only by the
  sport. `CON-398` and `CON-582` both require that one local human authority
  hold at most one direct-control locus over a multi-member side and transfer
  that same unique locus rather than create a second one; the only stated
  difference is eleven versus five. `INF-178` and `INF-289` both require that
  the live broadcast view keep the ball, the control marker, the nearby members
  of both sides and the surface's decision-relevant markings readable before
  the next action; the only stated difference is a pitch versus a court.
- How the problem was found: the full taxonomy duplicate audit, cards `C-02`
  (label-level near identity, numeric-only difference) and `C-03` (label token
  Jaccard 0.89), confirmed by independent review.
- Why this changes decision structure rather than terminology: a side's size
  and a playing surface are values inside one rule.
  [`knowledge/genes/README.md`](../../knowledge/genes/README.md) classifies
  "board size, count, magnitude, topology or threshold" as a parameter, and
  [`TAXONOMY_CHANGE_014`](TAXONOMY_CHANGE_014.md) already merged team-state
  disclosure records "split by HUD layout and match mode" for the same reason.
  Keeping four IDs asserts a decision difference that neither carrier
  evidences.

## Evidence

- Primary sources: the reviewed `GAME-0163` and `GAME-0241` records and their
  source ledgers.
- Reproducible transitions: in both products a switch input transfers the sole
  control locus to an eligible member and is rejected when no eligible member
  exists; in both, the live view exposes ball, control marker, local shape and
  the surface's boundaries before the next action is committed.
- Analysed games checked: fresh unit-level two-way transfer scans over all 608
  Active Constraint genes and all 323 Active Information genes. `CON-398` is
  the nearest Constraint to `CON-582` at 0.154 with the next candidate at
  0.095; `INF-178` is the nearest Information gene to `INF-289` at 0.455 with
  the next at 0.170. No better survivor exists in either type.
- External systems or literature checked: none required.
- Counterevidence, and why it fails: `CON-582`'s `Excludes` opens with "an
  eleven-player football side" and `INF-289`'s `Excludes` names
  "football-pitch presentation". Both exclusions name the sibling by sport
  rather than by decision structure, so they restate the duplication instead of
  refuting it. `INF-289` additionally lists occlusion among its parameters,
  which the survivor now carries as a parameter.

## Proposed change

- Old classification: four genes split by sport.
- Proposed classification: two genes, each parameterised over the sport.
- Definitions and boundaries: `CON-398` becomes "One direct-control locus
  governs a multi-member side" and states the declared side size as a
  parameter. `INF-178` becomes "Broadcast play view identifies ball, control
  and local team shape" and carries the playing surface, markings, scoring
  fixtures, boundaries, camera and occlusion as parameters.
- Lifecycle effects: `CON-582` and `INF-289` become `Merged` aliases pointing
  to their survivors. Their stable IDs are never reused.
- What does not change: `SYS-459` and `SYS-759` are untouched. Their merge is a
  `CONFIRMED-CONDITIONAL` audit finding whose prerequisite — deciding whether
  automatic line-up rotation is a parameter or a separate substitution
  transition — has not been discharged, so it is out of scope here. The
  basketball-specific `CON-583`–`CON-586`, `INF-290` and `INF-291` remain
  distinct, as do the football-specific records of `GAME-0163`.

## Genome and combination impact

- Genes added, deprecated, merged or split: `CON-582` merged into `CON-398`;
  `INF-289` merged into `INF-178`. Active genes fall from 2,354 to 2,352;
  `Merged` records rise from 32 to 34; the 2,387 total definitions are
  unchanged because no ID is deleted.
- Games requiring annotation: `GAME-0241` (signature, decomposition, normalised
  genome, preserved notes and selected-neighbour interpretation).
- Combinations affected: `COMB-0239` substitutes `CON-398` and `INF-178`. Its
  size stays at twenty-one genes and it remains a strict proper subset of the
  twenty-five-gene `GAME-0241` genome. A global scan found no exact combination
  collision and no additional game whose genome now contains `COMB-0239`.
- Novelty claims affected: both survivors record the generalisation.
  `GAME-0241` now claims fifteen new genes rather than seventeen and lists
  `CON-398` and `INF-178` among its reused records.
- Comparison impact: `GAME-0241` keeps `GAME-0163` EA SPORTS FC 26 as its
  selected near neighbour, but the score rises from `4 / 41 = 0.097561` to
  `6 / 39 = 0.153846` and the shared-gene list grows from four to six. No other
  game's selection changes and no exact genome match is created.

## Decision

- Decision: `Accepted`.
- Decided by: confirmed audit cards `C-02` and `C-03` plus fresh unit-level
  two-way transfer tests across both complete type registries.
- Rationale: each surviving gene accepts the same rule from both carriers once
  the side size and the playing surface are supplied as parameters.
- Implementation links: `CON-398`, `CON-582`, `INF-178`, `INF-289`,
  `GAME-0163`, `GAME-0241`, `COMB-0239`.

## Change history

- 2026-09-06 — created and accepted as unit 2 of the confirmed taxonomy
  normalisation derived from `FULL_TAXONOMY_DUPLICATE_AUDIT_001`.
