---
game_id: GAME-0696
slug: tides-of-tomorrow
game_title: "Tides of Tomorrow"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-131
    - ACT-232
    - ACT-341
    - ACT-915
    - ACT-916
  system:
    - SYS-1972
    - SYS-1973
  constraint:
    - CON-891
  information:
    - INF-119
    - INF-635
  objective: []
  time: []
---

# Game: Tides of Tomorrow

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The first boat conversation couples a selected predecessor's decision
to one scarce unit. The current player can diverge and leave a
different starting condition for a follower.

## Analysis scope

- Version / ruleset: DigixArt's English commercial PlayStation 5
  base game, published by THQ Nordic on April 22, 2026.
  Store product EP4389-PPSA29986_00-TIDESOFTOMORROW1,
  Standard edition. Use the Online Story-Link route.
  W1 and W2 identify their captures as PS5 Pro, show PlayStation
  controls and continue into the full campaign. Their exact
  installed builds, store region and entitlements are unverified.
- Structured analysis target: PLAT-PLAYSTATION-5 in
  [platform coverage](../../platforms/games.json).
- Entry: on the Follow screen after avatar setup, confirm one
  already recorded predecessor. Use a trace that leaves Nahe's
  first dose available for the main route. Swim up on the
  prompted ascent and let Nahe rescue the current Tidewalker.
- Primary decision loop: use Tides of Time to see the selected
  predecessor's echo aboard the boat. Read the prior response
  marker, talk with Nahe and decide whether to take the one
  offered Ozen or leave it with her for a follower. Taking it
  grants one carried unit. A separate command can use it for
  immediate recovery.
- Positive terminal: settle the dose choice and reach the
  scripted blackout and the next cabin conversation at Scrap
  Harbour. Stop before pursuing a later supply. The proved
  recorded path takes and consumes the dose before the handoff.
- Failure boundary: the scripted blackout follows the dose
  choice even after recovery. It is not evidence of a
  player-caused death or reset. The unassisted drowning
  condition and exact failure timing were not reproduced.
- Included: predecessor selection and visible candidate traits,
  ascent and movement aboard, the predecessor echo and option
  marker, the local conversation, the single inherited dose,
  accepting or leaving it, the trait signal and treatment use
  on the captured path.
- Excluded: appearance authoring, local offline presets, demo
  app PPSA36840, skins, later caches, resupply, pursuer routes,
  faction history, endings, network transport and server
  publication timing. A follower loading an exact captured
  outgoing seed was not independently run here.
- Potential scoped module: test how the inherited Marketland
  security state gates a later approach in the same commercial
  edition.
- Direct-play status: no personal console session, save or
  server inspection. Two independently recorded English
  PS5 Pro playthroughs were sampled in short, silent
  background frame sequences, with release and developer
  accounts to qualify provenance and alternate branches.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| TOT-001 | The commercial PS5 Standard release is English-capable and shipped April 22, 2026. The two recorded witnesses continue beyond the demonstration scope. | Confirmed | Corroborated | High | P1, P2; W1 and W2 full-game metadata and captured route |
| TOT-002 | The Follow menu selects an existing Story-Link. Candidate cards expose dominant traits and progress. The player's selected source remains named in the scene. The source is an earlier play record selected by the current player. | Observation | Corroborated | High | P3, P4; W1 0:52–1:01, W2 1:18–1:37 and 3:23–3:34 |
| TOT-003 | The ascent leads to Nahe's boat. Activating the local Tides of Time cue shows a translucent earlier actor on the same deck. W1 also marks the prior response beside the current option. The current player can commit another option. | Observation | Corroborated | High | P4; W1 1:20–1:52, 2:49–3:03 and 4:55–5:04; W2 3:23–3:35 |
| TOT-004 | When the followed player leaves the dose, Nahe can offer one unit. In W1 she attributes that unit to the named predecessor. Release accounts describe predecessor consumption as an unavailable incoming dose. That absence was not replayed in the two console recordings. | Observation | Corroborated | Medium | P3, P4; W1 4:38–4:59; W2 5:27–5:42; S1, S2 |
| TOT-005 | Both console witnesses accept and receive the single blue container. The interface reports that Nahe will have nothing for followers and shows an increase in Survivalist. The playable leave option retains the dose for a follower and is reported as Cooperative in release play. | Observation | Corroborated | Medium | P3 trait and consequence rules; W1 4:55–5:13; W2 5:37–5:53; S1, S2 |
| TOT-006 | The handover supplies a carried unit first. A separate consume command removes it and raises the visible health reserve. Both console witnesses then enter a scripted blackout and proceed to the next conversation. | Observation | Corroborated | High | W1 5:03–5:18, 5:26–5:38 and 6:39–6:55; W2 5:44–6:00, 6:10–6:32 and 7:20–7:36; S1 |
| TOT-007 | The studio describes using the selected earlier record to set a level and recording the current run's choices into its own Story-Link as levels finish. This defines the intended follower-side consequence. The console recordings show local flags and feedback rather than verification of a backend write. | Confirmed | Direct | High | P3, P4; W1 5:04–5:12; W2 5:44–5:53 |

## Basic data

- Release / origin: DigixArt, THQ Nordic, PlayStation 5 Standard
  edition, April 22, 2026. English narration and interface in
  the witnesses.
- Mechanical families: FAM-012 for inspecting and applying
  the predecessor's recorded information and FAM-017 for the
  dependence between source choice, available stock and use.
- P1: [PlayStation Store commercial PS5 Standard listing](https://store.playstation.com/en-us/product/EP4389-PPSA29986_00-TIDESOFTOMORROW1).
  Product, platform, release date, distributor and language.
- P2: [THQ Nordic's commercial release announcement](https://thqnordic.com/news/dive-into-tides-of-tomorrow-narrative-adventure-from-award-winning-road-96-creators-is-out-now).
  Distinguishes the full April 22 release from the earlier demo.
- P3: [DigixArt's Story-Link and trait explanation](https://blog.playstation.com/2026/03/03/tides-of-tomorrow-how-players-will-impact-one-anothers-solo-adventures-out-april-22/).
  Establishes predecessor selection, the level-by-level
  direction of stored effects and the trait summaries.
- P4: [Official game site](https://tidesoftomorrow.thqnordic.com/).
  Describes the earlier actor's echoes and variable scene state.
  The [game director's published launch account](https://news.xbox.com/en-us/2026/04/22/tides-of-tomorrow-player-choice/)
  confirms that earlier actions set local narrative state
  while the current player can choose independently.
- W1: [Ben-Gun's English PS5 Pro full-game capture](https://www.youtube.com/watch?v=_VuZzj-B_L4&t=52s).
  Shows binding, rescue, attributed offer, divergent choice,
  follower notice, item use and subsequent scene.
- W2: [Skycaptin5's English PS5 Pro release-day full-game recording](https://www.youtube.com/watch?v=aMoDLXRYLnQ&t=196s).
  Chooses a different recorded predecessor. Shows the
  local vision, same offer and the separate restorative use.
- S1: [Launch-day prologue walkthrough](https://intoindiegames.com/walkthroughs/tides-of-tomorrow-walkthrough-part-1/).
  Describes preserving the dose, the Cooperative signal and
  the following blackout.
- S2: [Released-game player's account of the entry variants](https://somanygames.co.uk/review/tides-of-tomorrow/).
  Describes the earlier Tidewalker taking or leaving the
  bottle, and the resulting available-or-unavailable offer.
- Claim IDs: TOT-001–TOT-007.

### Reproducible fixture evidence

1. Confirm a candidate on the Follow screen. In W1, compare
   the confirmation card near 0:58 with the persistent
   source label on the boat. W2 follows a different record.
   A trait is a guide to the earlier run, not a guarantee
   about one particular dose.
2. Complete the prompted ascent, reach Nahe and activate the
   visible L2 Tides of Time cue on deck. W1 2:49–3:03 and
   W2 3:23–3:35 show an echo in the same space, then return
   to the current character. Continue the conversation.
3. In W1 at 4:45 Nahe credits the predecessor with keeping the
   dose. The choice around 4:58 shows one held bottle and
   the two responses. The prior-choice symbol sits beside
   leaving the dose, independently of the current control
   symbols. W2 also sees the two responses, at 5:39.
4. In W1 take it around 5:04. Notice the Survivalist signal
   and the explicit follower shortage before activating the
   new inventory unit. The count reaches one near 5:12.
   W2 repeats this handover around 5:44–5:53.
5. Use the unit from stock. W1 around 5:14–5:17 and W2 around
   5:56–5:59 show depletion to zero and a rising health
   display. This second action does not produce another
   follower choice.
6. Finish the conversation. After the scripted interruption,
   W1 wakes in the next cabin scene. The release walkthrough
   describes the same interruption after the leave choice.
   Do not infer that taking or leaving changes this handoff.

## Mechanical decomposition

### Action Genes

- ACT-008: swim in the directed ascent and navigate the
  boat as the active Tidewalker. TOT-003.
- ACT-131: use a carried Ozen unit once for personal recovery.
  Taking it and using it are separate transitions. TOT-006.
- ACT-232: choose the offered answer that takes the dose
  or leaves it with Nahe. TOT-005.
- ACT-341: approach and address the reachable Nahe to advance
  the boat conversation and reach the offer. TOT-003–TOT-004.
- ACT-915: select and confirm a recorded predecessor from
  the Follow interface as the source of this scene. TOT-002.
- ACT-916: activate the local vision to observe the selected
  predecessor's visible echo from the current scene. TOT-003.

### System Behaviour Genes

- SYS-1972: the selected predecessor's recorded take-or-leave
  outcome determines stock for the corresponding scene.
  Current taking records a shortage for players who later
  follow this run. TOT-004–TOT-005, TOT-007.
- SYS-1973: the scene response updates the applicable behaviour
  trait that the interface surfaces. Taking has Survivalist
  feedback, while reported leaving has Cooperative feedback.
  The studio associates those traits with the selectable
  record. TOT-002, TOT-005, TOT-007.

### Constraint Genes

- CON-891: the one offered dose can enter personal stock
  or remain reserved for a follower. The scene does not
  permit both settlements from that same unit. TOT-004–TOT-005.

### Information Genes

- INF-119: the HUD exposes current life and carried Ozen
  separately so the player can read acquisition before use.
  TOT-006.
- INF-635: a prior-choice symbol identifies the recorded source's
  specific response among current options. Its separate
  placement lets the current player repeat or diverge.
  TOT-002–TOT-003.

### Objective Genes

None admitted. The handoff marks the end of the evidence
fixture. Taking the dose is not a requirement for reaching it.

### Time Genes

None admitted. The ascent has contextual motion prompts, but
a universal timer, break condition and fixed numeric life
drain for the scoped choice were not established.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Follow menu with multiple recorded candidates | Confirm an eligible source | Subsequent prompt, character echo and setting resolve from that source | TOT-002–TOT-003 |
| Present boat deck and its vision cue | Activate Tides of Time | The preceding actor's trace appears at the local position | TOT-003 |
| Nahe retains one dose from the selected source | Advance the conversation | Two mutually exclusive local responses are offered | TOT-004 |
| One offered unit | Take it | Carried stock gains one, Survivalist is credited and the follower shortage is reported | TOT-005 |
| One offered unit | Leave it | No unit acquired and the dose remains with Nahe for a follower, with reported Cooperative credit | TOT-005 |
| One unit carried after acceptance | Consume it separately | Stock returns to zero and current health rises | TOT-006 |
| Settled boat interaction | Finish the conversation | Scripted interruption precedes control in the next scene | TOT-006 |

## Strategic and experiential structure

The predecessor's action is part of the current room's
resource conditions. The current player can spend that
advantage or keep it available for a follower. The game
discloses this direction of effect at the choice, and
treatment remains an additional local action once taken.

## Replay and variation

The two PS5 traces use different predecessors and take
and consume the dose in both. The first explicitly shows
that this diverges from the earlier source's response.
The written release witness supplies the make-available
alternative. No simultaneous shared stock race or
measured server delay is asserted.

## Adjacent systems and history

Later places have caches, vendors and automated scene
changes. The studio describes each as influenced by
level-specific stored play. This record stops before
those mechanisms can supply another Ozen or introduce
a different recipient, price or survival condition.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-131, ACT-232, ACT-341, ACT-915, ACT-916 | Navigate, use a unit, choose, talk, bind a source and view its echo |
| System Behaviour | SYS-1972, SYS-1973 | Resolve follower-side stock and retain behavioural trait feedback |
| Constraint | CON-891 | One dose has one settlement |
| Information | INF-119, INF-635 | Distinguish health, carried stock and the earlier response |
| Objective | None | The scripted handoff bounds the capture |
| Time | None | The scoped dose choice has no certified deadline |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `695` (`GAME-0001`–`GAME-0695`).
- Exact genome matches: none.
- Tied near matches: `GAME-0268` — Undertale (`4 / 24 = 0.166667`); `GAME-0362` — The Elder Scrolls III: Morrowind (`4 / 24 = 0.166667`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Undertale (GAME-0268)](undertale.md) | ACT-008, ACT-131, ACT-341, INF-119 | Both use direct movement, contextual interaction and a separately carried restorative with visible health. Undertale settles encounters by non-damaging commands and continuous projectile evasion. Nahe's offer comes from a selected older play record and creates a supply condition for another player. | Near, `0.166667`. |
| [The Elder Scrolls III: Morrowind (GAME-0362)](the-elder-scrolls-iii-morrowind.md) | ACT-008, ACT-232, ACT-341, INF-119 | Both move to a local actor, read resources and select a meaningful dialogue response. Morrowind follows written orders and transfers a package along a route in its own save. The dose in Tides of Tomorrow reflects another player's earlier response, and the current choice forms a later follower condition. | Near, `0.166667`. |

## Taxonomy impact

Reuse a local authored response and a separate restorative
command. Isolate selection of another run, its opt-in echo,
the inline indication of its decision, and the asymmetric
resource settlement and behavior feedback.

## Negative results

- The predecessor is selected from an earlier play record.
  Appearance editing and the player's own game state do not
  supply that input.
- Recovering the record visually does not transfer the dose.
  A current dialogue choice settles it.
- Acquiring the bottle does not itself raise the health bar.
- Recovery in the two captures does not prevent the prologue
  interruption.

## Delta summary

Eleven genes describe the local choice and the directed
dependency across two runs.

## New facts

- The person being followed is visible before entering the scene.
- An inline predecessor marker can distinguish the earlier reply
  even when both current replies are still available.
- Taking an offer and consuming it affect different stores.

## Principles and design implications

A record from another run can become a current precondition
while preserving player control over the present response.
Expose both the inherited choice and the outgoing consequence
so the player can see where agency passes between runs.

## Puzzle or game generation potential

Prototype two independent play sessions connected through
a one-unit supply flag. Include a choice marker and separate
purchase or use actions. Test that taking a unit never
simultaneously credits the next shopper with the same supply.

## New genes

- ACT-915
- ACT-916
- CON-891
- INF-635
- SYS-1972
- SYS-1973

## New combinations

None. None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 442](../../../research/taxonomy-changes/TAXONOMY_CHANGE_442.md).

## New questions

- How is the alternate first conversation presented when the
  predecessor used the only dose?
- At which settlement point may another account follow the
  new scarcity state of a recorded run?

## Next recommended game

Continue Selection 060 with GAME-0697, Radiant Silvergun,
on Japanese Sega Saturn.

## Why this game

Its first offer shows an earlier player's actual decision
as a concrete condition, then allows a different outcome
to travel to another play session.
