---
game_id: GAME-0183
slug: vampire-survivors
game_title: Vampire Survivors
analysis_status: reviewed
reviewed: 2026-08-29
combination_ids:
  - COMB-0181
gene_ids:
  action:
    - ACT-008
    - ACT-140
  system:
    - SYS-004
    - SYS-299
    - SYS-469
    - SYS-572
    - SYS-573
    - SYS-574
    - SYS-575
    - SYS-576
    - SYS-577
    - SYS-578
    - SYS-579
  constraint:
    - CON-188
    - CON-485
    - CON-486
    - CON-487
  information:
    - INF-002
    - INF-119
    - INF-235
    - INF-236
  objective:
    - OBJ-107
  time:
    - TIM-003
---

# Game: Vampire Survivors

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: Windows PC stable Steam public branch, game version
  `1.16.100`, Steam build `24926490`, reviewed 2026-08-29; English, solo,
  unmodified base game from an empty save slot, Antonio Belpaese and normal Mad
  Forest with no PowerUps or optional stage modifiers.
- Primary decision loop: move Antonio to keep space and align the Whip's
  automatic horizontal coverage; let cooldown-governed weapons defeat enemies;
  route through the resulting Experience Gems; choose one eligible weapon,
  passive or upgrade whenever a level pauses play; collect boss chests and
  optionally satisfy the Whip/Hollow Heart evolution chain; then repeat while
  the authored enemy waves intensify toward the thirty-minute terminal.
- Entry and exit: begins at the first controllable `0:00` frame after selecting
  Antonio and normal Mad Forest. It succeeds when the stage reaches `30:00` and
  is marked complete; the first Reaper then provides the ordinary lethal cleanup
  and result settlement. It fails when Antonio's health reaches zero before the
  time limit.
- Included: direct two-dimensional movement; Antonio's default Whip and passive
  Might growth; cooldown-driven automatic weapons; normal Mad Forest's open
  terrain, fixed stage items, time-indexed waves and bosses; enemy damage and
  one continuous health pool; Experience Gems, Magnet attraction, level
  thresholds, paused random offers, six weapon and six passive level-up caps;
  cumulative run-local item levels; Hollow Heart; boss chests; maximum-level
  Whip evolution into Bloody Tear when its requirements are met; stage clock,
  completion, Reaper and ordinary result/reset.
- Excluded: every DLC, including Legacy of the Bloodmoon; public beta; online,
  local co-op and Party Mode; Adventures; Hyper, Hurry, Endless, Inverse,
  Limit Break and Random LevelUp; Arcanas, Darkanas, Golden Eggs, Reroll, Skip
  and Banish; later characters, stages, relics, secrets and unlock routes;
  account-wide PowerUps, exhaustive collection completion, mods and debug tools.
- Potential scoped modules: one independently versioned DLC stage; online or
  local co-op; an Adventure; an Arcana-enabled build; an Endless cycle; or a
  later cleanly bounded character/stage/evolution route.
- Direct-play status: not conducted. The current creator announcement, official
  store and official maintained wiki establish the build, starting character,
  stage, weapon, level-up, evolution and terminal transitions. Random offers
  and exact pathing remain run variation, not a claimed captured trace.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `VS-001` | The reviewed Windows public branch is stable version 1.16.100 / Steam build 24926490, while the public beta and new DLC are excluded | Confirmed | Corroborated | High | P1, P2, S1 |
| `VS-002` | Antonio is the default base-game character, starts with Whip and has the declared health, armour and level-based Might behaviour | Confirmed | Direct | High | P3 |
| `VS-003` | Normal Mad Forest is available from the start, has an open field, fixed base stage items and a 30:00 time limit | Confirmed | Direct | High | P4, P5 |
| `VS-004` | The player moves the character while equipped weapons activate automatically from weapon-specific cooldown and geometry | Confirmed | Direct | High | P2, P6 |
| `VS-005` | Defeated enemies can leave Experience Gems whose spatial collection advances the next level threshold | Confirmed | Direct | High | P7 |
| `VS-006` | Level-up pauses the stage, samples three or four unique eligible options and applies the selected new item or next item level | Confirmed | Direct | High | P7, P8 |
| `VS-007` | Ordinary level-up selection is bounded by separate six-weapon and six-passive capacities and item maximum levels | Confirmed | Direct | High | P6, P8 |
| `VS-008` | Mad Forest uses time-indexed waves and bosses; boss chests grant eligible levels or conditional evolutions | Confirmed | Direct | High | P4, P9, P10 |
| `VS-009` | Maximum-level Whip plus Hollow Heart and an evolution-capable chest can replace Whip with Bloody Tear | Confirmed | Direct | High | P6, P9, P11 |
| `VS-010` | Health reaching zero closes the run, while compatible pickups or Bloody Tear may restore missing health | Confirmed | Direct | High | P11, P12 |
| `VS-011` | Reaching Mad Forest's 30:00 limit completes the stage before Reapers arrive to end the non-Endless run | Confirmed | Direct | High | P5, P13 |
| `VS-012` | The bounded decisions couple local movement, automatic coverage, spatial XP collection and repeated build drafts without attack input | Observation | Corroborated | High | P2–P13, V1 |

## Basic data

- Release / origin: developed and published by poncle; the official Steam
  product remains titled **Vampire Survivors**.
- Platform or physical form: a real-time single-player survival run on Windows
  PC, with direct movement and automatically executing weapon systems.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary and reproducible sources:
  - **[P1]** [poncle's official 1.16 / Legacy of the Bloodmoon announcement](https://steamcommunity.com/games/1794680/announcements/detail/717913919982667417),
    for stable version `1.16.100`; all new DLC content is explicitly excluded.
  - **[P2]** [official Steam product page](https://store.steampowered.com/app/1794680/Vampire_Survivors/),
    for the current title, developer/publisher, movement-led survival, weapons,
    upgrades and PC product boundary.
  - **[P3]** [official Vampire Survivors Wiki — Antonio Belpaese](https://vampire.survivors.wiki/w/Antonio_Belpaese),
    for default availability, Whip, Max Health, Armour and Might growth.
  - **[P4]** [official Vampire Survivors Wiki — Mad Forest](https://vampire.survivors.wiki/w/Mad_Forest),
    for starting availability, open terrain, stage items, minute waves, bosses
    and the `30:00` stage table.
  - **[P5]** [official Vampire Survivors Wiki — Stages](https://vampire.survivors.wiki/w/Stages),
    for time-limit completion, normal/Endless distinction, Reaper cadence and
    completion reward.
  - **[P6]** [official Vampire Survivors Wiki — Weapons](https://vampire.survivors.wiki/w/Weapons),
    for automatic cooldown statistics, six ordinary weapon slots, item levels
    and evolution replacement.
  - **[P7]** [official Vampire Survivors Wiki — Experience Gem](https://vampire.survivors.wiki/w/Experience_Gem),
    for enemy drops, Magnet collection, experience thresholds and the paused
    level-up offer.
  - **[P8]** [official Vampire Survivors Wiki — Level up](https://vampire.survivors.wiki/w/Level_up),
    for weighted unique options, new-item/upgrade application, slot and maximum-
    level eligibility and resume semantics.
  - **[P9]** [official Vampire Survivors Wiki — Evolution](https://vampire.survivors.wiki/w/Evolution),
    for mature base weapon, counterpart and eligible-chest requirements, plus
    the Mad Forest first-chest exception.
  - **[P10]** [official Vampire Survivors Wiki — Treasure Chest](https://vampire.survivors.wiki/w/Treasure_Chest),
    for boss drops, item-level rewards and conditional evolution settlement.
  - **[P11]** [official Vampire Survivors Wiki — Bloody Tear](https://vampire.survivors.wiki/w/Bloody_Tear),
    for Whip/Hollow Heart evolution and critical-hit healing.
  - **[P12]** [official Vampire Survivors Wiki — Health](https://vampire.survivors.wiki/w/Health),
    for the ordinary current-health, damage, healing and death boundary.
  - **[P13]** [official Vampire Survivors Wiki — The Reaper](https://vampire.survivors.wiki/w/The_Reaper),
    for post-limit spawn cadence and ordinary lethal run cleanup.
- Secondary build metadata:
  - **[S1]** [SteamDB build 24926490](https://steamdb.info/patchnotes/24926490/),
    used only to pin the reproducible Steam public-branch build corresponding
    to the creator-declared version; it is not treated as a rules authority.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P13` under the declared clean-save stage boundary; rules reasoning,
  not a direct-play claim.
- Claim IDs: `VS-001`–`VS-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly navigate Antonio through the continuous Mad
  Forest field. Movement selects spacing, pickup routes and which side of the
  automatic Whip geometry reaches a crowd; it does not issue an attack.
- Existing `ACT-140`: commit one option from each bounded paused level-up offer.
  The chosen weapon, passive or next level persists for the remainder of the
  run; clean-save scope removes metaprogression reroll controls.
- Claim IDs: `VS-004`–`VS-007`, `VS-012`.

### System Behaviour Genes

- Existing `SYS-004`: select unresolved enemy drops, level-up candidates and
  chest contents from their current eligible pools.
- Existing `SYS-299`: collected experience crosses increasing thresholds and
  advances Antonio's run-local character level, including his level-based Might.
- Existing `SYS-469`: death/result settlement clears the transient enemies,
  gems, health and build while retaining eligible clean-save unlock credit.
- New `SYS-572`: spawn authored Mad Forest enemy waves and bosses by stage time.
- New `SYS-573`: activate every equipped weapon from its own cooldown and
  targeting/geometry, applying damage and defeat without attack commands.
- New `SYS-574`: turn eligible enemy defeats into spatial Experience Gems and
  credit their value only when Magnet attraction/contact collects them.
- New `SYS-575`: pause at a crossed level threshold and sample a finite unique
  offer from the currently eligible weapon/passive/upgrade pool.
- New `SYS-576`: add the selected item or advance its level, recompute the
  run-local build and resume the stage.
- New `SYS-577`: settle a collected boss chest into an eligible item level or,
  when all gates hold, weapon evolution.
- New `SYS-578`: apply incoming damage and compatible healing to the single
  continuous health pool and close an early-death run.
- New `SYS-579`: mark the stage complete at `30:00`, dispatch the first Reaper
  and settle the ordinary completed-run result.
- Resolution order: advance the stage clock and spawn schedule; update movement,
  enemies and weapon cooldowns; resolve hits, damage and deaths; create and
  attract drops; credit XP; pause for any crossed level offer and apply its
  choice; resume until early death or stage completion/Reaper settlement.
- Claim IDs: `VS-002`–`VS-012`.

### Constraint Genes

- Existing `CON-188`: each paused level-up offer permits one persistent choice
  and removes the unselected alternatives when play resumes.
- New `CON-485`: new weapons and passives obey separate six-item ordinary
  level-up caps; owned maximum-level items and duplicate offer entries are
  ineligible.
- New `CON-486`: ordinary Whip evolution requires maximum-level Whip, Hollow
  Heart and a chest permitted to evolve at that Mad Forest time.
- New `CON-487`: positive health is required before `30:00`; reaching the stage
  limit first establishes completion before the Reaper cleanup.
- Scarce strategic resources: navigable open space, current health, time before
  the next density step, nearby uncollected XP, finite offer slots, weapon and
  passive capacity, item levels, boss-chest timing and route distance to Hollow
  Heart.
- Claim IDs: `VS-006`–`VS-011`.

### Information Genes

- Existing `INF-002`: exact future level-up offers, random drops and chest
  results are not previewed before their triggering transitions.
- Existing `INF-119`: Antonio's health, experience, level, attributes and
  current weapon/passive build are inspectable.
- New `INF-235`: the camera exposes nearby enemies, gems, stage items, chests
  and current weapon effects for local movement decisions.
- New `INF-236`: the HUD joins stage clock, kills, level/XP and current run-build
  progression; it does not reveal the complete later wave schedule.
- Claim IDs: `VS-004`–`VS-012`.

### Objective Genes

- New `OBJ-107`: survive normal Mad Forest from `0:00` until its `30:00` stage
  completion. Reaper defeat, gold, kill count, level and later unlocks are not
  required success conditions.
- Claim IDs: `VS-003`, `VS-011`, `VS-012`.

### Time Genes

- Existing `TIM-003`: enemies, weapon clocks, damage, drops and the authored
  stage clock advance in real time while movement remains available. Level-up
  selection pauses that forced progression as an interrupting planning state;
  it does not turn the run into discrete turns.
- Claim IDs: `VS-003`–`VS-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty save slot, Antonio and normal Mad Forest are selected | Enter the stage | The first controllable frame begins at `0:00` with Whip and no purchased PowerUps | entry is reproducible and does not import later unlock state | `VS-001`–`VS-003` |
| Enemies approach while Whip is ready | Move without pressing an attack control | Whip releases on its own cadence across its current horizontal geometry and applies hits | movement and weapon execution are distinct | `VS-004` |
| One automatic weapon hit defeats an ordinary enemy | Approach the resulting gem | Magnet attraction pulls the Experience Gem into Antonio and increments the run XP counter | reward conversion is spatial, not immediate kill XP | `VS-005` |
| Collected XP crosses the next threshold | Give no movement input while the offer is open | Stage progression pauses and three or four unique eligible item choices appear | level-up is a bounded interrupting draft | `VS-006` |
| One offered new base weapon is eligible and its class has capacity | Commit that option | It occupies a weapon slot, joins the automatic cooldown portfolio and live play resumes | choice rewrites later automatic coverage | `VS-006`, `VS-007` |
| One owned item is offered below maximum level | Select the owned item | Its next declared level applies and the item's compatible effects change immediately | upgrades persist only in the current run | `VS-006`, `VS-007` |
| Six ordinary level-up weapons are already held | Cross another level threshold | No seventh new ordinary weapon is offered, though eligible owned upgrades remain possible | capacity constrains the random offer pool | `VS-007` |
| A scheduled Mad Forest minute boundary arrives | Continue moving | The authored enemy type, density and any boss for that minute enter the live field | pressure is clock-indexed rather than purely random | `VS-008` |
| Maximum-level Whip and Hollow Heart are held | Collect an evolution-capable boss chest | Whip is removed and Bloody Tear occupies its weapon role with evolved behaviour | evolution is gated replacement, not ordinary levelling | `VS-009` |
| Antonio has missing health and Bloody Tear lands an eligible critical hit | Give no healing command | The compatible critical-hit heal restores health up to the allowed cap | automatic combat can feed the same survival resource | `VS-010` |
| Health reaches zero at `29:59` with no revival | Give no further input | The attempt closes without stage completion and transient build state is cleared | early death is failure | `VS-010`, `VS-011` |
| Antonio remains alive as the normal clock reaches `30:00` | Continue surviving | Mad Forest is marked complete; a Reaper spawns and ordinary death/result settlement follows | completion precedes cleanup and does not require killing Reaper | `VS-011` |

## Strategic and experiential structure

- Local decision: choose a direction that preserves an escape corridor, keeps
  the Whip's horizontal slash on a dense edge and collects nearby gems without
  crossing more contact damage than the XP is worth.
- Medium-term planning: select items whose cadence, area, damage and defence
  cover complementary directions; balance new slots against upgrading reliable
  tools; route toward Hollow Heart and return for boss chests only when crowd
  shape permits.
- Long-term structure: grow the automatic portfolio faster than Mad Forest's
  authored density curve, converting dangerous gem fields into repeated build
  choices while preserving enough health and open ground for the final minutes.
- Common heuristics: orbit rather than reverse through the densest line; collect
  compact gem clusters; prefer coherent upgrades over filling every slot early;
  use Whip's facing geometry deliberately; do not treat optional evolution as
  more important than surviving the current wave.
- Failure attribution: the visible field distinguishes late routing and contact
  traps; the HUD exposes health, time and build; the paused offer makes the
  selected upgrade explicit, while future offers and off-screen density retain
  uncertainty.
- Player-trust factors: attacks need no hidden fire input, weapon levels state
  their changes, local pickups remain visible, and the stage clock makes the
  survival horizon legible even though reward offers are random.
- Claim IDs: `VS-004`–`VS-012`.

## Replay and variation

- What changes between sessions: random level-up options, drops and chest
  contents; exact crowd geometry; which base items enter the build; upgrade
  order; whether the optional Whip evolution becomes available early enough.
- Randomness or procedural generation: reward and offer selection vary, while
  the selected stage's broad minute schedule, fixed stage items and time limit
  remain authored.
- Multiple viable strategies: dense damage, knockback/area control, movement
  safety, recovery or evolution-focused builds can all serve the same `30:00`
  terminal.
- Typical replay motive: survive more consistently, refine pickup routes, test
  another base-game build or later pursue excluded unlocks and stages.
- Claim IDs: `VS-005`–`VS-012`.

## Adjacent systems and history

- The Binding of Isaac: Rebirth also combines direct movement, random run-local
  items, visible health/build and terminal reset. It requires aimed attacks,
  generated room routing, keys/bombs/coins and floor bosses; Vampire Survivors
  removes the attack command and turns enemy density, XP pickup and a fixed
  survival clock into the decision substrate.
- Loop Hero also delegates combat and allows live build intervention. Its hero
  walks a fixed circuit, equipment drops are replaced directly and the player
  places encounter-producing world cards; Antonio is freely steered through an
  open field and repeatedly drafts the automatic portfolio from collected XP.
- Project Zomboid shares continuous health/survival pressure but has no authored
  victory duration and retains a persistent survivor/world history. This scope
  completes at a fixed stage clock and discards the transient run build.
- DLC, co-op, Adventures, Arcanas and Endless mode are variants requiring
  independent versioned scopes rather than silent additions to this signature.
- Claim IDs: `VS-001`–`VS-012`.

## Taxonomy impact

- Fourteen new active boundaries are added: eight System Behaviours, three
  Constraints, two Information genes and one Objective.
- Nine existing generic genes are reused without changing their definitions or
  any earlier reviewed signature.
- `COMB-0181` records the strict movement–automatic-weapon–XP-draft–survival
  interaction. No existing combination or family boundary is changed.

## Negative results

- `SYS-051` is not reused because Antonio is never locked into a contextual
  autonomous encounter; weapon clocks remain active across one open field.
- `SYS-215` is not reused because no attack is directly commanded or aimed.
- `SYS-222` is not reused because Experience Gems increment an abstract XP
  counter rather than entering carried inventory.
- `CON-175` is not reused because health does not persist between discrete run
  nodes; this packet has one continuous stage and a clock-ordered terminal.
- `TIM-016` is not reused because `30:00` completes and settles the run rather
  than resetting a repeating world cycle.
- DLC, co-op, Adventures, Arcanas, later unlocks and Endless are excluded rather
  than unioned into a single live-service signature.
