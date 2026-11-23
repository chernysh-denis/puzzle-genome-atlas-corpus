# Taxonomy Change 269 — Returnal firing states and cross-cycle unlock

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-11-17.
- Trigger: [GAME-0522](../../knowledge/games/m-r/returnal.md), original PS5
  launch-era campaign through the first controllable return after the Charger.

| Addition | Boundary | Counterexample |
|---|---|---|
| `ACT-719` | Trigger depth selects two firing preparations. A separate input fires. | `ACT-403` swaps an equipped attachment. A digital secondary key does not sample trigger depth. |
| `SYS-1493` | Automatic primary recharge can complete early after a correctly timed press, without an ammo reserve. | `ACT-478` requires a second manual reload input. `SYS-924` defines additional graded timing outcomes. |
| `SYS-1494` | Alternate ability recharge is separate from primary readiness on the same weapon. | `SYS-864` owns reusable ability units, not two distinct channels on one selected gun. |
| `SYS-1495` | Thresholds of kills without damage add temporary tiers that an unprotected damaging hit clears. | `ACT-594` spends a pre-existing adrenaline resource. It does not resolve undamaged kill groups. |
| `SYS-1496` | Run proficiency changes potential finds. Earned traits remain unlocked for eligible later finds after proficiency resets. | `SYS-422` advances a locked hop-up for the current weapon object. |
| `SYS-1497` | Eligible pickups heal when injured and advance a temporary maximum-health threshold at full health. | `SYS-1417` banks restoration to fill missing health later. It does not raise the maximum. |
| `SYS-1498` | Permanent equipment unlocks a function on eligible guns without preserving the temporary instance. | `SYS-469` covers the whole reset boundary but does not specify a weapon-function unlock. |
| `CON-801` | Retain one replaceable gun with no second carried firearm. | `CON-353` explicitly permits an additional mount-carried gun. |

Fifteen existing definitions transfer unchanged. These eight additions
separate input thresholds, two readiness states, a damage-sensitive streak,
conditional recovery, eligibility of future finds and lasting use authority.
Ori and the Blind Forest is the sole selected neighbour among 521 earlier
signatures. None of 274 verified combinations is a proper subset.
