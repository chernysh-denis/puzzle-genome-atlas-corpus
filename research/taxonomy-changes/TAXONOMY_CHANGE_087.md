# Taxonomy Change 087: Bound one light-gun target-quota round

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-21
- Trigger: `GAME-0345` Duck Hunt complete lower-ID transfer test.
- Scope: seven new Active boundaries and supporting-carrier evidence for three
  reused genes; no earlier signature, lifecycle, combination or family change.

## Problem

The vocabulary already represented software-aimed combat, finite projectile
stocks, autonomous movement, live input, score maximisation and several kinds
of quota. It did not represent a physical light-sensing gun whose spatial
request is mediated by the displayed light response, nor a fixed round made of
separate moving-target opportunities that each close on a hit, three misses or
their own timeout and finally settle against a minimum hit count.

Reusing ordinary attack and ammunition genes would erase the device/display
causal loop. Reusing rescue, collection or score-threshold objectives would
also misstate the PASS LINE: the round accepts six of ten separately expiring
targets regardless of their point values.

## Accepted change

- `ACT-490` owns physical display-directed Zapper aim and trigger.
- `SYS-967` owns darkness/target-light sampling into hit or miss without
  claiming undocumented pixel or scanline constants.
- `SYS-968` owns the one-at-a-time moving-target schedule and its hit/escape
  successor transition.
- `SYS-969` owns target-class hit score and the no-miss round bonus.
- `CON-658` owns the per-target three-shot and independent live-duration cap.
- `INF-366` owns the joined moving target, shots, hit row, PASS LINE, round and
  score surface.
- `OBJ-202` owns the minimum hit count across a fixed target schedule.
- `SYS-045`, `OBJ-002` and `TIM-003` receive Duck Hunt support without a
  wording change.

## Complete lower-ID transfer test

- `ACT-161` aims a simulated current combat tool at a hostile or breakable
  world object. Duck Hunt receives screen direction through an external
  photosensor/display loop, so neither the action nor adjudication transfers.
- `CON-164` spends a finite physical projectile stock across an attempt.
  Duck Hunt refreshes three trigger opportunities for every new duck and also
  closes them by time, so the stock boundary does not transfer.
- `OBJ-019` rescues a minimum population through an exit and `OBJ-160` fills a
  delivery quota before boarding transport. Neither covers counted hit
  outcomes across independent expiring opportunities.
- `OBJ-013` reaches a score within an action budget, but Duck Hunt qualification
  is by six hit lamps rather than score; `OBJ-002` remains as the separate
  optional score motive.
- `SYS-045` transfers for autonomous live duck flight, `TIM-003` transfers for
  input while position/time advance, and `OBJ-002` transfers for round score.

## Migration and compatibility

All seven boundaries append as Active. No existing definition or signature is
broadened. English and Ukrainian records are introduced together. No verified
combination is added.

## Validation expectation

Repository validation must find no exact Active-definition collision, complete
Ukrainian coverage, a ten-gene `GAME-0345` signature, unchanged lower-ID
signatures and deterministic comparison/combination results. The executable
control must cover quota advance, below-quota Game Over, third-shot and timeout
misses, class scoring and PERFECT settlement.
