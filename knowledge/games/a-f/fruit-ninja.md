---
game_id: GAME-0401
slug: fruit-ninja
game_title: "Fruit Ninja"
analysis_status: reviewed
reviewed: 2026-09-25
combination_ids: []
gene_ids:
  action:
    - ACT-537
  system:
    - SYS-004
    - SYS-1069
    - SYS-1071
    - SYS-1072
    - SYS-1073
    - SYS-1074
  constraint:
    - CON-113
    - CON-183
  information:
    - INF-399
  objective:
    - OBJ-002
  time:
    - TIM-003
---

# Game: Fruit Ninja

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The fruit species,
screen coordinates, score thresholds and touch hardware are parameters, not
separate genes.

## Analysis scope

- Version / ruleset: the paid original iPhone *Fruit Ninja* at the May 2010
  version 1.2 rule boundary, **Classic mode without later purchasable
  power-ups**. Halfbrick's contemporary release note explicitly introduces
  one-swipe combos to Classic in 1.2 and distinguishes the new bomb-free,
  90-second Zen mode. The exact executable build was not inspected.
- Structured analysis target: original iPhone touch release; see `GAME-0401`
  in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: start one Classic score run at zero points, no missed-fruit marks and
  no fruit or bomb yet touched by the first stroke.
- Primary decision loop: watch fruit and occasional bombs rise and fall;
  trace a finger across several fruit in one continuous stroke to score a
  combo, or shorten/delay that path so it avoids a bomb; accept a missed fruit
  only within the finite strike allowance, use score milestones to recover a
  spent chance when available, and keep scoring until a bomb is cut or the
  missed-fruit stock is exhausted.
- Terminal: a swipe intersecting a bomb immediately ends the current run;
  otherwise the third outstanding missed-fruit strike ends it. The accumulated
  score is the outcome, not a fixed winning threshold. A recovery milestone
  may remove one outstanding strike before exhaustion. Exact same-frame
  precedence among score, miss and recovery is not established.
- Included: continuous touch-path input; changing fruit/bomb flights; path
  intersection and fruit splitting; one-swipe bonus for at least three fruit;
  occasional critical-score bonus; one miss mark for each uncut fruit leaving
  play; three-strike loss, immediate bomb loss, bounded recovery at score
  milestones, visible live objects and counters, and uninterrupted real time.
- Excluded: 90-second Zen; later 60-second Arcade, bananas, Blitz and end
  bonuses; purchasable Bomb Deflect, Berry Blast, alternate blade powers,
  missions and currencies; multiplayer, leaderboards and achievements; the
  separate Free app and modern rebalanced Classic versions. The source set
  does not establish launch probabilities, physics constants, critical odds,
  exact recovery cap implementation or simultaneous-event ordering.
- Reproducible parameterisation: on the original paid iPhone v1.2 binary,
  record its version, selected Classic mode, initial marks/score, fruit and
  bomb launch trajectories, finger-down/path/finger-up samples, every cut,
  three-plus-fruit single-stroke bonus, critical award, escaped uncut fruit,
  score crossing 100, restored mark, bomb contact and terminal screen. Repeat
  to distinguish fixed scoring/strike rules from variable launches. The
  published evidence supports a bounded reconstruction but not a direct trace.
- Potential scoped modules: original Zen, later Arcade, and power-up-equipped
  Classic should be separate packets if analysed.
- Direct-play status: none. No iPhone binary, touch trace, screenshot, video
  or audio was inspected. The version-1.2 combination boundary comes from a
  contemporaneous Halfbrick press release; original-launch and later
  developer descriptions plus contemporary reviews corroborate the stable
  Classic loop. The 100-point recovery rule is supported retrospectively,
  not independently tied to a directly examined v1.2 executable.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FN-001` | Halfbrick introduced one-stroke bonuses for three or more fruit into Classic in iPhone version 1.2; Zen is a separate mode. | Confirmed | Direct | High | P1 |
| `FN-002` | A continuous finger swipe slices the fruit whose moving silhouettes it crosses. | Observation | Corroborated | High | S1, P2 |
| `FN-003` | The original Classic run tolerates only two missed fruit; the third ends it, while a sliced bomb ends it immediately. | Observation | Corroborated | High | S1, P2 |
| `FN-004` | Three or more fruit in one stroke award an additional combo bonus; the first-party v1.2 note specifies +3 for three and +4 for four. | Confirmed | Direct | High | P1 |
| `FN-005` | Critical hits can grant extra points randomly, but the exact chance and same-frame settlement are not established for v1.2. | Observation | Limited | Medium | P2, R1 |
| `FN-006` | Classic can erase one accrued missed-fruit mark at a 100-point milestone, up to the ordinary allowance; exact v1.2 binary behaviour remains uninspected. | Observation | Corroborated | Medium | S2, S3, R1 |
| `FN-007` | Launched groups and bombs vary during a continuing score run and no fixed last volley is the selected terminal. | Observation | Corroborated | Medium | S1, P2 |
| `FN-008` | Exact object probabilities, flight constants, later power-up effects and ordering of coincident events are not inferred. | Observation | Limited | High | R1 |

## Basic data

- Release / origin: Halfbrick's paid iPhone game from 2010. The cited May 21
  update explicitly calls its version 1.2 a free update to the original paid
  title; it is not the distinct later Free app.
- Platform or physical form: iPhone touch screen, structured target `PLAT-IOS`.
- Puzzle family: real-time system pressure (`FAM-010`): flights and deadlines
  continue as the player decides whether a wide scoring stroke is safe.
- Contemporary first-party source, checked 2026-09-25: **[P1]** [Halfbrick's
  version 1.2 release announcement](https://www.impulsegamer.com/wordpress/?p=6169),
  carried as a 2010 press release, for original paid iPhone version, Classic
  combo and separate Zen boundaries.
- Later first-party cross-check, checked 2026-09-25: **[P2]** [Halfbrick's
  beginner guide](https://www.halfbrick.com/blog/the-ultimate-beginners-guide-to-fruit-ninja),
  for swipe, three-fruit combo, random critical and Classic/Arcade/Zen split.
  It describes later versions too; its power-ups are explicitly excluded.
- Independent played descriptions, checked 2026-09-25:
  - **[S1]** [TouchArcade's April 2010 launch
    review](https://toucharcade.com/2010/04/21/fruit-ninja-review-all-ninja-hate-fruit/),
    for swipe, changing volleys, three misses and immediate bomb loss.
  - **[S2]** [Pocket Gamer's 2013 iOS interview with
    Halfbrick](https://www.pocketgamer.com/fruit-ninja/halfbrick-shares-10-tips-tricks-and-secrets-for-fruit-ninja-on-ios/),
    for the 100-point recovery and bomb-versus-miss trade in later Classic.
  - **[S3]** [Contemporary Windows Phone Classic
    guide](https://www.xboxachievements.com/forum/topic/256162-achievement-guideroadmap-wp8-version/),
    December 2010, for the same recovery cadence on an adjacent port. It is
    not evidence that the iPhone binaries are byte-identical.
- **[R1]** This record's version-transfer and direct-play audit.

## Mechanical decomposition

### Action Genes

- New `ACT-537`: draw one continuous finger-held blade path across the live
  screen. One gesture may reach several fruit or accidentally cross a bomb;
  touching separate points is not the same committed path. `FN-002`.

### System Behaviour Genes

- Existing `SYS-004`: variable launched object groups and occasional critical
  reward use outcomes not fixed by the player. The precise distribution is
  deliberately unknown.
- Existing `SYS-1069`: a score milestone can restore one missed-fruit chance
  without purchasing it. The 100-point cadence is a carrier parameter with
  medium version-specific confidence (`FN-006`).
- New `SYS-1071`: release fruit and occasional bomb bodies into the same
  continuing screen; their trajectories create moving opportunities and
  hazards rather than fixed board pieces.
- New `SYS-1072`: resolve a sampled swipe path against moving objects; crossed
  fruit split, whereas bomb contact is routed to the immediate-loss rule.
- New `SYS-1073`: award points for cut fruit, add the v1.2 group bonus when
  one stroke cuts at least three, and optionally add a random critical bonus.
- New `SYS-1074`: when an uncut fruit leaves the play screen, add one missed
  mark; a bomb leaving uncut does not spend a miss. `FN-002`–`FN-007`.

### Constraint Genes

- Existing `CON-113`: a visible bomb crossed anywhere along the committed
  moving blade path ends the attempt; this is not merely a lost life.
- Existing `CON-183`: a finite three-miss allowance gates complete run loss,
  with supported score milestones capable of restoring a spent chance.

### Information Genes

- New `INF-399`: show present fruit and bombs together with score and miss
  marks, while later object launches and critical outcomes are not previewed.

### Objective Genes

- Existing `OBJ-002`: maximise the accumulated run score without a finite
  victory score.

### Time Genes

- Existing `TIM-003`: launched objects keep rising and falling while the
  finger waits, moves or lifts.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Three fruit rise near each other, no bomb on their line | trace one uninterrupted stroke through all three | all crossed fruit split, each scores and the v1.2 +3 group bonus applies | path intersection and one-stroke grouping | `FN-002`, `FN-004` |
| Two fruit separate around a bomb | shorten the stroke to one safe fruit | the crossed fruit scores and the bomb is not touched; another fruit may later be missed | safe-path trade against score | `FN-002`, `FN-003` |
| A visible bomb intersects the drawn path | continue the stroke through it | the current Classic run ends immediately even if miss marks remain | distinct bomb terminal | `FN-003` |
| One fruit falls uncut off-screen | make no cutting path through it | one miss mark is added; a bomb falling away adds none | miss debit | `FN-003` |
| Two misses are outstanding | let another uncut fruit leave | third outstanding mark ends the run | finite failure stock | `FN-003` |
| A previous miss exists and score passes 100 | settle qualifying cut points | one accrued mark is removed, up to the ordinary allowance; original v1.2 implementation is not directly inspected | repeatable score recovery | `FN-006` |
| A cut is eligible for a critical result | settle scoring | random bonus may add points without changing which objects the stroke intersected | score randomness separate from path | `FN-005` |

## Edge-case audit

- A bomb is not another fruit: cutting it fails immediately, while leaving it
  alone does not add a missed-fruit mark. A wide combo stroke therefore has
  a geometrical risk absent from a narrower single-fruit cut.
- The combo counts fruit within *one* swipe, not the number cut by several
  quick gestures. The +3/+4 values are version-1.2 parameters, not new genes.
- A missed fruit's third outstanding mark, not the third fruit ever missed,
  is terminal if an earlier mark was recovered at a score milestone. The
  exact ordering when a score recovery and off-screen miss share a frame is
  unresolved.
- A random critical award affects score, not whether the blade path touched
  the fruit. No critical probability is assumed.
- Later Arcade's timed bananas and 2016 guide's purchased Bomb Deflect
  cannot be imported into the 2010 unpowered Classic signature.
- Current visible objects and counters are shown, but future launches are
  not. `INF-001` would overstate the previewed state.

## Strategic and experiential structure

- Local decision: wait until fruit align, then choose a stroke that groups
  fruit without intersecting a bomb; accept a single miss if the alternative
  risks immediate failure.
- Medium-term planning: keep the miss allowance alive long enough to reach a
  score recovery, while opportunistic multi-fruit strokes accelerate scoring.
- Long-term structure: the run has no fixed completion stage; a higher score
  records a better attempt as changing volleys keep requiring live judgement.
- Failure attribution: a crossed bomb and an escaped fruit have different,
  visible consequences. Critical and future launches remain uncertain rather
  than information the player could have deduced from the present screen.

## Replay and variation

- The positions, times and groups of fruit and bombs can differ, yielding
  different safe paths and combo chances; exact selection odds are unknown.
- One can chase wide combos or preserve chances with narrow strokes and a
  deliberate missed fruit. The stable terminal rules make higher-score runs
  comparable without treating a leaderboard as the game's win condition.

## Adjacent systems and history

- Version 1.2 adds Classic combos to the original iPhone score loop; the new
  Zen mode removes bombs and lives and is not blended into this genome.
- *Geometry Wars: Retro Evolved* also scores under live hazard pressure but
  uses independently steered ship and gun, a finite player-triggered bomb
  stock and projectile collisions. Here the player's own continuous stroke
  can cross a bomb, and misses debit chance without killing an avatar.
- *Fruit Ninja Kinect* uses body movement and a distinct platform interface;
  its later rule descriptions corroborate but do not define this iPhone build.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-537` | continuous touchscreen path geometry |
| System Behaviour | `SYS-004`, `SYS-1069`, `SYS-1071`–`SYS-1074` | launch distribution, critical odds, 100-point recovery |
| Constraint | `CON-113`, `CON-183` | three outstanding misses, instant bomb loss |
| Information | `INF-399` | current moving objects, score and miss marks |
| Objective | `OBJ-002` | higher accumulated score |
| Time | `TIM-003` | uninterrupted object flight |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `400` (`GAME-0001`–`GAME-0400`).
- Exact genome matches: none.
- Tied near matches: `GAME-0400` — Geometry Wars: Retro Evolved (`4 / 23 = 0.173913`).
- Supported combination subsets: none.
- Scan date: 2026-09-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0400` — Geometry Wars: Retro Evolved | `SYS-1069`, `CON-183`, `OBJ-002`, `TIM-003` | Both score under uninterrupted pressure, can recover finite chances at score milestones and eventually lose the run when the allowance is exhausted. Geometry Wars steers a ship, fires projectiles, spends a separate limited bomb and scores kills with a life-local multiplier. Fruit Ninja draws one finger path through moving fruit, gains one-stroke group points, loses a chance for uncut fruit and immediately fails when that path crosses a bomb; its bomb is not a player resource. | Tied near, `0.173913` |

## Taxonomy impact

- Registry changes: six Active genes: `ACT-537`, `SYS-1071`–`SYS-1074`
  and `INF-399`.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_139`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_139.md).
- Candidate terms affected: live slicing stroke, mixed fruit/bomb launches,
  path intersection, one-swipe scoring, missed-fruit debit and visible state.

## Negative results

- None: no earlier signature or verified combination is revised.

## Delta summary

## New facts

- [Confirmed | Direct | High] Original iPhone version 1.2 explicitly adds
  three-or-more-fruit single-swipe bonuses to Classic (`FN-001`, `FN-004`).

## New genes

- [Observation | Corroborated | Medium] Six distinctions isolate the path,
  launched objects, cut response, group scoring, missed-fruit debit and live
  information display without treating touch hardware itself as a gene.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_139` adds six bounded
  genes without modifying earlier signatures.

## New questions

- Does an inspected paid iPhone v1.2 binary restore a spent mark at every
  100-point crossing exactly as later documented Classic builds do, and how
  does it order a same-frame miss, recovery, critical and bomb contact?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0402` *The Oregon Trail*.
- Optimisation criterion: change from real-time gesture score survival to
  resource-planning decisions in a historically distinct Apple II context.
- Expected information gain: compare a live spatial risk/reward gesture with
  a journey whose scheduled events and finite supplies unfold across turns.
- Backlog impact: no selected subject displaced.

## Why this game

- [Hypothesis | Limited | Medium] A globally recognisable mobile game supplies
  an unusually legible test of continuous touch-path geometry: its scoring
  opportunity and immediate hazard share the same gesture, rather than a
  separate movement or attack button.
