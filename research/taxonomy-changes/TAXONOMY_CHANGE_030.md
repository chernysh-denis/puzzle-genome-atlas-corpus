# Taxonomy Change 030: Move the coefficient-driven price and reward into SYS-817 and deprecate CON-613

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-06
- Trigger: finding `R-02` of
  [`BATCH_015_GENE_CORRECTION_REVIEW_001`](../normalisation/BATCH_015_GENE_CORRECTION_REVIEW_001.md),
  priority `P0`
- Supersedes: the statements in
  [`TAXONOMY_CHANGE_028`](TAXONOMY_CHANGE_028.md) that "`SYS-817` already
  carries the escalation value that produces both the price and the reward
  multiplier, so the computation has a System home and needs no new gene" and
  that `SYS-817`'s "boundary and wording" do not change. Both were false when
  written. That record's `INF-236` decision is unaffected and stands.

## Current classification

- Exact wording or stable IDs: `SYS-817` — Escalate run threat from elapsed time
  rather than from progress, whose definition covered hostile level, health and
  damage and the director spawn budget only; `CON-613` — A purchase requires
  covering a price set by the run's escalation value, whose `Excludes` delegated
  the price and reward computation to `SYS-817`.
- Files and entries affected: the System Behaviour and Constraint registries,
  Ukrainian gene localisation, the `GAME-0270` record and its signature,
  `COMB-0268`, gene salience, plain-language presentation, the generated
  indexes, the comparison artefacts and the web contract tests.
- Original evidence or rationale: both genes were isolated for `GAME-0270` Risk
  of Rain 2, and `TAXONOMY_CHANGE_028` restated `CON-613` as a legality while
  asserting that its computation already had a System home.

## Detected problem

- What is incorrect: the delegation had no destination. `SYS-817`'s definition,
  includes, excludes and parameters named the level, health, damage and spawn
  budget outputs and nothing about prices or rewards, so a Constraint's
  `Excludes` pointed at content the System gene did not state. A reader
  following the pointer found nothing, and `TAXONOMY_CHANGE_028` asserted the
  opposite in writing.
- Second defect, exposed once the first is fixed: with the computation named
  where it belongs, what `CON-613` still asserted was a bare affordability gate.
- How the problem was found: independent review finding `R-02`.
- Why this changes boundaries rather than wording: `SYS-817` gains two outputs
  it did not claim, so a ruleset that escalates threat without pricing the world
  no longer carries the whole gene as stated, and `GAME-0270`'s signature loses
  a Constraint.

## Evidence

- Primary sources: the `GAME-0270` claim ledger and the canonical `SYS-817`,
  `CON-613` and `ACT-130` records.
- `ROR-008` — "Interactable prices are computed from the same coefficient, and
  the gold a defeated hostile pays is multiplied by it" — is `Observation` /
  `Corroborated` / `High`, exactly the grade of `ROR-006` and `ROR-007`, which
  the System gene already carried. The transition table states the same
  relationship: as the escalation value rises, an interactable's price is higher
  than the same class cost earlier while defeated hostiles pay more gold. The
  expansion adds no claim the record did not already hold.
- The record does not evidence a refusal. Its only purchase row is "enough
  currency is held, pay at the interactable", which resolves to the currency
  being spent and one modifier taken. No claim and no row establishes that a
  purchase is ever refused for want of gold, so the residual legality is
  unsupported here in either type.
- Lower-ID System scan for a coefficient-driven price or reward: `SYS-378`
  scales enemy, loot and vendor tiers to the character's own level; `SYS-054`
  escalates on completing a circuit; `SYS-572` releases authored waves at
  scheduled minutes; `SYS-178` accumulates pressure from expansion. None ties a
  price or a reward to a time-funded value that also arms the opposition, so no
  lower-ID System gene can take the content and expanding `SYS-817` is the
  narrowest correct home.
- Lower-ID Constraint rescan for a portable remainder: `CON-177` and `CON-210`
  bound carried capacity, `CON-248` requires a recurring balance, `CON-261` a
  buy window and location, `CON-417` city unlocks and capacity. None states a
  bare balance gate, and this run has already declined to create one for
  `GAME-0265` under [`TAXONOMY_CHANGE_029`](TAXONOMY_CHANGE_029.md) on the same
  reasoning. `ACT-130` carries the purchase transition both records evidence.
- Counterevidence, and how it is handled: `CON-613` could have been kept by
  reading its distinctive content as "the legality threshold moves while the
  player deliberates". That was rejected because the movement belongs to the
  price, which is now System content, leaving the Constraint with a bare
  balance condition the packet never evidenced. Keeping the gene to preserve a
  genome count is explicitly not a reason.

## Proposed change

- Old classification: a System gene covering threat outputs only, plus a
  Constraint holding a computation and an unevidenced legality.
- Proposed classification: `SYS-817` becomes "Escalate run threat, prices and
  rewards from elapsed time rather than from progress" and states all four
  outputs the coefficient drives, while its `Excludes` says explicitly that the
  legality of any individual purchase is a Constraint question it does not
  answer. `CON-613` becomes `Deprecated`, keeps its heading as an auditable
  alias, and carries a `Deprecation` line naming this record.
- Lifecycle effects: `CON-613` moves from `Active` to `Deprecated`. No ID is
  retyped, reused or merged into another gene; a Constraint cannot be merged
  into a System gene, so no survivor field is recorded.
- What does not change: `INF-236`'s definition and `GAME-0183`'s signature;
  `SYS-818`, `INF-327`, `OBJ-164`, `CON-269` and `ACT-130`; the `GAME-0270`
  scope, ledger and terminal.

## Genome and combination impact

- Genes added, deprecated, merged or split: one deprecation. Totals become 2,387
  definitions, 2,342 `Active`, 43 `Merged` and 2 `Deprecated`.
- Games requiring annotation: `GAME-0270` — front matter, the system and
  constraint prose, the normalised genome table, the taxonomy impact, the
  negative results and the delta summary, plus its salience partition and
  plain-language cards.
- Combinations affected: `COMB-0268` falls from eight genes to seven and remains
  a strict proper subset of the now thirteen-gene genome. Its identity is
  unchanged, because the pricing it describes is now carried by `SYS-817`.
- Novelty claims affected: `SYS-817` records the expansion; `CON-613` records
  the deprecation.
- Comparison impact: `GAME-0270`'s genome falls from fourteen genes to thirteen,
  so its `genome-jaccard-v1` scores are recomputed. The selected near neighbour
  stays `GAME-0251` Hades and its score moves from `8 / 36 = 0.222222` to
  `8 / 35 = 0.228571`.

## Decision

- Decision: `Accepted`.
- Decided by: review finding `R-02`, a lower-ID System scan, a lower-ID
  Constraint rescan and the record's own claim ledger.
- Rationale: a delegation must have a destination, and a type must match its
  content. Putting the computation where it belongs leaves nothing portable
  behind, and the corpus does not invent a gene to fill the hole.
- Implementation links: `SYS-817`, `CON-613`, `ACT-130`, `GAME-0270`,
  `COMB-0268`, `TAXONOMY_CHANGE_028`, `TAXONOMY_CHANGE_029`.

## Change history

- 2026-09-06 — created and accepted as unit 2 of the batch-015 gene correction
  follow-up.
