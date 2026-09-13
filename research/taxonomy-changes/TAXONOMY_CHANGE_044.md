# Taxonomy Change 044: Generalise the Drive technique command to any shared-resource fighting technique

## Status

- Proposal status: `Rejected`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-09
- Trigger: Claude transfer-test initial pass for `GAME-0283` TEKKEN 8, under
  the authority granted by `docs/CLAUDE_GAME_ANALYST_QUALITY_PROTOCOL_V2.md`.

## Current classification

- Exact wording or stable IDs: `ACT-298` — Commit one legal Drive technique,
  whose definition read "the player requests one of the shared Drive System
  techniques from an eligible fighting state, accepting its current stock
  cost and combat transition".
- Files and entries affected: the Action registry; the Ukrainian gene
  localisation for `ACT-298`; the `GAME-0283` decomposition; generated
  indexes and research artifacts.
- Original evidence or rationale: the gene was first isolated for
  `GAME-0172` Street Fighter 6, whose five Drive techniques all draw on one
  shared six-stock gauge. The wording encoded that carrier's resource name
  as the boundary, although its parameters already listed technique, input,
  fighter state, stock cost and Burnout eligibility.

## Detected problem

- What is incorrect, ambiguous or at the wrong type: TEKKEN 8's Heat Burst,
  Heat Smash, Heat Dash and Rage Art are shared system techniques with
  universal inputs that are funded or unlocked by a universal combat state
  (Heat availability, the Heat state, the Rage state) rather than by a
  character's command list. The player's decision — commit a universal
  technique and accept its resource consequence — is the decision `ACT-298`
  already isolates; only the resource differs. Under the old wording a second
  carrier needed a duplicate Action.
- How the problem was found: the `GAME-0283` lower-ID scan of the Heat and
  Rage commands against `ACT-298`, `ACT-295`, `ACT-223`, `ACT-425`,
  `ACT-437` and `ACT-356`.
- Why this changes decision structure rather than terminology or theme: in
  both carriers the player chooses between a character command and a
  universal technique whose legality and cost come from a shared state;
  whether that state is a stock gauge or a timed availability only sizes the
  decision.

## Evidence

- Primary sources: the Street Fighter 6 evidence already cited by
  `GAME-0172`; for TEKKEN 8, Bandai Namco's official battle-system page and
  2023 mechanics article for Heat Burst, Heat Smash, Heat Dash and the Rage
  Art (`T8-011a`, `T8-012a`, `Confirmed | Direct | High`).
- Reproducible transitions: the `GAME-0172` Drive rows and the `GAME-0283`
  Heat activation, Heat consumption and Rage Art rows.
- Analysed games checked: `GAME-0172` and `GAME-0283`; `GAME-0198` carries
  `ACT-295` and `ACT-356` but no shared-resource technique, so it is not a
  carrier.
- External systems or literature checked: none beyond the two carriers.
- Counterevidence: Street Fighter 6 prices every technique from one stock
  and enters Burnout on exhaustion; TEKKEN 8 limits activation to once per
  round and consumes a timer. Both are recorded as resource parameters.

## Proposed change

- Old classification: one of the shared Drive System techniques accepting
  its stock cost.
- Proposed classification: `ACT-298` — Commit one legal shared-resource
  fighting technique: the player requests one of the ruleset's shared system
  techniques, funded or unlocked by a universal combat resource or state
  rather than owned by one character's command list, from an eligible
  fighting state, accepting its declared resource cost, consumption or
  once-per-round limit and its combat transition.
- Definitions and boundaries: the label is widened from `Commit one legal
  Drive technique`; the includes list names both carriers' instances; the
  excludes list keeps ordinary guard and a character-command Super Art
  (`ACT-295`) and adds a Heat Engager entered as an ordinary attack; the
  parameters gain resource state, consumption and once-per-round
  eligibility.
- Lifecycle effects: none.
- What does not change: the `GAME-0172` signature, every earlier reviewed
  signature, every lifecycle state and every stable ID.

## Genome and combination impact

- Genes added, deprecated, merged or split: none by this record.
- Games requiring annotation: `GAME-0283` reuses the generalised ID;
  `GAME-0172` remains a carrier with its wording valid under the wider
  boundary.
- Combinations affected: `COMB-0170` keeps the same gene set and its sole
  carrier `GAME-0172`; `GAME-0283` is not a superset of it.
- Novelty claims affected: the `GAME-0172` novelty note remains true; the
  first isolation is unchanged.

## Decision

- Decision: `Rejected` (corrective pass 02, confirmed in pass 03).
- Definitions and boundaries carrier audit: no single portable boundary
  survives both carriers. Street Fighter 6's five Drive techniques are
  universal moves funded by one six-stock reserve whose exhaustion causes
  Burnout, which is what `ACT-298`'s novelty note describes; TEKKEN 8's Heat
  Smash and Rage Art are fighter-specific attacks with universal inputs and
  a state gate, the class of command that `ACT-298` explicitly excludes as a
  Super Art entered as a character command, Heat Burst and Heat Dash are
  universal inputs whose cost is a once-per-round availability or a timed
  state rather than a spent stock, and Heat and Rage are two independent
  states rather than one shared reserve funding one technique family.
  Widening the definition to cover both would have replaced the stock-funded
  boundary with a generic "shared state" predicate that no carrier's
  evidence isolates.
- Decided by: the technique-by-technique command, ownership, gate and
  result audit recorded in the `GAME-0283` record and pass-02 checkpoint.
- Rationale: the committed `Commit one legal Drive technique` wording is restored because it is
  the only boundary its carrier evidence supports; TEKKEN 8 does not carry
  `ACT-298`, its Heat and Rage commands are owned by `ACT-295`, and their
  state eligibility is the entering and unlocking clause of `SYS-837` and
  `SYS-838` and the resource parameter of `ACT-295`. No committed wording,
  carrier, lifecycle or ID changed.
- Implementation links: `ACT-298`, `GAME-0172`, `GAME-0283`,
  `TAXONOMY_CHANGE_045`.
- Superseded pass-01 rationale (history only): the proposal argued that for
  Street Fighter 6 the trigger, the operation, the cost and the exclusions
  stayed true with Drive as the resource parameter and that TEKKEN 8
  committed the same operation with Heat availability, the Heat state or the
  Rage state as the resource; that reasoning is withdrawn.

## Ukrainian review

- The pass-01 draft that gave `ACT-298` a corrected Ukrainian label,
  definition, inclusion and exclusion for the widened boundary under the
  range batch `UK-GAME-0172-0283` was withdrawn with the rejection in pass
  02: the committed Ukrainian entry (`UK-GAME-0172-0172`) remains
  byte-for-byte unchanged, and the `GAME-0172` plain-language card keeps its
  Drive instance. The proposed widening survives only as the superseded
  history recorded in the Decision section above.

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
  lower-ID `CON-269` and `CON-351`. `ACT-298` is restored to its committed
  `Commit one legal Drive technique` wording, `GAME-0283` does not carry it, and the TEKKEN 8
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
