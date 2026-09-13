---
game_id: GAME-0279
slug: powerwash-simulator
game_title: PowerWash Simulator
analysis_status: reviewed
reviewed: 2026-09-08
combination_ids:
  - COMB-0271
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-202
    - ACT-446
  system:
    - SYS-630
  constraint:
    - CON-516
  information:
    - INF-329
    - INF-331
  objective:
    - OBJ-168
  time:
    - TIM-003
---

# Game: PowerWash Simulator

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / build: current unmodified English Windows Steam application
  `1290000`, package `1656019`, public branch build `20240979` with branch
  timestamp 2025-10-03; checked 2026-09-08. FuturLab's 2025-05-29 release is
  labelled the final content update but does not name a semantic client
  version, so the build observation and update label remain separate claims.
- Product boundary: the original **PowerWash Simulator**, currently developed
  and published by FuturLab in Valve application data. It is not PowerWash
  Simulator 2. All separately listed downloadable packs, including delisted
  packs that remain available to owners, are outside this packet.
- Platform, input and mode: Windows, English interface, mouse and keyboard,
  solo Career on a fresh profile, Classic wash behaviour. Career has no
  difficulty selector, time limit, water budget, final score or failure state.
- Entry: first actionable tutorial control in **Clean the Van**, the first
  Career vehicle job in the Home Garage, with the starting washer and supplied
  step stool.
- Primary decision loop: inspect overall and per-part completion; request the
  Dirt Highlight or select an incomplete part when visual dirt is ambiguous;
  move and change posture or reposition the step stool to expose its geometry;
  aim and sustain the washer over untreated area; read the permanent clean
  state and progress response; then choose the next incomplete part until each
  named target reaches its accepted clean threshold.
- Positive terminal: the final required part produces the accepted job-complete
  state, five stars and the job's total `$150` Career credit. Continue to the
  Career surface, save or use the enabled autosave, relaunch, and confirm that
  **Clean the Van** remains complete and the credited progression persists.
- Non-success control: Career provides no negative settlement for this job. If
  the player saves and leaves while a part remains incomplete, the same job
  returns with partial wash progress retained and no completion credit. This is
  an interruption state, not an invented failure terminal.
- Included: local navigation; portable step-stool placement; crouched and prone
  access; continuous washer aim and held-or-toggled output; persistent accepted
  surface treatment; overall and per-part progress; on-demand residual-dirt and
  selected-part highlighting; total accepted coverage; job settlement,
  retained Career credit and the live real-time update while washing.
- Excluded: online co-op; Free Play; Time and Water Challenges; every later
  Career, Bonus, Seasonal or Special Pack job; all DLC; the sequel; detergent,
  shop purchases, washer upgrades and long-term business economy; alternate
  equipment optimisation; the optional red-nozzle achievement route; story
  beyond messages visible before this terminal; account achievements;
  screenshots, official art, third-party assets and all audiovisual evidence.
- Reproducible parameterisation: install app `1290000`, select English, confirm
  the public branch build and create a fresh solo Career. Start **Clean the
  Van**, keep ordinary starting equipment, and clean the named vehicle parts in
  a fixed clockwise order, moving the supplied step stool only when height
  requires it and using crouch or prone for low geometry. Use the Details list
  and Dirt Highlight to locate any incomplete part, reach accepted completion,
  continue to Career, save, relaunch and verify retention. Part names, exact
  dirt geometry, nozzle choice, tolerance, payment components and bindings are
  game-scoped parameters.
- Potential scoped modules: one Time or Water Challenge; one co-op Career job;
  a later equipment-and-detergent job; any one separately named pack.
- Direct-play status: not conducted. Current official textual material plus one
  publisher-linked job reference and one complete secondary written route
  establish the declared mechanics and terminal. No video or audio was opened,
  played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PWS-001` | App `1290000` is the lawfully offered Windows original, package `1656019`, currently credited to FuturLab, with separate DLC products | Confirmed | Direct | High | P1 |
| `PWS-002` | The current public branch observation is build `20240979` dated 2025-10-03; no semantic version is asserted for it | Observation | Corroborated | Medium | S1, P5 |
| `PWS-003` | Career is a money-earning story mode distinct from Free Play, Time Challenge and Water Challenge | Confirmed | Direct | High | P2, P4 |
| `PWS-004` | Clean the Van is the first Career vehicle job, located in the Home Garage, with the starting washer and one step stool | Observation | Corroborated | High | P6, S2 |
| `PWS-005` | Washer output can be held or toggled and may be aimed independently in Aim Mode | Confirmed | Direct | High | P2, P3 |
| `PWS-006` | Newly washed eligible area persists and advances the job and component completion measures; already accepted overlap does not add new treatment | Observation | Corroborated | High | P3, S2 |
| `PWS-007` | The job exposes aggregate progress and per-part percentages in Details | Confirmed | Direct | High | P3 |
| `PWS-008` | Dirt Highlight marks residual dirt and selecting a Details item highlights that component in the world | Confirmed | Direct | High | P2, P3 |
| `PWS-009` | Crouch, prone and movable steps change which surface geometry can be reached or inspected | Confirmed | Direct | High | P3 |
| `PWS-010` | Each part settles at an accepted tolerance rather than requiring every rendered point to be geometrically untouched by dirt | Observation | Corroborated | Medium | S2 |
| `PWS-011` | Completing the first job records five stars and `$150` total Career credit | Observation | Corroborated | High | P6, S2 |
| `PWS-012` | Career has no time pressure or final score, while the separate Challenge Mode supplies time and water limits | Confirmed | Direct | High | P2, P4 |
| `PWS-013` | Autosave or manual save retains wash progress; leaving incomplete does not create a failure result | Confirmed | Direct | High | P2, P4 |

## Basic data

- Release / origin: FuturLab; released 2022-07-14. Valve's current product data
  lists FuturLab as developer and publisher; Square Enix Collective remains an
  official historical publisher page, not the current publisher claim.
- Platform or physical form: English Windows Steam application `1290000`, one
  fresh-profile solo Career **Clean the Van** job.
- Puzzle family: continuous spatial coverage; residual-state search; bounded
  task completion.
- Primary and official sources, accessed 2026-09-08:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=1290000&cc=ua&l=english),
    for exact title, current developer/publisher, Windows support, release,
    categories, package, lawful offer and separately listed DLC applications.
  - **[P2]** [FuturLab's current PowerWash Simulator FAQ](https://futurlab.freshdesk.com/support/solutions/articles/204000073336-powerwash-simulator-faqs),
    for Career, Free Play and Challenge boundaries, online-only multiplayer,
    Aim Mode, Dirt Highlight choices, autosave/manual save and wash modes.
  - **[P3]** [the developer-authored Steam FAQ](https://steamcommunity.com/app/1290000/discussions/0/3191368254812352852/),
    for Dirt Highlight, per-part Details percentages, component selection
    highlight, crouch, prone, ladders/steps and toggled washer output.
  - **[P4]** [Square Enix Collective's official product page](https://collective.square-enix-games.com/en_US/games/powerwash-simulator),
    for Career jobs, no time pressure or final score, and Free Play separation.
  - **[P5]** [FuturLab's Steam announcements](https://steamcommunity.com/app/1290000/announcements/),
    for the 2025-05-29 final-update label and later original-versus-sequel and
    pack-availability notices without a semantic client version.
  - **[P6]** [the publisher-linked PowerWash Simulator Wiki job record](https://powerwashsimulator.wiki.gg/wiki/Clean_The_Van),
    for first-job identity, Home Garage, starting washer, step stool, part list,
    star progression and `$150` total credit.
- Corroborating textual sources, accessed 2026-09-08:
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/1290000),
    for public build `20240979`, its branch timestamp and Windows depot
    manifest; a secondary distribution observation.
  - **[S2]** [the complete TrueTrophies Career walkthrough](https://www.truetrophies.com/game/PowerWash-Simulator/walkthrough/3),
    for the tutorial order, part-level acceptance tolerance, Details workflow,
    first-job stars/credit and retained progress behaviour.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P6` and `S1`–`S2` under the declared app, package, build, platform,
  fresh profile, exact job, entry, exclusions and retained terminal; rules
  reasoning, not direct play.
- Claim IDs: `PWS-001`–`PWS-013`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly move the washer around the Home Garage and van.
- Existing `ACT-048`: pick up, carry and place the free rigid step stool so a
  different portion of the van becomes reachable.
- Existing `ACT-202`, generalised by
  [`TAXONOMY_CHANGE_039`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_039.md):
  crouch or go prone to change reachable tool and viewing angles. Combat is a
  carrier parameter, not part of the portable posture action.
- New `ACT-446`: aim the continuous washer and sustain or toggle its stream over
  reachable area. The result depends on the traced coverage over time, not one
  discrete hit.
- Lower-ID scan: reject `ACT-341`, because carrying a stool is not a generic
  read/open/repair fixture interaction; `ACT-159`, because dirt is not one
  terrain cell removed to open topology; `ACT-161`, because the target is not a
  hostile receiving a strike; `ACT-245`, because no finite yield enters
  inventory; and `ACT-272`, because that firearm-maintenance action is a
  discrete owned-item transaction gated by oil.
- Claims: `PWS-004`–`PWS-006`, `PWS-009`.

### System Behaviour Genes

- Existing `SYS-630`, generalised by `TAXONOMY_CHANGE_039`: intersect a moving
  applicator footprint or stream with eligible surface, persist newly accepted
  treatment and advance task progress only for that new treatment. Handheld
  versus vehicle carrier and consumed versus unlimited material are parameters.
- Candidate `SYS-824` is merged into `SYS-630`; its proposed distinction was
  only the PowerWash carrier, target geometry and absence of fertilizer.
- Lower-ID scan: reject `SYS-079`, whose processing is an exact-once contact per
  named face and whose repeat contact fails the puzzle; reject object-damage,
  discrete repair and cosmetic-mark systems because none records continuous
  accepted area as task progress.
- Resolution order: active stream intersects eligible dirty area; newly
  accepted area changes state; component and aggregate progress update; overlap
  adds no new treatment; the final accepted component enables settlement.
- Claims: `PWS-005`, `PWS-006`, `PWS-010`.

### Constraint Genes

- Existing `CON-516`, generalised by `TAXONOMY_CHANGE_039`: settlement requires
  the accepted treated area to meet the declared threshold on the assigned
  target. Field/object geometry, partial/total threshold and explicit/automatic
  collection are parameters.
- Candidate `CON-619` is merged into `CON-516`; total coverage is one threshold
  value, not a new constraint family.
- Lower-ID scan: reject `CON-091`, because already cleaned area may be washed
  again without failure; route-checkpoint, object-count and delivery-quota
  constraints do not test accepted surface coverage.
- Scarcity: there is no deadline, finite water budget, required detergent or
  failure stock in this Career packet. Residual dirty area is a completion
  condition, not a consumable resource.
- Claims: `PWS-006`, `PWS-010`, `PWS-012`.

### Information Genes

- Corrected new `INF-329`: overall job percentage plus the Details list and
  per-part percentages expose measured aggregate and component completion.
- New `INF-331`: on request, Dirt Highlight spatially marks residual dirt and a
  selected incomplete Details item flashes as a whole. This is separate from
  the numeric measure and does not change the target.
- Lower-ID scan: reject `INF-252` and `INF-253`, whose definitions join field,
  machine, fill, contract offer, borrowing and collection state; `INF-265`,
  whose highlight is one part of learned monster investigation; and `INF-293`,
  whose targets are classified investigation objects and settlement results.
- Claims: `PWS-007`, `PWS-008`.

### Objective Genes

- New `OBJ-168`: bring every eligible surface of one bounded task to its
  accepted target state, settle the credit and retain the surrounding
  progression after reload.
- Lower-ID scan: reject `OBJ-027`, which additionally requires exactly one
  processing contact per surface and an exact return pose; and `OBJ-119`, which
  begins by accepting and borrowing equipment for a sampled field contract and
  ends through an explicit collection action. Those are not parameters of this
  first Career job.
- Success and non-success: the accepted five-star, `$150`, reload-retained job
  is success. Saved partial progress is an unfinished state; no negative
  settlement is manufactured.
- Claims: `PWS-010`, `PWS-011`, `PWS-013`.

### Time Genes

- Existing `TIM-003`: surface intersection and treatment update continuously
  while the washer runs and the player can still move or aim. The absence of a
  deadline does not make that live operation discrete.
- Reject candidate reuse of `TIM-002`: it explicitly excludes continuous
  real-time state change. Waiting with the washer inactive causes no failure,
  but sustained or toggled output changes state over time.
- Claims: `PWS-005`, `PWS-006`, `PWS-012`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Career opens Clean the Van | Accept first actionable control | Starting washer, dirty van, job measures and step stool are available in Home Garage | exact entry | `PWS-003`, `PWS-004` |
| One dirty part is reachable | Aim and sustain or toggle the washer across new area | Accepted dirt state clears continuously and both part and job progress rise | live coverage becomes persistent task state | `PWS-005`–`PWS-007` |
| The stream crosses already accepted area | Continue over the overlap | No equivalent new treatment or progress is added | overlap is not new coverage | `PWS-006` |
| Low or high geometry remains | Crouch, go prone, or place the step stool, then aim again | The avatar-tool relation exposes an angle that standing floor access lacked | posture and portable access change reach | `PWS-004`, `PWS-009` |
| Visual inspection cannot locate the residue | Request Dirt Highlight or select an incomplete Details item | Residual dirt or the addressed part flashes without being cleaned | locator information is separate from treatment | `PWS-007`, `PWS-008` |
| A part looks clean but is below its accepted threshold | Attempt to finish elsewhere | Details retains that part as incomplete and the job does not settle | measured acceptance outranks appearance | `PWS-007`, `PWS-010` |
| The final part crosses its accepted threshold | Continue | Job completion, five stars and `$150` total credit settle | positive terminal | `PWS-010`, `PWS-011` |
| Completed Career state is saved and relaunched | Reopen Career | Clean the Van remains complete and its progression remains credited | retained terminal | `PWS-013` |
| An incomplete state is saved and reopened as a control | Leave and resume | Partial washing returns without success or failure settlement | interruption is not defeat | `PWS-013` |

## Strategic and experiential structure

- Planning horizon: choose a sweep order over named parts, then switch from
  broad coverage to local residual search as the completion measure converges.
- Local tactics: stance, step-stool position, distance, angle and stream width
  determine reachable coverage and wasted overlap.
- Medium-term structure: per-part measurements identify the next target class;
  spatial highlights then reduce the final search without doing the cleaning.
- Reversible versus irreversible: aim, stance and stool placement are
  reversible; accepted clean area and Career settlement persist. Rewashing an
  accepted area is legal but adds no new state.
- Failure attribution: there is no ordinary failure. The interface distinguishes
  incomplete part, spatially hidden residue and accepted completion, while a
  save/reload distinguishes retained progress from an arbitrary stopping point.
- Player trust: visual cleanliness is advisory; the declared percentages,
  highlights and part-completion chime are authoritative.
- Claims: `PWS-006`–`PWS-013`.

## Replay and variation

- What changes: sweep order, nozzle choice, stance transitions, stool position,
  overlap and the moment at which the player queries Details or highlights.
- What does not change: van, named parts, starting tool set, authored dirt,
  accepted completion predicate and Career credit.
- Randomness or procedural generation: none admitted in this job.
- Multiple viable strategies: broad panel-first, component-by-component and
  highlight-led cleanup can all reach the same accepted terminal.
- Typical replay motive: efficiency, the excluded red-nozzle achievement or
  relaxed Free Play. None changes this packet's signature.

## Adjacent systems and history

- Direct predecessor context: the original game's 2025 final content update is
  part of product history; PowerWash Simulator 2 is a separate product.
- Variants: co-op changes player authority; Challenge introduces deadline or
  water scarcity; later Career adds equipment and business progression; packs
  change target content. All remain outside this signature.
- Similar games: Farming Simulator 25 independently converts continuous
  applicator coverage into retained surface treatment and gates job settlement
  on accepted target coverage. Its carrier is a filled vehicle implement over
  a sampled field contract; this packet uses a handheld unlimited-water stream
  over named vehicle parts with residual-state search and automatic completion.
- Important difference from exact-once surface puzzles: overlap is harmless but
  unproductive; repeated contact neither invalidates the attempt nor consumes a
  per-surface contact allowance.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-202`, `ACT-446` | van, step stool, washer, nozzle and bindings are parameters |
| System Behaviour | `SYS-630` | stream footprint, dirt geometry, tolerance and unlimited water are parameters |
| Constraint | `CON-516` | named target set and total accepted threshold are parameters |
| Information | `INF-329`, `INF-331` | percentage precision, list structure and highlight colours are parameters |
| Objective | `OBJ-168` | five stars, `$150`, successor and persistence control are parameters |
| Time | `TIM-003` | no deadline; live treatment only while output is active |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `278` (`GAME-0001`–`GAME-0278`).
- Exact genome matches: none.
- Tied near matches: `GAME-0112` — Human: Fall Flat (`3 / 15 = 0.200000`).
- Supported combination subsets: `COMB-0271`.
- Scan date: 2026-09-08.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0112` — Human: Fall Flat | `ACT-008`, `ACT-048`, `TIM-003` | Both packets combine directly steered movement, portable rigid-object placement and continuous real-time resolution. Human: Fall Flat makes two-hand articulated grip, leverage, rigid-body physics and exit traversal the puzzle; PowerWash makes posture, a continuous applicator, accepted surface coverage, measured component completion, residual-state location and retained job settlement the decision layer. | Near, `3 / 15 = 0.200000` |

The selected neighbour is the strongest whole-genome match. Farming Simulator
25 remains the narrower comparison corridor for `SYS-630 + CON-516` and the
independent second carrier of `COMB-0271`; its larger contract genome gives a
lower whole-signature Jaccard score.

### Preserved research notes

- New genes: `ACT-446`, corrected `INF-329`, new `INF-331` and `OBJ-168`.
- Reused genes: `ACT-008`, `ACT-048`, generalised `ACT-202`, generalised
  `SYS-630`, generalised `CON-516` and `TIM-003`.
- Classification result: reuse-first correction, two candidate merges, one
  information split and one independently supported combination.

## Taxonomy impact

- [`TAXONOMY_CHANGE_039`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_039.md)
  generalises `ACT-202`, `SYS-630` and `CON-516`; merges `SYS-824` into
  `SYS-630` and `CON-619` into `CON-516`; and separates spatial residual-state
  location into `INF-331` while `INF-329` retains measurement.
- No earlier reviewed game signature changes. Farming Simulator 25 remains a
  carrier of `SYS-630` and `CON-516` and gains only the independently verified
  `COMB-0271` relation.
- Candidate-term review is recorded in `knowledge/genes/CANDIDATE_TERMS.md`.
  Product, job, tool, object, part, payment, build and platform names remain
  game-scoped parameters.

## Negative results

- `ACT-341` is not a catch-all for moving the stool, and `TIM-002` contradicts
  the continuous surface update. Both are removed from the candidate signature.
- A nozzle-selection gene is not admitted: the bounded route can complete with
  the starting tool set without treating optional efficiency or the excluded
  achievement as a required decision boundary.
- No water, detergent, money, deadline, life or failure constraint is admitted.
  Challenge Mode demonstrates that time and water budgets are separate rulesets.
- No generic payment-system gene is invented. The finite retained settlement
  is owned by `OBJ-168`; its internal value is a parameter.
- No video or audio evidence was used.

## Delta summary

## New facts

- [Confirmed | Direct | High] `PWS-003`, `PWS-005`, `PWS-007`–`PWS-009`,
  `PWS-012` and `PWS-013` replace the candidate's secondary-only assertions
  with current FuturLab and developer-authored textual evidence.
- [Observation | Corroborated | High] `PWS-004`, `PWS-006`, `PWS-010` and
  `PWS-011` establish the exact first-job route, accepted coverage and retained
  settlement.

## New genes

- [Observation | Corroborated | High] `ACT-446`, `INF-329`, `INF-331` and
  `OBJ-168` isolate continuous application, numeric completion, spatial residual
  location and the retained all-surface terminal.

## New combinations

- [Pattern | Corroborated | High] `COMB-0271` — continuous applicator coverage
  becomes persistent surface treatment and accepted target coverage gates the
  same bounded task's settlement, independently carried by Farming Simulator
  25 and PowerWash Simulator.

## Taxonomy changes

- [Confirmed | Corroborated | High] `TAXONOMY_CHANGE_039` removes two
  parameter-only duplicates, makes posture and coverage boundaries portable,
  and splits measurement from spatial location without changing an earlier
  reviewed signature.

## New questions

- Does a future non-cleaning treatment game support `INF-331` independently,
  or is its residual-state predicate specific to cleaning tasks?
- Does a later Water Challenge add a reusable continuous-consumption constraint
  without changing the coverage-to-state system?

## Next recommended game

- None inside Batch 016. The next recorded unit is the independent final batch
  audit with full repository, web, build, browser and axe acceptance.

## Why this game

- The selection asked whether a low-pressure cleaning activity becomes a
  bounded analyzable task through its coverage rule or merely through theme.
  The result is a portable coverage-to-state system and coverage-settlement
  constraint shared with agriculture, plus two separate information boundaries
  that make residual geometry measurable and locatable.
