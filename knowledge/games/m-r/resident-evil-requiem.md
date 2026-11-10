---
game_id: GAME-0512
slug: resident-evil-requiem
game_title: Resident Evil Requiem
analysis_status: reviewed
reviewed: 2026-10-06
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-049
    - ACT-089
    - ACT-131
    - ACT-164
    - ACT-199
    - ACT-202
    - ACT-341
    - ACT-673
    - ACT-706
    - ACT-707
  system:
    - SYS-057
    - SYS-369
    - SYS-578
    - SYS-605
    - SYS-1449
  constraint:
    - CON-210
    - CON-282
    - CON-296
    - CON-621
    - CON-791
  information:
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-213
  objective:
    - OBJ-026
  time:
    - TIM-003
    - TIM-007
---

# Game: Resident Evil Requiem

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Parameters refine admitted transitions, not new gene identities.

## Analysis scope

- Version / ruleset: Released English PS5 base Resident Evil Requiem, first Grace Rhodes Hill
  Chronic Care Center episode, Standard (Modern), reconstructed from the
  release-period recording R1 published 2026-02-27. P1 lists the PS5 full
  product release as 2026-02-27, separately from its trial and Deluxe edition.
  R1’s difficulty-selection frame at 40 seconds explicitly selects Standard
  (Modern); its PS5 Pro attribution is not independent binary or hardware
  verification. Exact patch, region, build, checksum and 2026 current-patch
  parity remain unverified. Earlier demo/previews are not evidence for this
  packet.
- Structured analysis target: PLAT-PLAYSTATION-5, released English first Grace care-centre episode;
  knowledge/platforms/games.json is authoritative. No release-platform audit is
  implied.
- Primary decision loop: Navigate the care-centre floor, inspect reachable supplies and notes, acquire
  the Cherub Key and lighter, and evade the Girl using current concealment,
  fixed-light refuges and finite bottle distractions. Move the authored trolley
  while accounting for noise and both pre-move coin and post-move tool/herb
  access; recover the screwdriver, pass the newly opened route, open the fuse
  panel, take the Fuse and reach the locked exit to install it. Inventory,
  optional healing/discard, current route information, saving and failed-attempt
  recovery remain causal, not a successful-only walkthrough.
- Entry and exit: Entry is first ordinary Grace control in Room 203 after awakening and freeing
  her restraints, before collecting the local key, lighter or supplies. Exit is
  the first ordinary Leon Care Center control after Grace’s Fuse installation
  and intervening cutscenes. The complete first Grace episode is the accepted
  packet, not all Care Center, a whole-product campaign or an arbitrarily
  truncated surviving route. All reachable optional first-section coin, bottles,
  herb, injector, files and typewriter choices belong to the scope.
- Included: Direct walking/running and contextual climbing; retained crouch and low
  concealment; reachable light switches and handheld lighter selection; key/tool
  pickups and matched door/panel interactions; ordinary eight-slot carried
  supply capacity, typed bottle stacks, eligible pickup, selection, healing and
  irreversible discard; optional Antique Coin before moving the trolley,
  subsequent screwdriver and herb access; held trolley movement/noise and
  pursuer response; sight/sound-based pursuit and bottle distraction; powered
  fixed light forcing the Girl to retreat, later loss of local protection,
  dark-route refusal before lighter availability; authored door break opening a
  later passage, screwdriver-gated panel, Fuse retrieval and forced pursuit to
  exit; current health/item/map/clue disclosure; Standard (Modern) typewriter
  saving without Ink Ribbon expenditure, retained save selection and authored
  retry. Quantitative impact, detection, healing and retry-state coefficients
  remain unverified.
- Excluded: Earlier Wrenwood hotel and Leon city combat; subsequent Leon weapons/hatchet
  and later Grace firearm/knife, Blood Collector crafting, quartz-wing
  progression, coin spending/upgrades, steroid capacity, storage boxes, later
  basement portable UV/boss and ARK; Classic/Insanity ribbon expense and changed
  pickups, New Game Plus, bonuses, DLC/trial/demo, whole-campaign completion and
  current-patch equivalence. No available early recipe is invented merely
  because later product crafting exists; one reachable herb does not prove a
  two-herb recipe is legal here. No exact initial health, bottle damage,
  detection radius, light damage, duration, seed or controlled save-file
  coverage is claimed.
- Potential scoped modules: Later Grace collection/crafting/quartz and basement escape, or a complete Leon
  combat chapter, would require independent dated entry/exit and full reachable
  alternatives. No module ID or gene count is promised; lower-evidence refusal,
  full-capacity/discard and save/retry branches retain documentary
  qualifications.
- Direct-play status: No own PS5 executable, hardware, controller, timed reaction, damage
  measurement or save/reload was tested. R1 MKIceAndFire is a PS5 Pro-attributed
  full-game recording published 2026-02-27; metadata length 31920 seconds,
  actual player duration 31920.141. Paused frames actually inspected:
  40/900/1500/2100/2280/2400/2520/2580/2600/2620/2640/2650/2690/2700/2730/2760/2790/2810/2830/2850/2860/2880/2900/2910/2930/2940/2970/2980/3000/3010/3020/3030/3040/3050/3060/3070/3090/3100/3110/3120/3130/3140/3160/3180/3210/3240/3250/3300/3360/3480/3600/3720/3840.
  The first care-centre packet is approximately 2520–3300; preceding unrelated
  gameplay, the black 2400 frame and later Leon/Grace content are not evidence
  of an admitted early weapon. R1 2620 shows the bottle’s description and
  Power/Radius bars, not readable numerical damage; 2930 exposes lighter/bottle
  selection, 3000 the held cart prompt, 3040 Screwdriver receipt, and 3110 the
  incompatible injector selection at the fuse panel. Overlays sometimes obscure
  detail. Current map, save/discard, direct bottle impacts and failed branches
  are qualified documentary reconstructions, not controlled frame transitions.
  Source identity, duration, seek, no-ad, muted and paused states were checked.
  All media remained background/headless/muted without fullscreen, focus
  stealing, user-window/tab or system-sound changes; no audio analysis or
  remote-media download occurred. The linked official Capcom manual returned 404
  in HTTP and hidden-browser checks, so no manual contents are claimed read.
  Working captures/prompts remain outside Git.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| RQ-001 | The complete released PS5 first Grace care-centre episode, Standard (Modern), is distinct from demos, later chapters and an independently verified installed build. | Observation | Corroborated | High | P1; R1 40 and care-centre sequence; S1/S2 |
| RQ-002 | Cherub Key gives Room 201 access; its lighter enables the initially refused dark route, but does not protect like powered fixed light. | Observation | Limited | Medium | R1 2690/2700/2730; S1/S2/S3; dark refusal not replayed |
| RQ-003 | The Girl pursues current stimuli; powered fixed care-room light makes her retreat toward darkness, rather than merely exposing her. | Observation | Corroborated | High | R1 2790/2910/2930; S2/S6 |
| RQ-004 | Held trolley movement changes reachable coin/tool/herb opportunities and attracts the pursuer; concealment and the hostile-opened passage change escape access. | Observation | Corroborated | High | R1 2970/3000/3040; S1/S2/S5/S6 |
| RQ-005 | Finite thrown bottles break and divert attention; Power/Radius bars are not measured numerical damage or proof of a guaranteed direct-hit stagger. | Observation | Limited | Medium | R1 2620/2930; S1/S2/S7; no controlled impact |
| RQ-006 | Typed carried capacity, optional supplies, healing and irreversible discard belong to the first episode; no later recipe or coin economy is imported. | Observation | Limited | Medium | R1 3110 eight supply cells and injector description; S5/S9/S10/S11 |
| RQ-007 | A screwdriver opens the fuse panel; retrieval starts renewed pursuit and the installed Fuse closes this Grace episode. Room lighting can fail before retrieval. | Observation | Corroborated | High | R1 3040/3100/3110/3120/3140/3160/3300; S1/S2/S3/S6 |
| RQ-008 | Current threat, personal condition, carried items, local clues and discovered-route information do not reveal a guaranteed future patrol or every hidden item. | Observation | Corroborated | High | R1 item/quickslot/book/panel frames; S1/S2; map is documentary |
| RQ-009 | Modern saving uses Room 201's typewriter without ribbon expenditure; retained history and failed-checkpoint continuation are documentary, not own reload tests. | Observation | Limited | Medium | S3/S8/S11; no controlled save/reload |
| RQ-010 | Four additions and twenty-five unchanged transfers describe this complete packet, not an early firearm or darkness-damage loop. | Observation | Direct | High | TAXONOMY_CHANGE_249; registry boundary review |
| RQ-011 | Every lower-ID complete signature and every verified proper combination subset is recomputed. | Observation | Direct | High | Corpus comparison; repository validator |

## Basic data

- Release / origin: Capcom's full Resident Evil Requiem; official P1 PS5
  release date 2026-02-27. Recorded patch and region are not independently known.
- Structured target: PLAT-PLAYSTATION-5; no all-platform release audit.
- Families: FAM-010 concurrent autonomous pursuit, FAM-013 carried tools and
  protected fixture dependencies, FAM-017 ordered key/cart/tool/fuse admission.
  These reused boundaries are not a one-game horror-family proposal.
- P1: [Official PlayStation product](https://www.playstation.com/en-us/games/resident-evil-requiem/),
  read full-product identity, release date, offline single-player PS5 and
  switchable first/third-person presentation. Later product mechanics and
  trial/Deluxe offers are not admission into this episode.
- P2 access limit: [Steam technical support](https://help.steampowered.com/en/wizard/HelpWithGameTechnicalIssue?appid=3764200)
  links the official [Capcom manual](https://manual.capcom.com/requiem/).
  The target returned 404 both through HTTP inspection and a hidden browser;
  no manual rules are represented as read. PC support does not prove PS5 parity.
- R1: [MKIceAndFire full-game recording](https://www.youtube.com/watch?v=H4j5H_g-qeU),
  published 2026-02-27, PS5 Pro attribution, metadata 31920 seconds and actual
  duration 31920.141. Sampling and limits are enumerated above. First-person
  and third-person are presentation choices; no new control-identity gene.
- S1: [PowerPyx Care Center walkthrough](https://www.powerpyx.com/resident-evil-requiem-care-center-100-walkthrough/),
  Gage, 2026-02-26, first Grace section read. Pre-release press-guide dating
  remains explicit; R1 independently anchors the released sequence.
- S2: [Prima first Grace care-centre walkthrough](https://primagames.com/tips/resident-evil-requiem-complete-walkthrough-grace-ashcroft-care-center),
  Enzo Zalamea, updated 2026-02-27, first-episode body read. Its informal
  Shadow Ghost name is not treated as a separate enemy from the Girl.
- S3: [Evil Resource Room 201](https://www.evilresource.com/resident-evil-requiem/maps/rhodes-hill-care-center/care-center-2f/room-201),
  relevant Standard (Modern) entries read; other difficulty pickups excluded.
- S4: [Evil Resource Prep Room](https://www.evilresource.com/resident-evil-requiem/maps/rhodes-hill-care-center/care-center-2f/prep-room),
  conditional pre-lighter bottle and first Girl appearance entries read.
- S5: [Evil Resource Nurses Station](https://www.evilresource.com/resident-evil-requiem/maps/rhodes-hill-care-center/care-center-2f/nurses-station),
  Modern coin-before-cart, herb/tool-after-cart and injector entries read.
- S6: [Evil Resource the Girl](https://www.evilresource.com/resident-evil-requiem/enemies/the-girl),
  UV retreat and first-episode events read; later bosses and portable UV excluded.
- S7: [Evil Resource Empty Bottle](https://www.evilresource.com/resident-evil-requiem/items/empty-bottle),
  description and first-section Modern locations read, not all product drops.
- S8: [Evil Resource Grace save point](https://www.evilresource.com/resident-evil-requiem/miscellaneous-objects/save-point-grace),
  mode-dependent saving description and Room 201 Modern entry read.
- S9: [Evil Resource Med Injector](https://www.evilresource.com/resident-evil-requiem/items/med-injector)
  and [Green Herb](https://www.evilresource.com/resident-evil-requiem/items/green-herb),
  item descriptions and first Nurse Station Modern entries read. Later blood
  recipes, shop values and other chapter supplies are excluded.
- S10: [GameFAQs combat mechanics](https://gamefaqs.gamespot.com/ps5/473093-resident-evil-requiem/faqs/82414/combat-mechanics),
  JellifishPirate, version 1.4 dated 2026-03-29, Grace capacity/discard body
  read. Later documentation is qualified, not exact launch-build verification.
- S11: [GameFAQs item guide](https://gamefaqs.gamespot.com/ps5/473093-resident-evil-requiem/faqs/82432/items),
  attributed written item/Modern-versus-Classic saving corroboration, not own
  reload. The separately attempted care-centre chapter returned an access
  error and is not represented as read. No Reddit coefficient is admitted.
- Claim IDs: RQ-001–RQ-011. Later community documentation is corroboration;
  exact unobserved transitions retain Limited/Medium qualifications.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: ACT-008/049/089/131/164/199/202/341/673.
- Added genes: ACT-706 held authored-path trolley relocation; ACT-707 finite
  breakable aimed diversion without guaranteeing harmlessness or universal stun.
- Parameters: local navigation and contextual climb, light switch, selected
  lighter/bottle, addressed key/tool, supply stack, crouch, compatible fixture,
  consumed healing, eligible discard, cart path and finite throw.
- The lighter's visible selection is supported; no separately controlled
  fuel/refill or universal personal-light toggle is inferred. Ordinary climbing
  is not an aimed whip/grapnel attachment or manually selected airborne release.
- Claim IDs: RQ-002–RQ-007/010.

### System Behaviour Genes

- Existing gene IDs: SYS-057/369/578/605; added SYS-1449 protective fixed light.
- Resolution order: key/lighter access admits the initially dark route. Local
  pursuit responds to eligible sight/noise; fixed light changes the threat's
  retreat, whereas the pocket flame changes visibility. Moving the trolley
  changes reachable supplies and draws the Girl. Screwdriver acquisition and
  the authored hostile door break allow return toward Room 201. Lighting fails
  on the return before fuse removal, so loss is not falsely attributed solely
  to taking the fuse. Compatible tool opens the panel; taking Fuse triggers
  renewed pursuit. Exit installation starts the concluding scene and later
  ordinary Leon control, not a claimed additional player-pressed final button.
- Parameters: current threat and local stimuli, powered fixture, item identity,
  local route flags, injuries/healing, current save and restored checkpoint.
- Claim IDs: RQ-002–RQ-007/009/010.

### Constraint Genes

- Existing gene IDs: CON-210/282/296/621; added CON-791 local dark-route admission.
- Scarce resources: compatible supply slots and finite bottles/healing. Matching
  key and screwdriver fixture access differ from spare supply selection; a
  visible injector is not an opening tool. Eight ordinary supply cells do not
  imply that every key item occupies one of those cells. No later inventory
  expansion, item-box transfer or guaranteed full-health healing refusal is
  inferred. Modern saves do not consume the Classic/Insanity ribbon supply.
- Claim IDs: RQ-002/006/007/009/010.

### Information Genes

- Existing gene IDs: INF-115/119/125/128/213; no additions.
- Current local sight/sound, health, selected item/count, discovered navigation,
  contextual panels and read files are disclosed. Bottle Power/Radius bars and
  Med Injector full-restoration description are actually readable; no numerical
  bars, hidden future route or every secret are derived from them. Map access
  is documentary, not a sampled complete map or proven exact PS5 layout.
- Claim IDs: RQ-005/006/008/010.

### Objective Genes

- Existing gene ID: OBJ-026. No addition or arbitrary collectible quota.
- Success: reach the locked exit with Fuse and complete its required operation,
  through concluding scenes to first ordinary successor control. Tool collection
  or merely standing at the gate is insufficient. Coin pickup and every supply
  are optional alternatives, not compulsory requirements for a successful exit.
- Failure: ordinary fatal pursuit ends the attempt and offers checkpoint
  continuation; the scripted end-scene attack belongs to successful episode
  transition and is not evidence of a lost attempt or forced damage coefficient.
- Claim IDs: RQ-004/006/007/009/010.

### Time Genes

- Existing gene IDs: TIM-003/007. Real-time pursuit and optional retained-history
  resumption are distinct. Menu pause is a parameter: a continuing speedrun
  clock alone would not prove a continuing world simulation. No exact input
  interval, new countdown, time-reversal animation or self-imposed timer.
- Claim IDs: RQ-003–RQ-009/010.

## Reproducible transitions

These are source-grounded operational predictions, not own native executions.
Quantitative and documentary-only branches retain the ledger qualifications.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First ordinary Room 203 control | Explore reachable first-section fixtures | Local key, bottles and files can be reached before later weapons | Entry precedes item procurement | RQ-001/002/006 |
| Matching locked door and Cherub Key | Use the key | Room 201 access becomes available | Identity-dependent fixture admission | RQ-002 |
| Initial designated dark route, no lighter | Attempt that route | Documentary refusal persists until lighter availability | Connected geometry is not sufficient, but darkness is not player damage | RQ-002 |
| Read Room 202 light clue and encounter Girl | Retreat to powered room light | Eligible pursuer withdraws into darkness | Fixed refuge differs from handheld visibility | RQ-003 |
| Lighter selected in dark corridor | Continue near the Girl | Visibility alone supplies no fixed-light protection | Portable flame is not a UV weapon | RQ-002/003 |
| Unmoved trolley and reachable top locker | Climb for optional coin before moving | Carried coin can be retained without spending it here | Reachable optional branch belongs to scope | RQ-004/006 |
| Trolley engaged, held contextual input | Move along its permitted path | Higher tool and obstructed herb access change; noise draws attention | Held movement is not a one-cell push | RQ-004 |
| Girl approaching Nurse Station | Crouch under eligible obstruction or retreat | Current line of access and concealment change | Posture is not guaranteed invisibility | RQ-003/004 |
| Bottle carried and reachable throw point | Aim and throw | Unit is spent; breakage can draw local investigation | Diversion is finite, contact outcome not guaranteed stun | RQ-005 |
| Reached supply and compatible stack/free slot | Take it, or decline/relieve capacity | Accepted carried stock remains capacity-bounded | No unlimited bottle counter | RQ-006 |
| Injury and compatible healing stock | Use eligible supply | Item is consumed and current health restored by its disclosed type | No delayed painkiller rule or invented coefficient | RQ-006 |
| Eligible carried supply | Confirm discard | Supply is irreversibly removed rather than placed for recovery | Capacity relief can cost stock | RQ-006 |
| Screwdriver acquired and later passage approached | Continue the authored sequence | Girl opens the blocked door and new route becomes traversable | Hostile-authored opening is not a commanded player breach | RQ-004/007 |
| Return toward Room 201 | Approach after the sequence advances | Local lights can fail before Fuse is removed | Do not fabricate removal-causes-all-power-loss order | RQ-007 |
| Closed fuse panel and carried injector only selected | Try incompatible item | Opening prerequisite is not met | Visible inventory choice is not compatibility | RQ-007/008 |
| Closed fuse panel and Screwdriver | Use the correct tool and take Fuse | Panel opens, item is acquired and renewed pursuit starts | Tool gate and forced pursuit are separate from heal | RQ-007 |
| Reached locked exit without Fuse | Attempt exit operation | Required installation is unavailable | Arrival alone is insufficient | RQ-007 |
| Fuse carried and exit reached | Install it | Episode concludes through scenes to ordinary Leon control | Whole Grace packet has a reproducible terminal | RQ-001/007 |
| Eligible Room 201 typewriter, Standard Modern | Save and later select retained history | Save does not spend ribbon; different subsequent input is possible | Documentary history, not own reload | RQ-009 |
| Fatal ordinary pursuit | Select checkpoint continuation | Authored attempt state is restored | Failed attempt differs from successful terminal scene | RQ-009 |

## Strategic and experiential structure

- Local decision: balance immediate route, concealment, fixed refuge and finite
  diversion; a harmless-looking portable flame is not defensive immunity.
- Medium-term planning: inspect both trolley positions, reserve usable supplies,
  match tool to fixture and account for renewed pursuit after taking Fuse.
- Long-term structure: subsequent chapters and coin spending lie outside this
  episode; no whole-product strategy or early firearm economy is invented.
- Common heuristics: inspect the pre-move locker, use current threat cues,
  approach the correct panel prepared, and preserve a deliberate save branch.
- Failure attribution: dark-route refusal, wrong item, full supply capacity,
  exposed movement and fatal pursuit have distinct causes.
- Player trust: current descriptions and authored light clue explain useful
  choices; they do not promise exact damage or an omniscient enemy path.
- Claim IDs: RQ-002–RQ-009.

## Replay and variation

- Current position, threat stimulation, optional pickups, bottle expenditure,
  healing/discard and saving choices change the local route and retained stock.
- No seed, native adaptive-difficulty coefficient or random spawn distribution
  is reconstructed from paused frames. Authored progression is not asserted
  to make every pursuit trajectory deterministic.
- Multiple evasion and supply choices remain admitted. Neither collecting every
  supply nor spending a bottle is a fabricated mandatory victory condition.
- Claim IDs: RQ-003–RQ-009.

## Adjacent systems and history

- Existing Resident Evil 2/4, Alien Isolation and other survival packets can
  share inventory or pursuit genes without inheriting their complete genomes.
- Modern is distinct from Classic/Insanity. Later weapons, portable UV and
  blood crafting cannot be inserted because they occur in the same product.
- Claim IDs: RQ-001/003/006/009–RQ-011.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-008, ACT-049, ACT-089, ACT-131, ACT-164, ACT-199, ACT-202, ACT-341, ACT-673, ACT-706, ACT-707 | No additional candidate IDs; scoped parameters above |
| System Behaviour | SYS-057, SYS-369, SYS-578, SYS-605, SYS-1449 | No additional candidate IDs; scoped parameters above |
| Constraint | CON-210, CON-282, CON-296, CON-621, CON-791 | No additional candidate IDs; scoped parameters above |
| Information | INF-115, INF-119, INF-125, INF-128, INF-213 | No additional candidate IDs; scoped parameters above |
| Objective | OBJ-026 | No additional candidate IDs; scoped parameters above |
| Time | TIM-003, TIM-007 | No additional candidate IDs; scoped parameters above |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `511` (`GAME-0001`–`GAME-0511`).
- Exact genome matches: none.
- Tied near matches: `GAME-0348` — Resident Evil: Director’s Cut (`16 / 34 = 0.470588`).
- Supported combination subsets: none.
- Scan date: 2026-10-06.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| GAME-0348 — Resident Evil: Director’s Cut | ACT-008, ACT-199, ACT-341, CON-210, CON-282, CON-296, CON-621, INF-115, INF-125, INF-128, OBJ-026, SYS-057, SYS-369, SYS-578, TIM-003, TIM-007 | Both packets connect keyed local routes under live pursuit, finite carried capacity and retained fixture saves. Chris has a handgun, six slots, three Sword Key uses and a ribbon-paid reload terminal; Grace has fixed-light refuge, a held trolley, finite breakable diversion, an initially light-gated route and screwdriver/Fuse exit, with optional healing and Modern saving without ribbon expenditure. No franchise-wide equivalence or native PS5 reload is inferred. | 16 / 34 = 0.470588 |

### Preserved research notes

- New genes: ACT-706/707, SYS-1449 and CON-791.
- Classification result: New gene.
- Evidence and reasoning: complete signatures and proper verified subsets,
  not franchise affinity or copied screenshot motifs (RQ-010/011).

## Taxonomy impact

- Registry changes: four Active additions and twenty-five unchanged transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_249](../../../research/taxonomy-changes/TAXONOMY_CHANGE_249.md).
- No previous signature/definition, release audit or r000024 mapping changes.
- Claim IDs: RQ-010/011.

## Negative results

- No structured global negative result. Strictly inert diversion, one-cell
  pushing, darkness-damage survival, generic player door breach, delayed healing
  and later blood recipes do not transfer into this packet.
- Claim IDs: RQ-002–RQ-010.

## Delta summary

## New facts

- [Observation | Corroborated | High] Fixed protective light and portable
  visibility light have different causal roles (RQ-002/003).
- [Observation | Corroborated | High] Trolley relocation changes optional and
  required access while generating threat-relevant noise (RQ-004).
- [Observation | Limited | Medium] Bottle impact coefficients, discard,
  capacity and saved-history outcomes retain native-testing limits (RQ-005/006/009).

## New genes

- [Observation | Corroborated | High] Held fixture relocation and automatic
  protective-light retreat are separate command and resolver boundaries (RQ-003/004).
- [Observation | Limited | Medium] Breakable diversion and initial dark-route
  admission do not invent universal contact damage or darkness death (RQ-002/005).

## New combinations

- [Observation | Direct | High] Every verified proper subset is scanned;
  no motif-selected new combination is created (RQ-011).

## Taxonomy changes

- [Observation | Direct | High] TAXONOMY_CHANGE_249 accepts four additions
  without editing prior signatures or English boundaries (RQ-010).

## New questions

- [Hypothesis | Limited | Medium] A controlled pinned PS5 build could refine
  initial refusal, bottle contact, pause and restoration details without
  borrowing later chapter or mode rules.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0513 original Windows Thief: The Dark
  Project follows accepted local commitment and the stop window.
- Optimisation criterion: approved platform/era balance, final unit 18/18.
- Expected information gain: dated stealth scope, not a promised gene count.
- Backlog impact: stop after the complete final unit; no push/publication/deploy.

## Why this game

- [Hypothesis | Limited | Medium] The approved modern PS5 slot tests whether
  source-bounded survival dependencies can be represented without importing
  later combat or collapsing distinct illumination roles.
