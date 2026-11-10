---
game_id: GAME-0479
slug: pitfall
game_title: Pitfall!
analysis_status: reviewed
reviewed: 2026-10-02
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-633
  system:
    - SYS-037
    - SYS-045
    - SYS-911
    - SYS-1244
    - SYS-1245
    - SYS-1246
    - SYS-1247
  constraint:
    - CON-743
  information:
    - INF-192
    - INF-453
  objective:
    - OBJ-002
  time:
    - TIM-003
---

# Game: Pitfall! — original Atari 2600 score adventure

Use the [canonical genome vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Treasure values, screen count and twenty minutes are parameters, not individually named genes.

## Analysis scope

- Version / ruleset: original English-language 1982 Activision *Pitfall!* for Atari 2600, as documented by original booklet AX-018-03. Exact cartridge revision and PAL/NTSC timing were not inspected. Atari 5200 controls, later ports, remakes and *Pitfall II* are excluded.
- Structured analysis target: original Atari 2600 cartridge (`PLAT-ATARI-2600`); see [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: run, jump or climb through the currently visible jungle scene; choose surface travel or a reachable underground shortcut; time a vine catch/release or crocodile crossing against autonomous motion; touch reachable treasure and compare score gains with recoverable penalties, remaining time and finite lives. Repeat through the circular world rather than clearing independently reset stages.
- Entry: reset a one-player adventure and move the left joystick to start action, with 2,000 points, twenty minutes and three lives. Difficulty and game-select switches do not choose other rules in this original version.
- Exit: the same adventure ends when the twenty-minute clock expires or Harry is lost for the third time. Collecting all 32 treasures is a score objective, not an asserted separate automatic terminal; no such ending was directly verified.
- Included: bidirectional running, jumping and ladders; authored surface/tunnel connections; automatic right-to-left logs; vine catch, passive carriage and downward release; cyclic crocodile jaws; contact treasure scoring; recoverable ordinary-hole/log penalties; lethal hazards, limited replacement lives, current-screen information and terminal score evaluation. These form one coupled score adventure rather than an arbitrary first-room packet.
- Excluded: exact room indices or all-room geometry, collision boxes, jump coefficients, vine period, crocodile timing, moving-pit phase algorithm, pause controls of other ports, extra lives, attack or enemy-stomp kills, persistence after Reset, original source-code execution and any exact route record. The booklet's diagram is explicitly a **Composite Screen**, not proof that every pictured element coexists in one playable scene.
- Reproducible parameterisation: on a version-pinned original cartridge, reset and begin; record one ordinary-hole fall, a rolling-log contact, a reached treasure, a surface edge and corresponding tunnel edge, a vine catch/release, a jaw-phase crossing and recoverable lethal contact; finish at third loss or clock expiry. Exact trajectories, contact durations and run score need a future direct trace. This record supplies source-based conditional transitions, not a fabricated play log.
- Direct-play status: no cartridge, executable, emulator, save, input trace, gameplay video or audio was inspected; no direct play was conducted. The original booklet's text and scanned diagrams were inspected, with a developer interview and later publisher retrospective kept separate. The artwork is original interpretive art, not a screenshot.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PIT-001` | Original Atari 2600 movement uses left/right running, button-assisted jumping, up/down ladders and a downward vine release; switches do not select difficulty. | Confirmed | Direct | High | P1 |
| `PIT-002` | Touching one of 32 treasures adds its class value to a starting 2,000 score; an ordinary hole deducts 100 and a log deducts according to contact duration. | Confirmed | Direct | High | P1 |
| `PIT-003` | Catastrophic hazards spend a life, not points; a replacement appears at the screen's left while another life remains. Third loss or twenty-minute expiry ends the adventure. | Confirmed | Corroborated | High | P1, P2 |
| `PIT-004` | The original booklet describes 255 circular scenes; each tunnel scene traversed covers the equivalent of three surface scenes. | Confirmed | Corroborated | High | P1, P3 |
| `PIT-005` | Catching the already swinging vine carries Harry across a pit until the player releases; the booklet does not license steering, reeling or glide. | Confirmed | Direct | High | P1 |
| `PIT-006` | Crocodile jaw phase changes crossing safety; the creator advises landing on a closed-jaw head and timing the next jump. Landing does not kill that crocodile. | Confirmed | Direct | High | P1 |
| `PIT-007` | Score, remaining time and replacement-life marks are exposed with the local side-view scene; distant surface scenes are not all visible. | Observation | Direct | High | P1 diagram, P2 |

## Basic data

- Release / origin: David Crane's original 1982 Activision Atari 2600 jungle adventure. No precise release day is needed by the mechanical analysis.
- Platform or physical form: one cartridge, one left joystick and its red button, original Atari 2600 rules.
- Mechanical families: route and network construction (`FAM-005`) for composing a treasure itinerary through unequal surface/tunnel strides; geometry and collision (`FAM-007`) for support and crossings; real-time system pressure (`FAM-010`) for moving hazards and the running clock.
- **P1:** [original Activision AX-018-03 booklet scan](https://atarionline.org/wp-content/uploads/2024/03/Pitfall-atari-2600-manual_compressed.pdf), copyright 1982, accessed 2026-10-02; PDF leaves 2–5 visually inspected for controls, score, clock, lives, circular route, vine and crocodile advice. [AtariAge transcription of the same booklet](https://atariage.com/manual_html_page.php?SoftwareLabelID=360) supports text reading but is not independent corroboration.
- **P2:** [Activision retrospective by David Hodgson](https://blog.activision.com/activision/2019-04/RetroVision-Feature-Part-1-Happy-37th-Birthday-Pitfall-Harry), 23 April 2019, accessed 2026-10-02; original platform, live twenty minutes, three lives, screen-edge transitions and vine. Its 256-screen wording conflicts with the original booklet and is not transferred into this scope.
- **P3:** [David Crane, The Replay Interviews](https://www.gamedeveloper.com/design/the-replay-interviews-david-crane), interview conducted 8 July 2009, accessed 2026-10-02; creator account of the 255-screen algorithm and running/jumping/climbing prototype. This is an interview, not inspected source code or a watched postmortem video.
- Claim IDs: `PIT-001`–`PIT-007`.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for directly commanded running, jumping and ladder movement. These are movement parameters, not separate colour- or joystick-specific genes (`PIT-001`).
- New `ACT-633`: catch a reachable moving vine by a jump and deliberately release downward. The original has no evidenced adjustable tether or glide, so `ACT-479` does not transfer (`PIT-005`).

### System Behaviour Genes

- Reuse `SYS-037` for treasure contact credit and `SYS-045` for autonomous moving hazard actors, specifically the booklet's right-to-left logs. This does not assert an uninspected scorpion patrol algorithm (`PIT-002`).
- Reuse `SYS-911` for lethal-body replacement while finite lives remain, with the left screen edge as return parameter. No health bar, base protection or Continue is implied (`PIT-003`).
- New `SYS-1244` for circular scene succession with unequal surface and tunnel strides; choosing a ladder affects which surface opportunities the shortcut bypasses (`PIT-004`).
- New `SYS-1245` for nonlethal score subtraction from ordinary holes and duration-sensitive log contact. Lethal traps belong to the life transition instead (`PIT-002`, `PIT-003`).
- New `SYS-1246` for jaw-phase-dependent hazardous support: the crocodile remains in the scene while its mouth cycles. This is not enemy removal by a stomp (`PIT-006`).
- New `SYS-1247` for passive carriage of an attached body by the existing vine swing until release. Catch/release input and autonomous carriage have different transition ownership. No force integration, radius adjustment or inherited release velocity is claimed (`PIT-005`).

### Constraint Genes

- New `CON-743`: a finite score adventure ends at either clock expiry or exhausted loss allowance. Twenty minutes settles the score attempt; it is not automatically a failed goal, nor a Tour session preserving separate campaign tasks (`PIT-003`).

### Information Genes

- Reuse `INF-192`'s bounded side-view lookahead, with scene replacement at the screen edge rather than continuous camera scrolling. Current supports, pits and nearby hazards are visible; the full circular world is not (`PIT-007`).
- New `INF-453` for score, time remaining and replacement-life marks. The original diagram has no separate coin inventory, stage number or combat-capability meter, so `INF-347` is too broad (`PIT-007`).

### Objective Genes

- Reuse `OBJ-002`: maximise score through valued treasure while avoiding point loss. Eight treasures in each of four classes give 112,000 obtainable points; with the initial 2,000, a penalty-free complete collection reaches 114,000. This ceiling is a parameter, not a new objective type (`PIT-002`).

### Time Genes

- Reuse `TIM-003`: the adventure clock and autonomous obstacles continue while the player acts or waits after the initial joystick movement. Exact PAL/NTSC conversion and timing frames remain unmeasured (`PIT-003`, `PIT-005`, `PIT-006`).

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Reset, before joystick movement | Move the left joystick | Adventure action begins with the documented initial score, time and lives | Entry and start trigger | `PIT-001`, `PIT-003` |
| One reachable uncollected treasure | Run into it | The treasure is credited once at its class value | Contact score pickup, not a power-up | `PIT-002` |
| Harry above an ordinary floor hole | Fall through instead of using a ladder | Subtract 100 points without the catastrophic-hazard life debit | Nonlethal route mistake | `PIT-002`, `PIT-003` |
| An autonomous rolling log reaches Harry | Remain in contact, then separate | Point loss depends on contact duration, not an asserted fixed hit value | Continuous exposure penalty | `PIT-002` |
| A ladder connects surface and tunnel | Descend and traverse one tunnel scene | Its surface progression is equivalent to three surface scenes; return requires a reachable ladder | Shortcut stride and local topology | `PIT-004` |
| Vine passes within a jump's reach | Jump to catch it, then pull down | Attached Harry follows the existing swing until release; a safe landing still depends on position | Command versus carriage | `PIT-001`, `PIT-005` |
| A crocodile's jaw is closed | Land on its head and time the next jump | Jaw state matters; the animal is not removed or converted into a reward | Phase-dependent crossing | `PIT-006` |
| Harry meets a lethal hazard with another life available | Catastrophic contact | Spend a life and restore Harry at the current screen's left edge, rather than subtracting points | Recoverable finite loss | `PIT-003` |
| Two lives have already been lost, or the clock reaches zero | Third loss or expiry | Adventure ends; no automatic campaign or wager failure is inferred from time alone | Attempt boundary | `PIT-003` |

## Strategic and experiential structure

Local jumping and vine release must be timed under a live clock. Route choice connects those local skills: tunnel strides save traversal time but can bypass a surface treasure, so always heading one way is not a complete collection plan. Ordinary holes and logs damage score, whereas a fatal contact spends scarce lives and returns Harry to the left; their different costs can favour a different direction on the retry. The manual's advice to run left exploits log direction and replacement position, not a forced one-way route.

## Replay and variation

The circular world is an authored deterministic topology rather than a newly sampled map on each run. The player varies route, crossing timing, shortcut use and tolerated score loss. No exact first-room layout, complete fastest route or terrain mutation between resets is asserted.

## Adjacent systems and history

Original *Super Mario Bros.* (`GAME-0311`) also admits local movement, contact score and finite-life return, but its analysed World 1-1 has different hazards, power states and a stage exit. The geometric resemblance does not license Mario's enemy stomp or combat pickups here. The later Activision retrospective's 256-screen count is rejected in favour of the original booklet and Crane's 255-screen account.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-633` | run/jump/ladder and vine catch/release |
| System Behaviour | `SYS-037`, `SYS-045`, `SYS-911`, `SYS-1244`, `SYS-1245`, `SYS-1246`, `SYS-1247` | treasure, logs, replacement, paired routes, penalties, jaws and carrier |
| Constraint | `CON-743` | twenty minutes or third loss |
| Information | `INF-192`, `INF-453` | current scene, score, time and replacement marks |
| Objective | `OBJ-002` | maximal net treasure score |
| Time | `TIM-003` | live adventure |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `478` (`GAME-0001`–`GAME-0478`).
- Exact genome matches: none.
- Tied near matches: `GAME-0333` — Sonic the Hedgehog (`7 / 27 = 0.259259`).
- Supported combination subsets: none.
- Scan date: 2026-10-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0333` *Sonic the Hedgehog* | `ACT-008`, `SYS-037`, `SYS-045`, `SYS-911`, `INF-192`, `OBJ-002`, `TIM-003`: direct traversal, score pickup, moving actors, finite replacement, local side view, score maximisation and live time. | Pitfall! composes a circular surface/tunnel treasure route, uses a caught vine and cyclic crocodile support, and separates nonlethal point debits from lethal lives. Sonic's scoped Green Hill route instead resolves its own ring-protected harm, rolling attack and authored stage completion; these are not licensed by the shared movement core. | `7 / 27 = 0.259259`; nearest non-exact prior signature, not the same hazard or route rules. |

## Taxonomy impact

`TAXONOMY_CHANGE_216` admits seven bounded genes. Seven existing boundaries transfer unchanged. No earlier genome, definition or verified combination is rewritten.

## Negative results

- Reject `SYS-036`: the booklet does not prove force-integrated rather than authored jump/swing trajectories.
- Reject `SYS-064`: landing on a closed crocodile head does not destroy or transform it.
- Reject `SYS-1055` and `ACT-479`: no original adjustable-radius tether or glide is established.
- Reject `CON-068`: normal clock expiry ends a score adventure rather than necessarily declaring a completion goal failed. `CON-666` additionally requires retained Tour goals absent here.
- Reject `INF-347`: no independent route-resource tally, stage number or capability feedback is established by the original diagram.
- Reject the later publisher's 256 scenes and the manual's composite diagram as exact individual-room evidence; retain the original 255-scene circular route.

## Delta summary

## New facts

- [Confirmed | Direct | High] Point loss and life loss are distinct costs in the original adventure (`PIT-002`, `PIT-003`).
- [Confirmed | Corroborated | High] Underground travel advances three surface-scene equivalents within the original 255-scene ring (`PIT-004`).

## New genes

- [Observation | Direct | High] Seven boundaries separate vine command/carriage, unequal route stride, nonlethal score loss, cyclic support, attempt limits and HUD information.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed; earlier subsets are recomputed against the complete signature.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_216`; earlier signatures remain unchanged.

## New questions

- A pinned original-cartridge trace could verify exact collision geometry, jump/swing paths, jaw periods, closing-pit phases and the result immediately after the final treasure. None is filled in from another port.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0480` *Populous*, original Amiga, follows full acceptance and the Goal stop window.
- Optimisation criterion: move from one-body timed traversal to indirect terrain-mediated population management on a different platform.
