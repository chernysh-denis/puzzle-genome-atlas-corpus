---
game_id: GAME-0629
slug: dark-cloud
game_title: "Dark Cloud"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-139
    - ACT-341
    - ACT-836
  system:
    - SYS-1830
    - SYS-1831
  constraint: []
  information:
    - INF-372
    - INF-584
  objective:
    - OBJ-338
  time: []
---

# Game: Dark Cloud

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: English North American PlayStation 2 commercial
  release, disc family SCUS-97111, 2001. The book and retail identifier
  refer to the original PS2 product. The worked recording is explicitly
  labelled US PS2. Its exact disc pressing and execution host are unknown.
- Primary decision loop: approach and open an Atla in the cave, retain its
  named part across the return to Norune, place an available house in
  the surface editor, ask a resident about an unknown requirement and
  insert the recovered part in the matching slot.
- Entry: on a fresh route, Toan is already under player control
  in floor 1 of Divine Beast Cave when he approaches the Atla that
  yields Wheel in the observed recording.
- Exit: in Norune, Paige's House has been placed on the map and reached
  on foot. The Wheel from floor 1 has moved from the loose stock into
  the identified house slot. The house remains on the map when leaving
  the assembly panel.
- Included: local walking and contextual opening, the named Atla grant,
  the separate exit item used at the first floor door, saved-in-run
  Georama stock, a freely positioned incomplete house, the question to
  Pike that identifies the wheel requirement, and mode-limited fitting.
- Excluded: the opening cinema, combat details on the intervening
  floors, backfloor treasure, weapon growth, map generation algorithm,
  death and save/reload rules, full satisfaction or completion of
  Norune, later towns, the sequel, Japanese and PAL rulesets and the
  later PSN edition.
- Suggested later scope: separately verify the resident requests and
  distinct completion percentages for one whole Norune layout.

## Direct-play status

No direct play was performed. Sony's original North American manual
identifies the input, mode and part rules. Static samples from an
explicitly US PS2 recording connect the same named part from floor 1
to the loose Georama stock and the installed wheel slot. Other
firsthand and official sources corroborate assembly and live movement
in the edited village. Audio was not sampled. No physical controller
trace, disc hash or exact state after death or reload was inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DCL-001 | The target is the English commercial North American PS2 title, SCUS-97111. Sony announced a late-May 2001 launch. The observed trace is attributed to the US PS2 ruleset. | Confirmed | Corroborated | High | P1, P2, R1 and W1. The exact pressing and execution hardware are unverified. |
| DCL-002 | Toan walks up to a reachable Atla. A context exclamation mark precedes opening with the Atlamillia, which releases a named Georama object. The worked floor 1 orb yields Wheel. | Observation | Corroborated | High | P1 printed pp. 6, 12–13. W1 28:50–28:59. |
| DCL-003 | Dran's Crest is selected separately at the floor 1 exit. The door opens and floor 2 begins. Georama parts persist through dungeon departures. The manual says opened Atla do not return on a revisit even when treasures and foes do. | Observation | Corroborated | High | P1 pp. 17, 33. W1 33:00–33:40, 44:10–46:20 and 1:46:33–1:46:45. |
| DCL-004 | A house is a separate foundation part. The recording obtains Paige's House on floor 2. The surface editor places that foundation while some required components are still missing. Placement offers position and rotation and changes the live Norune layout. | Observation | Corroborated | High | P1 pp. 35–36 and P2. W1 about 35:39–35:40 and 1:39:39–1:39:44. The day and site are from this recording. |
| DCL-005 | The placed house persists when leaving the editor and is accessible in Walking Mode. Pike can be addressed outside it and discloses the missing wheel requirement. Unknown slots become typed after the corresponding information is learned. | Observation | Corroborated | High | P1 pp. 14, 35–36. W1 1:45:50–1:46:26 and 1:46:33–1:46:36. |
| DCL-006 | The Walking Mode parts screen can be inspected, but rejects assembly. Config/Assembly accepts the loose wheel in the revealed slot. The item leaves the loose stock, the applied wheel is visible in that slot, and the house remains on the map. | Observation | Corroborated | High | P1 pp. 17, 35–36. W1 1:46:33–1:46:50, including the installed wheel at 1:46:45. |
| DCL-007 | Settlement position and orientation, completion of a building's parts, and fulfilment of resident requests are separately represented. The scoped placement does not prove full building or village completion. | Observation | Corroborated | High | P1 pp. 35–37. W1 1:39:39–1:39:44 and 1:46:45. |

## Basic data

- Analysis target: `PLAT-PLAYSTATION-2`.
- Developer: Level-5. Publisher: Sony Computer Entertainment America.
- Mechanical families: `FAM-013` for typed parts and `FAM-014` for the
  live settlement edited from another view.
- Checked: 2026-11-21.
- P1: [Original North American PS2 instruction booklet](https://www.videogamemanual.com/PS2/Dark%20Cloud%20%28USA%29.pdf),
  printed pp. 6, 12–14, 17, 33 and 35–37.
- P2: [Sony's 2001 PS2 announcement](https://sony.mediaroom.com/index.php?item=125695&s=2429),
  for the announced May 29 release, Georama authoring and immediate
  walking interaction. The relevant boundary is the 2001 commercial
  North American disc family rather than an exact retail-day claim.
- R1: [PS2 carrier and disc label](https://psxdatacenter.com/psx2/games2/SCUS-97111.html).
- W1: [Tsunao's recorded US PS2 playthrough](https://www.youtube.com/watch?v=tSJAYgOlBcQ&t=1733s),
  posted by World of Longplays. Follow the floor badge and the named
  pickup, placement and part slot in one continuous source.
- R2: [WTappendorf's contemporary PS2 play account](https://gamefaqs.gamespot.com/ps2/197042-dark-cloud/faqs/12543),
  for the Paige/Pike house, wheel, village controls and the difference
  between geographical preferences and fitting the required components.

## Mechanical decomposition

### Action Genes

- ACT-008: walk Toan to the sphere and later reach the resident.
- ACT-139: choose and place a recovered foundation at a compatible
  position in the village. The edit also permits moving it.
- ACT-341: activate a reachable Atla using the context cue. Use the
  separately obtained crest at the addressed floor exit.
- ACT-836: move the recovered wheel from loose stock into the named
  compatibility slot using Config/Assembly.

### System Behaviour Genes

- SYS-1830: open a one-time protective sphere to retain a named
  settlement component for later use in a separate surface system.
- SYS-1831: commit edit-mode structure placement and keep the same
  materialised geometry and resident access in walking mode.

### Constraint Genes

The local interaction affordance and compatible part slot are carried
by ACT-341 and ACT-836. No separate timing, urban-allocation or expiry
limit was established for the placement.

### Information Genes

- INF-372: the nearby exclamation mark indicates an eligible
  world interaction before opening or key use.
- INF-584: the part panel distinguishes foundations, loose parts,
  unknown versus known slots and placed state. A resident can disclose
  a missing slot's meaning.

### Objective Genes

- OBJ-338: recover a missing component from an exploration area and
  install it in a restored, reachable settlement building.

### Time Genes

No time gene is required. The observed causal chain is staged through
travel between locations and manual mode changes.

## Reproducible transitions

| State | Input or event | Result | Evidence |
| --- | --- | --- | --- |
| The accessible Atla on floor 1 is still closed | Walk Toan in range, then use the prompted opening action | The sphere opens and the game credits one Wheel to Georama | DCL-002 |
| The cave part is collected and the floor exit is closed | Select Dran's Crest on the addressed door and take the onward route | The exit opens. Floor 2 is reached and the part is retained | DCL-003 |
| Paige's foundation has also been acquired and the player has returned to Norune | Choose the foundation in Config/Assembly and commit its position and orientation | Paige's House is placed despite unresolved sockets | DCL-004 |
| Paige's House is placed with the wheel slot unresolved | Leave edit mode and ask Pike about the building | A live resident outside the house reveals the wheel requirement | DCL-005 |
| Wheel is loose and its matching socket is identified | Switch from the Walking parts view to Edit Mode and apply the wheel in Config/Assembly | The socket shows the installed Wheels entry, the loose item is spent from the list and the house remains on the map | DCL-006 |

## Strategic and experiential structure

The cave supplies identified parts rather than money for buying houses.
A named foundation and a compatible detail solve different steps. The
foundation can already occupy the map before every detail is known.
This lets a player reach its resident for information, then come back
to the edit panel to complete a fitting action. Choosing a site and
filling the wheel socket are distinct decisions. The record shows a
part becoming actual edited village state.

## Replay and variation

The recorded pickup has a floor badge and a title. Those observations
demonstrate this particular route rather than a guaranteed floor for
every Atla. The manual distinguishes repeatable floor enemies and
treasure from one-time spheres. The restoration proof relies on live
house position and slot state within the same playthrough. It does not
estimate a distribution of starting layouts or claim a reload outcome.

## Adjacent systems and history

Georama Analysis reports collection, completion and resident requests
as separate measures. Completing a house can generate a further event.
The Wheel fitting does not establish either a full village score or a
particular long-term reward. The sculpted settlement in the manual
illustrates the broad system rather than the layout of this attempt.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-139, ACT-341, ACT-836 | Reach the orb and resident, use a local affordance, place a foundation and fit a typed part |
| System Behaviour | SYS-1830, SYS-1831 | Transfer one-time dungeon content to editing stock and keep the changed place live outside the editor |
| Constraint | None | Context eligibility and matching slots are owned by the two relevant actions |
| Information | INF-372, INF-584 | Read the context mark and the unknown, known, loose and installed part states |
| Objective | OBJ-338 | Confirm cave-to-village restoration of the component |
| Time | None | No timing gate was needed in the scoped restoration |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `628` (`GAME-0001`–`GAME-0628`).
- Exact genome matches: none.
- Tied near matches: `GAME-0382` — Ōkami HD (`3 / 22 = 0.136364`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Ōkami HD (GAME-0382)](../m-r/okami-hd.md) | ACT-008, ACT-341, INF-372 | Both walk a character to context-marked objects. Ōkami HD reveals brush techniques and applies them to existing route features before uncursing Kamiki. Dark Cloud retains a named component from the cave, places a house in another view and fits that component to a resident-revealed slot. | Near, `0.136364` |

## Taxonomy impact

[TAXONOMY_CHANGE_375](../../../research/taxonomy-changes/TAXONOMY_CHANGE_375.md)
records the scoped recovery, assembly and edit-to-walk distinctions.

## Negative results

- ACT-139 is the ordinary footprint commit. It does not place a
  typed component in a named slot of an already-owned foundation.
- SYS-063 is collection and automatic consumption by contact with a
  carried-key barrier. The cave exit instead uses an explicit
  addressed inventory interaction. The recovered wheel is a different item.
- A compatible house slot need not be known on the first placement.
  Reading a menu of visible part requirements is distinct from a full
  assembly schema predicted before meeting the resident.
- A part grant alone does not recreate the village. Location, fitted
  state, resident requests and subsequent completion events are distinct.

## Delta summary

Adds one B1 Atla-to-Norune restoration packet with an actual retained
house and installed component in the original North American ruleset.

## New facts

- The floor 1 Atla credited Wheel, which survived travel to the surface.
- The recorded house can be placed with unresolved required parts.
- Pike discloses the wheel slot and the correct part is applied in Edit Mode.

## New genes

ACT-836, SYS-1830, SYS-1831, INF-584 and OBJ-338.

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_375](../../../research/taxonomy-changes/TAXONOMY_CHANGE_375.md).

## New questions

What amount of placement or fitting contributes to each separate
Georama Analysis percentage before the first village-completion event?

## Next recommended game

Continue with the Japanese commercial PlayStation Vita edition of
Gnosia, from the introductory role through the first verified loop result.

## Why this game

A dungeon pickup can become a usable change to the village only after
distinct placement, investigation and fitting decisions. The first wheel
gives a reproducible cross-mode chain with a tangible installed result.
