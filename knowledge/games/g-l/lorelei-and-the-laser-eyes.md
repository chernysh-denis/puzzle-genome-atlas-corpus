---
game_id: GAME-0563
slug: lorelei-and-the-laser-eyes
game_title: Lorelei and the Laser Eyes
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-072
    - ACT-073
    - ACT-083
    - ACT-085
    - ACT-087
    - ACT-089
    - ACT-107
    - ACT-341
  system:
    - SYS-112
    - SYS-680
    - SYS-1637
    - SYS-1638
    - SYS-1639
  constraint:
    - CON-136
    - CON-621
    - CON-826
    - CON-827
  information:
    - INF-003
    - INF-179
    - INF-393
    - INF-496
  objective:
    - OBJ-031
  time:
    - TIM-002
---

# Game: Lorelei and the Laser Eyes

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Hotel Letztes Jahr, the architects, years, room numbers and Byte-Seyes are
carrier parameters, not independent name-based genes.

## Analysis scope

- Version / ruleset: original released English US Nintendo Switch eShop
  edition, 16 May 2024 rules profile, fresh New Game with no transferred
  progress. Exact installed patch, package, binary hash and native execution
  are unverified. The later PlayStation release and 2026 Switch 2 upgrade
  are separate distributions, not the selected execution. The changed 2022
  development prototype is not a source for released mechanics.
- Structured analysis target: original Switch entry in
  `knowledge/platforms/games.json`, grounded in developer/publisher material,
  the released in-game booklet and independently authored hotel routes.
- Primary decision loop: explore a reachable room, inspect its letters,
  diagrams and apparatus; reopen registered material, interpret the clue and
  optionally calculate a candidate; set a local lock and submit the answer;
  use accepted access to reach another source or map tube. Revisit an
  unfinished branch when its prerequisites become known. Reading a document,
  reasoning about it and submitting a lock answer are different transitions.
- Entry and exit: first ordinary control beside the car in the forest of a
  fresh game; complete hotel admission, access to Room 2014 and all five
  hotel floor plans. End after a manual computer save and same-slot reload
  retains acquired plans and room access. Forest Map and the accessible
  Maze Lithograph are inspected along this route; entering the red maze is
  excluded. This complete cartography packet is not a claim of the game's
  final Truth completion, an achievement threshold or a compulsory global
  order for every puzzle.
- Admission route: use the initially carried Car Key, inspect the glovebox
  booklet, letter and photograph, read the Forest Map and dog's notice.
  The car letter's next-year clue gives the gatehouse padlock's 1963;
  the subsequent 116-year offset gives the electrical cabinet's 1847.
  Collect the Byte-Seyes tool. Choose one value from each of three separate
  number banks to total 2014, then confirm to open the garden gate. The
  candidate values can vary; no copied guide combination is guaranteed.
  Read the front door's red-dot ordering and submit its four-digit answer.
- Reception route: tune the gatehouse television and inspect its resulting
  clue; visit the basement architect studio and both second and third floors,
  then return to the lobby/front door and speak with Renzo when available.
  Sources disagree about the minimal visit/TV trigger. This reproducible
  combined route covers their stated visits but does not certify that every
  one is necessary, nor invent a precise native conjunction of flags.
  Inspect the reception letter, apply its stated previous/next-year offset,
  and rotate the cabinet's fixed blocks to draw the resulting four digits.
  Take the Room 2014 Key and unlock the third-floor room. Accept its initial
  authored encounter if triggered, inspect the east-branch Maze Lithograph
  without entering its maze, and use the ladder to the loft/Room 3014.
- Complete cartography route: inspect all five architect sketches on the
  basement drawing board. Match each tube's stamped architect identity to
  the appropriate current sketch; neither a guide's name assignment nor
  most incidental prices are universal. Solve and open the tubes in the
  basement studio, ground-floor foyer bookshelf, second-floor Front West
  Hallway bookshelf, third-floor East Hallway drawer and loft shelf. The
  first three need not wait for Room 2014; the loft does require that route.
- Five reasoning tasks: infer thirteen modules from the symmetric structure
  and multiply by the current unit price; orient the Modern Design page to
  read its hidden numeral; choose a least-cost valid module composition for
  the target silhouette without rotating/flipping the pictured pieces;
  reinterpret the upside-down room dimensions and multiply length by width;
  match mansion halves by their architectural details and add their current
  prices. These are mental/document calculations followed by tube entry,
  not an invented in-game polyomino placement board. The hidden numeral is
  reported fixed as 714 in the inspected released accounts; this does not
  certify every later binary. Example prices are not general solutions.
- Included: direct movement; contextual inspection and dialogue; key/tool
  collection and compatible fixture use; keypad proposals, local tile and
  knob manipulation, separate confirmation; persistent prerequisites and
  accepted mechanism consequences; per-playthrough puzzle parameters;
  photographic archive, derived Mental Notes and auxiliary arithmetic;
  acquired floor plans/current position; revisable wrong entries and
  designated computer saving. A displayed playtime is not a solve deadline.
- Excluded: red-maze pursuit and its Game Over rules; later memory questions,
  coloured doors, script reconstruction, year boxes, full Truth computer
  and ending; optional arcade games, Bolt puzzles and dollar-store economy;
  magician route, shortcut puzzles and unrelated locked rooms. Visible money
  is not deliberately collected as a side control and does not admit a
  spending system. A later feature's menu label is not evidence of its use.
- Potential scoped modules: red-maze navigation/failure, memory questions,
  deeper media reconstruction, optional minigames and full finale.
- Direct-play status: not conducted. Inspected all eighteen static ten-second
  storyboard sheets of justonegamr's Switch-labelled 71:06 recording at
  160×90 source cells, including the opening, gatehouse, hotel and reception
  approach. Three larger 320×180-cell sheets support reading the released
  booklet pages 2–6. Inspected eighteen sheets of KrakenGaming's first
  seventy-five minutes, including cabinet, Room 2014 and later side puzzles;
  its execution platform is not certified. Inspected all three five-second
  sheets of PlatMatt's 5:42 all-map-tubes guide, showing five floor-plan
  reveals on an already advanced profile. No video/audio playback, console,
  executable, input trace, full save-field audit or native failure experiment
  was used. Sparse stills corroborate visible states, not exact inputs,
  minimal trigger flags, RNG seeds or timing.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| LLE-001 | Original Switch release is 16 May 2024; later PlayStation and Switch 2 editions and early prototypes are distinct. | Observation | Corroborated | High | P1, P2, P3, V1 |
| LLE-002 | Directional movement and one contextual action access inventory, photographic records, Mental Notes and manual computer saving; no autosave is promised. | Observation | Corroborated | High | P1, B1, S4, V1 |
| LLE-003 | Admission requires clue-derived codes, the electrical cabinet/tool and three independent selected numbers totaling 2014 before confirmation. Selected numeric parameters vary across fresh games. | Observation | Corroborated | High | P1, S1, S4, V1, V2 |
| LLE-004 | Reception gives access to a clue-derived rotated-block cabinet and Room 2014 Key with accepted digit shapes. | Observation | Corroborated | Medium | S2, S5, S6, V2 |
| LLE-005 | Five named sketches and stamped three-digit tubes supply five floor plans; most prices and assignments can vary, and modular composition includes least cost. | Observation | Corroborated | High | P1, S3, S7, S8, V3 |
| LLE-006 | Acquired plans expose authored layout/current position; progress is retained through an explicit computer write/load, not assumed autosave or visited-terrain painting. | Observation | Corroborated | Medium | B1, S3, S4, V1, V3 |
| LLE-007 | This admission/cartography packet is self-paced and wrong lock inputs are revisable; later maze pursuit and its failure are separate. | Observation | Corroborated | Medium | P1, B1, S1, S4, V1, V2 |
| LLE-008 | A secondary guide says four map tubes but lists fewer locations than independent five-tube routes and the inspected map guide. | Observation | Conflicting | High | S3, S4, S7, V3 |
| LLE-009 | Accounts disagree about the minimal TV/basement/upper-floor conditions for Renzo’s arrival; the combined coverage route does not prove necessity. | Observation | Conflicting | Medium | S2, S5, S6, V2 |

## Basic data

- Release / origin: Simogo, published by Annapurna Interactive; original
  Switch/Windows release 16 May 2024. Selected platform is original Switch.
- Platform or physical form: one-player console mystery with contextual
  direction/button input. The current Nintendo listing also offers Switch 2;
  that storefront option does not retrospectively identify the target patch.
- Puzzle family: deduction from constraints; knowledge/information
  investigation; inventory and persistent mechanism dependency. No separate
  family or platform is introduced.
- Primary sources, accessed 2026-11-20:
  - **P1** [Simogo's released game and development account](https://simogo.com/work/loreleiandthelasereyes/):
    release, one-button/directional intent, authored world, changing puzzle
    parameters and distinct earlier prototypes. Development history is not
    substituted for released rules.
  - **P2** [Annapurna product page](https://annapurnainteractive.com/games/lorelei-and-the-laser-eyes):
    release identity and nonlinear authored mystery.
  - **P3** [Nintendo US original Switch product](https://www.nintendo.com/us/store/products/lorelei-and-the-laser-eyes-switch/):
    English, original release date and one-player listing; no owned-package
    or version verification is implied.
  - **B1** released in-game instruction booklet, pages 2–6, visibly inspected
    in V1's larger static sheets: controls, introspection, records and manual
    computer saving. This is not Simogo's later promotional printable notebook.
- Independently authored corroboration, accessed 2026-11-20:
  - **S1** [Rahul Shirke, admission route](https://intoindiegames.com/walkthroughs/lorelei-and-the-laser-eyes-walkthrough-how-to-enter-hotel-letztes-jahr/).
  - **S2** [Shirke, Room 2014 route](https://intoindiegames.com/walkthroughs/lorelei-and-the-laser-eyes-walkthrough-how-to-get-into-room-2014/).
  - **S3** [Shirke, complete map route](https://intoindiegames.com/walkthroughs/lorelei-and-the-laser-eyes-walkthrough-how-to-find-all-the-maps/).
    S1–S3 share one author and are not three independent witnesses.
  - **S4** [Kim Snaith, GameSpew guide](https://www.gamespew.com/2024/05/lorelei-and-the-laser-eyes-guide/):
    archive, saving, changing parameters and least-cost composition; its
    four-tube wording/omitted third-floor location is not accepted as the count.
  - **S5** [Jamie Moorcroft-Sharp, reception route](https://www.destructoid.com/how-to-unlock-room-2014-lorelei-and-the-laser-eyes/):
    TV/basement trigger account, cabinet and key.
  - **S6** [shildosh, spoiler-graded hint guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3249636035):
    basement/third-floor trigger account and wrong-side digit-1 caution.
    Its PC-specific controls and overly broad map-access hint are not used
    as Switch button or universal access evidence.
  - **S7** [Anthony Yates, five document-tube puzzles](https://primagames.com/gaming/how-to-solve-every-document-tube-puzzle-in-lorelei-and-the-laser-eyes):
    independently explains composition, orientation and current costs.
  - **S8** [Lewis Rees, all document tubes](https://twinfinite.net/guides/lorelei-and-the-laser-eyes-how-to-unlock-all-document-tubes/):
    corroborates five tasks; its example architect headings are not universal
    per-playthrough assignments.
- Static recorded observations:
  - **V1** [justonegamr, Switch-labelled gameplay](https://www.youtube.com/watch?v=5VB6sQhwv8s),
    71:06, all eighteen sparse sheets plus larger booklet sheets inspected.
  - **V2** [KrakenGaming, complete recording](https://www.youtube.com/watch?v=keXdGoGOlEQ),
    8:28:41 total; only its first eighteen ten-second sheets are inspected.
  - **V3** [PlatMatt, all map tubes](https://www.youtube.com/watch?v=L5wSNEOTKtE),
    5:42, all three five-second sheets inspected. This is not a fresh-start
    minimal-route recording or certified original Switch execution.
- Restricted leads: GameFAQs and Neoseeker pages were not fully accessible;
  indexed excerpts are not treated as fully read rules.
- Claim IDs: LLE-001–LLE-009.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: move through the present forest, hotel or loft.
- Existing `ACT-072`: select the cabinet's addressed confirmation trigger.
- Existing `ACT-073`: fill and submit the ordered keypad/dial code proposal.
- Existing `ACT-083`: rotate an embedded fixed block at its current position.
- Existing `ACT-085`: change the addressed rotary control's selected setting,
  including number banks and the inspected television tuning.
- Existing `ACT-087`: apply a compatible carried key to its addressed lock.
- Existing `ACT-089`: inspect/take the handheld tool and accessible keys.
- Existing `ACT-107`: complete the authored Renzo exchange and retain its
  operational room/reception information; not a free-form dialogue tree.
- Existing `ACT-341`: inspect the current letter/diagram, open an eligible
  door or commit computer interaction. Claims: LLE-002–LLE-005.

### System Behaviour Genes

- Existing `SYS-112`: an accepted compatible operation persistently opens
  its gate, cabinet, key access or map tube; a code is not just a score.
- Existing `SYS-680`: eligible inspections/conversations register authored
  Mental Notes and investigation progress. This is different from retaining
  a raw document; it does not assert that every paper is mandatory before
  a knowledgeable player may submit a code.
- New `SYS-1637`: a fresh playthrough instantiates selected parameters and
  sketch/name assignments within authored puzzle templates. It does not
  generate a new hotel or reroll after each wrong answer.
- New `SYS-1638`: inspecting an eligible complete record copies it into
  categorized Photographic Memory without taking its physical source.
- New `SYS-1639`: the owned calculator evaluates selected arithmetic and
  displays a result without itself entering a world-lock answer.
- Claims: LLE-002–LLE-005. Exact seed, distribution, calculator precision and
  native save serialization are unverified.

### Constraint Genes

- Existing `CON-136`: key acquisition and accepted earlier access persist
  as prerequisites, including Room 2014 access before the loft map.
- Existing `CON-621`: a manual slot write requires an eligible computer;
  leaving the room is not an automatic save.
- New `CON-826`: choose one value per independent number bank to reach the
  exact displayed total. No all-different or overlapping line condition is
  inferred from arithmetic resemblance.
- New `CON-827`: local fixed-block orientations must draw accepted ordered
  digit glyphs; a numeral with the wrong segment placement can fail.
- Parameters: current values, target, code length and clue-derived adjacent
  year. No extra gene per architect, arithmetic operator or price.
- Claims: LLE-002–LLE-006.

### Information Genes

- Existing `INF-003`: the current run conceals fixed present answers until
  observation/reasoning reveals them, rather than sampling every proposal.
- Existing `INF-179`: the present view exposes local fixtures, exits and
  available space, not unseen rooms behind locked doors.
- Existing `INF-393`: retained Mental Notes and inspected evidence expose
  growing authored clues, people and leads without the entire solution.
- Existing `INF-496`: acquired floor plans disclose authored topology and
  current position without requiring every corridor to be visited first.
- Claims: LLE-002, LLE-004–LLE-006.

### Objective Genes

- Existing `OBJ-031`: finish the bounded authored task conjunction: hotel
  access, Room 2014 access and all five floor plans. One correct padlock or
  collecting a fixed identity list alone is insufficient; the save/load is
  an explicit persistence control, not an invented global victory screen.
- Full-game completion is excluded. Claims: LLE-003–LLE-006.

### Time Genes

- Existing `TIM-002`: inspect, reason and revise at the player's pace in
  this packet. Displayed elapsed time has no admitted solve deadline;
  later live red-maze pursuit is excluded. Claim: LLE-007.

## Reproducible transitions

| Before | Action | Resolution | Distinction | Claim |
| --- | --- | --- | --- | --- |
| Fresh car and carried key | Use key and inspect glovebox records | Booklet/letter enter readable knowledge and eligible archive | Reading does not require taking every paper | LLE-002 |
| Car letter gives the next year | Set gatehouse padlock to the inferred year | Correct proposal opens the gatehouse | Fixed authored clue, not a random guess each attempt | LLE-003 |
| Cabinet clue states an offset | Calculate and set the resulting code | Cabinet exposes the tool and next mechanism | Calculator result alone does not open a world lock | LLE-003 |
| Three independent banks show candidates | Choose one per bank and confirm | Exact total opens the garden gate | No distinctness or shared-grid equation is added | LLE-003 |
| Wrong total or code | Revise controls and resubmit | Access remains closed until accepted | No maze life loss is imported | LLE-007 |
| Renzo not yet at reception | Follow declared TV/basement/upper-floor route and return | Speak when his authored encounter is available | Minimal native trigger remains uncertain | LLE-004 |
| Current reception letter inspected | Apply its stated adjacent-year offset | A current-run four-digit target is derived | A guide's incidental example is not universal | LLE-004 |
| Correct numeral but wrong segment convention | Rotate the addressed fixed block | Only an accepted glyph arrangement releases the key | Semantic numeric equivalence alone is insufficient | LLE-004 |
| Room key acquired | Unlock Room 2014, inspect east branch and climb ladder | Loft tube becomes reachable | Not every map tube requires this key | LLE-004, LLE-005 |
| Tube stamped with a current name | Find corresponding sketch | Its current task/costs identify this tube's proposal | Container/name mapping can change next playthrough | LLE-005 |
| Symmetric sketch conceals rear modules | Infer full count and multiply current price | Result supplies one three-digit proposal | Visible front modules alone undercount | LLE-005 |
| Several silhouettes appear to fit | Choose least-cost valid pictured composition | Current costs determine accepted proposal | No actual pieces are dragged into a board | LLE-005 |
| Upside-down dimensions mislead | Reinterpret orientation before area calculation | Correct operands give the tube code | Blindly multiplying the first apparent digits can fail | LLE-005 |
| Five tubes accepted | Open the acquired plans | All five layouts/current position are inspectable | Not visited-terrain painting or the full finale | LLE-005, LLE-006 |
| All packet access/plans acquired | Write at the designated computer, load same slot | Retained access and plans can be checked | No native byte-complete save claim | LLE-006 |

## Strategic and experiential structure

- Local decision: distinguish a source's orientation, its relevant quantities
  and a proposed answer before committing the physical lock.
- Medium horizon: retain clue-to-container correspondences, revisit available
  branches and use plans to reduce blind hotel backtracking.
- Constraint tension: arithmetic is easy once the correct representation and
  premises are selected; a calculator cannot choose those premises for you.
- Failure attribution: incorrect digits, a wrong name match, non-minimal
  composition or misplaced digit segments can each explain closed access.
- Trust: archive raw documents separately from interpreted Mental Notes;
  expose route uncertainty instead of asserting an untested minimal flag.
- Claims: LLE-002–LLE-008.

## Replay and variation

- Authored topology and reasoning templates remain; selected numeric values
  and stamped correspondences vary across new playthroughs. No exact seed,
  full distribution or per-attempt resampling is certified.
- Several map tasks can be solved in a different partial order. The fixed
  route is a reproducible coverage path, not the only legal order.
- Claims: LLE-003–LLE-007.

## Adjacent systems and history

- Later ports and early prototypes are not silently pooled into this scope.
- The later red maze adds pursuit/failure; optional games add different
  rules. Neither follows merely from seeing a menu or lithograph here.
- Claims: LLE-001, LLE-007.

## Normalised genome

| Type | Genes |
| --- | --- |
| Action | `ACT-008`, `ACT-072`, `ACT-073`, `ACT-083`, `ACT-085`, `ACT-087`, `ACT-089`, `ACT-107`, `ACT-341` |
| System | `SYS-112`, `SYS-680`, `SYS-1637`, `SYS-1638`, `SYS-1639` |
| Constraint | `CON-136`, `CON-621`, `CON-826`, `CON-827` |
| Information | `INF-003`, `INF-179`, `INF-393`, `INF-496` |
| Objective | `OBJ-031` |
| Time | `TIM-002` |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `562` (`GAME-0001`–`GAME-0562`).
- Exact genome matches: none.
- Tied near matches: `GAME-0085` — The Room (`7 / 28 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0085` — The Room | `ACT-072`, `ACT-085`, `ACT-087`, `SYS-112`, `CON-136`, `INF-003`, `TIM-002` | Both turn clue-led, self-paced fixture operations into retained access. The Room reshapes a carried key and reveals lens-only traces before the safe objective; Lorelei varies clue parameters, archives documents, calculates and acquires five maps across rooms. | Tied near: 7 / 28 = 0.250000. |

### Preserved research notes

- New genes: five; nineteen unchanged definitions reused.
- Classification result: New gene.

## Taxonomy impact

- Registry additions: `SYS-1637`–`SYS-1639`, `CON-826`, `CON-827`.
- [Taxonomy Change 309](../../../research/taxonomy-changes/TAXONOMY_CHANGE_309.md)
  records accepted boundaries and rejected alternatives.

## Negative results

- None as a separate prior-claim rejection. Conflicting route/count accounts
  remain explicit source limitations rather than fabricated resolved facts.

## Delta summary

## New facts

- [Observation | Corroborated | High] LLE-002–LLE-005: retained documents,
  current-run arithmetic and local mechanism submissions are separate.
- [Observation | Conflicting | Medium] LLE-009: the minimal Renzo trigger
  is not resolved by the inspected sources or sparse recordings.

## New genes

- [Observation | Corroborated | Medium] `SYS-1637`–`SYS-1639`, `CON-826`, `CON-827`.

## New combinations

- [Observation | Direct | High] No new combination proposal; accepted proper
  subsets are owned by Corpus comparison.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_309`; no existing
  definition, lifecycle or signature changes.

## New questions

- Which exact native flags are necessary and sufficient for Renzo's arrival?
- What seed/distribution and persistence implement per-playthrough parameters?
- What precision/overflow policy does the auxiliary calculator use?
- Which inspected fields are serialized by an actual original Switch save?

## Next recommended game

- [Hypothesis | Limited | High] Original Neo Geo MVS Windjammers, `GAME-0564`,
  under approved Selection 045.
- Optimisation criterion: switch from modern self-paced investigation to
  retro arcade spatial contest while retaining platform/era variety.
- Expected information gain: isolate original disc trajectory, interception
  and scoring without inheriting the sequel's additional rules.
- Backlog impact: four subjects remain; stop after GAME-0567. No push,
  publication, Actions, merge or deploy is authorised.

## Why this game

- [Hypothesis | Limited | High] A complete admission/cartography packet tests
  the difference between evidence access, representation, calculation and
  accepted world change without claiming a whole-game union.
