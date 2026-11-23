---
game_id: GAME-0651
slug: the-plucky-squire
game_title: The Plucky Squire
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-049
    - ACT-864
  system:
    - SYS-036
    - SYS-220
    - SYS-1881
    - SYS-1882
  constraint:
    - CON-872
  information:
    - INF-603
  objective:
    - OBJ-026
  time: []
---

# Game: The Plucky Squire

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: native English commercial PlayStation 5 base game,
  released 17 September 2024. The two PS5-attributed captures are from
  September and October 2024. Exact application build IDs are unknown.
- Entry: ordinary Chapter 4, A Treacherous Trail, in Sonnet Swamps.
  Reach the illustrated spread whose central stone path is blocked by
  a huge bug. The two green portals and right-hand drained moat are
  available on this spread.
- Primary decision loop: take an editable word from a printed sentence,
  use an available portal and exterior movement to reach another part
  of the spread, then insert the word into a local sentence to change
  reachable terrain. Use the new access before reversing the water state.
- Exit: place TINY at the bug's sentence, observe the bug shrink and
  leave the path, then walk into the following illustrated swamp spread
  and resume free control by Martina before spending anything.
- Included: direct locomotion, single-object handling, portal transfer on
  the open spread, contextual word removal and placement, related text
  cues, the staged moat and lever, the rusty gate and the bug obstruction.
- Excluded: earlier key and exterior goblin encounters, optional advice
  and enlargement of the frog, purchases, the fish minigame and later
  spreads, page turning from outside, save persistence, alternate modes,
  later patches and non-PS5 releases. The chosen captures do not isolate
  differences between difficulty or accessibility presets.
- Suggested later scope: test cross-spread portable words when pages turn,
  and whether an unrecognised word can remain in the same socket.

## Direct-play status

No direct play was performed. The platform page and the developer's launch
material verify the commercial PS5 release. The official manual explains
visiting the real-world surface through portals. Arecky Gaming and Mixeli
attribute their different ordinary campaign captures to PS5. Both show
the flooded crossing, dry-floor access, changed bug and successor spread.
The creators' patch levels, physical inputs and PS5 application metadata
are not directly verified. Only the game frames and visible text were
inspected, in the background without audio.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PLUCK-001 | All Possible Futures' commercial English PS5 base game was released 17 September 2024. The scoped challenge is on a Chapter 4 Sonnet Swamps spread. | Confirmed | Corroborated | High | P1 and P2 verify the release; W1 14:20–14:38 and W2 1:23:10–1:23:50 show the selected entrance and printed obstruction. Build IDs remain unknown. |
| PLUCK-002 | Jot traverses the printed terrain on foot and can enter or exit at fixed green portals. Outside the illustrated terrain he can walk over the physical book surface and re-enter at the right portal, reaching the far bank of the drained moat. | Observation | Corroborated | High | P2, P3 pp. 9–10; W1 17:10–17:20 and 17:58–18:08. W2 1:32:15–1:32:40. No arbitrary transition through unmarked paper is observed. |
| PLUCK-003 | Designated movable words can be removed, carried visibly and set down. A word can cross both plane changes with Jot. A vacant part of the original sentence remains while its word is in transit. | Observation | Corroborated | High | P4; W1 17:26–18:12 shows loose DRAINED, the FULL source vacancy, exterior movement and delivered FULL. W2 1:32:25–1:32:39 corroborates the ready loose words and transfer. Exact carry capacity is untested. |
| PLUCK-004 | Seating FULL in the moat sentence raises water and the lily pads form a walkable link to the lever bank. Removing FULL does not drain the moat by itself. Seating DRAINED again restores the dry lower path. | Observation | Corroborated | High | W1 18:11–18:18, 18:23–18:35 and W2 1:32:36–1:32:51, 1:32:54–1:33:30. R1 matches the order. The temporary blank in the before/after frames is evidence for this socket only. |
| PLUCK-005 | The raised-water crossing makes the lever reachable. Its linked grate remains open when the moat is drained. Jot walks down to the now accessible words by the grate and lifts OPEN. | Observation | Corroborated | High | W1 18:17–18:22 at the lever, 18:34–18:45 on the drained floor. W2 1:32:44–1:32:50 and 1:33:30–1:33:52. R1 corroborates this order. |
| PLUCK-006 | Moving OPEN into the rusty gate's sentence changes the gate and makes the upper route to TINY reachable. TINY is lifted from the frog sentence. | Observation | Corroborated | High | W1 18:42–19:08 and 19:15–19:32; W2 1:33:45–1:34:20. In W1 the optional giant frog appears while swapping loose words; W2 shows the route without that side result. |
| PLUCK-007 | Inserting TINY into the bug's sentence shrinks the blocking bug, which scurries away. The companions respond, and Jot can cross and move on the newly shown swamp spread. | Observation | Corroborated | High | W1 19:43–19:50 and 20:33–20:48; W2 1:34:22–1:34:50 and 1:34:50–1:35:10. Crossing and movement precede the subsequent shop controls. |

## Basic data

- Analysis target: `PLAT-PLAYSTATION-5`, native English commercial PS5 base
  game, release-period Chapter 4 rules. Commercial concept 10007954.
- Developer: All Possible Futures. Publisher: Devolver Digital.
- Mechanical families: `FAM-014`, world topology and perspective, and
  `FAM-016`, rule and interface manipulation.
- Checked: 2026-11-22.
- P1: [Official PlayStation 5 product page](https://www.playstation.com/en-us/games/the-plucky-squire/).
  Platform, release date, supported English text and the two realms.
- P2: [PS5 launch announcement by co-creative director James Turner](https://blog.playstation.com/2024/08/15/plucky-squire-launches-on-ps5-september-17-as-part-of-playstation-plus-extra-and-premium/).
  Commercial PS5 launch timing and bounds of the storybook and exterior.
- P3: [Official English Adventurer's Guide](https://thepluckysquire.com/the-plucky-squire-manual-english.pdf).
  Puzzle and portal instructions and the distinction between the page and
  the physical world outside. The specific moat sequence is from recordings.
- P4: [Publisher's launch article](https://www.devolverdigital.com/propaganda/the-plucky-squire-leaps-into-our-dimension-today).
  Word substitution as a way to change the story, and 2D/3D transitions.
- W1: [Arecky Gaming, PS5 Chapter 4 walkthrough, 12 October 2024](https://www.youtube.com/watch?v=zVZCaYJ1eEk&t=1046s).
  Main continuous record from the bug and the moat to successor control.
- W2: [Mixeli, PS5 full-game recording, 18 September 2024](https://www.youtube.com/watch?v=zyLdNjRDVlg&t=5535s).
  Independent traversal and resolution of the same spread.
- R1: [Mahmud Munazil Rahman's Chapter 4 walkthrough](https://intoindiegames.com/walkthroughs/the-plucky-squire-walkthrough-chapter-4/).
  Independent route description. The audiovisual platform and exact
  timings are grounded in W1 and W2.

## Mechanical decomposition

### Action Genes

- ACT-008: guide Jot across the current printed terrain, physical surface,
  raised pads, dry lower path and opened successor route.
- ACT-048: take and set down loose word objects while changing which item
  is carried.
- ACT-049: operate the reachable lever after crossing on the raised pads.
- ACT-864: extract a marked word from its sentence or seat a carried word
  in another writable sentence position.

### System Behaviour Genes

- SYS-036: ordinary falling and geometry contact distinguish lower ground
  from the water-raised walkable supports.
- SYS-220: active portals transfer the avatar and held word between the
  book's represented terrain and the physical surface beyond it.
- SYS-1881: the resulting sentence applies its modifier to its local
  referent, with a scoped retained state while its word is absent.
- SYS-1882: water first creates access to the lever, then withdrawing it
  creates access to the lower route with the lever's gate change intact.

### Constraint Genes

- CON-872: cross planes only through the authored active portal positions
  of the exposed spread. Exterior navigation connects different marks.

### Information Genes

- INF-603: distinguish editable text, gaps, held words, local referents and
  contextual portal and word interactions on the current surface.

### Objective Genes

- OBJ-026: remove the obstruction and reach the onward spread under the
  player's own control.

### Time Genes

No decision deadline or timed platform cycle is admitted at this boundary.
The player can leave the word state in place while planning the next move.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| Huge bug blocks the main path and the moat is drained | Leave at the left spiral, walk outside to the right and re-enter | Jot reaches the opposite bank without first traversing the printed dry moat | PLUCK-002 |
| DRAINED is loose beside the moat sentence | Carry FULL from the ruins sentence through both portals and seat it by the moat | The source has a vacancy. The right moat fills and two pads rise to the height of their banks | PLUCK-003, PLUCK-004 |
| The flooded moat supports the crossing | Walk the pads and activate the lever on the inner bank | The linked grate opens while the lower approach remains submerged | PLUCK-004, PLUCK-005 |
| The grate is open and FULL is installed | Lift FULL, then reseat DRAINED | Water persists during the blank interval. Drainage exposes the lower approach and the grate stays open | PLUCK-004, PLUCK-005 |
| The lowered moat can be crossed on foot | Take OPEN by the grate and fit it to the left rusty gate's sentence | The rusty gate opens, allowing travel to the upper frog sentence and the movable TINY | PLUCK-005, PLUCK-006 |
| Huge bug still fills the central path | Replace HUGE with TINY and walk onward after the bug leaves | The crossing is clear. Jot is controllable in the succeeding swamp spread near Martina | PLUCK-007 |

## Strategic and experiential structure

The route has two different dependencies. The printed one is opened by
editing text, while the physical surface makes a second portal reachable
before the printed crossing exists. Raising the water is useful to reach
the lever, but the usable word is lower. The successful state is a dry
moat with the earlier lever result still set, so a prior step must be
reversed without reversing all its effects. The carried adjective is a
world object and therefore has a journey between its source and recipient.

## Replay and variation

The independent captures differ in time spent revisiting the portals and
moving loose words. The first shows the optional giant frog and its trophy.
The other moves TINY to the bug while leaving the frog's sentence vacant
and reaches the same following spread. Enlarging the frog and making a
purchase are outside the required route.

## Adjacent systems and history

The base game also has chapter and exterior sequences involving page
turning, detached illustrations, combat upgrades and small rule changes
later in the journey. No retention across a save or across reopening a
previous spread is inferred from this one observed successor transition.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-048, ACT-049, ACT-864 | Navigate, hold and release word objects, use the lever and change written text |
| System Behaviour | SYS-036, SYS-220, SYS-1881, SYS-1882 | Resolve local geometry, transfer carried state, apply a written modifier and retain switch effects through drainage |
| Constraint | CON-872 | Limit transitions to the exposed spread's authored portals |
| Information | INF-603 | Show locally editable text and crossing affordances |
| Objective | OBJ-026 | Make the blocked continuation traversable and reach its successor |
| Time | None | No separate decision deadline or cycle in the admitted puzzle |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `650` (`GAME-0001`–`GAME-0650`).
- Exact genome matches: none.
- Tied near matches: `GAME-0112` — Human: Fall Flat (`4 / 15 = 0.266667`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Human: Fall Flat (GAME-0112)](../g-l/human-fall-flat.md) | ACT-008, ACT-048, OBJ-026, SYS-036 | Both use a controlled body, carried rigid items and changing support to reach an otherwise inaccessible continuation. Human's local progression relies on physical manipulation and occupancy. The Squire carries words across the boundary of the illustrated surface and changes geometry by placing them in written sentences. | Near, `0.266667` |

## Taxonomy impact

ACT-060 places tokens in a structured answer. ACT-864 acquires and seats
physical words in an authored sentence, with portable world state between
slots. SYS-017 parses spatially assembled rules in Baba Is You. SYS-1881
updates the local referent of written story text at its fixed socket.
SYS-1882 requires retaining a switch result across the inverse water
transition. It is separate from maintaining occupancy over a pressure plate.
SYS-220 handles transfer of the actor and carried object. CON-872 specifies
its authored, co-located eligibility while the printed spread is exposed.

## Negative results

- Taking FULL out of its socket was insufficient to restore the dry floor.
  The observed restoration followed placing DRAINED back in that socket.
- The far-right grate and the left rusty gate are distinct. The first is
  linked to the lever and the second responds to its written modifier.
- Enlarging the frog is an optional result in one observed solve. The
  other recording opens the central route without it.
- No broad grammar, all-word inventory cap, canonical movement timing or
  save persistence is inferred from this run.

## Delta summary

Eleven scoped genes, with five additions and six reuses. The bounded
sequence ends under ordinary control in the next swamp spread.

## New facts

- A word from one fixed story sentence is movable across the physical
  surface outside the illustrated world, then usable inside another one.
- Water makes one route traversable and another route unavailable. A lever
  reached in the flooded state can make its inverse useful.
- Text can change the blocking animal's size, with an observable effect on
  the continuation available to the player.

## Principles and design implications

Use the illustrated layout to show where each edit will matter. Let the
exterior create a route that is useful before the corresponding internal
paths exist. If a reversible world change is required, leave a clear
persistent marker for anything the earlier state already unlocked.

## Puzzle or game generation potential

Design a spread with two fixed crossings and one moved word that a player
can bring between them. An elevated route gives access to a latched control.
Inverting the elevation should retain that control and expose a lower target
that can supply a new modifier for the way forward.

## New genes

- ACT-864
- SYS-1881
- SYS-1882
- CON-872
- INF-603

## New combinations

None. All 274 verified combination signatures were checked.

## Taxonomy changes

[TAXONOMY_CHANGE_397](../../../research/taxonomy-changes/TAXONOMY_CHANGE_397.md).

## New questions

Which syntax restrictions are checked before the word touches its slot?
Can a word left on the exterior move with a changed book spread? These
would test the distinction between positioning, compatibility and retention.

## Next recommended game

Mega Man Battle Network, original English North American Game Boy Advance
cartridge. Trace one complete opening battle from chip choice and live
execution through its result and the return to exploration.

## Why this game

A carried adjective is a world object at one moment and a terrain control
at the next. One witnessed puzzle closes both phases with visible successor
control.
