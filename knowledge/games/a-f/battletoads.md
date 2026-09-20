---
game_id: GAME-0318
slug: battletoads
game_title: Battletoads
analysis_status: reviewed
reviewed: 2026-09-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-295
    - ACT-348
  system:
    - SYS-045
    - SYS-215
    - SYS-578
    - SYS-911
    - SYS-915
    - SYS-916
    - SYS-917
  constraint:
    - CON-442
  information:
    - INF-119
    - INF-192
    - INF-235
    - INF-350
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Battletoads

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Ragnarok's Canyon,
Psyko-Pigs, Walker, Dragon and Tall Walker are carrier parameters rather than
separate genes.

## Analysis scope

- Version / ruleset: original North American English Nintendo Entertainment
  System cartridge `NES-8T-USA`, developed by Rare and published by Tradewest
  in June 1991. The packet covers a fresh one-player game and only Stage 1,
  `Ragnarok's Canyon`, without the opening warp, extra-life code, continue,
  emulator save state or Nintendo Classics wrapper features.
- Structured analysis target: North American licensed NES cartridge
  `NES-8T-USA`; see `GAME-0318` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: read the local canyon slice, health, lives and
  visible enemies; move on the side-view combat plane, jump or double-tap to
  run, then commit punches, kicks or a running headbutt; let hostile movement,
  contact, damage and recovery resolve in real time; clear the local group to
  release forward scrolling; optionally use a defeated Walker leg or stunned
  Dragon; then evade Tall Walker's volley, pick up its final rock and throw
  three rocks back through the boss-view screen.
- Entry: first ordinary control after the Vulture lowers the one-player Toad
  onto Ragnarok's World, with the normal three-life stock and no code active,
  before either opening Psyko-Pig is attacked.
- Positive terminal: the third returned rock destroys Tall Walker, the stage
  awards its closeout and the game reaches the first controllable `Wookie Hole`
  state with the surviving life stock and score carried into Stage 2.
- Negative terminal: the current health pool reaches zero when no life remains,
  producing the first Game Over / continue offer. Choosing Continue is outside
  the packet. Earlier deaths consume one life and restore direct control in
  the current Stage 1 combat region while the run remains viable.
- Included: direct movement, jumping, running and depth-axis alignment on the
  scrolling combat plane; character-owned punch, kick, finishing and headbutt
  attacks; real-time enemy movement and contact; health damage and fly healing;
  three starting lives and same-stage respawn; encounter-gated forward scroll;
  Walker parts as temporary hand weapons; knocking down and riding a Dragon,
  with mounted jump/flight and fire; the waterfall gap; Tall Walker's boss-view
  crosshair, volley, throwable rock and three-hit screen damage; score, health,
  life and local-stage information; transition to Stage 2.
- Excluded: the timed opening warp to Turbo Tunnel; the optional 1-Up before
  Tall Walker; farming score or lives; the five-Toad code; Continue; two-player
  play, partner damage and partner throws; Stage 2 play after first control;
  every later level and vehicle course; game completion; regional ports,
  sequels, crossover games and the 2020 reboot; Rare Replay, Nintendo Classics
  Suspend Points, rewind, online play, save states, cheats and speedrun glitches.
- Reproducible parameterisation: start the English `NES-8T-USA` one-player
  game normally; do not enter the five-Toad code; ignore the warp after the
  opening pair; move right only after each required local group is defeated;
  take or leave Walker legs and the Dragon ride as legal optional tools; cross
  the waterfall; during Tall Walker, evade each laser volley, use Button B to
  lift its final rock and return three rocks; stop when `Wookie Hole` first
  accepts normal control or at the first Game Over offer without continuing.
  Exact attack choice, score, damage, healing, optional tool use and surviving
  lives remain run parameters.
- Potential scoped modules: the opening warp, one complete no-warp game,
  two-player rules, `Wookie Hole`, `Turbo Tunnel`, Continue and licensed-wrapper
  convenience features each require their own boundary and evidence.
- Direct-play status: not conducted. No original cartridge, console, lawful
  installed wrapper, controller trace, save state or captured run was
  available. The transcribed original manual establishes product identity,
  controls, health, weapons, flies and HUD categories; two independent written
  NES guides establish the Stage 1 route, Dragon controls and Tall Walker
  terminal. No video or audio was opened, played or analysed. This is a
  source-bounded reconstruction, not a claimed playthrough or reload test.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BT-001` | The subject is the licensed June 1991 North American NES cartridge `NES-8T-USA`, not a port, sequel, crossover or reboot | Confirmed | Corroborated | High | P1, P2 |
| `BT-002` | The original controls map the pad to movement, double-tap left/right to run, A to jump and B to context-sensitive action | Confirmed | Direct | High | P1 |
| `BT-003` | Stage progression requires defeating local enemies and avoiding hazards before the next section can be traversed | Confirmed | Corroborated | High | P1, S1, S2 |
| `BT-004` | Ordinary attacks, running headbutts and finishing strikes resolve against Psyko-Pigs, Walkers and Dragons in real time | Observation | Corroborated | High | P1, S1, S2 |
| `BT-005` | A defeated Walker leaves a leg that can be picked up and used as a temporary weapon | Confirmed | Corroborated | High | P1, S1, S2 |
| `BT-006` | A Dragon can be knocked down and mounted; A controls mounted jump/flight and B breathes fire | Observation | Corroborated | High | S1, S2 |
| `BT-007` | Damage depletes a visible energy pool, a fly restores one energy segment and a lethal state consumes one life while stock remains | Observation | Corroborated | High | P1, S1, S3 |
| `BT-008` | A normal fresh game begins with three lives; the five-life code and Continue are separate excluded paths | Observation | Corroborated | High | S2, S3 |
| `BT-009` | Tall Walker switches to its own aiming view, fires a volley whose final object is a throwable rock, and breaks after three returned rocks | Observation | Corroborated | High | S1, S2, S4 |
| `BT-010` | Tall Walker's third hit closes Ragnarok's Canyon and advances to `Wookie Hole` | Observation | Corroborated | High | S1, S2, S4 |
| `BT-011` | The bounded identity joins encounter-gated brawling, defeated-enemy tool conversion and a perspective-reversed three-counter boss terminal | Strong Pattern | Corroborated | High | `BT-003`–`BT-010` |

## Basic data

- Release / origin: Rare developed *Battletoads*; Tradewest published the
  North American licensed NES cartridge in June 1991.
- Platform or physical form: English North American Nintendo Entertainment
  System cartridge `NES-8T-USA`, one player, original rules.
- Puzzle family: physics and object manipulation; tactical forecast and
  counterplay; real-time system pressure; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-20:
  - **[P1]** [transcribed original NES instruction
    manual](https://www.world-of-nintendo.com/manuals/nes/battletoads.shtml),
    for licensed product identity, controls, stage-clear framing, health,
    pick-up weapons, flies, enemy names, moves and score/energy/lives HUD.
  - **[P2]** [NES Directory cartridge
    record](https://nesdir.github.io/279710DC_USA.html), for region, catalogue
    `NES-8T-USA`, publisher, developer, release month, board and ROM-chip
    identity. The hash describes the catalogued cartridge image; no ROM was
    downloaded or executed for this research.
  - **[P3]** [Nintendo's Nintendo Classics update](https://www.nintendo.com/us/whatsnew/new-nintendo-classics-update/),
    for the current lawful catalogue availability of the original NES title;
    wrapper-only features do not enter the genome.
- Corroborating textual sources, accessed 2026-09-20:
  - **[S1]** [Bruplex's complete written NES
    guide](https://gamefaqs.gamespot.com/nes/587125-battletoads/faqs/10355),
    for Stage 1 controls, authored encounter order, Walker leg, flies, Dragon
    ride, waterfall, Tall Walker volley, three returned rocks and Stage 2
    clearance.
  - **[S2]** [M. J. Popp's written NES
    guide](https://gamefaqs.gamespot.com/nes/587125-battletoads/faqs/2968),
    independently corroborating three ordinary starting lives, the Stage 1
    route, Walker part, Dragon controls and Tall Walker's three-hit result.
  - **[S3]** [Battletoads 1991 rules and level
    record](https://battletoads.fandom.com/wiki/Battletoads_%281991%29), for
    the finite-life/Continue distinction and the separation of Ragnarok's
    Canyon, Wookie Hole and Turbo Tunnel.
  - **[S4]** [StrategyWiki's written Ragnarok's Canyon
    route](https://strategywiki.org/wiki/Battletoads/Ragnarok%27s_Canyon),
    independently corroborating the encounter sequence and three returned
    boss rocks.
- Research record: **[R1]** local preflight on 2026-09-20 found no cartridge,
  console, authorised emulator session, input trace or save. No audiovisual
  evidence was used.
- Claim IDs: `BT-001`–`BT-011`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly move, run and jump the Toad through the visible
  side-view combat plane and across the waterfall gap.
- Existing `ACT-295`: enter a legal character-owned punch, kick, finishing
  strike or running headbutt while the Toad's current pose and recovery permit.
- Existing `ACT-048`: pick up and release a reachable Walker leg or Tall
  Walker rock as a free world object. A leg is swung as the current temporary
  weapon; a boss rock is thrown back into the boss-view screen.
- Existing `ACT-348`: mount a knocked-down Dragon, directly steer its movement
  and jump/flight, use its mounted attack and remain mounted until the stage
  state removes or abandons the ride.
- Button names, exact move animations, hit values and Dragon identity are
  parameters. Claims: `BT-002`, `BT-004`–`BT-006`, `BT-009`.

### System Behaviour Genes

- Existing `SYS-045`: Psyko-Pigs, Walkers and Dragons pursue, attack and change
  position without a separate command for every step.
- Existing `SYS-215`: Toad and hostile attacks, contact, knockback, damage and
  defeat resolve continuously while movement and new attacks remain available.
- Existing `SYS-578`: hostile hits reduce one current health pool, fly contact
  restores missing health and zero health enters the life-loss transition.
- Existing, generalised `SYS-911`: a lethal Toad state consumes one finite life
  and returns the same controlled body to the current stage combat region while
  stock remains; the last loss opens Game Over instead.
- New `SYS-915`: each authored local encounter holds forward scrolling until
  its required hostile group is defeated, then releases the next canyon slice.
- New `SYS-916`: a compatible subdued hostile exposes a temporary combat
  capability: a defeated Walker yields a carryable leg, while a knocked-down
  Dragon admits a ride state with a different movement/attack vocabulary.
- New `SYS-917`: Tall Walker's live aiming cycle fires avoidable shots and then
  emits one carryable rock; throwing that rock through the boss view adds one
  crack, and the third accepted return destroys the boss and settles Stage 1.
- Resolution order: player and enemies advance; attacks and contact update
  health/defeat; fly healing or life loss resolves; defeated-body conversion
  becomes available; local hostile closure releases scrolling; Tall Walker
  replaces the ordinary view and repeats volley, rock and returned-hit
  evaluation until terminal. Claims: `BT-003`–`BT-010`.

### Constraint Genes

- Existing `CON-442`: movement, attack, object use and mounted commands begin
  only when the current Toad pose, recovery, held object or ride state makes
  that command legal. The same B button therefore attacks, snares a fly,
  handles a weapon or throws a boss rock under different current states.
- Enemy count, health values, recovery frames, attack reach, gap geometry and
  three boss hits remain parameters rather than separate constraints. Claim:
  `BT-002`, `BT-004`–`BT-006`, `BT-009`.

### Information Genes

- Existing `INF-119`: the interface exposes the controlled Toad's current
  energy state before the next damage or healing decision.
- Existing `INF-192`: the scrolling view exposes the current route slice,
  support, gap, walls and immediate forward lookahead rather than the whole
  stage.
- Existing `INF-235`: the live stage view exposes current enemies, flies,
  Walker parts, Dragon ride state, projectiles and rocks needed for local
  combat decisions.
- New `INF-350`: the Stage 1 presentation joins current energy, life stock and
  score with the visible held-weapon or mounted state; Tall Walker temporarily
  replaces the ordinary viewpoint with its crosshair, firing cue and cracked
  screen, without revealing the next exact player trajectory.
- Off-screen enemies, the timed warp and future boss shots remain hidden before
  their authored appearance. Claims: `BT-003`, `BT-005`–`BT-009`.

### Objective Genes

- Existing `OBJ-080`: clear the required authored combat route, defeat Tall
  Walker and cross the opened stage boundary into `Wookie Hole` with eligible
  run state retained. Not every optional fly, 1-Up or score opportunity is
  required, and the opening warp is excluded. Claims: `BT-003`, `BT-009`,
  `BT-010`.

### Time Genes

- Existing `TIM-003`: movement, hostile attacks, damage, healing opportunities,
  Dragon control and Tall Walker volleys resolve in real time while the player
  chooses new inputs. Pause is not a planning phase. Claims: `BT-004`–`BT-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| The opening two Psyko-Pigs occupy the current slice | Move on the combat plane and commit legal attacks | hits, knockback, health and defeat resolve live; ordinary forward progress remains held until the required pair is gone | encounter-gated brawling | `BT-003`, `BT-004` |
| A Walker is active | Defeat it with ordinary or running attacks | the Walker leaves its leg as a reachable object | enemy-to-weapon conversion | `BT-005` |
| A Walker leg lies free | Pick it up and attack | the leg becomes the current temporary striking object and changes the available hit result until it is lost or abandoned | stateful temporary weapon | `BT-005` |
| Current energy is below maximum and a fly is reachable | Press the contextual action in range | the Toad snares the fly and restores one missing energy segment | world healing without inventory | `BT-007` |
| A Dragon is flying above the combat plane | Align with its shadow and hit it | the Dragon falls into a brief eligible ride state | spatial alignment creates mount access | `BT-006` |
| The Dragon is knocked down | Jump onto it, then use A or B | control transfers to mounted movement/jump-flight and fire until the ride ends | temporary alternate control vocabulary | `BT-006` |
| Health reaches zero with another life available | Accept lethal resolution | one life is removed and direct control returns in the current Stage 1 region; transient combat state is restored | finite-life recovery, not a save reload | `BT-007`, `BT-008` |
| Health reaches zero with no life remaining | Accept lethal resolution | no replacement is created and the first Game Over / Continue offer opens | bounded negative terminal | `BT-008` |
| Tall Walker's crosshair is moving | Reposition before its firing cue | the volley resolves through the boss view and ends by creating one carryable rock | perspective-reversed attack cycle | `BT-009` |
| The emitted rock is reachable | Pick it up and throw it toward the boss view | one accepted return cracks the screen; the first two preserve the encounter | returned hostile output becomes boss damage | `BT-009` |
| Two returned rocks have cracked the screen | Evade the next volley and return its final rock | the third accepted rock destroys Tall Walker, awards closeout and advances to `Wookie Hole` | guardian-gated successor terminal | `BT-009`, `BT-010` |

## Strategic and experiential structure

- Local decision: align on the combat plane, choose ordinary attack, running
  headbutt, jump, temporary weapon or Dragon fire while hostile motion remains
  live.
- Medium horizon: preserve health and lives across encounter gates, decide
  whether the slower-scoring Walker leg or optional Dragon ride improves the
  next local relation, and avoid losing a body near the waterfall.
- Long horizon: reach Tall Walker with enough life stock to learn and complete
  its repeated volley/rock cycle, then carry the surviving stock into Stage 2.
- Reversibility: movement can be corrected while space remains; defeated
  enemies, consumed flies, lost health/lives and passed encounter gates do not
  reverse in the same run.
- Failure attribution: local hit animation, energy, life count, enemy state,
  crosshair, firing cue and cumulative screen cracks distinguish ordinary
  damage, life loss and boss progress.
- Player trust: the ordinary route fixes encounter order and the boss always
  needs three accepted returned rocks; optional tools change the route through
  those states, not the terminal predicate.

## Replay and variation

- Encounter order, route geometry and Tall Walker's three required returns are
  authored; no procedural stage generation is claimed.
- Different legal lines arise from attack choice, depth alignment, fly use,
  Walker-leg retention, Dragon riding, damage taken and surviving lives.
- The optional warp, 1-Up and score farming would change progression economy
  or route and are excluded rather than averaged into the ordinary packet.
- Typical replay motive includes score, fewer deaths or later-stage mastery;
  those goals do not replace the bounded first-stage terminal.

## Adjacent systems and history

- *Super Mario Bros.* shares direct side-scrolling movement, local lookahead,
  real-time enemies and a retained successor transition. Its World 1-1 route
  is opened by traversal and flag contact; Battletoads repeatedly locks the
  route behind local combat groups, turns defeated enemies into tools and ends
  with a boss-owned viewpoint.
- *Tank 1990* shares real-time combat, finite-life respawn and a next-stage
  boundary. Its one fixed arena feeds a bounded tank reserve around a protected
  base; Ragnarok's Canyon instead scrolls through authored encounter gates,
  direct body attacks and temporary weapon/mount conversion.
- *Brawlhalla* shares character-command attacks and recoverable life stock, but
  it settles a symmetric arena duel through blast-zone stocks. Battletoads uses
  health, authored enemies and a one-way route to a scripted guardian.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-295`, `ACT-348` | pad mapping, Toad, Walker leg, Dragon and rock are parameters |
| System Behaviour | `SYS-045`, `SYS-215`, `SYS-578`, `SYS-911`, `SYS-915`–`SYS-917` | health values, encounter roster, damage and boss cadence are parameters |
| Constraint | `CON-442` | pose, recovery, held object and ride eligibility are parameters |
| Information | `INF-119`, `INF-192`, `INF-235`, `INF-350` | HUD layout, palette, crosshair and cracks are parameters |
| Objective | `OBJ-080` | Tall Walker, three returns and `Wookie Hole` are parameters |
| Time | `TIM-003` | update cadence and pause behaviour are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `317` (`GAME-0001`–`GAME-0317`).
- Exact genome matches: none.
- Tied near matches: `GAME-0272` — Serious Sam 4 (`5 / 29 = 0.172414`); `GAME-0312` — ASTRO BOT (`5 / 29 = 0.172414`); `GAME-0313` — Tank 1990 (`5 / 29 = 0.172414`).
- Supported combination subsets: none.
- Scan date: 2026-09-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0272` — Serious Sam 4 | `ACT-008`, `SYS-215`, `SYS-578`, `INF-119`, `TIM-003` | Both directly move through live hostile combat with one visible health pool. Serious Sam 4 uses firearms, ammunition, armour, waves and an arena-clear terminal. Battletoads uses character-owned strikes, local scroll gates, finite lives, enemy-to-tool conversion and three returned boss objects before a successor stage. | Near, `0.172414` |
| `GAME-0312` — ASTRO BOT | `ACT-008`, `SYS-045`, `SYS-215`, `INF-192`, `TIM-003` | Both expose only nearby side-view route information while autonomous enemies and direct movement resolve in real time. ASTRO BOT centres platform fixtures, checkpoint recovery, persistent rescued Bots and a temporary Inflate route ability; Battletoads centres mandatory combat gates, a finite life stock, temporary hostile bodies as tools and the Tall Walker counter cycle. | Near, `0.172414` |
| `GAME-0313` — Tank 1990 | `ACT-008`, `SYS-045`, `SYS-215`, `SYS-911`, `TIM-003` | Both combine direct live combat, autonomous hostiles and a finite-life body replacement. Tank 1990 is one fixed top-down arena with a bounded enemy reserve, mutable tiles, random typed bonuses and a protected base. Battletoads is a scrolling authored route whose local groups release progress and whose defeated enemies and boss output become temporary player capabilities. | Near, `0.172414` |

### Preserved research notes

- New genes: `SYS-915`–`SYS-917` and `INF-350`.
- Classification result: `New gene`; no verified combination is expected.
- Evidence and reasoning: no lower-ID boundary holds a scrolling route behind
  repeated local combat clearance, converts a subdued hostile into either a
  carried weapon or directly ridden combat form, or turns the final object of
  a boss-view volley into the boss's own three-step damage channel.

## Taxonomy impact

- Registry changes: add three System Behaviour and one Information boundary;
  add Battletoads support to fourteen compatible existing genes.
- Taxonomy-change record: generalise `SYS-911` from controlled vehicle to
  controlled body without changing its finite-life/respawn boundary or the
  `GAME-0313` signature.
- Candidate terms affected: Ragnarok's Canyon, Psyko-Pig, Walker, Dragon,
  Tall Walker, Wookie Hole, Toad, button labels and exact numeric values remain
  product, actor, place or implementation parameters.

## Negative results

- No cartridge, console, executable, input trace, direct play, screenshot,
  video or audio evidence exists for this unit.
- The original manual does not document every Stage 1 order or exact respawn
  coordinate; those claims remain corroborated written observations rather
  than direct executable facts.
- The opening warp, five-Toad code, optional 1-Up and Continue are explicitly
  excluded, so this packet does not establish their timing, retention or later
  progression consequences.
- Turbo Tunnel's vehicle memorisation is not present in Stage 1. The Dragon is
  a temporary hostile-to-mount conversion inside the brawler route, not
  evidence for later Speeder Bike rules.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original manual establishes the licensed NES
  identity, direct controls, health, pickups, weapons and HUD categories
  (`BT-001`–`BT-004`, `BT-007`).
- [Observation | Corroborated | High] Independent written guides establish the
  Walker leg, Dragon ride and Tall Walker's three returned-rock terminal
  (`BT-005`, `BT-006`, `BT-009`, `BT-010`).

## New genes

- [Observation | Corroborated | High] `SYS-915`–`SYS-917` and `INF-350`
  isolate encounter-gated scrolling, subdued-enemy tool conversion, the
  boss-volley counter loop and the joined brawler/boss-view information state.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Corroborated | High] `SYS-911` now names the controlled body
  rather than a vehicle while preserving the already-reviewed Tank 1990 case.

## New questions

- Does a lawfully inspectable original-game code record expose the exact Stage
  1 respawn coordinates and which transient hostile states survive each lost
  life?
- Which distinct genes become necessary when `Turbo Tunnel` replaces the
  combat plane with authored high-speed obstacle memorisation?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0319` Sea of Thieves.
- Optimisation criterion: move from a fixed 1991 single-player stage to a
  current shared-world voyage with crew authority, navigation and uncertain
  hostile pressure.
- Expected information gain: test a bounded lawful-access voyage terminal and
  multi-actor ship roles against the direct-body route here.
- Backlog impact: `GAME-0319` remains next; no later unit starts in this commit.

## Why this game

- [Hypothesis | Limited | High] Battletoads is a culturally recognisable NES
  anchor whose first stage isolates the series' direct brawling, defeated-enemy
  tools and perspective-reversed boss without importing the famous later
  vehicle course.

## Research checklist

- [x] exact cartridge, one-player rules, entry and terminal declared
- [x] warp, code, Continue, later stages and wrapper features excluded
- [x] original manual separated from guide-level observations
- [x] direct-play and audiovisual limitations disclosed
- [x] complete six-type gene scan performed
- [x] deterministic lower-ID comparison and combination scan completed
- [x] reviewed Ukrainian localisation and bilingual presentation completed
- [x] original artwork and responsive browser checks completed
