---
game_id: GAME-0688
slug: lunar-silver-star-story-complete
game_title: "Lunar: Silver Star Story Complete"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-019
  system:
    - SYS-299
    - SYS-362
    - SYS-1963
  constraint:
    - CON-756
  information:
    - INF-119
  objective:
    - OBJ-029
  time:
    - TIM-033
---

# Game: Lunar: Silver Star Story Complete

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The opening cave fight separates command entry, physical melee approach
and the settlement that returns control to the cave.

## Analysis scope

- Version / ruleset: original North American English collector's
  retail PlayStation game published by Working Designs on May 28,
  1999. Disc 1 is SLUS-00628. The second game disc is SLUS-00899.
  No diagnostic screen, checksum or pressing identifier was
  independently verified in either recording.
- Structured analysis target: PLAT-PLAYSTATION in
  [platform coverage](../../platforms/games.json).
- Entry: after opening the icy entrance in White Dragon Cave,
  proceed down the passage into the first ordinary four-Slime
  encounter with Alex, Luna and Ramus. Use Command to inspect
  and allocate the party's opening actions.
- Primary decision loop: choose each available party member's
  command and its target when required. Read the relative positions
  and party HP and MP. After entry, let the committed round play
  out. Ordinary close attacks can move the actor toward a target
  before the strike and leave the actor at a different position.
  Choose again if enemies remain.
- Exit: defeat the four Slimes, read the encounter rewards and
  return to movement in the same cave passage. Stop before the
  next encounter. W2 provides an alternate resolution of the same
  opening fight.
- Included: visible cave-to-battle transition, targeted Attack and
  Healing Song, individual command allocation and batch timing,
  advance toward a melee target, persistent positions within the
  encounter, HP and MP display, clearing the hostile group,
  experience and the observed level increase.
- Excluded: exact turn order, ties, distance and pathing formula,
  attacks that cannot reach after movement, behaviour of an
  obsolete target, menu setup for Tactics, escape, other spell
  variants, retry and save semantics, optional rewards, later
  encounters and bosses, the Sega CD original, Japanese releases,
  the Fan Art reissue as an independently tested pressing,
  handheld remakes and the remaster.
- Potential scoped module: compare two legal starting formations
  against the same enemy and record a melee attack that spends
  its movement without reaching the target.
- Direct-play status: no personal PlayStation execution or
  binary inspection. Two attributed English PlayStation recordings,
  retail packaging, an edition catalogue and two firsthand
  1999 accounts bound the analysis. Only short background frame
  sequences were examined, without audio. W1 is an edited run.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| LU-001 | Working Designs released this English PlayStation edition in May 1999. The disc and box evidence identifies the retail series, while the dated catalogue identifies May 28. The first White Dragon Cave battle in both recordings starts against four Slimes. | Confirmed | Corroborated | High | P1, P2, W1 13:21–13:30, W2 18:47–18:56 |
| LU-002 | Command opens separate selections for the three party members, with target selection for a scoped targeted move. The round then resolves without further command entry. Allies and hostile actions can interleave, and the menu returns with fewer Slimes when a round leaves survivors. | Observation | Corroborated | High | W1 13:29–13:54, W2 18:50–19:14, R1 |
| LU-003 | A committed close attacker advances from its starting position before striking. The next command entry preserves changed positions. W2 independently shows an advance on the opening ice floor. Neither trace determines a universal distance or initiative formula. | Observation | Corroborated | High | W1 13:35–13:54, W2 18:58–19:12, R2 |
| LU-004 | The interface presents Alex, Luna and Ramus separately with level, HP and MP. The Healing Song appears as Luna's queued option and resolves from the back. Her displayed MP changes from 40 to 36 during the cast sequence. | Observation | Corroborated | High | W1 13:50–14:09, W2 approximately 21:10, R2 |
| LU-005 | The battle settles after the last Slime disappears. W1 reports 4 experience points and 24 Silver, then Ramus's increase to level 2 and maximum HP by four. The party returns to the cave and moves. W2 reaches the same cave after the first four Slimes; the following group is outside scope. | Observation | Corroborated | High | W1 14:24–14:51, W2 19:30–19:55, R2 |

## Basic data

- Release / origin: Game Arts, Working Designs, original English
  North American PlayStation retail release, May 1999.
- Mechanical family: FAM-009. A planned hit depends on where the
  actor will move in the adversarial round, and a rear caster can
  use a different action without making the same approach.
- P1: [PlayStation Museum retail box and product record](https://playstationmuseum.com/index.php/product/slus-00628/).
  The preserved packaging and catalogue identify the developer,
  publisher, platform and original disc set; SLUS-00921 is the
  making-of disc and is not part of this fixture.
- P2: [GameFAQs PlayStation release catalogue](https://gamefaqs.gamespot.com/ps/197808-lunar-silver-star-story-complete/data)
  dates the first North American retail line to May 28, 1999
  and lists the later marketing edition separately.
- W1: [Look Back Gaming's English PS1 capture](https://www.youtube.com/watch?v=kKDyZWUaDoE&t=801s).
  Review entry, commands, rounds, result and movement from 13:21
  to 14:51. The author explicitly calls the run segmented and
  edited. The continuous section before the result shows original
  English battle menus and the scoped state changes.
- W2: [Nexus Gaming's English PS1 capture](https://www.youtube.com/watch?v=pwT85Xrc-xw&t=1127s).
  Use the opening encounter from approximately 18:47 to 19:55;
  this trace also shows an actor-level AI assignment. Around 21:10,
  the later cave menu independently shows Healing Song as a
  single-ally heal with cost 4. Later encounters do not establish
  additional scope.
- R1: [Daniel Wagoner's English PlayStation account, June 1999](https://gamefaqs.gamespot.com/ps/197808-lunar-silver-star-story-complete/faqs/3964).
  Use the battle interface and White Dragon Cave sections to
  identify the playable party and command options. The author
  distinguishes the earlier platform versions.
- R2: [Exdeath's PlayStation walkthrough and reference](https://gamefaqs.gamespot.com/ps/197808-lunar-silver-star-story-complete/faqs/3965).
  Use the Range description and the separate spell and enemy
  entries to corroborate movement, Healing Song's use and
  encounter rewards. It does not supply captured disc checksums.
- Claim IDs: LU-001–LU-005.

### Reproducible fixture evidence

1. In W1 enter the cave and advance through the icy passage
   around 13:21–13:28. Confirm four named Slimes against three
   controlled party members. W2 enters the same four-Slime
   fixture around 18:47–18:52 after closing a setup menu.
2. Around 13:29–13:36 in W1 follow Command through the actor
   portraits, Attack and the selected target. The four foes stay
   present during the opening command entry. Follow the first
   committed attacker on the ice from around 13:36 onward.
3. At the returned menu around 13:53, compare the closer
   position of the front fighters and the remaining three Slimes
   with the opening. In W2 compare the starting lineup around
   18:53 with the approach and later forward stance around 19:04.
4. Around 13:57–14:09 in W1 follow Healing Song, the caster's
   rear position and the displayed MP before and after execution.
   Read ally and hostile actions as they resolve before the next menu.
5. Around 14:27–14:38 the last Slime disappears and the
   result reports 4 experience points, 24 Silver and Ramus's
   increased level and maximum HP.
   Follow the party back onto the cave floor, then to the next
   movement around 14:50. Match the alternate W2 settlement
   and stop on the passage before another hostile group.

## Mechanical decomposition

### Action Genes

- ACT-019: select an eligible party member's attack or spell and
  specify its enemy or ally target. LU-002, LU-004.

### System Behaviour Genes

- SYS-299: experience settlement promotes Ramus and reports a
  change to maximum HP. LU-005.
- SYS-362: the finite encounter awards earned progression before
  control returns to the cave. LU-005.
- SYS-1963: the chosen close attack automatically advances its
  actor toward the target, and the actor can start the next order
  from the resulting position. LU-003.

### Constraint Genes

- CON-756: each eligible party member contributes one scheduled
  command to the observed round; a spell occupies that actor's
  choice in place of a normal attack. LU-002, LU-004.

### Information Genes

- INF-119: party names, levels, HP and MP stay available in the
  fixture; comparing two rounds exposes the personal cost of
  Healing Song. The field menu includes the learned spell. LU-004.

### Objective Genes

- OBJ-029: remove all four required Slimes to settle a successful
  first encounter. LU-005.

### Time Genes

- TIM-033: complete party planning before the automatic mixed
  exchange, then choose again if enemies remain. LU-002.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Party moving in the icy corridor | Enter the first visible encounter | Separate battlefield with three controllable allies and four Slimes | LU-001 |
| First combat menu with all required enemies present | Choose Command, issue each available ally's action and relevant target | Menu closes and the round executes without new input | LU-002 |
| Close attack committed with space between actor and Slime | The assigned melee attack resolves | The fighter moves before striking and the new position carries into the next menu | LU-003 |
| Luna at the rear with 40 MP | Let the chosen Healing Song resolve | Her MP reads 36; the rest of the round continues | LU-004 |
| At least one Slime remains | Automatic round finishes | Command entry returns with the remaining enemies and changed positions | LU-002–LU-003 |
| Last required Slime disappears | Victory settles | Displayed experience and Silver, Ramus's level increase and resumed cave movement | LU-005 |

## Strategic and experiential structure

The party can assign a close attack and a restorative spell in the
same planning state. The fighter's advance changes the distance of
subsequent actions. The spell consumes a command and the caster's
own mana. Gained experience is settled only after the remaining
enemies are gone.

## Replay and variation

Both recordings begin against four Slimes and end on the cave floor.
W1 uses the party's manual commands and Healing Song in battle. In
W2, one actor is delegated to AI in Command and the player spends
mana on a field heal later. These are observed decisions in two runs
of the fixture. No save reload or deterministic initiative test was run.

## Adjacent systems and history

The English PlayStation edition was released by Working Designs.
The field menu offers equipment, spells and battle setup. Those
menus and the opening cave form the context for the fixture. This
record uses the original PlayStation rules, with the Sega CD release,
later remakes and remaster outside its evidence boundary.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-019 | Choose a command and its relevant actor target |
| System Behaviour | SYS-299, SYS-362, SYS-1963 | Settle progression and resolve persistent melee approach |
| Constraint | CON-756 | Assign one command to each eligible ally per round |
| Information | INF-119 | Read the separate ally resources and learned option |
| Objective | OBJ-029 | Clear the complete finite enemy group |
| Time | TIM-033 | Resolve automatically after the party commits |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `687` (`GAME-0001`–`GAME-0687`).
- Exact genome matches: none.
- Tied near matches: `GAME-0489` — Golden Sun (`7 / 19 = 0.368421`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Golden Sun (GAME-0489)](golden-sun.md) | ACT-019, CON-756, INF-119, OBJ-029, SYS-299, SYS-362, TIM-033 | Lunar carries the melee approach into the next planning state. Golden Sun has a complete agility-ordered batch with a documented obsolete-attack defence fallback and a separate Djinn state system. Neither of those specific behaviours was used to classify Lunar. | Near, `0.368421` |

## Taxonomy impact

Automatic approach is part of executing the attack against a
previously selected opponent. The same floor has different
positions in the following planning state. A selectable movement
destination, the number of positions moved and a fallback for an
outdated target need separate evidence.

## Negative results

- The actor movement happens after the party confirms its orders.
- One committed command does not imply a separate free move.
- Changed positions remain visible when the menu next returns.
- Healing Song changes the caster's MP without moving her into
  close attack range in this trace.
- The trace cannot establish what a still-unreachable attack
  or an outdated target does across supported commercial builds.

## Delta summary

Eight genes, one newly admitted. The melee approach links a
selected target to physical position within the automatic round.

## New facts

- Each ally gets its own command choice before the round settles.
- A close attacker can advance toward an enemy and retain the
  changed position when the player chooses the next commands.
- A rear ally can instead commit a targeted healing spell.
- The final Slime's removal precedes settlement and resumed movement.

## Principles and design implications

Keep the command-entry boundary visible and preserve the resulting
positions in the next decision state. Give players a way to compare
the cost of spending one ally's round on aid with attacking again.

## Puzzle or game generation potential

An original small cavern encounter could accept one instruction per
explorer and then resolve those instructions together. A close attack
advances one explorer, leaving a new spacing problem when the player
next chooses who should help and who should attack.

## New genes

- SYS-1963

## New combinations

None. All 274 verified combinations were checked; no combination is a proper subset of this genome.

## Taxonomy changes

[Taxonomy Change 434](../../../research/taxonomy-changes/TAXONOMY_CHANGE_434.md).

## New questions

- Does an attack spend the entire round when its permitted approach
  still leaves the chosen target out of reach?
- What happens when the preselected target disappears before impact?
- Does another formation change the outcome for the same orders?

## Next recommended game

Continue Selection 059 with `GAME-0689`, Shadow Point on the original
Oculus Quest retail release.

## Why this game

Physical spacing matters even though the player enters a complete
batch of menu commands. The first short fight exposes the connection
without relying on an inferred turn-order formula.
