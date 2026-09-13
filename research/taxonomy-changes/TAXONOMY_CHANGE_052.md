# Taxonomy Change 052: Generalise a terminal deadline from wall time to authoritative attempt time

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-09
- Trigger: Codex integration review of `GAME-0285` The Long Dark.

## Current classification

- Stable ID: `CON-068` — Fixed attempt deadline with failure settlement.
- Prior carrier: `GAME-0025` Lemmings, where the allowance decreases in ordinary
  real time.
- Prior wording required a real-time allowance even though the decision boundary
  is the authoritative attempt clock reaching zero before completion.

## Detected problem

- The Long Dark's `Hopeless Rescue` Challenge ends unsuccessfully when its seven
  in-game-day allowance expires. Ordinary activity advances that clock and sleep
  advances it faster while control is relinquished.
- A second deadline gene distinguished only by clock implementation would make
  wall time versus simulated time a false taxonomic split.

## Evidence

- The Lemmings timer remains documented by `GAME-0025`.
- The Long Dark's route, seven-day failure and sleep-time transition are
  documented by `GAME-0285` claims `TLD-003`, `TLD-008` and `TLD-010`.
- Carrier audit: both games declare an allowance, expose its remaining value,
  advance one authoritative clock while the attempt runs, test completion
  before expiry and settle unsuccessful termination at zero.
- Counterevidence: sleep changes the rate of the in-game clock in The Long Dark;
  the generalised parameters now state the clock and rate changes explicitly.

## Change

- Replace “real-time allowance” with “authoritative time allowance”.
- Add authoritative clock and rate changes to the parameters.
- Keep elapsed performance timers, action budgets and reward-only deadlines
  outside the boundary.

## Genome and combination impact

- `CON-068` remains Active under the same ID.
- `GAME-0025` keeps its signature and interpretation.
- `GAME-0285` reuses `CON-068`; no previous signature changes.
- No combination changes are required.

## Decision

- Decision: `Accepted`.
- Rationale: the transferable choice is how much authoritative attempt time to
  spend before a hard failure, not which clock implementation decrements it.

## Ukrainian review

- The Ukrainian definition and inclusion are corrected under
  `UK-GAME-0025-0285`; the existing label already names a fixed attempt
  deadline and remains portable.

## Change history

- 2026-09-09 — accepted during `GAME-0285`; no lifecycle or signature changed.
