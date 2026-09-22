---
game_id: GAME-0342
slug: pac-man
game_title: "PAC-MAN"
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
  system:
    - SYS-037
    - SYS-045
    - SYS-911
    - SYS-960
    - SYS-961
    - SYS-962
    - SYS-963
    - SYS-964
    - SYS-965
    - SYS-966
  constraint:
    - CON-183
  information:
    - INF-001
  objective:
    - OBJ-002
    - OBJ-007
  time:
    - TIM-003
---

# Game: PAC-MAN

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). PAC-MAN, Blinky,
Pinky, Inky, Clyde, Pac-Dots, Power Pellets and cherries are carrier
parameters, not gene names.

## Analysis scope

- Version / ruleset: the original North American Midway-licensed 1980 arcade
  PAC-MAN program, one-player mode, ordinary play rather than Rack Test or a
  speed-up modification. Cabinet settings are three starting lives and one
  bonus life at 10,000 points.
- Structured analysis target: one credited game on `PLAT-ARCADE-CABINET`,
  restricted to the first complete maze; see `GAME-0342` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: pre-enter one of four cardinal directions while
  PAC-MAN keeps moving; eat the next Pac-Dots; read four independently routed
  ghosts and their Scatter/Chase reversals; decide when a Power Pellet should
  turn pursuit into a short scoring opportunity; use the side tunnel and its
  ghost slowdown; optionally collect each timed cherry; preserve a finite life
  stock until all 244 dots are gone.
- Entry: first ordinary directional control after the first maze's `READY!`
  pause, with 240 ordinary Pac-Dots, four Power Pellets and the configured life
  stock intact.
- Positive terminal: all 244 dots have been collected, the cleared board has
  been rebuilt, and the next-round `READY!` state has appeared. The packet
  stops before first directional control in round two.
- Negative terminal: contact with a dangerous ghost consumes one life and
  returns the actors to their declared starts while collected dots remain
  removed; dangerous contact with no remaining life ends the credited game.
- Included: four-way buffered turning and continuous motion; dot and Power
  Pellet collection; the complete visible fixed maze; four ghosts' distinct
  target functions; timed Scatter and Chase periods and forced reversals;
  frightened pseudo-random routing; escalating 200/400/800/1600 ghost value;
  eaten-eye return and ghost restoration; personal/global dot-counter and
  timeout release from the ghost house; Blinky's two first-round Cruise Elroy
  thresholds; paired side-tunnel wrap and ghost-only slowdown; cherries after
  70 and 170 dots for a variable limited interval; visible score and lives;
  the one 10,000-point extra life; one-life reset, Game Over and first-maze
  clearance.
- Excluded: round-two input and every later difficulty table, fruit type,
  intermission and maze attempt; the level-256 split screen; two-player
  alternating mode; Puck Man, Ms. PAC-MAN, Pac-Man Plus, Championship Edition,
  ports, compilations and modern wrappers; Rack Test, speed-up chips, bootlegs,
  save states, patterns presented as guaranteed player execution, cheats and
  glitches such as actor tile pass-through.
- Reproducible parameterisation: begin one one-player credit under the declared
  settings, allow `READY!` to release ordinary control, then clear the first
  maze without changing service switches. Direction sequence, deaths, Power
  Pellet timing, ghost captures, cherries and final score may vary. Stop when
  the board has visibly reset for round two, or at Game Over if the finite life
  stock is exhausted first.
- Potential scoped modules: a performed board or verified ROM inspection,
  alternate DIP-switch configuration, second and later rounds, fruit table,
  split screen, two-player alternation, specific port or contemporary wrapper
  each require an independent entry, terminal and evidence packet.
- Direct-play status: not conducted. No cabinet, PCB, verified ROM, MAME run,
  controller trace, screenshot, video or audio was available or analysed. The
  packet is reconstructed from publisher history, the preserved Midway
  operator manual and a code-informed technical dossier; MAME is used only to
  distinguish documented program families and modifications.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PAC-001` | Namco released the original game in Japan in July 1980 and the Midway-licensed PAC-MAN reached the United States in October | Confirmed | Direct | High | P1, P2 |
| `PAC-002` | A four-way joystick preselects turns while PAC-MAN advances continuously through one fixed maze | Observation | Corroborated | High | P3, S1 |
| `PAC-003` | The first maze contains 240 ordinary dots and four Power Pellets, and all 244 must be eaten to start the next round | Observation | Corroborated | High | P3, S1 |
| `PAC-004` | Four ghosts alternate timed Scatter and Chase target modes, use different Chase targets and reverse on specified mode changes | Observation | Corroborated | High | S1 |
| `PAC-005` | A Power Pellet forces reversal and temporary frightened routing; captured ghosts score 200, 400, 800 and 1,600 in sequence, return as eyes and revive | Observation | Corroborated | High | P2, S1 |
| `PAC-006` | House release uses dot counters and timeout, while Blinky begins outside and accelerates at 20 and 10 remaining dots | Observation | Corroborated | High | S1 |
| `PAC-007` | The side tunnel wraps actors between horizontal edges and slows ghosts but not PAC-MAN | Observation | Corroborated | High | S1 |
| `PAC-008` | First-round cherries appear after 70 and 170 eaten dots for a variable nine-to-ten-second interval and are worth 100 points | Observation | Corroborated | High | S1 |
| `PAC-009` | Dangerous ghost contact consumes one life, restores actors while retaining cleared dots, and becomes Game Over when no life remains | Observation | Corroborated | High | P3, S1 |
| `PAC-010` | Under the declared cabinet settings, first reaching 10,000 points grants one extra life | Observation | Corroborated | High | P3, S2 |
| `PAC-011` | Scoring events update the visible score; clearing all dots rebuilds the board for the next round | Observation | Corroborated | High | S1 |
| `PAC-012` | No direct cabinet, PCB or verified-ROM play was performed | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Namco; Japanese public release in July 1980 and licensed
  North American Midway release in October 1980.
- Platform or physical form: original North American upright/cocktail arcade
  rules represented by `PLAT-ARCADE-CABINET`; one-player, one credited game.
- Puzzle family: real-time system pressure; tactical forecast and counterplay;
  agent routing and coordination; world topology and perspective.
- Primary and official sources, accessed 2026-09-21:
  - **[P1]** [official PAC-MAN history](https://www.pacman.com/en/history/),
    for focus-test, Japanese release, US release, creator credits and identity.
  - **[P2]** [official 1980 history panel](https://www.pacman.com/en/history/popup/y1980.php),
    for the name, maze pursuit and Power Pellet rule.
  - **[P3]** [preserved Midway operator manual](https://pacman.holenet.info/pacman_opmanual.pdf),
    for controls, play instructions, life and bonus adjustment boundaries and
    operator-test separation.
- Corroborating technical sources, accessed 2026-09-21:
  - **[S1]** Jamey Pittman's [The Pac-Man Dossier](https://pacman.holenet.info/),
    a documented code-informed account, for dot totals, routing modes, house
    release, fruit thresholds, speed, collision, scoring, death and clearance.
  - **[S2]** [International Arcade Museum DIP-switch record](https://www.arcade-museum.com/dipswitch-settings/pac-man),
    for available life and bonus-life settings; it is community corroboration.
  - **[S3]** [MAME hardware-driver record](https://github.com/mamedev/mame/blob/master/src/mame/pacman/pacman.cpp),
    for original-board, program-family and modification boundaries only.
- Research record: **[R1]** local preflight found no cabinet, PCB or verified
  program image; no audiovisual evidence or executable inspection was used.
- Claim IDs: `PAC-001`–`PAC-012`.

## Mechanical decomposition

### Action Genes

- `ACT-008` owns cardinal direction input and early turn buffering through the
  traversable maze. Continuous forward motion is system-owned. Claim: `PAC-002`.

### System Behaviour Genes

- `SYS-045` advances actors on the running clock; `SYS-037` removes contacted
  dots, Power Pellets and cherries and credits their value; `SYS-911` consumes
  one life and restores the controlled body while the stage remains viable.
- New `SYS-960` alternates Scatter and Chase schedules, assigns a different
  target function to each ghost and forces declared reversals. New `SYS-961`
  makes one Power Pellet temporarily reverse the predator relation, escalates
  consecutive capture value and restores captured ghosts through eye return.
  New `SYS-962` releases house-bound ghosts through dot counters or timeout and
  resets the appropriate release state after a lost life.
- New `SYS-963` creates two timed bonus objects at 70 and 170 collected dots.
  New `SYS-964` maps an actor through the paired side tunnel and applies its
  class speed. New `SYS-965` converts the first 10,000-point threshold into one
  additional life. New `SYS-966` settles all-dot clearance by rebuilding the
  maze and entering the next round's ready state. Claims: `PAC-003`–`PAC-011`.

### Constraint Genes

- `CON-183` bounds the credit by a visible finite life stock: lethal contact
  continues only while another life remains, one declared score milestone can
  extend the stock, and exhaustion ends the complete run. Claims: `PAC-009`,
  `PAC-010`.

### Information Genes

- `INF-001` exposes the complete current maze, remaining visible dots and
  Power Pellets, actor positions and modes, fruit presence, score and lives.
  Future target choices and fruit lifetime are not disclosed. Claims:
  `PAC-002`–`PAC-011`.

### Objective Genes

- `OBJ-007` requires all 244 declared dot targets; `OBJ-002` supports optional
  score maximisation through safe routing, frightened-ghost chains and fruit.
  Score cannot substitute for maze clearance. Claims: `PAC-003`, `PAC-005`,
  `PAC-008`, `PAC-010`, `PAC-011`.

### Time Genes

- `TIM-003` owns continuous motion, mode schedule, house timeout, frightened
  interval, fruit lifetime, collision and directional response. `READY!`
  suspends ordinary steering. Claims: `PAC-002`, `PAC-004`–`PAC-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| An open intersection approaches | hold a legal cardinal direction early | PAC-MAN turns in its accepted pre-turn window and continues down the new corridor | direction input is continuous steering, not a turn step | `PAC-002` |
| A Pac-Dot lies on the route | move through its tile | the dot disappears, ten points are credited and the collection count advances | route collection changes objective and score | `PAC-003`, `PAC-011` |
| A Power Pellet remains | contact it | the pellet disappears, ghosts reverse and enter timed vulnerability | one object temporarily reverses threat | `PAC-005` |
| Frightened time remains | contact successive blue ghosts | capture values double from 200 to 1,600; eyes return and revive | capture chains and enemy restoration share one mode | `PAC-005` |
| A ghost waits in the house | clear enough dots or let no-dot time expire | the eligible ghost exits; death selects the documented reset path | pressure is gated by collection and time | `PAC-006` |
| 70 or 170 dots are gone | continue play | a cherry appears below the house for a variable limited interval | milestones create optional timed score objects | `PAC-008` |
| An actor enters the side tunnel | continue through it | the actor exits opposite; only ghosts take the tunnel-speed penalty | topology and class speed couple | `PAC-007` |
| Score first reaches 10,000 | complete the scoring event | one life is added once | score extends the run without clearing the maze | `PAC-010` |
| Dangerous ghost contact occurs | allow collision outside frightened capture | one life is spent and actors reset while dots stay absent; zero stock ends play | progress persists but run stock does not | `PAC-009` |
| The final required dot remains | contact it | all 244 targets settle, the maze rebuilds and round-two `READY!` appears | exhaustive collection is the packet terminal | `PAC-003`, `PAC-011` |

## Strategic and experiential structure

- Local: pre-turn into safety, delay or take a Power Pellet, chase a vulnerable
  ghost, divert to a cherry or use the tunnel before modes close the route.
- Medium term: clear risky corners during Scatter, stagger Power Pellets,
  anticipate releases and Cruise Elroy, and protect lives as routes narrow.
- Long term: broad collection becomes dense pursuit; death preserves removed
  dots but spends run stock; exhaustive collection resets the same maze.
- Failure recovery: one life restores actors without replacing eaten dots.
  The finite stock and one score-earned extension bound retries.
- Information: current geometry and actors are public; future target tiles,
  frightened turns and fruit duration must be inferred rather than read.

## Replay and variation

- What changes: direction timing, dot order, contact deaths, Power Pellet use,
  captured-ghost chains, cherry collection and final first-maze score.
- Randomness: frightened routing reads a reset pseudo-random sequence; fruit
  lifetime varies within the documented interval. The first maze is fixed.
- Multiple strategies: corridor patterns, reactive routing, early or late
  Power Pellets and optional fruit detours can all reach the same final dot.
- Typical replay motive: safer clears and higher score are inside the rules;
  later speed tables and a perfect full game are outside this packet.
- Claim IDs: `PAC-002`–`PAC-011`.

## Adjacent systems and history

- Direct predecessor: the Japanese Puck Man is the earlier product identity,
  but this packet freezes the North American Midway-licensed PAC-MAN target.
- Variants: Ms. PAC-MAN, Pac-Man Plus, later ports, compilations and
  Championship Edition are separate products and rulesets.
- Similar games: maze traversal and collection recur widely, but the combined
  timed target modes, Power Pellet role reversal, house counters and paired
  tunnel distinguish this packet.
- Important difference: death preserves the current maze's removed dots while
  spending a run-level life, and clearance rebuilds the same maze under a new
  round table rather than ending the credited game.
- Claim IDs: `PAC-001`–`PAC-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008` | four-way joystick and pre-turn window are parameters |
| System Behaviour | `SYS-037`, `SYS-045`, `SYS-911`, `SYS-960`, `SYS-961`, `SYS-962`, `SYS-963`, `SYS-964`, `SYS-965`, `SYS-966` | ghost names, thresholds, scores, times and tunnel coordinates are parameters |
| Constraint | `CON-183` | starting lives and bonus setting are parameters |
| Information | `INF-001` | colour, sprites and HUD layout are presentation |
| Objective | `OBJ-002`, `OBJ-007` | score values and 244-target count are parameters |
| Time | `TIM-003` | frame rate, mode durations and fruit interval are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `341` (`GAME-0001`–`GAME-0341`).
- Exact genome matches: none.
- Tied near matches: `GAME-0114` — Peggle Deluxe (`4 / 19 = 0.210526`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0114` — Peggle Deluxe | `INF-001`, `OBJ-002`, `OBJ-007`, `TIM-003` | Both expose a complete current playfield, reward score, require a declared target set and continue in real time. Peggle uses one aimed ballistic shot, gravity, ricochet and a finite ball stock against orange pegs. PAC-MAN instead uses continuous steering, autonomous role-targeted pursuers, Power-Pellet role reversal, life-preserving maze progress, house release, fruit milestones and a class-sensitive wrap tunnel. | Near, `4 / 19 = 0.210526` |

### Preserved research notes

- New genes: `SYS-960`–`SYS-966`.
- Classification result: `New combination and seven new genes`.
- Evidence and reasoning: steering, continuous movement, contact collection,
  finite-life respawn, visible current state, dot clearance, score and live
  time transfer from reviewed carriers. The ghost-mode, house-release, bonus,
  tunnel, score-life and board-rebuild rules have no complete lower-ID owner.

## Taxonomy impact

- Registry changes: add seven Active system boundaries and GAME-0342 support
  to compatible existing genes; no lifecycle or earlier signature change.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_084`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_084.md).
- Candidate terms affected: PAC-MAN, Blinky, Pinky, Inky, Clyde, Pac-Dot,
  Power Pellet, Scatter, Chase, frightened, Cruise Elroy and cherry remain
  product or instance parameters.

## Negative results

- No cabinet, PCB, verified ROM, emulator execution, controller trace, save,
  screenshot, video or audio was available; timing and routing are source-
  reconstructed rather than locally measured.
- The packet does not claim parity with Puck Man, ports or modern wrappers and
  does not import later-round difficulty, fruit or split-screen behaviour.
- Ghost names, target formulas, fruit values and dot counts remain parameters;
  neither each ghost nor each scoring object becomes a gene.

## Delta summary

## New facts

- [Observation | Corroborated | High] One fixed first maze couples 244-target
  clearance with four role-specific pursuers, temporary predator reversal,
  finite lives and same-maze successor rebuilding (`PAC-002`–`PAC-011`).
- [Observation | Corroborated | High] Collection progress controls both an
  optional timed bonus and delayed hostile release (`PAC-006`, `PAC-008`).

## New genes

- [Observation | Corroborated | High] `SYS-960`–`SYS-966` isolate timed target
  routing, temporary capture reversal, house release, milestone bonus, paired
  tunnel, score-earned life and cleared-maze rebuilding.

## New combinations

- [Observation | Corroborated | High] No verified combination is a proper
  subset of the complete signature.

## Taxonomy changes

- [Observation | Corroborated | High] Seven new Active system definitions are
  appended without changing any earlier game signature or lifecycle.

## New questions

- Which verified original-board program revision should anchor a future direct
  execution packet, and do its default DIP settings match this configured run?
- How should second-round speed and frightened tables alter similarity once a
  later-round packet is independently bounded?

## Next recommended game

- [Hypothesis | Limited | Medium] a new nine-game audience-recognition
  selection, to be recorded only after this nine-unit Goal is accepted.

## Why this game

- [Hypothesis | Limited | High] PAC-MAN closes the batch with a globally
  recognisable compact ruleset whose pursuit and role reversal are not reduced
  to generic maze collection.

## Research checklist

- [x] exact arcade target, settings, entry, terminal and exclusions declared
- [x] publisher history, operator manual and technical dossier reviewed
- [x] direct-play and reverse-engineering limitations disclosed
- [x] complete six-type signature and lower-ID scan contract prepared
- [x] Ukrainian localisation, presentation and plain-language copy authored
- [x] original rule-valid artwork generated
- [ ] deterministic comparison and research artifacts regenerated
- [ ] repository, build, browser, typography and accessibility gates completed

## Transfer notes

- A comparison must preserve continuous movement, role-specific pursuit and
  temporary predator reversal; matching only collection or score is weak.
- Side-tunnel wrap is not a generic portal: it preserves direction and applies
  a ghost-specific speed modifier.
- This packet supports no claim about later fruits, speeds, ports or split screen.

## Comparison summary

No lower-ID game reproduces exhaustive dot clearance, independently targeted
timed pursuers, temporary edible reversal, counter-released pressure and
class-sensitive edge wrap. The generated scan is explanatory only; no verified
combination is registered.

## Review outcome

- Accepted: exact arcade identity, first-maze boundary, 244-dot target, ghost
  routing, Power Pellet reversal, house release, fruit milestones, side tunnel,
  finite lives, bonus life and round transition.
- Deferred: later rounds, alternate settings, hardware/program inspection,
  audiovisual capture and release parity.
- Rejected: importing Ms. PAC-MAN behaviour, treating a modern wrapper as the
  target, or calling reverse engineering direct play.
- Taxonomy: seven new system boundaries; all other terms reuse Active genes.
- Localisation: all Ukrainian game fields and seven new definitions were
  authored and reviewed in-unit; retained names appear in acceptance.
- Confidence: high for bounded rules and medium-high for code-level timing
  because no verified-program run occurred.
