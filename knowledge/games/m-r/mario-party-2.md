---
game_id: GAME-0392
slug: mario-party-2
game_title: Mario Party 2
analysis_status: reviewed
reviewed: 2026-09-24
combination_ids: []
gene_ids:
  action:
    - ACT-130
    - ACT-131
    - ACT-530
  system:
    - SYS-004
    - SYS-1050
    - SYS-1051
    - SYS-1052
    - SYS-1053
    - SYS-1054
  constraint:
    - CON-177
  information:
    - INF-002
    - INF-394
  objective:
    - OBJ-232
  time:
    - TIM-004
---

# Game: Mario Party 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The Pirate Land
route, individual minigame, die values, purchase price and round count are
parameters of this bounded board-contest genome, not additional genes for
each character or visual space.

## Analysis scope

- Version / ruleset: original English 1999–2000 Nintendo 64 *Mario Party 2*
  Adventure Board rules, represented by the licensed Nintendo 64 – Nintendo
  Switch Online release. Select Pirate Land, four human-controlled characters,
  LITE PLAY (20 turns) and NO BONUS. The original Nintendo booklet, not a
  played cartridge or installed Switch wrapper, defines these rules.
- Structured analysis target: `GAME-0392` in
  [`knowledge/platforms/games.json`](../../platforms/games.json). The
  available licensed wrapper is a distribution target, not evidence that its
  controller remapping or save conveniences were inspected.
- Primary decision loop: each active player takes the Dice Block result,
  chooses a legal direction at any reached junction, processes pass-through
  transactions and the final landing event, and may spend Coins on an
  encountered Star or item. After all four have moved, their landing colors
  determine a minigame class; its result changes the Coin balances that fund
  later routes and Star purchases. Repeat until the board-turn limit.
- Entry: confirm the four-character Pirate Land board with LITE PLAY and NO
  BONUS, then resolve the initial Dice Block order and begin the first board
  turn. A replication must log every subsequent die result, route choice,
  landing, encounter outcome, minigame result, Coin and Star transfer.
- Positive terminal: after all four players and the post-round minigame have
  completed the twentieth turn, compare Stars first and Coins second; if both
  totals tie, the final Dice Block contest decides. This is the one board
  winner, not a campaign or Mini-Game Land completion.
- Negative terminal: a player with a lower final ranking loses that board
  match. A poor die roll, inability to afford Toad or a lost minigame does
  not immediately end the game. Exact CPU behaviour is outside this four-human
  scope.
- Included: initial turn order, random Dice Block movement, board junctions,
  pass-versus-land space effects, blue/red Coins, Koopa Bank, Toad's priced and
  moving Star, optional item purchase/use with one carried slot, Boo and
  board-specific question-space events, end-of-turn minigame class and Coin
  result, last-five-turn changes, visible standings and final no-bonus ranking.
- Excluded: Bonus Stars and Hidden Blocks, 35/50-turn settings, other Adventure
  Boards, detailed controls and win conditions of the sixty-four distinct
  minigames, Mini-Game Land, Coaster and Stadium, CPU policy, online wrapper
  features, exact random-number generator, arbitrary house rules and any
  claim of an observed playthrough. Minigame internals are separable modules;
  their class selection and board Coin outcome remain inside this packet.
- Potential scoped modules: one named Pirate Land minigame's full controls,
  the Pirate Land cannon or toll as its own event packet, a Bonus-on board
  contest, and the Mini-Game Coaster's independent progression loop.
- Direct-play status: none. The official original Nintendo instruction
  booklet supplies the rules; official Nintendo pages identify the game and
  current licensed availability. No cartridge, ROM, installed wrapper, save,
  controller trace, screenshot, video or audio was inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MP2-001` | Four characters play the chosen Adventure Board; LITE PLAY is 20 turns and NO BONUS removes hidden blocks and end awards. | Confirmed | Direct | High | P1 pp. 10–11 |
| `MP2-002` | A Dice Block sets movement count and the player chooses a direction at a junction; passed fixtures and landed spaces are not equivalent. | Confirmed | Direct | High | P1 pp. 12–13 |
| `MP2-003` | Blue/red landings change Coins by three, a passed Koopa Bank takes five, and landing on it can pay its pot. | Confirmed | Direct | High | P1 pp. 12–13 |
| `MP2-004` | Toad exchanges one Star for twenty Coins and moves after a purchase; an item shop requires enough Coins and no already-held item. | Confirmed | Direct | High | P1 pp. 12–14 |
| `MP2-005` | After all four moves, final space colors select a 4-player, 1-vs-3 or 2-vs-2 minigame class; green colors change before classification and results award Coins. | Confirmed | Direct | High | P1 pp. 14–15 |
| `MP2-006` | In the final five turns, blue/red values double and a shared landing can cause a wagered duel. | Confirmed | Direct | High | P1 pp. 14–15 |
| `MP2-007` | Pirate Land question spaces can fire ship cannons; individual cannon outcome parameters are not inferred from the summary. | Confirmed | Direct | High | P1 p. 17 |
| `MP2-008` | After the fixed board horizon, Stars outrank Coins; exact ties use a final die. | Confirmed | Direct | High | P1 p. 16 |
| `MP2-009` | The original Nintendo 64 title is available through licensed Nintendo Switch Online + Expansion Pack. | Confirmed | Direct | High | P2 |
| `MP2-010` | No exact N64 cartridge revision, wrapper build, minigame trace or random seed was directly inspected. | Observation | Direct | High | R1 |

## Basic data

- Release / origin: Nintendo/Hudson Soft's Nintendo 64 *Mario Party 2*,
  originally released in Japan in 1999 and western regions in 2000. The
  packet uses the English Nintendo 64 booklet rather than importing rules
  from later Mario Party sequels or *Mario Party Superstars*.
- Platform or physical form: original N64 board-game rules with a currently
  licensed Nintendo Switch Online N64 Classics distribution target,
  `PLAT-NINTENDO-SWITCH`. This does not claim the Switch executable was played.
- Puzzle family: `FAM-017` ordered dependency sequencing: board-space Coins
  and minigame results fund a later positional Star purchase, which changes
  the next target before a fixed terminal ranking.
- **[P1]** [Nintendo's original *Mario Party 2* instruction
  booklet](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/nintendo_8/Manual_Nintendo64_MarioParty2_EN.pdf),
  pp. 10–17, checked 2026-09-24. It supplies setup, movement, events,
  minigame classes, late turns and final results.
- **[P2]** [Nintendo's licensed-availability
  announcement](https://www.nintendo.com/us/whatsnew/nintendo-switch-online-expansion-pack-mario-party-and-mario-party-2-are-now-available/),
  checked 2026-09-24; used for the distribution target, not proof of precise
  wrapper behaviour.
- **[R1]** The source-bound and no-direct-play audit in this record.
- Claim IDs: `MP2-001`–`MP2-010`.

## Mechanical decomposition

### Action Genes

- `ACT-530`: choose one legal outgoing route at a junction during an already
  rolled move. The choice can change whether the token passes Toad or a bank.
- `ACT-130`: spend available Coins on a Star at Toad or on a currently offered
  item at a passed shop. The Star price and item offer are parameters.
- `ACT-131`: activate an eligible carried immediate-effect item, such as a
  Mushroom or a location-eligible Skeleton Key. The distinct item effects
  are not all recoded as one new player action.
- Candidate genes: none. Dice result is system chance, not player selection.
  Claim IDs: `MP2-002`, `MP2-004`.

### System Behaviour Genes

- `SYS-004`: the initial order and later Dice Blocks, green-space color
  conversion and other stated chance outcomes are unchosen by the player.
- `SYS-1050`: move the board token a rolled number of connected spaces while
  allowing mid-move junction direction and passed-fixture resolution.
- `SYS-1051`: distinguish transactions triggered by passing a fixture from
  effects of the final landing; Pirate Land question-space cannons are one
  board-specific parameter of an event landing.
- `SYS-1052`: after four players stop, route landing colors into the board
  minigame format, then carry the result and awarded/collected Coins back to
  persistent board balances.
- `SYS-1053`: one paid Star moves Toad's next purchasable Star to another
  board site, so later route choice changes.
- `SYS-1054`: the last-five phase changes colored Coin settlement and
  overlapping landing encounters before the twentieth result.
- Resolution order: active Dice Block → traversed route and pass events →
  final landing event and any immediate item or board contest → next player;
  after the fourth player, classify and settle the minigame → advance round;
  apply final-five modifiers when their phase begins → compare final totals.
  Claim IDs: `MP2-001`–`MP2-008`.

### Constraint Genes

- `CON-177`: at most one carried item; a player already holding one cannot
  buy another at the shop. Toad's twenty-Coin affordability is the price
  parameter of `ACT-130`, not a new currency gene. Claim ID: `MP2-004`.

### Information Genes

- `INF-002`: future Dice Block results and green-color conversion are not
  previewed before they occur.
- `INF-394`: the inspectable board map, current Toad site and visible four
  players' Coins/Stars support route and spending decisions. Future Star
  relocation is not shown in advance. Claim IDs: `MP2-002`, `MP2-004`–
  `MP2-005`.

### Objective Genes

- `OBJ-232`: the no-bonus board ends after 20 complete rounds with Stars as
  primary rank, Coins as next tiebreak and a final Dice Block for an exact
  tie. A single Star sale is progress, not immediate victory. Claim IDs:
  `MP2-001`, `MP2-008`.

### Time Genes

- `TIM-004`: exclusive active turns proceed among four opposing players in
  the initial die-determined order; a board round closes only after their
  four moves and the selected minigame. The internal live time of each
  separate minigame is not flattened into this board-time gene. Claim IDs:
  `MP2-001`, `MP2-005`.

## Reproducible transitions

| Before | Action | Rule-bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| The active token is two steps from a fork with a rolled movement count still remaining | Choose one outgoing branch | The token continues on connected spaces and spends the same die count; no new roll occurs at the fork | branch agency inside chance-bounded travel | `MP2-002` |
| A token passes Koopa Bank but does not finish on it | Continue movement | Five Coins enter the bank if the player can pay under the current rules; the token continues | passing is not a landing payout | `MP2-003` |
| A token finishes on a blue space in an ordinary round | End its move | Its balance rises by three Coins; a red landing instead reduces it by three | colored terminal space, not every traversed space | `MP2-003` |
| A player with at least twenty Coins passes Toad | Buy one Star | Pay twenty, gain one Star, and move the next sale site; without enough Coins no Star is granted | currency gate and shifting target | `MP2-004` |
| A player already carries one item and passes the shop | Attempt another purchase | The shop refuses a second item even when the player has Coins | carrying capacity is distinct from affordability | `MP2-004` |
| Four characters end a round with one contrasting landing color | Resolve green colors, then play the selected class | A one-versus-three format is chosen; the actual minigame result determines board Coin awards | landing composition determines encounter class, not winner | `MP2-005` |
| The board has entered its final five turns | Land on a blue space or on another token's space | The blue payout becomes six Coins, or a shared-space duel can be initiated | closing-phase rule switch | `MP2-006` |
| The twentieth round and minigame are settled with equal Stars | Compare Coins; if still equal, roll final tiebreak | Higher Coin total wins; exact dual tie invokes the final Dice Block | finite lexicographic terminal | `MP2-008` |

## Strategic and experiential structure

- Local decision: after an uncertain die result, choose a reachable branch
  that balances a nearer Star, Coin income, item service and dangerous space.
- Medium-term planning: save enough Coins for the next Toad pass; minigame
  performance and bank or rival events can change affordability before that
  opportunity. A sold Star moves the route target.
- Long-term structure: twenty board rounds reward Star acquisition first,
  while leftover Coins matter to ties. NO BONUS removes hidden-block and
  three end-award Star routes from this packet.
- Common heuristics: inspect the map and standings before spending; a route
  toward the Star is not guaranteed by the die, and a favorable minigame
  result is not assumed.
- Failure attribution: a route choice and an item purchase are attributable,
  but die rolls, green conversion, encounters and distinct minigame outcomes
  introduce uncertainty. No exact random probabilities are claimed.
- Player-trust factors: official rules show priced Star and item gates, color
  conversion, final-five changes and final tiebreak rather than implying
  that the die alone decides the match. Claim IDs: `MP2-001`–`MP2-008`.

## Replay and variation

- Different Dice Block sequences, junction choices, purchases, event spaces,
  selected minigames and results change the board economy and winner.
- The Pirate Land map and no-bonus 20-turn setting are fixed for this packet;
  hidden blocks and end awards do not silently enter it.
- A player can pursue Coins for a later Star or preserve currency for a tied
  final score; no exact winning probability is inferred. Claim IDs:
  `MP2-001`–`MP2-008`.

## Adjacent systems and history

- *CATAN* also turns dice and resources into contested board progress, but
  its number roll produces adjacent resources, players trade and build a
  network, and the match ends at a point threshold on the claimant's turn.
  Pirate Land instead moves tokens by die count, runs a post-round contest
  and ranks Stars before Coins after a fixed horizon.
- The first *Mario Party*, other boards, bonus-on play and later sequels may
  share elements; their precise rules are not substituted for this booklet.
- Mini-Game Land is an independent progression mode, not a continuation of
  this one board contest. Claim IDs: `MP2-001`, `MP2-005`, `MP2-008`.

## Normalised genome

| Type | Active genes | Parameters outside signature |
|---|---|---|
| Action | `ACT-130`, `ACT-131`, `ACT-530` | shop offers, item identity, junction directions |
| System | `SYS-004`, `SYS-1050`–`SYS-1054` | die outcomes, space layout, coin values, vendor site |
| Constraint | `CON-177` | one item slot, purchase windows |
| Information | `INF-002`, `INF-394` | map geometry, standings, revealed Star site |
| Objective | `OBJ-232` | twenty turns, NO BONUS, final tallies |
| Time | `TIM-004` | four-player order and round index |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `391` (`GAME-0001`–`GAME-0391`).
- Exact genome matches: none.
- Tied near matches: `GAME-0120` — Slay the Spire (`5 / 38 = 0.131579`).
- Supported combination subsets: none.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0120` Slay the Spire | `ACT-130`, `ACT-131`, `SYS-004`, `CON-177` and `INF-002` share priced offers, consumable use, chance, carried-slot capacity and an unpreviewed future. | Slay the Spire follows a branching encounter map into card-hand combat, with energy, deck and enemy-turn resolution. Pirate Land spends a die count across a fixed board, settles four players' landing colors into a separate minigame, moves a paid Star vendor and compares Star then Coin totals at a turn horizon. Shared economy and uncertainty do not make the board and deck loops equivalent. | `5 / 38 = 0.131579`; tied near maximum, not an exact board-contest match |

### Preserved research notes

- New genes: `ACT-530`, `SYS-1050`–`SYS-1054`, `INF-394`, `OBJ-232`.
- Classification result: New gene.
- Evidence and reasoning: the Nintendo booklet defines a repeated die-bound
  board turn, pass/land split, minigame-to-Coin bridge, moved Star vendor and
  final ranking not captured by one prior CATAN-like threshold race.

## Taxonomy impact

- Registry changes: add eight Active IDs without revising an older gene or
  game signature.
- Taxonomy-change record: `TAXONOMY_CHANGE_130`.
- Candidate terms affected: board junction, passed fixture, minigame Coin
  bridge and Star-ranking terminal. Character names, space colours and Coin
  amounts remain parameters.

## Negative results

- No separate negative-result record. The minigame control packets, bonus-on
  rules and CPU policy are excluded by the stated scope, not disproven.

## Delta summary

The compact delta below names only this game's new corpus evidence.

## New facts

- [Confirmed | Direct | High] The original no-bonus board has four rotating
  players, a post-round minigame and a Stars-then-Coins terminal at the chosen
  twenty-turn limit (`MP2-001`, `MP2-005`, `MP2-008`).

## New genes

- [Observation | Direct | High] Eight new board-contest genes distinguish
  route choice, die-counted traversal, pass/land effects, minigame payout,
  vendor relocation, final-phase switch, public standings and final rank.

## New combinations

- [Observation | Direct | High] No new verified combination; no proper
  subset is promoted from one board example alone.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_130` records the additive
  transfer tests; no earlier signature is changed.

## New questions

- Does a named Pirate Land minigame form an independently useful scoped
  analysis once its exact control and scoring rules are directly verified?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0393` Mortal Kombat II.
- Optimisation criterion: contrast the discrete board economy and minigame
  bridge with a fixed-fighter live duel and its round result.
- Expected information gain: reuse or refine fighting timing and result
  boundaries against existing Street Fighter and Mortal Kombat analyses.
- Backlog impact: preserves the accepted genre-alternating order.

## Why this game

- [Hypothesis | Limited | Medium] A four-player board contest links chance,
  spatial choice, currency, short contests and a fixed end ranking; that
  differs from the preceding single-avatar live climb and city simulation.
