---
game_id: GAME-0538
slug: the-rise-of-the-golden-idol
game_title: The Rise of the Golden Idol
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids:
  - COMB-0046
gene_ids:
  action:
    - ACT-030
    - ACT-060
    - ACT-736
  system:
    - SYS-086
    - SYS-1559
  constraint:
    - CON-064
    - CON-093
  information:
    - INF-001
    - INF-024
    - INF-522
  objective:
    - OBJ-017
  time:
    - TIM-002
---

# Game: The Rise of the Golden Idol

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Names, room numbering, vocabulary size and the sentence are case parameters.

## Analysis scope

- Version / ruleset: the full English Steam base game for Windows, app
  2716400, as documented around the 12 November 2024 retail release.
  Exact executable build, hotfix parity and installed state are unverified.
- Entry: start at the unsolved Prologue: Constriction tableau after the
  brief opening phrase exercise. Use the ordinary pointer interface,
  first-time case state and visible evidence markers.
- Primary decision loop: focus on the corridor, badge, rounds record
  and clothing; collect their marked vocabulary by inspection. Use room
  adjacency and the record to associate an unseen full name with a
  portrait. Position the Words, Names and Events panels and assign
  reusable, role-compatible terms to the identity and event blanks.
- Positive exit: both Names and Events are accepted, Continue becomes
  available, and the player stops before controlling Academic Impact.
  Incorrect text remains open to revision without expiring an attempt.
- Included: frozen evidence scene, word and spot discovery, reusable
  scoped terms, typed identity and event slots, independent validation
  and case progression. Excluded: opening phrase exercise, optional
  hints, later scenes and chapter conclusions, demo, DLC, other ports,
  exact save persistence and an exhaustive synonym inventory.
- Direct-play status: no executable, install or save was opened. The
  publisher's Steam record establishes the product boundary; contemporary
  Windows play accounts and static walkthrough images attest the
  selected rules. No audiovisual playback was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| RGI-001 | The standalone full Windows release is Steam app 2716400, published by Playstack and developed by Color Gray Games. Constriction follows a short preliminary phrase exercise. | Confirmed | Corroborated | High | P1, S1, S3 |
| RGI-002 | The depicted scene is frozen while the player selects evidence. Inspecting an eligible detail automatically collects terms. The toolbar separately tracks 25 available words and nine evidence spots in Constriction. | Observation | Corroborated | High | P1, S1, S2, S3, S4 |
| RGI-003 | The badge supplies one identity. The number across from 201 is inferred as 202 from the 203/204 pair and linked to the rounds record to identify the other portrait. The clothing helps confirm the location. | Observation | Corroborated | High | S1, S2, S4 |
| RGI-004 | Names has two portraits with first- and last-name blanks. Events has a fixed sentence scaffold for the persons, role, object and institution. The same collected terms remain available in Words and can appear in both panels. Colour distinguishes eligible vocabulary roles. | Observation | Corroborated | High | S1, S3, S4 |
| RGI-005 | Completing a panel invokes a section-level correctness check. The Windows reviewer reports coarse feedback at one or two mistakes. A photographed state has Events accepted while Names remains open; another records both accepted with Continue. | Observation | Corroborated | High | S2, S3, S4 |
| RGI-006 | Words and the draft panels can coexist and be repositioned over the inspectable scene. The Windows play report distinguishes positioning from resizing, which it did not support in that review. | Observation | Corroborated | High | S3, S4 |
| RGI-007 | A complete discovery toolbar can coexist with an unfinished answer. Case clearance is the validated pair of panels, with no case clock or life expenditure in the observed loop. | Observation | Corroborated | High | P1, S1, S2, S3, S4 |

## Basic data

- Color Gray Games and Playstack, 12 November 2024, English Windows
  base game on Steam. Single-player point-and-click deduction.
- Families: hidden-state inference, and knowledge and evidence progression.
- Sources accessed 2026-11-17:
  - **P1** — [publisher's official Steam release](https://store.steampowered.com/app/2716400/The_Rise_of_the_Golden_Idol/),
    for release date, English interface, Windows support, base product,
    separate demo and DLC, fixed scenes and collected terms.
  - **S1** — [GameSpew launch walkthrough](https://www.gamespew.com/2024/11/the-rise-of-the-golden-idol-walkthrough/),
    for controls, the opening exercise, starting counts and case evidence.
  - **S2** — [Into Indie Games launch walkthrough](https://intoindiegames.com/walkthroughs/the-rise-of-the-golden-idol-walkthrough-prologue-chapter-1/),
    for the route through corridor and rounds evidence, and the static
    Constriction image showing Events accepted before Names.
  - **S3** — [RPGFan Windows play review](https://www.rpgfan.com/review/the-rise-of-the-golden-idol/),
    for the automatic collection trigger, movable windows, concurrent
    inspection and close-answer feedback.
  - **S4** — [Pro Game Guides photographed case](https://progameguides.com/general-walkthroughs/rise-of-the-golden-idol-walkthrough/#h-constriction-a-murderous-way-out),
    for the portraits, coloured token bank, accepted sentence and
    Continue while both checks are shown separately.
- Claim IDs: RGI-001–RGI-007.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-030`: direct pointer focus within the fixed event and
  open the corridor, possessions or documents as evidence.
- Reuse `ACT-060`: place one collected token into a compatible blank.
  An unaccepted identity or sentence can be corrected.
- New `ACT-736`: reposition an independent window so a draft, its
  vocabulary and the source scene remain available together.
- Claim IDs: RGI-002–RGI-006.

### System Behaviour Genes

- Reuse `SYS-086`: check the completed Names and Events sections
  independently. The near-answer signal reports limited error count
  information, leaving the player to identify a mistaken slot.
- New `SYS-1559`: inspection itself adds a detail's authored words to
  the case bank. No second input on each marked term is required.
- Claim IDs: RGI-002, RGI-003, RGI-005.

### Constraint Genes

- Reuse `CON-064`: evidence inspection and panel changes leave the
  represented people, objects and event time fixed.
- Reuse `CON-093`: fill slots from terms acquired in the current case.
  The coloured role classes restrict placements without uniquely
  identifying the accepted token in a class.
- Claim IDs: RGI-002–RGI-004.

### Information Genes

- Reuse `INF-001`: fixed evidence is available by directed inspection;
  the current acquired bank, open drafts and filled slots are readable.
  The inferred identity and yet-unopened detail contents are not
  advance disclosures.
- Reuse `INF-024`: the Words panel preserves terms beside the
  fixed text and blanks of a reusable answer scaffold.
- New `INF-522`: read found-over-total spot and word counts
  independently of one another and separately from answer validity.
- Claim IDs: RGI-002, RGI-004, RGI-006, RGI-007.

### Objective Genes

- Reuse `OBJ-017`: supply the accepted identities and event account
  in the mandatory panels to unlock the case exit.
- Claim IDs: RGI-004, RGI-005, RGI-007.

### Time Genes

- Reuse `TIM-002`: deliberate between discrete inspections and edits
  without an active pressure clock on the event or its draft.
- Claim IDs: RGI-002, RGI-007.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Constriction is open after the preliminary exercise | Inspect the badge and then the rounds record | Their authored terms enter Words while the depicted event stays fixed | Source focus and vocabulary acquisition are distinct effects of one inspection | RGI-001, RGI-002, RGI-003 |
| One room label is obscured | Compare the opposed 203/204 numbers and the visible 201; read the 202 entry in the rounds record | Associate the figure with Oriel Toussaint; compare the name Morg Brakka found on the badge | Identity can require spatial inference and independent evidence | RGI-003 |
| The Words panel obscures a useful detail | Move it and place a collected name in a compatible Names blank | The draft and original clue remain separately accessible | Layout is under the player's control and leaves the scene itself unchanged | RGI-004, RGI-006 |
| The word and spot counts are complete; Names is unfinished | Fill Events with the accepted tokens | Events receives its own acceptance while Names remains unfinished | Discovery and acceptance are separate; section order can vary | RGI-004, RGI-005, RGI-007 |
| One complete draft contains compatible but incorrect words | Revise its assignments after feedback | The draft can change and section validation can succeed later | Matching the slot class is weaker than satisfying the account | RGI-004, RGI-005 |
| Both mandatory panels are accepted | Use Continue | Proceed toward the next case | Clearance requires a validated account in both sections | RGI-005, RGI-007 |

## Strategic and experiential structure

Treat the room numbers as a relation and check the inferred room against
the orderly's record. The other identity can be assigned directly from
a badge. The same terms then appear in both portraits and the event
sentence, so a hypothesis can be compared across panels. A player who
has found all words still needs to reason about which terms belong to
which person and location. Finishing the evidence search and finishing
the answers produce visibly separate signals.

## Replay and variation

- Compare opening Words beside Names with keeping both answer panels
  open and moving Words aside before inspecting the corridor.
- Compare a complete wrong draft with a correct draft after visiting the
  same evidence. The discovery counts remain independent of correctness.
- Accept Events before Names, then compare the reverse order on a fresh
  case. The accepted answer is fixed regardless of inspection order.

## Adjacent systems and history

- The Case of the Golden Idol requires explicit term clicks in its
  scoped tutorial, then uses a distinct Thinking screen and a mandatory
  event Scroll. Constriction uses automatic acquisition and movable
  panels with a mandatory, independent Names check.
- Return of the Obra Dinn shares immutable, self-paced, directed
  inspection. It tests batched identity and fate dossiers from a
  ship-wide roster. Constriction collects a local vocabulary and uses
  a different check cadence and answer shape.
- Opening clue panels does not mark the current answer correct.
  Independent display counts do not establish that every clue must
  be inspected for the engine to accept both answers.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-030`, `ACT-060`, `ACT-736` | scene focus, typed assignment and movable draft windows |
| System Behaviour | `SYS-086`, `SYS-1559` | section check and automatic term acquisition |
| Constraint | `CON-064`, `CON-093` | frozen event and typed, case-local vocabulary |
| Information | `INF-001`, `INF-024`, `INF-522` | inspectable scene, reusable word bank and two distinct tallies |
| Objective | `OBJ-017` | accepted names and event account |
| Time | `TIM-002` | untimed investigation and revision |

Canonical signature:

`ACT-030,ACT-060,ACT-736; SYS-086,SYS-1559; CON-064,CON-093; INF-001,INF-024,INF-522; OBJ-017; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `537` (`GAME-0001`–`GAME-0537`).
- Exact genome matches: none.
- Tied near matches: `GAME-0046` — The Case of the Golden Idol (`9 / 13 = 0.692308`).
- Supported combination subsets: `COMB-0046`.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0046` — The Case of the Golden Idol | `ACT-030`, `ACT-060`, `CON-064`, `CON-093`, `INF-001`, `INF-024`, `OBJ-017`, `SYS-086`, `TIM-002` | Both reconstruct a fixed event with structured slots. The predecessor's scoped case requires manual word selection and a separate Thinking view. Constriction gathers words on inspection, keeps windows over the scene and reports spot and word discovery separately. | Tied near (`0.692308`) |

### Preserved research notes

- New genes: `ACT-736`, `SYS-1559`, `INF-522`.
- Classification result: `New gene`.
- Evidence and reasoning: selecting each source word and automatic
  acquisition after opening a source offer different actions. Vocabulary
  progress, visited locations and answer correctness are different states.

## Combination record

- `COMB-0046` — self-paced immutable evidence inspection is a proper
  subset. The case retains directed observation, an unchangeable event
  and no advancing decision clock. Word-bank rules and the two separate
  validations remain outside the combination.
- No other verified combination fits this bounded release scope.

## Taxonomy impact

- Registry changes: three Active additions and nine transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_285](../../../research/taxonomy-changes/TAXONOMY_CHANGE_285.md).

## Negative results

- `ACT-059` is excluded. Eligible words from the opened detail enter
  Words automatically. Their later placement in an answer is a
  different action.
- The short starting exercise and later chapter recaps do not
  establish a mechanic in this bounded scene.
- A coarse report of one or two wrong entries does not identify which
  entry is wrong. Optional hints and exact synonym acceptance remain
  outside the scoped claims.

## Delta summary

## New facts

- [Observation | Corroborated | High] Inspection automatically acquires
  terms and two mandatory deduction panels can be confirmed independently.

## New genes

- [Observation | Corroborated | High] Three additions in
  `TAXONOMY_CHANGE_285`.

## New combinations

- [Observation | Corroborated | High] An existing proper subset gains
  a third supporter. No new combination proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_285`.

## New questions

- Which exact authored substitutions are accepted in the current Windows
  build and did that set change for this prologue after launch?

## Next recommended game

- [Hypothesis | Limited | Medium] Scope the original Nintendo 64
  *Blast Corps* to one carrier route under Selection 042.
