---
game_id: GAME-0520
slug: animal-well
game_title: Animal Well
analysis_status: reviewed
reviewed: 2026-11-16
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
    - ACT-715
  system:
    - SYS-037
    - SYS-369
    - SYS-1363
    - SYS-1484
    - SYS-1485
    - SYS-1486
    - SYS-1487
    - SYS-1488
  constraint:
    - CON-799
  information:
    - INF-003
    - INF-179
  objective: []
  time:
    - TIM-003
---

# Game: Animal Well

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Button count, chamber layout, initial firecracker capacity and console prompts
parameterize the genes.

## Analysis scope

- Version / ruleset: English North American Nintendo Switch base game, released
  May 9, 2024, ordinary solo play in a fresh save. The analysis reconstructs
  the release-era route. The installed build and exact patch are unverified.
- Structured analysis target: `PLAT-NINTENDO-SWITCH`, original Switch base game.
- Primary decision loop: inspect the chamber and look for concealed routes,
  time jumps and lifts to reach the three door buttons, acquire the usable
  firecracker stock and hidden match, then choose when to spend a throw for
  brief light and ghost clearance and where to spend the match to change the
  room durably.
- Entry and exit: start when the avatar becomes controllable after emerging
  from the bulb. Follow the phone, three-button gate and firecracker route,
  including the hidden match chest. Finish when the candle in the blue-ghost
  chamber immediately east of the first telephone is lit, before any further
  exploration. The candle is the analysis endpoint, not an enforced game win.
- Included: lateral movement and jumps, narrow routes and concealed passages,
  a moving platform and crank-controlled lifts, yellow contact buttons and
  the linked door, first telephone save and failure return, the match chest,
  firecracker plants, carried capacity and release, mobile blue ghosts and
  the temporary flash versus lasting candle state.
- Excluded: eggs, map and stamps, other candles, the central hub and flame
  routes, later tools and capacity upgrades, later secret layers, speedrun
  routes, glitches and other platforms. Exact hitbox, fuse frames and complete
  inventory persistence across death are outside the verified boundary.
- Potential scoped modules: bubble traversal, Disc substitution on the shrine,
  and the multi-candle gate as separately evidenced tasks.
- Direct-play status: no direct play or audiovisual playback. Nintendo and the
  developer establish product, date, platform and design. Independent written
  walkthroughs document the initial route. The community reference supplies
  narrower ghost and restart details with stated confidence limits.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `AW-001` | The English Switch base game is a released product. The route starts at the controllable bulb emergence and passes the first telephone. | Observation | Corroborated | High | P1, R1, R3, R5 |
| `AW-002` | Jump across ledges and ride the independently moving support above the first phone. Local geometry and timing determine reachable routes. | Observation | Corroborated | High | R1, R2, R3, R5 |
| `AW-003` | Turn a nearby crank to raise its linked submerged platform. The route then uses that platform to cross water. | Observation | Corroborated | High | R1, R2, R3 |
| `AW-004` | Three spatially separated yellow buttons retain their individual activations over the route. The final unpressed button opens the gate. One path passes through a concealed opening. | Observation | Corroborated | High | R1, R2, R3 |
| `AW-005` | Collect firecrackers from plants. The opening capacity is three. A throw spends one, whose path depends on the launch direction and motion. Its flash briefly illuminates the room. | Observation | Corroborated | Medium | R1, R2, R3, R6 |
| `AW-006` | The local moving blue ghosts chase and can kill the starting avatar on contact. Community documentation specifies a reachable path, a flash warning and axis-aligned movement. | Observation | Corroborated | Medium | R1, R2, R3, R7 |
| `AW-007` | The firecracker can disperse a moving blue ghost. That does not set its candle flag or permanently suppress the spawn across death or reload. | Observation | Corroborated | Medium | R1, R2, R4, R6, R7 |
| `AW-008` | A concealed branch just beyond the button gate reaches the match chest. Lighting the candle spends a match, gives sustained local light and prevents further moving blue ghost spawns there. | Observation | Corroborated | High | P2, R3, R4, R7, R8 |
| `AW-009` | Interact with the yellow phone to save. Death returns to the last telephone used, or to the emergence room if none has been used. | Observation | Corroborated | Medium | R1, R3, R5, R9 |
| `AW-010` | The gate, pickups and candle locations are authored. Order of the three button contacts can vary. Waiting changes the moving support's position and the ghost encounter's state. | Observation | Corroborated | High | P2, R1, R2, R3 |

## Basic data

- Release / origin: Billy Basso, published by Bigmode. Nintendo lists the
  Switch release date as May 9, 2024.
- Platform or physical form: Nintendo Switch base game. The structured target
  is authoritative for this analysis. No broader platform inventory is inferred.
- Puzzle family: spatial physics, typed item delivery, ordered dependencies.
- Primary sources:
  - **P1** [Nintendo U.S. release listing](https://www.nintendo.com/us/store/products/animal-well-switch/).
  - **P2** [Nintendo's launch-period account with developer Billy Basso](https://www.nintendo.com/en-ca/whatsnew/explore-the-haunting-world-of-animal-well-and-read-some-tips-from-the-developer/),
    including exploration, hidden routes and candles for safety.
- Secondary sources:
  - **R1** [Shane Black, Dexerto, May 9, 2024](https://www.dexerto.com/gaming/animal-well-how-to-get-firecrackers-beat-the-first-enemy-2709714/),
    illustrated written run from the first ghost to the firecracker plants.
  - **R2** [Abdul Rafay, Nintendo Smash, May 14, 2024](https://nintendosmash.com/animal-well-how-to-get-past-the-first-ghost/),
    alternate button order, release stock and return to the east ghost room.
  - **R3** [Cande Maldonado, Bonus Action, opening route](https://bonus-action.com/guides/animal-well-complete-walkthrough/),
    switch positions, match recess, phone and protected advance.
  - **R4** [PCGamesN, May 9, 2024, candles and matches](https://www.pcgamesn.com/animal-well/candles),
    distinguishes room lighting from the short firecracker flash.
  - **R5** [Community starting-area inventory](https://animalwell.wiki.gg/wiki/Starting_area).
  - **R6** [Community firecracker reference](https://animalwell.wiki.gg/wiki/Firecrackers).
  - **R7** [Community moving and stationary blue ghost reference](https://animalwell.wiki.gg/wiki/Blue_ghost).
  - **R8** [Community match reference](https://animalwell.wiki.gg/wiki/Match).
  - **R9** [Community player and death reference](https://animalwell.wiki.gg/wiki/Player).
- Claim IDs: `AW-001` to `AW-010`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: move and jump as one persistent avatar through a side-view route.
- `ACT-341`: interact contextually with a chest, phone, crank or candle in reach.
- `ACT-715`: dispatch one carried firecracker in a chosen direction, with
  movement affecting its launch path. The carried item becomes a live object.
- Parameters: local clearance, support and input; equipped tool and current
  velocity; selected fixture and eligibility.
- Claim IDs: `AW-002`, `AW-003`, `AW-005`, `AW-008`, `AW-009`.

### System Behaviour Genes

- `SYS-037`: avatar contact acquires reachable firecracker plant pickups.
- `SYS-369`: failure returns to the selected local save anchor or the start.
- `SYS-1363`: the moving platform above the phone carries a supported avatar
  along its autonomous path. It changes the next reachable ledge.
- `SYS-1484`: crank input raises its linked support out of water.
- `SYS-1485`: individual contact flags accumulate, then release the linked gate.
- `SYS-1486`: a firecracker flash lights the immediate area for a short time and
  disperses the affected ghost without lighting the candle.
- `SYS-1487`: a match changes one candle to burning and suppresses future
  moving blue ghost spawns in that chamber.
- `SYS-1488`: a reachable route can trigger a warning and pursuit, with a
  damaging outcome upon player contact. Exact reachability is community-sourced.
- Resolution order: navigate or operate the lift, activate each switch, open
  the door on completion, take the stock and find the match, then clear or
  evade the mobile threat before approaching and lighting the candle.
- Claim IDs: `AW-002` to `AW-010`.

### Constraint Genes

- `CON-799`: the opening firecracker count is capped at three for that item
  type. A fourth cannot be added to the opening stock while it is full.
- Scarce strategic resources: the initially bounded firecrackers and the
  one match collected along this route. The single match is a route fact.
- Claim IDs: `AW-005`, `AW-008`.

### Information Genes

- `INF-003`: the hidden passage to a button and the match recess exist before
  discovery. The player tests openings in the apparent rock boundary.
- `INF-179`: the current chamber exposes visible enemies, supports, buttons,
  door and usable fixtures. Adjacent rooms and hidden branches can stay out of view.
- Claim IDs: `AW-002`, `AW-004`, `AW-006`, `AW-008`.

### Objective Genes

- No separate objective gene is added for the selected endpoint. The door has
  an in-game unlock predicate. Lighting this particular candle is a local
  safety decision rather than a mandatory stage settlement.
- Claim IDs: `AW-004`, `AW-008`.

### Time Genes

- `TIM-003`: movement and fixture actions are accepted while the independent
  platform, active ghost and thrown firecracker advance.
- Claim IDs: `AW-002`, `AW-005`, `AW-006`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First phone chamber, support away from the departure ledge | Wait on the upper ledge, jump when the support is within reach, then ride it | A supported actor is carried toward the opposite upper route | The moving platform is independent of the player's crank input | `AW-002` |
| Crank room, support below the water surface | Operate the reachable crank and use the raised platform | The platform becomes a usable intermediate foothold | A previously impossible crossing now has a landing | `AW-003` |
| Some yellow buttons down, door still closed | Contact the remaining button after reaching it by a different path | The last button opens the linked door without a second simultaneous occupant | Set completion differs from continuous pressure | `AW-004` |
| Gate open, no match in inventory | Jump into the upper concealed recess and open the chest | The chest grants a match without lighting anything yet | Concealed supply acquisition and fixture commitment are distinct | `AW-008` |
| Room unlit, at least one firecracker, active moving ghost | Throw into the ghost's area and let the flash resolve | The firecracker is spent, flash illuminates briefly and the ghost is removed from active play | The throw does not light the candle | `AW-005`, `AW-007` |
| Candle still unlit, match held | Reach the candle and light it | One match is used, the local light persists and moving blue ghosts stop spawning there | The candle changes later entry conditions | `AW-008` |
| First telephone saved, ordinary avatar dies | Allow the ordinary failure return | The player returns to the saved phone anchor | Defeat restarts at a local anchor rather than deleting the file | `AW-009` |

## Strategic and experiential structure

- Local decision: decide whether to bypass a ghost now or spend a firecracker
  to make the crank and jumps safe. Preserve room to escape while the fuse runs.
- Medium-term planning: use the upper loop to reach the separated switch and
  test apparent wall boundaries before returning with a match.
- Long-term structure: exchanging one match for local safety differs from
  repeatedly spending a carried throw. The larger candle set is outside this scope.
- Common heuristics: wait for the autonomous support, record which button remains,
  check a dark ledge for a continuing route, and avoid relying on the flash as a save.
- Failure attribution: mistimed traversal, insufficient separation from a ghost,
  or using the available item in the wrong place or at the wrong time.
- Player-trust factors: visible button changes and the opened door close the
  dependency chain. Concealed geometry and short light make local observation count.
- Claim IDs: `AW-002`, `AW-004` to `AW-010`.

## Replay and variation

- What changes between sessions: player route, button order, timing and number
  of firecrackers used. The authored positions remain the reference.
- Randomness or procedural generation: no evidence requires procedural room
  layout or random button assignment in this route.
- Multiple viable strategies: published routes use different button orders.
  A player can move past the early ghost or spend the acquired flash to remove it.
- Typical replay motive: make the opening route cleaner and reduce throws or retries.
- Claim IDs: `AW-004`, `AW-005`, `AW-007`, `AW-010`.

## Adjacent systems and history

- Direct predecessors: this packet does not assert a direct mechanical lineage.
- Variants: later tools and spirits interact with firecrackers in other ways.
  None is used to infer the opening ghost behavior.
- Similar games: LittleBigPlanet 2 shares live traversal, fixture use, prize
  contact and local retry. It has different mechanisms for crossing gaps.
- Important differences: a candle changes subsequent room conditions. A flash
  and a lit candle can both help against a ghost, but their persistence differs.
- Claim IDs: `AW-002`, `AW-005` to `AW-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-341`, `ACT-715` | route control, fixture and throw direction |
| System Behaviour | `SYS-037`, `SYS-369`, `SYS-1363`, `SYS-1484`, `SYS-1485`, `SYS-1486`, `SYS-1487`, `SYS-1488` | activation, recovery, route devices and two light responses |
| Constraint | `CON-799` | three firecrackers at base capacity |
| Information | `INF-003`, `INF-179` | authored concealment and chamber visibility |
| Objective | none | optional scoped candle endpoint |
| Time | `TIM-003` | live support, fuse and ghost sequence |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `519` (`GAME-0001`–`GAME-0519`).
- Exact genome matches: none.
- Tied near matches: `GAME-0394` — LittleBigPlanet 2 (`6 / 22 = 0.272727`).
- Supported combination subsets: none.
- Scan date: 2026-11-16.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0394` — LittleBigPlanet 2 | `ACT-008`, `ACT-341`, `SYS-037`, `SYS-369`, `INF-179`, `TIM-003` share live avatar movement, fixtures, contact pickups, checkpoint recovery and local view. | The Da Vinci route uses a reusable gripper, compatible anchors and bounce pads to reach its flags. This route uses the crank and an independently moving platform, a three-button condition, and two light tools with different costs and persistence. | Near, `0.272727` |

## Taxonomy impact

- Registry changes: `ACT-715`, `SYS-1484` to `SYS-1488`, `CON-799` admitted.
- Taxonomy-change record: [TAXONOMY_CHANGE_267](../../../research/taxonomy-changes/TAXONOMY_CHANGE_267.md).
- Candidate terms affected: none.

## Negative results

- No verified proper-subset combination. Release build, exact fuse timing,
  checkpoint retention per inventory field and broader platform parity remain
  unverified. No broader ghost, light or item behavior follows by analogy.

## Delta summary

The accepted unit adds a scoped route and new typed boundaries for light tools.

## New facts

- [Observation | Corroborated | High] A hidden match can durably suppress a
  room's moving blue ghost spawn after the short firecracker encounter (`AW-008`).

## New genes

- [Observation | Corroborated | Medium] Firecracker throw and flash, linked
  crank lift, persistent switch set, candle suppression, path-gated apparition
  and per-item capacity add seven registry entries.

## New combinations

- [Observation | Corroborated | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_267` records seven
  additions and eight unchanged transfers.

## New questions

- Which exact room, stock and checkpoint fields are retained on the original
  Switch build across death and a return from the title screen?

## Next recommended game

- [Hypothesis | Limited | Medium] Wii Sports Resort.
- Optimisation criterion: cover a motion-input task with repeated feedback.
- Expected information gain: compare physical input interpretation and spatial
  constraints to the discrete tool commitment documented here.
- Backlog impact: `GAME-0521` follows acceptance of this unit.

## Why this game

- [Hypothesis | Limited | Medium] An optional stable safety state changes the
  same space and threat that a finite throw can affect transiently.
