---
game_id: GAME-0567
slug: superhot-vr
game_title: SUPERHOT VR
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-048
    - ACT-161
    - ACT-714
    - ACT-769
    - ACT-770
    - ACT-771
  system:
    - SYS-036
    - SYS-215
    - SYS-369
    - SYS-706
    - SYS-755
    - SYS-1659
    - SYS-1660
    - SYS-1661
  constraint:
    - CON-773
    - CON-833
  information:
    - INF-142
    - INF-543
  objective:
    - OBJ-029
  time:
    - TIM-037
---

# Game: SUPERHOT VR

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
A movement-to-time relation, bodily exposure, hand readiness, gun ammunition
and checkpoint-group clearance are different state boundaries. Enemy count,
physical reach, gun capacity, material and scene transform are parameters.

## Analysis scope

- Version / ruleset: original standalone Oculus Quest full retail release of
  21 May 2019, ordinary solo campaign, default pyramidless scene flow and
  original Touch controllers. The target is the released 2019 rules before
  the later v1.111 Airport enemy adjustment, not a May preview, the free demo,
  PCVR, PSVR, flatscreen SUPERHOT, MIND CONTROL DELETE or optical hand tracking.
  A 2019 post-launch recording and developer interview support common rules;
  they do not certify the launch binary or every intervening patch.
- Structured analysis target: PLAT-META-QUEST in
  knowledge/platforms/games.json. The official launch names the Quest product
  ID 1921533091289407. Its current store page is not a version-locked build
  and does not prove historical controls, platform parity or binary identity.
- Entry: the first active vignette of the complete early Airport checkpoint
  group, after the opening tutorial/Dojo setup is already completed. Use the
  ordinary campaign rather than Guest or an optional restored pyramid mode.
  The previous clear is setup; it is not another game loop inside this unit.
- Primary decision loop: inspect visible red attackers, bullet trajectories,
  reachable dark props and both hand states; physically move the head/body
  out of danger or behind cover while remembering that movement advances
  the world. Grip or catch a weapon, disarm a reachable enemy, aim and fire,
  punch or throw an eligible prop, or interpose a ready hand/held object.
  Reassess ammunition, hand readiness and surviving enemies before moving
  again. Continue through the whole authored group, not merely one kill.
- Positive exit: clear every successive Airport combat vignette and observe
  the checkpoint-group settlement and transition onward to Mall. The scope
  stops before taking part in Mall combat. No global campaign clear, optional
  speedrun, perfect style score or later MindWave unlock is required.
- Negative exit: an unprotected lethal hit ends the current attempt and
  returns to the group's authored retry anchor. Clearing an earlier vignette
  does not make every smaller scene its own checkpoint. No finite life stock,
  health bar, healing pickup or retained failed-attempt ammunition is assumed.
- Included: continuous physical head/body displacement and independent Touch
  hands; taking loose props, timed catches, direct hostile-weapon grabs,
  aimed firearm/tool attacks and tracked fist strokes; projectile/hostile
  combat, thrown-prop dynamics and impact, fragile-prop removal, actual-volume
  held-object bullet blocks and ready-hand protection/recovery; finite
  unreloadable physical guns, lethal player vulnerability, local visual and
  attack cues, all-hostiles clear, group retry, default Quest scene
  recenter/rotation and movement-scaled simulation time. Two held objects are
  the hand-count parameter, not a new inventory gene.
- Time boundary: stillness strongly slows enemies and projectiles, while
  reaching, aiming and evasion can advance their simulation. The marketing
  slogan does not establish exact zero progression, identical weighting of
  head and hands, or a universal twitch threshold. Hand recovery uses active
  game time; an exact duration or shared/per-hand quota is not certified.
  System menus and inactive transitions are not evidence of an alternate
  tactical pause, rewind or fixed independent combat clock.
- Excluded: the opening tutorial as an additional completed encounter, Mall
  and later locations, later unlocked remote MindWave/head-explosion attacks,
  campaign-ending metanarrative acts, HOTSWITCH body transfer from flatscreen,
  the original PCVR/PSVR within-level pyramid grab, alternate BIOS/Guest flow,
  postgame level-select, Endless, challenges and speedruns. No manual reload,
  ammo drops, joystick walking, optical hand tracking or health regeneration
  is invented. Exact builds, spawning counts/coordinates, hand recovery
  arithmetic, material damage thresholds, capacities and timing samples
  require a separate authorised native test.
- Potential scoped modules: later MindWave acquisition/recovery, full campaign
  metanarrative settlement, postgame challenge constraints, or comparing the
  original pyramid-based PCVR flow with default Quest transitions.
- Direct-play status: not conducted. Official launch text, published developer
  statements and written released-version accounts were read. Seven static
  ten-second storyboard sheets from the 31 August 2019 Quest recording V1
  were inspected without audio or video playback. They show physical combat,
  repeated lobby attempts and later location changes; their coarse sampling
  does not measure contacts, exact vignette count, launch patch or recovery.
  No headset, native input replay, emulator, foreground window or fullscreen
  playback was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SHV-001 | The full standalone Quest release launched on 21 May 2019; its default within-level flow removes transition pyramids. | Confirmed | Direct | High | P1, P2, P3 |
| SHV-002 | Tracked physical movement controls the rate of hostile/projectile progression; stillness strongly slows it. Exact zero floor and channel weights remain unverified. | Observation | Corroborated | High | P2, S1, S2; V1 presentation only |
| SHV-003 | Physical leaning, ducking and available room-scale movement alter the embodied viewpoint and exposure; this is not movement of a separate miniature avatar. | Observation | Corroborated | High | P3 developer statements, S1 |
| SHV-004 | Touch hands grip, throw, catch and strike; a close enemy-held weapon can be taken, disrupting its armed state without necessarily killing its owner. | Observation | Corroborated | Medium | P2, S1, S2; V1 |
| SHV-005 | Guns have finite shots without ammo-drop or manual-reload replenishment; an empty gun remains a physical prop. Thrown props resolve eligible impact; exact material/force lethality is not universalised. | Observation | Corroborated | Medium | P2, S2; V1 |
| SHV-006 | Held objects can intercept bullets, with fragile props and weapons having different outcomes. A ready bare hand can block and then shows unavailable/glitched defence until recovery; exact quota/duration remains unsettled. | Observation | Corroborated | Medium | S2, S3 indexed first-hand discussion |
| SHV-007 | An unprotected hit is lethal and failure restores a larger authored checkpoint group, not necessarily the immediately previous vignette. | Observation | Corroborated | Medium | S2, S4 indexed contemporary Quest accounts; V1 repeated attempts |
| SHV-008 | On default Quest, the next scene is automatically centered on current physical position and rotated to facing. All required hostiles and successive scenes must be cleared before the group is complete. | Confirmed | Corroborated | High | P2, P3; S2, S4 qualify group structure |
| SHV-009 | Airport is an early complete group before Mall, following the opening/Dojo material. Later remote head destruction is outside this group's legal options. | Observation | Corroborated | Medium | S2 location/ability guide; V1 lobby sequence and later environment change, not exact launch layout |

## Basic data

- SUPERHOT Team; the 2016 PCVR origin is distinct from this 2019 standalone
  platform target. No cross-platform binary or collision equivalence follows.
- Families: FAM-007 physics and object manipulation, FAM-009 tactical forecast
  and counterplay. Moving to act also moves the hostile clock; a free static
  turn is not available. These are reused independently supported families.
- Primary sources, accessed 2026-11-20:
  - P1: [official Quest launch announcement through Valve's original news API](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=617830&count=30&maxlength=0&enddate=1561939200),
    SUPERHOT Team, 21 May 2019, article titled SUPERHOT VR has just landed on
    Oculus Quest!, timestamp 1558451278. It links Quest product 1921533091289407.
    The separate Steam PC patch in the same feed is not a Quest build ID.
  - P2: [official Quest release teaser](https://www.youtube.com/watch?v=Q9qNP5EPFEE),
    SUPERHOT, 21 May 2019; its publisher description documents the full Quest
    game, physical combat, absent ammo drops and rebuilt pyramidless flow.
    Description/metadata were read; no video or audio playback is claimed.
  - P3: [published interview with producer Callum Underwood and programmer Luke Thompson](https://www.uploadvr.com/superhot-vr-new-life-quest/),
    9 July 2019. Their direct statements establish physical movement and
    recentered/rotated scenes, distinguish native redevelopment from simple
    PCVR parity and explain optional post-launch BIOS/save/Guest changes.
- Secondary sources, accessed 2026-11-20:
  - S1: [contemporary Quest review](https://www.uploadvr.com/superhot-vr-quest-review/),
    20 May 2019 review of the complete launch game, not the public demo.
    First-hand body movement and mid-air gun catches corroborate common rules;
    the pre-launch publication is not an owned release-binary measurement.
  - S2: [written VR mechanics and location guide](https://readyvrone.com/vr-gaming/superhot-vr-game-guide/),
    later cross-platform account. Used for grip/disarm, finite weapon, physical
    blocking, Airport-to-Mall order and later ability boundary. Its PC-style
    pyramids and exact later Airport behaviour are not imported into Quest.
    Conflicting broad claims about all thrown objects killing are not adopted.
  - S3: [July 2019 Quest hand-blocking discussion](https://www.reddit.com/r/OculusQuest/comments/chsmwq/),
    dated 25–26 July, indexed passages only, not a fully retrieved thread.
    Readiness loss and recovery are retained; a reported three-game-second
    duration is not certified or made part of the signature.
  - S4: [contemporary Quest checkpoint discussion](https://www.reddit.com/r/OculusQuest/comments/bvm92s/),
    1 June 2019, indexed passages only. It distinguishes several scenes from
    their larger retry group; rough user counts are not asserted as exact.
  - V1: [released Quest recording, Part 1](https://www.youtube.com/watch?v=QUZLtd5CJf4),
    Dave The Psycho, 31 August 2019, 1695 seconds. All seven available 5-by-5
    static storyboard sheets at ten-second intervals were visually inspected.
    Around the middle, repeated terminal/counter fights precede a Hacker Room
    break and later open interior scenes. This is supporting presentation,
    not an exact frame/input or native checkpoint experiment.
- Unavailable/limited evidence: the original detailed launch blog now fails
  retrieval; two additional contemporary review pages returned errors.
  Current store metadata and later patch notes cannot certify a 2019 binary.
- Claim IDs: SHV-001–SHV-009. No review score or player rating is imported.

## Mechanical decomposition

### Action Genes

- Reuse ACT-048 for gripping, spatially holding and releasing/throwing a free
  rigid prop; independent hand slots and release impulse are parameters.
  ACT-714 covers intercepting an already flying portable gun. ACT-161 covers
  aimed shots and equipped-tool strikes, not an automatic turret.
- ACT-769 supplies continuous embodied head/body displacement, ACT-770 a
  tracked clenched-hand stroke, and ACT-771 direct hostile-hand disarming.
  These differ from inspecting a fixed miniature, a button punch animation
  and picking up an object that was already free.
- Claim IDs: SHV-003–SHV-005.

### System Behaviour Genes

- SYS-036 handles released-prop motion while simulation time advances;
  SYS-706 handles attributed prop impact. No claim applies gravity or a
  particular force threshold to every bullet or thrown material.
- SYS-215 reuses continuously resolved direct combat; its time rate is owned
  by TIM-037, not silently replaced with fixed independent progression.
- SYS-755 removes eligible fragile world props after their break trigger;
  living red enemy defeat remains combat, not world-object destruction.
- SYS-1661 owns actual-volume held-object bullet interception; SYS-1660 owns
  ready bare-hand interception and recovery. A gun does not inherit a hand
  cooldown and an empty gun does not automatically lose blocker eligibility.
- SYS-1659 owns Quest automatic scene recentering and rotation. SYS-369
  restores the authored group anchor on failure, independently of a scene
  change after success. Enemy positions and props are re-established by that
  retry; failed-attempt projectile trajectories are not carried forward.
- Claim IDs: SHV-004–SHV-008.

### Constraint Genes

- CON-833 ties remaining shots to each physical firearm without refill or
  reload; its empty state preserves other prop uses. CON-773 reuses current
  vitality failure with a binary live/dead parameter. This does not invent
  a numeric health bar, a multi-hit pool, finite lives or healing supplies.
- Hand readiness is a state transition in SYS-1660, not a second invented
  resource gauge. Reach and the two-hand holding count parameterise actions.
- Claim IDs: SHV-005–SHV-007.

### Information Genes

- INF-142 reuses incoming attack cues; INF-543 distinguishes local visible
  spatial bodies, bullet paths, held objects and glitched hand readiness.
  Occlusion remains meaningful; no complete future enemy sequence or exact
  numeric recovery/ammunition display is inferred from stylised colours.
- Claim IDs: SHV-002, SHV-006.

### Objective Genes

- OBJ-029 reuses finite all-hostiles encounter clearance. The Airport group
  composes its finite successive vignettes; one cleared scene is insufficient
  if another required fight follows. Remaining enemy threats matter, not a
  score threshold, a survival timer or an optional style challenge.
- Claim IDs: SHV-007–SHV-009.

### Time Genes

- TIM-037 makes moving to defend or aim a change to the hostile/projectile
  time rate. It is not a consumable pause ability or turn-based AP economy.
  No TIM-003 fixed-independent progression is admitted merely because combat
  is continuously resolved. Tiny tracking noise and stillness floor remain
  unmeasured parameters rather than a promise of perfectly frozen time.
- Claim IDs: SHV-002, SHV-006.

## Reproducible transitions

These source-reconstructed conditions are falsifiable tests, not claimed native
executions or exact trajectories reproduced from a recording.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| A visible bullet threatens the current viewpoint. | Lean out of its line or behind solid cover. | Exposure changes; the movement also advances hostile/projectile simulation. | Evasion is physical and has a time consequence, not a free pause move. | SHV-002, SHV-003 |
| A reachable loose pistol and one free hand. | Grip it, aim and trigger a shot. | It becomes a held physical gun and spends its own eligible supply. | Grip state and shot availability are distinct. | SHV-004, SHV-005 |
| A weapon is already flying within hand reach. | Time the grab before it passes. | Eligible contact transfers the moving prop to held state. | Catch is not an automatic inventory refill. | SHV-004 |
| An armed hostile is close and a player hand is free. | Grab its eligible gun directly. | The weapon changes owner and the armed threat is disrupted; the owner need not be dead. | Direct disarm differs from loose pickup and lethal impact. | SHV-004 |
| A nearby enemy and an eligible clenched hand. | Drive the hand through the hostile. | The actual tracked stroke commits close combat contact. | A firearm trigger or idle open palm is not the same action. | SHV-004 |
| The held gun has fired its final available shot. | Try firing again, then interpose or throw the gun. | Another shot is unavailable; eligible physical blocker/throw uses remain. | Empty does not mean nonexistent or inert. | SHV-005, SHV-006 |
| An incoming bullet is headed toward the viewpoint. | Put an eligible held object's volume across its path. | Contact blocks it; fragile-prop break and retained weapon outcomes differ. | Actual spatial overlap and material matter. | SHV-006 |
| A hand is ready, then becomes glitched after a block. | Compare contact before readiness loss and during unavailability; let active game time advance. | The ready interception is protective; unavailable contact has no equivalent guarantee; recovery can restore eligibility. | No infinite shield or exact unmeasured cooldown is promised. | SHV-006 |
| Earlier Airport vignettes are cleared but a required scene remains. | Suffer an unprotected lethal hit. | The failed attempt restores the authored group anchor. | Every cleared small scene is not a new checkpoint. | SHV-007 |
| The current vignette has no required hostile remaining. | Let default Quest success flow proceed. | The next scene is recentered and rotated around current tracked pose without a pyramid grab. | Scene transform is neither joystick travel nor chosen teleport. | SHV-008 |
| All required Airport scenes are cleared. | Observe the group settlement and next-location transition. | The full scoped objective is complete; stop before Mall combat. | A first kill or first room does not replace the group. | SHV-009 |

## Strategic and experiential structure

- Local decision: moving a hand to obtain a better weapon or blocker also
  gives an already visible bullet time to approach. Choose exposure, reach
  and object utility together rather than treating aim as a frozen menu.
- Medium-term planning: preserve a useful physical gun/prop through the local
  attack, catch an incoming replacement and distinguish a still-ready hand
  from one already consumed by defence. No exact shared-hand quota is assumed.
- Long-term structure: complete every scene in the current authored retry
  group. Earlier groups are setup; postgame modes are not secretly required.
- Failure attribution: visible projectile geometry, the player's physical
  displacement, weapon exhaustion and hand unavailability explain different
  mistakes. Occluded attacks and coarse media limit retrospective certainty.
- Player-trust factors: official Quest flow takes priority over PCVR guide
  pyramids; uncertain exact coefficients remain explicit rather than guessed.
- Claim IDs: SHV-002–SHV-009.

## Replay and variation

- The authored group and available object classes supply the scenario; body
  path, timing, gun order, catches, disarms and throws permit alternate
  solutions. No procedural enemy randomiser or unique replay seed is claimed.
- Retry restores a group anchor, not a persistent local style/health economy.
  Postgame speed or challenge records are separate possible modules.
- Claim IDs: SHV-004–SHV-009.

## Adjacent systems and history

- The original flatscreen SUPERHOT and its VR counterpart are distinct
  products. HOTSWITCH and keyboard walking are not imported here. The current
  corpus has no earlier separately analysed flatscreen SUPERHOT record.
- PCVR/PSVR scene pyramids and later Quest BIOS options are not the chosen
  default 2019 flow. The later MindWave attack is not an early Airport action.
- Moss uses an independent Reader and a separate small avatar; these tracked
  hands belong to the embodied combatant instead. Their shared platform does
  not justify shared control definitions without a boundary match.
- Claim IDs: SHV-001–SHV-004, SHV-008, SHV-009.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | ACT-048, ACT-161, ACT-714, ACT-769, ACT-770, ACT-771 | Two hands and reach are parameters |
| System Behaviour | SYS-036, SYS-215, SYS-369, SYS-706, SYS-755, SYS-1659, SYS-1660, SYS-1661 | Material and scene transform are parameters |
| Constraint | CON-773, CON-833 | Binary vitality; exact shot counts unverified |
| Information | INF-142, INF-543 | No omniscient future script |
| Objective | OBJ-029 | All scenes in the bounded group |
| Time | TIM-037 | Movement mapping and stillness floor unmeasured |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `566` (`GAME-0001`–`GAME-0566`).
- Exact genome matches: none.
- Tied near matches: `GAME-0323` — Marvel’s Spider-Man 2 (`6 / 40 = 0.150000`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0323` — Marvel’s Spider-Man 2 | ACT-048, ACT-161, SYS-036, SYS-215, SYS-369, SYS-706 | Both carry physical props, direct aimed attacks, continuous combat and authored retry. Spider-Man controls a traversing avatar with its own fixed-time abilities and mission structure; Quest couples the embodied head/hands to world time, finite unreloadable guns and actual-volume interception, then recenters successive scenes. | Tied near: 6 / 40 = 0.150000 |

### Preserved research notes

- New genes: ACT-769–ACT-771, SYS-1659–SYS-1661, CON-833, INF-543 and TIM-037.
- Classification result: New gene.
- Evidence and reasoning: eleven reused definitions remain unchanged; nine
  additions isolate physical embodiment, direct disarm, hand and object
  interception, Quest scene flow, nonrefillable gun shots, local visual
  readiness and movement-scaled time. No new combination is presumed.

## Taxonomy impact

- Registry changes: nine new Active definitions; eleven reused unchanged.
- Taxonomy-change record: [TAXONOMY_CHANGE_313](../../../research/taxonomy-changes/TAXONOMY_CHANGE_313.md).
- No previous game signature, lifecycle, history or published mapping changes.
  This is an internal boundary addition, not an external novelty claim.

## Negative results

- None. Boundary-fit rejections are recorded in TAXONOMY_CHANGE_313; no earlier
  accepted conclusion is overturned merely by selecting a different carrier.

## Delta summary

## New facts

- [Observation | Corroborated | High] SHV-001–SHV-003 and SHV-008 distinguish
  original Quest embodied movement, coupled time and default scene alignment.

## New genes

- [Observation | Corroborated | Medium] Nine bounded additions in
  TAXONOMY_CHANGE_313; no exact native arithmetic is invented.

## New combinations

- [Observation | Corroborated | High] No new combination. Proper-subset results
  are owned by Corpus comparison rather than a genre label.

## Taxonomy changes

- [Observation | Corroborated | Medium] TAXONOMY_CHANGE_313 adds the new
  boundaries without revising older signatures or definitions.

## New questions

- Exact 2019 Quest build, checkpoint layouts, head/hand time weights, stillness
  floor, hand recovery accounting and prop-specific damage require authorised
  native evidence. Coarse frame inspection does not settle them.

## Next recommended game

- [Hypothesis | Limited | Medium] None: this is the ninth and final approved
  Selection 045 game. Finish batch parity and stop; no tenth is selected.
- Optimisation criterion: preserve the completed mixed-platform batch.
- Expected information gain: the final audit verifies accepted parity rather
  than deferring translation or changing prior research.
- Backlog impact: a new selection requires a separate user request.

## Why this game

- [Hypothesis | Limited | Medium] Native embodied combat exposes the cost of
  moving the hostile clock while reaching, shooting and defending, contrasting
  with the preceding DS chart's independently advancing musical timeline.
