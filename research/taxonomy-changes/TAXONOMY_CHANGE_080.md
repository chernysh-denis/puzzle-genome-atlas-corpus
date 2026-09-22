# Taxonomy Change 080: Generalise compact body and timed-bomb boundaries

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-21
- Trigger: `GAME-0337` Super Metroid lower-ID scan.
- Scope: wording and support for `ACT-202`, `ACT-270` and `SYS-470`;
  supporting-carrier evidence for `ACT-008`, `ACT-161`, `ACT-164`, `SYS-215`,
  `SYS-222`, `SYS-398`, `SYS-417`, `SYS-578`, `CON-068`, `CON-282`, `CON-349`,
  `CON-402`, `CON-578`, `INF-073`, `INF-119`, `INF-125` and `TIM-003`; no
  earlier game signature, combination, family or lifecycle change.

## Problem

Three portable boundaries named their first carriers too narrowly. `ACT-202`
listed ordinary standing/crouched/prone/lean states but not a retained compact
body configuration that changes collision clearance. `ACT-270` required
spending a finite carried bomb even though placement and fuse timing are the
same player operation when access is reusable. `SYS-470` named Isaac rocks and
secret-room walls instead of the compatible room geometry affected by a placed
timed blast.

## Accepted change

- `ACT-202` admits a retained compact body configuration when the player
  directly enters/leaves it and it changes clearance or another local
  affordance.
- `ACT-270` admits either finite stock or a retained reusable bomb capability;
  supply model and compatible placement state are parameters.
- `SYS-470` resolves the placed bomb against overlapping actors and compatible
  destructible room geometry; rock, wall and bomb-block classes are parameters.

## Complete lower-ID transfer test

- PUBG: BATTLEGROUNDS, Cyberpunk 2077, PowerWash Simulator and TEKKEN 8 retain
  their standing, crouched, prone, lean or recovery configurations under
  `ACT-202`; none gains a compact rolling state or changes signature.
- The Binding of Isaac: Rebirth retains `ACT-270` and `SYS-470`: it still
  spends one carried bomb, places it locally, waits for the fuse and applies
  the bounded blast to actors, rocks and eligible secret-room walls.
- No lower-ID game gains either bomb boundary merely because it contains a
  grenade, projectile, automatic explosion or reusable terrain tool.
- Super Metroid adds only the independent retained-capability carriers and no
  retroactive gene membership for an earlier game.

## Migration and compatibility

Stable IDs are retained. English and Ukrainian labels, definitions, parameters
and carrier support change for the three generalised boundaries. `GAME-0337`
reuses them. Every earlier signature and comparison remains unchanged.

## Validation expectation

Repository validation must report no duplicate Active definition. The complete
lower-ID scan and Ukrainian review must preserve the direct body-configuration,
placed-fuse and bounded room-blast tests while admitting Super Metroid without
inventing finite Bomb stock.
