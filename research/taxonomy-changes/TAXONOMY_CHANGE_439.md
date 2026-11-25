# Taxonomy Change 439 — Relocate one floor unit through a tile hold

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-11-24
- Scope: [GAME-0693](../../knowledge/games/s-z/void-stranger.md),
  B002 of the commercial Windows release.
- Decision: admit ACT-912 and SYS-1967. The corpus grows from
  4,804 to 4,806 definitions, with 4,748 Active.

| Gene | Accepted boundary | Nearest reuse considered |
| --- | --- | --- |
| ACT-912 | From supported footing, lift the ordinary floor unit in front into the empty tool. | ACT-122 recovers material or an entity rather than retaining a floor unit for a matching cell. ACT-721 slides a tile directly into a neighbouring vacancy. ACT-162 already describes the separate placement input. |
| SYS-1967 | A floor unit leaves one hole, fills a one-tile hold, then becomes support in an unoccupied recipient. | SYS-217 resolves placement from an already held world item. It does not conserve support across pickup, transit and placement. SYS-096 settles a moving log into supported terrain without an inventory hold. |

Reuse CON-208 for the placement predicate and OBJ-164 for the
stair to the successor floor with retained progression. Earlier
definitions and signatures remain intact.
