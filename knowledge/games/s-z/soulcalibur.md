---
game_id: GAME-0455
slug: soulcalibur
game_title: Soulcalibur
analysis_status: reviewed
reviewed: 2026-09-30
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-202
    - ACT-223
    - ACT-294
    - ACT-295
    - ACT-296
    - ACT-297
    - ACT-459
    - ACT-604
    - ACT-605
  system:
    - SYS-215
    - SYS-522
    - SYS-868
    - SYS-1198
    - SYS-1199
    - SYS-1200
  constraint:
    - CON-442
    - CON-446
    - CON-733
  information:
    - INF-142
    - INF-209
    - INF-210
  objective:
    - OBJ-259
  time:
    - TIM-003
---

# Game: Soulcalibur

Use the canonical [vocabulary and signature](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Fighter names, weapons, costumes, control notation and arena dimensions are parameters, not additional genes.

## Analysis scope

- Version / ruleset: original English 1999 Namco Dreamcast Soulcalibur, one local two-player VS Battle match with Mitsurugi and Nightmare, ordinary full life bars and an ordinary finite ring with exposed edges. Use the original manual's default controller notation: X horizontal, Y vertical, B kick, A guard. Set and record FIGHT COUNT and ROUND TIME at the contemporary Dreamcast guide's reported defaults of two required wins and 40 seconds; these values are source-reported, not inspected on a disc. Neutral Guard remains enabled and both handicaps are unchanged. No exact regional disc serial, executable hash or stage dimensions were obtained.
- Primary decision loop: read opposing weapon reach, relative axis, posture, life and time; step or run around the opponent, crouch/jump, choose an attack or stance, guard, throw/escape, time a height-compatible Guard Impact or risk Soul Charge; let contact, counters, knockdown, recovery and edge departure settle; repeat through the awarded rounds until this fixed-pair VS match displays its result.
- Entry and exit: confirm the two named fighters and a non-walled ring before its first round, with the declared options recorded. Exit at the VS match result after the required round wins, including a displayed drawn result if both reach the requirement together, or deliberate abandonment. A drawn round awards both sides; the manual limits Sudden Death to Arcade and Time Attack, so no such VS rule is imported. Exact final VS double-result presentation remains unexecuted rather than guessed.
- Included: character selection; opponent-relative stepping and eight-way running; crouch, jump, ordinary and directional weapon/kick commands, pose/stance-specific command families and unblockable attacks; standing/crouching and optional neutral guard; front/side/back throws and eligible matching escapes; Guard Impact repel/parry, its brief freeze, priority reversal and counter-impact exception; manual-described two-state Soul Charge; counter hits, launches, airborne follow-ups, directed landing, downed rolls, quick recovery and stagger recovery; KO, ring out, timeout health comparison, simultaneous draw, repeated full-life round resets and required-win settlement; shared live view, life/clock/round state and animation cues.
- Excluded: Arcade ladder/Continue and its Sudden Death; Team Battle, Mission Battle, Survival, Time Attack, Practice, Art Gallery, Museum, unlock/progression and memory-card rewards; another fighter pair or stage-specific walls; exact damage, frame, impact/escape windows, charge duration and exhaustive command tables; later Soulcalibur II–VI meters, Reversal Edge, Critical Edge, armour breaks and online play. Future separate packets could cover Mission Battle's priced art-card progression or Survival's carried life.
- Direct-play status: not conducted. No Dreamcast, GD-ROM, executable, save, controller trace, gameplay video or audio was opened or played. The original Namco manual's scanned diagrams and rule pages were visually inspected. Only public indexed portions of the restricted contemporary Dreamcast guides were read, without bypassing access restrictions. The 1999 beginners' FAQ explicitly admits an arcade/Japanese basis and is not evidence of US disc parity. The cases below reconstruct source rules, not executed engine tests. Artwork is original interpretation, not a captured match.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SC-001` | The original Dreamcast manual distinguishes VS Battle from ladders, team, mission and carried-life modes | Observation | Direct | High | P1 pp. 6–13 |
| `SC-002` | Opponent-relative eight-way run, weapon commands and high/mid/low/special-mid guard or evasion organise contact | Observation | Direct | High | P1 pp. 16–19 |
| `SC-003` | Throws, eligible matching escapes, air control, quick roll and downed/stagger recovery offer different live responses | Observation | Direct | High | P1 pp. 19–22 |
| `SC-004` | Height-compatible timed repel/parry creates a freeze and first-move advantage; the impacted fighter may counter-impact but cannot ordinarily attack/guard immediately | Observation | Direct | High | P1 p. 21 |
| `SC-005` | The manual describes green counter-effect and gold selected-unblockable Soul Charge states; forcing its owner to guard cancels charge | Observation | Direct | Medium | P1 p. 23; no charge window executed |
| `SC-006` | KO, ring departure or favourable health at timeout earns a round; simultaneous KO/departure/equal timeout draws award both; Sudden Death is not a VS rule | Observation | Direct | High | P1 pp. 4–5 |
| `SC-007` | The intended two-win/40-second settings are contemporary Dreamcast default reports, not measured disc settings | Observation | Limited | Medium | P2 public indexed options clauses |
| `SC-008` | Original Dreamcast Mitsurugi has live Mist/Relic command forms, distinct from later-edition command tables | Observation | Limited | Medium | P3 public indexed Dreamcast-change clauses; P1 stance notation |
| `SC-009` | Every prior signature and verified combination is scanned without changing earlier boundaries | Observation | Direct | High | canonical comparison recomputation |
| `SC-010` | Exact executable, regional parity, final simultaneous VS presentation and hidden coefficients remain unverified | Observation | Direct | High | documentary inspection boundary |

## Basic data

- Release / origin: Namco, original Dreamcast 1999 ruleset; no later port equivalence is asserted.
- Platform or physical form: original Dreamcast GD-ROM and two local controllers; structured target is `PLAT-DREAMCAST`.
- Puzzle family: `FAM-009` tactical forecast and counterplay, and `FAM-010` real-time system pressure. Height, approach axis and impact timing change each exchange; live time does not wait for a response.
- Primary sources, checked 2026-09-30: **P1**, [Namco's original English Dreamcast instruction manual](https://www.digitpress.com/library/manuals/dreamcast/soul_calibur.pdf), archival scan, printed pp. 4–23 and character profiles pp. 25/27 inspected as pixels. **P2**, [CMurdock's original Dreamcast Mini-FAQ](https://gamefaqs.gamespot.com/dreamcast/198705-soulcalibur/faqs/2722), only indexed FIGHT COUNT, ROUND TIME, stage-selection and control-display passages. **P3**, [sherv22's Arcade to Dreamcast Changes](https://gamefaqs.gamespot.com/dreamcast/198705-soulcalibur/faqs/2725), only indexed Mist/Relic Dreamcast-change passages. These written player documents are primary testimony about their play, not publisher rules or a locally verified command chart.
- Scope-warning source: **P4**, [Chubsalex's 1999 beginners' FAQ](https://gamefaqs.gamespot.com/dreamcast/198705-soulcalibur/faqs/2721), readable introduction explicitly says its purported US guide still uses arcade/Japanese evidence; no exclusive US behaviour is taken from it.

## Mechanical decomposition

### Action Genes

`ACT-294` commits this fixed pair. `ACT-008` owns stepping, eight-way run, jumping and directed airborne placement; `ACT-202` changes crouch posture. `ACT-295` requests compatible horizontal/vertical/kick, directional, running and airborne follow-up attacks. `ACT-296` is sustained guard, whereas `ACT-223` already covers a timed eligible defensive response and therefore owns directional Guard Impact without a duplicate action gene. `ACT-297` owns close throw and eligible matching break. `ACT-459` changes a weapon's live command form; its Mitsurugi instance is source-limited, not a full recovered move list. `ACT-604` requests weapon charge or its alternate cancellation branch; `ACT-605` requests state-specific quick/downed/stagger recovery. Claims SC-002–SC-005, SC-008.

### System Behaviour Genes

`SYS-215` owns ordinary contact, whiff, height-aware guard, counter-hit damage/stagger, launch, juggle and knockdown. `SYS-868` applies the current weapon form to subsequent strikes. `SYS-1198` owns impact freeze, priority and the counter-impact exception, not persistent weapon wear. `SYS-1199` owns two charged-effect branches and guard-induced cancellation. `SYS-522` retains its KO/timeout round award and reset branch; `SYS-1200` adds the independently spatial ring-departure award, including simultaneous departure drawing both sides, feeding the same round-marker/reset loop. Neither existing gene is silently broadened. Claims SC-002–SC-006.

### Constraint Genes

`CON-442` gates commands by pose, direction, height, range and recovery, including the post-impact ordinary-command restriction. `CON-446` contributes vitality, clock and required-win bounds; it is not claimed to be the only terminal predicate. `CON-733` contributes opponent-relative lateral motion inside a finite ring and the additional departure terminal, unlike classic Tekken's explicitly no-ring-out floor. Exact ring dimensions, charge timings and escape windows remain parameters. Claims SC-002–SC-007.

### Information Genes

`INF-142` exposes attack/contact, impact and charge timing through animation and effects without exact frame values. `INF-209` keeps the pair's relative distance, axis, facing and pose perceptible in a shared view. `INF-210` exposes paired life, timer and accumulated round markers, not a later soul/super meter. The ground's visible edge is contextual geometry, not a claim of fully visible hidden command state. Claims SC-002–SC-006.

### Objective Genes

`OBJ-259` seeks enough wins against this fixed opponent with all three permitted award routes: KO, favourable timeout or ring departure. Do not transfer `OBJ-099` as an exhaustive objective: its unchanged wording admits KO/time-over only, which omits a decision-relevant nonzero-health victory route here. Claims SC-006–SC-007.

### Time Genes

`TIM-003` schedules movement, attack recovery and the round clock with live input; explicit pause interrupts play, not a player turn. Impact's brief freeze is part of its system transition, not a new general time mode. Claims SC-002, SC-004, SC-006.

## Reproducible transitions

These are source-derived edge cases. Use licensed original hardware/media for future execution, record the stage/options and inspect the game's own command list; no cartridge or disc execution is claimed here.

| Before | Action | Source-described resolution | What it establishes | Claim |
|---|---|---|---|---|
| A vertical strike approaches the previous axis | Step/run laterally before contact | A strike may miss the moved body; not every attack is defeated by any side step | alignment precedes damage | SC-002 |
| Defender stands or crouches | Sustain the corresponding guard | Standing guards high/mid, crouching low; special mid accepts either; crouch evades high and jump may evade low | height is a predicate, not strength | SC-002 |
| An eligible attack approaches | Time high/mid or mid/low repel/parry | Both freeze briefly; successful defender moves first | impact is not sustained guard | SC-004 |
| Attacker has been impacted | Attempt ordinary attack/guard versus timed counter-impact | Ordinary commands remain restricted; a counter-impact may answer the follow-up | priority is not a guaranteed unavoidable hit | SC-004 |
| Fighter begins ordinary Soul Charge | Choose the manual's hold versus guard-cancel branch | Green state gives counter-like attack effects; gold gives selected unblockables | two states, no modern meter debit | SC-005 |
| Opponent is charged | Force that fighter to guard | Charge is cancelled | charge is not permanent equipment | SC-005 |
| A gold-charged fighter faces an unblockable | Attempt ordinary defence versus eligible Guard Impact | Manual gives impact as the defensive exception; exact eligibility remains move-dependent | do not import universal immunity | SC-005 |
| Close ordinary throw begins | Press matching X or Y escape | Eligible throw escape avoids the ordinary grab; side/back/special exceptions are not guessed | escape depends on actual throw | SC-003 |
| Body is airborne or downed | Direct landing, hold guard for Quick Roll, roll or request recovery | Landing/recovery state changes the next attack opportunity and edge exposure | no automatic safe wake-up | SC-003 |
| Fighter staggers | Repeated compatible recovery inputs | Recovery can be accelerated while opponent remains active | recovery is a player intervention | SC-003 |
| One fighter still has positive life near the edge | A legal displacement carries it outside | Opponent earns Ring Out without needing zero life | arena departure is a separate round route | SC-006 |
| Both depart together or reach equal-health timeout | No invented tiebreak input | Draw awards both; Arcade/Time Attack Sudden Death is excluded | mode-specific draw scope | SC-006 |
| KO/timeout/ring award leaves the match unfinished | Continue the same pair | Eligible round state resets; accumulated markers remain until required wins | not an Arcade stage advance | SC-006 |

## Strategic and experiential structure

Height, lateral alignment and reach compete with edge position: a long weapon is not an unconditional hit, and remaining life does not protect against departure. Timed impact reverses initiative but permits a counter-impact, so the next attack remains a prediction. Charge risks spending live opportunity on altered effects; forcing guard removes that advantage. Knockdown, stagger and airborne placement retain decisions rather than becoming an automatically safe reset. These are bounded source interpretations (SC-002–SC-006), not measured player-performance claims.

## Replay and variation

The fixed pair, ring class and recorded options remain unchanged; each player's timing, approach, throws, charge, counters, recovery, round results and draws vary. No deterministic random seed, exact hitbox/frame/damage table or optimal sequence is claimed. Costume and arena backdrop are presentation parameters. Outside-match records do not define this packet (SC-001, SC-007, SC-010).

## Adjacent systems and history

The manual separates Mission Battle's rule variants and purchased artwork, Survival's partially restored carried life, and Arcade's ladder/Continue/Sudden Death. None is flattened into ordinary VS. Modern meters and cinematic counter systems belong to other editions; original-Dreamcast documentation does not establish their equivalence (SC-001, SC-010).

## Normalised genome

| Type | Active gene IDs | Role |
|---|---|---|
| Action | `ACT-008`, `ACT-202`, `ACT-223`, `ACT-294`, `ACT-295`, `ACT-296`, `ACT-297`, `ACT-459`, `ACT-604`, `ACT-605` | placement, posture, timed impact, selection, attacks, guard, throws, form, charge and recovery |
| System Behaviour | `SYS-215`, `SYS-522`, `SYS-868`, `SYS-1198`, `SYS-1199`, `SYS-1200` | contact, ordinary round reset, weapon form, impact, charge and ring departure |
| Constraint | `CON-442`, `CON-446`, `CON-733` | command state, ordinary match bounds and finite lateral ring |
| Information | `INF-142`, `INF-209`, `INF-210` | animation cues, body spacing and life/clock/round display |
| Objective | `OBJ-259` | required wins including the spatial terminal |
| Time | `TIM-003` | simultaneous live progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `454` (`GAME-0001`–`GAME-0454`).
- Exact genome matches: none.
- Tied near matches: `GAME-0393` — Mortal Kombat II (`14 / 26 = 0.538462`).
- Supported combination subsets: none.
- Scan date: 2026-09-30.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0393` — Mortal Kombat II | ACT-008, ACT-202, ACT-294, ACT-295, ACT-296, ACT-297, SYS-215, SYS-522, CON-442, CON-446, INF-142, INF-209, INF-210, TIM-003 | The original SNES opponent duel shares commands, live contact and ordinary round settlement. Its side-view line and KO/time-over objective do not supply Soulcalibur's lateral finite ring, positive-life Ring Out, impact priority with counter-impact, weapon forms or charge branches. Fatalities and other excluded MK systems do not transfer. | Near, `0.538462` |

## Taxonomy impact

- Add seven Active boundaries through [TAXONOMY_CHANGE_192](../../../research/taxonomy-changes/TAXONOMY_CHANGE_192.md). Reuse the other seventeen genes without changing definitions, previous signatures or verified combinations.
- Named GAME-0455 salience review rereads this complete original-Dreamcast VS scope and partitions all admitted uses; no rarity-derived weights.

## Negative results

- Reject `CON-667` because its explicit absence of ring-out is false here, and modern walled `CON-625` because this packet selects an open-edged ring.
- Reject knife-wear `SYS-777` and undirected `ACT-425`; impact here uses height-compatible directional commands without weapon-durability expenditure. Existing `ACT-223` fits, so no duplicate impact action is added.
- Reject `OBJ-099` as an exhaustive victory boundary because its literal KO/time-over wording omits spatial round wins; preserve the earlier definition and its carriers.
- Do not infer US parity from P4's admitted arcade/Japanese basis. Indexed player-guide clauses do not supply a full verified chart. Exact final drawn VS presentation and charge coefficients remain unresolved; no later-edition rules fill those gaps.

## Delta summary

## New facts

- [Observation | Direct | High] SC-004 and SC-006 distinguish counter-impact priority and positive-life Ring Out in the original manual.
- [Observation | Direct | Medium] SC-005 retains the manual's two charge branches without a direct timing measurement.

## New genes

- [Observation | Direct | High] Seven bounded charge, recovery, impact, ring and victory records; no external novelty claim.

## New combinations

- [Observation | Direct | High] No verified new combination; all existing subsets are checked by the complete scan.

## Taxonomy changes

- [Observation | Direct | High] TAXONOMY_CHANGE_192; no prior definition or signature migration.

## New questions

- What exact original regional disc reproduces the reported defaults, charge branches, impact windows and final simultaneous VS result under recorded input? Source reconstruction is not that measurement.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0456` Alone in the Dark (1992, DOS), next approved unit after acceptance and the 30-second stop window.
- Optimisation criterion: preserve selection 034's platform and loop diversity, one complete unit and one local commit; no push or deployment.

## Why this game

- [Hypothesis | Limited | Medium] The approved Dreamcast anchor tests spatial victory and reactive priority against reused fighting boundaries rather than treating a weapon theme as a gene.
