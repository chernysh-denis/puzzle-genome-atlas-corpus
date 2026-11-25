---
game_id: GAME-0691
slug: replaced
game_title: "REPLACED"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-223
    - ACT-295
    - ACT-429
  system:
    - SYS-045
    - SYS-215
    - SYS-736
  constraint:
    - CON-617
  information:
    - INF-268
    - INF-634
  objective:
    - OBJ-029
  time:
    - TIM-003
---

# Game: REPLACED

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
An authored fight teaches two responses to visible attacks before it
requires applying them in a live group encounter.

## Analysis scope

- Version / ruleset: commercial English Xbox Series X|S release,
  published April 14, 2026. W1 explicitly identifies Xbox Series X
  hardware. Its installed build, difficulty and remapping status
  were not independently verified. Use the English on-screen
  prompts and encounter sequence to identify the fixture.
- Structured analysis target: PLAT-XBOX-SERIES in
  [platform coverage](../../platforms/games.json).
- Entry: Chapter 1, Non-Standard Task, at the first Termite Dale
  fight just after the floor gives way in the brick hall. Start with
  the single opponent's dodge lesson.
- Primary decision loop: watch the opponent and the marker on the
  current attack, time the demonstrated defence, and follow the
  instruction's current success count. In the open fight, judge
  the spacing and next approaching opponent before committing an
  ordinary strike, dodge or counter.
- Positive terminal: defeat the remaining group in this room and
  reach ordinary controllable rightward traversal. Stop before
  opening the Survivor's Memoir.
- Failure and restart: a missed defensive input can leave a
  lesson uncredited or allow a hit during the live fight. The
  successful traces do not establish the exact restart anchor or
  what fields restore after a failed whole encounter.
- Included: lateral movement and spacing, red dodge and yellow
  counter-eligible markers, a strike command, staged instruction
  and accepted repetitions, autonomous attackers, the finite
  combat group and return to movement.
- Excluded: the prologue fight on the bridge, later firearm use,
  momentum and finishers as separate rules, precise defence
  windows and damage values, upgrades, collectibles, boss fights,
  later chapters, Windows builds, streamed play and later patches
  as distinct targets.
- Potential scoped module: reproduce a failed encounter in a
  recorded Xbox build and compare its restored lesson, position,
  opponents and health.
- Direct-play status: no personal Xbox play, build inspection or
  controller telemetry. W1 identifies Series X. W2 is a
  supplementary edited Hard run with unverified platform and
  build. Short background frame sequences were inspected without
  audio.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| RPL-001 | Xbox dates the commercial release to April 14, 2026. The Series X launch capture enters the first Termite Dale fight after a floor collapse. | Confirmed | Corroborated | High | P1, P2, W1 24:40–25:08 |
| RPL-002 | The first defender lesson shows B for dodging active enemy attacks. The attack itself carries a red marker tied to the attacking character. | Observation | Corroborated | High | W1 25:08–25:20, W2 23:25–23:36, H1 |
| RPL-003 | The next lesson shows Y for countering yellow-marked attacks. W1 shows 0/3 at 25:21 and 2/3 around 25:27–25:30, followed by the strike lesson. H1 independently describes dodge for red and counter eligibility for yellow. | Observation | Corroborated | High | W1 25:21–25:33, W2 23:36–23:48, H1 |
| RPL-004 | The ordinary strike lesson displays X and persists into a demand to defeat the first enemy. Other attackers enter only after that opponent is dealt with in the demonstrated sequence. | Observation | Corroborated | High | W1 25:33–25:56, W2 23:47–24:02 |
| RPL-005 | In the open exchange multiple opponents move, attack and can be defeated while the player acts. After the last active hostile stops, rightward traversal resumes before the optional memo. | Observation | Corroborated | High | W1 25:53–26:26, W2 23:59–24:43, H1 |

## Basic data

- Release / origin: Sad Cat Studios and Thunderful Publishing,
  Xbox Series X|S, April 14, 2026.
- Mechanical families: FAM-009 for response and position against
  visible hostile preparation; FAM-010 for live opponents that
  continue moving while the player decides.
- P1: [Xbox store listing](https://www.xbox.com/en-US/games/store/replaced/9NV3L234VGXD).
  Identifies product 9NV3L234VGXD, commercial date, developer and
  Xbox Series X|S support.
- P2: [Director Yura Zhdanovich's Xbox Wire account](https://news.xbox.com/en-us/2026/04/14/replaced-combat/).
  Confirms release availability and explains the broader attack,
  dodge and counter design. The later systems are outside this fixture.
- W1: [That Gaming Fella's launch-day Series X capture](https://www.youtube.com/watch?v=DGT7lbLn8ik&t=1480s).
  Inspect 24:40–26:26 for the entry, instruction counts, group
  engagement and first rightward movement after the fight.
- W2: [NeatPick's Hard walkthrough](https://www.youtube.com/watch?v=A70ZdBBBre0&t=1405s).
  Inspect 23:25–24:43 for the same lesson order and group
  clearance. The author discloses a review key and edited deaths.
  It corroborates the visible order without establishing Series X
  equivalence or unedited failure recovery.
- H1: [GamesHorizon's first-chapter walkthrough](https://gameshorizon.com/guides/replaced-chapter-1-full-walkthrough-all-collectibles/).
  Locates the training after the floor collapses, describes the
  two cue classes and places the first memoir after the fight.
- Claim IDs: RPL-001–RPL-005.

### Reproducible fixture evidence

1. Enter the first Termite Dale room. W1 shows the collapse and
   recovery around 24:40. Near 25:08 the dodge lesson starts at
   a live opponent. Match the B prompt and the local red marker.
2. Around 25:21 inspect the Y prompt and yellow-counter count.
   Around 25:27–25:30 the count displays 2/3 and the cue is
   again visible. Satisfy the drill and check that the next
   authored instruction is for an ordinary strike.
3. At 25:33–25:50 follow the X prompt through the first
   opponent's defeat. At about 25:53–25:56 other hostiles enter
   the active floor and individual instruction text clears.
4. At 25:56–26:17 follow the remaining opponents as they close
   and fall. By 26:20–26:26 the character moves to the right
   side with no active rival. Stop before opening the memoir.

## Mechanical decomposition

### Action Genes

- ACT-008: steer the controlled character across the floor and
  resume ordinary horizontal movement when the fight clears.
  RPL-001, RPL-005.
- ACT-223: time a manual dodge within a live telegraphed attack.
  RPL-002.
- ACT-295: commit an ordinary direct strike. The X instruction
  makes the input explicit. RPL-004.
- ACT-429: commit the reactive counter within its visible yellow
  opportunity. RPL-003.

### System Behaviour Genes

- SYS-045: opponents advance and shift their location while the
  player prepares a response. RPL-004–RPL-005.
- SYS-215: direct real-time commands resolve strikes, defence
  and defeat against live opponents. RPL-002–RPL-005.
- SYS-736: the active lesson advances after the required actions
  are credited. Individual teaching hands off to the group fight.
  RPL-002–RPL-005.

### Constraint Genes

- CON-617: the marked attack class determines whether the
  counter is eligible. Red calls for a dodge. RPL-002–RPL-003.

### Information Genes

- INF-268: the current instruction displays the relevant input and
  reports progress, including a required counter count. RPL-002–RPL-004.
- INF-634: the individual attacker carries a transient warning
  whose class communicates its defensive eligibility. RPL-002–RPL-003.

### Objective Genes

- OBJ-029: defeat the authored finite group to end the room
  encounter. RPL-004–RPL-005.

### Time Genes

- TIM-003: choose defensive and ordinary attacks while the
  hostiles continue to move and advance their strikes. RPL-002–RPL-005.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| One opponent in the dodge lesson | Time a dodge on the red-marked attack | Credited defence and continued lesson flow | RPL-002 |
| Yellow-counter lesson with a live cue | Execute the eligible counter in time | Updated counter progress; completion exposes strike instruction | RPL-003–RPL-004 |
| Strike lesson with the first opponent active | Land ordinary attacks until the current opponent is defeated | Instruction clears and other hostiles join the floor | RPL-004 |
| Several opponents active in the hall | Move, select a defence or attack and defeat those still active | Ordinary rightward traversal resumes | RPL-005 |

## Strategic and experiential structure

The cue identifies whose attack is imminent and how it can be
answered. Teaching isolates each response before the live group
requires reading different attackers while judging movement and
strike opportunities. The counter count teaches a success predicate
separate from the later room-clear condition.

## Replay and variation

The two recordings differ in the pace and positions of the group
exchange. They agree on the order of the lessons and ordinary
movement after clearance. The edited Hard trace does not show which
states survive an encounter loss.

## Adjacent systems and history

The developer describes Arkham's rhythmic combat as an influence.
Later attacks, equipment and collectibles have distinct rules.
The first Termite Dale room isolates colour-marked defence and
follows a separately excluded prologue encounter.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-223, ACT-295, ACT-429 | Lateral steering, dodge, directed strike and cued counter |
| System Behaviour | SYS-045, SYS-215, SYS-736 | Live opponents, contact resolution and lesson gates |
| Constraint | CON-617 | Counter requires an eligible incoming attack |
| Information | INF-268, INF-634 | Instruction and success count; attacker-specific defence cues |
| Objective | OBJ-029 | Clear the finite hostile group |
| Time | TIM-003 | Intervene as the attacks progress |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `690` (`GAME-0001`–`GAME-0690`).
- Exact genome matches: none.
- Tied near matches: `GAME-0277` — Cuphead (`6 / 20 = 0.300000`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Cuphead (GAME-0277)](../a-f/cuphead.md) | ACT-008, ACT-223, CON-617, OBJ-029, SYS-215, TIM-003 | Both use timed movement and class-based defence to resolve a finite threat. Cuphead uses pink-object parries and sustained projectile pressure. REPLACED distinguishes dodge and counter cues on a close attacker and reveals separate lessons before the group. | Near, `0.300000` |

## Taxonomy impact

Keep the active defence constraint separate from its display.
INF-310 exposes a counter opportunity with a local cue. INF-634
applies where separate markers distinguish alternative defensive
responses to the same class of ordinary live encounters. The
tutorial instruction is a separate surface.

## Negative results

- The counter target count is a tutorial gate, not a condition
  on every later ordinary exchange.
- The cue reveals eligibility; it does not establish exact active frames.
- The optional memoir lies outside the room-clear terminal.
- The two successful traces do not establish a restart anchor,
  damage values or parity between difficulty settings.

## Delta summary

Twelve genes, with one new informational boundary for the
contrast between the two defensive cues.

## New facts

- The marker is attached to the attacker and encodes response class.
- The taught counter count must resolve before the strike prompt.
- The authored room separates practice against one opponent from
  ordinary combat against the remaining group.

## Principles and design implications

Rehearsing an isolated visual distinction before a live group
keeps interpretation and execution separately observable. A
visible cue can disclose which response is possible without
automating its timing.

## Puzzle or game generation potential

Prototype a fictional clockwork arena with two visible advance
signals. Let players rehearse one movement response and one
interrupt response, then alternate both signals in a short trial.

## New genes

- INF-634

## New combinations

None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 437](../../../research/taxonomy-changes/TAXONOMY_CHANGE_437.md).

## New questions

- What checkpoint fields restore after a failed whole encounter on Xbox?
- Do later red and yellow cues use the same timing under specific accessibility changes?

## Next recommended game

Continue Selection 059 with `GAME-0692`, Klonoa 2: Lunatea's Veil
on the original North American PlayStation 2 release.

## Why this game

The first fight puts response eligibility, explicit counter
practice and mixed live timing into one short fixture.
