# Taxonomy Change 186: Paired partner actions and timed turn defence

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-09-28
- Trigger: `GAME-0449` *Paper Mario*, the original N64 four-Fuzzy battle after Kooper joins.
- Scope: admit `ACT-590`–`ACT-592`, `SYS-1178`–`SYS-1180`, `CON-724`–`CON-725` and `INF-434` as Active. Earlier signatures and verified combinations remain unchanged.

## Problem and accepted change

Nintendo's original manual specifies Mario plus one active helper, an optional Z-order exchange before either acts, position-limited commands, FP-gated special attacks and damage-reducing A timing during hostile turns. Two original-N64 routes place those rules in a finite four-Fuzzy fight immediately after Kooper joins and describe the enemy's life drain. Treating this as a lone-monster replacement, stat-sorted AP queue or live parry battle would erase observable decision boundaries.

## Transfer and rejection tests

- Reuse `ACT-019` for command and target choice, `ACT-222` and `SYS-358` for offensive Action Commands, `INF-142` for timing cues, `OBJ-029` for finite enemy clearance and `TIM-001` for discrete turns.
- `ACT-590` changes only the helper beside Mario; unlike `ACT-258`, it does not replace the sole acting Pokémon. `ACT-591` exchanges the two unspent allied actions without minting a third action. `SYS-1178` owns the resulting paired side phase rather than claiming `SYS-356`'s stat-ordered queue.
- `ACT-592` and `SYS-1180` isolate a simple near-contact input and reduced damage, not `ACT-223`/`SYS-359`'s dodge/parry/counter. `SYS-1179` ties Fuzzy healing to a successful draining attack. `CON-724` and `CON-725` separate legal target geometry from available FP. `INF-434` exposes battle resources and feedback without future AI information.
- Four Fuzzies, Kooper, Goombario, button letters and any FP costs remain packet parameters. No exact opening resources, timed input frames, enemy policy or optimal route are asserted.

## Decision

Admit nine reviewed boundaries, bilingual records and an original mechanics-first paper-theatre illustration for this source-only original-N64 packet. No direct play was inspected. This authorises one local game-unit commit only; no push, public corpus publication or deployment.
