---
game_id: GAME-0422
slug: patapon
game_title: Patapon
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-560
  system:
    - SYS-1116
    - SYS-1117
  constraint: []
  information:
    - INF-414
  objective:
    - OBJ-181
  time:
    - TIM-003
---

# Game: Patapon — first Patata Plain hunt

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Drum syllables, prey species, formation size and the number of successful calls are parameters, not separate genes.

## Analysis scope

- Version / ruleset: original English-language *Patapon* for PlayStation Portable, as described in Sony Computer Entertainment's contemporary PSP manual; exact UMD revision was not inspected. This packet is the first post-prologue `Hunting on Patata Plain` mission identified by a contemporary original-PSP walkthrough, not the remaster, sequels or the entire campaign.
- Structured analysis target: `PLAT-PLAYSTATION-PORTABLE` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: listen to and watch the live beat; enter one four-beat drum phrase for march or attack; let the Patapon formation answer and move or strike; judge distance to prey and the next beat; keep consecutive valid call-and-response cycles for Fever, then guide surviving Patapons across the mission's goal indicator and return with eligible hunting spoils.
- Entry and exit: after the prologue unlocks the obelisk, choose the first Patata Plain hunt and enter with its available formation and March song; the Attack song is taught at mission start. Positive terminal is crossing that mission's goal indicator with a surviving formation, accepting its completion and retained hunting spoils at Patapolis. Failure from loss of the viable formation does not satisfy the goal; this record does not assert an exact game-over threshold or a mandatory prey-kill count.
- Included: beat-pulsing screen edges, four drum inputs as ordered commands, March and Attack phrases, alternating player call and autonomous formation answer, attack-range cue, prey acquisition and damage, consecutive-combo Fever boost, health and possible member loss, goal crossing, return and acquired meat. The guide's specific boar/bird drops are examples, not prerequisites for exit.
- Excluded: Defend and later songs, Miracles, weather, equipment crafting, Tree of Life creation or revival, exact combo threshold, attack damage, measured input windows, later hunts and battles, boss routes, story ending, multiplayer and remaster timing. Preparing other squad types at headquarters is a potential separate packet, not silently part of this first hunt.
- Potential scoped modules: later defensive-rhythm mission, a fully instrumented Fever-threshold test, and pre-mission army creation/equipment.
- Direct-play status: no PSP, UMD, input log, screenshot, video or audio was inspected. The publisher manual directly states the general commands, combat, Fever, goal and loot rules; the 2008 written guide locates their first-hunt use. This is a bounded source reconstruction, not a frame-perfect play trace.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PTP-001` | Four face buttons act as PATA, PON, CHAKA and DON drums; four-syllable March and Attack patterns direct the army. | Confirmed | Direct | High | P1 |
| `PTP-002` | During a mission the screen edges pulse the beat; the player issues orders on that beat, and the formation performs the corresponding behaviour rather than receiving individually directed strikes. | Confirmed | Direct | High | P1 |
| `PTP-003` | Consecutive successful call-and-response cycles accumulate a combo and produce Fever, improving attack and enabling enhanced actions; the exact threshold is not established here. | Confirmed | Direct | High | P1, P3 |
| `PTP-004` | A goal-indicator mission completes when Patapons cross the line, whereas missions without it require defeating all enemies. The selected first hunt is treated as the former; its exact goal position was not directly viewed. | Observation | Corroborated | Medium | P1, P3, S1 |
| `PTP-005` | The contemporary guide places Attack-song teaching and hunting prey in Mission 1 on Patata Plain and says its meat is available after the mission. | Observation | Corroborated | Medium | P1, S1 |
| `PTP-006` | Neither the exact valid-beat window, Fever combo threshold nor original executable revision is established by this source-only reconstruction. | Observation | Limited | High | P1, S1 |

## Basic data

- Release / origin: Sony Computer Entertainment's original PSP game; Sony announced the North American release for 26 February 2008. The manual is the authority for the scoped rules rather than a later remaster description.
- Platform or physical form: original single-player PSP handheld release, face-button drums and horizontally advancing Patapon formation.
- Mechanical families: real-time system pressure (`FAM-010`) and agent routing and coordination (`FAM-015`).
- Sources accessed 2026-09-27:
  - **P1** — [Sony Computer Entertainment, original *Patapon* PSP instruction manual](https://manuals.plus/m/022be6c58003e45d11649414457926eeb0088f6e624a743a3006b6a45791a966.pdf), English printed pp. 2–8: controls and screen, drum commands, missions, formation, beat cue, goal indicator, health, spoils and Fever. Preserved publisher manual; no game binary was obtained.
  - **P2** — [Sony North American release announcement](https://sony.mediaroom.com/2008-02-26-Patapon-Marches-Its-Way-on-to-PSP-PlayStation-Portable), for publisher, platform and regional release date only.
  - **P3** — [PlayStation producer's *Pata-tips #1*](https://blog.playstation.com/2008/02/29/patapost-friday-pata-tips-1/), 29 February 2008, for explicit reference to Patata Plain as the first hunting level, its finishable route and the chained-command Fever advice. Its approximate six-to-ten successful calls are not treated as a fixed threshold.
  - **S1** — [deathfisaro, original-PSP *Patapon* guide, version 1.7 (2008)](https://gamefaqs.gamespot.com/psp/942065-patapon/faqs/51882), Prologue and Mission 1 sections, for the named entry, Attack-song teaching, prey and retained meat. The guide is not treated as executable telemetry.

## Mechanical decomposition

### Action Genes

- New `ACT-560`: enter the four ordered drum beats for March (`PATA PATA PATA PON`) or Attack (`PON PON PATA PON`) in the current command interval. This chooses an army-level verb, not a teacher's phrase to echo or one individually targeted strike. `PTP-001`, `PTP-002`.

### System Behaviour Genes

- New `SYS-1116`: after a recognised phrase, the formation answers and carries out its corresponding march or attack; the attack depends on target reach and soldiers act without per-member strike inputs. A mistimed or wrong phrase does not establish the intended order. `PTP-001`, `PTP-002`.
- New `SYS-1117`: repeated valid call-and-response cycles accumulate a combo, enter Fever and strengthen the formation's combat response. No exact numerical threshold or multiplier is asserted. `PTP-003`.
- Resolution order: beat cue → player four-drum phrase → recognition and formation answer → movement or prey attack and health/loot effects → successful-cycle combo/Fever update → next phrase or goal crossing. `PTP-001`–`PTP-005`.

### Constraint Genes

- None separately admitted. The four-beat syntax and timing are part of `ACT-560` and its `SYS-1116` recognition; attacking within reach is a parameter of formation response, not a second universal prohibition. `CON-071` is not transferred because it specifies a selectable persistent commander-led squad relocated as a unit, while here one drum phrase addresses the available army.

### Information Genes

- New `INF-414`: pulsating screen edges disclose the beat; the formation/target display and aggressive eye cue disclose an attack opportunity; squad health and rhythm-combo display show continuing risk and progress. Off-screen future prey is not claimed visible. `PTP-002`, `PTP-003`.

### Objective and Time Genes

- Reused `OBJ-181`: cross the first hunt's ordinary goal, accept mission completion, and return to the mission-selectable village with any credited meat retained. Killing every prey or maximising meat is not a prerequisite for this scoped terminal. `PTP-004`, `PTP-005`.
- Reused `TIM-003`: beats and moving actors advance in real time while the next command must be entered during its live interval. `PTP-002`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First hunt begins after obelisk selection | Read the taught Attack pattern and wait for pulsing beat | Available drum syntax and live cadence are disclosed | source-bounded entry | `PTP-001`, `PTP-005` |
| Formation is short of prey | Enter `PATA PATA PATA PON` on four beats | Formation answers and marches forward | command-to-agent response | `PTP-001`, `PTP-002` |
| Prey is within attack reach | Enter `PON PON PATA PON` on four beats | Formation answers with autonomous attacks against reachable prey | range-conditioned combat | `PTP-001`, `PTP-002` |
| Several call/answer cycles succeed consecutively | Continue valid phrases without breaking rhythm | Combo builds and Fever improves fighting; exact threshold remains unknown | accumulated cadence state | `PTP-003`, `PTP-006` |
| Prey is defeated | Continue toward the goal | Eligible spoils may be credited after mission completion | optional retained outcome | `PTP-005` |
| Surviving formation reaches the goal indicator | March across it | Mission closes and returns to Patapolis with eligible spoils | scoped positive terminal | `PTP-004`, `PTP-005` |

## Strategic and experiential structure

- Local decision: choose March to close distance or Attack when prey is reachable, then place every syllable on the beat.
- Medium-term decision: maintain an unbroken call-and-response sequence long enough to benefit from Fever while not advancing out of attack range.
- Long-term structure: first-hunt meat can be used later, but later army construction and the campaign are outside this packet.
- Failure attribution: the pulsing beat, attack-ready eye and combo display give visible feedback, but without a timed trace we do not assign exact frame tolerance or every lost-combo cause.

## Replay and variation

The selected mission is authored; this record does not claim procedural terrain or random prey placement. Performance timing, which prey are defeated, formation health, Fever entry and credited spoils can vary. Replay for more materials is outside the declared first-completion boundary.

## Adjacent systems and history

*PaRappa the Rapper* asks the player to echo a demonstrated phrase for a performance rating; *Patapon* lets the player choose a memorised phrase whose decoded order changes autonomous army behaviour. *DanceDanceRevolution* judges chart-matched floor steps but does not convert four-beat phrases into squad movement or combat. Conventional real-time strategy orders can direct troops, but their command semantics do not depend on a live drum pattern and consecutive musical call/answer Fever.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-560` | March and Attack drum phrases |
| System Behaviour | `SYS-1116`, `SYS-1117` | formation reply and Fever combo |
| Constraint | none | phrase validity belongs to action/response |
| Information | `INF-414` | beat pulse, range cue, health and combo |
| Objective | `OBJ-181` | first hunt goal, village return, eligible meat |
| Time | `TIM-003` | live beat and moving formation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `421` (`GAME-0001`–`GAME-0421`).
- Exact genome matches: none.
- Tied near matches: `GAME-0312` — ASTRO BOT (`2 / 20 = 0.100000`); `GAME-0391` — Uncharted 2: Among Thieves (`1 / 10 = 0.100000`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| ASTRO BOT (`GAME-0312`) | `OBJ-181`, `TIM-003`: a live authored level closes at an ordinary exit and retains eligible optional progress | ASTRO BOT directly steers a jumping body through a 3D rescue route; Patapon chooses rhythmic formation orders, receives autonomous replies and can enter Fever during a side-scrolling hunt (`ACT-560`, `SYS-1116`, `SYS-1117`) | Near, `0.100000` |
| Uncharted 2: Among Thieves (`GAME-0391`) | `TIM-003`: decisions happen while the authored route progresses in real time | Uncharted's opening is embodied escape from a collapsing train; Patapon's player drums group-level march and attack patterns and retains first-hunt spoils | Near, `0.100000` |

## Taxonomy impact

[`TAXONOMY_CHANGE_160`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_160.md) admits one rhythmic army-order Action, two formation/combo System Behaviours and one beat/formation Information gene. Earlier signatures and combinations remain unchanged.

## Negative results

- `ACT-533` and `SYS-1058` rejected: the player chooses a known march/attack command; no instructor first calls each phrase for the player to echo.
- `ACT-545` rejected: these are handheld drum buttons, not chart-matched physical floor steps.
- `SYS-215` rejected: it explicitly excludes autonomous squad engagement; `SYS-1116` resolves the whole-command reply.
- `INF-001` rejected: the next off-screen target is not fully visible before every order.
- Exact Fever threshold, input window, mandatory hunting quota and mission goal position remain unverified without a direct original-PSP trace.

## Delta summary

Four-beat rhythmic commands control an autonomous army's movement and attack. Successful consecutive call/answer cycles strengthen it through Fever. The first hunt ends at an ordinary goal and retains eligible spoils, not at a song score.

## New facts

- [Confirmed | Direct | High] The publisher manual distinguishes the March and Attack drum patterns, the alternating formation response, Fever from successful combos, and goal-indicator completion (`PTP-001`–`PTP-004`).

## New genes

- [Observation | Corroborated | High] `ACT-560`, `SYS-1116`, `SYS-1117` and `INF-414` distinguish rhythmic command input, its autonomous army response, accumulated Fever and the beat/range information surface.

## New combinations

- [Observation | Direct | High] None created; existing verified combinations are tested against this full six-gene signature.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_160` records the four new boundaries without changing an earlier signature.

## New questions

- At what exact timing window and consecutive count does the original UMD enter or leave Fever?
- Does every first-hunt release variant expose the same goal placement and prey pattern?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0423` *Banjo-Kazooie: Nuts & Bolts* after this unit's validation, local commit and Goal stop window.
- Optimisation criterion: move from beat-scheduled group command to assembled vehicle traversal and objective interaction.
- Backlog impact: preserve the approved `GAME-0423`–`GAME-0432` order; do not start another subject in this unit.

## Why this game

- [Hypothesis | Corroborated | Medium] The original PSP manual supplies transferable rhythmic-order and combo-state boundaries not captured by chart-judgement games, while a contemporary first-mission guide makes the packet reproducible.
