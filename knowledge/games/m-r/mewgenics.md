---
game_id: GAME-0514
slug: mewgenics
game_title: Mewgenics
analysis_status: reviewed
reviewed: 2026-11-15
combination_ids: []
gene_ids:
  action:
    - ACT-014
    - ACT-019
    - ACT-652
  system:
    - SYS-004
    - SYS-1289
    - SYS-1453
    - SYS-1454
    - SYS-1455
    - SYS-1456
  constraint:
    - CON-001
    - CON-269
    - CON-795
  information:
    - INF-002
    - INF-043
    - INF-119
    - INF-499
  objective:
    - OBJ-029
  time:
    - TIM-001
---

# Game: Mewgenics

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Cat appearances, spell names, mana costs and tile distances are parameters.

## Analysis scope

- Version / ruleset: released English Windows Steam base product, documented
  launch-day ruleset of 2026-02-10, first battle of The Path. The store
  identifies app 686060 and the release. The launch-day recording transcript
  does not identify an installed build number. Later patches, beta branches,
  consoles, mods and parity with the current Windows build are outside scope.
- Structured analysis target: `PLAT-WINDOWS-PC`; the exact documentary target
  is recorded in `knowledge/platforms/games.json`.
- Primary decision loop: on each allied cat's turn, inspect reachable cells,
  attack reach and available mana. Move the melee cat adjacent to the rat and
  strike. With the ranged cat, combine a normal move and a paid Roll to get a
  shot at Tom Tom. Spend the melee cat's replenished mana on Spit and finish
  the surviving enemy through ordinary turns. Once the tutorial stops
  correcting mistakes, a missed or misdirected shot can consume the attack.
- Entry and exit: take the first controllable melee turn on the first battle
  node of The Path during fresh-start onboarding, using the two supplied
  cats. Exit on the completed battle after Lil' Rat and Tom Tom are both
  incapacitated, before selecting a level-up ability. Quitting or skipping
  the tutorial abandons the analysed attempt and does not settle its battle.
- Included: finite tiled arena and individual turns, one ordinary move and
  one basic attack, current movement and attack indicators, adjacent strike,
  lobbed short shot, mana-funded Roll and repeated Spit, mana replenishment
  at the actor's turn end, a random self buff after downing a unit, scripted
  early retry, later spent misses, possible friendly and fallen-target hits,
  current health and removal of defeated combatants from active turns.
- Excluded: cosmetic selection of the two starting cats, level-up and later
  map nodes, Pebbles, equipment, injuries outside the encounter, breeding,
  inheritance, expedition rewards and house progression. No exact opening
  HP, initiative tie rule, later exhaustion behaviour, restart fidelity or
  ordinary whole-party defeat boundary is inferred for this battle.
- Potential scoped modules: the rest of The Path and the first house night
  need their own complete entry, exit and evidence. This encounter does not
  establish inheritance or ordinary expedition rules.
- Direct-play status: no executable was obtained or run. G1's launch-day
  transcript was read through the fight and its reward boundary. W1 and W2
  cross-check encounter identities and the tutorial's alternative responses.
  W3 supplies general rule context, not an independent capture of the launch
  executable. No recording was played. Transitions are documentary
  predictions. Wrong-input branches were not executed by the Atlas.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| MG-001 | This Windows launch-day encounter has two assigned cats and two required enemies, a rat and Tom Tom. Its battle exit is before the new ability choice. | Observation | Corroborated | High | P1, G1, W1 |
| MG-002 | The active actor can spend one ordinary move and one basic attack. A mana ability does not consume either opportunity by default. | Observation | Corroborated | High | P2, G1, W2 |
| MG-003 | Move selection marks available positions and shows the basic attack's reach. Melee requires adjacency; normal movement alone in the guided ranged opening does not reach Tom Tom. | Observation | Corroborated | High | G1, W1, W2 |
| MG-004 | Roll spends mana to reposition. The melee cat gains mana at turn end and can cast Spit twice on its next guided turn. | Observation | Corroborated | High | P2, G1, W2, W3 |
| MG-005 | The melee cat's Self-Assured passive grants it one undisclosed random stat increase after downing an eligible unit. | Observation | Corroborated | High | G1, W1, W2 |
| MG-006 | The first guided position can be retried after a wrong move. The first guided rat attack can be retried after a miss. Later misses, ally hits and attacks on the rat's body can expend the ranged attack. | Observation | Limited | Medium | W1, W2; G1 confirms the guided success branch |
| MG-007 | The living Tom Tom takes automatic individual turns and can hurt an allied cat. Removing it after the rat settles the encounter. The transcript does not identify exact hit odds or HP formulas. | Observation | Corroborated | High | G1, W1, W3 |
| MG-008 | The paw indicator identifies the current actor. The HUD exposes mana and spell cost, and inspection explains current perks. A projected attack footprint supplies no hit guarantee. | Observation | Corroborated | High | P2, G1, W2 |

## Basic data

- Release / origin: Edmund McMillen and Tyler Glaiel, Windows Steam, 2026-02-10.
- P1: [Developer's Steam product page](https://store.steampowered.com/app/686060/Mewgenics/), release and product boundaries.
- P2: [Developer combat explanation](https://store.steampowered.com/news/posts/?enddate=1673975627&feed=steam_community_announcements), early written description of separate actions and mana. Used only where the launch-day account and released tutorial agree.
- G1: [Gamereactor launch-day transcript](https://www.gamereactor.eu/video/784963/Mewgenics%2B-%2BLivestream%2BReplay/), 2026-02-10. The reporter's choices establish one completed path, not every branch or a binary revision.
- W1: [The Path reference](https://mewgenics.wiki.gg/wiki/The_Path), roles, encounter structure and guided exceptions.
- W2: [Butch's tutorial dialogue](https://mewgenics.wiki.gg/wiki/Butch/Dialogue), combat instructions and documented wrong-input cases. Unused dialogue is excluded.
- W3: [Battle reference](https://mewgenics.wiki.gg/wiki/Battle), scheduled turns and personal reserve rules. The three community reference pages are not independent publications.
- Family: `FAM-009`, tactical forecast and counterplay. Reach is visible but the next enemy decision and random stat increase are not committed previews.

## Mechanical decomposition

| Type | Active genes | Scoped interpretation |
|---|---|---|
| Action | ACT-014, ACT-019, ACT-652 | Move the active cat to a legal tile, select a basic or mana ability and its target, or end the cat's turn when allowed. |
| System Behaviour | SYS-004, SYS-1289, SYS-1453, SYS-1454, SYS-1455, SYS-1456 | Choose a random buff, take enemy turns, restore personal mana, award the down-triggered stat increase, correct early guided errors, and remove defeated combatants while their bodies can still be targeted. |
| Constraint | CON-001, CON-269, CON-795 | Fixed addressed cells, ability reach and resource gates, separate once-per-turn ordinary uses and paid additional abilities. |
| Information | INF-002, INF-043, INF-119, INF-499 | Unpreviewed buff identity, reachable cells, visible personal state and movement-mode attack reach. |
| Objective | OBJ-029 | Incapacitate the fixed two-enemy set. |
| Time | TIM-001 | Resolve each command before the next choice, with individual turn handoffs. |

## Reproducible transitions

| Before | Command or event | Result | Claims |
|---|---|---|---|
| First melee turn, rat outside adjacency | Select the prompted adjacent tile | The cat moves and can still make its basic attack. | MG-002/003 |
| Initial melee movement fails the lesson | Choose a position away from the rat | The guided step supplies another attempt at its prescribed move. | MG-006 |
| First guided melee attack misses | Repeat the attack as instructed | The guided exception allows another attack on the same turn. | MG-006 |
| Melee cat downs the rat | Settle the passive and inspect the effect | The rat stops acting and the cat gains one random stat increase. | MG-005/007/008 |
| Melee cat ends its first turn with insufficient casting mana | End Turn and wait for its next opportunity | Turn end credits its personal mana regeneration; the next guided melee turn has mana for Spit. | MG-004 |
| Ranged cat cannot reach Tom Tom by basic move alone | Use its ordinary move and spend four mana on Roll | The separate displacement can put Tom Tom within the basic shot's reach. The attack remains available. | MG-002/003/004 |
| Ranged cat has the necessary mana before moving | Use Roll first, then select an eligible ordinary move | The spell does not consume the move. The reverse order is specifically acknowledged in the tutorial. | MG-002/006 |
| Ranged cat spends the shot on a miss, ally or defeated rat | Try to make another basic shot this turn | The strike opportunity is spent. It can still use any remaining ordinary move or affordable compatible ability. | MG-002/006 |
| Melee cat has sufficient mana on its second turn | Cast Spit and cast it again | Both casts can resolve within one turn by paying their separate costs. | MG-004 |
| Rat has fallen and Tom Tom remains | End the active cat's turn, or finish Tom Tom with a legal attack | The living enemy can act when scheduled. Its defeat completes the bounded battle. | MG-007 |

## Strategic and experiential structure

- Inspect movement and attack reach together before committing a destination.
  The two allowances alone do not guarantee contact. Roll extends the ranged
  opening at the cost of mana, while ending a turn funds later casts.
- The script distinguishes a rejected early training mistake from a later
  legal shot with the wrong target or a nonlethal outcome. A body still being
  hittable does not make it a member of the living hostile set.
- The nearby positional counterexample is to stand just outside melee reach.
  That tile can be legal movement while the rat remains outside attack range.
  Likewise, possession of Spit does not make it usable with insufficient mana.

## Replay and variation

Assigned combat roles and this first enemy pair are fixed by the tutorial.
Attack choices, positioning and the random buff can differ. No general
procedural battle layout or random tutorial roster enters this signature.

## Adjacent systems and history

Unlike a party-wide planning phase, the player acts through the currently
scheduled individual cat. Unlike one shared action-point budget, the two
ordinary uses and the casting pool are independently checked. A guided retry
of a first lesson is narrower than player-selected rewind of a battle.

## Normalised genome

| Type | Active gene IDs | Candidates or parameters |
|---|---|---|
| Action | ACT-014, ACT-019, ACT-652 | destinations, abilities and handoff |
| System Behaviour | SYS-004, SYS-1289, SYS-1453, SYS-1454, SYS-1455, SYS-1456 | initiative display, buff pool, mana yield, tutorial stage and fallen target |
| Constraint | CON-001, CON-269, CON-795 | tiles, reach, costs and ordinary uses |
| Information | INF-002, INF-043, INF-119, INF-499 | marked tiles, attack footprint, personal indicators and unknown buff identity |
| Objective | OBJ-029 | Lil' Rat and Tom Tom |
| Time | TIM-001 | individual sequential turn handoff |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `513` (`GAME-0001`–`GAME-0513`).
- Exact genome matches: none.
- Tied near matches: `GAME-0486` — Final Fantasy Tactics (`10 / 34 = 0.294118`).
- Supported combination subsets: none.
- Scan date: 2026-11-15.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0486` Final Fantasy Tactics | ACT-014, ACT-019, ACT-652, SYS-004, SYS-1289, CON-001, CON-269, INF-119, OBJ-029, TIM-001 | Both schedule individual actors, permit addressed movement and commands, and require hostile clearance. Gariland preserves speed-fed readiness differently according to decisions and limits the actor to a Move and an Act. The Path's first battle adds separately paid casts and retires its scripted mistake correction before ordinary choices. | Near, `0.294118` |

### Preserved research notes

- New genes: SYS-1453, SYS-1454, SYS-1455, SYS-1456, CON-795, INF-499.
- Classification result: `New gene`.

## Taxonomy impact

- See [TAXONOMY_CHANGE_261](../../../research/taxonomy-changes/TAXONOMY_CHANGE_261.md).
  Reused boundaries and all earlier signatures remain intact.

## Negative results

- No full-game breeding, new combination, tactical spell hand or fixed
  enemy-intent preview is established by this encounter.
- The first documented melee retry does not establish a general freely
  reversible battle history; the later incorrect shot consumes its use.

## Delta summary

## New facts

- [Observation | Corroborated | High] Independent ordinary uses and repeated
  paid casting govern the first tutorial encounter. MG-001–MG-004.
- [Observation | Limited | Medium] Early tutorial steps offer retry while
  later wrong attacks remain spent. MG-006.

## New genes

- SYS-1453, SYS-1454, SYS-1455, SYS-1456, CON-795 and INF-499.

## New combinations

- None. The 274 verified combinations were tested as proper subsets.

## Taxonomy changes

- Six additions and twelve unchanged transfers; see TAXONOMY_CHANGE_261.

## New questions

- The precise first-battle injury, restoration and long-delay branches need
  controlled tests on a documented release. They do not enter this signature.

## Next recommended game

- `GAME-0515` Dino Crisis, original PlayStation release, after this unit passes.
