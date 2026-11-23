# Taxonomy Change 261: first Mewgenics tutorial battle

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-11-15.
- Trigger: `GAME-0514`, Windows Steam release-day first battle of The Path.

The [bounded game record](../../knowledge/games/m-r/mewgenics.md) names the
two supplied cats, two required enemies and battle exit before level-up.
The launch-day transcript records a successful path. Documented tutorial
exceptions are classified separately from that observed path. The exact
installed build and adverse branches were not reproduced by the Atlas.

| Addition | Boundary | Counterexample |
|---|---|---|
| `CON-795` | One ordinary move and one basic attack in either order, with separately paid abilities. | `CON-752` limits the ordinary turn to one Move and one Act. A single AP budget would allow casting to replace an ordinary use. |
| `SYS-1453` | The active actor's turn end credits personal casting mana. | A new allowance, start-of-party-turn refill or real-time recharge. |
| `SYS-1454` | The downing event triggers an attacker-local random stat increase when its passive permits it. | Random selection alone (`SYS-004`), a chosen spend or an award on every hit. |
| `SYS-1455` | An early learning step restores a narrowly specified retry after an error. | Broad branchable rewind (`TIM-007`) or a new attempt after losing an encounter. |
| `SYS-1456` | Incapacitation ends actor turns while a body can still receive a later shot. | Immediately removing an enemy entirely or requiring a second hit for the first defeat to count. |
| `INF-499` | Movement selection separately displays basic attack reach. | `INF-043` marks only movement destinations. A footprint does not reveal an enemy's committed action or a guaranteed hit. |

Transfers without definition changes: `ACT-014`, `ACT-019`, `ACT-652`,
`SYS-004`, `SYS-1289`, `CON-001`, `CON-269`, `INF-002`, `INF-043`, `INF-119`,
`OBJ-029` and `TIM-001`. Final Fantasy Tactics shares ten IDs, but its
speed-fed and use-dependent readiness does not represent this resource system.
All 513 earlier signatures and 274 verified combinations were considered.
No existing signature or verified combination changes.
