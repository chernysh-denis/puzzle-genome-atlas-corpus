---
game_id: GAME-0138
slug: dota-2
game_title: Dota 2
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0136
gene_ids:
  action:
    - ACT-130
    - ACT-187
    - ACT-188
    - ACT-189
    - ACT-190
    - ACT-191
    - ACT-192
    - ACT-193
  system:
    - SYS-045
    - SYS-051
    - SYS-215
    - SYS-297
    - SYS-298
    - SYS-299
    - SYS-300
    - SYS-301
    - SYS-302
    - SYS-303
    - SYS-304
    - SYS-305
    - SYS-306
  constraint:
    - CON-268
    - CON-269
    - CON-270
    - CON-271
    - CON-272
    - CON-273
    - CON-274
    - CON-275
  information:
    - INF-116
    - INF-118
    - INF-119
    - INF-120
  objective:
    - OBJ-072
  time:
    - TIM-003
---

# Game: Dota 2

## Analysis scope

- Version / ruleset: public PC Dota 2 gameplay update `7.41e`, observed
  2026-08-21; one ordinary unranked 5v5 All Pick match on the standard map,
  from simultaneous hero draft through the first destroyed Ancient.
- Included: hero and facet selection, destination/path commands, basic attacks,
  abilities, talents, gold, experience, items and recipes, stash/courier,
  lane and neutral creeps, towers, barracks, Roshan, wards, fog of war,
  day/night vision, death, respawn, buyback, team communication and Ancient victory.
- Excluded: Ranked MMR and role queue, Turbo, Captains Mode, Ability Draft,
  Single Draft, custom games, bot/tutorial rules, cosmetics, Dota Plus,
  compendiums, behaviour score, Low Priority, esports and post-match rewards.
- Direct-play status: no complete live match was played. Valve's current patch,
  product material and extracted live game definitions were inspected; current
  maintained mechanics references independently corroborated the bounded trace.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DOTA-001` | All Pick forms two five-player teams whose players each commit one hero before the live match | Confirmed | Corroborated | High | P1, P2, S1 |
| `DOTA-002` | Heroes use command-based pathing, basic attacks, mana/cooldown-gated abilities, levels, talents and item actives in continuous time | Confirmed | Corroborated | High | P1, P3, S2 |
| `DOTA-003` | Last hits, nearby kills and objectives create gold/experience progression that converts into levels, skills and shop items | Confirmed | Corroborated | High | P3, S2, S3 |
| `DOTA-004` | Scheduled lane creeps and defensive towers create three progressive routes; barracks destruction improves the opposing lane wave | Confirmed | Corroborated | High | P3, S4 |
| `DOTA-005` | Allied units and wards share vision while terrain, day/night and invisibility preserve incomplete enemy information | Confirmed | Corroborated | High | P3, S5 |
| `DOTA-006` | Death suspends hero control until respawn unless an eligible buyback is paid; destroying the enemy Ancient ends the match | Confirmed | Corroborated | High | P2, P3, S6 |
| `DOTA-007` | The repository control reproduces draft, lane economy, item delivery, death/respawn, buyback, barracks pressure and Ancient destruction | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Valve; public release 2013, continuously updated.
- Platform or physical form: free-to-play PC client and Valve matchmaking.
- Puzzle family: real-time team strategy under fog-limited information.
- Primary sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/570/Dota_2/),
    for Valve authorship, hero roster, abilities, items, free core content and
    continuously changing team play.
  - **[P2]** [official gameplay update 7.41e](https://www.dota2.com/patches/7.41e),
    for the live version boundary and current map, item and hero rules.
  - **[P3]** [current extracted Dota 2 game definitions](https://github.com/SteamTracking/GameTracking-Dota2),
    including standard-map lane spawners, the Ancient win condition and current
    hero, ability, item and unit data.
- Secondary and reproducible sources:
  - **[S1]** [Dota 2 Wiki game-mode reference](https://dota2.fandom.com/wiki/Game_modes),
    for current All Pick selection and timing boundaries.
  - **[S2]** [Liquipedia hero mechanics](https://liquipedia.net/dota2/Heroes),
    for levels, attributes, abilities, talents and death state.
  - **[S3]** [Liquipedia gold mechanics](https://liquipedia.net/dota2/Gold),
    for last hits, shared hero-kill awards and buyback coupling.
  - **[S4]** [Liquipedia buildings reference](https://liquipedia.net/dota2/Buildings),
    for towers, barracks, protection order and lane-pressure effects.
  - **[S5]** [Liquipedia vision reference](https://liquipedia.net/dota2/Vision),
    for fog, shared allied vision, day/night and detection.
  - **[S6]** [Liquipedia death reference](https://liquipedia.net/dota2/Death),
    for respawn and buyback eligibility.
  - **[V1]** repository-side transition trace derived from `P2`–`P3` and checked
    against `S1`–`S6`; it is executable rules reasoning, not direct-play evidence.
- Claim IDs: `DOTA-001`–`DOTA-007`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-130`, buy one offered run asset; `ACT-187`, transmit a
  live team cue.
- New genes: `ACT-188`, commit one hero and build option; `ACT-189`, issue a
  contextual destination/attack command; `ACT-190`, cast one hero or item
  ability; `ACT-191`, spend one level point on an ability or talent;
  `ACT-192`, configure stash/courier delivery; `ACT-193`, pay for buyback.
- Parameters: hero, facet, target type, path, attack order, ability, mana,
  cooldown, skill level, item, courier destination and buyback state.
- Claim IDs: `DOTA-001`–`DOTA-003`, `DOTA-006`.

### System Behaviour Genes

- Existing genes: `SYS-045`, continuous autonomous agent locomotion; `SYS-051`,
  context-triggered autonomous combat engagement; `SYS-215`, direct real-time combat.
- New genes: `SYS-297`, resolve command pathing and attack acquisition;
  `SYS-298`, award match gold and experience; `SYS-299`, convert experience
  into hero levels and build points; `SYS-300`, combine compatible item recipes;
  `SYS-301`, resolve hero death, respawn and buyback; `SYS-302`, spawn and route
  opposing lane waves; `SYS-303`, resolve tower protection and target priority;
  `SYS-304`, propagate barracks loss into stronger enemy creeps; `SYS-305`,
  propagate team vision, fog and detection; `SYS-306`, respawn neutral camps
  and award Roshan's bounded team resource.
- Resolution order: simultaneous commands and autonomous units resolve combat;
  deaths award gold/experience and start respawn; purchases and build points
  alter later combat; lane structure loss changes subsequent waves; a legal
  Ancient destruction terminates the match.
- Claim IDs: `DOTA-002`–`DOTA-006`.

### Constraint Genes

- New genes: `CON-268`, one committed hero per fixed five-player team slot;
  `CON-269`, ability use requires legal target, range, mana and cooldown;
  `CON-270`, hero build is bounded by levels, skill points and talent gates;
  `CON-271`, item ownership obeys gold, shop and inventory logistics;
  `CON-272`, death blocks hero control until respawn or eligible buyback;
  `CON-273`, fog, invisibility and detection gate actionable enemy state;
  `CON-274`, defensive buildings obey ordered protection and backdoor rules;
  `CON-275`, only a legally exposed enemy Ancient can receive the terminal loss.
- Scarce resources: health, mana, cooldowns, gold, experience, item slots,
  teleport resources, ward stock, buyback cost/cooldown, lives in the current
  fight, lane position and vision.
- Claim IDs: `DOTA-001`–`DOTA-006`.

### Information Genes

- Existing gene: `INF-116`, live team score, clock and shared-objective state.
- New genes: `INF-118`, team-shared fog-limited world and minimap state;
  `INF-119`, personal hero health, mana, experience, abilities and cooldowns;
  `INF-120`, gold, shop, inventory, courier and buyback state.
- Claim IDs: `DOTA-002`–`DOTA-006`.

### Objective Genes

- New gene: `OBJ-072`, destroy the opposing Ancient before the opposing team
  destroys yours.
- Success and failure: the first legal Ancient destruction immediately ends
  the match for both teams; hero kills and net worth are means, not victory.
- Claim IDs: `DOTA-004`, `DOTA-006`.

### Time Genes

- Existing gene: `TIM-003`, commands, attacks, cooldowns, spawns, day/night,
  respawn and objectives progress in real time.
- Parameters: draft and pre-game timing, attack interval, cooldown, creep wave,
  neutral respawn, day/night cycle, death timer and buyback cooldown.
- Claim IDs: `DOTA-001`–`DOTA-006`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| All Pick selection is open and the team slot has no hero | Commit an available hero and facet | The slot owns that hero/build option for this match and later commands address it | bounded draft identity | `DOTA-001`, `DOTA-007` |
| Hero is alive and a reachable lane destination is selected | Issue move/attack command | Pathfinding advances the hero; eligible enemies may be acquired and attacked at cadence | command-mediated live control | `DOTA-002`, `DOTA-007` |
| Enemy lane creep is in range and low enough to die from the hit | Commit the basic attack | Lethal last hit removes the creep, awards gold to the hitter and experience to eligible nearby heroes | lane economy | `DOTA-003`, `DOTA-007` |
| Hero has an unspent level point and the ability/talent gate is open | Spend the point | The selected legal build node becomes active and changes later combat parameters | match-local character build | `DOTA-002`, `DOTA-003`, `DOTA-007` |
| Sufficient gold and legal shop access exist | Purchase a component | Gold is deducted; the component enters inventory/stash and complete compatible recipes combine | item economy and assembly | `DOTA-003`, `DOTA-007` |
| Purchased item waits in stash and the courier is alive | Request delivery | Courier pathing carries eligible items to the hero; death can interrupt the delivery | vulnerable team logistics | `DOTA-003`, `DOTA-007` |
| Hero takes lethal damage | No survival effect resolves | Control stops, kill rewards resolve and a respawn timer begins | reversible death cost | `DOTA-003`, `DOTA-006`, `DOTA-007` |
| Dead hero meets current cost and cooldown gates | Pay buyback | Gold is deducted and the hero respawns immediately; buyback enters cooldown | economy-for-time recovery | `DOTA-006`, `DOTA-007` |
| Allied vision leaves a terrain region or an enemy becomes undetected | Move away / lose detection | Current hostile state disappears into fog or invisibility until allied vision/detection returns | partial team information | `DOTA-005`, `DOTA-007` |
| Lane tower is destroyed and its barracks become attackable | Destroy a barracks | Later opposing lane waves receive the corresponding upgraded creep state | persistent lane pressure | `DOTA-004`, `DOTA-007` |
| Required base protection is gone and the enemy Ancient is exposed | Deal lethal building damage | Ancient is destroyed and the match ends immediately for both teams | terminal team objective | `DOTA-006`, `DOTA-007` |

## Strategic and experiential structure

- Local decision: position for a last hit without accepting a bad trade; select
  the correct target and cast form; preserve mana/cooldown; reveal or deny vision.
- Medium-term planning: allocate farm among five heroes, complete item timings,
  move wards and courier safely, trade objectives for map control and preserve buyback.
- Long-term structure: draft complementary heroes, turn lane economy into tower
  and barracks pressure, use Roshan or pickoffs to cross high-ground protection,
  then expose and destroy the Ancient.
- Common heuristics: secure last hits, deny unsafe information, fight around
  vision and cooldown advantages, avoid feeding streak rewards, push lanes
  before taking a distant objective and keep a retreat or buyback reserve.
- Failure attribution: health, mana, cooldown, gold, experience, item and
  objective states are inspectable; hidden enemy movement and simultaneous
  team choice keep tactical causality partially inferred.
- Claim IDs: `DOTA-002`–`DOTA-006`.

## Replay and variation

- What changes: ten hero selections/facets, player plans, lane allocation,
  item and talent builds, neutral drops, fights, ward placement and objective order.
- Randomness: roster interactions and human choice dominate; attack variance,
  neutral drops and some spawn details add bounded uncertainty.
- Multiple viable strategies: lane pressure, split push, pickoff, five-player
  fight, Roshan timing and high-ground siege exchange economy, information and time.
- Typical replay motive: master a changing roster and patch through coordinated
  execution, build adaptation and opponent inference.
- Claim IDs: `DOTA-001`–`DOTA-006`.

## Adjacent systems and history

- Direct predecessors: Warcraft III custom map Defense of the Ancients and the
  wider lane-based action-strategy lineage.
- Variants: Ranked adds rating/role constraints; Turbo accelerates economy and
  weakens several timings; Captains Mode changes draft authority.
- Similar games: League of Legends, Heroes of the Storm, Smite and other MOBAs.
- Important differences: this scope centres deny-capable lane economy, courier
  logistics, buyback, destructible barracks pressure and fog-limited 5v5 control.
- Claim IDs: `DOTA-001`–`DOTA-006`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-130`, `ACT-187`–`ACT-193` | hero-specific ability shapes are parameters |
| System Behaviour | `SYS-045`, `SYS-051`, `SYS-215`, `SYS-297`–`SYS-306` | hero, item and neutral rosters are parameters |
| Constraint | `CON-268`–`CON-275` | exact costs, ranges and cooldowns are parameters |
| Information | `INF-118`–`INF-116` | HUD placement and cosmetic effects are excluded |
| Objective | `OBJ-072` | team side is a parameter |
| Time | `TIM-003` | live timers are parameters |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-130,ACT-187,ACT-188,ACT-189,ACT-190,ACT-191,ACT-192,ACT-193; SYS-045,SYS-051,SYS-215,SYS-297,SYS-298,SYS-299,SYS-300,SYS-301,SYS-302,SYS-303,SYS-304,SYS-305,SYS-306; CON-268,CON-269,CON-270,CON-271,CON-272,CON-273,CON-274,CON-275; INF-118,INF-119,INF-120,INF-116; OBJ-072; TIM-003`.
- Indexed games scanned: 137 (`GAME-0001`–`GAME-0137`).
- Indexed combinations scanned: 135 (`COMB-0001`–`COMB-0135`).
- Exact genome matches: none.
- Near match: Bad North: Jotunn Edition (`GAME-0027`) at
  `3 / 44 = 0.068182`, sharing autonomous locomotion/engagement and live time.
- Supported prior combination subsets: none.
- Scan date: 2026-08-21.

### Exhaustive prior-game similarity scan

- GAME-0001: 0 / 49 = 0.000000; GAME-0002: 0 / 42 = 0.000000; GAME-0003: 0 / 44 = 0.000000; GAME-0004: 1 / 49 = 0.020408.
- GAME-0005: 0 / 42 = 0.000000; GAME-0006: 0 / 44 = 0.000000; GAME-0007: 0 / 43 = 0.000000; GAME-0008: 0 / 42 = 0.000000.
- GAME-0009: 0 / 51 = 0.000000; GAME-0010: 0 / 44 = 0.000000; GAME-0011: 0 / 48 = 0.000000; GAME-0012: 0 / 44 = 0.000000.
- GAME-0013: 0 / 48 = 0.000000; GAME-0014: 0 / 50 = 0.000000; GAME-0015: 0 / 49 = 0.000000; GAME-0016: 1 / 49 = 0.020408.
- GAME-0017: 0 / 48 = 0.000000; GAME-0018: 1 / 53 = 0.018868; GAME-0019: 0 / 45 = 0.000000; GAME-0020: 0 / 49 = 0.000000.
- GAME-0021: 1 / 43 = 0.023256; GAME-0022: 0 / 47 = 0.000000; GAME-0023: 0 / 45 = 0.000000; GAME-0024: 1 / 46 = 0.021739.
- GAME-0025: 2 / 44 = 0.045455; GAME-0026: 1 / 46 = 0.021739; GAME-0027: 3 / 44 = 0.068182; GAME-0028: 3 / 49 = 0.061224.
- GAME-0029: 2 / 45 = 0.044444; GAME-0030: 2 / 47 = 0.042553; GAME-0031: 1 / 45 = 0.022222; GAME-0032: 0 / 46 = 0.000000.
- GAME-0033: 1 / 47 = 0.021277; GAME-0034: 2 / 47 = 0.042553; GAME-0035: 2 / 51 = 0.039216; GAME-0036: 0 / 47 = 0.000000.
- GAME-0037: 0 / 44 = 0.000000; GAME-0038: 1 / 50 = 0.020000; GAME-0039: 0 / 44 = 0.000000; GAME-0040: 0 / 43 = 0.000000.
- GAME-0041: 1 / 45 = 0.022222; GAME-0042: 0 / 44 = 0.000000; GAME-0043: 0 / 49 = 0.000000; GAME-0044: 0 / 45 = 0.000000.
- GAME-0045: 0 / 49 = 0.000000; GAME-0046: 0 / 45 = 0.000000; GAME-0047: 0 / 49 = 0.000000; GAME-0048: 0 / 49 = 0.000000.
- GAME-0049: 0 / 44 = 0.000000; GAME-0050: 0 / 50 = 0.000000; GAME-0051: 1 / 50 = 0.020000; GAME-0052: 0 / 45 = 0.000000.
- GAME-0053: 0 / 44 = 0.000000; GAME-0054: 0 / 46 = 0.000000; GAME-0055: 0 / 45 = 0.000000; GAME-0056: 0 / 43 = 0.000000.
- GAME-0057: 0 / 43 = 0.000000; GAME-0058: 0 / 44 = 0.000000; GAME-0059: 0 / 42 = 0.000000; GAME-0060: 0 / 42 = 0.000000.
- GAME-0061: 0 / 45 = 0.000000; GAME-0062: 0 / 43 = 0.000000; GAME-0063: 0 / 42 = 0.000000; GAME-0064: 0 / 40 = 0.000000.
- GAME-0065: 0 / 42 = 0.000000; GAME-0066: 0 / 45 = 0.000000; GAME-0067: 0 / 43 = 0.000000; GAME-0068: 0 / 43 = 0.000000.
- GAME-0069: 0 / 43 = 0.000000; GAME-0070: 0 / 43 = 0.000000; GAME-0071: 0 / 42 = 0.000000; GAME-0072: 0 / 43 = 0.000000.
- GAME-0073: 0 / 42 = 0.000000; GAME-0074: 0 / 44 = 0.000000; GAME-0075: 0 / 44 = 0.000000; GAME-0076: 0 / 42 = 0.000000.
- GAME-0077: 0 / 42 = 0.000000; GAME-0078: 0 / 42 = 0.000000; GAME-0079: 0 / 42 = 0.000000; GAME-0080: 0 / 42 = 0.000000.
- GAME-0081: 0 / 43 = 0.000000; GAME-0082: 0 / 43 = 0.000000; GAME-0083: 0 / 43 = 0.000000; GAME-0084: 0 / 45 = 0.000000.
- GAME-0085: 0 / 46 = 0.000000; GAME-0086: 0 / 48 = 0.000000; GAME-0087: 1 / 44 = 0.022727; GAME-0088: 0 / 44 = 0.000000.
- GAME-0089: 0 / 44 = 0.000000; GAME-0090: 0 / 50 = 0.000000; GAME-0091: 1 / 43 = 0.023256; GAME-0092: 2 / 43 = 0.046512.
- GAME-0093: 0 / 44 = 0.000000; GAME-0094: 1 / 44 = 0.022727; GAME-0095: 1 / 46 = 0.021739; GAME-0096: 1 / 44 = 0.022727.
- GAME-0097: 1 / 42 = 0.023810; GAME-0098: 1 / 41 = 0.024390; GAME-0099: 0 / 43 = 0.000000; GAME-0100: 1 / 45 = 0.022222.
- GAME-0101: 0 / 45 = 0.000000; GAME-0102: 0 / 42 = 0.000000; GAME-0103: 0 / 44 = 0.000000; GAME-0104: 0 / 44 = 0.000000.
- GAME-0105: 1 / 44 = 0.022727; GAME-0106: 0 / 42 = 0.000000; GAME-0107: 0 / 43 = 0.000000; GAME-0108: 0 / 45 = 0.000000.
- GAME-0109: 0 / 51 = 0.000000; GAME-0110: 1 / 42 = 0.023810; GAME-0111: 0 / 42 = 0.000000; GAME-0112: 1 / 42 = 0.023810.
- GAME-0113: 1 / 48 = 0.020833; GAME-0114: 1 / 41 = 0.024390; GAME-0115: 0 / 41 = 0.000000; GAME-0116: 1 / 40 = 0.025000.
- GAME-0117: 0 / 43 = 0.000000; GAME-0118: 1 / 50 = 0.020000; GAME-0119: 3 / 55 = 0.054545; GAME-0120: 1 / 63 = 0.015873.
- GAME-0121: 1 / 57 = 0.017544; GAME-0122: 1 / 49 = 0.020408; GAME-0123: 1 / 72 = 0.013889; GAME-0124: 3 / 79 = 0.037975.
- GAME-0125: 2 / 75 = 0.026667; GAME-0126: 3 / 75 = 0.040000; GAME-0127: 3 / 80 = 0.037500; GAME-0128: 1 / 50 = 0.020000.
- GAME-0129: 2 / 68 = 0.029412; GAME-0130: 2 / 86 = 0.023256; GAME-0131: 3 / 78 = 0.038462; GAME-0132: 2 / 84 = 0.023810.
- GAME-0133: 1 / 79 = 0.012658; GAME-0134: 1 / 85 = 0.011765; GAME-0135: 1 / 82 = 0.012195; GAME-0136: 2 / 93 = 0.021505.
- GAME-0137: 3 / 62 = 0.048387.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Bad North: Jotunn Edition (`GAME-0027`) | `SYS-045`, `SYS-051`, `TIM-003` | island-by-island squad landing defence versus persistent hero builds, fog-limited three-lane economy, respawn/buyback and ordered base siege | nearest at `3 / 44 = 0.068182` |

- New genes: `ACT-188`–`ACT-193`, `SYS-297`–`SYS-306`, `CON-268`–`CON-275`,
  `INF-118`–`INF-120`, `OBJ-072`.
- Classification result: `New gene` and a new combination of reused/new genes.
- Evidence and reasoning: seven existing genes preserve shop purchase, live team
  cue, autonomous movement/engagement, direct combat and real-time boundaries;
  the new records isolate MOBA draft, lane economy, builds, fog, buyback and siege.

### Registry normalisation 006 score corrections

These recomputed values supersede the pre-normalisation fractions above:

- `GAME-0132`: `3 / 83 = 0.036145`
- `GAME-0137`: `5 / 60 = 0.083333`
- Current prior-corpus near match after normalisation 006: `GAME-0137`.

## Taxonomy impact

- Registry changes after normalisation: 28 bounded active genes and added Dota
  2 evidence to six reused records; `TIM-003` needs no wording change.
- Taxonomy-change record: `TAXONOMY_CHANGE_014`.
- Candidate terms affected: carry/support role, gank, deny, split push, high
  ground and power spike are strategies or parameters, not independent genes.

## Negative results

- Negative results: `ACT-008` was not reused because Dota movement is a
  destination command with autonomous pathing, not direct local locomotion.
- `INF-115` was not reused because its first-person audiovisual boundary does
  not fit shared top-down fog and ward vision; `INF-116` is reused only for the
  live team/clock/objective HUD boundary.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] All Pick поєднує fixed five-hero teams із
  match-local gold, XP, abilities, talents, items і courier (`DOTA-001`–`DOTA-003`).
- [Confirmed | Corroborated | High] Shared fog, respawn/buyback та ordered
  building protection переводять lane pressure в Ancient victory (`DOTA-004`–`DOTA-006`).

## Нові гени

- [Observation | Corroborated | High] Додано 28 genes для hero draft/commands,
  abilities/builds, courier/buyback, lane economy, structures, fog і Ancient victory.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0136` — fog-limited lane economy
  into Ancient destruction.

## Зміни таксономії

- [Observation | Direct | High] Змін таксономії немає.

## Open questions

- Re-check patch-specific numbers if Valve replaces `7.41e`; the genome stores
  causal boundaries, not volatile balance values.
- Hero-specific exceptions remain roster parameters unless a later analysis
  demonstrates a reusable causal boundary absent from this structural scope.

## Нові питання

- Які survival/capture genes справді перенесе Palworld, не змішуючи server
  settings, co-op authority і creature-specific roster parameters?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] `GAME-0139` Palworld.
- Optimisation criterion: continue the authorised demand-led Goal queue.
- Expected information gain: creature capture, delegated labour, survival,
  base production and open-world boss progression.
- Backlog impact: preserves `GAME-0140` PUBG: BATTLEGROUNDS and later units.

## Чому саме вона

- [Hypothesis | Limited | Medium] Palworld tests whether a recognisable
  open-world survival/capture loop bridges existing autonomous-agent and
  production families without inheriting Dota's fixed-team lane structure.
