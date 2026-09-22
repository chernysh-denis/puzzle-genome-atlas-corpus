# Taxonomy Change 085: Isolate the clue-ordered Treasure Huntery trial

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-21
- Trigger: `GAME-0343` The Secret of Monkey Island lower-ID scan.
- Scope: three new Active genes; supporting-carrier evidence for reused genes;
  no earlier signature, lifecycle, combination or family-definition change.

## Problem

The vocabulary represented point-selected movement, addressed inventory
pickup/use/give, transactions, dialogue responses, fixed rewards, persistent
dependencies and self-paced interaction. It did not represent a carried clue
whose interpreted words are the exact ordered locomotion branches, the route
gate that accepts that sequence, or a separately completable qualification
whose retained item is proof while parallel trials remain incomplete.

## Accepted change

- `INF-365` owns the inspectable carried artefact that encodes each successive
  traversal branch without a waypoint or automatic route.
- `CON-657` owns the exact finite branch-order gate between route start and the
  concealed destination.
- `OBJ-200` owns completion of one named qualification through acquisition of
  its retained proof object, independently of parallel qualifications.

## Complete lower-ID transfer test

- `GAME-0319` Sea of Thieves compares one pictorial treasure map with a
  separate ship chart, accepts spatially tolerant digging and requires a
  shared-world chest return and sale. It does not encode successive branches or
  terminate at one trial-proof object.
- `GAME-0098` Hyperbolica has a fixed branch sequence and destination, but the
  route is not disclosed by an inspectable carried clue and its crystal is not
  proof of one parallel qualification.
- `GAME-0088` Day of the Tentacle shares addressed inventory transfer,
  prerequisite state and self-paced action, but its recipient constructs a
  device from an exact hand-in set rather than interpreting a route clue.
- `ACT-106` remains distinct because it submits directions symbolically to a
  receiver without locomotion. No lower-ID signature changes.

## Migration and compatibility

All three IDs are appended as Active definitions. English and Ukrainian
records are introduced together. Existing signatures, verified combinations
and lifecycle states remain unchanged; `GAME-0343` is the initial carrier.

## Validation expectation

Repository validation must find no exact Active-definition collision, all
three Ukrainian definitions and the complete GAME-0343 signature. The
deterministic comparison and combination scan must replace the provisional
comparison text in the game record before acceptance.
