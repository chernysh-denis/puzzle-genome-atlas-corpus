---
game_id: GAME-0276
slug: forza-horizon-5
game_title: Forza Horizon 5
analysis_status: reviewed
reviewed: 2026-09-08
combination_ids: []
gene_ids:
  action:
    - ACT-044
    - ACT-290
  system:
    - SYS-320
    - SYS-515
    - SYS-516
    - SYS-519
  constraint:
    - CON-438
  information:
    - INF-204
    - INF-205
    - INF-208
  objective:
    - OBJ-134
  time:
    - TIM-003
---

# Game: Forza Horizon 5

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1551360`, Standard Edition offered through packages `547831`, `596608` and
  `596609`, observed against public branch build `21856128`, whose branch record
  was updated 2026-02-17; checked 2026-09-08. The publisher does not give that
  branch a semantic client version, so **no semantic version is asserted**.
- Product boundary: this is **Forza Horizon 5** on Windows, not `GAME-0171`
  Forza Horizon 6. All fifty-two separately listed DLC apps are outside the
  packet.
- Platform, input and fixed setup: English interface, Windows, controller or
  keyboard, offline Solo, stock `2020 Toyota GR Supra`, `Average` Drivatar
  difficulty, `Anti-Lock On` braking, `Simulation` steering, traction control
  on, stability control off, automatic shifting, full driving line, cosmetic
  damage, Rewind on and Offline Game Speed at `100%`. Those selections are
  frozen before the grid and are setup parameters, not actions inside scope.
- Event: the ordinary `Horizon Presents` Solo form of **Horizon Mexico Circuit**,
  a `2.0 mi / 3.2 km` Road Racing route run for three laps. The route identity,
  car, profile, current weather and reward amounts are parameters.
- Entry: accept control on the starting grid, after the car, event and settings
  have already been selected.
- Primary decision loop: read speed, gear, driving line, current place, lap and
  checkpoint progress and nearby rivals; steer, accelerate and brake the stock
  car through each required checkpoint in order; decide whether a mistake is
  worth rewinding to a retained earlier state; resume from the chosen state and
  continue against the autonomous field until the three-lap finish settles.
- Positive terminal: cross the valid finish in first place, pass through the
  result transition, retain the credited race result and return to free roam.
- Negative terminal: a lower classified finish still settles and may still pay
  credits or experience, but it fails this packet's first-place objective;
  restart or abandonment before a classified finish produces no accepted
  terminal for the packet.
- Included: direct control of one fixed car; simulated steering, traction,
  surface contact and cosmetic collision response; difficulty-scaled Drivatars;
  ordered checkpoint, lap and finish validation; optional use of Rewind at least
  once; the live driving and race-progress surfaces; final result and retained
  reward settlement; uninterrupted real-time input.
- Excluded: choosing the car, changing the difficulty or assists, choosing or
  entering the event, its campaign unlock and its pre-entry card because all
  occur before the declared grid entry; online play; Rivals; championships;
  seasonal and Festival Playlist content; EventLab and community creations;
  expansions, car packs and all DLC apps; tuning, upgrades and liveries; every
  other route, class and discipline; the rest of the open world; Accolade,
  Wheelspin and account-progression optimisation; screenshots, official art,
  third-party visual assets, video and audio evidence.
- Reproducible parameterisation: install the English Windows Steam app, confirm
  the branch build, use a profile that has completed the onboarding and retains
  the stock starter Supra, select Horizon Mexico Circuit's ordinary Solo event,
  freeze the stated profile, enter the grid, use Rewind at least once, finish
  first, dismiss the result transition and confirm free-roam control with the
  result retained. The route remains the same across seasonal conditions; no
  time or payout comparison is asserted across seasons.
- Potential scoped modules: pre-entry vehicle/event selection; Horizon Adventure
  and its Accolade gates; a seasonal championship; Rivals; EventLab; a different
  racing discipline; tuning and upgrades; the expansions.
- Direct-play status: not conducted. Valve data and the Steam offer establish
  lawful availability and exact product identity. Current Forza Support and
  publisher-authored textual pages establish configurable offline assists,
  Drivatar difficulty, starter-car retention, Road Racing access, autonomous
  Drivatars, race checkpoints, event rewards and post-event continuation.
  Current route references establish the named route and three-lap geometry;
  complete written secondary sources corroborate the fixed settings, race
  payouts and Rewind. No audiovisual source was opened, played, heard, analysed
  or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FH5-001` | Steam app `1551360` is the current lawfully offered Windows product, sold through three packages with fifty-two separately listed DLC apps and single-player plus online categories | Confirmed | Direct | High | P1 |
| `FH5-002` | Its public branch carries build `21856128`, updated 2026-02-17, while no semantic client version is attached to that branch | Observation | Corroborated | Medium | S1, P1 |
| `FH5-003` | The 2020 Toyota GR Supra is one of three starter cars retained in the player's garage, making a stock base-game instance reproducible without DLC or purchase | Confirmed | Direct | High | P3, P5 |
| `FH5-004` | Horizon Mexico Circuit is an ordinary `2.0 mi / 3.2 km` Road Racing route; its standard circuit form has three laps | Observation | Corroborated | High | P6, S2 |
| `FH5-005` | Offline play exposes difficulty, driving assists, Offline Game Speed, driving line/HUD controls and Drivatar settings; the declared profile is fixed before grid entry | Confirmed | Direct | High | P2, S3 |
| `FH5-006` | During a Solo race the system drives a Drivatar field, resolves the controlled car continuously and validates progress through ordered checkpoints and laps | Observation | Corroborated | High | P3, P4, P5, S2 |
| `FH5-007` | Enabled Rewind restores an earlier race state so the player can resume and revise a mistake | Observation | Corroborated | Medium | P7, S4 |
| `FH5-008` | A classified finish exposes the result and transfers persistent race credits/experience; first place is this packet's success predicate, while lower places may still pay | Observation | Corroborated | High | P3, P4, S3, S5 |
| `FH5-009` | Dismissing the completed event returns control to the retained open-world state, from which the same event can be replayed | Observation | Corroborated | Medium | P3, S3 |
| `FH5-010` | From the grid onward the bounded event needs twelve existing genes; six pre-entry candidate actions, constraints and disclosures are outside the declared interval, and the place-threshold objective must be replaced by the existing first-place objective | Strong Pattern | Corroborated | High | `FH5-004`–`FH5-009`, V1 |

## Basic data

- Release / origin: developed by Playground Games and published by Xbox Game
  Studios; released 2021-11-08 on Steam.
- Platform or physical form: lawfully offered Windows Steam application
  `1551360`; one offline Solo Road Racing circuit.
- Puzzle family: physics and object manipulation; real-time system pressure;
  ordered dependency sequencing.
- Primary and official textual sources, accessed 2026-09-08:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=1551360&cc=ua&l=english),
    for exact title, app, Windows support, developer, publisher, release date,
    categories, three packages and fifty-two DLC apps.
  - **[P2]** [Forza Horizon 5 Accessibility Support](https://support.forza.net/hc/en-us/articles/46523995129747-Forza-Horizon-5-Accessibility-Support),
    for offline game speed, difficulty, assists, Tourist Drivatars, driving-line
    and HUD configuration, PC inputs and language selection.
  - **[P3]** [First Drive: A Forza Horizon 5 Starting Guide](https://forza.net/news/forza-horizon-5-first-drive),
    for the retained starter Supra, checkpoint-based first event, completion
    reward, post-event continuation, map access and replayable rewarded events.
  - **[P4]** [Forza Horizon 5 gameplay FAQ](https://support.forza.net/hc/en-us/articles/4410404129811-Forza-Horizon-5-gameplay-FAQ),
    for race/event Accolades and the campaign condition that exposes the wider
    Road Racing set.
  - **[P5]** [Road to Mexico — August update](https://forza.net/news/forza-horizon-5-road-to-mexico-august-update),
    for starter-car retention, Drivatars in Solo race events and configurable
    cosmetic versus simulation damage.
  - **[P6]** [FH5 Routes and Events](https://forums.forza.net/t/fh5-routes-and-events/773135),
    a maintained official-community resource that classifies Horizon Mexico
    Circuit under Road Racing and gives its `2.0 mi / 3.2 km` length.
  - **[P7]** [FH5 Fixed Issues](https://support.forza.net/hc/en-us/articles/4418548807699-FH5-Fixed-Issues),
    for the product's race Rewind system as an independently named gameplay
    mechanism.
- Corroborating complete textual sources, accessed 2026-09-08:
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/1551360),
    for public build `21856128` and its branch timestamp; a secondary
    distribution observation.
  - **[S2]** [Guides4Gamers Road Racing event list](https://guides4gamers.com/forza-horizon-5/pois/road-racing-events/),
    for Horizon Mexico Circuit's three laps and matching route length.
  - **[S3]** [GamesRadar's complete settings guide](https://www.gamesradar.com/forza-horizon-5-tips/),
    for the named fixed profile options, difficulty-scaled credit modifier,
    replayability and persistent Accolade/reward context.
  - **[S4]** [Gamer Journalist's restart guide](https://gamerjournalist.com/how-to-restart-in-forza-horizon-5/),
    for Rewind as the local alternative that revises a race mistake.
  - **[S5]** [GameSpot's credits guide](https://www.gamespot.com/articles/how-to-earn-credits-in-forza-horizon-5-best-ways-to-earn-money-fast/1100-6497721/),
    for race credits and experience settling at any classified place rather
    than only first, which calibrates the packet's negative terminal.
- Reproducible control: **[V1]** repository-side transition trace over the
  complete textual sources under the declared app, build, event, stock car,
  profile, grid entry, first-place terminal and exclusions; rules reasoning,
  not direct play.
- Claim IDs: `FH5-001`–`FH5-010`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-290`: directly steer, accelerate and brake the fixed car from
  grid to finish.
- Existing `ACT-044`: while Rewind is enabled, restore a retained earlier race
  state and resume with a different intervention.
- `ACT-291`, `ACT-292` and `ACT-293` are rejected here. Car selection, profile
  configuration and event commitment occur before the declared grid entry;
  their fixed outcomes are parameters, not in-scope actions.
- Claims: `FH5-005`–`FH5-007`.

### System Behaviour Genes

- Existing `SYS-320`: integrate the operated car's steering, acceleration,
  traction, road contact, collision and cosmetic-damage state.
- Existing `SYS-515`: continuously drive the rival Drivatar field around the
  same route at the fixed opponent difficulty.
- Existing `SYS-516`: accept progress through the ordered checkpoints and three
  laps, then settle elapsed time and the complete finish order.
- Existing `SYS-519`: record the classified driving-event result and transfer
  its declared credits, experience and completion state into persistent data.
- Resolution order: live vehicle and rival motion produces checkpoint progress;
  Rewind may restore an earlier simulation state; a valid final checkpoint and
  finish settle place/time; the event transfers rewards and returns control.
- Claims: `FH5-006`–`FH5-009`.

### Constraint Genes

- Existing `CON-438`: the finish is valid only after the fixed car crosses every
  required checkpoint in sequence and completes all three laps.
- `CON-437` and `CON-439` are rejected. Vehicle admission and campaign unlock
  are satisfied before the grid and are frozen setup conditions.
- Scarce resources: racing line, remaining route distance and recoverable recent
  history; no consumable fuel or finite Rewind stock is asserted.
- Claims: `FH5-004`, `FH5-006`, `FH5-007`.

### Information Genes

- Existing `INF-204`: the driving view exposes speed, gear and authored route
  guidance needed to judge steering and braking.
- Existing `INF-205`: the race surface exposes place, lap/checkpoint progress,
  time and nearby rivals.
- Existing `INF-208`: the post-finish transition exposes the classified result
  and retained race rewards.
- `INF-206` is rejected because the event card is consumed before grid entry.
- Claims: `FH5-005`, `FH5-006`, `FH5-008`.

### Objective Genes

- Existing `OBJ-134`: finish the finite rival race first and retain the
  classified result and disclosed reward.
- `OBJ-150` is rejected: it requires a disclosed multi-place acceptance set and
  progression marker. No such threshold is established for this ordinary event;
  lower classified places remain settled and rewarded but fail this packet's
  chosen first-place success predicate.
- Claims: `FH5-008`–`FH5-010`.

### Time Genes

- Existing `TIM-003`: player input, car motion and the rival field advance in
  real time until Rewind or the finish transition suspends the live interval.
- Claims: `FH5-005`–`FH5-008`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| The fixed stock Supra and autonomous field wait on the Horizon Mexico Circuit grid | Accept control and accelerate | The car responds directly while the Drivatar field begins the same three-lap route at the fixed difficulty | direct vehicle control and autonomous field | `FH5-005`, `FH5-006` |
| A required checkpoint approaches | Steer through its gate | The ordered progress state advances; bypassing the gate does not advance the accepted route | checkpoint legality | `FH5-004`, `FH5-006` |
| A corner error has put the car off line | Invoke Rewind, choose the retained prior state and resume | The earlier simulation state returns and live racing continues from it | retained-history revision | `FH5-007` |
| The final lap is active and every prior checkpoint is accepted | Cross the remaining checkpoints and finish | The course validator accepts the finish and settles elapsed time plus the complete order | finite race result | `FH5-006` |
| The valid classified result is first place | Continue through the result transition | First-place completion and race rewards are retained | positive terminal | `FH5-008` |
| The valid classified result is below first | Continue through the same transition | The event and its payout may still persist, but this packet's first-place objective is false | bounded negative terminal | `FH5-008` |
| The result transition is complete | Dismiss it | Control returns to free roam with the result retained and the route available for a separate replay | retained return | `FH5-009` |

## Strategic and experiential structure

- Planning horizon: all car, event and profile choices are fixed before entry,
  so the in-scope problem is line selection and recovery rather than loadout
  optimisation.
- Local tactics: brake and turn against the visible driving line and rival
  positions; Rewind changes whether a bad corner is accepted or revised.
- Medium-term structure: maintain legal checkpoint order through three laps
  while converting local overtakes into a first-place final state.
- Reversible versus irreversible: an enabled Rewind can revise recent driving;
  the classified result becomes fixed once its transition settles.
- Failure attribution: speed/gear, driving line, place, lap progress and visible
  rivals distinguish a bad line, missed checkpoint and insufficient pace.
- Player trust: the named route and fixed profile remain stable even though
  seasonal weather may vary; no seasonal reward or Playlist gate enters the
  terminal.

## Replay and variation

- What changes: driving line, overtaking order, collisions, exact Rewind point,
  finish time, place and season-dependent surface condition.
- Randomness or procedural generation: the course and lap count are authored;
  rival behaviour varies within its Drivatar rules. No procedural route claim
  enters the packet.
- Multiple viable strategies: a clean conservative line or a riskier line with
  a corrective Rewind can both produce first place.
- Typical replay motive: improve finish time or achieve first place after a
  lower classified result.

## Adjacent systems and history

- Direct predecessors: earlier Forza Horizon games; none supplies evidence for
  this product's scoped event.
- Variants: campaign openings, Rivals, seasonal championships, online races,
  EventLab, other disciplines and expansions are separate packets.
- Similar games: `GAME-0217` Need for Speed Underground is the selected nearest
  neighbour. `GAME-0171` Forza Horizon 6 shares the event core but its reviewed
  packet includes a much larger campaign-opening and festival-threshold layer.
- Important differences: Need for Speed Underground lacks Rewind but adds a
  pre-race difficulty commitment and event-card disclosure inside its earlier
  entry boundary. Forza Horizon 5 enters only at the grid, fixes those choices
  as parameters and makes recent race state revisable.
- Claims: `FH5-006`–`FH5-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-044`, `ACT-290` | Rewind point, control binding and stock car are parameters |
| System Behaviour | `SYS-320`, `SYS-515`, `SYS-516`, `SYS-519` | field size, difficulty, lap count, handling and reward values are parameters |
| Constraint | `CON-438` | route, checkpoint order and lap count are parameters |
| Information | `INF-204`, `INF-205`, `INF-208` | HUD styling and exact fields are presentation parameters |
| Objective | `OBJ-134` | event, first place and retained reward values are parameters |
| Time | `TIM-003` | physics and input cadence are implementation parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `275` (`GAME-0001`–`GAME-0275`).
- Exact genome matches: none.
- Tied near matches: `GAME-0217` — Need for Speed Underground (`11 / 15 = 0.733333`).
- Supported combination subsets: none.
- Scan date: 2026-09-08.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0217` — Need for Speed Underground | `ACT-290`, `SYS-320`, `SYS-515`, `SYS-516`, `SYS-519`, `CON-438`, `INF-204`, `INF-205`, `INF-208`, `OBJ-134`, `TIM-003` | Both directly drive one fixed car against autonomous rivals through ordered laps into a first-place result and retained reward. Underground admits its pre-race difficulty commitment and event disclosure because its packet begins before the event; this packet begins on the grid, so those are frozen parameters. Horizon instead adds `ACT-044`: the player can restore a recent race state and revise the line without restarting the event. | Near, `11 / 15 = 0.733333` |

- Reused genes: `ACT-044`, `ACT-290`, `SYS-320`, `SYS-515`, `SYS-516`,
  `SYS-519`, `CON-438`, `INF-204`, `INF-205`, `INF-208`, `OBJ-134`,
  `TIM-003`.
- Classification result: `New combination of known genes`.
- Evidence and reasoning: independent review removes six pre-entry boundaries,
  replaces the unsupported multi-place objective with the existing
  first-place-and-reward objective and admits no new gene. The result is not a
  subset of Forza Horizon 6 because the two packet objectives differ.

### Preserved research notes

- Reused genes: `ACT-044`, `ACT-290`, `SYS-320`, `SYS-515`, `SYS-516`,
  `SYS-519`, `CON-438`, `INF-204`, `INF-205`, `INF-208`, `OBJ-134`,
  `TIM-003`.
- Classification result: `New combination of known genes`.
- Evidence and reasoning: independent review removes six pre-entry boundaries,
  replaces the unsupported multi-place objective with the existing
  first-place-and-reward objective and admits no new gene. The result is not a
  subset of Forza Horizon 6 because the two packet objectives differ.
- Reused genes: twelve; no new ID.
- Evidence and reasoning: the live race core is highly recurrent, while Rewind
  is the only signature boundary absent from the selected Need for Speed packet.

## Taxonomy impact

- Registry changes: add this reviewed decomposition as an independent carrier
  for twelve existing Active genes. No canonical label or definition changes.
- Taxonomy-change record: none. No split, merge, deprecation, lifecycle change,
  wording generalisation or earlier reviewed signature change.
- Draft correction: remove `ACT-291`, `ACT-292`, `ACT-293`, `CON-437`,
  `CON-439` and `INF-206` because they occur before grid entry; replace
  `OBJ-150` with `OBJ-134` because the evidence establishes no accepted
  multi-place threshold.
- Candidate terms affected: event name, car, settings, difficulty, lap count,
  route length, weather and reward values remain game-scoped parameters.

## Negative results

- The draft's unnamed “ordinary road-racing event” was not reproducible. It is
  replaced by Horizon Mexico Circuit's ordinary three-lap Solo packet.
- The six pre-entry candidate genes are valid elsewhere but not within this
  grid-to-settlement interval. Their removal is a scope correction, not a
  taxonomy finding.
- `OBJ-150` was rejected rather than stretched: its accepted-place set and
  progression-marker requirements are not evidenced here. A lower place can
  still settle and pay, so it is only a negative terminal relative to the fixed
  first-place objective.
- The claim that all draft genes formed a strict subset of Forza Horizon 6 was
  false: the two records use different objectives. The corrected signature
  shares eleven of twelve genes with that later instalment but is not its subset.
- No new combination is recorded: no reviewed combination is a strict subset of
  the corrected signature.
- Seasonal weather can alter handling, but the authored route, ordered progress
  and terminal remain reproducible. No cross-season time or payout equality is
  claimed.
- No video or audio evidence was used.

## Delta summary

## New facts

- [Strong Pattern | Corroborated | High] `FH5-004`–`FH5-010`: the exact
  three-lap Horizon Mexico Circuit packet is a grid-to-settlement racing core,
  with recent state revision as its only boundary absent from the nearest
  Need for Speed genome.

## New genes

- [Observation | Corroborated | High] `No new genes`; all twelve admitted
  boundaries reuse Active lower-ID genes.

## New combinations

- [Observation | Direct | High] `No new combinations`.

## Taxonomy changes

- [Observation | Direct | High] `No taxonomy changes`; only this draft game's
  scope and signature are corrected.

## New questions

- Does a bounded seasonal championship add a portable multi-event scoring
  boundary after live-service rotation is frozen?
- Does Rivals replace the autonomous-field and first-place genes with a ghost
  comparison and retained-time threshold without changing course validation?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0277` — Cuphead.
- Optimisation criterion: leave racing for one authored multi-phase boss fight
  graded after completion.
- Expected information gain: test phase thresholds, parry legality and
  post-victory grading against the lower-ID corpus.
- Backlog impact: advances the recorded 271-to-279 closure horizon by one unit.

## Why this game

- [Strong Pattern | Corroborated | High] The selection asked which racing genes
  remain portable inside one ordinary event and which live-service layers sit
  outside it. The corrected packet isolates the complete grid-to-result core,
  excludes every pre-entry and seasonal boundary, and shows that Rewind—not
  festival economy—is its informative distinction from the nearest neighbour.
