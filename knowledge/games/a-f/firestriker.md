---
game_id: GAME-0713
slug: firestriker
game_title: "Firestriker"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-928
    - ACT-929
  system:
    - SYS-036
    - SYS-037
    - SYS-1999
    - SYS-2000
  constraint:
    - CON-897
  information:
    - INF-119
  objective:
    - OBJ-014
  time:
    - TIM-003
---

# Game: Firestriker

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Strike a freely moving Trialight in a chosen direction, cover the
lower breach and send the same orb through the northern passage.

## Analysis scope

- Version / ruleset: English North American commercial SNES
  cartridge SNS-3S-USA, DTMC, October 1994. The US instruction
  booklet and two English game recordings are the rule basis.
  The captured cartridge binaries, original hardware and timing
  revisions are unverified.
- Structured analysis target: PLAT-SUPER-NINTENDO in
  [platform coverage](../../platforms/games.json).
- Entry: choose 1 Player Normal Mode and the first playable
  area from the map after the Wind Castle briefing. Start in
  its first grassy room, with Slader, the blue Sorcerer Wain and
  a single Trialight next to the four southern barrier blocks.
- Primary decision loop: move Slader to intercept the live orb
  and strike it with a direction input. Use the orb against
  enemies and breakable blocks, cover the lower barrier with
  Wain and redirect the orb toward the upper passage.
- Positive terminal: after the Trialight leaves through the
  northern passage, the view scrolls into a room with two
  stone clusters. Slader and Wain reappear at its south edge.
  Stop at the new room's opening state.
- Included: direct movement and ordinary angled strikes, independent
  horizontal goalie positioning and automatic returns, changing
  brick and enemy states, collectible POW, visible life and power
  counts, and the lower breach rule documented by the manual.
- Excluded: separate use of a Power Strike, tool-assisted physics
  claims, exact collision constants, later locked doors and bosses,
  second-player control, Multi Mode, and credit and continue
  behaviour beyond one room.
- Potential scoped module: compare ordinary and charged Trialight
  strikes on the same brick row while controlling angle and position.
- Direct-play status: no personal SNES or emulator session, cartridge
  verification or input telemetry. The booklet specifies controls
  and failure. The two captures trace the opening room and transition.
  The first shows the Sorcerer's return with Slader beside him.
  No bottom-drain failure appears in the selected window. Frame
  inspection was in the background without audio.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| FST-001 | The North American English commercial Firestriker is a 1994 DTMC SNES release. The US booklet credits Axes Art Amuse. The catalogue identifies October and SNS-3S-USA. The traced game uses the 1 Player entry rather than the demo or Multi Mode. | Confirmed | Corroborated | High | P1 front and pp. 5–9; P2; W1 0:08–0:14, 0:46–0:54 |
| FST-002 | Slader can move directly in the room. A or B swings at a nearby Trialight, and the directional pad during the hit selects where the orb is sent. The ordinary swing can displace an enemy or obstacle without dealing the orb's impact damage. | Observation | Corroborated | High | P1 pp. 6, 9–10; W1 0:54–0:59; W2 2:25–2:43 |
| FST-003 | The Trialight continues after a strike and rebounds from surfaces. A valid contact with a green enemy or a breakable block can remove that target; solid and surviving objects continue to route the orb. The north route becomes open while unrelated bricks remain on the right. | Observation | Corroborated | High | P1 pp. 10–13; W1 0:55–1:05, 1:29–1:36; W2 2:30–2:44, 3:10–3:16 |
| FST-004 | In 1 Player mode, L and R position Wain near the bottom independently of Slader's directional movement. Wain automatically bats a nearby Trialight and is immune to damage. W1 shows the blue return animation with the red striker beside him at the southern blocks. | Observation | Corroborated | High | P1 pp. 8, 12; W1 1:05.8–1:06.5 |
| FST-005 | A Trialight escape through a gap in the bottom barrier costs a full life. Enemy contact can cost hearts, with depleted hearts also costing a life. The booklet distinguishes these counters. Both reviewed successes keep the Trialight in play and do not show the drain branch. | Confirmed | Direct | High | P1 pp. 10–12; W1 1:02–1:11 |
| FST-006 | An appearing POW item can be collected by overlap with Slader. The Power display shows stored shots with a maximum of three according to the booklet. In W1 the pickup disappears and the first slot lights around 1:17. A second slot lights around 1:26. | Observation | Corroborated | High | P1 pp. 10–11, 14; W1 1:16–1:18, 1:24–1:27 |
| FST-007 | Sending the Trialight past the north side triggers the positive exit. In both traces the orb disappears at the upper opening and the screen scrolls while Slader is still in the old room; neither recording requires him to cross separately. Both characters are set down at the beginning of the next room. | Observation | Corroborated | High | W1 1:34–1:39; W2 3:13–3:19 |

## Basic data

- Release / origin: Axes Art Amuse and DTMC, commercial North
  American Super Nintendo cartridge, October 1994.
- Families: FAM-007 for directing the orb through contact and
  geometry, and FAM-010 for adjusting both interceptors during its
  uninterrupted flight.
- P1: [DTMC's original US instruction booklet](https://archive.org/details/firestriker-usa).
  See printed pp. 6–12 for the normal controls, strike, counters
  and goalie, and pp. 13–14 for door variants and pickups.
- P2: [North American release record and product ID](https://www.arcade-history.com/game/63009/fire-striker-model-sns-3s-usa)
  and [regional release list](https://www.mobygames.com/game/17882/firestriker/releases/).
  These corroborate product and date, without asserting the ROM
  identity of the recordings.
- W1: [LongplayArchive, English NTSC SNES opening](https://www.youtube.com/watch?v=22h5SPTENQU&t=53s).
  The first room is shown from its placement to the second room
  becoming active.
- W2: [NintendoComplete, English SNES opening](https://www.youtube.com/watch?v=LywWmlSGRGk&t=144s).
  A slower route through the same room independently checks the
  separation between the orb's exit and the avatar's position.
- Claim IDs: FST-001–FST-007.

### Reproducible fixture evidence

1. W1 0:53–0:55 shows the first room initialise. The blue
   Sorcerer is immediately above the four intact bottom blocks.
   Slader starts to his left with the orb close by. Move Slader
   up the grassy field and use A or B plus the intended direction
   when within reach of the orb.
2. Follow the rebounds and contact effects at W1 0:55–1:05.
   Green enemies move independently. The orb hits enemies and
   blocks and leaves surviving geometry in play. At 1:05.8–1:06.5
   the blue figure animates as a nearby orb is sent back into
   the arena. The red figure stands to its right.
3. W1 around 1:17 and 1:26 shows power icons fill as Slader
   overlaps pickups. The manual permits a later Power Strike,
   while this witness keeps the two filled slots through the
   exit. No consumption or extra damage is inferred from its
   ordinary swings.
4. By W1 1:34 the upper left route has opened, with a large
   group of bricks still on the right. At about 1:35 the ball
   leaves the visible opening, followed shortly by the camera
   scroll. The trace does not expose the exact boundary frame
   or collision threshold for the exit.
5. W2 3:13–3:19 repeats the change of room from a noticeably
   leftward avatar position. Slader remains left of the opened
   passage when scrolling begins. The next room contains a
   pair of stone clusters and places both actors along the
   bottom again.

## Mechanical decomposition

### Action Genes

- ACT-008: move Slader around the grass to meet the live orb or
  avoid an enemy.
- ACT-928: strike the nearby Trialight with a direction command
  and redirect that same moving object.
- ACT-929: shift a separate bottom defender left or right with
  the shoulder buttons while retaining Slader's direct control.

### System Behaviour Genes

- SYS-036: the Trialight continues through motion and contacts
  between player actions.
- SYS-037: Slader's overlap credits a loose POW pickup to his
  reserve while the room continues.
- SYS-1999: when the Trialight comes within the solo Sorcerer's
  reach, his local automatic strike returns it to play.
- SYS-2000: eligible impacts from the live Trialight remove
  enemies and field bricks. Clearing one brick changes the route
  still available to the orb. The ordinary sword swing itself
  does not apply these target effects.

### Constraint Genes

- CON-897: a Trialight escape through the broken lower barrier
  costs a life independently of Slader's current hearts. Losing
  all hearts is a separate way to lose a life.

### Information Genes

- INF-119: visible hearts, Power and remaining lives distinguish
  damage, available shots and remaining attempts.

### Objective Genes

- OBJ-014: route the live Trialight through the fixed northern
  opening and trigger the next room.

### Time Genes

- TIM-003: the orb and enemies move while the player positions
  and times the striker and the keeper.

### Parameters

Striker and orb position, strike direction and reach, remaining
block pattern, keeper lane, lives, hearts and POW stock. Rebound
equations and exact contact thresholds were not measured.

## Reproducible transitions

| Entry state | Input or event | Expected next state | Evidence |
| --- | --- | --- | --- |
| Slader near the live orb | Strike while holding a direction | The existing orb moves on the commanded heading | FST-002 |
| Orb approaches a valid enemy or brick | Allow qualifying contact | The target can be removed and the route changes where a brick was hit | FST-003 |
| Ball approaches the bottom defender | Position Wain within intercept reach | Wain strikes automatically and the orb moves back into the room | FST-004 |
| Bottom barrier already has a gap | Let the orb escape through it | A life is lost independently of the current heart count | FST-005, booklet rule |
| Loose POW is visible | Walk Slader over the pickup | The pickup is credited to the visible Power stock | FST-006 |
| North opening is reachable | Send the Trialight through the opening | Camera scrolls, then places the actors at the next room entrance | FST-007 |

## Strategic and experiential structure

Slader can chase the orb and choose the angle of the next hit.
Moving Wain is a separate decision that changes the fallback line.
A useful attack opens space at the far end while limiting downward
escape. A successful room depends on the orb's travel, with the
striker free to end the shot from a different position.

## Replay and variation

Both first-room traces share the bottom barrier and northern
passage. They spend different amounts of time clearing and aiming,
and end with different surviving brick arrangements. A universal
kill or block quota does not follow from the scoped exit.

## Adjacent systems and history

The US booklet distinguishes breakable, defeat-gated and key-gated
doors elsewhere. It describes an optional Power Strike requiring
stored POW. The two visible reserve acquisitions in the first room
do not establish a powered hit or a later door requirement.

## Normalised genome

- Action: ACT-008, ACT-928, ACT-929.
- System Behaviour: SYS-036, SYS-037, SYS-1999, SYS-2000.
- Constraint: CON-897.
- Information: INF-119.
- Objective: OBJ-014.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `712` (`GAME-0001`–`GAME-0712`).
- Exact genome matches: none.
- Tied near matches: `GAME-0460` — Super Mario 64 (`5 / 18 = 0.277778`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Super Mario 64 (GAME-0460)](../s-z/super-mario-64.md) | ACT-008, INF-119, SYS-036, SYS-037, TIM-003 | Firestriker routes one separate orb with directed hits and an independently positioned defender. In the scoped Super Mario 64 mission, Mario uses jumps, terrain and direct boss throws to reach and collect a Power Star. | Near, `0.277778`. |

## Taxonomy impact

Reuse independent avatar movement, continuing dynamics, contact
pickups, visible resources, designated payload delivery and live
intervention. Admit directional strikes of one existing orb,
independent keeper positioning, the automatic return,
impact-dependent target removal and a life loss on lower escape.

## Negative results

- Reaching the upper bricks with Slader is insufficient to infer
  that he crosses the room exit.
- A target can be a barrier or enemy. A sword animation on its
  own does not establish the orb's damage result.
- Filled Power slots do not prove that a Power Strike was used.
- The room clears while pale blocks remain beside the opening.
- Neither successful trace tests a bottom drain or credit use.

## Delta summary

One orb is both the thing to protect and the means to open the
route. The mobile striker aims its hits and a separately positioned
keeper can return it. Sending the orb out at the top advances the
room. Letting it leave through a lower breach has a different
documented consequence.

## New facts

- The shot's direction is chosen at nearby strike contact.
- The solo lower defender's return activates automatically.
- The orb's upper exit advances the arena independently of the
  red striker's crossing.

## Principles and design implications

Keep the controlled character and routed object distinct. Give
incoming and outgoing openings disjoint consequences. Offer an
interceptor that has its own placement decision, while keeping
the orb's actual collision and exit results observable.

## Puzzle or game generation potential

Use one free orb, a mobile direction-selecting striker, a narrow
auto-return lane and breakable geometry. Build a fixture where one
upper gap qualifies even with other bricks left, and a separate
lower gap drains the ball. Test that moving the defender changes the
chance of interception without granting direct control over the orb.

## New genes

- ACT-928
- ACT-929
- CON-897
- SYS-1999
- SYS-2000

## New combinations

None.

## Taxonomy changes

[Taxonomy Change 459](../../../research/taxonomy-changes/TAXONOMY_CHANGE_459.md).

## New questions

- How much additional brick clearance does one Power Strike provide
  relative to an ordinary hit on the same row?
- What part of the animated return determines Wain's contact
  boundary on the original target?

## Next recommended game

Continue Selection 062 with Thirsty Suitors, the English PlayStation 5
commercial base game. Follow an opening conversation battle through
a mood change and its effect on the available turn outcomes.

## Why this game

The opening arena isolates a released ball, a direction-selecting
strike, a separate automatic defender and asymmetric exit rules.
