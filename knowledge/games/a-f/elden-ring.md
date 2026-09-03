---
game_id: GAME-0152
slug: elden-ring
game_title: Elden Ring
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0150
gene_ids:
  action:
    - ACT-008
    - ACT-123
    - ACT-130
    - ACT-131
    - ACT-161
    - ACT-200
    - ACT-221
    - ACT-224
    - ACT-227
    - ACT-247
    - ACT-248
    - ACT-249
    - ACT-250
    - ACT-251
  system:
    - SYS-215
    - SYS-222
    - SYS-251
    - SYS-364
    - SYS-399
    - SYS-409
    - SYS-411
    - SYS-412
    - SYS-413
    - SYS-414
  constraint:
    - CON-210
    - CON-269
    - CON-282
    - CON-285
    - CON-286
    - CON-352
    - CON-359
    - CON-360
    - CON-362
    - CON-363
    - CON-364
    - CON-365
  information:
    - INF-119
    - INF-125
    - INF-128
    - INF-159
    - INF-160
    - INF-161
    - INF-162
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Elden Ring

## Analysis scope

- Version / ruleset: base PC game App Ver. `1.16`, Regulation Ver. `1.16.1`,
  offline single-player, new character from creation and Cave of Knowledge
  through first defeat of Margit, the Fell Omen and entry into Stormveil.
- Included: origin class and keepsake as parameters; direct movement, lock-on,
  attacks, guarding, guard counters, dodge, jump, stealth and critical hits;
  HP, FP, stamina, stance and status; Sites of Grace, enemy reset and flask
  refill; death, one current dropped-rune location and recovery; rune purchase
  and attribute levelling; inventory, equipment load, armament requirements,
  upgrades and Ashes of War; crafting; Limgrave map fragment, markers,
  Guidance of Grace and discovered-Grace travel; Torrent traversal and mounted
  combat; one Spirit Ash summon in an eligible zone; Gatefront, Stormhill,
  Margit and the first Stormveil threshold.
- Excluded: online messages, invasions, co-op and NPC cooperator analysis;
  Stormveil beyond its entrance, Godrick, later regions, Great Runes, endings,
  New Game Plus, Shadow of the Erdtree, Nightreign, exhaustive builds, quests,
  bosses, spells, weapons, drops, farming, speedruns, mods and achievements.
- Direct-play status: no new paid-account session was conducted. Official
  current patch, starter and early-game guides were reconciled with public
  Margit route traces into deterministic repository-side transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ER-001` | Regulation 1.16.1 is the current base-game boundary | Confirmed | Direct | High | P1 |
| `ER-002` | Grace restores resources, refills flasks and revives most defeated field enemies | Confirmed | Direct | High | P2 |
| `ER-003` | Death drops carried runes at one recoverable location; another death before recovery replaces the recoverable stock | Confirmed | Direct | High | P2 |
| `ER-004` | Melina's accord unlocks rune levelling and Torrent after early Grace discovery | Confirmed | Corroborated | High | P3 |
| `ER-005` | Equipment requirements, load tier, stamina, FP and flask allocation bound the active build | Observation | Corroborated | High | P2, P3 |
| `ER-006` | Spirit Ash requires the bell, an eligible monument zone and sufficient FP; one spirit type acts autonomously | Confirmed | Direct | High | P2, P3 |
| `ER-007` | Map fragments reveal regional detail while Guidance of Grace suggests, but does not force, the Stormveil route | Confirmed | Direct | High | P2, P3 |
| `ER-008` | Defeating Margit opens the scoped Stormveil entrance | Observation | Corroborated | High | S1, S2 |
| `ER-009` | The repository trace reproduces rest/reset, rune loss/recovery, build gates, Torrent, Spirit Ash and Margit's gate | Observation | Direct | High | V1 |

## Basic data

- Release / origin: FromSoftware / Bandai Namco; released 2022-02-25 and
  reviewed at base PC Regulation Ver. `1.16.1` on 2026-08-21.
- Platform or physical form: third-person open-world action RPG; offline PC.
- Puzzle family: real-time system pressure; inventory and fixture
  dependencies; tactical forecast and counterplay; ordered sequencing.
- Primary sources:
  - **[P1]** [official patch 1.16.1 notes](https://en.bandainamcoent.eu/elden-ring/news/elden-ring-patch-notes-version-1161),
    for the current regulation boundary.
  - **[P2]** [official starter guide](https://en.bandainamcoent.eu/elden-ring/news/elden-ring-starter-guide-tips-know-playing-the-game),
    for HUD resources, combat, Grace, runes, death recovery, map, Torrent and
    Spirit Ash rules.
  - **[P3]** [official early-game tips](https://en.bandainamcoent.eu/elden-ring/news/elden-ring-early-game-tips),
    for Cave of Knowledge, map fragments, Melina, levelling, smithing and the
    Spirit Calling Bell.
- Secondary sources:
  - **[S1]** [IGN Margit gameplay trace](https://www.youtube.com/watch?v=Jm3mcjeC3ho),
    for the first Margit victory boundary.
  - **[S2]** [Limgrave walkthrough](https://www.powerpyx.com/elden-ring-limgrave-walkthrough/),
    for Gatefront-to-Margit ordering and entry into Stormveil.
- Reproducible control: **[V1]** repository-side trace from `P1`–`P3` and
  `S1`–`S2`; rules reasoning, not a claim of direct play.
- Claim IDs: `ER-001`–`ER-009`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate the Tarnished; `ACT-123`, craft a known
  inventory recipe; `ACT-130`, buy from a merchant; `ACT-131`, use an immediate
  item; `ACT-161`, aim and attack; `ACT-200`, commit a restorative flask use;
  `ACT-221`, upgrade an armament; `ACT-224`, rest at Grace; `ACT-227`, place a
  map marker.
- New genes: `ACT-247`, call and directly steer Torrent; `ACT-248`, spend runes
  on one attribute level; `ACT-249`, touch the active death mark to reclaim its
  runes; `ACT-250`, summon one equipped Spirit Ash; `ACT-251`, assign a legal
  Ash of War and affinity to an armament.
- Parameters: origin, action, target, timing, item, recipe, rune price,
  attribute, mount, spirit, armament, skill, affinity and upgrade tier.
- Claim IDs: `ER-002`–`ER-008`.

### System Behaviour Genes

- Existing genes: `SYS-215`, resolve live hostile combat; `SYS-222`, collect
  eligible world loot; `SYS-251`, advance the authored opening; `SYS-364`,
  refill player resources and respawn field enemies on rest; `SYS-399`, convert
  death into checkpoint return and one recoverable currency mark.
- New genes: `SYS-409`, accumulate guard or stance damage and expose a critical
  opening; `SYS-411`, convert runes into a chosen attribute level at its next
  price; `SYS-412`, derive attack, defence, stamina recovery and dodge tier from
  equipped statistics; `SYS-413`, integrate Torrent traversal, mounted attacks
  and recoverable mount defeat; `SYS-414`, execute and dismiss one autonomous
  Spirit Ash group.
- Parameters: damage, stance, rune stock, return point, level cost, equipment
  load, scaling, mount state, spirit AI, FP and arena boundary.
- Claim IDs: `ER-002`–`ER-008`.

### Constraint Genes

- Existing genes: `CON-210`, stacks and slots bound inventory transfer;
  `CON-269`, skills require resource, readiness and a legal target; `CON-282`,
  story encounters obey authored gates; `CON-285`, weapon use needs compatible
  live equipment; `CON-286`, restorative use needs a legal uninterrupted state;
  `CON-352`, only one unrecovered death-currency mark may persist.
- New genes: `CON-359`, armament requirements and equipment-load tier gate
  effective attacks and dodge form; `CON-360`, Spirit Ash requires bell, FP,
  eligible monument range, no multiplayer and no concurrent spirit; `CON-362`, an attribute
  level requires Melina's accord and its escalating rune price; `CON-363`, an
  Ash of War requires compatible armament and unlocked affinity; `CON-364`, map
  opening or fast travel is blocked by live combat and destination rules;
  `CON-365`, finite flask charges are allocated between HP and FP recovery.
- Parameters: requirement, load ratio, summon zone, death mark, level price,
  armament class, map state, Grace state and flask allocation.
- Claim IDs: `ER-002`–`ER-008`.

### Information Genes

- Existing genes: `INF-119`, HUD exposes avatar resources and condition;
  `INF-125`, explored map and authored gates are visible; `INF-128`, inventory
  exposes ground loot and compatibility.
- New genes: `INF-159`, combat HUD exposes HP, FP, stamina, status, equipped
  actions and carried runes; `INF-160`, the map exposes fragments, Grace,
  guidance, markers and the current rune mark; `INF-161`, equipment panels
  expose requirements, scaling, load tier, damage and defence; `INF-162`, Grace
  menus expose level prices, flask allocation and rest consequences.
- Parameters: gauge, status, rune count, region, marker, requirement, scaling,
  load, level price and flask split.
- Claim IDs: `ER-002`–`ER-008`.

### Objective Genes

- Existing gene: `OBJ-080`, defeat the mandatory route guardian and cross the
  newly opened authored progression threshold; here the guardian is Margit.
- Claim ID: `ER-008`.

### Time Genes

- Existing gene: `TIM-003`, exploration and combat unfold continuously except
  in explicit menus, rest transitions and loading boundaries.
- Claim IDs: `ER-002`–`ER-008`.

## Reproducible transitions

1. Create a fresh offline character, complete Cave of Knowledge and reach
   Limgrave with starting equipment and flasks.
2. Activate and rest at Grace; verify recovery, flask refill and enemy reset.
3. Defeat a field enemy, collect runes and a reachable item, then spend or
   retain the currency.
4. Die with runes, return from Grace or a legal Stake, touch the mark and
   recover them; alternatively die again first and verify replacement loss.
5. Reach Gatefront Grace, accept Melina's accord, call Torrent and purchase one
   legal attribute level.
6. Obtain the Limgrave West fragment, place a marker and compare it with
   Guidance of Grace without treating either as forced routing.
7. Configure legal equipment and one Ash of War; verify requirement/load,
   stamina, FP and flask gates during live combat.
8. In an eligible monument zone, summon one Spirit Ash and observe autonomous
   assistance and boundary dismissal.
9. Rest, travel through Stormhill, enter Margit's arena, create a stance break
   or ordinary opening and defeat him.
10. Activate the post-boss Grace and cross into Stormveil; the scoped objective
    completes before the castle is analysed.

## Strategic and experiential structure

The opening turns exploration into preparation. Guidance suggests Margit, but
the player may divert for fragments, runes, levels, smithing materials, spirits
or flask improvements. Rest safely restores the build while also reviving most
field opposition. Carrying unspent runes creates a reversible risk only until a
second death. Combat joins spacing and timing to stamina, stance, FP, armament
requirements and equipment load, so route and build decisions alter the same
live encounter rather than replacing it.

## Replay and variation

Origin, keepsake, armament, spell access, attribute allocation, route, optional
encounters, summon and Margit strategy vary. The invariant is the bounded rule
chain from fresh character through Grace-enabled preparation to Margit victory
and first Stormveil entry.

## Adjacent systems and history

Elden Ring extends earlier checkpoint action RPG structures into a freely
branching open field whose currency is simultaneously progression capital and
recoverable death stake. This unit records only the observable base-game
opening and makes no claim about the full Souls lineage or later campaign.

## Normalised genome

The genome contains 45 genes: 23 reused and 22 new. It separates direct inputs,
live combat, checkpoint reset, rune-risk progression, build legality,
navigation information and the bounded Margit gate.

## Edge cases

- Skipping the Cave of Knowledge changes instruction exposure, not mechanics.
- Guidance of Grace is advisory; detours and the Liurnia bypass are legal but
  do not satisfy the scoped Margit objective.
- A second death before recovery destroys the previous rune stock even when
  the new mark contains zero runes.
- Touching Grace without resting does not trigger the full reset bundle.
- Torrent and Spirit Ash are distinct: one is directly controlled traversal,
  the other autonomous help with arena and multiplayer restrictions.
- NPC or online summons are excluded and do not instantiate `ACT-250`.
- Margit may be defeated without stance break, crafting or a spirit; Torrent is
  available on the approach but unavailable inside Margit's arena.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `151` (`GAME-0001`–`GAME-0151`).
- Exact genome matches: none.
- Tied near matches: `GAME-0150` — Hollow Knight: Silksong (`13 / 54 = 0.240741`).
- Supported combination subsets: `COMB-0150`.
- Scan date: 2026-08-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Hollow Knight: Silksong (`GAME-0150`) | `ACT-008`, `ACT-130`, `ACT-161`, `ACT-224`, `SYS-215`, `SYS-364`, `SYS-399`, `CON-269`, `CON-352`, `INF-119`, `INF-125`, `TIM-003` | Silksong attaches a Cocoon-linked Silk penalty to Bench recovery and gates authored ascent through movement capabilities; Elden Ring selects Grace or Stake, carries rune-priced attribute preparation and feeds Torrent, Spirit Ash and equipment choices into Margit's gate | Near, `0.240741` |

## Combination assessment

`COMB-0150` is a strict subset retaining the Grace–rune-risk–build–Margit loop
while omitting generic navigation, purchase, crafting, pickup and broad HUD.

## Taxonomy impact

The unit adds bounded records for Grace levelling, Torrent, Spirit Ash, stance
openings, equipment-load legality and the first Stormveil gate. It reuses the
parameterised death-currency mark and single-unrecovered-mark genes shared with
Silksong rather than splitting them by object name.

## Negative results

The existing death-currency mark genes are reused with Grace-or-Stake and rune
parameters; Silksong's Cocoon-linked temporary Silk cap remains a game-specific
parameter. No existing companion gene combines monument eligibility, FP,
single-summon and arena dismissal. Monster Hunter's target-routed Seikret is not
direct Torrent control. Generic character levels do not encode selectable
rune-priced stats.
