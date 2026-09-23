---
game_id: GAME-0366
slug: tekken-3
game_title: Tekken 3
analysis_status: reviewed
reviewed: 2026-09-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-202
    - ACT-294
    - ACT-295
    - ACT-296
    - ACT-297
  system:
    - SYS-215
    - SYS-522
    - SYS-1000
  constraint:
    - CON-442
    - CON-446
    - CON-667
  information:
    - INF-142
    - INF-209
    - INF-210
  objective:
    - OBJ-099
    - OBJ-212
  time:
    - TIM-003
---

# Game: Tekken 3

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Jin Kazama,
Arcade Mode, four limb buttons and the 40-second setting are parameters, not
gene names.

## Analysis scope

- Version / ruleset: the original 1998 North American English Namco PlayStation
  disc, NTSC-U/C `SLUS-00402`, at the manual's default game options and
  controller mapping. This is one-player Arcade Mode with Jin Kazama fixed for
  the entire ladder. The exact disc image and executable were not obtained or
  hashed; the manual's product identity and the independent serial catalogue
  establish the intended edition, not a verified byte-for-byte build.
- Primary decision loop: read opponent distance, pose, health, timer and round
  markers; move toward, away from or around the opponent, crouch, attack with
  one of four limb commands, guard high/mid or low and attempt or break a
  throw; let live contact, knockdown and recovery settle; repeat through the
  round result, the match result and the next CPU opponent until every Arcade
  opponent is defeated. On a lost match, decide whether to continue at the
  same stage with Jin or leave the ladder.
- Entry: the character-selection confirmation of Jin in fresh one-player
  Arcade Mode with unchanged default options; the first CPU duel is about to
  begin. The selected costume is cosmetic.
- Positive terminal: Jin wins the final required CPU match and Arcade Mode
  declares the ladder clear. An ending movie or unlockable reward is outside
  this packet; the manual establishes completion without naming a precise
  stage count or fixed opponent order.
- Negative terminal: after losing a match, the player declines the Continue
  screen and leaves the Arcade attempt. A loss followed by Continue is a
  retry of that stage, not a terminal failure; continues have no stated cap.
- Reproducible route: start with the default controller layout and game
  options, choose Arcade Mode and Jin, fight each generated opponent with
  any legal movement, guard, throw or Jin attack, and keep Jin when continuing
  after a loss. Record the shown opponent, stage and round state rather than
  asserting a scripted opponent sequence. Stop at the Arcade clear or a
  declined Continue screen.
- Included: forward/back movement, dash, jump, crouch and sidestep; Jin's
  four-limb normal and directional attacks, including legal launches and
  airborne follow-ups, and four-button Super Charger with its vulnerable
  activation; high/mid/low hit classes; standing, crouching and neutral
  auto-guard; close throws and available throw escape; knocked-down recovery
  and quick roll; live contact, health depletion, 40-second default round
  timer, time-over health comparison, double-KO/equal-health draw, awarded
  round markers, match reset; Arcade stage advance and same-stage Continue.
- Excluded: a second player entering and converting the session to VS Mode;
  Team Battle, Survival, Time Attack, Tekken Force, Tekken Ball, Practice and
  custom Option settings; selecting another fighter during Continue; memory
  card records and unlocks; full Jin move/frame/damage tables, CPU policy,
  exact opponent order and count, ending cinematics, later Tekken games,
  modern Heat/Rage/recoverable-health/wall-combo mechanics and emulated ports.
- Direct-play status: not conducted. No disc, console, executable, controller
  trace, save, screenshot, video or audio was obtained or inspected. The
  original Namco manual (read through a scan transcription) supplies the
  edition's rules, with an official Namco product page and a contemporary
  PlayStation guide as corroboration. The executable control below tests only
  the stated transitions; it does not emulate PlayStation code.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TK3-001` | The target is the original North American PlayStation Tekken 3, serial `SLUS-00402`, not a later Tekken or port | Observation | Corroborated | High | P1, P2, S1 |
| `TK3-002` | One-player Arcade Mode pits the selected fighter against CPU opponents until all are beaten; continues are unlimited and retry the lost stage | Confirmed | Direct | High | P1 |
| `TK3-003` | Jin is a starting selectable fighter; selecting via punch or kick changes costume, not the fighter's identity | Observation | Corroborated | Medium | P1, S2 |
| `TK3-004` | Four separate limb buttons combine with directions for attack; stepping, dashing and lateral sidestepping change the approach axis | Confirmed | Direct | High | P1, P2 |
| `TK3-005` | High, mid and low attacks meet different standing/crouching guard and evasion states; neutral auto-guard has exceptions | Confirmed | Direct | High | P1 |
| `TK3-006` | Throws can be attempted and eligible ordinary throws escaped; knocked-down fighters can recover with a timed quick roll | Confirmed | Direct | High | P1 |
| `TK3-007` | Four-button Super Charger temporarily increases attack damage including damage through guard but leaves its user vulnerable while charging | Confirmed | Direct | High | P1 |
| `TK3-008` | Zero health awards a round; the default 40-second timer awards a timeout to the fighter with more health; equal-health timeout or double KO awards both sides a point, and a final-round Arcade draw gives Game Over to one-player play | Confirmed | Direct | High | P1 |
| `TK3-009` | Jin has launchers and airborne follow-ups in the original PlayStation version | Observation | Limited | Medium | S2; source is a contemporary player guide, not direct execution |
| `TK3-010` | This edition's fighting plane permits lateral sidestep without a modern walled-arena or ring-out settlement | Observation | Limited | Medium | P1 for sidestep; S3 for wall-less classic Tekken stage classification; no direct arena measurement |
| `TK3-011` | The local source-model control covers high/mid/low defence, round draw, match clear, same-stage Continue and Arcade clear without executing the disc | Observation | Direct | High | V1 |
| `TK3-012` | Exact stage count, opponent order, CPU behaviour, damage/frame values and disc bytes are not established by this packet | Observation | Direct | High | R1 |

## Basic data

- Release / origin: Namco, 1998; original North American PlayStation release.
- Platform or physical form: original NTSC-U/C PlayStation disc, serial
  `SLUS-00402`; one standard controller and one CPU Arcade ladder.
- Puzzle family: `FAM-009` tactical forecast and counterplay and `FAM-010`
  real-time system pressure. This carrier makes lateral spacing and guard
  level matter while successive short duels test the same selected fighter.
- Primary sources, checked 2026-09-23: **[P1]** [Namco's original North
  American PlayStation instruction manual](https://manualzz.com/doc/6957401/tekken-3---sony-playstation---manual)
  (third-party scan transcription; OCR is imperfect, so numeric and rule
  clauses were cross-read in context); **[P2]** [Bandai Namco's original
  PlayStation Tekken 3 product page](https://www.bandainamcoent.co.jp/cs/list/tekken3/)
  and its [period game-mode page](https://www.bandainamcoent.co.jp/cs/list/tekken3/topics/mode.html).
- Secondary sources, checked 2026-09-23: **[S1]** [PSX Data Center's
  `SLUS-00402` catalogue](https://psxdatacenter.com/games/SLUS-00402.html),
  for the disc serial only; **[S2]** [contemporary PlayStation Jin command
  and combo guide](https://gamefaqs.gamespot.com/ps/198900-tekken-3/faqs/6644),
  for launch/follow-up and initial-roster details; **[S3]** [Fighting Game
  Glossary: infinite stage](https://glossary.infil.net/?t=Infinite+Stage),
  for the retrospective wall-less classic-Tekken classification only.
- Reproducible control: **[V1]**
  [`verify_tekken_3_control.py`](../../../scripts/verify_tekken_3_control.py),
  an executable model of admitted state transitions, not of game code.
- Negative evidence: **[R1]** no original disc or direct audiovisual trace;
  no exact full-ladder opponent list or stage-count claim admitted.

## Mechanical decomposition

### Action Genes

- `ACT-294` commits one Jin participant at the Arcade character screen;
  control mapping stays at its default and the CPU opponents are supplied by
  the mode, not chosen by the player.
- `ACT-008` owns forward/back travel, dash, jump and sidestep on the fighting
  plane. `ACT-202` changes standing/crouched posture, with a different target
  and guard envelope.
- `ACT-295` enters Jin's legal four-limb, directional, launching or airborne
  follow-up attack. Super Charger is an attack-state parameter with a risky
  activation, not a modern meter. `ACT-296` requests standing/crouching guard;
  neutral auto-guard is a system response, not a new input gene.
- `ACT-297` enters a close throw or a matching eligible throw escape.
- Claims: `TK3-003`–`TK3-007`, `TK3-009`.

### System Behaviour Genes

- `SYS-215` resolves hit, whiff, guard, throw, launch, airborne follow-up,
  damage and knockdown using current distance, axis, pose and command state.
- `SYS-522` awards the KO, time-over or draw points, resets fighters and clock
  between rounds and settles a match at its configured required-win count.
- `SYS-1000` carries the fixed selected fighter to the next CPU stage on a
  match win or offers the same-stage Continue after a loss; declining it ends
  this Arcade attempt.
- Claims: `TK3-002`, `TK3-005`–`TK3-009`.

### Constraint Genes

- `CON-442` gates each direction/limb/throw/guard command by current pose,
  range and recovery. `CON-446` bounds a match by health, timer and the
  required round wins; the manual directly gives the 40-second default but
  does not supply a verified numeric default win count for this packet.
- `CON-667` keeps the fighters in one opponent-relative open floor plane with
  a lateral sidestep that can change the line of contact. The lack of wall or
  ring-out resolution is conservatively `Limited` rather than inferred from
  the manual alone.
- Claims: `TK3-004`, `TK3-005`, `TK3-008`, `TK3-010`.

### Information Genes

- `INF-142` exposes attack start, hit, block and recovery through visible
  motion; exact frame advantage is not claimed. `INF-209` shows both fighter
  bodies and their changing distance/axis. `INF-210` shows health, timer and
  awarded round markers; it does not import Tekken 8's Heat/Rage gauges.
- Claims: `TK3-004`–`TK3-008`.

### Objective Genes

- `OBJ-099` is the local objective of enough round wins against the current
  CPU fighter. `OBJ-212` is the distinct Arcade terminal of defeating every
  required opponent with the same selected fighter, allowing same-stage
  continues as documented.
- Claims: `TK3-002`, `TK3-008`.

### Time Genes

- `TIM-003` keeps movement, input, attack recovery and the round clock live
  together. Pause is a menu interruption, not turn-based combat.
- Claims: `TK3-004`–`TK3-008`.

## Reproducible transitions

1. Confirm Jin and start Arcade; the CPU supplies a current opponent, both
   health bars and the first 40-second round clock begin.
2. A legal four-limb command, guard, throw or sidestep changes posture,
   spacing or attack state. High misses a crouching body; mid defeats crouch
   guard; low defeats standing guard. Contact is not guaranteed by pressing
   the button, especially after a sidestep.
3. An attack reaching zero health awards an ordinary round. At time-over,
   compare remaining health; equal health or double KO awards both fighters
   a point. A final-round draw in one-player Arcade gives Game Over, not a
   free ladder advance.
4. A match win starts the next CPU opponent, retaining Jin as the chosen
   fighter. A loss opens Continue; accepting restarts the lost stage with Jin,
   while declining ends this attempt. The manual states no Continue cap.
5. Only winning every required Arcade opponent reaches the positive terminal.
   The selected fighter and rules remain fixed; opponent order, exact stage
   count, damage and frames are recorded as unknown parameters, not invented.

## Strategic and experiential structure

The tactical choice is not a genre label: every approach predicts whether the
next attack reaches the opponent's current axis and whether its height beats
the expected guard. Sidestep makes positioning a decision before pressing an
attack button, while the 40-second round clock prevents indefinite distance
reset. Super Charger offers additional guarded damage at an exposed startup.
Winning a match changes the opponent, not Jin's input vocabulary; declining
Continue is the only ordinary loss branch that ends this bounded ladder.

## Replay and variation

Opponent identity, stage order, CPU commands, hits, throws, drawn rounds and
Continue use can change between attempts. The selected fighter, original disc
family, default rules, one-player Arcade route and terminal boundary remain
fixed. No claim about a deterministic random seed, exact opponent count or
progress saved after power-off is made.

## Adjacent systems and history

The original PlayStation package also offers VS, Team Battle, Survival, Time
Attack, Tekken Force and Practice; these change the player count, scoring or
progression boundary and are not silently included. TEKKEN 8's walled Arena,
Heat, Rage and recoverable gauge belong to another product and another scope.

## Normalised genome

| Type | Active gene IDs | Role in this packet |
|---|---|---|
| Action | `ACT-008`, `ACT-202`, `ACT-294`, `ACT-295`, `ACT-296`, `ACT-297` | select Jin, move and sidestep, change posture, attack, guard and throw |
| System Behaviour | `SYS-215`, `SYS-522`, `SYS-1000` | combat contact, round settlement and Arcade stage/Continue routing |
| Constraint | `CON-442`, `CON-446`, `CON-667` | legal commands, match bounds and lateral open-plane spacing |
| Information | `INF-142`, `INF-209`, `INF-210` | animation, fighter positions, health/clock/round HUD |
| Objective | `OBJ-099`, `OBJ-212` | win each match and the fixed-character ladder |
| Time | `TIM-003` | live simultaneous fighting |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `365` (`GAME-0001`–`GAME-0365`).
- Exact genome matches: none.
- Tied near matches: `GAME-0351` — Street Fighter II: The World Warrior (`14 / 19 = 0.736842`).
- Supported combination subsets: none.
- Scan date: 2026-09-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0351` — Street Fighter II: The World Warrior | `ACT-008`, `ACT-294`, `ACT-295`, `ACT-296`, `ACT-297`, `SYS-215`, `SYS-522`, `CON-442`, `CON-446`, `INF-142`, `INF-209`, `INF-210`, `OBJ-099`, `TIM-003` | Both use direct fighter movement, attacks, guard, throws, live contact and timed round wins. Street Fighter II's bounded side-view line has no lateral axis and its packet ends at the first duel; Tekken 3 sidesteps on an open plane, routes a retained Jin through successive CPU opponents and offers a same-stage Continue | Near, `14 / 19 = 0.736842` |

## Taxonomy impact

- Add `SYS-1000`, `CON-667` and `OBJ-212` under
  `TAXONOMY_CHANGE_105`; no older genome changes.
- Reuse the other fifteen existing active genes within their established
  boundaries. No verified combination is created from one new carrier.

## Negative results

- Reject `CON-443`: it describes a bounded side-view line with corners and
  no lateral axis. Reject `CON-625`: it requires walled geometry and wall-stop
  decisions from modern Tekken 8; these are not transferred to Tekken 3.
- Reject Heat, Rage, recoverable-gauge and wall-splat genes from Tekken 8.
  Their shared four-limb surface is not evidence of shared modern resources.
- Exact stage count/order, numeric default required-round wins, move frames,
  hit damage and disc hash remain unresolved rather than guessed.

## Delta summary

## New facts

- [Confirmed | Direct | High] Namco's original manual supplies the four-limb,
  high/mid/low, round-draw and unlimited same-stage Continue rules.
- [Observation | Limited | Medium] Launch follow-ups and wall-less classic
  Tekken stage classification have separate secondary support, not direct play.

## New genes

- [Observation | Corroborated | Medium] Three Active boundaries distinguish
  Arcade stage/Continue routing, open lateral fighting space and full-ladder
  completion from a single modern fixed-opponent Versus match.

## New combinations

- [Observation | Direct | High] No verified new combination.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_105` adds three
  definitions without changing previous signatures.

## New questions

- What is the exact opponent order, default required-round count and
  stage-count behaviour of the specific `SLUS-00402` disc under an instrumented
  licensed play session? Those values are not claimed here.

## Next recommended game

- [Confirmed | Direct | High] `GAME-0367` — Mass Effect 2, the next selected
  unit in `SEARCH_DEMAND_GAME_SELECTION_026` after the Goal stop window.
- Optimisation criterion: preserve the recorded order and one-game unit
  boundary; do not start the following unit in this turn.
- Expected information gain: squad-command, dialogue and loyalty causality
  contrasted with short real-time fighting rounds.
- Backlog impact: unit 6 of the selected nine-game horizon.

## Why this game

- [Confirmed | Direct | High] Tekken 3 is the sixth selected cult anchor,
  testing whether the corpus can reuse one-on-one fighting genes while
  representing an earlier lateral but wall-less Arcade ladder separately.

## Reproducibility notes

1. Use a licensed original NTSC-U/C `SLUS-00402` disc and default options;
   choose one-player Arcade Mode and Jin Kazama. Record disc hash if one is
   lawfully available, but do not substitute a later game or port.
2. Record first-opponent presentation, four-limb command responses,
   sidestep, high/mid/low guard, throw and knocked-down recovery with clock
   and health visible. The source-model control tests branch relations only.
3. Check KO, time-over and a drawn round; check a lost match's same-stage
   Continue with Jin, then complete every opponent or decline Continue.
4. Do not infer opponent order, count, exact frames or campaign rewards from
   the documentary reconstruction. No physical or executable test was done.

## Localisation review

- `verified`: Jin Kazama, Arcade Mode, Continue, Tekken 3, `SLUS-00402` and
  gene IDs remain evidence-relevant literal names and identifiers.
- `corrected`: Ukrainian profile, scope, direct-play caveat, web summary and
  three new-gene definitions retain the differences between a round, match,
  same-stage retry and full Arcade clear.
- `retained-with-reason`: limited English mode labels remain only where they
  identify literal UI choices in the original English manual.
