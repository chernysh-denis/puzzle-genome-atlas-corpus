---
game_id: GAME-0437
slug: diner-dash
game_title: Diner Dash
analysis_status: reviewed
reviewed: 2026-09-28
combination_ids: []
gene_ids:
  action:
    - ACT-091
    - ACT-341
    - ACT-574
  system:
    - SYS-030
    - SYS-1145
    - SYS-1146
    - SYS-1147
  constraint:
    - CON-620
    - CON-712
  information:
    - INF-330
  objective:
    - OBJ-013
  time:
    - TIM-003
---

# Game: Diner Dash — Flo's Diner early Career shift

Use the [canonical vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The number of tables, customer colour, tip goal and length of a repeated-action run are parameters rather than genes.

## Analysis scope

- Version / ruleset: original English Windows PC *Diner Dash* v1.0, as identified by PlayFirst's 2004 README, in the second early Career shift of Flo's Diner (1-2). The README establishes the base service rules; a first-hand PC guide corroborates their actual sequence, while a level-specific community route identifies 1-2 as a multi-table shift. The executable revision and level script were not directly inspected. Later sequels, phone/console adaptations and currently branded mobile releases are not assumed equivalent.
- Structured analysis target: `PLAT-WINDOWS-PC` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: watch parties arrive, drag one to a clean suitably sized table, then address that table's successive ready states: collect its order and deliver the ticket to the kitchen, take prepared food to the correct party, settle its bill and bus the dishes. Interleave stages across tables while each party's patience changes; grouping the same service action across parties earns a chain bonus. Earn enough tips from the finite shift's parties to clear its threshold.
- Entry: Career's second shift at the original Flo's Diner, before seating its first arriving party, with the ordinary early-shift tables and no later restaurant upgrade assumed active.
- Positive terminal: the shift's tip goal is met and the game declares that level won. A higher expert amount is optional; it is not required for this bounded success.
- Negative terminal: the available parties are exhausted without enough tips, costing a star under the original README. An impatient party leaving is a local lost opportunity, not by itself the end of the shift.
- Included: mouse-directed seating and service tasks; clean two-seat table eligibility; staged orders, kitchen ticket, ready meal, bill and dish return; up to two carried service items; multiple concurrent parties; visible ready-task markers and heart/patience feedback; colour-compatible seating, tip response, same-action score chain and minimum shift-tip target.
- Excluded: optional later coffee, podium, performer, snack station, restaurant critic, later customer classes, restaurant upgrades between shifts, Quick Play, Endless Shift, exact undisclosed scoring multipliers, all other restaurants, sequels and ports. The first shift's tutorial and its completion are setup predecessors, not part of this packet.
- Reproducible parameterisation: from a Career save eligible for Flo's Diner 1-2, seat a waiting party at a clean compatible two-seat table. Seat another when one is open, then take each ready order to the ticket station; collect and serve each kitchen-ready meal at the addressed table; collect payment, remove dirty dishes and repeat. Choose whether to visit equal task stages consecutively for chain points or answer a more urgent party first. Continue until the shift goal is reached or the finite customer opportunity ends. Exact numbers of arrivals, tips, heart decrement rates and chain multipliers are not asserted without executable measurement.
- Potential scoped modules: later first-diner beverage and critic rules; upgrade selection; measured colour-seat multiplier and chain reset arithmetic; whole Career or Endless Shift.
- Direct-play status: no Windows executable, input trace, original screenshot, video or audio was inspected. PlayFirst's original v1.0 README, preserved as text by an archival host, is the primary written rule source; the licensed distributor's game page independently identifies the original Windows product and mouse controls. A first-hand original-PC guide corroborates the stage order and customer differences. The precise 1-2 table and colour setup comes only from a level-specific community route and is treated as limited evidence, not used to define a universal gene.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DD-001` | The original PC v1.0 service loop seats parties, takes orders to a ticket station, serves prepared meals, settles bills and buses dishes before reseating a table. | Confirmed | Corroborated | High | P1, S1 |
| `DD-002` | A party can be seated only at a clean open table; matching customer and seat colours makes them happier. | Confirmed | Corroborated | High | P1, S1 |
| `DD-003` | Prompt service increases satisfaction and tips; excessive waiting can make a party leave and forfeit that opportunity. | Confirmed | Corroborated | High | P1, S1 |
| `DD-004` | Consecutive instances of the same service action earn a score bonus, independently of ordinary customer-tip response. | Confirmed | Direct | High | P1 |
| `DD-005` | Flo can queue addressed locations and carry at most two service items in the original PC rules. | Confirmed | Direct | High | P1 |
| `DD-006` | The shift is won by earning its tip goal; missing it costs a star. | Confirmed | Direct | High | P1 |
| `DD-007` | The selected early second Flo's Diner shift permits multiple tables and is described as a chaining lesson; its exact scripted setup was not directly verified. | Observation | Limited | Medium | S2 |

## Basic data

- Release / origin: gameLab and PlayFirst, original Windows *Diner Dash* v1.0 with a 2004 PlayFirst copyright notice. The README is version evidence, not proof of an exact binary build or date for every PC distribution.
- Platform or physical form: mouse-controlled Windows PC downloadable game; one early Career shift in Flo's Diner.
- Mechanical families: real-time system pressure (`FAM-010`) from arrivals and expiring patience; ordered dependency sequencing (`FAM-017`) from each party's service stages and dirty-table reset.
- **P1**: [PlayFirst's original *Diner Dash* v1.0 README, preserved verbatim as a Windows text document](https://oldgamesdownload.com/readme/diner-dash-windows-readme-english/), `HOW TO PLAY DINER DASH`, action list, score, item capacity, chain and star rules (accessed 2026-09-28). This is primary publisher-authored content on a third-party archival host; no executable was obtained from that host.
- **P2**: [Shockwave's licensed original *Diner Dash* Windows product page](https://www.shockwave.com/gamelanding/dinerdash), for publisher/developer identity, mouse input and base seating/order/clearing loop (accessed 2026-09-28). Its currently advertised availability is not taken as proof of v1.0 build identity.
- **S1**: [KeyBlade999's first-hand original-PC service guide](https://gamefaqs.gamespot.com/pc/926256-diner-dash/faqs/63909), stages, clean-table requirement, customer types and shifts (accessed 2026-09-28).
- **S2**: [community level-specific Flo's Diner walkthrough](https://dinerdash.fandom.com/wiki/Walkthrough:Flo%27s_Diner_(Diner_Dash)), 1-2 setup and consecutive-task advice (indexed passage accessed 2026-09-28; direct page fetch restricted). Its exact table count is not essential to the accepted genome.
- Claim IDs: `DD-001`–`DD-007`.

## Mechanical decomposition

### Action Genes

- Add `ACT-574` for dragging one waiting party to a selected clean compatible table. The party identity and table size are parameters; the choice changes which tables remain free (`DD-001`, `DD-002`).
- Reuse `ACT-341` for addressing a ready table or fixture to collect the order, hand the ticket to the kitchen, collect a check, pick up dishes and drop them at the bus station. These are current-state contextual interactions, not free-form recipe creation (`DD-001`, `DD-005`).
- Reuse `ACT-091` for carrying a prepared meal from the pass to the table whose order requested it. The addressed request and transferred dish remain distinct from merely clicking the kitchen ticket (`DD-001`).

### System Behaviour Genes

- Reuse `SYS-030` for time-driven party arrival into the waiting service queue. Add `SYS-1145` for the per-table service-stage transitions after each legal action, including kitchen preparation, departure after billing and dirty-table reset after busing (`DD-001`).
- Add `SYS-1146` for a party's changing satisfaction and resulting tip as delays or compatible seating alter that party's state. Add `SYS-1147` for bonus score from consecutive same-kind actions across parties; a different service action breaks that streak (`DD-002`–`DD-004`).
- Resolution order: arrival creates a waiting party; seating claims a clean table; order readiness precedes ticket submission and kitchen food readiness; served food precedes eating and check; departure leaves dirty dishes; clearing them makes the table eligible again. Satisfaction and chain bonuses change the score of accepted service, while the shift tip target settles separately.

### Constraint Genes

- Add `CON-712`: a party fits only an available clean table of adequate capacity; an occupied or dirty table cannot accept a new party (`DD-002`).
- Reuse `CON-620`: each waiting party's service opportunity can expire before the shift ends, removing its potential positive contribution (`DD-003`). The exact heart-loss rate is unmeasured.
- Two simultaneously carried items are a parameter of the service interactions rather than another globally reusable constraint in this packet (`DD-005`).

### Information Genes

- Reuse `INF-330` for current table readiness, order/food cues and individual patience; its interface does not disclose the entire future arrival schedule (`DD-001`, `DD-003`, `DD-005`).

### Objective Genes

- Reuse `OBJ-013`: earn the declared minimum tip total before the shift's finite service opportunities are exhausted. Extra expert tips are optional; losing one party is not an automatic whole-shift loss (`DD-006`).

### Time Genes

- Reuse `TIM-003` because parties and their patience progress while the player can select and queue work. This is not a turn-by-turn restaurant board (`DD-003`–`DD-005`).

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Blue-clad party waits; a clean table is free | Drag the party to that table | The party occupies it and begins its seated service stage; a dirty or occupied table would reject seating | addressed party-to-table allocation | `DD-001`, `DD-002` |
| Seated party puts down menus | Click the table, then the ticket station | Flo takes the order and submits its ticket; the kitchen begins its response | ordered service-stage transition | `DD-001` |
| Correct meal is ready while another table also needs service | Take the meal and click its requesting table | Flo delivers the dish to the addressed party; delaying may reduce the other party's satisfaction | competing live requests | `DD-001`, `DD-003` |
| Two tables have the same ready service stage | Perform the same action at both consecutively | The later eligible repetition adds a chain bonus; interleaving another task forfeits that continuity | same-action score chain | `DD-004` |
| Meal finished and bill ready | Address that table, then clear its dishes to the bus station | Payment is collected, the party leaves, and clearing restores the table for a new party | tip settlement and reusable table | `DD-001`, `DD-006` |
| One waiting party has nearly lost all patience | Serve it or continue a less urgent chain | Prompt service may preserve its tip; expiry removes that party without necessarily ending the shift | local service expiry trade-off | `DD-003`, `DD-004` |

## Strategic and experiential structure

- Local decision: choose the next ready station or party, balancing an urgent heart indicator against a same-action chain.
- Medium-term plan: keep clean seats available and move several parties through their order, meal, bill and dish states without blocking later arrivals.
- Long-term boundary: meet one Career shift's minimum tip goal; the restaurant upgrade tree and whole career are outside this scope.
- Failure attribution: a visible waiting or ready state makes a delayed party's departure understandable, but exact patience decay and score arithmetic were not measured.
- Player trust: a missed party is a recoverable local loss while enough other tip opportunities remain; no invented fixed global timer is used.

## Replay and variation

The authored early shift has a finite set of service opportunities, but the player's chosen seating, task order, repeat-action chains and delays can produce different scores and losses. The evidence does not establish a random party schedule for this exact shift, so that is not claimed.

## Adjacent systems and history

*DAVE THE DIVER* (`GAME-0278`) shares arriving service demand, visible requests and individual expiry but first acquires its menu stock in a separate dive; *Diner Dash* starts with a restaurant shift and makes seating, table turnover and same-action chains central. *Overcooked! 2* (`GAME-0300`) prepares food directly with controllable chefs for expiring orders; Flo sends tickets to an automatic kitchen and delivers ready food. These contrasts are mechanical, not claims about the selected mathematical neighbour below.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-091`, `ACT-341`, `ACT-574` | seating, contextual service and addressed meal delivery |
| System Behaviour | `SYS-030`, `SYS-1145`, `SYS-1146`, `SYS-1147` | arrival, service stages, satisfaction and action chain |
| Constraint | `CON-620`, `CON-712` | local expiry and clean table eligibility |
| Information | `INF-330` | ready tasks and patience |
| Objective | `OBJ-013` | minimum shift-tip target |
| Time | `TIM-003` | live service progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `436` (`GAME-0001`–`GAME-0436`).
- Exact genome matches: none.
- Tied near matches: `GAME-0278` — DAVE THE DIVER (`5 / 25 = 0.200000`).
- Supported combination subsets: none.
- Scan date: 2026-09-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0278` *DAVE THE DIVER* | `ACT-091`, `SYS-030`, `CON-620`, `INF-330`, `TIM-003` | Both games serve arriving patrons through live requests with expiring opportunities, but Dave acquires menu stock through a separate dive and allocates prepared menu offerings. Flo instead chooses clean seating, moves each table through staged service and earns a bonus for consecutive same-kind actions. | Tied-near maximum, not an exact match (`5 / 25 = 0.200000`). |

## Taxonomy impact

`TAXONOMY_CHANGE_174` admits party seating, staged table turnover, satisfaction-sensitive tips, consecutive same-action bonuses and clean-table eligibility. Existing contextual interaction, meal delivery, arrivals, local expiry, live service information, finite score goal and real-time input are reused. No earlier signature or verified combination changes.

## Negative results

- `SYS-823` requires stock imported from a prior separate player activity; this shift's kitchen preparation follows an order ticket, not a preceding fishing dive.
- `SYS-975` links traversal tricks through movement continuity and explicitly excludes order-service chains; Diner Dash instead rewards repeated same-kind table actions.
- `SYS-822` grades a completed bounded activity; the selected shift has minimum and optional expert tip goals, not a separately evidenced medal-like grade.
- Later podium, coffee and food critic are real original-game possibilities but excluded from the selected early 1-2 packet; no sequel mechanic is imported.

## Delta summary

## New facts

- [Confirmed | Corroborated | High] The original v1.0 publisher README sets out the five-stage service loop and dirty-table reset (`DD-001`).
- [Confirmed | Direct | High] Repeated same-kind actions earn bonuses without replacing the patience-sensitive ordinary tip calculation (`DD-003`, `DD-004`).

## New genes

- [Observation | Corroborated | High] Five typed boundaries are admitted in `TAXONOMY_CHANGE_174`.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_174`; earlier signatures remain unchanged.

## New questions

- What exact chain multipliers and patience decay rates does an instrumented original v1.0 Windows run produce for this shift?

## Next game

`GAME-0438` *Q*bert*, original arcade, follows after the Goal stop window. Its selected question concerns landing-colour state, enemy pursuit and board clearance; the exact arcade ruleset still requires its own research.
