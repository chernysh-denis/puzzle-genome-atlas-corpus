---
game_id: GAME-0311
slug: super-mario-bros
game_title: Super Mario Bros.
analysis_status: reviewed
reviewed: 2026-09-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
  system:
    - SYS-036
    - SYS-037
    - SYS-045
    - SYS-064
    - SYS-900
    - SYS-901
    - SYS-902
    - SYS-903
    - SYS-904
    - SYS-905
  constraint:
    - CON-068
  information:
    - INF-192
    - INF-347
  objective:
    - OBJ-002
    - OBJ-164
  time:
    - TIM-003
---

# Game: Super Mario Bros&#46;

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: the original 1985 North American Nintendo Entertainment
  System game, one-player mode, with the original cartridge rules represented
  by Nintendo's preserved manual and the deterministic Japan/USA ROM
  disassembly at commit `6d0d367ccb7c9d037ca3b5e50453c55bd74cb869`.
- Entry: accept control of small Mario at the fixed World 1-1 origin after the
  one-player start. Score and coin count are zero, the stage clock is full and
  no emulator-side save state, rewind or online feature is active.
- Primary decision loop: read the bounded side-scrolling horizon; walk or run,
  vary jump height and airborne direction to cross gaps, reach blocks, collect
  coins or power-ups and approach enemies from a safe contact direction; let
  gravity, enemy walking, collisions and the stage timer continue; then choose
  the next route and timing toward the flagpole.
- Positive terminal: contact the World 1-1 flagpole, let contact height and
  remaining time settle into score, enter the small castle and reach the first
  controllable World 1-2 state with score, coins and current power state carried
  forward.
- Negative terminal: end this one World 1-1 attempt through lethal enemy
  contact while small, a fall below the route or timer expiry. The following
  life, midpoint restart and broader finite-life loop are outside the packet.
- Included: direct left/right movement, acceleration, running and variable
  jump; continuous gravity and collision; authored World 1-1 terrain and enemy
  data; coins; visible and block-released Mushroom, Fire Flower, Star and 1-Up
  effects when their predicates are met; Goomba and Koopa contact; shell kicks;
  brick and item-block strikes; fireballs when Fiery Mario is obtained; the
  one-way camera boundary; score, coins, world, time and life display; flagpole
  and castle closeout; one successful transition into World 1-2.
- Excluded: World 1-2 play after its first controllable state; warp zones;
  water, castle and later-world rules; Bowser; two-player alternation; a second
  life, midpoint restart, continue or Game Over; high-score persistence;
  controller peripherals; speedrunning; glitches; and every emulator-side
  rewind, suspend point, save state or online feature.
- Direct-play status: not conducted. The official manual directly establishes
  controls, movement, enemies, power states, score, timer, area division and
  flagpole closeout. The pinned source disassembly directly establishes the
  fixed World 1-1 data and exact rule branches. This is a reproducible
  source-based reconstruction, not a claim that a cartridge or licensed
  emulator session was completed. No video, audio or screenshot was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SMB-001` | The packet is the original one-player NES World 1-1 attempt and successor transition, not a remake or emulator feature layer | Confirmed | Direct | High | P1, P2, R1 |
| `SMB-002` | Left/right movement accelerates and decelerates, B raises running speed, and A-hold duration plus current horizontal speed alter the jump | Confirmed | Direct | High | P1, R2 |
| `SMB-003` | World 1-1 is fixed authored terrain and enemy data, while the camera exposes only a local forward slice and prevents returning behind its left boundary | Confirmed | Direct | High | P1, R3, R4 |
| `SMB-004` | Upward contact with a block may bump or break it by avatar state and may release its fixed coin or item result once | Confirmed | Direct | High | P1, R5 |
| `SMB-005` | Mushroom and Fire Flower advance the avatar's power state, hostile damage demotes a powered avatar before lethal small-state damage, and Star grants temporary contact immunity | Confirmed | Direct | High | P1, R5 |
| `SMB-006` | Top contact defeats a qualifying enemy and rebounds Mario; unsafe side contact damages or defeats him according to current power state | Confirmed | Direct | High | P1, R5 |
| `SMB-007` | Stomping a Koopa leaves a shell that a later contact can launch horizontally into eligible enemies | Confirmed | Direct | High | P1, R5 |
| `SMB-008` | Coins add score and coin count without ending the attempt; one hundred coins or a 1-Up add to the life stock | Confirmed | Direct | High | P1, R5 |
| `SMB-009` | Pit entry, lethal contact or timer expiry ends the current attempt; the broader next-life restart is outside this packet | Confirmed | Direct | High | P1, R5 |
| `SMB-010` | Flagpole contact locks ordinary control, awards a height-dependent result, converts remaining time to score and advances through the castle to World 1-2 | Confirmed | Direct | High | P1, R5 |
| `SMB-011` | Score, coin count and power state survive the World 1-1 to World 1-2 transition while the area timer is reset for the successor | Confirmed | Direct | High | P1, R5 |
| `SMB-012` | The bounded identity is a directly steered momentum platform route whose enemy direction, block state and temporary power state reshape the safe line to a scored successor transition | Strong Pattern | Corroborated | High | `SMB-002`–`SMB-011` |

## Basic data

- Release / origin: Nintendo released *Super Mario Bros.* for the Famicom in
  Japan in 1985 and for the Nintendo Entertainment System in North America in
  the same original rules generation.
- Platform or physical form: original one-player NES cartridge rules; lawful
  current catalogue access does not contribute emulator-only mechanics.
- Puzzle family: physics and object manipulation; real-time system pressure.
- Primary sources, accessed 2026-09-19:
  - **[P1]** [Nintendo's preserved original NES instruction
    manual](https://www.nintendo.co.jp/clv/manuals/en/pdf/CLV-P-NAAAE.pdf), for
    one-player controls, run/jump response, area structure, enemies, blocks,
    items, power states, deaths, score, timer and flagpole settlement.
  - **[P2]** [Nintendo's official Famicom product
    record](https://www.nintendo.com/jp/titles/20010000000866.html), for the
    original 1985 identity and the separation of the reproduced Famicom game
    from later platform wrappers.
- Reproducible code record, accessed 2026-09-19:
  - **[R1]** [smb1-disasm at pinned commit
    `6d0d367`](https://github.com/pgattic/smb1-disasm/tree/6d0d367ccb7c9d037ca3b5e50453c55bd74cb869),
    whose README identifies the Japan/USA ROM target and SHA-1
    `ea343f4e445a9050d4b4fbac2c77d0693b1d0922`.
  - **[R2]** [pinned player-movement
    engine](https://github.com/pgattic/smb1-disasm/blob/6d0d367ccb7c9d037ca3b5e50453c55bd74cb869/src/engine/game-mode/player-movement.asm),
    for acceleration, friction, running speed, speed-dependent jump force,
    A-hold truncation and horizontal air control.
  - **[R3]** [pinned scroll
    engine](https://github.com/pgattic/smb1-disasm/blob/6d0d367ccb7c9d037ca3b5e50453c55bd74cb869/src/engine/game-mode/scroll.asm),
    for rightward camera activation and viewport boundaries.
  - **[R4]** [pinned level
    data](https://github.com/pgattic/smb1-disasm/blob/6d0d367ccb7c9d037ca3b5e50453c55bd74cb869/src/levels.asm),
    for the labelled fixed `L_GroundArea6` and `E_GroundArea6` World 1-1
    terrain and enemy streams.
  - **[R5]** [pinned main gameplay
    engine](https://github.com/pgattic/smb1-disasm/blob/6d0d367ccb7c9d037ca3b5e50453c55bd74cb869/src/main.asm),
    for timer expiry, block results, power-up collision, enemy contact, shell
    launch, flagpole capture, score tables and area progression.
- Reproducible control: repository-side transition tracing against `P1`–`P2`
  and pinned `R1`–`R5` under the declared entry, terminal and exclusions;
  rules reasoning, not direct play.
- Claim IDs: `SMB-001`–`SMB-012`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly walk, accelerate, run, jump and steer Mario in
  the air through local platform geometry. Button identity, jump height,
  acceleration and speed are parameters.
- Existing `ACT-161`: while Fiery Mario is available, face a reachable hostile
  and commit a fireball through the current side-scrolling scene.
- No new Action gene is admitted. Variable jump height and running are force
  parameters of the same directly navigated body, not separate addressed
  commands. Claims: `SMB-002`, `SMB-005`.

### System Behaviour Genes

- Existing `SYS-036`: gravity, velocity, support and collision continuously
  resolve Mario's run and jump body against World 1-1 geometry.
- Existing `SYS-037`: contacting a coin removes or marks it and credits score
  and coin count without ending the attempt.
- Existing `SYS-045`: Goombas and Koopas continue their authored walking and
  edge/collision response without a command for every step.
- Existing, generalised `SYS-064`: a qualifying top impact defeats the enemy
  and rebounds Mario; unsafe lateral contact instead applies the current
  power-state damage result, which may demote rather than immediately defeat.
- New `SYS-900`: upward avatar contact resolves a mutable block by block class
  and avatar state: an eligible brick may bump or break, while an item block
  changes to its spent state.
- New `SYS-901`: the first eligible strike on a fixed reward block emits its
  authored coin or power-up result; later strikes cannot repeat the exhausted
  result.
- New `SYS-902`: eligible pickups move small Mario to Super, Super to Fiery or
  grant temporary Star immunity; hostile damage moves a powered state toward
  small before small-state lethal resolution.
- New `SYS-903`: a qualifying Koopa stomp replaces the walking enemy with a
  stationary shell, and later side contact launches that shell as a moving
  hostile-clearing body.
- New `SYS-904`: once Mario crosses the forward camera threshold, the viewport
  advances through fixed geometry and its left boundary becomes the earliest
  reachable position, preventing ordinary backtracking into discarded screen
  space.
- New `SYS-905`: flagpole contact height awards its declared score, remaining
  time converts to additional score, control follows the scripted castle
  closeout and the successor area starts with eligible run state retained.
- Resolution order: movement and autonomous enemies advance; collision resolves
  support, blocks, pickups, stomp, damage, shell or pit; the timer then remains
  authoritative until flagpole capture changes to closeout. Claims:
  `SMB-002`–`SMB-011`.

### Constraint Genes

- Existing `CON-068`: the displayed World 1-1 allowance decreases during the
  active attempt and zero is terminal unless flagpole completion has already
  taken control.
- Ground support, block reach, collision envelopes and exact jump values are
  parameters of movement and authored geometry. The one-way viewport changes
  reachable world state, so it is `SYS-904`, not a passive prohibition.
- Claims: `SMB-003`, `SMB-009`, `SMB-010`.

### Information Genes

- Existing, generalised `INF-192`: the side-scrolling viewport exposes Mario,
  local support, enemies, blocks, gaps, pickups and the next route slice while
  later World 1-1 geometry remains off-screen.
- New `INF-347`: the stage HUD exposes score, coin count, world/area, remaining
  time and life stock while sprite state visibly distinguishes small, Super,
  Fiery and temporary Star response.
- Exact hidden block contents and later geometry remain concealed before their
  trigger or camera entry. Claims: `SMB-003`–`SMB-005`, `SMB-008`–`SMB-011`.

### Objective Genes

- Existing `OBJ-002`: increase the session score through enemies, blocks,
  coins, flagpole height and efficient remaining time; no fixed score is needed
  for ordinary stage completion.
- Existing, generalised `OBJ-164`: satisfy World 1-1's flagpole exit event,
  enter its castle and arrive in World 1-2 with eligible accumulated state
  carried forward. The transition, not collecting every coin or defeating
  every enemy, is the required completion.
- Claims: `SMB-008`, `SMB-010`, `SMB-011`.

### Time Genes

- Existing `TIM-003`: enemies, gravity, projectiles and the stage deadline
  continue on the real-time clock while movement, jumping and fire inputs are
  accepted.
- Pause is an interruption of the same attempt, not a planning phase or
  reversible history. Claims: `SMB-002`, `SMB-006`, `SMB-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Small Mario is on level ground | Hold right, then add B and jump | horizontal speed accelerates; the speed band and A-hold duration alter the jump arc while air steering remains available | direct force-controlled navigation | `SMB-002` |
| Small Mario is below an intact brick | Jump into its underside | brick bumps but remains; nearby bodies may react to the bump | state-dependent block collision | `SMB-004` |
| Super Mario strikes the same eligible brick class | Jump into its underside | brick breaks and no longer supports later contact | avatar state changes the block result | `SMB-004` |
| An unspent reward block is struck | Contact its underside | its fixed coin or eligible power-up emerges and the block becomes spent | one-shot authored reward | `SMB-004`, `SMB-005` |
| Small Mario contacts a Mushroom | Continue through contact | the pickup is consumed and Mario becomes Super | power-state advance | `SMB-005` |
| Powered Mario takes unsafe enemy contact | Continue through contact | current power is lost and a short damage-grace interval begins; small-state contact would instead end the attempt | damage ladder differs from instant death | `SMB-005`, `SMB-006` |
| Mario descends onto a walking Koopa | Land from above | Koopa becomes a stationary shell and Mario rebounds | directional contact creates a new world body | `SMB-006`, `SMB-007` |
| Mario approaches the stationary shell from its side | Contact it | shell launches horizontally and can defeat eligible enemies it later contacts | transformed enemy becomes route hazard/tool | `SMB-007` |
| Camera has advanced beyond earlier terrain | Move left to the viewport boundary | Mario cannot return into the discarded earlier screen even though the authored stage continues there | one-way route state | `SMB-003` |
| Timer reaches zero before flagpole capture | Allow the clock to expire | the current attempt enters lethal resolution and cannot complete | authoritative deadline | `SMB-009` |
| Mario contacts the flagpole above its base | Continue through closeout | contact height awards score, remaining time converts to score, Mario enters the castle and World 1-2 becomes controllable with eligible state retained | scored successor transition | `SMB-010`, `SMB-011` |

## Strategic and experiential structure

- Local decision: choose speed, take-off point, A-hold duration and contact
  direction against the visible obstacle slice.
- Medium horizon: decide whether a block, coin line, power-up or shell is worth
  time and positional risk before the camera boundary removes the old route.
- Long horizon: preserve a useful power state and enough time to reach a high
  flag contact while still completing the stage.
- Reversibility: horizontal corrections and many missed pickups are locally
  recoverable until the camera passes them; spent blocks, broken bricks, enemy
  transformations, lost power and elapsed time are not reversible in the same
  attempt.
- Failure attribution: the visible contact normal, avatar form, pit boundary
  and timer distinguish stomp success, recoverable damage and terminal loss.
- Player trust: identical authored World 1-1 data, movement bands and collision
  branches must reproduce the same state transitions from the same state.

## Replay and variation

- World 1-1 geometry, block rewards and enemy stream are fixed; no procedural
  generation or random reward selection is admitted.
- Different legal lines arise from running versus walking, optional blocks and
  coins, enemy avoidance versus stomp/fire/shell use, Star timing and flagpole
  contact height.
- The packet stops before a second attempt, so midpoint restart and finite-life
  optimisation are not part of its genome.
- Replay motive outside the packet includes higher score, faster completion,
  power-state preservation and route mastery.

## Adjacent systems and history

- Braid shares directly steered platform movement, autonomous walking enemies,
  direction-sensitive stomp contact and real-time execution, but Braid makes
  history reversible and marks rewind-exempt bodies; World 1-1 instead commits
  elapsed time, block state and the scrolled-away route.
- Geometry Dash shares continuous body physics, local side-scrolling lookahead
  and a complete authored level, but its horizontal travel is automatic and
  failure restarts a checkpointless attempt. Mario controls horizontal speed,
  can absorb damage through power state and settles a successor transition.
- Cuphead shares direct fire and real-time avoidance, but its bounded objective
  is a health-gated multi-phase encounter rather than a traversed authored
  route whose terrain, rewards and camera boundary retain local history.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161` | exact controls, speed and projectile values are parameters |
| System Behaviour | `SYS-036`, `SYS-037`, `SYS-045`, `SYS-064`, `SYS-900`–`SYS-905` | fixed level data and collision tables are parameters |
| Constraint | `CON-068` | timer value and completion precedence are parameters |
| Information | `INF-192`, `INF-347` | viewport, HUD layout and sprite feedback are parameters |
| Objective | `OBJ-002`, `OBJ-164` | score value and successor state are parameters |
| Time | `TIM-003` | update cadence and pause behaviour are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `310` (`GAME-0001`–`GAME-0310`).
- Exact genome matches: none.
- Tied near matches: `GAME-0034` — Braid, Anniversary Edition (`5 / 27 = 0.185185`).
- Supported combination subsets: none.
- Scan date: 2026-09-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0034` — Braid, Anniversary Edition | `ACT-008`, `SYS-037`, `SYS-045`, `SYS-064`, `TIM-003` | Both directly steer a jumping avatar through live side-view enemies and collectibles, including a top-contact stomp. Super Mario Bros. commits elapsed time, block state, power loss and scrolled-away terrain toward a scored stage transition; Braid instead lets the player rewind lived history and exempts marked entities from restoration. | Near, `0.185185` |

### Preserved research notes

- New genes: `SYS-900`–`SYS-905` and `INF-347`.
- Classification result: `New gene`; no verified combination is supported.

## Taxonomy impact

- Registry changes: add six Active System Behaviour genes and one Active
  Information gene; add Super Mario Bros. support to eleven compatible
  existing boundaries; no earlier signature or lifecycle changes.
- Taxonomy-change record: `TAXONOMY_CHANGE_073` broadens wording for `SYS-064`,
  `INF-192` and `OBJ-164` without changing earlier carriers.
- Candidate terms affected: Mario, Goomba, Koopa, item names, World 1-1,
  World 1-2 and NES buttons remain product or instance parameters.

## Negative results

- No NES cartridge, console, licensed emulator run, controller trace or
  observed World 1-2 transition exists; this unit makes no direct-play claim.
- The one-attempt boundary deliberately cannot establish midpoint restart,
  finite-life Game Over, continue behaviour or high-score persistence.
- The pinned disassembly is a reproducible code record, not an authorised ROM
  distribution or substitute play build.
- Later worlds, water, castles, Bowser, two-player alternation, warp zones,
  glitches and emulator features remain excluded even when other sources
  describe them.

## Delta summary

## New facts

- [Confirmed | Direct | High] Nintendo's original manual establishes the
  one-player movement, jump, enemies, blocks, items, power states, score,
  timer and flagpole rules (`SMB-001`–`SMB-011`).
- [Confirmed | Direct | High] The pinned Japan/USA disassembly establishes the
  fixed World 1-1 data and exact movement, collision, scroll and transition
  branches (`SMB-002`–`SMB-011`).

## New genes

- [Confirmed | Direct | High] `SYS-900`–`SYS-905` and `INF-347` isolate
  mutable block contact, one-shot reward emission, avatar power-state change,
  shell conversion, committed scrolling, flag/time settlement and the joined
  stage-status surface.

## New combinations

- [Observation | Direct | High] No verified combination is asserted pending
  the deterministic complete subset scan recorded after index generation.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_073` generalises three stable
  existing boundaries while preserving all earlier signatures.

## New questions

- Which exact North American cartridge revision, if any, changes a scoped
  World 1-1 rule relative to the pinned Japan/USA disassembly?
- Which life, midpoint and high-score states persist across a verified second
  attempt and power cycle on original hardware?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0312` — ASTRO BOT, PlayStation 5 base
  product, under the selection-020 amended horizon.
- Optimisation criterion: contrast a fixed 1985 one-way platform stage with a
  modern PS5 platforming packet whose controller, rescue and transformation
  rules must be source-bounded independently.
- Backlog impact: `GAME-0312` remains next; no later unit starts in this commit.

## Why this game

- [Hypothesis | Direct | High] The original Super Mario Bros. tests whether a
  culturally recognisable platformer can be represented through portable
  movement, collision, block, power-state, camera and exit rules rather than
  theme, character identity or genre shorthand.

## Research checklist

- [x] original one-player NES ruleset fixed
- [x] World 1-1 entry, positive terminal, negative terminal and exclusions fixed
- [x] official manual and product record inspected
- [x] pinned deterministic source implementation inspected
- [x] complete six-type gene scan performed
- [x] lower-ID comparison and combination scan delegated to deterministic gate
- [x] direct-play and audiovisual limitations disclosed
- [x] localisation and presentation authored in the same game unit
