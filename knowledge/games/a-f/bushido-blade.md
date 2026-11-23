---
game_id: GAME-0641
slug: bushido-blade
game_title: "Bushido Blade"
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-223
    - ACT-295
    - ACT-459
    - ACT-853
  system:
    - SYS-868
    - SYS-1850
    - SYS-1851
    - SYS-1852
    - SYS-1853
  constraint: []
  information:
    - INF-595
  objective:
    - OBJ-329
  time:
    - TIM-003
---

# Game: Bushido Blade

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: original English North American PlayStation
  retail program, NTSC-U/C disc SCUS-94180, 1997. Solo Story Mode
  as Utsusemi with the opening weapon selected at the story menu.
  The traces use a backwards-compatible PS2 Slim and a labelled
  NTSC-U PlayStation emulator. Their disc hashes are unverified.
- Primary decision loop: select the equipment for the opening
  encounter, manage spacing and stance, read the response to
  contact, and keep or end the exchange through the next choice
  of movement, defence or attack.
- Entry: choose Utsusemi and a primary weapon in solo Story Mode,
  then reach the snowy yard facing Tatsumi. W1 selects Katana and W2 selects Nodachi.
- Exit: Tatsumi falls, the game replays the winning contact,
  and the same protagonist resumes live play against Mikado.
  The outcome of that second duel is outside scope.
- Included: direct three-dimensional spacing, selectable
  weapon stance, basic strikes, deliberate defence and weapon
  contact, the documented local body-damage alternatives,
  single-blow resolution, replay and successor.
- Excluded: Versus, Slash, training, POV and link modes, second
  game and other regional rules, alternative escape route,
  complete honor and ending qualification, advanced move lists,
  internal hit checks and the exact timing of button presses.
- Suggested later scope: compare the gate and alternate castle
  routes, then isolate individual honor conditions with matched
  runs.

## Direct-play status

No direct play was performed. The North American packaging and
booklet identify the edition and document its stance, defence and
local damage rules. A region-labelled PS2 Slim disc-compatible run
and a separately labelled ePSXe run show the same first opponent
falling, the replay and the next live opponent. Samples were
inspected as silent frames. Neither run was used to infer exact
inputs from poses. Severe wound effects are booklet findings.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| BB-001 | Bushido Blade is a 1997 commercial English PlayStation release in North America. Its retail disc identity is SCUS-94180. | Confirmed | Direct | High | P1 English North American booklet, P2 original disc and packaging scans. |
| BB-002 | In solo Story Mode the player selects an opening protagonist and then a primary weapon. Both recordings select Utsusemi. W1 selects Katana and W2 selects Nodachi. The first named opponent is Tatsumi with the sledgehammer. | Observation | Corroborated | High | P1 booklet pp. 6–7, 16–19 and 21, 24; W1 0:23–0:29 and W2 0:00–0:20 and 0:37; R1 Utsusemi opening. |
| BB-003 | Movement can change spacing on the yard floor. High, normal and low weapon stances can be selected in play. Character, weapon and stance can affect which attacks are available. Defend can actively intercept an opposing weapon. | Observation | Corroborated | High | P1 pp. 4–5 and 8–11. W1 0:49–0:56. Separate inputs are documented by the booklet and not read from the frames. |
| BB-004 | Weapon contact and a body hit have distinct results. A clash can leave both fighters able to act. A sufficiently strong defended attack can interrupt control through a balance loss without causing bodily damage. | Observation | Corroborated | High | P1 pp. 8, 11 and 13; W1 white-blue contact flash near 0:54, both still live, and another contact near 0:55.75. The balance-loss branch is specified by the booklet; exact defence input was not isolated in the run. |
| BB-005 | Local damage can remove particular actions without ending the duel. The manual distinguishes severe left-arm impairment of a two-handed hold and progressive leg impairment that can prevent stance change and standing while some actions remain. | Observation | Direct | High | P1 pp. 9 and 13. The low stance in W1 0:53 is not used as proof of a wound. No injury severity thresholds or carryover between fights were tested. |
| BB-006 | A decisive contact can end the live duel without draining a displayed gauge. The encounter has no in-game round timer. In both recorded traces the opponent falls after the decisive contact. | Observation | Corroborated | High | P1 pp. 6, 13; W1 0:57–1:00; W2 0:37–0:41. The external run timer is compositor overlay. |
| BB-007 | After the win, the encounter enters a replay, followed by a new live opponent with the same protagonist in the observed lane. The next opponent is Mikado. | Observation | Corroborated | High | W1 1:01–1:04 replay and victory camera, 1:15–1:20 Mikado begins acting with different position and weapon. W2 0:41–0:45 replay and 0:54–0:57 successor. Her intro line in W1 identifies the same character as her Story dialogue. |
| BB-008 | Story mode records conduct consequences beyond any one won duel. The manual states the condition; a successful opening and successor do not establish final eligibility. | Observation | Limited | Medium | P1 pp. 3 and 6. W2 reaches its first live successor before the later explicit reprimand at 2:04. The behavior that triggers the reprimand was not isolated. |

## Basic data

- Analysis target: `PLAT-PLAYSTATION`.
- Developer: Light Weight. North American publisher: Sony Computer
  Entertainment America, with Square's title and copyright.
- Mechanical family: `FAM-009`, tactical forecast and counterplay.
- Checked: 2026-11-22.
- P1: [Bushido Blade North American instruction booklet](https://oldgamesdownload.com/wp-content/uploads/manuals/bushido-blade_ps1_manual_en_a3s.pdf),
  printed pages 3–13 for Story rules, controls, body damage and
  contact feedback, and 16–25 for weapons and characters.
- P2: [SCUS-94180 packaging and disc archive](https://psxdatacenter.com/games/U/B/SCUS-94180.html).
- W1: [LynnCarius, Utsusemi normal-ending run](https://www.youtube.com/watch?v=lMsuzxHpnd0&t=49s),
  [USA NTSC entry with PS2 Slim disclosure](https://www.speedrun.com/bushido_blade/runs/yj9vv67z).
- W2: [FunkySteve, Utsusemi route](https://www.youtube.com/watch?v=Nj_RWtZ5x1E&t=36s),
  [USA NTSC entry with ePSXe 1.9.0 disclosure](https://www.speedrun.com/bushido_blade/runs/z0j6kk8y).
  Emulation and backwards
  compatibility are not original hardware measurements.
- R1: [ANickerson, player-authored Utsusemi route](https://gamefaqs.gamespot.com/ps/196844-bushido-blade/faqs/3755),
  corroborating the identity and weapon of the first opponent.
- R2: [Mikado's recorded opening dialogue](https://bushidoblade.fandom.com/wiki/Mikado),
  used only to identify the second character by subtitle.

## Mechanical decomposition

### Action Genes

- ACT-008: steer the controlled fighter through the yard and
  change range before contact.
- ACT-223: select deliberate defence as an attack approaches.
- ACT-295: choose and commit a basic directly controlled attack.
- ACT-459: change the selected weapon stance during the exchange.
- ACT-853: select protagonist and primary weapon separately.

### System Behaviour Genes

- SYS-868: resolve the current stance as a different set of
  attack affordances for the equipped weapon.
- SYS-1850: resolve weapon collision or deflection apart from a
  body hit, with a documented uninjured balance-loss branch.
- SYS-1851: make localized impairment change available actions.
- SYS-1852: allow one decisive contact to end the live duel.
- SYS-1853: replay the win and then bring in the next opponent.

### Constraint Genes

No separate constraint gene is introduced. Contact legality and
injury-based action availability are part of the evidenced
stance and wound transitions.

### Information Genes

- INF-595: let contact cues and animation reveal relevant
  outcome and pose without displayed vitality or a match timer.

### Objective Genes

- OBJ-329: settle the required adversary's defeat directly.

### Time Genes

- TIM-003: movement, attack and defensive inputs can occur while
  the opponent and animation continue in real time.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| Solo Story Mode selected | Choose Utsusemi, then select the shown Nodachi option | The start loads Utsusemi opposite Tatsumi with the sledgehammer | BB-002 |
| Both fighters are standing apart | Shift stance, then commit an appropriate attack | Posture and weapon height change. Available attacks remain tied to the selected weapon and stance | BB-003 |
| Actual weapon exchange near 0:54 | The weapons meet | Local contact feedback appears. Both continue playing the same encounter | BB-004 |
| Viable fighter receives local arm or leg damage | A documented nonterminal wound restricts capability | The affected hold, stance or stand action can become unavailable. This branch is documented in the booklet | BB-005 |
| Tatsumi is active and exposed to contact | The decisive hit lands | Tatsumi falls; the fight settles without a round-count requirement | BB-006 |
| Result is settled | Replay and result interval finish or advance | The same protagonist appears with Mikado and active movement resumes | BB-007 |

## Strategic and experiential structure

The visible current weapon position, movement and feedback make
spacing matter from the first exchange. Contacts can leave the
fight active, restrict an opponent's next action or terminate
the duel. A posture change may matter even with both fighters'
equipment unchanged.

## Replay and variation

In W1 the exchange lasts through several visible contacts
before the hit that settles it. W2 reaches the effect and fall
shortly after the fighters first appear. Both routes replay
the result and proceed to Mikado. The replay shows committed
history, with no second playable round against Tatsumi.

## Adjacent systems and history

The North American booklet describes honor restrictions for
Story Mode. W2 advances through the opening duel and eventually displays
an explicit honor reprimand. The evidence here establishes
a local result and successor rather than the exact rule for
the whole campaign. The later route and second opponent's result
remain out of scope.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-223, ACT-295, ACT-459, ACT-853 | Position, defend, attack, change stance and select opening equipment |
| System Behaviour | SYS-868, SYS-1850, SYS-1851, SYS-1852, SYS-1853 | Transform strike availability, resolve weapon and body contacts, settle the winner and play the successor |
| Constraint | None | Effective restrictions are part of the documented wound and stance rules |
| Information | INF-595 | Read distinct contact feedback and live pose |
| Objective | OBJ-329 | Win the one live adversary encounter |
| Time | TIM-003 | Execute decisions while the exchange progresses |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `640` (`GAME-0001`–`GAME-0640`).
- Exact genome matches: none.
- Tied near matches: `GAME-0455` — Soulcalibur (`6 / 31 = 0.193548`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Soulcalibur (GAME-0455)](../s-z/soulcalibur.md) | ACT-008, ACT-223, ACT-295, ACT-459, SYS-868, TIM-003 | Both use live spacing, attacks and defence with stance-dependent moves. Soulcalibur's scoped bout uses vitality, time and ring edge adjudication. Bushido Blade distinguishes weapon contact and local impairments from the hit that ends one continuous duel. | Near, `0.193548` |

## Taxonomy impact

Six new definitions cover independent opening loadout, clash
and defence break, retained local impairment, one-contact result,
replay-to-successor and direct feedback. Seven definitions are reused.

## Negative results

- A weapon flash and a low pose are each insufficient to prove
  a crippling wound. The documented consequence is separate.
- The first result does not require a displayed health depletion,
  timer expiry or an accumulated series of round wins.
- The same first opponent seen on the Replay camera is a replay
  of the settled exchange. Mikado is the distinct active successor.
- The first opponent's defeat and the next match alone cannot
  establish secret-ending eligibility.

## Delta summary

Thirteen genes include six new definitions and seven reused ones.
Existing signatures and taxonomy boundaries remain intact.

## New facts

- The first fight can continue through local weapon contact.
- A decisive body result ends the fight even though the opponent
  could still act before it.
- After the replay of that result, active control resumes against
  a distinct opponent.

## Principles and design implications

- Distinguish an interrupted weapon contact from physical
  impairment and a settled result with readable local feedback.
- Let changes in a fighter's capabilities affect what the player
  can do next.
- Separate result presentation from the next playable encounter.

## Puzzle or game generation potential

Prototype a small turn-free contest with two positional fields,
distinct visible contact outcomes, a persistent local impairment
and a fast terminal result. Keep the successor separate from the
presentation of the past exchange.

## New genes

ACT-853, INF-595 and SYS-1850 through SYS-1853.

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_387](../../../research/taxonomy-changes/TAXONOMY_CHANGE_387.md).

## New questions

Which separate first-duel contacts are counted against the
Story honor condition, and at which later point is it evaluated?

## Next recommended game

Analyse Venba on Xbox Series X|S through one evidenced early
dish, its recipe interpretation, the completed result and
narrative successor.

## Why this game

The opponent's live capability can change at an individual
contact and the first decisive result immediately changes
which opponent the player faces.
