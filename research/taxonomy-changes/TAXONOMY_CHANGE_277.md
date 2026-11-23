# Taxonomy Change 277 — Lost Odyssey round execution and formation

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-11-17.
- Trigger: [GAME-0530](../../knowledge/games/g-l/lost-odyssey.md), original
  Xbox 360 retail rules, Grilgan at the Ipsilon Mountains peak.

| Addition | Reviewed boundary | Counterexample |
| --- | --- | --- |
| `ACT-725` | Change an actor's defensive formation row in place of that actor's combat command. | `ACT-199` changes a compatible equipment slot while preserving the command. |
| `SYS-1523` | Resolve a committed party batch against hostile actions by actor speed and command timing. | `SYS-1305` includes the obsolete-attack fallback specific to the scoped Golden Sun battle. |
| `SYS-1524` | Front-line damage wears down a separate reserve protecting the rear. Ordinary HP recovery does not restore it. | `SYS-1307` pays one command for its actor's direct defensive state. |
| `SYS-1525` | A hit on a casting member can defer the pending spell by a round, with formation guard affecting that outcome. | `SYS-1523` schedules the initial cast without claiming that execution cannot be postponed. |
| `SYS-1526` | Downed eligible actors may rise after a turn-count wait within a surviving group. | `SYS-1419` grants a ready personal revival and then puts its permission on cooldown. |
| `SYS-1527` | A persistent poison condition adds round-boundary damage and can be removed independently of HP recovery. | `SYS-825` models the coupled hit and status rolls and different damage timing of Darkest Dungeon. |
| `INF-515` | Show a separate guard reserve and disclose the queued execution sequence once the commands are committed. | `INF-141` exposes a turn order and AP before actor command choice. |

Fifteen definitions transfer. The same prompted attack effect boundaries
cover the Aim Ring input. The exact release window, spell coefficients,
actor order score, item stock and boss HP remain parameters. Casting-delay
behaviour is rated Medium, as no native encounter trace was captured.
No verified combination is a proper subset.
