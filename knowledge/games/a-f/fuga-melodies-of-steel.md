---
game_id: GAME-0626
slug: fuga-melodies-of-steel
game_title: "Fuga: Melodies of Steel"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-019
  system:
    - SYS-356
    - SYS-822
    - SYS-1827
  constraint: []
  information:
    - INF-581
  objective:
    - OBJ-029
  time:
    - TIM-001
---

# Game: Fuga: Melodies of Steel

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Names, weapon classes and the particular opening formation identify the observed battle.

## Analysis scope

- Version / ruleset: English commercial Standard Edition for Xbox Series X|S,
  product 9NLX3GWW0HF1, released July 29, 2021. The English Xbox
  recording does not identify the hardware model. A separately attributed
  Xbox Series S Game Pass recording corroborates the battle sequence.
  Exact builds and enabled extras are unverified.
- Primary decision loop: read whose activation is available and which
  weapon type matches the target's visible weakness. Commit the active
  gunner's ordinary attack against the opposing vehicle. Account for the
  target's postponed action when its marker breaks. Resolve the remaining
  activations until the hostile set is gone, accept the graded report
  and continue to the introduced route.
- Entry: the first controllable Taranis tutorial battle against a single
  Berman ground vehicle, before the initial attack. The opening crew
  assignments are those provided by the scenario.
- Exit: the enemy is removed, the Results book shows a rank and
  experience, and the opening route-progression display appears after
  the following exchanges. Stop before the second battle.
- Included: discrete gunner commands, the visible mutable activation
  order, the active weapon and exposed weakness class, ordinary attack
  damage and the confirmed delay, elimination of the single opposing
  unit, graded settlement and onward route presentation.
- Excluded: the second tutorial battle and its formation exercise,
  reserves and support modifiers as separate actions, unobserved skill
  or guard commands, items, camp and affinity management, route branching,
  later enemies with multiple markers, the Soul Cannon, later chapters,
  demo-specific behaviour, other editions and the sequels.
- Suggested later scope: follow the second encounter through the first
  in-battle formation change and prove its effect on a forecast turn.
  The first-battle packet does not establish that command there.

## Direct-play status

No direct play was performed. Xbox product and launch materials identify
the edition. CyberConnect2 documents the schedule and weakness rule and
illustrates them in an English mechanics guide. Only static frames were
inspected from the English Xbox trace and the separately attributed
Series S recording. A labelled Series X capture in German and a launch-era
trace corroborate the opening without independently authenticating every
detail of the English Xbox Series build. No installed binary, version
number, frame timing, rank formula or loss branch was verified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| FUG-001 | The commercial base game launched for Xbox Series X and Series S on July 29, 2021. Standard and Deluxe are separately identified. The scoped edition uses English text. | Confirmed | Corroborated | High | P1 and P2 establish product, edition and date. W1 has English Xbox menus; W2 is explicitly attributed to Series S. |
| FUG-002 | The first controllable battle pits the Taranis against one ground vehicle. The schedule displays allies and the hostile together. A currently acting gunner can issue a discrete ordinary attack. Each commitment settles before the next actionable turn. | Observation | Corroborated | High | W1 1:50–2:20, W2 1:10–1:30, P3 and P4 0:04–0:24. Exact scheduling coefficients were not measured. |
| FUG-003 | The initial yellow-marked weakness corresponds to the active grenade-launcher attack. The interface presents the weakness separately from enemy health and the acting crew member separately from the target. The formation is already supplied at entry. | Observation | Corroborated | High | W1 1:50–2:00; W2 1:20; P4 0:09–0:16 and 0:28–0:36; R1 explains the colour relation. |
| FUG-004 | A successful match can break the exposed marker and push the living enemy's pending activation later. An eligible ally can therefore act first even though the enemy is still present. This is distinct from removing a defeated actor. | Observation | Corroborated | High | P3 and P4 0:13–0:22, 0:33–0:43; W2 1:20 shows the yellow hit effect; W1 2:00–2:20 shows the changing line-up before the enemy vanishes. |
| FUG-005 | The battle ends after the single required enemy is gone. The Results book separately presents performance rank and crew experience, followed by dialogue and the visible route. A top grade is not needed for this path to continue. | Observation | Corroborated | High | W1 2:30–3:20 shows Results and the route; W3 2:40–3:50 shows the same order; W4 16:50–18:10 identifies the first tutorial result and successor. No exact reward coefficient is inferred. |
| FUG-006 | The first battle is completed on the supplied assignments. The broader official system supports changing a formation, but the reported first formation tutorial appears only after the opening Results and route. | Observation | Corroborated | Medium | W1 3:10–5:40, W2 1:50–3:40, P3. This does not assert every menu command is disabled during the first fight. |

## Basic data

- Analysis target: `PLAT-XBOX-SERIES`.
- Developed and published by CyberConnect2.
- Mechanical family: `FAM-009`, tactical forecast and counterplay.
- Checked: 2026-11-21.
- P1: [Xbox base-game product](https://www.xbox.com/en-us/games/store/Fuga-Melodies-of-Steel/9NLX3GWW0HF1).
- P2: [Xbox Wire launch notice](https://news.xbox.com/en-us/2021/07/29/fuga-melodies-of-steel-is-now-available-for-xbox-one-and-xbox-series-xs/).
- P3: [CyberConnect2 game system](https://www.cc2.co.jp/fuga/en/system.html).
- P4: [CyberConnect2 battle fundamentals](https://www.youtube.com/watch?v=rMACy5SyVVo).
  English static stills show the weapon prompt, initial shot, changing
  schedule and a separate example of the weakness rule.
- W1: [Year Of The Dad Gaming's English Xbox opening](https://www.youtube.com/watch?v=0TbURV9-UcI&t=110s).
  Results is visible at 2:30 and the route at 3:10. The author identifies
  Xbox Game Pass, with no claim about the console model.
- W2: [Otakugame's Series S report](https://otakugame.fr/lets-play-fuga-melodies-of-steel-sur-xbox-series-s-game-pass/)
  and [its own capture](https://www.youtube.com/watch?v=9biEExLnfho&t=70s).
  A coloured hit and the following route are visible. French presentation
  corroborates the sequence, without establishing exact English labels.
- W3: [XboxDynasty's Series X account](https://www.xboxdynasty.de/news/fuga-melodies-of-steel/gameplay-video-aus-dem-strategie-rollenspiel/)
  and [capture](https://www.youtube.com/watch?v=VlNzY1eUL6I&t=130s).
  The German-language showcase titles the clip a demo of gameplay. It
  corroborates the report and route, not access to the full licence.
- W4: [Launch-era account with marked opening battle](https://www.youtube.com/watch?v=puwbfUDbR_U&t=951s).
  The result precedes the chapter's route tutorial. It does not authenticate Xbox.
- R1: [Firsthand rules and interface walkthrough](https://shin-reviews.com/rt/review-tutorial-fuga-melodies-of-steel/),
  Battles section. Its colour-match and evaluation descriptions corroborate
  the rules rather than the exact Xbox configuration.

## Mechanical decomposition

### Action Genes

- ACT-019: choose the currently eligible gunner's ordinary attack and
  commit it against the given enemy.

### System Behaviour Genes

- SYS-356: advance the visible schedule for the allied crew and enemy as
  each activation settles.
- SYS-822: grade how the encounter was completed separately from
  establishing that the hostile set was defeated.
- SYS-1827: consume an exposed matching weakness on a successful hit
  to postpone the target's pending activation.

### Constraint Genes

No separate constraint is required. The class-match predicate is part
of the delay rule rather than a general restriction on attacking.

### Information Genes

- INF-581: show the current gunner's weapon category and the independent
  typed weakness marker beside the enemy's health for a pre-commit match.

### Objective Genes

- OBJ-029: eliminate the one required enemy while the Taranis remains
  active, then observe the report and the successor route boundary.

### Time Genes

- TIM-001: settle a committed activation discretely before another
  command can be chosen. This does not assume fixed alternating sides
  or a known per-actor countdown implementation.

## Reproducible transitions

| State | Input or event | Result | Evidence |
| --- | --- | --- | --- |
| First Taranis encounter, one ground opponent | Read the active gunner, schedule and target | Current operator and typed weakness are visible before the shot | FUG-002, FUG-003 |
| Initial matching marker is present | Commit the ordinary attack with the corresponding weapon | A landed match removes the weakness marker and pushes the living target's scheduled action later | FUG-003, FUG-004 |
| Combat is unresolved after the match | Resolve subsequent available gunner attacks | The affected enemy can remain alive even while another operator becomes eligible | FUG-002, FUG-004 |
| The only required target is eliminated | Allow the final activation to settle | Results records the victory evaluation and crew experience | FUG-005 |
| Results is visible | Acknowledge the report and advance the ensuing exchanges | The introductory route appears before the next encounter | FUG-005, FUG-006 |

## Strategic and experiential structure

A shot has both a damage effect and a conditional scheduling effect.
The useful comparison is between removing health immediately and changing
the order in which surviving opponents can act. A displayed marker lets
the player reason about the second effect before committing. The report
rates the attempt after the tactical objective is met. The first fight
does not require a preferred grade or a later formation command.

## Replay and variation

The English Xbox and marked launch-era traces show separately paced
play reaching the same Results and onward route. The Series S capture
also shows a successful matching strike followed by the route. Exact
scores, reward multipliers, revisiting the encounter and party or tank
state after a loss were not reproduced.

## Adjacent systems and history

CyberConnect2 separately documents formation changing, role pairing and
later options. Some appear in the next tutorial segment. They do not
establish a formation action in this first battle. Deluxe provides
separate extras and the later games add new effects. The scoped
signature is for this earliest ordinary battle in the first full release.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-019 | Commit the available gunner's attack at the opponent |
| System Behaviour | SYS-356, SYS-822, SYS-1827 | Mutable schedule, graded settlement and conditional target delay |
| Constraint | None | The visible match is a delay trigger rather than a legality gate |
| Information | INF-581 | Read active weapon and exposed weakness class |
| Objective | OBJ-029 | Remove the required enemy before tank defeat |
| Time | TIM-001 | Settle each discrete commitment before the next |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `625` (`GAME-0001`–`GAME-0625`).
- Exact genome matches: none.
- Tied near matches: `GAME-0449` — Paper Mario (`3 / 19 = 0.157895`); `GAME-0618` — Shining Force III (`3 / 19 = 0.157895`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Paper Mario (GAME-0449)](../m-r/paper-mario.md) | ACT-019, OBJ-029, TIM-001 | Both choose discrete actor-specific attacks to clear a finite enemy set. Paper Mario can reorder its player pair before either acts and tests offensive or defensive timing during resolution. The Taranis acts with the currently scheduled operator and can move a living target later by matching its weakness. | Near, `0.157895` |
| [Shining Force III (GAME-0618)](../s-z/shining-force-iii.md) | ACT-019, OBJ-029, TIM-001 | Both resolve separate activations into a complete enemy clearance. Shining Force III uses movement and terrain reach before a unit commits a strike or spell. The two vehicles stay in their battle presentation while the Taranis uses weapon matching to change an existing turn. | Near, `0.157895` |

## Taxonomy impact

[TAXONOMY_CHANGE_372](../../../research/taxonomy-changes/TAXONOMY_CHANGE_372.md)
separates visible type matching from its scheduling effect.

## Negative results

- SYS-855 grants another action on weakness knockdown. The scoped hit
  here changes the surviving target's existing place on the schedule.
- SYS-1686 accumulates the acting unit's own command costs. The verified
  effect here postpones a target via a matching hit.
- INF-538 reveals weakness by a learned scan, whereas the initial badge
  here is visible without one.
- Neither a crew-reassignment rule nor a Soul Cannon activation is
  imported from the later tutorial.

## Delta summary

Admits the first complete ordinary Taranis battle through its scored
report and visible continuation to the route.

## New facts

- A visible typed weakness can delay the enemy independently of defeat.
- The active operator, next actors and persistent target are separable.
- The first report presents grade and crew experience before the route.

## New genes

SYS-1827 and INF-581.

## New combinations

None.

## Taxonomy changes

[TAXONOMY_CHANGE_372](../../../research/taxonomy-changes/TAXONOMY_CHANGE_372.md).

## New questions

Which next-tutorial changes to the crew replace an upcoming activation,
and how is the subsequent restriction on another change represented?

## Next recommended game

Continue with the original North American GameCube release of Killer7.
Verify its first complete local encounter and renewed route movement.

## Why this game

The same tactical shot may damage an enemy and alter its pending turn
without defeating it. The result screen separates victory from evaluation.
