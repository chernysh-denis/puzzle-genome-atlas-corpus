---
game_id: GAME-0624
slug: paradise-killer
game_title: "Paradise Killer"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-107
  system:
    - SYS-1825
  constraint: []
  information:
    - INF-179
    - INF-393
  objective:
    - OBJ-335
  time:
    - TIM-002
---

# Game: Paradise Killer

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The names of the actors, documents and time entries identify the observed case.

## Analysis scope

- Version / ruleset: English commercial PlayStation 5 edition of
  Paradise Killer, announced for March 16, 2022. The platform store
  offers the PS5 version. Capture region and exact patch are unverified.
- Primary decision loop: advance the Judge's locally addressed
  briefing, distinguish the comparison reference from what people say
  happened, then read the dated account delivered to Starlight. Leave
  the exchange able to choose the next inquiry in the still-open case.
- Entry: the first Courthouse exchange with Judge after arrival with
  Lydia, before questions about the suspect and transfer of case materials.
- Exit: the acquired Blood Sample notice, the visible Crime Details
  Received and dated entries, and return to ordinary Courthouse control.
  An independent PS5 screenshot corroborates separate Starlight tabs and
  the presence of the Henry Division case folder.
- Included: directed scene movement after the briefing, dialogue
  decisions and resulting information, acquisition of the reference,
  dated case intake, available case records and continuing investigation.
- Excluded: the exile prologue puzzle, ride with Lydia, optional
  pickups and relationships, later interviews, comparing the sample
  to a crime-scene trace, manually classifying other evidence, trials,
  verdicts, performance settings, other releases and final case truth.
- Suggested later scope: inspect an original scene trace against the
  registered reference and document the resulting comparison entry
  before any later accusation.

## Direct-play status

No direct play was performed. The developer's launch article and the
PlayStation Store identify the PS5 edition. The reference recording
starts from the PlayStation interface and the author identifies PS5.
A separate PS5 release review shows the actual Case Files categories
and Henry's folder. The older opening recording corroborates the
key-item notice without establishing PS5 parity independently. Only
text and static stills were used. Exact captured builds, button input,
sample consumption, storage across reload and later verdicts are unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PK-001 | The scope is the commercially released single-player PS5 edition with English text. The creator's launch announcement and UK store give March 16, 2022. | Confirmed | Corroborated | High | P1, P2, P3. The video does not authenticate an exact patch. |
| PK-002 | Lady Love Dies can advance the first Courthouse briefing and is offered authored dialogue choices on the suspect. Completion makes actionable material and an initial lead available. | Observation | Corroborated | High | W1 11:20–14:20; W2 12:30–15:00 corroborates the opening exchange. No particular optional answer is claimed to be required. |
| PK-003 | Judge says Starlight holds the Council records and has received Henry's sample. The dialogue log records Blood Sample Obtained as a key item. Getting it does not itself compare two samples or establish guilt. | Observation | Corroborated | High | W1 14:30–14:50; W2 16:40 separately shows the item acquisition card. |
| PK-004 | Starlight identifies the receipt of crime details and presents ordered entries. The visible first dated statement is Henry Division's 23:52 escape from the Desolation Cell. The 00:00 entry records the Council's murder. Reading these entries is distinct from examining the sample. | Observation | Corroborated | High | W1 15:20–15:40. R1 corroborates separate Timeline, Inventory and Case Files surfaces in the PS5 build without replaying that brief. |
| PK-005 | Starlight keeps navigable material under different views. The PS5 screenshot shows a Henry Division folder and a distinct crime folder, with Notes, Inventory and Timeline separate. | Observation | Direct | High | R1's Case Files image, P3 and P4. The screenshot is not from W1 and does not establish which folder automatically receives the sample. |
| PK-006 | The briefing returns control to the Courthouse. The player can continue investigating. The later choice screen explicitly offers continuation and warns that initiating trials commits a different phase. That later phase is outside the packet. | Observation | Corroborated | High | W1 16:00–16:10, 16:50 and 19:00; P4. Neither the later trial nor its verdict occurs in the analysed exchange. |

## Basic data

- Analysis target: `PLAT-PLAYSTATION-5`.
- Developer: Kaizen Game Works. Publisher: Fellow Traveller.
- Mechanical family: `FAM-012`, progress from authored evidence.
- Checked: 2026-11-21.
- P1: [PlayStation Store PS5 product](https://store.playstation.com/en-gb/product/EP5661-PPSA04459_00-5766379953570371).
- P2: [Kaizen's PlayStation launch article](https://blog.playstation.com/2022/03/04/paradise-killer-launches-on-ps4-ps5-march-16/).
- P3: [Kaizen title record](https://kaizengameworks.com/portfolio-items/paradise-killer/).
- P4: [Publisher's investigation overview](https://www.fellowtraveller.games/paradise-killer).
- W1: [ChronoCache's PS5 opening](https://www.youtube.com/watch?v=eUv0tqjVUcQ&t=870s).
  The sample update, received crime details, first timeline
  lines and return to control are visible at 14:30–16:10.
- W2: [AJBRUN's earlier opening](https://www.youtube.com/watch?v=DuZyZpKfTaU&t=1000s).
  This older recording visibly reports Blood Sample Obtained at
  16:40. It corroborates the handoff rule, not the target edition.
- R1: [GamePitt firsthand PS5 review](https://www.gamepitt.co.uk/paradise-killer-ps5-review/),
  [its Starlight still](https://www.gamepitt.co.uk/wp-content/uploads/2022/03/Paradise-Killer-8.jpg).
  The captured interface distinguishes five relevant tabs and
  explicitly displays the Henry Division folder.

## Mechanical decomposition

### Action Genes

- ACT-107: advance authored questions and answers to receive case facts.
- ACT-008: resume directing the investigator in the Courthouse.

### System Behaviour Genes

- SYS-1825: register a key reference and a dated case handoff as
  distinguishable records originating in one authorised briefing.

### Constraint Genes

No separate constraint is needed for the evidenced exchange. Progressive
dialogue does not establish a timed, item-gated or proof-gated response.

### Information Genes

- INF-179: the current Courthouse view exposes the person to address
  and the routes available after the exchange.
- INF-393: the assistant keeps case facts and named subjects visible
  in separate views. The chronological entry is not a verdict.

### Objective Genes

- OBJ-335: complete the authority's brief, receive the case material
  and return to ordinary investigative control with the case open.

### Time Genes

- TIM-002: advance the individual briefing beats at the player's pace.
  The dates being reported are incident times, not dialogue deadlines.

## Reproducible transitions

| State | Input or event | Result | Evidence |
| --- | --- | --- | --- |
| First Courthouse briefing | Advance the directed exchange about the suspect | Case context and authored questions become visible | PK-002 |
| Judge introduces the comparison material | Finish the relevant briefing exchange | Blood Sample Obtained appears in the log | PK-003 |
| Assistant receives the initial crime account | Continue the briefing | The receipt and dated items, including 23:52, are displayed | PK-004 |
| The briefing has ended | Resume directed scene movement | The investigator can pursue the next inquiry with the case open | PK-006 |
| Case information is available | Open the relevant assistant views | PS5 view distinguishes the suspect folder, case folder and Timeline | PK-005 |

## Strategic and experiential structure

The early handoff yields both an instrument for later comparison and
a provisional chronology supplied by an authority. Reading an entry
answers a question about what was reported. It leaves the player free
to investigate whether the report is sufficient and does not label
the case complete. The player need not assign each received statement
manually before leaving the briefing.

## Replay and variation

The main trace and the older trace show the same named sample
acquisition. Their dialogue pacing and nearby activities differ.
Only W1 establishes the target edition's dated display and return
in this route. R1 independently corroborates the recorded categories.
No exact save/reload boundary or version parity is claimed.

## Adjacent systems and history

Starlight can support later comparisons, recurring inquiries and
trial preparation. Those uses should be researched separately. The
developer documents enhancements for PS5. They do not imply that
effects, optional content or exact storage are identical on every
earlier edition.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-107 | Ordinary navigation and authored fact acquisition |
| System Behaviour | SYS-1825 | Distinct reference and chronology handoff |
| Constraint | None | The scoped briefing needs no separate constraint |
| Information | INF-179, INF-393 | Present scene and growing named case records |
| Objective | OBJ-335 | Finish the initial intake and resume inquiry |
| Time | TIM-002 | Self-paced briefing progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `623` (`GAME-0001`–`GAME-0623`).
- Exact genome matches: none.
- Tied near matches: `GAME-0523` — Pentiment (`4 / 20 = 0.200000`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Pentiment (GAME-0523)](pentiment.md) | ACT-008, ACT-107, INF-393, TIM-002 | Both navigate a local investigation, gain authored information through conversation and retain a case record. Pentiment spends limited work and meal periods on substantial leads and later reaches a scheduled verdict. The Paradise Killer packet accepts initial reference material and chronological entries, then leaves the timing and direction of further inquiry open. | Near, `0.200000` |

## Taxonomy impact

[TAXONOMY_CHANGE_370](../../../research/taxonomy-changes/TAXONOMY_CHANGE_370.md)
distinguishes case intake from ordinary follow-up conversation or adjudication.

## Negative results

- SYS-1280 covers unlocking a later subject or topic with a particular
  answer. This packet gives an acquired comparison reference and a dated
  incident record together under a single initial authority.
- SYS-680 derives an investigation result by inspecting eligible scene
  traces. No such comparison has been performed at the endpoint here.
- INF-391 serves a trial's admitted evidence and participant profiles.
  The open inquiry instead uses a case record before trial.
- OBJ-017 evaluates a completed structured reconstruction. OBJ-295
  requires an announced verdict. Neither can be inferred from the handoff.

## Delta summary

Admits one PS5 investigation opening through its visible evidence and
chronology transfer plus the resumed ordinary Courthouse control.

## New facts

- The same initial briefing delivers a comparison reference and
  a separate chronological record.
- The displayed 23:52 report can be recorded without comparing a sample.
- The transfer leaves the case open and restores ordinary navigation.

## New genes

SYS-1825 and OBJ-335.

## New combinations

None. No verified combination is a subset of the bounded briefing genome.

## Taxonomy changes

[TAXONOMY_CHANGE_370](../../../research/taxonomy-changes/TAXONOMY_CHANGE_370.md).

## New questions

Can a later complete comparison be traced from an independently examined
scene trace to a recorded difference, without relying on the eventual verdict?

## Next recommended game

Continue with the original North American Nintendo DS release of
Ninja Gaiden Dragon Sword and an evidenced first complete local encounter.

## Why this game

The bounded handoff distinguishes acquiring evidence and a reported
timeline from deriving the test result or deciding a case.
