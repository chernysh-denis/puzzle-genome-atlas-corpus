---
game_id: GAME-0256
slug: bioshock-remastered
game_title: "BioShock™ Remastered"
analysis_status: reviewed
reviewed: 2026-09-05
combination_ids:
  - COMB-0235
  - COMB-0254
gene_ids:
  action:
    - ACT-008
    - ACT-131
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-199
    - ACT-341
    - ACT-431
  system:
    - SYS-112
    - SYS-208
    - SYS-215
    - SYS-216
    - SYS-222
    - SYS-380
    - SYS-578
    - SYS-749
    - SYS-790
  constraint:
    - CON-269
    - CON-282
    - CON-285
    - CON-402
    - CON-578
    - CON-579
    - CON-600
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-268
  objective:
    - OBJ-026
  time:
    - TIM-003
    - TIM-007
---

# Game: BioShock™ Remastered

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `409710`, explicitly the remastered executable sold in package `451`, public
  content Build ID `8552765`, built 2022-04-13 and published 2022-08-31, plus
  2K's current direct-launch state after complete launcher removal on
  2024-11-25; checked 2026-09-05. Build identity and timestamps are secondary
  distribution observations, not an invented publisher semantic version.
  Package `451` also contains original BioShock app `7670`; it is not analysed.
- Platform, input and difficulty: Windows, English interface and subtitles,
  keyboard and mouse, fresh local profile, `New Game`, `Medium`, default
  adaptive training, quest arrow and enabled Vita-Chambers. macOS, consoles,
  controller input, other difficulties and disabled Vita-Chambers are distinct
  packets.
- Entry: first ordinary retained swimming control after the opening crash
  video, before entering the lighthouse. Cinematic and menu inputs do not enter
  the admitted trace.
- Primary decision loop: follow the current goal and authored route; walk,
  crouch, jump, swim, search and collect; acquire the Wrench, Electro Bolt and
  Pistol; select and reload weapons; toggle between the current weapon and
  powered ability channels; aim a direct strike, shot or electrical effect;
  ration ammunition, EVE, EVE Hypos, First Aid Kits and health; stun a living
  hostile before a close strike, energise a compatible relay and propagate
  electricity through one connected pool to its eligible occupants; survive
  the final finite lockdown group and pass the opened bulkhead into the next
  loaded area.
- Positive terminal: enter the Medical Pavilion bulkhead after the final
  Welcome to Rapture pressure clears, allow the next area and its autosave to
  load, retain first ordinary Medical Pavilion control with the next goal state
  available, create a dedicated manual save, quit to the main menu and restore
  that state with `Continue` or `Load Game`. Do not activate, buy or hack the
  first Medical Pavilion machine.
- Negative terminal: health reaching zero with Vita-Chambers enabled revives
  the player at an eligible chamber in the same persistent area and does not
  complete the route. Insufficient ammunition, EVE or restorative stock narrows
  legal actions but is not a terminal. Reaching the bathysphere, acquiring a
  weapon or Plasmid, seeing the protected pair, triggering lockdown or merely
  touching the final bulkhead before the area-load/save/reload test is not
  positive settlement.
- Included: direct first-person traversal and swimming; contextual doors,
  containers, corpse searches and pickups; Wrench and Pistol combat, magazine
  reload and finite compatible ammunition; Electro Bolt, EVE cost, EVE Hypo
  refill, temporary direct disable, a compatible powered relay and the required
  conductive-water interaction; First Aid Kit use, health damage and recovery;
  the final finite hostile release and clearance-gated route; local HUD,
  objective, map and adaptive help; Vita-Chamber revival; save-anywhere,
  area-load autosave and the retained Medical Pavilion restore test.
- Excluded: original app `7670`; macOS-specific launcher paths and every console
  release; Survivor, Easy, Hard and disabled-Vita-Chamber variants; Director's
  Commentary, Museum of Orphaned Concepts and Challenge Rooms; all Medical
  Pavilion play after the retained terminal and every later area; hacking,
  security-camera alarms, controllable bots or turrets, vending and health
  machines, currency spending, alternate ammunition selection, weapon
  upgrading, crafting, research-camera progression, ADAM, Gatherer's Gardens,
  Plasmid/Gene Tonic loadout progression and the Little Sister decision; audio
  diaries, secrets, achievements, exhaustive loot, mods, cheats, debug tools,
  speedrun skips, later BioShock games and the whole franchise; screenshots,
  official art, third-party assets, video and audio.
- Reproducible parameterisation: install Steam app `409710` through package
  `451`, select English, keyboard/mouse, a fresh New Game and Medium with the
  stated defaults. From first swimming control, follow only the current route;
  acquire the Wrench, Electro Bolt and Pistol; use one direct Electro Bolt on a
  legal hostile before a Wrench strike, use the effect on the required relay
  and on the required occupied water pool, collect and spend at least one
  compatible finite combat resource where missing capacity permits, clear the
  final required group and perform the declared Medical Pavilion save/restore
  terminal. Exact route, aim, hostile order, damage, resource amounts, optional
  searches, save slot and completion time remain parameters.
- Potential scoped modules: one bounded Medical Pavilion route including the
  first hack; one disabled-Vita-Chamber ruleset; one declared Challenge Room;
  one later story area; original app `7670`; or one named non-Windows release
  each requires its own entry, decision loop, terminal and evidence review.
- Direct-play status: not conducted. Valve application/package data, the Steam
  product page, 2K's current launcher-removal notice and the publisher-linked
  Feral remastered manual establish lawful availability, exact product and
  build boundary, input, difficulty, weapon/Plasmid channels, EVE, resources,
  HUD, revival and save rules. Independent static written routes establish the
  exact admitted opening transitions. This is an evidence-backed rules
  reconstruction, not a claimed captured playthrough or entitlement. No video
  or audio was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BSR-001` | The current lawful Windows product is Steam app `409710`, exactly BioShock™ Remastered, while package `451` also contains excluded original app `7670` | Confirmed | Direct | High | P1–P3 |
| `BSR-002` | Public content Build `8552765` is the observed remastered distribution boundary, with the current executable launching directly after 2K launcher removal | Observation | Corroborated | High | P4, S1 |
| `BSR-003` | New Game exposes four difficulty choices and this packet fixes Medium with default keyboard/mouse control and enabled Vita-Chambers | Confirmed | Direct | High | P3 |
| `BSR-004` | Weapons and Plasmids occupy retained selections in distinct channels that toggle ownership of the primary input | Confirmed | Direct | High | P3 |
| `BSR-005` | Plasmids require visible finite EVE; compatible carried Hypos restore missing EVE while First Aid Kits restore missing Health | Confirmed | Direct | High | P3 |
| `BSR-006` | The scoped route supplies the Wrench, Electro Bolt and Pistol in authored order and teaches a direct electrical stun followed by close attack | Observation | Corroborated | High | S2, S3 |
| `BSR-007` | A compatible electrical effect opens the required relay-dependent route and propagates through the required water pool to eligible occupants | Observation | Corroborated | High | S2, S3 |
| `BSR-008` | Pistol fire uses finite compatible ammunition and a magazine reload while Wrench attacks do not spend ammunition | Confirmed | Corroborated | High | P3, S2 |
| `BSR-009` | The final authored lockdown releases a finite hostile group and preserves the Medical Pavilion route gate until required clearance | Observation | Corroborated | High | S2, S3 |
| `BSR-010` | The HUD and status surfaces expose Health, EVE, restorative stocks, ammunition, map, current position, goal and contextual help | Confirmed | Direct | High | P3 |
| `BSR-011` | Enabled Vita-Chambers revive ordinary death inside the persistent area rather than restoring a pre-failure checkpoint snapshot | Confirmed | Direct | High | P3 |
| `BSR-012` | Save is available at the current point, an area load creates an autosave, and Continue loads the most recent save | Confirmed | Direct | High | P3 |
| `BSR-013` | The Welcome to Rapture bulkhead loads Medical Pavilion as the immediate retained successor area | Observation | Corroborated | High | S2, S3 |
| `BSR-014` | The bounded opening joins exclusive weapon/ability channels, finite resource recovery and environmental electrical propagation to one retained area handoff | Strong Pattern | Corroborated | High | `BSR-004`–`BSR-013` |

## Basic data

- Release / origin: developed by 2K Boston, 2K Australia and Blind Squirrel,
  published by 2K; current Steam release date 2016-09-15. Feral Interactive is
  the macOS developer/publisher and supplies the remastered web manual used for
  cross-platform rules and default keyboard semantics.
- Platform or physical form: lawfully offered English Windows single-player
  Steam application `409710`; one fresh Medium opening-route packet.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; world topology and perspective; ordered
  dependency sequencing.
- Primary and official sources, accessed 2026-09-05:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=409710&cc=ua&l=english),
    for exact title, application identity, Windows support, single-player
    category, package relation, release date and current Ukraine availability.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=451&cc=ua&l=english),
    for lawful package `451`, its current Ukraine offer and the explicit union
    of original app `7670` with selected remastered app `409710`.
  - **[P3]** [publisher-linked BioShock™ Remastered web manual](https://www.feralinteractive.com/en/manuals/bioshockremastered/latest/steam/),
    for New Game entry, four difficulties, default keyboard/mouse controls,
    weapon/ammunition rules, Plasmids, EVE, weapon/Plasmid switching, HUD,
    items, adaptive help, Vita-Chambers, save-anywhere, area autosaves, map and
    Continue/Load. Its macOS launcher/path instructions are not imported into
    the Windows packet.
  - **[P4]** [2K Launcher complete-sunset notice](https://support.2k.com/hc/en-us/articles/34845053169939-2K-Launcher-Complete-Sunset),
    for the 2024-11-25 follow-up that removed the launcher and returned
    BioShock Remastered to direct game launch without changing saves.
  - **[P5]** [current Steam product page](https://store.steampowered.com/app/409710/BioShock_Remastered/?l=english),
    for current Windows product identity, single-player scope, developer and
    publisher, weapons/genetic-modification premise and the separately listed
    Museum, Challenge Rooms and Director's Commentary exclusions.
- Corroborating textual sources, accessed 2026-09-05:
  - **[S1]** [SteamDB public depots](https://steamdb.info/app/409710/depots/),
    for public Build `8552765`, Windows depot `409711`, build/public timestamps
    and the `BioshockHD.exe` distribution observation. SteamDB is not treated
    as the publisher.
  - **[S2]** [BioShock Wiki: Welcome to Rapture](https://bioshock.fandom.com/wiki/Welcome_to_Rapture),
    for the static first-control, Wrench, Electro Bolt, Pistol, direct-stun,
    powered relay, occupied-water, lockdown and Medical Pavilion transition
    route. Narrative, audiovisual and later-game claims are not imported.
  - **[S3]** [GameFAQs BioShock Remastered Welcome Center route](https://gamefaqs.gamespot.com/switch/286684-bioshock-remastered/faqs/81461/welcome-center),
    for independent static corroboration of the remastered opening order,
    required water interaction, finite pressure and Medical Pavilion bulkhead;
    Switch input glyphs and platform behaviour are not imported.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P5` and `S1`–`S3` under the declared app, build, input, difficulty,
  entry, exclusions and save/restore terminal; rules reasoning, not direct
  play.
- Claim IDs: `BSR-001`–`BSR-014`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly swim, walk, crouch and jump through the authored
  opening geometry; `ACT-161`: aim and commit a Wrench strike, Pistol shot or
  direct Electro Bolt against a reachable target; `ACT-164`: select the active
  acquired weapon; `ACT-183`: reload the Pistol magazine from compatible
  reserve.
- Existing wording-generalised `ACT-131`: consume one unit from a dedicated
  First Aid Kit or EVE Hypo stock into its immediate compatible meter effect;
  `ACT-199`: collect or equip reachable weapons, ammunition and resources;
  `ACT-341`: search or activate required bodies, containers, doors, relay and
  bulkhead.
- New `ACT-431`: toggle the shared primary input between retained current
  weapon and Plasmid channels. Selecting another member within either channel
  remains `ACT-164` or a later scoped module rather than part of this toggle.
- Product, weapon, ability, enemy, room, item and exact amount names remain
  game-scoped parameters. Claims: `BSR-004`–`BSR-010`, `BSR-013`.

### System Behaviour Genes

- Existing `SYS-208`: resolve Pistol aim, obstruction and body hit; `SYS-215`:
  resolve directly commanded Wrench, Pistol and electrical combat in real time;
  `SYS-380`: apply Electro Bolt's direct typed damage/control effect to an
  eligible live target; `SYS-578`: apply incoming damage and compatible item
  recovery to one continuous Health pool.
- Existing `SYS-112`: a compatible effect changes the authored relay and
  exposes its dependent route; `SYS-222`: contact with an eligible visible
  world item transfers compatible stock up to capacity; `SYS-749`: the settled
  final lockdown trigger releases its fixed finite hostile group; `SYS-216`:
  enabled Vita-Chambers revive ordinary death in the same persistent area under
  the scoped no-carried-loss rule.
- New `SYS-790`: when the emitted electrical effect reaches the required
  connected water region, propagate it to every eligible occupant currently in
  contact rather than resolving only the aimed point.
- Resolution order: current goal and local state expose the next route;
  traversal or interaction changes reach and inventory; the active channel
  owns the primary input; weapon or Plasmid legality checks ammunition/EVE and
  target; direct or medium-propagated effects resolve; damage, recovery and
  revival update personal state; finite lockdown clearance opens the bulkhead;
  loading the successor area writes the autosave that the terminal restores.
- Claims: `BSR-004`–`BSR-014`.

### Constraint Genes

- Existing `CON-269`: Electro Bolt requires a legal target, range and
  sufficient EVE; `CON-285`: Pistol fire and reload require compatible current
  weapon, magazine, reserve and action state; `CON-578`: Pistol fire consumes
  compatible finite ammunition and pickups cannot exceed its cap.
- Existing `CON-282`: lighthouse, bathysphere, weapon/Plasmid acquisition,
  relay, restaurant, water interaction, lockdown and bulkhead require authored
  predecessors; `CON-402`: the final route remains closed while any required
  member of the finite lockdown group remains active.
- Wording-generalised `CON-579`: a First Aid Kit or EVE Hypo may restore only
  its compatible below-cap meter while matching carried stock remains.
- New `CON-600`: only the current weapon or powered-ability channel may resolve
  the shared primary input; the inactive channel retains selection but cannot
  act until toggled.
- Scarce strategic resources: Health, EVE, EVE Hypos, First Aid Kits, Pistol
  magazine/reserve, safe position, active input channel, conductive occupancy,
  clearance state and retained save. Exact amounts and identities are
  parameters. Claims: `BSR-004`–`BSR-013`.

### Information Genes

- Existing `INF-073`: current weapon, ammunition and selected combat equipment
  are visible; `INF-119`: Health, EVE and both restorative stocks expose
  personal survival/ability state; `INF-115`: avatar-centred sight and visible
  effects expose only local hostiles and hazards without importing audio.
- Existing `INF-125`: map, current position, current goal and quest arrow expose
  the next authored route gate; `INF-268`: adaptive training, item help and
  progress-sensitive hints expose the current instruction without revealing
  the full future chain.
- Claims: `BSR-004`–`BSR-010`, `BSR-013`.

### Objective Genes

- Existing `OBJ-026`: make the authored path traversable, clear the final gate
  and reach the retained Medical Pavilion successor area.
- Success, evaluation and failure: success requires the next-area load,
  autosave and manual save/restore test; Vita-Chamber revival and resource
  exhaustion do not settle the packet; collectibles, achievements, optional
  systems and later-campaign outcomes are not objectives.
- Claims: `BSR-009`, `BSR-011`–`BSR-014`.

### Time Genes

- Existing `TIM-003`: traversal, attacks, hostile movement, damage, temporary
  disable and lockdown pressure continue in real time while inputs remain
  available.
- Existing `TIM-007`: save-anywhere and retained area autosaves allow a prior
  world state to be restored and continued through a different live action or
  resource sequence; this terminal checks restoration rather than claiming an
  explicit rewind mechanic.
- Claims: `BSR-004`–`BSR-013`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Medium New Game has completed the crash video | Accept first swimming control | The avatar begins in authored water outside the lighthouse with no later equipment imported | fixed entry | `BSR-001`, `BSR-003` |
| The Wrench lies on the required path | Collect it and select Weapon Mode | The close weapon becomes the current no-ammunition attack | authored acquisition and weapon channel | `BSR-006`, `BSR-008` |
| Electro Bolt is acquired and sufficient EVE remains | Toggle to Plasmid Mode and fire at the required compatible relay | The electrical effect spends EVE, changes the relay and opens its dependent route | channel/resource/fixture dependency | `BSR-004`, `BSR-005`, `BSR-007` |
| A living hostile is reachable with sufficient EVE | Fire Electro Bolt, toggle channel and strike | The direct typed effect temporarily disables the target before the legal close attack resolves | live cross-channel control | `BSR-004`–`BSR-006` |
| Health or EVE is below cap and matching stock remains | Use one First Aid Kit or EVE Hypo | One stock unit is spent and only its compatible missing meter rises to cap | bounded immediate restoration | `BSR-005`, `BSR-010` |
| The Pistol is selected with compatible reserve | Aim, fire and reload | A shot spends loaded ammunition, hit resolution applies, and reload transfers reserve into the magazine | finite weapon loop | `BSR-008` |
| Eligible hostiles occupy the required connected water pool | Emit Electro Bolt into the pool | The electrical result propagates through the compatible region to its current eligible occupants | environment as effect carrier | `BSR-007` |
| Final route lockdown is active and a required hostile remains | Move, toggle, attack or recover | Real-time pressure continues and the Medical Pavilion route remains closed | partial clearance is insufficient | `BSR-009` |
| The final required hostile settles | Allow the authored response to finish | The bulkhead route to Medical Pavilion becomes traversable | finite clearance opens route | `BSR-009` |
| The opened bulkhead is entered | Allow the next area to load | Medical Pavilion becomes the current retained area and an area-load autosave is written | positive terminal precursor | `BSR-012`, `BSR-013` |
| First Medical Pavilion control is retained | Save, quit, then Continue or Load | The same successor-area state and current goal are restored without activating its first machine | reproducible positive terminal | `BSR-012`, `BSR-013` |
| Health reaches zero before route settlement | Accept enabled Vita-Chamber revival | Control returns at an eligible chamber in the same persistent area and the packet remains incomplete | reproducible negative terminal | `BSR-011` |

## Strategic and experiential structure

- Planning horizon: preserve health, ammunition, EVE and the two restorative
  stocks across the next fixed combat pocket while retaining a fallback Wrench
  attack that spends neither ammunition nor EVE.
- Local tactics: choose which input channel should be active, whether a direct
  electrical disable justifies its EVE cost, when to reload or heal and when
  compatible water turns one cast into a multi-target environmental result.
- Medium-term structure: authored traversal and acquisition teach weapon,
  Plasmid and resource channels before the relay and occupied-water tests
  combine them, after which finite lockdown clearance admits a saved area
  transition.
- Failure attribution: visible Health, EVE, stocks, ammunition, current channel,
  local effects and goal state distinguish resource overspend, missed toggle,
  incompatible target, poor spacing and incomplete clearance.
- Player-trust factors: the same channel and compatibility rules apply to direct
  and environmental use; the fixed group closes; the bulkhead loads one named
  successor area; save/restore verifies persistence independently of arrival.
- Claim IDs: `BSR-004`–`BSR-014`.

## Replay and variation

- What changes between sessions: aim, path, hostile order, weapon/Plasmid
  timing, resource expenditure, optional searches, damage and manual-save point.
- Randomness or procedural generation: the admitted route, item acquisitions,
  relay, water region, lockdown and terminal are authored; live combat
  variation does not make the level procedural.
- Multiple viable strategies: use direct disable before close attack, spend
  finite Pistol ammunition, fall back to the Wrench, recover early or preserve
  restorative stock and exploit the required conductive region.
- Typical replay motive: another difficulty, disabled Vita-Chambers, optional
  exploration, achievements, Challenge Rooms and later-system combinations are
  real replay surfaces but excluded from this packet.
- Claim IDs: `BSR-003`–`BSR-013`.

## Adjacent systems and history

- Direct predecessors: original BioShock app `7670` shares much of the authored
  campaign but is a separate executable explicitly excluded from this record.
- Variants: Museum, Challenge Rooms and Director's Commentary are separately
  exposed current-package surfaces, not layers of the admitted story route.
- Similar games: DOOM (2016), Serious Sam HD: The First Encounter, Half-Life 2,
  Dishonored (2012), Fallout 4 and CONTROL Ultimate Edition.
- Important differences: this opening alternates mutually exclusive weapon and
  finite-EVE ability channels, then uses connected water as a typed-effect
  carrier. Enabled Vita-Chambers preserve area continuity instead of replacing
  the failed transient world with a checkpoint snapshot.
- Claim IDs: `BSR-001`–`BSR-014`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-341`, `ACT-431` | route, item, weapon, target, reload, interaction, channel |
| System Behaviour | `SYS-112`, `SYS-208`, `SYS-215`, `SYS-216`, `SYS-222`, `SYS-380`, `SYS-578`, `SYS-749`, `SYS-790` | relay, hit, combat, revival, pickup, typed effect, health, release, medium |
| Constraint | `CON-269`, `CON-282`, `CON-285`, `CON-402`, `CON-578`, `CON-579`, `CON-600` | EVE/target, gate order, weapon state, clearance, ammunition, restore, channel |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-268` | equipment, local state, resources, goal/map, help |
| Objective | `OBJ-026` | retained Medical Pavilion area |
| Time | `TIM-003`, `TIM-007` | live progression and branchable retained saves |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `255` (`GAME-0001`–`GAME-0255`).
- Exact genome matches: none.
- Tied near matches: `GAME-0245` — DOOM (2016) (`17 / 38 = 0.447368`).
- Supported combination subsets: `COMB-0235`, `COMB-0254`.
- Scan date: 2026-09-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0245` — DOOM (2016) | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-341`, `SYS-215`, `SYS-222`, `SYS-578`, `SYS-749`, `CON-282`, `CON-402`, `CON-578`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `OBJ-026`, `TIM-003` | DOOM's packet uses checkpoint replacement, armour and a stagger-finisher recovery exchange; BioShock adds magazine reload, persistent-world revival, instant carried Health/EVE restoration, mutually exclusive weapon/ability channels, finite ability reserve, typed direct control and environmental effect propagation, plus save-anywhere restoration | Near, `0.447368` |

### Preserved research notes

- New genes: `ACT-431`, `SYS-790`, `CON-600`.
- Classification result: `New gene`.
- Evidence and reasoning: the new boundaries isolate one live toggle between
  retained weapon and ability channels, its exclusive ownership of a shared
  primary input and connected environmental propagation of a typed effect.
  Plasmid, weapon, water, location, enemy and resource names remain parameters.
- Lower-ID scan: reuse direct navigation, instant consumable use, aimed combat,
  weapon selection/reload, item transfer, authored interaction, dependent
  fixture state, ranged hits, live combat, persistent-world revival, contact
  pickup, selected ability effects, continuous health, finite release, ability
  legality, authored order, weapon legality, clearance, ammunition, restorative
  legality, equipment/local/resource/map/help information, fixed location,
  real time and branchable retained saves. Wording-generalise `ACT-131` from a
  held slot to carried immediate-effect stock and `CON-579` from Health alone
  to one compatible missing Health or ability meter; all earlier reviewed
  signatures remain unchanged.

## Taxonomy impact

- Registry changes: add `ACT-431`, `SYS-790` and `CON-600`; wording-generalise
  `ACT-131` and `CON-579` with BioShock support while preserving every earlier
  signature and lifecycle state.
- Taxonomy-change record: none; the two wording edits preserve their accepted
  immediate-consumable and compatible-restorative legality boundaries rather
  than merging, splitting or changing lifecycle.
- Candidate terms affected: record accepted/rejected channel, restorative and
  environmental-propagation terms under `GAME-0256`.

## Negative results

- No direct play or entitlement claim; no video/audio evidence; no original-app
  union; no proof before the terminal for hacking, security-camera response,
  machine economy, ADAM choice, research, upgrades or later Plasmids; no whole-
  campaign, Collection or franchise signature.

## Delta summary

## New facts

- [Confirmed | Direct | High] The current Windows package contains distinct
  original and remastered apps, and the packet explicitly selects app `409710`
  under the current direct-launch state (`BSR-001`–`BSR-003`).
- [Confirmed | Corroborated | High] The fixed opening joins finite weapon/EVE
  resources, exclusive combat channels, electrical environment interaction and
  a save-verified next-area terminal (`BSR-004`–`BSR-014`).

## New genes

- [Confirmed | Corroborated | High] `ACT-431`, `SYS-790` and `CON-600` isolate
  the transferable dual-channel input and environmental-effect propagation
  boundaries.

## New combinations

- [Observation | Corroborated | High] `COMB-0254` captures the bounded
  resource/channel/environment route; existing `COMB-0235` recurs for its
  direct-combat, finite-release and clearance skeleton.

## Taxonomy changes

- [Observation | Corroborated | High] No lifecycle, merge, split or signature
  change; `ACT-131` and `CON-579` receive boundary-preserving transferable
  wording and new independent support.

## New questions

- Does Alien: Isolation's bounded opening reuse the same resource-gated
  authored survival route while replacing active powers and conductive effects
  with detection, hiding and threat avoidance?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0257` — Alien: Isolation.
- Optimisation criterion: compare another first-person authored survival route
  while isolating hiding, motion information and persistent-stalker pressure.
- Expected information gain: determine which resource, perception, gate and
  retained-terminal genes recur without importing BioShock's powered channel
  or environmental electricity.
- Backlog impact: advances the approved batch-014 ordered horizon.

## Why this game

- [Hypothesis | Limited | High] Alien: Isolation preserves embodied route and
  scarcity pressure while moving the central decision boundary from choosing a
  typed combat channel to controlling visibility, noise and concealment.
