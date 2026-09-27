# Taxonomy Change 154: Advance Wars terrain-and-day infantry battle

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-26
- Trigger: `GAME-0416` *Advance Wars*, original Game Boy Advance Field Training `Terrain Intel`.
- Scope: admit `ACT-554`, `SYS-1105`, `CON-702` and `INF-409` as Active. No earlier game signature or verified combination changes.

## Problem and accepted change

The mission asks the player to order several infantry on one square-grid map before explicitly ending the whole Orange Star day. Unit-type terrain costs govern reach, while the same terrain supplies defensive cover in health-bearing attacks and counterfire. The R-button intel and highlighted range make this trade-off visible before commitment. Existing selected-piece, generic grid, per-unit order and AI-phase genes cover adjacent structure, but do not isolate this whole-army handoff or the cost-versus-cover exchange. Four typed boundaries capture those decisions without importing later Field Training lessons.

## Transfer and rejection tests

- `ACT-554` requires a deliberate side-wide End that can forfeit unspent unit orders; one soldier's Wait does not qualify.
- `SYS-1105` requires health-bearing direct attack and eligible counterfire altered by defender terrain. An exact damage formula is a parameter, not a new gene.
- `CON-702` requires movement allowance charged by the selected unit's terrain class; mere fixed-grid occupancy is insufficient.
- `INF-409` requires visible present HP, order state, reachable cells and inspectable terrain or unit information. It does not predict the AI's exact next choice.
- Reuse `ACT-014`, `ACT-019`, `SYS-537`, `CON-001`, `CON-011`, `CON-034`, `OBJ-029` and `TIM-018`. Reject `INF-009` and `TIM-005` because the opponent's action is not a committed preview, `CON-410` because its hex and river rules do not transfer, and `SYS-944` because this mission has no speed-ranked activation queue.
- Do not admit base capture, income, production, CO Powers or fog merely because the original booklet also documents them; they are outside `Terrain Intel`.

## Evidence and limits

- [Nintendo's original Advance Wars booklet](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/game_boy_advance_8/Manual_GameBoyAdvance_AdvanceWars_EN_DE_FR_ES_IT.pdf), printed pp. 4–9, 12, 26 and 30, documents controls, direct attack, day progression, terrain and movement. The English section of this multilingual scan was rendered and visually reviewed; its SHA-256 is in the [game analysis](../../knowledge/games/a-f/advance-wars.md).
- [Original-game mission dialogue transcription](https://gamefaqs.gamespot.com/gba/471043-advance-wars/faqs/36404) identifies the second Field Training lesson and its mountain-cost and cover demonstration. [A contemporary Field Training guide](https://www.nintendoworldreport.com/feature/1889/advance-wars-guide-field-training) corroborates the bounded mission.
- No North American cartridge, emulator session, input trace, video or audio was inspected. The European publisher booklet is a rules witness, not proof of exact cartridge revision. The opening enemy count, AI branches and hidden damage formula remain unknown.

## Decision

Accept four new typed genes for `GAME-0416` only, leave earlier signatures unchanged, run deterministic lower-ID comparisons and combination subset checks, and accept only reviewed Ukrainian copy and a legal original illustration of one unit per cell before the local commit.
