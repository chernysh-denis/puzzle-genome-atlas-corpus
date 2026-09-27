# Taxonomy Change 153: Crazy Taxi open score-fare loop

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-26
- Trigger: `GAME-0415` *Crazy Taxi*, original Dreamcast Arcade course under `PLAY BY ARCADE RULES`.
- Scope: admit `SYS-1102`–`SYS-1104`, `CON-700`–`CON-701` and `INF-408` as Active. No earlier game signature or verified combination changes.

## Problem and accepted change

The original Sega Dreamcast manual describes a freely chosen sequence of customers, each boarded after a full stop, transported against a private deadline and either paid at a second full stop or abandoned unpaid. Timely payment adds money, trick tips can accumulate in a breakable combo and the Arcade-rule variant can extend the overall game clock. Those coupled transitions are not Mafia's fixed five-fare mission chain, a cargo delivery or a race finish. We isolate the fare settlement, tip combo, global-time award, stop eligibility, dual deadlines and information surface without creating a separate gene for every customer or taxi manoeuvre.

## Transfer and rejection tests

- `SYS-1102` applies when a player-chosen passenger receives a destination and personal deadline and the taxi service settles or forfeits that fare; a fixed authored order remains `SYS-708`.
- `SYS-1103` requires tip accrual from driving manoeuvres with a collision-breakable consecutive combo. The exact manoeuvre and multiplier are parameters, not new genes.
- `SYS-1104` requires successful service to award additional overall run time. Remaining personal time also contributes to money, but that separate bonus fare is part of `SYS-1102` and must not be confused with the clock award.
- `CON-700` is the full-stop-in-service-zone predicate for both boarding and paid drop-off. It is not generic race-end parking.
- `CON-701` retains two different expiry effects: one lost passenger fare versus the end of the whole score run. `CON-068` would wrongly imply that the whole attempt simply fails when time runs out.
- `INF-408` makes customer choice and active navigation legible but does not promise a fastest-road route; the arrow is general direction only.
- Reuse `ACT-290`, `SYS-320`, `SYS-365`, `OBJ-002` and `TIM-003` for dedicated driving, physical road/traffic motion, score objective and real-time operation. Reject `ACT-201`, `ACT-309`, `SYS-708`, `CON-557` and `OBJ-132` on their explicit boundaries.

## Evidence and limits

- [Sega's original Dreamcast instruction manual](https://www.digitpress.com/library/manuals/dreamcast/crazy_taxi.pdf), printed pp. 2–11, supplies the mode distinction, controls, pickup/drop-off rules, fare categories, customer and global clocks, tricks, combo and time award. The inspected PDF's SHA-256 is recorded in the [game analysis](../../knowledge/games/a-f/crazy-taxi.md).
- [GameSpot's contemporary Dreamcast review](https://www.gamespot.com/reviews/crazy-taxi-review/1900-2540233/) corroborates the prompt-delivery time award. The publisher manual, not the review, owns exact mode and fare rules.
- No original Dreamcast executable, console session, input trace, video or audio was inspected. Disc revision, starting option values, frame priority and numerical tip conversion remain unverified.

## Decision

Accept six new typed boundaries for `GAME-0415` only. Leave earlier signatures unchanged. Recompute every lower-ID comparison and verified-combination subset, review all bilingual definitions, and reject artwork that depicts an impossible passenger/stop-zone or vehicle state before the local commit.
