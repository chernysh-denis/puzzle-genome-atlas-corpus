# Taxonomy Change 093: Isolate mounted ingestion and temporary object exchange

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: `2026-09-22`
- Trigger: `GAME-0354` Super Mario World complete lower-ID transfer test.
- Scope: six new Active boundaries and supporting-carrier evidence for twenty-
  one reused movement, block, power, checkpoint, reward, information,
  objective and time boundaries.

## Problem

The vocabulary represented direct platform movement, mounting, portable
objects, mutable reward blocks, temporary avatar power, finite lives,
checkpoints, collectible milestones and stage settlement. It did not represent
the coupled Yoshi's Island 2 rule chain: a player-commanded mount mouth with
exclusive body occupancy, body-type-dependent release, recoverable separation
after harm, a consumed-berry reward threshold, or the P-Switch's timed exchange
between collectible and solid world-object classes.

## Accepted change

- Add `ACT-493` for commanding a mounted companion to ingest or expel one
  eligible world body.
- Add `SYS-978` for mapping one mouth-held body's type and timing to its mounted
  emitted, expelled or swallowed result.
- Add `SYS-979` for harmful contact that separates rider and companion into a
  recoverable chase state.
- Add `SYS-980` for an eligible mount-consumed forage threshold that emits a
  world reward.
- Add `SYS-981` for a bounded switch interval that exchanges authored coin and
  solid-block classes before restoration.
- Add `CON-660` for reach, target eligibility and exclusive mouth occupancy.

## Complete lower-ID transfer test

- `ACT-048` directly carries and throws one portable world object, but does not
  command a companion's ingestion apparatus or its exclusive mouth slot.
- `ACT-348` owns mount, direct riding and voluntary dismount, not a separate
  mounted-object command.
- `SYS-037` collects eligible objects into ordinary state; it does not retain a
  world body in the companion or branch by that body's type.
- Existing projectile, element and ammunition systems resolve attacks after
  creation but do not derive three fireballs, a returned shell or swallowing
  from one mouth-held body's type and timer.
- Existing armour, shield, vehicle and mount-loss systems spend protection,
  destroy a carrier or voluntarily dismount; none turns harm into a separately
  moving recoverable companion.
- `SYS-935` converts a route-collectible milestone into a finite life and is
  reused for five Dragon Coins. It does not own active companion feeding whose
  threshold emits a different world reward.
- Existing switch, door, tile and transform rules change one fixture, actor or
  authored region. None reversibly exchanges many instances of two world-
  object classes and changes both collision and collectibility for a timer.
- Existing capacity and action-state constraints do not bind a spatial tongue
  target to one exclusive transient mouth-held body.

## Migration and validation expectation

Append six Active IDs and complete reviewed Ukrainian coverage. Existing IDs,
lifecycle states, earlier signatures, combinations and family definitions
remain unchanged. Validation must find a twenty-seven-gene `GAME-0354`
signature and an executable reconstruction covering mount acquisition, ten
berries, red/green shell results, recoverable separation, five Dragon Coins,
Midway return, Grab Block handling, P-Switch exchange/restoration and mounted
Goal Tape settlement.
