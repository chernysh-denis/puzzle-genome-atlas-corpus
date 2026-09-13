---
game_id: GAME-0286
slug: doom-eternal
game_title: DOOM Eternal
analysis_status: reviewed
reviewed: 2026-09-10
combination_ids:
  - COMB-0235
  - COMB-0243
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-190
    - ACT-341
    - ACT-419
  system:
    - SYS-215
    - SYS-222
    - SYS-369
    - SYS-578
    - SYS-655
    - SYS-749
    - SYS-755
    - SYS-770
    - SYS-841
    - SYS-794
  constraint:
    - CON-269
    - CON-282
    - CON-402
    - CON-578
    - CON-589
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-295
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: DOOM Eternal

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `782330`, installed through `DOOM Eternal Standard Edition` package `235874`
  on the default public branch, whose secondary SteamCMD projection reports
  Build ID `24695697`, updated 2026-09-04 17:21:49 UTC; checked 2026-09-09.
  Bethesda's latest numbered PC note is Update 6.66 Rev 3 from 2024, while its
  2025 mod update and the later observed build do not publish a semantic
  version mapping. The packet is therefore identified by branch and build, not
  falsely labelled `6.66 Rev 3`.
- Entry: choose a fresh base Campaign slot and `Hurt Me Plenty`, then accept
  first direct control in the opening Hell Barge room with the Combat Shotgun.
  No completed save, replay equipment, cheat or account-derived modifier enters
  the packet.
- Primary decision loop: read the objective, local geometry, health, armour,
  weapons, ammunition, Chainsaw fuel and transient stagger cues; run, strafe,
  double-jump, swing, climb marked walls and mantle; select, aim and fire the
  Combat Shotgun or Heavy Cannon; destroy a dangerous located body component
  when the positional cost is worthwhile; Glory Kill a reachable staggered
  hostile for health or spend sufficient Chainsaw fuel on an eligible target
  for ammunition; collect compatible drops and world pickups; break marked
  route objects, use the yellow keycard and clear each finite Demon Gate before
  following the waypoint to the terminal elevator.
- Positive terminal: after the final required Earth encounter is cleared,
  enter and activate the authored elevator, let the `Hell on Earth` mission
  completion transition settle, and reach first controllable state in the
  retained Fortress of Doom hub. The following Flame Belch acquisition and
  `Exultia` launch are outside the packet.
- Negative terminal: health reaching zero ends the current attempt. Choosing
  `Load Checkpoint` restores the latest authored Campaign checkpoint rather
  than preserving the failed position, damage, ammunition, hostile or gate
  state. Resetting the whole mission remains an alternative, not the ordinary
  retry used by this record.
- Included: direct first-person movement and marked traversal; Combat Shotgun
  and Heavy Cannon fire; finite typed ammunition and contact pickups; health
  and armour loss/recovery; Glory Kill health conversion; Chainsaw fuel,
  automatic one-segment recovery, larger fuel pickups and ammunition
  conversion; the Arachnotron turret as a destructible capability component;
  breakable green route objects; yellow-keycard access; finite combat releases,
  clearance gates, objective/Automap guidance, checkpoint retry and the
  mission-to-Fortress settlement.
- Excluded: The Ancient Gods, Master Levels, Horde Mode, BATTLEMODE, events,
  boosters and account XP; Extra Life and Ultra-Nightmare rules, mission replay,
  cheats, Empowered Demons and mods; secrets, toys, Codex collection, Slayer
  Gates, fast-travel cleanup, Automap completion and upgrade optimisation;
  alternate difficulties and platforms; Dash, Blood Punch, Ice Bomb, Crucible,
  BFG, later weapons, later campaign systems and all later missions. Mod Bot
  choices, weapon-mod use and Frag Grenade use are optional route variation and
  are not admitted to the signature. Flame Belch and its armour conversion are
  explicitly second-mission mechanics.
- Reproducible parameterisation: use the English Windows public Steam branch,
  package `235874`, a clean Campaign slot, `Hurt Me Plenty` and default
  mouse/keyboard controls. Follow only the main waypoint from the Hell Barge,
  take the required Chainsaw and Heavy Cannon, use the yellow keycard, clear
  every route-blocking encounter and activate the final elevator. Weapon-mod,
  grenade, secret and collectible interactions are skipped. Aim, target order,
  exact pickups, recovery choices and completion time remain run parameters.
- Potential scoped modules: one verified Mod Bot choice; one Slayer Gate; one
  later Campaign mission introducing Flame Belch; one Master Level; one Horde
  run; or one current BATTLEMODE ruleset each requires a separate build, entry,
  terminal and evidence contract.
- Direct-play status: not conducted. Valve application/package data establish
  lawful current Windows availability; the SteamCMD projection supplies the
  observed branch build. Bethesda product, support, update and campaign
  materials establish the product split, resource loop, difficulty and
  checkpoint rules. GameSpot and GamePressure independently constrain the
  complete first-mission transitions and Fortress successor. This is an
  evidence-backed rules reconstruction, not a claimed captured playthrough.
  No video or audio was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DE-001` | The admitted product is id Software's base Windows `DOOM Eternal`, Steam app `782330` through Standard package `235874` | Confirmed | Direct | High | P1, P2 |
| `DE-002` | The default public branch is projected as Build ID `24695697`, updated 2026-09-04 17:21:49 UTC; no publisher semantic version is mapped to it | Observation | Corroborated | High | P3, P4, S1 |
| `DE-003` | Campaign is an installable product surface distinct from expansions, Master Levels, Horde Mode and BATTLEMODE | Confirmed | Direct | High | P1, P2, P5 |
| `DE-004` | A fresh `Hurt Me Plenty` Campaign begins `Hell on Earth` with the Combat Shotgun and acquires the Chainsaw before the first main arena | Observation | Corroborated | High | P6, S2, S3 |
| `DE-005` | Glory Kills restore health, Chainsaw kills restore ammunition, and Flame Belch armour conversion is unavailable until mission two | Confirmed | Direct | High | P1, P6, P7 |
| `DE-006` | The Chainsaw's standard reserve automatically recovers one of three segments while larger eligible targets require fuel gained from finite cans | Confirmed | Corroborated | High | P7, S2, S3 |
| `DE-007` | Aimed damage can destroy the Arachnotron's turret and remove its long-range attack while the hostile remains alive | Observation | Corroborated | High | S2, S3 |
| `DE-008` | Marked climbing, double jumps, bars, breakable route objects and a yellow access card form required traversal transitions | Observation | Corroborated | High | S2, S3 |
| `DE-009` | Required combat spaces keep their forward gate closed until the current finite hostile set is cleared | Confirmed | Corroborated | High | P8, S2, S3 |
| `DE-010` | Health, armour, ammunition, fuel, active weapon, objective, map elevation and stagger cues expose the bounded decision state | Observation | Corroborated | High | P6–P8, S2, S3 |
| `DE-011` | `Load Checkpoint` restores an earlier authored Campaign state after failure or a blocked Demon Gate | Confirmed | Direct | High | P8 |
| `DE-012` | Activating the final elevator completes `Hell on Earth` and transitions to the Fortress of Doom hub before `Exultia` | Observation | Corroborated | High | S2–S4 |

## Basic data

- Release / origin: id Software / Bethesda Softworks, March 2020. The scoped
  product is `DOOM Eternal`, not DOOM (2016), DOOM: The Dark Ages or an
  expansion campaign.
- Platform or physical form: lawfully available English Windows Steam
  distribution, application `782330`, Standard package `235874`; no local
  entitlement or direct play is claimed.
- Puzzle family: real-time tactical counterplay, finite combat-resource routing,
  world topology and ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-09:
  - `P1` — [Steam product](https://store.steampowered.com/app/782330/DOOM_Eternal/)
    and Valve application metadata, for product identity, developer/publisher,
    Windows support, single-player Campaign and the advertised resource loop.
  - `P2` — [Valve package metadata](https://store.steampowered.com/api/packagedetails?packageids=235874&cc=ua&l=english),
    for `DOOM Eternal Standard Edition` containing app `782330`.
  - `P3` — [Bethesda, Update 6.66 Rev 3](https://bethesda.net/en-US/news/doom-eternal-update-6-66-rev-3-release-notes),
    for the latest located numbered update and its limited 2024 changes.
  - `P4` — [Bethesda, PC Mods Update](https://slayersclub.bethesda.net/en-US/news/doom-eternal-pc-mods-update),
    for the later 2025 launcher separation between the standard unmodified
    retail game and the separately selected modded path.
  - `P5` — [Bethesda Support, Campaign installation](https://help.bethesda.net/app/answers/detail/a_id/49864/),
    for the separately named Campaign component on Steam.
  - `P6` — [Bethesda Support, health and ammunition](https://help.bethesda.net/app/answers/detail/a_id/49879/~/why-do-i-keep-running-out-of-health-and-ammo-in-doom-eternal%3F),
    for scarce world resources, stagger/Glory Kill health, Chainsaw ammunition
    and Flame Belch's second-mission boundary.
  - `P7` — [PlayStation Blog, first-hours tips](https://blog.playstation.com/2020/03/19/doom-eternal-essential-tips-to-survive-the-first-few-hours/),
    an official platform-holder account for `Hurt Me Plenty`, checkpoint reload,
    the three execution-to-resource classes and one-of-three fuel recovery.
  - `P8` — [Bethesda Support, objective and Demon Gate recovery](https://help.bethesda.net/app/answers/detail/a_id/49889/~/what-do-i-do-if-i-cant-progress-in-an-objective-in-doom-eternal),
    for map elevation, Demon Gate clearance and `Load Checkpoint`.
- Corroborating textual sources, accessed 2026-09-09:
  - `S1` — [SteamCMD public-branch projection](https://api.steamcmd.net/v1/info/782330),
    for Build ID `24695697` and Unix timestamp `1788542509`.
  - `S2` — [GameSpot, Hell on Earth walkthrough](https://www.gamespot.com/articles/doom-eternal-mission-1-walkthrough-hell-on-earth/1100-6474897/),
    for the complete weapon, traversal, arena, weak-point, keycard, elevator and
    Fortress route.
  - `S3` — [GamePressure, Hell on Earth walkthrough](https://www.gamepressure.com/doom-eternal/hell-on-earth-walkthrough/zdd15c),
    for an independent written route and the visible fuel state.
  - `S4` — [Doom Wiki, Hell on Earth](https://doom.fandom.com/wiki/Hell_on_Earth_%28Doom_Eternal_level%29),
    for the objective list, exit portal and Fortress successor only.
- Claim IDs: `DE-001`–`DE-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly run, strafe, jump, double-jump, swing from bars,
  climb marked walls and mantle through the fixed first-mission geometry.
- Existing `ACT-161`: aim and fire the current weapon at a reachable hostile or
  marked breakable route object; exact weapons, components and damage are
  parameters.
- Existing `ACT-164`: switch between the carried Combat Shotgun and Heavy
  Cannon without inventing a reload cycle.
- Existing `ACT-190`: commit the available targeted Chainsaw capability against
  an eligible reachable hostile.
- Existing `ACT-341`: activate authored doors, the matching keycard gate and
  the terminal elevator when their predicates are satisfied.
- Existing `ACT-419`: commit a prompted close Glory Kill while a reachable
  hostile remains staggered.
- Rejected new traversal Actions: `ACT-008` already admits local jump and
  surface-dependent movement, as demonstrated by the lower-ID Titanfall 2
  carrier. Rejected `ACT-183`: these weapons have no admitted magazine reload.
  Rejected Mod Bot and grenade actions because their optional use is excluded.
- Claims: `DE-004`–`DE-012`.

### System Behaviour Genes

- Existing `SYS-215`: resolve hostile movement, projectiles, weapon hits,
  damage, stagger, capability loss and defeat in live first-person combat.
- Existing `SYS-222`: contact transfers compatible ammunition, health and
  armour world items toward their bounded personal caps.
- Existing `SYS-369`: replace failed transient Campaign state with the latest
  authored checkpoint when the player selects `Load Checkpoint`.
- Existing `SYS-578`: incoming damage and compatible recovery alter one
  continuous health pool whose zero ends the current attempt.
- Existing `SYS-655`: armour absorbs eligible damage before health and can be
  restored separately by compatible world pickups.
- Existing `SYS-749`: crossing authored encounter triggers releases finite
  hostile groups into the current combat space.
- Existing `SYS-755`: sufficient compatible damage removes marked breakable
  route objects while leaving living-hostile defeat to combat.
- Generalised `SYS-770`: either a legal Glory Kill or a fuel-paid Chainsaw
  execution defeats its target and creates compatible world recovery drops;
  the action and legality predicates remain separate genes.
- New `SYS-841`: automatically replenish the segmented Chainsaw reserve only
  to its guaranteed one-segment floor; finite fuel cans are required to raise
  it above that floor toward its three-segment cap.
- Reused `SYS-794`, generalised by `TAXONOMY_CHANGE_064`: destroying a located
  attached hostile component disables the capability it carries while the
  hostile body remains alive and can continue its reduced combat cycle. The
  Arachnotron's mounted turret is a component parameter, not a separate System
  boundary.
- Resolution order: accept the fresh Campaign entry; integrate traversal and
  live combat; apply weapon/ammunition and layered survival state; expose
  stagger, fuel and components; resolve chosen ordinary fire, Glory Kill or
  Chainsaw exchange; collect compatible drops; restore the guaranteed fuel
  floor; settle breakables, interactions, finite releases and clearance; save
  authored checkpoints; settle the elevator and retained hub successor.
- Rejected `SYS-376`: it restores spent reusable health-item or grenade charges
  to their full count, whereas this reserve has a partial automatic floor and
  finite world stock above it. Rejected `SYS-347` and `INF-139`: their ARC
  perception/attention compounds exceed a player-destroyed demon component.
- Claims: `DE-005`–`DE-012`.

### Constraint Genes

- Existing `CON-269`: Chainsaw use requires an acquired capability, reachable
  eligible target and enough current fuel; target class and segment cost are
  parameters rather than a demon-named gene.
- Existing `CON-282`: first-mission rooms, breakables, encounters, keycard,
  elevator and locations must satisfy their authored predecessor predicates.
- Existing `CON-402`: a Demon Gate remains closed until every required member
  of its finite current hostile set is defeated.
- Existing `CON-578`: an ammunition-consuming weapon may fire only while its
  compatible finite reserve can pay the shot, and pickups cannot exceed cap.
- Existing `CON-589`: Glory Kill is legal only during the living, reachable,
  short stagger opportunity; Chainsaw legality does not inherit this predicate.
- Rejected a new Chainsaw constraint because lower-ID `CON-269` already owns
  target, range, resource and readiness jointly. Rejected `CON-285`: no
  magazine/reload state enters the packet. Scarce resources are health, armour,
  compatible ammunition, Chainsaw fuel, stagger time, safe space and retained
  checkpoint progress.
- Claims: `DE-004`–`DE-012`.

### Information Genes

- Existing `INF-073`: carried weapons, active weapon and compatible ammunition
  are visible before attack or switch.
- Existing `INF-115`: avatar-centred sight and visible effects expose only
  locally perceived hostiles, projectiles, components and hazards; no audio
  evidence is used.
- Existing `INF-119`: health, armour, Chainsaw fuel and current personal combat
  readiness are visible before resource decisions.
- Existing `INF-125`: current objective, discovered Automap region, waypoint,
  gate and elevation are inspectable before route choice.
- Existing `INF-295`: a transient visual change identifies a living hostile's
  current Glory Kill opportunity.
- Rejected a new weak-point Information gene: the scoped sources establish a
  visible anatomical component and tutorial knowledge, but not a distinct
  portable interface state beyond local sight and the general objective/help
  surfaces. Enemy and component names remain parameters.
- Claims: `DE-005`–`DE-012`.

### Objective Genes

- Existing `OBJ-026`: make the authored route traversable and reach/activate
  its designated elevator so the retained Fortress successor loads.
- Success and failure: elevator settlement and first controllable hub state are
  positive; health zero plus checkpoint retry closes only the failed attempt;
  secrets, score, mission challenges and full-Campaign completion are not
  objectives.
- Rejected `OBJ-166`: not every hostile in the mission is the declared terminal
  set, and the final command is spatial elevator activation rather than hostile
  elimination itself. Claims: `DE-008`–`DE-012`.

### Time Genes

- Existing `TIM-003`: movement, projectiles, hostile attacks, stagger windows,
  fuel recovery and damage continue in real time while the player supplies
  input. Menus and loading do not create another decision clock.
- Rejected a new Time gene: the one-segment fuel recovery is a System reserve
  rule under the same continuous clock. Claims: `DE-005`–`DE-011`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Campaign and `Hurt Me Plenty` are selected | Accept first direct control | `Hell on Earth` starts in the Hell Barge with the Combat Shotgun and no replay loadout | fixed entry | `DE-003`, `DE-004` |
| The route reaches the Chainsaw tutorial with an eligible fodder hostile | Commit the targeted Chainsaw capability | Required fuel is paid, the target is defeated and compatible ammunition drops enter the world | fuel-for-ammunition exchange | `DE-005`, `DE-006` |
| Chainsaw fuel is below one segment | Continue live play without taking a fuel can | The reserve recovers only to one segment and stops; world fuel is required above that floor | guaranteed floor differs from full stock | `DE-006` |
| A living hostile is visibly staggered and reachable | Commit the prompted Glory Kill | The target is defeated and compatible health recovery enters the world | stagger-for-health exchange | `DE-005`, `DE-010` |
| An Arachnotron remains alive with its turret intact | Aim and apply enough damage to the turret | The turret breaks and its long-range attack is disabled while the body remains an active hostile | component loss differs from defeat | `DE-007` |
| A marked wall or route object blocks progress | Jump into and climb the marked surface, or strike the marked breakable | The local geometry becomes traversable without granting free-form climbing or destruction | authored traversal vocabulary | `DE-008` |
| A finite encounter still has required hostiles | Move, fire or use an eligible recovery execution | Live combat continues and the Demon Gate remains closed | partial clearance is insufficient | `DE-009` |
| The last required hostile is defeated | Allow encounter settlement | The corresponding Demon Gate opens and exposes the next route segment or weapon | finite clearance gate | `DE-009` |
| The yellow access card is held at its matching gate | Activate the gate | The authored barrier opens and the subway route becomes reachable | typed route dependency | `DE-008` |
| Health reaches zero before mission settlement | Choose `Load Checkpoint` | Failed transient state is replaced by the latest authored Campaign checkpoint | reproducible negative terminal | `DE-011` |
| The final elevator is reachable after required Earth encounters | Activate it and allow the transition to settle | `Hell on Earth` completes and first controllable Fortress of Doom state loads | reproducible positive terminal | `DE-012` |

## Strategic and experiential structure

- Planning horizon: preserve enough health, armour, ammunition, fuel and safe
  space for the next authored arena while knowing one fodder-priced Chainsaw
  conversion remains recoverable but larger executions consume finite cans.
- Local tactics: stay mobile, remove a dangerous component when its continued
  attack would cost more than immediate body damage, choose ranged defeat or a
  risky Glory Kill for health, and reserve the Chainsaw for the ammunition
  state and target class that justify its fuel cost.
- Medium-term structure: marked traversal and breakables alternate with finite
  releases, resource conversion, clearance gates, a keycard route and the final
  mission-to-hub transition.
- Failure attribution: personal meters, weapon/ammunition state, fuel segments,
  local projectiles, component state, stagger cues and waypoint/gate feedback
  distinguish aim, spacing, resource-routing and navigation errors.
- Player-trust factors: each execution method always maps to its declared
  resource class; the one-segment fuel floor is stable; destroyed components
  stop their attached attack; complete clearance opens the matching gate; and
  checkpoint restore replaces failed transient state.
- Claims: `DE-005`–`DE-012`.

## Replay and variation

- What changes between attempts: aim, movement route, target order, ammunition
  spend, pickup timing, Glory Kill risk, Chainsaw target and component priority.
- Randomness or procedural generation: the admitted route and encounter gates
  are authored; live hostile variation does not generate another level.
- Multiple viable strategies: direct body damage can replace a weak-point
  break, ranged defeat can replace a Glory Kill, and one may delay Chainsaw use
  while ammunition remains comfortable.
- Typical replay motive: higher difficulties, collectibles, mission challenges,
  fast travel and upgrades exist but are excluded from this first fresh route.
- Claims: `DE-004`–`DE-012`.

## Adjacent systems and history

- Direct predecessor: `GAME-0245` — DOOM (2016), analysed at its first mission
  on the same named difficulty.
- Comparison corridor: `GAME-0272` — Serious Sam 4, another authored
  first-person finite-clearance route with typed ammunition but no contextual
  combat-resource conversions in its admitted opening level.
- Important differences: the complete DOOM (2016) first-mission genome recurs,
  but Eternal moves the Chainsaw economy into mission one, guarantees only a
  partial fuel floor and lets aimed component destruction disable an attack.
  Its Glory Kill now yields health rather than the predecessor record's broader
  health/ammunition drop claim; weapon and enemy names remain parameters.
- No franchise inheritance: Dash, Flame Belch, Blood Punch, later missions,
  DLC and modes are not imported from product marketing.
- Claims: `DE-001`–`DE-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-190`, `ACT-341`, `ACT-419` | traversal form, weapon, hostile and interaction identities |
| System Behaviour | `SYS-215`, `SYS-222`, `SYS-369`, `SYS-578`, `SYS-655`, `SYS-749`, `SYS-755`, `SYS-770`, `SYS-794`, `SYS-841` | damage, drops, fuel floor, component and checkpoint |
| Constraint | `CON-269`, `CON-282`, `CON-402`, `CON-578`, `CON-589` | fuel cost, target class, order, ammunition and stagger reach |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-295` | HUD styling, waypoint, local threat and opportunity treatment |
| Objective | `OBJ-026` | elevator and Fortress identity are parameters |
| Time | `TIM-003` | live cadence and recovery duration are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `285` (`GAME-0001`–`GAME-0285`).
- Exact genome matches: none.
- Tied near matches: `GAME-0245` — DOOM (2016) (`23 / 28 = 0.821429`).
- Supported combination subsets: `COMB-0235`, `COMB-0243`.
- Scan date: 2026-09-10.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0245` — DOOM (2016) | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-341`, `ACT-419`, `SYS-215`, `SYS-222`, `SYS-369`, `SYS-578`, `SYS-655`, `SYS-749`, `SYS-770`, `CON-282`, `CON-402`, `CON-578`, `CON-589`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-295`, `OBJ-026`, `TIM-003` | The predecessor's complete opening-mission signature recurs. Eternal additionally admits a targeted fuel-priced Chainsaw ability (`ACT-190` + `CON-269`), required breakable route objects (`SYS-755`), a passive one-segment fuel floor (`SYS-841`) and attached-component destruction that removes an attack without defeating the body (`SYS-794`). These are state boundaries, not changed enemy, weapon or amount names. | Near, `23 / 28 = 0.821429` |

### Preserved research notes

- New genes: `SYS-841` only. The historically proposed `SYS-842` was merged
  into reused `SYS-794` by `TAXONOMY_CHANGE_064`.
- Classification result: `Reuse with one new System boundary and two
  boundary-preserving generalisations`.
- Lower-ID scan: all twenty-seven reused mechanics were checked against their
  definitions and known carriers. `TAXONOMY_CHANGE_064` corrects the first
  review's missed `SYS-794` reuse by merging historical alias `SYS-842` into
  that survivor. `SYS-376` fails because it fully recharges reusable item
  charges; `SYS-754`, `SYS-791` and `SYS-851` bind drain or recovery to portable
  illumination; `SYS-347` and `INF-139` bind weak points to a larger ARC
  perception/attention compound; `SYS-580` and `SYS-701` resolve armoured
  vehicles. The historical rejection of `ACT-426`, `CON-595` and `INF-304` was
  withdrawn by `TAXONOMY_CHANGE_059`; those IDs are merged aliases for the same
  close command, legality and disclosure, while defeat settlement remains in
  `SYS-770`. None of those boundaries can absorb `SYS-841`. `SYS-794` does
  absorb the component transition without widening because limb anatomy,
  mounted-weapon identity and visible damage layers are carrier or Information
  parameters around the same functional loss.

## Taxonomy impact

- Registry changes: add `SYS-841`; generalise `SYS-770` without changing its
  lifecycle, ID, earlier carrier or combination membership; reuse generalised
  `SYS-794` after `TAXONOMY_CHANGE_064` merged the later `SYS-842` alias into
  that survivor.
- Taxonomy-change records: `TAXONOMY_CHANGE_054` and
  `TAXONOMY_CHANGE_064`.
- Earlier signatures: none changed. `GAME-0245` remains byte-equivalent in
  frontmatter and still instantiates the same Glory Kill conversion.
- Candidate terms: mission, hub, demon, body component, weapon, resource, fuel
  segment, keycard and gate names remain game parameters.

## Negative results

- No direct play, local entitlement, audio, video, screenshot or third-party
  visual evidence is claimed.
- No semantic version is assigned to public Build ID `24695697`.
- Flame Belch, Dash, Blood Punch, mod selection, grenade use, secrets, replay
  equipment, Extra Lives and post-first-mission progression are not inferred
  from whole-product descriptions.
- `SYS-770` does not merge Glory Kill and Chainsaw legality; it owns only their
  shared defeat-to-recovery result.
- The first controllable Fortress state is the retained successor; the route
  does not claim that a reload was personally executed.

## Delta summary

## New facts

- [Confirmed | Corroborated | High] `DE-001`–`DE-012`: the current base Windows
  Campaign supplies a bounded first mission whose two contextual execution
  methods refill different combat resources before an authored hub successor.

## New genes

- [Observation | Corroborated | High] `SYS-841` isolates a reserve that
  automatically returns only to a guaranteed floor, while finite world stock
  is required above it.
- [Confirmed | Corroborated | High] `SYS-794` transfers from anatomical limb
  severance to destruction of a located attached component that disables its
  capability without defeating the carrier; `SYS-842` is the historical merged
  alias of `SYS-794` under `TAXONOMY_CHANGE_064`.

## New combinations

- [Observation | Corroborated | High] `No new combination`. `GAME-0286` becomes
  a fifth supporter of `COMB-0235` and a second supporter of `COMB-0243`.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_054` generalises `SYS-770` from
  one stagger-finisher instance to the shared contextual defeat-to-recovery
  result while leaving action and legality distinctions intact.
- [Confirmed | Corroborated | High] `TAXONOMY_CHANGE_064` merges `SYS-842`
  into generalised `SYS-794`; limb and mounted weapon are carrier parameters.

## New questions

- Does another shooter cap passive recovery at a guaranteed reserve floor while
  requiring finite pickups for surplus, confirming `SYS-841` independently?
- Does a later bounded game disable living-hostile capabilities through
  component destruction without importing a vehicle-damage model?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0287` — Stellaris.
- Optimisation criterion: leave the authored first-person corridor and test
  whether one standard early empire packet reuses known economic/network genes
  without importing the whole grand-strategy timeline.
- Expected information gain: separate autonomous empire simulation, surveyed
  uncertainty and retained expansion from DOOM Eternal's local embodied loop.
- Backlog impact: advances the approved batch-017 ordered horizon.

## Why this game

- [Hypothesis | Limited | High] DOOM Eternal answers the selection question
  narrowly: most of DOOM (2016)'s opening genome transfers unchanged, while the
  meaningful differences are resource-source and component-state systems rather
  than renamed weapons, enemies or levels.
