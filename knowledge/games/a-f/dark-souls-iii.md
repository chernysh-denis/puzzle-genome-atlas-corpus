---
game_id: GAME-0262
slug: dark-souls-iii
game_title: DARK SOULS™ III
analysis_status: reviewed
reviewed: 2026-09-05
combination_ids:
  - COMB-0260
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-199
    - ACT-200
    - ACT-224
    - ACT-249
    - ACT-436
    - ACT-437
    - ACT-438
  system:
    - SYS-215
    - SYS-364
    - SYS-399
    - SYS-578
    - SYS-798
    - SYS-799
  constraint:
    - CON-282
    - CON-286
    - CON-352
    - CON-354
    - CON-604
  information:
    - INF-119
    - INF-128
    - INF-317
    - INF-318
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: DARK SOULS™ III

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `374320`, one-app standalone package `69024`, official PC `App Ver. 1.15.2`
  with `Regulation Ver. 1.35` dated 2023-01-12, observed against public branch
  build `10167187` whose branch record was last updated on the same date;
  checked 2026-09-05. The semantic application and regulation versions are the
  publisher's own claim; the numeric build identifier is a secondary
  distribution observation and is never treated as a publisher statement.
- Product boundary: this is **DARK SOULS III** on Windows, not DARK SOULS
  Remastered, DARK SOULS II, Elden Ring, Sekiro, a console release, a community
  client or a franchise union. The Deluxe package `94174` and its Season Pass
  apps `442010`, `506970` and `506971` are separate products whose rules are
  outside this packet even for an owner.
- Platform, input and difficulty: English interface, Windows, keyboard and
  mouse, offline play with no summoning, invasion or covenant activity. DARK
  SOULS III exposes no selectable difficulty setting, so the ruleset is fixed
  by the product rather than chosen; the declared route is the fresh base-game
  first playthrough, never New Game Plus.
- Setup-only predecessor: create a new character with the `Knight` starting
  class and decline the optional burial gift. Character creation establishes a
  fixed starting armament, protective equipment and attribute spread but
  contributes no genes or transitions to this packet.
- Entry: accept first ordinary control at the `Cemetery of Ash` after the
  character rises from the grave, before reading the first placed ground
  instruction. Record current health, the shared exertion reserve, carried
  Estus charges and carried souls before the first movement.
- Primary decision loop: read the current placed ground instruction and local
  geometry; walk, run, sprint and roll through the graveyard route; select or
  release a lock-on bind against one eligible hostile; spend the shared
  exertion reserve between light strikes, strong strikes, rolls, sprints and a
  held frontal guard, and let the reserve refill while disengaged; collect and
  equip reachable items including the second flask found at the flooded ruins;
  drink an Estus charge only when the interruptible animation is safe; rest at
  the `Cemetery of Ash` checkpoint to refill health and Estus and repopulate
  ordinary enemies; take the sword lodged in the immobile route guardian to
  seal the encounter; fight the guardian through its health-threshold
  transformation while reading its named remaining-health bar; and on death
  return to the last rested checkpoint and reclaim the single bloodstain before
  another death replaces it.
- Positive terminal: after defeating the route guardian and receiving the
  Coiled Sword, cross the opened doors, follow the descending route and use the
  Coiled Sword to ignite the `Firelink Shrine` bonfire. Rest at that newly lit
  checkpoint, quit to the main menu, load the same save and verify the retained
  lit `Firelink Shrine` checkpoint, retained carried souls and unchanged
  character level. Stop before spending any souls.
- Negative terminal: health reaching zero ends the current attempt; the
  character returns to the last rested checkpoint, ordinary enemies repopulate,
  and all carried souls remain in one bloodstain at the death position. Dying
  again before touching that bloodstain destroys its contents permanently.
  Defeating the guardian, reaching the shrine or seeing the bonfire without the
  stated ignition, rest and reload check is not success.
- Included: direct third-person traversal, sprinting and the directional
  evasive roll; light and strong melee strikes; the held frontal shield guard;
  the selectable lock-on bind; reachable item pickup and equipping; the
  interruptible Estus Flask; checkpoint rest with its resource refill and enemy
  repopulation; the shared exertion reserve that prices attack, evasion, sprint
  and guard; the continuous health pool; death returning to the checkpoint and
  storing souls in one recoverable bloodstain; the single-mark replacement
  rule; the authored gate that opens the route only after the guardian falls;
  the sealed guardian's health-threshold transformation; placed ground
  instructions; personal resource display; ground-item disclosure; and the
  reload-verified shrine settlement.
- Excluded: character creation choices beyond the declared fixed setup; every
  Season Pass area and its rules; online summoning, invasion, covenants,
  messages written by other players, bloodstain replays and phantom activity;
  New Game Plus and every later playthrough cycle; levelling, purchasing,
  weapon upgrade, infusion, spell attunement, pyromancy, miracles, sorcery,
  ember state, bonfire warp and every mechanic first reachable after the
  terminal; parry, riposte, backstab and guard-break criticals, which the
  product exposes but which this route neither requires nor evidences; the
  Ravenous Crystal Lizard and every optional detour; all later areas, bosses,
  merchants and characters; equipment-load tiers and armour swapping beyond the
  fixed starting loadout; controller and console input; screenshots, official
  artwork, third-party assets, video and audio evidence.
- Reproducible parameterisation: install English app `374320` from standalone
  package `69024`, confirm `App Ver. 1.15.2` / `Regulation Ver. 1.35`, play
  offline, create a `Knight` with no burial gift and retain default keyboard
  and mouse bindings. From first `Cemetery of Ash` control, read at least one
  placed ground instruction, collect the flask at the flooded ruins, defeat at
  least one Grave Warden using at least one roll, one held guard and one lock-on
  bind, deliberately die once to create and then reclaim a bloodstain, rest at
  the `Cemetery of Ash` checkpoint, take the lodged sword, defeat the route
  guardian across its transformation, then ignite, rest at and reload the
  `Firelink Shrine` checkpoint. Exact soul totals, health values, exertion
  values, hostile positions, roll timings and encounter duration are parameters.
- Potential scoped modules: one later named area and its guardian; the Season
  Pass areas; an online summoning, invasion or covenant ruleset; the levelling,
  upgrade and infusion economy; a New Game Plus cycle; or a different starting
  class each requires its own version, entry, loop, terminal and evidence.
- Direct-play status: not conducted. Valve application and package data plus the
  current Steam product record establish lawful availability, exact product
  identity, Windows support, package composition, the separated Season Pass
  apps and the Deluxe boundary. Bandai Namco's own patch page supplies the
  semantic application and regulation versions. The public SteamCMD info
  projection supplies one dated secondary build observation. Four independent
  static written reference pages plus one independent static route corroborate
  the area layout, checkpoint position, item placement, guardian trigger,
  transformation, drop and shrine transition, and four further static reference
  pages corroborate the exertion, guard, lock-on, flask, checkpoint and death
  rules. This is an evidence-backed rules reconstruction, not a claimed
  playthrough or entitlement. No video or audio was opened, played, heard,
  analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DS3-001` | Steam app `374320` and one-app standalone package `69024` identify the currently lawfully offered English Windows product, distinct from the Deluxe package and its Season Pass apps | Confirmed | Direct | High | P1–P3 |
| `DS3-002` | The publisher's current PC version is `App Ver. 1.15.2` with `Regulation Ver. 1.35`, dated 2023-01-12, and the public branch record carries build `10167187` last updated on the same date | Confirmed | Corroborated | High | P4, S1 |
| `DS3-003` | The product exposes no selectable difficulty setting, so the analysed ruleset is fixed rather than chosen, while the burial gift at character creation is optional | Observation | Corroborated | High | P1, S9 |
| `DS3-004` | A fresh route begins in the `Cemetery of Ash`, passes a checkpoint before the guardian arena, and ends at `Firelink Shrine` | Observation | Corroborated | High | S2, S10 |
| `DS3-005` | Fixed developer-authored messages placed on the ground disclose the controls relevant at those positions | Observation | Corroborated | High | S2, S10 |
| `DS3-006` | One shared exertion reserve is spent by almost every action except walking, refills automatically over time, may be overdrawn below zero and recovers more slowly while a guard is held | Confirmed | Corroborated | High | S4, S5 |
| `DS3-007` | Light strikes cost less of that reserve than strong strikes, and guarding spends it in proportion to the equipment's stability | Observation | Corroborated | High | S4 |
| `DS3-008` | A directional roll grants a protected interval at the start of its animation and is the recommended answer to an incoming attack | Observation | Corroborated | High | S4 |
| `DS3-009` | A held shield guard reduces incoming damage by an equipment-dependent share at the cost of the same reserve | Observation | Corroborated | High | S4, S8 |
| `DS3-010` | The player can bind the camera and facing to one nearby hostile so the character continues to face it while moving | Observation | Corroborated | High | S4 |
| `DS3-011` | The Estus Flask restores health, starts the game with a bounded number of charges, refills at a checkpoint and is consumed through a vulnerable uninterruptible-by-default animation during which the world continues | Observation | Corroborated | High | S6, S8 |
| `DS3-012` | Resting at a checkpoint restores health and Estus charges, sets the respawn position and resurrects most defeated ordinary enemies in the area | Observation | Corroborated | High | S7, S8 |
| `DS3-013` | Death returns the character to the last rested checkpoint and leaves all carried souls in a single visible mark at the death position | Confirmed | Corroborated | High | S8 |
| `DS3-014` | Only one such mark persists; dying again before reclaiming it replaces the mark and permanently destroys the earlier stock | Confirmed | Corroborated | High | S8 |
| `DS3-015` | Taking the sword lodged in the immobile guardian starts the sealed encounter, which awards souls and the Coiled Sword on defeat | Observation | Corroborated | High | S3, S10 |
| `DS3-016` | Below a remaining-health threshold the guardian grows a further form with additional attacks inside the same encounter | Observation | Corroborated | High | S3 |
| `DS3-017` | Defeating the guardian opens the route to `Firelink Shrine`, whose checkpoint is ignited with the Coiled Sword | Observation | Corroborated | High | S2, S10 |
| `DS3-018` | The lit shrine checkpoint, retained souls and unchanged character level survive a quit and reload, making that state a reproducible positive terminal | Confirmed | Corroborated | High | S7, S8, S10 |
| `DS3-019` | The bounded identity is one shared exertion reserve pricing offence, evasion and defence together, settled by a transforming sealed guardian whose defeat opens a reload-verified checkpoint | Strong Pattern | Corroborated | High | `DS3-004`–`DS3-018` |

## Basic data

- Release / origin: FromSoftware, Inc.; published on Windows by FromSoftware,
  Inc. and Bandai Namco Entertainment on 2016-04-11.
- Platform or physical form: lawfully offered English Windows Steam application
  `374320`; one fresh offline base-game `Cemetery of Ash` to `Firelink Shrine`
  packet.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-05:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=374320&cc=ua&l=english),
    for the exact title, app, Windows support, developers, publishers, release
    date, categories, the absence of a difficulty setting among its declared
    features, the three separate DLC apps and the current Ukraine offer.
  - **[P2]** [Valve standalone-package data](https://store.steampowered.com/api/packagedetails?packageids=69024&cc=ua&l=english),
    for package `69024` containing only app `374320`, its Windows-only platform
    support and its current Ukraine offer.
  - **[P3]** [current Steam product page](https://store.steampowered.com/app/374320/DARK_SOULS_III/?l=english),
    for lawful availability, the standalone versus Deluxe edition separation,
    the named Season Pass, `Ashes of Ariandel` and `The Ringed City` products
    and the single-player and co-op categories. Embedded media was not opened
    or used.
  - **[P4]** [Bandai Namco patch page for version 1.15.2](https://www.bandainamcoent.com/news/dark-souls-3-patch-v1152),
    for the publisher's own `App Ver. 1.15.2`, `Regulation Ver. 1.35`, PC
    platform and the 2023-01-12 date.
- Corroborating textual sources, accessed 2026-09-05:
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/374320),
    for public branch build `10167187` and its branch timestamps. This mirrors
    Valve's public product data and is treated as a secondary distribution
    observation, not a publisher claim.
  - **[S2]** [static Cemetery of Ash reference](https://darksouls3.wiki.fextralife.com/Cemetery+of+Ash),
    for the starting area, its two checkpoints, Grave Warden enemies, the placed
    control messages, the guardian and the transition through the large doors
    to `Firelink Shrine`.
  - **[S3]** [static route-guardian reference](https://darksouls3.wiki.fextralife.com/Iudex+Gundyr),
    for the immobile starting state, the sword-removal trigger, the awarded
    souls and Coiled Sword, and the health-threshold second form.
  - **[S4]** [static combat reference](https://darksouls3.wiki.fextralife.com/Combat),
    for the differing exertion cost of light and strong strikes, dashing cost,
    stability-dependent guard cost, the roll's protected opening interval and
    the lock-on bind that keeps the character facing a selected foe.
  - **[S5]** [static exertion-reserve reference](https://darksouls3.wiki.fextralife.com/Stamina),
    for the reserve being spent by every action except walking, its automatic
    load-dependent regeneration, its negative overdraw floor and the reduced
    recovery rate while blocking.
  - **[S6]** [static flask reference](https://darksouls3.wiki.fextralife.com/Estus+Flask),
    for health restoration, the bounded starting charge count, refill at
    checkpoints and the vulnerable non-pausing consumption animation.
  - **[S7]** [static checkpoint reference](https://darksouls3.wiki.fextralife.com/Bonfires),
    for the health and flask restoration, the resurrection of most defeated
    enemies and the checkpoint menu.
  - **[S8]** [static new-player reference](https://darksouls3.wiki.fextralife.com/New+Player+Help),
    for respawning at the last rested checkpoint, the guard control, flask
    replenishment and the single-mark death rule with its permanent loss on a
    second death.
  - **[S9]** [static burial-gift reference](https://darksouls3.wiki.fextralife.com/Burial+Gifts),
    for the nine offered gifts, the fact that selecting one is optional and its
    restriction to a new game.
  - **[S10]** [independent static Cemetery of Ash route](https://gamerwalkthroughs.com/dark-souls-3/cemetery-of-ash/),
    for the ordered route, the placed control marks, the flask found near the
    broken fountain, the checkpoint position, the guardian trigger and
    transformation, the Coiled Sword drop and the descent to the shrine. Images
    and embedded media were not opened or used.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P4` and `S1`–`S10` under the declared app, package, version, platform,
  input, offline state, fixed setup, exclusions and retained terminal; rules
  reasoning, not direct play.
- Claim IDs: `DS3-001`–`DS3-019`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: walk, run, sprint and traverse the authored graveyard
  route; `ACT-161`: aim and commit a light or strong melee strike against a
  reachable hostile; `ACT-199`: collect a reachable item and transfer or equip
  it into a compatible slot; `ACT-200`: commit one interruptible Estus
  treatment; `ACT-224`: rest at an activated checkpoint and accept its recovery
  and world-reset consequences.
- Existing `ACT-249`: reach and touch the active death mark to reclaim its
  stored souls before another death replaces it.
- New `ACT-436`: commit one directional evasive roll whose price is drawn from
  the shared exertion reserve rather than a cooldown. No existing action gene
  covered an evasion priced from the same reserve as attacking; `ACT-356`
  requires a dodge whose cost is its own cooldown and reset state, which is a
  different decision.
- New `ACT-437`: raise and hold the equipped shield toward the current facing
  so incoming strikes are absorbed against the exertion reserve. `ACT-349`
  requires the player to aim a guard toward one selected incoming attack
  direction, which this product does not ask for; no other gene covered a
  non-directional held absorb.
- New `ACT-438`: bind the camera and attack facing to one selected eligible
  hostile and release it at will. `ACT-405` and `SYS-747` describe a retained
  actor mark that survives occlusion and the encounter, which is a different
  boundary; nothing existing covered a reversible movement-reorganising bind.
- Actor, area, weapon, shield, item, class and exact quantity names remain
  parameters. Claims: `DS3-004`–`DS3-015`.

### System Behaviour Genes

- Existing `SYS-215`: directly controlled combatants exchange range-, cadence-,
  damage- and defeat-dependent effects while the world continues in real time;
  `SYS-578`: strikes reduce one continuous health pool, Estus restores missing
  health and zero ends the current attempt.
- Existing `SYS-364`: resting at the checkpoint restores health and flask
  charges and repopulates defeated ordinary enemies in the linked area;
  `SYS-399`: ordinary death returns the character to that checkpoint while
  storing the carried spendable currency in one recoverable world mark.
- New `SYS-798`: one continuous personal exertion reserve is drawn on by
  attacks, rolls, sprints and guarding and refills automatically while it is
  not being spent. No existing system gene modelled a single automatically
  recovering reserve that prices offence, evasion and defence together;
  `SYS-632` and `CON-435` describe survival meters, and `SYS-687` describes an
  opponent's exhaustion rather than the player's action budget.
- New `SYS-799`: below a declared remaining-health threshold the sealed
  guardian assumes a further form with additional attacks inside the same
  encounter. `SYS-409` explicitly excludes a boss phase change, and `SYS-420`
  is bound to one specific night-summoned opponent, so neither boundary fits.
- Resolution order: movement and the lock-on bind change reach and facing;
  every attack, roll, sprint or guard first tests and then spends the exertion
  reserve; contact resolves the strike against health or the held guard; the
  reserve refills while disengaged, more slowly while the guard is held; the
  guardian's accumulated damage crossing its threshold triggers the
  transformation without resetting the encounter; zero health returns the
  character to the checkpoint and stores souls in one mark; resting restores
  resources and repopulates enemies; and the guardian's defeat opens the gate
  to the shrine settlement. Claims: `DS3-006`–`DS3-018`.

### Constraint Genes

- Existing `CON-354`: a weapon move resolves only when its current exertion
  requirement and previous-animation recovery state permit it; `CON-286`: the
  flask produces its effect only with missing health and a completed, uncancelled
  animation.
- Existing `CON-352`: only one unrecovered death-currency mark may persist, so
  a second death permanently destroys the earlier stock; `CON-282`: the route
  to the shrine opens only after the authored guardian gate is satisfied.
- New `CON-604`: a roll, sprint or held guard may begin or continue only while
  the shared reserve retains a sufficient positive balance, so overspending on
  attacks withdraws defensive options until it recovers. `CON-354` governs only
  weapon moves, and no existing constraint bound defensive legality to the same
  reserve.
- Scarce resources: health, Estus charges, the exertion reserve at every
  instant, the single unreclaimed soul mark, checkpoint-local progress and the
  positional distance back to the mark. Exact values are parameters. Claims:
  `DS3-006`–`DS3-018`.

### Information Genes

- Existing `INF-119`: current health, the exertion reserve, carried souls and
  equipped state remain visible; `INF-128`: reachable ground items and the
  inventory expose identity, quantity and compatibility before transfer.
- New `INF-317`: fixed developer-authored messages placed at world positions
  disclose the control or hazard relevant there without tracking progress or
  reporting completion. `INF-268` requires a tutorial adviser that states the
  current objective and reports its completion, which this product does not do.
- New `INF-318`: the sealed encounter names the guardian and continuously
  exposes its remaining share of health. `INF-157` deliberately withholds exact
  monster health, `INF-165` is bound to one specific opponent's night state,
  and ordinary field enemies here expose no such surface.
- Exact bar geometry, message wording, fonts, icons, bindings and interface
  positions are presentation parameters. Claims: `DS3-005`, `DS3-006`,
  `DS3-013`, `DS3-016`.

### Objective Genes

- Existing `OBJ-080`: complete the bounded authored route by defeating its
  mandatory guardian and crossing the newly opened threshold into the next
  declared region, here the ignited and reload-verified `Firelink Shrine`
  checkpoint.
- Reaching the shrine, seeing the unlit checkpoint or receiving the Coiled
  Sword without the stated ignition, rest and reload check is not success.
  Claims: `DS3-017`–`DS3-019`.

### Time Genes

- Existing `TIM-003`: movement, strikes, rolls, guard, exertion recovery, flask
  consumption and the guardian's attacks all advance in real time while inputs
  remain accepted.
- Claims: `DS3-006`–`DS3-018`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A new `Knight` character with no burial gift has just risen from the grave | Accept first ordinary control in the `Cemetery of Ash` | The route begins with the fixed starting loadout and no imported cycle state | fixed clean entry | `DS3-003`, `DS3-004` |
| The character stands on a fixed developer-authored ground message | Read it | The message discloses the control relevant at that position and reports no progress or completion | position-delivered instruction | `DS3-005` |
| The exertion reserve is full and a hostile is in range | Commit one light strike, then one strong strike | The strong strike removes a larger share of the same reserve, and neither can begin without a sufficient balance | shared action budget | `DS3-006`, `DS3-007` |
| An attack is incoming and the reserve retains a sufficient balance | Commit a directional roll | The character displaces and is protected during the opening interval of the animation, and the reserve is reduced | exertion-priced evasion | `DS3-006`, `DS3-008` |
| An attack is incoming and a shield is equipped | Hold the guard toward the attack | The strike is absorbed at an equipment-dependent share against the reserve rather than falling wholly on health, and the reserve recovers more slowly while the guard is held | exertion-priced defence | `DS3-006`, `DS3-009` |
| The reserve has been overspent | Attempt another roll, sprint or guard | The action is withdrawn until the reserve recovers, while ordinary walking remains available | defensive legality gate | `DS3-006` |
| One eligible hostile is nearby | Bind the view to it, move, then release the bind | The character keeps facing that actor while moving and returns to free facing on release, without marking or revealing it | reversible facing bind | `DS3-010` |
| Health is below its cap and an Estus charge remains | Drink | Missing health is restored while the world continues, so an incoming strike during the animation can interrupt the exchange | vulnerable recovery | `DS3-011` |
| The `Cemetery of Ash` checkpoint has been activated | Rest at it | Health and flask charges refill, the respawn position is set, and most defeated ordinary enemies in the area return | checkpoint reset trade | `DS3-012` |
| Souls are carried and health reaches zero | Continue | The character returns to the last rested checkpoint and all carried souls remain in one mark at the death position | recoverable death currency | `DS3-013` |
| One unreclaimed mark exists | Die again before touching it | A new mark replaces the old one and the earlier stock is permanently destroyed | single-mark replacement | `DS3-014` |
| One unreclaimed mark exists and the character reaches it | Touch the mark | The stored souls return to the living character and the mark is removed | mark recovery | `DS3-013` |
| The immobile guardian holds a sword in its chest | Take the sword | The encounter seals and the guardian becomes active, with its name and remaining health exposed | sealed encounter entry | `DS3-015`, `DS3-016` |
| The guardian's remaining health crosses its threshold | Continue the same encounter | A further form with additional attacks emerges while the seal, accumulated damage and encounter identity persist | mid-encounter transformation | `DS3-016` |
| The guardian is defeated | Collect the drop and pass the opened doors | Souls and the Coiled Sword are awarded and the previously closed route to the shrine becomes traversable | guardian-gated threshold | `DS3-015`, `DS3-017` |
| The shrine's unlit checkpoint is reachable and the Coiled Sword is carried | Ignite it, rest, quit and load the save | The same lit checkpoint, carried souls and unchanged character level return | reproducible positive terminal | `DS3-018`, `DS3-019` |

## Strategic and experiential structure

- Planning horizon: the placed instructions and visible route expose the next
  stretch, while health, remaining Estus charges, the current exertion balance
  and the position of any unreclaimed mark determine whether to advance,
  retreat, rest or recover.
- Local tactics: keep a reserve margin large enough for one roll before
  committing a strong strike, release the guard to let the reserve recover,
  bind the view when a single hostile dictates spacing and release it when
  several do, and drink only after the opponent's recovery leaves a safe window.
- Medium-term structure: resting is never free, because it repopulates the
  ordinary enemies between the checkpoint and the guardian, so the player
  chooses between a full flask with a repeated route and a depleted flask with
  a cleared one.
- Reversible versus irreversible: movement, guard, lock-on and exertion spend
  are reversible within seconds; Estus charges and health are spent until a
  rest; a second death before recovery destroys the accumulated souls
  permanently; the guardian's defeat and the ignited shrine checkpoint persist.
- Failure attribution: the visible reserve, health and remaining charges make a
  loss traceable to a specific overspend, a mistimed roll, a guard held too
  long or an interrupted drink, rather than to hidden randomness.
- Player trust: the reserve, health and mark position are always displayed, the
  guardian's transformation is announced by its own visible remaining health,
  the single-mark rule is stated by the interface before it applies, and the
  reloaded save reproduces the settled state exactly.

## Replay and variation

- What changes: route order, which hostiles are engaged, exertion allocation,
  number of rolls versus guards, flask timing, how many deaths occur and
  whether a mark is reclaimed.
- Randomness or procedural generation: topology, enemy placement, item
  placement, the guardian and its threshold are authored. Minor attack
  selection varies; no procedural-generation claim enters this packet.
- Multiple strategies: the route admits engaging or avoiding each Grave Warden,
  answering attacks with rolls or with the guard, and resting or pressing on.
  The control demonstrates one of each rather than making a no-death or
  no-rest route the terminal.
- Typical replay motive: reach the guardian with more Estus charges and a
  cleaner exertion budget, and settle the transformation without spending the
  bloodstain cycle.

## Adjacent systems and history

- Black Myth: Wukong shares direct real-time melee, an interruptible
  restorative, checkpoint rest with enemy repopulation, an authored gate and a
  route guardian. It resolves offence through staff stances, a focus resource
  and unlocked spells, and its checkpoint carries no death-currency mark; this
  packet instead prices attack, evasion, sprint and guard from one reserve and
  makes the death mark itself a decision.
- Elden Ring shares the same publisher lineage, the recoverable death mark, the
  single-mark rule and checkpoint rest. Its packet is an open traversal scope
  with a mount, spirit summons, levelling, flask allocation and a world map;
  this bounded linear route excludes all of those and isolates the reserve, the
  guard and the transforming sealed guardian.
- STAR WARS Jedi: Fallen Order shares authored traversal, direct melee and
  checkpoint recovery, but organises its defence around a timed deflection and
  a separate force resource rather than one shared reserve.
- Hollow Knight: Silksong shares an authored route, a mandatory guardian and a
  recovered loss on death, but resolves movement and defence through
  two-dimensional geometry and a charge-based heal rather than a continuous
  exertion budget.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-199`, `ACT-200`, `ACT-224`, `ACT-249`, `ACT-436`, `ACT-437`, `ACT-438` | class, weapon, shield, item, area and actor names are parameters |
| System Behaviour | `SYS-215`, `SYS-364`, `SYS-399`, `SYS-578`, `SYS-798`, `SYS-799` | reserve capacity, regeneration rate, damage values and thresholds are parameters |
| Constraint | `CON-282`, `CON-286`, `CON-352`, `CON-354`, `CON-604` | costs, balances, charge counts and gate order are parameters |
| Information | `INF-119`, `INF-128`, `INF-317`, `INF-318` | bar geometry, message wording and interface layout are parameters |
| Objective | `OBJ-080` | guardian, threshold and settled checkpoint are parameters |
| Time | `TIM-003` | animation, recovery and regeneration timing are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `261` (`GAME-0001`–`GAME-0261`).
- Exact genome matches: none.
- Tied near matches: `GAME-0189` — Black Myth: Wukong (`12 / 43 = 0.279070`).
- Supported combination subsets: `COMB-0260`.
- Scan date: 2026-09-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0189` — Black Myth: Wukong | `ACT-008`, `ACT-161`, `ACT-200`, `ACT-224`, `SYS-215`, `SYS-364`, `CON-282`, `CON-286`, `CON-354`, `INF-119`, `OBJ-080`, `TIM-003` | Both advance one authored route through directly commanded real-time melee, spend an interruptible restorative, rest at a checkpoint that repopulates ordinary enemies, and settle by defeating a mandatory guardian and crossing its opened threshold. Wukong widens the packet with staff stance selection, an accumulating focus resource, unlocked spells and a transformation the player invokes. This packet instead makes one shared exertion reserve price attack, evasion, sprint and guard simultaneously, adds a reversible facing bind, exposes the guardian's own remaining health, transforms that guardian at a threshold the player did not choose, and turns death into a single recoverable currency mark that a second death destroys. | Near, `0.279070` |

### Preserved research notes

- New genes: `ACT-436`, `ACT-437`, `ACT-438`, `SYS-798`, `SYS-799`, `CON-604`,
  `INF-317`, `INF-318`.
- Reused genes: the remaining 18 admitted genes in the Normalised genome.
- Classification result: `New gene`.
- Lower-ID scan: reuse `ACT-249` + `SYS-399` + `CON-352` for the death mark
  rather than creating a souls-named gene; reuse `ACT-224` + `SYS-364` for the
  checkpoint rest trade; reuse `CON-354` for the attack exertion gate and add
  `CON-604` only for the defensive half it explicitly excludes. Reject a
  bonfire-, Estus-, souls-, Lothric- or Gundyr-named gene; reject a parry or
  riposte gene because this route neither requires nor evidences one; reject an
  equipment-load gene because the packet fixes one loadout; reject a levelling
  or upgrade gene because both lie after the terminal.

## Taxonomy impact

- Registry changes: add `ACT-436`, `ACT-437`, `ACT-438`, `SYS-798`, `SYS-799`,
  `CON-604`, `INF-317`, `INF-318` and `COMB-0260`, plus independent evidence
  for 18 reused genes. Generalise only the wording of `ACT-249` from a
  product-specific rune label to the same portable death-currency boundary; its
  definition semantics, lifecycle and all earlier signatures remain unchanged.
- Taxonomy-change record: none; no split, merge, deprecation, lifecycle change
  or signature change.
- Candidate terms: recorded in `CANDIDATE_TERMS.md`; all product, area, actor,
  weapon, item, class, app, package, build and version names remain parameters.

## Negative results

- No video or audio evidence was used; only official static text and data plus
  static written references support this packet.
- The Season Pass areas, online play, New Game Plus, levelling, upgrading,
  infusion, attunement and bonfire warp are excluded even though the product
  exposes them elsewhere, because none is reachable before the declared
  terminal.
- Parry, riposte, backstab and guard-break criticals were considered and
  rejected for this packet: the product supports them, but the declared route
  neither requires them nor supplies bounded evidence that they occur in it, so
  `SYS-409` is not admitted.
- Equipment load and armour tiers were considered and rejected because the
  packet fixes one starting loadout, so no load decision is exercised.
- Reaching `Firelink Shrine` or receiving the Coiled Sword without igniting,
  resting at and reloading the checkpoint is not the terminal.

## Delta summary

## New facts

- [Confirmed/Observation | Direct/Corroborated | High] `DS3-001`–`DS3-019`: one
  bounded opening route prices offence, evasion, sprint and defence from a
  single recovering reserve and settles a transforming sealed guardian into a
  reload-verified checkpoint.

## New genes

- [Observation | Corroborated | High] `ACT-436`, `ACT-437`, `ACT-438`,
  `SYS-798`, `SYS-799`, `CON-604`, `INF-317`, `INF-318` — exertion-priced
  evasion and guard, a reversible facing bind, one shared exertion reserve, a
  threshold guardian transformation, the defensive exertion gate, placed
  positional instructions and the sealed guardian's health disclosure.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0260` — one shared exertion
  reserve pricing offence and defence together, settled by a transforming
  sealed guardian and a recoverable death-currency mark.

## Taxonomy changes

- [Observation | Direct/Corroborated | High] `ACT-249` receives a
  boundary-preserving portable label and wording generalisation; no prior
  signature or lifecycle changes.

## New questions

- Does a bounded route from a product without a difficulty setting expose the
  same exertion structure that difficulty-selectable action products encode as
  separate cooldown and resource genes?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0263` — God of War.
- Optimisation criterion: hold the real-time melee corridor fixed while
  replacing the shared exertion reserve with a recallable thrown weapon and a
  commanded autonomous companion.
- Expected information gain: separate weapon-state and companion-command genes
  from the exertion budget admitted here.
- Backlog impact: advances the recorded 261-to-270 horizon by one unit.

## Why this game

- [Hypothesis | Limited | High] The selection admitted this product for
  explicit contrast against the already reviewed Elden Ring. The completed scan
  confirms the contrast is real: the bounded linear route selects Black Myth:
  Wukong rather than Elden Ring as its nearest signature, and shares only the
  twelve-gene authored-route-and-guardian backbone with it.
