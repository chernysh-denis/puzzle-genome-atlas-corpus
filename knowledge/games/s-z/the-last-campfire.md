---
game_id: GAME-0729
slug: the-last-campfire
game_title: "The Last Campfire"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-341
  system:
    - SYS-061
    - SYS-065
    - SYS-2031
  constraint: []
  information: []
  objective:
    - OBJ-378
  time:
    - TIM-002
---

# Game: The Last Campfire — The Guiding Light

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Ember, the weight, the cage and the stairs are scoped instances.

## Analysis scope

- Version / ruleset: English PlayStation 4 commercial digital Standard
  game, US product `UP2034-CUSA19507_00-CAMPFIREHG000001`, released on
  August 27, 2020. Ordinary puzzle rules. Explore Mode offers a way to
  skip puzzles and is outside the trace. The exact installed patch and
  recording hardware are unverified.
- Structured target: `PLAT-PLAYSTATION-4`. Start at the first caged
  Forlorn on the Forest approach. Continue through The Guiding Light,
  accept the release interaction and stop when the route returns to
  the Forest. Lighting the first campfire and entering another Forlorn
  puzzle are beyond the boundary.
- Primary decision loop: transfer one weight between two floor
  posts to raise the linked sections, ride or align the moving
  staircase with its pull rings, lower a separate chain and use
  it after switching the weight to the other post.
- Included: walking and authored climbing, ordinary interaction,
  single-weight pressure support, moving stairs, the lowered chain,
  and the flame release that returns Ember to the Forest. Excluded:
  the preceding gold-figure door, the next Forest gate and campfire,
  other Forlorn, collectibles, skips, failure and save rules.
- Direct-play status: no personal console or emulator session. The US
  store and developer announcement establish the release context.
  Recorded play and first-hand guides corroborate the rule sequence.
  Video was inspected in silent background frames.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| LC-001 | The English PS4 Standard digital product was released August 27, 2020. The developer identifies a separate Explore Mode for skipping puzzles. | Observation | Corroborated | High | P1, P2 |
| LC-002 | Addressing the first cage along the Forest approach enters a separate playable stone puzzle titled The Guiding Light. | Observation | Corroborated | High | W1 07:04–07:24, W2 00:07–00:25, S1, S2 |
| LC-003 | The single free weight can be lifted and put down on either of two matching posts. In both observed transfers the unoccupied section drops and the newly weighted post holds its linked section raised. Ember can leave the occupied post without the supported section dropping. | Observation | Corroborated | High | W1 07:24–07:36 and 07:54–08:10, W2 00:25–00:37 and 00:56–01:08, S1, S2 |
| LC-004 | With left access raised, Ember climbs to pull the first ring. The stair assembly travels to the other side with Ember on it. From its lower ledge Ember addresses the stowed chain, which drops into reach of the lower floor. | Observation | Corroborated | High | W1 07:34–07:55, W2 00:34–00:56, S1, S2 |
| LC-005 | After the chain drops, the same weight can be moved back to the right post. The chain stays lowered, giving access to the raised right-hand approach. A second pull ring changes the staircase alignment and opens the final ascent. | Observation | Corroborated | High | W1 07:55–08:25, W2 00:55–01:25, S1, S2 |
| LC-006 | The player reaches and interacts with the caged flame at the top. The puzzle resolves and returns Ember to the Forest approach. The flame is free before the later campfire interaction. | Observation | Corroborated | High | W1 08:22–08:51 and 09:30–09:48, W2 01:22–01:44, S1, S2 |
| LC-007 | The traced puzzle allows untimed pauses between route operations. There is no visible countdown or timing grade. The moving geometry still has an animation before the next chosen traversal. | Observation | Corroborated | High | W1 07:24–08:37, W2 00:25–01:37, S2 |

## Basic data

- Release / origin: Hello Games developed and published the PS4
  commercial Standard digital release, listed for August 27, 2020.
- Mechanical families: `FAM-013` for transferring the compatible
  weight between posts that gate later access. `FAM-017` for the
  order in which the player must open and preserve the routes.
- Primary product and developer evidence, checked 2026-11-25:
  - **P1:** [US PlayStation Store product](https://store.playstation.com/en-us/product/UP2034-CUSA19507_00-CAMPFIREHG000001).
    Digital product identity, language, platform, date and player count.
  - **P2:** [Sean Murray’s PlayStation launch announcement](https://blog.playstation.com/2020/08/26/navigate-the-puzzling-world-of-the-last-campfire-out-tomorrow-on-ps4/).
    PS4 release date and the alternative Explore Mode.
- Recorded and first-hand sources:
  - **W1:** [Gamer ZoneXF’s attributed PS4 route](https://www.youtube.com/watch?v=MfR3cz9Busg&t=424s).
    Follows the Forest entry, both posts and the first rescue through
    the handoff. Attribution does not establish the capture hardware
    or installed patch.
  - **W2:** [Play BRES’s all-puzzles trace](https://www.youtube.com/watch?v=aIYNPU8pyuA).
    The first 104 seconds corroborate geometry and order. Capture
    platform and installed patch are unverified.
  - **S1:** [Just Adventure’s first-hand walkthrough](https://www.justadventure.com/walkthrough/the-last-campfire/#the-first-forlorn).
    The first Forlorn route identifies the sequence before the campfire.
  - **S2:** [Sonder’s player guide](https://steamcommunity.com/sharedfiles/filedetails/?id=2860659777&l=english).
    The Guiding Light describes independent chain deployment and
    the second ring. Earlier gold-figure steps belong to the prologue.
- Claim IDs: LC-001–LC-007. Reproduce the route from the first cage.
  Check the chain after the weight moves and the Forest after release.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: move Ember along floor, steps and admitted
  climbable geometry (LC-003–LC-005).
- Reuse `ACT-048`: lift, carry and place the free stone weight
  on the other post (LC-003).
- Reuse `ACT-341`: address the cage or a reachable authored
  actuator and commit the local operation (LC-002, LC-004–LC-006).

### System Behaviour Genes

- Reuse `SYS-061`: the weight holds the matching platform raised
  while it occupies the linked post (LC-003, LC-005).
- Reuse `SYS-065`: a ring actuates authored movement of the
  stair assembly, changing where it lands (LC-004, LC-005).
- New `SYS-2031`: the upper deployment extends a climb route
  from the lower floor and keeps it available after reweighting (LC-004, LC-005).

### Constraint Genes

No separately admitted constraint. Access conditions are already
described by pressure occupancy, the moving stair and chain states.

### Information Genes

No separately admitted information gene. Visible local geometry
communicates state as the camera follows Ember. This does not
establish simultaneous visibility of the entire puzzle.

### Objective Genes

- New `OBJ-378`: make the first captive accessible and release
  it inside its puzzle. The action settles it and returns Ember
  to the Forest at the point of entry (LC-002, LC-006).

### Time Genes

- Reuse `TIM-002`: choose discrete route operations at the player's
  pace and allow the current operation to settle (LC-007).

## Formal state and transitions

Track current scene, Ember location, weight position or carried
state, the two independently linked raised sections, stair alignment,
chain deployment and captive release. Repositioning the weight
changes the corresponding sections after their motion settles.
The chain flag is independent of the post occupancy. Releasing the
captive inside the puzzle sets the rescue flag and restores the
entry scene. The first campfire is a later interaction.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| First cage on the approach | Interact | Enter The Guiding Light and gain local traversal control | LC-002 |
| Weight on right post | Lift, carry left, place on left post | Left section rises, the right is no longer held up | LC-003 |
| Ember on the first upper stair | Pull the nearby ring | The stair assembly shifts to the opposite landing with Ember | LC-004 |
| Chain stowed at the upper ledge | Interact, then climb down | Chain hangs within reach from below | LC-004 |
| Chain deployed, weight on left | Move the weight back to the right, then climb | The right section rises and the same chain still admits ascent | LC-005 |
| Ember at the second ring | Pull it, then climb the aligned stairs | Ember reaches the caged blue flame | LC-005 |
| Flame within reach | Interact with the captive | Puzzle settles and the Forest approach returns with the flame freed | LC-006 |

## Strategic and experiential structure

Each post can support only its own side in the observed layout. Use
the first placement to reach the initial ring, then secure a route
back to the upper level before removing the weight. The newly lowered
chain makes the second placement useful. It allows both posts to
matter across the sequence without requiring a second weight.

## Replay and variation

Both traces corroborate the transfer, chain and staircase sequence.
They do not establish every possible movement, any reset exploit,
or alternate routes in Explore Mode.

## Adjacent systems and history

The prologue uses a gold figure in a separate sliding-piece puzzle.
The freed flame subsequently leads to the first campfire. Other
Forlorn have distinct objectives and fixtures. This genome stops
on returning to the approach.

## Normalised genome

- Action: ACT-008, ACT-048, ACT-341.
- System Behaviour: SYS-061, SYS-065, SYS-2031.
- Constraint: none.
- Information: none.
- Objective: OBJ-378.
- Time: TIM-002.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `728` (`GAME-0001`–`GAME-0728`).
- Exact genome matches: none.
- Tied near matches: `GAME-0683` — Last Window: The Secret of Cape West (`3 / 12 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Last Window: The Secret of Cape West (GAME-0683)](../g-l/last-window-the-secret-of-cape-west.md) | ACT-008, ACT-341, TIM-002 | Both allow self-paced movement and contextual interactions. Last Window opens its route through observation, investigation and authored conversations. The Guiding Light uses a transferable weight, a moving stair and a chain that remains usable after the weight moves. | Near, `0.250000`. |

## Taxonomy impact

A pressure-supported route returns when its supporting weight is
removed. The lowered chain records a separate persistent affordance,
verified after the transfer. The captive interaction ends the local
puzzle and restores its entry scene, with no separate extraction leg.

## Negative results

- There is only one demonstrated portable weight in the puzzle.
- Moving the weight reverses the linked support but does not retract the chain.
- The two rings move an authored stair assembly. They are not a free
  control of an arbitrary platform.
- The first campfire is not the terminal event for the local rescue.

## Delta summary

Record a two-post route puzzle with an independently deployed
climb, a moving stair and a rescue that restores the route.

## New facts

- One repeatedly reusable weight determines which local access is supported.
- The deployed chain can be climbed after the weight transfers.
- Freeing the flame returns to the point of entry before lighting the campfire.

## Principles and design implications

A durable route can turn a reversible fixture into a staged plan.
Place the durable access where it must be reached before the
temporary support is reassigned.

## Puzzle or game generation potential

Build a bounded route with one transferable weight, two support posts,
a two-end stair and a deployable lower connection. Check the state
after the weight moves, then test resolution through a distinct
captive-release interaction that returns to the entry scene.

## New genes

- SYS-2031
- OBJ-378

## New combinations

None. The full predecessor and combination scan found no admitted combination.

## Taxonomy changes

[Taxonomy Change 475](../../../research/taxonomy-changes/TAXONOMY_CHANGE_475.md).

## Next recommended game

The next selection opens after the five-minute stop window.

## Why this game

The first complete Forlorn puzzle combines familiar carrying and
pressure support with a climb that persists across reconfiguration.

## Review status

Reviewed 2026-11-25 for the English PlayStation 4 commercial digital
ordinary puzzle ruleset. The scope ends on return to the Forest
after the first captive release.
