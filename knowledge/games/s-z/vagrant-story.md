---
game_id: GAME-0499
slug: vagrant-story
game_title: Vagrant Story
analysis_status: reviewed
reviewed: 2026-10-05
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-009
    - ACT-019
    - ACT-048
    - ACT-049
    - ACT-131
    - ACT-140
    - ACT-199
    - ACT-215
    - ACT-219
    - ACT-341
    - ACT-595
    - ACT-672
    - ACT-673
    - ACT-674
  system:
    - SYS-004
    - SYS-057
    - SYS-342
    - SYS-362
    - SYS-380
    - SYS-453
    - SYS-578
    - SYS-605
    - SYS-755
    - SYS-854
    - SYS-1186
    - SYS-1308
    - SYS-1353
    - SYS-1354
    - SYS-1355
    - SYS-1356
    - SYS-1357
    - SYS-1358
    - SYS-1359
    - SYS-1360
    - SYS-1361
    - SYS-1362
    - SYS-1363
    - SYS-1364
    - SYS-1365
    - SYS-1366
    - SYS-1367
  constraint:
    - CON-175
    - CON-210
    - CON-269
    - CON-304
    - CON-402
    - CON-766
    - CON-767
    - CON-768
    - CON-769
  information:
    - INF-119
    - INF-128
    - INF-142
    - INF-179
    - INF-180
    - INF-473
    - INF-474
    - INF-475
  objective:
    - OBJ-026
  time:
    - TIM-003
    - TIM-007
---

# Game: Vagrant Story — complete original Wine Cellar

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Weapon identities, button assignments, effect magnitudes, room geometry and
numeric resource limits are parameters, not separate genes.

## Analysis scope

- Version / ruleset: original 2000 English PlayStation retail rules reconstructed
  from the USA instruction booklet identifying NTSC U/C SLUS-01040 and the
  official Piggyback guide sample. The SLUS-90075 demonstration disc is not
  the target. Original physical retail, no remake, mod or New Game+ equivalence.
  Select ordinary Puzzle Mode / Evolve or Die OFF explicitly; its default and
  the recording's actual option setting were not inspected. No executable,
  disc hash, regional numerical parity or native frame timing is claimed.
- Structured analysis target: existing PLAT-PLAYSTATION, original English
  physical full-game release; the platform record must carry this boundary,
  not infer all reissues from the shared product name.
- Primary decision loop: read the current room, body condition, resources,
  equipment and reachable target parts; move and choose readiness, command a
  weapon attack, learned spell or eligible Break Art; time learned outgoing
  or incoming impact techniques; settle injury, Risk, MP, gear development
  and loot, then revise recovery, equipment and local access before continuing
  through the authored Wine Cellar network.
- Entry and exit: fresh New Game's first controllable Entrance to Darkness
  state in Wine Cellar, not the optional earlier manor introduction. Complete
  both mandatory guardians and the Chamomile return route. Exit after
  Dullahan in The Hero's Winehall: settle its statistic grant, offered items,
  optional final chest and eligible retained inventory decisions, then enter
  Catacombs before its next encounter or independent traversal challenge.
  The recorded map completion is 004%, not completion of the whole product.
  Earlier HP-zero Game Over ends this continuation without success.
- Included: all reachable Wine Cellar branches and returns, the optional
  crossbow, training dummy, Minotaur, acquired Chamomile access, Dullahan,
  final polearm, available equipment/gem changes, field disassembly, discard,
  storage, recovery items and permanent elixirs, paid book learning/casts,
  locally eligible weapon-experience Break Arts and Battle Ability unlocks,
  body-part condition, Risk, DP/PP, class/type/affinity, cubes and destruction,
  ledges, moving Cloudstone, locally evidenced floor panels, keys/clearance/
  timed lever doors, explored map and local save/restore opportunity. Optional
  training is not arbitrarily capped at the six initially displayed abilities.
- Excluded: independently timed Puzzle Mode ON, New Game+, other area's
  enemies/items/keys, the Stock Sigil obtained after Lich, later Analysis and
  Eureka, Catacombs challenge and workshop assembly/combine/repair. Field
  disassembly is available without that later workshop and stays included.
  No unrestricted late-game item table is flattened into this packet. No
  exact random, skill-threshold, impact-window or boss-stat formula is asserted.
- Potential scoped modules: an original workshop packet, a later timed route,
  exact executable regional comparison or New Game+ with their own entry and
  result. They have no invented module IDs or inherited signatures.
- Direct-play status: no native game, emulator, disc image, save or input trace
  was executed. Original booklet scans and official sample pages were visually
  inspected. Muted headless paused frames from an attributed emulator recording
  establish displayed states; edited cutscenes and reported save states prevent
  treating it as an uninterrupted native run. Its disc region/hash is unknown.
  No audio was analysed. Ads and blank frames were rejected. Secondary written
  routes corroborate qualitative alternatives, not measured engine order.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| VS-001 | Original English physical PlayStation rules and explicit ordinary-mode packet; native identity and regional parity unmeasured | Observation | Direct | High | M1 cover and pp4-5; P1 pp22-23 |
| VS-002 | Complete authored Wine Cellar route, optional branches, Minotaur, Chamomile return and post-Dullahan exit before Catacombs | Observation | Corroborated | High | P1 pp22-23; S1 Wine Cellar; R1 1640/2700/3077/3900/4050/4080 |
| VS-003 | Direct movement, draw/sheath, cube carry/push/destruction, ledges, autonomous Cloudstone, timed lever access and room-reset cubes | Observation | Corroborated | High | M1 pp7/14/17; P1 pp22-23; S1; R1 2401/3600 |
| VS-004 | Reachable body-part command, pre-attack probability/effect display and typed damage, with obstacles potentially hindering execution | Observation | Direct | High | M1 pp11/16-19; P1 pp4-5 |
| VS-005 | Separate HP, MP, Risk, local part condition, posture-dependent recovery and condition-specific functional penalties | Observation | Corroborated | High | M1 pp6/11/16/19; P1 pp4-5/22; R1 2700/3077/4042 |
| VS-006 | Learned three-channel chain and defence bindings, correctly timed impact responses and further eligible local growth | Observation | Corroborated | High | M1 pp17-18/22; R1 3080/3085/3100; S2 |
| VS-007 | Weapon-specific kill progress exposes Break Arts, which spend current HP; first book casts spend MP and retain learned spells | Observation | Direct | High | M1 p19; P1 pp114-115; R1 4050 |
| VS-008 | Gear-derived current statistics, adaptive class/affinity, DP-zero weakening and use-built PP that decays while drawn | Observation | Corroborated | High | M1 pp10-12/20; P1 pp4-5 |
| VS-009 | Category capacity, chosen transfers, permanent discard, field disassembly, shared storage and reward-close loss have different consequences | Observation | Corroborated | High | M1 pp9/13/20-21; P1 pp23/115; R1 1640/4050/4080 |
| VS-010 | Boss reel settles retained growth; Queens/Mages elixirs permanently increase eligible HP/MP capacity | Observation | Corroborated | Medium | P1 p114; R1 4030/4035/4040/4042/4050; S1; indexed S7/S8 stop descriptions |
| VS-011 | Ordinary running enemy/world time pauses in planning menus, targeting and free-look; total playtime is a separate continuing measurement | Observation | Direct | High | P1 pp4-5; M1 pp7/17 |
| VS-012 | Concealed locally eligible floor-panel effects and contact/temporary-detector disclosure are separate, with contact marks cleared on room exit | Observation | Direct | High | M1 pp15/20; P1 p22 Heal Panel and p114 Eye of Argon |
| VS-013 | Native hit/Risk formulas, unlock counter settlement, exact wheel selection/timeout, current-resource elixir restoration and complete regional parity remain open | Observation | Limited | Medium | Inspected M1/P1/R1 boundaries; S2/S7/S8 retrieval limits |
| VS-014 | The selected corpus neighbour shares support rules, not the new command-and-impact combat proposition | Observation | Direct | High | Deterministic complete-signature comparison below |

Observation records the cited artefact, not an independently reproduced engine
test. The uncertainty in VS-010 concerns the wheel procedure and unmeasured
current-resource restoration, not an assertion that permanent growth is absent.

## Basic data

- Release / origin: Square, original 2000 PlayStation release. M1 bears
  1999/2000 copyright and Square Electronic Arts LLC publication; the official
  guide's release date is 2000-06-21. These are documentary identities, not
  a fabricated executable patch version.
- Platform or physical form: original English PlayStation physical full-game
  retail; PLAT-PLAYSTATION target, not the enclosed demonstration disc.
- Puzzle family: command-and-response tactical decisions coupled to live
  traversal and authored dependencies; family metadata is a causal navigation
  classification, not a genre label or proof of historical influence.
- Primary sources: M1 original booklet and P1 publisher-offered guide sample.
  R1 is an original attributed recording artefact, with emulator/editing limits.
- Secondary sources: attributed RPGClassics route/combat/ability/item lists
  and narrowly inspected indexed GameFAQs player guides, not executable code.
- Claim IDs: VS-001–VS-014.

### Source and recorded-state ledger

M1: [USA instruction booklet scan](https://www.videogamemanual.com/ps1/Vagrant%20Story%20%28USA%29.pdf),
32 PDF pages, printed rule page = PDF page minus two, SHA-256
`2b38957c3632e2f891e44d7b2f83c236b84ba18e1beea813b1352f27d7c9b206`.
Visual scans resolve controller symbols that OCR alone cannot identify.

P1: [official Piggyback guide page](https://www.piggyback.com/en/guide/vagrant-story/)
and [its offered sample](https://www.piggyback.com/en/wp-content/uploads/sites/7/2020/04/VS_E_SamplePlages.pdf),
five PDF pages, including printed 4–5, 22–23 and 114–115, SHA-256
`96ff4ef0b08b09436b3a6531847dc159452f684b3ae5c2b2fd645816d4632f48`.
The full 164-page book was not retrieved from an unauthorised copy.

R1: [PSX Longplay 143, Part 1](https://www.youtube.com/watch?v=5GVE4a8ULww),
World-of-Longplays, played by Connor, published 2012-10-02 UTC. Actual source
duration is 15303.981s. The creator reports emulator issues and edited/re-recorded
cutscenes; channel save states are not native persistence evidence. Recording
metadata and temporary frames remain outside Git. No captions were available.

| Actual source seconds | Visually inspected state | Admitted use |
|---|---|---|
| 1640.040546 | Worker's Breakroom chest lists Tovarisch, Buckler, Leather Glove, Vera Bulb x5 and Cure Bulb x5 with category capacities | Initial equipment and recovery choices, not a generic four-weapon loadout |
| 2401.330704 | Smokebarrel room, crates and knights; HP226/250, MP50, Risk1 | Current room traversal and pre-Minotaur resources |
| 2700.048157 | Minotaur wind-up; HP95/250, MP50/50, Risk3 | Combat cue and persistent resources, not exact boss HP |
| 3000.047164; 3070.091482 | Sydney post-Minotaur scene | Unlock boundary, not another independent combat loop |
| 3077.043442 | Ordinary play HP195/255, MP50, Risk0 and Chain shortcut | Retained resource state and changed command availability |
| 3080.214342 | Initial defence list Ward, Reflect Damage, Impact Guard | Separate learned incoming-technique list; Ward prevents Paralysis and Numbness |
| 3085.043259 | Reflect Damage tooltip, non-magical 40%, incoming damage unchanged | Reflection is not universal avoidance; reject secondary 50% wording |
| 3100.043904 | Initial Heavy Shot, Gain Life, Temper; Heavy Shot extra70% | Three initial chain abilities, not six separate genes |
| 3600 | Post-unlock crate climb, HP247/255 | Traversal stays causal after new combat availability |
| 3900 | Dullahan in The Hero's Winehall | Required second guardian, not whole-product final boss |
| 4030.064618; 4035.045495 | Congratulations, result MAP004%, NORMAL AGENT | Bounded boss result before its remaining rewards |
| 4040.042408; 4042.235087 | Cycling reward field and settled HP+3 | Recorded statistic grant; no hidden input, frame offset or arbitrary-choice guarantee |
| 4050.039089 | Elixir of Queens, Elixir of Mages and Grimoire Lux / Spirit Surge | Final permanent-capacity and paid-learning choices stay in scope |
| 4080.332015 | Rusty Nail, Braveheart, Cure Bulb x3; Bronze Polearm, Piercing/Two-Handed | Optional final chest and weapon-hand compatibility |

4070/4200 are not assigned unverified room names; 4500 is a later chest and
excluded. Captures at 3300/4800/5400/6000 contain ads or blank frames and
do not support claims. Small storyboard previews located inspection points
but were not used to read unreadable rules. The Catacombs exit is corroborated
by P1's map and S1, not a guessed crossing timestamp.

S1: [RPGClassics first route](https://shrines.rpgclassics.com/psx/vs/walk1.shtml),
read through the complete Wine Cellar and later-area boundary.
S2: [combat](https://shrines.rpgclassics.com/psx/vs/combat.shtml).
S3: [chain abilities](https://shrines.rpgclassics.com/psx/vs/chainabilities.shtml).
S4: [Break Arts](https://shrines.rpgclassics.com/psx/vs/breakarts.shtml).
S5: [keys and sigils](https://shrines.rpgclassics.com/psx/vs/keysandsigils.shtml).
S6: [traps](https://shrines.rpgclassics.com/psx/vs/traps.shtml).
S7: [Redefiner's Stat Wheel Guide](https://gamefaqs.gamespot.com/ps/914326-vagrant-story/faqs/39091),
dated 2005-09-25; S8: [ZNicholson's guide](https://gamefaqs.gamespot.com/ps/914326-vagrant-story/faqs/7745).
S7/S8 stop-timing descriptions were inspected through the search index; direct
retrieval was restricted. No access restriction was bypassed. Their complete
tables, seven-slot offset and no-input timeout were not independently read or
tested and are not admitted numerical rules. DataCrystal code-address search
leads likewise are not inspected program code.

### Conflict dispositions

- M1/P1 establish that DP zero weakens retained gear; reject S2's universal
  unusability wording. P1 ties PP decay to drawn time, not all unused equipment.
- Actual R1 Reflect Damage returns 40% of non-magical harm without reducing
  received harm; do not substitute a secondary casual one-half value.
- Dulling Impact Slow versus Silence is conflicting. General typed learned
  responses are retained, but neither unsupported named assignment is asserted.
- Secondary Minotaur/Dullahan HP values disagree; exact native boss values
  are not required or invented. No regional parity follows from these sources.
- Head Silence blocks normal casting, but P1 explicitly excepts Grimoire
  casts. M1 p19 explicitly states that first Grimoire use spends MP.
- Trigger-discovered trap marks persist until room exit. Eye of Argon's
  temporary local reveal does not establish an exact duration or later Eureka.
- Permanent elixir capacity growth is retained. Whether current HP/MP also
  rises by the same amount is unmeasured; do not claim either absence or parity
  with SYS-417's mandatory same-amount restoration.
- Pause in targeting/free-look does not pause the separate playtime counter;
  that counter does not itself prove HP/MP regeneration keeps running there.

## Mechanical decomposition

### Action Genes

- Existing ACT-008/009/048/049: direct walking/running/jumping and authored
  ledge traversal, adjacent cube push, lift/carry/place and lever activation.
  Carry is a world-object action, not obtaining inventory loot.
- Existing ACT-019: choose a weapon, learned spell or eligible Break Art and
  its legal target part or area, including declared targeting height.
- Existing ACT-131/140/199: spend a carried medicine/elixir/book, choose one
  offered unlearned Battle Ability and transfer compatible loot, equipment,
  gems or stored inventory. Book ownership is not already learned magic.
- Existing ACT-215: rebind learned chain and defence capabilities in a paused
  preparation menu before the next live segment. Its unchanged definition is
  not restricted to a pre-match bench. Three inputs for each list are parameters.
- Existing ACT-219: disassemble an owned weapon/shield into component returns.
  This is field recycling, not unauthorised later workshop assembly.
- Existing ACT-341/595: operate authored fixtures/access/save and explicitly
  draw or sheath the retained weapon.
- New ACT-672: press an assigned secondary technique at an existing outgoing
  or incoming impact without choosing a new target. Ward and reflection do not
  turn every response into a weapon parry or successful avoidance.
- New ACT-673: permanently discard chosen eligible stock without item effect,
  component compensation or a recoverable ground object; equipped stock is
  ineligible for discard under the original menu condition.
- New ACT-674: choose when to request a cycling reward's stop, not directly
  choose any catalogue option or guarantee the currently visible entry.
- Claim IDs: VS-003, VS-006, VS-007, VS-009, VS-010.

### System Behaviour Genes

- Existing SYS-004/057: probabilistic eligible outcomes and perceived-target
  hostile pursuit. No exact random seed, universal between-room pursuit or
  perception radius is asserted. The timed statistic reel is not thereby
  declared a pure random draw.
- Existing SYS-342/362: activity-specific skill progress and eligible
  encounter/chest rewards. Matching weapon kills grow their Break Arts;
  successful impact responses grow further Battle Ability opportunity.
  Exact thresholds/counter addresses or kill-time unlock settlement are open.
- Existing SYS-380/854/578: selected typed learned effects, type/affinity
  command damage and persistent survival HP. A forecast is not guaranteed
  harm; HP zero is terminal. Ordinary basic attacks are not silently included
  in SYS-380's explicit exclusion.
- Existing SYS-453: equipped gear/gems and character properties derive current
  combat state and weapon-class command availability, without an invented
  passive tree, socket polarity or workshop.
- Existing SYS-605/755/1186/1308: route flags, destructible cube support, a
  finite-time lever door and own-HP payment for Break Arts. The secondary
  two-second lever value is attributed, not measured natively.
- New SYS-1353: eligible attacks raise Risk; eligible elapsed time or recovery
  lowers it; higher Risk lowers hit chance and raises critical opportunity.
  No exponential formula or universal incoming-harm multiplier is asserted.
- New SYS-1354/1355/1356: DP wear reaches weakened but usable gear; use builds
  PP, which boosts performance and decays while drawn; the retained item's
  class/affinity adapts to its own offensive/defensive use. These are three
  different states, not one anonymous durability/experience gauge.
- New SYS-1357: a timely outgoing technique extends an executing sequence
  through its declared effect and further opportunity; failed timing ends it.
  Incoming defence resolves one response, not consecutive defensive chains.
- New SYS-1358: local part condition changes its declared functions separately
  from total survival HP. Critical head Silence, right-arm harm reduction,
  left-arm avoidance reduction, body Risk and leg movement penalties are
  parameters. This is not detachment, prosthesis, disease or universal immunity.
- New SYS-1359: first eligible paid Grimoire cast both executes and learns;
  later normal use still spends MP. Merely taking the book does not learn it.
  No locally unproved duplicate-book level cap is imported.
- New SYS-1360/1361/1362: reward-list closure destroys unclaimed contents;
  leaving a room restores its authored cube state, not the retained run;
  contact triggers an eligible local floor panel's declared effect, including
  Smokebarrel's beneficial Heal Panel, not every later-area trap class.
- New SYS-1363/1364/1365: an autonomous to-and-fro Cloudstone carries supported
  occupants; HP gradually recovers at posture-dependent rate; paid magic spends
  a separate capped MP reserve with eligible gradual recovery. Neither HP
  recovery nor MP recovery is an invented quiet-delay or per-round AP refresh.
- New SYS-1366/1367: a settled permanent statistic increment updates the
  personal value or capacity, including wheel and consumed final elixirs;
  eligible containers expose one matching-save retained bank. Neither is
  automatic collection of every offered item or unbounded global storage.
- Resolution order: select and validate a command; expose its declared
  pre-commit information; spend its documented resource and execute; resolve
  eligible impact response, harm and current state changes; after a qualifying
  defeat expose statistic/loot settlement; transfer, consume, store, disassemble
  or discard before ending the current offer and continuing. This describes
  source-visible causal stages, not an uninspected engine's total event ordering.
- Claim IDs: VS-003–VS-013.

### Constraint Genes

- Existing CON-175/210: depleted survival HP and typed carrying/stack limits.
  Excess offered loot remains untransferred until the list closes; its ensuing
  destruction belongs to SYS-1360, not the capacity predicate.
- Existing CON-269/304/402: eligible spell/technique target/resource/readiness,
  current injury/status performance and required hostile-clear exits. Only
  evidenced body-condition parameters transfer, not hunger or all Zomboid
  subsystems. Paralysis, Silence and Numbness have different command effects.
- New CON-766: weapon-ready posture forbids cube carry and authored climb,
  not all running, jumping or attacks. Sheathing restores the free-hand option.
- New CON-767: ordinary target part must at least partly intersect the current
  weapon/attack range. Obstacles may hinder execution; no universal strict
  line-of-sight selection rejection is inferred.
- New CON-768: compatible learned assignment/context/body state admits an
  impact response. Consecutive outgoing techniques cannot immediately repeat
  identically; incoming defence has no consecutive defensive chain. Exact
  reaction-window length is unmeasured.
- New CON-769: separate shield and one-handed weapon compatibility versus
  two-handed occupation. S1's early shield condition and inspected item types
  support this; a native two-handed equip rejection was not reproduced.
- Scarce strategic resources: current HP/MP, usable carried recovery, category
  headroom, current low Risk and useful gear condition/specialisation. Not
  invented currency, universal ammunition or purchased character levels.
- Claim IDs: VS-003–VS-009, VS-013.

### Information Genes

- Existing INF-119/128: own resources/build/part panels and disclosed offered
  loot/quantity/capacity/compatibility. Unopened chests are not omniscient lists.
- Existing INF-142/179/180: visible attack/impact timing cues, current room
  geometry/actors/fixtures and explored authored room connectivity. No audio
  channel was inspected; an external complete guide is not the player's map.
- New INF-473: target-part estimated harm, probability, type/affinity/class or
  secondary effect before committing, not every precise enemy parameter.
  Later Analysis is required for exact enemy Status and is excluded here.
- New INF-474: original item properties versus combined ORG/EQP combat result,
  DP/PP and current class/type/affinity; not an imposed Mod-drain calculation.
- New INF-475: concealed floor-panel disclosure by triggering or eligible
  temporary detector; contact marks last until room exit. Information can change
  without requiring a new harmful effect; beneficial panels remain panels.
- Claim IDs: VS-004–VS-012.

### Objective Genes

- Existing OBJ-026: traverse the connected authored Wine Cellar exit after
  its boss/key/cube dependencies and settlement. One opened chest, Minotaur
  alone or the Dullahan Congratulations frame does not finish the full packet.
  Every optional item is not compulsory; MAP004% is not whole-game completion.
- Claim IDs: VS-002, VS-010.

### Time Genes

- Existing TIM-003: automatic enemy/world/effect time runs outside declared
  planning states. Menus, targeting and free-look pause relevant live simulation;
  pause is an explicit parameter, not a copied squad-wheel or ship-crisis gene.
  The independently continuing playtime counter is not the resource-update clock.
- Existing TIM-007: eligible Memory Card saves restore a recorded route
  continuation and permit another branch. A prior load is not automatic
  metaprogression, enemy respawn or proof that a discarded current reward stays
  recoverable. Native card execution was not tested.
- Claim IDs: VS-009, VS-011, VS-013.

## Reproducible transitions

| Before | Action | Qualitative resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Drawn weapon beside eligible cube/ledge | Attempt carry/climb, then sheath and retry | Ready posture rejects the free-hand interaction; compatible sheathed posture admits it | Movement is not universally disabled in Battle Mode | VS-003 |
| Target visible outside current sphere | Choose that part, then move into partial range intersection | Reachability changes with weapon and position; visibility alone is insufficient | Basic reach differs from the legal special-ability predicate | VS-004 |
| Legal target with disclosed hit chance below certainty | Commit ordinary attack | Its probability process can select hit or miss before typed harm/condition settlement | Forecast is not guaranteed damage or pure collision | VS-004, VS-005 |
| Learned assigned outgoing technique at weapon impact | Press its input in the eligible opportunity | Accepted technique applies added effect and exposes a further link; failed timing ends extension | Secondary input is not a new independently targeted attack | VS-006 |
| Last chain link used one technique | Request that same technique immediately again | Immediate identical continuation is unavailable | Binding and continuation predicate differ from effect magnitude | VS-006 |
| Non-magical hostile impact and learned Reflect Damage mapped | Time the incoming response | Recorded tooltip specifies 40% return with incoming damage unchanged | Reflection is not prevention, healing or one-half return | VS-006 |
| Gear DP reaches zero | Use the retained item | Offensive/protective performance is reduced; item remains usable | Zero wear is not item deletion/universal disablement | VS-008 |
| Charged retained weapon/shield remains drawn | Let eligible simulation time pass | PP decays separately from DP; sheathing changes the relevant state | Unused/unequipped decay is not the admitted trigger | VS-008, VS-011 |
| Same weapon repeatedly used against a declared class | Continue eligible attacks | Its retained class effectiveness changes | Gear specialisation is not actor-wide skill experience | VS-008 |
| Compatible body part becomes critical | Continue with its impaired function or apply eligible recovery | Part-specific function changes while global HP remains separate | No compulsory detachment or whole-body health equivalence | VS-005 |
| Owned unlearned Grimoire, sufficient MP and eligible target | Use the book | Required MP is spent, its spell executes and remains learned | Taking loot alone does not teach; first use is paid | VS-007 |
| Critical head Silence and eligible Grimoire | Compare normal cast with book use | P1 blocks normal casting but explicitly excepts the book | A generic Silence sentence cannot erase the exception | VS-005, VS-007 |
| Low HP and eligible Break Art | Commit the art | Its own HP cost is paid independently of subsequent retaliation | It is not MP, stamina or emergency-only permission | VS-007 |
| Offered chest/enemy loot exceeds carried category capacity | Transfer what fits, discard unneeded eligible stock or disassemble weapon | Capacity and retained constituent stock change without free assembly | Recycling returns parts; discard returns none | VS-009 |
| Some offered reward remains outside inventory | Confirm END/close | Untransferred current contents are lost from that continuation | No automatically banked or recoverable ground remainder | VS-009 |
| Stored item through one matching-save Container | Access another eligible Container | Same retained bank is available for transfer | It is not a fresh independent chest roll | VS-009 |
| Cubes displaced/destroyed locally | Exit and return to the room | Authored cube state is restored, retained actor route is not restarted | Local puzzle reset is not whole-run reset | VS-003 |
| Wine Guild Hall moving Cloudstone supports Ashley | Ride and leave toward the ledge | Autonomous to-and-fro travel changes launch/landing reach | No switch-directed or player-steered platform is required | VS-003 |
| Compatible lever door closed | Operate lever and delay passage | Door opens for its declared interval, expires closed and can be retriggered | S1's two seconds is not native timer measurement | VS-003 |
| Undisclosed eligible floor panel | Step on it | Panel effect applies; its contact mark stays disclosed until room exit | Beneficial effect and concealed information are independent | VS-012 |
| Qualifying guardian defeated | Request reel stop and settle its result | One retained statistic grant is credited; observed Dullahan result is HP+3 | No arbitrary-option or instant-visible-symbol guarantee | VS-010 |
| Dullahan final Queens/Mages elixir acquired | Consume the eligible item before area exit | Permanent HP/MP capacity increment is applied; current-resource restoration is unmeasured | Final reward decisions cannot be omitted as later content | VS-009, VS-010, VS-013 |
| Dullahan result reached, final chest still available | Decide final loot/equipment, then take Catacombs exit | Complete bounded route ends before the next area's loop | Result banner alone is not the scoped terminal | VS-002 |
| Recorded eligible save exists | Load it | Earlier recorded route state supplies another continuation | Current reward-close loss does not deny independent prior-save restoration | VS-009, VS-011 |

These transitions are reproducible from the identified written rules and
displayed recording states. They are not a native test suite, hidden-input
log, fully deterministic hit result or uninspected random distribution.

## Strategic and experiential structure

- Local decision: position and weapon change which parts are reachable;
  forecasted harm and probability expose different tradeoffs. A timed effect
  may protect against a status or reflect harm without preventing the hit.
- Medium-term planning: current Risk, HP/MP, local part state and gear DP/PP/
  class development respond independently. Carrying a better item does not
  equip it, learn a book or automatically compensate discarded loot.
- Long-term structure inside the packet: train eligible techniques, preserve
  recovery and useful specialised equipment, choose optional branch/storage
  visits, obtain Chamomile and settle both guardians before the Catacombs exit.
- Common heuristics are hypotheses, not guarantees: recover lower Risk before
  low-probability attacks; use forecast and class/type evidence rather than
  automatically choosing the highest nominal stat; inspect capacity before
  closing reward lists. A contrary state or unreliable forecast can weaken
  these heuristics. No numerical optimal route is asserted.
- Failure attribution: disclosed probabilities separate a miss from unlawful
  reach; a failed impact response is not identical to losing HP. A low-DP item
  and high Risk can weaken offence without removing the weapon.
- Player-trust factors: disclose source version and uncertainty; never call
  the art a screenshot or reviewed sources direct play. Preserve the normal
  casting/book exception, gear-zero usability and current-offer loss warning.
- Claim IDs: VS-002–VS-013.

## Replay and variation

- Authored room structure persists; branch order, weapon/shield choice,
  local training, equipment development, impact timing, recovery and retained
  loot decisions can vary. Cube reset permits revising a room arrangement.
- Hit/critical outcomes and eligible item increments may vary; exact seeds,
  distributions and frame offsets are not claimed. Source-attributed reel
  timing is not automatically a random draw or guaranteed desired result.
- Loading a prior local save starts another continuation of recorded history;
  emulator save states are excluded as game mechanics.
- Typical motive is a different retained build/route or better command timing,
  not an invented daily reward, absence penalty or live-service progression.
- Claim IDs: VS-003–VS-013.

## Adjacent systems and history

- The commercial product contains later workshops, spells, regions and New
  Game+; a shared title does not admit them into this bounded first-area loop.
- This review makes no unsearched external novelty or direct-influence claim.
  The selected complete-signature neighbour is interpreted below, not replaced
  with a genre-picked RPG or a list of unselected score anecdotes.
- Claim IDs: VS-001, VS-013, VS-014.

## Normalised genome

| Type | Active gene IDs | Candidates or parameters |
|---|---|---|
| Action | ACT-008, ACT-009, ACT-019, ACT-048, ACT-049, ACT-131, ACT-140, ACT-199, ACT-215, ACT-219, ACT-341, ACT-595, ACT-672, ACT-673, ACT-674 | 15 uses; buttons, item names and effect magnitudes are parameters |
| System Behaviour | SYS-004, SYS-057, SYS-342, SYS-362, SYS-380, SYS-453, SYS-578, SYS-605, SYS-755, SYS-854, SYS-1186, SYS-1308, SYS-1353, SYS-1354, SYS-1355, SYS-1356, SYS-1357, SYS-1358, SYS-1359, SYS-1360, SYS-1361, SYS-1362, SYS-1363, SYS-1364, SYS-1365, SYS-1366, SYS-1367 | 27 uses; native formulas remain unmeasured |
| Constraint | CON-175, CON-210, CON-269, CON-304, CON-402, CON-766, CON-767, CON-768, CON-769 | 9 uses; exact capacity, range and timing parameters |
| Information | INF-119, INF-128, INF-142, INF-179, INF-180, INF-473, INF-474, INF-475 | 8 uses; no audio or later enemy omniscience |
| Objective | OBJ-026 | Connected first-area exit, not whole-product ending |
| Time | TIM-003, TIM-007 | Planning pause and separate local save/restore |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `498` (`GAME-0001`–`GAME-0498`).
- Exact genome matches: none.
- Tied near matches: `GAME-0490` — Comix Zone (`14 / 84 = 0.166667`).
- Supported combination subsets: none.
- Scan date: 2026-10-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| GAME-0490 Comix Zone | ACT-008/009/131/341, SYS-578/755/1308, CON-175/210/402, INF-119/128, OBJ-026 and TIM-003 retain movement, cube push/destruction, carried recovery, access, health-paid action, capacity, clearance and connected live route | Comix Zone's complete first comic page uses live body attacks, facing deflection, paper/choice forks, Roadkill and three retained item slots. Wine Cellar instead uses paused reachable-part commands, probabilistic typed harm, impact-technique chains, independent Risk/DP/PP/part state, learned magic, field gear/storage and post-guardian settlement | Near, `0.166667` |

- New genes: 25 supported operational additions; site acceptance is recorded separately.
- Reused genes: 37 unchanged English boundaries, including field recycling,
  capability preparation, timed passage, probability and current body state.
- Classification result: New gene.
- Evidence and reasoning: complete declared packet, not an arbitrary gene
  quota. All 274 verified combinations were tested as proper subsets; none
  applies. A single new carrier does not establish a recurring combination.

### Preserved research notes

- New genes: 25 supported operational additions; site acceptance is recorded separately.
- Reused genes: 37 unchanged English boundaries, including field recycling,
  capability preparation, timed passage, probability and current body state.
- Classification result: New gene.
- Evidence and reasoning: complete declared packet, not an arbitrary gene
  quota. All 274 verified combinations were tested as proper subsets; none
  applies. A single new carrier does not establish a recurring combination.

## Taxonomy impact

- Registry changes: ACT-672–674, SYS-1353–1367, CON-766–769
  and INF-473–475. Previous English definitions and signatures stay unchanged.
- Taxonomy-change record: TAXONOMY_CHANGE_236. Full unit acceptance remains
  gated on the complete Ukrainian/presentation/validation envelope.
- Candidate terms affected: no vocabulary-only term gains an ID by resemblance.

## Negative results

- None as a new independent negative-result record. The primary/secondary
  conflict dispositions above reject overclaimed parity and unusability, not
  a previously accepted corpus definition or another game's signature.

## Delta summary

## New facts

- [Observation | Corroborated | High] The complete ordinary Wine Cellar packet
  includes final elixirs/books/polearm decisions, not only Dullahan's result
  banner; VS-002, VS-009 and VS-010 preserve their different consequences.
- [Observation | Corroborated | High] DP zero retains weakened usability and
  PP decays while drawn, not every unused/unequipped interval; VS-008.
- [Observation | Direct | High] First Grimoire use is MP-paid and learns the
  cast spell; head Silence has its primary-documented book exception; VS-007.

## New genes

- [Observation | Corroborated | Medium] Twenty-five paired operational
  additions retain impact responses, resource/equipment/part changes,
  spell learning, reward loss, local support/reset, permanent growth and
  specific eligibility/disclosure. Individual confidence and evidence remain
  attached to each registry record; no native formula is silently promoted.

## New combinations

- [Observation | Direct | High] No new combinations; no existing verified
  proper subset applies, and one carrier is not recurring evidence.

## Taxonomy changes

- [Observation | Corroborated | Medium] TAXONOMY_CHANGE_236
  admits the bounded additions without an earlier English boundary/signature
  mutation. The separate completion report records full unit gates.

## New questions

- [Hypothesis | Limited | Medium] Native regional reproduction may sharpen
  wheel timing, skill-counter settlement and elixir current-resource effects;
  a conflicting executable result would reject the corresponding attribution.
- [Hypothesis | Limited | Medium] Independent command-combat carriers may
  support a reusable impact/condition combination; an absence of independently
  analysed causal recurrence rejects promotion, not the current observation.

## Next recommended game

- [Hypothesis | Limited | Medium] R.E.P.O., Windows Early Access, GAME-0500,
  after this complete unit's acceptance, local commit and stop window.
- Optimisation criterion: approved Selection 039 alternates modern/retro
  and platform/decision structures, rather than another similar RPG.
- Expected information gain: cooperative physical extraction, fragile value
  and shared progression under an exactly dated evidenced Early Access packet.
- Backlog impact: no following game starts while this unit is incomplete.

## Why this game

- [Hypothesis | Limited | Medium] First-area command/impact decisions provide
  a distinct original PlayStation counterexample to the preceding transport
  management and later cooperative extraction packet. This is selection
  reasoning, not an external novelty or universal user-experience claim.
