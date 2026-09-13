# Taxonomy Change 041: Generalise initiative scheduling to per-round re-rolls

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-08
- Trigger: Claude transfer-test pass 01 for `GAME-0281` Darkest Dungeon, under
  the authority granted by `docs/CLAUDE_GAME_ANALYST_QUALITY_PROTOCOL_V2.md`.

## Current classification

- Exact wording or stable IDs: `SYS-388` — Schedule initiative turns and
  refresh action resources, whose definition read "entering combat rolls and
  orders initiative, activates one legal participant or tied allied group at
  a time and refreshes that creature's ordinary movement, Action, Bonus Action
  and Reaction resources on schedule".
- Files and entries affected: the System Behaviour registry; the Ukrainian
  gene localisation for `SYS-388`; the draft `GAME-0281` decomposition;
  generated indexes and research artifacts.
- Original evidence or rationale: the gene was first isolated for `GAME-0148`
  Baldur's Gate 3, whose combat rolls initiative once when combat begins and
  refreshes the fifth-edition resource set at each creature's turn. The
  wording encoded that carrier's cadence and resource names as the boundary.

## Detected problem

- What is incorrect, ambiguous or at the wrong type: Darkest Dungeon orders
  every round of combat by each unit's speed plus a hidden roll of 1 to 8,
  re-rolled at the start of every round, activates one unit at a time with
  heroes winning ties, and gives each unit one action per round. The
  transition is the same — an initiative attribute plus a random component
  orders participants, one participant activates at a time and its per-turn
  authority is refreshed — but the roll recurs every round and the refreshed
  resource is a single action rather than the fifth-edition set. Under the
  old wording a second carrier of the same mechanism would need a duplicate
  gene, which `SYS-356` (a visible stat-ordered queue) does not provide
  because it requires the upcoming sequence to be exposed.
- How the problem was found: the reuse-first scan for the `GAME-0281`
  initiative row, which inspected `SYS-356`, `SYS-388`, `SYS-534`, `SYS-586`
  and `TIM-005` before proposing a new gene.
- Why this changes decision structure rather than terminology or theme: the
  player's decision in both carriers is the same — act with the currently
  activated participant knowing that order is attribute-weighted but random —
  and the cadence of the roll and the names of the refreshed resources are
  parameters of that structure.

## Evidence

- Primary sources: the Baldur's Gate 3 evidence already cited by `GAME-0148`;
  for Darkest Dungeon, Red Hook's own 2020-04-30 Steam announcement
  ("Normally in Darkest Dungeon, at the start of each combat round we roll
  all combatants' initiative to establish a turn order. This initiative is
  the combination of the character's speed plus a die roll. We don't
  explicitly show who will act next"), cited as `P3`, corroborated by the
  in-game Glossary text transcribed by the official wiki ("Speed influences
  the order in which combatants act along with a hidden initiative dice
  roll. Initiative is re-rolled each turn") and its Combat Mechanics page,
  cited as `S2`. The per-round re-roll, the speed-plus-die form and the
  hidden order therefore rest on two independent source families
  (`DD-012a`, `Corroborated | High`); the exact 1–8 die, the hero tie rule
  and the lower-rank tie rule rest on the wiki alone (`DD-012b`,
  `Limited | Medium`) and are parameters, not part of the boundary.
- Reproducible transitions: the `GAME-0148` initiative row and the
  `GAME-0281` row "A battle begins; each round the system orders units by
  speed plus a hidden roll".
- Analysed games checked: `GAME-0148` and `GAME-0281`; `GAME-0144` Clair
  Obscur: Expedition 33 keeps `SYS-356` because its queue is visible and
  extra-turn driven.
- External systems or literature checked: none beyond the two carriers; no
  third carrier is asserted.
- Counterevidence: Baldur's Gate 3 rolls once per combat and exposes the
  order; Darkest Dungeon re-rolls each round and hides it. Both are recorded
  as the re-roll cadence and roll-visibility parameters, and disclosure is
  typed separately (`INF-141` for the visible queue, `INF-002` for the
  hidden roll and `INF-333` for the per-unit remaining-action pips that
  Darkest Dungeon shows without the order).

## Proposed change

- Old classification: initiative rolled on entering combat; refreshed
  resources named as movement, Action, Bonus Action and Reaction.
- Proposed classification: `SYS-388` — entering combat, and again at each
  round boundary where the ruleset re-rolls, rolls and orders initiative from
  each participant's initiative attribute plus a random component, activates
  one legal participant or tied allied group at a time and refreshes that
  participant's declared per-turn action resources on schedule.
- Definitions and boundaries: label unchanged; the excludes list gains the
  battle-start surprise check (`SYS-828`); parameters gain the initiative
  attribute, tie rule, re-roll cadence and roll visibility, and the
  fifth-edition resource names become examples.
- Lifecycle effects: none.
- What does not change: the `GAME-0148` signature, every earlier reviewed
  signature, every lifecycle state and every stable ID.

## Genome and combination impact

- Genes added, deprecated, merged or split: none by this record; `GAME-0281`
  separately adds new genes whose boundaries this record does not touch.
- Games requiring annotation: `GAME-0281` reuses the generalised ID;
  `GAME-0148` remains a carrier with its wording valid under the wider
  boundary.
- Combinations affected: `COMB-0146` keeps the same thirty-four-gene set and
  its sole carrier `GAME-0148`; `GAME-0281` shares only `ACT-008`, `ACT-019`,
  `SYS-388`, `INF-119` and `TIM-001` with that set, so it gains no carrier.
- Novelty claims affected: the `GAME-0148` novelty note remains true; the
  first isolation is unchanged.

## Decision

- Decision: `Accepted`.
- Definitions and boundaries carrier audit: for Baldur's Gate 3 the trigger
  (entering combat), the operation (initiative attribute plus a die orders
  participants), the activation rule (one participant or tied allied group at
  a time) and the refresh (movement, Action, Bonus Action and Reaction at the
  creature's turn) remain true sentence by sentence under the new wording,
  with cadence `once per combat` and visibility `exposed`.
- Decided by: the reuse-first scan and the two-way transfer test recorded in
  the `GAME-0281` record and transfer-test checkpoint.
- Rationale: substituting "each round, hidden, one action" for "once per
  combat, exposed, fifth-edition resources" in either direction leaves the
  trigger, the ordering rule, the one-at-a-time activation and the refresh
  unchanged. Cadence, visibility and resource names are parameters.
- Implementation links: `SYS-388`, `GAME-0148`, `GAME-0281`.

## Ukrainian review

- `SYS-388` receives corrected Ukrainian definition, inclusion, exclusion and
  parity for the widened boundary in the same unit.

## Change history

- 2026-09-08 — created and accepted during Claude transfer-test pass 01 for
  `GAME-0281`, before that draft's independent audit.
- 2026-09-08 — corrective pass 02: the Darkest Dungeon evidence was
  re-graded clause by clause after the Codex audit; the boundary and the
  decision are unchanged, the publisher statement of 2020-04-30 was added
  as independent support, and the die and tie values were recorded as
  `Limited` parameters.
