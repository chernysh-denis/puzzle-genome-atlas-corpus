---
game_id: GAME-0694
slug: a-game-about-digging-a-hole
game_title: "A Game About Digging A Hole"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-130
    - ACT-443
    - ACT-913
  system:
    - SYS-1649
    - SYS-1968
    - SYS-1969
  constraint:
    - CON-890
  information:
    - INF-119
  objective: []
  time: []
---

# Game: A Game About Digging A Hole

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The first trips make a widening hole both a source of saleable
material and a route the player must leave while still powered.

## Analysis scope

- Version / ruleset: DoubleBee's commercial English Windows
  Steam base game, app 3244220, released February 7, 2025.
  The captures show the early retail yard loop. Neither
  recording identifies its exact installed depot or build.
- Structured analysis target: PLAT-WINDOWS-PC in
  [platform coverage](../../platforms/games.json).
- Entry: stand on the lawn with the initial hand trowel,
  the orange cross intact, an empty backpack and no money.
- Primary decision loop: remove local soil and take ore,
  monitor remaining charge and carrying capacity, walk back
  to the workshop and sell the load. Choose between buying
  charge immediately to keep digging and saving for a shovel
  that removes a larger volume per use.
- Positive terminal: buy the first shovel tier and return
  to the existing shallow cut with the improved tool available.
  This is a study boundary chosen by the analyst.
- Failure and restart: exhausting the battery in the main
  recording interrupts digging, removes unsold ore and
  returns control above ground. The credited wallet and the
  hole remain. Recovery charge and health are not quantified.
- Included: ordinary movement, soil removal and ore transfer,
  finite starting capacity, visible battery and health, the
  workshop sale and recharge commands, and the first shovel
  upgrade.
- Excluded: higher upgrade tiers, optional inventory or
  health purchases, explosives, powered ascent, deeper
  encounters, the final cache, achievements, later save
  behavior, other platforms and separate games or products.
- Potential scoped module: compare the exit problem once the
  hole is deeper and powered ascent competes with the shovel
  for charge.
- Direct-play status: no personal Windows session or binary
  inspection. The sampled runs establish the transitions below.
  Frames were inspected silently in the background and do not
  supply key-event telemetry or executable identity.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DIG-001 | The commercial Windows base game launched on Steam on February 7, 2025. The publisher describes digging, sales and tool upgrades as the ordinary loop. | Confirmed | Direct | High | P1, P2 |
| DIG-002 | The hand trowel removes continuous patches beneath the aimed contact. A first stone appears partly inside the cut. Continued excavation credits it to inventory while the cut remains. | Observation | Corroborated | High | W1 2:01–2:28, W2 3:19–3:31 |
| DIG-003 | The starting inventory totals one unit after the first stone and up to three units across ore types. Attempts at capacity show the inventory-full warning. | Observation | Corroborated | High | W1 2:25–2:28 and 3:47–3:55, W2 3:25–3:33 |
| DIG-004 | The workshop computer displays ore lines, counts, unit prices and a single sale. Confirmation clears the basket and increases the wallet by the quoted sum. Stone is worth one dollar and coal two dollars in the recorded fixture. | Observation | Corroborated | High | W1 3:12–3:18 and 5:20–5:24, W2 3:35–3:41 |
| DIG-005 | Digging reduces the displayed energy reserve. Buying the early one-dollar charge in the workshop debits the balance and restores the blue meter. | Observation | Corroborated | High | W1 2:04–2:28 and 3:19–3:24, W2 4:08–4:23 |
| DIG-006 | At battery exhaustion W1 displays ore loss and returns above ground. The displayed five-dollar balance and the same hole survive this interruption. | Observation | Direct | High | W1 4:23–4:44 |
| DIG-007 | The console offers the first shovel tier for five dollars and shows a radius change from 13 to 20 cm. After purchase the wallet falls from seven dollars to two, the next tier is offered, and the improved shovel is available on return to the cut. | Observation | Direct | High | W1 5:21–5:36 |

## Basic data

- Release / origin: DoubleBee, Windows Steam app 3244220.
  The reviewed Steam page credits rokaplay select and Drillhounds
  as publishers.
- Mechanical family: FAM-014. Each local cut changes reachable
  space and can create a route that must be retraced.
- P1: [Steam commercial Windows release](https://store.steampowered.com/app/3244220/A_Game_About_Digging_A_Hole/).
  Establishes title, store credits, date, platform and the
  high-level excavation, sale and equipment loop.
- P2: [rokaplay's Windows release announcement video](https://www.youtube.com/watch?v=4pCvvyzFlXA).
  Publisher evidence for the selected release, independent of
  the observed early-shop prices.
- W1: [Nespeshnyi Letsplei's retail PC capture](https://www.youtube.com/watch?v=6f1yfBPJiU0&t=120s).
  Use 2:01–2:28 for the first stone, 3:12–3:24 for sale
  and recharge, 4:23–4:44 for exhaustion, and 5:20–5:36
  for the first shovel.
- W2: [Lollijingjing's edited Steam capture](https://www.youtube.com/watch?v=2TJwtHGjxqA&t=199s).
  The initial basket reaches three units at 3:25–3:33 and
  settles to three dollars at 3:35–3:41. The charge around
  4:17–4:20 leaves two dollars. This witness corroborates the
  loop with a different first basket.
- Claim IDs: DIG-001–DIG-007.

### Reproducible fixture evidence

1. Aim the starter trowel at the orange cross. In W1 the
   first cut interrupts the paint and repeated excavation
   exposes a blue-gray stone. Continue into its contact.
   The stone disappears while the cut remains. Open the
   inventory to verify one stone and one of three spaces
   used at 2:27–2:28.
2. In W1 walk back to the workshop with two stones. At 3:14
   the computer quotes two dollars while the wallet shows zero.
   Confirm the sale and observe the empty quote and two-dollar
   balance. W2 instead sells a three-unit basket for three dollars.
3. Walk to the upgrade panel. W1 shows the one-dollar charge
   and low blue reserve. Use the service. Check the single
   debit and full blue reserve by 3:23.
4. For the negative branch, keep digging until the warning
   advances to exhaustion. W1 shows the interruption at 4:38.
   On the surface the same cut and five credited dollars
   remain, while the notice records loss of unsold ore.
5. For the first upgrade, continue shallow loads and sales.
   W1's 5:21 quote prices two stones and one coal at four
   dollars. Selling raises three dollars to seven. Buy the
   shovel at 5:24–5:27, then return to the cut by 5:36.

## Mechanical decomposition

### Action Genes

- ACT-008: walk between the changing excavation and workshop.
  DIG-002, DIG-004–DIG-007.
- ACT-130: buy a single offered recharge or shovel tier with
  the current wallet. DIG-005, DIG-007.
- ACT-443: carve continuous local terrain and credit exposed
  deposit material during excavation. DIG-002.
- ACT-913: confirm one sale for the entire quoted ore basket
  at the local computer. DIG-004.

### System Behaviour Genes

- SYS-1649: the paid shovel tier remains available after
  leaving the upgrade panel and returning to the pit. DIG-007.
- SYS-1968: successive accepted digs draw down the battery,
  which can be restored with a paid workshop service. DIG-005.
- SYS-1969: battery exhaustion returns the player to the
  surface and clears unsold ore while retaining credited
  money and excavation geometry. DIG-006.

### Constraint Genes

- CON-890: each retained ore unit occupies one place in the
  shared current capacity even though inventory groups the
  quantities by type. The initial budget is three. DIG-003–DIG-004.

### Information Genes

- INF-119: the blue battery and red health reserves are
  separate, and the charge warns before exhaustion. DIG-005–DIG-006.

### Objective Genes

None admitted. The first equipment purchase is an analysis
endpoint within the player-directed early loop.

### Time Genes

None admitted. The observed budget is tied to digging.
There is no demonstrated deadline in this interval.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Uncut cross and empty inventory | Dig into the marked lawn and the exposed stone | The cut opens, inventory shows one stone at one of three places used | DIG-002–DIG-003 |
| Three retained ore units | Attempt a further acquisition | Full-inventory warning and no additional carried unit | DIG-003 |
| Two stones and zero dollars in W1 | Confirm the computer's sale | Both stones leave the basket, wallet credits two dollars | DIG-004 |
| Low battery and two dollars in W1 | Buy the offered charge | Blue battery refills, wallet retains one dollar | DIG-005 |
| No remaining battery and five credited dollars in W1 | Battery interruption | Control resumes above ground, unsold ore is lost, balance and pit persist | DIG-006 |
| Seven dollars and base shovel after a sale | Buy the first shovel tier and walk back | Two dollars at purchase, larger shovel carried to the retained pit | DIG-007 |

## Strategic and experiential structure

Charge can finance another trip only through the same money
used to buy the better tool. Carrying capacity and remaining
charge independently inform a turnaround. Selling a partial
load can buy a refill and protect the money from losing that
ore in the hole.

## Replay and variation

W1's first recorded sale contains two stones. W2 reaches
capacity and sells three stone units. The early refill still
costs one dollar in both runs. The evidence does not identify
the deposition seed or whether that first deposit is random.

## Adjacent systems and history

Inventory, shovel, battery and ascent offers share the
upgrade panel. The fixture stops before deeper travel makes
powered ascent a meaningful cost and before save retention
across sessions matters.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-130, ACT-443, ACT-913 | Walk, buy one offer, excavate and sell the quoted load |
| System Behaviour | SYS-1649, SYS-1968, SYS-1969 | Keep the bought shovel, spend and replenish charge, recover from exhaustion |
| Constraint | CON-890 | Bound the total carried ore by one shared unit cap |
| Information | INF-119 | Disclose health and battery separately |
| Objective | None | Fixture ends at a research boundary |
| Time | None | No separate temporal rule is established |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `693` (`GAME-0001`–`GAME-0693`).
- Exact genome matches: none.
- Tied near matches: `GAME-0266` — Deep Rock Galactic (`4 / 23 = 0.173913`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Deep Rock Galactic (GAME-0266)](deep-rock-galactic.md) | Walk through a spatial mine, use a carving tool to collect material, buy a local offer and read personal reserves. | The Mining Expedition treats cave excavation as a way to reach and deliver quota minerals during a hazardous mission. The shallow yard uses a small unbanked load, an explicit local sale and a payable tool battery while the player funds a larger shovel. | Near, `0.173913`. |

## Taxonomy impact

Reuse continuous excavation and the paid equipment-node
transition. Isolate the one-confirmation sale, the pooled
ore cap, the funded charge loop and the selective recovery
on zero power.

## Negative results

- Excavating a stone does not add spendable money.
- The first sale need not wait for a full bag.
- Running out of charge does not restore the lawn or subtract
  the five dollars that were previously credited in W1.
- The fixture does not require a jump upgrade, a late enemy
  or a deadline.

## Delta summary

Nine genes describe the opening trade among local terrain
work, ore carried before sale and power to continue digging.

## New facts

- The initial total ore capacity spans the separate material lines.
- The sale discloses its total before a single confirmation.
- Loss at zero energy affects unsold ore, and the existing hole remains.

## Principles and design implications

Moving collected units into a credited wallet changes their
exposure to loss. A refill makes that wallet a short-term
operating budget as well as the route to an upgrade.

## Puzzle or game generation potential

Prototype a short excavation with a priced refill, a small
common carry cap and pockets of varying sale value. Test
which partial loads make it worth returning to the surface
before the cap or battery is exhausted.

## New genes

- ACT-913
- CON-890
- SYS-1968
- SYS-1969

## New combinations

None. None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 440](../../../research/taxonomy-changes/TAXONOMY_CHANGE_440.md).

## New questions

- Is there a dependable way to predict which partly exposed
  bodies yield material before committing another strike?
- At what depths does ascent create a separate resource
  calculation for the return trip?

## Next recommended game

Continue Selection 060 with GAME-0695, Terranigma on the
English European Super NES release.

## Why this game

The first sale, refill and tool tier establish an excavation
economy without requiring late machinery or a completion run.
