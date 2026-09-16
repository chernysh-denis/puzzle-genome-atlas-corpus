---
game_id: GAME-0290
slug: lies-of-p
game_title: Lies of P
analysis_status: reviewed
reviewed: 2026-09-13
combination_ids:
  - COMB-0260
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-200
    - ACT-224
    - ACT-249
    - ACT-378
    - ACT-419
    - ACT-425
    - ACT-436
    - ACT-437
    - ACT-438
  system:
    - SYS-035
    - SYS-215
    - SYS-364
    - SYS-399
    - SYS-409
    - SYS-578
    - SYS-688
    - SYS-798
    - SYS-799
    - SYS-832
    - SYS-852
  constraint:
    - CON-282
    - CON-286
    - CON-324
    - CON-352
    - CON-354
    - CON-589
    - CON-604
  information:
    - INF-119
    - INF-142
    - INF-295
    - INF-318
    - INF-319
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Lies of P

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Product labels,
actors, quantities and timing windows parameterise the genes but do not enter
their canonical labels.

## Analysis scope

- Version / ruleset: current unmodified English Steam base product `1627720`,
  one-app package `877649`, official version `1.13.1.0` dated 2026-08-05 and
  public-branch Build ID `23560677`, checked 2026-09-13. The publisher's
  semantic version and the secondary public-build projection remain separately
  graded observations rather than an asserted binary mapping.
- Product boundary: the package contains only the base game. Overture app
  `2848330`, Prince of Krat Cosmetics Pack `2325281` and soundtrack app
  `1938420` are separate products and contribute no rule, object or artwork to
  this packet. The opening cannot reach Overture, whose official entry requires
  Chapter 9 and a repaired Hotel Stargazer.
- Platform, input and difficulty: English interface, Windows, keyboard and
  mouse, offline single player, fresh first playthrough. Select `Legendary
  Stalker`, the renamed original and current default difficulty, and do not
  change difficulty during the packet. The two easier settings introduced with
  the Overture-support update are excluded.
- Setup-only predecessor: start New Game and choose the balanced starting combat
  style and its supplied weapon. This fixes initial attributes and equipment as
  parameters; the choice itself adds no gene because no later reconfiguration
  or comparison is admitted before first control.
- Entry: accept first ordinary control inside Krat Central Station before the
  first hostile. Record health, stamina, Pulse Cell charges, current weapon
  durability and carried Ergo before moving.
- Primary decision loop: read local geometry, attack motion, personal meters,
  hostile health and temporary Fatal Attack cues; traverse the authored station
  and square; lock on, strike, roll, hold weapon guard or time a Perfect Guard;
  allocate one recovering stamina reserve across offence, evasion and defence;
  turn guarded damage into Guard Regain and recover it through safe counterhits
  before time or a later unguarded hit removes the bank; spend a Pulse Cell when
  its vulnerable use is safe, then earn progress toward one final charge by
  attacking after the ordinary stock reaches zero; maintain the active blade
  with the reusable Grinder before its durability reaches the broken state;
  activate and rest at Stargazers while accepting refill and ordinary-enemy
  repopulation; reclaim the single dropped-Ergo mark after death; drive a
  target's hidden stagger state to the white outlined window, land a charged
  attack and commit the exposed Fatal Attack; defeat Parade Master through its
  changed second-phase attack set; then give the door response required for
  ordinary Hotel Krat entry and activate the Hotel Stargazer.
- Positive terminal: Parade Master is defeated, the ordinary bridge and Hotel
  Krat door have been crossed, and the first Hotel Krat Stargazer is activated
  with continuing player control. The activated checkpoint and boss settlement
  define a reproducible successor state, but no local quit/load was available;
  this record replaces the selection hypothesis of a performed reload with an
  evidence-bounded terminal.
- Negative terminal: health reaching zero returns control at the last activated
  Stargazer, repopulates eligible ordinary enemies and stores current Ergo in
  one recoverable world mark. Another death before recovery replaces that mark
  and permanently loses its stored Ergo. A broken blade cannot be restored by
  the ordinary field Grinder and must be recovered through a Stargazer or an
  excluded compatible repair item.
- Included: direct traversal, sprint and stamina-priced roll; light, heavy and
  charged close attacks; selected-hostile lock-on; held weapon guard, Perfect
  Guard and Fury Attack response distinction; health, stamina, weapon
  durability and Pulse Cell stock; Guard Regain creation, attack recovery,
  timed decay and loss on replacement damage; combat-earned final Pulse Cell;
  reusable field Grinder maintenance; Stargazer refill and enemy reset; death,
  one dropped-Ergo mark and replacement loss; stagger threshold, white outline,
  charged stagger and Fatal Attack; named boss health, second-phase attack-set
  change, route gate and Hotel Stargazer terminal.
- Excluded: Overture and every DLC effect; the two easier difficulty settings
  and mid-packet difficulty changes; New Game Plus; later weapon assembly,
  handle alteration, weapon upgrade and special Grindstones; P-Organ and Quartz;
  later Legion Arms, Fable Arts as a separate resource loop, levelling beyond
  any incidental pre-Hotel option, merchants and broader inventory management;
  Specters, Wishstones, Gold Coin Fruit, records, side quests, alternate
  truth/lie consequences beyond the mandatory Hotel entry response, endings,
  later or optional bosses, achievements, downloadable attire, mods, online
  features, console/controller rules, screenshots, official artwork, video and
  audio evidence.
- Reproducible parameterisation: install English base app `1627720` from package
  `877649`, verify official version `1.13.1.0`, choose fresh New Game and
  `Legendary Stalker`, retain default keyboard and mouse input, and follow the
  ordinary written route. Demonstrate one roll, held guard, Perfect Guard,
  Guard Regain recovery, zero-stock Pulse Cell recharge, Grinder restoration,
  Stargazer rest, Ergo death-mark recovery and Fatal Attack before defeating
  Parade Master, entering Hotel Krat and activating its Stargazer. Damage,
  durability, Ergo, exact timings, hostile order, optional pickups and death
  count are parameters.
- Potential scoped modules: one later weapon-assembly packet, P-Organ
  progression, a Legion Arm/Fable Arts economy, Overture, one later guardian,
  one ending route or New Game Plus each requires its own version, entry, loop,
  terminal and evidence.
- Direct-play status: not conducted. No installed application, local save or
  Steam userdata for app `1627720` was available. Valve and NEOWIZ establish
  product, package, current version, difficulty and DLC boundaries. Current
  written route and mechanics references corroborate the tutorials, route,
  Parade Master and Hotel terminal. This is an evidence-backed reconstruction,
  not a claimed playthrough, entitlement or reload. No audiovisual source was
  opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `LOP-001` | Steam app `1627720` and one-app package `877649` identify the lawfully offered Windows base product separately from all three listed DLC or media apps | Confirmed | Direct | High | P1, P2 |
| `LOP-002` | NEOWIZ version `1.13.1.0` is the current official release, while the public branch projects Build ID `23560677` | Confirmed | Corroborated | High | P3, S1 |
| `LOP-003` | The 2025 support update added three changeable difficulty settings and left the original challenge as the default `Legendary Stalker`; Overture itself requires later Chapter 9 state | Confirmed | Corroborated | High | P4, S2 |
| `LOP-004` | The ordinary opening runs from Krat Central Station through its square and Cerasani Alley, Parade Master and the required Hotel entrance response to Hotel Krat | Observation | Corroborated | High | S3–S5 |
| `LOP-005` | Attacks, sprint, roll and weapon guard draw on one automatically recovering stamina reserve | Observation | Corroborated | High | S3, S6 |
| `LOP-006` | Held guard reduces rather than eliminates ordinary damage and banks the guarded share as visible Guard Regain recoverable through outgoing attacks | Confirmed | Corroborated | High | P5, S3, S6 |
| `LOP-007` | Guard Regain decays with time and a later unguarded hit removes the earlier bank before any newly guarded share is created | Observation | Corroborated | High | S6, S7 |
| `LOP-008` | A Perfect Guard at contact prevents ordinary health loss and applies greater stagger or weapon-destruction pressure than held guard | Confirmed | Corroborated | High | P5, S6 |
| `LOP-009` | A red Fury Attack rejects ordinary guard and dodge invulnerability but remains answerable by a correctly timed Perfect Guard or by leaving its hit region | Observation | Corroborated | High | S8, S9 |
| `LOP-010` | Weapon attacks and guards reduce the visible durability gauge; a held reusable Grinder action restores positive durability in live play, while Stargazer rest fully repairs the weapon | Observation | Corroborated | High | S10, S11 |
| `LOP-011` | Pulse Cells restore health from finite charges, Stargazer rest replenishes the base stock and attacks build one final charge when the stock is empty | Observation | Corroborated | High | S3, S12 |
| `LOP-012` | Qualifying pressure exposes a white stagger window; a charged attack then creates the short reachable Fatal Attack opportunity | Observation | Corroborated | High | S3, S13 |
| `LOP-013` | Stargazer rest restores declared resources, repairs the weapon and respawns eligible ordinary enemies | Observation | Corroborated | High | S3, S10 |
| `LOP-014` | Death returns to the last Stargazer with one recoverable Ergo mark, which a later death replaces | Observation | Corroborated | High | S3, S14 |
| `LOP-015` | Parade Master is the mandatory opening guardian, changes its attack set during the same encounter and opens the ordinary Hotel Krat route on defeat | Observation | Corroborated | High | S4, S5 |
| `LOP-016` | No local executable or save was available, so activation of the Hotel Stargazer is textually bounded and not represented as a performed reload | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: NEOWIZ, released 2023-09-18; current official version
  `1.13.1.0` dated 2026-08-05.
- Platform or physical form: lawfully offered English Windows Steam base app
  `1627720`, package `877649`; fresh offline New Game on `Legendary Stalker`.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-13:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=1627720&cc=ua&l=english),
    for title, app, developer, publisher, release, Windows support, adjustable
    difficulty, current offer and separate DLC app IDs.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=877649&cc=ua&l=english),
    for the one-app base package and its current Ukraine offer.
  - **[P3]** [NEOWIZ update notes 1.13.1.0](https://www.liesofp.com/en-us/news/update-notes-version-11310),
    for the current semantic version and 2026-08-05 date.
  - **[P4]** [official Overture launch patch notes](https://www.liesofp.com/en-us/news/launch-patch-notes-lies-of-p-overture),
    for the three changeable difficulty levels, separated Overture requirement,
    later boss-rematch modes and base-game quality-of-life boundary.
  - **[P5]** [official patch notes 1.3.0.0](https://www.liesofp.com/en-us/news/patch-notes-version-1-3-0-0),
    for Guard Regain, Perfect Guard destruction pressure and their separability
    from later P-Organ modifiers.
  - **[P6]** [official base-game page](https://www.liesofp.com/en-us/base-game),
    for the base product's Krat, weapon, Legion Arm and lie-choice framing.
- Corroborating textual sources, accessed 2026-09-13:
  - **[S1]** [SteamCMD public-branch projection](https://api.steamcmd.net/v1/info/1627720),
    for Build ID `23560677` and branch timestamps; secondary distribution data.
  - **[S2]** [VGC difficulty announcement](https://www.videogameschronicle.com/news/lies-of-p-is-getting-difficulty-options-to-make-the-soulslike-more-accessible/),
    for `Legendary Stalker` as the renamed original/default setting and the two
    added easier options.
  - **[S3]** [Krat Central Station written route](https://www.neoseeker.com/lies-of-p/walkthrough/Krat_Central_Station)
    and [station-square route](https://www.neoseeker.com/lies-of-p/walkthrough/Krat_Central_Station_Plaza),
    for opening order, tutorials, Pulse Cells, Guard Regain, Stargazer rest,
    stagger/Fatal Attack and ordinary enemy reset.
  - **[S4]** [Cerasani Alley written route](https://www.neoseeker.com/lies-of-p/walkthrough/Cerasani_Alley),
    for the checkpoint-to-Parade-Master route, encounter and Hotel approach.
  - **[S5]** [GameFAQs Chapter 1 route](https://gamefaqs.gamespot.com/ps5/321162-lies-of-p/faqs/80876/chapter-1-parade-master),
    for independent route order, Stargazer activation, Parade Master and the
    mandatory Hotel entrance response. Platform-specific controls are ignored.
  - **[S6]** [static Guard reference](https://lies-of-p.fandom.com/wiki/Guard),
    for held guard, stamina, Guard Regain, timed decay and Perfect Guard effects.
  - **[S7]** [Guard Regain discussion](https://steamcommunity.com/app/1627720/discussions/0/3887226396787874733/),
    for the later-damage bank-loss edge case, used only as corroboration.
  - **[S8]** [static Fury Attack reference](https://lies-of-p.fandom.com/wiki/Fury_Attack),
    for the red cue and ordinary-guard/dodge distinction.
  - **[S9]** [GameFAQs general mechanics](https://gamefaqs.gamespot.com/ps5/321162-lies-of-p/faqs/80876/general-suggestions),
    for independent Fury Attack and Perfect Guard corroboration.
  - **[S10]** [GameSkinny durability reference](https://www.gameskinny.com/tips/lies-of-p-how-to-repair-weapon-durability/),
    for the visible gauge, attack/guard degradation, reusable held Grinder,
    broken-state exception and Stargazer repair.
  - **[S11]** [God is a Geek repair reference](https://godisageek.com/2023/09/lies-of-p-how-to-repair-weapons/),
    for independent field-maintenance corroboration.
  - **[S12]** [static Pulse Cell reference](https://bannerlord.wiki/index.php/Pulse_Cell),
    for finite health-restoration charges and Stargazer refill; the combat-
    earned last charge is independently corroborated by S3.
  - **[S13]** [combat-command reference](https://samurai-gamers.com/lies-of-p/combat-control-guide/),
    for white stagger readiness, charged stagger and Fatal Attack sequence.
  - **[S14]** [death-and-Ergo reference](https://liesofp.wiki.fextralife.com/Death),
    for Stargazer return, one recoverable Ergo mark and replacement loss.
- Research record: **[R1]** local preflight on 2026-09-13 found no installed
  application, app manifest, local save or matching Steam userdata.
- Claim IDs: `LOP-001`–`LOP-016`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008` owns direct authored-route traversal; `ACT-161` light,
  heavy and charged close strikes; `ACT-200` the vulnerable Pulse Cell use;
  `ACT-224` deliberate Stargazer rest; `ACT-249` contact recovery of the active
  dropped-Ergo mark; `ACT-419` the exposed Fatal Attack; `ACT-425` timed Perfect
  Guard; `ACT-436` stamina-priced roll; `ACT-437` held facing-relative weapon
  guard; and `ACT-438` reversible hostile lock-on.
- Generalised `ACT-378` owns live reusable Grinder maintenance of the equipped
  close weapon without treating `Durability` and `sharpness` as different
  actions merely because the products label their cycling performance gauges
  differently.
- Rejected `ACT-131`: a Pulse Cell charge is replenishable at rest and through
  combat, not a permanently destroyed carried unit. Rejected `ACT-221`: the
  Grinder is field maintenance, not a safe-hub resource payment or upgrade.
  Claims: `LOP-004`–`LOP-015`.

### System Behaviour Genes

- Existing `SYS-215` owns direct real-time combat; `SYS-578` the continuous
  health pool; `SYS-798` the stamina reserve shared by attacks, roll, sprint and
  guard; `SYS-364` Stargazer refill and ordinary-enemy repopulation; `SYS-399`
  checkpoint return plus one recoverable Ergo mark; `SYS-409` stability
  threshold into a critical opening; and `SYS-799` Parade Master's retained
  encounter advancing into a changed attack phase.
- Existing `SYS-832` owns guarded damage becoming recoverable health and
  outgoing hits restoring it. Existing `SYS-852` owns its delayed decay and
  the later-damage replacement rule. Existing `SYS-035` owns combat-earned
  progress toward the single last Pulse Cell charge after the ordinary stock
  is empty.
- Generalised `SYS-688` owns attack/guard-driven reduction and live Grinder or
  checkpoint restoration of the close weapon's cycling maintenance gauge,
  including its broken-state performance and field-repair exception.
- Resolution order: position, facing and lock-on determine contact; an attack,
  roll, sprint or guard first tests and spends stamina; a held guard banks the
  reduced health share while a precisely timed guard prevents ordinary damage
  and adds hostile stability or weapon pressure; outgoing attacks can restore
  the bank and build the empty Pulse Cell; later time or damage removes the
  remaining bank; attacks and guards degrade weapon durability until Grinder
  maintenance or rest restores it; hostile stability crossing its threshold
  exposes charged-stagger and Fatal Attack windows; death returns to the
  Stargazer with one Ergo mark; Parade Master's phase and final defeat open the
  Hotel route. Claims: `LOP-005`–`LOP-015`.

### Constraint Genes

- Existing `CON-282` owns the authored Parade-Master and Hotel gate; `CON-286`
  the legal uninterrupted Pulse Cell and Grinder casts; `CON-324` the Perfect
  Guard timing window and Fury-response distinction; `CON-352` the single Ergo
  mark; `CON-354` stamina, maintenance and animation-recovery legality for
  weapon moves; `CON-589` the reachable temporary Fatal Attack opportunity;
  and `CON-604` sufficient stamina for roll, sprint and guard.
- Scarce resources are health, current Guard Regain, stamina, Pulse Cell
  charges, weapon durability, safe maintenance/heal openings, the single
  unrecovered Ergo mark and checkpoint-local progress. Exact values, windows
  and damage shares are parameters. Claims: `LOP-005`–`LOP-015`.

### Information Genes

- Existing `INF-119` exposes health, Guard Regain, stamina, Pulse Cell, Ergo,
  equipped weapon and durability; `INF-142` attack motion cues reactive timing;
  `INF-295` the temporary Fatal Attack opportunity; `INF-318` Parade Master's
  name and remaining health; and `INF-319` the red Fury classification that
  changes legal defensive responses.
- Rejected `INF-334`: the underlying hostile stability accumulation is hidden;
  only the later white readiness outline and contextual attack opportunity are
  exposed. Claims: `LOP-005`–`LOP-015`.

### Objective Genes

- Existing `OBJ-080`: defeat the mandatory route guardian and cross the opened
  progression threshold into the activated Hotel Stargazer state. Parade
  Master defeat alone, reaching the door without its required response or
  seeing the Stargazer without activating it is not success. Claims:
  `LOP-004`, `LOP-015`, `LOP-016`.

### Time Genes

- Existing `TIM-003`: traversal, hostile actions, stamina recovery, Guard
  Regain decay, healing and maintenance exposure, stagger windows and boss
  attacks advance continuously while player input remains live. Claims:
  `LOP-005`–`LOP-015`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh New Game has reached first Krat Central Station control | Traverse the ordinary exit route and engage one puppet | Continuous movement and authored gates lead toward the station-square Stargazer without changing the product boundary | exact entry and route | `LOP-004` |
| An ordinary eligible strike approaches and stamina remains | Hold weapon guard through contact | Damage is reduced, stamina and weapon durability are spent, and the guarded health share becomes visible Guard Regain | guarded-health bank | `LOP-005`–`LOP-007`, `LOP-010` |
| Guard Regain remains positive | Land an eligible outgoing weapon attack before expiry | Health is restored up to the remaining bank and health cap while weapon durability and hostile health change | attack-to-health exchange | `LOP-006`, `LOP-007` |
| Guard Regain remains positive but no eligible attack lands | Wait, or accept a later unguarded hit | The bank decays after its delay or is discarded by replacement damage | temporary recovery horizon | `LOP-007` |
| An eligible attack reaches contact | Press guard in the Perfect Guard window | Ordinary health loss is prevented and hostile stagger or weapon-destruction pressure increases | precise defence differs from held guard | `LOP-008` |
| A red Fury Attack is executing | Attempt ordinary guard or rely on roll invulnerability, then repeat with a Perfect Guard or leave the hit region | Ordinary defensive protection fails inside the hit region; correct Perfect Guard timing or spatial avoidance can prevent the hit | cue-selected defensive legality | `LOP-009` |
| The active weapon has positive but reduced durability | Hold the reusable Grinder action during a safe live interval | Durability rises while hostile time continues; the action can be abandoned when danger returns | field maintenance trade-off | `LOP-010` |
| Weapon durability reaches the broken state | Attempt the ordinary Grinder, then rest at a Stargazer | Field restoration is refused at the broken boundary; Stargazer rest fully repairs the weapon | distinct zero-state recovery | `LOP-010`, `LOP-013` |
| Health is below cap and a Pulse Cell charge remains | Complete one safe Pulse Cell use | One charge is spent and health rises up to its cap | bounded live restoration | `LOP-011` |
| Pulse Cell stock is empty | Land qualifying attacks without dying or resting | Progress accumulates until one final Pulse Cell charge becomes available; no second empty-stock charge is banked | performance-earned last charge | `LOP-011` |
| An activated Stargazer is reached | Rest | Health, base Pulse Cells and weapon durability restore while eligible defeated ordinary enemies repopulate | recovery versus route reset | `LOP-011`, `LOP-013` |
| Player health reaches zero with carried Ergo | Accept death, then reach the active mark before another death | Control returns at the last Stargazer and touching the mark restores its Ergo | recoverable failure | `LOP-014` |
| A prior Ergo mark remains unrecovered | Die again | The newer mark replaces the earlier one and its stored value is lost | single-mark constraint | `LOP-014` |
| A hostile's hidden stability crosses its threshold | Land a charged attack during the white outline, approach and commit Fatal Attack | The target is staggered and the contextual close attack resolves before recovery removes the opportunity | two-step critical opening | `LOP-012` |
| Parade Master remains alive near its authored phase boundary | Continue legal damage | The same sealed encounter advances to a changed attack set without resetting prior damage | retained boss phase | `LOP-015` |
| Parade Master is defeated | Cross the bridge, give the Hotel's required entry response and activate the Hotel Stargazer | The mandatory guardian and door gate remain settled and the successor checkpoint becomes available | evidence-bounded positive terminal | `LOP-004`, `LOP-015`, `LOP-016` |

## Strategic and experiential structure

- Local decision: roll away, hold guard and plan an immediate Guard Regain
  counterhit, risk a Perfect Guard, heal, repair, or spend stamina on another
  attack while reading the next motion and Fury classification.
- Medium-term planning: reach the next Stargazer with usable blade durability,
  Pulse Cells and recoverable Ergo; decide whether a safe opening is better
  spent on health, maintenance or charged stagger pressure.
- Long-term structure: the opening teaches the complete resource exchange
  before Parade Master tests it, then turns boss settlement and a required
  door answer into the first stable Hotel checkpoint.
- Common heuristics: avoid emptying stamina into a combo that removes both roll
  and guard; recover Guard Regain promptly; grind before the red durability
  boundary; use ordinary guard when timing confidence is low, but learn Perfect
  Guard for Fury pressure; save a charged attack for the white outline.
- Failure attribution: personal bars, attack motion, red Fury cue, white stagger
  outline, boss health and Ergo mark reveal why an option was available or why
  recovery was lost; hidden stability prevents exact threshold prediction.
- Player-trust factors: the field Grinder's broken-state exception and the
  empty-stock single Pulse Cell are explicit boundaries, not unlimited repair
  or healing. No reload outcome is inferred from storefront save support.
- Claim IDs: `LOP-004`–`LOP-016`.

## Replay and variation

- What changes between sessions: starting weapon parameters, optional pickups,
  hostile order, guard/roll mix, Perfect Guard accuracy, maintenance timing,
  Pulse Cell use, death count and carried Ergo.
- Randomness or procedural generation: the route, checkpoints, mandatory boss
  and Hotel gate are authored; hostile attack selection can vary without
  changing the response predicates.
- Multiple viable strategies: ordinary puppets can be bypassed or fought;
  guarded damage can be reclaimed aggressively or avoided through roll and
  spacing; Parade Master can be pressured through attacks, Perfect Guards and
  Fatal Attacks without requiring a single exact sequence.
- Typical replay motive: reach the boss with more health, Pulse Cells and blade
  durability, improve Perfect Guard timing and reduce death-mark exposure.
- Claim IDs: `LOP-004`–`LOP-015`.

## Adjacent systems and history

- DARK SOULS III shares the complete `COMB-0260` substrate: direct melee, one
  stamina budget, roll, guard, lock-on, checkpoint reset, one currency mark and
  a transforming required opening guardian. Lies of P adds weapon maintenance,
  Guard Regain, Perfect Guard, Fatal Attack and combat-earned last healing.
- Sekiro shares timed weapon defence and stability-to-critical pressure, but
  exposes Posture continuously, couples it to Vitality, requires sequential
  Deathblows and offers charged in-place Resurrection instead of stamina,
  weapon durability and a recoverable currency mark.
- Elden Ring shares checkpoint refill, stamina, stance break, critical attacks
  and rune recovery, but its open route, levelling, equipment, mount and summon
  systems are outside this compact linear opening.
- Dead Cells shares held/timed defence plus the same recoverable-health creation,
  attack recovery and expiry owners, but places them in a branching run without
  this checkpoint-mark, durability and boss-gate substrate.
- Monster Hunter: World shares reusable live weapon maintenance after attack-
  driven gauge degradation, but couples it to a timed hunt, target migration,
  supplies and faint allowance rather than a Stargazer route.
- Claim IDs: `LOP-004`–`LOP-015`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-200`, `ACT-224`, `ACT-249`, `ACT-378`, `ACT-419`, `ACT-425`, `ACT-436`, `ACT-437`, `ACT-438` | actor, weapon, attacks, Grinder and checkpoint names are parameters |
| System Behaviour | `SYS-035`, `SYS-215`, `SYS-364`, `SYS-399`, `SYS-409`, `SYS-578`, `SYS-688`, `SYS-798`, `SYS-799`, `SYS-832`, `SYS-852` | values, gains, loss rates, thresholds and phase timing are parameters |
| Constraint | `CON-282`, `CON-286`, `CON-324`, `CON-352`, `CON-354`, `CON-589`, `CON-604` | exact timing, reach, stock, durability and stamina costs are parameters |
| Information | `INF-119`, `INF-142`, `INF-295`, `INF-318`, `INF-319` | colours, icons, wording and display placement are parameters |
| Objective | `OBJ-080` | guardian, door response and successor checkpoint are parameters |
| Time | `TIM-003` | animation, recovery and decay timings are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `289` (`GAME-0001`–`GAME-0289`).
- Exact genome matches: none.
- Tied near matches: `GAME-0262` — DARK SOULS™ III (`23 / 39 = 0.589744`).
- Supported combination subsets: `COMB-0260`.
- Scan date: 2026-09-13.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0262` — DARK SOULS™ III | `ACT-008`, `ACT-161`, `ACT-200`, `ACT-224`, `ACT-249`, `ACT-436`, `ACT-437`, `ACT-438`, `SYS-215`, `SYS-364`, `SYS-399`, `SYS-578`, `SYS-798`, `SYS-799`, `CON-282`, `CON-286`, `CON-352`, `CON-354`, `CON-604`, `INF-119`, `INF-318`, `OBJ-080`, `TIM-003` | Both use the full shared-exertion, checkpoint-mark and transforming-guardian interaction. DARK SOULS III additionally requires a transferred/equipped route item, placed world instructions and ground-item disclosure. Lies of P instead adds Perfect Guard and attack cues, a hidden stagger-to-Fatal sequence, cycling blade maintenance, Guard Regain with timed/replacement loss, a combat-earned last healing charge and Fury response classification. | Near, `23 / 39 = 0.589744` |

- New genes: `none`.
- Classification result: `New combination of known genes`; `COMB-0260`
  becomes recurrent across two independently analysed games.
- Evidence and reasoning: all six type registries were scanned completely below
  their current maxima. Existing owners cover every admitted transition after
  `ACT-378` and `SYS-688` are generalised from product-local `sharpness` wording
  to the shared cycling close-weapon maintenance boundary.

### Preserved research notes

- New genes: `none`.
- Classification result: `New combination of known genes`; `COMB-0260`
  becomes recurrent across two independently analysed games.
- Evidence and reasoning: all six type registries were scanned completely below
  their current maxima. Existing owners cover every admitted transition after
  `ACT-378` and `SYS-688` are generalised from product-local `sharpness` wording
  to the shared cycling close-weapon maintenance boundary.

## Taxonomy impact

- Registry changes: generalise `ACT-378` and `SYS-688`; add this game as their
  second carrier. No lifecycle or earlier signature changes.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_068`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_068.md).
- Candidate terms affected: `weapon durability`, `Grinder` and `field weapon
  maintenance` route to the two active owners; no new candidate entry is left.

## Negative results

- Complete lower-ID Action scan rejects `ACT-131` because a Pulse Cell charge
  replenishes, `ACT-221` because no safe-hub payment or upgrade occurs, and
  `ACT-383` because `ACT-437` already owns the held facing-relative guard.
- Complete lower-ID System scan rejects `SYS-376` because Pulse Cell recovery is
  performance- or rest-driven rather than timed, `SYS-777` because it binds
  Resident Evil 4's own-knife wear to parry protection, and `SYS-836` because
  Guard Regain expires or is replaced rather than being partially eroded by a
  later hit. `SYS-832` plus `SYS-852` owns the complete recoverable-bank loop.
- Complete lower-ID Constraint scan rejects `CON-579` because this packet needs
  the live completion window already owned by `CON-286`; `CON-617` is narrower
  than the ordinary/Fury response relation covered by `CON-324` and `INF-319`.
- Complete lower-ID Information scan rejects `INF-334` because enemy stability
  is hidden until the white outlined readiness state owned by `INF-295`.
- Objective and Time scans retain `OBJ-080` and `TIM-003`. The all-combination
  scan finds only `COMB-0260` as a strict proper subset; no combination
  collision or unsupported claim remains.

## Delta summary

- New facts: one current base-product boundary; one reproducible station-to-
  Hotel opening; sixteen rules claims and sixteen transition rows.
- Reused genes: `36` — all admitted Action, System Behaviour, Constraint,
  Information, Objective and Time owners listed in the normalised genome.
- New genes: `0`.
- New combinations: `0`; existing `COMB-0260` gains a second carrier.
- Taxonomy changes: `1` — `TAXONOMY_CHANGE_068` generalises two labels without
  changing any earlier signature.
- Ukrainian review: all reused meanings verified; `ACT-378`, `SYS-688`, the
  complete game presentation and recurrent `COMB-0260` wording corrected;
  official names and identifiers retained with reason.

## New facts

- [Confirmed | Corroborated | High] Guarded health loss can become a temporary
  bank restored by counterattacks while Perfect Guard prevents that bank from
  being needed (`LOP-006`–`LOP-009`).
- [Observation | Corroborated | High] When ordinary healing stock is empty,
  continued combat can earn exactly one final replenishable charge
  (`LOP-011`).
- [Observation | Corroborated | High] The same reusable field-maintenance action
  transfers between `sharpness` and `Durability` labels when both gauges cycle
  through attacks and live grinding (`LOP-010`).

## New genes

- [Observation | Corroborated | High] No new genes; all 36 admitted mechanics
  reuse existing active boundaries.

## New combinations

- [Strong Pattern | Corroborated | High] No new combination ID;
  `COMB-0260` becomes recurrent through Lies of P and DARK SOULS III.

## Taxonomy changes

- [Confirmed | Corroborated | High]
  [`TAXONOMY_CHANGE_068`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_068.md)
  generalises `ACT-378` and `SYS-688` from `sharpness` wording to the shared
  close-weapon field-maintenance loop.

## New questions

1. Does another independently documented game combine attack-earned last-heal
   replenishment with guarded-damage recovery without the same checkpoint-mark
   substrate?
2. Which later Lies of P packet can isolate weapon assembly without importing
   P-Organ or special-Grindstone progression?

## Next recommended game

- [Confirmed | Direct | High] `GAME-0291` — Persona 5 Royal.
- Optimisation criterion: continue the fixed mechanic-contrast horizon with a
  calendar-driven turn-based JRPG after two real-time action packets.
- Expected information gain: test scripted calendar, resource-limited palace
  routing, turn economy, alert state and safe-room persistence against the
  existing role-playing corpus.
- Backlog impact: executes the third reserved unit of selection 018 without
  reordering any later game.

## Why this game

Lies of P is valuable because its opening proves that recognisable novelty does
not require new vocabulary. Its full stamina, checkpoint-mark and transforming-
guardian substrate exactly supports the earlier DARK SOULS III interaction,
while Guard Regain transfers from two very different combat games, last-heal
replenishment transfers from performance-supply systems and blade durability
transfers from a hunt's sharpening loop. The result improves recurrence and
comparison quality while keeping branded names, exact values and animation
timings as parameters.
