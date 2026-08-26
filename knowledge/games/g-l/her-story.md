---
game_id: GAME-0106
slug: her-story
game_title: Her Story
analysis_status: reviewed
reviewed: 2026-08-15
combination_ids:
  - COMB-0106
gene_ids:
  action:
    - ACT-108
    - ACT-109
  system:
    - SYS-142
  constraint:
    - CON-160
  information:
    - INF-012
  objective:
    - OBJ-051
  time:
    - TIM-002
---

# Game: Her Story

## Analysis scope

- Version / ruleset: Sam Barlow's original 2015 release, bounded to one
  transcript-query discovery packet in the L.O.G.I.C. police archive.
- Included: a broad typed term; case-insensitive transcript matching; fixed
  chronological ordering; disclosure of only the earliest five matching clips;
  selection and playback of one returned immutable interview clip; extraction
  of a rarer spoken term by the human player; a refined query; retrieval of a
  later clip hidden behind the broad-query cap; revisiting discovered clips;
  self-paced interaction; and increased watched-evidence coverage.
- Excluded: plot conclusions, identities, exact production transcript, user
  tags, Database Checker geometry, hidden admin commands, Mirror Game, the SB
  chat threshold, credits, achievements, platform differences and exhaustive
  retrieval of all 271 clips.
- Direct-play status: not conducted because no licensed executable was found on
  this Mac. The official site defines transcript-query retrieval; creator
  interviews establish the language graph, chronological first-five cap and
  refinement intent. BFI independently corroborates ordering and cap. A
  synthetic executable control reproduces those rules without copying dialogue.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HST-001` | The playable archive contains fixed clips from seven 1994 police interviews | Confirmed | Corroborated | High | P1, P2 |
| `HST-002` | A typed query retrieves clips whose answer transcript contains the requested words | Confirmed | Corroborated | High | P1, P2, S1 |
| `HST-003` | Matching clips are ordered chronologically and only the first five are viewable for one query | Confirmed | Corroborated | High | P3, S1, V1 |
| `HST-004` | Repeating the same broad query cannot page beyond that stable first-five window | Confirmed | Corroborated | High | P3, S1, V1 |
| `HST-005` | A term noticed in a viewed clip can be reused as a narrower query to expose a later record hidden by the broad-query cap | Confirmed | Corroborated | High | P2, P3, V1 |
| `HST-006` | Retrieved clips are immutable evidence records that can be replayed without changing their transcript or timestamp | Observation | Corroborated | High | P1, S1 |
| `HST-007` | Search and playback are self-paced; the bounded packet has no move or real-time deadline | Observation | Corroborated | High | P1–P3, S1 |

## Basic data

- Release / origin: designed, written and directed by Sam Barlow; released in
  2015 with Indie Fund support.
- Platform or physical form: single-player simulated desktop containing a
  searchable archive of live-action interview clips.
- Puzzle family: nonlinear evidence discovery through transcript queries.
- Primary sources:
  - **[P1]** [official Her Story about page](https://www.herstorygame.com/about/),
    for the seven interviews, police database and query-to-spoken-word rule.
  - **[P2]** [Game Developer interview with Sam Barlow](https://www.gamedeveloper.com/audio/road-to-the-igf-sam-barlow-s-i-her-story-i-),
    for video-plus-database-search design and the computed word/clip connection
    graph used to balance discoverability.
  - **[P3]** [PocketGamer.biz making-of interview](https://www.pocketgamer.biz/making-of-her-story/),
    where Barlow explains the first-five restriction and later multiword
    refinement from terms noticed in clips.
- Secondary sources:
  - **[S1]** [BFI tenth-anniversary analysis](https://www.bfi.org.uk/features/her-story-10-years),
    for transcript matching, chronological ordering, five-view cap and targeted
    terms as the route to later evidence.
  - **[V1]** [`verify_her_story_query_loop.py`](../../../scripts/verify_her_story_query_loop.py),
    an independent synthetic control for stable ordering, cap and refinement.

## Mechanical decomposition

### Action Genes

- `ACT-108` — submit free-text term query against evidence archive. The player
  types one or more chosen words into the L.O.G.I.C. search field and commits
  them as the next retrieval request.
- `ACT-109` — play selected immutable evidence record. The player chooses one
  returned clip and watches or replays its fixed interview response.
- Reading a spoken term and deciding it is useful is human inference. It is not
  automatic term extraction, a supplied vocabulary or a structured answer.

### System Behaviour Genes

- `SYS-142` — retrieve transcript-matching records in fixed chronological order.
  A committed query is matched against archived answer transcripts, and every
  qualifying record receives the same stable order on repeated requests.
- Resolution order: normalise the committed query; identify fixed transcript
  matches; order them chronologically; apply the visible-result cap; let the
  player select and play a result; retain that clip as revisitable evidence.

### Constraint Genes

- `CON-160` — earliest-five visibility cap per archive query. At most the first
  five chronologically ordered matches can be opened from one result set, even
  when more records match; repeating the query does not expose a next page.
- This is a retrieval boundary, not a five-action budget: the player may issue
  unlimited new queries and replay already discovered evidence.

### Information Genes

- `INF-012` — scene-indexed revisitable fixed evidence. Interview clips have
  stable dates, content and transcripts; once found they can be replayed and
  cross-referenced after another query.
- The complete corpus is not simultaneously visible. Search terms control
  which fixed records become available, while playback exposes visual and
  spoken evidence beyond the matching word itself.

### Objective Genes

- `OBJ-051` — expand reviewed evidence coverage through semantic retrieval.
  In this bounded packet, success means surfacing and watching one later fixed
  record that the broad query counts but its first-five window conceals.
- This objective deliberately does not claim that the game validates a single
  plot interpretation or requires 100% archive completion.

### Time Genes

- `TIM-002` — self-paced sequential action. Search, selection, playback pause
  and the next query have no move budget or advancing-world deadline.

## Reproducible transitions

The control uses original synthetic transcripts, not Her Story dialogue.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Seven fixed records contain `murder` | Submit `murder` | Seven matches are counted; only chronological records 1–5 are returned | transcript retrieval plus cap | `HST-002`, `HST-003` |
| The broad result remains open | Submit `MURDER` again | The same five records return in the same order | no pagination or random rotation | `HST-004` |
| Record 2 contains the rarer phrase `blue window` | Select and play record 2 | Its fixed spoken text exposes the phrase to the player | immutable evidence consumption | `HST-005`, `HST-006` |
| Record 6 also contains `blue window` but is outside the broad result | Submit `blue window` | Records 2 and 6 return; record 6 is now selectable | breadcrumb refinement bypasses broad-query cap | `HST-005` |
| No record contains the whole token `mur` | Submit `mur` | Zero records return | bounded term matching, not arbitrary substring access | `HST-002` |

## Strategic and experiential structure

- Local decision: choose a query whose expected match set is narrow enough to
  reveal new evidence, then choose which returned clip to inspect.
- Medium-term planning: retain names, objects, places and unusual phrases from
  clips as candidate keys, and refine broad terms that saturate the cap.
- Long-term structure: build a personal connection graph among fixed fragments
  until enough of the interview corpus has been reviewed to support an account.
- Common heuristics: follow rare nouns; combine related terms; use timestamps
  to compare context; do not expect repeated broad searches to paginate.
- Failure attribution: an empty or redundant result follows from the chosen
  term and fixed corpus. It consumes no scarce attempt and can be revised.
- Player-trust factors: matching, chronology, cap and clip contents must remain
  stable; a rare term heard in evidence must retrieve every eligible record.

## Replay and variation

- The archive, transcript words, timestamps and result ordering are authored
  and fixed. Query order, viewed subset and inferred story graph vary.
- No randomness or procedural generation occurs in the bounded packet.
- Replay chiefly tests a different breadcrumb path or fills missed evidence,
  rather than producing a new case.

## Adjacent systems and history

- Return of the Obra Dinn also distributes immutable evidence across revisitable
  scenes, but its scenes are unlocked through corpse-linked spatial discovery
  and support a validated structured ledger. Her Story retrieves clips through
  arbitrary typed language and does not validate a plot account.
- The Case of the Golden Idol lets players extract highlighted terms into a
  persistent supplied bank. Her Story highlights no canonical vocabulary:
  the player may type any inferred word, including a term never collected by
  the interface.
- The Password Game also accepts free text, but continuously evaluates one
  persistent answer against revealed rules. Her Story treats each committed
  string as an independent archive query and returns evidence records.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-108`, `ACT-109` | query syntax; playback controls |
| System Behaviour | `SYS-142` | normalisation; match semantics; order |
| Constraint | `CON-160` | visible result cap; no pagination |
| Information | `INF-012` | clip metadata; transcript; revisit path |
| Objective | `OBJ-051` | watched target; coverage threshold |
| Time | `TIM-002` | pause policy |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `105` (`GAME-0001`–`GAME-0105`).
- Exact genome matches: none.
- Tied near matches: `GAME-0023` — Return of the Obra Dinn (`2 / 15 = 0.133333`).
- Supported combination subsets: `COMB-0106`.
- Scan date: 2026-08-15.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0023`.

### Preserved research notes

- New genes: `ACT-108`, `ACT-109`, `SYS-142`, `CON-160`, `OBJ-051`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: the corpus already represented revisitable immutable
  evidence and self-paced investigation. It lacked arbitrary typed transcript
  queries, direct playback of a selected fixed record, stable chronological
  full-text retrieval, an earliest-five no-pagination cap and a mechanically
  represented objective of expanding reviewed evidence through query discovery.

## Taxonomy impact

- Registry changes: five Active IDs and two transfers to a new game.
- Taxonomy-change record: none; no previous gene is merged, split or retired.
- Candidate terms affected: transcript query, evidence-record playback,
  capped chronological retrieval and watched-evidence coverage.

## Negative results

- `ACT-059` rejected: Her Story does not highlight or collect a canonical term
  into an interface vocabulary; the human freely chooses what to type.
- `ACT-103` rejected: each query is a transient independent request, not one
  persistent answer string that remains under evaluation.
- `OBJ-017` rejected: the game does not require or validate a structured
  identity-and-fate ledger or a single plot interpretation.
- `CON-020` rejected: five is a result-visibility cap, not an action budget.
- `INF-001` rejected: the complete archive is deliberately unavailable at once.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Широкий запит повертає стабільні перші
  п’ять хронологічних збігів; рідкісне слово з переглянутого кліпу може відкрити
  пізніший запис, прихований за цим лімітом (`HST-002`–`HST-005`).

## Нові гени

- [Observation | Corroborated | High] `ACT-108` — подати вільний текстовий
  запит до архіву; `ACT-109` — відтворити вибраний незмінний доказовий запис.
- [Observation | Corroborated | High] `SYS-142` — повернути transcript-збіги у
  фіксованому хронологічному порядку; `CON-160` — показати лише перші п’ять.
- [Observation | Corroborated | High] `OBJ-051` — розширювати покриття
  переглянутих доказів через семантичне уточнення запитів.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0106` — мовний breadcrumb-цикл від
  запиту через перегляд кліпу до уточненого запиту, що обходить широкий cap.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Чи повторює Telling Lies повний `COMB-0106`, чи word-select, двосторонні
  дзвінки та інша навігація вимагають окремої межі?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] The Pedestrian.
- Optimisation criterion: contrast language-indexed evidence discovery with
  spatial editing of a traversable panel graph.
- Expected information gain: test whether rearranging and reconnecting signs
  transfers to existing panel-view genes or requires topology-edit boundaries.
- Backlog impact: preserves Telling Lies for a later direct reuse audit and
  avoids analysing two transcript-search relatives consecutively.

## Чому саме вона

- [Hypothesis | Limited | Medium] The Pedestrian should share self-paced
  authored progression while replacing every query/cap mechanism with direct
  panel rearrangement, connector editing and avatar traversal.
