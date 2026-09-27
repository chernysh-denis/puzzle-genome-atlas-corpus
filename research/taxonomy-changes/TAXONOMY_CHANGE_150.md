# Taxonomy Change 150: Reversible ink territory and paint-earned capability

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-26
- Trigger: `GAME-0412` *Splatoon 3*, one ordinary Nintendo Switch Turf War.
- Scope: admit `ACT-552`, `SYS-1096`–`SYS-1098`, `CON-698` and `OBJ-241` as Active. No earlier game signature or verified combination is changed.

## Problem and accepted change

Nintendo's Turf War packet links the same inked ground to team ownership, movement, ammunition recovery, special gain and final area comparison. Existing genes cover generic navigation, direct combat, temporary knockout, ability use, live team information and sustained surface application. They do not represent an opponent-reversible surface ledger or its colour-dependent access and timed area result. The six added genes isolate those independent decisions and system responses without making ink colour, stage or a particular weapon's numbers new IDs.

## Transfer and rejection tests

- `ACT-552` is a player-selected allied-map destination, not ordinary translation (`ACT-008`) or an automatic team-spawn return (`SYS-382`). Its destination remains ally-bound and the landing is risky.
- `SYS-1096` differs from `SYS-630` and `SYS-824`: those persist accepted treatment as task progress, whereas either Turf War team can repaint a formerly owned patch before the clock ends. Paint on a wall changes traversal but contributes no scored floor area.
- `SYS-1097` differs from finite reload (`ACT-183`) or stock pickup: a local tank is spent by fire and refilled by traversing own ink during the same contest.
- `SYS-1098` differs from `SYS-381`: Turf War special readiness is earned by eligible inking, not by dealing/receiving damage or healing; `SYS-380` still owns the particular special's effect.
- `CON-698` separates own-colour Swim Form access from the coating process itself. Its exclusion of rival ink is a legal movement/refill predicate, not a general claim that enemy colour is impassable.
- `OBJ-241` differs from `OBJ-079`, `OBJ-168` and `CON-516`: the result compares two currently owned ground areas at a fixed time, without ticket zeroing or a one-time treatment threshold. `CON-068` is rejected because expiry settles rather than fails the ordinary match.

## Evidence and limits

- [Nintendo's 2022 Splatoon 3 Direct summary](https://splatoon.nintendo.com/en/news/catch-up-on-all-the-latest-from-the-splatoon-3-direct/) establishes launch-era 4v4, three-minute territory and special gain through ink.
- [Nintendo's Turf War explanation](https://www.nintendo.com/jp/games/feature/splatoonqa/battle/nawabari/index.html) directly excludes walls from the scored area; [the official gameplay page](https://splatoon.nintendo.com/ca/gameplay/) describes own-colour swimming and ink refill.
- [Nintendo's online guide](https://splatoon.nintendo.com/en/news/beginner-basics-for-splatoon-3-the-ins-and-outs-of-playing-online/) describes opponent repaint and map-visible current coverage; [its Super Jump research report](https://splatoon.nintendo.com/en/news/squid-research-lab-dives-deep-into-the-splatlands/) describes frontline return and landing risk.
- Later teaching pages corroborate stable mechanics but do not establish every numerical rule of the launch `1.1.0` executable. No console build or online match was played, and no frame-specific balance or tie rule is inferred.

## Decision

Accept these six typed boundaries for `GAME-0412` only, retain the earlier genes unchanged and let deterministic signature and subset checks calculate any corpus relationships. This record is not an assertion that Splatoon 3 invented ink combat or that no earlier game used a related mechanic.
