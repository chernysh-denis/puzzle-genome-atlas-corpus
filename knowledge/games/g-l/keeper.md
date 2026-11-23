---
game_id: GAME-0543
slug: keeper
game_title: Keeper
analysis_status: reviewed
reviewed: 2026-11-18
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-726
    - ACT-741
  system:
    - SYS-066
    - SYS-407
    - SYS-1571
    - SYS-1572
  constraint: []
  information:
    - INF-372
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Keeper

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
This record analyses one complete main-route environment puzzle, not the
whole island or its later transformations.

## Analysis scope

- Version / ruleset: full English Xbox Series X|S release, launched
  17 October 2025. Default controller bindings establish the input names.
  The exact installed patch and executable were not inspected.
- Entry: arrive in Radiant Grove immediately after leaving Luminous
  Cavern on the ordinary story route. Focus Light is already available,
  and Twig is with the lighthouse. Begin before the intertwined trees.
- Primary decision loop: walk to a local obstruction, inspect the
  prompted interaction, choose Twig, a dash or focused light, and
  inspect the resulting passage. At the broken crossing, find the
  lower route, illuminate each of its two plants, then return uphill.
- Positive exit: walk across the completed root bridge and reach its
  far-side opening toward Mountain Shrine. Stop before the next cave's
  swarm and seed sequence. Bridge growth alone is not arrival.
- Included: direct walking through the grove and shallow lake, independent
  lamp aiming and focus, Twig's first targeted root operation and
  accompanying movement, dash-cleared small roots, the lower detour,
  two-part growth, local support and contextual control prompts.
- Excluded: opening balance lessons, acquiring Focus Light in Luminous
  Cavern, the optional left-hand overlook and Brim monument, achievement
  collection, subsequent Wither encounters, bird winding or item transport,
  time manipulation, body transformations, later chapters, other platforms,
  save/rewind semantics and unmeasured targeting or growth coefficients.
- Potential scoped modules: the later joint light-and-winding gate,
  the day-state shrine network, or transformed-body traversal.
- Direct-play status: no Xbox, executable, controller session or save was
  used. The creator's written interview, SpecialEffect's control audit,
  independent release walkthroughs and their still images were inspected.
  No audio or video was played. The transitions below are documentary
  reconstructions, not a newly executed success trace.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| KE-001 | Keeper is a full release for Xbox Series X and S from 17 October 2025. Its lighthouse and Twig have complementary world interactions. | Confirmed | Direct | High | P1, P2 |
| KE-002 | Left stick moves the lighthouse. Right stick independently aims its lamp; held RT focuses it. Moving recentres the lamp, and focus can acquire a nearby eligible target. | Observation | Corroborated | High | P2, P3 |
| KE-003 | At the first intertwined trees, X sends Twig to the target. The bird's operation separates the roots so the lighthouse can pass; the bird otherwise accompanies it. | Observation | Corroborated | High | P2, S1, S2, S3 |
| KE-004 | The main route crosses shallow water. A dash with A clears small obstructing roots at the next arch. Guides differ on press versus hold wording; exact minimum input duration was not measured. | Observation | Corroborated | High | P3, S1, S2, S3 |
| KE-005 | The upper crossing starts incomplete. Take the lower path and focus on its first eye-shaped plant to grow one bridge portion. Continue underneath to focus on the other plant and complete the span. | Observation | Corroborated | High | S1, S2, S3 |
| KE-006 | Return up the slope and traverse the completed upper bridge to its far-side opening. Each grown portion remains available for this local return and crossing. Global or save-file permanence is not established. | Observation | Corroborated | High | S1, S2, S3 |
| KE-007 | Contextual button prompts disclose eligible actions. Camera framing is largely authored. Twig movement and light-driven growth resolve over time while controls remain available, without an imposed local puzzle deadline. | Observation | Corroborated | High | P2, P3, S1, S2 |
| KE-008 | The control audit describes protected ledges and no health/life/progress loss. This packet does not establish a fall-damage system or a consumable light battery. | Observation | Limited | Medium | P3, S1, S2 |

## Basic data

- Double Fine Productions, published by Xbox Game Studios.
  Target: Xbox Series X|S, ordinary released story rules, default controls.
- Families: state transformation and world topology/perspective. The two
  plants change a disconnected crossing into usable support. Coordinating
  Twig and the lighthouse also fits agent routing and coordination.
- Sources accessed 2026-11-18:
  - **P1** — [Lee Petty's launch-day note](https://news.xbox.com/en-us/2025/10/17/keeper-launch-day-note-from-creator/),
    release identity and date, not a patch-level mechanics specification.
  - **P2** — [Official Xbox developer interview transcript](https://news.xbox.com/en-us/podcast/keeper-a-deep-dive-into-the-beauty-of-weird-but-chill-official-xbox-podcast/),
    unfocused/focused lamp distinction and Twig's complementary abilities.
    Its preview discussion is corroborated with released-game routes.
  - **P3** — [SpecialEffect's control inspection](https://gameaccess.info/keeper-controls/),
    controller inputs, assisted aim, authored view, prompts and access.
    Its later PS5 availability update is not evidence of platform parity.
  - **S1** — [Neoseeker's released Radiant Grove route](https://www.neoseeker.com/keeper/Chapter_6_to_10),
    first companion operation, roots, lower path and two-part crossing.
    The indexed article was readable; its origin denied a direct request.
  - **S2** — [Into Indie Games' illustrated route](https://intoindiegames.com/walkthroughs/keeper-walkthrough-chapters-1-to-17/),
    Radiant Grove images and steps from the first trees to the bridge.
    Its prose calls this the fourth chapter despite listing it sixth.
    This record identifies the location and entry instead of trusting that number.
  - **S3** — [GameSpew's released-game walkthrough](https://www.gamespew.com/2025/10/keeper-walkthrough/),
    independent support for the tree, dash and two-flower bridge sequence.
- Claim IDs: KE-001–KE-008.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for moving the lighthouse directly along the authored
  paths, into shallow water, under the crossing and back uphill.
  Its dash command is a movement parameter; the root-clearing response
  is a separate system behaviour.
- Reuse `ACT-726` for addressing the first eligible root fixture so
  Twig flies to it and operates it instead of steering the bird directly.
- Add `ACT-741` for independent lamp aim and held focus. `ACT-566`
  includes charge-priced hostile treatment, which this plant interaction lacks.
- Claim IDs: KE-002–KE-005.

### System Behaviour Genes

- Reuse `SYS-407` for the persistent companion accompanying the
  directly controlled lighthouse and reaching a work site.
- Reuse `SYS-066` for the contextual work mode inferred after
  dispatching Twig to the intertwined trees. This operation clears
  their passage without a player-driven winding stage in this packet.
- Add `SYS-1571` for light-responsive growth into linked support.
  The first half does not yet connect the upper banks. `SYS-1142`
  instead releases responsive cloth and excludes a bridge whose
  required component release remains incomplete.
- Add `SYS-1572` for clearing small authored roots by a body dash.
  `SYS-755` requires a damage threshold; no such hidden damage
  calculation is established here.
- Claim IDs: KE-003–KE-006.

### Constraint Genes

- No independent constraint gene is admitted. Authored collision and
  support are parameters of traversal and growth. `CON-011` requires
  exclusive occupancy and does not automatically follow from a guarded
  three-dimensional path. No health stock, light charge, imposed
  deadline or bridge-decay timer is inferred.
- Claim IDs: KE-004–KE-008.

### Information Genes

- Reuse `INF-372` for context-sensitive button prompts and target
  disclosure. Ambient flower responses also guide inspection, but
  are not a complete map or a numeric resource gauge.
- Claim IDs: KE-002, KE-003, KE-007.

### Objective Genes

- Reuse `OBJ-026`: make the far bank traversably connected and
  walk to its opening. This is a bounded task exit, not the game's ending.
- Claim IDs: KE-005, KE-006.

### Time Genes

- Reuse `TIM-003`: Twig's travel and growth animate and progress
  while input remains available. An untimed decision does not imply
  a discrete board that advances only after a completed move.
  No reaction deadline is required to cross the locally restored bridge.
- Claim IDs: KE-003–KE-007.

## Reproducible transitions

| Before | Input or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| The lighthouse has just entered the grove | Approach the intertwined trees and press the prompted X | Twig moves to the fixture and opens the passage | Companion work is distinct from lighthouse locomotion | KE-003 |
| The trees are separated | Follow the right main route through shallow water | Reach the arch with small roots | No swimming oxygen meter is established | KE-004 |
| Small roots still block the arch | Move into them using A dash | Clear the obstruction and continue uphill | A body action handles a different target from Twig's tree fixture | KE-004 |
| The upper bridge is incomplete | Inspect, then descend the right lower route | Reach the first eye-shaped plant below the crossing | The reachable work position differs from the eventual crossing level | KE-005 |
| Neither portion has grown | Aim and hold focused light on the first plant | Its linked root grows one portion | One successful interaction does not complete the whole crossing | KE-002, KE-005 |
| The first portion is grown | Walk below the crossing and focus on the other plant | The second portion completes continuous upper support | Both target states contribute to connectivity | KE-005, KE-006 |
| The upper support is continuous | Return up the slope and walk across to the far opening | Reach the packet's positive exit | Restoring the crossing and traversing it are separate steps | KE-006 |

## Strategic and experiential structure

The blocked upper route is a spatial question rather than a demand for a
longer jump. The lower path exposes the fixtures that change the upper
support. Twig, dash and focused light are not interchangeable verbs:
select the compatible action for each obstruction and inspect its result.
The first grown half supplies feedback without yet satisfying the task.

Lamp aim can be separated from movement. The player can reach a useful
position, stop, aim and focus instead of holding both sticks together.
Authored framing and prompts guide discovery. No numerical speed score,
combat reward or cost of waiting is added to the packet.

## Replay and variation

The main route and plant links are authored. Walking order, lamp angle
and the delay before recognising the lower route can vary. Exact focus
radius, activation duration, collision tolerances, reversing the plant
order and save/reload persistence were not reproduced. The documented
route establishes one valid order without asserting it is the only one.
The optional overlook is a separate branch, not a prerequisite for this exit.

## Adjacent systems and history

The Midnight Walk also sends a separate companion to fixtures while the
player remains elsewhere. Its burning resource, eye closure and enemy
behaviour are absent here. Journey turns responsive cloth into support;
Keeper's two addressed plants grow root sections whose joint connectivity
matters before the lighthouse returns to the upper path.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-008`, `ACT-726`, `ACT-741` | Body navigation, companion dispatch and independently focused lamp |
| System Behaviour | `SYS-066`, `SYS-407`, `SYS-1571`, `SYS-1572` | Companion following/work, linked growth and dash-cleared roots |
| Constraint | none | Traversal support and eligibility remain within the admitted operations |
| Information | `INF-372` | Live contextual input and target disclosure |
| Objective | `OBJ-026` | Arrive beyond the restored crossing |
| Time | `TIM-003` | Continuous local action resolution without a required deadline |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `542` (`GAME-0001`–`GAME-0542`).
- Exact genome matches: none.
- Tied near matches: `GAME-0098` — Hyperbolica (`3 / 14 = 0.214286`).
- Supported combination subsets: none.
- Scan date: 2026-11-18.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0098` — Hyperbolica | `ACT-008`, `OBJ-026`, `TIM-003` | Both navigate a directly controlled body to a world destination on a live local clock. Hyperbolica makes navigation depend on non-Euclidean space and transport. Keeper changes ordinary support through addressed light and companion work before returning to the crossing. | Near, `0.214286` |

### Preserved research notes

- New genes: `ACT-741`, `SYS-1571`, `SYS-1572`.
- Classification result: New gene.
- Evidence and reasoning: concentrated aim grows linked support, and a
  body dash clears eligible roots without asserting combat damage.

## Taxonomy impact

- Registry changes: three new Active definitions.
- Taxonomy-change record: [TAXONOMY_CHANGE_290](../../../research/taxonomy-changes/TAXONOMY_CHANGE_290.md).
- Candidate terms affected: none.

## Negative results

- none.

## Delta summary

## New facts

- [Observation | Corroborated | High] Two lower plants complete an
  upper crossing whose restoration precedes actual traversal. KE-005, KE-006.

## New genes

- [Observation | Corroborated | High] Three additions separate aimed
  focus, linked plant growth and body-dash root clearance.

## New combinations

- [Observation | Corroborated | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_290`.

## New questions

- Does reversing the two plant operations produce the same stable crossing?
- How long and precisely must the lamp focus for each plant to activate?

## Next recommended game

- [Hypothesis | Limited | Medium] Original Dreamcast Space Channel 5 in
  [Selection 043](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_043.md).
- Optimisation criterion: move from environmental support to rhythmic imitation.
- Expected information gain: ordered responses and timing feedback.
- Backlog impact: advance to `GAME-0544`.

## Why this game

- [Hypothesis | Limited | Medium] Ordered imitation should expose a
  distinct input schedule after an untimed environmental route.
