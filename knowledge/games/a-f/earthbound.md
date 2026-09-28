---
game_id: GAME-0435
slug: earthbound
game_title: EarthBound
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-019
    - ACT-131
  system:
    - SYS-355
    - SYS-362
    - SYS-380
    - SYS-1139
    - SYS-1140
    - SYS-1141
  constraint:
    - CON-269
    - CON-282
  information:
    - INF-119
  objective:
    - OBJ-250
  time:
    - TIM-003
---

# Game: EarthBound — the first Giant Step sanctuary

Use the [canonical vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Ness, Onett, the Sound Stone, Giant Step, Titanic Ant, the two Black Antoids, PSI Rockin, PP and the sanctuary melody are carrier parameters, not universal gene names.

## Analysis scope

- Version / ruleset: original 1995 North American English *EarthBound* for the Super Nintendo Entertainment System, not *EarthBound Beginnings*, a later Virtual Console or Nintendo Switch Online wrapper, a translation patch, randomizer, ROM hack or emulator-enhanced ruleset. Nintendo's 1995 Player's Guide governs the original route; the later official digital instruction manual corroborates core controls and battle menus but is not evidence of a new original-cartridge revision.
- Structured analysis target: `PLAT-SUPER-NINTENDO` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Scenario: Ness has already received Buzz Buzz's Sound Stone, defeated Frank at the Arcade and received the cabin key from Onett's Mayor. Start outside the now-accessible cabin north of town with ordinary campaign state and sufficient HP, PP and a carried recovery item; traverse the first cave, settle one normal visible-hostile contact, defeat Titanic Ant and its two Black Antoids, then walk to Giant Step until the first melody is recorded. Level, damage rolls and remaining resources are parameters, not asserted fixed values.
- Primary decision loop: move through visible cave enemies and choose an approach; when a battle opens, select Bash, a PP-funded PSI effect or a carried healing Good from the menu, watch Ness's rolling HP and choose whether to heal or finish the hostile set before the counter reaches zero. After the guardian falls, take the newly open route to the sanctuary so the carried Sound Stone records the melody.
- Entry: ordinary Ness control at the opened cabin before cave entry, with the key gate satisfied and no boss defeat or first sanctuary melody recorded. This is a bounded continuation save, not a claim that every new game starts here.
- Positive terminal: Titanic Ant and its two Black Antoids are defeated, the blocked passage opens, and the Sound Stone records the first Giant Step melody when Ness visits the sanctuary. Stop before the return through the cave or the Onett police sequence.
- Failure and recovery: a falling HP counter that reaches zero before the battle is settled makes Ness unconscious; the selected attempt does not achieve the terminal. The official later manual describes a Continue path with PP loss and carried-money reduction, but that recovery is outside this packet. Neither a gold-style grade nor an exact number of turns is required.
- Included: ordinary cave movement, one comparable visible cave hostile contact and its possible front/back opening advantage, one finite command battle, the scripted Titanic Ant battle with two supporting Black Antoids, Bash/PSI/Goods decisions, PP and carried item costs, current HP/PP display, HP decrement over live time, combat experience, guardian clearance, newly reachable sanctuary and automatic Sound Stone melody record.
- Excluded: a fresh meteorite-to-Frank opening, full Onett or Twoson exploration, banking and shopping, phone saving, equipment optimization, optional Magic Butterfly replenishment, comprehensive ailments and PSI catalogue, weak-hostile instant victories, exact boss damage statistics, all later sanctuaries and the full campaign. The conceptual illustration does not assert that the field and battle view share one screen.
- Reproducible parameterisation: use a normal unmodified original campaign state after the Mayor-key gate; approach a comparable roaming cave hostile without relying on instant victory; before the Shining Spot retain enough HP and PP to use an available offensive PSI and healing option. Trigger Titanic Ant at the spot, settle its finite group, then enter Giant Step. Exact enemy contact position, opening side, initiative, damage, consumed items, level and remaining health vary. The boss group, victory gate and first melody do not.
- Potential scoped modules: an exact original-ROM battle scheduler and HP tick rate; auto-victory against weak field enemies; full defeat/Continue accounting; Magic Butterfly replenishment; later eight-melody collection.
- Direct-play status: no original cartridge, executable, save, controller trace, screenshot, video or audio was inspected. Nintendo's original guide was visually read at pages 9–12 and 22–23; the later official manual and an independent first-hand written SNES walkthrough corroborate the battle controls and boss route. Exact cartridge revision and timing constants remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `EB-001` | The original North American SNES route opens Giant Step's cabin after Frank and the Mayor, then reaches the cave guardian. | Confirmed | Direct | High | P1 pp. 22–23 |
| `EB-002` | Visible field hostiles enter separate battles on contact; the approach side can confer an opening attack. | Confirmed | Direct | High | P1 p. 10, P2 p. 6 |
| `EB-003` | Ness selects Bash, PSI, Goods, Defend or Run Away in battle; PSI spends PP and Goods use carried items. | Confirmed | Direct | High | P1 p. 11, P2 pp. 5–6 |
| `EB-004` | The HP display decreases gradually after damage; defeating the hostile set before it reaches zero can prevent unconsciousness. | Confirmed | Direct | High | P1 p. 11 |
| `EB-005` | Titanic Ant is accompanied by two Black Antoids; the guardian blocks the path to Giant Step. | Confirmed | Direct | High | P1 p. 23, S1 |
| `EB-006` | After the guardian is defeated and Ness reaches the sanctuary, the Sound Stone records its first melody. | Confirmed | Direct | High | P1 p. 23, S1 |
| `EB-007` | A Battle command resolves against eligible hostile responses and returns to command choice while the encounter remains open. | Observation | Corroborated | High | P1 pp. 10–11, P2 p. 6 |
| `EB-008` | A carried healing item or PSI can restore HP during an eligible battle, but the sources do not establish exact tick speed or a guaranteed rescue after every mortal hit. | Observation | Corroborated | Medium | P1 pp. 11–12, P2 pp. 3, 5–6 |

## Basic data

- Release / origin: original English North American Super Nintendo *EarthBound*, 1995. The Japanese *MOTHER 2* and modern wrappers are not silently conflated with this packet.
- Platform or physical form: original Super Nintendo Game Pak, directional control and command menus. The later digital manual is a corroborating documentation source, not the analysed distribution.
- Mechanical families: tactical forecast and counterplay (`FAM-009`), real-time system pressure (`FAM-010`) and ordered dependency sequencing (`FAM-017`). The live pressure is the rolling HP counter inside otherwise menu-commanded battles, not real-time enemy movement while the battle menu is open.
- **P1**: [Nintendo of America's original EarthBound Player's Guide, hosted by Nintendo](https://www.nintendo.co.jp/clvs/manuals/common/pdf/CLV-P-SAAJE.pdf), pp. 9–12 and 22–23: field contact, battle menu, rolling HP, cave access, Titanic Ant and Sound Stone (visually inspected 2026-09-27). This is the original 1995 guide; its PDF is image-only and the cited pages were rendered rather than inferred from OCR.
- **P2**: [Nintendo's later digital instruction manual](https://www.nintendo.com/es-es/games/oms/snes-classic/manuals/earthbound/manual.pdf), pp. 3, 5–6: party resources, field encounter, battle commands, healing and failure continuation (accessed 2026-09-27). Its Wii U-specific UI lines are excluded from the original-cartridge rules.
- **S1**: [Kodos86's first-hand original-SNES walkthrough](https://gamefaqs.gamespot.com/snes/588301-earthbound/faqs/14736), Giant Step/Titanic Ant segment: supporting Black Antoids and melody after the boss (accessed 2026-09-27). The walkthrough corroborates the route; Nintendo's original guide remains authoritative.
- Claim IDs: `EB-001`–`EB-008`.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for Ness's controllable cave traversal toward a visible enemy and the post-boss sanctuary.
- Reuse `ACT-019` for choosing one Bash target or eligible PSI effect/target in a battle menu; the enemy's automatic resolution is not this action.
- Reuse `ACT-131` for spending one carried immediate-effect recovery Good at a legal battle opportunity.

### System Behaviour Genes

- Reuse `SYS-355` for ordinary visible cave contact and the possible rear-approach opening advantage, not the scripted Shining Spot guardian trigger.
- Reuse `SYS-362` for encounter experience and credit; do not classify the later sanctuary melody as a boss drop.
- Reuse `SYS-380` for the selected PSI's damage or healing effect, not Ness's ordinary Bash.
- Add `SYS-1139` for battle command and hostile-response resolution among surviving actors without claiming Pokémon Red's paired move-priority schedule.
- Add `SYS-1140` for damage first setting a target HP value while the visible counter rolls toward it, leaving a bounded opportunity to heal or end the encounter before zero.
- Add `SYS-1141` for the accessible sanctuary's melody entering the carried Sound Stone only after the guardian is gone and Ness reaches the site.

### Constraint Genes

- Reuse `CON-269` for a PSI command's learned-power, target and PP legality. Basic Bash does not consume PP.
- Reuse `CON-282` for the ordered route: prior Mayor-key access admits the cave, and the guardian must be defeated before the first sanctuary can be reached. The earlier Frank fight is an entry precondition, not replayed inside this packet.

### Information Genes

- Reuse `INF-119` for Ness's visible HP/PP and available PSI state. The rolling display reveals current HP, not the exact future action or a guaranteed time-to-zero prediction.

### Objective Genes

- Add `OBJ-250`: defeat the mandatory first-sanctuary guardian, cross its opened path and retain the Sound Stone's recorded melody. Stopping at boss victory alone is incomplete.

### Time Genes

- Reuse `TIM-003` only for the HP counter advancing in real time while the next battle menu decision is still possible. It does not imply that enemies roam in real time inside the command screen or that PSI has a continuous action clock.

## Reproducible transitions

| Before | Player input | Bounded resolution | Mechanic established | Claim ID |
|---|---|---|---|---|
| Cabin is open and Ness can move | Traverse the cave toward a comparable visible hostile | Contact transfers Ness and the local foe into a battle; the approach side may change the opening | authored field encounter rather than random grass sampling | `EB-001`, `EB-002` |
| One battle menu is available | Select Bash or a legal PSI target | Ness's command and eligible hostile actions resolve in battle order; the next menu follows if both sides remain | menu command and response loop | `EB-003`, `EB-007` |
| Ness takes a damaging hostile action | Observe HP; commit a recovery Good or suitable PSI, or finish the hostile set | the displayed counter rolls toward the lower target; timely recovery or victory can prevent zero | delayed HP settlement while input remains possible | `EB-004`, `EB-008` |
| Shining Spot is reached with usable HP/PP | Enter the guardian battle, use available offence and recovery against the boss group | the two supporting Black Antoids and Titanic Ant form a finite hostile set; victory opens the onward passage | bounded guardian combat | `EB-003`, `EB-005` |
| Titanic Ant is defeated | Walk through the opened passage to Giant Step | the sanctuary melody plays and is recorded in the Sound Stone | separate post-battle retained result | `EB-006` |

## Strategic and experiential structure

- Immediate choice: weigh Bash's no-PP cost against a PSI effect's PP cost or a carried heal, while the rolling HP display may make delay costly after a strong hit.
- Medium-term plan: preserve enough resources through a normal cave contact to meet the boss and its two supporters; a victory over a weak hostile is not the first-sanctuary terminal.
- Long-term boundary: the first melody becomes retained progress. Gathering the other seven melodies and completing the campaign are outside this analysis.
- Failure attribution: losing Ness before the guardian falls does not create a melody; the guide does not license a precise universal rescue window from every damage value.

## Replay and variation

The visible-hostile position, encounter approach, damage, turn sequence, remaining PP and item use can vary. The authored boss group and first-sound recording are fixed for this route. The packet does not infer stochastic sanctuary selection or a fixed number of combat turns.

## Adjacent systems and history

*Pokémon Red Version* (`GAME-0336`) also has command battles and persistent party resources, but its two committed creature commands settle by move priority and Speed before the next menu. EarthBound's distinctive hazard is a damaged hero's still-rolling HP during subsequent decisions. *Chrono Trigger* (`GAME-0346`) also converts world movement into battle, but its personal Active Time gauges are not EarthBound's turn-menu schedule.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-019`, `ACT-131` | Ness traversal, battle choice and recovery Good |
| System Behaviour | `SYS-355`, `SYS-362`, `SYS-380`, `SYS-1139`, `SYS-1140`, `SYS-1141` | field contact, experience, PSI, menu replies, rolling HP and melody |
| Constraint | `CON-269`, `CON-282` | PP/legal target and guardian route gates |
| Information | `INF-119` | HP/PP and available PSI |
| Objective | `OBJ-250` | first sanctuary melody retained after guardian |
| Time | `TIM-003` | HP movement while a response remains available |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `434` (`GAME-0001`–`GAME-0434`).
- Exact genome matches: none.
- Tied near matches: `GAME-0346` — Chrono Trigger (`7 / 24 = 0.291667`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0346` *Chrono Trigger* | `ACT-008`, `ACT-019`, `SYS-355`, `SYS-362`, `CON-269`, `CON-282`, `INF-119` cover field traversal, targeted battle choice, visible encounter contact, experience, ability legality, authored gates and current character status. | Chrono Trigger's scoped Gato encounter settles through individual Active Time readiness gauges and later opens a Pendant Gate; EarthBound uses a menu-and-response battle with HP that keeps falling after damage, then requires a separate post-guardian visit to record the first Sound Stone melody. Sharing seven general route and combat boundaries does not imply the same combat clock or objective. | Sole tied-near maximum, `7 / 24 = 0.291667`; not an exact or verified-combination match. |

## Taxonomy impact

`TAXONOMY_CHANGE_172` admits three system boundaries for a menu-response battle, rolling HP and a separately recorded sanctuary melody, plus the specific bounded sanctuary objective. Existing field contact, experience credit, selected PSI effects, PP legality, character display and live clock boundaries are reused. No earlier signature or verified combination changes.

## Negative results

- `SYS-955` requires two independently fixed creature commands reordered by Pokémon move priority and Speed; EarthBound's one controlled Ness and a hostile group do not share that scheduler.
- `TIM-026` requires independently filling battle-readiness gauges; the rolling HP display is not an Active Time Battle gauge.
- `OBJ-191` requires contact with a Triforce fragment inside the cleared dungeon; the Sound Stone records a melody at a reached sanctuary after guardian defeat.
- `SYS-1137` learns an Ecco key-glyph song for a matching acoustic barrier; the Sound Stone stores a sanctuary melody without opening a same-song barrier in this packet.
- A screen-space overlay showing Ness, the guardian and a rolling meter simultaneously is not claimed; the artwork is a conceptual encounter illustration.

## Delta summary

## New facts

- [Confirmed | Direct | High] Nintendo's original guide explicitly explains that a falling HP display can be outrun by an encounter victory (`EB-004`).
- [Confirmed | Direct | High] The first sanctuary melody is recorded only after the boss is defeated and Giant Step is visited (`EB-005`, `EB-006`).

## New hypotheses

- [Hypothesis | Limited | Medium] A later scoped exact-ROM study could measure HP tick speed and whether every healing action interrupts a lethal countdown; neither is inferred here.

## New genes

- [Confirmed | Direct | High] Four typed boundaries are admitted in `TAXONOMY_CHANGE_172` for battle resolution, rolling HP, a recorded sanctuary melody and the bounded guardian-to-site objective.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_172`; earlier signatures unchanged.

## New questions

- Can an exact original-cartridge program trace separate battle-order scheduling from the HP-counter clock at different menu text speeds?

## Next game

`GAME-0436` *Journey*, original PlayStation 3, is next after the Goal stop window. The research question is how cloth energy, movement and anonymous cooperation govern one passage; no mechanics are presumed from selection alone.
