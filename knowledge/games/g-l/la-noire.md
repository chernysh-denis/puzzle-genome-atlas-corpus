---
game_id: GAME-0388
slug: la-noire
game_title: L.A. Noire
analysis_status: reviewed
reviewed: 2026-09-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-232
    - ACT-341
    - ACT-528
    - ACT-529
  system:
    - SYS-680
    - SYS-1046
  constraint:
    - CON-692
  information:
    - INF-299
    - INF-393
  objective:
    - OBJ-229
  time:
    - TIM-002
    - TIM-003
---

# Game: L.A. Noire

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Particular clue
names, question counts, street addresses and the five-star maximum are
parameters, not separate genes.

## Analysis scope

- Version / ruleset: the North American English PlayStation 4 release of
  *L.A. Noire* (2017), base-game Traffic case **The Driver's Seat**. The PS4
  manual's Good Cop / Bad Cop / Accuse labels are authoritative here; the
  original PS3/Xbox 360 Truth / Doubt / Lie labels are not substituted.
- Structured analysis target: `GAME-0388` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: inspect the current investigation site for addressed
  objects and persons; examine an item's meaningful face or detail so its
  fact enters the notebook; choose a disclosed lead or interview topic;
  classify the response as credible, doubtful or contradicted by a particular
  recorded clue; follow the next authored lead. After the apartment reveals
  Adrian Black, pursue him in live movement to close the case.
- Entry: begin the first Traffic desk case at the station briefing on the
  abandoned car, before visiting the Pacific Electric Freight Depot. The
  preceding Patrol cases and any accumulated rank are setup, not analysed.
- Positive terminal: apprehend Adrian Black after reaching Frank Morgan's
  apartment, receive the case report and stop before the next case. A
  five-star report is a possible quality grade, not required for completion.
- Negative terminal: the case attempt can fail if Phelps or Bekowsky dies,
  the crime scene is contaminated, Adrian escapes or a required tail loses
  Morgan. A failed interview alone need not end the case; it can force the
  Morgan-tail route rather than direct apartment disclosure.
- Included: freight-depot vehicle/wallet/glasses/pipe clues; the Black-home
  notebook and water-heater clue chain; Nate Wilkey, Margaret Black and Frank
  Morgan interviews; lead selection and travel only as needed between sites;
  alternate Morgan tail if his apartment is not disclosed by questioning;
  final foot pursuit; result categories for clues, questions and conduct.
- Excluded: unrelated street crimes, optional collectibles and suits, all
  later cases, complete city driving simulation, gunfights not required by
  this case, all DLC, VR edition, historical accuracy, exact dialogue script,
  trial-and-error walkthrough use as player knowledge and an assumption that
  all fourteen key clues are mandatory for case completion.
- Reproducible parameterisation: select the North American PS4 edition and
  The Driver's Seat; record each visited site, examined clue and notebook
  entry, chosen interview topic and Good Cop / Bad Cop / Accuse response,
  evidence offered on an accusation, resulting lead, chosen Morgan route,
  chase outcome and final case-report categories. The packet reconstructs
  rules from sources rather than claiming a completed local controller trace.
- Potential scoped modules: a later Traffic case, the Homicide desk,
  optional street crimes, precise real-time chase physics, PS3 interview
  vocabulary and The VR Case Files require separate bounded analyses.
- Direct-play status: none. No PS4 executable, disc, save, controller trace,
  video or audio was inspected. The PS4 publisher manual, official store
  listing and written case/controls guides support this source-bounded
  reconstruction; exact build revision and unobserved optional branches
  remain unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `LAN-001` | The 2017 PS4 edition includes the original case content and presents investigation, suspect interviews and pursuit as its core activity. | Confirmed | Direct | High | P1, P2 |
| `LAN-002` | The Driver's Seat begins from an abandoned car and proceeds through the freight depot, Black residence, bar and Morgan apartment toward Adrian Black. | Observation | Corroborated | High | S1, S2 |
| `LAN-003` | Inspecting an eligible item's relevant detail registers a clue, while the notebook retains clues, persons, objectives and discovered destinations. | Confirmed | Corroborated | High | P2, S1, S2 |
| `LAN-004` | The bloody pipe and the home water-heater assembly form a case-specific physical cross-check; the live-hog receipt is another lead. | Observation | Corroborated | High | S1, S2 |
| `LAN-005` | An interview exposes chosen topics, then accepts Good Cop, Bad Cop or Accuse; a supported accusation requires choosing contradictory recorded evidence. | Confirmed | Direct | High | P2, S1 |
| `LAN-006` | Wrong interview assessments can withhold a positive clue or direct lead without automatically ending the case; Morgan may instead be tailed to his apartment. | Observation | Corroborated | Medium | S1, S2 |
| `LAN-007` | Finding Morgan's apartment leads to Adrian Black and a live foot pursuit that closes the case when he is caught. | Observation | Corroborated | High | S1, S2 |
| `LAN-008` | A completed case reports a one-to-five-star evaluation reflecting found clues, correct interview answers and conduct damage or injuries. | Confirmed | Direct | High | S1, S3 |
| `LAN-009` | Death, escape, contaminated scene or a lost required tail can fail the current attempt. | Observation | Limited | Medium | S1 |
| `LAN-010` | Investigation and interview decisions permit deliberation while a chase resolves with live movement and possible escape. | Observation | Corroborated | High | P2, S1, S2 |
| `LAN-011` | No PS4 build or direct play was inspected; written routes do not prove exact controller timing or every alternate branch. | Observation | Direct | High | R1 |

## Basic data

- Release / origin: the original L.A. Noire appeared in 2011; this packet
  selects Rockstar's North American PS4 edition released 2017-11-14. The
  PlayStation listing identifies the included original game and DLC; only
  one base-game Traffic case enters the genome.
- Platform or physical form: one-player PS4 application with embodied crime
  scene exploration, a persistent case notebook, authored interview choices
  and a short final pursuit. The structured analysis target records edition
  and evidentiary limits.
- Puzzle family: `FAM-002` hidden-state inference and `FAM-012` knowledge and
  evidence progression; the player infers the staged disappearance from
  observations and tests interview responses against retained facts.
- Primary sources, checked 2026-09-24:
  - **[P1]** [PlayStation's North American PS4 product
    listing](https://store.playstation.com/en-us/product/UP1004-CUSA09084_00-LANOIRE000000PS4),
    edition, date, included content and investigation/interview premise.
  - **[P2]** [Rockstar's PS4 English instruction
    manual](https://media.rockstargames.com/rockstargames-newsite/img/manuals/en_us/LAN_PS4_DIGITAL_MANUAL_ENG.pdf),
    case notebook, clue inspection and exact PS4 interrogation labels and
    evidence-selection rule. The publisher PDF was checked through its
    indexed text; physical controller execution was not observed.
- Reproducible corroboration:
  - **[S1]** [Prima's 2017 remaster guide, The Driver's
    Seat](https://primagames.com/eguides/la-noire-2017-remaster/walkthrough/the-traffic-cases/case-at001-the-drivers-seat),
    case itinerary, clue placement, interviews, failure list, alternative
    Morgan route and terminal pursuit.
  - **[S2]** [Neoseeker's The Driver's Seat written
    route](https://www.neoseeker.com/la-noire/walkthrough/The_Driver%27s_Seat),
    independent route corroboration. The current web fetch returned 403;
    search-index snippets were usable only for the broad case itinerary and
    tail/chase, not precise answer text.
  - **[S3]** [Prima's case-report rules](https://primagames.com/eguides/la-noire-2017-remaster/basics/the-case-report),
    report grade and categories.
  - **[R1]** this source and play-status audit.
- Claim IDs: `LAN-001`–`LAN-011`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — walk between inspectable objects and pursue Adrian in the
  bounded final chase. Citywide driving is not decomposed separately.
- `ACT-341` — address a case-local fixture or actor: examine the vehicle and
  later assemble the water-heater pipes, speak to a witness or activate a
  phone lead. These are world-object interactions, not free text entry.
- `ACT-528` — rotate or focus a held item so an informative detail such as a
  name, receipt or hidden message becomes a registered clue. Mere picking up
  an uninformative prop does not count.
- `ACT-232` — choose one offered interview topic and its response stance.
  This reuses consequential authored dialogue, with Good Cop / Bad Cop /
  Accuse as this version's available response domain.
- `ACT-529` — after choosing Accuse, select one current notebook clue as
  the alleged contradiction to that interview answer.
- Parameters: evidence object, detail orientation, question roster,
  credibility stance, selected proof item, site, witness and response.
- Claim IDs: `LAN-002`–`LAN-007`, `LAN-010`.

### System Behaviour Genes

- `SYS-680` — register a meaningful inspected clue and advance the authored
  notebook trail or location availability, as with the wallet address,
  matchbook and water-heater pipe relationship. It does not infer every fact
  automatically from mere proximity.
- `SYS-1046` — evaluate the selected interview stance and, when Accuse is
  chosen, its supplied proof against the authored response. A supported
  judgement releases the appropriate answer or lead; an unsupported one
  can withhold it and alter the route without erasing the whole case.
- Resolution order: examine detail → register available fact/lead → ask
  question → assess answer → validate optional proof → disclose or withhold
  authored lead → choose next available destination.
- Parameters: case clue set, answer truth status, chosen stance, accepted
  evidence mapping, lead disclosure and fallback route.
- Claim IDs: `LAN-003`–`LAN-006`.

### Constraint Genes

- `CON-692` — a positive Accuse resolution requires a recorded clue that
  contradicts the specific answer. Suspicion from expression alone may
  justify Bad Cop but is not proof for Accuse. The player can back out before
  committing an evidence item; a wrong submitted item loses the positive
  answer opportunity rather than consuming Phoenix Wright court marks.
- Scarce strategic resources: no finite objection-token budget is evidenced
  for this case. Rank or intuition points are outside this packet.
- Claim IDs: `LAN-005`, `LAN-006`.

### Information Genes

- `INF-393` — the notebook exposes registered clues, persons of interest,
  current objectives, available destinations and interview questions. Its
  entries grow at authored discovery points; they are not an omniscient
  suspect solution or Phoenix Wright's line-addressed Court Record.
- `INF-299` — the terminal case report exposes found-clue and question
  performance plus conduct costs and aggregate star grade.
- An investigation-music cue may indicate local search completeness, but it
  is not treated as proof that every case question was answered correctly.
- Claim IDs: `LAN-003`, `LAN-008`.

### Objective Genes

- `OBJ-229` — follow sufficient clues and leads to Morgan's apartment,
  apprehend the located Adrian Black and settle one authored investigation
  into a case report. Optional five-star optimization is distinct from
  completing the case.
- Success, evaluation and failure: successful capture completes the case;
  missing clues or wrong answers degrade evaluation, while death, escape,
  contaminated scene or a failed required tail can end an attempt.
- Claim IDs: `LAN-002`, `LAN-006`–`LAN-009`.

### Time Genes

- `TIM-002` — self-paced search, notebook reading and interview choices.
- `TIM-003` — the final chase, and the fallback tail when invoked, continue
  in real time while the player moves and can lose the target.
- Claim IDs: `LAN-007`, `LAN-009`, `LAN-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Depot car identified; wallet and glasses unrecorded | Examine wallet identity, then rotate glasses to the informative mark | Black's address and the glasses fact enter the notebook | Detail-level inspection, not proximity, registers a clue | `LAN-003` |
| Bloody pipe recorded; Black-home heater incomplete | Inspect flyer and place the loose pipe sections | The missing fitting can be related to the depot pipe | A physical fixture creates a corroborating authored inference | `LAN-004` |
| Wilkey gives a topic answer without contradicting proof | Choose Bad Cop on the defensive wallet answer | A new admission can be disclosed without an evidence-item accusation | Suspicion and proof are separate interview routes | `LAN-005` |
| Interview answer contradicted by a discovered clue | Choose Accuse and submit the matching notebook evidence | The case's authored positive response and next lead become available | Proof selection is addressed to a particular answer | `LAN-005`, `LAN-006` |
| Morgan does not disclose the apartment | Follow him without losing or alerting him | The apartment route remains reachable through tailing | One wrong interview need not end the case | `LAN-006` |
| Adrian is found at the apartment | Pursue and catch him before escape | Case closes and displays its report | Live chase is the terminal action, not five-star perfection | `LAN-007`–`LAN-009` |

## Strategic and experiential structure

- Local decision: distinguish meaningful from decorative objects; use the
  notebook to test an answer rather than guessing from facial expression
  alone.
- Medium-term planning: collect the car and house clue chain before key
  interviews; follow the bar or fallback tail lead to the apartment.
- Long-term structure: the case settles into a graded report and the next
  authored case; this packet stops at the report.
- Common heuristics: inspect all responsive object faces, cross-check an
  interview topic against recorded facts, reserve Accuse for a specific
  contradiction and limit driving damage if pursuing a higher report grade.
- Failure attribution: the report distinguishes clue/question performance
  from conduct; a failed tail or escape is an attempt failure, not simply a
  low star count.
- Player-trust factors: a recorded clue and its notebook text make positive
  accusations inspectable. The authored case can continue after a mistaken
  answer, so the interface should not be described as a fully branching
  free-form investigation.
- Claim IDs: `LAN-003`–`LAN-010`.

## Replay and variation

- What changes between sessions: the player's discovery order, interview
  accuracy, choice of direct versus tail route and final conduct grade.
- Randomness or procedural generation: none established for the scoped
  case's authored clues, answers or terminal.
- Multiple viable strategies: the accepted Morgan interview and the fallback
  tail can both reach the apartment; higher case grade asks for more complete
  investigation and cleaner conduct.
- Typical replay motive: improve the case report or inspect missed leads.
- Claim IDs: `LAN-002`, `LAN-006`–`LAN-008`.

## Adjacent systems and history

- Direct predecessors: the original 2011 L.A. Noire uses older interrogation
  label names; their mapping is not an independent PS4 gene.
- Variants: PS3/Xbox 360 originals, Switch, PC and VR are not this exact
  analysis target.
- Similar games: Phoenix Wright addresses testimony *lines* in court with a
  finite objection allowance; this case inspects embodied crime-scene
  evidence and grades interview credibility before a live pursuit. Return of
  the Obra Dinn asks the player to complete a structured fate ledger, not
  conduct staged witness questioning.
- Important differences: no universal five-mark objection budget, court
  verdict or frozen death tableau is transferred into L.A. Noire.
- Claim IDs: `LAN-001`–`LAN-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-008, ACT-232, ACT-341, ACT-528, ACT-529 | movement, authored responses, fixture contact, clue focus, accusation evidence |
| System Behaviour | SYS-680, SYS-1046 | authored clue progression and interview evaluation |
| Constraint | CON-692 | matching proof for Accuse |
| Information | INF-299, INF-393 | report and growing case notebook |
| Objective | OBJ-229 | Adrian capture and case settlement |
| Time | TIM-002, TIM-003 | self-paced investigation, live pursuit |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `387` (`GAME-0001`–`GAME-0387`).
- Exact genome matches: none.
- Tied near matches: `GAME-0252` — Detroit: Become Human (`5 / 25 = 0.200000`).
- Supported combination subsets: none.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0252` Detroit: Become Human | `ACT-008`, `ACT-232`, `ACT-341`, `SYS-680` and `TIM-003` share embodied investigation, authored responses, clue-led progress and live resolution. | Detroit's opening hostage incident chooses interventions in a live negotiation and retains a branch endpoint for a protected child. L.A. Noire's first Traffic case demands close inspection of physical objects, answer-specific proof from a notebook and apprehension after a chase; its terminal report grades investigative completeness and conduct. Neither objective, evidence interface nor response adjudication transfers. | `5 / 25 = 0.200000`; tied near maximum, not an equivalent investigation loop |

### Preserved research notes

- New genes: `ACT-528`, `ACT-529`, `SYS-1046`, `CON-692`, `INF-393`,
  `OBJ-229`.
- Reused genes: `ACT-008`, `ACT-232`, `ACT-341`, `SYS-680`, `INF-299`,
  `TIM-002`, `TIM-003`.
- Classification result: six source-bounded detective-case distinctions.
- Evidence and reasoning: the reusable pieces cover movement, consequential
  conversation, clue-to-lead progression and a graded report. The new pieces
  isolate manipulable physical evidence, an answer-addressed accusation,
  its proof condition, notebook disclosure and this case's terminal.

## Taxonomy impact

- Registry changes: six additive Active genes.
- Taxonomy-change record: `TAXONOMY_CHANGE_127`.
- Candidate terms affected: physical clue examination, interview accusation
  and case notebook versus courtroom evidence challenge.

## Negative results

- Do not infer that a wrong interview answer or a missed optional clue ends
  the case; the written route documents a Morgan-tail fallback.
- Do not convert the one-to-five-star quality grade into the binary completion
  goal, or assume that every later case shares this exact clue count.
- Do not mix PS3-era Truth / Doubt / Lie wording into the PS4 target or treat
  the publisher's period fiction as historical evidence.

## Delta summary

## New facts

- [Confirmed | Direct | High] The PS4 manual uses Good Cop, Bad Cop and
  Accuse, with recorded evidence required to sustain an accusation
  (`LAN-003`, `LAN-005`).
- [Observation | Corroborated | High] The first Traffic case couples object
  inspection, interview leads and a final live chase before its graded
  report (`LAN-002`–`LAN-008`).

## New genes

- [Observation | Corroborated | Medium] `ACT-528`, `ACT-529`, `SYS-1046`,
  `CON-692`, `INF-393` and `OBJ-229` distinguish the scoped detective case.

## New combinations

- [Observation | Corroborated | High] No verified combination is registered.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_127` adds the six
  source-bounded genes without revising older signatures.

## New questions

- Which optional dialogue misjudgements change only a report grade and which
  force a different site route? Direct PS4 branch tracing could verify every
  transition without relying on guide wording.
- What exact case-report weights are assigned to each missing clue, wrong
  answer and conduct category? The aggregate grade is documented, but its
  hidden coefficients are not in scope.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0389 Mega Man 2.
- Optimisation criterion: alternate authored interview inference with a
  side-view action stage and explicit boss-selection boundary.
- Expected information gain: stage hazard, weapon and boss interaction
  mechanics distinct from evidence-led investigation.
- Backlog impact: preserves the selected nine-game order; the next game is
  not started in this commit.

## Why this game

- [Hypothesis | Limited | Medium] An embodied investigation and interview
  proof rule tests a different decision structure from the previous grid
  bomb stage while adding a recognizable PlayStation case to the catalogue.
