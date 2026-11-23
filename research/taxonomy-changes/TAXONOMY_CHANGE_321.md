# Taxonomy Change 321 — Card commitments set the next turn’s delay

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-11-20.
- Trigger: [GAME-0575](../../knowledge/games/m-r/metal-gear-acid.md), the
  full first Outside Gate mission on North American PSP.

| Addition | Accepted boundary | Rejected substitution |
| --- | --- | --- |
| ACT-782 | Spend the same card on an eligible move or native command. | ACT-780 moves a fragment. Neon White's discard for movement and native fire have different expenditure and timing rules. |
| SYS-1686 | Effective costs of all paid commands add to the executor's next delay, with an order reduction for eligible subsequent cards. | TIM-026 schedules readiness in Final Fantasy VII without this accumulated command debt. |
| SYS-1687 | Refill toward the hand limit and charge the actor delay when the exhausted draw reserve is recycled. | SYS-588 routes resolving cards. It has no bounded per-turn refill or cost-clock charge for the recycle. |
| SYS-1688 | Progress from direct alarm through two intervening security states while out of sight as simulated delay elapses. | SYS-958 specifies two countdowns and one intervening phase. Outside Gate also has Caution and uses the shared discrete Cost clock. |
| SYS-1689 | Apply relative directional and elevation factors to eligible attacks. | SYS-625 matches attacker and blocker directions to resolve a defence. A target can face away and take a damage modifier without an entered block here. |
| SYS-1690 | On successful exit report effort, discoveries, eliminations and damage separately with points and rank. | OBJ-026 settles the spatial goal. The report has no authority to change that goal into a score threshold. |
| CON-838 | Renew an ordinary cap on interchangeable card commitments independent of their individual costs. | CON-095 reserves separate movement and action allowances. MOVE spends one of the same slots here. |
| INF-548 | Show a conditional joint view of card legality, slots and relative readiness. | A fixed future timeline or exact prediction of NPC decisions would remove the action-dependence of the observed queue. |
| TIM-038 | Advance common discrete delay at an activation boundary until a unit reaches zero. | TIM-026 fills local readiness under timed battle and pause rules. A larger cost here can defer the next multi-action turn. |

Reused the card-zone transition, stance change, surface lure, fixed-map
camera, directed occlusion, autonomous investigation, mission viability and
spatial objective. Ordinary range, hand size, reshuffle charge and slot count
are parameters. Keep card commitment, current slots, accumulated Cost and
the later common clock separate: changing one of the four need not change
the other three immediately. The shared countdown example leaves tie order
open. No earlier definition or signature changed.

Nine Ukrainian gene records and 17 bilingual player explanations were reviewed.
