---
game_id: GAME-0541
slug: the-incident-at-galley-house
game_title: The Incident at Galley House
analysis_status: reviewed
reviewed: 2026-11-18
combination_ids: []
gene_ids:
  action:
    - ACT-030
    - ACT-738
  system:
    - SYS-1563
  constraint:
    - CON-814
  information:
    - INF-012
  objective: []
  time:
    - TIM-002
---

# Game: The Incident at Galley House

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The code syntax, three field types, participant numbering and first address
are scoped parameters.

## Analysis scope

- Version / ruleset: full English Windows Steam base game, app 3641000,
  launch-period July 2026 rules. Developer and walkthrough material
  identify the retail edition. The exact executable build of sampled
  states is unverified.
- Entry: in a fresh investigation, power the room, obtain and insert the
  operator's access card, complete automatic People calibration and obtain
  the manual page and to-do list. Start there, before the location codes
  used by the first lookup are registered.
- Primary decision loop: inspect the supplied documents for location codes
  and a scene address. Register locations on the Display, assemble the
  scene number, location and participant set on the machine, and use its
  separate lever to request the record. Consult the opened conversation
  and its written record.
- Exit: the first reconstructed Quail Lane conversation is complete and
  its transcript is available. Stop before retrieving another scene.
- Included: clue inspection, location registration and selector gating,
  mutable address fields, explicit submission, fixed echo and its
  discoverable transcript. Excluded: generator and authentication
  mechanics before entry, later identity assignment, hints, branching
  chronology, late-game mechanics, exact persistence and patch parity.
- Potential scoped module: using dialogue across several scenes to
  infer an unprinted participant set for another lookup.
- Direct-play status: no executable or save was opened. The evidence
  consists of release and creator documents, independent opening routes
  and static images of the first address and its result. No video or
  audio was played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| IGH-001 | The 14 July 2026 Steam release is the retail reimagining of Type Help and has a Windows build and an English interface. | Confirmed | Corroborated | High | P1, P2 |
| IGH-002 | With the operator authorised and People calibrated, the documents supply codes to enter on the Display. Registered locations become selectable on the machine. Quail Lane uses QU. | Observation | Corroborated | High | P2, S1, S2 |
| IGH-003 | The knob selects the scene number, the selector chooses a registered location and switches indicate a set of numbered participants. The lever submits the chosen address as a separate action. | Observation | Corroborated | High | P2, S1, S2 |
| IGH-004 | The first evidenced lookup is 01 at Quail Lane with people 1 and 11. The authored reconstruction shows the two people with a stranded car in the rain. The conversation can subsequently be consulted as a transcript. | Observation | Corroborated | High | P2, S1, S2 |
| IGH-005 | The clue and address composition are self-paced. The reconstructed dialogue plays as evidence rather than responding to the player's settings after it opens. | Observation | Corroborated | High | P2, S1, S2 |
| IGH-006 | One guide writes QA in its registration list but QU in its own scene address. The pictured manual page and configured machine independently transcribe QU, agreeing with the other guide. | Observation | Conflicting | High | S1, S2 |

## Basic data

- William Rous and Evil Trout Inc., 14 July 2026. Full English
  Windows Steam release, app 3641000.
- Families: hidden-state inference and knowledge and evidence progression.
- Sources accessed 2026-11-18:
  - **P1** — [publisher's Steam product record](https://store.steampowered.com/app/3641000/The_Incident_at_Galley_House/),
    for release, Windows, English interface and product identity.
  - **P2** — [developer's technical account](https://eviltrout.com/blog/2026-07-28-building-galley-house/),
    especially Controlling the Machine, Rendering the Machine and
    The Scene Tool. It distinguishes the finite address components
    from the browser predecessor's filename entry and shows the retail
    control layout.
  - **S1** — [VGTimes opening walkthrough](https://vgtimes.com/guides/161787-the-incident-at-galley-house-walkthrough-all-scene-codes.html),
    including the photographed manual, post-calibration machine set
    to the first address and the resulting Quail Lane conversation.
  - **S2** — [The Review Geek opening walkthrough](https://www.thereviewgeek.com/theincidentatgalleyhouse-part1walkthrough/),
    for the registration route, selector behaviour, retrieval and
    transcript. Its QA transcription is superseded for this record
    by the manual and machine images in S1.
- Claim IDs: IGH-001–IGH-006.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-030`: navigate to fixed evidence and inspect the manual
  and to-do list for codes and the meaning of their fields.
- Add `ACT-738`: assemble one typed archive address using separate
  finite controls and commit it with a separate lever. Participant
  switches pick a set; they do not assign identities or order speakers.
- Claim IDs: IGH-002, IGH-003.

### System Behaviour Genes

- Add `SYS-1563`: resolve a submitted composite address against one
  authored echo, with the successful retrieval making the fixed
  scene available for inspection. No evidence supports retrieving
  a list of partial matches. The exact display for each invalid or
  incomplete address was not verified.
- Claim IDs: IGH-003, IGH-004.

### Constraint Genes

- Add `CON-814`: a known location is not selectable at the lookup
  machine until registered by code at the separate Display.
- Claim IDs: IGH-002, IGH-003, IGH-006.

### Information Genes

- Reuse `INF-012`: an immutable indexed conversation supplies facts
  and remains consultable as a transcript after successful retrieval.
- Claim IDs: IGH-004, IGH-005.

### Objective Genes

- None. The first transcript is an observable research boundary,
  distinct from solving the whole investigation. No new objective
  gene is inferred merely from that boundary.
- Claim IDs: IGH-004.

### Time Genes

- Reuse `TIM-002`: the address and clues may be inspected and revised
  at the player's pace. Playback timing is part of evidence playback,
  not a timer on entering the address.
- Claim IDs: IGH-003, IGH-005.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| The operator and People display are calibrated | Read the photographed manual and the location instructions | The printed Quail Lane code and a complete first address can be read before opening the echo | A printed clue and an enabled selector entry are separate | IGH-002, IGH-006 |
| The player knows the initial codes | Register QU and the other evidenced initial locations at the Display | Quail Lane is offered on the machine's location selector | A location must be registered before it can be included in an address | IGH-002 |
| The machine offers Quail Lane | Set 01, select Quail Lane and enable only participant switches 1 and 11 | The machine displays the first composite address while awaiting lever submission | Changing an address field does not itself request an echo | IGH-003, IGH-004 |
| The first address is assembled | Pull the lever | The Quail Lane conversation plays, with participants 1 and 11 by the stranded car, and becomes available in the text record | Retrieval opens a fixed record with later inspection | IGH-004, IGH-005 |

## Strategic and experiential structure

The visible address lets the investigator compare the candidate against the
manual before committing it. Separate fields let the investigator isolate
which premise to revisit: which episode, where it took place and which
participants were present. The first address is given outright. Later
deductions require separate evidence and are outside this packet.

## Replay and variation

The first address and conversation are authored. The route uses the
same successful input from a fresh calibration. The exact minimum
number of registered locations, behaviour of malformed registrations,
duplicate retrieval rewards and persistence after restarting were not
reproduced.

## Adjacent systems and history

Type Help used finite archive filenames entered through a text interface.
The Steam adaptation uses a separate dial, selector, indexed switches
and lever. Her Story retrieves a set by matching search terms against
transcripts. Return of the Obra Dinn accesses memories through corpse
inspection. Here the player addresses an echo by composing its three
fields before seeing its contents.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-030`, `ACT-738` | Evidence inspection and multipart address composition |
| System Behaviour | `SYS-1563` | Authored echo retrieval |
| Constraint | `CON-814` | Separate location registration |
| Information | `INF-012` | Indexed immutable scene and written record |
| Objective | none | First transcript as the analysis endpoint |
| Time | `TIM-002` | Self-paced inspection and address editing |

Canonical signature:

`ACT-030,ACT-738; SYS-1563; CON-814; INF-012; -; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `540` (`GAME-0001`–`GAME-0540`).
- Exact genome matches: none.
- Tied near matches: `GAME-0023` — Return of the Obra Dinn (`3 / 13 = 0.230769`).
- Supported combination subsets: none.
- Scan date: 2026-11-18.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0023` — Return of the Obra Dinn | `ACT-030`, `INF-012`, `TIM-002` | Both let the player inspect stable indexed evidence at their own pace. Obra Dinn uses a corpse-linked location to enter the memory and a fate book for conclusions. Galley House composes an address at a machine and opens the indexed echo. | Near, `0.230769` |

### Preserved research notes

- New genes: `ACT-738`, `SYS-1563`, `CON-814`.
- Classification result: New gene.
- Evidence and reasoning: separate address composition, location eligibility
  and exact authored retrieval from discovery and later consultation.

## Taxonomy impact

- Registry changes: `ACT-738`, `SYS-1563`, `CON-814`.
- Taxonomy-change record: [TAXONOMY_CHANGE_288](../../../research/taxonomy-changes/TAXONOMY_CHANGE_288.md).
- Candidate terms affected: none.

## Negative results

- none.

## Delta summary

## New facts

- [Observation | Corroborated | High] The first echo uses three
  editable fields and a separate submission action. IGH-002–IGH-004.

## New genes

- [Observation | Corroborated | High] `ACT-738`, `SYS-1563`,
  `CON-814` distinguish address entry, resolution and the registration gate.

## New combinations

- [Observation | Corroborated | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_288`.

## New questions

- Will a wrong but fully expressible address always preserve the
  draft and return the same kind of feedback?

## Next recommended game

- [Hypothesis | Limited | Medium] Original Wii Excite Truck in
  [Selection 043](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_043.md).
- Optimisation criterion: diversify control, pacing and outcome evaluation.
- Expected information gain: separate tilt steering, placement and
  star-based performance inside one bounded race.
- Backlog impact: advance to `GAME-0542`.

## Why this game

- [Hypothesis | Limited | Medium] A controller-led, timed race should
  test boundaries that the frozen-record retrieval loop cannot.
