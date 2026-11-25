---
game_id: GAME-0725
slug: crypt-custodian
game_title: "Crypt Custodian"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-341
  system:
    - SYS-398
    - SYS-755
    - SYS-2028
    - SYS-2029
  constraint: []
  information:
    - INF-656
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Crypt Custodian — broom route and the Palace exit

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The broom, statue, dialogue page and gate are scoped instances.

## Analysis scope

- Version / ruleset: English Xbox Series X|S commercial digital base
  game, published by Top Hat Studios on 27 August 2024. Use a fresh
  Normal opening and the standard Xbox inputs where stated by the
  game. W1 is Series X-attributed and W2 is Series S-attributed.
  Neither identifies its exact installed revision.
- Structured analysis target: `PLAT-XBOX-SERIES`. Begin at first
  ordinary control in the Palace approach after meeting Pip. Inspect
  the route and its obstructing props, detour for the broom and use
  it on the traversable return. Reach Kendra and follow her revised
  admission to the left exit. Stop on first entry to Weeping Wastes,
  before its exterior encounters and shrine.
- Primary decision loop: move and jump between safe surfaces. Read
  which route props can be hit and which gaps require a different
  approach, then take the broom to the obstructed return. Clear
  the ordinary entrance, approach Kendra and take the exit she enables.
- Included: ordinary movement and jumps, one nonterminal missed gap,
  broom pickup and swing, removal of eligible obstacles, the
  standard review scene and crossing the opened outside exit.
- Excluded: proving a globally mandatory statue, exact fall and hit
  arithmetic beyond the observed health change, zero-health retry,
  alternate intro skips, combat after the boundary, special attacks,
  upgrades, map options, the first shrine and later access changes.
- Direct-play status: no personal console, cloud or emulator session.
  The Xbox release evidence identifies the product. A Series X
  opening, a Series S gate outcome and an independent corroborating
  opening support the route. Background frames were inspected
  without sound. Hardware and recorded inputs were unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| CC-001 | Kyle Thompson's base game launched commercially on Xbox Series X and Series S on 27 August 2024 under Top Hat Studios. The new-file English witness shows Normal in the gameplay options. | Observation | Corroborated | High | P1, P2, W1 12:00–12:06 |
| CC-002 | Ordinary movement and jumps cross the Palace platforms. One failed jump toward the island with the large statue returns Pluto to the near lip, down from four to three displayed health units, with control available in the same scene. | Observation | Corroborated | High | P2, W1 11:41–11:55 and 12:10–12:42, W3 02:18–03:02 |
| CC-003 | A marked statue blocks the ordinary approach. The detour brings Pluto to a loose broom. The acquisition panel names it and shows the command for a swing. | Observation | Corroborated | High | S1, W1 14:07–14:27, W3 03:36–03:58 |
| CC-004 | The broom can remove eligible statues on the return. The body no longer blocks traversal. From the opening paths Pluto reaches the Palace hall while keeping the broom. This is the ordinary witnessed route. | Observation | Corroborated | High | P2, S1, W1 14:28–14:42, 15:38–16:13 and 20:53–21:35, W3 04:22–06:30 |
| CC-005 | In the ordinary audience Kendra initially indicates Palace admission, then reads a newly presented page depicting the recent statue destruction and withdraws that decision. | Observation | Corroborated | High | P2, S1, W1 24:08–25:32, W2 00:03–00:31, W3 07:44–08:49 |
| CC-006 | Kendra opens the left exit from the hall and assigns the outside cleanup. Pluto retains the broom and crosses into Weeping Wastes under player control. | Observation | Corroborated | High | P2, S1, W1 26:12–27:13, W2 00:29–00:48 |
| CC-007 | An attributed player account reports a jump-and-slam bypass on a different execution and says an alternate reason for the same banishment can appear. The claim does not establish parity with the scoped Xbox build or another destination. | Observation | Limited | Low | S2, outside the admitted route |

## Basic data

- Release / origin: Xbox Store product `9PLG24BMTP3T`, developed
  by Kyle Thompson and published by Top Hat Studios. The dated
  publisher article separates the Xbox launch from the other
  platform evidence. The release scope does not assert purchase
  or an installed launch executable.
- Platform or physical form: Xbox Series X|S digital solo action
  adventure. W1 starts through the Xbox dashboard, and W2 is an
  Xbox Series S-attributed partial record of the same narrative gate.
- Mechanical families: `FAM-013` for the compatible tool and
  obstruction and `FAM-017` for tool acquisition, cleared
  approach, audience and enabled exit in order.
- Primary sources accessed 2026-11-25:
  - **P1:** [Xbox Store product page](https://www.xbox.com/en-us/games/store/crypt-custodian/9plg24bmtp3t),
    Xbox Series X|S support, original product, developer, publisher and date.
  - **P2:** [Top Hat Studios on Xbox Wire](https://news.xbox.com/en-us/2024/08/21/clean-up-the-afterlife-in-crypt-custodian/),
    Xbox launch, broom, movement, Kendra's judgment and outside route.
- Independent written and recorded sources:
  - **S1:** [Erik Lunde's opening account](https://somanygames.co.uk/articles/crypt-custodian-opening/),
    explicitly traces visible cracked props, the detour, broom,
    breached approach and the left exit.
  - **S2:** [Steam player reports of an opening bypass](https://steamcommunity.com/app/2394650/discussions/0/595156583817860390/),
    qualify the broader necessity claim. The reported route and exact
    version were unverified and are excluded from the signature.
  - **W1:** [CodyJay19, Xbox Series X Day 1](https://www.youtube.com/watch?v=Fxapfg3iLYw).
    Menu and Xbox attribution, early crossing, fall at about 11:50,
    broom at 14:20, successive removal and hall entry, ordinary
    verdict and the outside-area title.
  - **W2:** [Series S gameplay excerpt](https://www.youtube.com/watch?v=BftJcNWlO2Q).
    Starts mid-audience. The newly added page, change of outcome,
    left exit and area title are visible. It does not show the acquisition.
  - **W3:** [Normal Gameplay opening run](https://www.youtube.com/watch?v=KPdiikq2vKw).
    The first approach, broom and ordinary audience are shown.
    The captured platform and exact build are unverified. Used
    only to corroborate shared visible mechanics.
- Claim IDs: CC-001–CC-007. Reproduce the ordinary approach,
  then check the acquired action, the earlier route prop's solid
  body, the page, the enabled exit and the new-area title separately.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: move and jump over local Palace surfaces
  (`CC-002`, `CC-004`).
- Reuse `ACT-161`: face an eligible object in range and strike
  it with the broom (`CC-003`, `CC-004`).
- Reuse `ACT-341`: interact with the local source of the broom
  and address the gatekeeper in her hall (`CC-003`, `CC-005`).

### System Behaviour Genes

- Reuse `SYS-398`: broom access stays with Pluto through the
  return route and the next area (`CC-003`–`CC-006`).
- Reuse `SYS-755`: eligible props break and stop obstructing
  the route after the tool's damage (`CC-004`).
- New `SYS-2028`: a missed ordinary gap returns the character
  to its near ledge at an observed health cost (`CC-002`).
- New `SYS-2029`: the new action record reverses announced
  admission and enables the other exit on this ordinary route
  (`CC-005`, `CC-006`).

### Constraint Genes

No separate constraint. Relevant reach, eligible props and
return-position behaviour are covered by the recorded actions and systems.

### Information Genes

- New `INF-656`: cracked scenery discloses a currently unserved
  affordance. The later acquisition cue identifies the compatible
  tool and its swing input (`CC-003`, `CC-004`).

### Objective Genes

- Reuse `OBJ-026`: reach the Palace hall and then the new area
  through the opened exit (`CC-004`–`CC-006`).

### Time Genes

- Reuse `TIM-003`: crossing, the fall and the swing resolve in
  live time under player control (`CC-002`, `CC-004`).

## Formal state and transitions

The state distinguishes position and current surface, visible health,
broom availability, eligible solid props, recorded recent action in
the witnessed ordinary route, dialogue stage and opened exit. The
same continuing character can return to an obstacle after acquisition.
The audience resolves a route instruction while preserving movement
capabilities. The actual transition requires crossing the opened door.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Pluto is on the near ledge by the large statue | Fail to reach the next supported surface | Flash and local return, with one fewer visible health unit | CC-002 |
| The blocked ordinary approach is visible | Traverse the available detour to the broom | The acquisition prompt unlocks the swing | CC-003 |
| A cracked obstruction remains solid | Swing the broom in reach of the prop | The broken prop stops blocking the ordinary return | CC-004 |
| Kendra has announced admission | Advance until the new page enters her review | The ordinary verdict changes and the other exit is enabled | CC-005, CC-006 |
| The left exit is open and Pluto has control | Walk through the exit | Weeping Wastes becomes the current area | CC-006 |

## Strategic and experiential structure

Inspect the narrow approaches before jumping and keep the
ledge under the expected landing point. Identify breakable
obstructions and return with a compatible tool. The changed
verdict gives the same acquisition a different role as a
cleaning tool for the outside route.

## Replay and variation

A referenced community account suggests a different route to
the audience can change the reason stated in dialogue. The
observed standard route, retained broom and terminal area stand
independently of that unverified account. No hidden statue count
or accessible alternate region is claimed.

## Adjacent systems and history

Exterior combat, special attacks, upgrades and sanctuary
mechanics continue after the first area title. The opening is
bounded before those systems become decision-relevant.

## Normalised genome

- Action: ACT-008, ACT-161, ACT-341.
- System Behaviour: SYS-398, SYS-755, SYS-2028, SYS-2029.
- Constraint: none.
- Information: INF-656.
- Objective: OBJ-026.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `724` (`GAME-0001`–`GAME-0724`).
- Exact genome matches: none.
- Tied near matches: `GAME-0615` — Skate Story (`5 / 14 = 0.357143`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Skate Story (GAME-0615)](../s-z/skate-story.md) | ACT-008, ACT-341, OBJ-026, SYS-398, TIM-003 | Both move in live time and take a retained capability from an authored source to reach a later location. Skate Story learns an Ollie and must land jumps at specific crests to open its portal. Crypt Custodian clears eligible solid props with the broom and separately follows Kendra's revised instruction through the outside door. | Near, `0.357143`. |

## Taxonomy impact

The broom action reuses direct striking and scoped destructible
props. The failed gap is an observed local recovery rather than
a lethal checkpoint. The scene's reviewed recent action and
revised admission are distinct from opening a door with the tool.

## Negative results

- The unsuccessful jump did not reset the Palace approach.
- The broom was not consumed when removing the statue or leaving.
- The walkthroughs do not establish a global minimum number
  of destroyed props.
- The outsider route is the witnessed outcome. A variant
  dialogue is not evidence of a different open region.

## Delta summary

Record an opening whose tool-free route becomes traversable
after acquisition, and a later review that acknowledges the
same action before redirecting the next destination.

## New facts

- One witnessed miss produces nearby recovery at a health cost.
- A retained broom strike can clear a solid route prop.
- The left gate opens after Kendra reviews an added page.

## Principles and design implications

Place a readable obstacle before its tool so a later acquisition
has an immediate use. Separate the physical result of the tool
from a later route or narrative consequence of using it.

## Puzzle or game generation potential

Provide a small network with a route prop, a readable damage
mark and a detour with the tool. Trace the enabled return
and one gated exit. Test local fall recovery separately from
opening the exit and from later combat.

## New genes

- SYS-2028
- SYS-2029
- INF-656

## New combinations

None. No verified combination matched the ordinary opening.

## Taxonomy changes

[Taxonomy Change 471](../../../research/taxonomy-changes/TAXONOMY_CHANGE_471.md).

## Next recommended game

Soul Bubbles on Nintendo DS is the next Selection 063 unit.

## Why this game

One acquired capability clears the first physical obstruction
and remains available after an authored change in the route.

## Review status

Reviewed 2026-11-25 for the English commercial Xbox Series X|S base game.
The ordinary Palace route is bounded by the first Weeping Wastes entry.
