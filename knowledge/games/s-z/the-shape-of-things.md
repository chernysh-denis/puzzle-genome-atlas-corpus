---
game_id: GAME-0721
slug: the-shape-of-things
game_title: "The Shape of Things"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-937
    - ACT-938
  system:
    - SYS-2016
    - SYS-2017
  constraint: []
  information:
    - INF-001
  objective:
    - OBJ-004
  time: []
---

# Game: The Shape of Things — first woodland objects

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
A compass, pine cone and backpack are instances of distinct assigned transforms.

## Analysis scope

- Version / ruleset: English Nintendo Switch eShop commercial
  base game, released 31 August 2023. Use the ordinary single-player
  opening shown by the Switch recording. Exact build and save
  identifiers were unavailable.
- Structured analysis target: `PLAT-NINTENDO-SWITCH`. Begin with
  the opening room balance of seven G-Coins and its first capsule
  offer. Confirm the exchange, enter the unlocked woodland
  capsule and restore the compass, pine cone and backpack.
  Stop when the mushroom appears with three G-Coins.
- Primary decision loop: turn the entire model to inspect a
  seam, cycle to the intended part and apply the transform
  assigned by the current puzzle. Compare the silhouette and
  surface markings with their neighbours. Upon acceptance,
  see the advance and coin before working on the next object.
- Included: the opening capsule exchange, selecting the
  capsule, view rotation, targeted rotation, translation and
  rescaling, visible geometry and the three automatic clear
  transitions.
- Excluded: solving the mushroom, later worlds and prices,
  repeat-clear payouts, draw probabilities and ordering,
  exact snap tolerances, save/reload persistence, DLC, room
  ambience and differences between later platform ports.
- Direct-play status: no personal Switch session or input
  trace. Nintendo's listing identifies the released target.
  One Switch-labelled recording visibly shows Switch control
  prompts. A separate Steam recording corroborates the early
  puzzle sequence. Only silent storyboards and selected
  background video frames were inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| ST-001 | Hyper Three Studio's Switch eShop base game released on 31 August 2023 with English and single-player support. The puzzle modes shown are rotation, translation and scaling. | Observation | Corroborated | High | P1, P2; W1 00:37–00:58, 01:15–02:07 |
| ST-002 | Confirming the first capsule offer consumes seven G-Coins, shows New world unlocked and makes the woodland capsule selectable beside the shelf. Entering that capsule begins the compass at a zero balance. | Observation | Corroborated | High | P1; W1 00:08–00:38; W2 00:48–01:06 |
| ST-003 | The whole-model context changes the displayed orientation while preserving relative parts. L and R select part focus; the right stick adjusts the current context, laterally for the selected compass part. The outlined part can move relative to its neighbours. | Observation | Corroborated | High | P2; W1 00:37–00:58 and 01:00–01:08; W2 01:05–01:17 |
| ST-004 | The first three objects assign different local transformations: turning a compass band, sliding a pine-cone band and resizing a backpack band. Matching changes the relative seams; there is no free placement of loose pieces in this fixture. | Observation | Corroborated | High | P1, P2; W1 00:43–01:08, 01:15–01:53, 01:55–02:51; W2 01:13–02:05 |
| ST-005 | Restoring each object yields one coin and brings in the next object without a separate stage-selection step. W1 shows 0 to 1 to 2 to 3, then the mushroom. | Observation | Corroborated | High | P1; W1 01:08–01:16, 01:50–01:56, 02:50–02:59; W2 01:19–01:25, 01:41–02:08 |
| ST-006 | Partial matches lead to more editing. The three objects are untimed; there is no move-budget failure in the published base rules. | Observation | Corroborated | High | P1, P2; W1 00:48–01:06, 02:10–02:49 |

## Basic data

- Release / origin: developed and published by Hyper Three Studio.
  Nintendo identifies the North American digital Switch release as
  31 August 2023. The Steam edition launched on a different date
  and is used as corroboration for object rules.
- Platform or physical form: single-player Nintendo Switch digital
  base game. No Switch 2 or Steam behaviour is inferred beyond
  the stated cross-platform rule corroboration.
- Mechanical families: `FAM-003` for the bounded state changes and
  `FAM-006` for restoring a coherent assembly.
- Primary sources accessed 2026-11-25:
  - **P1:** [Nintendo eShop product page](https://www.nintendo.com/us/store/products/the-shape-of-things-switch/).
    Edition, release, language support, three transform classes,
    reward and capsule economy, and no pressure timer or punishment.
  - **P2:** [Hyper Three Studio's Steam product description](https://store.steampowered.com/app/1853410/The_Shape_of_Things/).
    Describes separately targeting one piece or the entire
    model and changing the view or assigned piece transform.
    Its mouse bindings are Windows evidence.
- Secondary and recorded play evidence:
  - **W1:** [Handheld Players, Nintendo Switch gameplay](https://www.youtube.com/watch?v=yTtNmEY__1A&t=8s).
    Capsule exchange 00:08–00:19, selecting it 00:25–00:36,
    inspection and compass edit 00:37–01:09, pine cone
    01:15–01:53 and backpack 01:55–02:53. The mushroom
    enters by 02:59.
  - **W2:** [Crystal Dreams, Steam playthrough](https://www.youtube.com/watch?v=3YEeXMMcrjM&t=48s).
    Opening base-game capsule sequence at 00:48–02:08.
    Only the first base-game portion was used. Later DLC in
    this recording sits outside the fixture.
- Claim IDs: `ST-001`–`ST-006`. For a direct replay, capture
  opening balance, shop confirmation, unlocked world and
  control context. Rotate the whole compass, then edit the
  outlined slice from the same view. Record coin and successor
  after each of the initial three clears.

## Mechanical decomposition

### Action Genes

- New `ACT-937`: turn the whole object for inspection. All
  relative seam states persist through the view change (`ST-003`).
- New `ACT-938`: address one band, then edit its assigned
  transform. The compass rotates, the cone slides and the
  backpack scales; addressing a new part alone leaves its
  geometry unchanged (`ST-003`, `ST-004`).

### System Behaviour Genes

- New `SYS-2016`: accepting the reassembled object emits clear
  feedback, credits one coin and advances the set (`ST-005`).
- New `SYS-2017`: the confirmed capsule exchange debits the
  displayed price and opens a selectable world (`ST-002`).

### Constraint Genes

The assigned transform belongs to the meaning of `ACT-938`.
Exact geometric acceptance bounds and rejection predicates
were not measured. No additional constraint gene is admitted.

### Information Genes

- Reuse `INF-001`: inspect the current band geometry and markings
  by turning the object. The visible outline identifies the
  current selection without changing its geometry (`ST-003`).

### Objective Genes

- Reuse `OBJ-004`: reconstruct the coherent shape from the
  existing parts, as confirmed by the local clear (`ST-004`, `ST-005`).

### Time Genes

There is no gameplay timer or move depletion in the scoped
three-object sequence (`ST-006`).

## Formal state and transitions

Let the room state contain the G-Coin balance and which capsule
world is selectable. The live puzzle state contains the current
object, one transform parameter for each authored band, its
focus and the whole-model view. View rotation preserves all
band parameters. Editing a band changes its own referenced
parameter. The accepted shape settles a coin and advances the
object pointer.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Opening room has seven G-Coins and the first exchange prompt | Confirm the exchange | Balance reaches zero and the delivered woodland capsule becomes available | ST-002 |
| Woodland capsule is unlocked on the shelf | Select it | Compass appears with a zero balance | ST-002 |
| Compass has mismatched bands and the whole model is addressed | Turn the model | Inspection angle changes while the relative mismatch remains | ST-003 |
| Compass band is outlined after shoulder selection | Adjust the band with lateral right-stick input | It turns relative to its neighbours. Alignment settles one coin and the cone enters | ST-003, ST-004, ST-005 |
| Pine-cone bands have displaced silhouettes | Adjust the parts in their slide mode | Matching the whole shape yields the second coin and the backpack enters | ST-004, ST-005 |
| Backpack bands have inconsistent scale | Grow or shrink the selected parts until their outlines fit | The accepted backpack adds the third coin. The mushroom is the next active object | ST-004, ST-005 |

## Strategic and experiential structure

A seam can be visually obscured even when its current state
is inspectable. Rotating the view lets the player compare
contours before changing the selected band. The taught modes
change one parameter at a time. The post-clear coin makes the
local success useful in the room economy.

## Replay and variation

Both recordings show the same beginning of the woodland
sequence with different inspection and adjustment paths.
Switch has a shoulder selection and stick adjustment. The
Steam witness uses a pointer. Successful routes establish
the shared outcome, without determining exact input timing
or the effect of replaying a cleared object.

## Adjacent systems and history

Further puzzles use other object shapes and may combine
transforms. The room includes atmosphere controls and the
capsule machine. Later draw distribution, full set size and
full-world completion are outside this scope.

## Normalised genome

- Action: ACT-937, ACT-938.
- System Behaviour: SYS-2016, SYS-2017.
- Constraint: none.
- Information: INF-001.
- Objective: OBJ-004.
- Time: none.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `720` (`GAME-0001`–`GAME-0720`).
- Exact genome matches: none.
- Tied near matches: `GAME-0002` — Rubik’s Cube (`2 / 11 = 0.181818`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Rubik’s Cube (GAME-0002)](../m-r/rubiks-cube.md) | INF-001, OBJ-004 | Both expose inspectable geometry and require a declared reconstructed shape. Rubik’s Cube turns a coupled layer and permutes shared edge and corner cubies. The woodland puzzles independently adjust one retained band using a prescribed rotation, slide or scale. Each accepted object credits a coin and advances the capsule sequence. | Near, `0.181818`. |

## Taxonomy impact

Reuse inspectable current state and target reconstruction.
Separate whole-model inspection from changing one band.
Record the automatic reconstruction settlement and the
room's distinct paid capsule unlock. Transform classes are
parameters of one addressed edit rule.

## Negative results

- Turning the model as a whole does not repair relative seams.
- Sending the same adjustment input to a different object can
  change a different physical parameter.
- The initial capsule unlock is a separate confirmed transaction.
  Awarding a coin after a local clear does not itself dispense
  another capsule.
- The footage cannot establish exact alignment tolerances,
  replay payout or the installed Switch patch.

## Delta summary

Start from the paid woodland unlock. Distinguish whole-model
inspection, part focus and the assigned rotation, translation
or scale. End after the third accepted configuration and its
credited coin, with the next object ready.

## New facts

- A single inspection control and a targeted geometry edit
  operate in separate focus contexts.
- The early sequence demonstrates three assigned transforms in order.
- An accepted object advances automatically and adds one G-Coin
  to the balance. The machine exchange is a separate event.

## Principles and design implications

Keep inspection non-destructive and make part focus legible.
Teach one geometry operation on one recognisable model before
asking the player to infer its use elsewhere.

## Puzzle or game generation potential

Choose a three-dimensional object with prominent seams and
cut it into a few retained bands. Distort one band with an
independent parameter. Verify its inverse transformation
allows exact reassembly after arbitrary inspection turns.

## New genes

- ACT-937
- ACT-938
- SYS-2016
- SYS-2017

## New combinations

None.

## Taxonomy changes

[Taxonomy Change 467](../../../research/taxonomy-changes/TAXONOMY_CHANGE_467.md).

## Next recommended game

QuackShot Starring Donald Duck on the original North American
Sega Genesis cartridge is the next Selection 063 unit.

## Why this game

One authored set separates inspection from the geometry it
changes and shows how verified local clears feed room progress.

## Review status

Reviewed 2026-11-25 for the first woodland capsule sequence
on English Nintendo Switch.
