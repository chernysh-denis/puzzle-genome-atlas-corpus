---
game_id: GAME-0606
slug: the-seance-of-blake-manor
game_title: "The Séance of Blake Manor"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-060
    - ACT-232
    - ACT-341
    - ACT-806
  system:
    - SYS-680
    - SYS-1559
    - SYS-1780
    - SYS-1781
  constraint:
    - CON-093
    - CON-136
  information:
    - INF-024
    - INF-571
  objective:
    - OBJ-017
  time:
    - TIM-043
---

# Game: The Séance of Blake Manor

This scope follows the
[canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Names, clock readings, fixture values and the three comparison points
are parameters of this first case.

## Analysis scope

- Version / ruleset: English full Windows Steam release, app `1395520`,
  issued 27 October 2025. The primary Steam trace was published 9
  November 2025 and corroborates an early commercial ruleset. Its
  exact installed build and compatibility with later patches are
  unverified. The demo is a separate Steam app and is excluded.
- Primary decision loop: spend priced investigation actions selectively
  before midnight, create a known handwriting reference, question and
  observe the manager, use the telegraph repair to gain office access,
  compare the departure signature and place evidence-derived terms in
  the hypothesis. Then make the accepted inference about the unknown
  writer and check how it advances the journal.
- Entry: ordinary control just inside the manor's main entrance on the
  first evening, before checking in or recording the required signatures.
  The opening courtyard and its optional evidence are outside the case.
- Exit: the recorded ability-to-write criterion in the culprit view
  and the visible unlock of The Culprit, verified in the course of leaving
  the office by its window. Stop before the separate lobby exchange, bedtime, dream
  and any investigation of specific candidates.
- Included: local navigation, reception bell, guest registration,
  relevant object and person observations, testimony about Evelyn,
  discarded telegraph parts and replacement discs, the stacked-cell
  test, the repair dialogue, ordinary office access, departure letter,
  targeted signature comparison, the supported hypothesis, its follow-up
  and the first new journal case.
- Excluded: peripheral evening events and evidence without a causal role
  in this route, later mysteries, identity selection, confrontation,
  alternate endings, later builds, demo, ports, fast-route exploits and
  save/reload behaviour outside the observed route.
- Suggested later scope: one complete suspect case using both a formal
  hypothesis and a subsequent confrontation under a named installed build.

## Direct-play status

No direct play was performed. Raw Fury and Steam establish the full Windows
release. Static frames of beav's explicitly Steam commercial playthrough
show the opening rule, both evidence sources, the restoration and the
accepted inference. A contemporaneous written walkthrough and a separate
early recording corroborate the sequence. Installed builds, alternate
wrong answers, precise slot-error feedback, the full deadline-failure rule
and native save retention were not independently tested. No video or audio
playback was used.

## Claim ledger

| ID | Claim | Claim status | Evidence quality | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- |
| BM-001 | The full English Windows Steam game shipped on 27 October 2025. The standalone demo and later material fall outside the ruleset used for this record. | Confirmed | Corroborated | High | P1, P2, P3. Installed build is not claimed. |
| BM-002 | Inside the entrance the opening notice specifies midnight for the first investigation. The journal exposes Miss Deane’s Departure and a check-in lead. Ordinary movement and charged interactions are distinct. | Observation | Corroborated | High | P1, W1 3:50–5:00, H1. Exact outcome of missing the deadline was not observed. |
| BM-003 | The guest book has individually selectable observations, including Evelyn’s recorded signature. Varley’s appearance can also be analysed for separate observations during conversation. Discussing Evelyn and that inspection support the office-letter lead. | Observation | Corroborated | High | H1, W1 5:20–5:50, 7:40–9:10, W2 48:00 and 51:00. Other observations are not asserted as minimal prerequisites. |
| BM-004 | The faulty telegraph uses a distinct stacked-disc puzzle. Replacement types are available at reception and the reference illustration gives an ordered unit. The written route reports six repeated units and the demonstrated test accepts the repaired assembly. | Observation | Corroborated | High | H1, W1 9:30, 10:00–10:50. No rule is claimed for arbitrary alternative stacks. |
| BM-005 | Reporting the fixed telegraph to Varley moves him away from the office. The office-search lead and normal entry are visible after this change. | Observation | Corroborated | High | H1, W1 11:20–12:10. The observed route uses the report rather than exploiting access timing. |
| BM-006 | Separate office records can be examined. The disputed letter is on the manager's desk clipboard and can be compared once the genuine reference is known. | Observation | Corroborated | High | H1, W1 12:30–13:30, W2 1:24:00 vicinity. Other documents from the room need not be named as prerequisites. |
| BM-007 | The authored handwriting comparison presents the two samples together. Mark three differences to reach the evidence-confirmed hypothesis state. | Observation | Corroborated | High | H1, W1 13:30–13:40. The inspected targets are specific strokes and not language typed by the player. |
| BM-008 | Evidence makes selectable terms available. Enter the subject, document and forged status on the Hypothesis panel and choose Consider. The accepted sentence opens a separate inference about the actor. | Observation | Corroborated | High | W1 13:40–14:40, H1. The exact UI error behaviour of an incorrect sentence was not tested. |
| BM-009 | Selecting the writing inference adds a retained ability-to-write fact about the unknown actor. The distinct The Culprit investigation appears after the successful inference. One trace shows the unlock before leaving and another shows it during the window departure. | Observation | Corroborated | High | W1 14:40–15:30, H1, W2 1:24:30–1:26:20. No culprit identification or full campaign resolution follows from the fact alone. |
| BM-010 | Some inspections advance the in-game clock in minute steps. Several focused observations and most of the positive deduction sequence hold the displayed minute while real time passes. | Observation | Corroborated | High | P1, W1 5:30–5:50, 10:00–10:20, 14:10–15:30, H1. Exact action prices outside the scope are not transferred. |

## Basic data

- Release / origin: Spooky Doorway developed and Raw Fury published the
  Windows game, commercially released on Steam on 27 October 2025.
- Platform: `PLAT-WINDOWS-PC`, English single-player Windows Steam base
  game. The identified commercial app is not the standalone demo.
- Puzzle families: knowledge and evidence progression (FAM-012) for the
  comparison and hypothesis, and inventory and fixture dependencies
  (FAM-013) for repair supplying the practical route to the evidence.
- P1: [commercial Steam listing](https://store.steampowered.com/app/1395520/The_Seance_of_Blake_Manor/).
  Release, platform, investigation premise and the role of time and actions.
- P2: [Raw Fury release announcement](https://rawfury.com/the-seance-of-blake-manor-out-now/).
  Identifies the released commercial game and scenario.
- P3: [Steam demo listing](https://store.steampowered.com/app/3547180/The_Sance_of_Blake_Manor_Demo/)
  and [publisher's September 2026 demo and full-game update](https://store.steampowered.com/news/posts/?enddate=1788339603&feed=steam_community_announcements).
  The separate app and later main-mystery updates are distinct from the
  captured opening. No equivalence across them is assumed.
- H1: [Into Indie Games firsthand Day 1 walkthrough](https://intoindiegames.com/walkthroughs/the-seance-of-blake-manor-walkthrough-day-1/),
  published 29 October 2025. Shows the evidence, telegraph, letter,
  comparison and accepted hypothesis. Other guided steps are outside the unit.
- W1: [beav full commercial Steam playthrough](https://www.youtube.com/watch?v=SQU-aOGVQ6I),
  published 9 November 2025. The description explicitly identifies Steam.
  The early frames through 15:30 show the required sequence.
- W2: [rx Hydro first evening recording](https://www.youtube.com/watch?v=0EHNEUC7Yk0),
  published 2 November 2025. Cross-checks registration, dialogue, office
  and the retained culprit fact. Its exact installed build and store
  entitlement are unverified.

### Reproducible route evidence

1. Enter through the main doorway. Read the opening midnight notice
   and select the journal's Miss Deane’s Departure card. Its first lead
   directs Ward to check in. W1 3:50–4:30 shows this transition.
2. Ring the bell and meet manager Vincent Varley. Open the sign-in book
   and select the specific reference signature of Evelyn Deane. In W1
   5:30 it is already a separate observation and additional book
   observations update the visible tally without consuming another
   displayed minute inside that opened view.
3. Ask Varley about Evelyn. The actor-analysis view exposes individual
   details such as his hand on a watch and the damaged glasses. The
   discussion and examination reveal a lead to find the letter. H1
   distinguishes the case contact from optional broader conversation.
4. Collect replacement discs at the reception fixture and examine the
   nonworking telegraph. Remove its spent stack and use the authored
   layer reference. Repeat the three-type layer unit to build the
   required stack. H1 reports the target of six in the game's capacity
   units. W1 10:30–10:50 shows the reference and a successful test.
5. Return to reception and discuss the repaired machine. Varley leaves
   for the telegraph room. Approach his now accessible office through
   its ordinary door and identify the disputed letter on the desk
   clipboard. W1 11:20–12:10 shows the change to office access and
   13:10–13:30 the document route.
6. Compare the authentic signature and the disputed one in the paired
   view. Mark the three authored differences rather than guessing a
   story proposition from the mere existence of a letter. The view at
   W1 13:30 has individual red annotations. The evidence notification
   at 13:40 enables the hypothesis.
7. Open the hypothesis and fill the three indicated roles with Miss
   Deane’s departure, the letter and its forged status. Select Consider.
   The resulting dialogue asks what can be inferred about the unknown
   writer. Select the writing ability option shown at W1 14:40.
8. Verify the new ability-to-write fact in the culprit view at W1
   15:10. W2 shows Mystery Solved at 1:24:50 and The Culprit
   unlocked by 1:26:20 inside the office. Leave by the window on the
   evidenced route. W1 15:30 also shows the new case as Ward departs.
   Leaving marks the scope boundary. It does not unlock the case itself.

Claim IDs: BM-002–BM-010. The wall-time evidence addresses, in-game
minutes and action durations refer to different clocks.

## Mechanical decomposition

### Action Genes

- ACT-008: navigate Ward directly between reception, telegraph and office.
- ACT-060: assign a known evidence-derived term to one compatible gap.
- ACT-232: discuss Evelyn and report the fixed telegraph to change the
  investigation and the manager's next destination.
- ACT-341: use eligible fixtures such as the bell, sign-in book and
  telegraph before addressing the disputed letter.
- ACT-806: select authored contrasting features in the paired signatures.
- Claim IDs: BM-002–BM-009.

### System Behaviour Genes

- SYS-680: the live investigation registers examined source details and
  relates them to the next authored lead.
- SYS-1559: acquiring eligible evidence exposes its authored terms to
  the hypothesis without an additional manual copy of each word.
- SYS-1780: tests an accumulated stack for the correct repeating layers
  and required capacity before admitting the repair.
- SYS-1781: the accepted hypothesis and follow-up produce a fact about
  a still-unknown actor and enable a related investigation.
- Claim IDs: BM-003–BM-009.

### Constraint Genes

- CON-093: choose a gained candidate from the appropriate term category.
  Mere possession of several possible words does not solve a gap.
- CON-136: the demonstrated route needs acquired parts before the
  telegraph test, repair before its successful report, and the
  letter comparison before the accepted hypothesis.
- Claim IDs: BM-004–BM-009.

### Information Genes

- INF-024: a prewritten scaffold exposes slots and permits reading
  the available terms beside it.
- INF-571: the case exposes connected leads, discoveries and unfinished
  nodes as a navigable journal structure.
- Claim IDs: BM-002, BM-003, BM-007, BM-008.

### Objective Genes

- OBJ-017: supply the supported subject, document and verdict in the
  structured hypothesis and reach the accepted finding.
- Claim IDs: BM-007–BM-009.

### Time Genes

- TIM-043: charged actions move the case clock in minutes. Time does
  not fall continuously during local navigation and the open comparison
  in the sampled opening.
- Claim IDs: BM-002, BM-003, BM-010.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Ordinary control inside the manor | Open the announced mystery | Check-in lead is available under a midnight due time | The first task and its schedule are disclosed | BM-002 |
| Reception and register accessible | Check in and select Evelyn’s book signature | A genuine comparison reference is recorded | A book can contain separately acquired evidence | BM-003 |
| Varley available | Discuss Evelyn and analyse visible details | A letter lead becomes actionable | Interviews and observations can open the next evidence stage | BM-003 |
| Fault and replacement parts available | Assemble and test the repeated fixture layers | Telegraph works | Correct layer order and capacity both matter | BM-004 |
| Telegraph repaired with Varley still available | Report the repair | He relocates, enabling the evidenced office visit | The physical repair and its dialogue result are separate | BM-005 |
| Genuine signature registered and letter found | Mark three differences in the paired view | Evidence can support synthesis | Comparing features differs from collecting the sheet | BM-006, BM-007 |
| Hypothesis available | Fill the slots and choose Consider | Accepted forgery finding asks for a further inference | Authored word matching is distinct from interpretation | BM-008 |
| Writing inference chosen | Read the saved fact and verify the new case before or during the window exit | The Culprit is available in the journal | The first case settles with a criterion for a later case | BM-009 |

## Strategic and experiential structure

Because selected inquiries cost in-game time, prioritize the signature and
the office access path. The fixture is not itself evidence of forgery. Its
use is to make the office visit possible through an authored conversation.
The evidence comparison establishes what happened to the letter. The
second inference turns that result into a limited criterion for the
next investigation. Claim IDs: BM-002–BM-010.

## Replay and variation

The two early recordings differ in time spent on adjacent observations.
Neither proves minimum evidence requirements, the full timing cost table,
or the response to deliberate wrong hypotheses. H1 recommends leaving
through the window and warns that using the office door at that stage
can end the investigation. That side branch was not reproduced here.
Claim IDs: BM-006–BM-010.

## Adjacent systems and history

Later cases can involve other interviewees, timetables, room occupancy and
confrontations. The culprit board now carries a limited fact. It does not
yet assign a name or imply a final resolution. The dream sequence and
subsequent weekend investigation are outside this case. Claim IDs:
BM-009, BM-010.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-060, ACT-232, ACT-341, ACT-806 | Traverse, bind a term, converse, use a fixture and compare features |
| System Behaviour | SYS-680, SYS-1559, SYS-1780, SYS-1781 | Evidence progression, term admission, ordered stack and saved inference |
| Constraint | CON-093, CON-136 | Candidate categories and prerequisite order |
| Information | INF-024, INF-571 | Hypothesis scaffold and named case graph |
| Objective | OBJ-017 | Complete an accepted structured account |
| Time | TIM-043 | Allocate time in priced interactions |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `605` (`GAME-0001`–`GAME-0605`).
- Exact genome matches: none.
- Tied near matches: `GAME-0597` — Duck Detective: The Ghost of Glamping (`7 / 20 = 0.350000`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Duck Detective: The Ghost of Glamping (GAME-0597)](../a-f/duck-detective-the-ghost-of-glamping.md) | ACT-008, ACT-060, ACT-341, CON-093, INF-024, OBJ-017, SYS-1559 | Both inspect evidence in a navigable scene and use the automatically available terms in authored slots. Duck Detective closes a local naming and campsite account. Blake Manor spends investigation minutes and gains the letter through a repaired fixture and changed room access, then retains a separate clue about an unknown writer. | 7 shared of 20, Jaccard 0.350000 |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_352](../../../research/taxonomy-changes/TAXONOMY_CHANGE_352.md)
  defines the five new boundaries and records the reused hypothesis rules.

## Negative results

- ACT-059 requires clicking individual evidence words to copy them.
  Confirmed observations and the completed comparison grant selectable
  terms here. SYS-1559 supplies that automatic transfer.
- CON-064 would require an immutable evidence tableau. The relevant
  documents are inspected in close views, while the live manor changes
  during the telegraph and access chain.
- SYS-042 confirms proper batches of identities and fates. Here one
  written result leads to a separately accepted actor trait.
- TIM-003 is a live time-driven schedule. The opening uses priced actions
  with non-continuous progression in the sampled moments.
- ACT-160 uses a spatial crafting grid. An ordered vertical stack with
  a test models the repair more precisely.

## Delta summary

## New facts

- [Observation | Corroborated | High] Registration provides an authentic
  signature and the manager's absence makes the disputed letter reachable.
  BM-003–BM-006.
- [Observation | Corroborated | High] Three comparison observations
  support the typed forgery hypothesis. The accepted follow-up supplies
  the first usable culprit trait and the case handoff. BM-007–BM-009.
- [Observation | Corroborated | High] Charged inspections advance a
  displayed in-game clock while the sampled evidence and deduction views
  do not continuously spend it. BM-010.

## New genes

- [Observation | Corroborated | Medium] ACT-806, SYS-1780, SYS-1781,
  INF-571 and TIM-043.

## New combinations

- [Observation | Direct | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_352.

## New questions

- Which case facts are the minimum required to admit Consider?
- How is an incorrect complete sentence signalled and can it be corrected
  without charging time under the sampled release family?
- How does the game settle at midnight with the required case unresolved?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0607`, Mischief Makers, North
  American Nintendo 64. Trace an early stage from grasp, shake and throw
  to the recorded exit or evaluation.

## Why this game

- [Hypothesis | Limited | Medium] One bounded case links physical access,
  comparison of two tangible samples and structured argument to a
  specific, limited fact about another actor.
