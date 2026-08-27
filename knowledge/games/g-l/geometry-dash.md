---
game_id: GAME-0167
slug: geometry-dash
game_title: Geometry Dash
analysis_status: reviewed
reviewed: 2026-08-27
combination_ids:
  - COMB-0165
gene_ids:
  action:
    - ACT-282
  system:
    - SYS-036
    - SYS-037
    - SYS-045
    - SYS-494
    - SYS-495
    - SYS-496
    - SYS-497
    - SYS-498
    - SYS-499
  constraint:
    - CON-113
    - CON-422
    - CON-423
    - CON-424
  information:
    - INF-192
    - INF-193
    - INF-194
  objective:
    - OBJ-094
  time:
    - TIM-003
---

# Game: Geometry Dash

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: official PC Steam version `2.2081`, default classic
  gameplay options, the built-in RobTop level `Stereo Madness` in Normal Mode,
  with progress display enabled and no third-party extensions.
- Primary decision loop: read the local side-scrolling obstacle horizon and
  audiovisual cadence; press, hold or release the one vertical control at a
  chosen time; let automatic horizontal travel, the current cube/ship force
  law, collision and the authored level clock advance; after failure, use the
  clean 0% retry and retained best progress to revise the next timing sequence.
- Entry and exit: begins when a fresh Normal Mode attempt starts as the cube at
  0%; succeeds at the first valid 100% finish, regardless of Secret Coin count,
  and otherwise returns to the same entry after lethal contact.
- Included: fixed automatic horizontal travel; cube support-gated jumps; ship
  hold/release flight; continuous gravity and collision; the authored cube ↔
  ship portals; visible blocks, gaps and spikes; the fixed Stereo Madness song,
  pulses and route timing; three optional Secret Coins and their alternate
  lines; attempt count, progress and best-percentage feedback; checkpointless
  Normal Mode failure, retry and completion settlement.
- Excluded: Practice Mode and checkpoints; the browser demo's coin-free variant;
  Click Between Steps, Click On Steps, Ignore Damage and non-default precision
  or editor-testing options; every other official level; platformer levels;
  user-created levels, editor, gauntlets and leaderboards; unlock economy,
  achievements, cosmetics, account/cloud state and third-party extensions.
- Potential scoped modules: one later official classic level with gravity,
  speed, size, orb or additional-form transitions; one official platformer
  level; Practice Mode learning; or the current user-level creation/verification
  packet.
- Direct-play status: no fresh complete paid-PC run was conducted. The official
  Steam product and current official announcements establish version, rhythm
  platforming, modes and Practice boundary; RobTop's official editor guide
  establishes the authored song/level relation; the official site offers a
  bounded Stereo Madness browser demo; the maintained Geometry Dash Wiki
  reproduces the current PC level sequence, coin routes and Normal/Practice
  distinction. The browser demo is evidence of the bounded subject, not a
  substitute for the PC coin layout.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GD-001` | The scoped software boundary is official Steam `2.2081`, whose update adjusts precision options without replacing Stereo Madness | Confirmed | Direct | High | P1, P2 |
| `GD-002` | Stereo Madness is one fixed official classic level with cube and ship sections | Observation | Corroborated | High | P1, P4, S1 |
| `GD-003` | One press/hold/release stream controls vertical response while horizontal travel remains automatic | Observation | Corroborated | High | P1, S1 |
| `GD-004` | Cube and ship both resolve continuous gravity/collision, but use different vertical input laws | Observation | Corroborated | High | P1, S1 |
| `GD-005` | Fixed portals change cube to ship and back without ending the attempt or resetting progress | Observation | Corroborated | High | P3, S1 |
| `GD-006` | The fixed soundtrack and authored geometry advance from one repeatable level origin | Observation | Corroborated | High | P1, P3, S1 |
| `GD-007` | Visible spike or unsafe solid contact ends the attempt before completion credit | Observation | Corroborated | High | P1, S1 |
| `GD-008` | Normal Mode failure restarts from 0%, while Practice Mode is the separate checkpoint-bearing ruleset | Observation | Corroborated | High | P1, S2 |
| `GD-009` | Stereo Madness contains three optional Secret Coins on alternate lines; ordinary completion does not require all three | Observation | Corroborated | High | S1 |
| `GD-010` | A valid finish settles 100% completion and eligible reward/coin state | Observation | Corroborated | High | P1, S1 |
| `GD-011` | The live viewport, progress and attempt feedback expose a local execution horizon but not the full future route | Observation | Corroborated | High | P4, S1 |

## Basic data

- Release / origin: RobTop Games; original mobile release 2013 and Steam PC
  release 2014; scoped current update `2.2081`.
- Platform or physical form: PC Steam single-player software.
- Puzzle family: checkpointless rhythm-cued precision auto-run platformer.
- Primary sources:
  - `P1` — [official Geometry Dash Steam product page](https://store.steampowered.com/app/322170/Geometry_Dash/),
    checked 2026-08-27.
  - `P2` — [official Geometry Dash Steam announcements](https://steamcommunity.com/app/322170/announcements/),
    including Update `2.2081`, checked 2026-08-27.
  - `P3` — [official RobTop Geometry Dash Editor Guide](https://www.robtopgames.com/files/GDEditor.pdf),
    checked 2026-08-27.
  - `P4` — [official Geometry Dash website](https://geometrydash.com/) and its
    official Steam launch notice for playable Stereo Madness, checked 2026-08-27.
- Secondary sources:
  - `S1` — [Stereo Madness — Geometry Dash Wiki](https://geometrydash.wiki.gg/wiki/Stereo_Madness),
    current level sequence and Secret Coin routes, checked 2026-08-27.
  - `S2` — [Practice Mode — Geometry Dash Wiki](https://geometrydash.wiki.gg/wiki/Practice_Mode),
    checkpoint and reward boundary, checked 2026-08-27.
- Claim IDs: `GD-001`–`GD-011`.

## Mechanical decomposition

### Action Genes

- `ACT-282` — modulate one context-sensitive vertical control. The player times
  press, hold and release; no horizontal direction or explicit mode choice is
  available.
- Candidate genes: none after review.
- Parameters: input device, input sampling, buffering, hold duration and current
  cube/ship mode.
- Claim IDs: `GD-003`, `GD-004`.

### System Behaviour Genes

- `SYS-036` — continuous force-constrained body dynamics. Gravity, impulses,
  velocity and collision remain live in both modes.
- `SYS-037` — contact-triggered collectible acquisition. A Secret Coin contact
  marks optional attempt state while travel continues.
- `SYS-045` — continuous autonomous agent locomotion. The icon advances
  horizontally without directional commands.
- `SYS-494` — authored portal replaces cube/ship mode and its control law.
- `SYS-495` — the one input resolves as supported cube jump or ship lift/drop.
- `SYS-496` — obstacle sequence, visual pulses and soundtrack share a fixed
  replayed level clock.
- `SYS-497` — lethal contact creates a clean retry from the 0% origin.
- `SYS-498` — failed attempts retain best reached percentage as feedback.
- `SYS-499` — the finish settles 100%, reward and contacted Secret Coins.
- Candidate genes: none after review.
- Resolution order: sample current input; advance authored clock and automatic
  travel; apply current-mode force response and body dynamics; resolve portal,
  coin and collision contacts in path order; on lethal contact end and restart,
  otherwise settle the finish when reached.
- Parameters: exact speed, timestep, input option, portal percentages, song
  offset, restart delay, reward values and prior save state.
- Claim IDs: `GD-002`–`GD-010`.

### Constraint Genes

- `CON-113` — contact with a visible spike is terminal before completion.
- `CON-422` — cube input is support-gated, ship input remains airborne-eligible,
  and neither mode grants horizontal stopping or reversal.
- `CON-423` — Normal Mode admits no intermediate respawn checkpoint.
- `CON-424` — safe support and lethal solid contact depend on mode, collision
  envelope and surface normal.
- Candidate genes: none after review.
- Scarce strategic resources: future obstacle sight time and the player's
  learned timing sequence; these are not inventory genes.
- Claim IDs: `GD-003`, `GD-004`, `GD-007`, `GD-008`.

### Information Genes

- `INF-192` — the side-scrolling viewport exposes a bounded local obstacle
  horizon rather than the full future level.
- `INF-193` — attempt, progress, best percentage, coin and completion state are
  visible under the scoped display settings.
- `INF-194` — fixed soundtrack and pulses cue the authored obstacle cadence.
- Candidate genes: none after review.
- Claim IDs: `GD-006`, `GD-009`–`GD-011`.

### Objective Genes

- `OBJ-094` — complete Stereo Madness from 0% to 100% in one checkpointless
  Normal Mode attempt; optional Secret Coins do not gate success.
- Candidate genes: none after review.
- Success, evaluation and failure: 100% is success; partial best percentage and
  optional coins provide evaluation; lethal contact fails only the current
  attempt and starts another.
- Claim IDs: `GD-007`–`GD-010`.

### Time Genes

- `TIM-003` — player input remains available while horizontal travel, forces,
  collision, music and progress advance in real time.
- Candidate genes: none after review.
- Claim IDs: `GD-003`, `GD-006`–`GD-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Opening cube is supported and the first spike approaches | Press or retain the one control at an eligible time | Cube receives its jump response while horizontal travel and gravity continue | Support-gated one-button auto-run | `GD-003`, `GD-004` |
| Cube reaches the first ship portal | Supply no separate mode command | Portal preserves the attempt clock/progress and replaces cube control with ship hold/release flight | Authored mode transformation | `GD-005` |
| Ship is airborne between solid floor and ceiling obstacles | Hold, then release the one control | Current mode biases vertical force up, then down, while forward speed continues | Continuous contextual input and collision envelope | `GD-003`, `GD-004` |
| Icon enters an optional Secret Coin route | Time the same control so the icon contacts the coin | Coin becomes pending attempt state without ending travel | Optional route collection | `GD-009` |
| Icon touches a spike or an unsafe solid face before the finish | Any preceding input sequence | Attempt ends; transient mode/position/pending coin state clear; a new cube attempt starts at 0% | Terminal collision and checkpointless retry | `GD-007`, `GD-008` |
| A failed attempt exceeded the prior best percentage | Begin the next retry | Route resets to 0%, while best progress remains visible | Learning feedback without position persistence | `GD-008`, `GD-011` |
| Icon reaches the authored finish alive | Continue through the boundary | Normal completion becomes 100%; ordinary reward and eligible contacted coins settle persistently | Scoped terminal | `GD-009`, `GD-010` |

## Strategic and experiential structure

- Local decision: choose the next press, hold duration or release from a short
  visible obstacle horizon and the current mode's force response.
- Medium-term planning: memorise the next cluster, portal transition and any
  optional coin deviation, then execute it from the same replay origin.
- Long-term structure: turn repeated best-percentage failures into one complete
  uninterrupted input sequence.
- Common heuristics: jump slightly before a spike rather than over its centre;
  treat each portal as a control-law boundary; in ship mode use short corrections
  instead of one long hold; learn optional coin lines separately.
- Failure attribution: fixed geometry and repeated timing make a crash largely
  attributable to input timing, duration or mode expectation rather than an
  unseen random sample.
- Player-trust factors: the route, music origin and collision rules repeat;
  local visibility, crash feedback and best progress expose why a retry differs.
- Claim IDs: `GD-002`–`GD-011`.

## Replay and variation

- What changes between sessions: player timing, optional coin path and retained
  completion/best-progress state; the scoped level sequence does not change.
- Randomness or procedural generation: none in the active level route.
- Multiple viable strategies: several jump timings can clear wide hazards;
  Secret Coins add three optional alternate lines, but all successful runs
  traverse the same authored mode order and finish.
- Typical replay motive: improve best progress, consolidate remembered timing,
  complete the level, then return for missing optional coins.
- Claim IDs: `GD-006`, `GD-008`–`GD-011`.

## Adjacent systems and history

- Direct predecessors: one-button auto-runners and rhythm-authored platformers;
  the claim is mechanical adjacency, not title ancestry.
- Variants: later official classic levels add gravity, size, speed, orbs and
  additional avatar forms; 2.2 platformer levels remove the same forced-scroll
  boundary.
- Similar games: The Impossible Game, BIT.TRIP RUNNER and rhythm precision
  platformers.
- Important differences: this scope fixes one current official level, two
  control regimes, optional coins and a clean full-level Normal Mode retry; it
  does not generalise the editor or user-level ecosystem.
- Claim IDs: `GD-001`–`GD-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-282` | input device, sampling and hold duration are parameters |
| System Behaviour | `SYS-036`, `SYS-037`, `SYS-045`, `SYS-494`–`SYS-499` | exact physics, percentages and reward values are parameters |
| Constraint | `CON-113`, `CON-422`–`CON-424` | collision tolerances are parameters |
| Information | `INF-192`–`INF-194` | progress display option and audio latency are parameters |
| Objective | `OBJ-094` | collected Secret Coin count is not a victory gene |
| Time | `TIM-003` | frame/input precision option is a parameter |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `166` (`GAME-0001`–`GAME-0166`).
- Exact genome matches: none.
- Tied near matches: `GAME-0021` — Cut the Rope (`3 / 25 = 0.120000`).
- Supported combination subsets: `COMB-0165`.
- Scan date: 2026-08-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0021` — Cut the Rope | continuous force-constrained body dynamics, contact-triggered collectible acquisition and real-time execution | Geometry Dash advances one icon automatically through a fixed audiovisual route, changes one vertical command between cube and ship laws, and restarts the whole level after terminal contact; Cut the Rope exposes several spatial cut actions and routes a separate candy through local contraptions toward a receiver | Near, `0.120000` |

### Preserved research notes

- New genes: `ACT-282`, `SYS-494`–`SYS-499`, `CON-422`–`CON-424`,
  `INF-192`–`INF-194` and `OBJ-094`.
- Classification result: `New gene` and new verified combination.
- Evidence and reasoning: the corpus already owns continuous force physics,
  contact collection, automatic locomotion, visible terminal hazards and
  real-time forced progression. New boundaries are limited to the shared
  one-button mode law, authored audiovisual clock, checkpointless fixed-origin
  retry, performance retention, local horizon, coin/finish settlement and this
  exact terminal.

## Taxonomy impact

- Registry changes: fourteen Active genes and `COMB-0165`.
- Taxonomy-change record: none; no existing definition is deprecated, merged or
  split.
- Candidate terms affected: none.

## Negative results

- `ACT-008` is rejected: the player does not directly navigate horizontal
  position or freely choose local direction.
- `INF-001` is rejected: later route geometry is outside the scrolling viewport
  and cannot be inspected before the attempt reaches it.
- `SYS-369` and other checkpoint restoration genes are rejected: Normal Mode
  restarts the whole level from 0% rather than restoring an authored checkpoint.
- Practice checkpoints, user levels, editor objects, cosmetics and achievement
  rewards remain exclusions rather than silently expanding the signature.

## Delta summary

The Ukrainian headings below are the compact public delta ledger used by the
maintainer. Do not repeat the analysis; list only changes to the corpus.

## Нові факти

- [Observation | Corroborated | High] Зафіксований `Stereo Madness` поєднує
  автоматичний горизонтальний рух, різні закони керування кубом і кораблем,
  фіксовану музику, локальний огляд перешкод, смертельні зіткнення, повний
  перезапуск і фініш на 100%
  (`GD-001`–`GD-011`).

## Нові гени

- [Observation | Corroborated | High] Чотирнадцять обмежених генів описують
  спільну однокнопкову команду, портал зміни режиму, аудіовізуальний годинник,
  чистий повтор, збереження найкращого поступу, залежні від режиму контакти,
  локальний огляд, відгук про поступ і монети та фініш звичайного режиму без
  контрольних точок.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0165` — однокнопковий
  аудіовізуальний автопробіг без контрольних точок від 0% до 100%.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Family classification

- `FAM-007` — Physics and object manipulation: success depends on gravity,
  impulses, collision envelope and timing through authored geometry.
- `FAM-010` — Real-time system pressure: the level clock, automatic travel and
  collision continue while the player chooses the next input instant.
- No new family is created from one game.

## Plain-language interpretation

Stereo Madness moves whether or not the player is ready. The only control does
different work in different forms: on safe support it starts a cube jump; in
the ship it changes the vertical flight tendency while forward travel continues.
The portal is therefore not decoration — it changes how the next identical
press will resolve.

The fixed song, pulses and obstacles replay from the same origin, so failure
builds route memory. The viewport shows only a short future slice, while the
best percentage records how far the last timing sequence survived. A spike or
unsafe block face clears the live attempt and returns the icon to 0%; only one
unbroken run to the finish records 100%. Secret Coins invite harder side lines,
but none is required for the ordinary completion objective.

## New questions

- Which later rhythm platformer reuses a fixed audiovisual route while replacing
  clean full-level retry with checkpoints or beat-graded input?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0168` — Warframe.
- Optimisation criterion: continue the recorded demand-led horizon in exact order.
- Expected information gain: contrast a fixed one-button route with a current
  movement/loadout/mission/extraction progression packet.
- Backlog impact: sixth of nine authorised game units; it is not started here.

## Чому саме вона

- [Hypothesis | Limited | High] Warframe is the next immutable subject in
  `SEARCH_DEMAND_GAME_SELECTION_004` and tests live-service scope discipline
  after the compact Geometry Dash packet.

## Localisation status

- Ukrainian game, all new-gene and combination entries are reviewed in this unit.
- The canonical title remains `Geometry Dash` without a translated title suffix.

## Open questions

- A later official-level module can test gravity, size, speed, orb and additional
  form transitions without changing this Stereo Madness signature.
- Direct PC capture could verify exact current UI spacing and input-option labels;
  no unsupported frame-perfect or hitbox measurement is claimed here.

## Source notes

- Official Steam, RobTop guide and GeometryDash.com materials plus maintained
  current Stereo Madness/Practice references were checked on 2026-08-27.
- Product-wide user levels, editor, platformer mode and cosmetics were used only
  to draw exclusions and were not unioned into the active genome.

## Next recommended action

- After this unit passes every gate and receives its local source commit,
  integrate `GAME-0168` — Warframe after the required thirty-second stop window.

## Evidence limitations

- No fresh complete paid-PC playthrough was performed; current transitions are
  reconstructed from official product/update/guide material and maintained
  current level references.
- The official browser demo omits the current PC Secret Coins and is not treated
  as the active ruleset.
- Exact physics constants, input-step options and rendering latency remain
  versioned parameters rather than universal claims.
