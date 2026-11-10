# Taxonomy Change 221: original C64 guarded search and password assembly

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Direct
- Confidence: Medium
- Date: 2026-10-02.
- Trigger: `GAME-0484`, original English Commodore 64 *Impossible Mission*, one complete timed mission.
- Scope: fifteen Active additions `ACT-644`–`ACT-648`, `SYS-1273`–`SYS-1278`, `CON-749`–`CON-750`, `INF-460`, `OBJ-273`; twelve unchanged reuses. No earlier definition or signature changes.

## Evidence and transfer tests

The licensed reproduction of original instructions was read in full. One
independent first-hand written C64 account supports token consumption, timed
lethal retries, pitch sorting and the completed-card gate; a separate room-guide
introduction supports the connected route. Indexed creator answers support
reflection/superposition, not a claimed source-code inspection. No executable,
native PAL/NTSC variant, input trace, audiovisual or direct play was inspected.

- `ACT-216` covers the held reachable search command unchanged. `ACT-313`
  requires an equipped analyser and does not transfer. `CON-319` is Raider-
  specific uninterrupted work, so it is not silently broadened. `SYS-1273`
  preserves the distinct room-local retained-progress/reset/reveal transition.
- `ACT-008` transfers direct walking and somersault. `SYS-065` expressly
  excludes platforms directly moved by the avatar; `ACT-648` isolates occupied
  vertical lift control rather than a remote switch trajectory.
- `ACT-341` transfers contextual terminal/door activation. `CON-296` transfers
  key/code authority unchanged. `SYS-1274` resolves a spent typed utility code
  into a room-local reset or temporary disable, not a whole-world rewind or
  permanent destruction. Code type and effect duration are parameters.
- `ACT-056` edits persistent world-map fragments; `ACT-424` packs inventory
  footprints and `ACT-090` makes a fixture-usable composite item. None covers
  retained-memory copies, colour/reflection and editable overlay (`ACT-644`).
  `ACT-631` reverses difficulty-gated movement/block actions, while `ACT-044`
  rewinds simulation history; neither covers last-delete/join undo (`ACT-645`).
- `CON-065` enables multi-panel represented-world continuity; `CON-141`
  requires gapless exact cover. `CON-750` instead distinguishes same-colour
  non-overlap joining from complete correctly oriented card membership.
  `SYS-300` replaces a known item recipe; `SYS-1275` permits wrong local joins
  and recognises a correct card into a password letter.
- `ACT-522` spends a hint coin for a fixed clue. `ACT-646` spends mission
  time on addressed orientation or partner-availability help. The returned
  red orientation mark/inventory answer is visible feedback in `INF-460`,
  not a permanently revealed solution before card assembly.
- `ACT-076` preserves presentation order, which is explicitly wrong for this
  code room. `ACT-647` sorts by pitch; `SYS-1276` rewards the successful sort
  with a utility code and lengthens another challenge. No new gene is created
  for a pitch, square, token type or number of notes.
- `CON-076` coordinates complementary actor classes; `CON-749` instead
  restricts one actor's computer to corridor/elevator context. The room's
  identical input remains a somersault, not a globally accessible editor.
- `SYS-1153` penalises missed gates in final score and excludes a decreasing
  deadline. `SYS-610` preserves listed progression resources at a checkpoint;
  it does not establish this mission's exact death-restoration state.
  `SYS-1277` only establishes charged mission-time retry and resumed control,
  without inventing a precise return position or finite-life stock.
- `SYS-028` has order-sensitive additive/multiplicative modifiers and excludes
  a flat score table. `SYS-1278` adds terminal clock/finding/card/completion
  contributions; numerical weights are parameters. `OBJ-002` transfers score
  improvement, but `OBJ-154` is a designated hostile-target set. `OBJ-273`
  instead requires recognised password assembly and timely protected entry.
- `SYS-004`, `SYS-045`, `SYS-057`, `INF-003`, `INF-179`, `CON-068` and
  `TIM-003` transfer setup variation, autonomous/perceived movement, concealed
  contents, visible room, deadline and live input unchanged. No measured seed,
  exact hostile-program preview or universal sight/hearing is admitted.

## Decision and limitations

Admit the bounded transitions with reviewed bilingual fields, a named causal-
role partition and complete game-specific plain language. Original instructions
are separated from THEC64's modern menu restart. Sources differ about room
catalogue counts; no independently verified exact layout is claimed. Native
timing, collision, pause scheduling, death restoration and token decrement need
a later lawful executable trace before stronger claims. No earlier definition,
signature, combination, platform identity, automatic suggestion decision or
public publication changes. Health advisories receive an explicit measured
unit disposition after regeneration.
