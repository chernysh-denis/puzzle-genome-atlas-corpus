---
game_id: GAME-0441
slug: pokemon-go
game_title: Pokémon GO
analysis_status: reviewed
reviewed: 2026-09-28
combination_ids: []
gene_ids:
  action:
    - ACT-194
    - ACT-577
  system:
    - SYS-307
    - SYS-1156
  constraint:
    - CON-276
    - CON-715
  information:
    - INF-426
    - INF-427
  objective:
    - OBJ-252
  time: []
---

# Game: Pokémon GO — launch-era location-to-catch encounter

Use the [canonical vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). A Poké Ball, a particular species, GPS coordinates and ring colour are parameters or carriers, not separate gene names.

## Analysis scope

- Version / ruleset: the original English mobile Pokémon GO at its July 2016 public launch in the United States, one ordinary visible wild encounter from the walking map through one successful capture or exit. The exact Android/iOS binary revision and server encounter table were not inspected. Dated launch and August 2016 publisher notices are used to distinguish this packet from later features; the current official help page corroborates only the unchanged elementary catch sequence, not the complete 2016 rules.
- Structured analysis target: `PLAT-ANDROID` in [`knowledge/platforms/games.json`](../../platforms/games.json), original US Android launch release. The simultaneously launched iOS app is historical context, not a second reviewed analysis target.
- Primary decision loop: move physically with the phone while the location-aware map follows; inspect a wild Pokémon appearing within reach, tap it, hold a carried Poké Ball to judge the visible coloured target ring, then flick a timed and aimed throw. If it misses or the Pokémon breaks out, decide whether to spend another available Ball, use a different eligible Ball or leave. A hit and capture check can retain the Pokémon in the collection.
- Entry: location service and app are functioning, a map-visible ordinary wild Pokémon is in reach, and at least one compatible Ball is carried. Account creation, starter tutorial, acquiring the initial Ball supply and Pokémon storage exhaustion are outside this bounded packet.
- Positive terminal: the selected wild Pokémon is caught and recorded as owned. Negative or voluntary terminal: it can break free and eventually flee, the player can leave the encounter, or available Ball supply may be exhausted; no claim is made that an ordinary catch is guaranteed.
- Included: real-world walking as map input, map-visible wild encounter, tap-to-enter encounter, aimed touch throw, hit-versus-miss gate, finite compatible Ball supply, visible ring as difficulty/timing feedback, capture-versus-breakout response and one retained catch.
- Excluded: weakening a Pokémon in a turn-based battle, Gyms, PvP, eggs, evolution, PokéStops as a subloop, lure/incense, optional camera/AR rendering, accessory auto-capture, the later Nearby redesign, raids, research, weather, medals or streak bonuses, later Ball types, exact capture-rate formula, server spawn algorithm, legal/security policy and location spoofing. The 2016 notices identify Nice/Great/Excellent XP and a temporary throw-accuracy bug, but neither an exact XP amount nor the bug is treated as a stable rule of this launch packet.
- Reproducible parameterisation: in a functioning original July 2016 Android client in a supported US area, walk safely until a wild Pokémon appears on the map; tap it, hold a Ball to expose the changing ring, flick at the Pokémon and observe a miss, breakout or catch. Retry only while the encounter and Ball supply remain. This is a source-based procedure, not a claim of direct play or a deterministic replayable coordinate; the 2016 server and executable were not available here.
- Potential scoped modules: PokéStop inventory replenishment, Gym battle/ownership, egg-distance progress, account-level collection and post-launch capture modifiers.
- Direct-play status: no 2016 Android binary, server, phone, gameplay capture, video or audio was inspected. Dated Niantic primary statements and a contemporary first-hand written guide bound the historical packet; current official help is used only for the elementary continuing interface sequence. The illustration is original interpretive art, not a game screenshot.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PGO-001` | The July 2016 public app used smartphone location to connect neighbourhood exploration with wild Pokémon capture; PokéStops provided Balls. | Confirmed | Direct | High | P1 |
| `PGO-002` | A map-visible wild Pokémon can be tapped to enter a separate catch view, where a flicked Ball aims at it. | Observation | Corroborated | High | P2, P3 |
| `PGO-003` | The target ring communicates difficulty and timing; a Ball must connect before capture can resolve, and the Pokémon may break out. | Observation | Corroborated | High | P2, P3 |
| `PGO-004` | Balls are an available, consumed supply; retry or leave is possible rather than a guaranteed one-throw success. | Observation | Corroborated | High | P1, P2, P3 |
| `PGO-005` | In August 2016 Niantic acknowledged a temporary accuracy bug and separately fixed Nice/Great/Excellent throw XP awards; exact coefficients must not be inferred as launch constants. | Confirmed | Direct | High | P4, P5 |

## Basic data

- Release / origin: Niantic's public Pokémon GO launch on 6 July 2016 for Android and iOS in the United States, Australia and New Zealand; analysis target is original US Android.
- Platform or physical form: GPS-capable Android smartphone with touch input and an online location-linked map.
- Mechanical family: spatial object manipulation (`FAM-007`) through the aimed Ball's contact gate, and inventory/fixture dependencies (`FAM-013`) through a finite carried capture supply addressed to a visible wild target. Neither implies that a PokéStop is played within this one-encounter packet.
- **P1:** [Niantic, launch announcement](https://pokemongo.com/news/launch), 6 July 2016 (accessed 2026-09-28). Primary evidence for launch platforms, location technology, neighbourhood capture and Ball supply at PokéStops.
- **P2:** [Nintendo Life, contemporary first-hand capture guide](https://www.nintendolife.com/news/2016/07/guide_advanced_pokemon_go_capture_tips_and_how_to_get_better_pokeballs), 14 July 2016 (accessed 2026-09-28). Independent first-hand description of the encounter ring, Ball aim and early capture interface; it is not internal probability documentation.
- **P3:** [Pokémon GO Help Center, finding and catching wild Pokémon](https://niantic.helpshift.com/hc/en/6-pokemon-go/faq/102-finding-catching-wild-pokemon/), accessed 2026-09-28. Current official help corroborates map tap, ring, throw, breakout, remaining Balls and encounter exit. Its newer berries, bonuses and settings are explicitly excluded from the historical scope.
- **P4:** [Niantic, throw-accuracy bug notice](https://pokemongo.com/news/encounter-update), 4 August 2016.
- **P5:** [Niantic, 0.33.0 / 1.3.0 release notes](https://pokemongo.com/news/update-080816), 8 August 2016.
- Claim IDs: `PGO-001`–`PGO-005`.

## Mechanical decomposition

### Action Genes

- Add `ACT-577` for deliberate physical relocation that changes the location-based play position. Reuse `ACT-194` for committing one carried capture device to the wild target; touch-flick direction and release timing are parameters of this action, not another gene (`PGO-001`–`PGO-004`).

### System Behaviour Genes

- Add `SYS-1156` for projecting the device's real-world position into the map and exposing nearby wild creatures eligible for contact. Reuse `SYS-307` for a successful hit's uncertain capture response and retained ownership (`PGO-001`–`PGO-004`). Resolution order: location update → map-visible encounter → tap → aimed Ball hits or misses → on hit, catch or breakout → retain on catch.

### Constraint Genes

- Reuse `CON-276` for an eligible wild target and carried compatible Ball. Add `CON-715` because an aimed throw must physically intersect the visible target before any catch check; a miss cannot be treated as an unlucky capture roll (`PGO-002`–`PGO-004`). The exact Ball depletion semantics on misses are not independently measured here.

### Information Genes

- Add `INF-426` for the location-following map and locally visible wild target; add `INF-427` for the separate encounter ring's changing size and colour as feedback on timing and apparent catch difficulty. It does not reveal the exact probability or guarantee success (`PGO-001`–`PGO-003`).

### Objective Genes

- Add `OBJ-252`: complete this analytic episode by retaining one wild Pokémon after a resolved catch. The original app has a broader open-ended collection, not an authored global one-catch victory (`PGO-001`, `PGO-004`).

### Time Genes

- None admitted. The encounter is live and a Pokémon may flee, but the cited packet establishes no universal fixed deadline or action-clock whose timing is necessary to the chosen catch. The changing ring is visible feedback, not a separate forced-progression terminal.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Working map in one real-world location; no target in contact range | Walk safely with the app open | Device position and visible local map region change; a nearby wild target may appear | physical location is input to encounter availability | `PGO-001`, `PGO-002` |
| Wild Pokémon appears on map | Tap that target | Separate capture view shows the target and Ball | map detection and throw attempt are distinct | `PGO-002` |
| Ball is held in encounter view | Observe changing ring, then flick | Throw trajectory either connects or misses; the ring indicates difficulty and timing but not certainty | hit gate precedes stochastic capture | `PGO-002`, `PGO-003` |
| Ball connects with eligible wild target | Wait for capture response | Pokémon is caught and retained, or breaks free for another attempt if still present | ownership is not guaranteed by contact | `PGO-003`, `PGO-004` |
| Encounter remains unresolved and Balls remain | Retry or leave | Another eligible Ball can be committed, or the encounter ends without this catch | finite retry/exit branch | `PGO-004` |

## Strategic and experiential structure

- Local decision: balance ring timing and a clean on-screen trajectory against available Balls; colour is a difficulty cue, not an exact forecast.
- Medium-term planning: physical position determines which wild targets are available. Ball replenishment at PokéStops supports future loops but is outside this single encounter.
- Long-term boundary: one owned catch. The broader collection and battle economy are not compressed into this local objective.
- Failure attribution: a visible miss and a Ball breakout are different events; the latter does not reveal the hidden capture coefficient.
- Player trust: dated publisher notes show that accuracy/XP behaviour changed around a documented bug fix; avoid claiming one launch-era percentage or XP award that the sources do not settle.

## Replay and variation

Different real-world locations and currently exposed wild Pokémon change the encounter, while Ball stock and the timing/trajectory change the attempt. A successful hit can still break out. No precise spawn schedule, species weighting or catch formula is claimed from these sources.

## Adjacent systems and history

*Pokémon Red Version* (`GAME-0336`) also spends a Poké Ball and resolves uncertain capture, but its wild target is sampled through cartridge terrain steps and the Ball is selected from a turn-based battle menu. *Pokémon Legends: Z-A* (`GAME-0160`) also throws toward visible wild targets, but its analysed route includes avatar-controlled live combat and party progression rather than a device-location map linked to physical walking. The 2016 launch preceded later Pokémon GO systems such as raids and weather, both excluded.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-194`, `ACT-577` | wild target, available Ball, physical relocation and touchscreen flick |
| System Behaviour | `SYS-307`, `SYS-1156` | map projection, encounter availability, catch/breakout result |
| Constraint | `CON-276`, `CON-715` | target eligibility, Ball stock and throw contact |
| Information | `INF-426`, `INF-427` | map marker and encounter ring |
| Objective | `OBJ-252` | one caught, retained wild Pokémon |
| Time | none | no evidenced fixed deadline in this packet |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `440` (`GAME-0001`–`GAME-0440`).
- Exact genome matches: none.
- Tied near matches: `GAME-0336` — Pokémon Red Version (`3 / 31 = 0.096774`).
- Supported combination subsets: none.
- Scan date: 2026-09-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0336` Pokémon Red Version | `ACT-194`, `SYS-307`, `CON-276` | Both commit a finite Ball to an eligible wild creature and may retain it after an uncertain capture response. Red samples a hidden terrain-step encounter and chooses a Ball from a turn-based battle menu; GO first shows a target on a device-location map, then requires an aimed touchscreen contact before the capture check. | Tied-near maximum, not an exact match (`3 / 31 = 0.096774`). |

## Taxonomy impact

`TAXONOMY_CHANGE_178` admits six typed boundaries for physical-location input, map encounter response, throw contact, two information surfaces and one local capture objective. Earlier signatures and verified combinations are unchanged.

## Negative results

- `SYS-954` samples a hidden battle on a traversed cartridge terrain step; the Pokémon GO target is first visible on a location-following map and entered by touch.
- `ACT-008` directs a virtual avatar inside the game world; Pokémon GO's encounter search uses the player's actual physical relocation.
- `INF-144` is an authored GPS route to a designated driving target, not a device-position map of nearby wild creatures.
- `TIM-003` is rejected absent an evidenced universal timer or forced decision window for this one encounter. This does not deny that the online world is live.
- No exact 2016 server spawn tables, catch-rate equation, Ball depletion-on-miss measurement or original client trace were obtained.

## Delta summary

## New facts

- [Confirmed | Direct | High] Niantic's launch account ties phone location and neighbourhood exploration to wild capture (`PGO-001`).
- [Observation | Corroborated | High] Map tap, ring-guided throw and catch-versus-breakout form a bounded encounter (`PGO-002`–`PGO-004`).

## New genes

- [Observation | Corroborated | High] Six typed boundaries are admitted in `TAXONOMY_CHANGE_178`; three existing capture boundaries are reused.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_178`; earlier signatures remain unchanged.

## New questions

- Which exact launch build, when run against a preserved server or authenticated video trace, separates a miss's Ball consumption from capture-roll failure and documents encounter despawn timing?

## Next game

No next game is selected after `GAME-0441`; this closes the approved nine-game Goal horizon. A new subject selection requires maintainer direction.
