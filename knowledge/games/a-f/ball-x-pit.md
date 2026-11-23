---
game_id: GAME-0610
slug: ball-x-pit
game_title: "BALL x PIT"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-140
    - ACT-810
  system:
    - SYS-004
    - SYS-469
    - SYS-574
    - SYS-575
    - SYS-576
    - SYS-1792
    - SYS-1793
    - SYS-1794
    - SYS-1795
    - SYS-1796
  constraint:
    - CON-188
    - CON-773
  information:
    - INF-002
    - INF-119
    - INF-235
  objective:
    - OBJ-308
  time:
    - TIM-003
---

# Game: BALL x PIT

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The named layer, character, reactor choices and gear requirement are
parameters of the observed base-game route.

## Analysis scope

- Version / ruleset: commercial Apple App Store release of BALL x PIT,
  app ID `6738703497`, available from 12 March 2026. Full Game unlock,
  standard base-game descent in The BONExYARD with The Warrior. The
  paid product also offers the first layer in the trial. The paid
  boundary is evidenced by access to the second layer in the Apple
  recording. The precise iOS build, hardware model in that recording
  and purchase transaction are unverified.
- Primary decision loop: move and direct the next volley into the
  approaching line or off a wall. Approach dropped experience to
  draft a ball, passive or upgrade. Use the resulting build to keep
  the lane open, dodge the Skeleton King’s attacks and defeat him.
  Read the share of permanent progress credited on return.
- Entry: select The Warrior and the first layer with ordinary early camp
  progress. The recorded winning try follows a failed attempt on the
  same layer. It is not a clean save or an inventory reset procedure.
- Exit: Skeleton King clear, character-completion award and the
  first-clear gear handoff at New Ballbylon. The lift’s requirement
  and subsequent access to The SNOWYxSHORES verify the handoff and
  product boundary. Play on that layer is outside this mechanical scope.
- Included: independent movement and aim, wall bounces, ball recovery,
  advancing ranks and their attacks, XP drops and build draft, the
  reactor choice when found, the final boss and the settlement that
  carries the gear into the lift screen. The earlier failed attempt
  establishes a separate ending and return to camp.
- Excluded: precise movement, damage, catch or hit timing, the complete
  recipe list, later layers and characters, construction rules, speed
  tiers, Endless, New Game+, Risen Ballbylon, later balance changes,
  paid transaction execution, manual save handling and the Android,
  PC and console editions as analysis targets.
- Suggested later scope: reproduce one named eligible evolution to
  its changed outgoing ball effect on a separately specified run.

## Direct-play status

No direct play, purchase or restore was performed. Apple and Devolver
establish the product, full unlock and ordinary mobile rules. App
Unwrapper’s Apple App Store-linked recording has the Apple mobile
home indicator and shows both the first-layer clear and actual play
in the second layer in one session. It does not identify its device
model or storefront transaction. A contemporaneous firsthand iPhone
16 Pro Max account independently supports the shared combat and
progression rules. The separate Shorty Bluejova capture ends at a
Google Play purchase sheet and only establishes the mobile trial
boundary. Console testimony is identified where used for shared
rules. Only static frames and written sources were examined.

## Claim ledger

| ID | Claim | Claim status | Evidence quality | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- |
| BP-001 | The Apple App Store product has a separate Full Game unlock; the release went live on 12 March 2026. The Apple route shows a later layer beyond the first-layer trial. | Confirmed | Corroborated | High | P1 lists both the app and the full-game purchase. P2 and P3 establish date and commercial release. W1 44:40 shows subsequent play. W2 12:30–12:35 establishes the trial boundary independently on Android. |
| BP-002 | The warrior moves across the live lane while aim and shots point separately. Projectiles can strike approaching skeletons directly or reach them after a solid side-wall ricochet. | Observation | Corroborated | High | P4, R1 and W1 17:30–18:40. Static frames resolve positions, the dotted aim line and balls; precise touch sensitivity is outside the scope. |
| BP-003 | A projectile remains unavailable while in flight. Intercepting it returns it earlier, and balls that pass the avatar return after crossing the lower edge. The enemy side of the exchange is different: the advancing front rank can attack at the lower boundary. | Observation | Corroborated | Medium | R1 on return, R2 on catch and front-rank damage, W1 17:30–18:50 confirms the shared mobile geometry and travel directions. Exact cooldown and collision coefficients were not measured on iOS. |
| BP-004 | Defeated enemies leave XP pickups. Approaching and collecting them fills the run-level meter. A crossed threshold interrupts play and presents a finite random offer. One selected upgrade remains in the active build as play resumes. | Observation | Corroborated | High | P4, R1 and W1 at 18:00, 19:40, 19:50 and 33:20–33:30. At 19:40 the three options include new picks and an owned upgrade. A preview does not establish an exact pick. |
| BP-005 | A reactor can offer Fission to distribute upgrade levels. Fusion becomes an additional alternative when compatible, sufficiently developed inputs are present. | Observation | Corroborated | Medium | W1 19:20 shows Fission only and 34:00 shows Fusion as well. P1 and P4 describe combining effects, and C1 documents the developed-input requirement. The precise committed fusion and full recipe table are not established by the samples. |
| BP-006 | Enemy and boss offensive actions can reduce the Warrior’s health during a descent. The earlier attempt ends in Game Over and returns to camp; the successful attempt advances to the Skeleton King and navigates his visible purple spreads. | Observation | Direct | High | W1 14:40–15:20 for depletion, result and return; 37:50 and 40:20–41:40 for the Skeleton King and dodge lane. P4 independently describes mobile boss pressure. |
| BP-007 | The Skeleton King’s defeat ends the normal layer. The recorded clear displays the character-completion award, then a retained gear message while back at the base. | Observation | Direct | High | W1 41:40 shows the remaining boss, 41:50 the character-completion award, 42:00 the character level panel and 42:10 the gear message. |
| BP-008 | A first clear by an eligible character contributes a gear. The next layer needs a separate lift upgrade; the displayed requirement for The SNOWYxSHORES is two gears. The recording subsequently begins that layer. | Observation | Corroborated | High | W1 42:10–42:30 shows the gear handoff and upgrade, and 44:20–44:40 show descent and control in snow. C2 corroborates the first-clear and layer rules. The earlier gear’s acquisition is outside this sampled run. |

## Basic data

- Release / origin: Kenny Sun and collaborators developed the game.
  Devolver Digital published the Apple mobile edition in March 2026.
- Platform: `PLAT-IOS`, full game from the Apple App Store. The shared
  Apple app is listed for iPhone and iPad via the same product page;
  no hardware-specific equivalence or performance claim is inferred.
- Puzzle families: physics and object manipulation (FAM-007) for
  aimed wall banking, and real-time system pressure (FAM-010) for
  defending the lane while ranks and boss shots advance.
- P1: [Devolver’s Apple App Store entry](https://apps.apple.com/us/app/ball-x-pit/id6738703497).
  Establishes the full-game entitlement and iPhone support. The
  page now also advertises the separately released expansion.
- P2: [Devolver’s mobile release announcement](https://www.youtube.com/watch?v=6aRB1l2qhRk)
  dated 12 March 2026. Official metadata identifies the available
  mobile commercial release and explains feature parity.
- P3: [Publisher’s launch announcement and App Store link](https://www.reddit.com/r/BALLxPIT/comments/1rrvqso/ball_x_pit_is_now_available_on_mobile/)
  dated 12 March 2026, and [its own Steam announcement feed](https://steamcommunity.com/app/2062430/announcements/)
  for the optional trial and paid full game. The Steam news post
  repeating the release carries a later date.
- P4: [Apple’s iPhone launch feature](https://apps.apple.com/st/iphone/story/id1860671472)
  for ricochets, descending opponents, experience, ball upgrades,
  boss pressure and building after the run.
- W1: [App Unwrapper’s App Store-linked commercial Part 2](https://www.youtube.com/watch?v=MynX9M56r08&t=1030s),
  dated 15 March 2026. Earlier failed attempt at 14:40–15:20,
  Warrior selection at 17:10–17:20, first layer at 17:30–41:50,
  handoff at 42:00–42:30 and second-layer play by 44:40.
- W2: [Shorty Bluejova’s mobile trial observation](https://www.youtube.com/watch?v=twdasNB8MQI&t=750s),
  dated 15 March 2026. The 12:30 unlock prompt and 12:35 Google
  Play purchase sheet separate the trial and full mobile product.
  Google Play identifies that recording as Android despite both
  stores and multiple devices being listed in its description.
- R1: [Leonid Shmatenko’s iPhone 16 Pro Max account](https://pocket-gaming.org/review-shorties/ball-x-pit/),
  dated 15 March 2026. Corroborates mobile wall ricochets, ordinary
  return, XP collection, offers and retaining resources. Its broad
  bottom-of-screen description does not negate mobile movement
  visible across W1’s lane.
- R2: [Nintendo Life’s firsthand Switch review](https://www.nintendolife.com/reviews/nintendo-switch/ball-x-pit).
  Separately corroborates the earlier catch, lower-boundary return,
  and attacking enemy rank. Switch commands are outside iOS scope.
- C1: [Fusion Reactor reference](https://ballxpit.wiki.gg/wiki/Fusion_Reactor).
  Cross-check for the choices present in W1. This community page
  is supplementary and later recipe or balance rules are excluded.
- C2: [Pit layers and gear reference](https://ballxpit.wiki.gg/wiki/Pit).
  The first two layers and first-clear gear rule corroborate W1.

### Reproducible route evidence

1. In the full game pick The Warrior and descend to the opened The
   BONExYARD. The sampled win begins from an early camp with previous
   progress (W1 17:10–17:30). Take an initial aim at the nearest
   skeleton line or at the lane wall to approach the formation from
   a flank.
2. Move the avatar through the open lane as outgoing and returning
   balls travel separately. The dotted aim line stays legible while
   the avatar moves. When the front rank is close, hit it directly
   or relocate. Waiting for a long ricochet can leave that rank alive.
3. Defeat enemies and approach the scattered XP. At the visible draft
   choose one offered new item or an eligible upgrade. W1 19:40 and
   33:20 show options, and the following frames show resumed combat
   with the build slots visible. Fission is present at 19:20; the
   later reactor presents Fusion as an alternative at 34:00.
4. Continue to the Skeleton King. Use the spaces between the purple
   spreads while pointing shots back into the boss and its enemies.
   W1 41:40–41:50 shows the boss disappear and the completion award.
   The earlier attempt shows a Game Over at 15:00 instead.
5. Read the character screen and return to New Ballbylon. W1 42:10
   displays the gear award, and the lift at 42:20 names The
   SNOWYxSHORES and its gear requirement. The recording reaches the
   next snowy lane by 44:40. End the mechanical analysis at the
   gear and lift handoff.

These are recording timestamps. They do not set in-game deadlines or
prescribe fixed level-up or reactor decisions. Claim IDs: BP-001–BP-008.

## Mechanical decomposition

### Action Genes

- ACT-008: move the Warrior around the two-dimensional lane.
- ACT-140: choose one offered item or upgrade with a run-long effect.
- ACT-810: direct outgoing shots independently of avatar movement.
- Claim IDs: BP-002, BP-004, BP-006.

### System Behaviour Genes

- SYS-004: level-up offers draw from more than one eligible outcome.
- SYS-469: the prior attempt settles without carrying over its temporary
  balls. The successful one leaves its eligible first-clear reward.
- SYS-574: defeated enemies leave scattered XP credited near the avatar.
- SYS-575: crossing a run-level threshold interrupts the live stage
  with a finite eligible random offer.
- SYS-576: the selected ball or passive and its upgrades change the
  current active build.
- SYS-1792: side-wall collisions redirect free projectiles in the lane.
- SYS-1793: intercept or wait for the lower-edge return to recover a
  projectile.
- SYS-1794: incoming ranks become attacking threats at the lower edge.
- SYS-1795: a collected reactor opens a different decision from a
  level-up. Which choices are eligible depends on the build.
- SYS-1796: retain a first-clear gear and spend the qualified lift
  upgrade to open a successor.
- Claim IDs: BP-002–BP-008.

### Constraint Genes

- CON-188: each accepted roll of the offer allows one selection.
- CON-773: zero vitality ends the ordinary active attempt.
- Claim IDs: BP-004, BP-006.

### Information Genes

- INF-002: exact future level-up options are hidden before the offer.
- INF-119: health and the run’s XP and current build are visible.
- INF-235: nearby ranks, projectiles and pickups can be read together.
- Claim IDs: BP-002, BP-004, BP-006.

### Objective Genes

- OBJ-308: defeat the final guardian of the selected layer and
  settle its progression token, here a gear, at the level selector.
- Claim IDs: BP-007, BP-008.

### Time Genes

- TIM-003: ranks and shots move while the player aims and navigates.
  The level-up menu interrupts that running simulation.
- Claim IDs: BP-002–BP-006.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| The first layer opens with lines of skeletons ahead | Move the Warrior and point a volley into a side wall | The shot turns back into the lane and can approach the formation from an angle | Movement and direction of fire are distinct | BP-002 |
| A live ball is returning | Intercept it or let it pass through the lower edge | Interception restores availability earlier; an ordinary missed catch can still return it | Missing the return is not a life loss | BP-003 |
| An approaching rank remains alive near the lower edge | Delay clearing the front ranks | An enemy that reaches the boundary can attack | A distant bank shot and immediate defence compete | BP-003, BP-006 |
| XP remains near a fallen enemy | Approach and cross an experience threshold | The action interrupts and an upgrade tray opens | XP collection precedes the build decision | BP-004 |
| An eligible new ball, passive or upgrade is displayed | Choose one option | The active run build changes and the lane resumes | The same choice set does not grant every option | BP-004 |
| A reactor is collected | Inspect the eligible alternatives | The later build enables a fusion alternative in addition to level distribution | Reactor access and build eligibility are separate | BP-005 |
| An earlier descent runs out of health | Dismiss the Game Over result | The game returns to New Ballbylon without the transient run build | Failure and return to base are compatible | BP-006 |
| The Warrior survives the final attack pattern | Land the final boss damage and continue the result | The boss clears, the character award appears and the first-clear gear enters the lift progression | An eligible completion leaves a durable route token | BP-007, BP-008 |
| The lift has the required gear total | Confirm the lift upgrade | The next layer becomes selectable | A single clear, sufficient gears and next-layer admission are different events | BP-008 |

## Strategic and experiential structure

A side-wall bank can get a projectile behind a row. A front rank
that is already close may instead demand direct fire. The Warrior
can pursue XP or returning projectiles, but each route changes
safe space and the next launch position. A level-up can improve
the existing attacks or broaden the build. At the boss, open
lanes between projectile spreads matter as much as keeping one
persistent attack angle. Claim IDs: BP-002–BP-007.

## Replay and variation

W1 shows both defeat and a later successful attempt. Starting camp
progress and rolled offers differ with progression and play; the
observed Warrior win establishes one achievable route. The
documented first-clear gear cannot be assumed to recur every time
the same character defeats the same boss. Claim IDs: BP-004–BP-008.

## Adjacent systems and history

The town can turn retained resources into lasting construction
and character unlocks, but placement and harvesting are separate
decisions outside the selected run. Regal content was advertised
with mobile launch; content from other layers, later free updates
and the later paid expansion is outside the evidence boundary.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-140, ACT-810 | Move, choose a run upgrade and aim independently |
| System Behaviour | SYS-004, SYS-469, SYS-574, SYS-575, SYS-576, SYS-1792, SYS-1793, SYS-1794, SYS-1795, SYS-1796 | Random offers, run reset and retained reward, XP, draft, build changes, banking, return, advancing ranks, reactor and lift |
| Constraint | CON-188, CON-773 | Choose within the offer and keep the live attempt viable |
| Information | INF-002, INF-119, INF-235 | Hidden future rolls, exposed personal build and visible nearby field |
| Objective | OBJ-308 | Clear the boss and retain the layer token |
| Time | TIM-003 | Decide while the lane and threats advance |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `609` (`GAME-0001`–`GAME-0609`).
- Exact genome matches: none.
- Tied near matches: `GAME-0183` — Vampire Survivors (`12 / 31 = 0.387097`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Vampire Survivors (GAME-0183)](../s-z/vampire-survivors.md) | ACT-008, ACT-140, CON-188, INF-002, INF-119, INF-235, SYS-004, SYS-469, SYS-574, SYS-575, SYS-576, TIM-003 | BALL x PIT couples separate live aim to wall reflections and projectile return, then ends at a boss and retained gear. Mad Forest uses autonomous weapon geometry and a clock-based clear. | Near, `0.387097` |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_356](../../../research/taxonomy-changes/TAXONOMY_CHANGE_356.md)
  records the accepted new boundaries and candidate distinctions.

## Negative results

- ACT-113 fixes the launch position and commits a single shot.
  Here the player moves with an independent shot direction.
- SYS-146 models gravity and momentum transfer, neither required
  to explain planar side-wall banking in the pit.
- SYS-056 redirects autonomous grounded locomotion. The balls are
  free projectiles in flight.
- SYS-573 activates weapon geometry without player-aimed attacks.
  The scoped combat still uses the Warrior’s directed shots.
- SYS-577 resolves a boss chest into an upgrade or evolution.
  This reactor offers a separate choice whose eligibility changes
  with the current run build.
- OBJ-245 uses qualification to select a different terminal boss.
  No alternate final boss is needed for this gear route.

## Delta summary

## New facts

- [Observation | Corroborated | High] Arena movement and independently
  aimed side-wall banking jointly control the defence. BP-002, BP-003.
- [Observation | Corroborated | High] Collected experience opens a
  run-local build decision. The later reactor shows an extra
  alternative beyond ordinary level distribution. BP-004, BP-005.
- [Observation | Direct | High] The successful first-layer run awards
  completion and then a gear. Lift qualification and opening the
  second layer are separate from that boss clear. BP-007, BP-008.

## New genes

- [Observation | Corroborated | Medium] ACT-810 and SYS-1792–SYS-1796.

## New combinations

- [Observation | Direct | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_356.

## New questions

- What is the exact time advantage of interception over lower-edge
  return on a measured iPhone build?
- Which specific pair was fused, if any, in the sampled later reactor
  state, and in what order do its effects resolve?
- How do enemy advance and projectile return behave after changing the
  mobile pace beyond the ordinary route sampled here?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0611`, Culdcept, original North
  American PlayStation 2 release. Follow a complete bounded match
  through its route, territory and toll decisions and settled result.

## Why this game

- [Hypothesis | Limited | Medium] The arena turns position and time
  into access to an upgrade. Culdcept can test how a route turns an
  arrival into property control, a toll and a retained match result.
