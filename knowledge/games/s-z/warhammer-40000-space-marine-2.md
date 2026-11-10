---
game_id: GAME-0496
slug: warhammer-40000-space-marine-2
game_title: "Warhammer 40,000: Space Marine 2"
analysis_status: reviewed
reviewed: 2026-10-04
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-223
    - ACT-341
    - ACT-419
    - ACT-425
    - ACT-494
    - ACT-669
  system:
    - SYS-045
    - SYS-051
    - SYS-215
    - SYS-292
    - SYS-359
    - SYS-369
    - SYS-578
    - SYS-655
    - SYS-736
    - SYS-749
    - SYS-755
    - SYS-778
    - SYS-779
    - SYS-832
    - SYS-836
    - SYS-913
    - SYS-1339
    - SYS-1340
    - SYS-1341
    - SYS-1342
    - SYS-1343
    - SYS-1344
  constraint:
    - CON-282
    - CON-331
    - CON-589
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-268
    - INF-295
    - INF-319
    - INF-372
  objective:
    - OBJ-284
  time:
    - TIM-003
---

# Game: Warhammer 40,000: Space Marine 2 — complete solo Rain of Terror

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Inputs, armour segments, counters and durations parameterise boundaries, not IDs.

## Analysis scope

- Version / ruleset: English Windows Steam base Campaign, Normal, complete
  solo `Rain of Terror` prologue, reconstructed for publisher patch 3.0,
  dated 2024-09-26. Earlier written route/control observations are combined
  with that explicit patch delta, not silently treated as current 2026 rules.
  No installed executable, Steam Build ID, controller trace, native save or
  exact later-patch parity was inspected.
- Structured analysis target: existing `PLAT-WINDOWS-PC`, authorised Steam
  application `2183900`. Other platform releases remain unassessed.
- Primary decision loop: read threats, attack category, tutorial/objective
  cues, ammunition, armour and recoverable health; reposition, sprint, lock
  an opponent, combine light/heavy chainsword attacks, aim/fire, reload,
  switch firearm, dodge or parry; use a marked Gun Strike or approach a
  staggered target for execution; replenish supplies, use eligible scenery
  and operate the ordered bomb/door/console route while combat remains live.
- Entry and exit: choose fresh solo Normal Campaign and start at first
  control after the Deathwatch landing crash. Include the complete lesson and
  jungle/facility route, weapon acquisition, virus-bomb collection/loading,
  lift and launch controls, charging holdout and final scripted encounter.
  Exit only after the forced injury and Primaris transition into first
  retained Battle Barge control. Launching alone is not the terminal;
  defeating the final Carnifex is not required.
- Included: every documented local combat/traversal option in this route,
  pistol then rifle, frag grenades, finite magazines and compatible resupply;
  hostile motion and attacks, timed defence, stagger, execution and Gun
  Strike; damage-first armour, delayed quiet refill, direct finisher credit,
  recoverable-health creation/recovery/expiry and reported incoming erosion;
  interactive barriers/plants/doors, explosive scenery, tutorial predicates,
  authored finite groups, route gates and threshold rather than total-clear
  launch eligibility; ordinary failure/retry and the distinct final forced
  story-loss segment.
- Excluded: later `Skyfire` play, Righteous Fury, jump pack, later weapon
  pods, Medicae Stimms and squad revival first described on later routes;
  Operations classes/perks, armour-data economy, Eternal War, Sparring Arena,
  collectibles/achievement optimisation, cosmetics and whole Campaign;
  speedrun/exploit outcomes, exact damage/decay/recharge/holdout constants,
  random spawn distributions, later patch mechanics and console parity.
  A general product control or perk does not prove availability in the solo
  prologue. Non-causal social annotation is outside the decision packet.
- Potential scoped modules: first ordinary squad mission, one Operations
  loadout/mission, an independently executed patch/save comparison and
  collectible/marking objectives need separate entries and terminals.
- Direct-play status: not conducted. Official product and patch text,
  dated independent written combat accounts and complete written prologue
  routes were inspected. Game8 and Neoseeker route text was available through
  indexed search results; direct requests returned 402/403 and were not
  bypassed. Later route corroboration does not certify a native build.
  No game, executable, save, screenshot, video or audio was executed or
  analysed. Generated artwork is not evidence.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| SM2-001 | The 2024 Saber/Focus Windows product separates Campaign from Operations and Eternal War | Confirmed | Direct | High | P1, P2 |
| SM2-002 | Patch 3.0 fixes healing above contested health; Operations parry changes must not be silently imported into Campaign | Observation | Direct | High | P3 |
| SM2-003 | The complete solo prologue includes teaching, weapon acquisition, bomb/facility route, holdout, launch and a scripted successor transition | Observation | Corroborated | Medium | S1, S2, S3 |
| SM2-004 | Live aimed fire, reload, light/heavy melee, lock-on, parry/dodge and frag use offer distinct responses | Observation | Corroborated | Medium | S1, S2, S4, S5 |
| SM2-005 | Eligible perfect defence or heavy displacement exposes Gun Strike; an executable stagger instead permits a close finisher | Observation | Corroborated | High | S1, S4, S5 |
| SM2-006 | Executions credit armour directly and protect their animation; Gun Strike does not grant that same protection | Observation | Corroborated | High | S4, S5; P4 for deliberate Gun Strike exposure |
| SM2-007 | Health loss creates a recoverable bank; attacking restores it, time expires it and later incoming hits reportedly erode it | Observation | Limited | Medium | S5, S6; P3 for corrected cap |
| SM2-008 | Defeating a synaptic Warrior can kill nearby dependent lesser Tyranids, not every enemy in the arena | Observation | Limited | Medium | S5 |
| SM2-009 | Renewable armour refills after quiet without passively refilling lost underlying health | Observation | Corroborated | Medium | S3, S7 |
| SM2-010 | Charging survival releases launch interaction without requiring every remaining hostile to die; final injury is scripted, not a required boss kill | Observation | Corroborated | Medium | S1, S3 |
| SM2-011 | Tutorial predicates, compatible supplies and interaction gates organise progression | Observation | Corroborated | Medium | S1, S2, S3 |
| SM2-013 | Ordinary Campaign lethal failure returns to a checkpoint; transfer to solo prologue does not establish exact saved resource fields | Observation | Limited | Medium | S8 |
| SM2-012 | No native execution or numerical/patch-parity verification was performed | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Saber Interactive / Focus Entertainment, September 2024.
- Platform or physical form: English Windows Steam; dated 3.0 reconstruction.
- Puzzle family: tactical counterplay, real-time pressure, inventory/fixture
  dependencies and ordered progression. Existing families only.
- Official sources, accessed 2026-10-04:
  - **P1:** [Publisher overview](https://www.focus-entmt.com/en/news/warhammer-40000-space-marine-2-shows-off-its-intense-combat-and-mechanics-in-todays-overview-trailer),
    2024-06-20; product identity and mode separation, not viewed trailer evidence.
  - **P2:** [Steam product](https://store.steampowered.com/app/2183900/Warhammer_40000_Space_Marine_2/),
    lawful Windows distribution.
  - **P3:** [Publisher patch 3.0](https://community.focus-entmt.com/focus-entertainment/space-marine-2/blogs/90-space-marine-2-patch-3),
    2024-09-26; general healing/AI changes and explicitly separated mode deltas.
  - **P4:** [Developer community Q&A](https://community.focus-entmt.com/focus-entertainment/space-marine-2/blogs/84-frequently-asked-questions),
    initially published 2024-09-18; explicit risk/reward reason for no Gun
    Strike invulnerability and right-hand melee/left-hand pistol animations.
    Later annotated updates on the page do not certify launch-patch parity.
- Written observation sources, accessed 2026-10-04:
  - **S1:** [Game8 Rain of Terror](https://game8.co/games/Warhammer-40000-Space-Marine-2/archives/473163),
    updated 2024-09-13, indexed written route and tutorial/terminal conditions.
  - **S2:** [Neoseeker Rain of Terror](https://www.neoseeker.com/warhammer-40000-space-marine-2/walkthrough/Operation_Rain_of_Terror),
    indexed Normal reference route, controls, acquisition and supply distinctions.
  - **S3:** [VGTimes complete campaign route](https://vgtimes.com/guides/113467-complete-walkthrough-of-warhammer-40000-space-marine-2.html),
    2024-10-09 / 2024-11-08; prologue, rifle and successor sections only.
    Its broad healing sentence is not authority for automatic lost-health refill.
  - **S4:** [NoobFeed timed defence and finishers](https://www.noobfeed.com/articles/warhammer-40000-space-marine-2-how-to-parry-counter-gun-strike-and-execute-finishers),
    2024-09-08; qualitative legal responses, not its inconsistent mouse labels.
  - **S5:** [GameSpot launch combat tips](https://www.gamespot.com/gallery/11-space-marine-2-tips-to-help-you-bring-glory-to-the-emperor/2900-5755/),
    2024-09-06; combat sustain, dependent lesser enemies and environmental effects.
  - **S6:** [Parz1vol's dated player report](https://community.focus-entmt.com/focus-entertainment/space-marine-2/forums/6-general/threads/44489-the-melta-bug-contested-health-and-difficulty),
    2024-09-20, indexed text; qualitative bank erosion/recovery only.
    Proposed balance changes and Operations expertise are not accepted rules.
  - **S7:** [Windows Central product/combat account](https://www.windowscentral.com/gaming/xbox/warhammer-40000-space-marine-2-faq-gameplay-trailers-everything-you-need-to-know),
    initially published 2023-10-17 and subsequently updated pre-launch;
    regenerative outer protection only, not its mode-mixing or numerical claims.
  - **S8:** [Gamer Guides Campaign difficulty](https://www.gamerguides.com/warhammer-40000-space-marine-2/guide/campaign/difficulty/campaign-difficulty-modes),
    2024-09-03 guide / 2024-10-01 update; lethal failure/checkpoint retry,
    transferred with Limited/Medium confidence to the solo prologue. Exact
    checkpoint locations and restored supply/world fields are not asserted.
- **R1:** this source-limited reconstruction and repository verification record.
- Claim IDs: SM2-001–SM2-013.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008/161/164/183/184`: embodied motion, aimed firearm or
  chainsword strikes including light/heavy sequence parameters,
  active weapon selection, magazine reload and carried frag throw.
- Existing `ACT-223/425/494`: timed dodge,
  timed weapon parry and retained opponent focus. No worn-knife
  requirement is imported with the parry command.
- Existing `ACT-341/419`: local fixture interaction and prompted close
  execution. Neither describes a marked shot from outside execution reach.
- New `ACT-669`: commit the exposed target-directed Gun Strike through the
  ordinary fire input rather than freely aim that particular contextual shot.
- Parameters: input mapping, range, chainsword sequence, guard timing,
  magazine size and firearm identity. No frame or ammunition-cost claim for
  Gun Strike is necessary to admit its distinct target-directed command.
  `ACT-295` excludes equipped tools; it is not additionally admitted for
  the same chainsword command already covered by `ACT-161`.
- Claim IDs: SM2-004–SM2-006, SM2-011.

### System Behaviour Genes

- Existing `SYS-045/051/215/292/359`: hostile motion/engagement, live hit
  resolution, grenade field and eligible timed defensive adjudication.
- Existing `SYS-369/578/655/913`: ordinary checkpoint return, underlying
  health, armour-first damage and quiet restoration of renewable outer
  protection. The last transfer is operational shield equivalence, not armour
  durability, item repair, Overshield or passive health regeneration.
- Existing `SYS-736/749/755`: staged teaching predicates, finite authored
  releases and eligible damaged scenery/barrier settlement.
- Existing `SYS-778/779/832/836`: temporary living stagger, survival-threshold
  release, recoverable loss/outgoing recovery and independently reported
  incoming bank erosion. Erosion quantity remains unmeasured.
- New `SYS-1339`: declared contextual defeat credits outer protection directly.
- New `SYS-1340`: delayed expiry consumes the remaining bank, with protected
  execution suspension; unlike `SYS-852`, it does not discard the old bank
  wholesale before registering another loss.
- New `SYS-1341`: a slain synaptic carrier propagates a defeat response to
  eligible nearby dependent lesser enemies.
- New `SYS-1342`: an accepted close-execution animation suppresses compatible
  incoming damage; that protection is not promised for Gun Strike or afterward.
- New `SYS-1343`: the final playable forced-loss scene replaces ordinary
  lethal defeat with its authored injury/successor transition.
- New `SYS-1344`: a compatible local source replenishes bounded carried
  weapon/supply state by interaction, with finite versus renewable source
  availability separate from carried capacity.
- Resolution order: evaluate command/target eligibility, resolve live contacts
  and defence, update damaged layers/bank/stagger, then declared defeat
  credits/dependent response and progression predicates. This is the causal
  decomposition, not a recovered engine event order.
- Claim IDs: SM2-004–SM2-011.

### Constraint Genes

- Existing `CON-282/331/589`: ordered mission prerequisites, compatible
  class/magazine/reserve limits and live reachable execution eligibility.
- Rejected `CON-594`: its disabled-durability prerequisite is not evidenced
  for this chainsword. Unparryable categories remain in timed defence and cue
  parameters rather than a fictional knife-wear reserve.
- Claim IDs: SM2-004, SM2-005, SM2-011.

### Information Genes

- Existing `INF-073/115/119/125/268/295/319/372`: active equipment and stocks,
  partial local threats, health/protection/bank, current authored objectives,
  tutorial progress, executable stagger, legal attack-category cues and
  currently exposed contextual mark/action. No complete future map is inferred.
- Claim IDs: SM2-004–SM2-011.

### Objective Genes

- New `OBJ-284`: complete bomb acquisition/loading and eligible launch,
  then retain successor control beyond the forced injury. It is not merely
  arrival `OBJ-026`, charge planting `OBJ-100` or Carnifex elimination.
- Success, evaluation and failure: satisfy the full ordered terminal above.
  Ordinary lethal failure restores the latest checkpoint; post-launch
  scripted loss is progression, not failure. No save/relaunch equality claim.
- Claim IDs: SM2-003, SM2-010, SM2-011.

### Time Genes

- Existing `TIM-003`: continuous live combat; solo pause and local animation
  suspension are parameters. Teaching counters and charging duration are not
  new time genes. No exact timer is guessed.
- Claim IDs: SM2-004–SM2-011.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Required lesson predicate incomplete | Perform its eligible light, heavy, parry or marked-shot response | Corresponding counter advances toward its own threshold | Teaching gates are distinct from ordinary enemy clearance | SM2-003, SM2-011 |
| Eligible incoming close strike | Time a parry; instead dodge an unparryable red/orange strike | Accepted defence avoids its hit; incorrect response does not acquire a perfect counter | Category and timing both matter; unmarked ordinary attacks can still be parried | SM2-004, SM2-005 |
| Marked target after eligible defence/displacement | Press fire without ordinary aiming | Contextual directed shot resolves against the exposed target | Gun Strike is not a close execution or arbitrary manual shot | SM2-005 |
| Live enemy in executable stagger and reach | Commit execution | Defeat, direct armour credit and animation protection; remaining bank can recover | No world healing-drop pickup or Gun Strike immunity follows | SM2-006, SM2-007 |
| Recoverable bank remains positive | Attack before expiry; alternatively receive another eligible hit | Outgoing recovery consumes bank; incoming erosion is a separate reported transition | Not replacement of the entire earlier bank; no numerical fraction asserted | SM2-007 |
| Synaptic Warrior with nearby eligible lesser dependants | Defeat that Warrior | Local dependent response can kill those lesser enemies | Not universal room clearance | SM2-008 |
| Armour depleted, permanent underlying loss | Remain free from new damage | Renewable outer protection begins refill after delay, underlying loss remains | Quiet is not a full health item | SM2-009 |
| Missing ammunition beside compatible source | Interact, then fire/reload | Source replenishes accepted capacity; loaded/reserve scarcity still applies afterward | Renewable cache is not unlimited carried ammunition | SM2-011 |
| Bomb installed and charging encounter active | Survive, then use newly eligible launch control | Launch can advance with enemies remaining | Threshold release is not a kill-all gate | SM2-010 |
| Launch complete, final live story-loss segment active | Continue fighting until its authored transition | Injury/cutscene and successor control settle without required boss kill | Ordinary zero-health failure is overridden only in that declared phase | SM2-010 |

These are sourced qualitative test cases, not a claimed native replay.

## Strategic and experiential structure

- Local decision: defend, finish or retreat according to geometry and current
  bank; a distant Gun Strike trades execution reach/protection for a different
  exposed command.
- Medium-term planning: retain ammunition and a dodge lane while supplying the
  required bomb/console chain; do not confuse every fight with the holdout.
- Long-term structure: only this complete onboarding packet is analysed.
- Common heuristics: prioritise current legal cues over remembered colours;
  close execution can sustain protection but does not recover arbitrary lost
  health; finish dependencies near the carrier when the local opportunity fits.
- Failure attribution: mistimed defence, blocked retreat, wasted finite stock
  and missed launch authority are different from a mandatory story injury.
- Player-trust factors: visible prompts distinguish legal responses; source
  limits and post-launch progression are disclosed.
- Claim IDs: SM2-003–SM2-011.

## Replay and variation

- What changes between sessions: positioning, contacts, timing and expenditures.
- Randomness or procedural generation: no seed, probability or fixed random
  wave roster is established.
- Multiple viable strategies: ordinary ranged/melee/defensive choices remain;
  mandatory teaching and bomb predicates still apply.
- Typical replay motive: practise the complete tutorial, not farm a purported
  Operations economy.
- Claim IDs: SM2-003–SM2-011.

## Adjacent systems and history

- Direct predecessors: 2011 Space Marine is not admitted through sequel branding.
- Variants: later Campaign patches, co-op and other product modes require their
  own scope; source disagreement is not patched with a mode-specific perk.
- Similar games: shared typed boundaries may compare this route with existing
  live combat carriers; only the recomputed selected results are interpreted.
- Important differences: direct protection credit is not DOOM's spawned drops;
  recoverable-bank erosion is not Dead Cells' replacement rule.
- Claim IDs: SM2-001–SM2-011.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-008, ACT-161, ACT-164, ACT-183, ACT-184, ACT-223, ACT-341, ACT-419, ACT-425, ACT-494, ACT-669 | Mapping, range, sequence |
| System Behaviour | SYS-045, SYS-051, SYS-215, SYS-292, SYS-359, SYS-369, SYS-578, SYS-655, SYS-736, SYS-749, SYS-755, SYS-778, SYS-779, SYS-832, SYS-836, SYS-913, SYS-1339, SYS-1340, SYS-1341, SYS-1342, SYS-1343, SYS-1344 | Capacities, quantities, windows |
| Constraint | CON-282, CON-331, CON-589 | Prior flags, reach, stocks |
| Information | INF-073, INF-115, INF-119, INF-125, INF-268, INF-295, INF-319, INF-372 | Prompts and categories |
| Objective | OBJ-284 | Full launch and successor contract |
| Time | TIM-003 | Live input and scoped pause |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `495` (`GAME-0001`–`GAME-0495`).
- Exact genome matches: none.
- Tied near matches: `GAME-0245` — DOOM (2016) (`18 / 51 = 0.352941`).
- Supported combination subsets: none.
- Scan date: 2026-10-04.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0245` DOOM (2016) | `ACT-008/161/164/341/419`, `SYS-215/369/578/655/749`, `CON-282/589`, `INF-073/115/119/125/295`, `TIM-003`: 18 shared live movement/tool/firearm, prompted-finisher, damage/health, finite-release, route and current-feedback boundaries | DOOM's scoped UAC finisher spawns world health/ammunition and its arena requires full clearance; this prologue directly credits armour, restores only remaining contested health, distinguishes exposed Gun Strike from protected execution, permits threshold launch with remaining hostiles and requires a forced-injury successor rather than boss elimination. Reload, timed defence, local synaptic dependence and the bomb contract are not inferred for DOOM. | Near, `0.352941` |

### Preserved research notes

- New genes: ACT-669, SYS-1339–SYS-1344, OBJ-284.
- Classification result: New gene.
- Evidence and reasoning: individual causal command, recovery and terminal
  distinctions remain separate; no franchise-wide novelty claim.

## Taxonomy impact

- Registry changes: eight new boundaries; no earlier signatures change.
- Taxonomy-change record: [Taxonomy Change 233](../../../research/taxonomy-changes/TAXONOMY_CHANGE_233.md).
- Candidate terms affected: none; proposals are not promoted from similarity.

## Negative results

No exact build hash, damage formula, decay duration, recharge interval,
Gun Strike ammunition cost, universal parry colour requirement, room-wide
synaptic kill, finisher resource drop, unlimited carried ammunition,
post-animation immunity, required final boss defeat or current-patch parity.

## Delta summary

This unit reconstructs one complete dated solo prologue; roles and artwork
do not establish extra research evidence.

## New facts

- [Observation | Corroborated | Medium] Launch eligibility and scripted final
  injury have different terminals from ordinary clearance and lethal retry.

## New genes

- ACT-669; SYS-1339–SYS-1344; OBJ-284.

## New combinations

- None without independently supported recurring subsets.

## Taxonomy changes

- [Observation | Corroborated | Medium] Eight explicit boundaries and
  thirty-eight unchanged transfers are recorded in
  [TAXONOMY_CHANGE_233](../../../research/taxonomy-changes/TAXONOMY_CHANGE_233.md).

## New questions

- Independently execute a declared patch/save route to verify contested-bank
  erosion, exact checkpoint rollback and the forced-loss terminal.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0497 Wario Land 4, original Game Boy Advance.
- Optimisation criterion: approved mixed-era horizon, different decision structure.
- Expected information gain: timed return and transformation rules rather than live firearms.
- Backlog impact: one complete second unit, not implicit franchise coverage.

## Why this game

- [Hypothesis | Limited | Medium] Approved modern Windows entry complements
  the following retro handheld target without a run of identical genres.

## Resemblances to known games

- Only selected neighbours from the complete canonical comparison are interpreted.

## Updated hypotheses

- No cross-family hypothesis is promoted.

## Next research subject

- GAME-0497 Wario Land 4, original Game Boy Advance.
