---
game_id: GAME-0282
slug: dead-cells
game_title: Dead Cells
analysis_status: reviewed
reviewed: 2026-09-10
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-130
    - ACT-140
    - ACT-161
    - ACT-199
    - ACT-341
    - ACT-356
    - ACT-425
    - ACT-437
    - ACT-451
  system:
    - SYS-004
    - SYS-167
    - SYS-215
    - SYS-222
    - SYS-450
    - SYS-456
    - SYS-464
    - SYS-467
    - SYS-469
    - SYS-578
    - SYS-755
    - SYS-832
    - SYS-833
    - SYS-834
    - SYS-835
    - SYS-852
  constraint:
    - CON-175
    - CON-404
    - CON-519
    - CON-596
    - CON-623
    - CON-624
  information:
    - INF-002
    - INF-117
    - INF-119
    - INF-142
    - INF-180
    - INF-306
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Dead Cells

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `588650`, base package `152266` (containing only that application),
  default public branch Build ID `23762174` (built and published 2026-06-16),
  which Motion Twin's own patch-notes page labels `Update 35.9` and its
  2026-06-15 Steam announcement describes as a stability patch on top of
  `Update 35: The End is Near`; checked 2026-09-08. The Steam build
  identifier is a secondary distribution observation (`DC-002a`); the
  `Update 35.9` label and its 2026-06-15 date are the publisher's own
  statement (`DC-002b`); that the two describe the same build rests on
  their adjacent dates alone (`DC-002c`). The `public_alpha`, `public_beta` and every archived `v0.0`
  to `v3.4` version branch are excluded.
- Product boundary: this is the 2018 Motion Twin game (developed by Evil
  Empire from 2019 to 2024 and by Motion Twin again since), not any of its
  five content DLC applications — the free Rise of the Giant (`1046440`),
  The Bad Seed (`1204130`), Fatal Falls (`1451460`), The Queen and the Sea
  (`1580050`) and Return to Castlevania (`2101430`) — nor the three
  soundtrack applications, the Workshop, mods, Custom Mode, Daily Challenge,
  Boss Rush, Assist Mode, the Training Room, Aspects, a console, macOS,
  Linux or mobile build. The required setup is the base package alone: no
  paid DLC application is installed beside it. This is a prescribed
  reproducible setup, not an observed entitlement or installation fact,
  because no direct play or entitlement inspection was conducted. Whether
  the free Rise of the Giant is installed does not change this packet: its only reach into
  the first biome is a locked door that needs the Hand of the King defeated
  and the Homunculus Rune, neither of which a fresh profile owns.
- Campaign settings: a fresh save slot with no Boss Stem Cell, because the
  first cell is awarded only for defeating a final boss; default gameplay
  and video options; no Assist Mode option enabled (all are off by
  default and are declared optional by the publisher); no Aspect selected
  from the Doctor; no Custom Mode, which needs a rune the profile lacks.
- Entry: first ordinary control of the Beheaded in the Prisoners' Quarters
  starting area, after the profile's opening, with the Rusty Sword equipped
  in the first weapon slot, the Beginner's Bow and the Old Wooden Shield
  lying in the starting-weapons room, no skills, no amulet, no Health Flask
  unlock, no gold, no cells and all three stats at 1.
- Primary decision loop: run, jump, double-jump, climb and roll through the
  generated Prisoners' Quarters while reading the explored map, the health
  bar with its orange recoverable portion, the gold and cell counters and
  each enemy's attack cue; strike Zombies, Undead Archers, Shieldbearers
  and Grenadiers with the equipped weapon combo or bow, or roll past them,
  hold or tap the shield if it was taken, and win back recently lost health
  by hitting back before the recoverable portion drains; collect the gold
  and cells that fly to the Beheaded from any enemy killed, pick up or
  leave sampled weapons against the two weapon slots, assign each Scroll of
  Power reached to one of the three stats, buy from the biome's one shop if
  it is reached, open the guaranteed treasure chest if the route passes it;
  reach the exit to the Promenade of the Condemned; in the Passage let any
  carried blueprint be delivered, commit the carried cells to the
  Collector's entry — or strike the door that bars the exit while cells
  remain until it breaks — choose a mutation, refill missing health at the
  fountain and enter the time door or the kill-streak door if that door's
  own condition holds; then arrive in the Promenade.
- Positive terminal: the first controllable state in the Promenade of the
  Condemned after the Passage, with the run's carried loadout, gold,
  remaining cells, stat points and chosen mutation, and the profile's newly
  completed unlocks, retained partial investments and delivered blueprints.
  That arrival is the retained successor on the common ground of the save
  sources: a 2018 guide says `Quit` saves and `Continue` resumes at the
  same location, a 2025 thread says `Continue` resumes at the beginning of
  the current level, and both agree that a quit run is resumed by
  `Continue`, that no manual save or load exists and that death removes
  the option; the two resume rules coincide exactly at this entry, and no
  stronger save rule is claimed. The reproducible verification path — quit
  to the main menu, choose `Continue`, confirm the Promenade start with the
  same loadout, gold, cells, stats and unlocks — is recorded here and was
  not executed in this analysis; no returned value is claimed as observed.
  No Promenade action after that arrival is admitted.
- Negative terminal: reaching zero health in the Prisoners' Quarters ends
  the run. The Beheaded restarts in the Prisoners' Quarters starting area
  of a new run; run-local gold (with the default Gold Reserves level, none
  is kept), cells in hand, undelivered blueprints, gear and stat points are
  lost, while completed unlocks, partial investments already paid to the
  Collector, delivered blueprints and the run counter remain. There is no in-level retry and no life stock.
- Included: direct locomotion with jump, double jump, ledge climb, crouch,
  platform drop and dive attack; the roll with its protected interval and
  cooldown; weapon combos and bow shots at reachable hostiles; the shield's
  held block and tapped parry as an ordinary option when the shield is
  taken; real-time hostile combat with enemy attack cues, breach stun and
  door-smash stun; one continuous health pool with recovery of recently lost
  health, one-hit protection and persistence between rooms and biomes;
  gold, cell and blueprint drops that fly to the Beheaded from killed
  enemies; weapon and chest drops sampled at the biome's gear level from
  the fresh profile's unlocked pool; the two weapon slots with forced
  replacement (skill and amulet slot counts as parameters); stat scrolls and
  their damage and health scaling; the biome shop and its prices; the
  authored-chunk biome generation and explored map; the exit door; the
  Passage's automatic blueprint delivery, the cell commitment at the
  Collector with its compulsory first entry and retained partial progress,
  the exit door barred while cells remain, the weapon strikes that break
  that door and remove it under the damage-threshold rule, the mutation
  offer with its per-biome slot, the fountain refill and the separate time
  and kill-streak reward doors; the run's documented quit-save and
  `Continue` resume and its death reset that keeps unlocks; one seeded
  generated biome.
- Excluded: everything after the first Promenade state; the Toxic Sewers,
  Dilapidated Arboretum and Castle's Outskirts exits (Vine Rune, DLC plus
  Teleportation Rune, and DLC respectively); the Health Flask's use, which a
  fresh profile can unlock only at this packet's Passage and therefore never
  drinks inside it; skills, whose presence in a fresh profile's unlocked
  offer pool is not evidenced beyond one inconsistently tagged wiki page and
  which are therefore excluded for insufficient evidence; amulets, affixes
  on level-1 gear, the backpack,
  recycling, random starter weapons and every other Collector upgrade
  beyond the first flask; mutation effects, which trigger only after the
  terminal; the elite room, cursed chest, gold doors, wall runes, secret
  blueprints, lore rooms and Specialist's Showroom, which are chance spawns
  or later unlocks and are not route steps; Boss Stem Cells, the Malaise,
  curses, the Legendary Forge, the Blacksmith's Apprentice (absent before a
  first boss kill), the Bank, bosses, later biomes, full-run completion,
  seeded farming, speedrun routing, meta-unlock history, Custom Mode, Daily
  Challenge, Boss Rush, Training Room, Aspects, Assist Mode, every DLC,
  Workshop mods, console and mobile editions, achievements as goals,
  screenshots, official artwork, video and audio.
- Reproducible parameterisation: install application `588650` from package
  `152266` on the default public branch; start a new save slot and reach
  first control. Walk the starting area, enter the starting-weapons room,
  take or leave the bow and shield, pass the large door, traverse the
  generated Prisoners' Quarters to the Promenade exit using any legal
  movement and attack, interact with the exit, cross the Passage and enter
  the Promenade. Killing enemies is the ordinary way through the biome but
  no kill is required by the route, so every drop, blueprint and cell is a
  run variable. Which weapon accompanies the sword, which enemies are
  fought or bypassed, which of the three stats each scroll is assigned to,
  whether the shop is used, whether the chest is reached and its item taken,
  whether the time door or the kill-streak door is open on arrival, which
  mutation is chosen, whether the carried cells complete Health Flask I,
  are committed in part or are carried out through the broken door, whether
  the fountain has any missing health to restore, how much damage is taken and whether
  the Beheaded dies are run parameters; no hit, death, timer target, farm,
  secret, seed or item is instructed. Live combat leaves the ordinary route
  in outcome branches: an undamaged arrival, a damaged arrival healed at the
  fountain, and the documented death reset. None is chosen deliberately.
- Potential scoped modules: the Promenade through the first Passage after
  it; the first boss route (Black Bridge or Insufferable Crypt) with the
  Legendary Forge; a Boss-Stem-Cell run; Custom Mode; Daily Challenge; Boss
  Rush; each DLC biome chain.
- Direct-play status: not conducted. Valve application, package and DLC
  data establish lawful availability and product separation; the SteamCMD
  projection establishes the current branch's build identifier and Motion
  Twin's patch-notes page separately establishes the `Update 35.9` label;
  Motion Twin's and Evil Empire's Steam announcements (enumerated through
  Valve's 400-item feed, keyword-scanned, with three announcements read in
  full), the store description, the official site and the press kit
  establish permadeath, the retained unlocks, the panic roll, the time
  doors' placement between levels, the first level's 30-kill no-hit
  challenge, the starter-weapon tubes, the Boss Stem Cell order, the Assist
  Mode defaults and the remark that quitting while dying once resumed from
  the beginning of the biome. The community-maintained
  official wiki is one source family; it alone supplies the exact numeric
  combat, roll, recovery, one-hit-protection, breach, drop, scroll, slot,
  shop, Passage and door values and the Prisoners' Quarters layout, and
  every claim resting on it alone is graded `Limited`. Dated community
  threads and one static guide supply the quit-and-`Continue` behaviour,
  whose resume location they state differently, and the Collector's door
  and partial-investment rules.
  This is an evidence-backed rules reconstruction, not a claimed captured
  playthrough or entitlement. No video or audio was opened, played, heard,
  analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DC-001` | The admitted product is the Windows Steam application `588650` Dead Cells, developed and published by Motion Twin, released 2018-08-06, in base package `152266` that contains only that application, separate from five content DLC applications and three soundtracks | Confirmed | Direct | High | P1, P2 |
| `DC-002a` | The default public branch is Build `23762174`, built and published 2026-06-16; the `public_alpha`, `public_beta` and archived version branches are separate | Observation | Limited | Medium | S1 (a secondary projection of Valve data; one family) |
| `DC-002b` | Motion Twin's patch-notes page lists `Update 35.9` dated 2026-06-15 as its latest entry, and the publisher's Steam announcement of that date describes a stability patch on top of `Update 35: The End is Near` | Observation | Direct | High | P4 (2026-06-15), P5 |
| `DC-002c` | Build `23762174` is the build that carries `Update 35.9`; this rests on the adjacent dates alone, with no publisher statement that ties the label to the build identifier | Observation | Limited | Medium | S1, P5 (dates only) |
| `DC-003` | The required setup installs the base package without any paid DLC application, so their content is absent by construction of the setup rather than by inspection, and the free Rise of the Giant reaches the first biome only through a door that needs the Hand of the King defeated and the Homunculus Rune | Observation | Corroborated | Medium | P2, S2 |
| `DC-004` | The publisher describes the game as having no checkpoints, permadeath, a panic roll and progress kept between runs as unlocked paths, levels, mutations, abilities and weapons | Observation | Corroborated | High | P4, P6, P7, P8 |
| `DC-005` | A fresh profile owns no Boss Stem Cell, because the first cell is awarded for defeating a final boss with none active, so the packet runs at `0 BSC` | Observation | Corroborated | High | P4 (2022-06-23), S2 |
| `DC-006a` | Every run starts with fixed starter weapons unless the random starter-weapon upgrades are bought | Observation | Corroborated | Medium | P4 (2020-12-21), S2 |
| `DC-006b` | The Rusty Sword is equipped at start and the Beginner's Bow and Old Wooden Shield lie in the starting-weapons room; the Beheaded has two weapon slots, two skill slots and an amulet slot, starts with no skill, and the bow and shield carry a weapon-slot restriction | Observation | Limited | Medium | S2 |
| `DC-007a` | The Prisoners' Quarters is the first biome of every run, assembled from authored level chunks into a generated layout | Observation | Corroborated | Medium | S2, P4 (2017-06-22 chunk additions) |
| `DC-007b` | At `0 BSC` it holds two Scrolls of Power, one weapon or skill shop not behind a rune, one guaranteed treasure chest, spike and rotating-ball traps, gear level I, enemy tier 1–3, and exits to the Promenade (no requirement), Toxic Sewers (Vine Rune), Dilapidated Arboretum (DLC and Teleportation Rune) and Castle's Outskirts (DLC) | Observation | Limited | Medium | S2 |
| `DC-008` | At `0 BSC` the biome's enemies are Zombies (scratch, leap), Undead Archers (arrow), Shieldbearers (frontal immunity, charge) and Grenadiers (long detection through walls, delayed bomb); each attack can be blocked, parried or rolled | Observation | Limited | Medium | S2 |
| `DC-009` | Default inputs are move, jump, roll, primary weapon, secondary weapon, two skills, heal, interact, pause and map, with crouch, platform drop, dive attack, double jump and ledge climb as movement forms | Observation | Limited | Medium | S2 (Controls, Mechanics) |
| `DC-010a` | The roll is the publisher's advertised emergency panic roll | Observation | Corroborated | High | P7, P8, S2 |
| `DC-010b` | A roll lasts 0.4 s with a 0.37 s cooldown, dodges most attacks, passes one-tile gaps and smashes wooden doors, which stuns nearby enemies | Observation | Limited | Medium | S2 (Mechanics, Objects) |
| `DC-011` | Weapons resolve as combos with per-hit damage and breach values; the Beginner's Bow has six arrows that return when enemies die; holding the shield absorbs 75% of frontal damage and tapping it parries, stunning a melee attacker for 0.8 s and reflecting projectiles | Observation | Limited | Medium | S2 |
| `DC-012a` | The Beheaded has one health pool; hostile hits and traps reduce it and reaching zero ends the run | Observation | Corroborated | High | P7, S2, S4 |
| `DC-012b` | After a hit, 80% of the lost health becomes an orange recoverable portion that drains at 30% of maximum health per second and is discarded by the next hit; while it remains, each hit dealt restores 12% of the damage inflicted, capped per hit at 20% of the original loss | Observation | Limited | Medium | S2 (Mechanics) |
| `DC-012c` | A hit that would kill from above 25% health instead leaves 1 HP and stuns nearby enemies, then the protection recharges for 45 s or is reset by a full heal | Observation | Limited | Medium | S2 (Mechanics) |
| `DC-013` | Direct damage dealt during an enemy manoeuvre accumulates breach damage that stuns the enemy for 1.4 s past a tier-scaled threshold; falls stun the Beheaded without damage in this biome | Observation | Limited | Medium | S2 (Mechanics) |
| `DC-014` | Enemy attacks show a visible wind-up and attack prompt before they land | Observation | Limited | Medium | S2 (enemy pages; Elite notes) |
| `DC-015a` | Killed enemies drop gold and cells that fly to the Beheaded within range, and can drop blueprints and items | Observation | Corroborated | Medium | S2, P7 |
| `DC-015b` | Enemy blueprints drop by assigned rarity at generation, at most one item and one outfit blueprint per biome; the Zombie's Blood Sword blueprint is a 100% drop; gear drops, shop stock and the treasure chest sample the unlocked pool at the biome's gear level, the chest one level higher; level-1 non-starter gear has no affixes | Observation | Limited | Medium | S2 (Blueprints, Gear, Objects, Zombie) |
| `DC-016a` | Scrolls raise the run's stats and the early biomes were given more scrolls in Update 19 | Observation | Corroborated | Medium | S2, P4 (2020-07-01) |
| `DC-016b` | A Scroll of Power adds one point to one of Brutality, Tactics or Survival; each point multiplies matching items' damage by 1.15 and raises maximum health | Observation | Limited | Medium | S2 (Stats, Pickups) |
| `DC-017a` | A biome shop is a weapon shop or a skill shop, sells its class for gold at prices that rise with item level, in stat categories, with a free reroll that raises prices | Observation | Corroborated | Medium | S2 (Shops), P4 (2020-07-01) |
| `DC-017b` | Whether a fresh profile's unlocked pool contains any skill, so that a skill shop or a skill drop can offer one before the terminal, is not evidenced: the wiki tags only Wolf Trap `AutoUnlocked` (one page, inconsistent with its blueprint fields) and no publisher statement lists the initial pool, so skills are excluded from the packet | Observation | Limited | Low | S2 (Wolf Trap, Ice Grenade, Gear); negative search |
| `DC-018` | Gold, cells and undelivered blueprints are run-local: on death gold is kept only up to the Gold Reserves level (default none), cells in hand are lost and undelivered blueprints are lost, while unlocks persist | Observation | Corroborated | Medium | S2, S4, P7 |
| `DC-019a` | Leaving a biome enters a Passage that holds the Collector, Guillain, a Health Fountain, and time and kill-streak reward doors; time doors sit between levels | Observation | Corroborated | Medium | S2 (Passage, doors), P4 (2018-12-14) |
| `DC-019b` | The Passage after the Prisoners' Quarters has a time door holding the Assault Shield blueprint that opens when the run arrived at or below 2:00 (a timer equal to 2:00 still opens it) and a separate streak door that opens when at least 30 consecutive damage-free kills were reached (the streak stays earned once reached); each door tests only its own measure, and either door holds gems, 20 cells and a three-choice altar; time in the transition does not count; the fountain restores health and flask charges at `0 BSC`; the Blacksmith's Apprentice appears only after a first boss kill | Observation | Limited | Medium | S2 (Time, killstreak and no-hit doors; Passage) |
| `DC-019c` | The first level's no-hit challenge requires 30 kills where later levels require 60, rewards cells, gold and a weapon, and time doors sit between levels | Observation | Corroborated | Medium | P4 (2018-12-14), S2 |
| `DC-020a` | A blueprint carried into a transition is delivered to the Collector automatically with no interaction, and a blueprint still carried at death is lost | Observation | Limited | Medium | S2 (Blueprints, `2.3` history; Passage) |
| `DC-020b` | A completed Collector unlock persists across runs and adds the item to later runs' pools | Observation | Corroborated | High | S2, P7, S3 (2018-07-04) |
| `DC-020c` | Health Flask I is the compulsory first entry at 5 cells and must be unlocked before any other upgrade; later flask levels require the previous level and item-count thresholds, shown as padlocked requirements | Observation | Corroborated | Medium | S2 (Runes and upgrades, Health Flask), S3 (2018-07-04) |
| `DC-020d` | Cells may be paid in part toward an entry, the paid amount is retained on the profile as progress toward that entry after death, and the entry completes only once the total cost has been paid | Observation | Limited | Medium | S3 (2018-10-05: "invest all you have at the moment which will be saved as progress in that upgrade (for example 20/65)"), S2 (Blueprints: "once the total cell cost has been paid") |
| `DC-020e` | The door out of the Collector's room stays locked while cells are carried | Observation | Corroborated | Medium | S2 (Currency), S3 (2017-07-23) |
| `DC-020f` | A biome's base cell yield is about a quarter of its enemy count, with more in vats, so whether a first run arrives with the 5 cells for Health Flask I is a run variable, not a route fact | Observation | Limited | Medium | S2 (Currency) |
| `DC-020g` | That door can be broken by the player, after which the carried cells may be taken onward unspent | Observation | Corroborated | Medium | S2 (Currency: "can actually be broken"), S3 (2021-01-25) |
| `DC-020h` | Breaking the door carries no penalty | Observation | Limited | Medium | S3 (2021-01-25 only: "Nothing") |
| `DC-021` | Guillain offers one mutation per cleared biome up to three, with a paid reset; most mutations need blueprints, and a small initial set is available without one | Observation | Limited | Low | S2 (Mutations, Guillain); the exact initial set rests on incomplete wiki data |
| `DC-022` | The Promenade of the Condemned is the stage-2 biome entered from the Prisoners' Quarters, at gear level II | Observation | Limited | Medium | S2 |
| `DC-023a` | Quitting through the pause menu saves the current run; forced quits and crashes caused rollbacks | Observation | Limited | Medium | S3 (2018-08-09) |
| `DC-023b` | The game saves on `Quit`; `Continue` resumes in the same location where the game was left; resuming deletes the save | Observation | Limited | Medium | S4 (2018-08-17) |
| `DC-023c` | Quitting inside a level resumes at the beginning of that level, quitting between levels resumes between levels, and passing a door creates a save point | Observation | Limited | Medium | S3 (2025-09-19, 2025-09-24) |
| `DC-023d` | The publisher wrote in 2022 that resurrecting from the beginning of the biome "effectively already existed by quitting the game when you die"; this concerns a quit during death and is not used as proof of the ordinary quit-save location | Observation | Direct | Medium | P4 (2022-06-23, 2022-04-12) |
| `DC-023e` | The sources conflict on the resume location (`DC-023b` same location; `DC-023c` level start); their common supported statement is that a quit run is resumed by `Continue`, that no manual save or load exists, and that a quit at the first Promenade state resumes at that state under either rule | Observation | Conflicting | Medium | S3, S4 |
| `DC-023f` | Death removes the `Continue` option and the next run starts from the Prisoners' Quarters | Observation | Corroborated | Medium | S4, S2, P7 |
| `DC-024` | The run counter is retained: the Quick Bow secret appears from the third run and the Tutorial Knight's corpse with the Training Room key from the fourth | Observation | Limited | Medium | S2; outside this packet |
| `DC-025` | The map shows the explored part of the biome with shops, treasure rooms, teleporters and the Beheaded's position | Observation | Limited | Medium | S2 (Biomes) |
| `DC-026` | The HUD shows the health bar with its orange portion, gold, cells, equipped gear and the stat values | Observation | Corroborated | Medium | S2, P4 (2022-06-23 interface and stat-colour options) |
| `DC-027` | The elite room (5%), cursed chest (1%), gold doors, wall runes, lore rooms, secret blueprints, Specialist's Showroom, Hunter's Mirror, Daily Challenge, Custom Mode, Training Room and Aspects are chance spawns, later unlocks or optional modes, not steps of the ordinary first run | Observation | Limited | Medium | S2 |
| `DC-028` | The bounded identity is one generated side-scrolling biome fought in real time with a roll, weapon combos and an optional shield, a single health pool that gives back recently lost health for aggression and shields one lethal hit, sampled gear against bounded weapon slots, stat scrolls, a transition that banks delivered blueprints automatically, keeps committed cells as profile progress and bars its exit while cells remain unless the door is broken, while everything else stays run-local, and a quit-save resumed by `Continue` whose exact location the sources state differently | Observation | Limited | Medium | `DC-004`–`DC-027`; inherits the weakest material clause |

## Basic data

- Release / origin: Motion Twin; Early Access 2017-05-10, full release
  2018-08-06 (Steam) for Windows, macOS and Linux; Evil Empire developed
  updates 2019–2024; Update 35 `The End is Near` 2024-08-19 was the final
  content update; `Update 35.9` stability patch 2026-06-15.
- Platform or physical form: lawfully available English Windows Steam
  client, base package `152266`; one offline single-player run opening.
- Puzzle family: tactical forecast and counterplay; real-time system
  pressure; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-08:
  - `P1` — [Valve application data](https://store.steampowered.com/api/appdetails?appids=588650&cc=ua&l=english),
    for title, Motion Twin as developer and publisher, Windows, macOS and
    Linux support, single-player, Steam Cloud and Workshop categories, the
    2018-08-06 release, package `152266`, the eight DLC applications, the
    support address at Evil Empire and the store description.
  - `P2` — [Valve package and DLC data](https://store.steampowered.com/api/packagedetails?packageids=152266&cc=ua&l=english)
    for package `152266` containing only application `588650`, and the
    application data for `1046440` (free, 2019-03-28), `1204130`,
    `1451460`, `1580050` and `2101430`.
  - `P4` — [Motion Twin's and Evil Empire's Steam announcements](https://store.steampowered.com/news/app/588650),
    enumerated through Valve's news feed (400 items, 2017–2026) and
    keyword-scanned for rule terms (save, quit, continue, checkpoint,
    Collector, invest, door, timed door, kill streak, blueprint,
    automatically, starting weapon, Boss Cell, Assist Mode). Three
    announcements were read in full: the 2026-06-15 stability patch, the
    2022-06-23 `Breaking Barriers` notes and the 2018-12-14 `1.1` beta
    notes; every other statement below is quoted from its matched passage
    read in its surrounding paragraph, not from a full read. The items:
    the 2026-06-15 stability patch (crash fixes, SDL upgrade), the 2026-06-07
    Castlevania: Belmont's Curse notice, the 2024-08-19 `Update 35: The End
    is Near` notes, the 2022-06-23 `Breaking Barriers` notes (Assist Mode
    optional and off by default; "each time you die you can resurrect from
    the beginning of the biome (this effectively already existed by quitting
    the game when you die, now it's just 'official')"; "beat the final
    boss. Then you add a Boss Cell"; interface, outline and stat-colour
    options), the 2022-04-12 alpha notes with the same continue statement,
    the 2020-12-21 Update 21 notes (backpack as a Collector meta upgrade
    "like Recycling or the random starting weapon tubes"; two weapon
    slots), the 2020-07-01 Update of Plenty notes (more scrolls in early
    biomes; shop categories by stat; gear price by item level; free reroll
    raising prices; `0BC` tuned for new players), the 2018-12-14 `1.1`
    beta notes ("Time doors moved to in-between levels"; a new challenge
    "rewards killing 60 enemies (only 30 in the first level) without being
    hit"), the 2018-08-04
    Twitch-integration note naming timed doors, the 2018-08-06 release
    notice, and the 2017-06-22 `Update 2` notes ("Extra level chunks for
    the Promenade of the Condemned").
  - `P5` — [Motion Twin's patch-notes page](https://dead-cells.com/patchnotes),
    listing `Update 35.9` (2026-06-15) as the latest entry after `35.8`
    (2024-08-26) and `35.0`–`35.7` (2023); no save, difficulty or
    starting-equipment statement.
  - `P6` — [Motion Twin press kit](https://motiontwin.com/presskit/81),
    for the factsheet (Motion Twin, Bordeaux; PC, Switch, PlayStation 4,
    Xbox One) and the description ("No checkpoints. Kill, die, learn,
    repeat"; "permanent weapon upgrades"; "special permanent abilities").
  - `P7` — [Steam store page](https://store.steampowered.com/app/588650/Dead_Cells/),
    for the absence of a `View manual` link, the DLC list, and the
    description ("No checkpoints"; "the corpses you possess are not
    immortal… you will be sent back to the dungeon"; "you keep some of
    your progress for successive runs: new paths you've unlocked, access to
    new levels, mutations, abilities and weapons"; "the emergency panic
    roll").
  - `P8` — [Official site](https://dead-cells.com/), for "No checkpoints.
    Kill, die, learn, repeat", "Unlock new levels with every death", the
    patch-notes and wiki links; no manual, FAQ or support page exists.
- Corroborating textual sources, accessed 2026-09-08:
  - `S1` — [public SteamCMD info projection](https://api.steamcmd.net/v1/info/588650),
    for the `public` (`23762174`, 2026-06-16), `public_alpha`,
    `public_beta` and archived `v0.0`–`v3.4` branches; a secondary
    distribution mirror.
  - `S2` — [official Dead Cells wiki](https://deadcells.wiki.gg/), read as
    MediaWiki wikitext and Cargo data: Prisoners' Quarters, Promenade of the
    Condemned, Biomes, Passage, Boss Stem Cells, Pickups, Currency,
    Blueprints, The Collector, Runes and upgrades, Health Flask, Gear, Shields, Mutations,
    Guillain, The Blacksmith's Apprentice, Shops, Objects, Time, killstreak
    and no-hit doors, Mechanics, Stats, Status effects, Controls, Enemies,
    Zombie, Undead Archer, Shieldbearer, Grenadier, Rusty Sword, Beginner's
    Bow, Old Wooden Shield, Tutorial Knight, Training Room, Custom Mode,
    Curse, The Beheaded, Dead Cells. Community text with rules-file
    references; never sole support for a product or build claim; the site
    is linked from the official site but is not publisher evidence.
  - `S3` — dated Steam community threads:
    [Does it save the current run when you quit the game?](https://steamcommunity.com/app/588650/discussions/0/1744469078236984811/)
    (2018-08-09: yes; forced quits caused rollbacks) and
    [saving during a run](https://steamcommunity.com/app/588650/discussions/0/595160389826644466/)
    (2025-09: quitting in a level resumes at the beginning of the level;
    quitting between levels resumes between levels; going through a door
    creates a save point);
    [How... do you return to the Collector to hand in stuff?](https://steamcommunity.com/app/588650/discussions/5/1727575977575395633/)
    (2018-07-04: blueprints and invested cells are stored forever; padlocked
    entries list their requirements);
    [How do you progress, when you loose ALL your cells every time you die?](https://steamcommunity.com/app/588650/discussions/0/1729837292635340425/)
    (2018-10-05: cells can be invested in part and saved as progress, "for
    example 20/65");
    [Door Break at collector](https://steamcommunity.com/app/588650/discussions/0/3112518479600547337/)
    (2021-01-25: breaking the door before spending all cells has no
    penalty); and
    [Banking cells and refunding upgrades](https://steamcommunity.com/app/588650/discussions/3/1458455461491391050/)
    (2017-07-23: a suggestion thread describing the door as locked until
    the cells are spent). No developer reply appears in any of them, and
    all threads count as one family.
  - `S4` — [gamepressure guide "Can you save your progress?"](https://www.gamepressure.com/dead-cells/can-you-save-your-progress/zdb353)
    (2018-08-17): the game saves on quit; `Continue` resumes where the game
    was left; resuming deletes the save; death removes `Continue`; every
    death restarts in the Prisoners' Quarters while permanent upgrades,
    blueprints and a little gold are kept.
- Negative searches, 2026-09-08: no official manual exists on the site,
  the store page (no `View manual`), the press kit or the Steam support
  entry; the official patch-notes page holds fix lists only; the wiki has
  no Save, HUD or Timer page, so saving rests on the threads and the guide,
  which disagree on the resume location, with the publisher's 2022 remark
  recorded separately; no official statement of the Collector's door or of
  partial investment exists, so both rest on the wiki and the threads; and
  the run-timer display is not evidenced as a default HUD element.
- Evidence independence: sources are counted by family. Valve data (`P1`,
  `P2`, `S1`) is one family; Motion Twin and Evil Empire statements (`P4`,
  `P5`, `P6`, `P7` text, `P8`) are one family; the wiki (`S2`) is one
  family; the threads (`S3`, one family however many threads agree) and
  the guide (`S4`) are separate families of lower reliability.
  `Corroborated` requires two families; `S2` alone is `Limited`; a single
  publisher statement is `Direct` for what it states and does not prove a
  neighbouring clause.
- Reproducible control: `V1` repository-side transition trace across
  `P1`–`P8` and `S1`–`S4` under the declared application, package, branch,
  fresh profile, `0 BSC`, entry, exclusions and Promenade-arrival terminal;
  rules reasoning, not direct play.
- Claim IDs: `DC-001`–`DC-028`; lettered sub-rows split composite claims
  so that each clause carries its own grade, and an unlettered reference
  means every sub-row of that claim. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: run, jump, double-jump, climb ledges, crouch, drop
  through platforms and dive-attack through the generated corridors;
  `ACT-130`: buy one offered weapon for gold at the biome shop, which enters
  a weapon slot at once; `ACT-140`: assign each
  Scroll of Power to Brutality, Tactics or Survival, and choose one mutation
  from Guillain's offer; `ACT-161`: aim the weapon combo, the bow or the
  dive attack at a reachable hostile, or aim weapon strikes at the barred
  Collector's room door (target class widened by `TAXONOMY_CHANGE_043`,
  which the Half-Life carrier already exercised on route glass); `ACT-199`:
  pick a reachable weapon into a compatible weapon slot, replacing the
  current item; `ACT-341`:
  interact with scroll vats, the treasure chest, wooden doors, the exit,
  the Collector, Guillain and the fountain; `ACT-356`: commit the roll in
  place or in one direction and accept its cooldown; `ACT-425`: tap the
  shield to parry one incoming attack; `ACT-437`: hold the shield toward
  the facing to absorb frontal damage.
- New `ACT-451`: select the Collector's available entry and commit the
  carried cells toward its price, up to the balance or the remaining price,
  whether or not the commitment completes it; the retained result is
  `SYS-835`. The command was scanned against `ACT-130` (acquires the offer
  at once; a partial commitment acquires nothing), `ACT-093` (typed item,
  abstract currency excluded), `ACT-143` (between runs, persistent
  resource), `ACT-136`, `ACT-118`, `ACT-248` (full-price purchases
  or sacrifices), `ACT-134`, `ACT-175` and `ACT-207` (point or currency
  purchases of one eligible entry that must be affordable and takes effect
  at once), `ACT-273` (a donation into pooled shared funds with no selected
  priced entry, whose own exclusion names buying the ledger upgrade from
  those funds), `ACT-128` and `ACT-140` (no payment) and `ACT-191`,
  `ACT-231` and `ACT-401` (point allocation, no priced ledger entry);
  generalising `ACT-130` was rejected because its eight carriers all
  acquire the offer by the same command and a pay-toward command has a
  different resolution.
- Rejected `ACT-190`: no skill or amulet is available on a fresh profile
  before the Passage, and skill availability inside the packet is not
  evidenced (`DC-017b`), so no skill is bought, found or used before the
  terminal. Rejected `ACT-223`: the roll and the parry are freely timed
  commands, not responses prompted per telegraphed attack. Rejected
  `ACT-436`: the roll costs no stamina or reserve. Rejected `ACT-143`:
  cells are a run-local currency spent inside the run, not a persistent
  resource between runs; the persistence of the payment is `SYS-835`.
  Rejected `ACT-093`: cells are an abstract currency, which that gene
  excludes, not a typed inventory item. Rejected `ACT-091`: blueprint
  delivery is automatic on arrival, with no selected recipient command.
  Rejected `ACT-040`: pickup is by reach with a slot choice, not a
  loot-window assignment. Rejected `ACT-131` and item use: no consumable is
  available before the terminal.
- Parameters: slot restrictions of the bow and shield, combo timings, arrow
  count and return, block percentage, parry window, roll duration and
  cooldown, dive-attack damage tiers, door smash stun, the door's target
  class for `ACT-161`, the Collector's minimum commitment increment.
  Claims: `DC-006`,
  `DC-009`–`DC-011`, `DC-015`–`DC-017`, `DC-019`–`DC-021`.

### System Behaviour Genes

- Existing `SYS-004`: blueprint rarity rolls, drop rolls and generation
  randomness; `SYS-167`: gold, cells, stats, health and loadout carried from
  the Prisoners' Quarters through the Passage into the Promenade; `SYS-215`:
  real-time combat with Zombies, Undead Archers, Shieldbearers and
  Grenadiers, including their detection, frontal immunity, breach stun and
  door-smash stun; `SYS-222`: gold and cells flying to the Beheaded within
  range; `SYS-450`: enemy, chest and shop items sampled from the unlocked
  pool at gear level I, the chest at level II, with quality and affix rules;
  `SYS-456`: the roll's protected opening interval against attack overlap;
  `SYS-464`: the biome assembled at entry from authored chunks with its
  shop, chest, scroll, trap and exit placements; `SYS-467`: stat points and
  the chosen mutation composing into damage scaling, maximum health and the
  run build; `SYS-469`: death clearing the run's layout, loadout, gold,
  cells and undelivered blueprints while unlocks and paid investments
  remain; `SYS-578`: the
  single health pool reduced by hits and traps, restored by the fountain
  when any is missing, and ended at zero; `SYS-755`: weapon hits reducing
  the barred Collector's room door until it breaks and its solid body is
  removed, the same resolution the Half-Life carrier applies to route
  glass, with the door's material and hit count as unrecorded parameters.
- Generalised `SYS-832`: after eligible health loss, a declared share stays
  recoverable and each eligible hit landed on an enemy restores health from
  that bank. New `SYS-852`: after its delay the bank drains continuously, and
  a later damaging hit discards the old bank before creating a new recoverable
  portion. The two owners are separated by `TAXONOMY_CHANGE_065`: TEKKEN 8
  transfers into the first trace but not the timed-drain or replacement trace.
  New `SYS-833`: a hit that would kill from above a health fraction
  leaves one health point and stuns nearby enemies, then the protection
  recharges on a cooldown. New `SYS-834`: entering the transition delivers
  carried blueprints into the profile's purchasable ledger automatically,
  while an undelivered blueprint dies with the run. New `SYS-835`: cells
  paid toward an available Collector entry are retained on the profile as
  progress even in part, a completed total makes the entry permanent
  content of later runs, and cells never invested stay run-local. The two
  were split first: delivery is triggered by arrival with no agency and
  needs no cells; investment is a player choice that needs no delivered
  blueprint (Health Flask I has none); either occurs without the other, so
  they are not one gene.
- Branch scope, stated for every conditional rule: damage, recovery,
  one-hit protection and death are outcome branches of the enemies' own
  attacks and the traps; no representation of the route commands them. Health
  Flask I is completed at the Passage only when at least 5 cells were
  collected; otherwise the carried cells are invested toward it in part or
  carried out through the broken door; the flask is never drunk inside the
  packet; the fountain restores only what is missing, so its material
  effect is conditional on a damaged arrival and it is a healing-source
  parameter of `SYS-578`; the door break is exercised only when cells are
  still carried at the room's exit; traps are a damage-source
  parameter of `SYS-578` and a placement parameter of `SYS-464`; the
  kill-combo speed boost, wall runes and the trap-chest chance are
  parameters.
- Rejected `SYS-782`: cells in hand are not preserved at death, so the
  Hades hub retention fails. Rejected `SYS-362`: no bounded encounter
  settles a reward; drops are per-kill and per-container samples. Rejected
  `SYS-468`: no guardian gates the exit. Rejected `SYS-166`: the chosen
  mutation triggers only after the terminal. Rejected `SYS-399`, `SYS-610`
  and `SYS-369`: death is a run reset, not a checkpoint return.
  Rejected `SYS-820`: one-hit protection is free and cooldown-gated, not
  paid from a stock. Rejected `SYS-364`: the fountain is not a rest that
  respawns enemies. Rejected `SYS-426`, `SYS-335`: unlocks come from
  delivered blueprints and invested cells, not milestones or research.
  Rejected `SYS-116`: a cell payment has no typed slot identity, which
  that gene excludes as a plain counter. Rejected `SYS-159`: nothing is
  consumed over time by a facility. Rejected `SYS-210`: its own exclusion
  names purchasing an optional upgrade with accumulated points, which a
  cell-priced entry is. Rejected `SYS-171`: no shaped delivery quota.
  Rejected `SYS-168`: the biome is a spatial layout, not a node map.
  Rejected `SYS-057`: enemy detection is a combat-target parameter, not a
  patrol replacement.
- Resolution order: generate the biome at entry; each frame — movement,
  roll protection, attack hit and breach, enemy cues and attacks, damage,
  recoverable-health banking, attack-based recovery, delayed drain or
  replacement by later damage, one-hit protection, drops flying in; scroll or mutation
  composition on choice; exit interaction closes the biome; Passage —
  blueprint delivery on arrival if one is carried, the cell commitment at
  the Collector, the barred exit or the strikes that break it, mutation
  offer, fountain refill of missing health, each reward door against its
  own predicate; Promenade entry.
  Claims: `DC-007`–`DC-023`.

### Constraint Genes

- Existing `CON-175`: health lost in one room stays lost in the next until
  the fountain, and zero ends the run; `CON-404`: two weapon slots hold the
  sword and the optional starter bow or shield, and a sampled third weapon
  can be taken only by replacing one, with the skill and amulet slot counts
  as parameters the packet does not exercise (generalised by
  `TAXONOMY_CHANGE_042` so that counts and classes are parameters);
  `CON-519`: the second jump is available only until
  it is spent and returns on landing; `CON-596`: a mutation may be taken
  only into the one slot the cleared biome grants and cannot duplicate an
  owned mutation.
- New `CON-623`: each transition reward door opens only if its own
  declared measure satisfies that door's declared comparison predicate
  during the biome — the time door if the run arrived at or below 2:00
  (equality opens it), the separate streak door if at least 30 damage-free
  kills were reached — and otherwise stays locked for the run; comparator
  direction and equality are parameters, and the two doors are instances of
  one predicate form, not one door with a joined predicate. New `CON-624`:
  the Collector's room exit stays barred while cells are carried, so
  leaving ordinarily means committing every cell, and the only other legal
  exit is the removal of the door, whose damage and destruction resolve
  under `SYS-755` and whose absence of a penalty rests on one thread
  (`DC-020h`).
- Rejected `CON-284`: no bulk capacity exists beside the slots. Rejected
  `CON-485`: slots bound pickups, not level-up offers. Rejected `CON-353`:
  no mounted secondary. Rejected `CON-210`: no typed stacks or grid.
  Rejected `CON-191`: its affordability clause fails, because the Collector
  accepts a partial payment toward an entry that is not yet affordable; the
  compulsory first entry and the later prerequisites are the entry-ladder
  parameter of `SYS-835`. Rejected
  `CON-188`: whether a scroll or mutation offer may be deferred is not
  evidenced. Rejected `CON-269`: no ability with target, resource and
  readiness gates is used. Rejected `CON-402`: no room locks its exits
  behind clearance. Rejected `CON-440`: the doors test one area's
  performance, not an accumulated progression threshold. Rejected `CON-068`, `CON-187`: the timer never ends the
  attempt. Rejected `CON-183`: no life stock.
- Scarce strategic resources: health and its recoverable portion, the
  one-hit protection cooldown, gold, cells, the two weapon slots, the three
  stat points from scrolls, the run timer and the kill
  streak. Claims: `DC-006`, `DC-009`, `DC-012`, `DC-015`, `DC-019`–`DC-021`.

### Information Genes

- Existing `INF-002`: the next room's contents, drops and blueprint
  assignments are not previewed; `INF-117`: the shop shows each item's
  price against the gold balance before purchase; `INF-119`: the HUD shows
  health with its orange portion, gold, cells, equipped gear and stats;
  `INF-142`: enemy wind-ups and attack prompts cue roll, parry and strike
  timing; `INF-180`: the map shows the explored biome with shop, treasure
  and teleporter marks; `INF-306`: the scroll and mutation offers state
  each option's effect before the choice.
- Excluded for insufficient evidence: a run-timer HUD element on a default
  profile, and any biome-name or reward preview on the exit door.
  Rejected `INF-179`: the scrolling side view does not expose one bounded
  room. Rejected `INF-305`: the exit previews no reward class. Rejected
  `INF-317`: no fixed placed instruction is evidenced. Rejected `INF-327`,
  `INF-236`: no escalation tier or default clock display is evidenced.
- Claims: `DC-014`, `DC-016`, `DC-017`, `DC-021`, `DC-025`, `DC-026`.

### Objective Genes

- Existing `OBJ-026`: reach the Promenade exit of the generated biome by
  traversing it, with the exit interaction as the required interaction and
  the Promenade arrival as the retained successor.
- Rejected `OBJ-164`: the exit needs no event. Rejected `OBJ-029`: no
  hostile set must be cleared. Rejected `OBJ-156`: no guardian chain and
  no escape settlement. Rejected `OBJ-113`, `OBJ-148`, `OBJ-153`,
  `OBJ-155`: no authored episode or captivity gate.
- Success, evaluation and failure: success is the Promenade arrival with
  the carried run state, retained on the save sources' common ground of a
  quit run resumed by `Continue`; failure is
  death, which resets the run while keeping unlocks; there is no retry
  inside the run. Claims: `DC-007`, `DC-018`, `DC-022`–`DC-024`.

### Time Genes

- Existing `TIM-003`: enemies, projectiles, traps, the recovery drain, the
  protection cooldown and the run timer advance in real time while inputs
  are accepted.
- Rejected `TIM-021`: its boundary excludes a run that restarts from an
  initial state on defeat, which is exactly this game's failure model, and
  its sole carrier's campaign profile shares no boundary with a run reset
  that could be kept without erasing that exclusion; the quit-save and
  `Continue` behaviour is therefore a documented persistence parameter of
  `SYS-167` and `SYS-469`, not a gene. Rejected `TIM-007`: no branchable
  save. Rejected `TIM-005`, `TIM-001`: no phase or turn. The publisher's
  remark that quitting during a death once resumed from the biome start is
  recorded as a parameter, not as a route step or as proof of the ordinary
  quit-save location. Claims: `DC-023`.

## Reproducible transitions

Row classes: **A** always executed on the ordinary route; **C** conditional on
an ordinary enemy attack, run parameter or player option; **F** failure
boundary; **V** documented verification path for the retained successor,
recorded from the sources and not executed in this analysis.

| Class | Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|---|
| A | New save slot at the main menu | Start a new game | Control begins in the Prisoners' Quarters starting area with the Rusty Sword equipped, no skill, no flask, stats at 1, no gold or cells | reproducible entry and `0 BSC` | `DC-001`, `DC-002`, `DC-005`, `DC-006` |
| A | The starting area | Walk, jump and roll to the starting-weapons room | The Beginner's Bow and Old Wooden Shield lie on the floor; the large door beyond leads into the generated biome | locomotion and the fixed starter set | `DC-006`, `DC-009` |
| C | The starting-weapons room | Pick up the bow, the shield, or neither | The taken item fills the second weapon slot under the starter slot restriction; the other stays | the loadout choice before the biome | `DC-006b`, `DC-011` |
| A | The large door | Enter the biome | The layout is assembled from authored chunks with two scroll vats, one shop, one treasure chest, traps and the Promenade exit; the map shows only explored rooms | generation and the explored map | `DC-007`, `DC-025` |
| A | A room with enemies | Engage with the combo or bow, roll through or past them, and read the attack prompts | Hits resolve in real time; enough damage during an enemy manoeuvre breaches and stuns it; the Shieldbearer's front absorbs hits until it is flanked or parried; the Grenadier's bomb explodes after landing; bypassing is legal, so no kill is required | real-time combat with cues, breach and facing | `DC-008`, `DC-011`, `DC-013`, `DC-014` |
| C | An enemy attack or trap connects | None | Health falls; 80% of the loss turns orange and drains; hitting an enemy while it remains restores part of the loss; a hit that would kill from above 25% health leaves 1 HP and stuns the enemies nearby, then the protection recharges for 45 s | recoverable loss and one-hit protection as outcome branches | `DC-012` |
| C | The shield was taken and an attack is incoming | Hold the shield, or tap it | Holding absorbs 75% of frontal damage; a timed tap negates the hit, stuns a melee attacker and reflects a projectile | the block and parry options | `DC-011` |
| C | An enemy is killed | None | Gold and cells fly to the Beheaded within range; a blueprint or item assigned at generation drops; the first Zombie killed drops the Blood Sword blueprint | drops and a carried blueprint, when the run kills | `DC-015` |
| C | A scroll vat is reached | Interact and choose Brutality, Tactics or Survival | The chosen stat gains one point, matching items' damage rises by 15% and maximum health rises; the choice persists for the run | the stat offer and its composition | `DC-016` |
| C | The shop is reached | Buy an offered weapon with gold, or leave | Gold falls by the shown price; the weapon enters a weapon slot or replaces one; whether a skill can be offered on a fresh profile is not evidenced | the run purchase | `DC-017a`, `DC-017b` |
| C | The route passes the guaranteed treasure chest | Open it, or pass it | One item at gear level II is sampled; taking a weapon into two held weapons forces a keep-or-drop choice | sampled loot against the bounded weapon slots, as an ordinary branch | `DC-015b`, `DC-006b` |
| A | The Promenade exit is reached | Interact with the exit | The biome closes and the Passage opens; time spent in the transition does not count toward the time door | the biome settlement | `DC-019a`, `DC-019b` |
| C | The Passage entrance, with a blueprint carried | None | The carried blueprint is delivered into the Collector's ledger automatically; a blueprint still carried at death would have been lost | automatic blueprint banking, when a blueprint was obtained | `DC-020a` |
| A | The Collector's room | Pass through; open the Collector's menu if cells are carried | Health Flask I is the only entry available, at 5 cells; the carried cells are shown against it; how many cells arrived, including none, is a run variable | the compulsory first entry and its affordability | `DC-020c`, `DC-020f` |
| C | At least 5 cells are carried | Commit cells to Health Flask I | The commitment reaches the price, the unlock completes and persists on the profile; any remainder stays in hand | the completing commitment | `DC-020b`, `DC-020c` |
| C | Fewer than 5 cells are carried, or a remainder is left | Commit the carried cells toward the next available entry, or keep them | Committed cells are retained on the profile as progress toward that entry and are not a completed unlock; cells kept in hand stay run-local | the partial commitment kept apart from completion | `DC-020d` |
| C | Cells are still carried at the room's exit | Strike the door until it breaks, or commit the rest | The exit stays barred while cells are carried; weapon hits reduce the door until it breaks and its body is removed; the cells stay run-local; one thread reports no penalty | the barred exit, the strike command and the destruction resolution | `DC-020e`, `DC-020g`, `DC-020h` |
| C | Guillain's offer | Choose one mutation, or none | The mutation fills the one slot the cleared biome grants and joins the build; its effects fire only in later biomes | the mutation offer | `DC-021` |
| C | The fountain, with health missing | Interact | Missing health is restored; on an undamaged arrival there is nothing to restore, and a flask bought in this Passage has no spent charge | the transition refill, conditional on a damaged arrival | `DC-019b` |
| C | The time door, and separately the kill-streak door | Enter a door if it is open | Each door tests its own predicate: the time door is open only if the run arrived at or below 2:00 (equality opens it), the streak door only if at least 30 damage-free kills were reached; either holds gems, 20 cells and a three-choice altar | two instances of the performance-gated reward door | `DC-019b`, `DC-019c` |
| A | The Passage exit | Enter the Promenade | The first Promenade state begins with the carried loadout, gold, cells, stats, mutation and the profile's completed unlocks, partial investments and delivered blueprints; the save sources' resume rules coincide at this entry | the retained successor | `DC-022`, `DC-023e` |
| F | Health reaches zero anywhere before the terminal | None | The run ends; a new run starts in the Prisoners' Quarters; gold (with no Gold Reserves), cells in hand, undelivered blueprints, gear and stats are gone; completed unlocks, paid investments, delivered blueprints and the run count remain | the death reset | `DC-018`, `DC-020d`, `DC-023f`, `DC-024` |
| V | The Promenade is shown | Documented path, not executed here: quit to the main menu, choose `Continue` | The guide says the run resumes where it was left and the 2025 thread says at the start of the current level; at this entry both rules name the same state, and no earlier state can be loaded; a reproducing analyst would compare loadout, gold, cells, stats and unlocks, and no returned value is claimed as observed | documented persistence of the arrival under conflicting resume statements | `DC-023a`–`DC-023e` |

## Strategic and experiential structure

- Planning horizon: leave the Prisoners' Quarters with as much health,
  gold and as many cells as possible, and with a weapon and stat build that
  the sampled drops and the two scrolls allow, because gold and cells are
  only useful if spent before death and the Promenade raises enemy tier.
- Local tactics: roll through a Zombie's leap and strike its back; flank or
  parry the Shieldbearer; close on the Grenadier before its second bomb;
  hit back immediately after taking damage while the orange portion lasts;
  avoid trading hits while the one-hit protection recharges; smash a door
  into a room to stun what waits behind it.
- Medium-term structure: the biome teaches traversal, the roll, the combo,
  drops and scrolls; the Passage teaches that delivered blueprints and invested cells
  outlive the run while everything else does not, that the exit will not
  open while cells are carried unless the door is broken down, and that
  speed and clean fighting each open their own extra room.
- Reversible versus irreversible: three state layers must be kept apart.
  Breach, stun, the orange recoverable portion, the protection cooldown and
  the kill streak are transient combat values; the Passage transforms a
  second layer by refilling health and flask charges, by banking delivered
  blueprints and by turning invested cells into retained progress or a
  completed unlock; the loadout, gold, remaining cells, stat points and
  mutation are run-local and survive only until death, while the completed
  unlocks, partial investments, delivered blueprints and run count are the
  profile's retained result. A quit run is resumed by `Continue`, but the
  sources disagree whether at the exact position or at the level start, so
  no intermediate position is claimed as protected.
- Failure attribution: the attack prompts, the orange health portion, the
  breach stun and the protection flash separate timing, greed and
  positioning errors; the layout, drops and blueprint assignment are the
  acknowledged variance.
- Player trust: a roll must pass through the attack it was timed against,
  the orange portion must be recoverable by hitting, a lethal hit above a
  quarter of health must leave one point, a delivered blueprint and an invested cell must
  survive the next death, and `Continue` must resume the quit run.
  Claims: `DC-008`–`DC-023`.

## Replay and variation

- What changes between runs: the biome layout, enemy placement, drop and
  blueprint assignments, shop stock, chest item, scroll placement, whether
  the reward doors are open, and which stat and mutation are chosen.
- Randomness or procedural generation: the biome is generated from authored
  chunks with fixed structural requirements; drops, blueprints and shop
  stock are sampled; the starter set and the two scrolls are fixed.
- Multiple viable strategies: sword-and-shield with parries, sword-and-bow
  at range, a single stat or a spread, a fast run for the time door or a
  full clear for the kill-streak door and more cells; enemies may also be
  bypassed at the cost of drops.
- Typical replay motive: reach the Passage with more cells to unlock the
  flask and then gear, and deliver the first blueprints; later progression
  is outside this packet. Claims: `DC-007`, `DC-015`–`DC-021`.

## Adjacent systems and history

- Direct product corridor: no reviewed predecessor or sequel exists in the
  corpus; the 2026 Castlevania: Belmont's Curse by Evil Empire is a
  separate product.
- Same-corpus corridors: Hades, the mathematically selected neighbour,
  shares the run's locomotion, dodge, strike, purchase and offer commands,
  the carried run state, the composed build, the single health pool and
  its persistence, the real-time combat and the unpreviewed drops, but
  gates each chamber's exit behind clearance, previews the next reward on
  its doors, keeps meta currency at death and ends only at the surface;
  The Binding of Isaac: Rebirth shares the seeded layout from authored
  rooms, the explored map, the contact pickups, the bounded typed slots, the
  composed build and the death reset that keeps unlocks, but locks rooms, uses a bounded room
  camera and clears by floor guardians; Hollow Knight shares locomotion,
  strikes, the health pool and real-time combat but returns death to a
  bench with a recoverable mark and rests to refill; Risk of Rain 2 shares
  purchases, interactions and real-time combat but escalates with elapsed
  time and gates its exit behind a charge event.
- Important differences: this packet's whole pressure is one generated
  biome fought in real time with a free roll, weapon combos and an optional
  shield, a health pool that pays back aggression and forgives one lethal
  hit, sampled gear against bounded weapon slots, and a transition that banks
  delivered blueprints and invested cells while everything else stays
  run-local, resumed after a quit only through `Continue`. Claims: `DC-004`–`DC-028`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-130`, `ACT-140`, `ACT-161`, `ACT-199`, `ACT-341`, `ACT-356`, `ACT-425`, `ACT-437`, `ACT-451` | starter items, combo timings, arrow count, parry window, roll timings, dive tiers, strike target class, commitment increment |
| System Behaviour | `SYS-004`, `SYS-167`, `SYS-215`, `SYS-222`, `SYS-450`, `SYS-456`, `SYS-464`, `SYS-467`, `SYS-469`, `SYS-578`, `SYS-755`, `SYS-832`, `SYS-833`, `SYS-834`, `SYS-835`, `SYS-852` | door material and hit count, chunk pool, enemy tiers, gear level, drop rarities, recoverable share, recovery and drain rates, replacement trigger, protection threshold and cooldown, fountain, Gold Reserves, entry ladder and prices, quit-save and `Continue` behaviour |
| Constraint | `CON-175`, `CON-404`, `CON-519`, `CON-596`, `CON-623`, `CON-624` | slot counts and classes, mutation slots per biome, door measures, comparators and thresholds, barrier-removal penalty |
| Information | `INF-002`, `INF-117`, `INF-119`, `INF-142`, `INF-180`, `INF-306` | map icons, HUD layout, prompt form |
| Objective | `OBJ-026` | exit identity, arrival snapshot |
| Time | `TIM-003` | run timer, cooldowns, drain rates |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `281` (`GAME-0001`–`GAME-0281`).
- Exact genome matches: none.
- Tied near matches: `GAME-0251` — Hades (`18 / 52 = 0.346154`).
- Supported combination subsets: none.
- Scan date: 2026-09-10.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0251` — Hades | `ACT-008`, `ACT-130`, `ACT-140`, `ACT-161`, `ACT-356`, `SYS-004`, `SYS-167`, `SYS-215`, `SYS-222`, `SYS-456`, `SYS-467`, `SYS-578`, `CON-175`, `CON-596`, `INF-002`, `INF-119`, `INF-306`, `TIM-003` | Both are one attempt of a run whose avatar runs, dodges and strikes in real time, buys from run merchants, commits exclusive build offers that compose into the attempt, carries health and currency across nodes under a single persistent health pool and sees neither the next room nor the next drop. Hades gates every chamber's exit behind clearing its hostiles, previews the next reward class on each door, composes divine boons into ability slots, keeps its meta currencies at death and settles only at the surface escape. Dead Cells instead traverses one seeded side-scrolling biome whose exit needs no clearance, banks eligible damage as health won back by attacking before the separate timed drain or replacement rule removes the opportunity, forgives one lethal hit on a cooldown, samples gear with level and quality against bounded weapon slots, banks delivered blueprints and invested cells at the transition, bars the Collector's exit while cells remain and resumes a quit run only through `Continue`. | Near, `0.346154` |

### Preserved research notes

- Reused genes: `ACT-008`, `ACT-130`, `ACT-140`, `ACT-161`, `ACT-199`,
  `ACT-341`, `ACT-356`, `ACT-425`, `ACT-437`, `SYS-004`, `SYS-167`,
  `SYS-215`, `SYS-222`, `SYS-450`, `SYS-456`, `SYS-464`, `SYS-467`,
  `SYS-469`, `SYS-578`, `SYS-755`, `CON-175`, `CON-404`, `CON-519`,
  `CON-596`, `INF-002`, `INF-117`, `INF-119`, `INF-142`, `INF-180`,
  `INF-306`, `OBJ-026` and `TIM-003`.
- Classification result: `New gene plus later common-core split`.
- Evidence and reasoning: thirty boundaries transfer from the reviewed
  corpus without any wording change; `CON-404` transfers after the minimal
  generalisation recorded in `TAXONOMY_CHANGE_042` (slot counts and classes
  as parameters) and `ACT-161` after `TAXONOMY_CHANGE_043` (an eligible
  breakable object as an aimed target, as the Half-Life carrier already
  exercised); `SYS-755` transfers unchanged for the door's destruction.
  The corpus had no recoverable-loss health rule, no cooldown-gated one-hit
  protection, no automatic banking of carried unlock tokens at a
  transition, no run-currency commitment that retains partial progress on
  the profile, no pay-toward command that is legal while the target stays
  unaffordable, no reward door gated by one declared performance predicate
  per door, and no settlement exit barred while unspent currency is
  carried, so seven genes are new; each is portable to other run-based
  rulesets and none is named after a biome, enemy, item or update.
  `CON-191` and `TIM-021` were tested and rejected: the first requires the
  full cost to be affordable, which partial commitment contradicts, and the
  second excludes a run that restarts on defeat. The grades follow the
  evidence-independence matrix: `CON-623` is `Corroborated` (publisher and
  wiki); `CON-624` is `Corroborated` on the door state and breakability
  (wiki and threads), with the no-penalty clause `Limited` and kept as a
  parameter; at their original isolation, `SYS-832`, `SYS-833` and `SYS-834`
  rested on the wiki alone and were `Limited`; `SYS-835` and `ACT-451`
  inherit the `Limited` partial-retention clause. On 2026-09-10,
  `TAXONOMY_CHANGE_065` preserves
  `SYS-832` as the two-carrier damage-bank and attack-recovery core and moves
  the Dead Cells-only timed drain and replacement transition to `SYS-852`.

## Taxonomy impact

- Registry changes: the original seven Active genes listed above plus new
  `SYS-852`; `SYS-832` is generalised across Dead Cells and TEKKEN 8 by
  [`TAXONOMY_CHANGE_065`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_065.md),
  which separates this game's timed drain and replacement into `SYS-852`;
  `CON-404`
  generalised by
  [`TAXONOMY_CHANGE_042`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_042.md)
  so that typed-slot counts and item classes are parameters; `ACT-161`
  generalised by
  [`TAXONOMY_CHANGE_043`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_043.md)
  so that an eligible breakable world object may be the aimed target;
  thirty further Active genes gain this game as an additional carrier. No
  lifecycle, ID or earlier reviewed signature changes.
- Taxonomy-change record: `TAXONOMY_CHANGE_042`, `TAXONOMY_CHANGE_043` and
  `TAXONOMY_CHANGE_065`.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; the
  Beheaded, the Prisoners' Quarters, the Promenade of the Condemned, the
  Passage, the Collector, Guillain, the Rusty Sword, the Beginner's Bow, the
  Old Wooden Shield, every enemy, item, mutation and blueprint name, `Boss
  Stem Cell`, `Continue`, `Update 35.9` and every application, package,
  build and branch identifier remain parameters or literal product terms.

## Negative results

- No direct-play, entitlement, screenshot, video or audio claim.
- No skill, amulet, flask use, mutation effect, affix, backpack, curse,
  elite, boss, later biome, DLC, mode or meta-history mechanic is imported;
  skill availability on a fresh profile is excluded for insufficient
  evidence rather than asserted.
- `ACT-190`, `ACT-223`, `ACT-436`, `ACT-143`, `ACT-093`, `ACT-091`,
  `ACT-136`, `ACT-118`, `ACT-248`, `ACT-134`, `ACT-175`, `ACT-207`,
  `ACT-273`, `ACT-128`, `ACT-191`, `ACT-231`, `ACT-401`,
  `ACT-391`, `ACT-040`, `ACT-131`, `SYS-782`, `SYS-362`, `SYS-468`, `SYS-166`,
  `SYS-399`, `SYS-610`, `SYS-369`, `SYS-820`, `SYS-364`, `SYS-426`,
  `SYS-335`, `SYS-116`, `SYS-159`, `SYS-210`, `SYS-171`, `SYS-168`,
  `SYS-057`, `CON-191`, `CON-284`, `CON-485`, `CON-353`, `CON-210`,
  `CON-188`, `CON-269`, `CON-402`, `CON-440`, `CON-068`, `CON-187`,
  `CON-183`,
  `INF-179`, `INF-305`, `INF-317`, `INF-327`, `INF-236`, `OBJ-164`,
  `OBJ-029`, `OBJ-156`, `OBJ-113`, `OBJ-148`, `OBJ-153`, `OBJ-155`,
  `TIM-021`, `TIM-007`, `TIM-005` and `TIM-001` are rejected with the
  smallest counterexamples recorded above.
- No hit, death, timer target, farm, secret, seed or item is instructed to
  make a gene legal; damage, recovery, one-hit protection, the reward
  doors and death are admitted only as branches that the run's own rolls
  and the player's ordinary options produce.
- No reload verification is claimed as executed; the exact quit-save
  location is recorded as a source conflict rather than resolved; the
  run-timer display and the exit-door preview are excluded for
  insufficient evidence rather than admitted; no partial commitment is
  described as a completed unlock; no kill, drop or blueprint is described
  as required; the fountain's effect is conditional on missing health; and
  no Steam announcement is described as read in full beyond the three
  named.

## Delta summary

## New facts

- [Confirmed | Direct | High] Current base-package Windows availability and
  the eight DLC or music applications are fixed in `DC-001`.
- [Observation | Direct | High] The publisher's `Update 35.9` label and
  its 2026-06-15 stability-patch description are stated by Motion Twin
  itself in `DC-002b`; the 2022 remark about quitting while dying is the
  publisher's own words in `DC-023d` (`Medium`).
- [Observation | Corroborated | High] The `0 BSC` fresh profile, the
  publisher's no-checkpoint and retained-unlock premise, the panic roll,
  the single health pool and the persistence of a completed Collector
  unlock are bounded in `DC-004`, `DC-005`, `DC-010a`, `DC-012a` and
  `DC-020b`.
- [Observation | Corroborated | Medium] The base-package setup, the fixed
  starter set, the chunk-assembled biome, drops, scrolls, the shop,
  run-local currencies, the Passage and its doors, the first-level 30-kill
  challenge, the compulsory first unlock, the barred Collector exit and its
  bypass, the HUD and the death reset are bounded in `DC-003`, `DC-006a`,
  `DC-007a`, `DC-015a`, `DC-016a`, `DC-017`, `DC-018`, `DC-019a`,
  `DC-017a`, `DC-019c`, `DC-020c`, `DC-020e`, `DC-020g`, `DC-023f` and
  `DC-026`.
- [Observation | Conflicting | Medium] The quit-save resume location is
  stated as the exact position by the guide and as the level start by the
  2025 thread (`DC-023e`); only their common ground is admitted.
- [Observation | Limited | Medium] The build identifier and its link to the
  label, the exact starter, layout, enemy, input, roll, combo, recovery,
  one-hit-protection, breach, cue, drop, scroll, Passage, automatic
  delivery, partial investment, cell-yield, map, Promenade, run-counter,
  optional-room and individual save-statement values rest on one family
  each (`DC-002a`, `DC-002c`, `DC-006b`, `DC-007b`, `DC-008`, `DC-009`,
  `DC-010b`, `DC-011`, `DC-012b`, `DC-012c`, `DC-013`, `DC-014`,
  `DC-015b`, `DC-016b`, `DC-019b`, `DC-020a`, `DC-020d`, `DC-020f`,
  `DC-020h`, `DC-022`, `DC-023a`, `DC-023b`, `DC-023c`, `DC-024`, `DC-025`,
  `DC-027`, `DC-028`); the initial mutation set and the fresh profile's
  skill pool are `Limited | Low` (`DC-021`, `DC-017b`).

## New genes

- [Observation | Corroborated | Medium] `CON-623` and `CON-624` isolate the
  transition reward door whose one declared measure must satisfy that
  door's comparison predicate, and the settlement exit barred while unspent
  unlock currency is carried unless the barrier is removed.
- [Observation | Limited | Medium] `ACT-451`, `SYS-833`, `SYS-834`, `SYS-835`
  and `SYS-852` isolate the pay-toward command, cooldown-gated one-hit
  protection, automatic banking of carried blueprints, run-currency commitment
  with retained partial progress, and timed expiry or replacement of a
  recoverable-health bank. `SYS-832` is now the `Confirmed | Corroborated |
  High` two-carrier common core for banking eligible loss and regaining it by
  attacking.

## New combinations

- [Observation | Corroborated | High] `No new combinations`; none of the 271
  verified sets is a strict subset of this signature, and the nearest misses
  (`COMB-0270`, `COMB-0271`) lack two genes each.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_042` generalises
  `CON-404` so that typed-slot counts and item classes are parameters, and
  `TAXONOMY_CHANGE_043` generalises `ACT-161` so that an eligible breakable
  world object may be the aimed target. `TAXONOMY_CHANGE_065` generalises
  `SYS-832` and extracts `SYS-852`; no lifecycle alias is created.

## New questions

- Does TEKKEN 8's offline Versus match, the next ordered subject, share any
  of the recoverable-health or one-hit-protection structure, or is its
  recoverable health a fighting-game rule with a distinct boundary?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0283` — TEKKEN 8, only under a new
  game-specific prompt after this unit's independent audit.
- Optimisation criterion: replace a generated single-player biome with a
  fixed two-fighter ruleset while keeping real-time combat and a retained
  result.
- Expected information gain: separate one-on-one guard, throw and
  recoverable-health boundaries from the run-based combat above.
- Backlog impact: advances the recorded 280-to-288 calibration horizon.

## Why this game

- [Hypothesis | Limited | High] The second transfer test had to succeed on
  a generated real-time run with no shared substrate with the previous
  turn-based packet, so success could not come from reusing that record's
  shape.
