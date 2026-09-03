---
game_id: GAME-0221
slug: world-of-warcraft
game_title: World of Warcraft
analysis_status: reviewed
reviewed: 2026-09-01
combination_ids:
  - COMB-0219
gene_ids:
  action:
    - ACT-008
    - ACT-107
    - ACT-161
    - ACT-190
    - ACT-199
    - ACT-341
  system:
    - SYS-215
    - SYS-299
    - SYS-362
    - SYS-379
    - SYS-380
    - SYS-716
  constraint:
    - CON-269
    - CON-282
    - CON-395
    - CON-562
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-153
    - INF-268
  objective:
    - OBJ-137
  time:
    - TIM-003
---

# Game: World of Warcraft

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current official US **Retail World of Warcraft** Windows
  client in the Midnight branch, patch/build `12.1.0.69587`, checked
  2026-09-01. The build is fixed from Blizzard's official US distribution
  metadata; the current public content boundary is Midnight `12.1`, Curse of
  Ula'tek.
- Reproducible character and entry: fresh account, US Normal realm, Alliance,
  one Human Warrior, level 1 aboard the Exile's Reach expedition ship with
  `Warming Up` available. Choose the full tutorial and reject the Housing Skip.
- Primary decision loop: read the current tutorial and quest tracker; talk to
  the addressed NPC; follow map and world markers; move into legal reach;
  target and attack or activate the learned Warrior ability; interact with,
  collect, use or equip the required object; survive the response; turn in the
  objective; retain experience, levels, gear, abilities and the next quest;
  repeat through the tutorial dungeon and the routed region hand-off.
- Reproducible terminal: complete every required Exile's Reach main-chain step,
  complete Darkmaul Citadel, arrive at the Dragon Isles docks and hand
  `An End to Beginnings` to Kalecgos. Success requires the same Human Warrior
  to return to control with the hand-in, level, abilities and equipment
  retained. Merely reaching level 10, leaving the island, or defeating the
  dungeon's first boss is not success.
- Included: the required ship, shore, expedition, quilboar, harpy and Darkmaul
  sequence; Human Warrior-specific combat lessons; NPC conversations; direct
  locomotion, targeting, basic attacks and learned Warrior abilities; quest
  devices and fixtures; required collection, rescue and defeat predicates;
  experience/levels, loot, inventory and equipment; the 1–5-player tutorial
  dungeon entered alone so autonomous role-capable followers complete the
  party; both required dungeon bosses; the current Dragon Isles transition and
  final hand-in.
- Reproducible parameterisation: use default current difficulty and controls,
  a Normal realm, no heirlooms or transferred account resources and no invited
  human party. Exact character name, realm identity within the US Normal pool,
  incidental enemy, sampled loot, movement line, combat cadence and elapsed
  time may vary. Complete only required objectives in their shown order.
- Excluded: the Housing Skip; optional `Killclaw the Terrible`, `Freeing the
  Light` and other side objectives; Stormwind and its former city tour;
  Dragonflight play after the Kalecgos hand-in; Horde, another race/class,
  specialisation or talent planning beyond automatically usable Warrior state;
  RP realms, War Mode, PvP, professions, auction/economy, mounts, pet battles,
  account collections, boosts, housing, later dungeons, raids, Midnight story,
  endgame and every Classic branch or historical live-service union.
- Potential scoped modules: one declared Horde/race/class Exile's Reach route,
  the post-terminal Dragonflight chapter, a current group dungeon, profession
  tutorial, War Mode or Classic branch requires its own build, entry, loop and
  terminal.
- Direct-play status: no authenticated client was played. Current Blizzard
  guides and update notes establish product, branch, new-player entry and
  route destination; official distribution metadata fixes the build. A
  maintained current walkthrough supplies required step order and the
  observable post-dungeon hand-in where Blizzard does not publish a complete
  quest trace. No video or audio was opened, played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `WOW-001` | The reviewed US Retail boundary is Midnight patch `12.1`, build `12.1.0.69587` | Confirmed | Direct | High | P1, P2, P3 |
| `WOW-002` | A fresh player begins Exile's Reach aboard a ship and learns movement, NPC interaction, class abilities and inventory use | Confirmed | Direct | High | P1 |
| `WOW-003` | Current fresh-account routing proceeds from completed Exile's Reach into Dragonflight rather than the historical capital-city continuation | Confirmed | Corroborated | High | P1, P4, S1 |
| `WOW-004` | Normal and RP are current realm types; this packet fixes Normal and excludes War Mode, which is unavailable before level 20 | Confirmed | Direct | High | P1 |
| `WOW-005` | Exile's Reach is a level 1–10 tutorial culminating in a two-boss 1–5-player Darkmaul Citadel run | Confirmed | Corroborated | High | P5, S1 |
| `WOW-006` | The fixed Human Warrior route teaches class-specific actions while required quests join navigation, interaction, combat, collection, rewards and experience | Observation | Corroborated | High | P1, S1, S2 |
| `WOW-007` | Entering Darkmaul Citadel alone supplies autonomous allies for the required tutorial party and retains direct control of only the Warrior | Observation | Corroborated | High | P5, S1 |
| `WOW-008` | The current full route ends at the Dragon Isles docks with the `An End to Beginnings` hand-in to Kalecgos | Observation | Corroborated | Medium | S1 |
| `WOW-009` | The current Housing Skip bypasses the island and therefore cannot satisfy the full-route terminal | Observation | Corroborated | Medium | S1 |
| `WOW-010` | The repository trace reproduces fixed entry, ordered quests, combat growth, follower dungeon and retained regional hand-off without direct play | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Blizzard Entertainment; World of Warcraft launched in 2004
  and the scoped Retail branch remains maintained in 2026.
- Platform or physical form: authenticated networked Windows PC client; one
  persistent character on one US Normal realm.
- Puzzle family: real-time system pressure; agent routing and coordination;
  ordered dependency sequencing; inventory and fixture dependencies.
- Primary sources:
  - **[P1]** [official New Players Starter Guide](https://worldofwarcraft.blizzard.com/en-us/news/24266319/new-players-starter-guide-welcome-to-world-of-warcraft),
    for current fresh-player entry, taught interfaces, Dragonflight routing,
    realm types and War Mode boundary.
  - **[P2]** [official Curse of Ula'tek content notes](https://worldofwarcraft.blizzard.com/en-us/news/24293281/curse-of-ulatek-content-update-notes),
    for the current Midnight `12.1` content boundary.
  - **[P3]** Blizzard official US `wow/versions` distribution metadata, checked
    2026-09-01, for `VersionsName 12.1.0.69587` and `BuildId 69587`.
  - **[P4]** [official 11.2.7 new/returning-player update](https://worldofwarcraft.blizzard.com/en-us/news/24226733/welcome-back-to-world-of-warcraft),
    for the refreshed Exile's Reach-to-Dragonflight flow.
  - **[P5]** [official Exile's Reach overview](https://worldofwarcraft.blizzard.com/en-us/news/23873862),
    for the 1–10 island, class teaching and 1–5-player two-boss dungeon.
- Secondary and reproducible sources:
  - **[S1]** [Wowhead maintained Exile's Reach walkthrough](https://www.wowhead.com/guide/exiles-reach-walkthroughs-analysis),
    checked 2026-09-01 for the required current route, follower fill, Housing
    Skip exclusion and Dragon Isles dock terminal.
  - **[S2]** [Warcraft Wiki Exile's Reach storyline](https://warcraft.wiki.gg/wiki/Exile%27s_Reach_storyline),
    checked 2026-09-01 only to corroborate Human Warrior lesson and required
    Darkmaul sequence names.
  - **[V1]** repository-side transition trace from `P1`–`P5`, `S1` and `S2`;
    rules reasoning, not direct play.
- Claim IDs: `WOW-001`–`WOW-010`.

## Mechanical decomposition

### Action Genes

- Existing: `ACT-008`, traverse the current directed route; `ACT-107`, talk to
  the addressed NPC; `ACT-161`, target and strike a reachable hostile;
  `ACT-190`, activate a learned Warrior ability; `ACT-199`, collect/equip one
  compatible reward or world item; `ACT-341`, commit a required quest-device,
  rescue, vehicle, switch or dungeon interaction.
- New genes: none. Ship cannon, enhanced boar and catapult use are contextual
  quest-interaction parameters, not independently recurring control families.
- Parameters: NPC, marker, destination, target, weapon, ability, resource,
  item, fixture, quest stage and party context.
- Claim IDs: `WOW-002`, `WOW-005`–`WOW-010`.

### System Behaviour Genes

- Existing: `SYS-215`, directly commanded real-time combat; `SYS-299`, retained
  experience thresholds and character levels; `SYS-362`, bounded encounter and
  quest rewards; `SYS-379`, retained authored quest-state advancement;
  `SYS-380`, typed Warrior ability effects.
- New `SYS-716`: when one player enters the required tutorial dungeon, fill
  missing party functions with autonomous followers that navigate, acquire
  targets, tank, heal or deal damage around the controlled character until the
  instance ends.
- Resolution order: character and tutorial entry expose the first quest; each
  legal interaction/combat predicate advances its retained stage and reward;
  experience raises the same character; Darkmaul entry fixes participants and
  supplies missing functions; followers and hostiles resolve continuously
  around player attacks; both boss gates settle; the route transition exposes
  the Dragon Isles hand-in; the accepted hand-in writes the terminal.
- Claim IDs: `WOW-002`–`WOW-010`.

### Constraint Genes

- Existing: `CON-269`, ability target/range/resource/readiness legality;
  `CON-282`, ordered authored quest prerequisites; `CON-395`, equipment and
  skills compatible with current Human Warrior state.
- New `CON-562`: the Darkmaul tutorial packet admits one to five eligible
  players only after the required quest gate and supplies autonomous missing
  party functions rather than permitting an empty or unrelated roster.
- Scarce resources: health, ability readiness/resource, reach, compatible gear,
  quest prerequisites, character level and live party condition.
- Claim IDs: `WOW-005`–`WOW-010`.

### Information Genes

- Existing: `INF-073`, hotbar and equipment; `INF-115`, locally perceived NPC
  and hostile state; `INF-119`, health, resource, level, experience, learned
  abilities and readiness; `INF-125`, explored map, quest tracker and markers;
  `INF-128`, reward/loot identity and compatibility; `INF-153`, active party
  members and their condition; `INF-268`, current tutorial instruction and its
  completion response.
- New genes: none. The selected surfaces already distinguish personal, local,
  quest, item, party and authored teaching information without claiming future
  quest omniscience.
- Claim IDs: `WOW-002`, `WOW-005`–`WOW-010`.

### Objective Genes

- New `OBJ-137`: complete the full current Alliance Exile's Reach route,
  Darkmaul Citadel and the Dragon Isles `An End to Beginnings` hand-in while
  retaining the same Human Warrior's progress.
- Success requires every predicate. Level 10, the Housing Skip, one dungeon
  boss or dock arrival without hand-in is not success; a recoverable combat
  error remains inside the attempt rather than redefining the terminal.
- Claim IDs: `WOW-003`, `WOW-005`, `WOW-008`–`WOW-010`.

### Time Genes

- Existing `TIM-003`: avatar, followers, hostiles, attacks, ability readiness
  and live world state advance concurrently outside blocking interfaces.
- Claim IDs: `WOW-005`–`WOW-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Current US Retail client; fresh account | Choose Normal realm, Alliance Human Warrior and full Exile's Reach | Creates one persistent level-1 character aboard the tutorial ship; Housing Skip is rejected | exact entry | `WOW-001`–`WOW-004`, `WOW-009` |
| Current quest addresses an NPC or world object | Talk or commit the prompted interaction | Objective records completion, grants bounded reward/experience and reveals the next required step | authored teaching chain | `WOW-002`, `WOW-006` |
| Required hostile is reachable | Target, basic-attack or use a ready Warrior ability | Damage, health, resource, readiness and hostile response resolve continuously until defeat or disengagement | live class combat | `WOW-006` |
| Reward or required item is eligible | Collect, inspect and equip/use it | Inventory and compatible equipment update; experience may cross a retained level threshold | progression joins equipment | `WOW-002`, `WOW-006` |
| `To Darkmaul Citadel` gate is satisfied; no human invite | Enter the tutorial dungeon | The instance admits the Warrior and supplies autonomous missing party functions | bounded assisted party | `WOW-005`, `WOW-007` |
| Darkmaul route and first boss are complete | Continue required interactions and defeat the final boss | Dungeon completion settles and current routing transitions the same character to Dragon Isles docks | historical capital path rejected | `WOW-003`, `WOW-005`, `WOW-008` |
| Warrior stands at Dragon Isles docks with the final hand-in available | Hand `An End to Beginnings` to Kalecgos | Quest completion, level, abilities and equipment remain on the same controllable character | positive terminal | `WOW-008`, `WOW-010` |

## Strategic and experiential structure

- Local decision: position for one target, keep a legal ability/resource state,
  interpret the current prompt and use the required item or fixture without
  losing track of the immediate objective.
- Medium-term planning: complete only prerequisites that unlock the next main
  stage, compare usable gear, retain learned Warrior actions and enter the
  dungeon with the required route state.
- Long-term structure: authored quest completion and experience progressively
  transform an untrained level-1 character into a level-10-capable participant,
  then the assisted dungeon validates those learned actions before a retained
  region hand-off.
- Common heuristics: follow the tracked objective rather than optional markers;
  keep the current weapon equipped; use class actions when their resource and
  readiness permit; let role-capable followers hold their functions while the
  Warrior maintains target pressure; verify the final hand-in rather than
  treating travel animation as completion.
- Failure attribution: tutorial text, quest predicates, target state, personal
  HUD, item compatibility, party frames and retained quest state distinguish
  navigation, combat, equipment, prerequisite and terminal errors.
- Player-trust factors: one-step teaching, explicit markers, readable resource
  and readiness, visible party condition, objective acknowledgements and a
  retained quest completion make causes inspectable.

## Replay and variation

- Variable parameters: realm and name, incidental target, sampled rewards,
  movement line, timing, mistakes and exact follower combat cadence.
- Fixed comparison packet: faction, race, class, full tutorial choice, required
  quest chain, solo dungeon entry and final hand-in.
- Alternative classes and Horde share much tutorial structure but teach other
  abilities and may change NPC/route text; they require explicit future scopes.
- Optional quests and Housing Skip offer different route/time outcomes and are
  excluded rather than silently unioned.

## Adjacent systems and history

- Similar games: Lineage II, FINAL FANTASY XIV Online, Warframe, Skyrim Special
  Edition and Monster Hunter Wilds share tutorial, quest, combat, equipment,
  party or region-boundary structures.
- Lineage II earns a permanent first class transfer after level and quest gates;
  this character starts as Warrior and retains automatically taught class state.
  FFXIV syncs an existing tank and fixes an exact 1/1/2 NPC roster for one duty;
  Darkmaul is a fresh-character tutorial that admits 1–5 humans and fills
  missing functions. Warframe restores an Orbiter across generated missions;
  WoW follows an authored island into a current regional hand-off.
- Classic branches, former capital routing and twenty years of expansions are
  historical or adjacent modules, not parameters of this one current packet.
- Claim IDs: `WOW-001`–`WOW-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-107`, `ACT-161`, `ACT-190`, `ACT-199`, `ACT-341` | navigation, NPC, combat, ability, item and contextual interaction |
| System Behaviour | `SYS-215`, `SYS-299`, `SYS-362`, `SYS-379`, `SYS-380`, `SYS-716` | live combat, growth, rewards, quest, class effects and follower fill |
| Constraint | `CON-269`, `CON-282`, `CON-395`, `CON-562` | ability, order, compatibility and dungeon roster gates |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-153`, `INF-268` | equipment, local, personal, quest, item, party and tutorial state |
| Objective | `OBJ-137` | retained Exile's Reach-to-Dragon-Isles hand-in |
| Time | `TIM-003` | concurrent real-time world, combat and follower action |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `220` (`GAME-0001`–`GAME-0220`).
- Exact genome matches: none.
- Tied near matches: `GAME-0219` — Lineage II (`19 / 29 = 0.655172`).
- Supported combination subsets: `COMB-0219`.
- Scan date: 2026-09-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0219` — Lineage II | `ACT-008`, `ACT-107`, `ACT-161`, `ACT-190`, `ACT-199`, `SYS-215`, `SYS-299`, `SYS-362`, `SYS-379`, `SYS-380`, `CON-269`, `CON-282`, `CON-395`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `TIM-003` | both start a fresh persistent character, follow marked NPC quests, fight in real time, retain experience levels and equip compatible rewards; Lineage II remains ungrouped and makes level 20 plus quest completion gate a permanent first class transfer, while World of Warcraft fixes Warrior at creation, teaches it step by step, fills a variable-count tutorial dungeon with autonomous functions and requires the later Dragon Isles hand-in | Near, `19 / 29 = 0.655172` |

## Combination status

- `COMB-0219` is a verified strict subset coupling directed tutorial
  information, quest order, persistent character growth, assisted live combat,
  equipment state and the retained Dragon Isles hand-in.
- Every earlier verified combination is tested after registration; supporting
  subsets are recorded rather than inferred from theme.

## Taxonomy impact

- Adds `SYS-716`, `CON-562`, `OBJ-137` and one combination; all other movement,
  interaction, combat, reward, quest, information and time genes are reused.
- No previously reviewed signature or lifecycle changes.
- The new boundaries isolate variable-count tutorial follower fill, its entry
  rule and the exact retained fresh-character terminal.

## Negative results

- `SYS-602`/`CON-503` are not reused: FFXIV fixes a four-member 1/1/2 light party
  with named preset role replacements, whereas Darkmaul admits 1–5 humans and
  supplies missing tutorial functions around that variable roster.
- `SYS-712`/`CON-559` are absent: Warrior is selected at character creation and
  no persistent first class transfer is earned at the terminal.
- `OBJ-113` is not reused: Skyrim escapes one captivity dungeon into open-world
  control; this route teaches through an island, completes a follower dungeon
  and requires a current cross-region quest hand-in.
- Housing Skip, optional quests, capital-city history, later expansion play,
  professions, PvP and endgame do not enter merely because the service exposes
  them.
