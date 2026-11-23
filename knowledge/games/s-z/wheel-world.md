---
game_id: GAME-0603
slug: wheel-world
game_title: "Wheel World"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-309
    - ACT-341
    - ACT-804
  system:
    - SYS-516
    - SYS-691
    - SYS-765
    - SYS-1775
    - SYS-1776
  constraint:
    - CON-438
    - CON-848
  information:
    - INF-205
    - INF-208
    - INF-566
  objective:
    - OBJ-134
  time:
    - TIM-003
---

# Game: Wheel World

Comparison uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Race name, bicycle components, lap count and reward amount are instance
parameters of this opening route.

## Analysis scope

- Version / ruleset: full English Windows Steam base game, app
  `1497460`, released 23 July 2025. The observed rules are from two
  early commercial PC traces published on 5 and 8 August. The exact
  build of either recording is unverified. Patch 3 later noted an
  incorrect starting-position fix for the Lunardo race.
- Structured analysis target: PLAT-WINDOWS-PC in
  `knowledge/platforms/games.json`. The Steam product is the scope.
  Both attributed recordings show the commercial story and beyond
  the scoped opening. Neither proves its installed binary or purchase
  entitlement.
- Primary decision loop: acquire and equip the beach wheel during
  preparation. Race through two marked laps, closing behind opponents
  to build boost and choosing when to spend it on an overtake or
  useful exit line. Win and settle the distinct reputation award.
- Entry and exit: in a fresh ordinary story, begin mounted on the
  initial bicycle at the first barrier conversation with the
  Lunardo Boys boss, after the prologue. Follow the beach instruction,
  fit the shown rear wheel, return to the barrier and enter the
  first Lunardo Hill Boys race. Stop after the first-place result,
  the reputation award and the following dialogue opening access
  past the group, before the rematch or shrine.
- Included: first entry conditions, ordinary route to the beach,
  open the part box, fit a typed component, base handling, steer,
  pedal and brake, boost lesson, drafting, charge and spend, marked
  course position, two laps, finish and retained reward.
- Excluded: prologue on foot, optional boxes or alternate builds,
  unattested gear setups, later shifts and off-road perks, timed
  records and KAT challenges in later races, Lone Wolf races,
  Lunardo Rematch, shrine upgrades, bridge crossing, other platforms
  and exact meter, grip, checkpoint or AI constants.
- Potential scoped modules: a repeatable KAT-and-first race, one
  Lone Wolf event under a fixed patch, or a build-specific time trial.
- Direct-play status: no direct play. Official release and developer
  documents establish the product, physical wheel model and design
  intent. Still frames from two PC-attributed traces establish the
  ordinary route and finish. Firsthand documentation corroborates the
  preparation and two laps. No intentionally lost race, missed gate,
  collision threshold or persistence after a reload was tested.
  No video or audio playback.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| WW-001 | Steam distributes the single-player Windows base release from 23 July 2025. Early commercial footage and later patch changes are separate. | Confirmed | Corroborated | High | P1, P2, P4, W1, W2. |
| WW-002 | The initial boss declines the race before the crew returns. The preparation visits the beach and rejoins the crew at the barrier, where the first event is offered. | Observation | Corroborated | High | W1 4:00–4:30, 6:00–8:40, 9:30–10:00; W2 4:00 and 8:40–8:50; H1. |
| WW-003 | The addressed beach box supplies a Commuter Wheel. An owned wheel can replace the rusty rear wheel in its own Bike slot without replacing the whole bicycle. | Observation | Corroborated | High | W2 6:10–6:20, W1 6:40–7:20; P3, H1. |
| WW-004 | Fitted parts contribute to current bicycle ratings. The moving bicycle uses distinct linked wheels and tyre-surface friction, with steering from the front wheel. | Confirmed | Corroborated | High | P3, W1 7:00–7:10, W2 6:20. No exact part coefficients are asserted. |
| WW-005 | The tutorial describes following a cyclist to earn boost. A separate held command spends the available reserve into acceleration. The charge and active effect have visible signals. | Observation | Corroborated | High | P3, W1 8:20, 10:10–10:40, W2 9:00–9:50. |
| WW-006 | The first event follows marked course intervals over two laps with live place, speed, next marker and minimap. Completing the first loop changes the status to final lap while rivals and input still advance. | Observation | Corroborated | High | W1 10:00–11:40, W2 8:50–10:30, H1. The exact missed-marker predicate was not isolated. |
| WW-007 | The demonstrated valid first place yields Winner 1st and a separate +1 Rep reward. One reputation point remains displayed in the ensuing conversation. | Observation | Corroborated | High | P5, W1 11:50–12:40, W2 10:40–11:20. |
| WW-008 | After settlement the boss permits access, and play resumes before the shrine. A later optional rematch is a separate event with its own entry. | Observation | Corroborated | High | W1 12:10–13:20, W2 10:50–12:40, W3 18:10–19:50. |
| WW-009 | Winning the tutorial and starting a later race are established. Effects of a deliberate skipped gate, narrow wheel-eligibility alternatives, losing the first event and exact retry preservation were not directly reproduced. | Observation | Limited | Medium | P4, H1, W1–W3; ordinary winning traces. |

## Basic data

- Release / origin: developed by Messhof and published by Annapurna
  Interactive, Windows Steam commercial release in 2025.
- Platform or physical form: English single-player Windows PC,
  using controller prompts in the two observed traces.
- Puzzle families: physics and object manipulation (FAM-007) and
  real-time system pressure (FAM-010). The linked wheels and selected
  components influence the live racing line; the relative position
  of moving rivals constrains access to drafting opportunities.
- P1: [official Steam product](https://store.steampowered.com/app/1497460/Wheel_World/),
  release date, Windows requirements and single-player product.
- P2: [Messhof's release announcement](https://store.steampowered.com/news/app/1497460/view/524223243273373598)
  and [publisher product page](https://annapurnainteractive.com/games/wheel-world)
  corroborate the commercial release, distinct from the prior demo.
- P3: [Messhof creative director’s design account](https://unity.com/blog/how-frankenstein-bikes-inspired-wheel-world),
  on fitted components, drafting, independent wheel simulation, tyre
  friction and AI lines. The developer describes implementation,
  while the traces establish which systems are used in this route.
- P4: [official development and patch feed](https://steamcommunity.com/app/1497460/allnews/)
  and [Post Launch Patch #3](https://store.steampowered.com/news/app/1497460/view/524227425953909063),
  on later adjustments to collision handling, course-return guidance
  and a possible wrong starting position for the Lunardo race.
- P5: [Steam achievement record](https://steamcommunity.com/achievements/1497460),
  New Kid on the Block identifies the official opponent/clear
  relation; the traces establish the displayed Rep result.
- H1: [firsthand opening-route report](https://www.trueachievements.com/a577827/new-kid-on-the-block-achievement),
  corroborates the wheel, instruction, two laps and victory;
  its carrier does not establish the Windows build. Drafting, rather
  than a separate drift mechanism, is documented by the observed
  PC instruction and P3.
- W1: [fgw commercial PC walkthrough](https://www.youtube.com/watch?v=2i_stn1DFzs),
  published 8 August 2025, with product link and continuation
  through the whole game. Inspected static thumbnails for the
  ordinary scoped route.
- W2: [Video Game Universe full PC walkthrough](https://www.youtube.com/watch?v=SyytFaWQ97M),
  published 5 August 2025. Selected stills corroborate the acquired
  part, race card, final lap, winner and handoff.
- W3: [Daandigo first-session trace](https://www.youtube.com/watch?v=sPyjQ3Mf_AY),
  published 3 August 2025. Independent confirmation of the event
  and the separate rematch card, with installed version unverified.

### Reproducible route evidence

1. Ride to the first barrier with Kat and the already acquired
   bicycle. Talk to the Lunardo Boys boss. W2 4:00 shows the
   boss requiring his team before the race. The follow-on directs
   the rider to the beach; W1 6:00–6:40 shows the conversation
   there and the instruction to open and equip a part.
2. Open the designated box reachable behind the beach group.
   W2 6:10 shows Commuter Wheel as the new part and 6:20 shows a
   separate Back Wheel selection with the rusty and new alternatives.
   W1 6:50 shows the box objective and W1 7:00–7:10 shows the Bike
   ratings and fitted rear wheel. Fit there and resume with the
   same bike. One component changes while the other wheel and
   chassis remain. Do not infer the numerical rating formula.
3. Talk to the beach riders again and use the boost lesson.
   W1 7:20–8:40 shows dialogue and the held-boost instruction at
   8:20. Return up the marked road to the barrier. W1 9:30–10:00
   and W2 8:40–8:50 go from the regrouped crew to the first
   Lunardo Hill Boys card and rolling start.
4. Pedal, steer and brake to keep speed through the marked course.
   W1 10:10 pauses on the drafting lesson. Tuck behind one rider
   rather than colliding or riding abreast. Drafting contributes to
   the stored acceleration reserve; spend it separately when the
   line opens. W1 10:20 shows fourth place near another rider,
   10:30 shows second with active acceleration, and 10:40 shows
   first. These positions describe the example, not scripted
   starting or intermediate ranks for every attempt.
5. Use the next route marker, race minimap and chevrons to complete
   both laps. W2 9:50 shows the final-lap transition. Neither free
   exploration nor taking an early lead suffices to get the
   reward. W1 11:50 shows Winner 1st; 12:00 displays +1 Rep.
6. Continue through the reward panel. In W1 12:10–12:40 the
   boss conversation still displays the reputation point and opens
   access onward. Stop at that handoff. W3 19:50 separately shows
   Lunardo Rematch; W1 continues toward a later shrine, which has
   its own disclosure and upgrade.

Claim IDs: WW-001–WW-009. The timestamps are evidence addresses. They
do not define required split times for the race.

## Mechanical decomposition

### Action Genes

- ACT-008: steer the local rider with direct movement while
  travelling between the beach and barrier and when racing.
- ACT-309: hold the available acceleration command to spend the
  current reserve when accelerating along a chosen line.
- ACT-341: approach and open the indicated world part box to
  acquire its bicycle component.
- ACT-804: select the rear-wheel position and fit the owned
  wheel, retaining the rest of the same build.
- Claim IDs: WW-002–WW-006.

### System Behaviour Genes

- SYS-516: successive marked course passages advance the lap
  counter and settle the classified two-lap result.
- SYS-691: spend a bounded reserve independently of the action
  that earned it. Boost raises forward acceleration while active.
- SYS-765: ride within the useful following position of a moving
  cyclist to earn later acceleration charge.
- SYS-1775: integrate current contact for the two linked wheels
  and front-wheel steering with surface grip.
- SYS-1776: the fitted parts contribute to the current build
  ratings and resulting performance, beyond the moment of acquisition.
- Claim IDs: WW-003–WW-007.

### Constraint Genes

- CON-438: complete the marked circuit sequence and its two laps
  before the finish settles. No exact off-course recovery horizon
  or invalid-gate grace period is inferred.
- CON-848: each declared component position takes one compatible
  part. Front and rear wheel positions are separate.
- Claim IDs: WW-003, WW-004, WW-006, WW-007, WW-009.

### Information Genes

- INF-205: follow current place, lap marker, nearby rivals and
  course display during the race.
- INF-208: after the finish, distinguish the winning result from
  the separate race reward and its retained amount.
- INF-566: the live reserve and active boost indicator distinguish
  available charge from the current acceleration effect.
- Claim IDs: WW-005–WW-008.

### Objective Genes

- OBJ-134: win the first complete rival race and retain the
  tutorial reputation award at the return to the boss.
- Claim IDs: WW-006–WW-008.

### Time Genes

- TIM-003: rival positions and course motion advance after launch.
  Decide when to tuck in, steer across the line and spend the
  current reserve during that live progression.
- Claim IDs: WW-005, WW-006.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Boss alone at the barrier | Talk to the boss | The team must regroup; head to the beach | Reaching the barrier alone does not start the event | WW-002 |
| Part box available by the crew | Open the box | The Commuter Wheel becomes owned | Acquisition precedes fitting | WW-003 |
| Owned wheel and original fitted rear | Select it at Back Wheel | Only that position changes while the current bike remains active | Component choice affects the build | WW-003, WW-004 |
| Crew at the barrier after preparation | Accept the event | Enter the first marked two-lap race | The rematch is separately offered later | WW-002, WW-006, WW-008 |
| A rival is ahead on the live line | Follow within the drafting opportunity | The draft can charge the acceleration reserve | The moving opponent can be a source of boost | WW-005 |
| Charge exists and a line opens | Hold Boost while steering | Spend the reserve for forward acceleration | Spending and charging are different decisions | WW-005 |
| One marked lap completed | Continue through the live route | The final lap remains to be completed | First place at this point is provisional | WW-006 |
| Finish the two-lap route in first place | Continue from winner to rewards | Receive one Rep; later access permission is given in dialogue | The winning place and retained progression settle separately | WW-007, WW-008 |

## Strategic and experiential structure

A rival ahead can supply drafting charge while also occupying the
opening for an overtake. Delay spending until the rider can steer
through a useful line. The preparation changes the bike once,
before the moving contest, while drafting and boost change only
its temporary race state. The finish rewards placement and then
returns to the authored story handoff. Claim IDs: WW-002–WW-008.

## Replay and variation

The captures use different approaches and part menus but agree on
the first race, two laps, first-place goal and handoff. The Windows
capture texts do not expose an exact depot build. Later notes
describe updated collision behaviour and one Lunardo start-position
fix. They do not demonstrate that every variant of earlier contact,
missed gates or retry behaves the same. Claim IDs: WW-001, WW-006,
WW-008, WW-009.

## Adjacent systems and history

The introduction’s award is one Rep for the win. It does not
establish a time or KAT requirement for this first race. The
rematch has its own entry card and can award a part, as sampled
in W2 12:00–14:40. Later race requirements and shrine upgrades
are outside the first event. Claim IDs: WW-007–WW-009.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-309, ACT-341, ACT-804 | Steer, spend boost, open box and fit part |
| System Behaviour | SYS-516, SYS-691, SYS-765, SYS-1775, SYS-1776 | Classified finish, spend, drafting charge, wheel contact and fitted ratings |
| Constraint | CON-438, CON-848 | Course sequence and independent compatible positions |
| Information | INF-205, INF-208, INF-566 | Live progress, settled reward and boost state |
| Objective | OBJ-134 | Win and retain the result |
| Time | TIM-003 | Live relative position and response |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `602` (`GAME-0001`–`GAME-0602`).
- Exact genome matches: none.
- Tied near matches: `GAME-0242` — Asphalt Legends (`8 / 26 = 0.307692`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| Asphalt Legends (GAME-0242) | ACT-309, CON-438, INF-205, INF-208, SYS-516, SYS-691, SYS-765, TIM-003 | Both earn and spend a bounded acceleration resource on a live, ordered route. Asphalt Legends uses assisted path selection and nitro earned through driving technique. Wheel World steers the bicycle continuously, equips its replacement wheel first, drafts behind a rider and settles the first-place Rep. | 8 shared of 26, Jaccard 0.307692 |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_349](../../../research/taxonomy-changes/TAXONOMY_CHANGE_349.md)
  records five Active boundaries. Existing definitions are retained.

## Negative results

- SYS-540 and CON-457 require spatial boost-pad stock. Drafting
  earns charge from a moving relative position. ACT-309, SYS-765
  and SYS-691 cover charge and spend without a pad.
- SYS-892 resolves the charge on drift release. Following a cyclist
  earns a reserve for a later independent use.
- SYS-320 includes broad vehicle damage and occupant effects. The
  scope supports independent wheel grip and contact without that
  damage model.
- ACT-283 and CON-425 refer to mod sockets with other capacity
  and compatibility conditions. The bicycle uses typed physical
  positions rather than a shared drain budget.

## Delta summary

## New facts

- [Observation | Corroborated | High] The beach wheel is acquired,
  fitted to a named position and then taken into the first race.
  WW-002–WW-004.
- [Observation | Corroborated | High] Riding behind a rival earns
  a stored resource. A later command applies acceleration and
  spends the reserve. WW-005.
- [Observation | Corroborated | High] The first event finishes
  after two laps and a win awards one Rep before the onward
  conversation. WW-006–WW-008.

## New genes

- [Observation | Corroborated | Medium] ACT-804, SYS-1775,
  SYS-1776, CON-848 and INF-566.

## New combinations

- [Observation | Direct | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_349.

## New questions

- What are the exact order and tolerance rules when a rider
  misses a gate or rejoins the course?
- Which later tutorial prompts accept a differently fitted wheel?
- What does the first race preserve after a lower classified place
  followed by an ordinary retry?

## Next recommended game

- [Hypothesis | Limited | Medium] Selection 050 follows the
  parity closeout of the nine completed games in Selection 049.

## Why this game

- [Hypothesis | Limited | Medium] One opening event makes a
  functional component, a temporary following reward and a
  persistent race reward independently observable.
