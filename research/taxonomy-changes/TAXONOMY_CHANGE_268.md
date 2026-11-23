# Taxonomy Change 268 — Wii Sports Resort disc delivery and hole settlement

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-11-16.
- Trigger: [GAME-0521](../../knowledge/games/s-z/wii-sports-resort.md), original
  Wii release and solo manual Frisbee Golf, Classic A hole 1.

| Addition | Boundary | Counterexample |
|---|---|---|
| `ACT-716` | Select a reusable reach class for the current delivery. | `ACT-061` commits a finite movement card from a hand. |
| `ACT-717` | Change prethrow bearing while the lie remains fixed. | `ACT-498` grants separable stance relocation and aiming along a lane. |
| `ACT-718` | Release at the chosen motion sample to launch an orientable aerial disc. | `ACT-499` rolls on a lane. `ACT-615` points at a world target and samples a strength throw. |
| `SYS-1489` | Attitude changes flight and the landed disc can still skid or roll. | `SYS-146` tracks launched-body ballistic collision, while `SYS-100` resolves prescribed grid stages. |
| `SYS-1490` | Use the legal settled position as the next delivery origin. | Free repositioning or returning to the tee after every throw does not inherit the lie. |
| `SYS-1491` | Charge a penalty and select a legal lie from the hazard type. | `SYS-1153` adds time for a missed gate without moving the next delivery origin. |
| `SYS-1492` | Accept qualifying moving contact with a three-dimensional target volume. | `OBJ-014` designates the receiver without fixing an in-flight capture rule. |
| `CON-800` | End an unfinished hole at a counted-throw ceiling. | Par gives a benchmark, regardless of whether a maximum is enforced. |
| `INF-505` | Show current shot and wind cues and recommend a reselectable range. | `INF-373` shows a bowling frame and outstanding pinfall bonuses. |
| `OBJ-294` | Minimize counted deliveries with penalties against a fixed benchmark. | `OBJ-251` settles a penalty-adjusted clock instead of counted strokes. |

Three definitions transfer unchanged. Lower confidence remains on the exact
penalty-placement branch in the North American disc, the mechanics of the
unfinished-hole ceiling, and the quantitative flight and display details.
The cited Nintendo regional rulebook and community result differ on the
water-placement description. Neither a numerical cutoff nor that release's
water edge coordinates are assumed. Golf Peaks is the sole selected neighbour
among 520 earlier signatures. No verified combination is a proper subset.
