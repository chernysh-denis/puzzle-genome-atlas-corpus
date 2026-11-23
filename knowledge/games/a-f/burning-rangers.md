---
game_id: GAME-0546
slug: burning-rangers
game_title: Burning Rangers
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-223
    - ACT-341
    - ACT-605
    - ACT-610
    - ACT-744
    - ACT-745
    - ACT-746
  system:
    - SYS-037
    - SYS-215
    - SYS-369
    - SYS-605
    - SYS-755
    - SYS-773
    - SYS-948
    - SYS-1582
    - SYS-1583
    - SYS-1584
    - SYS-1585
  constraint:
    - CON-183
  information:
    - INF-142
    - INF-527
  objective:
    - OBJ-303
  time:
    - TIM-003
---

# Game: Burning Rangers

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Crystals parameterise a shared protection and transport resource, not separate
health and rescue currencies. Danger percentage is not a terminal countdown.

## Analysis scope

- Version / ruleset: original English North American Sega Saturn retail
  release, 1998, ordinary Story Mode before the first campaign clear.
  Use the US booklet's control map: B fires/charges and operates switches,
  A/C supply thrust, X/Z request guidance or quick post-hit recovery,
  and Start pauses. No prototype, Japanese demo, fan tribute, patch or cheat
  is selected. Exact disc revision, binary and controller trace were not used.
- Entry: on a fresh Story Mode profile choose Tillis, complete Training Space
  and enter Mission 1, Fallen Memory, with its ordinary initial mission stock,
  original layout and no password or post-clear random generation. Start at
  the mission entrance before its first ordinary fire or survivor encounter.
  No exact initial crystal count or training-to-mission carryover is invented.
- Primary decision loop: navigate the power plant and request local guidance,
  read hazards and choose pulse or full laser. Collect usable crystals, decide
  when to approach a survivor and fund transport, operate route fixtures and
  move through the opened geometry. Inspect protection and danger before the
  next hazard; use defensive thrust, recovery or a checkpoint retry as needed.
- Positive exit: reach and defeat the first mission's final plant threat,
  Anemoth, accept Mission Result and use B to return to Mission Select with
  Mission 2, Silent Blue, available. Rescue performance is evaluated; neither
  an S rank nor every optional survivor is declared an ordinary clear gate.
  The unit does not end at the first transported survivor.
- Negative exit: compatible damage at zero crystals opens Retry if a continue
  remains; accepting it returns to the last authored continue point. Exhausted
  stock leads to Game Over. A high danger percentage raises live pressure;
  reaching 100 percent is not declared an instantaneous failure transition.
- Included: direct movement, obstacle auto-jump, manual directional thrust,
  camera control, ordinary and charged shots, hostile and breakable-object
  interaction, pulse-created pickups, shared crystal shielding and transport,
  continue awards and retry, route switches and ordered access, voiced
  guidance, telegraphed hazards, rising danger and the first boss/result.
- Excluded: the preceding training tasks themselves, later missions' swimming,
  zero gravity, child carrying and ship subgame; post-clear generated layouts,
  Password Missions, alternative-character cheats, complete survivor/mail
  collection, music playback, full-campaign endings and save-device management.
  Exact damage grace, emitted pickup cap, danger rate/floors, shot coefficients,
  initial-stock carryover and rank thresholds remain unmeasured.
- Potential modules: post-clear layout generation; survivor-mail persistence;
  Silent Blue's underwater traversal and mass evacuation.
- Direct-play status: no Saturn, disc image, executable, save or input trace
  was run. The original US booklet's control, HUD, shot, rescue, shield,
  retry and result spreads were visually inspected from preserved page scans.
  Sega's original gameplay page and independent written routes corroborate
  the model. No video or audio was played; transitions are reconstructions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| BR-001 | The selected product is the original 1998 Saturn release. A fresh story profile reaches Training Space and the first mission before later generation unlocks. | Observation | Corroborated | High | P1 pp. 14–17, P2, S1 |
| BR-002 | Direct movement combines manual thrust, airborne directional manoeuvres and grounded tumbles. Eligible obstacles also trigger automatic jumping; camera commands change the view. | Observation | Corroborated | High | P1 pp. 10–12, P2, S1 controls |
| BR-003 | Ordinary pulses home toward eligible flames and leave expiring crystals after extinguishing. Full charged lasers damage robots or the boss and clear stronger/nearby flames, destroying their collectible yield. | Confirmed | Corroborated | High | P1 pp. 11, 20–21, S2, S3 |
| BR-004 | Proximity transport needs at least five crystals and consumes up to ten. Paying ten also awards a continue. This spends the same held reserve that protects the ranger. | Confirmed | Corroborated | High | P1 p. 21, S1, S2 |
| BR-005 | Compatible hits scatter a positive reserve into briefly recoverable crystals. With none held, another compatible hit causes Retry or Game Over. X/Z immediately after shield damage speeds recovery without reducing the damage. Exact grace and scatter cap were not measured. | Observation | Corroborated | Medium | P1 pp. 22–23, S2, S3 |
| BR-006 | Time increases danger; extinguishing reduces it and volatile explosions increase it. Twenty-percent boundaries produce temporary explosion bursts. At 100 percent severe live pressure continues, not a documented instant timeout. | Confirmed | Corroborated | High | P1 pp. 19, 23, S2 |
| BR-007 | Fallen Memory uses authored route mechanisms, including restoring power, and ends at the plant boss Anemoth. Defeating it reaches the mission result. | Observation | Corroborated | High | P1 pp. 17, 24, S1 first-mission route, S2, S3 |
| BR-008 | HUD fields separate crystals, charge, room, applicable ID card, overall danger and its next-boundary bar. Chris supplies automatic or requested local voice directions; warning sounds/visuals cue impending hazards without a full map. | Observation | Corroborated | High | P1 pp. 10, 19, 22, P2, S2, S3 |
| BR-009 | Mission Result separates rescue, crystal, boss-time and danger categories plus S-to-D total rank. B returns to Mission Select; A/C advances. Exact reward tally and thresholds are not reconstructed from conflicting descriptions. | Confirmed | Corroborated | High | P1 pp. 24–25, S1, S3 |

## Basic data

- Sonic Team and Sega. Target: English North American Saturn retail rules.
- Families: real-time system pressure and inventory/fixture dependencies.
- Sources accessed 2026-11-19:
  - **P1** — [Original US Sega instruction booklet](https://archive.org/details/Burning_Rangers_1998_U),
    preserved publisher-authored scans. The public page-image archive and OCR
    were readable; the PDF endpoint returned a temporary server error.
    Printed pp. 10–12, 16–17, 19–25 were visually checked. OCR page ordering around
    the Mission 1/2 spread is not used to reverse the two mission descriptions.
  - **P2** — [Sega's original gameplay page](https://burningranger.sega.jp/con02.html),
    Japanese original text decoded as CP932: obstacle auto-jump, double-jump
    movement, voice navigation and active environmental fire. Shared design
    corroboration, not proof of exact North American timing coefficients.
  - **S1** — [NMetatron's original Saturn FAQ](https://gamefaqs.gamespot.com/saturn/196841-burning-rangers/faqs/5158),
    version 3.1, 11 February 1999. Controls, original-map markers, restored
    power and first boss Anemoth. Its later random survivor lists and personal
    records are not fixed first-clear requirements.
  - **S2** — [Lucas LaPlante's first-hand retrospective](https://www.hardcoregaming101.net/burning-rangers/),
    5 February 2016. Crystal loss, shot tradeoff, danger bursts and plant boss.
  - **S3** — [Jeremy's original Saturn review](https://infinityretro.com/burning-rangers-review/),
    5 June 2025. First-hand camera, warning, voice and crystal observations.
    Its simplified five-crystal price and whole-stage retry wording yield
    to P1's up-to-ten price and latest-continue-point rule.
  - **S4** — [GHZ's preserved gameplay notes](https://www.theghz.com/br/br/br.html),
    corroborating first-boss identity and broad resource tradeoff. The page
    marks itself outdated. Its Y-button recovery differs from P1's X/Z;
    its banked-crystal score detail is not adopted as an exact formula.
  - **S5** — [Bo Bayles' build comparison](https://www.bbayles.com/index/burning-rangers/br-prototype-roundup),
    independently distinguishes prototype countdowns, objects and maps from
    the Japanese final release. No prototype behaviour transfers to this unit.
- Claim IDs: BR-001–BR-009.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for embodied movement/jumps, `ACT-161` for aimed hostile
  attacks, `ACT-223` for warning-timed defensive responses, `ACT-341` for
  reachable route fixtures, `ACT-605` for quick post-hit recovery and
  `ACT-610` for camera reframing.
- Add `ACT-744` for pulse versus held laser, `ACT-745` for directional
  thrust manoeuvres and `ACT-746` for explicitly requesting local navigation.
- Claim IDs: BR-002, BR-003, BR-005, BR-007, BR-008.

### System Behaviour Genes

- Reuse `SYS-037` for contact pickup, `SYS-215` for live hostile combat,
  `SYS-369` for checkpoint retry, `SYS-605` for required route flags,
  `SYS-755` for breakable volatile objects and `SYS-773` for mission evaluation.
- Reuse `SYS-948` for positive-reserve scatter/recollection and zero-reserve
  lethal damage. Crystals are this ruleset's reserve parameter, not a reason
  to duplicate the ring-loss kernel. The crystal shield is that reserve,
  not a separate protective item taking precedence over conversion.
  Exact native grace, scatter cap and trajectories remain unmeasured;
  Sonic's numerical cap is not transferred.
- Add `SYS-1582` for shot-dependent crystal yield, `SYS-1583` for obstacle
  auto-jump, `SYS-1584` for funded transport with a full-payment continue,
  and `SYS-1585` for environmental danger increments and explosion bursts.
- Claim IDs: BR-002–BR-007, BR-009.

### Constraint Genes

- Reuse `CON-183`: retries require remaining finite life/continue stock,
  with a ten-crystal transport able to refill it. P1 states three remain
  after the first initial loss; no different post-training count is invented.
- The five-crystal minimum and up-to-ten spend belong to the transport rule,
  not a second independent resource or a duplicate numerical-price gene.
- Claim IDs: BR-004, BR-005.

### Information Genes

- Reuse `INF-142` for warning-timed defensive input from audible/visible cues.
- Add `INF-527` for the crystal/charge/location/danger display and local voice
  instruction without a complete map. A room name is not an omniscient route.
- Claim IDs: BR-006, BR-008, BR-009.

### Objective Genes

- Add `OBJ-303` for the complete first facility mission through its boss,
  graded result and successor access. Optional collection and rank are
  evaluated without being silently imposed as perfect-clear requirements.
- Claim IDs: BR-007, BR-009.

### Time Genes

- Reuse `TIM-003`: actor input, hazards, combat, pickup expiry and danger
  advance on the unpaused mission schedule. Start explicitly pauses.
  Elapsed time is displayed upward, not a prototype's fixed countdown.
- Claim IDs: BR-003, BR-005, BR-006, BR-008.

## Reproducible transitions

| Before | Input or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| An eligible obstacle lies in the steered route | Continue toward it | The authored auto-jump response supplements manual movement | Not every crossing requires a separate jump press | BR-002 |
| The ranger is airborne | Combine direction and thrust | Move in the requested admitted direction | No single-extra-jump stock is inferred for chained thrusts | BR-002 |
| Ordinary compatible fire is nearby | Tap B and let the pulse connect | Extinguish it and expose expiring crystals | Resource yield depends on shot class | BR-003 |
| A stronger flame or robot is in range | Hold B to full charge and release | Resolve the stronger laser; cleared fire supplies no collectible energy | Rapid clearing can sacrifice the next rescue resource | BR-003 |
| A live red or green crystal is within collection proximity | Move into it | Credit one or five energy units respectively | Pickup is automatic, not a separate inventory command | BR-003, BR-004 |
| An eligible survivor is approached with four crystals | Enter transport proximity | Insufficient reserve does not fund transport | Rescue is not a free contact reward | BR-004 |
| An eligible survivor is approached with five crystals | Enter transport proximity | Spend the available required reserve and transport the survivor | Rescue can consume the current damage buffer | BR-004, BR-005 |
| The same transport is funded with at least ten | Approach the survivor | Spend ten, record rescue and award a continue | Full funding creates a second survival benefit | BR-004 |
| Compatible damage arrives with a positive reserve | Let the hit resolve | Scatter the held reserve; approach recoverable crystals before expiry | Post-hit movement can rebuild protection | BR-005 |
| The ranger has just taken shield damage | Press X/Z promptly | Recover actionability sooner without refunding the hit | This contextual input is not a fresh route query | BR-005 |
| Compatible damage arrives with no crystals | Accept Retry if available | Spend continuation stock and restore the last continue point | A retry is not an in-place free resurrection | BR-005 |
| Danger approaches its next twenty-percent boundary | Continue on the live schedule | A temporary explosion burst creates immediate evasion pressure | Percentage is an evolving hazard system | BR-006 |
| Flames are removed or volatile containers explode | Let the event settle | Respectively reduce danger or raise it rapidly | Time alone does not determine current danger | BR-006 |
| A route switch has been reached | Use B and follow the opened route | Update required access, including the restored-power phase | Progression is ordered world state | BR-007 |
| The route is unclear | Press X/Z outside post-hit recovery | Receive a local instruction from Chris | Guidance supplies partial information, not automatic navigation | BR-008 |
| The final plant encounter is reached | Use compatible charged attacks and evade | Defeat Anemoth and enter Mission Result | Finding one survivor does not complete the mission | BR-003, BR-007 |
| Mission Result is active | Read categories, then choose B | Return to Mission Select with the next mission available | Rank and retained progression differ from perfection | BR-009 |

These reconstruct documented rules; no newly executed mission clear is claimed.

## Strategic and experiential structure

A fast charged clearance can remove danger while destroying the pickups that
would fund rescue and shield the ranger. Approaching a survivor at the minimum
price can remove that protection. Funding the larger price earns a continue,
which helps a later failed attempt rather than preventing the next hit.

The route problem is both spatial and informational. Camera control exposes
nearby geometry; Chris supplies a local instruction; neither gives a complete
map. Warning cues demand attention while danger and missed pickup opportunities
continue changing. The first boss adds a charged-attack encounter before the
mission's graded settlement.

## Replay and variation

The unit uses the original first-clear map. P1 places random generation after
all four missions and provides passwords to recover original layouts. Later
victim lists in S1 mix such variants and are not a fixed checklist here.
Exact rank thresholds and whether transported crystals are banked into the
final crystal tally remain unresolved between the booklet and retrospective
accounts. The admitted evaluation categories and successor do not depend on
inventing that formula.

## Adjacent systems and history

Training establishes the controls but is not the completed rescue mission.
Silent Blue adds underwater traversal; later missions add exceptional carrying
and ship play. None is inferred merely from the global booklet. Rescue mail
and long-term save management are separate possible modules.

## Normalised genome

| Type | Genes | Scoped role |
| --- | --- | --- |
| Action | `ACT-008`, `ACT-161`, `ACT-223`, `ACT-341`, `ACT-605`, `ACT-610`, `ACT-744`, `ACT-745`, `ACT-746` | Movement, combat, defence, fixtures, recovery, view, shots, thrust and guidance |
| System Behaviour | `SYS-037`, `SYS-215`, `SYS-369`, `SYS-605`, `SYS-755`, `SYS-773`, `SYS-948`, `SYS-1582`, `SYS-1583`, `SYS-1584`, `SYS-1585` | Pickups, combat, retry, route, destruction, rating, reserve loss, yield, auto-jump, rescue and danger |
| Constraint | `CON-183` | Finite replenishable continue stock |
| Information | `INF-142`, `INF-527` | Warning cues and local mission presentation |
| Objective | `OBJ-303` | Boss-complete graded facility mission |
| Time | `TIM-003` | Continuing unpaused mission simulation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `545` (`GAME-0001`–`GAME-0545`).
- Exact genome matches: none.
- Tied near matches: `GAME-0341` — Ninja Gaiden Black (`10 / 42 = 0.238095`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0341` — Ninja Gaiden Black | `ACT-008`, `ACT-161`, `ACT-223`, `ACT-341`, `SYS-215`, `SYS-369`, `SYS-755`, `SYS-773`, `INF-142`, `TIM-003` | Both use directly steered real-time attacks and defence, contextual fixtures, breakable objects, checkpoint restoration and evaluated mission completion. Ninja Gaiden adds held guard and uncollected Essence that accelerates charging. Burning Rangers uses pulse-created crystals for both hit protection and funded rescue, while charged clearance destroys that yield and environmental danger creates periodic explosion pressure. | Near, `0.238095` |

### Preserved research notes

- New genes: `ACT-744`–`ACT-746`, `SYS-1582`–`SYS-1585`, `INF-527`, `OBJ-303`.
- Classification result: New gene.
- Evidence and reasoning: pulse/laser yield, resource-funded rescue and periodic environmental danger distinguish the facility mission from ordinary combat or a terminal race clock.

## Taxonomy impact

- Sixteen definitions are reused and nine are added; 25 genes in total.
- Registry changes: nine new Active definitions.
- Taxonomy-change record: [TAXONOMY_CHANGE_293](../../../research/taxonomy-changes/TAXONOMY_CHANGE_293.md).
- Candidate terms affected: none.

## Negative results

- none.

## Delta summary

## New facts

- [Confirmed | Corroborated | High] Transport shares the hit buffer,
  spends up to ten crystals and grants a continue at full payment.

## New genes

- [Observation | Corroborated | High] Nine additions separate shot choice,
  thrust, guidance, yield, auto-jump, transport, danger, display and completion.

## New combinations

- [Observation | Corroborated | High] No new combination is proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_293`.

## New questions

- What are the native post-hit grace, scatter cap and danger floor rules?
- How exactly does the final crystal category treat transported energy?

## Next recommended game

- [Hypothesis | Limited | Medium] Full Meta Quest Walkabout Mini Golf in
  [Selection 043](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_043.md).
- Optimisation criterion: move from compound rescue pressure to tracked putting.
- Expected information gain: a bounded original-course hole and stroke settlement.
- Backlog impact: advance to `GAME-0547`.

## Why this game

- [Hypothesis | Limited | Medium] A tracked putting hole should distinguish
  physical stroke control from the rescue mission's shared resource pressure.
