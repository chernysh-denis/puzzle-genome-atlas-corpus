# Taxonomy Change 045: Generalise the Drive legality constraint to any shared-resource technique

## Status

- Proposal status: `Rejected`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-09
- Trigger: Claude transfer-test initial pass for `GAME-0283` TEKKEN 8, under
  the authority granted by `docs/CLAUDE_GAME_ANALYST_QUALITY_PROTOCOL_V2.md`.

## Current classification

- Exact wording or stable IDs: `CON-444` — Drive techniques require stock
  and non-Burnout state, whose definition read "a Drive technique is legal
  only when the fighter is outside Burnout, its current Drive stock can
  satisfy the technique's cost and its combat-state prerequisites permit
  activation".
- Files and entries affected: the Constraint registry; the Ukrainian gene
  localisation for `CON-444`; the `GAME-0283` decomposition; generated
  indexes and research artifacts.
- Original evidence or rationale: the gene was first isolated for
  `GAME-0172` Street Fighter 6 as the legality gate of the Drive techniques.
  Its parameters already listed stock, cost, Burnout, fighter state and
  technique.

## Detected problem

- What is incorrect, ambiguous or at the wrong type: TEKKEN 8 gates Heat
  Burst on Heat being unused in the round, Heat Smash and Heat Dash on the
  Heat state, and the Rage Art on the Rage state. The legality test — a
  shared technique is legal only while the universal resource state permits
  it — is the test `CON-444` isolates; Burnout and stock are one carrier's
  parameter values. Under the old wording the second carrier needed a
  duplicate Constraint.
- How the problem was found: the `GAME-0283` lower-ID scan of the Heat and
  Rage legality gates against `CON-444`, `CON-445`, `CON-442` and `CON-604`.
- Why this changes decision structure rather than terminology or theme: in
  both carriers the player must track a universal state before committing a
  shared technique; whether the state is a stock count with an exhaustion
  penalty or a once-per-round availability and an entered state only sizes
  the decision.

## Evidence

- Primary sources: the Street Fighter 6 evidence already cited by
  `GAME-0172`; for TEKKEN 8, Bandai Namco's official battle-system page
  (Heat "available once per round", Heat Smash "during Heat state", Rage Art
  "during Rage state"; `T8-011a`, `T8-012a`, `Confirmed | Direct | High`).
- Reproducible transitions: the `GAME-0172` Drive row and the `GAME-0283`
  Heat activation, consumption and Rage Art rows.
- Analysed games checked: `GAME-0172` and `GAME-0283`; no other carrier of
  `CON-444` exists.
- External systems or literature checked: none beyond the two carriers.
- Counterevidence: none; a technique gated only by pose and recovery remains
  `CON-442`, and tiered Super stock remains `CON-445`.

## Proposed change

- Old classification: legal only outside Burnout with sufficient Drive
  stock.
- Proposed classification: `CON-444` — Shared-resource fighting techniques
  require their declared resource state: a shared system technique is legal
  only while the fighter's declared universal resource state permits it —
  outside any exhausted or locked-out state, with enough stock or unused
  availability to pay the technique's cost, and inside any entered state the
  technique requires — and its combat-state prerequisites permit activation.
- Definitions and boundaries: the label is widened from `Drive techniques
  require stock and non-Burnout state`; the includes list names both
  carriers' instances; the excludes list gains `CON-445` and `CON-442` by
  ID; the parameters gain resource or state, exhaustion or lock-out,
  per-round availability and entered-state requirement.
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

- Decision: `Rejected` (corrective pass 02, confirmed in pass 03).
- Definitions and boundaries carrier audit: no single portable boundary
  survives both carriers. Street Fighter 6's `CON-444` gates five universal
  techniques on one spendable stock and its Burnout exhaustion, which is what
  its novelty note describes; TEKKEN 8 gates Heat Burst on a once-per-round
  availability, Heat Smash and Heat Dash on an entered timed state and the
  Rage Art on an entered low-health state, none of which is a spendable
  stock with an exhaustion penalty. Widening the definition to "any declared
  resource state" would have turned the gene into a generic legality
  predicate overlapping the lower-ID `CON-269` and `CON-351` without a
  carrier-complete proof.
- Decided by: the technique-by-technique legality audit recorded in the
  `GAME-0283` record and pass-02 checkpoint, extended in pass 03 by the
  re-adjudication of `CON-269`.
- Rationale: the committed `Drive techniques require stock and non-Burnout state` wording is restored because it is
  the only boundary its carrier evidence supports; TEKKEN 8 does not carry
  `CON-444` and, after pass 03 also rejected `CON-269`, carries no separate
  Constraint for Heat and Rage eligibility: the once-per-round availability
  and the entered states are clauses of `SYS-837` and `SYS-838` and resource
  parameters of `ACT-295`, while `CON-442` continues to own pose, recovery
  and mapping legality. No committed wording, carrier, lifecycle or ID
  changed.
- Implementation links: `CON-444`, `GAME-0172`, `GAME-0283`,
  `TAXONOMY_CHANGE_044`.
- Superseded pass-01 rationale (history only): the proposal argued that the
  Street Fighter 6 legality test stayed true as the exhausted-state and stock
  parameter values and that TEKKEN 8 read the same test through the
  once-per-round availability and the entered Heat or Rage state; that
  reasoning is withdrawn.

## Ukrainian review

- The pass-01 draft that gave `CON-444` a corrected Ukrainian label,
  definition, inclusion and exclusion for the widened boundary under the
  range batch `UK-GAME-0172-0283` was withdrawn with the rejection in pass
  02: the committed Ukrainian entry (`UK-GAME-0172-0172`) remains
  byte-for-byte unchanged. The proposed widening survives only as the
  superseded history recorded in the Decision section above.

## Change history

- 2026-09-09 — created and accepted during Claude transfer-test initial pass
  for `GAME-0283`, before that draft's independent audit.
- 2026-09-09 — corrective pass 02, after Codex audit 01 (`P1-01`): rejected.
  A technique-by-technique audit found that Heat Smash and the Rage Art are
  character-owned attacks with a state gate, exactly as Street Fighter 6's
  Super Art is a character command with a stock gate that `ACT-298` and
  `CON-444` already exclude, that Heat Burst and Heat Dash are universal
  inputs whose cost is an availability or timed state rather than a spent
  stock, and that Heat and Rage are two independent states rather than one
  shared reserve funding one technique family. No single portable boundary
  survives both carriers, and the widened legality gate overlapped the
  lower-ID `CON-269` and `CON-351`. `CON-444` is restored to its committed
  `Drive techniques require stock and non-Burnout state` wording, `GAME-0283` does not carry it, and the TEKKEN 8
  commands are owned by `ACT-295` with their legality under `CON-269`
  (that `CON-269` reuse was itself withdrawn in pass 03; the eligibility is
  now a clause of `SYS-837` and `SYS-838`). No committed wording, carrier,
  lifecycle or ID changed.
- 2026-09-09 — corrective pass 03, after Codex audit 02 (`P2-01`): the
  operative Decision section is rewritten to state the rejection reasoning;
  the pass-01 acceptance rationale is kept only as superseded history.
- 2026-09-09 — corrective pass 04, after Codex audit 03 (`P2-02`): the
  Ukrainian review section now states that the draft localisation was
  withdrawn and the committed Ukrainian entry is unchanged.
