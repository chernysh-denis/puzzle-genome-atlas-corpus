# Taxonomy Change 006: Merge persistent-body direct-control transfer

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-08-14
- Trigger: `REGISTRY_NORMALISATION_004` Action boundary audit

## Detected problem

`ACT-052` switched direct navigation and follower-command authority between two
persistent Pikmin 4 leaders. `ACT-055` transferred The Swapper's unique direct-
control locus to an existing clone while the former body remained present.
Both commands select another eligible persistent body, move one unique direct-
control locus to it and leave the former body in the same world state under
non-locus rules.

Leader class, target acquisition, follower coupling and former-body behaviour
change the command's parameters and downstream consequences, not its authority.
The transfer test succeeds in both directions without losing any available
player command.

## Change

- Generalise `ACT-052` to **transfer direct control among persistent bodies**.
- Add The Swapper evidence and target / former-body parameters to `ACT-052`.
- Replace `ACT-055` with `ACT-052` in The Swapper and `COMB-0038`.
- Mark `ACT-055` as `Merged` and retain it as a historical alias.

## What does not change

- `ACT-054` still owns creation of a new clone body.
- Shared clone input, active-device permission and local collision divergence
  remain System/Constraint records.
- Pikmin follower groups and The Swapper synchronized clones remain distinct
  state models.
- No combination gains a second complete supporting genome.

## Impact

- Active genes: 486 → 485.
- Reused active genes: 118 → 119.
- Active singleton genes: 368 → 366.
- Active-gene usages remain 1031.

## Decision

- Decision: `Accepted`.
- Rationale: body class was duplicated inside two records for the same direct-
  control transfer authority.
