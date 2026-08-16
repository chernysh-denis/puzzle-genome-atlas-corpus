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

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `ACT-008,ACT-115; SYS-150; CON-169; INF-001,INF-056; OBJ-026; TIM-002`.
- Indexed games scanned: 117, including this record.
- Indexed combinations scanned: 116.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0040` — Carto at `4 / 12 = 0.333333`; `GAME-0107` — The Pedestrian at `4 / 12 = 0.333333`.
- Supported combination subsets: `COMB-0116`.
- Scan date: 2026-08-16.

### Full prior-game Jaccard scan

- `GAME-0001`: `1 / 21 = 0.047619`; `GAME-0002`: `2 / 13 = 0.153846`; `GAME-0003`: `0 / 17 = 0.000000`; `GAME-0004`: `1 / 22 = 0.045455`.
- `GAME-0005`: `2 / 13 = 0.153846`; `GAME-0006`: `3 / 14 = 0.214286`; `GAME-0007`: `2 / 14 = 0.142857`; `GAME-0008`: `2 / 13 = 0.153846`.
- `GAME-0009`: `1 / 23 = 0.043478`; `GAME-0010`: `1 / 16 = 0.062500`; `GAME-0011`: `2 / 19 = 0.105263`; `GAME-0012`: `2 / 15 = 0.133333`.
- `GAME-0013`: `1 / 20 = 0.050000`; `GAME-0014`: `1 / 22 = 0.045455`; `GAME-0015`: `1 / 21 = 0.047619`; `GAME-0016`: `1 / 22 = 0.045455`.
- `GAME-0017`: `0 / 21 = 0.000000`; `GAME-0018`: `1 / 26 = 0.038462`; `GAME-0019`: `1 / 17 = 0.058824`; `GAME-0020`: `1 / 21 = 0.047619`.
- `GAME-0021`: `1 / 16 = 0.062500`; `GAME-0022`: `1 / 19 = 0.052632`; `GAME-0023`: `1 / 17 = 0.058824`; `GAME-0024`: `1 / 19 = 0.052632`.
- `GAME-0025`: `1 / 18 = 0.055556`; `GAME-0026`: `1 / 19 = 0.052632`; `GAME-0027`: `1 / 19 = 0.052632`; `GAME-0028`: `1 / 24 = 0.041667`.
- `GAME-0029`: `2 / 18 = 0.111111`; `GAME-0030`: `1 / 21 = 0.047619`; `GAME-0031`: `1 / 18 = 0.055556`; `GAME-0032`: `1 / 18 = 0.055556`.
- `GAME-0033`: `2 / 19 = 0.105263`; `GAME-0034`: `2 / 20 = 0.100000`; `GAME-0035`: `2 / 24 = 0.083333`; `GAME-0036`: `3 / 17 = 0.176471`.
- `GAME-0037`: `1 / 16 = 0.062500`; `GAME-0038`: `2 / 22 = 0.090909`; `GAME-0039`: `2 / 15 = 0.133333`; `GAME-0040`: `4 / 12 = 0.333333`.
- `GAME-0041`: `2 / 17 = 0.117647`; `GAME-0042`: `1 / 16 = 0.062500`; `GAME-0043`: `2 / 20 = 0.100000`; `GAME-0044`: `2 / 16 = 0.125000`.
- `GAME-0045`: `2 / 20 = 0.100000`; `GAME-0046`: `2 / 16 = 0.125000`; `GAME-0047`: `1 / 21 = 0.047619`; `GAME-0048`: `1 / 21 = 0.047619`.
- `GAME-0049`: `0 / 17 = 0.000000`; `GAME-0050`: `2 / 21 = 0.095238`; `GAME-0051`: `1 / 23 = 0.043478`; `GAME-0052`: `1 / 17 = 0.058824`.
- `GAME-0053`: `2 / 15 = 0.133333`; `GAME-0054`: `3 / 16 = 0.187500`; `GAME-0055`: `2 / 16 = 0.125000`; `GAME-0056`: `1 / 15 = 0.066667`.
- `GAME-0057`: `1 / 15 = 0.066667`; `GAME-0058`: `1 / 16 = 0.062500`; `GAME-0059`: `1 / 14 = 0.071429`; `GAME-0060`: `1 / 14 = 0.071429`.
- `GAME-0061`: `2 / 16 = 0.125000`; `GAME-0062`: `2 / 14 = 0.142857`; `GAME-0063`: `2 / 13 = 0.153846`; `GAME-0064`: `2 / 11 = 0.181818`.
- `GAME-0065`: `1 / 14 = 0.071429`; `GAME-0066`: `1 / 17 = 0.058824`; `GAME-0067`: `0 / 16 = 0.000000`; `GAME-0068`: `1 / 15 = 0.066667`.
- `GAME-0069`: `2 / 14 = 0.142857`; `GAME-0070`: `1 / 15 = 0.066667`; `GAME-0071`: `2 / 13 = 0.153846`; `GAME-0072`: `2 / 14 = 0.142857`.
- `GAME-0073`: `2 / 13 = 0.153846`; `GAME-0074`: `2 / 15 = 0.133333`; `GAME-0075`: `2 / 15 = 0.133333`; `GAME-0076`: `2 / 13 = 0.153846`.
- `GAME-0077`: `2 / 13 = 0.153846`; `GAME-0078`: `2 / 13 = 0.153846`; `GAME-0079`: `2 / 13 = 0.153846`; `GAME-0080`: `2 / 13 = 0.153846`.
- `GAME-0081`: `2 / 14 = 0.142857`; `GAME-0082`: `2 / 14 = 0.142857`; `GAME-0083`: `2 / 14 = 0.142857`; `GAME-0084`: `2 / 16 = 0.125000`.
- `GAME-0085`: `1 / 18 = 0.055556`; `GAME-0086`: `2 / 19 = 0.105263`; `GAME-0087`: `1 / 17 = 0.058824`; `GAME-0088`: `2 / 15 = 0.133333`.
- `GAME-0089`: `1 / 16 = 0.062500`; `GAME-0090`: `3 / 20 = 0.150000`; `GAME-0091`: `3 / 14 = 0.214286`; `GAME-0092`: `1 / 17 = 0.058824`.
- `GAME-0093`: `3 / 14 = 0.214286`; `GAME-0094`: `2 / 16 = 0.125000`; `GAME-0095`: `2 / 18 = 0.111111`; `GAME-0096`: `2 / 16 = 0.125000`.
- `GAME-0097`: `3 / 13 = 0.230769`; `GAME-0098`: `3 / 12 = 0.250000`; `GAME-0099`: `2 / 14 = 0.142857`; `GAME-0100`: `0 / 19 = 0.000000`.
- `GAME-0101`: `2 / 16 = 0.125000`; `GAME-0102`: `1 / 14 = 0.071429`; `GAME-0103`: `1 / 16 = 0.062500`; `GAME-0104`: `3 / 14 = 0.214286`.
- `GAME-0105`: `2 / 16 = 0.125000`; `GAME-0106`: `1 / 14 = 0.071429`; `GAME-0107`: `4 / 12 = 0.333333`; `GAME-0108`: `4 / 14 = 0.285714`.
- `GAME-0109`: `1 / 23 = 0.043478`; `GAME-0110`: `1 / 15 = 0.066667`; `GAME-0111`: `3 / 12 = 0.250000`; `GAME-0112`: `3 / 13 = 0.230769`.
- `GAME-0113`: `2 / 20 = 0.100000`; `GAME-0114`: `1 / 14 = 0.071429`; `GAME-0115`: `2 / 12 = 0.166667`; `GAME-0116`: `2 / 12 = 0.166667`.

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
