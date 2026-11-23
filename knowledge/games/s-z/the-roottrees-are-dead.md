---
game_id: GAME-0660
slug: the-roottrees-are-dead
game_title: "The Roottrees are Dead"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-030
    - ACT-108
    - ACT-874
    - ACT-875
  system:
    - SYS-042
    - SYS-1901
  constraint:
    - CON-876
  information:
    - INF-012
    - INF-608
  objective:
    - OBJ-017
  time:
    - TIM-002
---

# Game: The Roottrees are Dead

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: the English commercial Windows Steam remake,
  app 2754380, released 15 January 2025. Scope is the base game's
  opening Roottree Sisters tutorial, with launch-period evidence.
  Exact installed Steam build, input timing and save persistence
  remain unverified.
- Entry: after the first employer conversation, the board shows
  three blank sibling cards, the To Do List and the oldest-to-youngest
  arrow. The photo and a supplied list of names are available to inspect.
- Primary decision loop: inspect the original photo and register faces
  as eligible portraits. Search the fictional Internet for the sisters.
  Refine leads with specific names or a brand term, then cross-reference
  the results and left-to-right birth order to choose a name, occupation
  and portrait for each card. Revise provisional assignments as needed
  until the game confirms and locks the three correct records together.
- Exit: the confirmation screen lists the three locked sisters and
  reads 3 / 50 Blood Relatives. Continue through the employer's handoff
  to the wider available family board; the later tree investigation
  is outside this packet.
- Included: the provided photo and name list, face selection and
  portrait registration, typed searches and one documented refinement,
  sibling position, three kinds of editable fields, the shared
  confirmation and the first wider board. The optional spouse field
  is documented only to delimit the completion condition.
- Excluded: completing the whole tree, later hints and archives,
  knowing all encounter names before search, optional spouse solving
  as a requirement, exact search implementation and untested aliases,
  cross-session persistence, the 2023 browser original,
  Roottreemania and other platform editions.
- Suggested later scope: follow a specific source after the first
  handoff into its distinct archive, then isolate the prerequisite
  for the first subsequent family-record lock.

## Direct-play status

No direct play was performed. The official Steam listing and publisher
site identify the commercial remake and describe its evidence-led
family-tree loop. Fever's January 2025 Steam walkthrough supplies the
principal Windows trace; Marstead's separate 2025 run corroborates
the three-entry lock and shows how an optional entry is presented.
Only still frames and on-screen text were reviewed, in the background
without audio. Exact depot, capture hardware and save reload were not
verified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| RT-001 | The commercial Steam remake launched on 15 January 2025 and supports English and Windows. The scoped test opens on the three sisters' blank cards. | Observation | Corroborated | High | P1, P2; W1 0:00 and 1:53–2:10, W2 2:37–3:10. The Windows exit label and Steam attribution establish the main capture context, not its exact build. |
| RT-002 | Opening the employer's group photo exposes usable faces. Merely viewing it does not populate the portrait picker; selecting faces from the evidence makes those crops independently selectable. | Observation | Corroborated | High | P2's evidence loop, R1, W1 2:22–2:48 and 6:54–7:19. At 6:55 the picker still reports no available portraits, while after the face selection it contains three. |
| RT-003 | Free-text SpiderSearch returns written in-world evidence. The sisters query supplies modeling and nickname or birth-order leads; the interface indicates spelling and punctuation can matter despite case-insensitive lookup. | Observation | Corroborated | High | P2; W1 4:24–4:47 and 9:17–9:51. `ROOT` shows advice about the common term, while `ROOT. clothing` returns the clue about the fashion brand. The recordings do not establish the search algorithm or test punctuation in isolation. |
| RT-004 | The sibling links and oldest-to-youngest arrow make birth order a slot clue before identities are known. The board accepts separate provisional names, occupations and portraits from distinct pickers. | Observation | Corroborated | High | R1/R2, W1 6:49–7:23, 7:56–8:09 and 12:55–13:07; W2 11:10–12:30. A roster name and a face can be held provisionally without completing the occupation. |
| RT-005 | All three accepted tutorial cards are locked together after the final needed edit, with confirmed entries and the 3 / 50 Blood Relatives count shown. The three accepted occupations are Model. | Observation | Corroborated | High | W1 12:22 and 12:55–13:20, W2 18:11–18:36, R1/R2. Compare the editable board and the named confirmation. Both traces show the grouped transition, without evidence of per-field validation or that every later lock has the same threshold. |
| RT-006 | The optional spouse is not a fourth mandatory tutorial entry. The main receipt shows no optional record; the second receipt confirms one separately while the count still reads 3 / 50. | Observation | Corroborated | High | W1 13:19, W2 18:26–18:36. The extra field and its separate presentation are in scope, not its identity or the mechanics of later optional batches. |
| RT-007 | Continuing after confirmation leads to the second employer conversation and the wider editable family board. The first lock is a tutorial handoff, not resolution of the larger investigation. | Observation | Corroborated | High | W1 13:20–15:20, W2 18:30–20:19; P2 for the wider family-tree task. No reload or persistent achievement predicate was tested. |

## Basic data

- Analysis target: `PLAT-WINDOWS-PC`, commercial English Windows
  Steam remake, app 2754380, 2025.
- Commercial developer and publisher: Evil Trout Inc. The Steam
  listing distinguishes the remake from the 2023 browser game.
- Mechanical families: `FAM-001`, constraint deduction;
  `FAM-012`, knowledge and evidence progression.
- Checked: 2026-11-23.
- P1: [Evil Trout's Steam product listing](https://store.steampowered.com/app/2754380/The_Roottrees_are_Dead/).
  Release date, distribution, platform support and original/remake split.
- P2: [Official publisher game site](https://roottrees.com/).
  Describes evidence retrieval, deduction and filling a fixed family tree.
- R1: [Neoseeker's commercial game walkthrough](https://www.neoseeker.com/the-roottrees-are-dead/walkthrough).
  Describes the first board, photo registration and different fields.
- R2: [9Puz's first-test route and placement notes](https://9puz.com/2462-the-roottrees-are-dead-walkthrough/).
  Used for the initial evidence, birth order and three mandatory entries.
  Named role and optional claims rely on the observed receipts.
- W1: [Fever's Steam-edition walkthrough](https://www.youtube.com/watch?v=nYp86N9jvs4&t=113s),
  30 January 2025. Main trace, with the Windows exit label,
  empty-to-populated portrait picker, query refinement and first receipt.
- W2: [Marstead's separate 2025 opening run](https://www.youtube.com/watch?v=GmNQ8hIiXa4&t=157s),
  2 May 2025. Corroborates the first tutorial and the optional-entry
  distinction. The underlying capture build and platform label are
  attributed only where visible or identified.

## Mechanical decomposition

### Action Genes

- ACT-030: focus an immutable photograph and inspect individual faces.
- ACT-108: submit free-text queries to the fictional archive.
- ACT-874: select a pictured subject to register its cutout as a
  selectable portrait.
- ACT-875: set and revise the separate name, occupation and portrait
  for one provisional card on the existing tree.

### System Behaviour Genes

- SYS-042: confirm and lock three complete correct required records
  together when the first threshold is met.
- SYS-1901: a specific typed term exposes one authored account or
  help response inside the fake search interface. Refining a lead
  reaches a different response.

### Constraint Genes

- CON-876: each provisional relative card accepts its name and job
  from their supplied pickers and its portrait from registered
  evidence faces. These are typed field domains, not an unrestricted
  answer input. Occupations can repeat across records.

### Information Genes

- INF-012: stable named evidence such as the supplied photo and
  recalled search responses can be revisited and compared after
  discovery.
- INF-608: sibling positions visibly encode oldest-to-youngest
  order independent of their still-unknown names and portraits.

### Objective Genes

- OBJ-017: complete the three mandatory structured entries of this
  opening account. Its result is the first locked batch, not the
  whole 50-relative case.

### Time Genes

- TIM-002: select faces, read searches and revise cards at a chosen
  pace. The fictional computer clock does not drive a decision
  deadline for this packet.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| Three blank sibling cards after the employer | Open the evidence photo and inspect the pictured faces | The source depicts the three sisters; viewing alone leaves the portrait picker empty | RT-001, RT-002 |
| Photo is open and a face is available | Select that face to register it | Its individual crop becomes selectable; returning to the board does not by itself identify its correct slot | RT-002 |
| A clue term in the photo note or current account is available | Submit the sisters query, read its names, clue wording and occupations, and refine an ambiguous lead | A fixed result supplies birth-order and role clues; the brand query retrieves different authored context | RT-003 |
| Birth order visible and three separate candidate pools available | Choose name, occupation and portrait separately, revising a provisional placement where needed | The blue cards remain editable while the batch is incomplete. All three occupations can use the same candidate | RT-004, RT-005 |
| Three correct complete required entries coexist | Finish the final necessary field choice | One confirmation enumerates the entries and raises the blood-relative count to 3 / 50. The optional line can be empty | RT-005, RT-006 |
| The first confirmation is shown | Continue through the employer's conversation | The wider family board becomes reachable with ordinary inspection and placement control | RT-007 |

## Strategic and experiential structure

Birth order narrows the slot without naming its occupant. Search
results supply clues that still need to be compared against an image
and the finite roster. An exposed portrait adds one candidate but
does not establish its identity. Editing remains provisional until
a check can settle several complete cards together, so a plausible
assignment can be held while a different clue is pursued.

## Replay and variation

The principal run registers portraits from the employer's photo and
locks only the three required records. The secondary run also locks
one optional name. Both reach 3 / 50. The portrait art looks
different between the captures. With exact builds unverified, this
does not establish that multiple distinct crops are accepted for
each sister within a single installed build.

## Adjacent systems and history

The 2023 browser original is a separate source and was not
substituted for the Steam remake. The broader board introduces
more people, proceedings and evidence surfaces after this test.
Those later links, search types and campaign termination require
their own bounded study.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-030, ACT-108, ACT-874, ACT-875 | Inspect, query, register usable portraits and revise typed relative cards |
| System Behaviour | SYS-042, SYS-1901 | Confirm a correct batch and route authored search responses |
| Constraint | CON-876 | Accept only candidates offered for each of the three separate field classes |
| Information | INF-012, INF-608 | Revisit evidence and use the displayed sibling birth order |
| Objective | OBJ-017 | Complete the first exact three-record account |
| Time | TIM-002 | Read and revise at the player's pace |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `659` (`GAME-0001`–`GAME-0659`).
- Exact genome matches: none.
- Tied near matches: `GAME-0023` — Return of the Obra Dinn (`5 / 16 = 0.312500`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Return of the Obra Dinn (GAME-0023)](../m-r/return-of-the-obra-dinn.md) | ACT-030, INF-012, OBJ-017, SYS-042, TIM-002 | Both allow revisiting fixed evidence, entering a structured account and waiting for grouped confirmation at the player's pace. Obra Dinn opens a frozen death memory from a corpse and assigns identities and dependent fates from a manifest. Roottrees submits written search terms, registers individual pictures and fills names, jobs and portraits at visible birth-ordered positions. | Near, `0.312500` |

## Taxonomy impact

ACT-874 creates a reusable portrait choice, distinct from magnifying
the source under ACT-030 or extracting a highlighted phrase under
ACT-059. ACT-875 joins three typed fields on a positioned relative
card. The fate clause and dependencies in ACT-032 are absent here.
CON-876 distinguishes supplied names and occupations from acquired
portraits; CON-093 constrains phrase slots to the case's extracted
vocabulary. INF-608 discloses an otherwise unknown subject's birth
rank, not the manifest with named role metadata in INF-013.
SYS-1901 returns authored prose or advice rather than the ordered
transcript matches of SYS-142. SYS-042 already expresses the
thresholded correct-record settlement, with the tuple and count as
parameters.

## Negative results

- An opened photograph alone leaves no portrait candidates.
- The names and portraits can both be filled while the current
  batch remains editable because occupations are incomplete.
- The first receipt succeeds with an empty optional line. It
  never proves completion or reload of the wider 50-person record.
- No exact substring behavior, fuzzy-match range or untested
  normalization is inferred from the story browser.

## Delta summary

Eleven scoped genes, including five new and six reused boundaries.
No prior signature or verified combination is revised.

## New facts

- A click on a face makes one sourced portrait available for later
  selection independently of identification.
- Birth order is visible even when every relative is unidentified.
- The photograph, name and occupation become accepted together
  under the three-record threshold rather than when first entered.

## Principles and design implications

Give a structured board legible positional meaning before disclosing
candidate assignments. Let a source expose an affordance to register
one candidate independently of answering. Separate a complete
provisional card from the group of correct cards the game confirms.

## Puzzle or game generation potential

Give three named positions in order and an uncatalogued group image.
Add a searchable document with a nickname and a role shared by
multiple subjects. Require identity, role and portrait across the
three positions, then confirm only the combined correct account.

## New genes

- ACT-874
- ACT-875
- CON-876
- INF-608
- SYS-1901

## New combinations

None of the 274 verified combinations is a proper subset. COMB-0023's
corpse-triggered scene, compound fate and finite identity-role roster
requirements are absent. The shared lock-in does not imply that
interaction is present.

## Taxonomy changes

[TAXONOMY_CHANGE_406](../../../research/taxonomy-changes/TAXONOMY_CHANGE_406.md).

## New questions

Which equivalent image crops are recognized across different evidence
sources? When can a correct optional entry be locked after its nearby
required cards already are? Which normalization is shared across
fictional search interfaces?

## Next recommended game

Pilotwings, original English North American Super NES cartridge.
Trace one complete opening Flight Club trial through its airborne
task, landing and accepted score or licence boundary.

## Why this game

The tutorial makes the difference between finding a clue, registering
a candidate, assigning it to a birth-ordered record and committing
three complete correct records observable in one bounded loop.
