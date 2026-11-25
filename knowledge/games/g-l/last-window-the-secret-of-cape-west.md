---
game_id: GAME-0683
slug: last-window-the-secret-of-cape-west
game_title: "Last Window: The Secret of Cape West"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
    - ACT-905
  system:
    - SYS-1957
  constraint: []
  information:
    - INF-629
  objective:
    - OBJ-361
  time:
    - TIM-002
---

# Game: Last Window: The Secret of Cape West

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The first chapter's mailbox number, note page, dial marks and papers
are fixture parameters.

## Analysis scope

- Version / ruleset: original English Nintendo DS retail release
  distributed in Europe from September 17, 2010. The target uses Chapter 1,
  December 18, 1980, in the apartment lobby, after the exchange with
  Margaret Patrice. The English recordings show the DS game and the
  same fixture. Exact cartridges and playback hardware are unverified.
- Structured analysis target: PLAT-NINTENDO-DS in
  [platform coverage](../../platforms/games.json).
- Entry: regain lobby movement after Margaret tells Kyle Hyde about
  his full mailbox and leaves. Mailbox 202 is still closed.
- Primary decision loop: walk to the mailboxes, inspect the bank,
  pan the close view and identify the lower-left box marked 202.
  Touch its lock and consult the final notebook page for the ordered
  targets and directions. Translate the three instructions into
  actual dial travel, keeping the first two arrivals distinct.
  After the lock releases, inspect the papers that fall.
- Exit: Kyle has read the eviction notice and taken the useful
  information flyer. Its information view is accessible, the rest of
  the post has been gathered in the observed route, and the lobby
  becomes controllable again. Stop before the upstairs encounter.
- Included: local movement and inspection, box selection, reading
  the supplied notebook clue, dial input and release, and the separate
  reading and gathering actions on the loose papers.
- Excluded: the earlier interviews and consequences of pushing or
  ignoring a response, freehand notes, other dial uses, explicit tests
  of missed marks or wrong-direction recovery, room 202's separate
  door and letter, the later chapter quiz, and reboot persistence.
- Potential scoped module: compare object placement on the door
  frame with the mailbox's dial-controlled release.
- Direct-play status: no personal DS run or cartridge inspection.
  Nintendo establishes the regional release, touch layout and the
  reproduced mailbox sequence. W1 and W2 show the English fixture and
  resulting paper states. R1 corroborates the repeated turn, the
  reversal and how the flyer is retained. Only visual frames of the
  recordings were inspected in the background, with audio excluded.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| LW-001 | Nintendo of Europe dates the Nintendo DS retail release to September 17, 2010. The title is presented in book orientation and uses stylus interaction. | Confirmed | Direct | High | P1, P2 |
| LW-002 | After Margaret's departure, the player can move to the bank of mailboxes. An inspection pan exposes the left end of the bank. The lower-left door marked 202 opens its own view and touching the lock brings up a numbered dial. | Observation | Corroborated | High | P3, W1 17:50–18:20, W2 18:20–18:40, R1 |
| LW-003 | The authored final notebook page shows three targets with turn directions. The player's dial motion follows two counterclockwise arrivals at 7 and a clockwise arrival at 1. The second 7 requires leaving and returning to it in the first direction. | Observation | Corroborated | High | P3 clue image and steps, W1 18:20–18:40, R1 |
| LW-004 | The successful directed sequence releases the mailbox and spills its contents into a floor inspection. The papers are still present before individual selection. | Observation | Corroborated | High | P3, W1 18:40–19:30, W2 19:10–19:30, R1 |
| LW-005 | Touching the notice exposes its eviction text. Taking the flyer opens or adds its useful-information material. The inspected English route later returns to the playable lobby, where Kyle can move toward the stairs. | Observation | Corroborated | High | P3, W1 19:40–20:50, W2 19:30–20:30, R1 |

## Basic data

- Release / origin: Cing and Nintendo, European Nintendo DS retail,
  September 17, 2010. This record uses the English release.
- Mechanical families: FAM-012 for converting a recorded clue into
  accessible new information, and FAM-017 for the ordered dial trace
  followed by separately examining the newly accessible papers.
- P1: [Nintendo UK product and play description](https://www.nintendo.com/en-gb/Games/Nintendo-DS/Last-Window-The-Secret-of-Cape-West-271320.html).
  Identifies Nintendo DS and the book orientation and touch screen.
- P2: [Nintendo's European release announcement](https://www.nintendo.com/en-gb/News/2010/In-shops-now-Last-Window-The-Secret-of-Cape-West-252144.html).
  Confirms the original retail date and region.
- P3: [Nintendo Spain official Chapter 1 guide](https://www.guiasnintendo.com/0_NINTENDO_DS/last_window_cape_west/last_window_cape_west_sp/capitulo_01.html).
  The mailbox section and stills 004–007 show the left-side box,
  the dial, handwritten note and papers on the floor. Use it for
  the common fixture and verify the English presentation separately.
- W1: [NintendoComplete English capture](https://www.youtube.com/watch?v=-bcuo7UX7c4&t=1070s).
  The scoped sequence begins at about 17:50 with the
  lobby after Margaret, and resolves by 20:50.
- W2: [CJUGames English Chapter 1 capture](https://www.youtube.com/watch?v=yM9GplS8anI&t=1100s).
  Mailbox inspection is visible around 18:20, followed by the dial
  and paper reading in the next two minutes.
- R1: [Chibischala's English DS walkthrough](https://gamefaqs.gamespot.com/ds/979371-last-window-the-secret-of-cape-west/faqs/61024).
  Chapter 1 corroborates the same-mark repeat, reversal and flyer
  treatment. Its audio report was not used as a required signal.
- Claim IDs: LW-001–LW-005.

### Reproducible fixture evidence

1. Start in the lobby after Margaret's departure. Move to the
   boxes and open their inspection view. Pan the view, select
   the lower-left 202 door and then select its lock.
2. Before solving it, open the notebook and inspect page 6/6.
   The marks direct two left turns ending at 7 and a final right
   turn ending at 1. The arrows apply to the corresponding
   targets. Close the notebook to resume operating the dial.
3. Drag counterclockwise to align 7 at the reference mark.
   Continue in the same direction until 7 arrives there again.
   From that second arrival, turn clockwise until 1 aligns.
   Paper access follows the full sequence.
4. The floor view now contains several distinct mail pieces.
   Select the notice to read that the building will be cleared.
   Then select the separate flyer and
   verify the available information view. W1 shows the rest
   of the bundle being gathered during this part of the route.
5. Close the information view and regain lobby navigation.
   Stop before meeting the maintenance worker upstairs.

## Mechanical decomposition

### Action Genes

- ACT-008: move Kyle through the lobby to the mailbox bank. LW-002.
- ACT-341: select box 202, address its lock, then commit separate
  read and pickup interactions on the post. LW-002, LW-005.
- ACT-905: drag around the dial against its fixed reference mark,
  completing each turn with its instructed direction. LW-003.

### System Behaviour Genes

- SYS-1957: accept the ordered arrivals according to both their
  target marks and travel direction, including a repeat reached by
  another revolution. The complete trace releases the addressed
  mailbox and exposes the post. LW-003–LW-004.

### Constraint Genes

No distinct admission. The dependency between direction, selected
mark and sequence step is represented by SYS-1957.

### Information Genes

- INF-629: the notebook pairs a mark and a turn direction for each
  step. The close-up keeps the sequence readable while recalling
  the control. LW-003.

### Objective Genes

- OBJ-361: use the recorded sequence to release the post, read the
  identified notice, take the flyer and regain lobby navigation.
  LW-003–LW-005.

### Time Genes

- TIM-002: perform the dial steps and individually inspect the
  fallen papers at the player's pace. LW-003–LW-005.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Lobby freely navigable after Margaret | Approach, inspect and pan the mailbox bank | Box 202 identifiable at the left end | LW-002 |
| Box 202 in focus | Touch its lock | Numbered dial and notebook affordance | LW-002 |
| Dial visible, instructions unconsulted | Inspect the final notebook page | Three paired targets and directions readable | LW-003 |
| First 7 reached via leftward travel | Continue one leftward revolution to 7 | Second occurrence of 7 reached with its required turn | LW-003 |
| Second 7 reached | Turn right to 1 | Lock releases and papers become separately inspectable | LW-004 |
| Mail on the floor | Read the notice, then take the flyer | Eviction text and useful-information material exposed | LW-005 |
| Flyer inspection open | Close the information view | Ordinary lobby movement can resume | LW-005 |

## Strategic and experiential structure

The note specifies a motion sequence. The dial exposes only
where its current mark is, so returning to the same value can
use a distinct step. Opening the compartment creates another
choice of targets. Reading the relevant paper is the next
investigative action after getting mechanical access.

## Replay and variation

The common route is corroborated by both English recordings and
the publisher's walkthrough. The route does not establish the
precise gesture threshold or how the game recovers from any
incorrect arrival. The timings identify source frames and
are not fixture deadlines.

## Adjacent systems and history

The preceding Hotel Dusk title also generates a separate
inspectable clue from local object work. Its scoped puzzle
requires orienting and fitting picture pieces during an optional
help branch. The mailbox here depends on a recorded rotation
sequence and releases existing papers through a separate lock.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-341, ACT-905 | Move to the bank, address fixtures and papers, and drag the dial |
| System Behaviour | SYS-1957 | Convert ordered directed arrivals into mailbox release |
| Constraint | None | Represent the accepted movement sequence in its system rule |
| Information | INF-629 | Read the paired target marks and directions from the notebook |
| Objective | OBJ-361 | Release the post, read the notice, collect the flyer and resume navigation |
| Time | TIM-002 | Allow the sequence and inspections at the player's pace |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `682` (`GAME-0001`–`GAME-0682`).
- Exact genome matches: none.
- Tied near matches: `GAME-0654` — Hotel Dusk: Room 215 (`3 / 15 = 0.200000`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Hotel Dusk: Room 215 (GAME-0654)](hotel-dusk-room-215.md) | ACT-008, ACT-341, TIM-002 | Both move through a building, address a new physical clue and resume movement after the local task. Hotel Dusk grants the marked fragment after helping with a picture assembly. Last Window uses written directions and accumulated dial turns to expose pre-existing documents on the lobby floor. | Near, `0.200000` |

## Taxonomy impact

Four admissions describe directed dial input, its phase-sensitive
validation, the paired written instructions and the notice-and-flyer
outcome. The fixture reuses local navigation, contextual interaction
and self-paced sequencing without changing earlier definitions.

## Negative results

- Arriving at a marked value once does not complete its later
  repeated instruction.
- The terminal mark 1 is visible earlier in the dial interaction
  and is not sufficient on its own to release the mailbox.
- Opening the mailbox leaves the papers on the floor for later
  examination. It does not automatically read the eviction notice.
- The received post excludes the distinct letter later found against
  the apartment door frame.

## Delta summary

Seven genes, four new and three reused. The claim boundary runs
from the movable player in the lobby through the changed mailbox
and accessible notice back to the movable player in the same area.

## New facts

- The clue has corresponding directions and marks, including one
  repeated mark that needs a full additional revolution.
- The opened lock exposes multiple independent paper targets.
- The notice and flyer have separate information outcomes, after
  which movement in the same lobby resumes.

## Principles and design implications

If a physical control has meaningful travel between equal values,
give the player a clue that conveys direction and repetition.
When the lock is solved, leave the revealed evidence available
for its own readable interaction.

## Puzzle or game generation potential

An original investigation could use a written directional trace
to release a small hatch, then require recognition of a distinct
message among the articles that spilled from it.

## New genes

- ACT-905
- INF-629
- OBJ-361
- SYS-1957

## New combinations

None admitted. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[Taxonomy Change 429](../../../research/taxonomy-changes/TAXONOMY_CHANGE_429.md).

## New questions

- How does a partly entered sequence recover after the wrong turn?
- Is consulting the notebook itself ever tested as a progression flag?
- Can all unrelated post pieces be ignored before the required evidence?

## Next recommended game

Continue Selection 058 with `GAME-0684`, the commercial English
Windows Steam release of REANIMAL. Follow a partner-dependent
traversal puzzle in solo play into its next controllable space.

## Why this game

A clue describes the history of a physical input, and a successful
input exposes information behind the mechanism. The same place
remains navigable after the player inspects the result.
