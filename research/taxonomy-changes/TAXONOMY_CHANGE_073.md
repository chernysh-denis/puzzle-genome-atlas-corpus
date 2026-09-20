# Taxonomy Change 073: Generalise three side-scrolling transition boundaries

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-19
- Trigger: `GAME-0311` Super Mario Bros. complete lower-ID scan.
- Scope: wording and support for `SYS-064`, `INF-192` and `OBJ-164`; no earlier
  game signature, combination gene set, family membership or lifecycle change.

## Problem

Three reusable boundaries were phrased around their first carriers more narrowly
than their actual causal functions. `SYS-064` made unsafe directional contact
sound immediately disabling even when a declared avatar state absorbs it.
`INF-192` named an automatically moving icon although bounded side-view
lookahead is also decision-relevant for a directly steered body. `OBJ-164`
required an exit to be opened before it could carry one region's accumulated
state into the next, excluding a distinct fixed exit event such as World 1-1's
flagpole and castle closeout.

## Accepted change

- `SYS-064` retains top-contact defeat plus rebound, but unsafe side or underside
  contact now applies the avatar's declared penalty **or** defeat. Immediate
  death, power-state demotion and carried-item effects remain parameters.
- `INF-192` names the controlled body rather than an auto-run icon and accepts
  either automatic or directly commanded horizontal travel. It still requires
  a bounded local side-view horizon rather than full-level disclosure.
- `OBJ-164` requires satisfaction of the current region's declared exit event
  and arrival in the successor with eligible accumulated state. Opening a gate,
  charging a teleporter or contacting a flagpole are carrier parameters; merely
  reaching an uneventful location remains excluded.

## Complete lower-ID transfer test

- Braid remains a valid `SYS-064` carrier: unsafe monstar contact defeats Tim,
  which is one allowed penalty value. No signature changes.
- Geometry Dash remains a valid `INF-192` carrier: its body advances
  automatically, while Super Mario Bros. directly controls horizontal speed.
  Both expose only a bounded forward slice. No signature changes.
- Risk of Rain 2 remains a valid `OBJ-164` carrier: charging the Teleporter,
  defeating its boss and taking the opened exit is one declared exit event.
  Super Mario Bros. uses flagpole contact and scripted castle entry instead.
- `OBJ-026` remains distinct because it requires making a location traversably
  connected and does not require carrying run state into a successor region.
- `OBJ-094` remains distinct because it requires an automatically advancing,
  checkpointless Normal Mode route and does not define successor-state transfer.

## Evidence and confidence

Nintendo's preserved original manual directly states stomp and side-contact
outcomes, local side-scrolling area play, flagpole score and successor-area
structure. The pinned deterministic disassembly confirms power-state damage,
camera boundaries, flagpole capture, time conversion and area transition. The
new carrier therefore tests the causal boundaries directly rather than through
genre analogy.

## Migration and compatibility

- Stable IDs are retained.
- Only English/Ukrainian wording, carrier support and evidence links change.
- Earlier signatures, combinations and family memberships remain unchanged.
- `GAME-0311` reuses all three IDs.

## Validation expectation

- Repository validation must report no duplicate active definition.
- The lower-ID comparison must scan all 310 earlier game signatures.
- Ukrainian wording must preserve contact direction, bounded lookahead and
  successor-state carry without importing carrier-specific fiction.
