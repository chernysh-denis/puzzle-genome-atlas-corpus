# Taxonomy Change 008: Remove control method from fixed-receiver objective

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-08-14
- Trigger: `REGISTRY_NORMALISATION_004` Objective boundary audit

## Detected problem

Three Objective records described the same terminal relation while repeating
how the payload was controlled:

- `OBJ-014`: indirect physics/environment intervention in Cut the Rope;
- `OBJ-034`: avatar-carried destructive delivery in Bonfire Peaks;
- `OBJ-036`: card-commanded ball delivery in Golf Peaks.

All three complete a bounded attempt when one designated payload contacts,
enters or is committed to one fixed receiver. Indirect physics, carried pose and
card-directed displacement are already represented by Action, System and
Constraint genes. Keeping them in Objective duplicated another type's work.

## Change

- Generalise `OBJ-014` to **deliver designated payload to fixed receiver**.
- Treat payload identity, accepted entry, preservation/consumption and control
  pathway as parameters or cross-type context.
- Replace `OBJ-034` in Bonfire Peaks and `COMB-0055` with `OBJ-014`.
- Replace `OBJ-036` in Golf Peaks and `COMB-0057` with `OBJ-014`.
- Mark `OBJ-034` and `OBJ-036` as `Merged` historical aliases.

## What does not change

- `OBJ-010` remains overlap with a mutable rule-defined goal.
- `OBJ-039` remains complete-footprint extraction through a boundary gap.
- Bonfire consumption, carry clearance and elevation access remain explicit.
- Golf Peaks card consumption and staged heightfield traversal remain explicit.
- Cut the Rope rope/physics control remains explicit.

## Impact

- Active genes: 484 → 482.
- Reused active genes: 120 → 121.
- Active singleton genes: 364 → 361.
- Golf Peaks/Bonfire Peaks similarity: `4 / 14 = 0.285714` →
  `5 / 13 = 0.384615`.
- No combination gains a second complete supporting genome.

## Decision

- Decision: `Accepted`.
- Rationale: an Objective records the terminal relation, while control method
  belongs to the action and transition layers.
