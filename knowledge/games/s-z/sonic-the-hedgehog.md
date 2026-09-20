---
game_id: GAME-0333
slug: sonic-the-hedgehog
game_title: "Sonic the Hedgehog"
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-295
  system:
    - SYS-036
    - SYS-037
    - SYS-045
    - SYS-215
    - SYS-755
    - SYS-902
    - SYS-905
    - SYS-911
    - SYS-933
    - SYS-935
    - SYS-947
    - SYS-948
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

# Game: Sonic the Hedgehog

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Sonic, Green Hill,
rings, lampposts and signposts are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: original North American English Sega Genesis launch
  cartridge, `REV00`, with the unmodified retail behaviour represented by the
  pinned disassembly configuration `Revision = 0`, `FixBugs = 0`.
- Structured analysis target: physical Sega Genesis cartridge; see
  `GAME-0333` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Scenario: a fresh one-player game from the title screen through `Green Hill
  Zone Act 1`, without Debug Mode, Continue or prior checkpoint state.
- Entry: press Start at the title screen; the first retained decision frame is
  Sonic standing at the authored beginning of Green Hill Zone Act 1 with zero
  rings and the initial finite life stock.
- Primary decision loop: read the side-view route, timer, rings and nearby
  threats; accelerate, brake, jump or enter a moving roll; carry retained
  ground momentum over slopes, loops and gaps; collect rings and optional
  monitor states; spin into eligible enemies and monitors; activate the
  lamppost; recover after compatible damage by recollecting scattered rings;
  cross the signpost before the ten-minute deadline.
- Positive terminal: Sonic crosses the Act 1 signpost; ordinary control and
  time lock, elapsed-time and retained-ring bonuses settle, and Green Hill
  Zone Act 2 begins with eligible run state retained. Act 2 itself is outside
  the packet.
- Failure terminals: compatible hostile contact at zero rings and without a
  shield, crushing or other declared lethal hazards, falling beyond the stage
  boundary, or `TIME OVER` consumes one finite life and returns Sonic at the
  current start/lamppost anchor while lives remain; exhausting that stock
  reaches Game Over.
- Included: direct left/right travel; acceleration, braking, jumping and
  moving roll; authored slopes, loops, springs, platforms and pits; local
  enemies; spin contact; rings; compatible hit, knockback, ring scatter,
  bounded recollection and grace; Shield, Power Sneakers and invincibility
  monitor states when encountered; breakable monitors; one lamppost; elapsed
  timer and ten-minute deadline; one-hundred-ring extra life if reached;
  signpost settlement and Act 2 handoff.
- Reproducible parameterisation: follow any successful Green Hill Zone Act 1
  route that activates the lamppost, retains or recollects at least one ring
  after one compatible hit, and crosses the signpost before ten minutes.
  Exact ring count, score, elapsed time, enemy contacts, monitor route and
  acceleration profile are bounded parameters. The canonical transitions are
  source-proven; no direct-play trace is claimed.
- Excluded: Green Hill Acts 2–3; every later zone; bosses; Special Stages and
  Chaos Emeralds; Continue screen; secret ending; Debug Mode; cheats; two-
  player play; later Genesis revisions except where a source file is invariant;
  Master System/Game Gear versions; Sonic Origins, Genesis Mini wrapper rules,
  emulation features, save states, ports, remakes and sequels.
- Potential scoped modules: one fifty-ring giant-ring/Special Stage packet,
  one underwater Labyrinth packet, one boss packet and each later edition or
  revision require independent entry, loop, terminal and evidence boundaries.
- Direct-play status: not conducted. No cartridge, console, ROM, emulator,
  screenshot, video, audio, save or input trace was used. The preserved
  official manual establishes player-facing rules; the pinned deterministic
  reverse-engineered disassembly establishes exact transitions. This is a
  source-bounded reconstruction, not a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SON-001` | The packet is the original one-player North American Genesis cartridge and fresh Green Hill Zone Act 1, not a modern wrapper | Confirmed | Direct | High | P1, P2, P3 |
| `SON-002` | Left/right input accelerates or brakes a continuously simulated body; jumping and a moving down input enter spin states | Confirmed | Direct | High | P1, P3 |
| `SON-003` | Surface angle changes retained ground inertia, with different walking and rolling resistance and low-speed detachment from steep surfaces | Confirmed | Direct | High | P3 |
| `SON-004` | Ring contact increments the visible reserve and first crossings of 100 and 200 grant finite lives without subtracting rings | Confirmed | Direct | High | P1, P3 |
| `SON-005` | Compatible damage with rings clears the reserve, emits at most 32 recoverable ring bodies, knocks Sonic away and starts grace; compatible damage at zero rings is lethal | Confirmed | Direct | High | P1, P3 |
| `SON-006` | Shield consumes itself before rings, while Power Sneakers and invincibility temporarily alter movement or contact capability | Confirmed | Direct | High | P1, P3 |
| `SON-007` | A lamppost stores a return position and stage time; later finite-life return resumes there with zero rings | Confirmed | Direct | High | P1, P3 |
| `SON-008` | Ten elapsed act minutes cause TIME OVER and one lost life | Confirmed | Direct | High | P1, P3 |
| `SON-009` | Crossing the signpost locks ordinary play and timer, converts elapsed-time tier and retained rings into score, then advances to Act 2 | Confirmed | Direct | High | P1, P3 |
| `SON-010` | The repository trace admits only transitions causally available in the fixed Act 1 packet | Observation | Direct | High | P1–P3, V1 |

## Basic data

- Release / origin: Sonic Team / SEGA; original North American Genesis release
  1991-06-23. SEGA's current historical page identifies the first title as a
  1991 release; the exact scoped region/date is pinned by the original manual
  and `REV00` cartridge reconstruction.
- Platform or physical form: one-player North American Sega Genesis cartridge,
  original launch revision.
- Puzzle family: physics and object manipulation; traversal and timing;
  real-time pressure.
- Primary sources, accessed 2026-09-21:
  - **[P1]** [SEGA's preserved original North American Genesis manual](https://manuals.sega.com/genesismini/pdf/SONIC_THE_HEDGEHOG.pdf),
    for cartridge identity, one-player controls, spin, rings, damage, lives,
    time limit, lampposts, monitors, score and zone/act progression.
  - **[P2]** [SEGA's Sonic Origins historical title page](https://asia.sega.com/SonicOrigins/en/about/),
    for original-title identity and 1991 release history, not for wrapper rules.
  - **[P3]** [Sonic Retro deterministic Sonic 1 disassembly at commit `064e3c68`](https://github.com/sonicretro/s1disasm/tree/064e3c68eb19cc85b8801b087f9d95f9b3e82cea),
    rebuilt conceptually as `Revision = 0`, `FixBugs = 0`; `_incObj/01 Sonic.asm`
    establishes movement, roll and slope response; `_incObj/Sonic
    ReactToItem.asm` and `_incObj/25, 37 Rings.asm` establish damage, ring loss,
    recovery and life thresholds; `_incObj/79 Lamppost.asm` establishes return
    state; `_incObj/0D Signpost.asm` establishes act settlement. This is a
    reverse-engineered deterministic reconstruction, not original source code.
- Validation source:
  - **[V1]** repository-side transition reconstruction from P1–P3; rules
    reasoning only, with no direct play or audiovisual evidence.
- Claim IDs: `SON-001`–`SON-010`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: steer Sonic left/right and commit jumps through traversable local
  geometry rather than selecting an automatic destination.
- Revised `ACT-295`: commit a jump-spin or grounded moving roll as a directly
  controlled character-owned attack state.
- Claims: `SON-002`, `SON-003`.

### System Behaviour Genes

- `SYS-036`: continuously integrate velocity, gravity, support and collision
  for Sonic, enemies and loose rings while live time runs.
- `SYS-037`: ring and eligible monitor-reward contact immediately credits the
  corresponding reserve or state without ending the act.
- `SYS-045`: local enemies traverse authored patterns without a command for
  every step.
- `SYS-215`: resolve legal spin contact, hostile contact, damage, knockback and
  enemy defeat in live time.
- `SYS-755`: accepted spin contact breaks an eligible monitor and resolves its
  contained power-up.
- Revised `SYS-902`: Shield, Power Sneakers and invincibility grant bounded
  capability states whose timer or next compatible hit removes them.
- Revised `SYS-905`: signpost contact locks the route, converts current act
  measures into score and hands retained run state to the successor act.
- `SYS-911`: a lethal state spends one finite life and replaces Sonic at the
  active return anchor while lives remain.
- Revised `SYS-933`: activating the lamppost replaces the intra-act return
  anchor and records the declared time/position state without requiring a
  breakable fixture.
- Revised `SYS-935`: reaching the first 100- and 200-ring milestones awards
  one life each without subtracting the ring counter.
- New `SYS-947`: continuously couple retained ground inertia to current surface
  angle, changing ascent resistance, downhill acceleration, roll friction and
  low-speed attachment across slopes and loops.
- New `SYS-948`: compatible damage turns a positive ring reserve into zero plus
  at most 32 recoverable live ring bodies, knockback and temporary grace;
  compatible zero-ring damage becomes lethal.
- Resolution order: controller input updates acceleration, jump or roll state;
  surface angle and current pose update inertia; physics and autonomous actors
  advance; contact resolves collection, attack, monitor or damage precedence;
  lethal state reaches life/anchor handling; signpost contact stops act time
  before bonus settlement and successor transfer.
- Claims: `SON-002`–`SON-009`.

### Constraint Genes

- `CON-068`: Green Hill Zone Act 1 must reach the signpost before ten elapsed
  game-minutes or TIME OVER consumes a life.
- Scarce route state: time, rings, shield state, speed, surface attachment,
  jump arc, lives and recoverable loose-ring lifetime.
- Claims: `SON-005`, `SON-008`.

### Information Genes

- `INF-192`: the side-view camera exposes local ground, slopes, loops, springs,
  rings, monitors, enemies, pits and the immediate travel corridor while future
  route remains off-screen.
- Revised `INF-347`: the stage HUD exposes score, elapsed act time, current
  rings and finite lives; world sprites expose compatible temporary states,
  checkpoint activation, damage grace and signpost closure.
- Claims: `SON-002`–`SON-009`.

### Objective Genes

- `OBJ-002`: score remains an explicit evaluation channel from enemies, rings,
  elapsed-time tier and act settlement without replacing stage clearance.
- `OBJ-164`: cross the Green Hill Zone Act 1 signpost and carry eligible run
  state into Act 2 before life stock or time failure ends the attempt.
- Claims: `SON-004`, `SON-009`.

### Time Genes

- `TIM-003`: locomotion, enemies, timer, loose rings, contacts, damage and
  temporary states continue in real time between local commands.
- Claims: `SON-002`–`SON-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Sonic stands on level ground | hold right, release, brake or reverse | ground inertia accelerates, coasts or decelerates under the active movement constants | retained ground velocity | `SON-002` |
| Sonic carries positive inertia onto a slope or loop | continue, jump or roll | surface angle adds resistance or acceleration and converts ground inertia into oriented motion; insufficient steep-surface speed can detach | angle-coupled momentum | `SON-003` |
| Sonic contacts one ring | continue moving through it | the ring disappears, the visible counter increments and the act continues | contact reserve | `SON-004` |
| Sonic has rings and no shield | touch one compatible damaging enemy/hazard | ring count becomes zero, at most 32 ring bodies scatter, Sonic is knocked away and flashes temporarily | recoverable hit loss | `SON-005` |
| One scattered ring has become collectable before despawn | steer into it | contact restores a positive ring reserve, so a later compatible hit is no longer immediately lethal | bounded recovery loop | `SON-005` |
| Sonic has zero rings and no shield | touch one compatible damaging enemy/hazard | the body enters death instead of ring loss | zero-reserve lethality | `SON-005` |
| A Shield monitor is broken | contact its released state, then take one compatible hit | the shield clears before the ring reserve; knockback/grace still settle | temporary protection precedence | `SON-006` |
| A lamppost has not been activated | pass its trigger | the return anchor, position and stage time are recorded | intra-act checkpoint | `SON-007` |
| Sonic dies after that lamppost with lives left | allow death settlement | one life is removed and Sonic returns near the lamppost with stored time but zero rings | checkpoint reset boundary | `SON-007` |
| The act timer reaches ten minutes | allow the next time check | TIME OVER invokes the finite-life failure path | hard attempt deadline | `SON-008` |
| Sonic reaches the Act 1 signpost in time | cross its trigger | timer and ordinary route lock; elapsed-time tier and rings become score bonuses; Act 2 follows | stage settlement | `SON-009` |

## Strategic and experiential structure

- Local decision: trade acceleration, braking, roll and jump timing against
  visible slope geometry, enemies, rings and hazards.
- Medium-term planning: preserve enough speed for loops and gaps while keeping
  at least one ring or shield before uncertain contact, then use the lamppost
  as the current failure anchor.
- Long-term structure: finish the authored act quickly enough for a time bonus
  and before TIME OVER, carrying lives and score into the successor act.
- Common heuristics: enter descents with room to accelerate; roll only when
  existing speed and terrain help; keep one ring; recollect the first safe
  scattered ring rather than chase every lost ring; favour survival over an
  optional score route.
- Failure attribution: the visible route, ring reserve, elapsed timer, contact
  and post-hit grace distinguish mistimed movement from depleted protection.
- Player-trust factors: the same surface-angle and reserve transitions are
  applied consistently, while off-screen route, enemy timing and lost-ring
  despawn still require bounded prediction.
- Claims: `SON-002`–`SON-010`.

## Replay and variation

- What changes between sessions: route, speed profile, ring total, elapsed
  time, score, monitor use, enemy contact and post-hit recovery.
- Randomness or procedural generation: none admitted for stage geometry; Green
  Hill Zone Act 1 and its objects are authored. Small runtime timing variation
  follows input and simulation state rather than procedural layout.
- Multiple viable strategies: safe upper/lower route choices and careful
  jumping versus speed-preserving roll/loop lines can all reach the signpost.
- Typical replay motive: faster settlement, higher score, more retained rings,
  fewer lost lives or a cleaner momentum line.
- Claims: `SON-003`–`SON-010`.

## Adjacent systems and history

- Direct predecessors: earlier side-view platform games supply running,
  jumping, collectibles, enemies and lives; this packet's distinct test is
  continuous surface-angle momentum plus recoverable ring-buffer damage.
- Variants: `REV01`, Master System/Game Gear Sonic, sequels, ports and modern
  wrapper modes require separate identity and transition checks.
- Similar games: original Super Mario Bros., Crash Bandicoot and Donkey Kong
  Country share direct movement, live enemies, collectibles, temporary states,
  lives and stage handoff.
- Important difference: Sonic's retained inertia is continuously transformed
  by slope angle and roll state, while compatible damage converts the entire
  positive ring reserve into a short-lived recoverable world field.
- Claims: `SON-001`–`SON-010`.

## Normalised genome

The front matter is canonical. The complete signature contains 18 Active
genes: two Action, twelve System Behaviour, one Constraint, two Information,
two Objective and one Time gene. Carrier labels remain parameters.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `332` (`GAME-0001`–`GAME-0332`).
- Exact genome matches: none.
- Tied near matches: `GAME-0311` — Super Mario Bros. (`12 / 26 = 0.461538`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0311` — Super Mario Bros. | `ACT-008`, `SYS-036`, `SYS-037`, `SYS-045`, `SYS-902`, `SYS-905`, `CON-068`, `INF-192`, `INF-347`, `OBJ-002`, `OBJ-164`, `TIM-003` | Both directly traverse an authored side-view level under live enemies, collectibles, temporary capabilities, a hard timer, finite lives, local route information and a scored stage-to-stage handoff. Mario commits passed terrain, changes ordered body forms, reveals block rewards and turns a stomped walker into a shell; Sonic permits backtracking, continuously couples inertia to slope angle, attacks by spinning and converts the whole ring reserve into recoverable world objects after damage. | Near, `12 / 26 = 0.461538` |

## Taxonomy impact

`TAXONOMY_CHANGE_077` generalises `ACT-295`, `SYS-902`, `SYS-905`, `SYS-933`,
`SYS-935` and `INF-347` while preserving every earlier carrier and signature.
`SYS-947` and `SYS-948` remain new because generic body physics does not own
surface-angle ground inertia, and generic damage/health does not turn the
entire reserve into recoverable live world objects.

## Negative results

- No verified combination is registered from one new carrier.
- No cartridge, console, ROM, emulator, direct play or audiovisual evidence is
  claimed.
- `REV01`, ports and wrappers do not support this exact signature without a
  separate parity review.
- The fifty-ring giant-ring rule is evidenced but excluded because Special
  Stage entry and its terminal are outside the Act 1 packet.
- Exact frame-perfect routes, object-slot exhaustion, retail bugs and hidden
  timing exploits are not promoted into genes.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original manual and pinned disassembly close
  the Act 1 movement, ring, hit, checkpoint, deadline and signpost transitions.
- [Observation | Direct | High] The bounded packet reaches Act 2 without
  importing Special Stage, later-zone, boss or modern-wrapper rules.

## New genes

- [Confirmed | Direct | High] `SYS-947` isolates surface-angle momentum and
  roll-dependent resistance.
- [Confirmed | Direct | High] `SYS-948` isolates positive-ring conversion into
  bounded recoverable world objects and zero-ring lethality.

## New combinations

- [Observation | Direct | High] None; recurrence remains evidence-driven.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_077` generalises six lower-ID
  boundaries without changing any earlier signature.

## New questions

- Which later platformer independently reproduces the same whole-reserve-to-
  recoverable-world-objects damage boundary?
- Does a separately scoped Special Stage packet require a rotating-frame
  navigation gene rather than reusing this act's world physics?

## Next recommended game

- No `GAME-0334` subject is reserved. Close and review the completed 325–333
  horizon before selecting another nine-game batch.

## Why this game

- Sonic is a recognisable Genesis anchor whose decisive causal structure is
  not theme or speed alone: surface angle transforms retained momentum, and a
  positive ring reserve can be scattered then partially recovered after harm.

## Completion checklist

- [x] Exact original product, revision, act, entry, terminal and exclusions declared.
- [x] Official manual and deterministic reconstruction evidence separated.
- [x] Momentum, ring buffer, checkpoint, deadline and act settlement decomposed.
- [x] Deterministic indexes, comparison and taxonomy artifacts regenerated.
- [x] Reviewed Ukrainian, presentation, platform, families, salience and plain language integrated.
- [x] Original artwork and responsive variants integrated.
- [x] Repository, localisation, build, browser and accessibility gates passed.

## Search-demand continuation

The unit fulfils the ninth and final reserved subject in
[`SEARCH_DEMAND_GAME_SELECTION_022`](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_022.md).
No later research unit starts implicitly after this horizon closes.
