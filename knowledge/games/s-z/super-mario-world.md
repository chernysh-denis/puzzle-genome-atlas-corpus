---
game_id: GAME-0354
slug: super-mario-world
game_title: Super Mario World
analysis_status: reviewed
reviewed: 2026-09-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-295
    - ACT-348
    - ACT-493
  system:
    - SYS-036
    - SYS-037
    - SYS-045
    - SYS-064
    - SYS-900
    - SYS-901
    - SYS-902
    - SYS-905
    - SYS-911
    - SYS-933
    - SYS-935
    - SYS-978
    - SYS-979
    - SYS-980
    - SYS-981
  constraint:
    - CON-068
    - CON-660
  information:
    - INF-192
    - INF-347
  objective:
    - OBJ-002
    - OBJ-164
  time:
    - TIM-003
---

# Game: Super Mario World

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Mario, Yoshi,
Yoshi's Island 2, Dragon Coins, red berries, Koopa shells, Midway Gate,
P-Switch and Goal Tape are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: original North American English Super NES release of
  *Super Mario World*, internal revision `00`, reconstructed from Nintendo's
  original instruction booklet and the pinned `U` build of the community
  disassembly at commit `30643c7595a7d097d731de69476f8059c7cf98c3`.
- Structured analysis target: one-player Yoshi's Island 2 from fresh course
  entry to its ordinary Goal Tape, with one separately reconstructed
  post-Midway lethal-fall control; see `GAME-0354` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: a fresh one-player save has cleared only Yoshi's Island 1 through its
  normal exit. Enter Yoshi's Island 2 as Small Mario with no Yoshi, no reserve
  item and Yellow Switch Palace not pressed. Preparation is outside the packet,
  and the course's dotted yellow blocks therefore remain inactive.
- Primary decision loop: read the side viewport and HUD; run, jump, spin-jump,
  carry or throw a Grab Block; hit reward blocks; hatch and mount Yoshi; eat a
  berry or eligible shell and decide whether to hold, swallow or spit its typed
  result; preserve power, Yoshi, lives and time; collect route rewards; activate
  the Midway Gate; transform the late coin path with the P-Switch; and touch the
  moving Goal Tape to settle the course.
- Fixed reproducible route: hatch the first Yoshi Egg and mount Yoshi; eat ten
  red berries to produce the reward egg and collect its Super Mushroom; ingest
  one red shell and release its three-fireball effect, then ingest and spit one
  green shell; collect all five Dragon Coins; cross the Midway Gate; use one
  spin jump on an eligible enemy or turn block; enter the optional pipe room,
  carry and throw one Grab Block and return by the right pipe; hit the block
  that releases the P-Switch, press it so the authored coins temporarily become
  solid Brown Blocks, traverse the resulting steps, and touch the Goal Tape
  while riding Yoshi. The exact legal path, enemy contacts, optional coins and
  tape height may vary.
- Positive terminal: the Goal Tape closes the course, the overworld path to
  Yoshi's Island 3 opens, and Mario begins the successor while still carrying
  the admitted power state and Yoshi. Score and tape-star height may vary and
  do not replace course completion.
- Failure and recovery control: after activating the Midway Gate, a separate
  branch sends Mario into a lethal pit. One finite life is consumed and the
  course restarts at the Midway Gate rather than its entrance. This branch is
  reset before the positive route and contributes checkpoint/life rules, not a
  claim that failure is required for completion.
- Included: direct side-view traversal; gravity and collision; enemy contact;
  jump and spin jump; portable Grab Block; mutable and reward blocks; temporary
  mushroom power; course time and finite lives; Yoshi mount, tongue, mouth-held
  shell, typed shell result and dismount; recoverable Yoshi separation after a
  hit; ten-red-berry reward; five-Dragon-Coin life award; Midway Gate; P-Switch
  coin/block exchange; Goal Tape settlement; successor route and carried Yoshi.
- Excluded: Yoshi's Island 1 play; Yellow Switch Palace; secret exits; later
  courses, castles and world completion; Cape Feather, Fire Flower as a player
  power-up, reserve-item use, Star Road, Special Zone, coloured Yoshis, baby
  Yoshis, two-player alternation, 100-coin and 100-star bonus demonstrations,
  save prompts, glitches, arbitrary code execution, speedrun techniques, ROM
  hacks, randomisers, PAL/Japanese revisions, ports and later Mario games.
- Potential scoped modules: coloured-shell wings and flight, cape traversal,
  reserve-item release, secret exits, switch-palace persistence, two-player
  alternation and save retention each require a separate bounded packet.
- Direct-play status: not conducted. No cartridge, ROM, emulator, console,
  save, controller trace, screenshot, video or audio was obtained or inspected.
  The record is a source-bounded reconstruction, not a claimed playthrough or
  byte-perfect audit of a locally executed ROM.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SMW-001` | The target is the original North American English Super NES ruleset at internal revision `00`, not a later wrapper, port or modification | Confirmed | Corroborated | High | P1, P2, R1 |
| `SMW-002` | Direct movement, jump, spin jump, carried objects, blocks, enemy contact, time, lives and side-view HUD structure ordinary course play | Confirmed | Direct | High | P1, R1 |
| `SMW-003` | Yoshi can be mounted and dismounted, extends his tongue, holds eligible shells and later swallows or expels them | Confirmed | Direct | High | P1, R1 |
| `SMW-004` | A red shell produces three fireballs while a green shell can be expelled as a projectile; shell type therefore changes the mounted result | Confirmed | Direct | High | P1, R1 |
| `SMW-005` | A hit while Mario rides Yoshi separates them and sends Yoshi running, but permits recovery before he leaves reachable space | Confirmed | Direct | High | P1, R1 |
| `SMW-006` | Eating ten red berries makes Yoshi lay an egg containing a Super Mushroom | Confirmed | Direct | High | P1, R1 |
| `SMW-007` | Five Dragon Coins in one course award one life, and Yoshi's Island 2 contains exactly five authored Dragon Coin objects | Confirmed | Corroborated | High | P1, R1 |
| `SMW-008` | The Midway Gate records a new return anchor and makes Small Mario Super when its tape is crossed | Confirmed | Direct | High | P1, R1 |
| `SMW-009` | Pressing the scoped P-Switch temporarily exchanges authored coin and Brown Block states and thereby changes late-route footing | Confirmed | Direct | High | P1, R1, S1 |
| `SMW-010` | Touching the moving Goal Tape settles the course, derives a height-based reward and carries mounted Yoshi into the unlocked successor | Confirmed | Direct | High | P1, R1 |
| `SMW-011` | Yoshi's Island 2 contains the two Yoshi blocks, berry supply, Midway Gate, optional pipe room, P-Switch, coin path, five Dragon Coins and Goal Tape used by the fixed route | Observation | Corroborated | High | R1, S1 |
| `SMW-012` | The repository control reconstructs the admitted transitions but does not execute or measure the original game | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Nintendo, Super NES, North American release 1991-08-23;
  original program developed and published by Nintendo.
- Platform or physical form: original North American English Super NES
  cartridge ruleset, not a current wrapper or emulated storefront product.
- Puzzle family: world topology and perspective; inventory and fixture
  dependencies; transformation and state-space search; real-time system
  pressure; ordered dependency sequencing.
- Primary and first-party sources, accessed 2026-09-22:
  - **[P1]** [Nintendo's original English instruction booklet
    PDF](https://www.nintendo.co.jp/clvs/manuals/common/pdf/CLV-P-SAAAE.pdf),
    for controls, blocks, Yoshi, berries, shells, Dragon Coins, lives, Midway
    Gate, Switch Block, Goal Tape, course time and successor carry.
  - **[P2]** [Nintendo's Super Famicom / SNES Classic product
    page](https://www.nintendo.co.jp/clvs/soft/mario_world.html), for the
    licensed product and original platform context; wrapper presentation is not
    imported into the target ruleset.
- Reproducible implementation source:
  - **[R1]** [SMWDisX](https://github.com/IsoFrieze/SMWDisX), pinned at commit
    `30643c7595a7d097d731de69476f8059c7cf98c3`, using the `U` revision-00
    configuration plus `106_YI2main` and `1CA_YI2sub` object/sprite sources for
    level placement and the named goal, Yoshi, berry, P-Switch, Dragon Coin and
    checkpoint routines. The repository contains no game ROM and was inspected
    as reverse-engineered source, not as a licensed executable.
- Independent route source:
  - **[S1]** [Thonky's Yoshi's Island 2 written
    route](https://www.thonky.com/super-mario-world/yoshis-island-2), for an
    independent ordered account of the egg, ten berries, shell effects,
    Midway Gate, pipe room, P-Switch route and Goal Tape.
- Reproducible control: **[V1]**
  [`verify_super_mario_world_control.py`](../../../scripts/verify_super_mario_world_control.py),
  a repository-side state reconstruction that does not execute the game.
- Claim IDs: `SMW-001`–`SMW-012`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly run and jump Mario through the authored side-view course.
- `ACT-048`: pick up, carry and release one reusable Grab Block in the optional
  pipe room.
- `ACT-295`: commit a spin jump whose contact result differs from an ordinary
  jump on eligible enemies or blocks.
- `ACT-348`: mount Yoshi, steer and jump the combined actor, and dismount while
  the companion remains available in the world.
- New `ACT-493`: command the mounted companion to extend its tongue toward one
  eligible berry, enemy or shell, ingest it, or expel a mouth-held shell.
- Claims: `SMW-002`–`SMW-004`, `SMW-011`.

### System Behaviour Genes

- `SYS-036` resolves continuous gravity, collision and moving-body contact;
  `SYS-064` distinguishes stomp from side contact; `SYS-045` advances enemies
  independently in real time; `SYS-037` collects compatible route objects.
- `SYS-900` and `SYS-901` resolve upward contact with mutable stage blocks and
  emit authored rewards; `SYS-902` applies or removes the Mushroom power state.
- `SYS-911` spends one finite life and reconstructs an attempt; `SYS-933`
  replaces the course entrance with the activated Midway Gate as return anchor;
  `SYS-935` turns the fifth Dragon Coin into one life.
- `SYS-905` settles Goal Tape contact, tape-height rewards and the successor.
- New `SYS-978` maps a mouth-held shell's type and release timing to the
  mounted result: red becomes three fireballs, green can be spat as a shell,
  and an unreleased held shell is swallowed after its timer.
- New `SYS-979` converts a hit while mounted into rider separation and Yoshi's
  recoverable autonomous escape instead of immediately applying the ordinary
  Small-Mario damage terminal.
- New `SYS-980` turns the tenth red berry eaten by Yoshi into a reward egg that
  releases a Super Mushroom.
- New `SYS-981` temporarily exchanges designated coin and solid Brown Block
  states while the P-Switch timer remains active, then restores them.
- Resolution order: input changes movement, jump, mount or tongue intent;
  collision resolves; a legal ingestion changes mouth or berry state; typed
  shell or threshold rules settle; block/contact pickups update power, coin,
  Dragon Coin and life state; checkpoint or goal contact records route state;
  time, actors and temporary switch state advance continuously.
- Claims: `SMW-002`–`SMW-011`.

### Constraint Genes

- `CON-068`: the course timer is an authoritative attempt deadline; reaching
  zero produces the same finite-life failure path as other lethal terminals.
- New `CON-660`: Yoshi's tongue can acquire only an eligible reachable target,
  and a new shell cannot occupy the mouth while another shell is held; the
  held body can be expelled only while that mouth state still exists.
- Scarce route state: remaining course time, lives, current power, Yoshi
  availability, mouth-held shell, berry count and temporary P-Switch interval.
- Claims: `SMW-003`, `SMW-004`, `SMW-006`, `SMW-008`, `SMW-009`.

### Information Genes

- `INF-192`: the side-scrolling viewport exposes local terrain, enemies,
  blocks, berries, Yoshi, coins and the moving Goal Tape while distant course
  geometry remains outside the camera.
- `INF-347`: the stage HUD exposes score, coins, time, lives, reserve and current
  power context needed to attribute reward and failure.
- Claims: `SMW-002`, `SMW-007`–`SMW-010`.

### Objective Genes

- `OBJ-164`: reach and trigger Yoshi's Island 2's Goal Tape so the course
  settles and the successor path opens.
- `OBJ-002`: voluntarily optimise score, Dragon Coins, coins, tape stars and
  retained power/Yoshi without substituting those measures for the exit.
- Success, evaluation and failure: Goal Tape contact is the positive terminal;
  lethal contact, pit or zero time spends a life and restarts at the current
  anchor; optional score and collectibles grade the route but do not replace it.
- Claims: `SMW-007`, `SMW-008`, `SMW-010`.

### Time Genes

- `TIM-003`: movement, enemies, shell holding, switch duration, goal movement
  and the course countdown resolve in shared real time.
- Claims: `SMW-002`–`SMW-005`, `SMW-009`, `SMW-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Yoshi Egg remains in its authored block | strike the block and contact the hatched companion | the egg hatches, Mario mounts and direct movement controls the combined actor | mount acquisition | `SMW-003`, `SMW-011` |
| Yoshi is mounted and nine red berries have been eaten | tongue the tenth eligible red berry | berry count resets and Yoshi lays a reward egg containing a Super Mushroom | forage threshold emits a power reward | `SMW-006` |
| Yoshi's mouth is free and a red shell is reachable | ingest the shell and release its result | the red-shell rule emits three fireballs rather than returning the shell body | type-derived mount effect | `SMW-004` |
| Yoshi's mouth is free and a green shell is reachable | ingest and expel the shell before swallow timeout | the held green shell returns as a moving projectile | held-body expulsion | `SMW-003`, `SMW-004` |
| Mario is riding Yoshi | receive one eligible hostile hit | Mario separates, Yoshi runs autonomously and can be remounted before leaving reach | recoverable mount-loss state | `SMW-005` |
| Four Dragon Coins have settled | contact the fifth course Dragon Coin | its collectible state settles and one life is added | route milestone to finite life | `SMW-007` |
| The Midway Gate is inactive | cross its tape | checkpoint state is retained and Small Mario becomes Super; a later death returns here | authored restart anchor | `SMW-008` |
| A Grab Block remains in the pipe room | pick it up, carry it and throw it | the portable block changes world position, then follows its throw/collision result | direct portable-world-object handling | `SMW-002`, `SMW-011` |
| Late authored coins and Brown Blocks are in ordinary state | press the released P-Switch | coins become temporary solid blocks and designated blocks become coins for the active interval | timed topology exchange | `SMW-009` |
| The P-Switch interval expires | wait without another switch activation | exchanged objects return to their authored ordinary states | reversible timed world state | `SMW-009` |
| Goal Tape is moving and Mario is riding Yoshi | cross the tape | height-derived reward settles, the course closes, Yoshi's Island 3 opens and Yoshi is carried onward | positive terminal and successor | `SMW-010` |
| Midway Gate is active and at least one life remains | fall into the admitted lethal pit | one life is spent and a fresh course attempt begins at the Midway anchor | finite-life checkpoint recovery | `SMW-008` |

## Strategic and experiential structure

- Local decision: choose jump versus spin jump, whether to hold or spit a shell,
  whether a berry lies safely on the route, and whether the temporary P-Switch
  steps can be crossed before restoration.
- Medium-term planning: preserve Yoshi long enough to reach ten berries, route
  through all five Dragon Coins, activate the Midway Gate and return from the
  optional pipe room without losing the mount or exhausting time.
- Long-term structure: ordinary platform movement acquires a companion whose
  mouth turns object types and forage counts into new route/combat resources;
  the course then composes checkpoint, temporary topology and exit settlement.
- Common heuristics: remount a fleeing Yoshi quickly, release a shell before it
  is swallowed when its projectile is needed, and press the P-Switch only when
  positioned to use the temporary steps.
- Failure attribution: the HUD separates time and lives; the side view shows
  pit/enemy contact, Yoshi separation and switch restoration; checkpoint return
  distinguishes a lost attempt from a reset save.
- Player-trust factors: a berry must count once, only the shell in Yoshi's mouth
  may resolve, the fifth Dragon Coin must award exactly once, and the Goal Tape
  must not erase the admitted mounted successor state.
- Claims: `SMW-002`–`SMW-012`.

## Replay and variation

- What changes between attempts: route timing, enemy phase, shell choice,
  optional pipe use, damage, coin/score total, Goal Tape height, remaining time
  and whether Yoshi and power survive to the exit.
- Randomness or procedural generation: course geometry, object placement,
  Dragon Coins, berries, checkpoint, switch and Goal Tape are authored. Enemy
  phases and interaction timing vary, but no procedural layout is claimed.
- Multiple viable strategies: Yoshi's Island 2 can be cleared without all five
  Dragon Coins, ten berries or the pipe room; they are deliberately included
  here to exercise bounded rules while Goal Tape remains the sole exit target.
- Typical replay motive: faster completion, more coins/score/stars, full Dragon
  Coins, retained Yoshi or a cleaner route. No completion-percentage gene is
  inferred from this one course.
- Claims: `SMW-006`–`SMW-011`.

## Adjacent systems and history

- Direct predecessor relation: the reviewed original *Super Mario Bros.*
  packet shares side-view traversal, blocks, power, enemies, time, lives and a
  stage goal but lacks Yoshi's mounted mouth state, Midway return anchor,
  Dragon Coin milestone and P-Switch exchange admitted here.
- Variants: Japanese, PAL and later Virtual Console, Classic Mini, Nintendo
  Switch Online and Game Boy Advance packages are not assumed mechanically
  identical. Their wrappers, revisions and added features require evidence.
- Similar games: Donkey Kong Country shares direct mounting, finite lives,
  checkpoints and collectible life milestones, but not typed ingestion or the
  coin/block exchange.
- Important difference: shell colour is not cosmetic in the mounted state. It
  selects a different system result, while mouth occupancy constrains the next
  tongue action and a hit can separate rather than immediately destroy the
  companion relationship.
- Claims: `SMW-001`, `SMW-003`–`SMW-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-295`, `ACT-348`, `ACT-493` | Mario, Yoshi, tongue length, shell and Grab Block are parameters |
| System Behaviour | `SYS-036`, `SYS-037`, `SYS-045`, `SYS-064`, `SYS-900`, `SYS-901`, `SYS-902`, `SYS-905`, `SYS-911`, `SYS-933`, `SYS-935`, `SYS-978`, `SYS-979`, `SYS-980`, `SYS-981` | berry count, shell colours, switch interval, checkpoint and reward values are parameters |
| Constraint | `CON-068`, `CON-660` | course time, reach, eligibility and mouth occupancy are parameters |
| Information | `INF-192`, `INF-347` | camera bounds and HUD styling are presentation parameters |
| Objective | `OBJ-002`, `OBJ-164` | course, tape height, score and successor identity are parameters |
| Time | `TIM-003` | frame cadence and exact timers are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `353` (`GAME-0001`–`GAME-0353`).
- Exact genome matches: none.
- Tied near matches: `GAME-0333` — Sonic the Hedgehog (`16 / 31 = 0.516129`).
- Supported combination subsets: none.
- Scan date: 2026-09-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0333` — Sonic the Hedgehog | `ACT-008`, `ACT-295`, `SYS-036`, `SYS-037`, `SYS-045`, `SYS-902`, `SYS-905`, `SYS-911`, `SYS-933`, `SYS-935`, `CON-068`, `INF-192`, `INF-347`, `OBJ-002`, `OBJ-164`, `TIM-003` | Both packets use direct side-view movement, a distinct character attack, continuous collision, live enemies, pickups, temporary power, finite lives, checkpoint return, collectible-life milestones, HUD information and a timed stage goal. Super Mario World adds direct object carrying, Yoshi mount/mouth state, typed shell and berry results, mutable reward blocks, recoverable rider separation and the P-Switch exchange; Sonic adds slope-derived momentum, recoverable rings, shields and signpost-specific rules. | Near, `16 / 31 = 0.516129` |

- New genes: `ACT-493`, `SYS-978`, `SYS-979`, `SYS-980`, `SYS-981` and
  `CON-660`.
- Classification result: New gene.
- Evidence and reasoning: existing platforming, mounting, pickup, checkpoint,
  power and goal boundaries transfer without change. No lower-ID definition
  owns a directly commanded companion mouth that holds a typed world body,
  maps its type to a mounted result, converts mounted harm into recoverable
  separation, emits a reward at a mount-consumed forage threshold, or
  temporarily exchanges two authored world-object classes.

### Preserved research notes

- New genes: `ACT-493`, `SYS-978`, `SYS-979`, `SYS-980`, `SYS-981` and
  `CON-660`.
- Classification result: New gene.
- Evidence and reasoning: existing platforming, mounting, pickup, checkpoint,
  power and goal boundaries transfer without change. No lower-ID definition
  owns a directly commanded companion mouth that holds a typed world body,
  maps its type to a mounted result, converts mounted harm into recoverable
  separation, emits a reward at a mount-consumed forage threshold, or
  temporarily exchanges two authored world-object classes.

## Taxonomy impact

- Registry changes: add six Active definitions with complete reviewed Ukrainian
  coverage; preserve every earlier ID, definition, signature and lifecycle.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_093`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_093.md).
- Candidate terms affected: record Mario, Yoshi, berry, shell colours, Dragon
  Coin, Midway Gate, P-Switch, Brown Block, Goal Tape and level identifiers as
  carrier parameters rather than taxonomy labels.

## Negative results

- No generic “platformer”, “mascot”, “power-up”, “secret” or “companion” gene
  is created. Each admitted new boundary owns a reproducible transition.
- `SYS-935` already permits a parameterised route-collectible threshold and
  therefore owns five Dragon Coins to one life without a Mario-specific gene.
- `SYS-901` and `SYS-902` already own reward-block emission and temporary avatar
  power; the Mushroom reward itself is not new.
- `SYS-655` is rejected: mounted damage does not spend a protective capacity in
  sequence but creates a recoverable separated actor state.
- No flight or coloured-Yoshi capability is admitted; the fixed route uses only
  ordinary green Yoshi and red/green shells.
- No direct-play, ROM hash, input timing, screenshot, video, audio, port parity,
  save retention, secret exit or whole-game completion is claimed.

## Delta summary

## New facts

- [Confirmed | Direct | High] The bounded Yoshi's Island 2 route composes a
  mouth-held typed object, forage threshold, recoverable rider separation,
  checkpoint, collectible-life threshold and temporary topology exchange
  before its Goal Tape (`SMW-003`–`SMW-011`).

## New genes

- [Observation | Corroborated | High] Add `ACT-493`, `SYS-978`, `SYS-979`,
  `SYS-980`, `SYS-981` and `CON-660` under
  `TAXONOMY_CHANGE_093`.

## New combinations

- [Observation | Direct | High] No verified combination is registered from one
  new carrier.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_093` isolates the six
  new mounted-companion and temporary-world-state boundaries while leaving all
  existing signatures unchanged.

## New questions

- Which later packet best tests Yoshi's coloured-shell flight and reserve-item
  release without importing full-game completion?
- Does another reviewed mount game reuse the recoverable separation boundary
  once its source evidence is tightened?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0355` — *Metroid Prime*, original North
  American GameCube ruleset and the bounded route recorded in selection 025.
- Optimisation criterion: contrast retained first-person ability gating with
  this side-view mounted-object and temporary-topology packet.
- Expected information gain: high across lock-on navigation, scan information,
  three-dimensional ability gates and retained world-state progression.
- Backlog impact: continue research selection 025 without changing its order.

## Why this game

- [Hypothesis | Limited | High] Super Mario World adds a historically
  recognisable companion-mediated object state and a compact reversible world
  transformation while retaining a close, explainable relation to the original
  Super Mario Bros. packet.
