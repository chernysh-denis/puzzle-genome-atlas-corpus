---
game_id: GAME-0113
slug: portal-2-co-op
game_title: Portal 2 — Cooperative Campaign
analysis_status: reviewed
reviewed: 2026-08-16
combination_ids:
  - COMB-0033
  - COMB-0112
gene_ids:
  action:
    - ACT-008
    - ACT-047
    - ACT-048
  system:
    - SYS-036
    - SYS-059
    - SYS-060
    - SYS-061
  constraint:
    - CON-078
    - CON-079
    - CON-166
  information:
    - INF-001
    - INF-019
  objective:
    - OBJ-022
  time:
    - TIM-003
---

# Game: Portal 2 — Cooperative Campaign

## Analysis scope

- Version / ruleset: Portal 2's two-player cooperative campaign, bounded to one
  ordinary test chamber where ATLAS and P-body each own a complete two-colour
  portal pair and must both reach their exit receptors.
- Included: two independently controlled robots, four portal channels, surface
  eligibility, replacement, cross-owner traversal, momentum, cube carrying,
  visible portal views, live physics and dual exit completion.
- Excluded: single-player campaign, gels, excursion funnels, light bridges,
  gestures, calibration, story progression, workshop maps and speedrun exploits.
- Direct-play status: not conducted. Valve's product page establishes the
  separate two-player campaign; Portal's primary mechanics provide the shared base.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `P2C-001` | Portal 2 includes a separate two-player cooperative campaign | Confirmed | Direct | High | P1 |
| `P2C-002` | Each robot owns a distinct portal pair, yielding four persistent channels | Confirmed | Corroborated | High | P1, S1 |
| `P2C-003` | The scoped chamber requires both agents to coordinate topology and reach their exits | Observation | Corroborated | High | P1, S1 |

## Basic data

- Release / origin: Valve released Portal 2 in 2011.
- Platform or physical form: first-person cooperative spatial puzzle.
- Puzzle family: world topology and agent coordination.
- Primary sources: **[P1]** [Portal 2 on Steam](https://store.steampowered.com/app/620/Portal_2/).
- Secondary sources: **[S1]** [Portal Dialogue Corpus paper](https://arxiv.org/abs/2512.03381).
- Claim IDs: `P2C-001`–`P2C-003`.

## Mechanical decomposition

### Action Genes

- `ACT-008` navigates each robot, `ACT-047` places owned endpoints and
  `ACT-048` carries a shared cube.
- Candidate genes: none.
- Claim IDs: `P2C-002`, `P2C-003`.

### System Behaviour Genes

- `SYS-036` resolves physics; `SYS-059`, `SYS-060`, `SYS-061` provide paired
  traversal, momentum redirection and occupancy-held mechanisms.
- Resolution order: endpoint placement; collision / transit; mechanism state; exit.
- Claim IDs: `P2C-003`.

### Constraint Genes

- `CON-078` restricts surfaces, `CON-079` limits one endpoint per channel and
  `CON-166` preserves two owners and four channel identities.
- Scarce strategic resources: four replaceable endpoints and two bodies.
- Claim IDs: `P2C-002`.

### Information Genes

- `INF-001` exposes local chamber state; `INF-019` shows live cross-portal views.
- Candidate genes: none.
- Claim IDs: `P2C-003`.

### Objective Genes

- `OBJ-022` requires both controlled robots to reach the paired exit receptors.
- Success, evaluation and failure: both present; death resets affected state.
- Claim IDs: `P2C-003`.

### Time Genes

- `TIM-003` keeps body and object physics live during coordination.
- Candidate genes: none.
- Claim IDs: `P2C-003`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| ATLAS has blue / purple portals; P-body has orange / red | P-body replaces red | Only P-body's red endpoint moves | owned channel identity | `P2C-002` |
| ATLAS enters its blue endpoint | Continue through topology | ATLAS exits ATLAS purple or linked active pair, preserving momentum | shared traversal law | `P2C-003` |
| Only one robot reaches an exit | Stand on receptor | Chamber remains incomplete | dual-agent completion | `P2C-003` |

## Strategic and experiential structure

- Local decision: choose which owner places which endpoint.
- Medium-term planning: distribute bodies and cube across portal-separated spaces.
- Long-term structure: preserve a four-endpoint route until both exits are occupied.
- Common heuristics: describe colours and avoid replacing a partner's needed route.
- Failure attribution: endpoint ownership is visible; communication errors dominate.
- Player-trust factors: colour / owner distinction needs accessible redundancy.
- Claim IDs: `P2C-002`, `P2C-003`.

## Replay and variation

- What changes between sessions: division of labour and timing.
- Randomness or procedural generation: none in the authored chamber.
- Multiple viable strategies: some chambers permit timing variants.
- Typical replay motive: cooperate with another partner.
- Claim IDs: `P2C-001`.

## Adjacent systems and history

- Direct predecessors: Portal's single-player paired topology.
- Variants: later co-op elements are outside scope.
- Similar games: Portal and synchronized-body puzzles.
- Important differences: four owner-specific portal channels and two required actors.
- Claim IDs: `P2C-002`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-047`, `ACT-048` | two controllers |
| System Behaviour | `SYS-036`, `SYS-059`, `SYS-060`, `SYS-061` | portal physics |
| Constraint | `CON-078`, `CON-079`, `CON-166` | ownership |
| Information | `INF-001`, `INF-019` | colour / symbol labels |
| Objective | `OBJ-022` | dual exits |
| Time | `TIM-003` | live coordination |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `112` (`GAME-0001`–`GAME-0112`).
- Exact genome matches: none.
- Tied near matches: `GAME-0033` — Portal (`13 / 14 = 0.928571`).
- Supported combination subsets: `COMB-0033`, `COMB-0112`.
- Scan date: 2026-08-16.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0033`.

## Taxonomy impact

- Registry changes: `CON-166`.
- Taxonomy-change record: none.
- Candidate terms affected: portal ownership.

## Negative results

- `none`.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Co-op preserves Portal's laws while adding
  four persistent owner-specific channels (`P2C-002`).

## Нові гени

- [Observation | Corroborated | High] `CON-166`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0112`.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Which later co-op chambers require explicit synchronous action timing?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] Peggle Deluxe.
- Optimisation criterion: reuse launcher physics without structural destruction.
- Expected information gain: separate shared ballistics from hit-target response.
- Backlog impact: continue the popularity batch.

## Чому саме вона

- [Hypothesis | Limited | High] It provides an immediate transfer test for `ACT-113` and `SYS-146`.
