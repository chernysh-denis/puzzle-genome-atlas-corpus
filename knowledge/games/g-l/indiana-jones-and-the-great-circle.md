---
game_id: GAME-0510
slug: indiana-jones-and-the-great-circle
game_title: Indiana Jones and the Great Circle
analysis_status: reviewed
reviewed: 2026-10-06
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-089
    - ACT-131
    - ACT-161
    - ACT-164
    - ACT-296
    - ACT-341
    - ACT-703
  system:
    - SYS-045
    - SYS-112
    - SYS-116
    - SYS-215
    - SYS-578
    - SYS-680
    - SYS-1388
    - SYS-1437
    - SYS-1438
    - SYS-1439
    - SYS-1440
    - SYS-1441
    - SYS-1442
    - SYS-1443
  constraint:
    - CON-140
    - CON-177
    - CON-282
    - CON-693
    - CON-773
  information:
    - INF-039
    - INF-073
    - INF-115
    - INF-119
    - INF-393
    - INF-480
    - INF-496
  objective:
    - OBJ-274
  time:
    - TIM-003
---

# Game: Indiana Jones and the Great Circle — complete opening investigation

Use the canonical [vocabulary and signature](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Controls, artifact names, physical geometry, marks, quantities, bar costs and
cinematic camera changes are parameters, not separate genes.

## Analysis scope

- Version / ruleset: English base single-player Xbox Series release of Indiana Jones and the Great
  Circle, complete The Golden Idol and The Break-In opening packet. Full release
  is dated 2024-12-09 by P1; R1 is an Xbox Series X-labelled recording published
  that day. Its exact installed patch, build checksum, Action/Adventure presets
  and modification status are not exposed. R3 is a separately qualified German
  premium-access recording dated 2024-12-06, not the admission target or proof
  of launch-binary parity. Later publisher tips and 2025 guides retain their
  dates.
- Structured analysis target: PLAT-XBOX-SERIES, English full-release base story;
  knowledge/platforms/games.json is authoritative. No release-platform audit is
  implied.
- Primary decision loop: Navigate the jungle and trapped temple, inspect and acquire reachable optional
  objects, reset or avoid hazards, attach the whip at the eligible gap, press
  marked floor plates with the torch, perform the sand exchange and escape the
  forced collapse. At Marshall College, investigate the intruder, perform the
  compulsory fist/guard/grapple tutorial, match four scattered exhibits, inspect
  optional notes and supplies, recover the pendant with Brody, acquire the
  journal and pack all four required objects. Stop at the Rome/Vatican arrival
  film before ordinary Vatican control.
- Entry and exit: Fresh base-story opening The Golden Idol, including its reachable
  jungle/temple alternatives, then the entire The Break-In college packet.
  Positive exit is the completed packing predicate, departure and arrival film;
  none of the first controlled Vatican exploration is admitted. Optional
  prologue objects and all ten college note identities, the acquired campus
  plan, apple, nurse’s bandage and available local interactions belong to the
  packet rather than being removed for a shorter profile.
- Included: Direct walk, sprint, crouch, jump and reachable ledge traversal; contextual
  holds/gestures, local reading and held-object inspection; aimed reusable whip
  gap crossing without an inferred adjustable simulation; trap reset, light
  avoidance, marked torch presses and wrong-plate hazard; mandatory
  sand-exchange collapse and live escape pressure; the giant’s live punches,
  guard, evasion and grapple escape followed by mandated knockout; shared
  exertion, guard-suppressed recovery, source-qualified food bonus and bandage
  recovery; four semantic artifact-display placements and missing-object
  inference; optional evidence acquisition and one-time Adventure Points;
  acquired full local floor plan, partial local sight, resource/tool disclosure,
  growing journal, ordered clue and packing gates, four retained suitcase
  contributions and next investigation lead.
- Excluded: Vatican free exploration, camera acquisition/photos/hints, disguises,
  merchants, Adventure Book spending, Medicine Bottle upgrades, firearm/revolver
  use merely because a gun lies in the office, later whip combat, body carrying,
  other regions, DLC, multiplayer, whole-campaign ending, achievements as
  mechanical objectives, New Game Plus, configurable difficulty as an analysed
  alternative ruleset, native damage/timing coefficients, controlled save/reload
  durability and any claimed transfer of dream inventory or points into the
  awakened college. The giant is not a winnable ordinary boss and adjusting sand
  does not establish a successful weight-balancing branch.
- Potential scoped modules: A complete Vatican camera/book/disguise investigation or later combat region
  needs its own dated packet. No module ID is created. Installed binary,
  captured presets, exact resource coefficients, consumable cancellation and
  checkpoint rollback sets remain open; documentation and sampled video are not
  own controller tests.
- Direct-play status: No own native executable, Xbox hardware, controller input, save or reload was
  tested. R1 is Skycaptin5’s Xbox Series X-labelled video, published 2024-12-09,
  metadata length 23544 seconds and player duration 23544.361. Paused muted
  frames in its opening 0:30–20:50 were inspected, including 390/398/405
  (crossing), 470/480/500/505/510 (torch floor presses), 515/517/520/525/535
  (sand and collapse), 556/610 (live escape), 760/763/768/770/775/781
  (combat/grapple), 890/895/900/905/915/917/920/924/930 (exhibits), 960/1015
  (clue acquisition), 1100/1110/1113/1120/1125/1138/1140 (journal/packing) and
  1220/1240/1250 (departure/arrival). The black frame at 485 supplies no rule
  evidence. R3 is Goody’s German college guide, published 2024-12-06, metadata
  777 seconds, player 776.541; inspected
  7/22/50/75/125/220/275/320/345/365/372/385/405/435/580/610/680/735. Native +15
  Adventure Points, reading/collection distinction and two-floor plan are
  separated from its editor-added collectible counter. Source identity, time,
  duration, no-ad, paused and muted checks accompany captures. This is
  attributed sampling, not continuous play, verified hardware, preset or build
  parity. All playback stayed headless and muted without fullscreen, focus or
  changes to user tabs/windows/system sound. No audio analysis or remote media
  download occurred. Frames and working prompts stay outside Git; artwork is an
  original illustration, not an official asset.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| IJ-001 | Xbox Series full release is 2024-12-09; attributed recording dates do not prove installed patch, presets or hardware. | Observation | Direct | High | P1; R1/R3 metadata |
| IJ-002 | Complete opening includes both prologue and college with reachable optional branches, ending at packed departure/arrival before Vatican control. | Observation | Corroborated | High | R1 opening; S1; S3; S4 |
| IJ-003 | An aimed eligible whip anchor enables the first local gap crossing; captured third-person passage does not prove adjustable reeling or free release momentum. | Observation | Corroborated | Medium | R1 390/398/405/410; S2 |
| IJ-004 | Trap reset and beam avoidance differ from marked torch-floor presses that release the next local passage; wrong plates expose a hazard. | Observation | Corroborated | Medium | R1 330/360/470/480/500/505/510; S2; S5 |
| IJ-005 | Sand adjustment still triggers collapse and a live escape; mandated final dream outcome does not make all intervening jumps harmless. | Observation | Corroborated | Medium | R1 515–625; S5; S2 |
| IJ-006 | The giant tutorial has live punches, guard and grapple escape, but its progression ends in a scripted knockout rather than a winnable boss terminal. | Observation | Corroborated | Medium | R1 760–810; R3 125; S1 |
| IJ-007 | Four museum artifacts must match their visual display correspondences; rejection retains the held object, and the complete set reveals the missing Cat Mummy. | Observation | Corroborated | High | R1 890–940; S1 exhibit |
| IJ-008 | Optional college notes have separate read/collect states and one-time Adventure Points; an acquired two-floor plan exposes position without exploring every corridor. | Observation | Limited | Medium | R1 960/1125; R3 50/365/372/385/405; S3; S7 |
| IJ-009 | The local apple can fund a temporary stamina bonus and the nurse’s bandage can restore health; exact use/cancellation timing was not tested. | Observation | Limited | Medium | S1 locations; S6/S7 indexed explanations; P4 later food corroboration |
| IJ-010 | Recovering the pendant changes investigation/preparation access; journal acquisition and four physical packing contributions precede departure, with pendant note registration at packing. | Observation | Corroborated | High | R1 985/1015/1100–1140/1220–1250; S1; S3 |
| IJ-011 | Melee, dodge and sprint use recovering exertion; guarding suppresses regeneration without a debit, and ordinary ledge travel is unpriced. | Observation | Limited | Medium | R1 610/765/768/775/781/875; S6 indexed article dated 2024-12-12 |
| IJ-012 | Camera, skill-book spending, disguises and later-region combat are not opening mechanics; a visible office gun is not observed firearm control. | Observation | Corroborated | High | P2 camera boundary; R1 opening/arrival; P4 later additions |
| IJ-013 | Nine additions and twenty-eight unchanged transfers represent the full packet; no previous gene definition or game signature is edited. | Observation | Direct | High | TAXONOMY_CHANGE_247; registry review |
| IJ-014 | Exact prior-signature and proper-combination scans are derived from the complete admitted set, not a genre ranking. | Observation | Direct | High | Corpus comparison; validator |

## Basic data

- Release / origin: MachineGames / Bethesda Softworks, full Xbox Series and
  Windows release 2024-12-09 (P1). Only PLAT-XBOX-SERIES is this structured
  analysis target; other releases are not inferred as audited.
- Families: FAM-002 hidden-state inference, FAM-007 physical object handling,
  FAM-010 live pressure, FAM-012 evidence progression, FAM-013 inventory/fixture
  dependencies and FAM-017 ordered dependencies. The hidden missing exhibit,
  physical placements, moving escape/combat, retained clues, four required
  packing identities and predecessor gates each materially support membership.
  Museum placement is not geometric bin packing; no FAM-006 is added.
- P1: [Xbox Wire release/gameplay announcement](https://news.xbox.com/en-us/2024/08/20/indiana-jones-and-the-great-circle-new-gameplay/),
  Joe Skrebels, 2024-08-20. Release/platform and general physical interaction
  context; marketing is not proof of every opening affordance.
- P2: [Xbox Wire starting tips](https://news.xbox.com/en-us/2024/12/05/indiana-jones-and-the-great-circle-starting-tips/),
  staff, 2024-12-05, actually read. Camera starts at the Vatican; broader book,
  disguise and weapon tips define exclusions, not opening admission.
- P3: [Creator puzzle interview](https://news.xbox.com/en-us/2024/12/02/indiana-jones-and-the-great-circle-puzzles-interview/),
  2024-12-02. Physical puzzles and configurable Adventure difficulty; no preset
  is inferred for R1.
- P4: [Publisher tips](https://bethesda.net/en-US/news/indiana-jones-and-the-great-circle-tips-and-tricks),
  Anne Lewis, 2025-04-17, actually read. Journal and fruit support qualitative
  corroboration. Its explicitly new book and PS5 context are later, not launch
  evidence or permission to admit them.
- P5: [Publisher Update 1](https://bethesda.net/en-US/news/indiana-jones-and-the-great-circle-tm-update-1),
  2024-12-08. A public changelog is not R1's verified installed build.
- R1: [Skycaptin5, Xbox Series X-labelled full walkthrough](https://www.youtube.com/watch?v=syUhgITiDf0),
  published 2024-12-09, metadata 23544 seconds, actual 23544.361. Only sampled
  opening frames listed above were inspected; no whole-video watch or native
  execution is claimed. Facecam obstructs part of the lower-left HUD.
- R3: [Goody, German Marshall College collectible guide](https://www.youtube.com/watch?v=MNXGvvd47DY),
  published 2024-12-06, metadata 777 seconds, actual 776.541. Qualified premium
  access, unknown hardware/build; optional note/map observation is supplementary
  and remains Limited/Medium. Editor-added counts are not native HUD.
- S1: [Greg Wheeler, The Break-In route](https://www.thereviewgeek.com/indianajonesgreatcircle-breakin-walkthrough/),
  2024-12-10, updated 2024-12-13, actually read. Four exhibits and four packing
  objects corroborate R1. Optional apple/bandage locations are documentary,
  not own use tests. Reference pictures, not historical flag accuracy, establish
  display correspondence.
- S2: [The Golden Idol route](https://www.thereviewgeek.com/indianajonesgreatcircle-goldenidol-walkthrough/),
  relevant indexed passages were read; full page fetch was unavailable. Used
  only with actual R1 observations and S5, not as claimed full-guide review.
- S3: [Matt Villei, college note locations](https://gameranx.com/features/id/518665/article/indiana-jones-and-the-great-circle-all-marshall-college-note-locations/),
  2024-12-16, actually read. Ten identities include two required story records;
  pendant note registration occurs on packing.
- S4: [Opening collectible route](https://nightlygamingbinge.com/the-golden-idol-collectibles-indiana-jones-and-the-great-circle/),
  2024-12-11, actually read. Warriors of the Clouds book, Chachapoyan Urn,
  Stone Mace Head and Chachapoyan Vase are local optional interactions; their
  persistence or AP transfer into the college is not asserted. A later route's
  claim of no prologue collectibles does not establish absent physical objects
  or classify this lore book as a spendable Adventure Book.
- S5: [Temple puzzle route](https://www.gamepressure.com/indiana-jones-and-the-great-circle/the-temple-of-the-golden-idol/zb1170b),
  updated 2025-01-23, actually read. Marked plate, beam and forced sand-exchange
  outcome corroborate R1; later date and absence of a controlled alternative
  replay remain explicit.
- S6: [Release-period stamina account](https://game8.co/games/Indiana-Jones-and-the-Great-Circle/archives/488078),
  dated 2024-12-12. Indexed body was read; direct page fetch returned 403.
  Distinct costs, guard-suppressed recovery and fruit bonus remain qualified
  documentary evidence, not natively measured coefficients.
- S7: [Beginner controls/resources account](https://game8.co/games/Indiana-Jones-and-the-Great-Circle/archives/486991),
  dated 2024-12-08. Relevant indexed body read: bandages, food, bounded stock
  and acquired maps. No exact cancellation policy is inferred.
- Claim IDs: IJ-001–IJ-014. Qualified source dates remain independent of the
  admitted full-release target.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: ACT-008/048/089/131/161/164/296/341.
- Added gene: ACT-703. Movement includes crouch, jump, ledge and local dodge
  controls as parameters; the floor press, spider removal, trap reset, local
  radio/cabinet use and prompted grapple escape are contextual requests.
  Portable museum/packing objects differ from notes acquired into discrete
  inventory. Consuming an item is an accepted use effect, not an asserted
  zero-duration animation or interruptible cast.
- Boundaries: ACT-531 requires adjustable reeling/chosen release; ACT-361 is
  an endpoint pull. Neither is silently inferred from a cinematic whip swing.
  A required gesture has no demonstrated expiry; no timed-QTE gene is added.
- Claim IDs: IJ-003–IJ-011.

### System Behaviour Genes

- Existing gene IDs: SYS-045/112/116/215/578/680/1388.
- Added genes: SYS-1437–1443. Scripted loss does not eliminate live combat
  decisions or escape failure. The sand prompt does not prove a weight-solving
  alternative, and an ordinary ledge does not prove stamina-priced wall grip.
- Resolution order: eligible movement/interaction resolves against current
  reach and tool; marked presses change local floor safety; accepted anchor
  crossing restores supported traversal. Sand exchange releases the mandated
  escape sequence. College encounter responses progress to authored knockout.
  Compatible exhibit placements retain identity, rejection preserves the held
  object and completing four reveals the absent exhibit. Examined trail and
  pendant advance inquiry; collecting notes records identity and discovery
  points. Acquisition of the journal and retained four-item suitcase completion
  enable the cinematic successor route.
- Parameters: quantities, artifact correspondence, floor geometry, authored
  gestures, stamina coefficients, temporary bonus and observation horizon.
  Bandage recovery is source-qualified; no partial-health recovery law or
  exact animation/cancellation schedule is invented.
- Claim IDs: IJ-003–IJ-011.

### Constraint Genes

- Existing gene IDs: CON-140/177/282/693/773. Five unchanged boundaries:
  required distinct packing identities, finite carried consumable stock,
  ordered story conditions, reachable eligible tether anchor and ordinary
  vitality before local retry. Scripted knockout is not ordinary health failure.
- Candidate genes: none. Artifact-display correspondence is the eligibility
  parameter of SYS-1438, not a second name for its rejection transition.
- Scarce resources: current health, ordinary/bonus exertion, finite local food
  and bandage stock, next legal route state. Optional AP is retained knowledge
  credit, not a spendable opening skill menu. S7's stock cap is a parameter,
  not a claimed count of nurse-cabinet items.
- Claim IDs: IJ-003/006–IJ-011.

### Information Genes

- Existing gene IDs: INF-039/073/115/119/393/480.
- Added gene: INF-496. Physical reference pictures and rejection speech are
  local matching feedback, not an omniscient solution table. The growing
  journal is reused without importing L.A. Noire's credibility judgement.
  Required suitcase identities/filled state differ from optional note count.
  An acquired floor plan is not progressively explored terrain or a paired
  dungeon map-and-compass unlock.
- Parameters: current hand, health/stamina/points, local giant animation,
  literal prompts, clue roster, known lead and current floor/position.
  No spatial-audio claim is made from muted research.
- Claim IDs: IJ-004/006–IJ-011.

### Objective Genes

- Existing gene: OBJ-274. Complete the situated opening inquiry and required
  physical encounters into the Rome/Vatican successor lead; neither defeat of
  the giant nor solving the entire global mystery is the terminal.
- Success: four required packed identities, departure and arrival film.
  Optional ten-note completion is not a main-story requirement. Ordinary live
  route failure requires a declared retry; exact rollback/persistence was not
  tested. Compulsory sand/giant adverse outcomes instead advance the story.
- Claim IDs: IJ-002/005/006/010.

### Time Genes

- Existing gene: TIM-003. Input and live combat, escape hazards and exertion
  continue in real time outside authored locks; no universal packet countdown
  or expiring cue is asserted. Films and item animations are mode boundaries,
  not separate timing genes.
- Claim IDs: IJ-003–IJ-011.

## Reproducible transitions

The following are source-grounded replay instructions, not fabricated own runs.
Native timing, presets and reload comparisons remain explicitly untested.

| Before | Action | Resolution | Boundary established | Claim |
|---|---|---|---|---|
| Retractable temple trap and visible beam | Reset locally, then crouch along the permitted side | Reset removes the immediate obstruction; entering the hazardous light is a separate failure risk | Reset is not universal invulnerability | IJ-004 |
| Eligible gap anchor | Aim and request whip crossing | Attachment supports passage and returns control on the far side | No inferred arbitrary reel/release simulation | IJ-003 |
| Marked floor plate | Aim held torch and press | Local plate/trap withdrawal permits the next reach | Active state change rather than passive clue reading | IJ-004 |
| Unsafe floor contact | Press or step on the wrong plate | Hazard is exposed instead of legal local withdrawal | Wrong contact is not a neutral rejected menu choice | IJ-004 |
| Idol and selected Sand Bag | Perform required adjustment/exchange | The authored collapse follows and escape control resumes | No successful balancing branch is admitted | IJ-005 |
| Return gap before scripted handoff | Respect the authored exchange, then run/jump | Correct sequence advances; premature jump can require retry | Live route failure differs from mandated final dream outcome | IJ-005 |
| Giant tutorial | Punch, guard or respond to grasp | Live stamina/combat response occurs, then the authored knockout | Successful local response is not a boss-victory terminal | IJ-006 |
| Carried exhibit at incompatible display | Request placement | Rejection leaves the object held | No consumption or fabricated placement penalty | IJ-007 |
| Four compatible displays | Return each matching artifact | Retained set reveals the missing Cat Mummy | Four identities, not three or any four objects | IJ-007 |
| Readable college letter not yet collected | Read, then separately collect | Native acquisition records its identity and discovery credit | Readability alone is not pickup | IJ-008 |
| Campus plan still on board | Collect and open it | Authored local floors and position are inspectable | Not a visited-corridor exploration fill | IJ-008 |
| Available fruit and base stamina | Select and consume the apple | Documentary temporary bonus supports the declared consecutive-spending threshold | No permanent capacity purchase or automatic bonus refill | IJ-009/011 |
| Missing health and carried bandage | Select and complete its use | Compatible health recovery is requested/applied | Cancellation and exact latency remain unmeasured | IJ-009 |
| Fallen shelf and pendant above | Cooperate with Brody, climb and take pendant | Investigation/preparation access advances | Seeing it alone does not complete later note registration | IJ-010 |
| Journal acquired, suitcase partly filled | Bring each of photo, pendant, record and bullwhip | Required contributions remain filled; complete set enables departure | Optional note collection is not required packing | IJ-010 |
| Completed packing and arrival film | Stop before Vatican control | Successor inquiry is exposed, not yet executed | Camera/disguise/book mechanics remain outside this packet | IJ-002/012 |

## Strategic and experiential structure

- Local decision: infer safe floor interactions, fit artifacts to the visible
  references, manage exertion versus guard and decide when to inspect or collect.
- Medium-term planning: follow evidence while retaining optional supplies/notes;
  satisfy dependencies before packing, rather than search the whole campaign.
- Long-term structure: successor investigation only; no claimed solved mystery.
- Common heuristics: inspect local markings and pictures, distinguish readable
  from acquired, avoid assuming guard refills stamina, and separate mandatory
  story loss from a failed local movement.
- Failure attribution: wrong plate, illegal display, depleted effort and
  scripted knockout have different consequences. Exact coefficients remain open.
- Player-trust factors: visible prompts, reference pictures and journal support
  causal reading; sandbox-looking sand preparation is a mandated outcome, which
  the analysis discloses rather than presenting as a freely solved puzzle.
- Claim IDs: IJ-003–IJ-012.

## Replay and variation

- Alternatives: optional prologue branches, college notes/map/supplies, exhibit
  order and live response timing. Authored main sequence/required identities
  remain fixed. The ten-note guide count is not a random collectible spawn law.
- No seed, procedural map, universal replay persistence or optimal route is
  claimed. Dream pickup registration after awakening remains unverified.
- Claim IDs: IJ-002–IJ-012.

## Adjacent systems and history

- The opening recreates an authored film situation in interactive form;
  licensed setting and camera choice do not themselves create a mechanical gene.
- Current publisher descriptions cover later affordances that this first
  packet does not possess. Premium-access source date is not hidden or relabelled.
- Decision comparison is limited to the exact/tied selections computed below.
- Claim IDs: IJ-001/002/012–IJ-014.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-008, ACT-048, ACT-089, ACT-131, ACT-161, ACT-164, ACT-296, ACT-341, ACT-703 | No additional candidate IDs; scoped parameters above |
| System Behaviour | SYS-045, SYS-112, SYS-116, SYS-215, SYS-578, SYS-680, SYS-1388, SYS-1437, SYS-1438, SYS-1439, SYS-1440, SYS-1441, SYS-1442, SYS-1443 | No additional candidate IDs; scoped parameters above |
| Constraint | CON-140, CON-177, CON-282, CON-693, CON-773 | No additional candidate IDs; scoped parameters above |
| Information | INF-039, INF-073, INF-115, INF-119, INF-393, INF-480, INF-496 | No additional candidate IDs; scoped parameters above |
| Objective | OBJ-274 | No additional candidate IDs; scoped parameters above |
| Time | TIM-003 | No additional candidate IDs; scoped parameters above |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `509` (`GAME-0001`–`GAME-0509`).
- Exact genome matches: none.
- Tied near matches: `GAME-0258` — Prey (2017) (`12 / 51 = 0.235294`).
- Supported combination subsets: none.
- Scan date: 2026-10-06.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| GAME-0258 Prey (2017) | ACT-008, ACT-161, ACT-164, ACT-341, CON-282, INF-073, INF-115, INF-119, SYS-112, SYS-215, SYS-578, TIM-003 | Both retain direct first-person control, aimed combat, active-hand selection, local fixture progress and visible personal resources. This opening instead requires marked trap probes, semantic exhibit matching, mandated adverse gates and four-object packing; Prey's finite GLOO supply, prop disguise, temporary restraint and verified reload settlement remain outside this opening. | 12 / 51 = 0.235294 |

- New genes: ACT-703, SYS-1437–1443 and INF-496.
- Classification result: New gene.
- Evidence and reasoning: complete signatures and verified proper subsets are
  computed, not chosen by visual theme or genre (IJ-013/014).

### Preserved research notes

- New genes: ACT-703, SYS-1437–1443 and INF-496.
- Classification result: New gene.
- Evidence and reasoning: complete signatures and verified proper subsets are
  computed, not chosen by visual theme or genre (IJ-013/014).

## Taxonomy impact

- Registry changes: nine Active additions and twenty-eight unchanged transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_247](../../../research/taxonomy-changes/TAXONOMY_CHANGE_247.md).
- Candidate terms affected: none. No existing signature/definition, published
  r000024 public commit/tag, mapping or release audit changes.
- Claim IDs: IJ-013/014.

## Negative results

- No new structured negative-result record. Adjustable tether, timed-QTE,
  all-actions shared exertion, explored-map and future-camera boundaries fail
  this transfer without being declared globally invalid.
- Claim IDs: IJ-003–IJ-012/013.

## Delta summary

## New facts

- [Observation | Corroborated | High] Four matched exhibits expose the stolen
  object's identity; four packing contributions enable the successor (IJ-007/010).
- [Observation | Corroborated | Medium] Mandated story losses coexist with
  meaningful live route/combat control (IJ-005/006).
- [Observation | Limited | Medium] Optional consumable, exertion and map
  branches retain their documentary and premium-access source limits (IJ-008/009/011).

## New genes

- [Observation | Corroborated | Medium] ACT-703 and SYS-1437–1440/1443 isolate
  requested crossing, local floor withdrawal, semantic exhibit rejection,
  mandatory interactive outcomes and distinct note credit (IJ-003–IJ-008/010).
- [Observation | Limited | Medium] SYS-1441/1442 and INF-496 retain qualified
  guard/recovery, fruit bonus and acquired floor-plan boundaries (IJ-008/009/011).

## New combinations

- [Observation | Direct | High] No new combination is minted from a convenient
  illustration or partial opening fragment; all verified subsets are scanned.

## Taxonomy changes

- [Observation | Direct | High] TAXONOMY_CHANGE_247 accepts nine bounded
  additions without changing previous signatures or English definitions.

## New questions

- [Hypothesis | Limited | Medium] A controlled launch-build/preset replay could
  refine exertion, bonus use, item cancellation and checkpoint rollback; none
  of those numeric or persistent outcomes is invented from a source timestamp.
- [Hypothesis | Limited | Medium] Native opening-versus-awakening inventory
  comparison could determine dream collectible persistence; no transfer is encoded.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0511 original Nintendo 3DS Animal
  Crossing: New Leaf follows this accepted unit, local commit and stop window.
- Optimisation criterion: approved retro/platform alternation and contrast
  authored evidence traversal with social/calendar and local-world decisions.
- Expected information gain: a complete original-release packet, not a promised
  number of new genes or the later Welcome amiibo ruleset.
- Backlog impact: unit 16/18 in Selection 039; no push/publication/deploy.

## Why this game

- [Hypothesis | Limited | Medium] The approved modern Xbox slot supplies a
  physical clue/fixture loop rather than another first-person shooting packet.
  Similarity and novelty still depend on the admitted complete signature.
