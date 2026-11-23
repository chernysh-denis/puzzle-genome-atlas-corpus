---
game_id: GAME-0597
slug: duck-detective-the-ghost-of-glamping
game_title: "Duck Detective: The Ghost of Glamping"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-030
    - ACT-060
    - ACT-341
  system:
    - SYS-086
    - SYS-1559
    - SYS-1758
  constraint:
    - CON-093
  information:
    - INF-024
    - INF-179
  objective:
    - OBJ-017
  time:
    - TIM-002
---

# Game: Duck Detective: The Ghost of Glamping

Use the [canonical vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
An inspected detail supplies a word. A name pair identifies a subject.
A separate five-slot proposition settles why the two people are leaving.

## Analysis scope

- Version / ruleset: American-English North American Nintendo Switch
  digital base game by Happy Broccoli Games, released May 22, 2025.
  Ordinary solo Sleuth Mode, opening apartment deduction Holiday.
  Nintendo's listing identifies the original Switch edition. The
  installed software revision, save fields and exact control timings
  were not verified.
- Structured analysis target: `PLAT-NINTENDO-SWITCH` in
  [platform coverage](../../platforms/games.json).
- Entry: on a fresh Sleuth route, finish the bedroom's Old Flame
  deduction and its conversation. Start the bounded packet with
  Holiday active as you leave the bedroom for the shared living
  room. Old Flame supplies the prerequisite and Frederson; the
  Duck Detective token persists from the previous bedroom evidence.
- Primary decision loop: move to a lead, focus on a detail within its
  magnified view, take the resulting clue into the notebook and
  decide which role it fits. Check the crocodile's two-part name
  separately. Then use the five blanks to test the organiser,
  guest, activity, description and destination. Replace an
  unsupported clue or return to its source.
- Positive exit: Holiday receives its acceptance stamp; continue
  the exchange with Freddy and reach the bus stop at Sunny Lakeside
  Campsite. Stop at first control there, before inspecting a notice
  or taking the next case objective.
- Negative exit: an unfinished or wrong statement does not settle
  Holiday or start the trip. Sleuth Mode withholds per-slot wrong
  highlights. The draft can be revised and previously inspected
  evidence remains available. No time limit or lost-clue penalty
  is imposed during the investigation. A controlled wrong Holiday
  submission and exact feedback string for this Switch build were
  not directly observed.
- Included: local movement and inspection, the shared-room sources,
  carried clue terms, magnified hotspot selection, finite typed
  words, a separate two-name subject record, automatic complete-page
  validation, the confirmed Holiday and travel handoff.
- Excluded: solving the bedroom tutorial as a second unit, a
  collected-word minimum apart from the demonstrated complete
  route, whether assigning the name is independently mandatory to
  submit Holiday, exact rejection-count bands, changing difficulty,
  hints, optional achievements and repeated quacks, all later
  campsite deductions, other platforms and the earlier game.
- Potential scoped modules: first campsite dossier round with
  interrogations, adding documents to the case file and several
  distinct identities before a new event statement.
- Direct-play status: no console, executable, native controller
  trace or audio playback. Two independent captures identified as
  Switch were inspected as still images. A third same-version-family
  trace corroborates the stamp. Nintendo and a contemporary Switch
  reviewer establish the carrier, inspection and mode distinction.
  Written routes corroborate exact evidence and accepted roles.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DG-001 | The US English Nintendo Switch digital base game was released May 22, 2025 and is a stand-alone single-player mystery. The developer describes evidence inspection and filling structured blanks. | Confirmed | Direct | High | P1, P2 |
| DG-002 | Holiday follows Old Flame and spans the apartment until the first Sunny Lakeside arrival. Frederson is available on that transition; the detective's self-name token carries over. Entering the shared room exposes new leads including unrelated travel possibilities. | Observation | Corroborated | High | W1 6:50–9:30, W2 10:50–13:30, R1, R2 |
| DG-003 | The left conversation detail on the laptop supplies Freddy; its video-description area supplies Spooky and Sanatorium. The grouped wall photos include the camping flyer, which supplies Glamping and Tranquil. In the close-up, focusing and selecting eligible areas records authored words, rather than requiring the player to type the description. | Observation | Corroborated | High | W1 10:10–12:00, W2 13:30–16:10, R1, R2 |
| DG-004 | Investigating the crocodile reveals a portrait and observable traits. The notebook's Suspects tab asks for distinct first and last name fields. The Switch footage shows Freddy entered before Frederson completes the name. | Observation | Corroborated | High | W1 9:40–11:20, W2 14:20–15:10 and 18:50–19:30, R1 |
| DG-005 | Freddy Frederson appears as the confirmed name on the same suspect record before the Holiday page is accepted. Completing the name fields and solving the travel proposition are separate state changes. It is unverified whether the former is a hard prerequisite for submission of the latter. | Observation | Corroborated | High | W2 15:00–15:20, 19:40–20:30; R1, R2 |
| DG-006 | Holiday has five structured blanks and uses collected tokens as choices. The placed actors are Freddy and The Duck Detective, the activity is Glamping, and the destination is qualified by Spooky and specified as Sanatorium. A nearby sourced descriptor, Tranquil, is evidence but does not satisfy the destination description. | Observation | Corroborated | High | W1 12:20–12:50, W2 19:40–20:20, W3 10:50–11:00, R1, R2 |
| DG-007 | Placing the complete accepted statement yields a stamp and a marked settled page in the observed route. After the acceptance the apartment conversation leads to the bus-stop scene. Inspecting a clue or confirming the crocodile alone does not show this handoff. | Observation | Corroborated | High | W1 12:40–14:00, W2 20:00–21:40, W3 11:00–12:30 |
| DG-008 | The Switch mode selector and first-hand Switch review say Sleuth does not highlight wrong individual answers, while Story does. The Windows release account reports aggregate error feedback in Sleuth. Exact wrong-attempt wording or timing for Holiday on Switch is not asserted. | Observation | Corroborated | Medium | W2 6:20, R3, R4 |

## Basic data

- P1: [Nintendo of America's digital product](https://www.nintendo.com/us/store/products/duck-detective-the-ghost-of-glamping-switch/).
  Date, US English, Nintendo Switch, ordinary single player and
  explicit stand-alone sequel status.
- P2: [Happy Broccoli Games](https://www.happybroccoligames.com/).
  Studio's Ghost of Glamping entry identifies inspecting evidence
  and making deductions about the luxury campsite.
- `FAM-002`: infer the trip and identity from separate observations.
  `FAM-012`: evidence collection and the accepted notebook statement
  advance the story through the next location.

### Reproducible route evidence

- W1: [Nintendo Dads' opening on Switch](https://www.youtube.com/watch?v=8HvI3-h5sUQ&t=520s),
  published May 23, 2025. Silent stills show the reusable bedroom
  words, room entry, close-ups, dropdown, accepted transition and
  first campsite control. The handoff is visible near 12:50–14:00.
- W2: [Seth Sturgill's Switch release-window route](https://www.youtube.com/watch?v=v0AR6y6aQeE&t=730s).
  The description discloses a Switch review copy. Static frames
  show the Sleuth selection at about 6:20, the name split by
  15:10, the Holiday slots near 19:40 and the travel handoff at
  about 21:10–21:40.
- W3: [Shmoo Gaming's independently labelled Switch sequence](https://www.youtube.com/watch?v=jxia2ReICZY&t=630s).
  A still near 11:00 contains the completed page with its stamp;
  the bus scene follows. Exact build number is not legible in
  the sampled material.
- R1: [Rahul Shirke's opening route and evidence list](https://intoindiegames.com/walkthrough-hub/duck-detective-the-ghost-of-glamping-walkthrough-solutions-guide/).
  Separately identifies the laptop chat and video, flyer, name
  fields and Holiday answer. Its date precedes the public release;
  use details corroborated by the released Switch captures.
- R2: [The Walkthrough King's apartment route](https://www.walkthroughking.com/text/duckdetectivegg.aspx).
  Corroborates clue vocabulary, name and travel resolution. The
  guide's Steam keys and achievement notes do not establish Switch
  controls or runtime parity.
- R3: [Switch It On Gaming's launch-day hands-on review](https://switchitongaming.com/2025/05/22/duck-detective-the-ghost-of-glamping-nintendo-switch-review/).
  Distinguishes the two modes and close-up collection from ordinary
  navigation and dialogue.
- R4: [Erin McAllister's Windows hands-on review](https://www.gamegrin.com/reviews/duck-detective-the-ghost-of-glamping-review/?os=36).
  External corroboration of coarse wrong-answer feedback only.
  No precise platform parity is inferred.

## Mechanical decomposition

### Action Genes

- ACT-008 moves Eugene between reachable room objects. ACT-341
  opens an available clue or starts dialogue at the relevant entity,
  including the post-deduction conversation (DG-002, DG-003, DG-007).
- ACT-030 applies inside a close-up to moving the inspection focus
  among fixed details of the currently shown source (DG-003, DG-004).
- ACT-060 fills and revises typed name and story blanks using
  collected words (DG-004, DG-006).

### System Behaviour Genes

- SYS-1559 records authored terms upon eligible detail inspection.
  One video-description hotspot supplies two words. There is no
  separate operation to click each resulting word (DG-003).
- SYS-1758 confirms the crocodile's matching first name and surname
  on a separate roster record (DG-004, DG-005).
- SYS-086 checks a complete case statement. The ordinary Sleuth
  interface does not mark each wrong slot; acceptance seals the
  correct statement and releases the story handoff (DG-006–DG-008).

### Constraint Genes

- CON-093 restricts each role to a finite contextual phrase pool,
  with separate selectors for names, activity, description and
  destination. Acquiring a word does not make it correct (DG-006).

### Information Genes

- INF-179 exposes the current room, the crocodile, the laptop and
  grouped departure evidence as reachable actors and objects.
- INF-024 shows the retained clue vocabulary alongside a scaffold.
  Observed colour-coding and slot pickers distinguish roles without
  guaranteeing the chosen word is right (DG-003, DG-004, DG-006).

### Objective Genes

- OBJ-017 requires the exact accepted Holiday account. The identity
  and evidence inventory alone do not settle this objective (DG-005–DG-007).

### Time Genes

- TIM-002 allows room search and notebook changes in self-paced
  order. No elapsed-time criterion determines acceptance (DG-002–DG-008).

## Reproducible transitions

| Initial state | Intervention | Discriminating result | Evidence |
| --- | --- | --- | --- |
| Old Flame resolved, bedroom exit available | Leave for the shared living room with Holiday active | The new shared-room sources can be approached. Frederson and the detective's own name remain available | DG-002 |
| At the reachable laptop | Open the close-up and inspect the chat detail and video-description region | Freddy becomes available. A separate hotspot yields the descriptor and destination terms together | DG-003 |
| At the framed photos and flyer | Move the lens to the flyer and inspect it | Glamping enters the available vocabulary along with a plausible alternative descriptor. These are evidence terms, not a settled conclusion | DG-003, DG-006 |
| Crocodile's portrait available and two name words known | Select Freddy and Frederson in order in his Suspects card | The portrait is now named while the Holiday proposition is still open | DG-004, DG-005 |
| Holiday active and words available | Inspect a slot picker and leave at least one of the five blanks unfilled | Different roles use different subsets of the word pool. The stills show the unfinished statement remains open | DG-006 |
| Complete statement would use an unsupported descriptor such as Tranquil | Compare it to the laptop wording and revise the description to Spooky | The accepted assignment requires the supported descriptor. Sleuth mode is not a per-slot error highlighter. This contrast is the documented rule, not a recorded deliberate wrong submission | DG-006, DG-008 |
| Accepted actors, activity, description and destination fill all five blanks | Return to the conversation and continue to the trip | The stamp is shown and the story reaches Sunny Lakeside's bus stop. Stop before inspecting campsite evidence | DG-007 |

## Strategic and experiential structure

There is no value in choosing a word simply because it sounds plausible
or belongs to the right role. The same camping evidence yields relevant
and misleading language. Reading the chat and video separately also
prevents the name and destination tasks from collapsing into one guess.
The route retains enough evidence to revise the hypothesis without
starting a new visit or sacrificing a limited action supply.

## Replay and variation

A reproducible run logs the game edition, mode, room entry, provenance
of each term, identity slots before and after, five proposition values,
stamp state and first campsite location. The captures include sightings
of distractors and partially filled pages, but not a matched controlled
wrong submission in Holiday. The minimum discovery count that still
permits acceptance and the relationship between optional name assignment
and page submission warrant separate testing.

## Adjacent systems and history

The succeeding campsite adds different people, interrogations and
documents. The scope ends before them. The eShop describes this title
as a standalone sequel to The Secret Salami. No Switch 2, later
physical cartridge or desktop rule variation is inferred.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-030, ACT-060, ACT-341 | Approach, inspect, assign and interact |
| System Behaviour | SYS-086, SYS-1559, SYS-1758 | Validate a page, record words and confirm a two-part identity |
| Constraint | CON-093 | Use collected compatible terms |
| Information | INF-024, INF-179 | Notebook choices and local leads |
| Objective | OBJ-017 | Settle the authored Holiday account |
| Time | TIM-002 | Untimed exploration and revision |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `596` (`GAME-0001`–`GAME-0596`).
- Exact genome matches: none.
- Tied near matches: `GAME-0538` — The Rise of the Golden Idol (`8 / 16 = 0.500000`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| GAME-0538 The Rise of the Golden Idol | ACT-030, ACT-060, CON-093, INF-024, OBJ-017, SYS-086, SYS-1559, TIM-002 | Both turn inspected details into a finite word bank and check complete, typed propositions. Constriction freezes a witnessed scene and separates Names and Events panels; Holiday moves through the current apartment, binds names to an inspected subject and opens a new location after settling the trip. | 8 shared of 16; Jaccard 0.500000 |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_343](../../../research/taxonomy-changes/TAXONOMY_CHANGE_343.md)
  adds one name-confirmation rule. Earlier signatures remain intact.

## Negative results

- CON-064 is outside this scope. The whole apartment is a traversable
  current setting with characters and conversation, rather than a
  preserved event represented as an immutable tableau.
- ACT-059 is outside this scope. Selecting the clue hotspot acquires
  its authored words directly instead of separately copying each
  highlighted token from the opened detail.
- A complete word list, the portrait alone and the identity confirmation
  are distinct from the accepted story statement.

## Delta summary

## New facts

- [Observation | Corroborated | High] Eligible evidence selection
  populates a finite vocabulary for distinct name and narrative slots.
  The first trip concludes when the separate authored page is accepted.

## New genes

- [Observation | Corroborated | High] SYS-1758 binds separately
  discovered first-name and surname tokens to an inspected subject.

## New combinations

- [Observation | Corroborated | High] No new combination is proposed.

## Taxonomy changes

- [Observation | Corroborated | High] Added one bounded definition.
  Keep existing evidence collection, assignment and evaluation rules.

## New questions

- Could an exact Holiday submission advance immediately if the profile
  goes unnamed? Observe controlled Switch attempts with an intentionally
  wrong collected term and with some distracting clues left uninspected.

## Next recommended game

- [Hypothesis | Limited | Medium] Sega Bass Fishing on the original
  North American Dreamcast disc. Check the full loop from a legal lure
  cast to a graded catch or attempt boundary.

## Why this game

- [Hypothesis | Limited | Medium] A small, untimed inference separates
  acquiring vocabulary, binding identity and accepting a proposition.
