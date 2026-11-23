# Taxonomy Change 272 — Anno 117 category and road supply

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-11-17.
- Trigger: [GAME-0525](../../knowledge/games/a-f/anno-117-pax-romana.md),
  Windows launch patch 1.2, one Latium starter settlement.

| Addition | Reviewed boundary | Counterexample |
| --- | --- | --- |
| `SYS-1505` | Individual needs produce independent attribute returns. Consumption coverage can scale the return before the upgrade gate. | `SYS-244` broadly updates occupancy, income and happiness from basic and luxury supplies; it does not isolate optional per-need effects and fractional returns. |
| `SYS-1506` | A production building's local attribute effect has its own coverage, separate from where its output can be consumed. | `SYS-153` propagates a civic service that can satisfy a need. |
| `CON-805` | Independently meet the supply minimum in each category. Alternatives can substitute within a category. | `CON-224` captures Anno 1800's required basic needs and occupancy. |
| `CON-806` | Eligible directional corner frontage can create a road link. The orientation condition prevents arbitrary corner connectivity. | `CON-099` conditions road-crossing continuity on elevation. |
| `CON-807` | Production requires both continuity to the founded road network and a depot within working road reach. | `CON-172` requires recipe-compatible flow and does not determine the reachable transport graph. |
| `INF-509` | The residence panel exposes separate category minima, fulfilment and individual optional returns. | `INF-086` exposes the general residence and workforce state. |
| `OBJ-296` | Pay to convert the first eligible home while retaining the original staffed local supply loop. | `OBJ-067` describes the much later World’s Fair and exhibition. |

Sixteen existing definitions transfer unchanged. No complete verified
combination matched as a proper subset. Earlier signatures are preserved.
