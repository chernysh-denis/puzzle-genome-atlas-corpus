---
game_id: GAME-0300
slug: overcooked-2
game_title: Overcooked! 2
analysis_status: reviewed
reviewed: 2026-09-18
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-052
    - ACT-410
    - ACT-461
  system:
    - SYS-030
    - SYS-872
    - SYS-873
    - SYS-874
  constraint:
    - CON-620
    - CON-637
  information:
    - INF-330
  objective:
    - OBJ-176
  time:
    - TIM-003
    - TIM-023
---

# Game: Overcooked! 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Ingredients,
thresholds and times parameterise genes rather than creating new labels.

## Analysis scope

- Version / ruleset: the original 2018 Nintendo Switch base edition of
  Overcooked! 2, not the Gourmet Edition, Switch 2 Edition, downloadable
  kitchens or a later seasonal mode. Nintendo's base-product listing and
  Team17's launch FAQ establish the edition and original Switch release.
  No installed software version was inspected; later patches could affect
  exact thresholds or timing.
- Structured analysis target: the matching original Nintendo Switch base
  entry in `knowledge/platforms/games.json`, not an inferred cross-platform
  release inventory.
- Primary decision loop: read the current fish or shrimp sashimi order and its
  remaining wait; move a selected chef between ingredient crate, chopping
  board, plate and serving hatch; carry or throw an ingredient, chop it,
  place the prepared ingredient on a plate, switch between the two persistent
  solo chefs, and submit the matching plate before its order expires. Serve
  tickets in their displayed sequence to retain the combo multiplier while
  the kitchen clock runs, then read the score and star settlement.
- Entry and exit: begin a new solo Story save, complete the mandatory tutorial
  and enter ordinary kitchen `1-1` with the game's one-player two-chef mode.
  End at the settled `1-1` result with at least one star and the successor
  `1-2` node available on returning to the Story map. The selected packet
  calls for a fixed recorded completion score and reload check, but neither
  an actual run nor a reload occurred; no observed score, retained save or
  exact installed-build claim is made.
- Included: tutorial as entry prerequisite; sashimi orders of chopped fish or
  shrimp on a plate; ingredient transport including the sequel's throw;
  manual chopping, plate assembly and serving; solo chef switch; independently
  waiting orders, their expiry, accepted-order score and order-sequence combo;
  the first-serving clock start described for `1-1`; final star evaluation and
  `1-2` progression. The one-player one-star threshold of 20 and the `2:30`
  kitchen interval are secondary-source parameters, not verified Switch
  measurements.
- Excluded: local or online multiplayer, Arcade, Versus, New Game+, four-star
  scoring, practice and survival modes, all DLC and seasonal recipes, later
  Story kitchens, cooking heat, dishwashing, moving layouts, score optimisation
  beyond the first accepted one-star result, and additional chef abilities.
- Potential scoped modules: investigate Switch build-specific score and timer
  parity, throwing collision details, and post-reload map persistence in a
  later direct-play review; do not silently add them to this signature.
- Direct-play status: not conducted. No Nintendo Switch entitlement, installed
  build, fresh save, capture or reload was available. Publisher and platform
  pages support the product and general sequel rules; a level-specific
  community reference and independent written walkthrough support the 1-1
  route. This is a source-bounded reconstruction, not an observed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `C-300-001` | The original Switch base game launched in 2018 with solo Story play distinct from later editions and DLC. | Confirmed | Direct | High | Nintendo product listing; Team17 FAQ |
| `C-300-002` | Solo play controls two persistent chefs by switching, not by admitting a second player. | Pattern | Corroborated | Medium | Team17 support explanation; independent solo guides |
| `C-300-003` | Kitchen 1-1's sashimi uses either chopped fish or chopped shrimp on a plate and has no required heat or washing. | Pattern | Corroborated | Medium | Level-specific community guide; independent written walkthrough |
| `C-300-004` | The first accepted dish starts the 1-1 clock; orders have individual wait limits and accepted service contributes to score. | Pattern | Limited | Medium | Level-specific community guide; Team17 A–Z |
| `C-300-005` | Solo 1-1 lists a 20-point one-star threshold, a 2:30 kitchen interval and a successor 1-2; Switch build parity and retained reload state are untested. | Hypothesis | Limited | Low | Level-specific community guide |
| `C-300-006` | Serving recipes in the exact displayed ticket order maintains a score-combo multiplier rather than merely counting consecutive dishes. | Confirmed | Direct | High | Team17 A–Z |

## Basic data

- Release / origin: Ghost Town Games / Team17; original Switch base product
  dated 2018-08-07 by Nintendo and Team17.
- Platform or physical form: original Nintendo Switch base digital game.
- Puzzle family: real-time service pressure, coordinated agent routing and
  ordered preparation dependencies.
- Primary sources: [Nintendo original Switch product](https://www.nintendo.com/es-es/Juegos/Juegos-de-Nintendo-Switch/Overcooked-2-1388792.html),
  [Team17 launch FAQ](https://www.team17.com/news/overcooked-2-faq),
  [Team17 A–Z](https://www.team17.com/news/the-a-z-of-overcooked-2),
  [Team17 solo-chef support response](https://steamcommunity.com/app/728880/discussions/1/4355617246783394926/).
- Secondary sources: [Overcooked Wiki 1-1 guide](https://overcooked.fandom.com/wiki/1-1_(Overcooked!_2)),
  [independent written early-game guide](https://home-gamer.com/2023/02/14/over_cooked_a_full_course_of_the_kingdom_overcooked2/?PageSpeed=noscript).
- Claim IDs: `C-300-001`–`C-300-006`.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: `ACT-008` (direct kitchen movement), `ACT-048` (carry,
  release or throw a portable ingredient or plate), `ACT-052` (switch the
  unique direct-control locus between two present chefs), `ACT-410` (chop one
  ingredient at a manual board).
- Candidate genes: `ACT-461` (commit a carried prepared plate at the serving
  hatch). `ACT-091` requires an addressed NPC and therefore does not fit the
  inanimate hatch and ticket queue.
- Parameters: chef, station, raw ingredient, prepared state, plate, hatch and
  switch timing.
- Claim IDs: `C-300-002`–`C-300-004`.

### System Behaviour Genes

- Existing gene IDs: `SYS-030` (new visible service tickets arrive over time).
- Candidate genes: `SYS-872` (the plate retains recipe-compatible prepared
  contents); `SYS-873` (matching service settles ticket score and the
  displayed-order combo); `SYS-874` (end-of-kitchen score settles stars and
  successor access).
- Resolution order: fetch → chop → plate → carry to hatch → match live ticket
  → apply score/tip → continue under the clock → final star and map settlement.
- Parameters: fish/shrimp order, plate contents, ticket queue, dish value,
  displayed ticket order, combo multiplier, star thresholds and next-node
  grant.
- Claim IDs: `C-300-003`–`C-300-006`.

### Constraint Genes

- Existing gene IDs: `CON-620` (each ticket can expire before fulfilment).
- Candidate genes: `CON-637` (only the matching prepared, plated dish can
  fulfil a currently live order).
- Scarce strategic resources: time, chef attention, chopping-board access and
  limited ready plates; exact inventory numbers are parameters.
- Claim IDs: `C-300-003`, `C-300-004`.

### Information Genes

- Existing gene IDs: `INF-330` (visible live dish tickets and wait pressure).
- Candidate genes: none. Aggregate score and kitchen time are displayed
  feedback, not independently claimed as a novel information boundary.
- Claim IDs: `C-300-004`.

### Objective Genes

- Existing gene IDs: none; score optimisation beyond one accepted result is
  out of scope.
- Candidate genes: `OBJ-176` (earn the first ordinary kitchen's one-star
  progression award).
- Success, evaluation and failure: a qualifying final score awards at least
  one star and permits `1-2`; an insufficient score fails this bounded goal
  without deleting the Story save. The reported 20-point solo threshold is
  secondary and pending direct Switch verification.
- Claim IDs: `C-300-005`.

### Time Genes

- Existing gene IDs: `TIM-003` (live chef input under ongoing orders and
  deadline).
- Candidate genes: `TIM-023` (the first accepted plate triggers the 1-1
  kitchen countdown after an initial untimed prep interval).
- Claim IDs: `C-300-004`, `C-300-005`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Raw fish at crate; a fish ticket is visible | Carry fish to an available board and chop | Fish becomes prepared; no pot or cooking step is needed in 1-1 | Manual recipe step, not generic cooking | `C-300-003` |
| Prepared fish and an empty plate | Transfer fish to plate | The plate retains a one-ingredient sashimi dish | Prepared object and plate state are distinct | `C-300-003` |
| One chef holds a prepared plate; the other remains by the crate | Switch direct control | Both chefs remain in the same kitchen; the new chef becomes directly controlled | Solo switch is not a second multiplayer client | `C-300-002` |
| Matching live ticket and prepared plate at hatch | Submit plate | The ticket is fulfilled, score/tip updates, and the first accepted service starts 1-1's countdown | Service, score and clock start are separate transitions | `C-300-004`, `C-300-006` |
| A ticket's wait allowance reaches zero | Continue without matching service | That ticket expires; kitchen session and other tickets continue | Individual deadline differs from shared session end | `C-300-004` |
| Kitchen interval ends with qualifying score | Read result and return to map | One or more stars are awarded and 1-2 is reported available | Graded result and successor progression | `C-300-005` |

## Strategic and experiential structure

- Local decision: choose which ticket and which chef can complete its next
  recipe step before the ticket times out.
- Medium-term planning: stage chopped ingredients and plates before starting
  the main clock; switch chefs to reduce empty travel; follow the displayed
  ticket order to retain the score combo rather than merely serving quickly.
- Long-term structure: leave the first ordinary kitchen with a qualifying
  star and advance to 1-2, not later chapter mastery.
- Common heuristics: put a chef near each ingredient side, prepare a first
  correct plate before service, and prioritise a nearly expired ticket.
- Failure attribution: wrong or unprepared plate fails compatibility; slow
  handling loses a ticket; insufficient settled score misses the star.
- Player-trust factors: visible ticket and wait state make urgency legible;
  report exact Switch parity as unverified rather than claiming a measured run.
- Claim IDs: `C-300-002`–`C-300-006`.

## Replay and variation

- What changes between sessions: live ticket arrival/order and the player's
  chef routing and preparation timings; no procedural map variation is
  claimed for the fixed first kitchen.
- Randomness or procedural generation: order timing may vary; the source
  packet does not establish an exact random seed or distribution.
- Multiple viable strategies: stage fish or shrimp, alternate chefs, or
  optimise a service sequence; only the first accepted one-star route matters.
- Typical replay motive: improve stars or score, excluded from this packet.
- Claim IDs: `C-300-003`–`C-300-006`.

## Adjacent systems and history

- Direct predecessors: Overcooked! established shared-kitchen order pressure;
  the sequel officially adds throwing and online play, but online play is
  outside this one-player packet.
- Variants: Gourmet Edition, Switch 2 Edition, seasonal and DLC kitchens are
  different product/content scopes and do not establish 1-1 rules here.
- Similar games: DAVE THE DIVER's first restaurant service reuses arriving
  tickets, expiry and visible wait; its inventory stock and NPC hand-in are
  materially different. It Takes Two shares coordination but not a solo
  time-pressured plate queue.
- Important differences: 1-1's manually chopped one-ingredient dish is
  committed at a hatch, and the first accepted service gates the main clock.
- Claim IDs: `C-300-001`–`C-300-006`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-052`, `ACT-410`, `ACT-461` | Chef switch and fish/shrimp transport |
| System Behaviour | `SYS-030`, `SYS-872`, `SYS-873`, `SYS-874` | Order arrival, plating, order-combo score, stars |
| Constraint | `CON-620`, `CON-637` | Per-ticket expiry and recipe match |
| Information | `INF-330` | Ticket and wait feedback |
| Objective | `OBJ-176` | First qualifying 1-1 result |
| Time | `TIM-003`, `TIM-023` | Live orders after first-service clock start |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `299` (`GAME-0001`–`GAME-0299`).
- Exact genome matches: none.
- Tied near matches: `GAME-0278` — DAVE THE DIVER (`5 / 28 = 0.178571`).
- Supported combination subsets: none.
- Scan date: 2026-09-18.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0278` — DAVE THE DIVER | `ACT-008`, `SYS-030`, `CON-620`, `INF-330`, `TIM-003` | Both operate live expiring service demand, but DAVE THE DIVER spends stock from a preceding dive and hands dishes to addressed customers; here two solo-switched chefs physically chop, plate and submit sashimi at a common hatch before a star-gated kitchen result. | Near, `0.178571` |

- New genes: `ACT-461`, `SYS-872`–`SYS-874`, `CON-637`, `OBJ-176`, `TIM-023`.
- Classification result: `New gene`.
- Evidence and reasoning: the live order and expiry boundaries transfer from
  existing service games, but the carried plate-to-hatch commitment,
  preparation compatibility, first-service clock start and star progression
  are not covered by their narrower existing definitions.

### Preserved research notes

- New genes: `ACT-461`, `SYS-872`–`SYS-874`, `CON-637`, `OBJ-176`, `TIM-023`.
- Classification result: `New gene`.
- Evidence and reasoning: the live order and expiry boundaries transfer from
  existing service games, but the carried plate-to-hatch commitment,
  preparation compatibility, first-service clock start and star progression
  are not covered by their narrower existing definitions.

## Taxonomy impact

- Registry changes: add the seven Active definitions above; no existing
  signature or definition is reinterpreted.
- Taxonomy-change record: none; this is a prospective game addition.
- Candidate terms affected: serving hatch, prepared plate, service-tip
  settlement, first-service countdown and one-star unlock.

## Negative results

- `ACT-091` is rejected because its delivery target is an addressed NPC, not
  the inanimate service hatch; `SYS-823` requires stock from a preceding
  activity, absent from this self-contained kitchen; `SYS-711` grades elapsed
  driving time rather than kitchen score. A 4-star New Game+ threshold is
  excluded; secondary sources disagree on its exact 1-1 value.

## Delta summary

## New facts

- [Confirmed | Direct | High] Original Nintendo Switch base product and
  separated later editions are fixed for the packet (`C-300-001`).
- [Pattern | Corroborated | Medium] First kitchen uses solo chef switching,
  manual one-ingredient sashimi and live tickets (`C-300-002`–`C-300-004`).

## New genes

- [Observation | Corroborated | Medium] Seven bounded definitions capture
  serving, plate compatibility, ticket scoring, stars, recipe legality and
  the first-service timing edge.

## New combinations

- [Observation | Corroborated | Medium] No verified combination is a strict
  subset of this first-kitchen signature.

## Taxonomy changes

- [Observation | Corroborated | Medium] No existing boundary changes.

## New questions

- Does the current original Switch build preserve the 20-point one-star
  threshold, first-service 2:30 countdown and 1-2 unlock after a reload?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0301` Divinity: Original Sin 2 -
  Definitive Edition, as recorded in selection 019's platform amendment.
- Optimisation criterion: preserve the nine-game platform-balanced selection
  while moving from real-time kitchen service to turn-based tactical systems.
- Expected information gain: compare surfaces, AP, environmental effects and
  party-coordination boundaries against the existing CRPG corpus.
- Backlog impact: no reordered later subject.

## Why this game

- [Hypothesis | Limited | Medium] Overcooked! 2 exposes a compact live
  multi-chef recipe and score loop that contrasts with the existing stock-fed
  restaurant session and the previous combat-focused unit.
