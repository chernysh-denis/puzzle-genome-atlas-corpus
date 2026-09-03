---
game_id: GAME-0204
slug: crusader-kings-iii
game_title: "Crusader Kings III"
analysis_status: reviewed
reviewed: 2026-08-31
combination_ids:
  - COMB-0202
gene_ids:
  action:
    - ACT-006
    - ACT-189
    - ACT-365
    - ACT-366
    - ACT-367
    - ACT-368
    - ACT-369
  system:
    - SYS-205
    - SYS-297
    - SYS-670
    - SYS-671
    - SYS-672
    - SYS-673
    - SYS-674
    - SYS-675
    - SYS-676
    - SYS-677
    - SYS-678
    - SYS-679
  constraint:
    - CON-538
    - CON-539
    - CON-540
    - CON-541
    - CON-542
    - CON-543
  information:
    - INF-260
    - INF-261
    - INF-262
    - INF-263
    - INF-264
  objective:
    - OBJ-126
  time:
    - TIM-003
---

# Game: Crusader Kings III

## Analysis scope

- Version / ruleset: unmodified Windows Steam public version `1.19.0.6`, build
  `23530548` dated 2026-06-04, reviewed 2026-08-31; English single-player
  **Learning the Game** tutorial as Petty King Murchad mac Donnchad of Munster
  in 1066, default tutorial game rules, Ironman off, no mods and every
  separately selectable DLC disabled.
- Primary decision loop: inspect Murchad, candidates, opinions, relationships,
  council, titles, vassals, claims, levies, gold and tutorial guidance; choose
  a lifestyle focus, marriage, councillor/task and legal character or title
  interaction; advance or pause time; declare the instructed war for Desmond,
  raise and route the available army, resolve battle and siege, then enforce
  demands when the war score permits and read the tutorial completion state.
- Entry and exit: entry is the first retained controllable tutorial frame as
  Murchad. Positive exit is the explicit guided-tutorial completion state after
  the instructed Desmond war has been won, demands have settled and retained
  campaign control is returned. Stop before free post-tutorial play. Murchad's
  death, succession, creating the Kingdom of Ireland or an arbitrary calendar
  date are not terminals for this packet.
- Included: Murchad's fixed 1066 character, traits, skills and Diplomacy
  lifestyle choice; candidate filtering and one ordinary marriage; the
  tutorial council, one eligible appointment and instructed tasks; titles,
  realm/domain distinction, the starting vassal relation and levy contribution;
  the available Desmond claim/casus belli; gold/prestige costs exposed by the
  route; war declaration, rally and raising, army movement, battle, retreat,
  siege, occupation, war score, enforce demands, title/vassal settlement,
  tutorial prompts, pause and simulation speeds.
- Excluded: any play after the completion prompt; succession, heirs as a
  terminal system, Murchad's death and later generations; forming Ireland;
  fabricated claims or schemes not required by the accepted tutorial trace;
  construction, innovations, culture, faith reform, stress, factions, hooks,
  secrets, prisoners and mercenaries except incidental read-only state; custom
  rulers, other bookmarks or characters; multiplayer, Ironman, achievements,
  mods, console commands, ruler designer, DLC tutorials and all DLC systems.
- Potential scoped modules: one succession transition, one intrigue scheme,
  one fabricated-claim packet, one title-creation route, one independently
  versioned DLC start or one later-generation campaign segment each requires a
  separate entry and terminal contract.
- Direct-play status: no authenticated current Windows tutorial was played.
  Official version, product, tutorial, Murchad and feature sources establish the
  current executable and base mechanics; current and historical Steam tutorial
  traces corroborate the ordered Desmond completion boundary. The repository
  transition table is rules reasoning, not a direct-play claim.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CK3-001` | Version `1.19.0.6` / build `23530548` is the reviewed current Windows Steam public rules boundary | Confirmed | Corroborated | High | P1, S1 |
| `CK3-002` | Learning the Game places the player in retained control of Petty King Murchad of Munster and teaches through the live campaign interface | Confirmed | Direct | High | P2, P3 |
| `CK3-003` | Characters expose traits, skills, relationships and opinions that condition eligible interactions and their consequences | Confirmed | Direct | High | P3, P4 |
| `CK3-004` | One eligible ordinary marriage changes persistent spouse and alliance/relationship state | Observation | Corroborated | High | P2, P4 |
| `CK3-005` | Council membership and assigned tasks convert councillor skill into realm or claim progress over time | Observation | Corroborated | High | P2, P5 |
| `CK3-006` | Realm, domain, titles and vassal relations determine ownership, obligations and available levies | Observation | Corroborated | High | P4, P5, S2 |
| `CK3-007` | A valid claim or de jure casus belli is required to declare the instructed Desmond war | Observation | Corroborated | High | P4, P6, S2 |
| `CK3-008` | Raised levies and men-at-arms gather, follow map orders and resolve battles and retreat under commanders | Confirmed | Corroborated | High | P4, P6 |
| `CK3-009` | A hostile fortified holding needs an eligible besieging force; completed siege creates occupation and war score | Observation | Corroborated | High | P4, P6, S3 |
| `CK3-010` | Battles, occupations, captives and the war objective update war score, which gates enforce demands | Observation | Corroborated | High | P4, P6, S3 |
| `CK3-011` | Winning and settling the instructed Desmond war produces the tutorial's explicit completion state while the broader campaign remains playable | Observation | Corroborated | High | P2, S3, S4 |
| `CK3-012` | Succession and forming Ireland occur outside the explicit guided completion boundary | Observation | Corroborated | High | P4, S4 |

## Basic data

- Release / origin: Paradox Development Studio and Paradox Interactive;
  Windows PC release 2020, reviewed at `1.19.0.6` in 2026.
- Platform or physical form: pausable real-time character-and-realm grand
  strategy on Windows; one current base-game single-player tutorial is scoped.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  agent routing and coordination; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official Update 1.19.0.6 announcement](https://steamcommunity.com/ogg/1158310/announcements/detail/677373278422041208),
    for the latest named stable version before the reviewed public build.
  - **[P2]** [official tutorial developer diary](https://store.steampowered.com/news/app/1158310/view/1719750490053071870),
    for the guided live-interface tutorial and Murchad start.
  - **[P3]** [official Petty King Murchad page](https://www.paradoxinteractive.com/games/crusader-kings-iii/legends-of-crusader-kings-iii/petty-king-murchad),
    for Murchad, Munster, traits, Diplomacy lifestyle and relationship focus.
  - **[P4]** [official Steam product page](https://store.steampowered.com/app/1158310/Crusader_Kings_III/),
    for characters, dynasties, marriage, claims, vassals, levies and warfare.
  - **[P5]** [official March developer-diary digest](https://store.steampowered.com/news/posts/?appids=1158310&enddate=1586262735),
    for tutorials, governments, vassal management, council-linked realm
    systems, men-at-arms and casus belli.
  - **[P6]** [official console feature description](https://www.paradoxinteractive.com/games/crusader-kings-iii/news/crusader-kings-iii-console-edition-coming-soon),
    used for the shared base rules of political marriage, vassal levies,
    men-at-arms and castle sieges, not for a console control claim.
- Reproducible mechanics sources:
  - **[S1]** [SteamDB public build record](https://steamdb.info/patchnotes/23530548/),
    for public build `23530548` dated 2026-06-04 after the named `1.19.0.6`
    patch.
  - **[S2]** [current Steam tutorial realm discussion](https://steamcommunity.com/app/1158310/discussions/0/3114795024909694845/),
    for the tutorial's Thomond/Ormond realm-domain distinction and Desmond de
    jure boundary.
  - **[S3]** [current Steam Desmond tutorial trace](https://steamcommunity.com/app/1158310/discussions/0/597410050678479543/),
    for the instructed claim, raising, battle, siege and won-war route in the
    2025 client lineage.
  - **[S4]** [Steam tutorial completion discussion](https://steamcommunity.com/app/1158310/discussions/0/3052862273807031500/),
    for Desmond victory as completion and forming Ireland only afterwards.
- Claim IDs: `CK3-001`–`CK3-012`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-006`, change the running simulation speed; `ACT-189`,
  issue a selected army a reachable destination or hostile target.
- New genes: `ACT-365`, choose one eligible lifestyle focus; `ACT-366`, propose
  one eligible marriage from the current candidate set; `ACT-367`, appoint an
  eligible councillor and assign one legal council task; `ACT-368`, declare war
  using one available casus belli; `ACT-369`, raise or disband the available
  realm troops at a legal rally point.
- Parameters: character, lifestyle, focus, candidate, marriage type, acceptance,
  councillor, office, task, target, title, casus belli, cost, rally point, army,
  map destination, speed and pause.
- Claim IDs: `CK3-003`–`CK3-008`.

### System Behaviour Genes

- Existing genes: `SYS-205`, update directed opinion and persistent
  relationships; `SYS-297`, execute selected-army pathing and hostile attack
  acquisition.
- New genes: `SYS-670`, instantiate the fixed 1066 Murchad tutorial state;
  `SYS-671`, derive interaction and realm effects from character traits, skills
  and opinions; `SYS-672`, settle an accepted marriage into spouse,
  relationship and alliance state; `SYS-673`, advance assigned council tasks
  from office and skill; `SYS-674`, propagate titles, domain and vassal
  obligations into taxes and levies; `SYS-675`, instantiate a declared claim-
  bounded war and its objective; `SYS-676`, gather available levy and men-at-
  arms contributions into a raised army; `SYS-677`, resolve commander-led army
  movement, battles, retreat and siege; `SYS-678`, convert battles, occupation,
  prisoners and objective control into war score; `SYS-679`, enforce demands,
  transfer the scoped title/vassal result and settle tutorial completion.
- Resolution order: instantiate Murchad and tutorial guidance; accept focus,
  marriage and council choices; advance time-driven relationship, task and
  realm state; validate and declare the Desmond war; gather troops; execute map
  movement, battle, retreat and siege while time runs; update occupation and
  war score; enforce demands; apply the title relation and completion state.
- Parameters: 1066 start, character graph, skill, trait, opinion, marriage,
  alliance, office, task rate, title rank, domain, vassal obligation, levy,
  men-at-arms, rally time, commander, terrain, advantage, casualties, retreat,
  fort level, siege progress, occupation, prisoner, war objective, war score,
  demand and tutorial flag.
- Claim IDs: `CK3-002`–`CK3-012`.

### Constraint Genes

- New genes: `CON-538`, a lifestyle focus must belong to the character's
  available lifestyle state; `CON-539`, marriage requires eligible partners,
  compatible doctrine/relationship rules and acceptance; `CON-540`, council
  appointment and task assignment require the correct office, character and
  target eligibility; `CON-541`, war declaration requires an available casus
  belli, a legal target and any displayed cost or truce condition; `CON-542`,
  troop raising and command require available contributions, legal rally state
  and reachable map orders; `CON-543`, demands require sufficient war score and
  a still-valid war settlement.
- Scarce strategic resources: calendar time, gold, prestige where required,
  opinion, alliance value, council skill and task time, domain capacity, vassal
  obligations, levies, men-at-arms, supply, army strength, commander advantage,
  siege strength and war score.
- Claim IDs: `CK3-003`–`CK3-011`.

### Information Genes

- New genes: `INF-260`, expose character traits, skills, opinions,
  relationships and lifestyle; `INF-261`, expose titles, realm/domain,
  vassals, claims and de jure map relations; `INF-262`, expose marriage and
  council candidates, eligibility, expected effects and task progress;
  `INF-263`, expose levies, rally state, army composition, movement, battle,
  retreat and siege; `INF-264`, expose casus belli, war objective, war score,
  enforce-demand eligibility and tutorial completion.
- Claim IDs: `CK3-003`–`CK3-011`.

### Objective Genes

- New gene: `OBJ-126`, complete Murchad's guided tutorial by winning and
  settling the instructed Desmond war.
- Success, evaluation and failure: success requires the war result, enforce-
  demands settlement and explicit tutorial completion state. Abandoning or
  losing the route before that state fails the bounded attempt; continued
  campaign survival, a succession or creating Ireland does not extend it.
- Claim IDs: `CK3-002`, `CK3-011`, `CK3-012`.

### Time Genes

- Existing gene: `TIM-003`, relationships, council tasks, rallying, movement,
  battles and sieges advance on a real-time schedule while the player may pause
  for unbounded planning or select a faster running rate.
- Claim IDs: `CK3-004`–`CK3-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Public `1.19.0.6` / `23530548` is selected with DLC and mods off | Start Learning the Game | The fixed 1066 Murchad state reaches its first retained guided frame | current bounded entry | `CK3-001`, `CK3-002` |
| Murchad has an available Diplomacy focus | Select the prompted eligible focus | Its persistent bonuses and event weighting become active | character development changes later relations | `CK3-003` |
| One compatible candidate is visible | Propose the chosen ordinary marriage | Acceptance creates spouse and relationship state and may create an alliance | candidate evaluation becomes persistent political structure | `CK3-004` |
| A council office or task is editable | Appoint an eligible character and assign the prompted task | Office skill and target begin contributing their declared timed effects | people are productive assignments, not static bonuses | `CK3-005` |
| The realm view distinguishes held domain, vassal land and de jure titles | Inspect Murchad, Ormond and Desmond | Ownership and obligation panels disclose direct control, vassal contribution and the legal Desmond relation | title hierarchy drives available power and war | `CK3-006`, `CK3-007` |
| The Desmond casus belli is available and no gate blocks declaration | Declare the instructed war | The game binds attacker, defender, objective and settlement effects into one war | claims are executable legal predicates | `CK3-007` |
| Realm contributions are available and the war is active | Raise all available troops at the rally point | Levies and men-at-arms gather over time into a selected army | military capacity is derived from the realm | `CK3-006`, `CK3-008` |
| The raised army can reach hostile territory | Issue the instructed destination or hostile order | Pathing moves the army; contact instantiates battle, casualties and retreat | map routing and combat share one live clock | `CK3-008` |
| A sufficient living army occupies Desmond's hostile fortified holding | Remain and advance time | Siege phases progress; completion occupies the holding and adds war score | fortification requires sustained local force | `CK3-009`, `CK3-010` |
| Battles and occupation provide enough war score | Choose Enforce Demands | The declared result settles, Desmond's title/vassal relation changes and the war closes | war score gates legal state transfer | `CK3-010`, `CK3-011` |
| The instructed Desmond settlement has resolved | Dismiss/read the completion guidance | The tutorial records completion and returns retained campaign authority | explicit terminal exists before open campaign play | `CK3-011`, `CK3-012` |

## Strategic and experiential structure

- Local decision: compare a person, candidate or office, inspect one title or
  army, pause, change speed, reroute troops or wait for a siege phase.
- Medium-term planning: align relationship and council choices with the levies,
  claim and commander capacity needed for the instructed war.
- Long-term structure: convert Murchad's character network and feudal realm into
  one legal war, then convert battle and occupation into the enforceable
  Desmond settlement without importing the open campaign.
- Common heuristics: pause before irreversible interactions; read acceptance
  and effect tooltips; use the strongest eligible council skill; wait for full
  rally; keep the army together; avoid chasing a retreat when the fort is the
  objective; verify 100 war score before enforcing demands.
- Failure attribution: character and candidate panels explain eligibility;
  realm/title views explain legal authority and levies; army and siege panels
  explain strength and progress; the war view separates objective, battle,
  occupation and settlement state.
- Player-trust factors: explicit prerequisites, predicted interaction effects,
  reversible pause/speed control, inspectable title hierarchy and one named
  completion prompt keep the trace auditable.
- Claim IDs: `CK3-003`–`CK3-012`.

## Replay and variation

- What changes between attempts: spouse/council choices, event timing, AI army
  route, battle casualties, captives, siege duration and the exact completion
  date.
- Randomness or procedural generation: fixed historical actors and titles open
  the tutorial, while combat, events and AI response can diverge.
- Multiple viable strategies: stronger marriage alliance, better martial task,
  patient full rally or direct numerical superiority can support the same
  instructed legal war and settlement.
- Typical replay motive: make cleaner character/council choices, lose fewer
  levies, avoid unnecessary pursuit and reach the same completion state sooner.
- Claim IDs: `CK3-003`–`CK3-011`.

## Adjacent systems and history

- Direct predecessors: earlier Crusader Kings games share dynasty-centred
  feudal strategy; this record does not import their exact rules.
- Variants: succession, schemes, fabricated claims, other rulers and DLC starts
  change the dependency graph and need separate bounded terminals.
- Similar games: Hearts of Iron IV shares pausable grand-strategy time and
  army routing; Total War: WARHAMMER III shares a guided campaign-to-battle
  route; The Sims 4 shares inspectable relationships; RimWorld shares
  opinion-driven persistent interpersonal state.
- Important differences: this tutorial makes people simultaneously actors,
  offices, family links and sources of legal/military capacity, then settles
  one claim-defined war without requiring dynasty succession.
- Claim IDs: `CK3-002`–`CK3-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-189`, `ACT-365`–`ACT-369` | people, offices, title and control bindings are parameters |
| System Behaviour | `SYS-205`, `SYS-297`, `SYS-670`–`SYS-679` | numeric opinion, task and combat formulas are parameters |
| Constraint | `CON-538`–`CON-543` | costs, thresholds and eligibility values are parameters |
| Information | `INF-260`–`INF-264` | layout and exact displayed numbers are presentation |
| Objective | `OBJ-126` | Murchad, Desmond and tutorial are parameters |
| Time | `TIM-003` | pause and speed values are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `203` (`GAME-0001`–`GAME-0203`).
- Exact genome matches: none.
- Tied near matches: `GAME-0182` — Hearts of Iron IV (`4 / 66 = 0.060606`).
- Supported combination subsets: `COMB-0202`.
- Scan date: 2026-08-31.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0182` — Hearts of Iron IV | `ACT-006`, `ACT-189`, `SYS-297`, `TIM-003` | Both are pausable grand-strategy tutorials in which selected armies follow contextual map orders while time can be accelerated. Hearts of Iron IV converts national focus, research, industry, supply, air missions and territorial surrender into Ethiopian capitulation; Crusader Kings III converts character, marriage, council, title, vassal and casus-belli relations into a Desmond settlement and tutorial-complete state | Near, `0.060606` |

### Preserved research notes

- New genes: `ACT-365`–`ACT-369`, `SYS-670`–`SYS-679`, `CON-538`–`CON-543`,
  `INF-260`–`INF-264` and `OBJ-126`.
- Reused genes: `ACT-006`, `ACT-189`, `SYS-205`, `SYS-297` and `TIM-003`; no
  earlier signature changed.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: generic opinion, live army routing and pausable time
  remain reusable; the character-office-title-claim-war tutorial chain remains
  bounded new structure.

## Taxonomy impact

- Registry changes: twenty-seven bounded Active genes and `COMB-0202`; no
  earlier reviewed game signature changes.
- Taxonomy-change record: none.
- Candidate terms affected: lifestyle focus, political marriage, council task,
  realm/domain, vassal obligation, claim, casus belli, levy gathering, siege,
  war score, enforce demands and tutorial settlement.

## Negative results

- The explicit Desmond tutorial completion prompt is used instead of inventing
  an Ireland-conquest or calendar terminal; no selection amendment is needed.
- The current 1066 Murchad base-game tutorial is kept separate from the
  DLC-specific Qin Guan tutorial and all expansion mechanics.
- Succession is visible as product context but not causally required before the
  terminal, so no succession gene is admitted.
- Incidental random events, prisoners and costs remain parameters or exclusions
  unless they become necessary in a reproduced legal route.
- No prior combination is accepted from genre resemblance; proper-subset
  support remains validator-owned.
