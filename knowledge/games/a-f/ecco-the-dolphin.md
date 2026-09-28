---
game_id: GAME-0433
slug: ecco-the-dolphin
game_title: Ecco the Dolphin
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-571
  system:
    - SYS-543
    - SYS-1137
  constraint:
    - CON-460
  information:
    - INF-075
    - INF-422
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Ecco the Dolphin — breath, sonar and a matching-glyph passage

Use the [canonical vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Swimming direction, breath capacity and the identities of two crystals are parameters of one bounded route, not separate genes.

## Analysis scope

- Version / ruleset: original English Sega Genesis cartridge rules, not the later 3DS *3D Ecco the Dolphin* port. Exact cartridge revision and region-specific difficulty values were not inspected.
- Structured analysis target: `PLAT-SEGA-GENESIS` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: steer Ecco through the Bay of Medusa's connected water, inspect the reachable region with a held sonar song, plan dives around the continuously draining breath meter and refill at surface or air pockets, contact the key glyph to gain its song, then direct that song at the compatible barrier glyph and swim through the released passage.
- Entry: after the opening Home Bay storm, Ecco enters Bay of Medusa with ordinary health and a breathable route available. The storm's cause and exact opening positions are narrative context, not this packet's mechanics.
- Positive terminal / evaluation: Ecco passes the opened barrier and reaches the transition into Undercaves. This is a stage passage, not completion of the full game or rescue of the pod.
- Negative state: staying submerged after breath expires ends the attempt and restarts the level; hostile contact can also cause harm. This packet follows a survivable route and does not model combat or healing choices that are not required to show the sonar–air–glyph dependency.
- Included: direct swimming and leaps to breathable air, the live breath meter and refill, requested directional echolocation map, key-glyph contact, learned matching song, barrier response, and stage exit under real-time progression.
- Excluded: exact breath duration, enemy damage values, fish and healing-clam decisions, movable boulders beyond route obstacles, later rescue/whale/time-travel stages, passwords, 3DS save-anywhere and Super Dolphin invincibility or unlimited breath.
- Reproducible parameterisation: select original English Genesis rules; after Home Bay storm, enter Bay of Medusa; sing while facing several directions to expose local rock, air and glyph features; use a reachable air pocket before breath runs out; contact the key glyph; return to the matching barrier, emit the newly acquired song and traverse to Undercaves. Route details are reconstructed from the original manual plus an independent first-hand written guide, not from direct play.
- Potential scoped modules: enemy combat and health recovery, moving rocks and currents, later distinct glyph powers and passwords require separate records.
- Direct-play status: no Genesis console, cartridge binary, controller trace, save, screenshot, video or audio was inspected. The Sega-hosted original booklet establishes controls, meters and glyph classes. Sega's later original-game explanation clarifies key-crystal contact and matching gate song; a first-hand written route supports the Bay of Medusa to Undercaves sequence. The latter two do not establish cartridge revision or measured timing.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ECC-001` | Directional swimming, an A-button song and held-song echolocation are available in original Genesis play. | Confirmed | Direct | High | P1 pp. 5, 8 |
| `ECC-002` | Submerged breath drains; surface and air pockets restore it, while exhaustion ends the attempt. | Confirmed | Direct | High | P1 pp. 6–7 |
| `ECC-003` | The sonar map distinguishes local rock paths, danger, glyphs and air pockets but must be requested by song. | Confirmed | Direct | High | P1 p. 8 |
| `ECC-004` | A key glyph grants a song; the matching song can release a barrier glyph that otherwise blocks the route. | Confirmed | Corroborated | High | P1 p. 8, P2 |
| `ECC-005` | The first Bay of Medusa route links an air pocket, key glyph and exit toward Undercaves. | Observation | Corroborated | Medium | S1, P1 pp. 7–8 |

## Basic data

- Release / origin: Ed Annunziata's *Ecco the Dolphin*, published by Sega for Genesis. The exact cartridge revision is unverified.
- Platform or physical form: original English Sega Genesis cartridge; the later 3DS port is used only as a clearly separated explanatory source, not as the analysed build.
- Mechanical families: real-time system pressure (`FAM-010`) through the breath-limited live dive; ordered dependency sequencing (`FAM-017`) through key-glyph song before matching barrier passage.
- Primary source **P1**: [Sega-hosted original Genesis manual](https://manuals.sega.com/genesismini/pdf/ECCO_THE_DOLPHIN.pdf), especially pp. 5–8 (accessed 2026-09-27). **P2**: [Sega's 3D Ecco product explanation](https://archives.sega.jp/3d/ecco/) (accessed 2026-09-27), which describes the original key-crystal/gate-crystal relation but separately lists later portable features excluded here.
- First-hand route **S1**: [Ecco the Dolphin Genesis written walkthrough](https://gamefaqs.gamespot.com/genesis/563323-ecco-the-dolphin/faqs/31465), Bay of Medusa sequence (accessed 2026-09-27). Its route is used as bounded corroboration, not a claim of our own witnessed play.
- Claim IDs: `ECC-001`–`ECC-005`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for direct swimming and jumping across connected water/air geometry. Add `ACT-571` for a player-emitted directional song: a short pulse can address a glyph, and a held pulse returning to Ecco opens his local map (`ECC-001`, `ECC-003`).

### System Behaviour Genes

- Reuse `SYS-543` for continuous breath depletion under water and refill at a breathable surface or air pocket. Add `SYS-1137` for key-glyph contact granting a song that releases the matching barrier when sung toward it. The key is knowledge/capability, not a consumed carried object (`ECC-002`, `ECC-004`).

### Constraint Genes

- Reuse `CON-460`: an underwater leg must reach air before breath exhaustion. The route also has an authored matching-song dependency represented by `SYS-1137`, not a generic inventory-key constraint (`ECC-002`, `ECC-004`).

### Information Genes

- Reuse `INF-075` for the currently visible breath/survival meter. Add `INF-422` for the requested returned-echo map of nearby rock, glyph, air and danger features; it is neither a whole-stage reveal nor a route solution (`ECC-002`, `ECC-003`).

### Objective Genes

- Reuse `OBJ-026`: reach the designated Undercaves transition after the barrier makes the passage traversable (`ECC-005`).

### Time Genes

- Reuse `TIM-003`: breath and environmental danger continue to advance while movement and song inputs are available. The sonar map is a requested view; no claim that it pauses breath is made (`ECC-001`, `ECC-002`).

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Ecco is submerged with breath remaining | Swim away from a breathable place | Breath declines while the route continues; exhaustion ends the attempt | live air budget | `ECC-002` |
| Ecco can reach an air pocket | Swim into breathable air | Breath refills, allowing another underwater leg | spatial replenishment | `ECC-002` |
| The next cavern remains unknown | Hold song while facing the passage | Returned echo gives a bounded map including air, rocks and glyph marks | active partial spatial information | `ECC-001`, `ECC-003` |
| The matching barrier remains closed | Contact its key glyph | Ecco learns the corresponding song, without consuming a physical key | capability prerequisite | `ECC-004` |
| Ecco has the song and faces the barrier | Sing the learned song, then swim onward | Matching barrier yields; the route to Undercaves becomes passable | ordered song gate and local exit | `ECC-004`, `ECC-005` |

## Strategic and experiential structure

- Local decision: compare breath remaining with the next reachable air pocket before choosing a dive and sonar direction.
- Medium-term planning: explore to learn the key song and reserve enough air for the return to its matching barrier.
- Long-term structure: this packet stops at Undercaves entry; later crystal abilities are outside scope.
- Failure attribution: breath exhaustion is visible and tied to route timing; the barrier's unmatched-song rejection signals a missing prerequisite, not arbitrary collision.
- Player-trust factor: the echo shows useful categories but does not reveal an entire safe path or exact remaining travel time.

## Replay and variation

The authored cavern, glyph relation and destination do not become a procedurally generated board. Different swim lines and sonar requests alter the player's available information and breath margin. No unverified random spawn or exact speed advantage is needed to explain this route.

## Adjacent systems and history

*Subnautica* (`GAME-0178`) shares spatial air budgeting, but its first submersible/habitat construction differs from Ecco's acquired acoustic gate song. *Chants of Sennaar* (`GAME-0055`) uses glyph interpretation for a linguistic puzzle; Ecco's learned crystal song is a capability lock, not player-entered translation.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-571` | swim/leap and directional/held song |
| System Behaviour | `SYS-543`, `SYS-1137` | breath refill and matching learned-song gate |
| Constraint | `CON-460` | reachable air before exhaustion |
| Information | `INF-075`, `INF-422` | visible breath and requested local echo |
| Objective | `OBJ-026` | Undercaves transition |
| Time | `TIM-003` | continuously advancing dive |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `432` (`GAME-0001`–`GAME-0432`).
- Exact genome matches: none.
- Tied near matches: `GAME-0098` — Hyperbolica (`3 / 13 = 0.230769`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0098` *Hyperbolica* | `ACT-008`, `OBJ-026`, `TIM-003` cover direct navigation toward a traversable destination under a continuing world clock. | Hyperbolica asks the player to reason about authored curved-space adjacency and curvature cues; Ecco manages a live breath budget, requests sonar, learns a crystal song and opens a matched acoustic gate. The shared three genes do not equate their geometry or information. | Sole tied-near maximum, `0.230769`; not an exact or verified-combination match. |

## Taxonomy impact

Three typed boundaries (`ACT-571`, `SYS-1137`, `INF-422`) separate player-issued sonar/song, learned acoustic gate resolution and returned-echo spatial information. See `TAXONOMY_CHANGE_170`. No earlier signature or verified combination changes.

## Negative results

- `ACT-471` scans terrain and cargo with an Odradek but does not address a compatible glyph or use returned acoustic information.
- `SYS-063` consumes a carried physical key; Ecco learns and emits a matching song.
- `INF-001` would falsely imply the whole cavern state is already visible. Ecco must request a direction-bounded echo.
- The later 3DS Super Dolphin mode removes breath pressure and is incompatible with this original Genesis packet.

## Delta summary

## New facts

- [Confirmed | Direct | High] Breath refills at air pockets, and a held song returns a local map (`ECC-002`, `ECC-003`).
- [Confirmed | Corroborated | High] Contact with a key glyph grants a song capable of releasing its matching barrier (`ECC-004`).

## New genes

- [Confirmed | Corroborated | High] Three new boundaries in `TAXONOMY_CHANGE_170`.

## New combinations

- [Observation | Corroborated | Medium] No new verified combination proposed.

## Taxonomy changes

- [Confirmed | Corroborated | High] `TAXONOMY_CHANGE_170`; prior signatures unchanged.

## New questions

- What exact Genesis revision, breath durations and barrier-trigger timing would a direct cartridge trace establish?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0434` *Cooking Mama*, original Nintendo DS context.
- Optimisation criterion: alternate an underwater real-time route with stylus-driven recipe steps.
- Expected information gain: distinguish directly performed touch gestures, step assessment and recipe-level settlement.
- Backlog impact: retain the approved 433–441 order; begin the next unit only after the Goal stop window.

## Why this game

- [Hypothesis | Limited | Medium] The bounded Genesis opening tests whether breath, actively requested echolocation and a learned acoustic gate can be separated without conflating them with generic collection keys or modern port conveniences.
