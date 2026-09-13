# Taxonomy Change 040: Generalise focused-shot advantage beyond stagger

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-08
- Trigger: Claude calibration pass 01 for `GAME-0280` Resident Evil 2 (2019
  remake), under the authority granted by
  `docs/CLAUDE_GAME_ANALYST_QUALITY_PROTOCOL_V2.md`.

## Current classification

- Exact wording or stable IDs: `SYS-776` — Convert sustained weapon aim into
  focused-shot advantage, whose definition required the focused shot to have
  "increased stagger or critical-result likelihood"; `INF-303` — Weapon
  reticle exposes current aim-focus state, whose definition tied the disclosed
  state to a shot "whose stagger or critical-result relation depends on it".
- Files and entries affected: the System Behaviour and Information registries;
  the Ukrainian gene localisation for both IDs; the draft `GAME-0280`
  decomposition; generated indexes and research artifacts.
- Original evidence or rationale: both genes were first isolated for
  `GAME-0249` Resident Evil 4 (2023 remake), whose official manual describes
  focused aim through its stagger and critical consequences. The wording
  encoded that carrier's disclosed consequence as the boundary.

## Detected problem

- What is incorrect, ambiguous or at the wrong type: Capcom's official
  Resident Evil 2 web manual states that the reticle becomes smaller the
  longer the player aims, that shots at the smallest reticle are more precise
  and pack more power, and that moving or firing resets it. The transition is
  identical — sustained readied aim converges the reticle to a focused state
  that improves the accepted shot — but the improved quantity is precision and
  damage rather than stagger or critical likelihood. Under the old wording a
  second carrier of the same mechanism would need a duplicate gene.
- How the problem was found: the complete same-series delta table against
  `GAME-0249` during the `GAME-0280` reuse-first scan.
- Why this changes decision structure rather than terminology or theme: the
  player's decision is the same in both carriers — wait for focus or fire now
  — and the improved shot quantity is a parameter of that trade-off, not a
  different transition or disclosure.

## Evidence

- Primary sources: Capcom's official Resident Evil 4 web manual (already
  cited by `GAME-0249`) and the official Resident Evil 2 web manual, Steam
  English edition, pages Actions (`page/2/2`), Game Screen (`page/3/1`) and
  Loading Tips (`page/7/1`, "Improving Your Aim").
- Reproducible transitions: the `GAME-0249` focused-shot row and the
  `GAME-0280` row "Hold aim without moving until the reticle closes, then
  fire".
- Analysed games checked: `GAME-0249` and `GAME-0280`; no other carrier
  exists.
- External systems or literature checked: none beyond the two official
  manuals; no third carrier is asserted.
- Counterevidence: Resident Evil 4 additionally keeps the focused reticle
  through some movement while Resident Evil 2 resets on movement. That is the
  reset-input parameter, not a different boundary; both carriers reset on
  firing.

## Proposed change

- Old classification: focused shot advantage restricted to stagger or
  critical-result likelihood; disclosed focus state tied to those relations.
- Proposed classification: `SYS-776` — the focused shot gains its declared
  advantage in precision, damage, stagger or critical-result likelihood, and a
  declared reset input reopens the reticle; `INF-303` — the reticle discloses
  the focus state before a shot whose declared precision, damage, stagger or
  critical relation depends on it.
- Definitions and boundaries: labels unchanged; the excludes lists are
  unchanged; parameters gain the reset input and the precision and damage
  relations.
- Lifecycle effects: none.
- What does not change: the `GAME-0249` signature, `COMB-0247`, every earlier
  reviewed signature, every lifecycle state and every stable ID.

## Genome and combination impact

- Genes added, deprecated, merged or split: none.
- Games requiring annotation: `GAME-0280` reuses both generalised IDs;
  `GAME-0249` remains a carrier with its wording valid under the wider
  boundary.
- Combinations affected: `COMB-0247` keeps the same gene set; it gains no
  second carrier because `GAME-0280` lacks its grid, parry and pressure
  members.
- Novelty claims affected: the `GAME-0249` novelty notes remain true; the
  first isolation is unchanged.

## Decision

- Decision: `Accepted`.
- Decided by: the complete same-series delta table, a two-way transfer test
  between both official manuals and the lower-ID scan recorded in the
  `GAME-0280` record and calibration checkpoint.
- Rationale: substituting "more precise and stronger" for "more stagger or
  critical" in either direction leaves the trigger, the focus transition, the
  reset and the wait-or-fire decision unchanged. The advantage is a parameter.
- Implementation links: `SYS-776`, `INF-303`, `GAME-0249`, `GAME-0280`.

## Ukrainian review

- `SYS-776` and `INF-303` receive corrected Ukrainian label, definition,
  inclusion and exclusion parity for the widened boundary in the same unit.

## Change history

- 2026-09-08 — created and accepted during Claude calibration pass 01 for
  `GAME-0280`, before that draft's independent audit.
