---
game_id: GAME-0736
slug: bomb-rush-cyberfunk
game_title: "Bomb Rush Cyberfunk"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
    - ACT-949
  system:
    - SYS-036
    - SYS-974
    - SYS-2047
  constraint: []
  information:
    - INF-179
    - INF-664
  objective:
    - OBJ-379
  time:
    - TIM-003
---

# Game: Bomb Rush Cyberfunk — First Franks mural in Versum Hill

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The rail, trace and repaint are instances of movement,
selection and distinct-site credit.

## Analysis scope

- Version / ruleset: English Xbox One commercial Xbox Store
  base game, product 9PN0WRT1ZFJ2, released September 1, 2023.
  The lead trace runs the Xbox-family product on Series X.
  The installed Xbox One build and device-specific parity were
  not tested directly.
- Reproducible entry and exit: in Chapter 1 Versum Hill, use Red
  with the skateboard after the first plaza conversation with Bel.
  Pass the street barricade, use the plaza rail toward the large
  Franks mural by the circular sculpture, paint it, advance the
  resulting conversation and paint the same wall once more.
  Stop when free movement resumes with the second mural visible.
- Primary decision loop: use skate motion and rail contact to
  reach a marked wall, commit to its local input, pick a sequence
  of directional nodes and distinguish the first territory credit
  and encounter from the repeatable change of design.
- Included: skate movement and landing, an attached rail, the
  nearby spray prompt, directional node feedback and design,
  distinct-site reputation, first Frank response and one repaint.
  Excluded: combo and boost optimisation, expiry behaviour and
  exact duration of the trace allowance, other spots except a
  credit contrast, phone design inventory, heat, rival challenges,
  other chapters, DLC and mods.
- Direct-play status: no personal Xbox One or Series X session.
  Microsoft and Team Reptile establish the shared store release.
  Series X footage shows Xbox prompts, passage, first and repeated
  paint. An independent PC trace corroborates the first encounter
  and shows a different accepted design. Only muted background
  frames were inspected. Xbox One timing and binary identity
  remain unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| BRC-001 | The commercial base product launched on Xbox One and Series X on September 1, 2023. The scoped Xbox controller prompts come from a Series X recording of the release, with no installed Xbox One build fingerprint. | Observation | Corroborated | High | P1, P2, W1 |
| BRC-002 | Bel asks how to draw the Franks out. Red can ride past the plaza barricade, attach the board to a compatible railing, follow it and leave it in an airborne arc toward the marked wall. The rail is one available route, with a different approach accepted in W2. | Observation | Corroborated | High | P1, W1 00:38–01:16, W2 04:59–05:25, S1 |
| BRC-003 | A nearby paintable wall exposes a spray icon and RB prompt. Accepting shifts control to the marked surface trace. Ordinary moving past the wall does not change its design. | Observation | Corroborated | High | W1 01:15–01:18, 02:03–02:06, W2 05:23–05:27, S2 |
| BRC-004 | During the trace, directional points link in the chosen order. Yellow feedback and segments distinguish visited points. A small allowance bar decreases while node input remains available. Two accepted orders are seen producing different artwork at the same wall. Exact expiry is unmeasured. | Observation | Corroborated | High | W1 01:17–01:23, 02:04–02:13, W2 05:26–05:32, S2, S3 |
| BRC-005 | The first completed paint changes the wall and triggers a local Frank conversation. Once free movement returns, the Xbox HUD shows district REP 006. W2 also gets the Frank conversation after settling a different design at that wall. | Observation | Corroborated | High | P1, W1 01:21–02:00, W2 05:31–06:13, S1 |
| BRC-006 | After that encounter, the Xbox trace paints the same mark again, displaying a different design. Movement returns directly, with no second Frank encounter and no second first-site REP announcement. | Observation | Direct | High | W1 02:03–02:16 |
| BRC-007 | REP accrues from newly credited sites. In the Xbox trace the large mural and its immediate repaint are followed later by one new small mark, with REP 008 displayed instead of another full large-site grant. The later small mark tests the running total and is outside the signature's scope. | Observation | Corroborated | High | W1 01:59–02:16, 02:57–03:08, S2, S3 |

## Basic data

- Release / origin: Team Reptile, Xbox Store product 9PN0WRT1ZFJ2,
  September 1, 2023. Analysis target `PLAT-XBOX-ONE`.
- Families: `FAM-017` for reach, address, trace and encounter
  dependencies, and `FAM-010` for the live route and active
  node-selection interval.
- Primary sources checked 2026-11-25:
  - **P1:** [Microsoft's Xbox product listing](https://www.xbox.com/en-us/games/store/bomb-rush-cyberfunk/9pn0wrt1zfj2).
    Lists the shared commercial product, date, Xbox One support
    and traversal, graffiti and territory roles.
  - **P2:** [Team Reptile's release trailer](https://www.youtube.com/watch?v=9HKDfO51Ja4).
    Its official description names the September 1 Xbox release.
  - **W1:** [Skycaptin5's Xbox Series X recording](https://www.youtube.com/watch?v=08M3hGHSNgU&t=38s).
    Around 00:46–01:15 Red passes the barricade and uses the plaza
    rails. In 01:16–01:23 the wall prompt opens the trace and its
    first design settles. The Frank exchange ends around 01:59,
    with REP 006. At 02:04–02:14 the same site accepts
    `WHOLE SIXER`; at 03:05 REP 008 is visible after a separate
    new small mark.
  - **W2:** [Amy Symilton's independent Chapter 1 route](https://www.youtube.com/watch?v=hWt3Z3i1aBs&t=319s).
    The PC control screen appears around 02:00. At 05:23–05:33
    a different path and design settle the same first wall. The
    Frank appears during 05:33–06:12. The recording is a spatial
    and causal contrast, not Xbox One build evidence.
- Supporting sources:
  - **S1:** [Versum Hill play guide](https://www.neoseeker.com/bomb-rush-cyberfunk/Versum_Hill).
    Describes the opening barricade, the first large Franks mark
    and the resulting conversation.
  - **S2:** [Graffiti interaction guide](https://bombrushcyberfunk.wiki.gg/wiki/Graffiti).
    Describes the contextual spray action, directional designs
    and repeated painting of one location.
  - **S3:** [District reputation reference](https://bomb-rush-cyberfunk.fandom.com/wiki/REP).
    Describes the distinct new-site predicate for REP. Site
    totals and later amendments are outside this unit.
- Claim IDs: BRC-001–BRC-007.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: steer Red on the moving skateboard around the barricade and into mural range (BRC-002).
- Reuse `ACT-341`: accept the available mural interaction at the prompt to start its local input phase (BRC-003).
- New `ACT-949`: choose a paint design by directing the stick through a specific order of eligible nodes (BRC-004).

### System Behaviour Genes

- Reuse `SYS-036`: the skateboard leaves contact into a progressing airborne arc and lands at a reachable position (BRC-002).
- Reuse `SYS-974`: eligible contact carries the board along a rail until the skater leaves it (BRC-002).
- New `SYS-2047`: a site's first accepted paint credits district REP, while a later paint can change the image without another grant (BRC-005–BRC-007).

### Constraint Genes

No separate constraint is admitted. Marked-surface eligibility is
in the addressed action boundary. The trace bar is visible, but its
expiry outcome and the absence of a paint resource budget are not
generalised to other graffiti sizes or chapters.

### Information Genes

- Reuse `INF-179`: the visible plaza exposes rails, entering approaches and the marked wall (BRC-002, BRC-003).
- New `INF-664`: the spray prompt and trace overlay expose the available interaction, visited nodes and local allowance (BRC-003, BRC-004).

### Objective Genes

- New `OBJ-379`: complete the first paint on the designated Franks mural, receive the local response and resume traversal (BRC-002, BRC-005, BRC-006).

### Time Genes

- Reuse `TIM-003`: rail motion and airborne travel progress during steering, and the live graffiti trace accepts input while its allowance advances (BRC-002, BRC-004).

## Formal state and transitions

Track the skater's position, velocity and current contact surface;
the target wall, addressed prompt and trace; its displayed design
and first-credit state; the district REP and the local encounter
phase. A paint request opens the local trace. An accepted direction
sequence updates the wall design. The first such result for the
site also adds its district credit and opens the authored exchange.
Repainting updates the visible design with the site credit already
recorded and the encounter already resolved.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Near the plaza entrance with skateboard control | Reach and take a compatible rail | Board follows the path; departing permits an aerial approach | BRC-002 |
| First mural still belongs to the Franks and spray prompt is visible | Press the paint input | Switch from traversal to the directional node trace | BRC-003 |
| First mural trace active | Select and connect a valid order of nodes | Recognise the design and overpaint the site | BRC-004, BRC-005 |
| The first paint has settled | Follow the resulting local exchange to its end | Frank appears, then route control resumes with REP 006 shown | BRC-005 |
| Wall already credited and previously painted | Reopen its prompt and take a different valid trace | Replace the visible design without another visit credit or encounter | BRC-006, BRC-007 |

## Strategic and experiential structure

The rail saves a traversal step but does not satisfy the wall
by itself. The node trace is expressive because the order
chooses the design. The immediate story and reputation results
are tied to the site, so replaying a different design at the
same wall cannot substitute for reaching fresh surfaces.

## Replay and variation

The Xbox trace paints a multicolour design and later chooses
`WHOLE SIXER` over it. The independent PC trace settles a
different first design and still draws the local Frank out.
The route stays within the same plaza. Later region gates and
unseen timeout outcomes are outside the comparison.

## Adjacent systems and history

Jet Set Radio pairs marked-wall progress with a prescribed
command trace and spray spending. This scope establishes
elective node order and a repaintable wall with one credit.
It does not infer balance rules from the predecessor or later
high-score, police or district-control encounters.

## Normalised genome

- Action: ACT-008, ACT-341, ACT-949.
- System Behaviour: SYS-036, SYS-974, SYS-2047.
- Constraint: none.
- Information: INF-179, INF-664.
- Objective: OBJ-379.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `735` (`GAME-0001`–`GAME-0735`).
- Exact genome matches: none.
- Tied near matches: `GAME-0615` — Skate Story (`4 / 15 = 0.266667`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Skate Story (GAME-0615)](../s-z/skate-story.md) | ACT-008, ACT-341, INF-179, TIM-003 | Both steer a skater through a visible plaza, enter a local interaction and act while movement or the current state advances. Skate Story uses its obelisk lesson to land qualifying ollies at four crests and unlock a separate portal. Bomb Rush Cyberfunk approaches a wall along a possible rail route, chooses the design with a node trace and credits the first paint separately from later repainting. | Near, `0.266667`. |

## Taxonomy impact

Separate rail attachment and contextual activation from the
directional choice that selects the image. Site credit and
artwork remain separate state variables. The resolved local
encounter differs from a district-wide cleared quota.

## Negative results

- The rail itself does not change the wall or grant site REP.
- Distinct accepted designs can settle the same first site.
- Repainting remains possible and does not replay the encounter.
- The later battle, street countdown and spray-frame budget of
  a different game or mode are not part of this path.

## Delta summary

Record the opening Versum Hill rail and first Franks mural
through route control, a selectable trace, separate territory
credit and an optional immediate repaint.

## New facts

- A marked wall can accept different designs from different
  orders through the directional nodes.
- The first accepted paint credits six REP and opens the local
  exchange before returning traversal control.
- A later paint can change the image without another site credit.

## Principles and design implications

Let exploration and expressive selection coexist at a marked
location. Bind progression to the distinct place rather than
to the repeatable cosmetic action.

## Puzzle or game generation potential

Build a compact route with one optional rail, one marked
wall and at least two valid traces. Check first credit,
repainting with a different trace and return from the local
reaction as separate branches.

## New genes

- ACT-949
- INF-664
- OBJ-379
- SYS-2047

## New combinations

None. No verified combination is a proper subset of the signature.

## Taxonomy changes

[Taxonomy Change 482](../../../research/taxonomy-changes/TAXONOMY_CHANGE_482.md).

## Next recommended game

Pullblox on Nintendo 3DS is the next Selection 064 unit.

## Why this game

One local route connects free movement, surface contact,
gesture choice, site credit and a story response. Repainting
the wall shows which outcomes depend on novelty of the site.

## Review status

Reviewed 2026-11-25 for the English commercial Xbox release's
first Franks mural and immediate repaint. Witness Xbox hardware
and analysis target are identified separately above.
