# Taxonomy Change 147: Bounded vehicular arena combat

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-26
- Trigger: `GAME-0409` *Twisted Metal: Black*, original PS2 first Junkyard
  Story arena with Junkyard Dog.
- Scope: admit `ACT-550`, `ACT-551`, `SYS-1092`, `SYS-1093` and `INF-405`
  as Active. Reuse fifteen existing boundaries, including `OBJ-166`. No older
  genome or verified combination changes.

## Problem and accepted change

The first arena is neither a race nor an ordinary on-foot shooter. The
driver cycles carried weapons, may issue a second command to one launched
Special, and weighs limited station repair against hostile pressure.
Shield/freeze share a replenishing energy budget separate from ammunition,
machine-gun heat and turbo. Radar and opponent count disclose the current
arena state. Existing `OBJ-166` already covers eliminating the declared
finite hostile set and retaining the next Story stage; a new arena objective
would duplicate it.

## Transfer and rejection test

- Existing dedicated driving, direct combat, pickup, finite-ammo, heat,
  health/lives and real-time boundaries transfer without revision.
- `ACT-164` is a generic active inventory slot, not in-vehicle weapon
  cycling. `ACT-199` requires a deliberate transfer, not contact pickup.
- `SYS-798` describes personal exertion stamina; the manual's vehicle
  energy attacks use a common automatically recharging meter. `SYS-738`
  remains the distinct machine-gun heat boundary.
- No prior vehicle or shooter signature is retrofitted. Junkyard Dog,
  spiked-ball shape, missiles and exact gauge amounts remain parameters.

## Evidence and limits

- [Sony's original PS2 manual, OCR-hosted
  scan](https://www.passeidireto.com/arquivo/120692120/twisted-metal-black-manual-ps-2)
  directly states controls, pickups, HUD, repair, energy and Junkyard Dog's
  two-step Special. The host is not the rights holder.
- [Original PS2 written Story
  guide](https://gamefaqs.gamespot.com/ps2/378092-twisted-metal-black/faqs/12610)
  corroborates first-arena order and later selection, but no disc was run.
- Exact opponent count, item placement, damage constants and respawn state
  are excluded pending a direct original-disc trace.
