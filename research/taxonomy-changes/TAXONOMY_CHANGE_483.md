# Taxonomy Change 483 — Bounded depth edits and exposed slab treads

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-11-25
- Scope: [GAME-0737](../../knowledge/games/m-r/pullblox.md),
  the original Nintendo 3DS Basic Lessons, Lesson 3.
- Decision: admit ACT-950, CON-906, INF-665 and SYS-2048.
  The corpus contains 4,987 definitions, including 4,929 Active genes.

| Gene | Accepted boundary | Nearest reuse considered |
| --- | --- | --- |
| ACT-950 | Grip one reachable slab and move it in or out along its fixed depth axis. | ACT-009 pushes an adjacent movable object. This action includes a distinct grip and inward or outward depth changes for the same height-fixed slab. |
| CON-906 | Apply the fixed absolute extension limit to each slab independently. | CON-020 spends a finite attempt action budget. This constraint caps individual positions, while the player can keep editing and moving. |
| INF-665 | Combine current 3D tread visibility with a separate face map containing the goal and player position. | INF-179 covers visible world geometry. The separate face map intentionally omits the depth change needed to infer support. |
| SYS-2048 | Expose a tread where a lower movable slab currently projects beyond a higher slab. | SYS-2046 creates a new bridge, and SYS-2042 toggles a cell to solid. These surfaces belong to persistent wall slabs with independently edited positions. |

Reuse ACT-008, INF-179, OBJ-026, SYS-036 and TIM-002.
The original signatures, definitions and combination memberships
remain as recorded.
