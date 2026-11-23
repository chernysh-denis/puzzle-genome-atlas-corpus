---
game_id: GAME-0574
slug: florence
game_title: Florence
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-780
    - ACT-781
  system:
    - SYS-1685
  constraint:
    - CON-837
  information:
    - INF-547
  objective:
    - OBJ-316
  time:
    - TIM-002
---

# Game: Florence

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Fitting a speech balloon advances an authored response. The same gesture
becomes less laborious across the date as the supplied replies become simpler.

## Analysis scope

- Version / ruleset: launch-period English US iPhone App Store release from
  February 2018, application ID 1297430468. Use the native single-player
  touch rules of Act 2, Chapter 5, First Dates. No exact installed build
  was authenticated.
- Structured analysis target: PLAT-IOS in knowledge/platforms/games.json.
- Entry: finish Crash in an ordinary first play, after Florence has met
  Krish. Open First Dates before the first conversation puzzle, with its
  first authored reply unassembled.
- Primary decision loop: read the scene and its blank reply shape, choose
  one loose fragment and drag it into a compatible place. Complete each
  visual reply and proceed through the intervening panels in order.
  Later setups use fewer, more directly placeable parts. Pace depends on
  the player's completion of these interactions.
- Positive exit: complete the eight reply puzzles documented in the
  chapter study, including the final single-fragment placement, see the
  authored first-kiss vignette and reach the transition to Chapter 6,
  Dreams. The first active task in Dreams is outside the scope.
- Negative exit: no documented gameplay loss or timed expiration in
  First Dates. An incomplete or incompatible placement leaves the
  requirement pending. Quitting the application is outside chapter
  settlement. Save and resume granularity were not tested.
- Included: touch placement, visual boundary and response feedback,
  fixed fragment fit, reply completion, authored reduction in placement
  work, illustrated panel transitions, self-paced interaction and the
  complete chapter's handoff.
- Excluded: numeric match tasks, focus sliders from Crash, dialogue outcomes or
  dialogue-text choice, competitive timing and angular pieces from later
  arguments, Dreams interactions, subsequent relationship branches or
  endings, achievements, Android and desktop/console versions.
- Potential scoped modules: the competing reply pace in Groceries or
  the separate idle condition in Let Go. They use other rules.
- Direct-play status: not conducted. Apple metadata, launch interviews
  and contemporary touch play accounts were read with later published
  screenshots and chapter analysis. No iPhone installation, emulation or
  video/audio playback was used. Exact placement tolerances, all eight
  starting arrangements, native panel transition thresholds and exact
  per-build parity are unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| FLO-001 | Mountains made the February 2018 iPhone release published by Annapurna Interactive. The US App Store product is 1297430468, and Apple lookup marks 13 February UTC. Several contemporary launch sources name 14 February. | Observation | Corroborated | High | P1, P2, R1, R2, R3 |
| FLO-002 | Drag a loose part to fit Florence’s visible blank speech balloon. The whole reply depends on the assembled image and does not ask the player to select or spell words. Krish’s authored bubbles appear independently. | Observation | Corroborated | High | R1, R2, D1, D2 |
| FLO-003 | The scene presents eight reply puzzles in the chapter study. It starts at eight fragments and uses fewer, larger parts, ending with one. Two late two-piece layouts differ in the order of their starting parts. | Observation | Corroborated | Medium | D1 figs. 2–3, D2 fig. 1, R2 |
| FLO-004 | Each assembled balloon makes the scripted next response possible. The final single-piece reply leads to the first-kiss scene. No first-date timeout, game-over branch or alternative relationship result is documented. | Observation | Corroborated | High | R1, R2, D1, D2 |
| FLO-005 | The chapter uses forward movement through illustrated date panels and hands off to Dreams. The upward pull is described in a later PC walkthrough and is consistent with the mobile comic presentation. Exact original iPhone gesture thresholds remain unverified. | Observation | Limited | Medium | D1, D2, R4 |
| FLO-006 | The part-count and layout progression offers a reproducible representation of the conversation easing. A chapter with geometrically simpler input cannot by itself demonstrate that every player interprets the scene alike. | Hypothesis | Limited | Medium | R1, R2, D1, D2 |

FLO-006 could be weakened if players notice the smaller placement burden
without connecting it to growing familiarity when compared with unchanged
puzzles under the same visual context. It is not an additional gene.

## Basic data

- Mountains / Annapurna Interactive. Native English iPhone release.
- Families FAM-003 state transformation and FAM-017 ordered dependency
  sequencing.
- P1: [US App Store product](https://apps.apple.com/us/app/florence/id1297430468)
  and [Apple lookup for app 1297430468](https://itunes.apple.com/lookup?id=1297430468&country=us).
  Checked 2026-11-20. The lookup returned releaseDate
  `2018-02-13T07:58:07Z` and current version 1.0.5. Store version-history
  dates, public announcement dates and present compatibility are separate
  from a verified original executable. This record targets February 2018.
- P2: [Annapurna’s product page](https://annapurnainteractive.com/games/florence).
  Establishes the developer and vignette structure. Its February 4 date
  disagrees with Apple's date and the contemporary reports; it is not
  used as the iPhone availability date.
- R1: [Dean Takahashi’s preview and Ken Wong interview](https://gamesbeat.com/florence-uses-clever-interactions-to-create-a-relatable-mobile-game-about-romance/),
  12 February 2018. Describes the intended 14 February iOS release and the
  gradual reduction in the number of reply parts.
- R2: [Julie Muncy’s iOS-era touch account](https://www.wired.com/story/florence-touch-mobile-game/),
  2 March 2018. Supports direct assembly, changing input effort and the
  one-piece finale. Its informal initial count is lower than the worked
  opening in D1 and D2. Those independent diagrams support eight pieces.
- R3: [AppUnwrapper’s launch-period iPhone review](https://www.appunwrapper.com/2018/02/13/florence-walkthrough-and-review/),
  13 February 2018. The publication date and native touch scope establish
  release-period context. Embedded media was not opened.
- R4: [The Walkthrough King, First Dates and Dreams](https://www.walkthroughking.com/text/florence.aspx),
  2021 PC guide. It names the upward movement between date scenes and their
  chapter order. No PC-specific timing, control or trophy rule is imported.
- D1: [Batu Aytemiz, Nick Junius and Nathan Altice, DiGRA 2019](https://dl.digra.org/index.php/dl/article/download/1083/1083/1080),
  Florence section, figs. 2–3. Worked analysis of eight puzzles, beginning
  and ending counts, the two different two-part layouts and the closing
  scene. Its phrase about the release period conflicts with P1 and R1–R3.
- D2: [Mela Kocher, Florence chapter, pp. 304–305](https://www.transcript-publishing.com/media/pdf/3e/50/0f/oa97838394534528KtbFGbXKClRq.pdf),
  fig. 1 and puzzle section. Independent scene description and stills
  corroborate the first eight-part reply, the turn structure and final
  reply immediately before the kiss. The later Groceries race is excluded.

## Mechanical decomposition

### Action Genes

- ACT-780 covers touching and moving an individual loose fragment into
  the current outline. Its fixed orientation is part of the operation.
- ACT-781 covers pulling an eligible panel to present the scripted next
  vignette. The same touch device acts on a different object.
- Claim IDs: FLO-002, FLO-003, FLO-005.

### System Behaviour Genes

- SYS-1685 resolves a completed balloon as Florence's line and makes
  the next authored beat available. Each setup is tied to its chapter
  position. The late two-fragment arrangement and final one-piece state
  are different authored parameters of that operation.
- Claim IDs: FLO-002–FLO-004.

### Constraint Genes

- CON-837 requires individual geometric placement within the current
  target and complete coverage. Being partly assembled does not satisfy
  the reply. Exact snapping radii and invalid-contact persistence are
  unmeasured.
- Claim IDs: FLO-002, FLO-003.

### Information Genes

- INF-547 covers visual speech from the other participant, the current
  target outline, its loose reply fragments and the finished transition.
  There is no semantic choice among written lines in this chapter.
- Claim IDs: FLO-002–FLO-004.

### Objective Genes

- OBJ-316 covers the complete sequence of puzzles and linking scenes to
  the final handoff into Dreams. One intermediate reply progresses the
  chapter without settling it.
- Claim IDs: FLO-003–FLO-005.

### Time Genes

- TIM-002 covers waiting between actions while the current geometric
  problem remains available. Scripted animations can follow completion
  without turning the placement into a live timed contest.
- Claim IDs: FLO-002, FLO-004, FLO-005.

## Reproducible transitions

| State / precondition | Action or event | Observable transition | Boundary | Claims |
| --- | --- | --- | --- | --- |
| First Dates opens after Crash | Advance to the first conversation | Blank target and first eight loose reply fragments | Pieces are provided for this reply, not fetched from earlier chapters | FLO-002, FLO-003, FLO-005 |
| A target and loose fragment are visible | Drag a fragment into a compatible gap | One part of the required outline is satisfied | No wording decision is made | FLO-002, FLO-003 |
| One or more parts remain outside the right locations | Leave the current target incomplete or attempt an incompatible placement | The reply remains pending | No claim about exact snap distance or unsuccessful drop animation | FLO-002–FLO-004 |
| All parts in the current reply fit | Finish the balloon | Florence's visual reply resolves and the next authored beat becomes available | Local completion is not chapter completion | FLO-002, FLO-004 |
| Two late puzzles each have two parts | Inspect their initially presented arrangement | Matching requires crossing positions in the earlier layout and direct alignment in the later one | Count alone does not give the full placement burden | FLO-003 |
| The last puzzle provides one fragment | Drag it into the outline | The final response resolves into the authored closing scene | There is no alternative reply or score target | FLO-003, FLO-004 |
| The closing scene settles | Continue to the next chapter boundary | Dreams is next | Stop before its first active gesture | FLO-005 |

## Strategic and experiential structure

- Reading the external contours and matching edges helps assemble the reply.
  The task is always bounded to the shown pieces and current orientation.
- Early and late puzzles use the same touch operation, but later puzzles
  require fewer commitments or less crossing. The player's own placement
  effort changes while the kind of action stays familiar.
- The first-date response cannot be changed into a different story route by
  leaving a piece out. Pausing delays the current interaction.
- Claim IDs: FLO-002–FLO-006.

## Replay and variation

- Repeat the chapter to compare authored beat setups. Individual accepted
  placement order can vary within a reply. The date and closing scene are
  fixed. Exact per-build piece tolerances and persistence are unverified.
- Claim IDs: FLO-002–FLO-005.

## Adjacent systems and history

- Later arguments alter contours and overlap the sides' timing. They are
  separate scoped modules. No argument-phase timeout is inherited here.
- Other releases may preserve the scene while mapping the same drag to
  pointer or controller input. This unit models native phone touch.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | ACT-780, ACT-781 | Drag a fragment; pull a story panel |
| System Behaviour | SYS-1685 | Complete reply and advance one authored beat |
| Constraint | CON-837 | Fit the present outline before release |
| Information | INF-547 | Outlined target, parts and speaker feedback |
| Objective | OBJ-316 | Complete First Dates through the Dreams boundary |
| Time | TIM-002 | Untimed sequential placements |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `573` (`GAME-0001`–`GAME-0573`).
- Exact genome matches: none.
- Tied near matches: `GAME-0064` — SET (`1 / 11 = 0.090909`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0064` — SET | TIM-002 records an unforced interval to inspect the shown pieces and act. | SET checks a selected triple across card attributes. Florence fits the current visible contour and advances a fixed scripted reply. Completion never awards a SET or refills a shared tableau. | Tied near: 1 / 11 = 0.090909 |

### Preserved research notes

- New genes: ACT-780, ACT-781, SYS-1685, CON-837, INF-547 and OBJ-316.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_320](../../../research/taxonomy-changes/TAXONOMY_CHANGE_320.md)
  explains why geometry, local completion, presentation and chapter
  progression remain separate from contextual dialogue selection.

## Negative results

- The App Store version-history date, lookup date, publisher page and
  advertised Valentine's Day release are different observations, not proof
  of one exact verified build or simultaneous regional availability.
- A smaller part count is an authored change across story beats, not a
  performance-based assistance system. Later arguments cannot be used as
  evidence for a first-date deadline.

## Delta summary

## New facts

- [Observation | Corroborated | High] FLO-002–FLO-004 separate completing a
  scripted speech turn by shape from branching dialogue and timed response.

## New genes

- [Observation | Corroborated | Medium] Six additions in taxonomy change 320.

## New combinations

- [Observation | Corroborated | High] No new combination proposed.
  Existing supported subsets are owned by the comparison section.

## Taxonomy changes

- [Observation | Corroborated | Medium] Earlier definitions and signatures
  stay unchanged.

## New questions

- An authenticated launch build could resolve invalid release handling,
  touch tolerance and the animation or gesture boundary at chapter end.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0575, Metal Gear Acid on North
  American PSP.
- Optimisation criterion: alternate platform and compare self-paced single
  actions with multiple costly card commands in an infiltration turn.
- Backlog impact: eighth Selection 046 unit.

## Why this game

- [Hypothesis | Limited | Medium] The full first-date chapter isolates
  a story transition produced by changing the work required for one
  repeated gesture. Verify by comparing the opening and closing setups
  and the effect of changing their order.
