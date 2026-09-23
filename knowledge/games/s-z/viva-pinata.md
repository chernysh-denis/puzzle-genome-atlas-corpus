---
game_id: GAME-0375
slug: viva-pinata
game_title: Viva Piñata
analysis_status: reviewed
reviewed: 2026-09-23
combination_ids: []
gene_ids:
  action:
    - ACT-512
  system:
    - SYS-1021
  constraint:
    - CON-679
  information:
    - INF-382
  objective:
    - OBJ-217
  time:
    - TIM-003
---

# Game: Viva Piñata

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Species, garden
patch, the displayed condition list and the arrival interval are parameters,
not extra genes.

## Analysis scope

- Version / ruleset: original English 2006 Xbox 360 *Viva Piñata* garden
  rules in the contemporary Microsoft Game Studios booklet. Neither an Xbox
  360 disc nor an installed backwards-compatible release was inspected.
- Structured analysis target: one first-garden Whirlm residency transition;
  `GAME-0375` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: clear obstructing junk with Leafos's shovel, inspect
  the approaching Whirlm and its Condition Status, watch whether the wild
  piñata appears and visits, adjust the cleared garden according to the
  displayed residence conditions, and recognise the first
  black-and-white visitor's change into a coloured resident.
- Entry and exit: start a new original-game garden under a fresh profile with
  Leafos's introductory tutorial, initial junk, shovel access and no resident
  Whirlm. Record the profile, cleared patches and Whirlm Condition Status as
  it becomes inspectable. The positive terminal is one Whirlm's visible
  visitor-to-resident colour transition. Seeing it outside the garden or
  inside as a black-and-white visitor is insufficient. The first-grass reward
  may follow either the Whirlm's appearance or clearing the garden; that
  ordering is not forced into a single scripted path.
- Included: tutorial junk clearance; distinct appearance, visit and
  residence predicates; contextual Condition Status information; autonomous
  approach; first resident colour change. Leafos's grass reward is documented
  context, but grass sowing is not admitted to this genome because the
  booklet does not prove it necessary for the first Whirlm.
- Excluded: homes, two-piñata romance, eggs, visits from Sparrowmint or pond
  species, shops, selling and gifts, helper labour, illnesses, garden-wide
  level optimisation, later species, *Trouble in Paradise*, PC/DS variants,
  online features and any claim that a neglected resident remains forever.
- Potential scoped modules: species-specific food chains, habitat for pond
  species, house/romance/breeding or multigarden management need their own
  entry states and terminals.
- Direct-play status: none. The original booklet documents the mechanics, but
  no disc, save, executable hash, in-game Condition Status screenshot,
  controller trace, video or audio was inspected. Its general explanation
  does not print an exact numeric Whirlm condition threshold or an arrival
  timer; neither is asserted here. A replication must transcribe the actual
  displayed conditions rather than import unverified web tables.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `VP-001` | The opening tutorial gives a shovel to clear junk and mentions an approaching Whirlm. | Confirmed | Direct | High | Original Xbox 360 booklet pp. 8–9 |
| `VP-002` | Leafos awards a reusable instant grass-seed packet after either Whirlm appearance or garden clearance; it is sown on fertile ground. | Confirmed | Direct | High | Original Xbox 360 booklet pp. 8–9, 14–15 |
| `VP-003` | Each species has separate conditions for appearing, visiting and taking residence; suitable plants, neighbours, food or garden conditions may matter. | Confirmed | Direct | High | Original Xbox 360 booklet pp. 16–17 |
| `VP-004` | Highlighting a piñata and pressing Y exposes its information and Condition Status. | Confirmed | Direct | High | Original Xbox 360 booklet pp. 14, 16 |
| `VP-005` | A qualifying visitor becomes a coloured resident rather than remaining black and white; poor treatment can later lose residency. | Confirmed | Direct | High | Original Xbox 360 booklet pp. 16–17 |
| `VP-006` | The general booklet does not state a numeric Whirlm habitat threshold, exact first-visit delay or guaranteed order of the two grass-award triggers. | Observation | Limited | Medium | Original Xbox 360 booklet pp. 8–9, 16–17; bounded absence review |

## Basic data

- Release / origin: Rare / Microsoft Game Studios, original *Viva Piñata*,
  2006.
- Platform or physical form: English Xbox 360 original garden tutorial;
  backwards compatibility is a distribution option, not the analysed ruleset.
- Puzzle family: `FAM-017` ordered dependency sequencing. Garden edits make
  species appearance, visit and residence gates satisfiable in order;
  the animal is not placed directly like a zoo specimen.
- Primary source: [original Microsoft Game Studios Xbox 360 instruction
  booklet](https://www.videogamemanual.com/xbox360/Viva%20Pi%C3%B1ata.pdf),
  pp. 8–9 and 14–17. The booklet is a publisher-authored primary document
  preserved by a third-party manual archive.
- Product identity: [Microsoft's current original-game Xbox
  listing](https://www.xbox.com/en-us/games/store/Viva-Pinata/BSXSL6WBJ0V7).
  Its current platform availability does not replace the original rules.
- Secondary sources: no secondary numerical threshold is admitted to this
  packet.
- Claim IDs: `VP-001`–`VP-006`.

## Mechanical decomposition

### Action Genes

- Candidate gene: `ACT-512` removes garden junk. `ACT-213` plants/tends one
  crop, while digging genes target buried terrain rather than junk. Sowing
  grass is documented but not proven causally necessary for this first-Whirlm
  terminal, so it is excluded from the signature.
- Parameters: tool and obstructed patch.
- Claim IDs: `VP-001`, `VP-002`, `VP-006`.

### System Behaviour Genes

- Candidate gene: `SYS-1021` evaluates staged species conditions and changes
  an individual wild visitor into a coloured resident when qualified. It
  does not guarantee a fixed arrival tick.
- Resolution order: clear ground; the Whirlm may appear; inspect conditions;
  satisfy any outstanding residence
  gate; observe a valid visit and the individual's colour transition.
- Claim IDs: `VP-001`–`VP-006`.

### Constraint Genes

- Candidate gene: `CON-679` separates appearance, visit and residence gates;
  merely meeting the earlier one cannot skip a later one. A universal Whirlm
  area threshold is not assumed.
- Claim IDs: `VP-003`, `VP-006`.

### Information Genes

- Candidate gene: `INF-382` for the highlighted species' Condition Status;
  `INF-168` is a resident motive/action panel, not a species gate list.
- Claim IDs: `VP-004`, `VP-006`.

### Objective Genes

- Candidate gene: `OBJ-217` ends at one visibly coloured resident Whirlm.
  It is not the later house, pair or egg objective.
- Claim IDs: `VP-003`, `VP-005`.

### Time Genes

- Existing gene ID: `TIM-003`; the visitor can approach and move while the
  player inspects and edits a living garden. No exact clock delay is claimed.
- Claim IDs: `VP-001`, `VP-003`, `VP-006`.

## Reproducible transitions

| Before | Action | Rule-bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| New garden contains tutorial junk | Use the shovel on a chosen obstructing piece until cleared | That patch becomes usable garden ground; chocolate coins may be exposed | The gardener changes the habitat rather than merely waiting | `VP-001` |
| Whirlm appears near the boundary | Highlight it and press Y, then open Condition Status | The game presents the species' current staged requirements | Appearance is not proof of residence | `VP-003`, `VP-004` |
| Whirlm is inside as a black-and-white visitor | Compare displayed residence conditions with garden state; make the documented needed edit | If the species' residence gates are satisfied, that individual qualifies | A visit alone cannot satisfy the positive terminal | `VP-003`, `VP-004` |
| A qualifying Whirlm remains in the garden | Observe its visible colour transition | One resident is established | The colour change, not later housing, marks this packet's terminal | `VP-005` |
| A resident is later mistreated | Continue without adequate care | It may cease to stay | First residency does not imply permanent retention | `VP-005` |

For direct replication, record original edition/build, new-profile state,
cleared junk and exposed soil, packet award trigger, highlighted Whirlm
Condition Status before and after edits, appearance/visit times
and the exact frame of colour change. This packet is a source-grounded
protocol, not a falsely recorded playthrough.

## Strategic and experiential structure

- Local decision: remove a blocking object or sow a specific fertile patch
  after reading the current condition panel.
- Medium-term planning: work backwards from the target species' displayed
  residence gate through visit and appearance conditions.
- Long-term structure: a first resident can enable other species, but this
  packet stops before that downstream chain.
- Failure attribution: a monochrome visitor signals that residency is not
  yet achieved; Condition Status directs the next investigation.
- Player-trust factors: the explicit conditions and strong black-and-white to
  colour transition distinguish incomplete from complete progress.
- Claim IDs: `VP-003`–`VP-006`.

## Replay and variation

- What changes between sessions: cleared junk, exposed ground and species
  condition satisfaction.
- Randomness: the booklet gives no exact Whirlm arrival schedule; the packet
  does not infer one from one future observation.
- Multiple viable strategies: the grass award may follow either appearance
  or clearance, but its later sowing is not presumed necessary for Whirlm.
- Typical replay motive: verify a different initial garden edit sequence or
  later pursue another species, which would be a separate packet.
- Claim IDs: `VP-001`–`VP-006`.

## Adjacent systems and history

- Variants: *Trouble in Paradise* is a different ruleset, not silently mixed
  with the 2006 original.
- Similar games: the complete lower-ID signature comparison is owned below.
- Important differences: the gardener changes habitat so autonomous wildlife
  qualifies; it does not purchase and assign a stored animal to an enclosure.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-512` | Junk, shovel and cleared ground |
| System Behaviour | `SYS-1021` | Species and staged transition |
| Constraint | `CON-679` | Appearance, visit and residence predicates |
| Information | `INF-382` | Highlighted condition panel |
| Objective | `OBJ-217` | One coloured resident |
| Time | `TIM-003` | Autonomous visitor timing |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `374` (`GAME-0001`–`GAME-0374`).
- Exact genome matches: none.
- Tied near matches: `GAME-0116` — The Stanley Parable: Ultra Deluxe (`1 / 11 = 0.090909`); `GAME-0302` — Captain Toad: Treasure Tracker (`1 / 11 = 0.090909`).
- Supported combination subsets: none.
- Scan date: 2026-09-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0116` The Stanley Parable: Ultra Deluxe | `TIM-003` | Both worlds continue while the player acts, but Stanley's authored narrated branch is chosen by traversal. Viva Piñata edits a garden to qualify one autonomous visitor for residence; it shares no branch, condition-panel or resident objective. | Tied near, score 0.090909 |
| `GAME-0302` Captain Toad: Treasure Tracker | `TIM-003` | Both have a live world, but Captain Toad navigates a no-jump diorama toward a Power Star. Viva Piñata clears habitat to advance an independent visitor through species gates; grass sowing is not presumed necessary. | Tied near, score 0.090909 |

### Preserved research notes

- New genes: `ACT-512`, `SYS-1021`, `CON-679`, `INF-382`, `OBJ-217`.
- Classification result: New gene.
- Evidence and reasoning: the booklet's explicit attraction stages and
  colour-change terminal are not explained by existing zoo, crop or wildlife
  capture boundaries.

## Taxonomy impact

- Registry changes: add five bounded genes; no earlier signature changes.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_114`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_114.md).
- Candidate terms affected: junk, grass, visitor, Condition Status and
  resident are operational boundaries, not a generic garden genre tag.

## Negative results

- No existing verified combination is presumed supported merely by the
  garden theme. The generated proper-subset scan decides support.

## Delta summary

The headings below list only new corpus changes. Reviewed Ukrainian research
views are generated from the separate locale layer.

## New facts

- [Confirmed | Direct | High] The original tutorial Whirlm is a candidate
  for a staged appearance/visit/residence path, not instantly resident on
  sight (`VP-001`, `VP-003`, `VP-005`).

## New genes

- [Confirmed | Direct | High] Five new genes separate habitat editing, staged
  residency, requirement disclosure and the first-resident terminal.

## New combinations

- [Observation | Direct | High] No combination is added for this packet.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_114` adds five definitions
  without changing earlier game signatures.

## New questions

- Direct play should transcribe the original Whirlm Condition Status and
  measure its numeric thresholds and visit delay; neither is resolved by the
  general booklet.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0376` Katamari Damacy REROLL, the
  next selected genre-contrast unit.
- Optimisation criterion: alternate habitat qualification with rolling
  scale growth and object collection.
- Expected information gain: distinguish size-gated object adhesion from
  garden-condition residency.
- Backlog impact: no predecessor signature is revised.

## Why this game

- [Hypothesis | Limited | Medium] Viva Piñata tests whether habitat edits
  make autonomous wildlife a resident through inspectable staged conditions,
  rather than direct capture or purchase.
