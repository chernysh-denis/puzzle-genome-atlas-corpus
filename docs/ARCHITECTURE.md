# Repository Architecture

Puzzle Genome Atlas separates accepted knowledge from active investigation.
That boundary is the main scaling rule.

## Canonical vocabulary

These definitions are normative throughout the repository.

- A **gene** is one typed, bounded, decision-relevant mechanic represented by
  an immutable ID. Its admission rules live in
  [`knowledge/genes/README.md`](../knowledge/genes/README.md).
- A **parameter** is a value inside one gene, such as board capacity or
  direction set. It refines an instance of that gene but is not a gene and has
  no stable ID. If a parameter repeatedly changes decision structure enough to
  make one gene boundary misleading, that is evidence for a taxonomy change.
- A **genome** is the complete set of active gene IDs assigned to one scoped
  game or ruleset, partitioned into the six gene types. Parameters and source
  notes belong to the analysis but not to the signature defined below.
- An **analysis scope** is one explicitly bounded ruleset or primary decision
  loop. Every new or materially revised analysis must name that loop, its
  reproducible entry and exit, causally included systems, exclusions and
  potential scoped modules.
  An exhaustive union of mechanically separate product subsystems is not
  automatically a comparable genome. The accepted boundary and rollout are
  recorded in
  [`ADR-007`](architecture-decisions/ADR-007-bounded-game-analysis-scope.md).
- A **genome signature** is the canonical, parameter-free representation of a
  genome used for corpus comparison.
- A **combination** is a verified interaction among two or more genes from at
  least two types. Its gene set must be a proper subset of every supporting
  game's genome signature. A combination captures a reusable decision
  structure; it is not another name for a game or its full genome.
- A **mechanical profile** is a short game-specific description used for
  catalogue scanning. It is not a reusable taxonomic class.
- A **mechanical family** is a controlled, many-to-many grouping of games that
  share a broad causal structure. A game may belong to several families, and a
  family must be supported by at least two independently analysed games. The
  registry and its boundary rules live in
  [`knowledge/families/`](../knowledge/families/README.md).
- **Gene salience** is a reviewed, game-scoped presentation partition of the
  complete genome into defining, structural and supporting roles. It explains
  mechanical emphasis but never removes genes, assigns numeric weights or
  changes the canonical comparison formula. The pilot registry lives in
  [`knowledge/salience/`](../knowledge/salience/README.md).
- **Plain-language gene copy** is a reviewed, game-scoped explanation and
  concrete example shown above the unchanged canonical ID and label. The pilot
  lives in [`knowledge/plain-language/`](../knowledge/plain-language/README.md)
  and never changes taxonomy or similarity.

Presentation, theme, platform, mechanical profiles, family memberships, gene
salience, plain-language copy and release metadata are outside the genome signature.

## Genome signature

Let the six ordered gene types be

```text
T = (ACT, SYS, CON, INF, OBJ, TIM)
```

For a scoped game `g`, let `G_t(g)` be the finite set of active gene IDs of type
`t`. Its signature is the ordered tuple

```text
S(g) = (G_ACT(g), G_SYS(g), G_CON(g), G_INF(g), G_OBJ(g), G_TIM(g))
```

Each set is deduplicated and rendered in ascending ID order. The `gene_ids`
front matter of a game record is the canonical stored form; index signatures
are derived lookup copies and must contain the same IDs.

Parameters are deliberately excluded. Therefore an exact match means “the same
structure at the current gene resolution”, not identical numbers, board
geometry, presentation or implementation.

### Exact match

Games `a` and `b` are an exact genome match if and only if

```text
S(a) = S(b)
```

Equivalently, `G_t(a) = G_t(b)` for all six types.

### Near match

Flatten the signature into typed pairs:

```text
U(g) = {(t, id) | t in T and id in G_t(g)}
```

Define Jaccard similarity over the complete typed gene sets:

```text
sim(a, b) = |U(a) ∩ U(b)| / |U(a) ∪ U(b)|
```

Presentation surfaces may also show **smaller-genome coverage** as an
explanatory containment measure:

```text
coverage(a, b) = |U(a) ∩ U(b)| / min(|U(a)|, |U(b)|)
```

Coverage answers how much of the more compact signature is present in the
shared core. It must be labelled separately and must not replace Jaccard for
ranking, near-match selection or canonical comparison records.

Every valid genome contains at least one gene, so the denominator is non-zero.
This formula does not award similarity for two games merely lacking the same
gene type and introduces no untested type weights.

For a new game `a`, its **near matches** are all non-exact indexed games with a
positive score equal to the maximum non-exact `sim(a, x)` in the corpus. Ties
are retained. If every non-exact score is zero, there is no near match.

The score selects records for detailed comparison; it is not evidence that two
games feel alike or that their shared structure is novel. Parameters explain
decision-relevant differences after the mathematical scan.

## Top-level structure

```text
docs/        Method, governance, evidence model and research plan
knowledge/   Canonical genes, game genomes and verified combinations
research/    Leads, taxonomy proposals, candidates and negative results
templates/   Required contribution formats
web/         Thin Astro presentation and bounded static browser artifacts
ops/         Atlas-only feedback proxy and static release templates
scripts/     Repository-integrity validation
```

Root files are limited to public orientation and project governance.

## Stable identifiers

- Games: `GAME-xxxx`
- Genes: `ACT-xxx`, `SYS-xxx`, `CON-xxx`, `INF-xxx`, `OBJ-xxx`, `TIM-xxx`
- Combinations: `COMB-xxxx`
- Taxonomy changes: `TAXONOMY_CHANGE_xxx`

IDs are never reused. Renames change labels, not identifiers.

## Game-file scaling

Game analyses use stable alphabetical path shards:

```text
knowledge/games/0-9/
knowledge/games/a-f/
knowledge/games/g-l/
knowledge/games/m-r/
knowledge/games/s-z/
```

The shard is non-semantic, so a change in puzzle family never moves a file.

## Comparison scaling

Every new genome is still checked against the full corpus, but the result is
not copied as hundreds of prose rows into the new analysis.

1. Compare the complete game signatures in the game index using the rules
   above. For a subject game, the scan domain is every reviewed game with a
   lower numeric stable ID, so every unordered pair is owned once.
2. Test whether each verified combination's gene set is a subset of the new
   signature.
3. Record every exact match and every mathematically selected near match.
4. Keep any detailed comparison prose limited to those selected records; the
   concise exact and tied-near fields are always required.
5. Put shared combination knowledge in one `COMB-xxxx` record.

This preserves exhaustive matching while avoiding quadratic narrative
duplication.

[`ADR-006`](architecture-decisions/ADR-006-derived-comparison-results.md)
defines pair scores as derived data: the complete scan is recomputed from
canonical signatures, while records retain exact matches, all tied near
matches, supported combinations and scan metadata. Its accepted migration is
implemented by `scripts/migrate_comparisons.py`; `--check` proves that all game
sections match the deterministic `genome-jaccard-v1` renderer. The complete
matrix and per-game scan digests are not stored.

## Integrity checks

`scripts/generate_indexes.py` deterministically derives the game index,
combination index and marked completed-game catalogue blocks from canonical
records plus the short mechanical-profile manifest. Its `--check` mode detects
drift. `scripts/validate_repository.py` separately checks the reusable family
registry, including stable IDs, bilingual definitions, known game references,
minimum two-game support and complete game coverage.
[`ADR-002`](architecture-decisions/ADR-002-generated-derived-indexes.md)
defines ownership and generated-file boundaries.

`scripts/validate_repository.py` verifies local Markdown links, stable-ID
uniqueness, controlled metadata values, gene boundaries, game front matter,
type-correct gene references, path shards, combination subsets, index
signature equality, recomputed exact and tied-near comparison selections and
byte-for-byte generated-output freshness. It rejects legacy full-score ledgers
and non-selected narrated pair scores. Continuous validation also runs
Markdown lint.

TODO: automatic claim-to-prose coverage is intentionally deferred. Determining
whether arbitrary prose contains a substantive claim requires human judgement;
the validator checks claim-ledger field values, while review checks whether the
ledger is complete. Do not add heuristic prose classification until repeated
review failures justify it.

TODO: parameter schemas and a separate multi-maintainer governance document
remain deferred because the corpus has not exposed their trigger conditions.
Generated indexes are implemented by `INDEX_AUTOMATION_001`; extend generation
only when another repeated structured view demonstrates comparable drift.

## Build and authoring scaling

ADR-011 establishes the static-first target: reviewed Git is projected
deterministically in-process; Astro emits immutable HTML and bounded static
JSON; Caddy serves those files. There is no corpus API or database runtime.

Local and pull-request validation generates the normalized direct projection
twice, verifies its content identity, runs one pinned Astro build and tests the
already-built output. Publication creates a separate allowlisted public Git
projection. PostgreSQL and Go are not dependencies of contribution, CI,
publication, site build or production runtime.

Markdown and reviewed JSON in private Git remain the human authoring/evidence
authority until a separately accepted editor exists. The accepted target
publishes one immutable static website release. The public Git corpus remains
an exact append-only projection rather than an independently editable mirror.

Public research navigation is locale-separated under
[`ADR-012`](architecture-decisions/ADR-012-locale-separated-public-research.md).
English site pages link to English canonical Markdown. Ukrainian site pages
link to deterministic Ukrainian research overviews generated from reviewed
localisation records under `knowledge/locales/uk/research/`. A missing
localised record fails publication; it never falls back across the language
boundary.

Dependency-free derived Python tools share the readers in
`scripts/generate_indexes.py`. The repository validator keeps an independent
parse so it can detect disagreement with generated output rather than repeat
the generator's assumptions. New tooling must reuse the appropriate existing
boundary instead of adding another Markdown parser.

The historical PostgreSQL implementation and SQL migrations remain in Git
history and `docs/migrations/archive/postgresql/`; they are audit evidence, not
executable architecture. The historical parsing and payload measurements remain in the
[`Scaling implementation report`](SCALING_IMPLEMENTATION_REPORT.md). ADR-009
selected PostgreSQL for ownership/release governance rather than a crossed
parsing threshold. The later implementation and independent audit showed that
an immutable artifact can retain those release identities without storing the
complete corpus and public export bytes in PostgreSQL; ADR-010 therefore
supersedes the permanent database authority. Incremental or sharded site builds
remain deferred until a complete local build exceeds ten minutes or CI exceeds
twenty minutes. A future Studio remains a separate authoring decision and may
not silently become another corpus authority.

[`ADR-008`](architecture-decisions/ADR-008-concept-lab-static-product-boundary.md)
continues to govern Concept Lab as a bounded static derived surface. In API
mode its versioned shards are built from the same pinned corpus revision as the
pages; visitor-authored state remains ephemeral and client-side. Authenticated
writes, server persistence, non-rebuildable data, runtime Lab state or a
runtime LLM still require a new decision.

## Architecture change policy

This revision is intended to be the last broad relocation. Future structural
changes require:

1. a concrete scaling or integrity failure;
2. an architecture decision record in `docs/architecture-decisions/`;
3. a migration plan with link validation;
4. preservation of stable IDs and Git history.

Adding genes, analyses, combinations or validators is normal knowledge work and
does not count as an architecture change.
