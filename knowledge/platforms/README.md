# Platform registries

This directory owns structured platform identity, exact game analysis targets
and evidence-bounded known-release coverage. The normative schema, audit
language and migration gates are defined in
[`PLATFORM_COVERAGE_POLICY`](../../docs/PLATFORM_COVERAGE_POLICY.md) and
accepted by
[`ADR-014`](../../docs/architecture-decisions/ADR-014-structured-platform-and-release-coverage.md).

The implemented registries are:

```text
registry.json  stable platform/form identities, English labels and local icons
games.json     one exact analysisTarget plus separately audited releases per game
```

Reviewed Ukrainian platform labels live in
`knowledge/locales/uk/platforms.json`. None of these fields enters a genome
signature. The current 297-game corpus contains one evidenced
`analysisTarget` per game. `PLATFORM_RELEASE_AUDIT_001` adds only release
platforms corroborated by two independently maintained catalogue surfaces;
unpaired statements remain in the audit evidence as unresolved and are not
published as releases. The dated result is a verified-known set under that
bounded method, never a claim of exhaustive platform coverage.

Platform marks are generated from `registry.json`, not from a second hard-coded
platform list. Current high-recognition platforms use locally drawn identity
pictograms; the remaining registry identities use deterministic, distinct name
marks. They deliberately do not embed or hotlink vendor artwork:

```sh
python3 scripts/generate_platform_icons.py --check
```
