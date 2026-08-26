---
game_id: GAME-0023
slug: return-of-the-obra-dinn
game_title: Return of the Obra Dinn
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0023
  - COMB-0046
gene_ids:
  action:
    - ACT-030
    - ACT-031
    - ACT-032
  system:
    - SYS-041
    - SYS-042
  constraint:
    - CON-064
  information:
    - INF-012
    - INF-013
  objective:
    - OBJ-017
  time:
    - TIM-002
---

# Game: Return of the Obra Dinn

## Analysis scope

- Version / ruleset: the main investigation loop of Lucas Pope's original
  2018 release, from boarding the returned ship through discovering and
  revisiting death memories, recording provisional fates and completing the
  crew ledger.
- Included: first-person ship exploration only where it discovers corpses or
  supports evidence access; Memento Mortem activation; fixed pre-death audio;
  frozen navigable tableaux; book indexing, transcripts, manifest, group
  sketches and glossary; structured identity, fate, responsible-party or
  destination assignments; revision; grouped validation and lock-in; the
  all-subject investigation objective.
- Excluded: spoiler-level reconstruction of particular deaths; narrative or
  moral interpretation beyond the answer schema; audiovisual style as a gene;
  insurance payment values, endings as qualitative rewards, achievements,
  speedrunning, localisation differences and external notes or guides.
- Direct-play status: not conducted for this record. Creator and publisher
  descriptions are combined with a creator interview, contemporary reviews
  and one spoiler-free rules guide for the late validation threshold.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ROD-001` | The main mechanical task is to determine the identities and fates of the sixty people aboard and complete their book records | Confirmed | Corroborated | High | F1–F4, P1, S1–S3 |
| `ROD-002` | Activating Memento Mortem at an eligible corpse plays fixed sounds or dialogue immediately before death and opens the corresponding frozen moment | Confirmed | Corroborated | High | F4, S1, S4 |
| `ROD-003` | Inside a memory the player can walk and focus on details but cannot alter objects, people or advance the represented time | Confirmed | Corroborated | High | S1, S4 |
| `ROD-004` | Discovered memories remain stable and revisitable, and the book indexes dialogue, scene participants and appearances for cross-reference | Observation | Corroborated | High | S1–S3 |
| `ROD-005` | The book exposes a complete manifest with names, occupations and nationalities plus sketches and a glossary while withholding face-to-name mappings | Confirmed | Corroborated | High | F4, S2, S3 |
| `ROD-006` | The player enters provisional structured assignments for identity and fate, adding a killer, creature or destination when required | Confirmed | Corroborated | High | F4, S1, S3 |
| `ROD-007` | Provisional entries can be revised and receive no immediate per-field correctness signal | Observation | Corroborated | High | S2, S3 |
| `ROD-008` | The system normally confirms and permanently typesets three complete correct fates together rather than confirming guesses one at a time | Confirmed | Corroborated | High | S2, S3, S5 |
| `ROD-009` | After fifty-four confirmed fates the late threshold drops to two; this is a parameter of grouped validation, not another interaction | Confirmed | Direct | Medium | S5 |
| `ROD-010` | Corpse discovery and memory traversal progressively index further scenes and evidence, but every indexed scene preserves fixed content | Observation | Corroborated | High | S1–S3 |
| `ROD-011` | Evidence must often be combined across dialogue, location, clothing, work, relationships and elimination rather than read from one scene | Confirmed | Corroborated | High | F4, P1, S1–S3 |
| `ROD-012` | The scoped investigation contains no random evidence generation or time-driven change while the player reasons or edits the book | Observation | Corroborated | High | ROD-002–ROD-011 |
| `ROD-013` | Mechanical completion evaluates the structured identities and fates; the player's broader interpretation of the voyage is not a scored answer field | Confirmed | Direct | High | P1 |

## Basic data

- Release / origin: Lucas Pope created and 3909 LLC published Return of the
  Obra Dinn for PC and Mac in 2018; console versions followed in 2019.
- Platform or physical form: digital first-person exploration plus a diegetic
  indexed book and immutable three-dimensional evidence reconstructions.
- Puzzle family: investigative deduction from distributed fixed evidence.
- Creator and publisher sources:
  - **[F1]** [Return of the Obra Dinn creator site](https://obradinn.com/),
    insurance-investigation premise and creator attribution.
  - **[F2]** [official prerelease information](https://obradinn.com/media/prerelease.html),
    creator summary of first-person exploration and logical deduction.
  - **[F3]** [Nintendo publisher description](https://www.nintendo.com/en-gb/Games/Nintendo-Switch-download-software/Return-of-the-Obra-Dinn-1633060.html),
    freeform observation and deduction scope.
  - **[F4]** [Nintendo Japan feature](https://www.nintendo.com/jp/topics/article/1c18e843-c55f-11e9-b641-063b7ac45a6d),
    sixty subjects, book and Memento Mortem, final-moment scenes, fate entry,
    cross-scene reasoning and manifest metadata.
- Creator interview:
  - **[P1]** [Game Developer — Road to the IGF interview](https://www.gamedeveloper.com/business/road-to-the-igf-lucas-pope-s-i-return-of-the-obra-dinn-i-),
    Lucas Pope on the empty-book completion pressure and the strict mechanical
    focus on specific identities and fates rather than broad story knowledge.
- Contemporary and reproducible corroboration:
  - **[S1]** [GameSpot review](https://www.gamespot.com/reviews/return-of-the-obra-dinn-review-the-good-ship/1900-6417017/),
    corpse activation, audio, bounded frozen scenes, non-interaction, book
    assignments, cross-memory evidence and progressive discovery.
  - **[S2]** [PC Gamer review](https://www.pcgamer.com/return-of-the-obra-dinn-review/),
    manifest, sketches, glossary, revisits and three-correct grouped lock-in.
  - **[S3]** [PCWorld review](https://www.pcworld.com/article/402788/return-of-the-obra-dinn-review.html),
    structured dropdown fate sentences, sixty-person objective, revision and
    grouped validation.
  - **[S4]** [Nintendo World Report review](https://www.nintendoworldreport.com/review/51991/return-of-the-obra-dinn-switch-review),
    fixed final sounds and freeze-frame memory behaviour.
  - **[S5]** [GameFAQs spoiler-free validation guide](https://gamefaqs.gamespot.com/pc/248186-return-of-the-obra-dinn/faqs/80340/words-of-advice),
    reproducible normal threshold of three and endgame reduction to two after
    fifty-four confirmed records.
- Claim IDs: `ROD-001`–`ROD-013`.

## Mechanical decomposition

### Action Genes

- `ACT-030` — navigate and focus within static evidence scene. The player
  changes viewpoint and zoom target to examine participant identity, object
  geometry, pose and line of action without changing the memory.
- `ACT-031` — activate corpse-linked evidence memory. Memento Mortem selects a
  discovered death record for first entry or revisit; the resulting content is
  fixed rather than generated by the choice.
- `ACT-032` — assign structured identity-fate hypothesis. The player edits
  identity and cause fields and, when the fate grammar requires it, a killer,
  creature or destination field.
- Bookmarking and book cross-links parameterise evidence navigation; they do
  not automatically infer or assign an answer.
- Claim IDs: `ROD-002`–`ROD-007`, `ROD-010`, `ROD-011`.

### System Behaviour Genes

- `SYS-041` — corpse-triggered audio and frozen-scene reconstruction. One
  activation plays the immutable pre-death audio interval and instantiates the
  matching spatial tableau for inspection.
- `SYS-042` — thresholded correct-record confirmation and lock-in. The system
  remains silent on individual guesses, then confirms all currently eligible
  correct records together when the threshold is met and prevents later edits
  to those accepted records.
- The standard threshold is three; the final-tail value of two is a parameter
  of the same transition because only the count changes.
- Scene indexing and newly accessible bodies are progression parameters of
  `SYS-041` and `INF-012`, not random generation.
- Claim IDs: `ROD-002`, `ROD-004`, `ROD-007`–`ROD-010`, `ROD-012`.

### Constraint Genes

- `CON-064` — immutable non-interactive evidence tableau. A memory permits
  observation and interface use but forbids moving people or objects, changing
  the event, or advancing past the frozen death instant.
- This rules out experimentation on the past: deductions must arise from
  preserved evidence and cross-scene comparison.
- Book fields constrain the form of a hypothesis, but their identity, fate and
  dependent-agent vocabulary is a parameter of `ACT-032` and `OBJ-017`, not a
  second generic assignment constraint.
- Claim IDs: `ROD-003`, `ROD-011`, `ROD-012`.

### Information Genes

- `INF-012` — scene-indexed revisitable fixed evidence. Audio, frozen spatial
  details, transcripts and participant appearances are distributed across
  named memories that remain identical on every revisit.
- `INF-013` — finite identity roster with disclosed role metadata. Names,
  occupations and nationalities form a complete candidate set, while sketches
  show faces without initially resolving the mapping.
- `INF-003` is absent. Minesweeper's hidden current contents are exposed by a
  reveal action; Obra Dinn does not reveal a stored identity value from a
  corpse. It supplies evidence from which the player must infer the answer.
- `INF-001` is absent because no current scene simultaneously exposes every
  decision-relevant fact; cross-scene retrieval is the core information cost.
- Claim IDs: `ROD-002`, `ROD-004`, `ROD-005`, `ROD-010`–`ROD-012`.

### Objective Genes

- `OBJ-017` — complete exact identity-and-fate ledger. Every person in the
  finite roster must receive the accepted identity and compound fate, with a
  responsible party or location where required.
- The identity, cause and dependent third field form one validated subject
  record. They are not three independent win conditions because incomplete or
  mismatched fields do not contribute a confirmed fate.
- Understanding event order or motive may support deduction, but the game does
  not require a free-form narrative explanation as an answer.
- Claim IDs: `ROD-001`, `ROD-006`–`ROD-009`, `ROD-013`.

### Time Genes

- `TIM-002` — self-paced sequential action. Ship exploration, memory inspection
  and book editing do not advance a deadline or mutate evidence while the
  player waits.
- The fixed audio lead-in after memory activation is a bounded presentation
  resolution, not a time-pressure phase; the evidence scene then remains
  frozen for unrestricted inspection.
- `TIM-001` is absent because most navigation and hypothesis edits are direct
  self-paced state changes rather than one board command followed by complete
  automatic puzzle resolution.
- Claim IDs: `ROD-002`, `ROD-003`, `ROD-007`, `ROD-012`.

## Reproducible transitions

| Before | Player action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Eligible corpse is present on the ship | Activate Memento Mortem | Fixed final audio plays and the associated death tableau opens | Memory access is corpse-linked and deterministic | `ROD-002` |
| Frozen memory is open | Walk behind a participant and zoom on an object | Viewpoint changes; every represented body, object and pose remains fixed | Inspection does not mutate evidence | `ROD-003` |
| One memory lacks an identity clue | Exit and enter another indexed scene containing the same face | The second scene supplies different stable context while the first remains revisitable | Evidence is distributed and cross-referenceable | `ROD-004`, `ROD-011` |
| Subject record is blank | Select one manifest name and a fate expression | Handwritten provisional fields appear and remain editable | Assignment records a hypothesis, not revealed truth | `ROD-006`, `ROD-007` |
| One complete correct record exists | Finish the fields | No correctness signal appears | Individual guesses are deliberately unconfirmed | `ROD-007`, `ROD-008` |
| Three ordinary unconfirmed records are all correct | Complete the third record | All three are confirmed together and locked | Validation is thresholded and batched | `ROD-008` |
| Two records are correct and one is wrong | Change unrelated fields or wait | No subset is identified or locked | The system withholds which hypothesis failed | `ROD-007`, `ROD-008` |
| Fifty-four fates are confirmed | Make two more complete correct assignments | The pair confirms under the lower tail threshold | Endgame threshold is a parameter | `ROD-009` |
| All required records are confirmed | Complete the final eligible assignments | The book satisfies the investigation objective | Success is exact ledger completion | `ROD-001`, `ROD-013` |

## Strategic and experiential structure

- Local decision: choose the next face, dialogue line, pose, object or book
  field to inspect and decide whether the evidence justifies a provisional
  assignment.
- Medium-term planning: follow one person across scenes, combine manifest
  metadata with occupation and social grouping, and reserve high-confidence
  records to test a more uncertain third hypothesis.
- Long-term structure: progressively reduce the identity permutation and fate
  possibilities until every compound record can be validated.
- Common heuristics: solve clearly named or visually obvious subjects first;
  use confirmed identities as anchors; revisit scenes after new context;
  separate observed cause from inferred identity; use elimination only after
  the candidate roster has genuinely narrowed.
- Failure attribution: no terminal failed attempt exists in the main loop.
  Wrong hypotheses remain editable but delay a confirmation batch without
  saying which field is wrong.
- Player-trust factors: face links, transcripts, scene geometry, accepted fate
  synonyms, threshold timing and permanent confirmation must be consistent.
- Claim IDs: `ROD-001`–`ROD-013`.

## Replay and variation

- What changes between sessions: player discovery order, revisit path,
  provisional hypotheses and which correct records happen to form a batch.
- What remains stable: all scenes, dialogue, roster data, true identities,
  accepted fates and validation rules.
- Randomness or procedural generation: none in the scoped investigation.
- Multiple viable strategies: evidence can be followed chronologically, by
  person, by role group or by confidence; the final ledger is fixed.
- Typical replay motive: limited after full solution because evidence and
  answers are stable; replay may reconstruct chronology or test a different
  deduction order, not discover a new generated case.
- Claim IDs: `ROD-004`, `ROD-007`–`ROD-013`.

## Adjacent systems and history

- Minesweeper also begins with unknown facts, but a reveal directly exposes a
  concealed cell and an exact local count. Obra Dinn preserves indirect scene
  evidence and never reveals a face's identity as the result of inspecting it.
- Nonogram and Sudoku expose all clues simultaneously and accept cell-level
  assignments under global constraints. Obra Dinn distributes evidence across
  revisitable scenes and validates compound subject records in batches.
- Into the Breach previews committed future actions in one current tactical
  state. Obra Dinn indexes immutable past instants whose relation must be
  reconstructed without time pressure.
- Claim IDs: `ROD-001`–`ROD-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-030`, `ACT-031`, `ACT-032` | camera access, bookmarks and fate grammar |
| System Behaviour | `SYS-041`, `SYS-042` | memory indexing and validation thresholds |
| Constraint | `CON-064` | tableau boundary and permitted overlays |
| Information | `INF-012`, `INF-013` | scene metadata, roster fields and sketch grouping |
| Objective | `OBJ-017` | subject count and accepted compound fates |
| Time | `TIM-002` | audio lead-in and unrestricted inspection time |

Canonical signature:

`ACT-030,ACT-031,ACT-032; SYS-041,SYS-042; CON-064; INF-012,INF-013; OBJ-017; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `22` (`GAME-0001`–`GAME-0022`).
- Exact genome matches: none.
- Tied near matches: `GAME-0002` — Rubik’s Cube (`1 / 16 = 0.062500`); `GAME-0005` — Sudoku (`1 / 16 = 0.062500`); `GAME-0008` — Nonogram (`1 / 16 = 0.062500`).
- Supported combination subsets: `COMB-0023`, `COMB-0046`.
- Scan date: 2026-08-11.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0002` — Rubik's Cube | `TIM-002` | Rubik's Cube exposes one current permutation and changes it through reversible moves; Obra Dinn preserves distributed past evidence and edits a compound ledger | Near, `0.062500` |
| `GAME-0005` — Sudoku | `TIM-002` | Sudoku exposes all givens and checks one simultaneous number assignment; Obra Dinn requires cross-scene observation and delays correctness feedback across subject records | Near, `0.062500` |
| `GAME-0008` — Nonogram | `TIM-002` | Nonogram gives complete line clues and edits a binary grid; Obra Dinn maps a metadata roster to faces and structured fates using indexed scenes | Near, `0.062500` |

### Preserved research notes

- New genes: `ACT-030`, `ACT-031`, `ACT-032`, `SYS-041`, `SYS-042`,
  `CON-064`, `INF-012`, `INF-013`, `OBJ-017`.
- Classification result: `New gene` and a new verified combination.
- Evidence and reasoning: only self-paced scheduling fits an existing gene.
  The evidence access, hypothesis interface, grouped confirmation, immutable
  tableaux, roster mapping and compound investigation objective have no
  operational match in the first twenty-two genomes.

## Combination record

- Registered [`COMB-0023`](../../combinations/COMB-0023.md), a proper
  eight-gene subset centred on revisitable death evidence, structured fate
  hypotheses and delayed grouped confirmation.
- Later corpus expansion also registers recurring
  [`COMB-0046`](../../combinations/COMB-0046.md), the smaller `ACT-030` +
  `CON-064` + `TIM-002` immutable evidence-inspection subset shared with The
  Case of the Golden Idol. It does not weaken `COMB-0023`'s dossier boundary.
- General camera inspection and scene immutability remain in the complete
  genome but are not both required to identify the dossier-validation loop.

## Taxonomy impact

- Registry changes: nine stable genes added; `TIM-002` reused.
- Taxonomy-change record: none. Evidence disclosure remains Information,
  player-entered propositions remain Actions, automatic verification remains
  System Behaviour and the accepted full ledger remains an Objective.
- Candidate terms affected: frozen-scene inspection, corpse-memory activation,
  structured fate assignment, death reconstruction, batch confirmation,
  immutable evidence, scene indexing, roster metadata and ledger completion
  are promoted.

## Negative results

- `INF-003` and `INF-004` are absent because no reveal exposes a concealed
  identity value or exact local aggregate clue.
- `INF-001` is absent because evidence is deliberately distributed across
  selectively revisited scenes.
- `OBJ-004` is absent because the target is a structured semantic ledger, not
  a spatial configuration of existing components.
- `TIM-001` is absent because observation and book revision remain self-paced.
- No structured negative-result record is required; no prior concrete novelty
  or taxonomy claim was rejected.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] A corpse selects immutable pre-death audio
  and a navigable frozen tableau rather than revealing the person's identity
  directly (`ROD-002`–`ROD-004`).
- [Confirmed | Corroborated | High] Correct compound records are confirmed and
  locked in groups, withholding per-guess feedback (`ROD-006`–`ROD-009`).

## Нові гени

- [Observation | Corroborated | High] Added `ACT-030`, `ACT-031`, `ACT-032`,
  `SYS-041`, `SYS-042`, `CON-064`, `INF-012`, `INF-013` and `OBJ-017`;
  reused `TIM-002`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0023` captures structured dossier
  deduction from revisitable fixed evidence with delayed batch validation.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; the existing
  Action / Information / System Behaviour split represents hypothesis,
  evidence and confirmation without a seventh type.

## Нові питання

- Does another detective puzzle reuse `INF-012` while validating each answer
  immediately rather than through `SYS-042`?
- Can a non-narrative matching puzzle support `INF-013` and `OBJ-017` without
  spatial evidence scenes?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0024` — Gorogoa.
- Optimisation criterion: move from semantic deduction to direct spatial image
  manipulation while testing panel rearrangement, overlay and viewpoint depth.
- Expected information gain: distinguish moving a panel as a container from
  transforming the illustrated world it exposes, and test whether visual
  alignment requires new Action, System Behaviour and Constraint genes.
- Backlog impact: remove Gorogoa from the retained pool; preserve Lemmings and
  World of Goo.

## Чому саме вона

- [Hypothesis | Limited | High] Its panel-layer grammar is mechanically distant
  from both dossier deduction and all existing grid-placement records, while
  its publisher documentation gives a bounded next scope.
