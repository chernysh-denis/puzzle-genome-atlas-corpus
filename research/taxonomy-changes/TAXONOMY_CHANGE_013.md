# Taxonomy Change 013: Merge duplicated automatic transitions

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-08-21
- Trigger: `REGISTRY_NORMALISATION_006` System Behaviour transfer tests

## Detected problem

Nine System records encoded the same automatic transition twice after a later
game changed its subject vocabulary. Signal propagation, staffed research,
experience conversion, persistent-world respawn, direct combat, typed ability
effects and station crafting do not become new transitions because their
targets or persistence horizon change.

## Change

- `SYS-261 → SYS-192`;
- `SYS-207 → SYS-194` and `SYS-272 → SYS-194`;
- `SYS-309 → SYS-299` and `SYS-351 → SYS-299`;
- `SYS-314 → SYS-216`;
- `SYS-252 → SYS-215`;
- `SYS-393 → SYS-380`;
- `SYS-415 → SYS-353`.

The surviving definitions are generalised to own only the shared trigger and
state consequence. Game-specific signals, research points, recipients, loss
rules, combat bodies, effect types, stations and durations become parameters.

## What does not change

- Research prerequisites and staffing eligibility remain Constraints.
- Match-local versus persistent progression remains a parameter of the scoped
  instance; account-only progression remains excluded.
- One-life elimination, recoverable currency marks and ticketed downing remain
  outside the persistent-world respawn survivor.
- Naval facing, gadget cooldown and recipe legality remain separately encoded.

## Decision

- Decision: `Accepted`.
- Rationale: every alias fails the two-way distinction test after already
  modelled parameters and Constraints are supplied.
- Implementation links: all System IDs listed under Change and their supporting
  game/combination records.
