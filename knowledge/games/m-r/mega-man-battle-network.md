---
game_id: GAME-0652
slug: mega-man-battle-network
game_title: Mega Man Battle Network
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-021
    - ACT-161
    - ACT-865
  system:
    - SYS-215
    - SYS-1883
    - SYS-1884
    - SYS-1885
  constraint:
    - CON-873
    - CON-874
  information:
    - INF-604
  objective:
    - OBJ-029
  time:
    - TIM-046
---

# Game: Mega Man Battle Network

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: original English North American commercial Game Boy
  Advance cartridge, AGB-AREE-USA, 2001. The primary footage is labelled US
  GBA. No cartridge-image checksum or executable revision was verified.
- Entry: Ms. Mari's third introductory classroom battle, the pop quiz at
  the end of the first virus-busting lesson. MegaMan.EXE has 100 HP. Three
  Mettools each start with 40 HP and the Custom Screen offers five chips.
- Primary decision loop: defer the first chip selection with ADD, steer
  and fire Mega Buster while the gauge fills, reopen the selection window
  and send available compatible chips. Return to live play and combine
  ordinary fire with deliberate use of the next readied chip.
- Exit: delete all three Mettools. The battle closes, Ms. Mari ends class,
  and the recording shows Lan moving around the classroom again before
  starting an optional match with Dex.
- Included: the timed battle and paused chip preparation, visible offer
  and compatible send, chipless deferral, side-owned movement panels,
  row-based Buster fire and dodging, chip expenditure and classroom return.
- Excluded: the first two teaching encounters as gameplay scopes, Steal as
  an executed attack, the optional Dex battle, ordinary loot and Busting
  Level payout, deck editing, Program Advance, failure and save recovery,
  link play, Japanese versions, Wii U and the Legacy Collection itself.
- Suggested later scope: compare two consecutive ADDs, mixed-code
  selection rejection and ordinary post-battle grade and rewards.

## Direct-play status

No direct play was performed. Capcom's release history and a photograph
of the North American cartridge establish the selected product. The
Nintendo-hosted original European GBA booklet and Capcom's later manual
for the first title corroborate common rules. Both are distinguished
from execution on the North American cartridge. The US-labelled GBA
recording by xRavenXP and a separate original-game walkthrough by
RoahmMythril demonstrate the classroom result and different chip uses.
Frames and on-screen text were inspected in the background without audio.
Physical hardware, recorded button presses and the exact build of either
capture are unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| BN1-001 | The original Capcom release is a 2001 Game Boy Advance game. The North American label identifies AGB-AREE-USA. The packet starts at the third classroom fight with 100 player HP, three 40-HP Mettools and five initial chips. | Observation | Corroborated | High | P1, P2 for product; W1 14:10–15:04, W2 06:17–06:33 and R1 for the encounter. No exact cartridge revision is inferred. |
| BN1-002 | In the Custom Screen, the player can view chip names and letter codes and commit one or more eligible chips. Grouped chips can share a name or a letter, with a five-entry send capacity. Selected order is the use order. | Observation | Corroborated | High | P3 PDF pp. 9–10 and P4 selection and live screens. W1 11:25–12:34 teaches name, code and order before the scoped battle; W1 15:20–15:29 and W2 06:45–06:54 show actual choices. A mixed-code counterfactual was not played. |
| BN1-003 | ADD selected with no chips sent begins a live interval without a chip. It grants five more choices at the next opening. The instruction documents a second consecutive ADD and restoration of ordinary offer size after sending a chip. | Observation | Corroborated | High | W1 14:20–15:08 and W2 06:24–06:34; P3 PDF p. 10 and P4. Both fights exercise one ADD. A second ADD is documented and not observed here. |
| BN1-004 | The active field has three rows and six columns in this lesson. Ordinary movement stays on the three friendly columns. Buster shots and hostile waves can cross the ownership divide along a row. Moving to another row can avoid an approaching wave. | Observation | Corroborated | High | P3 PDF p. 10 and P4 confirm side ownership and Buster fire. W1 15:09–15:19 and W2 06:34–06:45 show stepped movement, firing and crossing projectiles. No exact hitbox, frame timing or panel reassignment is inferred. |
| BN1-005 | The Custom Gauge fills in live play. Opening the chip interface holds enemy and player action. One ADD expands the next offer from five to ten; the held enemies keep their positions and HP across transmission. The next live interval restarts the gauge. | Observation | Corroborated | High | W1 15:09–15:29 with fixed enemy HP 23, 6 and 40 during choice; W2 06:34–06:55 and 07:03 with a full meter in live play; P3 PDF p. 10, P4 and R1. Exact fill time and early-input buffering are unmeasured. |
| BN1-006 | From ten visible options W1 sends one MiniBomb C with 50 shown attack power, uses it in live play, and resumes Buster fire with the chip indicator gone. W2 instead sends Cannon B. | Observation | Corroborated | High | W1 15:20–15:37 and W2 06:45–07:06. P3 PDF p. 10 and P4 explain separate chosen chip use. The menu coefficient is not an inferred hit calculation. |
| BN1-007 | Clearing three enemies closes the battle. Ms. Mari announces class completion. Lan then moves around the physical classroom. Neither recorded quiz closeout displays the ordinary itemised Busting Level and GET DATA screen. | Observation | Corroborated | High | W1 15:35–15:43, 16:04–16:19; W2 07:03–07:16; R1. P3 PDF p. 11 describes the distinct ordinary battle result outside this exercise. |

## Basic data

- Analysis target: `PLAT-GAME-BOY-ADVANCE`, 2001 original North American
  cartridge, AGB-AREE-USA.
- Developer and publisher: Capcom.
- Mechanical families: `FAM-009`, tactical forecast and counterplay, and
  `FAM-010`, real-time system pressure.
- Checked: 2026-11-23.
- P1: [Capcom 2005 annual report and release timeline](https://www.capcom.co.jp/ir/english/data/pdf/2005annual/Annual2005e.pdf).
  Establishes the original Game Boy Advance title and year. Its Japanese
  March release entry is not the North American street date.
- P2: [North American catalogue and cartridge photos](https://www.vgcollect.com/item/2660).
  The original label bears AGB-AREE-USA. The listing is used for edition
  identification rather than to choose a day of regional release.
- P3: [Original European GBA instruction booklet, English pages](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/game_boy_advance_8/Manual_GameBoyAdvance_MegaManBattleNetwork_EN_DE_FR_ES_IT.pdf).
  Nintendo-hosted scan of AGB-AREP-EUR. PDF pp. 9–11 document choosing,
  adding and using chips, territories, the gauge and ordinary results.
  Cross-check the shared rules against the US capture before applying them.
- P4: [Capcom battle manual for the first title in Legacy Collection](https://game.capcom.com/manual/REXEAC/vol1/en/steam/page/1/2).
  Later corroboration of common choices, transfer and battle screens, not
  evidence for the selected hardware or its physical buttons.
- W1: [World-of-Longplays US GBA recording played by xRavenXP](https://www.youtube.com/watch?v=-TrutmFRTtU&t=852s).
  The third classroom fight from the quiz through MiniBomb use and return.
- W2: [RoahmMythril original-game school walkthrough](https://www.youtube.com/watch?v=bOeMF0L0Wlw&t=378s).
  Independent early recording with a different offered hand and use of
  Cannon in the third fight. It predates the Virtual Console and collection
  releases; its precise cartridge pressing is not established.
- R1: [Dev's 2001 original-GBA walkthrough](https://gamefaqs.gamespot.com/gba/457634-mega-man-battle-network/faqs/14499).
  The Custom Meter and School sections corroborate the separate three
  exercises and ordinary classroom movement after the final one.

## Mechanical decomposition

### Action Genes

- ACT-008: move MegaMan between neighbouring available friendly panels to
  line up attacks or leave a threatened row.
- ACT-021: select and send a bounded subset from the visible chip offer.
- ACT-161: align the Buster's row with a hostile target and fire.
- ACT-865: open a live interval without sending chips by choosing ADD for
  the next selection.

### System Behaviour Genes

- SYS-215: resolve live shots, hostile actions and losses during direct
  control.
- SYS-1883: expose and consume transferred chips one at a time in selected
  order, leaving ordinary weapon use available between chip actions.
- SYS-1884: retain the initial offer and expand the next opening after the
  live chipless interval.
- SYS-1885: fill the Custom Gauge automatically, enable a manual return
  to preparation at full, and resume from a reset gauge after sending.

### Constraint Genes

- CON-873: restrict multi-chip sends to a common name or code and a separate
  maximum transfer size independent of offer width.
- CON-874: restrict ordinary orthogonal movement to currently friendly
  panels, independently of which lanes can carry fire.

### Information Genes

- INF-604: expose the selectable chip details and order in preparation,
  and health, positions, next chip, remaining entries and recharge in live
  action.

### Objective Genes

- OBJ-029: delete all three Mettools to clear the bounded battle.

### Time Genes

- TIM-046: suspend player action, enemy progression and live readiness
  while selecting chips. A transfer or the explicit ADD branch resumes
  real-time play.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| Initial five-chip view and three 40-HP enemies | Confirm ADD with no selection | Live battle starts without a chip. The Buster can fire and the Custom Gauge begins to fill | BN1-001, BN1-003 |
| Three-by-six active panel field | Move to the friendly edge and fire along the centre lane, change rows around the waves | Waves cross into friendly territory. Enemy health falls without spending a chip | BN1-004 |
| Custom Gauge is full after the chipless interval | Reopen the selection view | Ten choices are visible and the surviving enemies hold at 23, 6 and 40 HP in W1 | BN1-005 |
| Ten visible choices and an empty selected column | Send MiniBomb C, then use it in the live field | Its 50-power listing is replaced by the live head indicator, which disappears on use. Buster fire continues | BN1-002, BN1-006 |
| Final live enemies remain | Finish the remaining targets and allow the lesson to close | The third encounter ends, Ms. Mari closes class, and Lan moves again beside the classroom desks | BN1-007 |

## Strategic and experiential structure

Waiting for a broader choice has a live cost. The player must keep the
nearest row safe without a chip until a fresh selection becomes possible.
The Buster is still useful during the wait and after the selected chip is
spent. Enemies in the two nearest rows invite close-range shots, but the
same alignment creates exposure to their waves. Meanwhile a widened offer
only creates alternatives. It does not make unrelated chips jointly legal.

## Replay and variation

The two captures have different initial offers and choose different chips
from the expanded offer. Their shared ADD interval and final classroom
return verify the general arc without requiring a single documented damage
sequence. The exact 23, 6 and 40 HP staging values belong to W1.

## Adjacent systems and history

The earlier two teaching fights introduce compatible chips and Steal.
Those explanations corroborate the governing selection rules, while their
executed attacks do not extend the target signature. Later ordinary fights
add result grades and itemised rewards. Those settlement rules require
later evidence and are excluded from the classroom quiz.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-021, ACT-161, ACT-865 | Steer, send visible choices, use the Buster and defer loadout |
| System Behaviour | SYS-215, SYS-1883, SYS-1884, SYS-1885 | Resolve combat, spend the queue head, widen the offer and unlock preparation |
| Constraint | CON-873, CON-874 | Govern compatible sends and side-owned movement |
| Information | INF-604 | Show combat and preparation status in their separate views |
| Objective | OBJ-029 | Remove the three required enemies |
| Time | TIM-046 | Freeze action and recharge in the command view |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `651` (`GAME-0001`–`GAME-0651`).
- Exact genome matches: none.
- Tied near matches: `GAME-0550` — Ghost of Yōtei (`4 / 18 = 0.222222`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Ghost of Yōtei (GAME-0550)](../g-l/ghost-of-yotei.md) | ACT-008, ACT-161, OBJ-029, SYS-215 | Both put direct movement and aimed attacks inside live encounters whose required opposition must be removed. Atsu reads a single opponent and creates counterattack openings with a held guard. MegaMan moves among side-owned panels, uses lane fire and separately makes paused chip decisions that shape later active commands. | Near, `0.222222` |

## Taxonomy impact

ACT-865 explicitly trades all current transferred options for a later
expanded offer. SYS-1884 owns retention and later expansion of that offer.
SYS-026 replaces consumed hand positions and does not provide the current
chipless interval. SYS-090 executes its queued attacks as one uninterrupted
command. SYS-1883 instead consumes the queue head for each separate command
within live play. TIM-046 covers the paused window. SYS-1885 covers its
full-gauge eligibility rather than the pause itself. SYS-813 concerns a
real-time phase with evasion only. The live phase here accepts direct
attacks and movement. CON-873 and CON-874 separate chip eligibility from
spatial ownership.

## Negative results

- The ADD branch does not give an immediate redraw. It starts live play
  without a transferred chip, while ordinary Buster fire remains usable.
- A visible ten-chip offer is not ten usable attack slots and does not
  remove the compatibility condition.
- The scoped quiz closes on teacher dialogue followed by Lan's movement,
  not a documented ordinary loot payout or a new optional fight.
- The recorded interval supplies no exact gauge coefficient, random seed
  or terminal failure behaviour.

## Delta summary

Thirteen scoped genes, with seven additions and six reuses. The packet is
one initial classroom battle with two live intervals and a witnessed exit.

## New facts

- A player can voluntarily forego a tactical loadout while retaining
  ordinary control and basic fire during the next timing interval.
- The subsequent wider offer retains a separate restrictive send rule.
- Prepared chip use is individually triggered from the next queue slot
  while movement, hostile attacks and readiness continue in real time.

## Principles and design implications

Keep the preparation clock and field clock visibly distinct. A wide future
offer becomes valuable when giving up the current offer still leaves an
interesting fallback. Separate the size of the visible choice from both
its compatibility rule and the capacity of the ready queue.

## Puzzle or game generation potential

Use three controllable lanes split by a firm movement boundary. Make
low-power fire always available and offer typed single-use attacks at
paused preparation breaks. Let the player defer the current attack queue
at the cost of surviving until one more preparation break.

## New genes

- ACT-865
- SYS-1883
- SYS-1884
- SYS-1885
- CON-873
- CON-874
- INF-604

## New combinations

None. All 274 verified combination signatures were checked.

## Taxonomy changes

[TAXONOMY_CHANGE_398](../../../research/taxonomy-changes/TAXONOMY_CHANGE_398.md).

## New questions

What does a second ADD retain among the ten earlier choices? Can partial
completion of a visible same-name group admit a mixed-code third choice?
Use matched cartridge traces with inputs and no incidental battle upgrades.

## Next recommended game

A Quiet Place: The Road Ahead, commercial native English Xbox Series X|S
base game. Trace one early noise-sensitive encounter to verified bypass
or response and one playable successor.

## Why this game

The quiz isolates the opportunity cost of postponing a prepared attack
choice while the same fight continues with ordinary movement and fire.
