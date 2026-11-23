---
game_id: GAME-0570
slug: cult-of-the-lamb
game_title: Cult of the Lamb
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-127
    - ACT-140
    - ACT-148
    - ACT-161
    - ACT-223
    - ACT-318
    - ACT-341
    - ACT-598
    - ACT-773
  system:
    - SYS-037
    - SYS-1670
    - SYS-1671
    - SYS-1672
    - SYS-1673
    - SYS-168
    - SYS-467
    - SYS-550
    - SYS-591
  constraint:
    - CON-175
    - CON-176
    - CON-402
    - CON-834
  information:
    - INF-062
    - INF-126
  objective:
    - OBJ-312
  time:
    - TIM-003
---

# Game: Cult of the Lamb

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
A disposable expedition brings living recruits and physical supplies to a
persistent settlement. Building access and combat capability use different
sources of progression at home.

## Analysis scope

- Version / ruleset: English North American native PS5 base release of
  11 August 2022, ordinary new solo game on Normal with default controls.
  Evidence reconstructs intended launch-window rules. Exact console package
  and version string, launch bugs and patch equivalence are unverified.
- Structured analysis target: PLAT-PLAYSTATION-5 in knowledge/platforms/games.json.
- Entry: after the initial rescue, first induction, cooking fire and berry
  meal, begin at the unopened Darkwood gate with an inducted follower and
  permission from Ratau to make the first resource and recruitment crusade.
  The introductory escape and meal are setup.
- Primary decision loop: open the gate, take the opening weapon, clear local
  sealed fights, choose connected branch nodes by type and decide which
  resources or optional run modifiers to take. Defeat Amdusias, accept the
  recruit and return with supplies. Induct a follower and separate worship
  from gathering. Place and finish the Shrine, collect its Devotion,
  redeem Divine Inspiration for the Temple, build it and perform the first
  sermon for Crown progression. Work assignments can change during settlement.
- Positive exit: the first sermon has settled after the Amdusias clear,
  portal return and recruitment branch. Stop before departing on the next
  crusade. The analysis follows Amdusias into induction as an observed
  recruitment branch. It does not claim the Temple rejects other recruits.
- Negative exit: zero expedition health ends that route and returns the
  player to their established settlement without boss clear. Ordinary failed
  expedition reports can debit carried loot. Exact loss and Faith effects
  during this introductory run on the PS5 package are unverified. This is an
  attempt failure. A later fresh attempt may continue from home.
- Included: one connected Darkwood route through Amdusias, direct movement
  and committed attack and dodge, lethal run health, room clearance, disclosed
  route categories, optional available tarot and boss rewards, the ordinary
  return, follower induction and assignment, local harvesting and construction,
  Shrine Devotion, settlement unlock, Temple and first sermon. Generic named
  resources include Coin, Lumber and Stone. Do not assume a fixed room count,
  offer contents, exact material quota, score or drop table.
- Time boundary: live combat and local production have timing constraints.
  The introductory scheduling of the calendar and persistence of pending
  Shrine work across later absences are outside this scope. Do not infer a
  fixed wall-clock interval or that all settlement systems run everywhere.
- Excluded: the opening escape, early cooking task and tutorial exploits,
  subsequent Darkwood bosses or Leshy, curses and Fervour in later runs,
  rituals and Doctrines, dungeon revival and re-entry, Knucklebones, DLC,
  later co-op modes, alternate difficulty and hardware/version parity.
- Potential scoped modules: post-sermon Doctrine and Bonfire cycles,
  independent follower needs during later crusades, later on-death choices.
- Direct-play status: not conducted. Read the developer launch material,
  Sony's PS5 listing, first-hand PS5 review and dated worked accounts of
  the opening. Other release-era accounts corroborate common rules but do
  not identify the exact native PS5 binary. Neither media nor a game
  executable was played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| CL-001 | PlayStation 5 received the full base game on 11 August 2022. | Confirmed | Direct | High | P1, P2 |
| CL-002 | The first instructed Darkwood crusade follows first induction and initial feeding. The unopened gate displays a one-follower threshold. | Observation | Corroborated | High | P1, R1, R2 |
| CL-003 | Within the run, direct movement, weapon attacks and chosen dodges operate in live combat. Lethal health closes the current route. Amdusias telegraphs lunges and projectile danger. | Observation | Corroborated | High | R1, R2, R3 |
| CL-004 | Combat rooms and the macro route are distinct. The latter displays connected category choices. Combat exits require clearance. An encountered tarot choice can modify the current run. | Observation | Corroborated | High | P1, R1, R2, R4 |
| CL-005 | The first Darkwood boss is Amdusias. Defeat permits recruiting the surviving character, settling rewards and returning through the portal. | Observation | Corroborated | High | R1, R3 |
| CL-006 | Successful and defeated routes return to the same persistent settlement. The successful portal return brings gathered resources. Release-period reports describe partial expedition loss after lethal defeat, with no fixed first-run PS5 percentage or Faith delta established here. | Observation | Corroborated | Medium | P1, R1, R2, R5 |
| CL-007 | A new recruit reaches home before becoming an assigned follower. Induction enables job selection, including gathering or worship as available. Construction requires an allowed footprint and materials, then work on the plan. | Observation | Corroborated | High | P1, R1, R2, R4 |
| CL-008 | Shrine worship produces pending Devotion. Player collection moves it into settlement progression for Divine Inspiration. Redeeming a point unlocks the Temple plan. The unlocked Temple still has to be placed and built. | Observation | Corroborated | High | R1, R4, R6 |
| CL-009 | With the Temple built, the player can deliver the first sermon and receive expedition-oriented Crown progression through attending followers. This progress and communal Faith are tracked separately. | Observation | Corroborated | High | P1, R1, R2, R4 |

## Basic data

- Massive Monster and Devolver Digital. English North American PS5 launch
  boundary. Families FAM-009 tactical forecast and counterplay and FAM-015
  agent routing and coordination.
- P1: [JoJo Zhou, Massive Monster developer launch explanation](https://blog.playstation.com/2022/07/07/managing-a-cult-can-be-a-messy-business-in-cult-of-the-lamb-out-august-11/),
  7 July 2022. Establishes the expedition to settlement cycle, induction and
  Temple sermon feedback to character power.
- P2: [Official PlayStation product record](https://www.playstation.com/en-us/games/cult-of-the-lamb/).
  Confirms platform and launch. The present bundle and later features are
  outside the August 2022 boundary.
- R1: [ShowGamer, launch walkthrough](https://showgamer.com/en/prohozhdeniya-igr/847-prohozhdenie-cult-of-the-lamb),
  12 August 2022. The Amdusias and return sections establish order and local
  transitions. The English first-return section has an inconsistent phrase
  about the Temple already being built before Shrine collection. Use the
  separate building dependency and worked corroboration for the order.
- R2: [Push Square, contemporary PS5 first-hand review](https://www.pushsquare.com/reviews/ps5/cult-of-the-lamb).
  Supports native-context combat, resource labor, persistent base and
  returned defeat. Does not measure tutorial-specific penalties.
- R3: [Pro Game Guides, release-day Amdusias fight account](https://progameguides.com/cult-of-the-lamb/how-to-beat-amdusias-in-cult-of-the-lamb/).
  Supports boss identity, readable attacks and dodge-and-strike response.
- R4: [Jessica Cogswell, GameSpot launch play account](https://www.gamespot.com/reviews/cult-of-the-lamb-review-a-cult-classic/1900-6417933/),
  10 August 2022. Route categories, distinct room types, branch choice,
  autonomous labor and separate Temple upgrades.
- R5: [Ari Notis, Kotaku release-window play account](https://kotaku.com/cult-of-the-lamb-review-ps4-xbox-one-switch-pc-1849423403),
  17 August 2022. Partial death retention in the general launch loop.
  The exact reported fraction is not promoted to a first-run PS5 claim.
- R6: [Sarah James, contemporaneous beginner guide](https://www.pcgamer.com/cult-of-the-lamb-tips-guide/),
  10 August 2022. Distinguishes spent Divine Inspiration for buildings from
  sermon upgrades and communal Faith. Sources checked 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-008 covers runner steering. ACT-161 applies the equipped weapon to
  hostiles and destructible material. ACT-223 covers dodge timing.
- ACT-127 chooses one adjacent next node. ACT-140 commits one limited offered
  benefit, such as a tarot choice retained during that run or a boss prize.
- ACT-341 covers local weapon pickup, recruit acceptance, induction, Shrine
  collection and altar interaction. ACT-318 assigns gathering work and
  ACT-598 assigns worship. ACT-773 spends an earned build unlock. ACT-148
  places a known structure plan with a legal footprint and material cost.
- Claim IDs: CL-002–CL-005, CL-007–CL-009.

### System Behaviour Genes

- SYS-168 produces the finite connected route. SYS-037 covers contact pickup
  of exposed supplies and SYS-467 covers compatible run-local tarot effects.
- SYS-1670 converts defeated Amdusias to pending home recruitment and
  ultimately an inducted worker through the separate intervention. SYS-1672
  accounts for returned haul and retained settlement in clear and death
  branches. It does not model a local room rollback.
- SYS-591 covers direct harvesting. SYS-550 covers timed construction
  labor. SYS-1671 buffers worship output at the Shrine until collected and
  then awards the inspiration threshold. SYS-1673 applies the first sermon
  to a different persistent measure used for expedition power.
- Claim IDs: CL-004–CL-009.

### Constraint Genes

- CON-834 gates first entry by inducted residents. CON-176 bounds macro-route
  choices. CON-402 binds sealed combat exits to defeating the local hostile
  set. CON-175 ends an attempt on exhausting health carried between rooms.
- Claim IDs: CL-002–CL-004.

### Information Genes

- INF-062 provides a chart of node types and traversable connections, with
  encounter details still unknown. INF-126 covers the observable settlement
  work, material and operating conditions used in assignment and building.
- Claim IDs: CL-004, CL-007–CL-009.

### Objective Genes

- OBJ-312 captures the scoped declared expedition-and-sermon endpoint.
  Boss clear, bringing a recruit home, induction, unlock, physical construction
  and sermon remain separate states. The actual game can accept other
  recruitment branches for later settlement development.
- Claim IDs: CL-005–CL-009.

### Time Genes

- TIM-003 covers live controls and ongoing action between the player's
  discrete route selections. It does not assert exact day-cycle activation.
- Claim IDs: CL-003, CL-007, CL-008.

## Reproducible transitions

| State / precondition | Action or event | Observable transition | Boundary | Claims |
| --- | --- | --- | --- | --- |
| One inducted follower and first Darkwood gate unopened | Use the eligible gate | First crusade admits the Lamb | Roster is checked, not consumed | CL-002 |
| First weapon collected, combat room entered | Dodge telegraphed danger and attack until hostile set clears | Room opens travel and awards any available loot | Tactical timing differs from choice of branch | CL-003, CL-004 |
| At a route decision | Select a connected node with a useful disclosed category | Next authored category is entered with current run state | The icon does not expose every local encounter detail | CL-004 |
| Optional tarot choice available | Select a card | Its eligible modifier affects this crusade | It is not a permanent Temple unlock | CL-004 |
| Amdusias encounter active | Evade its lunge or marked projectile danger and reduce health to zero | Amdusias becomes available as a recruit | Boss defeat and induction differ | CL-003, CL-005 |
| Recruit accepted and reward available | Settle reward and take return portal | Re-enter settlement with eligible collected supplies and pending recruit | Chapter boss Leshy remains outside this clear | CL-005, CL-006 |
| Expedition health exhausted before successful exit | Ordinary lethal return | Resume at home without this clear, possibly with part of the haul debited | Previously established home persists | CL-006 |
| Recruit awaiting induction | Complete induction and choose eligible work | The follower joins the active roster and can gather or worship | A pending rescue does not supply labor | CL-007 |
| Shrine built with an assigned worshipper | Wait, collect Devotion and reach inspiration threshold | Gain a building-unlock point | Accumulating, collecting and spending are distinct | CL-008 |
| Temple known and resources available | Place a legal plan and finish construction | Temple becomes usable | Unlock alone grants no sermon site | CL-007, CL-008 |
| Built Temple with first sermon available | Deliver the sermon | Gain Crown progression for subsequent expeditions | The scoped loop ends here | CL-009 |

## Strategic and experiential structure

- A resource branch can support construction while a follower branch can supply
  a worker. Combat and route choices both affect the home state.
- A worshipping worker occupies time that could have produced material. A full
  Shrine needs collection before more output can accumulate.
- Clear, induction, construction and sermon have distinct visible evidence.
  A missing material or incomplete foundation explains absence of an available
  sermon even after a successful expedition.
- Claim IDs: CL-004–CL-009.

## Replay and variation

- Run routes and offers can vary around the first authored boss. Failures end
  the current chain while prior home improvements persist. First-sermon
  progression is spent on later expeditions rather than rolling the first
  expedition back into a partially completed room state.
- Claim IDs: CL-004–CL-009.

## Adjacent systems and history

- Later launch quests introduce curse use, Doctrines and turn cult Faith into
  further decisions. This record stops before those dependencies. Later patch
  systems and the save-state effects of launch defects need separate evidence.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-127, ACT-140, ACT-148, ACT-161, ACT-223, ACT-318, ACT-341, ACT-598, ACT-773 | Weapon, reward types, footprint, assignment |
| System Behaviour | SYS-037, SYS-168, SYS-467, SYS-550, SYS-591, SYS-1670, SYS-1671, SYS-1672, SYS-1673 | Recruit and output transitions, exact death penalty unverified |
| Constraint | CON-175, CON-176, CON-402, CON-834 | Health, connected edges, clearance, one follower |
| Information | INF-062, INF-126 | Partial route and home displays |
| Objective | OBJ-312 | First boss return through first sermon |
| Time | TIM-003 | Live control and productive work |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `569` (`GAME-0001`–`GAME-0569`).
- Exact genome matches: none.
- Tied near matches: `GAME-0458` — The Legend of Zelda: Link's Awakening (`8 / 52 = 0.153846`); `GAME-0459` — Daxter (`6 / 39 = 0.153846`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0458` — The Legend of Zelda: Link's Awakening | ACT-008, ACT-161, ACT-223, ACT-341, CON-175, CON-402, SYS-037, TIM-003 | Both use direct attacks, defensive timing, contextual interactions and local combat clearance. Link pursues permanent traversal capabilities in authored rooms. The Lamb selects a disposable branch, then brings loot and a recruit home for building and sermon progression. | Tied near: 8 / 52 = 0.153846 |
| `GAME-0459` — Daxter | ACT-008, ACT-161, ACT-341, CON-175, SYS-037, TIM-003 | Both use continuous embodied action, health, pickups and reachable interactions. Daxter removes infestations through authored approaches and his own mobility tools. The Lamb returns from a generated route to allocate followers and open a home capability. | Tied near: 6 / 39 = 0.153846 |

### Preserved research notes

- New genes: ACT-773, SYS-1670 through SYS-1673, CON-834 and OBJ-312.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_316](../../../research/taxonomy-changes/TAXONOMY_CHANGE_316.md)
  records the seven additions and rejected substitutions.

## Negative results

- Broad launch reviews do not establish the exact console tutorial death
  fraction or Faith adjustment. Both remain unmeasured scope parameters.

## Delta summary

## New facts

- [Observation | Corroborated | High] CL-004–CL-009 separate run-local
  investment, gathered supplies, pending recruitment, stored worship output,
  construction and persistent sermon progression.

## New genes

- [Observation | Corroborated | Medium] Seven additions are recorded in
  TAXONOMY_CHANGE_316.

## New combinations

- [Observation | Corroborated | High] No new combination is proposed. Existing
  full subsets are enumerated in the comparison record.

## Taxonomy changes

- [Observation | Corroborated | Medium] Prior definitions, signatures and
  lifecycles remain unchanged.

## New questions

- A version-addressed native run could measure the first defeat debit, full
  Shrine capacity, calendar activation and exact first sermon reward.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0571, original Virtua Tennis for Dreamcast.
- Optimisation criterion: alternate era and platform. Replace the expedition
  and settlement feedback loop with a scoped embodied tennis match.
- Backlog impact: fourth Selection 046 unit.

## Why this game

- [Hypothesis | Limited | Medium] The first Darkwood loop exposes multiple
  forms of progression with different owners and lifetimes within one route
  that ends in a measurable new home capability.
