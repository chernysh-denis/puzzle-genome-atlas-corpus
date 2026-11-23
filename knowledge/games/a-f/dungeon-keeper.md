---
game_id: GAME-0573
slug: dungeon-keeper
game_title: Dungeon Keeper
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-152
    - ACT-777
    - ACT-778
    - ACT-779
  system:
    - SYS-051
    - SYS-1681
    - SYS-1682
    - SYS-1683
    - SYS-1684
    - SYS-549
  constraint:
    - CON-836
  information:
    - INF-546
  objective:
    - OBJ-315
  time:
    - TIM-003
---

# Game: Dungeon Keeper

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
A floor can be excavated, claimed and assigned a room function. Each step
changes what the Keeper can do with the creatures that live beneath it.

## Analysis scope

- Version / ruleset: original English commercial PC CD-ROM DOS release of
  the 1997 base game. Target the full original single-player campaign and
  first realm, Eversmile (MAP00001). No installed build was verified.
- Structured analysis target: PLAT-DOS in knowledge/platforms/games.json.
- Entry: start a new campaign, select Eversmile and begin at the first
  playable red Dungeon Heart before issuing tasks. Full-campaign sources
  report three Imps and 2,500 gold at this point.
- Primary decision loop: mark earth and gold, let Imps excavate, claim and
  haul, pay for room tiles and connect the neutral Portal. Once creatures
  arrive, keep their dungeon supplied and lift and drop defenders onto owned
  floor where they can intercept the scripted hero assaults.
- Positive exit: defeat the tunnellers and then the Lord of the Land while
  the player's Dungeon Heart survives. Read the victory objective and
  advance through the results to the world map, where Cosyton follows.
  Optional building after victory is outside the decision interval.
- Negative exit: destruction of the player's Dungeon Heart loses the realm.
  Losing a worker, one fight or the first raid's defenders does not by
  itself settle defeat. Imps can be created if the notified recovery branch
  is available and the cost can be paid.
- Included: ordinary indirect control without Possess Creature, excavation
  and gold delivery, territory and Portal ownership, Treasure Room, Lair and
  Hatchery, creature arrivals, upkeep, Create Imp, claimed-floor redeployment,
  live waves, and the complete result. The reported nine-tile rooms form a
  reproducible preparation route. Exact native tick arithmetic and unexercised
  alternative preparation paths remain qualified.
- Excluded: the Windows demo also called Eversmile, Windows executable and
  patches, Gold-specific extras, Deeper Dungeons, KeeperFX, later realms,
  training, research, traps, additional Keepers, creature possession as
  direct control, slapping, cheats, score optimization and multiplayer.
- Potential scoped modules: the training and wages trade-off in Cosyton,
  or a separate first-person route using Possess Creature.
- Direct-play status: not conducted. The PC CD-ROM manual, release listing,
  attributed full-campaign walkthroughs and a qualified old script excerpt
  were read. No retail DOS binary, native run, emulator or audiovisual
  playback was used. The rule and stage boundary is corroborated. The
  unmodified DOS script and exact executable revision are not authenticated.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DKE-001 | Eversmile opens the commercial 1997 base campaign. Its DOS product differs from the later Windows demo. The stage starts with the red Heart, three Imps and 2,500 gold. | Observation | Corroborated | High | P1, P2, R1, R2, R5 |
| DKE-002 | Orders designate earth or ore for Imps. Excavation opens floor, Imps claim reachable neutral ground and can reinforce adjacent walls. Mining produces gold that Imps haul to the Treasury. | Observation | Corroborated | High | P1 §§11–14, R1 |
| DKE-003 | Building spends gold per eligible claimed tile of an available room type. Treasure Room stores gold, Lair provides sleeping spaces and Hatchery generates chickens. Room shape affects service efficiency. | Observation | Corroborated | High | P1 §§13, 16–17, R1 |
| DKE-004 | Players must connect and claim the neutral Portal for periodic arrivals. Its local pool enables Fly and Beetle with room and script conditions, at a capacity reported as seven non-Imp creatures. | Observation | Corroborated | High | P1 §§14, 22, 24, R1, R2, R4, R5 |
| DKE-005 | Applicable creatures choose places to sleep and visit the food and wage sources themselves. Imps follow separate worker rules and do not use ordinary creature meals. | Observation | Direct | High | P1 §§13, 17, 24–25 |
| DKE-006 | The Hand can hold up to eight picked creatures. Release requires claimed ground. Nearby defenders then fight by their own combat rules. | Observation | Corroborated | High | P1 §§23, 28, R1, R2 |
| DKE-007 | The tutorial makes Create Imp available during preparation. Its price depends on current Imp count, and its selected target must be claimed. The old script excerpt exposes a fallback when no Imps remain. | Observation | Corroborated | Medium | P1 §18.2, R1, R3, R4 |
| DKE-008 | Construction, mining and creature milestones lead to a timed first wave of tunnellers. Their defeat advances the scenario to a separate interval and the Knight. Exact conditions are supported by the play accounts and a qualified old script excerpt. | Observation | Corroborated | Medium | R1, R2, R3, R4, R5 |
| DKE-009 | Pop-up objectives, flashing availability, room flags, revealed map and battle panel report current state. Some terrain and invaders are undisclosed before exploration or warning. | Observation | Corroborated | High | P1 §§4–5, 10, 16, 28, R1 |
| DKE-010 | Defeating the dispatched Lord and closing the hostile assault gives the win notice and a route through results to the next map. A destroyed own Heart is a defeat. | Observation | Corroborated | High | P1 §§2, 30, P2, R1, R2 |

## Basic data

- Bullfrog Productions / Electronic Arts. 1997 DOS CD-ROM base game.
- Families FAM-010 real-time system pressure, FAM-014 world topology and
  perspective, and FAM-015 agent routing and coordination.
- P1: [Original English PC CD-ROM manual](https://images2.wikia.nocookie.net/__cb20120720033242/dungeonkeeper/images/c/cb/Dk_manual-en.pdf).
  Use §§11–17, 18.2, 22–25 and
  28–30 for common PC rules. The manual describes options from later
  levels. It establishes eligibility only where the campaign evidence
  actually places that option in Eversmile.
- P2: [Electronic Arts product and release history](https://www.ea.com/games/dungeon-keeper/dungeon-keeper).
  Gives 26 June 1997 and publishes the base product description. The
  current app offer and requirements do not define original DOS execution.
  The [archived publisher catalog](https://www.mocagh.org/ea/ea-97catalog.pdf)
  and [Centre for Computing History CD-ROM record](https://www.computinghistory.org.uk/det/30723/Dungeon-Keeper/)
  document the original PC distribution.
- R1: [Phil Estelle’s 1998 Eversmile route](https://draketungsten.org/arcade/pcmanuals/dungeonkeeper/keeper/level01.htm).
  Records the starting gold and workers, 3 × 3 rooms, neutral Portal,
  creature release and both assaults. The guide index identifies a PC AI
  patch. This route supports transitions without certifying original ticks.
- R2: [Telago’s original campaign guide, GameFAQs](https://gamefaqs.gamespot.com/pc/197183-dungeon-keeper/faqs/60666).
  Use its Eversmile entry and original PC creature, room and deployment notes.
  Later realm rules and creature statistics are outside this record.
- R3: [Original-game run notes, Speed Demos Archive](https://speeddemosarchive.com/DungeonKeeper.html).
  Written Eversmile comments describe mining, the three rooms, creature count
  and delay. The possession optimization is outside the chosen route.
- R4: [Archived Eversmile script fragments, October 2006](https://www.united-forum.de/threads/mod-erstellen-zu-dungeon-keeper.47996/).
  The quoted stock-looking tutorial branches describe room sizes, cumulative
  mining, Creature/Imp separation, timed waves and the phase-guarded win.
  The user was changing the level. The attachment is not evidence of an
  unmodified retail file and its exact constants are secondary corroboration
  only. [Classic script reference](https://keeper.lubiki.pl/dk1_docs/dk_scripting_ref.htm)
  explains turn counters and conditional dispatch.
- R5: [Eversmile campaign inventory](https://dungeonkeeper.fandom.com/wiki/Eversmile).
  Later community inventory corroborates starting values and two raid
  phases. Its [separate demo inventory](https://dungeonkeeper.fandom.com/wiki/Eversmile_(Demo))
  describes a shifted Portal, pre-existing rooms and six starting Imps.
  Neither the demo nor later enhanced map is used as the analysis target.
  Sources checked 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-777 designates eligible earth or ore. A task can exist before any
  worker accepts it. ACT-152 chooses a functional room and its footprint.
- ACT-778 lifts an owned creature and redeploys it at a chosen legal slab.
  An ordered batch may use the hand, but each unit still fights on its own.
- ACT-779 spends gold to create a new worker on eligible floor. Creation and
  Portal attraction are distinct routes to a larger population.
- Claim IDs: DKE-002, DKE-003, DKE-006, DKE-007.

### System Behaviour Genes

- SYS-1681 changes geometry by digging and ownership by claiming. SYS-549
  covers finite stock extraction and delivery to a compatible gold store.
- SYS-1682 admits eligible creature types through the claimed Portal over
  time. SYS-1683 governs the creature-side use of shelter, food and wages.
- SYS-1684 advances the tutorial and two assault stages by milestones,
  live state, timing and prior clearance. SYS-051 owns the defenders'
  automatic engagements when placed within reach of a hostile.
- Claim IDs: DKE-002–DKE-008.

### Constraint Genes

- CON-836 applies room availability, ownership, floor and affordability
  at tile placement. A marking on rock cannot build that floor. The land
  rules on the Hand, the spell cost and population cap are components of
  their respective transitions. Their exact constants are parameters.
- Claim IDs: DKE-002–DKE-007.

### Information Genes

- INF-546 shows the current notice, available tools, gold, room bars, map
  and combat feedback. The player can see the next preparation requirement
  and see changes to the present threat without a full future route.
- Claim IDs: DKE-003, DKE-008, DKE-009.

### Objective Genes

- OBJ-315 covers the full two-wave sequence and protected Heart. Removing
  only the preliminary group progresses the tutorial without settling the
  realm. The result is available after the authorized final group is cleared.
- Claim IDs: DKE-008, DKE-010.

### Time Genes

- TIM-003 covers live worker jobs, arrivals, needs and combat while the
  player builds and uses the Hand. The clocks for assault are gated by
  state. Elapsed time from the initial view is insufficient for victory.
- Claim IDs: DKE-004–DKE-009.

## Reproducible transitions

| State / precondition | Action or event | Observable transition | Boundary | Claims |
| --- | --- | --- | --- | --- |
| Starting Heart and three Imps, nearby earth and ore | Mark an accessible rock or gold slab | An available Imp takes the job and opens the slab after work | The input designates; the player does not instantly remove rock | DKE-001, DKE-002 |
| Mined gold and a reachable Treasure Room with space | An Imp brings the gold to storage | Usable gold increases | Mined amount, carried gold and spendable gold differ | DKE-002, DKE-003 |
| Dry owned floor with room type available | Choose a Treasure Room, Lair or Hatchery tile | Pay per tile and give the floor its room use | Neutral terrain and unexcavated rock are ineligible | DKE-003 |
| Portal reached by an excavated passage | Allow Imps to finish claiming and wait for an eligible arrival | Fly or Beetle arrives according to local conditions | An exposed Portal is not automatically owned, and Imps are separate | DKE-004, DKE-007 |
| Hatchery ready and eligible hire population arrives | Continue the live simulation | Food generation and visits proceed, with Create Imp and the next preparation checks available | Room service, purchased workers and arrivals are separate | DKE-003–DKE-005, DKE-007 |
| Preparation milestones and scenario delay are satisfied | Wait for the scripted advance | The tunneller group is dispatched | The initial entry clock alone does not force the wave | DKE-008, DKE-009 |
| Tunnellers reach eligible land and defenders are alive | Lift gathered defenders and release onto claimed floor nearby | Dropped creatures can enter autonomous combat | Release on neutral ground is not an ordinary combat order | DKE-006 |
| First hostile wave defeated | Wait on the subsequent scenario condition with replacement arrivals if needed | The Lord arrives after a separate delay | No win at the preliminary clear | DKE-008 |
| Final enemy defeated, own Heart survives | Accept result and advance | Victory is retained and Cosyton is next on the world map | Destroying the Heart before this is defeat | DKE-010 |

## Strategic and experiential structure

- Pay for storage and income before using all floor space for recruitment.
  A useful room requires an owned path, usable tiles and room for its
  occupants or stock. More excavated area by itself does not hire creatures.
- More Imps can shorten work and hauling, with a charge against room and
  wage gold. Most defenders follow their own routines until they are
  moved into contact, where combined local presence helps.
- The Hand can bypass an internal walk for a chosen creature but cannot
  claim neutral terrain or serve as an attack. The timing of claimed
  approach tiles affects where defense can happen.
- Claim IDs: DKE-002–DKE-008.

## Replay and variation

- A fresh realm restores authored layout and starting stock. Room footprint,
  order timing, arrival composition and placement can differ with decisions.
  Exact randomness and tick rates are unmeasured.
- The late script excerpt reports 9,000 cumulative gold mined and nine
  basic room tiles of each type along a preparation route. It uses a
  population condition and a timer after the Hatchery, then a separate
  condition after wave clearance. These are not assertions that every
  route must hold all three room counts continuously. Reports differ
  on order and earliest entry. Proceed along the ordinary routed path.
- Claim IDs: DKE-003–DKE-010.

## Adjacent systems and history

- Later parts of the campaign introduce training, research, doors and
  broader Keeper wars. The original manual covers them, but this first
  realm cannot stand in for those separate rules.
- The initial Eversmile opening in the Windows demo is a distinct scenario
  despite sharing the name. Earlier unpublished and later reimplemented
  scenarios are excluded.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | ACT-152, ACT-777, ACT-778, ACT-779 | Mark excavation, make rooms, lift and drop, create Imps |
| System Behaviour | SYS-051, SYS-1681, SYS-1682, SYS-1683, SYS-1684, SYS-549 | Combat, finite funded haul, claim, portal, needs, scheduled assault |
| Constraint | CON-836 | Room type, owned floor, payment |
| Information | INF-546 | Objectives, station and combat state |
| Objective | OBJ-315 | Final hero clearance with own Heart intact |
| Time | TIM-003 | Concurrent work, arrivals and assaults |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `572` (`GAME-0001`–`GAME-0572`).
- Exact genome matches: none.
- Tied near matches: `GAME-0027` — Bad North: Jotunn Edition (`2 / 24 = 0.083333`); `GAME-0407` — Plants vs. Zombies (`2 / 24 = 0.083333`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0027` — Bad North: Jotunn Edition | SYS-051, TIM-003 | Both move defenders to useful territory and let them engage under live pressure. Bad North positions squads against landing waves on an island. Eversmile makes its own claimed floor, recruits individual creatures and deploys them by hand. | Tied near: 2 / 24 = 0.083333 |
| `GAME-0407` — Plants vs. Zombies | SYS-051, TIM-003 | Both place defenders who attack nearby targets while waves progress. Plants vs. Zombies uses planted lane positions and sun. Eversmile expands the defensive space, moves persistent creatures and guards a surviving Heart against a milestone-gated Lord. | Tied near: 2 / 24 = 0.083333 |

### Preserved research notes

- New genes: ACT-777–ACT-779, SYS-1681–SYS-1684, CON-836, INF-546 and OBJ-315.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_319](../../../research/taxonomy-changes/TAXONOMY_CHANGE_319.md)
  retains the distinction between terrain requests, autonomous work,
  functional rooms, voluntary creature arrivals and actual combat.

## Negative results

- Eversmile does not support assuming a Training Room or upgraded troops
  from a later realm. The original campaign differs from the demo map.
- The edited forum attachment cannot certify exact retail tick or branch
  dependencies. Timing, availability and eligibility are qualified where
  the old excerpt extends beyond the corroborated preparation route.

## Delta summary

## New facts

- [Observation | Corroborated | High] DKE-002–DKE-010 distinguish
  excavation, ownership, room construction, population, defense and
  ordinary realm victory.

## New genes

- [Observation | Corroborated | Medium] Ten additions in taxonomy change 319.

## New combinations

- [Observation | Corroborated | High] No new combination proposed.
  Existing subset results are recorded in the comparison section.

## Taxonomy changes

- [Observation | Corroborated | Medium] Earlier definitions and signatures
  stay unchanged.

## New questions

- An authenticated original DOS executable and level script could settle
  all early-turn alternatives, eligibility edge cases and timer values.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0574, Florence on iOS.
- Optimisation criterion: alternate platform and era. Contrast the
  asynchronous dungeon with a bounded narrative gesture sequence.
- Backlog impact: seventh Selection 046 unit.

## Why this game

- [Hypothesis | Limited | Medium] One complete realm connects terrain
  edits and indirect labor to unit needs and autonomous defense.
