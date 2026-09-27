# Taxonomy Change 136: nested timed microgame course

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-09-25
- Trigger: `GAME-0398` *WarioWare, Inc.: Mega Microgame$!*, original North
  American GBA introductory course through the tenth-slot boss.
- Scope: admit `ACT-534`, `SYS-1061`–`SYS-1063`, `INF-397` and `OBJ-234`
  as Active; no existing genome or verified combination changes.

## Problem and accepted change

The Nintendo GBA booklet and two contemporary original-game written guides
describe brief command-driven tasks chained without a menu, a four-life run,
increasing speed and a designated tenth-slot boss. Local task expiry does not
end the whole run while lives remain. The new genes isolate the changing
task response, automatic course handoff, pace increase, local result,
transient instruction/state display and boss-gated course terminal. Existing
`SYS-004`, `CON-068`, `CON-183` and `TIM-003` retain their usual boundaries.

## Transfer and rejection test

- `ACT-223` is tied to an incoming hostile attack, while introductory tasks
  may ask for a catch, stop, jump or steer. `ACT-533` echoes a demonstrated
  musical phrase rather than interpreting a new imperative.
- `INF-067` discloses task reward and threat, which Wario's one-word prompt
  does not. `SYS-004` selects a random identity but does not express the
  fixed boss slot or automatic handoff. `CON-068` terminates one task at
  expiry, while `CON-183` governs the shared stock and whole-run failure.
- The exact prompt text, car sprite, A/D-pad mapping and nominal seconds
  stay parameters. Neither a new combination nor a prior-game signature
  mutation is justified.

## Evidence and limits

- [Official Nintendo GBA booklet](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/game_boy_advance_8/Manual_GameBoyAdvance_WarioWareIncMinigameMania_EN_DE_FR_ES_IT.pdf),
  English pages 8–9 and 18–19, documents controls, short-stage structure
  and tenth boss. It bears the PAL subtitle; exact NA binary identity is
  not inferred.
- [Shdwrlm3's 2003 original-GBA guide](https://gamefaqs.gamespot.com/gba/589714-warioware-inc-mega-microgame/faqs/22353)
  and [MoonSaultKid's independent 2003 guide](https://gamefaqs.gamespot.com/gba/589714-warioware-inc-mega-microgame/faqs/24737)
  describe opening task selection, lives, pace and named task inputs.
- No cartridge or emulator was played. Exact draw weights, frame windows
  and boss timer semantics are not claimed.
