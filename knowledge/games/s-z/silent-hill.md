---
game_id: GAME-0430
slug: silent-hill
game_title: Silent Hill
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-087
    - ACT-089
    - ACT-131
    - ACT-161
    - ACT-341
    - ACT-409
  system:
    - SYS-045
    - SYS-057
    - SYS-215
    - SYS-578
    - SYS-797
  constraint:
    - CON-282
    - CON-296
    - CON-442
  information:
    - INF-075
    - INF-115
    - INF-125
    - INF-128
    - INF-359
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Silent Hill — find the three-key school route

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Harry, Cheryl, Levin Street, the doghouse, school and three named keys are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: original North American English *Silent Hill* for PlayStation, released in 1999. The original Konami of America booklet defines controls and survival-information rules. A bounded early Old Silent Hill route is reconstructed from two written walkthroughs; exact disc revision, difficulty setting, installed hardware and direct play were not inspected. This is not *Silent Hill 2*, a later remake, or a modern port.
- Structured analysis target: `PLAT-PLAYSTATION` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: steer Harry through the fog-limited street; consult the acquired map and its red route annotations, inspect authored clues, listen to the carried radio's non-directional static, decide whether the flashlight's useful illumination warrants increased exposure, avoid or fight local monsters, find the House Key in the Levin Street doghouse, then gather the Lion, Woodman and Scarecrow keys, apply them to the matching locked house exit, and follow the resulting path to Midwich Elementary School.
- Entry: ordinary control after leaving Cafe 5 to 2 with the town map, radio and flashlight obtained, before following the first `To School` clue. Exact prior cafe combat is excluded.
- Positive terminal: the three-key doghouse-house gate has opened and Harry reaches and enters Midwich Elementary School. No school interior puzzle or route is admitted.
- Negative state: depletion of Harry's continuous health ends the attempt. Save and continue semantics are not part of the signature.
- Included: direct movement; contextual clue and fixture inspection; authored map annotations; typed key pickups and three-key gate; radio warning near monsters without exact bearing; fog-limited local sight; flashlight toggle and its effect on search/aim versus monster sight; autonomous enemies, optional close combat or avoidance, finite health and healing, and live time. A specific opponent count, compulsory kill or exact three-key collection order is not asserted.
- Excluded: cafe encounter, school interior, Otherworld, bosses, endings, explicit save-state persistence, optional pickups, exact damage and ammunition values, a claim that the guide route is the only route, modern controls, later editions, screenshots, video and audio evidence.
- Reproducible parameterisation: use the original PlayStation game and follow the written early route from the cafe's exit toward the alley's school clue, then the broken-road Doghouse note on Matheson Street. Return to Levin Street, inspect the doghouse more closely for the House Key, enter the house and inspect its three-key back door. Collect the three named keys from their mapped neighborhood locations, unlock the back-door continuation and approach the school. Current monster placement, fight/avoid choice, healing spend and elapsed time are not fixed by this analytical packet.
- Potential scoped modules: one school puzzle, an Otherworld transition, a boss or an ending need separate entry/terminal evidence.
- Direct-play status: no PlayStation console, disc, input trace, screenshot, video or audio was inspected. The original manual directly supports controls, map annotations, radio/flashlight tradeoffs and survival rules; two independent written guides corroborate the early route. The guide-derived terminal is a source-bounded reconstruction, not a witnessed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SH1-001` | The original booklet presents Harry's search for Cheryl in Silent Hill and explains direct movement, examination and the town map. | Confirmed | Direct | High | P1 |
| `SH1-002` | The acquired map records explored route details in red; life condition is visible and health depletion is fatal. | Confirmed | Direct | High | P1 |
| `SH1-003` | The flashlight helps searching and aiming in darkness but can expose Harry to monsters; disabling it reduces that exposure without making him invisible. | Confirmed | Direct | High | P1 |
| `SH1-004` | Carried radio static intensifies near monsters without giving an exact bearing, and monsters cannot hear the static. | Confirmed | Direct | High | P1 |
| `SH1-005` | The school-alley clue and Matheson Doghouse note lead to the House Key in the Levin Street doghouse; the house's locked back door then requires Lion, Woodman and Scarecrow keys before the school route. | Observation | Corroborated | Medium | S1, S2 |
| `SH1-006` | Knife, pipe and handgun offer different reachable attacks; handgun ammunition is limited and healing items recover life. | Confirmed | Direct | High | P1 |
| `SH1-007` | The early route can end analytically at arrival inside Midwich Elementary; the guides do not establish a unique solution or exact encounter schedule. | Observation | Corroborated | Medium | S1, S2 |

## Basic data

- Release / origin: Konami Computer Entertainment Tokyo / Konami of America, original 1999 PlayStation game.
- Platform or physical form: North American English PlayStation disc, one-player third-person survival-horror exploration; exact disc revision unverified.
- Mechanical families: inventory and fixture dependencies (`FAM-013`), tactical forecast and counterplay (`FAM-009`), real-time system pressure (`FAM-010`).
- Sources accessed 2026-09-27: **P1** — [original Konami of America PlayStation booklet](https://www.silenthillmemories.net/sh1/versions/silent_hill_ps1_us_manual.pdf), printed pp. 6–15 for premise, controls, map, life, equipment, flashlight and radio; **S1** — [written Old Silent Hill chapter route](https://www.silenthillmemories.net/sh1/walkthrough_01_old_silent_hill_en.htm), for the cafe, school clue, doghouse and three-key house; **S2** — [independent StrategyWiki Old Silent Hill route](https://strategywiki.org/wiki/Silent_Hill/Old_Silent_Hill), for the same neighborhood gate and school direction. Neither written route establishes an exact disc revision or mandatory combat sequence. S1 conflicts with P1 by saying monsters hear radio static; the original booklet explicitly says they cannot, so the primary manual governs this scope.

## Mechanical decomposition

### Action Genes

- Reused `ACT-008`: directly move Harry between the cafe, clue locations, three key sites and school entrance.
- Reused `ACT-087`: apply the matching collected keys to the locked back-door fixture.
- Reused `ACT-089`: take each addressed key and any relevant health or weapon item into inventory.
- Reused `ACT-131`: spend a carried healing item after damage, not as a mandatory route step.
- Reused `ACT-161`: aim and strike a reachable hostile with the selected knife, pipe or handgun when avoidance fails.
- Reused `ACT-341`: inspect written clues, map-relevant places and the doghouse-house fixture.
- Reused `ACT-409`: switch Harry's carried flashlight between on and off during embodied traversal.
- Claims: `SH1-001`, `SH1-003`, `SH1-005`, `SH1-006`.

### System Behaviour Genes

- Reused `SYS-045`: local monsters move independently while Harry navigates.
- Reused `SYS-057`: an eligible monster can orient or pursue on sight or sound, with flashlight exposure as a visibility modifier; the radio static itself is not an alert source.
- Reused `SYS-215`: movement, attacks and enemy contact settle under a live clock rather than turn alternation.
- Reused `SYS-578`: damage and recovery update one continuous life pool.
- Reused `SYS-797`: Harry's active flashlight changes local exposure and monster detection pressure, while off-state does not confer guaranteed invisibility.
- Resolution order: inspect map/clue → choose a route and light state → evaluate monster perception and optional contact → collect each eligible key → validate the three-key lock → continue to school.

### Constraint Genes

- Reused `CON-282`: the authored school-clue, doghouse-house gate and neighborhood key chain must be resolved before the school route is available.
- Reused `CON-296`: each of the three key identities must match the secured back-door gate; a generic held item is insufficient.
- Reused `CON-442`: examination, attack and door use require an actionable compatible position and current item state.
- The map-read/search and gun-aim penalty when the flashlight is off remains a parameter of the manual's light tradeoff, not a claimed finite-battery system. Claims: `SH1-003`, `SH1-005`.

### Information Genes

- Reused `INF-075`: the life display exposes whether damage and healing are urgent.
- Reused `INF-115`: fog and local sound expose only nearby opponent state, not an omniscient street map.
- Reused `INF-125`: the acquired map's explored red annotations and authored route hints support the current path choice.
- Reused `INF-128`: contextual examination and inventory identify the clue/key/fixture compatibility.
- Reused `INF-359`: the carried radio warns of an anonymous nearby monster without exact direction or identity. The manual expressly says that monsters cannot hear the static.
- Claims: `SH1-002`–`SH1-005`.

### Objective and Time Genes

- Reused `OBJ-026`: enter the designated school location after the route is traversable.
- Reused `TIM-003`: enemy movement and Harry's actions advance in real time.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Harry has the town map and reaches blocked Matheson Street | Inspect the Doghouse note, return to Levin Street and search the doghouse roof | The House Key becomes available for the front door without revealing every unseen threat | partial map information and authored clue chain | `SH1-002`, `SH1-005` |
| Radio static rises in the fog | Listen and change route or prepare an attack | A monster may be nearby, but no exact bearing or enemy identity is disclosed; static does not alert it | sensor information is distinct from monster perception | `SH1-004` |
| A dark passage needs visual search | Toggle flashlight on, inspect, then optionally switch off | Search/aim becomes easier while visual exposure may increase; off-state does not eliminate risk | reversible light-versus-stealth tradeoff | `SH1-003` |
| House back door is locked and one key is missing | Apply collected compatible keys | The continuation stays gated until all three named key requirements are met | key identity and ordered route gate | `SH1-005` |
| All three keys are available and the back-door continuation opens | Traverse toward and enter Midwich Elementary | The declared external route reaches its terminal; interior rules are excluded | bounded location objective | `SH1-005`, `SH1-007` |

## Strategic and experiential structure

- Local decision: use partial radio and fog signals to choose avoidance, light exposure or a finite-ammunition fight.
- Medium-term planning: inspect red map notes and gather three distinct keys without losing the route back to the house.
- Long-term structure: open the neighborhood gate and enter the school; no later story arc is folded into the packet.
- Failure attribution: life can be lost to active monsters; radio silence is not a guaranteed clear street, and turning off the flashlight is not invulnerability.
- Player-trust factor: the original booklet explicitly separates helpful light, hostile sight and a radio warning that enemies cannot hear.

## Replay and variation

The written routes give one reproducible early progression chain. Optional fights, healing and exact wandering path can vary; their numbers and timing were not measured.

## Adjacent systems and history

The 2024 *Silent Hill 2* remake also has anonymous radio warning and partial mapping, but it is a different game and scoped item chain. The original first game's three-key neighborhood gate and explicit flashlight/radio asymmetry define this packet.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-087`, `ACT-089`, `ACT-131`, `ACT-161`, `ACT-341`, `ACT-409` | Harry, keys, flashlight, optional combat/healing |
| System Behaviour | `SYS-045`, `SYS-057`, `SYS-215`, `SYS-578`, `SYS-797` | enemy perception and live health |
| Constraint | `CON-282`, `CON-296`, `CON-442` | clue chain, matching keys, compatible reach |
| Information | `INF-075`, `INF-115`, `INF-125`, `INF-128`, `INF-359` | life, fog, map notes, radio static |
| Objective | `OBJ-026` | enter Midwich Elementary |
| Time | `TIM-003` | live exploration and threats |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `429` (`GAME-0001`–`GAME-0429`).
- Exact genome matches: none.
- Tied near matches: `GAME-0330` — Silent Hill 2 (2024 remake) (`19 / 28 = 0.678571`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0330` *Silent Hill 2 (2024 remake)* | Shared radio, local threat, map, survival and key-chain boundaries. | Original first game uses a three-key doghouse-house gate and manual light/detection tradeoff; the remake packet centres an assembled juke-box and Wood Side Apartments. | Tied-near maximum, `0.678571`; not exact or a verified combination match. |

## Taxonomy impact

No new gene or combination is required. Existing `ACT-409`, `SYS-797`, `INF-359` and typed gate boundaries fit the primary manual's light, radio and key rules without broadening their definitions.

## Negative results

- `CON-601` rejected: the original booklet does not establish a finite flashlight battery/refill rule for this scope.
- `SYS-063` rejected: its key-consumption transition exceeds what the cited sources establish for these locks; `ACT-087` and `CON-296` cover verified application and matching without claiming when an item disappears.
- A directional tracker gene rejected: radio static does not locate or identify the monster.
- A radio-noise alert gene rejected: the booklet expressly states monsters cannot hear the static.
- The S1 guide's contrary radio sentence is rejected against the original manual; it is used only for route corroboration.
- No claim of direct play, exact disc revision, compulsory enemy kill, exact route duration or unique solution.

## Delta summary

Three matching keys gate an early school route while map notes, anonymous radio static and switchable light supply different kinds of partial information under live monster pressure.

## New facts

- [Confirmed | Direct | High] The original Konami booklet establishes the map, flashlight, radio and health asymmetry (`SH1-001`–`SH1-004`, `SH1-006`).
- [Observation | Corroborated | Medium] Two written routes align on the doghouse-house three-key path to Midwich Elementary (`SH1-005`, `SH1-007`).

## New genes

- [Observation | Corroborated | Medium] None; all twenty-two admitted boundaries are reused without changing prior signatures.

## New combinations

- [Observation | Direct | High] None created; verified combinations are tested against the complete signature.

## Taxonomy changes

- [Observation | Direct | High] None; no earlier game or registry boundary is revised.

## New questions

- On a pinned original disc, how do exact radio range and flashlight-on detection timing vary by monster type and difficulty?
- Does each collected key disappear from inventory immediately on its matching back-door interaction, or only after all three are applied?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0431` *Ori and the Blind Forest* only after this unit's validation, local commit and Goal stop window.
- Optimisation criterion: contrast fog-limited survival navigation against ability- and checkpoint-gated traversal.
- Backlog impact: no successor is started in this unit.

## Why this game

- [Hypothesis | Limited | Medium] An original PlayStation solo survival route tests whether existing map, radio, illumination and typed-gate genes cover a classic horror structure without inventing battery or enemy-alert rules.
