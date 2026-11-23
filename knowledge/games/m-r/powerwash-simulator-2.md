---
game_id: GAME-0534
slug: powerwash-simulator-2
game_title: PowerWash Simulator 2
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids:
  - COMB-0271
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-202
    - ACT-446
    - ACT-731
  system:
    - SYS-630
    - SYS-1544
    - SYS-1545
  constraint:
    - CON-516
    - CON-812
  information:
    - INF-329
    - INF-331
  objective:
    - OBJ-168
  time:
    - TIM-003
---

# Game: PowerWash Simulator 2

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Spray widths, initial equipment, task parts, credit and coverage tolerances
parameterise the observed rules.

## Analysis scope

- Version / ruleset: English digital base game for Xbox Series X|S,
  full release starting 23 October 2025. Study the ordinary release-era
  single-player Career rules with the starting equipment and a controller.
  Xbox product 9P45GGDTFNSM identifies the edition. No installed binary
  revision was observed.
- Entry: start the fresh Career's first `Removals Van` job and begin at
  the first actionable state in the wash bay with the dirty vehicle and
  supplied light-duty gear. Use the assigned surfaces and supplied access
  equipment. No shop purchase is needed.
- Primary decision loop: inspect aggregate and part state, choose an
  accessible unwashed patch, move or change posture, choose a nozzle and
  sustain the stream over new dirt. On a stubborn patch, either direct a
  stronger footprint or deposit foam and rinse it. Read the current task
  list and request a spatial highlight for remaining dirt or a missed part.
- Positive exit: the last required part reaches accepted completion. Use
  the resulting finish transition and stop once the completed job is
  credited to Career with the next job available, before starting it.
  An incomplete job is unfinished regardless of time spent.
- Included: exterior and cargo interior, stance and local movement,
  supplied movable ladder and its eligible positions, nozzle choice and
  spray direction, water coverage, local foam and its reusable supply,
  part and job progress, selected-part and residual-dirt highlights,
  and first-job settlement. No enforced order among the named parts.
- Excluded: Home Base decoration, later or phased sites, purchasing and
  selling, upgrades, floor-cleaner optimisation, Free Play, cooperative
  play, cloud clients, demo, downloadable packs, other platforms, and
  exact save-file and patch behaviour. Keep separate currencies as
  reported settlement fields rather than analysing the shop.
- Direct-play status: no Xbox or executable was run. The developer and
  Xbox listings establish the release and tool rules. Xbox-focused written
  instructions, first-job play records and static captures corroborate
  this instance. No audiovisual playback or timings were used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PW2-001 | FuturLab's completed base game released digitally on Xbox Series X and S on 23 October 2025. Solo Career uses jobs separate from Free Play. | Confirmed | Direct | High | P1–P3 |
| PW2-002 | Removals Van is the first Career job. The player uses starting light-duty tools and washes required exterior and cargo surfaces. No purchased tool or fixed treatment order is required. | Observation | Corroborated | High | P3, S1–S3 |
| PW2-003 | Aim the held or toggled spray and move between available positions. At a given reachable patch, width trades the area of a pass against concentrated pressure. Rotating the water nozzle changes the fan's orientation. | Observation | Corroborated | High | P1, P3, S1 |
| PW2-004 | Crouching changes the angle to lower surfaces. Enter the rear for interior surfaces. Place the movable ladder at an indicated valid spot to change access to higher surfaces. | Observation | Corroborated | High | P1, S1–S3 |
| PW2-005 | Soap has a separate applicator and leaves foam on untreated surfaces. The coating loosens dirt for a subsequent water pass, including with broad nozzles. Soap is optional and placement is not the same as accepted cleaning. | Observation | Corroborated | High | P1, P3, S1, S4 |
| PW2-006 | The current deployable foam stock is limited. Rinsing applied foam frees supply. Recall can remove applied foam without counting it as a cleaning pass. The player need not purchase a replacement stock for the job. | Observation | Corroborated | High | P1, P4, S1, S4 |
| PW2-007 | The current part's dirt bar, overall percentage and task list distinguish component state from job state. Select a component for an in-world highlight or request a distinct residual-dirt highlight. Neither operation cleans it. | Observation | Corroborated | High | S1, S2, S4 |
| PW2-008 | Accepted water treatment persists while washing the same job. The final required part enables job completion and the finishing transition, after which Career can advance. The Xbox route reports $200 and a separate points field. | Observation | Corroborated | High | P1, P3, S1, S3, S5 |

## Basic data

- Release / origin: FuturLab, 23 October 2025 digital Xbox Series X|S launch.
- Families: state transformation and inventory and fixture dependencies.
- Sources accessed 2026-11-17:
  - **P1** — [FuturLab's release announcement](https://www.futurlab.co.uk/news/its-time-to-shine-powerwash-simulator-2-is-out-now),
    for supported platforms, currency types, ladder families, nozzles
    and optional foam and water as separate operations.
  - **P2** — [Xbox digital product listing](https://www.xbox.com/en-US/games/store/powerwash-simulator-2/9p45ggdtfnsm)
    and [Xbox Wire's developers' release account](https://news.xbox.com/en-us/2025/10/23/powerwash-simulator-2-how-futurlab-built-a-sparking-sequel/),
    for product 9P45GGDTFNSM, target consoles and the completed launch.
  - **P3** — [FuturLab support FAQ](https://futurlab.freshdesk.com/support/solutions/articles/204000073222-powerwash-simulator-2-faqs),
    for accessible Career and Free Play regions, no separate challenge
    levels, the base and the optional cleaning effects of the foam.
  - **P4** — [FuturLab's 1.2 notes on soap recall](https://www.futurlab.co.uk/news/clean-up-the-tiny-town-free-caldera-chronicles-level-plus-12-patch-notes)
    and [its controller clarification](https://steamcommunity.com/app/2968420/discussions/0/571540300205414101/).
    The later notes confirm the intended operation. Multiplayer bugs and
    rebindable presets are not part of the studied opening job.
  - **S1** — [Xbox Career walkthrough](https://www.trueachievements.com/game/PowerWash-Simulator-2/walkthrough/3),
    Removals Van section, for starting gear, controls, the two kinds of
    highlights, ladder sites, interior access, foam capacity and settlement.
  - **S2** — [Written first-job route and tool notes](https://www.powerwashsimulator2.wiki/),
    for broad and narrow passes, remaining components and access angles.
  - **S3** — [FuzionByte's 2025 play and achievement guide](https://www.fuzionbyte.com/powerwash-simulator-2-trophy-guide/),
    for first-job acceptance, inside and outside coverage and initial gear.
  - **S4** — [A release-period PC play report](https://steamcommunity.com/profiles/76561198305741403/recommended)
    and [a dated player discussion on deployed foam](https://www.reddit.com/r/PowerWashSimulator/comments/1p0ni58/),
    corroborate replenishment through rinsing. They do not establish the
    Xbox stock size, recovery timing or console bindings.
  - **S5** — [Game8's release review and job-complete still](https://game8.co/articles/reviews/powerwash-simulator-2-review)
    distinguishes accepted 100 percent coverage from the subsequent finish
    input. The displayed PC binding is not used as a console binding.
- Claim IDs: PW2-001–PW2-008.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: move around the exterior and into the cargo area
  to aim at other assigned surfaces.
- Reuse `ACT-048`: pick up the ladder and release it at a legal access
  site. Placement is checked independently of the carry.
- Reuse `ACT-202`: change stance to see and reach lower edge surfaces.
- Reuse `ACT-446`: aim and hold or toggle the washer output so the
  active stream covers a chosen sweep of the reachable surface.
- New `ACT-731`: change the fitted applicator footprint during the job
  by selecting a compatible nozzle. Reorient an anisotropic water fan
  where the current patch is easier to reach along another axis.
- Claim IDs: PW2-002–PW2-005.

### System Behaviour Genes

- Reuse `SYS-630`: the directed stream converts newly contacted
  eligible dirty surface to persistent accepted treatment. Additional
  overlap on already accepted area cannot stand in for missed surface.
- New `SYS-1544`: foam remains on the dirty patch as a preparatory
  layer. A following water pass over it detaches the coating and eases
  removal of the underlying dirt. The coating alone is not the result.
- New `SYS-1545`: available foam and deployed foam share a reusable
  supply. Rinsing deposited foam makes it available again. The recall
  input takes the coating back without performing the wash.
- Claim IDs: PW2-005–PW2-008.

### Constraint Genes

- Reuse `CON-516`: accepted treatment must reach each required part's
  target clearance for the job to finish. Nozzle strength, treatment
  order and foam use are not additional end conditions.
- New `CON-812`: a carried access ladder is set only at authorised,
  indicated spots for that equipment. This constrains the subsequent
  position and tool angle separately from carried movement.
- Claim IDs: PW2-002–PW2-004, PW2-008.

### Information Genes

- Reuse `INF-329`: the task list and current-part bar identify missing
  components independently of the aggregate job percentage.
- Reuse `INF-331`: request a residual-dirt highlight for the patch or
  highlight an incomplete part selected from the list. Reducing the list
  to remaining items changes its display, not the wash state.
- Claim IDs: PW2-007.

### Objective Genes

- Reuse `OBJ-168`: reach accepted completion on every assigned exterior
  and cargo surface and take the finish transition to the credited
  Career result before starting another job.
- Claim IDs: PW2-002, PW2-008.

### Time Genes

- Reuse `TIM-003`: directing the active spray over time changes what is
  cleaned while live control remains available. Leaving the nozzle
  inactive does not impose a Career failure deadline.
- Claim IDs: PW2-003, PW2-005, PW2-008.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| The first job opens with a dirty exterior and cargo interior | Inspect the tasks and begin a water pass on an accessible dirty panel | Treatment changes where the compatible stream reaches new dirty area | The washer treats coverage continuously rather than selecting a whole part | PW2-002, PW2-003, PW2-008 |
| A roof angle or lower edge is out of useful reach | Set the ladder at a marked place or change stance | The new access position or lower viewpoint lets the stream reach the required geometry | Portable access and posture change coverage | PW2-004 |
| A wide stream leaves a stubborn window patch | Apply soap, switch to water and sweep the foamed surface | The coating remains until rinsed or recalled. Rinsing makes the prepared dirt easier to clear. | Pre-treatment and accepted surface conversion are distinct | PW2-005, PW2-006 |
| Some of the reusable soap is deployed | Rinse the coating, or repeat the demonstration with recall | Both ways return deployable supply; recall removes foam without itself cleaning the patch | Supply recovery and coverage credit are separate | PW2-006 |
| Overall progress is high but one part is unfinished | Locate it with the list and selected-part highlight; use the dirt highlight on its surface | The overlay identifies what to aim at. It does not remove residue or complete a task. | Information is distinct from treatment and progress | PW2-007 |
| Only one required part remains below acceptance | Remove its remaining dirt, then follow the finish prompt | The job becomes complete and the Career settlement is available. No second cleaning job is part of the result. | The job is gated by accepted coverage on all assigned parts | PW2-008 |

## Strategic and experiential structure

A wide pass gives a useful footprint when little pressure is needed.
A tight angle can justify a different standing position, a placed ladder
or a narrower nozzle. Foam adds a preparatory pass but reduces the water
effort on stubborn dirt. Its deployment temporarily uses part of the
same reusable supply. To finish, choose the next actual task from the
list rather than relying on the van's appearance alone.

## Replay and variation

- Compare water alone with a foamed pass on a stubborn patch. Compare
  recall versus rinsing when the foam stock is low.
- Once the exterior looks clear, check the task list and enter the
  cargo bay before closing the job. Missing required surfaces cannot
  be replaced with repeated washing of already complete surfaces.
- The precise per-part tolerance, exact refill timing and behaviour
  after closing or relaunching the executable remain unmeasured.
- Claim IDs: PW2-002–PW2-008.

## Adjacent systems and history

- The original game's first `Clean the Van` scope includes the
  same coverage gate but uses the garage assignment and a different
  rule boundary for detergent. The sequel's assigned interior,
  optional foam and reusable capacity apply here.
- Phased objects, advanced tools and later Career jobs require
  independent scoped evidence.
- Claim IDs: PW2-001, PW2-002, PW2-005, PW2-006, PW2-008.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-008`, `ACT-048`, `ACT-202`, `ACT-446`, `ACT-731` | route, carried ladder, stance, applicator and footprint choice |
| System Behaviour | `SYS-630`, `SYS-1544`, `SYS-1545` | lasting treatment, foam preparation and reusable supply |
| Constraint | `CON-516`, `CON-812` | accepted coverage and authorised ladder positions |
| Information | `INF-329`, `INF-331` | aggregate and individual progress, spatial highlight |
| Objective | `OBJ-168` | first van's completed coverage and credited result |
| Time | `TIM-003` | continuously directed treatment during live control |

Canonical signature:

`ACT-008,ACT-048,ACT-202,ACT-446,ACT-731; SYS-630,SYS-1544,SYS-1545; CON-516,CON-812; INF-329,INF-331; OBJ-168; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `533` (`GAME-0001`–`GAME-0533`).
- Exact genome matches: none.
- Tied near matches: `GAME-0279` — PowerWash Simulator (`10 / 14 = 0.714286`).
- Supported combination subsets: `COMB-0271`.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0279` — PowerWash Simulator | `ACT-008`, `ACT-048`, `ACT-202`, `ACT-446`, `CON-516`, `INF-329`, `INF-331`, `OBJ-168`, `SYS-630`, `TIM-003` | Both accept new washer coverage and require completed parts, with posture and highlights guiding access. The first game uses the garage van and step stool. The sequel adds its cargo interior, constrained ladder placement, adjustable fan orientation and foam that deposits before rinsing and returns to the nozzle. | Tied near (`0.714286`) |

### Preserved research notes

- New genes: `ACT-731`, `SYS-1544`, `SYS-1545`, `CON-812`.
- Classification result: `New gene`.
- Evidence and reasoning: reusable staged foam is independent of accepted
  cleaning. The aligned applicator and specific ladder positions affect
  how a player reaches and treats valid surface. `COMB-0271` is
  supported unchanged by the sequel's live treatment and coverage gate.

## Taxonomy impact

- Registry changes: four Active additions and ten transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_281](../../../research/taxonomy-changes/TAXONOMY_CHANGE_281.md).

## Negative results

- Evidence does not require a universal order for washing the assigned
  van parts, an exact foam capacity or an exact clean percentage per
  component. No physical runoff rule is inferred from wetness effects.
- A finish prompt and reward do not imply a second payment for the
  same work. Exact autosave and relaunch behaviour were not exercised.
- Paid upgrades, multiplayer recall fixes and every optional challenge
  are outside the model.

## Delta summary

## New facts

- [Observation | Corroborated | High] Foam can prepare a patch and
  return to the reusable supply, while only effective treatment meets
  the coverage gate for the job.

## New genes

- [Observation | Corroborated | High] Four definitions in
  `TAXONOMY_CHANGE_281`.

## New combinations

- [Observation | Corroborated | High] `COMB-0271` gains another scoped
  supporter. The combination predicate is unchanged.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_281`.

## New questions

- Which exact job-state fields are retained on a clean Xbox relaunch,
  and when does the final finish transition write them?

## Next recommended game

- [Hypothesis | Limited | Medium] Examine an authored ship battle in
  the original Dreamcast *Skies of Arcadia* under Selection 042.
