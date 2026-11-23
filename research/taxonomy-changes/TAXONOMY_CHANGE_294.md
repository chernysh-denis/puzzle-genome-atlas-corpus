# Taxonomy Change 294 — Tracked putting and independent inspection

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-11-19.
- Trigger: [GAME-0547](../../knowledge/games/s-z/walkabout-mini-golf.md),
  full standalone Quest, Standard Tourist Trap Easy first hole, Stroke Limit
  off and Grip to Putt on, current documented rules rather than launch binary.

| Addition | Reviewed boundary | Counterexample |
| --- | --- | --- |
| `ACT-747` | A tracked club contacts the resting ball; face and motion choose the delivery. | `ACT-499` releases the held bowling body; `ACT-718` releases a disc. Neither models contact by a separate tool. |
| `ACT-748` | Relocate the embodied view to an addressed spot or the ball while retaining its lie and count. | `ACT-610` reframes a following camera around a separately steered actor. A portal moving the payload changes its lie. |
| `SYS-1586` | Contact creates free ball roll, bank response and cup approach under continuous surface physics. | `SYS-146` starts at launcher release; `SYS-995` includes bowling pin chains; `SYS-100` follows finite exact-distance card stages. |
| `SYS-1587` | An abandoned invalid ball returns to its previous position. Timing and additional count remain separately unmeasured. | `SYS-1490` carries a legal new lie; `SYS-1491` requires an extra penalty and hazard-class fallback. Practice undo refunds history and is excluded. |
| `CON-815` | The selected hold-to-enable setting permits contact only while the activating control is held. | A release launch or power meter has a different commitment event; changing a controller button is a parameter, not another gene. |
| `INF-528` | Inspect club, lie, banks and cup, with wrist/scorecard hole and stroke feedback. | `INF-505` includes wind and a recommended disc. An exact future path is not supplied here. |

Four unchanged definitions transfer: legal next lie `SYS-1490`, payload receiver
`OBJ-014`, par-relative minimisation `OBJ-294` and live input `TIM-003`.
The recovery claim explicitly retains Limited evidence and Medium confidence;
P6 documents a developer-described mechanism on another course, not a newly
measured Quest first-hole penalty. No existing definition or signature changes.
No new combination is asserted. A named GAME-0547 salience review partitions
all ten admitted genes without assigning weights.

The first exact Meta Quest analysis target adds one controlled registry
identity and its generated local mark. No earlier game's release coverage
or equivalence is inferred merely because another platform now exists.
