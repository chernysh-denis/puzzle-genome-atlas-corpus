---
game_id: GAME-0734
slug: nex-machina
game_title: "Nex Machina"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-810
  system:
    - SYS-037
    - SYS-045
    - SYS-2043
    - SYS-2044
    - SYS-2045
  constraint: []
  information:
    - INF-179
    - INF-662
  objective:
    - OBJ-007
  time:
    - TIM-003
---

# Game: Nex Machina — Techno Forest 1-1 in Arcade

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The opening robots, secret human and settlement rings are instances
of the scoped enemy, rescue and closeout rules.

## Analysis scope

- Version / ruleset: English Windows Steam commercial base game,
  app 404540, Housemarque's v1.05 gameplay rules, solo Arcade on
  Experienced. The lead replay shows v1.05. Housemarque specifies
  gameplay and content parity for v1.05 across the supported
  storefronts and PS4. The replay's platform and native Steam
  files were not independently fingerprinted.
- Reproducible entry and exit: from Arcade choose Techno Forest
  on Experienced. Enter 1-1 after the opening arrival. Stop
  on first control in 1-2, before clearing its targets or taking
  its pickups. Retained score and the rescue marker can be read
  at the transition.
- Primary decision loop: move through the small arena while
  directing a separate stream of shots, decide when to stop
  thinning robots and expose and save the hidden human, then
  clear the final marked threat and optionally time the end dash.
- Included: direct movement, independent directional fire,
  local robot motion, breakable cover, contact rescue, last-threat
  highlight, hostile clearance and the timed dash and deathless
  score awards. Excluded: combat dash protection classes and
  measured cooldowns, harvesting patterns in later rooms,
  rescue-chain renewal after further rescues, later worlds,
  weapons and upgrades, continues, co-op, Single World and
  the separate online Arena challenges.
- Direct-play status: no personal Windows or console session.
  Steam and Housemarque establish the commercial release and
  v1.05 parity. The Experienced replay anchors the positive
  opening. Two Windows routes corroborate the basic handoff.
  Only silent background frames were inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| NM-001 | Housemarque released Nex Machina for Windows Steam on June 20, 2017. The scoped v1.05 gameplay and content are documented as equivalent across Steam, GOG, Humble Store and PS4. | Observation | Corroborated | High | P1, P2, P3, W1 00:08–00:11 |
| NM-002 | From the first controllable arena, the player moves while firing a repeated stream in an independently chosen direction. Robots keep moving while the player changes position and fire direction. | Observation | Corroborated | High | P1, P2, S2, W1 00:15–00:18, W2 03:47–03:50 |
| NM-003 | Breaking eligible foliage on the northeast side reveals a green human in 1-1. Reaching the exposed human credits the rescue separately from breaking its cover. W1 displays a first Human Combo mark and first Secret Human credit while 1-1 is still live. | Observation | Corroborated | High | P1, W1 00:16–00:19, S1 |
| NM-004 | The last required robot is highlighted magenta while the room remains active. Resolving that target triggers the closing ring sequence and the automatic handoff. A Windows Rookie route reaches 1-2 without saving the hidden human. | Observation | Corroborated | High | W1 00:18–00:21, W2 03:49–03:54, W3 00:06–00:10, S1 |
| NM-005 | After clearance a large ring closes on the smaller one at the player. An end dash at coincidence earns a separate award. W1 displays the successful dash and credits 1,000 points in that trace. Both Windows contrast routes advance without the successful-dash credit. | Observation | Corroborated | High | P4 tip 7, W1 00:19–00:21, W2 03:50–03:54, W3 00:06–00:10 |
| NM-006 | At 1-1 settlement a no-death clear credits 10,000 independently of the end dash. The W1 score rises from 6,430 to 17,430 with both awards. W2 and W3 show the no-death award and the same numbered handoff. | Observation | Corroborated | High | W1 00:19–00:21, W2 03:50–03:54, W3 00:06–00:10 |
| NM-007 | The accumulated score carries through the transition. The rescue mark and live Human Combo meter are still visible at 1-2 entry in W1. The route ends before the next rescue, so no later chain-renewal values are used. | Observation | Corroborated | High | P4 tip 4, W1 00:20–00:21.5, W2 03:52–03:54 |

## Basic data

- Release / origin: Housemarque, June 20, 2017, Steam app 404540.
  The analysis target is `PLAT-WINDOWS-PC`.
- Mechanical family: `FAM-010` for independently directed live
  fire, autonomous threats, the rescue opportunity and the brief
  timing window at a forced handoff.
- Primary evidence checked 2026-11-25:
  - **P1:** [Nex Machina on Steam](https://store.steampowered.com/app/404540/Nex_Machina/).
    The official Windows product, date, twin-stick description and
    optional secret humans.
  - **P2:** [Housemarque's release announcement](https://housemarque.com/news/nex-machina-from-housemarque-is-finally-here).
    Confirms the PC release, solo arcade campaign, Techno Forest
    opening and parallel rescue and survival decisions.
  - **P3:** [Housemarque's v1.05 Steam patch notes](https://store.steampowered.com/news/posts/?appids=404540&enddate=1509544438).
    The July 6 balance and July 17 hotfix entries identify the
    ruleset and storefront parity. Exact replay sub-build and
    live Steam depot state are not inferred.
  - **P4:** [Jonas Elfving's tips on PlayStation Blog](https://blog.playstation.com/archive/2017/07/06/10-expert-tips-for-dying-slightly-less-frequently-in-housemarques-brutal-ps4-shooter-nex-machina).
    The release-window PlayStation account of human combo retention
    and distinct convergence timing after the level clears.
- Recorded and independent evidence:
  - **W1:** [CRI's Experienced Arcade replay](https://www.youtube.com/watch?v=WaYY8QxHnoo&t=8s).
    The displayed run is dated July 17, 2017. Around 00:16–00:19
    foliage breaks, a green subject appears, and contact registers
    Secret Human 1/5. Around 00:19–00:21 the marked threat resolves,
    rings close and both scoring awards appear. The player enters
    1-2 with the rescue indicator still present.
  - **W2:** [GaminGHD's Windows Arcade start](https://www.youtube.com/watch?v=f2RwqHW2QPg&t=173s).
    The Arcade choice appears around 02:53 and Rookie is selected
    around 03:41. At 03:47–03:54 the player clears 1-1 and reaches
    1-2 without the secret rescue or the timed dash award. The
    description points to GOG. Use it as a contrast, not as an
    Experienced score or a Steam-specific binary record.
  - **W3:** [Father's Steam Windows gameplay](https://www.youtube.com/watch?v=iRGGTBwKiKM).
    At 00:03–00:10 the same opening tile cluster and transition
    are visible. The recording starts after mode selection.
  - **S1:** [Mogg1342's Techno Forest walkthrough](https://www.supercheats.com/nex-machina/walkthrough/world-01-techno-forest),
    1-1. Locates the foliage and identifies the final-target cue.
  - **S2:** [DarkZero's contemporary Windows play report](https://darkzero.co.uk/game-reviews/nex-machina-pc/).
    Separates analog movement, firing direction and the dash.
- Claim IDs: NM-001–NM-007. Use the visible stage indicator
  and separate rescue and settlement messages as boundaries.
  No frame-perfect input window or harvest rate was extracted.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: move the controlled body through the arena toward the cover or away from a robot (NM-002, NM-003).
- Reuse `ACT-810`: fire a repeated directional stream independently of the movement direction (NM-002).

### System Behaviour Genes

- Reuse `SYS-037`: touching the revealed human marks the rescue and credits score while the arena remains active (NM-003).
- Reuse `SYS-045`: active enemies change position on the running field without player commands (NM-002).
- New `SYS-2043`: destroy authored cover to reveal a separate, uncredited rescue subject (NM-003).
- New `SYS-2044`: judge a dash at the closing ring alignment as an optional transition award (NM-005).
- New `SYS-2045`: credit a deathless arena clear separately from the timed dash (NM-006).

### Constraint Genes

No separate constraint is admitted. The rescue must precede the
handoff to count for this room. The dash window is part of its
award rule.

### Information Genes

- Reuse `INF-179`: the visible room shows the body, robots, cover and the revealed human (NM-002, NM-003).
- New `INF-662`: highlight the final required hostile as a warning that its defeat will close the arena (NM-004).

### Objective Genes

- Reuse `OBJ-007`: defeat the required robots to settle 1-1 and automatically progress to 1-2 (NM-004, NM-006).

### Time Genes

- Reuse `TIM-003`: while move and fire are available the robots and projectiles continue to move, and the closeout window advances on its own (NM-002, NM-005).

## Formal state and transitions

Track the player's position and firing direction, required hostile
set, authored cover and human state, current score, death history
for the arena and transition phase. Breaking the cover moves the
human from hidden to exposed without credit. Contact marks it
rescued. A last-target cue marks the final outstanding hostile.
Its removal advances the closeout regardless of rescue credit.
The ring judges a transient dash input and the deathless award
reads the arena's death history. After settlement the next arena
starts with the score and eligible rescue-chain progress retained.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Control in 1-1 with active robots | Move while keeping fire on a different direction | Body and shot stream follow distinct command directions while foes advance | NM-002 |
| Secret human still covered | Shoot the relevant foliage without clearing the last robot | Expose the separate human, which can then be reached | NM-003 |
| Human exposed and 1-1 active | Move into the human | Credit the rescue before settlement | NM-003 |
| One required robot remains and is highlighted | Eliminate it | Start automatic closeout and the converging ring cue | NM-004, NM-005 |
| Outer ring meets the smaller ring | Dash at the timing cue | Earn the independent successful-dash award | NM-005 |
| Deathless arena has cleared | Let settlement finish | Credit the no-death award and begin 1-2, whether or not the timing award was earned | NM-005–NM-007 |

## Strategic and experiential structure

The final highlighted robot gives the player a decision about
when to close the room. Saving the human requires a detour
before that clearance. The transition offers a second brief
input test for bonus points even though the combat objective
has already been settled.

## Replay and variation

The Experienced replay rescues one secret human and times the
exit dash. The Windows Rookie contrast fires through the required
robots and leaves without those credits. Both illustrate the
auto-advance predicate, while exact shot counts and bonus
parameters are kept with their observed ruleset.

## Adjacent systems and history

Housemarque distinguishes continued human chains, world time
bonuses, upgrades and other scoring events. This opening records
only the chain's start and retained display on first arriving in
1-2. It does not admit the subsequent credit accumulation or
the world result.

## Normalised genome

- Action: ACT-008, ACT-810.
- System Behaviour: SYS-037, SYS-045, SYS-2043, SYS-2044, SYS-2045.
- Constraint: none.
- Information: INF-179, INF-662.
- Objective: OBJ-007.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `733` (`GAME-0001`–`GAME-0733`).
- Exact genome matches: none.
- Tied near matches: `GAME-0387` — Super Bomberman (`6 / 19 = 0.315789`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Super Bomberman (GAME-0387)](../s-z/super-bomberman.md) | ACT-008, INF-179, OBJ-007, SYS-037, SYS-045, TIM-003 | Both show a live enclosure, moving enemies and separate contact credit for pickups. Super Bomberman commits a fuse-driven bomb and needs a safe route away from its blast before reaching the exposed exit. Nex Machina fires while moving, weighs an optional rescue against killing the final robot and transitions automatically. | Near, `0.315789`. |

## Taxonomy impact

Keep the cover's destruction separate from collecting its subject.
The room clear uses a hostile set, while the end dash and
deathless awards are independent score outcomes. The final-target
marker communicates a pending irreversible phase change.

## Negative results

- The secret human can be revealed before rescue credit appears.
- The Windows Rookie trace reaches 1-2 without a secret rescue.
- Missing the end dash does not block the next arena.

## Delta summary

Record one early top-down arena with independent movement and fire,
optional reveal-and-rescue, a last-target cue and two separate
closeout scores.

## New facts

- The last required threat can be identified before clearing the room.
- The optional rescue advances its own credit while combat continues.
- Dash timing and deathless clearance settle independently.

## Principles and design implications

Use the last-target cue to make imminent phase closure legible.
Let optional score routes compete with safe removal of enemies.
An extra timing decision at the handoff can reward execution
while leaving the main clearance predicate stable.

## Puzzle or game generation potential

Build a small real-time arena with one optional rescue hidden
behind destructible cover and a finite hostile set. Explicitly
test clear alone, reveal without rescue, rescue then clear and
timed versus ordinary closeout as different sequences.

## New genes

- SYS-2043
- SYS-2044
- SYS-2045
- INF-662

## New combinations

None. No verified combination is a proper subset of the signature.

## Taxonomy changes

[Taxonomy Change 480](../../../research/taxonomy-changes/TAXONOMY_CHANGE_480.md).

## Next recommended game

Toki Tori on the North American Game Boy Color cartridge is the next Selection 064 unit.

## Why this game

The player balances two concurrent directions and two independent
routes to score. The last hostile ends the opportunity to rescue,
but creates a separate timing decision before the next fight.

## Review status

Reviewed 2026-11-25 for the Windows Steam commercial v1.05 Arcade
opening through first control in Techno Forest 1-2.
