---
game_id: GAME-0700
slug: planet-of-lana-ii
game_title: "Planet of Lana II: Children of the Leaf"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-408
  system:
    - SYS-061
  constraint: []
  information:
    - INF-639
  objective:
    - OBJ-026
  time: []
---

# Game: Planet of Lana II: Children of the Leaf

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Ask Mui to hold the floor plate long enough for Lana to make two
jumps. The temporary foothold folds when the companion leaves.

## Analysis scope

- Version / ruleset: the commercial English Nintendo Switch 2 Edition
  of Wishfully's sequel, launched by Thunderful on March 5, 2026. The
  Nintendo UK listing identifies game page 3043028. The recording
  attributed to this edition supplies the route and the Switch prompt.
  The installed patch number is not available.
- Structured analysis target: PLAT-NINTENDO-SWITCH-2 in
  [platform coverage](../../platforms/games.json).
- Entry: Chapter 1, Secrets, after Lana and Anua reunite with Mui.
  Follow the first route toward the captain's quarters to the floor
  plate beneath the folding plant ledge.
- Primary decision loop: get Mui onto the floor plate and give the
  stay order while the ledge is extended. Move Lana separately to
  the foot of the high structure. Jump onto the plant ledge, then
  jump again and pull onto the higher fixed top. Recall Mui once
  Lana stands on the fixed surface.
- Positive terminal: reach the floor beyond the high structure and
  reunite with Mui by the first closed generator door. Stop before
  giving Mui the next generator action.
- Included: direct movement and the two-step climb, the paired Stay
  and Follow cue, the companion's temporary assignment, occupancy
  maintaining the extended plant ledge, release and local reunion.
- Excluded: previous solo sequences, the prologue, Anua's movement
  logic, precise command distance and jump timings, testing every
  possible plate occupant, the next generator door, water, later
  companion or robot powers, the demo and all other editions.
- Potential scoped module: compare the first generator door with
  the next room's shorter opening after the same companion action.
- Direct-play status: no personal Switch 2 session or input trace.
  The release listing and a platform-attributed Switch 2 recording
  anchor the scope. A second commercial-game recording corroborates
  the route, with its platform unverified. Short frame sequences
  were sampled silently in the background.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| LANA2-001 | Wishfully's commercial Nintendo Switch 2 Edition was released on March 5, 2026 and supports English. The release is separate from the demo. | Confirmed | Direct | High | P1, P2, P3 |
| LANA2-002 | While the player controls Lana’s movement, the field prompt shows one button for two orders to Mui. The Switch 2 presentation labels A as Stay and hold A as Follow. | Observation | Corroborated | High | W1 19:34–20:12; W2 13:55–14:21 confirms the paired meanings, with different glyphs; S1, S2 |
| LANA2-003 | Mui can wait on the floor plate while Lana travels independently. The plate holds the plant shelf extended, and the shelf folds when the plate is vacated during recall. | Observation | Corroborated | High | W1 20:09.5–20:23.5; W2 14:14–14:28; S1, S2 |
| LANA2-004 | With the shelf still extended, Lana jumps onto it, then jumps toward the higher fixed top and pulls up. The floor plate and the usable foothold are separate positions. | Observation | Corroborated | High | W1 20:13–20:19; W2 14:21–14:28; S1, S2 |
| LANA2-005 | The player can resume Follow after reaching stable support, then continue to the far side. Mui is visible again by the subsequent generator-door area. That door is a successor fixture, separate from the plate controlled shelf. | Observation | Corroborated | High | W1 20:21–20:34; W2 14:28–14:35; S1 |

## Basic data

- Release / origin: Wishfully and Thunderful, English digital
  Nintendo Switch 2 Edition, March 2026.
- Mechanical families: FAM-015 for separating companion stationing
  from directly controlled traversal and rejoining after the crossing.
- P1: [Nintendo US commercial product](https://www.nintendo.com/us/store/products/planet-of-lana-ii-nintendo-switch-2-edition-switch-2/).
  Lists edition, date, publisher and English support.
- P2: [Nintendo UK edition listing](https://www.nintendo.com/en-gb/Games/Nintendo-Switch-2-Edition/Planet-of-Lana-II-Nintendo-Switch-2-Edition-3043028.html).
  Identifies the Switch 2 Edition and distinguishes its presentation
  enhancements from the original Switch product.
- P3: [Thunderful launch statement](https://thunderfulgames.com/planet-of-lana-ii-children-of-the-leaf-is-out-now/).
  Names the sequel, dates launch and identifies the demo separately.
- W1: [JustOneGamr Switch 2 new-game recording](https://www.youtube.com/watch?v=rO_yD8Eq1-w&t=1197s).
  The author identifies a publisher-supplied game code and a
  Nintendo Switch 2 session. The upload does not expose an installed
  patch identifier.
- W2: [BeardBear full-game route](https://www.youtube.com/watch?v=FqgGT3xiWfo&t=849s).
  Starts Chapter 1 at 3:00. Used for independent visual confirmation
  of the same room, companion policy and landing, without assuming
  its hardware or substituting its controller prompts.
- S1: [Into Indie Games first-chapter walkthrough](https://intoindiegames.com/walkthroughs/planet-of-lana-2-walkthrough-chapter-1-2-secrets-and-home-sweet-home/).
  Describes having Mui wait on the switch, climbing the platform and
  calling Mui back from the other side.
- S2: [GAMES.GG Chapter 1 guide](https://games.gg/planet-of-lana-ii-children-of-the-leaf/guides/planet-of-lana-2-chapter-1-walkthrough/).
  Confirms the stay/hold assignment, plant foothold and distinction
  from the following generator rooms.
- Claim IDs: LANA2-001–LANA2-005.

### Reproducible fixture evidence

1. In Secrets, after the reunion, approach the first plant ledge
   during the route toward the captain's quarters. W1 shows the
   goal near 19:48 and the room with paired Follow and Stay cues
   around 20:01. W2 shows the same room and prompts around 14:10.
2. Keep Mui in Follow until the two are close to the panel. Issue
   Stay with Mui on the panel. Around 20:09.5 in W1, Lana has
   begun moving right while the small dark companion remains at
   the amber-marked panel and the plant shelf is extended. W2
   shows a folded profile during the approach at 14:16 and a
   projecting foot surface by 14:21 with Mui down at the panel.
3. Move Lana under the ledge and jump up onto it from the right
   side, then reverse the direction to jump onto the taller
   solid structure. W1 shows her on the shelf at 20:16.5 and
   pulling onto the higher surface at 20:18.5–20:19.0. W2
   shows the corresponding moments at 14:24.5 and 14:28.0.
4. With Lana standing on the fixed surface, restore Follow. W1
   shows the shelf still extended at 20:21.0, then folded by
   20:23.5 as Mui moves away. The on-screen companion indicator
   shows its new position when the animal is obscured. Proceed
   down to the far side and stop with the party near the next
   generator door, before activating it. W2 shows Mui again at
   floor level around 14:34.5.

## Mechanical decomposition

### Action Genes

- ACT-008: move Lana under the extended shelf, take the two jumps
  to the fixed top and proceed to the far side.
- ACT-408: directly address the accompanying Mui with Stay to
  preserve the current position, then with Follow to reunite. The
  action changes Mui's control relation without taking over the
  companion's locomotion.

### System Behaviour Genes

- SYS-061: Mui's continuous occupancy sustains the linked
  extended plant ledge. After departure, the shelf folds,
  removing that temporary foothold.

### Constraint Genes

No independent constraint is admitted. Using the foothold while it is
extended follows from its maintained occupancy state.

### Information Genes

- INF-639: the paired A-button prompts show short press for Stay
  and hold for Follow at the same command opportunity.

### Objective Genes

- OBJ-026: reach the far side of the climb after making the
  intermediate route available. The local task includes recalling
  Mui before the next fixture is operated.

### Time Genes

No independent timer is established. The availability window is
controlled by the companion's position.

### Parameters

Companion mode and position, panel contact region, cue glyph, linked
plant shelf, jump approach and independent landing are parameters.

## Reproducible transitions

| Entry state | Input | Expected next state | Evidence |
| --- | --- | --- | --- |
| Mui follows Lana near the panel | Position Mui on the panel and tap Stay | Mui remains on the panel so the linked shelf stays extended | LANA2-002–LANA2-003 |
| The shelf is held out | Jump from the lower floor to the shelf, then onto the fixed top | Lana takes the new two-step route while Mui remains below | LANA2-004 |
| Lana stands on the fixed top | Restore Follow | Mui leaves the panel and the shelf folds | LANA2-003, LANA2-005 |
| Lana and Mui can proceed | Descend to the far side and reunite by the door approach | Both reach the next fixture without activating it | LANA2-005 |

## Strategic and experiential structure

The button assignment and the mechanism have different states. Mui
holds a position to maintain a route while Lana is free to leave.
Recall waits until stable support replaces the temporary foothold.

## Replay and variation

The witnesses show settling at the panel, then the same climb and
recall. They establish neither a checkpoint reset location nor the
result of calling Mui in the middle of Lana's jump. In the observed
route the plant ledge folds without undoing Lana's arrival on the
fixed ledge.

## Adjacent systems and history

Earlier solo Mui puzzles and later generator actions use other
command and power contexts. Repeated Stay and Follow assignments
here do not establish all of the sequel's expanded companion controls.

## Normalised genome

- Action: ACT-008, ACT-408.
- System Behaviour: SYS-061.
- Constraint: none.
- Information: INF-639.
- Objective: OBJ-026.
- Time: none.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `699` (`GAME-0001`–`GAME-0699`).
- Exact genome matches: none.
- Tied near matches: `GAME-0098` — Hyperbolica (`2 / 10 = 0.200000`); `GAME-0666` — Chicory: A Colorful Tale (`2 / 10 = 0.200000`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Hyperbolica (GAME-0098)](../g-l/hyperbolica.md) | ACT-008, OBJ-026 | Both navigate directly to a specific world location. Hyperbolica reads and selects junctions in fixed hyperbolic geometry. Lana depends on a temporary foothold that another body keeps extended. | Near, `0.200000`. |
| [Chicory: A Colorful Tale (GAME-0666)](../a-f/chicory-a-colorful-tale.md) | ACT-008, OBJ-026 | Both make a higher destination reachable and then navigate to it. Chicory's marked plant launches the avatar on contact and spends its prepared pigment state. Mui's continuous plate occupancy supplies a platform on which Lana can stand before making a second jump. | Near, `0.200000`. |

## Taxonomy impact

Reuse direct navigation, an addressed follow/wait order, sustained
occupancy and reaching a designated place. Add the paired short/held
command cue. The plate and retracting foothold form one coupled
mechanism rather than requiring a separate gene for timed closure.

## Negative results

- The Switch prompts show a direct policy order to the companion,
  not a command to consume a key or permanently latch the support.
- Recalling Mui after landing removes access to the temporary plant
  surface. It does not reopen the higher-route task.
- The proof ends before the generator door. This route does not
  establish whether the chapter's later switches use the same rule.

## Delta summary

Five genes cover a reversible companion assignment and the route
that depends on it.

## New facts

- A short press and a hold on the same input disclose two different
  companion orders.
- A reachable horizontal foothold can require a companion to remain
  assigned below.
- The fixed landing survives losing the temporary intermediate route.

## Principles and design implications

Present the two companion orders together before separating the
actors. Make the temporary route readable and give the player a
stable endpoint from which it is safe to recall the holder.

## Puzzle or game generation potential

Use one station, an independent helper and a temporary step. Test
that moving the helper while the main actor is still below removes
the shortcut, and that moving it from the permanent destination
permits a local reunion without changing the goal geometry.

## New genes

- INF-639

## New combinations

None. None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 446](../../../research/taxonomy-changes/TAXONOMY_CHANGE_446.md).

## New questions

- Which other bodies can sustain the room's plate?
- How do the two generator-door rooms alter the safe time for recall?

## Next recommended game

Continue Selection 060 with GAME-0701, Warcraft II: Tides of
Darkness, on MS-DOS.

## Why this game

The first shared climb isolates the difference between using a
companion to create a route and keeping the route available until
the controlled actor no longer needs it.
