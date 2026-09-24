---
game_id: GAME-0379
slug: worms-armageddon
game_title: Worms Armageddon
analysis_status: reviewed
reviewed: 2026-09-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-520
  system:
    - SYS-146
    - SYS-324
    - SYS-1030
    - SYS-1031
    - SYS-1032
    - SYS-1033
  constraint:
    - CON-686
  information:
    - INF-386
  objective:
    - OBJ-221
  time:
    - TIM-028
---

# Game: Worms Armageddon

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Damage values,
turn duration, team size and water-rise rate are parameters, not genes.

## Analysis scope

- Version / ruleset: Team17's Windows PC *Worms Armageddon* as described by
  its preserved English publisher manual, revised 2002. One non-network
  two-human-team match, configured on the Create Game screen with three worms
  per team, 100 starting energy each, no handicap or alliance, no manual worm
  selection, one required round victory, a ten-minute round clock, timed
  turns, an island above water, ordinary fall damage, and Sudden Death water
  rise enabled with energy reduction off. The admitted arsenal is unlimited
  Bazooka and Grenade only; all other editable arms, reinforcements, special
  weapons, crates and starting mines are disabled. Record the actual selected
  landscape, worm placements, wind, turn time and water-rise setting before
  replay; this analysis does not claim that this custom scheme is a factory
  default or a measured executable trace.
- Structured analysis target: the publisher-manual Windows PC ruleset for
  this explicitly configured offline match, not a later console remaster or
  network scheme. The exact disc/build and regional patch were not inspected.
- Primary decision loop: on the active team's timed turn, walk or jump its
  scheduled worm to an advantageous position, select Bazooka or Grenade, set
  aim and power (and grenade fuse/bounce), then fire. Wind and physical flight
  determine contact; an explosion damages or displaces worms and cuts eligible
  ground. The game waits for motion to settle before handing control to the
  other team. Repeated turns change firing lines, cover and survival until only
  one team has a living worm.
- Entry and exit: begin after the two configured teams and one island are
  generated, with their three worms placed and the first timed turn active.
  The positive terminal is all opponent worms dead by exhausted energy or
  drowning while at least one allied worm remains; the negative terminal is
  symmetric. The ten-minute round boundary starts Sudden Death water rise,
  not a scored draw or automatic victory. The single required round victory
  completes this match. A simultaneous-removal/draw branch is possible but
  not assigned an invented tie-breaker here.
- Included: direct local movement; one worm's committed weapon use per turn;
  ballistic projectile flight; wind-sensitive Bazooka aiming; Grenade fuse
  and bounce; impact/explosion damage and displacement; persistent combat
  terrain craters; energy loss and drowning; fixed worm rotation; visible
  terrain, energy, wind and turn time; timed alternating turns; the selected
  Sudden Death water rise; last-team-standing result.
- Excluded: Quickstart bots and adaptive difficulty, campaign missions,
  training, network/WormNET, other teams or alliances, multiple-round
  stockpiling, team-chosen special weapons, homing or multi-shot arms, remote
  strikes, utility crates, donor cards, land mines, terrain editor decisions,
  online settings, alternate Artillery mode, account statistics and remaster
  assists. The disabled content is not assumed absent from the product.
- Potential scoped modules: default/advanced weapon schemes, the single-player
  mission sequence, network tactics and multiple-round inventory economy.
- Direct-play status: none. The Team17-authored manual and publisher product
  page were reviewed, but no executable, disc, input trace, screenshot, video
  or audio of this configured match was inspected. Transition examples are
  manual-grounded rule reconstructions; exact physics, damage falloff, wind
  sequence and generated landscape require direct replication.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| WA-001 | A non-network game may use two human-controlled teams; three worms and 100 energy per worm are supported settings. | Confirmed | Direct | High | P1 pp. 30–33 |
| WA-002 | Teams take timed turns; without Worm Select the next worm is fixed, and the next turn waits for motion to settle. | Confirmed | Direct | High | P1 pp. 3, 6, 8, 33 |
| WA-003 | Players can move and jump an active worm, then aim and power a Bazooka or set a Grenade fuse/bounce and launch it. | Confirmed | Direct | High | P1 pp. 6, 10, 12, 15 |
| WA-004 | Bazooka flight is affected by wind, while explosions can hurt or displace worms and change eligible ground. | Confirmed | Corroborated | High | P1 pp. 8, 12, 15, 36; P2 |
| WA-005 | A worm dies at zero energy or by drowning; the surviving team wins. | Confirmed | Direct | High | P1 p. 2 |
| WA-006 | Round time can trigger Sudden Death; water rise and energy reduction are configurable independently. | Confirmed | Direct | High | P1 pp. 3, 33, 36 |
| WA-007 | The exact selected two-weapon scheme, projectile coefficients and outcome of any run were not directly observed. | Observation | Limited | High | P1 pp. 32–36; direct-play limit |

## Basic data

- Release / origin: Team17's *Worms Armageddon*, originally released for
  Windows PC in 1999. This packet follows the preserved Team17 manual's
  configurable PC rule set, not every subsequent version.
- Platform or physical form: local non-network Windows PC game;
  `PLAT-WINDOWS-PC`.
- Puzzle family: timed, turn-based physical artillery tactics on mutable
  terrain; the teams pursue elimination rather than a score threshold.
- **[P1]** [Team17's *Worms Armageddon* English manual, preserved as
  HTML](https://manualzz.com/doc/62252192/team17-worms-armageddon-manu%C3%A1l),
  pp. 2–3, 6, 8, 10, 12, 15, 30–36; reviewed 2026-09-24. The source text is
  publisher-authored, hosted by a third party. A [PDF from an archive of
  Team17's former FTP](https://ftp.zx.net.nz/pub/archive/ftp.team17.com/pub/t17/manuals/Worms_Armageddon.pdf)
  preserves the same manual identity.
- **[P2]** [Team17 publisher product
  page](https://www.team17.com/games/worms-armageddon), checked 2026-09-24;
  product identity and broad strategy premise, not custom-scheme detail.
- Secondary sources: none required for the admitted mechanics.
- Claim IDs: WA-001–WA-007.

## Mechanical decomposition

### Action Genes

- `ACT-008`: directly walk or jump the currently controlled worm over
  traversable ground; it is not a destination-click command.
- `ACT-520`: choose an available carried Bazooka or Grenade, set its aiming
  line and power, set grenade fuse/bounce when applicable, and commit a shot
  from the active worm's current position.
- Parameters: move duration, jump direction, firing angle, power, grenade
  fuse and bounce.
- Claim IDs: WA-002, WA-003.

### System Behaviour Genes

- `SYS-146`: advance launched projectile motion through gravity and physical
  contacts until impact or explosion; the worm is not the fixed launcher of
  `ACT-113`.
- `SYS-324`: remove eligible island soil and update collision after an
  explosion; the crater remains available as altered cover and travel space.
- `SYS-1030`: apply a resolved shot's impact or blast to worm energy and
  position, including knockback, without pretending every near miss is lethal.
- `SYS-1031`: remove a worm whose energy reaches zero or whose body enters
  lethal water; surviving team membership changes accordingly.
- `SYS-1032`: after the configured round clock expires, raise water at the
  selected Sudden Death setting; it does not instantly choose a winner.
- `SYS-1033`: use the disclosed wind direction/strength to deflect an eligible
  Bazooka shot during flight, rather than altering every weapon equally.
- Resolution order: turn input and shot commitment; projectile flight under
  gravity and eligible wind; collision/fuse event; blast, terrain removal and
  displacement; fall/energy/water deaths; motion settlement; team result or
  next turn. Sudden Death water advancement is a separate round-clock event.
- Parameters: physical coefficients, wind, damage falloff, crater size,
  waterline, blast order and settlement duration.
- Claim IDs: WA-002–WA-006.

### Constraint Genes

- `CON-686`: only the scheduled living worm acts for its team because Worm
  Select is disabled; a completed weapon use or expiring turn clock closes
  that team's current command opportunity. Walking alone need not end it.
- Scarce strategic resources: remaining turn seconds, living worm bodies,
  safe land and terrain cover. Bazooka and Grenade ammunition are unlimited in
  this configured packet; no finite-ammo gene is admitted.
- Claim IDs: WA-002, WA-003.

### Information Genes

- `INF-386`: the match view exposes the current worm, terrain, worm/team
  energy, active turn clock and wind direction/strength; it does not display
  an exact future projectile trajectory or guaranteed damage.
- Claim IDs: WA-002–WA-004.

### Objective Genes

- `OBJ-221`: leave at least one worm on the player's team alive after all
  opposing worms have been removed in the selected one-round match.
- Success, evaluation and failure: enemy elimination by zero energy or water
  with an allied survivor wins; symmetrical removal loses; the manual does not
  justify inventing a simultaneous-removal tie-breaker.
- Claim IDs: WA-005.

### Time Genes

- `TIM-028`: team command windows alternate under a live turn countdown, but
  the system finishes projectile and body motion before the next team acts.
  Reaching the separate round clock invokes Sudden Death rather than ending
  the same turn directly.
- Claim IDs: WA-002, WA-006.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Red team's scheduled worm has time left on supported soil | Walk to a different firing position and aim Bazooka | The worm's location and aiming line change while Red retains the current turn | Movement is a pre-shot tactical choice | WA-002, WA-003 |
| Red worm aims a Bazooka while wind points right | Commit one powered shot | Projectile travels with gravity and eligible wind until contact; aim alone does not promise a hit | Wind and physical flight mediate the result | WA-003, WA-004 |
| A Grenade is available and a worm stands near a soil ledge | Set fuse/bounce and launch so it settles near the ledge | Fuse expiry produces a bounded blast; eligible soil is removed and affected bodies may lose energy or be displaced | Fuse, blast and terrain are distinct transitions | WA-003, WA-004 |
| A worm is displaced into the water below the island | Let post-shot motion settle | That worm is removed even if its prior energy exceeded zero | Drowning differs from health exhaustion | WA-005 |
| A team still has living worms when the round timer expires | Continue to the next legal timed turn | Configured Sudden Death water rise advances while the match continues | Round timeout is not automatic victory | WA-006 |
| Only Red has living worms after a resolved action | Settle the final motion and evaluate team state | Red wins the one required round and the match | Last-team-standing terminal | WA-005 |

The rows are reconstructions from the manual, not measured frames or a claim
that the exact unplayed layout guarantees any illustrated shot.

## Strategic and experiential structure

- Local decision: move a worm into a line of fire while retaining enough time
  to aim and fire; compare a direct Bazooka path with a bouncing timed Grenade.
- Medium-term planning: use craters to change cover or send opponents toward
  the water, while not destroying a safe footing for one's own later worms.
- Long-term structure: no unlock or inventory economy in this one-round
  custom scheme. Preserving living worms is the continuing resource.
- Common heuristics: inspect wind before Bazooka aim; estimate grenade fuse and
  bounce; seek safer elevation when Sudden Death begins.
- Failure attribution: the energy display, terrain change and drowning are
  visible, but exact trajectory/knockback cannot be attributed to a particular
  coefficient without a recorded run.
- Player-trust factors: turn and round clocks are disclosed. Generated terrain,
  placements and changing wind must be recorded to reproduce a specific duel.
- Claim IDs: WA-001–WA-007.

## Replay and variation

- What changes between sessions: generated island, worm placement, wind,
  chosen movement/aim/fuse, terrain craters and elimination order.
- Randomness or procedural generation: island and placements may vary;
  per-turn wind sequence cannot be reconstructed without a run record.
- Multiple viable strategies: direct damage, knockback into water and
  defensive repositioning can each contribute to elimination.
- Typical replay motive: refine aiming and terrain tactics; account rank,
  campaign rewards and network competition are outside scope.
- Claim IDs: WA-002–WA-007.

## Adjacent systems and history

- Direct predecessors: earlier *Worms* games establish the series, but no
  predecessor rules are imported into this packet.
- Variants: console remasters, broad custom schemes and online matches can
  change timing, arsenal or presentation and need independent review.
- Similar games: Angry Birds Classic and PUBG: BATTLEGROUNDS contribute
  bounded projectile or destructible-ground genes, not this two-team timed
  artillery result.
- Important differences: the active worm can reposition and aim under a
  ticking team turn, while physical shots reshape the shared combat ground.
- Claim IDs: WA-001–WA-007.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-520` | Movement and aimed weapon selection |
| System Behaviour | `SYS-146`, `SYS-324`, `SYS-1030`, `SYS-1031`, `SYS-1032`, `SYS-1033` | Flight, damage, crater, water, wind |
| Constraint | `CON-686` | Scheduled worm and one committed shot per turn |
| Information | `INF-386` | Visible turn, wind and health state |
| Objective | `OBJ-221` | Last surviving team in one round |
| Time | `TIM-028` | Alternating timed windows and settled physics |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `378` (`GAME-0001`–`GAME-0378`).
- Exact genome matches: none.
- Tied near matches: `GAME-0116` — The Stanley Parable: Ultra Deluxe (`1 / 17 = 0.058824`); `GAME-0212` — Half-Life 2 (`2 / 34 = 0.058824`); `GAME-0302` — Captain Toad: Treasure Tracker (`1 / 17 = 0.058824`).
- Supported combination subsets: none.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0116` The Stanley Parable: Ultra Deluxe | `ACT-008` | Both directly navigate an avatar, but Stanley commits narrative branches by traversal; Worms positions a scheduled combat unit and resolves artillery, terrain and elimination under a turn clock. | Tied near, `0.058824` |
| `GAME-0212` Half-Life 2 | `ACT-008`, `SYS-146` | Both move an agent and resolve a physical launched body, but Half-Life 2 uses a continuous first-person Gravity Gun route with level transitions; Worms alternates team windows, wind-sensitive aimed shots, craters and last-team survival. | Tied near, `0.058824` |
| `GAME-0302` Captain Toad: Treasure Tracker | `ACT-008` | Both move one controlled character through visible geometry; Captain Toad solves a fixed diorama without jumping or combat, while Worms jumps, fires and changes a shared battlefield against another team. | Tied near, `0.058824` |

- New genes: `ACT-520`, `SYS-1030`, `SYS-1031`, `SYS-1032`, `SYS-1033`,
  `CON-686`, `INF-386`, `OBJ-221`, `TIM-028`.
- Classification result: `New gene`.
- Evidence and reasoning: the manual directly defines the timed team-turn,
  wind, water and artillery terminal. Generic navigation, ballistic flight
  and deformable combat ground transfer without changing old signatures.

### Preserved research notes

- New genes: `ACT-520`, `SYS-1030`, `SYS-1031`, `SYS-1032`, `SYS-1033`,
  `CON-686`, `INF-386`, `OBJ-221`, `TIM-028`.
- Classification result: `New gene`.
- Evidence and reasoning: the manual directly defines the timed team-turn,
  wind, water and artillery terminal. Generic navigation, ballistic flight
  and deformable combat ground transfer without changing old signatures.

## Taxonomy impact

- Registry changes: nine additive Active IDs; old signatures unchanged.
- Taxonomy-change record: `TAXONOMY_CHANGE_118`.
- Candidate terms affected: mobile artillery fire, blast knockback, drowning,
  Sudden Death water, wind and team-turn timing.

## Negative results

- `none`; no earlier accepted mechanic or combination is disproved. Disabled
  modes and weapons are exclusions, not claims that the product lacks them.

## Delta summary

## New facts

- [Confirmed | Direct | High] `WA-001`–`WA-006` establish a configurable
  offline team battle with timed turns, physical weapons and survival result.

## New genes

- [Observation | Direct | High] Nine bounded additions isolate the chosen
  game's artillery, water and timed team-turn mechanics.

## New combinations

- [Observation | Direct | High] `No new combinations` are registered by this
  unit; the existing subset registry is checked separately.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_118` records additive IDs only.

## New questions

- What exact wind and damage-falloff values does a reproduced PC build use?
- How does the original executable settle simultaneous last-worm removal?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0380` Professor Layton and the
  Curious Village, as recorded in the selected horizon.
- Optimisation criterion: alternate a physical tactics loop with a bounded
  clue-and-puzzle progression loop.
- Expected information gain: distinguish authored puzzle gating from
  player-created terrain and team elimination.
- Backlog impact: retains the remaining seven selected subjects in order.

## Why this game

- [Hypothesis | Limited | Medium] Worms Armageddon contributes a recognisable
  turn-based artillery packet and a visually different side-view battlefield
  between the preceding rolling course and the next narrative puzzle.
