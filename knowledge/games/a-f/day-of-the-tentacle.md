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

The comparison scanned every complete `GAME-0001`–`GAME-0087` signature with
canonical Jaccard intersection over union.

- Near match: `GAME-0086` Machinarium is uniquely nearest at
  `5 / 17 = 0.294118`.

| Prior game | Shared genes | Boundary | Jaccard |
|---|---|---|---:|
| `GAME-0086` — Machinarium | `ACT-089`, `ACT-091`, `CON-136`, `INF-001`, `TIM-002` | one requested item immediately grants an avatar leg; no exact accumulated set or constructed device | nearest, `5 / 17 = 0.294118` |
| `GAME-0064` — SET | `INF-001`, `TIM-002` | identifies one relational card triple; no inventory hand-in or intermediary | next, `2 / 12 = 0.166667` |
| `GAME-0080` — Keen | `INF-001`, `TIM-002` | completes arithmetic cages and a Latin square; no addressed item transfer | background tie, `2 / 14 = 0.142857` |
| `GAME-0087` — The Longest Journey | `CON-136`, `INF-001` | directly builds a timed composite tool; no recipient accumulation | boundary control, `2 / 17 = 0.117647` |

No prior full signature is exact, no prior combination equals the candidate and
no prior combination is a supported subset of the complete genome. Machinarium
therefore validates the action-level continuity while the moderate similarity
confirms that multi-item accumulation and intermediary fabrication require
separate system, constraint, information and objective boundaries.

- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `1 / 22 = 0.045455`; `GAME-0002`: `2 / 14 = 0.142857`; `GAME-0003`: `0 / 18 = 0.000000`; `GAME-0004`: `1 / 23 = 0.043478`; `GAME-0005`: `2 / 14 = 0.142857`; `GAME-0006`: `2 / 16 = 0.125000`; `GAME-0007`: `2 / 15 = 0.133333`; `GAME-0008`: `2 / 14 = 0.142857`.
  - `GAME-0009`: `1 / 24 = 0.041667`; `GAME-0010`: `1 / 17 = 0.058824`; `GAME-0011`: `2 / 20 = 0.100000`; `GAME-0012`: `2 / 16 = 0.125000`; `GAME-0013`: `1 / 21 = 0.047619`; `GAME-0014`: `1 / 23 = 0.043478`; `GAME-0015`: `1 / 22 = 0.045455`; `GAME-0016`: `1 / 23 = 0.043478`.
  - `GAME-0017`: `0 / 22 = 0.000000`; `GAME-0018`: `1 / 27 = 0.037037`; `GAME-0019`: `1 / 18 = 0.055556`; `GAME-0020`: `1 / 22 = 0.045455`; `GAME-0021`: `1 / 17 = 0.058824`; `GAME-0022`: `1 / 20 = 0.050000`; `GAME-0023`: `1 / 18 = 0.055556`; `GAME-0024`: `1 / 20 = 0.050000`.
  - `GAME-0025`: `1 / 19 = 0.052632`; `GAME-0026`: `1 / 20 = 0.050000`; `GAME-0027`: `1 / 20 = 0.050000`; `GAME-0028`: `1 / 25 = 0.040000`; `GAME-0029`: `1 / 20 = 0.050000`; `GAME-0030`: `1 / 22 = 0.045455`; `GAME-0031`: `1 / 19 = 0.052632`; `GAME-0032`: `1 / 19 = 0.052632`.
  - `GAME-0033`: `1 / 21 = 0.047619`; `GAME-0034`: `1 / 22 = 0.045455`; `GAME-0035`: `1 / 26 = 0.038462`; `GAME-0036`: `2 / 19 = 0.105263`; `GAME-0037`: `1 / 17 = 0.058824`; `GAME-0038`: `1 / 24 = 0.041667`; `GAME-0039`: `2 / 16 = 0.125000`; `GAME-0040`: `2 / 15 = 0.133333`.
  - `GAME-0041`: `1 / 19 = 0.052632`; `GAME-0042`: `1 / 17 = 0.058824`; `GAME-0043`: `1 / 22 = 0.045455`; `GAME-0044`: `1 / 18 = 0.055556`; `GAME-0045`: `1 / 22 = 0.045455`; `GAME-0046`: `2 / 17 = 0.117647`; `GAME-0047`: `1 / 22 = 0.045455`; `GAME-0048`: `1 / 22 = 0.045455`.
  - `GAME-0049`: `0 / 18 = 0.000000`; `GAME-0050`: `1 / 23 = 0.043478`; `GAME-0051`: `1 / 24 = 0.041667`; `GAME-0052`: `1 / 18 = 0.055556`; `GAME-0053`: `1 / 17 = 0.058824`; `GAME-0054`: `1 / 19 = 0.052632`; `GAME-0055`: `1 / 18 = 0.055556`; `GAME-0056`: `1 / 16 = 0.062500`.
  - `GAME-0057`: `1 / 16 = 0.062500`; `GAME-0058`: `1 / 17 = 0.058824`; `GAME-0059`: `1 / 15 = 0.066667`; `GAME-0060`: `1 / 15 = 0.066667`; `GAME-0061`: `2 / 17 = 0.117647`; `GAME-0062`: `2 / 15 = 0.133333`; `GAME-0063`: `2 / 14 = 0.142857`; `GAME-0064`: `2 / 12 = 0.166667`.
  - `GAME-0065`: `1 / 15 = 0.066667`; `GAME-0066`: `1 / 18 = 0.055556`; `GAME-0067`: `0 / 17 = 0.000000`; `GAME-0068`: `1 / 16 = 0.062500`; `GAME-0069`: `2 / 15 = 0.133333`; `GAME-0070`: `1 / 16 = 0.062500`; `GAME-0071`: `2 / 14 = 0.142857`; `GAME-0072`: `2 / 15 = 0.133333`.
  - `GAME-0073`: `2 / 14 = 0.142857`; `GAME-0074`: `2 / 16 = 0.125000`; `GAME-0075`: `2 / 16 = 0.125000`; `GAME-0076`: `2 / 14 = 0.142857`; `GAME-0077`: `2 / 14 = 0.142857`; `GAME-0078`: `2 / 14 = 0.142857`; `GAME-0079`: `2 / 14 = 0.142857`; `GAME-0080`: `2 / 14 = 0.142857`.
  - `GAME-0081`: `2 / 15 = 0.133333`; `GAME-0082`: `2 / 15 = 0.133333`; `GAME-0083`: `2 / 15 = 0.133333`; `GAME-0084`: `2 / 17 = 0.117647`; `GAME-0085`: `2 / 18 = 0.111111`; `GAME-0086`: `5 / 17 = 0.294118`; `GAME-0087`: `2 / 17 = 0.117647`.

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
- Nearest prior genome: Machinarium at `5 / 17 = 0.294118`.
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

## Delta summary

- Added one reviewed game record and one verified combination.
- Added one System Behaviour, one Constraint, one Information and one Objective
  gene.
- Extended two Actions, one Constraint, one Information and one Time gene with
  Day of the Tentacle evidence.
- Added an executable six-milestone exact-set commission control.

## Нові факти

- Межу звужено до замовлення супербатареї в лабораторії Red Edison.
- Патент відкриває точний список: олія, оцет і золото.
- Гравець передає три предмети окремо; Red накопичує набір і сам автоматично
  створює батарею після останньої складової.
- Батарея спершу існує на полиці й лише потім окремо переходить до інвентарю.
- Перевірено шість віх, один точний трипредметний набір і шість порушень передумов.

## Нові гени

- `SYS-115` — отримувач накопичує типізовані передачі й створює фіксований результат.
- `CON-139` — точний набір різних типізованих предметів для передачі.
- `INF-038` — адресований отримувач повідомляє точне багатопредметне замовлення.
- `OBJ-046` — отримати визначений пристрій через конструкцію посередником.

## Нові комбінації

- `COMB-0088` — повідомлений точний набір передач у конструкцію посередником.

## Зміни таксономії

- `ACT-089`, `ACT-091`, `CON-136`, `INF-001` і `TIM-002` розширено доказами
  Day of the Tentacle.
- Автоматичну роботу Red відділено від прямого `ACT-090`: Hoagie не об'єднує
  предмети сам.

## Український підсумок

Супербатарея Day of the Tentacle показує іншу граматику інвентарного
«крафту». Hoagie передає патент Red Edison, отримує список з олії, оцту й золота
та віддає кожну складову окремо. Red стійко накопичує набір і лише після третьої
передачі автоматично створює батарею, яку треба окремо забрати з полиці.
Machinarium закономірно найближчий через спільні передачу предметів, pickup і
ланцюг передумов, але тут результат — не частина аватара, а створений
посередником пристрій: `5 / 17 = 0.294118`.
