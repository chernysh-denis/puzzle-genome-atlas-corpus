# Taxonomy Change 132: adjustable tether and elastic platform route

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-09-24
- Trigger: `GAME-0394` original PS3 *LittleBigPlanet 2*, one-player
  post-level-link *Grab and Swing* route.
- Scope: admit `ACT-531`, `SYS-1055`, `SYS-1056` and `CON-693` as Active;
  no existing signature, lifecycle or combination is changed.

## Problem and accepted change

The current grappling pair `ACT-361`/`SYS-653` describes a line committed to
an eligible target and an approach that ends on arrival, collision or
release. *Grab and Swing* instead keeps the avatar suspended below the
anchor, permits lateral steering and reeling, then preserves release
momentum. `ACT-531` records the player's attachment/length/release choice;
`SYS-1055` records the continuing anchor-bound motion. The hook cannot
attach to arbitrary scenery, so `CON-693` isolates compatible reach and
material from the physical swing. Contact with a bounce pad adds a separate
automatic launch impulse, `SYS-1056`, rather than an ordinary jump input.

## Transfer and rejection test

`ACT-361`/`SYS-653` remain correct for NARAKA and Sekiro's selected-anchor
approaches. `ACT-479` still requires alternating tether swing with an
aerodynamic glide and is not transferred to this pad route. `CON-533` requires
finite carried grappling stock and is rejected for the reusable LBP2 hook.
The `It Takes Two` placed-nail swing anchor is a candidate for a later
review-on-touch reuse check, but its existing two-player role partition and
signature are not silently migrated. `SYS-1056` describes a contact impulse,
not every airborne body or an independently moving lift. Ordinary depth
navigation stays `ACT-008`; sponge colour, line length, pad placement and
final flag geometry are carrier parameters, not further IDs.

## Evidence and limits

- [PlayStation's official LBP2 feature list](https://blog.playstation.com/2010/12/17/littlebigplanet-2-update-music-sequencer/)
  names both Grappling Hook and Bounce Pads but not their level-specific
  placement.
- The independent [GameFAQs *Grab and Swing* walkthrough](https://gamefaqs.gamespot.com/ps3/954843-littlebigplanet-2/faqs/61926)
  and [Gamepressure route](https://www.gamepressure.com/littlebigplanet2/grab-and-swing/z62aab)
  describe attachment to sponges, reel control, steered release, pad contact,
  eligible switch pull and the electric-floor race.
- No PS3 binary or direct movement trace was inspected. Exact velocity,
  collision and checkpoint numbers remain unmeasured parameters.
