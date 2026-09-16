# Taxonomy Change 070: Generalise authored-checkpoint restoration beyond missions

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Date: 2026-09-13
- Trigger: `GAME-0293` Ori and the Will of the Wisps complete lower-ID System
  Behaviour scan.
- Scope: wording and support for `SYS-369`; no earlier game signature,
  combination gene set, family membership or lifecycle changes.

## Problem

`SYS-369` already owned the portable resolution in which failure discards the
failed transient state and restores the latest authored checkpoint. Its label
and definition unnecessarily assumed both a mission context and a player-
chosen retry. Ori and the Will of the Wisps supplies the same state transition
inside ordinary authored traversal, where lethal failure returns automatically
to a dense recent checkpoint.

Creating a second automatic-checkpoint gene would duplicate the checkpoint
restoration boundary. Reusing `SYS-610` would instead overclaim retention of
currency, inventory and completed progression that the accepted Ori sources do
not enumerate.

## Accepted change

- Rename `SYS-369` from “Restore an authored mission checkpoint after failure”
  to “Restore an authored checkpoint after failure”.
- Replace “mission-critical condition” with “critical condition”.
- Permit either an automatic return or a chosen retry.
- Replace “mission variables” with “authored variables” in the parameters.
- Add `GAME-0293` as a carrier for lethal failure returning to a recent
  automatic checkpoint.

The invariant remains unchanged: failure ends the current attempt segment,
discards its transient damage and positions, and restores an authored
checkpoint snapshot. Whether the checkpoint belongs to a mission, chapter or
ordinary route, and whether the return is automatic or confirmed, are
parameters.

## Complete lower-ID transfer test

- `SYS-369` already covers Grand Theft Auto V, Cyberpunk 2077, Need for Speed
  Payback and Resident Evil 2 (2019 remake). Their critical failures still
  restore authored checkpoints and retain their existing parameters.
- `SYS-610` remains distinct because it asserts a complete no-drop retained set
  across checkpoint death. Ori's written sources establish nearby checkpoint
  restoration but not that full retained-set contract.
- `SYS-399`, `SYS-410` and `SYS-849` remain distinct because each couples
  checkpoint return to a recoverable mark or immediate resource loss.
- `SYS-624` remains activity-specific because it restores an authored activity
  after a complete solo wipe rather than one avatar's ordinary lethal failure.
- `TIM-007` remains distinct because it permits restoration of an earlier saved
  history for a different continuation; failure restoration need not offer
  branch selection.

No earlier game signature, lifecycle, combination or family membership changes.

## Evidence and confidence

- Evidence quality: `Corroborated`.
- Confidence: `Medium` because Ori's exact automatic-checkpoint placement and
  post-death restored fields rest on contemporary written secondary sources;
  the more limited invariant of recent checkpoint restoration is independently
  stated and does not import an unevidenced retained-resource set.
- Source: [Ori and the Will of the Wisps decomposition](../../knowledge/games/m-r/ori-and-the-will-of-the-wisps.md),
  claims `ORI-010`–`ORI-013`.

## Migration and compatibility

- Stable ID: `SYS-369` is retained.
- Registry: wording and evidence support change only.
- Existing signatures: unchanged.
- New signature: `GAME-0293` reuses `SYS-369`.
- Public consumers: resolve by stable ID, so the wording change is compatible.

## Validation expectation

- Repository validation must still report no duplicate active definition.
- Lower-ID comparison must scan all 292 earlier game signatures.
- Ukrainian canonical wording and the carrier-local plain-language card must
  preserve failure, discarded transient state, authored checkpoint and resumed
  control without adding an unverified currency or inventory promise.
