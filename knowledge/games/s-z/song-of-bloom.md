---
game_id: GAME-0698
slug: song-of-bloom
game_title: "Song of Bloom"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-072
    - ACT-781
    - ACT-918
    - ACT-919
  system:
    - SYS-1978
  constraint: []
  information:
    - INF-637
  objective:
    - OBJ-367
  time: []
---

# Game: Song of Bloom

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The prologue doubles as an interactive drawing surface. A bud shows a mark
that opens a separate landscape and leads to a credited story fragment.

## Analysis scope

- Version / ruleset: Philipp Stollenmayer's commercial English iPhone
  release, App Store product 1479162134. The developer dates the original
  iOS launch to December 18, 2019. App Store version history and capture
  dates identify the product and period. They do not authenticate the
  exact binary of either recording.
- Structured analysis target: PLAT-IOS in
  [platform coverage](../../platforms/games.json).
- Entry: finish the introductory chalk narrative and reach the tree hub
  with a single unbloomed bud. Hold the bud to inspect its cue. Use Start
  to play the chalk presentation again. Advance to the recognizable
  mountain image.
- Primary decision loop: infer where to copy the bud's red circle onto
  the current drawing. Make the mark at the summit. Once the landscape
  opens, swipe left to move its presentation through successive phases.
  Stop changing phases once the tower's selectable asterisk is visible
  and tap it to redeem the first fragment.
- Positive terminal: the first fragment appears after the tap. Return
  to the tree and verify that a flower occupies the completed branch.
  Stop with that first clearance visible, before solving another route.
- Included: replay and advance controls, requested hint, relative visual
  correspondence, finger drawing, the accepted scene transition, swipe
  progression, visible tower marks, the separate asterisk tap, the
  fragment and its credited bloom.
- Excluded: later chalk gates and other buds, recreating the full hint
  graph, subsequent volume, light, charge and motion-sensor puzzles,
  reverse swipe boundaries, exact stroke tolerances, save restoration
  after app termination, other localisations, iPad, Android and ending.
- Potential scoped module: follow the tower's next red notation to the
  paper-tearing route and test which discoveries remain available.
- Direct-play status: no personal device session, binary inspection or
  touch telemetry. A release-period iOS recording and a later witness
  attributed to iPhone 8 were sampled as short silent frame sequences.
  The narrated text was checked only where it appeared on screen.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| BLM-001 | The English-capable commercial iPhone product is App Store 1479162134. The developer dates the original iOS launch to December 18, 2019. | Confirmed | Direct | High | P1, P2 |
| BLM-002 | Holding the bud at the tree discloses a particular mountain silhouette with a red circle at its summit, giving a transfer cue for a later chalk image. | Observation | Corroborated | High | P3; W1 0:56–1:02; W2 0:40–0:45; S1 |
| BLM-003 | Replaying the chalk scene and drawing a circle over the depicted summit changes the view to the desert landscape. The witnessed transition has no separate Submit screen. | Observation | Corroborated | High | P2; W1 1:12–1:15; W2 0:54–0:57; S1, S2 |
| BLM-004 | Leftward swipes advance the landscape through successive appearances of the sun and pyramid and then raise the tower. The camera can expose a clue face and an asterisk face before completion. | Observation | Corroborated | High | W1 1:16–1:53; W2 0:57–1:33; S2 |
| BLM-005 | The tower asterisk is tapped once visible. Both captured routes show a fragment card, then a credited flower on the tree. The circle and the tower reveal precede this distinct terminal input. | Observation | Corroborated | High | W1 1:53–2:14; W2 1:33–1:48; S2, S3 |
| BLM-006 | The consistent corner control returns to the tree. Long-press hints there belong to the puzzle interface; the credited branch visibly survives the return within the session. | Observation | Corroborated | High | P3; W1 2:04–2:14; W2 1:40–1:48 |

## Basic data

- Release / origin: Kamibox / Philipp Stollenmayer, original English
  iPhone commercial product, December 2019.
- Mechanical families: FAM-012 because the solution transfers knowledge
  between the tree and the prologue. The interface participates in that
  relationship without changing its underlying rules.
- P1: [Apple App Store product and version history](https://apps.apple.com/us/app/song-of-bloom/id1479162134).
  Identifies the product, supported phone platform and English.
- P2: [Kamibox release and design notes](https://kamibox.de/songofbloom-files).
  Separates the iOS launch from Android and describes drawing on the film.
- P3: [Apple Developer interview with Stollenmayer](https://developer.apple.com/news/?id=q9fq8jkq).
  Explains the consistent corner button and the tree's long-press hints.
- W1: [App Unwrapper's release-period iOS walkthrough](https://www.youtube.com/watch?v=HXs2GPs9cgo&t=56s).
  Shows the branch cue, accepted drawing, landscape progression, fragment
  and first flower. Its video description links the commercial product.
- W2: [Reality Player 7AB's iPhone 8 walkthrough](https://www.youtube.com/watch?v=9bqnF2MspRw&t=40s).
  Independently shows the same transitions. The author identifies the
  device in the recording description. Exact installed version unverified.
- S1: [Craig Grannell's launch-period iOS play account](https://www.stuff.tv/review/app-of-the-week-song-of-bloom-review/).
  Corroborates the held bud, circle at the summit and progressive scene.
- S2: [Applizm's first-route walkthrough](https://applizm.com/song-of-bloom%E3%82%BD%E3%83%B3%E3%82%B0%E3%82%AA%E3%83%96%E3%83%96%E3%83%AB%E3%83%BC%E3%83%A0%E6%94%BB%E7%95%A5part1/).
  Corroborates the redraw, leftward swipe direction and terminal tap.
  Later play account, used only for the witnessed sequence.
- S3: [App Unwrapper's accompanying launch-period notes](https://www.appunwrapper.com/2019/12/18/song-of-bloom-walkthrough-guide/).
  Describes distinct scene access and the asterisk-to-flower rule.
- Claim IDs: BLM-001–BLM-006.

### Reproducible fixture evidence

1. Reach the single-bud tree. Hold the bud and examine the white summit
   and the red ring placed over its tip. Compare W1 near 1:00 and W2
   near 0:44. The hint shows a relationship between a mark and an image,
   rather than a numerical answer or an instruction about screen pixels.
2. Replay the chalk presentation. At the unmarked mountain, trace a
   red loop around the tip. W1 shows the visible line growing around
   1:13.0–1:13.7 and the landscape at 1:14.5. W2 shows the mark near
   0:55 and the landscape at 0:57. No separate Submit button appears.
3. Use repeated left swipes in the landscape. The pyramid and sun
   presentation changes before the pyramid sinks and the tower rises.
   W1 shows the low structure at 1:38 and the tall tower at 1:41.
   W2 shows a raised tower by 1:25. Visible movement supports the
   reported swipe control. Neither capture contains a touch overlay
   proving swipe thresholds or distance.
4. Examine the tower markings. The patterned face includes a red
   notation on the instrument-like pictures. This can inform another
   route but is separate from the reddish asterisk on a pale tile.
   W1 shows it at 1:44 and again near 1:53. W2 returns to it at 1:33.
5. Tap the asterisk. W1 shows duplicate tiles spreading briefly,
   then a light fragment card around 1:56. W2 makes the equivalent
   transition around 1:34–1:35. The tree is credited with its first
   flower around 2:08–2:14 in W1 and 1:45–1:47 in W2. Stop here.

## Mechanical decomposition

### Action Genes

- ACT-072: activate the visible Start, return or completion affordance.
  The tower asterisk invokes the authored fragment transition.
- ACT-781: pull the landscape left through its authored successive
  phases. The swipes change the illustration's stage of presentation.
- ACT-918: directly draw the indicated mark on the matching chalk
  image. The committed gesture itself opens the corresponding scene.
- ACT-919: press and hold the current bud to inspect its own cue
  from the tree rather than spending currency or clearing the puzzle.

### System Behaviour Genes

- SYS-1978: redeem the exposed asterisk into a story fragment and
  retain the matching bud as a flower on returning to the hub.
  The landscape entry alone does not settle this progress.

### Constraint Genes

No independent constraint is admitted. Placement of the mark and use of
the matching image belong to ACT-918's recognition boundary.

### Information Genes

- INF-637: a reference image with a contrasting overlay identifies
  both the target chalk scene and the location and shape of a stroke.

### Objective Genes

- OBJ-367: reach and activate the first vignette's exposed terminal
  marker and verify both its fragment and credited blossom.

### Time Genes

No separate time gene. The swipe advances a presented phase. It has
not been shown to rewind simulation history or race a timer.

### Parameters

Reference silhouette, cue colour, summit position, approximate stroke
shape, swipe direction, tower state and branch identity are parameters.

## Reproducible transitions

| Entry state | Action | Expected next state | Evidence |
| --- | --- | --- | --- |
| One unbloomed bud visible | Hold that bud | White mountain and red summit circle appear | BLM-002 |
| Matching unmarked mountain visible | Draw the summit loop | Transition into the landscape rather than a separate answer screen | BLM-003 |
| Pyramid landscape active | Swipe left through its phases | Tower rises and its marked faces become visible | BLM-004 |
| Asterisk visible on the tower | Tap the marker | Fragment card appears | BLM-005 |
| Fragment sequence finished | Return to the tree | The matching bud is a credited flower | BLM-005–BLM-006 |

## Strategic and experiential structure

The hint shows both which picture to revisit and what to do there.
Seeing the monument and revealing its optional annotation are intermediate
milestones. The next story fragment follows the distinct claim action.

## Replay and variation

The witnessed route can be attempted by replaying the prologue from
the tree. Restarting or choosing a different vignette is outside this
first-bloom fixture. The captures do not establish an exact geometrical
stroke tolerance or a device-input log.

## Adjacent systems and history

Later vignettes use different touch and hardware affordances. The
subsequent Android release and later iOS revisions are distinct research
targets. The shared opening in both witnesses does not certify the
equivalence of all editions or patches.

## Normalised genome

- Action: ACT-072, ACT-781, ACT-918, ACT-919.
- System Behaviour: SYS-1978.
- Constraint: none.
- Information: INF-637.
- Objective: OBJ-367.
- Time: none.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `697` (`GAME-0001`–`GAME-0697`).
- Exact genome matches: none.
- Tied near matches: `GAME-0060` — HOOK (`1 / 13 = 0.076923`); `GAME-0574` — Florence (`1 / 13 = 0.076923`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [HOOK (GAME-0060)](../g-l/hook.md) | ACT-072 | Both use a visible addressed trigger. HOOK retracts linked pieces and demands an interference-safe order. Song of Bloom first transfers a visual mark into a different scene and later claims an independent narrative credit. | Near, `0.076923`. |
| [Florence (GAME-0574)](../a-f/florence.md) | ACT-781 | Both advance an authored illustration through a directional touch. Florence builds mandatory reply shapes to finish a fixed chapter. Song of Bloom matches one hint to a drawn gate, views a changing landscape and deliberately claims its distinct fragment. | Near, `0.076923`. |

## Taxonomy impact

Reuse an addressed trigger and a directional move of the story
presentation. Add the held bud cue, relative overlay and direct mark
at the image. Distinguish the objective of a claimed fragment from
the system that credits a flower to its context.

## Negative results

- The bud preview shows a cue. It does not credit the branch.
- The accepted circle opens a playable vignette. It is not the terminal.
- The tower's red annotation is not the asterisk that claims the fragment.
- Neither capture establishes an exact stroke recognizer threshold or
  how progress would behave after deleting application data.

## Delta summary

Seven genes express the shortest reviewed path from a visible hint
to a mark, a changed scene and an independently claimed story fragment.

## New facts

- A source hint can reference both an image and a relative gesture.
- The player can act directly on the matching story illustration.
- An episode's entry and its completion affordance are different states.

## Principles and design implications

A clue that depicts a modification communicates action as well as
identity. A short exploration phase between gate and claim lets the
same scene host a reward and a separate clue for later work.

## Puzzle or game generation potential

Put a marked motif in a persistent menu and an unmarked equivalent in
a scene. Validate the relative mark and enter a small presentation
with one separately targetable claim affordance. Test that the card
becomes complete only after the claim.

## New genes

- ACT-918
- ACT-919
- INF-637
- OBJ-367
- SYS-1978

## New combinations

None. None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 444](../../../research/taxonomy-changes/TAXONOMY_CHANGE_444.md).

## New questions

- Does the recognized gesture tolerate a different centre or direction?
- How does the tower annotation become revisitable after the first flower?

## Next recommended game

Continue Selection 060 with GAME-0699, Dungeon Master, on Atari ST.

## Why this game

The opening makes a narrative frame operate as an input surface and
ties its distinct scene completion to a visible branch in the hub.
