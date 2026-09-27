# Taxonomy Change 165: Directed light and Taken vulnerability

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-27
- Trigger: `GAME-0427` *Alan Wake*, original Xbox 360 first post-tutorial Taken packet.
- Scope: admit `ACT-566`, `SYS-1126`, `SYS-1127`, `SYS-1128` and `INF-419` as Active. Reuse direct movement, dodge, aimed attack, battery refill, real-time combat, HUD, one-encounter defeat and live timing. No earlier signature or verified combination changes.

## Problem and accepted change

An ordinary firearm shot does not bypass the Taken's darkness shroud. Directed flashlight contact progressively removes it, boosted contact does so faster at a charge cost, and a bright break cue marks when conventional bullets can hurt the target. Releasing boost restores charge despite the normal beam remaining lit. One generic “light reveals enemy” gene would lose both the damage gate and the distinct rechargeable resource condition.

## Transfer and rejection tests

- Reuse `ACT-008`, `ACT-161`, `ACT-223`, `ACT-453`, `SYS-215`, `SYS-791`, `INF-119`, `OBJ-029` and `TIM-003` with bounded encounter parameters.
- Reject `ACT-183`: its canonical action reloads magazine-fed weapons, not a revolver cylinder. Reloading is not needed to establish this selected one-foe loop.
- Reject `ACT-543` and `SYS-1080`: *Luigi's Mansion* suppresses light before surprising a ghost into a brief heart-exposure state, not ongoing darkness erosion.
- Reject `SYS-754`: its portable light consumes energy simply while active; Alan's ordinary unboosted flashlight remains lit and recharges.
- Reject `SYS-851`: its recovery needs an inactive light; Alan's recovery needs only boost release.
- No separate constraint gene is created for charge, ammunition or target damage legality, which are defined by the admitted action/system transitions.
- Do not infer that the first encountered Taken has regenerating darkness, mandatory-kill progress gating or a fixed hit count.

## Evidence and limits

The [original Microsoft/Remedy Xbox 360 instruction manual](https://manuals.plus/m/3537e546dddabff38ce730c0e9cb1dcfdb522d89325690ea6ae65575ec6b36c8) directly describes Taken darkness, the contracting corona and bright break, boosted-drain/ordinary-recharge, inserted batteries and revolver inputs. [AlanWake.info's first-hand Episode 1 route](https://www.alanwake.info/2000/05/walkthrough-3-episode-01-dream-sequence.html) identifies one lone post-tutorial Taken before a later pair. No disc or direct play was inspected; exact numeric timing, health, damage and mandatory story gating are not asserted.

## Decision

Accept five bounded new genes only with deterministic comparison, complete Ukrainian presentation, original rule-valid artwork and all repository/browser gates before this unit's one authorised local commit. No push or public publication is authorised by this record.
