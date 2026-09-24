# Taxonomy Change 123: a shared racing energy reserve and interim Cup result

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-24
- Trigger: `GAME-0384` F-Zero GX, original GameCube Novice Ruby Cup's first
  Mute City: Twist Road race.
- Scope: five additive Active genes; no prior signature, lifecycle, family
  definition or verified combination changes.

## Problem and accepted change

Existing race genes cover direct steering, event selection, autonomous rivals,
ordered laps, rank and finite acceleration. They do not distinguish the
GameCube game's shared energy buffer, first-lap command prohibition or a
first-race score inside an unfinished five-race championship.

- `ACT-525` isolates a deliberately commanded side or spin attack by the
  machine, not ordinary vehicle contact or a carried item.
- `SYS-1040` couples manual-boost spend, collision damage, Pit Area recovery
  and retirement on further damage after empty energy.
- `CON-689` gates manual boost until completion of the first lap independent
  of current energy amount.
- `INF-390` exposes that shared meter and its post-first-lap colour change.
- `OBJ-226` describes local first-race first place and carried points without
  misreporting an entire Cup trophy or a standalone career race reward.

## Transfer and rejection test

`ACT-290`, `ACT-292`, `ACT-293`, `ACT-309`, `SYS-320`, `SYS-515`, `SYS-516`,
`SYS-691`, `CON-438`, `INF-205`, `INF-208` and `TIM-003` transfer at their
existing boundaries. `INF-204` demands a gear readout absent from the source.
Mario Kart 8 Deluxe's item and drift-charge genes do not apply. Burnout
Paradise's manoeuvre-earned Boost stock is not a damage buffer. `OBJ-134`
requires a self-contained race result/reward and `OBJ-180` a completed Cup;
neither represents this first of five courses. No other game's genome is
changed by this distinction.

## Evidence and limits

- [Nintendo's original GameCube instruction booklet](https://manualzz.com/doc/22999165/nintendo-gx-f-zero-gx-instruction-booklet)
  establishes controls, side/spin attack, three-lap race, five-course Cup,
  points, first-lap booster ban, energy, Pit Areas, retirement and HUD.
- [Nintendo UK product page](https://www.nintendo.com/en-gb/Games/Nintendo-GameCube/F-Zero-GX-267972.html)
  identifies the original GameCube game and the 29-rival shared-energy race.
- [SEGA's archived official course page](https://backup.segakore.fr/f-zero.jp/f-zero_gx/planet_course/mutecity.html)
  identifies Twist Road as Ruby Cup's opening Mute City course.
- No PAL disc execution, input trace or exact numerical energy coefficient was
  observed. The manuscript's simplified zero-energy summary is resolved by
  its explicit official retirement rule: damage after depletion.
