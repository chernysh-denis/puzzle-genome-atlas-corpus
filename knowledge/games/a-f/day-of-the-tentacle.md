---
game_id: GAME-0088
slug: day-of-the-tentacle
game_title: Day of the Tentacle
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0088
gene_ids:
  action:
    - ACT-089
    - ACT-091
  system:
    - SYS-115
  constraint:
    - CON-136
    - CON-139
  information:
    - INF-001
    - INF-038
  objective:
    - OBJ-046
  time:
    - TIM-002
---

# Game: Day of the Tentacle

## Analysis scope

- Version / ruleset: Day of the Tentacle Remastered, restricted to Hoagie's
  super-battery commission in Red Edison's laboratory, from handing over the
  patent application with all three ingredients already acquired through
  collecting the newly built uncharged battery from the shelf.
- Included: giving the patent application; Red's disclosed request for oil,
  vinegar and gold; handing in those three distinct inventory identities;
  persistent partial ingredient accumulation; rejection of unsupported or
  duplicate hand-ins; automatic device construction after the exact set;
  collecting the battery; visible inventory and shelf state; self-paced input.
- Excluded: obtaining the patent and ingredients; cross-era item transfer;
  wine-to-vinegar transformation and the gold-pen puzzle; charging the battery
  with Franklin's kite; powering the Chron-O-John; other characters, narrative,
  dialogue branches, full campaign, art mode and platform features.
- Direct-play status: not conducted. Double Fine establishes the remastered
  product and its three-character time-travel puzzle-adventure form. Three
  independent walkthroughs agree that the patent elicits the exact ingredient
  list, the three items are given separately, Red constructs the battery and
  Hoagie collects it. The local verifier formalises only that bounded exchange.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DOTT-001` | Day of the Tentacle is LucasArts' 1993 cartoon puzzle adventure, remastered by Double Fine in 2016 | Confirmed | Direct | High | F1 |
| `DOTT-002` | Giving the patent application to Red Edison discloses that oil, vinegar and gold are required to fabricate the super-battery | Confirmed | Corroborated | High | S1–S3 |
| `DOTT-003` | Oil, vinegar and the gold-plated quill are handed to Red as distinct inventory identities | Confirmed | Corroborated | High | S1–S3 |
| `DOTT-004` | Partial hand-ins persist and Red waits until the required set is complete | Confirmed | Corroborated | High | S1–S3 |
| `DOTT-005` | After the final ingredient Red automatically constructs an uncharged super-battery and places it on the shelf | Confirmed | Corroborated | High | S1–S3 |
| `DOTT-006` | Hoagie must separately collect the completed battery from the shelf | Confirmed | Corroborated | High | S1–S3 |
| `DOTT-007` | The executable control contains six accepted milestones, one exact three-ingredient set, one NPC-built device and six tested prerequisite rejections | Observation | Direct | High | V1, DOTT-002–DOTT-006 |
| `DOTT-008` | Hoagie never combines the ingredients directly and the scoped construction has no expiring constituent state | Observation | Corroborated | High | S1–S3 |

## Basic data

- Release / origin: originally released by LucasArts in 1993; the analysed
  remaster was released by Double Fine on 22 March 2016.
- Platform or physical form: single-player cartoon point-and-click adventure
  with character-specific inventories and addressed verb/object interaction.
- Puzzle family: NPC-mediated exact-set inventory commission.
- Primary source:
  - **[F1]** [Double Fine — Day of the Tentacle Remastered](https://www.doublefine.com/games/day-of-the-tentacle-remastered?platform=all),
    for the 1993 origin, 2016 remaster, platforms and three-friend time-travel
    puzzle-adventure premise.
- Reproducible corroboration:
  - **[S1]** [GameFAQs — Day of the Tentacle Remastered walkthrough](https://gamefaqs.gamespot.com/pc/187889-day-of-the-tentacle-remastered/faqs/44900),
    for patent hand-in, disclosed ingredient list and battery objective.
  - **[S2]** [Adventure Gamers — Day of the Tentacle walkthrough](https://adventuregamers.com/walkthroughs/day-of-the-tentacle),
    for separate oil, vinegar and quill hand-ins, automatic construction and
    shelf collection.
  - **[S3]** [Andrew Ferrier — complete Day of the Tentacle solution](https://www.andrewferrier.com/my-work/dott_solution/),
    independently corroborating the patent, three hand-ins and battery pickup.
  - **[V1]**
    [`verify_day_of_the_tentacle_control.py`](../../../scripts/verify_day_of_the_tentacle_control.py),
    an executable state machine for six milestones, the exact ingredient set,
    automatic construction and six invalid prerequisites.

## Mechanical decomposition

### Player actions

- `ACT-089` — collect addressed scene item into inventory. After Red finishes,
  Hoagie deliberately takes the uncharged super-battery from its shelf.
- `ACT-091` — give held item to addressed character. The patent and each of the
  three requested ingredients are selected and transferred to Red Edison.

### System behaviours

- `SYS-115` — recipient accumulates typed hand-ins and constructs fixed output.
  Red retains each accepted ingredient; completing the requested set triggers
  automatic fabrication of exactly one uncharged super-battery on the shelf.

### Constraints

- `CON-136` — persistent prerequisite-gated mechanism dependency. The patent
  precedes ingredient acceptance, completed ingredient accumulation precedes
  construction, and construction precedes collection.
- `CON-139` — exact distinct typed hand-in set. The commission requires one oil,
  one vinegar and one gold-plated quill; unsupported identities, duplicates and
  incomplete subsets cannot produce the battery.

### Information

- `INF-001` — fully visible current state. Hoagie's current inventory, accepted
  remaining ingredients and the constructed battery's shelf presence are
  inspectable at their respective decisions.
- `INF-038` — addressed recipient discloses exact multi-item commission. Red's
  response to the patent names oil, vinegar and gold before any ingredient
  hand-in is required.

### Objective

- `OBJ-046` — obtain specified device through intermediary construction. The
  bounded packet completes only when Red has transformed the exact commission
  set and Hoagie has collected the resulting uncharged super-battery.

### Time

- `TIM-002` — self-paced sequential action. Red's partial ingredient state does
  not decay, and the battery waits on the shelf until Hoagie collects it.

## Reproducible transitions

The executable control encodes this accepted trace:

1. Give the patent application to Red Edison.
2. Receive the exact request for oil, vinegar and gold.
3. Hand in oil, vinegar and the gold-plated quill as three distinct identities.
4. Complete the exact set and trigger Red's automatic battery construction.
5. Collect the uncharged super-battery from the shelf.

Six controls reject an ingredient before the recipe, an unsupported item,
collection before construction, duplicate patent hand-in, unsupported hand-in
after disclosure and a duplicate accepted ingredient. An incomplete two-item
set is separately asserted not to construct the output.

## Strategic and experiential structure

- The patent is a commissioning input rather than a recipe constituent: its
  hand-in changes what Red communicates and which later items he accepts.
- Progress is monotonic but order-flexible across the three ingredients. Each
  accepted identity reduces the remaining exact set without requiring direct
  item–item combination.
- Red externalises crafting. The player's decision is whom to give which item,
  while the system performs the deterministic transformation only after the
  recipient owns the complete set.
- The separate shelf pickup keeps construction and acquisition distinct: an
  output can exist visibly in the scene before entering player inventory.

## Replay and variation

- The requested ingredient identities and resulting device are fixed.
- Oil, vinegar and gold may be handed in in any order once the patent has been
  accepted; their partial set persists without a deadline.
- Ingredient-acquisition routes contain substantial cross-era puzzles but are
  outside this narrow commission record.

## Adjacent systems and history

- Machinarium is the nearest corpus control because both use addressed item
  hand-ins inside a persistent prerequisite chain. Its one requested doll
  grants an avatar component immediately; Day of the Tentacle instead
  accumulates three distinct ingredients and constructs an inanimate device.
- The Longest Journey directly combines inventory identities and depends on a
  decaying material state. Neither boundary survives here because Red, not the
  player, owns and transforms the complete set without time pressure.
- Ordinary multi-item fetch quests remain outside `SYS-115` unless the recipient
  persistently aggregates a typed set and produces one fixed constructed output.

## Normalised genome

| Type | IDs | Key parameters |
|---|---|---|
| Action | `ACT-089`, `ACT-091` | four addressed hand-ins; one shelf pickup |
| System | `SYS-115` | persistent accumulation; one deterministic constructed output |
| Constraint | `CON-136`, `CON-139` | patent gate; exact three-identity ingredient set |
| Information | `INF-001`, `INF-038` | visible current state; disclosed oil/vinegar/gold list |
| Objective | `OBJ-046` | obtain the uncharged super-battery |
| Time | `TIM-002` | self-paced; no expiry |

Compact signature:

`ACT-089,ACT-091; SYS-115; CON-136,CON-139; INF-001,INF-038; OBJ-046; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `87` (`GAME-0001`–`GAME-0087`).
- Exact genome matches: none.
- Tied near matches: `GAME-0086` — Machinarium (`5 / 17 = 0.294118`).
- Supported combination subsets: `COMB-0088`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0086`.

## Combination candidate

- Candidate ID: `COMB-0088`.
- Gene set: `ACT-091`, `SYS-115`, `CON-139`, `INF-038`, `OBJ-046`.
- Supporting game: `GAME-0088`.
- Proper-subset rationale: `ACT-089`, `CON-136`, `INF-001` and `TIM-002`
  support pickup, ordering, visibility and pace but do not define the disclosed
  exact-set commission and intermediary construction.
- Novelty claim: not assessed.

## Outcome

- Reused genes: `ACT-089`, `ACT-091`, `CON-136`, `INF-001`, `TIM-002`.
- Added genes: `SYS-115`, `CON-139`, `INF-038`, `OBJ-046`.
- Added combination: `COMB-0088`.
- Evidence gate: passed with Double Fine's product record, three independently
  agreeing walkthroughs and one executable commission verifier.
- Nearest prior genome: Machinarium; see `Corpus comparison` for the current
  result.
- Next falsification target: a recipient-accumulated exact item set whose
  completion grants access or status rather than constructing a new object.

## Taxonomy impact

- Character hand-in now has two demonstrated result families: immediate
  capability-component reward and persistent multi-item intermediary crafting.
- The requested item information is separated by cardinality and function:
  one pictured identity differs operationally from an exact verbal recipe set.
- Direct player combination remains absent even though ordinary language calls
  the result “crafted”; responsibility for the state transformation matters.

## Negative results

- Ingredient acquisition, time travel and cross-character flushing are outside
  this bounded commission and cannot support its genes.
- Red's construction animation is not a player action; it is the deterministic
  system consequence of the completed set.
- The uncharged battery is a fixed authored output, not random loot or a recipe
  discovery system.
- Dialogue flavour around Red is excluded except for the exact mechanically
  actionable ingredient disclosure.
- The verifier proves set acceptance and construction, not all permissible
  dialogue or ingredient-order animations in every remastered platform build.
