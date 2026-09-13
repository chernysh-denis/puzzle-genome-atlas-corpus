# Taxonomy Change 056: Remove carrier assumptions from reusable Sekiro mechanics

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-10
- Trigger: `GAME-0288` — Sekiro™: Shadows Die Twice - GOTY Edition.
- Scope: wording generalisation only; no lifecycle, existing signature,
  combination or family assignment changes.

## Problem

Six lower-ID Active genes already describe mechanics required by the bounded
Sekiro packet, but their wording retained incidental properties of their first
carrier: a mandatory grab, a consumable hook, a depleting rather than filling
stability meter, compulsory hook consumption, the noun `grapple` inside a
stealth predicate, or reachability updates only after architecture changes.
Duplicating those records for Sekiro would encode resource source, animation or
display direction rather than a new player decision or state transition.

## Decision

- `ACT-235` becomes **Neutralise an unaware reachable hostile at close range**.
  Grabbing and body movement remain Cyberpunk parameters; Sekiro's stealth
  Deathblow shares the close unaware-target commitment.
- `ACT-361` becomes **Commit a grappling-line approach**. A reusable ability and
  carried consumable charge are alternative availability parameters; the
  action is the aimed tethered approach.
- `SYS-409` becomes **Convert stability-threshold crossing into a critical
  opening**. Whether the interface fills Posture or depletes stance is a
  presentation direction.
- `SYS-653` becomes **Resolve grappling-line attachment and approach**. The
  attachment and traversed tether path are invariant; carried-stock
  consumption remains independently represented for NARAKA by `CON-533`.
- `CON-335` removes the carrier noun `grapple` from its stealth predicate while
  preserving awareness, reach, relative position and disallowing combat state.
- `INF-043` allows reachability marking to update whenever local reachability
  changes, including a moving character entering grapple range; architecture
  reconfiguration is one carrier parameter.

The matching Ukrainian labels and definitions receive the same portable
boundaries in `UK-GAME-0288`. Existing evidence is retained and Sekiro is added
as support.

## Checks against lower-ID meaning

- `ACT-235` remains a close neutralisation performed before active detection.
  It does not absorb alert combat or the Posture-break finisher `ACT-419`.
- `ACT-361` remains the player commitment to an aimed tethered approach. It
  does not absorb eligibility display (`INF-043`) or resolution (`SYS-653`).
- `SYS-409` remains the threshold that opens a critical opportunity. It does
  not absorb the player finisher, temporary display or multi-marker defeat.
- `SYS-653` remains attachment followed by movement of the user along a tether.
  It does not absorb inventory stock or target-neutralisation rules.
- `CON-335` remains the unaware, reachable close-target gate. It does not cover
  staggered alerted targets governed by `CON-589`.
- `INF-043` remains current selectable-destination or attachment reachability.
  It does not become a full route overlay or an enemy-awareness display.

## Migration result

- Existing game signatures changed: `0`.
- Existing combination gene sets changed: `0`.
- Lifecycles changed: `0`.
- New aliases or merged IDs: `0`.
- Definition records generalised: `6`.
- New supporting carrier: `GAME-0288`.

## Rejection condition

Reopen this decision only if a later carrier demonstrates that any
generalisation joins separable player commitments, legality predicates,
information surfaces or state transitions. A different animation, meter
direction, hook inventory source, character, boss or terrain skin is not
sufficient.
