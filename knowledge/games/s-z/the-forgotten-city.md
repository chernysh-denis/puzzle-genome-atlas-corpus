---
game_id: GAME-0576
slug: the-forgotten-city
game_title: The Forgotten City
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-091
    - ACT-107
    - ACT-232
    - ACT-783
  system:
    - SYS-1691
    - SYS-1692
    - SYS-1693
  constraint:
    - CON-839
  information:
    - INF-055
    - INF-549
  objective:
    - OBJ-317
  time:
    - TIM-003
---

# Game: The Forgotten City

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The medicine that dooms one version of the city can save a patient
after the world resets. Returning with an item and a remembered
conversation opens an earlier opportunity to act.

## Analysis scope

- Version / ruleset: English July 2021 standalone Xbox Series X|S
  commercial base game, Xbox product 9NJ4R763M7TH. First solitary story
  play, full Dying Gasp lead via the directly stolen medicine and one
  successful return to the start of the city day. No installed patch,
  disc image, runtime trace or particular controller remapping inferred.
- Structured analysis target: PLAT-XBOX-SERIES in knowledge/platforms/games.json.
- Entry: reach the living city through the prologue portal in an ordinary
  first play. Begin at the Shrine of Proserpina before the initial Galerius
  conversation, with no Silphium Resin and no learned city leads. Follow
  the offered introduction to Sentius, then identify Lucretia's need.
  A backstory without a special advantage is sufficient for this route.
- Primary decision loop: read the current lead and question residents.
  Obtain the specified remedy, respond to the consequences of taking it,
  cross the open return portal and use the retained object and prior
  knowledge to reach the still-treatable patient. Direct character movement
  and an optional downhill cable affect how early the player returns.
- Positive exit: give Lucretia the Silphium Resin at the Shrine of Apollo
  during the new iteration and observe Iulia recover, settling Dying Gasp.
  Check that Iulia can give the next lead about Ulpius. Stop before pursuing
  it. The successor dialogue is a witness for available access, not another
  condition for saving Iulia.
- Negative exit: leaving Iulia untreated in the current iteration can lose
  that opportunity. If the player cannot reach the return portal alive,
  the carried resin has not made the documented transition. No exact
  injury threshold or autosave and reload snapshot is claimed.
- Included: introduction, causal conversation facts, journal and route
  prompts, unauthorised take, Golden Rule response, physical return,
  retained object and learned facts, downhill cable and delivery to
  Lucretia, recovery and first successor clue.
- Excluded: alternative funding and purchase routes as executable packets,
  combat loadouts, achievement hunting, the golden bow, a third iteration,
  delegating solved tasks to Galerius, the election, campaign endings,
  other platform rulesets and the Skyrim mod.
- Potential scoped modules: Galerius repeating already-solved tasks on a
  later cycle and the evidence requirements for ending the loop. Neither
  is needed for this first successful handover.
- Direct-play status: not conducted. Xbox product data and published
  creator accounts were checked against documented play of the standalone
  release, including written Xbox routes. No console, emulator, audio or
  video was used. Build parity, exact timing and save behaviour remain open.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| TFC-001 | The commercial standalone game launched on Xbox Series consoles on 28 July 2021. The US Xbox catalogue identifies 9NJ4R763M7TH and also lists Xbox One. | Observation | Corroborated | High | P1, P2 |
| TFC-002 | A prohibited act can doom residents regardless of its author. Sentius introduces that rule after the first city arrival. Local NPC routines continue in active play. | Observation | Corroborated | High | P2, P3, R1, R2 |
| TFC-003 | Lucretia identifies Silphium Resin as the needed remedy. Desius has it. The journal can track that lead. Taking the resin directly is an executable route even without the requested payment. | Observation | Corroborated | High | R1, R2, R3 |
| TFC-004 | Taking the owned resin without permission puts it into the player's possession and triggers the Golden Rule. Danger follows before the reset. Follow the return prompt toward Proserpina's Shrine and enter the portal Sentius opens. | Observation | Corroborated | High | P2, R1, R2, R5 |
| TFC-005 | Portal crossing returns the city to the initial arrival while keeping the resin. Galerius repeats a first meeting and the player's prior facts can be used in dialogue. | Observation | Corroborated | High | P3, P4, R1, R3, R5 |
| TFC-006 | The repeated meeting offers a reply demonstrating knowledge from the earlier encounter. The route can obtain Galerius's cable handle and slide toward the city from the higher end of the available cable. | Observation | Corroborated | Medium | P4, R1, R4 |
| TFC-007 | Lucretia can use the carried resin to treat the recoverable Iulia in the next iteration. Dying Gasp settles, and speaking to the recovered patient can point to Ulpius. An untreated iteration can miss recovery. | Observation | Corroborated | High | R1, R3, R4, R5 |
| TFC-008 | Later resets can let Galerius repeat completed interventions. This is a later capability, separate from recognising him, obtaining the handle and personally making the first successful handover. | Observation | Corroborated | High | P3, P4, R1 |

## Basic data

- Modern Storyteller / Dear Villagers. Families FAM-012 for progression
  through learned facts and FAM-017 for the remedy/reset/handover dependencies.
- P1: [Xbox US product listing](https://www.xbox.com/en-us/games/store/The-Forgotten-City/9NJ4R763M7TH).
  Verified 2026-11-20. Provides 28 July 2021, the product identity and Xbox
  platform targets. The listing is not a claim about the latest patch
  of a particular installed copy.
- P2: [Nick Pearce's launch-day account on Xbox Wire](https://news.xbox.com/en-us/2021/07/28/the-forgotten-city-journey-from-a-mod-to-a-standalone-game/).
  Author's first-person account of stand-alone availability and design
  of the shared rule and loop.
- P3: [Xbox Wire's interview with Nick Pearce](https://news.xbox.com/en-us/2021/11/08/the-forgotten-city-interview-with-creator-nick-pearce/).
  The creator documents the Golden Rule premise and distinguishes a first
  treatment from later repetition by an NPC.
- P4: [Nick Pearce interview in Game Developer](https://www.gamedeveloper.com/design/delving-into-the-narrative-structure-of-the-forgotten-city).
  Creator account of reset dialogue flags, retained inventory and delegation
  once a solution is already known. Describes shortcuts designed around
  the asymmetry between the player's and characters' knowledge.
- R1: [EIP Gaming's launch-day walkthrough, part 1](https://eip.gg/the-forgotten-city/guides/walkthrough-part-1-welcome-to-the-forgotten-city/).
  First entry through Dying Gasp and the following clue. Used for the
  witnessed logic and outcomes. PC key prompts are not Xbox input proof.
- R2: [TrueAchievements' Xbox story walkthrough](https://www.trueachievements.com/game/The-Forgotten-City/walkthrough/3).
  Corroborates portal return and tracked lead on Xbox. Several steps in
  that account serve later achievement objectives and are outside scope.
- R3: [Gamepressure's remedy FAQ](https://www.gamepressure.com/forgotten-city/the-silphium-resin-how-to-get/z3f09d).
  Documents direct theft and separate payment alternatives. No universal
  price, minimum timer or class-specific shortcut is inferred here.
- R4: [Gamepressure's treatment walkthrough](https://www.gamepressure.com/forgotten-city/heal-iulia/zdf0a6).
  Provides the renewed encounter, downhill cable, handover and recovered
  patient's clue. Only written sections used.
- R5: [Wireframe issue 62, published play excerpt](https://www.mclibre.org/descargar/docs/revistas/wireframe/wireframe-62-en-202205.pdf).
  Independent documented player observation of the remedy, shrine escape,
  retained possession and treatment. Exact platform controls are not used.

## Mechanical decomposition

### Action Genes

- ACT-008 is directing the traveller through the city and crossing the
  available portal under local movement input.
- ACT-091 is transferring the selected medicine to Lucretia as requested.
- ACT-107 is asking about Iulia and learning the exact remedy and its source.
  The follow-up about Ulpius supplies another operational fact.
- ACT-232 covers committing a currently offered response, including
  demonstrating prior knowledge to Galerius on the renewed arrival.
- ACT-783 is directly taking the owned resin into inventory without
  permission. The world response is separately resolved.
- Claim IDs: TFC-002–TFC-007.

### System Behaviour Genes

- SYS-1691 restores the repeated world's initial day by live portal crossing
  while keeping held resin and facts explicitly available to the player.
- SYS-1692 switches the city's shared peril phase after the prohibited take.
  This is the condition for the retreat sequence, not its successful end.
- SYS-1693 covers the downward cable that becomes available with the handle.
  It is a route option. The selected mission witness uses it.
- Claim IDs: TFC-004–TFC-006.

### Constraint Genes

- CON-839 requires the correct remedy and a still-recoverable patient in
  this city iteration. The object can be ready while the local state
  disallows the desired treatment in an abandoned iteration.
- Claim IDs: TFC-003, TFC-007.

### Information Genes

- INF-055 covers the offered reply that exposes prior knowledge. The
  game presents it even while Galerius has returned to his original
  encounter.
- INF-549 is active lead tracking and the requested guidance toward the
  current step or return shrine. Movement and treatment remain separate.
- Claim IDs: TFC-003–TFC-007.

### Objective Genes

- OBJ-317 settles the lead when Lucretia's application of the delivered
  remedy restores Iulia. Her next testimony verifies successor access
  and is a separate action from the treatment.
- Claim ID: TFC-007.

### Time Genes

- TIM-003 covers the city's live unfolding while the player can move and
  the post-breach interval before escape or failure. There is no claimed
  fixed-duration reset, real-time progress while paused or precise local
  treatment deadline.
- Claim IDs: TFC-002, TFC-004, TFC-007.

## Reproducible transitions

| State / precondition | Action or event | Observable transition | Boundary | Claims |
| --- | --- | --- | --- | --- |
| Fresh first arrival in the living city, no resin | Accept the introduction and speak with Sentius | Golden Rule becomes known and the starting investigation opens | No particular optional backstory advantage | TFC-001, TFC-002 |
| Lucretia is attending Iulia | Ask about her condition and what she needs | Learn the required medicine and start Dying Gasp; the merchant is a tracked contact | The journal does not grant the remedy | TFC-003 |
| Owned resin is reachable at Desius's stall | Take it directly without payment | It enters the inventory and the city becomes dangerous | The breach alone does not reset the city | TFC-003, TFC-004 |
| Breach is active and the return has opened | Reach and enter the portal at Proserpina's Shrine | Begin another city day, still holding the resin; the opening encounter recurs | Death or manual reload is not this authored transfer | TFC-004, TFC-005 |
| Galerius starts the introduction again | Cite facts learned on the prior iteration | Bypass the repeated introduction and obtain his cable handle on the documented route | This does not yet delegate treatment | TFC-005, TFC-006, TFC-008 |
| The handle is available at the cable's upper mount | Ride the line from the shrine toward town | Reach the lower end earlier by a directional route | No uphill transport on that line | TFC-006 |
| Iulia remains treatable, with the resin carried | Give the resin to Lucretia | Iulia recovers and Dying Gasp settles | Holding the resin or entering the shrine alone cannot settle the request | TFC-007 |
| Iulia has recovered | Ask her about the investigation | Talk to Ulpius becomes an available next step | The later quest is outside this packet | TFC-007 |
| Escape fails or the player misses this opportunity to treat Iulia | Do not complete the live portal crossing or handover | The specified successful transition is absent in that iteration | Exact save and retry behaviour unmeasured | TFC-004, TFC-007 |

## Strategic and experiential structure

- The take can solve a resource problem and create a global emergency at the
  same time. Keep the resource, the world phase and the physical exit as
  separate state variables.
- A witness of the full route is possession false before the theft, true
  during the emergency, still true after crossing and no longer merely an
  inventory possibility once handed over. The external world's danger and
  the patient's state can change independently of that possession.
- Speaking to Galerius with remembered facts shortens the opening encounter.
  The handle offers a separate route; the help required for a later
  delegation is not inferred from that interaction.
- Claim IDs: TFC-003–TFC-008.

## Replay and variation

- Restarting the city by portal makes earlier conversations available under
  different knowledge and lets the medicine be brought sooner. Different
  movement or dialogue sequences can lead to the same treatment.
- Buying the medicine is documented as an alternative. The selected
  witness uses theft and one return to show the inventory boundary. One
  successful reset is a route property, not a proven quest-wide minimum.
- Claim IDs: TFC-003–TFC-008.

## Adjacent systems and history

- The 2015–2016 mod and July 2021 standalone game are distinct products.
  Later NPC delegation executes solved tasks in a reset world and is
  separate from the first successful treatment. No campaign ending or
  later artifact gate is implied by a single settled lead.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-091, ACT-107, ACT-232, ACT-783 | Move, question, choose a reply, take and hand over |
| System Behaviour | SYS-1691, SYS-1692, SYS-1693 | Violation, asymmetric reset and downhill ride |
| Constraint | CON-839 | Exact remedy and treatable patient |
| Information | INF-055, INF-549 | Prior facts, lead tracking and route cue |
| Objective | OBJ-317 | Settle Dying Gasp and inspect successor access |
| Time | TIM-003 | Live world evolution until the current exit |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `575` (`GAME-0001`–`GAME-0575`).
- Exact genome matches: none.
- Tied near matches: `GAME-0105` — Outer Wilds (`4 / 19 = 0.210526`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0105` — Outer Wilds | ACT-008, ACT-107, INF-055 and TIM-003 cover direct navigation, facts from conversations, access to known facts after reset and live progression. | Outer Wilds normally ends its cycle at the supernova and retains learned facts without carrying the present inventory. The Forgotten City route uses a live return portal made available by the breach, keeps a material remedy and tests its application on the next day. | Tied near: 4 / 19 = 0.210526 |

### Preserved research notes

- New genes: ACT-783, SYS-1691–SYS-1693, CON-839, INF-549 and OBJ-317.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_322](../../../research/taxonomy-changes/TAXONOMY_CHANGE_322.md)
  separates the offending acquisition, shared danger, carried-state
  exception, actionable facts and first treatment outcome.

## Negative results

- The reset is not a fixed cycle timeout or a player death respawn.
  It restores the city after a live crossing while keeping some player state.
- The obtained medicine does not automatically treat the patient or end the
  city's entire loop. The node for the completed lead differs from the
  restored local NPC state.
- Source descriptions do not establish every possible infringement,
  an exact console build, a timing optimum or universal state persistence.
  The worked rules do not use a PC control binding as Xbox evidence.

## Delta summary

## New facts

- [Observation | Corroborated | High] TFC-003–TFC-007 establish a full
  treatment path across a materially asymmetric world reset.

## New genes

- [Observation | Corroborated | Medium] Seven additions in taxonomy change 322.

## New combinations

- [Observation | Corroborated | High] No new combination proposed.
  Existing supported subsets are owned by the comparison section.

## Taxonomy changes

- [Observation | Corroborated | Medium] Older definitions and signatures
  stay unchanged.

## New questions

- A paired Xbox capture could resolve the latest treatable state, the
  remedy's exact inventory transition and platform-specific failure saves.

## Next recommended game

- [Hypothesis | Limited | Medium] Selection 046 ends here. A subsequent
  subject requires a new request and selection. Close the nine-game
  parity checkpoint before considering the scope of another batch.

## Why this game

- [Hypothesis | Limited | Medium] Finishing one time-loop intervention
  can separate saved knowledge and possessions from changed world state
  more clearly than treating every action in a full campaign as mandatory.
