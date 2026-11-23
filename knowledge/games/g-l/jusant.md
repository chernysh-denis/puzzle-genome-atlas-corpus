---
game_id: GAME-0552
slug: jusant
game_title: Jusant
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-114
    - ACT-341
    - ACT-363
    - ACT-531
    - ACT-610
    - ACT-750
  system:
    - SYS-036
    - SYS-112
    - SYS-661
    - SYS-665
    - SYS-1055
    - SYS-1597
    - SYS-1598
    - SYS-1599
  constraint:
    - CON-534
    - CON-536
    - CON-693
    - CON-819
  information:
    - INF-073
    - INF-075
    - INF-258
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Jusant

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Trigger labels, three pitons, hold positions, rope length and tower artwork are
parameters; they are not separate genes.

## Analysis scope

- Version / ruleset: original English Xbox Series X|S full-release campaign,
  October 2023 launch-rules profile, single player, Chapter 1 *Daymark*.
  Prescribe standard Xbox controller, default independent-hand climbing,
  default rappelling/interactions and stamina enabled. No simplified climbing,
  automatic jump grabbing or No Stamina mode. The official November 2023
  accessibility update establishes that these alternatives are separate
  settings, not the scope's ordinary rules. Exact installed native build,
  package hash, entitlement and save are unverified; no demo, PC/PS5 binary
  or cloud-stream session substitutes for the target.
- Primary decision loop: read reachable holds, rope geometry, remaining pitons
  and current/recoverable stamina; walk, alternate hand grips, jump, rest,
  place a piton or reel and swing toward the next supported ledge; recover
  equipment and capacity on stable ground, operate the route fixtures and
  continue to the chapter-top horn.
- Entry and exit: begin at first ordinary control at the base after the
  opening desert approach. Complete the first walls, stamina/net section,
  settlements, rope swings, bridge and exterior tower route; interact at the
  top and accept the horn/Ballast awakening and vine-opening transition.
  Stop at the handoff to Chapter 2 *Migration*, before its live traversal.
  Reaching an intermediate ledge, reading a letter or merely seeing the top
  does not finish the chapter. No full-campaign ending is claimed.
- Failure and recovery: releasing both grips or exhausting usable climbing
  stamina can lose the current hold. The attached safety line arrests the
  fall; reel, swing or regrip from that live suspended state. This is a local
  setback, not a health death, lost life or checkpoint snapshot restoration.
  Out-of-bounds bugs, exact zero-stamina grace, fall distance and recovery
  timing were not measured. Native save/reload persistence was not tested.
- Included: direct walking/jumping and camera control; independent hand
  channels on authored holds; three climb-local pitons and valid placement;
  story-path carabiner attachment and eligible aimed attachments; finite
  rope payout, length adjustment, directed swing and release; live gravity
  and contact; current stamina, jump-reduced capacity, requested wall rest,
  stable-ground capacity/equipment recovery; pull/bridge fixtures and the
  chapter-top interaction and resulting opening; visible body/terrain,
  equipment and stamina feedback. The end cutscene introduces Ballast;
  later player-commanded Echo is not imported into the first-climb signature.
- Excluded: optional letter, Bianca journal, shell and cairn detour accounting,
  collectible-completion achievements, later moving pebbles, heat/wind biomes,
  repeatable Ballast Echo guidance/vegetation puzzles, other chapters and
  full summit ending, survival food/weight, combat, lives and health damage,
  chapter-select cleanup, speedrun glitches and assisted-control variants.
  No universal rope metre count, stamina coefficient or exact grip solver
  is inferred. A new piton does not establish an unlimited new rope supply.
- Reproducible parameterisation: start a fresh released campaign with the
  prescribed default controls. Log supported surface, left/right grip,
  reachable next hold, current stamina and ceiling, jump/rest, current
  tether/anchor chain, paid-out length, remaining pitons, equipment recovery,
  opened bridge and chapter transition. Optional detours do not change the
  declared completion condition. Do not silently toggle assistance mid-run.
- Potential scoped modules: the first repeatable Ballast Echo route, one
  heat-exposed later climb, and the simplified/no-stamina profile need their
  own evidence and entry/exit contracts.
- Direct-play status: no Xbox, native executable, owned installation, input
  trace or save was used. Read official Xbox climbing guidance, developer
  product/release and patch material, SpecialEffect's controller study and a
  written Daymark route. Inspect eight public static storyboard sheets at
  ten-second sampling from GameSmyth's full Chapter 1 recording, without
  audio/video playback, foreground windows or focus changes. These support
  route, equipment, prompts and chapter handoff, not exact input timing,
  installed patch or certified native platform. Blocked secondary pages were
  not treated as fully read.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| `JUS-001` | Jusant's full release reached Xbox Series X and S on 2023-10-31; the chosen target is the released campaign, not the earlier demo. | Confirmed | Direct | High | P1, P2 |
| `JUS-002` | Default climbing separates hand grip/release channels from stick-directed reaching; releasing both loses support, while default rappelling uses bumper inputs. | Observation | Corroborated | High | P2, S1 |
| `JUS-003` | Movement drains usable stamina, jumps reduce its recoverable ceiling, wall rest refills only to that ceiling and stable standing ground restores full capacity. | Observation | Corroborated | High | P2, S2, V1 |
| `JUS-004` | Story-path auto-attachment and placed pitons protect local progress; three pitons are consumable within a climb and renewed after stable-ground line recovery. | Observation | Corroborated | High | P2, S2, V1 |
| `JUS-005` | A valid tether supports controllable reel/swing/release traversal and bounds reach by finite line geometry; no exact length or reset-on-every-piton rule is certified. | Observation | Corroborated | High | P3, S1, S2, V1 |
| `JUS-006` | Daymark teaches the wall/net and swing route, opens a bridge through its reachable upper attachment, and ends with the horn/Ballast scene and next-chapter vegetation opening. | Observation | Corroborated | High | S2, V1 |
| `JUS-007` | The November accessibility update adds simplified climbing/interactions, alternate rappel, jump assistance and disabled stamina; these do not define the prescribed default profile. | Confirmed | Direct | High | P3, S1 |
| `JUS-008` | Documentary reconstruction and sparse frames cannot prove native build, physical input timing, save restoration fields or exact solver equations. | Observation | Direct | High | R1 |

## Basic data

- Release / origin: DON'T NOD, full release 2023-10-31. No current subscription
  availability or purchase entitlement is asserted.
- Platform or physical form: `PLAT-XBOX-SERIES`, single-player controller
  campaign. The structured analysis target owns platform/edition identity.
- Mechanical families: physics and object manipulation; world topology and
  perspective; real-time system pressure.
- Primary sources, checked 2026-11-19:
  - **P1:** [DON'T NOD launch release](https://dont-nod.com/wp-content/uploads/2023/11/EN_Jusant_Launch.pdf),
    for the full-release date and platforms, not present subscription status.
  - **P2:** [Xbox Wire climbing guidance](https://news.xbox.com/en-us/2023/10/31/jusant-climbing-tips/),
    launch-day hand controls, three pitons, safety tether and two stamina layers.
  - **P3:** [Official accessibility patch 1.04](https://support.dont-nod.com/hc/en-gb/articles/14957643453853-Jusant-Patch-1-04-The-Accessibility-Update-November-2023),
    for separate assist modes and acknowledged maximum-rope animation;
    its later web update date is not a newly dated game release.
  - **P4:** [Developer product page](https://dont-nod.com/en/games/jusant/),
    for route exploration, tool use and Ballast's later nature relationship.
- Secondary/documentary sources:
  - **S1:** [SpecialEffect controller/accessibility study](https://gameaccess.info/jusant-gameplay-accessibility-options/),
    first-hand default versus assisted controller examples, not a claimed
    launch-native binary inspection.
  - **S2:** [Dave Acuña's Daymark route](https://sirusgaming.com/jusant-walkthrough-chapter-1-daymark/),
    2023-11-02, chapter route and ground/rest distinction. Input descriptions
    are checked against official/SpecialEffect controls rather than adopting
    its ambiguous directional-pad wording.
  - **V1:** [GameSmyth complete Daymark recording](https://www.youtube.com/watch?v=a5NMU6C6P5U),
    30:42, eight static sheets at ten-second spacing. Ordinary control near
    02:40; walls, net and stamina teaching before 09:00; swing/fixture route
    through settlements; exterior tower climb near 26:00–28:40; horn and
    companion/vegetation transition about 28:40–30:30. Collectible detours
    shown in the recording are not mandatory scoped objectives. Xbox-style
    prompts support controller presentation but do not certify the binary.
  - **R1:** review boundary above. Neoseeker/Video Chums returned 403 and
    TrueAchievements 402; no restricted article body was bypassed or adopted.
- Claim IDs: `JUS-001`–`JUS-008`.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for walking/jumps, `ACT-114` for independent hand channels,
  `ACT-341` for reachable route fixtures, `ACT-363` for piton placement,
  `ACT-531` for aimed tether/reel/swing/release and `ACT-610` for camera framing.
- Add `ACT-750` for a requested stationary wall rest. Neither an inventory
  restorative nor timed sleep represents this input. Do not also count the
  single-channel grip `ACT-362`, whose boundary excludes independent hands.
- Parameters: default triggers, left stick/free hand, bumpers, X/piton, LS/rest,
  current hold and legal ground/fixture. Claim IDs: JUS-002–JUS-006.

### System Behaviour Genes

- Reuse `SYS-036` for gravity/contact, `SYS-661` for stamina-bounded surface
  attachment, `SYS-665` for the temporary deployed support and `SYS-1055`
  for adjustable swings. `SYS-112` covers accepted fixture operations that
  persistently open the bridge and the chapter's successor route.
- Add `SYS-1597` for recoverable reserve versus jump-eroded ceiling,
  `SYS-1598` for live fall arrest without world reset, and `SYS-1599` for
  supported recovery of the finite temporary-anchor allowance.
- Resolution order: establish legal support/attachment; resolve reach and
  input; debit movement/jump costs; update body/line contact; resolve release
  or exhaustion into the attached suspended state; rest within the remaining
  ceiling or regain stable ground and equipment; operate the required route
  fixture; settle the chapter transition. Exact same-frame ordering is unknown.
- Claim IDs: JUS-002–JUS-006, JUS-008.

### Constraint Genes

- Reuse `CON-534` for reachable stamina-priced holds, `CON-536` for stock and
  legal piton terrain, and `CON-693` for reachable compatible tether anchors.
- Add `CON-819` for finite connected payout. Anchor eligibility, remaining
  pitons, line length and stamina are different rejection reasons. No piton
  creates unlimited line, and no numeric universal length is asserted.
- Claim IDs: JUS-002–JUS-005.

### Information Genes

- Reuse `INF-073` for remaining equipment uses, `INF-075` for current stamina
  and its ceiling, and `INF-258` for hold/body/terrain and safe-ledge feedback.
  Sparse prompts and local geometry are not an omniscient solved route.
- Claim IDs: JUS-002–JUS-006.

### Objective Genes

- Reuse `OBJ-026`: make the connected route and reach/interact at the first
  tower's chapter terminal. The required interaction and successor opening
  belong to that location objective; no combat victory or collection quota.
- Claim IDs: JUS-006.

### Time Genes

- Reuse `TIM-003`: movement, stamina use and suspended-body motion resolve
  while control remains live. No global stage deadline, rhythm score,
  turn queue or player-controlled rewind is imported.
- Claim IDs: JUS-002–JUS-005.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| One hand holds a legal projection; another is free | Aim the free hand and hold its trigger, then release the older grip | The new attachment carries continued ascent | Independent grip requests differ from one automatic climb input | JUS-002 |
| Both hands support the body on a wall | Release both | Connected rope arrests the fall and leaves a suspended body | Not a lost life or checkpoint reload | JUS-002, JUS-004 |
| A jump has reduced maximum recoverable stamina | Stop and request wall rest | Current stamina rises only to the reduced ceiling | Wall rest cannot erase all jump fatigue | JUS-003 |
| The same reduced ceiling remains | Reach stable standing ground | Full capacity/reserve returns | Ground recovery differs from wall rest | JUS-003 |
| A legal wall and at least one piton remain | Place a piton, then attempt a risky transfer | A new local safety point limits lost height on a subsequent slip | Placement uses stock and changes support, not a save snapshot | JUS-004 |
| Temporary anchors were spent in a climb | Stand securely and recover the rope | Anchors return for the next segment | Climb-local stock differs from permanent inventory loss | JUS-004 |
| A valid tether hangs beside a gap | Pay out/reel, steer laterally, release toward a reachable ledge | Arc and release trajectory determine the transfer | Adjustable swing is not an automatic endpoint pull | JUS-005 |
| Connected geometry exhausts available line | Try to climb farther without changing that geometry | Rope bounds the extension | A piton alone does not certify a fresh unlimited supply | JUS-005 |
| Bridge attachment cannot be reached from below | Take the upper route and operate it from the higher room | The bridge becomes traversable | Reach and persistent fixture state matter | JUS-006 |
| Chapter top reached, required interaction not settled | Complete the horn/companion transition | Vegetation opens the successor route | A vista or optional letter is not completion | JUS-006 |

## Strategic and experiential structure

- Local decision: maintain one reliable hold while reaching, or trade a
  jump's short-term distance against reduced recovery headroom.
- Medium-term planning: place a piton before a risky transfer, choose useful
  swing length and seek true standing rests rather than repeating wall rests.
- Long-term structure: complete one authored chapter; no colony economy,
  character upgrade tree or full-campaign optimisation is admitted.
- Failure attribution: visible body, grip, line and meter feedback explain
  many local setbacks; exact native solver and grace timings remain unknown.
- Player-trust factors: the tether preserves a live recovery opportunity;
  three pitons renew between climbs. No health-death tax or time-pressure
  claim is invented merely because the controls run in real time.
- Claim IDs: JUS-002–JUS-006, JUS-008.

## Replay and variation

- Daymark is authored, not a claimed procedurally generated daily tower.
  Hold choices, rests, pitons and transfer timing may vary within the route.
- Optional cultural objects support exploration, but their collection ledger
  and achievement settlement are separate from this chapter-completion scope.
- Claim IDs: JUS-006; route-choice interpretation is Hypothesis/Corroborated/High.

## Adjacent systems and history

- Human: Fall Flat independently controls hands but does not establish this
  two-layer stamina and safety-line recovery contract. PEAK's survival
  capacity, carried loot and unconsciousness are not imported.
- LittleBigPlanet 2 supplies a reusable adjustable-swing boundary; its electric
  deaths and checkpoint restoration are absent here. These are boundary
  counterexamples, not a substitute for the computed selected-neighbour scan.
- Claim IDs: JUS-002–JUS-008 and cited unchanged gene definitions.

## Normalised genome

| Type | Active gene IDs | Parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-114, ACT-341, ACT-363, ACT-531, ACT-610, ACT-750 | Hands, controller, holds, piton, camera, rest |
| System Behaviour | SYS-036, SYS-112, SYS-661, SYS-665, SYS-1055, SYS-1597, SYS-1598, SYS-1599 | Grip, tether, reserve/ceiling, temporary anchors, bridge |
| Constraint | CON-534, CON-536, CON-693, CON-819 | Reach, stock, material and finite connected payout |
| Information | INF-073, INF-075, INF-258 | Equipment, stamina and body/terrain cues |
| Objective | OBJ-026 | Whole Daymark terminal and successor transition |
| Time | TIM-003 | Live control, no global deadline |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `551` (`GAME-0001`–`GAME-0551`).
- Exact genome matches: none.
- Tied near matches: `GAME-0394` — LittleBigPlanet 2 (`7 / 30 = 0.233333`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| GAME-0394 LittleBigPlanet 2 | ACT-008, ACT-341, ACT-531, CON-693, OBJ-026, SYS-1055, TIM-003 | Both connect an authored route using fixtures, aimed reusable tether, reel/swing/release and live traversal toward an exit. LBP2 additionally admits bounce pads, acquired hook gating, optional contact pickups and lethal checkpoint return. Daymark adds independent hands, two-layer exertion, pitons, live fall arrest and supported stock renewal without importing death or collectible goals. | Near, `0.233333`; unique positive maximum |

### Preserved research notes

- New genes: `ACT-750`, `SYS-1597`, `SYS-1598`, `SYS-1599`, `CON-819`.
- Classification result: `New gene`.
- Evidence and reasoning: known hand, climb, swing, placement and fixture
  boundaries remain unchanged. The new input/recovery/capacity/payout rules
  are separately falsifiable and do not rename scenery or a meter quantity.

## Taxonomy impact

- Registry changes: five new Active definitions, no earlier mutation.
- Taxonomy-change record: [TAXONOMY_CHANGE_298](../../../research/taxonomy-changes/TAXONOMY_CHANGE_298.md).
- Candidate terms affected: no untyped candidate or unresolved scope debt.

## Negative results

- None. Rejected borrowed mechanics are scoped counterexamples, not an
  unsupported universal novelty or absence claim.

## Delta summary

Five typed rules extend a complete first-chapter reconstruction. Existing
signatures, release mappings and published corpus history remain unchanged.

## New facts

- [Observation | Corroborated | High] JUS-003 distinguishes recovery reserve
  from jump-reduced capacity; JUS-004 distinguishes live tether protection
  and renewed temporary anchors from lethal checkpoint restoration.

## New genes

- [Observation | Corroborated | High] ACT-750, SYS-1597–SYS-1599 and CON-819
  separate requested rest, capacity, safety recovery, stock renewal and payout.

## New combinations

- [Observation | Direct | High] None; all 274 verified subsets are scanned.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_298 adds only the five
  bounded definitions; no previous definition or signature is rewritten.

## New questions

- Which native revision is available for a licensed replay, and what are its
  exact grip-exhaustion grace and line-recovery state fields?
- How do later Echo, moving surfaces and weather change the same climbing loop?

## Next recommended game

- [Hypothesis | Limited | High] GAME-0553 *The Lost Vikings*, original SNES.
- Optimisation criterion: preserve Selection 044's alternate-era/platform order.
- Expected information gain: deliberate three-character role handoffs instead
  of one body with independent hand channels and safety-line physics.
- Backlog impact: retain the remaining six approved subjects without replacement.

## Why this game

- [Hypothesis | Corroborated | High] A fully released Xbox climbing chapter
  tests reuse across hand physics, authored fixtures and stamina-constrained
  traversal while isolating forgiving tether recovery from survival death.
