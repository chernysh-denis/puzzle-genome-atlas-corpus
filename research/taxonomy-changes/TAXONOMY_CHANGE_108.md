# Taxonomy Change 108: Contested landscape claims and terminal field scoring

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-23
- Trigger: `GAME-0369` Carcassonne, Z-Man English two-player land-tile game
  with Farmers, without River and Abbot.
- Scope: six additive Active boundaries; no earlier game signature or gene
  lifecycle is changed.

## Problem

Existing frontier placement, edge matching, random draw and group evaluation
describe the landscape, but they do not encode a second optional decision to
claim a new-tile feature with one scarce follower. They also do not express
feature-wide occupied-claim legality, later merging of separately claimed
features, majority-based completed-feature score and meeple return, or
terminal valuation of unfinished structures and farmer fields. The existing
replenishable stack ends a solo attempt; Carcassonne's unreplenished shared bag
ends with competitive final scoring, and its impossible-draw discard is not
the unconditional commitment of `CON-039`.

## Accepted change

- `ACT-503` is the optional claim action after `ACT-026` tile placement.
- `CON-669` checks the connected feature is unoccupied at claim time, but
  permits separate occupied features to join later.
- `CON-670` gates deployment by the personal reserve and releases ordinary
  followers on completion while keeping farmers deployed until the end.
- `CON-671` defines the unreplenished shared tile supply, forced impossible
  draw discard and terminal score trigger.
- `SYS-1003` allocates completed road, city and monastery points by majority
  and releases followers. `SYS-1004` separately settles incomplete features
  and distinct completed-city field adjacency at exhaustion.

## Lower-ID transfer test

- Dorfromantik's `ACT-026`, `CON-056`, `CON-058` and `SYS-034` transfer to
  Carcassonne's tile orientation, frontier, edge legality and component join.
  Its `CON-059` and `SYS-035` do not: no quest refills the physical tile bag.
- Carto's square-edge `CON-058` transfers, but Carto has no scarce feature
  claimant, majority score or field settlement.
- Azul's `SYS-004`, `INF-001`, `INF-002`, `OBJ-002` and `TIM-004` transfer
  at the random-supply, visible-state and competitive-turn boundaries; its
  private pattern-line drafting and refill rules do not.
- `CON-039` explicitly excludes discarding the current element; Carcassonne
  requires a forced discard and redraw if there is no legal placement.
- Generic occupancy and finite action allowance genes do not describe a
  follower reserve that recycles completed-feature markers while farmers stay
  committed.
- One new carrier does not establish a verified recurring combination.

## Evidence and limits

The publisher's linked English main rulesheet directly documents the
landscape, follower placement, majority/tie, completed-feature scores,
forced redraw and final-score reference. The linked supplemental rulesheet
directly documents farmers' posture, persistence, majority and three points
per adjacent completed city. No physical set, actual two-person play or exact
tile draw distribution was inspected. The local source model tests selected
rule predicates only.
