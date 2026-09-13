# Taxonomy Change 035: Treat guardian form as a phase parameter

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-07
- Trigger: independent closure review of `GAME-0274` Hollow Knight.

## Current classification

- `SYS-799` was titled “Transform a sealed guardian into a further attack
  phase”. Its definition required the guardian to become a further form at a
  remaining-health threshold while the encounter and damage state continued.
- `GAME-0262` DARK SOULS III supplied the reviewed carrier. Draft
  `GAME-0277` Cuphead also reuses the same ID for authored boss forms.

## Detected problem

- Hollow Knight's declared guardian retains the same body but advances through
  health-gated stagger cycles into later phases that add falling arena hazards
  to its existing attacks. The attack-set replacement is mechanical; a cosmetic
  form change is not.
- Requiring a visible transformation would force a duplicate System gene for
  the same threshold-to-new-counterplay transition. Ignoring the phase would
  omit a decision-relevant change in safe healing windows and movement.

## Evidence

- The full textual False Knight reference records the health/stagger thresholds,
  continuing encounter, later phase numbering and added falling-hazard attacks:
  <https://hollowknight.wiki/w/False_Knight>.
- Carrier evidence: the bounded decompositions for
  [`GAME-0262`](../../knowledge/games/a-f/dark-souls-iii.md) and
  [`GAME-0274`](../../knowledge/games/g-l/hollow-knight.md).
- Counterevidence considered: a mere stagger that only exposes a damage window
  remains excluded. Hollow Knight qualifies because subsequent attack phases
  add hazards after the threshold rather than only pausing the guardian.

## Proposed change

- Rename `SYS-799` to “Advance a sealed guardian into a health-gated attack
  phase”.
- Make remaining-health or stagger threshold, optional visible transformation,
  changed attack set and added arena hazard parameters.
- Keep the same ID, lifecycle and all earlier signatures.

## Genome and combination impact

- `GAME-0274` gains one lower-ID reuse, `SYS-799`.
- No earlier reviewed signature, combination gene set or lifecycle changes.
- Definition and Active totals do not change.

## Decision

- Decision: `Accepted`.
- Decided by: independent lower-ID scan and two-way transfer test.
- Rationale: both carriers preserve encounter identity and accumulated progress
  while a threshold invalidates earlier counterplay by changing the attack set.
  Body transformation is presentation, not the boundary.
- Implementation links: `SYS-799`, `GAME-0262`, `GAME-0274`.

## Change history

- 2026-09-07 — created and accepted during the independent `GAME-0274`
  closure unit.
