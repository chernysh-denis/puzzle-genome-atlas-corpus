# Taxonomy Change 133: submitted sequence and selective time-cycle reset

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-09-24
- Trigger: `GAME-0395` original English European Nintendo 64 *The Legend of
  Zelda: Majora's Mask*, first Clock Town three-day cycle.
- Scope: admit `ACT-532`, `SYS-1057` and `INF-395` as Active; no existing
  signature, lifecycle or verified combination changes.

## Problem and accepted change

The original Nintendo booklet makes the temporal distinction explicit. The
72-hour moonfall is Game Over, while the player must recover an Ocarina and
submit a known Song of Time sequence to return to the first dawn. Certain
acquired items and songs remain while day-local events and event items reset.
`SYS-140` retains knowledge only, and `TIM-016` would falsely imply automatic
reset at deadline. `SYS-1057` isolates the player-requested, selective reset.
`ACT-532` covers finite non-directional symbolic submissions at addressed
interfaces: the Bomber numeric passcode and the Ocarina note sequence. The
current day/time display is decision-relevant to the tower's final-night gate
and to fatal expiry, so `INF-395` is not a generic date label.

## Transfer and rejection test

TUNIC and Helldivers 2 retain `ACT-106` for cardinal-direction command
strings; this change does not broaden that gene to digits or musical notes.
`INF-336` remains Persona 5 Royal's date/activity-period disclosure rather
than a continuously advancing moonfall clock. *Outer Wilds* retains its
automatic `TIM-016`/knowledge-only `SYS-140` loop. *Prince of Persia: The
Sands of Time* retains its unique artefact objective but rewinds local action,
not a scheduled Town cycle. The exact digits, notes, clock rate and retained
items are parameters, not further genes. No older game was silently migrated.

## Evidence and limits

- [Nintendo's original N64 booklet](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/nintendo_8/Manual_Nintendo64_TheLegendOfZeldaMajorasMask_EN.pdf)
  supplies the 72-hour failure and the chosen Song of Time save/reset rules.
- [Zelda Dungeon's first-three-days route](https://www.zeldadungeon.net/majoras-mask-walkthrough/first-three-days/)
  and [GameFAQs' N64 route](https://gamefaqs.gamespot.com/n64/197770-the-legend-of-zelda-majoras-mask/faqs/56570)
  corroborate the Bomber code, Tear trade, tower, Ocarina and first song.
- No cartridge, executable or direct input trace was inspected; exact
  cartridge-revision behaviour and frame timing remain unmeasured.
