---
game_id: GAME-0665
slug: sega-worldwide-soccer-97
game_title: "Sega Worldwide Soccer '97"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-052
    - ACT-267
    - ACT-268
    - ACT-269
    - ACT-883
    - ACT-884
    - ACT-885
    - ACT-886
  system:
    - SYS-457
    - SYS-459
    - SYS-460
    - SYS-461
    - SYS-462
    - SYS-463
    - SYS-1912
  constraint:
    - CON-398
    - CON-399
    - CON-400
    - CON-401
    - CON-880
  information:
    - INF-116
    - INF-178
    - INF-291
  objective:
    - OBJ-090
  time:
    - TIM-003
---

# Game: Sega Worldwide Soccer '97

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
National team names, formation numbers, button names and the recorded score
are parameters of this match.

## Analysis scope

- Version / ruleset: original English North American Sega Saturn
  commercial CD, Sega of America product 81112, 1996. One ordinary
  one-player versus computer Exhibition with the standard pad
  assignments. The package is documented, not an authenticated image
  of the disc from either recording.
- Structured analysis target: PLAT-SEGA-SATURN in
  `knowledge/platforms/games.json`. The linked instruction booklet
  is Sega's North American manual.
- Entry: select Exhibition, one player versus the computer, and the
  two national teams. Confirm Game Setup and Strategy, then take the
  first centre kick-off. England and El Salvador are the recorded sides,
  at Second Stadium with night and rain selected.
- Primary decision loop: steer the currently marked footballer and
  transfer control as the ball moves. Choose the direction and kind of
  pass or shot on the ball. Out of possession, close a passing lane,
  challenge the carrier or order the team to re-form. Adapt to the
  next live ball or official restart, and protect the score advantage
  through the second-half whistle.
- Exit: the 4–1 attempt settles as WIN for England and LOSE for El
  Salvador. Inspect match totals, goal times and player facts, then
  select Exit to reach the actionable Play Again choice. The main
  recording highlights No and fades after selection. The manual
  identifies the successor as Mode Select. End at the result-backed
  choice rather than another match.
- Included: match setup and formation, one-player control transfers,
  continuous ball and running play, passes, shots, challenges, team
  orders and keeper handling, field boundaries, fouls, offside and
  restarts under the applicable settings, goals, two regulation halves,
  the final score and its next menu.
- Excluded: multiplayer, player editing, season/tournament progress,
  rank and cup qualification, replay camera controls, shoot-outs and
  extra time as played phases, other regional builds, the Windows port
  and the other Saturn entries. Exact executable, pad trace, physics
  coefficients, switching ties and full foul adjudication thresholds
  were not verified.
- Potential scoped modules: the regulation tie with different rule
  toggles, a controlled penalty shoot-out, formation-order comparisons
  or weather effects under like-for-like inputs.

## Direct-play status

No personal play, installation or verified original Saturn hardware.
The North American booklet documents the eligible mode and controls.
A full Saturn trace follows England against El Salvador through
results and the next choice but gives no verified region or binary.
A USA-attributed emulated trace corroborates ordinary opening play
and presentation without reaching a full result. Static frames
were inspected in the background without sound.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| WWS-001 | Sega sold the 1996 North American Saturn edition under product 81112. Exhibition is a one-match branch. W1 selects England versus El Salvador in the one-player branch and confirms a rainy night at Second Stadium. | Observation | Corroborated | High | D1 packaging, P1 pp. 9 and 15–18, W1 2:37–4:20. |
| WWS-002 | The D-pad moves the marked teammate. Auto transfers the mark when another eligible teammate is nearer. Manual uses R to move the mark to the next closest teammate, while the rest of the side remains active. | Observation | Corroborated | High | P1 pp. 4, 6 and 22, W1 5:12–5:24, W2 0:48–1:20. Recorded Marker values and distance ties are unverified. |
| WWS-003 | A carrier can choose directional B ground passes, C lobs and A shots. Quick repeated A or C substitutes a ground shot or chip for its single-press action. Without the ball, A tackles and B shoulder-challenges. | Observation | Corroborated | High | P1 pp. 4 and 23–24; W1 5:12–5:24 and 11:03–11:14 support visible movement and shot states but do not identify exact presses. |
| WWS-004 | Select tactics, formation and line or sweeper defence in Strategy, with eligible member substitutions. In live defence, Y orders pressing, Y and Z together order individual marking and Z orders a line step for an offside trap. | Observation | Direct | High | P1 pp. 18–20 and 25; W1 3:54–4:20 confirms the formation and tactic screens only. |
| WWS-005 | The keeper normally responds autonomously. X requests manual keeper control while in view. A keeper holding the ball grants direct distribution, with B to a near teammate and A for a long kick. | Observation | Corroborated | High | P1 p. 25, W1 16:29–16:35 and the five home saves in W1 20:24–20:28. The control request itself is manual-sourced. |
| WWS-006 | The ball persists through contact and free motion. Live play yields to law- and location-specific restarts. Fouls and offside, when enabled, can cause free kicks, with the penalty area changing a foul restart. Dangerous play can draw a caution or dismissal. | Observation | Corroborated | High | P1 pp. 6, 22 and 26–27, W1 10:37–10:45 and 20:18–20:28, W2 1:44–2:00. |
| WWS-007 | Regulation uses two halves and the greater valid goal total decides a decisive fixture. A tied regulation score can settle as a draw with both continuation options off. Short goal presentation and replay precede a centre restart. | Observation | Corroborated | High | P1 p. 21 and mode flow p. 9; W1 5:12, 11:09–11:27, 12:50 and 19:35–19:47. |
| WWS-008 | W1's settled score is England 4–1 El Salvador, 1–1 in the first half and 3–0 in the second. The settled goal list credits Jacinto at 30 minutes, Simmons at 42 and Chapman at 52, 58 and 77. Results expose team totals and per-player numbers. | Observation | Direct | High | W1 20:16–20:54, including Goals. P1 pp. 30–31 defines the report. |
| WWS-009 | After exiting the Exhibition result, choose to play again with the same teams, change teams via Play Type, change match settings or return to Mode Select. W1 reaches that four-option menu. | Observation | Corroborated | High | P1 p. 32, W1 20:56–20:59. No second match was played in the trace. |

## Basic data

- Release / origin: Team Aquila / Sega, 1996. D1's US physical
  record gives product 81112 and UPC 010086811124. October day
  listings vary and the scope uses the year.
- Puzzle families: FAM-009 (tactical forecast and counterplay)
  for deciding where to deliver or challenge a live ball, and
  FAM-010 (real-time system pressure) for moving players, clock,
  possession and short recovery windows.
- P1: [original North American Sega instruction booklet](https://archive.org/download/SEGASaturnManuals_201812/Sega%20Worldwide%20Soccer%20%2797%20%28USA%29.pdf).
  Printed pages 4, 6, 9, 15–27 and 30–32 establish the selected
  controls, rules and completion route. The scan SHA-256 is
  `3e2e88286e0233a45386ffecf784b93327e999c616f66a13d84c645720b30f10`.
- D1: [Satakore North American packaging and disc catalogue](https://www.satakore.com/sega-saturn-game%2C%2C81112%2C%2CSega-Worldwide-Soccer-97-USA.html).
  The cover, country and product code identify the edition.
- W1: [Raw Gameplay Footage, complete Saturn Exhibition](https://www.youtube.com/watch?v=I9OED2rH-tI).
  Match confirmation near 3:40, kick-off 5:12, equaliser
  11:12 and restart around 11:25, late second half 19:30,
  results 20:16–20:54 and Play Again at 20:56–20:59.
  The recording provides no verified region.
- W2: [Metal Gamer Suneku, USA-attributed Ymir capture](https://www.youtube.com/watch?v=PLO5Ao6vGzE).
  The opening Portugal and Spain fixture shows a marked
  player, the joint radar and ball, a throw or restart,
  and changing control before the trace ends in the first
  half. Used only for these visible shared controls and states.
- Claim IDs: WWS-001–WWS-009.

### Reproducible route evidence

1. Load a North American copy. Choose Exhibition and the
   one-player branch. Select England and El Salvador for the
   recorded pairing. Check Game Setup and Strategy. W1 shows
   a rainy night, England's 4-4-2 and El Salvador's 3-5-2 DV.
   Its exact half length, difficulty and Marker option are
   not independently identified. To run a pure regulation
   test, disable Extra Time and Shoot Out; enable offside,
   fouls and cards to see all relevant referee states.
2. At the centre, confirm kick-off. Follow the selected
   footballer, rather than relying on the bottom nameplate alone, when control
   and ball ownership differ. Use variable direction and
   the declared pass or shot button. The ball may be loose
   and a teammate or rival can reach it.
3. For a legal attack, move the ball before the defender
   closes space. For a defensive recovery, close the lane
   or challenge with A or B and accept the referee's
   decision. W1 shows the 0–1 deficit and an El Salvador
   dead-ball restart around 10:37–10:41. At 11:09–11:27
   the England equaliser changes the live score and the
   opponent resumes from centre.
4. Match play continues into the second half without losing
   the 1–1 first-half total. Extend or protect the advantage
   while the clock advances. The captured second half
   ends 4–1 in favour of England; the game displays the
   win at 19:47.
5. Read the settled 4–1 at 20:16. Match Stats lists shots,
   possession, passes and penalties. Goals lists five marks
   in time order; Player Facts can switch between the sides.
   Choose Exit at 20:56 to expose the next consequence:
   same teams, other teams, changed settings or return to
   modes. This next choice is the analysis endpoint.

## Mechanical decomposition

### Action Genes

- ACT-008 and ACT-052: move the marked player with the pad or
  transfer the active controller locus within the same side.
  WWS-002, WWS-005.
- ACT-267 and ACT-268: deliver the ball directionally toward
  a teammate or attempt an opponent goal, using separate kick
  inputs. Keeper and corner B can seek the nearest teammate.
  WWS-003, WWS-005, WWS-006.
- ACT-269: choose a slide or shoulder challenge without
  already holding the ball. WWS-003, WWS-006.
- ACT-883: a quick second press selects the alternate
  trajectory of the same shot or lob input. WWS-003.
- ACT-884: set the one-match team tactics, spatial system,
  defensive type and eligible lineup while retaining direct
  field control at kick-off. WWS-001, WWS-004.
- ACT-885: explicitly continue or leave Exhibition after its
  settled result, choosing what to carry to the next setup.
  WWS-009.
- ACT-886: command planned defence shapes in live play while
  still directly steering one player. WWS-004.

### System Behaviour Genes

- SYS-457: one shared ball persists as it is passed,
  challenged, held or set at a restart. WWS-003, WWS-006.
- SYS-459: unswitched teammates and opposing members
  run to support, mark or challenge according to the
  current orientation and team posture. WWS-002, WWS-004.
- SYS-460: award and stage the applicable restart after
  an offence or boundary. WWS-006.
- SYS-461: the keeper responds to the threat independently
  until manual control is taken or gained. WWS-005.
- SYS-462: a valid goal immediately changes the count
  and ultimately returns the ball to centre for the other
  side. WWS-007.
- SYS-463: the clock progresses through two regulation
  halves; in a decisive fixture compare the score at expiry.
  WWS-007, WWS-008.
- SYS-1912: switch eligibility and selection depend on
  Auto or Manual marker policy, with a separate keeper
  visibility and held-ball rule. WWS-002, WWS-005.

### Constraint Genes

- CON-398: the one human controls at most one of the
  eleven footballers; other active members are not removed
  or simultaneously steerable. WWS-002.
- CON-399: field and goal lines and last touch determine
  the boundary outcome and location of the restart. WWS-006.
- CON-400: enabled offside can bar attacking involvement
  and award the other team a free kick. The executable's
  borderline formula is unverified. WWS-006.
- CON-401: illegal contact can concede a free kick or
  penalty, and serious or repeated cautioned contact can
  dismiss a player. WWS-006.
- CON-880: the same buttons change available effects by
  ball and handling context. WWS-003, WWS-005.

### Information Genes

- INF-116 and INF-178: the play view exposes the score,
  half, clock, named current players, marked control,
  ball, pitch and nearby shape via the radar. WWS-002,
  WWS-006, WWS-007.
- INF-291: the settled result shows final and half scores,
  WIN and LOSE, plus separate match statistics, goal times
  and player facts. WWS-008.

### Objective Genes

- OBJ-090: have more valid goals at the second-half expiry
  in a decisive fixture, respecting a documented draw branch
  if both continuation options are off. WWS-007, WWS-008.

### Time Genes

- TIM-003: players and ball advance in live time while
  the controller can act. An official interruption and
  result replace the live phase. WWS-002, WWS-006, WWS-007.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| One-player Exhibition and chosen teams | Confirm stadium, conditions and Strategy | First kick-off with one marked member | WWS-001, WWS-004 |
| Marked carrier has the ball | Choose direction and pass, lob, chip or attempt a shot | Ball travels before the next contest for possession | WWS-003 |
| Friendly control and an opponent carrying the ball | Steer the defender and press A or B | Try a slide or shoulder challenge; an offence may stop play | WWS-003, WWS-006 |
| Keeper has claimed the ball | Use B for a near teammate or A for a long kick | The shared ball leaves the keeper's hands in the selected distribution | WWS-005 |
| England has just equalised | Settle the goal and play resumes from centre | El Salvador restarts at 1–1 | WWS-007 |
| Second half expires at 4–1 | Let the result settle and inspect the figures | Final score, player statistics and goal chronology are stable | WWS-008 |
| Settled Exhibition result | Choose Exit | Four-option Play Again menu, with branches for retention, revision or exit | WWS-009 |

## Strategic and experiential structure

The human manages a single moving point of control in a larger
team. A pass changes what space is reachable before the opponent
can challenge. A late tackle may sacrifice a free kick rather
than recover the ball. The chosen formation is a starting
organisation for the whole side, and live orders can briefly
adjust the defenders while one body still answers movement.
The match's tally, not an isolated highlight, owns the outcome.

## Replay and variation

The recording shows one successful outcome, not a deterministic
scoring sequence. Alternate teams and settings change the setup,
and manual control can change which player receives the next
command. The same-team rematch is an explicit choice. The match
record supplies opportunities to test near-ball transfers,
single- or double-press kicks and after-goal restarts independently.

## Adjacent systems and history

League and cup modes have separate progress and saving screens.
A tied Exhibition can branch by two independent settings.
The North American disc, the Windows derivative and the related
Saturn entries are distinct publication targets.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-052, ACT-267, ACT-268, ACT-269, ACT-883, ACT-884, ACT-885, ACT-886 | Move and transfer control, play the ball, challenge, configure play and take the next result branch |
| System Behaviour | SYS-457, SYS-459, SYS-460, SYS-461, SYS-462, SYS-463, SYS-1912 | Resolve shared ball, team AI, adjudication, keeper, goals, regulation and policy-based marking |
| Constraint | CON-398, CON-399, CON-400, CON-401, CON-880 | One controller locus, geometry, offside, lawful contact and context-dependent controls |
| Information | INF-116, INF-178, INF-291 | Live score and local shape plus settled match and individual reports |
| Objective | OBJ-090 | Lead the valid goal count at the end of regulation |
| Time | TIM-003 | Play responds under a live clock between rule stops |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `664` (`GAME-0001`–`GAME-0664`).
- Exact genome matches: none.
- Tied near matches: `GAME-0163` — EA SPORTS FC 26 (`19 / 27 = 0.703704`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [EA SPORTS FC 26 (GAME-0163)](../a-f/ea-sports-fc-26.md) | ACT-008, ACT-052, ACT-267, ACT-268, ACT-269, CON-398, CON-399, CON-400, CON-401, INF-116, INF-178, OBJ-090, SYS-457, SYS-459, SYS-460, SYS-461, SYS-462, SYS-463, TIM-003 | Both use switched direct control, off-ball team AI, one spatial ball, referee restarts and two-half score settlement. Sega documents proximity-triggered switching, repeat-press kicks and immediate defensive orders while preserving manual movement. The modern assisted targeting and contact formula is not established for the older release. | Near, `0.703704` |

## Taxonomy impact

The six additions split repeated-button input, on-pitch setup,
post-match retention choice, live team tactics, controller
assignment and context-specific input legality. The manual
documents near-teammate distribution in particular contexts
but does not expose a general assisted targeting formula
equivalent to SYS-458. Reusing contact and passing genes
does not import that extra system from a modern title.

## Negative results

- The input for a shot with the ball can become a defensive
  slide when the marked player lacks it.
- An ordinary goalkeeper catch does not leave the keeper
  purely autonomous while holding the ball.
- One yellow card does not by itself expel a player. W1's
  home totals show four yellow cards and no red cards.
- A settled Exhibition result is not a league save or
  a new fixture already in progress.
- Exact assist strength, rain physics, interception
  coefficients and passing-target ties remain unmeasured.

## Delta summary

Twenty reused mechanics and six new boundaries in the scoped match.

## New facts

- Marker policy can make a move command change recipients
  within the team without substituting a player.
- Shot, pass and defence respond to the ball context. The
  same set of buttons also has a distinct keeper-held mapping.
- Exit from the result presents a meaningful choice
  between three ways to continue and leaving the mode.

## Principles and design implications

When a control identity moves among active teammates, keep its
marker visible and distinguish it from possession. Show the cost
of a risky challenge through the resulting restart and sanction.
Keep condensed goal history and player statistics accessible
after live pressure ends.

## Puzzle or game generation potential

An original short shared-ball contest could preserve one direct
control marker per human while an independent team formation
reacts to position. Vary only the marker policy and restart
rules to test how the local decisions change.

## New genes

- ACT-883
- ACT-884
- ACT-885
- ACT-886
- CON-880
- SYS-1912

## New combinations

None. None of the 274 verified combination signatures is a proper subset.
COMB-0161 requires SYS-458, whose full assisted targeting and
contact inputs were not established in this edition.

## Taxonomy changes

[TAXONOMY_CHANGE_411](../../../research/taxonomy-changes/TAXONOMY_CHANGE_411.md).

## New questions

Which marker is selected when two teammates are equally near?
How do weather and body orientation interact when repeating
the same kick? Which extra-time and penalty result screens
are shared with the independently launched shoot-out?

## Next recommended game

Chicory: A Colorful Tale, fully released Xbox Series X|S edition.
Follow a scoped brush interaction through a completed local
puzzle and its first playable successor.

## Why this game

The ordinary fixture combines transferable player control, one
shared ball, live team shape, referee decisions and a genuine
settled result with a selectable continuation.
