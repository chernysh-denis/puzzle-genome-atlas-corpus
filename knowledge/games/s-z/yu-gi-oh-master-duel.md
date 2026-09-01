---
game_id: GAME-0206
slug: yu-gi-oh-master-duel
game_title: "Yu-Gi-Oh! Master Duel"
analysis_status: reviewed
reviewed: 2026-09-01
combination_ids:
  - COMB-0204
gene_ids:
  action:
    - ACT-371
    - ACT-372
    - ACT-373
    - ACT-374
    - ACT-375
    - ACT-376
    - ACT-377
  system:
    - SYS-681
    - SYS-682
    - SYS-683
    - SYS-684
    - SYS-685
    - SYS-686
  constraint:
    - CON-544
    - CON-545
    - CON-546
    - CON-547
    - CON-548
    - CON-549
  information:
    - INF-003
    - INF-266
  objective:
    - OBJ-109
  time:
    - TIM-020
---

# Game: Yu-Gi-Oh! Master Duel

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam public build
  `24462996`, built 2026-07-30 and reviewed 2026-09-01; online account used
  only to enter Solo Mode; Tutorial gate, final goal chapter `10003`, fixed
  loaner deck versus CPU `First Duel Partner`, `4,000` LP each, `40` fixed
  Main Deck cards each, player Extra Deck of `5`, opponent Extra Deck of `0`,
  fixed opening hands of `5`, `noshuffle: true`, no personal deck, no mods.
- Primary decision loop: inspect the fixed hand, public zones, phase, Life
  Points and card text; Normal Summon/Set or Special Summon an eligible monster;
  Set or activate a Spell/Trap/effect; choose whether to add a legal Chain Link;
  advance through the ordered phases; declare one eligible attack and target;
  resolve the completed Chain, card movement and battle; repeat across
  alternating turns until the duel result settles.
- Entry and exit: after clearing prerequisite Tutorial chapters `10001` and
  `10002`, select goal chapter `10003` and accept its supplied packet. Entry is
  the first retained opening-hand decision state of the chapter. Positive exit
  is the Victory result after `First Duel Partner` first meets a legal loss
  condition, chapter `10003` is marked clear and retained control returns to
  the Tutorial gate. Defeat, deck-out of the controlled player or surrender is
  a negative result and does not establish the positive terminal.
- Included: the fixed chapter `10003` card order and hands; player and opponent
  hidden hands/decks; visible Monster, Spell/Trap, Graveyard and Extra Deck
  state; Draw, Standby, Main 1, Battle, Main 2 and End phases; one Normal
  Summon/Set allowance; Tribute, Flip and reachable Special Summons; Attack and
  Defense Position; Set Spell/Trap delay; reachable costs, targets, Spell
  Speeds and alternating Chain responses; reverse-order Chain resolution;
  individual attacks, ATK/DEF comparison, destruction, battle damage, direct
  damage, LP, failed-draw and surrender terminals; the result and gate-clear
  return.
- Excluded: the guided actions inside chapters `10001` and `10002` beyond
  their prerequisite clear flags; starter-deck choice and tutorial rewards;
  deck editing, personal collection, crafting, dismantling, Gems, packs, shop
  and missions; Duel Strategy, later Solo gates and loaners; Casual, Ranked,
  Team, Duel Room, events and every PvP mode; current Forbidden/Limited lists,
  side decks, match play and tournament policy; cards and summon procedures not
  reachable from the two fixed packets; mobile/console input, cosmetics,
  replays, spectating, achievements, mods and unofficial server operation.
- Potential scoped modules: either guided prerequisite chapter; one named Duel
  Strategy practice; another fixed Solo loaner chapter; one current Ranked
  ruleset; or collection/deck-construction economy each requires a separate
  version, admitted card packet, entry and terminal.
- Direct-play status: no authenticated current Steam-client play was performed.
  Konami product, support and official rulebook evidence establishes the Solo
  tutorial and rules kernel. Current public build metadata and a pinned
  read-only extraction of the client Solo structures corroborate the exact
  chapter, fixed packet and result boundary. No extracted asset or proprietary
  audiovisual material enters the repository; the transition table is rules
  reasoning, not a direct-play claim.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MD-001` | Windows Steam public build `24462996` is the reviewed executable boundary | Confirmed | Corroborated | High | P1, S1 |
| `MD-002` | Konami presents Solo Mode as the new-player place for basic operation and rules, with Tutorial and Duel Strategy | Confirmed | Direct | High | P1, P2 |
| `MD-003` | Tutorial gate `1` ends at clear chapter `10003`, whose ordered prerequisites are `10001` and `10002` and whose `mydeck_set_id` is zero | Observation | Corroborated | High | S2, S3 |
| `MD-004` | Chapter `10003` is Solo PvE against `First Duel Partner` with two fixed 40-card Main Decks, only the player's five-card Extra Deck, fixed five-card hands, no shuffle and 4,000 LP each | Observation | Corroborated | High | S2, S3 |
| `MD-005` | A turn advances through Draw, Standby, Main 1, Battle, Main 2 and End; the first player cannot draw or battle on the first turn | Confirmed | Direct | High | P3 |
| `MD-006` | A player may normally Summon or Set once per turn, while higher-Level monsters require Tributes and legal Special Summons follow their stated procedure | Confirmed | Direct | High | P3 |
| `MD-007` | Spells, Traps and effects require their stated timing, costs and targets; a Trap must normally be Set until a later turn | Confirmed | Direct | High | P3, S4 |
| `MD-008` | Eligible responses form numbered Chain Links under Spell Speed, then the completed Chain resolves newest effect first without adding new links during resolution | Confirmed | Direct | High | P3 |
| `MD-009` | One declared monster attack resolves through target position, ATK/DEF, destruction, battle damage or a direct LP debit | Confirmed | Direct | High | P3 |
| `MD-010` | Zero LP, failure to draw or an applicable card effect can lose a Duel; chapter result and gate clear form the bounded positive terminal | Confirmed | Corroborated | High | P3, S2, S3 |
| `MD-011` | The fixed player packet includes Normal, Effect and Tuner monsters, Normal Spells, Normal/Continuous Traps and Synchro, Xyz and Link options, so the admitted loop exposes summon, Set, battle and response choices without collection construction | Observation | Corroborated | High | S2–S4 |
| `MD-012` | The bounded game is a deterministic hidden-card duel whose main uncertainty is concealed fixed information and the CPU's legal choices, not deck generation | Observation | Corroborated | High | MD-003–MD-011 |

## Basic data

- Release / origin: developed and published by Konami Digital Entertainment;
  worldwide digital release in 2022, reviewed through the current Windows
  Steam public build in 2026.
- Platform or physical form: network-authenticated digital collectible-card
  game on PC, consoles and mobile; only the declared Windows Solo chapter is
  admitted.
- Puzzle family: hidden-state inference; tactical forecast and counterplay;
  ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official Master Duel product and Solo page](https://www.konami.com/yugioh/masterduel/eu/en/),
    for Windows availability, Solo Mode, Tutorial, Duel Strategy and the
    maintained 2026 product boundary.
  - **[P2]** [official Konami new-player support answer](https://us-support.konami.com/hc/en-us/articles/4812893829399-I-m-new-to-Yu-Gi-Oh-MASTER-DUEL-How-should-we-start-the-game),
    for learning basic operations, rules and tactics in Solo Mode before Duel.
  - **[P3]** [official Yu-Gi-Oh! rulebook](https://www.yugioh-card.com/en/downloads/rulebook/SD_RuleBook_EN_10.pdf),
    especially pp. 24–30 and 33–47 for Summon/Set, Spell/Trap timing, phases,
    battle, LP terminals, Chains and Spell Speed.
- Reproducible mechanics sources:
  - **[S1]** [SteamDB public depots](https://steamdb.info/app/1449850/depots/),
    for Windows public build `24462996`, built 2026-07-30.
  - **[S2]** [pinned YgoMaster Solo dump](https://github.com/pixeltris/YgoMaster/blob/b1c313fd6ce398e132f79ac566e801e406a90a7e/YgoMaster/Data/Solo.json),
    for gate `1`, ordered chapter prerequisites, `clear_chapter: 10003`, CPU
    identities and loaner-only `mydeck_set_id: 0`.
  - **[S3]** [pinned chapter `10003` packet](https://github.com/pixeltris/YgoMaster/blob/b1c313fd6ce398e132f79ac566e801e406a90a7e/YgoMaster/Data/SoloDuels/10003.json),
    for fixed Main/Extra Deck counts, card order, hands, LP, CPU, no-shuffle,
    Solo flag and result-capable chapter identity.
  - **[S4]** [YGOProDeck card data API](https://db.ygoprodeck.com/api-guide/),
    used only to corroborate types and current English text of the fixed packet,
    including `Unexpected Dai`, `Ballista Squad`, `Call of the Haunted`,
    `Skill Successor`, `Mighty Warrior`, `Kachi Kochi Dragon` and Link cards.
- Claim IDs: `MD-001`–`MD-012`.

## Mechanical decomposition

### Action Genes

- New `ACT-371`: Normal Summon or Normal Set one eligible monster from hand,
  consuming the shared once-per-turn allowance.
- New `ACT-372`: commit one legal rule-procedure Special Summon by choosing the
  source, required materials and resulting position.
- New `ACT-373`: Set one Spell or Trap from hand into an open Spell/Trap Zone.
- New `ACT-374`: activate one eligible Spell, Trap or monster effect, paying
  costs and declaring required targets so it becomes the first Chain Link.
- New `ACT-375`: add one eligible response as the next Chain Link after the
  opponent's activation opportunity.
- New `ACT-376`: declare one eligible Attack Position monster's attack against
  a legal target or directly when no target prevents it.
- New `ACT-377`: change one eligible monster between Attack Position and
  face-up Defense Position, or Flip Summon an eligible Set monster.
- Parameters: hand card, field zone, summon allowance, Tribute, materials,
  battle position, Spell/Trap, effect, cost, target, Spell Speed, Chain Link,
  attacker and defender.
- Claim IDs: `MD-006`–`MD-009`, `MD-011`, `MD-012`.

### System Behaviour Genes

- New `SYS-681`: instantiate the fixed loaner/opponent packets, fixed concealed
  order, five-card hands, LP totals and public zones for chapter `10003`.
- New `SYS-682`: advance the ordered turn phases, perform the legal Draw and
  phase-bound actions, refresh turn allowances and transfer the active turn.
- New `SYS-683`: alternate legal response opportunities, append numbered Chain
  Links and resolve the completed Chain from newest effect to oldest.
- New `SYS-684`: apply resolving card text and move cards among hand, Deck,
  field, Graveyard, banished and Extra Deck states.
- New `SYS-685`: resolve one declared attack from positions and ATK/DEF into
  destruction, battle damage, direct LP damage or no LP change.
- New `SYS-686`: monitor legal Duel-loss predicates, settle Victory/Defeat and
  update the Solo chapter/gate clear state before returning retained control.
- Resolution order: instantiate the fixed packet; expose the opening state;
  advance phases and active player; accept legal summons, Sets, activations,
  position changes and attacks; ask alternately for compatible responses;
  settle a completed Chain backward; route cards and apply battle; check the
  duel terminal after every relevant change; otherwise continue to the next
  phase or turn.
- Claim IDs: `MD-003`–`MD-012`.

### Constraint Genes

- New `CON-544`: Tutorial chapter `10003` admits only its two immutable
  loaner/CPU packets and does not accept a personal or edited deck.
- New `CON-545`: Normal Summon/Set shares one own-turn allowance, higher-Level
  monsters require the declared Tributes and Special Summons require all
  procedure or card-text materials.
- New `CON-546`: Monster and Spell/Trap placements require an open compatible
  zone and a legal face-up/face-down Attack/Defense state.
- New `CON-547`: a card or effect requires its phase, activation predicate,
  cost and targets, while an ordinary Trap cannot activate during the turn it
  was Set.
- New `CON-548`: a Chain response requires a compatible Spell Speed not lower
  than the preceding link; no new link enters while the completed Chain is
  resolving.
- New `CON-549`: an attack requires the Battle Phase, an eligible Attack
  Position monster that has not used its ordinary attack and a legal target;
  the first player has no first-turn Battle Phase.
- Scarce strategic resources: cards in the fixed hand and Deck, once-per-turn
  Normal Summon/Set, open zones, monsters usable as Tributes/materials, Set
  response latency, eligible Chain windows, attacks, LP and concealed
  opponent information.
- Claim IDs: `MD-004`–`MD-012`.

### Information Genes

- Existing `INF-003`: fixed Deck order, opponent hand and face-down cards exist
  in current state but remain concealed until a legal draw, reveal or effect.
- New `INF-266`: the digital duel interface exposes own hand, both LP totals,
  public cards/zones, phase, positions, inspected card text, legal prompts and
  the current ordered Chain without revealing concealed opponent resources.
- Claim IDs: `MD-004`–`MD-012`.

### Objective Genes

- Existing `OBJ-109`: cause the opposing player to meet a legal single-game
  loss condition before the controlled player, then receive the Duel result.
- Success, evaluation and failure: ordinary success reduces `First Duel
  Partner` to zero LP, but legal empty-Deck or card-defined loss also settles
  Victory. Controlled-player loss or surrender settles Defeat. The positive
  packet closes only when chapter/gate clear state returns to Solo control;
  rewards and starter-deck selection are outside evaluation.
- Claim IDs: `MD-010`, `MD-012`.

### Time Genes

- New `TIM-020`: players alternate active turns through fixed phases, while
  eligible activations create alternating Chain-response windows that close
  before reverse-order resolution and phase continuation.
- Claim IDs: `MD-005`, `MD-007`, `MD-008`, `MD-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Tutorial chapters `10001` and `10002` are clear | Select chapter `10003` | The client admits the fixed two-deck, five-card-hand, 4,000-LP Solo packet without personal deck selection | bounded loaner entry | `MD-003`, `MD-004` |
| Own Main Phase 1 has an unused Normal Summon/Set allowance and an open Monster Zone | Normal Summon one eligible Level 4 monster | It enters face-up Attack Position and the shared Normal Summon/Set allowance becomes spent | summon and set share a turn resource | `MD-006` |
| The same allowance is spent | Attempt another ordinary Normal Summon or Set | The action remains illegal unless card text grants an exception; a compatible Special Summon remains separately possible | normal and special procedures differ | `MD-006` |
| A Trap is in hand and an open Spell/Trap Zone exists | Set the Trap | It becomes concealed public occupancy, but ordinary activation is unavailable until the next turn | Set creates delayed response authority | `MD-007` |
| An eligible effect is activated as Chain Link 1 | Opponent adds a compatible Spell Speed response, then the player adds another legal response | The effects remain unresolved as Links 1–3 until neither side adds a link | activation and effect are separated | `MD-008` |
| Both sides decline another legal response to a three-link Chain | Close the Chain | Link 3 resolves first, then Link 2 and Link 1; no new link enters during that resolution | Yu-Gi-Oh! reverse resolution is not the MTG stack | `MD-008` |
| A Tuner and compatible non-Tuner levels are face-up in Main Phase | Declare the reachable Synchro Summon and choose materials | Materials move to the Graveyard and the matching Extra Deck monster enters the legal zone | fixed Extra Deck adds procedure planning | `MD-006`, `MD-011` |
| An eligible Attack Position monster is controlled in a legal Battle Phase | Declare its attack on an opposing Attack Position monster | ATK values determine destruction and LP battle damage; responses may form before damage settlement | attack is one target-bound commitment | `MD-009` |
| The opponent controls no monster preventing a direct attack | Declare a direct attack with sufficient ATK | The attack debits the opponent's LP by that ATK after legal responses settle | board clearance converts to terminal pressure | `MD-009` |
| Opponent LP reaches zero after a legal effect or battle | Complete the current rules check | The opponent loses, Victory appears, chapter `10003` clears and retained Tutorial-gate control returns | explicit bounded positive terminal | `MD-010` |
| The controlled player must draw with no card remaining | Advance the Draw Phase | The controlled player loses and the Defeat result returns without positive clear | alternate negative terminal | `MD-010` |

## Strategic and experiential structure

- Local decision: commit the once-per-turn monster placement, conceal a delayed
  Trap, spend monsters as Tribute or Extra Deck materials, attack the exposed
  target or preserve a legal response and position.
- Medium-term planning: use the fixed hand and known own packet to build enough
  field presence while reading face-down occupancy, remaining zones, possible
  Chain responses and whether battle exposes LP or a counterattack.
- Long-term structure: convert a fixed concealed Deck into visible monsters and
  delayed interaction, use ordered phases and Chains to gain field advantage,
  then turn cleared opposing Monster Zones into LP loss before deck-out.
- Common heuristics: spend the Normal Summon/Set only after checking material
  routes; Set Traps before yielding the turn; inspect exact activation timing;
  build Chains so the newest effect protects or changes earlier links; compare
  ATK/DEF and positions before committing each attack.
- Failure attribution: own hand, public field, LP, phase, Chain and card text
  are visible; the opponent's fixed but concealed hand, Deck order and
  face-down identities keep exact counterplay uncertain.
- Player-trust factors: legal highlights, prompts, phase indicators, inspected
  card text, Chain numbering and result state explain settlement; client
  automation does not imply that personal deckbuilding or the full card pool is
  inside this packet.
- Claim IDs: `MD-004`–`MD-012`.

## Replay and variation

- What changes between attempts: player choices, CPU choices, summons, Sets,
  activations, Chain growth, targets, battle positions, attacks, LP route and
  terminal, while the admitted card order and opening packet remain fixed.
- Randomness or procedural generation: none is claimed inside the chapter
  fixture; `noshuffle: true` and the retained packet make concealed order fixed.
  CPU policy may choose among legal actions, but no unpublished distribution is
  inferred.
- Multiple viable strategies: yes; normal-monster development, Trap timing,
  card removal, recovery and the reachable Synchro/Xyz/Link routes can produce
  different legal wins from the same packet.
- Typical replay motive: learn phase, Summon/Set, battle and Chain rules or
  recover from a poor line without collection or matchmaking variance.
- Claim IDs: `MD-003`–`MD-012`.

## Adjacent systems and history

- Direct predecessors: the maintained Yu-Gi-Oh! Trading Card Game rules supply
  the duel kernel; Master Duel implements those rules with digital zones,
  prompts, legal checks, Solo opponents and current client presentation.
- Variants: guided Tutorial chapters, Duel Strategy, later Solo loaners,
  constructed PvP, events, Ranked formats and collection economy alter the
  packet, rules or terminal and remain outside scope.
- Similar games: Magic: The Gathering Arena, Inscryption, Slay the Spire and
  other digital adversarial card engines.
- Important differences: unlike MTG Arena, Master Duel has no land/mana growth,
  blocker declaration, London mulligan, priority or separately resolving top
  stack object. It uses a shared Normal Summon/Set allowance, monster positions,
  one-at-a-time attacks and a completed Spell-Speed Chain that resolves all
  links backward. Unlike Inscryption, it has no fixed opposing lanes, Blood
  sacrifice economy or relative damage scale. Unlike Slay the Spire, it is a
  two-sided duel rather than a planning hand followed by autonomous intent.
- Claim IDs: `MD-002`–`MD-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-371`–`ACT-377` | summon, set, activate, respond, attack and position parameters |
| System Behaviour | `SYS-681`–`SYS-686` | fixture, phases, Chain, card text, battle and result parameters |
| Constraint | `CON-544`–`CON-549` | loaner, summon, zone, timing, Spell Speed and attack parameters |
| Information | `INF-003`, `INF-266` | concealed packet and public duel interface parameters |
| Objective | `OBJ-109` | opponent loss and chapter-clear result parameters |
| Time | `TIM-020` | active turn, phase and Chain-response parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `205` (`GAME-0001`–`GAME-0205`).
- Exact genome matches: none.
- Tied near matches: `GAME-0185` — Magic: The Gathering Arena (`2 / 47 = 0.042553`).
- Supported combination subsets: `COMB-0204`.
- Scan date: 2026-09-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0185` — Magic: The Gathering Arena | `INF-003`, `OBJ-109` | both conceal fixed card information and end one adversarial game at a legal player-loss result; Master Duel replaces land/mana, mulligan, blockers, MTG priority and one-object stack settlement with loaner-only fixed order, one Normal Summon/Set allowance, positions, single attacks and whole-Chain reverse resolution | Near, `0.042553` |

### Preserved research notes

- New genes: `ACT-371`–`ACT-377`, `SYS-681`–`SYS-686`, `CON-544`–`CON-549`,
  `INF-266` and `TIM-020`.
- Reused genes: `INF-003` and `OBJ-109`; no earlier reviewed signature changed.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: only fixed concealed current information and the
  single-game opponent-loss objective fit earlier boundaries. The Tutorial
  fixture, Summon/Set allowance, positions, Spell-Speed Chain and individual
  attack sequence require separate mechanically testable rules.

## Taxonomy impact

- Registry changes: twenty-one new Active genes, links on `INF-003` and
  `OBJ-109`, `COMB-0204` and three existing family memberships.
- Taxonomy-change record: none; no existing lifecycle, definition or reviewed
  game signature changes.
- Candidate terms affected: fixed Solo loaner, Normal Summon/Set, procedure
  Special Summon, Spell/Trap Set, activation, Chain Link, Spell Speed, battle
  position, individual attack, reverse Chain resolution, public duel
  interface and alternating phase/Chain time.

## Negative results

- `ACT-333`–`ACT-337`, `SYS-585`–`SYS-590`, `CON-490`–`CON-495`, `INF-239`
  and `TIM-019` are not reused: their definitions depend on MTG casting,
  land/mana, priority, blockers, stack-object settlement, state-based actions
  or the Arcane Aerialists event.
- `ACT-125`, `SYS-163`, `SYS-164`, `CON-043` and `TIM-005` are not reused:
  Slay the Spire's energy-priced solitary planning hand and hostile phase do
  not model alternating duel control or Chains.
- `ACT-135`, `SYS-172`, `CON-180`, `CON-182` and `OBJ-057` are not reused:
  Inscryption's four paired lanes, Blood cost and five-point relative scale are
  absent.
- `SYS-004` is rejected because the admitted chapter explicitly fixes order
  with `noshuffle: true`; concealed state is not enough to claim a randomised
  library.
- The full current card pool, banlist, collection economy and every unreachable
  card mechanic are rejected even though the live product supports them.

## Delta summary

## Нові факти

- [Confirmed | Direct + Corroborated | High] Поточний Tutorial chapter `10003`
  надає два незмінні пакети, упорядковані фази, виклики/встановлення, ланцюги,
  бій і явний результат без особистої колоди (`MD-001`–`MD-012`).

## Нові гени

- [Observation | Direct + Corroborated | High] Додано 21 ген для незмінного
  навчального пакета, правил виклику й установлення, ланцюга, позицій, бою,
  інтерфейсу та чергування фаз.

## Нові комбінації

- [Observation | Direct + Corroborated | High] `COMB-0204` поєднує обмеження
  позиченої колоди з фазами, ланцюгом і боєм до першого законного результату.

## Зміни таксономії

- [Observation | Corroborated | High] Життєвих циклів чи попередніх сигнатур
  не змінено; два наявні загальні гени лишилися без змін.

## Нові питання

- Яка наступна гра повторює підготовку спорядження й фазове полювання, але
  повертає безперервне позиційне керування замість прихованої карткової руки?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0207` — Monster Hunter: World.
- Optimisation criterion: continue the recorded demand-led Goal in exact order.
- Expected information gain: test one versioned hunt whose tracking,
  preparation, weapon commitment, monster state and carve/reward settlement
  replace fixed-card phases and Chains.
- Backlog impact: ninth and final game unit before the batch audit.

## Чому саме вона

- [Hypothesis | Limited | Medium] Monster Hunter: World should reuse embodied
  preparation and live combat while isolating one hunt's tracking, sharpness,
  part damage, flee/return cycle and explicit quest settlement.
