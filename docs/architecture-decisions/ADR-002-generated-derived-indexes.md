# ADR-002 — Generated derived indexes

- Status: `Accepted`
- Date: 2026-08-12
- Decision owner: Puzzle Genome Atlas maintainer

## Context

The 46-game final audit found two omissions in human-facing completed-game
catalogues even though canonical game and combination records were valid. The
trigger in ADR-001 for replacing manual index maintenance has therefore been
met.

Four repository views repeat facts owned elsewhere:

- the complete game-signature table;
- the verified-combination table;
- the root README completed-game catalogue;
- the game README completed-game catalogue.

Maintaining those views by hand creates omission and drift risk. Family labels
are useful for navigation but deliberately remain outside the genome signature
and may change without moving a game file.

## Decision

- Treat game files, combination files and
  `knowledge/games/index-metadata.json` as the inputs to derived indexes.
- Keep short family navigation labels in that explicit metadata manifest;
  they are curatorial presentation metadata, not genes or stable taxonomy IDs.
- Generate both complete index files and the marked completed-game blocks with
  the dependency-free `scripts/generate_indexes.py` command.
- Sort records by numeric stable ID and gene sets by the canonical type and ID
  order so repeated generation is byte-identical.
- Make generation fail on a missing or surplus family-label entry rather than
  emit a partial index.
- Provide `--check` for non-mutating drift detection and call the same renderer
  from `scripts/validate_repository.py` so continuous validation rejects stale
  derived files.
- Keep generated files in Git for readable diffs, direct browsing and links;
  contributors regenerate them after changing an input record.

## Consequences

- A new or edited canonical record cannot silently disappear from an index or
  completed-game catalogue.
- Review diffs remain deterministic and require no third-party runtime.
- Contributors must add one short family label for each game, but that label
  cannot affect stable paths, genomes or comparison results.
- Manual edits inside generated files or marked blocks are overwritten and
  rejected by validation.
- Other prose remains hand-maintained; only repeated structured views are
  generated.

## Migration

`INDEX_AUTOMATION_001` captured the 46 existing family labels in the manifest,
added generation markers, regenerated all four outputs and integrated drift
checking without changing any stable ID, genome, claim, combination or
taxonomy lifecycle.
