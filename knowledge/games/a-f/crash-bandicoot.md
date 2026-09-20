---
game_id: GAME-0326
slug: crash-bandicoot
game_title: Crash Bandicoot
analysis_status: reviewed
reviewed: 2026-09-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-295
  system:
    - SYS-036
    - SYS-037
    - SYS-045
    - SYS-064
    - SYS-215
    - SYS-755
    - SYS-911
    - SYS-933
    - SYS-934
    - SYS-935
    - SYS-936
  constraint:
    - CON-650
  information:
    - INF-357
  objective:
    - OBJ-192
  time:
    - TIM-003
---

# Game: Crash Bandicoot

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Crash, Wumpa fruit,
Aku Aku, `N. Sanity Beach` and the crate artwork are carrier parameters, not
gene names.

## Analysis scope

- Version / ruleset: original North American English PlayStation disc
  `SCUS-94900`, one-player mode, fresh game and the first `N. Sanity Beach`
  level only. The packet is not the 2017 *N. Sane Trilogy* remake.
- Structured analysis target: licensed North American PlayStation disc
  `SCUS-94900`; see `GAME-0326` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: read the near forward/depth slice; steer, jump or
  spin to cross gaps, defeat or avoid a crab or turtle, break reachable typed
  crates, collect fruit, life and mask results, preserve the gem-eligible
  attempt through the checkpoint, trigger the exclamation crate that creates
  the optional crate bridge, clear both fork branches and continue toward the
  level portal.
- Entry: first ordinary control of Crash at the authored beach origin of a
  fresh `N. Sanity Beach` attempt, before the first crab or crate.
- Positive terminal: all 49 qualifying crates have been broken in one
  gem-eligible attempt, the clear gem is credited at the end-of-level
  settlement and Crash enters the portal so the island-map successor becomes
  available.
- Negative terminal: a lethal contact or fall consumes the last available life
  and the Game Over surface appears. Continue/password recovery and another
  attempt are outside the packet.
- Included: direct path/depth movement, jump and spin; gravity, support, gaps
  and local collision; crabs and turtles; top-contact defeat/bounce and unsafe
  hostile contact; ordinary, question-mark, arrow, checkpoint, Crash-life,
  Aku Aku, iron and exclamation crates present on the route; authored crate
  count; the switch-created bridge; Wumpa fruit and the hundred-fruit life
  conversion; finite lives; checkpoint return; Aku Aku one-hit protection and
  three-mask temporary invulnerability; the fork, hidden crate, clear-gem
  settlement and portal transition.
- Excluded: every level after the first island-map return, bonus rounds, Tawna
  tokens, keys, coloured gems, bosses, save points, passwords and Continue;
  later moves such as slide, body slam, crouch, sprint or double jump; time
  trials and relics; full-game completion; Japanese/PAL rule differences;
  prototypes, sequels, ports, emulation features, *N. Sane Trilogy*, cheats,
  glitches, speedrunning and fan modifications.
- Reproducible parameterisation: use a fresh one-player `SCUS-94900` game,
  enter `N. Sanity Beach`, break the first checkpoint crate, activate the
  exclamation crate, traverse its created crate bridge, visit both fork paths,
  break all 49 qualifying crates without a later death, receive the clear gem
  and enter the exit portal. Trigger at least one arrow-crate bounce, collect
  at least one Wumpa fruit and Aku Aku mask, and defeat one eligible enemy by
  top contact and one by spin. Fruit total, mask count and extra-life timing
  may otherwise vary.
- Potential scoped modules: the ordinary no-gem stage exit, death/restart
  accounting before and after checkpoint, the island map, save/password
  persistence, each later level, bonus rounds, keys, bosses and later releases
  require separate packets or evidence.
- Direct-play status: not conducted. No original disc, PlayStation console,
  licensed installed wrapper, memory card, controller trace, save, screenshot,
  video or audio was used. The original manual scan establishes controls,
  pickups, masks, crate classes, lives and gem conditions; a written original-
  PlayStation route corroborates the exact first-level order. This is a
  source-bounded reconstruction, not a claimed playthrough or reload test.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CB-001` | The subject is the North American original PlayStation disc `SCUS-94900`, not a remake | Confirmed | Corroborated | High | P1, P2, P3 |
| `CB-002` | The D-pad moves Crash, X jumps, Square or Circle spins and START pauses | Confirmed | Direct | High | P1 |
| `CB-003` | A qualifying top contact defeats or passes an eligible enemy while rebounding Crash; unsafe contact or a fall can lose the current life | Confirmed | Direct | High | P1 |
| `CB-004` | Crates are typed fixtures: ordinary/reward crates break, arrow crates bounce, checkpoint crates set return state, iron crates remain unbreakable and exclamation crates change linked level geometry | Confirmed | Direct | High | P1; corroborated by S1 |
| `CB-005` | Wumpa fruit are collected on contact and one hundred award an extra life | Confirmed | Direct | High | P1 |
| `CB-006` | One Aku Aku mask absorbs one compatible hit; three collected masks grant temporary invulnerability | Confirmed | Direct | High | P1 |
| `CB-007` | A lethal result consumes one finite life and returns Crash at the latest activated checkpoint while stock remains | Confirmed | Direct | High | P1 |
| `CB-008` | The original gem attempt requires breaking every qualifying crate and reaching the level end without losing a life after checkpoint activation | Confirmed | Direct | High | P1; corroborated by S1 |
| `CB-009` | North American `N. Sanity Beach` contains 49 qualifying crates, one checkpoint and a fork whose exclamation crate creates a ten-crate bridge | Observation | Corroborated | High | S1, S2 |
| `CB-010` | The exit settlement credits the clear gem when eligible and the portal returns control to the island-map successor | Observation | Corroborated | High | S1, S2 |
| `CB-011` | No executable, direct play, memory-card, reload or audiovisual evidence was used | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Naughty Dog developed and Sony Computer Entertainment
  published the North American PlayStation release in 1996.
- Platform or physical form: original English North American PlayStation disc
  `SCUS-94900`, one-player fresh game.
- Puzzle family: physics and object manipulation; real-time system pressure;
  ordered dependency sequencing.
- Original and product sources, accessed 2026-09-20:
  - **[P1]** [scan of the original North American PlayStation instruction
    manual](https://www.gamesdatabase.org/Media/SYSTEM/Sony_Playstation//Manual/formated/Crash_Bandicoot_-_1996_-_Sony_Computer_Entertainment.pdf),
    for controls, jumping and spinning, enemies, Wumpa fruit, lives, Aku Aku,
    crate classes, checkpoints and gem conditions.
  - **[P2]** [Redump disc record search for *Crash
    Bandicoot*](https://redump.org/discs/region/Am/quicksearch/crash-bandicoot/),
    for the USA/English original-disc identity and serial `SCUS-94900`. No disc
    image was downloaded or executed.
  - **[P3]** [PSX Data Center `SCUS-94900` product
    record](https://psxdatacenter.com/games/U/C/SCUS-94900.html), for serial,
    publisher, developer and 1996 North American release identity.
- Corroborating written sources, accessed 2026-09-20:
  - **[S1]** [GameFAQs original-PlayStation written
    walkthrough](https://gamefaqs.gamespot.com/ps/196986-crash-bandicoot/faqs/48030),
    for the first-level crate, enemy, checkpoint, fork and exit order.
  - **[S2]** [Bandipedia `N. Sanity Beach`
    reference](https://crashbandicoot.fandom.com/wiki/N._Sanity_Beach), used
    only to cross-check the North American 49-crate count, first-level identity
    and clear-gem target.
- Research record: **[R1]** local preflight on 2026-09-20 found no original
  disc, console, licensed executable, memory card, input trace, screenshot,
  video or audio. No audiovisual evidence was used.
- Claim IDs: `CB-001`–`CB-011`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: steer Crash directly along the route's forward/depth
  plane and jump through local support and gap geometry.
- Existing `ACT-295`: commit Crash's character-owned spin attack while his
  current pose permits it. Enemy and crate contact resolve separately.
- Exact pad buttons, run speed, jump arc, spin duration and collision reach are
  parameters. Claims: `CB-002`–`CB-004`.

### System Behaviour Genes

- Existing `SYS-036`: gravity, velocity, support, bounce and collision
  continuously resolve Crash and eligible crates against authored geometry.
- Existing `SYS-037`: contact consumes Wumpa fruit, a loose life, a mask or
  the settled gem and credits its declared state.
- Existing `SYS-045`: crabs and turtles move through the live route without a
  separate player command. Existing `SYS-064`: qualifying top contact removes
  or bypasses an eligible enemy and rebounds Crash, while unsafe contact
  applies the current protection or lethal result.
- Existing `SYS-215`: movement, spin, hostile motion, contact, crate response
  and damage resolve on one live clock. Existing `SYS-755`: compatible jump or
  spin contact destroys a qualifying crate and resolves its contained output;
  iron crates reject ordinary damage.
- Existing `SYS-911`: lethal resolution consumes one finite life and restores
  Crash at the current start/checkpoint only while stock remains.
- New `SYS-933`: breaking a checkpoint crate replaces the current within-level
  respawn anchor; later life loss returns Crash there while restoring the
  authored post-checkpoint transient route state.
- New `SYS-934`: striking the authored exclamation crate converts a previously
  absent linked set into a traversable ten-crate bridge, after which each
  created crate remains an individually breakable counted body.
- New `SYS-935`: Wumpa contacts increase one bounded counter; every completed
  hundred is removed from that counter and adds one life to the finite stock.
- New `SYS-936`: mask pickups advance a protection ladder; one or two masks
  each cancel one compatible hit by consuming one layer, while the third
  changes the state to temporary contact invulnerability before ordinary
  vulnerability returns.
- Resolution order: player/enemies move; support and contact resolve; spin or
  top contact classifies enemy/crate results; pickups and protection update;
  lethal state consumes life and returns to the current anchor; exit evaluates
  crate/death eligibility before the portal successor. Claims:
  `CB-002`–`CB-010`.

### Constraint Genes

- New `CON-650`: the original clear-gem settlement is eligible only when every
  qualifying crate in the current level has been broken and the attempt has
  not lost a life after checkpoint activation; an ordinary portal exit may
  still complete without the gem.
- Forty-nine qualifying crates, iron exclusion, death boundary and checkpoint
  position are parameters. Claim: `CB-008`, `CB-009`.

### Information Genes

- New `INF-357`: the fixed near-camera route view and HUD jointly expose Crash,
  immediate support/depth, enemies, visible crate classes and pickups, plus
  current Wumpa, life, mask and destroyed-crate state, while later geometry,
  hidden crate contents and untriggered bridge bodies remain unknown.
- The viewport does not reveal the whole route or solve the fork. Exact future
  hostile motion is also concealed. Claims: `CB-004`–`CB-009`.

### Objective Genes

- New `OBJ-192`: break the complete qualifying crate set in a gem-eligible
  `N. Sanity Beach` attempt, accept the clear-gem settlement and enter the
  portal to reach the island-map successor. Fruit, lives, masks and enemy
  defeats matter only as route state; no particular final amount is required.
- Claims: `CB-008`–`CB-010`.

### Time Genes

- Existing `TIM-003`: Crash, enemies, falls, rebounds, temporary immunity and
  route contact continue in real time while the player chooses movement, jump
  and spin inputs. Pause is an interruption, not a planning phase.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Crash stands before one gap | Run in the chosen depth line and press jump | momentum and gravity resolve a continuous arc; insufficient support contact falls below the route | direct 3D platform traversal | `CB-002` |
| A crab or turtle is reachable from above | Descend onto the eligible body | the enemy is removed or displaced and Crash rebounds | top contact differs from unsafe contact | `CB-003` |
| The same enemy is reachable at ground level | Press spin before contact | the character-owned attack resolves against the enemy while live movement continues | spin is an explicit attack command | `CB-002`, `CB-003` |
| An ordinary or reward crate is intact | Spin into it or land through a compatible break contact | the crate loses its solid state, the destroyed count advances and any declared contents become available | crates are counted breakable world state | `CB-004` |
| An arrow crate is supported below Crash | Land on its top | the contact applies its stronger authored rebound and may make a higher crate reachable | typed crate changes traversal | `CB-004` |
| The checkpoint crate is intact | Break it | the crate counts as destroyed and the current within-level return anchor becomes its authored location | counted object also changes later failure | `CB-004`, `CB-007` |
| One life remains after checkpoint activation | Fall or take an unprotected lethal contact | the life stock reaches zero and Game Over appears instead of another checkpoint body | finite stock owns complete failure | `CB-007` |
| Ninety-nine Wumpa fruit are currently credited | Contact one more fruit | one hundred fruit are converted into one additional life and the fruit counter rolls to its declared remainder | collection changes survival stock | `CB-005` |
| Crash has no mask protection | Contact one Aku Aku crate result, then take one compatible hit | one mask layer is added, then consumed to cancel that hit instead of losing a life | one pickup buys one hit | `CB-006` |
| Crash already has two mask layers | Collect a third mask | the ladder changes to temporary invulnerability; its expiry returns ordinary protection/vulnerability rules | threshold changes contact law | `CB-006` |
| The crate bridge is absent at the fork | Strike the exclamation crate | ten linked crate bodies appear as a traversable bridge on the other path | switch mutates both route and counted set | `CB-004`, `CB-009` |
| All 49 qualifying crates are broken without a post-checkpoint death | Reach the end settlement and enter the portal | the clear gem is credited and the island-map successor becomes available | exact positive terminal | `CB-008`–`CB-010` |

## Edge-case audit

- The iron crate is visible geometry but not one of the 49 qualifying
  breakables. Ordinary jump/spin contact neither destroys nor credits it.
- The arrow crate is both support and a rebound fixture; its stronger bounce
  is a typed parameter of continuous physics, not a separate jump command.
- The exclamation crate does not award an inventory key. It changes an
  authored linked crate set in the current level, so `SYS-934` stays distinct
  from carried-key barriers and generic one-shot rewards.
- A checkpoint crate is also counted when broken. `SYS-933` owns its future
  respawn-anchor effect; `SYS-755` owns its destruction.
- One or two Aku Aku masks cancel discrete compatible hits. Three masks create
  a timed law change; neither state is ordinary health, armour or Mario's
  capability-form ladder.
- The clear gem is optional to ordinary level completion, but required by this
  reproducible packet. The genome therefore includes the gem-eligible
  objective without claiming that every player must earn it to leave.

## Strategic and experiential structure

- Local decision: select a depth line and time jump or spin against the
  visible gap, enemy, crate stack or rebound surface.
- Medium horizon: preserve masks and lives through the checkpoint, remember a
  hidden or passed crate and traverse both fork branches after creating the
  bridge.
- Long horizon: keep the attempt gem-eligible while converting enough typed
  crate and fruit state into survival resources before the final crate count.
- Reversibility: lateral/depth corrections remain possible on broad ground;
  broken crates, spent masks, consumed lives and a post-checkpoint death's gem
  consequence do not reverse inside the same attempt.
- Failure attribution: visible contact, the mask/life presentation,
  checkpoint return, crate count and end-of-level settlement distinguish route
  error, absorbed hit, life loss and gem ineligibility.
- Player trust: the authored 49-crate set, checkpoint location, exclamation
  linkage and exit evaluation must give the same result from equivalent state.

## Replay and variation

- Route geometry, crate identities, checkpoint, fork and qualifying count are
  authored; no procedural level generation is claimed.
- Enemy timing, chosen fork order, Wumpa collection line, mask retention,
  spin/jump choices and extra-life timing can vary without changing the
  all-crate terminal.
- An ordinary first completion without the clear gem is a valid broader-game
  outcome but is outside this parameterised run.

## Adjacent systems and history

- *Super Mario Bros.* shares direct jumping, live enemies, typed blocks,
  optional pickups, life state and a successor stage. World 1-1 is a side-view
  route whose camera commits passed terrain and flag height/time settle score;
  `N. Sanity Beach` uses near-camera depth, counted crate destruction, a
  checkpoint anchor, stacked masks and an all-crate no-death gem predicate.
- *ASTRO BOT* shares direct 3D platform movement, local view, authored
  checkpoints and real-time enemies. Its bounded packet rescues persistent
  Bots and uses temporary traversal abilities; Crash centres finite lives,
  typed crates and a gem-eligible count.
- *Battletoads* shares a finite life stock, direct body attacks and live route
  enemies. Its canyon advances through combat gates and converted enemy tools;
  Crash can bypass many enemies but must account for every qualifying crate.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-295` | pad mapping, movement plane, jump arc and spin duration are parameters |
| System Behaviour | `SYS-036`, `SYS-037`, `SYS-045`, `SYS-064`, `SYS-215`, `SYS-755`, `SYS-911`, `SYS-933`–`SYS-936` | route geometry, crate roster, contents, counters, mask duration and return point are parameters |
| Constraint | `CON-650` | qualifying crate set and post-checkpoint death boundary are parameters |
| Information | `INF-357` | camera, HUD layout, crate symbols and hidden future state are parameters |
| Objective | `OBJ-192` | level, 49-crate set, clear gem and portal successor are parameters |
| Time | `TIM-003` | update cadence and pause behaviour are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `325` (`GAME-0001`–`GAME-0325`).
- Exact genome matches: none.
- Tied near matches: `GAME-0312` — ASTRO BOT (`6 / 27 = 0.222222`); `GAME-0313` — Tank 1990 (`6 / 27 = 0.222222`).
- Supported combination subsets: none.
- Scan date: 2026-09-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0312` — ASTRO BOT | `ACT-008`, `SYS-036`, `SYS-037`, `SYS-045`, `SYS-215`, `TIM-003` | Both directly steer a jumping body through a live three-dimensional platform route with local enemies and collectibles. ASTRO BOT uses authored checkpoint rollback, persistent Bot rescue, struck fixtures and temporary Inflate traversal; Crash spends a finite life at a counted checkpoint and binds typed crate destruction, fruit/mask survival state and a no-death exhaustive gem predicate to the exit. | Near, `6 / 27 = 0.222222` |
| `GAME-0313` — Tank 1990 | `ACT-008`, `SYS-045`, `SYS-215`, `SYS-755`, `SYS-911`, `TIM-003` | Both directly move and attack through live autonomous threats, can destroy eligible world objects and spend a finite life to recreate the controlled body. Tank 1990 feeds a bounded tank reserve through one fixed defended arena with random typed bonuses and mutable terrain; Crash traverses a near-camera authored course whose checkpoint, counted crates, mask ladder and optional perfect-clear gem govern the run. | Near, `6 / 27 = 0.222222` |

### Preserved research notes

- New genes: `SYS-933`–`SYS-936`, `CON-650`, `INF-357` and `OBJ-192`.
- Classification result: `New gene`; no verified combination is expected.
- Evidence and reasoning: no lower-ID boundary activates a counted checkpoint
  crate as a finite-life return anchor, creates a linked counted-crate bridge,
  converts a hundred route collectibles into one life, stages mask layers into
  temporary invulnerability, owns the original no-death crate-gem gate, joins
  the depth-route information surface or settles its complete gem-and-portal
  terminal.

## Taxonomy impact

- Registry changes: add seven Active boundaries and add Crash Bandicoot
  support to nine compatible existing boundaries.
- Taxonomy-change record: none; `ACT-295` already includes character-owned
  platform/brawler attacks, and the remaining reused genes fit as written.
- Candidate terms affected: Crash, Wumpa, Aku Aku, crate artwork, exact counts,
  buttons, `N. Sanity Beach` and the portal are product or carrier parameters.

## Negative results

- No disc, console, executable, memory card, direct play, reload comparison,
  screenshot, video or audio evidence exists for this unit.
- No claim is made about a hidden crate result before it is triggered, precise
  frame timing, enemy randomisation or the exact internal reset table.
- The original manual's broad crate catalogue is not imported wholesale:
  only classes corroborated on `N. Sanity Beach` enter the bounded route.
- Bonus-round deaths, Tawna tokens, keys, save/password state and later-level
  coloured-gem dependencies are excluded rather than inferred.
- Remake mechanics, including revised controls, time trials and altered gem
  handling, do not support this original-disc signature.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original manual establishes movement, spin,
  jump, Wumpa/life conversion, mask protection, typed crates, checkpoint return
  and gem eligibility (`CB-002`–`CB-008`).
- [Observation | Corroborated | High] The written original-game route
  establishes the 49-crate first level, fork, switch bridge and portal terminal
  (`CB-009`, `CB-010`).

## New genes

- [Confirmed | Direct | High] `SYS-933`, `SYS-935`, `SYS-936` and `CON-650`
  isolate checkpoint, Wumpa/life, mask and gem-eligibility transitions.
- [Observation | Corroborated | High] `SYS-934`, `INF-357` and `OBJ-192`
  isolate the switch-created counted bridge, joined depth-route disclosure and
  all-crate gem/portal terminal.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Corroborated | High] No earlier boundary, signature or
  lifecycle state changes; nine existing genes are reused as written.

## New questions

- Which exact crate and enemy states restore after each original-disc
  checkpoint death, and how does the hidden crate counter represent that loss?
- Which `SCUS-94900` revision differences, if any, alter timing without changing
  the bounded signature?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0327` Fable, original Xbox base game, is
  the next reserved audience-recognition unit.
- Optimisation criterion: replace a fixed reflex route with moral choice,
  staged training and a retained first guild transition.
- Backlog impact: this unit completes 2/9 of the current horizon.

## Why this game

- [Hypothesis | Limited | High] The original Crash Bandicoot is a recognisable
  PlayStation anchor whose near-camera depth, typed crates, checkpoint/life
  economy and no-death gem condition differ causally from side-view platformer
  labels.

## Research checklist

- [x] exact original disc, level, entry, terminal and exclusions declared
- [x] original manual and independent written route evidence separated
- [x] crate destruction, checkpoint, switch bridge, fruit/life and mask state separated
- [x] direct-play, executable, reload and audiovisual limits disclosed
- [x] complete six-type gene scan performed
- [x] deterministic lower-ID comparison output integrated
- [x] reviewed Ukrainian localisation and bilingual presentation completed
- [x] original artwork and responsive browser checks completed
