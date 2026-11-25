---
game_id: GAME-0709
slug: baby-steps
game_title: "Baby Steps"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-925
  system:
    - SYS-036
    - SYS-1990
    - SYS-1991
  constraint: []
  information:
    - INF-258
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Baby Steps

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Lift one foot, place it on the mossy incline and transfer enough weight
to free the other foot. A fall can leave the next attempt lower on the
same slope.

## Analysis scope

- Version / ruleset: English commercial PS5 base game, PlayStation Store
  product UP3643-PPSA16935_00-0010234175390827, released September 23,
  2025. The evidence identifies the launch-period ruleset and does
  not identify the installed patch or accessibility settings of either
  PS5 capture.
- Structured analysis target: PLAT-PLAYSTATION-5 in
  [platform coverage](../../platforms/games.json).
- Entry: first controllable upright stance above the opening pool
  in the mossy hollow. Look uphill along the central slope between
  the stones. The first hint panels teach moving and lifting the feet.
- Primary decision loop: choose a foot, hold its lift control, use
  the left stick to direct its placement and shift the body, then
  release the trigger so the foot descends. Once the new foothold
  supports the body, move the other foot. After a fall, resume
  from the current part of the slope when upright control returns.
- Positive terminal: upright and able to take the next stride on
  the upper moss strip, just below the lip that precedes the first
  guide scene. This is a spatial fixture endpoint. Neither a precise
  scene trigger nor a stored checkpoint is asserted.
- Included: manual foot lift, directional placement, transfer of
  support, local pose and ground feedback, live falling and the
  return to an actionable upright stance on the first slope.
- Excluded: the initial room and pool sequence, the cutscene at
  the lip, dialogue, later balancing routes, gear, global navigation,
  save or reload behaviour, exact collision and joint thresholds,
  later patches and versions on other platforms.
- Suggested later scope: compare one narrow elevated crossing from
  multiple approach lines, including one witnessed fall that comes
  to rest on a lower part of the route.
- Direct-play status: No personal console session, hardware telemetry or save inspection.
  Two attributed PS5 recordings were examined as silent frame sequences.
  The PS5 default controls come from the official PS Blog hands-on
  account. The frames show poses and locations and cannot confirm
  the physical input used to rise or the captures' control remapping.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| BS-001 | The English PS5 commercial base game was released September 23, 2025 under the named North American digital product. | Confirmed | Direct | High | P1, P2 |
| BS-002 | L2 holds the left foot up and R2 holds the right. Release lowers the selected foot. Moving the left stick during the hold adjusts its placement. | Observation | Corroborated | High | P3 control section; P4 independent foot control; W1 0:44–0:49 control hints |
| BS-003 | Directional input shifts the body and alternating foot placements can move it up the opening slope. A successful step leaves a new point of support for the next leg. | Observation | Corroborated | High | P3; P4; W1 1:08–1:20; W2 1:59–2:03 |
| BS-004 | The hiker's foot, torso and the visible ground let the player distinguish an upright supported stance from a tipping or fallen body and judge the next contact. | Observation | Corroborated | High | P3 slope and contact account; W1 0:49–0:58; W2 0:50–0:58 |
| BS-005 | In the playable ascent, balance loss can leave Nate on his side or front among the same stones and moss. The falling body can move downhill before settling. | Observation | Corroborated | High | P3; W1 0:50–0:56 and 1:02–1:07; W2 0:51–0:57 and 1:54–1:59 |
| BS-006 | The next upright steps start on the local slope after recovery. No reload, fail menu or fixed trailhead reset appears in these transitions. | Observation | Corroborated | High | W1 0:54–1:00 and 1:05–1:10; W2 0:54–1:00 and 1:58–2:03 |
| BS-007 | Both traces regain an upright advancing stance on the upper moss strip before the first guide scene. The first guide scene changes camera and is outside the live-fall sample. | Observation | Corroborated | High | W1 1:16–1:22; W2 2:00–2:07 |

## Basic data

- Analysis target: English single-player PS5 commercial download by Gabe
  Cuzzillo, Maxi Boch and Bennett Foddy, published by Devolver Digital.
- Family: FAM-007, physics and object manipulation. Direct foot placement
  alters the body's support in a running physical simulation.
- P1: [PlayStation Store, named PS5 product](https://store.playstation.com/en-us/product/UP3643-PPSA16935_00-0010234175390827).
  Establishes platform, English availability, release date and physics-based
  walking.
- P2: [Devolver Digital September 2025 interim investor presentation](https://investors.devolverdigital.com/files/downloads-and-publications/devo-fy25-1h-investor-presentation--final-2025-09-29.pdf).
  Confirms the September 23 commercial launch on PS5 and identifies the
  three developers.
- P3: [PlayStation Japan, released PS5 hands-on account](https://blog.ja.playstation.com/?p=271046).
  Section two explains the left and right triggers, left-stick weight
  shift and foot placement, right-stick view, supported holds and tumbles.
- P4: [Maxi Boch, PlayStation Blog developer introduction](https://blog.playstation.com/2023/09/14/wonderfully-weird-walking-sim-baby-steps-toddles-onto-playstation-next-year/).
  Establishes independently steered feet and simulated surfaces. Its
  prelaunch schedule is historical and not used to date the released game.
- W1: [Lutfinator82496, attributed PS5 opening capture, September 24](https://www.youtube.com/watch?v=6b1IHKW8W2E&t=42s).
  Shows the first hints, multiple playable falls, recovery and the crest.
- W2: [HausofZombies, separate attributed PS5 opening capture, September 25](https://www.youtube.com/watch?v=u85AsZkCwyU&t=48s).
  Shows repeated falls along a different line past the right-hand stones
  and upright control returning before the scene. Examined through
  sampled video frames without playback or sound.

### Reproducible fixture evidence

1. Start after the opening pool at the first rear follow-camera stance.
   W1 at 0:42–0:49 displays move and foot-lift hints. P3 describes
   the default input split. Face the rising moss strip ahead.
2. Hold the control for either foot, adjust where it will descend
   and release the trigger. Use the planted contact to move the
   next foot. W1 at 1:08–1:20 and W2 at 1:59–2:03 show repeated
   changes of the raised and planted leg with forward movement.
3. For the negative trace, compare W2 at 0:50–0:58. The body tips
   beside the right-hand edge, lies against the moss and rises nearby.
   W1 at 1:02–1:10 shows another fall with the torso on the ground
   followed by an upright stance on the same incline. Precise causes
   and any recovery input are not visible as telemetry.
4. Mark the positive end while still upright on the upper moss strip.
   W1 at 1:16–1:20 has regained steady forward steps there. W2 at
   2:00–2:03 briefly settles upright and starts another step.
   In both recordings the first cinematic cut follows, and the
   cinematic fall is excluded from the live experiment.

## Mechanical decomposition

### Action Genes

- ACT-008: directly guide the persistent avatar onto the upper strip,
  including changing the uphill line after a local fall.
- ACT-925: separately lift the chosen foot, guide it with live
  direction, and release its lift control to lower it. The other
  leg can stay planted before switching roles.

### System Behaviour Genes

- SYS-036: the body keeps moving under weight, ground geometry and
  collision while contact changes. Prone motion can continue after
  a failed foot placement.
- SYS-1990: a viable new foot contact receives weight so the former
  supporting foot can be moved. Poor positioning or a collision
  can cause an unstable stance before or after contact.
- SYS-1991: a fallen body remains in the same terrain and the next
  upright steps start near its resulting local position.

### Constraint Genes

The fixture has physically constrained placements. Reach, slope and usable
support are parameters of the walking resolution. No distinct input gate,
footstock, action quota or timed constraint was observed.

### Information Genes

- INF-258: the slope, stone edges, the lifted foot, current contact
  and torso tilt expose current support and fall risk. These cues
  are visible immediately before choosing another step.

### Objective Genes

- OBJ-026: reach the upper strip of the first climb with actionable
  upright footing. Achieving it requires building a traversable
  sequence of live footholds on the local ascent.

### Time Genes

- TIM-003: the body continues to tip, settle and move while
  controls are available. The phase is self-paced in the ordinary
  sense and the physical simulation continues between inputs.

### Parameters

Chosen side, direction, current foot contact, surface geometry,
centre-of-mass shift, step length, current velocity, posture and
resulting local position. Exact joint forces, minimum stable angles,
button-hold thresholds and recovery timing are not established.

## Reproducible transitions

| Entry state | Input or event | Expected next state | Evidence |
| --- | --- | --- | --- |
| Upright on the first ascent | Hold the selected foot's trigger and use the left stick | One raised foot changes position while the other can support the stance | BS-002–BS-003 |
| Raised foot reaches a viable point | Release the trigger and transfer body weight | The lowered foot takes support and the other can advance | BS-003 |
| An unstable stance on the same slope | Lose support as contact and momentum resolve | The body falls to the local terrain and may slide down it | BS-004–BS-005 |
| Body has fallen on the slope | Let the recovery reach an upright, actionable state | Another step is possible at the resulting place on the slope | BS-006 |
| A viable sequence of alternating steps | Advance onto the upper strip below the lip | An upright stride is possible before the guide camera takes over | BS-007 |

## Strategic and experiential structure

Place a foot where it can bear weight before moving the other.
On a shallow rise, a short placement can preserve a usable posture
where an extended stride can tip. A fall can erase elevation by
moving the body downhill, so the next useful move uses the new
nearby contacts rather than a reset position.

## Replay and variation

Both captures share the first slope and upper strip. Their
lines, time spent recovering and positions beside stones differ.
These are differences in observed execution. The comparison
does not establish a fixed step count, a randomised layout or
a universal recovery delay.

## Adjacent systems and history

Later physical routes use other terrain, and the publisher describes
a much longer mountain journey. The first guide scene supplies an
observable boundary for this unit. Its dialogue, animation and
subsequent route remain separate.

## Normalised genome

- Action: ACT-008, ACT-925.
- System Behaviour: SYS-036, SYS-1990, SYS-1991.
- Constraint: none.
- Information: INF-258.
- Objective: OBJ-026.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `708` (`GAME-0001`–`GAME-0708`).
- Exact genome matches: none.
- Tied near matches: `GAME-0112` — Human: Fall Flat (`4 / 12 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Human: Fall Flat (GAME-0112)](../g-l/human-fall-flat.md) | ACT-008, OBJ-026, SYS-036, TIM-003 | Both directly steer one body toward a local destination while physics continues. Human: Fall Flat uses a carried crate and two independently gripped hands to gain leverage below its exit ledge. Baby Steps transfers weight between individually placed feet and resumes on the terrain where a fall ends. | Near, `0.333333`. |

## Taxonomy impact

Reuse local agent navigation, live dynamics, climbing cues, goal
arrival and continuing time. Separate the selectable foot inputs,
the change of support on a successful foot contact and the
in-world return of control after an ordinary fall.

## Negative results

- Moving the lifted foot forward can fail to produce an upright
  advance if the character loses support.
- The observed playable falls lead back to local control without
  a fixed respawn. Later checkpoint and fast-travel behaviour
  are separate research questions.
- The falling camera scene at the lip supplies no evidence about
  the cause of a failed ordinary foot placement.
- The recordings alone do not establish an exact command or
  delay for standing.

## Delta summary

One input addresses one walking foot. Body support transfers
when a placement can sustain it, and a fall can change the
next starting position anywhere along the first slope.

## New facts

- The same directional input adjusts position and shifts body
  weight under the documented foot-control scheme.
- Alternating current support lets the player make measured
  progress uphill.
- Falling and regaining control can take place in one continuous
  local traversal.

## Principles and design implications

Make the current support easy to read while the player moves
the other foot. Offer a reachable sequence of firm placements and
keep failed positions physically meaningful by starting the next
attempt where the body actually settled.

## Puzzle or game generation potential

Create a short hill with uneven footholds. Give each foot a
dedicated lift control and end each hold with a fall toward the
terrain. Check that planting one foot frees the other and that
next attempts after loss of balance use the actual position.

## New genes

- ACT-925
- SYS-1990
- SYS-1991

## New combinations

None. The complete scan supports no verified subset.

## Taxonomy changes

[Taxonomy Change 455](../../../research/taxonomy-changes/TAXONOMY_CHANGE_455.md).

## New questions

- How do surface geometry and incoming momentum interact when
  the new foot contacts a raised edge?
- What conditions end the fallen state on different slopes?

## Next recommended game

Continue Selection 061 with Racing Destruction Set on the English
Commodore 64 commercial disk. Follow one track configuration into
its observed race-physics consequence and result.

## Why this game

A short opening path makes manual foot placement, the resulting
transfer of support and the next attempt after a fall visible as
three distinct mechanical events.
