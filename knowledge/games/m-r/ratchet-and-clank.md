---
game_id: GAME-0404
slug: ratchet-and-clank
game_title: Ratchet & Clank
analysis_status: reviewed
reviewed: 2026-09-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-341
  system:
    - SYS-215
    - SYS-578
    - SYS-1083
  constraint:
    - CON-578
  information:
    - INF-073
    - INF-119
    - INF-125
  objective:
    - OBJ-237
  time:
    - TIM-003
---

# Game: Ratchet & Clank

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Ratchet, Clank,
Novalis, the Bomb Glove, the wrench, the three terminal guards, the Kerwan
Infobot and the courier ship are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: the original North American English 2002 PlayStation 2
  release by Insomniac Games and Sony Computer Entertainment America. The
  exact disc revision was not inspected. This is not the 2016 PlayStation 4
  reimagining, a later series entry or a remastered edition.
- Structured target: the first Novalis visit's **crater / find-a-new-ship**
  mission, not the whole planet. Sony's original announcement establishes the
  PS2 title and two contemporary written original-game routes independently
  describe the mission.
- Entry: ordinary control after Ratchet and Clank crash on Novalis, with the
  starting wrench and Bomb Glove available, before dropping to the crater.
  No later acquired gadget, bought weapon, visited planet or optional Gold
  Bolt is assumed.
- Primary decision loop: read the local map, current health and active weapon;
  move and jump through the crater's broken traversal line; change between
  unlimited wrench strikes and finite Bomb Glove throws according to enemy
  reach and ammunition; survive live robot fire; defeat the final guards by
  the parked ship; speak to the rescued chairman and accept the Infobot and
  use of the courier ship.
- Positive terminal: the finite terminal guard group is defeated, the
  chairman's rescue reward has granted the Kerwan Infobot and courier-ship
  access, and ordinary control remains on Novalis. Taking the ship to
  Kerwan is the next route, not this packet's required terminal.
- Negative attempt boundary: lethal damage or an unrecoverable fall before
  the rescue fails the current traverse/encounter. The exact restart point
  and retained transient state have not been verified on an original disc.
  A missed jump that merely returns Ratchet to safe ground is not terminal.
- Included: direct crater traversal, jumping across the broken bridge,
  switching starting weapons, direct wrench and bomb attacks, finite bomb
  reserve and eligible ammunition refill, current health and damage, live
  hostile response, map/mission information, defeat of the guards at the
  ship, chairman interaction and the two-part travel reward.
- Excluded: the separate waterworks route and optional 500-bolt Aridia
  Infobot; the optional bolt-crank, dive and destructible-boulder Gold Bolt
  detour; the later Hydro-Pack-only Gold Bolt; purchased Pyrocitor and other
  weapons; Heli-Pack, Swingshot, Trespasser and all later gadget gates;
  boarding the courier ship, subsequent planets, New Game+ and remake rules.
- Gadget-gate finding: no acquired gadget gates the selected first-visit
  crater route. The starting Bomb Glove is an optional ranged combat tool in
  this packet, not a newly unlocked world-access key. The selection question
  therefore has a negative result for this bounded mission; the optional
  bolt-crank path is recorded as a separate possible module, not smuggled in
  as mandatory.
- Reproducibility: on the original North American PS2 disc, record the exact
  revision, first Novalis loadout, map and health, active weapon and bomb
  reserve, every jump and hostile encounter, final guard count, dialogue,
  Infobot possession, ship availability and any death/retry state. Repeat
  once using only the wrench and once with a legal bomb expenditure. The
  guides establish the causal route but do not establish exact enemy AI,
  damage values, ammunition-drop schedule or checkpoint retention.
- Direct-play status: no disc, emulator, original gameplay image, video,
  audio or input trace was opened. A putative online manual scan denied
  access, so no claim below cites its unread contents. The two written
  routes are first-hand guides but not a binary-level verification.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `RC-001` | The selected title is Insomniac's original 2002 PS2 game, not the 2016 reimagining | Confirmed | Direct | High | P1 |
| `RC-002` | Novalis follows the opening Veldin crash and offers a crater mission to find a replacement ship | Observation | Corroborated | High | S1, S2 |
| `RC-003` | Ratchet directly traverses the crater and broken bridge while nearby enemies attack in real time | Observation | Corroborated | High | S1, S2 |
| `RC-004` | The starting wrench and Bomb Glove are usable against route hostiles; the latter spends finite ammunition while the wrench does not | Observation | Corroborated | Medium | S1, S2 |
| `RC-005` | Clearing the guards at the ship lets the chairman award the Kerwan Infobot and courier-ship access | Observation | Corroborated | High | S1, S2 |
| `RC-006` | The waterworks mechanic's 500-bolt Aridia Infobot and the bolt-crank Gold Bolt branch are separate first-visit options, not conditions of the ship rescue | Observation | Corroborated | High | S1, S2 |
| `RC-007` | The Hydro-Pack-dependent Novalis collectible cannot be assumed on the first visit | Observation | Corroborated | High | S1, S2 |
| `RC-008` | Quick Select and the map are available in the original controller description; the guide does not establish that weapon selection pauses hostile motion | Observation | Direct | Medium | S1 |
| `RC-009` | The exact checkpoint, inventory retention and enemy reset after a Novalis death remain unverified for this selected disc | Hypothesis | Limited | Low | S2 |

## Basic data

- Origin / platform: Insomniac Games, Sony Computer Entertainment America,
  original PlayStation 2; `PLAT-PLAYSTATION-2`.
- Puzzle family: real-time system pressure (`FAM-010`), with traversal and
  combat jointly determining whether the bounded rescue can finish.
- **[P1]** [Sony Computer Entertainment America's 1 May 2002
  announcement](https://sony.mediaroom.com/2002-05-01-Ratchet-Clank-Revolutionizes-the-Action-Platform-Genre),
  accessed 2026-09-25, establishes the original PS2 product, developer and
  broad weapon/gadget/planet-travel premise, not specific Novalis mechanics.
- **[S1]** [RStein, original PS2 *Ratchet & Clank* written
  guide](https://gamefaqs.gamespot.com/ps2/561107-ratchet-and-clank/faqs/20119),
  sections 2, 3 and 4.2, accessed 2026-09-25. It documents controller
  mappings, crates, three Novalis areas and their separate missions. The
  author used an English-language European release and explicitly disclaims
  knowledge of North American differences. Button contradictions in later
  special-move lines are not used as exact control evidence.
- **[S2]** [ZoopSoul, independent original PS2 written
  walkthrough](https://gamefaqs.gamespot.com/ps2/561107-ratchet-and-clank/faqs/20673),
  section VII.b, accessed 2026-09-25. It describes the waterworks, labels
  the bolt-crank route optional and separately traces the crater, guard
  battle, Kerwan Infobot and ship. It is a first-hand route account, not
  original source code or a captured disc trace.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly move, jump and cross the crater's broken
  bridge; jump distance and bridge geometry are route parameters.
- Existing `ACT-164`: choose the carried Bomb Glove or wrench as the active
  weapon. The selection mechanism is not assumed to pause the world.
- Existing `ACT-161`: strike a reachable robot with the wrench or commit a
  Bomb Glove throw against it.
- Existing `ACT-341`: interact with the rescued chairman and accept the
  authored Infobot/ship-access reward.

### System Behaviour Genes

- Existing `SYS-215`: robots move, shoot and receive direct weapon damage
  while Ratchet remains under live control.
- Existing `SYS-578`: hostile hits reduce current health; eligible Nanotech
  replenishes missing health, while zero defeats the current attempt.
- New `SYS-1083`: clearing the finite hostile set protecting an authored
  stranded transport makes the rescued actor's route-information and
  transport-use reward available; damage alone or merely reaching the ship
  does not settle the rescue.

### Constraint Genes

- Existing `CON-578`: Bomb Glove attacks require compatible finite reserve;
  the wrench remains available without that ammunition. Weapon vendors,
  purchase prices and later ammunition classes are outside scope.

### Information Genes

- Existing `INF-073`: the selected weapon and its usable ammunition can be
  inspected before a throw; the exact Quick Select pause semantics are open.
- Existing `INF-119`: current health is visible while surviving the crater.
- Existing `INF-125`: the map and mission view locate the current objective
  without revealing future destinations before the Infobot reward.

### Objective Genes

- New `OBJ-237`: recover off-world travel from an authored crash by traversing
  the guarded route, clearing the transport's defenders and accepting the
  survivor's information-and-ship reward. Arrival at the ship before that
  handoff is insufficient.

### Time Genes

- Existing `TIM-003`: hostile fire and movement continue while Ratchet moves,
  jumps or attacks. No global mission timer is claimed.

## Reproducible transitions

| Before | Action | Bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| First Novalis control after crash | Open map and take crater lift/path | Crater mission is the chosen route, distinct from waterworks | selected branch | `RC-002`, `RC-006` |
| Living Ratchet at broken bridge | Move and jump across safe segments | Reach the next hostile area or fall and retry | traversal risk | `RC-003` |
| Wrench active, robot in reach | Direct wrench strike | Live robot combat can progress without Bomb Glove reserve | alternate attack | `RC-004` |
| Bomb Glove active, compatible reserve positive | Throw at a reachable guard | Reserve falls and the attack can damage the guard | finite ranged option | `RC-004` |
| Bomb Glove reserve empty | Request another throw | No legal ammunition-consuming shot; switch to wrench or refill | ammunition gate | `RC-004` |
| Final ship guards remain | Reach ship without clearing them | Chairman rescue reward has not yet settled | clearance gate | `RC-005` |
| Final required guards defeated | Accept chairman's interaction | Kerwan Infobot and courier-ship access become available | packet terminal | `RC-005` |

## Edge-case audit

- The final guards are a finite authored set, not an endless survival wave.
  The first guide explicitly counts three shooters at the parked ship; that
  count is a carrier parameter, not a general gene.
- Bombs are an optional route tactic: a wrench-only clear is allowed by the
  written route. The genome admits weapon switching because the fixed test
  traces explicitly exercise both starting options, not because a bomb is a
  compulsory key.
- The waterworks purchase is separate and optional for this rescue. The
  first guide's mission list has no prerequisite from it to finding the ship.
- The bolt crank opens an optional Gold Bolt branch, not the critical crater
  path. Hydro-Pack is acquired later and must not be drawn on first arrival.
- Reaching the ship before killing its protectors is not the terminal; the
  information and usable transport arise after the rescue interaction.
- Exact original-disc death/retry retention, enemy damage, Bomb Glove capacity
  and the timing of Quick Select are open and omitted from fixed claims.

## Strategic and experiential structure

- Local: choose safe footing and weapon reach while robots keep firing.
- Medium term: protect health and finite bombs while working toward the
  defended ship; the free wrench remains a fallback.
- Long term: the reward restores interplanetary choice, but actual departure
  and subsequent planet rules lie beyond this packet.
- Player trust: a visible map, health and active weapon make current choices
  legible; an optional collectible detour must not be described as mandatory.

## Replay and variation

The same crater rescue and reward order persists while the precise approach,
weapon mix, damage and ammunition use vary. No random encounter frequency or
checkpoint-reset algorithm is inferred from the written guides.

## Adjacent systems and history

- *Luigi's Mansion* also combines live navigation and a finite defended
  reward, but its room changes state through light exposure and contested
  vacuum capture rather than weapon reach and ammo scarcity.
- *Metroid Prime* uses capability-gated route fixtures and later loss of
  tools. The first Novalis crater does **not** require a newly acquired
  gadget; equating its optional crank/collectible with a mandatory gate would
  import a different route.
- The 2016 PS4 reimagining changes planets and mechanics and is not an
  interchangeable evidence source for the 2002 PS2 mission.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-341` | bridge geometry, wrench, Bomb Glove, chairman |
| System Behaviour | `SYS-215`, `SYS-578`, `SYS-1083` | guard count, health and reward |
| Constraint | `CON-578` | bomb reserve and refill |
| Information | `INF-073`, `INF-119`, `INF-125` | weapon, health, local map |
| Objective | `OBJ-237` | guarded courier ship and Kerwan Infobot |
| Time | `TIM-003` | live combat without global deadline |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `403` (`GAME-0001`–`GAME-0403`).
- Exact genome matches: none.
- Tied near matches: `GAME-0352` — DOOM (1993) (`11 / 18 = 0.611111`).
- Supported combination subsets: none.
- Scan date: 2026-09-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0352` — DOOM (1993) | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-341`, `SYS-215`, `SYS-578`, `CON-578`, `INF-073`, `INF-119`, `INF-125`, `TIM-003` | Both bounded routes use live direct movement, weapon choice, finite ammunition, health and a map, but DOOM's no-jump first-person E1M1 path ends at an exit switch and adds armour, sight/noise pursuit and an ordinary door/automap layer. Novalis instead jumps broken terrain and must clear a guarded ship to receive an Infobot and transport. The shared generic action-shooter base does not make their terminals or spatial control identical. | Near, `11 / 18 = 0.611111` |

## Taxonomy impact

- Registry changes: two Active genes, `SYS-1083` and `OBJ-237`.
- Taxonomy-change record: `TAXONOMY_CHANGE_142`.
- No earlier genome or verified combination changes.

## Negative results

- No acquired-gadget gate belongs to this mandatory first-Novalis crater
  mission. The optional bolt-crank collectible branch and later Hydro-Pack
  route are not part of the admitted signature.

## Delta summary

## New facts

- [Observation | Corroborated | High] The original crater's rescue reward is
  separate from both the waterworks' purchasable Infobot and the optional
  bolt-crank Gold Bolt path (`RC-005`–`RC-007`).

## New genes

- [Observation | Corroborated | High] Two bounded distinctions represent the
  guarded transport settlement and the crash-to-restored-travel objective.

## New combinations

- [Observation | Corroborated | High] None verified in this packet.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_142` adds two genes
  without changing an earlier signature.

## New questions

- What exact checkpoint position and carried-state retention does the
  North American original disc use after a death in the Novalis crater?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0405` *Fable II*.
- Optimisation criterion: change platform and decision loop from real-time
  guarded route to a bounded quest with character choices and consequences.
- Expected information gain: separate lasting quest/character response from
  the simple authored reward of the Novalis rescue.
- Backlog impact: no selected subject displaced.

## Why this game

- [Hypothesis | Limited | Medium] This early, source-bounded PS2 route tests
  whether weapon selection and finite bombs matter independently of the
  famously broad later gadget inventory, without pretending to have played
  the original disc.
