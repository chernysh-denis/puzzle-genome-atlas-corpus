---
game_id: GAME-0341
slug: ninja-gaiden-black
game_title: "Ninja Gaiden Black"
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-131
    - ACT-161
    - ACT-223
    - ACT-341
    - ACT-437
  system:
    - SYS-215
    - SYS-222
    - SYS-369
    - SYS-574
    - SYS-578
    - SYS-749
    - SYS-755
    - SYS-773
    - SYS-959
  constraint:
    - CON-175
    - CON-282
    - CON-324
  information:
    - INF-115
    - INF-119
    - INF-125
    - INF-142
    - INF-268
    - INF-299
    - INF-318
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Ninja Gaiden Black

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Ryu Hayabusa,
Murai, Ayane, the Dragon Sword, Essence and every room, item, enemy or
technique name are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: original North American English *Ninja Gaiden Black* for
  the original Xbox, released 2005-09-20, restricted to the unmodified retail-
  disc Story Mode rules. The current Xbox Store listing corroborates the same
  Tecmo product identity and backward-compatible availability but does not
  redefine this packet as an Xbox One or Xbox Series release.
- Structured analysis target: fresh Story Mode game on `Normal`, default
  controls and no prior clear data, restricted to Chapter 1, `The Way of the
  Ninja`; see `GAME-0341` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: read the authored Kunai instruction, local geometry,
  enemy motion and health state; run, jump, wall-run, hang, swing and climb;
  alternate direct sword or projectile attacks with held guard and timed
  Reverse Wind; collect or deliberately consume the coloured Essence left by
  defeated enemies; use nearby Essence to shorten a held heavy-attack charge;
  open the next route gate and repeat until Murai's encounter and the chapter
  evaluation settle.
- Entry: first ordinary control of Ryu on the mountain path at the start of
  Chapter 1, before reading the first Ayane Kunai instruction.
- Positive terminal: Murai reaches the encounter's scripted defeat threshold,
  the Chapter 1 completion and Karma evaluation are accepted, and the game
  reaches first ordinary Ryu control in Chapter 2, `The Hayabusa Ninja
  Village`. The packet stops before leaving Murai's room.
- Negative state: health depletion produces Game Over; `Continue` restores the
  most recent manually written Dragon Save Point rather than the transient
  failed fight. Before the first save, no resumable save is claimed.
- Included: ordinary run and jump traversal; wall run, wall-run jump, Flying
  Bird Flip, ledge hang and branch swing as parameters of embodied navigation;
  Dragon Sword light, heavy, running, jumping, wall and combo attacks; the
  carried Shuriken; held blocking and directional Reverse Wind; health damage,
  finite Elixirs and immediate healing; yellow, blue and red Essence released
  by enemy defeat and pulled into Ryu at proximity; held heavy-attack charge,
  nearby-Essence absorption and charged release; authored Kunai instructions,
  map and colour-coded door state; breakable pots, torches and wall scrolls;
  contextual chest, armour, Fangs, key, door and Dragon Save Point
  interactions; finite authored ninja groups; Murai's visible health, attack
  cues, guarded strings and unblockable grab; Game Over, Continue, chapter
  Karma categories and first Chapter 2 control.
- Excluded: walking beyond Murai's room in Chapter 2; Ninpo, swimming, running
  on water, Bow, Lunar, shops, weapon upgrades, Counter Attacks, Golden Scarab
  rewards and every later weapon, enemy, boss or chapter; Ninja Dog, Hard, Very
  Hard and Master Ninja; Mission Mode; the emulated classic trilogy; the 2004
  original release, Hurricane Packs, *Ninja Gaiden Sigma*, *Master Collection*,
  sequels, emulation, cheats, glitches and mods; a save/relaunch equality claim
  after the chapter boundary.
- Reproducible parameterisation: start a fresh North American retail-disc Story
  Mode game on `Normal`; follow the mountain and fortress route, read the Kunai
  instructions, take the fortress map, survive the sealed-room group, reveal
  the hidden wall-scroll passage, descend through the trap door, recover the
  Fangs of the Samurai, apply them to the armour, take the Key of Courage,
  write the Dragon Save Point, open the Inner Sanctum and defeat Murai. Accept
  the chapter report and stop at first Chapter 2 control. Exact combos, wall
  attacks, Shuriken use, Essence colours, Ultimate Technique use, Elixir use,
  incidental pots, damage, deaths, Karma total and rank may vary.
- Potential scoped modules: a performed original-Xbox build inspection,
  chapter-boundary save/reload test, other difficulty, Ninja Dog transition,
  Mission Mode, one shop/upgrade cycle, a later chapter, classic arcade titles
  and backward-compatible wrapper behaviour each need independent entry,
  terminal and evidence.
- Direct-play status: not conducted. No original Xbox, retail disc, installed
  executable, controller trace, save, screenshot, video or audio was available
  or analysed. The packet is a source-bounded reconstruction; the original
  2004 manual is used only for the inherited core control and Essence rules,
  while Black-specific route and scoring claims are independently marked as
  corroborated rather than presented as direct play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `NGB-001` | Tecmo published Team Ninja's original-Xbox Ninja Gaiden Black on 2005-09-20, and the same product remains listed for compatible Xbox hardware | Confirmed | Direct | High | P1, P2 |
| `NGB-002` | Core controls expose direct movement, jump and wall traversal, sword and projectile attacks, held block, directional Reverse Wind and contextual interaction | Observation | Corroborated | High | P3, S1 |
| `NGB-003` | Defeated enemies release yellow, blue or red Essence; proximity collects it as currency, health or Ki | Observation | Corroborated | High | P3, S1 |
| `NGB-004` | Holding the heavy-attack command absorbs nearby uncollected Essence to accelerate a charged attack, and release commits the resulting technique instead of the Essence's ordinary pickup effect | Observation | Corroborated | High | P3, S1, S3 |
| `NGB-005` | Chapter 1 follows an authored mountain-and-fortress route through instructions, map, sealed fights, a hidden passage, Fangs, armour, Key of Courage, save point and Inner Sanctum | Observation | Corroborated | High | S1, S2 |
| `NGB-006` | Murai's mandatory encounter exposes a health gauge, blockable strings and charge plus an unblockable grab that must be avoided rather than guarded | Observation | Corroborated | High | P3, S1, S2 |
| `NGB-007` | Game Over follows Ryu's health depletion, and Continue restores the latest manually written Dragon Save Point | Observation | Corroborated | High | P3, S1 |
| `NGB-008` | End-of-chapter Karma aggregates performance including completion time, kills and unspent Essence into a displayed chapter evaluation | Observation | Corroborated | High | P3, S3 |
| `NGB-009` | Defeating Murai settles Chapter 1 and yields ordinary Chapter 2 control in the same fortress room | Observation | Corroborated | High | S1, S2 |
| `NGB-010` | Chapter completion does not itself write a save; the next available Dragon Save Point lies later in Chapter 2 | Observation | Corroborated | High | S1 |
| `NGB-011` | Normal Chapter 1 teaches the admitted movement, block, combat and Essence rules through Ayane's authored Kunai messages | Observation | Corroborated | High | S1, S2 |
| `NGB-012` | No direct play or chapter-boundary persistence comparison was performed | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Team Ninja / Tecmo; North American original-Xbox release
  on 2005-09-20.
- Platform or physical form: original English original-Xbox retail disc,
  source-bounded Story Mode `Normal`, fresh save.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; world topology and perspective; ordered
  dependency sequencing.
- Primary and official sources, accessed 2026-09-21:
  - **[P1]** [official Xbox Store product
    page](https://www.xbox.com/en-US/games/store/ninja-gaiden-black/C17KKS83S9GS),
    for product identity, publisher, developer, original release date and
    current backward-compatible hardware statement.
  - **[P2]** [official Xbox backward-compatibility
    overview](https://www.xbox.com/en-US/games/backward-compatibility), for the
    distinction between an original title and the compatible runtime wrapper.
  - **[P3]** [preserved original *Ninja Gaiden* Xbox manual
    transcript](https://manuals.plus/m/7effa5f40b6da7f52d2de26b41aca3b6a6fed3bf89afbaeb9fbacdb24b7c582c),
    for inherited controls, HUD, map, save/Continue, health, items, Essence,
    Ultimate Technique and chapter-Karma rules. This is the 2004 predecessor's
    manual, not a Black-specific manual; no Black-only claim rests on it alone.
- Corroborating written sources, accessed 2026-09-21:
  - **[S1]** [Black-specific written guide and
    walkthrough](https://db.hfsplay.fr/files/2020/06/19/Ninja_Gaiden_Black_-_Microsoft_Game_Studios_MLAIP3R.pdf),
    pp. 2–3 and 56–59, for Essence trade-offs, `Normal` Chapter 1 route, Murai,
    Chapter 2 entry, manual-save warning and the later Chapter 2 save point.
  - **[S2]** [A_I_e_x Black-specific written
    walkthrough](https://gamefaqs.gamespot.com/xbox/928401-ninja-gaiden-black/faqs/39059),
    for an independent Chapter 1 and Chapter 2 route reconstruction.
  - **[S3]** [Ninja Gaiden Black Karma System
    FAQ](https://gamefaqs.gamespot.com/xbox/928401-ninja-gaiden-black/faqs/42597),
    for live combo and timed-encounter Karma plus end-of-chapter time, kill,
    unspent-Essence and filled-Ki categories.
- Research record: **[R1]** local preflight found no original Xbox console,
  disc, executable or save; no audiovisual or direct-play evidence was used.
- Claim IDs: `NGB-001`–`NGB-012`.

## Mechanical decomposition

### Action Genes

- `ACT-008` owns direct ground, air, wall, ledge and branch traversal;
  `ACT-161` ordinary sword, Shuriken, combo, wall and held/released heavy
  attacks; `ACT-437` the facing-relative held weapon guard; `ACT-223` the
  cue-timed directional Reverse Wind response; `ACT-341` authored chest,
  armour, key, door and Dragon Save Point interactions; and `ACT-131` one
  immediate finite Elixir use. Claims: `NGB-002`, `NGB-005`–`NGB-007`,
  `NGB-011`.

### System Behaviour Genes

- `SYS-215` resolves directly commanded real-time combat; `SYS-578` damage,
  healing and lethal health depletion; `SYS-749` finite route-triggered ninja
  groups; `SYS-755` damage-threshold removal of admitted pots, torches and
  wall-scroll barriers; `SYS-222` eligible world-item transfer; `SYS-369`
  Game Over Continue from a written Dragon Save Point; and `SYS-773` the
  terminal Karma evaluation.
- Revised `SYS-574` converts an eligible defeated enemy into a proximity-
  collected typed run resource rather than limiting the transferable boundary
  to experience gems. New `SYS-959` resolves nearby uncollected defeat
  resources as accelerated held-attack charge, consumes them instead of their
  ordinary pickup effects and releases the resulting charged technique.
- Resolution order: a defeated eligible enemy emits typed Essence; ordinary
  proximity pulls it into currency, health or Ki through `SYS-574`, but holding
  the eligible heavy attack first allows `SYS-959` to consume nearby Essence,
  advance the charge and replace that ordinary benefit with an Ultimate
  Technique. Claims: `NGB-003`–`NGB-009`.

### Constraint Genes

- `CON-175` makes zero health terminal for the current attempt; `CON-282`
  orders the route's map, hidden passage, Fangs, armour, key, save point and
  Murai gates; and `CON-324` requires Reverse Wind or jump evasion to overlap
  the matching live attack window. Held guard does not legalise Murai's grab.
  Claims: `NGB-005`–`NGB-007`, `NGB-011`.

### Information Genes

- `INF-115` exposes local sight and sound; `INF-119` health, Ki, item and
  currently equipped state; `INF-125` map rooms and yellow, blue or red door
  states; `INF-142` enemy motion and sound cues for guard or evasion;
  `INF-268` the current Ayane Kunai instruction; `INF-318` Murai's remaining
  health; and `INF-299` end-of-chapter categories and aggregate Karma
  evaluation. Claims: `NGB-002`, `NGB-005`–`NGB-011`.

### Objective Genes

- `OBJ-080` owns clearing the required fortress gate chain, defeating Murai
  and crossing the chapter threshold into first Chapter 2 control. The chapter
  report is part of the terminal; a save/relaunch check and every Chapter 2
  route decision are excluded. Claims: `NGB-005`, `NGB-006`, `NGB-008`–`NGB-010`.

### Time Genes

- `TIM-003` owns continuous navigation, combat, charge, Essence attraction,
  encounter pressure and defensive timing. Pause-menu item use and map review
  suspend that live loop rather than creating a second simulation authority.
  Claims: `NGB-002`–`NGB-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A wall or narrow shaft admits traversal | Jump toward it and continue the matching wall input | Ryu runs along or up the wall, can jump away or alternate between walls, and reaches geometry unavailable to ground motion | advanced movement remains parameterised embodied navigation | `NGB-002`, `NGB-005` |
| One ninja has been defeated and coloured Essence remains nearby | Move into pickup range | the Essence is attracted and resolves as yellow currency, blue health or red Ki under its type | defeat creates a typed spatial resource, not direct abstract credit | `NGB-003` |
| Uncollected Essence remains within absorption range | Hold the heavy-attack input, then release | nearby Essence is consumed to advance the charge and release a stronger technique instead of granting its ordinary resource effect | current sustain or economy can be traded for immediate offence | `NGB-004` |
| A blockable attack string is incoming | Hold guard through contact | eligible hits are negated or reduced while grab remains outside the guard's protection | guard and health resolution remain separate | `NGB-002`, `NGB-006` |
| Murai begins the documented grab motion | Commit Reverse Wind or a jump inside its live window | Ryu relocates before the grab resolves; late or mismatched defence permits the grab | readable cue and timed evasion determine safety | `NGB-006` |
| The sealed fortress room has closed | Defeat its finite ninja group | the doors unlock and the route resumes | authored hostile clearance can gate world topology | `NGB-005` |
| The Fangs have been recovered from the cave | Apply them to the armour | the armour yields the Key of Courage, which opens the Inner Sanctum route | a carried authored prerequisite changes a stateful fixture and gate | `NGB-005` |
| Ryu has reached the Dragon Save Point | Commit the save interaction | current admissible route state is written for later Continue | checkpoint recovery depends on explicit world interaction | `NGB-005`, `NGB-007` |
| Ryu reaches zero health after that save | Choose Continue at Game Over | the last written Dragon Save Point is restored without the failed transient combat state | failure restoration is not automatic chapter saving | `NGB-007` |
| Murai reaches the scripted encounter threshold | Complete the encounter and accept the chapter report | Chapter 1 closes, Karma categories and rank are displayed, and Chapter 2 begins in Murai's room | guardian defeat, aggregate evaluation and chapter crossing are distinct boundaries | `NGB-006`, `NGB-008`–`NGB-010` |

## Strategic and experiential structure

- Local decision: choose when to keep guarding, move through a cue with Reverse
  Wind, commit a recoverable sword string, use a wall attack, spend a finite
  Elixir or leave Essence on the floor for a charged technique.
- Medium-term planning: preserve health to the Dragon Save Point, read the map
  and door colours, satisfy the Fangs-to-key dependency and avoid consuming a
  valuable blue Essence when its healing benefit matters more than immediate
  offence.
- Long-term structure: authored traversal instruction becomes sealed combat,
  a short inventory-key chain and a mandatory guardian, then the same recorded
  conduct is classified at the chapter boundary.
- Common heuristics: block ordinary strings but evade grabs; use geometry as
  both route and combat surface; collect health Essence when damaged; absorb
  Essence only when the charged attack has a reachable target; save before
  entering the Inner Sanctum.
- Failure attribution: missed attack cue, overlong committed string, unsafe
  charge, wrong Essence trade-off, depleted health, missed route prerequisite
  and unwritten save remain distinguishable through HUD, animation, map,
  prompt, result and Continue state.
- Player-trust factors: health, Ki, items, hit count, interactions, door state,
  instructions, boss health, visible Essence and the terminal Karma report are
  exposed before or immediately after their relevant commitments.
- Claim IDs: `NGB-002`–`NGB-011`.

## Replay and variation

- What changes between sessions: combat spacing, combo and wall-attack choice,
  block/evasion timing, Shuriken and Elixir use, damage, deaths, Essence colour
  and pickup/charge use, incidental breakables, completion time, kills, Karma
  total and displayed rank.
- Randomness or procedural generation: no procedural room or route layout is
  evidenced; Essence type and live enemy behaviour may vary inside fixed
  authored encounters.
- Multiple viable strategies: patient guard-and-counter, wall attacks, short
  ground strings and Essence-funded charged attacks can all advance the same
  required route.
- Typical replay motive: higher chapter rank, faster completion, harder
  difficulty and Mission Mode are known motives but excluded from this packet.
- Claim IDs: `NGB-003`–`NGB-011`.

## Adjacent systems and history

- Direct predecessor: the 2004 original-Xbox *Ninja Gaiden* supplies the core
  control, Essence and Story Mode substrate; Black revises the product's
  difficulty, route content and supplementary modes.
- Variants: Black's original Xbox retail version is admitted; original 2004,
  Hurricane Packs, Sigma, Master Collection and sequels are excluded.
- Similar games: `GAME-0299` Nioh 2 shares real-time close combat, held guard,
  timed evasive response, authored route pressure, health loss and a mandatory
  guardian but uses a replenishing Ki economy, stances, Shrines, recoverable
  death currency, Yokai abilities and Dark Realm.
- Important difference: Ninja Gaiden Black makes enemy Essence simultaneously
  valuable as ordinary currency/recovery and as accelerated charged-offence
  fuel, then settles chapter conduct into Karma rather than retaining a build
  or grave-recovery loop.
- Claim IDs: `NGB-001`–`NGB-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-223`, `ACT-341`, `ACT-437` | Ryu, Dragon Sword, Shuriken, Elixir and movement names are parameters |
| System Behaviour | `SYS-215`, `SYS-222`, `SYS-369`, `SYS-574`, `SYS-578`, `SYS-749`, `SYS-755`, `SYS-773`, `SYS-959` | Essence types, charge tiers, save point, groups and Karma labels are parameters |
| Constraint | `CON-175`, `CON-282`, `CON-324` | route order, attack members and defensive windows are parameters |
| Information | `INF-115`, `INF-119`, `INF-125`, `INF-142`, `INF-268`, `INF-299`, `INF-318` | HUD layout, door colours and report art are presentation |
| Objective | `OBJ-080` | chapter, guardian, report and successor names are parameters |
| Time | `TIM-003` | live rates, charge and response intervals are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `340` (`GAME-0001`–`GAME-0340`).
- Exact genome matches: none.
- Tied near matches: `GAME-0245` — DOOM (2016) (`13 / 37 = 0.351351`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0245` — DOOM (2016) | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-215`, `SYS-222`, `SYS-369`, `SYS-578`, `SYS-749`, `CON-282`, `INF-115`, `INF-119`, `INF-125`, `TIM-003` | Both drive a bounded authored action route through direct movement and attacks, contextual gates, finite hostile groups, contact pickups, health failure and checkpoint recovery. DOOM adds weapon switching, finite ammunition, mandatory lockdown clearance, armour and contextual stagger executions that emit recovery drops before a spatial mission exit. Ninja Gaiden Black instead adds held guard, timed evasion, breakable route surfaces, typed Essence whose ordinary attraction competes with charged absorption, a visible guardian and a Karma-settled chapter crossing. | Near, `13 / 37 = 0.351351` |

### Preserved research notes

- New genes: `SYS-959`.
- Classification result: `New combination and one new gene`.
- Evidence and reasoning: ordinary navigation, attacks, guard, timed evasion,
  interaction, combat, health, authored groups, destruction, checkpoint,
  chapter evaluation and disclosure all transfer from reviewed carriers. The
  optional use of uncollected Essence as held-charge acceleration has no lower-
  ID owner and is isolated from both the attack command and ordinary pickup.

## Taxonomy impact

- Registry changes: add GAME-0341 support to compatible existing genes,
  generalise `SYS-574` with a second carrier and add `SYS-959`.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_083`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_083.md).
- Candidate terms affected: Ninja Gaiden Black, Xbox, Ryu Hayabusa, Murai,
  Dragon Sword, Shuriken, Reverse Wind, Ultimate Technique, Essence, Ayane,
  Fangs of the Samurai, Key of Courage and Karma remain product or instance
  parameters.

## Negative results

- No original hardware, disc, build, controller trace, save, screenshot,
  audiovisual observation or reload comparison was available. Chapter entry,
  route and Continue are source-backed, not locally measured.
- The end-of-chapter transition is deliberately not called an autosave. The
  packet stops at first Chapter 2 control and excludes the later Dragon Save
  Point, so neither `SYS-780` nor `OBJ-155` applies.
- Wall-running, hanging, swinging, Flying Bird Flip and ordinary combo members
  parameterise `ACT-008` or `ACT-161`; they do not justify move-name genes.
  Essence colour names are resource parameters. The Karma report reuses
  `SYS-773` and `INF-299` rather than creating a Ninja-specific ranking gene.

## Delta summary

## New facts

- [Observation | Corroborated | High] The bounded first chapter combines
  wall-rich traversal, guard/evasion combat, a short item-gate chain, manual
  checkpoint recovery, Murai and a Karma-classified chapter transition
  (`NGB-002`, `NGB-005`–`NGB-011`).
- [Observation | Corroborated | High] Defeated-enemy Essence can resolve either
  as its typed ordinary resource or as charge acceleration for an immediate
  Ultimate Technique (`NGB-003`, `NGB-004`).

## New genes

- [Observation | Corroborated | High] `SYS-959` — convert nearby uncollected
  defeat resources into accelerated held-attack charge.

## New combinations

- [Observation | Corroborated | High] No verified combination is a proper
  subset of the complete signature.

## Taxonomy changes

- [Observation | Corroborated | High] `SYS-574` is generalised from experience
  gems to typed proximity-collected resources without changing its causal
  boundary or the Vampire Survivors signature.

## New questions

- Which exact Chapter 1 inventory, Karma and world flags survive after the
  first Chapter 2 Dragon Save Point and a cold original-Xbox reload?
- Does original hardware apply any build-specific variation to the timing or
  attraction radius of Essence absorption on `Normal`?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0342` PAC-MAN, as reserved by selection
  023.
- Optimisation criterion: freeze one exact licensed arcade ruleset and a finite
  first-board terminal rather than merging ports, sequels or championship
  variants.
- Expected information gain: test discrete maze routing, pellet depletion,
  energizer state, ghost targeting and life loss against this continuous
  authored action route.
- Backlog impact: advances unit 8/9; `GAME-0342` remains reserved but
  unstarted.

## Why this game

- [Hypothesis | Limited | Medium] Ninja Gaiden Black contributes a recognisable
  original-Xbox action benchmark whose Essence decision is separable from
  ordinary loot, generic stamina combat and later Sigma variants.

## Research checklist

- [x] exact original-Xbox product, mode, difficulty and fresh-save boundary declared
- [x] primary loop, entry, terminal, parameters and exclusions declared
- [x] official product evidence, inherited manual and two Black-specific route sources reviewed
- [x] direct-play, predecessor-manual and persistence limitations disclosed
- [x] complete six-type signature and lower-ID comparison prepared
- [x] deterministic nearest-neighbour and duplicate checks regenerated
- [ ] reviewed Ukrainian localisation and bilingual presentation completed
- [ ] original artwork and responsive browser checks completed
- [ ] repository and web quality gates completed
