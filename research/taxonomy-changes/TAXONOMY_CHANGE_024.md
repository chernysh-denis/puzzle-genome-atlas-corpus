# Taxonomy Change 024: Merge the region-and-escape run progression into the guardian-gated area sequence

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-06
- Trigger: card `C-11` of
  [`FULL_TAXONOMY_DUPLICATE_AUDIT_001`](../normalisation/FULL_TAXONOMY_DUPLICATE_AUDIT_001.md),
  disposition `CONFIRMED`, routed as the second half of implementation target
  `T-06`

## Current classification

- Exact wording or stable IDs: `SYS-468` — Advance a boss-gated floor sequence
  toward the scoped ending; `SYS-781` — Advance a boss-gated region sequence
  toward scoped escape.
- Files and entries affected: the System Behaviour registry, Ukrainian gene
  localisation, the `GAME-0251` signature and prose, `COMB-0249`, the candidate
  terms record, the generated game and combination indexes, gene salience,
  plain-language presentation, the deterministic research artifacts and the web
  contract tests.
- Original evidence or rationale: `SYS-468` was isolated for `GAME-0164` The
  Binding of Isaac: Rebirth. `SYS-781` was isolated for `GAME-0251` Hades, whose
  unit rejected `SYS-468` "because its reviewed floor/trapdoor ending does not
  cover a four-region escape and House return".

## Detected problem

- What is incorrect: both records state the same transition — clearing the
  mandatory guardian of the current bounded area opens its legal transition,
  taking that transition carries the same run's health, resources and build into
  the next area, and the final guardian settles the run's declared terminal.
- How the problem was found: the full taxonomy duplicate audit, card `C-11`,
  confirmed by independent review.
- Why this changes decision structure rather than terminology: the residual
  differences are the authored names of the objects involved — "floor",
  "descent" and "ending" against "region" and "escape".
  [`TAXONOMY_CHANGE_015`](TAXONOMY_CHANGE_015.md) established that a game object
  name is not a progression boundary. The recorded rejection also conflated two
  genes: the "House return" it cited is `SYS-782`'s hub settlement, not this
  progression rule, and `SYS-782` remains separate and unmerged.

## Evidence

- Primary sources: the reviewed `GAME-0164` and `GAME-0251` records and their
  source ledgers.
- Reproducible transitions: in both packets the mandatory guardian of the
  current area must be cleared before its exit becomes legal; taking that exit
  preserves current health, currency and accumulated run modifiers; and the
  final guardian's defeat settles the declared terminal.
- Analysed games checked: a fresh unit-level two-way transfer scan over all 804
  Active System genes. `SYS-468` is the nearest System to `SYS-781` at 0.247
  with the next candidate at 0.167, and `SYS-781` is the nearest System to
  `SYS-468` at 0.247 with the next candidate at 0.148. The pair is mutually
  nearest. The margin is narrower than in the other System merges of this run
  because both records are short and written almost entirely in their own
  product's vocabulary — which is precisely the defect being corrected.
- Counterevidence, and how it is handled:
  - `SYS-469` and `SYS-782` carry what each terminal then discards or retains.
    They are separate genes, remain `Active`, and are now named in the
    survivor's `Excludes`. The Hades rejection's real content — the House return
    retaining metaprogression — is entirely `SYS-782`.
  - `SYS-611` scored 0.133 and is a real sibling: it persists each admitted
    boss's own reward and route flag across an authored chapter, so its unit of
    progress is a set of retained boss states rather than one carried run.
    Named in the survivor's `Excludes`.
  - `SYS-464` generates the area layout and stays separate; `SYS-455` resets an
    area after a softcore death and is already excluded by wording the survivor
    retains.
- External systems or literature checked: none beyond the two products' own
  published material.

## Proposed change

- Old classification: two System genes separated by the authored names of the
  bounded area, its transition and its terminal.
- Proposed classification: one System gene for advancing a guardian-gated area
  sequence toward the scoped run terminal.
- Definitions and boundaries: `SYS-468` becomes "Advance a guardian-gated area
  sequence toward the scoped run terminal". The guardian-gated transition, the
  carried transient run state and the final settlement are the boundary. The
  area and its authored name, the guardian, the clear condition, the transition
  and its authored name, the next area, the retained run state, the final
  guardian and the terminal's name are parameters.
- Lifecycle effects: `SYS-781` becomes a `Merged` alias pointing to `SYS-468`.
  Its stable ID is never reused.
- What does not change: `SYS-469`, `SYS-782`, `SYS-611`, `SYS-464` and
  `SYS-455` keep their boundaries and lifecycles. The `GAME-0164` signature and
  its selected-neighbour interpretation are unchanged.

## Genome and combination impact

- Genes added, deprecated, merged or split: `SYS-781` merged into `SYS-468`.
  Active genes fall from 2,347 to 2,346; `Merged` records rise from 39 to 40;
  the 2,387 total definitions are unchanged.
- Games requiring annotation: `GAME-0251` (signature, system prose, normalised
  genome, corpus comparison, selected-neighbour interpretation, preserved notes,
  lower-ID scan, taxonomy impact, negative results and the delta summary), plus
  the `GAME-0251` entry of the candidate-terms record.
- Combinations affected: `COMB-0249` substitutes `SYS-468`, stays at eighteen
  genes and remains a strict proper subset of the thirty-gene `GAME-0251`
  genome. A global recomputation confirms that every combination's declared
  supporters still equal the set of games whose genome contains it; unlike unit
  6, this merge creates no new containment.
- Novelty claims affected: `SYS-468` records the generalisation. `GAME-0251` now
  claims five new genes rather than six.
- Comparison impact: `GAME-0251`'s selected near neighbour stays `GAME-0164`,
  whose shared-gene count rises from fourteen to fifteen and whose score rises
  from `14 / 44 = 0.318182` to `15 / 43 = 0.348837`. No other selected neighbour
  moves, and no exact genome or combination collision is created.

## Decision

- Decision: `Accepted`.
- Decided by: confirmed audit card `C-11` plus a fresh unit-level two-way
  transfer test over the complete System Behaviour registry.
- Rationale: the surviving System accepts both carriers' progression rules once
  the area, transition and terminal names are supplied as parameters, and the
  rejection that kept them apart rested on a hub-return rule that a different
  gene already carries.
- Implementation links: `SYS-468`, `SYS-781`, `SYS-469`, `SYS-782`, `SYS-611`,
  `GAME-0164`, `GAME-0251`, `COMB-0162`, `COMB-0249`.

## Change history

- 2026-09-06 — created and accepted as unit 7 of the confirmed taxonomy
  normalisation derived from `FULL_TAXONOMY_DUPLICATE_AUDIT_001`.
