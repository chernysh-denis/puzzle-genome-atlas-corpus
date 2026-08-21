# Taxonomy Change 012: Merge subject-specific player commands

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-08-21
- Trigger: `REGISTRY_NORMALISATION_006` Action transfer tests

## Detected problem

Five Action records repeated existing player authority while encoding the
purchase window, progression label, crafting duration or loadout subject in the
Action ID. Those differences are parameters or independently represented
System/Constraint rules.

## Change

- Merge `ACT-182 → ACT-130` and generalise the survivor to one offered asset or
  service bought with current scoped currency.
- Merge `ACT-220 → ACT-191` and parameterise match-local or persistent
  character-development points.
- Merge `ACT-252 → ACT-123` and make the Action select a known recipe and
  quantity without owning immediate or queued resolution.
- Merge `ACT-239 → ACT-215` and `ACT-242 → ACT-215`; parameterise raid, match,
  checkpoint, class, augment and Crest subjects while retaining their distinct
  legality Constraints.

## Evidence

- `GAME-0137`, `GAME-0143`, `GAME-0149`, `GAME-0150` and `GAME-0153` provide
  the merged aliases.
- Existing supporters of `ACT-130`, `ACT-191`, `ACT-123` and `ACT-215` provide
  the two-way comparison boundaries.

## What does not change

- Buy-window location and timing remain in Counter-Strike constraints.
- XP conversion remains System Behaviour, not part of `ACT-191`.
- Craft duration and station conversion remain System Behaviour.
- Augment capacity, class whitelist and Crest-colour legality remain separate
  Constraints.

## Decision

- Decision: `Accepted`.
- Rationale: each surviving Action accepts the same direct command after
  subject and scheduling parameters are substituted.
- Implementation links: `ACT-130`, `ACT-182`, `ACT-191`, `ACT-220`, `ACT-123`,
  `ACT-252`, `ACT-215`, `ACT-239` and `ACT-242`.
