# Taxonomy Change 026: Remove the unestablished income exclusivity from SYS-808

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-06
- Trigger: finding `A-05` of
  [`BATCH_015_GENE_AUDIT_001`](../normalisation/BATCH_015_GENE_AUDIT_001.md),
  disposition `BOUNDARY-AND-EVIDENCE-REVIEW`

## Current classification

- Exact wording or stable IDs: `SYS-808` — Fund the defence budget solely from
  destroyed hostile layers.
- Files and entries affected: the System Behaviour registry, Ukrainian gene
  localisation, the `GAME-0265` record, `COMB-0263`, the generated indexes and
  the deterministic research artifacts.
- Original evidence or rationale: `SYS-808` was isolated for `GAME-0265` Bloons
  TD 6. Its definition asserted that the destroyed-layer credit "is the only
  source funding further placements and upgrades" and that the hostiles are
  "the defence's entire income".

## Detected problem

- What is incorrect: the exclusivity is not established by the record's own
  evidence and is contradicted by the evidence obtained for this correction.
  `BTD-011` established only that destroyed layers credit cash and that cash
  funds placements and upgrades. Nothing in `BTD-003`–`BTD-014` established
  that no other credit path exists, yet the gene, the scope prose, `BTD-015`,
  the transition table and `COMB-0263` all strengthened the sourced claim into
  "only income".
- How the problem was found: the batch-015 gene audit, finding `A-05`.
- Why this changes the boundary rather than the wording: "only" is a universal
  negative over the whole ruleset. A gene that asserts it is falsified by any
  further credit path, and the corrected evidence supplies one.

## Evidence

- Primary sources: none of the publisher's own material documents the income
  model, and the game itself was not played.
- New retrieved evidence: [static income
  reference](https://topper64.co.uk/nk/btd6/income), fetched and read in full on
  2026-09-06, states that the player receives "$1 for every pop" and "$100+n for
  completing round n", and that "secondary sources of income can be provided by
  farms and certain upgrades of other towers". The round-completion credit is
  unconditional and applies on every difficulty, so it is inside the declared
  `Easy` standard route.
- Source-family correction: `S2`, `S4`, `S5`, `S6` and `S7` of the `GAME-0265`
  record are five pages of `bloons.fandom.com` and are one corroborating family.
  `S3`, the Steam guide, was retrieved in full for this correction and documents
  no income mechanics at all, so it cannot support `BTD-011` either. The new
  `S8` is the only fetched complete page and is a different family.
- Counterevidence, and how it is handled: none was found for the existence of
  the round-completion credit. The remaining uncertainty is its exact formula,
  which is why `BTD-016` is recorded at `Limited` evidence and `Medium`
  confidence rather than promoted.

## Proposed change

- Old classification: a System gene whose identity included the claim that the
  destroyed-layer credit is the ruleset's only income.
- Proposed classification: the same System gene narrowed to the transition it
  actually names — the destruction-to-budget conversion plus the legality of a
  commitment against the balance that conversion produces.
- Definitions and boundaries: `SYS-808` becomes "Credit the shared defence
  budget from every destroyed hostile layer". Its `Excludes` now states
  explicitly that the boundary does not assert the absence of other credit
  paths, and its `Parameters` admit "any further credit paths the ruleset
  settles outside this transition".
- Lifecycle effects: none. `SYS-808` stays `Active` and no ID is retired.
- What does not change: `SYS-806`, `SYS-807` and `SYS-809` keep their
  boundaries; the `GAME-0265` signature and `COMB-0263`'s gene set are
  unchanged; the affordability clause stays inside `SYS-808`.

## Genome and combination impact

- Genes added, deprecated, merged or split: none. Totals are unchanged at 2,387
  definitions, 2,343 `Active`, 43 `Merged` and 1 `Deprecated`.
- Games requiring annotation: `GAME-0265` — scope loop, claim ledger including
  the new `BTD-016`, sources, system prose, transition table, negative results,
  adjacent-systems row and delta summary.
- Combinations affected: `COMB-0263` keeps its thirteen genes and its single
  carrier; its title, novelty assessment, decision structure and match boundary
  drop the same exclusivity.
- Novelty claims affected: `SYS-808` records the narrowing. `COMB-0263`'s
  novelty now claims the weaker and supportable form — the only income the
  player's own decisions can raise.
- Comparison impact: none. No signature changed, so no Jaccard score or selected
  neighbour moves.

## Decision

- Decision: `Accepted`.
- Decided by: audit finding `A-05` plus newly retrieved complete-page evidence.
- Rationale: the gene's distinctive content is that destroying a hostile is what
  pays for the defence that destroys it. That survives intact. The universal
  negative attached to it was never evidenced and is false.
- Implementation links: `SYS-808`, `SYS-806`, `SYS-807`, `SYS-809`,
  `GAME-0265`, `COMB-0263`.

## Change history

- 2026-09-06 — created and accepted as unit 2 of the batch-015 gene correction
  run.
