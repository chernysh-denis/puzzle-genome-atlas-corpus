---
game_id: GAME-0686
slug: maniac-mansion
game_title: "Maniac Mansion"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-087
    - ACT-089
    - ACT-096
    - ACT-341
    - ACT-907
  system:
    - SYS-112
    - SYS-1431
  constraint:
    - CON-136
  information:
    - INF-003
    - INF-631
  objective:
    - OBJ-026
  time: []
---

# Game: Maniac Mansion

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The original floppy, driveway, doormat, front-door key and foyer identify the fixture.

## Analysis scope

- Version / ruleset: Lucasfilm Games' commercial English 1987
  Commodore 64 retail floppy edition. The manual identifies the
  Commodore platform and load medium. W1 shows a boxed floppy
  and the English route from a physical disk test. Its disk bytes,
  exact pressing and machine firmware were not independently verified.
- Structured analysis target: PLAT-COMMODORE-64 in
  [platform coverage](../../platforms/games.json).
- Entry: select two companions for the mandatory Dave and start.
  Begin the fixture when the three stand by the driveway fence,
  with Dave active and his inventory empty. The two companions
  are present and take no action on the witnessed porch route.
- Primary decision loop: send Dave to the front door, identify
  the addressed door and mat through the cursor and sentence
  line, move the mat aside, pick up the exposed key and use
  it in the composed Unlock command. Once the doorway is
  visibly open, direct Dave through it.
- Exit: Dave is inside the first foyer, the key still appears
  in his inventory and ordinary movement is available. Stop
  before entering the kitchen or addressing the staircase fixture.
- Included: cursor-directed travel, choice of verb and operands,
  manual confirmation, visible pending sentence and result text,
  the mat and distinct key, key retention and front-door states.
- Excluded: later uses of the key, companion switching and
  character-specific skills, other mat verbs as tested alternatives
  in this pressing, scripted intrusions, later mansion puzzles,
  exact input timeouts, saves, sequel inclusions and other ports.
- Potential scoped module: test separate controlled actors at the
  foyer gargoyle and basement door in the original disk edition.
- Direct-play status: no personal Commodore 64 execution or disk
  inspection. W1 shows the physical floppy test. The Lucasfilm
  manual and hint book corroborate the opening and its command
  format. W2 is a tool-assisted C64 reference with unknown
  disk identity. W3 uses a later cartridge conversion and
  provides corroboration only, not release identity. Only relevant
  frames were reviewed in the background, with audio excluded.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| MM-001 | The 1987 commercial Commodore 64 game loads from floppy. Dave is fixed in the team; the player chooses two other teenagers. In the opening driveway Dave is initially controlled and his inventory is empty. | Confirmed | Corroborated | High | P1 pp. 1–2, P2, P3, W1 11:52–12:16 and 14:22–14:32 |
| MM-002 | The Commodore interface exposes preset verbs and a sentence line. World objects and inventory names supply operands; the interface inserts joining words. The manual describes confirming the sentence or its last word, and the line returns to Walk to after resolution. | Confirmed | Corroborated | High | P1 pp. 2–4, P2, W1 15:06–15:17 and 16:20–16:26 |
| MM-003 | Dave follows the selected walking destinations to the porch. The front door rejects an Open attempt with a locked message. Addressing the door with Unlock shows a pending tool position in the sentence even before a key is held. | Observation | Corroborated | High | W1 14:22–15:07, P1 pp. 3–4, P4 |
| MM-004 | In the retail recording, Pick up door mat moves the mat and leaves a separately selectable key on the landing. A second Pick up takes the key from the landing and adds its name to Dave's inventory. | Observation | Corroborated | High | W1 15:25–15:42, P1 p. 5, P4, W3 2:50–5:00 |
| MM-005 | After Dave executes the completed Unlock command with the carried key, the entrance opens and a later movement command leads into the foyer. The key remains listed. The sampled sequence does not establish a distinct second Open command as a necessary step. | Observation | Corroborated | High | W1 16:20–16:48, P1 pp. 3–4, P4, W2 2:00–2:50 |

## Basic data

- Release / origin: Lucasfilm Games, 1987, commercial English
  Commodore 64 disk. Designed by Ron Gilbert and Gary Winnick.
- Mechanical families: FAM-013 for the carried key and compatible
  fixture, and FAM-017 for the exposure, acquisition and entry order.
- P1: [Lucasfilm's 1987 Commodore and Apple manual](https://www.mocagh.org/lucasfilm/maniac-alt-manual.pdf).
  Use pp. 1–5 for the disk setup, team, initial view, sentence
  assembly and front-door example.
- P2: [Lucasfilm's history of SCUMM](https://www.lucasfilm.com/news/lucasfilm-originals-scumm/).
  Identifies the 1987 commercial game and the distinction between
  preset commands and earlier typed interfaces.
- P3: [Scans of the Commodore retail package and documentation](https://www.c64sets.com/set.html?id=84&title=Maniac+Mansion).
  Use the box, disk and booklet images for edition identification.
- P4: [Lucasfilm's original hint book](https://mocagh.org/lucasfilm/maniac-alt-hintbook.pdf).
  Scene One corroborates the locked porch door, key beneath the
  mat and entry into the house. Its later puzzles are outside scope.
- W1: [Floppy Deep Dive original boxed Commodore 64 disk test](https://www.youtube.com/watch?v=bvmuhtgMZ9Y&t=712s).
  Use 11:52–12:16 for the disk and team, and 14:22–16:48 for
  the driveway, locked door, key retrieval and foyer. The maker's
  later emulator test is separate from this segment.
- W2: [Myrryspeikko's C64 tool-assisted recording](https://www.youtube.com/watch?v=PM8ot8bJS3Q&t=120s).
  Use 2:00–2:50 to corroborate porch travel and entry. It does
  not establish the exact retail disk or the route's normal speed.
- W3: [MadMatty's C64 route and variant disclosure](https://longplays.org/infusions/longplays/longplays.php?longplay_id=13635).
  Use the 2:50–5:00 house segment as supplemental corroboration.
  It names the 2011 EasyFlash conversion. It is not evidence for
  disk loading, exact timing or identical behavior in other rooms.
- Claim IDs: MM-001–MM-005.

### Reproducible fixture evidence

1. At 11:56 in W1 the seven portraits are shown and only Dave
   starts selected. Choose two others and start. At 14:22
   Dave leaves the two companions by the driveway fence.
2. Select progressively leftward scene points until Dave reaches
   the porch stairs. Around 14:57 an Open attempt reports the
   locked door. At about 15:06 the incomplete Unlock sentence
   already names the target door and awaits its tool argument.
3. At 15:25–15:31 choose the mat with Pick up and confirm.
   Dave reaches it, the mat shifts, and the key is a separate
   object on the landing. The inventory is still empty.
4. Around 15:36–15:42 choose the exposed key and execute
   Pick up. Check that the word key now appears in inventory.
5. In W1 near 16:22 the completed sentence has the front door
   as its scene operand and the key as its inventory operand.
   Execute it and allow the scene to settle. The doorway is visibly
   open around 16:27, after the cursor briefly changes during
   resolution. Select the open passage to reach the foyer.
6. At 16:40, the entry, the foyer clock, the carried key and
   the ordinary Walk to command are all visible. Stop before
   using any interior door or object.

## Mechanical decomposition

### Action Genes

- ACT-087: apply the held key to the compatible front door through
  the explicit Unlock command. MM-005.
- ACT-089: collect the separately addressable exposed key into
  Dave's inventory. MM-004.
- ACT-096: select reachable scene points to approach the porch and
  cross through its open doorway. MM-003, MM-005.
- ACT-341: activate the mat as an addressed fixture. MM-004.
- ACT-907: assemble the command from a verb and its scene or
  inventory operands, then confirm it. MM-002, MM-005.

### System Behaviour Genes

- SYS-112: the accepted mat interaction exposes the previously
  concealed key as a separate scene object. MM-004.
- SYS-1431: resolve the locked front door into an open and
  traversable entrance after the compatible operation.
  MM-003, MM-005.

### Constraint Genes

- CON-136: the key must first be exposed, then acquired. The
  complete door command depends on the key still being carried.
  MM-003–MM-005.

### Information Genes

- INF-003: the key is fixed and concealed beneath the mat until
  the mat interaction exposes it. MM-004.
- INF-631: the sentence line shows the pending command, including
  its empty tool argument before the key is selected. The result
  message appears separately. MM-002–MM-003, MM-005.

### Objective Genes

- OBJ-026: make the foyer reachable through the front door and
  direct the active teenager inside. MM-005.

### Time Genes

No separate admission. The command order is essential. The
record does not establish a global pause or a fixed time window
for the porch solution.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Trio at the driveway fence | Choose reachable points to the left | Dave reaches the front porch; two companions stay behind | MM-001, MM-003 |
| Closed locked door, no held key | Try Open, then draft Unlock against the door | Locked response; the pending tool argument is empty | MM-002–MM-003 |
| Mat covers the key | Address and confirm the mat command | Mat displaced; key exposed on the landing, inventory still empty | MM-004 |
| Exposed key on the landing | Commit Pick up on the key | Key in Dave's inventory | MM-004 |
| Key held, door locked | Complete and execute Unlock with the key | Door opens after resolution; key retained | MM-005 |
| Doorway visibly open | Direct Dave through the opening | Dave inside the foyer with the key and movement available | MM-005 |

## Strategic and experiential structure

The default movement command lets the player approach the
door but does not solve its lock. The visible partial sentence
helps identify the missing tool. Moving the mat changes what
the cursor can address. Collecting the new scene target then
changes which sentence the player can complete.

## Replay and variation

The manual allows any two of the six companions at selection.
The witnessed entrance uses Dave alone. Switching protagonists,
alternate interactions with the mat and later dependencies on
the chosen roster require their own evidence.

## Adjacent systems and history

The resulting front door is an authored environment fixture.
Its state changes through local operations, while the separate
command line makes the user's current choice inspectable before it
takes effect. Lucasfilm identifies that choice as part of the
original SCUMM interaction design.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-087, ACT-089, ACT-096, ACT-341, ACT-907 | Apply the key, acquire it, navigate, operate fixtures and compose commands |
| System Behaviour | SYS-112, SYS-1431 | Distinguish door states and reveal the separately collectible object |
| Constraint | CON-136 | Require earlier exposure and acquisition for the completed key operation |
| Information | INF-003, INF-631 | Conceal the fixed object and expose the pending sentence |
| Objective | OBJ-026 | Enter the newly reachable foyer |
| Time | None | The causal sequence has no independently admitted timing requirement |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `685` (`GAME-0001`–`GAME-0685`).
- Exact genome matches: none.
- Tied near matches: `GAME-0613` — The Drifter (`6 / 16 = 0.375000`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [The Drifter (GAME-0613)](../s-z/the-drifter.md) | ACT-087, ACT-089, ACT-341, CON-136, OBJ-026, SYS-112 | Both expose and collect an object, apply it to an authored fixture and reach a newly accessible space. The Drifter interrupts a passenger to release the rebar and shows contextual icons. Maniac Mansion shifts a static cover, then makes the carried key part of an explicit verb sentence for the front door. | Near, `0.375000` |

## Taxonomy impact

Two additions separate command composition from the display
of the pending sentence and its missing argument. ACT-606
maintains a verb mode across uses. INF-590 represents a held
item at the cursor. The editable command and argument row
here are distinct. The mat's accepted operation already
matches SYS-112. The Drifter's SYS-1807 additionally needs
a separate actor whose tool grip is interrupted.

## Negative results

- An ordinary open attempt on the locked entrance fails.
- A visible Unlock sentence without a tool is incomplete.
- Moving the mat exposes the key and does not collect it.
- The footage does not establish either the necessity of a second
  Open command or a timed opening window.
- The key remains in the inventory after entering the foyer.
- Companion-specific skills did not determine the observed entrance.

## Delta summary

Eleven genes, two additions. The scoped sequence advances the
first controllable teenager from a locked exterior to the foyer by
exposing, collecting and explicitly applying a retained key.

## New facts

- The initial actor can perform the whole front-door route.
- A pending verb sentence displays its selected door and absent tool.
- The mat exposes an independent object rather than granting a reward.
- The open aperture can be crossed with a separate travel command.

## Principles and design implications

Separate the feedback for the drafted command, the visible scene
result and the retained item. An incomplete sentence can point to
a missing affordance without solving the search for the player.

## Puzzle or game generation potential

Give an original observatory entry a folded canvas over a
mechanical crank. A visible command line can show the intended
shutter and the missing crank before the player exposes it,
carries it and opens the unlocked shutter.

## New genes

- ACT-907
- INF-631

## New combinations

None admitted. All 274 verified gene sets were checked as proper subsets.

## Taxonomy changes

[Taxonomy Change 432](../../../research/taxonomy-changes/TAXONOMY_CHANGE_432.md).

## New questions

- Do additional mat verbs produce an equivalent result on the same disk?
- Which later interactions require an explicit character handoff?
- Can the foyer's basement route be reproduced without approaching the kitchen?

## Next recommended game

Continue Selection 059 with `GAME-0687`, Denshattack!, on
the commercial PlayStation 5 release.

## Why this game

The entrance compresses the early SCUMM adventure grammar into one
observable dependency: express a desired operation, inspect what
is missing and make its missing object addressable.
