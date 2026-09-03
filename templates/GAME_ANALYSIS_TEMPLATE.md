---
game_id: GAME-XXXX
slug: GAME_SLUG
game_title: GAME_TITLE
analysis_status: draft
reviewed: YYYY-MM-DD
combination_ids: []
gene_ids:
  action: []
  system: []
  constraint: []
  information: []
  objective: []
  time: []
---

# Game: GAME_TITLE

Use the canonical [vocabulary, genome signature and comparison
rules](../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe gene
instances but do not enter the signature.

## Analysis scope

- Version / ruleset:
- Primary decision loop:
- Entry and exit:
- Included:
- Excluded:
- Potential scoped modules:
- Direct-play status:

## Claim ledger

Sections may inherit these labels by claim ID. Add a row for every substantive
claim that is not a simple citation or question.

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `C-GAME-001` | | Observation / Hypothesis / Pattern / Strong Pattern / Confirmed | Direct / Corroborated / Limited / Conflicting | Low / Medium / High | |

## Basic data

- Release / origin:
- Platform or physical form:
- Puzzle family:
- Primary sources:
- Secondary sources:
- Claim IDs:

## Mechanical decomposition

### Action Genes

- Existing gene IDs:
- Candidate genes:
- Parameters:
- Claim IDs:

### System Behaviour Genes

- Existing gene IDs:
- Candidate genes:
- Resolution order:
- Parameters:
- Claim IDs:

### Constraint Genes

- Existing gene IDs:
- Candidate genes:
- Scarce strategic resources:
- Claim IDs:

### Information Genes

- Existing gene IDs:
- Candidate genes:
- Claim IDs:

### Objective Genes

- Existing gene IDs:
- Candidate genes:
- Success, evaluation and failure:
- Claim IDs:

### Time Genes

- Existing gene IDs:
- Candidate genes:
- Claim IDs:

## Reproducible transitions

Record edge cases that distinguish the rules from nearby systems.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| | | | | |

## Strategic and experiential structure

- Local decision:
- Medium-term planning:
- Long-term structure:
- Common heuristics:
- Failure attribution:
- Player-trust factors:
- Claim IDs:

## Replay and variation

- What changes between sessions:
- Randomness or procedural generation:
- Multiple viable strategies:
- Typical replay motive:
- Claim IDs:

## Adjacent systems and history

- Direct predecessors:
- Variants:
- Similar games:
- Important differences:
- Claim IDs:

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | | |
| System Behaviour | | |
| Constraint | | |
| Information | | |
| Objective | | |
| Time | | |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned:
- Exact genome matches: every exact prior match, with stable ID and title.
- Tied near matches: every positive non-exact maximum, with stable ID, title
  and exact `intersection / union = score` fraction.
- Supported combination subsets:
- Scan date: use the deterministic review date from front matter.

The validator recomputes the complete prior-game scan from canonical genome
signatures. Do not narrate or paste the full score ledger. Detailed comparison
is limited to exact and tied near matches; ties are retained using exact integer
fractions rather than rounded decimals.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| | | | Exact / tied near only |

- New genes: `none` / evidenced candidates requiring registry updates.
- Classification result: `New gene` / `New combination of known genes` /
  `Exact genome match` / `Baseline`.
- Evidence and reasoning:

## Taxonomy impact

- Registry changes: `none` / stable IDs and links.
- Taxonomy-change record: `none` / link.
- Candidate terms affected:

## Negative results

- `none` / linked structured records and affected claims.

## Delta summary

The headings below are the compact canonical delta ledger. Keep this source
record in English; reviewed Ukrainian research views are generated from the
separate localisation layer. Do not repeat the analysis; list only changes to
the corpus.

## New facts

- [Status | Evidence | Confidence] Claim and claim ID.

## New genes

- [Observation | Evidence | Confidence] `No new genes` / supported gene.

## New combinations

- [Observation | Evidence | Confidence] `No new combinations` /
  supported combination.

## Taxonomy changes

- [Observation | Evidence | Confidence] `No taxonomy changes` /
  `TAXONOMY_CHANGE_xxx`.

## New questions

-

## Next recommended game

- [Hypothesis | Limited | Confidence] GAME_TITLE
- Optimisation criterion:
- Expected information gain:
- Backlog impact:

## Why this game

- [Hypothesis | Limited | Confidence] Expected genome distance and coverage gain.
