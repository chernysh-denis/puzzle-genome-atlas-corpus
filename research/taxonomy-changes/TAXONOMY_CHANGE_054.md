# Taxonomy Change 054: Generalise contextual defeat-to-recovery conversion

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-09
- Trigger: `GAME-0286` — DOOM Eternal.
- Affected gene: `SYS-770`.
- Lifecycle changes: none.
- Earlier signature changes: none.

## Problem

`SYS-770` was first isolated for the Glory Kill in DOOM (2016). Its result
boundary was already portable — a legal contextual defeating action creates
compatible recovery drops — but the definition required a staggered target and
explicitly excluded the later Chainsaw. DOOM Eternal places both actions inside
one first-mission packet: Glory Kill legality depends on stagger and reach,
whereas Chainsaw legality depends on target, reach and fuel; both defeat the
target and create a declared class of recoverable world drops.

Keeping the exclusion would force a duplicate System gene distinguished only by
the source action and resource class. Merging the actions or constraints would
erase a real player decision. The correct boundary is therefore to generalise
the shared System result while retaining separate Action and Constraint genes.

## Decision

- Rename `SYS-770` from `Convert a contextual finisher into compatible recovery
  drops` to `Convert a contextual defeating action into compatible recovery
  drops`.
- Replace the stagger-specific definition with a legal-contextual-action
  definition.
- Keep `ACT-419` + `CON-589` as the Glory Kill command and its stagger/reach
  predicate.
- Reuse lower-ID `ACT-190` + `CON-269` for the Chainsaw command and its
  target/range/fuel predicate.
- Add DOOM Eternal's first-mission Glory Kill and Chainsaw results as support.
- Do not change `GAME-0245`, `COMB-0243`, lifecycle or any earlier signature.

## Carrier audit

Before this change, the only reviewed carrier was `GAME-0245` — DOOM (2016),
and the only combination containing the gene was `COMB-0243`. Its Glory Kill
still satisfies the generalised boundary exactly: the command is contextual,
legally defeating and produces compatible recovery drops. The new wording adds
no action, legality or resource source to that record.

`GAME-0286` contributes two legal source actions. They share only the System
result; their different predicates remain visible in the same signature.

## Rejected alternatives

- New Chainsaw-only System gene: rejected as duplication by source action and
  resource parameter.
- Merge `ACT-419` into `ACT-190`: rejected because one is a prompted stagger
  finisher and the other a target/resource-gated active capability.
- Merge `CON-589` into `CON-269`: rejected because stagger/reach opportunity is
  not fuel/readiness legality.
- Extend `SYS-770` to ordinary defeats: rejected; an ordinary kill without the
  declared contextual conversion remains outside the boundary.

## Localisation disposition

- `corrected`: Ukrainian `SYS-770` label, definition, includes and excludes are
  rewritten against the final English boundary.
- `verified`: all earlier carrier meaning is retained.
- `retained-with-reason`: `Glory Kill`, `Chainsaw`, `DOOM (2016)` and
  `DOOM Eternal` remain recognisable official names or product terms.

## Acceptance

The change is accepted inside the complete `GAME-0286` unit only if repository,
comparison, localisation, generated-artifact, web, browser and axe gates pass.
