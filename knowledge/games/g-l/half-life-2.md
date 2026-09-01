---
game_id: GAME-0212
slug: half-life-2
game_title: Half-Life 2
analysis_status: reviewed
reviewed: 2026-09-01
combination_ids:
  - COMB-0210
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-199
    - ACT-341
  system:
    - SYS-146
    - SYS-215
    - SYS-339
    - SYS-348
    - SYS-369
    - SYS-705
    - SYS-706
  constraint:
    - CON-262
    - CON-285
    - CON-305
    - CON-556
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-271
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Half-Life 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam app `220`, public
  Build ID `19307283`, built 2025-07-21 and published 2025-07-23, checked
  2026-09-01; the base Half-Life 2 campaign on Normal difficulty, mouse and
  keyboard, one complete `We Don’t Go to Ravenholm…` chapter packet from
  `d1_town_01` through `d1_town_05` and its ordinary transition into
  `d2_coast_01` / `Highway 17`.
- Primary decision loop: read Gordon's health, HEV protection, suit power,
  active weapon, ammunition and local threats; traverse the authored town,
  rooftops, graveyard, mine and rail-side route; choose firearm, crowbar,
  grenade or Gravity Gun; pull, hold, place, drop or launch an eligible physics
  object; turn props, saw blades, explosive barrels and authored traps into
  paths, cover or attacks; survive headcrabs, zombies and the final rail-side
  opposition; follow Father Grigori's route cues and cross the retained chapter
  transition.
- Entry and exit: entry is the first retained Gordon control at the beginning
  of `d1_town_01` after the Black Mesa East passage has forced the Ravenholm
  detour; the Gravity Gun and carried campaign equipment are accepted as the
  chapter's authored entry state. Positive exit is the settled transition into
  `d2_coast_01`, where the `Highway 17` chapter begins. Gordon's death and
  checkpoint reload end only the failed attempt; they are not positive or
  alternate packet terminals.
- Included: first-person walking, sprinting, crouching, jumping and ladders;
  finite firearm magazines/reserves, weapon switching and reload; melee and
  thrown explosives; health, HEV protection, suit power and pickups; the
  ordinary Gravity Gun's aimed pull, attachment, view-relative hold, drop and
  launch; eligible movable, breakable and explosive props; physical collision
  and prop-to-hostile damage; authored blades, crushers, fire and environmental
  route mechanisms; local headcrab/zombie perception, pursuit and attacks;
  Father Grigori's scripted assistance; authored map gates, saves, checkpoints,
  death and reload; the final chapter transition.
- Excluded: every base-campaign chapter before Ravenholm and after first
  `Highway 17` control; Episodes One and Two, Lost Coast, Developer Commentary,
  Workshop campaigns, mods and Half-Life 2: Deathmatch; achievements, Lambda
  caches, exhaustive weapon/enemy tables, speedrun skips, glitches, console
  commands, cheats, manual map loading, alternate difficulties, controllers,
  Steam Deck, Linux, macOS and every non-PC port; whole-series or whole-campaign
  inventory and narrative union.
- Reproducible parameterisation: start an ordinary base-campaign New Game at
  `We Don’t Go to Ravenholm…` on Normal with Commentary disabled and no
  Workshop content; retain the chapter-supplied state. Record one legal Gravity
  Gun pull into attachment, one collision-safe hold and drop, one launched prop
  striking a hostile, one conventional weapon shot and reload, one pickup, one
  authored mechanism, one death/checkpoint restoration if naturally reached,
  and the transition to `Highway 17`. Exact health, ammunition, chosen props,
  hostile positions, save timing and completion time are run parameters.
- Potential scoped modules: Black Mesa East's Gravity Gun tutorial; the
  vehicle-centred `Highway 17`; one Combine-squad urban chapter; the complete
  base campaign; one declared Episode; Commentary mode; or a named Workshop
  campaign.
- Direct-play status: not conducted. Current Valve product/update material,
  Valve's published Source SDK 2013 code, Valve-hosted chapter documentation
  and the archived official guide establish the declared build, control and
  transition rules. The trace below is evidence-based rules reconstruction,
  not a claimed captured playthrough. No video or audio was opened, played,
  heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HL2-001` | The current Steam product is Half-Life 2; its public Windows branch is Build ID `19307283` after Valve's 2025-07-23 update | Confirmed | Corroborated | High | P1, P2, S1 |
| `HL2-002` | The 20th Anniversary default client integrates Episodes, Lost Coast, Commentary and Workshop, while the declared packet isolates the base campaign and disables those additions | Confirmed | Direct | High | P2 |
| `HL2-003` | `We Don’t Go to Ravenholm…` is the sixth base-game chapter, begins at `d1_town_01` and precedes `Highway 17` at `d2_coast_01` | Confirmed | Corroborated | High | P3, S2, S3 |
| `HL2-004` | Gordon directly traverses, switches weapons, aims, attacks, reloads, collects resources and activates authored route objects in real time | Observation | Corroborated | High | P1, P4, S4 |
| `HL2-005` | The ordinary Gravity Gun traces an eligible physics object, pulls it from distance, attaches it within range, maintains a collision-bounded held pose and can drop or launch it | Confirmed | Direct | High | P4 |
| `HL2-006` | Ordinary Gravity Gun pickup is bounded by object eligibility, physics state, line/range and maximum mass; flesh and explicitly forbidden objects are rejected | Confirmed | Direct | High | P4 |
| `HL2-007` | A player-launched physics prop receives force, returns to live collision and can produce attributed impact damage or hostile interaction | Confirmed | Direct | High | P4, P5 |
| `HL2-008` | Ravenholm supplies zombies, headcrabs, physical props, explosive barrels, saw blades, traps and Father Grigori's authored route assistance | Observation | Corroborated | High | P2, S4, S5 |
| `HL2-009` | Gordon's health, HEV state, active weapon/ammunition and Gravity Gun target/hold response provide attributable current-state feedback | Observation | Corroborated | High | P4, P6, S4 |
| `HL2-010` | Death or mission failure restores a retained save/checkpoint, while the positive packet terminal is the chapter transition into `Highway 17` | Observation | Corroborated | High | P2, S2–S5, V1 |
| `HL2-011` | The bounded decision structure joins ordinary FPS survival to physical object selection: the same prop may become cover, route support, trap input or damaging projectile | Observation | Corroborated | High | P1, P4, P5, S4, V1 |

## Basic data

- Release / origin: developed and published by Valve; released for Windows on
  2004-11-16 and retained as the current Steam product **Half-Life 2**.
- Platform or physical form: authored single-player first-person action game;
  only the current unmodified Windows base-campaign chapter declared above is
  admitted.
- Puzzle family: physics and object manipulation; tactical forecast and
  counterplay; real-time system pressure; spatial logic and topology.
- Primary and official sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/220/HalfLife_2/),
    for current title, Valve identity, single-player product, first-person
    combat, physics, Windows support and Ukrainian interface/subtitles.
  - **[P2]** [official Valve Steam announcements](https://store.steampowered.com/oldnews/?appgroupname=Half-Life+2&appids=220&feed=steam_community_announcements&headlines=0&l=english),
    for the 2024-11-15 Anniversary default, integrated Episodes, Lost Coast,
    Commentary and Workshop, `steam_legacy`, Ravenholm map fixes, localisation
    updates and the 2025-07-23 current public-update boundary.
  - **[P3]** [Valve Developer Community Half-Life 2 page](https://developer.valvesoftware.com/w/index.php?title=Half-Life_2),
    for the base chapter order, `d1_town_01` Ravenholm entry and `d2_coast_01`
    `Highway 17` successor. It is Valve-hosted community documentation and is
    corroborated independently below.
  - **[P4]** [Valve Source SDK 2013 `weapon_physcannon.cpp`](https://github.com/ValveSoftware/source-sdk-2013/blob/master/src/game/server/hl2/weapon_physcannon.cpp),
    for trace/range, mass and class eligibility, pull, attachment, collision-
    bounded held position, drop and launch rules.
  - **[P5]** [Valve Source SDK 2013 `props.cpp`](https://github.com/ValveSoftware/source-sdk-2013/blob/master/src/game/server/props.cpp),
    for physics-prop motion, breakage, Gravity Gun pickup/drop events,
    player-launched state, collision damage and NPC interaction attribution.
  - **[P6]** [Valve Source SDK 2013 `hl2_player.cpp`](https://github.com/ValveSoftware/source-sdk-2013/blob/master/src/game/server/hl2/hl2_player.cpp),
    for movement speeds, suit power, flashlight/sprint state, armour, active
    weapon input and HUD-facing player state.
- Secondary and reproducible sources:
  - **[S1]** [SteamDB Half-Life 2 depots](https://steamdb.info/app/220/depots/),
    observed 2026-09-01, for public Build ID `19307283`, built 2025-07-21 and
    updated 2025-07-23; Valve's announcement independently establishes the
    customer-facing update boundary.
  - **[S2]** [StrategyWiki Half-Life 2 overview](https://strategywiki.org/wiki/Half-Life_2),
    for the independent single-player and ordered chapter listing.
  - **[S3]** [SourceRuns map list](https://wiki.sourceruns.org/Half-Life-2-Maps.html),
    for the retail Ravenholm `d1_town_*` map packet and `Highway 17` successor;
    speedrun methods themselves are excluded.
  - **[S4]** [StrategyWiki Ravenholm walkthrough](https://strategywiki.org/wiki/Half-Life_2/%22We_Don%27t_Go_To_Ravenholm%22),
    for the chapter route, enemies, Gravity Gun props, explosive barrels,
    radiators, saw blades, traps and Grigori interactions.
  - **[S5]** [archived Half-Life 2 Prima Official Game Guide](https://valvearchive.com/Games/Half-Life%202/Documents/Half-Life%202%20Prima%20Official%20eGuide.pdf),
    Chapter 6, for an independent complete Ravenholm route through town,
    churchyard, mines and Shorepoint plus prop/trap tactics.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P6` and `S1`–`S5` under the declared entry, chapter and exclusions;
  rules reasoning, not direct play.
- Claim IDs: `HL2-001`–`HL2-011`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly walk, sprint, crouch, jump and climb Gordon
  through the authored first-person route.
- Existing `ACT-048`: acquire one eligible free rigid prop, retain it at a
  controlled offset and release, drop or throw it back into the live world;
  Gravity Gun reach, pull and launch force are parameters.
- Existing `ACT-161`: aim and commit a firearm, crowbar, grenade or launched
  prop attack against a reachable hostile.
- Existing `ACT-164`: switch the active weapon/tool; `ACT-183`: reload a
  magazine-fed weapon; `ACT-199`: collect compatible weapons, ammunition,
  health and HEV resources; `ACT-341`: activate a reachable authored route
  switch, crank, door or trap mechanism.
- New action genes: none. The Gravity Gun's command boundary is a specialised
  instance of existing rigid-object pickup/release; its distinct resolution and
  eligibility live in `SYS-705`, `SYS-706` and `CON-556`.
- Parameters: movement, stance, aim, weapon, magazine, reserve, prop, trace,
  hold offset, release mode, mechanism and interaction state.
- Claim IDs: `HL2-004`–`HL2-011`.

### System Behaviour Genes

- Existing `SYS-146`: advance a launched rigid prop under live gravity and
  collision; `SYS-215`: resolve directly commanded combat; `SYS-339`: route
  local zombies from eligible perception cues; `SYS-348`: apply damage through
  Gordon's protection/health into death; `SYS-369`: restore a retained authored
  save or checkpoint after failed attempt.
- New `SYS-705`: resolve Gravity Gun pull, attachment and collision-bounded
  view-relative holding before drop or launch.
- New `SYS-706`: convert a player-launched physics prop's collision into
  attributable breakable or hostile damage and return the surviving prop to
  ordinary physical state.
- Resolution order: current route and player state expose legal inputs; local
  hostiles perceive and move; ordinary weapon or Gravity Gun input is accepted;
  a selected prop pulls and attaches or rejects; held geometry updates against
  collision; drop/launch returns it to world physics; collision, explosion,
  combat and health resolve; authored interaction and arrival gates advance;
  death restores retained state or the final map transition settles the packet.
- Claim IDs: `HL2-004`–`HL2-011`.

### Constraint Genes

- Existing `CON-262`: carried weapon classes, magazines and reserve ammunition
  are finite; `CON-285`: weapon fire, switching and reload require compatible
  equipment/ammunition/action state; `CON-305`: zombie pursuit requires a
  perceived cue and reachable route.
- New `CON-556`: the ordinary Gravity Gun may pull or attach only an eligible
  VPhysics target within its trace, mass, flesh, spawn-flag and player-relative
  clearance rules; a rejected target remains world state.
- Scarce strategic resources: health, HEV protection, suit power, ammunition,
  loaded magazines, safe props, explosive barrels, line of sight, collision
  clearance, route position and retained checkpoint progress.
- Claim IDs: `HL2-004`–`HL2-011`.

### Information Genes

- Existing `INF-073`: active weapon, ammunition and available carried slots
  are visible; `INF-115`: local sight and spatial effects expose only nearby
  enemies and hazards; `INF-119`: health, HEV protection and suit power are
  visible.
- New `INF-271`: Gravity Gun beam/effect, target reaction, held pose and deny
  response disclose whether the current aimed prop is being pulled, attached,
  held, released or rejected without predicting its later collision result.
- Claim IDs: `HL2-004`–`HL2-011`.

### Objective Genes

- Existing `OBJ-026`: traverse the authored Ravenholm packet and reach the
  designated retained transition into `Highway 17`.
- Success, evaluation and failure: entering `d2_coast_01` is positive. Reaching
  Grigori, the graveyard or the mine is intermediate. Death followed by save or
  checkpoint restoration fails only that attempt and does not redefine the
  chapter terminal.
- Claim IDs: `HL2-003`, `HL2-008`, `HL2-010`, `HL2-011`.

### Time Genes

- Existing `TIM-003`: Gordon, hostiles, props, traps, fire, projectiles, suit
  power and authored triggers advance concurrently in real time.
- Claim IDs: `HL2-004`–`HL2-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Base campaign, Normal, Commentary off, Ravenholm selected | Start and accept first `d1_town_01` control | Gordon enters with the chapter's authored Gravity Gun, health/equipment and route state | reproducible bounded entry | `HL2-002`, `HL2-003`, `HL2-010` |
| An eligible loose prop lies beyond immediate attachment range but inside the Gravity Gun search trace | Aim and hold secondary fire | The prop receives a pull force until it can attach or leaves eligibility | remote pull is physical resolution, not teleportation | `HL2-005`, `HL2-006` |
| The eligible prop reaches attachment range and clearance | Continue the pickup input | The prop attaches to a view-relative controlled pose; incompatible flesh, mass or flags reject instead | typed manipulation boundary | `HL2-005`, `HL2-006` |
| A prop is held while Gordon faces nearby solid geometry | Walk and turn toward the obstruction | The held target pose is clamped by collision and may detach if its valid relation is lost | carrying does not bypass world geometry | `HL2-005`, `HL2-011` |
| A prop is held with a clear forward path | Drop it or commit primary launch | Drop returns ordinary velocity; launch applies force and marks it as player-launched | release mode changes future physical role | `HL2-005`, `HL2-007` |
| A launched saw blade, radiator or other damaging prop reaches a hostile | Give no additional input during impact | Collision transfers momentum and eligible damage with Gordon's launch attribution | world object becomes a combat projectile | `HL2-007`, `HL2-011` |
| An explosive barrel is physically displaced into a useful relation | Attack or launch it into a hostile group | Ballistic collision and eligible ignition/explosion change props, enemies and local route safety | manipulation and conventional combat compose | `HL2-007`, `HL2-008`, `HL2-011` |
| A zombie or headcrab receives a local sight/acoustic cue and has a route | Move, hide, attack or manipulate cover | The hostile pursues/attacks through reachable geometry while combat, props and health continue | enemy pressure remains local and concurrent | `HL2-004`, `HL2-008` |
| A magazine is depleted with compatible reserve ammunition | Reload | The active weapon becomes unavailable during its reload and receives a new legal magazine | finite conventional fire complements props | `HL2-004`, `HL2-009` |
| An authored switch, crank, trap or gate is reachable | Activate it | Its declared local mechanism changes state and the authored route or hazard relation updates | Ravenholm is not only an enemy-clearance corridor | `HL2-004`, `HL2-008` |
| Gordon reaches zero health | Accept the ordinary retry/load | Transient enemies, damage, props and position return to a retained save/checkpoint state | death is recoverable attempt failure | `HL2-009`, `HL2-010` |
| Gordon survives town, Grigori route, graveyard, mines and the final link | Cross the retained chapter boundary | `d2_coast_01` loads and `Highway 17` begins | reproducible positive terminal | `HL2-003`, `HL2-010` |

## Strategic and experiential structure

- Local decision: spend ammunition or reuse a nearby prop; pull an object into
  cover, use it against one target, stage an explosive barrel, activate a trap
  or preserve clearance for movement.
- Medium-term planning: read how a roof, alley, fire line, gate and enemy route
  change the value of the same movable object; keep enough health, ammunition
  and usable props for the next authored pressure point.
- Long-term structure: translate one retained Gravity Gun vocabulary across
  town, graveyard, mine and rail-side scenes until the route reaches the next
  chapter rather than treating each encounter as an isolated shooting gallery.
- Common heuristics: use blades and heavy props for efficient zombie removal;
  do not carry a blocking object into a narrow escape line; reserve conventional
  fire for targets or geometry that a prop cannot safely solve; inspect Grigori
  and mechanism cues before committing across one-way drops.
- Failure attribution: health/ammunition displays, local impact effects,
  Gravity Gun target/hold response, visible prop motion and checkpoint restore
  explain most failures; live collision and simultaneous hostile movement keep
  exact outcomes uncertain.
- Player-trust factors: the held object remains visibly physical, target denial
  occurs before commitment and the successful map transition gives a concrete
  terminal instead of an inferred story beat.
- Claim IDs: `HL2-004`–`HL2-011`.

## Replay and variation

- What changes between attempts: chosen props and traps, ammunition use,
  hostile positions, damage, pickup state, route timing, save/checkpoint and
  completion time.
- Randomness or procedural generation: the map packet and gates are authored;
  physics contacts, AI timing and some combat outcomes create run variation
  without changing the terminal.
- Multiple viable strategies: conventional firearm clearance, Gravity Gun
  conservation, aggressive explosive staging, trap use, avoidance and mixed
  prop/firearm play can cross the same chapter.
- Typical replay motive: improve prop recognition, ammunition efficiency,
  movement through vertical spaces and confidence in the Gravity Gun's mass,
  distance and collision envelope.
- Claim IDs: `HL2-003`–`HL2-011`.

## Adjacent systems and history

- Direct predecessors: historical retail or pre-Anniversary builds are not
  imported; public Build ID `19307283` is the declared current baseline.
- Variants: earlier/later base chapters change weapons, vehicles, allies and
  enemy sets; Episodes add different campaign state; Commentary and Workshop
  change the product surface but are excluded.
- Similar games: Portal shares direct first-person traversal, rigid-object
  carrying and physical collision but makes paired portals and chamber exits
  the central structure; Left 4 Dead 2 shares authored real-time zombie route
  survival but adds a four-Survivor party and Director; Cyberpunk 2077 shares
  first-person combat, pickups, health and checkpoints but its build/hacking
  systems replace Gravity Gun world-object composition.
- Important differences: Ravenholm's distinctive choice is not physics beside
  combat; it is reclassifying available physical props as cover, route tools,
  trap inputs and attacks under one ordinary Gravity Gun eligibility model.
- Claim IDs: `HL2-001`–`HL2-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-341` | traverse, manipulate, fight, reload, collect and activate |
| System Behaviour | `SYS-146`, `SYS-215`, `SYS-339`, `SYS-348`, `SYS-369`, `SYS-705`, `SYS-706` | physics, combat, zombie routing, health, restore and Gravity Gun resolution |
| Constraint | `CON-262`, `CON-285`, `CON-305`, `CON-556` | ammunition, equipment, pursuit and prop eligibility |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-271` | equipment, local threats, body state and Gravity Gun response |
| Objective | `OBJ-026` | reach the `Highway 17` chapter transition |
| Time | `TIM-003` | concurrent live route, combat and physics |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `211` (`GAME-0001`–`GAME-0211`).
- Exact genome matches: none.
- Tied near matches: `GAME-0193` — Destiny 2 (`12 / 36 = 0.333333`).
- Supported combination subsets: `COMB-0210`.
- Scan date: 2026-09-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0193` — Destiny 2 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-341`, `SYS-215`, `SYS-348`, `CON-262`, `INF-073`, `INF-115`, `INF-119`, `TIM-003` | Both join direct first-person traversal, weapon switching, finite fire, reload, authored interaction, local threats, layered body state and live pressure. Half-Life 2 replaces fixed Void abilities, radar/team scoring, mesh defence, Walker/Sepiks gates and activity grade/chest with eligible rigid-prop pull/hold/launch, attributed collision damage, local zombie routing, checkpoint restoration and a pure chapter-location terminal | Near, `0.333333` |

### Preserved research notes

- New genes: `SYS-705`, `SYS-706`, `CON-556` and `INF-271`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: generic navigation, rigid-object carrying, direct
  combat, finite equipment, zombie routing, health, checkpoint, HUD and live
  time records fit unchanged; four new records isolate the ordinary Gravity
  Gun's held-object resolution, impact attribution, eligibility and feedback.

## Combination status

- `COMB-0210` is a verified strict subset of the complete genome, joining
  first-person traversal, rigid-object manipulation, physical launch damage,
  local hostile pressure and the authored chapter terminal.
- Every earlier verified combination is checked after registration; none is an
  exact substitute for this chain.

## Taxonomy impact

- Registry changes: four new Active genes, evidence links on reused genes, one
  new combination and four existing family memberships.
- Taxonomy-change record: none; no prior lifecycle or reviewed game signature
  changes.
- Candidate terms affected: Gravity Gun pull/hold resolution, player-launched
  prop damage, ordinary physcannon eligibility and manipulation feedback.

## Negative results

- No new action gene is created for the Gravity Gun because `ACT-048` already
  covers acquiring, carrying and releasing a reachable rigid object; the
  distinctive trace, hold and impact rules belong to system/constraint genes.
- `SYS-147` is not reused because Ravenholm does not require a cascading
  support-collapse structure; ordinary prop breakage is only a parameter.
- `CON-147` is not reused because its Maquette boundary concerns recursive
  avatar-relative scale rather than the Gravity Gun's mass, flesh, flags and
  VPhysics eligibility.
- `SYS-621` is not reused because Ravenholm's authored encounters are not a
  Left 4 Dead Director panic request.
- `OBJ-115` is not reused because one Gordon chapter does not require collective
  living occupancy and safe-room closure.
- Episodes, Commentary, Workshop, achievements, collectibles and speedrun
  skips are excluded rather than silently made universal.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] The current base-campaign Ravenholm chapter
  is a reproducible physics-combat route from `d1_town_01` to the retained
  `Highway 17` transition (`HL2-001`–`HL2-011`).

## Нові гени

- [Observation | Corroborated | High] Added four genes for Gravity Gun pull and
  hold resolution, player-launched prop damage, manipulation eligibility and
  target/hold feedback.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0210` isolates the chain that turns
  one eligible world prop into a held tool, physical projectile and route
  resource inside an authored first-person chapter.

## Зміни таксономії

- [Observation | Direct | High] No lifecycle migration and no earlier reviewed
  signature change.

## Family classification

- `FAM-007` — Physics and object manipulation: mass, trace, attachment,
  collision, launch and damage make props causal.
- `FAM-009` — Tactical forecast and counterplay: each enemy, prop, trap,
  explosive and firing line changes the preferred next commitment.
- `FAM-010` — Real-time system pressure: movement, AI, projectiles, props,
  fire, traps and health advance together.
- `FAM-017` — Ordered dependency sequencing: authored rooftops, alleys, gates,
  Grigori's route, graveyard and mine transitions must be crossed in chapter
  order even when local encounters admit several physical solutions.
- No one-game family is created.

## Plain-language interpretation

In this packet, Half-Life 2 is one complete Ravenholm chapter, not the whole
campaign. Gordon already has the Gravity Gun. He can pull a suitable loose
object from a short distance, hold it in front of him, carry it while the world
still blocks it, then drop or launch it. The gun does not accept everything:
the object must be a compatible physical target within the tool's range, mass
and clearance rules.

That turns the environment into a changing set of choices. A radiator can be
cover now and a projectile a moment later; a saw blade can clear zombies
without spending firearm ammunition; a barrel can be staged for an explosion;
an authored switch can make the route itself dangerous or useful. Zombies and
headcrabs keep moving while Gordon aims, carries and reloads, so object choice
and ordinary shooting are one live decision loop. The chapter is complete only
after surviving the town, graveyard and mines and entering `Highway 17`.

## Нові питання

- Does a later first-person game reuse collision-bounded remote carrying while
  removing prop-to-hostile damage?
- Would a bounded `Highway 17` packet preserve the same combat resources but
  replace rigid-object manipulation with continuous vehicle control?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0213` — STAR WARS Jedi: Fallen Order.
- Optimisation criterion: continue Batch 009 in its recorded immutable order.
- Expected information gain: replace remote prop manipulation and conventional
  firearm pressure with authored melee/Force traversal, guarded combat and a
  bounded story-region terminal.
- Backlog impact: sixth of nine authorised game units.

## Чому саме вона

- [Confirmed | Direct | High] STAR WARS Jedi: Fallen Order is the next subject
  in `SEARCH_DEMAND_GAME_SELECTION_009`.

## Localisation status

- Ukrainian game, new-gene and combination entries are reviewed in this unit.
- The canonical product title remains `Half-Life 2`; Ukrainian prose keeps
  exact official chapter/map/tool labels where evidence requires them and uses
  natural descriptions for every player-facing mechanic.

## Open questions

- Re-check the current public build, Anniversary menu composition and any
  Ravenholm-specific map fixes on future review-on-touch.
