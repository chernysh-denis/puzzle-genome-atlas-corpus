# Taxonomy Change 180: Pedal-cover gunfight in original arcade Time Crisis

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-09-28
- Trigger: `GAME-0443` *Time Crisis*, original arcade Story Game first Stage 1 Area 1 combat view.
- Scope: admit `SYS-1160`, `SYS-1161`, `CON-717` and `INF-428` as Active. No earlier signature or verified combination changes.

## Problem and accepted change

The player cannot shoot safely from the authored cover. Releasing the Action Pedal both ducks and refills a six-round magazine; pressing exposes the actor to hostile fire and permits a finite volley. The overall stage countdown still runs while hidden. A designated hostile can extend that countdown, while defeating the required local set releases the next authored viewpoint. These transitions are more specific than generic firearm combat or a static cover stance.

## Transfer and rejection tests

- Reuse `ACT-202` for direct posture choice, `ACT-490` for physically aimed display gunfire, `SYS-215` for live combat, `SYS-915` for clearance-gated authored progression, `CON-068` for time expiry, `CON-183` for finite lives, `INF-179` for the current view, `OBJ-029` for finite hostile clearance and `TIM-003` for live progress.
- Reject `SYS-967`: NES Zapper darkness/target-local flash sampling was not established for Namco's calibrated arcade gun. Reject `ACT-226`: there is no free contextual movement along a reachable cover edge in the scoped combat view.
- `SYS-1160` is the automatic cover-linked refill; `CON-717` is the distinct eligibility test for an exposed, loaded shot. A hidden actor may have six rounds and still be unable to fire, while an exposed actor may remain unable to fire after all six are spent. Their predicates therefore cannot be merged.
- `SYS-1161` changes the authoritative countdown only for a designated target. The supporting first-view two-second amount comes from one contemporary route and is treated as a parameter, not a universal constant.
- `INF-428` only exposes current clock/ammunition/lives; it does not reveal future enemy placements or the exact attack schedule.
- No earlier reviewed signature was altered for a merely similar mechanic.

## Evidence and limits

The [Namco America original operator manual](https://manualzz.com/doc/994451/namco-time-crisis-arcade-game-operator%E2%80%99s-manual) directly documents the cabinet, Action Pedal, six-bullet refill, Story Game time and lives, operator options and special-enemy time rewards. [Donny Chan's contemporary arcade observations](https://gamefaqs.gamespot.com/arcade/583641-time-crisis/faqs/1081) independently document press/release and play pressure. [Mark Kim's arcade route](https://gamefaqs.gamespot.com/arcade/583641-time-crisis/faqs/1079) identifies the first three targets, optional right-first bonus and successor view. No original cabinet, ROM, screen capture or direct play was inspected; the precise sensor sampling and first-view bonus condition have not been experimentally verified.

## Decision

Accept four typed boundaries with reviewed Ukrainian and rule-valid original illustration after complete repository and browser gates. This unit authorises exactly one local commit, not push, public publication or deployment.
