---
game_id: GAME-0104
slug: tunic
game_title: TUNIC
analysis_status: reviewed
reviewed: 2026-08-15
combination_ids:
  - COMB-0104
gene_ids:
  action:
    - ACT-008
    - ACT-106
  system:
    - SYS-037
    - SYS-139
  constraint:
    - CON-158
  information:
    - INF-001
    - INF-054
  objective:
    - OBJ-026
  time:
    - TIM-015
---

# Game: TUNIC

## Analysis scope

- Version / ruleset: original released game, bounded to the Overworld fountain
  manual pickup and the nearby patterned Holy Cross door.
- Included: possessing the Hero's Laurels; reaching the fountain; collecting
  instruction pages 42–43; inspecting page 43; interpreting the Holy Cross as
  D-pad or arrow-key input; addressing the nearby patterned door; entering
  `Down, Right, Up, Left, Up, Right`; inactivity reset; permanent opening;
  traversal through the doorway; and collecting pages 44–45 behind it.
- Excluded: combat, bosses, other manual pages and patterned locks, the Golden
  Path, language decoding, endings, sequence breaking and accessibility modes
  except where Sequence Assist corroborates the input-time boundary.
- Direct-play status: not conducted because no licensed executable was found
  on this Mac. Creator-controlled descriptions establish the progressively
  collected manual and its communication purpose; page records and independent
  guides corroborate the bounded locations, code and timing behaviour. The
  executable control distinguishes knowledge from an inventory prerequisite.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TUN-001` | Instruction pages are collected gradually into a persistent, inspectable in-world manual | Confirmed | Corroborated | High | P1, P2, P3 |
| `TUN-002` | Pages 42–43 are collected at the Overworld fountain with the Hero's Laurels, and pages 44–45 lie behind the nearby patterned door | Confirmed | Corroborated | High | S1, S2 |
| `TUN-003` | Page 43 identifies the Holy Cross as D-pad or arrow-key input and teaches patterned-door interpretation | Confirmed | Corroborated | High | S1, S3 |
| `TUN-004` | The scoped door opens for `Down, Right, Up, Left, Up, Right`, not its mirrored sequence | Confirmed | Corroborated | High | S2, S4, V1 |
| `TUN-005` | The code is a knowledge gate: it can work without page 43 in inventory | Confirmed | Corroborated | High | S3, S5, V1 |
| `TUN-006` | Excess inactivity ends an unfinished code entry, while retry remains possible and Sequence Assist removes that timing pressure | Confirmed | Corroborated | High | S6, V1 |

## Basic data

- Release / origin: designed by Andrew Shouldice; published by Finji in 2022.
- Platform or physical form: single-player action-adventure videogame with a
  collectible instruction booklet embedded in play.
- Puzzle family: knowledge-only directional code decoded from a diegetic manual.
- Primary sources:
  - **[P1]** [Andrew Shouldice on the instruction manual](https://blog.playstation.com/?p=370009),
    for gradual page collection, dense diagrams, zoom and communication as
    mystery.
  - **[P2]** [Official TUNIC site](https://tunicgame.com/), for the creator-
    controlled product identity and official destination.
  - **[P3]** [Xbox Wire launch article](https://news.xbox.com/en-us/2022/03/16/tunic-launches-today-with-xbox-game-pass/amp/),
    for scattered manual pages, their persistent booklet and clue-bearing maps.
- Secondary sources:
  - **[S1]** [Instruction Booklet page 43 record](https://tunic.wiki/books/instruction-booklet/page/page-43-hidden-secrets),
    for the Holy Cross meaning and page content.
  - **[S2]** [Manual-page location guide](https://www.neoseeker.com/tunic/Collectibles_and_useful_item_locations/Manual_Pages),
    for the fountain pickup, Laurels prerequisite, adjacent door, exact code
    and pages 44–45.
  - **[S3]** [Instruction Booklet location index](https://tunic.fandom.com/wiki/Instruction_Booklet),
    for the paired page locations and knowledge-only reading context.
  - **[S4]** [Community confirmation of the six-direction code](https://steamcommunity.com/app/553420/discussions/0/5675129542133028613/),
    for the same exact sequence and its manual derivation.
  - **[S5]** [Community confirmation that no item unlock is required](https://www.reddit.com/r/TunicGame/comments/tvqa4a),
    used only to corroborate the knowledge-gate boundary.
  - **[S6]** [Community timing and Sequence Assist report](https://steamcommunity.com/app/553420/discussions/0/3820781817413077938/),
    for inactivity reset without asserting an exact undocumented duration.
  - **[V1]** [`verify_tunic_holy_cross.py`](../../../scripts/verify_tunic_holy_cross.py),
    an independent executable control for the bounded packet.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. The player moves from the fountain
  to the nearby door and crosses its threshold after it opens.
- `ACT-106` — enter ordered directional code without locomotion. At the door,
  six cardinal commands address the seal instead of moving the fox.

### System Behaviour Genes

- `SYS-037` — contact-triggered collectible acquisition. Touching the fountain
  page object adds pages 42–43 to the booklet; the post-door object adds 44–45.
- `SYS-139` — recognise buffered directional code and open addressed seal. The
  exact complete code opens this door permanently; partial or mirrored input
  does not.
- Resolution order: contact the page pair; inspect the newly persistent manual
  spread; stand at the patterned seal; buffer directional symbols; clear an
  unfinished buffer after excess inactivity; compare the complete sequence;
  open on the exact match; traverse and collect the next pair.

### Constraint Genes

- `CON-158` — exact ordered cardinal trace for one patterned seal. This door's
  accepted sequence is `Down, Right, Up, Left, Up, Right`; page possession is
  not part of the acceptance predicate.

### Information Genes

- `INF-001` — fully visible current state. The page pickup, persistent manual,
  closed or open door and post-door page pair can all be inspected directly.
- `INF-054` — collectible diegetic manual progressively expands persistent
  reference. Page 43 communicates a control and clue that the simulation
  already accepts; it does not grant a new mechanical verb.

### Objective Genes

- `OBJ-026` — reach designated traversable world location. The bounded packet
  ends beyond the previously sealed doorway at pages 44–45.

### Time Genes

- `TIM-015` — short inactivity terminates buffered code entry without world
  penalty. A slow unfinished attempt resets, while a fresh complete entry can
  still open the unchanged door.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Hero's Laurels held at fountain | Contact page object | Pages 42–43 become persistent manual pages | ordinary pickup plus persistent reference | `TUN-001`, `TUN-002` |
| Page 43 available | Inspect its diagram | Holy Cross is identified as directional input; nearby patterns become readable | authored knowledge, not capability grant | `TUN-003` |
| Closed scoped door, no pages owned | Enter exact six directions without long pause | Door opens permanently | knowledge-only gate | `TUN-004`, `TUN-005` |
| Same closed door | Enter `Down, Left, Up, Right, Up, Left` | Door remains closed | exact ordered code, not mirrored shape | `TUN-004` |
| Three-symbol prefix entered | Wait beyond the accepted gap, then enter suffix | Old prefix is unavailable; door remains closed | inactivity resets only the buffer | `TUN-006` |
| Door open | Traverse and contact page object | Pages 44–45 join the manual | access consequence and bounded objective | `TUN-002` |

## Strategic and experiential structure

- Local decision: infer which directional turns the visible line encodes, then
  reproduce them promptly while addressing the correct seal.
- Medium-term planning: revisit suspicious world patterns as later manual pages
  reveal how already-familiar controls can carry hidden meanings.
- Long-term structure: the manual converts world decoration into a distributed
  knowledge network; acquisition changes player understanding more often than
  avatar capability.
- Common heuristics: zoom the page; distinguish visual path from character
  movement; start from the marked endpoint; enter continuously; retry from the
  beginning after a pause.
- Failure attribution: a closed door does not identify the wrong symbol, but a
  known exact sequence separates interpretation error from missing inventory.
- Player-trust factors: an exact code must work before and after clue collection,
  and the same directional grammar must remain consistent across patterns.

## Replay and variation

- Page and door locations and the six-direction code are authored and fixed.
- The player may discover the code externally or infer it before collecting
  page 43; this changes discovery order, not the door predicate.
- Sequence Assist changes the timing burden, not the exact symbol order.

## Adjacent systems and history

- The Witness also turns environmental lines into a reusable puzzle language,
  but its panels receive continuous traced paths rather than buffered cardinal
  commands at a world seal.
- Chants of Sennaar validates an editable glyph glossary and gates progress on
  that validation. TUNIC's manual is fixed authored reference and the door does
  not inspect whether the relevant page was collected.
- Fez uses directional codes and diegetic clues, but this scoped packet adds a
  progressively collected manual and an inactivity-sensitive input buffer.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-106` | address range; input device |
| System Behaviour | `SYS-037`, `SYS-139` | buffer recovery; door persistence |
| Constraint | `CON-158` | six-symbol authored sequence |
| Information | `INF-001`, `INF-054` | page order; zoom; encoded language |
| Objective | `OBJ-026` | post-door page location |
| Time | `TIM-015` | inactivity threshold; assist override |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `103` (`GAME-0001`–`GAME-0103`).
- Exact genome matches: none.
- Tied near matches: `GAME-0098` — Hyperbolica (`3 / 13 = 0.230769`).
- Supported combination subsets: `COMB-0104`.
- Scan date: 2026-08-15.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0098`.

### Preserved research notes

- New genes: `ACT-106`, `SYS-139`, `CON-158`, `INF-054`, `TIM-015`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: the corpus already represented navigation, ordinary
  contact pickup, visible state and reaching a location. It lacked a stationary
  cardinal-code action, target-specific sequence recognition, exact seal code,
  progressively collected authored manual that communicates pre-existing
  capability, and nonterminal inactivity reset of a code buffer.

## Taxonomy impact

- Registry changes: five Active IDs and four transfers to a new game.
- Taxonomy-change record: none; no earlier boundary is merged or retired.
- Candidate terms affected: knowledge gate and rejected-neighbour boundaries
  recorded in `CANDIDATE_TERMS.md`.

## Negative results

- `ACT-076` rejected: the door does not present a transient authored cue then
  enter a separate reproduction phase; the player initiates live code entry.
- `ACT-073` rejected: the six inputs are not an editable proposal submitted as
  a complete object; they resolve through a live sequence buffer.
- `CON-155` rejected: collecting or validating page 43 is not checked by the
  door and the correct code works without it.
- `INF-052` rejected: the manual is authored persistent reference, not a
  player-editable provisional glossary with validation slots.
- `INF-050` rejected: one player can inspect both world state and manual; there
  is no human role partition.
- `TIM-002` rejected: inactivity can clear an unfinished code buffer even
  though exploration and manual reading otherwise have no deadline.
- `SYS-063` rejected: the door consumes no carried key or inventory item.
