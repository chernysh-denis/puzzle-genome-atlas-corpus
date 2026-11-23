---
game_id: GAME-0639
slug: rollerdrome
game_title: "Rollerdrome"
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-161
    - ACT-223
    - ACT-851
  system:
    - SYS-822
    - SYS-974
    - SYS-1843
    - SYS-1844
    - SYS-1845
  constraint:
    - CON-867
  information:
    - INF-593
  objective:
    - OBJ-344
  time:
    - TIM-003
---

# Game: Rollerdrome

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: native English commercial PlayStation 4
  digital release, 16 August 2022. The UK PlayStation Store
  identifies the PS4 package as CUSA34254. The capture producers
  identify PS4 or PS4 Slim. Their region code and patch are
  unverified. A separate contemporary comparison identifies PS4
  version 1.02 without binding that version to the main capture.
- Primary decision loop: keep rolling while using finite Dual
  Pistols ammunition, create a safe opening for a trick when low
  or empty, resume the live engagement and check its result.
- Entry: Matterhorn Arena in the 2030 Championship Opening
  Stages, after the briefing and practice. The initial weapon
  shown in the first-clear record is Dual Pistols.
- Exit: defeat the last required opponent, see Victory and the
  arena settlement, then observe active movement at Pike's
  Canyon. Pike's Canyon solutions are outside the packet.
- Included: aimed attacks, temporally qualified evasions,
  contextual skate tricks including grind, finite ammunition
  and its visible recovery, ordinary Reflex Time, scoring and
  challenges as separate result layers.
- Excluded: PS5, Windows and Xbox programs, later campaign
  arenas and weapon unlocks, Out for Blood, precise refill and
  combo formulas, Super Reflex Time tests, assist combinations
  and online leaderboard acceptance.
- Suggested later scope: test the independent enhanced Reflex
  Time branch and the later aggregate challenge gate.

## Direct-play status

No direct play was performed. The edition and release date
come from PlayStation and the original publisher announcement.
The native PS4 Slim recording shows changing ammunition, a
first-clear trophy and active play in the next arena. A PS4
playback with Assist Mode visibly enabled supplies the complete
menu sequence and names the successor. Its fixed ammo counter
is excluded from refill evidence. A separate PS4 replay shows
declining health and ammunition and the full named result.
Exact patch, region and controller inputs of those runs are
unverified. Analysis used silent static frames.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DROME-001 | Roll7 developed a standalone commercial PS4 download released on 16 August 2022. The native PS4 program can be identified separately from the PS5 application and trial entitlement. | Confirmed | Direct | High | P1 PS4 product and release date, P2 contemporary release announcement, W4 PS4 and PS5 captures explicitly run different executable versions. |
| DROME-002 | The player chooses airborne grabs and flips or moves onto an eligible rail for a grind. The same skater can keep moving while attacking and time an evasion against a visible threat. | Observation | Corroborated | High | P3 describes grabs, grinds and defensive timing. W1 1:44–2:24 and final arena sequence. W3 15:12, 15:44–15:48. W2 teaching exercises show the contextual trick inputs. |
| DROME-003 | Dual Pistols spend a finite count. At zero the run continues and shows a no-ammo warning. An eligible trick raises the live count before it needs to be fired again. | Observation | Corroborated | High | P3 Ammunition. W1 1:54 shows 0, 1:55 shows Tail Grab 180 and 3, 1:56 shows the combined grab and flip with 6, and 1:57–1:59 spends rounds again. W1 2:07–2:10 repeats the direction of change on Melancholy. W3 15:26–15:39 corroborates movement and renewed ammunition in a replay. The separate visible evasion credit is not attributed to the grab. |
| DROME-004 | Ordinary Reflex Time briefly slows play while aimed inputs remain legal. The brief slowdown has a renewable limit. | Observation | Corroborated | High | P3 documents the PS activation and renewable duration. W2 exercise around 7:18–7:31 shows the named state while shots are accepted. The more powerful perfect-dodge branch is outside the measured packet. |
| DROME-005 | Current health, ammunition, elapsed time and the live combo are shown separately. Timely eliminations grow the active multiplier, and the developer explains that combo tokens can keep it active during tricks. Settled score is tracked separately. | Observation | Corroborated | High | P3 combo and token guidance. W1 1:54–2:14 retains the multiplier during the grab and increases it as the engagement continues. W3 15:24–15:31 shows the old chain value bank separately while health and ammunition remain live. |
| DROME-006 | Defeating the remaining required House Player settles the arena into Victory. The local report separately counts opponents, optional challenges, elapsed time, score and rank. | Observation | Corroborated | High | W1 4:08–4:17 final defeat, Victory and PlayStation Debut trophy. W3 16:20–16:37 Victory, 22 of 22, rank C and incomplete challenges. W2 10:54–11:20 repeats these report stages in an explicitly assisted run. |
| DROME-007 | Pike's Canyon becomes selectable after the observed first arena result while optional opener challenges remain incomplete. Selecting it leads to live skater control in the distinct arena. | Observation | Corroborated | High | W2 shows 4 of 10 at 11:08, C at 11:19, Continue, the named Start panel at 11:33 and active movement by 11:55. W1 Victory cuts to the matching red canyon entrance and live play by 4:20. The exact minimum challenge count was not varied. |

## Basic data

- Analysis target: `PLAT-PLAYSTATION-4`.
- Developer: Roll7. Original launch publisher: Private Division.
  The current PlayStation Store listing identifies 2K.
- Mechanical families: `FAM-009`, tactical forecast and counterplay,
  and `FAM-010`, real-time system pressure.
- Checked: 2026-11-22.
- P1: [PlayStation Store, CUSA34254 product](https://store.playstation.com/en-gb/product/EP4829-CUSA34254_00-ROLLERDROME00000).
- P2: [Private Division and Roll7, commercial launch announcement](https://ir.take2games.com/node/29051/pdf), 16 August 2022.
- P3: [Roll7 developer combat notes, PlayStation Blog](https://blog.playstation.com/2022/08/11/prepare-for-rollerdrome-with-dev-combat-tips-out-august-16/), on input, timing, tricks and ammunition.
- W1: [ChesBM, native PS4 Slim capture](https://www.youtube.com/watch?v=nY0oM4sjc6w&t=104s), 17 August 2022.
- W2: [Casual Racer Red, PS4 campaign capture](https://www.youtube.com/watch?v=LDwrTI_b-Q8&t=650s), with Assist Mode disclosed in the standings.
- W3: [Minnesota Native2, PS4 arena replay](https://www.youtube.com/watch?v=OaNFEsNRSgQ&t=908s), 21 August 2022. Later loadout equipment is not admitted into the opener.
- W4: [VG Tech, separately labelled base PS4 segment](https://www.youtube.com/watch?v=gk5LVycNrU0&t=1202s), PS4 1.02 and PS5 1.002.000 identified in the capture description.

## Mechanical decomposition

### Action Genes

- ACT-161: aim and fire at an addressed House Player while moving.
- ACT-223: time an active evasion when the attack or lock is visible.
- ACT-851: commit a selected grab, flip or contact trick in the
  current movement mode.

### System Behaviour Genes

- SYS-822: settle the completed arena into its graded report.
- SYS-974: a supported grind carries skater motion along the rail
  until leaving contact.
- SYS-1843: recognized skate activity replenishes usable rounds
  while live movement continues.
- SYS-1844: eligible defeats maintain a short combat multiplier
  within which skate trick value also contributes. Compatible
  combo tokens can hold the chain open.
- SYS-1845: an ordinary, renewable Reflex Time state slows the
  arena briefly while shots still remain available.

### Constraint Genes

- CON-867: firing requires an available round at the current
  weapon. Empty stock leaves other actions available.

### Information Genes

- INF-593: current ammunition, health, elapsed time and live
  score chain remain separately readable.

### Objective Genes

- OBJ-344: defeat the required arena opponents and reach its
  outcome without an additional traversal or collection task.

### Time Genes

- TIM-003: the skater and opponents keep acting while the player
  redirects motion, executes tricks or attacks.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| Dual Pistols have rounds and a House Player is addressed | Fire while rolling | Stock decreases and the encounter keeps running | DROME-002, DROME-003 |
| The HUD shows no ammunition and the skater approaches a suitable slope | Take off and hold Tail Grab | The active trick caption appears and the counter reaches 3 during the maneuver | DROME-003 |
| The skater continues the air maneuver | Add rotation and descend | The count is 6 at the shown grab-flip frame. Subsequent pistol shots spend renewed rounds | DROME-003 |
| The scoring chain is running and additional threats arrive | Continue the timed encounter | The HUD distinguishes multiplier, settled total, health and current rounds | DROME-005 |
| The final required opponent is still active | Resolve that defeat | Victory and the named score and challenge reports follow | DROME-006 |
| Matterhorn Arena has a settled result | Continue and start the next selectable card | The next card and introduction identify Pike's Canyon. Ordinary movement resumes | DROME-007 |

## Strategic and experiential structure

The refill opportunity is produced by motion chosen for its
own spatial requirements. A player with no rounds still has
an immediate way to rebuild attack capacity. Enemy pressure
and the expiring score window constrain when to do it. The
local grade and optional challenges report how the arena
went, while the witnessed continuation establishes progression.

## Replay and variation

The ordinary finite-ammo trace uses longer skating and refill
intervals than the assisted clip with a constant 12. The PS4
replay records a graded win while taking damage. No comparative
medal thresholds, assistance strengths or scoring coefficients
are established by those differences.

## Adjacent systems and history

The game later introduces other weapons and additional conditions.
The special second campaign and the enhanced Reflex Time state
remain distinct from this first live arena demonstration. The
successor entry supplies a boundary and no later clear.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-161, ACT-223, ACT-851 | Attack directly, evade during pressure and select a moving trick |
| System Behaviour | SYS-822, SYS-974, SYS-1843, SYS-1844, SYS-1845 | Grade the arena, carry rail motion, refill rounds, settle chains and briefly slow play |
| Constraint | CON-867 | Keep a finite recoverable ammunition requirement |
| Information | INF-593 | Disclose current combat, capacity and score state |
| Objective | OBJ-344 | Clear the required roster into a result |
| Time | TIM-003 | Continue live progression during inputs |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `638` (`GAME-0001`–`GAME-0638`).
- Exact genome matches: none.
- Tied near matches: `GAME-0277` — Cuphead (`4 / 22 = 0.181818`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Cuphead (GAME-0277)](../a-f/cuphead.md) | ACT-161, ACT-223, SYS-822, TIM-003 | Both require live attacks and evasive choices before exposing a performance grade. Cuphead coordinates health-gated boss transitions and separately graded defensive or special moves. Rollerdrome alternates route-dependent skate tricks and ammunition spend across a required arena roster before starting a different arena. | Near, `0.181818` |

## Taxonomy impact

Seven new definitions distinguish contextual roller tricks, skate
refill, live ammunition admission, defeat-linked chain, renewable
aim slowdown, HUD feedback and the required-roster outcome.
Five definitions already cover aiming, evasion, rail contact,
result grades and concurrent progression.

## Negative results

- Empty ammunition does not end the run in the captured base
  behavior. Continued motion and trick credit restore usable rounds.
- The archived assist-enabled result shows a constant counter and
  cannot establish the finite-ammunition cycle.
- The observed next card is playable with optional challenges
  incomplete. No exact minimum unlock threshold was measured.
- The elapsed clock and a result time bonus do not establish a
  hard first-arena timeout.

## Delta summary

Twelve genes include seven new definitions and five existing
definitions. Earlier game signatures and definitions remain intact.

## New facts

- Usable ammunition can return during visible trick activity.
- A combat multiplier survives ongoing style activity while its
  window remains alive.
- The last required opponent settles into a result that leads
  to an actual next-arena start with incomplete opener challenges.

## Principles and design implications

- Keep a route back from empty ammunition inside the active loop.
- Make resource recovery visible while movement continues.
- Show optional performance goals separately from the basic result.

## Puzzle or game generation potential

Prototype a bounded arena with movement stunts as a renewable
tool resource. Expose its reserve during the maneuver, then
settle a required target set while tracking optional goals and
a performance grade separately.

## New genes

ACT-851, CON-867, INF-593, OBJ-344, SYS-1843, SYS-1844 and SYS-1845.

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_385](../../../research/taxonomy-changes/TAXONOMY_CHANGE_385.md).

## New questions

Which parts of the ordinary refill depend on maneuver duration,
variety and repetition? What condition first gates the next
campaign tier after the observed Pike's Canyon entry?

## Next recommended game

Analyse Pizza Tower for Windows through the first commercial
John Gutter escape and its settled result.

## Why this game

Movement stunts restore the means to finish the same active
encounter. The timing of the two systems is visible throughout.
