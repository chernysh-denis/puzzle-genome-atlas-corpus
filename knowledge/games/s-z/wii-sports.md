---
game_id: GAME-0364
slug: wii-sports
game_title: Wii Sports
analysis_status: reviewed
reviewed: 2026-09-22
combination_ids: []
gene_ids:
  action:
    - ACT-498
    - ACT-499
  system:
    - SYS-995
    - SYS-996
    - SYS-997
  constraint:
    - CON-664
  information:
    - INF-373
  objective:
    - OBJ-002
  time:
    - TIM-003
---

# Game: Wii Sports

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The Mii, Wii
Remote, B button, bowling ball, pins and Pro title are carrier or interface
parameters, not separate gene names.

## Analysis scope

- Version / ruleset: original English North American *Wii Sports* physical
  Wii-disc release (2006), one-player Bowling, one complete ten-frame game on
  a console-stored Mii. No Wii Sports Resort, Wii Sports Club, Nintendo Switch
  Sports or later control variant is imported.
- Structured analysis target: Wii disc on `PLAT-NINTENDO-WII` as recorded in
  [`knowledge/platforms/games.json`](../../platforms/games.json); ordinary Wii
  Remote with wrist strap, no modified input or emulator conveniences.
- Primary decision loop: observe the standing pins and frame; choose lateral
  standing position and aiming line; hold B and swing the Wii Remote; release
  B at the chosen motion sample with optional wrist twist; watch the one ball
  roll, curve and knock pins down; use a legal next delivery if pins remain;
  read the pending strike/spare bonuses and repeat until all ten frames and
  earned final fills settle; inspect the score and the stored Mii's revised
  sport skill level.
- Entry: select a console-stored Mii and one player, choose Bowling, and start
  a new ten-frame game before the first delivery.
- Positive terminal: all ten frames and any earned tenth-frame fill deliveries
  are complete; a final score is recorded, a performance-dependent Bowling
  skill-level change is displayed and the eligible Mii record can be saved.
  This packet maximises score rather than requiring a fixed target or Pro.
- Negative terminal: a low-scoring but completed game is still a valid game;
  a gutter shot or missed spare is not a separate failure state. The packet
  does not define an impossible-to-win terminal before frame ten.
- Reproducible route: start with a stored Mii; in frame one, adjust the
  standing position and aim independently, hold B, swing and explicitly
  release; observe a first-ball non-strike, throw at the remaining pins for a
  spare, then let the next delivery resolve the spare bonus. Continue the
  permitted sequence through frame ten and inspect the final score and skill
  screen. A second branch deliberately bowls a first-ball strike and checks
  that the next two deliveries, not the strike alone, complete its bonus.
- Included: standing position, aiming line, explicit B hold/release, sampled
  swing and wrist spin, one rolling ball, gutter and pin collisions, standing
  pin carry-over within a frame, strike/spare marks and delayed bonuses,
  tenth-frame fill entitlement, final score, selected-Mii Bowling skill
  update, Pro threshold and save eligibility.
- Excluded: Tennis, Baseball, Golf, Boxing, multiplayer, Training and Fitness
  Test, audience reactions, exact hidden skill formula, exact sensor
  calibration, numerical spin/friction coefficients, replay camera, other
  Mii records, guest or Remote-Mii persistence, sequel mechanics, exploits
  and perfect-game strategy.
- Potential scoped modules: multiplayer turn-taking and shared Wii Remote;
  Bowling Training modes; guest-Mii ephemeral records; actual direct-play
  measurement of ball spin, pin physics and skill-rating delta.
- Direct-play status: no Wii console, original disc, save, controller trace,
  screenshot, video or audio was obtained or inspected. The Nintendo manual
  directly specifies the controls and retained rating; the ten-pin score
  model is source-bounded corroboration, not a measurement of game code.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `WII-001` | The original disc's Bowling mode is a ten-frame game and supports one player | Confirmed | Direct | High | P1 |
| `WII-002` | Standing position and aiming line are separately adjustable before the throw | Confirmed | Direct | High | P1 |
| `WII-003` | Holding B, swinging and explicitly releasing B determines the delivery; wrist turn changes spin | Confirmed | Direct | High | P1 |
| `WII-004` | A rolling ball's path and pin contacts settle pinfall; exact numerical physics are not disclosed | Observation | Corroborated | Medium | P1, P2 |
| `WII-005` | The ten-pin frame score defers strike/spare bonuses to later deliveries and grants only earned tenth-frame fills | Observation | Corroborated | Medium | P1, P3 |
| `WII-006` | Sport skill rises or falls with performance, Pro requires a value above 1,000, and a fall can remove Pro | Confirmed | Direct | High | P1 |
| `WII-007` | A console-stored Mii has saved records, while guest and Remote-stored Mii records are not saved | Confirmed | Direct | High | P1 |

## Basic data

- Release / origin: original Nintendo Wii release in 2006; this record uses
  the North American English disc manual, not a remaster.
- Platform or physical form: Wii Game Disc and motion-sensing Wii Remote.
- Puzzle family: `FAM-007` physics and object manipulation, bounded here to
  rolling alignment and pinfall; competitive sport scoring is a parameter of
  this game, not a new singleton family.
- Primary sources: **[P1]** [Nintendo original Wii Sports manual](https://csassets.nintendo.com/noaext/image/private/t_KA_PDF/Wii_Wii_Sports?_a=DATAg1AAZAA0),
  especially printed pages 4–9; **[P2]** [Nintendo Wii Sports product
  page](https://www.nintendo.com/en-gb/Games/Wii/Wii-Sports-283971.html);
  **[P3]** [United States Bowling Congress: How to score](https://images.bowl.com/bowl/media/legacy/internap/bowl/rules/pdfs/ScoreHowto.pdf)
  for the conventional ten-pin frame arithmetic. P3 is a sport rule, not
  direct observation of the Wii executable.
- Claim IDs: `WII-001`–`WII-007`.

## Mechanical decomposition

### Action Genes

- `ACT-498` independently changes stance and aim before a delivery. The
  manual specifies the D-pad and A switch between modes; neither control
  launches the ball.
- `ACT-499` commits one physically sampled ball delivery by holding B,
  swinging, releasing B and optionally twisting the wrist. Automatic release
  is specifically excluded for this original version.
- Claim IDs: `WII-002`, `WII-003`.

### System Behaviour Genes

- `SYS-995` resolves the rolling ball's path, spin, gutters, pin impacts and
  resulting settled pinfall. No numerical coefficient is asserted.
- `SYS-996` retains fallen pins across a second in-frame delivery, resets an
  eligible new rack, scores ordinary open/strike/spare frames and resolves
  bonus dependencies and earned tenth-frame fills. It does not create an
  eleventh frame.
- `SYS-997` revises the selected stored Mii's Bowling skill level after
  completed play, separately from the one-game score; the hidden formula is
  deliberately not reconstructed.
- Resolution order: adjustment → B-held swing → B release → ball/pin
  settlement → legal next delivery or frame transition → score/bonus
  settlement → final skill and record update.
- Claim IDs: `WII-004`–`WII-007`.

### Constraint Genes

- `CON-664` permits at most two ordinary-frame deliveries, ends a frame on
  an opening strike, and admits only earned tenth-frame fill deliveries.
- Scarce strategic resource: the finite delivery opportunities within ten
  frames, not a carried stock of bowling balls.
- Claim IDs: `WII-001`, `WII-005`.

### Information Genes

- `INF-373` presents the lane's standing pins, current frame and score marks.
  A pending strike or spare makes part of the eventual total contingent on
  later deliveries; the interface does not reveal the hidden skill formula.
- Claim IDs: `WII-001`, `WII-005`, `WII-006`.

### Objective Genes

- `OBJ-002` maximises the ten-frame score. A Pro skill threshold is a
  persistent evaluation state, not the required terminal of this match.
- Claim IDs: `WII-001`, `WII-006`.

### Time Genes

- `TIM-003` covers continuous input sampling during the B-held swing and
  uninterrupted live ball/pin resolution after release. There is no
  frame-level countdown forcing a throw at a fixed deadline.
- Claim IDs: `WII-003`, `WII-004`.

## Reproducible transitions

| Before | Action | Deterministic rule-level resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First frame, fresh ten-pin rack, stance mode active | Set lateral offset, switch mode and change aim | A distinct standing position and aiming line remain adjustable before release | Separate alignment action | `WII-002` |
| B held during backward and forward swing | Release B at the chosen point with a wrist turn | One ball receives a direction, speed and spin; no automatic release or post-release steering is required | Motion-sampled delivery | `WII-003` |
| First ball fells fewer than ten pins | Let impacts settle | Remaining pins stay eligible for the second delivery of that frame | Pinfall and two-delivery boundary | `WII-004`, `WII-005` |
| First and second deliveries together fell ten | Begin the next frame and bowl once | Prior spare's ten-plus-next-ball value becomes resolvable only after that delivery | Deferred spare bonus | `WII-005` |
| First delivery fells ten | Begin the next eligible frame and bowl twice | The prior strike is worth ten plus those next two deliveries, not an immediate isolated ten | Deferred strike bonus | `WII-005` |
| Tenth-frame first delivery is a strike or its first two make a spare | Take only the earned fill deliveries | Final score settles inside frame ten; no frame eleven is created | Tenth-frame exception | `WII-005` |
| Ten frames and fills completed with a stored Mii | Continue to result and save | Score is final; sport-specific skill may rise or fall and its eligible record persists | Distinct retained rating | `WII-006`, `WII-007` |

## Strategic and experiential structure

- Local decision: align a narrow path and choose the release timing and wrist
  motion that give the ball a useful entry into the pin triangle.
- Medium-term planning: a first-ball miss changes the second delivery's legal
  target field; a strike or spare makes later shots affect earlier score.
- Long-term structure: complete ten frames, improve score and possibly change
  the persistent skill level without assuming a guaranteed Pro result.
- Common heuristic: use the visible standing pins and prior miss to revise the
  next legal delivery rather than repeat the identical line blindly.
- Failure attribution: a gutter ball, off-centre entry or missed spare is
  visible, but the numerical physics and skill delta are not source-observed.
- Player-trust factors: explicit pinfall and frame marks make the match score
  legible, while Nintendo's hidden rating algorithm limits exact prediction.
- Claim IDs: `WII-002`–`WII-007`.

## Replay and variation

- What changes between sessions: the player's swing samples, aim, spin,
  collision outcomes, score and stored skill state.
- Randomness or procedural generation: no random pin arrangement or hidden
  randomness is claimed for this bounded Bowling mode.
- Multiple viable strategies: changing stance, aim, release and spin can
  approach the pin triangle differently; no optimal formula is asserted.
- Typical replay motive: score improvement and the Mii's displayed skill
  progression.
- Claim IDs: `WII-002`–`WII-007`.

## Adjacent systems and history

- Real-world ten-pin Bowling provides the frame vocabulary and bonus
  arithmetic, but this record does not infer exact game-engine coefficients.
- Wii Sports' other sports, multiplayer and Training are excluded modules.
- Peggle Deluxe and Angry Birds Classic also resolve launched bodies, but
  their fixed or pointer launchers, airborne paths and target budgets do not
  match an embodied rolling delivery over a ten-frame scorecard.
- Claim IDs: `WII-001`, `WII-003`–`WII-005`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-498`, `ACT-499` | independent alignment and B-release gesture |
| System Behaviour | `SYS-995`, `SYS-996`, `SYS-997` | roll/pin collision, frame score, retained skill |
| Constraint | `CON-664` | two deliveries, strike and tenth-frame exceptions |
| Information | `INF-373` | lane, pins, frame and pending score |
| Objective | `OBJ-002` | maximise final ten-frame score |
| Time | `TIM-003` | sampled gesture and live ball resolution |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `363` (`GAME-0001`–`GAME-0363`).
- Exact genome matches: none.
- Tied near matches: `GAME-0114` — Peggle Deluxe (`2 / 14 = 0.142857`).
- Supported combination subsets: none.
- Scan date: 2026-09-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0114` — Peggle Deluxe | `OBJ-002`, `TIM-003` | Both raise a session score while a released ball resolves in real time. Peggle aims a fixed launcher into gravity-driven pegs with a recoverable finite ball stock and an orange-clear terminal. Wii Sports instead samples an explicit physical B release, rolls and spins one ball into ten pins, limits deliveries by frame, defers strike/spare bonuses and separately updates stored Mii skill | Near, `2 / 14 = 0.142857` |

## Taxonomy impact

- Add `ACT-498`, `ACT-499`, `SYS-995`–`SYS-997`, `CON-664` and `INF-373`
  under `TAXONOMY_CHANGE_103`; reuse `OBJ-002` and `TIM-003`.
- Do not broaden `ACT-113`, `SYS-146` or `SYS-342` to erase the distinctions
  between a fixed launcher, rolling pin physics and an evaluative Mii rating.
- Add no combination without a verified recurring proper subset.

## Negative results

- `ACT-113` and `SYS-146` are rejected: a standing bowler explicitly releases
  a physically sampled rolling ball rather than firing a ball from a fixed
  launcher into ballistic bounces.
- `CON-164` is rejected: there is no depleting carried stock of balls; legal
  shots are governed by frame and pinfall.
- `SYS-342` is rejected: skill level evaluates performance and is not evidence
  of new playable modifiers or throw capabilities.
- Nintendo's manual does not publish the exact rating formula or physical
  simulation constants; neither is invented here. No direct game execution
  or audiovisual evidence was obtained.

## Delta summary

## New facts

- [Confirmed | Direct | High] Original Bowling is ten frames and uses two
  independent pre-release alignment controls and explicit B-held release
  (`WII-001`–`WII-003`).
- [Observation | Corroborated | Medium] Pinfall and conventional strike/spare
  bonuses structure the score (`WII-004`, `WII-005`).
- [Confirmed | Direct | High] The Mii's performance skill is separate from
  score, can change in both directions, and has a revocable Pro title;
  eligible console-Mii records save (`WII-006`, `WII-007`).

## New genes

- [Confirmed | Direct | High] `ACT-498`, `ACT-499` and `SYS-997` isolate
  independent aim, physical release and retained performance rating.
- [Observation | Corroborated | Medium] `SYS-995`, `SYS-996`, `CON-664` and
  `INF-373` isolate pin physics and ten-frame score/eligibility disclosure.

## New combinations

- [Observation | Direct | High] No verified new combination.

## Taxonomy changes

- [Observation | Corroborated | High] Seven new Active boundaries; no
  lower-ID signature or lifecycle changes.

## New questions

- What is the original Wii executable's precise mapping of gesture samples
  to lane speed and spin, and how does the hidden skill formula respond to
  different completed Bowling scores? Direct licensed observation would be
  needed; neither is inferred from the manual.

## Next recommended game

- [Confirmed | Direct | High] `GAME-0365` — Tony Hawk's Pro Skater 1 + 2,
  the next authorised unit in `SEARCH_DEMAND_GAME_SELECTION_026`.
- Optimisation criterion: continue the fixed Goal order only after this
  full unit's validation and stop window.
- Expected information gain: continuous trick chains, balance, route and
  timed objective settlement versus ten-frame discrete sport scoring.
- Backlog impact: unit 5 of the active nine-game Goal.

## Why this game

- [Confirmed | Direct | High] Wii Sports is the fourth selected cultural
  anchor and tests whether motion input, rolling collision, frame bonuses
  and a retained sport rating can be represented without conflating them.

## Reproducibility notes

1. Use the original English 2006 Wii Sports disc, one console-stored Mii and
   one-player Bowling, with the wrist strap fastened.
2. Before the first shot, adjust stance and aim separately. Hold B, swing
   and release B; turn the wrist for one spin comparison. Do not substitute
   an automatic-release sequel control.
3. Record pinfall after each ball, retain unfallen pins for a legal second
   shot and compare first-ball strike with two-ball spare scoring.
4. In the tenth frame, record only the fill balls earned by a strike or
   spare. Confirm the final score after the last permitted ball.
5. Observe the separate Mii skill display and saved record if entitled to
   direct play. The repository-side control checks rule transitions only and
   is not itself execution of Wii Sports.

## Localisation review

- `verified`: all nine admitted gene IDs, the original title, Wii Remote,
  Mii, B and Pro are preserved as official terms or literal controls.
- `corrected`: reviewed Ukrainian profile, scope, direct-play caveat,
  presentation, seven new-gene definitions and all admitted plain-language
  cards preserve the ten-frame entry and settlement semantics.
- `retained-with-reason`: `Wii Sports`, `Mii`, `Wii Remote` and `Pro` are
  source-specific names; the Ukrainian prose does not use generic English
  substitute explanations.
