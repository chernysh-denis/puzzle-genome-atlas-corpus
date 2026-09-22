---
game_id: GAME-0359
slug: crimson-skies-high-road-to-revenge
game_title: "Crimson Skies: High Road to Revenge"
analysis_status: reviewed
reviewed: 2026-09-22
combination_ids: []
gene_ids:
  action:
    - ACT-161
    - ACT-341
    - ACT-392
    - ACT-496
  system:
    - SYS-215
    - SYS-369
    - SYS-723
    - SYS-987
    - SYS-988
    - SYS-989
  constraint:
    - CON-269
    - CON-282
    - CON-578
    - CON-662
  information:
    - INF-115
    - INF-125
    - INF-268
    - INF-277
  objective:
    - OBJ-209
  time:
    - TIM-003
---

# Game: Crimson Skies: High Road to Revenge

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Nathan Zachary,
`Brooklyn` Betty, Devastator, Pandora, magnetic missiles, Desert Fox fighters
and `The Morning After` are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: original North American English Xbox retail release,
  Microsoft Game Studios product `P06-00001`, UPC `805529097681`, title ID
  `0x4D530021` / `MS-033`; a fresh campaign on the ordinary initial difficulty
  and default controls. It is not the PC predecessor, a prototype, later
  regional release, Xbox backward-compatibility wrapper, Xbox Live mode,
  modification, cheat-enabled save or completed campaign.
- Structured target: first ordinary Devastator control in Mission 1, `The
  Morning After`, through the fixed tutorial flight, recapture of Pandora,
  mission settlement, retained first Upgrade Token and first ordinary
  post-mission control inside Pandora. Stop before accepting or launching a
  Mission 2 objective.
- Entry: Nathan has the fixed Devastator, its four machine guns and finite
  magnetic-missile reserve; Betty is the moving guide; the first follow
  objective is current; no upgrade token has been earned from this mission.
- Fixed route: follow Betty to the training island; destroy the three practice
  zeppelins with primary gunfire; destroy the three training gun towers with
  magnetic missiles; demonstrate brakes, an Immelmann, a barrel roll and one
  turbo burst; fly the rock route to Pandora; destroy the required harbour gun
  towers; defeat both authored fighter waves with Betty; fly to Pandora's blue
  objective marker, accept the action prompt and let the mission settle.
- Bounded failure control: after the first cited checkpoint, duplicate the
  state, deplete armour and verify that the failed transient flight is replaced
  by the latest authored checkpoint rather than credited as mission success.
  Return to the accepted route from a clean duplicate; failure is not part of
  the positive terminal.
- Primary decision loop: read the current objective, radar, target colour,
  armour, special-energy bar and secondary reserve; steer the aircraft in
  three dimensions; use brakes or turbo to change relative geometry; trigger
  one preprogrammed manoeuvre when reversal or roll is useful; align and fire
  primary guns or finite magnetic missiles; preserve armour; clear the current
  predicate so the next instruction appears.
- Positive terminal: every required `The Morning After` predicate has settled,
  the Pandora is recaptured, the completion Upgrade Token is retained and
  ordinary post-mission control is restored inside Pandora. Destroying only
  the last fighter, reaching the blue marker without accepting it or viewing a
  transition without returned control is insufficient.
- Included: direct third-person aircraft steering; throttle-like turbo and air
  brakes; preprogrammed Immelmann/roll input; primary and finite secondary
  weapon fire; magnetic missile correction toward a near-aimed target;
  real-time craft motion, collision, armour damage and hostile combat; one
  shared special-energy reserve; current radar/objective/target/HUD feedback;
  staged tutorial order; checkpoint retry; Pandora interaction and retained
  mission token.
- Excluded: optional service-station repair, health/re-arm pickups, plane
  swapping, AA-gun control, later missions, hidden Upgrade Tokens, plane
  purchases/upgrades, races and wagers, other aircraft and secondary weapons,
  multiplayer, Xbox Live, complete campaign, cheat codes, glitches and later
  compatibility behaviour. The manual documents repair opportunities for the
  wider game, but the cited first-mission route neither requires nor
  independently locates one; repair is therefore not admitted.
- Direct-play status: not conducted. No disc, image, Xbox console, emulator,
  controller trace, profile, save, screenshot, video or audio was obtained or
  inspected. The official Microsoft manual establishes controls, HUD, weapons,
  armour, turbo, manoeuvres and general repair surfaces; the preserved Prima
  guide and two independent written routes establish the bounded first-mission
  order and terminal. This is a source-bounded reconstruction, not a claimed
  playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CSHR-001` | The packet targets the original North American English Xbox retail product `P06-00001`, UPC `805529097681`, title ID `0x4D530021` | Confirmed | Corroborated | High | P1, R1, R2 |
| `CSHR-002` | Default Xbox controls directly steer the aircraft, fire primary and secondary weapons, brake, turbo, roll, trigger special manoeuvres and accept action prompts | Confirmed | Direct | High | P1 |
| `CSHR-003` | The HUD exposes armour, crosshairs, enemy brackets, current objective and finite secondary-weapon state; the route guide additionally exposes radar colours and special energy | Confirmed | Corroborated | High | P1, P2 |
| `CSHR-004` | Turbo and preprogrammed manoeuvres draw from the same bounded special-energy reserve | Observation | Direct | High | P2 |
| `CSHR-005` | Devastator magnetic missiles correct toward a near-aimed target and consume a finite secondary reserve | Confirmed | Direct | High | P1, P2 |
| `CSHR-006` | Mission 1 teaches follow, primary targets, secondary targets, manoeuvres, turbo and the final Pandora dogfight in authored order | Observation | Corroborated | High | P2, S1, S2 |
| `CSHR-007` | Certain completed mission goals establish checkpoints, and armour depletion restores the previous checkpoint | Observation | Direct | High | P2 |
| `CSHR-008` | The final enemy wave is followed by a Pandora blue action marker whose accepted prompt ends the mission | Observation | Corroborated | High | P2, S1, S2 |
| `CSHR-009` | Completing the last task recaptures Pandora and awards the mission's only Upgrade Token | Observation | Direct | High | P2 |
| `CSHR-010` | Service stations exist generally but are not established as a required or available first-mission route step | Confirmed | Corroborated | High | P1, P2 |
| `CSHR-011` | The repository control reconstructs the cited route, special-energy sharing, finite missiles, checkpoint failure and retained terminal without executing the game | Observation | Direct | High | V1 |

## Basic data

- Release / origin: FASA Studio developed the Xbox game and Microsoft Game
  Studios published the North American release on 2003-10-21.
- Platform or physical form: licensed original North American English Xbox
  optical disc, product `P06-00001`, UPC `805529097681`, title ID
  `0x4D530021` / `MS-033`; no executable or disc image was obtained or hashed.
- Puzzle family: embodied spatial reasoning; tactical forecast and counterplay;
  real-time system pressure; ordered dependency sequencing.
- Primary sources, accessed 2026-09-22:
  - **[P1]** [official Microsoft English Xbox
    manual](https://download.microsoft.com/download/f/d/9/fd90191d-8010-4bc8-818c-a5d668ba796f/CrimsonSkies2_Manual_EN.pdf),
    preserved from Microsoft's historical download through the Internet
    Archive, pp. 8–11, 18–19 and 28–30, for controls, direct flight, weapons,
    armour, HUD, turbo, brakes, special manoeuvres, repair surfaces and action
    prompts. Preserved local SHA-256:
    `0f964a16251eb600638d7a6b179273239650f476ae8a1f685f96affec9442ce5`.
  - **[P2]** [Prima's Official Strategy
    Guide](https://www.ogxbox.co.uk/media/com_eshop/attachments/Crimson_Skies_High_Road_To_Revenge_Strategy_Guide_2004_Book.pdf),
    pp. 4–5 and 23–25, for special energy, radar colours, checkpoints, the
    complete first-mission route, Pandora prompt and Upgrade Token. Preserved
    local SHA-256:
    `b2da70af67f9f63c9a0eb6c78f0a61659ab5d708905ac67b0b7c795ac96e8e4a`.
  - **[P3]** [official Xbox product
    page](https://www.xbox.com/en-us/games/store/crimson-skies-high-road-to-revenge/c4b8xr1lcxr5),
    used for licensed title and publisher identity only, not to infer exact
    mechanical parity with the current compatibility wrapper.
- Reproducible identity sources:
  - **[R1]** [GameFAQs original-Xbox release-data
    record](https://gamefaqs.gamespot.com/xbox/559078-crimson-skies-high-road-to-revenge/data),
    for Microsoft Game Studios, `P06-00001`, UPC `805529097681` and the North
    American 2003-10-21 release.
  - **[R2]** [xemu title record](https://xemu.app/titles/4d530021/), for title ID
    `0x4D530021` / `MS-033`; it identifies the carrier and does not claim that
    emulation was performed.
- Corroborating written sources, accessed 2026-09-22:
  - **[S1]** [GameFAQs original-Xbox written
    walkthrough](https://gamefaqs.gamespot.com/xbox/559078-crimson-skies-high-road-to-revenge/faqs/28730),
    `The Morning After`, for the fresh setup, Devastator, Betty route, three
    practice targets, gun towers, brakes/turbo, manoeuvres, Pandora battle and
    post-mission transition.
  - **[S2]** [CheatCodes written original-Xbox
    walkthrough](https://www.cheatcodes.com/guide/my-faq-and-walkthrough-crimson-skies-high-road-to-revenge-xbox-47267/),
    `The Morning After`, for the independently matching follow, target,
    manoeuvre, boost, harbour and fighter sequence.
- Validation source: **[V1]**
  [`verify_crimson_skies_control.py`](../../../scripts/verify_crimson_skies_control.py),
  an executable transition reconstruction over the cited relations. It does
  not execute Crimson Skies.
- Claim IDs: `CSHR-001`–`CSHR-011`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-161`: align the current weapon toward one eligible practice
  target, tower or hostile aircraft and commit primary or secondary fire.
- Existing `ACT-341`: accept the blue Pandora action prompt after every combat
  predicate is closed.
- Existing `ACT-392`: continuously steer the Devastator through open
  three-dimensional space; this arcade craft does not use the runway/system
  boundary excluded by the gene.
- New `ACT-496`: trigger one authored aircraft manoeuvre or turbo burst from
  the directly controlled flight state.
- Exact bindings, turn rates and manoeuvre animations are parameters. Claims:
  `CSHR-002`, `CSHR-004`–`CSHR-006`, `CSHR-008`.

### System Behaviour Genes

- Existing `SYS-215`: guns, missiles, towers and fighters exchange damage in
  live time until the current hostile predicate settles.
- Existing `SYS-369`: armour depletion replaces failed transient state with
  the latest authored mission checkpoint.
- Existing `SYS-723`: steering and collision continuously update craft motion
  and can convert unsafe contact into armour damage.
- New `SYS-987`: a fired magnetic missile consumes one finite secondary use
  and corrects its path toward the eligible target near the aiming relation.
- New `SYS-988`: turbo and preprogrammed manoeuvres consume one shared special-
  energy reserve whose remaining value gates further use and recovers under
  the carrier rule.
- New `SYS-989`: the first mission advances through its ordered tutorial and
  combat predicates, then the accepted Pandora marker settles recapture,
  Upgrade Token and restored post-mission control.
- Claims: `CSHR-003`–`CSHR-009`.

### Constraint Genes

- Existing `CON-269`: weapons and the Pandora action require a legal target,
  spatial relation, current readiness and applicable resource.
- Existing `CON-282`: follow, target-practice, secondary-weapon, manoeuvre,
  turbo, harbour and fighter predicates must settle in authored order.
- Existing `CON-578`: magnetic-missile fire requires a positive compatible
  secondary reserve.
- New `CON-662`: turbo and preprogrammed manoeuvres compete for one bounded
  special-energy reserve rather than independent allowances.
- Armour, geometry, ammunition and special energy are the bounded local
  resources. Claims: `CSHR-004`–`CSHR-008`.

### Information Genes

- Existing `INF-115`: the third-person view and sound expose visible local
  terrain, projectiles, towers, aircraft and collision risk.
- Existing `INF-125`: the radar/map exposes current coloured contacts and the
  current objective marker without revealing hidden future waves.
- Existing `INF-268`: Betty's staged instruction explains the current taught
  flight or combat predicate and acknowledges its completion.
- Existing `INF-277`: the craft HUD exposes armour, crosshairs, target brackets,
  secondary weapon/uses, special energy and current objective state.
- Claims: `CSHR-003`, `CSHR-006`–`CSHR-008`.

### Objective Genes

- New `OBJ-209`: complete `The Morning After`, recapture Pandora, retain its
  completion Upgrade Token and regain ordinary post-mission Pandora control.
- Optional repair, hidden collection and every later mission remain outside
  the objective. Claims: `CSHR-006`, `CSHR-008`–`CSHR-010`.

### Time Genes

- Existing `TIM-003`: craft motion, hostile motion, projectiles, armour damage,
  special energy, objective response and player input advance concurrently
  outside blocking transitions. Claims: `CSHR-002`–`CSHR-008`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| First Devastator control; Betty and follow objective active | steer after Betty | craft motion follows direct input while radar marks Betty as friendly and the current destination in yellow | exact entry and direct flight | `CSHR-002`, `CSHR-003`, `CSHR-006` |
| Three practice zeppelins are current | align and fire primary guns until each is destroyed | live hits reduce target state and clearing all three exposes the secondary-weapon lesson | primary combat gate | `CSHR-005`, `CSHR-006` |
| Three training gun towers are current and magnetic missiles remain | aim near a tower and fire the secondary weapon | one missile use is debited, the projectile corrects toward the target and sufficient hits destroy it | finite guided secondary | `CSHR-005`, `CSHR-006` |
| Special-flight lesson is current | brake, trigger Immelmann and barrel roll, then engage turbo | the commanded manoeuvres alter orientation while manoeuvres/turbo consume the common special reserve | shared manoeuvre economy | `CSHR-002`, `CSHR-004`, `CSHR-006` |
| Pandora harbour objective is current | use the rock approach and destroy required gun towers | hostile structures settle under live combat and the first fighter wave becomes current | authored harbour gate | `CSHR-006` |
| One fighter wave remains | steer, brake or manoeuvre for geometry and attack visible hostiles | all required fighters must be defeated before the next wave or terminal marker is exposed | dogfight predicate | `CSHR-006`, `CSHR-008` |
| Armour reaches zero after a checkpoint | accept failure resolution | failed transient positions/damage are discarded and the latest checkpoint is restored | checkpoint failure branch | `CSHR-007` |
| Both waves and harbour targets are cleared | fly to the blue Pandora marker and press the action input | mission settles, Pandora is recaptured, one completion token is credited and post-mission control returns inside Pandora | exact retained terminal | `CSHR-008`, `CSHR-009` |

## Edge-case audit

- `ACT-321`, `SYS-556` and `CON-472` are rejected: this mission starts already
  airborne and models arcade open-space steering, not runway take-off,
  aerodynamic envelope management or landing rollout.
- `SYS-726` is rejected despite missiles: it couples selected-target lock,
  incoming hostile locks and finite countermeasures. The Devastator packet
  establishes near-aim magnetic correction but no countermeasure loop.
- `SYS-728` and `OBJ-141` are rejected: `Form the Vanguard` settles into a
  debrief medal, while `The Morning After` settles Pandora recapture, a token
  and returned interior control.
- `ACT-393`, `SYS-724` and `CON-565` are rejected: special energy is spent by
  turbo and manoeuvres; the player does not reallocate one live power budget
  among engines, lasers and shields.
- `SYS-738`, `CON-571` and `INF-280` are not admitted. One independent route
  mentions primary-gun overheating, but the official manual and bounded Prima
  first-mission route do not establish the complete heat/cooling information
  loop required by those genes.
- General service-station repair and dropped health/re-arm pickups remain
  excluded because the accepted first-mission route does not establish a
  required, repeatable or even located repair opportunity.

## Strategic and experiential structure

- Local decision: convert the current radar/contact geometry into steering,
  brake, turbo, manoeuvre and weapon timing while preserving armour and finite
  missiles.
- Medium horizon: spend special energy to reach or reverse on a target without
  exhausting the same reserve needed for later manoeuvres; decide when a
  magnetic missile is worth its finite use instead of primary gunfire.
- Long horizon: learn one flight/combat dependency at a time, then combine them
  against towers and two fighter waves before committing the Pandora return.
- Failure attribution: target colour and objective text separate wrong target
  from incomplete gate; armour distinguishes accumulated damage; the special
  bar and secondary display distinguish depleted flight/weapon resources;
  checkpoint restoration distinguishes failure from mission settlement.
- Player trust: equivalent target sets, resource debits, checkpoint triggers
  and the Pandora prompt must settle identically under the pinned ruleset.

## Replay and variation

- Tutorial order, target classes, Pandora harbour, wave order, checkpoint
  milestones, terminal interaction and completion token are authored.
- Exact flight line, weapon mix, target order within a simultaneous group,
  damage, remaining missile count and special-energy spend may vary.
- No procedural arena, random weapon, service economy or later open-objective
  selection is admitted. Replay motives are cleaner flying, faster target
  acquisition and more conservative resource use.

## Adjacent systems and history

- `GAME-0225` STAR WARS: Squadrons is the anticipated strongest neighbour:
  both combine direct four-axis craft flight, live targeted combat, ordered
  objectives, cockpit/HUD state and shared real time. Squadrons adds subsystem
  power allocation, directional shields, countermeasures and AI resupply;
  Crimson Skies instead uses arcade brakes, preprogrammed manoeuvres, one
  shared special-energy reserve and a Pandora/token terminal.
- `GAME-0355` Metroid Prime shares a guided combat tutorial and target-state
  presentation but keeps avatar exploration/scan fixtures and a capability-
  loss terminal rather than direct aircraft flight.
- Later Crimson Skies service stations, plane swaps and open objective nodes
  are possible modules, not evidence that Mission 1 already contains them.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-161`, `ACT-341`, `ACT-392`, `ACT-496` | craft, bindings, brake, manoeuvre and turbo parameters |
| System Behaviour | `SYS-215`, `SYS-369`, `SYS-723`, `SYS-987`, `SYS-988`, `SYS-989` | combat, checkpoint, motion, missile correction, shared energy and settlement |
| Constraint | `CON-269`, `CON-282`, `CON-578`, `CON-662` | target/resource legality, authored order, finite missiles and shared energy |
| Information | `INF-115`, `INF-125`, `INF-268`, `INF-277` | local view, radar/objective, staged instruction and craft HUD |
| Objective | `OBJ-209` | mission, Pandora, token and successor control are parameters |
| Time | `TIM-003` | live flight/combat cadence is a parameter |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `358` (`GAME-0001`–`GAME-0358`).
- Exact genome matches: none.
- Tied near matches: `GAME-0225` — STAR WARS: Squadrons (`11 / 31 = 0.354839`).
- Supported combination subsets: none.
- Scan date: 2026-09-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0225` — STAR WARS: Squadrons | `ACT-161`, `ACT-392`, `SYS-215`, `SYS-723`, `CON-269`, `CON-282`, `INF-115`, `INF-125`, `INF-268`, `INF-277`, `TIM-003` | Both use direct four-axis craft flight, live attack, damaging collision, legal-resource gates, authored objectives, staged instruction, local danger and a craft-status display. Squadrons adds subsystem allocation, directional shields, lock/countermeasure defence and AI resupply; Crimson Skies adds discrete arcade manoeuvres, finite near-aim magnetic missiles, one shared turbo/manoeuvre reserve, checkpoint return and the Pandora/token terminal. | Near, `11 / 31 = 0.354839` |

### Preserved research notes

- New genes: `ACT-496`, `SYS-987`, `SYS-988`, `SYS-989`, `CON-662` and
  `OBJ-209`.
- Classification result: six new boundaries plus reused flight, attack,
  interaction, combat, checkpoint, collision, legality, order, finite-ammo,
  information and real-time boundaries.
- Evidence and reasoning: complete lower-ID transfer tests reject runway
  simulation, Squadrons' countermeasure/power/medal packet and generic
  checkpoint/mission terminals where their causal state differs.

## Taxonomy impact

- Registry changes: add `ACT-496`, `SYS-987`–`SYS-989`, `CON-662` and
  `OBJ-209` under
  [`TAXONOMY_CHANGE_098`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_098.md).
- Lifecycle changes: none. Earlier signatures remain unchanged.

## Delta summary

## New facts

- [Confirmed | Direct | High] The official Xbox manual separates direct
  steering, primary/secondary fire, turbo, brakes, special manoeuvres, armour,
  targeting and the action prompt (`CSHR-002`, `CSHR-003`, `CSHR-005`).
- [Observation | Corroborated | High] The cited first mission joins those
  controls in an ordered training-to-harbour route and settles only after the
  Pandora prompt, token credit and returned interior control
  (`CSHR-006`–`CSHR-009`).

## New genes

- [Observation | Corroborated | High] Add `ACT-496`, `SYS-987`–`SYS-989`,
  `CON-662` and `OBJ-209` under `TAXONOMY_CHANGE_098`.

## New combinations

- [Observation | Direct | High] No verified combination is registered from one
  new carrier.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_098` adds six boundaries
  and preserves every earlier signature and lifecycle state.

## Negative results

- `ACT-321`, `SYS-556` and `CON-472` remain fixed-wing runway/aerodynamic
  boundaries; no take-off, landing or cockpit-system chain is scoped here.
- `SYS-726` cannot be reused partially because its incoming-lock and
  countermeasure branch is absent.
- `ACT-393`, `SYS-724` and `CON-565` allocate power among three subsystems;
  Crimson Skies instead consumes one common reserve through two action classes.
- `SYS-728`/`OBJ-141` require Squadrons' debrief medal, while this terminal
  returns to Pandora with an Upgrade Token.
- `SYS-738`, `CON-571` and `INF-280` remain excluded because the bounded
  first-mission evidence does not establish the complete weapon-heat loop.
- Service-station repair remains outside scope despite its general manual
  documentation; no unsupported first-mission placement is inferred.

## Open questions

- Exact internal armour values, checkpoint serialization, magnetic correction
  strength, missile count, special-energy drain/recovery constants, fighter
  counts and ordinary difficulty label remain parameters because no executable
  or direct trace was inspected.
- A later Sea Haven module could test service-station repair, plane switching
  and open objective selection without changing this first-mission packet.

## Reproducibility notes

- Record the original North American retail identifiers before applying route
  claims and keep the compatibility wrapper outside the ruleset.
- Preserve the exact positive terminal: accepted blue Pandora marker,
  completion token and returned post-mission control.
- Keep the armour-depletion checkpoint branch separate from success and record
  the latest crossed checkpoint rather than assuming save-file persistence.
- Treat all exact resource values and fighter counts not jointly established by
  the cited packet as parameters, not invented rules.
- Treat the verifier as a transition proof over written evidence, not an
  emulator, timing measurement or binary execution.

## Localisation review

- Ukrainian profile, scope, direct-play statement, presentation, six new gene
  definitions and every plain-language card are reviewed in this unit under
  [`UKRAINIAN_LOCALISATION_POLICY`](../../../docs/UKRAINIAN_LOCALISATION_POLICY.md).
- `verified`: Crimson Skies: High Road to Revenge, Xbox, Microsoft Game
  Studios, FASA Studio, Nathan Zachary, `Brooklyn` Betty, Devastator, Pandora,
  `The Morning After`, Upgrade Token, Immelmann and stable product/title IDs
  remain official names, evidence labels or identifiers.
- `corrected`: all explanatory Ukrainian prose is authored naturally and keeps
  actors, inputs, resource sharing, order, failure branch, terminal and
  exclusions intact.
- `retained-with-reason`: remaining Latin-script terms are only the official
  product, character, craft, place, mission, manoeuvre and identifier labels
  above; no generic English prose is deferred to a later batch.
