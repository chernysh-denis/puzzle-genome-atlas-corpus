---
game_id: GAME-0714
slug: thirsty-suitors
game_title: "Thirsty Suitors"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-222
    - ACT-592
    - ACT-930
  system:
    - SYS-358
    - SYS-1180
    - SYS-2001
    - SYS-2002
  constraint:
    - CON-351
  information:
    - INF-119
    - INF-142
    - INF-647
  objective:
    - OBJ-373
  time: []
---

# Game: Thirsty Suitors

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Provoke a susceptible opponent into a temporary mood, use the extra
action to exploit it, and reconcile after winning the encounter.

## Analysis scope

- Version / ruleset: English PlayStation 5 commercial base release,
  Annapurna Interactive, 2 November 2023. The PlayStation Store lists
  PS5 and PS4 under the linked product. The principal recording uses
  PlayStation prompts. Its native console version and executable build
  are unverified. A second capture shows Xbox-style prompts.
- Structured analysis target: PLAT-PLAYSTATION-5 in
  [platform coverage](../../platforms/games.json).
- Entry: in Chapter 1, enter Home Skillet after the bus and accept
  the opening confrontation with Sergio. Begin at the introductory
  dialogue before Jala's first combat command.
- Primary decision loop: check HP, Will Power and the rival's
  mood. Use a basic attack to rebuild Will Power when needed. Time
  the prompts in the chosen action and in the rival's replies.
  Spend Will Power to try a taunt, then direct a matching skill
  at the newly susceptible target during the mood window.
- Positive terminal: defeat Sergio in his Inner World and accept
  Make Up. Finish at the results that follow the return to the diner.
- Included: prompted attack and defence, Will Power costs,
  temporary thirst and rage, the observed bonus action,
  skill-effectiveness labels and the separate reconciliation command.
- Excluded: the introductory quiz's stat allocation, alternative
  assist settings, later duels, favour quests, skating, cooking,
  exact damage formulas and behaviour after Jala loses.
- Potential scoped module: use Suitor Slam on comparable neutral
  and Thirsty targets, holding input grade and attack rank constant.
- Direct-play status: no personal hardware session, executable
  verification or captured inputs. The publisher and store establish
  release and the mood system. Two post-release visual traces
  corroborate the tutorial path. The primary trace displays PlayStation
  prompts. Exact hardware and assist settings are unverified.
  Footage was inspected in the background without audio.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| TS-001 | The English commercial PS5 base game was released 2 November 2023. Outerloop Games developed it. Annapurna Interactive is the publisher. Diner combat starts against Sergio after the bus introduction and continues into his Inner World. | Confirmed | Corroborated | High | P1, P2; W1 9:30–11:18 and 17:55–18:20; W2 16:08–16:45 |
| TS-002 | Jala sees personal HP and WP separately. The Attack description states that the basic attack reduces enemy HP and builds Will Power. Taunt and Skill list WP costs. The tutorial initially restricts commands. Later Attack, Taunt and Skill are shown together with a locked Items row. | Observation | Corroborated | High | W1 11:14, 15:02–15:18, 15:46, 20:44; W2 17:00 and 18:50 |
| TS-003 | On Be Mine, a contracting ring signals when to press cross to defend. One resolved example displays 10 blocked and 2 damage. The offensive prompt is separate and can be a repeated input or a timed press. Rage Side A displays an execution grade. | Observation | Corroborated | High | W1 12:09–12:36, 15:06–15:11, 15:50–15:55, 21:13–21:20; W2 11:00–11:24 and 13:28–13:34 |
| TS-004 | Jala selects Thirsty Taunt and spends 8 WP. Sergio acquires Thirsty for three turns in this trace. Bonus Turn is displayed and Jala can choose a follow-up before Sergio's next attack. | Observation | Corroborated | High | P2; W1 15:02–15:19 and 15:46; W2 13:18–13:50 |
| TS-005 | Suitor Slam costs 16 WP. Its description advertises greater damage against a Thirsty target and the skill and target both show Effective before confirmation. The trace shows 56 WP dropping to 40 WP and damage landing. The same skill is selectable outside that mood during the later observed battle. | Observation | Corroborated | High | W1 15:44–15:56 and 21:10; W2 13:48–14:02 and 22:06–22:17 |
| TS-006 | Later, Raging Taunt succeeds. The trace shows Raging with two turns, then the preview for Rage Side A marks Sergio as an effective target and shows a 20 WP cost. Thirst-specific Suitor Slam remains a separately listed option. | Observation | Corroborated | High | W1 20:48–21:23; W2 18:48–19:22 |
| TS-007 | Once Sergio is defeated, a Make Up command appears in the battle view, with an empty rival health bar. Accepting it leads to a separate exchange, a return to the diner and the rewards and level screen. | Observation | Corroborated | High | W1 23:25–24:20; W2 22:10–22:25 |

## Basic data

- Release / origin: Outerloop Games and Annapurna Interactive,
  PlayStation 5 commercial digital base game, 2 November 2023.
- Families: FAM-010 for live input windows inside the resolved
  combat action, and FAM-017 for the ordered dependency from
  taunt to active mood, matching skill and post-defeat settlement.
- P1: [PlayStation Store product UP2470-PPSA06878_00-THIRSTYSIEA00000](https://store.playstation.com/en-us/product/UP2470-PPSA06878_00-THIRSTYSIEA00000).
  Primary release listing, platforms, screen language, modes and description.
  Checked 2026-11-25.
- P2: [Annapurna Interactive product page](https://www.annapurna.com/interactive/thirsty-suitors).
  Publisher's description of turn-based narrative fights and mood-linked
  vulnerabilities. Checked 2026-11-25.
- W1: [Zoddronite, full gameplay](https://www.youtube.com/watch?v=UsyDo7rMRPY).
  Published 3 November 2023. English floor-to-results trace. Cross and L1/R1 prompts
  are visible at 12:24 and 15:46. PlayStation controller glyphs
  establish the observed control path. The video's multiplatform
  description does not identify the native console version.
- W2: [Stoic, part 1](https://www.youtube.com/watch?v=hJy0qF6v1Xo).
  Published 7 November 2023. Independent trace with Xbox-style prompts, used to
  corroborate shared mechanics. Exact build unverified.

### Reproducible fixture evidence

1. On the diner floor the Attack entry explains the basic strike's
   HP and WP effects. At 12:33–12:35 the blue cross prompt resolves
   against Be Mine. Two damage remains alongside the block amount.
2. At 15:03, Thirsty Taunt targets Sergio with 64 WP in Jala's
   reserve and two unknown weakness markers on the rival panel.
   The player sees a repeated square prompt. At about 15:19,
   the reserve reads 56 WP, the Thirsty timer shows three turns and
   Bonus Turn appears. Sergio stays available as the next target.
3. At 15:46 the Suitor Slam preview highlights effectiveness on the
   skill and target. The mood remains at three turns. A timed prompt
   occurs during the attack, then Jala has 40 WP and Sergio has less HP.
   The record does not estimate how much damage came from the mood
   versus the timing result.
4. The setting transforms to Sergio's Inner World without leaving
   the encounter. Around 21:07 Sergio is visibly Raging with two turns.
   At 21:10 Rage Side A is marked effective while Suitor Slam remains
   listed and unhighlighted. At 21:14 the execution displays Super.
5. At 23:29 the rival's health bar is empty, he is visibly defeated,
   and Make Up occupies a separate command panel. The following
   exchange returns to the diner, and rewards appear. W2 reaches
   the same post-defeat command along a different basic-attack route.

## Mechanical decomposition

### Action Genes

- ACT-222: execute the prompts inside a chosen taunt or strike.
- ACT-592: press at the indicated moment during Sergio's attack
  to reduce the incoming damage.
- ACT-930: choose and pay for the taunt that attempts to install a
  specific mood on the target.

### System Behaviour Genes

- SYS-358: grade inputs embedded in a chosen combat action and
  apply the action's execution-dependent result.
- SYS-1180: turn the prompted defensive press into damage reduction.
- SYS-2001: resolve a successful mood taunt into a temporary target
  state and an immediate bonus action.
- SYS-2002: increase a skill's effect when the current target mood
  matches its declared damage condition.

### Constraint Genes

- CON-351: fund the declared taunt or skill cost from Will Power.

### Information Genes

- INF-119: show Jala's health and Will Power as distinct reserves.
- INF-142: use the contracting ring and button prompt as timing cues.
- INF-647: show target mood, turns left and skill effectiveness
  before confirming the follow-up.

### Objective Genes

- OBJ-373: after the opponent is defeated, choose Make Up to close
  the duel and reach its rewards.

### Parameters

Current HP and WP, taunt cost, mood susceptibility, active mood,
remaining turns, follow-up cost, effectiveness marker, execution
grade, rival defeat and Make Up availability.

## Reproducible transitions

| Entry state | Input or event | Expected next state | Evidence |
| --- | --- | --- | --- |
| Sergio commits Be Mine | Press cross at the displayed defence window | Incoming damage can be partly blocked | TS-003 |
| Sergio is eligible and Jala has enough WP | Choose Thirsty Taunt and resolve the prompted input | Sergio becomes Thirsty for three displayed turns and Jala gains an immediate follow-up | TS-004 |
| Sergio is Thirsty and Jala has at least 16 WP | Preview and commit Suitor Slam | Effective before commitment, 16 WP consumed and the attack resolves with its applicable modifiers | TS-005 |
| Sergio has entered his Inner World | Land Raging Taunt and preview Rage Side A | A two-turn Raging state makes Rage Side A effective in the trace | TS-006 |
| Sergio is defeated | Choose Make Up | The reconciliation exchange and results follow | TS-007 |

## Strategic and experiential structure

A taunt creates a short-lived target state at a Will Power cost.
The immediate follow-up lets Jala exploit it before handing over
control. Reserve management, mood compatibility and execution
timing each affect the value of that plan. Make Up has its own
post-defeat interaction before battle rewards.

## Replay and variation

Both traces reproduce the early Thirsty follow-up and the separate
Make Up prompt. The captures differ in pacing and attack choices.
The displayed costs and durations here are scoped observations.

## Adjacent systems and history

The introductory quiz and in-battle dialogue belong to the story
framing. The observed encounter later offers Summon Mom. This ledger
does not generalize exact summons, resistances or the triggers for
phase transitions across different skills or releases.

## Normalised genome

- Action: ACT-222, ACT-592, ACT-930.
- System Behaviour: SYS-358, SYS-1180, SYS-2001, SYS-2002.
- Constraint: CON-351.
- Information: INF-119, INF-142, INF-647.
- Objective: OBJ-373.
- Time: none admitted.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `713` (`GAME-0001`–`GAME-0713`).
- Exact genome matches: none.
- Tied near matches: `GAME-0449` — Paper Mario (`5 / 22 = 0.227273`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Paper Mario (GAME-0449)](../m-r/paper-mario.md) | ACT-222, ACT-592, INF-142, SYS-1180, SYS-358 | Both duels add prompted execution to a chosen attack and a defensive press during the opponent's reply. Sergio's duel adds paid mood induction, an immediate bonus action for compatible damage and separate reconciliation after defeat. | Near, `0.227273`. |

## Taxonomy impact

Reuse timed offensive execution, reactive blocking, reserve gates,
HUD and timing cues. Admit mood selection, a bonus action on
successful mood induction, mood-matched damage, target preview,
and reconciliation after defeat.

## Negative results

- A mood-compatible marker is visible before selecting the target.
- Suitor Slam is still listed when Raging is the active mood.
- The reduced damage example leaves two damage. A timed block
  does not establish a full dodge or a counterattack.
- The first encounter has a separate interaction after defeat.
  No evidence here establishes the consequences of declining it.

## Delta summary

One deliberate action changes the opponent's mood and grants a
chance to act again. The following skill uses the newly active
condition with a separately graded execution. Defeat enables a
final reconciliation interaction.

## New facts

- The first Thirsty Taunt spends 8 WP and opens an immediate
  bonus action with three displayed turns of Thirsty.
- Suitor Slam lists a 16 WP cost and an effectiveness marker
  against that active mood.
- Make Up is visible as a separate command after Sergio's defeat.

## Principles and design implications

Give the player enough feedback to distinguish the induced state,
its duration and the matching action. Let an extra turn carry the
setup into a payoff. Make the terminal narrative choice separately
legible after the tactical success condition.

## Puzzle or game generation potential

Use a bounded duel with two temporary moods and one skill linked to
each. Let a successful taunt create a bonus action. Test that the
matching skill's damage preview changes with its target, and open an
explicit settlement action at the defeat boundary.

## New genes

- ACT-930
- INF-647
- OBJ-373
- SYS-2001
- SYS-2002

## New combinations

None.

## Taxonomy changes

[Taxonomy Change 460](../../../research/taxonomy-changes/TAXONOMY_CHANGE_460.md).

## New questions

- How do the two observed mood durations advance across a bonus
  action, an ordinary enemy turn and a scripted interruption?
- What is the isolated effect of a matching mood at a fixed grade?

## Next recommended game

Continue Selection 062 with Pushover, the original English Commodore
Amiga commercial floppy release. Trace the introductory domino
layout through trigger placement and the first accepted exit.

## Why this game

The first duel isolates a temporary target condition, an immediate
extra action, condition-matched skill damage and reconciliation.
