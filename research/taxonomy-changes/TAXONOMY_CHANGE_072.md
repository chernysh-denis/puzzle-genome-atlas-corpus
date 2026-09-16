# Taxonomy Change 072: Generalise the directly steered personal-mount boundary

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-13
- Trigger: `GAME-0297` MONSTER HUNTER RISE complete lower-ID Action scan.
- Scope: wording and support for `ACT-247`; no earlier game signature,
  combination gene set, family membership or lifecycle changes.

## Problem

`ACT-247` already owns calling, mounting and directly steering a personal field
mount, but its title named Torrent's spectral presentation. MONSTER HUNTER RISE
provides the same player-control invariant through a living Palamute: the hunter
calls the personal Buddy, mounts, directly steers ground travel, may dash, jump
or use allowed mounted actions, and dismounts back into hunter control.

Spectral embodiment is therefore a carrier parameter rather than a portable
action boundary. Keeping it in the title would force a duplicate action whose
only distinction is creature fiction.

## Accepted change

- Rename `ACT-247` from “Call and directly steer a spectral field mount” to
  “Call and directly steer a personal field mount”.
- Replace saddle-specific wording with a general riding state while preserving
  call, mount/dismount, direct steering and allowed mounted actions.
- Add the scoped MONSTER HUNTER RISE Palamute as support.
- Keep target-routed Seikret travel, autonomous vehicles and fast travel
  excluded.

## Complete lower-ID transfer test

- Elden Ring remains the only lower-ID carrier. Torrent is still an unlocked
  personal field mount that can be called, mounted, steered, jumped, used for
  mounted attacks and dismissed; its `GAME-0138` signature is unchanged.
- Monster Hunter Wilds' `ACT-243` stays distinct. Seikret can follow the
  selected scoutfly target route without continuous direct steering and can
  carry a second weapon, so routing and portable armament are not folded into
  `ACT-247`.
- Vehicle-entry and driving genes remain distinct because they govern general
  world vehicles, seating and vehicle systems rather than one callable
  personal field mount.
- Autonomous-companion `SYS-407` stays separate: it resolves Buddy choices
  while unmounted; `ACT-247` owns only the player's call and direct riding
  commands.

No earlier game signature, lifecycle, combination or family membership changes.

## Evidence and confidence

- Evidence quality: `Direct`.
- Confidence: `High` for the portable control invariant. Capcom's maintained
  official manual directly lists Palamute call, mount, movement, dash, jump,
  allowed mounted item use and dismount.
- Source: [MONSTER HUNTER RISE decomposition](../../knowledge/games/m-r/monster-hunter-rise.md),
  claims `MHR-004`, `MHR-008` and `MHR-010`.

## Migration and compatibility

- Stable ID: `ACT-247` is retained.
- Registry: title, wording, parameters and evidence support change only.
- Existing signature: `GAME-0152` is unchanged.
- New signature: `GAME-0297` reuses `ACT-247`.
- Public consumers: resolve by stable ID, so the wording change is compatible.

## Validation expectation

- Repository validation must report no duplicate active definition.
- Lower-ID comparison must scan all 296 earlier game signatures.
- Ukrainian canonical wording must preserve personal availability, direct
  steering, riding state and the distinction from target-routed travel.
- Torrent, Palamute, Seikret, saddle, spectral form and mounted item names
  remain carrier-scoped evidence or parameters; none becomes a canonical gene
  label.
