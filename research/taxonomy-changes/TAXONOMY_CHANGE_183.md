# Taxonomy Change 183: Paid railway service and separate equity

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-28
- Trigger: `GAME-0446` *Railroad Tycoon II*, original 1998 PC Tutorial's first paid service.
- Scope: admit `ACT-582`–`ACT-585`, `SYS-1170`–`SYS-1171`, `CON-721`, `INF-430`–`INF-431` and `OBJ-255` as Active. Earlier game signatures and verified combinations stay unchanged.

## Problem and accepted change

The original manual separates founding capital and ownership, physically laying priced rail with grades, placing stations with industrial catchment, programming a train's ordered stops/consist/wait rule, and receiving company revenue for transported—not owned—cargo. It also separates the corporate ledger from the founder's personal portfolio. A generic network or trade label would erase the eligibility and account boundaries.

## Transfer and rejection tests

- Reuse `ACT-130` for locomotive acquisition, `ACT-006` for speed control, `SYS-266` for autonomous scheduled train service, `CON-171` for managed solvency, `CON-237` for compatible connected service, `INF-058` for corporate accounts and `TIM-003` for editable live simulation.
- `ACT-582` commits rail geometry and grade; `ACT-583` places track-aligned stations; `ACT-584` authors the train's itinerary and per-stop load/wait instructions. These cannot collapse into Mini Metro's abstract line editing or RollerCoaster Tycoon's attraction-track construction.
- `ACT-585` produces both a company budget and an equity split. `INF-431` reports the resulting personal holdings, while `INF-058` remains corporate. One paid freight trip does not automatically satisfy the $10 million personal scenario objective.
- `CON-721` gates local cargo by station radius independently of `CON-237`'s rail reachability. `SYS-1170` makes industry output available later; the manual explicitly warns against assuming a first-return goods load. `SYS-1171` is transport payment, not a commodity sale. `OBJ-255` is the bounded first-paid-service checkpoint, not the full 1900 scenario.

## Evidence and limits

The [original publisher/developer manual](https://manualzilla.com/doc/5757182/railroad-tycoon-ii%C2%A9), especially Tutorial, Railroading, Running Trains and Finances, establishes the funding, route, station, scheduling, cargo, transport-payment and dual-finance rules. No original CD-ROM, save, input trace or measured values were inspected. Resource placements, first-trip loads, cost and payment arithmetic remain unmeasured.

## Decision

Admit ten typed boundaries with reviewed Ukrainian wording and an original, mechanically plausible route illustration after all local repository and browser gates. The decision authorises only this requested local game-unit commit; no push, corpus publication or deployment.
