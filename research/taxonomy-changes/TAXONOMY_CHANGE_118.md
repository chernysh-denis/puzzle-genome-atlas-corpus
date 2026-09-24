# Taxonomy Change 118: Timed worm-team artillery on mutable ground

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-24
- Trigger: `GAME-0379` Worms Armageddon, the configured original-PC
  non-network two-team one-round artillery packet.
- Scope: nine additive Active genes; no earlier game signature, lifecycle or
  verified combination changes.

## Problem

The Team17 manual describes a worm walking to a firing line, selecting and
aiming an arm, launching it under wind and physical flight, altering terrain
and reducing or displacing enemy worms. Timed team turns and the later
Sudden Death waterline determine which team remains. Existing direct agent
navigation (`ACT-008`), physical projectile flight (`SYS-146`) and mutable
combat ground (`SYS-324`) transfer. They do not by themselves encode a mobile
worm's weapon commitment, damage and drowning, scheduled team member, disclosed
wind or the last-team terminal.

## Accepted change

- `ACT-520` captures aimed shot commitment from a mobile active worm.
- `SYS-1030` resolves blast energy loss and displacement; `SYS-1031` removes
  zero-energy or drowned worms; `SYS-1032` advances lethal Sudden Death water;
  `SYS-1033` couples eligible projectile flight to disclosed wind.
- `CON-686` limits control to the rotating scheduled worm and one committed
  weapon opportunity; `INF-386` exposes energy, terrain, wind and turn state.
- `OBJ-221` requires a surviving team after opposing elimination;
  `TIM-028` distinguishes countdown-bounded team windows and post-shot physics
  settlement from chess's one-action turn.

## Lower-ID transfer and rejection test

- Reuse `ACT-008`, `SYS-146` and `SYS-324` for direct movement, ballistic
  contacts and bounded combat-ground craters. Their existing inclusion and
  exclusion boundaries fit without assigning them a new ID.
- `ACT-113` assumes a fixed launcher; here the worm can change its firing
  origin during its timed turn. `SYS-292` covers typed transient grenade
  fields but does not by itself describe knockback, water death or the
  selected Bazooka. `SYS-423` includes recoverable squad states, absent from
  this one-round no-revival packet. `TIM-004` hands over after each single
  action, whereas a Worms turn permits movement before one shot and waits for
  physical settling.
- The deterministic lower-ID scan selected three tied-near games at the exact
  maximum: The Stanley Parable: Ultra Deluxe, Half-Life 2 and Captain Toad:
  Treasure Tracker. The canonical game record explains all three; these are
  mathematical neighbours, not claims of equivalent genre or objective.

## Evidence and limits

The [Team17-authored PC manual preserved as
HTML](https://manualzz.com/doc/62252192/team17-worms-armageddon-manu%C3%A1l)
documents game setup, timed turns, weapon controls, wind, health, drowning,
Sudden Death and winner. The [Team17 publisher
page](https://www.team17.com/games/worms-armageddon) confirms product
identity. No executable or physical match was inspected; coefficients,
generated terrain and precise simultaneous elimination remain unclaimed.
The configured two-weapon scheme intentionally excludes crates and advanced
arms rather than asserting that the full product lacks them.
