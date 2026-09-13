---
game_id: GAME-0281
slug: darkest-dungeon
game_title: Darkest Dungeon
analysis_status: reviewed
reviewed: 2026-09-08
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-019
    - ACT-199
    - ACT-341
    - ACT-449
    - ACT-450
  system:
    - SYS-004
    - SYS-362
    - SYS-388
    - SYS-538
    - SYS-825
    - SYS-826
    - SYS-827
    - SYS-828
    - SYS-829
    - SYS-830
    - SYS-831
  constraint:
    - CON-001
    - CON-210
    - CON-622
  information:
    - INF-002
    - INF-003
    - INF-119
    - INF-128
    - INF-332
    - INF-333
  objective:
    - OBJ-029
  time:
    - TIM-001
    - TIM-021
---

# Game: Darkest Dungeon

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `262060`, base package `33877`, default public branch Build ID `24960041`
  (built and published 2026-08-27), which Red Hook's own announcement of the
  same day labels the `Retail 27890` hotfix of The Fire's Edge update cycle;
  checked 2026-09-08. The Steam build identifier is a secondary distribution
  observation; the `27890` label is Red Hook's. The `legacy` branch (Build
  `9545898`, "2022 version before updates") and the `coming_in_hot` public
  beta (Build `25110930`, 2026-09-03) are excluded.
- Product boundary: this is the 2016 Red Hook Studios game, not Darkest
  Dungeon II, and not any of its six DLC applications — The Crimson Court
  (`580100`), The Shieldbreaker (`702540`), The Color of Madness (`735730`),
  the free The Musketeer (`445700`), the free The Butcher's Circus
  (`1117860`) and The Fire's Edge (`4964110`, released 2026-08-18) — nor the
  soundtrack (`345800`), a console, iPad or macOS/Linux build, mods or the
  Steam Workshop. DLC content joins a campaign only through the per-campaign
  DLC toggles shown at campaign creation; this packet leaves every toggle
  disabled, and Red Hook states that The Fire's Edge is additive and changes
  no existing hero or enemy, so the Old Road content is the same whether or
  not a free DLC is installed.
- Campaign settings: New Campaign → estate name → game mode `Darkest`, which
  Red Hook's Radiant Update notes call the normal mode and the official wiki
  records as the default; the gameplay options stay at their default
  `Darkest Dungeon Config` state (corpses on, mortality debuffs on, retreats
  may fail, combat-delay penalties on). `Radiant`, `Stygian` and the DLC
  `Bloodmoon` mode are separate packets; the only Old Road differences they
  document are Stygian's Transcendent Terror curio and seven-point light
  decay.
- Entry: first ordinary control of the two-hero party in the Old Road
  entrance room after the two opening cinematics, with Reynauld (Crusader,
  resolve level 0, rank 1) and Dismas (Highwayman, resolve level 0, rank 2),
  their fixed four equipped skills and fixed quirks, no trinkets, the light
  meter at 100 and the two-room map revealed. No source documents any item
  in the party's inventory at entry: no provisioning stage precedes the Old
  Road, the official wiki's Old Road page names no starting supplies, and
  the only torch mentioned on the route is one static guide's random loot
  after the final battle, after which no travel or battle remains.
- Primary decision loop: read the light band, each hero's health, stress and
  status icons, the remaining-action pips and the corridor map; walk the party forward
  along the corridor; when a battle begins, accept the surprise check and the
  hidden speed-plus-roll order; on each hero's turn choose one of its four
  skills that is legal from its current rank against a legal target rank, or
  shift the hero along the formation at the cost of the turn, or pass; watch
  the hit, protection, critical and status resolution and the brigands'
  weighted skill choices; work around corpses that hold the enemy line;
  decide whether to snuff the torch for loot at the cost of stress, surprise
  and enemy strength; investigate or ignore the tent; take loot into the
  sixteen-slot inventory; repeat in the battle room; then accept the
  completion prompt, the debrief and the first retained Hamlet state.
- Positive terminal: both authored encounters are cleared (`OBJ-029` twice),
  the completion prompt is accepted, the debrief converts loot, pays the
  5,000 gold reward and 2 resolve experience, restores health, caps stress at
  100 and returns the surviving roster, and the campaign arrives in the
  Hamlet at Week 1 with the `Welcome home...` narration. Persistence of that
  state is documented, not observed: the game autosaves constantly and
  exposes no manual save or load, and Red Hook's notes describe battles and
  Death's Door debuffs resuming after the game is restarted, so no earlier
  state can be loaded. The reproducible verification path — quit to the
  desktop, relaunch, select the same campaign profile and compare the week,
  roster, gold and stress — is recorded here and was not executed in this
  analysis; no returned value is claimed as observed. No Hamlet action after
  the arrival is admitted.
- Negative terminal: there is no campaign failure on the Old Road. A hero at
  zero health stands at Death's Door and every further hit rolls a deathblow;
  a dead hero is permanently removed. Even a full party wipe settles into the
  same Hamlet arrival with the reward and replacement recruits in the Stage
  Coach, which is documented as a retained state, not a game over.
- Included: direct corridor walking; rank-legal skill selection and
  targeting; the formation shift; the light meter's decay, bands and manual
  snuff; the battle-start surprise check; per-round hidden
  initiative with one action per unit; hit, protection, critical and
  resistance-tested status resolution including bleed ticks, stun and
  knockback; the brigands' weighted skill and target selection; corpses that
  hold enemy ranks; per-hero stress accumulation, relief and carry-over;
  Death's Door, the deathblow roll and permanent death; curio investigation
  with random outcomes; the loot window, slot-bounded pickup and its
  disclosure; encounter rewards and the debrief; roster settlement; the
  visible light meter and band, the per-unit remaining-action markers, the
  hero panels and the concealed corridor contents; autosave-only persistence
  with no reloadable earlier state; two finite hostile sets.
- Excluded: everything after the first retained Hamlet state, including
  recruiting, provisioning, the Ruins tutorial quest, buildings, upgrades,
  camping, hunger checks, traps, scouting as a separate decision, retreat and
  abandonment (both impossible on the Old Road), reinforcements, the
  resolve-test affliction or virtue outcomes and the heart attack, which the
  Old Road's two short fights do not ordinarily reach, torch refuelling and
  every other inventory-item use, because no source establishes a carried
  torch or any other item in the packet's inventory, inspection of hostile
  statistics beyond the health bar, because no source documents such a
  tooltip, quirk gain or removal, trinkets, town events, the weekly clock, later
  regions, bosses, the Darkest Dungeon location, `Radiant`, `Stygian` and
  `Bloodmoon`, every DLC hero, region, district and mode, The Butcher's
  Circus, Workshop mods, Darkest Dungeon II, console and mobile editions,
  achievements as goals, screenshots, official artwork, video and audio.
- Reproducible parameterisation: install application `262060` from package
  `33877` on the default public branch; start New Campaign, name the estate,
  select `Darkest`, leave every DLC toggle disabled and every gameplay option
  at its default. From first control, walk the corridor to the right, fight
  the Brigand Cutthroat using rank-legal skills, investigate or ignore the
  Brigand's Tent, enter the battle room, defeat the Brigand Bloodletter and
  Brigand Fusilier, accept the completion prompt and leave for the Hamlet
  without opening the trapped chest, and accept the debrief. The documented
  persistence check — quit to the desktop, relaunch and reopen the same
  profile — is the verification path a reproducing analyst would execute; it
  was not executed here. Which skills are
  chosen, whether a stun is attempted, whether and when the torch is snuffed,
  whether the tent is investigated, which loot drops, how much damage,
  bleed and stress each hero takes, whether either hero reaches Death's Door
  or dies, and elapsed time are run parameters; no hit, snuff, detour or
  resource spend is instructed. Live combat leaves the ordinary route in
  outcome branches at the debrief: an undamaged branch, a damaged branch in
  which health is restored at the Hamlet while stress persists, a Death's
  Door branch, a death branch in which the Stage Coach supplies a
  replacement, and the documented wipe branch. None is chosen deliberately.
- Potential scoped modules: the first Ruins quest with provisioning, hunger,
  traps, scouting and camping; one Hamlet management week; a `Stygian`
  campaign with its failure conditions; a DLC-enabled campaign; The Butcher's
  Circus; Darkest Dungeon II requires a separate scope.
- Direct-play status: not conducted. Valve application and package data,
  Red Hook's Steam announcements, official site, support index and
  achievement list establish lawful availability, product separation, the
  current branch, the DLC set, the mode and option defaults, the tutorial's
  mandatory place and the autosave profile. Red Hook's own announcements
  independently state the per-round speed-plus-die initiative and its hidden
  order, the gold remaining-action pips, the torch meter at the top of the
  screen, corpses that block positions and targeting, the surprise roll,
  Death's Door with its mortality debuff and deathblow resistance, the light
  band's dodge bonus, the option defaults and the resumption of battles after
  a restart. The official Darkest Dungeon wiki, including its transcription
  of the in-game Glossary, is one community-maintained source family; it
  alone supplies the exact numeric combat, light, stress, corpse, surprise
  and hostile-policy values, the rank-legality rule, the snuff command and
  the Old Road layout, and every claim resting on it alone is graded
  `Limited`. A second static route corroborates the two encounters, the tent
  and the reward, and dated community threads corroborate the tutorial lock
  and the save behaviour. The in-game Glossary was not inspected as a
  shipped artefact. This is an evidence-backed rules reconstruction, not a
  claimed captured playthrough or entitlement. No video or audio was opened,
  played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DD-001` | The admitted product is the 2016 Red Hook Studios Windows Steam application `262060`, base package `33877` containing only that application, separate from six DLC applications and the soundtrack | Confirmed | Direct | High | P1, P2, P7 |
| `DD-002` | The default public branch is Build `24960041` published 2026-08-27, matching Red Hook's `Retail 27890` hotfix announcement; the `legacy` and `coming_in_hot` branches are separate | Observation | Corroborated | High | P3, S1 |
| `DD-003` | DLC content applies to a campaign only when enabled on that campaign's save at creation or later, and cannot be disabled afterwards | Observation | Corroborated | Medium | P3, P7, S2, S5 |
| `DD-004` | The Fire's Edge is additive, changes no existing hero or enemy and adds two heroes, a Burn mechanic, trinkets and districts, none of which alters the Old Road | Observation | Corroborated | High | P3, P4, S2 |
| `DD-005` | `Darkest` is the normal, default campaign mode chosen at creation and immutable afterwards; `Radiant` relaxes progression and `Stygian` adds failure conditions, more stress, faster light decay and, on the Old Road, the Transcendent Terror curio | Observation | Corroborated | High | P3, S2 |
| `DD-006` | Gameplay options default to the master `Darkest Dungeon Config`, which keeps corpses, mortality debuffs, combat-delay penalties and failable retreats enabled | Observation | Corroborated | High | P3, P6 |
| `DD-007` | Every new campaign begins on the mandatory, unskippable Old Road with Reynauld (Crusader) and Dismas (Highwayman) at resolve level 0, fixed skills and fixed quirks and no trinkets | Observation | Corroborated | High | P3, P6, S2, S3, S5 |
| `DD-008a` | The Old Road is one entrance room, one corridor and one battle room, entered after the second cinematic | Observation | Limited | Medium | S2 (Old Road, Locations); S3 mirrors S2 |
| `DD-008b` | Every campaign starts on the Old Road and it cannot be skipped | Observation | Corroborated | Medium | S2 (Locations), S5 (2017 thread), P3 (2016-01-19 expanded tutorial; 2016-02-05 dying on the Old Road) |
| `DD-008c` | Retreat is impossible on the Old Road and it cannot be entered again after the first Hamlet arrival | Observation | Limited | Medium | S2 (Locations) only |
| `DD-009a` | The corridor holds one Brigand Cutthroat battle midway and the room holds a size-two Brigand Bloodletter in ranks 1–2 with a Brigand Fusilier in rank 3 | Observation | Limited | Medium | S2 (Old Road); S4 names only a first and a second enemy |
| `DD-009b` | Two battles must be won to complete the quest | Observation | Corroborated | Medium | S2 (Old Road), S4 |
| `DD-010a` | The corridor's Brigand's Tent is a Scrounging curio found only on the Old Road that yields two loot draws by hand | Observation | Limited | Medium | S2 (Curios, Old Road) |
| `DD-010b` | The room's Bandit's Trapped Chest yields no loot and inflicts blight by hand unless a Skeleton Key is used | Observation | Conflicting | Low | S2 (Old Road) against S4, which says trapped chests may hold food; the chest is ignored on the route |
| `DD-011a` | Heroes and enemies occupy ranks 1–4 per side; every skill declares launch ranks and target ranks; a multi-rank enemy is hit at any of its ranks | Observation | Limited | Medium | S2 (Combat Mechanics, Old Road, hero and enemy pages) |
| `DD-011b` | A corpse keeps the slain enemy's ranks, so skills must reach around it and random targeting ignores it | Observation | Corroborated | High | S2 (Corpse, Glossary), P3 (2016-01-28 random targeting; 2017-06-20 units behind corpses) |
| `DD-012a` | At the start of every combat round each unit's initiative is re-rolled as its speed plus a die roll, the resulting order is not shown, and each unit ordinarily acts once per round | Observation | Corroborated | High | P3 (2020-04-30 Butcher's Circus announcement), S2 (Combat Mechanics, Glossary) |
| `DD-012b` | The die is 1–8, heroes win ties and lower ranks act first within a side | Observation | Limited | Medium | S2 (Combat Mechanics); P3 records only a 2015 experiment with a D8 |
| `DD-012c` | Each hero and brigand carries a gold pip beside its health bar whose tooltip reads as actions remaining, cleared as it acts, while the remaining order stays hidden | Observation | Corroborated | High | P3 (2015-12-21 tooltips; 2020-04-30 gold pips), S2 (Combat Mechanics) |
| `DD-013a` | A skill's hit chance is its accuracy minus the target's dodge | Observation | Limited | Medium | S2 (Combat Mechanics, Glossary); P3 confirms only that hero accuracy and monster dodge oppose each other (2015-12-21) |
| `DD-013b` | A hidden +5 applies after modifiers, a displayed 95 or more always hits, and a critical deals 150% of the skill's maximum damage | Observation | Limited | Medium | S2 (Combat Mechanics) |
| `DD-013c` | Protection reduces direct damage by a percentage, capped internally | Observation | Corroborated | Medium | S2 (Combat Mechanics), P3 (2016-12-14 internal PROT cap) |
| `DD-014a` | Stun, bleed, blight, knockback and debuff effects roll their chance against the target's matching resistance | Observation | Corroborated | Medium | S2 (Move, Stun, Glossary), P3 (2018-08-15 stun and debuff resist; 2018-07-16 move resist) |
| `DD-014b` | A stunned unit passes its next turn and gains stun resistance afterwards | Observation | Corroborated | Medium | S2 (Glossary, Old Road), P3 (2017-09-18 stun-resist increment) |
| `DD-014c` | Bleed and blight tick at each of the target's round starts and at each corridor step | Observation | Limited | Medium | S2 (Glossary) |
| `DD-015a` | An enemy killed by ordinary damage leaves a corpse that occupies its ranks, takes no turns and is not chosen by random targeting | Observation | Corroborated | High | S2 (Corpse, Glossary), P3 (2015-12-21 corpses option; 2016-01-28; 2017-06-20) |
| `DD-015b` | A corpse holds a fraction of the enemy's health without protection or dodge, disappears at the end of the fourth round, and is not left by critical or damage-over-time kills | Observation | Limited | Medium | S2 (Corpse); P3 only hints at a critical clearing a corpse (2018-08-15) |
| `DD-016a` | Each battle starts with a two-sided surprise check; a surprised party is shuffled and surprised monsters act last in round 1 | Observation | Corroborated | High | S2 (Surprise, Glossary), P3 (2015-12-14 surprise rolls saved; 2016-02-02 Glossary entry; 2017-06-19 Fanatic surprise) |
| `DD-016b` | The base chance is 10%, light and scouting modify it, a party at Radiant light cannot be surprised, and a surprised party cannot retreat in round 1 | Observation | Limited | Medium | S2 (Surprise, Light Meter) |
| `DD-017a` | One shared light meter depletes as the party traverses corridor segments and rooms, faster in Stygian | Observation | Corroborated | Medium | S2 (Light Meter, Expeditions), P3 (2017-02-09 more light loss per step in Stygian) |
| `DD-017b` | The meter starts at 100, falls six points per new segment and one per explored segment, and exposes five bands from Radiant Light to Black as Pitch | Observation | Limited | Medium | S2 (Light Meter) |
| `DD-017c` | The current band scales stress, party dodge, scouting and surprise chances, hostile accuracy, damage and criticals, hero criticals and extra loot draws | Observation | Corroborated | High | S2 (Light Meter), P3 (2017-06-19 torchlight dodge bonus; 2020-05-27 Radiant Light dodge values; 2017-02-09 darkness penalties), P7 (the ever-encroaching dark) |
| `DD-017d` | The player may lower the meter by 25 or fully by interacting with the meter at any time outside an attack animation | Observation | Limited | Medium | S2 (Light Meter, Old Road) |
| `DD-017e` | Clicking the torch meter at the top of the screen spends one inventory torch for +25 light; Bulwark of Faith also raises the light | Observation | Corroborated | High | P3 (2015-12-21), S2 (Light Meter, Torch, Old Road); no torch is evidenced in the packet, so the rule stays outside scope |
| `DD-017f` | The torch meter is displayed persistently at the top of the screen with its band and effect icons | Observation | Corroborated | High | P3 (2015-12-21; 2018-08-15 torch tooltip zones), S2 (Light Meter) |
| `DD-018a` | Stress rises from hostile stress skills, from received critical hits and from occasional travel events, scaled by the light band | Observation | Corroborated | High | S2 (Stress, Expeditions, Glossary), P3 (2015-11-30 stress design; 2015-12-21 monster stress output), P7 |
| `DD-018b` | A received critical adds 10 stress with a 50% chance of 5 to the party; a kill has a 50% chance of 3 relief and an own critical relieves 3; passing costs 5 | Observation | Limited | Medium | S2 (Stress, Expeditions) |
| `DD-018c` | Stress is not restored at the end of an expedition and is capped at 100 on return to the Hamlet | Observation | Corroborated | Medium | S2 (Stress), P7 (heroes rest in town to keep stress in check); the cap value rests on S2 |
| `DD-018d` | Stress tests resolve at 100 and a heart attack at 200 drops the hero to Death's Door | Observation | Corroborated | High | P3 (2015-11-30), S2 (Stress, Glossary); outside the packet |
| `DD-019a` | A hero at zero health stands at Death's Door, each further hit rolls against deathblow resistance, and healing off it leaves a mortality debuff until the quest ends | Observation | Corroborated | High | P3 (2015-11-30 mortality debuffs; 2018-08-15 and 2020-05-27 deathblow resistance), S2 (Death's Door, Glossary) |
| `DD-019b` | The Death's Door penalties are −10 ACC, −25% DMG, −5 SPD and +33% stress, base deathblow resistance is 67% and the cap is 87% | Observation | Limited | Medium | S2 (Death's Door) |
| `DD-020a` | Hero death is permanent and removes the hero from the roster | Observation | Corroborated | High | P7 (character permadeath), S2 (Death, Old Road) |
| `DD-020b` | A hero lost on the Old Road is replaced by Stage Coach recruits and a full wipe still settles into the Hamlet with the reward | Observation | Corroborated | Medium | S2 (Old Road), P3 (2016-02-05: the campaign continues after dying on the Old Road) |
| `DD-021` | At Apprentice level the Cutthroat selects Slice and Dice, Uppercut Slice or Shank with equal chance, the Bloodletter uses Point Blank Shot only from rank 1 and never twice in a row, and the Fusilier uses Blanket Fire from ranks 2–4 or Rushed Shot from rank 1 | Observation | Limited | Medium | S2 (Brigand Cutthroat, Brigand Bloodletter, Brigand Fusilier) |
| `DD-022a` | Loot appears in a window after each battle and from curios and is taken or left | Observation | Corroborated | Medium | S2 (Items, Old Road), S4 (gold after the first battle; gold, an emerald and a torch after the second) |
| `DD-022b` | The inventory has sixteen slots with typed stack limits, and lower light adds extra loot draws | Observation | Limited | Medium | S2 (Inventory, Items, Light Meter) |
| `DD-023a` | Completing the objective prompts continue-or-leave; the debrief converts loot to gold and pays the 5,000 gold Old Road reward | Observation | Corroborated | Medium | S2 (Expeditions, Old Road), S4 |
| `DD-023b` | The debrief grants resolve experience, 2 points on the Old Road, which reaches level 1 in `Darkest`, restores health and retains stress and afflictions | Observation | Limited | Medium | S2 (Expeditions, Resolve Level, Old Road); stress retention is corroborated under `DD-018c` |
| `DD-024` | The first Hamlet state is Week 1 with the surviving heroes, the reward and a Stage Coach holding a Plague Doctor and a Vestal, marked by the `Welcome home...` narration and the `Reach the Estate` achievement | Observation | Corroborated | High | P6, S2 (Old Road) |
| `DD-025a` | Progress autosaves constantly into one campaign profile with no manual save or load | Observation | Corroborated | Medium | S2 (premise text), P5 (`Profile_0` save location), S5 (2016 thread) |
| `DD-025b` | A reopened profile resumes the retained state, including a battle in progress and its Death's Door debuffs | Observation | Corroborated | Medium | P3 (2017-07-06 restart in battle; 2015-12-14 surprise rolls restored; 2017-09-18 turn-order saving), S5; documented, not executed here |
| `DD-025c` | The game writes a save when the player quits | Observation | Limited | Medium | S5 (2016 thread) only |
| `DD-026` | Hunger checks, camping, corridor traps, scouting decisions, retreat, abandonment, reinforcements, combat item use and the resolve-test outcomes are not exercised by the ordinary Old Road route | Observation | Limited | Medium | S2 (Old Road, Locations, Hunger, Camping, Trap), S5 |
| `DD-027` | The bounded identity is two-hero formation combat under hidden per-round initiative, resistance-tested status effects, corpses that hold the line, a shared light meter traded against stress and loot, per-hero stress that survives the expedition, Death's Door as the only failure boundary, and autosave-only persistence into the first retained Hamlet state | Observation | Limited | Medium | `DD-005`–`DD-026`; inherits the weakest material clause |

## Basic data

- Release / origin: Red Hook Studios; Early Access 2015-02-03, full release
  for Windows and OS X on 2016-01-19; The Fire's Edge DLC and its base-game
  update on 2026-08-18.
- Platform or physical form: lawfully available English Windows Steam client,
  base package `33877`; one offline single-player campaign opening.
- Puzzle family: tactical forecast and counterplay; ordered dependency
  sequencing.
- Primary and official sources, accessed 2026-09-08:
  - `P1` — [Valve application data](https://store.steampowered.com/api/appdetails?appids=262060&cc=ua&l=english),
    for title, Red Hook Studios as developer and publisher, Windows, macOS
    and Linux support, single-player and Steam Cloud categories, the
    2016-01-19 release, package `33877` and the seven DLC or music
    applications.
  - `P2` — [Valve base package data](https://store.steampowered.com/api/packagedetails?packageids=33877&cc=ua&l=english)
    for package `33877` containing only application `262060`, and the
    application data for `445700`, `580100`, `702540`, `735730`, `1117860`,
    `4964110` and `345800` for their types, release dates and free status.
  - `P3` — [Red Hook's Steam announcements for the application](https://store.steampowered.com/news/app/262060),
    read in full through Valve's news feed: the 2026-08-18 The Fire's Edge
    release, the 2026-08-21, 2026-08-24, 2026-08-25 and 2026-08-27 hotfixes
    (`27850`, `27860`, `27868`, `Retail 27890`), the 2026-09-03
    `coming_in_hot 27942` notes, the 2025-04-30 Build `25807` unified-binary
    and `legacy` branch notice, the 2017-02-09 Radiant Update notes (normal
    `Darkest` mode, selectable Stygian, more save slots), the 2016-01-19 full
    release notes (expanded beginning tutorial, `DD Strict` options), the
    2015-12-21 Holiday Cheer notes (`Darkest Dungeon Config` default,
    corpses, mortality debuffs, retreat option), the 2015-11-30 Inhuman
    Bondage notes (heart attack to Death's Door, mortality debuffs), the
    2016-02-05 Build `13488` and 2016-03-09 Build `13850` notes (dying on the
    Old Road; Dismas at full health in the tutorial), the 2020-06-22 mod
    showcase ("you don't even need to enable the Circus on your save"), and
    the rule statements read for this record's independence matrix: the
    2020-04-30 Butcher's Circus announcement ("at the start of each combat
    round we roll all combatants' initiative … the character's speed plus a
    die roll. We don't explicitly show who will act next … we use gold pips
    on the actors to show who has yet to act"), the 2015-12-21 Holiday Cheer
    notes ("CLICK on torch meter at top of screen to quickly use a torch
    from inventory"; "actions remaining" tooltips on the health/stress bar
    tick mark; the corpses option; the Death's Door mortality-debuff option),
    the 2015-11-30 Inhuman Bondage notes (Death's Door at 0 HP, mortality
    debuffs, the heart attack at 200 stress, the D8 initiative experiment),
    the 2016-01-28 Build `13421` and 2017-06-20 hotfix notes (random
    targeting ignores corpses; units standing behind corpses), the
    2015-12-14 hotfix (surprise rolls saved and restored), the 2017-06-19
    Crimson Court base-game update (torchlight dodge bonus), the 2020-05-27
    `coming_in_hot` Build `25521` (Radiant Light dodge values; deathblow
    resistance rules), the 2016-12-14 Build `16628` (internal PROT cap), the
    2017-09-18 Build `20547` (monster stun-resist increment; battle
    turn-order saving), the 2018-07-16 Build `24121` and 2018-08-15 Build
    `24353` (move, stun and debuff resistances; heroes' deathblow resist),
    and the 2017-07-06 Build `20340` (Death's Door debuffs kept after
    restarting the game in a battle).
  - `P4` — [Red Hook's official site](https://www.darkestdungeon.com/), its
    [product page](https://www.darkestdungeon.com/darkest-dungeon/) and the
    [The Fire's Edge availability post](https://www.darkestdungeon.com/news/the-fire-s-edge-available-now-/),
    for platforms, the additive DLC statement and roster expansion; the site
    links no manual and its patch-notes page covers only Darkest Dungeon II
    consoles.
  - `P5` — [Red Hook support centre](https://redhookgames.zendesk.com/hc/en-us),
    read through its public API: thirteen articles across Darkest Dungeon
    PC, Mac, iPad, Butcher's Circus and Darkest Dungeon II sections; the PC
    [Save Locations](https://redhookgames.zendesk.com/hc/en-us/articles/115003306013-Save-Locations)
    article maps `Profile_0` to the first campaign slot; no manual, FAQ,
    difficulty, DLC or tutorial article exists.
  - `P6` — [Steam achievement list](https://steamcommunity.com/stats/262060/achievements/),
    for `Welcome home...` (Reach the Estate), `On the old road, we found
    redemption.` (Dismas and Reynauld), `Strict Mode` (default difficulty
    options) and `The first of many has fallen...`.
  - `P7` — [Steam store page](https://store.steampowered.com/app/262060/Darkest_Dungeon/),
    for the absence of a `View manual` link, the DLC list including The
    Fire's Edge, the official website and support links, and Red Hook's
    store description ("turn-based", "battle not only monsters, but stress",
    "the ever-encroaching dark", "character permadeath", resting
    shell-shocked characters in town to keep their stress in check).
- Corroborating textual sources, accessed 2026-09-08:
  - `S1` — [public SteamCMD info projection](https://api.steamcmd.net/v1/info/262060),
    for the `public` (`24960041`, 2026-08-27), `legacy` (`9545898`) and
    `coming_in_hot` (`25110930`) branches and the 64-bit depot; a secondary
    distribution mirror.
  - `S2` — [official Darkest Dungeon wiki](https://darkestdungeon.wiki.gg/),
    read as MediaWiki wikitext: Old Road, Game Modes, Locations, Combat
    Mechanics, Critical Hit, Corpse, Surprise, Retreating, Curios, Trap,
    Inventory, Provisions, Hunger, Scouting, Dungeon Map, Expeditions, Stress,
    Affliction, Virtue, Death's Door, Death, Move, Light Meter, Torch,
    Camping, Hamlet, Stage Coach, Heroes, Crusader, Highwayman, Brigand
    Cutthroat, Brigand Bloodletter, Brigand Fusilier, Quirks, Skeleton Key,
    Resolve Level, Glossary (the in-game options-menu glossary transcribed),
    The Ancestor (tutorial narration lines), Darkest Dungeon (the premise
    text "Progress autosaves constantly, so actions are permanent"), DLC,
    The Crimson Court, The Fire's Edge and The Butcher's Circus. Community
    text with strong rule-file references; never sole support for a product
    or build claim.
  - `S3` — [Darkest Dungeon Fandom wiki Old Road](https://darkestdungeon.fandom.com/wiki/Old_Road),
    read through its API; the same route text as `S2`, so counted as a
    mirror rather than an independent source.
  - `S4` — [Ludo guide for The Old Road](https://www.ludo.guide/guide/darkest-dungeon/the-old-road),
    a second static route (published May 2026) that records a first and a
    second enemy without naming them, gold after the first battle, an
    emerald, gold and a torch after the second, the tent and the 5,000 gold
    reward; it says trapped chests may hold food, which conflicts with `S2`
    and is not adopted, and its single-run torch drop after the final battle
    is random loot, not evidence of a carried torch inside the packet.
  - `S5` — dated Steam community threads:
    [Way to skip tutorial?](https://steamcommunity.com/app/262060/discussions/0/1369506834141932041/)
    (2017: not skippable),
    [Autosave – When is it safe to exit game?](https://steamcommunity.com/app/262060/discussions/0/412448158162783132/)
    (2016: saves on quit anywhere, no manual save) and
    [Accidentally enabled dlc](https://steamcommunity.com/app/262060/discussions/0/1621726179582758778/)
    (2018: DLC is enabled per save and cannot be disabled). No developer
    reply appears in any of them.
  - `S6` — [Wikipedia](https://en.wikipedia.org/wiki/Darkest_Dungeon), for
    release and platform history only.
- Evidence independence: sources are counted by family, not by page. Valve
  data (`P1`, `P2`, `P6`, `P7`, `S1`) is one family; Red Hook's
  announcements, site and support centre (`P3`–`P5`) are one family; the
  official wiki (`S2`) is one family and `S3` mirrors it; `S4`, `S5` and
  `S6` are separate families of lower reliability. `Corroborated` in the
  ledger means at least two families support the clause; a clause resting
  on `S2` alone is `Limited`, and the in-game Glossary transcribed by `S2`
  is not treated as an inspected shipped artefact.
- Negative searches, 2026-09-08: no official manual exists on Red Hook's
  product page, the store page (no `View manual`), the support centre or the
  Steam store category list; the console patch-notes page holds only Darkest
  Dungeon II entries; `darkestdungeon.com/press/` and the Crimson Court
  release-information page return `404`; the official X statement on DLC
  toggles is not retrievable; GameFAQs returned `402`, Fandom HTML `403` and
  the Steam update-history page renders no static content; the wiki has no
  Tutorial, Campaign or Save page, so the tutorial lock and autosave rest on
  the premise text, the support article and the dated threads.
- Reproducible control: `V1` repository-side transition trace across
  `P1`–`P7` and `S1`–`S6` under the declared application, package, branch,
  mode, option, DLC, entry, exclusions and reopened-profile terminal; rules
  reasoning, not direct play.
- Claim IDs: `DD-001`–`DD-027`; lettered sub-rows split composite claims so
  that each clause carries its own grade, and an unlettered reference means
  every sub-row of that claim. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: walk the two-hero party right along the corridor tiles
  and, optionally, back toward the entrance; `ACT-019`: on a hero's initiative
  turn choose one of its four equipped skills that is legal from its rank and
  a target in that skill's ranks; `ACT-199`: take loot from the post-battle or
  curio window into the sixteen-slot inventory or leave it; `ACT-341`:
  investigate the Brigand's Tent by hand, or ignore it, and ignore the
  Bandit's Trapped Chest.
- New `ACT-449`: snuff the torch by 25 or fully at any time outside a
  resolving action; the ordinary route recommends but never instructs it,
  and refuelling by a carried torch is outside the packet because no torch
  is evidenced in the inventory (`DD-017e`). New `ACT-450`: spend a hero's turn to shift it along the
  formation, the ordinary reply to a knockback that has left its skills
  illegal.
- Rejected `ACT-096`: the destination room is the only room, and the corridor
  must still be walked, so no route is delegated to the system. Rejected
  `ACT-067`: repositioning is a turn-costing move command with declared
  ranges, not walking into an adjacent unit. Rejected `ACT-125`, `ACT-126`
  and `ACT-061`: there is no hand, energy or phase to end. Rejected
  `ACT-131` and item use: no source records any item in the Old Road
  inventory, no provisioning stage precedes the route, and the one torch a
  static guide lists is random loot after the last battle, so item use,
  including torch refuelling, has insufficient evidence and is excluded.
  Rejected `ACT-409`: the torch changes a shared meter, not a personal light
  field.
- Passing the turn, which costs 5 stress, is available every turn but never
  forced because Tracking Shot and Open Vein are legal from rank 1 and Smite
  from rank 2; it is a parameter of `ACT-019`. Destination selection on the
  two-room map, hero names, skill names, move ranges and the choice of which
  hero investigates a curio are parameters. Claims: `DD-007`–`DD-011`,
  `DD-017`, `DD-022`.

### System Behaviour Genes

- Existing `SYS-004`: the tent's loot table and each loot window draw from
  weighted outcome tables; `SYS-362`: each cleared battle opens a loot window
  and the completed quest pays 5,000 gold, converts loot and grants 2 resolve
  experience at the debrief; generalised `SYS-388` (`TAXONOMY_CHANGE_041`):
  every round re-rolls speed plus a hidden 1–8 for each unit, orders them
  with heroes winning ties, and activates one unit for one action at a time;
  `SYS-538`: damage updates hero health and death state, survivors return to
  the Hamlet at full health and a killed hero is permanently absent from the
  roster.
- New `SYS-825`: a committed skill rolls accuracy minus dodge, samples damage
  reduced by protection, rolls its critical and tests stun, bleed, blight,
  knockback or debuff against resistances, after which bleed ticks each round
  and each corridor step; `SYS-826`: each brigand's turn draws a rank-legal
  skill by its declared weights and applies its targeting rule; `SYS-827`: an
  ordinary kill leaves a corpse that keeps the enemy's ranks until destroyed
  or decayed, so the Fusilier stays in rank 3 behind the Bloodletter's
  size-two corpse; `SYS-828`: each battle opens with a two-sided surprise
  check modified by the light band, which at Radiant light cannot surprise
  the party; `SYS-829`: the shared light meter decays with travel and its
  band scales stress, dodge, surprise, hostile accuracy, damage and criticals
  and extra loot; `SYS-830`: each hero's stress rises from Bloodletter whips,
  received criticals and occasional travel events, falls from own kills and
  criticals, and is carried into the Hamlet capped at 100 while health is
  restored; `SYS-831`:
  a hero at zero health remains active with penalties and each further hit
  rolls a deathblow that can kill permanently.
- Branch scope, stated for every conditional rule: damage, bleed, knockback,
  Death's Door and death are outcome branches of the brigands' hit rolls and
  no representation of the route commands them; the resolve test at 100
  stress and the heart attack at 200 are parameters of `SYS-830` because two
  short fights at Radiant light do not ordinarily reach them; Reynauld's
  Kleptomaniac forced interaction is recorded as an insufficiently evidenced
  parameter of `ACT-341` because the quirk table lists Treasure curios while
  the tent is typed Scrounging.
- Rejected `SYS-356`: the upcoming order is never exposed. Rejected `SYS-164`
  and `SYS-537`: no intent is telegraphed and no separate enemy phase exists.
  Rejected `SYS-389` and `SYS-208`: no armour class, saving throw, cover or
  body-part resolution. Rejected `SYS-390`: a Death's Door hero keeps acting
  and rolls per hit, not per turn while downed. Rejected `SYS-820`: no
  restorative stock suspends the blow. Rejected `SYS-355`: surprise is a
  random check, not a player-initiated field strike. Rejected `SYS-190`,
  `SYS-198`, `SYS-338` and `SYS-592`: stress is event-driven and per hero,
  not a need or morale drift. Rejected `SYS-020`: knockback is resisted and
  resolves no collision. Rejected `ACT-453`, `SYS-593`, `SYS-754`, `SYS-791`,
  `SYS-851` and `SYS-797`: the light is a shared expedition meter, not a local
  field or a portable device refilled from carried stock.
  Rejected `SYS-167` and `CON-175`: health is restored at the debrief, so
  no run health persists; stress persists instead under `SYS-830`.
- Resolution order: enter a tile (deterministic light decay, a possible
  travel-stress event, contents revealed); surprise check; each round: initiative roll, then per unit —
  hero input or brigand weighted choice — hit, damage, critical, status; bleed
  ticks at turn start; corpse creation and decay; loot window; curio outcome;
  quest completion prompt; debrief conversion, reward, experience, health
  restore and stress cap; Hamlet arrival; autosave. Claims: `DD-009`–`DD-025`.

### Constraint Genes

- Existing `CON-001`: two opposed ordered lines of four addressable ranks that
  heroes, brigands and corpses occupy for the battle; `CON-210`: a pickup
  needs a free slot or a compatible typed stack among sixteen slots.
- New `CON-622`: a skill is legal only from its launch ranks and only against
  its target ranks, so Dismas pushed to rank 1 loses Pistol Shot and
  Grapeshot Blast while Tracking Shot and Open Vein remain, and the Fusilier
  is reachable only by skills that target rank 3 while the Bloodletter or its
  corpse holds ranks 1–2.
- Rejected `CON-269`: no resource, cooldown or readiness gate exists and the
  binding predicate is the actor's own slot. Rejected `CON-182` and
  `CON-011`: ranks are a line, not paired lanes or exclusive grid cells.
  Rejected `CON-343`, `CON-094`, `CON-174` and `CON-455`: one action per unit
  is a parameter of `SYS-388`, not a resource economy. Rejected `CON-177`:
  the inventory is a general sixteen-slot store. Rejected `CON-203`: no
  affliction is ordinarily reached.
- Scarce strategic resources: each hero's health, stress and single action
  per round, the light meter, rank-legal skills, free inventory slots and
  the roster itself. The four equipped skills per hero, formation length,
  corpse decay rounds, stack limits and the tutorial lock on retreat and
  abandonment are parameters. Claims: `DD-008`, `DD-011`, `DD-014`,
  `DD-015`, `DD-022`.

### Information Genes

- Existing `INF-002`: the round's initiative roll and each brigand's skill
  choice are not previewed; `INF-003`: the corridor's battle and curio tiles
  exist at generation but are exposed only on entry or by a scouting roll,
  which is the reveal parameter; `INF-119`: each hero's health, stress,
  stats, resistances, status icons and equipped skills with their accuracy,
  damage and critical values are inspectable; `INF-128`: the loot window and
  inventory show item identity, stacks and free slots before a pickup.
- New `INF-332`: the torch meter at the top of the screen shows the shared
  light value, its band and the band's effect icons throughout the
  expedition, read before each step and before any snuff. New `INF-333`:
  every hero and brigand carries a gold pip that shows it has yet to act
  this round and clears as it acts, while the order among the remaining
  units stays hidden.
- Split-first audit of the former compound HUD gene: the light display
  (producer `SYS-829`, updated per segment and per snuff, present in
  corridors with no combat), the remaining-action pips (producer `SYS-388`,
  updated per unit action, present only in combat), hero health, stress and
  status (producer `SYS-825`/`SYS-830`, already `INF-119`) and hostile
  statistics vary independently and support different decisions, so no
  conjunctive gene is kept. Enemy health bars are the ordinary presentation
  baseline the corpus does not isolate, and inspection of a brigand's dodge,
  protection, speed and resistances is excluded for insufficient evidence
  because no source documents such a tooltip.
- Rejected `INF-141` and `INF-061`: no queue and no intent are exposed; the
  pips disclose the set of units yet to act, never their sequence. Rejected
  `INF-327`: the light meter shows its exact value and is player-depletable,
  whereas the escalation tier withholds its value. Rejected `INF-212` and
  `INF-183`: those resource counts carry no modifier band. Rejected
  `INF-316` and `INF-240`: the light is a shared expedition meter, not a
  personal visibility or darkness indicator. Rejected `INF-220` and
  `INF-190`: they expose the selected unit's own action budget and forecast,
  not every unit's remaining action. Rejected `INF-062`: room categories are
  not shown before entry. Rejected `INF-221`: no cover or concealment is
  documented; the accuracy value is shown on the skill. Rejected `INF-125`:
  the two-room map carries no mission gates beyond the one corridor.
  Rejected `INF-075`: stress and health are hero panels under `INF-119`, not
  survival meters with tool wear.
- Claims: `DD-011`–`DD-013`, `DD-016`, `DD-017c`–`DD-017f`, `DD-022`.

### Objective Genes

- Existing `OBJ-029`: each of the two authored battles is completed by
  incapacitating its finite hostile set — the single Cutthroat, then the
  Bloodletter and Fusilier — before both heroes are lost; the quest completes
  when the second set is cleared. The Old Road adds no objective beyond
  these two encounters, because arrival at the Hamlet follows every outcome,
  including a wipe, and is therefore the retained successor rather than a
  pursued state.
- Rejected `OBJ-166`: its completion requires the hostile set to be removed,
  yet the Hamlet is reached even when the party is wiped, so it would
  overstate the settlement condition; the retained successor is the debrief
  settlement of `SYS-538`, `SYS-362`, `SYS-830` and `TIM-021`. Rejected
  `OBJ-026`: the Hamlet is not navigated to but entered through a prompt.
  Rejected `OBJ-113`: no captivity, disaster survival or open-world control
  gate exists, and the Old Road cannot be failed. Rejected `OBJ-055`,
  `OBJ-100` and `OBJ-156`: no multi-act boss climb, sabotage fixture or
  terminal health loss.
- Success, evaluation and failure: success is both sets cleared and the
  Hamlet state retained by the documented autosave; a lost battle is a failed `OBJ-029`
  whose documented settlement still enters the Hamlet; there is no retry.
  Claims: `DD-009`, `DD-020`, `DD-023`–`DD-025`.

### Time Genes

- Existing `TIM-001`: one committed skill, shift or pass input per hero turn
  is followed by automatic resolution and by the brigands' interleaved turns
  until the next hero input; corridor walking is self-paced.
- New `TIM-021`: the campaign autosaves into one profile with no manual
  save or load of an earlier state, so the tutorial's losses, stress and
  deaths persist; Red Hook's notes and the community thread document the
  reopened profile resuming the retained state, and the exact save moments,
  including the quit-save reported by the thread, are parameters.
- Rejected `TIM-005`: no player phase precedes a committed hostile phase;
  units interleave by initiative. Rejected `TIM-004`: the order is not a
  fixed alternation. Rejected `TIM-007`: no earlier state can be restored.
  Claims: `DD-012`, `DD-025`.

## Reproducible transitions

Row classes: **A** always executed on the ordinary route; **C** conditional on
an ordinary enemy hit roll or player option; **F** failure boundary; **V**
documented verification path for the retained successor, recorded from the
sources and not executed in this analysis.

| Class | Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|---|
| A | Fresh profile at the main menu | New Campaign → estate name → `Darkest` → no DLC toggle → default options | Two cinematics play and control begins in the Old Road entrance room with Reynauld in rank 1, Dismas in rank 2, no trinkets, light 100 and the two-room map revealed | reproducible entry, mode and DLC boundary | `DD-001`, `DD-003`, `DD-005`–`DD-008` |
| A | The party stands in the entrance room | Walk right along the corridor, reading the torch meter | Each new segment deterministically lowers the light by six; travel may, not must, add a light-scaled stress event on any segment; a tile's battle or curio is exposed on entry; walking back adds extra stress | deterministic light decay beside a probabilistic travel-stress event, under concealed contents | `DD-008a`, `DD-017a`, `DD-017b`, `DD-017f`, `DD-018a` |
| A | The Cutthroat tile is entered | None; the battle begins | A surprise check rolls with the party's chance at zero under Radiant light and the monster's chance raised; the round's order is rolled as speed plus a hidden 1–8; each unit shows a gold remaining-action pip | two-sided surprise, hidden initiative and disclosed remaining actions | `DD-012a`–`DD-012c`, `DD-016a`, `DD-016b` |
| A | It is Reynauld's turn in rank 1 | Choose Smite, Stunning Blow or Zealous Accusation against rank 1, or Bulwark of Faith, or shift, or pass | Only skills legal from rank 1 and against the Cutthroat's rank are offered; a chosen skill resolves accuracy minus dodge with the hidden +5, damage reduced by 15% protection, a critical roll and, for Stunning Blow, a 100% stun against 25% resistance | rank legality feeding the hit, protection, critical and resistance pipeline | `DD-011`, `DD-013`, `DD-014` |
| A | It is the Cutthroat's turn | None | One of Slice and Dice, Uppercut Slice and Shank is drawn with equal chance and targets by its rule; a hit may apply a bleed-resistance debuff, a knockback or a bleed against 30% resistance | weighted hidden hostile selection | `DD-014`, `DD-021` |
| C | Uppercut Slice has knocked Reynauld back to rank 2, putting Dismas in rank 1 | Shift Dismas back or use Tracking Shot or Open Vein from rank 1 | A shift spends the turn and restores Pistol Shot; the alternative keeps the turn with the rank-1-legal skills | the formation trade-off after displacement | `DD-011`, `DD-014` |
| C | A bleed has been applied | None | Two points tick at each of the hero's turn starts and at each corridor step for the declared rounds | damage over time outside the hit | `DD-014` |
| A | The Cutthroat reaches zero health from a non-critical hit | None | A corpse holds rank 1 with grey health and no turns until destroyed or four rounds pass; a critical or bleed kill leaves none; the battle ends with no living enemy | corpse creation and battle end | `DD-015`, `DD-009` |
| A | The battle has ended | Take or leave each loot item | Items enter free slots or compatible stacks of the sixteen; low light would have added draws; a kill rolls a 50% chance of 3 stress relief for the killer | slot-bounded loot and stress relief | `DD-018`, `DD-022` |
| C | The Brigand's Tent is reached | Investigate by hand with either hero, or ignore | Two loot draws resolve from the tent's table; ignoring changes nothing | optional curio with random yield | `DD-010` |
| C | The player decides on the torch, reading the meter and its band | Snuff by 25 or fully, or leave it | The band changes at once: lower light raises loot chances, stress, hostile accuracy, damage and criticals and lets the party be surprised; no refuel is available because no torch is evidenced in the inventory | the light trade-off as an ordinary option | `DD-016b`, `DD-017c`, `DD-017d`, `DD-017f` |
| A | The battle room is entered | None; the second battle begins | The Bloodletter occupies ranks 1–2 and the Fusilier rank 3; the same surprise and initiative rolls apply; Point Blank Shot is legal only from rank 1 and Blanket Fire only from ranks 2–4 | multi-rank enemy and rank-bound hostile skills | `DD-009`, `DD-011`, `DD-021` |
| C | Point Blank Shot or Rain of Whips has hit | None | Knockback rolls against move resistance, bleed against bleed resistance, +5 stress on whip hits, +10 stress and a 50% party 5 on any received critical | stress and displacement as outcomes of enemy rolls | `DD-014`, `DD-018` |
| C | The Bloodletter dies by ordinary damage | Target the corpse, or the Fusilier through rank-3 skills | The size-two corpse keeps the Fusilier in rank 3 until it is destroyed or decays, after which the Fusilier moves to rank 1 and can only use Rushed Shot | corpse geometry deciding target legality | `DD-011`, `DD-015`, `DD-021` |
| C | A hero's health reaches zero | Continue with rank-legal skills, shift or pass | The hero stays active at Death's Door with −10 ACC, −25% DMG, −5 SPD and +33% stress; each further hit rolls the 33% deathblow; no heal is equipped | Death's Door as the reached failure boundary | `DD-019` |
| F | A deathblow roll fails | None | The hero dies permanently and leaves the roster; the other hero fights on, and a wipe still settles into the Hamlet with the reward | permanent loss without a game over | `DD-020` |
| A | Both enemies are dead | Accept the prompt and leave for the Hamlet, without opening the chest | The debrief converts loot to gold, pays 5,000 gold and 2 resolve experience so both survivors reach level 1, restores health, caps stress at 100 and keeps any affliction | settlement into the retained roster | `DD-023` |
| A | The debrief is accepted | None | The campaign enters the Hamlet at Week 1 with the `Welcome home...` narration, the survivors, replacements for the dead in the Stage Coach beside a Plague Doctor and a Vestal, and the state autosaved | the first retained Hamlet state | `DD-024`, `DD-025a` |
| V | The Hamlet is shown | Documented path, not executed here: quit to the desktop, relaunch, select the same profile | The sources state that the reopened profile resumes the retained state and that no earlier state can be loaded; a reproducing analyst would compare the week, roster, gold and stress, and no returned value is claimed as observed | documented persistence of the settled arrival | `DD-025a`–`DD-025c` |

## Strategic and experiential structure

- Planning horizon: bring both heroes through two fights with as little
  stress as possible, because health is restored at the Hamlet but stress
  is not, and decide whether extra loot from a snuffed torch is worth the
  stress and risk.
- Local tactics: kill the Cutthroat before its Shank bleeds; choose a stun
  attempt against 25% resistance or a full Smite; keep Dismas in rank 2 so
  Pistol Shot and Grapeshot Blast stay legal, or accept a shift; focus the
  Bloodletter, whose Point Blank Shot from rank 1 can knock the front hero
  back; clear or wait out its corpse to reach the Fusilier; ignore the
  trapped chest.
- Medium-term structure: the corridor teaches travel, light and one duel;
  the room teaches multi-rank enemies, corpses and rank-bound hostile
  skills; the debrief teaches that stress, not health, is what the campaign
  keeps.
- Reversible versus irreversible: skill and shift choices are revisable each
  turn. Three state layers must be kept apart: damage, bleed and other
  status effects are temporary expedition values; the debrief transforms or
  clears a second layer, restoring survivor health and converting loot into
  settled gold beside the reward; only the resulting campaign state — each
  hero's retained stress, a death or Stage Coach replacement and the settled
  gold — is the retained result, and autosave-only persistence means that
  result cannot be rolled back through a load menu, not that every
  intermediate value survives unchanged.
- Failure attribution: the skill accuracy, the enemy health bars, the
  remaining-action pips, the light band, the health and stress bars and the
  Death's Door icon separate rank, roll, light, stress and survival
  failures; the hidden
  initiative and hostile choice remain the acknowledged variance.
- Player trust: an illegal skill must be greyed from a wrong rank, a
  displayed 95 accuracy must hit, a corpse must block its ranks, the torch
  band must change the loot and stress rules, and the documented autosave
  must leave no earlier state to load. Claims: `DD-011`–`DD-025`.

## Replay and variation

- What changes between campaigns: rolls for initiative, hits, criticals,
  stuns, bleeds and knockbacks; the brigands' skill draws; loot identities;
  whether the tent is investigated; whether the torch is snuffed; damage,
  stress, Death's Door and deaths at the debrief.
- Randomness or procedural generation: the two rooms, the corridor, both
  encounters, the tent and the chest are authored; every combat outcome and
  loot draw is sampled.
- Multiple viable strategies: stun-and-strike, straight damage or a bleed
  build on the Bloodletter, and full or snuffed light all reach the same
  Hamlet; the control fixes no stun, snuff or curio choice.
- Typical replay motive: arrive with both heroes alive and low stress, or
  farm the loot bonus of darkness; later campaign strategy is outside this
  packet. Claims: `DD-009`–`DD-023`.

## Adjacent systems and history

- Direct product corridor: Darkest Dungeon II moves the roster into a
  road-trip run and exposes a visible turn order, so it requires its own
  scope; the 2026 The Fire's Edge DLC adds two of its heroes to this game
  without changing the Old Road.
- Same-corpus corridors: Slay the Spire shares only random outcome
  selection, unpreviewed and concealed information and the finite hostile
  set, because its combat is a planning phase with telegraphed intents,
  shared energy and block rather than interleaved initiative, ranks and
  resistances; XCOM 2 shares the ability-and-target command, random
  selection, fixed occupancy, the finite hostile set and the settlement of
  survivors and permanent losses, but spends Action Points in a squad phase,
  resolves cover and reaction fire, and returns survivors into wound recovery
  rather than restoring health and keeping stress;
  Baldur's Gate 3 shares the generalised initiative scheduling, the
  ability-and-target command and the character panel, but rolls once per
  combat against armour classes and downs rather than holds a zero-health
  member; Clair Obscur: Expedition 33 shares encounter rewards and the
  character panel but exposes its queue; World of Warcraft, the
  mathematically selected neighbour, shares only the traversal, loot,
  interaction, panel and reward substrate of a tutorial route.
- Important differences: this packet's whole pressure is rank legality
  under hidden per-round initiative, resistance-tested status effects,
  corpses, the light trade-off, stress that survives the expedition and
  Death's Door as the only failure boundary; the debrief restores survivor
  health and converts loot, and only the settled campaign result that
  follows — retained stress, roster death or replacement and gold — is
  fixed by autosave-only persistence with no reloadable earlier state.
  Claims: `DD-011`–`DD-025`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-019`, `ACT-199`, `ACT-341`, `ACT-449`, `ACT-450` | hero, skill, curio, room and item names; move ranges; pass cost |
| System Behaviour | `SYS-004`, `SYS-362`, `SYS-388`, `SYS-538`, `SYS-825`, `SYS-826`, `SYS-827`, `SYS-828`, `SYS-829`, `SYS-830`, `SYS-831` | roll ranges, damage, resistances, decay rates, band thresholds, stress amounts, deathblow resistance, reward values |
| Constraint | `CON-001`, `CON-210`, `CON-622` | four ranks per side, sixteen slots, stack limits, launch and target ranks |
| Information | `INF-002`, `INF-003`, `INF-119`, `INF-128`, `INF-332`, `INF-333` | tooltip depth, scouting chance, band icons, pip form, hidden modifiers |
| Objective | `OBJ-029` | enemy sets, quest completion prompt, reward |
| Time | `TIM-001`, `TIM-021` | rounds, interleaving, profile slots, quit-save behaviour |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `280` (`GAME-0001`–`GAME-0280`).
- Exact genome matches: none.
- Tied near matches: `GAME-0221` — World of Warcraft (`6 / 48 = 0.125000`).
- Supported combination subsets: none.
- Scan date: 2026-09-08.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0221` — World of Warcraft | `ACT-008`, `ACT-199`, `ACT-341`, `SYS-362`, `INF-119`, `INF-128` | Both are tutorial routes in which a directly walked party collects loot into a bounded inventory, interacts with authored objects, reads a character panel with health, resources and abilities, and receives encounter rewards before a retained successor. World of Warcraft resolves its Exile's Reach lessons in real-time targeted combat with learned abilities, quest hand-ins and levels on a persistent shared realm, and keeps a reloadable client state. Darkest Dungeon instead fights two authored brigand groups in rank-legal turn combat under hidden per-round initiative, resistance-tested status effects and corpses, trades a shared light meter against stress and loot, carries per-hero stress rather than health into the Hamlet, holds a zero-health hero at Death's Door and, after a debrief that restores survivor health and converts loot, fixes only the settled campaign result — retained stress, roster death or replacement and gold — through autosave-only persistence with no reloadable earlier state. | Near, `0.125000` |

### Preserved research notes

- New genes: `ACT-449`, `ACT-450`, `SYS-825`, `SYS-826`, `SYS-827`,
  `SYS-828`, `SYS-829`, `SYS-830`, `SYS-831`, `CON-622`, `INF-332`,
  `INF-333` and `TIM-021`.
- Reused genes: `ACT-008`, `ACT-019`, `ACT-199`, `ACT-341`, `SYS-004`,
  `SYS-362`, `SYS-388`, `SYS-538`, `CON-001`, `CON-210`, `INF-002`,
  `INF-003`, `INF-119`, `INF-128`, `OBJ-029` and `TIM-001`.
- Classification result: `New gene`.
- Evidence and reasoning: sixteen boundaries transfer from the reviewed
  corpus, one of them after a wording generalisation that makes the
  initiative re-roll cadence and resource names parameters. The corpus had
  no formation-rank legality, no hidden-initiative hostile policy, no
  subtractive hit and resistance pipeline, no corpse obstacle, no surprise
  check, no shared light meter, no event-driven carried stress, no
  active Death's Door state, no visible shared-meter band, no per-unit
  remaining-action disclosure and no autosave-only persistence structure,
  so thirteen genes are new; each is portable to other formation, roguelike
  and expedition rulesets and none is named after a hero, enemy, room or
  reward. The grades follow the evidence-independence matrix: genes whose
  boundary rests on the official wiki alone are `Limited`, and those with
  publisher or store corroboration are `Corroborated`.

## Taxonomy impact

- Registry changes: thirteen new Active genes listed above; `SYS-388`
  generalised by
  [`TAXONOMY_CHANGE_041`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_041.md)
  so initiative may be re-rolled each round with parameterised resources;
  fifteen further Active genes gain this game as an additional carrier. No
  lifecycle, ID or earlier reviewed signature changes.
- Taxonomy-change record: `TAXONOMY_CHANGE_041`.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; Reynauld,
  Dismas, the Ancestor, the Hamlet, the Old Road, every brigand and skill
  name, the tent, the chest, the Stage Coach, `Darkest`, `Radiant`,
  `Stygian`, `Bloodmoon`, `Darkest Dungeon Config`, `Profile_0` and every
  application, package, build and achievement identifier remain parameters
  or literal product terms.

## Negative results

- No direct-play, entitlement, screenshot, video or audio claim.
- No hunger, camping, trap, scouting decision, retreat, abandonment,
  reinforcement, affliction, virtue, heart attack, item use, quirk gain,
  trinket, town, DLC, mode, mod, console or sequel mechanic is imported.
- `ACT-096`, `ACT-067`, `ACT-125`, `ACT-126`, `ACT-061`, `ACT-131`,
  `ACT-409`, `SYS-356`, `SYS-164`, `SYS-537`, `SYS-389`, `SYS-208`,
  `SYS-390`, `SYS-820`, `SYS-355`, `SYS-190`, `SYS-198`, `SYS-338`,
  `SYS-592`, `SYS-020`, `SYS-593`, `SYS-754`, `SYS-791`, `SYS-851`, `SYS-797`,
  `SYS-167`, `CON-175`, `CON-269`, `CON-182`, `CON-011`, `CON-343`,
  `CON-094`, `CON-174`, `CON-455`, `CON-177`, `CON-203`, `INF-141`,
  `INF-061`, `INF-062`, `INF-220`, `INF-221`, `INF-125`, `INF-075`,
  `INF-327`, `INF-212`, `INF-183`, `INF-316`, `INF-240`, `INF-190`,
  `OBJ-166`, `OBJ-026`, `OBJ-113`, `OBJ-055`, `OBJ-100`, `OBJ-156`,
  `TIM-005`, `TIM-004` and `TIM-007` are rejected with the smallest
  counterexamples recorded above.
- No compound HUD gene is retained: the former `INF-332` was split into the
  visible light meter and the remaining-action pips, hero panels stay under
  `INF-119`, enemy health bars are baseline presentation, and inspectable
  enemy statistics are excluded for insufficient evidence.
- No torch refuelling is admitted, because no source establishes a carried
  torch at entry or before the last battle; no reload verification is
  claimed as executed.
- No hit, snuff, detour or resource spend is instructed to make a gene
  legal; damage, bleed, knockback, Death's Door and death are admitted only
  as outcome branches that the brigands' own rolls produce, and the light
  action is an option the route never commands.
- A separate forced-interaction gene for Reynauld's Kleptomaniac is not
  created because the curio typing evidence conflicts.

## Delta summary

## New facts

- [Confirmed | Direct | High] Current base-package Windows availability and
  the seven DLC or music applications are fixed in `DD-001`.
- [Observation | Corroborated | High] The current branch, the per-campaign
  DLC boundary, the additive 2026 DLC, the `Darkest` default, the option
  defaults, the mandatory Old Road, per-round hidden initiative with
  remaining-action pips, corpse occupancy, the surprise check, the light
  band's effects and display, Death's Door with its deathblow roll,
  permadeath and the first Hamlet state are bounded in `DD-002`–`DD-007`,
  `DD-011b`, `DD-012a`, `DD-012c`, `DD-015a`, `DD-016a`, `DD-017c`,
  `DD-017f`, `DD-018a`, `DD-019a`, `DD-020a` and `DD-024`.
- [Observation | Corroborated | Medium] The two required battles, the loot
  window, the debrief reward, stress carried past the expedition, the
  light meter's depletion, resisted status effects and autosave-only
  persistence are bounded in `DD-009b`, `DD-013c`, `DD-014a`, `DD-014b`,
  `DD-017a`, `DD-018c`, `DD-020b`, `DD-022a`, `DD-023a`, `DD-025a` and
  `DD-025b`.
- [Observation | Limited | Medium] The Old Road layout and retreat lock,
  rank legality, the exact initiative die and tie rule, the hit formula
  and its constants, bleed timing, corpse decay, the surprise and light
  values, the snuff command, the exact stress amounts, the Death's Door
  penalties, the brigands' selection weights, the inventory bounds and the
  debrief experience rest on the official wiki alone (`DD-008a`, `DD-008c`,
  `DD-009a`, `DD-010a`, `DD-011a`, `DD-012b`, `DD-013a`, `DD-013b`,
  `DD-014c`, `DD-015b`, `DD-016b`, `DD-017b`, `DD-017d`, `DD-018b`,
  `DD-019b`, `DD-021`, `DD-022b`, `DD-023b`, `DD-026`, `DD-027`) or on one
  community thread (`DD-025c`); `DD-010b` is `Conflicting`.

## New genes

- [Observation | Corroborated | High] `SYS-831`, `INF-332` and `INF-333`
  isolate Death's Door, the visible shared light meter and the per-unit
  remaining-action pips with publisher and wiki support.
- [Observation | Corroborated | Medium] `SYS-827`, `SYS-828`, `SYS-829`,
  `SYS-830` and `TIM-021` isolate the corpse obstacle, the surprise check,
  the shared light meter, carried stress and autosave-only persistence;
  their core clauses are corroborated while their exact values rest on the
  wiki.
- [Observation | Limited | Medium] `ACT-449`, `ACT-450`, `SYS-825`,
  `SYS-826` and `CON-622` isolate the snuff command, the formation shift,
  the hit-and-resistance pipeline, the hidden hostile policy and rank
  legality on the official wiki alone.

## New combinations

- [Observation | Corroborated | High] `No new combinations`; none of the 271
  verified sets is a strict subset of this signature, and the nearest miss
  (`COMB-0049`) lacks `INF-004`.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_041` generalises
  `SYS-388`; no prior signature, lifecycle or ID changes.

## New questions

- Does Dead Cells' first Prisoners' Quarters traversal keep the same
  autosave-and-loss structure as `TIM-021` while replacing turn order with
  real-time timed combat?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0282` — Dead Cells, only under a new
  game-specific prompt after this unit's independent audit.
- Optimisation criterion: replace formation-rank turn combat with real-time
  generated-route combat while keeping a retained successor terminal.
- Expected information gain: separate generated biome routing, timed
  combat and death reset from the initiative, stress and autosave boundaries
  above.
- Backlog impact: advances the recorded 280-to-288 calibration horizon.

## Why this game

- [Hypothesis | Limited | High] The transfer test had to succeed on a
  turn-based, roster-carrying packet with no shared substrate, so success
  could not come from reusing the previous record's shape.
