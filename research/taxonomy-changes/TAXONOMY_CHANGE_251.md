# Taxonomy Change 251 Character control policy in equipped item replacement

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-10-14
- Scope: `ACT-040` and its four current carriers; no signature or lifecycle migration.

## Decision

`ACT-040` describes a player replacing an equipped item with one acquired
inventory item in a compatible slot, changing that character's combat
statistics. Subsequent autonomous or directly commanded combat is a parameter
of the recipient, not a requirement of this equipment command. The inventory
source, compatible slot, replacement and statistical effect remain required.

The four current carriers retain their existing IDs and signatures. Terraria's
game-specific explanation is restricted to armour and accessory replacement;
selecting a weapon or tool on the hotbar remains `ACT-164`.

## Evidence and transfer

- [Loop Hero](../../knowledge/games/g-l/loop-hero.md), `LH-003`, separates the
  player's compatible inventory-item replacement from the hero's subsequent
  automatic combat. The [developer account](https://www.gamedeveloper.com/design/postmortem-loop-hero)
  likewise distinguishes player equipment choices from autonomous walking
  and fighting; its development mockups do not establish exact current locks.
- [Clair Obscur Expedition 33](../../knowledge/games/a-f/clair-obscur-expedition-33.md)
  and its reviewed weapon-replacement explanation admit the same slot choice
  before later directly selected turn commands and reactive execution.
- [Baldur's Gate 3](../../knowledge/games/a-f/baldurs-gate-3.md) admits replacing
  a party member's inventory equipment; direct party control and initiative
  scheduling do not change that equipment request.
- [Terraria](../../knowledge/games/s-z/terraria.md), equipment checkpoint 5,
  separates compatible armour/accessory equipment from active hotbar
  selection. Its existing Hermes Boots example replaces an accessory rather
  than turning a weapon or tool into worn equipment.

Within these admitted cases, substituting the character and its subsequent
control policy preserves the inventory source, slot compatibility and
replacement request. Removing an equipped occupant or changing later
combat control does not turn a generic storage transfer, automatic stat
increase or class choice into this command. This is a source-model
reconciliation, not a new authenticated playthrough of every pinned build.

## Adjacent boundaries

`ACT-199` also accepts some equipment transfers, but additionally admits
reachable items and compatible stack/storage transfers with optional
replacement. `ACT-215` configures a bounded preparation loadout. Neither is
silently merged, narrowed or substituted here. The overlap with `ACT-199`
remains a separate minimality question, not a declared independent-boundary
proof or a reason to suppress duplicate routing.

[Taxonomy Change 226](TAXONOMY_CHANGE_226.md) rejects a spirit ready/standby
change because it is not equipped-loot replacement. That rejection remains
valid after the control-policy correction.

## Corpus and localisation impact

All 513 game signatures and 274 combination sets remain unchanged, including
`COMB-0151`. The registry retains 3769 definitions, 3711 Active and 58 inactive.
No gene is added, merged, split or deprecated; all Jaccard scores are unchanged.

The Ukrainian label, definition, examples and exclusions are corrected against
the complete source contract. The original integration batch is preserved.
Terraria's two labels and two explanations are corrected; its paired Hermes
Boots example is retained as an official item name. The other three carrier
explanations retain their game-specific control and equipment conditions.

The gene's evidence-quality label becomes `Corroborated` for the broader
four-carrier boundary; Loop Hero's developer evidence remains part of that
support. Implementation snapshots and verification results are recorded in
[the canonical review](../normalisation/P2_CANONICAL_SOURCE_REVIEW_003.json).
