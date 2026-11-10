---
game_id: GAME-0508
slug: ready-or-not
game_title: Ready or Not
analysis_status: reviewed
reviewed: 2026-10-06
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-189
    - ACT-202
    - ACT-215
    - ACT-303
    - ACT-341
    - ACT-409
    - ACT-697
    - ACT-698
    - ACT-699
    - ACT-700
    - ACT-701
    - ACT-702
  system:
    - SYS-051
    - SYS-208
    - SYS-215
    - SYS-292
    - SYS-297
    - SYS-318
    - SYS-538
    - SYS-773
    - SYS-1425
    - SYS-1426
    - SYS-1427
    - SYS-1428
    - SYS-1429
    - SYS-1430
    - SYS-1431
  constraint:
    - CON-175
    - CON-262
    - CON-285
    - CON-287
    - CON-769
    - CON-785
    - CON-786
    - CON-787
    - CON-788
    - CON-789
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-299
    - INF-388
    - INF-492
    - INF-493
    - INF-494
  objective:
    - OBJ-289
  time:
    - TIM-003
---

# Game: Ready or Not — first Commander deployment and roster return

Use the canonical [vocabulary and signature](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Weapon names, officer identities, ammunition, armor, mission labels, geometry,
score, stress bands and device coefficients are parameters, not extra genes.

## Analysis scope

- Version / ruleset: full-release Windows Steam base Ready or Not, application
  1144200, original 1.0 rules dated 2023-12-13; fresh ordinary non-Ironman
  Commander. R1's pause view displays build label 39903 DEC 13, 2023. That
  observation is not a verified distribution Build ID, checksum, mod audit or
  own executable run. The December 18 hotfix and later console updates do not
  silently replace these rules. Product release is established by P4/P8.
- Structured analysis target: PLAT-WINDOWS-PC; English base-game Commander,
  Thank You, Come Again at the gas station. Practice, cooperative play,
  Ironman, DLC and the whole campaign are different targets.
- Primary decision loop: compose and equip Judge's available four-officer
  element; consult partial briefing, inspect each reachable route and contact,
  direct red/blue/all officers to cover or enter, choose compliance, eligible
  restraint, less-lethal tools or justified force, register people and evidence,
  then settle the deployment into the mission report and retained HQ roster.
  Contact compliance, squad exposure and post-mission officer stress couple
  preparation, local intervention and the terminal personnel decision.
- Entry and exit: begin at the fresh ordinary Commander HQ after onboarding,
  before assigning equipment and committing the first gas-station mission.
  Include all offered preparation alternatives and reachable interventions in
  that mission, not only the recording's rifle route. The positive terminal
  is an accepted first-mission result, return to HQ with retained officer
  identities/stress and exposed 23 Megabytes a Second availability. Stop before
  deploying into that second mission. Premature spawn-point exfil, player
  death or an unsuccessful result is not positive completion. Mission-end
  permission alone does not establish a perfect grade; no universal exact
  grade threshold for unlocking is inferred from R1's successful return.
- Included: available roster recruitment/dismissal/assignment and therapy;
  compatible weapon, attachment, armor, headwear and shared munitions slots;
  four AI officers and subgroup selection; direct walking/posture/lean, aiming,
  firing, slot switching, magazine reload, tactical throws and interaction;
  squad movement/stack/entry/security, unlocked or locked/wedged/breached doors;
  local hostile perception and movement; surrender, fake surrender, flight,
  force, restraint, reporting and evidence; documented ballistic penetration,
  facing-dependent armor and ceramic wear; local cameras/light/night vision;
  health, bleeding and intended self-bandaging with launch bugs qualified;
  mission objectives, optional proof, conduct evaluation, exit and HQ personnel
  settlement. Exact numerical coefficients and bug-free execution are not
  asserted. Preparation alternatives remain causal even when R1 equips another.
- Excluded: Early Access as the analysis target; later missions, DLC, multiplayer,
  Practice, Ironman save deletion, replay viewer, achievements, cosmetic watch
  and clothing unlocks, HQ shooting-range/minigame scoring; active trait effects
  requiring further mission experience. First-packet traits are visibly locked.
  No trap on a gas-station door, infinite ammunition, automatic full health
  recovery, mandatory perfect grade or all-NPCs-alive condition is invented.
  Authored pre-existing bodies are not evidence that the player killed them.
- Potential scoped modules: another mission, unlocked trait deployment,
  Ironman loss, cooperative entry, Practice and each DLC require their own
  dated rules and terminal evidence. No module identifier is allocated here.
- Direct-play status: not conducted. Official release/development statements,
  launch recording R1 and qualified contemporary writing reconstruct the
  packet. No own game input, native timing, binary, save/reload, random seed or
  original coefficients were inspected. The complete official December 13,
  2023 release statement was read through Steam ISteamNews. Pre-release
  Commander and squad descriptions are work in progress; intentions do not
  automatically establish shipped rules. Attributed launch recording Casas
  Plays R1 shows four officers' assignment/equipment, local entry, restraint,
  actor reporting, separate evaluation categories, return with Anxious or
  Content states and next-mission availability. Traits remain locked. Label
  39903 DEC 13, 2023 is not a verified unmodified executable. Selected paused
  frames, not the entire continuous playthrough, were inspected; black frames
  were rejected, later missions excluded and the animating score rejected as
  an exact final total. Creator recording P5 shows entry preparation and cover,
  not measurements of every squad procedure. Contemporary post-hotfix guides
  corroborate only qualified boundaries. Earlier treatment documentation and
  launch bug reports leave intended self-bandaging Limited/Medium, not flawless
  original-launch execution; exact headwear protection and rejection of
  incompatible shield weapons were likewise not measured. Metadata-only R2
  and inaccessible S5 do not establish admitted mechanics. All video inspection
  was headless/background, muted and paused; audio was neither played nor
  analysed. No foreground/fullscreen, focus, user-window/tab or system-sound
  change occurred. Source frames and working material are not redistributed.
  Original artwork illustrates a possible contact/security state, not a game
  screenshot or an official asset.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| RON-001 | Full 1.0 release is dated December 13, 2023; ordinary Commander is distinct from Ironman and Practice. Exact inspected binary provenance is unverified. | Observation | Corroborated | High | P1/P4/P8; R1 120/950 |
| RON-002 | Four assigned AI officers retain separate identities/loadouts; reserves, recruitment and dismissal change future deployment assignment. | Observation | Corroborated | High | P1/P2; R1 180/220/1585/1600/1650 |
| RON-003 | Preparation exposes compatible guns, attachments and armor; primary/sidearm magazines and tactical utility share an armor-dependent allowance. | Observation | Corroborated | High | R1 440/480/680/710; S3/S6; P1 |
| RON-004 | Direct movement, posture, weapon choice, fire and reload coexist with material-dependent projectiles, armor facing and ceramic deterioration. | Observation | Corroborated | High | P1/P7; R1 850–1450 |
| RON-005 | Addressed squad procedures use selected subgroups, current doors and carried equipment; known launch bugs preclude guaranteed flawless queuing or securing. | Observation | Corroborated | Medium | P1/P3/P5/P6; R1 850/1000/1050/1100/1250 |
| RON-006 | Local contact response includes resistance, surrender, fake surrender, flight and violence; pepper exposure need not disable shooting. | Observation | Direct | High | P1; R1 900/1470 corroborates custody states, not every alternative |
| RON-007 | Compliant reachable restraint, actor reporting and securing proof are different from killing or merely seeing a contact/item. | Observation | Corroborated | High | P1; R1 900/1150/1470/1490; S1 |
| RON-008 | Missing arms can prevent ordinary restraint; ballistic effects and available access must not be reduced to a generic kill counter. | Observation | Direct | High | P1 |
| RON-009 | Open, locked, wedged and breached door states affect local passage and entry; exact native wedge/AI reliability is unverified. | Observation | Corroborated | Medium | P1/P3; R1 1000/1050; S3/S6/S10 |
| RON-010 | Flashlight, Mirror Gun, NVGs and protective headwear are causal alternatives; precise launch visual/protection coefficients are unmeasured. | Observation | Limited | Medium | R1 440/710; P1; S3/S4/S6/S11 |
| RON-011 | Briefing and camera feeds supply partial mediated knowledge, not an omniscient live contact map. | Observation | Corroborated | Medium | P1 New Tablet; R1 preparation; S4 |
| RON-012 | Self-bandaging exists at launch; intended bleeding control without full healing is indirect evidence and has contemporary completion/weapon-return bug qualifications. | Observation | Limited | Medium | S8 earlier account; S9 launch reports; P6 animation fix |
| RON-013 | R1 distinguishes mission-end permission, four main flags, optional veteran proof, categorized conduct and HQ return; an animating score is not a measured final grade. | Observation | Corroborated | High | R1 1150/1470/1480/1490/1500/1550/1575; S1/S7 |
| RON-014 | Surviving officers can return Anxious or Content; stress/treatment and resignation risk persist independently of physical survival. Operational traits are still locked after this first packet. | Observation | Corroborated | High | P1/P2; R1 1500/1585/1600/1650; S2 |
| RON-015 | Spawn-point early exfil is distinct from completion and reduces stress relative to quitting; unpaused mission actors continue in real time. | Observation | Corroborated | High | P1; R1 120/850/950/1470 |
| RON-016 | Shield and sidearm pairing is documented before release and shield equipment persists into the 1.0 materials; exact native launch equip rejection is not reproduced. | Observation | Limited | Medium | P3/P9; S6; in-game description via S12 |

## Basic data

- Release / origin: VOID Interactive, full Windows release 2023-12-13; the
  earlier 2021 Early Access entry is not this target's release date.
- Platform or physical form: Windows Steam base game, ordinary English
  Commander. This target does not infer all later platform releases or parity.
- Mechanical families: reused FAM-009 tactical forecasting/counterplay,
  FAM-010 real-time systemic pressure and FAM-015 agent coordination;
  cover, contact readiness, entry geometry and personnel
  consequences are causal, not merely a police theme.
- P1: [Official 1.0 launch feature changelog](https://store.steampowered.com/news/app/1144200/view/3859085878636601509),
  December 13, 2023. Complete official BBCode was read through Steam's public
  ISteamNews interface. States release mechanics, not exact measured rates.
- P2: [Official Commander briefing, volume 63](https://store.steampowered.com/news/app/1144200/view/3801661174266563080),
  November 3, 2023; actually read, explicitly work in progress. Intended rules
  require P1 or launch corroboration rather than assumption of implementation.
- P3: [Official SWAT AI briefing, volume 64](https://store.steampowered.com/news/app/1144200/view/3835439444392378669),
  November 17, 2023; actually read, work in progress. Formation, stack and tool
  procedures do not prove flawless launch queues or every offered animation.
- P4: [Authorised full-release announcement](https://www.oneprstudio.com/ready-or-not-launches-on-december-13-2023/),
  December 8, 2023; product/date evidence, not observed gameplay.
- P5: [VOID Interactive SWAT AI vLog](https://www.youtube.com/watch?v=0nj6qWDNU0A),
  published December 12, 2023, metadata duration 845 seconds. Muted paused
  frames 60/150/270/390/510/650/760 inspected, with identity/no-ad/time checks;
  room coverage, door positions and entry presentation, not complete native
  measurement of every procedure. No audio was played or analyzed.
- P6: [Official news including first hotfix](https://store.steampowered.com/news/posts/?enddate=1702936555&feed=steam_community_announcements),
  December 18, 2023. Shield-first ordering, closed-room securing, healing
  animation and Practice spectating fixes constrain what launch can guarantee.
- P7: [Official ammunition briefing, volume 65](https://steamcommunity.com/games/1144200/announcements/detail/3887232108508303656?l=english),
  December 1, 2023; complete official BBCode actually read via Steam ISteamNews.
  Work-in-progress material penetration and weapon/tool compatibility are
  corroborated where P1 retains them. Training-only ammunition is excluded.
- P8: [Official Steam product](https://store.steampowered.com/app/1144200/Ready_or_Not/).
  Lawful access and full-release identity, not a guarantee of current-build
  parity with this dated original-1.0 packet.
- P9: [Official January Update Patch 1](https://steamcommunity.com/games/1144200/announcements/detail/3113678624632870079),
  February 4, 2022. Full official BBCode actually read through Steam ISteamNews;
  pistol-plus-shield fix is earlier implementation evidence, not proof of
  every December 2023 restriction. No EA mission inventory is imported.
- R1: [Casas Plays, 1.0 launch Commander part 1](https://www.youtube.com/watch?v=oG5ZV6CEA3Y),
  published December 13, 2023; checked metadata length 12338 seconds. Muted
  paused frames 120/180/220/280/400/440/480/510/540/570/680/710/750/850/900/
  950/1000/1050/1100/1150/1200/1250/1350/1400/1450/1470/1480/1490/1500/
  1510/1525/1540/1550/1560/1575/1585/1600/1650 actually inspected. Black
  600/1700 frames rejected; captured later-mission frames are excluded. The
  510 frame is largely black and supplies only a readable equipment panel;
  540/570 expose equipment/attachment alternatives. 1480/1490 evaluation is
  animating; no precise final total/grade is certified. Attributed recording,
  not own continuous play or proof of an unmodified executable.
- S1: [First-mission written walkthrough](https://sirusgaming.com/ready-or-not-thank-you-come-again-mission-walkthrough/),
  Kyle Christopher Go, December 19, 2023; actually read, after first hotfix.
  Corroborates objective/report identities. Universal two-evidence-per-suspect
  and automatic-end assertions are not adopted.
- S2: [Contemporary Commander roster account](https://itemlevel.net/ready-or-not-commander-mode-guide-in-1-0-roster-therapy-traits/),
  Christian Gallos, December 24, 2023; actually read, after hotfix. Exact
  treatment duration is not promoted to measured launch behavior.
- S3: [Contemporary equipment preparation](https://www.gameleap.com/articles/ready-or-not-best-weapon-loadout-for-beginners),
  Tom Collin, December 14, 2023; actually read. Product footer has the EA date
  and magazine advice is internally inconsistent; neither becomes a fixed build.
- S4: [Mirror Gun operation](https://quoramarketing.com/ready-or-not-optiwand-how-to-use/),
  December 19, 2023; actually read, post-hotfix. Exact launch sensor geometry
  and all hidden contacts are not independently established.
- S6: [Contemporary loadout alternatives](https://attackofthefanboy.com/guides/best-loadouts-in-ready-or-not/),
  Davi Braid, December 18, 2023; mechanics text actually read. Universal top
  rank, nonfatality and contradictory armor recommendations are not inherited.
- S7: [Contemporary end-permission explanation](https://attackofthefanboy.com/guides/how-to-finish-end-a-mission-in-ready-or-not-explained/),
  Davi Braid, December 15, 2023; actually read. Resolved/failed conditions can
  permit ending; permission is not a perfect evaluation or proven unlock rule.
- S8: [Earlier self-treatment account](https://gamezo.gg/how-to-heal-in-ready-or-not/),
  Burak Yazar, updated April 25, 2023; indexed full text read after direct
  access failed. Earlier intended bleeding rule, not native 1.0 execution.
- S9: [Dated launch bug reports](https://www.reddit.com/r/ReadyOrNotGame/comments/18i4iac),
  December 14, 2023; indexed dated reports read after direct access failed.
  Bandaging/weapon-return failures qualify intended reliability; no exact
  health-loss rate is extracted from player reports.
- S10: [Dated door-wedge observations](https://www.reddit.com/r/ReadyOrNotGame/comments/18jd7t9),
  December 15, 2023; indexed responses read. Restricted flanking routes do not
  prove bug-free AI pathfinding or universal perimeter safety.
- S11: [Earlier armor and headwear account](https://www.gamepressure.com/newsroom/ready-or-not-armor-types-and-magazine-pouch-materials/z246a7),
  Przemyslaw Dygas, July 4, 2022; full mechanics text read. Protective intent
  is earlier evidence paired with launch gear presence, not measured launch
  immunity. Contradictory armor counts/body coverage are not adopted.
- S12: [Shield in-game description preserved by the community](https://readyornot.wiki.gg/wiki/Tactical_Shield).
  Indexed description read; current undated presentation is not exact launch
  inspection. Sidearm compatibility corroborates P9, with Medium confidence.
- R2 metadata-only and inaccessible S5 do not supply accepted mechanical proof.
  Evidence checked October 6, 2026. Claim IDs: RON-001–RON-016.

## Mechanical decomposition

### Action Genes

- Reuse ACT-008 direct movement, ACT-202 posture/lean, ACT-161 equipped attack,
  ACT-164 active slot, ACT-183 magazine reload and ACT-184 tactical throw.
  ACT-215 owns preparation loadout; ACT-189 owns squad movement directives.
  ACT-303 owns eligible impact/explosive breach; ACT-341 owns contextual
  restraint, report, evidence and door operations; ACT-409 emits flashlight
  illumination. Exact weapons, throws, ammunition and door tools are parameters.
- ACT-697 separately changes persistent personnel and assignment; ACT-698
  requests temporary stress treatment. ACT-699 requests state-qualified contact
  compliance/reposition, not a guaranteed arrest. ACT-700 selects a live tactical
  camera view; ACT-701 toggles fitted night vision without emitting light.
  ACT-702 requests self-bandaging with RON-012's indirect/bug qualification.
- Claims: RON-002–RON-012, RON-014, RON-016.

### System Behaviour Genes

- Reuse SYS-051 autonomous engagement, SYS-297 committed local pathing and
  SYS-292 perception/hostile commitment, independently from directly controlled
  combat SYS-215. SYS-208 owns projectile/material cover, hit and armor effects;
  SYS-318 owns equipment-dependent capabilities; SYS-538 owns consumable
  grenade effects. SYS-773 settles mission conduct rather than custody alone.
- SYS-1425 owns uncertain contact response; SYS-1426 registers custody/report/
  evidence; SYS-1427 performs contextual equipped squad procedures; SYS-1428
  carries mission stress into treatment/resignation risk; SYS-1429 distinguishes
  intended bleed control from restoring lost health; SYS-1430 returns retained
  result/personnel to HQ; SYS-1431 changes local door access.
- Resolution order: equipment/assignment before deployment; local perception,
  compliance or combat and squad orders in ongoing simulation; eligible physical
  custody/report/evidence before corresponding register updates; end permission
  before categorized report; result and surviving personnel/stress before HQ
  assignment/treatment and successor availability. Exact native scheduler and
  coefficients are not established. Claims: RON-002–RON-015.

### Constraint Genes

- Reuse CON-175 spatial contact/traversal, CON-262 finite carried supply,
  CON-285 active weapon compatibility and CON-287 ceramic durability. Steel
  wear is not inferred from ceramic. CON-769 separates sidearm-compatible
  shield use from free independent two-handed equipment, qualified RON-016.
- CON-785 gates four assigned AI positions by retained life/availability;
  CON-786 shares armor-dependent preparation capacity; CON-787 gates physical
  restraint by eligible reachable state and intact access; CON-788 gates body
  passage by aperture/lock/wedge; CON-789 qualifies fitted headwear protection.
- Scarce resources: available personnel, health, ammunition, utility slots,
  ceramic protection, information and safe entry positions. No weapon-name
  genes, universal exact plate endurance or automatic spare recruitment.
- Claims: RON-002–RON-010, RON-012, RON-014, RON-016.

### Information Genes

- Reuse INF-073 active weapon/supply, INF-115 local scene, INF-119 immediate
  personal condition, INF-388 required objective checklist and INF-299 categorized
  terminal evaluation. Qualitative health is not an exact exposed numeric pool.
- INF-492 owns partial briefing, INF-493 limited live tactical camera views,
  INF-494 current officer/subgroup/order/health and retained personnel readiness.
  A locked trait is information, not an operational trait effect. Claims:
  RON-002–RON-005, RON-010–RON-014.

### Objective Genes

- OBJ-289 resolves population-wide order/civilian and named-person requirements,
  enabled ending, categorized proof/conduct and retained HQ personnel return.
  This differs from OBJ-154's declared finite designated-target set without
  narrowing that earlier gene to assassination methods.
- Required flags, optional veteran proof, living custody quality and final grade
  are not identical. R1 verifies a successful return, not every failed-flag
  successor threshold. Early exfil, player death and unfinished deployment are
  negative outcomes, not a second positive terminal. Claims: RON-013–RON-015.

### Time Genes

- Reuse TIM-003 for live unpaused movement, hostility, response, orders and
  exposure. Pause and HQ preparation do not create turns. Therapy recovery
  coefficients are unmeasured and unlocked traits are outside the packet.
- Claims: RON-005/006/012/015.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh ordinary Commander HQ exposes assigned officers and reserves | Replace one available assigned member and configure loadout | Active four-slot identity/equipment selection changes before deployment | retained personnel preparation, not tactical starting panels | RON-002/003 |
| A fixed armor-dependent munitions allowance is allocated | Add one compatible magazine while removing another allocation | Shared preparation capacity remains bounded | finite allowance, not free extra supply | RON-003 |
| First gas-station deployment is live | Walk/lean, aim, fire, switch or reload a compatible weapon | Local embodied and ammunition state changes while other actors progress | live direct control versus autonomous response | RON-004/015 |
| A closed addressed door and equipped squad are reachable | Select subgroup and stack or eligible pick/open/breach procedure | Local order and door state change subject to geometry/tool access; bugs can prevent completion | contextual procedure, not guaranteed queue | RON-005/009 |
| A contact remains active or has apparently surrendered | Issue compliance or compatible less-lethal intervention | Response may surrender, resist, flee or deceive; visible surrender alone is not permanent incapacity | conditional contact state | RON-006 |
| A reachable eligible contact is kneeling with usable restraint access | Restrain and report | Physical custody and registered report are separate from defeat | living custody and proof | RON-007/008 |
| A dropped weapon or named-person proof is visible but not registered | Secure/report through an eligible interaction | Corresponding proof flag or evaluation credit changes | seeing is not recording; proof is not combat loot | RON-007/013 |
| A door is closed/locked or wedged | Inspect through Mirror Gun, then attempt ordinary body passage | Camera knowledge does not itself open the aperture; compatible unlocking/removal/breach is distinct | sensing versus traversal permission | RON-009/010/011 |
| Dark room and compatible headwear/weapon attachment are selected | Toggle flashlight or NVGs, or inspect a selected live camera | Emitted light, filtered own view and mediated view remain different limited observations | device-sensitive information | RON-010/011 |
| Controlled officer is bleeding | Request self-bandaging | Intended outcome stops bleed without restoring lost health; launch bugs may prevent ordinary return to weapon use | qualified treatment, not full healing | RON-012 |
| R1 shows final restraint/report and main objective resolution | Accept exposed mission-end permission and inspect report | Main flags, optional proof and conduct categories appear separately; animating total is not a measured final grade | evaluated end, not guaranteed perfection | RON-013 |
| First evaluated deployment returns to HQ with survivors | Inspect roster and send an eligible member to therapy or replace them | Anxious/Content survives the return; available assignment can differ despite no officer death; traits remain locked | retained personnel consequence | RON-002/014 |
| R1's accepted first result has returned to HQ | Inspect available successor but do not deploy | 23 Megabytes a Second is exposed; current packet ends before restored control there | bounded positive terminal | RON-013/014 |
| Unfinished live mission still permits spawn-point withdrawal | Return to initial exfil rather than quit directly | Deployment ends without positive completion; documented stress reduction has no admitted exact value | distinct negative withdrawal | RON-015 |

## Strategic and experiential structure

- Local decision: inspect an uncertain entry/contact, select safe coverage and
  admissible force, then complete restraint/report rather than equating every
  encounter with lethal removal.
- Medium-term planning: armor and utility allocation trade protection, camera,
  entry tools and consumables; ordering a subset changes who is exposed. A
  successful firefight still leaves civilian, named-person and evidence work.
- Long-term structure: this first deployment reaches retained stress, roster
  availability and treatment, not later trait utility or a campaign inventory.
- Common heuristics: inspect before crossing, cover another officer's custody
  operation, avoid needless lethal force and revisit unregistered proof. These
  are proposed strategies, not universal guarantees of a grade or AI response.
- Failure attribution: objective flags, current order/health and terminal
  categories separate omission, hostile exposure and officer consequences;
  opaque contact responses and launch bugs remain documented trust limits.
- Player-trust factors: apparent surrender must not be misrepresented as
  guaranteed safety; end permission must not imply complete optional proof;
  survival must not imply healthy retained personnel. Claims: RON-002–RON-015;
  heuristics are Hypothesis / Limited / Medium, not an externally novel claim.

## Replay and variation

- Same authored gas station, but loadout, personnel, route, orders, contacts,
  compliance, force, proof, health and officer stress can differ.
- S1 reports variable contact positions; exact seed/distribution and parity with
  every launch attempt are not verified. No procedural map generation is claimed.
- Viable alternatives include camera-assisted entry, different compatible
  weapons/protection/tools and differentiated subgroup use. Less-lethal does
  not mean universally nonfatal or guaranteed compliance.
- Replay can improve conduct and living custody, but replay and later unlocked
  traits are not admitted as additional playable packets. Claims: RON-003–015.

## Adjacent systems and history

- Full release adds Commander personnel consequences and revised SWAT/contact
  behavior to earlier product history; earlier rules are qualified corroboration,
  not the scoped target. Current console/DLC behavior is not launch parity.
- Continuous gun-coverage compliance in Battlefield Hardline is not this
  uncertain morale/fake-surrender state. PAYDAY's finite civilian ties do not
  describe this police-restraint eligibility. Neither game's old signature or
  definition changes.
- The deterministically selected HITMAN neighbour retains direct local action,
  finite compatible weapons, cover and evaluated conduct, but its social-role
  access and closed designated-target exit do not describe police proof or
  persistent officer stress. Claims: RON-001–RON-016; corpus computation below.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-008, ACT-161, ACT-164, ACT-183, ACT-184, ACT-189, ACT-202, ACT-215, ACT-303, ACT-341, ACT-409, ACT-697, ACT-698, ACT-699, ACT-700, ACT-701, ACT-702 | weapon, officer, input, tool and directive |
| System Behaviour | SYS-051, SYS-208, SYS-215, SYS-292, SYS-297, SYS-318, SYS-538, SYS-773, SYS-1425, SYS-1426, SYS-1427, SYS-1428, SYS-1429, SYS-1430, SYS-1431 | material, response, geometry, conduct and stress |
| Constraint | CON-175, CON-262, CON-285, CON-287, CON-769, CON-785, CON-786, CON-787, CON-788, CON-789 | finite allowance, available roster, aperture and equipment |
| Information | INF-073, INF-115, INF-119, INF-299, INF-388, INF-492, INF-493, INF-494 | device viewpoint, partial briefing and current labels |
| Objective | OBJ-289 | required conditions, evaluation and retained personnel |
| Time | TIM-003 | ordinary unpaused real-time mission |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `507` (`GAME-0001`–`GAME-0507`).
- Exact genome matches: none.
- Tied near matches: `GAME-0248` — HITMAN World of Assassination (`16 / 70 = 0.228571`).
- Supported combination subsets: none.
- Scan date: 2026-10-06.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0248` HITMAN World of Assassination | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-202`, `ACT-341`, `SYS-208`, `SYS-215`, `SYS-773`, `CON-262`, `CON-285`, `INF-073`, `INF-115`, `INF-119`, `INF-299`, `TIM-003` | Paris uses acquired roles, exceptional observers and a fixed designated-target exit. This police packet uses variable compliance, equipped subgroups, custody/evidence registers, armor-dependent prep and retained officer stress; it does not inherit disguise access or Instinct. | Tied near: `16 / 70 = 0.228571` |

- New genes: ACT-697–702, SYS-1425–1431, CON-785–789, INF-492–494, OBJ-289.
- Classification result: New gene.
- Evidence and reasoning: operational boundaries separate requests, resolution,
  eligibility, information and positive terminal. Limited source qualifications
  survive admission rather than being promoted by signature count or artwork.

### Preserved research notes

- New genes: ACT-697–702, SYS-1425–1431, CON-785–789, INF-492–494, OBJ-289.
- Classification result: New gene.
- Evidence and reasoning: operational boundaries separate requests, resolution,
  eligibility, information and positive terminal. Limited source qualifications
  survive admission rather than being promoted by signature count or artwork.

## Taxonomy impact

- Registry changes: the 22 additions above; no older definition or signature edit.
- Taxonomy-change record: [TAXONOMY_CHANGE_245](../../../research/taxonomy-changes/TAXONOMY_CHANGE_245.md).
- Candidate terms affected: no brand-dependent term promoted as a mechanism.

## Negative results

- No separate negative-result record. Rejected transfers are boundary checks,
  not claims that the predecessor lacks a mechanic or that external novelty
  has been proven.

## Delta summary

## New facts

- [Observation | Corroborated | High] The first deployment reaches an evaluated
  HQ roster terminal with surviving but differently stressed officers and
  locked traits; RON-013/014.
- [Observation | Limited | Medium] Treatment and protective gear retain
  indirect original-launch qualifications; RON-010/012/016.

## New genes

- [Observation | Corroborated | Medium] Twenty-two bounded additions, including
  explicitly Limited/Medium treatment, night-vision and headwear boundaries.
  Their individual claims and definitions own the narrower evidence status.

## New combinations

- [Observation | Direct | High] No new combinations; deterministic proper-subset
  scan found no supported existing combination in the complete admitted genome.

## Taxonomy changes

- [Observation | Corroborated | Medium] TAXONOMY_CHANGE_245 records new
  boundaries and counterexamples without mutating accepted earlier signatures.

## New questions

- [Hypothesis | Limited | Medium] Native original-1.0 treatment, shield rejection,
  headwear exposure, stress coefficients and failed-flag successor thresholds
  could strengthen or overturn qualified claims. A dated binary/input trace
  and controlled transition test, not a current console guide, is the test.

## Next recommended game

- [Hypothesis | Limited | Medium] Original Xbox MechAssault, GAME-0509.
- Optimisation criterion: approved mixed-era/platform order, not a promise of
  mechanistic novelty or a selected neighbour before its complete analysis.
- Expected information gain: vehicle-mounted combat and bounded mission
  resources, to establish from original rules rather than police assumptions.
- Backlog impact: 18-game selection 039 is unchanged. Do not begin the next
  unit before this game's complete gates, sole local commit and stop window.

## Why this game

- [Hypothesis | Limited | Medium] The selected full-release police loop adds
  custody/report/personnel counterexamples to embodied combat. Theme alone
  cannot establish a taxonomy distinction or external novelty.
