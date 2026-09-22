# Taxonomy Change 099: Isolate Space Invaders formation pressure, fortress erosion and rack reset

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: `2026-09-22`
- Trigger: `GAME-0360` Space Invaders complete lower-ID transfer test.
- Scope: four new Active boundaries; no lifecycle or earlier-signature change.

## Problem

The vocabulary already represents lateral movement, aimed fire, live projectile
combat, finite-stock recovery, score-earned stock, visible state, hostile-set
clearance and shared real time. Four causal boundaries still fail transfer:

- one formation reverses and descends at an occupied edge while fewer surviving
  members shorten its effective traversal cycle;
- player fire, hostile fire and the low formation all remove persistent pixels
  from the same four fortress masks;
- zero survivors rebuilds both the formation and fortress masks while retaining
  run score and base stock;
- one player-projectile channel rejects another fire request until its current
  projectile settles.

## Accepted change

- Add `SYS-990` for edge-reversing, descending, population-coupled formation
  pressure.
- Add `SYS-991` for persistent fortress-pixel erosion from either side or low
  formation contact.
- Add `SYS-992` for a clearance-triggered successor-rack rebuild that retains
  run stock.
- Add `CON-663` for the one-active-player-projectile legality boundary.
- Reuse ten existing movement, attack, live-combat, recovery, bonus-stock,
  finite-life, information, score, clearance and real-time boundaries unchanged.

## Complete lower-ID transfer test

- `SYS-037`, `SYS-045` and `SYS-960`–`SYS-966` describe PAC-MAN's maze,
  role-targeted pursuit, temporary predator reversal, bonus timing and round
  settlement. Their shared stock and successor-round relations do not cover a
  live edge-coupled firing formation.
- Existing destructible-cover boundaries attach damage to discrete cover
  objects, rebuilding fixtures or authored obstacles. None preserves one pixel
  mask damaged by both projectile directions and by formation contact until
  the rack boundary.
- Existing cadence and escalation boundaries alter clocks, waves, danger tiers
  or authored encounters. None derives effective formation pressure directly
  from the number of surviving members served by one repeated movement cycle.
- Existing ammunition, cooldown and charge gates permit multiple projectiles,
  consume stock or replenish over time. They cannot assert the exact reusable
  single-projectile channel without adding absent resource semantics.
- Existing successor-state resets do not jointly rebuild the hostile formation
  and cover while retaining score and remaining lives.

## Migration and validation expectation

Append four Active IDs, preserve every lower-ID signature, add complete reviewed
Ukrainian coverage and require a fourteen-gene `GAME-0360` signature. The
dedicated state reconstruction must cover a 55-member rack, four fortress masks,
lateral-only motion, one active shot, edge descent, survivor-coupled pace,
bidirectional erosion, the one-time 1,500-point bonus, stock and invasion Game
Over branches, and returned control in a rebuilt successor rack.
