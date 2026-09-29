# Taxonomy Change 184: Boxing hearts, stars and bout settlement

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-28
- Trigger: `GAME-0447` *Punch-Out!!*, the first Glass Joe bout in the 1990 NES Mr. Dream edition.
- Scope: admit `ACT-586`–`ACT-587`, `SYS-1172`–`SYS-1174`, `CON-722`, `INF-432` and `OBJ-256` as Active. Earlier game signatures and verified combinations remain unchanged.

## Problem and accepted change

The [official Nintendo manual](https://www.nintendo.co.jp/clv/manuals/en/pdf/CLV-P-NAATE_en.pdf) distinguishes Mac's hearts from stamina, earned stars from both, a button-driven rise before the referee's ten-count, a once-per-bout SELECT recovery between rounds, and a whole-bout result reached by KO, three falls within one round or final points. Generic one-pool health or first-to-N independent fighting rounds would lose these causal boundaries.

## Transfer and rejection tests

- Reuse `ACT-295` for directly controlled punches, `ACT-296` for held block, `ACT-356` for timed weave/duck, `SYS-215` for live hostile combat, `CON-442` for actionable fighter state, `INF-142` for visible attack motion and `TIM-003` for continuing bout time.
- `SYS-1172` models hearts' temporary offence lock, not stamina knockdown. `SYS-1173` owns earned/forfeited stars, whereas `CON-722` gates a particular START uppercut on that stock. `ACT-586` requests recovery while fallen; `ACT-587` requests the separate one-use between-round stamina recovery. `SYS-1174` adjudicates the count, TKO and decision.
- `INF-432` reports three distinct stocks with the boxing clock and points. `OBJ-256` is victory in one fixed bout, not `OBJ-099`'s required count of independently won versus rounds. *Street Fighter II* is the nearest prior signature but does not establish these boxing-specific states.
- Glass Joe's exact attack timing, star-award triggers and a guaranteed route are excluded; the manual and official title description do not supply a measured first-bout trace.

## Decision

Admit eight reviewed boundaries with corresponding Ukrainian copy and one original, rule-plausible ring illustration. The decision authorises only the requested local unit commit; no push, public corpus publication or deployment.
