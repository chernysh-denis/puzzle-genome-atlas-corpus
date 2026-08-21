# Taxonomy Change 014: Merge duplicated settlement and team-state disclosure

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-08-21
- Trigger: `REGISTRY_NORMALISATION_006` Information transfer tests

## Detected problem

Settlement panels were split by citizen species and game terminology, while
team objective state was split by HUD layout and match mode. The player can ask
the same decision-relevant questions after substituting population fields or
objective schema.

## Change

- Generalise `INF-086` to visible settlement population, needs, well-being,
  housing and workforce state; merge `INF-093` and `INF-097` into it.
- Generalise `INF-116` to visible live team, score/time and shared-objective
  state; merge `INF-121` and `INF-151` into it.

Radar geometry, enemy-visibility rules, exact population categories and
objective phases remain instance parameters or separate Information genes.

## Decision

- Decision: `Accepted`.
- Rationale: interface layout and game vocabulary do not change the disclosed
  state or the queries it supports.
- Implementation links: `INF-086`, `INF-093`, `INF-097`, `INF-116`, `INF-121`
  and `INF-151`.
