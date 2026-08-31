---
game_id: GAME-0190
slug: the-elder-scrolls-v-skyrim-special-edition
game_title: "The Elder Scrolls V: Skyrim Special Edition"
analysis_status: reviewed
reviewed: 2026-08-29
combination_ids:
  - COMB-0188
gene_ids:
  action:
    - ACT-008
    - ACT-131
    - ACT-161
    - ACT-190
    - ACT-199
    - ACT-202
    - ACT-343
    - ACT-344
  system:
    - SYS-215
    - SYS-342
    - SYS-373
    - SYS-379
    - SYS-612
    - SYS-613
  constraint:
    - CON-188
    - CON-269
    - CON-282
    - CON-508
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-243
  objective:
    - OBJ-113
  time:
    - TIM-003
    - TIM-007
---

# Game: The Elder Scrolls V: Skyrim Special Edition

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodded Windows Steam **The Elder Scrolls V:
  Skyrim Special Edition**, official Update `1.7.99` plus its 2026-08-27
  hotfix, Steam public build `24914197`, checked 2026-08-29; default Adept
  difficulty and one fresh base-game `Unbound` (`MQ101`) route through Hadvar.
- Content boundary: load `Skyrim.esm` and the Special Edition's ordinary
  official masters, but do not enter Dawnguard, Hearthfire or Dragonborn
  systems. Disable downloaded Creations and mods and do not claim Anniversary
  Upgrade content. The four bundled free Creation files may remain installed
  as current product files but none is activated by or causal to Helgen.
- Reproducible character and route: confirm one Nord with a declared name and
  otherwise default presentation; retain the default difficulty; choose Hadvar
  at the two-door fork; take and equip the ordinary chest gear; use sword and
  Flames in the required fights; ignite the oil patch; drink one found healing
  potion after damage; open exactly one novice prison cell with a lockpick;
  lower the bridge by its lever; clear the frostbite spiders; crouch and sneak
  past the sleeping bear; follow Hadvar through the cave exit.
- Primary decision loop: read the current objective marker, local sight/sound,
  health, magicka, stamina and equipment; move or crouch through the authored
  route; choose weapon, spell, potion, loot, lock or fixture interaction;
  resolve live hostile perception and combat; retain equipment, skill and quest
  changes; then advance Hadvar's next required gate toward the exterior.
- Entry and exit: begins when `New Game` commits the prisoner-cart sequence;
  the first player-authored state is Nord confirmation at the mandatory Helgen
  character gate. It succeeds only when the Hadvar cave exit completes
  `Unbound`, activates `Before the Storm` and leaves the same character under
  first retained controllable exterior-world state. Reaching the keep, killing
  the bear or seeing daylight before quest settlement is not the terminal.
- Included: cart/execution scripting; character confirmation; direct walking,
  running, jumping and crouching; local quest compass and objective markers;
  the exclusive Hadvar/Ralof fork with Hadvar fixed for reproduction; ordinary
  Hadvar-route gear, inventory, carry state and equipment; one-handed combat,
  blocking only where the equipped route item permits it, bow use if acquired,
  Flames and Healing, health/magicka/stamina, one healing potion, hostile sight
  and sound, skill-use progress, one novice lock, oil ignition, keys, lever,
  bridge and collapse, spiders, the sleeping bear, quest flags, autosave/manual
  save and reload before the terminal.
- Excluded: following Ralof in the canonical trace; Riverwood and every later
  quest; free-form province exploration; levelling after the cave, perk trees,
  smithing, enchanting, alchemy, shouts, dragons as ordinary combatants,
  followers beyond Hadvar, factions, crime, marriage, houses, radiant quests,
  Dawnguard, Hearthfire, Dragonborn, Survival Mode, Fishing, Saints & Seducers,
  Rare Curios, Anniversary Upgrade, Creation Club/Creations, mods, console
  commands, exploits, achievements and the product's update history.
- Potential scoped modules: the Ralof fork, one separately bounded later main
  quest, one base-game dungeon, one faction branch, one declared official add-on
  or one current Creation only after its own version and terminal are fixed.
- Direct-play status: no authenticated Windows Steam fresh start was conducted.
  Official product/update/support material fixes the current executable and
  content boundary; Bethesda's official manual fixes the enduring controls and
  mechanics; maintained route references supply the reproducible `MQ101`
  transitions. Repository transitions are rules reasoning, not direct play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SKYRIM-001` | The current Windows Steam product remains The Elder Scrolls V: Skyrim Special Edition at official Update 1.7.99 with the 2026-08-27 hotfix and public build 24914197 | Confirmed | Corroborated | High | P1, P2, P3, S1 |
| `SKYRIM-002` | Special Edition, Anniversary Upgrade and optional Creations are separable content boundaries, so a clean Helgen base-game route can exclude them | Confirmed | Direct | High | P1, P3 |
| `SKYRIM-003` | New Game requires character confirmation, and the selected ancestry persists mechanical starting traits while appearance and name identify the save | Observation | Corroborated | High | P4, S2 |
| `SKYRIM-004` | `Unbound` is the opening tutorial quest, branches through Hadvar or Ralof and completes at the exterior cave exit before `Before the Storm` | Observation | Corroborated | High | S2, S3 |
| `SKYRIM-005` | The Hadvar route teaches loot/equipment, direct weapon/spell combat, potions, authored fixture gates and the cave exit | Observation | Corroborated | High | P4, S2, S3 |
| `SKYRIM-006` | Health, magicka and stamina constrain current combat and spell decisions while the HUD, compass, inventory and quest journal expose their decision state | Confirmed | Direct | High | P4 |
| `SKYRIM-007` | Crouching changes detection, and the declared bear can be passed without combat when the character remains outside its detection result | Observation | Corroborated | High | P4, S2, S3 |
| `SKYRIM-008` | One novice prison lock maps pick angle and torque to graded resistance, pick breakage or persistent access | Observation | Corroborated | High | P4, S2, S3 |
| `SKYRIM-009` | Performing admitted combat, spell, sneak and lock actions can advance their matching skill progress without requiring a post-cave level allocation | Confirmed | Direct | High | P4 |
| `SKYRIM-010` | Manual and automatic saves can restore an earlier route state and admit a different continuation before the declared terminal | Confirmed | Direct | High | P4 |
| `SKYRIM-011` | The scoped Hadvar trace reproducibly orders character gate, escape scripting, equipment, combat, oil, lock, lever/bridge, spiders, bear and exterior quest settlement | Observation | Corroborated | High | S2, S3 |
| `SKYRIM-012` | The repository trace reproduces ancestry, branch, loot, combat, perception, lock, fixture, save and terminal transitions without claiming direct play | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Bethesda Game Studios and Bethesda Softworks; Skyrim
  Special Edition released for Windows in 2016 and is maintained through the
  official 2026 Update 1.7.99/hotfix boundary reviewed here.
- Platform or physical form: one unmodded single-player Windows Steam save;
  keyboard/mouse versus controller binding is a parameter rather than a gene.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/489830/The_Elder_Scrolls_V_Skyrim_Special_Edition/),
    for current title, Windows product, single-player form, Special Edition
    contents and the separately sold Anniversary Upgrade boundary.
  - **[P2]** [official Steam announcement for Update 1.7.99](https://steamcommunity.com/games/489830/announcements/detail/681885122980479680),
    for the 2026-08-20 update and its additional 2026-08-27 hotfix note.
  - **[P3]** [official Bethesda PC support article](https://help.bethesda.net/app/answers/detail/a_id/36338/),
    for the current executable, mod removal and clean unmodded troubleshooting
    boundary; current Bethesda support separately records the August 27 hotfix.
  - **[P4]** [official Bethesda Skyrim game manual](https://cdn.akamai.steamstatic.com/steam/apps/72850/manuals/skyrim_gfw_manual-07.pdf?t=1438622529),
    for controls, HUD, health/magicka/stamina, skills, inventory/equipment,
    magic, combat, stealth, lockpicking, maps, quests and save/load semantics.
- Secondary and reproducible sources:
  - **[S1]** [SteamDB public build 24914197](https://steamdb.info/patchnotes/24914197/),
    for the public Windows build associated with the August 27 hotfix; SteamDB
    is used only for the store build identifier.
  - **[S2]** [maintained `Unbound` quest reference](https://skyrim.fandom.com/wiki/Unbound_(quest)),
    for `MQ101`, character creation, Hadvar/Ralof fork, oil, lock, lever,
    collapse, spiders, bear, cave exit and `Before the Storm` transition.
  - **[S3]** [Special Edition `Unbound` walkthrough](https://gamefaqs.gamespot.com/ps4/191475-the-elder-scrolls-v-skyrim-special-edition/faqs/76005/unbound),
    for the independent Hadvar gear, key, combat, potion, lever, bear and
    exterior-route reproduction. Cross-platform route claims are reused only
    where the current PC base quest is unchanged.
  - **[V1]** repository-side transition trace derived from `P1`–`P4` and
    `S1`–`S3`; executable rules reasoning, not direct play.
- Claim IDs: `SKYRIM-001`–`SKYRIM-012`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, directly navigate the prisoner; `ACT-131`, drink
  one carried healing potion; `ACT-161`, aim and commit the current sword, bow
  or other direct weapon strike; `ACT-190`, cast Flames or Healing under its
  current target/resource state; `ACT-199`, transfer and equip compatible
  chest, body or world loot; `ACT-202`, enter or leave crouched sneak posture.
- New genes: `ACT-343`, confirm one ancestry plus persistent bodily
  presentation without a class/build budget; `ACT-344`, adjust one lockpick
  angle and apply torque to the declared novice cell lock.
- Parameters: route position, posture, target, hand/equipment state, spell,
  magicka, item, loot, ancestry, appearance, lock, angle and torque.
- Claim IDs: `SKYRIM-003`, `SKYRIM-005`–`SKYRIM-009`, `SKYRIM-011`–`SKYRIM-012`.

### System Behaviour Genes

- Existing genes: `SYS-215`, resolve directly commanded live hostile combat;
  `SYS-342`, add use progress to the matching One-Handed, Destruction, Sneak or
  Lockpicking skill; `SYS-373`, turn local sight/sound exposure into detection
  and combat; `SYS-379`, retain Hadvar selection and `Unbound` objective flags
  into the successor quest.
- New genes: `SYS-612`, apply the chosen ancestry's starting bonuses, passive
  and power to the persistent character; `SYS-613`, turn pick angle, torque and
  resistance into partial motion, pick loss or an opened lock.
- Resolution order: character confirmation writes the persistent starting
  state; scripted escape reaches the exclusive keep fork; equipment and hand
  state gate live combat/spells; local sight and sound update hostile awareness;
  eligible use adds skill progress; lock and fixture interactions update route
  access; required quest flags settle at the cave exit into `Before the Storm`.
- Claim IDs: `SKYRIM-003`–`SKYRIM-012`.

### Constraint Genes

- Existing genes: `CON-188`, the Hadvar/Ralof offer permits one persistent
  escort branch for the opening route; `CON-269`, Flames and Healing require
  their legal cast form, target/state and magicka; `CON-282`, later Helgen
  interactions require the authored prior location, key, lever, escort and
  encounter state.
- New gene: `CON-508`, lock travel requires an angle within the concealed
  tolerance and excess resisted torque consumes the finite pick.
- Scarce strategic resources: health, magicka, stamina, healing potion,
  lockpicks, safe combat/recovery windows, stealth exposure, current equipment,
  distance to Hadvar and valid quest/fixture state.
- Claim IDs: `SKYRIM-004`–`SKYRIM-011`.

### Information Genes

- Existing genes: `INF-073`, expose current hand/equipment and quick-selection
  state; `INF-115`, expose hostiles through local sight and sound; `INF-119`,
  expose health, magicka, stamina, skills and active effects; `INF-125`, expose
  current quest marker, journal and explored route; `INF-128`, expose reachable
  loot identity, inventory compatibility and carried weight.
- New gene: `INF-243`, expose graded lock-angle proximity through pick pose,
  cylinder motion, resistance and break feedback.
- Claim IDs: `SKYRIM-005`–`SKYRIM-010`, `SKYRIM-012`.

### Objective Genes

- Existing genes: none.
- New gene: `OBJ-113`, complete one authored captivity tutorial through the
  selected Hadvar route until `Unbound` settles and the same persistent
  character gains controllable exterior-world state.
- Success, evaluation and failure: only the completed quest plus retained
  outside-cave control is success. Death before it requires restoring a save;
  a broken pick, detected bear or alternative combat tactic can be recovered
  without changing the terminal. Abandoning the save lies outside the rules.
- Claim IDs: `SKYRIM-004`, `SKYRIM-011`–`SKYRIM-012`.

### Time Genes

- Existing genes: `TIM-003`, scripted danger, perception, movement, combat and
  resources continue in real time outside menus and loading; `TIM-007`, manual
  or automatic save restoration permits a different subsequent route history.
- New genes: none.
- Claim IDs: `SKYRIM-005`–`SKYRIM-007`, `SKYRIM-010`–`SKYRIM-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Clean current client at the main menu | Select `New Game` | The authored prisoner-cart and execution sequence begins with no retained prior character | exact fresh-save entry | `SKYRIM-001`, `SKYRIM-002` |
| Character gate is active | Select Nord, set the declared presentation/name and confirm | The persistent character receives Nord starting state and the execution sequence continues | mandatory identity is mechanical but has no class budget | `SKYRIM-003` |
| Alduin disrupts the execution | Follow the objective marker through the tower and yard | Scripted hazards and Hadvar guidance admit the two-door keep fork | authored disaster precedes direct dungeon play | `SKYRIM-004`, `SKYRIM-005` |
| Hadvar and Ralof offer different entrances | Enter with Hadvar | The Hadvar route persists; Ralof's interior allies/enemies and later Riverwood contact are not this trace | one exclusive branch is fixed | `SKYRIM-004` |
| Hadvar has cut the bindings | Open the ordinary chest, transfer its gear and equip the sword/armour | Compatible items enter inventory/equipment and change the available combat state | loot and equipment are causal to escape | `SKYRIM-005`, `SKYRIM-006` |
| Stormcloak hostiles occupy the next room | Move, aim and strike or cast Flames until the required group is cleared | Live damage, resources, hostile action and defeat resolve; the next gate becomes usable | combat is embodied and real-time | `SKYRIM-005`, `SKYRIM-006` |
| The route exposes oil and a hostile crossing it | Cast Flames onto the oil | The environmental surface ignites and applies its live hazard to eligible bodies | spell targeting can alter route combat indirectly | `SKYRIM-005`, `SKYRIM-006` |
| Health is below maximum and one potion is held | Drink the potion | The item is consumed and health increases immediately | healing is a finite inventory decision, not a cast bar | `SKYRIM-005`, `SKYRIM-006` |
| One novice prison cell is locked and at least one pick remains | Probe angles and apply torque | Wrong torque resists or breaks a pick; sufficient travel inside tolerance opens the cell and persists access | analog feedback couples inference and consumable risk | `SKYRIM-008` |
| The drawbridge is raised | Activate the reachable lever | The bridge lowers; crossing it triggers the authored collapse that prevents return | fixture state orders the route | `SKYRIM-005`, `SKYRIM-011` |
| Frostbite spiders block the cavern | Clear them with the admitted weapon/spell state | Their live attacks and defeat settle, and matching used skills may gain progress | combat use and retained skill progress remain distinct | `SKYRIM-005`, `SKYRIM-009` |
| The sleeping bear has not detected the character | Crouch and move outside its detection result | Sneak posture reduces exposure; the route advances without required bear combat | perception creates a non-combat solution | `SKYRIM-007` |
| A save exists before a route decision | Reload it and choose a different legal continuation | The earlier state is restored and the prior future is replaced | history is player-branchable before terminal | `SKYRIM-010` |
| Every required Hadvar-route gate is satisfied | Follow Hadvar through the cave mouth and wait for quest settlement | `Unbound` completes, `Before the Storm` activates and retained exterior control begins | the terminal is quest settlement plus open-world control | `SKYRIM-004`, `SKYRIM-011`, `SKYRIM-012` |

## Strategic and experiential structure

- Local decision: follow the marker or check nearby loot; hold weapon or spell;
  strike, block, cast, drink, crouch, reposition, probe the lock or operate the
  current fixture while preserving the three live resources.
- Medium-term planning: carry compatible gear and a potion, spend or preserve
  magicka, avoid unnecessary detection, save before a branch or risk and keep
  the selected escort and quest gates advancing in order.
- Long-term structure: convert one mandatory created identity and exclusive
  escort choice into an equipped, surviving persistent character whose opening
  quest settles into the wider world.
- Common heuristics: take the first reliable gear; let Hadvar share pressure;
  ignite oil only when the target is in it; test a novice lock with small angle
  changes; preserve stamina for movement; crouch before the bear; verify the
  quest transition rather than stopping at apparent daylight.
- Failure attribution: wrong branch, missed equipment, empty resource, exposed
  stealth, resisted pick angle, broken finite pick, untriggered lever, surviving
  hostile or premature terminal can be distinguished from random loot detail.
- Player-trust factors: explicit objective markers, visible resource bars and
  equipment, local perception cues, graded lock feedback, persistent door and
  quest flags, save restoration and a clear exterior transition.
- Claim IDs: `SKYRIM-003`–`SKYRIM-012`.

## Replay and variation

- What changes between sessions: ancestry/presentation, Hadvar or Ralof, loot
  details, weapon/spell use, damage and potion timing, skill gains, lockpick
  losses, bear detection and saves. The canonical trace fixes Nord and Hadvar.
- Randomness or procedural generation: Helgen geometry and mandatory gates are
  authored; incidental container/loot amounts and combat timings may vary but
  are not terminal prerequisites.
- Multiple viable strategies: melee, ranged or Flames can clear encounters;
  the bear can be fought or bypassed; the novice lock is an admitted deliberate
  test rather than a mandatory `MQ101` gate.
- Typical replay motive: compare the other escort branch or starting ancestry,
  execute a cleaner escape or continue into the open world. Only one declared
  Hadvar escape belongs to this genome.

## Adjacent systems and history

- Direct predecessor: the 2011 Skyrim rules provide the core quest and manual;
  Special Edition is the current separate product/version boundary analysed.
- Variants: console builds, Legendary Edition, Anniversary Upgrade, official
  Creations, mods, DLC masters and later quests require separate scope packets.
- Similar games: Cyberpunk 2077, Baldur's Gate 3, Elden Ring, Black Myth: Wukong
  and Red Dead Redemption 2 share selected character, live combat, inventory,
  quest, route or save mechanics.
- Important differences: Cyberpunk's scoped record couples lifepath, attributes,
  cyberware and a full ending branch; Skyrim's packet has ancestry without a
  build budget and stops after one tutorial escape. Baldur's Gate 3 uses a
  class/background point-buy character and turn-based party rules. Elden Ring
  centres Grace and a recoverable rune mark; Skyrim restores ordinary saves.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-190`, `ACT-199`, `ACT-202`, `ACT-343`, `ACT-344` | movement, healing, combat, spell, loot, sneak, ancestry and lock inputs |
| System Behaviour | `SYS-215`, `SYS-342`, `SYS-373`, `SYS-379`, `SYS-612`, `SYS-613` | live combat, skill use, detection, quest, ancestry and lock resolution |
| Constraint | `CON-188`, `CON-269`, `CON-282`, `CON-508` | escort, spell, route and lock legality |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-243` | equipment, perception, resources, quest, loot and lock feedback |
| Objective | `OBJ-113` | settle `Unbound` into retained exterior control |
| Time | `TIM-003`, `TIM-007` | live progression plus save-restored branches |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `189` (`GAME-0001`–`GAME-0189`).
- Exact genome matches: none.
- Tied near matches: `GAME-0146` — Cyberpunk 2077 (`18 / 61 = 0.295082`).
- Supported combination subsets: `COMB-0188`.
- Scan date: 2026-08-29.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0146` — Cyberpunk 2077 | `ACT-008`, `ACT-161`, `ACT-199`, `ACT-202`, `SYS-215`, `SYS-342`, `SYS-373`, `SYS-379`, `CON-188`, `CON-269`, `CON-282`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `TIM-003`, `TIM-007` | both use a persistent avatar, direct live combat, stance-sensitive detection, loot/equipment, activity skills, authored quest choices, local information and branchable saves, but Cyberpunk commits a lifepath plus attribute budget and carries cyberware, hacking and a full ending route; Skyrim commits ancestry without a build budget, introduces consumable analog lock feedback and stops at one escort tutorial's exterior-world settlement | Near, `0.295082` |

### Preserved research notes

- New genes: `ACT-343`, `ACT-344`, `SYS-612`, `SYS-613`, `CON-508`, `INF-243`
  and `OBJ-113`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: direct movement/combat/spells/loot/posture, live
  combat, skill use, perception, quest state, exclusive choice, route gates,
  equipment/resources/maps and real-time/save history reuse safely. Mandatory
  ancestry without a build budget, analog consumable lock probing and the
  tutorial-to-open-world terminal are absent as lower-ID boundaries.

## Combination status

- `COMB-0188` is a verified strict twenty-four-gene subset of the twenty-seven-
  gene genome, coupling ancestry, the exclusive Hadvar route, live
  weapon/spell/inventory combat, stealth, analog lockpicking, ordered fixtures
  and the exterior quest terminal.
- Every earlier verified combination is tested deterministically after
  registration; none is a proper subset of this genome.

## Taxonomy impact

- Registry changes: seven new Active genes, `COMB-0188` and four existing
  family memberships.
- Taxonomy-change record: none; no prior lifecycle or reviewed-game signature
  changes. Reused definitions retain their prior boundaries.
- Candidate terms affected: ancestry-only character confirmation, fragile
  angular lock probing, graded lock feedback and captivity-tutorial settlement.

## Negative results

- `ACT-238` and `CON-342` are not reused: Skyrim requires neither class,
  background, proficiency selection nor point-buy at Helgen.
- `ACT-231` and `CON-332` are not reused: there is no lifepath plus initial
  attribute budget.
- `SYS-369` is not reused: death restores a player/automatic save rather than a
  mission-authored checkpoint that preserves a specific failed route packet.
- `CON-286` is not reused: Skyrim's scoped potion is immediate and has no
  interruptible cast requirement.
- `OBJ-080` is not reused: there is no mandatory guardian whose defeat alone
  opens the exterior threshold; ordered escape and quest settlement do.
- Anniversary, Creation, DLC and later open-world mechanics are not admitted
  merely because their files or menus exist in the current product.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Current Update 1.7.99 plus the August 27
  hotfix supports a clean public-build-24914197 Hadvar route from mandatory
  character confirmation through completed `Unbound` (`SKYRIM-001`–`SKYRIM-012`).

## Нові гени

- [Observation | Corroborated | High] Added seven genes for ancestry-only
  character confirmation, persistent ancestry state, analog lock input,
  lock resolution/tolerance/feedback and the tutorial-to-open-world terminal.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0188` isolates the joined ancestry,
  Hadvar branch, equipment, live combat/spells, stealth, lock, fixture and
  completed-cave-escape structure.

## Зміни таксономії

- [Observation | Corroborated | High] No lifecycle migration and no previously
  reviewed signature change; the unit only adds bounded records and evidence.

## Нові питання

- Which later authored RPG tutorial preserves a mandatory ancestry decision and
  analog lock risk while replacing the solo escort route with army command?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0191` Total War: WARHAMMER III.
- Optimisation criterion: maximise demand-led information gain while testing a
  bounded strategic tutorial against the embodied Skyrim escape corridor.
- Expected information gain: faction asymmetry, campaign-map allocation,
  formation command, turn settlement and one authored prologue terminal.
- Backlog impact: Unit 2 of the active nine-game Goal.

## Чому саме вона

- [Confirmed | Direct | High] It is the next authorised entry in
  `SEARCH_DEMAND_GAME_SELECTION_007` and preserves the recorded order.

## Localisation status

- Ukrainian game, seven new-gene and combination entries are reviewed in this
  unit. The trademark title remains unchanged; Ukrainian prose is
  presentation-only.

## Open questions

- Recheck official update/build state and whether Bethesda changes default
  bundled Creation behaviour on review-on-touch. Do not add later quests,
  DLC, Anniversary content or mods without a separate bounded unit.
