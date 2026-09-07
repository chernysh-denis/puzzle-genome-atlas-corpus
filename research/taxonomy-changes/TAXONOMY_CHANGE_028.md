# Taxonomy Change 028: Remove the INF-236 reuse from Risk of Rain 2 and restate CON-613 as a legality rule

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-06
- Trigger: findings `A-03` and `A-13` of
  [`BATCH_015_GENE_AUDIT_001`](../normalisation/BATCH_015_GENE_AUDIT_001.md),
  dispositions `SIGNATURE-REVIEW` and `SPLIT-AND-TYPE-REVIEW`

## Current classification

- Exact wording or stable IDs: `INF-236` — Survival HUD exposes clock, level and
  run-build progression, carried by `GAME-0183` Vampire Survivors and, at
  integration, by `GAME-0270` Risk of Rain 2; `CON-613` — Interactable prices
  rise with the same value that raises the threat, carried by `GAME-0270`.
- Files and entries affected: the Constraint registry, the `GAME-0270` record,
  gene salience, plain-language presentation, Ukrainian gene localisation, the
  generated indexes, the comparison artefacts and the web contract tests.
  `INF-236`'s own definition, lifecycle and Ukrainian record are untouched.
- Original evidence or rationale: `GAME-0270` reused `INF-236` for "the run
  clock, the survivor's level and experience progress and the retained modifier
  build together", and introduced `CON-613` for the coefficient-derived price.

## Detected problem

Two independent defects in one signature, resolved in one unit because they
share a record but decided separately.

- **`INF-236` is conjunctive and this record satisfies only part of it.** Its
  definition requires the survival clock, a kill count, level and experience
  progress, the retained weapon and passive-item build, and item levels
  available for inspection. `ROR-001`–`ROR-015` establish none of the kill
  count, the retained weapon display or the inspectable item levels; in fact no
  claim in the record covers the run HUD's contents at all except `ROR-009`,
  which covers the escalation tier. Matching selected clauses of a conjunctive
  boundary is not carrying it.
- **`CON-613`'s content was a system relationship under a Constraint type.** Its
  definition stated that a price "is computed from the run's current escalation
  value", with the reward multiplier scaling from it too. That is an automatic
  computation, which
  [`knowledge/genes/README.md`](../../knowledge/genes/README.md) places on the
  System side of the System/Constraint boundary. The only Constraint content in
  it was implicit.

## Evidence

- Primary sources: the `GAME-0270` claim ledger and the canonical `INF-236` and
  `CON-613` records.
- Analysed games checked: a cross-type scan preceded the `CON-613` decision.
  `SYS-817` already carries the escalation value that produces both the price
  and the reward multiplier, so the computation has a System home and needs no
  new gene. No lower-ID Constraint ties a purchase's legality to a value that
  simultaneously strengthens the opposition: `CON-177` and `CON-210` bound
  carried capacity, `CON-248` requires a recurring balance, `CON-261` a buy
  window and location, `CON-417` city unlocks and capacity.
- Counterevidence, and how it is handled: generalising or splitting `INF-236` to
  fit Risk of Rain 2 was rejected outright, because `GAME-0183` Vampire
  Survivors does satisfy every clause and its boundary must not be rewritten to
  accommodate a partial match. Creating a replacement run-HUD gene was rejected
  because this record's evidence does not establish one; the absence is recorded
  as an evidence gap instead.

## Proposed change

- Old classification: `GAME-0270` reuses `INF-236`; `CON-613` states a price
  computation.
- Proposed classification: `GAME-0270` carries no run-HUD Information gene, and
  `INF-327` continues to carry the one disclosure its evidence establishes.
  `CON-613` becomes "A purchase requires covering a price set by the run's
  escalation value" and states the legality directly, naming the computation in
  its `Excludes` as `SYS-817` system content.
- Lifecycle effects: none. No ID is retired, retyped by ID or reused.
- What does not change: `INF-236`'s definition, lifecycle and Ukrainian record;
  `GAME-0183`'s signature; `SYS-817`'s boundary and wording; `SYS-818`, which
  this unit reviewed split-first and retained with four further named
  exclusions; `COMB-0268`'s gene set, which never contained `INF-236`.

## Genome and combination impact

- Genes added, deprecated, merged or split: none. Totals stay at 2,387
  definitions, 2,343 `Active`, 43 `Merged` and 1 `Deprecated`. `INF-236` falls
  from two carriers to one.
- Games requiring annotation: `GAME-0270` — signature, information and
  constraint prose, normalised genome, preserved notes, taxonomy impact,
  negative results and delta summary, plus its salience partition and
  plain-language cards.
- Combinations affected: none. `COMB-0268` keeps its eight genes and remains a
  strict proper subset of the now fourteen-gene genome.
- Novelty claims affected: the record no longer claims Vampire Survivors' HUD
  boundary. `CON-613`'s novelty now states a legality that moves while the
  player decides.
- Comparison impact: `GAME-0270`'s genome falls from fifteen to fourteen genes,
  so its `genome-jaccard-v1` scores are recomputed and its selected near
  neighbour re-derived.

## Decision

- Decision: `Accepted`.
- Decided by: audit findings `A-03` and `A-13`, a cross-type scan and an
  explicit type-boundary decision.
- Rationale: a record may not claim a conjunctive boundary it satisfies in part,
  and a gene's type must match the content it states.
- Implementation links: `INF-236`, `INF-327`, `CON-613`, `SYS-817`, `SYS-818`,
  `GAME-0183`, `GAME-0270`, `COMB-0268`.

## Change history

- 2026-09-06 — created and accepted as unit 7 of the batch-015 gene correction
  run.
