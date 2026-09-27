---
game_id: GAME-0428
slug: super-mario-maker
game_title: Super Mario Maker
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-567
    - ACT-568
  system:
    - SYS-036
    - SYS-1129
    - SYS-1130
  constraint:
    - CON-707
  information:
    - INF-001
    - INF-192
  objective:
    - OBJ-247
  time:
    - TIM-002
    - TIM-003
---

# Game: Super Mario Maker — author, test and prove a course

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Course length, chosen blocks, gap, game style and goal position are parameters, not independent genes.

## Analysis scope

- Version / ruleset: Nintendo's original 2015 *Super Mario Maker* for Wii U, launch-era course-making and historical upload-clear rules documented by its official electronic manual. Choose the original *Super Mario Bros.* style and a short ground-theme course with no checkpoint, sub-area, enemies or optional sound elements. Exact installed patch and a particular saved course were not inspected.
- Structured analysis target: `PLAT-NINTENDO-WII-U` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: inspect the editable course grid, palette, start and goal; place or erase a ground element to make a short traversable route; switch directly into trial play of the current layout; run and jump the controlled character across that layout; return to the editor after failure or completion, revise if necessary, save the course in Coursebot, and perform the creator's clear proof required by the historical upload rule.
- Entry and exit: begin in the Wii U GamePad course editor with one short **illustrative** player-authored ground course, start and goal already present and a small route gap to address. End when the authored course has been saved locally and its creator has cleared it for the historical upload eligibility check. This is an analytical completion boundary, not an assertion that such a course was uploaded or that the upload service still works.
- Included: touch placement and erasure of ordinary ground, inspectable editor grid and palette, adjustable goal/course extent as a parameter, direct editor-to-trial toggle, live movement, jumping, gravity and collisions, goal/failure return to editing, Coursebot local save and separate creator clear proof before historical upload.
- Excluded: actual network upload or download, which Nintendo discontinued on 31 March 2021; all Wii U network features, which ended on 8 April 2024; checkpoint proof, sample or other-maker course restrictions beyond the declared original-course condition; later update elements; enemy, power-up, costume, sub-area, sound, scroll-speed and custom time-limit systems; 3DS edition, *Super Mario Maker 2*, competitive course ratings and a whole-course design-quality judgement.
- Potential scoped modules: checkpoint-specific upload proof after the November 2015 update, multiple game styles and their different movement rules, sharing and discovery during the historical online period.
- Direct-play status: no Wii U console, game copy, exact executable, input trace, screenshot, audio or video was inspected. Nintendo's original electronic manual and support instructions directly establish editor, trial, save and upload-proof boundaries. The tiny gap-and-block course is a **constructed analytical example**, not a witnessed course or a claim of a tested geometry. Exact motion and collision values are unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SMM-001` | Wii U GamePad touch editing places and erases course elements from a palette; the start and goal and course length are adjustable. | Confirmed | Direct | High | P1 |
| `SMM-002` | One touch changes the current edited course into playable trial mode, and completion or loss returns the player to editing. | Confirmed | Direct | High | P1 |
| `SMM-003` | The editor offers four game styles, including original *Super Mario Bros.*; this packet chooses that style without asserting every style's exact physics. | Confirmed | Direct | High | P1 |
| `SMM-004` | Created courses can be saved into Coursebot and subsequently loaded or played; saving is distinct from uploading. | Confirmed | Direct | High | P1, P2 |
| `SMM-005` | Under the historical upload rule, the creator had to demonstrate that a saved, own-authored course could be cleared before upload. Ordinary trial play alone is not equivalent to that separate proof. | Confirmed | Direct | High | P1, P3 |
| `SMM-006` | Wii U upload closed on 31 March 2021 and remaining Wii U online communication ended on 8 April 2024; the historical proof is analysed as a rule, not a currently usable service. | Confirmed | Direct | High | P4 |
| `SMM-007` | A short edited ground route, a trial run and a creator clear check together form an illustrative bounded packet. No exact saved layout or resulting clear was observed. | Hypothesis | Limited | Medium | P1–P3 |

## Basic data

- Release / origin: Nintendo's 2015 Wii U original, not its later 3DS adaptation or Switch sequel.
- Platform or physical form: Wii U GamePad touch editor followed by directly controlled side-view platform play.
- Mechanical families: route and network construction (`FAM-005`) and ordered dependency sequencing (`FAM-017`). The layout must be authored, tested and saved before its historical clear-proof gate matters.
- Primary sources, accessed 2026-09-27: **P1** — [Nintendo's original electronic manual, Create](https://microsite.nintendo-europe.com/super-mario-maker-manual/enGB/page_01.html), GamePad editor, palette, four styles, start/goal, trial mode and save; **P2** — [Nintendo support, saving a created course](https://en-americas-support.nintendo.com/app/answers/detail/a_id/15180/c/950), Coursebot save slot and name; **P3** — [Nintendo's manual, Upload](https://microsite.nintendo-europe.com/super-mario-maker-manual/enGB/page_05.html), saved-course prerequisite and creator clear proof; **P4** — [Nintendo support, Wii U service discontinuations](https://en-americas-support.nintendo.com/app/answers/detail/a_id/53854/p/603), 2021 upload and 2024 online shutdown dates.
- No secondary or direct-play source was used to assert precise geometry, time, failure count or checkpoint behaviour.

## Mechanical decomposition

### Action Genes

- Reused `ACT-008`: steer the character by running and jumping across the current authored course **during trial/clear play**, not while dragging editor pieces. `SMM-002`.
- New `ACT-567`: choose one editor-palette ground element, place it on the visible course grid or erase a placed element without consuming a live play resource. This is distinct from Minecraft Survival's held-item, reach- and material-bound `ACT-162`. `SMM-001`.
- New `ACT-568`: deliberately switch the **current edited layout** into direct trial play and back, rather than selecting a different game or merely pausing a live run. `SMM-002`.

### System Behaviour Genes

- Reused `SYS-036`: the directly controlled body follows continuous gravity, jump and collision dynamics in trial play; exact style-specific constants are not asserted. `SMM-002`, `SMM-003`.
- New `SYS-1129`: the editor's current placement state becomes the immediately playable collision/route layout; a trial clear or loss returns to the editor where that layout can be revised. A test from the middle is not asserted to satisfy the separate historical upload proof. `SMM-001`, `SMM-002`, `SMM-005`.
- New `SYS-1130`: an explicit Coursebot save stores a named, reloadable local course slot rather than automatically publishing it. `SMM-004`.
- Resolution order: inspect grid and available ground → place/revise tile → trial play current layout → return to edit on success or loss → save own course → prove a complete clear for historical upload eligibility. `SMM-001`–`SMM-005`.

### Constraint Genes

- New `CON-707`: historical upload acceptance requires that the saved course be the maker's own eligible course and that the maker demonstrate a clear. This is an upload gate, **not** a prerequisite for local save or ordinary trial play; upload is now discontinued. `SMM-004`–`SMM-006`.

### Information Genes

- Reused `INF-001`: the player can inspect the current course grid, placed elements, palette and start/goal by viewing or panning the editor; this does not reveal a hidden future outcome. `SMM-001`.
- Reused `INF-192`: live trial play exposes a local side-scrolling route slice, not the entire editor canvas at once. `SMM-002`.

### Objective and Time Genes

- New `OBJ-247`: close the bounded maker packet with an own-authored locally saved course and the creator's demonstrated full clear under the historical upload-check rule. This is not actual network distribution. `SMM-004`–`SMM-006`.
- Reused `TIM-002`: editor placements and revisions are self-paced; no running hostile or deadline changes the course while the player deliberates. `SMM-001`.
- Reused `TIM-003`: once in trial/clear play, movement, gravity and collision advance while the player steers the character. `SMM-002`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| The short illustrative route has a small gap | Choose a ground element and place it at the intended course cell | The edited layout now contains that element; no live Mario movement has yet occurred | authoring changes spatial state, not a current run | `SMM-001`, `SMM-007` |
| Current grid is editable | Enter Trial Play | The same current layout becomes a playable side-view course | no export or separate build step is required for local test | `SMM-002` |
| Character is at the start of the trial | Run or jump toward the goal across the placed terrain | Gravity and collision determine the traversable route; reaching the goal finishes the trial | playing tests the authored geometry rather than dragging tiles through live play | `SMM-002`, `SMM-007` |
| Trial ends by goal or loss | Return to the editor, alter a troublesome cell if needed | The layout is again editable for another trial | failed trial is feedback, not permanent course loss | `SMM-002` |
| Own course has a chosen layout | Save to Coursebot in a named slot | The course is retained locally and may be loaded again | local persistence is distinct from online sharing | `SMM-004` |
| Saved own course has not passed a creator clear check | Try the historical Upload path | Creator must prove a complete clear before the upload gate could pass | ordinary save or mid-course trial is insufficient for historical publishing | `SMM-005`, `SMM-006` |

## Strategic and experiential structure

- Local decision: decide which visible ground cell to change and whether to trial immediately or keep editing.
- Medium-term planning: compare the traversable play route with the editor arrangement; revise after a failed test, then save a stable version.
- Long-term structure: the historical clear gate made publication depend on the maker's own ability to traverse the finished course. Current local play and save remain analytically distinct from unavailable online upload.
- Common heuristic: test the path in playable mode before naming and retaining it; do not infer that attractive geometry is traversable merely from the editor view.
- Failure attribution: an inaccessible goal or failed jump calls for route revision, while a saved course lacking creator proof is not historically upload-eligible. The available sources do not determine the exact tolerable gap width in the illustrative example.
- Player-trust factors: visible editing, immediate play switching and a separate clear requirement expose what has been authored, what has been tested and what would historically qualify for sharing.

## Replay and variation

The maker can alter ground placement, course extent and trial route. No procedural generation or fixed optimal layout is asserted. The scoped example deliberately omits enemies, styles beyond its chosen one and post-launch checkpoint rules.

## Adjacent systems and history

*Super Mario Bros.* shares directly controlled side-view movement but has fixed developer-authored World 1-1 terrain; *Super Mario Maker* makes course geometry the player's editable input before testing. *LittleBigPlanet 2* also includes authoring in the marketed product, but its currently canonical packet is a story-level run, not its creator tools. A fixed machine build/test cycle (`TIM-006`) is not this reversible editor-to-direct-play mode switch.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-567`, `ACT-568` | directly controlled run/jump; touch placement/erasure; trial toggle |
| System Behaviour | `SYS-036`, `SYS-1129`, `SYS-1130` | live gravity/collision; current-layout test; named Coursebot slot |
| Constraint | `CON-707` | own saved course and creator clear for historical upload |
| Information | `INF-001`, `INF-192` | inspectable editor; local live viewport |
| Objective | `OBJ-247` | locally saved and creator-cleared example |
| Time | `TIM-002`, `TIM-003` | self-paced edit, live trial |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `427` (`GAME-0001`–`GAME-0427`).
- Exact genome matches: none.
- Tied near matches: `GAME-0112` — Human: Fall Flat (`4 / 16 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0112` *Human: Fall Flat* | `ACT-008` direct movement, `SYS-036` continuous body physics, `INF-001` inspectable present arrangement and `TIM-003` live input | *Human: Fall Flat* moves a ragdoll, grips and carries a crate through a fixed 3D room to its exit. *Super Mario Maker* edits the course geometry itself on a self-paced GamePad grid, trial-plays that current layout, saves it as a named local course and separates the historical author-clear proof from ordinary play. | Tied-near maximum, `0.250000`; not exact or a verified combination match. |

## Taxonomy impact

[`TAXONOMY_CHANGE_166`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_166.md) admits editor placement, current-layout trial, local course persistence, historical clear legality and bounded maker completion. No earlier signature or verified combination changes.

## Negative results

- `ACT-162` rejected: a Wii U course-editor tile is not a carried Minecraft/Terraria item limited by survival reach, support and material stock.
- `TIM-006` rejected: trial play directly controls a platform character; it is not a locked autonomous machine simulation.
- No asserted checkpoint clear proof, exact gap dimension, upload success after shutdown or legal use of another maker's/sample course.
- No claim that simply finishing an ordinary trial already fulfills the separate upload clear check.

## Delta summary

The editable spatial arrangement becomes immediately testable as live platform geometry, but local save and the historical proof-of-clear upload gate remain separate states.

## New facts

- [Confirmed | Direct | High] Course creation, trial play and local Coursebot save are separate, documented Wii U transitions (`SMM-001`–`SMM-004`).
- [Confirmed | Direct | High] A creator's clear proof was required before historical upload (`SMM-005`), while the online service is no longer available (`SMM-006`).

## New genes

- [Confirmed | Direct | High] `ACT-567`, `ACT-568`, `SYS-1129`, `SYS-1130`, `CON-707` and `OBJ-247` capture the editor/test/save/proof chain without changing earlier genomes.

## New combinations

- [Observation | Direct | High] None created; every verified combination is checked against the complete signature.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_166` admits six typed boundaries for this one scoped unit.

## New questions

- On a pinned original Wii U executable, what exact course-edit actions invalidate an earlier clear proof, and what message distinguishes ordinary trial completion from the upload check?
- What are the movement constants and maximum jumpable gap for the selected *Super Mario Bros.* style and a precisely measured short course?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0429` *Commandos: Behind Enemy Lines* only after this unit's full validation, one local commit and Goal stop window.
- Optimisation criterion: contrast self-authored route testing with fixed-map specialist stealth and detection.
- Expected information gain: role-specific infiltration and alarm response under live hostile patrols.
- Backlog impact: no successor is started in this unit.

## Why this game

- [Hypothesis | Limited | Medium] Editor-to-play-to-proof dependencies are a different decision boundary from the prior light-gated combat unit and from fixed authored platform stages.
