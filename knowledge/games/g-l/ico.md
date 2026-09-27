---
game_id: GAME-0399
slug: ico
game_title: Ico
analysis_status: reviewed
reviewed: 2026-09-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-049
    - ACT-161
    - ACT-341
    - ACT-535
  system:
    - SYS-215
    - SYS-1064
    - SYS-1065
  constraint:
    - CON-076
    - CON-621
  information:
    - INF-179
  objective:
    - OBJ-235
  time:
    - TIM-003
---

# Game: Ico

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The cage, chain,
Idol Door, couch and Yorda are parameters of the scoped route, not genes by
their proper names.

## Analysis scope

- Version / ruleset: original English North American PlayStation 2 retail
  *Ico* from 2001, on a fresh ordinary New Game. The US manual transcript
  is a primary-document transcription, not a directly inspected disc or
  verified byte-identical scan; two contemporary PS2 written routes bound
  the opening. Japanese/PAL editions, PS3 remaster and later versions are
  outside this target. Exact executable revision was not inspected.
- Structured analysis target: original North American PS2 game; see
  `GAME-0399` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: first ordinary control of Ico after the sacrificial crypt opens,
  before finding or releasing Yorda in the opening tower.
- Primary decision loop: inspect reachable windows, ladders, chains and
  levers; directly traverse to alter the cage's position and release Yorda;
  defend and retrieve her from a shadow's portal attempt; coordinate her
  different movement and gate permissions by calling, holding her hand and
  helping her onto ledges; then lead both through the first Idol Door to
  the first couch.
- Positive terminal: after Yorda opens the first Idol Door, both pass it,
  reach the first paired couch and sit together to expose the save screen.
  This is one early-route checkpoint, not the castle's final escape. A
  completed memory-card write is an optional local persistence action,
  not evidence that the full game was cleared.
- Negative terminal: a shadow completes Yorda's recapture into its portal;
  the escape attempt ends. A grab or partial drag remains recoverable. Ico's
  own lethal fall during traversal also ends the current attempt, but exact
  fall-height thresholds are not asserted.
- Included: directed 3D traversal, the lever that lowers the hanging cage,
  jumping onto that cage to break its support, the initial stick defence,
  real-time spirit pursuit and portal drag, calling and handholding Yorda,
  her position-limited movement and assisted ledge climb, her exclusive
  opening of the first Idol Door, current-room affordances and the two-person
  couch save eligibility.
- Excluded: the Old Bridge after the first couch, further doors and shadow
  variants, pressure-switch and block puzzles beyond this opening, later
  swords, bombs, full-castle escape, New Game+ differences, time-attack
  records, other releases and any invented exact combat damage, AI path,
  recovery time or fall threshold. The original manual describes some of
  those wider systems, but their presence elsewhere does not place them in
  this signature.
- Reproducible parameterisation: start a fresh original North American PS2
  New Game, record the first controllable position, cage lever state and
  lowering, cage break, Yorda's release, first shadow's grab/portal and
  recovery, stick strikes, handhold/call, each ledge both actors cross,
  first Idol Door response and both couch seats. Record disc revision,
  input trace and save-screen state if directly replayed. Source routes
  alone do not establish exact timings or every failure animation.
- Potential scoped modules: the Old Bridge and subsequent cooperative
  castle puzzles; later weapons and spirit encounters; full ending route.
- Direct-play status: none. No disc, emulator, controller trace, screenshot,
  video or audio was inspected. This is a source-bounded reconstruction from
  a transcription of the original Sony manual and two independent written
  PS2 opening routes.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `IC-001` | The original PS2 controls support direct climbing, lever use, strikes and contextual R1 companion actions. | Observation | Corroborated | High | P1, S1, S2 |
| `IC-002` | The opening tower lever lowers Yorda's cage; Ico's jump onto it breaks its support and frees her. | Observation | Corroborated | High | P1, S1, S2 |
| `IC-003` | A shadow tries to carry Yorda into a portal; Ico can intervene before completed capture. | Observation | Corroborated | High | P1, S1, S2 |
| `IC-004` | Yorda responds to call or hand contact but some ledges require Ico's assistance. | Observation | Corroborated | High | P1, S1, S2 |
| `IC-005` | Yorda can open the first Idol Door, whereas Ico cannot open it alone at this point. | Observation | Corroborated | High | P1, S1, S2 |
| `IC-006` | The first shared couch follows the first Idol Door and higher ledge; both must sit to expose saving. | Observation | Corroborated | High | P1, S1 |
| `IC-007` | Exact original-disc timing, AI trajectory, fall threshold and successful memory-card write were not directly measured. | Observation | Limited | High | R1 |

## Basic data

- Release / origin: Sony Computer Entertainment's original 2001
  PlayStation 2 *Ico*; not the 2011 PS3 remaster.
- Platform or physical form: original North American PS2 disc and DualShock 2;
  structured target `PLAT-PLAYSTATION-2`.
- Puzzle family: agent routing and coordination (`FAM-015`); the lever and
  the exclusive companion door alter a shared castle route.
- Original publisher booklet transcription, checked 2026-09-25: **[P1]**
  [North American Sony *Ico* instruction-manual transcript](https://icoshrine.neocities.org/gallery/manual_transcripts),
  pp. 4, 10, 12–14, 16–18 and 20–22. The hosting site is an independent
  transcription of a primary artefact; no scan was directly inspected.
- Contemporary original-PS2 opening route, checked 2026-09-25: **[S1]**
  [Grand_Admiral's 2002 guide](https://gamefaqs.gamespot.com/ps2/367472-ico/faqs/19202),
  first tower/cage, shadow, Idol Door, ledges and first couch.
- Independent original-PS2 written route, checked 2026-09-25: **[S2]**
  [black_hole_sun's 2002 guide](https://gamefaqs.gamespot.com/ps2/367472-ico/faqs/18667),
  opening tower, cage lever, shadow and first exit.
- Publisher chronology, checked 2026-09-25: **[P2]**
  [PlayStation's history of PS2](https://www.playstation.com/ja-jp/playstation-history/2000-ps2-psp/)
  names the original *Ico* as a PS2 title; it does not define these rules.
- **[R1]** Scope and direct-play audit in this record. Claim IDs:
  `IC-001`–`IC-007`.

## Mechanical decomposition

### Action Genes

- `ACT-008` is Ico's directly controlled movement through windows, ladders,
  chains and ledges, including the jump onto the hanging cage.
- `ACT-049` is the reachable lever that lowers the cage; this does not
  represent later pressure-switch or block puzzles.
- `ACT-161` commits stick strikes at the first materialised shadow.
- `ACT-341` covers the couch interaction after both actors arrive; the
  memory-card write itself is outside the required terminal.
- `ACT-535` is the contextual R1 call, handhold or ledge assist addressed
  to Yorda. These are different local instances of one companion-directed
  input, not direct control of her body. Claims: `IC-001`–`IC-004`, `IC-006`.

### System Behaviour Genes

- `SYS-215` resolves real-time stick attacks and hostile interference.
  `SYS-1064` moves Yorda in response to a legal call, handhold or assisted
  climb while respecting her physical route. `SYS-1065` models the first
  shadow carrying her toward the portal with a recoverable window.
- Resolution order: lever lowers cage; Ico lands on it and its support
  breaks; the released Yorda becomes vulnerable to the first shadow;
  strike or pull her back before portal capture; establish hand contact
  or call; guide her to the door and through the ledges. Claims:
  `IC-002`–`IC-005`.

### Constraint Genes

- `CON-076` keeps Ico's climbing and Yorda's Idol-Door authority distinct:
  the same path and gate are not interchangeable between actors.
  `CON-621` makes the first couch a designated save fixture whose local
  predicate requires both to sit. A save-anywhere menu is not inferred.
  Claims: `IC-004`–`IC-006`.
- Scarce strategic resource: Yorda's recoverable position and safety, not
  ammunition, coins or a countdown whose numeric length is known.

### Information Genes

- `INF-179` exposes the current tower's traversable ledges, lever, cage,
  shadow, portal, door and couch as local spatial information. It does not
  reveal concealed later rooms. Claims: `IC-001`–`IC-006`.

### Objective Genes

- `OBJ-235` requires Yorda's live presence and unique door interaction,
  then both actors at the first shared couch. Ico reaching the door alone
  does not satisfy it. Claims: `IC-005`, `IC-006`.

### Time Genes

- `TIM-003` makes shadow movement and the portal drag progress while Ico
  chooses to move, strike or rescue. The route has no claimed global
  countdown. Claim: `IC-003`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Yorda's cage hangs above the tower floor | Reach and throw the upper lever, then return and jump onto the lowered cage | The cage support breaks and Yorda is released | linked mechanism plus direct traversal | `IC-002` |
| First shadow has grabbed Yorda near its portal | Strike the materialised shadow with the stick or retrieve Yorda before completed capture | The grab/drag is interrupted and Yorda remains available | recoverable companion threat | `IC-003` |
| Yorda is free but separated from Ico | Call or take her hand within reach | She follows a reachable route instead of being directly steered | dependent response | `IC-004` |
| Ico reaches the first Idol Door without Yorda | Attempt passage alone | The gate does not open for him; bring Yorda to it | asymmetric gate authority | `IC-005` |
| The first door has opened and a ledge is too high for Yorda alone | Climb with Ico, face Yorda and use R1 | Ico pulls her to his reachable ledge; both can continue | actor-specific climb plus assist | `IC-004` |
| Both reach the first couch | Sit together | The save interface becomes available | paired checkpoint terminal | `IC-006` |

## Strategic and experiential structure

- Local decision: choose a safe route and use the appropriate context input
  while keeping Yorda close enough to respond.
- Medium-term planning: open the cage, survive the first capture attempt,
  then route two differently capable actors through the same exit.
- Long-term structure: the first couch marks only a stable early checkpoint
  before the Old Bridge, not the castle escape.
- Common heuristics: inspect upper windows before assuming the broken bridge
  can be jumped; keep Yorda near, and separate only to cross an obstacle
  that requires Ico to assist from the other side.
- Failure attribution: completed portal capture ends the attempt; a grab
  alone is recoverable. Neither exact recovery seconds nor enemy AI
  distribution is claimed.
- Player-trust factors: the camera and visible door response make the two
  actors' different route and gate roles observable. Claims: `IC-001`–`IC-007`.

## Replay and variation

- The tower geometry and gate order are authored. Player timing and how
  quickly the first shadow is intercepted can differ.
- No procedural room layout, random loot or globally fixed exact shadow
  path is inferred from the written routes.
- Replaying the route can test the recovery window and companion spacing;
  this record does not report firsthand success times. Claim: `IC-007`.

## Adjacent systems and history

- *The Last of Us Part I* also has an allied actor alongside direct avatar
  control, but its ally independently chooses local help (`SYS-407`). Here
  hand contact, calls and ledge assistance determine Yorda's movement,
  and she has exclusive Idol-Door authority.
- *Timelie* also coordinates actors with different world permissions
  (`CON-076`), but it switches among directly controlled characters and
  uses a time-revision system; Ico never directly steers Yorda.

## Normalised genome

| Type | Active genes | Parameters outside signature |
|---|---|---|
| Action | `ACT-008`, `ACT-049`, `ACT-161`, `ACT-341`, `ACT-535` | Ico, lever, stick, couch and R1 |
| System | `SYS-215`, `SYS-1064`, `SYS-1065` | shadow, follow reach and portal |
| Constraint | `CON-076`, `CON-621` | actor permissions and both seated |
| Information | `INF-179` | tower view, door and threats |
| Objective | `OBJ-235` | first Idol Door and first couch |
| Time | `TIM-003` | concurrent spirit movement |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `398` (`GAME-0001`–`GAME-0398`).
- Exact genome matches: none.
- Tied near matches: `GAME-0347` — Castlevania: Symphony of the Night (`6 / 26 = 0.230769`).
- Supported combination subsets: none.
- Scan date: 2026-09-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0347` — Castlevania: Symphony of the Night | Both packets use direct traversal and strikes (`ACT-008`, `ACT-161`), contextual fixtures (`ACT-341`), live combat (`SYS-215`), a designated save fixture (`CON-621`) and a locally visible room (`INF-179`). | Castlevania's scoped route retains equipment, relic and boss progression; Ico's early tower instead depends on Yorda's hand-led position, her exclusive gate permission and a recoverable shadow abduction. Shared basic navigation does not imply shared companion rules. | Near, `6 / 26 = 0.230769` |

### Preserved research notes

- New genes: `ACT-535`, `SYS-1064`, `SYS-1065`, `OBJ-235`.
- Classification result: New gene.
- Evidence and reasoning: existing direct traversal, switch, strike, room
  view, real-time combat, actor permissions and fixture save boundaries
  transfer. The companion-directed hand/contact response, portal drag and
  two-actor gate/checkpoint terminal do not transfer from generic escort,
  combat, door or destination genes.

## Taxonomy impact

- Four new Active genes are admitted with `TAXONOMY_CHANGE_137`; no earlier
  signature or verified combination changes.

## Negative results

- `ACT-408`/`SYS-752` require a follow/wait guard who can give autonomous
  role-specific help. Yorda instead needs hand contact or call and a pull
  at a high ledge. `SYS-407` expects independent attack or support choices.
- `OBJ-026` is direct-avatar arrival and does not require Yorda to open a
  gate and reach a paired couch. The wide manual's bombs, swords and later
  bridges are excluded by this route boundary.
- Exact original-disc timings, shadow paths and memory-card outcome remain
  unknown without direct play.

## Delta summary

## New facts

- [Observation | Corroborated | High] `IC-002`–`IC-006` establish an early
  two-actor route from cage release to the first joint checkpoint.

## New genes

- [Observation | Corroborated | High] Four dependent-companion, portal and
  joint-terminal distinctions are admitted in `TAXONOMY_CHANGE_137`.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_137` adds four Active
  genes without changing older signatures.

## New questions

- [Hypothesis | Limited | Medium] A future direct-disc trace should check
  exact rescue timing and whether every apparent high ledge in the first
  tower has the same assist predicate.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0400` *Geometry Wars: Retro Evolved*.
- Optimisation criterion: alternate the two-actor spatial route with a
  score-driven continuous twin-stick arena on Xbox 360.
- Expected information gain: bounded hostile spawning, weapon response and
  score/multiplier retention without a companion or gate.
- Backlog impact: execute only after this Goal's stop window; no implicit
  push, public publication or deployment.

## Why this game

- [Hypothesis | Limited | Medium] Ico tests whether existing coordination
  genes can represent a dependent actor whose location and unique gate
  permission are causally necessary, without turning the marketed game's
  entire castle into one oversized signature.
