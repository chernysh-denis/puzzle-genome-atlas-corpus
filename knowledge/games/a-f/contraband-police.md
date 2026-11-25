---
game_id: GAME-0705
slug: contraband-police
game_title: "Contraband Police"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-072
    - ACT-104
    - ACT-105
    - ACT-922
  system:
    - SYS-137
    - SYS-138
    - SYS-1984
  constraint:
    - CON-157
  information:
    - INF-299
  objective:
    - OBJ-370
  time: []
---

# Game: Contraband Police

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Request the second visitor's documents and compare a validity date against
the checkpoint calendar. Record the grounds separately from stamping a
verdict, then check how the game rates both after the driver leaves.

## Analysis scope

- Version / ruleset: English Windows Steam commercial base product
  756800, Crazy Rocks and PlayWay, released March 8, 2023. Reference
  captures were published in March and April 2023. Exact depot builds,
  client patches, key remaps and comparison settings are unverified.
- Structured analysis target: PLAT-WINDOWS-PC in
  [platform coverage](../../platforms/games.json).
- Entry: Chapter I, Training, Day 1, April 16, 1981 in the fictional
  checkpoint. Start after the guided first visitor has left. Call the
  next vehicle using the admission lever, approach its driver and
  request the passport and entry permit.
- Primary decision loop: open the Duty Folder, read the two documents
  and the current date, and invoke the field comparator on selected
  facts when useful. Record the suspected discrepancy category on the
  separate Inspection Report. Apply the denial stamp and return the
  papers. Wait for the vehicle to leave and verify the review result.
- Positive terminal: the second visitor departs and the game credits
  a justified refusal, with a reported grade or cash award. The two
  observed packets have different expired documents and ratings.
- Included: the addressed call and approach, the one current packet,
  selected fact comparison, active admissibility requirements, report
  marking, committed refusal and post-departure review.
- Excluded: the opening briefing, first and later visitors except as
  context for the entry, searches, arrests, chasing, combat, trade,
  other days and modes, exact scoring weights, and any later client or
  device rules. Neither case establishes a shift intake cutoff.
- Potential scoped module: compare two independently priced outcomes
  for the same fixed date discrepancy on a known retail build.
- Direct-play status: no personal Windows run, input telemetry or
  runtime inspection. Steam establishes the released product and
  comparison options. Two independent early retail recordings were
  examined via silent frames. A live checkout of current retail
  behaviour and the exact settings of the witnesses are unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| CP-001 | Crazy Rocks and PlayWay released the Windows Steam base game on March 8, 2023. The observed records show English Chapter I play during the early release period. | Confirmed | Direct | High | P1, P2; W1, W2 |
| CP-002 | The player controls approach to a called vehicle and requests its passport and entry permit. The Duty Folder shows the current date beside the separate documents. | Observation | Corroborated | High | W1 7:20–7:45, W2 4:50–5:22 |
| CP-003 | The second visitor's defect may be expiration in a different document. W1 shows a permit valid through April 11 and a passport current through November 29. W2 shows a passport expiring February 15 and permit valid through September 15. The checkpoint shows April 16, 1981 in both. | Observation | Corroborated | High | W1 7:43–8:17, W2 5:20–5:42 |
| CP-004 | Holding inspection focus and selecting two facts can render a relation before any verdict. Comparing the W2 passport expiration to the calendar gives `MISMATCH`. Equality of a name or passport number alone does not establish admissibility. | Observation | Corroborated | High | P1, P2; W2 5:28–5:42 |
| CP-005 | A category mark on the Inspection Report is separate from the terminal passport stamp. W2 shows `Expiration Date` marked; W1 visibly marks `Photo`. Each witness independently applies `DENIED` and the vehicle leaves. | Observation | Corroborated | High | W1 8:11–8:36; W2 6:03–6:34 |
| CP-006 | The refusal outcome and report evaluation are separate. W1 receives `JUSTIFIED REFUSAL`, +$80 and `GREAT`; the audit shows a red cross on `Photo`. W2 receives the same refusal classification with $100 and the `Perfect inspection!` message. | Observation | Corroborated | High | P2; W1 8:38–8:44; W2 6:34–6:40 |
| CP-007 | Individual audit fields, total reward and grade are visible after departure. The two observations do not isolate a universal per-field cost or prove all audit colour semantics. | Observation | Corroborated | Medium | P2; W1 8:42–8:45; W2 6:35–6:38 |

## Basic data

- Release / origin: Windows Steam retail base game, app 756800,
  March 2023. Fictional Day 1 document room and second driver only.
- Family: FAM-012. The decision advances by relating case materials,
  checking the current date, recording a reason and receiving an audit.
- P1: [Crazy Rocks and PlayWay's commercial Steam page](https://store.steampowered.com/app/756800/Contraband_Police/).
  Identifies the product, date and Windows requirements. Its
  document-control description makes any discrepancy disqualifying.
- P2: [Crazy Rocks release-period Steam announcements](https://store.steampowered.com/news/posts/?appids=756800&enddate=1689347344&feed=steam_community_announcements).
  The March 17 patch discusses document comparison settings and
  audit detail for missed errors. That establishes a version
  distinction without authenticating either witness's binary.
- W1: [PalatinG, Chapter I Training](https://www.youtube.com/watch?v=bx8ykCsOf_M&t=440s),
  published March 16, 2023. Follow the second visitor in the green
  compact from the permit date to the itemized `AUDIT #2`.
- W2: [Totohli Gameplay, Chapter 1 Training](https://www.youtube.com/watch?v=lcMFno1Mpqk&t=294s),
  published April 8, 2023. Follow the second visitor in a black
  compact from the calendar comparison to the perfect refusal notice.
- Claim IDs: CP-001–CP-007.

### Reproducible fixture evidence

1. Use the lever to call the next vehicle after the guided inspection.
   Go to the driver's window and request the two documents. W1 shows
   the window interaction at 7:39 and the opened folder by 7:43.
2. Compare validity dates independently against the current calendar,
   rather than assuming the two expiry dates need to match. W1 at
   7:55 shows a permit valid to April 11, a passport current to
   November 29 and a current date of April 16. W2 at 5:41 shows a
   passport expiring February 15, a September 15 permit and the
   same day. All dates in these two comparisons are in 1981.
3. In W2 use the pair comparator at 5:41. The link between passport
   expiration and calendar shows `MISMATCH`. The separate paper
   shown at 6:07 has a mark on `Expiration Date`. W1 at 8:12
   shows `Photo` marked even though the visibly expired permit
   is the grounds for refusal.
4. Address the visitor again, choose the denial item and stamp the
   passport. W2 displays the red passport impression around 6:16.
   W1 shows the stamp motion at 8:19 and the visitor turning
   away. Returning the paperwork commits the outcome.
5. Wait for the vehicle to clear. W2 at 6:35 shows a justified
   refusal with $100 and the perfect message. W1 at 8:42 shows
   `AUDIT #2`, +$80, `GREAT` and a red cross on the Photo row.
   Both refuse admission. The payout values belong to these cases.

## Mechanical decomposition

### Action Genes

- ACT-008: walk from the call control to the addressed driver's window.
- ACT-072: use the designated lever to start automatic vehicle intake.
- ACT-104: select the expiry field and the calendar or other
  comparable addressed fields before committing a verdict.
- ACT-105: apply the binary terminal stamp to the passport and
  return the documents to close the case.
- ACT-922: enter a suspected reason in the matching report category
  independently from the pair tool or verdict.

### System Behaviour Genes

- SYS-137: the comparator resolves a selected case relation and
  exposes a relation result for that pair only.
- SYS-138: after departure the system audits the committed verdict
  against the complete active admissibility requirements.
- SYS-1984: the case also grades the inspection categories. Two
  warranted identical verdicts can earn different grades or pay.

### Constraint Genes

- CON-157: all required current packet checks are conjunctive for
  admission. One expired document makes the observed case ineligible
  despite legitimate fields elsewhere.

### Information Genes

- INF-299: the post-departure audit identifies inspection categories,
  classification and grade/pay state separately from the live folder.

### Objective Genes

- OBJ-370: close this assigned visitor with the warranted admission
  or refusal and reach the independently graded review.

### Time Genes

The records disclose a current date and a clock. This fixed case
does not establish a forced terminal or future intake cutoff.

### Parameters

Visitor packet, current calendar date, comparison settings, validity
fields, open report, category marks, stamp, terminal route, review
classification and payout are scoped parameters.

## Reproducible transitions

| Entry state | Input or event | Expected next state | Evidence |
| --- | --- | --- | --- |
| Prior guided visitor has left | Activate the call lever and approach the next driver | Addressed vehicle and a requestable packet | CP-002 |
| Open folder has a past validity date | Select the invalid expiry and the visible calendar date | Pair comparison can show an explicit mismatch | CP-003–CP-004 |
| Pair relation known while decision is open | Mark a suspected category in the inspection report | A case annotation is visible with no verdict yet | CP-005 |
| Required date check fails | Stamp denial and return paperwork | Vehicle leaves the checkpoint in the refusal direction | CP-003, CP-005 |
| Refused vehicle clears | Read the audit notice or summary | Justified refusal plus separate category/pay evaluation | CP-006–CP-007 |

## Strategic and experiential structure

Comparing a single pair is useful for isolating the decisive date but
does not annotate the inspection report. Entering the case verdict
without understanding every marked field can still produce a justified
refusal. The second witness demonstrates that accurate inspection can
raise the reward for that same decision class.

## Replay and variation

The same second case position has different driver packets in the
two recordings. One expires the permit and one expires the passport,
so compare each document to the current file date. The observation
does not identify the seed or the population of possible variants.

## Adjacent systems and history

Later document sets and incidents are outside this delivery. Crazy
Rocks records post-launch changes to comparison difficulty and audit
detail. A Windows retail product listing or a shared interface alone
does not establish unchanged behaviour across versions.

## Normalised genome

- Action: ACT-008, ACT-072, ACT-104, ACT-105, ACT-922.
- System Behaviour: SYS-137, SYS-138, SYS-1984.
- Constraint: CON-157.
- Information: INF-299.
- Objective: OBJ-370.
- Time: none.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `704` (`GAME-0001`–`GAME-0704`).
- Exact genome matches: none.
- Tied near matches: `GAME-0103` — Papers, Please (`5 / 15 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Papers, Please (GAME-0103)](../m-r/papers-please.md) | ACT-104, ACT-105, CON-157, SYS-137, SYS-138 | Both compare facts before stamping and audit the committed verdict against the current requirements. The scoped Papers, Please shift uses a daily bulletin, intake cutoff and throughput. Contraband Police's single visitor has a separate inspector-authored report and can yield different grades for justified refusals. | Near, `0.333333`. |

## Taxonomy impact

Reuse local navigation, fixture activation, visible fact comparison,
terminal stamping, policy audit and scored report presentation. Admit
an explicit category annotation, one fixed case decision and independent
inspection assessment of a warranted verdict.

## Negative results

- A current permit in W2 does not make the expired passport current.
- W1 reaches a warranted refusal with a visible report error.
- Two different scores from different packets are not a controlled
  estimate of the exact cost of one wrong mark.

## Delta summary

This unit isolates one evaluation comparing records and authority before
a binary decision, then independently grading the report behind it.

## New facts

- The compared expiry field can come from either document.
- The selected comparison and separately entered annotation have
  different outputs.
- A valid refusal admits multiple inspection grades in the observations.

## Principles and design implications

Distinguish the factual check, the inspector's recorded reason and
the final decision. Give the player a case summary that shows which
dimension drove the grade. Vary the documents while preserving one
observable rule.

## Puzzle or game generation potential

Offer a small fictional case packet, a date reference and a selected
field comparator. Ask for a report category and a separate terminal
choice. Verify the difference between a warranted verdict with
accurate grounds and a warranted verdict with an inconsistent report.

## New genes

- ACT-922
- OBJ-370
- SYS-1984

## New combinations

None. None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 451](../../../research/taxonomy-changes/TAXONOMY_CHANGE_451.md).

## New questions

- How do later patches distinguish wrong, absent and extra annotations
  for the same fixed case?
- Can the two expiry variants be produced on demand through normal play?

## Next recommended game

Continue Selection 061 with Kula World on the original European
PlayStation disc. Trace an early key-to-exit route during a face change.

## Why this game

One small case separates comparing evidence, recording an argument,
committing a verdict and receiving a scored judgment.
