---
game_id: GAME-0103
slug: papers-please
game_title: Papers, Please
analysis_status: reviewed
reviewed: 2026-08-15
combination_ids:
  - COMB-0103
gene_ids:
  action:
    - ACT-104
    - ACT-105
  system:
    - SYS-137
    - SYS-138
  constraint:
    - CON-157
  information:
    - INF-001
    - INF-053
  objective:
    - OBJ-050
  time:
    - TIM-014
---

# Game: Papers, Please

## Analysis scope

- Version / ruleset: original desktop story mode, bounded to Day 4
  (26 November 1982) and its scripted third entrant.
- Included: the pre-shift bulletin and persistent rulebook; a foreign entrant
  with a current passport and a same-day entry ticket but no entry permit;
  visible document fields; inspection mode; selecting the empty permit area
  and current foreigner rule; discrepancy feedback; interrogation; `APPROVED`
  and `DENIED` passport stamps; delayed citation adjudication; the 6am-6pm
  shift clock and minimum-scripted-entrant exception.
- Excluded: other Day 4 entrants, fingerprint resolution, token decisions,
  detainment, searches, body scans, forged seals, confiscation, EZIC, family
  budgeting, later policy layers, endings, endless mode and mobile controls.
- Direct-play status: not conducted because no licensed executable is present
  in the workspace. The official product page and Lucas Pope's development
  logs establish the core inspection, stamping and timed-case loop; the Day 4
  record independently fixes the entrant and rule change. The executable
  control models that bounded state rather than the production random fields.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PPL-001` | The player classifies entrants from their documents and Ministry inspection references | Confirmed | Corroborated | High | P1, P2, S1 |
| `PPL-002` | Inspect mode relates two exposed facts as matching, discrepant or unrelated and may enable interrogation | Confirmed | Corroborated | High | P2, P3, S2 |
| `PPL-003` | Day 4 replaces foreign entry tickets with entry permits and requires Arstotzkan identity cards | Confirmed | Corroborated | High | S2, S3 |
| `PPL-004` | The scripted third Day 4 entrant has an obsolete ticket but lacks the now-required permit and must be denied | Confirmed | Corroborated | High | S2, V1 |
| `PPL-005` | A committed incorrect verdict produces a delayed citation after the entrant leaves | Confirmed | Corroborated | High | S1, S3 |
| `PPL-006` | The shift clock gates new paid cases while an open or required scripted case may finish after cutoff | Confirmed | Direct | High | P4, S3, V1 |

## Basic data

- Release / origin: designed and developed by Lucas Pope; published by 3909 on
  8 August 2013.
- Platform or physical form: single-player desktop document-inspection game;
  later official mobile versions adapt the same rule loop.
- Puzzle family: rule-changing document adjudication under throughput pressure.
- Primary sources:
  - **[P1]** [Official Papers, Please site](https://papersplea.se/), for the
    creator-controlled release, platforms and official product destination.
  - **[P2]** [Lucas Pope development log: inspect mode and forgeries](https://dukope.com/devlogs/papers-please/tig-01/),
    for two-fact highlighting, missing-document comparison and document seals.
  - **[P3]** [Lucas Pope mobile-interface development log](https://dukope.com/devlogs/papers-please/mobile/),
    for the desktop document desk, stamp bar, inspect-mode sequence, bulletin,
    transcript and rulebook roles.
  - **[P4]** [Lucas Pope development log: day quota](https://dukope.com/devlogs/papers-please/tig-03/),
    for clock expiry, completing the current or minimum scripted entrants and
    post-cutoff pay behaviour.
- Secondary sources:
  - **[S1]** [Official Steam product page](https://store.steampowered.com/app/239030/),
    for release metadata and the inspect/search/fingerprint decision premise.
  - **[S2]** [Day 4 rules and scripted entrants](https://papersplease.fandom.com/wiki/Day_4),
    for the date, policy swap and third entrant's obsolete ticket.
  - **[S3]** [Gameplay overview](https://en.wikipedia.org/wiki/Papers%2C_Please),
    for daily rule changes, verdict stamps, citations, limited shift time and pay.
  - **[V1]** [`verify_papers_please_day4.py`](../../../scripts/verify_papers_please_day4.py),
    an independent executable control for the bounded packet.

## Mechanical decomposition

### Action Genes

- `ACT-104` — cross-reference two visible case facts. The control selects the
  empty permit area and the Day 4 foreigner-entry-permit rule.
- `ACT-105` — stamp one case with a terminal binary verdict. The passport
  receives exactly one accepting or denying classification for this packet.

### System Behaviour Genes

- `SYS-137` — adjudicate a selected fact pair as matching, discrepant or
  unrelated. The missing permit comparison exposes a discrepancy and the
  interrogation affordance.
- `SYS-138` — audit the committed case verdict against the complete active
  policy. Approval produces a citation; denial does not.
- Resolution order: expose documents and statements; accept fact-pair
  selection; report its relation; accept a stamp; return the case; compare the
  verdict with the full Day 4 policy; issue any citation; admit the next case
  if the clock or scripted minimum permits it.

### Constraint Genes

- `CON-157` — current-day policy jointly defines case admissibility. Day 4
  replaces the Day 3 ticket predicate with a permit predicate for foreigners.
- The control's other predicates are parameters: passport present and current,
  entrant not wanted, foreign permit required and Arstotzkan identity card
  required only for citizens.

### Information Genes

- `INF-001` — fully visible current state. The scoped passport, obsolete ticket,
  absent permit area, bulletin, rule reference, date and current clock are
  inspectable before the verdict.
- `INF-053` — visible current-day policy with persistent reference detail. The
  bulletin announces the changed document requirements while the rulebook
  remains available for exact comparisons.

### Objective Genes

- `OBJ-050` — maximise correctly processed cases within a work shift. A correct
  processed entrant contributes pay; throughput competes with checking effort
  and protocol errors incur citations.

### Time Genes

- `TIM-014` — real-time shift gates admission of new cases. The clock advances
  from 6am to 6pm but the current or required scripted case can finish after
  cutoff rather than failing instantly.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Control foreigner has current passport and same-day ticket | Evaluate under Day 3 rules | No violation; ticket satisfies the foreign-document predicate | day-relative policy | `PPL-003`, `PPL-004` |
| Same fixed packet on Day 4 has no entry permit | Evaluate the active conjunction | Exactly one violation: missing entry permit | policy replacement, not parameter drift | `PPL-003`, `PPL-004` |
| Day 4 missing-permit state | Highlight empty permit area plus foreigner-permit rule | `Discrepancy detected`; interrogation becomes available | fact-pair adjudication | `PPL-002`, `PPL-004` |
| Same state | Highlight passport expiry plus inspection date | `Matching data` | valid fields do not inherit another discrepancy | `PPL-002` |
| Missing permit remains unresolved | Stamp `DENIED` and return the case | Verdict matches full policy; no citation | complete-case audit | `PPL-005` |
| Missing permit remains unresolved | Stamp `APPROVED` and return the case | Verdict conflicts with policy; citation follows | errors are delayed beyond pair feedback | `PPL-005` |
| Clock reaches 6pm with required entrants processed | Attempt to call next entrant | No new ordinary case enters; an already open case may finish | shift gate is not terminal expiry | `PPL-006` |

## Strategic and experiential structure

- Local decision: choose the cheapest reliable comparison that can establish a
  disqualifying discrepancy, then commit the correct stamp.
- Medium-term planning: arrange bulletin, rulebook and documents so common
  fields can be checked quickly without forgetting a newly introduced rule.
- Long-term structure: policy changes between days expand and replace checks;
  memorisation saves time but stale memorisation causes citations.
- Common heuristics: read the bulletin before calling the first entrant; check
  document presence first; stop after one unresolved disqualifying discrepancy;
  keep the clock visible; return every document after stamping.
- Failure attribution: pair feedback identifies a selected discrepancy, while
  a citation proves the terminal verdict violated some active predicate.
- Player-trust factors: daily amendments, reference data and citation reasons
  must apply consistently to the exact policy snapshot used for the verdict.

## Replay and variation

- The scoped third entrant's decisive missing-permit state is scripted, while
  incidental passport identity fields may vary and remain outside the control.
- Different inspection orders change elapsed time, not the correct verdict.
- Across the full story, daily rules, scripted people and procedurally generated
  entrants change; those later systems are not inferred into this packet.

## Adjacent systems and history

- The Password Game also uses multiple simultaneous predicates, but its rules
  accumulate during one editable answer. Papers, Please snapshots one day's
  policy across many terminal cases and can replace a predicate at day change.
- Hexcells Infinite immediately adjudicates one asserted cell class. Here a
  highlighted pair only exposes evidence; a separate stamp commits the case,
  and full-policy audit is delayed until the entrant leaves.
- The Case of the Golden Idol supports static evidence inspection, but asks for
  one structured historical reconstruction without a paid shift or changing
  government policy.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-104`, `ACT-105` | fact classes; stamp alignment |
| System Behaviour | `SYS-137`, `SYS-138` | relation text; citation delay |
| Constraint | `CON-157` | Day 4 policy conjunction |
| Information | `INF-001`, `INF-053` | bulletin layout; rulebook tabs |
| Objective | `OBJ-050` | credits and penalties |
| Time | `TIM-014` | shift cutoff; scripted minimum |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `102` (`GAME-0001`–`GAME-0102`).
- Exact genome matches: none.
- Tied near matches: `GAME-0064` — SET (`1 / 13 = 0.076923`).
- Supported combination subsets: `COMB-0103`.
- Scan date: 2026-08-15.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0064`.

### Preserved research notes

- New genes: `ACT-104`, `ACT-105`, `SYS-137`, `SYS-138`, `CON-157`,
  `INF-053`, `OBJ-050`, `TIM-014`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: the corpus lacked an explicit two-fact inspection
  query, a diegetic terminal case stamp, delayed full-policy citation, a
  replaceable day policy, visible amendments, correct-case throughput and a
  nonterminal work-shift cutoff. Fully visible current state transfers.

## Taxonomy impact

- Registry changes: eight Active IDs and one transfer to a new game.
- Taxonomy-change record: none; no earlier boundary is merged or retired.
- Candidate terms affected: new boundaries recorded in `CANDIDATE_TERMS.md`.

## Negative results

- `SYS-089` rejected: inspection feedback does not immediately classify one
  concealed cell and a wrong stamp is audited only after case completion.
- `CON-156` rejected: Day 4 rules govern many separate cases and may replace a
  Day 3 rule; they do not grow over one mutable answer.
- `TIM-003` rejected: the current document packet does not mutate in real time;
  the clock gates future entrants and pay rather than forcing live-state motion.
- `CON-068` rejected: 6pm does not make the current case a terminal failure.
