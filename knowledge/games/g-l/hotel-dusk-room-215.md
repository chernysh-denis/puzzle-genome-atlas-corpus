---
game_id: GAME-0654
slug: hotel-dusk-room-215
game_title: "Hotel Dusk: Room 215"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-070
    - ACT-232
    - ACT-341
    - ACT-866
  system:
    - SYS-1888
  constraint:
    - CON-875
  information:
    - INF-148
    - INF-606
  objective:
    - OBJ-349
  time:
    - TIM-002
---

# Game: Hotel Dusk: Room 215

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: the English mode of the original commercial European
  Nintendo DS Game Card, released 13 April 2007. The European carrier is
  catalogued as NTR-AWIP-EUR. The primary recording is attributed to the
  European game. Exact cartridge bytes, revision and physical device were
  not verified.
- Entry: Chapter 1, during the 17:00–17:30 block. Check-in is already
  complete. Guide Kyle to the stairs at the end of the central hallway and
  enter the encounter with the girl sitting there.
- Primary decision loop: use a contextual follow-up in the conversation to
  reach the offer to work on the puzzle. Select, rotate and place the five
  loose jigsaw pieces. Advance the ensuing exchange until the girl leaves,
  then take and inspect the fragment she dropped.
- Exit: the marked piece is obtained and its black line is shown. The
  paired exploration views return in the upper hallway and Kyle moves
  toward the next room encounter. The scope ends before talking to Jeff.
- Included: orientation and position on the two displays, contextual cue
  and reply, placement fit, picture completion, separate clue acquisition
  and restored local navigation. A documented alternate branch is used
  to distinguish stair access from the successful clue outcome.
- Excluded: check-in, the Room 215 key and suitcase, the next conversation,
  later uses of the piece, solving any hidden message, the later lid
  puzzle, optional rumble, Chapter 1's recap, retry internals, other
  regional releases as analysis targets, and the sequel.
- Suggested later scope: follow the later return of the piece through the
  assembled reverse-side clue. Compare physical lid input and the
  corresponding successor access.

## Direct-play status

No direct play was performed. Nintendo's European listing confirms the
Game Card and its English option. The original booklet and Nintendo of
Europe's description establish the common control layout. Geekmeister's
European-attributed recording provides the principal trace. Silent
Longplays corroborates the puzzle and clue on the original DS game with
the exact region unverified. The supergreatfriend recording documents a
different stairway outcome. All video review used silently inspected
stills and on-screen text. Physical stylus input, cartridge checksum,
saving and reloading, and left-handed operation were not exercised.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| HD-001 | The original commercial game is available as a Nintendo DS Game Card in Europe with English among its language options. | Observation | Corroborated | High | P1 and P2, 13 April 2007; R2 for NTR-AWIP-EUR; W1 title and channel attribution for the capture. These do not establish exact binary parity. |
| HD-002 | In the evidenced layout, exploration pairs the first-person hotel view with a touch map showing current position and heading. Conversations and puzzles instead show scene-specific views on the two adjacent screens. | Observation | Corroborated | High | P2, P3 printed pp. 16–19. W1 19:19 to 19:35, 22:42 and 25:13–25:16. W2 has a visible gutter between the two views. Left-handed options are documented in P3 but outside the trace. |
| HD-003 | A yellow contextual cue opens offered follow-up replies about the current exchange. The cue and choosing the subsequent offered reply are distinct. The girl's remarks expose the puzzle branch. | Observation | Corroborated | High | P3 pp. 18–19, P4 stairway dialogue and W1 20:10–20:18, 22:01–22:21. R1 transcribes branches; no hidden global disposition score is inferred. |
| HD-004 | The supplied jigsaw has five loose pieces at entry. On the right touch view each can be selected, turned with the corner arrows and fitted in its compatible gap. The completed picture settles and returns to dialogue. | Observation | Corroborated | High | P4 specifies five and the rotation arrows. W1 22:42–22:57 shows assembly and the completion flash; W2 32:00–32:50 repeats the process more slowly. No exact snap distance or forced countdown was measured. |
| HD-005 | In the accepted branch the girl scatters the finished puzzle, gathers pieces and leaves. Kyle can take the outstanding piece and see a black line on its reverse. Movement then returns in the upstairs hallway. | Observation | Corroborated | High | W1 23:06–25:17, W2 32:50–35:55, P4 and R1. The authored outcome exposes the marked fragment separately from the completed board. No meaning for the line is claimed here. |
| HD-006 | Ordinary access to upstairs does not depend on finishing this puzzle. A different conversation branch can reach the upper floor without the marked-piece outcome. The separate branch can carry a later conversational consequence. | Observation | Corroborated | High | W3 29:24–30:30 and 34:36 onward, R1's early exit and repeat stairway notes, P3's game-over rules. Later possible recovery or durable access after reload was not tested. |

## Basic data

- Analysis target: `PLAT-NINTENDO-DS`, 2007 original commercial European Game
  Card, English mode.
- Developer: Cing. Publisher: Nintendo.
- Mechanical family: `FAM-006`, spatial assembly and packing.
- Checked: 2026-11-23.
- P1: [Nintendo UK commercial Game Card listing](https://www.nintendo.com/en-gb/Games/Nintendo-DS/Hotel-Dusk-Room-215-271089.html).
  Confirms release date, Nintendo DS and the available languages.
- P2: [Nintendo of Europe's release and screen-layout account](https://www.nintendo.com/en-gb/News/2007/Check-out-Hotel-Dusk-coming-to-Nintendo-DS-249511.html).
  Confirms the book-held DS and the separate first-person and map displays.
- P3: [Original Nintendo instruction booklet, printed pp. 16–19](https://www.manualslib.com/manual/111805/Nintendo-Hotel-Dusk-Room-215-61313a.html).
  Scan of the North American English/French booklet. Its movement and
  conversation rules are corroborated by the European material and stills.
- P4: [Nintendo's Spanish guide for the European release, Chapter 1](https://www.guiasnintendo.com/0_NINTENDO_DS/Hotel_Dusk/hotel_dusk_sp/cap_01_pas_01.html).
  The stairway section documents replies, five loose pieces, the corner
  rotation arrows and the pickup. English wording comes from W1.
- W1: [World-of-Longplays European DS recording by Geekmeister](https://www.youtube.com/watch?v=6-PSLgFLpj4&t=1159s).
  Main route from the central hallway through the mark and restored motion.
  The channel notes that it often uses save states. No saved-state
  mechanics or elapsed-time properties are inferred from editing.
- W2: [Silent Longplays original DS recording](https://www.youtube.com/watch?v=oc0cReUcMvw&t=1910s).
  Corroborates the split display, the solve and the marked piece.
  Physical hardware and regional label unverified.
- W3: [supergreatfriend early DS route](https://www.youtube.com/watch?v=cDR3wIn1q_0&t=1764s).
  A different response reaches the upper floor without the assembly,
  followed by Dunning's intervention. Scope of this corroboration is
  the alternate outcome, with platform execution and region unverified.
- R1: [chibischala's scene transcript and branch trace](https://gamefaqs.gamespot.com/ds/933043-hotel-dusk-room-215/faqs/47968).
  In the Chapter 1 stair sequence, checks the separation between solving,
  obtaining the piece and ordinary passage.
- R2: [European cartridge identifier catalogue](https://www.vgdb.com.br/nintendo-ds/jogos/hotel-dusk-room-215/).
  Corroborates regional packaging and carrier identification. It does not
  identify the exact bytes used by W1.

## Mechanical decomposition

### Action Genes

- ACT-008: move Kyle toward the stairs and later along the upper corridor.
- ACT-070: select a loose piece, rotate it and drag it toward its position.
- ACT-232: choose one authored response from the displayed follow-up options.
- ACT-341: address the dropped piece and acquire it in the close-up.
- ACT-866: take the current dialogue cue to open those follow-up responses.

### System Behaviour Genes

- SYS-1888: settle the assembled puzzle into the remainder of the
  conversation and make the separate dropped piece available to inspect.

### Constraint Genes

- CON-875: accept each loose piece only in a matching location and
  orientation. All five gaps must be settled for picture completion.

### Information Genes

- INF-148: expose the contextual follow-up opportunity and available
  responses before commitment. The future branch result is withheld.
- INF-606: show first-person space alongside the touch map in navigation,
  then split the encounter between portrait and interaction views.

### Objective Genes

- OBJ-349: finish the help branch with the marked piece acquired and
  ordinary movement restored.

### Time Genes

- TIM-002: assemble through separate player actions. The recorded board
  has no failure countdown that advances placements. Dialogue cue timing
  and the game's later chapter time are separate from this board rule.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| First-person stairs and current pose on the central-hallway map | Approach the stairs after checking in | The paired displays hand over to Kyle and the girl in an authored encounter | HD-002 |
| The girl refuses to move and describes why she is upset | Take the visible cue and choose the reply that engages with the puzzle | The exchange hands over to the right-hand jigsaw view, with Kyle on the left | HD-003, HD-004 |
| The right display has five loose fragments and matching gaps | Select, turn when needed and drag each fragment into its target | The board settles from five outstanding parts to a complete picture, then returns to dialogue | HD-004 |
| The finished picture has been handed back | Advance the ensuing exchange after it is scattered | The girl gathers the pieces and runs upstairs. One loose piece now has a separate close-up | HD-005 |
| One fragment is available on the step | Take it and advance the inspection | The reverse shows a black line. The upper hallway and touch map return and movement resumes | HD-005 |
| The exchange is abandoned or takes a different response branch | Continue past the stair encounter | The upper floor can be reached before piece acquisition, which is a distinct clue state | HD-006 |

## Strategic and experiential structure

The two displays serve different tasks without requiring two independent
actors. At the stairs, a contextual dialogue cue makes an actionable
problem available. Once inside the jigsaw, image continuity and edge
compatibility matter together. After acceptance, the restored picture
is itself temporary. The immediate clue comes from looking at one
physical fragment after the other character has left.

## Replay and variation

Both successful recordings use the same board outcome, with different
pacing between placements. W3 takes a different reply and reaches
upstairs without the immediate jigsaw and clue. Its later intervention
by Dunning does not imply that every skipped optional reply causes
failure. The repeat-encounter and later pickup possibilities are
documented separately by the transcript.

## Adjacent systems and history

The clue is not yet decoded. Showing or returning the piece, manipulating
the lid, and resolving the larger investigation require different scenes.
No physical hinge, breath or microphone input is part of the scoped
stairway action. The alternate dialogue branch is cited only as a
boundary test of the positive outcome.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-070, ACT-232, ACT-341, ACT-866 | Steer, fit, reply, acquire and open a follow-up |
| System Behaviour | SYS-1888 | Convert accepted puzzle work into a separate available clue |
| Constraint | CON-875 | Require each fragment's compatible place and orientation |
| Information | INF-148, INF-606 | Show dialogue affordances and paired live views |
| Objective | OBJ-349 | Acquire the marked fragment and resume navigation |
| Time | TIM-002 | Allow self-paced individual jigsaw placements |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `653` (`GAME-0001`–`GAME-0653`).
- Exact genome matches: none.
- Tied near matches: `GAME-0523` — Pentiment (`5 / 23 = 0.217391`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Pentiment (GAME-0523)](../m-r/pentiment.md) | ACT-008, ACT-232, ACT-341, INF-148, TIM-002 | Both combine movement, offered dialogue responses and examination in a staged investigation. Pentiment makes substantial inquiries spend calendar periods and carries testimony into a later verdict. The Hotel Dusk packet turns one follow-up into a five-piece picture task and then exposes a physical clue, without deciding the larger mystery. | Near, `0.217391` |

## Taxonomy impact

ACT-866 separates opening a follow-up from selecting one under ACT-232.
ACT-526 addresses revisitable testimony rather than the current remark
in a live exchange. ACT-070 already covers choosing, orienting and
seating a rigid piece, whereas ACT-780 holds the fragment's orientation
unchanged. CON-875 requires each fragment's target image and pose rather
than accepting any exact geometric cover. SYS-1888 and OBJ-349 separate
clue availability and the achieved clue state. SYS-119 and OBJ-048
require a persistent traversal lock that this alternate branch
contradicts. INF-606 covers simultaneous map and environment and the
substitution of task views. It does not treat a mirror or a second player
as the other screen.

## Negative results

- The stairs admit a different route through conversation. The jigsaw
  is not a universal physical gate to the upper floor.
- The complete picture is not the clue in inventory. The separate dropped
  piece is obtained afterward, with one partial mark.
- No numeric reaction threshold, hidden relationship score, frame window,
  binary checksum or save-reload persistence is inferred.

## Delta summary

Eleven scoped genes, including five additions and six reused definitions
for the first stairway conversation, jigsaw and marked-clue outcome.

## New facts

- A transient dialogue affordance can expose another offered response
  rather than committing the response itself.
- A solved object task can expose a secondary clue through what a
  character does afterward.
- A map can remain actionable while the neighbouring view supplies
  continuous local spatial context.

## Principles and design implications

Separate a conversation's follow-up window from its response list.
Let an apparent puzzle reward settle while keeping the later clue
a second, visible interaction. Keep location progress and evidence
progress legible when they can diverge.

## Puzzle or game generation potential

Use a conversation to expose a small, rigid arrangement. Give the
arrangement a clear completion cue and let it change a nearby actor's
behaviour. Let a single released object carry a visible partial clue
that can be kept while movement becomes available again.

## New genes

- ACT-866
- SYS-1888
- CON-875
- INF-606
- OBJ-349

## New combinations

None. All 274 verified combination signatures were checked.

## Taxonomy changes

[TAXONOMY_CHANGE_400](../../../research/taxonomy-changes/TAXONOMY_CHANGE_400.md).

## New questions

Does a missed cue permit the same useful reply at the next meeting?
Which route settles or reveals the complete marked pattern, including
the timing of the lid interaction? Compare original-DS traces with
visible physical controls and do not infer results from this first piece.

## Next recommended game

Kirby Air Riders, native English commercial Nintendo Switch 2 release.
Trace one complete Air Ride race from control and a steering or boost
decision through the resulting finish and final classification.

## Why this game

The first stairway encounter offers verifiable evidence of dialogue,
physical arrangement and clue acquisition across two different display
roles, within an otherwise traversable investigation route.
