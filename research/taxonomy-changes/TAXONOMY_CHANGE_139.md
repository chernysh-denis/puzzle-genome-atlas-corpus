# Taxonomy Change 139: Classic slicing path and fruit-run response

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-09-25
- Trigger: `GAME-0401` *Fruit Ninja*, original paid iPhone version 1.2
  Classic score run without later power-ups.
- Scope: admit `ACT-537`, `SYS-1071`–`SYS-1074` and `INF-399` as Active;
  no earlier signature or verified combination changes.

## Problem and accepted change

Halfbrick's contemporary version-1.2 note makes one-swipe fruit grouping a
specific scoring rule in Classic, not a later Arcade import. An original
iPhone launch review describes a continuing screen of fruit and bombs where
three misses or one bomb contact ends the score run. Existing random outcome,
score-milestone stock recovery, visible-hazard failure, finite life stock,
score objective and real-time pressure are reused. Six new boundaries retain
the continuous freehand input, mixed live arcs, collision response, one-stroke
scoring, uncut-fruit debit and present-object display.

## Transfer and rejection test

- `ACT-016` traces a fixed-endpoint grid path; Fruit Ninja commits a freehand
  live path through moving bodies. `ACT-027` cuts a selected support link,
  not a set of airborne objects. Hardware is a parameter; path semantics
  justify `ACT-537`.
- `SYS-1066` emits hostile groups into an arena with ship pursuit; these are
  transient fruit and bombs with rising/falling arcs, so `SYS-1071` is not a
  relabelled enemy-spawn gene. `SYS-1072` separates collision response from
  the scoring rule in `SYS-1073` and the uncut-exit debit in `SYS-1074`.
- `CON-113` covers the moving blade's visible bomb contact, while `CON-183`
  covers three outstanding miss marks and possible recovery. A bomb is not a
  third miss. Later-version evidence for score recovery has medium
  version-specific confidence; direct v1.2 testing remains open.
- `INF-001` would claim future volleys were knowable. `INF-399` states only
  currently exposed objects and run counters, without inferring spawn odds.
- Zen, Arcade, power-ups, alternate blades, exact object distributions and
  simultaneous-frame resolution are out of scope, not silently normalised.

## Evidence and limits

- [Halfbrick's May 2010 version-1.2 press
  release](https://www.impulsegamer.com/wordpress/?p=6169) explicitly puts
  three-plus-fruit one-swipe bonuses in Classic and separates Zen.
- [TouchArcade's original iPhone launch
  review](https://toucharcade.com/2010/04/21/fruit-ninja-review-all-ninja-hate-fruit/)
  directly describes swipes, three missed fruit and instant bomb loss.
- [Halfbrick's later general
  guide](https://www.halfbrick.com/blog/the-ultimate-beginners-guide-to-fruit-ninja)
  explains Classic's continuing loop, combo and random critical, but also
  describes later modes and purchasable advantages not included here.
- [Pocket Gamer's Halfbrick interview](https://www.pocketgamer.com/fruit-ninja/halfbrick-shares-10-tips-tricks-and-secrets-for-fruit-ninja-on-ios/)
  and a [December 2010 adjacent-port
  guide](https://www.xboxachievements.com/forum/topic/256162-achievement-guideroadmap-wp8-version/)
  corroborate the 100-point miss-mark recovery; neither is a direct reading
  of the original paid iPhone v1.2 binary. No executable or audiovisual trace
  was inspected.
- The original editorial illustration shows one stroke cutting three fruit
  while a bomb remains outside the path. It is not a screenshot, logo or
  evidence of exact launch trajectories.
