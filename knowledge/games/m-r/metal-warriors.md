---
game_id: GAME-0728
slug: metal-warriors
game_title: "Metal Warriors"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-946
  system:
    - SYS-755
  constraint: []
  information:
    - INF-659
  objective:
    - OBJ-377
  time:
    - TIM-003
---

# Game: Metal Warriors — Rescue at Axis 5

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Nitro, Marissa and the station barriers are scoped instances.

## Analysis scope

- Version / ruleset: English North American Super NES commercial
  cartridge, `SNS-AWME-USA`, April 1995. Use default controls
  and a fresh One Player story opening. The label, booklet and
  attributed NTSC trace identify the release context. The exact
  executable and physical hardware used by each recording are unverified.
- Structured target: `PLAT-SUPER-NINTENDO`. Start with the first
  controllable Nitro on the Axis 5 approach. Reach Marissa, advance
  through the escape passage and stop at the first Mission Complete
  overlay, before playing Boarding Party. The departure and briefing
  are used only to confirm the handoff.
- Primary decision loop: walk or apply held thrust to steer the
  occupied Nitro through corridor heights, aim at enemies and
  eligible breakable obstructions, read the worn chassis, find
  Marissa and traverse the escape corridor.
- Included: horizontal control, flight, aimed attacks, course
  obstruction destruction, visible damage and the two-part rescue
  outcome. Excluded: mandatory ejection, other suits, alternate
  pilot routes, death and continue behaviour, full damage arithmetic,
  optional pickup optimisation, map coverage and later missions.
- Direct-play status: no personal cartridge, emulator or console
  session. The original instruction booklet, a cartridge archive,
  a first-hand route account and two English gameplay records
  establish the scoped rules. Only silent background frames
  were inspected. The selected route keeps Stone in Nitro.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| MW-001 | The North American product is the LucasArts Super NES game published by Konami in April 1995. One Player enters the mission named Rescue at Axis 5, with the assigned Nitro. | Observation | Corroborated | High | P1 pp. 5–8, P2, P3, W1 01:09–02:18, W2 01:39–02:46 |
| MW-002 | Nitro walks on local surfaces, rises under the held flight control and can steer into another corridor level while airborne. The manual names B for flight and describes releasing and pressing it again to manoeuvre. | Observation | Corroborated | High | P1 pp. 11–13, W1 02:27–02:50 and 03:27–03:48, W2 02:52–03:14 and 04:12–04:33 |
| MW-003 | Nitro aims and fires on the same live route. On the escape leg the forward shots remove eligible red lattice blocks, changing solid coverage so Nitro can pass to the left. The exact number of shots and early wall-destruction attribution were not measured. | Observation | Corroborated | High | P1 pp. 11–13, W1 04:43–04:56 and 05:15–05:33, W2 05:30–05:48, S1 |
| MW-004 | The damaged controlled suit stays visibly darker between hits without a life bar. The booklet identifies dents, sparks and later offensive loss. This trace shows the darkened Nitro continuing to fire; an arm-loss threshold was not witnessed here. | Observation | Corroborated | High | P1 pp. 9–10, W1 03:33–03:52 and 04:41–05:34, W2 04:42–05:49 |
| MW-005 | Marissa stands at the end of the rescue approach. Closing the distance triggers the rescue acknowledgment and asks the player to leave. The same occupied Nitro keeps control and can enter the left block passage. A separate manual passenger transfer is not visible. | Observation | Corroborated | High | W1 05:02–05:18, W2 05:16–05:33, S1 |
| MW-006 | The result appears after travelling left beyond the rescue point, while Nitro is still visible on the route. The extraction scene follows Mission Complete. The examples do not show a separate controlled boarding action or a mandatory boss. | Observation | Corroborated | High | W1 05:18–05:44, W2 05:32–05:57, S1 |
| MW-007 | Default Select permits exiting and entering a suitable battledroid. On foot the pilot has separate movement and jet-pack commands. The documented general affordance is outside the selected Mission 1 trace. | Observation | Direct | High | P1 pp. 9 and 11–13, S1 Mission 2 contrast |

## Basic data

- Release / origin: LucasArts developed the game for the Super NES.
  Konami (America) Inc. published the original North American
  commercial Game Pak. The April month is corroborated, without a
  claim of a particular retail day or exact revisions across copies.
- Platform or physical form: Super NES cartridge. One Player starts
  with a mission-assigned suit, with no free character selection.
- Mechanical family: `FAM-017`, because the rescue while still
  controlling the mech precedes the final extraction boundary.
- Primary sources checked 2026-11-25:
  - **P1:** [Konami’s original North American instruction booklet](https://archive.org/details/metal-warriors-usa).
    Printed pp. 5–13 cover solo play, the mission log,
    damage presentation, default controls, ejection and Nitro.
  - **P2:** [Snes Central cartridge and box archive](https://snescentral.com/article.php?id=0476).
    Contemporary packaging and physical identifier. The archive
    attributes the developer and publisher separately.
  - **P3:** [Mike Ebert’s developer interview](https://www.gamedeveloper.com/game-platforms/playing-catch-up-i-zombies-ate-my-neighbors-i-mike-ebert).
    Developer attribution, original release month and suit design context.
- Independent recorded and first-hand sources:
  - **W1:** [LongplayArchive, NTSC route by JTBKnuggetsauce](https://www.youtube.com/watch?v=k9mPsdBH01g).
    First control is visible before the creator’s 02:19 chapter marker.
    Rescue acknowledgment begins around 05:06 and the result appears
    around 05:34. The exact hardware and ROM revision are unverified.
  - **W2:** [World of Longplays, xRavenXP’s full run](https://www.youtube.com/watch?v=5rtTZh7F9m0).
    Shows the same English mission, rescue and extraction. The
    channel discloses that its recordings can use save states. W2
    corroborates on-screen effects without proving native execution.
  - **S1:** [Attributed GameFAQs route archive](https://gamefaqs.gamespot.com/snes/563216-metal-warriors/faqs/5410).
    Mission 1 describes reaching Marissa and exiting left.
    Mission 2 separately documents a pilot-scale passage.
- Claim IDs: MW-001–MW-007. Reproduce the ordinary rescue from
  fresh One Player control. Observe acknowledgment before
  crossing the escape boundary and stop at the explicit result.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: move the persistent controlled Nitro through
  the open station surfaces (MW-002).
- Reuse `ACT-161`: aim and act upon a reachable hostile
  or eligible lattice barrier (MW-003).
- New `ACT-946`: keep powered lift active while steering
  laterally inside the passage (MW-002).

### System Behaviour Genes

- Reuse `SYS-755`: accepted hits remove the solid lattice
  units and reveal a usable escape path (MW-003).

### Constraint Genes

No separately admitted constraint. Geometry and success boundary
are covered by the action, destruction and objective genes.

### Information Genes

- New `INF-659`: the controlled suit’s persistent appearance
  discloses worsening damage in place of a life bar (MW-004).

### Objective Genes

- New `OBJ-377`: credit the designated rescue, then cross the
  escape boundary while control and mission state are live (MW-005, MW-006).

### Time Genes

- Reuse `TIM-003`: move and fire during the live movement and
  enemy response, before the current route position resolves (MW-002, MW-003).

## Formal state and transitions

Track the controlled Nitro position and heading, thrust state,
body damage cues, solid barrier occupancy and rescue acknowledgment.
The latter changes the active route from approach to extraction.
The Mission Complete overlay is a future boundary distinct
from the change in route direction at the rescue.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Nitro stands by a lower platform | Hold B and steer into the open shaft | Thrusters stay active during the ascent and Nitro reaches another level | MW-002 |
| An intact lattice section obstructs the retreat | Direct eligible fire at the section | Hit lattice units are removed, exposing passage geometry | MW-003 |
| The damaged Nitro remains in control | Read its body between successive hits | It remains visibly darker with no dedicated life bar | MW-004 |
| Marissa is visible ahead | Bring Nitro into the rescue location | The rescue acknowledgment appears and control continues | MW-005 |
| Rescue has been credited | Move left beyond the opened corridor | The mission result appears before the departure scene | MW-006 |

## Strategic and experiential structure

Use the held flight input to position Nitro at the next passage
height. Clear solid obstacles with directed fire and read the
suit itself while moving rather than waiting for a numeric gauge.
After reaching Marissa, use the already opened or newly broken
lattice to get back toward the mission's extraction boundary.

## Replay and variation

Both recordings credit the rescue and left escape in Nitro with
different combat timing. The evidence does not establish the
only possible traversal or all alternate ejection outcomes.

## Adjacent systems and history

The documented pilot can exit and use a separate jet pack.
The first recorded complete rescue does not require that
action. The later pilot-only corridor belongs to Boarding Party.
Other suits and competitive play also remain outside this unit.

## Normalised genome

- Action: ACT-008, ACT-161, ACT-946.
- System Behaviour: SYS-755.
- Constraint: none.
- Information: INF-659.
- Objective: OBJ-377.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `727` (`GAME-0001`–`GAME-0727`).
- Exact genome matches: none.
- Tied near matches: `GAME-0725` — Crypt Custodian (`4 / 13 = 0.307692`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Crypt Custodian (GAME-0725)](../a-f/crypt-custodian.md) | ACT-008, ACT-161, SYS-755, TIM-003 | Both require live traversal and aimed attacks that can remove solid obstacles. Crypt Custodian detours to acquire a broom and exits after an authored change of admission. Metal Warriors uses held flight to change elevation and credits the rescue before the player breaks through toward the exit. | Near, `0.307692`. |

## Taxonomy impact

Separate sustained propulsion, persistent body damage feedback and
the ordered rescue-and-exit success condition. Keep the exact
thrust numbers and terminal damage thresholds outside the claims.

## Negative results

- The rescue notification does not end the mission on its own.
- The documented ejection option is not required on the observed route.
- No separate controllable loading or boarding action is visible.
- The in-world damage cues do not establish an exact life total.

## Delta summary

Record a single flight-capable chassis through the ordinary Axis 5
sortie, with terrain damage altering the escape route and a rescue
state required before the terminal exit.

## New facts

- Held Nitro thrust supports controlled passage-height changes.
- The damaged chassis remains legible without an independent life bar.
- Rescue and successful extraction are separate observed transitions.

## Principles and design implications

Make sustained lift useful for vertical route selection and use
distinct breakable material to indicate an alternate opening.
Let a rescue acknowledgment change the task while preserving
active traversal to the true end boundary.

## Puzzle or game generation potential

Use one ruled corridor with a vertical bypass, damageable solid tiles,
a designated subject and a separately checked exit. Test the rescue-state
change and extraction outcome separately. Keep the pilot form optional
unless the level explicitly verifies a different size constraint.

## New genes

- ACT-946
- INF-659
- OBJ-377

## New combinations

None matched after checking all 274 verified combinations.

## Taxonomy changes

[Taxonomy Change 474](../../../research/taxonomy-changes/TAXONOMY_CHANGE_474.md).

## Next recommended game

The Last Campfire on PlayStation 4 is the next Selection 063 unit.

## Why this game

The first sortie combines live flight, material changes and a rescue
whose recognition does not yet finish the route.

## Review status

Reviewed 2026-11-25 for the commercial English North American Super NES
ruleset. The record ends at the first Rescue at Axis 5 mission result.
