---
game_id: GAME-0577
slug: people-of-note
game_title: People of Note
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-019
    - ACT-222
    - ACT-223
  system:
    - SYS-1694
    - SYS-1695
    - SYS-1696
    - SYS-1697
    - SYS-358
  constraint:
    - CON-269
    - CON-756
  information:
    - INF-119
    - INF-142
    - INF-550
  objective:
    - OBJ-029
  time:
    - TIM-039
---

# Game: People of Note

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Choose who acts on the next allied measure. Once the move begins, match
its rhythmic cue. The boss's separate escalation rewards winning before
too many Stanzas elapse.

## Analysis scope

- Version / ruleset: English full-release Nintendo Switch 2 base game
  launched 7 April 2026, US store product 70010000111667. First proper
  Yuna Verse encounter in Chapter 1, Pop and Locked In. Rising Talent
  difficulty, active combat and manual timing. Exact installed version
  and presentation latency are unverified.
- Structured analysis target: PLAT-NINTENDO-SWITCH-2 in
  knowledge/platforms/games.json.
- Entry: advance the normal opening with Cadence and Cerrin past the
  preceding club access tasks to their first confrontation with Yuna
  Verse at Whirls Generation. Start at the first actionable encounter
  state. Use the admitted early repertoire with no later party, stones
  or elective extra-action setup. No particular character level, stats or
  starting BP inferred from unlike-platform footage.
- Primary decision loop: read both action counts, the next measures,
  available performers and their personal BP. Choose the current performer
  and command or Rest. Resolve its real-time timing when prompted.
  Reconsider the next measure after the effect, and respond to scheduled
  enemy attacks. Watch Crescendo while managing damage and recovery.
- Positive exit: defeat the required enemy set through the ordinary
  encounter and reach the post-fight clef handoff dialogue. Stop before
  travel out of Chordia. The earlier audition is a different scene.
- Negative exit: an individual's zero HP can make them faint while the
  other musician still acts. Losing the last able party performer prevents
  this combat clear. No exact Game Over menu, retry snapshot, or interval
  and cost for revival on the target console is claimed.
- Included: ordinary early party slots, personal BP, Rest, measure-addressed
  support, a timed attack, responsive defence, opponent schedule, boss
  escalation, individual faint and the story battle clear.
- Excluded: the audition, quiz and drink gates, the club exploration segment,
  optional random encounters, whole weapon/Remix Stone loadout optimisation,
  later bandmate Mashups, final chapters, Yuna's later rematch, assisted
  timing and combat skip, the prerelease demo and other platform rulesets.
- Potential scoped modules: genre-changing Mashups after Fret joins or a
  fixed-roster Puzzle Battle with an authored action limit.
- Direct-play status: not conducted. Target product material and Switch 2
  play accounts establish native release and common controls. Creator
  interviews, launch-period accounts and static Windows storyboard frames
  identify the encounter and visible transitions. No console runtime,
  audio playback or motion-video playback was used. The PC frames do not
  establish Switch 2 timing tolerances, exact numbers or hardware parity.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PON-001 | The full Nintendo Switch 2 base game launched on 7 April 2026. Rising Talent is the middle difficulty; the enabled combat and manual-timing options define this packet. | Observation | Corroborated | High | P1, P2, P3, R1 |
| PON-002 | Combat groups ordered action measures into Stanzas. The displayed pair of counts allocates actions to the two sides, separately from personal BP. The staff exposes the action schedule and upcoming opposing moves. | Observation | Corroborated | High | P3, P4, R1, R2, W1 |
| PON-003 | The player chooses eligible allied performers and resolves one action before choosing the next. In the ordinary opening allocation, give each eligible member its opportunity before relying on extras. The party is Cadence and Cerrin in this encounter. | Observation | Corroborated | High | P4, R1, R2, R3, W1 |
| PON-004 | Songstone commands spend personal BP when affordable. Rest trades a measure for BP and a defensive posture. Early Instant Hit is shown at three BP in the recorded build. Battle resources do not require carrying a consumable supply forward. | Observation | Corroborated | High | P3, R2, R3, W1 |
| PON-005 | Cerrin's B-Side addresses a measure. A performer who uses the prepared measure can receive an effect such as BP recovery. This is not unrestricted direct targeting of a recipient. | Observation | Corroborated | Medium | P4, R4, W1 |
| PON-006 | Confirm presses during the selected action are judged with overlapping ring cues. Successful timing increases the realised attack effect, and a miss can still leave the base result. Enemy execution permits a separate timed defence. | Observation | Corroborated | High | P2, R1, R2, R5, W1 |
| PON-007 | The encounter introduces Crescendo, visibly increasing boss power as battle proceeds. Reported gauge segments represent strengthening thresholds. One fainted ally can leave the other able to take a measure. | Observation | Corroborated | High | P4, R1, R2, R3, W1 |
| PON-008 | Yuna's first authored defeat leads to the clef handoff and the search for a band. The later Yuna encounter is a different state and is excluded. | Observation | Corroborated | High | R3, R4, W1, W2 |

## Basic data

- Iridium Studios / Annapurna Interactive. Family FAM-015, agent routing
  and coordination through ordered, compatible party roles.
- P1: [Nintendo Switch 2 product](https://www.nintendo.com/us/store/products/70010000111667/).
  Release date, console, commercial product and publisher, checked
  2026-11-20.
- P2: [Annapurna's product page](https://annapurnainteractive.com/games/people-of-note)
  and [publisher's mechanical overview](https://www.new.annapurnainteractive.com/en/games/people-of-note).
  Full release date and the distinction between turn-based choices,
  real-time rhythmic execution and configurable game modes.
- P3: [Jason Wishnov interview in Game Developer](https://www.gamedeveloper.com/design/behind-people-of-note-s-methods-for-luring-players-into-enjoying-a-musical).
  Release-day developer account of the two action counts, staff design,
  fresh encounter resources and configurable combat.
- P4: [Jason Wishnov interview in RPGamer](https://rpgamer.com/2026/04/people-of-note-interview/).
  Explains direct control of upcoming allied order, visible enemy forecast,
  power escalation and effects addressed to measures.
- R1: [Hey Poor Player's Switch 2 play account](https://www.heypoorplayer.com/2026/04/07/people-of-note-review-switch-2/).
  Confirms Rising Talent, the top and bottom action counts, freely chosen
  allied order with ordinary eligibility, ring inputs and staged Crescendo.
- R2: [RPGFan's full-release play account](https://www.rpgfan.com/review/people-of-note/).
  Explains the shown battle score, per-performer resources, action order,
  timing and stronger later measures. Genre bonuses and late Mashups are
  not inferred for this first boss.
- R3: [Stack Up's PS5 play account](https://www.stackup.org/post/review-people-of-note).
  Confirms Yuna's first party, Instant Hit, Rest, the clef and the
  basic boss pressure. The secondary platform's button map is outside scope.
- R4: [Story and battle reference from GAMES.GG](https://games.gg/people-of-note/guides/people-of-note-full-trophy-guide/).
  Distinguishes the first victory from the optional rematch, and describes a
  later documented placement of the same B-Side effect on a chosen measure.
  Special remixes and amounts from its extra-action cases are excluded.
- R5: [Gaming Respawn's full-release timing comparison](https://gamingrespawn.com/featured/64591/people-of-note-review/).
  A timely prompt yields a higher attack result than a missed prompt. It
  corroborates the cue and the limited penalty without establishing
  the target hardware's threshold.
- W1: [Welonz's full-release PC first-chapter record](https://www.youtube.com/watch?v=WsvP4bEGOD4&t=4850s).
  Static storyboard stills sampled from approximately 1:20:50 to 1:28:10.
  They identify the first battle, both allied performers, the Crescendo
  and faint tutorials, BP commands, visible grade changes, continuing
  play with a fainted ally and the clef handoff. No audio, precise
  frame timing or complete attack pattern is inferred from 10-second samples.
- W2: [Passione Videogiochi's written opening walkthrough](https://www.passionevideogiochi.it/people-of-note-guida-completa-e-soluzioni/).
  Its Yuna Verse section corroborates the boundary after club access and
  the transition towards Durandis. The story still is independent
  context, separate from the native console release evidence.

## Mechanical decomposition

### Action Genes

- ACT-019 covers selecting an eligible performer and one of that
  performer's current targetable commands.
- ACT-222 covers committing the confirm input when the cue aligns during
  the selected offensive or support action's execution.
- ACT-223 covers defensive timing in a scheduled enemy action. It does
  not spend the next allied measure or follow the offensive cue as a second
  mandatory step.
- Claim IDs: PON-002–PON-006.

### System Behaviour Genes

- SYS-358 applies the live-input grade to the selected command's effect.
  A weaker timed result is distinct from refusing an unaffordable skill.
- SYS-1694 sets separate allied and hostile measure counts for the current
  Stanza. No arithmetic equivalence with BP is inferred.
- SYS-1695 spends the acting performer's BP on a skill or restores it
  through a Rest commitment that also protects the performer.
- SYS-1696 places support on a selected measure and applies it when that
  measure is used. B-Side differs from directly casting on a named ally.
- SYS-1697 advances Crescendo as the encounter continues. Its thresholds
  strengthen the active boss without themselves settling victory or defeat.
- Claim IDs: PON-002–PON-007.

### Constraint Genes

- CON-269 covers legal targets and sufficient BP for the selected
  command. An attack and a paid skill consume an action opportunity
  without drawing the same BP.
- CON-756 covers one ordinary opportunity per eligible active member
  in the ordinary two-member allocation, with control of their order.
  Additional measure effects or an unavailable performer are separate
  cases. The capture does not prove the general rule for every extra slot.
- Claim IDs: PON-002–PON-005, PON-007.

### Information Genes

- INF-119 exposes health, BP and currently eligible skills per performer.
- INF-142 exposes the live timing prompt and resulting grade during an
  action. It gives an observable alignment cue without a verified interval
  in frames or milliseconds.
- INF-550 shows the two action budgets and relative hostile schedule
  before command selection, with a separate visible Crescendo gauge.
- Claim IDs: PON-002, PON-004, PON-006, PON-007.

### Objective Genes

- OBJ-029 settles the bounded required battle set before the story
  resumes with the clef conversation. It does not encode the campaign
  or require a perfect grade.
- Claim IDs: PON-007, PON-008.

### Time Genes

- TIM-039 separates waiting at a decision, live timing within the
  reached measure and the decision after that measure resolves.
  It does not collect all party actions before executing them.
- Claim IDs: PON-002, PON-003, PON-006.

## Reproducible transitions

| State / precondition | Action or event | Observable transition | Boundary | Claims |
| --- | --- | --- | --- | --- |
| First Whirls Generation confrontation, active combat | Begin the confrontation with both opening musicians | Action measure schedule and Crescendo appear | No later Yuna encounter or Mashup roster | PON-001–PON-003, PON-007 |
| A friendly measure is selectable | Choose its eligible performer and command | The current action begins with that performer | No full-team batch of commands is committed | PON-002, PON-003 |
| Cadence has enough BP to choose Instant Hit | Commit that command and time the prompts | Current measure and declared BP cost pay for an attack whose grade alters its result | Insufficient BP blocks selection; off-time execution can still resolve | PON-004, PON-006 |
| The eligible performer needs BP | Choose Rest for the current measure | Recover personal BP and defend in that measure | No extra action is bought by recovery | PON-004 |
| Cerrin can act and a later measure is eligible | Commit B-Side to the shown measure | The support modifier is available to its eventual user | The command does not guarantee a fixed recipient before that choice | PON-005 |
| The next scheduled opposing action executes | Respond to its live cue when offered | Resolve the defence attempt or take the corresponding effect | The attack sequence is separate from allied command timing | PON-006 |
| The unresolved fight continues | Allow further combat to settle | Crescendo advances and threshold power can rise | A full gauge is not an automatic loss | PON-007 |
| One ally reaches zero health while the other remains able | Continue through an eligible allied measure | The surviving performer still has an actionable turn | No exact revive command or console reload asserted | PON-007 |
| The required opposition is defeated | Read the post-battle exchange | Yuna's first defeat settles and the clef handoff follows | The later band quest and optional rematch are outside the packet | PON-008 |

## Strategic and experiential structure

- The party's ability to act now, the current performer's resource balance
  and their execution grade are three separate constraints. Spending BP
  can improve the chosen action without granting more measures.
- An addressed support effect can make the next eligible performer choice
  matter even before the attack cue starts. Rest increases future options
  but leaves less opportunity to win before the boss grows stronger.
- Illustrative decision state: if the remaining friendly measure is
  available and the active member lacks the cost shown for a skill, a
  legal Rest can improve a later BP balance. The same measure cannot
  also execute that skill. Check the next enemy and Crescendo state
  before treating a future resource gain as a guaranteed win.
- Claim IDs: PON-002–PON-008.

## Replay and variation

- Selection order, Rest, support placement and input grade can change how
  much damage arrives before the next power threshold. The two opening
  performers and the ordinary story terminal remain the same.
- The documented clear does not require perfect timing. Later difficulty
  and assist choices use other settings, and a replay's exact initial
  health, BP, boss schedule and timing tolerance are unmeasured here.
- Claim IDs: PON-001–PON-008.

## Adjacent systems and history

- The PC demo starts in a later chapter to expose systems the opening
  fight does not teach. Its Fret and genre combinations are not first-boss
  evidence. The rematch and later measure-changing loadouts are separate.
- The optional keyboard-style minigame has its own rhythm objective.
  In this battle, rhythm modifies chosen role-playing commands.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | ACT-019, ACT-222, ACT-223 | Select a command, execute its cue, defend on cue |
| System Behaviour | SYS-1694, SYS-1695, SYS-1696, SYS-1697, SYS-358 | Paired measure allowances, skill BP, support slot, escalation |
| Constraint | CON-269, CON-756 | Eligible performer, affordable skill |
| Information | INF-119, INF-142, INF-550 | Personal resources, timing cue, battle staff and gauge |
| Objective | OBJ-029 | Clear the first Yuna Verse encounter |
| Time | TIM-039 | Immediate per-measure settlement then choice |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `576` (`GAME-0001`–`GAME-0576`).
- Exact genome matches: none.
- Tied near matches: `GAME-0530` — Lost Odyssey (`8 / 29 = 0.275862`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0530` — Lost Odyssey | ACT-019, ACT-222, CON-269, CON-756, INF-119, INF-142, OBJ-029 and SYS-358 cover party command, target gates, ordinary slots, resource display and timing inside a scoped fight. | Lost Odyssey commits a party batch before speed-ordered resolution and uses a ring to modify eligible attacks. People of Note lets the player respond to the result of each measure before committing the next, with a prepared measure modifier and an explicit escalation meter. | Tied near: 8 / 29 = 0.275862 |

### Preserved research notes

- New genes: SYS-1694–SYS-1697, INF-550 and TIM-039.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_323](../../../research/taxonomy-changes/TAXONOMY_CHANGE_323.md)
  distinguishes measure count, action sequencing and time-sensitive effects
  from ordinary skill use, prompt input and timing grade.

## Negative results

- The first Yuna fight does not establish the later Mashup roster or
  justify attributing demo mechanics to the native opening battle.
- The cost displayed in the PC evidence establishes that snapshot, not
  every build or every modified Songstone. No exact grade thresholds,
  rhythm sync accuracy, boss strength formula, death save or unlock
  persistence after reloading has been measured.

## Delta summary

## New facts

- [Observation | Corroborated | High] PON-002–PON-007 separate the supply
  of actions, the skill resource and rhythm during chosen execution.

## New genes

- [Observation | Corroborated | Medium] Six additions in taxonomy change 323.

## New combinations

- [Observation | Corroborated | High] No new combination proposed.
  Existing supported subsets are owned by the comparison section.

## Taxonomy changes

- [Observation | Corroborated | Medium] Earlier definitions and signatures
  stay unchanged.

## New questions

- Native recordings with identical loadouts could settle exact BP and
  defence timing, measure count changes under faint and console retry.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0578, OutRun 2 on original Xbox.
- Optimisation criterion: compare timing execution within a command with
  continuous racing and a route choice under a timer.
- Backlog impact: second Selection 047 unit.

## Why this game

- [Hypothesis | Limited | Medium] The first complete boss includes two
  playable performers, a visible schedule and delayed power growth. It
  makes more decision boundaries observable than a single tutorial attack.
