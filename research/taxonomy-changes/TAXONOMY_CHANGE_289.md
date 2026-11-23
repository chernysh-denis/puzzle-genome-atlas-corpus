# Taxonomy Change 289 — Excite Truck thermal driving and stunt settlement

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-11-18.
- Trigger: [GAME-0542](../../knowledge/games/a-f/excite-truck.md),
  the original Wii Greenhorn Gulch race.

| Addition | Reviewed boundary | Counterexample |
| --- | --- | --- |
| `ACT-739`, `SYS-1564` | Hold boost, accumulate heat and enter a temporary non-destructive lockout. | `ACT-695` and `SYS-1421` include destructive overheat in MotorStorm. |
| `ACT-740`, `SYS-1569` | Repeated crash input restores the local racer with boost. | `ACT-605` applies to a downed fighter. A whole-race retry resets a different state. |
| `SYS-1565` | Course contact triggers an authored terrain or fixture change that may affect a rival. | Tyre rut persistence and pre-race track editing have different triggers. |
| `SYS-1566` | Live driving feats add stars, including the documented crash credit. | `SYS-1183` requires cleanly landed snowboard tricks and feeds adrenaline. |
| `SYS-1567` | A contact pickup immediately changes speed and permits obstacle destruction for a bounded interval. | A stored kart item waits for a separate use command. |
| `SYS-1568` | Takeoff timing and four-wheel landing give movement assistance without direct stars. | `ACT-308` describes the player's orientation command without this automatic burst. |
| `SYS-1570`, `OBJ-300` | Finish position adds a bonus, then the complete star total determines passing. | A first-place-only race, an elapsed-time medal and cumulative cup standings have different terminal predicates. |
| `INF-524` | Read live feat credit, earned and required stars, and current heat. | `INF-491` includes an initial charging state and destructive-heat warnings. |

Eleven existing genes transfer without a definition rewrite. The first
Mexico event supplies one bounded unit. Additional vehicles, whole-cup
awards and water cooling remain outside it. No combination is proposed.
