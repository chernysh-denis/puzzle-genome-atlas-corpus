# Taxonomy Change 284 — Kirby Tilt 'n' Tumble controls and course settlement

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-11-17.
- Trigger: [GAME-0537](../../knowledge/games/g-l/kirby-tilt-n-tumble.md),
  normal first course on the original North American Game Boy Color cartridge.

| Addition | Reviewed boundary | Counterexample |
| --- | --- | --- |
| `ACT-734` | A brief physical upward gesture launches the avatar. | `ACT-519` continuously steers; `ACT-637` directly launches supported inhabitants globally. |
| `ACT-735` | Set the physical neutral reference used to interpret future tilt. | Changing the current inclination or choosing a camera direction leaves sensor calibration alone. |
| `SYS-1554` | Roll into a round holder, then release from it along a cue. | `ACT-668` is the decision to release an already occupied launcher. |
| `SYS-1555` | Nearby uncollected item types change on a flick. | `SYS-037` credits a pickup on later contact. |
| `SYS-1556` | A typed pickup adds time to the current countdown. | `SYS-1204` requires a reached route checkpoint, and ordinary star-piece score adds no time. |
| `SYS-1557` | Bumper type decides whether a contact rebounds or lifts the ball. | The free jump or a round hole launch needs its separate input. |
| `SYS-1558` | Pad contact clears while spatial position separately grades reward. | `SYS-1029` grades remaining time, and `OBJ-220` does not require a reward grade. |
| `INF-521` | Panning discloses course geometry independently of tilt, beside live resources. | `INF-385` describes a different view with a speed indication. |

Fifteen definitions transfer, including tilt, ongoing rolling movement,
a moving carrier and the finite-life return. The sensor chip model,
amount of clock credit, exact timing, board geometry and bonus points
are parameters. No verified combination is a proper subset. The exact
remaining-time behaviour when crossing or returning to the gate is a
separate unresolved question.
