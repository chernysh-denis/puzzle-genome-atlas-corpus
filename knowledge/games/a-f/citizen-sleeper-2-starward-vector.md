---
game_id: GAME-0673
slug: citizen-sleeper-2-starward-vector
game_title: "Citizen Sleeper 2: Starward Vector"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-897
    - ACT-898
  system:
    - SYS-1929
    - SYS-1930
    - SYS-1931
    - SYS-1932
    - SYS-1933
    - SYS-1934
  constraint:
    - CON-886
  information:
    - INF-620
  objective:
    - OBJ-354
  time:
    - TIM-002
---

# Game: Citizen Sleeper 2: Starward Vector

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Crew names, dice faces, costs and individual clock sizes are instance parameters.

## Analysis scope

- Version / ruleset: English commercial base game for Xbox Series X|S,
  Xbox product 9MWCF1XBJBR2, January 31, 2025. Ordinary solo Hexport
  Conway Signal board contract. The complete reference uses a Machinist.
  The exact installed Xbox build and recording difficulty are unverified.
- Structured analysis target: PLAT-XBOX-SERIES in
  `knowledge/platforms/games.json`. The Xbox-attributed witness
  corroborates the contract, crew and check rules. The full outcome
  witness uses pointer controls and does not identify its host.
- Entry: after access to Hexport's Contract Board, purchase coordinates
  for Conway Signal for 10 cryo. Confirm the vector and crew and pay
  2 fuel to travel. Serafin is locked into the crew. In the reference
  Nia is available but remains unselected. The Xbox-attributed witness
  uses both Serafin and Nia.
- Primary decision loop: inspect the Sleeper's and crew's rolled dice,
  owner skills, action outcomes and Drone Stress. Assign and confirm
  one die on a skill action. Build Control Access at the hatch and
  Broadcast Access at the damaged hull. When each access clock clears,
  open its successor task and spend more dice to disable the core or
  array. Renew dice through a supply-limited cycle only when the
  remaining drone and countermeasure pressure leaves room.
- Exit: both shutdown branches reach the successful Drone Death
  result. Confirm leaving via Contract Concluded and verify the
  return to Hexport, +200 cryo and the completed minor drive.
- Included: the paid offer and fuel gate, crew assignment, known
  individual dice, skill-dependent outcomes, access and shutdown
  clocks, personal and crew stress, Drone Stress, the separately
  labelled countermeasure cycle clock, supplies and settlement.
- Excluded: earlier credit grinding, complete relationship routes,
  other contracts and optional field loot, every Push configuration,
  repair or glitch economy, dangerous-mode overrides, alternative
  explosion outcomes, later upgrades and save/reload.
- Potential scoped modules: a reproduced failed or mixed contract,
  a bounded controlled Push experiment, or a variant with Nia carried
  through a full result.
- Direct-play status: No personal console installation or control input. The Xbox store and
  publisher identify the commercial Series release and describe dice,
  skills, crews and multi-cycle contracts. Lutfinator82496 attributes
  the gameplay to Xbox Series X|S, shows console prompts, and captures
  Conway entry and active play. That recording ends during the contract.
  XUBRNC independently shows the full route through recovery and payment
  with a pointer interface and does not identify its platform. The
  common mechanics and same-named action panels match. The full settlement
  is therefore cross-corroborated for the retail rules, without claiming
  to have seen a complete Xbox hardware replay. Static frames were
  inspected in the background without audio. Executable identity,
  controller telemetry and the exact probability and stress functions
  are not established.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| CS2-001 | Xbox lists the English-capable commercial base game for Series X and Series S from January 31, 2025. Its contracts use crew, dice and multiple cycles. | Observation | Direct | High | P1, P2, P3 |
| CS2-002 | The Conway Signal board fee is 10 cryo, the vector costs 2 fuel, and the offer shows 200 cryo payment for disabling the signal source. Crew is confirmed before travelling. | Observation | Corroborated | High | W1 49:20–49:29 and 54:03–54:22, W2 32:55–33:10, R1 |
| CS2-003 | Serafin is locked. Nia can be selected when available. Each included crewmate gets two dice and their own skill matches. W1 takes Serafin alone; W2 uses both portraits. | Observation | Corroborated | High | W1 54:07–54:22 and 56:39, W2 33:02–35:00, P2 |
| CS2-004 | Select a current die and insert it in a skill action, then confirm. Owner and skill affect its outcome. Positive progress can exceed neutral progress; a negative result can add Drone Stress. | Observation | Corroborated | High | W1 58:26–60:44 and 63:50–64:18, W2 34:38–36:45 and 38:24–38:35 |
| CS2-005 | Control Access at the hatch leads to Core Disabled via Disconnect Backup. Broadcast Access at the hull leads to Array Disabled via Hack Broadcast. Progress on one does not replace the other. | Observation | Corroborated | High | W1 56:54–58:25 and 63:36–68:03, W2 34:39–39:30, R1 |
| CS2-006 | On-site cycle renewal refreshes usable dice. Available supplies support that cycle. The tutorial says depleted supplies add one stress per cycle to each participant. A full crew stress track makes that member unavailable. | Observation | Corroborated | High | W1 56:39, 60:20–61:45, W2 34:27 and 36:45–39:15, P2 |
| CS2-007 | The game distinguishes personal stress and die damage from Drone Stress. The latter is a contract hazard and separate from the later Drone Countermeasure cycle clock. High personal stress threatens dice through subsequent cycle rolls. | Observation | Corroborated | High | P2, P3, W1 61:39–61:45 and 63:50–64:02, W2 38:24–38:35 |
| CS2-008 | Filling the core and array requirements leads to the success scene. The leave confirmation bars return to the contract site. Arrival credits 200 cryo and the minor drive, with the reference balance rising from 57 to 257. | Observation | Direct | High | W1 67:40–69:37 |
| CS2-009 | The Xbox-attributed witness ends before settlement. Its exact platform model and the outcome witness's host are unverified. | Observation | Limited | High | W1 title/controls, W2 title and 39:33 endpoint |

## Basic data

- Release / origin: Jump Over the Age, published by Fellow Traveller.
  This analysis covers the English retail Series rules.
- P1: [Xbox commercial product](https://www.xbox.com/en-US/games/store/citizen-sleeper-2-starward-vector/9MWCF1XBJBR2).
  Product identity, release date, Series target and publisher.
- P2: [Fellow Traveller product and mechanics](https://www.fellowtraveller.games/citizen-sleeper-2-starward-vector).
  Multi-cycle contracts, crew skills, persistent dice wear and
  tradeoffs across risks. The published page covers several platforms.
- P3: [Xbox Wire at release](https://news.xbox.com/en-us/2025/01/30/citizen-sleeper-2-launch-xbox-game-pass/).
  Describes insertion, new rolls at the start of cycles, the class
  skills, travel and the effect of stress on die integrity.
- W1: [XUBRNC, completed Conway Signal reference](https://www.youtube.com/watch?v=X8oY8iWwLEw&t=3243s).
  From crew selection at 54:05 to the shut-down and receipt at
  approximately 69:37. The board purchase is near 49:20.
- W2: [Lutfinator82496, Xbox Series X|S contract capture](https://www.youtube.com/watch?v=COm9cHgyqqU&t=1975s).
  From the vector at 32:55, crew and same control scheme through
  an active, two-crewmate visit. Includes failure feedback at 38:24–38:35.
  Use as corroboration of the Xbox route, not a proof of Xbox settlement.
- R1: [Neoseeker Hexport contract walkthrough](https://www.neoseeker.com/citizen-sleeper-2-starward-vector/Escape_Hexport).
  Cross-checks offer and travel costs and the two distinct branch goals.
- Claim IDs: CS2-001–CS2-009.

### Reproducible route evidence

1. Buy Conway Signal on Hexport's board. On the map, select its
   vector and inspect the forecast 2-fuel debit and 200-cryo offer.
   On the crew screen, Serafin is already locked. W1 confirms with
   Nia still selectable and Juni unavailable. W2 proceeds with Nia
   included. The two roster states establish that Nia is optional.
2. At the drone, inspect Control Access and Broadcast Access.
   Reprogram Hatch uses Interface, Release the Hatch uses Engineer,
   Identify Route uses Intuit and Create Opening uses Endure.
   Picking a die into a slot brings up the commit action. Subsequent
   skill results spend it. At W1 60:32 the visible Serafin die in
   Create Opening is already absent from his free slots during work.
3. When current dice are inadequate, return to the Rig's cycle
   controls and renew them. W1 visibly shifts from one remaining
   supply to none. W2 at 38:24–38:35 shows a failed Control Access
   attempt ending with adverse feedback while the branch remains
   unresolved. The tutorial separates each actor's stress from the
   contract hazard.
4. Complete the hatch access clock to expose Disconnect Backup.
   In W1 near 64:05 this action produces a neutral result that
   increments Core Disabled. Complete the broadcast access clock to
   expose Hack Broadcast. The second access class has a separate
   Array Disabled progress requirement. Drone Countermeasure is
   shown as a cycle clock alongside the final branches.
5. At around 68:03, the successful route reaches the quiet drone
   scene. A separate Contract Concluded confirmation permits leaving
   and states that there is no return. At approximately 69:37 the
   Hexport balance is 257 instead of 57, the minor drive completes
   and its upgrade point is visible. Stop before spending it.

## Mechanical decomposition

### Action Genes

- ACT-897: allocate and confirm a currently available die from a
  particular actor on an addressed skill task. CS2-003, CS2-004.
- ACT-898: confirm mandatory and optional crew entries before travel.
  Different selections open distinct die pools and skills. CS2-002,
  CS2-003.

### System Behaviour Genes

- SYS-1929: consume the committed die and resolve a skill-modified
  result with separate positive, neutral and negative outcomes.
  Progress or costs depend on the actual resolved class. CS2-004.
- SYS-1930: renew the current participants' usable dice on a new
  contract cycle and resolve supply availability. Exhausting supplies
  changes the cost of subsequent cycles without itself ending the
  contract. CS2-006.
- SYS-1931: completing an access clock exposes the next subtask for
  that branch. Both latter clocks must complete for the successful
  dual shutdown. CS2-005, CS2-008.
- SYS-1932: the contract's Drone Stress responds to adverse outcomes
  and can end the contract. Drone Countermeasure is a separate clock
  driven by cycles. Their exact trigger interaction is not measured.
  CS2-004, CS2-007.
- SYS-1933: crew stress accumulates per member, and filling that
  member's capacity removes their available actions. CS2-006.
- SYS-1934: personal stress can damage individual dice when a cycle
  refreshes them, separately from ordinary spending of available
  dice and party-member stress. CS2-006, CS2-007.

### Constraint Genes

- CON-886: confirm a fuel-priced vector and have the declared
  fuel available for departure. Coordinates and travel are separate
  purchases. Supplies are an operating stock; the Xbox-attributed
  trace shows a zero-supply departure. CS2-002, CS2-006.

### Information Genes

- INF-620: expose each actor's current dice and skill relation to
  the current action alongside progress and pressure. Show the
  resolved outcome and affected track. CS2-003–CS2-007.

### Objective Genes

- OBJ-354: complete the finite set of service tasks, confirm the
  concluded departure and verify the delivered contract payment.
  CS2-005, CS2-008.

### Time Genes

- TIM-002: choose and confirm the discrete action or cycle boundary.
  Visible cycle clocks do not require a real-time response between
  inputs. CS2-004, CS2-006, CS2-007.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Paid signal coordinates and sufficient travel fuel | Confirm the vector and crew | One contract instance with the selected participants and the charged fuel | CS2-002, CS2-003 |
| A crew die is available and matches an action skill | Insert it and start the action | Die committed, outcome class and its progress or cost displayed | CS2-003, CS2-004 |
| Broadcast Access or Control Access is complete | Inspect the accessible successor | The corresponding array or core operation is now available | CS2-005 |
| A cycle ends with or without supplies | Renew the pools | Usable dice rerolled, with supply-supported operation or escalating stress | CS2-006, CS2-007 |
| Core and array disabled | Confirm the concluded leave and return | Hexport payment +200 cryo and minor drive completed | CS2-008 |

## Strategic and experiential structure

The player can compare an actor's skill with the task before giving up
a useful die. A neutral result can make partial progress, so the
choice need not be a success-or-failure gamble. The shared branch
objective and the actor's individual dice and stress are different
resources. The exposed pressure changes the cost of waiting for a
better roll or completing one branch ahead of the other.

## Replay and variation

The outcome reference uses Serafin without Nia. The Xbox-attributed
capture includes both and operates the same entry tracks. It shows
that a different roster changes available dice and skill coverage.
It does not show payoff equivalence under every difficulty or a
failed contract. The exact probabilities and stress damage schedule
were not inferred from one outcome trace.

## Adjacent systems and history

The previous Citizen Sleeper also used dice and cycles. Here the
choosable contract requires separate crew, voyage and result states.
The later upgrade from the returned payment or drive is an external
progression step outside this contract.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-897, ACT-898 | Assign an actor's die and commit a crew |
| System Behaviour | SYS-1929, SYS-1930, SYS-1931, SYS-1932, SYS-1933, SYS-1934 | Resolve dice, renew cycles, unlock tracks and retain distinct risks |
| Constraint | CON-886 | Require and debit route fuel |
| Information | INF-620 | Show dice ownership, skill match, effect and pressure |
| Objective | OBJ-354 | Close all service tasks and return for settlement |
| Time | TIM-002 | Self-paced choices between discrete resolutions |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `672` (`GAME-0001`–`GAME-0672`).
- Exact genome matches: none.
- Tied near matches: `GAME-0064` — SET (`1 / 16 = 0.062500`); `GAME-0637` — Tiny Glade (`1 / 16 = 0.062500`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [SET (GAME-0064)](../s-z/set.md) | TIM-002 | Both sampled modes permit untimed decision steps. SET validates a selected triple against visible attribute patterns. Conway Signal allocates finite crew dice to two separate task branches and can accumulate stress when proceeding. | Near, `0.062500` |
| [Tiny Glade (GAME-0637)](../s-z/tiny-glade.md) | TIM-002 | Both allow an unhurried next edit or action. Tiny Glade places and reshapes architecture with automatic contextual detail. Conway Signal has a required shutdown predicate and spends dice, supplies and fuel before settlement. | Near, `0.062500` |

## Taxonomy impact

Eleven boundaries separate role assignment, dice use, travel,
skill-dependent outcome, cycle renewal, parallel successor clocks,
contract pressure, crew stress, individual dice wear, the visible
forecast and payment. The existing self-paced action rule is reused.

## Negative results

- Nia is optional in the observed crew selector. Serafin is locked.
- The access clocks are not themselves the two disable results.
- Supplies are useful but not the same as the required route fuel.
- The 200 cryo is credited after the successful return. A display of
  the offer or the separate local success scene is not a payment.
- The exact probability model and failure payout were not established.

## Delta summary

Twelve admitted genes, eleven new and one reused. One sampled retail
contract with the platform attribution and full outcome sources stated
separately.

## New facts

- Different crew choices change each cycle's available dice rather
  than only changing the dialogue.
- The terminated drone and the successful Hexport payment are
  separate observations on the same route.

## Principles and design implications

Give each crew member a small accountable pool and expose the part of
the risk that is known before commitment. Let two different progress
lines converge on one visible result, then settle payment at an
explicit return boundary.

## Puzzle or game generation potential

Offer two viable skill paths to each branch. Let a prepared crew spend
one resource to leave and another to preserve usable dice through the
work. Keep progress, actor condition and the contract's hazard separate.

## New genes

- ACT-897
- ACT-898
- CON-886
- INF-620
- OBJ-354
- SYS-1929
- SYS-1930
- SYS-1931
- SYS-1932
- SYS-1933
- SYS-1934

## New combinations

None. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[TAXONOMY_CHANGE_419](../../../research/taxonomy-changes/TAXONOMY_CHANGE_419.md).

## New questions

- What are the full action odds for each face and skill pairing?
- How does expiry of Drone Countermeasure interact with Drone Stress?
- How does the settled failure outcome vary with the route already completed?

## Next recommended game

Wave Race: Blue Storm on GameCube. Follow one scored Stunt Mode attempt.

## Why this game

The same contract visibly separates the travel requirement, the
cost of extending the field visit and payment after the return.
