# Taxonomy Change 053: Extend the survival-state boundary to fatigue, rest and carried load

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-09
- Trigger: Codex integration review of `GAME-0285` The Long Dark.

## Current classification

- Stable IDs: `SYS-327` — Continuously update metabolism and environmental
  exposure; `CON-281` — Maintain bodily needs, protection and equipment
  viability.
- Existing carriers include `GAME-0141` Rust, `GAME-0142` Project Zomboid,
  `GAME-0178` Subnautica and `GAME-0216` Don't Starve Together where applicable.
- Existing wording already covered health, calories, hydration, temperature,
  activity, protection and recovery, but omitted a distinct fatigue state and
  carried load from the portable boundary.

## Detected problem

- In The Long Dark the same continuous survival loop updates Fatigue from
  activity and rest, while carried load and Fatigue jointly change traversal
  viability, especially at fixed ropes.
- Creating a game-specific fatigue or rope gene would duplicate the existing
  metabolism/exposure system and bodily-viability constraint. The rope is a
  parameter of movement; the resource relation is the transferable mechanism.

## Evidence

- Existing carrier evidence remains in the four reviewed game records named
  above.
- `GAME-0285` claims `TLD-005`, `TLD-006` and `TLD-008` document four Needs,
  Condition, activity/load depletion, sleep recovery and rope consequences.
- Carrier audit: adding fatigue and rest leaves every old `SYS-327` carrier true;
  adding hydration, fatigue and carried load leaves every old `CON-281` carrier
  true because each ruleset instantiates only its relevant parameter subset.
- Counterevidence: equipment durability remains outside `SYS-327` and inside
  the wider viability constraint only where a carrier actually uses it. The
  generalisation does not claim every parameter exists in every game.

## Change

- `SYS-327` adds fatigue to state and rest to its update sources.
- `CON-281` adds hydration, fatigue, carried load, drink and rest to its
  portable viability vocabulary.
- The Long Dark becomes an additional supporting carrier for both IDs.

## Genome and combination impact

- Both IDs remain Active; nothing is merged, split or deprecated.
- No earlier signature changes and no combination changes.
- `GAME-0285` reuses both genes; fixed-rope traversal remains parameterised
  under `ACT-008` rather than creating a quest- or fixture-specific gene.

## Decision

- Decision: `Accepted`.
- Rationale: fatigue and load change the same “continue now or recover/reduce
  burden first” decision already owned by the survival state pair.

## Ukrainian review

- Both Ukrainian records are corrected under `UK-GAME-0141-0285` with natural
  terms for hydration, fatigue, load and rest.

## Change history

- 2026-09-09 — accepted during `GAME-0285`; all prior carrier signatures were
  retained unchanged.
