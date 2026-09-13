# Taxonomy Change 048: Generalise the municipal milestone unlock to any declared settlement progression measure

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-09
- Trigger: Codex final acceptance audit of `GAME-0284` Cities: Skylines II,
  after Claude transfer passes supplied a research candidate.

## Current classification

- Exact wording or stable IDs: `SYS-169` — Unlock municipal capabilities at
  population milestones, whose definition read "when the current city
  population first crosses a declared threshold, the simulation persistently
  adds its associated municipal tools, services, zones, policies, finance
  options or purchasable land areas to the available action catalogue".
- Files and entries affected: the System Behaviour registry; the Ukrainian
  gene localisation for `SYS-169`; the `GAME-0284` decomposition; generated
  indexes and research artifacts.
- Original evidence or rationale: the gene was first isolated for `GAME-0121`
  Cities: Skylines, whose milestones are population thresholds, and reused by
  `GAME-0132` Anno 1800, whose milestones are population tiers. The wording
  encoded those two carriers' shared measure as the boundary, although its
  parameters already treated the threshold schedule and the unlock bundle as
  parameters.

## Detected problem

- What is incorrect, ambiguous or at the wrong type: Cities: Skylines II
  reaches each milestone by accumulating Expansion Points rather than by
  crossing a population threshold. Paradox states that "Each Milestone is
  unlocked by reaching a specific amount of Expansion Points (XP)" and that
  active Expansion Points are "granted immediately as a result of actions you
  take, such as placing or upgrading a service building, constructing a
  signature building, or expanding the city's road network". A city therefore
  advances toward its milestone with no population change at all, which the old
  wording cannot express. The decision the gene isolates — a settlement
  crossing a declared threshold and permanently gaining municipal commands —
  is unchanged; only the measure compared differs.
- How the problem was found: the mandatory complete same-series delta of
  `GAME-0121` for `GAME-0284`, run gene by gene before any ID was allocated.
- Why this changes decision structure rather than terminology or theme: in all
  three carriers the player plans against one settlement-wide quantity whose
  declared thresholds convert into a permanently wider action catalogue.
  Whether that quantity is population, a population tier or an accumulated
  point total only sizes and sources the decision.

## Evidence

- Primary sources: the Cities: Skylines and Anno 1800 evidence already cited
  by `GAME-0121` and `GAME-0132`; for Cities: Skylines II, Paradox's official
  [Feature Highlight #10: Game Progression](https://www.paradoxinteractive.com/games/cities-skylines-ii/features/game-progression)
  (`CS2-005a`, `CS2-005b`, `CS2-006a`, `Confirmed | Direct | High`). The exact
  current first bundle remains an unenumerated run-time gap (`CS2-006b`,
  `Observation | Limited | Low`) and is not needed by the generalisation.
- Reproducible transitions: the `GAME-0121` milestone row, the `GAME-0132`
  population-tier rows and the `GAME-0284` milestone settlement row.
- Analysed games checked: `GAME-0121`, `GAME-0132` and `GAME-0284`. No other
  reviewed game carries `SYS-169`.
- External systems or literature checked: none beyond the three carriers.
- Counterevidence: none. Cities: Skylines and Anno 1800 both remain true
  sentence by sentence, because a population count and a population tier are
  each one value of a declared settlement progression measure, and both
  carriers already grant a cash award that the widened wording now names
  explicitly.

## Proposed change

- Old classification: a persistent catalogue addition triggered when city
  population first crosses a declared threshold.
- Proposed classification: `SYS-169` — Unlock municipal capabilities at a
  settlement progression milestone: when the settlement's declared progression
  measure first reaches a declared threshold, the simulation persistently adds
  that milestone's associated municipal tools, services, zones, policies,
  finance options or purchasable land areas to the available action catalogue
  and grants any declared one-time award.
- Definitions and boundaries: the label is widened from `at population
  milestones`; the includes list names all three carriers' instances; the
  excludes list keeps queued technology, random upgrades and cosmetic
  achievements and adds both the crediting of the measure itself, which the
  generalised `SYS-517` owns, and the legality predicate that withholds the
  released capability, which `CON-179` and `CON-440` own; the parameters name
  the compared measure and its threshold schedule and generalise the cash
  award to any declared one-time award.
- Lifecycle effects: none.
- What does not change: the `GAME-0121` and `GAME-0132` signatures, every
  earlier reviewed signature, every lifecycle state and every stable ID.

## Genome and combination impact

- Genes added, deprecated, merged or split: none by this record. Crediting
  the measure is owned by the generalised `SYS-517` under
  [`TAXONOMY_CHANGE_050`](TAXONOMY_CHANGE_050.md), and that boundary is
  excluded from `SYS-169` explicitly. The pass-01 proposal to create a
  separate new System for the same crediting is withdrawn, and its identifier
  `SYS-839` is registered `Deprecated` with no carrier under
  [`TAXONOMY_CHANGE_050`](TAXONOMY_CHANGE_050.md).
- Games requiring annotation: `GAME-0284` reuses the generalised ID;
  `GAME-0121` and `GAME-0132` remain carriers with their wording valid under
  the wider boundary and gain an explicit support line.
- Combinations affected: none. `SYS-169` is not a member of `COMB-0117` or of
  any other verified combination set, so no combination gene set changes.
- Novelty claims affected: the `GAME-0121` first-isolation note remains true.

## Decision

- Decision: `Accepted`.
- Decided by: Codex's complete carrier audit recorded in the `GAME-0284` record
  and final acceptance checkpoint, which restates each existing carrier's trigger,
  preconditions, operation, result, persistence and exclusions under the
  widened wording.
- Rationale: the boundary survives every carrier. The measure was already a
  parameter-shaped notion in the gene's own parameter list, and refusing the
  generalisation would have required a duplicate System gene whose only
  difference from `SYS-169` is which quantity the threshold reads.
- Implementation links: `SYS-169`, `GAME-0121`, `GAME-0132`, `GAME-0284`,
  `TAXONOMY_CHANGE_050`; `TAXONOMY_CHANGE_049` records the withdrawn
  companion proposal for `CON-179`.

## Ukrainian review

- `SYS-169` receives a corrected Ukrainian label, definition, inclusion,
  exclusion and parameter wording for the widened boundary in the same unit,
  under the range batch `UK-GAME-0121-0284`.

## Change history

- 2026-09-09 — proposed during the Claude transfer-test initial pass for
  `GAME-0284`; not yet accepted at that stage.
- 2026-09-09 — corrective pass 02: the generalisation stands, because
  `GAME-0284` compares an accumulated progression total rather than a
  population, but its `GAME-0284` inclusion no longer enumerates a
  first-milestone bundle. The exact current bundle could not be closed from
  current official evidence and is recorded as an open gap in the game record,
  so the gene now states only that a milestone releases the capabilities it
  carries. The `Excludes` list additionally separates crediting the measure
  (`SYS-517`) and the gate predicate (`CON-179`, `CON-440`) from this gene.
- 2026-09-09 — accepted by Codex after the final carrier audit under accepted
  selection amendment 001; Claude's passes remain research input, not the
  canonical acceptance authority.
