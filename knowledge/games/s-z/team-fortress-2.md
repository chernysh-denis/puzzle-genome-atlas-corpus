---
game_id: GAME-0187
slug: team-fortress-2
game_title: Team Fortress 2
analysis_status: reviewed
reviewed: 2026-08-29
combination_ids:
  - COMB-0185
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-187
    - ACT-190
    - ACT-340
  system:
    - SYS-004
    - SYS-208
    - SYS-215
    - SYS-380
    - SYS-382
    - SYS-384
    - SYS-385
    - SYS-598
    - SYS-599
    - SYS-600
  constraint:
    - CON-262
    - CON-269
    - CON-272
    - CON-341
    - CON-346
    - CON-502
  information:
    - INF-073
    - INF-115
    - INF-116
    - INF-119
    - INF-150
  objective:
    - OBJ-111
  time:
    - TIM-003
---

# Game: Team Fortress 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current Windows Steam client, public build `24245096`,
  Valve update boundary `2026-07-16`, checked `2026-08-29`; one ordinary
  official Valve Casual Core Payload match on stock map `pl_upward`, entered at
  the beginning of its 70-second setup and ending at the map result.
- Primary decision loop: choose or change one of nine classes in team spawn;
  move, aim, switch stock weapons, fire, reload, use stock class effects and
  communicate; after death wait for the next eligible team respawn wave; BLU
  escorts the cart while RED contests it; checkpoint state changes time,
  rollback floor and spawn access; complete or deny the route through the final
  legal overtime state.
- Entry and exit: begins on a newly matched Upward server at the opening setup
  state, before class confirmation. If matchmaking joins a match already in
  progress, requeue. It ends when BLU pushes the cart into checkpoint D's pit
  and the cart explodes, or when the clock and final eligible overtime expire
  before that terminal and RED is declared the winner.
- Included: ordinary Casual teams up to 12 players per side; all nine class
  choices as typed alternatives; the controlled player's stock loadout;
  direct movement, weapon combat, random critical hits where the stock weapon
  permits them, stock class abilities, health/ammo/metal supply, death and
  team-wave return; Upward checkpoints A–D, time awards, spawn relocation,
  route locking, BLU cart proximity, RED blocking, capped pusher speed, Scout
  double push count, unattended rollback, cart resupply, route HUD and
  five-second-reset overtime.
- Reproducible parameterisation: queue only Casual Core Payload with Upward
  selected and requeue unless a fresh Upward setup is obtained. The controlled
  player may choose any currently useful class but uses that class's always-
  available stock weapons. Other players may carry legal unlocks; unlock-
  specific effects are not decomposed separately and remain generic combat
  parameters. Exact team composition, aim, casualties and match duration are
  parameters.
- Excluded: Payload Race and every other map or mode; Competitive, Mann vs.
  Machine, community/custom servers, Workshop and event variants; alternate
  weapons, crafting, trading, item drops, cosmetics, achievements, contracts,
  Casual XP/MMR, auto-balance policy, rematch voting and post-match rewards;
  exhaustive class matchups, map exploits, balance history and update history.
- Potential scoped modules: one alternate stock map, another official mode,
  one declared unlock loadout, Competitive, Mann vs. Machine or a community
  ruleset whose bounded terminal materially changes the decision loop.
- Direct-play status: no authenticated live match was played. Current Valve
  product and update material pins the live client; Valve's maintained official
  Team Fortress Wiki establishes the Casual, Payload, Upward, class, critical,
  health and respawn transition trace. Steam package metadata is secondary
  build corroboration. The repository trace is rules reasoning, not direct play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TF2-001` | The current Steam product is Team Fortress 2; build `24245096` follows Valve's `2026-07-16` update boundary | Confirmed | Corroborated | High | P1, P2, S1 |
| `TF2-002` | Casual lets players filter Core Payload maps and official Valve servers enforce the ordinary pure-server boundary | Confirmed | Direct | High | P3 |
| `TF2-003` | Upward is official `pl_upward`, begins with 70 seconds of setup and has one four-checkpoint Payload round | Confirmed | Direct | High | P4, P5 |
| `TF2-004` | BLU proximity advances the cart, more pushers accelerate it up to the declared cap, Scout counts double and RED proximity blocks movement | Observation | Direct | High | P5, P6 |
| `TF2-005` | Unattended cart state can roll back to the latest secured checkpoint, while reaching A, B and C awards 3, 5 and 4 minutes and changes spawn access | Observation | Direct | High | P4, P5 |
| `TF2-006` | The cart supplies nearby BLU players like a Level 1 Dispenser, restoring health, ammunition and Engineer metal | Observation | Direct | High | P5, P9 |
| `TF2-007` | Nine classes expose different stock combat, mobility, support, building, healing, disguise and infiltration effects; stock weapons remain available | Confirmed | Direct | High | P7, P8 |
| `TF2-008` | Death removes control until an eligible shared team respawn wave; the default wave is ten seconds and high population may defer a player to the next wave | Observation | Direct | High | P10 |
| `TF2-009` | Ordinary eligible weapons can sample random critical hits whose chance depends on weapon category and recent damage and whose full result normally triples base damage | Observation | Direct | High | P11 |
| `TF2-010` | At clock expiry an eligible non-retreating cart enters overtime; BLU then has five seconds to touch it, each push resets the window, final delivery wins BLU and cleared pressure wins RED | Observation | Direct | High | P5 |
| `TF2-011` | The repository transition trace reproduces class choice, stock combat, respawn waves, cart motion, checkpoints, supply, overtime and the one-round terminal | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Valve; Windows release in 2007 and continuously updated
  official Steam live client.
- Platform or physical form: authenticated networked Windows PC client on an
  official Valve Casual server.
- Puzzle family: simultaneous team objective combat; asymmetric escort and
  denial; class-mediated coordination; real-time system pressure.
- Primary sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/440/Team_Fortress_2/),
    for the current title, Valve identity, nine classes and supported modes,
    checked 2026-08-29.
  - **[P2]** [official Valve update history](https://www.teamfortress.com/?tab=updates),
    for the `2026-07-16` live update boundary.
  - **[P3]** [official Team Fortress Wiki Casual Mode](https://wiki.teamfortress.com/wiki/Casual_Mode),
    for map filtering, Core Payload, party/server boundaries, late joining and
    excluded XP/rematch systems.
  - **[P4]** [official Team Fortress Wiki Upward](https://wiki.teamfortress.com/wiki/Upward),
    for `pl_upward`, setup, checkpoints, time awards, spawn changes and final pit.
  - **[P5]** [official Team Fortress Wiki Payload](https://wiki.teamfortress.com/wiki/Payload),
    for proximity motion, checkpoints, rollback, cart supply, overtime and result.
  - **[P6]** [official Team Fortress Wiki cart push speed](https://wiki.teamfortress.com/wiki/Cart_push_speed),
    for capped pusher contribution and Scout's doubled count.
  - **[P7]** [official Team Fortress Wiki Classes](https://wiki.teamfortress.com/wiki/Classes),
    for the nine classes and their typed roles and stock abilities.
  - **[P8]** [official Team Fortress Wiki Weapons](https://wiki.teamfortress.com/wiki/Weapons),
    for always-available stock weapons and weapon/ammunition boundaries.
  - **[P9]** [official Team Fortress Wiki Health](https://wiki.teamfortress.com/wiki/Health),
    for pickups, lockers and the cart's Level 1 Dispenser health rate.
  - **[P10]** [official Team Fortress Wiki respawn times](https://wiki.teamfortress.com/wiki/Respawn_times),
    for shared team waves and their ordinary timing.
  - **[P11]** [official Team Fortress Wiki critical hits](https://wiki.teamfortress.com/wiki/Critical_hits),
    for random selection, recent-damage scaling and critical damage.
- Secondary and reproducible sources:
  - **[S1]** [SteamDB Team Fortress 2 depots](https://steamdb.info/app/440/depots/),
    observed 2026-08-29, for public build `24245096`; Valve sources independently
    establish the live update boundary.
  - **[V1]** repository-side transition trace derived from `P1`–`P11`; executable
    rules reasoning, not direct play.
- Claim IDs: `TF2-001`–`TF2-011`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate the active class; `ACT-161`, aim and
  strike; `ACT-164`, switch the carried stock weapon; `ACT-183`, reload;
  `ACT-187`, communicate a live team cue; `ACT-190`, activate a stock class
  ability, building or tool input.
- New gene: `ACT-340`, choose or change one playable class in team spawn.
- Parameters: class, movement, weapon slot, aim, target, reload, ability,
  building, communication channel and spawn state.
- Claim IDs: `TF2-007`, `TF2-011`.

### System Behaviour Genes

- Existing genes: `SYS-004`, sample eligible random critical outcomes;
  `SYS-208`, resolve ranged aim, cover and body hit; `SYS-215`, resolve live
  hostile combat; `SYS-380`, resolve stock class abilities into typed effects;
  `SYS-382`, remove a defeated class and return it through the legal spawn;
  `SYS-384`, advance, stop or reverse the route cart from team proximity;
  `SYS-385`, extend legal objective pressure into overtime and adjudicate the
  route result.
- New genes: `SYS-598`, secure a Payload checkpoint and apply its time, rollback
  and spawn transition; `SYS-599`, batch eligible dead players into team
  respawn waves; `SYS-600`, project the cart's attacker-only health/ammo/metal
  resupply field.
- Resolution order: class choice establishes the stock kit; continuous movement,
  attacks, abilities and cues resolve; eligible attacks may sample a critical;
  lethal state waits for a team wave; attacker and defender proximity settle
  cart motion; checkpoints lock route state and transform time/spawns; cart
  proximity supplies BLU; clock expiry tests overtime pressure; final delivery
  or cleared legal pressure declares the team result.
- Claim IDs: `TF2-004`–`TF2-011`.

### Constraint Genes

- Existing genes: `CON-262`, weapon slots and ammunition are finite;
  `CON-269`, stock ability use requires legal target, range, resource and
  readiness; `CON-272`, death blocks class control until return; `CON-341`,
  overtime requires continuing legal objective pressure; `CON-346`, the scoped
  stock loadout must belong to the selected class and playlist.
- New gene: `CON-502`, a class change takes effect only through a legal team-
  spawn or next-life state, while teammate duplicates remain permitted.
- Scarce strategic resources: health, living teammates, cart presence,
  ammunition, metal, charge/readiness, respawn timing, safe sightlines,
  checkpoint time and overtime touch window.
- Claim IDs: `TF2-004`–`TF2-010`.

### Information Genes

- Existing genes: `INF-073`, active stock weapon and ammunition are visible;
  `INF-115`, local sight, sound and effects reveal partial opponents;
  `INF-116`, team, clock, cart route, checkpoint, push and overtime state are
  visible; `INF-119`, health, condition and class readiness are visible;
  `INF-150`, the class roster exposes roles, kits and allied composition.
- New genes: none; cart outline and progress are parameters of shared-objective
  visibility rather than a new information boundary.
- Claim IDs: `TF2-004`–`TF2-011`.

### Objective Genes

- Existing genes: none.
- New gene: `OBJ-111`, win one Payload route by delivering the BLU cart to its
  terminal or denying it through the final legal overtime state.
- Success, evaluation and failure: BLU succeeds only at checkpoint D's pit;
  RED succeeds when legal time and pressure end before D. Eliminations,
  personal score and intermediate checkpoints are enabling state, not terminals.
- Claim IDs: `TF2-003`–`TF2-005`, `TF2-010`–`TF2-011`.

### Time Genes

- Existing gene: `TIM-003`, both teams and the match clock evolve concurrently.
- New genes: none.
- Claim IDs: `TF2-004`–`TF2-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Upward setup, player in team spawn | Select one of nine classes with its stock kit | Class becomes the controlled body; later changes require legal spawn/next-life state | reproducible class entry without hero uniqueness or role lock | `TF2-007`, `TF2-011` |
| BLU cart idle, no RED blocker | One or more eligible BLU players enter its push radius | Cart advances; speed uses capped pusher count and Scout contributes two | proximity escort rather than vehicle steering | `TF2-004` |
| BLU and RED are both in legal cart-blocking state | Continue fighting near cart | Cart stops until the RED block clears | combat controls route pressure without being a separate kill terminal | `TF2-004` |
| Cart has been unattended for 30 seconds after a secured checkpoint | No BLU player retouches it | Cart rolls backward toward, but not behind, its secured floor | checkpoint retention and reversible local progress | `TF2-005` |
| Cart crosses A, B or C | Maintain legal BLU push through the marker | Adds 3, 5 or 4 minutes and applies authored spawn/route state | checkpoint is a state transition, not only a progress label | `TF2-005` |
| BLU player stands within cart supply range | Remain beside the objective | Cart restores health, ammunition and eligible Engineer metal | objective presence also changes combat sustain | `TF2-006` |
| Several dead teammates await return | Team wave becomes eligible | Eligible players re-enter together through the current spawn system | shared wave timing differs from independent fixed countdowns | `TF2-008` |
| Clock reaches zero while cart is not rolling backward | BLU establishes or renews legal push | Overtime grants a five-second window and each valid push resets it | terminal pressure is touch-renewed and route-specific | `TF2-010` |
| Cart reaches D's pit / overtime pressure clears before D | Resolve terminal state | BLU cart explodes and BLU wins / RED wins | one complete authored Payload match | `TF2-010`, `TF2-011` |

## Strategic and experiential structure

- Local decision: aim or evade, choose weapon/ability timing, hold cover, push,
  block, heal, build or communicate while cart, health and nearby threats move.
- Medium-term planning: select a class that repairs the current composition,
  coordinate pushes around team waves, spend lives for checkpoint time, defend
  rollback space and exploit the cart as moving supply.
- Long-term structure: BLU converts four ordered route segments into a final
  delivery; RED consumes the clock and forces repeated re-entry from changing
  spawns until pressure disappears.
- Common heuristics: group after a wave rather than trickle; contest the cart
  only when the life trade protects time; use checkpoints as spawn/logistics
  pivots; change class at spawn when a missing function matters more than
  retaining the current kit.
- Failure attribution: missed aim, poor class coverage, uncoordinated waves,
  lost flank control, abandoned cart, failed block or illegal overtime touch
  are separable from matchmaking strength.
- Player-trust factors: readable class silhouettes and sound, clear cart path,
  checkpoint/time feedback, visible push/overtime state and consistent spawn
  transitions.
- Claim IDs: `TF2-004`–`TF2-011`.

## Replay and variation

- What changes between sessions: teams, class composition, spawn-wave phase,
  aim, random critical outcomes, combat positions, checkpoint timing and class
  switches.
- Randomness or procedural generation: eligible stock attacks may sample
  random critical outcomes; map geometry, route, checkpoints and terminal are
  authored and fixed.
- Multiple viable strategies: yes; teams can combine direct fire, mobility,
  healing, buildings, area denial, pick pressure and infiltration in different
  class mixtures without a formal role queue.
- Typical replay motive: improve class adaptation, coordinated wave timing,
  route control and checkpoint conversion against different teams.
- Claim IDs: `TF2-004`–`TF2-011`.

## Adjacent systems and history

- Direct predecessors: Team Fortress established class-based team shooting;
  Team Fortress Classic precedes the current Source-engine live client.
- Variants: other official modes, maps, unlock sets, Competitive, Mann vs.
  Machine and community servers are separate bounded modules.
- Similar games: Overwatch, Marvel Rivals, Battlefield 6 and class/objective
  multiplayer shooters.
- Important differences: unlike Overwatch Role Queue, TF2 allows duplicate
  classes and has no fixed team-role composition or match-local perks. Unlike
  Marvel Rivals Convergence, Upward starts with an already active cart and no
  opening capture phase, then binds route progress to checkpoint time/spawn
  transformations, unattended rollback and cart resupply. Unlike Battlefield 6
  Conquest, the terminal is one asymmetric authored route rather than a ticket
  economy across multiple capture areas.
- Claim IDs: `TF2-002`–`TF2-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-187`, `ACT-190`, `ACT-340` | navigation, stock combat, cue and class-change parameters |
| System Behaviour | `SYS-004`, `SYS-208`, `SYS-215`, `SYS-380`, `SYS-382`, `SYS-384`, `SYS-385`, `SYS-598`, `SYS-599`, `SYS-600` | critical, combat, cart, checkpoint, wave, supply and terminal parameters |
| Constraint | `CON-262`, `CON-269`, `CON-272`, `CON-341`, `CON-346`, `CON-502` | ammunition, readiness, death, overtime, loadout and spawn gates |
| Information | `INF-073`, `INF-115`, `INF-116`, `INF-119`, `INF-150` | weapon, local opponent, objective, personal and roster state |
| Objective | `OBJ-111` | complete or deny the four-checkpoint Payload route |
| Time | `TIM-003` | simultaneous teams and continuous authored match clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `186` (`GAME-0001`–`GAME-0186`).
- Exact genome matches: none.
- Tied near matches: `GAME-0147` — Marvel Rivals (`17 / 38 = 0.447368`).
- Supported combination subsets: `COMB-0185`.
- Scan date: 2026-08-29.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0147` — Marvel Rivals | `ACT-008`, `ACT-161`, `ACT-187`, `ACT-190`, `SYS-215`, `SYS-380`, `SYS-382`, `SYS-384`, `SYS-385`, `CON-269`, `CON-272`, `CON-341`, `INF-115`, `INF-116`, `INF-119`, `INF-150`, `TIM-003` | both are real-time class/hero team shooters with typed abilities, death-return pressure and a proximity-driven escort terminal, but TF2 begins with an active cart, permits duplicate class changes, batches returns into team waves, samples stock random crits and makes checkpoints alter time/spawns while the cart resupplies attackers; Marvel Rivals instead requires opening area capture, team-unique hero/Team-Up legality, ultimate economy and destructible arena state | Near, `0.447368` |

### Preserved research notes

- New genes: `ACT-340`, `SYS-598`–`SYS-600`, `CON-502` and `OBJ-111`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: generic movement, weapon combat, typed abilities,
  death return, proximity escort and contested overtime reuse safely. Spawn-
  legal duplicate class changes, authored checkpoint transformations, shared
  respawn waves, cart-linked supply and the Payload-specific result require
  narrower new records.

## Combination status

- `COMB-0185` is a verified strict twenty-gene subset of the thirty-gene
  genome, coupling class adaptation, live combat, team waves, checkpointed cart
  motion, moving supply and legal overtime to the one-round Payload terminal.
- Every earlier verified combination is tested deterministically after
  registration; none is a proper subset of this genome.

## Taxonomy impact

- Registry changes: six new Active genes, evidence links on twenty-four reused
  genes, `COMB-0185` and existing family memberships.
- Taxonomy-change record: none; no prior lifecycle or reviewed-game signature
  changes. `SYS-384`, `SYS-385`, `CON-341` and `CON-346` receive wording that
  preserves their original boundary while admitting a second evidenced ruleset.
- Candidate terms affected: spawn class change, payload checkpoint
  transformation, team respawn wave, objective-linked resupply and authored
  Payload terminal.

## Negative results

- `ACT-237` and `CON-338` are not reused: their active boundary includes
  Marvel Rivals Team-Up selection and team hero uniqueness, neither of which
  applies to duplicate-permitted TF2 classes.
- `ACT-188` is not reused: its match character is committed rather than changed
  freely through the live spawn state.
- `SYS-383` and `CON-340` are not reused: Upward has no opening area-capture
  phase before its cart becomes active.
- `OBJ-078` is not reused: its Convergence terminal requires that omitted
  opening capture, while `OBJ-111` begins with a Payload cart on its route.
- Payload Race, other maps/modes, unlock-specific effects, item economy and
  account progression are not admitted merely because the live client contains them.
