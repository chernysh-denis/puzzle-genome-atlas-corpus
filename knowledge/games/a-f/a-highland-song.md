---
game_id: GAME-0718
slug: a-highland-song
game_title: "A Highland Song"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
    - ACT-934
  system:
    - SYS-2010
    - SYS-2011
  constraint:
    - CON-900
  information:
    - INF-192
    - INF-268
    - INF-650
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: A Highland Song — the first east-loch route

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Drawn landmarks, journal controls and the loch route are parameters of the observed rules.

## Analysis scope

- Version / ruleset: the English macOS Steam commercial base game,
  app 1240060, released 5 December 2023. The target is the release-window
  rules before the 8 December Look Further update. Two English
  post-release recordings were uploaded on 6 and 7 December.
  The primary footage identifies Steam. Its operating system,
  depot, executable build and input device are not independently
  authenticated; no button mapping is transferred to macOS.
- Structured analysis target: `PLAT-MACOS`, the first journey, at
  The Bald Edge on Lann Maol before the first summit survey through
  selecting and traversing the east-side loch path by the Giant's
  Tooth. Stop when ordinary movement returns on the wooded ridge.
- Primary decision loop: read an annotated paper sketch against the
  surveyable view from the summit. Select a plausible spot near the
  tooth-shaped stone, then descend and walk to the shore. Inspect the
  actual location to confirm the sketch. Accept the separate local
  traversal choice to cross to the next ridge.
- Included: contextual summit and route interactions, panning and
  zooming the survey, choosing a carried sketch and a tentative spot,
  retaining the mark as local guidance, direct traversal, location
  checking, both verification signals and a separately accepted
  passage. The first terminal has an afternoon period indicator.
- Excluded: the preceding rhythm run, numerical stamina and damage
  rates, other optional finds, peak blessings, shelters, weather
  survival, later Look Further and Harmony Landmarks features,
  full campaign and ending, deadline optimisation and new game plus.
  The second sketch is evidence about the verification boundary,
  not a second selected stage.
- Direct-play status: no personal macOS session, downloaded game,
  inspected depot, controller trace or input log. The developer's
  Steam listing and press kit establish the macOS commercial
  release. English commercial release-window video frames and the
  developer's explanation document the navigation rules. The frames
  were inspected in the background without audio. Exact macOS
  input timing and portability of later changes were not tested.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| AHS-001 | Inkle's English commercial base game shipped on Steam for Mac on 5 December 2023. Later Look Further and Harmony Landmarks changes are out of scope. | Observation | Corroborated | High | P1, P2, P4 |
| AHS-002 | The first survey is entered at The Bald Edge. The nearby tower sketch and the east-loch sketch can be cycled; ordinary directional walking resumes after leaving the survey. | Observation | Corroborated | High | P2; W1 04:19–05:40; W2 06:45–07:26 |
| AHS-003 | From the summit, the player can pan and zoom the view while the selected paper sketch remains visible as a reference. The east-loch sketch depicts the Giant's Tooth beside the indicated shore. | Observation | Corroborated | High | P2; W1 05:09–05:34; W2 06:54–07:11 |
| AHS-004 | A provisional question-mark pin can be placed, removed or moved. The chosen east-loch site is retained as guidance while walking. A plausible pin and a verbal acknowledgement at the summit do not confirm the sketch. | Observation | Corroborated | High | P3; W1 05:32–05:35 and 06:34–06:38; W2 07:13–07:23 |
| AHS-005 | The matching site must be examined on foot. A rough summit estimate can be corrected by searching on the ground. Exact marking from afar is not a condition for useful guidance or for the subsequent local confirmation. | Observation | Corroborated | High | P3; W1 06:36–06:49; W2 07:24–07:33 |
| AHS-006 | At the Giant's Tooth, inspecting the place where the signpost stood leads to an on-site comparison and a green check on the carried sketch. The tower sketch can also be confirmed while staying on the current ridge. | Observation | Corroborated | High | P3; W1 06:37–06:51; W2 07:24–07:34 |
| AHS-007 | The confirmed loch site then offers a separate local choice to go or stay. Taking the path brings the avatar to a new wooded ridge, with navigation restored and the indicator showing early afternoon after midday at the shore. Exact travel duration and map-free availability of this route were not measured. | Observation | Corroborated | High | P2; W1 06:52–07:18; W2 stays on ridge 07:33–07:52 |

## Basic data

- Release / origin: inkle Ltd, Steam app 1240060, commercial base
  game released 5 December 2023. The macOS target is not the Switch
  port, soundtrack package, press demo or a pre-release build.
- Platform or physical form: English Steam download for macOS.
  The public store and launch press kit establish this edition.
  The footage supports cross-platform base rules and cannot
  identify the exact macOS binary.
- Mechanical family: `FAM-012`, knowledge and evidence progression.
  The sketch provides interpretable evidence for a located passage;
  the player does not assemble new physical geometry.
- Primary sources accessed 2026-11-25:
  - **P1:** [Steam commercial listing and macOS requirements](https://store.steampowered.com/app/1240060/A_Highland_Song/).
    Developer, release date, declared English support and Mac availability.
  - **P2:** [Inkle's launch press kit](https://www.inklestudios.com/press/a-highland-song/)
    and [the developer overview](https://www.inklestudios.com/a-highland-song/).
    Release on Mac, summit orientation, sketches, hidden routes,
    and the later Harmony update boundary.
  - **P3:** [Inkle's answers on marking and confirming maps](https://steamcommunity.com/app/1240060/discussions/0/4029096483732473517/).
    From 11–12 December 2023, the developer explains approximate
    marking and journal confirmation at the actual site. The
    earlier clips test the shared rule. No later feedback copy is
    assumed to have been present at release.
  - **P4:** [Inkle's December 8 update notice and developer response](https://steamcommunity.com/app/1240060/discussions/0/4029096129892178138/)
    identify the separately introduced Look Further feature.
- Independent evidence accessed 2026-11-25:
  - **W1:** [rinimt, Steam full game recording posted December 6](https://www.youtube.com/watch?v=KU01yaygazU&t=259s).
    The opening shows a first journey. At 04:19–05:40 the summit
    survey and the east-loch assignment are visible. At 06:34–06:51
    the approach, signpost-site examination and green check appear.
    At 06:52–07:18 the route prompt and wooded-ridge handoff appear.
  - **W2:** [Estinto, independent commercial walkthrough posted December 7](https://www.youtube.com/watch?v=BaHh1qfAoW0&t=405s).
    The survey visits the same loch outcrop and shows the radio
    tower sketch being marked and verified on foot, followed
    by continued exploration of the current ridge. Exact operating
    system and build are not shown. Compare 06:45–07:23 and
    07:24–07:52.
  - **S1:** [Independent original route and map confirmation guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3146853629)
    supports retaining and following a marked spot, a separate
    site confirmation, and the existence of routes that need no
    map. It describes later play and does not place every rule at
    this exact location. Its advice about first marking is read
    with the developer's explicit rough-mark allowance in P3.
- Claim IDs: `AHS-001`–`AHS-007`. To retest, use the English commercial
  macOS edition and a first-journey save before the first summit
  survey. Record the build, selected sketch, mark position, avatar
  position and available verbs at the matching shore. The video
  sequences support event order without supplying executable traces.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: directly walk and descend from the summit to
  the candidate area. Selecting a point does not guide the avatar
  there automatically (`AHS-002`, `AHS-005`).
- Reuse `ACT-341`: invoke the locally offered summit survey, examine
  the old signpost position, and separately choose the discovered
  path's offered interaction (`AHS-002`, `AHS-006`, `AHS-007`).
- New `ACT-934`: select one carried route sketch during the summit
  survey and place or edit its provisional mark in the viewed
  terrain. The same sketch can remain unsettled after this
  action (`AHS-003`, `AHS-004`).

### System Behaviour Genes

- New `SYS-2010`: preserve the provisional assignment when leaving
  the survey and expose the marker as local terrain guidance.
  Reaching the indicated area and settling the sketch are
  distinct transitions (`AHS-004`, `AHS-005`).
- New `SYS-2011`: examining the matching place confirms the sketch
  and exposes its linked route choice. The player chooses
  separately whether to traverse (`AHS-006`, `AHS-007`).

### Constraint Genes

- New `CON-900`: the confirmation requires the clue's authored
  physical location at local examination. The mapped candidate
  is evidence for the approach but does not satisfy the
  location check by itself (`AHS-005`, `AHS-006`).

### Information Genes

- Reuse `INF-192`: the ordinary following view shows immediate
  surfaces, ledges and shore approach while moving (`AHS-002`,
  `AHS-005`).
- Reuse `INF-268`: opening guidance introduces surveying and the
  descent; the game supplies context-specific instructions up
  to the located interaction (`AHS-002`, `AHS-005`).
- New `INF-650`: the selected sketch and pannable summit view
  show comparable geographic cues. A question mark distinguishes
  the proposal from the green check acquired on site (`AHS-003`,
  `AHS-004`, `AHS-006`).

### Objective Genes

- Reuse `OBJ-026`: make the selected crossing available by
  interpreting and confirming the clue, then take it to restore
  controllable movement on the next ridge. A green check alone
  stops before this selected outcome (`AHS-006`, `AHS-007`).

### Time Genes

- Reuse `TIM-003`: ordinary traversal and the passage occur in a
  progressing day. The witnessed route moves between visible
  periods, without measuring an exact tariff or deadline
  (`AHS-005`, `AHS-007`).

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| First arrival at The Bald Edge | Look out and cycle to the east-loch sketch | The sketch remains beside the moving panorama and shows the Giant's Tooth | AHS-002, AHS-003 |
| Matching outcrop visible from the summit | Choose the shore spot next to it | A question-mark marker appears; it can be removed or moved | AHS-004 |
| Survey closed with the east-loch mark | Descend and walk to the shore | Ordinary movement remains necessary; local guidance and the sketch are visible on approach | AHS-004, AHS-005 |
| At the old signpost spot next to the Giant's Tooth | Read or examine the matching clue | The carried sketch gains a green check | AHS-005, AHS-006 |
| Local path choice is offered after confirmation | Choose Go | A separate scenic transfer ends on the wooded ridge with movement enabled and early afternoon shown | AHS-007 |
| Independent recording beside the radio tower | Confirm the other sketch, then continue on the current ridge | Confirmation appears without automatically taking a linked way | AHS-006 |

## Strategic and experiential structure

The player has the rough shape of the destination and a wide
view, but the travelled landscape still has to be read on foot.
Using the silhouette to place a provisional mark cuts down the
search without settling the destination by interface alone. The
discovery then changes which local action is offered. Choosing
the discovered crossing trades an early local endpoint for the
next ridge while the journey carries on.

## Replay and variation

The first survey can test more than one sketch and move a
candidate marker before descent. W2 confirms the tower sketch
and stays in the current area, whereas W1 uses the east-loch
passage. These are two filmed choices, not an exhaustive route
tree or a controlled test of the same exact loaded save.

## Adjacent systems and history

The journey contains climate, weather, climbs, timed music,
optional shelters and carryover between runs. The selected
window starts at the first summit approach after the rhythm run
and ends at the first controllable successor on the loch route.
Later changes to preview distance or landmark tooling are
separate versions.

## Normalised genome

- Action: ACT-008, ACT-341, ACT-934.
- System Behaviour: SYS-2010, SYS-2011.
- Constraint: CON-900.
- Information: INF-192, INF-268, INF-650.
- Objective: OBJ-026.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `717` (`GAME-0001`–`GAME-0717`).
- Exact genome matches: none.
- Tied near matches: `GAME-0615` — Skate Story (`4 / 16 = 0.250000`); `GAME-0692` — Klonoa 2: Lunatea's Veil (`4 / 16 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Skate Story (GAME-0615)](../s-z/skate-story.md) | ACT-008, ACT-341, OBJ-026, TIM-003 | Both use direct real-time traversal and local interactions to reach a newly admitted destination. Skate Story needs spatially qualified ollies at crests before its portal lights. A Highland Song checks an interpreted route sketch on foot and offers a separate crossing. | Near, `0.250000`. |
| [Klonoa 2: Lunatea's Veil (GAME-0692)](../g-l/klonoa-2-lunateas-veil.md) | ACT-008, INF-192, OBJ-026, TIM-003 | Both use local side-view navigation and a reachable continuation. Klonoa spends a captured enemy mid-jump to reach an elevated ledge. A Highland Song verifies geographic evidence before the separate route offer. | Near, `0.250000`. |

## Taxonomy impact

Keep physical navigation, contextual interaction and the reached
route objective. Separate the player-authored preliminary mark,
persistence of its guidance, location legality, the verified
offer and the visible cue states.

## Negative results

- Neither recording transports the avatar when a place is marked
  from the summit.
- A question-mark pin and spoken acknowledgement are preliminary
  states. The green check follows inspection at the location.
- Confirming a sketch and taking a path are separately observable.
  No general ban on map-free routes follows from this example.
- Exact marker tolerance, travel charge and input timing remain
  unmeasured.

## Delta summary

The destination becomes useful in three distinct states.
The player proposes a place from a sketch, verifies it in the
world and accepts the newly offered path.

## New facts

- The live summit view and the paper clue are visible together.
- The same tentative assignment guides the on-foot approach.
- At the Giant's Tooth the green check appears before the distinct
  passage choice.

## Principles and design implications

Show a plausible interpretation without confirming it. Give
players a separate on-site check and keep a discovered route
available for a deliberate choice.

## Puzzle or game generation potential

Give a high overlook a view of several shoreline silhouettes
and provide sketches with independently known landmarks. Have
the player propose one match, take a walk and verify the
location before using the opened connection.

## New genes

- ACT-934
- CON-900
- INF-650
- SYS-2010
- SYS-2011

## New combinations

None.

## Taxonomy changes

[Taxonomy Change 464](../../../research/taxonomy-changes/TAXONOMY_CHANGE_464.md).

## Next recommended game

Continue Selection 062 with Alisia Dragoon on the original North
American Sega Genesis cartridge. Document the opening stage's
lightning targeting, recharge and one visible companion choice.

## Why this game

It makes a player interpretation, a geography check and committed
traversal observable as different states along one short route.

## Review status

Reviewed 2026-11-25 for this original commercial early route.
Exact macOS executable and line-by-line input trace remain unverified.
