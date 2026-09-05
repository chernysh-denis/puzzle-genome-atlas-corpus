---
game_id: GAME-0252
slug: detroit-become-human
game_title: "Detroit: Become Human"
analysis_status: reviewed
reviewed: 2026-09-05
combination_ids:
  - COMB-0250
gene_ids:
  action:
    - ACT-008
    - ACT-232
    - ACT-341
    - ACT-427
  system:
    - SYS-379
    - SYS-680
    - SYS-783
    - SYS-784
    - SYS-785
  constraint:
    - CON-282
    - CON-597
  information:
    - INF-125
    - INF-148
    - INF-307
    - INF-308
  objective:
    - OBJ-157
  time:
    - TIM-003
---

# Game: Detroit: Become Human

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam full-game
  application `1222140`, current one-app retail package `423337` and public
  branch Build ID `12158144`, built 2023-09-11 and published 2023-09-28,
  checked 2026-09-05. The build identifier and dates are secondary
  distribution observations. This is the Windows full game, not the PC demo,
  PlayStation demo or release, Alexa skill, soundtrack, art book or another
  Quantic Dream title.
- Platform, input and difficulty: Windows 10 64-bit, English interface and
  subtitles, keyboard and mouse, `Experienced`, fresh unused local story save,
  ordinary `New Story`. Controller, `Casual`, Chapter Select replay and an
  imported or completed save are separate modules.
- Entry: begin the opening chapter, `The Hostage`, and retain the first
  controllable Connor state after the elevator opens into the apartment. The
  incoming incident, actors and authored apartment state are fixed setup; the
  optional fish interaction is not required by the reproducible route.
- Primary decision loop: read the current objective, scene, investigation
  markers and incident pressure; directly navigate Connor; inspect eligible
  objects and bodies; scrub fixed reconstructions to their causal points;
  convert the resulting authored facts into named context for negotiation;
  enter the rooftop; read the current response set, timer and displayed chance
  of success; commit one response or intervention before its opportunity
  closes; let the accumulated evidence, trust and final action settle one
  authored incident branch; then inspect the chapter flowchart.
- Reproducible positive route: speak to Captain Allen; inspect and reconstruct
  the empty gun case; inspect the child's media in her room to learn the
  deviant's name; scan and reconstruct the father's body and inspect the
  replacement-order record; scan and reconstruct the officer's body, locate
  but leave the firearm; inspect the blue blood; enter the rooftop; choose
  `Name`, `Calm`, `Possible Cause`, `Emma and You`, `Sympathetic`; obey the
  demand not to aid the wounded officer; choose `Accept` to dismiss the
  helicopter, then `Trust`, `Compromise` and `Reassure`. With the resulting
  maximum negotiation advantage, Daniel releases Emma and is killed by the
  snipers while Connor survives, producing `Snipers Shot Deviant`.
- Positive terminal: the post-chapter flowchart displays the traversed path and
  `Snipers Shot Deviant` endpoint after Emma is released and Connor survives.
  Exit the flowchart without replaying, reopen the completed chapter's
  flowchart from the chapter surface and verify that the traversed nodes and
  endpoint remain recorded. The first such retained reinspection closes the
  packet. Neither rooftop control, Emma's release before settlement nor an
  unverified transition into the next chapter is terminal.
- Negative terminal: the incident settles into a branch where Connor fails to
  reach the confrontation in time, Connor dies, Emma dies or both Connor and
  the hostage fall; the corresponding post-chapter flowchart endpoint is the
  formal evaluated result. Restarting, quitting, pausing or letting one
  dialogue timer expire without accepting the chapter settlement is not a
  terminal by itself.
- Included: direct third-person navigation; bounded contextual object and body
  inspection; fixed-event reconstruction with a movable time cursor; authored
  facts and investigation completion; incident time pressure; rooftop
  dialogue choices and their bounded timers; displayed success estimate;
  named evidence-conditioned options; the wounded-officer intervention gate;
  helicopter dismissal; accumulated trust; alternative incident outcomes as
  legal branches of this one ruleset; automatic chapter settlement; the
  traversed-versus-locked flowchart; local story persistence; and a
  non-replaying flowchart retention check.
- Excluded: every chapter after `The Hostage`; the complete Connor, Kara and
  Markus story; later public-opinion, relationship, software-instability and
  character-survival consequences; all other endings and full-flowchart
  completion; deliberate replay, Chapter Select overwrite behaviour and
  global player percentages; `Casual`; controller; PC/PS4 demos, Alexa skill
  and Community Play/Twitch voting; trophies, achievements, extras, gallery,
  surveys and soundtrack; PlayStation, macOS, Linux/Proton, streaming or
  another platform; mods, trainers, save editing and debug tools; audio and
  audiovisual performance analysis.
- Reproducible parameterisation: preserve app, package, public build, Windows,
  English text, keyboard/mouse, `Experienced`, unused save and `New Story`.
  Follow the listed clue and response route exactly, leave the firearm, obey
  the wounded-officer demand and accept helicopter dismissal. Record the
  success estimate before each rooftop commitment and the first flowchart
  state after settlement; exit and reopen only the completed flowchart to
  prove retention. Exact walking path, camera angle, prompt binding, optional
  fish state, inspection order among already available clues and elapsed
  seconds are parameters unless they change an authored opportunity.
- Potential scoped modules: one `Casual` run, one alternative `The Hostage`
  branch, one replay/overwrite test, one later named chapter, one complete
  story route or one named non-Windows build each requires its own entry,
  decision loop, evidence and retained terminal.
- Direct-play status: not conducted. Valve and Quantic Dream material establish
  current lawful Windows availability, full-game product identity, PC input
  support and branching choice boundary. Official PlayStation editorial
  material establishes the opening incident, investigation, time pressure,
  choice effects, difficulty distinction and post-scene flowchart; maintained
  textual walkthroughs corroborate exact clues, response order and terminal
  route. This is evidence-backed rules reconstruction, not a claimed
  playthrough or entitlement. No video or audio was opened, played, heard,
  analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DBH-001` | The selected lawful product is the English Windows full-game Steam app `1222140` in one-app retail package `423337`, with keyboard/mouse and controller support | Confirmed | Direct | High | P1–P3 |
| `DBH-002` | Steam public Build `12158144` is the current observed Windows distribution boundary | Observation | Corroborated | Medium | S1, S2 |
| `DBH-003` | `Experienced` preserves the full control and protagonist-death opportunity set, unlike the simplified `Casual` mode | Confirmed | Direct | High | P4 |
| `DBH-004` | `The Hostage` is the first scene and begins with Connor investigating a live homicide/hostage incident under time pressure | Confirmed | Direct | High | P4, P5 |
| `DBH-005` | Inspecting eligible scene evidence and scrubbing reconstructions yields authored facts that open or strengthen later negotiation options | Confirmed | Corroborated | High | P4–P6, S3, S4 |
| `DBH-006` | Rooftop responses and interventions occur within bounded opportunities, and the interface updates a visible probability of success from the current negotiation state | Observation | Corroborated | High | P4, S3, S4 |
| `DBH-007` | The fixed clue/response trace can reach maximum negotiation advantage, release Emma, preserve Connor and settle as `Snipers Shot Deviant` | Observation | Corroborated | High | S3, S4 |
| `DBH-008` | Other legal branches can kill Connor, Emma or both, or settle before Connor reaches the confrontation | Confirmed | Corroborated | High | P4–P6, S3 |
| `DBH-009` | After the scene, a flowchart exposes the traversed path and locked alternatives while preserving the completed chapter for later inspection | Confirmed | Direct | High | P4–P7 |
| `DBH-010` | One opening incident from first control through a retained endpoint is the bounded ruleset; the wider three-character campaign and later consequences are not required | Strong Pattern | Corroborated | High | `DBH-003`–`DBH-009` |

## Basic data

- Release / origin: developed by Quantic Dream and published on Windows in
  2019; Steam release 2020-06-18. Current product state checked 2026-09-05.
- Platform or physical form: single-player authored branching narrative on
  Windows; one opening chapter on `Experienced` with English text.
- Puzzle family: knowledge and evidence progression; real-time system pressure;
  tactical forecast and counterplay; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-05:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=1222140&cc=ua&l=english),
    for exact title, Windows support, single-player/full-controller categories,
    language support, release date and current application availability.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=423337&cc=ua&l=english),
    for current one-app retail package availability.
  - **[P3]** [official Quantic Dream PC page](https://www.quanticdream.com/en/detroit-become-human/pc),
    for full-game PC identity, Windows requirements, keyboard/mouse and gamepad
    integration, language support and the choice-to-consequence premise.
  - **[P4]** [official first-thirty-minutes guide](https://blog.playstation.com/archive/2018/04/23/7-things-youll-notice-in-your-first-30-minutes-of-detroit-become-human),
    for `Experienced` versus `Casual`, Connor's opening investigation, clue and
    time pressure, improvised negotiation, death possibility and end-scene
    flowchart.
  - **[P5]** [official `The Hostage` demo article](https://blog.playstation.com/?p=200288),
    for first-scene identity, crime-scene examination, negotiation, multiple
    outcomes and terminal flowchart. Demo availability itself is excluded.
  - **[P6]** [official hands-on article](https://blog.playstation.com/?p=200839),
    for reconstruction-led investigation and the path-versus-locked-alternative
    flowchart contract.
  - **[P7]** [official PlayStation Japan flowchart guide](https://blog.ja.playstation.com/2018/04/26/20180426-detroit/),
    for per-chapter path retention, hidden alternatives and later flowchart
    inspection from the chapter list.
- Corroborating textual sources, accessed 2026-09-05:
  - **[S1]** [SteamDB public depots](https://steamdb.info/app/1222140/depots/),
    for the Windows 64-bit depot and public Build `12158144`, built 2023-09-11
    and published 2023-09-28. SteamDB is a secondary distribution mirror.
  - **[S2]** [SteamDB retail package](https://steamdb.info/sub/423337/depots/),
    for package-to-app/depot corroboration.
  - **[S3]** [PowerPyx `The Hostage` route](https://www.powerpyx.com/detroit-become-human-the-hostage-opening-walkthrough-100/),
    for inspectable clues, time pressure, gun and wounded-officer choices,
    response sequence, success estimate and incident endpoints.
  - **[S4]** [GameFAQs Chapter 1 guide](https://gamefaqs.gamespot.com/ps4/182637-detroit-become-human/faqs/75941/chapter-1-the-hostage),
    for reconstruction points, evidence-conditioned options and the
    reproducible maximum-advantage negotiation sequence.
- Claim IDs: `DBH-001`–`DBH-010`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly navigate Connor through the apartment and onto
  the rooftop; `ACT-341`: inspect one reachable authored object, record or body
  and register its current evidence interaction; `ACT-232`: commit one offered
  rooftop dialogue or intervention response before any displayed timer closes.
- New `ACT-427`: scrub one fixed reconstructed incident interval and commit its
  causal inspection point. This observes an authored past rather than rewinding
  live game state, editing a command timeline or inventing evidence.
- Actor, apartment, clue, body, object, reconstruction, time point, response,
  prompt and exact control binding remain parameters. Claims:
  `DBH-004`–`DBH-008`.

### System Behaviour Genes

- Existing `SYS-680`: accepted clue inspection and reconstruction become
  authored investigation progress; `SYS-379`: completed chapter actions and
  choices update retained story state rather than resetting after the scene.
- New `SYS-783`: combine registered evidence and current interaction state into
  context-specific dialogue options and negotiation advantage; `SYS-784`:
  resolve the accumulated evidence, timed responses and final intervention into
  one authored incident endpoint; `SYS-785`: persist completed chapter nodes
  and endpoint into a revisitable flowchart while leaving untraversed branch
  identities locked.
- Resolution order: accept navigation or clue interaction; validate reach and
  eligibility; expose and scrub any reconstruction; register the resulting
  fact; update available responses and success estimate; accept or time out the
  current response opportunity; update trust and incident pressure; resolve the
  final branch; store the traversed node sequence; display and later reopen the
  retained chapter flowchart. Claims: `DBH-005`–`DBH-010`.

### Constraint Genes

- Existing `CON-282`: the first chapter's investigation, rooftop entry,
  dialogue and final settlement require their authored predecessor, evidence
  and location gates.
- New `CON-597`: a live authored incident can close an evidence, response or
  intervention opportunity when its scene pressure or displayed decision
  interval expires; an unanswered option cannot be selected retroactively.
- Scarce resources: incident time, currently open response window, available
  evidence, negotiation advantage, actor viability and the one unreplayed
  branch. Exact countdown lengths, percentage values and option labels remain
  parameters. Claims: `DBH-004`–`DBH-008`.

### Information Genes

- Existing `INF-125`: current objective, eligible investigation focus and
  chapter transition are inspectable; `INF-148`: the dialogue interface exposes
  the current response set and its timing while keeping downstream consequence
  details concealed.
- New `INF-307`: the negotiation surface displays the current estimated success
  probability and updates it after evidence, dialogue and intervention changes;
  it does not promise a particular future branch. New `INF-308`: the completed
  chapter flowchart distinguishes visited nodes and the reached endpoint from
  locked alternative paths without naming every untraversed consequence.
- Exact icons, colours, font, line geometry, percentage values and node names
  are presentation or run parameters. Claims: `DBH-005`–`DBH-009`.

### Objective Genes

- New `OBJ-157`: investigate and resolve one live authored incident into a
  retained branch endpoint. For this reproducible trace, Emma's release,
  Connor's survival and the retained `Snipers Shot Deviant` flowchart endpoint
  are positive; a death/failure endpoint is evaluated but negative. The whole
  story, all branches and full flowchart completion are excluded. Claims:
  `DBH-004`–`DBH-010`.

### Time Genes

- Existing `TIM-003`: incident pressure, actor danger and bounded response
  opportunities progress in real time while Connor can navigate, investigate
  and respond. A paused flowchart and menu inspection do not create a second
  gameplay time model. Claims: `DBH-004`–`DBH-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh `Experienced` story has loaded the first chapter | Retain first control when the elevator opens | Connor enters the live apartment investigation with no prior chapter path | exact entry | `DBH-003`, `DBH-004` |
| An eligible body or scene object is reachable | Inspect its accepted evidence points | The authored clue and any reconstruction become available | bounded evidence interaction | `DBH-005` |
| A reconstruction exposes a fixed past interval | Move its cursor to the accepted causal point | The authored past event completes and registers its fact without changing live history | observational reconstruction | `DBH-005` |
| Gun case, child-room, father, officer and blue-blood facts are registered | Enter the rooftop confrontation | Named/contextual response options and the strongest available negotiation state are admitted | evidence-to-negotiation transfer | `DBH-005`, `DBH-006` |
| One timed response set is open | Choose the listed response before expiry | Trust, incident state and displayed success estimate update; alternatives close for this run | consequence-bearing dialogue | `DBH-006` |
| The wounded officer remains exposed and Daniel objects | Obey and do not aid the officer | The intervention closes without the trust loss caused by defiance | timed non-action as branch input | `DBH-006`, `DBH-007` |
| Daniel demands the helicopter leave | Choose `Accept` | The helicopter withdraws and the current success estimate rises for the selected route | world intervention through dialogue | `DBH-006`, `DBH-007` |
| Maximum negotiation advantage has been reached through the listed trace | Choose `Reassure` at the final commitment | Daniel releases Emma; snipers kill Daniel; Connor survives | reproducible positive incident outcome | `DBH-007` |
| The authored incident has settled | Accept the chapter transition | A flowchart marks the traversed nodes and `Snipers Shot Deviant` endpoint while leaving alternatives locked | evaluated chapter settlement | `DBH-008`, `DBH-009` |
| The completed flowchart has been exited without replay | Reopen `The Hostage` flowchart from the chapter surface | The same visited nodes and endpoint remain recorded | positive retained terminal | `DBH-009`, `DBH-010` |

## Strategic and experiential structure

- Planning horizon: acquire enough authored causal facts before rooftop entry
  that the live negotiation exposes high-leverage responses and a strong
  success estimate, then preserve trust through each closing opportunity.
- Local tactics: scan the current room, inspect one eligible point, scrub any
  reconstruction to its causal instant, read the newly learned fact and decide
  whether remaining incident time justifies another clue before advancing.
- Medium-term structure: evidence changes later choice availability and
  effectiveness; each rooftop commitment changes trust, the displayed estimate
  and the next response set; closed options cannot be recovered without replay.
- Reversible versus irreversible: navigation and reconstruction scrubbing are
  revisable before commitment; registered facts persist through the chapter;
  each timed response closes alternatives; incident settlement fixes the path
  recorded by the flowchart.
- Failure attribution: missing evidence explains absent contextual responses;
  the timer explains expired choices; the success estimate explains current
  negotiation direction without guaranteeing it; the flowchart attributes the
  actual traversed node sequence and endpoint.
- Player trust: a discovered fact must affect the declared option set or
  estimate consistently, choice timing must close visibly, and the same settled
  path must remain inspectable after leaving the flowchart. Claims:
  `DBH-005`–`DBH-010`.

## Replay and variation

- The apartment, evidence, reconstruction contents, dialogue tree and legal
  incident endpoints are authored and fixed. Inspection order, missed clues,
  response timing and selected options vary the reached path.
- `Experienced` permits the complete control and death opportunity set used by
  this packet; `Casual` is excluded rather than merged as a parameterless
  variant.
- Replay can reveal alternative nodes and consequences, but the canonical
  trace deliberately performs one fresh path and only reopens its completed
  flowchart. It does not overwrite or complete the branch graph.
- Later consequences may carry into the full story, but their systems and
  outcomes are outside the chapter terminal and are not inferred here.

## Adjacent systems and history

- Her Story also turns authored evidence into later discovery, but uses
  arbitrary transcript queries and immutable video records without a live
  incident, embodied scene reconstruction, timed dialogue or validated branch
  endpoint.
- Papers, Please also converts visible evidence into a terminal decision, but
  checks one document packet against a daily policy and delays citations rather
  than changing a negotiated success estimate and authored story graph.
- A Way Out shares direct movement, contextual interactions and an authored
  retained story segment, but requires two simultaneous human roles and passed
  shared-object coordination rather than evidence-conditioned solo choices.
- Kingdom Come: Deliverance II shares retained authored quest choices and timed
  responses, but carries character, inventory, combat and recipe state into a
  successor quest rather than settling one incident into a traversed flowchart.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-232`, `ACT-341`, `ACT-427` | actor, clue, reconstruction cursor, response and prompt |
| System Behaviour | `SYS-379`, `SYS-680`, `SYS-783`, `SYS-784`, `SYS-785` | evidence, trust, outcome and retained path |
| Constraint | `CON-282`, `CON-597` | authored order and closing incident opportunity |
| Information | `INF-125`, `INF-148`, `INF-307`, `INF-308` | objective, option, probability and flowchart presentation |
| Objective | `OBJ-157` | incident, protected actor, endpoint and retention check |
| Time | `TIM-003` | continuous incident and response timing |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `251` (`GAME-0001`–`GAME-0251`).
- Exact genome matches: none.
- Tied near matches: `GAME-0240` — Kingdom Come: Deliverance II (`8 / 34 = 0.235294`).
- Supported combination subsets: `COMB-0250`.
- Scan date: 2026-09-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0240` — Kingdom Come: Deliverance II | `ACT-008`, `ACT-232`, `ACT-341`, `SYS-379`, `CON-282`, `INF-125`, `INF-148`, `TIM-003` | Both traverse an authored real-time story route, inspect context and commit bounded responses whose state persists. Kingdom Come carries inventory, character, recipe and combat state through a full quest to successor control; Detroit converts fixed reconstructions into a visible negotiation estimate, resolves one pressured incident and retains its traversed-versus-locked branch flowchart. | Near, `0.235294` |

### Preserved research notes

- New genes: `ACT-427`, `SYS-783`, `SYS-784`, `SYS-785`, `CON-597`,
  `INF-307`, `INF-308` and `OBJ-157`.
- Reused genes: `ACT-008`, `ACT-232`, `ACT-341`, `SYS-379`, `SYS-680`,
  `CON-282`, `INF-125`, `INF-148` and `TIM-003`.
- Classification result: `New combination of known and new genes`.
- Evidence and reasoning: existing embodied navigation, authored dialogue,
  contextual evidence interaction, retained quest state, investigation
  progress, ordered gates, current objectives and real-time pressure transfer
  without names from this chapter. New terms isolate an observational time
  scrub, evidence-conditioned negotiation, branch settlement/persistence and
  two information contracts absent from the lower-ID corpus.
- Lower-ID scan: reject `ACT-030`, because Connor navigates a live embodied
  incident and scrubs reconstructed intervals rather than moving an observation
  pointer through one immutable tableau; reject `ACT-044`, because the scrub
  does not restore or branch live simulation state; reject `ACT-261`, because
  response prompts select authored actions/options rather than hitting a moving
  success interval; reject `SYS-149`/`CON-168`, because branches are committed
  by dialogue and intervention rather than spatial thresholds and narrator
  response; reject `SYS-371`, because the endpoint does not select a permanent
  controllable roster; reject `SYS-780`/`OBJ-155`, because terminal validity is
  the retained flowchart endpoint, not ordinary control in a successor action
  chapter; reject `INF-293`/`OBJ-151`, because there is no custody score/rank or
  investigative episode successor; reject `OBJ-052`, because the chapter
  endpoint is not a complete-run narrative ending and replay boundary.

## Taxonomy impact

- Registry changes: eight new Active genes and nine reused transfers. No prior
  definition, lifecycle state or reviewed game signature changes.
- Taxonomy-change record: none; this is additive game-unit taxonomy work.
- Candidate terms affected: recorded in `CANDIDATE_TERMS.md`; product,
  character, chapter, scene, option, ending and numeric labels remain
  game-scoped parameters.

## Negative results

- No direct-play, local-entitlement, screenshot, video, audio or acting-analysis
  claim. No PlayStation evidence is used to identify the current PC build.
- No whole-story, three-protagonist, all-ending, replay, platform, difficulty,
  demo, streaming-vote or live-service union.
- No earlier reviewed signature, definition or lifecycle state changes.

## Combination subset scan

- Every verified combination in the pre-unit registry is tested as a proper
  subset of this seventeen-gene signature; none of the 249 earlier
  combinations fits completely. `COMB-0250` records the strict fourteen-gene
  evidence, negotiation, pressured branch and retained-flowchart core; it omits
  generic quest-state carry, ordered campaign gates and current-objective UI.
- Comparison and subset scan date: 2026-09-05.

## Delta summary

## New facts

- [Confirmed | Direct | High] Current Windows product, input, language,
  difficulty distinction, first-scene investigation and flowchart contracts
  are fixed in `DBH-001`–`DBH-005` and `DBH-009`.
- [Observation | Corroborated | High] The exact evidence/response route, live
  success estimate and retained `Snipers Shot Deviant` terminal are fixed in
  `DBH-006`–`DBH-010`.

## New genes

- [Observation | Corroborated | High] `ACT-427` scrubs one fixed reconstructed
  event; `SYS-783` converts registered evidence into negotiation options and
  advantage; `SYS-784` resolves the incident branch; `SYS-785` retains its
  traversed path.
- [Observation | Corroborated | High] `CON-597` closes timed incident
  opportunities; `INF-307` exposes current success estimate; `INF-308` exposes
  visited versus locked branch state; `OBJ-157` fixes the retained incident
  endpoint.

## New combinations

- [Strong Pattern | Corroborated | High] `COMB-0250` captures an embodied
  evidence investigation whose fixed reconstructions change timed negotiation
  options and a visible success estimate before one incident settles into a
  revisitable traversed-versus-locked branch map.

## Taxonomy changes

- [Observation | Corroborated | High] None: all changes are additive and no
  earlier reviewed game signature changes.

## New questions

- Does the completed nine-game batch preserve every product/scope, taxonomy,
  language, artwork, generated-index and comparison contract at 252 games?

## Next recommended unit

- [Hypothesis | Limited | High] `SEARCH_DEMAND_BATCH_013_AUDIT`.
- Optimisation criterion: independently recompute and inspect every batch-013
  record, source boundary, translation, image, index, relation and release gate.
- Expected information gain: distinguish local unit success from batch-level
  parity and catch cross-unit drift before any separate publication decision.
- Backlog impact: closes the approved batch-013 Goal without pushing,
  publishing a corpus revision, tagging or deploying.

## Why this unit

- [Hypothesis | Limited | High] Nine individually complete commits still need a
  single independent 252-game audit of aggregate totals, localisation,
  generated artifacts, comparison parity and browser accessibility.
