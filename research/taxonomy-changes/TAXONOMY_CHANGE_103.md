# Taxonomy Change 103: Preserve motion delivery and ten-frame score settlement

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: `2026-09-22`
- Trigger: `GAME-0364` Wii Sports original one-player Bowling full lower-ID
  transfer test.
- Scope: seven new Active boundaries; no earlier lifecycle or signature
  changes.

## Problem

The existing corpus can describe an aimed projectile, ballistic collision,
finite launched balls and session score. Those boundaries do not encode a
physically sampled B-release swing, independent lane stance and aim, a rolling
ball whose spin changes the pin-contact cascade, ten-frame delivery entitlement
and deferred strike/spare bonuses, or a separate saved Mii skill evaluation.

## Accepted change

- Add `ACT-498` for pre-release stance and aim adjustment and `ACT-499` for
  the explicit motion-sampled B release.
- Add `SYS-995` for rolling spin and pinfall, `SYS-996` for frame and deferred
  scoring settlement, and `SYS-997` for the saved sport-specific skill level.
- Add `CON-664` for frame-limited deliveries with the tenth-frame exception
  and `INF-373` for frame-indexed pinfall and pending score disclosure.
- Reuse `OBJ-002` for score maximisation and `TIM-003` for real-time sampling
  and ball/pin resolution. Mii identity, bowling-ball properties and the
  undisclosed skill-update formula remain parameters or explicit unknowns.

## Complete lower-ID transfer test

- `ACT-113` fires from a fixed launcher; original Wii Sports Bowling has a
  standing position, separate aim and bodily swing with explicit B release.
- `ACT-413` is a release-timed basket attempt, not a rolling lane delivery.
- `SYS-146` resolves airborne gravity/peg ricochets, not spin-shaped rolling
  and a rack of ten colliding pins.
- `SYS-028` is a generic ordered additive/multiplicative score rule but its
  established boundary concerns ranked merge-stage scoring; it does not
  preserve standing pins, next-delivery strike/spare bonuses or tenth fills.
- `CON-164` tracks a replenishable finite ball stock; Bowling has one ball
  per legal delivery and frame-conditioned eligibility, not an inventory.
- `INF-366` discloses Duck Hunt shots, hit row, pass line and round; it does
  not expose unresolved ten-pin bonuses or the standing pin field.
- `SYS-342` accumulates activity experience and modifiers; Nintendo only
  supports a performance-responsive Mii skill evaluation, not altered
  play capabilities or a known gain formula.
- `OBJ-002` and `TIM-003` fit without any wording change. No verified
  recurring proper-subset combination is created.

## Evidence limits and migration

The original Nintendo manual directly fixes the control scheme, ten-frame
mode, Mii records and rating threshold. Conventional strike/spare arithmetic
is corroborated by United States Bowling Congress scoring rules, not by
executing the Wii binary. Exact physical coefficients and skill formula
remain unknown. Append the seven new records, translate them in the reviewed
Ukrainian layer, and validate the complete nine-gene packet. A deterministic
control must reject automatic release, treating a spare as final before its
next delivery, inventing an eleventh frame or saving a guest-Mii record.
