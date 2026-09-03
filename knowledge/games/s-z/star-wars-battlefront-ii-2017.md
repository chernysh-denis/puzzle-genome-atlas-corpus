---
game_id: GAME-0230
slug: star-wars-battlefront-ii-2017
game_title: "STAR WARS Battlefront II (2017)"
analysis_status: reviewed
reviewed: 2026-09-02
combination_ids:
  - COMB-0228
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-199
    - ACT-202
    - ACT-341
  system:
    - SYS-208
    - SYS-215
    - SYS-369
    - SYS-380
    - SYS-736
    - SYS-737
    - SYS-738
    - SYS-739
  constraint:
    - CON-269
    - CON-282
    - CON-330
    - CON-571
  information:
    - INF-115
    - INF-119
    - INF-125
    - INF-268
    - INF-280
  objective:
    - OBJ-144
  time:
    - TIM-003
---

# Game: STAR WARS Battlefront II (2017)

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current legally available English Windows Steam package,
  app `1237950`, public Build ID `10351139`, built 2023-01-18 and published
  2023-01-31, checked 2026-09-02; official last PC gameplay patch dated
  2020-08-26. The installed store package is Celebration Edition, but this unit
  analyses only unchanged base-game Campaign content and excludes every
  cosmetic entitlement.
- Entry: from the Campaign menu choose a fresh `The Cleaner` start on
  `Soldier` difficulty and retain the first controllable ID10 state after the
  opening interrogation. Keyboard and mouse, default third-person infantry
  camera and one local player are fixed parameters.
- Primary decision loop: read the current objective and control prompt; steer
  ID10 through reachable corridors, vents, doors and terminals; use its legal
  shock or slice interaction; release Iden; continue as Iden while ID10 becomes
  a command-driven support ability; move, crouch, scan, aim and fire; manage
  health exposure and weapon heat; retrieve the required blaster; purge the
  intercepted message; clear or bypass required opposition; defend the final
  door slice and reach the airlock.
- Positive retained terminal: finish the airlock sequence and allow the
  mission-complete transition to expose `The Battle of Endor` as the successor
  campaign mission. Return to the main menu, quit cleanly, relaunch, and verify
  that `Continue` or Chapter Select retains the successor rather than restoring
  the opening interrogation. Reaching the airlock before the completion
  transition, or relying only on a transient checkpoint, is intermediate.
- Negative evaluation terminal: ID10 destruction, Iden death or another
  mission-critical failure before completion ends the attempt. A chosen retry
  may restore the latest authored checkpoint, but the packet is not positive
  until the successor mission remains available after relaunch.
- Included: fixed first campaign prologue; one remote-control-to-companion
  handoff; droid navigation, vents, doors, lockdown and computer slices; droid
  shock and scan; direct infantry traversal, crouch, aiming, firearm and melee
  controls; required blaster pickup; local enemies; cover and body hits;
  weapon heat, passive and timed active cooling; personal health and delayed
  regeneration; ordered objectives; authored checkpoints; airlock escape;
  retained first-mission completion and successor access.
- Reproducible parameterisation: Windows Steam app `1237950`; Build ID
  `10351139`; English; keyboard/mouse; third-person; `Campaign > The Cleaner >
  Soldier`; fresh mission state; no collectible detours; exit/relaunch terminal
  check after `The Battle of Endor` is exposed.
- Excluded: the 2005 game of the same subtitle; all later campaign missions;
  Resurrection; Arcade; Instant Action; multiplayer, Galactic Assault, Supremacy,
  Co-Op, Heroes, Starfighter and Ewok modes; online matchmaking; ranks, XP,
  milestones, Star Cards, currencies and account grind; collectibles;
  Celebration cosmetics; DLC or edition unions; mods; controller; any service
  history beyond identifying the stable package.
- Direct-play status: not directly played in this unit. The packet is a
  reproducible source-backed transition trace; no audiovisual source was
  opened, played, heard or used.
- Scope rationale: the first campaign mission is fixed, local, short, ordered,
  checkpointed and ends at a named successor. It therefore supplies a stronger
  bounded terminal than an arbitrary multiplayer stop while preserving the
  product's authored remote-droid and infantry teaching sequence.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SWBF2-001` | EA currently distributes the 2017 Windows product separately from the 2005 game; the Steam package is app `1237950`, public Build `10351139` | Confirmed | Direct | High | P1, S1 |
| `SWBF2-002` | Campaign, Multiplayer and Arcade are distinct top-level modes, and Celebration ownership adds cosmetics rather than changing the base campaign mission | Confirmed | Direct | High | P1, P2 |
| `SWBF2-003` | The official PC manual documents movement, crouch, aim, fire, melee, interact and ID10 shock/slice/ability controls | Confirmed | Direct | High | P2 |
| `SWBF2-004` | The Cleaner begins with directly controlled ID10 navigation through vents, doors and terminals before control transfers to Iden | Observation | Corroborated | High | S2, S3, S4 |
| `SWBF2-005` | ID10 actions require an eligible target and resolve as typed shock, scan or slice effects | Confirmed | Corroborated | High | P2, S2, S3 |
| `SWBF2-006` | Lockdown terminals, Iden's release, weapon retrieval, message purge and airlock occur in a fixed authored order | Observation | Corroborated | High | S2, S3, S4 |
| `SWBF2-007` | After Iden's release, the same ID10 persists as her command-driven support rather than remaining the directly controlled body | Observation | Corroborated | High | S2, S3, S4 |
| `SWBF2-008` | Blaster fire produces visible heat, may overheat, cools passively and supports a timed active-cooling input | Confirmed | Direct | High | P2 |
| `SWBF2-009` | Incoming attacks reduce visible personal health and health regenerates after the player avoids further damage | Confirmed | Direct | High | P2 |
| `SWBF2-010` | The final route requires defending while ID10 completes an airlock-door slice | Observation | Corroborated | High | S2, S3, S4 |
| `SWBF2-011` | The Cleaner is Mission 1 and The Battle of Endor is its named successor | Confirmed | Corroborated | High | S2, S5 |
| `SWBF2-012` | Checkpoint restore bounds failure, while clean relaunch and retained successor access form the packet's positive terminal | Observation | Corroborated | High | P2, S2, S5, V1 |

## Basic data

- Release / origin: DICE, Motive Studios and Criterion Games / Electronic Arts;
  original release 2017-11-17; current Windows product distributed through EA
  and Steam.
- Platform or physical form: Windows PC client; current Steam Celebration
  package; one local base-game Campaign mission with no admitted online or
  account-progression dependency.
- Puzzle family: real-time system pressure; inventory and fixture dependencies;
  agent routing and coordination; ordered dependency sequencing.
- Primary and secondary evidence:

- Primary sources:
  - **[P1]** [official EA product page](https://www.ea.com/games/starwars/star-wars-battlefront-2),
    for current Windows availability, the base single-player Iden story and the
    separation of Standard and cosmetic-rich Celebration offerings.
  - **[P2]** [official PC manual](https://eaassets-a.akamaihd.net/eahelp/manuals/swfbii-manuals_pc_EN.pdf),
    for keyboard/mouse movement, crouch, fire, zoom, melee, interact, droid
    shock/slice/ability inputs; Campaign separation from Multiplayer and Arcade;
    objective/scanner/health displays; health regeneration; weapon heat,
    overheat and active cooling; and `Reload from Last Checkpoint`, `Restart
    Mission` and checkpoint-retaining quit behaviour.
  - **[P3]** [official August 26 PC patch notes](https://forums.ea.com/discussions/star-wars-battlefront-2-en/star-wars-battlefront-ii---august-26th-patch---release-notes/10819478),
    for the last official PC gameplay patch and its deployment date.
  - **[P4]** [official final-content letter](https://www.ea.com/games/battlefield/news/letter-to-the-community-original-era-content),
    for the declared completion of the content vision after twenty-five free
    updates and for evidence that live-service modes remain separate scopes.
- Secondary and reproducible sources:
  - **[S1]** [SteamDB depots](https://steamdb.info/app/1237950/depots/), for the
    Windows depot, public Build ID `10351139` and 2023-01 timestamps.
  - **[S2]** [The Cleaner mission record](https://battlefront.fandom.com/wiki/The_Cleaner),
    for first-mission identity, ID10-to-Iden order, terminals, lockdown,
    weapon retrieval, message purge, airlock and successor mission.
  - **[S3]** [written The Cleaner walkthrough](https://www.gamepur.com/guides/cleaner-walkthrough-star-wars-battlefront-ll),
    for the droid opening, communication centre, weapon retrieval, final
    defence while the droid unlocks the route and mission ending.
  - **[S4]** [written mission route](https://www.speedrun.com/id-ID/star_wars_battlefront_ii_2017/guides/b4jlk),
    for two terminal interactions, vents, lockdown, the Iden handoff, weapon,
    purge area and final door delay.
  - **[S5]** [mission-completion achievement guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3242462995),
    for `The Cleaner` as Mission 1, `The Battle of Endor` as Mission 2,
    mission replay and the three campaign difficulty labels.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P4` and `S1`–`S5` under the fixed build, difficulty, controls and
  retained-terminal contract; no audiovisual playback or direct-play claim.
- Claim IDs: `SWBF2-001`–`SWBF2-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly navigate first ID10 and then Iden through fixed
  mission geometry; `ACT-161`: aim and commit direct blaster or melee attacks;
  `ACT-199`: retrieve and equip the required reachable blaster; `ACT-202`:
  change Iden between standing and crouched posture; `ACT-341`: commit legal
  vent, door, lockdown, computer and airlock interactions.
- The system-authored transfer from ID10 control to Iden control is not
  `ACT-228`: the player does not choose among protagonists.
- Parameters: controlled body, corridor, vent, posture, target, weapon, pickup,
  terminal, interaction duration, door and route.
- Claim IDs: `SWBF2-004`–`SWBF2-009`.

### System Behaviour Genes

- Existing `SYS-208`: resolve blaster aim through cover and body hits;
  `SYS-215`: resolve live directly commanded combat; `SYS-369`: restore the
  latest authored checkpoint after accepted failure; `SYS-380`: resolve ID10
  scan, shock and slice effects; `SYS-736`: advance staged controls and
  objectives after their current predicate is completed.
- New `SYS-737`: apply incoming damage to personal health and regenerate
  missing health only after a no-damage interval; new `SYS-738`: accumulate
  weapon heat and resolve passive cooling or a successful timed active-cooling
  input; new `SYS-739`: preserve ID10 across the authored control handoff and
  rebind it from directly steered body to Iden's command-driven support ability.
- Resolution order: accept movement, posture, contextual, ability or attack
  input; validate reach, target and readiness; resolve interaction or hits;
  update heat, health and enemy state; resolve cooling or delayed regeneration;
  advance the current objective and checkpoint; change control authority at
  Iden's release; then settle airlock completion and retain successor access.
- Claim IDs: `SWBF2-004`–`SWBF2-012`.

### Constraint Genes

- Existing `CON-269`: ID10 abilities require legal targets, reach and readiness;
  `CON-282`: terminals, lockdown, weapon retrieval, purge and airlock require
  ordered authored gates; `CON-330`: the controlled body and required droid,
  terminal or route fixture must remain viable.
- New `CON-571`: firearm input requires remaining heat capacity or a completed
  cooling state; overheat temporarily rejects further fire.
- Scarce strategic resources: safe exposure time, health, available cover,
  weapon-heat headroom, active-cooling timing, ability readiness and the final
  slice-defence interval.
- Claim IDs: `SWBF2-005`–`SWBF2-010`.

### Information Genes

- Existing `INF-115`: local sight and scanner disclosure provide partial enemy
  state; `INF-119`: expose health and droid-ability readiness; `INF-125`: expose
  the current authored objective and route marker; `INF-268`: expose the current
  staged control instruction and its completion.
- New `INF-280`: the reticle's heat gauge exposes current heat, overheat and the
  timed active-cooling window before the next firing choice.
- Later mission gates, hidden enemies beyond current sight/scan and the full
  campaign graph do not enter the information set.
- Claim IDs: `SWBF2-004`–`SWBF2-011`.

### Objective Genes

- New `OBJ-144`: complete one ordered infiltration-to-purge-to-escape mission
  and retain access to its named successor after a clean relaunch.
- Releasing Iden, purging the message or reaching the last door alone is
  intermediate. A checkpoint retry is recoverable but not a positive terminal;
  later story completion and multiplayer settlement are outside the objective.
- Claim IDs: `SWBF2-006`–`SWBF2-012`.

### Time Genes

- Existing `TIM-003`: movement, hostile combat, damage, heat, cooling,
  regeneration and the final door defence advance in real time while inputs
  remain available.
- Claim IDs: `SWBF2-005`–`SWBF2-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| ID10 is the directly controlled body | Navigate to a legal vent or terminal and interact | ID10 traverses the fixed route or changes the addressed fixture | remote body is ordinary direct navigation plus contextual interaction | `SWBF2-004` |
| A valid droid target is reachable | Commit shock or slice | The typed effect disables a hostile or advances the fixture | ability legality differs from basic fire | `SWBF2-005` |
| Lockdown is active and required terminals remain | Slice them in authored order | Lockdown clears and the route reaches Iden | ordered gates advance the staged prologue | `SWBF2-006` |
| Iden is released | Complete the authored handoff | Control moves to Iden and the same ID10 becomes her command ability | persistent support changes control role without player-selected switching | `SWBF2-007` |
| Required blaster is reachable | Transfer and equip it | Iden gains ordinary ranged attack authority | a mission pickup enables the combat phase | `SWBF2-008` |
| Weapon heat is below its limit | Fire repeatedly | Shots resolve and heat rises; at the limit firing locks | fire cadence creates a visible heat budget | `SWBF2-008` |
| Cooling window or passive cooling is available | Time active cooling or cease fire | A successful input accelerates readiness; waiting lowers heat | cooling is an actionable system, not ammunition reload | `SWBF2-008` |
| Iden has missing health and avoids further damage | Remain out of incoming fire | Health begins regenerating after the quiet interval | cover creates recovery opportunity | `SWBF2-009` |
| Purge area is secured | Interact with the required computer | The intercepted message is deleted and escape objectives advance | combat and interaction jointly gate escape | `SWBF2-009` |
| Final airlock route is locked | Command ID10 to slice while defending | Slice progress and live opposition continue until the route opens | support ability and combat overlap in real time | `SWBF2-010` |
| Airlock sequence completes | Allow mission settlement, quit and relaunch | `The Battle of Endor` remains available through Continue/Chapter Select | explicit positive retained terminal | `SWBF2-011`, `SWBF2-012` |
| ID10 or Iden fails before settlement | Choose checkpoint retry | Transient combat and positions reset to the latest authored checkpoint | retry is recoverable but not mission completion | `SWBF2-005`, `SWBF2-012` |

## Strategic and experiential structure

- Local decision: choose a safe line through vents or cover; select a legal
  droid target; pace bursts against weapon heat; time active cooling; leave
  hostile sight long enough to regenerate before the next gate.
- Medium-term planning: preserve health and droid readiness for required
  terminals; distinguish a route-clearing slice from an optional shock; clear
  the purge and final-door spaces before committing to exposed interaction.
- Long-term structure: a staged remote-droid infiltration releases the human
  protagonist, reuses the droid as support, teaches infantry combat and ends in
  a retained successor mission rather than an arbitrary corridor checkpoint.
- Common heuristics: inspect the objective marker; use scanner before entering
  a room; fire in controlled bursts; cool behind cover; command a slice only
  when the required defence interval is supportable.
- Failure attribution: target/readiness feedback, objective text, heat gauge,
  health, checkpoint restore and successor availability separate input,
  combat, ordering and retention failures.
- Player trust: positions and authored gates are stable; the manual documents
  combat/checkpoint semantics, and the clean relaunch makes retention testable.

## Replay and variation

- What changes: aim, route micro-positioning, detection order, combat timing,
  damage, cooling choices and checkpoint use.
- Randomness or procedural generation: no relevant procedural level generation;
  combat outcomes vary within a fixed authored mission layout and objective
  sequence.
- Multiple viable strategies: firing cadence, cover choice, scan timing and
  enemy-clear order vary, but the droid handoff, message purge, airlock and
  retained successor are mandatory.
- Typical replay motive: a cleaner Soldier run, collectible search or another
  difficulty. Collectibles and difficulty comparison are outside this packet.

## Adjacent systems and history

- Direct predecessors: the 2005 Battlefront II is a separate product and must
  not be merged. The 2017 release's later updates and multiplayer modes do not
  alter this bounded base-campaign prologue.
- Similar games: Call of Juarez: Gunslinger joins one authored firearm mission,
  heat-independent ammunition, direct combat and checkpoints; World of
  Warcraft Exile's Reach and Once Human use staged tutorial objectives;
  Cyberpunk 2077 joins local scan-assisted combat and ability readiness.
- Important differences: `The Cleaner` starts in a directly controlled support
  body, preserves that unit through a system-authored transfer into companion
  ability, couples blaster heat to active cooling, and verifies a named
  successor mission after relaunch.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-199`, `ACT-202`, `ACT-341` | navigate, posture, attack, equip and interact |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-369`, `SYS-380`, `SYS-736`, `SYS-737`, `SYS-738`, `SYS-739` | hits, combat, checkpoints, abilities, guidance, health, heat and handoff |
| Constraint | `CON-269`, `CON-282`, `CON-330`, `CON-571` | ability, mission, viability and cooling legality |
| Information | `INF-115`, `INF-119`, `INF-125`, `INF-268`, `INF-280` | opponents, personal state, objective, instruction and heat |
| Objective | `OBJ-144` | purge and escape into retained successor access |
| Time | `TIM-003` | continuous combat, recovery, cooling and defence |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `229` (`GAME-0001`–`GAME-0229`).
- Exact genome matches: none.
- Tied near matches: `GAME-0223` — Aion Classic (`12 / 33 = 0.363636`).
- Supported combination subsets: `COMB-0228`.
- Scan date: 2026-09-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0223` — Aion Classic | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-215`, `SYS-380`, `CON-269`, `CON-282`, `INF-115`, `INF-119`, `INF-125`, `INF-268`, `TIM-003` | Both stage direct real-time movement, hostile attacks, contextual fixtures and typed abilities through current tutorial and objective information. Aion Classic instead attacks three Mystic Cube reward fixtures, can reset all skill cooldowns randomly and ends through a one-use tutorial exit. The Cleaner uses authored ID10-to-Iden control-role transfer, a required blaster, cover/body hits, full delayed health regeneration, visible heat and active cooling, checkpoint recovery, data purge, airlock defence and a retained named successor; the 12 shared genes cover `12 / 21 = 0.571429` of Aion's smaller genome. | Near, `12 / 33 = 0.363636` |

### Preserved research notes

- New genes: `SYS-737`, `SYS-738`, `SYS-739`, `CON-571`, `INF-280`, `OBJ-144`.
- Reused genes: `ACT-008`, `ACT-161`, `ACT-199`, `ACT-202`, `ACT-341`,
  `SYS-208`, `SYS-215`, `SYS-369`, `SYS-380`, `SYS-736`, `CON-269`,
  `CON-282`, `CON-330`, `INF-115`, `INF-119`, `INF-125`, `INF-268` and
  `TIM-003`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: movement, attacks, world pickup, posture, contextual
  interactions, hits, direct combat, checkpoints, typed abilities, ordered
  objectives and staged information retain existing boundaries. New records
  isolate full delayed health recovery, heat/cooling, the support-unit handoff,
  its firing gate, visible cooling timing and retained first-mission objective.

## Taxonomy impact

- Registry changes: `SYS-737`–`SYS-739`, `CON-571`, `INF-280`, `OBJ-144`; no
  earlier signature changes.
- Taxonomy-change record: none.
- Candidate terms affected: delayed personal regeneration, weapon heat, active
  cooling, support-unit role handoff, heat readiness and retained successor.
- Taxonomy-health disposition: accept the measured `active-singleton-share`
  advisory at `1,612 / 2,122 = 0.759661` for this bounded unit. The latest-nine
  new-gene rate remains below its threshold at `55 / 9 = 6.111111`; duplicate
  and lexical reports are suggestion-only and authorise no lifecycle change.

## Negative results

- `ACT-228` and `SYS-690` are rejected: control changes by authored mission
  sequence, not a player-selected protagonist switch or vehicle seat exchange.
- `SYS-348`, `SYS-578` and `SYS-714` are rejected: this is one unshielded
  personal health pool with full delayed regeneration, no downed/revive layer,
  consumable healing loop or partial recovery cap.
- Ammunition/reload genes are rejected: the scoped blaster is governed by heat,
  passive cooling and active-cooling timing rather than a carried magazine
  economy.
- Multiplayer deployment, classes, heroes, vehicles, capture, tickets, ranks,
  unlocks and all later story systems are excluded rather than unioned.
