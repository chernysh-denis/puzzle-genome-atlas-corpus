---
game_id: GAME-0120
slug: slay-the-spire
game_title: Slay the Spire
analysis_status: reviewed
reviewed: 2026-08-18
combination_ids:
  - COMB-0119
gene_ids:
  action:
    - ACT-125
    - ACT-126
    - ACT-127
    - ACT-128
    - ACT-129
    - ACT-130
    - ACT-131
  system:
    - SYS-004
    - SYS-087
    - SYS-163
    - SYS-164
    - SYS-165
    - SYS-166
    - SYS-167
    - SYS-168
  constraint:
    - CON-043
    - CON-094
    - CON-174
    - CON-175
    - CON-176
    - CON-177
    - CON-178
  information:
    - INF-002
    - INF-003
    - INF-061
    - INF-062
  objective:
    - OBJ-029
    - OBJ-055
  time:
    - TIM-005
---

# Game: Slay the Spire

## Analysis scope

- Version / ruleset: PC main-branch version 2.3, standard single-player
  Ascension 0 climb as the Ironclad from Neow through ordinary victory over the
  Act 3 boss.
- Included: run-seeded Acts 1–3; revealed branching maps; combat, elite,
  unknown, treasure, shop, rest and boss nodes; persistent health, deck, gold,
  relics and potions; card draw, discard, exhaust and reshuffle; Energy, Block,
  enemy intents, card and potion use; post-combat rewards; merchant purchases
  and removal; rest and Smith choices; act bosses and ordinary Act 3 victory.
- Excluded: the optional unlocked Act 4 and Heart; Ascension modifiers; Daily
  Climb, Custom and Endless modes; seeded-run comparison, scoring and
  achievements; mods; other characters' exclusive Orb, stance and poison
  subsystems; profile unlock progression; platform-specific input details.
- Direct-play status: prior player familiarity informed boundary review, but no
  fresh instrumented run was recorded. Primary developer material establishes
  the generated climb, reward-driven deck construction and build strategy;
  current mechanics and map transitions are corroborated by the maintained
  rules reference.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `STS-001` | During a player phase, held cards may be played in flexible order when their Energy and target requirements are satisfied | Confirmed | Corroborated | High | P2, S1 |
| `STS-002` | End Turn discards ordinary unretained cards, resolves end-turn effects, lets enemies execute their intents and starts a new hand with refreshed base Energy | Confirmed | Corroborated | High | S1, S3 |
| `STS-003` | A depleted draw pile is replenished by shuffling the discard pile, while Exhaust normally removes a card for the current combat | Confirmed | Corroborated | High | S1 |
| `STS-004` | Enemy intent icons disclose the next action category and attack magnitude but may withhold exact buff, debuff or special details | Confirmed | Corroborated | High | S1, S3 |
| `STS-005` | Block absorbs ordinary incoming damage before health and ordinarily clears at the next player-turn boundary | Confirmed | Corroborated | High | S1 |
| `STS-006` | Defeating a combat's finite hostile set yields run rewards that may include gold, a potion and one optional card from a bounded offer | Confirmed | Corroborated | High | P1, P2, S2 |
| `STS-007` | Each act uses a generated finite branching route whose visible node categories and connections constrain the next choice | Confirmed | Corroborated | High | P1, P2, S2 |
| `STS-008` | Shops exchange persistent gold for cards, relics, potions or card removal, while rest sites ordinarily trade healing against one card upgrade | Confirmed | Corroborated | High | S2 |
| `STS-009` | Health, deck mutations, gold, relics and potion inventory persist between resolved nodes until the run ends | Confirmed | Corroborated | High | P1, P2, S1, S2 |
| `STS-010` | Relics apply persistent automatic effects at their declared run and combat triggers | Confirmed | Corroborated | High | P1, S1 |
| `STS-011` | Ordinary victory requires surviving three acts and defeating the Act 3 boss; the unlocked fourth act is optional and outside scope | Confirmed | Corroborated | High | P3, S1 |
| `STS-012` | Run seed, generated route, encounters and reward offers vary, forcing deck and path adaptation rather than one invariant build | Confirmed | Corroborated | High | P1, P2, P3, S2 |

## Basic data

- Release / origin: Mega Crit developed and published Slay the Spire; version
  1.0 left Early Access on 23 January 2019 and the fourth character arrived in
  the free 2.0 update. The scoped PC main branch is version 2.3.
- Platform or physical form: single-player digital turn-based deckbuilding
  roguelike on desktop, console and mobile platforms.
- Puzzle family: persistent deck construction; telegraphed card combat;
  branching risk-route selection; multi-encounter resource attrition.
- Primary and creator sources: **[P1]** [official Steam product page](https://store.steampowered.com/app/646570/Slay_the_Spire/),
  documenting dynamic deckbuilding, changing routes, cards, relics, enemies and
  bosses; **[P2]** [Mega Crit designer's official PlayStation guide](https://blog.playstation.com/2019/05/13/how-to-come-out-on-top-in-slay-the-spire-out-may-21-on-ps4/),
  documenting generated runs, post-combat card choice, deck consistency,
  upgrades, potions and build interactions; **[P3]** [official 1.0 release
  record](https://store.steampowered.com/news/posts/?appids=646570&enddate=1568160786&feed=steam_community_announcements),
  documenting the Final Act, Ascensions, seeded runs and the shipped content
  boundary; **[P4]** [official 2.0 update record](https://store.steampowered.com/news/posts/?appids=646570&enddate=1579549216&feed=steam_community_announcements),
  documenting the fourth character and versioned content change.
- Reproducible rules references: **[S1]** [Slay the Spire Wiki —
  Mechanics](https://slaythespire.wiki.gg/wiki/Mechanics), for turn order,
  Energy, draw/discard recycling, card and potion timing, intents and Act 4
  boundary; **[S2]** [Slay the Spire Wiki — Map
  Locations](https://slaythespire.wiki.gg/wiki/Map_Locations), for node
  categories, rewards, merchant and rest-site transitions; **[S3]** [Slay the
  Spire Wiki — Intent](https://slaythespire.wiki.gg/wiki/Intent), for disclosed
  and deliberately categorical hostile information.
- Claim IDs: `STS-001`–`STS-012`.

## Mechanical decomposition

### Action Genes

- `ACT-125` plays one held effect card; `ACT-126` ends the current player
  combat phase; `ACT-127` chooses one reachable revealed route node; `ACT-128`
  accepts or skips one offered persistent-deck card; `ACT-129` upgrades,
  removes or transforms one persistent deck card; `ACT-130` purchases one
  offered run asset or service; `ACT-131` consumes one held potion.
- Candidate genes: none.
- Parameters: card, target, Energy cost, route node, reward offer, persistent
  mutation, merchant price, potion timing and event-specific option.
- Claim IDs: `STS-001`, `STS-006`–`STS-009`.

### System Behaviour Genes

- `SYS-004` selects seeded route, encounter and reward outcomes; `SYS-087`
  turns over the hand and recycles discard; `SYS-163` resolves played card
  text; `SYS-164` executes telegraphed hostile intents; `SYS-165` applies Block
  before persistent health loss; `SYS-166` triggers relic effects; `SYS-167`
  carries mutable run state across nodes; `SYS-168` generates each finite
  branching act route.
- Resolution order: accept legal card or potion use and finish its effects;
  when End Turn is chosen, resolve end-turn effects, discard ordinary held
  cards, execute surviving enemies left to right, clear ordinary Block, refresh
  Energy, draw and apply start-turn triggers; after combat, resolve rewards and
  persist the resulting run state before route choice.
- Claim IDs: `STS-001`–`STS-012`.

### Constraint Genes

- `CON-043` bounds the visible hand and one-card commit; `CON-094` shares and
  renews the Energy budget; `CON-174` gates card play by cost and target;
  `CON-175` makes persistent health depletion terminal; `CON-176` restricts
  progression to connected successor nodes; `CON-177` bounds potion slots;
  `CON-178` makes persistent deck membership define later combat draws.
- Scarce strategic resources: health, Energy, draw access, deck consistency,
  gold, potion slots, route access and safe opportunities to heal or upgrade.
- Claim IDs: `STS-001`–`STS-009`, `STS-011`.

### Information Genes

- `INF-002` withholds future random encounter and reward identities; `INF-003`
  conceals the fixed current combat draw order; `INF-061` previews hostile
  intent category and attack magnitude; `INF-062` reveals route categories and
  connections while withholding node-specific contents.
- Candidate genes: none.
- Claim IDs: `STS-002`–`STS-004`, `STS-006`, `STS-007`, `STS-012`.

### Objective Genes

- `OBJ-029` clears each finite hostile encounter; `OBJ-055` completes the
  continuous three-act climb by defeating the Act 3 boss.
- Success, evaluation and failure: every ordinary combat requires all enemies
  defeated before player health reaches zero; health remains at risk across
  nodes, and zero ends the run. Defeating the Act 3 boss produces ordinary
  victory in scope; score and optional Act 4 access are excluded.
- Claim IDs: `STS-006`, `STS-009`, `STS-011`.

### Time Genes

- `TIM-005` provides a self-paced player planning phase with several flexible
  card and potion actions before explicit commitment to hostile resolution.
- Candidate genes: none.
- Claim IDs: `STS-001`–`STS-005`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Three Energy, Strike and Defend are held, and one enemy intends to attack for six | Play Defend, then Strike | Energy falls by two; Block rises; the target loses Strike damage; both cards enter discard after their text resolves | card choice, cost, target and effect resolution are separate rules | `STS-001`, `STS-005` |
| Five Block remains when a six-damage attack resolves | End Turn | Block absorbs five and persistent health loses one | temporary defence mediates rather than replaces run health | `STS-002`, `STS-005` |
| Draw pile is empty and the next player turn must draw five | End Turn and complete the enemy phase | discard is shuffled into a new concealed draw pile, then the new hand is drawn | persistent deck membership and concealed draw order coexist | `STS-002`, `STS-003` |
| A normal combat ends with the player alive | Defeat the final enemy | combat ends and a bounded reward screen offers gold and an optional one-of-three card addition | clearance feeds persistent deck construction | `STS-006` |
| The map shows an elite branch and a safer combat branch | Choose the connected elite node | the run enters that elite encounter; unconnected next-floor nodes remain unavailable | visible path choice controls risk and reward access | `STS-007` |
| Current health is low at a rest site and one key card is unupgraded | Choose Rest or Smith | Rest restores health; Smith persistently upgrades one eligible card; only the chosen service resolves | survival and deck strength compete at the same route resource | `STS-008`, `STS-009` |
| A merchant offers a card and removal service while gold is limited | Purchase one option | gold decreases and the acquired card enters the deck, or the selected existing card is removed | economy mutates later combat draw supply | `STS-008`, `STS-009` |
| The Act 3 boss loses its final health while the Ironclad remains alive | Resolve the final damaging effect | ordinary three-act victory is recorded; optional Act 4 is outside the scoped objective | encounter clearance and run completion are nested objectives | `STS-011` |

## Strategic and experiential structure

- Local decision: convert the visible hand and Energy into enough damage,
  Block or scaling against the previewed hostile intent without exhausting
  future options.
- Medium-term planning: accept only cards that improve the current deck's
  draw quality and synergies, preserve potions for dangerous nodes and weigh
  healing against upgrades.
- Long-term structure: choose a route whose elites, shops, rests and unknown
  events produce enough power to survive increasingly demanding bosses while
  persistent health attrition remains recoverable.
- Common heuristics: remove weak starter cards, value reliable damage early,
  add defence and scaling before later bosses, avoid unnecessary card bloat,
  and inspect the route before committing to a reward.
- Failure attribution: current hand, Energy, deck list, route, health and
  attack magnitudes are inspectable, but hidden draw order and future offers
  make exact outcomes uncertain.
- Player-trust factors: every selected card exposes its text and cost; the map
  shows reachable categories; intent icons make imminent attack magnitude
  legible while honestly keeping some special effects categorical.
- Claim IDs: `STS-001`–`STS-012`.

## Replay and variation

- What changes between sessions: act map, node contents, enemies, bosses,
  offered cards, relics, potions, events and the resulting deck route.
- Randomness or procedural generation: a run seed governs generated maps and
  many offers; combat draw order is seeded but concealed after shuffle.
- Multiple viable strategies: yes; Ironclad decks may emphasise Strength,
  Block, Exhaust, status interactions, self-damage or smaller combo structures.
- Typical replay motive: discover a different build, route and relic
  interaction or later apply excluded Ascension modifiers.
- Claim IDs: `STS-006`–`STS-012`.

## Adjacent systems and history

- Direct predecessors: tabletop deckbuilding and digital roguelike run
  structures; Mega Crit explicitly describes the design as a fusion of card
  games and roguelikes.
- Variants: Ascension adds cumulative difficulty rules; Act 4 adds optional
  key collection and the Heart; Daily, Custom and Endless alter the run. They
  remain excluded.
- Similar games: Balatro, Fights in Tight Spaces, Monster Train, Wildfrost and
  Inscryption.
- Important differences: unlike Balatro's scoped one-Blind pattern scoring,
  Slay the Spire persistently edits the deck between encounters and carries
  health through a visible branching route. Unlike Fights in Tight Spaces, its
  card targeting has no positional board and hostile intent is partly
  categorical rather than an exact redirectable attack geometry.
- Claim IDs: `STS-001`–`STS-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-125`–`ACT-131` | card, target, node, reward, deck mutation, purchase and potion parameters |
| System Behaviour | `SYS-004`, `SYS-087`, `SYS-163`–`SYS-168` | seed, order, trigger and offer parameters |
| Constraint | `CON-043`, `CON-094`, `CON-174`–`CON-178` | Energy, health, route, slot and deck parameters |
| Information | `INF-002`, `INF-003`, `INF-061`, `INF-062` | intent detail, map disclosure and concealed order |
| Objective | `OBJ-029`, `OBJ-055` | hostile set, act and boss parameters |
| Time | `TIM-005` | actions per phase and hostile order |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-125,ACT-126,ACT-127,ACT-128,ACT-129,ACT-130,ACT-131; SYS-004,SYS-087,SYS-163,SYS-164,SYS-165,SYS-166,SYS-167,SYS-168; CON-043,CON-094,CON-174,CON-175,CON-176,CON-177,CON-178; INF-002,INF-003,INF-061,INF-062; OBJ-029,OBJ-055; TIM-005`.
- Indexed games scanned: 120, including this record.
- Indexed combinations scanned: 119.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0047` at `6 / 37 = 0.162162`.
- Supported combination subsets: `COMB-0119`.
- Scan date: 2026-08-18.

### Full prior-game Jaccard scan

- `GAME-0001`: `2 / 41 = 0.048780`; `GAME-0002`: `0 / 36 = 0.000000`; `GAME-0003`: `1 / 37 = 0.027027`; `GAME-0004`: `1 / 43 = 0.023256`.
- `GAME-0005`: `0 / 36 = 0.000000`; `GAME-0006`: `0 / 38 = 0.000000`; `GAME-0007`: `0 / 37 = 0.000000`; `GAME-0008`: `0 / 36 = 0.000000`.
- `GAME-0009`: `2 / 43 = 0.046512`; `GAME-0010`: `0 / 38 = 0.000000`; `GAME-0011`: `0 / 42 = 0.000000`; `GAME-0012`: `0 / 38 = 0.000000`.
- `GAME-0013`: `0 / 42 = 0.000000`; `GAME-0014`: `1 / 43 = 0.023256`; `GAME-0015`: `1 / 42 = 0.023810`; `GAME-0016`: `1 / 43 = 0.023256`.
- `GAME-0017`: `2 / 40 = 0.050000`; `GAME-0018`: `2 / 46 = 0.043478`; `GAME-0019`: `0 / 39 = 0.000000`; `GAME-0020`: `1 / 42 = 0.023810`.
- `GAME-0021`: `0 / 38 = 0.000000`; `GAME-0022`: `0 / 41 = 0.000000`; `GAME-0023`: `0 / 39 = 0.000000`; `GAME-0024`: `0 / 41 = 0.000000`.
- `GAME-0025`: `0 / 40 = 0.000000`; `GAME-0026`: `0 / 41 = 0.000000`; `GAME-0027`: `0 / 41 = 0.000000`; `GAME-0028`: `2 / 44 = 0.045455`.
- `GAME-0029`: `0 / 41 = 0.000000`; `GAME-0030`: `0 / 43 = 0.000000`; `GAME-0031`: `0 / 40 = 0.000000`; `GAME-0032`: `0 / 40 = 0.000000`.
- `GAME-0033`: `0 / 42 = 0.000000`; `GAME-0034`: `0 / 43 = 0.000000`; `GAME-0035`: `0 / 47 = 0.000000`; `GAME-0036`: `0 / 41 = 0.000000`.
- `GAME-0037`: `0 / 38 = 0.000000`; `GAME-0038`: `0 / 45 = 0.000000`; `GAME-0039`: `0 / 38 = 0.000000`; `GAME-0040`: `0 / 37 = 0.000000`.
- `GAME-0041`: `0 / 40 = 0.000000`; `GAME-0042`: `0 / 38 = 0.000000`; `GAME-0043`: `0 / 43 = 0.000000`; `GAME-0044`: `0 / 39 = 0.000000`.
- `GAME-0045`: `0 / 43 = 0.000000`; `GAME-0046`: `0 / 39 = 0.000000`; `GAME-0047`: `6 / 37 = 0.162162`; `GAME-0048`: `1 / 42 = 0.023810`.
- `GAME-0049`: `1 / 37 = 0.027027`; `GAME-0050`: `1 / 43 = 0.023256`; `GAME-0051`: `2 / 43 = 0.046512`; `GAME-0052`: `0 / 39 = 0.000000`.
- `GAME-0053`: `0 / 38 = 0.000000`; `GAME-0054`: `0 / 40 = 0.000000`; `GAME-0055`: `0 / 39 = 0.000000`; `GAME-0056`: `0 / 37 = 0.000000`.
- `GAME-0057`: `0 / 37 = 0.000000`; `GAME-0058`: `0 / 38 = 0.000000`; `GAME-0059`: `0 / 36 = 0.000000`; `GAME-0060`: `0 / 36 = 0.000000`.
- `GAME-0061`: `0 / 39 = 0.000000`; `GAME-0062`: `0 / 37 = 0.000000`; `GAME-0063`: `0 / 36 = 0.000000`; `GAME-0064`: `0 / 34 = 0.000000`.
- `GAME-0065`: `1 / 35 = 0.028571`; `GAME-0066`: `1 / 38 = 0.026316`; `GAME-0067`: `2 / 35 = 0.057143`; `GAME-0068`: `1 / 36 = 0.027778`.
- `GAME-0069`: `0 / 37 = 0.000000`; `GAME-0070`: `0 / 37 = 0.000000`; `GAME-0071`: `0 / 36 = 0.000000`; `GAME-0072`: `0 / 37 = 0.000000`.
- `GAME-0073`: `0 / 36 = 0.000000`; `GAME-0074`: `0 / 38 = 0.000000`; `GAME-0075`: `0 / 38 = 0.000000`; `GAME-0076`: `0 / 36 = 0.000000`.
- `GAME-0077`: `0 / 36 = 0.000000`; `GAME-0078`: `0 / 36 = 0.000000`; `GAME-0079`: `0 / 36 = 0.000000`; `GAME-0080`: `0 / 36 = 0.000000`.
- `GAME-0081`: `0 / 37 = 0.000000`; `GAME-0082`: `0 / 37 = 0.000000`; `GAME-0083`: `0 / 37 = 0.000000`; `GAME-0084`: `0 / 39 = 0.000000`.
- `GAME-0085`: `1 / 39 = 0.025641`; `GAME-0086`: `0 / 42 = 0.000000`; `GAME-0087`: `0 / 39 = 0.000000`; `GAME-0088`: `0 / 38 = 0.000000`.
- `GAME-0089`: `0 / 38 = 0.000000`; `GAME-0090`: `0 / 44 = 0.000000`; `GAME-0091`: `0 / 38 = 0.000000`; `GAME-0092`: `0 / 39 = 0.000000`.
- `GAME-0093`: `0 / 38 = 0.000000`; `GAME-0094`: `0 / 39 = 0.000000`; `GAME-0095`: `0 / 41 = 0.000000`; `GAME-0096`: `0 / 39 = 0.000000`.
- `GAME-0097`: `0 / 37 = 0.000000`; `GAME-0098`: `0 / 36 = 0.000000`; `GAME-0099`: `0 / 37 = 0.000000`; `GAME-0100`: `0 / 40 = 0.000000`.
- `GAME-0101`: `0 / 39 = 0.000000`; `GAME-0102`: `0 / 36 = 0.000000`; `GAME-0103`: `0 / 38 = 0.000000`; `GAME-0104`: `0 / 38 = 0.000000`.
- `GAME-0105`: `0 / 39 = 0.000000`; `GAME-0106`: `0 / 36 = 0.000000`; `GAME-0107`: `0 / 37 = 0.000000`; `GAME-0108`: `0 / 39 = 0.000000`.
- `GAME-0109`: `2 / 43 = 0.046512`; `GAME-0110`: `1 / 36 = 0.027778`; `GAME-0111`: `0 / 36 = 0.000000`; `GAME-0112`: `0 / 37 = 0.000000`.
- `GAME-0113`: `0 / 43 = 0.000000`; `GAME-0114`: `0 / 36 = 0.000000`; `GAME-0115`: `0 / 35 = 0.000000`; `GAME-0116`: `0 / 35 = 0.000000`.
- `GAME-0117`: `0 / 37 = 0.000000`; `GAME-0118`: `0 / 45 = 0.000000`; `GAME-0119`: `0 / 52 = 0.000000`.

Near matches are selected by the canonical formula. Detailed comparison is
limited to those records; ties are retained.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0047` | `SYS-087`, `CON-043`, `CON-094`, `INF-003`, `OBJ-029`, `TIM-005` | Slay the Spire couples card combat to persistent health, deck mutation and a generated three-act route | Unique near match |

- New genes: `ACT-125`–`ACT-131`, `SYS-163`–`SYS-168`, `CON-174`–`CON-178`,
  `INF-061`–`INF-062`, `OBJ-055`.
- Classification result: new combination of reused card-hand, randomness,
  information, encounter-objective and phase-timing genes with new persistent
  deckbuilding-run boundaries.
- Evidence and reasoning: complete signature comparison distinguishes the
  run-level deck mutation and health attrition from both one-Blind score
  construction and spatial card tactics.

## Combination record

- Registered [`COMB-0119`](../../combinations/COMB-0119.md), a proper
  eighteen-gene subset centred on persistent deck growth feeding previewed
  turn-based combat across one terminal-health climb.
- Route generation, merchant economy, potions, relic triggers and partial
  future-node information remain outside that stricter interaction pattern.

## Taxonomy impact

- Existing six-type architecture remains sufficient. New genes separate
  player card choice, run-persistent state, hostile intent, route access and
  survival rather than collapsing the entire genre into one deckbuilder label.
- Taxonomy-change record: none.
- Candidate terms affected: none.

## Negative results

- `ACT-021` is rejected: Slay the Spire ordinarily plays one effect card, not a
  bounded multi-card subset for pattern evaluation.
- `ACT-061` is rejected: card use has optional combatant targeting but no
  spatial cell, direction or displacement geometry.
- `SYS-019` and `INF-009` are rejected: intents do not disclose exact spatial
  target positions or every buff and debuff detail, and cannot be redirected
  through occupancy.
- `INF-001` is rejected because combat draw order and future node contents are
  decision-relevant but concealed.
- No separate negative-result record or taxonomy correction is required.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] The same persistent deck and health state
  connect generated route choice, combat, rewards and services across Acts
  1–3 (`STS-001`–`STS-012`).

## Нові гени

- [Observation | Corroborated | High] `ACT-125`–`ACT-131`, `SYS-163`–`SYS-168`,
  `CON-174`–`CON-178`, `INF-061`–`INF-062`, `OBJ-055`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0119`.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Which independent deckbuilder preserves the same persistent combat-deck loop
  while changing route topology, hostile preview or between-node economy?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] Cities: Skylines.
- Optimisation criterion: return to the approved city-simulation constellation
  and test a close, user-legible SimCity relationship after a distant card run.
- Expected information gain: determine which municipal growth, service,
  transport and budget boundaries recur under a newer simulation model.
- Backlog impact: continues the approved editorial batch as `GAME-0121`.

## Чому саме вона

- [Hypothesis | Corroborated | High] Cities: Skylines should create the first
  high-overlap same-constellation comparison in this batch and test whether the
  SimCity 4 municipal combination generalises without erasing meaningful rule
  differences.
