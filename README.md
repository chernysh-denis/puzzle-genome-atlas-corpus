# Puzzle Genome Atlas — Canonical Corpus

This public repository contains the reviewed, stable-ID research corpus behind
[Puzzle Genome Atlas](https://puzzlegenome.org). The website, generated
artwork, internal research leads and development tooling live in a separate
private working repository. Deterministic `scripts/verify_*.py` controls cited
by canonical records are included as public research evidence.

## Corpus snapshot

- 261 reviewed game genomes
- 2296 active typed mechanic genes
- 259 verified causal combinations
- reviewed Ukrainian presentation data under `knowledge/locales/uk/`

## Browse

- [Game genomes](knowledge/games/INDEX.md)
- [Ukrainian research overviews](knowledge/locales/uk/research/README.md)
- [Gene registry](knowledge/genes/README.md)
- [Verified combinations](knowledge/combinations/INDEX.md)
- [Evidence model](docs/EVIDENCE_MODEL.md)
- [Architecture and stable identifiers](docs/ARCHITECTURE.md)
- [Executable research controls](scripts/)

Stable IDs are never reused. English records are canonical; reviewed Ukrainian
translations form a separate presentation layer. Empty regions and single-game
combinations are research leads, not proof of novelty.

## Licence

Released under the [MIT License](LICENSE).
