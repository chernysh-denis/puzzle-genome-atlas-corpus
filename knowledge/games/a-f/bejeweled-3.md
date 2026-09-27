---
game_id: GAME-0411
slug: bejeweled-3
game_title: Bejeweled 3
analysis_status: reviewed
reviewed: 2026-09-26
combination_ids: []
gene_ids:
  action:
    - ACT-011
    - ACT-012
  system:
    - SYS-003
    - SYS-004
    - SYS-010
    - SYS-011
    - SYS-012
    - SYS-013
    - SYS-014
    - SYS-1095
  constraint:
    - CON-001
    - CON-019
  information:
    - INF-001
    - INF-002
  objective:
    - OBJ-002
    - OBJ-003
  time:
    - TIM-003
---

# Game: Bejeweled 3

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Gem colours,
point values and animation speed are parameters, not additional genes.

## Analysis scope

- Version / ruleset: PopCap's original English Windows PC *Bejeweled 3*,
  version `1.0.8.6128` (2010), **Classic** mode only. The original PC readme
  and PopCap's official strategy guide bound this packet. It does not equate
  a later console or mobile release with the analysed executable.
- Structured analysis target: `PLAT-WINDOWS-PC` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: inspect the visible 8 × 8 gem field; choose one
  orthogonally adjacent exchange that forms a line of at least three, or
  exchange a stored Hypercube with an adjacent colour; let matched gems,
  specials, falling gems, unpreviewed refill and cascades alter the field;
  optionally make another valid match while gems from the previous one are
  still falling; weigh immediate score against keeping future exchanges
  possible, until no physical move remains.
- Entry: start Classic on the original PC build and take first control of
  its initial 8 × 8 field. Record actual executable revision, starting field,
  score, level, and whether any special gem exists; do not assume a fixed
  seed or first layout.
- Positive terminal: Classic has no level-completion target. The bounded
  run terminates naturally when the board has no possible move; the final
  score and reached level appear on its results screen. A high score is an
  evaluation, not a distinct win-state threshold.
- Failure and recovery control: deliberately create a field with no
  remaining legal exchange and verify the same natural terminal. A manual
  Reset instead aborts the run and its score is not recorded; it is not
  treated as successful completion.
- Included: seven ordinary colour classes; adjacent match-producing swaps;
  three-or-more line clearing; fall and unpreviewed replenishment; repeated
  cascades; four-line Flame, five-line Hypercube, T/L Star and six-line
  Supernova creation; documented Flame, Hypercube and Star effects; the
  match/scoring schedule and current Classic level multiplier; no-move
  termination; the free Hint; permitted matching during falling.
- Excluded: the undisclosed exact Supernova effect footprint, exact refill
  distribution and board-generation safeguards; exact thresholds for
  advancing a Classic level; untested input timing within one animation
  frame; the cosmetic Instant Replay, window settings, achievements and
  cumulative account rank; Zen, Lightning, Quest, secret modes, later
  editions, purchases and online features.
- Potential scoped modules: Classic's complete level-threshold schedule,
  tested Supernova effects, another named mode's distinct clock/objective,
  or mode unlocking and account rank outside one Classic run.
- Reproducible parameterisation: capture the executable revision, mode,
  board and level before each swap, legal adjacency/match, special created
  or consumed, post-clear collapse/refill, cascade depth, early-swap timing,
  score increment and whether any legal exchange remains. Test a five-line
  Hypercube swap and a falling-gem early swap separately. For a natural
  terminal, record the no-move board and results; for Reset, record the
  aborted score's absence from results.
- Direct-play status: none. The PC executable, save, input trace, screen,
  video and audio were not inspected. This is a source-bounded
  reconstruction of original PC Classic, not a claim of played or
  frame-verified behaviour.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BJ3-001` | Original PC Classic uses an 8 × 8 field, seven ordinary colours and only orthogonally adjacent match-producing exchanges. | Confirmed | Direct | High | P1 |
| `BJ3-002` | A valid line clears, gems fall and refill from above; new matches can cascade repeatedly. | Confirmed | Direct | High | P1, P2 |
| `BJ3-003` | A four-line makes Flame, five-line Hypercube, T/L makes Star and six-line makes Supernova. | Confirmed | Direct | High | P1, P2 |
| `BJ3-004` | Flame clears its surrounding eight cells when matched; Star clears both axes; a Hypercube exchanged with an adjacent colour clears that colour across the board. | Confirmed | Direct | High | P1, P2 |
| `BJ3-005` | Classic is untimed and ends when no physical move remains, not after a preset move count or target quota. | Confirmed | Direct | High | P1, P2 |
| `BJ3-006` | The player may form another match while gems from a prior one are still falling. | Confirmed | Direct | High | P1 |
| `BJ3-007` | Classic uses base match, special and increasing cascade awards multiplied by current level number. | Confirmed | Direct | High | P1 |
| `BJ3-008` | Hint reveals a possible match for no score cost; Reset aborts without recording the run score. | Confirmed | Direct | High | P1 |
| `BJ3-009` | Refill colours are not previewed; their exact selection distribution is not established. | Observation | Corroborated | Medium | P1, P2 |
| `BJ3-010` | The untested Supernova footprint and Classic level thresholds cannot be inferred from this source packet. | Observation | Limited | High | P1, P2 |

## Basic data

- Release / origin: PopCap Games released *Bejeweled 3* for Windows PC on
  7 December 2010; the analysed original readme names build `1.0.8.6128`.
- Platform or physical form: original Windows PC pointer/keyboard game;
  exact installed executable uninspected.
- Puzzle family: matching and combination (`FAM-004`).
- Primary sources, accessed 2026-09-26:
  - **P1** — [PopCap's original PC *Bejeweled 3* readme, preserved as source
    text](https://bejeweled.wiki.gg/wiki/Bejeweled_3/readme.html/source),
    sections Playing the Game, Classic and Basic Scoring. The readme itself
    is a primary manufacturer document; the hosting wiki is a mirror, not
    independent gameplay corroboration.
  - **P2** — [PopCap's official *Bejeweled 3* strategy
    guide](https://images.popcap.com/www/images/product/extras/strategyguides/bejeweled3/1033/bejeweled3strategyguide.pdf),
    printed pp. 4–7. It corroborates special creation/effects and the
    untimed no-move end. The PDF's original host needed a local TLS-bypass
    download for inspection; P1 supplies the independent readable claim
    surface. Neither source is a direct play trace.
- Claim IDs: `BJ3-001`–`BJ3-010`.

## Mechanical decomposition

### Action Genes

- `ACT-011`: exchange orthogonally adjacent addressed gems. Ordinary
  exchanges count only if they produce a three-or-more line.
- `ACT-012`: exchange a persistent Hypercube with an adjacent ordinary gem
  to trigger its colour-wide effect even though the ordinary match pattern
  need not form. Matched Flame and Star gems instead trigger as part of
  ordinary match resolution, not by an invented tap command.
- Hint is a free interface query, not a score-bearing board action. Reset is
  an abort control outside the continuing decision loop.
- Claim IDs: `BJ3-001`, `BJ3-004`, `BJ3-008`.

### System Behaviour Genes

- `SYS-010`, `SYS-011`, `SYS-003` and `SYS-004` clear a valid line, collapse
  occupied columns and choose unpreviewed new gems from above.
- `SYS-012` repeats newly formed matches and special triggers as cascades;
  `SYS-013` converts defined four-, five-, T/L- and six-patterns to stored
  specials. `SYS-014` applies documented Flame, Star and Hypercube multi-gem
  footprints. The Supernova class is admitted by its six-line creation but
  no unsourced precise clearing shape is assigned.
- New `SYS-1095` adds base match/special/cascade awards and scales all
  Classic base values by the current level: a simple triple is 50 at level
  one; each later cascade adds a 50-point bonus over the prior cascade base.
  The source specifies values for the other named effects; their exact
  resolution order in overlapping early-input cascades is not asserted.
- Resolution order in a non-overlapped example: accepted swap → pattern
  detection → clearing/special effect → score increment → collapse and
  refill → further cascade detection → evaluate legal-move availability.
  The original controls also admit a fresh valid swap *during* falling, so
  this serial description is not imposed as a global input lock.
- Claim IDs: `BJ3-002`–`BJ3-004`, `BJ3-006`, `BJ3-007`, `BJ3-010`.

### Constraint Genes

- `CON-001`: exactly 64 addressed positions on a fixed 8 × 8 field;
  occupants change but capacity does not.
- `CON-019`: an ordinary exchange must be orthogonally adjacent and form a
  match; a stored Hypercube's adjacent-colour activation is the exception.
- `CON-020` is absent: Classic has no finite allotted move stock. The number
  of future legal moves is state-dependent, not a displayed decrementing
  quota.
- Claim IDs: `BJ3-001`, `BJ3-004`, `BJ3-005`.

### Information Genes

- `INF-001` exposes the current field, present specials, score and level.
  Hint can point to a currently legal match without spending points.
- `INF-002` covers unpreviewed future refill identities; no probability
  table or claim of guaranteed solvability follows from this.
- Claim IDs: `BJ3-008`, `BJ3-009`.

### Objective and Time Genes

- `OBJ-002` evaluates the session by accumulated Classic score;
  `OBJ-003` captures the need to preserve at least one legal next exchange
  to keep that score run alive. Reaching a new level is not the terminal.
- `TIM-003` applies **only during a self-created falling/cascade interval**:
  new gems advance on live animation time and the PC controls can accept
  another match before they settle. Between such intervals Classic is
  untimed, so `TIM-003` does not imply a level countdown. `TIM-001` is
  rejected because it forbids the documented early next match.
- Claim IDs: `BJ3-005`–`BJ3-007`.

## Reproducible transitions

| Before | Action | Bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Two neighbours would form no line | Try exchanging them | Ordinary exchange is not accepted as a move | match-validity gate | `BJ3-001` |
| Three same-colour gems would align after a legal exchange | Swap the adjacent pair | Line clears, its column falls and new gems enter | base match loop | `BJ3-001`, `BJ3-002` |
| Four equal gems can align in a line | Make that exchange | A Flame gem is created at a rule-selected position | pattern creates a stored special | `BJ3-003` |
| A Flame or Star is part of a later match | Complete that match | Flame clears its surrounding eight positions, or Star its row and column | class-specific area effect | `BJ3-004` |
| A Hypercube is adjacent to a coloured gem | Exchange the two | All present gems of that colour are cleared, then the board resolves | special activation exception | `BJ3-004` |
| Falling/refill creates another line | Let it resolve without a new command | Another clear and fall occurs; cascade bonus rises | uncharged repeated system step | `BJ3-002`, `BJ3-007` |
| A legal exchange exists while earlier gems are still falling | Make the exchange during that interval | Another match can begin before full settlement; exact frame ordering is untested | input is not globally turn-locked | `BJ3-006` |
| A settled field has no legal physical move | Wait or request Hint | Classic ends and displays final score and level | no-move terminal, not move-budget exhaustion | `BJ3-005` |
| A run is underway | Press Reset | New game starts; aborted score is not recorded | abort differs from natural terminal | `BJ3-008` |

## Strategic and experiential structure

- Local decision: find a valid exchange and forecast the first clear,
  special creation and position of resulting empty cells.
- Medium-term planning: high-board matches tend to leave movement options;
  low-board matches can produce larger cascades. Hold a Hypercube as a
  colour-wide rescue option when ordinary moves become scarce.
- Long-term structure: extend a Classic run through successive level-scaled
  scoring states until the first no-move board, then compare final score.
- Failure attribution: a blocked field ends the run regardless of stored
  score. Exact next-gem identities and their probabilities are unknown.
- Player-trust factors: Hint is free, current field is visible, and Reset
  clearly distinguishes an abandoned run from a recorded terminal score.
- Claim IDs: `BJ3-001`–`BJ3-009`.

## Replay and variation

- Initial field and subsequent refill may differ between sessions; the
  source does not document a probability distribution or safety algorithm.
- Matching at different locations changes column collapse, cascades and
  remaining legal moves. High-score seeking is therefore not reducible to
  a fixed quota or level-clear script.
- Claim IDs: `BJ3-002`, `BJ3-005`, `BJ3-007`, `BJ3-009`.

## Adjacent systems and history

- The official guide calls Classic the traditional untimed Bejeweled mode;
  this packet does not infer undocumented earlier-version rules from that
  historical description.
- Royal Match and Candy Crush Saga also swap, clear and refill; their
  analysed records are finite-move target levels, whereas Classic is an
  open score run whose terminal is no possible exchange. PC Bejeweled 3
  additionally permits a match during falling, unlike `TIM-001`'s strict
  completed-resolution boundary in those records.
- Claim IDs: `BJ3-001`–`BJ3-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-011`, `ACT-012` | gesture; Hypercube neighbour |
| System Behaviour | `SYS-003`, `SYS-004`, `SYS-010`–`SYS-014`, `SYS-1095` | colour selection, match shape, cascade depth, level multiplier |
| Constraint | `CON-001`, `CON-019` | 8 × 8 capacity; valid exchange |
| Information | `INF-001`, `INF-002` | current field, hidden refill |
| Objective | `OBJ-002`, `OBJ-003` | session score; mobility |
| Time | `TIM-003` | self-paced pauses; early input during falling only |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `410` (`GAME-0001`–`GAME-0410`).
- Exact genome matches: none.
- Tied near matches: `GAME-0009` — Royal Match (`13 / 20 = 0.650000`); `GAME-0109` — Candy Crush Saga (`13 / 20 = 0.650000`).
- Supported combination subsets: none.
- Scan date: 2026-09-26.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0009` — Royal Match | `ACT-011`, `ACT-012`, `SYS-003`, `SYS-004`, `SYS-010`–`SYS-014`, `CON-001`, `CON-019`, `INF-001`, `INF-002` | Both swap adjacent items and resolve match, special and refill cascades on a visible fixed board. Royal Match charges a finite move stock toward level targets and locks input through each resolution; Classic pursues level-scaled score and survival until no swap remains, with documented input during falling. | Near, `0.650000` |
| `GAME-0109` — Candy Crush Saga | `ACT-011`, `ACT-012`, `SYS-003`, `SYS-004`, `SYS-010`–`SYS-014`, `CON-001`, `CON-019`, `INF-001`, `INF-002` | The common swap-clear-refill substrate is the same. Candy Crush's scoped order level is won within a fixed move allowance; Bejeweled Classic has neither order quota nor move allowance, but scales cascade awards by level and ends only when mobility is exhausted. | Near, `0.650000` |

## Taxonomy impact

- New `SYS-1095`, documented in
  [`TAXONOMY_CHANGE_149`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_149.md).
- `TIM-003` is reused for early legal input while the previous gem-fall
  window progresses; it does not assert an inter-move time limit.
- No older reviewed signature changes.

## Negative results

- `TIM-001` rejected because the primary PC controls explicitly allow
  another match while previous gems are still falling.
- `CON-020` and `OBJ-007` rejected: Classic has no finite move stock or
  declared colour-order target.
- `SYS-028` rejected: the multiplier is the current Classic level, not an
  ordered player-controlled modifier sequence.
- Exact Supernova footprint, level thresholds, refill probabilities and
  guarantee of future moves remain unverified; no gene is inferred from
  those missing details.

## Delta summary

- A historically central match-3 game has a mechanically different scoped
  signature from contemporary move-limited target levels. Its automatic
  cascade can overlap an early next input, and its score is scaled by
  current Classic level until mobility ends the run.

## Source and method notes

- Sources P1 and P2 are original PopCap documents hosted by a wiki mirror
  and the former PopCap content domain respectively. They are rules
  evidence, not direct observation of the named executable.
- The source-bounded packet does not promote unknown Supernova behaviour,
  refill policy or level schedule to a fact.

## New facts

- [Confirmed | Direct | High] PopCap explicitly permits a new match during
  falling despite Classic's absence of a running deadline (`BJ3-005`,
  `BJ3-006`).
- [Confirmed | Direct | High] Cascades receive increasing bonus base points
  and all Classic base values scale by current level (`BJ3-007`).

## New genes

- [Confirmed | Direct | High] `SYS-1095` isolates Classic's level-scaled
  match and cascade scoring from board resolution and other score systems.

## New combinations

- [Observation | Corroborated | High] No new verified combination. The
  move-limited target core `COMB-0009` is not a subset of this genome.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_149` admits `SYS-1095`
  without revising an older signature.

## New questions

- What does a directly inspected original PC Supernova actually clear,
  and in what order relative to an overlapping early swap?
- What exact progress threshold raises a Classic level in build 1.0.8.6128?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0412` *Splatoon 3*.
- Optimisation criterion: alternate from an untimed PC matching field to
  a time-bounded Nintendo Switch team territory contest.
- Expected information gain: distinguish ink coverage, refill, traversal
  and final turf evaluation from earlier shooter objectives.
- Backlog impact: no selected subject displaced.

## Why this game

- [Hypothesis | Corroborated | Medium] *Bejeweled 3* tests whether the
  archetypal match-three substrate is separable from finite move quotas
  and target clearing, while its original PC readme resolves a subtle
  early-input timing boundary.
