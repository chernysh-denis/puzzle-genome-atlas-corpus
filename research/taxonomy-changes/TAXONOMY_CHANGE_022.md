# Taxonomy Change 022: Merge the duel phase and duel card-text genes into the ordered-phase and card-routing boundaries

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-06
- Trigger: cards `C-08` and `C-09` of
  [`FULL_TAXONOMY_DUPLICATE_AUDIT_001`](../normalisation/FULL_TAXONOMY_DUPLICATE_AUDIT_001.md),
  both disposition `CONFIRMED`, routed together as implementation target `T-05`

## Current classification

- Exact wording or stable IDs: `SYS-586` — Advance the ordered turn phases and
  refresh permanents; `SYS-682` — Advance ordered duel phases and active turns;
  `SYS-588` — Apply card text and route the object between zones; `SYS-684` —
  Apply card text and route cards among duel zones.
- Files and entries affected: the System Behaviour registry, Ukrainian gene
  localisation, the `GAME-0206` signature and prose, `COMB-0204`, the generated
  game and combination indexes, gene salience, plain-language presentation, the
  deterministic research artifacts and the web contract tests.
- Original evidence or rationale: `SYS-586` and `SYS-588` were isolated for
  `GAME-0185` Magic: The Gathering Arena; `SYS-682` and `SYS-684` were isolated
  for `GAME-0206` Yu-Gi-Oh! Master Duel three weeks later. Neither pair was
  compared against the other at the time, because the Master Duel unit rejected
  the whole `SYS-585`–`SYS-590` block on the strength of the MTG vocabulary in
  their wording rather than on their decision structure.

## Detected problem

- What is incorrect: each pair states one invariant twice in two products'
  vocabularies.
  - `SYS-586` / `SYS-682`: the system advances the active turn through a fixed
    ordered list of named phases, performs each phase's declared automatic
    actions, refreshes the per-turn allowances that phase restores and passes
    the active turn to the opponent.
  - `SYS-588` / `SYS-684`: when a card or effect resolves, the system performs
    its text clauses in rules order and routes each affected represented card to
    its type- and effect-defined destination zone together with whatever state
    the rules retain, creating any resulting triggers.
- How the problem was found: the full taxonomy duplicate audit, cards `C-08`
  and `C-09`, both confirmed by independent review.
- Why this changes decision structure rather than terminology: the residual
  differences are the phase names, which phases are optional, which allowance
  each phase refreshes, the zone names, and whether a moved card retains a face
  and battle position. Every one of those is an authored value the two records
  already carried in their own `Parameters` fields — `SYS-586` listed "phase,
  step, untap, upkeep triggers, draw, combat, cleanup", `SYS-682` listed "phase,
  draw, allowances, optional phases", `SYS-588` listed "destination zone" and
  `SYS-684` listed "origin, destination, face, position". No player authority,
  state transition, timing, information availability, eligibility, persistence,
  failure or settlement differs between the members of either pair.

## Evidence

- Primary sources: the reviewed `GAME-0185` and `GAME-0206` records, the
  official Magic comprehensive-rules evidence behind the former and the official
  Yu-Gi-Oh! rulebook evidence (`MD-005`–`MD-008`) behind the latter.
- Reproducible transitions: in both products advancing past the last phase of a
  turn transfers the active turn and restores that ruleset's per-turn
  allowances; in both, a resolved rule object performs its clauses in rules
  order and each affected card lands in the destination its type and the
  resolving text define.
- Analysed games checked: a fresh unit-level two-way transfer scan over all 807
  Active System genes. `SYS-586` is the nearest System to `SYS-682` at 0.152
  with the next candidate at 0.077; `SYS-588` is the nearest System to `SYS-684`
  at 0.173 with the next candidate at 0.132. In both directions the pair is
  mutually nearest, and no third System is a better survivor.
- Counterevidence, and how it is handled:
  - The two rulesets' response models genuinely differ — MTG grants priority and
    resolves one top stack object, Master Duel builds a Spell-Speed Chain that
    settles backward. Those are carried by `SYS-587`, `SYS-683`, `TIM-019` and
    `TIM-020`, all of which remain `Active` and unmerged. Each survivor's
    `Excludes` now names the scheduling genes explicitly so the phase and
    routing boundaries cannot absorb them.
  - `SYS-356`, the stat-ordered initiative queue, scored 0.134 against `SYS-586`
    and is a real sibling: its order is derived from a mutable initiative
    statistic rather than declared as a fixed list, so `SYS-586`'s `Excludes`
    now names it.
  - `SYS-163`, resolving one played card's text in a Slay the Spire run, scored
    0.132 against `SYS-684` and is likewise a real sibling: it resolves inside a
    single-sided run deck with no opposing controller's zones. `SYS-588`'s
    `Excludes` now names it. `SYS-163` itself is untouched.
- External systems or literature checked: none beyond the two products' own
  published rules.

## Proposed change

- Old classification: four System genes, two per product, separated by phase
  and zone vocabulary.
- Proposed classification: two System genes — one for ordered named phase
  progression with its refreshed allowances, one for applying resolving card
  text and routing represented cards among rule-defined zones.
- Definitions and boundaries:
  - `SYS-586` becomes "Advance the ordered named turn phases and refresh their
    allowances". Phase and step names, which phases are optional, the
    phase-bound automatic actions, the allowances each phase refreshes, maximum
    hand and the next active player are parameters.
  - `SYS-588` becomes "Apply resolving card text and route cards among
    rule-defined zones". Zone names, replacement effects, and the face, position
    or modifier state a moved card retains are parameters.
- Lifecycle effects: `SYS-682` becomes a `Merged` alias pointing to `SYS-586`
  and `SYS-684` a `Merged` alias pointing to `SYS-588`. Neither stable ID is
  ever reused.
- What does not change: `SYS-585`, `SYS-587`, `SYS-589`, `SYS-590`, `SYS-681`,
  `SYS-683`, `SYS-685`, `SYS-686`, `SYS-163`, `SYS-356`, `TIM-019` and
  `TIM-020` keep their boundaries and lifecycles. `GAME-0185`'s signature is
  unchanged. Priority, stack settlement and Chain construction remain carried
  independently by `SYS-587`, `SYS-683`, `TIM-019`, `TIM-020` and `CON-548`.

## Genome and combination impact

- Genes added, deprecated, merged or split: `SYS-682` merged into `SYS-586` and
  `SYS-684` merged into `SYS-588`. Active genes fall from 2,350 to 2,348;
  `Merged` records rise from 36 to 38; the 2,387 total definitions are
  unchanged.
- Games requiring annotation: `GAME-0206` (signature, system prose, normalised
  genome, corpus comparison, selected-neighbour interpretation, preserved notes,
  taxonomy impact, negative results and the delta summary).
- Combinations affected: `COMB-0204` substitutes `SYS-586` and `SYS-588`. Its
  size stays at nineteen genes and it remains a strict proper subset of the
  twenty-three-gene `GAME-0206` genome. `COMB-0183` already contained both
  survivors and is unchanged; neither combination is a subset of the other, and
  a global scan found no exact combination collision.
- Novelty claims affected: both survivors record the generalisation. `GAME-0206`
  now claims nineteen new genes rather than twenty-one.
- Comparison impact: `GAME-0206`'s selected near neighbour stays `GAME-0185`,
  whose shared-gene count rises from two to four and whose score rises from
  `2 / 47 = 0.042553` to `4 / 45 = 0.088889`. No other selected neighbour moves
  and no exact genome match is created.

## Decision

- Decision: `Accepted`.
- Decided by: confirmed audit cards `C-08` and `C-09` plus a fresh unit-level
  two-way transfer test over the complete System Behaviour registry.
- Rationale: each surviving System accepts both carriers' rules once the phase
  names, optional phases, refreshed allowances, zone names and retained card
  state are supplied as parameters, and the genuinely different response models
  were never carried by these four genes.
- Implementation links: `SYS-586`, `SYS-588`, `SYS-682`, `SYS-684`, `SYS-587`,
  `SYS-683`, `TIM-019`, `TIM-020`, `GAME-0185`, `GAME-0206`, `COMB-0183`,
  `COMB-0204`.

## Change history

- 2026-09-06 — created and accepted as unit 5 of the confirmed taxonomy
  normalisation derived from `FULL_TAXONOMY_DUPLICATE_AUDIT_001`.
