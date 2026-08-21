---
game_id: GAME-0123
slug: inscryption
game_title: Inscryption
analysis_status: reviewed
reviewed: 2026-08-18
combination_ids:
  - COMB-0121
gene_ids:
  action:
    - ACT-085
    - ACT-087
    - ACT-126
    - ACT-127
    - ACT-128
    - ACT-129
    - ACT-130
    - ACT-131
    - ACT-135
    - ACT-136
    - ACT-137
    - ACT-138
  system:
    - SYS-004
    - SYS-112
    - SYS-166
    - SYS-167
    - SYS-168
    - SYS-172
    - SYS-173
    - SYS-174
    - SYS-175
  constraint:
    - CON-043
    - CON-136
    - CON-176
    - CON-177
    - CON-178
    - CON-180
    - CON-181
    - CON-182
    - CON-183
  information:
    - INF-002
    - INF-003
    - INF-009
    - INF-062
  objective:
    - OBJ-057
    - OBJ-058
  time:
    - TIM-002
    - TIM-005
---

# Game: Inscryption

## Analysis scope

- Version / ruleset: released base game, fresh-save Act I in Leshy's cabin,
  from the first tutorial run through obtaining the film roll, defeating Leshy
  with it available and exposing the New Game card.
- Included: the main and Squirrel decks; visible hand; Blood sacrifices, Bones,
  Power, Health and Sigils; four paired combat lanes; queued opponent cards;
  the damage scale; items; generated maps and connected node choices; card
  rewards, upgrades, removals, Totems, pelts and Teeth; candles; Deathcards;
  persistent cabin mechanisms and the required film-roll puzzle chain.
- Excluded: Acts II and III, the finale, lore interpretation, video records,
  ARG material, Kaycee's Mod, challenges, starter-deck variants, post-game
  unlocks, achievements and card-balance analysis outside the ordinary Act I
  progression gates.
- Direct-play status: not conducted for this record. The official product page
  establishes the deliberately combined deckbuilding and escape-room scope;
  the bounded rules below are corroborated by maintained specialist reference
  records for Act I, card battles, the cabin, events and Deathcards.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `INS-001` | Inscryption combines a deckbuilding roguelike with escape-room-style puzzles, and Act I places both systems in Leshy's cabin | Confirmed | Corroborated | High | P1, S1, S6 |
| `INS-002` | Every ordinary Act I battle starts with three main-deck cards and one Squirrel, then each later player turn draws from either the main or Squirrel deck | Confirmed | Corroborated | High | S2, S3 |
| `INS-003` | A held creature is played into one of four open friendly lanes after its free, Blood or Bone cost is satisfied | Confirmed | Corroborated | High | S2, S3, S4 |
| `INS-004` | Blood payment removes a player-selected sufficient set of eligible friendly creatures, while each ordinary friendly death or sacrifice produces a Bone | Confirmed | Corroborated | High | S4, S5 |
| `INS-005` | Ringing the bell commits the player's phase; friendly creatures attack left to right, queued opposing cards advance, and opposing creatures then attack | Confirmed | Corroborated | High | S2, S3 |
| `INS-006` | An unblocked attack tips a shared scale, and a five-point net advantage ends the battle | Confirmed | Corroborated | High | S2, S3 |
| `INS-007` | The Act I route exposes connected node categories and ends each generated area at a fixed boss while the deck, items, Teeth and modifiers persist between nodes | Confirmed | Corroborated | High | S1, S7, S8 |
| `INS-008` | Map events can add, remove, strengthen or merge card properties, create Totems, provide consumables, and exchange Teeth for pelts and pelts for cards | Confirmed | Corroborated | High | S7, S8, S9 |
| `INS-009` | Losing a battle consumes a candle; losing without another candle ends the run, while boss progression can restore the candle stock | Confirmed | Corroborated | Medium | S1, S10 |
| `INS-010` | Run failure clears ordinary run state but can retain solved cabin mechanisms, staged rule unlocks and player-composed Deathcards | Confirmed | Corroborated | High | S6, S10 |
| `INS-011` | A Deathcard is composed from sampled cost, statistics and Sigils and may appear in later Act I card offers | Confirmed | Corroborated | High | S10 |
| `INS-012` | The cabin's authored mechanism chain reveals the film roll, which changes the post-Leshy camera outcome and permits Act I completion | Confirmed | Corroborated | High | S6, S11 |
| `INS-013` | Act I therefore couples two mechanically necessary progress loops: repeated deckbuilding routes and persistent cabin-puzzle state | Observation | Corroborated | High | INS-007–INS-012 |
| `INS-014` | At Atlas resolution Inscryption is related to Slay the Spire through persistent-deck route progression, but its sacrifice economy, paired lanes, chosen draw source, damage scale and cross-run cabin state are distinct | Observation | Corroborated | High | INS-002–INS-013, GAME-0120 |

## Basic data

- Release / origin: Daniel Mullins Games, published by Devolver Digital on
  19 October 2021.
- Platform or physical form: first-person single-player digital card adventure
  with a manipulable three-dimensional cabin between tabletop encounters.
- Puzzle family: tactical forecast and counterplay; inventory and fixture
  dependencies; loop retention; ordered dependency sequencing.
- Primary source:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/1092790/Inscryption/),
    release metadata and the creator-approved description of the deckbuilding
    roguelike, escape-room puzzle and horror blend.
- Secondary specialist sources:
  - **[S1]** [Inscryption Wiki: Act I](https://inscryption.fandom.com/wiki/Act_I),
    cabin setting, branching areas, event route and boss order.
  - **[S2]** [Inscryption Wiki: Card Battle](https://inscryption.fandom.com/wiki/Card_Battle),
    opening draw, player draw choice, bell timing, attack order and scale end.
  - **[S3]** [Inscryption Wiki: Cards](https://inscryption.fandom.com/wiki/Cards),
    Power, Health, costs, lane attacks and direct scale damage.
  - **[S4]** [Inscryption Wiki: Blood](https://inscryption.fandom.com/wiki/Blood),
    pending-card sacrifice selection, Blood value and legality.
  - **[S5]** [Inscryption Wiki: Bones](https://inscryption.fandom.com/wiki/Bones),
    friendly death and sacrifice conversion into Bone payment.
  - **[S6]** [Inscryption Wiki: Leshy's Cabin](https://inscryption.fandom.com/wiki/Leshy%27s_Cabin),
    persistent escape-room mechanisms and film-roll reveal.
  - **[S7]** [Inscryption Wiki: Events](https://inscryption.fandom.com/wiki/Events),
    non-combat node effects, consumables, card modification and Totems.
  - **[S8]** [Inscryption Wiki: Act I map](https://inscryption.fandom.com/wiki/Map),
    generated connected node categories and current-run progression.
  - **[S9]** [Inscryption Wiki: Teeth](https://inscryption.fandom.com/wiki/Teeth),
    overkill Teeth and the pelt economy.
  - **[S10]** [Inscryption Wiki: Deathcard](https://inscryption.fandom.com/wiki/Deathcard),
    terminal run creation sequence and future-run card availability.
  - **[S11]** [Inscryption Wiki: Leshy](https://inscryption.fandom.com/wiki/Leshy),
    final battle and the film-roll-dependent post-battle outcomes.
- Claim IDs: `INS-001`–`INS-014`.

## Mechanical decomposition

### Action Genes

- `ACT-135` places one held creature into one chosen open friendly lane after
  its current cost is payable.
- `ACT-136` makes Blood a board-state decision: the player chooses which
  eligible friendly creatures fund the pending card rather than spending an
  abstract replenishing Energy pool.
- `ACT-137` selects the main deck or Squirrel side deck for the ordinary
  start-of-turn draw.
- `ACT-126` rings the bell and commits any remaining placement opportunity so
  both sides' ordered attacks and queue movement can resolve.
- `ACT-127` chooses one visibly connected successor map node.
- `ACT-128` accepts one offered card into the persistent run deck; some Act I
  offers are mandatory-choice instances of this boundary.
- `ACT-129` covers persistent campfire strengthening, Sigil transfer, duplicate
  fusion and removal from the current run deck.
- `ACT-130` exchanges Teeth for pelts and pelts for offered cards through the
  bounded Trapper / Trader economy.
- `ACT-131` consumes one of at most three held immediate-effect items during a
  legal player phase.
- `ACT-138` composes a named Deathcard from sampled cost, statistics and Sigils
  after terminal failure.
- `ACT-085` manipulates authored cabin mechanisms such as the safe, sliding
  cabinet and clock; `ACT-087` applies acquired cabin objects to compatible
  fixtures in the film-roll dependency chain.
- Claim IDs: `INS-002`–`INS-004`, `INS-007`–`INS-012`.

### System Behaviour Genes

- `SYS-172` resolves active creatures left to right against paired cards or the
  shared scale; `SYS-174` first advances disclosed hostile cards from their
  queued back row when the corresponding active lane permits entry.
- `SYS-173` converts ordinary friendly death or Blood sacrifice into Bones.
- `SYS-166` triggers persistent Totem, boon and other run modifiers at their
  declared events.
- `SYS-167` carries the mutable deck, items, Teeth, pelts and modifiers across
  resolved route nodes; `SYS-168` generates each finite branching area ending
  at its boss.
- `SYS-004` selects variable route, reward, event and encounter outcomes that
  have not yet become fixed disclosed state.
- `SYS-112` exposes downstream cabin items when the accepted authored mechanism
  state is satisfied, including the film roll behind the clock chain.
- `SYS-175` resets failed-run state while preserving the declared cabin,
  staged-progression and Deathcard metaprogression.
- Resolution order in combat: draw from the chosen pile; sacrifice and place
  any legal creatures; optionally consume items; ring bell; resolve friendly
  lanes; advance eligible opponent queue cards; resolve opponent lanes; test
  the scale; begin the next draw step if neither side has won.
- Claim IDs: `INS-002`–`INS-013`.

### Constraint Genes

- `CON-180` requires both an open friendly lane and complete free, Blood or Bone
  payment before a creature enters play; `CON-181` specifically requires a
  sufficient selected sacrifice value for Blood.
- `CON-182` fixes four mutually exclusive active lanes per side and pairs
  ordinary attack relationships by lane index.
- `CON-043` bounds the visible hand and ordinary one-card commit.
- `CON-178` makes the current persistent run deck the main combat draw supply.
- `CON-176` limits travel to visible outgoing route edges.
- `CON-177` caps the carried consumable inventory at three slots.
- `CON-183` uses the finite candle stock to distinguish a recoverable encounter
  loss from terminal run failure.
- `CON-136` orders the persistent cabin mechanism prerequisites that eventually
  expose the film roll.
- Scarce strategic resources: open lanes, sacrifice bodies, Bones, cards in
  each draw pile, item slots, candles, Teeth, pelts and the quality / size of
  the persistent run deck.
- Claim IDs: `INS-002`–`INS-012`.

### Information Genes

- `INF-003` covers the concealed current order of both draw piles and the
  authored contents behind unopened cabin mechanisms.
- `INF-009` exposes Leshy's queued card identities and assigned lanes before
  they advance and attack, allowing positional counterplay.
- `INF-062` exposes connected route edges and node categories before travel,
  while node-specific rewards or encounters may remain unknown.
- `INF-002` captures those unpreviewed future route, reward and event outcomes
  before the seeded system resolves them into current state.
- `INF-001` is absent: the board and hostile queue are visible, but concealed
  deck order and unopened cabin state remain decision-relevant.
- Claim IDs: `INS-002`, `INS-005`, `INS-007`, `INS-012`.

### Objective Genes

- `OBJ-057` wins an ordinary card encounter by tipping the relative scale five
  points toward the player before Leshy reaches the opposing margin.
- `OBJ-058` completes the scoped chapter only when the player solves the
  film-roll chain, reaches and defeats Leshy, then obtains the successful
  camera outcome that exposes the New Game card.
- Success, evaluation and failure: a battle ends at either five-point scale
  margin. A loss may consume a candle; loss with none remaining resets the
  run. Beating Leshy without the film roll deliberately does not satisfy the
  scoped chapter objective.
- Claim IDs: `INS-006`, `INS-009`, `INS-012`.

### Time Genes

- `TIM-005` structures each battle as a flexible player placement / item phase
  followed by committed friendly and hostile resolution after the bell.
- `TIM-002` leaves cabin inspection and mechanism manipulation self-paced
  between tabletop commits.
- Claim IDs: `INS-005`, `INS-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Opening hand contains a Squirrel and a one-Blood creature; one friendly lane is open | Start the creature play, select the Squirrel as sacrifice and choose the open lane | Squirrel leaves play, one Bone is granted and the creature occupies the chosen lane | Blood selection, death conversion and lane placement are coupled but distinct | `INS-003`, `INS-004` |
| A Bone-cost creature is held but the Bone pool is below its cost | Try to place it | Placement is rejected without sacrificing another creature | accumulated Bones and pending Blood sacrifice are different payment systems | `INS-003`, `INS-004` |
| Player turn begins with both decks non-empty | Select the Squirrel deck | its concealed top Squirrel enters the hand; no main-deck card is drawn | draw-source choice is an Action, not an automatic full-hand refill | `INS-002` |
| A friendly creature faces an opposing creature in the same lane | Ring the bell | friendly Power reduces that card's Health rather than tipping the scale | lane opposition intercepts ordinary direct damage | `INS-005`, `INS-006` |
| A friendly creature has no opposing card | Ring the bell | its Power tips the shared scale toward the player | scale progress comes only from unblocked direct damage, subject to Sigils | `INS-005`, `INS-006` |
| A disclosed hostile card waits behind an open opposing active lane | Ring the bell and finish friendly attacks | the queued card advances into that same lane before the hostile attack phase | queued intent is visible current state and preserves its lane relation | `INS-005` |
| Current route node has two visible outgoing edges | Choose one successor | the other branch becomes inaccessible and the chosen category resolves | map choice is constrained by the disclosed graph | `INS-007` |
| A campfire has already granted its safe first increase | Risk the same selected card again | it either gains the next declared increase or is removed from the run deck | persistent card improvement can trade deck value for removal risk | `INS-008` |
| Last candle remains and the scale reaches Leshy's winning margin | Resolve defeat | the run ends, the player composes a Deathcard and a new route begins with retained metaprogression | failure resets run state but is not a clean save reset | `INS-009`–`INS-011` |
| Cabin clock chain is incomplete | Manipulate its final fixture without the required prior state | film-roll compartment remains unavailable | authored prerequisite state gates the progress item | `INS-012` |
| Film roll is owned when Leshy is defeated | Take the post-battle camera | the film changes the outcome and the New Game card becomes accessible | boss victory alone is insufficient for Act I completion | `INS-012` |

## Strategic and experiential structure

- Local decision: decide whether to draw a guaranteed sacrifice body or risk a
  stronger concealed main-deck card, then allocate scarce lanes and sacrifice
  bodies against Leshy's disclosed queue.
- Medium-term planning: preserve low-cost deployment, Bone generation, Sigil
  synergies and item capacity while editing the deck across route nodes.
- Long-term structure: route choices build a boss-capable deck, while repeated
  failures and cabin investigation unlock the separate prerequisites required
  to turn a Leshy victory into chapter completion.
- Common heuristics: count open lanes before sacrificing; compare immediate
  scale pressure with blocking; read the opposing queue; avoid bloating the
  persistent deck; use the Squirrel draw when a known Blood body matters more
  than an unknown main-deck top card; revisit changed cabin mechanisms.
- Failure attribution: the current board, queued enemy cards and route edges
  are legible, but concealed draws and random offers create variance. Persistent
  cabin state and Deathcards make failure informative rather than identical
  repetition.
- Player-trust factors: sacrifice eligibility, Bone credit, left-to-right order,
  Sigil exceptions, queue movement, scale arithmetic and cross-run persistence
  must remain consistent across ordinary and boss encounters.
- Claim IDs: `INS-002`–`INS-014`.

## Replay and variation

- What changes between runs: generated route, encounter and reward contents,
  offered cards, deck edits, items, Teeth, pelts, Totems and created Deathcards.
- What persists: authored rule unlocks, solved cabin mechanisms, some puzzle
  rewards and the eligible Deathcard pool.
- Randomness or procedural generation: route and offers vary, but currently
  revealed board, queue, costs and mechanism dependencies resolve by fixed
  rules.
- Multiple viable strategies: sacrifice tempo, Bone-heavy decks, airborne or
  multi-lane pressure, defensive blocking, Totem engines, lean decks and strong
  Deathcards can all support completion.
- Typical replay motive: mandatory recovery after failure, experimentation with
  a new deck route, stronger Deathcard construction and later Kaycee's Mod,
  which remains outside this record.
- Claim IDs: `INS-007`–`INS-013`.

## Adjacent systems and history

- Slay the Spire shares a generated disclosed route, persistent run deck,
  offered card acquisition, card modification, limited consumables and a
  committed hostile phase. Inscryption replaces renewable Energy and
  persistent player Health with board sacrifices, Bones, paired lanes, a
  relative scale and candles, and adds required cabin-puzzle metaprogression.
- Fights in Tight Spaces shares a card-planning phase and exact hostile preview,
  but its cards command one spatial agent rather than becoming persistent lane
  combatants.
- The Room shares persistent authored fixture dependencies, while Inscryption
  embeds a smaller mechanism chain inside a repeated deckbuilding run rather
  than making enclosure manipulation the complete ruleset.
- Balatro shares a visible bounded hand and concealed deck order, but evaluates
  selected multi-card patterns into score instead of paying sacrifice costs to
  deploy creatures into adversarial lanes.
- Claim IDs: `INS-001`, `INS-013`, `INS-014`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-085`, `ACT-087`, `ACT-126`, `ACT-127`, `ACT-128`, `ACT-129`, `ACT-130`, `ACT-131`, `ACT-135`, `ACT-136`, `ACT-137`, `ACT-138` | lane, payment, draw-source, route, deck-edit, item, cabin and Deathcard parameters |
| System Behaviour | `SYS-004`, `SYS-112`, `SYS-166`, `SYS-167`, `SYS-168`, `SYS-172`, `SYS-173`, `SYS-174`, `SYS-175` | combat order, scale, queue, Bones, route and cross-run persistence |
| Constraint | `CON-043`, `CON-136`, `CON-176`, `CON-177`, `CON-178`, `CON-180`, `CON-181`, `CON-182`, `CON-183` | hand, fixture, route, item, deck, payment, lanes and candles |
| Information | `INF-002`, `INF-003`, `INF-009`, `INF-062` | concealed draws, hostile queue, route and future offers |
| Objective | `OBJ-057`, `OBJ-058` | battle margin and film-roll-gated chapter completion |
| Time | `TIM-002`, `TIM-005` | self-paced cabin and committed combat phases |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-085,ACT-087,ACT-126,ACT-127,ACT-128,ACT-129,ACT-130,ACT-131,ACT-135,ACT-136,ACT-137,ACT-138; SYS-004,SYS-112,SYS-166,SYS-167,SYS-168,SYS-172,SYS-173,SYS-174,SYS-175; CON-043,CON-136,CON-176,CON-177,CON-178,CON-180,CON-181,CON-182,CON-183; INF-002,INF-003,INF-009,INF-062; OBJ-057,OBJ-058; TIM-002,TIM-005`.
- Indexed games scanned: 123, including this record.
- Indexed combinations scanned: 121.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0120` — Slay the Spire at
  `18 / 49 = 0.367347`.
- Supported combination subsets: `COMB-0121`.
- Scan date: 2026-08-18.

### Full prior-game Jaccard scan

- `GAME-0001`: `2 / 50 = 0.040000`; `GAME-0002`: `1 / 44 = 0.022727`; `GAME-0003`: `1 / 46 = 0.021739`; `GAME-0004`: `1 / 52 = 0.019231`.
- `GAME-0005`: `1 / 44 = 0.022727`; `GAME-0006`: `1 / 46 = 0.021739`; `GAME-0007`: `1 / 45 = 0.022222`; `GAME-0008`: `1 / 44 = 0.022727`.
- `GAME-0009`: `2 / 52 = 0.038462`; `GAME-0010`: `0 / 47 = 0.000000`; `GAME-0011`: `1 / 50 = 0.020000`; `GAME-0012`: `1 / 46 = 0.021739`.
- `GAME-0013`: `0 / 51 = 0.000000`; `GAME-0014`: `2 / 51 = 0.039216`; `GAME-0015`: `1 / 51 = 0.019608`; `GAME-0016`: `1 / 52 = 0.019231`.
- `GAME-0017`: `2 / 49 = 0.040816`; `GAME-0018`: `2 / 55 = 0.036364`; `GAME-0019`: `0 / 48 = 0.000000`; `GAME-0020`: `1 / 51 = 0.019608`.
- `GAME-0021`: `0 / 47 = 0.000000`; `GAME-0022`: `0 / 50 = 0.000000`; `GAME-0023`: `1 / 47 = 0.021277`; `GAME-0024`: `1 / 49 = 0.020408`.
- `GAME-0025`: `0 / 49 = 0.000000`; `GAME-0026`: `0 / 50 = 0.000000`; `GAME-0027`: `0 / 50 = 0.000000`; `GAME-0028`: `2 / 53 = 0.037736`.
- `GAME-0029`: `0 / 50 = 0.000000`; `GAME-0030`: `0 / 52 = 0.000000`; `GAME-0031`: `0 / 49 = 0.000000`; `GAME-0032`: `0 / 49 = 0.000000`.
- `GAME-0033`: `0 / 51 = 0.000000`; `GAME-0034`: `0 / 52 = 0.000000`; `GAME-0035`: `0 / 56 = 0.000000`; `GAME-0036`: `1 / 49 = 0.020408`.
- `GAME-0037`: `0 / 47 = 0.000000`; `GAME-0038`: `0 / 54 = 0.000000`; `GAME-0039`: `1 / 46 = 0.021739`; `GAME-0040`: `1 / 45 = 0.022222`.
- `GAME-0041`: `0 / 49 = 0.000000`; `GAME-0042`: `0 / 47 = 0.000000`; `GAME-0043`: `0 / 52 = 0.000000`; `GAME-0044`: `0 / 48 = 0.000000`.
- `GAME-0045`: `0 / 52 = 0.000000`; `GAME-0046`: `1 / 47 = 0.021277`; `GAME-0047`: `4 / 48 = 0.083333`; `GAME-0048`: `0 / 52 = 0.000000`.
- `GAME-0049`: `1 / 46 = 0.021739`; `GAME-0050`: `0 / 53 = 0.000000`; `GAME-0051`: `2 / 52 = 0.038462`; `GAME-0052`: `0 / 48 = 0.000000`.
- `GAME-0053`: `0 / 47 = 0.000000`; `GAME-0054`: `0 / 49 = 0.000000`; `GAME-0055`: `0 / 48 = 0.000000`; `GAME-0056`: `0 / 46 = 0.000000`.
- `GAME-0057`: `0 / 46 = 0.000000`; `GAME-0058`: `0 / 47 = 0.000000`; `GAME-0059`: `0 / 45 = 0.000000`; `GAME-0060`: `0 / 45 = 0.000000`.
- `GAME-0061`: `1 / 47 = 0.021277`; `GAME-0062`: `1 / 45 = 0.022222`; `GAME-0063`: `1 / 44 = 0.022727`; `GAME-0064`: `1 / 42 = 0.023810`.
- `GAME-0065`: `2 / 43 = 0.046512`; `GAME-0066`: `2 / 46 = 0.043478`; `GAME-0067`: `2 / 44 = 0.045455`; `GAME-0068`: `2 / 44 = 0.045455`.
- `GAME-0069`: `1 / 45 = 0.022222`; `GAME-0070`: `0 / 46 = 0.000000`; `GAME-0071`: `1 / 44 = 0.022727`; `GAME-0072`: `1 / 45 = 0.022222`.
- `GAME-0073`: `1 / 44 = 0.022727`; `GAME-0074`: `1 / 46 = 0.021739`; `GAME-0075`: `1 / 46 = 0.021739`; `GAME-0076`: `1 / 44 = 0.022727`.
- `GAME-0077`: `1 / 44 = 0.022727`; `GAME-0078`: `1 / 44 = 0.022727`; `GAME-0079`: `1 / 44 = 0.022727`; `GAME-0080`: `1 / 44 = 0.022727`.
- `GAME-0081`: `1 / 45 = 0.022222`; `GAME-0082`: `1 / 45 = 0.022222`; `GAME-0083`: `1 / 45 = 0.022222`; `GAME-0084`: `1 / 47 = 0.021277`.
- `GAME-0085`: `6 / 43 = 0.139535`; `GAME-0086`: `5 / 46 = 0.108696`; `GAME-0087`: `2 / 46 = 0.043478`; `GAME-0088`: `2 / 45 = 0.044444`.
- `GAME-0089`: `1 / 46 = 0.021739`; `GAME-0090`: `2 / 51 = 0.039216`; `GAME-0091`: `0 / 47 = 0.000000`; `GAME-0092`: `0 / 48 = 0.000000`.
- `GAME-0093`: `2 / 45 = 0.044444`; `GAME-0094`: `0 / 48 = 0.000000`; `GAME-0095`: `0 / 50 = 0.000000`; `GAME-0096`: `0 / 48 = 0.000000`.
- `GAME-0097`: `0 / 46 = 0.000000`; `GAME-0098`: `0 / 45 = 0.000000`; `GAME-0099`: `0 / 46 = 0.000000`; `GAME-0100`: `0 / 49 = 0.000000`.
- `GAME-0101`: `1 / 47 = 0.021277`; `GAME-0102`: `1 / 44 = 0.022727`; `GAME-0103`: `0 / 47 = 0.000000`; `GAME-0104`: `0 / 47 = 0.000000`.
- `GAME-0105`: `0 / 48 = 0.000000`; `GAME-0106`: `1 / 44 = 0.022727`; `GAME-0107`: `1 / 45 = 0.022222`; `GAME-0108`: `1 / 47 = 0.021277`.
- `GAME-0109`: `2 / 52 = 0.038462`; `GAME-0110`: `0 / 46 = 0.000000`; `GAME-0111`: `4 / 41 = 0.097561`; `GAME-0112`: `0 / 46 = 0.000000`.
- `GAME-0113`: `0 / 52 = 0.000000`; `GAME-0114`: `0 / 45 = 0.000000`; `GAME-0115`: `1 / 43 = 0.023256`; `GAME-0116`: `0 / 44 = 0.000000`.
- `GAME-0117`: `1 / 45 = 0.022222`; `GAME-0118`: `0 / 54 = 0.000000`; `GAME-0119`: `0 / 61 = 0.000000`; `GAME-0120`: `18 / 49 = 0.367347`.
- `GAME-0121`: `0 / 61 = 0.000000`; `GAME-0122`: `0 / 53 = 0.000000`.

Near matches are selected by the canonical positive-maximum rule. Slay the
Spire is the unique maximum; the lower-scoring adventure-puzzle records share
only the authored cabin-fixture substrate rather than the combat loop.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0120` — Slay the Spire | `ACT-126`–`ACT-131`, `SYS-004`, `SYS-166`–`SYS-168`, `CON-043`, `CON-176`–`CON-178`, `INF-002`, `INF-003`, `INF-062`, `TIM-005` | Slay the Spire pays renewable Energy for immediate card effects against intent-previewed enemies; Inscryption pays Blood by removing friendly lane creatures, accrues Bones from death, resolves paired-lane entities against a relative scale and gates Act I through candles plus cabin mechanisms | Unique near match |

## Combination record

- Registered [`COMB-0121`](../../combinations/COMB-0121.md), the only current
  proper registered subset of this complete genome.
- The combination isolates chosen draw source, sacrifice payment, Bones,
  disclosed hostile queue, persistent paired lanes and scale victory; route,
  deck services, items, cabin puzzles and Deathcards remain outside it.

## Taxonomy impact

- Registry changes: four Action, four System Behaviour, four Constraint and two
  Objective genes admitted as Active.
- Taxonomy-change record: none; existing Slay the Spire and The Room genes are
  reused where their established boundaries fit.
- Candidate terms affected: creature-lane card play, Blood sacrifice payment,
  chosen draw pile, damage scale, candle stock and cross-run Deathcard retention.

## Negative results

- `INF-001` rejected because concealed draw order and unopened cabin state are
  decision-relevant current state.
- `ACT-125` and `SYS-163` rejected because Act I creature cards become
  persistent lane entities rather than immediate effect cards.
- `CON-094` rejected because Blood consumes selected board entities and Bones
  accumulate from death rather than one renewable per-turn pool.
- `CON-175` and `OBJ-029` rejected because defeat is governed by a recoverable
  candle stock and scale margin, not persistent Health or eliminating every
  hostile actor.
- `SYS-140` rejected because Act I preserves solved mechanisms and generated
  Deathcards, not only learned facts.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Act I couples sacrifice-funded paired-lane
  card combat with a persistent cabin-puzzle chain (`INS-001`–`INS-013`).
- [Observation | Corroborated | High] The closest genre neighbour does not
  collapse the new mechanics: Slay the Spire shares route deckbuilding but not
  Inscryption's board economy or chapter gate (`INS-014`).

## Нові гени

- [Observation | Corroborated | High] `ACT-135`–`ACT-138`, `SYS-172`–`SYS-175`,
  `CON-180`–`CON-183`, `OBJ-057` and `OBJ-058`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0121` — sacrifice-funded paired-
  lane card combat with chosen draw source and disclosed hostile queue.

## Зміни таксономії

- [Observation | Corroborated | High] Змін меж наявних генів немає; додано
  нові механіки, які не вкладаються в Energy-card або effect-card boundaries.

## Нові питання

- Which independently analysed lane card battler will first reuse the paired-
  lane and scale genes without Inscryption's cabin metaprogression?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] Against the Storm.
- Optimisation criterion: continue the approved popular-game batch while
  contrasting finite settlement cycles with the open-ended city and factory
  systems already admitted.
- Expected information gain: settlement-wide hostility / impatience pressure,
  rotating orders, random blueprint offers and cross-settlement progression.
- Backlog impact: continues the approved nine-game local batch as `GAME-0124`.

## Чому саме вона

- [Hypothesis | Limited | High] Against the Storm should reuse live production
  and resource-network genes while testing whether its finite storm cycle and
  reputation race require new boundaries rather than another city-builder
  parameter set.
