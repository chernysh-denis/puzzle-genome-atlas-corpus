# Taxonomy Change 260: Withdraw an incompatible compound combat-HUD admission

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-10-16
- Scope: existing `INF-141`, its two admitted games and two combinations.

## Detected problem

`INF-141` requires a conjunction: upcoming combat order, current character AP,
party health/status and the selected enemy's health, Break and condition state
before a command. Its English boundary and original Clair Obscur example never
made AP or Break optional. The broader Ukrainian wording and the later
Baldur's Gate 3 admission substituted generic action resources and special
gauges for those mandatory predicates.

The historical audit
[`P2_CANONICAL_SOURCE_REVIEW_001`](../normalisation/P2_CANONICAL_SOURCE_REVIEW_001.json)
correctly identified the conflict but deferred removal because it would leave
the visible initiative queue unencoded. This correction supersedes that
deferral, not its evidence. Preserving an incompatible ID is not a valid way
to claim complete encoding of a documented disclosure.

## Evidence and transfer test

- Clair Obscur's accepted `COE-003` and `COE-007`, decomposition and transitions
  retain its visible AP-funded queue and selected-target Break state.
- Baldur's Gate 3's accepted `BG3-004`, scope and transitions describe
  initiative plus separate movement, Action, Bonus Action and Reaction
  resources. They do not establish the required AP-and-Break conjunction.
- The regional publisher's written
  [combat guide](https://www.spike-chunsoft.co.jp/pages/baldursgate3/guide2/),
  re-read 2026-10-16, separately identifies visible combat order, target and
  controlled-character state, Action/Bonus Action, movement, spell slots and
  class resources. Its controls are for PS5: this corroborates the resource
  distinction, not the exact pinned PC binary or every possible game state.
- The Divinity: Original Sin 2 record already rejects `INF-141` because its
  admitted encounter does not establish Break; `INF-343` still requires AP.
- `INF-333` deliberately withholds future order; `INF-119` and `INF-153`
  disclose different character/party state; `SYS-388` schedules turns and
  `CON-343` limits their resources. None is redefined as an initiative-display
  substitute. The earlier seven-candidate review remains a bounded scan, not
  a proof about every conceivable Information boundary.
- No video/audio playback, native gameplay, new PC-version verification or
  exhaustive claim that every BG3 state lacks every gauge is asserted.

## Decision

- Retain the complete English `INF-141` definition, type and lifecycle.
- Correct its four Ukrainian boundary fields to match AP and Break explicitly.
- Retain it in `GAME-0144` and its strict subset `COMB-0142`.
- Withdraw it from `GAME-0148` and `COMB-0146`, including the scoped card and
  salience role. Do not add a substitute, merge, split or allocate a gene.
- Keep visible initiative documented in the game source as an explicit
  representation gap. This is not a claim that BG3 hides order, or that
  scheduling and resource legality automatically encode its disclosure.
- Preserve the historical scheduling decision in `TAXONOMY_CHANGE_041` and
  adjacent-boundary decision in `TAXONOMY_CHANGE_066`. Only the former's
  incidental `INF-141` admission reference is superseded here; `SYS-388` is
  unchanged. No historical record is rewritten.

## Genome and combination impact

The BG3 genome changes from 43 to 42 genes; its interaction subset changes
from 34 to 33 and remains proper. Every other game and combination set remains
unchanged. Derived comparisons, indexes, projections and web data must be
recomputed; prior simulation is not evidence of the final current impact.
Exact current matrix differences and verification belong to
[`P2_CANONICAL_SOURCE_REVIEW_012`](../normalisation/P2_CANONICAL_SOURCE_REVIEW_012.json).
No public corpus, release mapping or production action is part of this change.
