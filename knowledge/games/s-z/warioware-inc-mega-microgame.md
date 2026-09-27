---
game_id: GAME-0398
slug: warioware-inc-mega-microgame
game_title: 'WarioWare, Inc.: Mega Microgame$!'
analysis_status: reviewed
reviewed: 2026-09-25
combination_ids: []
gene_ids:
  action:
    - ACT-534
  system:
    - SYS-004
    - SYS-1061
    - SYS-1062
    - SYS-1063
  constraint:
    - CON-068
    - CON-183
  information:
    - INF-397
  objective:
    - OBJ-234
  time:
    - TIM-003
---

# Game: WarioWare, Inc.: Mega Microgame$

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). A particular
microgame's picture, prompt, input mapping and seconds are parameters, not
automatically separate genes.

## Analysis scope

- Version / ruleset: the original 2003 North American English Game Boy
  Advance release (`AGB-AZWE-USA`), not the PAL *Minigame Mania* title or a
  later compilation. Nintendo's official PAL booklet establishes the
  shared introductory controls and course structure; two contemporary
  North American written guides supply the more specific opening-course
  route. Their exact binary equivalence is not asserted.
- Structured analysis target: original North American GBA cartridge; see
  `GAME-0398` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: first ordinary control of Wario's introductory course after the
  initial name entry, before the first microgame appears.
- Primary decision loop: read each newly shown imperative and its very short
  bomb countdown, infer the local A-button or D-pad response, perform it
  before expiry, then read the immediate clear/fail result. The course
  selects another eligible microgame without returning to a menu, debits a
  life on failure, and periodically accelerates. The tenth slot is the
  authored Sparring Wario boss rather than another ordinary random draw.
- Positive terminal: clear the tenth boss while a life remains and observe
  the opening course's completion/next-course availability. This is not a
  claim of finishing all 200-plus microgames or the full game.
- Negative terminal: four failed microgames exhaust the visible four-life
  stock and end this course attempt before its positive terminal. Individual
  timeout is a failed microgame, not a direct whole-course Game Over while
  lives remain.
- Included: the introductory pool and scheduled boss; brief visible task
  instructions and bomb countdown; context-dependent A/D-pad responses such
  as jumping one oncoming car or steering through a short passage; local
  binary clear/fail; random pool selection; continuous course handoff;
  four lives; course-progress feedback; speed increases before the boss.
- Excluded: the other character courses, every possible microgame, later
  difficulty/level variants, unlock collection, two-player or unlockable
  modes, endless score competition, sound tests, saves, adaptations and
  later rereleases. No exact random weights, frame windows or boss timing
  are asserted. The specific introductory microgames can be drawn in a
  different order; this packet covers their shared course rules and a
  reproducible example response, not one fixed random sequence.
- Reproducible parameterisation: start the original North American GBA
  release from a fresh profile, enter Wario's opening course, record each
  instruction, selected microgame, control input, countdown, result, life
  stock, speed cue, slot and boss result through either course clear or
  four failures. Repeat to distinguish pool variation from fixed tenth-slot
  scheduling. Do not infer probability weights from one run.
- Potential scoped modules: one later character course with its own
  mechanics, level variants, or the full unlocked-course progression.
- Direct-play status: none. No cartridge, emulator binary, input trace,
  screenshot, video or audio was inspected. The official booklet and two
  contemporary written guides support a source-bounded reconstruction.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `WW-001` | The original North American GBA release and PAL-titled manual refer to the 2003 game family, but their exact binaries are not established as identical. | Observation | Corroborated | High | P1, P2, S1 |
| `WW-002` | The introduction presents successive very short microgames with a brief imperative and countdown; A and D-pad inputs have task-specific effects. | Observation | Corroborated | High | P1, S1, S2 |
| `WW-003` | Eligible ordinary introductory microgames vary by selection; the tenth position is the boss rather than a normal random draw. | Observation | Corroborated | High | P1, S1, S2 |
| `WW-004` | A failed or expired microgame costs a life; four lost lives end the course attempt, whereas an earlier failure permits the next microgame. | Observation | Corroborated | High | S1, S2 |
| `WW-005` | The opening course has speed-up cues during its ten-slot sequence; the two written routes place them after early progress rather than claiming a universal schedule. | Observation | Corroborated | Medium | S1, S2 |
| `WW-006` | Jumping the one approaching car in Crazy Cars and steering in Diamond Dig are examples of distinct local responses, not simultaneous minigames. | Observation | Corroborated | High | S2 |
| `WW-007` | Neither exact draw weights, frame-perfect input windows nor boss clock semantics were directly measured. | Observation | Limited | High | R1 |

## Basic data

- Release / origin: Nintendo and Intelligent Systems' original North
  American GBA *WarioWare, Inc.: Mega Microgame$!* release in 2003. The
  official European booklet uses *WarioWare, Inc.: Minigame Mania*.
- Platform or physical form: Game Boy Advance cartridge and D-pad/A-button
  controls; structured target `PLAT-GAME-BOY-ADVANCE`.
- Puzzle family: real-time system pressure (`FAM-010`).
- Original publisher manual, checked 2026-09-25: **[P1]**
  [Nintendo's Game Boy Advance manual PDF](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/game_boy_advance_8/Manual_GameBoyAdvance_WarioWareIncMinigameMania_EN_DE_FR_ES_IT.pdf),
  English booklet pp. 8–9 and 18–19. Its PAL title and scanned text are
  stated; it is not a second North American executable witness.
- Publisher product description, checked 2026-09-25: **[P2]**
  [Nintendo's official WarioWare page](https://www.nintendo.com/en-gb/Games/Game-Boy-Advance/WarioWare-Inc-Minigame-Mania-267607.html).
- Contemporary written original-game guide, checked 2026-09-25: **[S1]**
  [Shdwrlm3's North American GBA guide](https://gamefaqs.gamespot.com/gba/589714-warioware-inc-mega-microgame/faqs/22353),
  covering intro, life display, course flow and speed.
- Independent contemporary written route, checked 2026-09-25: **[S2]**
  [MoonSaultKid's North American GBA guide](https://gamefaqs.gamespot.com/gba/589714-warioware-inc-mega-microgame/faqs/24737),
  detailing the first ten-slot course and named task examples.
- **[R1]** Boundary and direct-play audit in this record. Claim IDs:
  `WW-001`–`WW-007`.

## Mechanical decomposition

### Action Genes

- `ACT-534` commits the response required by the currently shown microgame.
  Pressing A to jump over one car and using D-pad direction to steer are
  alternative task instances, not a persistent avatar-navigation campaign.
  Claims: `WW-002`, `WW-006`.

### System Behaviour Genes

- `SYS-004` chooses ordinary tasks from the eligible introductory pool.
  `SYS-1061` hands one microgame to the next and schedules the boss at the
  declared position; `SYS-1063` settles each local clear/fail before the
  handoff. `SYS-1062` increases the pace at course milestones. Claims:
  `WW-002`–`WW-005`.
- Resolution order: disclose instruction and timer; accept the task-specific
  response while time advances; settle clear or failure; debit a life only
  on failure; stop if the stock is exhausted; otherwise continue at current
  pace, with a speed cue at a milestone or boss at the tenth slot.

### Constraint Genes

- `CON-068` bounds each ordinary microgame by its short deadline; expiry
  fails that microgame. `CON-183` carries the finite four-life stock across
  the course. The timeout and course-loss boundaries are deliberately
  distinct. Claims: `WW-002`, `WW-004`.
- Scarce resource: lives and seconds of local reaction time, not a shared
  currency or inventory.

### Information Genes

- `INF-397` shows the current imperative, countdown and course feedback
  needed to distinguish the active task from the remaining chance stock.
  It does not reveal the next random draw. Claims: `WW-002`–`WW-004`.

### Objective Genes

- `OBJ-234` requires clearing the scheduled boss to complete the introductory
  course. Clearing one ordinary task is only local progress. Claims:
  `WW-003`, `WW-004`.

### Time Genes

- `TIM-003` keeps the bomb countdown and task state running while the
  player interprets and responds; there is no turn-based pause between
  observation and action. Claims: `WW-002`, `WW-005`.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Crazy Cars instruction and one car are visible; timer is live | Press A to jump before contact | The character clears the car and the task reports success | context-dependent timed response | `WW-002`, `WW-006` |
| Ordinary task is unresolved and time reaches zero | No successful response | That task fails and one life is removed; the course continues if lives remain | local deadline differs from whole-run loss | `WW-004` |
| A task clears before the tenth slot and lives remain | Wait for handoff | Another eligible ordinary microgame appears; later pace cues shorten reaction opportunity | selected chain with acceleration | `WW-003`, `WW-005` |
| Tenth slot is reached with a life remaining | Resolve Sparring Wario successfully | Introductory course completes and its successor becomes available | fixed boss-gated terminal | `WW-003` |
| Fourth life is lost before the boss clear | Continue attempt | Course attempt ends unsuccessfully | finite chance stock | `WW-004` |

## Strategic and experiential structure

- Local decision: immediately identify which simple response the new prompt
  demands, then time that response before the bomb expires.
- Medium-term planning: preserve the shared life stock across unrelated
  short tasks; the player cannot guarantee which ordinary one appears next.
- Long-term structure: the accelerated chain ends in a designated boss.
- Failure attribution: the prompt, timer, result and life indicator expose
  local missed action and cumulative risk; exact frame tolerance is unknown.

## Replay and variation

- Ordinary task selection and exact player responses vary. The opening
  course's boss placement and four-life gate remain the declared structure.
- Random weights, complete draw history and later level variants were not
  measured or imported into this signature.

## Adjacent systems and history

- PaRappa's first lesson also requires fast interpretation of audiovisual
  cues, but it asks for a demonstrated beat-aligned phrase and maintains
  an ordinal live rap rating. This packet instead switches to independently
  settled, brief commands with a finite life stock and scheduled boss.
- Mario Party 2 also chains minigames, but between-game board turns, Coins
  and Stars are not part of Wario's introductory course.

## Normalised genome

| Type | Active genes | Parameters outside signature |
|---|---|---|
| Action | `ACT-534` | displayed task, A/D-pad mapping and response instant |
| System | `SYS-004`, `SYS-1061`, `SYS-1062`, `SYS-1063` | eligible pool, order, pace milestones and result cue |
| Constraint | `CON-068`, `CON-183` | seconds, four lives and local expiry |
| Information | `INF-397` | imperative, countdown and life display |
| Objective | `OBJ-234` | tenth-slot boss and successor |
| Time | `TIM-003` | continuous countdown and speed |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `397` (`GAME-0001`–`GAME-0397`).
- Exact genome matches: none.
- Tied near matches: `GAME-0376` — Katamari Damacy REROLL (`2 / 16 = 0.125000`).
- Supported combination subsets: none.
- Scan date: 2026-09-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0376` — Katamari Damacy REROLL | Both packets use `CON-068` for a local deadline and `TIM-003` for continuous time. | Katamari sustains one growing ball in a size-gated level and finishes at a size threshold; WarioWare replaces the whole task after each binary result, keeps a four-life stock, accelerates and schedules a boss. The shared clock does not imply shared movement, object growth or goals. | Near, `2 / 16 = 0.125000` |

## Taxonomy impact

- Six new Active genes (`ACT-534`, `SYS-1061`–`SYS-1063`, `INF-397`,
  `OBJ-234`) are bounded by `TAXONOMY_CHANGE_136`; no older signature or
  verified combination changes.

## Negative results

- `ACT-223` presumes a telegraphed hostile attack; many opening tasks are
  not attacks. `ACT-533` presumes an instructor phrase and beat-aligned
  echo. Neither is a general imperative-driven five-second response.
- `INF-067` requires a promised task reward and threat disclosure, which
  the one-word microgame prompt does not supply. `SYS-004` alone selects an
  identity but does not settle and hand off a linked course.
- No exact random weights or direct cartridge observations are claimed.

## Delta summary

## New facts

- [Observation | Corroborated | High] `WW-002`–`WW-004` distinguish a
  microgame's short deadline from the four-life course result.

## New genes

- [Observation | Corroborated | High] Six course-specific distinctions are
  admitted with the transfer tests in `TAXONOMY_CHANGE_136`.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_136` adds six Active
  genes and changes no older signature.

## New questions

- Which exact introductory draw weights and frame windows occur in a
  directly inspected North American cartridge?
- How do later character courses change the ordered result structure?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0399` *Ico* in the selected horizon.
- Optimisation criterion: contrast immediate handheld microtasks with a
  persistent PlayStation 2 companion-and-environment route.
- Expected information gain: companion state and traversal gates.
- Backlog impact: one next game unit, not an implicit start.

## Why this game

- [Hypothesis | Limited | Medium] The series is iconic for rapid rule
  switching; the bounded course tests whether the Atlas can represent
  nested local results without mistaking them for full-game wins.
