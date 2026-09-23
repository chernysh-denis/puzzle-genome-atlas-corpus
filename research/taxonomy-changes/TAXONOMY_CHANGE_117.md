# Taxonomy Change 117: Continuous tilted-stage ball navigation

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-09-23
- Trigger: `GAME-0378` Super Monkey Ball 2, original English-language
  GameCube Story Mode first-stage packet.
- Scope: six additive Active genes; no earlier game signature, gene
  lifecycle or verified combination changes.

## Problem

The player turns the stage with a continuous Control Stick input; a
monkey-containing ball then rolls under gravity and retained motion. An
unsupported edge or expiring clock fails the current attempt. Goal entry
clears it, while optional bananas and faster completion contribute to score.
Existing direct-avatar navigation, card-commanded ball travel and generic
platform HUD/goal genes do not preserve this indirect physical control and
the Story Mode attempt boundary.

## Accepted change

- `ACT-519` distinguishes continuous playfield tilt from direct avatar
  movement and discrete gravity-frame selection.
- `SYS-1028` captures gravity/inertia response of a supported ball;
  `SYS-1029` separates time-dependent goal scoring from optional banana
  contact already covered by `SYS-037`.
- `CON-685` isolates off-field support loss from `CON-068`'s timer expiry.
- `INF-385` records the live ball/course/clock/speed/score surface without
  importing finite Challenge lives; `OBJ-220` retains the timed fixed-goal
  clear of the avatar-containing ball.

## Lower-ID transfer and rejection test

- Reuse `SYS-037` for optional contact pickups, `CON-068` for a terminal
  deadline and `TIM-003` for live advancement.
- `ACT-008` directly navigates an agent rather than tilting the traversable
  field. `ACT-097` chooses a discrete orthogonal gravity face; it does not
  meter analog slope continuously. `SYS-100` resolves a committed card move
  through a heightfield; its ball is not steered during live motion.
- `INF-347` includes finite platformer lives, absent from the scoped Story
  attempt. `OBJ-014` receives a separate payload; `OBJ-026` requires direct
  avatar navigation. Neither is silently broadened to fit a monkey inside a
  ball whose course is tilted indirectly.
- The complete lower-ID scan and proper-subset combination test are
  deterministic repository results, not a judgement from the series name.

## Evidence and limits

The [original SEGA GameCube instruction booklet, preserved on
Manualzz](https://manualzz.com/doc/54732408/sega-super-monkey-ball-2-user-manual)
states stage tilt, rolling ball, bananas, clock, goal and Story retries. The
[publisher-supplied Nintendo GameCube
page](https://www.nintendo.com/en-gb/Games/Nintendo-GameCube/Super-Monkey-Ball-2-268929.html)
corroborates gravity, inertia and platform hazards. The first-stage name and
banana presence are bounded by contemporary secondary stage guides. No disc,
controller trace, source code or video was inspected; exact *Simple* geometry,
timer, coefficients and score formula remain unclaimed. Challenge Mode,
party games and remakes are excluded.
