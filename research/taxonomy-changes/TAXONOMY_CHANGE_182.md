# Taxonomy Change 182: First-Mare flight collection and return

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-28
- Trigger: `GAME-0445` *NiGHTS into Dreams*, the first Spring Valley Mare of the original North American Sega Saturn game.
- Scope: admit `ACT-580`, `ACT-581`, `SYS-1166`–`SYS-1169`, `CON-720`, `INF-429` and `OBJ-254` as Active. No earlier signature or verified combination changes.

## Problem and accepted change

The original Saturn manual specifies a flight route with two ways to collect chips: direct contact and a closed Paraloop. Twenty Blue Chips must be delivered to an Ideya Capture, but this only releases the guarded Ideya; a separate return to the Palace starts the next Mare. A held Drill Attack spends a gauge restored by rings. A live timer, Minion penalties and post-expiry ground pursuit alter the route risk. Generic collectible and time-pressure labels would collapse these distinct input, threshold, response and terminal boundaries.

## Transfer and rejection tests

- Reuse `ACT-008` for direct movement, `SYS-037` for contact pickup, `SYS-045` for autonomously moving hostile actors, `SYS-1029` for the time-dependent Capture bonus, `OBJ-002` for optional score maximisation and `TIM-003` for live input under a continuing clock.
- `ACT-580` collects an enclosed set through path closure; it is not individual `SYS-037` contact or a permanent drawn fence. `ACT-581` consumes drill capacity; `SYS-1168` restores that capacity at a ring, distinct from ring score.
- `SYS-1166` handles the Capture's delivered-chip threshold and release. `CON-720` states the required order of capture and return, while `OBJ-254` names the bounded completed Mare. Twenty loose chips alone satisfy neither return nor progression.
- `SYS-1167` converts zero flight time into Claris' vulnerable ground control and Alarm Egg pursuit. The manual does not define immediate automatic failure on zero or a finite life-stock decrement.
- `SYS-1169` rewards connected pickups and ring passage with a Link count. It does not transfer `SYS-975`'s connected skateboard-trick scoring: items and rings, not grind/air-trick completions, are the scored units.
- `INF-429` is the live combined flight display, not a complete route forecast. Exact initial seconds, ring recharge amount, Link arithmetic and first-Mare chip geometry remain parameters requiring direct measurement.

## Evidence and limits

The [original Sega Saturn instruction manual](https://segaretro.org/images/e/e9/Nightsintodreams_sat_us_manual.pdf), printed pp. 3–4 and 19–23, documents the twenty-chip target, Paraloop, drill gauge, ring recharge, live HUD, Minion five-second loss, scoring Links, Capture release, Palace return and timer-expired ground pursuit. [SEGA's anniversary notice](https://social.sega.com/articles/rt-sega-nights-into-dreams-was-released-on-the-sega/) confirms original US Saturn identity. The [contemporary Saturn guide](https://gamefaqs.gamespot.com/saturn/198201-nights-into-dreams/faqs/5183) corroborates the course order. No original disc, console, executable or direct play was inspected.

## Decision

Accept nine distinct typed boundaries with reviewed Ukrainian text and a mechanically valid original illustration after repository and browser gates. This approval covers one local game-unit commit only, not push, public publication or deployment.
