# Taxonomy Change 258 Current HP check for a held Berry

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-10-14
- Scope: existing `SYS-1213` in `GAME-0463`; no carrier or lifecycle change.

## Decision

`SYS-1213` activates when a living holder's **current** HP is strictly below
the item's threshold at an eligible held-item check in battle. A fresh drop
across the threshold is not required. In the original Gold carrier, the check
runs between turns, after faint settlement. An ordinary Berry then restores
up to ten HP and is consumed once without a PACK command.

The earlier definition said the holder *crosses* the threshold. The
[pinned Gold battle caller](https://github.com/pret/pokegold/blob/62388c7204e5d13aa05b4231e220b6760584d1b5/engine/battle/core.asm#L205-L249)
invokes held-item handling between turns, and its
[HP-healing handler](https://github.com/pret/pokegold/blob/62388c7204e5d13aa05b4231e220b6760584d1b5/engine/battle/core.asm#L4009-L4116)
reads current and maximum HP. It contains no previous-HP comparison or
damage flag. The [item attributes](https://github.com/pret/pokegold/blob/62388c7204e5d13aa05b4231e220b6760584d1b5/data/items/attributes.asm#L353-L359)
give the ordinary Berry its ten-HP amount. These pinned source passages
support the check's predicate and timing, not a claim of direct cartridge
play or a rule for every later Pokémon version.

The after-damage transition in the [Gold decomposition](../../knowledge/games/m-r/pokemon-gold-version.md)
remains a valid example, but damage in the immediately preceding action is
not a universal condition. The historical
[`TAXONOMY_CHANGE_200`](TAXONOMY_CHANGE_200.md) still records the original
isolation decision; this decision supersedes only its ambiguous
*falls-below* phrasing. No new gene or reassignment follows. `GAME-0463`
remains the sole carrier, no verified combination contains `SYS-1213`, and
all signatures and pair scores remain unchanged. Exact before/after fields
and verification are in the
[canonical audit](../normalisation/P2_CANONICAL_SOURCE_REVIEW_010.json).
