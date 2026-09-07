# Taxonomy Change 029: Remove the affordability legality from SYS-808 and add no Constraint in its place

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-06
- Trigger: finding `R-01` of
  [`BATCH_015_GENE_CORRECTION_REVIEW_001`](../normalisation/BATCH_015_GENE_CORRECTION_REVIEW_001.md),
  priority `P0`
- Supersedes: the sentence of
  [`TAXONOMY_CHANGE_026`](TAXONOMY_CHANGE_026.md) that reads "the affordability
  clause stays inside `SYS-808`". That record's own decision — removing the
  income exclusivity — stands unchanged.

## Current classification

- Exact wording or stable IDs: `SYS-808` — Credit the shared defence budget from
  every destroyed hostile layer, whose definition also stated that "a placement
  or upgrade commitment is legal only within the balance that budget currently
  holds".
- Files and entries affected: the System Behaviour registry, Ukrainian gene
  localisation, the `GAME-0265` record, the `GAME-0265` plain-language cards and
  the web contract tests. `COMB-0263`'s gene set, the `GAME-0265` signature and
  every generated index are unaffected.
- Original evidence or rationale: `SYS-808` was isolated for `GAME-0265` Bloons
  TD 6, and `TAXONOMY_CHANGE_026` deliberately left the affordability clause in
  place while narrowing the gene's income claim.

## Detected problem

- What is incorrect: the gene joined two differently typed statements. The
  destruction-to-budget credit is a System transition; "a commitment is legal
  only within the current balance" is a legality rule, which
  [`knowledge/genes/README.md`](../../knowledge/genes/README.md) places on the
  Constraint side of the System/Constraint boundary. The governing correction
  prompt forbade exactly this, and the Ukrainian record repeated the same
  contamination.
- How the problem was found: independent review finding `R-01`.
- Why this changes the boundary rather than the wording: removing the clause
  removes a condition the gene asserted about every carrier. A ruleset that
  credits a budget from destroyed hostiles but never refuses a commitment for
  want of balance now carries `SYS-808`, and previously did not.

## Evidence

- Primary sources: the `GAME-0265` claim ledger and the canonical `SYS-808`,
  `ACT-130`, `CON-062` and `CON-608` records.
- The packet does not evidence the removed clause. `BTD-011` establishes that
  destroyed layers credit spendable cash and that the cash funds placements and
  upgrades. `BTD-016` establishes the further flat round credit. No claim, and
  no row of the reproducible transition table, establishes that a commitment is
  ever refused for insufficient balance. The two refusals this packet does
  evidence are the terrain rejection in `BTD-005` and the path cap in `BTD-006`,
  already carried by `CON-062` and `CON-608`.
- Cross-type scan: `ACT-130` — "the player spends current scoped currency to
  acquire one currently offered asset or execute one priced service" — is
  already in this signature and carries the purchase transition the record does
  evidence.
- Lower-ID Constraint scan: every Active Constraint below `CON-609` whose label
  or body mentions affordability, cost, price, balance, currency, funds,
  payment, purchase or budget was read. The nearest boundaries each add a second
  condition this packet does not have: `CON-171` municipal solvency with
  recurring service budgets, `CON-174` a card cost with target eligibility,
  `CON-180` a lane plus a declared cost, `CON-191` a predecessor level,
  `CON-234` a one-off research price, `CON-248` a recurring balance, `CON-261` a
  buy window and spawn area, `CON-303` a creation point balance, `CON-409`
  ledger unlocks, `CON-417` city unlocks and capacity, `CON-445` a tiered stock.
  No reviewed Constraint states a bare balance gate.
- Counterevidence, and how it is handled: it is obviously true of the product
  that a tower cannot be bought without money. That is not the question. The
  question is whether this bounded packet's evidence establishes the refusal, and
  it does not, so asserting it would be an unsourced claim in either type.

## Proposed change

- Old classification: a System gene stating both an automatic credit and a
  commitment legality.
- Proposed classification: the same System gene reduced to the automatic credit.
  Its `Excludes` now states explicitly that it asserts no legality and that
  whether a commitment is refused for want of balance is a Constraint question
  it does not answer.
- No Constraint is created. A bare "the commitment must fit the current balance"
  gate has no evidence in this packet, and introducing it as a portable gene
  would silently apply to a large number of unaudited economy carriers. It stays
  a recorded gap and a future audit candidate.
- Lifecycle effects: none. `SYS-808` stays `Active` and no ID is retired,
  retyped or reused.
- What does not change: the `GAME-0265` signature of fifteen genes; `COMB-0263`'s
  thirteen genes and its strict-subset relation; `ACT-130`, `CON-062` and
  `CON-608`; `SYS-806`, `SYS-807` and `SYS-809`; every comparison score and
  selected neighbour.

## Genome and combination impact

- Genes added, deprecated, merged or split: none. Totals stay at 2,387
  definitions, 2,343 `Active`, 43 `Merged` and 1 `Deprecated`.
- Games requiring annotation: `GAME-0265` — the system prose, the Constraint
  section, the negative results, the taxonomy impact and the delta summary, plus
  its plain-language `SYS-808` card in both languages.
- Combinations affected: none by gene set. `COMB-0263`'s prose already describes
  the budget as what upgrades are bought from rather than as a legality.
- Novelty claims affected: `SYS-808` records the second narrowing.
- Comparison impact: none. No signature changed.

## Decision

- Decision: `Accepted`.
- Decided by: review finding `R-01`, a cross-type scan, a complete lower-ID
  Constraint scan and the packet's own claim ledger.
- Rationale: a System gene may not hold a legality rule, and the honest
  resolution here is subtraction rather than substitution — the affordability
  rule the audit went looking for is not evidenced by this record at all.
- Implementation links: `SYS-808`, `ACT-130`, `CON-062`, `CON-608`, `GAME-0265`,
  `COMB-0263`, `TAXONOMY_CHANGE_026`.

## Change history

- 2026-09-06 — created and accepted as unit 1 of the batch-015 gene correction
  follow-up.
