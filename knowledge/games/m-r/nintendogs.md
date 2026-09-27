---
game_id: GAME-0419
slug: nintendogs
game_title: Nintendogs
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-557
    - ACT-558
    - ACT-559
  system:
    - SYS-1111
    - SYS-1112
    - SYS-1113
  constraint:
    - CON-705
  information:
    - INF-412
  objective:
    - OBJ-244
  time:
    - TIM-003
---

# Game: Nintendogs — first named puppy at home

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Labrador breed, a chosen name, the word “sit”, a care item and the Nintendo DS stylus are carriers or parameters, not universal gene names.

## Analysis scope

- Version / ruleset: original 2005 North American English Nintendo DS *Nintendogs: Labrador & Friends*, using Nintendo of America's contemporary instruction booklet shared by the three launch editions. The exact cartridge revision and starting puppy variation were not inspected. This packet begins immediately after buying one first puppy at the kennel and follows the opening home tutorial through naming, teaching its first sit cue, unlocking the Supplies menu, checking the puppy's condition, one available feeding or grooming interaction and an explicit Home-screen save.
- Structured analysis target: `PLAT-NINTENDO-DS` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: attend to the puppy and the touch-screen prompts; say a consistent name and register it as text; use a trick opportunity to associate a spoken cue with sitting; after the two onboarding gates unlock supplies, inspect current condition, choose a suitable available care item and apply it through the touch screen. The puppy reacts to touch and learned voice cues rather than acting as a directly steered avatar. Save the resulting state.
- Entry and exit: begin at home with one newly purchased, unnamed puppy. The positive analytical endpoint is a named puppy that has learned the first sit command, an unlocked Supplies menu, one completed available care interaction and a manual save. This is **not** a game-wide victory screen or a claim that every welfare indicator is maximised. An unrecognised name or cue can be retried; the exact number of attempts is not fixed. The saved state persists the puppy and learned commands.
- Included: voice-and-text name registration, attention-sensitive spoken trick teaching and response, stylus petting with an adverse overlong boundary, the name-plus-sit menu gate, the Dog Status view, one care supply chosen from the available stock, and the explicit save control.
- Excluded: breed acquisition beyond the first puppy, three-dog household management, future-day care decay, precise needs values or purchase prices, advanced tricks, walks, contests, shopping, Bark Mode, wireless communication, breed unlocks and any rules from the later *Nintendogs + Cats* series. The chosen puppy and available care item are not claimed to be identical across cartridges or save files.
- Potential scoped modules: a measured later care session with need-state changes, one walk and stamina route, a contest with scored commands, or an edition-specific kennel and breed audit.
- Direct-play status: no DS cartridge, console, microphone trace, screenshot, video, audio or saved file was inspected. Nintendo's 2005 booklet supports this source-bounded reconstruction, but exact voice recognition tolerances, condition deltas and animation timings are unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `NDO1-001` | The booklet distinguishes three original editions and says their initial kennel breeds differ; this packet selects Labrador & Friends without asserting a fixed puppy. | Confirmed | Direct | High | P1; P2 |
| `NDO1-002` | A newly bought puppy is named by voice and then text; consistent pronunciation improves its recognition. | Confirmed | Direct | High | P1 |
| `NDO1-003` | The microphone calls a dog or issues a learned command; a learned trick may fail if the dog is not focused on the player. | Confirmed | Direct | High | P1 |
| `NDO1-004` | Stylus petting prompts a response, but doing it too long can annoy the puppy. | Confirmed | Direct | High | P1 |
| `NDO1-005` | Supplies, Go Out and Training icons appear only after the name and first sit teaching are complete. | Confirmed | Direct | High | P1 |
| `NDO1-006` | Dog Status shows current condition and learned commands; available care supplies can feed or groom the dog. | Confirmed | Direct | High | P1 |
| `NDO1-007` | The Home-screen save icon writes the puppy's experience and taught commands; no authored game-wide win is attached to this first-session endpoint. | Confirmed | Direct | High | P1 |
| `NDO1-008` | The exact cartridge revision, voice threshold, number of training attempts, condition values and real-time intervals were not measured. | Observation | Limited | High | P1 |

## Basic data

- Release / origin: Nintendo's original 2005 Nintendo DS *Nintendogs* family, scoped to the North American English *Labrador & Friends* edition. The shared North American booklet is marked © 2005. Nintendo's official product page independently identifies the DS edition and its touch/microphone pet-care premise; its European release date is not substituted for a North American cartridge date.
- Platform or physical form: Nintendo DS cartridge with touch screen, stylus and built-in microphone; not a phone touch port, 3DS sequel or emulator.
- Mechanical family: ordered dependency sequencing (`FAM-017`). Name recognition and first sit teaching gate the care-supply menu; later household play does not turn that first unlock into a whole-game ending.
- Sources accessed 2026-09-27:
  - **P1** — [Nintendo of America original Nintendogs instruction booklet](https://csassets.nintendo.com/noaext/image/private/t_KA_PDF/DS_Nintendogs?_a=DATC1RAAZAA0), printed pp. 8–23: kennel and naming, touch/microphone, Home and Dog Status, teaching tricks, care supplies and save. This is a publisher primary source, not a later-game manual. The booklet is shared across the three launch editions and does not identify a specific cartridge revision.
  - **P2** — [Nintendo's official Labrador & Friends product page](https://www.nintendo.com/en-gb/Games/Nintendo-DS/Nintendogs-Labrador-Friends-272057.html), platform, edition identity and pet-care premise. Its European regional date is not asserted as the North American release date.
- Claim IDs: `NDO1-001`–`NDO1-008`.

## Mechanical decomposition

### Action Genes

- `ACT-557`: stroke the puppy at a selected touch-screen contact. Petting has a response and may turn unwelcome when prolonged; it is not direct movement of the dog.
- `ACT-558`: speak the puppy's name or a trained trick cue through the microphone. The first naming flow also requires registering the name in text; speaking a command is not guaranteed to produce a trick.
- `ACT-559`: choose one available Care-category supply and use it to feed or groom the puppy after the Supplies icon unlocks.
- Claim IDs: `NDO1-002`–`NDO1-006`.

### System Behaviour Genes

- `SYS-1111`: pair the spoken name with its text registration and a trick cue with the puppy's learned action through repeated training opportunities; later recognise a sufficiently consistent cue only when attention permits. The booklet does not give a numerical acceptance threshold.
- `SYS-1112`: respond to touch-screen petting with a positive puppy reaction until overlong contact can annoy it; this is a pet response, not a scoring combo.
- `SYS-1113`: resolve a selected care item as its supported feeding or grooming interaction with the puppy. The packet records that the item performs care, not an invented numeric hunger, cleanliness or happiness increment.
- Resolution order: buy puppy → voice-and-text name → first sit training → unlocked supplies → inspect condition and apply an available care item → save. Petting and calling can be interleaved; the precise frames are unmeasured.
- Claim IDs: `NDO1-002`–`NDO1-008`.

### Constraint Genes

- `CON-705`: the Supplies, Go Out and Training affordances remain unavailable until the puppy has been named and taught to sit. This gates use of the care supply in this initial packet; it does not make later walks or contests part of the analysed route.
- Scarce resources: no time limit, money cost or consumable quantity for the chosen existing care item is promoted into this packet. The book does not establish a fixed starting inventory for every edition or file.
- Claim IDs: `NDO1-005`, `NDO1-008`.

### Information Genes

- `INF-412`: the Home/Dog Status view identifies the puppy, its current condition and learned commands, while touch-screen icons expose available menus. It does not reveal a numeric voice-recognition threshold or future need changes.
- Claim IDs: `NDO1-005`, `NDO1-006`, `NDO1-008`.

### Objective and Time Genes

- `OBJ-244`: establish a named, first-command-trained puppy and perform one available care action, then save this bounded opening session. This is an analytical local completion criterion inside an open-ended pet game, not an authored victory condition.
- `TIM-003`: touch and microphone inputs occur while the animated puppy can shift attention and react. No externally imposed session deadline or exact response window is claimed.
- Claim IDs: `NDO1-002`–`NDO1-008`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First puppy bought at the kennel | Say a clear name and register the same name in text | The puppy is named; consistent pronunciation improves later calling | voice identity plus explicit text registration | `NDO1-002` |
| Puppy is reachable on the touch screen | Stroke it briefly, or continue unusually long | Petting normally pleases it; excessive petting may annoy it | touch duration changes response | `NDO1-004` |
| Puppy has not learned sit | Use the available training opportunity and repeat one spoken cue as directed | The cue can be learned after several tries, not by a guaranteed single utterance | voice-to-trick training | `NDO1-003`, `NDO1-005` |
| Named puppy has learned sit | Return to Home and inspect its menu | Supplies, Go Out and Training affordances become available | two-prerequisite unlock | `NDO1-005` |
| Puppy may be distracted | Speak the learned sit cue before and after obtaining its focus | Only the attentive, recognised case is expected to perform the trick | voice recognition is not an unconditional button press | `NDO1-003` |
| Supplies menu is available | Inspect Dog Status, then choose an available care supply | Current condition and known tricks are readable; selected supply feeds or grooms | care choice informed by visible status | `NDO1-006` |
| Named and trained puppy after care | Use Home-screen Save | The current puppy and taught experience are stored | persistence, not a victory screen | `NDO1-007` |

## Strategic and experiential structure

- Local decision: attend to the puppy's current response; stop petting before it becomes irritating, obtain focus before saying a known cue, and choose a suitable available care item.
- Medium-term planning: establish the name and first trick before expecting care-supply access, then use condition information to decide what care to perform.
- Long-term structure: the persistent dog can be cared for, trained and taken elsewhere in the broader game. This packet neither models future-day decline nor claims that one action completes raising it.
- Failure attribution: a missed spoken cue can reflect naming consistency or attention; the exact recognition threshold is not exposed. A locked Supplies icon reflects incomplete onboarding, not a missing hardware feature.
- Player-trust factors: visible status and learned-trick list make care and training legible, whereas voice recognition is approximate and source evidence does not quantify it.
- Claim IDs: `NDO1-002`–`NDO1-008`.

## Replay and variation

- Edition-specific kennel breeds and individual puppies differ. This packet does not require one fixed Labrador coat or personality, only the original *Labrador & Friends* edition and one first puppy.
- The chosen name, pronunciation, number of training attempts and available care item may vary. The same gate and information roles are expected, not an identical scripted sequence of frames.

## Adjacent systems and history

- *The Sims 4* shows household needs and contextual resident orders, but a DS puppy's touch contact and microphone-trained cue are not orders to a directly controlled resident.
- *Viva Piñata* also exposes animal residence conditions, but its garden visit and habitat gates do not establish voice recognition or the first-name-plus-sit interface unlock.
- *Planet Zoo* recomputes species habitat welfare, a broader management simulation rather than one puppy's direct care interaction.
- *Nintendogs + Cats* is a later product with different hardware and is not retroactively included.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-557`, `ACT-558`, `ACT-559` | stroke, utterance, care item |
| System Behaviour | `SYS-1111`, `SYS-1112`, `SYS-1113` | recognition, attention, pet response, care operation |
| Constraint | `CON-705` | named puppy and first sit gate |
| Information | `INF-412` | current condition, learned tricks, available icons |
| Objective | `OBJ-244` | bounded first-home session, not whole-game victory |
| Time | `TIM-003` | live pet attention and response without a session deadline |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `418` (`GAME-0001`–`GAME-0418`).
- Exact genome matches: none.
- Tied near matches: `GAME-0391` — Uncharted 2: Among Thieves (`1 / 14 = 0.071429`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Uncharted 2: Among Thieves (`GAME-0391`) | `TIM-003`: live input while a responsive state advances | Nintendogs names, trains and cares for one autonomous puppy with touch and voice; Uncharted's selected train passage is a forced physical escape across failing supports. Neither its traversal, hazards nor stage objective transfers to puppy care | Near, `0.071429` |

## Taxonomy impact

- [`TAXONOMY_CHANGE_157`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_157.md) admits nine typed boundaries. `TIM-003` is reused; no earlier signature or verified combination is changed.

## Negative results

- `ACT-257` rejected: a resident's contextual autonomous task in *The Sims* does not describe direct stylus touch and a microphone-trained puppy cue.
- `SYS-431` and `SYS-867` rejected: household-motive and zoo-species welfare calculations would invent numeric need changes not established for this first puppy session.
- `TIM-017` rejected: no offline care decay is evidenced by the bounded manual pages.
- No fixed training-attempt count, exact voice score, care delta or all-puppies breed set is inferred.

## Delta summary

A new puppy's voice-and-text identity and first learned sit unlock the first care tools. Stylus petting can please or annoy depending on duration; voice response depends on a learned cue and attention. Status inspection, a chosen care supply and explicit save close a bounded opening session without pretending that the open-ended pet game has been won.

## New facts

- [Confirmed | Direct | High] Nintendo's original booklet identifies the name-plus-sit affordance gate and the Dog Status condition/trick view (`NDO1-005`, `NDO1-006`).
- [Confirmed | Direct | High] Puppy touch and trained microphone cues have distinct response conditions (`NDO1-003`, `NDO1-004`).

## New genes

- [Observation | Direct | High] `ACT-557`–`ACT-559`, `SYS-1111`–`SYS-1113`, `CON-705`, `INF-412` and `OBJ-244` isolate the touch, voice, care, unlock, inspection and local-session boundaries.

## New combinations

- [Observation | Limited | High] No verified combination is introduced from one first-home session; proper-subset validation remains authoritative.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_157` documents nine new typed boundaries and the rejected household or zoo-welfare transfers.

## New questions

- Which exact North American cartridge revision, microphone input conditions and cue repetitions reproduce one named puppy's training?
- What condition values change after a measured feeding or grooming event, and what changes while the DS is closed or powered off?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0420` *Project Gotham Racing 2* on original Xbox, only after this unit's validation, local commit and Goal stop window.
- Optimisation criterion: contrast the puppy's care and voice-feedback session with one scored vehicle event where racing position and style points can diverge.
- Backlog impact: preserve approved `GAME-0420`–`GAME-0432` order; do not start another subject in this unit.

## Why this game

- [Hypothesis | Direct | Medium] The original DS pet interface contrasts FTL's paused shipwide command overview. Name registration, a learned spoken cue and a touch-care response are source-backed boundaries that cannot be inferred from a generic pet label.
