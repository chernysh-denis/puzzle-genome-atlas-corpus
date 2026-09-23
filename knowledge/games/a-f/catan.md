---
game_id: GAME-0377
slug: catan
game_title: CATAN
analysis_status: reviewed
reviewed: 2026-09-23
combination_ids: []
gene_ids:
  action:
    - ACT-513
    - ACT-514
    - ACT-515
    - ACT-516
    - ACT-517
    - ACT-518
  system:
    - SYS-004
    - SYS-1024
    - SYS-1025
    - SYS-1026
    - SYS-1027
  constraint:
    - CON-681
    - CON-682
    - CON-683
    - CON-684
  information:
    - INF-002
    - INF-003
    - INF-384
  objective:
    - OBJ-219
  time:
    - TIM-004
---

# Game: CATAN

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Resource names,
piece counts, exchange ratios and the ten-point threshold parameterise the
genes rather than becoming a separate gene for each value.

## Analysis scope

- Version / ruleset: CATAN's fifth English-language base rules, whose text
  states a 2015 precedence date, in the publisher-hosted 2020 PDF checked
  2026-09-23. This is the
  four-player physical game using its fixed *Starting Set-up for Beginners*,
  with the ordinary separate roll, trade and build phases. The optional
  combined trade/build phase is excluded. No physical printing, full match,
  video or installed digital adaptation was inspected.
- Structured analysis target: `PLAT-PHYSICAL-TABLETOP`, four players, 19
  terrain hexes, the printed fixed starting board, base resources and
  development deck. The exact die and shuffled-card sequence is recorded for
  replication, not presumed deterministic.
- Primary decision loop: the active player rolls two dice; numbered adjacent
  settlements and cities produce resources for all eligible players, or a
  seven forces discards and robber movement; the active player may trade
  resource cards, then spend typed cards on legal roads, settlements, cities
  or development cards. One eligible development card can be played during
  the turn. Road reach, scarce intersections, production odds and concealed
  hands feed back into later turns and visible victory points.
- Entry and exit: assemble the publisher's beginner board, give all four
  colours two starting settlements and roads plus the prescribed starting
  resources, shuffle the development deck and pass the first player the
  dice. The positive terminal is the first player who has at least ten
  victory points **on their own turn** and declares victory. A player who
  reaches ten on another turn must wait; an illegal construction or failed
  trade is not a game-over.
- Included: number-triggered production, bank shortage, the seven/robber
  sequence, active-player domestic exchange, maritime exchange with normal
  or owned-harbour ratios, piece costs and limits, road and settlement
  topology, city upgrades, development-card purchase and permitted play,
  transferable Longest Road and Largest Army bonuses, concealed hands and
  development cards, and the ten-point own-turn victory gate.
- Excluded: variable board setup, 3-player/5–6-player variants, Seafarers,
  Cities & Knights, other expansions, online or app adaptations, house
  rules, trading development cards, simultaneous turns and the optional
  combined trade/build phase. Card art and flavour are not mechanisms.
- Direct-play status: none. The official publisher rules provide direct
  normative evidence, but this packet is a source-based reconstruction, not
  a claimed observed playthrough. A physical replication should record the
  edition, board layout, dice, trades, piece positions, hidden-card reveals,
  supply shortages, bonus-holder changes and final point proof.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| CAT-001 | The fixed beginner setup gives each of four players two initial roads and settlements, with starting resources around the marked settlement. | Confirmed | Direct | High | P1 pp. 1–2 |
| CAT-002 | Every ordinary turn rolls two dice, trades, then builds; an eligible development card may be played during the turn. | Confirmed | Direct | High | P1 pp. 3–4 |
| CAT-003 | A numbered roll produces one resource for each adjacent settlement and two for each city, subject to robber blocking and the finite bank. | Confirmed | Direct | High | P1 pp. 3–4, 9 |
| CAT-004 | A seven yields no production, forces players above seven hand cards to discard half rounded down, then moves the robber and permits one random adjacent steal. | Confirmed | Direct | High | P1 p. 4 |
| CAT-005 | The active player may exchange resources with another player or the bank; maritime rates depend on a settlement or city at a harbour. | Confirmed | Direct | High | P1 pp. 3, 8, 13 |
| CAT-006 | Roads extend from the player's network; settlements obey distance and connection rules; a city replaces an owned settlement. All cost typed resources and available pieces. | Confirmed | Direct | High | P1 pp. 3–4, 6, 11–12 |
| CAT-007 | Development purchases draw hidden cards; one knight or progress card may be played per turn but not on its purchase turn; victory-point cards are a stated exception. | Confirmed | Direct | High | P1 pp. 4, 7, 9 |
| CAT-008 | Longest Road and Largest Army each carry two transferable points, with minimum five road segments or three played knights respectively. | Confirmed | Direct | High | P1 pp. 8–9 |
| CAT-009 | First reaching at least ten points wins only on that player's own turn. | Confirmed | Direct | High | P1 pp. 4, 7 |

## Basic data

- Release / origin: CATAN is the physical base board game by Klaus Teuber;
  this packet uses the fifth English-language base rules in CATAN's 2020 PDF,
  not an assertion about a specific boxed print run or digital adaptation.
- Platform or physical form: four-person physical tabletop game,
  `PLAT-PHYSICAL-TABLETOP`.
- Puzzle family: contested network construction and resource-economy planning;
  the win condition is adversarial rather than a fixed solo solution.
- **[P1]** [Official CATAN base-game rules and almanac
  PDF](https://www.catan.com/sites/default/files/2021-06/catan_base_rules_2020_200707.pdf),
  16 pages, checked 2026-09-23. The publisher's [rules
  hub](https://www.catan.com/understand-catan/game-rules) now also links a
  newer edition; this packet intentionally does not mix editions.

## Mechanical decomposition

### Action Genes

- `ACT-513`: the active player negotiates and commits an accepted
  typed resource-card exchange with another player; a rival may make a
  counteroffer, but non-active players cannot trade among themselves.
- `ACT-514`: the active player gives a matching resource set to the bank and
  selects a different resource, using an available 4:1, 3:1 or 2:1 rate.
- `ACT-515`: pay the declared cost and place a road or settlement, or replace
  an owned settlement with a city, at a legal board location.
- `ACT-516`: buy the top hidden development card from a nonempty deck using
  ore, wool and grain; the player chooses to buy but not the card identity.
- `ACT-517`: choose and play a permitted development card. Knight, Road
  Building, Year of Plenty and Monopoly effects are typed parameters; a
  victory-point card is revealed at the required winning declaration.
- `ACT-518`: after a seven or played knight, relocate the robber to another
  hex and select one adjacent opposing owner to steal from if one is present.

### System Behaviour Genes

- `SYS-004` resolves the unpredictable two-dice result, random stolen
  resource and shuffled development draw; probabilities are not an extra gene.
- `SYS-1024` pays numbered-hex production to all adjacent owners; cities
  double their yield, the robber blocks its hex and finite supply can prevent
  a contested resource payout.
- `SYS-1025` handles the seven sequence: no production, simultaneous
  above-seven hand discards, then robber relocation and random steal.
- `SYS-1026` executes a revealed development card's declared effect, such as
  knight robber movement, two legal roads, two bank resources or gathering
  one named resource from every opponent.
- `SYS-1027` recalculates Longest Road and Largest Army; possession and two
  points move when another player qualifies under the printed comparison and
  tie rules. A rival settlement can interrupt a road.
- Resolution order: roll and production or seven; optional eligible card
  play; domestic/maritime trade; paid construction and card purchase; check
  whether the active player can claim victory, then pass dice left.

### Constraint Genes

- `CON-681` admits a road only on an empty connected edge and a settlement
  only on an empty intersection at least two edges from every settlement or
  city and connected to the builder's road. A city must replace one's own
  settlement.
- `CON-682` requires exact typed resource costs and a piece still in the
  player's supply; a bought development card needs a nonempty deck.
- `CON-683` permits the 3:1 or specific 2:1 bank ratio only while the player
  owns a settlement or city at the relevant harbour; otherwise 4:1 remains.
- `CON-684` permits at most one knight or progress development card on a turn,
  disallows playing a card bought that turn, and treats winning-point reveal
  as the printed exception.

### Information Genes

- `INF-002` leaves the next dice result and drawn development-card identity
  unpreviewed; this differs from already-hidden current cards.
- `INF-003` covers the shuffled deck order and opponents' currently held
  resource and development identities. A visible card count is not identity.
- `INF-384` exposes the shared hex numbers, roads, buildings, harbours,
  piece reserves and visible points while each player's hand remains private.

### Objective and Time Genes

- `OBJ-219` ends the contest at ten or more victory points on the scoring
  player's own turn, including buildings, bonuses and hidden victory-point
  cards revealed to substantiate the claim. Visible points alone can be below
  the threshold before reveal.
- `TIM-004` alternates active turns around the table without a turn clock.

## Reproducible transitions

| Before | Action | Rule-bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Red settlement touches numbered pasture; red city touches numbered grain | Roll that number | Red takes one wool and two grain unless blocked or a bank shortage prevents an owed type | Production follows pieces and numbers, not land ownership | CAT-003 |
| Active player rolls seven; another has nine resources | Each over-limit player selects the required floor-half discard, then active player moves robber and selects a legal victim | No hex produces; a randomly taken victim card is transferred if eligible | Seven is a distinct interruption, not a normal productive roll | CAT-004 |
| Red has four matching wool but no harbour | Offer the set to the bank for ore | Red receives one ore at 4:1; a 2:1 wool claim is illegal without its specific harbour | Bank rate is a spatially gated exchange | CAT-005 |
| Red has brick and lumber and an empty connected edge | Build a road | Cards return to bank and one red road occupies that edge | Construction spends resources and extends later settlement reach | CAT-006 |
| Red has a legal empty vertex beside a settlement | Attempt to build there | Rejected by the distance rule even if red could pay | Spatial legality is independent of affordability | CAT-006 |
| Red holds ore, wool and grain and the development deck is nonempty | Buy its top card, then try to play it immediately | Card identity is drawn hidden; a new knight or progress card cannot be played this turn | Purchase, uncertainty and timing are separate | CAT-007 |
| Red's valid connected road first reaches five edges | Re-evaluate road lengths | Red takes Longest Road and two points; a later longer rival road can take them | Score has transferable spatial control | CAT-008 |
| Red holds eight visible points and two concealed victory-point cards on their turn | Reveal both and claim ten | Red wins; the same total reached during another player's turn waits until red's turn | Own-turn threshold is the terminal rule | CAT-009 |

## Strategic and experiential structure

- The fixed number tiles make settlement placement an investment in future
  roll opportunities. A city amplifies a productive intersection but cannot
  create a new one; a road alone earns no point yet grants geographic reach.
- Exchange addresses resource mismatch. A harbour can improve bank rates,
  but opponents can decline domestic offers; no assumed trade is guaranteed.
- Hidden hands and development cards create uncertainty even though the
  terrain, costs and buildings are public. The robber can interrupt a high-yield
  hex and create short-term hand-risk from holding more than seven cards.
- Longest Road and Largest Army are two-point swings, not permanent unlocks.
  A route can be broken by a legal opposing settlement; exact route count
  must be recalculated before treating those points as secure.

## Replay and variation

- Dice, shuffled card order, offers accepted by rivals, robber choice and
  placement order change the contest despite the fixed beginner board.
- The fixed starting map controls setup variation for this packet; it does not
  eliminate stochastic production or private information.

## Adjacent systems and history

- Carcassonne also contests a growing tabletop landscape, but its tile draw
  and follower-majority scoring do not contain numbered shared production,
  tradable resource hands or a ten-point race. CATAN does not place a new
  terrain tile every turn.
- Civilization VI has settlement geography and resource-driven expansion,
  but its digital city production, research and military orders belong to a
  different scoped turn loop; no civilisation-wide subsystem is imported.

## Normalised genome

| Type | IDs | Boundary |
|---|---|---|
| Action | ACT-513–ACT-518 | domestic and bank exchange, construction, development purchase/play, robber choice |
| System | SYS-004, SYS-1024–SYS-1027 | chance, shared production, seven, card effects, transferable bonuses |
| Constraint | CON-681–CON-684 | geometry, cost/supply, harbour rights, development timing |
| Information | INF-002, INF-003, INF-384 | future chance, current concealed cards, public board/private hand |
| Objective | OBJ-219 | claim ten points on own turn |
| Time | TIM-004 | alternating active players |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `376` (`GAME-0001`–`GAME-0376`).
- Exact genome matches: none.
- Tied near matches: `GAME-0369` — Carcassonne (`3 / 32 = 0.093750`).
- Supported combination subsets: none.
- Scan date: 2026-09-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0369` — Carcassonne | `SYS-004`, `INF-002`, `TIM-004` | Both are physical alternating contests with random future events. Carcassonne draws and matches terrain tiles, then claims connected features with followers for majority and final field score. CATAN starts with fixed numbered terrain, negotiates hidden resource hands, builds paid roads and settlements, and races to ten points on the active player's turn. | Near, `0.093750` |

### Preserved research notes

- New genes: `ACT-513`–`ACT-518`, `SYS-1024`–`SYS-1027`,
  `CON-681`–`CON-684`, `INF-384`, `OBJ-219`.
- Classification result: new genes for a bounded physical resource contest.
- Evidence and reasoning: production tied to numbered hexes and adjacent
  buildings, voluntary card exchange, spatial construction and a turn-gated
  point race form one coupled loop.

## Taxonomy impact

- Registry changes: add sixteen bounded genes; no predecessor signature is
  changed merely to increase apparent similarity.
- Taxonomy-change record: `TAXONOMY_CHANGE_116`.

## Negative results

- No combination is accepted from hex geometry or genre alone. The generated
  proper-subset scan decides support.

## Delta summary

## New facts

- [Confirmed | Direct | High] CATAN's fixed beginner board supports a complete
  four-player race from two initial settlements each to an own-turn ten-point
  declaration under the publisher's base rules.

## New genes

- [Confirmed | Direct | High] Sixteen new boundaries distinguish the resource
  exchange, construction, production, robber, development and score loop.

## New combinations

- [Observation | Direct | High] No theme-derived combination is admitted.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_116` records the additions.

## New questions

- A direct four-person physical replication should sample bank-shortage and
  road-interruption edge cases and confirm the exact printing in hand.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0378` Super Monkey Ball 2, the final
  selected genre-contrast unit.
- Optimisation criterion: switch from negotiated tabletop turns to inertial
  real-time stage navigation.
- Expected information gain: test slope control, momentum, hazards and a
  bounded goal gate against existing rolling and platform genes.
- Backlog impact: no predecessor signature is revised.

## Why this game

- [Hypothesis | Limited | Medium] Its shared dice production and negotiated
  resource exchange contrast directly with the prior solo size-growth stage.
