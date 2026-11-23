---
game_id: GAME-0561
slug: psychonauts-2
game_title: Psychonauts 2
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-190
    - ACT-295
    - ACT-341
    - ACT-356
    - ACT-438
    - ACT-680
  system:
    - SYS-036
    - SYS-037
    - SYS-045
    - SYS-051
    - SYS-215
    - SYS-369
    - SYS-380
    - SYS-398
    - SYS-578
    - SYS-755
    - SYS-1049
    - SYS-1363
    - SYS-1386
    - SYS-1631
    - SYS-1632
  constraint:
    - CON-269
    - CON-282
    - CON-349
    - CON-556
    - CON-661
  information:
    - INF-115
    - INF-119
    - INF-268
    - INF-271
  objective:
    - OBJ-155
  time:
    - TIM-003
---

# Game: Psychonauts 2

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Raz, Loboto, Censor, Regret, Doubt, figments, dental scenery and the four
named PSI powers are carrier parameters, not additional gene types.

## Analysis scope

- Version / ruleset: released English native Xbox Series X|S campaign,
  August 2021 launch-rules profile; fresh one-player game, original controller
  mapping, base powers and no imported progress. The exact installed package,
  binary checksum and patch are unverified. No Fall Damage, Invincibility and
  Narrative Combat assists are disabled; their existence does not make them
  the selected rules. A preview, Xbox One compatibility session, Windows
  executable, cloud stream or later collection-cleanup profile is not the
  analysis target.
- Structured analysis target: the matching original Xbox Series X|S entry in
  `knowledge/platforms/games.json` records that evidence boundary, not a
  claim that every marketed port has been tested.
- Primary decision loop: read the current platform, enemy, power cue and
  health; steer, jump, dodge and lock onto compatible threats; choose PSI
  Punch, PSI-Blast, Telekinesis or Pyrokinesis for the current target; use
  a moved tooth, an opened zipper, a burnt cover or Levitation to make the
  next crossing possible; preserve mental health while satisfying the
  investigation's ordered traversal and combat gates.
- Entry and exit: first ordinary control following Loboto through the office
  after the opening introduction, then the entire fresh Loboto's Labyrinth:
  distorted office, falling-tooth section, Central Office, Conference Room,
  Poster Gallery, Dental Void, drain/ball run, Asylum encounter and ladder.
  Accept the closing mind sequence and jet debrief, and stop at first
  ordinary real-world Motherlobe arrival control before entering or exploring
  the headquarters. The final ladder is a chapter closeout, not an optional
  boss victory or proof of having identified the employer conclusively.
- Reproducible route: follow the taught movement and wall jumps; rescue
  Coach with the giant tooth, place it at the authored socket and pull the
  zippers; clear the Censors, use PSI-Blast on the uvula and Tooth Fairies,
  then address Regrets and their removable anvil; burn the route-blocking
  posters, cross the sinking teeth and fight the Doubts; use the base
  Levitation balloon and updrafts, then the ground ball through the drain;
  clear the final mixed group, cross the last supports and climb the ladder.
- Bounded side controls: contact visible figments and one healing pickup,
  retain incidental Psitanium, and reunite the first reachable Dufflebag tag
  with the Dufflebag. No complete collectible set or rank threshold is a
  terminal requirement. A safe miss can exercise the local hazard recovery;
  full health depletion is a separate checkpoint branch, not a life debit.
- Included: direct movement, camera-relative navigation, jump/double-jump,
  compatible dodge and selected-target lock; direct PSI attacks and active
  powers; inert prop pickup, held placement and launch, compatible scripted
  fixture operation; contextual power effects, burning and breakage, airborne
  float/updraft interaction, grounded ball movement and its declared
  electrical-floor protection; autonomous threats, combat, one mental-health
  pool and healing, surviving fall recovery, ordinary failure retry; moving
  and failing supports; contact acquisition and one typed baggage reunion;
  retained early abilities, ordered route/capability/target gates; local
  view, resource/power HUD, current instruction and held-object feedback.
- Excluded: complete Motherlobe exploration, Clairvoyance, Mental Connection,
  Time Bubble, Projection, later enemy classes or boss fights; Otto-Matic
  purchases, Pins, upgrade-credit allocation, PSI cards/cores, complete Intern
  Rank economy, later wallet expansion, Psi Pops and Dream Fluff; full memory
  vault slideshow collection, revisits, Nuggets of Wisdom, every baggage
  reunion and a compulsory 80/80 figment route; all-assist play, speed-run
  glitches, previews, full campaign and postgame cleanup. Visible incidental
  counters do not make the excluded shop/rank loop necessary for this terminal.
- Potential scoped modules: the headquarters upgrade economy; Hollis's
  thought rewiring; later time manipulation; Projection routes; full mind
  collectible completion and the campaign finale.
- Direct-play status: not conducted. Read Double Fine's official released-
  product, powers, enemies and accessibility pages. Inspected all nine static
  storyboard sheets of IGN Guides' 35:12 first-level recording at ten-second
  sampling, 160×90 source cells, including the office, tooth/zipper, battles,
  posters, float/ball passage, Asylum and returned real-world sequence. These
  sparse stills corroborate geometry, order and visible interfaces; they do
  not certify its platform, selected assists, package version, exact inputs,
  float lifetime or saved fields. No native executable, console, controller
  trace, save or frame-accurate failure experiment was inspected. No video or
  audio playback, foreground window or focus interception was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PN2-001 | The full release includes native Xbox Series consoles; the four early powers are available by the end of the first level. | Observation | Corroborated | High | P1, P2, P5, S1, V1 |
| PN2-002 | The fresh route progresses through office movement, tooth/zipper manipulation, staged combat, posters, Dental Void, ball passage and Asylum ladder. | Observation | Corroborated | High | S1, S2, V1 |
| PN2-003 | Compatible props can be remotely held, placed or thrown; anvil theft and fire susceptibility create target-dependent combat choices. | Observation | Corroborated | High | P2, P3, S1, S2, S4, V1 |
| PN2-004 | Base airborne Levitation has a short active interval outside updrafts; a rising stream sustains the float, while the ground ball has a different traversal role. | Observation | Corroborated | Medium | P2, S1, S3, S4, V1 |
| PN2-005 | Health is one mental-energy pool, with compatible healing and ordinary checkpoint restoration at depletion; no astral-layer stock is used. | Observation | Corroborated | High | P4, S1, S5, V1 |
| PN2-006 | A surviving water/void miss loses health and returns to recent support while already credited figments remain; exact complete rollback fields are unmeasured. | Observation | Corroborated | Medium | P4, S1, V1 |
| PN2-007 | Figments and a reachable typed baggage reunion can be credited, but a fresh full collectible/rank economy is not required or wholly accessible. | Observation | Corroborated | High | S1, S2, S3, S6, V1 |
| PN2-008 | The ladder closes the mental chapter and the ensuing debrief leads to real-world headquarters arrival; it is not Oleander's training invitation. | Observation | Corroborated | High | S1, S2, S6, V1 |
| PN2-009 | A terse secondary account's one-hit Regret, fall protection and first-tag shorthand must not override the detailed route, target, timing and assist qualifications. | Observation | Conflicting | Medium | P3, P4, S1, S2 |

## Basic data

- Release / origin: Double Fine Productions, Xbox Game Studios, 25 August
  2021. Native Xbox Series X|S full campaign, not an Early Access product.
- Platform or physical form: released Xbox Series digital console campaign;
  exact native package and checksum unverified, not falsely inferred from a
  current store update or a PC walkthrough.
- Puzzle family: physics and object manipulation; real-time system pressure;
  ordered dependency sequencing. Typed baggage is a bounded side control,
  not the principal reusable family of this platform-adventure packet.
- Primary sources, accessed 2026-11-19:
  - **P1** [Double Fine launch notice](https://www.doublefine.com/news/psychonauts-2-is-here),
    dated 25 August 2021; native Series X and the separate compatibility PS5
    release are distinguished by the publisher.
  - **P2** [official Basic Braining 2 — Psychic Powers](https://www.doublefine.com/games/psychonauts-2/updates/basic-braining-episode-2-psychic-powers),
    early PSI-Blast, Levitation, Pyrokinesis and Telekinesis and the later
    powers excluded here. Narrative retained knowledge does not imply every
    tutorial command is usable before its current introduction.
  - **P3** [official Basic Braining 5 — Enemies](https://www.doublefine.com/games/psychonauts-2/updates/basic-braining-episode-5-enemies),
    Censors, Regrets' removable weights and Doubts' flammable behaviour.
    Later enemies and upgrades on that page are not inherited.
  - **P4** [official accessibility features](https://www.doublefine.com/games/support/psychonauts-2/accessibility?platform=all),
    input options and separate No Fall Damage, Invincibility and Narrative
    Combat assists. Do not assume an uninspected recording's selected values.
  - **P5** [Xbox launch announcement](https://news.xbox.com/en-us/2021/06/13/psychonauts-2-launches-august-25-play-it-on-day-one-with-xbox-game-pass/),
    full-release date and Xbox Series X|S target.
- Independently authored corroboration, accessed 2026-11-19:
  - **S1** [dschepler, GameFAQs, version 1.0, 14 September 2021](https://gamefaqs.gamespot.com/pc/183898-psychonauts-2/faqs/79499/lobotos-labyrinth),
    complete first-level route and qualified float/recovery description.
    Its PC listing is not proof of native Xbox execution.
  - **S2** [Gamepressure, first-level route, 5 September 2021](https://www.gamepressure.com/psychonauts-2/lobotos-labryinth/z2ebd7),
    independently matching tooth, zipper, combat, fire and final-ladder gates.
    Its shorthand one-hit, protection and first-tag language is not taken universally; the earlier Dufflebag control follows S1 and the visible sequence.
  - **S3** [Neoseeker first-level route](https://www.neoseeker.com/psychonauts-2/walkthrough/Loboto%27s_Labyrinth),
    read indexed excerpts for electric-floor ball traversal, first-visit
    limits and four powers. Full page fetch was restricted; no full-page
    read is claimed.
  - **S4** [TrueAchievements general controls and base powers](https://www.trueachievements.com/game/Psychonauts-2/walkthrough/2),
    and [first-level instructions](https://www.trueachievements.com/game/Psychonauts-2/walkthrough/3),
    indexed excerpts for held prop use, selected-target lock and base ball
    versus float; full page access was restricted.
  - **S5** [Gamepressure health](https://www.gamepressure.com/psychonauts-2/heros-health/zfebc5),
    one pool, healing and latest-save recovery. Later capacity upgrades are
    excluded; exact damage constants are not assumed.
  - **S6** [successor-area boundary](https://gamefaqs.gamespot.com/pc/183898-psychonauts-2/faqs/79499/motherlobe-exploration),
    separates subsequent shop/rank/Clairvoyance lessons from this first mind;
    [independent first-visit limitation](https://video-game-guide-walkthrough.supersoluce.com/solution/psychonauts-2-guide-walkthrough/psychonauts-2-missions/lobotos-labyrinth/)
    corroborates that revisit completion is a different packet.
- **V1** [IGN Guides first-level recording](https://www.youtube.com/watch?v=1FwcF86sbu0),
  35:12, all nine static ten-second storyboard sheets inspected. Its metadata
  chapters are gameplay 03:41, Trashcan 06:50, Central Office 08:40,
  Conference Room 10:20, Poster Gallery 15:40, Dental Void 23:12 and Asylum
  26:15. Those are the recording's labels, not native benchmark timings.
- Claim IDs: PN2-001–PN2-009.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: steer, run, jump, wall-jump and climb the authored route.
- Existing `ACT-048`: retain and reposition an eligible inert tooth or prop.
- Existing `ACT-190`: address and commit the currently available psychic
  ability, including held preparation, fixture pull and base ball activation.
- Existing `ACT-295`: commit character-owned PSI Punch, aerial strike and
  PSI-Blast; these are not equipped firearm shots.
- Existing `ACT-341`: address a compatible fixture or reunite credited luggage
  with the matching baggage body.
- Existing `ACT-356`: request a compatible directional dodge rather than
  assume passive immunity or a universal safe frame window.
- Existing `ACT-438`: select an eligible threat to bind view and attack facing.
- Existing `ACT-680`: deploy the airborne balloon and steer its descent.
- No live opponent carry or force-integrated Gravity Gun is asserted from
  throwing an anvil. Claims: PN2-002–PN2-004, PN2-007.

### System Behaviour Genes

- Existing `SYS-036`: live body gravity, support and contact resolve traversal.
- Existing `SYS-037`: contact credits eligible figments, health and currency.
- Existing `SYS-045`, `SYS-051`: threats move and initiate compatible attacks
  without a new player command for each step or strike.
- Existing `SYS-215`: direct combat resolves eligible hits, damage and defeat.
- Existing `SYS-369`: health depletion restores the ordinary authored
  checkpoint; it is distinct from a surviving local miss.
- Existing `SYS-380`: selected powers apply their typed displacement, stun,
  damage-over-time, protection or movement effect. Telekinesis operates on
  admitted targets, Pyrokinesis burns compatible targets, and the ground ball
  serves the declared drain-floor crossing. None is universal immunity.
- Existing `SYS-398`: each early introduction leaves its taught capability
  usable for subsequent compatible route edges.
- Existing `SYS-578`: damage and healing update one mental-health pool.
- Existing `SYS-755`: compatible attacks or fire remove eligible breakables
  and route-covering posters, with their authored linked result.
- Existing `SYS-1049`: a sinking tooth or failing route support removes the
  current foothold and requires a continuing crossing; exact delays and reset
  periods are parameters, not a universal destruction simulation.
- Existing `SYS-1363`: moving/rotating supports change reachable departures
  while carrying a supported actor; boarding does not make every edge safe.
- Existing `SYS-1386`: the extra ordinary airborne jump is spent, then becomes
  available again on eligible support; no unmeasured wall reset is asserted.
- New `SYS-1631`: airborne balloon duration and sustaining updrafts differ
  from grounded ball movement and Noita's upward-thrust reserve.
- New `SYS-1632`: surviving a failed crossing returns to recent support with
  health loss and retained figments, rather than restoring a whole failed
  encounter or spending a life. Exact rollback fields remain source-limited.
- Claims: PN2-002–PN2-006, PN2-009.

### Constraint Genes

- Existing `CON-269`: active-power target, range, readiness and current-state
  prerequisites gate the requested effect; no shared mana pool is invented.
- Existing `CON-282`: ordered tutorial, combat and route predicates gate the
  investigation's continuation.
- Existing `CON-349`: the taught interaction capability and compatible input
  are required at its authored route edge.
- Existing `CON-556`: a remote manipulation must address an admitted target;
  a fixed structure or rejected foe is not automatically a portable prop.
- Existing `CON-661`: Dufflebag settlement accepts its matching luggage tag,
  not an arbitrary token or any other baggage type.
- Exact ranges, prompt buttons, recasts, sinking periods and backpack
  placement are parameters. Claims: PN2-001–PN2-004, PN2-007.

### Information Genes

- Existing `INF-115`: local view and cues reveal present threats and their
  relation to the navigable scene, not an omniscient future encounter list.
- Existing `INF-119`: HUD and current panels expose mental health, available
  powers, readiness and retained current collectible/resource counters.
- Existing `INF-268`: the current adviser and prompt identify the taught action
  and acknowledge the current predicate, not the complete future chain.
- Existing `INF-271`: psychic targeting and held-object response disclose
  acceptance, holding, release or rejection without proving exact impact math.
- Claims: PN2-002–PN2-007.

### Objective Genes

- Existing `OBJ-155`: survive the complete ordered mental action chapter,
  accept its final ladder/closing sequence and retain real-world successor
  control. Optional pickups, one encounter or mere level entry do not finish it.
- `OBJ-208` is rejected: this is an investigation, not a class-sensitive
  training gallery returning Sasha's next-training invitation. No new
  objective is needed because `OBJ-155` already fits. Claims: PN2-008.

### Time Genes

- Existing `TIM-003`: traversal, hostile attacks, sinking supports, active
  effects and the float interval resolve live outside pauses and cutscenes.
- Claims: PN2-002–PN2-006.

## Reproducible transitions

| Before | Action | Resolution | Distinction | Claim |
| --- | --- | --- | --- | --- |
| Coach beneath the large tooth | Address it with Telekinesis, then place it at its socket | Rescue and a usable authored stepping support | Retained prop and fixture role, not inventory crafting | PN2-002 |
| Closed compatible zipper | Pull it with the taught power | Authored passage opens | Tool/target compatibility, not arbitrary scenery deformation | PN2-003 |
| Combat Censor and nearby prop | Hold and launch the prop at the eligible target | Declared impact/stun effect resolves | Not proof of mass-scaled Gravity Gun damage or lifting the Censor | PN2-003 |
| Regret carries its weight | Address the weight with Telekinesis | Compatible weight becomes a held/throwable prop | Carrier equipment can be repurposed | PN2-003 |
| Chomping mouth blocks onward passage | PSI-Blast its compatible uvula | The authored opening permits continuation | No universal enemy weak-point percentage | PN2-002 |
| Tooth Fairies hold the route object | Defeat the required carriers | Dropped tooth or door makes the next route available | Not a permanent character weapon reward | PN2-002 |
| Required poster covers an opening | Prepare and apply Pyrokinesis | Compatible cover burns and the opening becomes usable | Not every painting or world surface must burn | PN2-003 |
| Base float active outside an updraft | Continue the crossing too long | Bounded floating support can expire | Held input is not endless flight | PN2-004 |
| Base float reaches an updraft | Remain in the eligible rising column | Airflow sustains the float and raises the crossing opportunity | Environmental support, not a purchased reserve refill | PN2-004 |
| Surviving avatar misses a void/water crossing | Accept local recovery | Health is debited, recent support is restored and credited figments remain | Partial recovery differs from zero-health checkpoint rollback | PN2-006 |
| Mental health reaches zero | Accept failure resolution | Latest authored save/checkpoint and its combat attempt are restored | No astral layer, finite life or currency death marker is established | PN2-005 |
| Dufflebag tag credited | Address its matching bag | That reunion settles | Neither an unmatched tag nor a full five-bag quota | PN2-007 |
| Final encounter and remaining supports cleared | Climb the Asylum ladder and accept closeout | Mental chapter and debrief settle into real-world arrival control | No mandatory first-level boss, full collectible set or next-mind play | PN2-008 |

## Strategic and experiential structure

- Local decision: choose timing, target and tool. A carried anvil, a flammable
  Doubt, a poster and a floating gap demand different legal effects.
- Medium horizon: learn the capability sequence, budget current health and
  decide whether an optional visible figment or matched bag merits a detour.
- Crossing heuristic: use current supports and updrafts; deploy float near
  its useful interval rather than assume sustained ascent from holding input.
- Combat heuristic: lock onto a reachable threat, dodge compatible attacks
  and exploit typed interactions instead of treating every enemy as a one-hit
  target or using every later power advertised by the studio.
- Failure attribution: separate a modest surviving crossing penalty from a
  complete encounter retry. Already credited figments do not justify claiming
  that every transient world state survives identically.
- Trust: accessibility alternatives are explicit selected rules, not hidden
  difficulty inference. Story protection and collecting every optional item
  must not be conflated with the chapter's actual completion predicate.
- Claims: PN2-002–PN2-009.

## Replay and variation

- The fresh route, four introductions, authored encounters and final ladder
  are fixed. Combat movement, target order and optional pickup detours vary.
- No procedural room generator, universal damage constant or random loot
  distribution is asserted. Later revisits fragment the mind differently and
  can expose additional collectibles; they are a separate scope.
- Claims: PN2-002–PN2-008.

## Adjacent systems and history

- Original Psychonauts separates later badges, point-valued figments and
  finite astral layers from this sequel's early abilities and chosen retry.
- Rhombus of Ruin is a separate VR product, not this native console packet.
- Headquarters shops, later powers, class lessons and mind revisits are
  deliberately not flattened into one whole-product union.
- Official power names remain literal source identifiers, not independent
  scientific or mental-health claims. Claims: PN2-001, PN2-005, PN2-007–PN2-009.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-008`, `ACT-048`, `ACT-190`, `ACT-295`, `ACT-341`, `ACT-356`, `ACT-438`, `ACT-680` | None; see scope and source limits. |
| System Behaviour | `SYS-036`, `SYS-037`, `SYS-045`, `SYS-051`, `SYS-215`, `SYS-369`, `SYS-380`, `SYS-398`, `SYS-578`, `SYS-755`, `SYS-1049`, `SYS-1363`, `SYS-1386`, `SYS-1631`, `SYS-1632` | None; see scope and source limits. |
| Constraint | `CON-269`, `CON-282`, `CON-349`, `CON-556`, `CON-661` | None; see scope and source limits. |
| Information | `INF-115`, `INF-119`, `INF-268`, `INF-271` | None; see scope and source limits. |
| Objective | `OBJ-155` | None; see scope and source limits. |
| Time | `TIM-003` | None; see scope and source limits. |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `560` (`GAME-0001`–`GAME-0560`).
- Exact genome matches: none.
- Tied near matches: `GAME-0254` — CONTROL Ultimate Edition (`18 / 46 = 0.391304`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0254` — CONTROL Ultimate Edition | `ACT-008`, `ACT-048`, `ACT-190`, `ACT-341`, `SYS-215`, `SYS-369`, `SYS-380`, `SYS-398`, `SYS-578`, `SYS-755`, `CON-269`, `CON-282`, `CON-556`, `INF-115`, `INF-119`, `INF-268`, `INF-271`, `TIM-003` | Both routes combine direct navigation, retained props, typed abilities, one health pool, authored retry and current manipulation feedback. CONTROL’s Federal Bureau packet uses an equipped firearm, reserve-limited combat and collision-bounded remote physics with attributed prop damage; the first mental labyrinth instead uses intrinsic PSI attacks, taught fire/zipper routes, short airborne float with updrafts, a ground ball, a matched baggage control and surviving hazard return with credited figments. Completion is the entire mental chapter and real-world arrival, not CONTROL’s designated site. | Tied near; `18 / 46 = 0.391304` |

### Preserved research notes

- New genes: two; thirty-two unchanged definitions reused.
- Classification result: New gene.

## Taxonomy impact

- Registry additions: `SYS-1631`, `SYS-1632` only.
- [Taxonomy Change 307](../../../research/taxonomy-changes/TAXONOMY_CHANGE_307.md)
  records both boundaries and the rejected alternatives.

## Negative results

- None as a separate prior-claim rejection. Scope exclusions and source
  disagreements above do not authorise changing an earlier accepted record.

## Delta summary

## New facts

- [Observation | Corroborated | High] The complete first mind couples four
  early capabilities with target-dependent combat and route predicates.
- [Observation | Corroborated | Medium] Float/updraft and surviving crossing
  recovery require boundaries distinct from reserves and full death.

## New genes

- [Observation | Corroborated | Medium] `SYS-1631`, `SYS-1632`.

## New combinations

- [Observation | Direct | High] No new combination proposal; complete proper-
  subset support is owned by Corpus comparison.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_307` admits only the
  two bounded systems. All existing definitions and signatures are unchanged.

## New questions

- What are the exact native launch-build float deadline and updraft reset rules?
- Which non-figment fields survive each partial hazard recovery versus death?
- How do later acquired powers change the same route on an authorised revisit?

## Next recommended game

- [Hypothesis | Limited | High] Original PlayStation Parasite Eve,
  `GAME-0562` under approved Selection 045.
- Optimisation criterion: retain mixed platforms, eras and consecutive
  mechanics; move from psychic platforming to positional action-RPG combat.
- Expected information gain: inspect the released original encounter/route
  without inheriting later remakes or an entire campaign union.
- Backlog impact: retain all six remaining subjects and stop after GAME-0567;
  no push, publication, Actions or deploy is authorised.

## Why this game

- [Hypothesis | Limited | High] A contemporary native Xbox platform adventure
  provides a direct sequel counterexample to the original Xbox training scope
  and alternates with the preceding Genesis run-and-gun game.
