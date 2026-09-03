---
game_id: GAME-0087
slug: the-longest-journey
game_title: The Longest Journey
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0087
gene_ids:
  action:
    - ACT-087
    - ACT-090
    - ACT-092
  system:
    - SYS-114
  constraint:
    - CON-136
    - CON-138
  information:
    - INF-001
    - INF-037
  objective:
    - OBJ-045
  time:
    - TIM-003
---

# Game: The Longest Journey

## Analysis scope

- Version / ruleset: Funcom's released Windows edition of The Longest Journey,
  restricted to the Chapter 1 subway-key tool packet after April has acquired
  the clamp, clothesline and rubber ducky and before the recovered iron key is
  used elsewhere.
- Included: close inspection of the ducky; exposing and removing its Band-Aid;
  combining clamp with clothesline; inflating the unpatched ducky; combining it
  with the first composite; decay of inflation while the player can still act;
  composite expiry and retry; applying the completed fishing instrument to the
  dangerous track area; acquiring the iron key; persistent inventory state.
- Excluded: acquisition puzzles for the three starting constituents; subway
  pass purchase and travel; every later use of the key or Band-Aid; dialogue,
  narrative branches and parallel worlds; full campaign; cursor cosmetics,
  voice acting, saves, achievements and platform differences.
- Direct-play status: not conducted. Funcom's manual directly documents close
  inventory inspection, subpart manipulation, two-item combination and
  item-to-scene application. Three walkthroughs independently agree on the
  clamp–line–inflated-ducky assembly, timed deflation and key retrieval. The
  local verifier encodes only those corroborated state transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TLJ-001` | The Longest Journey is a Funcom graphical adventure controlled through April Ryan | Confirmed | Direct | High | F1, F2 |
| `TLJ-002` | The interface permits close inspection of held items, interaction with their subparts, inventory-item combination and application to a scene target | Confirmed | Direct | High | F2 |
| `TLJ-003` | Close inspection of the rubber ducky exposes a removable Band-Aid over its leak | Confirmed | Corroborated | High | S1–S3 |
| `TLJ-004` | Clamp and clothesline combine into the first persistent composite | Confirmed | Corroborated | High | S1–S3 |
| `TLJ-005` | The unpatched ducky must be inflated and combined with that first composite to hold the clamp open | Confirmed | Corroborated | High | S1–S3 |
| `TLJ-006` | Inflation decays in real time; if the player delays, the clamp closes and the tool must be prepared again | Confirmed | Corroborated | High | S2, S3 |
| `TLJ-007` | Timely application of the completed fishing instrument retrieves the iron key from beside the electrified rail | Confirmed | Corroborated | High | S1–S3 |
| `TLJ-008` | The executable control contains six accepted milestones, two staged combinations, one expiry reset and six tested prerequisite rejections | Observation | Direct | High | V1, TLJ-003–TLJ-007 |
| `TLJ-009` | The scoped packet constructs a tool without restoring April, exchanging with a character or changing avatar reach | Observation | Corroborated | High | S1–S3 |

## Basic data

- Release / origin: developed and published by Funcom; the current Steam
  product record lists 17 November 2000.
- Platform or physical form: single-player graphical point-and-click adventure
  with scene hotspots, close-up inventory views and combinable held items.
- Puzzle family: authored multi-item inventory construction under transient
  constituent state.
- Primary sources:
  - **[F1]** [The Longest Journey on Steam](https://store.steampowered.com/app/6310/The_Longest_Journey/),
    for developer, publisher, release record, protagonist and graphical
    adventure form.
  - **[F2]** [The Longest Journey manual](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/6310/manuals/manual_en.pdf?t=1675333329),
    especially pp. 15–17 for inventory acquisition, close-up subpart
    interaction, compatible item combination and item-to-scene application.
- Reproducible corroboration:
  - **[S1]** [Walkthrough King — The Longest Journey](https://www.walkthroughking.com/text/longestjourney.aspx),
    for the Chapter 1 clamp, clothesline, inflation, Band-Aid and key sequence.
  - **[S2]** [Adventure Gamers — The Longest Journey walkthrough](https://adventuregamers.com/walkthroughs/the-longest-journey),
    for the three item identities, their combination and track-key outcome.
  - **[S3]** [Plover — The Longest Journey solution](https://www.plover.net/~davidw/sol/TLJ.html),
    independently corroborating close inspection, Band-Aid removal, inflation,
    staged assembly, deflation window and key recovery.
  - **[V1]**
    [`verify_the_longest_journey_control.py`](../../../scripts/verify_the_longest_journey_control.py),
    an executable state machine for six milestones, two combinations, one
    transient inflation window, expiry recovery and six invalid prerequisites.

## Mechanical decomposition

### Player actions

- `ACT-087` — apply held item to compatible fixture. The completed fishing
  instrument is committed to the addressed track-key hotspot rather than used
  as generic equipment.
- `ACT-090` — combine two held inventory items. The player first replaces
  clamp and clothesline with a clamp-line composite, then replaces that and the
  inflated ducky with the completed three-part instrument.
- `ACT-092` — alter one held item's functional state. In close-up the player
  removes the Band-Aid without a second item and later inflates the retained
  ducky through the mouth interaction.

### System behaviours

- `SYS-114` — transient constituent decay invalidates composite use. Once the
  Band-Aid is removed, the inflated ducky loses air while interaction remains
  live; expiry closes the clamp and returns the assembly to a retryable state.

### Constraints

- `CON-136` — persistent prerequisite-gated mechanism dependency. Inspection
  gates Band-Aid removal, both first constituents gate the clamp-line, and the
  prepared ducky plus clamp-line gate the final assembly and key attempt.
- `CON-138` — transient held-item state gates composite compatibility and use.
  The second combination accepts the ducky only while inflated, and the final
  instrument retrieves the key only before that same inflation state expires.

### Information

- `INF-001` — fully visible current state. The inventory shows constituent or
  composite identities, close-up shows the Band-Aid, and the track scene shows
  the inaccessible key and electrical hazard.
- `INF-037` — close inspection exposes a manipulable held-item subpart. The
  ducky's removable Band-Aid hotspot is mechanically unavailable until the
  dedicated close-up view reveals it.

### Objective

- `OBJ-045` — retrieve inaccessible scene item with a constructed reach tool.
  The bounded packet completes when the composite clamp instrument removes the
  iron key from the hazard-adjacent track into April's inventory.

### Time

- `TIM-003` — real-time input during forced progression. After inflation, the
  ducky's air state advances toward expiry while the player must complete and
  apply the assembly; pausing between those actions is not mechanically free.

## Reproducible transitions

The executable control encodes this accepted trace:

1. Inspect the rubber ducky closely and expose its Band-Aid hotspot.
2. Remove the Band-Aid, making the retained ducky deliberately leaky.
3. Combine clamp and clothesline into the persistent first-stage composite.
4. Inflate the ducky and start its bounded decay window.
5. Combine the inflated ducky with the clamp-line assembly.
6. Apply the open-clamp instrument before expiry and retrieve the iron key.

Six controls reject Band-Aid removal without inspection, an incomplete first
combination, inflation while still patched, final assembly without inflation,
key retrieval without the complete tool and retrieval after a tested expiry.
The expiry control proves that deflation restores retryable constituents rather
than granting the key or creating an unrecoverable fail state.

## Strategic and experiential structure

- The puzzle makes close inspection productive: it changes the action graph by
  exposing a subpart, not merely by enlarging artwork or adding flavour text.
- The recipe is staged rather than flat. The first composite becomes a named
  constituent of the second, so three objects are assembled through two binary
  compatibility decisions.
- The Band-Aid is removed because leakage is useful. Preparation deliberately
  creates a temporary weakness that becomes the tool's closing mechanism.
- Real-time decay converts a self-paced inventory grammar into a short execute
  window: the player must understand the recipe before committing inflation.

## Replay and variation

- The item identities, compatibility graph, leak and target key are authored
  and deterministic.
- Delay can force repeated inflation and assembly, but does not randomise the
  solution or replace the constituents.
- The scope has one successful outcome; later use of the key belongs to a
  separate puzzle dependency and is excluded.

## Adjacent systems and history

- Graphic adventures commonly combine inventory items, but this packet is
  retained because a constituent's live temporary state persists into and
  controls the usability of the multi-item composite.
- Machinarium is the nearest corpus control: both combine held objects and
  apply the result through a persistent dependency chain. The Longest Journey
  removes pickup, character request, exchange and avatar restoration, while
  adding close-up subpart discovery and real-time expiry.
- The Room also exposes inventory close-ups, but its articulated key states are
  persistent and fixture-specific; they do not decay while the player acts.

## Normalised genome

| Type | IDs | Key parameters |
|---|---|---|
| Action | `ACT-087`, `ACT-090`, `ACT-092` | one target application; two binary combinations; remove patch and inflate |
| System | `SYS-114` | real-time inflation decay; retryable expiry |
| Constraint | `CON-136`, `CON-138` | authored prerequisite chain; temporary state gates assembly and use |
| Information | `INF-001`, `INF-037` | visible inventory / target; inspection-only Band-Aid hotspot |
| Objective | `OBJ-045` | retrieve the iron key with the constructed reach tool |
| Time | `TIM-003` | live decay after inflation |

Compact signature:

`ACT-087,ACT-090,ACT-092; SYS-114; CON-136,CON-138; INF-001,INF-037; OBJ-045; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `86` (`GAME-0001`–`GAME-0086`).
- Exact genome matches: none.
- Tied near matches: `GAME-0086` — Machinarium (`4 / 19 = 0.210526`).
- Supported combination subsets: `COMB-0087`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0086`.

## Combination candidate

- Candidate ID: `COMB-0087`.
- Gene set: `ACT-090`, `ACT-092`, `SYS-114`, `CON-138`, `INF-037`, `OBJ-045`,
  `TIM-003`.
- Supporting game: `GAME-0087`.
- Proper-subset rationale: `ACT-087`, `CON-136` and `INF-001` enable or expose
  execution but do not define the inspected, prepared and expiring composite.
- Novelty claim: not assessed.

## Outcome

- Reused genes: `ACT-087`, `ACT-090`, `CON-136`, `INF-001`, `TIM-003`.
- Added genes: `ACT-092`, `SYS-114`, `CON-138`, `INF-037`, `OBJ-045`.
- Added combination: `COMB-0087`.
- Evidence gate: passed with Funcom's manual, current product record, three
  independently agreeing walkthroughs and one executable control.
- Nearest prior genome: Machinarium; see `Corpus comparison` for the current
  result.
- Next falsification target: an authored inventory scene with close-up item
  preparation and multi-stage combination but no real-time state decay.

## Taxonomy impact

- Held-item preparation is separated from articulated reshaping and from
  combining two identities: the duck retains its identity while its patch and
  inflation states change.
- A temporary constituent can remain causally active inside a composite tool;
  decay is therefore recorded as system behaviour plus a compatibility/use
  constraint rather than as cosmetic animation or an external timer.
- Close inspection becomes information only when it exposes a new manipulable
  subpart and changes the legal action set.

## Negative results

- Walking between the apartment, café and subway is excluded access rather than
  a gene in this bounded packet.
- The electrified rail is target context, not a general damage or health system:
  the scoped solution never asks the player to enter it.
- The recipe is authored and deterministic, not an economy, free-form crafting
  system or discovered statistical combination.
- Ordinary inventory opening and cursor flashing are interface support, not
  separate genes.
- The verifier proves the recorded causal boundary and expiry retry, not the
  exact number of real-time seconds in every released build.
