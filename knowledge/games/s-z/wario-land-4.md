---
game_id: GAME-0497
slug: wario-land-4
game_title: Wario Land 4
analysis_status: reviewed
reviewed: 2026-10-04
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-049
    - ACT-202
    - ACT-295
    - ACT-611
  system:
    - SYS-037
    - SYS-045
    - SYS-064
    - SYS-215
    - SYS-578
    - SYS-755
    - SYS-1345
    - SYS-1346
    - SYS-1347
    - SYS-1348
    - SYS-1349
    - SYS-1350
  constraint:
    - CON-175
    - CON-282
  information:
    - INF-115
    - INF-119
    - INF-470
  objective:
    - OBJ-002
    - OBJ-285
  time:
    - TIM-003
---

# Game: Wario Land 4 — complete Normal Palm Tree Paradise

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Input mappings, money values, block classes and timer lengths are parameters.

## Analysis scope

- Version / ruleset: original English European Game Boy Advance Game Pak,
  Normal, complete first Emerald Passage stage Palm Tree Paradise. Nintendo's
  preserved AGB-P-AWAP-NEU6 booklet is the primary rules source. Original
  US/EU reconstructed code is corroboration, not an executed or hash-verified
  cartridge. Virtual Console, Switch emulation and difficulty variants are
  not silently equated with this target.
- Structured analysis target: existing `PLAT-GAME-BOY-ADVANCE`; original
  European English Game Pak, not an assertion about every regional release.
- Primary decision loop: read local terrain, enemies, health, collected
  pieces and score; walk, dash, jump, crouch/crawl, swim or strike; stun and
  carry eligible actors, charge directional throws, break compatible blocks
  and operate coloured switches; use the available apple transformation to
  reach optional rewards, then trigger the frog and choose a return route
  while time and possible overtime losses continue.
- Entry and exit: first controlled position after a fresh first entry through
  the stage vortex, with Entry Passage already cleared and no earlier
  Palm Tree Paradise collection credits. Include the entire main route,
  both caves, secret walls, underwater detour and both Professor bonus rooms,
  every available collection/interaction alternative, the frog switch and
  return. Exit at retained Stage Select settlement after returning through
  the reopened vortex; alternatively health loss, exhausted overtime money
  or Give Up ends the attempt without its new treasure credits. Suspend and
  resume remains the same attempt, not a second successful clear.
- Included: body attacks and available dash/air/ground-pound/crouch variants,
  enemy contact and rebound, charged carried-actor throws, swimming, local
  block destruction, colour-linked solid geometry, hidden-wall exploration,
  Fat Wario from the local Apple Ape, health and sub-heart recovery, score,
  four independently collected jewel pieces, optional CD, following Keyzer,
  switch-started return clock, money-draining overtime, automatic settlement
  and one-use mid-stage save-and-quit.
- Excluded: prior Entry Passage, other Emerald stages, bosses, item shop and
  purchased minigames, Sound Room use after CD credit, whole-pyramid victory,
  Hard/Super Hard layouts, unavailable Puffy/Bat/Zombie/Flaming/Frozen/Flat
  forms, emulator rewinds, deliberate geometry clips and TAS timing exploits.
  No slope-triggered rolling state is evidenced in this stage; the general
  booklet command is not proof of a local trigger. File administration and
  soft reset are outside the causal attempt, not a fictional retry currency.
  No exact native frame, collision box, enemy-drop distribution or complete
  original-engine event order is asserted.
- Potential scoped modules: another stage with a distinct transformation,
  one boss/shop encounter, original difficulty comparison and native
  save/overtime measurement require separate entries and terminals.
- Direct-play status: no cartridge, ROM, emulator, native save, gameplay
  screenshots, movie, video or audio was executed or analysed. The booklet
  was visually read; written routes and pinned reconstructed source were
  inspected. Generated illustrative art is not evidence.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| WL4-001 | The target is the original GBA English Normal first Emerald stage, not a later emulator or difficulty layout | Confirmed | Direct | High | P1; S1, S2 for scope |
| WL4-002 | Movement, body attacks, crouching, swimming and weight/charge-sensitive throws remain distinct available choices | Observation | Corroborated | High | P1 pp. 4–8; S1 |
| WL4-003 | The complete route contains two caves, secret walls, water, two Professor rooms, coloured switches, four pieces, CD, Keyzer and frog | Observation | Corroborated | Medium | S1, S2, S3 |
| WL4-004 | Apple contact produces slower Fat Wario with strong landing/contact effects; walking restores ordinary form | Observation | Corroborated | High | P1 pp. 20–21; S1 |
| WL4-005 | The frog reopens the entry vortex and starts the return clock; expiry drains money before eventual ejection | Observation | Corroborated | High | P1 pp. 10–12; S1 |
| WL4-006 | Keyzer credit unlocks the next stage, while jewel pieces and CD have independent retained functions | Observation | Corroborated | High | P1 pp. 10–11, 18–19; P2 AutosaveStageClear |
| WL4-007 | Successful return banks current collected credits and score; zero health or Give Up discards attempt treasure without consuming finite lives | Observation | Corroborated | High | P1 pp. 12–14; P2 autosave.c |
| WL4-008 | Small hearts fill an auxiliary gauge to restore one health unit; the heart chest fully restores health | Observation | Corroborated | High | P1 pp. 12–13, 18–19; S1 |
| WL4-009 | Quit creates a resumable mid-stage save that is consumed on continuation, unlike replayable permanent clear data | Observation | Direct | High | P1 pp. 13–14 |
| WL4-010 | Matching ! switches toggle linked block solidity; actor throws can activate an otherwise unreachable switch | Observation | Corroborated | High | P1 pp. 6, 18–19; S1 |
| WL4-011 | No native execution or exact quantitative parity is established | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Nintendo, original 2001 Game Boy Advance product.
- Platform or physical form: original English European Game Pak; Normal.
- Puzzle family: state transformation, physics/object manipulation,
  real-time pressure and ordered dependency sequencing; existing families.
- Primary sources, inspected 2026-10-04:
  - **P1:** [Nintendo original booklet](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/game_boy_advance_8/Manual_GameBoyAdvance_WarioLand4_EN_DE_FR_ES_IT.pdf),
    AGB-P-AWAP-NEU6, English printed pp. 4–23. Publisher-hosted scan,
    downloaded and visually inspected; its PDF creation date is not a game
    release date. SHA-256:
    `62ac07bd708f54ae104daa25f6619a89a582221ae138d51c21d296907974ba42`.
  - **P2:** [Pinned clean-room reconstruction](https://github.com/lilDavid/warioland4/tree/abb7800a8d8fa6d7f7f003627893e06bc2879329),
    `src/autosave.c`, `src/sprite_ai/vortex.c`, `src/sprite_ai/keyzer.c`.
    `AutosaveStageClear` stores each collected piece/CD/Keyzer separately;
    vortex reopening tests `gSwitchPressed`, not an exhaustive-piece quota.
    Source inspection only; repository ROM identity is an author claim,
    not an independently built, dumped or executed binary in this unit.
- Written firsthand sources, inspected 2026-10-04:
  - **S1:** [EOrizzonte Normal route](https://gamefaqs.gamespot.com/gba/524513-wario-land-4/faqs/16061),
    version 1.0, updated 2002-03-01; scoped Palm Tree route and optional
    Professor/apple/colour-switch branches, not adjacent stage paragraphs.
  - **S2:** [StarFighters76 Normal route](https://gamefaqs.gamespot.com/gba/524513-wario-land-4/faqs/47612),
    version 1.0, 2007-03-26; explicit Normal scope and full stage diagram.
  - **S3:** [Reseren original Normal TAS account](https://tasvideos.org/7966S),
    submitted 2023-01-15; written Palm Tree section confirms outward/return
    collection alternatives. The movie and ROM were not inspected; its
    glitches, input optimisations and frame claims are not ordinary rules.
  - **S4:** [Rickosss written route](https://walkthrough.freeola.com/game/2477/gba/wario-land-4.html),
    landmark-based cave/CD corroboration only, not its room numbering.
- Access limitation: direct GameFAQs pages were blocked; indexed written
  sections were read without bypass. A 403 StrategyWiki page and AI-generated
  DeepWiki overview are not independent mechanical evidence. Inconsistent
  player rebound-button advice is resolved by P1, not copied into the genome.
- **R1:** this source-limited reconstruction and repository verification.
- Claim IDs: WL4-001–WL4-011.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008/048/049/202/295/611`: direct traversal, portable-body
  manipulation, switch operation, posture, body attacks and eligible hostile
  throws. ACT-611 covers the booklet's stunned enemies, which remain combat
  actors. The indestructible Professor is instead carried and released as
  a physical switch tool under ACT-048; his friendly role is not broadened
  into a live opponent. This admission concerns his held-body manipulation,
  not a claim that he is inherently inanimate or that his idle AI is a prop.
  Hold duration, weight, upward release, dash run-up and ground-pound height
  are command parameters rather than extra gene IDs.
- Claim IDs: WL4-002, WL4-003, WL4-010.

### System Behaviour Genes

- Existing `SYS-037/045/064/215/578/755`: collectible credit, autonomous
  local movement, approach-sensitive enemy rebound/penalty, live attack
  resolution, single health pool and compatible block destruction.
- New `SYS-1345/1346`: return-clock activation and soft overtime are separate
  from clear banking, retained collection and failure rollback.
- New `SYS-1347/1348`: apple-induced capability conversion with locomotion
  recovery, and matching switch-directed solid-block groups.
- New `SYS-1349/1350`: one-use suspend-save consumption, and auxiliary
  recovery-gauge completion restoring one health unit.
- Resolution order: apply eligible movement/action/contact, update actor,
  geometry, collection and health, then current return/overtime and terminal
  predicates. This is qualitative causality, not recovered engine ordering.
- Claim IDs: WL4-002–WL4-010.

### Constraint Genes

- Existing `CON-175/282`: persistent attempt health and authored progression
  conditions. Zero health ends this multi-room attempt but is not a finite
  life stock or permanent campaign game-over. General solid geometry is not
  Baba Is You's property-assigned cell rule `CON-032`.
- Claim IDs: WL4-003, WL4-005–WL4-007.

### Information Genes

- Existing `INF-115/119`: presently exposed local opponents and own resources;
  neither reveals future cave geometry or enemy schedules.
- New `INF-470`: current stage score, collected piece/CD/Keyzer indicators,
  health/sub-heart meter and return-clock phase without a finite-lives field.
- Claim IDs: WL4-003–WL4-010.

### Objective Genes

- Existing `OBJ-002`: preserve/improve independently evaluated score.
- New `OBJ-285`: trigger return authority and settle the entry-vortex return,
  with successor access conditional on Keyzer and independent optional
  collection credits. Ordinary return without Keyzer is not falsely called
  next-stage unlock; four pieces are not all required for ordinary exit.
- Claim IDs: WL4-005–WL4-007.

### Time Genes

- Existing `TIM-003`: simultaneous live input, enemy evolution and physics;
  pause/save policy and the switch-triggered phase are separate parameters
  and system transitions, not a turn-based stage.
- Claim IDs: WL4-002, WL4-005, WL4-009.

## Reproducible transitions

| Before | Action | Resolution | Decision boundary | Claim ID |
|---|---|---|---|---|
| Eligible small hostile below Wario | Land from above; hold the booklet's rebound input | Rebound and the eligible defeat/stun response differ from unsafe side contact | Top contact is not general body immunity | WL4-002 |
| Eligible stunned hostile, or the portable friendly Professor | Pick up, move, charge B and release upward or sideways | Actor travels as a physical tool, striking eligible block/switch | The Professor does not require the hostile-stun predicate and is not destroyed like an ordinary hostile | WL4-002, WL4-010 |
| Cave entrance hidden by breakable blocks | Break compatible blocks, enter door and explore the optional pipe | Access the piece and Professor room rather than skip the entire branch | Complete scope includes optional decisions | WL4-003 |
| Local Apple Ape and compatible landing surface | Accept apple, then jump/land; later walk | Slower Fat form supplies strong contact/landing, then ordinary form returns | Not a selectable copied ability or damage-demoted Mario pickup | WL4-004 |
| Coloured dotted/solid block group | Hit its matching ! switch directly or with the eligible thrown actor | Linked group changes solidity | Fixed path geometry changes, not a moving Braid platform | WL4-010 |
| Frog unpressed, entry vortex closed | Trigger frog | Entry vortex reopens and return clock starts | Keyzer and complete jewel quota do not activate this clock | WL4-005, WL4-006 |
| Return clock reaches zero with positive stage money | Continue navigating | Money drains while returning remains possible | Zero time is not immediate defeat | WL4-005 |
| Reopened vortex reached | Return with or without Keyzer and optional treasures | Clear settlement banks eligible collected credits; Keyzer alone gates successor access | Boss-piece collection and CD credit remain independent | WL4-006, WL4-007 |
| Health missing, auxiliary gauge partly filled | Collect eligible small hearts until the gauge fills | One health unit returns; a heart chest instead refills health fully | Gauge completion is not passive regeneration | WL4-008 |
| Active unsaved attempt | Select Quit and later continue | Saved mid-stage state resumes and that suspend record is consumed | Not an unlimited rewind or reusable checkpoint | WL4-009 |
| Zero health, Give Up or exhausted overtime money | Settle failure | Return to selection without new attempt treasures | No finite-life currency is invented | WL4-005, WL4-007 |

These are sourced qualitative tests, not a claimed native execution.

## Strategic and experiential structure

- Local decisions trade attack/rebound positioning, throw reach, fragile
  health and transformation access rather than demand every hostile kill.
- Route planning separates optional treasure detours from the switch and
  timed reverse traversal. Outbound versus return collection is viable.
- Failure attribution distinguishes health exhaustion, overtime attrition
  and voluntary abandonment; successful return does not guarantee Keyzer.
- Player-trust factors: readable current indicators and disclosed source
  limits; no inferred finite-life pool or mandatory four-piece exit quota.
- Claim IDs: WL4-002–WL4-010.

## Replay and variation

- Authored geometry is retained; timing, collection, throws and contacts vary.
- No random seed, precise enemy-drop probabilities or native timing is claimed.
- Replays may improve score and missing retained credits; other difficulty
  layouts and tool-assisted routes are outside this packet.
- Claim IDs: WL4-003–WL4-010.

## Adjacent systems and history

- Shared platform branding does not transfer Mario pickup/life rules.
- Other transformation stages and boss/shop economy require separate scope.
- Claim IDs: WL4-001, WL4-004–WL4-009.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-008, ACT-048, ACT-049, ACT-202, ACT-295, ACT-611 | Direction, hold duration, weight, run-up |
| System Behaviour | SYS-037, SYS-045, SYS-064, SYS-215, SYS-578, SYS-755, SYS-1345, SYS-1346, SYS-1347, SYS-1348, SYS-1349, SYS-1350 | Timer, recovery and collision quantities |
| Constraint | CON-175, CON-282 | Health and prior-route predicates |
| Information | INF-115, INF-119, INF-470 | Current field/indicator presentation |
| Objective | OBJ-002, OBJ-285 | Independent score and conditional unlock |
| Time | TIM-003 | Live time and pause policy |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `496` (`GAME-0001`–`GAME-0496`).
- Exact genome matches: none.
- Tied near matches: `GAME-0459` — Daxter (`9 / 35 = 0.257143`).
- Supported combination subsets: none.
- Scan date: 2026-10-04.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0459` Daxter | `ACT-008/202`, `SYS-037/045/215/578`, `CON-175`, `INF-119`, `TIM-003`: direct traversal/posture, collected credit, local movement, contact combat, persistent health and current live feedback | Daxter's swatter extermination requires a location-specific Gem quota and concierge report. Wario's body attacks and actor throws, local apple form, coloured solidity, switch-started money-draining return, independent collection banking and key-conditional successor differ. No spray, finite lives or immediate clock-expiry loss is inferred. | Near, `0.257143` |

### Preserved research notes

- New genes: SYS-1345–SYS-1350, INF-470, OBJ-285.
- Classification result: New gene.
- Evidence and reasoning: explicit timer, banking, transformation, geometry,
  suspension, recovery and terminal distinctions; no external novelty claim.

## Taxonomy impact

- Eight additions; earlier English boundaries and signatures remain unchanged.
  Review-on-touch restores Ukrainian parity for ACT-049, CON-282 and INF-115.
- [Taxonomy Change 234](../../../research/taxonomy-changes/TAXONOMY_CHANGE_234.md).

## Negative results

No native execution, immediate zero-time defeat, finite-life decrement,
four-piece exit quota, automatic successor access without Keyzer, imported
Hard-only layout, slope-roll trigger, unavailable transformation, exact
throw/recovery/frame formula or current-emulator parity is established.

## Delta summary

One complete original Normal stage includes optional branches and return
settlement rather than a curated treasure-only route.

## New facts

- [Observation | Corroborated | High] Return, successor access and independent
  collection banking have different predicates; time expiry precedes failure.

## New genes

- SYS-1345–SYS-1350, INF-470, OBJ-285.

## New combinations

- None without independently supported recurring subsets.

## Taxonomy changes

- Eight additions and eighteen unchanged transfers; no older game rewrite.

## New questions

- Execute a lawful declared cartridge/save to measure overtime debit,
  suspend restoration and exact throw/contact resolution.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0498 Transport Fever 3, Windows.
- Optimisation criterion: approved mixed-era, varied-platform horizon.
- Expected information gain: transport decisions rather than platform return.
- Backlog impact: one complete third unit; no implicit start here.

## Why this game

- [Hypothesis | Limited | Medium] Original handheld traversal complements
  modern Windows combat without a contiguous genre block.

## Resemblances to known games

- Only deterministically selected prior neighbours are interpreted.

## Updated hypotheses

- No cross-game pattern is promoted solely from the new signature.

## Next research subject

- GAME-0498 Transport Fever 3, Windows.
