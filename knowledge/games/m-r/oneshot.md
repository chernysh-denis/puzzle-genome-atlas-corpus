---
game_id: GAME-0117
slug: oneshot
game_title: OneShot
analysis_status: reviewed
reviewed: 2026-08-16
combination_ids:
  - COMB-0116
gene_ids:
  action:
    - ACT-008
    - ACT-115
  system:
    - SYS-150
  constraint:
    - CON-169
  information:
    - INF-001
    - INF-056
  objective:
    - OBJ-026
  time:
    - TIM-002
---

# Game: OneShot

## Analysis scope

- Version / ruleset: 2016 PC release, bounded to one spoiler-minimised
  meta-puzzle packet: an in-world state causes the game to publish a clue in an
  intended external artefact; the player inspects it and applies the disclosed
  information to open the next route.
- Included: top-down navigation, authored external clue publication, focus
  shift / file inspection, returning to the world, applying the clue and route
  progression.
- Excluded: exact copyrighted clue contents, story ending, Solstice, irreversible
  narrative choice, full inventory chain and World Machine Edition extras.
- Direct-play status: not conducted. Future Cat's product page says the world
  knows the player exists; the developer AMA confirms puzzles beyond the window
  and the mock-OS adaptation that preserves them.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ONE-001` | OneShot is a puzzle adventure whose world recognises the player | Confirmed | Direct | High | P1 |
| `ONE-002` | Intended puzzles can require clues presented beyond the normal game window | Confirmed | Corroborated | High | P1, P2 |
| `ONE-003` | World Machine Edition preserves the boundary through a mock operating system | Confirmed | Direct | High | P1, P2 |

## Basic data

- Release / origin: Future Cat released the commercial OneShot in 2016.
- Platform or physical form: top-down puzzle adventure with host-interface interaction.
- Puzzle family: rule and interface manipulation; knowledge progression.
- Primary sources: **[P1]** [OneShot on Steam](https://store.steampowered.com/app/420530/One_Shot/);
  **[P2]** [Future Cat developer AMA](https://www.reddit.com/r/Games/comments/1fj9asf/ama_were_the_devs_of_oneshot_and_were_bringing/).
- Claim IDs: `ONE-001`–`ONE-003`.

## Mechanical decomposition

### Action Genes

- `ACT-008` navigates Niko; `ACT-115` inspects the intended external artefact.
- Candidate genes: none.
- Claim IDs: `ONE-002`, `ONE-003`.

### System Behaviour Genes

- `SYS-150` publishes or updates a clue through the host or mock-OS surface.
- Resolution order: reach trigger; publish clue; inspect; return; apply.
- Claim IDs: `ONE-002`, `ONE-003`.

### Constraint Genes

- `CON-169` withholds the required answer from ordinary world presentation.
- Scarce strategic resources: player attention across two interface layers.
- Claim IDs: `ONE-002`.

### Information Genes

- `INF-001` exposes current world state; `INF-056` exposes the authored clue in
  the external interface.
- Candidate genes: none.
- Claim IDs: `ONE-002`, `ONE-003`.

### Objective Genes

- `OBJ-026` completes the packet by opening and traversing the next route.
- Success, evaluation and failure: correct clue use opens the route; retries are self-paced.
- Claim IDs: `ONE-002`.

### Time Genes

- `TIM-002` allows unbounded inspection between world actions.
- Candidate genes: none.
- Claim IDs: `ONE-002`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Meta-puzzle trigger has not occurred | Inspect external location | Required clue is absent | authored publication gate | `ONE-002` |
| Trigger occurs in world | Shift focus and inspect | Game-authored clue is visible externally | external information channel | `ONE-002` |
| Player returns with correct information | Apply it to receiver | Route opens | cross-interface dependency | `ONE-002` |

## Strategic and experiential structure

- Local decision: recognise that the game points beyond its ordinary window.
- Medium-term planning: preserve and translate the external clue.
- Long-term structure: treat player, host and world as one puzzle system.
- Common heuristics: inspect newly changed intended artefacts after unusual prompts.
- Failure attribution: wrong answers remain visible; discovery of the channel is the main risk.
- Player-trust factors: platform equivalents must preserve discoverability.
- Claim IDs: `ONE-002`, `ONE-003`.

## Replay and variation

- What changes between sessions: knowledge; exact packet remains authored.
- Randomness or procedural generation: none in scope.
- Multiple viable strategies: no for the information channel, yes for discovery pace.
- Typical replay motive: narrative revisitation outside this packet.
- Claim IDs: `ONE-001`.

## Adjacent systems and history

- Direct predecessors: fourth-wall and desktop-interaction games.
- Variants: World Machine Edition moves the host boundary into a mock OS.
- Similar games: Tunic and The Stanley Parable.
- Important differences: the clue is a mechanically required external artefact,
  not only commentary about the player.
- Claim IDs: `ONE-002`, `ONE-003`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-115` | host or mock OS |
| System Behaviour | `SYS-150` | publication trigger |
| Constraint | `CON-169` | external clue gate |
| Information | `INF-001`, `INF-056` | artefact format |
| Objective | `OBJ-026` | route receiver |
| Time | `TIM-002` | self-paced |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `116` (`GAME-0001`–`GAME-0116`).
- Exact genome matches: none.
- Tied near matches: `GAME-0040` — Carto (`4 / 12 = 0.333333`); `GAME-0107` — The Pedestrian (`4 / 12 = 0.333333`).
- Supported combination subsets: `COMB-0116`.
- Scan date: 2026-08-16.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0040`, `GAME-0107`.

## Taxonomy impact

- Registry changes: four Active genes.
- Taxonomy-change record: none.
- Candidate terms affected: external interface artefact.

## Negative results

- `none`.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] OneShot makes an external or emulated OS
  surface a required part of the puzzle loop (`ONE-002`, `ONE-003`).

## Нові гени

- [Observation | Corroborated | High] `ACT-115`, `SYS-150`, `CON-169`, `INF-056`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0116`.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Which other games preserve this boundary without depending on the real host OS?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] pause for a nine-game batch audit.
- Optimisation criterion: verify new boundaries and exact matches before expansion.
- Expected information gain: detect over-splitting in fresh genes.
- Backlog impact: no further game is authorised in this iteration.

## Чому саме вона

- [Hypothesis | Limited | High] The full nine-game page is now ready for integrated validation.
