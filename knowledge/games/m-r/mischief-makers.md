---
game_id: GAME-0607
slug: mischief-makers
game_title: "Mischief Makers"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-611
    - ACT-807
  system:
    - SYS-037
    - SYS-1782
    - SYS-1783
  constraint: []
  information:
    - INF-572
  objective:
    - OBJ-329
  time:
    - TIM-003
---

# Game: Mischief Makers

This scope follows the
[canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Button mappings and the stage title are scoped parameters.

## Analysis scope

- Version / ruleset: English North American commercial Nintendo 64 Game
  Pak, product `NUS-NTME-USA`, released 1 October 1997. The product
  catalogue identifies an American revision, but the exact cartridge
  revision in the recordings is unknown. No Japanese, PAL or modified
  version is substituted.
- Primary decision loop: position for a close grab on the worm's head as
  it passes. Shake the held worm to expose an optional Gold Gem.
  Throw the worm into the arena surfaces, then position and catch it
  again until the encounter clears.
- Entry: select stage 1-7, Wormin’ Up!!, on Planet Clancer. Start at
  the garden introduction, before ordinary control of the encounter.
- Exit: the worm is defeated, the stage-clear transition settles, and
  the result and next-stage route become available. Stop before the
  first action of 1-8, Crisis: Nepton.
- Included: ordinary local movement and jump if needed for contact,
  near-head capture while the worm is alive, directed shake while
  it is held, separate gem acquisition, directional release into
  the arena, repeated grabs, worm defeat, and stage evaluation.
- Excluded: other stages, story choices, normal red and blue Star
  routes, Clanpots, continue currency, campaign ending thresholds,
  timed record optimisation, save persistence, glitches, and exact
  impact damage, throw count, rank or gem time thresholds.
- Suggested later scope: reach the distinct warp and exit stars in
  Clanball Land by shaking its mobile and stationary Clanballs.

## Direct-play status

No direct play was performed. A Nintendo of America booklet establishes
commands, gem qualification and the general result presentation. An
American-edition firsthand route identifies the worm's grab point, the
two kinds of useful contact and its hidden gem. Static English N64
frames, including an independent capture identified by its author as
recorded on hardware, corroborate contact, the separate collectible
route and the clear transition. The exact revisions and input timing were
not independently verified. No video or audio playback was used.

## Claim ledger

| ID | Claim | Claim status | Evidence quality | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- |
| MM-001 | The 1997 North American commercial Nintendo 64 edition is the scope. The Nintendo of America booklet and the matching US box/manual/cartridge catalogue establish the edition family. | Confirmed | Corroborated | High | P1, P2. The recordings do not establish a specific cartridge revision. |
| MM-002 | Grab with B. Down presses applied to a grasped target shake it. Direction plus B throws, and B alone can release a held item vertically. These are distinct commands. | Confirmed | Direct | High | P1 pp. 18–20. No assumption is made about hidden input buffers. |
| MM-003 | As the live worm approaches, Marina can grab it by the head at close range. The encounter can require another approach and capture after an earlier release. | Observation | Corroborated | High | H1, H2, W1 21:20–21:40, W2 0:44–1:04. No minimum range or capture window is measured. |
| MM-004 | Shaking the grasped worm exposes the hidden Gold Gem while the worm is still in the encounter. This is an optional branch accessed before defeating it. | Observation | Corroborated | High | P1 pp. 16 and 19, H1, H2, W2 0:50–0:58. No exact press count is claimed. |
| MM-005 | The gem must be collected separately. Nintendo documents timely stage completion for gem credit. The gem branch is separate from the required worm defeat. | Observation | Corroborated | Medium | P1 p. 16, H1, H2, W2 route. No cutoff, persistence or automatic gem award is inferred. |
| MM-006 | Surface impacts from throwing the live worm into a cliff face or downward into the ground can defeat it. The shown encounter settles with a stage-clear/next-stage transition without a separate exit grab. | Observation | Corroborated | High | H1, H2, W1 21:30–22:10, W2 1:07–1:29, W3 18:20–19:00. No exact hit count or value is claimed. |
| MM-007 | Results expose a rank and completed time, with a slot for the earlier time; stage selection records a rank by the cleared tile. The first-world route reports faster clears as generally ranking higher. | Observation | Corroborated | High | P1 p. 17, H1 grading notes, W1 20:30 shows the result template for the immediately preceding stage, W3 18:50 shows the new cleared tile. No exact Wormin’ Up!! grade threshold or replay improvement is asserted. |

## Basic data

- Release / origin: Treasure developed Mischief Makers. Nintendo of
  America published the scoped North American commercial edition.
- Platform: `PLAT-NINTENDO-64`, English single-player commercial Game Pak.
- Puzzle families: physics and object manipulation (FAM-007) for throws
  whose target is itself the body that impacts the arena, and real-time
  system pressure (FAM-010) for manual capture as that body passes.
- P1: [Nintendo of America instruction booklet](https://device.report/m/ed59b8cfef6fe83e7df982148f70d4d3c3b2257bb5b68784cf7d151d4f3477b8.pdf).
  Publisher booklet mirrored by an archive. Pages 15–20 establish ordinary
  clearing rules, Gold Gem qualification, result reporting and base inputs.
- P2: [Nintendo64EVER catalogue with US product identity and release date](https://www.nintendo64ever.com/Nintendo-64-Game-Data-Sheet,1677,Mischief-Makers.html).
  The catalogue entry describes the American V1.1 (A) variant and provides
  the three matching product serials. It does not identify the footage's ROM.
- H1: [Procyon Lotor’s November 1997 firsthand US-adjusted FAQ](https://gamefaqs.gamespot.com/n64/197950-mischief-makers/faqs/3127).
  The first-world level 7 route and grading notes supply the capture, arena
  impacts, and optional shake. Its earlier Japanese draft and broader
  ending claims are excluded.
- H2: [SayainPrince’s Nintendo 64 firsthand stage guide](https://gamefaqs.gamespot.com/n64/197950-mischief-makers/faqs/28316).
  The 1-7 section independently describes throws and the hidden gem
  dropping after a shake. Exact regional revision unknown.
- W1: [LongplayArchive English NTSC N64 recording](https://www.youtube.com/watch?v=PWqvseZrdAE&t=1234s).
  Public static frames from 20:34–22:06 show the garden, active encounter
  and transition. Playback was not used.
- W2: [N64th Street hardware recording of the Gold Gem route](https://www.youtube.com/watch?v=D7WDTQY6PzM).
  Use static frames near 0:44–1:04 for the active loop and 1:07–1:29 for
  the terminal sequence. The full source segment has no next-stage play.
- W3: [LongplayArchive’s other English NTSC N64 recording](https://www.youtube.com/watch?v=484WfygPC0g&t=989s).
  Second run from the same archive as W1. Read the 18:30 clear scene and
  the world map at 18:50 before Crisis: Nepton opens. It is a separate
  run, with the independence cross-check supplied by W2 and H1.

### Reproducible route evidence

1. Select Wormin’ Up!! in the first world's stage grid on the English
   commercial N64 release. After the opening dialogue, move in the
   garden until the approaching worm passes within reach.
2. Grab the head while it is present in reach. A missed positioning
   opportunity leaves the worm active. W2 0:44–0:47 shows the close
   figure and changing worm positions, H1 supplies the grab point.
3. For the optional Gold Gem, keep the worm held and shake it by
   pressing down repeatedly. Collect the exposed gem separately.
   The booklet specifies timely completion for gem credit, without
   giving this encounter's precise threshold. The small W2 stills
   support the branch's sequence and are not a button-input trace.
4. Use direction and B to throw it against a side wall or down onto the
   ground, as described by H1. Reacquire the head while the worm is
   still active and repeat. Compare W2 0:50–1:04 to 1:07–1:15,
   where arena contact is followed by the final flashes.
5. Read the stage-clear transition and the onward prompt around W2
   1:17–1:20. W3 18:30–18:50 shows the same outcome and the next
   stage highlighted in the world menu. End before starting that stage.

Claim IDs: MM-001–MM-007. All video addresses are external timecodes,
not values of the game's internal attempt timer.

## Mechanical decomposition

### Action Genes

- ACT-008: reposition Marina in the garden before each capture.
- ACT-611: grasp the nearby live adversary and throw it back into the
  arena in a chosen direction.
- ACT-807: while holding the worm, use down presses to shake it.
- Claim IDs: MM-002–MM-004, MM-006.

### System Behaviour Genes

- SYS-037: acquire the separate exposed gem by reaching it.
- SYS-1782: the eligible held shake releases an authored collectible
  while the worm remains alive.
- SYS-1783: arena contact damages the thrown worm, and a live target can
  be recaptured after a nonterminal release.
- Claim IDs: MM-003–MM-006.

### Constraint Genes

- No independent constraint gene is assigned. Reachability belongs to
  the captured-opponent action and the optional time qualification is
  recorded as evidence without inferring its exact threshold.
- Claim IDs: MM-002–MM-005.

### Information Genes

- INF-572: the post-stage result distinguishes the rank, elapsed
  completion time and previous-time slot.
- Claim IDs: MM-006, MM-007.

### Objective Genes

- OBJ-329: defeat the worm to clear this bounded stage directly.
  The Gold Gem remains a separate optional objective.
- Claim IDs: MM-004–MM-007.

### Time Genes

- TIM-003: worm movement and arena physics advance in real time
  during the catch and throw loop, so input follows a moving opportunity.
- Claim IDs: MM-003, MM-006, MM-007.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Approaching free worm | Grab the head in reach | Worm enters a held state | Capture precedes both follow-ups | MM-002, MM-003 |
| Worm held, Gold Gem hidden | Shake the held worm | Optional gem becomes available | Release of a collectible differs from release of the held worm | MM-004 |
| Gold Gem exposed | Collect it and continue | Optional collection is eligible for later credit | A spawned item is separate from stage progress | MM-005 |
| Worm in hand | Throw toward wall or ground | Impact advances the fight; live worm remains a possible target | Capturing the worm is distinct from doing damage | MM-003, MM-006 |
| Final successful impact | Allow the sequence to resolve | Stage clear and next-stage prompt | Stage completion needs no separate exit grab in this encounter | MM-006 |
| Stage cleared | Read the result and world map | Grade/time result and the onward route are visible | Evaluation is separate from the live inputs | MM-007 |

## Strategic and experiential structure

A successful catch provides a choice. Throwing the held opponent advances
the required battle if the impact is useful. Shaking first can expose
the optional gem, but the fight still needs to be finished. The available
arena surface determines a useful release direction. Repeated passes
give further opportunities rather than making the initial grab decisive.
Claim IDs: MM-002–MM-007.

## Replay and variation

W1, W2 and W3 show different timing and positions. The written route
documents both side and downward throws. The sources do not establish a
necessary hit count, exact Gold Gem settlement cutoff, exact rank
thresholds or overwrite rules for previous times. Claim IDs: MM-003–MM-007.

## Adjacent systems and history

The booklet describes blue exit stars and red warp gates for other
stages, and an ending effect for collecting Gold Gems. This encounter's
direct terminal and its one optional collectible do not model those
larger systems. Claim IDs: MM-005–MM-007.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-611, ACT-807 | Position, grasp and throw, or shake while holding |
| System Behaviour | SYS-037, SYS-1782, SYS-1783 | Separate pickup, shake yield and impact logics |
| Information | INF-572 | Expose a completed stage's grade and time comparison |
| Objective | OBJ-329 | Defeat the bounded opponent and settle the stage |
| Time | TIM-003 | Act while the opponent and arena continue moving |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `606` (`GAME-0001`–`GAME-0606`).
- Exact genome matches: none.
- Tied near matches: `GAME-0460` — Super Mario 64 (`4 / 17 = 0.235294`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Super Mario 64 (GAME-0460)](../s-z/super-mario-64.md) | ACT-008, ACT-611, SYS-037, TIM-003 | Big Bob-omb needs valid summit landings and a separate Power Star after defeat. The worm can be shaken for a gem while alive, and useful impacts directly advance the required clear. | 4 shared / 17 union; Jaccard 0.235294 |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_353](../../../research/taxonomy-changes/TAXONOMY_CHANGE_353.md)
  defines the new boundaries and records the evaluated alternatives.

## Negative results

- ACT-048 applies to an inert physics item. The captured worm remains a
  participant, so the grasp and directional release use ACT-611.
- ACT-297 is an immediate grapple/escape resolution without a deliberate
  held shake phase. That does not model the live held decision.
- SYS-1628 is a supply source releasing items to eligible strikes or
  contact. Here the trigger is shaking a source already grasped.
- SYS-1211 needs an explicit valid-landing boundary test with a special
  return on outside hits. The scoped worm impacts do not establish that.
- OBJ-262 requires a separate progress token after guardian defeat.
  The worm stage proceeds from defeat to stage clear without that token.
- TIM-023 initiates a hard countdown after a committed service. The
  available evidence supports real-time inputs and an elapsed result,
  without such a countdown start or a specific losing deadline.

## Delta summary

## New facts

- [Observation | Corroborated | High] The same held worm supports
  separate shake and throw commands. MM-002–MM-004.
- [Observation | Corroborated | Medium] An optional gem appears
  separately from the held opponent and its defeat. MM-004, MM-005.
- [Observation | Corroborated | High] Arena impacts can end the
  encounter, which settles directly and opens the next-stage route.
  MM-006, MM-007.

## New genes

- [Observation | Corroborated | Medium] ACT-807, SYS-1782, SYS-1783,
  INF-572 and OBJ-329.

## New combinations

- [Observation | Direct | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_353.

## New questions

- What timing governs the optional credit if the gem is acquired but
  the player delays stage completion?
- Which impacts count at which angles and heights?
- What exactly changes on a clear with a slower previous result?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0608`, Dosa Divas, full PS5
  release. Trace one early cooking-and-combat chain within an evidenced
  commercial route.

## Why this game

- [Hypothesis | Limited | Medium] A single live opponent can serve as a
  held item source or as the body whose collision advances the fight.
