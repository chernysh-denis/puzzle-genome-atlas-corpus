---
game_id: GAME-0157
slug: split-fiction
game_title: Split Fiction
analysis_status: reviewed
reviewed: 2026-08-26
combination_ids:
  - COMB-0155
gene_ids:
  action:
    - ACT-008
    - ACT-049
    - ACT-161
    - ACT-201
    - ACT-256
  system:
    - SYS-036
    - SYS-065
    - SYS-429
    - SYS-430
  constraint:
    - CON-076
    - CON-378
    - CON-379
  information:
    - INF-001
    - INF-167
  objective:
    - OBJ-086
  time:
    - TIM-003
---

# Game: Split Fiction

## Analysis scope

- Version / ruleset: released PC base game after the official 17 March 2025
  update, bounded to a fresh two-human-player run of Chapter 1, `Rader
  Publishing`, from first control inside the shared simulation through both
  `Freedom Fighters` and `Brave Knights` and the transition into `Neon
  Revenge`.
- Primary decision loop: each human reads both live panes, navigates one
  protagonist through the current hazards, commits the actor-specific or paired
  interaction at the needed position and time, preserves the segment through
  one partner's failure, and advances both actors to the next authored gate.
- Reproducible entry: start a new two-human-player base-game session, assign one
  player to Mio and the other to Zoe, complete the opening cutscene and take
  control at the first Rader Publishing traversal with no later chapter
  ability active.
- Reproducible exit: both players complete every mandatory Freedom Fighters
  and Brave Knights segment and cross the authored transition into Neon
  Revenge; stop before using its gravity whip or energy katana.
- Included: fixed Mio/Zoe ownership, split-screen local or online co-op, running,
  double-jump, dash, grapple and contextual switches; paired consoles, held
  mechanisms and dual plates; live hazards and combat; the complementary
  pilot/gunner escape; single-partner respawn, two-partner checkpoint reset and
  completion of both authored opening stories.
- Excluded: later `Neon Revenge` gravity whip/energy katana systems, all later
  chapters and Side Stories, Friend's Pass entitlement as a mechanic,
  collectibles, achievements, accessibility checkpoint skipping, reduced enemy
  damage and the campaign ending.
- Direct-play status: not conducted. EA's current product, launch and
  accessibility material establishes the fixed two-player, split-screen and
  checkpoint surface; two independent walkthroughs reproduce the bounded
  chapter transitions. No live solution or later-chapter mechanic was consumed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SF-001` | Split Fiction is specifically designed as a two-player split-screen or online cooperative game | Confirmed | Direct | High | P1, P2 |
| `SF-002` | The official free opening reaches the start of Neon Revenge, making Rader Publishing a publicly named bounded opening packet | Confirmed | Direct | High | P2 |
| `SF-003` | Chapter 1 contains the two authored stories Freedom Fighters and Brave Knights | Confirmed | Corroborated | High | S1, S2 |
| `SF-004` | Players traverse live geometry with jumps, dash, grapple, switches and timed hazards | Observation | Corroborated | High | S1, S2 |
| `SF-005` | Progress repeatedly requires both players: simultaneous consoles, held passage mechanisms, separate plates and joint door interaction | Observation | Corroborated | High | P1, S1, S2 |
| `SF-006` | Freedom Fighters temporarily assigns one player to pilot and the other to the turret | Observation | Corroborated | High | S1, S2 |
| `SF-007` | One failed player can return while the partner remains active, but simultaneous pair failure resets the segment | Observation | Corroborated | High | S1, S3 |
| `SF-008` | The interface continuously exposes both player views through the split-screen presentation | Confirmed | Direct | High | P1, P2, P3 |
| `SF-009` | Later levels intentionally replace mechanics and abilities, so they do not belong to this chapter signature | Confirmed | Direct | High | P1 |

## Basic data

- Release / origin: Hazelight Studios; Electronic Arts released the PC,
  PlayStation 5 and Xbox Series versions on 6 March 2025.
- Platform or physical form: real-time third-person two-player cooperative
  action-platform chapter.
- Puzzle family: authored cooperative traversal and role coordination.
- Primary sources: **[P1]** [official product features](https://www.ea.com/games/split-fiction/split-fiction),
  **[P2]** [official release article](https://www.ea.com/games/split-fiction/split-fiction/news/split-fiction-is-available-now),
  **[P3]** [official accessibility resources](https://www.ea.com/able/resources/split-fiction/split-fiction),
  **[P4]** [official 17 March update notes](https://www.ea.com/games/split-fiction/split-fiction/news/split-fiction-update-notes-17-03).
- Secondary sources: **[S1]** [VGTimes Rader Publishing walkthrough](https://vgtimes.com/guides/122474-split-fiction-rader-publishing-walkthrough.html),
  **[S2]** [ShowGamer complete walkthrough, Chapter 1](https://showgamer.com/en/prohozhdeniya-igr/2855-polnoe-prohozhdenie-split-fiction),
  **[S3]** [TechRadar opening-gameplay preview](https://www.techradar.com/gaming/split-fiction-preview).
- Claim IDs: `SF-001`–`SF-009`.

## Mechanical decomposition

### Action Genes

- `ACT-008` covers direct navigation; `ACT-049` covers local world switches;
  `ACT-161` covers aimed hostile strikes and `ACT-201` the temporary vehicle
  pilot role.
- `ACT-256` records each player's separately committed half of a paired
  cooperative interaction.
- Candidate genes: none.
- Claim IDs: `SF-004`–`SF-006`.

### System Behaviour Genes

- `SYS-036` resolves live body and hazard physics; `SYS-065` moves linked
  authored platforms from local controls.
- `SYS-429` keeps the segment alive and returns one failed partner while the
  other remains active; `SYS-430` restores the segment checkpoint only after
  the pair fails together.
- Resolution order: input and collision; paired-gate state; survival/respawn;
  checkpoint or chapter progress.
- Claim IDs: `SF-004`, `SF-005`, `SF-007`.

### Constraint Genes

- `CON-076` binds temporary interactions to Mio/Zoe or pilot/gunner authority.
- `CON-378` requires two independently controlled human participants;
  `CON-379` withholds paired-gate resolution until both eligible halves are
  committed.
- Scarce strategic resources: two independently surviving bodies and each
  actor's current position; no inventory economy belongs to the packet.
- Claim IDs: `SF-001`, `SF-005`, `SF-006`.

### Information Genes

- `INF-001` exposes each actor's local hazards, prompts and reachable geometry.
- `INF-167` simultaneously exposes the partner's live view, position and
  interaction state through the persistent split-screen surface.
- Candidate genes: none.
- Claim IDs: `SF-008`.

### Objective Genes

- `OBJ-086` requires both players to complete the finite authored two-story
  chapter and cross its transition into Neon Revenge.
- Success, evaluation and failure: both enter the next chapter; one-player
  failure is recoverable, while simultaneous failure restores the segment.
- Claim IDs: `SF-002`, `SF-003`, `SF-007`.

### Time Genes

- `TIM-003` keeps movement, hazards, vehicle motion and combat advancing while
  both players supply real-time input.
- Candidate genes: none.
- Claim IDs: `SF-004`–`SF-007`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Both players stand at the opening lift console | Each commits the paired prompt in its timing window | The lift activates only from the accepted pair | two-human paired gate | `SF-005` |
| One player holds the rotating barrier control | Partner traverses the exposed gap, then returns access from the far side | The roles sequence passage for both bodies | asymmetric temporary authority | `SF-005` |
| Escape vehicle is reached | One player pilots while the other mounts the turret | Steering and hostile clearance remain complementary live tasks | role-bound vehicle sequence | `SF-006` |
| One player fails while the partner survives | Failed player completes the return prompt / delay | The live segment continues and the failed body returns | survivor-held segment | `SF-007` |
| Both players fail before the next checkpoint | Resolve simultaneous pair failure | Current segment reloads from its authored checkpoint | pair-wipe reset | `SF-007` |

## Strategic and experiential structure

- Local decision: time a jump, grapple, switch, strike or paired prompt against
  the current hazard.
- Medium-term planning: position one actor to hold or operate a mechanism while
  the other crosses, then restore access for the first.
- Long-term structure: carry both human-controlled protagonists through the two
  opening stories and into the next chapter.
- Common heuristics: announce countdowns, watch the partner pane, let the
  stronger survivor preserve a live segment and exchange temporary roles.
- Failure attribution: the split view distinguishes positioning, timing and
  role errors; pair failure identifies the shared checkpoint boundary.
- Player-trust factors: prompts, hazard telegraphs and the partner pane must
  remain readable without assuming voice chat.
- Claim IDs: `SF-004`–`SF-008`.

## Replay and variation

- What changes between sessions: player-to-character assignment, timing,
  movement execution and pilot/gunner performance.
- Randomness or procedural generation: none in the scoped authored chapter.
- Multiple viable strategies: local traversal timing varies, but story gates
  and role sequence are authored.
- Typical replay motive: swap roles or play with another partner.
- Claim IDs: `SF-003`–`SF-007`.

## Adjacent systems and history

- Direct predecessors: Hazelight's A Way Out and It Takes Two; neither is
  currently a canonical Atlas game.
- Variants: online, local split-screen and Friend's Pass share the scoped
  gameplay; entitlement and networking are not genome genes.
- Similar games: Portal 2 Cooperative Campaign and authored action-platformers.
- Important differences: the partner viewport, two-human requirement and
  survivor-held respawn remain stable while later level-specific abilities are
  deliberately replaced.
- Claim IDs: `SF-001`, `SF-008`, `SF-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-049`, `ACT-161`, `ACT-201`, `ACT-256` | character assignment |
| System Behaviour | `SYS-036`, `SYS-065`, `SYS-429`, `SYS-430` | respawn delay, checkpoint |
| Constraint | `CON-076`, `CON-378`, `CON-379` | two humans, paired timing |
| Information | `INF-001`, `INF-167` | split layout, prompt channel |
| Objective | `OBJ-086` | chapter endpoint |
| Time | `TIM-003` | live hazard and combat timing |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `156` (`GAME-0001`–`GAME-0156`).
- Exact genome matches: none.
- Tied near matches: `GAME-0095` — Manifold Garden (`5 / 23 = 0.217391`).
- Supported combination subsets: `COMB-0155`.
- Scan date: 2026-08-26.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0095` — Manifold Garden | `ACT-008`, `ACT-049`, `SYS-036`, `SYS-065`, `TIM-003` | Both use direct avatar navigation, reachable switches, continuous body physics, switch-linked platform motion and live-time traversal; Manifold Garden has global gravity reorientation and periodic topology, while Split Fiction requires two humans, paired inputs, actor-specific roles, a partner viewport and survivor-held cooperative recovery | Near, `0.217391` |

### Preserved research notes

- New genes: `ACT-256`, `SYS-429`, `SYS-430`, `CON-378`, `CON-379`, `INF-167`
  and `OBJ-086`.
- Reused genes: `ACT-008`, `ACT-049`, `ACT-161`, `ACT-201`, `SYS-036`,
  `SYS-065`, `CON-076`, `INF-001` and `TIM-003`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: later anthology mechanics are excluded; the new
  records cover only the stable two-human ownership, paired progress,
  split-view information and recovery boundary that the first chapter itself
  reproduces.

## Taxonomy impact

- Registry changes: `ACT-256`, `SYS-429`, `SYS-430`, `CON-378`, `CON-379`,
  `INF-167`, `OBJ-086`; existing records gain Split Fiction evidence only.
- Taxonomy-change record: none.
- Candidate terms affected: paired co-op interaction, survivor-held respawn,
  pair-wipe reset, two-human requirement and partner viewport.

## Negative results

- Later chapter abilities, the Friend's Pass entitlement and accessibility
  checkpoint skipping are excluded because they are not causal members of the
  ordinary Rader Publishing completion packet.
