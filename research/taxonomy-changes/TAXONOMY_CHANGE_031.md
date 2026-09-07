# Taxonomy Change 031: Remove the unexecuted ACT-261 reuse from Undertale and withdraw the admission rule that authorised it

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-06
- Trigger: finding `R-04` of
  [`BATCH_015_GENE_CORRECTION_REVIEW_001`](../normalisation/BATCH_015_GENE_CORRECTION_REVIEW_001.md),
  priority `P1`
- Supersedes: the closure of `BATCH_015_GENE_AUDIT_001` finding `A-09` by the
  corrective run's unit 5, which admitted `ACT-261` under a corpus-wide rule it
  wrote in the same unit.

## Current classification

- Exact wording or stable IDs: `ACT-261` — Execute one prompted skilful timing
  input, carried by `GAME-0161` Dead by Daylight, `GAME-0268` Undertale and
  `GAME-0269` DREDGE; and the `RESEARCH_PRINCIPLES.md` section "Available
  actions the declared route does not execute".
- Files and entries affected: the Action registry's `Additional support` line,
  Ukrainian gene localisation, `docs/RESEARCH_PRINCIPLES.md`, the `GAME-0268`
  record and its signature, `COMB-0266`, gene salience, plain-language
  presentation, the generated indexes, the `GAME-0268` and `GAME-0269`
  comparison artefacts and the web contract tests.
- Original evidence or rationale: `UND-005` evidences that the Undertale attack
  option resolves damage by where a moving marker is stopped, which fits
  `ACT-261`'s boundary exactly.

## Detected problem

- What is incorrect: the declared successful route never executes the attack, so
  the Action is not a verb this packet's route performs. The previous unit
  admitted it by writing a new four-condition corpus-wide admission rule into
  `RESEARCH_PRINCIPLES` and applying that rule to the case that motivated it.
- Why that is a governance problem, not a wording problem: the rule changes what
  a genome signature means for every game in the corpus, prospectively.
  `RESEARCH_PRINCIPLES` requires an ADR for architecture changes and
  `ARCHITECTURE.md` requires a concrete integrity failure plus an ADR for
  structural changes. No ADR and no explicit maintainer decision existed. A
  useful written rule is not an authorised rule.
- How the problem was found: independent review finding `R-04`.

## Evidence

- Primary sources: the `GAME-0268` record's own scope, negative results and
  claim ledger, and the canonical `ACT-261`, `ACT-019`, `OBJ-162` and `CON-611`
  records.
- The record states in two places that the declared route does not execute the
  attack option, and the route's positive terminal is a reload-verified zero
  defeat count. No claim establishes that the route performs the input.
- Nothing is lost by removal. `ACT-019` — select one of the encounter's declared
  options, including per-monster sub-options — already carries the presence of
  the destructive option among the choices. `OBJ-162` carries the zero-defeat
  terminal and `CON-611` the earned release legality, so the decision the packet
  is about remains fully stated. `UND-005` remains in the ledger as evidence of
  what the refused option would resolve to.
- Counterevidence, and how it is handled: the four conditions genuinely hold for
  this packet, which is why the rule was attractive. That is preserved rather
  than discarded, as the `Proposed`
  [`ADR-013`](../../docs/architecture-decisions/ADR-013-unexecuted-action-admission.md),
  which explicitly authorises nothing until a maintainer accepts it.

## Proposed change

- Old classification: `GAME-0268` reuses `ACT-261`; `RESEARCH_PRINCIPLES` states
  a corpus-wide unexecuted-Action admission rule.
- Proposed classification: `GAME-0268` carries no timing-input Action; the rule
  is withdrawn from `RESEARCH_PRINCIPLES` and preserved as a `Proposed` ADR.
- Lifecycle effects: none. `ACT-261` stays `Active` with its definition,
  parameters and Ukrainian record intact, and falls from three carriers to two.
- What does not change: `GAME-0161` and `GAME-0269` keep `ACT-261`;
  `COMB-0159` and `COMB-0267` keep their gene sets; `ACT-019`, `OBJ-162` and
  `CON-611` are untouched.

## Genome and combination impact

- Genes added, deprecated, merged or split: none. Totals stay at 2,387
  definitions, 2,342 `Active`, 43 `Merged` and 2 `Deprecated`.
- Games requiring annotation: `GAME-0268` — front matter, scope inclusions,
  action prose, normalised genome, preserved notes, taxonomy impact and negative
  results, plus its salience partition and plain-language cards. `GAME-0269`
  requires a new selected-neighbour interpretation.
- Combinations affected: `COMB-0266` falls from eleven genes to ten and remains
  a strict proper subset of the now seventeen-gene genome. Its identity is
  unchanged: the destructive option enters the pattern through `ACT-019`.
- Novelty claims affected: none. `COMB-0266`'s novelty is the earned reward-free
  release, not the attack input.
- Comparison impact: `GAME-0268` falls from eighteen genes to seventeen, so its
  scores are recomputed; the selected neighbour stays `GAME-0259` Dead Space
  (2023 remake) and moves from `8 / 45 = 0.177778` to `8 / 44 = 0.181818`.
  `GAME-0269` DREDGE loses its selected neighbour: Undertale was selected at
  `4 / 29 = 0.137931` on a set that included `ACT-261`, and the new tied
  selection is `GAME-0224` Once Human and `GAME-0228` A Way Out at
  `3 / 26 = 0.115385`.

## Decision

- Decision: `Accepted`.
- Decided by: review finding `R-04` and the governance rules in
  `RESEARCH_PRINCIPLES` and `ARCHITECTURE.md`.
- Rationale: the conservative model is the one the corpus is actually built on,
  and a single case may not silently redefine what every signature means. The
  proposal survives as a decision for the maintainer to take or refuse.
- Implementation links: `ACT-261`, `ACT-019`, `OBJ-162`, `CON-611`, `GAME-0268`,
  `GAME-0269`, `COMB-0266`, `ADR-013`, `RESEARCH_PRINCIPLES`.

## Change history

- 2026-09-06 — created and accepted as unit 4 of the batch-015 gene correction
  follow-up.
