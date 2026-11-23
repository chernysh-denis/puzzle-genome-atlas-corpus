---
game_id: GAME-0622
slug: pepper-grinder
game_title: "Pepper Grinder"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
    - ACT-829
    - ACT-830
  system:
    - SYS-037
    - SYS-369
  constraint:
    - CON-862
  information:
    - INF-119
    - INF-179
    - INF-317
  objective:
    - OBJ-283
  time:
    - TIM-003
---

# Game: Pepper Grinder

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Soft-ground colors and the first stage's layout are evidence instances.

## Analysis scope

- Version / ruleset: English, commercial Nintendo Switch digital base
  game, released March 28, 2024. Both recordings are from the release
  period. Exact recorder region, entitlement and patch are unverified.
- Primary decision loop: steer on the surface until an exposed soft
  region can be entered. Power the drill, turn within the material and
  time a boost before emerging to reach a safe landing or the next
  patch. Avoid enemies and hazards or retry from the last lit lantern.
  Activate the final flag fixture to clear the stage and open the map route.
- Entry: the first controllable part of 1-1 Lost Claim on a new game,
  before the first in-stage drill prompt.
- Exit: the drill-operated flag settlement and the opening of 1-2
  Wellspring Canyon on the map. The recorded entry into 1-2 confirms
  access. Its traversal rules, including swimming, are outside this analysis.
- Included: ordinary movement and jumps, directed drilling, the material
  boundary, boosting before emergence, visible surface and in-stage control
  information, contact pickups, health display and checkpoint recovery,
  flag operation and map-route opening. Skull Coins can be collected and
  credited with the clear without requiring a full set.
- Excluded: the introductory story, later stages, other terrain types
  and detachable drill attachments, swimming, water skimming, grappling,
  the shop, gold-key branches, sticker collection, Time Attack, later
  updates, other platforms and optional cannon detours. No exact speed,
  input window,
  recovery retention rule or collision dimensions are claimed.
- Suggested later scope: water entry, sinking and skimming in a
  separately bounded run of Wellspring Canyon.

## Direct-play status

No direct play was performed. Nintendo and Devolver identify the
commercial release. The booklet, which diagrams a Switch Pro Controller,
supplies the drill, jump, checkpoint and finish rules. Two separately
recorded Switch playthroughs show the course and actual map handoff.
The first collects more Skull Coins and visibly retries. The second
reaches the successor with uncollected first-stage coins. Only written
sources and static frames were inspected, without audio or video playback.
The frames do not establish precise button timings or executable identity.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PG-001 | The commercial Switch download released March 28, 2024, includes American English and single-player play. The captured opening belongs to its ordinary campaign. | Confirmed | Corroborated | High | P1, P2, W1 opening and W2 opening. No exact recording build is asserted. |
| PG-002 | The player steers the same body on ordinary surfaces and through designated soft material using the drill. Within an exposed soft pocket the body can turn; fixed rock bounds the route. | Confirmed | Corroborated | High | P1, P2, P3 pp. 3 and 6; W1 1:40–2:20 and 4:20, W2 2:00 and 3:20. |
| PG-003 | The jump command during powered drilling increases speed. Used just before emergence, it can make a fast airborne arc across a gap; the trajectory depends on position and heading at exit. | Confirmed | Corroborated | High | P3 p. 7, W1 1:50, 3:10–3:30 and 4:40–5:10, W2 3:00–3:40. The trajectories support the rule; button timing comes from the booklet. |
| PG-004 | Fixed local prompts expose how to operate the drill or boost. Soft material, ordinary rock, enemies, health and visible pickups furnish in-stage information; contact can credit a collectible while movement continues. | Observation | Corroborated | High | P3 pp. 4, 6–9; W1 1:20–1:50, 2:10 and 3:10; W2 1:40 and 4:40–5:00. |
| PG-005 | At zero health the attempt resets to the last lit lantern. The reference trace shows empty health, then restored health and renewed control at an earlier section. | Confirmed | Corroborated | High | P3 p. 4; W1 6:10–6:30 and return toward the same pits. No general inventory retention claim. |
| PG-006 | The authored finish fixture requires using the drill. It raises the flag and closes the level, revealing the successor on the map. The reference route returns to the completed Lost Claim entry and then enters the new stage. | Confirmed | Corroborated | High | P3 pp. 3–4; W1 7:50 flag area, 8:00 Lost Claim map entry, 8:10 successor gameplay; W2 5:30 at the flag base, 5:40 Wellspring Canyon map selection and 5:50 active play. |
| PG-007 | Lost Claim can be cleared with an incomplete optional Skull Coin set. In the independent trace, the finish-area HUD has both marked and unmarked slots, then the successor is selected and entered. | Observation | Corroborated | High | P3 pp. 3 and 9; W1 8:00 shows five marked slots; W2 5:30–5:50 shows the incomplete alternative and successful handoff. |

## Basic data

- Analysis target: `PLAT-NINTENDO-SWITCH`.
- Developer: Ahr Ech. Publisher: Devolver Digital.
- Mechanical family: `FAM-007` for steering under contact and momentum on
  a spatial route. Entering soft material changes body movement without a
  demonstrated durable edit to the route graph.
- Checked: 2026-11-21.
- P1: [Nintendo Switch commercial listing](https://www.nintendo.com/us/store/products/pepper-grinder-switch/).
- P2: [Devolver commercial edition and mechanical overview](https://www.devolverdigital.com/games/pepper-grinder).
- P3: [Devolver instruction booklet](https://cdn.akamai.steamstatic.com/steam/apps/2076580/manuals/Pepper_Grinder_Manual.pdf?t=1709813521).
  Pages 3–4 cover map, health and the finish; 5–7 show Switch controls,
  supported movement, turning during drill use and the boost.
- W1: [Handheld Players, release-day Switch](https://www.youtube.com/watch?v=icF2GdeAeyk&t=68s).
  See 1:40 for the curved soft path, 3:10 for the launch cue,
  6:20–6:30 for the recovery sequence and 7:50–8:10 for the handoff.
- W2: [GameCorner, Switch playthrough](https://www.youtube.com/watch?v=JcovHg_RydE&t=310s).
  Inspect 5:30–5:50 for the incomplete set, flag, named map node and
  resumed control. The game names Wellspring Canyon on the map.
- Supplemental [Switch written route](https://gamefaqs.gamespot.com/switch/386399-pepper-grinder/faqs/81195/world-1)
  describes which first-stage coins require a detour. Its heading calls
  1-2 Wellspring Cannon, so use the captured map's Canyon spelling.

## Mechanical decomposition

### Action genes

- ACT-008: steer or jump the same runner through the visible route.
- ACT-829: keep the drill active and choose direction within the material.
- ACT-830: send the boost before leaving material to extend outward travel.
- ACT-341: address the finish mechanism with the drill in reach.

### System Behaviour genes

- SYS-037: credit contact-collected gems or coins without ending play.
- SYS-369: recover at the latest authored lit lantern following failure.

### Constraint genes

- CON-862: powered traversal is confined to eligible parts of the terrain.

### Information genes

- INF-119: inspect health and the drill indicator before committing.
- INF-179: read the view's accessible surfaces, hazards and exits.
- INF-317: use a placed control prompt when the relevant action is taught.

### Objective genes

- OBJ-283: clear the stage to open the next map route. Collecting all Skull
  Coins is independent of accepting that ordinary exit.

### Time genes

- TIM-003: choose a heading or boost while body motion and hazards advance.

## Reproducible transitions

| Before | Decision or event | After | Evidence |
| --- | --- | --- | --- |
| Runner on ordinary support | Approach the exposed soft material with the drill active | The same runner enters the soft patch in the current plane | PG-002 |
| Runner moving inside a soft pocket | Turn toward the exposed edge and boost before crossing it | A fast exit with an airborne leg toward the next landing | PG-003 |
| Soft region ends at solid rock | Choose another heading or use an exposed boundary | Fixed rock continues bounding the usable route | PG-002 |
| Runner contacts a pickup | Continue the route | The pickup is credited and play continues | PG-004 |
| Health depletes with a lantern already lit | Failure resolves | Earlier checkpoint and controllable retry | PG-005 |
| Runner reaches the final flag mechanism | Operate it with the drill | Stage clears and 1-2 becomes selectable, even with missed coins | PG-006, PG-007 |

## Strategic and experiential structure

The boost is not a second jump after entering the air. An early command
may accelerate the underground leg; useful reach is governed by the
remaining path and the exit heading. Fixed rock stays a boundary.
Using an optional cannon is a separate path choice, not the source of
every airborne crossing. The checkpoint is an authored fixture, not a
player-placed save point. The replay shows recovery after empty health
without exposing each transient object or save flag that gets reset.

## Replay and variation

The same ordered map stages accept different optional detours and
collection results. The first Switch trace recovers after health
depletion and later credits a full set on the map. The second trace
opens the same successor with empty slots. No difference in the
ordinary flag requirement follows from those different outcomes.

## Adjacent systems and history

The commercial booklet gives separate rules for water movement,
grappling and shop keys. The newly accessible stage begins at water
in both recordings. Its own traversal rules and keys for separate
map branches do not supply requirements for finishing Lost Claim.
The same publisher describes both Switch and PC releases. Only the
commercial Switch course is the research target.

## Normalised genome

| Type | Genes | Rationale |
| --- | --- | --- |
| Action | ACT-008, ACT-341, ACT-829, ACT-830 | Surface motion, flag operation, steerable drilling and timed boost |
| System Behaviour | SYS-037, SYS-369 | Collect on contact and retry after failure |
| Constraint | CON-862 | Material and active locomotion condition |
| Information | INF-119, INF-179, INF-317 | Resource HUD, route geometry and instructions |
| Objective | OBJ-283 | Ordinary flag clear, unlocked successor and independent set |
| Time | TIM-003 | Commit movement and boost in continuous time |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `621` (`GAME-0001`–`GAME-0621`).
- Exact genome matches: none.
- Tied near matches: `GAME-0394` — LittleBigPlanet 2 (`6 / 19 = 0.315789`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [LittleBigPlanet 2 (GAME-0394)](../g-l/littlebigplanet-2.md) | ACT-008, ACT-341, INF-179, SYS-037, SYS-369, TIM-003 | Both have live navigation, pickups, contextual activation and checkpoint recovery. LittleBigPlanet 2 uses a tether and explicit layer placement in its opening route. Lost Claim instead keeps the runner in one plane while drilling and turns underground heading and boost timing into exit reach. | Near, `0.315789` |

## Taxonomy impact

[TAXONOMY_CHANGE_368](../../../research/taxonomy-changes/TAXONOMY_CHANGE_368.md)
separates same-plane drill traversal, material eligibility and timed emergence.

## Negative results

- ACT-815 and CON-855 model leaving one state layer and appearing in
  another. The drill can run along a curved route inside visible terrain
  without leaving the current plane.
- ACT-820 and CON-859 choose a struck volume for removal. The sample
  distinguishes local drilling eligibility from persistent excavation.
- ACT-668 times a preset launcher. ACT-830 preserves an exit heading
  chosen while the runner is already moving through soft material.
- SYS-905 converts finish contact into attempt scoring and starts a
  linear successor. The drill-activated flag instead closes to a map,
  with optional coin credit that leaves ordinary access independent.
- Ordinary clear does not use SYS-085's exhaustive-collection gate.
  A gold-key route from the shop is outside the bounded main route.

## Delta summary

Admits one Switch stage from the earliest hands-on movement to its
flag settlement and an opened successor. The same-plane material
rules explain crossings distinct from ordinary platform jumps.

## New facts

- The player can steer a powered drill continuously inside soft ground.
- A boost before emerging can extend the airborne crossing.
- Wellspring Canyon opens even when the Lost Claim coin set is incomplete.

## New genes

ACT-829, ACT-830 and CON-862.

## New combinations

None. No verified combination is a subset of the bounded stage genome.

## Taxonomy changes

[TAXONOMY_CHANGE_368](../../../research/taxonomy-changes/TAXONOMY_CHANGE_368.md).

## New questions

Can a separate Wellspring Canyon record reproduce water entry, launch
angle and sustained skimming without importing Lost Claim's material boundary?

## Next recommended game

Continue with Blue Lightning on the original Atari Lynx card, a full
early flight sortie with a recorded completion outcome.

## Why this game

Lost Claim couples active material-dependent locomotion with a timed
exit impulse while keeping a conventional map-based clear and a separate
collection goal. It separates inhabiting a movement medium from changing
the scene into a durable newly open route.
