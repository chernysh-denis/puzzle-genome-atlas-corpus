---
game_id: GAME-0547
slug: walkabout-mini-golf
game_title: Walkabout Mini Golf
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-747
    - ACT-748
  system:
    - SYS-1490
    - SYS-1586
    - SYS-1587
  constraint:
    - CON-815
  information:
    - INF-528
  objective:
    - OBJ-014
    - OBJ-294
  time:
    - TIM-003
---

# Game: Walkabout Mini Golf

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The putter calibration, par, course shape and controller are parameters.
A viewing teleport does not reposition the ball, and an enabled contact is
not a button-release launch.

## Analysis scope

- Version / ruleset: full English standalone Meta Quest release, Quest 2
  with one tracked Touch controller. The documentary ruleset was checked on
  2026-11-19 against the current developer support pages. The product first
  released in 2020; this is not a claim to have installed its launch build.
  Exact application binary, patch number, sensor sampling, physics constants
  and saved settings were not captured. No Early Access or Pocket Edition
  input scheme is selected.
- Structured analysis target: `PLAT-META-QUEST`, Meta Quest Store full game.
- Entry: at Welcome Island choose the base course Tourist Trap, Easy/day,
  ordinary solo Standard play on the currently remastered base course, starting at hole 1 of Full 18 with zero strokes
  on that hole. Explicitly turn Stroke Limit off and Grip to Putt on, use
  teleport movement and keep the ordinary putter calibration fixed. Tutorial
  completion and these settings are setup prerequisites. Start at the first
  tee before the first counted contact.
- Primary decision loop: inspect the current ball lie, cup and wooden banks;
  reposition the viewpoint or warp to the ball without changing that lie.
  Rehearse with the putter disabled, hold the enabling control and physically
  swing to contact the ball. Read the rolling result and stroke count, then
  prepare another contact from the legal resting lie until cup settlement.
- Positive exit: sink the ball in the first hole, accept its recorded stroke
  result relative to par two and stop before playing hole 2. A higher score
  than par is a completed result, not a failed clear. This bounded hole is
  not represented as a completed eighteen-hole round.
- Negative / continuation boundary: a miss continues from its legal lie;
  an abandoned unplayable ball can return to the previous position. With the
  optional stroke ceiling disabled, this packet has no declared count-based
  terminal loss. Native out-of-play volumes, reset delay and any additional
  penalty-count treatment were not measured and are not imported from real
  golf or Wii Sports Resort.
- Included: tracked club contact, trigger-enabled rehearsal, ball motion and
  collision, lawful next lie, out-of-play recovery, ball-independent viewing
  teleports, visible course geometry, wrist/scorecard information, counted
  putting and the first hole's result. Ordinary gravity is selected; no
  custom giant/miniature or alternate-gravity modifier is assumed.
- Excluded: Practice undo and freely placed practice balls, Stroke Limit-on
  thresholds, later holes and aggregate round victory, multiplayer order,
  Match Play, Race and Simultaneous modes, hidden-ball collection, foxhunts,
  DLC, flight and overhead God Mode, avatar customisation, hand tracking,
  shared-course access, real-world tournament rules and mobile touch swings.
- Potential modules: a complete multiplayer stroke-play card; no-score Practice
  restoration; hidden-ball collection and clue-driven putter unlocks.
- Direct-play status: no headset, controller, purchased installation, save,
  executable or input trace was run. Official written controls, support and
  course material were read. A dated Quest scorecard still was visually
  inspected; a Pocket Edition still from UploadVR’s hands-on report was used only to
  corroborate the first hole's broad geometry, never Quest controls or physics.
  No video or audio was played. Transitions below are source reconstructions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| WMG-001 | The full Quest game includes Tourist Trap. Standard scoring counts strokes; Practice permits repeated holes and undo, while Stroke Limit is optional. The chosen packet starts at its first easy hole. | Observation | Corroborated | High | P1, P2, P3, P4, P7, S1, S4 |
| WMG-002 | One tracked controller positions the putter. Physical face direction and swing strength influence the contacted ball; no release button launches it. With Grip to Putt enabled the current support page requires holding the trigger to activate the putter head. | Observation | Corroborated | High | P2, P5, S1, S2, S3 |
| WMG-003 | The ball rolls through authored terrain and contacts banks; pace and line can produce a miss rather than automatic cup entry. The first easy hole is a narrow lane opening into a broader cup area, with par two. | Observation | Corroborated | High | P4, S1, S2, S3, S4, S5 |
| WMG-004 | The next putt uses the legal resting lie. Viewing from another place or warping to the ball changes the player's viewpoint, not the ball's world position or stroke result. | Observation | Corroborated | High | P2, S1, S2, S3 |
| WMG-005 | Developer notes explicitly describe an out-of-bounds ball returning to its previous position. The rule is not an immediate failure on touching a wooden bank. Exact first-hole invalid volumes, timeout and extra penalty accounting are unmeasured. | Observation | Limited | Medium | P6, P2, S1 |
| WMG-006 | The wrist/scorecard exposes hole, strokes and score. A completed hole compares its counted strokes with par; one on this par-two hole is one under, two level and three one over. | Observation | Corroborated | High | P2, S1, S3, S4 |
| WMG-007 | Shot motion resolves continuously rather than as prescribed grid steps; view commands can still be used during that motion. There is no selected shot clock forcing a stationary ball to move. | Observation | Corroborated | High | S1, S2, S3, P2 |

## Basic data

- Release / origin: Mighty Coconut's full game first released on Quest on
  24 September 2020; current documentary support was checked on 19 November
  2026. The exact installed revision is unverified.
- Platform or physical form: standalone Meta Quest 2 with one tracked Touch
  controller. A PC-streamed version is not substituted for the analysis target.
- Puzzle family: physics and object manipulation, `FAM-007`.
- Primary sources:
  - **P1** [Meta Quest Store, Walkabout Mini Golf](https://www.meta.com/experiences/walkabout-mini-golf/2462678267173943/),
    the released standalone product and base-course package.
  - **P2** [Mighty Coconut's resources and general FAQ](https://www.mightycoconut.com/wmg-resources),
    Standard stroke scoring, other modes, Practice and accessibility controls.
    The evolving page's counts of courses or multiplayer seats are not fixed
    as launch-build rules.
  - **P3** [Official glossary](https://support.mightycoconut.com/kb/article/13-wmg-glossary/),
    updated 12 February 2026: Stroke Limit, teleport, warp-to-ball, Practice,
    flight and game-mode distinctions.
  - **P4** [Official Tourist Trap course page](https://www.mightycoconut.com/tourist-trap),
    day and night treatments and original authored island setting.
  - **P5** [Official putter/controller troubleshooting](https://support.mightycoconut.com/kb/article/23-putter-controller-tracking-troubleshooting/)
    and [accessibility guide](https://support.mightycoconut.com/kb/article/17-accessibility-features/),
    one controller and trigger-held head activation. The feature name is
    Grip to Putt; it does not establish an identical hardware button on every
    platform or historical build.
  - **P6** [Developer's Venice release notes, 25 April 2024](https://store.steampowered.com/news/app/1408230/view/5759616966664969967),
    Ice Lair correction explicitly explains falling out-of-bounds and return
    to the previous position. This is evidence of the recovery mechanism,
    not a measured Tourist Trap timeout or a cross-platform parity test.
  - **P7** [Developer's Tourist Trap remaster announcement, 15 December 2023](https://store.steampowered.com/news/app/1408230/view/5409450219976783331),
    describes environmental, animation, lighting and colour updates. P1 also
    identifies the remaster. The current target is not an unpatched 2020 map;
    old scorecard evidence corroborates par, not binary equivalence.
- Secondary sources:
  - **S1** [Paul Stuart's Quest 2 review](https://www.impulsegamer.com/walkabout-mini-golf-oculus-quest-2-review/),
    25 October 2020, tracked putting, banks, warp and motion-following,
    wrist fields and the original Tourist Trap course. Its launch ceiling
    is not the selected Stroke Limit-off rule.
  - **S2** [Andrew Courtney's written putting guide](https://vrlowdown.com/walkabout-mini-golf-tips/),
    face alignment, swing power, rehearsing through the disabled ball,
    course inspection and Practice. Numeric real-golf cup calculations and
    controller-calibration coefficients are not adopted.
  - **S3** [Fbs's written Steam guide](https://steamcommunity.com/sharedfiles/filedetails/?id=2812327682),
    first published 24 May 2022, updated 3 September 2024. Contact direction,
    power, moving-body observation, settings and Practice support the loop.
    It calls the activating control grip; the selected Quest mapping follows
    current P5's trigger wording, not an assumed Valve Index button.
  - **S4** [Dated Quest impressions and scorecard](https://apicodes.hatenablog.com/entry/Walkabout_Mini_Golf),
    page dated 27 March 2022, with a hosted image keyed `20201016`.
    The image key is not treated as an independently verified capture date.
    The Tourist Trap Full 18 scorecard was visually inspected:
    hole 1 has par two, a four-stroke result is retained and the round uses
    signed score. No new native play is claimed.
  - **S5** [UploadVR's first-hole Pocket Edition hands-on still](https://www.uploadvr.com/walkabout-mini-golf-pocket-edition-arrives-on-iphone-in-open-beta/),
    February 2024, corroborates narrow green, wider cup area, wooden edging and
    par two. Only geometry is used; neither its beta nor touch inputs are the
    selected released Quest edition.
- Claim IDs: WMG-001–WMG-007.

## Mechanical decomposition

### Action Genes

- Add `ACT-747`: an enabled tracked putter is swung into contact. Trigger
  release does not select a launch sample as it does for `ACT-499` bowling
  or `ACT-718` disc throwing.
- Add `ACT-748`: aim a viewing teleport or warp back to the ball while leaving
  its world-space lie untouched. This is not following-camera `ACT-610`
  around a separately steered actor or a portal transporting the payload.
- Claim IDs: WMG-002, WMG-004.

### System Behaviour Genes

- Add `SYS-1586` for contact-driven ball roll, pace, friction and bank response.
  `SYS-146` starts at launcher release and `SYS-995` includes pin-chain scoring;
  neither boundary is silently rewritten into grounded putter contact.
- Reuse `SYS-1490`: a legal unsunk rest becomes the next delivery origin.
- Add `SYS-1587`: restore an abandoned unplayable ball to its previous lie.
  No exact timeout or extra penalty is asserted. `SYS-1491` necessarily adds
  a penalty and distinguishes hazard-class fallback; that stronger claim is
  not transferred without a measured Quest result.
- Claim IDs: WMG-002–WMG-005.

### Constraint Genes

- Add `CON-815`: in the selected Grip to Putt setting, the enabling trigger
  must be held for the head to contact the ball. A disabled rehearsal does not
  spend a counted shot. Holding it is not a power meter or release gesture.
- `CON-800` is absent because the selected optional stroke ceiling is off.
  `CON-103` is absent because no finite command-card hand funds ordinary putts.
- Claim IDs: WMG-001, WMG-002.

### Information Genes

- Add `INF-528`: tracked head/ball/cup geometry and the wrist/scorecard's hole,
  stroke and signed-score fields support line and pace choice. No exact
  future trajectory or automatically correct force is shown or inferred.
- `INF-505` requires wind and a recommended disc, neither of which belongs to
  the selected putting hole. Do not infer them from Frisbee Golf.
- Claim IDs: WMG-003, WMG-004, WMG-006.

### Objective Genes

- Reuse `OBJ-014` for getting the ball into the fixed cup.
- Reuse `OBJ-294` for the counted result against par. Its generic penalty
  parameter does not supply a missing game-specific penalty formula.
- A three-stroke completion remains a completed hole; par is a benchmark,
  not a mandatory upper bound or a speed race.
- Claim IDs: WMG-006.

### Time Genes

- Reuse `TIM-003`: continuous shot motion and tracking remain live while
  a view command can still be supplied. There is no discretised exact-distance
  movement card and no promise of input-free deterministic sensor sampling.
- Preparation at a stationary lie has no selected countdown. That local
  freedom does not turn the entire physical shot into `TIM-002` or the
  locked, input-free resolution required by `TIM-001`.
- Claim IDs: WMG-007.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| The first tee holds the ball; Grip to Putt is on | Move the putter through the ball without holding the enabling trigger | The inactive head does not commit a contact or counted stroke | Rehearsal and commitment differ | WMG-002 |
| The ball is at rest | Hold the enabling trigger and swing into contact | Face direction and sampled movement launch the rolling response and count a putt | Contact, not button release, commits delivery | WMG-002, WMG-006 |
| The ball is on the same lie | Use a firmer physical stroke along a similar line | Pace changes the distance and later contacts; no exact coefficient is claimed | Strength is a physical input parameter | WMG-002, WMG-003 |
| A rolling shot meets the wooden edging | Let the contact resolve | The bank can redirect it within the hole | Ordinary bank contact is not immediate out-of-bounds failure | WMG-003, WMG-005 |
| A ball stops legally outside the cup | Warp to it and prepare the next shot | Continue from that same resting lie with the retained count | View movement is not ball relocation | WMG-004 |
| The same ball lies on the green | Aim a teleport to inspect from the side | Change viewpoint without replacing the ball or refunding the shot | Surveying is an information action | WMG-004 |
| A shot is in motion | Use the documented ball-following warp command | Change viewing position while physical resolution continues | Motion is not an atomic input-locked grid turn | WMG-007 |
| An eligible ball is abandoned outside play | Allow the invalid-position recovery to settle | Return it to its previous position; timing and any extra count remain unmeasured | Recovery is distinct from both a legal new lie and terminal loss | WMG-005 |
| A shot crosses near the cup but is not captured | Observe the physical result | Continue from the eventual lawful lie | Proximity or a line drawn over the hole is not completion | WMG-003, WMG-006 |
| The par-two first hole is completed in one, two or three counted strokes | Read the retained result | Respectively one under, level or one over | Good score and valid completion are separate | WMG-006 |
| A stationary ball has not been struck | Inspect and rehearse without a clock limit | No automatic putt or selected shot-clock defeat occurs | Time pressure is not invented | WMG-001, WMG-007 |

These are reproducible source-based cases, not a claimed headset test session.

## Strategic and experiential structure

Direction alone does not solve the hole. Contact speed determines whether
an aligned ball reaches the cup, stops short, passes it or contacts a bank.
A poor but lawful shot leaves a new angle for the next stroke and keeps its
count. Rehearsal can improve alignment without acting on the ball, while
teleporting reveals the same geometric problem from another viewpoint.

The narrow neck opens into a broader putting area; the cup is one fixed
receiver. A safe approach can accept another stroke, while an attempted ace
seeks a smaller final count. Native contact thresholds and exact lip-out
physics are unmeasured. No real-golf numerical coefficient is disguised as
reproduced code or a guaranteed hole-in-one recipe.

## Replay and variation

The selected remastered base-course easy hole is authored, not procedurally regenerated.
Physical execution changes from stroke to stroke. Replaying it for a better
score is separate from Practice undo, which has its own no-score state rules.
Stroke Limit-on's exact maximum is excluded deliberately: secondary guide
wording differs, whereas official material confirms the setting can be off.

## Adjacent systems and history

Golf Peaks commits a finite card's discrete trajectory; this packet commits
physical contact with a tracked tool. Wii Sports Resort uses a chosen disc,
wind and explicit release, including a volumetric receiver. The reused legal-lie
and par objectives do not imply identical contact or penalty semantics.
Hidden balls, later foxhunts, other players, flying, DLC and mobile input
remain explicitly separate modules rather than an exhaustive product genome.

## Normalised genome

| Type | Active genes | Scoped role |
| --- | --- | --- |
| Action | `ACT-747`, `ACT-748` | Tracked contact and ball-independent viewing relocation |
| System Behaviour | `SYS-1490`, `SYS-1586`, `SYS-1587` | Next lie, rolling response and abandoned-ball return |
| Constraint | `CON-815` | Hold-to-enable putter contact |
| Information | `INF-528` | Club/ball/cup geometry and counted result |
| Objective | `OBJ-014`, `OBJ-294` | Cup entry and par-relative delivery minimisation |
| Time | `TIM-003` | Continuing physical motion with available view commands |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `546` (`GAME-0001`–`GAME-0546`).
- Exact genome matches: none.
- Tied near matches: `GAME-0521` — Wii Sports Resort (`3 / 20 = 0.150000`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0521` — Wii Sports Resort | `SYS-1490`, `OBJ-014`, `OBJ-294` | Both inherit a legal resting lie, deliver a payload into a fixed receiver and minimise counted deliveries against par. Frisbee Golf chooses a disc, aims under wind and commits an explicit release into a scoring volume. Walkabout commits a tracked club contact into a physical cup, permits ball-independent view relocation and selected disabled rehearsal, and has no enabled stroke ceiling in this packet. | Near, `0.150000` |

### Preserved research notes

- New genes: `ACT-747`, `ACT-748`, `SYS-1586`, `SYS-1587`, `CON-815`, `INF-528`.
- Classification result: New gene.
- Evidence and reasoning: physical putter contact, independently relocated viewing and enabled rehearsal differ from a release-launched disc or a finite grid-command hand.

## Taxonomy impact

- Four definitions are reused and six are added; ten genes in total.
- Registry changes: six new Active definitions and the first Meta Quest target.
- Taxonomy-change record: [TAXONOMY_CHANGE_294](../../../research/taxonomy-changes/TAXONOMY_CHANGE_294.md).
- Candidate terms affected: none.

## Negative results

- none.

## Delta summary

## New facts

- [Observation | Corroborated | High] Grip to Putt permits a disabled rehearsal,
  while view relocation preserves the physical ball lie.

## New genes

- [Observation | Corroborated | High] Six definitions separate contact, view,
  rolling, enablement and information; the recovery boundary retains its
  explicitly Limited, Medium evidence rather than an invented penalty.

## New combinations

- [Observation | Corroborated | High] No new combination is proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_294`.

## New questions

- What are the precise Quest invalid-position volumes, return delay and count?
- How do native head-speed sampling and cup-capture thresholds vary by build?

## Next recommended game

- [Hypothesis | Limited | Medium] Original Nintendo 64 Space Station Silicon
  Valley in [Selection 043](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_043.md).
- Optimisation criterion: alternate tracked putting with robot-body possession.
- Expected information gain: different bodies turn access and energy into route choices.
- Backlog impact: advance to `GAME-0548`.

## Why this game

- [Hypothesis | Limited | Medium] First-hole tracked putting tests the boundary
  between contact commitment, viewing freedom and inherited physical lie.
