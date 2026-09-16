# Taxonomy Change 068: Generalise close-weapon field maintenance

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-13
- Trigger: `GAME-0290` Lies of P complete lower-ID Action and System scan.
- Scope: `ACT-378`, `SYS-688`, their two carrier records and Ukrainian labels;
  no game signature, combination gene set or lifecycle changes.

## Current classification

`ACT-378` and `SYS-688` were introduced for Monster Hunter: World's reusable
whetstone loop. Their labels and definitions named `sharpness`, while the actual
boundaries already separated three transferable responsibilities: a player
commits exposed field maintenance with a reusable tool; ordinary close-weapon
use degrades one cycling performance gauge; and completing maintenance restores
that gauge without replacing or upgrading the weapon.

Lies of P exposes the same responsibilities under the labels `Durability` and
`Grinder`. Attacks and guards reduce the current gauge, low or zero state
changes combat performance, the reusable Grinder restores positive durability
during live control, and Stargazer rest supplies a carrier-specific zero-state
repair. Treating the product label as a new gene would duplicate the shared
decision.

## Complete lower-ID and transfer scan

All 377 lower-ID Active Action definitions preceding `ACT-378` and all 687
lower-ID Active System definitions preceding `SYS-688` were checked.

- `ACT-221` requires a safe-hub selection and resource payment to repair or
  upgrade a retained weapon, which neither reusable live maintenance action
  performs.
- `ACT-200` covers a finite or replenishable restorative/repair cast but does
  not own the weapon-specific reusable maintenance command or its cycling
  performance gauge.
- `SYS-656` binds match-local Durability to a finite Weapon Repair Kit and a
  different zero-state consequence. Its supply-and-repair economy is not the
  reusable whetstone/Grinder loop.
- `SYS-777` owns a timed parry that debits the defender's close-weapon
  durability; it does not own general degradation, restoration or the reusable
  maintenance command.
- `CON-286` may govern whether an individual repair cast completes, and
  `CON-354` may govern whether a weapon move is legal. Neither is the command
  or state transition itself.

The two carriers vary weapon, gauge label, degrading event, low/zero effect,
restoration rate, checkpoint recovery, timing and route context while retaining
the same action and state transition. They therefore pass the two-carrier
transfer test.

## Decision

- Rename `ACT-378` to **Maintain the equipped close-range weapon in the field**
  and generalise its wording from a whetstone/sharpness pair to one reusable
  live maintenance action and a cycling sharpness-or-durability gauge.
- Rename `SYS-688` to **Degrade and restore a close-range weapon maintenance
  gauge** and admit attack, guard or declared combat-effect degradation plus a
  carrier-specific zero-state exception.
- Add Lies of P as the second carrier of both genes.
- Preserve Monster Hunter: World's existing signature and evidence. Preserve
  every other game, combination and lifecycle unchanged.

## Genome, combination and comparison impact

- `GAME-0207` retains `ACT-378` and `SYS-688` with no signature change.
- `GAME-0290` reuses both owners in its thirty-six-gene signature.
- `COMB-0205` retains its existing gene set and sole carrier.
- `COMB-0260` gains Lies of P as a second carrier because of the new game's
  separate stamina, checkpoint-mark and guardian substrate; the maintenance
  genes are deliberately outside that twenty-gene combination.
- DARK SOULS III remains the selected lower-ID neighbour for Lies of P at
  `23 / 39 = 0.589744`. No earlier selected neighbour changes.

## Corpus accounting

- Canonical and Active definition counts remain 2,458 and 2,400.
- Games increase from 289 to 290.
- Active game-gene usages increase by the complete thirty-six-gene Lies of P
  signature; no existing usage is added or removed.
- Both `ACT-378` and `SYS-688` increase from one to two carriers. Their former
  singleton status is removed without creating a new definition.
- Combinations and families remain 274 and 17; `COMB-0260` becomes recurrent.

## Localisation disposition

- `ACT-378` and `SYS-688`: `corrected` in Ukrainian to preserve the
  product-neutral maintenance boundary and both carriers.
- `GAME-0207`, `COMB-0205` and their unchanged Ukrainian presentation:
  `verified`; no text needs rewriting because the carrier-local sharpness
  statements remain accurate.
- `GAME-0290`, recurrent `COMB-0260`, metadata, salience, plain-language and web
  presentation: `corrected` in the game unit.
- Monster Hunter: World, Hunter's Knife I, whetstone, Lies of P, Durability,
  Grinder and Stargazer are `retained-with-reason` only as official product or
  interface names and evidence examples.

## Rejection condition

Reopen this generalisation only if a later carrier proves that the current
`sharpness` and `Durability` gauges cannot vary as parameters while preserving
reusable exposed field maintenance, use-driven cycling degradation and
non-upgrade restoration. A different label, animation, tool appearance,
degradation rate or zero-state exception alone is insufficient.

## Change history

- 2026-09-13 — accepted with `GAME-0290` after a complete lower-ID scan and
  two-carrier transfer test; no prior signature changed.
