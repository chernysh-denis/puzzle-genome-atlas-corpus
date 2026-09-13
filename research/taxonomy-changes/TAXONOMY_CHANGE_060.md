# Taxonomy Change 060: Restore System ownership at authored-segment boundaries

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-10
- Trigger: card `C-04` of
  [`BATCH_017_FULL_TAXONOMY_AUDIT_001`](../normalisation/BATCH_017_FULL_TAXONOMY_AUDIT_001.md),
  inherited from cards `C-17` and `C-23` of the first full taxonomy audit.
- Scope: wording-only repair of `SYS-780` and `SYS-785` plus their Ukrainian
  records; no lifecycle, signature, combination, family or carrier change.

## Confirmed boundary defect

Both System mechanics are real, but their definitions claimed work already
owned by another type:

- `SYS-780` combined the automatic retained-state transition with closing the
  current objective set and exposing segment completion. `OBJ-155` owns the
  pursued authored-segment terminal. A completion display is presentation or
  Information, not part of the state transition.
- `SYS-785` combined persistent branch-state storage with exposing that state
  in a revisitable map. `INF-308` owns the later distinction between traversed
  and unavailable paths. The stored path state can exist independently of that
  display.

The Objective/System and Information/System pairs are therefore valid typed
siblings, not merge candidates. The defect is only the System wording that
crossed their owner boundaries.

## Carrier and transfer review

`SYS-780` is carried by eight bounded authored-segment packets:

- `GAME-0249` Resident Evil 4 (2023 remake);
- `GAME-0253` Titanfall 2;
- `GAME-0257` Alien: Isolation;
- `GAME-0259` Dead Space (2023 remake);
- `GAME-0260` Metro Exodus;
- `GAME-0261` The Last of Us Part I;
- `GAME-0263` God of War; and
- `GAME-0273` Max Payne 3.

Across all eight, the System invariant begins after the scoped terminal has
settled: the resulting authored state crosses a retention boundary, ordinary
control is instantiated in the named successor and the declared retention
check can recover it. The pursued terminal, exact final interaction and any
completion message vary independently and do not belong in this System gene.

`SYS-785` is carried by `GAME-0252` Detroit: Become Human. Its invariant is the
persistent state of the nodes, edges and endpoint actually traversed by the
completed chapter, including which alternatives remain untraversed. The later
flowchart disclosure is separately represented by `INF-308`. Removing that
disclosure from `SYS-785` leaves a complete state transition.

The existing canonical game ledgers supply the evidence for every carrier.
This correction changes type ownership in no game-scoped claim and therefore
requires no fresh product, version, video or audio evidence.

## Decision

- Rename `SYS-780` to **Carry settled authored-segment state into successor
  control**. Its definition owns only retained result-state transfer,
  successor-state instantiation and recoverability through the declared
  retention check.
- Rename `SYS-785` to **Persist traversed chapter-node state across
  settlement**. Its definition owns only persistent node, edge, endpoint and
  untraversed-alternative state.
- Keep `OBJ-155` unchanged as the authored-segment terminal Objective.
- Keep `INF-308` unchanged as the branch-map disclosure.
- Do not create, merge, split, deprecate or migrate any ID.

## Corpus impact

- Canonical definitions: 2,453 → 2,453.
- Active definitions: 2,396 → 2,396.
- Inactive definitions: 57 → 57.
- Active singleton definitions: 1,759 → 1,759; singleton share remains
  `1,759 / 2,396 = 0.734140`.
- Game gene slots remain 6,179.
- Games, combinations and families remain 288, 274 and 17.
- Existing game signatures changed: `0`.
- Existing combination gene sets changed: `0`.
- Selected neighbours changed: `0`.

## Localisation disposition

- `SYS-780` and `SYS-785`: `corrected` in Ukrainian to preserve the same
  System-only ownership as the English records.
- All nine carrier-local interpretations and the Ukrainian records for
  `OBJ-155` and `INF-308`: `verified`; their meanings remain unchanged.
- Official product, chapter, mission, mode and interface names are
  `retained-with-reason` only in game-scoped evidence and examples.
- No translation work is deferred.

## Rejection condition

Reopen either wording decision only if a later carrier proves that the retained
successor state or stored traversed path cannot exist independently of the
typed terminal or disclosure. Shared timing, a common carrier, the same
chapter name or the fact that the states are later displayed is insufficient:
it does not collapse Objective, System and Information ownership.

## Change history

- 2026-09-10 — accepted as `BATCH_017_TAXONOMY_CORRECTION_004` after complete
  carrier review; wording repaired without any identifier or signature change.
