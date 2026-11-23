---
game_id: GAME-0530
slug: lost-odyssey
game_title: Lost Odyssey
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids: []
gene_ids:
  action:
    - ACT-019
    - ACT-131
    - ACT-199
    - ACT-222
    - ACT-725
  system:
    - SYS-358
    - SYS-362
    - SYS-854
    - SYS-1307
    - SYS-1523
    - SYS-1524
    - SYS-1525
    - SYS-1526
    - SYS-1527
  constraint:
    - CON-269
    - CON-756
  information:
    - INF-119
    - INF-142
    - INF-515
  objective:
    - OBJ-029
  time:
    - TIM-003
    - TIM-033
---

# Game: Lost Odyssey

Use the [canonical vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Enemy names, spell ranks, stocked items and exact input windows are parameters.

## Analysis scope

- Version / ruleset: original North American English Xbox 360 retail
  release, 2008, Disc 1, base game without downloadable content. The
  scoped evidence identifies the release but not an installed title update.
- Structured analysis target: PLAT-XBOX-360, standard controller. The later
  digital and backward-compatible distributions are not the execution target.
- Primary decision loop: use formation and resources to assign a command to
  each eligible party member. Follow the interleaved execution and release
  the trigger during an equipped attack's closing ring cue. Reassess damage,
  Guard Condition, poison and pending actions before the next batch.
- Entry: the checkpoint immediately before the authored Grilgan battle on
  the Ipsilon Mountains peak. Use Kaim and Seth in front and Jansen behind,
  with at least the earlier Bruiser Ring available to Kaim and Flare
  available to Jansen. The entry specifies no exact HP, MP or item stock.
- Exit: Grilgan is defeated and the victory rewards settle, or all active
  party members are downed and the attempt ends. Stop before descending
  the mountain.
- Included: batch commands, one action per eligible member, targeted attacks
  and spells, Defend, consumables, ring equipment and timing, row changes,
  Guard Condition, casting delay, poison, conditional revival and rewards.
- Excluded: the earlier Heavy Tank opening and Kelolon tutorials, preparation
  encounters, ring crafting, learning or linking skills, stealing, grinding
  requirements, exact damage or timing formulas, later battles and ports.
  Pre-equipped defence skills may affect the encounter, but no such skill
  is required for the selected entry.
- Direct-play status: no console, emulator, game video or audio ran.
  The Microsoft product interview and original guide describe the control
  and battle rules. Contemporary written play accounts corroborate the
  Grilgan encounter and accessible loadout. Exact executable timing and
  the enemy's full decision policy are unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| LO-001 | The original Xbox 360 party fights Grilgan at the Ipsilon Mountains peak on Disc 1. Kaim, Seth and Jansen are available, with the early Bruiser Ring and Flare obtainable before the fight. | Confirmed | Corroborated | High | P1, P2, P3, S1, S2 |
| LO-002 | Assign each eligible ally their round command before execution. The party batch then interleaves with hostile actions according to actor speed, action kind and casting timing. The execution icons appear after commitment. | Observation | Corroborated | High | P3 pp. 19–25, S1 |
| LO-003 | In the command menu, choose one compatible ring without spending the round's combat command. During an equipped physical Attack, hold RT to show its contracting outer circle and release against the inner circle. Perfect and Good yield different benefits. Bad gives the weapon attack without the ring bonus. | Observation | Corroborated | High | P2, P3 pp. 20–21, 29–30, S1 |
| LO-004 | Front-row HP supplies the opening Guard Condition. Damage to the front erodes it, reducing protection for the rear. Plain HP recovery does not raise spent protection. Moving a character between rows spends their command and changes the guard calculation. | Observation | Corroborated | High | P3 pp. 27–28, S3 |
| LO-005 | Defend trades a command for a protective state. Ordinary items such as Healing Medicine or Antidote perform a specified effect and expend stock. Guard Heal adds HP recovery to Defend and installed Stand Ready can recover Guard Condition when the defending actor is attacked. | Observation | Corroborated | High | P3 pp. 25–30, 50 and skills appendix, S1, S2 |
| LO-006 | A spell uses available MP and enters the execution order by casting grade. A hit during casting can postpone an unresolved spell, with Guard Condition affecting that chance. The exact delay roll for Grilgan is unknown. | Observation | Corroborated | Medium | P3 pp. 25, 27, S2 |
| LO-007 | Grilgan is Wind-aligned and vulnerable to Fire. Jansen can choose Flare while the front line attacks or protects. Grilgan's Downburst hits the party, and Poison Claw can leave a target taking poison damage at turn end until cured. | Observation | Corroborated | High | P3 p. 50, S1, S2, S3 |
| LO-008 | While the party remains in combat, a downed immortal such as Kaim or Seth can get back up after the documented two-turn wait. Mortal Jansen requires a revival effect during battle. An all-down party cannot wait out defeat. | Observation | Corroborated | High | P2, P3 p. 26, S1 |
| LO-009 | Winning settles experience, skill points and the eligible drop. The original guide lists the Slot Seed reward. A checkpoint precedes the battle and supports retry after defeat. | Observation | Corroborated | High | P3 p. 50, S1, S2 |

## Basic data

- Release / origin: Mistwalker and feelplus, published by Microsoft Game
  Studios, North American Xbox 360 release in 2008.
- Families: tactical forecast and counterplay, and real-time system pressure
  within the attack's execution interval.
- Sources accessed 2026-11-17:
  - **P1** — [Xbox product listing](https://www.xbox.com/en-US/games/store/lost-odyssey/bzb4s8fs8t5b)
    and [publisher's Xbox 360 distribution history](https://news.xbox.com/en-us/2016/12/14/lost-odyssey-and-blue-dragon-are-now-available-digitally-plus-lost-odyssey-free-for-limited-time/),
    identifying the title and original hardware lineage. The
    [retail box and disc catalogue](https://rfgeneration.com/cgi-bin/getinfo.pl?ID=U-115-S-02660-A)
    identifies the North American four-disc edition.
  - **P2** — [Microsoft Game Studios product-manager interview](https://archive.rpgamer.com/games/other/xbox2/losto/lostointerview.html),
    concerning grades of the timed Aim Ring System and distinct mortal
    and immortal behaviour.
  - **P3** — [Prima Official Game Guide, ISBN 9780761558804](https://books.google.com/books/about/Lost_Odyssey.html?id=_EmgPQAACAAJ)
    (2008), Combat pp. 19–30, Grilgan p. 50 and skill appendix; combat
    phases, ring operation and replacement, guard, magic, recovery and
    the original encounter were reviewed in the guide text.
  - **S1** — [Chris Quigley's Xbox 360 Disc 1 walkthrough](https://gamefaqs.gamespot.com/xbox360/928334-lost-odyssey/faqs/51958),
    controls, battle system and the Ipsilon Mountains peak, including
    the original ring source, Grilgan and immediate reward.
  - **S2** — [February 2008 firsthand written encounter report](https://thirdworldgamer.blogspot.com/2008/02/january-npd-figures-sony-on-top.html)
    and [Freeola walkthrough of Grilgan](https://walkthrough.freeola.com/game/9481/xbox-360/lost-odyssey.html).
    These corroborate the use of fire and fast restorative items. The
    embedded recording was not opened or analysed.
  - **S3** — [Contemporary Hooked Gamers Xbox 360 play account](https://www.hookedgamers.com/x360/lost_odyssey/review/article-209-2.html),
    describing the ring input and rear-line Guard Condition. The
    [boss guide](https://gamefaqs.gamespot.com/xbox360/928334-lost-odyssey/faqs/55931)
    corroborates the specific encounter attacks and early fire tactic.
- Claim IDs: LO-001–LO-009.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-019` to choose one eligible member's command and its legal target.
- Reuse `ACT-131` to issue a restorative, Antidote, revival item or
  available elemental bomb from a finite inventory.
- Reuse `ACT-199` to equip a compatible ring in the command menu. One
  ring occupies that slot. Swapping that equipment is not a second
  scheduled action in the round.
- Reuse `ACT-222` for the RT hold and release during the attack selected
  earlier. Its timing cannot change that attack's target.
- New `ACT-725`: assign a row change instead of the moving actor's attack,
  spell or item in that round. The membership change updates which actors
  contribute to and benefit from rear protection.
- Claim IDs: LO-002–LO-005, LO-007.

### System Behaviour Genes

- Reuse `SYS-358`: grade the trigger release and apply the equipped ring's
  modifier. A Bad grade leaves the ordinary attack in play.
- Reuse `SYS-854`: the enemy's Wind affinity gives the legal Fire effect an
  advantage, and damage can settle its defeat.
- Reuse `SYS-1307`: a scheduled Defend reduces incoming damage. Optional
  prepared abilities can heal HP when defending or restore guard when
  an attack hits the defending actor.
- Reuse `SYS-362`: defeat settles eligible encounter awards including the
  documented Slot Seed for the un-stolen route.
- New `SYS-1523`: a committed round interleaves eligible actions by
  actor speed and action scheduling. Items and Defend tend to resolve
  early, while a spell uses its casting grade. No exact priority table
  or speed-tie formula is asserted.
- New `SYS-1524`: front-row HP contributes to a distinct guard reserve.
  Front-line hits wear down the reserve, its strength reduces received
  rear-row damage, and row changes and declared guard recovery affect it.
  Healing HP alone does not refund spent guard.
- New `SYS-1525`: enemy contact against a casting actor can defer the pending
  spell to a later round. Guard Condition affects eligibility for the
  delay outcome without dictating a guaranteed delay on every hit.
- New `SYS-1526`: a downed immortal can return after the designated number
  of turns inside a still-active battle. A mortal has no equivalent
  automatic return. An item can resolve revival before that wait where legal.
- New `SYS-1527`: a landed poison-inflicting attack can attach a persistent
  damaging status whose ticks resolve at the turn boundary until cleared.
- Claim IDs: LO-002–LO-009.

### Constraint Genes

- Reuse `CON-269`: abilities require a legal actor, target and resources.
  Magic needs eligible access and enough MP. A stocked item must be
  compatible with the selected target.
- Reuse `CON-756`: each eligible member has one queued combat command
  per round. Defend and changing rows use that opportunity. The equipment
  menu does not grant another scheduled action.
- Claim IDs: LO-002–LO-006, LO-008.

### Information Genes

- Reuse `INF-119`: inspect party HP, MP, status and available loadout.
- Reuse `INF-142`: the target circle and contracting outer circle show
  the release cue during the executing attack. They do not announce
  the grade in advance.
- New `INF-515`: read party Guard Condition separately from character HP.
  During resolution the live icons show the remaining action order
  and can show a pending cast's remaining turns. That queue is not a
  pre-commit list of enemy intentions.
- Claim IDs: LO-002–LO-006.

### Objective Genes

- Reuse `OBJ-029`: defeat the finite enemy Grilgan before the available
  party is downed. Experience and the optional drop belong to settlement.
- Claim IDs: LO-001, LO-008, LO-009.

### Time Genes

- Reuse `TIM-033`: issue the party batch before the interleaved round begins.
- Reuse `TIM-003`: once the equipped attack starts, its real-time outer ring
  closes and passes the best release point even if the player waits.
- Claim IDs: LO-002, LO-003.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Three eligible party members on the peak, with the batch incomplete | Choose Kaim's Attack against Grilgan | Command is queued. The attack and its ring cue do not begin until remaining choices are committed. | Choosing a target is earlier than executing the timed input | LO-001, LO-002 |
| Equipped Kaim advances during execution | Hold RT and release as the rings align | Perfect gives the stronger applicable ring result. A near release gives a lesser benefit. Bad gives no additional ring effect. | Outcome grading changes a completed command without choosing a new one | LO-003 |
| Front guard has fallen and one actor is wounded | Use ordinary Healing Medicine on the actor | HP rises if the item resolves. The spent Guard Condition is not restored by the HP gain. | Current vitality and rear protection are distinct measures | LO-004, LO-005 |
| Jansen remains behind the front row, and Kaim chooses a row move | Resolve the move instead of an attack | Kaim changes rows and the reserve adjusts to the front contribution. | Row membership is tactical and costs an action during battle | LO-004 |
| Jansen has enough MP and a selected Flare is pending | Allow execution to reach its cast | The Fire effect answers Grilgan's affinity. An intervening enemy hit may delay it. | Timing role differs from the ring prompt | LO-006, LO-007 |
| Poison Claw has left an actor poisoned | Use an available Antidote before later poison ticks | The item removes poison if it resolves and is spent. It does not undo earlier damage. | Clearing a status and restoring health are separate | LO-005, LO-007 |
| Seth is down and another ally keeps the battle alive | Complete the immortal recovery wait | Seth can return automatically. The same wait does not return Jansen. | Continuation depends on character class | LO-008 |
| Grilgan reaches defeat and the party is still active | Complete victory settlement | The encounter's rewards are granted and field control resumes. | The local goal does not require the rest of the mountain route | LO-009 |

## Strategic and experiential structure

A stronger ring release rewards execution of a decision made earlier.
Assigning both front-line characters to attacks creates more opportunities
for damage but spends the commands that could protect them or treat poison.
A protected Jansen can exploit the Fire matchup. When the front guard
erodes, restoring only HP leaves the rear under pressure. Fast items,
committed defence and changes to the battle rows answer different parts
of that state. No fixed winning command string or enemy attack cycle is
assumed.

## Replay and variation

- The boss, party candidates and checkpoint are authored. Starting item
  counts, equipped passives, command priorities, attack grades and the
  boss's chosen actions can change the observed sequence.
- Compare an ordinary bad release and a Perfect release with the same
  equipped ring. Compare a plain heal and a documented guard-restoring
  defence after rear protection has fallen.
- The individual speed comparison, casting interruption chance and damage
  formula remain outside the source-backed rule boundaries.
- Claim IDs: LO-002–LO-009.

## Adjacent systems and history

- Aim Ring modifies a selected turn attack, in contrast to the encounter's
  deliberation phase. The title's larger memory narrative, linking and
  equipment-mastery progression do not supply prerequisites in this packet.
- The game permits equipment changes in the command screen independently
  of row-change commands. Ring recipes and multi-skill assembly do not
  need to be reconstructed to analyse the fight.
- Claim IDs: LO-001, LO-003–LO-005.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-019`, `ACT-131`, `ACT-199`, `ACT-222`, `ACT-725` | commands, item, one ring, release, row move |
| System Behaviour | `SYS-358`, `SYS-362`, `SYS-854`, `SYS-1307`, `SYS-1523`, `SYS-1524`, `SYS-1525`, `SYS-1526`, `SYS-1527` | grade, settlement, affinity, defence, order, front reserve, delayed cast, immortal revival, poison |
| Constraint | `CON-269`, `CON-756` | available resources, actor and target, one command |
| Information | `INF-119`, `INF-142`, `INF-515` | character state, timing cue, guard and execution order |
| Objective | `OBJ-029` | one authored boss and party survival |
| Time | `TIM-003`, `TIM-033` | real-time release inside a batched round |

Canonical signature:

`ACT-019,ACT-131,ACT-199,ACT-222,ACT-725; SYS-358,SYS-362,SYS-854,SYS-1307,SYS-1523,SYS-1524,SYS-1525,SYS-1526,SYS-1527; CON-269,CON-756; INF-119,INF-142,INF-515; OBJ-029; TIM-003,TIM-033`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `529` (`GAME-0001`–`GAME-0529`).
- Exact genome matches: none.
- Tied near matches: `GAME-0489` — Golden Sun (`10 / 30 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0489` — Golden Sun | `ACT-019`, `ACT-131`, `CON-269`, `CON-756`, `INF-119`, `OBJ-029`, `SYS-1307`, `SYS-362`, `SYS-854`, `TIM-033` | Both assign a full party batch with one command per eligible member, then resolve an interleaved encounter using action costs, affinity, defence and rewards. Golden Sun also schedules Djinn Set, Standby and shared summons. Lost Odyssey grades a timed release during a ring-equipped attack and maintains a front-row guard reserve that protects the casting row. | Tied near (`0.333333`) |

### Preserved research notes

- New genes: `ACT-725`, `SYS-1523`–`SYS-1527`, `INF-515`.
- Classification result: `New gene`.
- Evidence and reasoning: protect the distinct boundaries of command
  commitment, equipped attack grading, guard wear and revival.

## Taxonomy impact

- Registry changes: seven Active additions and fifteen transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_277](../../../research/taxonomy-changes/TAXONOMY_CHANGE_277.md).

## Negative results

- No source justifies a measured original ring window, deterministic enemy
  pattern, or an exact protection formula from opening party stats.
- The selected fight does not demonstrate a larger Skill Link or crafting
  interaction, and it supplies no timed enemy parry command.

## Delta summary

## New facts

- [Observation | Corroborated | High] One scheduled attack may still
  take a live quality input. Guard Condition can degrade independently
  of restored character HP.

## New genes

- [Observation | Corroborated | High] Seven new boundaries are reviewed
  in `TAXONOMY_CHANGE_277`. The casting-delay assessment is Medium.

## New combinations

- [Observation | Corroborated | High] No new combination proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_277`.

## New questions

- How exactly do frame rate and title update affect the original
  three Aim Ring outcomes?

## Next recommended game

- [Hypothesis | Limited | Medium] PlayStation 5 *The Midnight Walk*.
- Optimisation criterion: compare ring-centred timing feedback with a
  short path governed by flame and state-dependent perception.
- Backlog impact: advance Selection 041 to its ninth candidate.

## Why this game

- [Hypothesis | Limited | Medium] A single scripted battle makes it
  possible to observe the ring, guard and turn schedule without conflating
  them with the complete party progression.
