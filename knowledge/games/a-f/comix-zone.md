---
game_id: GAME-0490
slug: comix-zone
game_title: Comix Zone
analysis_status: reviewed
reviewed: 2026-10-04
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-009
    - ACT-089
    - ACT-131
    - ACT-161
    - ACT-202
    - ACT-270
    - ACT-295
    - ACT-296
    - ACT-297
    - ACT-341
    - ACT-662
  system:
    - SYS-020
    - SYS-036
    - SYS-045
    - SYS-112
    - SYS-215
    - SYS-470
    - SYS-578
    - SYS-755
    - SYS-1308
    - SYS-1309
    - SYS-1310
    - SYS-1311
  constraint:
    - CON-175
    - CON-176
    - CON-210
    - CON-402
    - CON-442
    - CON-685
  information:
    - INF-119
    - INF-128
    - INF-192
    - INF-467
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Comix Zone — original Genesis first comic page

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Actor names, panel layout, attack buttons, damage, three slots and serial-hit
threshold are parameters, not separate genes or a product-wide item inventory.

## Analysis scope

- Version / ruleset: original English Mega Drive / Genesis Comix Zone,
  original 1995 cartridge booklet rules preserved by SEGA. Exact executable
  revision and regional binary parity are uninspected. The scanned booklet's
  2019 PDF conversion does not establish a new ruleset. No modern collection,
  GBA, Windows or mobile port supplies original-engine parity.
- Structured analysis target: existing `PLAT-SEGA-GENESIS` in
  `knowledge/platforms/games.json`; default six-button controls with BLOCK on C.
- Primary decision loop: inspect the current panel, health, three held slots
  and available exit arrows; move, change posture, strike, block, seize/throw,
  push an obstacle, operate a fixture, spend a held tool or deploy/retrieve
  Roadkill; let live movement, hostile contact, health costs, destruction and
  mechanism responses resolve; select an available successor panel and repeat
  until the whole first page's exit or the attempt's terminal defeat.
- Entry and exit: one fresh ordinary first-episode Page 1 attempt, beginning
  at first Sketch control in Alissa's command-centre panel, with one health
  pool, no earned continue or imported item. Knife, Ice Tea and bomb lie on the
  floor; taking them is optional and within scope. Stop when the final broken
  bridge is crossed and the page completes, before acting in Page 2. Zero
  health or the final lethal unsupported gap ends this single attempt.
  Both the right and down branch are included alternatives, not two branches
  traversed in one attempt; they merge into the shared crate/lever route.
- Included: all materially available traversal, jumping, crouching, rolling,
  hanging movement/attacks, ordinary high/low/body attacks, six-button held
  block, close humanoid grab/scissor attack/throw, serial accepted-hit finish
  and rapid attack alternation; health-paid solid-object hits and declared
  special actions; addressed pickup and three common slots; immediate tea,
  knife throw, placed fuse bomb, obtainable Super Fist, carried/deployed
  Roadkill and the secret held-input paper airplane; authored enemies,
  destructible barrels, manholes, cage, grate and fragile panel borders;
  flaming drums, explosive crate, high lever and opened floor; local health,
  slot and exit/advice disclosure, continuing attrition and page completion.
  X/Y/Z immediately use their item slot, not an extra active-weapon selector.
  The first-page rat can reveal a knife; its shared-slot cost, autonomous
  contacts, finite-hit loss and condition-restoring physical pickup remain.
  Ordinary humanoids are subject to the documented serial/combination rules;
  the flying creatures are not assumed to share that finisher counter.
- Excluded: Page 2, first-episode boss and earned continues; later episodes,
  endings, timed final rescue, later enemies, grenades or random Mystery
  pickups not established on this page; configuration changes, alternative
  auto-block/custom-move setup, cheats, level selection, save states and
  wrapper conveniences. No exact damage, bomb delay, roll protection,
  interruption interval, durability, native finisher-counter reset or tea
  fraction is asserted. Written accounts disagree about tea restoration.
- Potential scoped modules: complete first-episode boss route and continue
  settlement; later clock/switch puzzles; final rescue with alternative
  endings. None is silently flattened into this first-page signature.
- Direct-play status: not conducted. No cartridge, ROM, emulator, native
  save, game video/audio or controller trace was inspected. The original
  SEGA manual's printed pp. 10–27 were read; scanned control, movement,
  health, item and character pages were visually inspected. Written routes
  establish both first-page branches and their shared route; the recorded
  player's text corroborates paper-airplane health cost and refusal while
  health flashes red. These are their observations, not our play. Conflicting
  tea restoration fractions do not establish an exact native healing value.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CZ-001` | Direct movement, down pickup, pushing, jumps/hanging and six-button BLOCK differ from slot use | Confirmed | Direct | High | P1 pp. 10–15 |
| `CZ-002` | Three accepted humanoid serial hits lead to a special finisher; rapid move alternation defeats guard | Confirmed | Direct | High | P1 pp. 14–17 |
| `CZ-003` | Solid-object hits and special moves debit Sketch's own health, not only hostile damage | Confirmed | Direct | High | P1 pp. 18–19 |
| `CZ-004` | Fresh Page 1 supplies knife, tea and bomb; two fork alternatives merge before a shared exit | Observation | Corroborated | Medium | R1 Page 1, R2 Page 1 |
| `CZ-005` | Slot-limited tea, knife, placed bomb and obtainable fist resolve distinct effects; blast may hit Sketch | Observation | Corroborated | Medium | P1 pp. 12–13, 20–21; R1–R2 |
| `CZ-006` | Roadkill occupies a common item slot and is physically released/picked up, with autonomous electrical and hidden-find help | Observation | Corroborated | Medium | P1 pp. 18–21; R1–R2 |
| `CZ-007` | Incoming hits can remove Roadkill; pickup restores the rat, not Sketch | Observation | Corroborated | Medium | R2 Basics; S1 |
| `CZ-008` | Moving the explosive crate reaches a high lever; opening the floor and dropping the crate removes burning drums | Observation | Corroborated | Medium | R1–R2 Page 1 |
| `CZ-009` | Held-attack paper airplane costs health, returns across the panel and may hit its maker; red-health use is reported refused | Observation | Corroborated | Medium | R2 Basics; R3 player comments |
| `CZ-010` | Flashing current-panel exits and Alissa's advice disclose local routes, not complete future hidden state | Confirmed | Direct | High | P1 pp. 18–19 |
| `CZ-011` | Health persists between panels; zero or the final gap ends the first-page attempt without an earned continue | Observation | Corroborated | Medium | R1–R2 Page 1; R2 Basics |
| `CZ-012` | Tea restores part of the pool; differing secondary fractions do not establish an exact value | Observation | Conflicting | Medium | P1 p. 20; R1 Items; R2 Basics |
| `CZ-013` | Bombs/breakage may remove enclosed pickups, so clearing a route can sacrifice its contents | Observation | Corroborated | Medium | R1–R2 Page 1; P1 p. 21 |

## Basic data

- Release / origin: SEGA Technical Institute / SEGA, original 1995 cartridge.
  No exact release-day, ownership, ROM hash or installed revision claim.
- Platform or physical form: English original Genesis cartridge controls;
  the analysis target is distinct from an all-release platform audit.
- Puzzle family: spatial physics, tactical counterplay, live pressure,
  typed object/fixture delivery and ordered dependency sequencing. All
  seventeen controlled family definitions were tested.
- Primary sources, accessed 2026-10-04:
  - **P1:** [SEGA's preserved original instruction booklet](https://manuals.sega.com/genesismini/pdf/COMIXZONE.pdf),
    printed pp. 10–27. Original scanned rules establish commands, humanoid
    sequences, health costs, common slots, items, exit arrows and local advice.
  - **R1:** [Ed Osciak III's original Genesis first-hand guide](https://gamefaqs.gamespot.com/genesis/10975-comix-zone/faqs/13691),
    Final, 2001-08-22, Items and Page 1. Written route supplies the two branches
    and shared mechanism, not measured native state or exact health fractions.
  - **R3:** [Todd Foreman's recorded-player comments](https://speeddemosarchive.com/ComixZone.html),
    run dated 2011-12-22; text only. The airplane cost and low-health restriction
    are retained; speculative boss damage-counter exploits are excluded.
- Secondary sources:
  - **R2:** HonestGamers' independently authored
    [Basics](https://www.honestgamers.com/guides/comix-zone/21/read/413.html) and
    [first-page route](https://www.honestgamers.com/guides/comix-zone/21/read/415.html)
    corroborate first-page geometry, optional alternatives, tool effects and
    rat pickup/condition. Its half-health tea conflicts with R1's approximation.
  - **S1:** [Source Gaming's first-hand backlog account](https://sourcegaming.info/2023/11/06/beat-the-backlog-comix-zone/),
    2023-11-06, independently supports health-paid breaking and rat condition.
    The reported three-hit rat allowance remains a parameter, not engine proof.
- Claim IDs: `CZ-001`–`CZ-013`.

## Mechanical decomposition

### Action Genes

- Existing: `ACT-008` movement/jump/roll/hanging travel; `ACT-009` body push;
  `ACT-089` down-pickup; `ACT-131` tea/fist immediate use; `ACT-161` aimed
  knife/tool strike; `ACT-202` posture; `ACT-270` placed bomb;
  `ACT-295` character attacks and held-input airplane; `ACT-296` dedicated
  live guard; `ACT-297` ordinary close grab/throw; `ACT-341` fixture operation.
- New: `ACT-662`, releasing a helper from a common item slot, not remotely
  recalling a separate party member. Physical retrieval remains `ACT-089`.
- Parameters: facing, high/low/air/hanging attack, item slot, target and reach.
  Alternative automatic block is outside the declared control configuration.
- Claim IDs: `CZ-001`–`CZ-006`, `CZ-009`.

### System Behaviour Genes

- Existing: `SYS-020` attack displacement into fragile borders/danger;
  `SYS-036` continuous body fall and support; `SYS-045` hostile movement;
  `SYS-112` persistent lever/tool-triggered floor opening; `SYS-215` live
  damage/guard/defeat, including consumed fist's normal-hostile panel effect;
  `SYS-470` timed bomb blast, including owner; `SYS-578` one health pool and
  partial tea healing; `SYS-755` durability destruction, linked explosion
  consequences and contents. No separate gene is created for every prop.
- New: `SYS-1308` own-action/solid-hit health debit; `SYS-1309` accepted
  humanoid sequence/finisher and alternation against guard; `SYS-1310` item
  helper world contacts, discovery and condition; `SYS-1311` automatic
  outbound/reverse projectile with owner risk. Distinct triggers are retained.
- Resolution: eligible input commits; live motion/contact updates hit, guard,
  health, helper, object durability and declared outputs; fixture state changes
  support/route access; conquered-panel gates reveal outgoing directions;
  arrival at the final successor completes the page unless defeat occurs.
  This qualitative ordering is not a frame-accurate collision precedence.
- Parameters: threshold, damage, health cost, terrain, linked blast targets,
  contents, helper tolerance and airplane reversal. No exact formula claimed.
- Claim IDs: `CZ-002`–`CZ-009`, `CZ-011`–`CZ-013`.

### Constraint Genes

- Existing: `CON-175` attrition across panels; `CON-176` directed outgoing
  route edges with mutually exclusive branches; `CON-210` three typed shared
  slots with one item per slot; `CON-402` finite required panel-hostile
  clearance; `CON-442` pose/recovery/range prerequisites; `CON-685` terminal
  final unsupported fall. No new constraint is needed.
- Scarce resources: one continuing health pool, acquired consumables, three
  slots and the condition of the helper occupying one of them. Breaking a
  prop can spend health or destroy its contents; neither is a free reset.
- Claim IDs: `CZ-001`, `CZ-004`–`CZ-009`, `CZ-011`–`CZ-013`.

### Information Genes

- Existing: `INF-119` own health and red alert; `INF-128` visible ground
  items/common slots; `INF-192` bounded local side-view geometry/threats.
- New: `INF-467` current conquered-panel directions and local authored advice.
  These do not reveal hidden pickups or guarantee an optimal future route.
- Claim IDs: `CZ-001`, `CZ-005`–`CZ-006`, `CZ-010`.

### Objective Genes

- Existing: `OBJ-026`, open the authored route and cross the final broken
  bridge to the page's connected exit. First-panel victory is not completion.
- Failure: zero health or lethal final gap; no earned continue exists at
  this entry. Later continue/retry handling is a separate potential module.
- Claim IDs: `CZ-004`, `CZ-008`, `CZ-011`.

### Time Genes

- Existing: `TIM-003`, live enemies, projectiles, fuses and body motion continue
  while input is possible, except explicit pause. No universal countdown,
  external time limit or exact roll-protection interval is invented.
- Claim IDs: `CZ-001`–`CZ-003`, `CZ-005`–`CZ-009`.

## Reproducible transitions

These are conditional source reconstructions, not native controller traces.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Initial tools lie on floor, a slot is free | Stand over knife and press down | Knife becomes carried | Addressed pickup, not contact score | `CZ-001`, `CZ-004` |
| Three slots are occupied and Roadkill is reachable | Attempt another pickup | Capacity prevents carrying the extra item | Rat competes with tools | `CZ-005`–`CZ-006` |
| Solid obstruction remains; Sketch has health | Hit it with a qualifying body attack | Durability falls and own health is charged | Breaking is not free | `CZ-003` |
| Bomb carried, compatible ground position | Place it, then leave blast reach | Fuse resolves destruction; remaining nearby bodies can be hit | Blast also threatens owner | `CZ-005`, `CZ-013` |
| Humanoid has accepted preceding serial hits | Land the threshold-reaching serial member | Special finishing attack resolves | Hits, not raw button count | `CZ-002` |
| First combat panel's required foes remain | Attempt fork traversal | Outgoing combat gate is not yet cleared | Finite panel clearance | `CZ-004`, `CZ-010` |
| Fork is available after clearance | Choose right or down | Follow that directed branch toward the common route | Not two visits in one attempt | `CZ-004` |
| Roadkill is carried and world position reachable | Activate its occupied slot | Rat becomes autonomous and slot becomes available | Item-helper release | `CZ-006` |
| Rat traverses compatible authored hidden locus | Let it proceed, then pick it up | Hidden knife is revealed; rat condition is restored on pickup | Owner health is not restored | `CZ-006`–`CZ-007` |
| Explosive crate intact, raised lever unreachable | Push crate into stepping position; climb and operate lever | Floor opens while intact crate can still be moved | Ordered fixture dependency | `CZ-008` |
| Floor open, burning drums below | Push crate through opening | Falling marked crate detonates/removes linked drums | Preserve prop until its useful destination | `CZ-008` |
| Health permits held-input airplane | Hold attack, then avoid returning line | Health paid; projectile reverses across panel and may hit Sketch | Owner risk survives creation cost | `CZ-009` |
| Final gap visible, page not complete | Clear final threats and jump across | Page exit reached; falling instead ends attempt | Arrival and support terminal differ | `CZ-011` |

## Strategic and experiential structure

- Local decision: positional attack/guard versus a scarce held tool; whether
  a breakable body should instead be pushed or reached through a helper.
- Medium-term planning: keep sufficient health and slot space through either
  authored branch; preserve the explosive crate for the shared route.
- Long-term structure: none admitted beyond this complete first page.
- Common heuristics: vary humanoid attacks, retreat from one's blast, retrieve
  useful Roadkill and inspect the final gap before committing movement.
- Failure attribution: distinguish hostile damage, self-paid breaking,
  destroyed contents, lost helper and unsupported terminal fall.
- Player-trust factors: disclosure is local. Partial healing and documented
  source conflicts are stated; a creator-costly projectile is not owner-safe.
- Claim IDs: `CZ-001`–`CZ-013`.

## Replay and variation

- What changes between sessions: chosen branch, used tools, attack placement,
  received damage, helper deployment and remaining inventory/health.
- Randomness or procedural generation: authored panel layout; exact enemy
  choices and numerical randomness uninspected. No generated page is claimed.
- Multiple viable strategies: direct breaking versus placed blast, close
  fighting versus tool/fist, right versus down, reachable lever versus
  compatible remote contact. Not every inventory plan is guaranteed viable.
- Typical replay motive: explore the other route and conserve health/items.
- Claim IDs: `CZ-002`–`CZ-013`.

## Adjacent systems and history

- Direct predecessors: none established as a genealogy claim.
- Related systems: live arena combat, constrained carried tools and authored
  fixture routes; resemblance is not historical derivation.
- Distinguishing evidence: shared-slot helper, health-paid obstacle work and
  automatically returning owner-dangerous projectile within one comic page.
- Claim IDs: `CZ-003`–`CZ-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-009`, `ACT-089`, `ACT-131`, `ACT-161`, `ACT-202`, `ACT-270`, `ACT-295`, `ACT-296`, `ACT-297`, `ACT-341`, `ACT-662` | Controls, posture, item and reach |
| System Behaviour | `SYS-020`, `SYS-036`, `SYS-045`, `SYS-112`, `SYS-215`, `SYS-470`, `SYS-578`, `SYS-755`, `SYS-1308`, `SYS-1309`, `SYS-1310`, `SYS-1311` | Damage, cost, serial threshold and output |
| Constraint | `CON-175`, `CON-176`, `CON-210`, `CON-402`, `CON-442`, `CON-685` | Three slots and directed branches |
| Information | `INF-119`, `INF-128`, `INF-192`, `INF-467` | Local panel, item and advice |
| Objective | `OBJ-026` | Page exit |
| Time | `TIM-003` | Live update and explicit pause |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `489` (`GAME-0001`–`GAME-0489`).
- Exact genome matches: none.
- Tied near matches: `GAME-0330` — Silent Hill 2 (2024 remake) (`14 / 47 = 0.297872`).
- Supported combination subsets: none.
- Scan date: 2026-10-04.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0330` Silent Hill 2 (2024) | Direct movement, addressed pickup, immediate items, aimed tool attacks, fixture operations, finite carried slots, state-gated commands, loot disclosure, local exit, autonomous hostiles, live combat, one health pool, destructible objects and real-time input | Eastern South Vale's repaired-record/key route differs from a one-way comic page: Comix Zone adds health-paid obstacle work, shared-slot rat, humanoid finishers, blast/return risk and crate-to-lever dependency; no radio, fog map, record assembly, consumed route key or apartment progression is inferred | Tied near: `14 / 47 = 0.297872` |

### Preserved research notes

- New genes: six evidenced additions with thirty unchanged boundary transfers.
- Classification result: `New gene`.
- Evidence and reasoning: the full page preserves ordinary combat, fixtures,
  resources and both fork alternatives, not just its unusual artwork.

## Taxonomy impact

- Registry changes: `ACT-662`, `SYS-1308`–`SYS-1311`, `INF-467`.
- Taxonomy-change record:
  [TAXONOMY_CHANGE_227](../../../research/taxonomy-changes/TAXONOMY_CHANGE_227.md).
- Candidate terms affected: no candidate is promoted by a similarity tool.

## Negative results

- No separate named-item, comic-skin, exact-healing or universal roll-immunity
  gene. No historical derivation or original-port parity was established.

## Delta summary

## New facts

- [Observation | Corroborated | Medium] First-page slot, crate, helper and
  returning-projectile dependencies are preserved; `CZ-004`–`CZ-009`.

## New genes

- [Observation | Corroborated | Medium] Six additions; `TAXONOMY_CHANGE_227`.

## New combinations

- [Observation | Corroborated | Medium] No new recurring combination claimed.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_227`; prior signatures,
  platform identities and release mappings unchanged.

## New questions

- Exact native cost, guard/serial-reset and pickup/health-conflict measurements.
- Original regional revision and port comparisons need independently scoped evidence.

## Next recommended game

- [Hypothesis | Limited | Medium] Original BBC Micro disc *Elite*, `GAME-0491`.
- Optimisation criterion: preserve the approved varied-platform order.
- Expected information gain: trade/travel/encounter settlement, not comic combat.
- Backlog impact: unit 5/9 follows full acceptance and one local commit.

## Why this game

- [Hypothesis | Limited | Medium] The approved Genesis packet tests a portable
  health/tool/fixture boundary alongside many fitting prior carriers.
