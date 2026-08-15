# Taxonomy Change 007: Merge structured investigation completion schemas

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-08-14
- Trigger: `REGISTRY_NORMALISATION_004` Objective boundary audit

## Detected problem

`OBJ-017` required every mandatory identity-and-fate field in Return of the Obra
Dinn's roster ledger. `OBJ-028` required every mandatory actor/action/object/
location field in The Case of the Golden Idol's event Scroll. Both complete an
investigation only when every slot of a declared structured semantic account is
filled with accepted values supported by fixed evidence.

Roster rows versus an event statement changes account topology and field
grammar. It does not change the terminal predicate. The transfer test preserves
all required fields by substituting the declared schema.

## Change

- Generalise `OBJ-017` to **complete exact structured evidence account**.
- Add event count, account topology and semantic-field grammar as parameters.
- Replace `OBJ-028` with `OBJ-017` in The Case of the Golden Idol.
- Mark `OBJ-028` as `Merged` and retain it as a historical alias.

## What does not change

- Evidence navigation, phrase extraction, phrase-slot editing and validation
  remain distinct Action, Information and System genes.
- `COMB-0046` remains the shared immutable-evidence inspection core; its gene
  set does not contain either objective.
- `COMB-0023` does not become a subset of Golden Idol's genome.

## Impact

- Active genes: 485 → 484.
- Reused active genes: 119 → 120.
- Active singleton genes: 366 → 364.
- Obra Dinn/Golden Idol Jaccard similarity: `3 / 17 = 0.176471` →
  `4 / 16 = 0.250000`.

## Decision

- Decision: `Accepted`.
- Rationale: the old records encoded two schemas of one evidence-account
  completion predicate.
