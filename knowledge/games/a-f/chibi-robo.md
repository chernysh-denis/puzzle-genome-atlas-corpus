---
game_id: GAME-0555
slug: chibi-robo
game_title: Chibi-Robo!
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-089
    - ACT-199
    - ACT-219
    - ACT-754
    - ACT-755
  system:
    - SYS-630
    - SYS-1352
    - SYS-1606
    - SYS-1607
    - SYS-1608
    - SYS-1609
  constraint:
    - CON-799
  information:
    - INF-073
    - INF-179
    - INF-532
  objective:
    - OBJ-306
  time:
    - TIM-003
---

<!-- markdownlint-disable-next-line MD026 -->
# Game: Chibi-Robo!

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The number of wrappers, stain values, battery capacity and timer duration are
parameters of the admitted rules, not separate genes.

## Analysis scope

- Version / ruleset: original English European Nintendo GameCube retail
  Chibi-Robo!, released 26 May 2006 according to Nintendo UK. This is not a
  DS sequel, New Play Control! Wii adaptation or Switch 2 Classics wrapper.
  The European product identity is primary; the inspected printed manual and
  labelled GameCube recording are North American. They corroborate shared
  original-game housekeeping rules, not checksum-proven PAL control, speed,
  save or binary parity. No disc image, entitlement, console, emulator,
  installed revision or personally played save was inspected.
- Primary decision loop: choose reachable litter or floor dirt, collect and
  equip the toothbrush, scrub accepted surface residue or carry refuse to the
  bin, then judge the next chore against current charge and remaining night.
  Carry the attached plug to an outlet before exhaustion; retain happiness
  and money and settle ranking at the home outlet.
- Entry and exit: new-game state immediately after Jenny's birthday-flower
  tutorial and its initial home ranking, at the first night departure into
  the living room. Keep the default Timer 5 and buy no new gear. Finish the
  complete first night through its automatic dawn return, recharge/ranking
  settlement and next-period handoff, before the next live work period.
  Within this packet, use the living-room housekeeping module: its floor,
  accessible litter, first toothbrush, trash can, existing outlets and home
  base. Introductory dialogue is contextual gating, not a new social system.
- Failure and retry: an empty personal battery stops control and Telly returns
  the robot home. The manual states a monetary loss; the specialist account
  distinguishes the first Trauma Suit rescue from later money penalties.
  Retain that first/later qualification rather than inventing an exact loss
  fraction. The night clock ending is ordinary return, not the same failure.
  No clean-all, fixed happiness or cash quota is imposed as a native exit gate.
- Included: direct miniature-body traversal; addressed pickup; finite trash
  stacks per type; toothbrush equipment and repeated contact scrubbing;
  persistent treated floor; disposal with per-class accept/skip and separate
  money/happiness rewards; declared cleaning rewards and bonus eligibility;
  finite personal charge, outlet restoration and zero-charge rescue;
  running period clock with explicit pause contexts; automatic retained-state
  return; home-only rank update and capacity milestones; room, inventory and
  distinct resource/clock information. A milestone need not be reached in
  every first night for its conditional settlement rule to apply.
- Excluded: purchasing or using Chibi-Copter, Chibi-Blaster, timer replacements
  or spare batteries; high-drawer/Chibi-Door routes; Drake costume/pose tasks;
  the Foyer Free Rangers encounter; other-room chores, Spydorz, scrap,
  Utilibots, gardening, later family/toy quests and the campaign finale.
  The in-world Chibi-Manual drops later; possession is not an entry condition.
  DS house electricity, refuse sorting, 60-unit starting capacity and special
  cord-length upgrades are not silently transferred. No exact PAL drain rate,
  hidden bonus probability, cleanliness percentage or native reload trial.
- Potential scoped modules: first costume/pose exchange; Foyer encounter;
  purchased traversal and Chibi-Doors; later scrap/Utilibot routing; finale.
- Direct-play status: none. Read the original Nintendo US booklet, including
  printed pp. 12–13, 18–21, and its controls/equipment sections; inspect eight
  static 120×90 storyboard sheets from the NTSC GameCube longplay, approximately
  08:20–41:40. They show the first night, chores/outlet interactions and its
  home/day handoff, plus subsequent context. The recording also takes excluded
  costume/Foyer branches; their visibility does not add those modules to the
  genome. Tiny frames do not certify individual HUD numbers or exact input
  timing. No video stream, audio, foreground playback or focus change was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CHR-001` | Nintendo UK identifies the original European GameCube release as 26 May 2006; the manual/observed recording are North American corroboration, not authenticated PAL execution. | Observation | Direct | High | P1, P2, V1 |
| `CHR-002` | The first night follows the birthday flower tutorial; litter can be collected and delivered to the living-room bin for happiness and money. | Observation | Corroborated | High | P2 pp. 16–19, S1, S2, V1 |
| `CHR-003` | The first red toothbrush is acquired near Dad; equipment and repeated local strokes remove eligible floor dirt and earn declared cleaning rewards. | Observation | Corroborated | High | P2 pp. 14–17, S1, S3, V1 |
| `CHR-004` | Charge, happiness, money and period clock are distinct; carrying the attached plug to a socket restores personal charge and offers saving. | Observation | Corroborated | High | P2 pp. 6, 12, 18, S4, V1 |
| `CHR-005` | Empty charge causes home rescue; first-rescue and later monetary-penalty descriptions differ, and no exact penalty fraction or PAL drain formula is certified. | Observation | Limited | Medium | P2 p. 12, S5 |
| `CHR-006` | Refuse has a ten-per-type carried cap; the bin offers each held class for acceptance or skipping before removal and its priced rewards. | Observation | Corroborated | Medium | P2 pp. 16–19, S2, S6 |
| `CHR-007` | The running day/night period returns the robot home on expiry; equipment/pause and home contexts suspend time, and accepted work persists. | Observation | Corroborated | High | P2 pp. 10–12, 20, S7, V1 |
| `CHR-008` | The home outlet updates happiness-based rank; reached milestones grant larger batteries, whereas ordinary room outlets only recharge/save. | Observation | Corroborated | High | P2 pp. 20–21, S4, S8, V1 |
| `CHR-009` | Individual cleaning and the cleaning bonus are not a whole-room completion quota; unmeasured hidden bonus formulas are excluded. | Observation | Corroborated | Medium | P1, S1, S3 |

## Basic data

- Release / origin: skip Ltd. original GameCube adventure, published by
  Nintendo; European target 26 May 2006. The printed booklet credits the
  development team; Nintendo's current page uses broader developer metadata.
- Platform or physical form: Nintendo GameCube, English European retail,
  one player; structured target `PLAT-NINTENDO-GAMECUBE`.
- Puzzle family: live system pressure; inventory/fixture dependencies;
  ordered resource and work dependencies. Household theme alone is not family.
- Primary sources:
  - P1: [Nintendo UK original product page](https://www.nintendo.com/en-gb/Games/Nintendo-GameCube/Chibi-Robo--267829.html),
    European identity, date, English language, recharge and happiness premise.
  - P2: [original Nintendo North American instruction booklet, public scan](https://archive.org/details/Plug-Into-Adventure-NA-instructions),
    read original pages and OCR. Printed pp. 6–7 anatomy; 10–11 controls and
    paused equipment; 12–13 separate HUD/empty-battery rescue; 14–17 tools,
    equipment and inventory; 18–19 movement, plug, save and refuse; 20–21 home
    return, rank, battery milestones and optional store. Its US region is
    explicit; it does not prove an exact European executable.
- Secondary sources:
  - S1: [George Cube, GameCube walkthrough, May 2009](https://www.supercheats.com/gamecube/walkthroughs/chibirobo-walkthrough04.txt),
    prologue and first-night A Huge Place route. Its optional copter, costume
    and Foyer branches are not silently mandatory chores. Its exact bonus
    and pose-cost wording is not independently measured here.
  - S2: [original-game Trash section](https://chibi-robo.wiki/wiki/Trash),
    ten-per-type cap, chosen-class disposal and separate reward values.
  - S3: [Stain](https://chibi-robo.wiki/wiki/Stain) and
    [Toothbrush](https://chibi-robo.wiki/wiki/Toothbrush), original GameCube
    sections only. Cleaning bonus eligibility is retained, not a certified
    hidden random-number formula or an all-house dirt checklist.
  - S4: [Outlet](https://chibi-robo.wiki/wiki/Outlet), original-game section,
    room recharge/save versus home-only ranking. DS-only house-power and
    save restrictions are excluded.
  - S5: [Watt](https://chibi-robo.wiki/wiki/Watt), original-game section,
    80-unit initial capacity and first-rescue/later-penalty distinction.
    The DS section's 60-unit start is not this target. Exact sub-unit rates
    remain unverified secondary parameters, not native measurements.
  - S6: [CyricZ original GameCube FAQ](https://gamefaqs.gamespot.com/gamecube/583171-chibi-robo/faqs/41630),
    public indexed original-game trash/timer and second-night manual text.
    Direct retrieval is restricted; no bypass and no claim of a full fetched
    copy. This is corroboration, not the only authority for the scope.
  - S7: [Time Cycle](https://chibi-robo.wiki/wiki/Time_Cycle), original section,
    default five-minute half-day, optional paid replacements and pause contexts.
  - S8: [Chibi-Ranking](https://chibi-robo.wiki/wiki/Chibi-Ranking), original
    section, home update and capacity milestones rather than immediate levels.
  - V1: [LongplayArchive, explicitly NTSC GameCube](https://www.youtube.com/watch?v=sWyrxEcyCN8),
    35,410-second recording. Eight static sheets at ten-second sample steps,
    cells 120×90, range 500–2,490 seconds, inspected without audio/stream
    playback. The first-night return appears near the 25-minute region;
    later sampled daytime/night context is not claimed to be the first night.
- Claim IDs: `CHR-001`–`CHR-009`.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: `ACT-008` direct walking, running and authored ledge/cord
  traversal; `ACT-089` addressed toothbrush/litter pickup; `ACT-199` toothbrush
  equipment; `ACT-219` deliberate irreversible refuse delivery.
- Candidate genes: accepted `ACT-754` repeated contact scrubbing; `ACT-755`
  the actor's own attached plug carried and connected at a reachable socket.
- Parameters: target, reach, equipped tool, brush footprint, refuse class and
  quantity, attached plug and charging location; `CHR-002`–`CHR-006`.

### System Behaviour Genes

- Existing gene IDs: `SYS-630` accepts and retains newly treated floor state;
  `SYS-1352` applies the declared one-time reward of each eligible clean target
  and separate bonus credits. It does not invent cash for every brush stroke.
- Candidate genes: `SYS-1606` personal charge/refill/rescue; `SYS-1607` chosen
  refuse-class conversion; `SYS-1608` period-end retained return; `SYS-1609`
  home rank and capacity milestones.
- Resolution order: pickup → retained stack; equip → brush contact → accepted
  surface treatment → eligible reward; bin confirmation → chosen class removed
  → happiness and money; charge zero → rescue policy, distinct from night
  expiry → retained return → home charge/rank → successor period.
- Parameters: per-class rewards, bonus predicate, cap, action/time drain,
  first/later rescue, rank milestones; `CHR-002`–`CHR-009`.

### Constraint Genes

- Existing gene IDs: `CON-799`, a separate cap for each collected consumable
  refuse type; one full class does not forbid a different class.
- Candidate genes: none. Ten is a parameter, not a GameCube-specific gene.
- Scarce strategic resources: remaining charge, live period and free space in
  the relevant refuse stack; no shared total ten-slot bag; `CHR-004`–`CHR-007`.

### Information Genes

- Existing gene IDs: `INF-073` inventory/tool selection; `INF-179` currently
  visible room geometry, dirt, litter, outlets and bin.
- Candidate genes: `INF-532`, charge, clock, happiness, money and base rank as
  distinct decision information, not one cleanliness percentage.
- Information boundary: tiny inspected frames do not establish exact HUD
  sub-unit coefficients or unseen room contents; `CHR-002`–`CHR-008`.

### Objective Genes

- Existing gene IDs: none.
- Candidate genes: `OBJ-306`, use the whole first housekeeping period through
  retained home ranking and next-period handoff.
- Success, evaluation and failure: earn happiness from eligible chores; normal
  period expiry does not require complete cleanliness or a fixed reward total.
  Charge depletion is interrupted work/rescue, not campaign death. Rank one
  belongs to the excluded campaign finale; `CHR-005`, `CHR-007`–`CHR-009`.

### Time Genes

- Existing gene IDs: `TIM-003`, body and chore input remain live while the
  household clock and unplugged operation progress. Pause/equipment/home
  contexts are explicit parameters, not a claim that every indoor room pauses.
- Candidate genes: none. Do not reuse the fixed-reset loop `TIM-016`, or
  Harvest Moon's all-indoor clock stop `TIM-031`; `CHR-004`, `CHR-007`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Reachable wrapper, free capacity in its type | Pick it up | Scene item enters that carried stack; disposal reward remains unearned | Collection differs from banking | CHR-002, CHR-006 |
| Ten wrappers, room for another refuse class | Attempt another wrapper, then another class | Full class is refused; different class can still fit | Per-type cap, not shared bag | CHR-006 |
| First toothbrush acquired | Equip it and scrub an eligible floor mark | Contact accepts treated area; cleared target earns its declared reward | Tool, persistent surface and reward are separable | CHR-003, CHR-009 |
| Already clean floor beneath the brush | Repeat the same pass | No equivalent new target-clear reward | Cosmetic motion is not repeated progress | CHR-003 |
| Several carried refuse classes at bin | Accept wrappers but skip crumbs | Only committed class is removed and paid | Player-controlled disposal and distinct currencies | CHR-002, CHR-006 |
| Low charge, accessible outlet | Pick up own plug and connect | Personal charge refills; saving is offered | Active charging rather than proximity healing | CHR-004 |
| No charge remains | Allow rescue | Return home under first/later rescue policy; no invented campaign reset | Exhaustion is not normal dawn | CHR-005 |
| Live night, equipment menu opened | Inspect equipment then close it | Paused planning resumes the same period | Running-time pressure with pause contexts | CHR-007 |
| Night expires after some accepted chores | Accept home transition and rank handling | Retained work and rewards enter successor-period state | No clean-all quota or time-loop erasure | CHR-007, CHR-008 |
| Happiness available at a room outlet | Recharge there, then settle at home | Only home performs rank/capacity milestone handling | Outlet roles differ | CHR-004, CHR-008 |

## Strategic and experiential structure

- Local decision: a nearby stain, one more wrapper or an outlet route compete
  for charge and live night opportunity; the brush changes floor state while
  disposal banks carried refuse separately.
- Medium-term planning: empty full types at the bin, recharge before a risky
  traversal and bank happiness at home for capacity milestones.
- Long-term structure: persistent rank and retained world work lead beyond the
  packet. The campaign's family/toy dependencies are not claimed completed.
- Common heuristics: check charge before lengthy scrubbing, combine nearby
  litter routes and do not mistake money for usable personal energy.
- Failure attribution: explicit low charge and home rescue differ from normal
  phase expiry; no unsupported exact penalty fraction is promised.
- Player-trust factors: every unfinished stain need not be cleared tonight,
  and the European target does not masquerade as personally tested PAL play.
- Claim IDs: `CHR-002`–`CHR-009`.

## Replay and variation

- What changes between sessions: chore order, refuse classes retained, charge
  routes, reached bonuses and conditional capacity milestone.
- Randomness or procedural generation: no fabricated random room topology,
  certified bonus seed or fixed first-night point quota.
- Multiple viable strategies: clean near an outlet or collect a fuller bin
  load first while preserving enough charge for return.
- Typical replay motive: better use of a night and exploration of separately
  scoped modules; no native replay measurement is claimed.
- Claim IDs: `CHR-002`–`CHR-009`.

## Adjacent systems and history

- Direct predecessors: no unsupported mechanical parent is asserted.
- Variants: original European identity is distinct from US source provenance,
  Wii controls, DS house power and later Switch 2 presentation.
- Similar games: only selected complete-signature neighbours below receive
  numeric comparison; shared cleaning theme cannot override the scan.
- Important differences: personal charge/refill and home rank create pressure
  absent from an unlimited no-failure vehicle-washing job.
- Claim IDs: `CHR-001`, `CHR-004`–`CHR-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-089`, `ACT-199`, `ACT-219`, `ACT-754`, `ACT-755` | body, item, equipped brush, disposal, attached plug |
| System Behaviour | `SYS-630`, `SYS-1352`, `SYS-1606`, `SYS-1607`, `SYS-1608`, `SYS-1609` | surface, rewards, charge, class conversion, return, home rank |
| Constraint | `CON-799` | per-type refuse capacity |
| Information | `INF-073`, `INF-179`, `INF-532` | held state, room, separate HUD measures |
| Objective | `OBJ-306` | complete period into home settlement |
| Time | `TIM-003` | live clock with specified paused contexts |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `554` (`GAME-0001`–`GAME-0554`).
- Exact genome matches: none.
- Tied near matches: `GAME-0307` — Slime Rancher (`4 / 26 = 0.153846`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0307` — Slime Rancher | `ACT-008`, `ACT-219`, `INF-073`, `TIM-003` | Both combine live body traversal, carried items and deliberate sale/disposal. Slime Rancher vacuums and feeds creatures for plorts and builds a corral; the robot scrubs persistent floor dirt, budgets personal charge, disposes refuse for two rewards and banks rank at home. Shared cleaning imagery with PowerWash Simulator does not supersede the complete-signature result. | Tied near; `4 / 26 = 0.153846` |

- New genes: eight accepted definitions; ten reused without change.
- Classification result: `New gene`.
- Evidence and reasoning: complete prior-signature and verified-combination
  scan, independent of household theme.

### Preserved research notes

- New genes: eight accepted definitions; ten reused without change.
- Classification result: `New gene`.
- Evidence and reasoning: complete prior-signature and verified-combination
  scan, independent of household theme.

## Taxonomy impact

- Registry changes: ACT-754, ACT-755, SYS-1606–SYS-1609, INF-532, OBJ-306.
- Taxonomy-change record: [TAXONOMY_CHANGE_301](../../../research/taxonomy-changes/TAXONOMY_CHANGE_301.md).
- Candidate terms affected: contact scrubbing, attached charging plug,
  personal-charge rescue, refuse banking, retained return and home ranking.

## Negative results

- No separate record. Rejected boundaries are recorded in the taxonomy review.
  No earlier definition or signature is revised.

## Delta summary

The following compact ledger records changes rather than restating the analysis.

## New facts

- [Observation | Corroborated | High] Pickup, disposal, happiness, money,
  current charge and home rank are distinct; CHR-002–CHR-008.
- [Observation | Limited | Medium] First/later rescue penalty qualification
  remains explicit; no exact PAL formula or personally tested save; CHR-005.

## New genes

- [Observation | Corroborated | High] Eight bounded additions; personal rescue
  retains the documented Medium qualification for its exception.

## New combinations

- [Observation | Corroborated | High] None introduced; deterministic scan owns support.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_301 adds definitions only.

## New questions

- [Hypothesis | Limited | Medium] A future authorised native EU experiment
  could compare charge, first/later rescue and save retention field by field;
  a regional difference would reject untested parity, not rewrite the evidence.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0556 Sayonara Wild Hearts, iOS.
- Optimisation criterion: preserve approved mixed-platform Selection 044.
- Expected information gain: authored rhythmic traversal after resource-bound chores.
- Backlog impact: retain Boktai and Moss in the approved order.

## Why this game

- [Hypothesis | Limited | Medium] Original GameCube household care contrasts
  with the previous untimed botanical service and exercises energy decisions.
