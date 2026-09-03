---
game_id: GAME-0181
slug: overwatch
game_title: Overwatch
analysis_status: reviewed
reviewed: 2026-08-29
combination_ids:
  - COMB-0179
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-187
    - ACT-188
    - ACT-190
    - ACT-191
    - ACT-322
    - ACT-323
  system:
    - SYS-208
    - SYS-215
    - SYS-299
    - SYS-380
    - SYS-381
    - SYS-382
    - SYS-395
    - SYS-560
    - SYS-561
    - SYS-562
  constraint:
    - CON-269
    - CON-272
    - CON-348
    - CON-474
    - CON-475
    - CON-476
  information:
    - INF-115
    - INF-116
    - INF-119
    - INF-150
    - INF-228
  objective:
    - OBJ-105
  time:
    - TIM-003
---

# Game: Overwatch

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current Windows PC live client, Steam public build
  `24782458`, Reign of Talon Season 4 retail boundary dated `2026-08-11` and
  checked `2026-08-29`; one ordinary unranked Quick Play Role Queue 5v5 Control
  match on Busan, Damage role, starting as Soldier: 76, from map ballot and hero
  selection until either team wins two Control rounds.
- Primary decision loop: commit the Damage queue slot; vote among the offered
  maps; select a role-legal unoccupied hero; move, aim, fire, reload, use
  cooldown abilities, communicate and contest the active point; turn combat
  contribution into ultimate and perk choices; after a knockout respawn and,
  if useful, swap within Damage; win point ownership long enough to take two
  percentage-scored rounds.
- Entry and exit: begins when the matched lobby exposes its four-option map
  ballot. It succeeds or fails when one fixed five-player team earns its second
  Control-round win and the client declares the match result.
- Included: 5v5 Role Queue `1 Tank / 2 Damage / 2 Support`; current map vote,
  including Random Map and landslide settlement; Busan's three Control
  submaps; one neutral point per round; team presence, contest, ownership,
  percentage progress, overtime and first-to-two match settlement; Soldier: 76
  primary fire, reload, Sprint, Biotic Field, Helix Rockets and Tactical Visor;
  health, damage, healing, cooldowns, ultimate charge, two match-local perk
  choices, knockout, timed respawn, team communication and legal Damage-hero
  swap from spawn.
- Reproducible parameterisation: vote Busan whenever it is offered; if the
  ballot settles another map, requeue rather than import a different mode. Pick
  Soldier: 76 whenever unoccupied; if temporarily unavailable, requeue. At each
  perk threshold choose the first displayed legal option in the current
  left-to-right UI order. Exact teammates, opponents, submap order, aim values,
  balance numbers and match duration are parameters.
- Excluded: Competitive ranks, Hero Bans and side/rating settlement; Open Queue
  6v6; Quick Play Hacked Flex/Dynamic Queue tests; Stadium, Arcade, Mystery
  Heroes, Custom, Practice and event modes; Escort, Hybrid, Push, Flashpoint and
  Clash; exhaustive heroes, maps, perks and balance history; Battle Pass,
  challenges, cosmetics, shop, endorsements, account progression, esports and
  post-match rewards.
- Potential scoped modules: one Competitive match with bans; one standard 6v6
  Open Queue match; Stadium rounds and Armory economy; Escort or Hybrid;
  another hero whose role passive and perk branches materially alter the loop.
- Direct-play status: no authenticated live match was played. Current Blizzard
  product, patch, hero, format, map-vote and known-issue material establishes
  the live boundary; maintained mode documentation corroborates the exact
  Control percentage, round and overtime trace. Steam package metadata pins the
  public PC build. The repository trace is rules reasoning, not direct play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `OW-001` | The current product is titled Overwatch; Season 4 uses the `2026-08-11` retail rules boundary and Steam public build `24782458` | Confirmed | Corroborated | High | P1, P2, S1 |
| `OW-002` | Ordinary Unranked Role Queue is the standard 5v5 format and fixes one Tank, two Damage and two Support slots per team | Confirmed | Direct | High | P3, P4 |
| `OW-003` | Quick Play map voting offers three maps plus Random Map and settles by a declared landslide rule or a weighted choice | Confirmed | Direct | High | P5, P6 |
| `OW-004` | Soldier: 76 directly moves, aims and fires an automatic rifle, reloads, sprints, deploys healing, launches rockets and spends an earned ultimate | Confirmed | Direct | High | P7, P8 |
| `OW-005` | Match activity raises a hero through two perk opportunities whose selected effects modify the current hero for the match | Confirmed | Corroborated | High | P7, P9 |
| `OW-006` | Lethal damage removes the hero from control until a timed team-spawn return, where a legal same-role hero swap can occur | Observation | Corroborated | High | P2, P4, S2 |
| `OW-007` | In Control, eligible uncontested presence captures one neutral point; ownership then increases that team's percentage while contest blocks the next ownership transition or terminal | Observation | Corroborated | High | P2, P10, S2 |
| `OW-008` | A Control round normally ends at 100 percent, overtime preserves a legal opposing contest, and the first team to win two rounds wins Quick Play Control | Observation | Corroborated | High | P10, S2 |
| `OW-009` | The known-issues record disables Lifeweaver and Black Forest but does not disable Soldier: 76 or Busan, so the reproducible selection remains legal | Confirmed | Direct | High | P11 |
| `OW-010` | The repository transition trace reproduces role lock, map vote, hero/perk choices, combat, knockout/respawn, Control capture, percentage, overtime and the two-round terminal | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Blizzard Entertainment; first released in 2016 and now an
  continuously updated free-to-play service titled `Overwatch`.
- Platform or physical form: authenticated networked Windows PC client; this
  unit pins the Steam public package but analyses rules shared by the ordinary
  PC live client.
- Puzzle family: simultaneous team objective combat; partial-information
  coordination; real-time system pressure.
- Primary sources:
  - **[P1]** [official Overwatch product page](https://overwatch.blizzard.com/en-us/),
    for the current title and live-service identity, checked 2026-08-29.
  - **[P2]** [official `2026-08-11` retail patch notes](https://overwatch.blizzard.com/en-us/news/patch-notes/live/),
    for Season 4, live Quick Play applicability and the Busan Control rework.
  - **[P3]** [official Future Formats Director's Take](https://overwatch.blizzard.com/en-us/news/24289101/director-s-take-future-formats/),
    for standard 5v5, separate temporary 6v6 Quick Play Hacked experiments and
    current unranked Role Queue participation.
  - **[P4]** [official 5v5 and 6v6 format discussion](https://overwatch.blizzard.com/en-us/news/24104605/),
    for the standard `1-2-2` Role Queue composition and spawn counter-swapping.
  - **[P5]** [official map-voting launch patch](https://overwatch.blizzard.com/en-us/news/patch-notes/live/2025/06/),
    for the three-map Quick Play ballot and vote-weighted selection.
  - **[P6]** [official April 2026 map-voting update](https://overwatch.blizzard.com/en-us/news/patch-notes/live/2026/04/),
    for Random Map, landslide settlement, mode diversity and hidden teammate votes.
  - **[P7]** [official Soldier: 76 hero page](https://overwatch.blizzard.com/en-us/heroes/soldier-76/),
    for the current Damage role, active kit and two Minor/Major perk offers.
  - **[P8]** [official hero ability overview](https://overwatch.blizzard.com/en-us/videos/video/blt409b02d5a04d1616/soldier-76-ability-overview/),
    for the authored direct-combat kit.
  - **[P9]** [official Perks launch patch](https://overwatch.blizzard.com/en-us/news/patch-notes/live/2025/2/),
    for match activity, hero levels, two perk choices and hero-swap handling.
  - **[P10]** [official Quick Play: Hacked comparison](https://overwatch.blizzard.com/en-us/news/24021898/),
    for traditional Control capture and percentage progress as the normal
    baseline to which the temporary faster variant was compared.
  - **[P11]** [official known issues, updated 2026-08-21](https://us.forums.blizzard.com/en/overwatch/t/overwatch-known-issues-aug-21-2026/942905/1),
    for current temporary hero/map exclusions and the retained Busan/Soldier scope.
- Secondary and reproducible sources:
  - **[S1]** [SteamDB Overwatch depots](https://steamdb.info/app/2357570/depots/),
    observed 2026-08-29, for Steam public build `24782458`; Blizzard sources
    independently establish the retail patch and season.
  - **[S2]** [maintained Overwatch Wiki Control reference](https://overwatch.fandom.com/wiki/Control),
    for ordinary point unlock, 100-percent rounds, best-of-three settlement,
    contest and overtime edge conditions not stated together by Blizzard.
  - **[V1]** repository-side transition trace derived from `P1`–`P11` and
    checked against `S1`–`S2`; executable rules reasoning, not direct play.
- Claim IDs: `OW-001`–`OW-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, directly navigate the hero; `ACT-161`, aim and
  strike with the current weapon; `ACT-164`, select the active weapon or
  ability input; `ACT-183`, reload; `ACT-187`, transmit a team cue; `ACT-188`,
  commit one available match hero; `ACT-190`, cast one ready ability or
  ultimate; `ACT-191`, spend one unlocked match-local perk choice.
- New genes: `ACT-322`, commit one Role Queue slot before matchmaking;
  `ACT-323`, cast one vote for an offered map or Random Map.
- Parameters: role, hero, weapon, aim, ability, cooldown, ultimate, perk tier,
  communication channel, map offer and ballot choice.
- Claim IDs: `OW-002`–`OW-006`.

### System Behaviour Genes

- Existing genes: `SYS-208`, resolve ranged attacks through aim, cover and hit
  state; `SYS-215`, resolve simultaneous hostile combat; `SYS-299`, convert
  eligible match activity into hero-level and perk opportunities; `SYS-380`,
  resolve each selected hero ability into its typed effect; `SYS-381`, build
  and spend ultimate readiness; `SYS-382`, resolve knockout and timed team-spawn
  return; `SYS-395`, convert eligible point occupancy into contested ownership.
- New genes: `SYS-560`, settle a map ballot through landslide or weighted/random
  selection; `SYS-561`, convert sustained Control ownership into percentage and
  one round win; `SYS-562`, reset the active Control point between rounds and
  convert the first two round wins into the match result.
- Resolution order: commit role; settle map vote; select a legal Damage hero;
  resolve continuous movement, weapon, ability, perk and team-cue inputs;
  lethal damage starts respawn; uncontested presence captures the point;
  ownership advances percentage; a legal contest preserves overtime; round
  settlement resets local point state but retains round score; the second round
  win terminates the match.
- Claim IDs: `OW-002`–`OW-010`.

### Constraint Genes

- Existing genes: `CON-269`, ability use requires legal target, range,
  readiness and resource; `CON-272`, knockout blocks hero control until return;
  `CON-348`, control progress requires uncontested eligible presence.
- New genes: `CON-474`, Role Queue fixes one Tank, two Damage and two Support
  slots per team; `CON-475`, hero selection and swapping require the committed
  role, team uniqueness and legal spawn state; `CON-476`, Control percentage
  and overtime require current ownership or continuing eligible objective
  pressure rather than eliminations elsewhere.
- Scarce strategic resources: health, living teammates, point presence,
  cooldown readiness, ammunition, ultimate charge, perk timing, sightlines,
  cover, respawn time and round percentage.
- Claim IDs: `OW-002`, `OW-004`–`OW-008`.

### Information Genes

- Existing genes: `INF-115`, local sight, sound and effects expose only nearby
  opponents; `INF-116`, the team HUD exposes allied, round, clock, point,
  percentage, contest and overtime state; `INF-119`, the hero HUD exposes
  health, ammunition, cooldowns, status, ultimate and perk progress; `INF-150`,
  the roster exposes heroes, roles, kits and allied occupancy.
- New gene: `INF-228`, the pre-match ballot exposes three candidate maps, their
  modes, Random Map and the player's selectable vote state.
- Claim IDs: `OW-003`–`OW-008`.

### Objective Genes

- New gene: `OBJ-105`, win one Quick Play Control match by earning two round
  wins before the opposing team.
- Success, evaluation and failure: one round requires legal point ownership to
  reach its terminal percentage after any eligible overtime; eliminations are
  only means. The second retained round win ends the match.
- Claim IDs: `OW-007`, `OW-008`, `OW-010`.

### Time Genes

- Existing gene: `TIM-003`, movement, attacks, healing, cooldowns, ultimate and
  perk gain, respawn, capture, percentage and overtime advance continuously.
- Parameters: attack cadence, cooldown, respawn, point unlock, capture rate,
  score rate, overtime decay and round transition.
- Claim IDs: `OW-004`–`OW-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Quick Play Role Queue is open | Commit Damage and enter matchmaking | The matched team reserves two Damage slots beside one Tank and two Support slots | Role is a pre-match composition constraint | `OW-002` |
| The lobby exposes three maps and Random Map | Vote Busan | A landslide selects it directly; otherwise the declared weighted/random rule settles one candidate | Map choice influences but does not fully determine the match | `OW-003` |
| Damage selection is open and Soldier: 76 is unoccupied | Select Soldier: 76 | The slot gains his current weapon, active abilities, ultimate and perk track | Match identity is role- and team-bounded | `OW-004`, `OW-005` |
| A visible hostile is reachable | Aim, fire and reload the Heavy Pulse Rifle | Ballistics apply legal damage and consume ammunition; reload restores the magazine after its channel | Direct aim and ammunition timing matter | `OW-004` |
| Biotic Field or Helix Rockets is ready | Cast it at a legal point or vector | The authored healing field or explosive projectile resolves and the cooldown starts | Ability identity changes live spatial state | `OW-004` |
| The hero crosses a perk threshold | Spend the first displayed legal perk choice | The chosen authored modifier becomes active for this hero in the current match | Combat progression creates a bounded build branch | `OW-005` |
| Soldier: 76 receives lethal damage | Wait through the respawn timer; optionally select another unoccupied Damage hero in spawn | Live control is removed, then returns through team spawn with a role-legal hero | Knockout costs presence but does not end the match | `OW-006` |
| The round's neutral point is unlocked | Enter it with no eligible opponent present | Capture advances to team ownership; opposing presence contests and pauses the transition | Presence, not kill count, controls the point | `OW-007` |
| The team owns the point | Hold ownership while fighting | Its percentage advances toward 100; loss of ownership redirects future progress without erasing retained percentage | Control converts spatial dominance into round score | `OW-007` |
| The leading team reaches the normal terminal while an opponent maintains eligible point pressure | Continue contesting | Overtime preserves the round until the contest clears or ownership reverses | Terminal time is pressure-gated | `OW-008` |
| One team has one round win and wins the next active point | Complete the percentage terminal after any overtime | The second round win is retained and the client declares that team the match winner | First-to-two is the bounded terminal | `OW-008`, `OW-010` |

## Strategic and experiential structure

- Local decision: aim or reposition; fire, reload, sprint, heal, rocket, use an
  ultimate, communicate, or preserve a cooldown while reading threat and point
  state.
- Medium-term planning: choose perks and hero swaps that answer the current
  composition; synchronise returns; trade point percentage against space,
  health and ultimate economy rather than feeding alone.
- Long-term structure: use the map ballot and role commitment to enter one
  Control fixture, learn opponent composition, adjust within Damage, convert
  won fights into ownership and preserve enough coordinated pressure to win two
  distinct submap rounds.
- Common heuristics: regroup after staggered deaths; take cover before reload;
  contest only with a viable return path; use Biotic Field where allies can
  share it; avoid spending multiple ultimates on a secured fight; swap only
  when the new kit repays lost familiarity and current charge.
- Failure attribution: hit feedback and death recap expose combat loss; hero
  HUD exposes cooldown/ammunition errors; team frames show staggered returns;
  point/percentage/overtime UI distinguishes lost space from lost damage races.
- Player-trust factors: explicit role and map commitments, readable ability and
  perk state, visible point ownership, retained percentage, announced overtime
  and an unambiguous two-round result.
- Claim IDs: `OW-002`–`OW-010`.

## Replay and variation

- What changes between sessions: ballot candidates, selected map, Control
  submap order, team and opponent heroes, perk choices, swaps, positioning,
  ultimate economy and fight outcomes.
- Randomness or procedural generation: matchmaking and ballot settlement vary;
  the authored map and hero rules are fixed at the pinned patch. Random Map is
  an explicit ballot option rather than hidden world generation.
- Multiple viable strategies: direct pressure, off-angle fire, grouped point
  play, high-ground control and timely same-role counter-swaps can all produce
  the required two rounds.
- Typical replay motive: improve aim, positioning, cooldown/ultimate economy,
  perk timing, composition response and coordinated objective conversion.
- Claim IDs: `OW-003`–`OW-008`.

## Adjacent systems and history

- Direct predecessors: Overwatch 2 and the original Overwatch are product
  lineage, but the canonical title and current 2026 live rules alone define
  this record.
- Variants: 6v6 Open Queue changes composition; Quick Play Hacked temporarily
  changes formats or rates; Competitive adds bans, rating and different
  settlement; Stadium adds rounds, currency, items and Powers.
- Similar games: Marvel Rivals shares live hero selection, cooldown abilities,
  ultimate economy, knockout/respawn, team communication and an objective HUD;
  Battlefield 6 shares capture occupancy and contested control.
- Important differences: this scope fixes pre-queue `1-2-2` roles, a
  player-influenced map ballot, two in-match perk choices and a symmetric
  neutral-point percentage race across first-to-two Control rounds.
- Claim IDs: `OW-002`–`OW-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-187`, `ACT-188`, `ACT-190`, `ACT-191`, `ACT-322`, `ACT-323` | hero control, role, ballot, weapon, ability, cue and perk choices |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-299`, `SYS-380`, `SYS-381`, `SYS-382`, `SYS-395`, `SYS-560`–`SYS-562` | combat, progression, respawn, vote and Control settlement |
| Constraint | `CON-269`, `CON-272`, `CON-348`, `CON-474`–`CON-476` | legal ability, return, role, hero and objective gates |
| Information | `INF-115`, `INF-116`, `INF-119`, `INF-150`, `INF-228` | local combat, hero/team/objective HUD and ballot |
| Objective | `OBJ-105` | first to two Control-round wins |
| Time | `TIM-003` | continuously advancing live match |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `180` (`GAME-0001`–`GAME-0180`).
- Exact genome matches: none.
- Tied near matches: `GAME-0149` — Battlefield 6 (`18 / 50 = 0.360000`).
- Supported combination subsets: `COMB-0179`.
- Scan date: 2026-08-29.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Battlefield 6 (`GAME-0149`) | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-187`, `ACT-190`, `SYS-208`, `SYS-215`, `SYS-380`, `SYS-382`, `SYS-395`, `CON-269`, `CON-272`, `CON-348`, `INF-115`, `INF-116`, `INF-119`, `TIM-003` | Battlefield 6 uses classes, vehicles, downed revival and multi-point ticket attrition; Overwatch uses unique swappable heroes, perk/ultimate progression and one neutral percentage point per round | Near, `0.360000` |

### Preserved research notes

- New genes: `ACT-322`–`ACT-323`, `SYS-560`–`SYS-562`, `CON-474`–`CON-476`,
  `INF-228` and `OBJ-105`.
- Classification result: twenty-three established hero-combat, capture,
  information and real-time boundaries are reused; ten genes isolate the
  current role queue, ballot and Control round structure.
- Evidence and reasoning: no earlier gene combines the four-option map ballot
  with landslide/weighted settlement, and neither Convergence nor Conquest
  expresses the retained percentage plus first-to-two submap reset.

## Combination status

- `COMB-0179` is a verified strict subset coupling the pre-match role and map
  commitments, swappable role-legal hero combat, match-local perks, respawn,
  percentage control and retained first-to-two round settlement.
- Earlier verified combinations remain tested after registration.

## Taxonomy impact

- Registry changes: ten new Active genes, twenty-three reused Active genes and
  `COMB-0179`.
- Taxonomy-change record: none; no existing definition is deprecated, merged,
  split or altered.
- Candidate terms affected: none.

## Negative results

- `ACT-237` and `CON-338` retain Marvel Rivals Team-Up partner/loadout
  semantics; Overwatch instead uses Role Queue and independent perk choices.
- `SYS-383`–`SYS-385` and `OBJ-078` retain Convergence's ordered capture-to-
  escort route; Control resets neutral-point state and retains only round score.
- `SYS-396` and `OBJ-079` retain Battlefield Conquest's simultaneous control
  network and reinforcement-ticket terminal; Overwatch has one active point
  and percentage round score.
- Stadium Powers, item currency and round economy are excluded rather than
  folded into ordinary Quick Play Perks.
- Current temporary Hacked formats and disabled content are not treated as the
  stable ordinary ruleset.
