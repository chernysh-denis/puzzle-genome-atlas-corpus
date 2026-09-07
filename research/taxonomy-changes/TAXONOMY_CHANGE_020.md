# Taxonomy Change 020: Merge the reserve-free held guard into the facing-relative guard

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-06
- Trigger: card `C-06` of
  [`FULL_TAXONOMY_DUPLICATE_AUDIT_001`](../normalisation/FULL_TAXONOMY_DUPLICATE_AUDIT_001.md),
  disposition `CONFIRMED`

## Current classification

- Exact wording or stable IDs: `ACT-437` — Hold an exertion-absorbing frontal
  guard; `ACT-439` — Hold or release an undirected guard with no depleting
  reserve.
- Files and entries affected: Action registry, Ukrainian gene localisation,
  `GAME-0263` signature and prose, `COMB-0261`, the generated game and
  combination indexes, gene salience, plain-language presentation, a
  cross-reference in `GAME-0268`, the candidate-term disposition, the
  deterministic research artifacts and the web contract tests.
- Original evidence or rationale: `ACT-437` was isolated for `GAME-0262` DARK
  SOULS III, where guarding spends a shared exertion reserve. `ACT-439` was
  isolated for `GAME-0263` God of War on the ground that its held guard "costs
  nothing but the actions it forgoes".

## Detected problem

- What is incorrect: both records describe the same player command — raise and
  hold equipped protective equipment toward the character's current facing so
  incoming attacks are reduced or absorbed, then release it. The only stated
  difference is whether absorption is priced against a depleting reserve. That
  price is not part of the command: in DARK SOULS III it is already carried by
  `SYS-798` "Deplete and regenerate one shared exertion reserve" and `CON-604`
  "Evasion and guard require remaining exertion". Encoding it again in the
  Action ID duplicates an independently represented rule, which is the defect
  [`TAXONOMY_CHANGE_012`](TAXONOMY_CHANGE_012.md) merged.
- How the problem was found: the full taxonomy duplicate audit, card `C-06`,
  confirmed by independent review.
- Why this changes decision structure rather than terminology: the player's
  decision in both records is when to commit to a facing and forgo ordinary
  action. Whether that commitment also debits a reserve changes the price of
  the decision, not the decision itself, and the price already has a
  type-correct home.

## Evidence

- Primary sources: the reviewed `GAME-0262` and `GAME-0263` records and their
  source ledgers.
- Reproducible transitions: in both products the hold input raises the guard
  within a facing arc, incoming attacks inside that arc are reduced or
  absorbed, and release returns ordinary action. DARK SOULS III additionally
  debits `SYS-798` and is gated by `CON-604`; God of War has no such reserve.
- Analysed games checked: a fresh unit-level two-way transfer scan over all 438
  Active Action genes. It surfaced four other held-guard records and each was
  read: `ACT-349` requires the player to aim the guard toward one chosen
  incoming direction; `ACT-296` is an opponent-relative high or low guard
  requested by a movement direction rather than by raising equipment; `ACT-425`
  requires a durability-bearing close weapon and resolves as a timed parry; and
  `ACT-383` requires a dedicated guard meter that incoming strikes can exhaust
  into an exposed state.
- Counterevidence, and how it is handled: **`ACT-383` is the closest surviving
  neighbour and is deliberately not merged.** Its discriminator is a
  settlement difference — the guard itself can be broken into an exposed state
  — not a price difference, and its carrier `GAME-0213` is not an accepted
  carrier of this unit. The survivor's `Excludes` names that boundary
  explicitly so the distinction stays auditable, and the pair is recorded as a
  new candidate for a separate future review rather than absorbed here.
  `ACT-439`'s own `Excludes` named "a guard whose incoming strikes deplete a
  guard meter or a shared exertion reserve", which excluded its sibling by
  price rather than by decision structure.

## Proposed change

- Old classification: two Action genes separated by whether guarding costs a
  reserve.
- Proposed classification: one Action gene for the held facing-relative guard,
  with the absorption price as a parameter.
- Definitions and boundaries: `ACT-437` becomes "Hold and release an undirected
  facing-relative guard" and states that the command does not own whether or
  how absorption is priced. Its `Excludes` retains the directional,
  opponent-relative, timed-parry, absorbing-pool and passive-armour boundaries
  and adds the dedicated-guard-meter boundary of `ACT-383`.
- Lifecycle effects: `ACT-439` becomes a `Merged` alias pointing to `ACT-437`.
  Its stable ID is never reused.
- What does not change: `SYS-798` and `CON-604` are untouched and continue to
  carry the exertion behaviour in `GAME-0262`. No reserve is invented for the
  God of War carrier; the absence of one is recorded as that instance's
  parameter value. `ACT-383`, `ACT-349`, `ACT-296` and `ACT-425` remain
  distinct. `GAME-0213` is not modified.

## Genome and combination impact

- Genes added, deprecated, merged or split: `ACT-439` merged into `ACT-437`.
  Active genes fall from 2,352 to 2,351; `Merged` records rise from 34 to 35;
  the 2,387 total definitions are unchanged.
- Games requiring annotation: `GAME-0263` (signature, decomposition, normalised
  genome, preserved notes, taxonomy impact and delta summary) and a
  cross-reference in `GAME-0268`'s lower-ID scan.
- Combinations affected: `COMB-0261` substitutes `ACT-437`. Its size stays at
  eighteen genes and it remains a strict proper subset of the twenty-five-gene
  `GAME-0263` genome. A global scan found no exact combination collision and no
  additional game whose genome now contains `COMB-0261`.
- Novelty claims affected: `ACT-437` records the generalisation. `GAME-0263`
  now claims three new genes rather than four.
- Comparison impact: none. `GAME-0263` keeps `GAME-0245` DOOM (2016) as its
  selected near neighbour at an unchanged `0.297297`, because `GAME-0245`
  carries neither gene. No other selection changes and no exact genome match is
  created.

## Decision

- Decision: `Accepted`.
- Decided by: confirmed audit card `C-06` plus a fresh unit-level two-way
  transfer test over the complete Action registry.
- Rationale: the surviving Action accepts the same command from both carriers
  once the absorption price is supplied as a parameter, and that price is
  already represented by `SYS-798` and `CON-604` where it exists.
- Implementation links: `ACT-437`, `ACT-439`, `SYS-798`, `CON-604`, `ACT-383`,
  `GAME-0262`, `GAME-0263`, `COMB-0261`.

## Change history

- 2026-09-06 — created and accepted as unit 3 of the confirmed taxonomy
  normalisation derived from `FULL_TAXONOMY_DUPLICATE_AUDIT_001`.
