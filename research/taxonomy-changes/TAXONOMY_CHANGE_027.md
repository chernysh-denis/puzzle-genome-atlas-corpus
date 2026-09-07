# Taxonomy Change 027: Remove the SYS-592 reuse from the bounded DREDGE route

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-06
- Trigger: findings `A-04` and `A-11` of
  [`BATCH_015_GENE_AUDIT_001`](../normalisation/BATCH_015_GENE_AUDIT_001.md),
  disposition `SIGNATURE-REVIEW`

## Current classification

- Exact wording or stable IDs: `SYS-592` — Advance sanity and hostile shadow
  manifestation, carried by `GAME-0186` Don't Starve Together and, at
  integration, by `GAME-0269` DREDGE.
- Files and entries affected: the `GAME-0269` record, gene salience,
  plain-language presentation, the generated indexes, the comparison artefacts
  and the web contract tests. `SYS-592`'s own definition, lifecycle and
  Ukrainian record are untouched.
- Original evidence or rationale: the DREDGE unit reused `SYS-592` because
  darkness raises a visible panic meter that light, daylight and resting lower,
  and because the route's deadline is defined against that meter beginning to
  rise.

## Detected problem

- What is incorrect: `SYS-592`'s transition is not "a mental-state meter
  moves". Its definition requires that "low thresholds alter perception and make
  shadow creatures present and eventually physically hostile", and its
  `Includes` cites below-fifteen-percent shadow creatures becoming aggressive.
  The DREDGE record's own declared scope excludes "night encounters, obelisks
  and every panic consequence beyond the meter's rise", and states that the
  successful route does not enter those thresholds. The defining half of the
  reused boundary is therefore neither executed nor verified in this packet.
- How the problem was found: the batch-015 gene audit, findings `A-04` and
  `A-11`.
- Why this changes the signature rather than the wording: ADR-007 admits a
  mechanic that is causally relevant to the bounded terminal, but causal
  relevance does not waive the gene's own transition. Retaining `SYS-592` here
  would let any product with a rising meter claim a threshold-and-hostility
  boundary it never reaches.

## Evidence

- Primary sources: the `GAME-0269` record's declared scope and route, which
  state the exclusion and the non-entry directly.
- Reproducible transitions: the record's own transition table has one panic row.
  It read "the panic level begins to rise and the display distorts", but
  distortion is a `DRG-012` high-panic consequence, not an onset consequence, so
  that row overstated its own claims. It is corrected in this unit to state the
  boundary hour and its effect on the terminal.
- Analysed games checked: a lower-ID scan over every Active System gene
  mentioning sanity, stress, panic, fear, morale, a rising meter or exposure
  returned `SYS-190`, `SYS-198`, `SYS-226`, `SYS-311`, `SYS-321`, `SYS-327`,
  `SYS-338`, `SYS-593` and `SYS-621`. Every one resolves its meter into a
  consequence this route excludes, so none can be reused as a narrower
  replacement.
- Counterevidence, and how it is handled: the deadline the meter signals is
  real and remains represented. `SYS-816` advances the clock the player spends,
  `CON-612` bounds the return and `OBJ-163` defines the terminal against the
  boundary hour. What is removed is the claim to a threshold-and-hostility
  transition, not the deadline.

## Proposed change

- Old classification: `GAME-0269` reuses `SYS-592`.
- Proposed classification: `GAME-0269` does not carry a mental-state gene. No
  replacement gene is created, because a transition whose entire admitted
  content is "a number starts moving, with no consequence inside the packet" is
  not decision-bearing.
- Definitions and boundaries: unchanged. `SYS-592` keeps its definition,
  lifecycle, Ukrainian record and its `GAME-0186` carrier.
- Lifecycle effects: none.
- What does not change: `GAME-0186`'s signature, `COMB-0267`'s gene set — it
  never contained `SYS-592` — and every other batch-015 record.

## Genome and combination impact

- Genes added, deprecated, merged or split: none. Totals stay at 2,387
  definitions, 2,343 `Active`, 43 `Merged` and 1 `Deprecated`. `SYS-592` falls
  from two carriers to one.
- Games requiring annotation: `GAME-0269` — signature, system prose, resolution
  order, transition table, normalised genome, preserved notes, lower-ID scan,
  adjacent-systems row, taxonomy impact, negative results and delta summary,
  plus its salience partition and plain-language cards.
- Combinations affected: none. `COMB-0267` keeps its eleven genes and remains a
  strict proper subset of the now fifteen-gene genome.
- Novelty claims affected: the record no longer claims to share Don't Starve
  Together's mental-state meter.
- Comparison impact: `GAME-0269`'s genome falls from sixteen to fifteen genes,
  so its `genome-jaccard-v1` scores against every earlier signature are
  recomputed and its selected near neighbour is re-derived.

## Decision

- Decision: `Accepted`.
- Decided by: audit findings `A-04` and `A-11` plus a lower-ID replacement scan.
- Rationale: a bounded route may not claim a gene whose defining transition it
  declares out of scope.
- Implementation links: `SYS-592`, `SYS-816`, `CON-612`, `OBJ-163`,
  `GAME-0186`, `GAME-0269`, `COMB-0267`.

## Change history

- 2026-09-06 — created and accepted as unit 6 of the batch-015 gene correction
  run.
