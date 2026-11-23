# Taxonomy Change 355 — Navigate with an independently turning span

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-11-21.
- Scope: [GAME-0609](../../knowledge/games/g-l/kuru-kuru-kururin.md),
  original European Normal Adventure Grasslands 3.

ACT-809 separates held translation speeds from steering. Reuse ACT-008
for choosing the centre path. SYS-1788 advances the collision-bearing rotor
while the player can wait or move. This differs from the commanded rotation
under ACT-058. CON-852 checks clearance of the whole current span over time,
outside CON-090's discrete grid sweep with a coupled carried object.
Reuse TIM-003 for live input and OBJ-026 for reaching the spatial goal.

SYS-1789 couples damage, time and a counted miss at the event boundary.
Reuse CON-773 for the zero-heart termination. SYS-1790 replenishes
health in a protected place during the same attempt, so it does not
fit SYS-1750's spatial return. The recorded penalty and miss stay in
effect. SYS-1791 records the distinct error-free and standard-span
conditions for a star, while INF-251 describes the exposed time and
local placement. Reuse SYS-037 for the sibling contact branch.
No earlier gene definition, game signature or combination changes.
