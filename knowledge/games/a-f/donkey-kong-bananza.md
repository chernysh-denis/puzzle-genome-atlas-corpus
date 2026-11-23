---
game_id: GAME-0619
slug: donkey-kong-bananza
game_title: Donkey Kong Bananza
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-820
    - ACT-821
  system:
    - SYS-735
    - SYS-863
    - SYS-1816
  constraint:
    - CON-859
  information:
    - INF-540
  objective:
    - OBJ-332
  time: []
---

# Game: Donkey Kong Bananza

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The positions, material types and named gem are instances.

## Analysis scope

- Version / ruleset: English single-player first visit to Ingot Isle in
  the commercial Nintendo Switch 2 base game released July 17, 2025. The
  post-release recordings show the released opening and its named results.
  The capture media and software update numbers are unverified.
- Primary decision loop: steer to the local face or floor that blocks
  progress, punch toward the solid volume and enter the connected opening.
  Read the newly visible cave, use the area hand slap when useful and
  excavate the stone that encloses the named Banandium Gem. Break the
  exposed gem and confirm its local acquisition.
- Entry: in the first Ingot Isle visit, after the conveyor-belt
  gem, start at the earthen floor where the prospector points the player
  toward more bananas. The route is on Sublayer 1.
- Exit: the collection event names Digging Up a Snack, the third
  gem on that initial visit; ordinary control resumes by the first
  checkpoint. Punching the checkpoint itself and following the further
  descent are successors. The checkpoint label can appear before the gem
  is claimed; neither label alone proves the other result.
- Included: the downward breach into Ancient Cave, local steering, directed
  material removal and physically accessible space, Hand Slap's contextual
  loose-item and sonar affordances, a concealed fixed gem, and its named
  acquisition. The scan is useful information; it does not remove rock or
  award the concealed gem. No assumption that every player needs it here.
- Excluded: the first and conveyor-belt gems, the detour to the subsequent
  collapse, Sublayer 10, bosses and combat, upgrades and their prices,
  timed Challenges, transformations, multiplayer or GameShare, amiibo,
  the later revisit, the demo and DK Island & Emerald Rush. The route
  establishes no universal resistance table or persistence across reloads.
- Suggested later scope: analyse one Shifty Smash challenge and its timer separately.

## Direct-play status

No direct play was performed. Nintendo identifies the commercial Switch 2
release and describes its mechanics. The post-release RetroArchive and CJR
Gaming captures show independent versions of the early route. BeardBear's
pre-release-dated capture is a corroboration of the named gem's local
sequence only. No source verifies the capture's save state, update number
or controller inputs frame by frame. Written sources and static sampled
frames were inspected without playing video or sound.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DKB-001 | Nintendo released the commercial Nintendo Switch 2 base game on July 17, 2025. The English initial Ingot Isle segment is distinguished from the later revisit and paid add-on. | Confirmed | Direct | High | [Nintendo product](https://www.nintendo.com/us/store/products/donkey-kong-bananza-switch-2/) and [first-visit gem list](https://www.mariowiki.com/List_of_Banandium_Gems_in_the_Ingot_Isle_Cave-In). |
| DKB-002 | A reachable loose floor seals the lower route. Downward punches clear actual traversable space and the character comes through to Ancient Cave. | Observation | Corroborated | High | [RetroArchive, 2:30–2:50](https://www.youtube.com/watch?v=JgnlA7_JEh0&t=150s) and [CJR Gaming, 41:30–42:10](https://www.youtube.com/watch?v=wgzR3sb2oik&t=2490s). |
| DKB-003 | The fixed third gem is inside stone beside the checkpoint. Removing enclosing rock gives direct access; the gem's own destruction credits it. | Observation | Corroborated | Medium | [First-visit gem list](https://www.mariowiki.com/List_of_Banandium_Gems_in_the_Ingot_Isle_Cave-In), [Nintendo on smashing gems](https://www.nintendo.com/en-gb/News/2025/October/Five-tips-to-fast-track-your-promotions-in-Donkey-Kong-Bananza-s-Emerald-Rush-DLC-2929569.html), and [RetroArchive, 3:10–3:30](https://www.youtube.com/watch?v=JgnlA7_JEh0&t=190s). Nintendo's page supports the smash-to-credit method; its add-on-specific systems are excluded. |
| DKB-004 | The hand slap operates around the character. Its ordinary use can gather loose items nearby and temporarily show silhouettes or positions of eligible buried targets. | Observation | Corroborated | High | [Nintendo move guide](https://www.nintendo.com/en-ca/whatsnew/learn-how-to-make-the-most-of-donkey-kongs-powerful-mitts/), [Ask the Developer, chapter 2](https://www.nintendo.com/en-gb/News/2025/July/Ask-the-Developer-Vol-19-Donkey-Kong-Bananza-Chapter-2-2871378.html), [RetroArchive, 3:00](https://www.youtube.com/watch?v=JgnlA7_JEh0&t=180s) and [CJR Gaming, 42:30](https://www.youtube.com/watch?v=wgzR3sb2oik&t=2550s). The traces do not require a successful scan of this gem before acquisition. |
| DKB-005 | RetroArchive shows the named Digging Up a Snack result at 3:30 and live control by 3:40. BeardBear shows the first checkpoint at 4:20, the same named reward at 4:30 and live control at 4:40. | Observation | Corroborated | High | Source [RetroArchive](https://www.youtube.com/watch?v=JgnlA7_JEh0&t=210s); corroborating [BeardBear](https://www.youtube.com/watch?v=AXgRMvAnixk&t=260s). The award is separate from a departure or final clear. |
| DKB-006 | Nintendo describes material-bearing voxels, local breakage, material-specific properties and stronger strikes reducing the work on tough materials. This explains geometry changes without implying that adjacent material vanishes or that all materials break to an ordinary punch. | Confirmed | Direct | High | [Ask the Developer, chapter 2](https://www.nintendo.com/en-gb/News/2025/July/Ask-the-Developer-Vol-19-Donkey-Kong-Bananza-Chapter-2-2871378.html) and [Nintendo move guide](https://www.nintendo.com/en-ca/whatsnew/learn-how-to-make-the-most-of-donkey-kongs-powerful-mitts/). |

## Basic data

- Title: Donkey Kong Bananza
- System: Nintendo Switch 2
- Analysis target: `PLAT-NINTENDO-SWITCH-2`, English commercial base game.
- Mechanical family: `FAM-014`, changing what space can be entered by removing local solid volume.
- Sources checked 21 November 2026.
- Release: Nintendo commercial base game, July 17, 2025
- Player arrangement: one directly controlled on-foot character in the scoped English opening
- Observed area: Ingot Isle, Sublayer 1; Ancient Cave and the first checkpoint approach
- Measured result: Digging Up a Snack acquisition and subsequent ordinary movement

## Mechanical decomposition

### Action Genes

- `ACT-008`: steer the character through the changed three-dimensional route and into reach of the gem stone.
- `ACT-820`: direct a punch into a reachable solid volume; a downward excavation is an explicit option before descending.
- `ACT-821`: issue one Hand Slap near loose pickups or buried points of interest. It is centred on the character rather than aimed into the desired tunnel.

### System Behaviour Genes

- `SYS-735`: disclose eligible nearby resource positions temporarily through the local pulse. The type cue or outline is evidence for choosing where to dig, not settlement.
- `SYS-863`: an admitted impact changes the mutable terrain at actual affected positions, altering the space through which the character can move.
- `SYS-1816`: the fixed embedded item is credited as a named collectible after access and breakage. An opened cavity, loose gold and the award are distinct states.

### Constraint Genes

- `CON-859`: the blow is local and the amount removed depends on its contact with the material. The body can enter only after connected clearance opens.

### Information Genes

- `INF-540`: the mine view exposes newly opened solids, routes and material cues locally; the whole hidden layer is unavailable. Hand Slap adds scoped information without turning the ordinary view into a full map.

### Objective Genes

- `OBJ-332`: complete the local excavation route and acquire the declared enclosed gem. This result does not require delivering it or leaving the layer.

### Time Genes

No independent time predicate is admitted. The segment accepts live
movement, but no countdown, forced progress or timing threshold for this
acquisition was established.

## Reproducible transitions

| State | Input or trigger | Result | Evidence |
| --- | --- | --- | --- |
| Opening floor after the belt | Approach the prospector and aim down into the low dirt area | A local opening can be made with repeated punches | DKB-002, RetroArchive 2:30–2:40; CJR Gaming 41:30–41:50 |
| Connected hole | Continue through the removed volume | Move into Ancient Cave below; the earlier floor no longer blocks that occupied space | DKB-002, RetroArchive 2:40–2:50; CJR Gaming 41:50–42:10 |
| Cave interior | Steer toward the checkpoint approach; use the area slap when useful | See the changed shape; the hand slap can gather nearby loose items or expose a temporary buried-target cue | DKB-003, DKB-004 |
| Local stone by the first checkpoint | Break local enclosing material and then the exposed gem | Named Digging Up a Snack award followed by continued movement | DKB-003, DKB-005 |
| Cue or checkpoint only | Leave the gem embedded or stop at the checkpoint | The signal or place label is insufficient evidence for the gem reward | DKB-004, DKB-005 |

## Strategic and experiential structure

The local choice is which material to remove and from which side. A
downward breach converts obstructing dirt into reachable cave space.
Inside the cave, a pulse gives information about where to excavate; the
player must still make space and act on the fixed gem. The surrounding
rock constrains the route and can remain behind the player. The named
result distinguishes this target from currency dispersed by other hits.

## Replay and variation

The traces take different amounts of time around the cave, and the
first checkpoint label is seen at different points relative to the target
approach. Both traces with visible settlement show the same gem name.
No minimal input count, scoop radius, retry state or save persistence
claim follows. Exact update numbers are unknown.

## Adjacent systems and history

Nintendo's developers distinguish the destructible material model from
how the voxel grid is presented to the player. This record uses those
properties to explain a shipped route; the earlier original-Switch
prototype is neither carrier nor play evidence. Consumption of later
Skill Points and the availability of specialized powers are outside
this first-visit route.

## Normalised genome

- Action: `ACT-008`, `ACT-820`, `ACT-821`.
- System behaviour: `SYS-735`, `SYS-863`, `SYS-1816`.
- Constraint: `CON-859`.
- Information: `INF-540`.
- Objective: `OBJ-332`.
- Time: none.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `618` (`GAME-0001`–`GAME-0618`).
- Exact genome matches: none.
- Tied near matches: `GAME-0313` — Tank 1990 (`2 / 23 = 0.086957`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Tank 1990 (GAME-0313)](../s-z/tank-1990.md) | ACT-008, SYS-863 | Both move a directly controlled body and alter the live level by removing mutable terrain. Tank 1990 fires projectiles to remove eligible cells, opening lines in a fight around a protected base. Donkey Kong Bananza directs local bodily strikes to excavate connected space and completes the route by breaking a fixed embedded gem. | Near, `0.086957` |

## Taxonomy impact

Five predicates are admitted on the route evidence. The strike defines the
local player choice, while the resistance and clearance constraint limits
it. A separate slap changes nearby information or loose inventory. Removing
rock makes space; the fixed gem has its own break-to-credit resolution.
The bounded objective joins the descent and that named acquisition.
Use existing direct navigation, simulated terrain removal, local survey
reveal and local mine-view definitions.

## Negative results

- `ACT-159` and `CON-206` address one terrain cell with a legal tool. They do
  not cover the selected directional removal from a continuous route.
- `ACT-443` requires direct transfer of contained yield during carving. This
  route opens space and settles the separate collectible.
- `ACT-815` switches layers at a surface coordinate and later resurfaces.
  Here the player opens a physical hole and enters it.
- `ACT-400` is a device-based resource pulse; the embodied hand slap also
  gathers loose items. Reuse `SYS-735` for its disclosure effect.
- `SYS-919` exposes a free carryable object after accepted digging, whereas
  the gem remains until its local break and is not carried to a receiver.
- `SYS-037` and `OBJ-025` require contact acquisition. The gem is broken and
  individually credited without establishing a mandatory later gate.
- No fixed save-reset consequence, timing threshold, transformation or item
  ratio is established by the first-visit traces.

## Delta summary

Admits the English initial Switch 2 excavation route through named gem
acquisition. Integrates the game into the world topology and perspective
family, with separate bilingual presentation and original route artwork.

## New facts

- Downward impacts into a formerly solid area permit the character to descend.
- The mine's ordinary view, local pulse, opened stone and acquisition display
  are four different kinds of evidence.
- Digging Up a Snack settles as an identifiable collectible on the first
  visit; movement resumes around the checkpoint without delivery.

## New genes

`ACT-820`, `ACT-821`, `CON-859`, `SYS-1816` and `OBJ-332`.

## New combinations

None. No general recipe was admitted.

## Taxonomy changes

[TAXONOMY_CHANGE_365](../../../research/taxonomy-changes/TAXONOMY_CHANGE_365.md).

## New questions

Could a timed Shifty Smash course demonstrate a separate completion
predicate involving a designated mutable set and resistant interleaving
material? That would require its own shipped-course trace.

## Next recommended game

`GAME-0620` Alien Soldier, Japanese Sega Mega Drive commercial cartridge.

## Why this game

The expansion roster contrasts spatial editing with a short, confirmed
boss confrontation where weapon stock and rapid movement interact.
