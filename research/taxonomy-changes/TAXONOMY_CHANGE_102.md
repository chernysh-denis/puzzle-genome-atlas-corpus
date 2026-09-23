# Taxonomy Change 102: Preserve active reflection, context disclosure and giver settlement

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: `2026-09-22`
- Trigger: `GAME-0363` The Legend of Zelda: Ocarina of Time complete
  lower-ID transfer test.
- Scope: three new Active boundaries, one System Behaviour, one Information
  and one Objective; no earlier lifecycle or signature changes.

## Problem

The existing vocabulary covers a held guard, live combat, an authored dungeon,
earned Map/Compass disclosure and the original NES Zelda's passive shield and
contact-awarded Triforce fragment. Those boundaries do not express the first
N64 dungeon's actively returned projectile creating a conversation window,
the field-facing action icon that discloses what one contextual button will do
before its press, or a boss victory followed by a separate giver-awarded
persistent story token before next-region entry.

## Accepted change

- Add `SYS-994` for an incoming shot reflected by actively held protection
  into its source, changing that source's interaction state.
- Add `INF-372` for live contextual command text and focus disclosure.
- Add `OBJ-210` for boss, exit and subsequent story-token giver settlement.
- Reuse `ACT-437`, `ACT-494`, `ACT-341`, `SYS-605`, `SYS-931`, `INF-356` and
  other fitting lower-ID boundaries. A `2-3-1` Scrub order, switch identity,
  eye timing and temporary stick flame are route parameters, not extra genes.

## Complete lower-ID transfer test

- `SYS-932` protects passively while facing a compatible projectile; here the
  player must hold the Deku Shield and the returned shot stuns its source.
- `SYS-215` resolves general directly commanded combat, but alone does not
  encode the defender-to-source projectile reversal that opens SPEAK.
- `INF-179` reveals the visible room and `INF-356` joins earned map layers;
  neither changes the displayed legal meaning of A with the current focus.
- `INF-295` and `INF-304` disclose special temporary close follow-ups only
  after combat, not ordinary OPEN/SPEAK/CHECK across world contexts.
- `OBJ-191` credits a directly collected first Triforce fragment in the NES
  dungeon. The Emerald is awarded by the Great Deku Tree after leaving the
  boss room. `OBJ-080` additionally requires crossing into a new region,
  which this packet explicitly stops before.
- `SYS-063` and keyed-door constraints are rejected: Nintendo's N64 manual
  explicitly excludes small keys from the earliest dungeons, and no reviewed
  first-Deku-Tree route spends one.

## Migration and validation expectation

Append `SYS-994`, `INF-372` and `OBJ-210`, preserve all lower-ID signatures,
add reviewed Ukrainian definitions and validate the complete `GAME-0363`
genome. A source-bounded control must reject passive shield resolution,
invented early keys, boss-death-only success and an Emerald granted after the
excluded forest departure.
