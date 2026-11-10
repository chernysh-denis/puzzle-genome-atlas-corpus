---
game_id: GAME-0493
slug: wheres-my-water
game_title: Where's My Water?
analysis_status: reviewed
reviewed: 2026-10-04
combination_ids:
gene_ids:
  action:
    - ACT-666
  system:
    - SYS-1325
    - SYS-1326
    - SYS-1327
  constraint:
    - CON-761
    - CON-762
  information:
    - INF-001
  objective:
    - OBJ-002
    - OBJ-014
  time:
    - TIM-003
---

# Game: Where's My Water?

## Analysis scope

- Version / ruleset: original paid English 2011 iOS Swampy puzzle packet;
  Meet Swampy level 1-3, Choose Wisely. Contemporary written rules and the
  reconciled early-level diagram establish this target, not an installed
  binary version or modern-port parity.
- Primary decision loop: swipe out eligible soil, observe released water,
  revise the channels while fluid remains in motion and allocate the finite
  batch between optional duck collection and compulsory receiver delivery.
- Entry and exit: fresh-reset 1-3 with intact soil, fixed rocks, initial upper
  reservoir, three uncredited ducks and the shower inlet; finish at accepted
  delivery and its result, or player abandonment/reset of a bad route. Earlier
  level qualification is entry configuration, not another game loop.
- Included: every allowed soil cut and retained cut, immutable stone,
  divisible live flow, branch allocation, merging and basins, finite initial
  water, sufficient-water duck collection, visible current geometry and
  collection feedback, fixed inlet delivery, completion speed/duck/overflow
  evaluation, pause affordance and reset as a fresh attempt.
- Excluded: poison, ooze, moss, switches, moving bars, bombs, balloons,
  steam, mud and hidden object discovery, none present in this packet;
  chapter unlock accounting, purchases, Free, Perry, sequel and other ports.
  Numeric fluid solver, dose, delivery threshold and score formula are not
  reconstructed. No assumption that collected ducks consume water.
- Potential scoped modules: mixed liquids and reactive vegetation; gated
  liquid mechanisms; replenishing-source packets; other characters' targets.
- Direct-play status: not conducted. No original application, binary hash,
  native execution, audiovisual playthrough or saved-data behaviour inspected.
  Two independently authored contemporary written accounts and the level
  diagram support qualitative rules; Disney material establishes the original
  product and input, not exact internal numbers or later-version equivalence.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| WMW-001 | The original paid iOS product launched with Swampy and 80 levels | Observation | Direct | High | F1 |
| WMW-002 | Soil swipes intervene in the environment rather than directly steering a moving water actor | Observation | Corroborated | High | F2, S1, S2 |
| WMW-003 | The reconciled 1-3 packet has upper reservoir, fixed stone channels, three duck targets and lower inlet | Observation | Corroborated | High | S1 diagram, S2 1-3 |
| WMW-004 | Open geometry controls live downward water motion, pools and branch allocation | Observation | Corroborated | High | S1, S2 |
| WMW-005 | Duck credit requires enough water, not merely one grazing particle, and is separate from delivery completion | Observation | Corroborated | High | S1, S2 |
| WMW-006 | Completion evaluates speed, duck credit and extra delivered water through separate bonus contributions | Observation | Limited | Medium | S2 result; S1 corroborates optional duck score only |
| WMW-007 | A fresh reset restores the puzzle; ordinary swiping removes eligible soil rather than recreating stone or soil | Observation | Corroborated | Medium | S1 diagram, S2 restart |
| WMW-008 | This reservoir packet allocates finite initial water, unlike the later replenishing 1-5 | Observation | Corroborated | High | S1 diagram, S2 1-3 and 1-5 |
| WMW-009 | The exposed layout supports route prediction, not claims of exact solver constants or hidden numerical quotas | Observation | Limited | Medium | S1 diagram, S2 |

## Basic data

- Release / origin: Disney Mobile, September 22, 2011; launch target is iPad,
  iPhone and iPod touch. This genome is one early ordinary puzzle, not the
  union of every launch chapter or later update.
- Platform or physical form: original iOS touch-screen application;
  structured target must match `PLAT-IOS` in the platform registry.
- Puzzle family: soil-authored physical fluid routing with live allocation.
- Primary sources:
  - [F1 — Disney Mobile launch announcement](https://www.prnewswire.com/news-releases/disneys-first-original-character-for-mobile-splashes-onto-the-app-store-in-wheres-my-water-130342928.html),
    September 22, 2011, inspected product/platform/launch content.
  - [F2 — Disney Mobile's Bart Decrem interview](https://gamesbeat.com/bart-decrem-says-mobile-games-will-spawn-a-new-generation-of-disney-characters-interview/),
    July 14, 2012 edited first-person account; core input, not exact level data.
  - [F3 — authorised current product listing](https://apps.apple.com/us/app/wheres-my-water/id449735650),
    legal product navigation only; newer contents do not prove launch parity.
- Independently authored contemporary play accounts:
  - [S1 — JohnB review and attached early walkthrough](https://jayisgames.com/review/wheres-my-water.php),
    October 3, 2011 review; later general-guide additions separated from 1-3.
    [Inspected 1-3 diagram](https://jayisgames.com/images/wheres-my-water/level103.jpg).
  - [S2 — Talor Berthelson iOS walkthrough](https://www.gamezebo.com/walkthroughs/wheres-my-water-walkthrough/),
    September 25, 2011 visible HTML metadata, first levels and result account.
- Checked: October 4, 2026. No exact installed version, direct play, internal
  quantities or uninspected native loss-popup trigger are claimed.
- Claim IDs: WMW-001–WMW-009.

## Mechanical decomposition

### Action Genes

- `ACT-666`: chosen finger path removes the intersected compatible soil.
  Cutting a narrow opening can release only a trickle to a secondary route.
  The gesture is an environmental edit, not a command assigning water velocity.
- Parameters: sweep shape, extent and time; no harvested inventory.
- Claim IDs: WMW-002–WMW-004, WMW-007.

### System Behaviour Genes

- `SYS-1325`: released water deforms, flows, divides, reunites and pools
  against actual terrain. A hollow basin can retain water despite apparent
  connectedness; its outlet must be opened at a useful height.
- `SYS-1326`: adequate clean-water exposure credits each optional duck while
  the delivery attempt remains active. An underfed branch need not credit it.
- `SYS-1327`: result feedback converts completion speed, collected ducks and
  extra receiver water into distinct score contributions. No exact weights
  or universal linearity are asserted.
- Claim IDs: WMW-004–WMW-006.

### Constraint Genes

- `CON-761`: ordinary soil removal is restricted to the editable material
  mask; rocks remain solid and cuts cannot be restored during that attempt.
- `CON-762`: this packet starts with one finite batch. Diverting too much
  away from a required receiver can leave insufficient recoverable water;
  further cuts do not create a new source. No universal all-level rule follows.
- Numeric reservoir/duck/receiver quantities are parameters, not new genes.
- Claim IDs: WMW-003, WMW-007, WMW-008.

### Information Genes

- `INF-001`: visible soil, rock, water, ducks and inlet disclose the current
  routing state. Predicting a flow is not a promised future-preview display.
- Exact unknown simulation values do not justify a random-transition gene.
- Claim IDs: WMW-003, WMW-009.

### Objective Genes

- `OBJ-014`: deliver the required clean-water payload quantity into the fixed
  inlet leading to Swampy's shower. Duck completion is not the inlet gate.
- `OBJ-002`: improve optional result score via collection, speed and overflow;
  a higher score is distinct from accepting compulsory delivery.
- Claim IDs: WMW-004–WMW-006.

### Time Genes

- `TIM-003`: cuts remain available while released fluid progresses.
  Safe preparatory cuts and pause do not make the running state turn-based.
  Performance time is not evidence for an expiring hard level deadline.
- Claim IDs: WMW-004, WMW-006, WMW-007.

## Reproducible transitions

| Before | Action | Qualitative source-derived resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Water held above intact soil | Cut an outlet below its current surface | Newly free space permits downward release | Environmental action and fluid response differ | WMW-002, WMW-004 |
| Stone occupies part of a route | Swipe through stone and adjacent soil | Soil can disappear; the stone barrier persists | Material compatibility is causal | WMW-003, WMW-007 |
| Reservoir can feed two channels | Open the main channel and a smaller side opening | Actual geometry divides the batch rather than granting equal water to both | Allocation matters | WMW-004, WMW-008 |
| Water has pooled below a high exit | Open a lower compatible outlet | Retained water can continue down the new channel | Connectivity alone is insufficient | WMW-004 |
| Duck has not received enough water | Divert more of the remaining batch through its location | Adequate exposure credits that target without itself completing the delivery | Threshold collection is not simple contact | WMW-005 |
| Some ducks remain uncredited | Deliver enough clean water to the inlet | Mandatory delivery can complete with imperfect optional collection | Evaluation is not qualification | WMW-005, WMW-006 |
| Bad retained cuts or poor allocation | Select restart | A fresh attempt restores the initial layout and batch | Reset is not an in-attempt refill or soil painting command | WMW-007, WMW-008 |

These are source-reproducible qualitative tests, not tests run on a native
application or claims of bit-identical trajectories across device versions.

## Strategic and experiential structure

- Local decision: where and when to remove soil, including how much of a
  branch entrance to expose before the upper batch escapes.
- Medium-term planning: keep enough water routed through optional collectors
  without starving the inlet; preserve useful supports before opening them.
- Long-term structure: only one complete bounded attempt; chapter progression
  remains outside the signature.
- Common heuristic: prepare lower channels before releasing the reservoir,
  then leave a narrow secondary opening rather than indiscriminately carving.
- Failure attribution: route geometry and allocation expose a plausible cause
  of misses; unmeasured solver details limit quantitative prediction claims.
- Player-trust factors: visible protected rock, consistent terrain removal,
  threshold feedback and explicit fresh restart distinguish recoverable edits
  from irrecoverable escaped water.
- Claim IDs: WMW-002–WMW-009.

## Replay and variation

- Same fresh 1-3 begins from the same documented layout. Different gesture
  geometry and timing alter allocation and optional result.
- No procedural layout or stochastic selector is evidenced inside this packet.
  This does not assert native cross-device solver determinism.
- Replay can pursue missing ducks or better speed/overflow result.
- Claim IDs: WMW-003–WMW-009.

## Adjacent systems and history

- Original identity is separately supported by F1. Neither current App Store
  characters nor other mobile releases establish original-level parity.
- A linked-pipe propagation model or one rigid moving candy cannot stand in
  for divisible fluid and soil-channel geometry.
- Later mixed-liquid, growing-plant and gated-source packets require their
  own evidence and should not be added merely because the product contains them.
- Claim IDs: WMW-001–WMW-009.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-666` | swipe geometry and time |
| System Behaviour | `SYS-1325`, `SYS-1326`, `SYS-1327` | fluid tuning, wetting quota, score contributions |
| Constraint | `CON-761`, `CON-762` | editable mask, initial water quantity |
| Information | `INF-001` | current-state visibility |
| Objective | `OBJ-002`, `OBJ-014` | optional score and required delivered quantity |
| Time | `TIM-003` | live cadence and pause |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `492` (`GAME-0001`–`GAME-0492`).
- Exact genome matches: none.
- Tied near matches: `GAME-0021` — Cut the Rope (`4 / 15 = 0.266667`).
- Supported combination subsets: none.
- Scan date: 2026-10-04.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0021` — Cut the Rope | `INF-001`, `OBJ-002`, `OBJ-014`, `TIM-003` | Both expose a live indirectly controlled payload, a fixed receiver and optional evaluation. Where’s My Water? removes editable soil and allocates divisible fluid through actual basins and sufficient-water collectors; Cut the Rope severs support links for one rigid candy, credits stars on contact and terminates boundary escape. Neither simple contact nor a rigid-body-only transition reproduces the fluid packet | Near, `0.266667` |

## Taxonomy impact

- `TAXONOMY_CHANGE_230` accepts six bounded additions and four unchanged
  transfers. Existing single-body, cell-pressure, 3D mixing/evaporation,
  embodied digging, tactical deformation and contact-only collection
  boundaries were reviewed and do not replace this packet. No older English
  gene boundary, signature or combination is changed.
- Named bilingual presentation review partitions all ten uses into three
  defining, six structural and one supporting role, with complete causal
  cards. Existing `FAM-005`, `FAM-007` and `FAM-010` cover authored routes,
  spatial fluid geometry and live intervention. Roles do not weight Jaccard.

## Negative results

- No external novelty claim or independent new combination accepted.
- Avoid single-contact collection, rigid-body-only fluid substitution,
  all-level finite supply and made-up countdown failure.

## Delta summary

## New facts

- [Observation | Corroborated | High] One finite split-flow packet distinguishes
  optional wetting credit from fixed receiver delivery (WMW-003–WMW-008).

## New genes

- [Observation | Corroborated | Medium] `ACT-666`, `SYS-1325`, `SYS-1326`,
  `CON-761`, `CON-762`; their eligibility, response and allocation differ
  from the reviewed counterexamples.
- [Observation | Limited | Medium] `SYS-1327` preserves the written three
  result contributions without inventing exact weights or arithmetic.

## New combinations

- [Observation | Direct | High] None: all 274 verified combinations were
  checked as proper subsets. One new carrier is not an independent pattern.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_230` admits six
  additions and four transfers; prior canonical signatures remain unchanged.

## New questions

- What native dose and result formula apply in the original installed build?
- Which later replenishing or reactive-liquid packets warrant another scope?

## Next recommended game

- [Hypothesis | Limited | High] Approved GAME-0494 Dead or Alive 2 ordinary
  Dreamcast edition, only after full GAME-0493 acceptance and stop window.
- Optimisation criterion: test attack/hold/throw and arena state after fluid
  routing without silently analysing Hardcore or Ultimate.
- Expected information gain: adversarial timing instead of soil-authored flow.
- Backlog impact: retain the amended Wii final subject at GAME-0495.

## Why this game

- [Hypothesis | Limited | High] Original iOS fluid allocation supplies a
  platform and causal contrast with the preceding PS3 combat chapter.
