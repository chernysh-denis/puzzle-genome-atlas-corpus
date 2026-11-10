# Taxonomy Change 252 Manual harvesting input and yield destination

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-10-14
- Scope: `ACT-122`, its 11 existing carriers and six combinations;
  no signature or lifecycle migration.

## Decision

`ACT-122` requires direct work on a reachable world resource or recoverable
entity that yields materials or a recovered item. Holding a command,
repeating strikes or initiating timed work are input parameters. The yield
may enter inventory directly or require subsequent collection. A compulsory
tool, visible progress bar and automatic inventory delivery are not universal
requirements.

Material or item recovery remains the positive boundary. Merely deleting an
entity, transferring an already loose or stored item, autonomous mining and
weapon attacks on enemies do not qualify. Output availability and later
collection remain subject to the carrier's own rules; no universal full-node
depletion or immediate pickup guarantee is introduced.

## Evidence and transfer

[Factorio](../../knowledge/games/a-f/factorio.md) admits held manual mining and
recovery of placed entities. Its [official Player documentation](https://wiki.factorio.com/Player)
distinguishes these requests from picking up already loose items.
[Valheim](../../knowledge/games/s-z/valheim.md), `VLH-004`, instead separates
resource work, resulting drops and eligible contact pickup, represented by
`SYS-222`. [7 Days to Die](../../knowledge/games/0-9/7-days-to-die.md) admits
held or repeated harvesting within its bounded tutorial.
[Project Zomboid](../../knowledge/games/m-r/project-zomboid.md) admits timed
fixture dismantling with its own tool and skill conditions.

The existing dossiers and paired explanations also admit manual work in
[Satisfactory](../../knowledge/games/s-z/satisfactory.md),
[Dyson Sphere Program](../../knowledge/games/a-f/dyson-sphere-program.md),
[Palworld](../../knowledge/games/m-r/palworld.md),
[Rust](../../knowledge/games/m-r/rust.md),
[Don't Starve Together](../../knowledge/games/a-f/dont-starve-together.md),
[No Man's Sky](../../knowledge/games/m-r/no-mans-sky.md) and
[Starfield](../../knowledge/games/s-z/starfield.md).
Bethesda's [resource guide](https://help.bethesda.net/app/answers/detail/a_id/61082)
corroborates reachable solid-resource cutting with the Cutter and distinguishes
outpost extraction. These sources support the manual production boundary,
not a newly measured input binding for every pinned build.

Dyson Sphere Program's explanation no longer copies Factorio's unsupported
held-progress requirement. Palworld's explanation likewise names direct
resource work rather than requiring a held button. Their existing examples
and the other nine paired explanations remain unchanged. Exact input
cadence not established by a scoped dossier remains unspecified.

## Adjacent boundaries and prior decision

`ACT-119` admits changing live factory entities; `ACT-159` targets mutable
terrain cells; `ACT-161` commits direct strikes; `ACT-199` transfers existing
items; `ACT-213` covers cultivated crop interactions. Some transitions overlap
manual harvesting. This correction does not merge these IDs or establish
pairwise minimality.

[Taxonomy Change 145](TAXONOMY_CHANGE_145.md) remains an immutable historical
decision. Its held-input and direct-inventory premises are superseded for
`ACT-122`, but its rejection of regular daytime PvZ shovelling remains valid:
`ACT-547` removes a defender without recovering material or an inventory item.
The [PopCap readme](https://akamai.cdn.ea.com/eadownloads/u/f/manuals/GAME-PVZ/en_US_readme.html)
documents removal, not a recovery/refund for that scoped operation. Its Mac
version does not establish binary equivalence with Windows GOTY or every mode.

## Corpus and localisation impact

All 513 game signatures and 274 combination sets remain unchanged. The six
combinations containing `ACT-122` retain their members; all Jaccard scores
are unchanged. The registry retains 3769 definitions, 3711 Active and 58
inactive. No gene is added, merged, split or deprecated.

The Ukrainian definition, inclusions and exclusions preserve the corrected
complete source boundary; the original integration batch is retained.
Four bilingual explanation fields across Dyson Sphere Program and Palworld
are corrected, while their labels and examples remain unchanged. Snapshots,
carrier-specific source qualifications and verification results belong to
[the canonical review](../normalisation/P2_CANONICAL_SOURCE_REVIEW_004.json).
