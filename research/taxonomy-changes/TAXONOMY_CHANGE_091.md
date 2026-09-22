# Taxonomy Change 091: Separate incapacitated-body relocation from cargo

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: `2026-09-21`
- Trigger: `GAME-0349` Tom Clancy's Splinter Cell complete lower-ID transfer
  test.
- Scope: one new Active Action boundary and supporting-carrier evidence for
  twenty-six reused stealth, mission and persistence boundaries.

## Problem

The vocabulary already represented inventory pickup, bagged objective cargo,
living-subject extraction, stealth neutralisation, local perception and body-
triggered suspicion. It did not represent the player's direct transition of a
dead or unconscious actor into an exclusive carried-body state followed by
placement at a new discoverable world position. That operation matters because
the body's visibility can independently trigger later hostile perception.

## Accepted change

- Add `ACT-491` for carrying and placing one incapacitated world body.
- Keep body discovery and resulting suspicion inside existing perception and
  escalation boundaries; the new Action owns only player-authored relocation.
- Add explicit Splinter Cell carrier evidence to reused boundaries without
  changing operational definitions, lifecycle states or earlier signatures.

## Complete lower-ID transfer test

- `ACT-199` transfers an item into compatible inventory/equipment. An
  unconscious guard remains a world actor and is never converted into stock.
- `ACT-359` carries or throws a bagged objective payload toward a secure region
  and payout. The body is neither bagged loot nor deposited for reward.
- `ACT-466` carries a living mission subject into an extraction vehicle. The
  selected body is already incapacitated and is placed in concealment rather
  than extracted.
- `ACT-341` can initiate a contextual pickup but does not own the resulting
  exclusive carry, movement and freely selected world placement.
- `CON-335` gates the preceding stealth neutralisation; it cannot represent
  later relocation of an already incapacitated actor.
- `SYS-373` admits body discovery as an observer stimulus, while `ACT-491`
  alone owns the player's positional intervention before that discovery.
- Interrogation reuses `ACT-107` because it registers an exact operational
  fact. Forced retinal cooperation is one legal contextual fixture interaction
  under `ACT-341`, not a reusable new action family in this packet.

## Migration and validation expectation

Append `ACT-491` as Active and add reviewed Ukrainian coverage. Existing IDs,
lifecycle states, lower-ID signatures, combinations and family definitions
remain unchanged. Validation must find a twenty-seven-gene `GAME-0349`
signature, complete bilingual presentation, original artwork and an executable
state reconstruction covering light/noise perception, interrogation, lock and
retinal access, nonlethal neutralisation, body placement, mission order,
checkpoint replacement and retained successor control.
