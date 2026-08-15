---
game_id: GAME-0105
slug: outer-wilds
game_title: Outer Wilds
analysis_status: reviewed
reviewed: 2026-08-15
combination_ids:
  - COMB-0105
gene_ids:
  action:
    - ACT-008
    - ACT-072
    - ACT-107
  system:
    - SYS-140
    - SYS-141
  constraint:
    - CON-159
  information:
    - INF-055
  objective:
    - OBJ-026
  time:
    - TIM-003
    - TIM-016
---

# Game: Outer Wilds

## Analysis scope

- Version / ruleset: original base game, bounded to first Launch Day, the first
  learned launch-code access, one paired loop reset and repeat access to the
  launch lift without revisiting Hornfels.
- Included: awakening at the Timber Hearth campfire; navigating to the
  observatory; receiving the fixed launch codes `-- | -.. | -.` from Hornfels;
  Nomai-statue pairing; activating the code-gated launch lift; reaching the
  ship; live world progression; one death or supernova reset; physical-state
  restoration at the campfire; retained code knowledge; Slate's acknowledgement;
  and opening the same lift without current-loop reacquisition.
- Excluded: optional village tutorials, detailed ship controls, individual
  planets, ship-log graph, every discovery except launch codes, coordinates,
  quantum rules, endgame, Echoes of the Eye, mods and speedrunning.
- Direct-play status: not conducted because no licensed executable was found on
  this Mac. Mobius developer material establishes Launch Day, the one required
  observatory task and knowledge-led structure; creator and publisher material
  establishes the 22-minute resetting system. Maintained records and an
  independent account corroborate the exact code, lift gate and later-loop
  acknowledgement. The executable control isolates retained knowledge from
  reset physical state.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `OWI-001` | The only required opening-village task is obtaining launch codes from Hornfels at the observatory | Confirmed | Corroborated | High | P1, P2 |
| `OWI-002` | The fixed code is `-- / -.. / -.` and gates the launch-tower lift | Confirmed | Corroborated | High | S1, S2, V1 |
| `OWI-003` | Nomai-statue pairing occurs after code acquisition and establishes remembered later loops | Confirmed | Corroborated | High | S3, S4 |
| `OWI-004` | The solar system advances in real time and resets after an approximately 22-minute cycle or earlier death | Confirmed | Corroborated | High | P3, P4 |
| `OWI-005` | A reset restores the Hatchling and world origin but retains learned launch-code knowledge rather than carried physical state | Confirmed | Corroborated | High | P3, S1, V1 |
| `OWI-006` | On a later loop Slate acknowledges that the Hatchling already has the code and the lift works without another Hornfels visit | Confirmed | Corroborated | High | S4, V1 |

## Basic data

- Release / origin: developed by Mobius Digital and released in 2019.
- Platform or physical form: single-player first-person exploration videogame.
- Puzzle family: knowledge-persistent exploration across a resetting live world.
- Primary sources:
  - **[P1]** [Mobius Digital: Filling Out the Toolbox](https://www.mobiusdigitalgames.com/news/filling-out-the-toolbox),
    for Launch Day, the sole required launch-code goal and optional village
    training.
  - **[P2]** [Alex Beachum's Outer Wilds thesis](https://sbekumod.github.io/Assets/OWtesi.pdf),
    for the observatory launch-code task as the only mandatory introduction.
  - **[P3]** [PlayStation Blog: a solar system that resets every 22 minutes](https://blog.playstation.com/archive/2019/10/08/explore-a-solar-system-that-resets-every-22-minutes-in-the-outer-wilds-out-this-month),
    for the fixed cycle, changing environments and knowledge-only progression.
  - **[P4]** [Outer Wilds GDC 2021 presentation](https://media.gdcvault.com/GDC%2B2021/beachum_gdc_2021%281%29.pdf),
    for the evolving loop and supernova boundary.
- Secondary sources:
  - **[S1]** [Official Outer Wilds Wiki: Launch codes](https://outerwilds.fandom.com/wiki/Launch_codes),
    for the exact code, lift requirement and post-death retention.
  - **[S2]** [PC Gamer opening account](https://www.pcgamer.com/exploring-the-final-frontier-in-the-outer-wilds/),
    for the observatory-to-console-to-lift sequence.
  - **[S3]** [Official Outer Wilds Wiki: Timber Hearth](https://outerwilds.fandom.com/wiki/Timber_Hearth),
    for the observatory, statue pairing and code-gated launch tower.
  - **[S4]** [Official Outer Wilds Wiki: Slate](https://outerwilds.fandom.com/wiki/Slate),
    for the later-loop interception and authored `already got them` branch.
  - **[V1]** [`verify_outer_wilds_launch_loop.py`](../../../scripts/verify_outer_wilds_launch_loop.py),
    an independent executable control for the bounded packet.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. The player walks from campfire to
  observatory, returns to the launch tower and reaches the lift in both loops.
- `ACT-072` — activate addressed mechanism trigger. Holding the available
  launch-console interaction commands the linked lift; the player does not edit
  a free-form code or consume a key.
- `ACT-107` — acquire operational fact through authored dialogue. Completing
  Hornfels' exchange registers the fixed launch code as learned.

### System Behaviour Genes

- `SYS-140` — reset embodied world state while preserving learned facts. Death
  or the supernova returns the Hatchling to the campfire and clears the first
  loop's physical state while transferring paired knowledge.
- `SYS-141` — authorise mechanism from registered learned fact. The launch lift
  accepts the learned code in a later loop without a new observatory visit.
- Resolution order: learn the code; pair with the statue; activate the lift;
  let the live cycle end or die; restore the world origin; retain learned facts;
  acknowledge the code to Slate; activate the newly reset lift again.

### Constraint Genes

- `CON-159` — learned credential gates access without current-loop
  reacquisition. Before the code is learned the lift is unavailable; after a
  paired reset the same knowledge satisfies the gate without an inventory item.

### Information Genes

- `INF-055` — retained fact is explicitly available after world reset. The code
  marks remain available and Slate's branch exposes that the Hatchling knows
  something this reset world has not supplied again.

### Objective Genes

- `OBJ-026` — reach designated traversable world location. The bounded opening
  task ends at the ship's launch pad after the code-gated lift becomes usable.

### Time Genes

- `TIM-003` — real-time input during forced progression. The world keeps moving
  while the player navigates, speaks and explores.
- `TIM-016` — fixed real-time world cycle terminates in loop reset. The
  approximately 22-minute post-pairing cycle ends in the supernova, while
  earlier death may trigger the same reset transition.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First Launch Day, code unknown | Reach Hornfels and complete the code dialogue | `-- / -.. / -.` is registered as learned | dialogue-acquired operational fact | `OWI-001`, `OWI-002` |
| Code unknown at launch tower | Activate the lift console | Lift remains unavailable | credential gate | `OWI-002` |
| Code learned after statue pairing | Activate the lift console | Lift carries the Hatchling to the ship | fact-authorised mechanism | `OWI-002`, `OWI-003` |
| Paired loop with temporary physical state | Die or reach the supernova | Campfire origin is restored; temporary physical state clears; learned code remains | selective reset partition | `OWI-004`, `OWI-005` |
| Later loop, Hornfels not visited | Approach Slate and activate lift | Slate accepts the already-known code; lift reaches the ship | cross-loop knowledge is operational | `OWI-006` |

## Strategic and experiential structure

- Local decision: decide whether to spend time in optional village tutorials or
  take the direct path to the sole required observatory fact.
- Medium-term planning: use a later iteration's unchanged starting geometry and
  retained information to omit previously necessary acquisition travel.
- Long-term structure: discoveries, not avatar upgrades, progressively replace
  exploration uncertainty with executable routes through a reset solar system.
- Common heuristics: distinguish knowledge from world state; test whether a
  learned fact survives; exploit the stable start to shorten the next route.
- Failure attribution: losing temporary position or possessions at reset is
  expected, while losing the learned code would contradict the paired loop.
- Player-trust factors: a known credential must work identically after reset,
  and NPC acknowledgement must not force a logically repeated tutorial.

## Replay and variation

- The launch code, observatory path and lift destination are authored and fixed.
- Optional tutorials and exploration change elapsed time, not the code predicate.
- Death can end the loop before the supernova; both boundaries produce the same
  scoped knowledge-retaining reset once statue pairing has occurred.

## Adjacent systems and history

- TUNIC also lets prior knowledge open a world route, but its player manually
  enters a directional sequence and its world does not reset around that fact.
- Braid restores prior physical states through player-controlled rewind;
  Outer Wilds instead imposes a loop boundary and preserves a fact-class subset.
- Loop Hero repeats a world route with persistent resources, while this packet
  resets embodied state and advances by knowledge rather than retained loot.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-072`, `ACT-107` | dialogue path; console hold |
| System Behaviour | `SYS-140`, `SYS-141` | reset partition; fact key |
| Constraint | `CON-159` | current-loop reacquisition policy |
| Information | `INF-055` | code HUD; Slate acknowledgement |
| Objective | `OBJ-026` | launch-pad arrival |
| Time | `TIM-003`, `TIM-016` | cycle start; early death |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `(ACT-008,ACT-072,ACT-107; SYS-140,SYS-141; CON-159; INF-055; OBJ-026; TIM-003,TIM-016)`.
- Indexed games scanned: 105, including this record.
- Indexed combinations scanned: 105.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0098` is nearest at
  `3 / 14 = 0.214286`; it shares navigation, live progression and destination
  arrival but none of the knowledge-retaining reset structure.
- Supported combination subsets: `COMB-0105` only.
- Scan date: 2026-08-15.

### Full prior-game Jaccard scan

- `GAME-0001`: `0 / 24 = 0.000000`; `GAME-0002`: `0 / 17 = 0.000000`; `GAME-0003`: `0 / 19 = 0.000000`; `GAME-0004`: `1 / 24 = 0.041667`.
- `GAME-0005`: `0 / 17 = 0.000000`; `GAME-0006`: `1 / 18 = 0.055556`; `GAME-0007`: `0 / 18 = 0.000000`; `GAME-0008`: `0 / 17 = 0.000000`.
- `GAME-0009`: `0 / 26 = 0.000000`; `GAME-0010`: `0 / 19 = 0.000000`; `GAME-0011`: `0 / 23 = 0.000000`; `GAME-0012`: `0 / 19 = 0.000000`.
- `GAME-0013`: `0 / 23 = 0.000000`; `GAME-0014`: `0 / 25 = 0.000000`; `GAME-0015`: `0 / 24 = 0.000000`; `GAME-0016`: `1 / 24 = 0.041667`.
- `GAME-0017`: `0 / 23 = 0.000000`; `GAME-0018`: `1 / 28 = 0.035714`; `GAME-0019`: `0 / 20 = 0.000000`; `GAME-0020`: `0 / 24 = 0.000000`.
- `GAME-0021`: `1 / 18 = 0.055556`; `GAME-0022`: `0 / 22 = 0.000000`; `GAME-0023`: `0 / 20 = 0.000000`; `GAME-0024`: `1 / 21 = 0.047619`.
- `GAME-0025`: `1 / 20 = 0.050000`; `GAME-0026`: `1 / 21 = 0.047619`; `GAME-0027`: `1 / 21 = 0.047619`; `GAME-0028`: `1 / 26 = 0.038462`.
- `GAME-0029`: `2 / 20 = 0.100000`; `GAME-0030`: `1 / 23 = 0.043478`; `GAME-0031`: `0 / 21 = 0.000000`; `GAME-0032`: `0 / 21 = 0.000000`.
- `GAME-0033`: `2 / 21 = 0.095238`; `GAME-0034`: `2 / 22 = 0.090909`; `GAME-0035`: `2 / 26 = 0.076923`; `GAME-0036`: `1 / 21 = 0.047619`.
- `GAME-0037`: `0 / 19 = 0.000000`; `GAME-0038`: `2 / 24 = 0.083333`; `GAME-0039`: `0 / 19 = 0.000000`; `GAME-0040`: `2 / 16 = 0.125000`.
- `GAME-0041`: `2 / 19 = 0.105263`; `GAME-0042`: `0 / 19 = 0.000000`; `GAME-0043`: `1 / 23 = 0.043478`; `GAME-0044`: `1 / 19 = 0.052632`.
- `GAME-0045`: `1 / 23 = 0.043478`; `GAME-0046`: `0 / 20 = 0.000000`; `GAME-0047`: `0 / 24 = 0.000000`; `GAME-0048`: `0 / 24 = 0.000000`.
- `GAME-0049`: `0 / 19 = 0.000000`; `GAME-0050`: `1 / 24 = 0.041667`; `GAME-0051`: `1 / 25 = 0.040000`; `GAME-0052`: `0 / 20 = 0.000000`.
- `GAME-0053`: `1 / 18 = 0.055556`; `GAME-0054`: `2 / 19 = 0.105263`; `GAME-0055`: `1 / 19 = 0.052632`; `GAME-0056`: `0 / 18 = 0.000000`.
- `GAME-0057`: `0 / 18 = 0.000000`; `GAME-0058`: `0 / 19 = 0.000000`; `GAME-0059`: `0 / 17 = 0.000000`; `GAME-0060`: `1 / 16 = 0.062500`.
- `GAME-0061`: `0 / 20 = 0.000000`; `GAME-0062`: `0 / 18 = 0.000000`; `GAME-0063`: `0 / 17 = 0.000000`; `GAME-0064`: `0 / 15 = 0.000000`.
- `GAME-0065`: `0 / 17 = 0.000000`; `GAME-0066`: `0 / 20 = 0.000000`; `GAME-0067`: `0 / 18 = 0.000000`; `GAME-0068`: `0 / 18 = 0.000000`.
- `GAME-0069`: `0 / 18 = 0.000000`; `GAME-0070`: `0 / 18 = 0.000000`; `GAME-0071`: `0 / 17 = 0.000000`; `GAME-0072`: `0 / 18 = 0.000000`.
- `GAME-0073`: `0 / 17 = 0.000000`; `GAME-0074`: `0 / 19 = 0.000000`; `GAME-0075`: `0 / 19 = 0.000000`; `GAME-0076`: `0 / 17 = 0.000000`.
- `GAME-0077`: `0 / 17 = 0.000000`; `GAME-0078`: `0 / 17 = 0.000000`; `GAME-0079`: `0 / 17 = 0.000000`; `GAME-0080`: `0 / 17 = 0.000000`.
- `GAME-0081`: `0 / 18 = 0.000000`; `GAME-0082`: `0 / 18 = 0.000000`; `GAME-0083`: `0 / 18 = 0.000000`; `GAME-0084`: `0 / 20 = 0.000000`.
- `GAME-0085`: `1 / 20 = 0.050000`; `GAME-0086`: `0 / 23 = 0.000000`; `GAME-0087`: `1 / 19 = 0.052632`; `GAME-0088`: `0 / 19 = 0.000000`.
- `GAME-0089`: `0 / 19 = 0.000000`; `GAME-0090`: `1 / 24 = 0.041667`; `GAME-0091`: `3 / 16 = 0.187500`; `GAME-0092`: `1 / 19 = 0.052632`.
- `GAME-0093`: `1 / 18 = 0.055556`; `GAME-0094`: `2 / 18 = 0.111111`; `GAME-0095`: `2 / 20 = 0.100000`; `GAME-0096`: `2 / 18 = 0.111111`.
- `GAME-0097`: `3 / 15 = 0.200000`; `GAME-0098`: `3 / 14 = 0.214286`; `GAME-0099`: `1 / 17 = 0.058824`; `GAME-0100`: `1 / 20 = 0.050000`.
- `GAME-0101`: `1 / 19 = 0.052632`; `GAME-0102`: `0 / 17 = 0.000000`; `GAME-0103`: `0 / 19 = 0.000000`; `GAME-0104`: `2 / 17 = 0.117647`.

- New genes: `ACT-107`, `SYS-140`, `SYS-141`, `CON-159`, `INF-055`, `TIM-016`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: the corpus already represented navigation, addressed
  mechanism activation, live world progression and reaching a location. It
  lacked dialogue-acquired operational facts, a reset partition that preserves
  knowledge, fact-authorised access after reset, explicit post-reset knowledge
  acknowledgement and a fixed live loop boundary.

## Taxonomy impact

- Registry changes: six Active IDs and four transfers to a new game.
- Taxonomy-change record: none; no earlier boundary is merged or retired.
- Candidate terms affected: knowledge persistence, reset partitions and learned
  credentials recorded in `CANDIDATE_TERMS.md`.

## Negative results

- `ACT-106` rejected: the player does not enter this credential as a stationary
  cardinal sequence.
- `SYS-139` rejected: the lift checks learned-code state rather than buffering
  and matching a manually entered directional code.
- `SYS-061` rejected: the mechanism does not rescale a carried object.
- `TIM-006` rejected: the player can keep acting throughout the live world cycle.
- Inventory-key and permanent-open-door models rejected: physical mechanisms
  reset, while the learned fact is what crosses the loop boundary.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Після спарювання зі статуєю смерть або
  наднова скидає фізичний стан світу, але коди запуску лишаються доступним
  знанням і повторно відкривають ліфт без відвідин Горнфелс (`OWI-003`–`OWI-006`).

## Нові гени

- [Observation | Corroborated | High] `ACT-107` — набути робочий факт через
  діалог; `SYS-140` — скинути світ і тіло зі збереженням вивчених фактів.
- [Observation | Corroborated | High] `SYS-141` — авторизувати механізм знаним
  фактом; `CON-159` — не вимагати повторного набуття коду в поточному циклі.
- [Observation | Corroborated | High] `INF-055` — явно показати збережений факт
  після reset; `TIM-016` — завершити фіксований живий цикл скиданням.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0105` — перенести вивчений код крізь
  фізичне скидання світу й використати його для повторної авторизації ліфта.

## Зміни таксономії

- Не потрібні: шість нових меж додаються без зміни чинних визначень; чотири
  наявні гени отримують нового носія.
