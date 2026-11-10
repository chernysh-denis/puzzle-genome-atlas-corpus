---
game_id: GAME-0268
slug: undertale
game_title: Undertale
analysis_status: reviewed
reviewed: 2026-09-06
combination_ids:
  - COMB-0266
gene_ids:
  action:
    - ACT-008
    - ACT-019
    - ACT-131
    - ACT-341
    - ACT-445
  system:
    - SYS-369
    - SYS-578
    - SYS-813
    - SYS-814
    - SYS-815
  constraint:
    - CON-269
    - CON-611
  information:
    - INF-119
    - INF-325
  objective:
    - OBJ-162
  time:
    - TIM-001
    - TIM-003
---

# Game: Undertale

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: historically recorded unmodified English Windows Steam
  application 391540, sole one-app package 74780, on the default public branch
  carrying build 4279148, built 2019-10-11 with its branch record updated
  2019-10-28; checked 2026-09-06. No publisher announcement establishes a
  semantic version for this build: the developer's most recent Steam
  announcement at that observation was dated 2016-01-20, more than three years
  before the branch was last updated. This unit therefore asserts no semantic
  version and identifies the ruleset by the default branch and its build
  identifier alone, treating that identifier as a secondary distribution
  observation.
- Product boundary: this is **Undertale** on Windows, not Deltarune or any
  other title by the same developer. The single listed DLC app `391570` is a
  soundtrack and is outside this packet. The application also publishes opt-in
  legacy and test branches; this packet uses only the default `public` branch.
- Platform, input and difficulty: English interface, Windows, keyboard, a
  fresh single-player save. The product offers no difficulty setting in
  ordinary play, so the ruleset is fixed by the product rather than chosen.
- Setup-only predecessors: the fall onto the bed of golden flowers, the first
  encounter with the flower character, and the first monster encounter in the
  tutorial area. The guardian character interrupts and ends both of those
  encounters, so neither is settled by the player and neither contributes a
  transition to this packet. They establish a clean save only.
- Entry: accept first ordinary control on the bed of golden flowers in the
  tutorial area, before the first encounter and before any command is issued.
- Primary decision loop: move the protagonist through the tutorial area until
  an encounter opens; in the command phase inspect the four declared options
  against the current monster and commit only required non-damaging
  interactions, healing-item use or eligible release; the offered attack has
  moving-marker damage control but is never executed by this route; watch the
  interface for the marker that says the monster may now be released; when the
  opponent's phase begins, steer the small token continuously inside the
  bounded board so it avoids the shapes the monster releases into it; repeat
  until the release marker appears, then commit the release option to close
  the encounter without defeating anything; and use a save point to restore
  health and record the run.
- Positive terminal: settle one ordinary monster encounter entirely through
  the monster's non-damaging interactions followed by the release option,
  having defeated nothing at any point in the run. Then reach a save point,
  record the run, quit to the title and reload; verify retained position,
  health and no-kill continuity from an adequate event/state record rather
  than assuming an initially visible KILLS counter. This is an unexecuted
  verification protocol, not an observed save result. Stop without advancing
  to the guardian's own encounter.
- Negative terminal: health reaching zero ends the current attempt; continuing
  restores the last recorded save point. Reaching the release marker or opening
  the release option without committing it, or defeating any monster at any
  point in the run, is not success.
- Included: overworld movement; the encounter's four declared command options
  and their per-monster sub-options, the attack option among them as an offer
  the declared route never takes; the healing item and its consumption; the
  continuous steering of the token inside the bounded board during the
  opponent's phase; the strict alternation of the command phase and the
  opponent's phase; the accumulation of per-monster interactions into release
  eligibility; the eligibility marker in the interface; committed non-killing
  release, with whole-encounter closure only when no opponents remain and
  without asserting zero GOLD; the single health pool and its zero terminal;
  save-point interaction and the restore that follows a failed attempt; and
  the authored no-kill continuity and save/reload verification requirement,
  whose native result is still outstanding.
- Excluded: Deltarune and every other title; the soundtrack DLC; the opt-in
  legacy and test branches; the guardian's own encounter and every later area,
  character and ending; the attack option's use, which the declared route
  refuses although the packet admits the option itself as the decision the
  objective is defined against; the game's persistent cross-save behaviour and
  anything it changes on a later run, which lies outside a single bounded
  attempt; alternate routes defined by defeating monsters; equipment, GOLD
  spending and shop loops; possible incidental GOLD is not ruled out merely
  because kill EXP is absent; all inputs and platforms not declared above;
  screenshots, official artwork, third-party assets, video and audio evidence.
- Reproducible parameterisation: install English app 391540 from package
  74780, confirm the default public branch, and start a fresh save. Pass the
  setup-only predecessors without settling either. From ordinary control,
  enter one ordinary monster encounter, use at least one of that monster's
  declared non-damaging interactions, survive at least one opponent phase by
  steering the token inside the board, observe the release marker appear, and
  commit the release option. Then use a save point and perform the stated
  record-and-reload check. An ordinary ACT-dependent opponent and encounter
  composition must be identified before native verification; initially
  spareable monsters, damage-induced eligibility and special boss exceptions
  are excluded from this selected analytical branch. Exact interaction
  wording, projectile patterns, health values and elapsed time are parameters.
  No native trace is supplied by this review.
- Potential scoped modules: the guardian's encounter; one later area; a route
  defined by defeating monsters; the persistent cross-save behaviour; or the
  product's alternate hard ruleset requires its own version, entry, loop,
  terminal and evidence.
- Direct-play status: No direct playthrough, identified executable,
  input/event trace or native save/reload inspection was conducted in this
  audit. The historically declared Windows public build 4279148 remains a
  secondary distribution identifier, not a newly certified current build. The
  publisher About page supports nonviolent resolution generally; Undertale
  Wiki Combat, Froggit, Gold and Stats are community pages from one source
  family, not official product specifications or independent native
  confirmations. During P5, direct HTTP retrieval was refused (403), while
  relevant public text bodies were read through the web reader. P7 reread the
  publisher About page and the relevant public wiki text through the web
  reader; no fresh direct-HTTP failure or downloaded HTML hash is claimed.
  They motivate separating eligibility, removal, group closure, kill EXP and
  possible GOLD, and warn that the initial KILLS stat is hidden. They do not
  establish exact historical event order, reward amounts, target-selection
  mechanics or persistence for this build. `TAXONOMY_CHANGE_031` and ACT-261
  exclusion remain intact. No video or audio was opened or played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `UND-001` | Steam app `391540` and its sole one-app package `74780` identify the currently lawfully offered English Windows product, whose only DLC app is a soundtrack | Confirmed | Direct | High | P1, P2 |
| `UND-002` | The default `public` branch carries build `4279148`, built 2019-10-11 and updated 2019-10-28, alongside opt-in legacy and test branches | Observation | Limited | Medium | S1 |
| `UND-003` | No publisher announcement establishes a semantic version for that build; the developer's most recent Steam announcement predates it by more than three years | Observation | Direct | High | P3 |
| `UND-004` | An encounter exposes four command options together with the protagonist's level and health | Observation | Limited | Medium | S2 |
| `UND-005` | The attack option resolves damage by how close a marker moving along a bar is stopped to its centre | Observation | Limited | Medium | S2 |
| `UND-006` | The interaction option can change the opponent's mood or reveal information about it | Observation | Limited | Medium | S2 |
| `UND-007` | The item option consumes one carried item from the inventory | Observation | Limited | Medium | S2 |
| `UND-008` | In the selected ordinary marker-gated branch, the release option removes eligible monster participants; the name or option colour marks eligibility before the release is committed. This is not a universal boss rule | Observation | Limited | Medium | S2 |
| `UND-009` | During the opponent's phase the protagonist's token is placed inside a bounded board and the monster attacks it with projectiles | Observation | Limited | Medium | S2 |
| `UND-010` | The tutorial area begins on a bed of golden flowers and contains a save point in its first room | Observation | Limited | Medium | S3 |
| `UND-011` | The flower character's opening encounter is ended by the guardian character, who then guides the protagonist through the tutorial area | Observation | Limited | Medium | S3 |
| `UND-012` | The first ordinary monster encounter is also ended by the guardian after any non-attack command, so it takes one turn and the player does not settle it | Observation | Limited | Low | S4 |
| `UND-013` | Community descriptions of an ordinary ACT-dependent monster distinguish an interaction that prepares marked eligibility from a subsequent committed release; the exact opponent and historical build trace remain unverified | Observation | Limited | Medium | S4 |
| `UND-014` | The save point records the run, restores health and receives the protagonist after a failed attempt | Observation | Limited | Medium | S3 |
| `UND-015` | The bounded identity is one encounter whose two phases demand different competences in strict alternation, and whose peaceful close is a legality the player must earn rather than a chance they roll | Strong Pattern | Corroborated | Medium | `UND-004`–`UND-014` |

Documentary limits: all existing evidence grades remain unchanged. The
selected ordinary ACT-dependent encounter distinguishes preparation, a
precommit eligibility marker, actual removal and closure only when no
opponents remain. Community descriptions do not certify build4279148 native
reward amounts, exact targeting, a visible initial kill counter or a completed
save/reload trace. The authored positive terminal still requires retained
position, health and no-kill continuity after save/reload; no such result is
claimed. FIGHT remains an offered but unexecuted option, not an admitted Action.

## Basic data

- Release / origin: tobyfox; developed and published on Windows by tobyfox and
  released 2015-09-15.
- Platform or physical form: lawfully offered English Windows single-player
  Steam application `391540`; one fresh tutorial-area route to a single
  non-lethally settled encounter.
- Puzzle family: tactical forecast and counterplay; knowledge and evidence
  progression.
- Primary and official sources, accessed 2026-09-06:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=391540&cc=ua&l=english),
    for the exact title, app, Windows support, developer and publisher, release
    date, the `Indie` and `RPG` genres with no Early Access marker, the
    single-player-only category list, the single soundtrack DLC app, the sole
    package and the current Ukraine offer.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=74780&cc=ua&l=english),
    for package `74780` containing only app `391540` and its current Ukraine
    offer.
  - **[P3]** [Valve news endpoint for this application](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=391540&count=20&feeds=steam_community_announcements),
    for the complete developer announcement list, whose most recent entry is
    dated 2016-01-20 and therefore predates the current branch build. This
    establishes the absence of a publisher-stated version for that build.
- Corroborating textual sources, accessed 2026-09-06:
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/391540),
    for the default `public` branch build `4279148`, its timestamps and the
    opt-in legacy and test branches. This mirrors Valve's public product data
    and is treated as a secondary distribution observation, not a publisher
    claim.
  - **[S2]** [community product wiki, Encounter](https://undertale.fandom.com/wiki/Encounter),
    for the four command options shown with level and health, the attack
    option's moving-marker damage bar, the interaction option changing mood or
    revealing information, the item option drawing from inventory, the release
    option removing a monster whose name is coloured, and the protagonist's
    token being placed inside the bounded board while the monster attacks it
    with projectiles. The wiki host refuses direct retrieval from this
    environment, so its content was reached through search indexing rather than
    by fetching the page.
  - **[S3]** [community product wiki, Ruins](https://undertale.fandom.com/wiki/Ruins),
    together with its linked `Golden Flowers`, `Flowey` and `Frisk` pages, for
    the opening on the bed of golden flowers, the tutorial area's role, the
    guardian character ending the flower character's encounter and guiding the
    protagonist, the save point in the first room, and the save point's
    recording, healing and post-failure return.
  - **[S4]** [community product wiki, Froggit](https://undertale.fandom.com/wiki/Froggit),
    together with the static community route guide it summarises, for the first
    monster encounter being ended by the guardian after any non-attack command,
    and for a later monster of the same kind being released by using one of its
    declared interactions and then the release option, with its name turning
    coloured.
- P7 source re-review: [publisher About](https://undertale.com/about/)
  supports nonviolent resolution and evasion generally, not exact historical
  reward or save rules. Relevant public text on [Encounter](https://undertale.wiki/w/Combat),
  [Froggit](https://undertale.wiki/w/Froggit), [GOLD](https://undertale.wiki/w/Gold)
  and [Stats](https://undertale.wiki/w/Stats) was reread through the web reader.
  These wiki pages count as one community family, not official specifications
  or four independent confirmations. Froggit ACT descriptions are documentary
  selection context, not an executed build-qualified result or a newly fixed
  monster/formation. The earlier search-only access limits below describe
  their historical review; P5 directHTTP403was not repeated in P7.
- Source-class correction, recorded for `BATCH_015_GENE_AUDIT_001` finding
  `A-10`: `undertale.fandom.com` is a community wiki. This unit found no
  evidence of publisher ownership, and the record's own citations list it under
  corroborating textual sources, so calling it an official product wiki was
  wrong. It is relabelled here. `S2`, `S3` and `S4` are also three pages of that
  one wiki and count as one corroborating family, not three independent
  sources; the host refuses direct retrieval, so none of them was fetched.
  Every claim resting on that family alone — `UND-004` through `UND-014` — is
  therefore downgraded to `Limited` evidence with `Medium` or `Low` confidence,
  and `UND-015` to `Medium` confidence. The mechanical findings are not
  discarded: the source class was overstated, not the observations refuted.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P3` and `S1`–`S4` under the declared app, package, branch, build,
  platform, input, clean save, exclusions and terminal; rules reasoning, not
  direct play.
- Claim IDs: `UND-001`–`UND-015`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: move the protagonist through the tutorial area until an
  encounter opens; `ACT-341`: address the save point as a reachable authored
  object and commit its recording interaction.
- Existing `ACT-019`: select one of the encounter's declared options against
  the current monster, including the per-monster sub-options the interaction
  command exposes. The boundary already covers choosing a declared ability and
  specifying its target, so no battle-command gene was created.
- `ACT-261` is **not** admitted, although the attack option resolves through a
  moving marker that would fit its boundary exactly. The declared successful
  route never executes the attack, and an Action gene records a verb the route
  performs, not an offer it refuses. `UND-005` keeps the resolution on record as
  evidence of what the refused option would do, and `ACT-019` already carries
  the choice among the encounter's declared options, so nothing about the
  decision is lost. This reverses the previous unit's admission; see
  [`TAXONOMY_CHANGE_031`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_031.md).
- Existing `ACT-131`: consume one carried item for its immediate effect.
- New `ACT-445`: continuously steer the small token inside the bounded board so
  it avoids the shapes the opponent releases. `ACT-223` commits one input at a
  chosen instant, `ACT-436` buys a protected interval from a shared reserve,
  `ACT-437` holds a facing-relative guard, and `ACT-008` navigates a persistent
  agent through level geometry; none covers continuous spatial evasion inside a
  frame the opponent fills.
- Monster, interaction wording, item and area names remain parameters. Claims:
  `UND-004`–`UND-013`.

### System Behaviour Genes

- Existing `SYS-578`: attacks reduce one continuous health pool, the item
  restores it and zero ends the current attempt; `SYS-369`: a failed attempt is
  restored from the latest recorded save point rather than preserving its
  transient state.
- New `SYS-813`: the encounter alternates strictly between a discrete command
  phase and a continuous evasion phase, and neither accepts the other's inputs.
  `SYS-356` orders many combatants in an initiative queue and `SYS-359`
  resolves a timed defensive input inside an otherwise discrete turn; neither
  describes two phases with different time regimes.
- New `SYS-814`: in the selected ordinary ACT-dependent branch, non-damaging
  interactions prepare spare eligibility before release; this is not a universal
  prerequisite for all monsters and does not itself remove an opponent.
- New `SYS-815`: valid committed release removes eligible opponents without
  killing or their kill EXP; the encounter closes only when none remain.
  Incidental GOLD is not ruled out. Exact native reward/save results remain
  unverified for build 4279148.
- Documentary composition, not a measured native event order: command selection
  and continuous evasion belong to different phases. The admitted ACT branch
  updates eligibility before Spare is committed. A valid release removes
  eligible opponents and terminates the battle only if none remain; do not
  force another enemy attack after final settlement. The route never executes
  FIGHT or the withdrawn ACT-261. Exact reward and persistence order requires
  a version-identified native trace; no zero-GOLD or visible KILLS=0 is assumed.

### Constraint Genes

- Existing `CON-269`: an option resolves only when its target, availability and
  current state permit it.
- New `CON-611`: in the selected ordinary marker-gated branch, release removes
  eligible opponents; no eligible opponent means the command spends a phase
  without removal. This is not a universal boss rule or universal prior-ACT
  requirement. CON-276 probabilistic capture remains a distinct mechanism.
- Scarce resources: health, carried items and phases spent preparing the
  selected opponent's eligibility. No-kill continuity is an authored condition,
  not a claim that an initial zero KILLS counter is visible. Exact values and
  adequate native persistence evidence remain to be verified.
  Claims: `UND-007`–`UND-014`.

### Information Genes

- Existing `INF-119`: the encounter exposes the protagonist's level and health.
- New `INF-325`: the interface distinguishes which opponents have satisfied
  their release condition, by marking the option or the opponent's own entry,
  without disclosing the condition that produced the change. `INF-122` shows a
  numeric capture estimate and `INF-295` exposes a finisher opportunity;
  neither states a legality while withholding its rule.
- Exact colours, fonts, board geometry and interface positions are presentation
  parameters. Claims: `UND-004`, `UND-008`, `UND-013`.

### Objective Genes

- New `OBJ-162`: close the ordinary encounter through non-damaging ACT and
  committed release, with no kills anywhere in the run, then verify retained position, health and run state
  after save/reload using an adequate event/state record. The initial KILLS
  statistic is not presumed visible; this native verification is outstanding.
  OBJ-029 and generic survival do not replace the no-kill retained terminal.
  OBJ-153 admits lethal or non-lethal settlement of a designated target; it
  does not substitute for the declared no-kill retention requirement.
- Reaching the release marker without committing it, or defeating any monster
  at any point, is not success. Claims: `UND-013`–`UND-015`.

### Time Genes

- Existing `TIM-001`: in the command phase the player supplies one discrete
  input and the system completes its resulting state changes before accepting
  another.
- Existing `TIM-003`: in the opponent's phase the decision state advances on a
  real-time schedule while the steering input remains accepted.
- The packet therefore carries two time structures, and their strict
  alternation is owned by `SYS-813` rather than by either time gene. Claims:
  `UND-005`, `UND-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A fresh save has completed only the setup-only predecessors | Accept ordinary control in the tutorial area | The run begins with nothing defeated and the first save point available | fixed clean entry | `UND-010`, `UND-011` |
| The first monster encounter opens | Issue any non-attack command | The guardian ends the encounter after one turn, so the player does not settle it | setup-only predecessor | `UND-012` |
| An ordinary encounter offers commands | Inspect the unexecuted FIGHT alternative; do not perform it on the authored route | The described moving-marker damage input is a counterfactual offered capability, not an executed transition or admitted ACT-261 | historical option description outside the successful route | `UND-005`, `TAXONOMY_CHANGE_031` |
| An ordinary encounter is open and it is the command phase | Choose one of the monster's declared interactions | The monster's mood or exposed information changes and no damage is dealt | opponent-specific interaction | `UND-006` |
| The monster's declared condition has been satisfied | Look at the encounter interface | The release option or the monster's own entry is marked differently | eligibility disclosure | `UND-008`, `UND-013` |
| The monster is not yet marked releasable | Commit the release option | The phase is consumed and the monster remains in the encounter | release legality | `UND-008` |
| An ordinary opponent is eligible | Commit valid Spare | Eligible opponent participants leave without kill EXP; close only if none remain, with exact reward trace unverified | non-killing settlement, not merely eligibility | `UND-013`, pending build-specific verification |
| A non-terminal command resolves and the ordinary encounter continues | Enter the enemy phase | The token is confined to the bounded board and projectiles cross it; a valid release that removes the last opponents instead closes the encounter | phase alternation with final-settlement exit | `UND-009`, `UND-013` |
| The opponent's phase is running | Steer the token | Only steering is accepted; contact with a projectile reduces health | continuous evasion | `UND-009` |
| Health is below its cap and an item is carried | Choose the item option | One item is consumed and health is restored | item recovery | `UND-007` |
| Health reaches zero | Continue | The attempt ends and resumes from the last recorded save point | reproducible negative recovery | `UND-014` |
| An ordinary encounter is closed by release with no kills in the run | Save, quit and reload, retaining an adequate event/state record | Verify retained position, health and no-kill continuity without presuming visible initial KILLS=0; native result outstanding | authored positive-terminal verification protocol | `UND-014`, `UND-015`, pending native check |

## Strategic and experiential structure

- Planning horizon: the health pool, the carried items and the number of phases
  a monster's condition still needs decide whether to keep interacting, heal,
  or accept another opponent phase.
- Local tactics: spend the command phase on the interaction the monster's own
  responses point to, keep enough health that one more opponent phase is
  survivable, and watch the interface for the marker rather than guessing when
  the condition is met.
- Medium-term structure: refusing the attack option is not a handicap but the
  objective, so every encounter becomes a short investigation of one specific
  opponent rather than an application of a general combat capability.
- Reversible versus irreversible: interactions and steering are freely
  repeatable within the run; a consumed item and a spent phase are not; a
  defeat would be irreversible for the objective, which is why the route
  refuses the attack option entirely.
- Failure attribution: the visible health, the item count and the eligibility
  marker make a loss traceable to a specific unhealed phase or an interaction
  that was not the one the monster required.
- Player trust: distinguish the precommit eligibility marker from actual
  removal; the command and evasion phases retain their distinct inputs.
  Distinguish final closure from partial group removal. No-kill continuity
  and retained state require evidence after save/reload; an initially visible
  zero KILLS counter is not promised and no native result was observed.

## Replay and variation

- What changes: which monster is encountered, which interactions it requires,
  the projectile patterns, how much health is lost and how many items are
  spent.
- Randomness or procedural generation: the area, its save points, the monster
  roster and each monster's release condition are authored. Which ordinary
  monster appears varies; no procedural-generation claim enters this packet.
- Multiple strategies: the encounter admits interacting immediately, healing
  first, or attacking. The control demonstrates the interaction-and-release
  route rather than making a no-damage-taken run the terminal.
- Typical replay motive: close the same encounter having spent fewer phases and
  no items, or learn which interaction a different monster requires.

## Adjacent systems and history

- Dead Space (2023 remake) shares movement, item consumption, authored-object
  interaction, option legality, a visible personal state, checkpoint restore
  after failure, one health pool and real-time resolution. Its encounters are
  resolved entirely by destroying opponents in continuous time; this packet
  splits the encounter into two alternating phases and defines success by
  destroying nothing.
- Clair Obscur: Expedition 33 is the closest structural relative, sharing the
  command selection, item consumption, option legality, the visible personal
  state and both time genes. Its real-time element is a timed defensive input
  committed inside an otherwise discrete turn, and its objective is to
  incapacitate the hostile set; this packet's defence is continuous spatial
  evasion and its objective is satisfied by leaving that set alive.
- Pokémon Legends: Z-A shares removing an opponent without defeating it,
  but by probabilistic capture into owned storage. The selected ordinary
  Undertale branch prepares eligibility through ACT and removes through Spare;
  this comparison does not assert that release pays zero GOLD.
- Papers, Please shares a deterministic bounded decision loop with a visible
  legality marker, but resolves it by classification rather than by an
  encounter with two time regimes.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-019`, `ACT-131`, `ACT-341`, `ACT-445` | monster, interaction wording, item and area names are parameters |
| System Behaviour | `SYS-369`, `SYS-578`, `SYS-813`, `SYS-814`, `SYS-815` | phase durations, conditions, damage values and kill EXP versus possible GOLD (exact settlement still unverified) are parameters |
| Constraint | `CON-269`, `CON-611` | eligibility markers and per-opponent conditions are parameters |
| Information | `INF-119`, `INF-325` | colours, board geometry and interface layout are parameters |
| Objective | `OBJ-162` | encounter identity and the count that must stay at zero are parameters |
| Time | `TIM-001`, `TIM-003` | command pacing and projectile timing are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `267` (`GAME-0001`–`GAME-0267`).
- Exact genome matches: none.
- Tied near matches: `GAME-0259` — Dead Space (2023 remake) (`8 / 44 = 0.181818`).
- Supported combination subsets: `COMB-0266`.
- Scan date: 2026-09-06.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0259` — Dead Space (2023 remake) | `ACT-008`, `ACT-131`, `ACT-341`, `SYS-369`, `SYS-578`, `CON-269`, `INF-119`, `TIM-003` | Both move a protagonist through an authored area, consume carried items for their immediate effect, address authored objects, gate options on their current legality, expose the protagonist's personal state, reduce one continuous health pool to a terminal, restore a checkpoint after failure and run in real time. Dead Space resolves every encounter by destroying opponents in continuous time with a targeted-dismemberment economy. This packet splits each encounter into a discrete command phase and a continuous evasion phase that never accept each other's inputs, makes ending an encounter peacefully a legality earned through that specific opponent's own interactions, withholds kill EXP without asserting zero GOLD, and defines success by no-kill continuity and retained state, whose native verification remains outstanding. The shared core is the traversal-and-survival substrate, not the encounter itself. | Near, `0.181818` |

### Preserved research notes

- New genes: `ACT-445`, `SYS-813`, `SYS-814`, `SYS-815`, `CON-611`, `INF-325`,
  `OBJ-162`.
- Reused genes: `ACT-008`, `ACT-019`, `ACT-131`, `ACT-341`, `SYS-369`,
  `SYS-578`, `CON-269`, `INF-119`, `TIM-001`, `TIM-003`.
- Classification result: `New gene`.
- Lower-ID scan: reuse `ACT-019` for the command selection rather than adding a
  battle-menu gene, because the boundary already covers choosing a declared
  ability against a target; do not admit `ACT-261` for the attack marker, whose
  boundary the resolution would fit, because the declared route never executes
  the attack, and reject `ACT-223`, which covers a timed defensive response this
  product does not have; reuse `SYS-578` and `SYS-369` for the health pool and the
  post-failure restore; reuse `TIM-001` and `TIM-003` for the two phases and
  let `SYS-813` own their alternation. Reject `SYS-356` and `SYS-359` on their
  stated boundaries, `OBJ-029` and `OBJ-153` for the objective, `CON-276` for
  the release legality and `INF-122` and `INF-295` for the eligibility marker.
  Reject a monster-, area-, character- or item-named gene.

## Taxonomy impact

- Registry changes: add `ACT-445`, `SYS-813`, `SYS-814`, `SYS-815`, `CON-611`,
  `INF-325`, `OBJ-162` and `COMB-0266`, plus independent evidence for ten reused
  genes.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_031`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_031.md)
  removed the `ACT-261` reuse from this signature, which falls from eighteen
  genes to seventeen, and withdrew the corpus-wide admission rule that had
  authorised it. No gene was added, merged, split, deprecated or retyped;
  `ACT-261` keeps its definition, lifecycle and its two remaining carriers.
- Candidate terms: recorded in `CANDIDATE_TERMS.md`; all product, character,
  monster, area, item, app, package and build names remain parameters.

## Negative results

- No video or audio evidence was used; only official product data, the Valve
  news endpoint and community product wiki material support this packet.
- No semantic version is asserted. The Valve news endpoint shows that the
  developer's most recent announcement predates the current branch build by
  more than three years, so no publisher statement covers it. This is a third
  distinct version situation in this batch, alongside the announced-but-earlier
  updates of `GAME-0265` and `GAME-0266` and the exactly matching announcement
  of `GAME-0267`.
- The community product wiki host refuses direct retrieval from this
  environment. Its content was reached through search indexing and is cited
  with that limitation stated, exactly as recorded for `GAME-0267`. Its three
  cited pages are one source family rather than three independent sources.
- The attack option is exposed at the declared command phase and the route
  refuses it, and that refusal is the packet's central decision — but the option
  is described in this record's prose rather than admitted as a gene.
  `BATCH_015_GENE_AUDIT_001` finding `A-09` was closed in the previous unit by
  writing a four-condition corpus-wide admission rule into
  `RESEARCH_PRINCIPLES` and admitting `ACT-261` under it. Review finding `R-04`
  held that this changed corpus-wide admission semantics without an ADR or an
  explicit maintainer decision, so
  [`TAXONOMY_CHANGE_031`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_031.md)
  reverted both: the rule is withdrawn from `RESEARCH_PRINCIPLES` and preserved
  as the `Proposed`
  [`ADR-013`](../../../docs/architecture-decisions/ADR-013-unexecuted-action-admission.md)
  for maintainer review, and `ACT-261` leaves this signature. `OBJ-162` and
  `CON-611` still define the terminal and the release legality by reference to
  the refused option, which is where that content belongs.
- The product's persistent cross-save behaviour is excluded because it acts
  between attempts rather than inside one bounded attempt; it is named as a
  potential scoped module.
- Reaching the eligibility marker without committing the release is not the
  terminal.

## Delta summary

## New facts

- [Observation | Corroborated | High] `UND-001`–`UND-015`: one bounded
  encounter alternates a discrete command phase with a continuous evasion phase
  and closes peacefully only through a legality earned from that specific
  opponent, without kill EXP but without asserting zero GOLD; these historical metadata are retained, not new build-specific verification.

## New genes

- [Observation | Corroborated | High] `ACT-445`, `SYS-813`, `SYS-814`,
  `SYS-815`, `CON-611`, `INF-325`, `OBJ-162` — continuous evasion inside a
  bounded board, the strict two-regime phase alternation, opponent-specific
  interactions accumulating into release eligibility, the non-killing release (no zero-GOLD assertion),
  its legality, the eligibility marker and the objective satisfied by a
  capability deliberately not used.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0266` — an encounter whose two
  phases demand different competences; the selected ordinary ACT-dependent
  branch earns release eligibility, then removes through committed Spare
  without kill EXP. Possible GOLD is not excluded; exact native rewards and
  retained-state verification remain outstanding.

## Taxonomy changes

- [Observation | Direct | High] No taxonomy changes; no split, merge,
  deprecation, lifecycle change, wording generalisation or earlier signature
  change.

## New questions

- Does a second product reuse `SYS-813`, or is the strict two-regime phase
  alternation specific to this encounter model?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0269` — DREDGE.
- Optimisation criterion: leave the encounter corridor and test whether spatial
  cargo packing coupled to a day-cycle pressure meter is a genuine interaction
  or two already-reviewed structures sharing a product.
- Expected information gain: the falsifiable question the selection recorded
  for this subject.
- Backlog impact: advances the recorded 261-to-270 horizon by one unit.

## Why this game

- [Hypothesis | Limited | High] The selection asked whether one packet can hold
  a turn-based selection phase and a real-time dodge phase without collapsing
  into two scopes, and whether non-lethal settlement is a distinct objective
  gene. The completed decomposition answers both: the alternation is one system
  boundary rather than two scopes, and the objective required a new gene because
  every existing bounded-encounter objective is satisfied by removing opponents
  rather than by refusing to.
