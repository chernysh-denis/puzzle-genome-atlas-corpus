---
game_id: GAME-0506
slug: avowed
game_title: Avowed
analysis_status: reviewed
reviewed: 2026-10-06
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-131
    - ACT-161
    - ACT-190
    - ACT-191
    - ACT-199
    - ACT-215
    - ACT-223
    - ACT-232
    - ACT-341
    - ACT-383
    - ACT-419
    - ACT-425
    - ACT-692
    - ACT-693
  system:
    - SYS-057
    - SYS-215
    - SYS-251
    - SYS-299
    - SYS-369
    - SYS-407
    - SYS-409
    - SYS-453
    - SYS-578
    - SYS-755
    - SYS-1416
    - SYS-1417
    - SYS-1418
    - SYS-1419
    - SYS-1420
  constraint:
    - CON-269
    - CON-270
    - CON-282
    - CON-304
    - CON-336
    - CON-337
    - CON-354
    - CON-589
    - CON-737
    - CON-769
    - CON-783
  information:
    - INF-119
    - INF-125
    - INF-128
    - INF-148
    - INF-295
    - INF-319
    - INF-334
  objective:
    - OBJ-080
  time:
    - TIM-003
    - TIM-007
    - TIM-027
---

# Game: Avowed — released On Strange Shores and the Paradis arrival

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Weapon names, two prepared sets, named companions, dialogue thresholds,
consumable quantities and controller labels parameterise rules, not new genes.

## Analysis scope

- Version / ruleset: original full-release February 2025 base-game tutorial,
  reconstructed from publisher instructions and post-release recording R2 of
  2025-02-21. The complete public launch was 2025-02-18. No installed executable,
  exact patch identifier, language-dependent rule difference or Normal preset is
  established. This is a dated qualitative ruleset, not current 2026 binary
  parity, Premium prerelease gameplay or the anniversary expansion.
- Structured analysis target: PLAT-XBOX-SERIES; original Xbox Series X|S base
  edition, released On Strange Shores to first ordinary Paradis dock control.
  R2's author describes Series X performance, but Xbox achievements and
  controller glyphs do not independently prove the captured executable's
  platform. Windows and later PlayStation releases are not merged into this
  target or claimed mechanically equivalent.
- Primary decision loop: explore the wreck and fort for reachable equipment,
  keys and supplies; configure and swap complete hand-pair preparations, choose
  direct attacks, guard, dodge or eligible spells against live hostile groups,
  and allocate limited stamina, essence and banked restorative effects while
  retaining dialogue decisions that determine Ilora's role in the final fight;
  overcome Steadman Ralke, reach the boat and continue into Paradis.
- Entry and exit: first ordinary control on the shipwreck beach after character
  creation, before collecting the first route equipment and entering Fort
  Northreach. Appearance, background and initial attributes are committed entry
  parameters, not commands exercised inside this packet. Include all reachable
  tutorial branches, the optional storeroom and Ilora release route, loot and
  traps, initial point allocation and eligible reset, final Ralke encounter,
  Adra voice conversation and boat handoff. Exit at first ordinary Dawnshore /
  Paradis dock control before the Captain Cynric decisions of Message from Afar.
  Boss arrival or the sailing cinematic alone is not completion. An eligible
  Second Wind can recover a zero-health event; otherwise lethal failure ends the
  current attempt and an eligible retained save can restore prior progress.
- Included: directly controlled running, jumping, crouching and traversing the
  authored geometry; hostile perception and live combat; primary/offhand weapon
  compatibility, two prepared loadouts and item-granted offhand magic; aimed
  attacks, charged attacks, blocking, learned parry and dodging; separate health,
  selective melee/guard stamina and supplied essence; spell recovery, food
  recovery banks and finite potions; stun and prompted critical action; temporary
  allied combatants; carried-load movement limits; key and destructible access, fire pods and brambles;
  Ilora's retained release state and attribute-qualified dialogue; experience,
  level-two points and eligible paid resets; quest/map, loot and combat feedback;
  live progress, tactical radial pause and retained-state restoration.
- Excluded: creation commands before entry, later Dawnshore investigations and
  Dreamthrall bear/Voice-power reward, party-camp creation, resting, workshops,
  cooking, permanent companion training, fast travel and later companion-command
  upgrades, traders, lockpicked later buildings, later regional quests and the
  campaign ending; July ability revisions, anniversary ancestries, quarterstaff,
  New Game Plus and custom difficulty; exact unmeasured damage, stamina,
  cooldown, restored-health, gear-level and simultaneous-event formulas.
  General camp inventory services are not imported from later regions merely
  because a control is visible; AV-015 preserves the qualified island restriction.
- Potential scoped modules: first established party camp and inventory-service
  eligibility, later regional equipment advancement, named companion command
  development, a measured Resolve/Second Wind reproduction and anniversary
  rules. No module ID or whole-product signature is created.
- Direct-play status: no original executable, console or native input was run.
  Publisher and developer text plus attributed muted paused frames are evidence,
  not a claim of uninterrupted personal play. R2 establishes the released route
  and displayed states, not hidden setup, build identity or native timings. R1
  and R3 were rejected as rule authorities after their prerelease dates were
  checked. No audio was played or analysed, no research window entered the
  foreground and no user window, focus or sound setting was changed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| AV-001 | The full release was 2025-02-18 on Xbox Series X/S and Windows; R2 was published three days later. Exact captured build and difficulty remain unverified. | Observation | Direct | High | P0; R2 metadata; rejected R1/R3 metadata |
| AV-002 | The complete tutorial crosses wreck, fort, prison, hostile groups and Ralke, then reaches ordinary Paradis dock control; the Adra conversation is not the later Dreamthrall ability reward. | Observation | Corroborated | Medium | R2 420/550/1000/1180/1250/1450/1550/1600/1800/1850/1930/1950/2008; S1 |
| AV-003 | Loot equips compatible carried weapons and armour; destructible boards/floors and typed fire barriers admit alternative or required local access. Storeroom access uses a separate key. | Observation | Corroborated | Medium | R2 700/800/1100/1250/1550/1600; P1 environmental techniques; S2; S1 roof/key route |
| AV-004 | The opening tutorial explicitly provides two prepared weapon builds switched by Y; two-handed occupation differs from one-handed weapon plus shield or book. | Confirmed | Corroborated | High | P1 Weapon Swapping; P2; R2 1250/1600 |
| AV-005 | Melee attacks and block/parry spend stamina; the written account distinguishes ordinary ranged attacks and dodging from those costs. The actual released ingame block tutorial requires an empty offhand or shield, and learned parry is not an always-unlocked default. | Observation | Corroborated | High | P1 Examine All of the Abilities / Combat Techniques; P2 weapon costs; R2 600/740 shield/760 block tutorial/800/1300; S4 stamina; S5 guard |
| AV-006 | An offhand grimoire exposes its item spells without first unlocking them in the Wizard tree; casts still require essence and ability readiness. Separately learned powers have their own acquisition conditions. | Observation | Corroborated | High | R2 actual ingame text 1550/1600; P1 Grimoire; P2 spellbook/learned distinction |
| AV-007 | Live hostile attacks damage health; separate stun accumulation exposes a reachable critical-action opportunity. Red attack cues warn that blocking is not a legal answer. | Observation | Corroborated | Medium | P1 Combat Techniques; P2 stun; R2 800/1800/1850 |
| AV-008 | Food/drinks create retained recovery for health or essence, including excess beyond current fullness; published accounts report slower recovery in combat, while S7's PC Path of the Damned account instead says meals do not work in combat. R2's preset is undisclosed, so no universal nonzero combat rate is asserted. Potions and food quantities are finite; essence is not restored by unfunded waiting alone. | Observation | Conflicting | Medium | R2 1550/1600/1850 resource circles and Arrack tooltip; S4 HUD; S5 food; S6 banked restoration; S7 contrary combat-food statement |
| AV-009 | Garryck assists autonomously; physically freeing Ilora makes her an ally in the boss fight. Leaving her imprisoned makes her an escaped hostile at that encounter, not a required dead-end. The hostile alternative is written evidence, not personally replayed. | Observation | Corroborated | Medium | R2 1180/1250/1300/1850 allied route; S1 both outcomes |
| AV-010 | Ilora's cell requires its key and actual door release, not merely a favourable reply; dialogue exposes attribute-threshold responses without revealing every downstream consequence. | Observation | Corroborated | High | R2 1000 Intellect 2/2; 1180; S1 physical release |
| AV-011 | Encounter experience reaches level two and the first ability choice offers Charge, Tangle or Minoletta's Missiles; displayed essence costs and separate cooldowns demonstrate two simultaneous readiness conditions. Publisher instructions permit currency-paid build resetting, while exact tutorial prices and grouping depend on current menu eligibility. | Observation | Corroborated | Medium | R2 1450 level two; actual 1480 choice with cost/cooldown; 1500 radial tutorial; P1 paid reset; S4 point allocation |
| AV-012 | Eligible Second Wind turns zero health into brief incapacitation and partial recovery, with cooldown-qualified later failure. Sources disagree on unconditional/default eligibility versus requiring Resolve; neither a zero-Resolve entitlement nor once-per-encounter readiness is asserted. | Observation | Conflicting | Medium | S4 default shorthand; S8 Resolve condition; Game8/Fandom dated lookup; P3 later brief-incapacitation note is not capture-patch proof |
| AV-013 | The opening action-wheel tutorial offers abilities, consumables and equipment; developer text specifies paused radial resolution. A post-release PC walkthrough recommends saving before fights and replaying to change expenditure. Exact autosave triggers and native disk persistence were not exercised. | Observation | Corroborated | Medium | Actual R2 1500 ingame radial tutorial; P3 1.2.2 paused-radial/save fixes; S7 inspected introductory save/replay advice; no native retry |
| AV-014 | Two visible tripwires lie on the opening route; the indexed walkthrough passage describes approaching and disarming each. No exact trap damage, reset or simultaneous trigger ordering is established. | Observation | Corroborated | Medium | R2 actual 625/638 visible wires; S9 inspected indexed route passage; S10 2026 route corroboration; no native disarm |
| AV-015 | Publisher inventory instructions apply generally, while a dated player report explicitly corrects its alleged dismantling bug after leaving the tutorial island. Later replies agree on the island restriction but disagree about requiring a camp location thereafter. A visible prompt alone does not prove successful starting-island transfer or salvage. | Observation | Limited | Medium | P1 general inventory service; S11 actual dated report and replies; no successful R2 operation located |
| AV-016 | Carried weighted equipment is compared with the current capacity; exceeding it slows movement and disables sprint. Current weight and limit are visible. This is a movement consequence, not a hard prohibition on taking another item or proof that camp services work on the starting island. | Observation | Corroborated | Medium | P1 encumbrance instruction; S6 weighted equipment; S12 inspected weight and movement account; no native threshold measurement |

## Basic data

- Release / origin: Obsidian Entertainment's Avowed, full release 2025-02-18;
  Xbox Series X|S analysis target and original dated base rules, not the later
  PlayStation release or an Early Access target.
- Platform or physical form: one directly controlled character with temporary
  autonomous tutorial allies, first-person controller presentation; exact
  captured platform and reproduction difficulty are qualified above.
- Mechanical family: FAM-010 live system pressure, FAM-013 typed key/fixture
  dependencies and FAM-017 ordered acquisition/access subgoals. All seventeen
  existing bilingual descriptions were reviewed: no new family, automatic-agent
  coordination family or logical-grid family is inferred just from companions,
  a spellbook or traversable 3D geometry.
- Sources accessed 2026-10-06:
  - **P0** — [Obsidian release announcement](https://news.xbox.com/en-us/2025/02/18/avowed-available-now-your-journey-awaits/), 2025-02-18. Full release and declared platforms, not captured binary identity.
  - **P1** — [Xbox Wire survival guide](https://news.xbox.com/en-us/2025/02/13/avowed-survival-guide-starting-tips/), 2025-02-13, publisher-platform firsthand instructions. This predates the complete release; admitted tutorial controls are corroborated with the post-release recording rather than silently promoted to current-build proof.
  - **P2** — [Obsidian combat-design account](https://news.xbox.com/en-us/2024/11/21/player-choice-avowed-approach-to-combat/), 2024-11-21, named combat designers. Weapon-hand preparation, stamina, spell costs and stun are development statements qualified by released evidence, not all campaign mechanics.
  - **P3** — [Developer patch 1.2.2](https://forums.obsidian.net/topic/134121-patch-122-notes/), 2025-02-18, read save/reload and paused-radial fixes. [Patch 1.2.4](https://forums.obsidian.net/topic/134364-patch-124-notes/) was found but direct retrieval returned 403; its Second Wind ledger limitation is a search locator, not a fully inspected primary passage or R2 patch identifier.
  - **R2** — [AdayCanarioWTF, released full-game recording](https://www.youtube.com/watch?v=KE03hv9Zgo8), published 2025-02-21, length 46,477 seconds. Actual muted paused samples: 20, 100, 220, 420, 450, 550, 600, 625, 638, 650, 670, 700, 740, 760, 800, 1000, 1100, 1180, 1250, 1300, 1400, 1450, 1480, 1500, 1550, 1600, 1700, 1800, 1850, 1930, 1950 and 2008 seconds. Opening cinematic samples do not disclose setup; 300 is black and rejected. 625/638 show two tripwires; 740/760 show shield and block eligibility. 1480 displays the initial ability choice with essence costs and cooldowns; 1500 displays the action-wheel tutorial. 2008 establishes first ordinary Paradis dock control. All sample times are locators, not fixed game durations. Optional branches omitted by this recording use explicitly attributed written evidence, not invented direct observations.
  - **Rejected R1/R3** — [Shirrako](https://www.youtube.com/watch?v=pxVhXJXAQOg), 2025-02-13, and [Skycaptin5](https://www.youtube.com/watch?v=cY56ulmC9k8), 2025-02-14. Their Premium prerelease dates prevent their serving as the release-rule authority. R1's keyboard-glyph frames also cannot establish the declared Xbox target.
  - **S1** — [GamesRadar, Ilora release and consequences](https://www.gamesradar.com/games/action-rpg/avowed-free-or-leave-ilora-fort-northreach-jail/), key/roof route, physically opening the cell and allied-versus-hostile boss alternatives; later Escape Plan is outside this packet.
  - **S2** — [GamesRadar, Northreach storage key](https://www.gamesradar.com/games/action-rpg/avowed-fort-northreach-storage-key/), optional dead-guard key and storeroom equipment. Finding the chest is not required to clear the tutorial.
  - **S4** — [TechRaptor's Steam starter guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3426726487), posted 2025-02-13. Stamina, resource-circle and level-two instructions are early firsthand written evidence, qualified where R2 corroborates them; its default Second Wind shorthand conflicts with S8 and is not silently accepted.
  - **S5** — [GamesRadar beginner techniques](https://www.gamesradar.com/games/action-rpg/avowed-tips/), guard eligibility, food, inventory and contextual stealth damage. Later camp facilities are not imported into the island.
  - **S6** — [GameSpot beginner tips](https://www.gamespot.com/gallery/avowed-tips-to-help-you-save-the-living-lands/2900-6259/), 2025-02-13 firsthand food-bank account. Its prelaunch publication and absence of native reproduction retain a qualified rather than universal numerical model.
  - **S7** — [GameFAQs dated walkthrough](https://gamefaqs.gamespot.com/xbox-series-x/296446-avowed/faqs/81720/intro), updated 2025-02-21, PC Path of the Damned author target despite Xbox URL. The actual Intro instructs saving before fights and replaying to revise potion expenditure, and states ordinary essence does not automatically return. Its claim of no combat meal benefit conflicts with S5/S6; this is retained, not erased or resolved by assuming R2's difficulty. Its damage-tier advice does not define this packet's numerical model.
  - **S8** — [Gamepressure Second Wind guide](https://www.gamepressure.com/avowed/what-is-second-wind/zd117ca), 2025-02-13, Resolve qualification; [Game8](https://game8.co/games/Avowed/archives/498701) and [Pillars wiki lookup](https://pillarsofeternity.fandom.com/wiki/Second_Wind_%28Avowed%29) route to cooldown/attribute claims. Search-only or inaccessible passages are not described as fully read.
  - **S9** — [Neoseeker On Strange Shores](https://www.neoseeker.com/avowed/On_Strange_Shores), indexed route passages actually inspected for approaching and disarming two tripwires, optional key access and initial point/route progression. Full direct retrieval returned 403. Actual R2 625/638 shows the tripwire geometry and S10 independently corroborates its placement; exact blast/reset behavior and a native disarm are not claimed.
  - **S10** — [NightlyGamingBinge's route walkthrough](https://nightlygamingbinge.com/on-strange-shores-main-story-walkthrough-avowed/), 2026-01-21, full route text inspected. It independently corroborates tripwire, optional switch/hidden room, keys, typed fire access, Ilora allegiance and boat completion. Later publication and occasional loot/plant naming differ from R2; do not convert its inventory labels into a fixed February loot table.
  - **S11** — [Dated inventory-service discussion](https://steamcommunity.com/app/2457220/discussions/0/595150518792246024/), 2025-05-31–2025-06-02. The original author reports successful dismantling only after leaving the tutorial island. Replies corroborate the island restriction but disagree over requiring the physical camp, which P1's inventory instructions contradict. This is firsthand secondary evidence, not February executable proof or authority for a universal later camp restriction.
  - **S12** — [Gamepressure carry-capacity account](https://www.gamepressure.com/avowed/how-to-increase-carry-capacity/zf117cc), updated 2025-02-19, actual weight/capacity and movement text inspected. The over-limit state slows movement and prevents sprint; its later camp-service advice is not starting-island eligibility proof. Exact capacity coefficients and native threshold reproduction are unmeasured.
- Private source frames and authoring drafts are not committed or publicly
  exported. Artwork is an original rules-informed illustration, not extracted
  footage. No audio, window creation in the foreground or native execution is
  claimed.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: directly move, jump, crouch and traverse eligible terrain.
- Reuse `ACT-131`: consume one finite potion or food/drink unit; accepting food
  adds recovery stock rather than guaranteeing an atomic full-health refill.
- Reuse `ACT-161`: aim a current weapon attack or charged strike at a reachable
  hostile or breakable object. A stealth strike can do enhanced damage without
  necessarily neutralising its target, so `ACT-235` is not imported.
- Reuse `ACT-190`: select and cast an eligible learned or item-granted capability.
- Reuse `ACT-191`: spend available level points on legal attributes or abilities.
- Reuse `ACT-199`: take and equip eligible carried equipment or supplies.
- Reuse `ACT-215`: configure the prepared primary/offhand assignments in the
  inventory before returning to live control; not the switching command itself.
- Reuse `ACT-223`: evade a live incoming attack rather than blindly sustain guard.
- Reuse `ACT-232`: commit authored dialogue replies retaining relevant flags.
- Reuse `ACT-341`: open reachable doors with the relevant key, inspect route
  records, activate the optional secret-room switch, release the cell and commit
  the boat interaction; source-qualified tripwire disarm shares this contextual
  action rather than creating a trap noun gene.
- Reuse `ACT-383`: hold sustained eligible guard; stamina/hand legality remains
  distinct from possession of a shield.
- Reuse `ACT-419`: accept the close critical-action prompt while a live target
  remains in its reachable stun window, without asserting guaranteed death.
- Reuse `ACT-425`: time the eligible parry after its ability is learned, not as an
  unconditional starting move.
- New `ACT-692`: switch the complete prepared hand pair with Y during live
  control, retaining the inactive preparation rather than buying new equipment.
- New `ACT-693`: confirm an affordable reset of a declared point group.
- Claim IDs: AV-003–AV-011, AV-014.

### System Behaviour Genes

- Reuse `SYS-057`: a perceiving hostile leaves its local idle/search behavior
  to pursue the visible player; exact visibility thresholds are not measured.
- Reuse `SYS-215`: directly commanded player attacks, hostile attacks, typed
  damage, guarded impacts and contextual stealth damage resolve in real time.
- Reuse `SYS-251`: authored quest access and final boat advance the route.
- Reuse `SYS-299`: encounter experience crosses level thresholds and awards
  attribute/ability allocation authority.
- Reuse `SYS-369`: terminal failure permits restoration of an eligible retained
  authored save/checkpoint rather than keeping transient failed positions;
  native reproduction and exact trigger timings remain unmeasured.
- Reuse `SYS-407`: Garryck and freed Ilora autonomously fight alongside the
  controlled character inside the admitted tutorial horizon.
- Reuse `SYS-409`: separate stun accumulation reaches a threshold and exposes a
  temporary critical-action opening; the target's health remains separate.
- Reuse `SYS-453`: equipped items, attributes and learned passives derive current
  combat commands and statistics; a book granting spells is already inside this
  boundary, not a new book-shaped ability system.
- Reuse `SYS-578`: retained personal health receives damage/restoration; its
  zero-health transition is qualified by the eligible Second Wind alternative.
- Reuse `SYS-755`: sufficient eligible damage breaks boards/floors or burns
  brambles, exposing the local route or object. Fire-pod shooting and a book's
  fire spell are different commands supporting typed destruction, not new genes
  for the same bramble geometry.
- New `SYS-1416`: selected melee/guard commands spend recovering stamina;
  do not import `SYS-798`'s requirement that every evasion is stamina-priced.
- New `SYS-1417`: food restoration can remain banked beyond current
  fullness and settle later at a combat-qualified rate; it neither increases
  maximum health like Valheim nor restores value through unfunded waiting.
- New `SYS-1418`: spell readiness and shared supplied essence both qualify
  casts. `SYS-1381`'s explicit absence of a shared expendable pool and
  `SYS-1365`'s default gradual magic restoration do not transfer unchanged.
- New `SYS-1419`: eligible Second Wind briefly incapacitates, recovers a
  permitted portion and starts recovery; another lethal event while unavailable
  fails the attempt. Initial eligibility is source-conflicted, not universal.
- New `SYS-1420`: paid reset removes one group's allocated effects,
  refunds its points and preserves earned level.
- Resolution order: current route/quest flags and equipment → legal local
  movement, prepared-pair switch or commanded action → live combat/destruction
  and companion behavior → health/stun/resources and supplied recovery →
  experience/points, release-dependent actor role and route gates → eligible
  revival or failure/restore → Ralke clear, Adra dialogue, boat and dock control.
  No universal same-frame lethal-hit, stun, fire or revival ordering is measured.
- Claim IDs: AV-002–AV-013.

### Constraint Genes

- Reuse `CON-269`: acquired command, readiness, compatible resource and target
  must permit the selected cast; a displayed spell is not a free legal attack.
- Reuse `CON-270`: current points, level and prerequisites permit an allocation.
- Reuse `CON-282`: authored key, route, quest and guardian prerequisites govern
  progression, rather than a fully open regional route.
- Reuse `CON-304`: carrying weighted equipment above the current limit slows
  movement and prevents sprint; this is not a hard pickup capacity or proof
  that later stash services are available inside the tutorial.
- Reuse `CON-336`: retained physical release state gates Ilora's later allied
  participation; her hostile alternative is not an entirely separate game.
- Reuse `CON-337`: current matching attribute must meet a dialogue threshold.
  A background-only response is not recast as an attribute check.
- Reuse `CON-354`: current stamina and weapon recovery qualify eligible melee
  commands. Sharpness or finite normal-bow ammunition is not invented here.
- Reuse `CON-589`: critical action requires a still-live reachable stun window.
- Reuse `CON-737`: carried tools expose their active verbs only through the two
  assigned hand/action slots. The item's compatibility parameters require the
  grimoire in the offhand; possession and an inactive loadout do not add its
  spell input. This is not a new book-specific slot-capacity invariant.
- Reuse `CON-769`: compatible one-handed equipment can retain a separate shield;
  two-handed occupation does not permit an independent shield in the same hands.
- New `CON-783`: ordinary sustained guard requires empty/shield offhand;
  red-signalled attacks remain unblockable even in that equipment state.
- Scarce resources: missing health, current stamina, supplied essence, remaining
  consumables, earned point/currency budgets, load-dependent movement and
  revival readiness; precise capacity and service enablement remain qualified.
- Claim IDs: AV-003–AV-012, AV-015–AV-016.

### Information Genes

- Reuse `INF-119`: health, stamina, essence, pending-recovery circles, level,
  attributes and abilities are visible; circle stock is not present health.
- Reuse `INF-125`: map/quest interface identifies the current authored goals.
- Reuse `INF-128`: loot labels, quantities and equipment compatibility are
  inspectable before take/equip; no exact hidden generation schedule is revealed.
- Reuse `INF-148`: dialogue shows response/attribute context without exposing
  every downstream Ilora consequence.
- Reuse `INF-295`: current prompt exposes a reachable close critical opportunity.
- Reuse `INF-319`: telegraphed red attacks disclose an unblockable incoming event.
- Reuse `INF-334`: enemy stun accumulation is distinct from remaining health.
- No new information gene is required merely for a book icon or two resource
  circles within the existing current-character state boundary.
- Claim IDs: AV-004–AV-012.

### Objective Genes

- Reuse `OBJ-080`: complete the full tutorial's required access, defeat Ralke and
  cross the boat handoff into ordinary Paradis control. Optional loot, saving
  Ilora, maximising a build or killing every Xaurip are not the clear predicate.
- Failure: terminal lethal health loss when eligible recovery is unavailable;
  an optional branch changing combat participants does not itself fail escape.
- Claim IDs: AV-002, AV-009, AV-012–AV-013.

### Time Genes

- Reuse `TIM-003`: threats and attacks resolve through live continuous time;
  no player turn automatically freezes hostile activity.
- Reuse `TIM-007`: eligible retained saves permit a replacement continuation,
  qualified by unperformed native save/reload reproduction.
- Reuse `TIM-027`: tactical radial selection pauses live resolution before
  releasing commands back to live combat; available tutorial personal actions
  are not an invented later named-companion power tree.
- Claim IDs: AV-007, AV-012–AV-013.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Wreck route and compatible weapon loot | Take and equip item, resume control | Current hand attacks change; ownership alone is not active equipment | acquired commands | AV-003–AV-004 |
| Separate stored primary/offhand builds | Tap Y in live control | Entire active preparation changes, inactive pair remains retained | pair switch differs from slot editing | AV-004 |
| Blockable strike and shield/empty offhand | Sustain guard | Incoming impact is guarded subject to current defensive stamina | hand eligibility and priced defence | AV-005 |
| Book occupies offhand | Attempt ordinary guard | The book does not grant the shield's sustained defence | alternative preparation has a cost | AV-005–AV-006 |
| Red hostile attack cue | Dodge rather than rely on guard | Position/timing can avoid the otherwise unblockable strike | telegraph changes legal answer | AV-007 |
| Grimoire owned but inactive | Place it in active offhand and select spell | Its item spell set becomes available without prior Wizard purchase | equipment-granted acquisition | AV-006 |
| Book spell ready but insufficient essence | Request that spell | Readiness alone does not pay shared essence cost | independent eligibility tests | AV-006–AV-008 |
| Meter full and restorative food available | Consume finite food | Retained recovery can remain pending rather than overfill current meter | bank differs from immediate heal | AV-008 |
| Pending food recovery and missing health/essence | Let eligible live time run | Bank decreases as current value recovers; combat settlement is source-conflicted and may be zero | restoration must be funded | AV-008 |
| Missing essence with no supplied recovery | Merely wait | No baseline passive magic refill is assumed | rejects passive-magic transfer | AV-008 |
| Enemy stun threshold reached and target alive/reachable | Accept prompted critical action | Contextual damage resolves; guaranteed target death is not assumed | opening differs from health defeat | AV-007 |
| Ilora agrees to help but door still locked | Leave without physically unlocking it | Reply alone does not establish her release flag | stateful action differs from dialogue | AV-009–AV-010 |
| Ilora released with the prison key | Continue into boss encounter | Ilora participates as allied shooter | retained choice changes combat | AV-009 |
| Ilora left imprisoned | Continue into boss encounter | Written alternative has escaped hostile Ilora; boat remains reachable | adverse choice is not escape failure | AV-009 |
| Optional storeroom door locked | Obtain its key and open | Reach optional chest equipment without changing mandatory clear | access and optional reward | AV-003 |
| Reachable tripwire or optional secret-room fixture | Accept its contextual operation | Written disarm removes the trigger; secret switch opens local access without becoming the mandatory terminal | optional stateful fixtures | AV-014; S10 |
| Carried weighted equipment exceeds current limit | Attempt movement or sprint | Movement slows and sprint is unavailable; a visible stash prompt alone does not prove island service eligibility | load constrains live options | AV-015–AV-016 |
| Brambles obstruct route and valid fire source exists | Shoot nearby fire pod or use book's fire | Typed burning removes barrier, opening local access | command substitution into destruction | AV-003/006 |
| Encounter experience reaches level threshold | Allocate offered point | Build gains a legal selected effect | progression alters future options | AV-011 |
| Allocated group and affordable available reset | Confirm displayed reset | Debit price, return group points, retain level | paid reallocation differs from free reclaim | AV-011 |
| Zero health and eligible ready Second Wind | Let recovery resolve | Brief incapacity and partial restoration followed by cooldown | conditional revival, no finite-life stock | AV-012 |
| Lethal damage while revival unavailable | Accept eligible save restoration | Failed transient state is replaced by prior retained state | retry differs from local revival | AV-012–AV-013 |
| Ralke defeated and route reaches boat | Finish Adra/boat sequence | Sailing alone is followed by ordinary Paradis dock control | complete progression terminal | AV-002 |

## Strategic and experiential structure

- Local decision: retain defence with shield or expose book spells; choose
  stamina-priced pressure, telegraph-aware evasion and essence-funded casts.
- Medium-term planning: explore optional keys and gear, bank restorative food
  without confusing it with current survival, and release or abandon Ilora
  before her later allegiance changes the boss encounter.
- Long-term structure: initial level points and retained route state carry into
  the next authored region; no entire-campaign progression claim is made.
- Heuristics: inspect attack cues and hand state, spend recovery before becoming
  vulnerable, and distinguish a favourable reply from actually releasing a cell.
- Failure attribution: visible current resources, stun and red warnings support
  tracing combat failure. Undisclosed future Ilora behavior and conflicted
  Second Wind setup are not represented as fully predictable from the HUD.
- Player trust: no source screenshot, unmeasured preset, exact build or hidden
  formula is presented as a personally reproduced fact.
- Claim IDs: AV-003–AV-013.

## Replay and variation

- Alter equipment pairs, point allocation and approaches within authored local
  geometry; the release decision can change an actor's side in the same boss
  encounter. Not every spoken reply creates a new mechanical branch.
- No procedural route generation, universal loot seed or exact random schedule
  is established from a single walkthrough.
- Restoring an eligible save may allow a different continuation, but native
  comparison of both Ilora branches has not been performed.
- Claim IDs: AV-003–AV-013.

## Adjacent systems and history

- The publisher places Avowed in Eora, but common setting with Pillars of
  Eternity does not import turn-based combat, party creation or other rules.
- Later anniversary ancestry, difficulty and weapon additions are dated
  alternative rules, not silent additions to the February tutorial.
- Detailed mechanical neighbours must come from the complete deterministic
  prior-signature scan below, not a marketing genre list.
- Claim IDs: AV-001, AV-004–AV-013.

## Normalised genome

The typed front matter is the canonical 52-gene signature: fifteen actions,
fifteen system behaviours, eleven constraints, seven information genes,
one objective and three time genes. Forty-four transfers retain their existing
English boundaries; eight additions are reviewed in TAXONOMY_CHANGE_243.
No item, character, map, hidden preset or numerical cost is promoted to a gene.
The full decomposition above attributes each typed group to its claim ledger.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `505` (`GAME-0001`–`GAME-0505`).
- Exact genome matches: none.
- Tied near matches: `GAME-0213` — STAR WARS Jedi: Fallen Order (`17 / 63 = 0.269841`).
- Supported combination subsets: none.
- Scan date: 2026-10-06.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| GAME-0213, STAR WARS Jedi: Fallen Order | ACT-008, ACT-161, ACT-190, ACT-191, ACT-223, ACT-341, ACT-383; SYS-215, SYS-251, SYS-409; CON-269, CON-270, CON-282, CON-354; INF-119, INF-125; TIM-003 | Both use live authored traversal, attacks, eligible powers, guarding, evasion, stun and capability gates. Its Bogano packet instead teaches BD-1 Stims, attack-fed Force, Meditation rest/respawn and retained Wall Run before a recording terminal, excluding the optional boss. Avowed uses paired hand preparations, item-granted book spells, supplied essence/food banks, release-dependent Ilora and the mandatory Ralke-to-boat terminal; no Meditation enemy-reset or attack-fed Force model is imported. | Near 0.269841; sole positive non-exact maximum. The fraction is owned by this Corpus comparison section. |

## Taxonomy impact

- Eight additions and 44 unchanged English transfers;
  no prior canonical definition or game signature is authorised to change.
- Rejected transfers: automatic magic recovery SYS-1365; every-evasion stamina
  SYS-798; no-shared-pool spell recovery SYS-1381; guaranteed unaware-target
  neutralisation ACT-235; fixed-life SYS-911 and free Spark reset SYS-609.
- Operational counterexamples are owned by
  [TAXONOMY_CHANGE_243](../../../research/taxonomy-changes/TAXONOMY_CHANGE_243.md).

## Negative results

- No separate negative-result record: unsupported transfer candidates are
  rejected before admission, without changing a prior accepted claim.

## Delta summary

This ledger records the admitted corpus changes without replacing the full
scoped analysis or claiming external novelty.

## New facts

- [Observation | Corroborated | Medium] AV-004/006/008/009 distinguish complete
  equipment-pair switching, item-granted magic, food recovery banks and the
  release-dependent ally/hostile boss actor.

## New genes

- [Observation | Corroborated | Medium] Eight separately qualified operational
  boundaries; AV-008 retains conflicting recovery evidence and the reset/revival
  details remain Limited rather than silently promoted to direct native proof.
  No external novelty is claimed.

## New combinations

- No new combination is admitted: all 274 verified proper-subset checks fail.

## Taxonomy changes

- TAXONOMY_CHANGE_243 admits the eight new boundaries, retaining all earlier
  definitions and signatures without an inferred synonym merge.

## New questions

- Exact save trigger, native failure/retry and platform parity remain unmeasured;
  the inspected dated replay account now supports the retained-state boundary.
- Starting-island trap geometry is now actually sampled; the indexed disarm
  passage and independently inspected route support a contextual operation.
  Native trap damage, disabled camp-service invocation and exact February
  service eligibility remain unmeasured and qualified.
- Resolve initial Second Wind eligibility before claiming a universal default;
  retain conditional model and exact-parameter limits if the conflict persists.

## Next recommended game

- [Hypothesis | Limited | Medium] Approved original PlayStation 3 MotorStorm,
  GAME-0507, only after this full unit is accepted and committed.
- Information gain: terrain-sensitive racing and vehicle interaction differ
  from this live authored quest and equipment/resource packet.
- Backlog impact: preserve the approved platform/era sequence; no implicit
  push, public revision or deployment.
