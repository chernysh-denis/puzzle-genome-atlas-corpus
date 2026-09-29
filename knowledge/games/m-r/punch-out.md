---
game_id: GAME-0447
slug: punch-out
game_title: Punch-Out!!
analysis_status: reviewed
reviewed: 2026-09-28
combination_ids: []
gene_ids:
  action:
    - ACT-295
    - ACT-296
    - ACT-356
    - ACT-586
    - ACT-587
  system:
    - SYS-215
    - SYS-1172
    - SYS-1173
    - SYS-1174
  constraint:
    - CON-442
    - CON-722
  information:
    - INF-142
    - INF-432
  objective:
    - OBJ-256
  time:
    - TIM-003
---

# Game: Punch-Out!! — first Glass Joe bout

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). A boxer, controller button, star, heart and round duration are parameters of this edition; they are not each separate genes.

## Analysis scope

- Version / ruleset: Nintendo's 1990 NES *Punch-Out!! Featuring Mr. Dream* as documented by the official NES Classic manual. This is the non-Tyson edition, not the arcade title, Wii reboot or *Super Punch-Out!!*.
- Primary decision loop: read the opponent's visible attack motion, choose a timed weave, duck or block, counter with a legal body or face punch during an opening, decide whether to spend an earned star on an uppercut, and manage hearts, stamina and knockdowns until the bout settles.
- Entry: choose NEW and enter the first Minor Circuit fight against Glass Joe with Little Mac. The official game description names both fighters; the manual specifies NEW, boxing controls and match rules, but does not give a frame-by-frame Glass Joe script.
- Positive terminal: win that first fixed bout by knockout, three opposing knockdowns within one round (TKO), or favourable points after three three-minute rounds. The packet does not assume which route a particular unplayed attempt achieves.
- Failure: Mac can lose by the same bout rules; a knockdown permits rapid A/B presses to rise before the referee's count reaches ten. Three lost matches across the wider career end the game, but that career terminal is not the local bout objective.
- Included: Little Mac's face/body punches, timed weave/duck and held block; opponent attack cues and contact; hearts restricting attacks when empty; star acquisition by certain hits, star uppercut and star loss on hit, knockdown or round end; separate stamina bars, knockdown recovery, the once-per-fight between-round SELECT stamina recovery, round clock, points and KO/TKO/decision settlement.
- Excluded: exact Glass Joe attack frames, undisclosed star-award combinations, guaranteed knockout route, later opponents and circuits, pass keys, Tyson-edition differences, Wii motion controls, training between bouts and exact numeric damage values.
- Reproducible source-derived path: choose NEW, start the first bout, observe an incoming punch, weave or duck in time, answer with a legal punch, inspect the heart/star/stamina HUD, and continue until one of the documented result conditions settles. This is a manual reconstruction rather than a captured winning run.
- Direct-play status: no NES cartridge, ROM execution, save, controller trace, video or audio was inspected. The original Nintendo manual establishes the controls and result rules. Exact opponent-specific timing and a specific win trace remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PO-001` | NEW begins at the start; Little Mac boxes through the Minor Circuit and Glass Joe is an NES opponent. | Observation | Direct | High | P1, P2 |
| `PO-002` | A/B request left/right body blows; holding up makes face jabs; the directional pad permits timed dodge, duck and held block. | Observation | Direct | High | P1 pp. 2–3 |
| `PO-003` | Missed punches or incoming blows reduce hearts; at zero hearts Mac temporarily cannot attack. | Observation | Direct | High | P1 p. 7 |
| `PO-004` | Certain landed hits award stars; a held star permits START uppercut; an opponent hit removes one star, while knockdown or round end removes all. | Observation | Direct | High | P1 pp. 2, 7 |
| `PO-005` | Incoming hits reduce Mac's stamina; zero causes knockdown, and repeated A/B presses can return him before the ten-count. | Observation | Direct | High | P1 pp. 2, 7 |
| `PO-006` | A match has at most three three-minute rounds; KO, three knockdowns in one round or points after the bell settle a victory. | Observation | Direct | High | P1 p. 5 |
| `PO-007` | The HUD shows both stamina bars, hearts, stars, round, remaining time and points. | Observation | Direct | High | P1 p. 6 |
| `PO-008` | No exact Glass Joe attack script, frame window, result trace or original NES play was verified. | Confirmed | Direct | High | R1 |
| `PO-009` | Pressing SELECT between rounds can restore some stamina, once per fight. | Observation | Direct | High | P1 p. 2 |

## Basic data

- Origin: Nintendo's 1990 NES *Punch-Out!! Featuring Mr. Dream*, preserving the original boxing rules described in its official booklet.
- Platform: NES controller and original bounded boxing bout; the structured analysis target is in `knowledge/platforms/games.json`.
- Mechanical families: tactical forecast and counterplay (`FAM-009`) and real-time system pressure (`FAM-010`).
- **P1:** [Nintendo's official NES Classic manual for *Punch-Out!! Featuring Mr. Dream*](https://www.nintendo.co.jp/clv/manuals/en/pdf/CLV-P-NAATE_en.pdf), inspected 2026-09-28, pp. 2–7. This publisher artefact is rules evidence, not direct-play capture.
- **P2:** [Nintendo's NES product description](https://www.nintendo.com/es-es/Juegos/NES/Punch-Out--278656.html), inspected 2026-09-28, names Little Mac and Glass Joe and distinguishes the NES title.
- **R1:** local preflight found no original executable or direct-play trace for this unit.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-295` for body blows, face jabs and star uppercuts as directly controlled fighter attacks. Controller combinations and hand/target are parameters.
- Reuse `ACT-296` for held block and `ACT-356` for a committed lateral weave or duck; a timed evasion is not passive defence.
- `ACT-586` is the repeated A/B recovery input after Mac falls. It does not cause a punch while he is standing.
- `ACT-587` is the once-per-fight SELECT choice between rounds to restore some stamina. It is not the repeated A/B knockdown recovery input.

### System Behaviour Genes

- Reuse `SYS-215` for live exchange of opposing punches, defence and damage. The specific Glass Joe move schedule is not claimed.
- `SYS-1172` reduces hearts on misses or received blows and temporarily disables punching at zero hearts; this attack permission differs from stamina-based knockdown.
- `SYS-1173` awards stars for eligible landed hits, spends one on an uppercut and removes stars on the documented hit/down/round transitions.
- `SYS-1174` adjudicates boxing knockdowns and referee counts, three-in-one-round TKO, KO and the final points decision over a maximum of three rounds. These are not three independently won fighting-game rounds.

### Constraint Genes

- Reuse `CON-442` for attack/defence availability in the current standing, guarded, recovery or fallen state.
- `CON-722` gates the START uppercut on possession of at least one star. The star ledger is separate from hearts and stamina.

### Information Genes

- Reuse `INF-142` for visible punch animation as a timing cue; no exact frame preview or guaranteed tell is asserted.
- `INF-432` exposes paired stamina, Mac's hearts and stars, round clock, round number and points in one bout HUD.

### Objective and Time Genes

- `OBJ-256` is a first fixed boxing-bout win by one of the official settlement routes, not winning multiple independent fighter rounds or a whole circuit.
- Reuse `TIM-003` because the opponent and match clock continue during player input.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Why it matters | Claim ID |
|---|---|---|---|---|
| Opponent begins a punch; Mac standing | Weave, duck or hold block in time | Incoming contact can be avoided or defended; a subsequent counter remains a separate input | Defence precedes offence, with no exact frame claim | `PO-002` |
| Mac standing and a face/body target is available | B/A, optionally with up | A legal punch is attempted; contact is resolved separately | Button and posture select attack type | `PO-002` |
| A punch misses or an opposing blow lands | Continue bout | Heart stock falls; at zero, attacking is briefly unavailable | Hearts are an offence gate, not the stamina bar | `PO-003` |
| Mac has a star | Press START | One stocked uppercut is requested and the star is consumed | Star-gated attack is not an ordinary jab | `PO-004` |
| Mac is knocked down | Tap A/B repeatedly before ten-count | He can rise and continue; failure to beat ten ends in KO | Knockdown recovery is an active input | `PO-005` |
| Opponent has fallen three times in one round | Referee settles that round | TKO ends the bout immediately | Knockdowns are not round-win markers | `PO-006` |
| Three rounds expire without KO/TKO | Compare points | A points decision settles the bout | Time expiry is not automatic victory for Mac | `PO-006` |
| A round ends and SELECT recovery is unused | Press SELECT before the next round | Some stamina can be restored and that between-round recovery is no longer available in this fight | One-use interval action, separate from rising under count | `PO-009` |

## Strategic and experiential structure

The decision is when to defend and when to risk a counter. A missed attack spends hearts, so indiscriminate punching can temporarily remove the ability to attack even before Mac loses all stamina. A star offers a stronger uppercut, but taking a hit can erase it. If the bout reaches another round, the one-use SELECT recovery adds a separate allocation choice. The boxing clock and knockdown count make waiting, evasion and attack timing matter. The official booklet does not quantify Glass Joe's individual openings; this packet does not claim a speedrun route or a guaranteed knockout sequence.

## Replay and variation

Changing punch/evasion timing and star use can change damage, hearts, knockdowns and the settlement route within the same fixed bout. No randomized opponent pool, procedural ring or exact timing distribution is asserted.

## Adjacent systems and history

*Street Fighter II* also has timed attacks and defence, but wins separate health-reset rounds in a freely paced versus match. This NES boxing packet counts falls within a round toward a TKO, carries a distinct heart attack gate and star uppercut stock, and can settle the bout by points after the third bell. The 1990 Mr. Dream edition avoids conflating this analysis with the Tyson-branded 1987 cartridge or later Wii version.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-295`, `ACT-296`, `ACT-356`, `ACT-586`, `ACT-587` | punch/uppercut, guard, weave/duck, rise, one-use rest |
| System Behaviour | `SYS-215`, `SYS-1172`, `SYS-1173`, `SYS-1174` | contact, hearts, stars, boxing settlement |
| Constraint | `CON-442`, `CON-722` | actionable fighter, star prerequisite |
| Information | `INF-142`, `INF-432` | attack cue, bout HUD |
| Objective | `OBJ-256` | first fixed bout win |
| Time | `TIM-003` | real-time three-minute rounds |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `446` (`GAME-0001`–`GAME-0446`).
- Exact genome matches: none.
- Tied near matches: `GAME-0351` — Street Fighter II: The World Warrior (`6 / 24 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-09-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0351` — Street Fighter II: The World Warrior | `ACT-295`, `ACT-296`, `SYS-215`, `CON-442`, `INF-142`, `TIM-003` | Both use directly controlled live strikes, guard and attack cues in a fixed opponent fight. Street Fighter II awards separate round wins after health resets; this NES boxing bout counts falls within one round toward TKO, separately gates attacks by hearts, earns/forfeits stars for an uppercut, permits one between-round stamina recovery and can finish on points after the third round. | Nearest at `6 / 24 = 0.250000`; not the same bout economy or settlement. |

## Taxonomy impact

`TAXONOMY_CHANGE_184` admits eight source-supported boundaries without revising earlier game signatures or combinations.

## Negative results

- Do not substitute Tyson or Wii rules, infer precise Glass Joe frames, or claim a specific unplayed KO route.
- Do not treat the three boxing rounds as three independent required round wins.

## Delta summary

## New facts

- [Observation | Direct | High] Hearts can temporarily disable offence before stamina reaches knockdown (`PO-003`, `PO-005`).
- [Observation | Direct | High] Star uppercuts and three-in-round TKO create different risk and settlement boundaries from ordinary versus rounds (`PO-004`, `PO-006`).

## New genes

- [Observation | Direct | High] Eight typed boundaries isolate active rising, between-round recovery, heart attrition, star economy, boxing settlement, star prerequisite, bout HUD and the first-bout objective.

## New combinations

- [Observation | Limited | Medium] None proposed; existing proper-subset support is recomputed.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_184`; no earlier signature is changed.

## New questions

- Would direct NES play reveal Glass Joe's precise visual cues and frame windows without changing the manual's general heart, star and TKO rules?

## Next game

`GAME-0448` is the next selected unit only after this unit's acceptance and Goal stop window. No push, public publication or deployment is authorised.
