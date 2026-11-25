---
game_id: GAME-0697
slug: radiant-silvergun
game_title: "Radiant Silvergun"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-161
    - ACT-562
    - ACT-917
  system:
    - SYS-215
    - SYS-911
    - SYS-1410
    - SYS-1974
    - SYS-1975
    - SYS-1976
    - SYS-1977
  constraint: []
  information:
    - INF-235
    - INF-636
  objective:
    - OBJ-002
    - OBJ-288
  time:
    - TIM-003
---

# Game: Radiant Silvergun

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
An early flight passage makes enemy colour relevant to the event order,
while the firing command determines which targets are likely to be hit
and where the earned weapon experience goes.

## Analysis scope

- Version / ruleset: Treasure / ESP's original Japanese commercial
  Sega Saturn disc T-32902G, July 23, 1998. One solo pilot in Saturn
  Mode, with the original chain rules. Start a fresh Game Start
  with baseline weapon levels. W1 declares Easy, original chains,
  the second ship and remapped controls. W2 shows the first ship,
  the same route and the same closeout. Its difficulty, capture
  hardware and use of saved states are unverified. The two routes
  establish the transition structure, not a common wave schedule.
- Structured analysis target: PLAT-SEGA-SATURN in
  [platform coverage](../../platforms/games.json).
- Entry: use the Saturn rules and start a new game without Save Start.
  At first ship control in Stage 3A, verify the stage label, empty score
  and initial level. Use W1's declared Easy settings for its branch.
- Primary decision loop: move the ship to aim an immediately available
  weapon and avoid fire. Choose a firing pattern that strikes the intended
  colour while letting other ships pass. Complete a same-colour group or
  deliberately route the secret branch. Watch the local bonus, weapon
  progression and sword reserve. Preserve useful targeting during AKA-O's
  rotations and destroy side components before its core when pursuing the
  full destruction award.
- Positive terminal: destroy AKA-O, read the report's independent awards
  and regain ordinary control at the opening of Stage 3B. Both witnesses
  show the version with a perfect destruction-rate bonus. The optional
  chain score and perfect award do not define the stage transition.
- Other ends: a hit can cost one ship; exhaustion ends the attempt as
  described in the manual. A boss self-destruction can close out without
  the direct destruction award according to the guide. Neither a
  stock-exhausting failure nor an AKA-O timeout was replayed here.
- Included: bounded two-axis placement on the scrolling course,
  authored arrival of visible colour groups, real-time shots and
  evasion, direct single and combined attacks, enemy and projectile
  classes, sword charging and use, original chain and secret-chain
  observations, weapon growth, life reserve, AKA-O component order
  and report, and the move to 3B.
- Excluded: the Arcade route and arcade ST-V hardware, other ports
  and their alternate rules, patched controls, multiplayer play,
  continuing after stock depletion, saving and importing levels,
  hidden dogs, exact grazing and weapon-bonus formulas, extended
  scoring routes and the playable content of 3B and later stages.
- Potential scoped module: trace continuity of the weapon levels
  from game over through an explicitly selected Save Start.
- Direct-play status: no personal Saturn session, disc inspection or
  controller telemetry. The surviving manual and Sega release index
  establish the edition and controls. Two separately uploaded
  Saturn Mode runs were inspected in silent short frame sequences.
  W1 documents a remapped controller. W2's collection warns that
  some captures use save states; exact capture binaries are unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| RSG-001 | Sega identifies the July 23, 1998 original Japanese release as Treasure / ESP T-32902G. The disc's Game Start and Save Start are separate choices. | Confirmed | Direct | High | P1; P2 pp. 6–9 |
| RSG-002 | The controller moves the ship. Three base buttons and their pairs or triple select seven immediate attack patterns. Saturn supplies shortcuts and remapping. | Confirmed | Direct | High | P2 pp. 4–5, 8–10; P3 for design context; W1 0:56–0:58, 1:09–1:10; W2 6:25–6:28 |
| RSG-003 | The scrolling stage and local waves advance independently of the ship's two-axis steering. A concentrated forward shot reaches the left red flight while blue craft pass to its right. | Observation | Corroborated | High | P2 pp. 4, 10; W2 6:09–6:31; W1 1:01–1:14 |
| RSG-004 | The original chain credits consecutive same-colour trios. Continued groups increase the award. The documented secret red-to-one-blue-to-yellow route changes the chain state. W1 shows a secret award over a yellow kill; its entire input sequence is not reconstructed frame by frame. | Observation | Corroborated | Medium | P2 p. 12; W2 6:25–6:28; W1 0:55–0:58 and 1:09–1:11; S1 |
| RSG-005 | Defeats give experience to the base weapon used. A combination apportions experience to its constituent base weapons. The separate sword gauge is filled by absorbing eligible pink projectiles. With a full gauge the same sword command launches a stronger temporary attack. | Observation | Corroborated | High | P2 pp. 4–5, 10–11; W1 0:56–0:59 and 1:33–1:35; W2 6:59–7:04 |
| RSG-006 | The manual identifies score, weapon level and ship stock, and documents loss of a ship on damaging contact. W1 and W2 retain displayed stock in the observed encounter. | Confirmed | Corroborated | High | P2 pp. 10–11; W1 0:55–1:57; W2 6:09–7:19 |
| RSG-007 | AKA-O rotates and exposes separate destructible sections. Defeating its core settles the encounter; extra part destruction increases the rate award. Both records show Perfect, 5,000 for destruction and 100,000 for rate before the stage hands off. | Observation | Corroborated | Medium | P2 p. 12; W1 1:28–2:01; W2 6:49–7:19; S1 |
| RSG-008 | Local chain notices and the boss report denote different awards. W1 scores 196,350 before the report is applied and 301,350 after both boss lines settle. | Observation | Direct | High | W1 1:49–2:01; W2 7:15–7:18 corroborates the same line values |

## Basic data

- Release / origin: Japanese Sega Saturn, Treasure / ESP, 1998.
- Mechanical families: FAM-004 for matching a specific destruction colour
  across an ordered group; FAM-010 for decisions under real-time arrivals.
- P1: [Sega's official Saturn licensed-software catalogue](https://www.sega.jp/fb/segahard/ss/soft_licensee4.html).
  Release date, company and Japanese disc code.
- P2: [Original Japanese retail manual](https://archive.org/details/Radiant_Silvergun_1998_ESP_JP/mode/2up).
  Printed pp. 4–5, 6–11 and 12–13 cover controls, options, starting and
  save-start rules, live state, weapon progression and bonuses.
- P3: [Contemporary developer interview translated from Gamest](https://shmuplations.com/radiantsilvergun/).
  Pre-release arcade design context for simultaneous inputs, no weapon
  pickups, and the choice to read and avoid bullets. P2 governs Saturn.
- W1: [Sei-Dragon's Saturn Mode original-chain run](https://www.youtube.com/watch?v=5SC0eAWxXRA&t=55s).
  Describes settings, remapped controller and subtitles. Shows the secret
  route and the boss closeout with the second player's craft in solo play.
- W2: [Tsunao's Japanese Saturn Mode route](https://www.youtube.com/watch?v=Wue0F5YyeEQ&t=369s).
  Begins in Saturn Mode. Shows ordinary chains and the same opening closeout.
  The uploader warns that many longplays use save states.
- S1: [NMetatron's original Saturn guide](https://gamefaqs.gamespot.com/saturn/198389-radiant-silvergun/faqs/5252).
  Corroborates the secret entry recipe, the distinction between core and
  parts, and the direct defeat versus timeout award. Do not use it for
  an exact, universal chain formula.
- Claim IDs: RSG-001–RSG-008.

### Reproducible fixture evidence

1. Set Game Mode to Saturn and select Game Start. The supported new run
   begins at zero score and weapon level. W2 shows the 3A label at 6:09.
   W1 declares an Easy run. Avoid inferring that W2 uses the same setting.
2. Steer without passing control to a different pilot. Choose the narrow
   forward Vulcan shot for a line of intended targets. At 6:26 W2 destroys
   part of the red wave on the left and shows Chain 120 at score 390.
   At 6:27 it shows Chain 480 at score 990 while blue craft remain on the
   right. These are observed awards, not universal opening values.
3. The alternate W1 path shows Secret 10,000 at 0:56.5 over the yellow
   targets and Chain 10,000 at 0:57. At 1:10 a narrow orange forward shot
   through the left group displays Chain 20,000 and Chain 30,000 while
   blue ships are still present. Use the documented recipe and these
   observable checkpoints without assuming the same chain in W2.
4. Compare the blade near the pink bullets at 0:56–0:58 with the larger
   two-blade effect near 1:34 in W1. The manual maps ordinary sword and
   charged sword to the same input. Read the charge and weapon level
   separately. The capture alone cannot recover the precise press or
   division of weapon experience among base types.
5. After the warning, attack AKA-O as it changes orientation. The first
   distinct components burn before the main explosion around 1:40 in W1
   and 7:06 in W2. The documented completion check concerns the core;
   separate pieces influence the report's rate.
6. Before 3B, read the 5,000 destruction bonus and 100,000 perfect rate
   bonus. W2 displays both at 7:18. W1's score rises from 196,350 to
   301,350 across the report and its 3B label appears near 1:58.
   Stop after the initial return of active control in 3B.

## Mechanical decomposition

### Action Genes

- ACT-161: line up the current shot on one intended enemy or boss part.
- ACT-562: steer in two screen axes as the route advances separately.
- ACT-917: issue one base, combined or shortcut command to immediately
  produce the associated attack pattern without an intervening equip step.

### System Behaviour Genes

- SYS-215: resolve the active ship, shots, opposing bodies and eligible
  damage during the same live interval.
- SYS-911: on a lethal hit documented by the manual, spend one finite
  ship and restore a controllable craft while stock remains.
- SYS-1410: carry the ship through the fixed authored stage corridor and
  effects independently of its local aiming position.
- SYS-1974: credit same-colour groups in enemy destruction order and, on
  the evidenced special entry, advance a distinct chain progression.
- SYS-1975: credit earned experience to the producing base weapon or
  divide it among the base weapons of a combined attack.
- SYS-1976: absorb the permitted projectile class with the blade
  and let the full reserve convert the next sword command.
- SYS-1977: settle direct core destruction and the completeness of
  part destruction in separately computed bonus lines.

### Constraint Genes

No separate new predicate. Fixed bounds are part of flight control
and exposure. The colour rule belongs to chain settlement, and the
sword eligibility belongs to the charge transition. Counting them
twice would create duplicate signature boundaries.

### Information Genes

- INF-235: observe local target colours, attack trajectories, part
  exposure and available gaps on the visible region of the stage.
- INF-636: read the continuing score, weapon level and sword charge
  and distinguish transient event awards from the finite ship reserve.

### Objective Genes

- OBJ-002: improve the continuing numerical score through choices of
  target order and part destruction.
- OBJ-288: complete the local flight episode by defeating the boss,
  accepting its closeout and reaching the next active stage.

### Time Genes

- TIM-003: choose and fire while the authored formation progresses.
  A target can pass out of useful firing position during deliberation.

### Parameters

Weapon patterns, enemy colour and order, local reach, life stock,
experience attribution, charge, part identities and settlement lines
are fixture values rather than additional genes.

## Reproducible transitions

| Entry state | Action or event | Expected next state | Evidence |
| --- | --- | --- | --- |
| 3A begins, zero displayed score and initial level | Steer into the left flight and fire forward | Narrow fire reaches selected craft independently of blue targets | RSG-002–RSG-003, W2 6:09–6:28 |
| Compatible coloured defeats accumulated | Destroy another target completing the group | A distinct chain credit appears, separate from ordinary destruction points | RSG-004, W2 6:26–6:27 |
| Secret opening route | Destroy the yellow target after eligible prior colours | W1 displays Secret 10,000 before repeated chain awards | RSG-004, W1 0:56–0:57 |
| Sword available and eligible projectile approaches | Contact it with the ordinary blade; use the sword again at full charge | Gauge rises on valid absorption, and the full-gauge command gives the alternate attack | RSG-005, P2 pp. 4–5 and W1 0:56–0:58, 1:33–1:35 |
| AKA-O active with separately destructible pieces | Destroy parts before finishing its core | Two independent bonus lines are reported, then 3B begins | RSG-007–RSG-008, W1 1:28–2:01 and W2 6:49–7:18 |

## Strategic and experiential structure

The attack that destroys the most ships also risks ending the desired
colour sequence. Place the narrow shot so that a mixed wave offers
two parallel opportunities: enough targets to continue its chain and
a route through the projectiles. At the boss, damaging the core
earlier can secure completion at the cost of a perfect rate.

## Replay and variation

Use fresh weapon levels and the same mode for a replay. Watch the
visible outcome and preserve the selected difficulty and ship setting.
Other weapons, target orders and damage timing are legitimate routes.
W1 and W2 demonstrate different awards before the same report structure.

## Adjacent systems and history

The Japanese retail disc includes Arcade Mode and Saturn Mode. Later
ports, saves carrying previous shot levels, score extends, multi-pilot
play and later stages offer independent analysis questions. None
supplies a mechanic to this signature through a version assumption.

## Normalised genome

- Action: ACT-161, ACT-562, ACT-917.
- System Behaviour: SYS-215, SYS-911, SYS-1410, SYS-1974,
  SYS-1975, SYS-1976, SYS-1977.
- Constraint: none.
- Information: INF-235, INF-636.
- Objective: OBJ-002, OBJ-288.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `696` (`GAME-0001`–`GAME-0696`).
- Exact genome matches: none.
- Tied near matches: `GAME-0650` — Einhänder (`7 / 23 = 0.304348`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Einhänder (GAME-0650)](../a-f/einhander.md) | ACT-161, ACT-562, OBJ-002, OBJ-288, SYS-1410, SYS-215, TIM-003 | Both use bounded steering on a forced flight route, with live targeting and a credited boss handoff. Einhänder claims and switches recoverable live weapons. Radiant Silvergun makes attack forms available through combined inputs from the start, credits ordered enemy colours, distributes experience to participating weapon types and separates core defeat from the completeness of part destruction. | Near, `0.304348`. |

## Taxonomy impact

Retain the existing forced-flight placement, live damage, life-stock
and successor boundaries. Introduce distinct weapon-command composition,
colour-order settlement, attributed growth, absorption-driven sword
conversion, boss part accounting and live evidence cues.

## Negative results

- A shortcut invokes the combined attack directly. The player does not
  need to cycle or pick up a weapon before the shot.
- Enemy hull colour used for chains is distinct from the eligible pink
  projectile class used for sword charging.
- The 3A report gives boss credit independently of the wave's chain.
- Neither short capture authenticates the binary or exact controller input.
- The two visible perfect routes do not prove that a lower rate blocks 3B.

## Delta summary

Fifteen genes describe the bounded 3A packet. The decision combines
immediate weapon selection and destruction order with separately
credited experience, sword and boss outcomes.

## New facts

- One attack input maps to an immediate attack rather than a retained
  weapon selection for a second confirmation.
- Enemy choice changes wave bonus and can affect the growth of the
  firing channel.
- Part destruction and defeat of the core contribute separate
  report values. The stage label, not the explosion alone, marks the exit.

## Principles and design implications

Make optional target ordering matter without stopping the player from
completing the encounter. Direct narrow and broad attack forms can
differ in their scoring opportunities even when both are usable for
survival. Keep boss part completion independently legible.

## Puzzle or game generation potential

Try two naturally spaced streams of objects and a choice of narrow and
wide actions. Let matched removal trios produce separate awards, with
a stable boundary for when missed opportunities are removed from play.
Attach an optional partial-completion credit to a late multipart target.

## New genes

- ACT-917
- INF-636
- SYS-1974
- SYS-1975
- SYS-1976
- SYS-1977

## New combinations

None. None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 443](../../../research/taxonomy-changes/TAXONOMY_CHANGE_443.md).

## New questions

- Does an AKA-O timeout change the exact point where the next chain opens?
- Which weapon-growth values are carried by Save Start under a documented file?

## Next recommended game

Continue Selection 060 with GAME-0698, Song of Bloom, on iPhone.

## Why this game

The original Saturn release visibly separates weapon choice, ordered
target destruction, weapon development and boss settlement in one short stage.
