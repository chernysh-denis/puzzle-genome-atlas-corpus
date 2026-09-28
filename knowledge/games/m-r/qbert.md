---
game_id: GAME-0438
slug: qbert
game_title: Q*bert
analysis_status: reviewed
reviewed: 2026-09-28
combination_ids: []
gene_ids:
  action:
    - ACT-008
  system:
    - SYS-004
    - SYS-030
    - SYS-045
    - SYS-1148
    - SYS-1149
    - SYS-1150
    - SYS-1151
  constraint:
    - CON-001
    - CON-183
  information:
    - INF-001
  objective:
    - OBJ-004
  time:
    - TIM-003
---

# Game: Q*bert — original arcade Level I, Round 1

Use the [canonical vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Character names, cube colours, point awards, pyramid size and disc positions are parameters, not standalone genes.

## Analysis scope

- Version / ruleset: Gottlieb's original 1982 `GV-103A` arcade *Q*bert*, Level I Round 1, as described in its original instruction manual. Later rounds, console adaptations and remakes are not assumed equivalent. The manual is primary written evidence, not a directly played executable or measured arcade-board revision.
- Structured analysis target: `PLAT-ARCADE-CABINET` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: choose one of four diagonal hops between fixed pyramid cubes; each landing advances that cube top toward the displayed destination colour. Route to unfinished cubes while randomly arriving red and purple balls descend; the purple one hatches into Coily, which pursues the player. Avoid hostile contact and fatal off-pyramid jumps, or lure Coily over an edge while riding a side disc back to the summit. Change every cube top to the target colour to clear the round.
- Entry: start of Level I Round 1, with Q*bert on the top cube before the first directional hop and all cube tops in their starting state.
- Positive terminal: all cube tops have reached the designated colour, so the arcade game advances to the next round and returns the player to the top. Only that first-round clear is analysed.
- Negative terminal: off-pyramid or hostile contact spends a life; after the finite life stock is depleted, the whole arcade attempt ends. A single lost life is a recoverable local failure, not the bounded round's desired exit.
- Included: four-direction diagonal hops; fixed cube layout; landing-driven cube-top changes; current visible tile and hostile state; time-driven random ball arrival and descent; purple-ball transition into chasing Coily; deadly contact; disc-to-summit escape that can eliminate Coily; finite lives; whole-pyramid target-colour completion.
- Excluded: Level I Rounds 2–4, later multi-visit cube rules, Slick and Sam undoing colour progress, green freeze balls, Ugg and Wrong-Way, score thresholds for extra lives, exact random distributions, exact speed schedules, two-player alternation, attract-mode instruction demo, ports, remakes and complete-game progression. Coily's 500-point lure bonus is a documented consequence, not the selected objective.
- Reproducible parameterisation: on an original arcade ruleset at Level I Round 1, hop diagonally onto unconverted cube tops and observe their changes. Watch red and purple balls enter near the upper pyramid and descend; wait for the purple ball to hatch into Coily, then route away from his pursuit. At an edge where a disc remains, hop onto it to return to the top and, if Coily follows over that edge, remove him. Continue until all cube tops display the target colour or the life stock is exhausted. Exact spawn timing, Coily path tie-breaking and score-to-life thresholds were not measured.
- Potential scoped modules: later-round colour cycling and reversal, green-ball freeze, sideways hostiles, full four-round level progression and operator-adjusted life/score settings.
- Direct-play status: no cabinet, original arcade PCB, joystick input trace, screenshot, video or audio was inspected. The original Gottlieb instruction manual is the primary written source, checked through an accessible OCR mirror; character behaviour, first-round enemy classes and disc rule are direct manual claims. The illustration is an original interpretive depiction, not a captured game state.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `QB-001` | The joystick makes Q*bert hop between pyramid cubes in four diagonal directions; jumping off the pyramid is fatal. | Confirmed | Direct | High | P1 |
| `QB-002` | Landing on cube tops changes them toward the designated colour; converting every cube top advances to the next round with Q*bert at the summit. | Confirmed | Direct | High | P1 |
| `QB-003` | In the first two rounds, red and purple balls arrive unpredictably, bounce downward and are deadly to touch; red balls leave at the bottom while the purple ball hatches into pursuing Coily. | Confirmed | Direct | High | P1 |
| `QB-004` | Hopping onto a rotating side disc returns Q*bert to the summit; luring Coily over the edge during this escape destroys him and awards points. | Confirmed | Direct | High | P1 |
| `QB-005` | Lives form a finite operator-adjustable stock; an extra Q*bert can be earned at configured score levels. | Confirmed | Direct | High | P1 |
| `QB-006` | Green freeze balls, Slick, Sam, Ugg and Wrong-Way begin in later rounds and are absent from this first-round packet. | Confirmed | Direct | High | P1 |

## Basic data

- Release / origin: Gottlieb *Q*bert*, original `GV-103A` arcade manual, copyright 1982. The exact cabinet software revision was not inspected.
- Platform or physical form: joystick-controlled coin-operated arcade cabinet; one bounded first round.
- Mechanical families: state transformation (`FAM-003`) through cube-top changes toward one target configuration; real-time system pressure (`FAM-010`) from moving balls and Coily.
- **P1**: [Gottlieb original *Q*bert* instruction manual, `GV-103A`](https://arcarc.xmission.com/PDF_Arcade_Manuals_and_Schematics/Q-Bert_Instruction_Manual_%2811-82%29.pdf), section IV, "How to Play" and game-operation lives settings (1982; accessed 2026-09-28 through the [searchable scan transcription](https://manualzz.com/doc/8559673/gottlieb-q-bert-arcade-game-instruction-manual)). The OCR alters the printed character name in places, so rule claims are based on the surrounding passages rather than its corrupted glyphs.
- Claim IDs: `QB-001`–`QB-006`.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: one directional joystick input advances Q*bert to one adjacent cube along a diagonal; this is direct agent navigation, not remote path assignment (`QB-001`).

### System Behaviour Genes

- Add `SYS-1148`: each valid cube-top landing advances only that addressed top toward the current round's designated colour. This changes persistent board progress rather than merely tinting a sprite (`QB-002`).
- Reuse `SYS-030` and `SYS-004` for time-driven arrival and the manual's unpredictable red/purple ball outcomes, then `SYS-045` for their automatic downward motion. Add `SYS-1149` for the purple ball's distinct bottom-row hatch into a pursuer rather than simply departing like a red ball (`QB-003`).
- Add `SYS-1150`: Coily's subsequent autonomous hops react to Q*bert's current route rather than following a fixed falling-ball path. Generic `SYS-045` carries motion, but not the change of target from an independently navigated avatar (`QB-003`).
- Add `SYS-1151`: an eligible side-disc hop carries Q*bert to the summit; a pursuing Coily can instead continue over the unoccupied edge and be removed. The manual does not establish whether that exact disc may be reused after the ride (`QB-004`).
- Resolution order: a directional hop lands on a cube, changes its top if eligible and then tests full-board completion; meanwhile ball arrival and movement continue on the running clock. Contact or a missed edge hop costs a life. A disc hop returns the avatar to the top and may remove a pursuing Coily before normal pursuit resumes.

### Constraint Genes

- Reuse `CON-001` for the fixed finite individually addressable pyramid cube positions; their top colours change but the topology does not (`QB-002`). Reuse `CON-183` for the finite stock that absorbs ordinary deaths until complete game over (`QB-001`, `QB-003`, `QB-005`).

### Information Genes

- Reuse `INF-001`: current cube-top states, avatar and currently present enemies are visible. This does not claim that the next randomly arriving ball or its arrival time is previewed (`QB-002`, `QB-003`).

### Objective Genes

- Reuse `OBJ-004`: the complete set of persistent cube tops must match the round's target-colour configuration. Points for Coily are optional to this round clear (`QB-002`, `QB-004`).

### Time Genes

- Reuse `TIM-003`: hostile arrivals and motion continue while the player can choose the next hop (`QB-003`).

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Q*bert occupies a converted cube next to an unconverted cube | Hop diagonally onto the unconverted top | The destination top changes toward the designated colour; other tops remain as they were | addressed landing-state change | `QB-001`, `QB-002` |
| One unconverted cube remains and no enemy occupies it | Land on that cube | Its top becomes the target colour, all tops now match, and the next round starts at the summit | whole-board terminal, not score maximisation | `QB-002` |
| A red ball and purple ball are falling | Keep hopping while they descend | Red can leave the bottom; purple stops there and hatches into Coily | distinct actor transition | `QB-003` |
| Coily is pursuing near the edge and a side disc is available | Hop from the edge onto the disc | Q*bert returns to the summit; a following Coily falls off and is removed | disc escape and pursuer lure | `QB-004` |
| A hop targets empty space off the pyramid or meets a deadly ball | Commit or fail to avoid that contact | One life is lost; play can continue while lives remain | recoverable life boundary | `QB-001`, `QB-003`, `QB-005` |

## Strategic and experiential structure

- Local decision: prefer an unconverted reachable cube while leaving a safe next hop as balls descend.
- Medium-term plan: route through remaining tops without trapping Q*bert at an edge; use a disc to reset position and remove Coily if the pursuit alignment permits it.
- Long-term boundary: convert the whole first-round pyramid before exhausting lives. Later rounds change rules and are not silently imported.
- Failure attribution: the manual distinguishes wrong edge input, deadly contact and optional disc rescue, but exact timings and path tie-breaks were not measured.
- Player trust: currently visible cube progress and actors support local avoidance; future stochastic arrivals remain unknown.

## Replay and variation

The pyramid positions and target are fixed for this first round, while the manual describes unpredictable ball arrivals. Different hop routes, disc use and losses therefore vary the attempt without changing the round-clear rule. No exact probability distribution is asserted.

## Adjacent systems and history

*PAC-MAN* (`GAME-0342`) also has visible current state, continuous hostile movement and finite lives, but clears a maze by collecting Pac-Dots under role-specific timed ghost modes. Q*bert instead changes fixed cube tops on landing and has a disc-triggered Coily lure.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-008` | four diagonal hops |
| System Behaviour | `SYS-004`, `SYS-030`, `SYS-045`, `SYS-1148`, `SYS-1149`, `SYS-1150`, `SYS-1151` | ball class, arrival, landing colour, pursuit and disc position |
| Constraint | `CON-001`, `CON-183` | pyramid size and life stock |
| Information | `INF-001` | visible current tops and enemies |
| Objective | `OBJ-004` | all tops reach target colour |
| Time | `TIM-003` | live ball and pursuer motion |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `437` (`GAME-0001`–`GAME-0437`).
- Exact genome matches: none.
- Tied near matches: `GAME-0029` — HUMANITY (`5 / 20 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-09-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0029` *HUMANITY* | `ACT-008`, `SYS-045`, `CON-001`, `INF-001`, `TIM-003` | Both expose a fixed visible playfield, direct avatar movement and other agents advancing in real time. HUMANITY places persistent route commands to steer a recurring crowd into a quota goal, with losses ordinarily recycled. Q*bert instead changes individual cube tops on landing, must finish one target-colour configuration and navigates deadly balls, Coily pursuit and side-disc escapes. | Tied-near maximum, not an exact match (`5 / 20 = 0.250000`). |

## Taxonomy impact

`TAXONOMY_CHANGE_175` admits landing-state advance, purple-ball hatch, avatar-following pursuit and disc escape with a Coily lure. Existing direct navigation, random arrival, autonomous movement, fixed positions, visible current state, exact configuration objective, finite lives and live input are reused. No earlier signature or verified combination changes.

## Negative results

- `SYS-960` assigns PAC-MAN ghosts timed role-specific Scatter/Chase modes and forced reversals; Coily is one newly hatched pursuer without that schedule.
- `SYS-057` requires a perception-triggered hostile alert or diversion; the original manual says Coily chases Q*bert, not that he first detects sight or sound.
- `SYS-131` advances pursuers one shortest-route graph step after each player turn; this arcade round advances on a live clock and the manual does not establish shortest-path tie-breaking.
- Later-round colour reversal, freeze balls, green adversaries and sideways climbers are real rules, but not genes of this first-round packet.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original Gottlieb manual identifies a first-round loop of diagonal landings, target-colour tops and whole-pyramid clearance (`QB-001`, `QB-002`).
- [Confirmed | Direct | High] The same manual distinguishes red-ball departure, purple-ball hatch into Coily and disc-mediated snake lure (`QB-003`, `QB-004`).

## New genes

- [Observation | Direct | High] Four typed system boundaries are admitted in `TAXONOMY_CHANGE_175`.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_175`; earlier signatures remain unchanged.

## New questions

- How does the original arcade program select Coily's next hop at pursuit ties, and what are the exact Level I Round 1 ball arrival intervals?

## Next game

`GAME-0439` *Wii Fit* follows after the Goal stop window. Its exact selected activity and original hardware/ruleset require separate research.
