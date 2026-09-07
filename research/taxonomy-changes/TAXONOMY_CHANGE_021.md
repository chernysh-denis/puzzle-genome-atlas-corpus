# Taxonomy Change 021: Merge the variable-length lexicon gate into the declared-length gate

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-06
- Trigger: card `C-07` of
  [`FULL_TAXONOMY_DUPLICATE_AUDIT_001`](../normalisation/FULL_TAXONOMY_DUPLICATE_AUDIT_001.md),
  disposition `CONFIRMED`

## Current classification

- Exact wording or stable IDs: `CON-112` — Fixed-length lexicon membership
  gate; `CON-376` — Variable-length lexicon membership gate.
- Files and entries affected: Constraint registry, Ukrainian gene localisation,
  `GAME-0156` signature and prose, `COMB-0154`, the generated game and
  combination indexes, gene salience, plain-language presentation, the
  deterministic research artifacts and the web contract tests.
- Original evidence or rationale: `CON-112` was isolated for `GAME-0068`
  Wordle, whose proposals must be exactly five letters. `CON-376` was isolated
  for `GAME-0156` Strands, whose traced proposals must be at least four letters.

## Detected problem

- What is incorrect: both records state the same conjunction — an
  ordered-symbol proposal is eligible only when it satisfies a declared length
  predicate and belongs to the accepted lexicon, and a failing proposal does not
  consume the attempt allowance. The only difference is whether the predicate
  fixes an exact length or a minimum.
- How the problem was found: the full taxonomy duplicate audit, card `C-07`,
  confirmed by independent review.
- Why this changes decision structure rather than terminology: a length bound is
  a threshold, which
  [`knowledge/genes/README.md`](../../knowledge/genes/README.md) classifies as a
  parameter. Decisively, **both records already list the discriminating value
  inside their own `Parameters`** — "sequence length" in `CON-112` and "minimum
  length" in `CON-376` — so each declared the difference to be a parameter of
  itself while a second stable ID asserted it was a boundary.

## Evidence

- Primary sources: the reviewed `GAME-0068` and `GAME-0156` records and their
  source ledgers.
- Reproducible transitions: in both products an entry that fails the length
  predicate or the lexicon lookup is rejected and the attempt or assistance
  allowance is unchanged; an entry that passes both is admitted for scoring or
  answer classification.
- Analysed games checked: a fresh unit-level two-way transfer scan over all 608
  Active Constraint genes. `CON-112` is the nearest Constraint to `CON-376` at
  0.300, with the next candidate an unrelated city-founding rule at 0.081. No
  better survivor exists.
- Counterevidence, and how it is handled: `CON-376`'s `Excludes` named "a
  fixed-length word query", excluding its sibling by the very value both records
  call a parameter. That standing conflict is removed by this change; the
  survivor's `Excludes` keeps the boundaries that remain real — unrestricted
  symbol sequences, typed semantic slots, clue-reuse rules and theme-set
  membership. `CON-377`, the Strands spanning-answer constraint, is untouched.

## Proposed change

- Old classification: two Constraint genes separated by the shape of the length
  bound.
- Proposed classification: one Constraint gene for a declared length predicate
  conjoined with lexicon membership.
- Definitions and boundaries: `CON-112` becomes "Declared-length lexicon
  membership gate", admits a query, answer or assistance credit, and states that
  a failing proposal consumes neither the attempt nor the assistance allowance.
  Exact and minimum bounds, language, lexicon, normalisation, inflection and
  proper-name policy, duplicate handling and rejection feedback are parameters.
- Lifecycle effects: `CON-376` becomes a `Merged` alias pointing to `CON-112`.
  Its stable ID is never reused.
- What does not change: `CON-377` remains the separate spanning-answer
  constraint. Whether an eligible word belongs to an authored theme answer set
  remains excluded from this gate and stays with the Strands objective and
  system records. `GAME-0068`'s signature is unchanged.

## Genome and combination impact

- Genes added, deprecated, merged or split: `CON-376` merged into `CON-112`.
  Active genes fall from 2,351 to 2,350; `Merged` records rise from 35 to 36;
  the 2,387 total definitions are unchanged.
- Games requiring annotation: `GAME-0156` (signature, constraint prose,
  normalised genome, stored signature line, preserved notes, a forward
  hypothesis and the delta summary).
- Combinations affected: `COMB-0154` substitutes `CON-112`. Its size stays at
  ten genes and it remains a strict proper subset of the twelve-gene
  `GAME-0156` genome. A global scan found no exact combination collision and no
  additional game whose genome now contains `COMB-0154`.
- Novelty claims affected: `CON-112` records the generalisation. `GAME-0156` now
  claims six new genes rather than seven.
- Comparison impact: none. `GAME-0156` keeps `GAME-0012` as its selected near
  neighbour at an unchanged `0.235294`, because no lower-ID game carries either
  gene. No exact genome match is created.

## Decision

- Decision: `Accepted`.
- Decided by: confirmed audit card `C-07` plus a fresh unit-level two-way
  transfer test over the complete Constraint registry.
- Rationale: the surviving Constraint accepts the same legality rule from both
  carriers once the length predicate's form is supplied as a parameter, which
  both records had already classified as a parameter of themselves.
- Implementation links: `CON-112`, `CON-376`, `CON-377`, `GAME-0068`,
  `GAME-0156`, `COMB-0154`.

## Change history

- 2026-09-06 — created and accepted as unit 4 of the confirmed taxonomy
  normalisation derived from `FULL_TAXONOMY_DUPLICATE_AUDIT_001`.
