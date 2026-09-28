---
game_id: GAME-0440
slug: scribblenauts
game_title: Scribblenauts
analysis_status: reviewed
reviewed: 2026-09-28
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
    - ACT-576
  system:
    - SYS-1154
    - SYS-1155
  constraint:
    - CON-713
    - CON-714
  information:
    - INF-425
  objective:
    - OBJ-025
  time: []
---

# Game: Scribblenauts — original DS desert refreshment puzzle

Use the [canonical vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). `Lemonade`, The Gardens Puzzle 1-5, the Object Meter and the Starite are scoped parameters and carriers, not stand-alone gene names.

## Analysis scope

- Version / ruleset: original English North American *Scribblenauts* for Nintendo DS (2009), Challenge Mode Puzzle Mode, The Gardens Puzzle 1-5, the desert wanderer's `Refresh Him` request. The original instruction booklet itself walks through this puzzle; a first-hand original-game guide independently identifies it as Puzzle 1-5 and reports other compatible refreshment words. The exact ROM revision was not inspected.
- Structured analysis target: `PLAT-NINTENDO-DS` in [`knowledge/platforms/games.json`](../../platforms/games.json), touch-screen and Notepad controls of the original release, not a later sequel or remaster.
- Primary decision loop: read the short need hint and observe the desert wanderer; choose an eligible object noun in the Notepad; allow the system to instantiate the object; drag it to the actor and see whether it satisfies his need. A successful refreshment reveals a Starite. Move Maxwell to that token to complete the puzzle. If a created object is unsuitable, try another eligible noun within the Object Meter's simultaneous-object budget, removing an earlier object when required.
- Entry: Puzzle 1-5 is selected after the original game's profile and tutorial prerequisites; the wanderer and the `Refresh Him` hint are present, but the Starite is not yet exposed. Starting a new profile, unlocking this puzzle and choosing a world are outside the decision packet.
- Positive terminal: the wanderer receives a compatible refreshing object, the Starite appears, and Maxwell contacts it to credit this one puzzle.
- Negative terminal: the booklet documents rejection of unsupported words and a finite Object Meter, but does not establish a timer, life-loss or forced-failure terminal for this particular puzzle. A rejected word or an unhelpful object merely leaves this bounded solution unresolved; restart/quit is outside the successful trace.
- Included: context hint, eligible noun entry, object instantiation, object placement on the wanderer, semantic response, deferred Starite reveal, Maxwell's direct movement to collect it, word rejection and simultaneous-object cap with deletion. `Lemonade` is the directly documented success; the first-hand guide also reports water and rain as alternatives, without this analysis claiming the complete accepted set.
- Excluded: Action Mode with a pre-exposed Starite, the other 109 ordinary Puzzle Mode challenges, Ollars, scoring medals, object popularity, online/Wi-Fi functions, unrestricted natural-language understanding, exact accepted-word catalogue, object-property coefficients, NPC health simulation, adjective composition from later titles and the sequel's revised rules.
- Reproducible parameterisation: on the original DS version, enter The Gardens Puzzle 1-5, read `Refresh Him`, write `Lemonade` in the Notepad and confirm. Observe that a drink object appears; drag it to the desert wanderer, observe the Starite appear, then move Maxwell into the Starite. A second run can compare other recognised refreshment nouns and the meter after several objects. The ROM revision, direct screen trace and exact Object Meter maximum were not obtained.
- Potential scoped modules: another Puzzle Mode challenge with a different semantic need, Action Mode's exposed-token route, and the scoring/replay economy.
- Direct-play status: no Nintendo DS, cartridge, emulator, screenshot, video or audio was inspected for this research. The original printed game booklet was read directly through a scan, and a separate first-hand original-game route corroborates the level identity and alternative solutions. The artwork is original interpretive art, not a captured game frame.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SCR-001` | Puzzle Mode offers a short need hint; the booklet's desert-wanderer example says `Refresh Him` and specifies `Lemonade` as a working object. | Confirmed | Direct | High | P1 |
| `SCR-002` | The Notepad accepts an object word and creates that object above Maxwell for stylus manipulation; unsupported terms and characters are restricted. | Confirmed | Direct | High | P1 |
| `SCR-003` | Giving the lemonade to the wanderer reveals a Starite; Maxwell must then run to the Starite to complete the level. | Confirmed | Direct | High | P1 |
| `SCR-004` | The Object Meter caps simultaneous scene objects and allows deletion to free room. | Confirmed | Direct | High | P1 |
| `SCR-005` | The booklet example is The Gardens Puzzle 1-5, and a first-hand guide records water and rain as further solutions to `Refresh Him`. | Observation | Corroborated | Medium | P1, P2 |
| `SCR-006` | The noun/object system relies on authored object properties and category interactions, not a promise that every natural-language phrase or every physical effect is simulated. | Confirmed | Direct | High | P1, P3 |

## Basic data

- Release / origin: original North American Nintendo DS *Scribblenauts* (2009), by 5th Cell and Warner Bros. Interactive Entertainment; not *Super Scribblenauts*.
- Platform or physical form: Nintendo DS cartridge; stylus and touch-screen Notepad, with on-screen keyboard or handwriting input.
- Mechanical family: object manipulation (`FAM-007`) and inventory/fixture dependencies (`FAM-013`); the lexical choice creates an object that must then satisfy a context-sensitive actor request.
- **P1:** [Original *Scribblenauts* DS instruction booklet](https://db.hfsplay.fr/files/2020/07/14/Manual_AHhWSCb.pdf), pp. 5–8 in scan (2009; accessed 2026-09-28). This is the original product manual, hosted by a preservation mirror, not a contemporary walkthrough.
- **P2:** [Mykas0, first-hand original DS *Scribblenauts* walkthrough](https://gamefaqs.gamespot.com/ds/955689-scribblenauts/faqs/57775), The Gardens Puzzle 1-5 `Refresh him!` (2009; accessed 2026-09-28). This provides independent level numbering and candidate alternatives but is not publisher rule text.
- **P3:** [5th Cell, *Scribblenauts* postmortem](https://media.gdcvault.com/GD_Mag_Archives/GDM_November_2009.pdf), *Game Developer*, November 2009, pp. 26–28. Its description of object properties and categories supports bounded object interactions; it is not direct evidence for the exact Puzzle 1-5 accepted-word set.
- Claim IDs: `SCR-001`–`SCR-006`.

## Mechanical decomposition

### Action Genes

- Add `ACT-576`: the player chooses and submits an object noun instead of selecting a fixed item recipe. Reuse `ACT-341` for directing the instantiated object to the addressed wanderer and `ACT-008` for moving Maxwell to the revealed Starite (`SCR-001`–`SCR-003`). The stylus is an input channel, not a separate gene; `ACT-091` is rejected because no carried-inventory transfer is evidenced.

### System Behaviour Genes

- Add `SYS-1154` for instantiating a recognised noun as a manipulable world object. Add `SYS-1155` for the actor-need test that reveals, but does not automatically collect, the Starite (`SCR-002`, `SCR-003`, `SCR-006`). Resolution order: validate word → create object → place on actor → evaluate need → reveal token → separately collect token.

### Constraint Genes

- Add `CON-713` for recognised/permitted nouns and text restrictions, separate from whether a valid object is useful here. Add `CON-714` for the simultaneous Object Meter cap and delete-to-make-room recovery; no numerical capacity is claimed (`SCR-002`, `SCR-004`).

### Information Genes

- Add `INF-425` for `Refresh Him`, a short contextual need cue that does not prescribe the word. The wanderer and scene support an inference of thirst, but the entire accepted noun set is not shown (`SCR-001`, `SCR-005`).

### Objective Genes

- Reuse `OBJ-025`: acquire the one puzzle-gated Starite after first revealing it by solving the actor request (`SCR-003`). Collecting a token is a separate terminal action after delivery.

### Time Genes

- None admitted. The manual calls the man wandering, but no timed expiry, scheduled irreversible progression or deadline for this specific puzzle was established. The actor's possible ambient movement alone does not meet `TIM-003`'s forced-progression boundary.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Hint and thirsty desert wanderer visible; no Starite | Write and confirm `Lemonade` in Notepad | The eligible noun instantiates a drink above Maxwell | lexical choice and object creation are different transitions | `SCR-001`, `SCR-002` |
| Drink exists; actor still needs refreshment | Drag the drink onto the wanderer | The need is satisfied and one Starite appears | object placement is tested semantically; the reward is deferred | `SCR-003` |
| Starite is now visible | Move Maxwell into the Starite | Puzzle completion is credited | reveal and collection are distinct | `SCR-003` |
| Existing objects fill the meter | Delete an earlier player-created object, then submit another eligible noun | Capacity is restored for another object | finite concurrent-object budget and recovery | `SCR-004` |
| A blocked or unsupported word is entered | Submit it | No arbitrary requested object is created | lexical legality is not the puzzle-solution test | `SCR-002`, `SCR-004` |

## Strategic and experiential structure

- Local decision: interpret a need rather than search for one prelisted answer. `Lemonade` is a directly documented success, while a first-hand route also records water/rain possibilities; the player must still cause the object to reach the actor.
- Medium-term plan: if an eligible object fails to refresh him, remove it when the Object Meter becomes limiting and try another semantic candidate. The meter prices simultaneous experiments, not dictionary breadth.
- Long-term boundary: reveal and touch one Starite; buying levels, broader campaign progression and medal optimisation remain outside the packet.
- Failure attribution: an unrecognised noun fails at the lexical gate; a recognised but irrelevant object fails only the contextual need test. The screen's hint and object response give different clues about those cases.
- Player trust: the documented example names a successful object and separates a visible Starite reveal from the final Maxwell collection.

## Replay and variation

The authored need and Starite objective stay fixed in this puzzle, but valid object choices can vary. The independent first-hand guide reports several refreshment routes; this record does not extrapolate to every object, exact scoring, or later adjective-based systems.

## Adjacent systems and history

*Baba Is You* (`GAME-0013`) also makes words mechanically potent, but its word blocks are pre-existing movable entities that recompute global rules when arranged into sentences. *Scribblenauts* receives a player-chosen eligible noun in the Notepad, creates a local object and tests that object's effect on a specific actor. *Machinarium* (`GAME-0106`) includes requested-item hand-ins, but its items come from authored fixtures and inventory rather than an open noun-to-object creation interface.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-341`, `ACT-576` | Maxwell movement, object-to-actor interaction, noun submission |
| System Behaviour | `SYS-1154`, `SYS-1155` | noun object creation, contextual need and token reveal |
| Constraint | `CON-713`, `CON-714` | word eligibility, simultaneous-object cap |
| Information | `INF-425` | `Refresh Him` contextual hint |
| Objective | `OBJ-025` | one revealed Starite must be collected |
| Time | none | no evidenced timed terminal or forced progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `439` (`GAME-0001`–`GAME-0439`).
- Exact genome matches: none.
- Tied near matches: `GAME-0302` — Captain Toad: Treasure Tracker (`2 / 13 = 0.153846`).
- Supported combination subsets: none.
- Scan date: 2026-09-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0302` *Captain Toad: Treasure Tracker* | `ACT-008`, `OBJ-025` | Both move one avatar to claim a puzzle-gated progress token. Captain Toad rotates a small authored stage and manipulates local fixtures to expose a Power Star while hazards advance; Scribblenauts chooses an eligible noun, creates a world object, satisfies an actor's contextual need and only then reveals a Starite. The token objective is shared, but the causal puzzle operation is not. | Tied-near maximum, not an exact match (`2 / 13 = 0.153846`). |

## Taxonomy impact

`TAXONOMY_CHANGE_177` admits one noun-submission action, two response rules, two eligibility/capacity constraints and one need-hint information boundary. Existing signatures and verified combinations are unchanged.

## Negative results

- `ACT-091` requires transferring a currently carried inventory item to an addressed requester. Here the manual directs a newly instantiated world object over the wanderer, with no required carried-item inventory state.
- `SYS-037` from *Baba Is You* recomputes rules from spatial word sentences, not a Notepad noun that spawns a physical object.
- `TIM-003` requires consequential forced real-time progression, not merely a wandering ambient actor with no evidenced deadline in this puzzle.
- The manual does not prove a complete accepted-word list, exact object-meter maximum, or any unpublished semantic simulation formula.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original booklet documents the full `Refresh Him` → `Lemonade` → reveal Starite → collect Starite chain (`SCR-001`–`SCR-003`).
- [Observation | Corroborated | Medium] A first-hand original-game route identifies this as The Gardens Puzzle 1-5 and records further refreshment candidates (`SCR-005`).

## New genes

- [Observation | Direct | High] Six typed boundaries are admitted in `TAXONOMY_CHANGE_177`; three existing genes are reused.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_177`; earlier signatures remain unchanged.

## New questions

- What is the exact simultaneous Object Meter maximum on the original North American DS cartridge, and which additional objects satisfy this particular NPC under a recorded build?

## Next game

`GAME-0441` *Pokémon GO* follows after the Goal stop window; its launch-era client, location loop and bounded rules require independent source review.
