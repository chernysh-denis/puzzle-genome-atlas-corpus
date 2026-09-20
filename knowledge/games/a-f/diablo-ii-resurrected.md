---
game_id: GAME-0322
slug: diablo-ii-resurrected
game_title: "Diablo II: Resurrected"
analysis_status: reviewed
reviewed: 2026-09-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-191
    - ACT-199
  system:
    - SYS-215
    - SYS-222
    - SYS-299
    - SYS-449
    - SYS-450
    - SYS-925
    - SYS-926
  constraint:
    - CON-270
    - CON-394
    - CON-395
  information:
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-175
    - INF-354
  objective:
    - OBJ-189
  time:
    - TIM-003
---

# Game: Diablo II: Resurrected

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Class, item, enemy,
layout, difficulty and reward labels are parameters, not gene names.

## Analysis scope

- Version / ruleset: English Windows Battle.net launch base game released on
  2021-09-23, including the Lord of Destruction rules shipped with Resurrected;
  a fresh local offline Expansion Softcore Normal Barbarian. The packet uses
  the documented launch/base-game boundary rather than the current 2026
  Infernal Edition or `Reign of the Warlock` expansion.
- Structured analysis target: licensed digital Windows base game, offline
  character, fresh Normal session and Act I `Den of Evil`; see `GAME-0322` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: accept Akara's first quest, search the sampled Blood
  Moor for the sampled Den entrance, explore its local layout, directly fight
  every living or reanimated hostile, inspect and optionally fit compatible
  generated drops, then return to Akara, receive the fixed quest reward and
  commit one newly available skill point to an eligible Barbarian skill.
- Entry: first ordinary control of the fresh Barbarian in Rogue Encampment,
  before accepting `Den of Evil` from Akara.
- Positive terminal: every required hostile in the instantiated Den has been
  defeated, the cave light and quest state report clearance, the Barbarian
  returns to Akara, receives the automatic skill point and retained one-use
  Normal-difficulty stat/skill reset permission, then spends one available
  point on an eligible level-one Barbarian skill and regains ordinary control.
- Negative terminal: leaving the session or stopping before Akara's hand-in or
  before the declared skill allocation does not satisfy the packet. Character
  death and corpse recovery are valid wider-game rules but are not executed or
  required here; the packet does not manufacture a death merely to admit them.
- Included: direct isometric movement and basic attack; continuous hostile
  combat; local sight and sound; sampled Blood Moor/Den layout and encounter
  placement; Fallen Shaman reanimation of eligible Fallen; experience and
  level progression; generated item bases, rarity and modifiers; reachable
  compatible pickup/equipment transfer; rectangular inventory and equipment
  requirements; character, quest, inventory and item information; the final
  five-or-fewer hostile count; full clearance, Akara reward, one retained free
  reset permission and one legal skill-point allocation.
- Excluded: use of the newly allocated skill after the terminal; attribute
  allocation, vendors, repair, identification, stash organisation, Town Portal,
  waypoint activation, Cold Plains, Blood Raven and all later quests; forced
  item farming or a promised named drop; deliberate death, gold loss, corpse
  recovery or save/exit corpse relocation; Nightmare, Hell, Hardcore, online,
  Ladder, parties, PvP, trading and cross-progression; later balance seasons,
  Terror Zones, current Infernal Edition, Warlock content, cosmetics and the
  complete campaign.
- Reproducible parameterisation: create a fresh offline Expansion Softcore
  Normal Barbarian, accept Akara's quest, leave through Blood Moor, locate the
  sampled Den and traverse every branch until all required monsters—including
  any Fallen restored by a living Shaman—are defeated. Inspect generated drops
  and transfer at least one compatible reachable item if the sampled instance
  supplies one; this is a bounded parameter, not a completion prerequisite.
  Observe the remaining-hostile number once five or fewer remain, return on
  foot to Akara after the cave changes state, record the skill-point total
  before and after hand-in, then spend one available point on an eligible
  level-one Barbarian skill. Layout, encounter positions, experience timing,
  damage, reanimations and item outcomes may vary; the all-hostiles predicate,
  hand-in reward and point legality do not.
- Potential scoped modules: a performed corpse-recovery comparison; waypoint
  activation and saved-character reload; Town Portal economy; identification,
  vendors and stash; one named class build; online party quest credit; each
  later act, difficulty, season and expansion require their own boundaries.
- Direct-play status: not conducted. No Battle.net client, licensed installed
  build, local character, save, input trace, screenshot, video or audio was
  found or opened. Blizzard establishes product, offline and preserved-rule
  identity; its Arreat Summit establishes character, item, death, waypoint and
  skill rules; two current written Resurrected routes corroborate the bounded
  quest. This is a source-bounded reconstruction, not a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `D2R-001` | Blizzard released Diablo II: Resurrected digitally for Windows through Battle.net on 2021-09-23 as a remaster of Diablo II and Lord of Destruction | Confirmed | Direct | High | P1, P2 |
| `D2R-002` | A local offline character has separate save state and may play single-player without joining an online character pool | Confirmed | Direct | High | P1 |
| `D2R-003` | Character experience thresholds grant levels and skill points, while allocation is restricted by skill level requirements and prerequisites | Confirmed | Direct | High | P3, P4 |
| `D2R-004` | Item sources sample bases and quality; carried space is finite and equipment or class requirements remain visible before use | Confirmed | Direct | High | P3, P5 |
| `D2R-005` | `Den of Evil` begins with Akara, lies in Blood Moor and requires every monster in the cave to be defeated | Observation | Corroborated | High | S1, S2 |
| `D2R-006` | Fallen Shaman can restore Fallen, so restored monsters re-enter the required live hostile set | Observation | Corroborated | High | S1, S2 |
| `D2R-007` | At five or fewer remaining monsters the quest reports their count, and complete clearance changes the cave light and quest state | Observation | Corroborated | High | S1 |
| `D2R-008` | Returning to Akara after clearance automatically grants one skill point and unlocks one free stat/skill reset for that difficulty | Observation | Corroborated | High | S1, S2 |
| `D2R-009` | Waypoint activation and corpse recovery are persistent base rules but neither is causally required or executed in this bounded first-quest route | Confirmed | Direct | High | P3 |
| `D2R-010` | No installed build, direct run, generated-layout sample, death, waypoint, save or reload comparison was performed | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Blizzard Entertainment; digital Windows launch on
  2021-09-23; remastered Diablo II plus Lord of Destruction content.
- Platform or physical form: English licensed Windows Battle.net digital base
  game, fresh offline Expansion Softcore Normal Barbarian.
- Puzzle family: real-time system pressure; inventory and fixture
  dependencies; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-20:
  - **[P1]** [official Resurrected launch guide](https://news.blizzard.com/en-us/article/23725471/diablo-ii-resurrectedtm-launch-guide),
    for launch date, Windows Battle.net installation, offline/online character
    separation, classes and preserved local single-player rules.
  - **[P2]** [official launch announcement](https://news.blizzard.com/en-us/article/23679610/diablo-ii-resurrectedtm-the-gates-of-hell-open-september-23),
    for the digital base product, Diablo II/Lord of Destruction remaster scope
    and quality-of-life boundary.
  - **[P3]** [Blizzard Arreat Summit character rules](https://classic.battle.net/diablo2exp/basics/characters.shtml),
    for levels, skill allocation, death, corpse, save, quest and waypoint
    persistence rules inherited by the preserved base system.
  - **[P4]** [Blizzard Arreat Summit skill FAQ](https://classic.battle.net/diablo2exp/faq/skills.shtml),
    for rank, character-level and prerequisite gates on skill-point spending.
  - **[P5]** [Blizzard Arreat Summit item basics](https://classic.battle.net/diablo2exp/items/basics.shtml),
    for finite item management, stack/slot rules, rarity, requirements and
    monster/area-conditioned drops.
- Corroborating textual sources, accessed 2026-09-20:
  - **[S1]** [Gamer Guides `Den of Evil` record](https://www.gamerguides.com/diablo-ii-resurrected/guide/quests/quest-information/den-of-evil),
    for Akara, Blood Moor, complete cave clearance, Shaman reanimation, final
    count, cave-light change, skill point and reset option.
  - **[S2]** [Wowhead Act I walkthrough](https://www.wowhead.com/diablo-2/guide/act-1-walkthrough-quests),
    for an independent Resurrected route from Akara through full Den clearance
    and the returned reward.
- Research record: **[R1]** local 2026-09-20 preflight found no Battle.net
  client, installed Diablo II: Resurrected build, character or save; no direct
  play or audiovisual evidence was used.
- Claim IDs: `D2R-001`–`D2R-010`.

## Mechanical decomposition

### Action Genes

- `ACT-008` owns direct Barbarian movement through camp, Blood Moor and the
  Den; `ACT-161` the aimed basic attacks against a selected nearby hostile;
  `ACT-199` one compatible reachable drop moved into inventory or equipment;
  and `ACT-191` the declared post-reward skill-point commitment.
- No death, corpse, waypoint, portal, identification or reset action enters the
  packet. The reset is retained permission, not an executed respec.
- Claims: `D2R-003`–`D2R-010`.

### System Behaviour Genes

- `SYS-215` advances direct real-time hostile combat; `SYS-222` resolves an
  eligible ground pickup; `SYS-299` turns experience thresholds into levels
  and points; `SYS-449` instantiates Blood Moor and Den local contents; and
  `SYS-450` samples item bases, rarity and modifiers from eligible sources.
- New `SYS-925` returns an eligible slain Fallen to live hostile state when a
  living Fallen Shaman completes its reanimation. New `SYS-926` settles the
  cleared first quest at Akara into one automatic skill point plus a retained
  one-use Normal-difficulty reset permission.
- Resolution order: accept quest; instantiate and reveal local geography;
  movement and combat update health, experience and drops; a living Shaman may
  restore an eligible Fallen; every current required hostile must settle;
  clearance changes the cave and quest; Akara grants the two-part reward;
  legal point allocation changes the persistent build. Claims:
  `D2R-003`–`D2R-010`.

### Constraint Genes

- `CON-270` restricts the skill point to current level/prerequisite-legal
  ranks; `CON-394` requires a compatible free rectangular inventory placement
  or equipment slot; and `CON-395` requires the Barbarian to satisfy an item's
  class, attribute, hand and level conditions before its effect applies.
- All-hostile clearance is owned by the objective rather than `CON-402`: the
  Den entrance is not claimed to lock behind combat, while quest settlement
  alone waits for the complete required set. Claims: `D2R-003`–`D2R-008`.

### Information Genes

- `INF-115` exposes only local visible/audible threats; `INF-119` current Life,
  experience, level and skill state; `INF-125` quest and explored-route state;
  `INF-128` ground identity and inventory compatibility; and `INF-175` item
  quality, modifiers and unmet requirements.
- New `INF-354` exposes an exact remaining-hostile number only after the Den
  reaches five or fewer; it does not reveal their hidden positions or future
  reanimations. Claims: `D2R-003`–`D2R-008`.

### Objective Genes

- New `OBJ-189` owns the complete terminal: accept the first quest, find and
  clear the sampled Den including restored monsters, return to Akara, retain
  the skill/reset reward and commit one legal skill point. A lit cave without
  hand-in, a hand-in without the declared allocation or a waypoint detour is
  insufficient. Claims: `D2R-005`–`D2R-010`.

### Time Genes

- `TIM-003` owns simultaneous player movement, hostile attacks, Shaman
  reanimation, health loss and combat timing. Menus pause or constrain input
  according to their ordinary state but do not turn the route into rounds.
- Claims: `D2R-005`–`D2R-008`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh offline Barbarian has ordinary camp control | Speak with Akara and accept the first quest | `Den of Evil` becomes the current quest and identifies Blood Moor | quest acceptance precedes route settlement | `D2R-005` |
| Blood Moor has been instantiated but not fully explored | Traverse from the camp and search local branches | a sampled route eventually exposes the Den entrance without revealing its complete layout in advance | area identity is stable while local geometry varies | `D2R-005` |
| A living hostile is in legal basic-attack reach | Commit the basic attack | range, cadence, hit and damage resolve while every actor continues | combat is directly commanded and real-time | `D2R-005` |
| A Fallen corpse is eligible and a Fallen Shaman remains active | Allow the Shaman's reanimation to complete | that Fallen returns to living hostile state and must be defeated again | the required set can reopen before clearance | `D2R-006` |
| An eligible enemy or container resolves a drop | Inspect the resulting ground item | base, quality and modifiers are sampled within source/area rules | exact loot is bounded uncertainty | `D2R-004` |
| A compatible generated item is reachable and space is available | Transfer or equip it | the item occupies legal cells/slot and changes carried or equipped state | loot adaptation is available but not terminal | `D2R-004` |
| Experience crosses a character threshold | Accept the automatic level update | character level and available build points increase under the threshold table | combat can advance the persistent build | `D2R-003` |
| Five or fewer required hostiles remain | Continue clearing the cave | the quest surface reports the exact remaining count but not their locations | the final search has bounded count information | `D2R-007` |
| The last currently required hostile is defeated | Allow quest state to settle | the Den brightens and the quest directs return to Akara | full clearance is objectively detectable | `D2R-005`, `D2R-007` |
| The Den is clear and the Barbarian has returned to camp | Speak with Akara | one skill point is added and one Normal reset permission becomes available | fixed reward is separate from random loot | `D2R-008` |
| At least one point and eligible level-one Barbarian skill are available | Spend one point | that selected rank becomes part of the persistent character build | positive terminal includes a committed skill choice | `D2R-003`, `D2R-008` |
| The Barbarian remains alive throughout the bounded route | Do not trigger a deliberate death | no corpse-recovery transition occurs and no waypoint is needed | selection hypotheses are rejected when non-causal | `D2R-009`, `D2R-010` |

## Strategic and experiential structure

- Local decision: choose a safe reachable hostile, distinguish Shaman from its
  resurrectable Fallen, preserve Life and decide whether a generated item is
  worth limited cells or an equipment replacement.
- Medium horizon: explore every sampled cave branch, prevent reanimation from
  reopening progress, and use the final count to find omissions.
- Long horizon: experience, equipment and a permanently allocated skill point
  persist beyond the quest, while the one-use reset permission preserves a
  future correction without being consumed here.
- Feedback: visible combat, drop labels/tooltips, character and inventory
  panels, quest log, the final count, cave lighting and Akara dialogue separate
  attack, loot, clearance, reward and build errors.
- Failure recovery: ordinary Softcore corpse recovery is documented but
  deliberately outside the successful packet. This unit therefore makes no
  claim about a performed death, corpse retrieval or post-reload state.
- Skill expression: efficient local path coverage, Shaman prioritisation,
  attack spacing, inventory triage and a legal early skill commitment.
- Ambiguity: exact layout, hostile placement, reanimation timing, experience
  threshold timing and item outcomes vary; the quest's complete-set predicate
  and fixed reward are invariant.

## Edge-case audit

- A revived Fallen is live again and prevents full settlement until defeated;
  a previously counted corpse is not permanently removed while a compatible
  Shaman can restore it.
- The final counter reveals quantity, not coordinates. Searching the wrong
  cave branch remains a navigation error rather than hidden completion.
- An item that does not fit or whose requirements are unmet cannot contribute
  merely because it dropped. It may stay on the ground or in carried cells.
- No specific drop is required. A seed with no useful replacement can still
  complete the quest; the reward skill point is deterministic.
- The free reset option becomes available after the hand-in but remains unused.
  Treating its existence as an executed reallocation would conflate permission
  with player action.
- Activating a later waypoint or using Town Portal may shorten a wider route,
  but neither is necessary for this entry-to-terminal path and neither enters
  its genome.
- Normal Softcore death would create a corpse/equipment recovery problem, but
  the positive route neither requires nor observes it. The rule is a potential
  module, not evidence for a performed transition.
- Current 2026 product marketing includes an expansion and Warlock content;
  the scoped 2021 base game and Barbarian prevent those additions from leaking
  into the record.

## Replay and variation

- The same named Blood Moor and Den roles recur, but their traversable local
  geometry, encounter positions and item outcomes are sampled for the session.
- Character movement, target order, Shaman interruption, damage and experience
  timing vary by execution. The packet does not prescribe a named item drop or
  one exact geometric route.
- Quest settlement is invariant: every current required monster must be gone,
  Akara grants the fixed point/reset result and the declared terminal spends
  one legal point.
- A replay with another class, online party credit, a different difficulty,
  death/corpse recovery or a waypoint detour is a separate parameter/module,
  not silent evidence for this fresh offline Barbarian route.

## Adjacent systems and history

- Resurrected preserves Diablo II and Lord of Destruction gameplay while
  changing audiovisual presentation and adding launch quality-of-life features
  such as the enlarged stash and automatic gold pickup. This packet identifies
  the remaster as its own Windows product but relies only on rules explicitly
  preserved or corroborated for its bounded quest.
- Blizzard's classic Arreat Summit documents waypoints, corpse recovery,
  character saves and item management. They establish nearby system boundaries
  but do not prove execution inside this successful first-quest route.
- Current 2026 marketing includes Infernal Edition and `Reign of the Warlock`.
  Those later commercial/content layers are excluded instead of being treated
  as launch-base parity.
- Path of Exile 2 supplies reusable generated-area, generated-item, rectangular
  inventory and equipment-requirement boundaries. Diablo's Shaman reanimation,
  late exact count and two-part Akara reward remain distinct additions.

## Normalised genome

| Type | Genes | Boundary note |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-191`, `ACT-199` | move, fight, equip and commit one development point |
| System | `SYS-215`, `SYS-222`, `SYS-299`, `SYS-449`, `SYS-450`, `SYS-925`, `SYS-926` | live combat, pickup, progression, sampled area/item state, hostile return and fixed quest settlement |
| Constraint | `CON-270`, `CON-394`, `CON-395` | legal skill rank, rectangular capacity and compatible character/equipment state |
| Information | `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-175`, `INF-354` | local threats, build/quest/item state and the late exact hostile count |
| Objective | `OBJ-189` | clear the sampled Den, claim Akara's result and commit the skill reward |
| Time | `TIM-003` | combat and reanimation continue in real time |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `321` (`GAME-0001`–`GAME-0321`).
- Exact genome matches: none.
- Tied near matches: `GAME-0162` — Path of Exile 2 (`17 / 42 = 0.404762`).
- Supported combination subsets: none.
- Scan date: 2026-09-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0162` — Path of Exile 2 | direct movement and attacks, real-time combat, experience/point progression, sampled campaign areas and items, rectangular inventory, equipment/build gates, local perception plus character, quest and item information | Diablo's bounded first quest has no gem/support/currency/flask/dodge/checkpoint stack; it instead requires a re-openable full-clear set, exposes the last count and returns to Akara for point/reset settlement before one skill commitment | Near, `0.404762` |

## Taxonomy impact

- Four Active boundaries are added: hostile-caster reanimation, Akara's
  coupled point/reset settlement, the thresholded exact remaining count and the
  complete clear/hand-in/allocation objective.
- Eighteen existing boundaries are reused without wording, lifecycle or earlier
  signature changes. Parameters retain the named class, quest, enemy, item,
  area and difficulty details.
- No combination or family definition changes. The game joins three existing
  families after direct causal-boundary review.

## Negative results

- `CON-402` is rejected: Den quest completion waits for all required monsters,
  but this packet does not claim that the dungeon exit physically locks during
  combat.
- `OBJ-166` is rejected: it settles a hostile-set mission into a selectable next
  mission, whereas this packet returns to a giver, retains a two-part build
  reward and commits a skill point.
- No corpse-recovery, waypoint, Town Portal, identification or executed respec
  gene is admitted. Each is a real adjacent rule whose transition was neither
  causally necessary nor observed here.
- No named generated item, exact layout or exact hostile position is treated as
  canonical. They remain bounded sample outcomes.
- No current Infernal Edition/Warlock, online, Ladder, later-difficulty or
  complete-campaign feature is inferred from the launch base game.

## Delta summary

## New facts

- [Confirmed | Direct | High] The scoped Windows launch base game preserves a
  separate local offline character, persistent skill/item state and the
  original level, inventory and item rule families (`D2R-001`–`D2R-004`).
- [Observation | Corroborated | High] The first quest requires every current
  Den monster, including reanimated Fallen, and exposes its last five before a
  fixed skill-point/reset reward (`D2R-005`–`D2R-008`).
- [Confirmed | Direct | High] Corpse recovery and waypoint persistence are real
  wider rules but do not enter this successful first-quest packet (`D2R-009`).

## New genes

- [Observation | Corroborated | High] `SYS-925`, `SYS-926`, `INF-354` and
  `OBJ-189` isolate hostile reanimation, two-part first-quest settlement, the
  late remaining-hostile counter and the complete clear/hand-in/allocation
  terminal.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Confirmed | Direct | High] No earlier taxonomy boundary or signature changed.

## New questions

- How does a performed Normal Softcore death alter equipment, gold, instantiated
  Den state and return routing before the quest is complete?
- Which exact offline save fields survive quit/relaunch after Den clearance but
  before Akara's hand-in and after the reset permission is granted?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0323` Marvel's Spider-Man 2.
- Optimisation criterion: move from a source-bounded isometric full-clear quest
  into a current console-authored superhero traversal/combat packet.
- Expected information gain: test traversal vocabulary, encounter gating,
  dual-protagonist boundaries and exact PS5 edition evidence.
- Backlog impact: `GAME-0323` remains next; no later unit starts in this commit.

## Why this game

- [Hypothesis | Limited | High] Diablo II: Resurrected is a recognisable PC
  anchor whose smallest complete quest separates random local contents from an
  invariant full-clear predicate and deterministic retained build reward.

## Research checklist

- [x] Windows launch base game, offline mode, class, difficulty, entry and terminal declared
- [x] official product, character, skill and item rules separated from two quest routes
- [x] current expansion, online, later quests, corpse and waypoint modules excluded
- [x] direct-play, installed-build, generated-layout, save and reload limits disclosed
- [x] complete six-type gene scan performed
- [x] deterministic lower-ID comparison and combination scan prepared
- [ ] reviewed Ukrainian localisation and bilingual presentation completed
- [ ] original artwork and responsive browser checks completed
