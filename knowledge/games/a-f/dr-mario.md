---
game_id: GAME-0452
slug: dr-mario
game_title: Dr. Mario
analysis_status: reviewed
reviewed: 2026-09-30
combination_ids: []
gene_ids:
  action:
    - ACT-005
    - ACT-006
  system:
    - SYS-004
    - SYS-006
    - SYS-007
    - SYS-009
    - SYS-010
    - SYS-011
    - SYS-012
    - SYS-1187
  constraint:
    - CON-001
    - CON-007
    - CON-008
    - CON-729
  information:
    - INF-001
    - INF-005
  objective:
    - OBJ-002
    - OBJ-007
  time:
    - TIM-003
---

# Game: Dr. Mario — original NES single-player bottle

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Colour, match length, bottle dimensions, selected level, falling speed and score amounts are parameters, not separate genes.

## Analysis scope

- Version / ruleset: Nintendo's original 1990 English NES cartridge rules, one `1 PLAYER GAME` bottle beginning at `VIRUS LEVEL 5`, `SPEED MED`, with the ordinary next-capsule display. The contemporary NES-VU-USA booklet is authoritative; Nintendo's later NES Classic manual and original-game historical page corroborate it. No cartridge revision, NTSC frame trace or exact random seed was inspected.
- Primary decision loop: inspect the fixed viruses, settled capsules and displayed successor; move or rotate the currently falling two-half capsule, optionally accelerate it, then let it lock. Same-colour horizontal or vertical runs clear, an unmatched capsule half separates from its erased partner, unsupported capsule components fall, and newly formed matches resolve without another command. Choose the next placement to remove every virus without blocking the bottle entrance.
- Entry and exit: select the single-player mode and the stated settings, press Start, and begin at the first controllable capsule above the initial virus field. Positive exit is removal of the last virus and the stage-clear transition; the next bottle is outside this packet. Filling the neck ends the attempt. Score evaluates virus removals but is not a substitute for clearing the virus set.
- Included: one finite 8 × 16 bottle; stationary three-colour virus targets; one active paired capsule; lateral movement, both rotations and faster downward input; live gravity and blocked-descent locking; same-colour line removal; capsule bonds and surviving-half separation; vacancy collapse and cascades; variable initial arrangement and incoming colour pairs; one-successor preview, remaining-virus and score display; virus scoring, ordinary speed increase after each ten capsules, pause/resume, stage clear and neck obstruction.
- Excluded: the two-player race, crowns and opponent garbage; Game Boy monochrome rules; SNES, Nintendo 64, Dr. Luigi, Miracle Cure, World and other later modes or skills; touchscreen dragging; hold, hard drop, ghost landing and an unlimited preview; campaign/ending optimisation; music as a decision rule; exact rotation collision exceptions, random weights, frame timing, score implementation defects, save states, cheats and glitches. A separately bounded versus bottle is a potential future module.
- Direct-play status: no cartridge, ROM, executable, live play, input recording, save or video was inspected. The original manual's printed pp. 7–9 were visually reviewed, including its capsule-separation/cascade and screen diagrams; these are source illustrations, not an executed trace. Nintendo's patent embodiment corroborates the algorithmic distinction, but neither its claims nor later reissue documentation establish byte-for-byte retail equivalence. Exact timing and successful execution remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DM-001` | The original NES single-player bottle accepts moved/rotated two-half capsules, faster down input and pause; level and speed are chosen before entry. | Observation | Corroborated | High | P1, P2, P3 |
| `DM-002` | Four or more contiguous same-colour capsule halves and/or viruses in a horizontal or vertical line clear; a differently coloured adjacent virus remains. | Observation | Corroborated | High | P1, P2, P3 |
| `DM-003` | Removing one capsule half leaves its surviving partner separate; unsupported capsules fall and a new alignment can clear without another placement. | Observation | Corroborated | High | P1, P3, P4 |
| `DM-004` | Viruses remain fixed at their established cells until matched away; their targets do not fall into capsule vacancies. | Observation | Corroborated | High | P1, P4 |
| `DM-005` | The field has bounded addressed capacity, visible current occupancy and one displayed successor; clearing the last virus advances the stage, while a blocked neck ends play. | Observation | Corroborated | High | P1, P2, P4 |
| `DM-006` | Virus removals award speed- and simultaneous-removal-dependent score, and capsule descent grows faster after every ten capsules. | Observation | Direct | High | P1 |
| `DM-007` | Nintendo's described embodiment uses random-data selection for initial virus types/positions and capsule pairs; exact retail distribution and seeds are not established here. | Observation | Limited | Medium | P4 |
| `DM-008` | This is a source-led reconstruction, not direct play, and the patent embodiment cannot prove every retail implementation edge. | Confirmed | Direct | High | source-review boundary |

## Basic data

- Origin: Nintendo's 1990 *Dr. Mario*. The original NES/Famicom title, not a later same-name compilation, defines this analysis.
- Analysis target: `PLAT-NES`, English NES cartridge single-player rules. Known-release audit remains not started; no port equivalence or current purchase claim is made.
- Mechanical families: `FAM-004` for colour-conditioned removal and `FAM-010` for placement during forced descent.
- **P1:** [Nintendo's contemporary NES-VU-USA instruction booklet](https://www.gamingalexandria.com/highquality/NES/Dr.%20Mario/Dr.%20Mario%20-%20Manual.pdf), checked 2026-09-30. Printed pp. 4–10 cover controls, settings, six pair types, three virus colours, match examples, a falling-survivor cascade, next capsule, stage outcome, scoring and speed growth. The scan contains sixteen PDF pages; printed pp. 7–9 were also inspected visually rather than relying on damaged OCR. Printed p. 11 is the expressly excluded versus packet.
- **P2:** [Nintendo's NES Classic Dr. Mario manual](https://www.nintendo.co.jp/clv/manuals/en/pdf/CLV-P-NAAXE_en.pdf), checked 2026-09-30. Later first-party corroboration of original-game controls, four-or-more matching, one successor and single-bottle outcome. Reissue controls do not establish an original executable revision.
- **P3:** [Nintendo's original Famicom game history/rules page](https://www.nintendo.com/jp/famicom/software/hvc-vu/index.html), checked 2026-09-30. Its reproduced period instructions explicitly show surviving capsules falling, then another column disappearing; the page also separates single-player and versus and notes ten-capsule speed growth. Regional text is corroboration, not a regional frame-equivalence assertion.
- **P4:** [Nintendo-authored US5265888A, described capsule/virus embodiment](https://patents.google.com/patent/US5265888A/en), checked 2026-09-30. Description of registers/buffer and Fig. 9A–9B, steps 41–58: 16 × 8 addressed buffer, initial random-data placement, active capsule fixation, half reshaping, unsupported-component falls and repeated alignment tests. This is primary design documentation, not a disassembly or direct retail measurement. Only mechanics consistent with the booklet are corroborated; random-selection detail remains Limited / Medium. No legal or originality conclusion is drawn from a patent.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-005`: move or rotate the one current falling capsule before fixation. A/B select opposite quarter turns; two cell colours and horizontal/vertical orientations are parameters.
- Reuse `ACT-006`: down temporarily accelerates the same downward process. This is not an instantaneous hard drop or changing the setup speed during play (`DM-001`).

### System Behaviour Genes

- Reuse `SYS-004` for variable pair and initial-field selection, with the explicit P4 evidence limitation. No seven-bag, uniform distribution or exact sequence is inferred.
- Reuse `SYS-006` for periodic descent; its existing acceleration-schedule parameter admits the booklet's ten-capsule speed growth. Reuse `SYS-007` for the active pair becoming settled occupancy on blocked descent, and `SYS-009` for introduction of the next active pair after stable resolution.
- Reuse `SYS-010`: automatic qualifying same-colour pattern removal. Four rather than three and line orientation belong to its declared minimum-size/geometry parameters; it is not Tetris's full-width occupancy-row `SYS-008`.
- Reuse `SYS-011`: unsupported eligible capsule components fall into reachable vacancies. Retained whole pairs fall as connected components, not as independently settling Lumines columns; fixed viruses are ineligible by `CON-729`.
- Reuse `SYS-012`: repeat match detection and eligible falls until stable, without another paid placement. No replacement items refill every cleared cell.
- Add `SYS-1187`: if a match deletes one half of a bonded capsule, break the bond and retain the unmatched half as a separate movable unit. Merely losing external support does not split an intact pair. This changes later support and reachability, not just the drawn shape (`DM-003`).
- Order: active input/gravity → blocked descent fixes pair → qualifying lines remove eligible cells → deleted-half bonds break → unsupported eligible capsule components settle → detect further matches and repeat → credit virus removals/check stage result → introduce successor or fail at obstructed entry. No exact animation/frame ordering or scoring edge is asserted.

### Constraint Genes

- Reuse `CON-001` for finite addressed bottle capacity, `CON-007` for collision-valid active capsule transformations, and `CON-008` for terminal obstruction of required entry.
- Add `CON-729`: a virus target's settled cell is exempt from vacancy-driven descent and direct capsule relocation. It stays there until a qualifying same-colour removal affects it, even if empty space opens below. This eligibility boundary prevents treating every coloured occupant as a movable capsule (`DM-004`).
- Accessible entry and approach to a target colour are scarce spatial resources. An isolated gap or an awkward colour is not automatically an irrecoverable deadlock; unlimited later placement and clears may repair it.

### Information Genes

- Reuse `INF-001` for the visible bottle, capsule halves/bonds, virus colours, current piece, remaining-virus count, speed and score. Reuse `INF-005` for the one announced successor. Later pairs are outside that preview horizon; do not also claim `INF-002` for that same already displayed next pair (`DM-005`).

### Objective Genes

- Reuse `OBJ-007` for eliminating the entire declared virus set. Residual capsule cells need not all be removed when the last virus disappears.
- Reuse `OBJ-002` for the independently displayed virus-removal score. The manual's speed/multiple-removal table is an evaluation parameter, not six new reward genes. Merely clearing capsule-only lines earns no virus points; a high score cannot replace the required target clearance (`DM-005`, `DM-006`).

### Time Genes

- Reuse `TIM-003`: input occurs during forced descent, not on an unlimited planning turn. Ordinary pause/resume suspends the loop; pause-assisted optimisation is not analysed. No fixed overall bottle deadline is evidenced (`DM-001`, `DM-006`).

## Reproducible transitions

| Before | Action/event | Source-derived resolution | Boundary | Claim ID |
|---|---|---|---|---|
| One active two-half pair above space | Move/rotate or hold down | Permitted pose changes or faster descent occur before settlement | Player pose/rate versus automatic descent | `DM-001` |
| A supported pair completes a vertical run of three capsule halves plus one same-colour virus | Let it settle | Four matched cells disappear, including the virus | Target-inclusive same-colour removal | `DM-002` |
| Four matching capsule halves are adjacent to a differently coloured virus | Complete that horizontal line | Capsule cells disappear; the differently coloured virus remains | Not a full-width or indiscriminate clear | `DM-002` |
| A red-blue pair has its red half in a qualifying red line | Resolve the line | Red half disappears; blue half becomes a separate unit and falls if unsupported | Match-triggered bond loss | `DM-003` |
| A retained intact pair loses all external support | Resolve the first clear | Pair descends while retaining its bond; no invented split from gravity alone | Whole versus severed component | `DM-003` |
| Capsule material below a virus is removed | Resolve eligible falls | Virus stays in its established cell rather than joining the fall | Anchored-target eligibility | `DM-004` |
| A released blue half lands into another qualifying blue column | Wait for resolution | Second line clears without a new player placement | Cascading stable-resolution loop | `DM-003` |
| Last virus belongs to a qualifying line, with other capsule cells left | Resolve the match | Stage clears; a completely empty bottle is unnecessary | Declared target set, not all occupancy | `DM-005` |
| Capsule accumulation obstructs the neck while viruses remain | Continue the incoming-piece cycle | Attempt ends | Entry failure versus merely high stack | `DM-005` |
| Ten more capsules have been introduced | Continue ordinary play | Descent becomes slightly faster | Existing schedule parameter, no exact frame value | `DM-006` |

These are falsifiable source-derived cases, not an executed simulator. A lawful original-cartridge trace would need to test collision/rotation edge cases, intact-pair support, cascade ordering and exact seed/timing before upgrading implementation claims.

## Strategic and experiential structure

Inspect both colours: removing the useful half may release the other into a useful second match or bury access to another virus. Plan around fixed target cells and the one announced successor while keeping the neck free. A capsule-only clear can restore access without directly scoring or completing the stage. Faster descent progressively shortens execution time. These interpretations follow `DM-001`–`DM-007`; they are neither optimality claims nor measured player responses.

## Replay and variation

The described selection process can vary initial target arrangement and incoming pairs. Setup level and speed change pressure, not genome identity. No exact random distribution, fixed seed, fairness guarantee or campaign completion was measured. Stage-level scoring and a clean target clearance can motivate another attempt without importing the opponent's garbage mechanic.

## Adjacent systems and history

Tetris's rigid tetromino and complete occupancy-row shift do not imply Dr. Mario's colour match, stationary targets or severed capsule half. Lumines's independently landing columns and delayed music sweep are absent. Royal Match's match/collapse/cascade boundaries transfer, but adjacent swapping, finite move budget, per-cell random refill and special-element creation do not. The later NES Classic manual is cross-checked against the original booklet, not silently substituted as retail code.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-005`, `ACT-006` | current pair pose, faster descent |
| System Behaviour | `SYS-004`, `SYS-006`, `SYS-007`, `SYS-009`–`SYS-012`, `SYS-1187` | selection, descent schedule, lock, same-colour clear, bond break, eligible fall and cascade |
| Constraint | `CON-001`, `CON-007`, `CON-008`, `CON-729` | capacity, collision, entry, fixed target class |
| Information | `INF-001`, `INF-005` | current bottle and one successor |
| Objective | `OBJ-002`, `OBJ-007` | virus score and complete virus-set removal |
| Time | `TIM-003` | live input with forced descent |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `451` (`GAME-0001`–`GAME-0451`).
- Exact genome matches: none.
- Tied near matches: `GAME-0004` — Tetris (`13 / 21 = 0.619048`).
- Supported combination subsets: none.
- Scan date: 2026-09-30.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0004` Tetris | `ACT-005`, `ACT-006`, `SYS-004`, `SYS-006`, `SYS-007`, `SYS-009`, `CON-001`, `CON-007`, `CON-008`, `INF-001`, `INF-005`, `OBJ-002`, `TIM-003` | Both position one falling element with a preview under finite-capacity entry pressure. Tetris removes a completely occupied row and shifts higher rows; Dr. Mario removes colour runs containing fixed targets, severs an unmatched capsule half and repeats eligible falls/clears until stable. Virus-set clearance ends this bottle even with capsule material left. | Near 0.619048; not exact. |

## Taxonomy impact

`TAXONOMY_CHANGE_189` admits the matched-half bond break and fixed-target fall exemption. Seventeen existing genes transfer without changing earlier definitions, signatures or verified combinations. The named GAME-0452 salience/plain-language review rereads this complete source scope, partitions all nineteen genes and supplies one reviewed bilingual example per use; no weights or frequency-derived roles are inferred.

## Negative results

- No `SYS-008`, `SYS-1159`, music sweep, random refill after every clear, manual settled-half movement, opponent garbage, finite action budget or modern skill is inherited.
- Nintendo's patent supports a design-level process, not a precise ROM revision, legal novelty, fixed random distribution or measured timing. An inaccessible contemporary first-hand guide is not cited as read evidence.

## Delta summary

## New facts

- [Observation | Corroborated | High] Fixed viruses and match-triggered capsule separation alter what can fall and where a later clear can occur (`DM-002`–`DM-004`).

## New genes

- [Observation | Corroborated | High] `SYS-1187` and `CON-729`; other matching/placement/resolution boundaries are reused.

## New combinations

- [Observation | Limited | Medium] No new combination proposed; every current proper subset is checked in the deterministic comparison scan.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_189`; no earlier signature is edited.

## New questions

- Which ordinary rotation/support edge cases and cascade animation timings are corroborated by an exact original-cartridge trace?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0453` *Age of Mythology*, original Windows edition, is next in selection 034 after acceptance and the stop window.
- Optimisation criterion: alternate a falling-colour loop with deity-conditioned live economy/army control.
- Expected information gain: distinguish original deity powers and resource economy from already recorded historical RTS boundaries.
- Backlog impact: seven approved subjects remain; no push, public publication or deployment is authorised.

## Why this game

- [Hypothesis | Limited | Medium] A recognisable NES puzzle tests reusable automatic matching/collapse genes while isolating only the capsule bond and anchored-target differences.
