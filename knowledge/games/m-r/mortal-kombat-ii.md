---
game_id: GAME-0393
slug: mortal-kombat-ii
game_title: Mortal Kombat II
analysis_status: reviewed
reviewed: 2026-09-24
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
  constraint:
    - CON-442
    - CON-443
    - CON-446
  information:
    - INF-142
    - INF-209
    - INF-210
  objective:
    - OBJ-099
  time:
    - TIM-003
---

# Game: Mortal Kombat II

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Liu Kang, other
fighters, arena, individual special moves and controller buttons are carrier
parameters, not separate genes.

## Analysis scope

- Version / ruleset: original North American 1994 Super NES *Mortal Kombat II*,
  instruction booklet `SNS-28-USA`, one-player tournament at default options
  and controls. Select Liu Kang and examine only the first CPU match. The
  original booklet is the rules authority; no cartridge or later collection
  binary was played.
- Primary decision loop: read opponent distance, stance, vitality, round time
  and attack posture; move, crouch, jump, block, strike or attempt a close
  throw; let the two fighters' live contact and recovery resolve; repeat until
  one side wins the match's required rounds.
- Entry: one-player mode has begun, Liu Kang has been selected and the first
  computer opponent is present at the start of round one. Opponent identity
  and arena are recorded run parameters, not assumed fixed by this packet.
- Positive terminal: Liu Kang wins two rounds and the first tournament match
  is awarded to him. Stop before the next opponent or any post-match finisher.
- Negative terminal: the CPU wins two rounds; the booklet also states that
  five rounds without a match winner disqualify both fighters from the
  tournament. Stop at that result, without inventing a continue flow.
- Included: directional movement, jump and crouch; high/low punches and kicks,
  fighter-specific special commands, close throw, dedicated L/R blocking,
  opponent-relative attack/guard contact, injury and recovery, visible paired
  health meters, round timer, KO, time-over comparison, refreshed round
  vitality and two-round match settlement.
- Excluded: the rest of the tournament ladder, finishing moves, two-player
  interruption and handicap, non-default options, later SNES revisions,
  arcade/Genesis/32X/modern-collection rule substitution, exact damage,
  frame data, artificial-intelligence policy, hidden encounters and direct
  claims about a played build. The arcade manual is contrast only.
- Reproducible parameterisation: use `SNS-28-USA` ordinary one-player setup,
  default buttons/difficulty and Liu Kang; log the assigned opponent, arena,
  stance, input, contact, injury, timer and round result. No exact sequence of
  CPU moves or special-move success is presupposed.
- Potential scoped modules: a direct SNES input trace, precise character
  commands and damage, later CPU ladder, multiplayer challenge, finisher
  condition and rules of a particular later port or compilation.
- Direct-play status: none. No cartridge, ROM, emulator, controller trace,
  game screenshot, video or audio was inspected. This is a source-bounded
  reconstruction of the instruction booklet's first-match rules.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MK2-001` | The booklet identifies the original North American SNES edition `SNS-28-USA` and its one-player character selection. | Confirmed | Direct | High | P1 pp. 1, 5–6 |
| `MK2-002` | Directions move, crouch and jump; B/Y are low/high punch and A/X are low/high kick; L or R requests block. | Confirmed | Direct | High | P1 pp. 12–13, 16–17 |
| `MK2-003` | Direction-plus-button inputs create an uppercut, sweep, roundhouse, jumping attack or fighter-specific special move. | Confirmed | Direct | High | P1 pp. 14, 18 |
| `MK2-004` | Each round starts with full green vitality; injury turns a meter red, and a fully red meter causes KO and awards the round. | Confirmed | Direct | High | P1 p. 10 |
| `MK2-005` | If time runs out before KO, the less-injured fighter wins that round. | Confirmed | Direct | High | P1 p. 10 |
| `MK2-006` | The first fighter to win two rounds takes the match; after five rounds without a winner, both are disqualified from the tournament. | Confirmed | Direct | High | P1 p. 11 |
| `MK2-007` | Default one-player settings are held fixed; the Options screen can change difficulty and buttons, and handicap applies only to two-player play. | Confirmed | Direct | High | P1 p. 7 |
| `MK2-008` | The original arcade board uses a distinct five-button mapping, not proof that arcade controls apply to the scoped SNES packet. | Confirmed | Direct | High | P2 pp. 2, 12 |
| `MK2-009` | A contemporary licensed compilation lists Mortal Kombat II across arcade, SNES, Genesis and 32X, but its executable behaviour was not inspected. | Confirmed | Direct | High | P3 |
| `MK2-010` | No original cartridge, later wrapper or direct input trace was examined. | Observation | Direct | High | R1 |

## Basic data

- Release / origin: Midway's *Mortal Kombat II*; the selected North American
  Super NES home edition dates to 1994. Its manual code pins this packet more
  narrowly than the broader 1993 arcade title.
- Platform or physical form: `PLAT-SUPER-NINTENDO`, original SNES cartridge
  rules, not an assertion of a tested cartridge revision.
- Puzzle families: tactical forecast and counterplay; real-time system pressure.
- **[P1]** [Original *Mortal Kombat II* Super NES instruction booklet,
  `SNS-28-USA`](https://www.videogamemanual.com/snes/Mortal%20Kombat%20II%20%28USA%29.pdf),
  pp. 1, 5–7, 10–14, 16–18, inspected 2026-09-24; local source SHA-256
  `2f9234dc7a2f9115eda1ee03a66c75a6240209f711ff5eb75564259b3c28a851`.
  This is a scan of the original publisher's booklet, not a played game.
- **[P2]** [Midway original arcade operations
  manual](https://r.mprd.se/MAME/manuals/arcade/mk2.pdf), pp. 2 and 12,
  inspected 2026-09-24; local source SHA-256
  `ef2ddbcb60557314b6044349429a3a1d0e6d8bd69e6c18336a0545b8c0d2c775`.
  Used only to reject accidental arcade-button import.
- **[P3]** [Digital Eclipse's official *Mortal Kombat: Legacy Kollection*
  FAQ](https://www.digitaleclipse.com/media/mortal-kombat-legacy-kollection-launch-faq),
  checked 2026-09-24. It identifies a licensed modern availability route,
  not verified equivalence of its executable with the 1994 cartridge.
- **[R1]** Local no-direct-play and version-boundary audit in this record.
- Claim IDs: `MK2-001`–`MK2-010`.

## Mechanical decomposition

### Action Genes

- `ACT-294`: select Liu Kang before the duel. Character identity and moveset
  vary, but selection is a distinct pre-match commitment.
- `ACT-008`: move laterally or jump within the fight plane.
- `ACT-202`: crouch or rise, changing posture and available attack/guard
  relation. It is not a new stage or a turn.
- `ACT-295`: submit a high/low punch or kick, a legal direction-modified
  normal or a fighter-specific special command. Contact belongs to `SYS-215`.
- `ACT-296`: hold or release the dedicated L/R block request against the
  facing opponent. The input mapping differs from Street Fighter's hold-back
  guard; the common action is sustained live defensive posture.
- `ACT-297`: attempt a close throw. No throw-escape branch is inferred.
- Candidate terms: separate guard-button gene rejected as an input mapping
  variant; individual attack buttons and special names are parameters.
  Claim IDs: `MK2-001`–`MK2-003`.

### System Behaviour Genes

- `SYS-215`: resolve contact between live movement/attacks and guard, then
  apply injury and return to actionable states. Exact frames and damage are
  unverified parameters.
- `SYS-522`: award a round by KO or less injury at time-over, restore full
  vitality for the next round and settle the match at two wins; the booklet's
  five-round disqualification bounds unresolved matches.
- Resolution order: legal input → relative movement/posture → contact or
  block → injury/recovery → KO or time-over judgment → fresh round or match
  result. Claim IDs: `MK2-002`–`MK2-006`.

### Constraint Genes

- `CON-442`: attacking, guarding and recovery constrain which immediate
  command can succeed; the timing is not a turn queue.
- `CON-443`: the duel occurs on one bounded side-view arena floor, not across
  an open navigable world. Stage art is a parameter.
- `CON-446`: two finite vitality meters, a round timer and accumulated round
  wins bound the duel; a single hit is normally not a match result.
  Claim IDs: `MK2-002`–`MK2-006`.

### Information Genes

- `INF-142`: visible attack and guard posture can be read before choosing a
  counter, without claiming exact animation-frame timing from the manual.
- `INF-209`: the shared side-view arena exposes relative spacing and facing.
- `INF-210`: separate injury/vitality meters and the round timer disclose
  time-over pressure and which fighter is nearer KO. Claim IDs: `MK2-002`–
  `MK2-005`.

### Objective Genes

- `OBJ-099`: take the first two awarded rounds against the current CPU
  opponent, not the full tournament. Five inconclusive rounds instead end in
  disqualification under the booklet. Claim ID: `MK2-006`.

### Time Genes

- `TIM-003`: inputs and their opponent responses happen in live time while
  the round timer runs. Selecting a fighter is the setup, not a combat turn.
  Claim IDs: `MK2-002`–`MK2-006`.

## Reproducible transitions

| Before | Action | Rule-bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Both meters are green at round start | Move toward the opponent | Relative separation changes in the same arena while time runs | live spacing is a decision input | `MK2-002`, `MK2-004` |
| An attack is incoming at reachable range | Hold L or R to block | The fighter requests a defensive state; whether a particular hit is blockable depends on its class and timing | dedicated block input is not Street Fighter's away-direction mapping | `MK2-002` |
| The fighter is grounded near the opponent | Hold down and press high punch | An uppercut attempt is selected; contact and damage are not guaranteed | posture plus command selects an attack | `MK2-003` |
| One meter becomes fully red before time expires | Resolve the hit | The damaged fighter is knocked out and the other receives that round | KO is a round terminal, not automatically a match terminal | `MK2-004` |
| Neither fighter is knocked out when time expires | Compare injury | The less-injured fighter is awarded the round | time can settle the round without KO | `MK2-005` |
| One fighter records a second round win | Complete the result | That fighter wins the match and the packet stops | first-to-two match boundary | `MK2-006` |
| Five rounds finish without a match winner | Complete the result | Both fighters are disqualified from the tournament | finite unresolved-match boundary | `MK2-006` |

## Strategic and experiential structure

- Local decision: judge range and opponent stance before using a high/low
  strike, jump, crouch, block or throw. An attack command alone does not
  promise contact.
- Medium-term planning: preserve vitality across one timed round while
  forcing injury on the CPU; the next round refreshes both meters but retains
  awarded round wins.
- Long-term structure: acquire two round wins before the opponent, rather
  than clear the whole tournament or execute a finisher.
- Failure attribution: the manual explains controls and result rules, but
  exact collision timing, CPU policy and damage numbers are not evidenced by
  this packet. No fabricated success rate or direct play is claimed.
- Player-trust factors: the health meters and clock visibly expose why KO or
  time-over awards a round. Claim IDs: `MK2-002`–`MK2-006`.

## Replay and variation

- Opponent identity, spacing, player command timing, guarded contacts and
  remaining vitality can change a match; no exact CPU sequence is fixed.
- The fighter, SNES edition, default options, first match and stop boundary
  stay fixed. A changed port or handicap is a different packet.

## Adjacent systems and history

- *Street Fighter II: The World Warrior* shares a side-view real-time duel,
  ordinary attacks, guard, health, timer and two-round settlement. Its arcade
  six-strength attack panel and opponent-relative hold-back guard are not
  imported into this four-attack-button SNES MKII mapping; the shared genes
  identify operation-level rules, not identical button labels.
- *Tekken 3* also has live guard/throw and timed rounds but its examined
  route includes depth-axis sidestepping and a longer CPU progression. The
  present packet stops after a single side-view opponent.
- The original arcade MKII manual describes a different input panel, and the
  modern Legacy Kollection spans several editions; neither overrides P1.
  Claim IDs: `MK2-001`, `MK2-008`–`MK2-009`.

## Normalised genome

| Type | Active genes | Parameters outside signature |
|---|---|---|
| Action | `ACT-008`, `ACT-202`, `ACT-294`–`ACT-297` | Liu Kang, D-pad, L/R block, B/Y/A/X attacks |
| System | `SYS-215`, `SYS-522` | exact damage, contact and round sequence |
| Constraint | `CON-442`, `CON-443`, `CON-446` | arena geometry, health and clock settings |
| Information | `INF-142`, `INF-209`, `INF-210` | animation and HUD styling |
| Objective | `OBJ-099` | first CPU opponent, five-round disqualification |
| Time | `TIM-003` | round duration and input timing |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `392` (`GAME-0001`–`GAME-0392`).
- Exact genome matches: none.
- Tied near matches: `GAME-0351` — Street Fighter II: The World Warrior (`15 / 16 = 0.937500`).
- Supported combination subsets: none.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0351` — Street Fighter II: The World Warrior | Fifteen shared genes cover fighter selection, movement, attack, live guard and throw, contact, health, timer, arena and first-to-two result. | The SFII arcade packet uses six attack strengths and hold-back guard. The SNES MKII booklet uses four attack buttons plus L/R block; its crouch is explicitly separated as `ACT-202`, the only added gene versus this neighbour. The controller mapping and character commands are parameters, not proof of an identical execution trace. | `15 / 16 = 0.937500`; very near, not an exact match |

### Preserved research notes

- New genes: none.
- Classification result: Existing genes with a reviewed wording generalisation
  for `ACT-296`, documented in `TAXONOMY_CHANGE_131`.
- Evidence and reasoning: the SNES booklet directly supports a four-button
  attack arrangement, dedicated guard buttons and a first-to-two timed duel.

## Taxonomy impact

- Registry changes: generalise `ACT-296` from a hold-back-only input to a
  sustained opponent-relative live guard request, with direction and L/R
  button as carrier mappings. No older game genome is changed.
- Taxonomy-change record: `TAXONOMY_CHANGE_131`.
- Candidate terms affected: guard input, fighter stance and timed-round result.

## Negative results

- No separate negative-result record. Arcade controls, finishing moves and
  the later tournament are excluded from this SNES first-match scope, not
  disproven.

## Delta summary

The compact delta below names only this game's new corpus evidence.

## New facts

- [Confirmed | Direct | High] Original SNES MKII has L/R block, four punch/kick
  attack buttons, round vitality and timer, first-to-two match settlement and
  a five-round disqualification boundary (`MK2-002`–`MK2-006`).

## New genes

- [Observation | Direct | High] No new gene is required for this bounded duel;
  the dedicated guard button is an input-mapping parameter of an existing
  defensive action after the reviewed `ACT-296` wording change.

## New combinations

- [Observation | Direct | High] No verified combination is promoted from a
  single first-match packet.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_131` records the `ACT-296`
  wording transfer test with no retroactive genome migration.

## New questions

- How does a directly observed SNES input trace resolve borderline blocks,
  throws and character-specific special attacks against measured frames?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0394` LittleBigPlanet 2.
- Optimisation criterion: contrast a fixed adversarial duel with a cooperative
  authored platform-and-creation ruleset.
- Expected information gain: test whether level-object interactions and
  creative tool affordances need distinctions beyond this game's live guard.
- Backlog impact: preserves the accepted genre-alternating order.

## Why this game

- [Hypothesis | Limited | Medium] Its 1994 console fighting loop tests a
  dedicated block-button input against established fighting-game genes after
  the preceding multiplayer board economy.
