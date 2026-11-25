---
game_id: GAME-0735
slug: toki-tori
game_title: "Toki Tori"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-421
  system:
    - SYS-037
    - SYS-772
    - SYS-2046
  constraint:
    - CON-068
    - CON-905
  information:
    - INF-179
    - INF-663
  objective:
    - OBJ-328
  time:
    - TIM-003
---

# Game: Toki Tori — Forest Falls Normal Level 5

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The bridges, warp and eggs instantiate distinct construction,
relocation and collection rules within one bounded attempt.

## Analysis scope

- Version / ruleset: North American commercial Game Boy Color
  cartridge, English, Capcom USA and Two Tribes, 2001. The lead
  emulator replay identifies the US multilingual cartridge image.
- Reproducible entry and exit: in Forest Falls Normal, select
  Level 5 and press Start at its field prompt. Stop when the last
  egg settles the level and the selection advances to Level 6.
  Earlier tutorials are evidence for controls only.
- Primary decision loop: take the eggs on the descending path,
  save the only Telewarp for the alcove above the dead end, use
  both bridge builds on separate gaps, and get the upper egg
  before dropping to the final low egg.
- Included: local movement, contact pickup, aiming and accepting a
  short upward warp, bridge footing, finite separate tool counts,
  remaining-egg feedback and the three-minute attempt. Excluded:
  Eyes controls, optional display configuration, invalid bridge
  refunds, exact maximum range, unrelated tool effects, earlier
  and later stage rules, Hard stages, ports, remakes and arbitrary
  speedrun inputs outside the witnessed route.
- Direct-play status: no personal cartridge or emulator session.
  The release identification uses the commercial physical
  edition and the replay submission. The original on-screen
  tutorial and scoped replay supply affirmative transitions.
  The alternative guides corroborate route order and time.
  Only silent background frames were examined.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| TT-001 | Capcom USA issued the Two Tribes game for Game Boy Color in 2001. The replay runs the English text of the North American multilingual image. | Observation | Corroborated | High | P1, P2, W1 |
| TT-002 | Level 5 Normal has five eggs, two bridge actions, one warp and a three-minute allowance. The field display separates the selected tool count, outstanding eggs and countdown. Changing tools changes which tool's remaining count appears. | Observation | Corroborated | High | W1 04:54–05:13, S1 FF05 |
| TT-003 | Direct movement along the descending authored route brings the chick into contact with the first three eggs. Each contact removes one from the outstanding set while the clock and remaining route continue. | Observation | Corroborated | High | W1 04:58–05:09, S1 FF05, S2 FF.N.5 |
| TT-004 | The original warp tutorial discloses aim with the directional pad and a separate confirmation, with a rejection cue where travel is impossible. On Level 5, spending the only warp places the chick in the alcove above the dead end behind the waterfall without climbing there. Both bridge uses remain. | Observation | Corroborated | High | W1 04:00, 05:08–05:11, S1, S2, S3 |
| TT-005 | Build to the right from the upper ledge and then across a second gap from the central footing. Each build creates traversable footing and spends one bridge use. Both spans remain after the second build and as the player drops below them. | Observation | Corroborated | High | W1 05:10–05:16, S1 FF05, S2 FF.N.5, S3 Level 5 |
| TT-006 | The upper egg is collected before the drop to the low egg. The final contact takes the counter to zero with 02:45 displayed and settles the level without a separate exit. | Observation | Corroborated | High | W1 05:12–05:20, S1 FF05, S2 FF.N.5 |
| TT-007 | The allowance drains in live play and bounds the all-egg clear. The trace completes within the allowance; the expired screen is not part of the observed route. | Observation | Corroborated | Medium | W1 04:58–05:16, S1 FF05, S4 |

## Basic data

- Release / origin: Two Tribes, Capcom USA, 2001.
  The analysis target is `PLAT-GAME-BOY-COLOR`.
- Mechanical families: `FAM-005` for constructing two links that
  become part of the walkable route and `FAM-017` for the ordered
  warp, bridges, upper egg and final drop.
- Primary evidence checked 2026-11-25:
  - **P1:** [MSU Libraries physical release record](https://lib.msu.edu/rovi_game/8193).
    Catalogues the Capcom USA Game Boy Color commercial edition.
  - **P2:** [North American retail box scan](https://gamefaqs.gamespot.com/gbc/468485-toki-tori/boxes/28344).
    Shows the original Game Boy Color product branding.
  - **W1:** [ThunderAxe31's US cartridge replay](https://tasvideos.org/3601M)
    and [submission](https://tasvideos.org/5753S). The author's
    submission discloses the US image and emulator. In the
    [linked recording](https://www.youtube.com/watch?v=yDM-4u9BFh8),
    the original warp instruction appears at 04:00. The route
    runs about 04:58–05:16. See the counters before the warp,
    after each build and on the final pickup. The author also
    documents the Level 5 start and finish allowance independently
    of the displayed second's precision.
- Independent descriptions:
  - **S1:** [sandstorm6299's original GBC guide](https://gamefaqs.gamespot.com/gbc/468485-toki-tori/faqs/26154),
    FF05 and tool sections. Lists the quantities, exact starting
    time and upper route.
  - **S2:** [koholinttakeout's original GBC guide](https://gamefaqs.gamespot.com/gbc/468485-toki-tori/faqs/24242),
    FF.N.5. Contrasts the initial descent, upward warp and
    construction order with the last drop.
  - **S3:** [MonkeyforaHead's 2001 GBC route](https://gamefaqs.gamespot.com/gbc/468485-toki-tori/faqs/14022),
    Forest Falls Level 5. Identifies the blocked approach,
    waterfall ledge and separate bridges.
  - **S4:** [Firsthand Game Boy Color review](https://gamefaqs.gamespot.com/gbc/468485-toki-tori/reviews/178609).
    Corroborates the live time limit on the original release.
- Claim IDs: TT-001–TT-007.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: move the chick toward the eggs and each ledge (TT-003, TT-005).
- Reuse `ACT-421`: aim the bounded warp upward and confirm it separately from normal movement (TT-004).

### System Behaviour Genes

- Reuse `SYS-037`: contact removes and credits each intermediate egg (TT-003).
- Reuse `SYS-772`: the confirmed warp consumes its use and relocates the chick directly to the accepted endpoint (TT-004).
- New `SYS-2046`: build a horizontal section of lasting traversable footing from the current ledge (TT-005).

### Constraint Genes

- Reuse `CON-068`: the three-minute attempt bounds completion of the required collection (TT-007).
- New `CON-905`: distinct nonrefilling warp and bridge counts bind the two tools independently within the attempt (TT-002, TT-004, TT-005).

### Information Genes

- Reuse `INF-179`: the current field shows local eggs, platforms, walls and open gaps as the camera follows movement (TT-003, TT-005).
- New `INF-663`: show the selected tool's remaining uses alongside the separate clock and outstanding egg count (TT-002, TT-006).

### Objective Genes

- Reuse `OBJ-328`: collect the entire authored set within the allowance; the final pickup settles the stage directly (TT-002, TT-006, TT-007).

### Time Genes

- Reuse `TIM-003`: the countdown moves forward during controllable field play (TT-003, TT-007).

## Formal state and transitions

Track the chick's position and facing, highlighted tool and legal
warp aim, remaining bridge and warp uses, placed bridge surfaces,
outstanding egg set, countdown and completion phase. A valid warp
changes the position without filling a gap. A bridge changes the
terrain in front of the chick without directly changing its position.
The two operations consume separate values. Intermediate contacts
remove one outstanding egg each. The last contact within the time
allowance advances the attempt to the clear state.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Level 5 started, five eggs outstanding | Follow the descending path | Contact collects the first three eggs by the wall | TT-002, TT-003 |
| At the dead end, one warp and two builds remain | Aim Telewarp up and confirm | Reach the alcove above the dead end and spend only the warp | TT-004 |
| On the ledge, first gap ahead | Activate Bridge Builder facing right | Place footing and cross with one build left | TT-005 |
| On the centre ledge, second gap ahead | Build again and cross | Reach the upper egg with no builds left | TT-005, TT-006 |
| Upper egg collected, low egg remains | Drop and reach the low egg | Settle the successful stage with time remaining | TT-006, TT-007 |

## Strategic and experiential structure

Save the warp for the vertical connection that normal movement
cannot supply on this route. Use the builds for horizontal links.
The remaining eggs do not force a fixed pickup order through the
objective itself. The upper-first order follows from access after
the final drop with the available tools spent.

## Replay and variation

The cited route presents a successful clear with the two spans
intact. Independent original-version accounts reproduce the
same order. They warn that falling early leaves no second warp
for the climb. Alternative speedrun routes, pause timing, invalid
inputs and the exact timeout presentation are outside this trace.

## Adjacent systems and history

Earlier original tutorials give separate practice for each tool.
Their more permissive budgets do not establish Level 5 charges.
The current phase ends before Level 6 or subsequent unlocks. The
later remake is a different ruleset.

## Normalised genome

- Action: ACT-008, ACT-421.
- System Behaviour: SYS-037, SYS-772, SYS-2046.
- Constraint: CON-068, CON-905.
- Information: INF-179, INF-663.
- Objective: OBJ-328.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `734` (`GAME-0001`–`GAME-0734`).
- Exact genome matches: none.
- Tied near matches: `GAME-0605` — Outtrigger (`5 / 15 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Outtrigger (GAME-0605)](../m-r/outtrigger.md) | ACT-008, CON-068, OBJ-328, SYS-037, TIM-003 | Both use direct movement to collect a complete set under a live deadline and settle on the final contact. Outtrigger routes three medals through existing jump geometry for a scored clear. Toki Tori spends separate tools to open a vertical move and construct two horizontal links before taking the last eggs in an access-preserving order. | Near, `0.333333`. |

## Taxonomy impact

Keep direct relocation separate from altering the walkable route.
The budget operates per tool; spending one does not reduce the
other or itself end the attempt. The final pickup is a separate
all-collection settlement, independent of any exit.

## Negative results

- Warp relocates the chick without building a surface.
- The first bridge does not span both gaps in the witnessed route.
- Spending both builds does not remove already placed footing or
  prevent ordinary movement.
- The last egg requires no extra exit action.

## Delta summary

Record the fifth ordinary Forest Falls route, where a single warp
opens the vertical approach and two finite bridge builds connect
the final upper tier before the last descent.

## New facts

- The selected tool counter changes independently of remaining
  eggs and time.
- The upward warp and two horizontal bridges consume different
  stocks and affect different parts of the route.
- The final egg settles the timed attempt directly.

## Principles and design implications

Give the two tools orthogonal route roles and keep their stocks
separate. A low target can be left until the final drop, so the
local terrain creates an ordering problem without an explicit
pickup sequence in the objective.

## Puzzle or game generation potential

Build a small tiered route with a dead-end approach, exactly one
vertical relocation, two short horizontal spans and a final low
target. Check the two bridge stocks independently of the last
pickup and test a premature drop as a separate route.

## New genes

- CON-905
- INF-663
- SYS-2046

## New combinations

None. No verified combination is a proper subset of the signature.

## Taxonomy changes

[Taxonomy Change 481](../../../research/taxonomy-changes/TAXONOMY_CHANGE_481.md).

## Next recommended game

Bomb Rush Cyberfunk on Xbox One is the next Selection 064 unit.

## Why this game

Finite tools make traversal itself an allocation puzzle.
The last egg is visible before the route to it is ready.

## Review status

Reviewed 2026-11-25 for the original North American Game Boy Color
Forest Falls Normal Level 5.
