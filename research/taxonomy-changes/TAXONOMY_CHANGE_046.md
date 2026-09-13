# Taxonomy Change 046: Generalise the duel HUD gene to any shared-resource state and vitality overlay

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-09
- Trigger: Claude transfer-test initial pass for `GAME-0283` TEKKEN 8, under
  the authority granted by `docs/CLAUDE_GAME_ANALYST_QUALITY_PROTOCOL_V2.md`.

## Current classification

- Exact wording or stable IDs: `INF-210` — Duel HUD exposes paired meters,
  clock and round score, whose definition read "one live fighting HUD
  simultaneously exposes each participant's vitality, Drive state and Super
  Art stock together with the shared round timer and accumulated round
  markers".
- Files and entries affected: the Information registry; the Ukrainian gene
  localisation for `INF-210`; the `GAME-0283` decomposition; generated
  indexes and research artifacts.
- Original evidence or rationale: the gene was first isolated for
  `GAME-0172` Street Fighter 6, whose HUD shows vitality, Drive and Super.
  The wording encoded those two resource names as the boundary.

## Detected problem

- What is incorrect, ambiguous or at the wrong type: TEKKEN 8's battle
  screen exposes each Health Gauge with its Recoverable Gauge, each Heat
  gauge and Heat Timer, Rage indication, the Time Limit and the Rounds Won
  markers. The disclosure structure — each participant's vitality and shared
  resource state beside the shared clock and round score — is the structure
  `INF-210` isolates; the named resources are parameters. Under the old
  wording the second carrier needed a duplicate Information gene.
- How the problem was found: the `GAME-0283` lower-ID scan of the battle
  screen against `INF-210`, `INF-254`, `INF-276` and `INF-290`, with a
  clause-by-clause compound test: the vitality bars, resource gauges, timer
  and markers are permanent elements of one frame whose values update
  together, and the recoverable overlay and Rage indication are states of
  those elements rather than independently disappearing disclosures.
- Why this changes decision structure rather than terminology or theme: in
  both carriers the player reads the same paired frame to decide whether to
  spend a shared resource and how to play the clock; which resource is shown
  only sizes the decision.

## Evidence

- Primary sources: the Street Fighter 6 evidence already cited by
  `GAME-0172`; for TEKKEN 8, Bandai Namco's official starting guide naming
  the Health Gauge, Time Limit, Rounds Won, Heat Timer and Recoverable Gauge
  (`T8-016`, `Confirmed | Direct | High`).
- Reproducible transitions: the `GAME-0172` HUD reading in every row and the
  `GAME-0283` Heat, Rage, recoverable and round rows.
- Analysed games checked: `GAME-0172` and `GAME-0283`; `GAME-0198` keeps its
  own `INF-254` because it discloses damage colour and stocks rather than
  vitality and round markers.
- External systems or literature checked: none beyond the carriers.
- Counterevidence: none.

## Proposed change

- Old classification: vitality, Drive state and Super Art stock beside the
  timer and round markers.
- Proposed classification: `INF-210` — Duel HUD exposes paired vitality,
  shared-resource state, clock and round score: one live fighting HUD
  simultaneously exposes each participant's vitality, including any declared
  recoverable or temporary overlay, and the state of each shared combat
  resource, together with the shared round timer and accumulated round
  markers.
- Definitions and boundaries: the label is widened from `Duel HUD exposes
  paired meters, clock and round score`; the includes list names both
  carriers' instances; the excludes list replaces the Battle Hub product
  noun with lobby profile information; the parameters gain the recoverable or
  temporary overlay and generic shared resource gauges, states and timers.
- Lifecycle effects: none.
- What does not change: the `GAME-0172` signature, every earlier reviewed
  signature, every lifecycle state and every stable ID.

## Genome and combination impact

- Genes added, deprecated, merged or split: none by this record.
- Games requiring annotation: `GAME-0283` reuses the generalised ID;
  `GAME-0172` remains a carrier with its wording valid under the wider
  boundary.
- Combinations affected: `COMB-0170` keeps the same gene set and its sole
  carrier `GAME-0172`.
- Novelty claims affected: the `GAME-0172` novelty note remains true.

## Decision

- Decision: `Accepted`.
- Definitions and boundaries carrier audit: for Street Fighter 6 the HUD
  (vitality, Drive, Super, timer, markers, notices, control-type icon)
  remains true sentence by sentence with Drive and Super as the shared
  resources and no overlay. For TEKKEN 8 the same frame shows the
  Recoverable Gauge overlay, Heat and Rage.
- Decided by: the reuse-first comparison recorded in the `GAME-0283` record
  and pass checkpoint.
- Rationale: substituting "Heat gauge and Rage indication" for "Drive stocks
  and Super stock" leaves the disclosure structure unchanged.
- Implementation links: `INF-210`, `GAME-0172`, `GAME-0283`.

## Ukrainian review

- `INF-210` receives a corrected Ukrainian label, definition, inclusion and
  exclusion for the widened boundary in the same unit, under the range batch
  `UK-GAME-0172-0283`.

## Change history

- 2026-09-09 — created and accepted during Claude transfer-test initial pass
  for `GAME-0283`, before that draft's independent audit.
