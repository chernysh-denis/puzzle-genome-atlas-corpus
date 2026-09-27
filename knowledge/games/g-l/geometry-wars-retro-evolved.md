---
game_id: GAME-0400
slug: geometry-wars-retro-evolved
game_title: "Geometry Wars: Retro Evolved"
analysis_status: reviewed
reviewed: 2026-09-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-536
  system:
    - SYS-215
    - SYS-911
    - SYS-1066
    - SYS-1067
    - SYS-1068
    - SYS-1069
    - SYS-1070
  constraint:
    - CON-183
    - CON-694
  information:
    - INF-398
  objective:
    - OBJ-002
  time:
    - TIM-003
---

# Game: Geometry Wars: Retro Evolved

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Ship silhouettes,
enemy colours, exact score values, stick directions and the grid effect are
carrier parameters, not separate genes.

## Analysis scope

- Version / ruleset: the original 2005 Xbox 360 Xbox Live Arcade release of
  *Geometry Wars: Retro Evolved*, **Evolved** single-player mode, using its
  ordinary controller mapping. The Xbox listing explicitly distinguishes the
  original Retro mode from Evolved. This packet does not transfer Geom-pickup
  scoring from *Retro Evolved 2*, or rules from the PC port. The exact binary
  revision was not inspected.
- Structured analysis target: Xbox 360 Evolved mode; see `GAME-0400` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: begin one ordinary Evolved score-attack run at zero score with the
  initial ship, three lives and three bombs, before the first hostile contact.
- Primary decision loop: steer the ship with the left stick while independently
  directing continuous fire with the right; read the local moving viewport,
  avoid incoming geometric enemies, destroy targets to raise the score and
  current-life kill multiplier, decide whether a finite bomb is worth spending
  to survive a crowd, and adapt to new hostile groups and score-triggered
  weapon, life and bomb awards.
- Terminal: the run ends when a lethal contact exhausts the remaining life
  stock; the retained run score can be evaluated as a high-score attempt.
  There is no fixed winning score or finite last wave. A score milestone may
  extend the run before that terminal. Reaching an achievement threshold or
  uploading a leaderboard entry is not the terminal used here.
- Included: free two-axis movement and independent directional fire; live
  projectile and enemy contact; several motion classes including direct
  pursuers and the black-hole hazard; continuing enemy arrivals with increasing
  pressure; score by target class; a kill-count multiplier belonging to the
  current life; a finite bomb whose effect is limited to the visible screen
  and gives no kill points; three initial lives and bombs; life-spending
  respawn; repeated score milestones for weapon forms, life and bomb stock;
  local camera visibility and a continuing real-time arena.
- Excluded: the separate original Retro mode; *Retro Evolved 2* and its Geom
  pickups; PC controls and later releases; online leaderboard eligibility;
  achievement chasing, exact high-score upload rules, other player's scores,
  unsupported precise spawn probabilities, every enemy's undocumented AI and
  exact order within simultaneous bomb/death/award frames. Black-hole
  projectile details are not promoted into a new gene without direct rule
  verification.
- Reproducible parameterisation: on an original Xbox 360 Evolved build, record
  the build identity, starting stocks and score, independent left/right-stick
  vectors, hostile appearances and camera position, each shot or bomb result,
  target score, live kill count and multiplier, 10,000-point gun transitions,
  75,000-point life and 100,000-point bomb awards, lethal contacts, respawns
  and final zero-stock result. Repeat to separate fixed milestones from
  variable hostile timing. The two contemporary written guides support this
  reconstruction but do not supply an input trace or exact binary behavior.
- Potential scoped modules: the original Retro mode, sequel modes and Geom
  collection, and leaderboard/achievement submission as separate interfaces.
- Direct-play status: none. No Xbox 360 executable, controller trace,
  screenshot, video or audio was inspected. The official Xbox listing
  establishes the product/mode distinction; two independent contemporary
  Evolved-only guides support the bounded rules and explicitly leave some
  internal scheduling unresolved.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GW-001` | The Xbox release includes distinct Retro and Evolved modes; this packet selects Evolved. | Confirmed | Direct | High | P1 |
| `GW-002` | Left stick moves the craft, right stick fires in its direction, and either trigger spends a bomb. | Observation | Corroborated | High | S1, S2 |
| `GW-003` | Evolved is a continuing score attack against live geometric enemies, not a last-wave clear. | Observation | Corroborated | High | P1, S1, S2 |
| `GW-004` | Enemy types and arrival groups change as a run progresses; exact spawn probabilities are not established. | Observation | Corroborated | Medium | S1, S2 |
| `GW-005` | Ship-fire kills increase a current-life multiplier; death loses that multiplier, while base target values still differ. | Observation | Corroborated | High | S1, S2 |
| `GW-006` | A bomb removes enemies on the visible screen without awarding their kill points; enemies outside the camera view may remain. | Observation | Corroborated | High | S1, S2 |
| `GW-007` | Score milestones change the active gun at 10,000-point intervals, add a life every 75,000 points and add a bomb every 100,000 points, subject to stock caps. | Observation | Corroborated | Medium | S1, S2, S3 |
| `GW-008` | Lethal contact consumes a life and restores play while stock remains; exhaustion ends the score run. | Observation | Corroborated | High | S1, S2 |
| `GW-009` | The exact algorithm choosing between upgraded guns, simultaneous-frame precedence and all hostile trajectories remain unverified. | Observation | Limited | High | S1, S2, R1 |

## Basic data

- Release / origin: Bizarre Creations' original Xbox Live Arcade game from
  2005, published by Microsoft. The current store title shortens the label to
  *Geometry Wars Evolved*, but its description names *Retro Evolved* and
  confirms that Retro and Evolved are separate modes.
- Platform or physical form: Xbox 360 with two thumbsticks and triggers;
  structured target `PLAT-XBOX-360`.
- Puzzle family: tactical forecast and counterplay (`FAM-009`); real-time
  system pressure (`FAM-010`). Survival depends on positioning, reading the
  live field and trading a bomb for the chance to preserve multiplier growth.
- Official source, checked 2026-09-25: **[P1]** [Xbox product
  listing](https://www.xbox.com/en-us/games/store/Geometry-Wars-Evolved/BP5G8K2M71PM),
  for publisher, developer, original release identity and the distinct
  Retro/Evolved mode boundary. It is not a detailed rules manual.
- Contemporary written Evolved guides, checked 2026-09-25:
  - **[S1]** [Byrdpire's 2005–06 Xbox 360 strategy
    guide](https://gamefaqs.gamespot.com/xbox360/930851-geometry-wars-retro-evolved/faqs/40235),
    sections 1.2–1.3 and 2.1–2.2, for controls, rewards, multiplier,
    enemies and black holes. The author marks the gun-choice formula as
    unknown and revises multiplier estimates; exact internal formula is not
    inferred.
  - **[S2]** [sleepyjack's independent April 2006 Xbox 360 Evolved
    guide](https://gamefaqs.gamespot.com/xbox360/930851-geometry-wars-retro-evolved/faqs/42425),
    Basics and Enemies, for independent controls, 75,000/100,000 score
    awards, 10,000-point gun changes, kill multiplier and limited bomb effect.
  - **[S3]** [Contemporary May 2006 Xbox 360
    review](https://bjorn3d.com/2006/05/geometry-wars-retro-evolved/),
    for the three starting lives and bombs, independent fire direction and
    the repeated life/bomb score intervals. This is an independent played
    description, not an inspected executable in this unit.
- **[R1]** Scope and direct-play audit in this record. Claim IDs:
  `GW-001`–`GW-009`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: steer the persistent craft freely within the arena.
- Existing `ACT-161`: keep the right stick aimed to emit projectiles toward
  current reachable threats; the aim vector can differ from movement.
- New `ACT-536`: spend an available bomb with either trigger during live play.
  The system's visible-screen clear and point exception belong to `SYS-1070`.
  Claims: `GW-002`, `GW-006`.

### System Behaviour Genes

- Existing `SYS-215`: shots, moving enemies and collisions resolve while
  control continues.
- Existing `SYS-911`: a lethal ship contact consumes one life and restores
  the controlled craft while reserve remains.
- New `SYS-1066`: continue releasing changing hostile groups into the same
  arena as the score run advances, without a finite wave-clear terminal.
- New `SYS-1067`: apply a per-life kill-count multiplier to scored shot kills
  and reset it after death. Target classes retain different base values.
- New `SYS-1068`: at recurring score steps, replace or retain a current gun
  form among the documented alternatives. The selection formula is unknown.
- New `SYS-1069`: independently add life and bomb stock at their recurring
  score milestones, respecting their caps, without spending score.
- New `SYS-1070`: remove enemies within the current visible screen after an
  accepted bomb command, while awarding no points for those removals;
  off-screen entities may survive. Claims: `GW-003`–`GW-008`.

### Constraint Genes

- Existing `CON-183`: the finite life stock permits continued play after
  ordinary loss and terminates the run on exhaustion.
- New `CON-694`: bomb activation requires positive finite bomb stock; spending
  it leaves ordinary movement and fire available, and later score awards can
  replenish it. This is not a terminal action budget. Claims: `GW-006`–`GW-008`.

### Information Genes

- New `INF-398`: the scrolling camera exposes the current local arena,
  craft, threats, score, multiplier and resource stocks, but a threat beyond
  its edge need not be shown before it enters view. The exact next spawn
  pattern is not previewed. Claim: `GW-004`, `GW-006`.

### Objective Genes

- Existing `OBJ-002`: maximise the run's accumulated score; no fixed
  threshold is a universal victory. Claim: `GW-003`.

### Time Genes

- Existing `TIM-003`: movement, fire, new enemies and collision continue
  while the player decides. Claims: `GW-002`–`GW-004`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Craft in open arena | steer left while holding right stick toward a right-side enemy | craft and projectile vectors differ in the same live interval | independent movement and fire | `GW-002` |
| A hostile enters the local view | continue firing toward it | a hit removes it, raises score by its class value and advances this life's kill count | scored combat and multiplier input | `GW-003`, `GW-005` |
| Kill count reaches an eligible multiplier step without death | settle the next scored kill | later shot kills use the increased multiplier | life-local scoring state | `GW-005` |
| An enemy crowd blocks the visible route and a bomb remains | pull either trigger | one bomb is spent and visible enemies clear without kill points; an off-view enemy may remain | emergency trade and viewport boundary | `GW-006` |
| Run score crosses the next 10,000-point interval | settle that award | current gun becomes or remains one documented upgraded form; exact selector is not asserted | score-driven weapon mode | `GW-007`, `GW-009` |
| Score first crosses 75,000 and 100,000 | settle each independent award | one life and one bomb respectively are added if below cap | repeated resource replenishment | `GW-007` |
| Craft contacts a hostile with life reserve | accept lethal contact | life stock falls, craft returns and multiplier starts over; run score continues | recoverable loss with broken multiplier | `GW-005`, `GW-008` |
| Craft contacts a hostile with no life reserve | accept lethal contact | Game Over stops live control and retains the score result | complete-run terminal | `GW-008` |

## Edge-case audit

- The viewport is not the entire playfield. A bomb is not asserted to erase an
  off-screen enemy; the two guides explicitly warn about that distinction.
- Bomb-cleared enemies give no kill points and therefore are not treated as
  ordinary scored shot kills. The sources do not establish a separate exact
  bomb/multiplier frame-order rule.
- Gun upgrades, life awards and bomb awards use separate score intervals.
  The 75,000 and 100,000 values are carrier parameters, not one universal
  threshold gene. The choice between upgraded gun types is unresolved.
- A death resets the multiplier, not the accumulated run score. A bonus life
  may extend the run, so the entry's three lives do not impose a three-death
  hard maximum.
- The scrolling view makes full-state visibility (`INF-001`) wrong here.
  Future spawns also cannot be treated as concealed objects already fixed at
  entry.
- Black holes can alter local threat and shot opportunities, but their exact
  accumulation and projectile-release sequence is not promoted from one
  guide's unverified estimates into a distinct active gene.

## Strategic and experiential structure

- Local decision: keep moving away from collision while firing in a different
  direction; choose a gap or a bomb when the visible crowd closes.
- Medium-term planning: build a multiplier by preserving the current life,
  then use bombs before a likely lethal contact rather than hoarding them for
  a run that may end.
- Long-term structure: higher score supports lives, bombs and gun forms but
  also coincides with denser and less predictable pressure. This is a score
  attack, not a fixed encounter-clear puzzle.
- Failure attribution: direct contact, a spent bomb and a broken multiplier
  are legible local events; future group timing and the gun-choice formula
  are not fully knowable from the cited guides.
- Player trust: the game should not be described as awarding points for bomb
  kills or exposing the whole field when the camera hides some enemies.

## Replay and variation

- Enemy types, arrival position and the active gun form can differ between
  runs; exact sampling rules remain outside this source-bounded packet.
- Both firing and movement directions remain freely chosen under the same
  live enemy pressure, yielding different survival paths and multipliers.
- A new run is motivated by a higher final score rather than a fixed ending.

## Adjacent systems and history

- The Xbox store distinguishes the original Retro game from Evolved; this
  unit is Evolved, not a blended franchise signature.
- *Vampire Survivors* also survives hostile arrivals, but its weapon events
  resolve automatically by cooldown rather than a separately aimed right
  stick. *Space Invaders* also awards extra lives from score, but its player
  shot points only upward from one lower lane and its rack has a clear terminal.
- *Retro Evolved 2* Geom collection changes the multiplier mechanism and is
  excluded. Claim IDs: `GW-001`–`GW-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-536` | independent sticks and trigger input |
| System Behaviour | `SYS-215`, `SYS-911`, `SYS-1066`, `SYS-1067`, `SYS-1068`, `SYS-1069`, `SYS-1070` | enemy forms and score intervals |
| Constraint | `CON-183`, `CON-694` | three initial lives and bombs, stock caps |
| Information | `INF-398` | scrolling viewport and visible counters |
| Objective | `OBJ-002` | maximum score |
| Time | `TIM-003` | continuous live input |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `399` (`GAME-0001`–`GAME-0399`).
- Exact genome matches: none.
- Tied near matches: `GAME-0360` — Space Invaders (`7 / 22 = 0.318182`).
- Supported combination subsets: none.
- Scan date: 2026-09-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0360` — Space Invaders | `ACT-008`, `ACT-161`, `SYS-215`, `SYS-911`, `CON-183`, `OBJ-002`, `TIM-003` | Both directly move and fire at live hostiles, can lose a finite life and retain a score under real-time pressure. Space Invaders is constrained to a lower horizontal lane, one upward projectile channel and a finite 55-invader rack with cover erosion and next-rack rebuild. Evolved independently aims in any direction within a roaming arena, receives non-terminal enemy groups, grows a per-life multiplier and spends scoreless screen bombs while score repeatedly alters weapon and stock. | Tied near, `0.318182` |

- New genes: `ACT-536`, `SYS-1066`–`SYS-1070`, `CON-694`, `INF-398`.
- Classification result: `New gene`.
- Evidence and reasoning: the existing movement, aimed strike, live combat,
  respawn, life stock, score and time boundaries are reused. Separate control,
  response, replenishment and information boundaries prevent the core
  twin-stick score run from being flattened into genre alone.

### Preserved research notes

- New genes: `ACT-536`, `SYS-1066`–`SYS-1070`, `CON-694`, `INF-398`.
- Classification result: `New gene`.
- Evidence and reasoning: the existing movement, aimed strike, live combat,
  respawn, life stock, score and time boundaries are reused. Separate control,
  response, replenishment and information boundaries prevent the core
  twin-stick score run from being flattened into genre alone.

## Taxonomy impact

- Registry changes: eight Active genes as listed above.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_138`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_138.md).
- Candidate terms affected: Evolved arena spawn, bomb, multiplier, gun form,
  score awards and scrolling visibility.

## Negative results

- None: no earlier canonical claim or combination is rejected.

## Delta summary

## New facts

- [Observation | Corroborated | High] Independent twin-stick fire, finite
  screen-limited bombs and a kill-count multiplier coexist in one Evolved
  score run (`GW-002`, `GW-005`, `GW-006`).

## New genes

- [Observation | Corroborated | Medium] Eight bounded distinctions isolate
  the emergency input, open-ended spawn pressure, multiplier, score awards,
  bomb response and local visibility.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_138` adds the eight
  bounded genes without mutating an older signature.

## New questions

- What exact internal rule selects the upgraded firing form at each score
  interval, and what is the exact order if a bomb, contact and milestone occur
  on one simulation frame? The guides do not settle those points.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0401` *Fruit Ninja*.
- Optimisation criterion: move from twin-stick survival fire to one mobile
  touch gesture whose path intersects fruit, bombs and an explicit round rule.
- Expected information gain: tests whether a continuous gesture can be
  represented without importing the bomb-stock and projectile boundaries of
  this arena.
- Backlog impact: no selected subject displaced.

## Why this game

- [Hypothesis | Limited | Medium] An open-ended score attack on Xbox 360 tests
  a control-and-reward loop absent from the immediately previous companion
  escape, while retaining enough movement, combat and survival genes to make
  comparisons interpretable.
