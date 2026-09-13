# Taxonomy Change 034: Generalise the strike-funded active-effect reserve

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-07
- Trigger: independent closure review of `GAME-0274` Hollow Knight.

## Current classification

- `ACT-190` was titled “Cast one hero or item ability” and required a learned
  hero skill or carried-item active, although its parameters already admitted a
  channel and several carriers use innate character capabilities.
- `SYS-397` was titled “Convert needle strikes into Silk-funded Bind and
  skills” and named one sequel's weapon, reserve, heal and learned abilities.
- `CON-351` likewise required a full Silk spool for Bind or a declared Silk
  Skill cost.
- `GAME-0150` Hollow Knight: Silksong was the only carrier for `SYS-397` and
  `CON-351`. The Batch 016 candidate reused both for its predecessor without
  first making their canonical wording portable.

## Detected problem

- Hollow Knight's authored manual directly establishes the same causal law:
  eligible direct attacks add SOUL, holding Focus spends enough SOUL to heal,
  and Focus is unavailable without the required reserve state.
- Needle versus Nail, Silk versus SOUL, a full spool versus a smaller declared
  cost, and Bind versus Focus are product parameters. None changes who commits
  the action, how the reserve is generated, what gates the effect or when the
  reserve is consumed.
- Creating a predecessor-specific action, system or constraint would encode
  product vocabulary as taxonomy and duplicate the already reviewed boundary.

## Evidence

- Primary evidence: the Team Cherry-authored 2017 English game manual states
  that attacks gain SOUL, holding Focus consumes SOUL and repairs health, and
  the HUD exposes the relevant health and reserve state. The manual is preserved
  at <https://cdn.pidgi.net/images/5/51/Manual_EN_-_Hollow_Knight.pdf>; its
  authorship and copyright page are inspected directly.
- Availability and provenance corroboration: Fangamer's licensed physical-game
  listing states that every physical copy includes a manual:
  <https://www.fangamer.com/products/hollow-knight-switch-ps4-pc-game>.
- Carrier evidence: the bounded decompositions for
  [`GAME-0150`](../../knowledge/games/g-l/hollow-knight-silksong.md) and
  [`GAME-0274`](../../knowledge/games/g-l/hollow-knight.md).
- Counterevidence considered: Silksong Bind consumes a full spool and the
  predecessor Focus consumes a smaller fixed amount. This changes a threshold
  parameter, not the legality relation. Silksong also has learned Silk Skills;
  the predecessor's scoped route excludes later offensive spells, so only the
  recovery branch is exercised there.

## Proposed change

- Rename and generalise `ACT-190` to committing one currently available active
  character or carried-item ability, with target form and held channel as
  parameters. Add Hollow Knight Focus as a supported instance.
- Rename and generalise `SYS-397` to converting direct strikes into one bounded
  personal reserve spent by active recovery or learned abilities.
- Rename and generalise `CON-351` to requiring each reserve-spending active
  effect's declared resource predicate and consuming its declared amount when
  the effect is accepted.
- Update the reviewed Ukrainian canonical records to the same portable bounds.
- Do not create, merge, split, deprecate or retire any gene.

## Genome and combination impact

- `GAME-0274` admits `ACT-190`, `SYS-397` and `CON-351` in the corrected
  signature. `ACT-190` was omitted by the candidate; the other two were already
  present but written in sequel-specific terms.
- No earlier reviewed signature changes. `GAME-0150` retains the same gene set
  and `COMB-0148` retains the same IDs.
- Definition and Active totals do not change. Only canonical wording, evidence
  reach, localisation and the new carrier usage change.

## Decision

- Decision: `Accepted`.
- Decided by: independent lower-ID scan, direct manual evidence and the two-way
  transfer test.
- Rationale: substitute weapon, reserve, threshold and effect names in either
  direction and the decision law remains unchanged. Those values belong in the
  game-scoped explanation, not in the canonical label.
- Implementation links: `ACT-190`, `SYS-397`, `CON-351`, `GAME-0150`,
  `GAME-0274`, `COMB-0148`.

## Change history

- 2026-09-07 — created and accepted during the independent `GAME-0274`
  closure unit.
