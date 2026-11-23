---
game_id: GAME-0608
slug: dosa-divas
game_title: "Dosa Divas"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-019
    - ACT-091
    - ACT-123
    - ACT-222
    - ACT-223
    - ACT-341
    - ACT-808
  system:
    - SYS-358
    - SYS-362
    - SYS-1138
    - SYS-1784
    - SYS-1785
    - SYS-1786
    - SYS-1787
  constraint:
    - CON-710
    - CON-851
  information:
    - INF-142
    - INF-573
  objective:
    - OBJ-029
    - OBJ-249
  time:
    - TIM-003
---

# Game: Dosa Divas

This scope follows the
[canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Dish names, specific flavours, thresholds and amounts are parameters of
the recorded route.

## Analysis scope

- Version / ruleset: full English PlayStation 5 digital base game
  `UP4063-PPSA31534_00-0194121456613142`, issued 14 April 2026. The main
  PS5 capture was published at launch. Installed build and parity with
  subsequent updates are unverified.
- Primary decision loop: react to active enemy strikes, choose a
  party action that addresses a craving or exposed target, and clear
  the bounded group. Return to the village, take the noodle request,
  fit its ingredient requirements, complete two preparation steps and
  deliver an eligible portion. Read the credited local result.
- Entry: the sampled Port Zest encounter in the launch PS5 recording
  around 7:55–8:05, from its battle introduction. Port Zest is the third
  village in the commercial campaign trace. The earlier battle, other
  requests and existing progress in that same video are context.
- Exit: after the noodle order route, observe Village Rank Up and the
  Port Zest reward panel. Stop before another order or fight.
- Included: three-member party, enemy and party action phases,
  reactive block grades, timed attacks, matching flavours and shield
  break, group defeat, experience and separately retrieved Lina Loot,
  the request, named ingredient slots, one preparation session, its
  portion yield, and local delivery and rank settlement.
- Excluded: native execution, exact installed patch and input frames,
  precise shield and damage formulas, comparing every flavour,
  independent boost- or Ultimate-based strategies, in-battle meal use,
  other recipes beyond output cross-checks, previous progress values,
  minimum reputation routing, later village scenes, Steam demo, other
  carriers and September's later Family Dinner update.
- Suggested later scope: trace a specifically named cooked dish
  selected and consumed during a boss encounter on a known PS5 build.

## Direct-play status

No direct play was performed. The platform store and launch material
establish the commercial PlayStation 5 edition. Static frames from the
launch PS5 walkthrough identify the battle, bonus servings, order
delivery steps and local reward. A separate full PS5 play account
corroborates blocking, flavours, preparation and the post-battle
pickup. A dated commercial PC capture supplies chapter ordering only.
The exact installed build, straight-through footage between all sampled
frames, internal thresholds, retry and save behaviour were not verified.
No video or audio playback was used.

## Claim ledger

| ID | Claim | Claim status | Evidence quality | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- |
| DD-001 | The English PS5 commercial base product was released on 14 April 2026. The recorded route is scoped to early commercial PS5 behaviour, outside the standalone PC demo and later updates. | Confirmed | Corroborated | High | P1, P2, P3, W1 dated 14 April. |
| DD-002 | Enemy attacks admit a reactive block. Early accepted timing reduces damage, while timing just before contact can produce a perfect block and zero damage. | Observation | Corroborated | High | P1, H1, W1 8:05–8:20. No exact timing window is asserted. |
| DD-003 | Each actor can use a typed attack or skill against an eligible target. Confirmed craving types, unknown slots and shield values are displayed. Hits of the right flavour reduce the shield and a depleted shield can leave a target Stuffed and more vulnerable. | Observation | Corroborated | High | P1, H1, W1 8:25–8:45, 9:00 vicinity. No hidden craving is inferred from an unknown slot. |
| DD-004 | A prompted input executes inside the selected attack or skill. The featured sour Pucker Punch offers a timed extra hit; the sampled fight shows block feedback, the Stuffed state and additional damage displays. | Observation | Corroborated | High | P1, H1, W1 8:15, 8:35, 9:10–9:25 and 9:35–9:40. Inputs and multipliers are not reconstructed frame for frame. |
| DD-005 | The required enemy group is defeated and the battle settles before traversal resumes. The result shows level 15, experience progress and one Lina Loot reward. | Observation | Direct | High | W1 9:40–9:50; H1 confirms the general sequence. The snapshot level is neither an entry requirement nor necessarily a level gained. |
| DD-006 | The reserved battle loot still has a distinct world pickup interaction. The capture returns to the village and opens an item receipt at that site. | Observation | Corroborated | High | W1 9:45–9:55, H1. Do not treat the entire item receipt as an automatic addition at battle clear. |
| DD-007 | Village reputation is distinct from battle experience. Combat can credit local reputation and an accepted dish contributes to its village. The route includes a later village rank change. | Observation | Corroborated | High | P1, H1, W1 2:10 combat context, 9:45–9:50, 12:25–12:30. No claim that the bounded battle or order alone suffices at zero reputation. |
| DD-008 | A Port Zest resident starts the Spicy Veg Noodle Bowl order. The request enters the order list before choosing the meal in the Prep Realm. | Observation | Direct | High | W1 10:25–10:40, 11:05. The label is the order name rather than the final output name. |
| DD-009 | The request lists rice noodles, seasoning, tomato, lemon and a spicy special ingredient. The board admits ingredient substitutions for category slots and previews the matched dish. | Observation | Corroborated | High | W1 10:35, 11:05–11:25; H1 confirms named and categorical requirements. |
| DD-010 | The selected ingredients advance to two scored controller tasks. The sample uses a held pour toward its marker then repeated inputs at the second operation. The sampled pour shows strong timing feedback. | Observation | Corroborated | High | W1 11:30–11:45, H1. Other combinations of steps and failure behaviour are outside scope. |
| DD-011 | Cooking ends with Spicy Nourishing Noodle Bowl, Cooking Bonus +2 and four portions. Other same-platform recipe results show smaller bonuses and quantities. No bonus quantity is substituted for an ingredient requirement. | Observation | Corroborated | High | W1 11:55, 3:45 and 7:00 as contextual checks; H1. No universal recipe-yield baseline is claimed. |
| DD-012 | The route returns to the village and hands off prepared food. At the final rank notification, the Port Zest reward panel is visible. Earlier standings affect the threshold, independently of the level 15 battle result. | Observation | Corroborated | Medium | P1, H1, W1 12:00–12:30. The exact pre-order reputation, intermediate menu input and amount credited per portion are unverified. |

## Basic data

- Release / origin: Outerloop Games authored and published the scoped PS5
  base product, released 14 April 2026.
- Platform: `PLAT-PLAYSTATION-5`, commercial English PS5 digital base game.
- Puzzle families: tactical forecast and counterplay (FAM-009) for the
  choice of flavoured attacks and timing defences, and inventory and
  fixture dependencies (FAM-013) for the order, assembled ingredients
  and transfer of the prepared dish.
- P1: [PlayStation Store PS5 product and rules](https://store.playstation.com/en-us/product/UP4063-PPSA31534_00-0194121456613142).
  Confirms release, platform, language, matched flavours, active timing,
  village orders and the scope of battle food benefits.
- P2: [Outerloop Games press kit](https://outerloopgames.com/dosa_presskit)
  and [PlayStation's PS5 launch announcement](https://www.youtube.com/watch?v=nA04pk4opeE).
  Establish developer, commercial release and intended mechanic boundaries.
- P3: [Outerloop's separate Steam demo listing](https://store.steampowered.com/app/4316300/Dosa_Divas_Demo/)
  and [full Steam listing](https://store.steampowered.com/app/2950710/Dosa_Divas/).
  The full listing distinguishes the later Family Dinner update. Neither
  PC release is used as PS5 runtime or patch evidence.
- W1: [Video Chums launch-day commercial PS5 gameplay](https://www.youtube.com/watch?v=Cc26Ix82zjI).
  Platform identified in the creator's description. The static frames at
  7:55–12:30 contain the scoped loop. Earlier frames provide comparisons
  for results and local rating context.
- H1: [RipWitch’s full PS5 play account](https://witchsreviewcorner.com/2026/05/13/dosa-divas-review-ps5/).
  The review documents normal difficulty, ingredient categories, the
  two-step kitchen, turn commands, block grades and separate Lina Loot.
  Its author is separate from W1. W1's difficulty is unverified.
- W2: [fgw full commercial PC walkthrough](https://www.youtube.com/watch?v=8bHgmJ6UJ1E).
  Creator timestamps place Buroth Village, Canopea and then Port Zest.
  This only locates the village in the campaign.

### Reproducible route evidence

1. In the sampled Port Zest location, start the encountered goon group.
   W1 7:55–8:10 shows the location to battle transition. The enemy phase
   opens before the recorded player's choice.
2. On an incoming strike, use the defence input near contact. See W1
   8:15 for Perfect Block and zero damage. An early accepted input
   provides lesser mitigation. H1 describes the failure branch when an
   input misses both windows.
3. Read the displayed shield, known profiles and question marks. Choose
   a compatible attacker and target, and execute the shown input.
   W1 8:35 exposes Pucker Punch, a sour action with a timed extra hit,
   alongside a Stuffed enemy. Later hits and skill execution continue
   until the last enemy is down. Do not treat a flavour name as a
   requirement to have that ingredient in inventory.
4. At W1 9:45 read the result and Lina Loot entry. Continue and open the
   world pickup for the item receipt at 9:50–9:55.
5. Approach the resident near the bridge and trigger the offer, then
   read the Spicy Veg Noodle Bowl order. Enter the Prep Realm with the
   scoped ingredients available and choose the order. W1 10:35 and
   11:05–11:25 show the requested slots and recipe preview.
6. Fit the base, flavours and spicy special. Commit preparation, hold
   the prompted input to pour toward the marker, then follow the
   repeated-press prompt in the second task. W1 11:55 shows four portions
   of Spicy Nourishing Noodle Bowl with a +2 bonus.
7. Leave the Prep Realm, return to the resident and give eligible food.
   Watch the local rank notification and open its reward panel.
   W1 12:00–12:30 shows the village interactions and Village Rank Up.
   Keep this standing separate from the combat experience result.

## Mechanical decomposition

### Action Genes

- ACT-008: move the mech between the encounter, chest and resident.
- ACT-019: choose the current combatant, ability and eligible target.
- ACT-091: provide a finished portion to its addressed requester.
- ACT-123: choose and commit the eligible known recipe.
- ACT-222: execute an offensive action prompt at the current timing.
- ACT-223: respond to an approaching attack at its live contact window.
- ACT-341: interact with the resident and separately open the reward source.
- ACT-808: hold and repeat the prompted cooking inputs in the Prep Realm.
- Claim IDs: DD-002–DD-006, DD-008–DD-012.

### System Behaviour Genes

- SYS-358: the current combat action's timed input contributes to its result.
- SYS-362: finishing the encounter and opening its source grant scoped rewards.
- SYS-1138: separately assessed prep tasks precede the final recipe yield.
- SYS-1784: matching flavours exhaust the shield and expose a Stuffed target.
- SYS-1785: kitchen performance adds discrete portions to the meal.
- SYS-1786: eligible activities accrue toward local standing and rank rewards.
- SYS-1787: the incoming attack distinguishes partial and perfect blocks.
- Claim IDs: DD-002–DD-007, DD-009–DD-012.

### Constraint Genes

- CON-710: address the current prep task and its shown control window.
- CON-851: meet the base, named ingredients and category requirements.
- Claim IDs: DD-008–DD-011.

### Information Genes

- INF-142: active attack motion and prompts signal reactive timing, without
  numerically specifying the input window.
- INF-573: the enemy display differentiates known cravings, unknown slots
  and shield state.
- Claim IDs: DD-002–DD-004.

### Objective Genes

- OBJ-029: finish the local battle by defeating the finite required group.
- OBJ-249: finish the recipe and receive its assessed end result before
  attempting delivery. The cooking bonus is the evaluation used here.
- Claim IDs: DD-005, DD-010–DD-012.

### Time Genes

- TIM-003: combat actions and cooking tasks contain bounded live
  execution windows. Turn planning does not itself become real-time combat.
- Claim IDs: DD-002, DD-004, DD-010.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Enemy's attack is executing | Block near contact | Perfect Block and zero damage in the sampled case | Live defensive timing differs from choosing an attack already | DD-002 |
| An enemy still has a craving shield | Land a compatible attack and check the shield | Shield loss can expose the Stuffed state | Correct flavour is a shield interaction as well as attack context | DD-003, DD-004 |
| The last opponent is active | Resolve the last required damage | Experience and Lina Loot appear in the result | All-required-enemy defeat closes the encounter | DD-005 |
| Returned to the village | Inspect the spawned reward | Open a separate receipt | Reward entitlement and pickup are distinct | DD-006 |
| Resident offers food request | Take the order and fill declared recipe slots | The selected recipe advances to its prep tasks | Matching the request is separate from cooking well | DD-008, DD-009 |
| Ingredients admitted | Complete held pour and repeated action | Four portions and +2 cooking bonus | Execution is evaluated after recipe selection | DD-010, DD-011 |
| Eligible dish held and existing local credit present | Deliver and read the final notification | Village Rank Up and Port Zest reward panel | Local standing settles separately from battle experience | DD-007, DD-012 |

## Strategic and experiential structure

Reserve the right flavour for targets whose shields are worth removing,
while taking seriously the timing of each incoming strike. Victory yields
battle experience and makes local loot available. The preparation sequence
is a second kind of timed execution. First meet the order's composition,
then improve how many servings the recipe yields. Delivered food adds
local standing. Neither the battle nor the cooking bonus replaces the
ingredient match. Claim IDs: DD-002–DD-012.

## Replay and variation

The sources distinguish reduced and zero damage and report different
bonus quantities. W1's sando and fish bowls provide context for output
variation, while the selected request and delivery are the noodle
route only. An exact equal-recipe repeat and an isolated progression from
zero reputation were not observed. Claim IDs: DD-002, DD-007, DD-011,
DD-012.

## Adjacent systems and history

The official listing describes boost points, team Ultimates and meals
with different battle effects. The selected route does not identify a
cooked portion used as a battle consumable. No dependency from this
prepared dish to the earlier fight is assumed. By the same token the
contents of the recovered Lina Loot are not required ingredients unless
an evidenced route establishes that link. Claim IDs: DD-003, DD-006,
DD-007, DD-012.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-019, ACT-091, ACT-123, ACT-222, ACT-223, ACT-341, ACT-808 | Move, fight, choose, prepare and deliver |
| System Behaviour | SYS-358, SYS-362, SYS-1138, SYS-1784, SYS-1785, SYS-1786, SYS-1787 | Timed actions, rewards, cooking steps, craving shield, quantity, rank and graded blocks |
| Constraint | CON-710, CON-851 | Current prep window and named or categorical ingredient requirements |
| Information | INF-142, INF-573 | Timing cues and known or unknown cravings |
| Objective | OBJ-029, OBJ-249 | Defeat the group and finish the evaluated dish |
| Time | TIM-003 | Bounded live execution inside different activities |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `607` (`GAME-0001`–`GAME-0607`).
- Exact genome matches: none.
- Tied near matches: `GAME-0577` — People of Note (`6 / 31 = 0.193548`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [People of Note (GAME-0577)](../m-r/people-of-note.md) | ACT-019, ACT-222, ACT-223, INF-142, OBJ-029, SYS-358 | Both use prompted execution inside turn-based choices. People of Note uses music timing and group performance, while Port Zest has craving shields and a separate recipe-and-delivery route to local standing. | Near, `0.193548` |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_354](../../../research/taxonomy-changes/TAXONOMY_CHANGE_354.md)
  defines the new boundaries and compared alternatives.

## Negative results

- ACT-572 needs direct stylus action on the food. The scoped release
  uses held or repeated controller input while monitoring the prompt.
- SYS-359 has a complete-parry counter condition. Partial and perfect
  blocks here are graded around contact without that forced counter.
- SYS-361 combines Break, status, party defeat and checkpoint retry.
  The scoped shield specifically advances from craving matches. This
  unit does not establish its full party-wipe and retry rules.
- SYS-822 settles an aggregate assessment without converting reward
  tiers from a score. The observed cooking grade adds inventory
  portions, captured by SYS-1785.
- CON-207 requires exact spatial placement. The visible recipe
  predicates here are the base and the item or category matches.
- TIM-033 resolves a whole precommitted turn batch. The sampled party
  input and the real-time execution occur before the next action.

## Delta summary

## New facts

- [Observation | Corroborated | High] Enemy attack contact grades the
  live block. Correct flavours can deplete a shield and leave the target
  Stuffed. DD-002–DD-004.
- [Observation | Corroborated | High] A Port Zest dish requires
  ingredient matches before active tasks determine its portion bonus.
  DD-008–DD-011.
- [Observation | Corroborated | Medium] Battle reward and village
  promotion are separate visible settlements in the same village
  sequence. DD-005–DD-007, DD-012.

## New genes

- [Observation | Corroborated | Medium] ACT-808, SYS-1784, SYS-1785,
  SYS-1786, SYS-1787, CON-851 and INF-573.

## New combinations

- [Observation | Direct | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_354.

## New questions

- Which confirmed craving matches account for each shield debit under
  a multihit or boosted skill in a known installed build?
- How are partial preparation success and step disturbances weighted?
- Which quantities of combat and recipe credit independently reach
  the first Port Zest threshold from a clean regional state?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0609`, Kuru Kuru Kururin,
  European English Game Boy Advance. Trace one full early Adventure
  level through rotation, collision or refuge and its settled exit.

## Why this game

- [Hypothesis | Limited | Medium] Both the battle and kitchen reward
  moment-to-moment execution, while the village can recognise work from
  these distinct routes through its own standing.
