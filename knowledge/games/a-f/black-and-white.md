---
game_id: GAME-0425
slug: black-and-white
game_title: "Black & White"
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-036
    - ACT-563
  system:
    - SYS-1121
    - SYS-1122
    - SYS-1123
  constraint:
    - CON-269
  information:
    - INF-417
  objective:
    - OBJ-246
  time:
    - TIM-003
---

# Game: Black & White — a watched Food Miracle on Land 1

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The island, chosen creature, food quantity and number of demonstrations are parameters, not additional genes.

## Analysis scope

- Version / ruleset: original 2001 English Windows PC *Black & White* story game on Land 1, after Sable's creature-and-leash tutorial. The exact disc and patch revision were not inspected.
- Structured analysis target: `PLAT-WINDOWS-PC` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: take the chosen creature on the Leash of Learning to Guide's Aztec village, read its raised Food Desire flag, activate an available one-shot Food Miracle bubble, cast food into the Village Store while the creature watches, and inspect the resulting village need, belief and creature-learning feedback. Repeat a demonstration only if seeking a stronger lesson; do not infer instant mastery from a single cast.
- Entry and exit: start after the first creature tutorial and the Guide meeting, with the creature and Leash of Learning available and the village's Food Miracle bubble reachable. The bounded analytical packet ends after a successful watched Food Miracle deposits food into the store and the resulting need/learning feedback is checked. Guide may later congratulate the player as village belief rises, but this packet does not require a specific conversion threshold, creature mastery or completion of Land 1.
- Included: assigning the Learning Leash, a one-shot Food Miracle's availability and addressed casting, food entering the village supply, Food Desire and belief response, observation-dependent creature learning, visible lesson/need cues, and live village/creature activity during the god's actions.
- Excluded: choosing the initial creature, Sable's earlier tutorial, creature combat, further Guide tasks, full village conversion, regular Prayer-Power-funded miracle production, totem adjustment (unavailable on Land 1), morality/alignment, hostile gods, other lands, multiplayer, *Creature Isle* and *Black & White 2*.
- Potential scoped modules: repeated reinforcement and independent creature food provision after mastery, worshipper allocation and Prayer Power, taking over a rival village, creature combat and morality over several lands.
- Direct-play status: no original disc, executable, input trace or audiovisual play was examined. The original Lionhead manual was read as a scanned third-party-hosted PDF, with its printed pages visually checked. A contemporary walkthrough identifies the Guide/Aztec village sequence. Exact patch, stock increments, learning percentage and belief thresholds remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BW-001` | After the first quest the player can choose a creature; the Leash of Learning makes it watch the god's actions, and learning may need repeated examples. | Confirmed | Direct | High | M1 pp. 11, 13 |
| `BW-002` | A one-shot miracle is activated from a bubble and cast from the Hand at a chosen world location; a Food Miracle can supply food. | Confirmed | Direct | High | M1 pp. 29–30 |
| `BW-003` | Food stored at the Village Store is available to villagers, whose Food Desire flag reports need; fulfilling village desires can increase belief. | Confirmed | Direct | High | M1 pp. 18–19 |
| `BW-004` | The Land 1 Guide sequence presents an Aztec village and a Food Miracle demonstration with the creature on the Learning Leash beside the store. | Observation | Corroborated | High | M1 pp. 11, 18–19, 29–30; W1 Land One walkthrough |
| `BW-005` | A light-bulb cue can signal that the creature has learned something, but the manual warns that one observation need not finish a lesson. | Confirmed | Direct | High | M1 p. 11 |
| `BW-006` | The creator describes the creature as learning and operating independently; this supports potential later autonomous use but does not verify one-cast mastery in this packet. | Observation | Corroborated | Medium | M1 pp. 11–13; D1 §§ What Went Right 2, 4 |
| `BW-007` | Exact stock change, learning percentage, belief gain and the number of casts until Guide's congratulations are not fixed by the inspected sources. | Observation | Limited | High | M1; W1 |

## Basic data

- Release / origin: Lionhead Studios' original 2001 Windows PC *Black & White*, published by Electronic Arts.
- Platform or physical form: Windows PC story mode, Land 1 after the initial creature tutorial; the structured target does not infer Mac or later modified releases.
- Mechanical families: agent routing and coordination (`FAM-015`) for directing the autonomous learner, and real-time system pressure (`FAM-010`) for village needs and creature activity continuing during god-hand input.
- Primary source accessed 2026-09-27: **M1** — [Lionhead Studios, *Black & White* original Windows manual scan](https://d1.xp.myabandonware.com/f/lvlb/Black-White_Manual_Win_EN.pdf), printed pp. 11–13, 18–20 and 29–30; hosted by a third party. Page spreads were visually inspected after OCR search.
- Creator source accessed 2026-09-27: **D1** — [Peter Molyneux, Lionhead Studios postmortem](https://www.gamedeveloper.com/design/postmortem-lionhead-studios-i-black-white-i-), *Game Developer*, 13 June 2001; design intent and creature autonomy, not a measured play trace.
- Contemporary sequence check accessed 2026-09-27: **W1** — [TheSuperBaconPirate, *Black & White* Land One walkthrough](https://gamefaqs.gamespot.com/pc/914356-black-and-white/faqs/23229), GameFAQs, 2003; confirms Guide, Aztec village, Food Miracle bubble, Learning Leash and repeated food demonstration. Its suggested creature-specific learning percentages are not adopted.

## Mechanical decomposition

### Action Genes

- Reused `ACT-036`: assign the Learning Leash to the one available creature so it attends to the god-hand's subsequent work; the leash directs learning rather than specifying each later creature action. `BW-001`, `BW-004`.
- New `ACT-563`: activate one available Food Miracle bubble, then use the Hand to cast its food at the addressed Village Store. The player controls target and timing, not the amount of belief awarded. `BW-002`, `BW-004`.

### System Behaviour Genes

- New `SYS-1121`: while the Learning Leash is attached, the creature observes the god's action and updates a persistent lesson; a light bulb can indicate learning, but repetition may be necessary. It is not a directly queued clone of each cast. `BW-001`, `BW-005`, `BW-006`.
- New `SYS-1122`: an accepted Food Miracle at the Village Store creates food in the village's usable supply. This is not the creature independently fetching crops or a regular miracle automatically generating Prayer Power. `BW-002`–`BW-004`.
- New `SYS-1123`: the village's Food Desire and belief respond to a fulfilled food need; one cast is not guaranteed to finish conversion or the whole guided sequence. `BW-003`, `BW-004`, `BW-007`.
- Resolution order: leash assignment → bubble activation and god-hand target → food supply → village need/belief response while the creature watches → partial or settled lesson feedback. The sources do not fix exact same-frame ordering. `BW-001`–`BW-007`.

### Constraint Genes

- Reused `CON-269`: the one-shot miracle requires an available bubble and a legal addressed world target; accepting the cast spends that one-shot use. Regular Prayer-Power-funded miracles and Land 1 totem adjustment are outside this packet. `BW-002`, `BW-004`.

### Information Genes

- New `INF-417`: the Food Desire flag identifies the village's current need; the Village Center can expose belief; a light bulb over the creature indicates a learned observation. None is a precise future learning-rate or conversion forecast. `BW-003`, `BW-005`, `BW-007`.

### Objective and Time Genes

- New `OBJ-246`: in this bounded analytical task, get food from the watched demonstration into the village supply and inspect the response. This is not a claimed authored victory screen, full creature training or Land 1 completion. `BW-002`–`BW-005`.
- Reused `TIM-003`: creature and villagers continue acting while the god positions the Hand, casts and checks the result; the sources do not establish a fixed countdown for this demonstration. `BW-001`, `BW-003`, `BW-006`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| The post-Sable creature and Learning Leash are available near Guide's village | Attach the Learning Leash to the creature | The creature follows and attends to actions performed with the Hand | teaching is a directed relation, not permanent direct control | `BW-001`, `BW-004` |
| The Village Store's Food Desire flag is raised | Hover to identify the flag | Food is the current visible need; no exact belief increment is promised | relevant demand is disclosed | `BW-003` |
| A one-shot Food Miracle bubble is available | Activate it and cast over the store while the leashed creature watches | The one-shot is used and food enters the store | a located miracle changes usable supply and is demonstrated | `BW-001`, `BW-002`, `BW-004` |
| Food has entered the store | Inspect flag and village belief cue | The need is addressed and belief can rise; a complete village conversion is not guaranteed | supply and allegiance feedback differ from the spell input | `BW-003`, `BW-007` |
| The creature has observed one cast | Wait for or repeat the lesson as needed | A light bulb may show learned behaviour; one demonstration is not guaranteed to teach full Food Miracle use | learning is persistent but not instant copying | `BW-001`, `BW-005`, `BW-006` |
| No one-shot Food bubble is available | Try to repeat this one-shot cast without another bubble | The previous charge does not reappear automatically; this packet cannot assume a free second cast | finite availability is a legality condition | `BW-002` |

## Strategic and experiential structure

- Local decision: choose the addressed store instead of casting food at an unrelated patch of land; keep the creature in observation range with the Learning Leash.
- Medium-term planning: supply the raised need while demonstrating the same useful action; if pursuing competence, repeat with another legal use rather than treating the first observation as mastery.
- Long-term structure: an independently acting trained creature could later help village provision, but that later behaviour and full belief conversion require a separate packet.
- Common heuristic: read the Food Desire cue before expending a one-shot Food Miracle.
- Failure attribution: an unavailable bubble blocks the cast; an unobserved cast can supply food without being a teaching demonstration; a still-raised flag or no light bulb does not prove the action was impossible.
- Player-trust factors: need flag, belief tooltip and learning light bulb provide bounded feedback, without exact hidden percentages.

## Replay and variation

The selected creature, available miracle uses, current food demand, Hand target and number of demonstrations can vary. The Land 1 Guide sequence is authored, not a procedural village generator. The sources do not establish exact learning-rate, belief-gain or supply-quantity distributions.

## Adjacent systems and history

*Nintendogs* teaches a puppy a spoken cue paired with a performed trick, but the original *Black & White* creature watches world-changing god-hand acts while attached to a Learning Leash. *The Sims 4* also has autonomous needs and a live simulation, but not a giant persistent creature learning the player's miracles. *Age of Empires II* villagers gather to fixed stockpiles under explicit work orders; this God Hand can place a one-shot resource miracle at a village store while an observing creature learns.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-036`, `ACT-563` | leash role, miracle bubble, store target |
| System Behaviour | `SYS-1121`, `SYS-1122`, `SYS-1123` | observation, food supply, need and belief |
| Constraint | `CON-269` | one-shot availability and legal target |
| Information | `INF-417` | Food Desire, belief and lesson cues |
| Objective | `OBJ-246` | bounded supply-and-demonstration packet |
| Time | `TIM-003` | concurrent village and creature activity |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `424` (`GAME-0001`–`GAME-0424`).
- Exact genome matches: none.
- Tied near matches: `GAME-0025` — Lemmings (`2 / 18 = 0.111111`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0025` *Lemmings* | `ACT-036` role assignment; `TIM-003` live resolution | *Lemmings* assigns finite skill roles to many walkers racing terrain hazards, whereas this packet binds one learning creature to a god-hand food demonstration, shared village stock, need-driven belief and persistent observation. | Tied-near maximum, `0.111111`; not an exact or combination match. |

## Taxonomy impact

[`TAXONOMY_CHANGE_163`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_163.md) admits the directed miracle, watched creature lesson, store-supply, need-to-belief response, visible training/need cues and bounded task terminal. No earlier genome or verified combination changes.

## Negative results

- `SYS-1111` rejected: *Nintendogs* pairs a recorded spoken cue with a trick; this creature watches god-hand world actions on a physical Learning Leash and may need repetitions.
- `SYS-407` rejected: the creature is not merely a combat follower beside a directly controlled avatar; its lesson changes later autonomous world behaviour.
- `ACT-333` rejected: a Food Miracle bubble is not a spell card cast from a visible hand in a card game's turn structure.
- `INF-065` rejected: a food-desire flag and belief cue are not Against the Storm's exact group Resolve trajectory with positive/negative contributors.
- Full-village victory, free unlimited Miracle use, an exact learning percentage, regular worship economy and Land 1 totem adjustment are not evidenced within this bounded packet.

## Delta summary

The god's positioned food miracle can both address a village store's need and be watched by a learning creature. Village belief and persistent creature behaviour respond through different systems; neither is guaranteed complete after a single cast.

## New facts

- [Confirmed | Direct | High] The manual distinguishes a Food Desire flag, watched learning on a leash, and one-shot miracle casting (`BW-001`–`BW-005`).

## New genes

- [Observation | Corroborated | High] `ACT-563`, `SYS-1121`, `SYS-1122`, `SYS-1123`, `INF-417` and `OBJ-246` isolate the evidenced interaction.

## New combinations

- [Observation | Direct | High] None created; verified prior combinations are checked against the complete signature.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_163` admits six new typed boundaries without revising prior signatures.

## New questions

- At what precise creature-lesson threshold does the Food Miracle become an independently chosen action, and how does this differ among starting creatures?
- How much does each one-shot food cast alter store stock, Food Desire and local belief in an inspected 2001 executable revision?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0426` *Tearaway* only after this unit's full validation, one local commit and Goal stop window; retain the recorded selection order.
- Optimisation criterion: contrast watched creature learning and village need with player-made paper-world manipulation in a fixed route.
- Expected information gain: different action, geometry and input feedback boundaries.
- Backlog impact: no successor is started in this unit.

## Why this game

- [Confirmed | Corroborated | High] A manual-backed one-shot Food Miracle and creature-learning rule intersect in the contemporary Land 1 Guide sequence, allowing a bounded analysis without claiming direct play or a fully trained creature.
