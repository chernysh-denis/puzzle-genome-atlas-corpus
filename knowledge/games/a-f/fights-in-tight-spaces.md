---
game_id: GAME-0047
slug: fights-in-tight-spaces
game_title: Fights in Tight Spaces
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0047
gene_ids:
  action:
    - ACT-061
  system:
    - SYS-019
    - SYS-020
    - SYS-087
  constraint:
    - CON-001
    - CON-011
    - CON-043
    - CON-094
  information:
    - INF-001
    - INF-003
    - INF-009
  objective:
    - OBJ-029
    - OBJ-030
  time:
    - TIM-005
---

# Game: Fights in Tight Spaces

## Analysis scope

- Version / ruleset: released base game, standard campaign rules, scoped to an
  Ambassador-protection encounter in the first Death's Head Biker Gang chapter.
  The reproducible representative is the developer-documented pub scene with
  Agent 11, one yellow Ambassador and three biker enemies. Encounter order and
  placement vary between generated runs, so this is the earliest documented
  qualifying encounter family, not a guaranteed fixed node number.
- Included: visible grid and occupants; current six-card hand; draw/discard
  cycle; momentum costs; card-directed movement, attacks and repositioning;
  primed enemy attacks and displayed order; push/collision/friendly fire;
  end-turn enemy resolution; elimination success; Ambassador survival and its
  difficulty-dependent consequence.
- Excluded: ordinary encounters without an HVT, Informant encounters in which
  the protected character remains hostile, bosses, later chapters, route-map
  choice, deck acquisition and upgrades, injuries, events, daily/endless modes,
  Weapon of Choice and K9 Division DLC, score optimisation and cinematic replay.
- Direct-play status: not conducted. The product and HVT premise are direct;
  exact turn, hand, intent and protection rules are corroborated by contemporary
  hands-on reviews, developer material and reproducible player documentation.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FITS-001` | One encounter uses a fixed finite tile grid with Agent 11, enemies, barriers, exits and an Ambassador occupying exclusive positions | Confirmed | Corroborated | High | P1, P2, D1, S1 |
| `FITS-002` | The player's available commands are a bounded visible hand of cards whose legal target may be Agent 11, an enemy or a board position | Confirmed | Corroborated | High | P1, S1, S2 |
| `FITS-003` | Card play spends a shared momentum resource; unused cards are discarded and a new bounded hand is drawn for the next player turn | Confirmed | Corroborated | High | P1, S1, S3 |
| `FITS-004` | Enemies expose primed attacks, target geometry, effect and relative execution order before the player ends the turn | Confirmed | Corroborated | High | S1, S4, C1 |
| `FITS-005` | A primed surviving enemy automatically executes its committed attack during the enemy phase unless killed, stunned or otherwise cancelled | Confirmed | Corroborated | High | S1, S4, C1 |
| `FITS-006` | Card effects can move Agent 11 or an enemy and can push a target into a wall, a lethal boundary or another attack line | Confirmed | Corroborated | High | P1, S1, S2, S5 |
| `FITS-007` | Enemy attacks can hit other enemies or the Ambassador after the player changes occupancy without changing the committed attack | Confirmed | Corroborated | High | S2, D1, S5 |
| `FITS-008` | The ordinary encounter ends when the finite hostile set is incapacitated; Agent 11 defeat ends the run | Confirmed | Corroborated | High | S1, S3 |
| `FITS-009` | Keeping the Ambassador alive is an explicit protected-HVT outcome and yields campaign value, but standard-mode sources describe it as a bonus rather than universal encounter failure | Pattern | Conflicting | Medium | P1, S2, S5, C2 |
| `FITS-010` | On Brutal difficulty, Ambassador death is documented as terminal, so terminality is a difficulty parameter rather than part of the invariant base signature | Pattern | Limited | Medium | C2 |
| `FITS-011` | The game supports the intent-preview/disruption core of `COMB-0014` but not its per-mech allowance or shared-infrastructure objective | Observation | Corroborated | High | FITS-002–FITS-010, H1 |
| `FITS-012` | Slay the Spire-like hand turnover is coupled to a spatial target board and committed hostile phase rather than resolving only card-to-card combat | Observation | Corroborated | High | P1, S1, S3, H1 |

## Basic data

- Release / origin: Ground Shatter developed Fights in Tight Spaces; Mode 7
  published the Windows and Xbox release on 2 December 2021 after Early Access.
- Platform or physical form: single-player turn-based digital tactical
  deckbuilder on PC and consoles.
- Puzzle family: previewed positional card tactics with forced displacement and
  protected-character encounter variants.
- Primary and creator sources:
  - **[P1]** [Official Steam product page](https://store.steampowered.com/app/1265820/Fights_in_Tight_Spaces/),
    establishing deck construction, spatial control, environmental use and
    explicit high-value-target protection.
  - **[P2]** [Official PlayStation product page](https://www.playstation.com/en-gb/games/fights-in-tight-spaces/),
    corroborating the hand / momentum / positioning loop and HVT bodyguard role.
  - **[D1]** [James Vigor — developer portfolio](https://www.jamesvigor.co.uk/gamedev/fights-in-tight-spaces),
    documenting a representative pub encounter with Agent 11, three bikers and
    one protected Ambassador.
  - **[D2]** [Ground Shatter patch record](https://roadmap.groundshatter.com/home),
    documenting later-mission Ambassador health scaling and identifying these
    encounters as protect missions.
- Contemporary mechanical sources:
  - **[S1]** [GameSpot Early Access review](https://www.gamespot.com/reviews/fights-in-tight-spaces-early-access-review/1900-6417650/),
    based on ten hours of play and documenting the tile grid, hand, action
    points, primed attacks, attack overlays and end-turn hand turnover.
  - **[S2]** [Tech-Gaming preview](https://www.tech-gaming.com/fights-in-tight-spaces/),
    documenting weapon trajectories, enemy friendly fire and repositionable
    Ambassadors / Informants.
  - **[S3]** [PC Gamer review](https://www.pcgamer.com/fights-in-tight-spaces-review/),
    documenting energy costs, enemy action before a new random six-card hand
    and the spatial turn structure.
  - **[S4]** [GameSpot priming explanation](https://www.gamespot.com/reviews/fights-in-tight-spaces-early-access-review/1900-6417650/),
    documenting attack ranges, primed-state tooltips and behavioural updates.
  - **[S5]** [Finger Guns review](https://fingerguns.net/reviews/2021/12/02/fights-in-tight-spaces-review-pc-deck-em-deck-builder/),
    corroborating end-turn danger, friendly fire and protected NPC variants.
- Reproducible community documentation:
  - **[C1]** [Speedrun.com mechanics guide](https://www.speedrun.com/fights_in_tight_spaces/guides/s4j6e),
    documenting visible enemy execution order, stable attack patterns and the
    end-turn boundary.
  - **[C2]** [Steam-derived core-mechanics guide](https://steamah.com/fights-in-tight-spaces-tips-tricks-core-mechanics/),
    used narrowly for hand refresh and the distinction between Ambassador and
    hostile Informant protection; terminality remains mode-sensitive.
  - **[H1]** [Xbox Wire design account](https://news.xbox.com/en-us/?p=145986),
    creator/publisher context for the physical-board prototype and the explicit
    Slay the Spire / Into the Breach synthesis.
- Claim IDs: `FITS-001`–`FITS-012`.

## Mechanical decomposition

### Action Genes

- `ACT-061` — play held spatial action card. The player selects one visible
  card and its legal unit or cell target; the card may move Agent 11, attack,
  block, counter or reposition another occupant. One card is one command, even
  when it combines movement and attack effects.
- `ACT-019` is absent. Agent 11 does not select one persistent unit's fixed
  move/ability menu; the currently drawn card is the ability token and is
  consumed on play.
- `ACT-014` and `ACT-008` are absent. Movement is neither a remote free piece
  relocation nor an invariant local navigation verb: it requires an eligible
  held card and may be embedded in a compound attack.
- Claim IDs: `FITS-002`, `FITS-003`, `FITS-006`.

### System Behaviour Genes

- `SYS-019` — ordered execution of committed hostile intents. After the player
  ends the phase, surviving primed enemies resolve in the displayed order
  against then-current occupancy. Death or stun cancels an execution; moving a
  different body into the line does not make the attacker choose a new action.
- `SYS-020` — attack-induced displacement and collision resolution. Push cards
  shift targets and apply wall, occupant or lethal-boundary consequences.
- `SYS-087` — turn-boundary hand turnover. Played and unplayed cards enter the
  discard flow; the next player phase receives a new bounded hand from the
  current deck, with draw-pile recycling when required.
- Resolution order: establish / update enemy priming; play any affordable
  sequence of cards; end turn; discard remaining hand; resolve surviving
  enemies in displayed order; evaluate deaths and encounter completion; draw
  the next hand and restore the next-turn momentum allowance.
- Claim IDs: `FITS-003`–`FITS-008`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Each encounter exposes a small finite
  tile arena; generation fixes its current topology before tactical decisions.
- `CON-011` — exclusive occupancy with static barriers. Ordinary occupants do
  not share a tile, and walls / invalid boundaries block entry even when some
  edges are lethal push destinations.
- `CON-043` — bounded visible hand and commit size. The current hand has a
  declared capacity and each ordinary play commits exactly one held card.
- `CON-094` — shared renewable card-play budget. Momentum is one common pool
  spent by movement, attack and utility cards; it is not allocated per unit and
  refreshes at the turn boundary subject to modifiers.
- `CON-034` is absent: there is one controlled agent and no per-unit allowance
  of one move followed by one ability. Any affordable legal card sequence may
  interleave movement and attacks.
- Scarce strategic resources: momentum, useful movement cards, Agent 11 health,
  Ambassador health, safe cells and favourable enemy execution order.
- Claim IDs: `FITS-001`–`FITS-003`, `FITS-006`, `FITS-009`, `FITS-010`.

### Information Genes

- `INF-001` — fully visible current state. Current positions, health, card
  texts, momentum, primed attacks, target areas and enemy order are inspectable.
- `INF-003` — fixed concealed current state. The deck / discard composition is
  knowable but future shuffled draw order remains concealed until cards enter
  the hand.
- `INF-009` — exact committed hostile-intent preview. Primed attackers expose
  acting unit, target / range, effect and relative order before the player
  commits the phase; indicators update when a card changes the state.
- Claim IDs: `FITS-002`–`FITS-005`, `FITS-012`.

### Objective Genes

- `OBJ-029` — incapacitate finite hostile encounter set. Ordinary success is
  reached after all required enemies in the bounded room are removed or
  incapacitated before Agent 11 is defeated.
- `OBJ-030` — preserve designated vulnerable actor during clearance. The
  Ambassador must remain alive to earn the protected-HVT outcome while the same
  hostile set is cleared; terminal versus bonus status is a difficulty / mode
  parameter in the available evidence.
- `OBJ-011` is absent. The HVT is one health-bearing actor, not a shared
  infrastructure pool, and clearance rather than a fixed round horizon ends
  the encounter.
- `OBJ-020` is absent. Enemies begin in a compact encounter or enter through
  encounter-specific rules rather than forming Bad North's time-driven finite
  assault wave.
- Success, evaluation and failure: hostile clearance completes the ordinary
  encounter; Agent 11 defeat ends the run; Ambassador survival is evaluated
  separately and becomes terminal on documented higher difficulty.
- Claim IDs: `FITS-008`–`FITS-010`.

### Time Genes

- `TIM-005` — planning phase before committed hostile resolution. The player
  may sequence an affordable set of card commands without a running clock,
  then explicitly ends the phase and watches already primed enemies resolve
  before receiving the next hand.
- Replay animation is excluded: it reconstructs completed actions but cannot
  alter the encounter state.
- Claim IDs: `FITS-003`–`FITS-005`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Six visible cards and sufficient momentum | Select a movement card and legal empty cell | Momentum is spent, Agent 11 changes cell and enemy priming indicators update | card identity and target jointly define movement | `FITS-002`, `FITS-003` |
| One enemy is primed toward Agent 11's current cell | Play a card that moves Agent 11 away | The attack remains committed to its line / target and later strikes whatever valid body occupies it | intent precedes player-phase completion | `FITS-004`, `FITS-005` |
| A second enemy can be pushed into that committed line | Play a push card on the second enemy | Target shifts; collision consequences apply; the first enemy later hits the new occupant in its attack order | displacement converts hostile intent into friendly fire | `FITS-006`, `FITS-007` |
| A primed enemy remains alive but is stunned | End the player turn | Its committed attack is cancelled for that resolution | intent execution has explicit cancellation conditions | `FITS-005` |
| An enemy stands beside a wall or lethal edge | Play a legal knockback card | The target collides for extra consequence or leaves the arena and is incapacitated | board boundaries participate in attack resolution | `FITS-006` |
| Affordable cards remain but the tactical state is acceptable | End the turn | Unplayed cards leave the current hand, enemies resolve and a new hand is drawn | hand economy and hostile phase share one boundary | `FITS-003`, `FITS-005` |
| Ambassador occupies a threatened cell | Push the Ambassador to a legal safer cell | The HVT changes position; documented friendly pushes avoid ordinary attack damage but collision / enemy attacks remain relevant | protected actor is tactically manipulable | `FITS-007`, `FITS-009` |
| Final required enemy is incapacitated while Ambassador lives | Resolve the final effect | Encounter clears and the protected-HVT reward / record is retained | clearance and protection are conjunctive evaluated outcomes | `FITS-008`, `FITS-009` |
| Ambassador reaches zero health on Brutal | Resolve the damaging attack | The attempt fails under the documented difficulty rule | terminality is parameterised, not universal | `FITS-010` |

## Strategic and experiential structure

- Local decision: find an affordable card sequence that ends outside every
  dangerous target while turning at least one hostile attack, push or boundary
  into useful damage.
- Medium-term planning: preserve movement density in the deck, manage discard
  timing and momentum, keep the Ambassador away from ordered attack chains and
  avoid ending where the next hand must contain one specific escape card.
- Long-term structure: clear the bounded room with Agent 11 alive and preserve
  the Ambassador when its campaign reward or difficulty condition matters.
- Common heuristics: inspect enemy order before moving; treat committed lines
  as temporary weapons; push instead of spending damage when an edge is lethal;
  keep exits from being body-blocked; accept small HVT damage when survival is
  the actual predicate.
- Failure attribution: exact current threats are legible, but future card order
  is not. A failure can therefore be separated into a current forecast error,
  an avoidable deck-composition risk or an unfavourable concealed draw.
- Player-trust factors: intent overlays update after player actions and expose
  ordered consequences; mode-sensitive HVT terminality must be read from the
  chosen difficulty rather than inferred from the mission label.
- Claim IDs: `FITS-001`–`FITS-012`.

## Replay and variation

- What changes between sessions: encounter node order, room layout, enemy mix
  and placement, deck contents, enhancements and card draw order.
- Randomness or procedural generation: route / encounter generation and deck
  order vary attempts. Within a player phase, disclosed primed attacks resolve
  from current state rather than being resampled after commitment.
- Multiple viable strategies: movement-heavy, counter, aggression, grapple and
  other decks weight damage, displacement, defence and friendly fire
  differently.
- Typical replay motive: complete another generated run, preserve every HVT,
  test a deck style or improve optional turn / damage goals.
- Claim IDs: `FITS-002`–`FITS-012`.

## Adjacent systems and history

- Into the Breach is the mathematical near match and shares fixed board state,
  exact hostile intent, ordered automatic resolution, displacement and a
  planning boundary. It grants each of three mechs one move and one ability and
  protects a shared Grid through a fixed round horizon. Fights in Tight Spaces
  controls one agent through a random hand and shared momentum, clears the
  hostile set and treats the Ambassador as one vulnerable actor.
- Tactical Breach Wizards also previews enemy responses and permits turn
  rewinds, but its forecast reacts to the player's current draft actions rather
  than requiring every hostile attack to be committed before planning. It is a
  partial neighbour, not a supporter of exact-intent `INF-009` on current
  evidence.
- Slay the Spire supplies the acknowledged deckbuilding reference: a bounded
  hand, per-turn energy and discard/draw cycle. It does not place actors on a
  target grid or expose a set of spatial committed attacks that can be redirected
  into one another.
- Balatro is the corpus card control. It shares bounded held information and a
  concealed draw order but commits subsets for poker evaluation; Fights in
  Tight Spaces plays one targeted ability card at a time into a live board.
- Bad North shares selected spatial abilities and displacement, but runs in
  real time and telegraphs carrier arrival rather than exact committed attacks.
- Claim IDs: `FITS-001`–`FITS-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-061` | held card, target geometry and compound motion / attack effect |
| System Behaviour | `SYS-019`, `SYS-020`, `SYS-087` | attack order, cancellation, collision and draw / discard policy |
| Constraint | `CON-001`, `CON-011`, `CON-043`, `CON-094` | arena topology, occupancy, hand size and momentum refresh |
| Information | `INF-001`, `INF-003`, `INF-009` | visible present state, concealed draw order and exact hostile intents |
| Objective | `OBJ-029`, `OBJ-030` | required hostile set, HVT identity and difficulty-specific terminality |
| Time | `TIM-005` | player-card phase and enemy-resolution boundary |

Canonical signature:

`ACT-061; SYS-019,SYS-020,SYS-087; CON-001,CON-011,CON-043,CON-094;
INF-001,INF-003,INF-009; OBJ-029,OBJ-030; TIM-005`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `46` (`GAME-0001`–`GAME-0046`).
- Exact genome matches: none.
- Tied near matches: `GAME-0014` — Into the Breach (`7 / 22 = 0.318182`).
- Supported combination subsets: `COMB-0047`.
- Scan date: 2026-08-12.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0014` — Into the Breach | `SYS-019`, `SYS-020`, `CON-001`, `CON-011`, `INF-001`, `INF-009`, `TIM-005` | three persistent mechs with per-unit move/ability allowances and shared Grid horizon versus one card-driven agent, concealed hand turnover, shared momentum, hostile clearance and one HVT | Near, `0.318182` |

### Preserved research notes

- New genes: `ACT-061`, `SYS-087`, `CON-094`, `OBJ-029`, `OBJ-030`.
- Classification result: `New combination of known and new genes`; the game
  also establishes a derivative recurring supporter for the smaller exact-
  intent disruption core registered as `COMB-0047`.
- Evidence and reasoning: six shared spatial/intent genes make Into the Breach
  structurally close, but the hand / momentum and HVT / clearance deltas are
  causally necessary and cannot be represented as parameters of `CON-034` or
  `OBJ-011`.

## Combination record

- Registered recurring `COMB-0047` — previewed hostile intent redirected by
  displacement before ordered resolution, supported by Into the Breach and
  Fights in Tight Spaces.
- Exhaustive `COMB-0014` test: Fights in Tight Spaces has four of seven genes
  (`SYS-019`, `SYS-020`, `INF-009`, `TIM-005`) and lacks `ACT-019`, `CON-034`
  and `OBJ-011`; it is not a complete-genome supporter.
- No other existing combination gene set is a proper subset of this genome.

## Taxonomy impact

- Registry changes: added `ACT-061`, `SYS-087`, `CON-094`, `OBJ-029` and
  `OBJ-030`; added Fights in Tight Spaces evidence to `SYS-019`, `SYS-020`,
  `CON-001`, `CON-011`, `CON-043`, `INF-001`, `INF-003`, `INF-009` and
  `TIM-005`.
- Taxonomy-change record: none. No earlier gene definition or signature was
  corrected; the five additions occupy previously unrepresented boundaries.
- Candidate terms affected: promoted spatial action-card play, turn-boundary
  hand turnover, shared renewable card-play budget, finite hostile clearance
  and protected-actor clearance.

## Negative results

- Rejected `ACT-019`, `ACT-014`, `ACT-008`, `CON-034`, `OBJ-011` and
  `OBJ-020` through explicit action-economy and completion counterexamples.
- `COMB-0014` remains a verified single-game combination for Into the Breach;
  its seven-gene boundary is not weakened to force broader recurrence.
- [`NEGATIVE_RESULT_002`](../../../research/negative-results/NEGATIVE_RESULT_002.md)
  rejects the earlier independent-family interpretation after publisher
  evidence named Into the Breach as a positional design source; the game and
  derivative recurring `COMB-0047` remain valid.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] A bounded hand / momentum phase can alter
  exact committed attacks before automatic ordered resolution (`FITS-002`–`FITS-007`).
- [Pattern | Conflicting | Medium] HVT survival is invariantly evaluated but
  only documented as terminal on higher difficulty (`FITS-009`, `FITS-010`).

## Нові гени

- [Observation | Corroborated | High] Added `ACT-061`, `SYS-087`, `CON-094`,
  `OBJ-029` and `OBJ-030`; reused nine prior genes.

## Нові комбінації

- [Strong Pattern | Corroborated | High] Added recurring `COMB-0047`, the
  four-gene exact-intent / displacement / ordered-resolution core shared with
  Into the Breach; publisher evidence makes this derivative recurrence, not an
  independent-family result.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; no prior genome
  or lifecycle changed.

## Нові питання

- Does a directly inspected standard-mode build ever make Ambassador death
  terminal outside Brutal, or is the protected outcome always reward-only?
- Can Tactical Breach Wizards satisfy `INF-009` in a special authored encounter
  even though its ordinary forecast is action-reactive rather than precommitted?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] Tactical Breach Wizards.
- Optimisation criterion: test exact-intent versus reactive-forecast boundaries
  after `COMB-0047` becomes recurring, while avoiding another deck-economy game.
- Expected information gain: high for `SYS-019`, `INF-009`, `TIM-005`, rewind
  scope and the difference between computed response and committed intent.
- Backlog impact: retain Hexcells Infinite, Mini Motorways and Can of Wormholes;
  rank them formally against Tactical Breach Wizards in selection unit 007.

## Чому саме вона

- [Hypothesis | Corroborated | High] It is the strongest retained falsifier for
  whether `COMB-0047` has any independent-family recurrence or remains a
  derivative pair with a separate reactive-forecast neighbour.
