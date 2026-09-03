---
game_id: GAME-0228
slug: a-way-out
game_title: A Way Out
analysis_status: reviewed
reviewed: 2026-09-02
combination_ids:
  - COMB-0226
gene_ids:
  action:
    - ACT-008
    - ACT-341
    - ACT-398
  system:
    - SYS-045
    - SYS-369
    - SYS-733
  constraint:
    - CON-077
    - CON-378
    - CON-567
    - CON-568
  information:
    - INF-001
    - INF-167
  objective:
    - OBJ-086
  time:
    - TIM-003
---

# Game: A Way Out

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam release, app
  `1222700`, public Build ID `13095794`, built 2024-01-04 and published to the
  public branch 2024-01-11, checked 2026-09-02; one local split-screen Story
  session with a full game copy, default difficulty and two human players.
- Platform and mode: Windows local couch co-op. One human retains Leo and the
  other retains Vincent; neither character has an AI substitute. Online play,
  Friend Pass and Remote Play Together are excluded environment variants.
- Entry: load a local Story save or an unlocked Chapter Select at
  `Escape` → `Cell Breach`, then retain the first control after Fred delivers
  the chisel to Leo inside a book. Getting the chisel, the hospital, work detail
  and every earlier prison sequence are prior state rather than admitted play.
- Primary decision loop: both players read the simultaneous panes and the two
  guard approaches; the current chisel holder moves the toilet, releases its
  fasteners and panel and cuts the bars only during an unobserved window, while
  the partner watches and warns; the worker cancels and conceals the operation
  before inspection; after Leo completes his opening he passes the one chisel
  to Vincent, and the two players exchange worker/lookout duties until both
  openings are complete.
- Positive terminal: after both openings are complete, wait for lights-out,
  move both characters through their respective openings and retain the first
  automatic story checkpoint after both have left the visible cells. Confirm
  the terminal by returning to the menu only after the save indicator has
  cleared and verifying that Continue or Chapter Select preserves the reached
  post-cell state. Merely finishing Leo's opening, passing the chisel or moving
  only one character through is intermediate.
- Negative terminal: if either guard inspects a cell while its occupant keeps
  the forbidden work exposed, the current attempt fails and returns to its
  authored checkpoint; voluntary restart has the same non-positive boundary.
- Included: fixed Leo/Vincent ownership; two human input owners; persistent
  split-screen; direct cell movement; contextual toilet, fastener, panel, bar
  and opening interactions; two autonomous guard approaches; stopping and
  concealing work; the unique chisel and its Leo-to-Vincent handoff; retained
  completed fixture stages; both players' exit from the cells; failure retry
  and the first retained post-cell checkpoint.
- Excluded: the hospital theft and rooftop retrieval of the chisel; the later
  wrench relay, fan, shaft, balance climb and complete prison escape; fights,
  chases, driving, fishing, optional conversations and activities; every later
  chapter and the campaign ending; online co-op, Friend Pass, Remote Play
  Together, EA-account/network state, achievements, other platforms and the
  complete story.
- Reproducible parameterisation: install Steam app `1222700` public build
  `13095794`, use Local Play with two controllers and an existing save that has
  unlocked `Escape` → `Cell Breach`, retain Leo/Vincent assignment, start at
  Fred's book delivery, complete both cell openings and stop after the first
  cleared autosave indicator following both characters' departure from the
  cells. If the checkpoint does not retain after a clean menu return, the run
  does not satisfy this packet.
- Potential scoped modules: `Work Detail`, the later wrench relay, one chase or
  fight, an online Friend Pass session and any post-prison story segment each
  require their own entry, roles, systems and terminal.
- Direct-play status: not conducted. EA and Steam establish the current
  Windows two-human local split-screen product; the EA PC manual and an EA
  staff response establish session entry and automatic checkpoint/chapter
  retention; independent written walkthroughs reproduce the named Cell Breach
  sequence, role exchange, guard failure and exit. This is an evidence-based
  rules reconstruction. No video or audio was opened, played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `AWO-001` | A Way Out is an exclusively cooperative game that requires two players controlling Leo and Vincent | Confirmed | Direct | High | P1, P2, P3, P4 |
| `AWO-002` | The current Steam product supports Windows local shared/split-screen co-op and exposes public Build `13095794` | Confirmed | Corroborated | High | P1, S1 |
| `AWO-003` | `Cell Breach` begins when Fred returns the chisel to Leo inside a book | Observation | Corroborated | High | S2, S3, S4 |
| `AWO-004` | The chisel holder completes ordered toilet, plate and bar work while the partner watches two approaching guards | Observation | Corroborated | High | S2, S3, S4 |
| `AWO-005` | Continuing exposed work during a guard inspection fails the attempt, while stopping and concealing it preserves the run | Observation | Corroborated | High | S2, S3, S4 |
| `AWO-006` | Leo passes the one chisel to Vincent after completing his opening, exchanging worker and lookout duties | Observation | Corroborated | High | S2, S3, S4 |
| `AWO-007` | Both characters must complete their openings and leave the cells after lights-out before the bounded terminal is eligible | Observation | Corroborated | High | S2, S3, S4 |
| `AWO-008` | A Way Out uses automatic checkpoints that later permit Continue or Chapter Select from retained story progress | Confirmed | Direct | High | P5, P6 |
| `AWO-009` | The first cleared autosave after both characters leave the cells is a reproducible retained terminal rather than an arbitrary pause | Observation | Corroborated | Medium | P5, P6, S2, S3, S4 |

## Basic data

- Release / origin: Hazelight Studios; Electronic Arts released A Way Out on
  2018-03-23 and released the Steam version on 2020-06-18.
- Platform or physical form: real-time third-person, two-human cooperative
  action-adventure segment on Windows; only local `Cell Breach` is scoped.
- Puzzle family: physics and object manipulation; real-time system pressure;
  inventory and fixture dependencies; agent routing and coordination; ordered
  dependency sequencing.
- Primary and official sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/1222700/A_Way_Out/),
    for the current Windows product, local and online split-screen, Remote Play
    Together, full-controller support, developer, publisher and release data.
  - **[P2]** [official EA co-op design article](https://www.ea.com/ea-originals/news/coop),
    for co-op-only play, couch/online split-screen, the non-drop-in structure
    and the Leo/Vincent character boundary.
  - **[P3]** [official EA Friend Pass article](https://www.ea.com/games/unravel/news/a-way-out-friends-pass),
    for the two-player requirement, full-copy host, invitation flow and the
    online path excluded from this local packet.
  - **[P4]** [official EA release announcement](https://news.ea.com/press-releases/press-releases-details/2018/Experience-a-Daring-Story-Driven-Adventure-With-a-Friend-in-A-Way-Out-Available-Worldwide-Today/default.aspx),
    for the release date, Windows origin and fixed Leo/Vincent cooperation.
  - **[P5]** [official EA Windows manual](https://eaassets-a.akamaihd.net/eahelp/manuals/awo-manuals_pc_en.pdf),
    for local and online session entry, player/character selection and Continue
    from saved progress.
  - **[P6]** [EA staff checkpoint response](https://forums.ea.com/discussions/ea-originals-discussion-en/re-a-way-out-is-it-possible-to-save-2-different-games-to-progress-in-pararell/7564701),
    for automatic save/checkpoint retention and later chapter selection.
- Reproducible mechanics sources:
  - **[S1]** [SteamDB public depots](https://steamdb.info/app/1222700/depots/),
    for public Build `13095794` and its branch timestamps.
  - **[S2]** [Prima Games written Escape walkthrough](https://primagames.com/news/a-way-out-chapter-1-escape),
    for Fred's delivery, the two fixture sequences, lookout duty, chisel
    handoff, role exchange and departure after lights-out.
  - **[S3]** [Gameranx written Escape walkthrough](https://gameranx.com/features/id/144005/article/a-way-out-walkthrough-part-1-escape/),
    for the named `Cell Breach` boundary, two patrols, cancellation before
    inspection, immediate failure and the Leo-to-Vincent handoff.
  - **[S4]** [Neoseeker written Cell Breach walkthrough](https://www.neoseeker.com/a-way-out/walkthrough/Cell_Breach),
    for the same ordered interactions, chisel transfer, guard observation and
    both players' post-work cell exit.
- Claim IDs: `AWO-001`–`AWO-009`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: each human directly moves one prisoner inside the cell
  and through the completed opening; existing `ACT-341`: the current worker
  commits legal interactions with the toilet, fasteners, panel, bars and exit.
- New `ACT-398`: the current carrier explicitly passes the one cooperative
  chisel to the reachable partner instead of duplicating it or changing both
  players' inventories remotely.
- Parameters: Leo/Vincent assignment, controller, fixture stage, prompt,
  interaction duration, cancellation, chisel carrier, handoff position and
  receiving partner.
- Claim IDs: `AWO-004`–`AWO-007`.

### System Behaviour Genes

- Existing `SYS-045`: both guards advance through the cell-block inspection
  route without a player command for each step; existing `SYS-369`: detection
  failure restores the authored Story checkpoint rather than retaining the
  exposed attempt.
- New `SYS-733`: accepted fixture interactions retain an ordered local sequence
  of removed toilet, released fasteners, opened panel and cut bars; the accepted
  chisel handoff preserves Leo's completed opening, transfers exclusive tool
  ownership to Vincent and enables the same sequence for his separate fixture.
- Resolution order: accept movement or interaction input; advance guards;
  compare exposed work with current inspection; fail and restore or retain the
  completed local fixture stage; validate and resolve the chisel handoff;
  validate both openings and both departures; retain the next story checkpoint.
- Claim IDs: `AWO-004`–`AWO-009`.

### Constraint Genes

- Existing `CON-077`: an inspection failure depends on a guard's current
  directed view into the cell rather than global knowledge; existing
  `CON-378`: exactly two independently controlled human participants are
  required.
- New `CON-567`: the cooperative tool may have only one current carrier and can
  pass only through the authored adjacent-partner handoff while the receiver is
  eligible; new `CON-568`: an exposed concealed-work channel must be cancelled
  before a guard's inspection reaches the worker, or the attempt fails.
- Scarce strategic resources: one chisel, two uncompleted personal fixture
  sequences, both humans' attention, current guard windows and the time needed
  to cancel and conceal the active operation.
- Claim IDs: `AWO-001`, `AWO-004`–`AWO-007`.

### Information Genes

- Existing `INF-001` exposes current prompts, fixture state, chisel ownership,
  guard approach and failure/save feedback; `INF-167` exposes both live panes
  concurrently, so either player can read the partner's work and lookout view.
- Exact future guard timing beyond current observation, later escape geometry
  and online network state do not enter the packet.
- Claim IDs: `AWO-004`–`AWO-009`.

### Objective Genes

- Existing `OBJ-086` requires both human-owned protagonists to complete the
  finite authored Cell Breach packet and reach its retained post-cell story
  boundary together.
- One completed fixture sequence, the chisel handoff, lights-out or one exited
  character is intermediate; both exits plus the cleared retained checkpoint
  define positive completion.
- Claim IDs: `AWO-007`–`AWO-009`.

### Time Genes

- Existing `TIM-003`: guard movement, inspection windows and contextual work
  unfold in continuous time while the two players provide live input.
- Claim IDs: `AWO-004`–`AWO-007`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fred's book delivery has ended and Leo holds the chisel | Leo moves the toilet and commits the first compatible fixture prompt | The fixture advances to its next authored state while Vincent remains independently controlled | exact entry and staged contextual work | `AWO-003`, `AWO-004` |
| Leo is working and a guard approaches his current inspection window | Leo cancels and conceals the operation before the guard looks inside | Completed stages remain, the exposed channel closes and the attempt continues | interruptible concealment boundary | `AWO-005` |
| Leo keeps the forbidden operation exposed through inspection | Let the guard reach the cell view | The attempt fails and the authored checkpoint is restored | negative terminal and directed observation | `AWO-005` |
| Leo's personal opening is complete and Vincent is adjacent | Leo commits the partner handoff; Vincent accepts the chisel | Leo loses tool ownership, Vincent gains it and Leo's completed fixture state remains | exclusive tool transfer and operational role exchange | `AWO-006` |
| Vincent holds the chisel while his opening is incomplete | Vincent performs the same ordered fixture work while Leo watches | Vincent's separate sequence advances without reopening Leo's finished state | retained sequential partner work | `AWO-004`, `AWO-006` |
| Both openings are complete | Wait for lights-out, then move both characters through their own openings | Both bodies leave the visible cells and the story advances | joint authored gate | `AWO-007` |
| The post-cell autosave indicator appears | Wait for it to clear, return cleanly to the menu and inspect Continue or Chapter Select | The reached post-cell state remains selectable; otherwise the run is rejected | explicit retained positive terminal | `AWO-008`, `AWO-009` |

## Strategic and experiential structure

- Planning horizon: identify which guard will inspect next, reserve enough time
  to cancel, advance only a safe fixture stage and prepare the single handoff
  after Leo's opening is complete.
- Local tactics: the lookout tracks both approach directions; the worker avoids
  starting a long interaction late in a window and stops before visibility,
  while both players use the simultaneous panes to confirm the same threat.
- Long-term structure: repeated work/hide windows teach the inspection grammar;
  transferring the chisel swaps duties without resetting the first opening;
  both exits then convert local progress into retained story progress.
- Reversible versus irreversible: an active work channel can be cancelled;
  completed fixture stages persist inside the attempt; failure restores the
  checkpoint; the cleared post-cell autosave is retained across menu return.
- Failure attribution: guard position, the worker's exposed animation, both
  panes, contextual prompts and retry feedback distinguish late cancellation,
  wrong carrier, incomplete fixture state and missing partner exit.
- Player trust: the second human is not an AI follower. Each player owns a
  separate cell sequence, and the unique chisel plus two live viewpoints make
  coordination inspectable without importing later cinematic variety.

## Replay and variation

- What changes: human-to-character assignment, warning cadence, how much work
  fits each patrol window and cancellation timing.
- Randomness or procedural generation: none established in the scoped authored
  segment; the guard sequence and fixtures belong to the fixed story route.
- Multiple viable strategies: players can use conservative short work windows
  or risk longer ones, but Leo-to-Vincent tool order and the final joint exit
  are authored.
- Typical replay motive: swap Leo/Vincent control or improve coordination; the
  rest of the campaign is a separate research scope.

## Adjacent systems and history

- Direct successors: It Takes Two and Split Fiction retain Hazelight's
  mandatory two-human split-screen form but give both roles different scoped
  tools or chapter abilities.
- Similar games: Keep Talking and Nobody Explodes splits authoritative rules
  and object state between roles; Portal 2 uses two human-controlled bodies and
  authored cooperative gates.
- Important differences: Cell Breach uses one exclusive transferable tool and
  sequentially exchanged worker/lookout duties under failure-causing patrol
  inspection. It Takes Two fixes complementary hammer and nail ownership;
  Split Fiction more often admits paired prompts, traversal and temporary
  pilot/gunner authority.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-341`, `ACT-398` | direct movement, fixture interaction and partner tool pass |
| System Behaviour | `SYS-045`, `SYS-369`, `SYS-733` | guard locomotion, failure restoration and retained staged handoff |
| Constraint | `CON-077`, `CON-378`, `CON-567`, `CON-568` | directed inspection, two humans, one carrier and timely concealment |
| Information | `INF-001`, `INF-167` | visible local state and concurrent partner pane |
| Objective | `OBJ-086` | jointly reach the retained post-cell boundary |
| Time | `TIM-003` | continuous guards and work windows |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `227` (`GAME-0001`–`GAME-0227`).
- Exact genome matches: none.
- Tied near matches: `GAME-0157` — Split Fiction (`6 / 24 = 0.250000`).
- Supported combination subsets: `COMB-0226`.
- Scan date: 2026-09-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0157` — Split Fiction | `ACT-008`, `CON-378`, `INF-001`, `INF-167`, `OBJ-086`, `TIM-003` | Both require two human-controlled protagonists, simultaneous partner panes, direct live movement and one bounded cooperative terminal. Split Fiction centres paired prompts, live traversal/combat, temporary pilot/gunner authority and individual-return/pair-reset recovery. A Way Out instead advances two staged cell fixtures under autonomous directed inspections, restores the attempt when forbidden work is seen and preserves the first opening while one exclusive chisel passes to the second worker. | Near, `0.250000` |

### Preserved research notes

- New genes: `ACT-398`, `SYS-733`, `CON-567`, `CON-568`.
- Reused genes: `ACT-008`, `ACT-341`, `SYS-045`, `SYS-369`, `CON-077`,
  `CON-378`, `INF-001`, `INF-167`, `OBJ-086` and `TIM-003`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: generic movement, authored-object interaction,
  autonomous patrol, directed inspection, checkpoint restoration, two-human
  split view and cooperative chapter completion retain existing boundaries.
  New records isolate only the explicit cooperative-tool pass, its retained
  staged state, exclusive carrier gate and inspection-time interruption.

## Taxonomy impact

- Registry changes: `ACT-398`, `SYS-733`, `CON-567`, `CON-568`; existing
  records gain A Way Out evidence only.
- Taxonomy-change record: none; no prior signature or lifecycle changes.
- Candidate terms affected: cooperative-tool handoff, exclusive carrier,
  sequential fixture state, lookout window and concealed-work interruption.

## Negative results

- `CON-076` is rejected: Leo and Vincent do not have different intrinsic tool
  permissions in Cell Breach; the one chisel changes carrier and the duties
  exchange.
- `ACT-187` is rejected: couch conversation has no bounded in-game team channel
  and is not required to represent the split-pane information relation.
- `SYS-429` and `SYS-430` are rejected: guard detection fails the authored
  attempt; this segment does not establish the individual-return/pair-wipe
  recovery boundary used by the later Hazelight games.
- Later wrench, fan, chase, fight, vehicle and campaign systems are excluded
  rather than unioned into one A Way Out genome.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] A Way Out є обов'язковою кооперативною грою для
  двох людей із постійним поділом екрана й автоматичним збереженням
  (`AWO-001`, `AWO-002`, `AWO-008`).
- [Observation | Corroborated | High] У `Cell Breach` один різець послідовно
  переходить від Лео до Вінсента, а робота триває лише поза оглядом патрулів
  (`AWO-003`–`AWO-007`).

## Нові гени

- [Observation | Corroborated | High] `ACT-398`, `SYS-733`, `CON-567`,
  `CON-568`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0226`.

## Зміни таксономії

- [Observation | Corroborated | High] Змін життєвого циклу чи сигнатур раніше
  перевірених ігор немає.

## Нові питання

- Чи використовує пізніша bounded сцена інший унікальний предмет для
  послідовної зміни обов'язків без додавання всієї кампанії?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0229` — No Man's Sky.
- Optimisation criterion: перейти від заданого двоосібного стелс-сегмента до
  одного свіжого Normal tutorial packet у процедурному світі.
- Expected information gain: перевірити видобування, ремонт, підтримання життя,
  випадковий старт і ранній збережений tutorial terminal.
- Backlog impact: продовжити активний Goal, не починаючи `GAME-0229` у цьому
  unit.

## Чому саме вона

- [Hypothesis | Limited | High] Це наступна записана гра Batch 011 і найбільша
  зміна від фіксованої камерної кооперації до процедурного survival-onboarding.
