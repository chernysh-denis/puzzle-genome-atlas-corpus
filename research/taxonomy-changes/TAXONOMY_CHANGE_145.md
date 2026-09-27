# Taxonomy Change 145: Collectable sun and lane-bound emergency defence

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-26
- Trigger: `GAME-0407` *Plants vs. Zombies*, a regular first-stage
  daytime Adventure level of the Windows GOTY product.
- Scope: admit `ACT-546`, `ACT-547`, `SYS-1086`, `SYS-1087`,
  `SYS-1088`, `SYS-1089`, `CON-696` and `INF-403` as Active.
  Reuse `ACT-441`, `SYS-051`, `OBJ-020` and `TIM-003`; no older
  genome or verified combination changes.

## Problem and accepted change

One lane-defence purchase depends on resource tokens that must be clicked
before they expire, and on a seed packet's own recharge. A planted unit
occupies one lane cell, but can be deliberately removed with the shovel.
Zombies are introduced in a bounded sequence with flagged surges, advance
left by lane and chew blocking plants. An automatic mower clears a row only
once. The existing single-track tower-defence genes do not represent those
distinct transitions. The eight IDs isolate collection, removal, resource
production, assault release, lane attrition, one-use mower, placement legality
and disclosed decision state.

## Transfer and rejection test

- `ACT-441` transfers because the player prices and positions a persistent
  unit on a known hostile route, here an individual row; `SYS-051` covers
  the Peashooter's autonomous fire, `OBJ-020` covers clearing a finite
  assault and `TIM-003` covers uninterrupted threats.
- Bloons TD 6's `SYS-808` pays for destroyed hostile layers; PvZ's sky and
  Sunflower units require collection and are independent of zombie defeat.
  Its `SYS-809` advances player-triggered numbered rounds on one track,
  while this level releases increasingly large flagged waves across rows.
  Its `OBJ-159` permits a stock-cost leak; house breach here is terminal
  after a one-use mower, so `OBJ-020` is the accurate reuse.
- `ACT-122` requires held extraction and material entering inventory;
  shovelling a plant does neither. A named plant, sun amount, exact spawn
  minute or lane count is a parameter, not a separate gene.
- Night, pool, fog, roof, extra modes and unplayed packet types are outside
  this bounded daytime route. No older signature is retrofitted.

## Evidence and limits

- [PopCap's public readme](https://akamai.cdn.ea.com/eadownloads/u/f/manuals/GAME-PVZ/en_US_readme.html)
  directly documents sun collection and expiry, seed recharge, shovel,
  staged waves, zombie feeding, lawnmowers and level terminals.
- [PopCap's Windows Steam listing](https://store.steampowered.com/app/3590/Plants_vs_Zombies_GOTY_Edition/)
  identifies the selected PC product and its distinct Adventure mode.
- The public readme labels its own build as Mac `1.0.40`; the selected
  Windows GOTY executable and exact level `1-6` roster were not run. Core
  rules transfer is bounded, not a claim of binary equivalence.
