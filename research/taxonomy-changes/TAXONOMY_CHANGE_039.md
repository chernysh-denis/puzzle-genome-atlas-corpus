# Taxonomy Change 039: Generalise continuous coverage and split its feedback

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-08
- Trigger: independent closure review of `GAME-0279` PowerWash Simulator.
- Scope: `ACT-202`, `SYS-630`, `SYS-824`, `CON-516`, `CON-619`, `INF-329`
  and new `INF-331`.
- Earlier reviewed signatures changed: none.

## Problem

The Batch 016 candidate introduced `SYS-824` and `CON-619` because PowerWash
Simulator uses a handheld stream on vehicle geometry with no material cost and
requires total accepted cleaning, whereas `SYS-630` and `CON-516` were worded
around a filled vehicle implement, an assigned field and a partial contract
threshold. Those distinctions describe carrier, target, resource and threshold
parameters. Both pairs still express the same mechanical boundaries:

1. a continuously swept applicator writes newly accepted state and progress to
   eligible surface area, while already accepted overlap adds no equivalent new
   treatment; and
2. the same bounded task cannot settle until accepted treated area reaches its
   declared threshold on the assigned target.

The candidate also treated numeric completion and spatial residual-state
location as one `INF-329` record. PowerWash exposes them through distinct
queries: overall/per-part percentages say **which component is incomplete**,
while Dirt Highlight or a selected Details item says **where its residual state
is in the world**. Either can exist without the other.

Finally, `ACT-202` named combat even though the action boundary is the direct
posture change. PowerWash supplies an independent non-combat carrier in which
crouch and prone change reachable tool angles.

## Decision

1. Generalise `ACT-202` from **Change direct-combat posture or lean** to
   **Change direct avatar posture or lean**. Collision envelope, reachable
   viewing/tool angles, body exposure and weapon handling are parameters.
2. Generalise `SYS-630` from a filled vehicle implement on a field to any
   compatible directed applicator whose footprint or stream writes persistent
   accepted surface state and task progress. Carrier and optional material
   consumption are parameters.
3. Merge candidate `SYS-824` into `SYS-630`.
4. Generalise `CON-516` from a field contract to any bounded
   surface-treatment task whose settlement requires an accepted target-coverage
   threshold. Field/object geometry, partial/total threshold and
   explicit/automatic settlement are parameters.
5. Merge candidate `CON-619` into `CON-516`.
6. Narrow `INF-329` to aggregate and per-target measured completion.
7. Add `INF-331` for the independent on-demand spatial locator of residual
   target state.

## Carrier audit

- `ACT-202` retains PUBG: BATTLEGROUNDS and Cyberpunk 2077 and adds PowerWash
  Simulator. No earlier carrier loses any included action or gains a new one.
- `SYS-630` and `CON-516` retain Farming Simulator 25 unchanged and add
  PowerWash Simulator. Farming's vehicle, field, fertilizer, partial threshold
  and explicit `Collect` remain parameters or adjacent genes (`CON-515`,
  `SYS-631`, `INF-252`, `INF-253`, `OBJ-119`).
- `SYS-824` and `CON-619` have no reviewed carrier. Their only reference was the
  PowerWash draft, so the merge changes no reviewed signature.
- `INF-329` also has no earlier reviewed carrier. Separating `INF-331` before
  promotion prevents one compound information label from becoming canonical.

## Rejected alternatives

- **Keep both coverage pairs.** Rejected because vehicle/handheld, field/object,
  consumed/unlimited and partial/total do not change either causal rule.
- **Absorb PowerWash into Farming's complete job genome.** Rejected because
  equipment borrowing, attachment, fill, offer sampling and explicit
  collection remain real Farming-only boundaries.
- **Keep numeric progress and highlight in one information gene.** Rejected
  because measurement and spatial location answer different player questions
  and use different interface actions.
- **Create a cleaning-specific posture gene.** Rejected because standing,
  crouching and prone are the same direct-body command already owned by
  `ACT-202`; the affected affordance is a parameter.

## Combination consequence

New `COMB-0271` records the strict `SYS-630 + CON-516` interaction shared by
Farming Simulator 25 and PowerWash Simulator. The relation begins when live
applicator coverage writes accepted persistent treatment and ends when the same
coverage measure enables bounded task settlement. Carrier, target, material,
threshold and collection method remain outside the combination.

## Migration

- `SYS-824`: `Active` → `Merged`, survivor `SYS-630`.
- `CON-619`: `Active` → `Merged`, survivor `CON-516`.
- PowerWash Simulator: replace those IDs, remove `ACT-341` and `TIM-002`, add
  `ACT-048`, `ACT-202`, `INF-331` and `TIM-003`.
- Farming Simulator 25: signature unchanged; add `COMB-0271` and documentation
  of the new independent carrier.
- Ukrainian registry: update the three generalised records, both merged aliases,
  corrected `INF-329` and new `INF-331` in the same unit.
- Regenerate indexes, comparison selections, research artifacts and public
  presentation before acceptance.

## Invariants

- Stable IDs remain present and auditable.
- No earlier reviewed game signature changes.
- No mission, vehicle, field, object, tool, payment or brand name enters a
  canonical label.
- `SYS-630` remains state conversion, `CON-516` remains settlement legality,
  `INF-329` remains measured disclosure and `INF-331` remains spatial
  disclosure; the types do not absorb one another.
