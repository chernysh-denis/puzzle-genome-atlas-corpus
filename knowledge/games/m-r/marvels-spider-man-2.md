---
game_id: GAME-0323
slug: marvels-spider-man-2
game_title: "Marvel’s Spider-Man 2"
analysis_status: reviewed
reviewed: 2026-09-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-161
    - ACT-190
    - ACT-419
    - ACT-479
  system:
    - SYS-036
    - SYS-215
    - SYS-369
    - SYS-380
    - SYS-578
    - SYS-705
    - SYS-706
    - SYS-749
    - SYS-927
    - SYS-928
  constraint:
    - CON-269
    - CON-282
    - CON-402
  information:
    - INF-115
    - INF-119
    - INF-125
    - INF-268
    - INF-318
  objective:
    - OBJ-190
  time:
    - TIM-003
---

# Game: Marvel’s Spider-Man 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Hero, mission,
ability, hostile and reward labels are parameters, not gene names.

## Analysis scope

- Version / ruleset: English PS5 Standard Edition launch base game released on
  2023-10-20, fresh single-player save, default `Amazing` difficulty and
  default controls. No pre-order or Digital Deluxe early-unlock bonuses are
  admitted, and no installed build or patch number was observed.
- Structured analysis target: licensed PS5 Standard Edition base game and only
  the first main-story mission, `Surface Tension`; see `GAME-0323` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: swing and jump as Peter toward Sandman; dodge debris,
  pull and throw reachable loose objects, damage and web the boss until a Web
  Strike advances the encounter; escape the office, rescue the civilian and
  defeat the sand minions with direct attacks and Spider Barrage; accept the
  authored handoff to Miles, pursue with web traversal, use Venom Punch and
  Finishers against another group, deploy Web Wings through the debris chase;
  accept the return to Peter and settle the final minions and boss strike.
- Entry: first ordinary control of Peter after the opening school cutscenes,
  before travelling to the Financial District objective marker.
- Positive terminal: the final contextual attack defeats Sandman, the mission
  settles and awards the reported 1,900 XP, the post-mission cutscene completes
  and the save advances to the ordinary successor campaign state.
- Negative terminal: lethal health loss restores the latest accepted authored
  checkpoint. Stopping after a hero handoff, minion group, chase or earlier
  Sandman phase does not satisfy the packet.
- Included: direct third-person movement; jumping, tethered web swinging,
  point zips and Web Wings; real-time melee and web attacks; dodge and prompted
  Finishers; Spider Barrage and Venom Punch; finite ability readiness; visible
  health and recovery opportunity; contextual pull/throw of loose objects;
  scripted civilian rescue; authored Peter/Miles control handoffs; finite sand-
  minion groups; ordered tutorial/objective gates; boss health, web restraint
  and Web Strike phase changes; checkpoint restoration and fixed mission XP.
- Excluded: player-selected open-world hero switching; later `One Thing at a
  Time` content; free exploration, districts, crimes, activities, fast travel,
  suits, gadgets, skill purchases, collectibles, photo mode and New Game+;
  pre-order early Web Grabber/skill-point unlocks; Digital Deluxe content,
  accessibility modifiers, later updates, PC release and the complete story.
- Reproducible parameterisation: begin a fresh Standard Edition save with no
  entitlement bonuses, retain Amazing difficulty and default controls, follow
  every current objective marker, perform the prompted dodge, object throw,
  Web Strike, Spider Barrage, Venom Punch, Finisher and Web Wings lessons, clear
  only groups required to reopen the authored route, and accept each forced
  handoff. Damage, exact attack order, optional extra hits and checkpoint use
  may vary; ordered gates, control recipient, final boss settlement and 1,900
  XP do not.
- Potential scoped modules: open-world selected hero switching, gadget and
  skill-tree development, neighbourhood activities, performed checkpoint
  reload comparison, another difficulty, accessibility assists, later missions
  and the PC edition each require independent boundaries.
- Direct-play status: not conducted. No PS5 console, installed application,
  save, controller trace, screenshot, video or audio was found or opened.
  PlayStation establishes product, two-hero and opening identity; two current
  written routes corroborate the bounded mission. This is a source-bounded
  reconstruction, not a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SM2-001` | PlayStation released the single-player PS5 Standard Edition base game on 2023-10-20 | Confirmed | Direct | High | P1, P2 |
| `SM2-002` | The game directly controls Peter and Miles and combines web swinging, jumping and Web Wings traversal | Confirmed | Direct | High | P1, P3 |
| `SM2-003` | The opening was deliberately authored around both protagonists and the scaled Sandman encounter | Confirmed | Direct | High | P4 |
| `SM2-004` | `Surface Tension` begins after the opening cutscenes with Peter travelling to the objective and ends after the final Sandman strike for 1,900 XP | Observation | Corroborated | High | S1, S2 |
| `SM2-005` | The mission repeatedly requires damage plus web restraint before a contextual Web Strike advances Sandman's phase | Observation | Corroborated | High | S1, S2 |
| `SM2-006` | Peter escapes the office, rescues a civilian, defeats minions and uses Spider Barrage before authored control passes to Miles | Observation | Corroborated | High | S1, S2 |
| `SM2-007` | Miles uses Venom Punch and Finishers, then the route returns through a mandatory Web Wings chase and later restores Peter control | Observation | Corroborated | High | S1, S2 |
| `SM2-008` | Accessibility can modify combat timing, chase and game speed, but this packet freezes defaults rather than treating optional assists as base transitions | Confirmed | Direct | High | P5 |
| `SM2-009` | No installed build, direct play, checkpoint reload or audiovisual evidence was used | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Insomniac Games / Sony Interactive Entertainment; PS5
  release 2023-10-20.
- Platform or physical form: English licensed PS5 Standard Edition digital base
  game, fresh single-player save, default Amazing difficulty.
- Puzzle family: world topology and perspective; physics and object
  manipulation; tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-20:
  - **[P1]** [official PlayStation product page](https://www.playstation.com/en-us/games/marvels-spider-man-2/),
    for PS5 identity, release date, single-player scope, both protagonists,
    web traversal and accessibility summary.
  - **[P2]** [PlayStation Standard Edition and launch announcement](https://blog.playstation.com/2023/06/16/marvels-spider-man-2-arrives-only-on-ps5-october-20-collectors-and-digital-deluxe-editions-detailed/),
    for the Standard/Digital Deluxe/pre-order boundaries and launch date.
  - **[P3]** [official traversal and open-world details](https://blog.playstation.com/2023/09/14/marvels-spider-man-2-new-state-of-play-trailer-gameplay-details/),
    for web swinging, Web Wings and the wider two-protagonist distinction.
  - **[P4]** [official opening-sequence interview](https://blog.playstation.com/2023/10/20/marvels-spider-man-2-launch-interview-bryan-intihar-on-the-games-opening-sequence-asl-accessibility-options-and-more/),
    for the first 20–30 minutes, two-hero design and Sandman opening.
  - **[P5]** [official accessibility features](https://support.insomniac.games/hc/en-us/articles/46730041467027-What-Accessibility-options-does-Marvel-s-Spider-Man-2-feature),
    for optional damage, timing, chase and game-speed modifiers excluded from
    the default packet.
- Corroborating textual sources, accessed 2026-09-20:
  - **[S1]** [Push Square `Surface Tension` walkthrough](https://www.pushsquare.com/guides/marvels-spider-man-2-surface-tension),
    for the ordered Peter/Miles route, attacks, rescue, Web Wings, terminal and
    1,900 XP.
  - **[S2]** [GameSurve `Surface Tension` walkthrough](https://www.gamesurve.com/post/surface-tension-walkthrough-in-spider-man-2),
    for independent objective, ability, handoff, chase and reward corroboration.
- Research record: **[R1]** local 2026-09-20 preflight found no PS5 client,
  installed application, save or trace; no direct play or audiovisual evidence.
- Claim IDs: `SM2-001`–`SM2-009`.

## Mechanical decomposition

### Action Genes

- `ACT-008` owns ordinary ground movement, jumps and short traversal steps;
  new `ACT-479` owns momentum-preserving web swings and Web Wings travel.
- `ACT-161` owns direct strikes and web attacks; `ACT-190` the prompted Spider
  Barrage and Venom Punch abilities; `ACT-419` a prompted Finisher; `ACT-048`
  the contextual acquisition and release of a reachable loose object.
- No `ACT-228`: every control transfer in this mission is authored, not selected
  by the player. Claims: `SM2-002`–`SM2-007`.

### System Behaviour Genes

- `SYS-036` resolves momentum, gravity and collision; `SYS-215` live combat;
  `SYS-578` health loss and compatible recovery; `SYS-380` typed ability
  effects; `SYS-705` pull/hold physics; `SYS-706` thrown-object impact;
  `SYS-749` finite minion groups; and `SYS-369` checkpoint restoration.
- New `SYS-927` transfers authority at authored Peter/Miles beats without a
  player-selected switch. New `SYS-928` joins boss damage and restraint to the
  contextual Web Strike that changes phase or ends the encounter.
- Resolution order: traversal and debris physics continue; attacks, abilities
  and thrown objects update hostile and hero state; required minions settle;
  boss damage/restraint exposes a strike; fixed mission beats transfer control;
  the last strike settles completion and reward. Claims: `SM2-004`–`SM2-009`.

### Constraint Genes

- `CON-269` gates abilities by current target, range and readiness; `CON-282`
  orders mission, rescue, handoff and boss phases; `CON-402` prevents route
  continuation while the current required minion group remains live.
- Swing anchors, Web Wings clearance, Finisher reach and contextual object
  eligibility are parameters of the owning actions/systems, not extra genes.

### Information Genes

- `INF-115` exposes local threats and attack cues; `INF-119` health and ability
  readiness; `INF-125` the authored marker and gate state; `INF-268` the
  current tutorial command; and `INF-318` Sandman's phase health/progress.
- The packet does not infer hidden future attacks or free-switch availability.

### Objective Genes

- New `OBJ-190` owns the complete dual-protagonist opening mission from Peter's
  first control through Sandman's final contextual defeat, 1,900 XP settlement
  and retained successor state. One handoff or phase is insufficient.

### Time Genes

- `TIM-003` owns simultaneous traversal, debris, attacks, minion pressure,
  health changes and ability timing. Tutorial pauses do not make combat turn-
  based.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Peter has first ordinary control | Follow the Financial District marker by swing and jump | momentum and collision move Peter toward the authored encounter | web traversal is directly controlled | `SM2-002`, `SM2-004` |
| Sandman is in the first active phase | Dodge debris, throw a loose object and attack/web him | damage and restraint progress until Web Strike is exposed | physical objects and web state contribute separately | `SM2-005` |
| Web Strike is exposed | Commit the contextual strike | the current boss phase settles and the route moves to its authored location | boss progress is phase-gated | `SM2-005` |
| Peter is thrown into the office | Traverse the escape and accept the rescue interaction | the civilian is delivered and the first sand-minion gate becomes active | rescue precedes combat continuation | `SM2-006` |
| Spider Barrage is ready during the required group | Activate it against a legal target | its typed damage/control resolves and the finite group can settle | tutorial ability is mechanically causal | `SM2-006` |
| The Peter section reaches its fixed beat | Accept the authored transition | Peter's state is preserved and direct control begins at Miles's staged position | handoff is system-authored, not selected | `SM2-006` |
| Miles faces the next required group | Use Venom Punch and a prompted Finisher | ability and close action contribute to clearance | the second hero has a distinct admitted action set | `SM2-007` |
| The chase opens an air route | Open and steer Web Wings through debris | the controlled body glides through the required corridor | aerodynamic traversal is not a cinematic | `SM2-002`, `SM2-007` |
| The route restores Peter for the final phase | Clear minions and repeat damage/restraint | the final contextual strike becomes available | both protagonists contribute to one objective | `SM2-005`–`SM2-007` |
| Final strike is legal | Commit it and allow settlement | Sandman is defeated, 1,900 XP is awarded and successor state is retained | positive terminal is discrete | `SM2-004` |
| Hero health reaches zero before settlement | Accept retry | latest authored checkpoint replaces transient failed state | failure is recoverable but not success | `SM2-008`, `SM2-009` |

## Edge-case audit

- An optional accessibility modifier can widen timing or reduce pressure, but
  defaults are part of this packet; availability of an assist does not silently
  change the canonical transition.
- A Web Strike prompt is not proof of an ordinary always-available attack. It
  exists only after the current boss phase's required pressure has resolved.
- A scripted control handoff cannot support `ACT-228`, `CON-327` or `SYS-367`:
  the player chooses neither recipient nor timing in this mission.
- The loose object remains a world body before release; its accepted impact is
  represented by `ACT-048`, `SYS-705` and `SYS-706`, not a generic grenade.
- Clearing visible minions without advancing the current boss phase does not
  complete the mission. Likewise the final boss strike without the settled
  reward/successor state is not the declared terminal.
- Pre-order Web Grabber and three skill points are excluded so no entitlement
  bonus appears as an earned first-mission rule.

## Strategic and experiential structure

- Local decision: maintain traversal momentum, recognise the current dodge or
  contextual-object cue, select a reachable minion and spend a ready ability
  only where it contributes to the active gate.
- Medium horizon: preserve health through each finite group and satisfy both
  damage and web restraint so the next boss strike opens without confusing a
  temporary prompt for a permanent move.
- Long horizon: Peter's and Miles's distinct tutorial actions contribute to one
  shared mission result rather than separate scores or saves.
- Feedback: objective markers, health and ability state, attack warnings,
  tutorial prompts, boss progress, Web Strike availability and the mission XP
  settlement distinguish route, combat, phase and terminal errors.
- Failure recovery: lethal failure returns an authored checkpoint; no claim is
  made that every transient prop, minion position or ability charge survives.
- Skill expression: momentum routing, dodge timing, target priority, contextual
  object use and readiness management under simultaneous debris and combat.

## Replay and variation

- Attack order, damage taken, exact swing anchors, optional extra web shots,
  object choice and checkpoint use may vary while the ordered authored beats
  and control recipient remain fixed.
- The mission does not require an optimal time, no-damage run or exact combo.
  It does require every current gate and the final Sandman settlement.
- Accessibility assists, another difficulty, entitlement bonuses or later
  unlocked skills create different parameters and are not silently mixed into
  this default fresh-save packet.

## Adjacent systems and history

- The wider game allows player-selected switching between Peter and Miles in
  eligible campaign/open-world states. That official wider rule establishes an
  adjacent module but does not alter the scripted handoffs observed here.
- The Standard Edition supplies the base game. Pre-order and Digital Deluxe
  offers add early unlocks or cosmetics and therefore remain commercial-state
  boundaries rather than first-mission rewards.
- Existing Atlas records already cover ordinary movement, live combat, typed
  abilities, physics props, finite groups and checkpoints. This game adds only
  the traversal, handoff, phase and complete-terminal boundaries not owned by
  those reusable genes.

## Normalised genome

| Type | Genes | Boundary note |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-161`, `ACT-190`, `ACT-419`, `ACT-479` | move, swing/glide, fight, use abilities, finish and throw world objects |
| System | `SYS-036`, `SYS-215`, `SYS-369`, `SYS-380`, `SYS-578`, `SYS-705`, `SYS-706`, `SYS-749`, `SYS-927`, `SYS-928` | physics, live combat, health/retry, typed abilities/objects, groups, handoffs and boss phases |
| Constraint | `CON-269`, `CON-282`, `CON-402` | legal ability state, ordered mission gates and required group clearance |
| Information | `INF-115`, `INF-119`, `INF-125`, `INF-268`, `INF-318` | local threats, personal state, objectives, tutorial prompts and boss progress |
| Objective | `OBJ-190` | complete both-hero opening boss mission and retain its reward |
| Time | `TIM-003` | traversal, combat and debris continue in real time |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `322` (`GAME-0001`–`GAME-0322`).
- Exact genome matches: none.
- Tied near matches: `GAME-0254` — CONTROL Ultimate Edition (`18 / 38 = 0.473684`).
- Supported combination subsets: none.
- Scan date: 2026-09-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0254` — CONTROL Ultimate Edition | direct movement and attacks, typed abilities, live combat, physics-object pull/impact, health, checkpoints, ordered gates, authored groups, local/personal/mission information and real time | CONTROL acquires a retained telekinetic capability, alternates weapon/ability channels, cleanses nodes and crosses fixture/credential gates. Spider-Man instead preserves momentum across swing/glide travel, forces Peter/Miles handoffs and joins boss damage with web restraint before one opening-mission settlement | Near, `18 / 38 = 0.473684` |

## Taxonomy impact

- Four Active boundaries are added: momentum-preserving swing/glide traversal,
  authored dual-protagonist handoff, damage/restraint boss-phase settlement and
  the complete two-hero opening-mission terminal.
- Twenty-two existing boundaries are reused without wording or earlier
  signature changes. No combination definition changes.

## Negative results

- `ACT-228`, `CON-327` and `SYS-367` are rejected because the scoped mission's
  Peter/Miles transfers are not player-selected.
- Open-world crimes, districts, suit technology, skill purchasing and later
  mission systems are real but not causal inside `Surface Tension`.
- No pre-order or Digital Deluxe grant is treated as earned mission progress.
- No checkpoint-persistence claim beyond ordinary restoration is made because
  no installed build or reload comparison was available.

## Delta summary

## New facts

- [Confirmed | Direct | High] The launch Standard Edition is a single-player
  PS5 base game centred on Peter and Miles, with web swinging and Web Wings
  (`SM2-001`–`SM2-003`).
- [Observation | Corroborated | High] `Surface Tension` forces both control
  perspectives through rescue, minion and Sandman phases before awarding
  1,900 XP (`SM2-004`–`SM2-007`).
- [Confirmed | Direct | High] Optional accessibility changes exist but are
  excluded by the default-rules packet (`SM2-008`).

## New genes

- [Observation | Corroborated | High] `ACT-479`, `SYS-927`, `SYS-928` and
  `OBJ-190` isolate swing/glide momentum, authored protagonist handoff,
  damage-plus-restraint phase settlement and the complete opening terminal.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Confirmed | Direct | High] No earlier taxonomy boundary or signature
  changed; 22 existing genes are reused as written.

## New questions

- Which exact state fields survive a performed checkpoint reload inside each
  Sandman phase on the launch PS5 build?
- How should the later player-selected open-world switch partition retained
  concurrent state from this mission's authored handoff?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0324` Contra Force.
- Optimisation criterion: move from a current cinematic PS5 traversal/combat
  mission to a legacy NES run-and-gun packet with a manually directed partner.
- Expected information gain: test character-order, partner-control, weapon
  pickup and stage-terminal boundaries against an original manual and route.

## Research checklist

- [x] PS5 Standard Edition, defaults, mission, entry, terminal and bonuses declared
- [x] official product/opening evidence separated from two written mission routes
- [x] scripted handoff separated from player-selected switching
- [x] direct-play, installed-build, reload and audiovisual limits disclosed
- [x] complete six-type gene scan performed
- [ ] deterministic lower-ID comparison output integrated
- [ ] reviewed Ukrainian localisation and bilingual presentation completed
- [ ] original artwork and responsive browser checks completed
