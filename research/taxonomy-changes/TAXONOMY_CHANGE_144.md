# Taxonomy Change 144: Four-panel charted stepping

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-26
- Trigger: `GAME-0406` *DanceDanceRevolution*, one song on the Konami
  `GN845-UC` arcade cabinet documented in 1998.
- Scope: admit `ACT-545`, `SYS-1085`, `INF-402` and `OBJ-239` as Active;
  reuse `SYS-1013`, `INF-299` and `TIM-003`. No earlier genome or verified
  combination changes.

## Problem and accepted change

The contemporary operator manual shows four foot panels matching upward
arrows, timing-based five-class judgement, a live Dance Gauge that can end
the song early, and a ranked song result. `ACT-545` captures the physical
direction-and-beat step. `SYS-1085` captures the authored four-lane chart
and verdict. `INF-402` exposes both future step direction and present danger.
`OBJ-239` terminates one chart at a viable-gauge ranked result.

## Transfer and rejection test

- Guitar Hero III shares live chart survival through `SYS-1013` and real
  time `TIM-003`, but its `ACT-508` requires fret selection plus a strum,
  `SYS-1010` evaluates that input and sustains, `INF-379` bundles guitar
  meter/charge displays, and `OBJ-215` expects stars and streak statistics.
- PaRappa's `ACT-533` and `SYS-1058` alternate a teacher phrase and later
  answer, not continuously arriving floor-direction arrows.
- `ACT-261` expressly excludes a rhythm sequence whose notes constitute
  the whole objective. The present case is not a one-off minigame check.
- Reuse `INF-299` for judgement counts plus an aggregate letter rank.
  Foot-panel direction, song name, cabinet setting and grade labels are
  parameters, not separately multiplied genes.

## Evidence and limits

- [Konami's 1998 `GN845-UC` operator
  manual](https://www.hackmycab.com/downloads/manuals/Dance%20Dance%20Revolution%20(Operators%20Manual)%20(Model%20GN845-UC).pdf),
  pp. 11 and 19, is the direct publisher-authored source.
- No ROM, cabinet, direct-play trace, chart timing, licensed song inventory
  or Good-to-gauge effect was verified. The selected operator configuration
  is permitted by the manual, not asserted as every machine's default.
