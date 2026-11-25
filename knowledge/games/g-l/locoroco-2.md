---
game_id: GAME-0717
slug: locoroco-2
game_title: "LocoRoco 2"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-519
    - ACT-637
    - ACT-638
    - ACT-933
  system:
    - SYS-036
    - SYS-037
    - SYS-1259
    - SYS-1260
    - SYS-1261
    - SYS-1262
    - SYS-2009
  constraint:
    - CON-746
    - CON-747
  information:
    - INF-192
    - INF-268
    - INF-457
    - INF-649
  objective:
    - OBJ-181
    - OBJ-271
  time:
    - TIM-003
---

# Game: LocoRoco 2 — Franzea 1 on the original PSP

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Button labels, population numbers, note sprites and flower names are evidence-bearing parameters.

## Analysis scope

- Version / ruleset: first ordinary Franzea 1 visit in the original English PlayStation Portable base game after the prologue and initial MuiMui House visit. The intended reproduction edition is the North American retail UMD UCUS-98731, released on 10 February 2009. Its identity comes from Sony and disc catalogues. The primary route witness labels its footage PAL and shows the original PSP presentation in English. Its exact disc and hardware or emulator are unknown. Apply only rules supported by that witness and the original Sony evidence. No PS4 remaster features are transferred.
- Structured analysis target: initial Franzea 1 traversal from map confirmation through accepted Stage Clear and map return, on `PLAT-PLAYSTATION-PORTABLE`. Use a new save brought through the prologue and the house introduction without replay upgrades. Stop before Perculoka 1.
- Primary decision loop: tilt the ground and bump it to roll or bounce the group. Eat berries and choose when the group should split to fit a crevice or rejoin for more direct control. Look for buds, Pickories and local participants. At the marked chorus, gather enough individuals and stay still, then time Circle presses to receive additional notes. Reach the local exit and accept the stage result.
- Included: world tilt and bump, gravity and surface contact, living population growth, local splitting and reunion, physical clearance, bud reveal, contact collection, a marked minimum population, inactivity-triggered singing, single-button cue responses, visible note rewards, local instructions and settlement. The art represents the narrow descent, not exact coordinates.
- Excluded: exact judge windows, scoring or bonus tables, maximum score, complete secret route, audio cue identification, physical sampling, later learned super jump, swimming and swinging instruction, later boss fights, stamp sheets, house procurement, Time Attack, online and ad hoc variants, and the prologue as a separate stage. Black-cloud effects and local script activation are visible in the route; the scope does not assert a full cloud or enemy interaction model.
- Direct-play status: no personal PSP or emulator session, original UMD execution, save or live input trace. Documented retail identity plus frame inspection of an English PAL-labelled PSP route, corroborated by the original manual, a Sony producer's overview and a contemporary illustrated Franzea 1 route. Only short video-only windows and storyboard stills were inspected in the background without audio. No North American disc-specific variability was tested.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| LR2-001 | The inherited shoulder-button mappings change world inclination or bump the ground. Direct avatar steering is not the navigation method. | Observation | Corroborated | High | P1 Controls and Moving; P2; W1 Franzea entrance |
| LR2-002 | Eating a berry increases the living count. A hidden bud first grows a ripe berry within local reach. Pickories and discovered optional items credit progress separately. | Observation | Corroborated | High | P1 Eating; W1 09:51–10:15; S1 |
| LR2-003 | Tap Circle to divide, hold to reunite near the group. At the narrow curved descent the separated bodies pass while keeping the living count. | Observation | Corroborated | High | P1 Splitting and Joining; W1 10:07–10:15, 14:38–14:53; S1 shows another split route |
| LR2-004 | Local terrain, growth counts and contextual MuiMui guidance are visible as the camera follows the group. | Observation | Corroborated | High | P1 The Game Screen; W1 08:40–09:00, 12:11–12:31, 14:32 |
| LR2-005 | A marker at a Franzea 1 chorus asks for five individuals. The group is instructed to remain still before the note opportunities appear; twelve are present in the recorded run. This threshold applies to the local event. | Observation | Corroborated | High | W1 12:11–12:23; S1; P1 Singing |
| LR2-006 | A timed Circle prompt appears with visible moving note symbols. Well-timed replies generate more notes. Franzea 1 has more than one chorus scene, and the later group of flowers also presents the moving symbols. | Observation | Corroborated | High | P2 note minigame; W1 12:23–12:47 and 16:59–17:17; S1 |
| LR2-007 | At the stage's final basin a local response precedes Stage Clear. The settled run shows 14 of 20 living individuals, 238 Pickories, 7:47.20 and 13,512 score, followed by discovered MuiMui and a save prompt before map return. | Observation | Corroborated | High | P1 Completing a Stage; W1 17:50–18:30 |
| LR2-008 | An ordinary stage can finish with at least one living individual at the goal; all twenty earn an additional award. The visual route confirms a clear below twenty, but does not test the minimum of one or identify the full-count award. | Observation | Corroborated | High | P1 Completing a Stage and Hints and Tips; W1 18:02–18:08 |

## Basic data

- Release / origin: Japan Studio and Sony Computer Entertainment, original PSP title. The North American commercial PSP release was on 10 February 2009. The earlier PAL route is evidence about common PSP rules.
- Platform or physical form: original PlayStation Portable base game, North American retail UMD UCUS-98731 for reproduction. The available footage is not a verified dump of this disc, and the software version of the recording is unknown.
- Mechanical family: `FAM-007`, physics and object manipulation. The embedded chorus does not classify the whole fixture as a competitive rhythm chart or timed score attack.
- Primary sources accessed 2026-11-25:
  - **P1:** [Original Sony PSP instruction booklet, English opening section](https://manuals.plus/m/e267b99ad881514f51bcb8afc0d491e26f7d91ab31bfaa6949283025c2528348.pdf). Controls, Eating, Splitting and Joining, Singing, Musical Notes and Completing a Stage. PAL multilingual booklet, with noisy OCR; confirm ambiguous Circle glyph against the in-game prompt and route evidence.
  - **P2:** [Sony producer Tsubasa Inaba on the original PSP sequel](https://blog.playstation.com/2009/01/26/locoroco-2-turn-that-frown-upside-down/). Inherited tilt/roll/jump and timed music encounter for notes. The later unlocked abilities described there are not placed in this fixture.
  - **P3:** [Sony North American launch announcement](https://blog.playstation.com/2009/02/10/locoroco-2-dont-worry-get-loco-sweepstakes/). Dated retail availability for the original game, independent of the footage's region.
- Secondary evidence accessed 2026-11-25:
  - **S1:** [Mitch's contemporary illustrated Franzea 1 walkthrough](https://mitcheriouseffect.blogspot.com/2009/01/loco-roco-2-franzea-1-walkthrough-with.html). Independently locates optional buds and paths, the five-participant chorus and Circle reply. Its complete-item and milestone tables are outside the bounded checks.
  - **S2:** [SerialStation record of the UCUS-98731 UMD](https://www.serialstation.com/discs/b0946fb6-f6f1-4f5b-bf09-461d9c2c3f32), cross-checked against [GameFAQs original PSP release data](https://gamefaqs.gamespot.com/psp/950767-locoroco-2/data). Catalogued retail identity only, no source dump executed.
  - **W1:** [LongplayArchive, recorded by nikodem123asdf, English PSP run labelled PAL](https://www.youtube.com/watch?v=WmperQosrPg&t=518s). Map confirmation near 08:38; separated descent near 10:09; threshold and chorus 12:11–12:47; nearby regrouping near 14:50; flower chorus 16:59–17:17; result 17:50–18:30. Silent stills and short frame sets show scene order, not the player's unseen inputs or precise tolerances.
- Claim IDs: `LR2-001`–`LR2-008`. For a retest use the stated UMD and fresh progression, capture explicit shoulder- and Circle-button trace, record participant counts and compare deliberately early and timed Circle replies in repeated visits. The documentary run does not establish that counterfactual.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-519`: tilt the playfield using the shoulder buttons, leaving the soft bodies to respond to the new inclination (`LR2-001`).
- Reuse `ACT-637`: issue a separate ground bump with both shoulders to launch the group (`LR2-001`).
- Reuse `ACT-638`: tap Circle for small separate individuals and hold it to gather nearby individuals (`LR2-003`).
- New `ACT-933`: during a local chorus, time individual presses of the same Circle button to successive signals. The current interaction changes how the button is used (`LR2-005`, `LR2-006`).

### System Behaviour Genes

- Reuse `SYS-036`: integrate rolling, bending, collisions and bouncing as the angle and terrain change (`LR2-001`, `LR2-003`).
- Reuse `SYS-037`: register eligible pickups on contact in ordinary traversal, separately from the optional note output of the chorus (`LR2-002`, `LR2-006`).
- Reuse `SYS-1259`: consuming a red berry adds an individual to the living group rather than just adding score (`LR2-002`).
- Reuse `SYS-1260`: splitting and nearby regrouping change the physical bodies that represent the same group. Neither command credits growth (`LR2-003`).
- Reuse `SYS-1261`: approaching a hidden bud can reveal the berry before separate contact acquires it (`LR2-002`).
- Reuse `SYS-1262`: the qualified group waits to trigger the authored chorus scene. This trigger and the subsequent timed replies are separate transitions (`LR2-005`, `LR2-006`).
- New `SYS-2009`: successful timing replies in the active chorus release additional note rewards rather than merely updating an accuracy grade (`LR2-006`).

### Constraint Genes

- Reuse `CON-746`: the current bodies must fit the curved geometric bottleneck. Splitting changes body form while terrain remains the same (`LR2-003`).
- Reuse `CON-747`: a local singing scene is gated by a stated minimum participant count. The marked five is a local requirement independent of the ordinary ending rule (`LR2-005`, `LR2-008`).

### Information Genes

- Reuse `INF-192`: the following view shows local supports, recesses, landmarks and route approaches (`LR2-004`).
- Reuse `INF-268`: MuiMui instructions contextualise waiting, timing Circle and investigating the cavity (`LR2-004`–`LR2-006`).
- Reuse `INF-457`: the active living count and optional collection totals inform play; the terminal result exposes population, collection, time and score (`LR2-004`, `LR2-007`).
- New `INF-649`: moving note outlines and differentiated cues show reply opportunities in the local chorus view (`LR2-006`).

### Objective Genes

- Reuse `OBJ-181`: clear Franzea 1 below the full count, accept credited progress and return to the selectable map (`LR2-007`, `LR2-008`).
- Reuse `OBJ-271`: optional exploration and growth can raise the finished living group towards twenty (`LR2-002`, `LR2-008`).

### Time Genes

- Reuse `TIM-003`: physical motion, inactivity triggers and note opportunities progress while the game is unpaused. The result's elapsed time does not establish a required stage countdown (`LR2-001`, `LR2-005`–`LR2-007`).

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
|---|---|---|---|
| Group near a slope | Hold a shoulder button, then test the chord for a bump | The field tilts with one input and supplies a launch impulse with the chord | LR2-001 |
| Hidden bud near the path | Roll into its activation region and then contact the ripe berry | A reveal precedes a one-individual increase | LR2-002 |
| Six-individual body near the curved descent | Tap Circle before letting the individuals fall | Separate small bodies traverse the throat; the displayed count remains six | LR2-003 |
| Small bodies share the later cavity | Hold Circle | Nearby bodies merge into the larger rolling body | LR2-003 |
| Marked chorus with twelve individuals and a threshold of five | Leave the group still | The local chorus starts; moving prompts appear | LR2-005 |
| Active chorus with moving note outlines | Use a separate Circle press at the taught timing | Additional visual note rewards appear; the exact tolerance is not measured | LR2-006 |
| Group reaches the three flowers later in the route | Stop at the local chorus scene | A second visible note sequence uses the same reply pattern | LR2-006 |
| Living group reaches the final basin | Complete its local response and accept the result | Stage Clear settles at 14 of 20 and continues to the save prompt and map | LR2-007, LR2-008 |

## Strategic and experiential structure

A large body keeps the group together but can block itself at a tight bend. A divided group fits the passage while spreading across local surfaces. Fruit increases both optional progress and the branches available to a sufficiently large group. At the chorus the immediate task changes from steering to waiting and then timing one familiar button. The linked note rewards support optional collection while ordinary level success remains a separate evaluation.

## Replay and variation

The original map permits replay of a cleared stage and shows past records. The recorded first clear retains discoveries and returns to the map. Later movement unlocks, note milestone rewards, maximum score, all-twenty reward identity and later branches need their own scope. There was no test of regional differences, exact physics, save-byte persistence, timing tolerances or a failed chorus route.

## Adjacent systems and history

Later house decoration, ad hoc or wireless modes, mini-games, stamp and photo systems, soundtrack behaviour, the PS4 remaster and other parts of the campaign have no role in this representation.

## Normalised genome

- Action: ACT-519, ACT-637, ACT-638, ACT-933.
- System Behaviour: SYS-036, SYS-037, SYS-1259, SYS-1260, SYS-1261, SYS-1262, SYS-2009.
- Constraint: CON-746, CON-747.
- Information: INF-192, INF-268, INF-457, INF-649.
- Objective: OBJ-181, OBJ-271.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `716` (`GAME-0001`–`GAME-0716`).
- Exact genome matches: none.
- Tied near matches: `GAME-0482` — LocoRoco (`17 / 21 = 0.809524`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [LocoRoco (GAME-0482)](locoroco.md) | ACT-519, ACT-637, ACT-638, CON-746, CON-747, INF-192, INF-268, INF-457, OBJ-181, OBJ-271, SYS-036, SYS-037, SYS-1259, SYS-1260, SYS-1261, SYS-1262, TIM-003 | Both games use the same tilt, bump, split, reunion, geometric fit, growth and local waiting loop. LocoRoco 2 adds repeated Circle replies, visible note opportunities and additional collectible notes. The original's all-twenty parts and Time Attack eligibility do not transfer to the sequel from the evidence here. | Near, `0.809524`. |

## Taxonomy impact

Retain the physical navigation and group rules shared with LocoRoco.
Admit separate mechanics for timed single-button replies, reward
emission and cue information. The original game's full-population
bonus includes a distinct mode unlock requirement that is outside
the confirmed boundary of this sequel fixture.

## Negative results

- The observed 14-of-20 clear rules out a compulsory all-twenty finish.
- Count stays at six when the group first splits for the descent.
  Separate nearby reunion restores form without replacing fruit growth.
- The evidence does not establish an exact reply window, a map-wide
  threshold, an accuracy penalty on misses or later unlock criteria.

## Delta summary

The same collective body behaves differently according to form and
location. First passage clearance calls for splitting. A qualified
group at a singing spot must stay still to start the local scene,
then the player's task switches to timed replies for additional notes.

## New facts

- A narrow curved descent admits separate small bodies at unchanged count.
- A marked chorus admits a group meeting the local participant count.
- The singing prompt uses the same Circle button as division, but cue timing
  controls the note rewards during the chorus.
- A partial collection clears the stage and returns to the map.

## Principles and design implications

Make clearance a consequence of body form while retaining population as
an independent resource. Use an unambiguous local prompt when a shared
button changes from managing body form to timing a chorus response.

## Puzzle or game generation potential

Connect a tilted slope, a narrow descent and a stable gathering area in
one route. Put an optional local event behind a disclosed living count
with a short single-button timing sequence. Verify that settling the
route is separate from maximizing the reward.

## New genes

- ACT-933
- INF-649
- SYS-2009

## New combinations

None.

## Taxonomy changes

[Taxonomy Change 463](../../../research/taxonomy-changes/TAXONOMY_CHANGE_463.md).

## New questions

- What happens at the first chorus with exactly five and fewer than five?
- How many replies can miss before optional rewards change, and does
  that affect the same event's traversal result?
- Does the retail North American UMD show the same first-stage cues and
  thresholds as the English PAL-labelled recording?

## Next recommended game

Continue Selection 062 with A Highland Song on the English macOS
Steam base game. Follow one early route clue to a crossing or shelter.

## Why this game

Franzea 1 shows the different roles of physical clearance, a local
population threshold and rhythm replies in one bounded level.

## Review status

Reviewed on 2026-11-25 for the stated PSP Franzea 1 scope. The
documentary evidence and bilingual presentation are pinned to that scope.
