---
game_id: GAME-0385
slug: phoenix-wright-ace-attorney
game_title: 'Phoenix Wright: Ace Attorney'
analysis_status: reviewed
reviewed: 2026-09-24
combination_ids: []
gene_ids:
  action:
    - ACT-232
    - ACT-526
    - ACT-527
  system:
    - SYS-1041
  constraint:
    - CON-690
  information:
    - INF-391
    - INF-392
  objective:
    - OBJ-227
  time:
    - TIM-002
---

# Game: Phoenix Wright: Ace Attorney

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Witness names,
statement order, evidence item names and the five-mark allowance are scoped
parameters, not independent genes.

## Analysis scope

- Version / ruleset: original North American English Nintendo DS Game Card
  released in 2005. This is a source-bounded reconstruction, not a recorded
  cartridge run or a claim about later Trilogy or mobile assistance modes.
- Structured analysis target: the first case, The First Turnabout, on the
  original DS release; see `GAME-0385` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Setup: begin a fresh first case with Phoenix defending Larry Butz. The
  introductory lobby and judge's case questions supply the initial court
  context. The case has a courtroom trial but no player-directed crime-scene
  Investigation Phase before its verdict.
- Primary decision loop: read the currently addressable line of Frank
  Sahwit's authored testimony; inspect the current Court Record and press a
  statement for elaboration or present one evidence item against that exact
  line. A supported contradiction advances the authored testimony and may
  expose a revised account or a new item; an irrelevant presentation spends a
  finite court allowance. At prompted turning points choose an offered
  explanation or present the relevant record, then continue until verdict.
- Entry: start The First Turnabout from a fresh first-case selection, before
  the lobby and trial tutorial. The case-opening depiction of the culprit is
  given information, not a player action or a hidden killer to discover.
- Positive terminal: complete the first case's required contradictions and
  follow-up explanations so the court declares Larry not guilty. The packet
  stops at the verdict; the later lobby conversation and case two are out of
  scope.
- Negative terminal: make enough penalised wrong court challenges or answers
  to exhaust the five visible marks, causing a guilty verdict and game over.
  A reload is a separate attempt. Pressing a statement itself is not treated
  as a universal penalty-free rule for every later case.
- Included: fixed opening testimony and case questions; Court Record evidence
  and profiles, including the autopsy report, blackout record, statue-clock
  and passport as they become available; backward/forward line review;
  statement-specific pressing and evidence presentation; authored revisions
  and follow-up questions; finite wrong-objection allowance and first-case
  acquittal.
- Excluded: later cases and their Investigation Phases, searching a scene for
  evidence, fifth-case forensic touch/microphone mechanics, legal realism,
  optional flavour as a separate solution path, voice input as a required
  command, adaptive testimony generation, deduction of a concealed culprit,
  walkthrough use by the player and exact script quotation.
- Reproducible parameterisation: identify the original North American English
  DS Game Card and save, begin the first case, record each addressed statement,
  current Court Record item, press/present/choice input, testimony revision,
  visible penalty marks and verdict. The source-based packet describes rule
  transitions, not a completed local play trace.
- Potential scoped modules: the investigation-led second case, later multi-day
  trials, the DS-exclusive Rise from the Ashes forensic case, and remaster
  assistance or episode selection each require their own bounded analysis.
- Direct-play status: none. The official Nintendo product page, Capcom's
  creator interview and contemporary first-case review/walkthrough were read
  as text. No cartridge, licensed executable, save, controller trace,
  screenshot, video or audio was inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PWA-001` | The original DS title has five cases and divides general play into Investigation and Court phases, but the opening Larry Butz case is a short courtroom tutorial | Confirmed | Corroborated | High | P1, P2, S1, S2 |
| `PWA-002` | The first case opens with the culprit depicted, then tests how to expose an authored account rather than asking the player to identify an unknown killer | Confirmed | Corroborated | High | P2, S1, S2 |
| `PWA-003` | Court Record items and profiles remain inspectable and new items are added by scripted trial events, including the autopsy, blackout, statue-clock and passport | Observation | Corroborated | High | S1, S2 |
| `PWA-004` | A witness finishes an authored testimony before the player addresses and revisits its individual statements for cross-examination | Confirmed | Corroborated | High | S1, S2 |
| `PWA-005` | Pressing an addressed statement asks for elaboration; presenting one Court Record item against an addressed statement submits a contradiction claim | Confirmed | Corroborated | High | S1, S2 |
| `PWA-006` | A valid statement/item pairing and prompted explanation move the first case through revised testimonies and finally to an acquittal | Observation | Corroborated | High | S1, S2 |
| `PWA-007` | An incorrect presentation removes one of five visible marks; exhaustion produces a guilty verdict and a new attempt must reload | Confirmed | Corroborated | High | S1, S2 |
| `PWA-008` | The original first case has no player-driven pre-trial scene investigation, and the DS microphone is optional rather than required for courtroom commands | Confirmed | Corroborated | High | S1, S2 |
| `PWA-009` | No original cartridge execution, exact build revision or measured input trace was observed | Observation | Direct | High | R1 |

## Basic data

- Release / origin: Capcom's original English DS release reached North
  America in October 2005; the Nintendo UK listing gives the European DS
  release as 2006-03-31. This packet selects the original North American
  English ruleset, not both regional builds.
- Platform or physical form: Nintendo DS Game Card, single-player court
  dialogue and evidence interface. The structured target records the precise
  edition; no availability or direct ownership is asserted.
- Puzzle family: `FAM-002` hidden-state inference and `FAM-012` knowledge and
  evidence progression. The player's core task is to expose a contradiction
  with already supplied case facts, not to solve a physical board.
- Primary sources, checked 2026-09-24:
  - **[P1]** [Nintendo UK's original DS product
    description](https://www.nintendo.com/en-gb/Games/Nintendo-DS/Phoenix-Wright-Ace-Attorney-272222.html),
    identifying the five-case release, phase structure, testimony/evidence
    premise, developer and European date.
  - **[P2]** [Capcom's interview with series creator Shu Takumi](https://news.capcomusa.com/lets/browse/the-early-days-of-ace-attorney),
    explaining that the short The First Turnabout was written to introduce
    contradiction-finding and intentionally shows its culprit.
- Contemporary and reproducible corroboration:
  - **[S1]** [GameSpot's 2005 original-DS
    review](https://www.gamespot.com/reviews/phoenix-wright-ace-attorney-review/1900-6135422/),
    directly describing line selection, press/present, automatic evidence
    acquisition, five wrong-objection marks, guilty game over and the opening
    courtroom-only tutorial.
  - **[S2]** [contemporary original-DS first-case written
    route](https://gamefaqs.gamespot.com/ds/925589-phoenix-wright-ace-attorney/faqs/47084),
    for the initial Court Record and the autopsy → blackout → statue-clock →
    passport sequence and the Larry verdict. Its text is a reproducibility
    guide, not evidence that this analyst played the cartridge.
- **[R1]** Local environment statement: no executable or audiovisual source
  was opened; no quantitative timing or hidden judge rule was measured.
- Claim IDs: `PWA-001`–`PWA-009`.

## Mechanical decomposition

### Action Genes

- `ACT-526` — press one addressed witness statement for elaboration. The
  current line is selected before the request, so this is not generic NPC
  conversation or a contradiction submission.
- `ACT-527` — present one current Court Record item against the exact
  testimony line. The player submits an evidence-to-claim challenge, not a
  whole-case verdict and not `ACT-104`'s two-highlight discrepancy tool.
- `ACT-232` — choose a consequential offered court explanation or answer at
  authored branch prompts, including why the clock matters.
- Parameters: witness, statement index, available record, selected item and
  offered response set. Advancing uncommitted text is interface navigation,
  not a separate strategic gene.
- Claim IDs: `PWA-003`–`PWA-006`.

### System Behaviour Genes

- `SYS-1041` — resolve a supported contradiction into the next authored
  testimony or question and add/replace relevant case evidence when the
  script specifies it. This is not free-form language generation or automatic
  acceptance of any semantically similar argument.
- Resolution order: select statement; optionally press for fixed detail;
  inspect the current record; present item or choose prompted response; check
  the authored pairing; advance/revise on success or apply the finite court
  penalty on a penalised error; check verdict terminal.
- Parameters: authored transition table, testimony version, case-record
  contents, response gate and verdict state.
- Claim IDs: `PWA-003`–`PWA-007`.

### Constraint Genes

- `CON-690` — finitely many penalised unsupported objections/answers can
  exhaust the defense's visible allowance and force a guilty game over. The
  five marks are a first-game parameter; not every line press spends one.
- Scarce strategic resource: remaining court challenge marks. Save/reload
  belongs to a new attempt, not a free undo within this packet.
- Claim IDs: `PWA-007`.

### Information Genes

- `INF-391` — the Court Record exposes a revisitable, case-local set of
  evidence descriptions and participant profiles which scripted events may
  add or revise. It is not Obra Dinn's immutable scene-indexed tableau.
- `INF-392` — one authored witness's testimony is presented as individually
  addressable, revisitable statement lines during cross-examination; it may
  be replaced after an accepted contradiction.
- The introductory culprit depiction is a fixed narrative disclosure. It
  does not add a hidden-killer deduction gene to this first-case genome.
- Claim IDs: `PWA-002`–`PWA-006`.

### Objective Genes

- `OBJ-227` — expose the first case's authored contradictions and required
  explanations until the court declares the defendant not guilty. Merely
  knowing the culprit, losing every mark, or selecting a later episode does
  not satisfy it.
- Success, evaluation and failure: an acquittal is the positive case terminal;
  mark exhaustion yields guilty/game over. The local terminal does not score
  real-world legal persuasiveness.
- Claim IDs: `PWA-002`, `PWA-006`, `PWA-007`.

### Time Genes

- `TIM-002` — the text and courtroom choices are self-paced. The case has
  fictional dates and times but no deadline that expires while the player
  reads a testimony line or Court Record item.
- Claim IDs: `PWA-004`, `PWA-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh first-case courtroom context | Inspect initial Court Record and answer case questions | Autopsy and profile details support the correct victim/cause responses; the court moves to witness testimony | Supplied record precedes cross-examination | `PWA-003`, `PWA-004` |
| Sahwit claims the 1:00 discovery time | Present the autopsy report at that addressed line | A conflict with the recorded later death window forces a revised time account | Evidence must be paired with a statement | `PWA-005`, `PWA-006` |
| Revised account claims a television supplied the time | Present the blackout record against the television line | The impossible powered television is rejected and another account opens | An accepted contradiction replaces authored testimony | `PWA-003`, `PWA-006` |
| A new account treats the murder object as a clock | Press for detail, then present the statue-clock at its addressed line | The script reveals the object's spoken-clock function and opens a follow-up explanation | Press, present and branch choice are distinct operations | `PWA-005`, `PWA-006` |
| Final clock-time discrepancy remains | Give the required explanation and present the victim's passport | The time-zone relation supports the final challenge and the court acquits Larry | Correct chain reaches the local verdict | `PWA-006` |
| Any addressed line with a penalised irrelevant item | Present that item repeatedly across failures | Each wrong challenge removes one mark; exhausting all five yields guilty/game over | Error budget is finite, not a free brute-force search | `PWA-007` |

## Strategic and experiential structure

- Local decision: distinguish a real contradiction from a merely suspicious
  statement, then choose whether to request detail or risk a penalised item.
- Medium-term planning: keep the sequence of autopsy, blackout, clock and
  passport facts available as testimony changes.
- Long-term structure: the authored testimony sequence converges on one
  first-case acquittal; future cases are outside the packet.
- Common heuristic: press unclear statements for context and compare the
  newly exposed claim with the current Court Record before presenting.
- Failure attribution: a wrong presentation spends a visible mark, but the
  scripted story may still prompt a narrow answer; the game is not a general
  logic-proof checker.
- Player-trust factors: the case record and challenge allowance are visible,
  while the exact accepted item/line pair is authored rather than inferred
  semantically by the engine.
- Claim IDs: `PWA-003`–`PWA-008`.

## Replay and variation

- What changes between attempts: the player's chosen presses, challenged
  statement/item pairs and remaining marks. The case testimony and required
  evidence are authored, not randomised.
- Multiple viable strategies: optional presses and some answer detours can
  differ, but this packet claims no alternative successful verdict path.
- Typical replay motive: retry after guilty or revisit the narrative, not
  generate another culprit or court record.
- Claim IDs: `PWA-002`–`PWA-008`.

## Adjacent systems and history

- Nintendo's general product description mentions Investigation and Court
  phases. The first episode is an exception: a trial tutorial with supplied
  evidence, so later scene-search genes must not be imported here.
- Papers, Please asks the player to compare two highlighted case facts and
  commit a binary stamp; Phoenix instead presses or challenges an authored
  testimony line and receives a judge-issued verdict.
- Return of the Obra Dinn uses revisitable spatial memories and structured
  fate hypotheses; the first Ace Attorney case advances an authored courtroom
  script by addressed evidence challenges.
- Claim IDs: `PWA-001`–`PWA-008`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-232, ACT-526, ACT-527 | court responses, press and present |
| System Behaviour | SYS-1041 | authored testimony transitions |
| Constraint | CON-690 | five-mark challenge allowance |
| Information | INF-391, INF-392 | Court Record and addressable testimony |
| Objective | OBJ-227 | first-case acquittal |
| Time | TIM-002 | self-paced dialogue |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `384` (`GAME-0001`–`GAME-0384`).
- Exact genome matches: none.
- Tied near matches: `GAME-0343` — The Secret of Monkey Island (`2 / 22 = 0.090909`).
- Supported combination subsets: none.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0343` The Secret of Monkey Island | `ACT-232` consequential authored response and `TIM-002` self-paced decision | Monkey Island uses dialogue choices within a navigable prop-and-quest sequence; Phoenix addresses individual testimony lines with available case evidence and risks a finite objection allowance before a judge-issued acquittal. Neither the trial's evidence record nor its contradiction transition transfers. | `2 / 22 = 0.090909`; tied near maximum, not an equivalent conversation puzzle |

### Preserved research notes

- New genes: `ACT-526`, `ACT-527`, `SYS-1041`, `CON-690`, `INF-391`,
  `INF-392`, `OBJ-227`.
- Reused genes: `ACT-232`, `TIM-002`.
- Classification result: seven source-bounded courtroom genes.

## Taxonomy impact

- Registry changes: seven additive Active genes.
- Taxonomy-change record: `TAXONOMY_CHANGE_124`.
- Candidate terms affected: line-addressed pressing and evidence objection
  versus generic dialogue, case-form discrepancy and final verdict.

## Negative results

- Do not add later Investigation Phase or forensic touchscreen mechanics to
  this first-case-only genome.
- Do not code the fictional culprit as hidden: the introduction depicts him.
- Do not infer actual legal procedure, exact script alternatives or a
  remaster Story Mode from the original DS source packet.

## Delta summary

## New facts

- [Confirmed | Corroborated | High] Capcom designed the shorter first trial as
  an introduction to contradiction-finding; the original DS case uses
  individual testimony lines, Court Record items and finite objection marks
  (`PWA-001`, `PWA-002`, `PWA-004`–`PWA-007`).

## New genes

- [Observation | Corroborated | High] `ACT-526`, `ACT-527`, `SYS-1041`,
  `CON-690`, `INF-391`, `INF-392` and `OBJ-227` distinguish a court challenge
  from a generic answer, fact comparison or manual case verdict.

## New combinations

- [Observation | Corroborated | High] No verified combination is registered.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_124` adds seven
  source-bounded genes without changing older genomes.

## New questions

- Which precise first-case optional responses spend a mark and which only
  repeat a prompt? Direct original-cartridge tracing would test the branch
  table without extrapolating from a written route.
- Does the regional cartridge revision alter any case-record wording that
  matters to the supported contradiction sequence?

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0386 Banjo-Kazooie.
- Optimisation criterion: alternate authored courtroom evidence reasoning
  with embodied collect-and-transform platform routing.
- Expected information gain: character-form abilities, collectible gates
  and navigable three-dimensional world-state progression.
- Backlog impact: preserves the selected nine-game order; no next unit starts
  in this commit.

## Why this game

- [Hypothesis | Limited | Medium] The first trial isolates addressable
  testimony, evidence presentation and penalised failed objections absent
  from the previous high-speed racing packet.
