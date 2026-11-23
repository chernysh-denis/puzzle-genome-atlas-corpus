---
game_id: GAME-0604
slug: the-alters
game_title: "The Alters"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-123
    - ACT-245
    - ACT-341
    - ACT-805
  system:
    - SYS-312
    - SYS-1777
    - SYS-1778
  constraint:
    - CON-136
    - CON-849
    - CON-850
  information:
    - INF-567
    - INF-568
  objective:
    - OBJ-327
  time:
    - TIM-003
---

# Game: The Alters

The decision roles follow the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Room sizes, names, recipe counts and the sampled journey cost are parameters
of this route.

## Analysis scope

- Version / ruleset: commercial Xbox Series X|S digital base game,
  product `9N0P25WJHM8C`, released 13 June 2025. English Xbox Series X
  launch-day footage supplies the main trace. Another Series X trace
  displays Portuguese interface text. The installed build, exact difficulty
  setting and parity with the current binary were not independently verified.
- Primary decision loop: decide how to spend the time before sunrise on
  scouting, construction, supplies and the staged recovery of the base.
  Use the Quantum Computer to commission the one specialist needed for
  the failed machinery. Check departure readiness and start the first
  journey when the base can leave.
- Entry: Jan has reached the mobile base in the prologue. Begin at the
  subsequent Organics and Rapidium preparations. Intake and routine
  tool fabrication leading into this state are setup.
- Exit: confirm the first journey after the Technician assists in the
  machinery room, observe the base moving and regain the travelling
  interior. Stop before the separate Common Ground task or Act 1.
- Included: local scouting, hand-gathered Rapidium, surveyed Organics and
  relays, required modules and prologue demonstration, meal preparation,
  two attempted starts and the intervening machinery input, calls,
  the first branch and wake, assisted repair and the first timed departure.
- Excluded: landing and first base intake, unrelated collecting and optional
  room optimisation, later Alters and role choices, Act 1 shelter, later
  comms repairs, campaign survival or endings, DLC, other platforms and
  exact current build parity.
- Suggested later scopes: compare two genuinely available role branches
  in Act 1, or reproduce the time and rest boundary under a named build
  and difficulty.

## Direct-play status

No direct play was performed. The Xbox product and launch announcement
establish the commercial target. Static frames from two independently
published Xbox Series X recordings support early progression and the
Technician branch, with the English series continuing through his repair
assistance and actual departure. Firsthand route guides corroborate the
intervening tasks and the mass-dependent fuel cost. The PC trace is
corroboration only. Exact settings, alternate failure outcomes, installed
builds and tested save persistence were not independently established.
No video or audio playback was used.

## Claim ledger

| ID | Claim | Claim status | Evidence quality | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- |
| TA-001 | The commercial Xbox release uses Rapidium and alternate-life crew creation. Following base intake Jan finds and gathers Rapidium during the prologue; the guide records 30 as the tutorial threshold. | Observation | Corroborated | High | P1, P2, W1 23:00–23:40 and call 25:40, H1, H2. No current-build or Series S trace claim. |
| TA-002 | Surface probes resolve patches of the eligible Organics deposit. An outpost over the surveyed deposit needs a linked pylon route to base before extraction can supply it. | Observation | Corroborated | High | H2, H3; W2a 11:00–18:40, W1 43:20, 45:50. Exact maximum relay distance was not tested. |
| TA-003 | Communications supplies the Womb prerequisite. Its footprint connects to the base, the facility enables the prologue’s Molly demonstration, and the kitchen supplies six Mush meals for the route. | Observation | Corroborated | High | W1 25:40–31:10; W2a 19:30–25:40; W2b 2:00–4:40; H1, H2. Thirty Rapidium, six meals and the tutorial Organics target are guide or UI parameters, not a fuel formula. |
| TA-004 | Trying the Command Center control fails. The machinery intervention is followed by another failed start, fault escalation and Earth contact. The Quantum Computer history and a further call precede the legal first branching operation. | Observation | Corroborated | High | W2b 6:30–16:40, H1, H2. Exact dialogue variants and retry behaviour were not isolated. |
| TA-005 | The Quantum Computer discloses Going Away and the alternative Staying Behind associated with Technician before commitment. The new Jan appears in the Womb and recalls a different life. | Observation | Corroborated | High | W2b 18:10–31:40, W1 55:50–68:20, P1, H1. No wider roster of available first alternatives is inferred. |
| TA-006 | Following wake and dialogue, both Jans participate in a scripted machinery repair. Ordinary control resumes and the command terminal then offers a successful departure path. | Observation | Corroborated | High | W2b 33:00–33:20; W2c 0:00–2:10; H1. The trace does not show a separately commanded two-character minigame. |
| TA-007 | A sunrise deadline pressures the opening. The base panel and departure interface expose the available Organics and the journey requirement derived from base mass, separately from the taught preparation quantity. | Observation | Corroborated | High | W2c 1:50–2:10; H1, H2. H2 gives 172 in its layout and describes a tutorial Organics target of 180; neither is a universal departure cost. |
| TA-008 | Accepting Start Journey in the repaired state starts the first physical move and ends the current site’s countdown. The next activity belongs to a separate task. | Observation | Corroborated | High | W2c 2:00–3:00, H1, H2; W3 56:20 independently corroborates the separate PC route. |
| TA-009 | An early linked Organics network, later work scheduling, and choosing later Alters are separable activities. Sunset and energy failure, alternative dialogue effects and load behaviour remain untested. | Observation | Limited | Medium | W1, W2a–c, H1, H2. The observed traces represent ordinary progression and not a failure experiment. |

## Basic data

- Release / origin: 11 bit studios, first full commercial Xbox Series X|S
  release on 13 June 2025.
- Platform: single-player Xbox Series X|S base game. `PLAT-XBOX-SERIES`
  is the target; Xbox Play Anywhere entitlement is separate from measured
  PC parity. One walkthrough credits launch-day Game Pass Ultimate access.
- Puzzle families: ordered dependency sequencing (FAM-017) for the chained
  machinery and branch prerequisites; real-time system pressure (FAM-010)
  for deciding which preparation to carry out before sunrise.
- P1: [Microsoft Xbox listing](https://www.xbox.com/en-us/games/store/the-alters/9N0P25WJHM8C)
  establishes the SKU, date, platforms and Rapidium/branch premise.
- P2: [Xbox Wire launch listing](https://news.xbox.com/en-us/2025/06/06/next-week-on-xbox-new-games-for-june-9-to-13/)
  and [Xbox Wire developer session](https://news.xbox.com/en-us/2025/04/11/id-xbox-developer-sessions-10-indies/)
  corroborate the launch platform, alternate memories and survival premise.
- H1: [Into Indie Games firsthand prologue route](https://intoindiegames.com/walkthroughs/the-alters-walkthrough-prologue-2/).
  Provides the communications, demonstration, failed starts, required
  assistance and actual departure order.
- H2: [Gamepressure firsthand escape report](https://www.gamepressure.com/the-alters/how-to-escape-the-sun/z0119da).
  Records the gathering and food targets, the mass-dependent departure cost
  and the transition away from the timed site.
- H3: [Gamepressure scanner and Organics setup report](https://www.gamepressure.com/the-alters/how-to-use-a-scanner/z2119d3).
  Documents surveying a deposit and connecting the extraction point.
- W1: [FG77BR Series X prologue](https://www.youtube.com/watch?v=oLeIClrxGDY).
  Xbox controller prompts, early field actions, carried materials and branch
  aftermath. This recording does not independently show the first departure.
- W2a, W2b, W2c: Renfail's launch-day Xbox Series X commercial route,
  [Part 2](https://www.youtube.com/watch?v=E-DyjPY1qMA),
  [Part 3](https://www.youtube.com/watch?v=-zCLC3FGOCE) and
  [Part 4](https://www.youtube.com/watch?v=O1PPOoUiv-w).
  Selected frames show scan and facilities, two failed starts, timeline
  and branch commitment, wake, joint repair and the moving base.
- W3: [GLP Windows Steam commercial route](https://www.youtube.com/watch?v=EkfSGYzx4UY).
  The creator identifies the PC capture. First Technician and first Journey
  occur at 43:12 and 56:20 respectively. The run is independent corroboration,
  not an Xbox build observation.

### Reproducible route evidence

1. After base intake, start the surface supply work. Follow the red mineral
   discovery and gather Rapidium. H2 records the 30-unit tutorial goal.
   W1 23:00–23:40 shows the red discovery interval and W1 25:40 the call.
   These are applied resources and instructions within the game.
2. Sample the first Organics ground with the scanner. W2a 14:50 shows the
   mesh over a coloured deposit; 16:30 previews relay placement. Set the
   Mining Outpost at the surveyed site, extend the pylon chain to the base
   and use the connected terminal to extract. H3 and W1 45:50 distinguish
   a placed endpoint from a completed connection.
3. Use the communications and construction interfaces to obtain and fit the
   Womb. W2a 19:30, 21:00 and 25:40 show the call, grid and finished room.
   Complete the required Molly demonstration at the module and report back
   to Earth. Use the Kitchen to prepare six Mush meals. W2b 4:10–4:40 shows
   the recipe/work sequence, and H1/H2 give the taught quantity.
4. Use the right Command Center terminal and investigate the first failed
   start in Machinery. Work the lever and try the terminal again. The
   second failure escalates the fault and directs another call. W2b
   6:30–8:10 shows the changed emergency state. After inspecting the Quantum
   Computer, call again to unlock the first branch at W2b 8:50–16:40.
5. Preview and commit Staying Behind, associated with Technician, in the
   Quantum Computer. W2b 18:10–19:00 shows its alternative to Going Away
   and offers Alterate. The new Jan is present by W2b 24:20, followed by the
   conversation about his own past. W1 60:50–68:20 gives an independent
   look at the result.
6. Obtain his involvement at the machinery. W2b 33:00 shows two figures
   operating separate positions in the same assembly after the required
   conversation. The cut leads to ordinary control at the machine in W2c.
   Jan can now try a real departure rather than repeat the solo failure.
7. Check the fuel on the command terminal, returning to the Organics
   outpost if necessary. The taught collection target and the current
   layout-dependent cost are distinct. Confirm Start Journey at W2c
   2:00–2:10; 2:30 shows the mobile base rolling. Stop after the return to
   the travelling interior at W2c 2:40–3:00.

Claim IDs: TA-001–TA-008. Frame timestamps locate evidence; they do not
define action lengths or an optimal schedule.

## Mechanical decomposition

### Action Genes

- ACT-008: move Jan directly across the deposit area and between base rooms.
- ACT-123: commit the known Mush recipe at the Kitchen.
- ACT-245: collect one available Rapidium yield at the surface source.
- ACT-341: operate the reachable communications and machinery fixtures,
  then interact with the new Jan in the Womb.
- ACT-805: choose the counterfactual life branch that commissions Technician.
- Claim IDs: TA-001–TA-006.

### System Behaviour Genes

- SYS-312: accepted materials and active work advance the selected Mush
  recipe to finished meal stock.
- SYS-1777: a committed alternative life yields a separate active Jan
  with the associated recollections and mechanical specialty.
- SYS-1778: connected scanner points reveal the usable deposit footprint
  for registration and local extraction.
- Claim IDs: TA-002, TA-003, TA-005, TA-006.

### Constraint Genes

- CON-136: report the demonstration and progress through the failed starts,
  history inspection, authorised branch and wake to unlock the assisted
  repair. A repaired state is a prerequisite of the successful departure.
- CON-849: extraction to the base requires a permitted relay chain.
- CON-850: the final fuel threshold follows current base mass.
- Claim IDs: TA-002–TA-008.

### Information Genes

- INF-567: see a recorded past, marked alternative and resulting role
  on the life timeline before commitment.
- INF-568: read the assembled mass and the current amount of Organics
  against the journey cost before launching.
- Claim IDs: TA-005, TA-007, TA-008.

### Objective Genes

- OBJ-327: commission and wake the needed Technician, use his aid to
  restore the base and leave the threatened site with sufficient supplies.
- Claim IDs: TA-003–TA-008.

### Time Genes

- TIM-003: the simulated day and approaching sunrise constrain which
  preparation to complete before deciding to leave. This does not assert
  uninterrupted time passage in every interface or scripted scene.
- Claim IDs: TA-003, TA-007, TA-008.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Early supply scouting | Gather Rapidium and report the discovery | The prologue opens the facility instructions | The field resource feeds the character-creation sequence | TA-001, TA-003 |
| Organics deposit not yet supplying base | Survey, place the outpost and link pylons | The connected outpost can supply Organics | The placement and relay path are separate conditions | TA-002 |
| Facility plans and enough materials | Construct the connected Womb and finish the demonstration | Earth can be notified of its success | The facility and its demonstration are prerequisites | TA-003 |
| Supplies prepared; machine untested | Attempt start, intervene at the lever and retry | The second failure exposes the need for a specialist | A solo reset is insufficient in this chain | TA-004 |
| Fault escalated; initial history visible | Review the Quantum Computer and contact Earth | Technician's alternative becomes actionable | Reading history and commissioning an Alter are separate steps | TA-004, TA-005 |
| Staying Behind available | Commit the branch and wake the created Jan | A second Jan with a different past is active | The original stays and gains a crew counterpart | TA-005 |
| Both valid crew members awake | Meet the Technician and advance the machinery scene | Both work on the assembly; the departure terminal is usable | The role has an observed consequence beyond dialogue | TA-006 |
| Repaired base with sufficient fuel and supplies | Confirm Start Journey | The base moves away; ordinary control resumes | Physical departure completes this scoped route | TA-007, TA-008 |

## Strategic and experiential structure

The opening trades clock time among scouting, cooking, contact and machinery
work. A field survey reveals a source, but the outpost cannot add to the
departure stock until its relay path reaches the base. Useful facilities
add mass, so fuel targets can change even when the itinerary does not.
The earlier engine interventions unlock the authored branch. Waking the
Technician has a measurable payoff at the damaged machinery and enables the
actual departure. Claim IDs: TA-002–TA-008.

## Replay and variation

The two commercial Xbox traces corroborate the broad progression without
establishing identical build numbers, routes or time expenditures. The
guide's 172-unit departure threshold belongs to its base layout. No test
of a late failure, unsupported layout, failed relay edge or replay from
a save was performed for this analysis. Claim IDs: TA-007–TA-009.

## Adjacent systems and history

The first branch visibly presents the Technician option. That does not
establish which roles become available later, nor that every later repair
needs him. The first vehicle movement closes the scoped route. Subsequent
Comms work and Common Ground are recoverable as later modules.
Claim IDs: TA-005, TA-008, TA-009.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-123, ACT-245, ACT-341, ACT-805 | Direct movement, known meal, material, fixture and life branch |
| System Behaviour | SYS-312, SYS-1777, SYS-1778 | Recipe progress, separate embodied crew member, deposit surveying |
| Constraint | CON-136, CON-849, CON-850 | Authored prerequisites, linked extraction, mass-dependent fuel |
| Information | INF-567, INF-568 | Life and skill preview, departure fuel and mass |
| Objective | OBJ-327 | Restore transport with required specialist and actually leave |
| Time | TIM-003 | Allocate work under the approaching sunrise |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `603` (`GAME-0001`–`GAME-0603`).
- Exact genome matches: none.
- Tied near matches: `GAME-0314` — Grounded (`6 / 35 = 0.171429`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [GAME-0314 Grounded](../g-l/grounded.md) | ACT-008, ACT-123, ACT-245, ACT-341, SYS-312, TIM-003 | Both combine direct movement, field collection and a known recipe with local world interactions under live pressure. The Alters adds a surveyed relay supply, a life branch that commissions a specialist and a mass-dependent first departure. Grounded teaches miniature survival through sample analysis, early tool and shelter preparation, and a retained respawn point. | 6 shared of 35, Jaccard 0.171429 |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_350](../../../research/taxonomy-changes/TAXONOMY_CHANGE_350.md)
  records eight newly isolated Active boundaries; existing definitions are retained.

## Negative results

- CON-232 requires a shaft and mechanically covered demand. The outpost
  depends on a connected relay path supplying resources, so it does not
  imply a shaft, persistent power capacity or a trade link such as SYS-1404.
- INF-279 shows a nearby resource's identity, bearing and distance. The
  surveyed footprint depends on several local probes and yields a
  registered, extractable deposit, rather than a simple revealed marker.
- SYS-1108 accumulates assigned crew labour in a damaged room under active
  hazards. The opening instead observes a scripted repair after unlocking
  and waking a required specialist, with no verified room repair ticks.
- CON-704 uses mapped beacon connectivity, fixed unit fuel and FTL readiness.
  The observed departure cost changes with the mass of the assembled base.
- OBJ-143 requires later destination interaction and verified save retention.
  The observed closing transition is a physically moving travelling base.

## Delta summary

## New facts

- [Observation | Corroborated | High] Rapidium, connected Organics extraction
  and module work precede the first attempts to leave. TA-001–TA-004.
- [Observation | Corroborated | High] The revealed Technician branch brings
  a separate crew member into the world. He is present for the repair of
  the failed mechanism. TA-004–TA-006.
- [Observation | Corroborated | High] The selected route ends when the base
  physically starts its first journey with mass-dependent fuel readiness.
  TA-007, TA-008.

## New genes

- [Observation | Corroborated | Medium] ACT-805, SYS-1777, SYS-1778,
  CON-849, CON-850, INF-567, INF-568 and OBJ-327.

## New combinations

- [Observation | Direct | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_350.

## New questions

- How does missing the first sunrise deadline settle on the launch build?
- On a known installed version, can the required departure cost be reproduced
  under two different legal hull layouts?
- Which later role branches materially alter a different encountered task?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0605`, Outtrigger, on the North
  American commercial Dreamcast disc. One complete offline arena task,
  including its preparation and settled result.

## Why this game

- [Hypothesis | Limited | Medium] The first departure makes a character's
  alternative history consequential to a concrete repair and a live
  resource problem rather than to dialogue alone.
