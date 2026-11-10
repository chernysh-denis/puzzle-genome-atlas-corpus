---
game_id: GAME-0513
slug: thief-the-dark-project
game_title: Thief: The Dark Project
analysis_status: reviewed
reviewed: 2026-10-06
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-049
    - ACT-089
    - ACT-130
    - ACT-161
    - ACT-164
    - ACT-202
    - ACT-341
    - ACT-491
    - ACT-705
    - ACT-708
  system:
    - SYS-036
    - SYS-057
    - SYS-215
    - SYS-373
    - SYS-543
    - SYS-578
    - SYS-605
    - SYS-797
    - SYS-1450
    - SYS-1451
    - SYS-1452
  constraint:
    - CON-077
    - CON-198
    - CON-282
    - CON-285
    - CON-296
    - CON-335
    - CON-460
    - CON-773
    - CON-792
    - CON-793
    - CON-794
  information:
    - INF-073
    - INF-075
    - INF-115
    - INF-117
    - INF-316
    - INF-480
    - INF-498
  objective:
    - OBJ-291
  time:
    - TIM-003
    - TIM-007
---

# Game: Thief: The Dark Project

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Parameters refine transitions, not gene identities.

## Analysis scope

- Version / ruleset: Original released English Windows Thief: The Dark Project, complete Lord
  Bafford’s Manor on Expert, documentary v1.33 as identified by S1. Original
  1998 Looking Glass/Eidos instructions P1 and the licensed 1998 Prima guide P2
  corroborate the mission and rules; the developer’s 1999 postmortem P3
  corroborates perception architecture. This is not a claim that the 1998
  shipping executable was already v1.33. No installed executable, original-disc
  identity, patch installation, hash, native save or current-store parity was
  verified.
- Structured analysis target: PLAT-WINDOWS-PC, original English Lord Bafford’s Manor, Expert;
  knowledge/platforms/games.json is authoritative. No release-platform audit is
  implied.
- Primary decision loop: Prepare affordable utility arrows from the displayed pre-mission budget,
  navigate the street/sewer/well/manor, inspect partial local cues, pickpocket
  matching keys or nonlethally incapacitate eligible guards, and collect the
  scepter plus sufficient other valuables. Choose quieter floors and posture,
  time autonomous patrols, change torch light with finite water arrows, move
  discoverable bodies, and return through the operated exit gate. Air, health,
  equipment compatibility, carrying restrictions, prohibited fatalities and
  manual saved-history recovery remain causal, including unsuccessful branches.
- Entry and exit: Fresh mission selection with the tutorial skipped, Expert selected before the
  first pre-mission purchase screen; then ordinary street control before
  entering the manor or taking local valuables. The entry budget and stock are
  the currently displayed original-version values, not claimed numeric
  observations. Exit is ordinary mission success after entering the manor,
  acquiring the unique jeweled scepter, carrying at least 700 other loot value,
  maintaining mandatory no-kill eligibility and returning to the city street.
  The whole mission, including reachable optional items and adverse
  alternatives, is the packet; not merely one torch or a successful-only
  corridor.
- Included: Affordable pre-mission purchase and its visible costs/stock; direct
  walk/run/swim, contextual ladder attachment/release and mantling, currents and
  finite breath; crouch/lean and current local sight/sound;
  surface/speed-dependent footsteps, directed occlusion and
  light/movement/weapon-sensitive awareness with autonomous patrol, search and
  combat; world collection, matching worn-key theft, selected equipment and
  local switch/door/chest/key use; held/released finite water-arrow shots,
  evolving bow draw and eligible torch extinction; eligible head blackjack and
  persistent discoverable unconscious bodies, body carrying and quiet release;
  current loot aggregation, health and available healing effects, manual
  save/restore; imperfect authored map, compass, current
  exposure/air/health/item/objective information; required unique item, 700
  other valuables, no human fatalities and street extraction. Optional supplies,
  papers and reachable alternative approaches are documented; unexecuted
  alternative Actions are not silently admitted.
- Excluded: Training, later campaign levels, Gold additions, TFix/NewDark/HD
  modifications, the 2014 reboot, fan missions and current Steam/GOG product
  equivalence; later lockpicks, rope/moss/fire/gas/noisemaker arrows, mines,
  holy water and air/speed potions not established in this mission. Available
  but unexecuted refund, sword/broadhead attack, flashbomb throw, healing
  consumption and miscellaneous-prop throwing are described without admitted
  Action IDs under the current conservative admission rule; Proposed ADR-013
  authorises nothing. No exact initial cash/stock, prices,
  damage, hearing radius, draw seconds, patrol seed, deterministic patrol
  schedule, animal-kill exemption, instantaneous objective-failure timing or
  saved-file byte coverage is established. Carrying and fixed-item selection are
  distinguished; no automatic authored checkpoint is invented from manual
  save/load.
- Potential scoped modules: A complete later dated mission with lockpicking, rope/moss arrows or
  supernatural enemies would require independent entry/exit, availability and
  full alternatives. No module or next game is authorised. Controlled
  original-v1.33 tests could refine map updates, carry/selection priority,
  animal eligibility and reload fidelity without changing this documented human
  no-kill contract.
- Direct-play status: No native game was obtained or run. No video or audio was played, downloaded
  or analysed. P1 was read as text and visually inspected through its movement,
  interaction, stealth, bow, tools, health, map, objective, purchase and save
  sections (PDF spreads 9–18, printed 10–27; PDF 17/18 repeat printed 18/19).
  P2’s complete Bafford chapter, printed 59–68 / PDF 80–89, was read and all ten
  pages visually inspected; its photographed 350-loot sheet is Hard, not the
  Expert 700 quota stated in prose. P3’s perception/room sound/difficulty
  sections were read. S1 is the accessible original-PC-v1.33 FAQ v0.1, full
  Bafford text read; mirrors of the same author are not independent sources. The
  later GameFAQs version was blocked, so indexed loadout excerpts do not
  establish native numeric starting values. Transition tables are documentary
  operational predictions, not controlled executions. Quantitative,
  animal-failure, fixed-use priority and restoration limits remain explicit. PDF
  inspection and hidden source reading did not change the user’s windows, focus,
  fullscreen or system sound; working files and prompts remain outside Git.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| TH-001 | Original Windows Lord Bafford’s Manor, Expert, is a complete bounded mission; documentary v1.33 is not an installed binary or 1998 shipping-patch claim. | Observation | Corroborated | High | P1/P2; S1 explicit original-PC version |
| TH-002 | Preparation uses visible finite cash and offered stock, then the sewer/well entrance exposes ladder, current, underwater-air and matching-key choices. | Observation | Corroborated | High | P1 loadout/movement; P2 complete Bafford route; S1 |
| TH-003 | Held utility bow draw changes power, reach, zoom and fatigue; the current tool and compatible finite arrow reserve condition legal release. | Observation | Corroborated | High | P1 printed 16-19; no exact seconds measured |
| TH-004 | Water-arrow contact extinguishes eligible torch flame and changes local illumination, not a persistent traversable water layer or protective light weapon. | Observation | Corroborated | High | P1 printed 18/23; P2 Bafford torches; S1 |
| TH-005 | Surface and movement generate different sound, while directed geometry/light/movement affect observer acquisition and subsequent investigation. | Observation | Corroborated | High | P1 movement/stealth; P2 floor choices; P3 AI/room sound; S1 |
| TH-006 | Reachable worn keys may be stolen from unaware living owners; a head blackjack depends on target awareness and eligibility and can be nonlethal. | Observation | Corroborated | High | P1 pickpocket/blackjack; P2/S1 well and patrol approaches |
| TH-007 | Unconscious bodies remain discoverable and can be carried/placed; occupied carrying blocks attacks and other-item use. Fixed-use selection priority is documentary, not natively replayed. | Observation | Corroborated | High | P1 carrying/interaction; P2/S1 hidden bodies |
| TH-008 | Expert success combines unique scepter, at least 700 other loot, maintained no-kill eligibility and street extraction; exact animal/failure timing is not established. | Observation | Corroborated | High | P1 Expert humans; P2 Expert prose; S1 Expert list and exit |
| TH-009 | Current gem, items/loot, health/air, objective sheet, partial map and compass give different present information, not omniscient future patrols. | Observation | Corroborated | High | P1 interface/map/objectives; P2 map; S1 compass |
| TH-010 | Explicit manual save/load supports another continuation; native state fidelity and automatic checkpoint restoration were not demonstrated. | Observation | Limited | Medium | P1 menus/F11/F12; S1 patrol saving; no native save |
| TH-011 | Nine additions and thirty-four unchanged transfers describe the whole mission, with unused optional Actions and inaccessible late tools kept separate. | Observation | Direct | High | TAXONOMY_CHANGE_250; reviewed registry boundaries |
| TH-012 | Every lower-ID complete signature and every verified proper combination subset is recomputed. | Observation | Direct | High | Corpus comparison; deterministic repository validator |

## Basic data

- Release / origin: original Looking Glass/Eidos 1998 Windows product.
  Documentary original v1.33 is identified by S1, not a verified installed patch.
- Structured target: PLAT-WINDOWS-PC; no whole-product release audit.
- Families: FAM-010 autonomous patrol pressure, FAM-013 carried-key fixture
  dependencies and FAM-017 ordered ingress/tool/loot/extraction requirements.
- P1: [Original instruction booklet](https://www.abandonwaredos.com/public/aban_files_giochi/thiefdarkprojectmanual.pdf),
  Looking Glass/Eidos, 1998. Movement, interaction, stealth, bow, tool, health,
  map, objective, purchase and save sections read in text and visually inspected.
  This is a document scan, not a linked executable or store-parity assertion.
- P2: [Licensed Prima guide](https://the-clocktower.net/wp-content/uploads/2022/06/Thief-The-Dark-Project-Prima-Guide.pdf),
  Steve Honeywell, 1998, ISBN 0761517472. Complete Bafford chapter printed
  59-68 / PDF 80-89 read and visually inspected. Its objective photograph is
  Hard 350; Expert 700 and no-kill are established separately in its prose.
  Production acknowledgements mention early material, so exact patch fidelity
  is not inferred from publication year or photographs.
- P3: [Developer postmortem](https://www.gamedeveloper.com/design/postmortem-i-thief-the-dark-project-i-),
  Tom Leonard, 1999-07-09. Relevant AI perception, room sound propagation and
  difficulty/objective sections read. Architecture is qualitative support,
  not a measured Bafford hearing radius or exact live patrol schedule.
- S1: [Original PC-v1.33 Bafford FAQ](https://www.mogelpower.de/cheats/loesung.php?id=7310&pf=99),
  The Brigadier, FAQ v0.1, undated accessible mirror; full first-mission body
  read. Its version and explicit Expert objectives ground the complete written
  intervention route. Reproductions by the same author are not independent.
  Later GameFAQs text was blocked; indexed loadout snippets do not justify
  precise initial cash, stock or prices. No source email is preserved here.
- Source conflict: Normal lists fewer objectives in S1; P2's general exit
  prose is not used to add Expert's quota to Normal. The selected Expert packet
  has independently corroborated quota, no-kill and exit. S1 says no pets as
  well; P1 names fellow humans. No animal exemption or kill test is inferred.
- Claim IDs: TH-001-TH-012. No native media, audio or game execution is claimed.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: ACT-008/049/089/130/161/164/202/341/491/705.
- Added ACT-708: selected finite utility arrow, held aim and commanded release.
- Parameters: walk/run/swim, ladder/ledge, current posture and lean, highlighted
  item, carried key, local lever/door/chest/book, quiet body release, save menu.
- World pickup ACT-089 and active-hand selection ACT-164 are distinct;
  ACT-199's compatible-slot transfer is not added as a second equivalent pickup.
  An eligible blackout strike is ACT-161, but changing flame with water does
  not satisfy its hostile-or-breakable combat-target boundary.
- Affordable purchase is admitted preparation. Refund, lethal sword/broadhead,
  flashbomb, drinking and junk throwing remain available unexecuted alternatives
  in prose under the current conservative admission rule, not extra admitted
  Actions. Proposed ADR-013 remains unaccepted.
- Claim IDs: TH-002-TH-007/010/011.

### System Behaviour Genes

- Existing gene IDs: SYS-036/057/215/373/543/578/605/797.
- Additions: SYS-1450 live draw development, SYS-1451 eligible flame extinction,
  SYS-1452 surface/rate-generated footstep stimulus.
- Resolution order: live movement resolves against geometry/current. Footsteps
  arise from floor and movement; eligible listeners acquire local stimuli and
  change awareness and route. Bow draw develops while held; legal release pays
  compatible reserve. Eligible water impact changes torch state, then the new
  illumination changes subsequent detection. A qualified head strike resolves
  nonlethal incapacity; carrying and placing preserves a discoverable body.
  Key and switch operations update route flags, while valuables accumulate
  carried value and completed mandatory predicates settle street extraction.
- Breath depletion can cause damage; injury and optional recovery affect one
  health pool. These supporting adverse alternatives are not omitted because
  the documented successful route avoids drowning or lethal combat.
- No native damage, sound, friction, force, draw or awareness coefficients.
- Claim IDs: TH-002-TH-008/010/011.

### Constraint Genes

- Existing gene IDs: CON-077/198/282/285/296/335/460/773.
- Additions: CON-792 living unaware-owner transfer; CON-793 occupied carry and
  other-use exclusion; CON-794 mandatory human no-kill success eligibility.
- Scarcity: finite preparation cash, compatible arrows, breath and health.
  There is no inserted inventory-cell cap, firearm reload, ammo refill cap or
  persistent next-mission gear. Starting prices and stock remain documentary.
- A living worn-key transfer need not incapacitate its owner. Alert armed
  targets do not satisfy the ordinary quiet-blackjack conditions. Nonlethal
  incapacity need not violate Expert's mandatory no-kill predicate.
- P1 independently forbids fixed-object use while general inventory is selected;
  occupied junk/body use invokes release/throw instead of ordinary other-item
  use. Clear selection and place the body before fixtures. Exact native
  selection-priority rejection has not been replayed; no sidearm exception or
  universal two-handed-only limitation is imported from CON-644.
- Claim IDs: TH-002/003/006-TH-008/010/011.

### Information Genes

- Existing gene IDs: INF-073/075/115/117/316/480.
- Added INF-498: imperfect authored map and independently selected compass.
- Loot selection shows aggregate value, not merely pickup count. Air bubbles
  and red health shields expose present reserves. The visibility gem grades
  exposure with light/movement/readied-tool effects but does not disclose each
  observer's exact alert or guarantee invisibility.
- INF-480 covers inspectable current objectives independently from the map;
  INF-125 explored-terrain growth and INF-496 precise acquired-plan position
  are not transferred. Compass direction is not an exact current-coordinate
  guarantee; reaching a hidden room does not reveal the whole future route.
- Claim IDs: TH-002/005/009/011.

### Objective Genes

- Added OBJ-291: unique item plus independent aggregate-value quota and street
  extraction while mandatory conduct predicates remain valid.
- Expert requires at least 700 other valuables as well as the scepter. Neither
  reaching the street first nor acquiring only the scepter settles success.
  Collecting every optional valuable is not mandatory. Normal/Hard objectives
  differ and do not enter this signature as alternate modes.
- Failure: zero health or violating the prohibited human-fatality condition
  invalidates the ordinary attempt; exact failure tick and animal treatment
  are unresolved, not an asserted permission to kill spiders.
- Claim IDs: TH-001/008/011.

### Time Genes

- Existing gene IDs: TIM-003/007. Patrols, air and bow draw change on live time;
  explicit manual retained history permits a later different intervention.
- Mission menus pause play; no self-imposed timer or mandatory countdown is
  invented. A walkthrough's suggested waiting count is a heuristic, not a
  fixed patrol period. Manual save/load is not SYS-369's authored checkpoint.
- Claim IDs: TH-003/005/010/011.

## Reproducible transitions

These are source-grounded operational predictions, not native executions.
Read initial cash, stock and prices on the actual preparation screen rather
than copying later indexed excerpts. Follow current patrol cues, not a clock.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh mission selection | Choose Expert, inspect offered preparation and buy affordable water arrows | Current budget falls by displayed price; selected stock changes | Finite preparation, no invented cash value | TH-001/002 |
| Street before manor entry | Traverse sewer ladders and operate the local lever | Connected approach changes without collecting the scepter | Switch and locomotion are separate | TH-002 |
| Unaware well guard, highlighted worn key in reach | Take the key | Key transfers while the owner can remain standing | Pickpocket is not knockout | TH-006 |
| Wellhouse lock, matching key available | Select/apply key, clear ordinary selection and open | Required entry is unlocked and then traversable | Matching authority and interaction priority | TH-002/007 |
| Underwater tunnel, positive air | Swim with current and surface | Current changes movement and breathing becomes available | Live motion and reserve are causal | TH-002 |
| Underwater without breathable source | Remain until reserve exhaustion | Bubbles decline and drowning damage begins | Water is not indefinite concealment | TH-002/009 |
| Reachable pool/chest valuables | Open and take eligible items | Carried value increases; optional supplies may be retained | Quota concerns value, not pickup count | TH-002/008/009 |
| Patrol corridor with carpet and hard floor | Choose movement rate and surface | Footstep stimulus differs before observer processing | Stimulus source differs from AI response | TH-005 |
| Dark doorway near directed guard sight | Crouch/lean, observe and wait | Current geometry/exposure and patrol opportunity change | No guaranteed invisibility or exact schedule | TH-005/009 |
| Water type selected with compatible reserve | Hold draw, aim and release at torch | One arrow launches; eligible contact extinguishes flame | Command, eligibility and effect are distinct | TH-003/004 |
| Fully drawn bow retained | Keep holding without release | Later zoom/wobble/automatic letdown occur | No permanent steady full draw | TH-003 |
| Extinguished eligible torch | Traverse the formerly lit approach | New illumination changes subsequent acquisition | Not an invented traversable puddle | TH-004/005 |
| Eligible unaware guard head behind reach | Strike with blackjack | Nonlethal incapacity can leave a discoverable body | Nonlethal result preserves human no-kill | TH-006/007/008 |
| Alert armed guard | Attempt the same ordinary quiet knockout | Unawareness/eligibility condition is not met | Tool possession alone is insufficient | TH-006 |
| Unconscious body in traffic | Carry and quietly place in a dark recess | Body location changes; it remains discoverable | Placement is not deletion | TH-007 |
| Body/junk physically carried | Try attack or another inventory use | Ordinary other-use eligibility is blocked until release | Not a sidearm-compatible two-handed rule | TH-007 |
| Selected ordinary inventory item, fixed door | Clear selection before ordinary fixture use | Fixed operation becomes available under documented priority | Different from merely reaching the fixture | TH-007 |
| Upper living key owner unaware and reachable | Take its matching key and use the secured route | Key authority transfers without requiring a kill | Owner predicate differs from lock predicate | TH-006/008 |
| Manor entered, loot below 700 or scepter missing | Reach return location | Expert's complete conjunction is not satisfied | Arrival alone cannot finish | TH-008 |
| Scepter plus sufficient other loot and no prohibited fatality | Operate exit gate and return to street | Complete mandatory mission conditions settle success | Whole mission has an explicit terminal | TH-001/008 |
| Prohibited human killed | Continue toward exit | No-kill eligibility remains violated | Not merely a lost optional bonus | TH-008 |
| Save available before a patrol crossing | Save, later load and choose another approach | Retained branch permits different continuation | Documentary manual history, not own reload | TH-010 |

## Strategic and experiential structure

- Local decision: exposure, floor noise, guard orientation, carried selection
  and draw interval determine which immediate intervention is eligible.
- Medium-term planning: reserve utility arrows, steal the right keys, choose
  sufficient valuables and keep return access and no-kill eligibility intact.
- Long-term structure: campaign finance and tool non-carryover are documented
  context, not a second mission or whole-campaign optimisation signature.
- Common heuristics: listen/lean before crossing, use carpet and shadow,
  prefer eligible nonlethal approaches, place discoverable bodies deliberately.
- Failure attribution: unavailable key, wrong selection, loud floor, awareness,
  draw fatigue, empty reserve, breath loss and prohibited kill differ causally.
- Player trust: objective sheet and current gem/loot help inspect conditions;
  neither a dark gem nor an authored map guarantees an unknown future route.
- Claim IDs: TH-002-TH-010.

## Replay and variation

- Patrol timing, light changes, selected supplies, taken valuables and placed
  bodies make later approaches differ; no procedural seed is established.
- Pickpocket, waiting, eligible blackjack and multiple reachable loot routes
  remain choices. No single five-water-arrow expenditure is required by rules.
- Manual reload can support another intervention; exact native file fidelity
  is unverified. Expert is fixed before entry, not changed within the mission.
- Replay motive: deliberate route/noise/stock tradeoffs and optional valuables,
  not an invented mandatory perfect score.
- Claim IDs: TH-001-TH-010.

## Adjacent systems and history

- Original Thief differs from Gold/modded/2014 products. No later lockpicks or
  rope/moss tools enter merely because they occur elsewhere in the campaign.
- Splinter Cell's carried-body boundary transfers, but its two-handed/sidearm
  exception does not describe this occupied carry and other-use rule.
- F.E.A.R.'s map-independent assignment disclosure transfers; an explored
  map or acquired exact-location plan does not automatically transfer.
- Light changes detection rather than harming or repelling the patrol as
  Resident Evil Requiem's fixed protective illumination does.
- Claim IDs: TH-001/004/007/009-TH-012.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-008, ACT-049, ACT-089, ACT-130, ACT-161, ACT-164, ACT-202, ACT-341, ACT-491, ACT-705, ACT-708 | No additional candidate IDs; scoped parameters above |
| System Behaviour | SYS-036, SYS-057, SYS-215, SYS-373, SYS-543, SYS-578, SYS-605, SYS-797, SYS-1450, SYS-1451, SYS-1452 | No additional candidate IDs; scoped parameters above |
| Constraint | CON-077, CON-198, CON-282, CON-285, CON-296, CON-335, CON-460, CON-773, CON-792, CON-793, CON-794 | No additional candidate IDs; scoped parameters above |
| Information | INF-073, INF-075, INF-115, INF-117, INF-316, INF-480, INF-498 | No additional candidate IDs; scoped parameters above |
| Objective | OBJ-291 | No additional candidate IDs; scoped parameters above |
| Time | TIM-003, TIM-007 | No additional candidate IDs; scoped parameters above |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `512` (`GAME-0001`–`GAME-0512`).
- Exact genome matches: none.
- Tied near matches: `GAME-0349` — Tom Clancy’s Splinter Cell (`20 / 50 = 0.400000`).
- Supported combination subsets: none.
- Scan date: 2026-10-06.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| GAME-0349 — Tom Clancy’s Splinter Cell | ACT-008, ACT-161, ACT-202, ACT-341, ACT-491, SYS-057, SYS-215, SYS-373, SYS-578, SYS-797, CON-077, CON-282, CON-285, CON-335, INF-073, INF-075, INF-115, INF-316, TIM-003, TIM-007 | Both use local perceptual stealth, eligible nonlethal contact and discoverable bodies. Sam’s training and police packet has keypad/interrogation, protected actors, checkpoint and successor retention; Thief has finite water-arrow light control, surface-generated noise, living-owner key theft, a mission-wide human no-kill predicate and independent scepter/700-loot street extraction. Neither carries the other’s full mission contract or map. | Tied near: 20 / 50 = 0.400000 |

### Preserved research notes

- New genes: ACT-708, SYS-1450/1451/1452, CON-792/793/794, INF-498, OBJ-291.
- Classification result: New gene.
- Evidence and reasoning: complete signatures and proper verified subsets,
  not franchise affinity or a copied visual motif (TH-011/012).

## Taxonomy impact

- Registry changes: nine Active additions and thirty-four unchanged transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_250](../../../research/taxonomy-changes/TAXONOMY_CHANGE_250.md).
- No earlier signature/definition, all-platform audit or r000024 mapping change.
- Claim IDs: TH-011/012.

## Negative results

- No structured global negative result. Secured loot bags, threshold-valued
  puzzle elements, sidearm-compatible carrying, persistent water surfaces,
  precise live map positions and automatic checkpoint restoration do not fit.
- Claim IDs: TH-003/004/007-TH-011.

## Delta summary

## New facts

- [Observation | Corroborated | High] Expert's complete conjunction and local
  perceptual/tool choices differ from a genre-only stealth label (TH-001-TH-009).
- [Observation | Limited | Medium] Original executable, quantitative animal
  and save/failure details remain explicit testing limits (TH-001/008/010).

## New genes

- [Observation | Corroborated | High] Utility draw, draw development, eligible
  extinction and floor-generated stimuli have distinct command/resolver roles.
- [Observation | Corroborated | High] Living-owner theft, occupied carry,
  prohibited human fatalities, partial orientation and quota extraction retain
  operational counterexamples (TH-006-TH-011).

## New combinations

- [Observation | Direct | High] All verified proper subsets are scanned;
  no motif-selected new combination is proposed (TH-012).

## Taxonomy changes

- [Observation | Direct | High] TAXONOMY_CHANGE_250 accepts nine additions
  without changing earlier English definitions or signatures (TH-011).

## New questions

- [Hypothesis | Limited | Medium] A controlled original-v1.33 installation
  could refine map updates, animal/failure, selection priority and saved-state
  fidelity without borrowing Gold or modification rules.

## Next recommended game

- [Observation | Direct | High] No next subject is authorised: this is the
  final GAME-0513 unit of the amended approved 18-game horizon.
- Optimisation criterion: complete 9 retro and 9 released modern targets,
  preserve one local accepted commit per game and stop after batch audit.
- Expected information gain: documented complete stealth mission, not a
  promised future taxonomy count.
- Backlog impact: no next research, push, public mapping/publication or deploy.

## Why this game

- [Hypothesis | Limited | Medium] The final original Windows slot tests whether
  perceptual stealth and nonlethal quota extraction can be represented without
  importing later tools or treating every available Action as executed.
