# Taxonomy Change 254 Elden Ring personal beacon assignment

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-10-14
- Scope: replace one supporting `ACT-227` assignment in `GAME-0152` with
  the already Active `ACT-676`; no new ID or changed operational definition.

## Decision

Elden Ring's scoped personal map marker/beacon is `ACT-676`, not `ACT-227`.
The player chooses a reference point and uses its map, compass or world
projection for manual navigation. This request does not establish a
calculated GPS road route. Both existing English boundaries are preserved:
`ACT-227` remains a road-route waypoint, and `ACT-676` remains a free
navigation pin without a calculated path.

The Ukrainian `ACT-227` definition regains the complete road-route predicate;
its Includes no longer assigns Elden Ring's free beacon to that class. The
game's English explanation stops promising road calculation, while its
Ukrainian explanation explicitly distinguishes manual guidance from it.
The marker's supporting role and existing Stormveil examples remain.

## Evidence and transfer

[The frozen Elden Ring packet](../../knowledge/games/a-f/elden-ring.md),
`ER-007` and marker checkpoint 6, admits advisory map navigation before
Stormveil. Bandai Namco's [written gameplay overview](https://www.bandainamcoent.com/news/elden-ring-introduction-part-3-gameplay-overview)
shows a selected beacon creating a compass icon and blue world reference;
Guidance of Grace is a separate advisory feature. The
[official starter guide](https://en.bandainamcoent.eu/elden-ring/news/elden-ring-starter-guide-tips-know-playing-the-game)
also distinguishes placed map markers from discovered-Grace travel.
These written sources corroborate the request, not a newly observed PC
1.16/Regulation 1.16.1 binary or every current marker limit.

[Taxonomy Change 237](TAXONOMY_CHANGE_237.md) already distinguishes Pacific
Drive's free `ACT-676` point from calculated `ACT-227`/`SYS-510` routing and
`ACT-472`'s linked prospective line. Its accepted distinction and source
limits remain unchanged. Broadening `ACT-227` to absorb the Elden marker
would collapse that boundary rather than repair the assignment.

The five retained carriers admit road guidance in their scoped records:
[GTA V](../../knowledge/games/g-l/grand-theft-auto-v.md),
[Red Dead Redemption 2](../../knowledge/games/m-r/red-dead-redemption-2.md),
[Euro Truck Simulator 2](../../knowledge/games/a-f/euro-truck-simulator-2.md),
[Forza Horizon 6](../../knowledge/games/a-f/forza-horizon-6.md) and
[American Truck Simulator](../../knowledge/games/a-f/american-truck-simulator.md).
Their 30 paired explanation fields remain unchanged. Cyberpunk 2077 remains
a canonical product-system example, but its navigation module is explicitly
outside the current Arasaka packet (`CP-011`); this correction does not re-add
it to that signature.

## Membership and comparison impact

Exactly one game signature replaces `ACT-227` with `ACT-676`. Elden Ring still
has 45 genes. All 274 combination sets remain unchanged, including its
`COMB-0150` and routed `COMB-0143`/`COMB-0167`. Salience retains the same exact
partition with only that supporting ID replaced.

Six of Elden Ring's 512 pair scores change: shared road guidance disappears
against the five road carriers, while the free pin becomes shared with
Pacific Drive. Its closest prior game remains `GAME-0150` at `13 / 54`, and
its full-corpus closest remains `GAME-0295` at `17 / 55`. No closest-game
selection changes. Every other game signature and pair score is preserved.

The registry retains 3769 definitions, 3711 Active and 58 inactive. No gene
is merged, split, added or deprecated. Earlier P1/P2 checkpoint matrices
remain historical evidence; undoing only this recorded assignment reproduces
their exact original matrix, rather than pretending the current one is
unchanged. The complete source snapshots, six score deltas and acceptance
checks are in [the canonical audit](../normalisation/P2_CANONICAL_SOURCE_REVIEW_006.json).

The transfer gives `ACT-676` a second carrier, reducing the singleton-gene
count from 2806 to 2805. Its first appearance moves from `GAME-0500` to
`GAME-0152`, raising the recorded `GAME-0134`–`GAME-0153` mean from 21.65 to
21.7 newly introduced genes per game. Both changes are derived from the same
one-signature migration.
