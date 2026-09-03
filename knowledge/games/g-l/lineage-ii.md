---
game_id: GAME-0219
slug: lineage-ii
game_title: Lineage II
analysis_status: reviewed
reviewed: 2026-09-01
combination_ids:
  - COMB-0217
gene_ids:
  action:
    - ACT-008
    - ACT-107
    - ACT-161
    - ACT-190
    - ACT-199
    - ACT-387
  system:
    - SYS-215
    - SYS-299
    - SYS-362
    - SYS-379
    - SYS-380
    - SYS-712
  constraint:
    - CON-269
    - CON-282
    - CON-395
    - CON-559
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-128
  objective:
    - OBJ-136
  time:
    - TIM-003
---

# Game: Lineage II

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current official North American **Lineage II Live** Windows
  service, checked 2026-09-01 after the September 1 maintenance; July 14
  `Server War: Dimensional Clash` update plus the August 25 content update,
  delivered by PURPLE installer `2.26.831.38`. NCSOFT exposes no separate stable
  Live executable build number, so this dated update, maintenance and launcher
  boundary is the reproducible version packet.
- Reproducible character and server: existing North American Live server
  `Chronos`; one fresh male Human Fighter with an arbitrary unique name and no
  retained quest history. If Chronos or the declared quest is absent from the
  current Live client, this packet is not silently moved to another branch or
  server and must be re-reviewed.
- Primary decision loop: read the class-transfer quest instruction, map/marker
  and nearby world state; talk to the addressed NPC; move through the training
  route; select a reachable hostile; use ordinary weapon attacks or learned
  Fighter skills while managing health, readiness and equipment; collect
  eligible rewards and experience; turn in the next objective; at level 20
  choose Warrior and verify the retained class and quest result.
- Entry and exit: begins after selecting `Live` in PURPLE, entering Chronos and
  confirming the fresh Human Fighter at the level-1 tutorial state. It succeeds
  only when `Path of Destiny - Beginning` is complete, level 20 has been
  reached, the Warrior first class transfer is accepted and the same character
  returns to controllable server state with that class and quest completion
  retained. Level 20 without the transfer, or an unconfirmed offer, is not the
  terminal.
- Included: one fresh character; Human Fighter starting state; required NPC
  conversations, movement, targeting, attacks, Fighter skills, quest markers,
  experience, levels, quest rewards, carried/equipped items and hostile defeat
  in `Path of Destiny - Beginning`; ordinary death/return if encountered; one
  compatible first class fixed as Warrior; persistent quest, level, class,
  inventory and equipment state at the terminal.
- Reproducible parameterisation: use the current default Live rules; choose
  Chronos, male Human Fighter and Warrior; do not transfer resources from
  another character; follow only the current quest objectives in their shown
  order. Character name, incidental hostile identity within an objective,
  incidental drop, combat spacing and completion time may vary. Do not use
  paid boosts, event shortcuts, another player's power-levelling or unattended
  play.
- Excluded: Classic, Aden, Wolf, Samurai, test and future branches; the new Live
  server announced for 2026-09-15 because it was unavailable on the review
  date; Naia or another server; Ertheia and every race/class other than the
  fixed Human Fighter-to-Warrior path; later class transfers, later quests and
  full levelling; parties, clans, mentors, trading, crafting, auction/economy,
  monetisation, auto-hunt as an unattended strategy, PvP, Olympiad, raids,
  instances, castle sieges, events and the complete product history.
- Potential scoped modules: one later Live quest, a fixed party instance,
  Classic's early class route or Aden's accelerated route each needs its own
  current branch, server, character, entry and terminal.
- Direct-play status: no authenticated client or quest was played. Current
  official NCSOFT pages establish branch, delivery, update and service; official
  Live patch notes establish the integrated class quest, level/race boundary
  and retained tutorial item. Repository transitions model only those textual
  rules. No video or audio was opened, played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `L2-001` | The current North American product separates Live from Classic, Aden, Wolf and Samurai and presents Live as the original long-running branch | Confirmed | Direct | High | P1, P2 |
| `L2-002` | The reviewed Live boundary is the July 14 update plus the August 25 update and September 1 maintenance, delivered through PURPLE `2.26.831.38`; no separate public game-build number is exposed | Confirmed | Direct | High | P2, P3, P4, P5 |
| `L2-003` | Chronos is an official North American Lineage II Live server and is fixed rather than treating server choice as interchangeable | Confirmed | Corroborated | Medium | P6 |
| `L2-004` | The integrated non-Ertheia first-transfer route is `Path of Destiny - Beginning`, spans levels 1–20 and is distinct from later transfer/growth quests | Confirmed | Direct | High | P7 |
| `L2-005` | A later official Live rule still identifies the tutorial Teleportation Cubic as a reward from `Path of Destiny - Beginning` | Confirmed | Direct | High | P8 |
| `L2-006` | The current branch supports Humans and many class paths, while Human Fighter has a compatible first path to Warrior | Confirmed | Corroborated | High | P1, P7, S1 |
| `L2-007` | The scoped loop joins NPC quest prompts, movement, target combat, experience levels, equipment/rewards and persistent quest flags before transfer | Observation | Corroborated | High | P7, P8, S1 |
| `L2-008` | Level 20 plus completed quest state gates the retained first transfer; neither threshold alone is the terminal | Observation | Corroborated | High | P7, S1 |
| `L2-009` | The future Live server announced for September 15 is unavailable on the review date and cannot replace a current packet | Confirmed | Direct | High | P9 |
| `L2-010` | The repository trace reproduces branch/server entry, quest, combat experience, level gate, class choice and retained terminal without direct play | Observation | Direct | High | V1 |

## Basic data

- Release / origin: NCSOFT; North American Lineage II launched in 2004 and the
  scoped Live branch remains maintained in 2026.
- Platform or physical form: authenticated networked Windows PC client through
  PURPLE; one persistent character on one North American Live server.
- Puzzle family: real-time system pressure; tactical forecast and counterplay;
  ordered dependency sequencing; persistent character progression.
- Primary sources:
  - **[P1]** [official current overview](https://na-lineage2.plaync.com/en-us/about/index),
    for branch distinctions, races and class-path scale.
  - **[P2]** [official current site](https://na-lineage2.plaync.com/en-us/index),
    for the North American service and Live surface.
  - **[P3]** [official July 2026 update](https://na-lineage2.plaync.com/en-us/conts/260708_update),
    for `Server War: Dimensional Clash`, applied July 14.
  - **[P4]** [official August Update Patch Notes](https://na-lineage2.plaync.com/en-us/board/l2live/view?articleId=6a8c7c5038eb0528f9001ca8),
    for changes applied during August 25 maintenance.
  - **[P5]** [official September 1 maintenance](https://na-lineage2.plaync.com/en-us/board/l2live/view?articleId=6a960ae34b52050c9a2871d3),
    for the review-day boundary; official download exposes PURPLE installer
    `2.26.831.38`.
  - **[P6]** [official all-server player spotlights](https://www.lineage2.com/en-us/news/lineage-ii-all-servers-player-spotlights),
    for Chronos and Naia as named Live servers, with Chronos fixed here.
  - **[P7]** [official Fafurion Supplemental Update Part II notes](https://www.lineage2.com/en-us/news/lineage-ii-fafurion-supplemental-update-part-ii-now-live),
    for integrated class quests, `Path of Destiny - Beginning`, levels 1–20,
    non-Ertheia eligibility and distinct later quest bands.
  - **[P8]** [official Hero's Tome patch notes](https://www.lineage2.com/en-us/news/heros-tome-patch-notes),
    for the tutorial quest's retained Teleportation Cubic.
  - **[P9]** [official new Live server announcement](https://na-lineage2.plaync.com/en-us/board/l2live/view?articleId=6a872fe746be804931c310b0),
    for the September 15 future boundary.
- Secondary and reproducible sources:
  - **[S1]** [Lineage II Wiki: Human Fighter](https://lineage2.fandom.com/wiki/Human_Fighter),
    checked 2026-09-01 only to corroborate the Human Fighter-to-Warrior edge.
  - **[V1]** repository-side transition trace from `P1`–`P9` and `S1`; rules
    reasoning, not direct play.
- Claim IDs: `L2-001`–`L2-010`.

## Mechanical decomposition

### Action Genes

- Existing: `ACT-008`, move through the quest route; `ACT-107`, talk to the
  addressed NPC; `ACT-161`, strike a reachable hostile; `ACT-190`, activate a
  learned Fighter skill; `ACT-199`, take/equip a compatible reward or drop.
- New `ACT-387`: confirm one eligible first class transfer from the offered
  persistent class branches.
- Parameters: server, NPC, destination, target, weapon, skill, equipment, quest
  stage, level and offered class.
- Claim IDs: `L2-004`–`L2-010`.

### System Behaviour Genes

- Existing: `SYS-215`, live hostile combat; `SYS-299`, experience thresholds to
  retained levels; `SYS-362`, bounded loot/progression awards; `SYS-379`,
  authored quest-state advancement; `SYS-380`, typed Fighter-skill effects.
- New `SYS-712`: replace the eligible starting class with the confirmed first
  class while retaining character, server, level, quest, inventory and
  equipment and updating compatible skills.
- Resolution order: branch/server/character selection creates the start; NPC
  dialogue exposes the objective; movement/targeting admits combat or hand-in;
  attacks/skills resolve; rewards advance experience and quest; thresholds
  raise level; completed quest plus level 20 exposes the class offer; confirming
  Warrior writes the retained terminal.
- Claim IDs: `L2-004`–`L2-010`.

### Constraint Genes

- Existing: `CON-269`, skill target/range/resource/readiness; `CON-282`, ordered
  quest prerequisites; `CON-395`, equipment/skills compatible with character.
- New `CON-559`: first transfer requires eligible starting class/race, level,
  completed transfer quest and one compatible offered destination.
- Scarce resources: health, skill readiness, target reach, compatible
  equipment, quest prerequisites, experience and exclusive class commitment.
- Claim IDs: `L2-004`, `L2-006`–`L2-010`.

### Information Genes

- Existing: `INF-073`, current weapon/items/hotbar; `INF-115`, nearby NPCs and
  hostiles through local sight/world response; `INF-119`, health, level,
  experience, class, skills and readiness; `INF-125`, quest/marker/route;
  `INF-128`, reachable reward/loot identity and compatibility.
- New genes: none.
- Claim IDs: `L2-004`–`L2-010`.

### Objective Genes

- New `OBJ-136`: complete `Path of Destiny - Beginning`, reach level 20,
  confirm Warrior and regain control with quest and transfer retained on the
  fixed Live character.
- Only all predicates together are success. Death or a missed interaction can
  be retried; leaving, deleting the character, changing branch, or level 20
  without transfer is not success.
- Claim IDs: `L2-004`–`L2-010`.

### Time Genes

- Existing `TIM-003`: movement, hostile action, attacks, skill readiness and
  server state continue in real time outside blocking interfaces.
- Claim IDs: `L2-007`–`L2-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Current PURPLE and service available | Select `Live`, Chronos and create Human Fighter | Creates one persistent level-1 character; another branch/server is not interchangeable | exact entry | `L2-001`–`L2-003`, `L2-006` |
| Quest presents an addressed NPC | Talk and accept/continue the offer | Journal records the stage and reveals the next requirement | quest-driven route | `L2-004`, `L2-007` |
| Required hostile reachable | Select it and attack or use a legal skill | Damage, readiness, health and response resolve until defeat/disengagement | live target combat | `L2-007` |
| Eligible defeat or hand-in resolves | Collect/accept reward and credit | Items/experience enter persistent state and objective advances | reward, growth and order join | `L2-004`, `L2-007` |
| Experience crosses a threshold | Accept level transition | The same character retains the level and declared opportunities | persistent prerequisite | `L2-007`, `L2-008` |
| Level 20 or quest complete, not both | Inspect transfer | Warrior cannot settle the terminal | both gates required | `L2-008` |
| Human Fighter level 20 and quest complete | Confirm Warrior | Class becomes Warrior; compatible skills update and other state persists | first class transformation | `L2-006`, `L2-008` |
| Transfer settled | Return to control and inspect class/quest | Warrior, level 20 and completion remain on Chronos | positive terminal | `L2-008`, `L2-010` |

## Strategic and experiential structure

- Local: identify NPC/marker, choose route and target, manage distance, health
  and readiness, equip compatible rewards and turn in objectives.
- Medium-term: keep the quest advancing, retain useful equipment, reach level
  20 without paid/social shortcuts and preserve the Human Fighter path.
- Long-term: turn one fresh Live character into a level-20 Warrior by satisfying
  both the authored quest and exclusive class commitment.
- Heuristics: follow the current marker; verify NPC/hostile identity; use only
  current-class skills; distinguish experience threshold from quest completion;
  inspect retained class before declaring success.
- Failure attribution: branch/server, prerequisite, target, combat state,
  compatibility, quest credit, level and confirmation are separately visible.
- Player trust: journal, markers, experience, character panel, inventory,
  transfer offer and post-transfer class explain progression.
- Claim IDs: `L2-004`–`L2-010`.

## Replay and variation

- Character name, combat spacing, incidental drops, damage and time vary;
  server, race, starting class, quest and destination class stay fixed.
- Quest/class path is authored; incidental drops and live-world timing may vary
  without changing terminal identity.
- Attack/skill order and movement vary; paid acceleration, external resources
  and unattended auto-hunt are excluded.
- Replay normally compares another class or later progression, outside scope.

## Adjacent systems and history

- Classic, Aden, Wolf, Samurai, another server or race/class are separate
  product/rules packets, not interchangeable parameters.
- Similar games: FINAL FANTASY XIV Online, Skyrim Special Edition, Warframe,
  Cyberpunk 2077 and Black Myth: Wukong share live combat, growth, quest state
  or character decisions.
- FFXIV's Sastasha syncs an existing Gladiator and supplies preset NPC roles;
  this packet starts an ungrouped level-1 character and permanently replaces
  its starting class. Skyrim binds ancestry but no class transfer. Warframe
  ranks equipment and restores a hub; this levels one character and class path.
- Claim IDs: `L2-001`, `L2-004`–`L2-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-107`, `ACT-161`, `ACT-190`, `ACT-199`, `ACT-387` | navigation, NPC, target, attack, equipment, class choice |
| System Behaviour | `SYS-215`, `SYS-299`, `SYS-362`, `SYS-379`, `SYS-380`, `SYS-712` | combat, experience, reward, quest, skill, transfer |
| Constraint | `CON-269`, `CON-282`, `CON-395`, `CON-559` | ability, quest, compatibility, class gates |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128` | equipment, local, character, quest, reward state |
| Objective | `OBJ-136` | retained level-20 Warrior terminal |
| Time | `TIM-003` | concurrent live world and combat |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `218` (`GAME-0001`–`GAME-0218`).
- Exact genome matches: none.
- Tied near matches: `GAME-0205` — The Witcher 3: Wild Hunt (`15 / 37 = 0.405405`).
- Supported combination subsets: `COMB-0217`.
- Scan date: 2026-09-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0205` — The Witcher 3: Wild Hunt | `ACT-008`, `ACT-107`, `ACT-161`, `ACT-190`, `ACT-199`, `SYS-215`, `SYS-379`, `CON-269`, `CON-282`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `TIM-003` | both follow a marked open-world quest through NPC dialogue, equipment and live weapon/ability combat; The Witcher prepares from sensory clues and settles a monster trophy, while Lineage II converts retained experience into level 20 and makes quest completion jointly gate a permanent first class transfer | Near, `15 / 37 = 0.405405` |

## Taxonomy impact

- Added `ACT-387`, `SYS-712`, `CON-559`, `OBJ-136`, one combination and
  existing family memberships.
- Generic movement, combat, ability, experience, quest, equipment and
  information boundaries remain parameterised; new records isolate only the
  persistent transfer commitment and terminal.
- No lifecycle or previously reviewed signature changed.

## Negative results

- `ACT-340` changes a team-spawn class, not a persistent quest-earned class.
- `ACT-238`/`CON-342` configure a starting build budget, absent here.
- `SYS-601` temporarily level-syncs; this level is permanently earned.
- `SYS-603` party enmity is not required by the solo quest.
- Level 20, one kill or one hand-in is not terminal; completed quest plus
  retained Warrior is required.
- Events, future server, later classes, raids, sieges, store and full history do
  not enter merely because the service exposes them.
