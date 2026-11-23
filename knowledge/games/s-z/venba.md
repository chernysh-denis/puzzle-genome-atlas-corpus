---
game_id: GAME-0642
slug: venba
game_title: "Venba"
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-854
    - ACT-855
  system:
    - SYS-1854
    - SYS-1855
  constraint:
    - CON-868
  information:
    - INF-596
  objective:
    - OBJ-346
  time:
    - TIM-002
---

# Game: Venba

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: English-language commercial base release for Xbox
  Series X|S, store product 9P5P55S7HB9S, released on 31 July 2023.
  The release trace is labelled Xbox Series X. Neither a build number
  nor a separate capture from Series S is available.
- Primary decision loop: use the surviving recipe clues to prepare
  and orient stacked idli plates, then check the cooked result.
  If only the bottom cooks, the diagnosis guides a new attempt.
- Entry: reach Venba's first idli worktop. The worn recipe, batter,
  water, cloth and cooker are available.
- Exit: open the cooker after a successful cycle, see the prepared
  idlis in the lunchbox and reach the immediate conversation with
  Paavalan at the table.
- Included: the surviving recipe and diagrams, contextual transfers,
  preparation and orientation of stacked plates, heating and visible
  result, same-dish retry and the successful narrative transition.
- Excluded: preview/demo rules, ports, achievements, later recipes and
  story branches, chapter selection, exact hidden geometry of steam
  validation and physical button timings.
- Suggested later scope: isolate failed preparation with no cloth and
  inspect the validation difference between that and blocked steam paths.

## Direct-play status

No direct play was performed. The Xbox product listing establishes
the commercial Series X|S target. The Xbox Wire interview identifies
the first dish and the role of the damaged cookbook. A Series X
release recording establishes both a partial failure with local retry
and the successful dish followed by dialogue. A second recorded guide
and a written Xbox achievement guide corroborate preparation. The
second recording is not additional proof of native Xbox hardware.
Silent frames were inspected. Exact rotation coupling and the number
of valid orientations were not isolated.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| VB-001 | The commercial base game has an optimised Xbox Series X and Series S release, product 9P5P55S7HB9S, from Visai Games on 31 July 2023. Idlis are the opening dish. | Confirmed | Direct | High | P1 official product record, P2 creator interview about the first recipe, P3 developer site. W1 disclosure identifies Xbox Series X but does not establish an exact software build. |
| VB-002 | The player can consult a damaged recipe on the worktop. The surviving prompts name supplies and show the perforated plates and the path for steam. The page leaves a lining or arrangement relationship to interpret. | Observation | Corroborated | High | P2 damaged-cookbook description; W1 3:40–4:02 and 4:33–4:40. A surviving fragment about leakage is not proof of a separately recorded failure. |
| VB-003 | Water goes to the cooker. A cloth and then batter are applied to each plate for the successful assembly. The prepared plate moves into the cooker as a unit. Water can be added before the first plate or after the plates and before starting heat. | Observation | Corroborated | High | W1 7:50–8:30, water first; W2 2:41–3:23, water after loading, with success at 3:37; R1 handling of cloth, batter and plates. |
| VB-004 | Rotation controls allow the fitted plates' visible arrangement to change during successive loading. An arrangement that prevents steam from reaching the upper layers can still be heated but does not cook those layers. | Observation | Corroborated | High | W1 7:28–7:40 diagnosis and 8:10–8:30 corrections; W2 2:41–3:19; R1 orientation instruction. The footage does not expose exact hidden angle or pivot rules. |
| VB-005 | The player closes the cooker and starts heat. After a short automated interval the game cues opening. Lifting the lid is a separate action that reveals the cooked result. | Observation | Corroborated | High | W1 7:05–7:28 and 8:42–9:01; W2 3:23–3:37 shows lid, heat control and then removal. |
| VB-006 | The failed cook can leave only the lowest plate cooked. The dialogue diagnoses insufficient steam above and points to orientation. Continuing on the retry cue restores the worktop and ingredients for the same dish. | Observation | Corroborated | High | W1 7:24–7:50, including the diagnosis and the cue before the worktop resets; R1 corroborates a local retry. No chapter restart or charge is visible. |
| VB-007 | The successful cook yields a completed result after opening. The game shows the idlis in the lunchbox, then carries the player into the family dialogue. | Observation | Corroborated | High | W1 8:59–9:25 and W2 3:36–3:52, completed state, plated lunchbox and conversation. |
| VB-008 | The preparation action phase can be paced by the player while the recipe is read and plates are arranged. The separate heating interval runs automatically. | Observation | Corroborated | High | W1 3:35–4:02 and later worktop activity, with pauses and recipe revisits before closure; W2 completes the same phase faster. No inferred time limit applies to the whole game. |

## Basic data

- Analysis target: `PLAT-XBOX-SERIES`.
- Developer and Xbox publisher: Visai Games Inc.
- Mechanical family: `FAM-006`, spatial assembly and packing.
- Checked: 2026-11-22.
- P1: [Commercial Xbox listing](https://www.xbox.com/en-ca/games/store/venba/9p5p55s7hb9s).
- P2: [Xbox Wire interview with creative director Abhi, 19 July 2023](https://news.xbox.com/en-us/2023/07/19/venba-interview/).
- P3: [Visai Games' official game site](https://venbagame.com/).
- W1: [Xbox Stadium, opening on Xbox Series X](https://www.youtube.com/watch?v=cB9uSjqJuyw&t=215s).
- W2: [Lordacris Gaming, release-week cooking guide](https://www.youtube.com/watch?v=VGQ3xrFOm7w&t=160s)
  and [dated Xbox guide entry](https://www.trueachievements.com/forum/viewthread.aspx?tid=1486570).
- R1: [Tozi Tiberius, written Xbox guide, 31 July 2023](https://www.trueachievements.com/a398830/like-it-was-yesterday-achievement).
  The guide helps check tool order and positioning. Achievement
  eligibility is outside the analysis.

## Mechanical decomposition

### Action Genes

- ACT-854: address the cooker with water, prepare the plates with
  cloth and batter and transfer the prepared assemblies.
- ACT-855: use the rotation control on the fitted arrangement
  between successive insertions.

### System Behaviour Genes

- SYS-1854: close and heat the cooker, wait for the ready cue
  and open it to inspect the result.
- SYS-1855: expose the partial cooking result and probable cause,
  then restore the worktop for a retry of the same dish.

### Constraint Genes

- CON-868: the stacked configuration must allow steam to reach
  the upper plates. Unsuitable configurations can reach the heating
  stage and fail at inspection.

### Information Genes

- INF-596: show available ingredients and diagrammatic instructions
  in a damaged recipe, with relationships to infer.

### Objective Genes

- OBJ-346: achieve the cooked dish, see the serving transition
  and reach the family scene.

### Time Genes

- TIM-002: choose the pace of recipe reading and assembly.
  The closed-cooker interval is a separate system transition.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| First idli worktop | Open and inspect the recipe | The tools, supplies and pictured steam path are available even where text is damaged | VB-002 |
| Empty cooker and unprepared plate | Apply cloth, then batter and move the loaded plate into the open cooker | Its contents stay arranged as a single prepared assembly | VB-003 |
| Fitted plate with a further loaded plate available | Turn the arrangement between insertions | The visible relative positions of moulds and vents change | VB-004 |
| Loaded and watered cooker with obstruction | Close the lid, start heat, then reopen after the cue | Only the lower plate has cooked, with an explanation of the blocked path | VB-004, VB-005, VB-006 |
| Failed dish with diagnostic dialogue | Continue after the retry cue | The empty pot, water, batter and cloth are available again at the same worktop | VB-006 |
| Reassembled, watered plates | Heat and reopen after the cue | The dish succeeds and the prepared lunchbox leads to dialogue with Paavalan | VB-007 |

## Strategic and experiential structure

A plate is a retained assembly, but a legal insertion can still
create an arrangement that fails under steam. The cookbook provides
a prediction, the cooked stack supplies feedback and the retry
tests the revised prediction on the same dish.

## Replay and variation

W1 adds water before the first plate and W2 adds it after the loaded
plates. Both succeed. Cloth before batter is present on the observed
successful plates. W1 contains a full failed cook followed by a successful
attempt. W2 shows an independently completed assembly and the same
type of successful result. One observed rotation sequence establishes
a working arrangement only.

## Adjacent systems and history

The interview describes other dishes and scenes from different
times in the family's life. The analysis stops at the conversation
immediately after the opening idlis. It does not treat later narrative
choices or recipe mechanics as features of this workstation.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-854, ACT-855 | Apply supplies to the receiving item and turn the fitted arrangement |
| System Behaviour | SYS-1854, SYS-1855 | Resolve the closed cook, diagnose partial failure and restore the worktop |
| Constraint | CON-868 | The upper plates need a viable steam path |
| Information | INF-596 | Read surviving recipe text and geometry |
| Objective | OBJ-346 | Complete the dish and reach the family scene |
| Time | TIM-002 | Read and arrange at the player's pace |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `641` (`GAME-0001`–`GAME-0641`).
- Exact genome matches: none.
- Tied near matches: `GAME-0064` — SET (`1 / 12 = 0.083333`); `GAME-0637` — Tiny Glade (`1 / 12 = 0.083333`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [SET (GAME-0064)](set.md) | TIM-002 | The player can examine the visible material and act at their own pace. SET judges three chosen cards by their attribute relationships. Venba requires an assembled cooking configuration and a separate heat cycle before its result is visible. | Near, `0.083333` |
| [Tiny Glade (GAME-0637)](tiny-glade.md) | TIM-002 | Both let the player revise arrangements at their own pace. A ground path at a compatible wall changes its opening immediately in Tiny Glade. Venba checks steam access after heating and can restore ingredients after a partial failure. | Near, `0.083333` |

## Taxonomy impact

Seven new definitions separate preparation, fitted rotation, steam
access, incomplete instructions, cooked-result inspection, local retry
and the dish outcome. Reuse TIM-002 for the self-paced preparation.
The operational differences from scored cooking lessons and other
inventory actions are recorded in the taxonomy change.

## Negative results

- Accepted placement does not establish a finished dish. The failed
  stack was mounted, heated and then diagnosed.
- An observed successful rotation is not evidence of its unique angle
  or of independently rotating a particular hidden layer.
- Water-first is not required for a successful outcome in the two
  observed release paths.
- The retry restores local ingredients and returns to the same recipe.
  The eventual lunchbox arrangement is presented after success rather
  than exposed as player-controlled decoration in the scoped dish.

## Delta summary

Eight scoped genes, seven added and one reused. Two different cooked
results are visible, with an observed local retry and narrative successor.

## New facts

- The damaged recipe's diagram helps explain why a stack that fits
  can still cook only its bottom layer.
- Success and failure are revealed on opening the cooker.
- Recovering the worktop keeps the same dish available for another try.
- A successful dish brings the player to the family conversation.

## Principles and design implications

Separate the legality of assembling a structure from its performance
at evaluation. Provide evidence about a partial outcome so the player
can revise the arrangement using the same ingredients.

## Puzzle or game generation potential

Prototype a layered assembly with visible small openings and an
incomplete diagram. A closed evaluation resolves progress on each
layer. A diagnostic identifies the highest reached layer and restores
the setup so the player can improve the arrangement.

## New genes

ACT-854, ACT-855, CON-868, INF-596, OBJ-346, SYS-1854 and SYS-1855.

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_388](../../../research/taxonomy-changes/TAXONOMY_CHANGE_388.md).

## New questions

Which orientations succeed across the loaded layers, and what exact
outcome follows from omitting the cloth while preserving a valid stack?

## Next recommended game

Analyse the original North American Genesis Rocket Knight Adventures
from its first stage through its settled result and actual next state.

## Why this game

Recipe reading, stack geometry and a revealed cooking outcome make the
first dish a compact loop of interpretation, testing and revision.
