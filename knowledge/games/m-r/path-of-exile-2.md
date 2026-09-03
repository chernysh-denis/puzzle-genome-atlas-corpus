---
game_id: GAME-0162
slug: path-of-exile-2
game_title: Path of Exile 2
analysis_status: reviewed
reviewed: 2026-08-27
combination_ids:
  - COMB-0160
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-191
    - ACT-199
    - ACT-223
    - ACT-263
    - ACT-264
    - ACT-265
    - ACT-266
  system:
    - SYS-215
    - SYS-251
    - SYS-299
    - SYS-449
    - SYS-450
    - SYS-451
    - SYS-452
    - SYS-453
    - SYS-454
    - SYS-455
    - SYS-456
  constraint:
    - CON-269
    - CON-270
    - CON-282
    - CON-394
    - CON-395
    - CON-396
    - CON-397
  information:
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-142
    - INF-175
    - INF-176
    - INF-177
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Path of Exile 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: PC Early Access patch `0.5.4f`, solo Standard Softcore;
  one fresh Warrior from first control in the Riverbank through Act 1.
- Primary decision loop: explore each generated campaign area, read hostile
  attacks, combine weapon attacks, active Skill Gems, socketed Supports,
  directional dodge and charged flasks, then turn loot, experience, passive
  points and currency into a legal build able to defeat the next authored
  quest gate.
- Entry and exit: begin when the Warrior gains control in the Riverbank after
  escaping execution; finish after defeating Count Geonor, speaking to the
  Hooded One and committing `Travel East`, which crosses into the first Act 2
  state. Act 2 play is excluded.
- Included: mandatory Act 1 quest progression through Ogham; instantiated area
  layouts and encounters; live melee combat; directional dodge and hold-to-
  sprint; Life, Mana and flask charges; experience, levels and connected
  Passive Skill Tree allocation; Uncut Skill and Support Gem engraving;
  Support sockets and compatibility; equipment drops, rarity, affixes, level,
  attribute and weapon requirements; rectangular inventory placement; one
  ordinary currency-item craft; checkpoints, waypoints, Softcore death reset;
  Count Geonor's two-phase terminal fight.
- Excluded: optional Act 1 quests and bosses except incidental encounters;
  Fate of the Vaal league mechanics; party play, trade and the account economy;
  Hardcore; Ascendancy; Acts 2 and later, Cruel, endgame and Atlas; exhaustive
  classes, skills, supports, items, recipes and balance values; cosmetics,
  microtransactions, achievements, races, private leagues and modifications.
- Potential scoped modules: one named class build; current Fate of the Vaal
  league systems; party/trade economy; the complete released campaign;
  post-campaign Atlas and pinnacle progression.
- Direct-play status: no authenticated Early Access campaign was played for
  this unit. Current official pages establish version, campaign, skill,
  support, equipment and passive-tree boundaries; the official community wiki
  corroborates reproducible Act 1, checkpoint, death, gem, item and boss
  transitions. Exact sampled layouts and drops remain bounded uncertainty.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `POE2-001` | Patch 0.5.4f is the current public Early Access game patch at review time | Confirmed | Corroborated | High | P1, P2 |
| `POE2-002` | Act 1 advances through authored Ogham quest gates inside re-instantiated combat areas and ends with Count Geonor | Confirmed | Corroborated | High | P3, S1, S2 |
| `POE2-003` | Combat is continuous and permits directional dodge, hold-to-sprint and skill cancellation against telegraphed attacks | Confirmed | Corroborated | High | P4, S3 |
| `POE2-004` | Uncut Gems create chosen skills or Supports, and compatible Supports socket into active skills to modify them | Confirmed | Corroborated | High | P3, P4, S4 |
| `POE2-005` | Experience levels grant character growth and passive points allocated through connected tree nodes | Confirmed | Corroborated | High | P5, S5, S6 |
| `POE2-006` | Dropped equipment varies by rarity and affixes and remains gated by inventory space, slot and character requirements | Confirmed | Corroborated | High | P3, S7, S8, S9 |
| `POE2-007` | An eligible currency item directly transforms a target item's rarity, affixes or sockets under that currency's rules | Confirmed | Corroborated | High | S9, S10 |
| `POE2-008` | Checkpoints refill resources; Softcore campaign death returns the character while resetting the area, ground loot and current boss | Confirmed | Corroborated | High | S11, S12, S13 |
| `POE2-009` | Count Geonor has a second full-life form, and victory opens the Hooded One's Travel East transition into Act 2 | Confirmed | Corroborated | High | S1, S2, S14 |

## Basic data

- Release / origin: Grinding Gear Games; Early Access began 6 December 2024;
  scoped public patch `0.5.4f`, released 12 August 2026.
- Platform or physical form: online-authenticated isometric action RPG; this
  scope uses the PC solo Standard Softcore campaign rules.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing; inventory and fixture dependencies.
- Primary sources:
  - **[P1]** [official 0.5.4f patch notes](https://www.pathofexile.com/forum/view-thread/3996513),
    for the current patch boundary and dodge, targeting and shapeshift fixes.
  - **[P2]** [official Path of Exile 2 patch index](https://www.pathofexile.com/forum/view-forum/2222),
    for the reviewed release sequence.
  - **[P3]** [official Early Access overview](https://pathofexile2.com/early-access),
    for Ogham, classes, Skill Gems, Supports and equipment depth.
  - **[P4]** [official Third Edict mechanics page](https://pathofexile2.com/edict),
    for hold-to-sprint and the current Support Gem model.
  - **[P5]** [official Passive Skill Tree overview](https://pathofexile2.com/game/passive-skill-tree),
    for connected passive development.
- Secondary and reproducible sources:
  - **[S1]** [Act 1 record](https://www.poe2wiki.net/wiki/Act_1), for the Ogham
    quest sequence and Count Geonor boundary.
  - **[S2]** [Count Geonor record](https://www.poe2wiki.net/wiki/Count_Geonor),
    for the required terminal fight and its two phases.
  - **[S3]** [Dodge roll record](https://www.poe2wiki.net/wiki/Dodge_roll), for
    direction, avoidance interval, cancellation and sprint transition.
  - **[S4]** [Gem record](https://www.poe2wiki.net/wiki/Gem), for Uncut Gem
    engraving, active skills, Supports and socket rules.
  - **[S5]** [Level record](https://www.poe2wiki.net/wiki/Level), for
    experience thresholds, resource growth and passive points.
  - **[S6]** [Passive Skill Tree record](https://www.poe2wiki.net/wiki/Passive_skill_tree),
    for connected allocation and gold refunds.
  - **[S7]** [Equipment record](https://www.poe2wiki.net/wiki/Equipment), for
    equipment slots and requirements.
  - **[S8]** [Rarity record](https://www.poe2wiki.net/wiki/Rarity), for normal,
    magic, rare and unique item boundaries.
  - **[S9]** [Modifier record](https://www.poe2wiki.net/wiki/Modifier), for
    affix classes and item limits.
  - **[S10]** [Crafting record](https://www.poe2wiki.net/wiki/Crafting), for
    currency-target eligibility and deterministic mutation classes.
  - **[S11]** [Checkpoint record](https://www.poe2wiki.net/wiki/Checkpoint), for
    refill, respawn and within-area travel.
  - **[S12]** [Death record](https://www.poe2wiki.net/wiki/Death), for Softcore
    campaign area, ground-item and boss reset.
  - **[S13]** [Flask record](https://www.poe2wiki.net/wiki/Flask), for charges
    gained from monsters, wells and checkpoints.
  - **[S14]** [Acts route guide](https://www.poe2wiki.net/wiki/Guide:Acts_quick_guide),
    for the post-Geonor Hooded One transition.
- Claim IDs: `POE2-001`–`POE2-009`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate the Warrior; `ACT-161`, aim and strike
  with the equipped weapon or active skill; `ACT-191`, allocate a passive
  point; `ACT-199`, collect and equip compatible loot; `ACT-223`, commit a
  directional dodge against a telegraphed attack.
- New genes: `ACT-263`, engrave one Uncut Gem into a selected active Skill or
  Support; `ACT-264`, socket or remove one compatible Support; `ACT-265`, apply
  one currency item to an eligible item; `ACT-266`, activate a charged Life or
  Mana Flask.
- Parameters: class, weapon, skill, target, gem level, support category,
  inventory cells, currency class, flask charges and dodge vector.
- Claim IDs: `POE2-003`–`POE2-008`.

### System Behaviour Genes

- Existing genes: `SYS-215`, resolve directly commanded real-time hostile
  combat; `SYS-251`, advance the authored cross-region campaign sequence;
  `SYS-299`, convert experience thresholds into levels and passive points.
- New genes: `SYS-449`, instantiate an authored campaign-area identity with a
  sampled local layout and encounters; `SYS-450`, sample eligible item bases,
  rarities and affixes from combat sources; `SYS-451`, grant a Skill from its
  Gem and compose socketed Support modifications; `SYS-452`, transform an
  eligible item according to one currency item's rules; `SYS-453`, derive
  usable skills and combat statistics from attributes, passives and equipment;
  `SYS-454`, consume and replenish flask charges; `SYS-455`, reset the current
  campaign area and boss after Softcore death; `SYS-456`, resolve dodge start,
  direction and cancellation against overlapping attacks.
- Resolution order: an authored zone is instantiated; movement and combat
  reveal local threats; kills award experience, flask charges, Gems and item
  drops; the player fits, equips, engraves, sockets, crafts and allocates;
  checkpoints refill and anchor failure recovery; mandatory quest gates open
  the Manor and Count Geonor; his defeat opens Travel East.
- Claim IDs: `POE2-002`–`POE2-009`.

### Constraint Genes

- Existing genes: `CON-269`, skill use needs legal target, range, Mana and
  readiness; `CON-270`, passive allocation is bounded by points and connected
  branch access; `CON-282`, mandatory Act 1 gates occur in authored order.
- New genes: `CON-394`, carried items need compatible rectangular inventory
  cells, stacks or equipment slots; `CON-395`, equipment and skills require
  current level, attributes and weapon compatibility; `CON-396`, a Support
  needs an eligible free socket and compatible category/attribute budget;
  `CON-397`, currency use requires an eligible item state and respects rarity,
  affix, socket and corruption bounds.
- Scarce strategic resources: Life, Mana, flask charges, inventory cells,
  passive points, currency items, compatible sockets and safe attack windows.
- Claim IDs: `POE2-002`–`POE2-009`.

### Information Genes

- Existing genes: `INF-115`, sight and sound expose only local hostile state;
  `INF-119`, Life, Mana, experience, attributes and build state are visible;
  `INF-125`, explored map and quest gates are visible; `INF-128`, ground loot
  and inventory compatibility are visible; `INF-142`, attack animation and
  sound cue reactive timing.
- New genes: `INF-175`, item panels expose rarity, affixes, requirements and
  equipment comparison; `INF-176`, Skills expose sockets, Support
  compatibility, cost and modified effect; `INF-177`, the Passive Tree exposes
  connected nodes, effects, available points and refund cost.
- Claim IDs: `POE2-002`–`POE2-009`.

### Objective Genes

- Existing gene: `OBJ-080`, defeat Count Geonor as the route guardian and
  cross the opened Travel East threshold into Act 2.
- Success, evaluation and failure: Geonor's defeat plus the Hooded One
  transition satisfies the route; ordinary death resets the current area and
  does not terminate the Softcore campaign.
- Claim IDs: `POE2-002`, `POE2-008`, `POE2-009`.

### Time Genes

- Existing gene: `TIM-003`, movement, attacks, recovery, hostile behaviour and
  boss phases continue in real time while the player retains eligible inputs.
- Parameters: attack time, recovery, dodge interval, sprint onset, skill cost,
  flask recovery and checkpoint reset.
- Claim IDs: `POE2-003`, `POE2-008`, `POE2-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| An Uncut Skill Gem is carried | Engrave one eligible offered skill | The Uncut Gem is replaced by that Skill Gem and the skill becomes assignable | selected action acquisition | `POE2-004` |
| A Skill has a free compatible socket | Socket one eligible Support Gem | The Support occupies the socket and changes the declared skill properties or cost | compositional skill build | `POE2-004` |
| A passive point and connected node exist | Allocate that node | The point is spent and the node's stat modification joins the character build | connected build growth | `POE2-005` |
| An item lies on the ground | Pick it up with enough free cells | The item enters a compatible rectangular inventory placement; otherwise pickup fails | spatial carrying limit | `POE2-006` |
| Equipment requirements are met | Equip the item in its matching slot | It replaces prior slot state and contributes its declared stats and usable weapon skills | requirement-gated build | `POE2-006` |
| An eligible currency and target item exist | Apply the currency | The currency is consumed and the target receives the declared legal rarity, affix or socket mutation | item-state transformation | `POE2-007` |
| A flask has at least one use available | Activate the Life or Mana Flask | Charges are consumed and the declared recovery effect begins immediately | rechargeable survival resource | `POE2-008` |
| A checkpoint is approached | Enter its activation radius | Life, Mana, Flasks and Charms refill and the checkpoint becomes available for respawn/travel | recovery anchor | `POE2-008` |
| The Warrior dies in a campaign area | Choose checkpoint respawn | The character returns without XP penalty, while the area, ordinary monsters, ground items and current boss reset | recoverable failure with world loss | `POE2-008` |
| A telegraphed Geonor attack is beginning | Dodge across a legal direction | The start interval avoids eligible hits, moves the Warrior and cancels compatible recovery, but later overlap can still hit | directional timing defence | `POE2-003`, `POE2-009` |
| Geonor's first form reaches zero Life | Continue the encounter | The second form begins with a full Life pool and its distinct attack sequence | staged terminal guardian | `POE2-009` |
| Count Geonor is defeated | Speak to the Hooded One and select Travel East | Act 1 completes and control crosses into the first Act 2 state | scoped objective completion | `POE2-009` |

## Strategic and experiential structure

- Local decision: attack through recovery or dodge; spend Mana on a supported
  skill or preserve it; drink a limited flask now; pick up a large item or
  preserve inventory cells; socket damage, control or efficiency support.
- Medium-term planning: keep weapon and attribute requirements aligned with
  connected passive choices, compare affixes, reserve currency for useful
  bases and activate checkpoints before dangerous encounters.
- Long-term structure: convert experience, drops, Gems and currency across the
  mandatory Ogham route into a legal build that can survive both Geonor forms.
- Common heuristics: move out of delayed ground attacks; avoid overcommitting
  long animations; keep Life Flask charges for boss pressure; use comparison
  panels before replacing requirement-sensitive equipment.
- Failure attribution: Life/Mana, flask charges, skill costs, item
  requirements, passive connections, attack tells and reset checkpoints make
  most failures causal; sampled drops and layouts remain explicit uncertainty.
- Claim IDs: `POE2-003`–`POE2-009`.

## Replay and variation

- What changes between sessions: local zone layouts, encounter placement,
  item bases, rarity and affixes, Gem timing, chosen skills, passive route,
  equipment and tactical boss responses.
- Randomness or procedural generation: campaign identity and quest order are
  authored, while each local area instance and eligible loot outcome are
  sampled. Enemy action selection adds bounded combat uncertainty.
- Multiple viable strategies: weapon, Skill, Support, passive and equipment
  combinations can trade area damage, single-target damage, control, defence,
  speed and resource efficiency while reaching the same Act 1 boundary.
- Typical replay motive: try a different class or build path, improve Geonor
  execution or experience different layouts and drops.
- Claim IDs: `POE2-002`–`POE2-009`.

## Adjacent systems and history

- Direct predecessors: Diablo-style action RPGs provide real-time loot and
  build progression; Path of Exile contributes currency crafting, support
  composition and a large connected passive graph.
- Variants: league mechanics add a separate seasonal rule layer; Hardcore
  changes death stakes; party/trade changes ownership and economy.
- Similar games: Elden Ring shares telegraphed real-time defence, checkpoint
  recovery and requirement-sensitive builds; Monster Hunter Wilds shares
  equipment preparation and staged boss combat.
- Important differences: active skills are itemised through Gems and Supports,
  ordinary currency directly edits items, and Softcore death resets the local
  campaign instance instead of leaving a recoverable currency marker.
- Claim IDs: `POE2-003`–`POE2-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-191`, `ACT-199`, `ACT-223`, `ACT-263`–`ACT-266` | chosen class, skill and item are parameters |
| System Behaviour | `SYS-215`, `SYS-251`, `SYS-299`, `SYS-449`–`SYS-456` | layouts, drops, affixes and balance values are parameters |
| Constraint | `CON-269`, `CON-270`, `CON-282`, `CON-394`–`CON-397` | level, attributes, sockets and inventory geometry are parameters |
| Information | `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-142`, `INF-175`–`INF-177` | panel layout and cue presentation are parameters |
| Objective | `OBJ-080` | optional bosses and later acts are excluded |
| Time | `TIM-003` | combat cadence is a parameter |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `161` (`GAME-0001`–`GAME-0161`).
- Exact genome matches: none.
- Tied near matches: `GAME-0144` — Clair Obscur: Expedition 33 (`12 / 60 = 0.200000`).
- Supported combination subsets: `COMB-0160`.
- Scan date: 2026-08-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0144` — Clair Obscur: Expedition 33 | navigation, direct attacks, passive allocation, reactive dodge, experience progression, build gates, map/quest information, attack cues and real-time defensive timing | Path of Exile 2 keeps all hostile combat continuous and adds generated areas, itemised Skill/Support composition, currency crafting, rectangular inventory, charged flasks and area-reset death; Clair Obscur structures attacks in turns around a persistent party and mastered passive loadouts | Near, `0.200000` |

## Combination status

- `COMB-0160` is a verified strict subset coupling Skill/Support build
  composition, connected passive development, charged recovery and
  checkpoint-reset combat with the Act 1 guardian threshold.
- No earlier verified combination is a proper subset of this complete genome.

## Reuse and novelty decision

- Reused genes: nineteen existing genes retain their established boundaries.
- New genes: `ACT-263`–`ACT-266`, `SYS-449`–`SYS-456`, `CON-394`–`CON-397`
  and `INF-175`–`INF-177` isolate mechanics not represented by parameter-only
  changes.
- Rejected near terms: `ACT-200` requires an interruptible consumable channel,
  unlike charged instant flasks; `SYS-399` leaves a recoverable death marker,
  unlike Path of Exile 2's local reset; `CON-210` lacks rectangular placement.
- Registry changes: nineteen new stable genes and `COMB-0160`; compatible
  families reuse existing multi-game boundaries.

## Taxonomy impact

- Registry changes: nineteen new stable genes and `COMB-0160`; compatible
  evidence added to eighteen existing action, system, constraint, information,
  objective and time boundaries; memberships in `FAM-009`, `FAM-010`,
  `FAM-013` and `FAM-017`.
- Taxonomy-change record: none; no existing boundary, lifecycle or earlier
  signature changes.
- Candidate terms affected: none.

## Negative results

- No exact full-genome match is expected; the deterministic scan is recorded
  above after regeneration.
- `ACT-200` is not reused because its consumable has an interruptible use
  channel; the scoped Flasks consume charges and begin recovery immediately.
- `SYS-399` is not reused because Path of Exile 2 leaves no recoverable death
  marker; it resets the current campaign area, ground loot and boss.
- `CON-210` is not reused because typed slots and stacks do not express the
  rectangular cell placement admitted here.
