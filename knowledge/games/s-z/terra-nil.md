---
game_id: GAME-0716
slug: terra-nil
game_title: "Terra Nil"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-117
    - ACT-932
  system:
    - SYS-153
    - SYS-2005
    - SYS-2006
    - SYS-2007
    - SYS-2008
  constraint:
    - CON-229
    - CON-240
    - CON-292
    - CON-440
  information:
    - INF-067
    - INF-648
  objective:
    - OBJ-375
  time:
    - TIM-002
---

# Game: Terra Nil

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Place turbines on rock, clean powered footprints, and rotate
irrigators over prepared soil until the greenery target opens
the next restoration phase.

## Analysis scope

- Version / ruleset: English Windows Steam commercial base game,
  app 1593030, released 28 March 2023. Use the release-window
  Gardener preset with its guided building objectives enabled.
  The exact Steam build and map seed of each capture are unverified.
- Structured analysis target: PLAT-WINDOWS-PC in
  [platform coverage](../../platforms/games.json).
- Entry: select Gardener and start the opening River Valley.
  Begin at the first turbine placement objective on the barren
  tutorial plot, after the camera instructions.
- Primary decision loop: choose a free rock within reach of the
  next treatment area and place a turbine. Fit powered scrubbers
  where their clean-soil footprints cover useful bare ground.
  Rotate and preview an irrigator to grow fresh greenery and
  replenish the leaf reserve. Repeat around the expanded valley,
  placing powered pumps on usable dry beds to restore waterways.
- Positive terminal: commit enough real greenery to open phase
  two on the same landscape. Stop at the temperate handbook
  transition and the newly available phase-two controls.
- Included: rock foundations, priced facilities, automatic power
  radius and capacity preview, cleaning before irrigation, water
  pump and channel response, foliage-linked budget return,
  conditional coverage previews and the vegetation quota.
- Excluded: initial camera instructions, executing the Calcifier
  and Excavator branches, biome diversity construction, climate
  triggers, fauna scans and recycling. Fee and yield formulae
  beyond the visible sample, generator seeds and update-specific
  changes are unverified. No mobile, console, demo or later maps.
- Potential scoped module: compare a placed Calcifier opening
  a turbine site with using a naturally available rock on the
  same starting map.
- Direct-play status: no personal Windows session or executable
  comparison. Steam and the publisher establish the release.
  Two post-release recordings show the opening mechanics. The
  main trace uses Gardener. The comparison trace identifies PC
  Steam and Environmental Engineer. Media frames were inspected
  in the background without audio.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| TN-001 | The Steam base game launched for Windows on 28 March 2023. The Gardener trace confirms a 1,500-leaf starting allocation, 50% base cost, tutorials and building unlock objectives before using the River Valley opening. The build and seed are unverified. | Confirmed | Corroborated | High | P1, P2; W1 1:07–1:10; W2 opening identification |
| TN-002 | A turbine requires a rock foundation and supplies nearby buildings. A pending powered consumer shows a projected connection, reach overlay and load on the serving turbine. In the guided fixture the turbine label shows a six-slot capacity. | Observation | Corroborated | High | W1 1:58–2:10, 2:17–2:23, 9:54–10:08; W2 0:08–0:26 |
| TN-003 | A Toxin Scrubber requires eligible terrain and power. Placing it can turn nearby cracked barren ground into clean brown soil before any grass appears. The first guided block requires four scrubber placements. | Observation | Corroborated | High | W1 2:05–2:34, 2:35–2:40; W2 0:14–0:28 |
| TN-004 | An Irrigator requires clean ground and waters an orientable neighbouring footprint. The preview distinguishes eligible and excluded ground. Placement animates irrigation and converts the selected clean area into greenery. The first guided block requests three irrigators. | Observation | Corroborated | High | W1 2:35–3:16; W2 0:28–0:42 |
| TN-005 | The toolbar lists a placement price, and the map preview can show different leaf gains at different placements. The post-placement leaf counter changes as new greenery is credited. At the guided stage a turbine costs 40, a scrubber 25 and an irrigator 25. | Observation | Corroborated | High | W1 2:08 and 2:32–3:08; W2 0:28–0:44 |
| TN-006 | A Water Pump needs power and usable dry-channel terrain. Its card explains that its water fills the connected riverbed and cleans the banks, and that placement height can affect reach. After confirmation, a formerly dry channel holds water and its banks change. | Observation | Corroborated | High | W1 7:34–7:43 and 9:54; W2 1:59–2:07, 2:24–2:33 |
| TN-007 | The greenery ring is progress toward a regional target. Candidate progress is prospective. Committing a final irrigator in Gardener reaches 104% with bare land still present and adds phase two. Environmental Engineer remains in phase one at a committed 99% before its subsequent placement and unlock. | Observation | Corroborated | High | W1 10:28–10:50; W2 3:24–3:40 |
| TN-008 | Gardener stages availability inside phase one. The Excavator slot is still marked with its 75% condition while settled greenery is 63%. Phase two changes the toolbox and handbook phase on the same valley. The harder witness's initial palette differs. | Observation | Corroborated | High | W1 1:08, 7:28 and 10:42–10:49; W2 0:08–0:44 |

## Basic data

- Release / origin: Free Lives original project, published by
  Devolver Digital on Windows Steam, 28 March 2023. The current
  storefront also credits Clockwork Acorn.
- Families: FAM-003 for converting addressed terrain between
  incompatible stages and FAM-017 for the ordered dependency
  from power supply through cleaning, irrigation and the next
  phase's vegetation requirement.
- P1: [Steam app 1593030](https://store.steampowered.com/app/1593030/Terra_Nil/).
  Commercial identity, launch date, Windows support, and
  release descriptions. Checked 2026-11-25.
- P2: [Devolver Digital launch announcement](https://www.devolverdigital.com/propaganda/terra-nil-springs-forth-on-pc-and-netflix-on-march-28).
  Confirms the PC launch date and distinguishes other editions.
- W1: [Chocoholie, post-launch walkthrough](https://www.youtube.com/watch?v=TedKHTfSmiI&t=67s).
  Published 31 March 2023. Covers the Gardener confirmation,
  prescribed tools, expanding valley and phase-one result.
  The original tooltips and handbook are visible in the frames.
- W2: [Quill18, PC Steam launch-day play](https://www.youtube.com/watch?v=O4kOC6Ih0CA).
  Published 28 March 2023. Independently checks facilities,
  channel response and threshold on Environmental Engineer.
  Its prices and opening progress are outside the Gardener contract.

### Reproducible fixture evidence

1. At 1:08 W1 confirms Gardener. Around 2:00 the turbine preview
   attaches to an exposed stone. At 2:18 the scrubber ghost shows
   both its candidate footprint and a line to the nearby turbine.
   The finished scrubber footprint has clean brown ground and
   the vegetation goal is still zero when irrigation is introduced.
2. At 2:53 and 2:55 the same priced irrigator selection shows
   different candidate returns at different positions, including
   +47 and +109. The marked orientation changes the working
   footprint. These frames do not isolate a gain attributable to
   rotation while holding terrain and anchor constant.
3. Near 7:38 W1 shows a channel filling from a powered pump.
   Around 2:00–2:06 W2 shows a red candidate on unsuitable
   terrain, then the water and green banks after placement.
   The pump card separates its power and site needs.
4. At 10:30 in W1 the settlement is still below the target.
   A later irrigation preview shows over 100%, but the phase
   does not change on the preview. At about 10:42–10:43 the new
   irrigator is in the world, 104% is visible and the phase-two
   tab appears. The temperate handbook opens. W2 holds at 99%
   in phase one at 3:29–3:33 and opens phase two after planting
   again, with uncultivated terrain left.

## Mechanical decomposition

### Action Genes

- ACT-117: purchase a turbine, scrubber, irrigator or pump at
  its chosen valid anchor.
- ACT-932: rotate the irrigator's effect before confirming the
  building so it can cover a better set of clean tiles.

### System Behaviour Genes

- SYS-153: turbine supply services eligible consumers in its
  local radius.
- SYS-2005: powered scrubbers turn eligible barren cells into
  clean soil while leaving planting for another command.
- SYS-2006: a placed irrigator grows vegetation on compatible
  ground within the orientation-dependent coverage mask.
- SYS-2007: newly green ground credits leaves used to pay for
  later sites and treatments.
- SYS-2008: a powered pump refills an eligible river route and
  changes banks alongside the filled channel.

### Constraint Genes

- CON-229: match a pump to compatible channel terrain and its
  geometry.
- CON-240: match powered machinery to an in-range supply
  with available capacity.
- CON-292: place a turbine on an unused rock foundation and
  respect other buildings' site eligibility.
- CON-440: unlock additional phase-one facilities at the displayed
  progress gates when building objectives are active.

### Information Genes

- INF-067: current progress and the guide disclose the greenery
  objective and the next tool or phase.
- INF-648: before confirmation, inspect the effective tile mask
  and projected leaf delta, including noncontributing tiles.

### Objective Genes

- OBJ-375: meet the vegetation quota to unlock the next phase
  while the existing region and buildings persist.

### Time Genes

- TIM-002: choose each site and orientation without a pressure
  clock. Short settlement animations follow placement.

### Parameters

Rock and channel positions, reach and turbine occupancy, clean
soil, oriented mask, current construction reserve, base prices,
leaf credit, committed greenery and local unlock thresholds.

## Reproducible transitions

| Entry state | Input or event | Expected next state | Evidence |
| --- | --- | --- | --- |
| Barren plot with an unoccupied exposed rock | Commit the turbine on that rock | Available electricity appears for eligible close sites | TN-002 |
| New powered candidate with untreated ground in reach | Place a Toxin Scrubber | Its treatment area changes to clean soil, with vegetation still pending | TN-003 |
| Prepared ground and an irrigator in preview | Rotate or move the candidate and read its mask and result | Compatible cells and expected return update before any building is committed | TN-004–TN-005 |
| Same preview after orientation has been chosen | Pay for and confirm a valid irrigator | New grass grows and earns leaves; coverage progress rises | TN-004–TN-005 |
| Compatible dry riverbed near spare supply | Place the Water Pump | The channel fills within pump reach and the banks respond | TN-006 |
| Committed greenery is below the target, forecast above it | Confirm a qualifying conversion | Phase two becomes available on the retained valley | TN-007 |

## Strategic and experiential structure

A rock determines where supply can start. A scrubber need only sit
inside that supply, so the player can use the outside of its
treatment area for a larger clean-soil return. An irrigation
position and orientation together determine the renovated cells
and the budget for extending the network. Later plant coverage
builds on the retained plan.

## Replay and variation

The two captures reach the same phase boundary with different
layouts, budgets, settings and sequences. Gardener includes a
prescribed guided start and phase-one unlock goals. The harder
trace corroborates the structural prerequisites but does not
authenticate the Gardener prices in other presets.

## Adjacent systems and history

The toolbar includes other terrain tools during the phase.
The Calcifier card shows that water and nearby greenery can
help create a rock site. The selected dependency isolates
existing rock, powered cleaning, irrigation and water pumping.
Other biome, climate, fauna and recycling goals begin later.

## Normalised genome

- Action: ACT-117, ACT-932.
- System Behaviour: SYS-153, SYS-2005, SYS-2006, SYS-2007, SYS-2008.
- Constraint: CON-229, CON-240, CON-292, CON-440.
- Information: INF-067, INF-648.
- Objective: OBJ-375.
- Time: TIM-002.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `715` (`GAME-0001`–`GAME-0715`).
- Exact genome matches: none.
- Tied near matches: `GAME-0284` — Cities: Skylines II (`3 / 28 = 0.107143`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Cities: Skylines II (GAME-0284)](../a-f/cities-skylines-ii.md) | ACT-117, CON-440, SYS-153 | Both place priced infrastructure, extend utility service and use measured progress to unlock capabilities. Terra Nil concerns the eligible footprints of soil cleaning and vegetation conversion. The Cities: Skylines II slice develops an inhabited settlement with roads, zoning, services and milestone demand. | Near, `0.107143`. |

## Taxonomy impact

Reuse priced infrastructure, service reach, compatible foundations,
powered connections, channel geometry, threshold gating,
disclosed objectives and untimed sequential action. Admit
the rotated facility effect, differentiated soil states, irrigation
conversion, vegetation-linked leaf credit, routed river refill,
previewed return and the vegetation-based phase gate.

## Negative results

- Cleaning alone leaves bare brown soil and has no observed
  direct vegetation credit in the guided placement.
- An irrigator's preview can indicate a winning placement while
  the actual phase remains unchanged.
- Candidate masks and gains vary with orientation and position.
  Their exact per-tile scoring rule was not independently measured.
- The quota can exceed 100% with bare ground remaining. It is
  not a requirement to turn every visible cell green.
- The selected terminal does not finish the River Valley region.

## Delta summary

Coordinate which sites can supply other sites, then cover
distinct eligible layers in sequence. Each new patch both
approaches the coverage quota and feeds the same reserve that
pays for extending the restoration.

## New facts

- Turbines require rock and show used and available slots while
  a powered consumer is previewed.
- Clean soil and greenery are visibly distinct tile states.
- Confirming a final viable layout can exceed its greenery goal
  and open phase two without clearing every cell.

## Principles and design implications

Give each prerequisite a visible result. Display both fixed
cost and candidate returns before purchase. Let one placeable
converter support the next phase without making the paid step
itself equivalent to completing the objective.

## Puzzle or game generation potential

Use a small graph of rock, power and water placements over a
tile board with three ground states. Vary treatment and rotated
planting masks. Require a quota and sufficient reserve along a
certified route, with at least one legal but inefficient overlap.

## New genes

- ACT-932
- INF-648
- OBJ-375
- SYS-2005
- SYS-2006
- SYS-2007
- SYS-2008

## New combinations

None.

## Taxonomy changes

[Taxonomy Change 462](../../../research/taxonomy-changes/TAXONOMY_CHANGE_462.md).

## New questions

- At one fixed anchor, how do all supported rotations differ in
  predicted leaf return and in the number of qualifying tiles?
- How does elevation extend pump reach on two otherwise matched
  river segments?

## Next recommended game

Continue Selection 062 with LocoRoco 2, the English North
American PlayStation Portable UMD UCUS-98731. Follow an early
rolling route from tilt to separation or reunion and the stage result.

## Why this game

The first valley makes power, terrain eligibility, spatial
conversion and an invested restoration budget visible in one
bounded puzzle.
