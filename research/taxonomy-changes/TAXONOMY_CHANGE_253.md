# Taxonomy Change 253 Explicit food consumption across survival meters

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-10-14
- Scope: `ACT-165`, ten existing carriers and three combinations;
  no signature or lifecycle migration.

## Decision

`ACT-165` requires an explicit command for the controlled avatar to eat
eligible food, consuming its chosen whole item or portion and applying the
food's declared nourishment and associated condition effects. Food may be
carried or available from a reachable feeding fixture. Holding use, whole-item
consumption, hunger and saturation are Minecraft parameters, not universal
requirements. Resolution may be immediate or gradual under the carrier's
existing survival model; food is not guaranteed to improve every meter.

The positive decision remains when and what the avatar eats, rather than
food manufacture, autonomous feeding, drinking solely for hydration or an
automatic contact-to-growth transition. Food that also affects health is
not thereby a healing potion. No exact digestion, safety or beneficial-food
guarantee is added.

## Evidence and transfer

[Minecraft](../../knowledge/games/m-r/minecraft.md), `MNC-006`, admits held
food use. The official [mushroom-stew article](https://www.minecraft.net/en-us/article/taking-inventory--mushroom-stew)
corroborates selected held use, hunger and saturation, but does not establish
every food exception in Java 26.2.
[Project Zomboid](../../knowledge/games/m-r/project-zomboid.md) admits timed
whole or partial food consumption, while
[DayZ](../../knowledge/games/a-f/dayz.md), `DAYZ-005`, `DAYZ-007` and
`DAYZ-009`, separates consumption, gradual energy transfer and contamination.
Bohemia's [quantity-based self-eating source](https://github.com/BohemiaInteractive/DayZ-Script-Diff/blob/86974a0f5bd16b1ee3e334ad828133c93dca80a1/scripts/4_world/classes/useractionscomponent/actions/continuous/actioneat.c)
and [quantity component](https://github.com/BohemiaInteractive/DayZ-Script-Diff/blob/86974a0f5bd16b1ee3e334ad828133c93dca80a1/scripts/4_world/classes/useractionscomponent/actioncomponents/cacontinuousquantityedible.c)
corroborate portioned commands. That public source commit is not asserted to
be the exact frozen 1.29.163709 binary.

[Kingdom Come Deliverance II](../../knowledge/games/g-l/kingdom-come-deliverance-ii.md),
`KCD2-004`, explicitly restores nourishment by eating from the opening pot.
Requiring carried stock would contradict that accepted Fortuna transition.
The fixture case does not establish measured depletion of the pot itself.

The admitted scopes and paired explanations also retain self-eating in
[Palworld](../../knowledge/games/m-r/palworld.md),
[Rust](../../knowledge/games/m-r/rust.md),
[Subnautica](../../knowledge/games/s-z/subnautica.md),
[Don't Starve Together](../../knowledge/games/a-f/dont-starve-together.md),
[PEAK](../../knowledge/games/m-r/peak.md) and
[The Long Dark](../../knowledge/games/s-z/the-long-dark.md).
Their hunger, calorie, food-reserve, bonus-stamina and other item properties
remain local parameters. Hinterland's [condition documentation](https://hinterlandgames.zendesk.com/hc/en-us/articles/360042349471-Condition-and-Character-Status)
separates Hunger, Thirst, Warmth, Fatigue and Condition rather than requiring
Minecraft saturation.

## Adjacent boundaries and prior decision

`ACT-311` concerns a carried drink's hydration; `ACT-200` begins interruptible
restorative-item use; `ACT-341` operates authored fixtures. A food command can
overlap those broader input descriptions. This correction neither merges
them nor certifies pairwise minimality.

[Taxonomy Change 112](TAXONOMY_CHANGE_112.md) remains unchanged. Its description
of `ACT-165` as only carried hunger-restoring food is superseded, but its
Spore rejection remains valid. The Cell stage resolves mouth-compatible
contact into DNA and growth, not an explicit self-eating command using a
selected food item or feeding fixture. `SYS-1014`, `SYS-1015` and the Spore
signature remain unchanged.

## Corpus and localisation impact

All 513 game signatures, 274 combination sets and Jaccard scores remain
unchanged. `COMB-0127`, `COMB-0140` and `COMB-0201` retain their members.
The registry retains 3769 definitions, 3711 Active and 58 inactive. No ID is
added, merged, split or deprecated.

The four Ukrainian registry fields are corrected against the complete
source contract, including the exact healing-potion exclusion. The original
integration batch is preserved. All 60 carrier-copy fields retain their
game-specific food, portion, meter and fixture conditions. The broader
ten-carrier evidence-quality label is `Corroborated`, not a new direct-play
claim. Before/after snapshots, qualifications and verification results are in
[the canonical review](../normalisation/P2_CANONICAL_SOURCE_REVIEW_005.json).
