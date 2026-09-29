---
game_id: GAME-0442
slug: lumines-puzzle-fusion
game_title: 'Lumines: Puzzle Fusion'
analysis_status: reviewed
reviewed: 2026-09-28
combination_ids: []
gene_ids:
  action:
    - ACT-005
    - ACT-006
  system:
    - SYS-004
    - SYS-006
    - SYS-009
    - SYS-1157
    - SYS-1158
    - SYS-1159
  constraint:
    - CON-001
    - CON-007
    - CON-008
    - CON-716
  information:
    - INF-001
    - INF-005
  objective:
    - OBJ-002
    - OBJ-003
  time:
    - TIM-003
---

# Game: Lumines: Puzzle Fusion — one original PSP Single Skin session

Use the [canonical vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Orange/white appearance, a particular song and exact score coefficients are skin parameters, not separate genes.

## Analysis scope

- Version / ruleset: original North American English *Lumines: Puzzle Fusion* on PlayStation Portable, released 24 March 2005; solo Single Skin mode using the initially unlocked `Shinin'` skin. This is not the 2006 PS2 *Lumines Plus*, 2018 *Lumines Remastered*, or later *Lumines Arise* ruleset. The exact UMD revision was not inspected.
- Primary decision loop: inspect the occupied field and incoming two-colour 2 × 2 block, choose a lateral position and rotation during automatic descent, optionally accelerate the drop, then let its two columns settle. Form at least one monochrome 2 × 2 square; the music-paced line clears qualifying cells when it reaches them, dropping unsupported cells and giving space and score before the next decisions.
- Entry: select the already unlocked `Shinin'` skin in Single Skin mode with an empty field and ordinary controls. The selected skin remains fixed for the session; Challenge unlock progression is outside this packet.
- Positive local result: clear at least one formed monochrome square with the next sweep and increase the score while keeping room for subsequent blocks. This is a repeatable local success, not a finite win of Single Skin.
- Terminal: a new block cannot enter/settle without exceeding the field top; the score is then evaluated. Single Skin has no fixed Time Attack countdown.
- Included: two-colour 2 × 2 incoming blocks, movement and rotation, faster down input, random/variable successor patterns, automatic descent, independent two-column support at an uneven landing, a finite 16 × 10 field, 2 × 2 monochrome qualifying shape, visible sweep position, delayed music-line clear and resulting fall, an occasional special over-block clearing touching same-colour cells once part of a qualifying square, score and top-out.
- Excluded: Challenge skin changes and unlocks, Puzzle Mode target silhouettes and timer, Time Attack, local/CPU versus, character unlocks, exact random-piece distribution, exact score multipliers or sweep-frame timing, later Burst mechanics, and audiovisual decoration that does not change a decision. The `Shinin'` skin fixes music and colour for this packet; its roughly three-second sweep reported by a contemporary guide is not asserted as an exact measured constant.
- Reproducible parameterisation: on an original North American UMD, choose Single Skin → `Shinin'`; move and rotate falling 2 × 2 blocks to produce four adjacent orange cells in a 2 × 2 footprint, observe that they remain until the next visible line passes, then observe clearing, score and falling cells. Continue until top-out. This is a source-based procedure, not a claim that an original UMD was run here.
- Potential scoped modules: Challenge's successive skins, Puzzle Mode's authored shapes, Time Attack deadlines and versus territory exchange.
- Direct-play status: no original PSP, UMD, gameplay capture, video or audio was inspected or played here. Two first-hand written original-PSP guides, a published formal analysis and the series owner's historical page bound the reconstruction. The illustration is original interpretive art, not a screenshot.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `LUM-001` | The original PSP release has an initially available `Shinin'` skin and a separate Single Skin mode that keeps one skin until top-out. | Observation | Corroborated | High | P1, P2, P3 |
| `LUM-002` | Four same-colour cells in a 2 × 2 footprint qualify, but remain until the left-to-right music line reaches them. | Observation | Corroborated | High | P2, P3, A1 |
| `LUM-003` | A falling 2 × 2 block can be moved, rotated and accelerated downward; its two columns may settle at different heights on an uneven stack. | Observation | Corroborated | High | P2, P3, A1 |
| `LUM-004` | A special marked cell in a formed square extends the clear to touching cells of its colour. | Observation | Corroborated | Medium | P2, P3 |
| `LUM-005` | The original playfield has 16 columns and 10 rows, a visible incoming-piece preview and a top-out loss boundary. | Observation | Corroborated | High | P2, P3, A1 |
| `LUM-006` | The official series history identifies the first PSP title as the 2004 Japanese / 2005 North American release; later editions must not be silently substituted. | Confirmed | Direct | High | P1 |

## Basic data

- Release / origin: Q Entertainment and Bandai's first PSP *Lumines* launched in Japan in December 2004; the analysed English North American release appeared 24 March 2005. The owner's historical page identifies both dates; a particular disc revision was not determined.
- Platform or physical form: original PSP UMD with directional pad and face/shoulder controls, selected single-player skin.
- Mechanical families: matching and combination (`FAM-004`) for 2 × 2 same-colour formation and delayed clear; real-time system pressure (`FAM-010`) for falling input and line timing.
- **P1:** [Lumines series owner, original-game history](https://lumines.game/history/), accessed 2026-09-28. Primary release/edition evidence, not an original-mode rules manual.
- **P2:** [Tightning, original PSP first-hand guide](https://gamefaqs.gamespot.com/psp/924594-lumines/faqs/35465), updated 5 April 2005, accessed 2026-09-28. Describes Single Skin, `Shinin'`, control, delayed Music Bar, special Over block and top-out. Its optional-mode timer sentence is not imported into Single Skin.
- **P3:** [sp0rtsfan, original PSP first-hand guide](https://gamefaqs.gamespot.com/psp/924594-lumines/faqs/36468), updated 9 August 2005, accessed 2026-09-28. Independent corroboration of controls, 2 × 2 formations, special block, Single Skin and top-out.
- **A1:** [*Lumines Strategies*, published formal analysis](https://www.researchgate.net/publication/225333916_LUMINESStrategies), accessed 2026-09-28. Analytic account of the 16 × 10 field, three-piece preview, independently settling two-cell columns and sweep-line timing. Its simplified model is not treated as a complete original executable specification.
- Claim IDs: `LUM-001`–`LUM-006`.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-005` for moving or rotating the active falling two-colour 2 × 2 block. Reuse `ACT-006` for holding down to speed its descent without changing its direction (`LUM-003`). The particular control mapping is a parameter.

### System Behaviour Genes

- Reuse `SYS-004` for variable incoming block-pattern selection, `SYS-006` for automatic descent and `SYS-009` for bringing in the next block after the prior one settles. No exact random distribution is inferred.
- Add `SYS-1159`: on an uneven surface, each two-cell vertical column of the falling block continues to its own support rather than the whole four-cell unit locking rigidly. A column cannot hang in midair (`LUM-003`). This rejects Tetris-specific `SYS-007` for whole-piece locking.
- Add `SYS-1157`: formed same-colour 2 × 2 or larger regions wait for the rhythm-linked line, which removes them only as it passes and allows remaining cells to fall (`LUM-002`). This is not immediate completed-row deletion `SYS-008`.
- Add `SYS-1158`: a marked over-block incorporated in a qualifying same-colour square extends that clear to adjacent connected cells of its colour (`LUM-004`). Its colour and graphic marker are parameters.
- Order: introduce block → gravity and chosen movement/drop → independent column settlement → recognise same-colour square → line reaches and clears it (possibly with the special-cell extension) → unsupported cells settle → score/capacity update → next block or top-out. Line motion can continue during block placement.

### Constraint Genes

- Reuse `CON-001` for the finite 16 × 10 addressed field, `CON-007` for collision-valid pre-settlement movement/rotation, and `CON-008` for terminal top obstruction.
- Add `CON-716`: four same-colour cells must occupy an orthogonally aligned 2 × 2 square before they are eligible for the ordinary sweep clear. Mere adjacency or a complete horizontal row does not suffice (`LUM-002`).

### Information Genes

- Reuse `INF-001` for the current field, active piece, marked squares and visible moving line. Reuse `INF-005` for the ordered successor preview; the formal analysis reports a three-block horizon, unlike Tetris's one (`LUM-005`). Hidden later draws are not fully known.

### Objective Genes

- Reuse `OBJ-002` for improving score by cleared squares and `OBJ-003` for preserving board capacity and further legal placements. Single Skin has no finite completion target; clearing one square is the local repeatable goal, not a separate global victory.

### Time Genes

- Reuse `TIM-003`: the falling block and music-linked line continue moving while the player acts. The selected skin's beat changes the sweep cadence parameter, not the time gene. Do not add a fixed Time Attack deadline to this mode.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Active 2 × 2 block above open cells | Move sideways or rotate before landing | Its pose changes while gravity continues | direct control during live descent | `LUM-003` |
| Active block above columns of unequal height | Let it land | The supported two-cell column stops; the other can continue downward | independent column settlement, not rigid whole-piece lock | `LUM-003` |
| Four same-colour cells occupy one 2 × 2 footprint | Let the block settle before line arrival | The square becomes clear-eligible but remains occupied | matching gate is not immediate deletion | `LUM-002` |
| Formed square remains ahead of moving line | Wait for line to reach its columns | Square cells disappear; unsupported cells fall and score increases | music-paced delayed clear | `LUM-002` |
| Special marked cell belongs to a formed same-colour square | Wait for qualifying sweep | Touching same-colour cells are cleared with it | marked-cell extension | `LUM-004` |
| Settled stack blocks incoming space at field top | Permit the next spawn/placement attempt | Session ends and score remains | top-out rather than fixed-time expiry | `LUM-005` |

## Strategic and experiential structure

- Local: choose a pose that creates a 2 × 2 same-colour square rather than merely filling a row. The line's current location determines how long the square waits and whether further cells can be added before clearing.
- Medium term: use the visible successor sequence and the independently falling columns to build flat, accessible colour regions while avoiding unsupported guesses about unseen later pieces.
- Long term: improve score without filling the finite height faster than delayed clears restore space. The fixed `Shinin'` skin links a repeating line cadence to visual and sound feedback but has no Challenge skin ladder.
- Failure attribution: a square may be correctly formed yet still occupy capacity until the next line pass; top-out is not proof that the match was invalid.

## Replay and variation

Incoming pattern order, line phase at placement, column heights and optional marked cells vary the same session loop. No exact probability or score formula is asserted. Different skins or modes could alter tempo or objectives, but they are not silently merged into this packet.

## Adjacent systems and history

NES *Tetris* (`GAME-0004`) shares falling-piece control, gravity, preview, score and top-out, but locks the tetromino rigidly and removes completed horizontal rows immediately after lock. This original PSP game instead allows two-column settling and defers same-colour square removal to the music line. Later *Lumines* editions preserve a family resemblance but have separate mechanics outside this analysis.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-005`, `ACT-006` | move/rotate one 2 × 2 block; faster downward input |
| System Behaviour | `SYS-004`, `SYS-006`, `SYS-009`, `SYS-1157`, `SYS-1158`, `SYS-1159` | incoming variation, gravity, column settlement and music-line clear |
| Constraint | `CON-001`, `CON-007`, `CON-008`, `CON-716` | 16 × 10 field, collision, top-out and same-colour square |
| Information | `INF-001`, `INF-005` | visible field/line and ordered short preview |
| Objective | `OBJ-002`, `OBJ-003` | score and continued placement |
| Time | `TIM-003` | live falling and sweep |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `441` (`GAME-0001`–`GAME-0441`).
- Exact genome matches: none.
- Tied near matches: `GAME-0004` — Tetris (`13 / 19 = 0.684211`).
- Supported combination subsets: none.
- Scan date: 2026-09-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0004` Tetris | `ACT-005`, `ACT-006`, `SYS-004`, `SYS-006`, `SYS-009`, `CON-001`, `CON-007`, `CON-008`, `INF-001`, `INF-005`, `OBJ-002`, `OBJ-003`, `TIM-003` | Both offer falling-piece pose control, a bounded field, preview, score and top-out. Tetris locks one rigid tetromino and deletes a full row immediately after lock; Lumines can settle its two columns separately and needs a same-colour 2 × 2 square that stays occupied until the music line reaches it. The Over block can widen that delayed clear. | Sole tied-near maximum, not exact (`13 / 19 = 0.684211`). |

## Taxonomy impact

`TAXONOMY_CHANGE_179` admits four boundaries: delayed music-line clear, marked-cell extension, two-column landing and monochrome-square eligibility. Earlier signatures and verified combinations do not change.

## Negative results

- `SYS-007` and `SYS-008` encode rigid whole-piece locking and immediate completed-line deletion in NES Tetris; neither describes the two-column settlement and delayed square sweep here.
- The three-piece preview does not make the entire future pattern stream visible; `INF-005` covers only the displayed horizon.
- Single Skin has no fixed Time Attack timer; no separate deadline gene is warranted.
- Exact PSP UMD revision, random-pattern weights, marked-cell frequency and score formula were not measured.

## Delta summary

## New facts

- [Observation | Corroborated | High] The original PSP Single Skin loop delays a qualifying square's clear until the line reaches it (`LUM-001`–`LUM-003`).

## New genes

- [Observation | Corroborated | High] Four typed boundaries in `TAXONOMY_CHANGE_179` distinguish Lumines from a superficial Tetris match.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed; proper-subset support is recomputed in the comparison section.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_179`; no older signature is edited.

## New questions

- Would a preserved North American UMD trace refine column-split timing, special-cell probability or scoring without changing these four causal boundaries?

## Next game

`GAME-0443` *Time Crisis* is the next recorded unit, after this unit's acceptance and the Goal stop window. No push, public publication or deployment is authorised.
