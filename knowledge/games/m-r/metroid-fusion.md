---
game_id: GAME-0474
slug: metroid-fusion
game_title: Metroid Fusion
analysis_status: reviewed
reviewed: 2026-10-02
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-202
  system:
    - SYS-045
    - SYS-215
    - SYS-398
    - SYS-578
    - SYS-1234
  constraint:
    - CON-282
    - CON-349
    - CON-578
  information:
    - INF-073
    - INF-119
    - INF-125
  objective:
    - OBJ-198
  time:
    - TIM-003
---

# Game: Metroid Fusion — first BSL station mission

Use the [canonical genome vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Samus, Adam, the BSL station, X parasites, Arachnus and Morph Ball are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: original English *Metroid Fusion* for Game Boy Advance, single-player New Game, from the first Docking Bays mission briefing through the first return to a Main Deck Navigation Room after recovering Morph Ball. This is not *Super Metroid*, a later Virtual Console or Nintendo Switch Online wrapper, a randomizer, an item-percentage run or the subsequent Sector 1 mission. Exact cartridge revision and regional variation were not inspected.
- Structured analysis target: original licensed GBA cartridge; see `GAME-0474` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: Samus reaches the BSL station with most former abilities unavailable. The computer marks Quarantine Bay as the first objective. No Missile data has been downloaded, Arachnus has not been defeated and Morph Ball is unavailable.
- Bounded route: uplink at Navigation Room 1, inspect Quarantine Bay and return to report; follow the opened level-0 route to Navigation Room 2; travel to Operations Deck and download Missile data; after the Main Deck elevators fail, find the alternate route, spend missiles to remove the compatible obstruction and reach Arachnus; defeat Arachnus, break the exposed Core-X with missiles, touch the parasite to regain Morph Ball; roll through the narrow exit and return to the Main Deck Navigation Room for the next objective. Optional Missile/Energy Tanks, Save Rooms and Recharge Rooms may help but are not counted as mandatory acquisitions.
- Primary decision loop: read the current objective and explored map, traverse visible connected rooms, fire the beam or spend finite missiles against legal targets, manage Energy while enemies act in real time, absorb eligible free X to recover resources, then use the newly restored compact form to cross a previously inaccessible passage.
- Positive terminal: Morph Ball is recovered from Arachnus's Core-X, the narrow exit is crossed in compact form, and Samus reaches the Main Deck Navigation Room with the ability retained. The later Sector 1 briefing is a boundary marker, not part of the analysed mission.
- Failure/recovery: Energy reaching zero ends the attempt; compatible free X or a Recharge Room can replenish missing Energy or missile supply. The packet does not assert a fixed time limit, an exact boss hit count, a particular optional tank inventory or a demonstrated save-reload trace.
- Included: direct side-view running/jumping/crouching; beam and missile fire; finite missiles and one Energy pool; the map and mission marker; Navigation/Data Room use; level-0 hatch release; authored elevator outage and alternate route; X parasite absorption; Arachnus and its Core-X; retained Morph Ball and narrow-passage return.
- Excluded: Sector 1 stabilisers, later SA-X encounters, Bombs, High Jump, Varia Suit, Ice/Super/Diffusion Missiles, Power Bombs, later bosses, endings, time/percentage rankings, sequence breaks and wrapper features. No Bomb placement is available in the bounded route even though Morph Ball is recovered.
- Direct-play status: no cartridge, emulator, executable, controller trace, screenshot, video or audio gameplay was inspected. The official Nintendo manual establishes controls and general rules; its broad ability list is not evidence that every ability is initially available. A written game script and contemporary route establish this mission order. The image is original illustrative artwork, not game capture.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MF-001` | The original GBA release is the target, not a later wrapper | Confirmed | Direct | High | P1, P2 |
| `MF-002` | The opening directs Samus to Quarantine Bay via Navigation Room and later marks bio-signs as the next Main Deck target | Observation | Corroborated | High | P2, S1, S2 |
| `MF-003` | The Navigation Room objective and explored map are inspectable, while undiscovered rooms remain hidden | Confirmed | Direct | High | P2 |
| `MF-004` | Data Room download restores Missiles before the elevator-outage alternate route and Arachnus encounter | Observation | Corroborated | High | P2, S1, S2 |
| `MF-005` | Firing a Missile spends a finite reserve; a Recharge Room or eligible free X can restore it | Confirmed | Direct | High | P2, S1 |
| `MF-006` | Hostile defeat can release free X, and eligible contact with it restores resources instead of treating it as a conventional carried item | Confirmed | Direct | High | P2, S1 |
| `MF-007` | Arachnus's exposed Core-X must be broken with Missiles, and absorption restores Morph Ball | Observation | Corroborated | High | P2, S1, S2 |
| `MF-008` | Recovered Morph Ball changes Samus's posture and enables the narrow return passage | Confirmed | Direct | High | P2, S1 |
| `MF-009` | Morph Ball recovery alone is not the packet's terminal; reaching the Main Deck Navigation Room closes this first route | Observation | Corroborated | Medium | S1, S2 |
| `MF-010` | Later SA-X, Bomb and sector mechanics are not available on this bounded route | Observation | Corroborated | High | P2, S1, S2 |

## Basic data

- Release/origin: Nintendo R&D1 and Nintendo, 2002, Game Boy Advance. Nintendo's current archive also lists later access platforms; they are not this ruleset.
- **P1**: [Nintendo's Metroid Fusion product archive](https://www.nintendo.com/en-gb/Games/Game-Boy-Advance/Metroid-Fusion-267046.html), original GBA identity and release, checked 2026-10-02.
- **P2**: [Nintendo's original multilingual GBA manual](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/game_boy_advance_8/Manual_GameBoyAdvance_MetroidFusion_EN_DE_FR_ES_IT.pdf), English printed pp. 8–25. It documents side-view controls, missile input, Navigation/Data Rooms, map disclosure, Energy and missile HUD, free-X and Core-X absorption, Morph Ball, hatches and enemy descriptions. The manual is a scan; the relevant pages were visually inspected rather than relying on empty text extraction.
- **S1**: [ultrasilver64's contemporary GBA walkthrough](https://gamefaqs.gamespot.com/gba/516709-metroid-fusion/faqs/20245), Quarantine Bay and first infestation/missile route, checked 2026-10-02.
- **S2**: [mtkennerly's game-script transcription](https://gamefaqs.gamespot.com/gba/516709-metroid-fusion/faqs/77034/main-area-visit-1), opening Main Deck objectives, Data Room and Morph Ball recovery order, checked 2026-10-02. It is independent transcription, not publisher documentation.
- Evidence limit: P2 describes the overall game, while S1/S2 bound the exact opening sequence. None is a direct-play measurement by this project. Exact initial missile count, damage values, boss vulnerability timing and cartridge-revision parity remain unverified.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly move Samus through connected side-view rooms, jumping and climbing along the first station route (`MF-002`, `MF-008`).
- `ACT-161`: aim and fire beam or, after the download, compatible Missiles at a hostile, obstruction or exposed Core-X (`MF-004`, `MF-007`).
- `ACT-202`: after the Core-X recovery, press down twice to change into Morph Ball posture and traverse low clearance (`MF-008`). No Bomb command is included.

### System Behaviour Genes

- `SYS-045`: ordinary infected hosts continue to act in the local room without a player order (`MF-006`).
- `SYS-215`: beam, missile, hostile and Arachnus attacks resolve during live room traversal (`MF-005`, `MF-007`).
- `SYS-398`: absorbing the first Core-X permanently restores Morph Ball for compatible later passages in this save (`MF-007`, `MF-008`).
- `SYS-578`: hostile damage reduces Energy, eligible recovery restores it to its cap and zero ends the attempt (`MF-005`, `MF-006`).
- New `SYS-1234`: an infected host's defeat exposes free X; ordinary compatible absorption restores the relevant reserve, whereas breaking and absorbing the first boss Core-X restores the particular lost ability. The X is not a generic inventory stack (`MF-006`, `MF-007`).
- Resolution order: current objective/map, direct movement and attack, hostile hit or drop, resource settlement, authored route-state change, Core-X recovery, retained compact traversal and Navigation Room return.

### Constraint Genes

- `CON-282`: Quarantine report, level-0 release, Missile download, alternate route, Arachnus/Core-X and return are authored prerequisites rather than freely reorderable destinations (`MF-002`, `MF-004`, `MF-007`, `MF-009`).
- `CON-349`: the narrow return edge accepts Samus only after Morph Ball has been recovered and selected at that passage (`MF-008`). The missile-compatible obstruction similarly requires a downloaded weapon and available reserve.
- `CON-578`: each Missile shot requires remaining compatible supply; ordinary beam fire is not billed to that reserve (`MF-005`).

### Information Genes

- `INF-073`: the HUD shows current Missile reserve before spending a shot (`MF-005`).
- `INF-119`: Energy and newly available equipment are inspectable before combat and route choices (`MF-003`, `MF-008`).
- `INF-125`: the pause map and Navigation Rooms expose current position, explored topology and the selected mission target, but do not reveal the whole station (`MF-002`, `MF-003`).

### Objective and Time Genes

- `OBJ-198`: complete the acquired-capability return: obtain Missiles, recover Morph Ball from the Core-X, use the compact passage and report at the earlier Main Deck Navigation Room (`MF-004`, `MF-007`–`MF-009`). Unlike Super Metroid's first Bombs route, Bombs are not part of this instance.
- `TIM-003`: room movement, projectiles and enemies resolve in real time; no mission-wide countdown is evidenced (`MF-005`, `MF-007`).

## Reproducible transitions

| Before | Player action | Bounded resolution | Claim |
|---|---|---|---|
| Quarantine Bay objective is marked | Travel via Navigation Room, defeat the local infected host and return | Report opens the next infestation target and level-0 route | `MF-002`, `MF-006` |
| Missile capability is absent | Follow the indicated Operations Deck route and enter Data Room | Missile data is downloaded; holding R and firing B is now legal | `MF-004`, `MF-005` |
| Main Deck elevators fail after download | Inspect the new route, spend eligible Missiles and descend | Alternate path reaches the first guardian and Arachnus | `MF-004`, `MF-005` |
| An infected host falls and a compatible free X remains | Touch the free X | Eligible Energy or ammunition recovery settles, subject to maximum | `MF-006` |
| Arachnus is defeated and its Core-X is exposed | Hit the Core-X with Missiles, then contact it | The parasite is absorbed and Morph Ball is retained | `MF-007` |
| The earlier narrow passage remains impassable upright | Enter Morph Ball posture and roll through | The return edge becomes traversable; Navigation Room return closes the packet | `MF-008`, `MF-009` |

## Strategic and experiential structure

The mission combines computer-directed objectives with locally chosen combat, recovery and optional side pickups. It is not an open-ended item-hunt or a fixed timed escape. The station's map and hatches guide the route, but the player still has to acquire the correct capability and spend resources in live rooms. General X absorption and boss Core-X restoration share a source carrier yet have distinct outcomes.

## Replay and variation

Optional tanks, save use, precise damage and X drops can vary without altering the ordered terminal. No random room graph or fixed repeated X-drop sequence is asserted. To reproduce one trace, pin original cartridge revision, first-mission entry state, route, damage, resource supply and input timing.

## Adjacent systems and history

*Super Metroid* (`GAME-0337`) also couples Morph Ball with authored low passages, but its bounded Ceres-to-Bombs packet includes an escape timer, a five-missile red door and reusable Bombs; this Fusion packet instead begins with a computer objective, downloads Missiles, has an elevator outage and recovers Morph Ball from a boss's X. *Metroid Prime* (`GAME-0355`) shares live Samus combat and a map but has first-person visor scanning and a separate timed Frigate escape. No earlier whole-game Metroid signature is copied into this first-mission packet.

## Normalised genome

| Type | Active IDs | Scoped role |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-202` | move, attack, change posture |
| System | `SYS-045`, `SYS-215`, `SYS-398`, `SYS-578`, `SYS-1234` | live hosts, combat, retained ability, Energy, X outcomes |
| Constraint | `CON-282`, `CON-349`, `CON-578` | ordered mission, capability edge, finite missiles |
| Information | `INF-073`, `INF-119`, `INF-125` | missile/Energy/equipment and mission map |
| Objective | `OBJ-198` | restored-capability return |
| Time | `TIM-003` | live room time |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `473` (`GAME-0001`–`GAME-0473`).
- Exact genome matches: none.
- Tied near matches: `GAME-0337` — Super Metroid (`14 / 23 = 0.608696`).
- Supported combination subsets: none.
- Scan date: 2026-10-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0337` — Super Metroid | `ACT-008`, `ACT-161`, `ACT-202`, `SYS-215`, `SYS-398`, `SYS-578`, `CON-282`, `CON-349`, `CON-578`, `INF-073`, `INF-119`, `INF-125`, `OBJ-198`, `TIM-003` | Both packets combine direct Samus movement and attacks, a retained compact form, finite missiles, Energy, map support, authored ability gates and live-time return. Super Metroid adds the timed Ceres escape, Missile Tank/door and Bomb capability chain. Fusion instead orders the Navigation/Data Room mission, uses an elevator-outage detour and resolves ordinary X versus protected Core-X absorption before its narrower Morph Ball return. Franchise identity does not erase those decision differences. | Near, `0.608696` |

## Taxonomy impact

`TAXONOMY_CHANGE_211` isolates the typed free-X/Core-X resolution. `SYS-398` still handles the resulting persistent Morph Ball state; the new gene does not duplicate retention itself. No previous game signature or verified combination changes.

## Negative results

`SYS-222` would imply a conventional carried world item and does not encode the first boss's regained lost capability. The manual's full ability catalogue does not license Bombs, Charge Beam, Ice Missiles or SA-X behaviour in the opening packet. Optional tanks are not assumed mandatory, and no mission-wide timer is added from live room time.

## Delta summary

## New facts

- [Observation | Corroborated | High] The opening route interleaves Navigation/Data Room orders, a disrupted elevator path, resource-bearing free X, the first Arachnus Core-X and retained Morph Ball (`MF-002`–`MF-009`).

## New genes

- [Observation | Corroborated | High] One Active `SYS-1234` separates typed X absorption from ordinary item pickup and from persistent capability retention.

## New combinations

- [Observation | Limited | Medium] None proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_211` adds the typed absorption boundary without changing prior signatures.

## New questions

- Which exact hit counts, refill amounts and optional-tank routes hold in a pinned original cartridge revision?
- Would direct cartridge play expose a regional difference in the first boss's Core-X behaviour?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0475` *The House of the Dead*, original arcade, only after full gates, one local commit and the Goal stop window.

## Why this game

- [Hypothesis | Limited | Medium] It continues the approved cross-platform horizon. The next selection horizon after this nine-game batch should distribute platforms rather than repeat mostly Nintendo.
