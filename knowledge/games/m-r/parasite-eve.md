---
game_id: GAME-0562
slug: parasite-eve
game_title: Parasite Eve
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-019
    - ACT-089
    - ACT-131
    - ACT-183
    - ACT-191
    - ACT-199
    - ACT-341
  system:
    - SYS-299
    - SYS-362
    - SYS-453
    - SYS-578
    - SYS-794
    - SYS-954
    - SYS-1271
    - SYS-1365
    - SYS-1633
    - SYS-1634
    - SYS-1635
    - SYS-1636
  constraint:
    - CON-136
    - CON-175
    - CON-210
    - CON-269
    - CON-621
  information:
    - INF-119
    - INF-179
    - INF-537
    - INF-538
  objective:
    - OBJ-155
  time:
    - TIM-003
    - TIM-026
---

# Game: Parasite Eve

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Aya, Eve, Carnegie Hall, PE, BP, Theater Key, Rehearse Key and the named
weapons are carrier parameters, not independent game-name genes.

## Analysis scope

- Version / ruleset: original released English North American PlayStation
  campaign, 1998, fresh New Game on Disc 1, ordinary original controls and
  no imported progress. The original product carries SLUS-00662 and SLUS-00668
  for its two game discs; the selected packet does not require Disc 2. Exact
  owned binary, disc image hash and hardware execution are unverified. No
  Greatest Hits delta, Japanese script, PSN wrapper, sequel, cheat, emulator
  save state or EX Game rule is substituted.
- Structured analysis target: original North American PlayStation entry in
  `knowledge/platforms/games.json`, grounded in the original Square manual,
  independently authored first-day routes and sparse recorded stills.
- Primary decision loop: read current HP, PE, AT readiness, weapon range and
  enemy wind-up; move to avoid a live attack while AT charges; open command
  selection, choose a target or part and spend the ready opportunity on a
  weapon attack, early PE ability or item; settle damage, resources and loot,
  then inspect the next room and key-dependent route. Position is chosen in
  live space, while command selection pauses the battle; this is neither
  fixed alternating turns nor a free-aim shooter.
- Entry and exit: first ordinary Aya control outside Carnegie Hall after
  naming in a fresh New Game; complete Day 1, Resonance, through the opera,
  both Eve encounters, backstage keys, sewers and the mutated alligator.
  Accept the escape, Daniel/car conversation, day closeout and offered save,
  then accept the scripted Day 2 briefing and its automatic Mod Permit
  grant. Stop at first ordinary NYPD office control before locker/armory
  exploration, using that permit or starting a new field mission. The
  incidental grant does not admit the later equipment-modification loop.
- Reproducible route: enter the auditorium and approach the stage; complete
  the first Eve fight and acquire Heal 1; optionally return to the entrance
  for the finite police ammunition grant and paramedic heal, then descend
  behind the curtain. Fight the first rat, search the dressing-room body for
  Theater Key and save at its phone; read Melissa's diary for Rehearse Key.
  Enter the far rehearsal room, defeat the second Eve form and descend behind
  the piano. Traverse the sewers, inspect the M1911A1 chest below the stairs,
  follow the girl and use the gate panel/emergency phone. Defeat the complete
  alligator encounter, addressing tail and then remaining head/body target,
  and accept the stated day transition.
- Bounded side controls: inspect one ordinary medicine chest, equip one
  reachable weapon/armor replacement and allocate earned BP to an available
  parameter. Exercise learned Scan only after its level gate; the first
  natural day route can reach the early unlock without importing a save.
  No exact level, random drop, every hidden chest or grinding quota is a
  terminal condition. A separate safe save/load branch demonstrates retained
  progress; no unsupported automatic retry is presumed.
- Included: movement during field and live battle; addressed inspection,
  collection, keys and gate operation; ready command and target selection;
  loaded bullets, reserve, field reload and empty-clip reload downtime;
  weapon/armor replacement and derived parameters; distance-sensitive attack
  effectiveness, live enemy movement and attack cues, distinct alligator
  target parts and capability change; HP/healing, early PE use/recovery and
  full-bar protection; battle afflictions and compatible cures; encounter
  rewards, experience, early level unlocks and BP allocation; bounded item
  slots, manual telephone saving and day-closeout retention; current room,
  resource, range/target and learned Scan disclosures.
- Excluded: using the Day 2 Mod Permit, Torres/Wayne armory storage and modification,
  Tool/Super Tool transfer, trading-card slots, later weapon classes and
  advanced armor effects; deliberate level grinding, later Slow, Detox,
  Barrier, Haste, Liberate and other later spells; booster-consumption
  optimisation and the full hidden-item route; Central Park, hospital,
  museum, later days, final campaign bosses, named endgame equipment,
  EX Game, Chrysler Building and New Game + carryover. A visible future
  menu label or an item merely carried does not admit its later economy.
- Potential scoped modules: equipment tuning and storage, the hospital's
  key dependencies, late PE and resource fatigue, the full campaign finale,
  EX carryover and Chrysler Building.
- Direct-play status: not conducted. Inspected the original 28-page US
  manual scan, specifically printed pages 8–19 for field/menu/battle,
  saving, items, equipment, PE, progression and reload rules. Inspected all
  twenty-one static ten-second storyboard sheets covering the first 87:30 of
  Rex Sterling's full recording, with 160×90 source cells, from the title
  through the first-day route and the Day 2 opening. The recording includes
  commentary overlays; no sound or video playback was used. Sparse stills
  corroborate order, geometry and visible menus, not platform execution,
  exact inputs, hit probabilities, timing, random seeds or complete saved
  fields. No console, executable, memory card, input trace or frame-accurate
  failure experiment was inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PEV-001 | The selected product is the original English North American PlayStation release; the later PSN edition is a separate distribution. | Observation | Corroborated | High | P1, P2, S4 |
| PEV-002 | Complete Day 1 requires both Eve encounters, the two backstage keys, sewer gate and alligator before the retained next-day opening. | Observation | Corroborated | High | S1, S2, S3, V1 |
| PEV-003 | Aya moves between ready commands; attack selection pauses battle and exposes a weapon range volume, with distance affecting hit effectiveness. | Observation | Corroborated | High | P1, S2, S3, V1 |
| PEV-004 | Early PE can restore HP and recover over eligible time; repeated use can slow recovery, and a bounded full-bar flashing state reduces received damage. Exact recovery-fatigue/reset formulas are not certified. | Observation | Corroborated | Medium | P1, S3, S5, S6, V1 |
| PEV-005 | Finite ammunition, field reload, immobilising empty-clip reload, equipment replacement and bounded carried slots create preparation choices. | Observation | Corroborated | High | P1, S2, S3, V1 |
| PEV-006 | Victory grants loot/experience, early levels unlock Scan and BP can improve character or owned equipment parameters. | Observation | Corroborated | High | P1, S3, V1 |
| PEV-007 | Temporary battle afflictions affect live movement/HP and clear at battle end; destroying the alligator tail changes its remaining attack repertoire. | Observation | Corroborated | Medium | P1, S2, S3, V1 |
| PEV-008 | HP zero is Game Over; phones and the day-closeout save retain selected progress, rather than an asserted automatic same-room checkpoint. | Observation | Corroborated | High | P1, S1, S3, V1 |
| PEV-009 | Optional consumable chest contents and exact original release day disagree across accounts; neither is treated as a universal route constant. | Observation | Conflicting | Medium | S1, S2, S3, S4 |

## Basic data

- Release / origin: Square, original North American PlayStation release,
  September 1998. Secondary catalogues disagree between 8 and 9 September;
  this scope needs the edition/year, not an invented resolved exact day.
- Platform or physical form: original two-disc console game, selected
  first-day Disc 1 packet; its later PS3/PSP digital distribution is not
  proof of an original-hardware execution.
- Puzzle family: real-time system pressure; inventory and fixture dependencies;
  ordered dependency sequencing. These classifications concern survival,
  key-dependent fixtures and the required day route, not a pure logic puzzle
  or a complete crafting economy.
- Primary sources, accessed 2026-11-20:
  - **P1** [original Square Soft North American instruction manual](https://impzone.club/pdf/parasiteeve.pdf),
    a 28-page scanned publisher artifact hosted by a third party. Printed
    pages 8–19 are visually read; the hosting site is not represented as
    Square's official web domain. The scan's later PDF creation date does
    not change the artifact's original rules edition.
  - **P2** [Square Enix product-support release notice](https://support.na.square-enix.com/faqarticle.php?id=2041&kid=58072&la=1&ret=main),
    distinguishes the 15 March 2011 PS3/PSP PSN distribution from the target.
- Independently authored corroboration, accessed 2026-11-20:
  - **S1** [zaranith, RPGClassics, complete Day One](https://shrines.rpgclassics.com/psx/pe/day1.shtml),
    stage, keys, second Eve encounter, sewer gate and alligator closeout.
  - **S2** [Almar, complete Day 1 route](https://almarsguides.com/retro/walkthroughs/PS1/Games/ParasiteEve/FullPlaythrough/Day1/),
    independent geometry, range, optional equipment, save and part targeting.
    Its warning that ordinary chest contents vary is retained.
  - **S3** [Shotgunnova's original-game walkthrough](https://www.supercheats.com/playstation/walkthroughs/parasiteeve-walkthrough05.txt),
    controls, early PE level list, Day 1 through alligator/day save and first
    Day 2 boundary. The EX section is explicitly not the selected profile.
  - **S4** [original-edition catalogue and serial images](https://crimson-ceremony.net/lostreleases/item.php?id=pegame_pe1-ps1-usa1)
    and [independent catalogue](https://www.psxdatacenter.com/games/U/P/SLUS-00662.html),
    matching disc identities but differing exact release day. Serial names
    identify the target; no image or binary checksum is implied.
  - **S5** [2012 full-PE discussion](https://gamefaqs.gamespot.com/boards/198265-parasite-eve/61612115),
    distinguishes the manual's short flashing protection from indefinite
    full-bar defense; its claimed multiplier/eight-second constant and
    repeated-refresh technique are not admitted as measured native facts.
  - **S6** [SIwata inventory guide](https://gamefaqs.gamespot.com/ps/198265-parasite-eve/faqs/4077),
    read indexed excerpt only for repeated-cast recovery slowdown and a
    claimed armor reset. Full-page access is restricted; exact reset and
    recovery formulas remain unverified, and no reset exploit is required.
- **V1** [Rex Sterling full-game recording](https://www.youtube.com/watch?v=MwOBfJn8jj8),
  12:12:32 total. Only its first twenty-one static storyboard sheets are
  inspected. Published chapter labels include alligator 01:00:56 and
  Meeting Daniel 01:11:43; they describe this recording, not a native timing
  benchmark. The next-day scene is a terminal boundary, not Day 2 gameplay
  admitted into the genome.
- Claim IDs: PEV-001–PEV-009.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: direct Aya movement in current field/battle space;
  no jump, dodge-roll or free-flight command is invented.
- Existing `ACT-019`: choose a ready weapon/PE command and eligible enemy,
  part or own target. A menu-selected shot is not free reticle aiming.
- Existing `ACT-089`: explicitly inspect and take reachable scene items.
- Existing `ACT-131`: consume a compatible carried medicine/cure.
- Existing `ACT-183`: request field ammunition transfer into the weapon.
- Existing `ACT-191`: spend available BP on an eligible character/equipment
  parameter; exact quantities are parameters, not a new point-spend action.
- Existing `ACT-199`: equip the compatible acquired weapon or armor.
- Existing `ACT-341`: inspect the body/diary, unlock doors, operate the gate
  and commit the reachable telephone interaction. Claims: PEV-002–PEV-006.

### System Behaviour Genes

- Existing `SYS-299`: earned experience crosses level thresholds, improving
  current statistics and exposing early learned PE/BP opportunities.
- Existing `SYS-362`: bounded victory/reward sources settle experience and
  eligible inventory drops before field traversal resumes.
- Existing `SYS-453`: currently equipped weapon/armor properties determine
  the relevant offense, protection, range and ammunition parameters.
- Existing `SYS-578`: damage/healing update Aya's single HP pool, with zero
  ending the attempt unless a genuinely carried eligible revival applies.
- Existing `SYS-794`: the alligator's separately addressed tail can be
  removed while the remaining actor continues with changed attacks.
- Existing `SYS-954`: eligible local traversal can instantiate a random
  encounter; exact spatial check period, rate and slot weights are unmeasured.
- Existing `SYS-1271`: an exhausted clip automatically reloads with downtime;
  this carrier also prevents movement during that reload. A field reload is
  a separate deliberate preparation action.
- Existing `SYS-1365`: PE is a capped spendable casting reserve that recovers
  over eligible battle time; repeated casts can slow recovery. It is not
  health or a separate cooldown per spell, and exact decay/reset formulas
  remain unverified.
- New `SYS-1633`: current spatial distance changes command-attack damage,
  critical opportunity and misses; an ineffective-range target is not simply
  prohibited by a hard intersection rule.
- New `SYS-1634`: BP allocations debit the retained balance and modify the
  addressed character or owned equipment parameter. Automatic level growth
  and optional later Tool transfer are different transitions.
- New `SYS-1635`: poison/movement afflictions have live effects, natural or
  compatible cure and battle-end clearing, not corridor-long round poison.
- New `SYS-1636`: a full flashing PE reserve reduces received damage while
  that condition holds, distinct from spending PE to heal already lost HP.
- Claims: PEV-003–PEV-008. No exact hit, regeneration-fatigue, status duration
  or full-bar damage multiplier is certified.

### Constraint Genes

- Existing `CON-136`: Theater Key and the diary/Rehearse Key prerequisites
  must persist before the corresponding onward doors become usable.
- Existing `CON-175`: unhealed HP loss persists across rooms/encounters;
  exhausting the survival threshold ends this multi-node route.
- Existing `CON-210`: item and equipment acquisition obey current free slots
  and compatible quantity stacks; surplus is not an unlimited backpack.
- Existing `CON-269`: a learned PE command needs its eligible target, current
  resource and readiness rather than access to every later spell.
- Existing `CON-621`: an ordinary manual write requires the reachable
  designated telephone fixture and a usable memory-card slot. The offered
  day-end save is separately declared at the closeout.
- Claims: PEV-002, PEV-004–PEV-008.

### Information Genes

- Existing `INF-119`: HP, PE, AT, ammunition, level/BP, equipment and current
  affliction state are disclosed through HUD and available panels.
- Existing `INF-179`: the current field reveals local threats, interactables,
  doors and movement space, not hidden neighboring rooms or random rolls.
- New `INF-537`: the attack wireframe, loaded bullets and selected target/
  part expose the relevant spatial command context without a guaranteed hit.
- New `INF-538`: learned Scan conditionally discloses selected enemy HP and
  weakness; it does not make every ordinary battle view omniscient.
- Claims: PEV-003, PEV-005, PEV-006.

### Objective Genes

- Existing `OBJ-155`: satisfy the entire ordered first-day action route,
  survive the alligator, accept the save/closeout and retain immediate
  successor control. A first Eve victory alone does not finish the packet.
- Claims: PEV-002, PEV-008.

### Time Genes

- Existing `TIM-003`: movement, attacks, projectiles, reload exposure and
  battle affliction effects run live outside menus/cutscenes.
- Existing `TIM-026`: actor-local AT readiness gates command commitment;
  this carrier pauses battle for command selection and permits movement
  while the gauge fills. Enemy readiness is not an alternating player turn.
- Claims: PEV-003–PEV-007.

## Reproducible transitions

| Before | Action | Resolution | Distinction | Claim |
| --- | --- | --- | --- | --- |
| AT not full and enemy winds up | Reposition Aya across available floor | Avoid a compatible volley while readiness advances | Live movement does not spend a command turn | PEV-003 |
| AT ready | Open attack selection and choose target | Battle pauses and range/target information appears | Not slow motion or free reticle shooting | PEV-003 |
| Target outside effective range | Commit an allowed shot | Reduced effectiveness or miss is possible | Not a universal target rejection | PEV-003 |
| Loaded clip reaches empty | Accept automatic reload | Fire and movement are temporarily unavailable | Reserve ammunition is not an unlimited loaded clip | PEV-005 |
| Between battles with spare bullets | Choose field Reload | Loaded supply is prepared for the next battle | Deliberate preparation avoids an exposed empty-clip window | PEV-005 |
| Missing HP, ready command and enough PE | Use learned Heal 1 | PE is spent and missing HP recovers | Not an inventory medicine or passive HP regeneration | PEV-004 |
| PE is full and flashing | Preserve the condition or spend PE | Defensive reduction persists only while its condition holds | Distinct from a separate shield pool | PEV-004 |
| Experience reaches early level threshold | Accept level progression | Stats/BP and eligible learned Scan become available | No imported later ability is required | PEV-006 |
| Earned BP and eligible parameter | Allocate a selected quantity | Balance decreases and that recipient improves | Owned gear improvement does not apply to every later weapon | PEV-006 |
| No Theater Key | Inspect eligible burned body | Retained key enables its compatible doors | Searching and onward opening are different steps | PEV-002 |
| Diary reached after first key | Read and take Rehearse Key | Far rehearsal-room access becomes available | Not one universal key or a skipped second Eve fight | PEV-002 |
| Temporary poison or movement impairment | Wait, use a compatible cure or settle battle | Declared live effect ends under its recovery rule | No lingering field poison is inferred | PEV-007 |
| Alligator has tail and head targets | Deplete the tail before the remaining target | Tail is removed and the remaining attack repertoire changes | Part destruction is not whole-actor defeat | PEV-007 |
| HP reaches zero without a resolving revival | Accept Game Over and Continue from a written slot | Retained save is loaded; unsaved progress is not guaranteed | No asserted automatic same-room retry | PEV-008 |
| Complete alligator defeated | Accept escape, closeout and save | Immediate next-day control becomes retained | Not full-campaign or EX completion | PEV-002 |

## Strategic and experiential structure

- Local decision: balance firing distance with space to avoid the next volley;
  commit only after reading readiness and the addressed target.
- Medium horizon: keep bullets, HP, PE and free slots usable across the whole
  route, then decide which earned BP recipient helps the next encounter.
- Resource tension: healing spends a reserve whose full flashing state can
  itself protect. A medicine consumes inventory stock instead. Neither is a
  universal no-cost reset or a later Haste/Barrier effect.
- Failure attribution: a visible wind-up and range globe can explain a poor
  position, but exact miss/critical rolls remain uncertain. Hidden chest
  contents and untested formulas must not be presented as guaranteed facts.
- Trust: retain explicit save boundaries and the difference between part
  removal and boss defeat. Do not describe this first day as the entire RPG.
- Claims: PEV-002–PEV-009.

## Replay and variation

- Key order, both Eve encounters, gate and alligator terminal are authored.
  Movement, attack order, optional gear, loot acceptance and BP choices vary.
- Local encounters and some ordinary chest/drop contents can vary; no
  certified distribution, fixed seed or universally identical medicine is
  assumed. No grinding quota or no-damage run defines acceptance.
- Claims: PEV-002, PEV-005–PEV-009.

## Adjacent systems and history

- The sequel's MP/reload/bounty rules are not substituted for original PE.
- The 2011 PSN release is a later wrapper, not a newly researched platform.
- Day 2 tuning, storage and campaign-wide item/weapon optimisation are
  potential separate modules, not necessary first-day mechanics.
- Claims: PEV-001, PEV-004–PEV-009.

## Normalised genome

| Type | Genes |
| --- | --- |
| Action | `ACT-008`, `ACT-019`, `ACT-089`, `ACT-131`, `ACT-183`, `ACT-191`, `ACT-199`, `ACT-341` |
| System | `SYS-299`, `SYS-362`, `SYS-453`, `SYS-578`, `SYS-794`, `SYS-954`, `SYS-1271`, `SYS-1365`, `SYS-1633`, `SYS-1634`, `SYS-1635`, `SYS-1636` |
| Constraint | `CON-136`, `CON-175`, `CON-210`, `CON-269`, `CON-621` |
| Information | `INF-119`, `INF-179`, `INF-537`, `INF-538` |
| Objective | `OBJ-155` |
| Time | `TIM-003`, `TIM-026` |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `561` (`GAME-0001`–`GAME-0561`).
- Exact genome matches: none.
- Tied near matches: `GAME-0338` — Final Fantasy VII (`13 / 37 = 0.351351`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0338` — Final Fantasy VII | `ACT-008`, `ACT-019`, `ACT-131`, `ACT-341`, `SYS-299`, `SYS-362`, `SYS-453`, `SYS-954`, `CON-175`, `CON-269`, `INF-119`, `INF-179`, `TIM-026` | Parasite Eve makes live movement and distance part of command effectiveness, separates tail destruction, PE recovery/protection, quantitative BP, affliction clearing and conditional range/Scan information; the reactor mission instead couples party/Materia commands and its bomb escape deadline. No full-campaign identity follows from the shared readiness loop. | Tied near; `13 / 37 = 0.351351` |

### Preserved research notes

- New genes: six; twenty-six unchanged definitions reused.
- Classification result: New gene.

## Taxonomy impact

- Registry additions: `SYS-1633`–`SYS-1636`, `INF-537`, `INF-538`.
- [Taxonomy Change 308](../../../research/taxonomy-changes/TAXONOMY_CHANGE_308.md)
  records the admitted boundaries and rejected alternatives.

## Negative results

- None as a separate prior-claim rejection. Version and source uncertainties
  are recorded without silently rewriting an existing definition.

## Delta summary

## New facts

- [Observation | Corroborated | High] The first-day route couples live
  positioning and readiness-gated paused command choice with explicit keys.
- [Observation | Corroborated | Medium] Full flashing PE has a defensive
  consequence distinct from spending that reserve to recover HP.

## New genes

- [Observation | Corroborated | Medium] `SYS-1633`–`SYS-1636`, `INF-537`, `INF-538`.

## New combinations

- [Observation | Direct | High] No new combination proposal; proper-subset
  support is owned by Corpus comparison.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_308`; no previous
  definition, lifecycle or game signature changes.

## New questions

- What are the native exact distance/critical and PE recovery-fatigue formulas?
- Which optional original chest contents are fixed versus sampled?
- What fields does each telephone and day-end save retain at byte level?

## Next recommended game

- [Hypothesis | Limited | High] Original Switch Lorelei and the Laser Eyes,
  `GAME-0563` under approved Selection 045.
- Optimisation criterion: move from spatial readiness combat to modern
  clue-driven investigation while preserving mixed eras and platforms.
- Expected information gain: inspect the released original rules without
  treating an entire product or a later port as an undifferentiated union.
- Backlog impact: retain the five remaining subjects and stop after GAME-0567;
  no push, publication, Actions or deploy is authorised.

## Why this game

- [Hypothesis | Limited | High] A full first-day route exposes the distinction
  between live movement, command readiness, effective range and persistence
  without conflating the original combat with its sequel or a pure shooter.
