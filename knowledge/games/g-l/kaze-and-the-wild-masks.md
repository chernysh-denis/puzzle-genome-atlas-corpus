---
game_id: GAME-0720
slug: kaze-and-the-wild-masks
game_title: "Kaze and the Wild Masks"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-295
    - ACT-936
  system:
    - SYS-037
    - SYS-369
    - SYS-2014
    - SYS-2015
  constraint: []
  information:
    - INF-192
    - INF-652
  objective:
    - OBJ-283
  time:
    - TIM-003
---

# Game: Kaze and the Wild Masks — Bean Bay

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The mask, crystal colour, letter glyphs and button labels identify local rules.

## Analysis scope

- Version / ruleset: English Xbox One commercial digital base game,
  Microsoft Store product `9P7TK3GJVH57`, released on 26 March 2021.
  Use Original Mode. W1 is Xbox-labelled and shows Xbox control
  prompts, with the hardware model, build and selected mode unavailable.
  W2 explicitly selects Original Mode but does not identify its platform.
- Structured analysis target: `PLAT-XBOX-ONE`. Enter Bean Bay (1-7)
  from the first island's map. Follow its ordinary route, the fixed
  shark altar and transformed underwater movement. Touch the final
  purple portal, inspect Level Clear and return to the map.
- Primary decision loop: read approaching terrain and enemies, steer
  between the water and ledges, reach the shark altar, then steer the
  transformed swimmer under the rock ledges. Hold acceleration where
  the route permits it. Choose whether to divert toward crystals
  before taking the final portal.
- Included: direct movement, attacks, real-time encounter movement,
  nearby route visibility, contact collection, an early failure and
  entry reset, the fixed form change, held swim acceleration and
  ordinary clear with distinct collection credits.
- Excluded: other masks, completing bonus chambers, exact enemy
  damage and invulnerability, exact post-altar failure retention,
  Casual Mode, time trials, assisted skips, later levels, other ports
  and save persistence across application restart.
- Direct-play status: no personal Xbox session or input capture.
  Publisher and store pages establish the product and intended
  capability. Two independent recordings document the bounded route.
  Only silent storyboards and selected video-only frames were
  examined in the background.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| KZ-001 | PixelHive's completed base game launched digitally on 26 March 2021, including Xbox One. Original and Casual are separate choices; W2 selects Original. | Observation | Corroborated | High | P1, P2, S2; W2 00:08–00:17 |
| KZ-002 | Bean Bay starts with ordinary Kaze, who can already enter shallow water and swim. Contact with a hostile before the altar can end the attempt; W1 returns to the entry with zero red crystals. | Observation | Corroborated | High | W1 05:54–06:04; W2 21:40–22:40; S1 checkpoint notes |
| KZ-003 | Approaching the fixed shark altar triggers a mask change while preserving this stage attempt and its collection progress. The statue darkens and control resumes at the altar in the new form. | Observation | Corroborated | High | P1 shark ability, S1 mask altars; W1 06:59–07:07; W2 23:10–23:20 |
| KZ-004 | After the altar, the swimmer can steer below the submerged shelf. The route offers held acceleration through the jump control. The underwater spin is a separate attack that can propel the current direction. | Observation | Corroborated | High | S1 Shark; W1 07:07–07:23, including the A prompt at 07:18; W2 23:20–23:37 |
| KZ-005 | Camera lookahead shows local hazards, passable openings and optional crystal lines. Contact advances the red counter and letter credit separately while the route continues. | Observation | Corroborated | High | W1 05:56–05:59, 07:15–07:22 and 09:25–09:28; W2 23:20–23:39 |
| KZ-006 | The ordinary exit triggers Level Clear and return to the island map. W1 reaches it with an incomplete letter set; the bonus portal is a separate excursion. | Observation | Corroborated | High | S1 Portals and Results; W1 07:26–07:51 and 09:32–09:52; W2 26:20–26:41 |
| KZ-007 | A total of at least 100 red crystals in a clearing attempt credits the separate crystal award. Full letters and the bonus emerald category are separate. W1 has 104 red crystals during its last submerged section and settles the crystal award even with a missing letter. | Observation | Corroborated | High | S1 Collectables and Results, S2; W1 09:17–09:51; W2 26:26–26:41 |

## Basic data

- Release / origin: PixelHive Studio, published by SOEDESCO. The
  commercial English Xbox One digital base game is the target.
  SOEDESCO dates its digital launch to 26 March 2021 and separately
  names the later physical release.
- Platform or physical form: one player, Xbox One digital base product.
  Store compatibility also lists Xbox Series X|S. The shared listing
  and button glyphs cannot authenticate a particular console model.
- Mechanical family: `FAM-010`, real-time encounters and moving
  hazards constrain safe windows while the player steers.
- Primary sources accessed 2026-11-25:
  - **P1:** [Microsoft Store, product 9P7TK3GJVH57](https://www.xbox.com/en-us/games/store/Kaze-and-the-Wild-Masks/9P7TK3GJVH57).
    Product, devices, developer, publisher and the shark capability.
  - **P2:** [SOEDESCO digital launch announcement, 26 March 2021](https://www.soedesco.com/news/critically-acclaimed-kaze-and-the-wild-masks-jumps-from-a-childhood-dream-into-reality).
    The launch includes Xbox One and distinguishes physical timing.
- Secondary and recorded play evidence:
  - **S1:** [Independent mechanics guide, Steam Community](https://steamcommunity.com/sharedfiles/filedetails/?id=3247931091).
    Controls, shark acceleration and spin, mask altars, checkpoints,
    goal and bonus portals, and three result categories. Keyboard
    bindings from this guide are not treated as Xbox bindings.
  - **S2:** [XboxAchievements retail guide](https://www.xboxachievements.com/game/kaze-and-the-wild-masks/guide/).
    Corroborates difficulty differences and separate optional
    goals. Exact checkpoint and damage limits are outside the fixture.
  - **W1:** [The 8-Bit Arcade, Xbox-labelled launch-window recording](https://www.youtube.com/watch?v=5q6YzgfSSGo&t=354s).
    Bean Bay 05:54 onward. In bounded stills, note normal swim
    and entry reset by 06:03, altar at 06:59–07:07, underwater
    prompt at 07:18, incomplete letter set, portal and map by 09:52.
  - **W2:** [NeatPick, independent launch-window retail recording](https://www.youtube.com/watch?v=cRoDMSy-xKs&t=1292s).
    Original Mode selection at 00:08–00:17, Bean Bay from
    21:32 in the chapter listing, shark altar at 23:10–23:20,
    and portal, Level Clear and island map at 26:20–26:41.
- Claim IDs: `KZ-001`–`KZ-007`. Use the actual Xbox One product,
  record its installed version and Original Mode, then compare
  inputs and displacement before and after the altar. To test
  persistence beyond this fixture, record a post-altar loss and
  the first controllable frame after the retry.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: steer the same avatar across ground, gaps and
  water before and after the altar (`KZ-002`–`KZ-004`).
- Reuse `ACT-295`: execute the routed character's own spin attack.
  In the shark form the attack can also displace the swimmer
  (`KZ-004`).
- New `ACT-936`: hold the mapped acceleration input while steering
  the transformed swimmer below the surface (`KZ-004`).

### System Behaviour Genes

- Reuse `SYS-037`: physical contact acquires crystals and credited
  letters without stopping the ordinary route (`KZ-005`).
- Reuse `SYS-369`: the early failure reinstates the authored entry
  and its initial count. Later checkpoint retention is outside the
  demonstrated transition (`KZ-002`).
- New `SYS-2014`: approaching the fixed altar applies its assigned
  form. Ordinary control resumes with revised traversal commands
  inside the active stage (`KZ-003`, `KZ-004`).
- New `SYS-2015`: the crystal total qualifies a separate award at
  the ordinary clear. The stage can finish independently of its
  collection awards (`KZ-006`, `KZ-007`).

### Information Genes

- Reuse `INF-192`: the following side view exposes the nearby rock
  shelf, ledges, hostiles and surfaces (`KZ-005`).
- New `INF-652`: in-play crystal count and letter cues feed distinct
  collection results visible at the stage close and map
  (`KZ-005`–`KZ-007`).

### Objective Genes

- Reuse `OBJ-283`: take the ordinary designated exit and retain
  independently earned collection credits on the island map
  (`KZ-006`, `KZ-007`).

### Time Genes

- Reuse `TIM-003`: enemies and local threats keep moving during
  the player's steering and changes of depth (`KZ-002`, `KZ-005`).

## Formal state and transitions

Represent the live state as the current stage and attempt, screen
position and movement, resolved avatar form, authored altar state,
local threats, retry anchor and per-attempt collection state. Goal
settlement consumes the live route and exposes the earned credits
on the result and island map.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Bean Bay marked on the island map | Enter the ordinary stage | Ordinary Kaze appears on the first grassy platform | KZ-001, KZ-002 |
| Ordinary Kaze enters the first pool | Move toward the far pier and collide with the approaching bean pod in W1 | The first attempt ends; the entry restores with zero crystals | KZ-002 |
| Kaze reaches the shark statue on the shore | Approach the eligible altar | Mask animation finishes and control resumes in shark form in the same stage | KZ-003 |
| The transformed swimmer enters the water near the shelf | Steer below it and hold the displayed acceleration command | Faster directed swim is available without triggering a separate attack | KZ-004 |
| A red crystal or letter is on an optional line | Move through the pickup | The relevant collection credit advances while the route continues | KZ-005 |
| The shark swimmer emerges below the late pier, with an incomplete letter set | Reach the final purple portal | Level Clear displays separate earned categories and the island map returns | KZ-006, KZ-007 |

## Strategic and experiential structure

Steering around an enemy, taking an optional crystal detour and
accelerating below a stone shelf are different decisions. The
fixed form change introduces an acceleration input partway
through the same route. The exit accepts ordinary completion
even if the player bypasses a collection branch.

## Replay and variation

W1 reaches the finish with a missing letter. W2 demonstrates the
same altar and gate with a complete letter award. This establishes
a successful range of collection outcomes. Timed replay, exact
maximum collection and Casual Mode remain outside the fixture.

## Adjacent systems and history

The full game also distinguishes other mask mechanics, timed
bonus collection, late boss progression and leaderboards. The
fixture touches a bonus entrance only as evidence that it is
independent of the goal portal. It does not import its own
challenge rules into the main-stage signature.

## Normalised genome

- Action: ACT-008, ACT-295, ACT-936.
- System Behaviour: SYS-037, SYS-369, SYS-2014, SYS-2015.
- Constraint: none.
- Information: INF-192, INF-652.
- Objective: OBJ-283.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `719` (`GAME-0001`–`GAME-0719`).
- Exact genome matches: none.
- Tied near matches: `GAME-0622` — Pepper Grinder (`5 / 18 = 0.277778`); `GAME-0640` — Pizza Tower (`5 / 18 = 0.277778`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Pepper Grinder (GAME-0622)](../m-r/pepper-grinder.md) | ACT-008, OBJ-283, SYS-037, SYS-369, TIM-003 | Both navigate a live route, credit contact pickups, retry from an authored state and finish with separate optional progress. Pepper Grinder steers a drill through eligible material and chooses when to burst from it. Bean Bay grants a distinct form at a fixed altar and introduces held underwater acceleration. | Near, `0.277778`. |
| [Pizza Tower (GAME-0640)](../m-r/pizza-tower.md) | ACT-008, ACT-295, INF-192, SYS-037, TIM-003 | Both use direct side-view movement and attacks, local lookahead and contact pickups under live hazards. Pizza Tower builds speed and commits to a timed exit after its route fixture. Bean Bay changes the swimming controls and retains optional threshold credit at its ordinary portal. | Near, `0.277778`. |

## Taxonomy impact

Reuse authored retry and ordinary completion with optional
collection. Separate altar application, held swim acceleration,
the clear-time pickup threshold and exposed result categories.
Portal form replacement with a distinct collision envelope,
inventory equipment and time-limited underwater oxygen are
different state contracts.

## Negative results

- Base movement through the first pool is observable before the
  mask. The act of entering the water does not grant the mask.
- Collecting one letter or opening the timed bonus room does not
  satisfy the ordinary exit condition.
- The witness does not establish an executable version, an
  acceleration ratio or frame-perfect attack timing.
- No fixed release rule about save retention across application
  restart was inferred from the map return.

## Delta summary

Compare ordinary swimming to the new control under the submerged
shelf. Judge progress by the final portal, then inspect collection
credits separately.

## New facts

- The fixed shore altar applies the traversal form partway
  through Bean Bay with no observed counter reset.
- The Xbox prompt attaches held swim acceleration to A under
  the submerged shelf.
- Ordinary Level Clear allows missing letters and shows the
  eligible red crystal award separately.

## Principles and design implications

Teach changed movement beside the first practical use. Display
optional collection goals separately from route completion so a
player can decide which detours are worth taking.

## Puzzle or game generation potential

Create a small shore-and-water route with a fixed form-change
fixture, an acceleration teaching corridor and a reachable
normal exit. Check that bypassing a set item still permits the
clear and that the earned threshold has a distinct result.

## New genes

- ACT-936
- INF-652
- SYS-2014
- SYS-2015

## New combinations

None.

## Taxonomy changes

[Taxonomy Change 466](../../../research/taxonomy-changes/TAXONOMY_CHANGE_466.md).

## Next recommended game

Selection 062 ends at this unit. The next subject belongs to a
new mixed-era, mixed-platform selection.

## Why this game

This first-island route documents one local movement change and
one clear with visibly incomplete optional collection.

## Review status

Reviewed 2026-11-25 for the English Xbox One base game, scoped to
the Bean Bay ordinary route and its immediate result.
