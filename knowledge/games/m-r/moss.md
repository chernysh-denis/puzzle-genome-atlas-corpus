---
game_id: GAME-0558
slug: moss
game_title: Moss
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-341
    - ACT-758
    - ACT-759
    - ACT-760
  system:
    - SYS-036
    - SYS-037
    - SYS-369
    - SYS-755
    - SYS-1363
    - SYS-1623
    - SYS-1624
  constraint:
    - CON-824
  information:
    - INF-271
    - INF-535
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Moss

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Quill, the Reader, stone shapes, wheel phase, controller mapping and collectible
counts are instance parameters, not independent genes.

## Analysis scope

- Version / ruleset: original fully released English standalone Oculus Quest
  edition of Moss, launched 21 May 2019, single-player Book I with two tracked
  Touch controllers and ordinary base equipment. This is the original Quest
  ruleset before the 2024 Quest 3/3S visual and combat-skip update, not PSVR's
  single tracked gamepad, PC VR streamed to a headset, Moss: Book II or the
  non-VR Moss: The Forgotten Relic. No owned headset, installed executable,
  version number, build hash, save file or regional binary was inspected.
- Primary decision loop: inspect the anchored miniature scene; directly steer
  and jump Quill while independently gripping marked scenery as the Reader;
  reposition constrained stones to establish reachable support, traverse
  authored ledges, then board and leave the slowed but still moving mill wheel,
  operate the bridge lever and bring Quill home.
- Entry and exit: fresh first visit to The Clearing, beginning with ordinary forest traversal around Quill’s discovery of the
  Glass and establishment of the Reader bond; include
  the entire forest, marked-stone and first fragment route, village gate,
  village passage, waterwheel, upper route, bridge lever and return crossing.
  Finish by entering Uncle Argus's home and accepting the return to the book
  that closes the chapter. Stop before playing Leaving Home. Opening the book
  and its story pages frame the packet but do not add a separate puzzle loop.
- Reproducible parameterisation: normal solo first visit with base sword,
  original two-controller tracking and an available safe physical play area.
  No native tracking calibration, exact jump distance, wheel-rate multiplier,
  collision solver, collectible rollback matrix or fixed random seed is claimed.
- Included: direct movement, jump and eligible automatic ledge catches with
  shimmy/pull-up/drop; separately tracked head inspection and Reader grip;
  marked stone translation and return along authored travel, gate pull,
  wheel braking without a complete stop and supported paddle transport;
  contextual bridge lever, changed walkable bridge, room transitions and home
  arrival; reachable ordinary container strikes/destruction and their dust,
  contact-collected fragments on the route, local affordance/interaction cues,
  companion advice, live gravity/support and authored failure checkpoint retry.
  These optional pickups do not become a prerequisite for entering home.
- Excluded: Chapter 2 combat, enemy possession, projectile redirection,
  pressure-plate enemy puzzles, later health attrition/healing under attack,
  boss encounters, Twilight Garden portals/equipment, later chapters,
  completionist replay, full-game collectible/trophy quotas and chapter-select
  cleanup. Friendly petting/high-fives and the reflected Reader mask are
  presentation rather than a separate scored or progress-gating mechanism.
  The Reader cannot be inferred to freely pick up Quill or arbitrary terrain.
- Potential scoped modules: Leaving Home combat and healing; enemy-mediated
  temple routing; Twilight Garden equipment; complete-book rescue; retained
  collectible cleanup; later hardware updates and non-VR dual control.
- Direct-play status: not conducted. Inspected all five public 160×90-cell
  storyboard sheets at ten-second sampling for Dave The Psycho's 18:41
  Quest-labelled recording from 8 June 2019, including Quest home/launch,
  forest, village, mill and home approach. Independently inspected eight
  320×180-cell sheets, 03:00–14:50, from ASVR's explicitly native Quest 2
  recording, published before the 2024 update: The Clearing starts at 03:20,
  the home/book closeout is visible around 09:40–10:10, and Leaving Home is
  labelled 12:43. This later capture corroborates geometry and the terminal,
  not an exact 2019 binary. Sparse stills are not uninterrupted playback or
  direct testing of failed jumps, input mappings or hardware. No video/audio
  playback, foreground window or focus capture was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MOS-001` | The approved target is the fully released 2019 standalone Quest game; later combat skip and non-VR versions are distinct. | Observation | Corroborated | High | P1, S5, S6, V1 |
| `MOS-002` | One human separately commands Quill and tracked Reader intervention inside an anchored miniature scene. | Observation | Corroborated | High | P1, P2, S1, V1, V2 |
| `MOS-003` | The forest route requires jump/ledge traversal and constrained marked-stone relocation, including changing support while Quill hangs. | Observation | Corroborated | High | S3, V1, V2 |
| `MOS-004` | An authored gate pull and Quill's later bridge lever change the available path; hand interaction alone does not teleport her to home. | Observation | Corroborated | High | S3, V1, V2 |
| `MOS-005` | Gripping the driven mill wheel slows its rotation; its changing paddles still require boarding, riding and leaving at valid positions. | Observation | Corroborated | High | S1, S3, V1, V2 |
| `MOS-006` | Ordinary containers yield dust and fragments are collectible on the Clearing route; no complete-collection quota gates ordinary chapter completion. | Observation | Corroborated | Medium | S2, S3, S4, V2 |
| `MOS-007` | Local markings, grip response, head inspection and authored Quill advice inform action, without disclosing the entire future route. | Observation | Corroborated | High | P2, P3, S1, S2, V1, V2 |
| `MOS-008` | Misjudged falls can fail locally and return to a room checkpoint rather than restarting the entire chapter. | Observation | Limited | Medium | S1 |
| `MOS-009` | Reaching home closes The Clearing and returns to the book before Leaving Home; later combat mechanics are not inherited into this genome. | Observation | Corroborated | High | S3, V2 |

## Basic data

- Release / origin: Polyarc's original Moss debuted on PSVR in February 2018;
  this standalone Quest edition launched 21 May 2019. That date is the target's
  release, not a claim that the product originated in 2019.
- Platform or physical form: standalone Oculus/Meta Quest, two tracked Touch
  controllers plus tracked head; structured target in the platform registry.
- Puzzle family: physics/object manipulation, real-time mechanism pressure,
  world-topology change and asymmetric agent/environment coordination.
- Primary sources:
  **[P1]** [Polyarc's official Moss page](https://www.polyarcgames.com/games/moss),
  current product identity and complementary control premise, checked 2026-11-19;
  **[P2]** [Corinne Scrivens's developer account, 16 April 2019](https://developers.meta.com/vr/blog/developer-perspective-creating-compelling-characters-w-corinne-scrivens-of-polyarc/),
  miniature-world interaction, tracked head/hands and embodied Reader design;
  **[P3]** [Chris Alderson creator interview, 23 June 2018](https://gamingtrend.com/interviews/the-world-behind-moss-an-e3-interview-with-polyarcs-chris-alderson/),
  authored Quill advice and two-hand design. Its PC/PSVR discussion is not an
  exact Quest button map or evidence that two enemies can be held at once.
- Secondary sources:
  **[S1]** [Oculus Quest Play review, 4 August 2019](https://www.oqplay.com/reviews/moss-oculus-quest-review/),
  actual Quest control, local checkpoint recovery and wheel/scene interaction;
  **[S2]** [Virtual Grip's Quest review, 15 August 2019](https://virtual-grip.com/moss-review-oculus-quest/),
  marked scenery, dust/fragments and non-mechanical friendly responses;
  **[S3]** [LittleBroomstick's complete Chapter 1 route](https://littlebroomstick.hateblo.jp/entry/2021/06/26/144640),
  Japanese route with screenshots and PSVR-style buttons. Use its ordered
  geometry, not those buttons as a Touch mapping;
  **[S4]** [Gameranx's original dust guide](https://gameranx.com/features/id/141365/article/moss-relic-dust-locations-collectibles-guide/),
  sword/orb breakables and contained collectibles, not a Quest quota;
  **[S5]** [Road to VR's dated 2024 update report](https://roadtovr.com/moss-1-2-get-a-visual-overhaul-and-25-discount-in-time-for-quest-3s-launch/),
  establishes why modern optional combat skip must not be backdated;
  **[S6]** [Contemporary Quest launch-content announcement](https://www.uploadvr.com/moss-twilight-garden/),
  launch date and separately integrated Twilight Garden, excluded here.
- Visual evidence:
  **[V1]** [Dave The Psycho's 2019 Quest Clearing recording](https://www.youtube.com/watch?v=oIVbCekvDIc),
  five sheets of 160×90 samples at ten-second intervals, 00:00–18:40;
  **[V2]** [ASVR's native Quest 2 playthrough](https://www.youtube.com/watch?v=ZVcMIoUhmbU),
  eight sheets of 320×180 samples at ten-second intervals, 03:00–14:50.
  Unused later book footage was not downloaded or inspected.
- Claim IDs: `MOS-001`–`MOS-009`.

## Mechanical decomposition

### Action Genes

- Existing: `ACT-008` directly steers/jumps Quill; `ACT-161` strikes admitted
  breakables with her ordinary sword; `ACT-341` operates the contextual lever.
- Added: `ACT-758` separately positions and holds a tracked Reader grip;
  `ACT-759` commands traversal from an automatically caught ledge; `ACT-760`
  physically reframes the anchored scene without moving Quill.
- Parameters: tracked hand/head poses, grip channel, analog motion, eligible
  edge, pull-up/drop command and addressed fixture. The same direction input
  is not broadcast to both Reader and Quill.
- Claim IDs: `MOS-002`–`MOS-007`.

### System Behaviour Genes

- Existing: `SYS-036` resolves live fall, contact and support;
  `SYS-037` credits contacted fragments; `SYS-369` restores a local authored
  checkpoint after a failed fall; `SYS-755` breaks admitted containers and
  resolves their dust output; `SYS-1363` carries supported Quill on the
  autonomously driven wheel paddles.
- Added: `SYS-1623` translates a held stone along its authored travel and
  retains the admitted release position; `SYS-1624` modifies wheel speed
  during its Reader grip rather than freezing the whole simulation.
- Resolution order: tracked/analog input and eligible target; fixture-specific
  motion; avatar jump/fall/support/edge response; contextual gate or bridge
  change, collection or local failure; scene transition and home/book terminal.
  This causal ordering does not claim the proprietary engine's update sequence.
- Claim IDs: `MOS-003`–`MOS-006`, `MOS-008`, `MOS-009`.

### Constraint Genes

- `CON-824` admits only authored Reader targets and their permitted motion;
  stones cannot be lifted freely into arbitrary air positions, and the Reader
  is not a general-purpose Quill transport tool.
- Scarce strategic resources: reachable support, wheel phase and an active
  interaction channel. No invented mana, grip timer or chapter deadline.
- Claim IDs: `MOS-002`, `MOS-003`, `MOS-005`.

### Information Genes

- Existing `INF-271` shows acquisition, held/released fixture response rather
  than an exact future path. Added `INF-535` records the tracked, partly
  occluded local diorama, authored surface/fixture cues and companion advice.
- Neither a whole-chapter map nor a perspective law creates a hidden bridge
  merely because two visible ledges line up in the headset.
- Claim IDs: `MOS-002`, `MOS-007`.

### Objective Genes

- Existing `OBJ-026`: bring the directly steered Quill to Uncle Argus's home
  after establishing the necessary connections. Entering home and accepting
  the book closeout completes the bounded chapter.
- Optional dust/fragments have local acquisition value; finding every one is
  not the ordinary success predicate. Failure is a local retry, not a lost-life
  stock, paid Continue or permanent save deletion.
- Claim IDs: `MOS-006`, `MOS-008`, `MOS-009`.

### Time Genes

- Existing `TIM-003`: gravity and the driven wheel continue while the player
  steers Quill and grips scenery. Calm observation elsewhere does not turn
  this live crossing into an alternating-turn puzzle.
- Claim IDs: `MOS-003`, `MOS-005`.

## Reproducible transitions

These are source-grounded procedures for the named ruleset, not a claim of
executed headset tests. Exact physical reach and rollback fields remain untested.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First patterned stone is recessed below an otherwise unreachable rise | Grip its accepted region and pull along its travel | Stone exposes a usable step; Quill must still jump/climb | Reader geometry change differs from avatar motion | `MOS-003` |
| Quill hangs on the edge above the long movable stone | Retain her ledge catch and move the stone with the Reader | A landing becomes available without dragging Quill by the orb | Separate live control and support | `MOS-002`, `MOS-003` |
| Quill has crossed to the other side of that stone | Return the stone, then jump/climb onward | The retained fixture becomes support for the next rise | Reconfiguration is reversible, not consumed | `MOS-003` |
| Unmarked wall blocks a desired shortcut | Address it with the Reader grip | It does not become a freely movable stone | Authored eligibility, not unrestricted telekinesis | `MOS-002`, `MOS-003` |
| Village gate is still closed | Pull its accepted Reader target and steer Quill through | Gate opens the ordinary passage | Opening geometry does not move the avatar automatically | `MOS-004` |
| Driven mill wheel is turning | Sustain the eligible grip | Angular motion slows but a valid paddle phase is still needed | Braking differs from a complete time stop | `MOS-005` |
| Quill stands on a moving paddle near the upper support | Jump at the aligned position | She leaves the carried support for the authored ledge | Support transport and manual departure differ | `MOS-003`, `MOS-005` |
| Bridge remains raised across the home route | Reach and operate its contextual lever | Bridge lowers; return over the wheel and cross the new connection | Joined dependency, not an optional scenic interaction | `MOS-004`, `MOS-005` |
| Accessible ordinary breakable still contains dust | Strike it with Quill or use its admitted Reader break response | Container breaks and credits/releases its contained output | Destruction is separate from stone relocation | `MOS-006` |
| A fragment is still on its local optional path | Guide Quill into it | It is acquired without ending the chapter | Pickup is not home arrival | `MOS-006` |
| A jump misses viable support | Continue into the authored failure boundary | Local checkpoint recovery permits retry | Room-local failure; exact retained collection fields are untested | `MOS-008` |
| Bridge route is open and Quill approaches home | Enter the home | Chapter returns to its book closeout | Complete terminal, not stopping at the wheel puzzle | `MOS-009` |

## Strategic and experiential structure

- Local decision: identify which body must act, then choose stone displacement,
  ledge command or wheel boarding/departure timing.
- Medium-term planning: keep useful support beneath Quill; return a shifted
  stone when needed; open the bridge from its far-side lever and return safely.
- Long-term structure: the entire chapter links forest, gate, village and home;
  later combat is a different packet, not silently part of this genome.
- Common heuristics: inspect from another head angle; park Quill on secure
  support before releasing a fixture; do not mistake slowing for stopping.
- Failure attribution: wheel phase, edge alignment and visible landing explain
  route mistakes; native tracking ambiguity and precise tolerances are untested.
- Player-trust factors: local retries reduce backtracking; authored Quill
  communication makes the two-role relationship legible without a timed quota.
- Claim IDs: `MOS-002`–`MOS-009`.

## Replay and variation

- What changes: player trajectories, head/hand poses, wheel phase and optional
  pickup detours. The scoped layout is authored rather than a shuffled maze.
- Randomness: no procedural route or exact hidden random distribution asserted.
- Multiple viable strategies: timings and inspection choices vary, but the
  observed authored fixture dependencies remain; no skip/glitch route is certified.
- Replay motive: cleaner coordination or optional pickup recovery outside the
  ordinary chapter-clear predicate. Full completionist replay is excluded.
- Claim IDs: `MOS-003`–`MOS-009`.

## Adjacent systems and history

- Direct context: original 2018 VR product, followed by the standalone Quest
  port. Creator discussion explains the tiny-world and embodied Reader design.
- Variants: PC VR/PSVR input differences, the later Quest update, Book II and
  non-VR reinterpretation are not mechanically interchangeable with this packet.
- Similar games: the exact selected-neighbour interpretation below owns the
  full-signature comparison; visual animal or miniature-world resemblance alone
  is not a genome match.
- Important differences: this is one human coordinating complementary live
  channels, not cooperative players, shared-input clones, a physics ragdoll or
  projection-created connectivity.
- Claim IDs: `MOS-001`, `MOS-002`, `MOS-007`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-341`, `ACT-758`, `ACT-759`, `ACT-760` | Instance parameters only |
| System Behaviour | `SYS-036`, `SYS-037`, `SYS-369`, `SYS-755`, `SYS-1363`, `SYS-1623`, `SYS-1624` | Instance parameters only |
| Constraint | `CON-824` | Instance parameters only |
| Information | `INF-271`, `INF-535` | Instance parameters only |
| Objective | `OBJ-026` | Instance parameters only |
| Time | `TIM-003` | Instance parameters only |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `557` (`GAME-0001`–`GAME-0557`).
- Exact genome matches: none.
- Tied near matches: `GAME-0312` — ASTRO BOT (`7 / 27 = 0.259259`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0312` — ASTRO BOT | `ACT-008`, `ACT-161`, `ACT-341`, `SYS-036`, `SYS-037`, `SYS-369`, `TIM-003` | Both packets directly steer a body through live jumps, fixture interactions, pickups and local retries. Sky Garden adds hostile combat, inflation/hover and retained level-map settlement; The Clearing instead separates tracked Reader/head channels, constrained stones, automatic ledges and local wheel braking before home arrival. Neither its exact collectible persistence nor a later enemy-control system is inherited. | Tied near; `7 / 27 = 0.259259` |

### Preserved research notes

- New genes: seven additions; eleven unchanged definitions reused.
- Classification result: `New gene`.
- Evidence and reasoning: tracked intervention and the still-driven wheel add
  distinct causal boundaries; shared ordinary traversal does not imply matching
  control, route state or terminal settlement.

## Taxonomy impact

- Registry changes: seven Active definitions, three Actions, two System
  Behaviours, one Constraint and one Information gene. All previous definitions
  and signatures are retained unchanged.
- Taxonomy-change record: [TAXONOMY_CHANGE_304](../../../research/taxonomy-changes/TAXONOMY_CHANGE_304.md).
- Candidate terms affected: tracked Reader grip, automatic ledge traversal,
  anchored head inspection, constrained scenery motion and wheel braking.

## Negative results

- None as a separate record. Rejected reuse boundaries are documented in the
  taxonomy decision; no claim of external novelty or missing game is made.

## Delta summary

## New facts

- [Observation | Corroborated | High] The Clearing couples Quill traversal and
  Reader intervention through the complete return-home terminal (`MOS-002`–`MOS-009`).
- [Observation | Limited | Medium] Local checkpoint recovery is sourced from a
  contemporary Quest review, not reproduced native failure experiments (`MOS-008`).

## New genes

- [Observation | Corroborated | High] `ACT-758`–`ACT-760`, `SYS-1623`,
  `SYS-1624`, `CON-824` and `INF-535` isolate the admitted boundaries without
  altering previous genes or asserting external novelty.

## New combinations

- [Observation | Direct | High] No new combinations: exhaustive proper-subset scanning
  found no supported subset among the 274 verified combinations.

## Taxonomy changes

- [Observation | Direct | High] TAXONOMY_CHANGE_304 adds seven Active genes;
  no merge, split, reactivation or existing-signature mutation.

## New questions

- Which exact 2019 binary checkpoint fields retain acquired dust and fragments
  after a failed local jump, and how do tracking loss and grip reacquisition act?
- Does an explicitly bounded later combat packet reuse independent Reader
  control without importing sequel equipment or modern assistance?

## Next recommended game

- [Hypothesis | Limited | Medium] None authorised. GAME-0558 closes the approved
  nine-game horizon; complete its final batch gates, then stop. Selecting new
  subjects, pushing or publishing requires the maintainer's separate request.
- Optimisation criterion: verify accepted coverage, not start a tenth game.
- Expected information gain: confirm complete bilingual batch parity.
- Backlog impact: no new game selected.

## Why this game

- [Hypothesis | Limited | High] The approved standalone VR slot tests asymmetric
  tracked intervention against direct avatar traversal without consecutive
  sensor-gun or handheld-combat coverage.
