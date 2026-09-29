# Taxonomy Change 187: Landed snowboard tricks fund race boost

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-09-28
- Trigger: `GAME-0450` *SSX Tricky*, original-PS2 Garibaldi Single Event Race.
- Scope: admit `ACT-593`–`ACT-594`, `SYS-1181`–`SYS-1184`, `CON-726`, `INF-435` and `OBJ-257` as Active. No earlier signature or verified combination changes.

## Problem and accepted change

The original EA-authored *SSX Tricky* booklet and a firsthand PS2 Garibaldi account establish a downhill contest in which route choice supplies air, a completed landing awards both points and adrenaline, and adrenaline powers speed. A full meter opens Uber manoeuvres; repeated successful Uber landings can complete TRICKY and make the speed reserve unlimited for the rest of that descent. This is neither a separate Showoff score mode nor a generic motor-racing fuel bar.

## Transfer and rejection tests

- Reuse `ACT-008` for direct rider motion and `TIM-003` for live time; course, rider, board, Amateur difficulty and numerical meter values remain parameters.
- `ACT-593` isolates the airborne grab/rotation and release; `ACT-594` isolates intentional spending. `SYS-1181` handles snow contact and air, `SYS-1182` handles autonomous rivals and ranked finish, `SYS-1183` handles landed trick points and finite adrenaline, and `SYS-1184` handles the Uber window and within-run TRICKY threshold.
- `CON-726` prevents awarding a failed airborne attempt, `INF-435` shows race/boost state, and `OBJ-257` limits success to first place in one Single Event Race. The connected skateboard combo (`SYS-975`), damage-paid vehicle boost (`SYS-1040`) and World Circuit medals do not fit this packet.
- EA's accessible original booklet is for the GameCube edition of the same game. The PS2 guide corroborates shared race behaviour; neither source proves an exact PS2 button mapping, numeric physics or a guaranteed winning trajectory. Mislabelled first-SSX and 2012-SSX manuals were rejected.

## Decision

Admit nine reviewed, bilingual mechanical boundaries and original mechanics-first art for this source-only PS2-targeted packet. One local game-unit commit is authorised by the user; no push, public corpus publication or deployment.
