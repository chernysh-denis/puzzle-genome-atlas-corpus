# Taxonomy Change 010: Generalise mutable voxel cells to embodied tile-world cells

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-08-21
- Trigger: `GAME-0153` Terraria boundary audit against Minecraft

## Current classification

- `ACT-159`, `SYS-212` and `CON-206` encode an embodied player targeting one
  reachable mutable world cell, completing a tool-dependent break and receiving
  its eligible item drop.
- `ACT-162`, `SYS-217` and `CON-208` encode the inverse placement request,
  inventory consumption and occupancy/support legality.
- `SYS-213` encodes a seed-determined mutable world whose generated terrain and
  discoverable geography persist.
- Their current wording says `voxel`, `block` and later region instantiation,
  reflecting Minecraft's 3D chunk implementation rather than the causal rule.

## Detected problem

Terraria 1.4.5.6 supplies the same decisions in a finite side-view tile world:
the player targets one reachable foreground block, wall or placed object with a
compatible tool, receives its item form when eligible, and places carried tiles
back into supported unoccupied cells. A world seed determines terrain, biomes,
ores, caves and structures before play. Treating the side-view projection and
finite upfront generation as new genes would promote dimensionality and loading
strategy from parameters into duplicate mechanics.

## Evidence

- [`GAME-0129` — Minecraft](../../knowledge/games/m-r/minecraft.md) establishes
  embodied reach, tool/harvest rules, persistent cell mutation and seeded world
  generation in a 3D chunked instance.
- [`GAME-0153` — Terraria](../../knowledge/games/s-z/terraria.md) establishes
  the same command, legality and persistent mutation boundaries in a finite 2D
  layered tile world.
- The official Terraria placement, pickaxe and world-generation references
  cited by `GAME-0153` distinguish foreground blocks, background walls,
  furniture support, tool power and seed-selected geography.

## Change

- Generalise `ACT-159`, `SYS-212` and `CON-206` from `voxel block` to one
  reachable mutable **terrain cell**.
- Generalise `ACT-162`, `SYS-217` and `CON-208` from adjacent voxel placement to
  one compatible reachable **tile-world cell**.
- Generalise `SYS-213` to seed-determined finite or incrementally instantiated
  mutable tile worlds.
- Record dimension, projection, layer count, finite extent, generation timing,
  reach shape, tool class and support rule as parameters.
- Add Terraria as corroborating evidence and update reviewed Ukrainian labels.

## What does not change

- Abstract puzzle-board marks remain excluded because these genes require an
  embodied avatar, local reach and persistent world geometry.
- Free rigid objects, factory footprints and autonomous excavation remain in
  their existing genes.
- Minecraft and its combination retain their current signatures.
- No active gene is added, merged, deprecated or split by this change.

## Impact

- Stable and active gene counts are unchanged before the Terraria additions.
- Seven existing singleton records become recurring when `GAME-0153` is added.
- Minecraft/Terraria similarity now reflects their shared mutable-world core
  without conflating crafting, death loss, housing, time ecology or objectives.
- No earlier combination gains a new supporting game solely from wording.

## Decision

- Decision: `Accepted`.
- Decided by: repository maintainer-authorised `GAME-0153` integration.
- Rationale: 2D versus 3D and finite versus chunked generation are parameters;
  embodied reach, mutation, persistence and legality are the reusable rules.
- Implementation links: `ACT-159`, `ACT-162`, `SYS-212`, `SYS-213`, `SYS-217`,
  `CON-206`, `CON-208` and `GAME-0153`.
