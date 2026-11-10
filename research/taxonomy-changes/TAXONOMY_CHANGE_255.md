# Taxonomy Change 255 Worker capability in material backed production

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-10-14
- Scope: `SYS-197` and its three existing carriers, `GAME-0126`, `GAME-0127`
  and `GAME-0139`; no membership or lifecycle change.

## Decision

`SYS-197` describes a worker's capability changing the completion rate or
finished quality of compatible material-backed production. The output need
not have a quality tier, and its value need not be modelled. Where those
properties exist, material choice and resulting quality may affect value.
Rate, quality and value are distinct outcomes, not three mandatory effects
of every task or one input that controls all three.

This corrects the former English conjunction, which required skill and
material to determine speed, quality and value together. It also aligns the
Ukrainian definition with a single portable condition: worker capability
must causally change work rate or finished quality. Material supply alone,
task eligibility and worker assignment do not satisfy this gene.

## Evidence by carrier

In [Dwarf Fortress](../../knowledge/games/a-f/dwarf-fortress.md), a skilled
craftsdwarf works supplied material at a workshop. The maintained
[workshop reference](https://dwarffortresswiki.org/index.php/Workshop)
describes skill-dependent speed or quality, including products without
quality modifiers. The [item-value reference](https://dwarffortresswiki.org/index.php/Item_value)
separates item form, material and resulting quality in value calculation.
The canonical metal-item transition now states those effects separately.

In [RimWorld](../../knowledge/games/m-r/rimworld.md), the relevant pawn skill
changes the quality distribution when an item has quality. The maintained
[skill reference](https://rimworldwiki.com/wiki/Crafting) explicitly says
Crafting level does not determine crafting speed; general labor speed and
required work do. The [quality reference](https://rimworldwiki.com/wiki/Quality)
places the quality result at completion, and the
[market-value reference](https://rimworldwiki.com/wiki/Market_Value)
relates ingredient value and quality to final value where applicable.
No crafting-skill speed claim is carried into the game explanation.

In [Palworld](../../knowledge/games/m-r/palworld.md), an eligible Pal with
Handiwork completes a material-backed workbench task. The maintained
[production reference](https://palworld.wiki.gg/wiki/Production) and
[Handiwork reference](https://palworld.wiki.gg/wiki/Handiwork) support
suitability-dependent work speed. They do not establish a Dwarf Fortress or
RimWorld style quality roll for that task. The older
[Workload article](https://palworld.wiki.gg/wiki/Work_Speed) is marked
outdated for version 1.0 and supplies no numerical parameter here.

The current corpus records are source-reconstructed rather than new native
sessions. The conclusion stays within the three recorded version scopes;
no exact hidden work-speed or quality formula is asserted.

## Adjacent boundaries and impact

`SYS-310` dispatches a Pal to a suitable job; `SYS-312` accumulates supplied
material and workload toward completion; `SYS-156` repeatedly runs a supplied
recipe. These can coexist with `SYS-197`, which requires a worker-dependent
rate or quality outcome. Eligibility, workload and recipe progress alone do
not substitute for that outcome.

All three game signatures, 274 combination sets and pair scores remain
unchanged. The registry retains 3769 definitions, 3711 Active and 58 inactive.
No gene is added, merged, split or deprecated. The four Ukrainian registry
fields are corrected; the six paired Dwarf Fortress and six paired RimWorld
pilot fields are corrected to their own mechanics. Palworld's six paired
fields are verified and retained. The original localisation batch remains
traceable. The exact before/after fields and checks are recorded in
[the canonical audit](../normalisation/P2_CANONICAL_SOURCE_REVIEW_007.json).
