---
game_id: GAME-0223
slug: aion-classic
game_title: Aion Classic
analysis_status: reviewed
reviewed: 2026-09-02
combination_ids:
  - COMB-0221
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-190
    - ACT-341
    - ACT-391
  system:
    - SYS-215
    - SYS-362
    - SYS-380
    - SYS-720
    - SYS-721
  constraint:
    - CON-269
    - CON-282
    - CON-563
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-268
  objective:
    - OBJ-139
  time:
    - TIM-003
---

# Game: Aion Classic

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current official North American **Aion Classic** Windows
  service at Patch `5.0`, activated 2026-04-28 and checked 2026-09-02; delivered
  through PURPLE installer `2.26.831.38`. NCSOFT exposes no separate stable game
  executable number, so the dated patch, service and launcher form the
  reproducible version packet.
- Reproducible character and server: official Classic server `Siel`; one fresh
  Elyos Warrior with no transferred resources and no retained completion of
  `Boundary of Light and Darkness`. If Siel or the tutorial is unavailable in
  the declared Classic service, this packet is not silently moved to Live,
  Ascend, another region or another route and must be re-reviewed.
- Primary decision loop: read the floor arrows, current objective, personal
  resources, buff and skill readiness; move to the required encounter; aim and
  strike one reachable hostile or use a legal Warrior skill; survive the live
  response while the tutorial counts the correct enemy class; after each named
  creature, attack its Mystic Cube to request a probabilistic level increase,
  then interact to claim the resulting enhanced equipment; repeat until all
  three objective counts and reward sources are settled, then leave through the
  Daeva of Time.
- Entry and exit: begins with the fresh Elyos Warrior controllable beside the
  Sanctum City Guard and accepting first entry to `Boundary of Light and
  Darkness`. It succeeds only after defeating 20 Invading Balaurs, five Special
  Forces and all three Creatures of Light and Darkness, claiming all three
  Mystic Cubes plus both counted-objective reward boxes, and returning through
  the Daeva of Time to controllable Sanctum state with rewards retained. Leaving
  before those predicates is a failed terminal because re-entry is forbidden.
- Included: direct movement; current-objective and controls guidance; direct
  target combat; Warrior skills; personal health, ability readiness, equipment
  and status information; `Blessing of Light and Darkness`; `Class
  Transformation`, whose attacks have a 30% chance to reset every skill
  cooldown; the three typed defeat counters; Fiery Rantak, Roaring Dahakar and
  Abyssal Karmatan; three Mystic Cubes; probabilistic cube levels up to five;
  equipment enhanced up to +15; two objective reward boxes, consumables and
  title-card bundles; the one-time exit rule.
- Reproducible parameterisation: use the current default Classic rules, Siel,
  Elyos and Warrior; enter through the Sanctum City Guard; follow floor arrows;
  complete all counters; attack each cube before interacting; claim every
  declared reward source; use no account-transferred gear, party assistance or
  event shortcut. Character name, exact combat movement, hit order, cooldown
  resets, cube levels and sampled rewards may vary.
- Excluded: the preceding Poeta route and Ascension; Aion Live and Ascend;
  Asmodian/Pandaemonium routing; Dread Blade and every other class; open-world
  quests, character levelling, flight, gathering, crafting, pets, inventory
  optimisation after exit, groups, legions, trading, Integrated World Exchange,
  PvP, faction war, rifts, raids, fortress sieges, later instances, events,
  passes, store state, account progression and the complete product history.
- Potential scoped modules: the current Poeta-to-Ascension route, one fixed
  flight-enabled quest, one faction-conflict ruleset or one later Classic
  instance each needs its own patch, character, entry and terminal.
- Direct-play status: no authenticated client or tutorial was played. Current
  official NCSOFT patch notes, service pages, launcher metadata and the complete
  official tutorial guide establish every admitted transition. Repository
  reasoning does not claim personal play. No video or audio was opened, played,
  heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `AION-001` | North American Aion separates Classic from Live and Ascend, and current Classic runs Patch 5.0 | Confirmed | Direct | High | P1, P3, P4 |
| `AION-002` | The current official site delivers the Windows service through PURPLE installer `2.26.831.38` | Confirmed | Direct | High | P4 |
| `AION-003` | Siel remains a named Classic server in current Patch 5.0 rules | Confirmed | Direct | High | P1 |
| `AION-004` | `Boundary of Light and Darkness` is the first post-creation tutorial instance and is entered through the faction capital's City Guard | Confirmed | Direct | High | P1, P2 |
| `AION-005` | The tutorial teaches controls and skills while applying `Blessing of Light and Darkness` and a class transformation whose attacks can reset all skill cooldowns | Confirmed | Direct | High | P2 |
| `AION-006` | Completion requires 20 Invading Balaurs, five Special Forces and three distinct Creatures of Light and Darkness | Confirmed | Direct | High | P2 |
| `AION-007` | Each named creature produces a Mystic Cube; attacking can raise it to level five, and interaction grants level-sensitive equipment up to +15 | Confirmed | Direct | High | P2 |
| `AION-008` | The first two objective rewards include consumables and title-card bundles, and the final creature exposes their boxes plus a cube | Confirmed | Direct | High | P2 |
| `AION-009` | Leaving through the Daeva of Time makes the tutorial unavailable for re-entry | Confirmed | Direct | High | P2 |
| `AION-010` | The repository trace reproduces entry, typed counters, combat, cooldown reset, cube upgrade/claim and retained exit without direct play | Observation | Direct | High | V1 |

## Basic data

- Release / origin: NCSOFT; the reviewed North American Aion Classic service is
  maintained separately from Live and Ascend in 2026.
- Platform or physical form: authenticated networked Windows PC client through
  PURPLE; one persistent character on the North American Classic server Siel.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary sources:
  - **[P1]** [official Classic 5.0 patch notes](https://aiononline.plaync.com/en-us/board/classicnotice/view?articleId=69eba8c301bb0567c3a20755),
    for the current patch, new tutorial, Classic-specific Siel rules and dated
    content boundary.
  - **[P2]** [official Boundary of Light and Darkness guide](https://aiononline.plaync.com/en-us/board/ascendguide/view?articleId=69f131e60d32e0377a4c1f3b),
    for entry, controls, buffs, counts, named creatures, cube progression,
    rewards and irreversible exit. The guide is published on the shared current
    Aion surface and Patch 5.0's Classic notes explicitly add the same instance.
  - **[P3]** [official April 28 maintenance](https://lounge.plaync.com/feed/66807?country=US&locale=en-US),
    for Patch 5.0 activation on Classic and separate Live maintenance.
  - **[P4]** [official current Aion service page](https://aiononline.plaync.com/en-us/index?redirect=false),
    for the active North American service, branch navigation and PURPLE
    installer `2.26.831.38`.
- Secondary and reproducible sources:
  - **[V1]** repository-side transition trace from `P1`–`P4`; rules reasoning,
    not direct play.
- Claim IDs: `AION-001`–`AION-010`.

## Mechanical decomposition

### Action Genes

- Existing: `ACT-008`, follow the authored route; `ACT-161`, directly strike a
  reachable hostile; `ACT-190`, activate a legal Warrior skill; `ACT-341`,
  interact with the City Guard, Mystic Cube, reward box or Daeva of Time.
- New `ACT-391`: strike one spawned Mystic Cube before claiming its reward.
- Parameters: City Guard, arrow, target, weapon, skill, creature class, cube,
  cube level, reward source and exit actor.
- Claim IDs: `AION-004`–`AION-010`.

### System Behaviour Genes

- Existing: `SYS-215`, directly commanded live hostile combat; `SYS-362`,
  bounded encounter and reward-source loot; `SYS-380`, typed Warrior-skill
  effects.
- New `SYS-720`: while Class Transformation is active, each attack independently
  has a 30% chance to reset every skill cooldown.
- New `SYS-721`: accepted strikes probabilistically increase a Mystic Cube's
  level up to five, and interaction converts that level into a bounded enhanced
  equipment reward.
- Resolution order: entry applies tutorial guidance and buffs; movement exposes
  the current typed targets; attacks/skills and hostile responses resolve in
  real time; eligible defeats update the relevant counter; each named creature
  spawns a cube; cube attacks may increase level; interaction grants its reward;
  all three counters expose the completion sources; post-completion exit writes
  the terminal.
- Claim IDs: `AION-005`–`AION-010`.

### Constraint Genes

- Existing: `CON-269`, skill target/range/resource/readiness legality;
  `CON-282`, authored objective prerequisites and arrow-led order.
- New `CON-563`: the tutorial admits a fresh eligible character only through
  its faction City Guard and permanently rejects re-entry after the Daeva of
  Time exit.
- Scarce resources: health, ability readiness, target reach, objective-class
  eligibility and the single tutorial admission.
- Claim IDs: `AION-004`–`AION-010`.

### Information Genes

- Existing: `INF-073`, current hotbar and equipment; `INF-115`, locally visible
  targets and hazards; `INF-119`, health, buffs and skill readiness; `INF-125`,
  authored route and objective gates; `INF-128`, reward-source identity and
  resulting equipment; `INF-268`, current controls/objective guidance and its
  completion response.
- New genes: none.
- Claim IDs: `AION-004`–`AION-010`.

### Objective Genes

- New `OBJ-139`: complete all three typed defeat counts, claim every admitted
  cube and objective reward, then return through the Daeva of Time with the
  fresh Classic character's rewards retained.
- Success requires every predicate. A partial counter, unclaimed cube or reward
  box is incomplete; early exit is irreversible failure for this character.
- Claim IDs: `AION-006`–`AION-010`.

### Time Genes

- Existing `TIM-003`: character movement, hostile response, attacks, skill
  readiness and cooldown-reset opportunities advance in real time outside
  blocking interfaces.
- Claim IDs: `AION-005`–`AION-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Current Classic Patch 5.0; fresh Elyos Warrior on Siel | Talk to Sanctum City Guard and accept first entry | Creates the one permitted tutorial instance and applies its guidance/buffs | exact entry and one-use gate | `AION-001`–`AION-005` |
| Current arrow and objective identify eligible hostiles | Move, target, strike or use a ready Warrior skill | Damage, health, readiness and hostile response resolve; an eligible defeat advances only its typed count | live taught combat and counted progress | `AION-005`, `AION-006` |
| Class Transformation active; an attack resolves | Accept its independent 30% check | All skill cooldowns either reset together or remain unchanged | stochastic readiness swing | `AION-005` |
| One named Creature of Light and Darkness is defeated | Approach and strike its Mystic Cube | The cube becomes interactive and may increase by one or more levels up to five | attack-driven reward preparation | `AION-007` |
| Mystic Cube is interactive | Commit its interaction | Level-sensitive enhanced equipment enters the character's reward state | bounded reward settlement | `AION-007` |
| All three typed counters are complete | Claim both objective boxes and final cube | Consumables/title cards and the final enhanced-equipment opportunity settle | complete reward envelope | `AION-006`–`AION-008` |
| Any required predicate is incomplete | Ask Daeva of Time to leave | Returns the character outside and permanently closes re-entry | explicit failed terminal | `AION-009` |
| All counters and rewards settled | Leave through Daeva of Time and inspect control/rewards | Returns to Sanctum with rewards retained and the tutorial closed | positive terminal | `AION-008`–`AION-010` |

## Strategic and experiential structure

- Local: follow the current arrow, identify the target class, keep a legal
  skill/health state, exploit an unexpected cooldown reset and avoid claiming a
  cube before completing the intended upgrade attempts.
- Medium-term: advance all three counters, distinguish named creatures from
  ordinary waves and settle every cube before leaving its encounter locus.
- Long-term: convert a single non-repeatable teaching instance into retained
  equipment, consumables and title cards without triggering the irreversible
  exit early.
- Heuristics: obey the current objective rather than attack arbitrary targets;
  use reset skills promptly; confirm the creature name; strike then interact
  with each cube; inspect all counters and reward sources before the Daeva of
  Time.
- Failure attribution: current-objective text, typed counters, target names,
  buff icons, cooldowns, cube response and final reward boxes separately expose
  combat, classification, readiness, reward and terminal errors.
- Player trust: exact counts, floor arrows, visible buffs/readiness, named
  creatures, cube response text and a warned one-time exit make causes
  inspectable.
- Claim IDs: `AION-004`–`AION-010`.

## Replay and variation

- Character name, positioning, attack/skill order, cooldown-reset results, cube
  levels and sampled equipment vary; branch, server, faction, class, tutorial,
  counts and one-time terminal stay fixed.
- Combat and cube upgrades contain bounded randomness; the three target classes
  and required counts are authored.
- Skill cadence may adapt to random resets, and cube results vary, but early
  exit, party help and account-transferred resources are excluded.
- The same character cannot replay after exit; comparison requires another
  fresh character and lies outside this one retained attempt.

## Adjacent systems and history

- Similar games: World of Warcraft, Lineage II, FINAL FANTASY XIV Online,
  Warframe and Destiny 2 share taught live combat, visible abilities, bounded
  instances or retained equipment rewards.
- World of Warcraft teaches a long quest chain and fills missing dungeon roles;
  this packet is solo, counter-driven and permanently closes one tutorial
  admission. FFXIV fixes a full Duty Support party and three boss gates; Aion
  instead grants self-buffs, random full-cooldown resets and attack-upgraded
  reward cubes. Lineage II earns a class transfer after levels and quest state;
  class growth is outside this packet.
- Classic's earlier patches, Live, Ascend and the full faction-war service are
  historical or adjacent modules, not parameters of this tutorial.
- Claim IDs: `AION-001`, `AION-004`–`AION-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-341`, `ACT-391` | movement, hostile attack, skill, contextual interaction, cube strike |
| System Behaviour | `SYS-215`, `SYS-362`, `SYS-380`, `SYS-720`, `SYS-721` | combat, reward, ability, cooldown reset, cube upgrade |
| Constraint | `CON-269`, `CON-282`, `CON-563` | skill legality, objective order, one-use admission |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-268` | equipment, local, personal, route, reward and tutorial state |
| Objective | `OBJ-139` | complete counters, rewards and retained exit |
| Time | `TIM-003` | concurrent live combat and readiness |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `222` (`GAME-0001`–`GAME-0222`).
- Exact genome matches: none.
- Tied near matches: `GAME-0221` — World of Warcraft (`16 / 30 = 0.533333`).
- Supported combination subsets: `COMB-0221`.
- Scan date: 2026-09-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0221` — World of Warcraft | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-341`, `SYS-215`, `SYS-362`, `SYS-380`, `CON-269`, `CON-282`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-268`, `TIM-003` | both teach direct real-time character combat through current instructions, contextual interactions, visible skills and bounded rewards; World of Warcraft retains levels, equipment and a quest chain through an automatically filled dungeon to a later regional hand-in, while Aion fixes a solo one-use tutorial whose attacks can reset every cooldown and upgrade non-hostile reward cubes before an irreversible exit; the 16 shared genes cover `16 / 21 = 0.761905` of Aion's smaller genome | Near, `16 / 30 = 0.533333` |

## Combination status

- `COMB-0221` is a verified strict subset coupling taught live combat, random
  cooldown resets, attack-upgraded reward cubes, one-use admission and a
  retained post-reward exit.
- Every earlier verified combination is tested after registration; supporting
  subsets are recorded rather than inferred from MMORPG theme.

## Taxonomy impact

- Adds `ACT-391`, `SYS-720`, `SYS-721`, `CON-563`, `OBJ-139` and one
  combination; all other movement, combat, ability, reward, information and
  time genes are reused.
- No previously reviewed signature or lifecycle changes.
- New boundaries isolate attack-prepared reward claiming, global probabilistic
  cooldown reset, probabilistic cube level/reward conversion and one-use exit.

## Negative results

- `SYS-299`, `SYS-379`, `SYS-712` and `CON-559` are absent: levelling, quest
  retention and Ascension/class transfer lie before the declared entry.
- `SYS-716` and `CON-562` are absent: the packet neither fills a human roster
  with followers nor uses World of Warcraft's quest-gated 1–5-player rule.
- `SYS-602`–`SYS-606` are absent: no fixed Duty Support party, role/enmity
  structure or three-boss sequence is admitted.
- `ACT-161` covers hostile attacks only; `ACT-391` is required because striking
  the non-hostile cube prepares a reward rather than dealing combat damage.
- Flight, PvP, faction war, open-world questing, economy and full service
  history do not enter merely because Aion Classic exposes them elsewhere.
