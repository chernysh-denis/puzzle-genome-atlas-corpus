---
game_id: GAME-0646
slug: cairn
game_title: Cairn
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-363
    - ACT-859
  system:
    - SYS-661
    - SYS-662
    - SYS-665
    - SYS-1865
    - SYS-1866
  constraint:
    - CON-534
    - CON-536
  information:
    - INF-258
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Cairn

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: English native commercial PlayStation 5 Standard Edition,
  PlayStation Store product EP0771-PPSA28769_00-CAIRNGAMESTNOV25,
  released 29 January 2026. Use the launch-window base-game evidence.
  Exact installed revision and every difficulty and assist setting are
  undisclosed. The two traces both show actual graded piton placement.
- Entry: the lower grassy bench before the early cleft in The Escarpment
  on Mount Kami. Approach the gray fractured wall and choose a line toward
  the upper grassy terrace.
- Primary decision loop: move one hand or foot, test the reachable contact,
  maintain supported posture under live exertion and choose whether to stop
  to place protection or change line. The captures show different lines.
- Exit: top out over the terrace lip, regain upright movement and walk
  onward on the upper ground. This is a physical climb result without an
  end-of-level score or summit claim.
- Included: local route choice, individual limb placement, secure grip and
  bracing, fatigue signals, in-world fall, available piton timing and tether,
  and the completed transfer to walkable upper ground.
- Excluded: the training gym and Tenzen, the separate demo, other climbing areas,
  later DLC and equipment, Free Solo and assist-specific rules, numerical fall
  or stamina formulas, forced-save or reload behavior, bivouac inventory and
  survival systems beyond the observed fall's health debit.
- Suggested later scope: repeat the same line at identical settings while
  varying stance and piton timing. Check tether arrest before ground contact.

## Direct-play status

No direct play was performed. The storefront and release announcement establish
the native PS5 commercial base game. Postmode attributes a release-day trace to
a standard PS5. Stumpt identifies a PS5 Pro in an independent sponsored recording
with both the introduction and the chapter transition. Their outdoor route
landmarks, controls and top-outs agree. Their exact installed revision and full
assist setting lists were not shown. The observed timed placements, rather than
an assumed difficulty preset, define this packet. Frames were sampled without
audio. No hardware input capture, save-file inspection or reload was performed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| CAI-001 | The Game Bakers released the commercial native PS5 game on 29 January 2026. The scoped outdoor climb belongs to The Escarpment on the Kami route. | Confirmed | Corroborated | High | P1 storefront, P2 launch announcement, W1 base PS5 release-day capture, W2 PS5 Pro Escarpment chapter. P3 separates settings variants. |
| CAI-002 | From below, cracks and shelves offer a choice of route. With body support on the rock, one selected hand or foot is moved and placed. Automatic selection can be overridden on PS5. | Observation | Corroborated | High | P1 climbing description, P4 official PS5 controls, W1 8:14–8:48, W2 56:24–57:24. The captures show successive individual reaches, not which selection button was physically pressed. |
| CAI-003 | A placement can take a hold or merely brace. Reach and contact quality affect posture and its ability to sustain attachment. Low exertion reserve is signalled by visible strain and a closer view. | Observation | Corroborated | High | P3 visual cues, P4 braced versus retained hold. W1 12:20–12:41 shows changing contact and framing at the lip. Exact grip and fatigue values are unavailable. |
| CAI-004 | Attempted piton placement shows a timed bar. W1 displays Twisted shortly before a fall. W2 displays Perfect, then a visible tether and Off belay action as climbing continues. | Observation | Corroborated | High | P4 describes timing, supply and clipping into the placement. W1 10:08–10:11 and W2 58:41–58:53 show different placement labels. No anchor strength or timing frame thresholds were isolated. |
| CAI-005 | In W1 the climber loses the wall, makes ground contact, loses part of the health bar and gets back up on the same bench. The next attempt uses the brighter slab to the right. | Observation | Direct | High | W1 10:10–10:39. The capture does not isolate whether anchor grade, rope length or some other factor determined ground impact. |
| CAI-006 | Both lines reach the upper portion of the same terrace. After hands pass over the rim and the body climbs onto the shelf, the climber walks on grass and stone while the next wall is accessible. | Observation | Corroborated | High | W1 12:35–13:12, W2 1:01:49–1:02:13. W1 reaches the lip by a painted mark, while W2 tops out nearer the tree. |

## Basic data

- Analysis target: `PLAT-PLAYSTATION-5`, English commercial PS5 Standard Edition.
- Developer and publisher: The Game Bakers.
- Mechanical families: `FAM-007`, physics and object manipulation,
  and `FAM-010`, real-time system pressure.
- Checked: 2026-11-22.
- P1: [PlayStation Store Standard Edition](https://store.playstation.com/en-us/product/EP0771-PPSA28769_00-CAIRNGAMESTNOV25/).
- P2: [Developer commercial release and edition announcement](https://www.thegamebakers.com/cairn-launches-january-29-pinky-promise/).
- P3: [Developer accessibility and difficulty settings](https://www.thegamebakers.com/cairns-accessibility-options/).
  Fall rewind, infinite supplies and grounded auto-saving are optional and
  excluded from the signature.
- P4: [PlayStation's launch-day climbing controls and rules](https://blog.playstation.com/2026/01/29/cairn-8-advanced-climbing-tips-to-make-it-to-the-summit/).
  Establishes wall inspection, limb override, contact and the piton interaction.
- W1: [Postmode, native base PS5 release-day capture](https://www.youtube.com/watch?v=8muHFtHT6C0&t=490s).
- W2: [Stumpt, native PS5 Pro playthrough, The Escarpment](https://www.youtube.com/watch?v=xeA3befhPO8&t=3384s).
  Sponsored by the developer and attributed independently of W1.

## Mechanical decomposition

### Action Genes

- ACT-008: walk to a selected point below the rock and resume direct travel
  after topping out.
- ACT-363: commit a carried piton to compatible nearby rock from the wall.
- ACT-859: direct one suggested or explicitly selected limb toward a reachable
  placement while the other limbs preserve the current stance.

### System Behaviour Genes

- SYS-661: posture, geometry and usable exertion govern continuing grip.
- SYS-662: the observed falling body strikes ground and loses health in place.
- SYS-665: the placed piton connects a physical tether to the wall. W2 shows
  the clipped state and the subsequent wall movement.
- SYS-1865: place a hand or foot against the target. The contact can secure a
  grip or merely brace and leave the current stance less sustainable.
- SYS-1866: resolve the manual timing slider into a displayed piton placement
  grade. The captured results include Twisted and Perfect.

### Constraint Genes

- CON-534: continued attachment depends on reachable surface and usable stamina.
- CON-536: deployment depends on the carried aid and compatible terrain. The
  evidence does not establish a maximum stock or exact geology of this face.

### Information Genes

- INF-258: folds and ledges show opportunities, while pose, camera distance and
  the visible response to a placement expose strain and risk.

### Objective Genes

- OBJ-026: reach the upper terrace and regain direct grounded travel with the
  next terrain open.

### Time Genes

- TIM-003: exertion and slip risk remain live while the player chooses the next
  contact. Piton timing also advances while awaiting the press.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| Grass and rock at the bottom of the early Escarpment face | Approach the cleft and put the first limb against reachable rock | Start ascent from the lower bench | CAI-002 |
| Body held by several contacts | Aim and place one hand or foot | The selected contact changes support and affects the next possible reach | CAI-002, CAI-003 |
| Climbers stop at different wall positions | Attempt piton placement and time the press | W1 sees Twisted. W2 sees Perfect and the connected rope | CAI-004 |
| W1 loses the wall after the placement | Fall and strike the grass | Health bar decreases. The climber gets back up and attempts the nearby slab | CAI-005 |
| The new line reaches the rim | Move the upper limbs beyond the lip and finish the transfer | Both feet come onto the upper terrace and ordinary traversal returns | CAI-006 |

## Strategic and experiential structure

A foothold can be chosen to improve the next reach even when it gives up
immediate height. The visible cracks offer different sequences of contacts.
Stopping to set protection takes time while exertion is live. The better
placements in the two traces occurred on different trajectories and are not
a controlled comparison of anchor strength.

## Replay and variation

W1 tries the shaded cleft, falls to the lower bench and uses the adjacent
brighter slab to reach the rim near a painted mark. W2 continues along the
cleft with a placed line and reaches the same upper ground nearer the tree.
Both preserve movement on the terrace. No additional course grade is needed
for the observed terminal.

## Adjacent systems and history

The demo includes the gym and the Tenzen training ridge. This packet uses the
commercial Kami route. The developer documents separate setting options for
fall rewind, extra gear, saving and survival. Later biomes and all camp and
summit systems are outside the recorded boundary.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-363, ACT-859 | Approach, request protection and choose a single contact |
| System Behaviour | SYS-661, SYS-662, SYS-665, SYS-1865, SYS-1866 | Maintain grip, resolve impact and tether, test contacts and grade piton placement |
| Constraint | CON-534, CON-536 | Require reachable compatible support, usable exertion and legal aid placement |
| Information | INF-258 | Expose affordance and physical strain |
| Objective | OBJ-026 | Top out onto the traversable terrace |
| Time | TIM-003 | Evolve grip and placement timing in real time |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `645` (`GAME-0001`–`GAME-0645`).
- Exact genome matches: none.
- Tied near matches: `GAME-0552` — Jusant (`9 / 28 = 0.321429`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Jusant (GAME-0552)](../g-l/jusant.md) | ACT-008, ACT-363, CON-534, CON-536, INF-258, OBJ-026, SYS-661, SYS-665, TIM-003 | Both read rock geometry, spend usable exertion, place safety gear and reach grounded terrain. Jusant maps the hands separately and limits rope payout, with temporary anchors returned between climbs. Cairn selects one hand or foot for each contact, distinguishes grip from bracing and grades the piton press. The scoped Cairn retry got up after a damaging ground impact. | Near, `0.321429` |

## Taxonomy impact

Three additions isolate a single selected limb input, its grip-versus-brace
contact resolution and the timed piton grade. Existing definitions admit wall
cost, terrain compatibility, physical fall and rope without duplicating them.
ACT-114 maps two hands to independent channels. This action selects among
hands and feet for one reach. The two captures do not isolate a tether-arrested
fall without ground contact, so SYS-1598 is left outside this scope.

## Negative results

- A contacted surface can support a brace without producing a secure grip.
- The captured Twisted placement did not prevent ground impact. The cause of
  that impact cannot be isolated from the observed fall.
- W2 top-out does not verify survival after falling on its Perfect placement.
- The terrace arrival provides a navigable successor without a measured save,
  explicit course score or proof of a summit clear.

## Delta summary

Thirteen scoped genes, three new and ten reused. The route runs from the
Escarpment bench to the grassy terrace after the first observed retry.

## New facts

- One chosen limb moves toward the next rock contact as the stance remains live.
- Timed piton placements display different results in the two traces.
- Both the retry up the slab and continued travel through the cleft top out.

## Principles and design implications

Make contact legible through the body and the rock. Offer a next foothold that
improves posture without leading immediately upward. Make the result visible as
the return to grounded movement, so the player can choose the next face.

## Puzzle or game generation potential

Prototype an early gray wall with a divided cleft and two lines to the same
walkable terrace. Track accepted contacts, weak bracing and timed protection
separately. Identify the supported exit through the transition to walking.

## New genes

- ACT-859
- SYS-1865
- SYS-1866

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_392](../../../research/taxonomy-changes/TAXONOMY_CHANGE_392.md).

## New questions

How much of the ground impact depends on the observed piton grade and how much
on position and effective tether length? A same-route controlled comparison
would separate those causes.

## Next recommended game

Analyse the first complete dragon fight on the original North American Saturn
disc one of Panzer Dragoon Saga.

## Why this game

A single early face makes limb placement, stance, protection and the successful
return to walkable support separately observable on commercial PS5.
