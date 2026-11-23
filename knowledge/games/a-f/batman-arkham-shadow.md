---
game_id: GAME-0662
slug: batman-arkham-shadow
game_title: "Batman: Arkham Shadow"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-429
    - ACT-877
    - ACT-878
  system:
    - SYS-215
    - SYS-789
    - SYS-1903
    - SYS-1904
  constraint:
    - CON-282
  information:
    - INF-309
    - INF-310
    - INF-610
  objective:
    - OBJ-351
  time:
    - TIM-003
---

# Game: Batman: Arkham Shadow

Comparison uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Officer names, the headset and the individual bonuses are scoped parameters.

## Analysis scope

- Version / ruleset: English commercial native Meta Quest 3
  release of Camouflaj's base game, Meta app 3551691271620960,
  launch-period 2024 rules. Use a fresh Story run on Hard with
  the Immersive VR preset and tracked controllers. The exact
  binaries and individual accessibility overrides were not verified.
- Structured analysis target: PLAT-META-QUEST in
  `knowledge/platforms/games.json`, with the Quest 3 headset
  specified in the edition. The Quest 3S trace is corroborating
  evidence for observed shared behaviour, outside the target edition.
- Entry: after the earlier sewer tutorials, reach the upper
  overlook of the first room with two officers tied together.
  One eligible target below exposes the contextual Glide Kick.
- Primary decision loop: identify the live room threat set,
  enter from above, move to eligible targets through tracked
  strike inputs, follow the current target's prompts and respond
  to eligible incoming attacks. After the combat result, use the
  Batarang on the common rope and let the objective advance.
- Exit: the first pair have stood up and the objective changes to
  Find officers Pettit and Marks while movement remains available.
  Stop before continuing down the next passage.
- Included: the optional Detective Vision inspection, descent
  attack, live combat and prompt-driven gesture strings, attack
  and counter target cues, the four-opponent result, the distinct
  rope interaction, the officers' recovery and the next objective.
- Excluded: training simulations before the room, earlier levers
  and ducts, the later pair and sewer exit, exact pose or timing
  thresholds, optional achievements, upgrade purchases, later
  equipment, reload behaviour, the full chapter, other difficulty
  presets, other games, DLC, standalone challenge rooms and ports.
- Potential scoped modules: the later armed room and second pair,
  the opening combat teaching simulation or one documented
  alternative comfort preset.

## Direct-play status

No headset play or entitlement check. Meta and Camouflaj identify
the product and explain the combat design. Still frames and screen
text from two attributed first-week or early-November commercial
runs establish the room. Media was inspected in the background
without sound. Raw controller motion, installed build hashes,
failed guard clearance and save reload were unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| AS-001 | Camouflaj released the base game on Quest 3 and 3S in October 2024. The analysed run identifies Quest 3, Hard and the Immersive VR preset. | Observation | Corroborated | High | P1, P2 and the W1 source description. |
| AS-002 | The first hostage chamber contains a tied pair and a set of four unarmed opponents. Detective Vision exposes the composition. An eligible lower target offers Glide Kick from the upper approach. | Observation | Corroborated | High | W1 19:46 and 20:04–20:13, W2 14:46–15:29. |
| AS-003 | Punch-To detects a tracked gesture and moves the avatar to an eligible opponent as part of the strike. It is distinct from manually walking into literal controller contact range. | Observation | Corroborated | High | P3 sections on Punch-To gesture detection and impact timing, W1 20:26–20:31, W2 15:35–15:39. Exact thresholds were unverified. |
| AS-004 | Combat follow-ups show direction or count on the addressed opponent. A cyan incoming-attack cue refers to a separate threat and can cause a change of target on a successful response. | Observation | Corroborated | High | P3 sections on Offscreen Counters and Rhythmic Combos, W1 20:24 and 20:39–20:43, W2 15:42–15:47 and 15:54–16:02. |
| AS-005 | Accepted follow-ups advance their target-local pattern while a separate running multiplier counts the ongoing chain. The count cue can shrink without closing the encounter. | Observation | Corroborated | High | P3 sections on Freeflow and Rhythmic Combos, W1 20:16–20:48, W2 15:40–16:00. |
| AS-006 | The W1 fight settles for 865 XP with max combo 34, seven move types, one gadget type and both clean bonuses. W2 settles for 785 XP with max combo 36, five move types and both clean bonuses, without a gadget bonus. Both receipts list four Rats. | Observation | Corroborated | High | W1 20:51–20:57, W2 16:05–16:08. Bonus amounts are the observed values for this room. |
| AS-007 | After the combat receipt the officers are still tied. A separate release objective appears. The Batarang addresses the shared rope, then the pair are able to stand. | Observation | Corroborated | High | W1 20:52, 21:18–21:28 and W2 16:06–16:23. |
| AS-008 | After the pair recover and speak, the objective changes to finding Pettit and Marks. The player can turn and move with the first room still present. | Observation | Corroborated | High | W1 21:47–21:54, W2 16:38–16:44. This is earlier than the full sewer exit. |

## Basic data

- Release / origin: Camouflaj and Oculus Studios, commercial
  single-player VR story for Meta Quest 3 and 3S. Target Quest 3
  with motion controllers. The store lists October 21 and the
  studio launch notice is dated October 22, 2024.
- Puzzle family: real-time system pressure (FAM-010). The player
  chooses among live target, follow-up and counter decisions as
  attacks progress. The rope and its eligible tool are an inventory
  and fixture dependency (FAM-013) after clearance.
- P1: [Meta Horizon Store, product 3551691271620960](https://www.meta.com/experiences/batman-arkham-shadow/3551691271620960/).
  The product page is a legal destination and identifies the full
  release and supported device family. Its current version display
  cannot date or authenticate footage.
- P2: [Camouflaj's launch notice](https://www.camouflaj.com/?p=840).
  Dated October 22, 2024. Describes both headsets and the commercial
  launch. [Meta's launch announcement](https://www.meta.com/blog/meta-connect-2024-content-recap/)
  corroborates its October 22 date independently of the store field.
- P3: [Camouflaj's GDC session](https://gdcvault.com/play/1035681/Punching-Across-the-Room-in)
  and its [design slides](https://media.gdcvault.com/gdc2026/Slides/Darcey_Ryan_Punching%2BAcross%2Bthe%2BRoom%2Bin%2BBatman_%2BArkham%2BShadow.pdf),
  presented by design director Ryan Darcey and gameplay engineer
  Troy Johnsen. Punch-To, Offscreen Counters, Freeflow and Rhythmic
  Combos ground the mechanism. Later deck examples do not prove
  every option exists in this early room.
- W1: [Batman Arkham Videos, Chapter 1 on Quest 3](https://www.youtube.com/watch?v=Xy10ZhiEsK8&t=1186s),
  uploaded October 21, 2024 on the source's stated time zone. The
  scoped stills run from 19:46 through 21:54. The description
  identifies Hard, Immersive VR and Meta Quest 3.
- W2: [The Arkham Channel, part 1 on Quest 3S](https://www.youtube.com/watch?v=nSzGb-IhGwE&t=886s),
  uploaded November 4, 2024 on the source's stated time zone.
  Uses Hard and Immersive VR. Its 14:46–16:44 stills independently
  establish the same observed terminal with a different XP receipt.
- Claim IDs: AS-001–AS-008.

### Reproducible route evidence

1. In the English Story, follow the opening sewer path beyond
   the combat tutorials to the upper approach of the first room
   holding a tied pair. W1 19:46 activates Detective Vision. Its
   overlay shows the hostage silhouettes and four hostiles, all
   unarmed. W1 20:07 shows the same arena from above in ordinary
   vision with the contextual Glide Kick cue.
2. Use that game command on the marked lower opponent to land
   in the group. W1 20:10–20:13 and W2 15:25–15:29 show the
   descent and the chain beginning. The viewport reaches the
   target before free floor combat continues. This is the
   visually evidenced route, with no requirement to use it for
   every successful entry inferred.
3. Address the current eligible opponent with the tracked strike
   control. The avatar closes the gap as part of the action.
   Respond to a local direction or count as the next part of
   the string, and read the separate incoming-attack cue when
   choosing whether to counter another target. W2 15:44 shows a
   remaining count and an incoming cue together. W1 20:39–20:43
   shows the continuing encounter switching its focal opponent.
4. Resolve all four opponents and read the Combat Summary.
   W1 20:52 shows 100 XP for the four Rats, 340 for max combo,
   175 for variety, 50 for gadget variety and 100 each for
   No Hit and Perfect Freeflow, for 865 XP. W2 16:06 shows 100,
   360, 125 and the same two 100 XP bonuses, for 785 XP, with no
   gadget row. The longer chain in W2 did not yield the higher
   total. At this point the two officers are still restrained
   in both recordings.
5. Move to the officers when the separate release objective is
   available. Direct the in-game Batarang at the shared rope.
   W1 21:20–21:23 shows the held tool and the transition to an
   absent rope. Both officers rise. W2 16:14–16:23 shows the
   same order. Wait through their immediate exchange. W1 21:48
   and W2 16:39 show the next search for Pettit and Marks, with
   the player able to turn. Stop in this retained room state.

## Mechanical decomposition

### Action Genes

- ACT-008: take local control of view and position to enter the
  room and move from the settled arena toward the tied pair.
  AS-002, AS-007.
- ACT-161: select the equipped Batarang and aim it at the eligible
  in-game restraint. The actual release belongs to the system
  rule, distinct from committing the aimed item action. AS-007.
- ACT-429: respond to a prompted incoming close attack with its
  eligible reactive counter. A nearby hostile can take over
  attention while another target's string is active. AS-004.
- ACT-877: a recognized Punch-To selects the opponent and starts
  an assisted approach as part of the strike. AS-003, AS-004.
- ACT-878: commit the visible contextual descent attack to the
  eligible opponent below. AS-002.

### System Behaviour Genes

- SYS-215: committed real-time attacks and counters settle contact
  and reduce the finite set of live room opponents. AS-003, AS-006.
- SYS-789: accepted combat actions extend the visible uninterrupted
  chain. On room clearance, its peak and the action variety contribute
  to the XP award alongside separate bonuses. AS-005, AS-006.
- SYS-1903: accept the next tracked strike against the current
  target's shown direction or count to progress the specific local
  pattern. It is independent of the accumulated multiplier.
  AS-004, AS-005.
- SYS-1904: one compatible action resolves the shared restraint,
  so both associated characters can resume movement. AS-007.

### Constraint Genes

- CON-282: ordered story gates present the room's guard clearance,
  then the separate release step, then the next search objective.
  Neither completed trace credits the next objective from combat
  settlement alone. AS-006–AS-008.

### Information Genes

- INF-309: the focused overlay behind the rail exposes four unarmed
  hostiles and separates them from the captives. AS-002.
- INF-310: the brief cyan signal classifies an incoming counter
  opportunity, separate from the prompt on the current target. AS-004.
- INF-610: the addressed opponent displays the expected next
  direction or remaining count and reflects accepted progress.
  AS-004, AS-005.

### Objective Genes

- OBJ-351: clear the local guards, free their captive pair and
  reach the next search objective in the same controllable room.
  AS-006–AS-008.

### Time Genes

- TIM-003: the room's hostile actions and counter opportunities
  advance while the player is choosing and performing gestures.
  AS-004, AS-005.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Upper approach and concealed composition | Activate Detective Vision | Captive outlines and four unarmed hostiles displayed | AS-002 |
| Eligible target below | Accept contextual Glide Kick | Assisted descent hits its addressed target and the finite fight proceeds | AS-002 |
| Out of immediate contact | Commit Punch-To to eligible opponent | Automatic approach and virtual contact | AS-003 |
| Target-local count or direction with ongoing pressure | Act on that cue or answer the incoming attack | Pattern progresses or attention transfers to a reactive counter | AS-004, AS-005 |
| Four defeated and encounter evaluated | Combat Summary awards XP | Pair still tied and eligible for the distinct release step | AS-006, AS-007 |
| First pair still tied | Compatible Batarang action on their rope | Both recover and stand, then a distinct search becomes current | AS-007, AS-008 |

## Strategic and experiential structure

The reading problem shifts from which targets are present to
which clue needs the next input. The current pattern has its own
progress ring or arrows, while a counter cue can pull attention
to an incoming opponent. The reward recognises variation as well
as continuity. The observed receipt is an encounter boundary,
and targeting the rope is a separate narrative interaction.

## Replay and variation

Two recorded routes use the same four opponents and release but
settle different maximum chains and move variety. Both satisfy
the objective. The difference in receipts grounds outcome
variation without requiring that XP affect eligibility. The
consequences of a failed attempt or reload were not measured.

## Adjacent systems and history

Earlier rooms separately teach combat and traversal. The later
armed rooms, stealth tools, second officers and street return
extend beyond this scope. The input implementation differs from
the button-driven Windows Arkham Asylum opening, while timed
counters, focused actor classification and post-fight chain
evaluation can reuse those existing definitions.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-161, ACT-429, ACT-877, ACT-878 | Move, address a target, counter, commit tracked approach and descend to strike |
| System Behaviour | SYS-215, SYS-789, SYS-1903, SYS-1904 | Resolve live combat, award chain XP, match the current pattern and release both captives |
| Constraint | CON-282 | Order guard clearance, rope release and successor objective |
| Information | INF-309, INF-310, INF-610 | Classify threats, signal a counter and expose the next target-local input |
| Objective | OBJ-351 | Free the first pair and retain the next search objective |
| Time | TIM-003 | Act while the current encounter advances |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `661` (`GAME-0001`–`GAME-0661`).
- Exact genome matches: none.
- Tied near matches: `GAME-0255` — Batman: Arkham Asylum Game of the Year Edition (`9 / 39 = 0.230769`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Batman: Arkham Asylum Game of the Year Edition (GAME-0255)](batman-arkham-asylum-game-of-the-year-edition.md) | ACT-008, ACT-161, ACT-429, CON-282, INF-309, INF-310, SYS-215, SYS-789, TIM-003 | Both turn target choice and timed counters into a live chain, classify hostiles in a vision mode and settle experience at a room boundary. Asylum separates keyboard or mouse attack input, grapnel traversal and a longer authored facility route. Shadow uses tracked target approach and visible local strike strings, then releases two officers by their shared restraint. | Near, `0.230769` |

## Taxonomy impact

ACT-877 commits locomotion and contact together through a tracked
gesture, whereas ACT-161 can address an object without moving the
body. ACT-878 couples a prompted descent to a lower opponent.
ACT-430 moves to an eligible anchor without requiring an attack.
SYS-1903 consumes a target-specific pattern, while SYS-789 is the
separate chain and settlement rule. INF-610 makes that local
requirement visible, unlike INF-310, which addresses an incoming
attack. SYS-1904 releases both actors linked by one rope, unlike
SYS-1734's released companion with a separate reassurance state.
OBJ-183 requires a transport extraction into another mission.
OBJ-351 uses the distinct release and retained objective in
the same area. No universal rule for campaign transitions follows.

## Negative results

- Defeating all four Rats and receiving the XP summary leaves
  the first pair bound. The summary is not the terminal.
- Two different max-combo and XP results advance to the same
  next search. Neither demonstrated a required XP minimum.
- A counter cue differs from the active target's next-strike
  instruction and a combat multiplier differs from its count.
- Hardware labels and settings come from the recorded authors.
  Exact executable identity, motion thresholds and reload state
  remain unverified.

## Delta summary

Fifteen scoped genes, six additions and nine reused boundaries.
All earlier signatures and verified combinations are preserved.

## New facts

- One tracked motion can commit both a virtual approach and a strike.
- Target-local gesture prompts coexist with a distinct incoming
  counter signal and a room-level chain receipt.
- The completed fight and the shared restraint are separate gates.

## Principles and design implications

Keep next-input prompts near the current target and make an
interrupting alert visually distinct. Make the scope of rewards
clear at the encounter boundary. A separately addressed rope
can preserve an explicit release decision after the fight.

## Puzzle or game generation potential

In a virtual chamber, give an active target a short visible
pattern and let a competing event interrupt it. Score the accepted
actions when the room settles. Require one shared release point
before crediting the next objective.

## New genes

- ACT-877
- ACT-878
- INF-610
- OBJ-351
- SYS-1903
- SYS-1904

## New combinations

No subset of the scoped genes supports any of the 274 verified combinations.

## Taxonomy changes

[TAXONOMY_CHANGE_408](../../../research/taxonomy-changes/TAXONOMY_CHANGE_408.md).

## New questions

Which cue states survive an interruption and return to the same
target? How do comfort settings change visual motion during Punch-To?
Does the successor objective persist after reloading the previous slot?

## Next recommended game

Gitaroo Man, the original commercial English North American
PlayStation 2 edition. Follow one first-stage song through its
playable phases, accepted graded result and successor state.

## Why this game

One room separates the motion-to-target action, local input
pattern, incoming threat, XP evaluation and final interactive
rescue without requiring a full-chapter completion.
