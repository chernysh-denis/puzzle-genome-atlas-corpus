# Taxonomy Change 023: Merge the sector-majority reinforcement gene into the committed-defeat ticket boundary

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-06
- Trigger: card `C-10` of
  [`FULL_TAXONOMY_DUPLICATE_AUDIT_001`](../normalisation/FULL_TAXONOMY_DUPLICATE_AUDIT_001.md),
  disposition `CONFIRMED`, routed as the first half of implementation target
  `T-06`

## Current classification

- Exact wording or stable IDs: `SYS-396` — Aggregate Conquest pressure into
  reinforcement tickets; `SYS-743` — Convert committed defeats and sector
  majority into reinforcement loss.
- Files and entries affected: the System Behaviour registry, Ukrainian gene and
  combination localisation, the `GAME-0234` signature and prose, `COMB-0232`,
  `COMB-0147`, the generated game and combination indexes, gene salience,
  plain-language presentation, the deterministic research artifacts and the web
  contract tests.
- Original evidence or rationale: `SYS-396` was isolated for `GAME-0149`
  Battlefield 6 and reused by `GAME-0220` Battlefield V. `SYS-743` was isolated
  for `GAME-0234` Battlefield 2042, whose unit explicitly rejected `SYS-396`
  because "it encodes continuous drain for each held control point, whereas this
  packet first resolves all-point sectors and then checks sector majority".

## Detected problem

- What is incorrect: both records state the same transition — a finite per-team
  reinforcement pool is debited once for each committed unrevived defeat and
  repeatedly debited for the opposing side while a declared map-control
  condition holds, and the match ends when either pool reaches zero.
- How the problem was found: the full taxonomy duplicate audit, card `C-10`,
  confirmed by independent review.
- Why this changes decision structure rather than terminology: the sole
  difference is the shape of the bleed predicate — "for every currently owned
  control point" versus "while one side controls a majority of the map's
  sectors". That is an aggregation rule over the same control state, evaluated
  at the same cadence, debiting the same resource, settling at the same
  threshold. The player's authority, the state transition, the timing, the
  information available, the eligibility rule, the persistence and the
  settlement are identical. The rejection recorded in `GAME-0234` mistook the
  predicate's arity for a boundary.

## Evidence

- Primary sources: the reviewed `GAME-0149`, `GAME-0220` and `GAME-0234`
  records and their source ledgers.
- Reproducible transitions: in all three packets a bled-out unrevived soldier
  debits exactly one ticket from that soldier's team, the opposing pool falls at
  a declared cadence while the map-control predicate holds, and the first pool
  to reach zero settles the match.
- Analysed games checked: a fresh unit-level two-way transfer scan over all 805
  Active System genes. `SYS-396` is the nearest System to `SYS-743` at 0.460
  with the next candidate at 0.163, and `SYS-743` is the nearest System to
  `SYS-396` at 0.460 with the next candidate at 0.182. The pair is mutually
  nearest by a wide margin and no third System is a better survivor.
- Counterevidence, and how it is handled:
  - `SYS-742`, which groups control points into all-owned sectors, is a
    genuinely separate ownership rule and is untouched. The survivor's
    `Excludes` now names it so the ticket boundary cannot absorb the
    aggregation that feeds it.
  - `SYS-583` scored 0.182 and is the closest surviving neighbour. It also
    drains in proportion to a control majority, but it debits **destroyed
    vehicles** rather than committed personnel defeats and adds a second
    terminal — no player able to spawn a ground vehicle. Those are eligibility
    and settlement differences, not a parameter, so it is recorded as a new
    candidate rather than merged, and the survivor's `Excludes` names it.
  - `SYS-643` and `SYS-644` remain distinct: the first moves the legal combat
    front between sectors, the second replenishes an attacker-only pool at
    sector boundaries. Both are named in the survivor's `Excludes`.
  - `SYS-561` remains distinct: it converts a single resettable Control point
    into a percentage round win rather than into a finite team pool.
- External systems or literature checked: none beyond the three products' own
  published rules.

## Proposed change

- Old classification: two System genes separated by the arity of the
  map-control predicate that sustains the bleed.
- Proposed classification: one System gene for converting committed defeats and
  held map control into reinforcement loss.
- Definitions and boundaries: `SYS-396` becomes "Convert committed defeats and
  held map control into reinforcement loss". The committed-defeat debit, the
  finite pool and the zero-pool settlement are the boundary. Teams, initial
  tickets, death debit, the map-control predicate and its form, drain cadence,
  drain magnitude, simultaneous updates, zero threshold and result are
  parameters.
- Lifecycle effects: `SYS-743` becomes a `Merged` alias pointing to `SYS-396`.
  Its stable ID is never reused.
- What does not change: `SYS-742`, `SYS-583`, `SYS-643`, `SYS-644` and
  `SYS-561` keep their boundaries and lifecycles. The `GAME-0149` and
  `GAME-0220` signatures are unchanged. The survivor's claim status stays
  `Observation`: this merge removes a duplicate, it does not add evidence about
  any carrier.

## Genome and combination impact

- Genes added, deprecated, merged or split: `SYS-743` merged into `SYS-396`.
  Active genes fall from 2,348 to 2,347; `Merged` records rise from 38 to 39;
  the 2,387 total definitions are unchanged.
- Games requiring annotation: `GAME-0234` (signature, combination list, system
  prose, normalised genome, corpus comparison, selected-neighbour
  interpretation, preserved notes, taxonomy impact, negative results and the
  delta summary).
- Combinations affected: `COMB-0232` substitutes `SYS-396`, stays at thirteen
  genes and remains a strict proper subset of the forty-six-gene `GAME-0234`
  genome.
- **Second-order combination consequence, beyond the audit's estimate.** The
  audit projected "one game signature, one combination". A global recomputation
  shows that with `SYS-396` in its signature, `GAME-0234`'s genome now properly
  contains all twenty-six genes of `COMB-0147` — the Battlefield 6 and
  Battlefield V squad-combined-arms combination. The repository's standing
  invariant is that a combination's declared supporters equal the set of games
  whose genome contains it, so `GAME-0234` is registered as `COMB-0147`'s third
  supporter, its `Supported combination subsets` line and `combination_ids` are
  updated, and `COMB-0147`'s interaction text, novelty assessment, additional
  support and Ukrainian record are generalised from "each owned point" to the
  held-map-control predicate. `COMB-0147`'s gene set itself is unchanged, and
  the distinctive Battlefield 2042 relation stays in `COMB-0232`.
- Novelty claims affected: `SYS-396` records the generalisation. `GAME-0234` now
  claims eleven new genes rather than twelve. `COMB-0147`'s recurrence moves
  from "unassessed" to established across three signatures.
- Comparison impact: `GAME-0234`'s selected near neighbour stays `GAME-0149`,
  whose shared-gene count rises from thirty-four to thirty-five and whose score
  rises from `34 / 47 = 0.723404` to `35 / 46 = 0.760870`. No other selected
  neighbour moves. The only exact genome collision in the corpus remains the
  pre-existing, correctly recorded `GAME-0009` / `GAME-0109` pair, which this
  change does not touch.

## Decision

- Decision: `Accepted`.
- Decided by: confirmed audit card `C-10` plus a fresh unit-level two-way
  transfer test over the complete System Behaviour registry.
- Rationale: the surviving System accepts all three carriers' ticket rules once
  the map-control predicate's form is supplied as a parameter, and the standing
  `Excludes` conflict between the two records — each naming the other's bleed
  shape — is removed.
- Implementation links: `SYS-396`, `SYS-743`, `SYS-742`, `SYS-583`, `SYS-643`,
  `SYS-644`, `GAME-0149`, `GAME-0220`, `GAME-0234`, `COMB-0147`, `COMB-0232`.

## Change history

- 2026-09-06 — created and accepted as unit 6 of the confirmed taxonomy
  normalisation derived from `FULL_TAXONOMY_DUPLICATE_AUDIT_001`.
