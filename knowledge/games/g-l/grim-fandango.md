---
game_id: GAME-0582
slug: grim-fandango
game_title: Grim Fandango
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-049
    - ACT-087
    - ACT-089
    - ACT-091
    - ACT-107
    - ACT-232
  system:
    - SYS-112
    - SYS-700
    - SYS-1715
    - SYS-1716
    - SYS-1717
    - SYS-1718
  constraint:
    - CON-136
  information:
    - INF-553
  objective:
    - OBJ-318
  time:
    - TIM-002
---

# Game: Grim Fandango

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Arrange a signature by changing the boss's recorded reply. Then change who
receives an assignment by preparing and inserting a physical playing card.

## Analysis scope

- Version / ruleset: the original English-language 1998 LucasArts
  Windows 95/98 commercial CD-ROM game. Solo Year One with the original
  direct keyboard controls. Default character-relative movement is usable.
  The executable revision of the recording is unverified.
- Structured analysis target: PLAT-WINDOWS-PC.
  See [platform coverage](../../platforms/games.json).
- Entry: Manny Calavera has control in his office on the first morning
  with the poisoning dispatch waiting in his tube, his scythe available
  and the playing cards on the table. No work order has been signed.
- Primary decision loop: move until Manny notices the intended target.
  Ask people for actionable information or an item, then apply the
  appropriate held item to a fixture. Obtain the work order from
  Glottis, change Don Copal's recorded reply and have Eva sign it.
  Complete the first call, then fill two balloons separately and send
  them into the same mail system. Keep the sorter reopenable, and use
  the hole-punched card on Domino Hurley's branch to intercept his lead.
- Positive exit: retrieve the redirected assignment and reach the first
  office meeting with Mercedes Colomar, called Meche, through the
  scripted pickup. Stop at the first controllable intake conversation.
- Negative exit: an unsigned order leaves the trip unavailable. An
  obstructed sorter without the prepared latch can close access after
  service. An unpunched card is pulled away instead of catching the
  dispatch. The scoped puzzles have no verified lethal or countdown
  failure condition. The exact recovery sequence for every missed step
  and native save persistence were not measured.
- Included: original contextual navigation, the carry-and-use interface,
  cards and scythe, Glottis and Eva, tie rope and office window,
  recorded authority reply, the first client, two separately filled
  balloons, repair access and latch, and the replacement client handoff.
- Excluded: Meche's subsequent assessment, the resulting disciplinary
  scene, the resistance, roof and teeth puzzles, later years, external
  guides as an in-game mechanic, and the 2015 remaster or demo.
- Potential scoped modules: the roof pigeon and dental impression
  requirements for leaving El Marrow, or the extraction machine
  synchronisation after the Glottis rescue.
- Direct-play status: not conducted. The LucasArts manual establishes the
  controls and first signature puzzle. Two contemporary Windows routes
  and pre-remaster PC storyboard stills corroborate the full chain to
  Meche. No game executable, audio or video playback was used. Native
  timing, binary revision and save/reload were unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| GF-001 | LucasArts issued the original four-year adventure for Windows in 1998. Year One opens in Manny's office. The 2015 remaster is a distinct product. | Confirmed | Direct | High | P1, P2, P3 |
| GF-002 | The original keyboard controls move and face Manny directly. Head direction signals a noticed target. Holding a selected inventory item allows its use on that target. The original interface does not directly combine two held inventory items. | Confirmed | Direct | High | P1, W1 |
| GF-003 | Reframing the oversized driver problem in conversation yields Glottis's unsigned work order. The ordinary request to Eva leaves it unsigned. The alley tie rope and open window give access to Don Copal's unattended computer. | Observation | Corroborated | High | P1, R1, R2, W1 |
| GF-004 | Selecting the reply that delegates signing changes Eva's later intercom result. Presenting the work order then authorizes the modified car, and using the scythe on the packaged first client leads back to the office. | Observation | Corroborated | High | P1, R1, R2, W1 |
| GF-005 | The clown can supply two deflated worm balloons separately. Using one on each packing-room dispenser produces carried objects with different contents. The card can be hole-punched at Eva's desk independently of filling the balloons. | Observation | Corroborated | High | R1, R2, W1 |
| GF-006 | Sending both filled balloons into Manny's tube obstructs the shared sorter. An attendant opens it for service. Moving the open door's deadbolt before departure keeps the door reopenable after the attendant's closing attempt. | Observation | Corroborated | High | R1, R2, W1 |
| GF-007 | The ordinary card is drawn into the tube too soon. Perforation is the required preparation for the card to act as a blocker at the red branch assigned to Domino. Readable walkthroughs agree that this intercepts his lead. | Observation | Corroborated | High | R1, R2, W1 |
| GF-008 | After the redirected lead, the scripted pickup brings Meche to Manny's office. The intake begins before the later disciplinary and resistance sequences. | Observation | Corroborated | High | R1, R2, W1 |

## Basic data

- LucasArts. FAM-013 for held items used at fixtures and FAM-017 for
  order-sensitive authorization, access and interception prerequisites.
- P1: [Original LucasArts manual](https://mocagh.org/lucasfilm/grimfandango-manual.pdf).
  Controls and character-relative/camera-relative selection, pp. 12–16.
  Pages 26–30 describe the opening through Eva's signature and departure.
  The opening closes one authorization chain before the later sorter
  reconstruction. The issuer identifies the Windows product.
- P2: [LucasArts original press material](https://lucasarts.grim-fandango.com/grim_features.html).
  Pre-release publisher material for the original Windows game, preserved
  by a fan archive. Use [the retail catalogue dates](https://www.mobygames.com/game/201/grim-fandango/releases/)
  for the North American 30 October 1998 release rather than treating
  the press forecast as actual availability.
- P3: [Double Fine's release history](https://www.doublefine.com/games/grim-fandango-remastered/making).
  The creator's studio discusses the 1998 original and its later
  remaster. The page is linked as history, with no claim that the
  original binary is offered there.
- R1: [CJayC's original PC guide](https://gamefaqs.gamespot.com/pc/50544-grim-fandango/faqs/2407),
  version 1.7 of 1 December 1998. Year One's first two segments and the
  question sequence on the unpunched card corroborate the puzzle's
  required order and the separate modes of failure.
- R2: [Tim Wuyts's original PC walkthrough](https://gamefaqs.gamespot.com/pc/50544-grim-fandango/faqs/2409),
  written 7–21 January 1999. The poisoning and better-client sections
  independently corroborate the signature, first pickup, two materials,
  bolt, return, red branch and the correct replacement client.
- W1: [Game Destroyer's pre-remaster PC recording](https://www.youtube.com/watch?v=OaV0ZaFd7iQ).
  Sampled static frames at 5:50–15:10 for contextual interaction and
  Glottis, 23:20–27:10 for the tie rope, reply and Eva's approval,
  27:40–30:20 for the first call, 42:30–45:10 for loading and mailing
  the two balloons, and 45:50–53:20 for repair access, interception
  and Meche. The capture predates the remaster. Exact execution
  environment and patch are not established by its stills.
- Sources accessed 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-008 moves and turns Manny through the offices, garage and street.
  ACT-049 changes the current position of the accessible deadbolt.
  ACT-087 applies the selected held item at its intended fixture
  (GF-002, GF-003, GF-005–GF-007).
- ACT-089 collects the playing cards; ACT-091 presents the work order
  to its signing recipient. ACT-107 elicits useful information about
  the missing driver. ACT-232 chooses responses in conversation and
  advances branches such as Glottis's offer (GF-002–GF-005).

### System Behaviour Genes

- SYS-112 changes an authored mechanism's downstream access state
  when an eligible fixture operation resolves. SYS-700 changes the
  carried item's usable state at a legal target, such as the cards
  at the hole punch (GF-003–GF-006).
- SYS-1715 changes the subsequent authorisation by replacing the
  reply from an absent authority. SYS-1716 brings two separately
  prepared carriers together through the postal mechanism, prompting
  service rather than combining them in inventory (GF-003–GF-006).
- SYS-1717 preserves reopenability after the mechanic leaves. SYS-1718
  uses the prepared insert at one directed branch to intercept the
  assignment inside the shared pneumatic system (GF-006–GF-008).

### Constraint Genes

- CON-136 requires persistent prerequisites, such as approval before
  travel and an accessible sorter plus a prepared card before
  interception. An unpunched card alone is ineffective (GF-003–GF-007).

### Information Genes

- INF-553 indicates context by where Manny looks. The cue identifies
  the currently noticed target and does not show the resulting
  operation or all required states (GF-002).

### Objective Genes

- OBJ-318 completes an authorization and reassignment chain through
  the resulting first meeting, after interception and scripted pickup
  (GF-003–GF-008).

### Time Genes

- TIM-002 allows deciding the route and item uses at the player's own
  pace. Authored animations and the attendant's departure resolve
  after their relevant actions. No simultaneous acting or forced
  countdown is established for this scope (GF-003–GF-008).

## Reproducible transitions

| Before | Action or event | Bounded result | Claims |
| --- | --- | --- | --- |
| Manny can approach two neighbouring targets | Walk or pivot until his head turns toward the desired one | The indicated current person or object changes before the action | GF-002 |
| Glottis believes he cannot fit the car | Reframe its size in the offered response | Glottis supplies the work order | GF-003 |
| Eva cannot approve the uncertified order | Reach Don's computer via the tie rope, change the recorded reply and re-present the order | Eva signs and travel becomes available | GF-003, GF-004 |
| First client remains in the package | Use the held scythe on the package | The first call resolves and the route returns to the office | GF-004 |
| Two deflated balloons and two different dispensers are available | Fill them separately, then send both through the same message tube | The sorter jams and goes into service | GF-005, GF-006 |
| The attendant is servicing the open junction | Turn the deadbolt while open, then leave and come back | The sorter can be reopened after the attendant's departure | GF-006 |
| Plain cards and an accessible hole punch | Use the cards on the punch | The carried card is prepared for interception | GF-005, GF-007 |
| Open sorter and prepared card | Use it on Domino's red branch | The replacement assignment is intercepted and the scene leads to Meche | GF-007, GF-008 |

## Strategic and experiential structure

The two bottlenecks depend on preparation in another room. For the first,
conversation supplies the order, while editing the intercom reply changes
the result of submitting it. For the second, separate objects cause a
shared interruption and the bolt preserves access after repair. The card
works only after preparation at a different fixture. The game reports
discoverable targets locally while leaving those dependencies for the
player to infer.

## Replay and variation

Taking the cards early and choosing when to ask for balloons can save
backtracking. The dependency edges remain: dispatch authorization,
first pickup, correct preparation, service access, altered latch,
perforated card, interception and new client intake. The order of
unrelated inspections and exact persistent inventory after failure
were not independently tested.

## Adjacent systems and history

Controls and route here come from 1998-era documentation. The remaster
can expose alternative interaction controls and presentation; those
features are excluded. The following lockout and resistance jobs form a
different scoped puzzle chain after this first new-client meeting.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-049, ACT-087, ACT-089, ACT-091, ACT-107, ACT-232 | direct position, latch, fixture item use, collecting, handover and conversation |
| System Behaviour | SYS-112, SYS-700, SYS-1715, SYS-1716, SYS-1717, SYS-1718 | fixture result, item alteration, delegated reply, packet-induced service, latch and interception |
| Constraint | CON-136 | persistent item and access prerequisites |
| Information | INF-553 | noticed target communicated by head direction |
| Objective | OBJ-318 | new-client intake after reassignment |
| Time | TIM-002 | self-paced sequence |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `581` (`GAME-0001`–`GAME-0581`).
- Exact genome matches: none.
- Tied near matches: `GAME-0343` — The Secret of Monkey Island (`7 / 25 = 0.280000`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0343` — The Secret of Monkey Island | ACT-087, ACT-089, ACT-091, ACT-232, CON-136, SYS-112, TIM-002 | Both use conversations, carried tools and persistent prerequisites at the player’s pace. Guybrush earns and spends money, reads the concealed route and digs up the trial proof. Manny changes authorization through the intercom and intercepts a dispatch with a mechanically prepared insert before meeting a client. | `7 / 25 = 0.280000` |

### Preserved research notes

- New genes: SYS-1715–SYS-1718, INF-553 and OBJ-318.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_328](../../../research/taxonomy-changes/TAXONOMY_CHANGE_328.md)
  separates the changed authorization reply, sorter blockage, preserved
  access and intercepted assignment from their shared actions.

## Negative results

- Reject ACT-090: the game sends two independent carriers into a
  shared system and applies the playing card to an external tool.
- Reject INF-372: head direction indicates the object without
  displaying the legal command on the same cue.
- Reject SYS-1499: the player edits a recorded response used by
  another actor independently of relationship memory.
- Reject OBJ-158: the terminal here depends on intervening in a
  physical system and no load/reload check was performed.
- The color of a pipe, the exact formulation of the packing materials
  and the specific character names are evidence parameters.

## Delta summary

## New facts

- [Observation | Corroborated | High] Permission can be obtained by
  changing a remote recorded reply. Reassigning a later lead instead
  requires modifying physical access and a carried insert.

## New genes

- [Observation | Corroborated | Medium] Six additions in
  TAXONOMY_CHANGE_328.

## New combinations

- [Observation | Corroborated | High] No new verified combination
  proposed. The comparison owns the list of existing subsets.

## Taxonomy changes

- [Observation | Corroborated | Medium] Earlier definitions and
  signatures are retained.

## New questions

- A controlled native replay could establish exactly how many states
  survive after sending wrong contents, feeding a plain card, or
  leaving while the unmodified sorter door can still relock.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0583, Kunitsu-Gami: Path of the
  Goddess on PS5. Analyse one complete daytime preparation and night
  defence loop through its local settlement.
- Optimisation criterion: contrast an authored chain of small item
  operations with a recovery objective shared by several agents.

## Why this game

- [Hypothesis | Limited | Medium] This early route ends in a verifiable
  client handoff and draws a clear line between obtaining authority and
  changing the path of a material message.
