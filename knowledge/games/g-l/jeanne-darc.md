---
game_id: GAME-0679
slug: jeanne-darc
game_title: "Jeanne d'Arc"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-014
    - ACT-019
  system:
    - SYS-004
    - SYS-299
    - SYS-362
    - SYS-1285
    - SYS-1950
    - SYS-1951
  constraint:
    - CON-001
    - CON-011
  information:
    - INF-119
    - INF-625
  objective:
    - OBJ-029
  time:
    - TIM-018
---

# Game: Jeanne d'Arc

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Stage, roster, turn limit, command names and result values are fixture parameters.

## Analysis scope

- Version / ruleset: original North American English PSP commercial
  base game, Sony Computer Entertainment America UMD UCUS-98700,
  released August 21, 2007. First story visit to Stage 2, Holy Armor,
  in Domrémy. The traces show the English PSP rules and interface.
  Their disc image, patch and capture hardware are unverified.
- Structured analysis target: PLAT-PLAYSTATION-PORTABLE in
  [platform coverage](../../platforms/games.json).
- Entry: confirm Sortie from the Holy Armor objectives panel. Jeanne,
  Liane and Roger are available on the first player phase, with Jeanne
  still in her ordinary form.
- Primary decision loop: select one available ally, read reachable
  positions and attack and counter forecasts, then commit movement
  and an eligible command. End the player phase for hostile responses.
  In player turn 3, use the armour acquired in the scripted event to
  defeat a reachable enemy. Use Godspeed to reposition and attack
  again while still in that same phase. When the form expires, finish
  the remaining enemies with ordinary commands while keeping Jeanne
  alive within the 10-turn limit.
- Exit: the last hostile, the English Officer in W1, is defeated
  during player turn 8. Read the complete Stage Spoils before the
  following story scene.
- Included: tile occupancy and traversable routes, independent ally
  commands, phase handoff, attack and counter chances, displayed
  current resources, one observed restorative item, the scripted
  form and its expiry, repeatable defeat-triggered reactivation and
  completion credit.
- Excluded: optional hidden treasure, skill binding and loadouts,
  later voluntary transformation, alternate forms, unplayed Coup de
  Grace commands, general Burning Aura and Unified Guard formulae,
  exact height thresholds, movement after every possible ordinary
  command, timeout and simultaneous defeat settlement, other stages,
  reissues and free encounters.
- Potential scoped module: reproduce Burning Aura and Unified Guard
  with paired input states in a later battle.
- Direct-play status: no personal PSP execution or binary inspection.
  The publisher confirms the original commercial release. The full
  stage in W1 supplies the main before-and-after observations. W2
  corroborates the scripted transformation, tutorial and live
  Godspeed reactivation. The original-system guides corroborate
  stage conditions, command roles and transformation rules. Neither
  Jeanne's defeat nor timeout was induced. Frames were inspected in
  the background with audio excluded.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| JDA-001 | Level-5's tactical game shipped for PSP in North America on August 21, 2007. UCUS-98700 is the English North American disc identity for the analysis target. | Observation | Direct | High | P1, P2 |
| JDA-002 | Stage 2 begins with Jeanne, Liane and Roger, requires every enemy defeated and declares defeat if Jeanne falls. Player and enemy phases alternate within a numbered battle turn. The HUD and guides establish a 10-turn limit. The stage lists five Orcs, one Orc Knight and one English Officer in both guides. | Observation | Corroborated | High | W1 22:42–24:04, R1, R2 |
| JDA-003 | Select an ally and use the marked route to an open reachable tile. An eligible attack opens separate attack and possible counter rows with damage and percentages. Both actors' resources are visible. Approaching from another side can alter the projected result. Roger uses a carried Healing Herb to restore HP on turn 3. | Observation | Corroborated | High | W1 23:00–23:50, 29:15–29:35, 30:18–30:23 and 33:00–34:20, R2 Combat School |
| JDA-004 | Holy Armor is granted by a scripted event between the turn 2 enemy actions and controllable player turn 3. The tutorial identifies Godspeed and Coup de Grace and then the live HUD shows Jeanne armoured with two turns remaining. The tutorial describes later Soul Power use, which is not the input that triggers this scene. | Observation | Corroborated | High | W1 26:22–28:07, W2 about 23:45–24:55, R2 |
| JDA-005 | Defeating an enemy while transformed renews Jeanne's movement and action. The displayed turn remains 3/10 and the armour remainder stays at two turns across multiple attacks. The renewed actor can select another route and another eligible target. Character experience and a level-up are visible during the chain. | Observation | Corroborated | High | W1 28:05–29:55, W2 24:50–25:20, R2 Godspeed |
| JDA-006 | The armour has one turn left on player turn 4. Jeanne is in ordinary form at the start of turn 5. A later normal-form defeat on that turn does not trigger the observed Godspeed renewal. | Observation | Corroborated | High | W1 30:27–32:30, R2 Transformation |
| JDA-007 | The last enemy is defeated on turn 8 in W1. The result settles at 236 EXP, 100 G, one Healing Herb and one Heal skill stone. Intermediate counts animate toward that receipt. | Observation | Corroborated | High | W1 35:14–35:45, R1, R2 Holy Armor |

## Basic data

- Release / origin: Level-5 and Sony Computer Entertainment America.
  The accepted fixture is the original retail PSP story battle.
- Puzzle family: FAM-009. Choosing the attacking tile controls the
  forecast exchange and the reachable follow-up options during Godspeed.
- P1: [Sony's 2007 North American release announcement](https://sony.mediaroom.com/2007-08-21-Jeanne-dArc-Delivers-a-Beautifully-Crafted-Tactical-Role-Playing-Game-RPG-Adventure-for-PSP-Playstation-Portable).
  Establishes the release and tactical transformation affordance.
- P2: [North American UMD catalogue and product photographs](https://www.vgcollect.com/item/5237).
  Establishes the commercial disc identity independently of the traces.
- W1: [Sieffre Plays, PSP story recording](https://www.youtube.com/watch?v=6lmXE6UHDds&t=1361s).
  Inspect from the routing panel through the turn 8 result. The two
  tutorial pages and the on-board Godspeed notices are distinct receipts.
- W2: [rpgbaklog, PSP opening chapters](https://www.youtube.com/watch?v=7dIX3m4TF4k&t=986s).
  A second English PSP capture of Stage 2. It corroborates the armour
  and reactivation. Its roster statistics and prior progression do
  not establish the same numerical starting state.
- R1: [darklao, Jeanne d'Arc walkthrough](https://gamefaqs.gamespot.com/psp/934454-jeanne-darc/faqs/50626).
  Stage 2 roster, enemy set, defeat rule and rewards.
- R2: [Paul Vhayste, PSP combat rules and Stage 2](https://www.supercheats.com/psp/walkthroughs/jeannedarc-walkthrough02.txt).
  See CBT003, CBT005–008 and WLK003 for the phase, commands, temporary
  form, refreshed actor opportunity and Holy Armor resolution.
- Claim IDs: JDA-001–JDA-007.

### Reproducible fixture evidence

1. At about 22:42–22:50 in W1, read the Stage 2 objectives and
   enter the board using Sortie. The party starts in the lower village
   approach and the HUD starts at 1/10. Route Liane or Roger to an
   unoccupied blue tile. The matching enemy phase follows when the
   party is done, with its own actions before player turn 2.
2. Wait through the scripted scene at the end of turn 2. Read
   the two armlet tutorial pages shown at about 27:50–27:58.
   Inspect the player turn 3 HUD after the tutorial closes to
   see the armoured unit and its two-turn count.
3. In W1, choose an Orc within attack reach at about 28:05.
   Its HP drops to zero. The same Jeanne is available again.
   Move and attack an eligible enemy, then repeat as a target
   and route permit. At about 29:30 the Orc Knight's defeat
   displays Godspeed; the movement grid then reopens. The HUD
   is still on the third player turn.
4. Use the remaining allies without assuming that each reactivation
   refreshes the whole party. Roger uses a Healing Herb on himself
   near 30:20. In player turn 4 inspect the one-turn remainder.
   See the reversion at the beginning of player turn 5 around
   31:40. Jeanne's ordinary-form kill around 32:20 produces no
   further reactivation.
5. Reach the English Officer and use eligible attacks while
   tracking its counter forecast. Finish the remaining enemy in
   player turn 8. At 35:44, after the result counters animate,
   Stage Spoils shows the full credit and items. Stop at this
   receipt.

## Mechanical decomposition

### Action Genes

- ACT-014: move a chosen ally to a reachable empty tile. JDA-003.
- ACT-019: select an available ally's eligible command and its
  target, including an attack or recovery. JDA-003, JDA-005.

### System Behaviour Genes

- SYS-004: attack and eligible counter outcomes use stated chances.
  This is independent of whether a successful hit finishes a unit.
  JDA-003.
- SYS-299: a defeat awards character experience and can advance
  level, as shown within the armour chain. JDA-005.
- SYS-362: the cleared battle grants its scoped spoils. JDA-007.
- SYS-1285: use a carried Healing Herb as a deliberate restorative
  command. JDA-003.
- SYS-1950: equip temporary Holy Armor at the scripted event and
  return to normal when the displayed term expires. JDA-004, JDA-006.
- SYS-1951: renew only the transformed actor's move and action
  after it defeats an enemy. The phase and the duration stay
  unchanged during the observed chain. JDA-005, JDA-006.

### Constraint Genes

- CON-001: the authored tactical grid supplies stable tile locations.
  JDA-002, JDA-003.
- CON-011: each occupied endpoint is exclusive. Building barriers and
  eligible terrain constrain the route independently of occupancy.
  JDA-003.

### Information Genes

- INF-119: read the units' current HP, MP, experience and state,
  including the armlet-form remainder. JDA-003–JDA-006.
- INF-625: compare the prospective attack and counter outcomes as
  distinct rows before committing. JDA-003.

### Objective Genes

- OBJ-029: clear the finite required enemy group while keeping the
  named protagonist alive. The stage applies its 10-turn horizon.
  JDA-002, JDA-007.

### Time Genes

- TIM-018: sides alternate multi-command phases. The player can
  choose which allied unit to use inside the phase rather than
  taking a new battle turn for each individual command. The turn
  advances after the opposing phase. JDA-002, JDA-005.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Holy Armor objectives visible | Sortie | Three available allies in player phase 1/10 | JDA-002 |
| Selected ally and reachable grid | Confirm a vacant legal destination, then select an attack target | Unit relocated and attack and counter forecast available | JDA-003 |
| Enemy phase 2 ending, ordinary Jeanne | Scripted armlet scene and tutorial finish | Armoured Jeanne ready in player phase 3/10 with two turns remaining | JDA-004 |
| Armoured Jeanne has used an attack | That attack defeats an enemy | Godspeed opens a fresh move and action for Jeanne at 3/10 | JDA-005 |
| Renewed Jeanne, another reachable enemy | Move and defeat another target | Another reactivation, same battle turn and remaining armour duration | JDA-005 |
| Armour at two turns, then one | Advance through player turns 4 and 5 | One turn visible at 4/10, ordinary Jeanne at 5/10 | JDA-006 |
| Ordinary Jeanne, remaining hostiles | Defeat the last opponent at 8/10 | Stage completion and settled spoils | JDA-007 |

## Strategic and experiential structure

A position offers both an immediate attack and a potential route to
the next opponent. Godspeed makes those two decisions dependent.
A foreseeable defeat can turn a spent activation into a new route,
but the whole phase and two-turn form duration remain independent.
After expiry, the remaining enemies still require ordinary turns.

## Replay and variation

Both traces demonstrate the authored first transformation and a
renewed opportunity after a defeat. They need not defeat the same
enemy first or show identical attack values. The observed clear
on turn 8 is one successful route; the guides and HUD provide the
10-turn horizon independently of that finish.

## Adjacent systems and history

The second armlet help page describes the general Soul Power command.
Later manual activation falls outside the scripted entry accepted
here. Burning Aura, Unified Guard and separately equipped skill
stones can be tested independently in a follow-up fixture.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-014, ACT-019 | Choose a reachable tile, command and target |
| System Behaviour | SYS-004, SYS-299, SYS-362, SYS-1285, SYS-1950, SYS-1951 | Resolve chance, recovery, credit, short armour state and reactivation |
| Constraint | CON-001, CON-011 | Tile identity, occupancy and terrain barriers |
| Information | INF-119, INF-625 | Read unit resources and both sides of an exchange |
| Objective | OBJ-029 | Clear every required enemy with Jeanne alive before the limit |
| Time | TIM-018 | Advance exclusive phases with several commands in each |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `678` (`GAME-0001`–`GAME-0678`).
- Exact genome matches: none.
- Tied near matches: `GAME-0486` — Final Fantasy Tactics (`10 / 30 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Final Fantasy Tactics (GAME-0486)](../a-f/final-fantasy-tactics.md) | ACT-014, ACT-019, CON-001, CON-011, INF-119, OBJ-029, SYS-004, SYS-1285, SYS-299, SYS-362 | Both select, move and command individual allies on an exclusive grid. Final Fantasy Tactics grants individual turns through Charge Time. Jeanne d'Arc uses player and enemy phases, a temporary armlet form and a qualifying defeat that reopens the same actor's options in the current phase. | Near, `0.333333` |

## Taxonomy impact

Separate the temporary form on the existing unit, the defeat
that restores its move and action, and the two-sided pre-attack
forecast. Reuse ordinary move, command, recovery, experience,
reward, grid, unit display, hostile objective and phase genes.

## Negative results

- The initial armour entry is scripted. The manual Transform
  instruction on the help page does not describe the initiating
  input for this battle.
- Godspeed does not increment the displayed battle turn or reset
  the displayed armour duration in the observed chain.
- The ordinary-form defeat on player turn 5 does not restore
  Jeanne's move and action. Defeat by timeout was not exercised.

## Delta summary

Fourteen genes, three new and eleven reused. The fixture covers one
full story battle, from Sortie through temporary armour, linked
reactivations and the receipt after the final enemy.

## New facts

- A defeat can refresh a single actor without advancing the battle
  clock or extending a form that expires on that clock.
- An attack forecast can reveal the counter as a separate
  commitment risk even when the actor has several further
  movement opportunities available through Godspeed.

## Principles and design implications

Separate the turn budget, form duration and earned action renewal.
An attack choice can be evaluated on expected damage, counter
exposure and the options unlocked by a possible defeat.

## Puzzle or game generation potential

Build an original tactical fixture in which an actor can use a
short form to earn repeated local activations. Use at least one
reachable opponent who survives the first attack, so a player can
distinguish a hit from the actual renewal predicate.

## New genes

- INF-625
- SYS-1950
- SYS-1951

## New combinations

None admitted. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[Taxonomy Change 425](../../../research/taxonomy-changes/TAXONOMY_CHANGE_425.md).

## New questions

- What happens if the tenth opposing phase ends with a hostile active?
- Which activation order best separates one positional aura from
  an adjacent ally's defensive response?
- Does a counter defeat while armoured renew an opportunity under
  the same exact conditions as the demonstrated player attack?

## Next recommended game

Continue Selection 058 with `GAME-0680`, the commercial Meta Quest
release of Ghost Town. Follow one observed investigation or
manipulation sequence through a concrete progress receipt.

## Why this game

Its short tactical form renews one actor's opportunity repeatedly
without giving the whole party a new turn.
