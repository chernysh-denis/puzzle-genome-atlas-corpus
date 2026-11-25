---
game_id: GAME-0695
slug: terranigma
game_title: "Terranigma"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-341
    - ACT-914
  system:
    - SYS-037
    - SYS-299
    - SYS-1970
    - SYS-1971
  constraint:
    - CON-402
  information:
    - INF-119
    - INF-179
  objective:
    - OBJ-366
  time:
    - TIM-003
---

# Game: Terranigma

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The first summit makes the player read a moving opponent, finish a
finite trial and then separately take the opened path to restoration.

## Analysis scope

- Version / ruleset: Quintet's commercial Nintendo of Europe English
  PAL Super NES release, cartridge family SNSP-AQTP-EUR (1996). The
  English booklet scanned under SNSP-AQTP-UKV identifies the
  standard control rules. The recordings agree with the European
  fixture, but do not independently specify a cartridge revision,
  video refresh rate or exact binary.
- Structured analysis target: PLAT-SUPER-NINTENDO in
  [platform coverage](../../platforms/games.json).
- Entry: take the last stair to the summit floor of Tower 1 in
  Chapter 1 with the Crystal Spear equipped. Stop at the bridge
  approach before addressing the Guardian. The final stone door
  is closed and its four red Huballs have yet to appear.
- Primary decision loop: address the Guardian, step around the
  monsters' rolling paths, find an aligned approach for the
  current spear move and strike. Track life and remaining
  opposition, then walk back to the opened chamber.
- Positive terminal: cross the final threshold after the last
  Huball and watch the Eurasia restoration. The first captured
  controllable state outside the tower closes the fixture.
- Failure boundary: hostile contact can reduce current life.
  W1 wins with a damaged but viable Ark. Death, retry and
  whether a return restores this particular roster were not
  reproduced in the two accepted witnesses.
- Included: summit geometry, the initiating conversation, the
  staggered appearance of four red Huballs, their advancing roll,
  the spear attacks and contact feedback, local life recovery,
  experience and optional money, gate release and restoration.
- Excluded: the lower-floor route and window climb, the Crysta
  errand, magic, healing items, alternate spear builds, later
  towers and settlements, non-English editions and modern ports.
- Potential scoped module: the earlier broken window and chains
  could be reviewed as their own mandatory spatial route.
- Direct-play status: no personal cartridge session, ROM check
  or input trace. The booklet and the declared PAL account fix
  the version and affordances. Two independent English runs
  were reviewed as short background frame sequences without
  audio. Button timing, health formulas and exact attack
  coefficients remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| TER-001 | Nintendo's 1996 PAL issue includes an English cartridge label SNSP-AQTP-EUR and the UKV instruction booklet. The latter documents the controls, combat and end-of-tower restoration. | Confirmed | Direct | High | P1, P2 |
| TER-002 | On Tower 1's summit the addressed Guardian uses a scripted hand raise, then leaves the gate area while four red Huballs appear. Neither trace fights the Guardian itself. | Observation | Corroborated | High | P2 pp. 10–11; W1 26:35–26:58; W2 13:55–14:18 |
| TER-003 | The same equipped weapon attack varies with the standard, dashing, jumping or combined movement state. The booklet separately documents rapid presses. The captures show thrusts while turning and longer travelling spear effects; they do not identify every move by button history. | Observation | Corroborated | High | P2 pp. 14–17; W1 26:58–27:17; W2 14:18–14:32; S1 |
| TER-004 | Red Huballs alternate their legged form with a compact moving red ball. They travel under their own motion while Ark can reposition and attack. W1 shows early hit numbers and later life loss during the pursuit. | Observation | Corroborated | High | W1 26:58–27:22; W2 14:18–14:32; S2 |
| TER-005 | With the starting spear selected earlier, W1 gains missing life during the active trial without opening the item window or stopping combat. The PAL account attributes gradual Underworld recovery to the Crystal Spear. | Observation | Corroborated | Medium | W1 20:17–20:23, 26:53–27:17; S1, S2 |
| TER-006 | Defeats grant experience, which can level Ark. W1 receives level 3 and a rise in maximum life after this fight, while W2 already arrives at level 3. Dropped gems can be taken by contact, separately from opening the route. | Observation | Corroborated | High | P2 pp. 16–17; W1 27:08–27:44; W2 14:19–14:52 |
| TER-007 | The last Huball permits the onward threshold. Crossing the opened door starts the restoration sequence. The map announces Eurasia and the game returns to Underworld exploration with Ark's live state carried forward. | Observation | Corroborated | High | P2 pp. 10–11; W1 27:23–27:51 and 29:23–29:51; W2 14:31–14:55 and 16:05–16:30; S2 |

## Basic data

- Release / origin: Quintet and the Enix production, published
  by Nintendo in PAL territories. This fixture uses the
  1996 English European Super NES commercial cartridge.
- Mechanical families: FAM-009 for repositioning against the
  changing attack path and FAM-017 for the ordered trial,
  passage and restoration.
- P1: [European cartridge photograph](https://snescentral.com/cart.php?id=0906&num=0).
  The collector archive's photograph identifies SNSP-AQTP-EUR.
- P2: [Nintendo's English instruction booklet](https://archive.org/details/terranigma-eu/page/n8).
  Cover and imprint identify the edition. Printed pp. 10–11
  separate guardian clearance from entering the restoration room.
  Printed pp. 14–17 explain movement and attacks, experience,
  floating damage feedback, and collecting coins on contact.
- W1: [Longplay Nexus English SNES recording](https://www.youtube.com/watch?v=I1m-jI2PEf4&t=1595s).
  The earlier equipment menu at 20:17–20:23 supplies context
  for the starting weapon. Use 26:35–27:23 for the fight,
  27:24–27:51 for the opened threshold, and 29:23–29:51
  for the acknowledgement and return.
- W2: [IndieGamerRetro Tower 1 and 2 recording](https://www.youtube.com/watch?v=jNS5n2o-wX0&t=835s).
  A second English presentation begins the summit at 13:55.
  Use 14:13–14:34 to identify the four-body encounter.
  Restoration begins after the threshold around 14:52–14:55.
  The continent appears on the map after 16:05.
- S1: [Version-identified PAL player account](https://gamefaqs.gamespot.com/snes/588784-terranigma/faqs/78151).
  Corroborates the opening Tower 1 roster, the movement input
  combinations and gradual Underworld regeneration with the
  Crystal Spear. Its measured rate and damage factors are
  outside this capture-based scope.
- S2: [Independent Tower 1 walkthrough](https://www.thonky.com/terranigma/tower-1)
  and its [opening equipment notes](https://www.thonky.com/terranigma/chapter-1-the-outset).
  Corroborates the rolling opponents, subsequent door transition
  and the early spear's slow recovery.
- Claim IDs: TER-001–TER-007.

### Reproducible fixture evidence

1. Approach the summit through the narrow stone passage with
   the Crystal Spear equipped. Face the Guardian standing
   in front of the sealed door and use the standard local
   interaction. Both recordings show the hand raise and then
   the four red bodies in the arena and passage.
2. Move out of the nearest red sphere's path and aim the
   equipped spear at a reachable body. The manual describes
   an ordinary grounded attack, a dash attack, a jump attack
   and a combined dash-jump attack on the same attack button.
   W1 26:58–27:17 and W2 14:19–14:32 show the live aiming,
   motion and visible contacts. Compare a short thrust with
   the intervening travelling blue attack effect.
3. After a successful blow check the floating damage number
   and current life. A pickup at the last defeated body's
   position is not a required key. In W1 the wallet increases
   from 59 to 71 during the recorded rout. W1 gains missing
   life from 11 to 15 out of 33 while playing without a
   healing item command, then takes further damage.
4. Let the last required red Huball be defeated. W1 is in
   the lower passage when the Guardian speaks after the clear.
   W2 stays on the platform. Both remain on that floor during
   the acknowledgement and must walk to the door.
5. Cross the now-open north threshold. The next room begins
   the restoration automatically. After the continent is
   acknowledged, W1 returns to the same Underworld landmark
   outside Tower 1. The opening of the next tower still
   shows level 3 and the 71-gem balance, confirming retention
   beyond the terminal. W1 29:47–30:20.

## Mechanical decomposition

### Action Genes

- ACT-008: walk, run and jump the same controllable body
  to change its position and facing relative to the red
  opponents and the reachable doorway. TER-003–TER-004, TER-007.
- ACT-161: aim and thrust the equipped spear into a nearby
  opponent. TER-003–TER-004.
- ACT-341: address the Guardian to begin this authored local
  challenge. TER-002.
- ACT-914: select a spear attack by committing it in the
  current locomotion state. A dash, a jump or both visibly
  change the documented attack form. TER-003.

### System Behaviour Genes

- SYS-037: touch a dropped coin to credit its value while
  ordinary movement continues. The coin is not a gate key.
  TER-006.
- SYS-299: defeat credit can cross a level threshold and
  enlarge Ark's life capacity. One witness gets level 3
  after the final defeat and the other begins at that level.
  TER-006.
- SYS-1970: the red Huball changes from a legged walker to a
  compact fast-moving contact threat and back. TER-004.
- SYS-1971: the equipped Crystal Spear gradually restores
  missing life during the active Underworld fixture without
  a separate healing item action. TER-005.

### Constraint Genes

- CON-402: the declared forward exit is sealed until the
  four required enemies are gone. The lower passage is
  still walkable during the encounter. TER-002, TER-007.

### Information Genes

- INF-119: current and maximum life, equipped kit and
  character level are readable independently of world motion.
  TER-003, TER-005–TER-006.
- INF-179: the room view exposes the moving monsters, corner
  geometry and onward door, while hits give immediate local
  feedback. TER-002–TER-004, TER-007.

### Objective Genes

- OBJ-366: finish the Guardian's trial, cross the released
  threshold and receive the restored-continent outcome.
  The last hit makes it reachable. Acting on that access
  is the separate terminal transition. TER-002, TER-007.

### Time Genes

- TIM-003: the visible live trajectories continue between
  spear attacks while the player chooses when to move or act.
  The dialogue and restoration sequences interrupt that
  ordinary play. TER-003–TER-004, TER-007.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Quiet summit and sealed door | Address the Guardian | Four red Huballs appear and the trial starts | TER-002 |
| Active opponent in reach | Commit a spear strike with the chosen locomotion state | Local hit and short damage readout when contact succeeds | TER-003–TER-004 |
| Red Huball uncurled | Hostile switches to its roll | A compact faster contact hazard crosses the approach | TER-004 |
| Ark below maximum life with Crystal Spear equipped | Continue the live Underworld interval | Missing life regenerates without spending a carried item | TER-005 |
| Final required monster still live | Defeat it | Guardian acknowledges the clear and grants forward access | TER-007 |
| Open summit threshold | Walk through | Restoration starts; Eurasia appears and exploration resumes outside | TER-007 |

## Strategic and experiential structure

Retreating into the lower passage gives room to separate
the adversaries. A move that travels farther can pursue a
rolling body, but committing toward its current course
can still leave Ark in the path of another threat. The
small passive recovery matters when coming in wounded.
The door gives the battle a purpose separate from
optional gold.

## Replay and variation

W1 begins at level 2 and reaches the lower passage with
the last roller. W2 begins at level 3 and ends combat on
the wider upper floor. Both clear the same four enemies
and then walk north. These traces show different approaches
and health histories under one gate rule.

## Adjacent systems and history

The lower tower teaches movement, hostile navigation and
a route that leaves and re-enters through different
windows. The summit analysis starts after those events.
The later towers reuse the Guardian structure with
different rooms and opposition.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-161, ACT-341, ACT-914 | Position, strike, begin the trial, vary attack by movement |
| System Behaviour | SYS-037, SYS-299, SYS-1970, SYS-1971 | Credit pickups, level, switch the hostile form, recover life |
| Constraint | CON-402 | Hold the onward route until required clearance |
| Information | INF-119, INF-179 | Read personal reserves, threats, hits and door |
| Objective | OBJ-366 | Restore a continent by entering after the trial |
| Time | TIM-003 | Act against changing live trajectories |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `694` (`GAME-0001`–`GAME-0694`).
- Exact genome matches: none.
- Tied near matches: `GAME-0622` — Pepper Grinder (`6 / 19 = 0.315789`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Pepper Grinder (GAME-0622)](../m-r/pepper-grinder.md) | ACT-008, ACT-341, INF-119, INF-179, SYS-037, TIM-003 | Both use live movement, local activation, visible routes and optional contact pickups. Lost Claim depends on soft-ground drilling and a boost into a safe emergence, then ends by operating a flag. Tower 1 depends on the moving Huball roster and the spear's movement-dependent attack, then a walk across the released threshold changes the world. | Near, `0.315789`. |

## Taxonomy impact

Reuse direct attack, contextual interaction, experience and finite
hostile clearance. Isolate the movement-selected spear form, the red
Huball roll, the equipment recovery behavior and the separate
restoration terminal through an opened trial chamber.

## Negative results

- Ark fights the four spawned red Huballs. The Guardian
  supplies the trial and the result.
- Defeating the last Huball does not start the continent sequence
  while Ark remains on the summit.
- The two witnesses do not require one exact level or one prescribed
  spear input to enter the opened chamber.
- The evidence does not establish that a curled Huball is immune to
  all spear strikes or identify a universal damage amount.

## Delta summary

Thirteen admitted genes describe a summoned contact trial and
the separate restoration-gate transition.

## New facts

- The red Huballs present both a legged body and a round moving body.
- The fight remains live when Ark backs into the narrow approach.
- The same finish is reachable at different observed starting levels.
- After the clear, the player supplies a separate spatial input
  by walking into the final chamber.

## Principles and design implications

A directional attack can depend on how the player starts moving
rather than on an inventory switch. Making restoration a distinct
traversal event keeps combat confirmation separate from world change.

## Puzzle or game generation potential

Prototype an original encounter with a wide space, a narrow retreat
and several enemies that periodically roll along traversable lanes.
Offer different attack footprints based on the player's current
movement. After the clear, require walking to a revealed chamber
that changes the visible map.

## New genes

- ACT-914
- OBJ-366
- SYS-1970
- SYS-1971

## New combinations

None. None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 441](../../../research/taxonomy-changes/TAXONOMY_CHANGE_441.md).

## New questions

- What controls the red body's next turn and curl timing?
- Is the lower passage retreat enough to reset the trial on
  the selected cartridge, or must Ark leave the whole floor?

## Next recommended game

Continue Selection 060 with GAME-0696, Tides of Tomorrow,
on PlayStation 5.

## Why this game

The summit demonstrates how movement chooses the attack shape
and how a cleared encounter grants separate access to the
world's next state.
