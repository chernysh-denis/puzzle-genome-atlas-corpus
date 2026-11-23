# Taxonomy Change 266 — Power Stone shared stones and temporary combat form

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-11-16.
- Trigger: [GAME-0519](../../knowledge/games/m-r/power-stone.md), original
  North American Dreamcast local Versus, Falcon and Gunrock on Londo.

| Addition | Boundary | Counterexample |
|---|---|---|
| `ACT-714` | Timed grab can make a thrown eligible prop held. | `ACT-048` picks up a reachable free prop without the approaching interception predicate. |
| `SYS-1477` | Resolve a fixed feature's contextual movement attack. | `ACT-048` handles portable rigid objects. A wall can also simply block displacement. |
| `SYS-1478` | Remove a token from the struck holder and make it contestable. | `SYS-1465` generates reserve pickups from hits without a prior holder. |
| `SYS-1479` | Completing the contested set automatically activates the powered combat form. | `SYS-608` transfers control to an acquired form with its own health and readiness. |
| `SYS-1480` | A diminishing shared meter admits partial-cost attacks or a finisher that spends its entire positive remainder. | `SYS-837` provides a once-per-round activation boundary. This gene covers the meter once the form is underway. |
| `SYS-1481` | Form depletion restores base control and returns the set to the arena during the round. | `SYS-522` resets states at a settled round boundary. |
| `SYS-1482` | A recoverable portion restores after a damage-free interval inside the current surviving segment. | `SYS-832` specifies hitting an opponent for recovery. Losing the current segment removes the Power Stone portion. |
| `SYS-1483` | A picked-up weapon runs out through its performed uses or is forcibly lost on impact. | `ACT-355` equips or abandons the neutral weapon. It does not consume or remove its capacity. |
| `CON-798` | The fixture, reach and current fighter determine the allowed scenery interaction. | `CON-147` depends on relative geometric size rather than fighter-specific handling rules. |
| `INF-504` | A small locator shows rough regions of loose contested tokens. | `INF-210` shows combat resources and results, including current stone possession. |

Fourteen existing definitions transfer without revision. The resource and
scenery claims have high confidence. The segment recovery claim has medium
confidence. The default
three-stone loop recurs within a round. Prop handling, outward token release,
ordinary contact collection, form entry and form depletion retain separate
causes. Street Fighter II: The World Warrior was selected across all 518
prior game signatures. None of the 274 combinations was a proper subset.
