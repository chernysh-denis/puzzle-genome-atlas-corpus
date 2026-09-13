# Taxonomy Change 037: Generalise sealed phases and evaluated result reports

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-08
- Trigger: independent closure review of `GAME-0277` Cuphead.

## Current classification

- `SYS-799` required one guardian body and accumulated damage to continue into
  its next health-gated attack phase.
- `INF-299` required a mission report whose categories described conduct and
  whose aggregate state classified that conduct.

## Detected problem

- Cuphead's fixed `Botanic Panic!` Regular encounter advances through three
  required Root Pack members. Depleting one member hands the same sealed level
  attempt, arena and retained phase progress to the next member and attack set;
  no intermediate level settlement occurs.
- Its successful results card reports performance categories — time, remaining
  HP, parries, Super Meter use and skill level — and their aggregate grade.
- Creating a Root-Pack relay gene or a grade-card-only Information gene would
  duplicate the same transition and disclosure functions because the changing
  occupant and category vocabulary are carrier parameters.

## Evidence

- Studio MDHR's official patch announcements directly refer to boss phase
  progression, result-screen HP scoring, Parry scoring and the post-death
  results/equipment surface:
  <https://steamcommunity.com/app/268910/announcements/>.
- Xbox Wire's official mechanical description establishes the stable timed
  pink-projectile parry-to-meter loop:
  <https://news.xbox.com/en-us/2015/06/18/xbox-cuphead-will-kill-you-with-cuteness/>.
- Complete written guide evidence identifies the three-member Root Pack order,
  changing attacks and the results/Equip Card fields:
  <https://steamcommunity.com/sharedfiles/filedetails/?id=1310872602> and
  <https://gameranx.com/features/id/122376/article/cuphead-how-to-defeat-root-pack-boss-guide/>.
- Carrier evidence: [`GAME-0262`](../../knowledge/games/a-f/dark-souls-iii.md),
  [`GAME-0274`](../../knowledge/games/g-l/hollow-knight.md),
  [`GAME-0247`](../../knowledge/games/a-f/dishonored-2012.md),
  [`GAME-0248`](../../knowledge/games/g-l/hitman-world-of-assassination.md) and
  [`GAME-0277`](../../knowledge/games/a-f/cuphead.md).

## Proposed change

- Rename `SYS-799` to `Advance a sealed encounter into a health-gated attack
  phase` and admit either transformation of the same body or replacement by the
  next required member of a declared sequential guardian set.
- Preserve the boundary that the same sealed encounter, arena and prior phase
  completion continue; a separately settled encounter or time-driven wave
  remains excluded.
- Rename `INF-299` to `Results report exposes categories and aggregate
  evaluation` and admit performance categories for bounded levels or encounters
  alongside conduct categories for missions.
- Preserve the boundary that the same terminal report exposes both category
  values and their aggregate evaluation. A result with only one total or only a
  completion flag remains excluded.

## Genome and combination impact

- `GAME-0277` reuses both generalised IDs.
- No earlier reviewed signature, combination set, lifecycle or ID changes.
- `SYS-822` remains distinct: it is the transition that computes and records a
  graded win; `INF-299` is the surface that makes its categories and aggregate
  readable.
- `SYS-623` and `INF-247` remain distinct reviewed compound records because
  they additionally map activity score to reward tier and chest admission.

## Decision

- Decision: `Accepted`.
- Decided by: full lower-ID scan, two-way transfer test and explicit comparison
  of state transition and information disclosure.
- Rationale: occupant identity does not change the phase-transition function,
  and category vocabulary does not change the result-report disclosure. Both
  generalisations remove product-shaped boundaries without erasing a decision-
  relevant distinction.
- Implementation links: `SYS-799`, `INF-299`, `GAME-0277`.

## Ukrainian review

- `SYS-799` and `INF-299` receive complete Ukrainian label, definition,
  inclusion and exclusion parity for their widened boundaries.
- Named encounter, phase members, colour, result fields and exact counts stay
  in game-scoped explanation as parameters.

## Change history

- 2026-09-08 — created and accepted during the independent `GAME-0277`
  closure unit.
