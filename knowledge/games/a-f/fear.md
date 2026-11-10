---
game_id: GAME-0501
slug: fear
game_title: F.E.A.R.
analysis_status: reviewed
reviewed: 2026-10-05
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-131
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-199
    - ACT-202
    - ACT-229
    - ACT-295
    - ACT-341
    - ACT-409
    - ACT-595
    - ACT-679
  system:
    - SYS-057
    - SYS-065
    - SYS-112
    - SYS-208
    - SYS-215
    - SYS-222
    - SYS-348
    - SYS-368
    - SYS-369
    - SYS-379
    - SYS-578
    - SYS-754
    - SYS-755
    - SYS-851
    - SYS-1271
    - SYS-1377
    - SYS-1378
    - SYS-1379
    - SYS-1380
  constraint:
    - CON-175
    - CON-210
    - CON-262
    - CON-282
    - CON-285
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-268
    - INF-479
    - INF-480
  objective:
    - OBJ-026
  time:
    - TIM-003
    - TIM-007
---

# Game: F.E.A.R. (2005)

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

This source-qualified original-rules reconstruction does not claim native play
or current-binary parity. Research acceptance is separate from full site and
exact-source acceptance in the unit checkpoint.

## Analysis scope

- Version / ruleset: original released English Windows base F.E.A.R. (2005),
  single-player campaign, Moderate difficulty, keyboard and mouse. Reconstruct
  the original rules from the publisher-hosted base booklet, the shipped-game
  developer paper and Lunadea's 2007 Moderate route. Steam application 21090
  identifies the currently lawful product destination but its storefront date
  of 2010 is not the original release date. No patch number, executable hash,
  native installation or current-binary parity was captured.
- Structured analysis target: original Windows base-release First Encounter
  packet; no console port, expansion, mod or multiplayer rules are imported.
  The structured platform entry must retain that exact target and limitation.
- Entry and exit: after a fresh ordinary campaign completes Interval 01, begin
  with personal control immediately after the helicopter rappel outside South
  River Wastewater Treatment Plant. Entry carries the ordinary AT-14 and RPL;
  prior eligible health-booster and supply decisions are recorded reproduction
  parameters, not an invented universal health value. Complete all of Interval
  02 Initiation: First Encounter: the initial gate, authored buildings and
  warehouse firefights, the crane crossing, final courtyard, basement and
  terminal window descent. Continue the terminal scene until the next ordinary
  control boundary in Interval 03 Escalation: Infiltration. Killing the first
  pair of soldiers or merely operating the crane does not complete the packet.
- Primary decision loop: inspect health, armour, magazine and reserve rounds,
  carried medkits, SlowMo readiness and local cover; move, crouch or lean to
  expose a useful firing line; choose aimed fire, melee, a finite grenade or
  short SlowMo use against reacting soldiers; reload, switch, swap, heal and
  collect supplies as appropriate; preserve survival through ordered switches,
  destructible route barriers and the relocated container to reach the terminal.
- Included: all material entry-to-terminal controls and support states,
  including aim magnification, manual and exhaustion-triggered reload, automatic
  next-weapon selection, dual AT-14 availability, holstering and directional
  body attacks, finite medkits, permanent health/reflex boosters, separately
  rechargeable personal light, partial enemy perception, qualified suppression
  and cover responses, local tutorial/mission information and permitted saving.
  Optional reachable boosters and supplies belong to this packet; they are not
  postponed simply because the fastest route can bypass them.
  Zero personal health is lethal and loading restores retained state rather
  than keeping the world after permanent death.
- Excluded: Interval 01 as an admitted route; all later intervals, expansion
  campaigns, sequels, console changes, multiplayer stations and respawn rules;
  later unavailable weapon classes, proximity mines, remote bombs, heavier
  enemies and unrelated advancement; cheats, imported saves and exact timings
  or damage formulas not established by the reviewed sources. Multiplayer
  refill/health stations do not establish campaign regeneration. No reinforcement
  spawn is inferred from a shouted request or complex coordinated pincer from
  the apparent final positions of ordinary cover-seeking soldiers.
- Reproduction: start a fresh released original Windows campaign on Moderate;
  record the Interval 01 retained supplies and maximum health. At the next
  control boundary, inspect the gate and take the optional low-shutter branch;
  operate its control, continue through every authored encounter, inspect at
  least one medkit, a second pistol, the assault rifle and both reachable health
  boosters, break the window boards and operate the crane before crossing its
  moved container. Observe the final courtyard and basement through the next
  interval boundary. Separately test manual/automatic reload, typed exhaustion,
  SlowMo cancellation/recovery, light off-state recovery, grenade fuse/contact,
  manual healing and save/load from retained snapshots. Exact amounts, rates,
  enemy paths and replay timings are parameters, not native measurements here.
- Potential scoped modules: one later named interval; one multiplayer ruleset;
  one expansion or a console variant needs its own reproducible packet and
  evidence. None is flattened into the present signature.
- Direct-play status: not conducted. The publisher-hosted combined PDF was
  read only for its base-game pages; the default-key chart was inspected as a
  rendered image. D1 is the original developer's shipped-game account, not a
  current executable trace. S1 is an attributed Moderate firsthand walkthrough,
  accessed through a text mirror; S2 and S5 corroborate the complete route
  without establishing capture patch or difficulty. S3 is Twiggymouse's
  firsthand qualitative booster account: full health refill is explicit, while
  immediate reflex refill is explicitly unknown. R1 is Zevik's original-PC recording, uploaded
  2009-05-09, declared Extreme without quicksaves: muted paused frames corroborate
  local affordances, not Moderate damage, hidden inputs, every failure branch,
  native timings or exact binary parity. No user window or system sound was
  changed and no media/source images will be distributed in this record.
  Contact medkit acquisition is reconstructed from S4's indexed secondary
  description and consistent R1 approach/stock credit; the full S4 article is
  blocked. This is Limited/Medium evidence, not a captured physical-input trace.
  M1 separately establishes manual healing and prompted weapon replacement.
  No audio was analysed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| FE-001 | Released identity: The original shipped 2005 Windows product is the target. Steam app 21090 currently reports its 2010 storefront date; that is not the original release date. | Observation | Direct | High | M1 Windows requirements; D1 p16; official Steam appdetails read 2026-10-05 |
| FE-002 | Complete packet: All of Interval 02 Initiation: First Encounter, from post-rappel control through the final window descent and Alma approach into Interval 03 Escalation: Infiltration; not the first two soldiers alone. | Observation | Corroborated | High | S1 §§7.2–7.3; S2 route; S5 complete terminal window and Alma approach |
| FE-003 | Weapons and melee: Direct shots, weapon-butt strikes, holstered punches and directional jump/slide kicks are distinct commands; aiming zoom and weapon selection do not themselves fire. | Observation | Direct | High | M1 base Arsenal and rendered key chart; S1 Controls |
| FE-004 | Inventory: Three weapon entries, or two pistols plus two other weapons, coexist with separate grenades; acquiring a second AT-14 permits dual wield. Medkit stock is capped at ten. | Observation | Direct | High | M1 base Arsenal/HUD; S1 First Encounter |
| FE-005 | Ammo exhaustion: An empty magazine reloads from compatible reserve; complete ammunition-type exhaustion selects another available carried weapon. Manual reload remains a separate request. | Observation | Direct | High | M1 base HUD Ammo and rendered key chart |
| FE-006 | SlowMo: Inactive SlowMo recharges; blue readiness permits activation while red requires waiting. Active use is finite and Reflex Boosters permanently extend the maximum duration. | Observation | Direct | High | M1 base HUD/Gear; S1 Controls and First Encounter |
| FE-007 | Light: A lit flashlight drains its own charge; automatic charge recovery occurs only while it is off, not while using SlowMo or standing at a multiplayer station. | Observation | Direct | High | M1 base HUD Flashlight |
| FE-008 | Health and armour: Zero health is lethal; manually spent medkits restore missing health. Armour reduces standard weapon fire but not explosive/environmental damage; no armour-first or split-fraction formula is asserted. | Observation | Direct | High | M1 base HUD/Gear; S1 Item List |
| FE-009 | Boosters: Health Boosters permanently raise maximum health and fully refill current health; Reflex Boosters enlarge maximum SlowMo. No immediate reflex refill, exact increments or final caps are asserted. | Observation | Corroborated | High | M1 base Gear; S1 Item List and scoped locations; S3 firsthand full-heal report and explicit reflex-refill uncertainty |
| FE-010 | Grenades: A thrown N6A3 follows a fuse but detonates immediately on enemy contact; the blast can injure anyone in range. Later mine/remote-bomb mechanics are outside this route. | Observation | Direct | High | M1 base Arsenal; S1 First Encounter pickups |
| FE-011 | Traversable progress: The gate switch opens the barrier; breakable boards expose the window route; the crane relocates a container to form a usable crossing before the final courtyard and basement. | Observation | Corroborated | High | S1 complete First Encounter; S2 route |
| FE-012 | Enemy responses: Perceived threats change local hostile plans. Eligible soldiers can coordinate suppression and distinct cover; incoming fire or grenades may invalidate cover and interrupt orders. | Observation | Direct | High | D1 pp1–3,13–16; S1 route encounters |
| FE-013 | Dialogue limit: Spoken reinforcement requests do not implement a reinforcement-spawn mechanism; the apparent complex flank can emerge from ordinary reachable cover choices. | Observation | Direct | High | D1 pp14–16 |
| FE-014 | Information: HUD exposes personal reserves, active weapon and relative crosshair precision; local sight/sound, contextual lean instruction and current Mission Status remain partial rather than an omniscient map. | Observation | Direct | High | M1 base HUD/rendered chart; D1 pp15–16; S1 First Encounter |
| FE-015 | Persistence: Esc pauses via the system menu; manual save/load and quicksave/quickload restore a retained world state. S1 marks authored checkpoints; retry is not world-retaining permadeath. | Observation | Direct | High | M1 base menus/rendered chart; S1 First Encounter checkpoint markers |
| FE-016 | Collection and input limits: Eligible medkits enter carried stock on contact before separate manual healing; weapon replacement remains a prompted Use action. Contact collection is a secondary reconstruction consistent with R1 approach and stock credit, not a captured physical-input trace. Exact item amounts are not native measurements. | Observation | Limited | Medium | M1 weapon swap and manual healing; R1 180–185; S4 explicit Medkit contact description retrieved through search index, full page blocked |

R1 frames at 30, 40, 44, 48, 60, 160, 180, 182, 185, 190,
195, 300 and 365 seconds were actually inspected. The ready HUD, initial
Reflex Booster acknowledgement, lean instruction and first medkit credit are
visible. A paused frame is not a record of the player's physical keypress.

## Basic data

- Release / origin: shipped in 2005; D1's original author explicitly dates it
  to that year. The current Steam catalogue date is separately reported above.
- Platform or physical form: original Windows personal single-player campaign,
  English base edition, Moderate reconstruction; PLAT-WINDOWS-PC.
- Puzzle family: real-time adversarial positioning with finite survival and
  ordered authored traversal, not an exhaustive psychological-horror product.
- Primary sources: M1 base booklet; D1 original shipped-game AI explanation;
  R1 attributed PC recording, qualified by its declared Extreme difficulty.
- Secondary sources: S1 attributed Moderate route and S2 independent illustrated
  route; their exact executable builds were not inspected.
- Claim IDs: FE-001–FE-016.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: `ACT-008`, `ACT-131`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-199`, `ACT-202`, `ACT-229`, `ACT-295`, `ACT-341`, `ACT-409`, `ACT-595`.
- Candidate genes: ACT-679 isolates the deliberate Aim/Zoom view command;
  aiming magnification is not a shot or a newly charged weapon-focus meter.
- Parameters: locomotion, crouch/lean, held weapon, target direction, attack
  member, magazine request, selected slot, N6A3 release, healing unit, optional
  fixture/phone interaction and illumination state. ACT-295 already covers
  holstered punches and directional kicks; no unarmed duplicate is proposed.
- Claim IDs: FE-003–FE-011, FE-014–FE-015.

### System Behaviour Genes

- Existing gene IDs: `SYS-057`, `SYS-065`, `SYS-112`, `SYS-208`, `SYS-215`, `SYS-222`, `SYS-348`, `SYS-368`, `SYS-369`, `SYS-379`, `SYS-578`, `SYS-754`, `SYS-755`, `SYS-851`, `SYS-1271`.
- Candidate genes: SYS-1377 full-refill health booster, SYS-1378 permanent
  SlowMo-duration extension, SYS-1379 typed total-ammunition exhaustion and
  SYS-1380 interruptible hostile suppression/distinct cover coordination.
- Resolution order: a legal shot resolves current line/body hit and compatible
  protection; zero health closes the attempt. The empty magazine either starts
  reserve reload or selects an available other weapon. N6A3 resolves its own
  collision/fuse and immediate enemy-contact exception. Active SlowMo and light
  consume independent reserves; eligible inactive states restore readiness.
  Gate operation changes persistent passage state and the crane starts its
  linked platform movement. Saved state can replace the failed continuation.
- Parameters: bullet-compatible armour, absent downed/revive phase, current
  health, finite stock, meter readiness, cover invalidation, weapon dispersion,
  grenade trigger and blast radius. No exact armour-before-health or fraction
  split is asserted. SYS-348 retains compatible layers; SYS-578 retains health.
- Claim IDs: FE-005–FE-013, FE-015–FE-016.

### Constraint Genes

- Existing gene IDs: `CON-175`, `CON-210`, `CON-262`, `CON-282`, `CON-285`.
- Candidate genes: none. Three weapon entries, the paired-pistol exception,
  bounded typed rounds and ten medkits remain capacity parameters, not new IDs.
- Scarce strategic resources: persistent health and standard-fire armour,
  loaded/reserve ammunition, grenades, carried medical stock, current SlowMo
  and light charge. Gate state, intact boards and container location constrain
  reachable continuations. Contact medkit acquisition is a Limited/Medium secondary reconstruction
  consistent with R1 stock credit, separately from prompted weapon replacement;
  it is not guessed from a generic instruction to collect an item.
- Claim IDs: FE-004–FE-011, FE-016.

### Information Genes

- Existing gene IDs: `INF-073`, `INF-115`, `INF-119`, `INF-268`.
- Candidate genes: INF-479 directly exposed weapon/posture/speed dispersion;
  INF-480 inspectable current requirements without a promised reward or map.
- Current personal and weapon state, local sight/sound, explicit lean teaching
  and current mission requirements are distinct information surfaces. Dialogue
  can explain a soldier's state without causing the proclaimed reinforcement.
  Smaller spread signals relative precision, not exact future hit probability.
- Claim IDs: FE-006–FE-014.

### Objective Genes

- Existing gene IDs: OBJ-026.
- Candidate genes: none.
- Success, evaluation and failure: reach the authored next-interval boundary
  alive after making its intervening route traversable; zero personal health
  is lethal and reloads a retained state. No score reward, competitive victory
  screen or permanent save deletion is invented.
- Claim IDs: FE-002, FE-008, FE-011, FE-015.

### Time Genes

- Existing gene IDs: TIM-003, TIM-007.
- Candidate genes: none.
- World movement, hostile responses, shots, reload downtime and two independent
  resource clocks remain live during input. SlowMo changes rate rather than
  turning combat into alternating turns; Esc pauses separately. Retained manual
  or automatic saves permit another continuation instead of universal rewind.
- Claim IDs: FE-005–FE-007, FE-012, FE-015.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Loaded rounds exhausted, compatible reserve positive | Continue firing until empty | Same ammunition reload starts; fire waits for readiness | Automatic reload is not new ammunition | FE-005 |
| Loaded and compatible reserve both empty; another carried weapon available | Exhaust current type | System selects next available weapon | Distinct from player selection and reserve reload | FE-005 |
| Ordinary weapon view | Invoke Aim/Zoom | Equipped magnified aiming view becomes active without a shot | Explicit command independent of the crosshair's dispersion signal | FE-003, FE-014 |
| One AT-14 carried and another reached | Accept the compatible weapon acquisition | Dual AT-14 becomes available within the paired-pistol slot exception | Weapon member and slot value are parameters | FE-004 |
| Injured and carrying medkits | Invoke Use Medkit | Spend carried medical stock to restore health | No passive health station is imported into single player | FE-008 |
| Low present health and eligible Health Booster | Acquire booster | Higher maximum and independently corroborated complete refill | Not SYS-417 increment-only recovery | FE-009 |
| Original SlowMo duration capacity | Acquire optional Reflex Booster | Maximum active duration permanently increases | No claim of an immediate measured meter fill | FE-006, FE-009 |
| Blue SlowMo readiness | Activate then cancel or exhaust | Finite active interval ends; inactive recovery becomes possible | Red/blue readiness is not a purchased charge | FE-006 |
| Light active with charge | Leave active, then turn off | Active drain stops and off-state recharge begins | Independent of SlowMo and medkits | FE-007 |
| Standard-fire armour positive | Receive compatible weapon fire versus an explosion | Standard-fire protection differs; explosion bypasses it | No universal armour-first rule | FE-008 |
| N6A3 airborne before fuse expiry | Contact an enemy rather than ordinary terrain | Immediate explosion on enemy contact | Enemy-contact exception inside existing grenade resolution | FE-010 |
| Window boards intact | Apply eligible strike/shot | Broken boards no longer block the route | Destroyed collision matters beyond decorative damage | FE-011 |
| Cargo crossing unavailable | Operate crane switch, then traverse stopped container | Authored cargo motion creates the usable crossing | Switch request, movement and actual arrival are separate | FE-011 |
| Soldier's cover invalidated and roles available | Apply pressure, then threaten new cover with grenade | Eligible suppression/reposition may be interrupted by danger | Conditional coordination, not a guaranteed pincer | FE-012 |
| Soldier calls for reinforcements | Continue the authored route | Later authored soldiers are not proved spawned by that line | Dialogue consequence must not be invented | FE-013 |
| Retained save precedes injury or changed position | Load it and choose another intervention | Saved world state replaces current continuation | Not world-retaining permadeath | FE-015 |

## Strategic and experiential structure

- Local decision: weigh visible line and exposed body against firing precision,
  magazine downtime, possible enemy cover responses and current ability time.
- Medium-term planning: preserve carried weapons, medical stock and health
  across rooms; choose optional booster branches and safely operate route gates.
- Long-term structure: the admitted target ends at the next interval, not at
  campaign victory or the later expansion endings.
- Common heuristics: a stationary lean can expose a shot without walking
  wholly past the doorway; finite SlowMo can create a reposition/reload window.
  These are possibilities, not always-optimal or always-safe policies.
- Failure attribution: local hits, empty rounds and current health are exposed;
  unseen soldier plans, damage numbers and authored visions are not omniscient.
- Player-trust factors: save/load permits alternative preparation; voiced plans
  need not describe implemented reinforcement or exact flank algorithms.
- Claim IDs: FE-002–FE-016.

## Replay and variation

- What changes between sessions: positions, attack/weapon choices, supplies,
  optional collection and reactive cover selection within authored geography.
- Randomness or procedural generation: no procedurally regenerated warehouse
  or independently measured random shot distribution is claimed.
- Multiple viable strategies: direct fire, crouched/leaned positions, limited
  grenades, SlowMo, weapon swaps and bodily attacks remain legal affordances.
- Typical replay motive: different survival and preparation decisions through
  the same complete packet; no claim about measured player preference.
- Claim IDs: FE-003–FE-015.

## Adjacent systems and history

- Direct predecessors: D1 explicitly compares perceived soldiers with Half-Life
  marines; this is attributed reception, not a proved universal design lineage.
- Variants: expansions, console changes and later intervals remain excluded.
- Similar games: only the selected complete-signature results below are narrated.
- Important differences: independent off-state light recovery, current SlowMo,
  manual carried healing, permanent boosters, automatic typed weapon fallback
  and qualified cover roles coexist inside one authored first-combat interval.
- Claim IDs: FE-001–FE-016.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| action | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-199`, `ACT-202`, `ACT-229`, `ACT-295`, `ACT-341`, `ACT-409`, `ACT-595`, `ACT-679` | Numeric quantities, body posture, weapon identity and level geometry remain parameters |
| system | `SYS-057`, `SYS-065`, `SYS-112`, `SYS-208`, `SYS-215`, `SYS-222`, `SYS-348`, `SYS-368`, `SYS-369`, `SYS-379`, `SYS-578`, `SYS-754`, `SYS-755`, `SYS-851`, `SYS-1271`, `SYS-1377`, `SYS-1378`, `SYS-1379`, `SYS-1380` | Numeric quantities, body posture, weapon identity and level geometry remain parameters |
| constraint | `CON-175`, `CON-210`, `CON-262`, `CON-282`, `CON-285` | Numeric quantities, body posture, weapon identity and level geometry remain parameters |
| information | `INF-073`, `INF-115`, `INF-119`, `INF-268`, `INF-479`, `INF-480` | Numeric quantities, body posture, weapon identity and level geometry remain parameters |
| objective | `OBJ-026` | Numeric quantities, body posture, weapon identity and level geometry remain parameters |
| time | `TIM-003`, `TIM-007` | Numeric quantities, body posture, weapon identity and level geometry remain parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `500` (`GAME-0001`–`GAME-0500`).
- Exact genome matches: none.
- Tied near matches: `GAME-0239` — Half-Life (1998) (`21 / 54 = 0.388889`); `GAME-0273` — Max Payne 3 (`21 / 54 = 0.388889`); `GAME-0340` — Halo: Combat Evolved Anniversary (`21 / 54 = 0.388889`).
- Supported combination subsets: none.
- Scan date: 2026-10-05.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| GAME-0239 Half-Life (1998) | Direct embodied weapon/traversal control, compatible inventory, live combat, visible personal resources, charged portable light, breakable route objects and checkpoint return | F.E.A.R. adds SlowMo, medkit stock, body attacks, permanent boosters, complete-ammo fallback, explicit aiming view and conditional hostile cover roles; Half-Life's scoped fixture supplies and route capabilities are not imported | Near, 0.388889 |
| GAME-0273 Max Payne 3 | Direct fire, manual reload, carried item/supply choices, SlowMo resource, local combat cues, contextual instruction and retry | F.E.A.R. retains first-person posture/lean, off-state light, armour compatibility, grenade contact exception, capacity boosters and distinct-cover enemy coordination; Max Payne 3's own dive, critical recovery and mission settlement remain separate | Near, 0.388889 |
| GAME-0340 Halo: Combat Evolved Anniversary | Direct first-person movement, posture, firearms, grenades, contact supplies, compatible layered survival, finite portable light, contextual instruction and checkpoint return | F.E.A.R. adds manual medkit stock, SlowMo, bodily attacks, permanent capacity boosts, complete-ammunition fallback and interruptible cover roles; Halo’s scoped regenerating shield, motion tracker, friendly relations and encounter-clear settlement remain separate | Near, 0.388889 |

- New genes: seven source-bounded operational distinctions.
- Classification result: New gene.
- Evidence and reasoning: full six-type signature comparison is unweighted;
  no genre, platform, artwork or salience affects the result. The final contact-collection boundary is included in the recomputed scan;
  its source-specific limitation remains in FE-016.

### Preserved research notes

- New genes: seven source-bounded operational distinctions.
- Classification result: New gene.
- Evidence and reasoning: full six-type signature comparison is unweighted;
  no genre, platform, artwork or salience affects the result. The final contact-collection boundary is included in the recomputed scan;
  its source-specific limitation remains in FE-016.

## Taxonomy impact

- Registry changes: ACT-679, SYS-1377–SYS-1380, INF-479–INF-480;
  no accepted earlier English definition or existing game signature changes.
- Taxonomy-change record: [TAXONOMY_CHANGE_238](../../../research/taxonomy-changes/TAXONOMY_CHANGE_238.md)
  owns the reviewed operational counterexamples and unchanged transfers.
- Candidate terms affected: none. Corpus-internal isolation is not external
  novelty and does not promote a hypothesis to a cross-family law.

## Negative results

- No separate negative-result record. Reject unsupported automatic reinforcement,
  universal armour absorption, campaign health stations, exact source-uncaptured
  damage/duration formulas and current-patch equivalence in this scoped ledger.

## Delta summary

Add the complete original Windows First Encounter reconstruction, forty
unchanged English transfers and seven bounded additions with paired Ukrainian
copy. No earlier game signature or English definition changes. Full integration
acceptance remains in the unit checkpoint; no push or publication is implied.

## New facts

- [Observation | Direct | High] FE-005 distinguishes reserve reload from complete
  typed-ammunition fallback; FE-007 requires off-state light recovery.
- [Observation | Direct | High] FE-013 keeps reinforcement speech separate from
  the shipped AI's actual mechanisms.

## New genes

- ACT-679, SYS-1377–SYS-1380 and INF-479–INF-480 with paired Ukrainian
  definitions, inclusion/exclusion boundaries and reviewed causal presentation.

## New combinations

- None.

## Taxonomy changes

- TAXONOMY_CHANGE_238 separates aiming view, permanent capacities, complete
  ammunition fallback, conditional hostile roles and current information.

## Negative findings

- No unauthorised binary, screenshot redistribution, native play or current
  build identity is claimed.

## Sources and reproduction boundary

- M1: publisher-hosted [combined F.E.A.R. booklet](https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/21090/manuals/FEAR_combined.pdf?t=1681232225),
  checked 2026-10-05. Base menus, HUD, arsenal, gear and rendered default controls
  only; expansion pages are excluded. Local read-only source SHA-256:
  b3cc6149837a4c41e2c3e2ec48b2b4e2f63eb4998af4eadedd92b64dac9cf67a.
- D1: Jeff Orkin, Monolith/MIT, [Three States and a Plan: The A.I. of F.E.A.R.](https://madwomb.com/tutorials/gamedesign/prototyping/gdc2006_JeffOrkin_AI_FEAR.pdf),
  Game Developers Conference 2006, pp1–3 and13–16; author-primary paper reached
  through an attributed mirror, checked 2026-10-05. SHA-256:
  313546d083d3d243e61839af489d0fd0476162309a93740eb0f01d2c73ec01d8.
- S1: Lunadea, [PC guide original listing](https://gamefaqs.gamespot.com/pc/920744-fear/faqs/51186),
  v1.1 dated 2007-12-26, read via the
  [attributed text mirror](https://www.cheatbook.de/wfiles/feard.htm).
  Complete First Encounter and its adjacent entry/exit, controls, tips and
  scoped item/weapon descriptions were actually read. Moderate declared; native
  build unspecified. Author credits bob3739 for booster locations, which must
  not be counted as independent corroboration. No guide text is redistributed.
- S3: Twiggymouse, [firsthand original F.E.A.R. playthrough notes](https://www.lp.zone/t/lets-first-encounter-assault-and-recon-in-f-e-a-r-first-encounter-assault-recon/2287),
  opened 2026-10-05, original post dated 2017-08-02. Health/reflex/medkit
  descriptions actually read: full health refill is explicit; immediate reflex
  refill is explicitly unknown. No console, binary or exact numerical parity
  is inferred from these qualitative observations.
- S4: [community Medkit description](https://fear.fandom.com/wiki/Medkit),
  retrieved through its indexed description on 2026-10-05. It explicitly states
  contact transfer into inventory and separate manual use; full article access
  is blocked. This is secondary Limited/Medium evidence, not primary input
  capture; R1 shelf approach and later stock credit are consistent but cannot
  alone exclude a hidden keypress. No unsupported input is claimed for every
  other supply class.
- S5: [independent complete First Encounter route](https://www.gamepressure.com/firstencounterassaultrecon/interval-02-first-encounter/zbd7),
  updated 2016-05-11, checked 2026-10-05. Full route text through the second
  booster, terminal window and dangerous Alma approach was read; exact build
  and difficulty remain unknown. It corroborates the terminal rather than
  replacing M1 or D1 as primary mechanical evidence.
- S2: [First Encounter illustrated route](https://portforward.com/games/walkthroughs/F.E.A.R/Interval-02-Initiation.htm),
  page dated 2016-09-12 and updated 2021-09-15; route HTML actually read,
  checked 2026-10-05. Unknown difficulty and capture build; terminal window is
  corroborated, but this is not sole evidence for every gameplay rule.
- R1: Zevik, [original PC First Encounter part 1](https://www.youtube.com/watch?v=vSrCC9dOdEQ),
  uploaded 2009-05-09, 420-second recording, Extreme without quicksaves declared.
  The named paused frames were inspected in an isolated headless Chrome process
  with media forced muted before playback. Hidden inputs, exact binary and
  Moderate quantitative parity remain unverified.
- P1: [official Steam product](https://store.steampowered.com/app/21090/FEAR/)
  and Valve appdetails, checked 2026-10-05; product name, released status, Windows
  support and storefront date were read. Current entitlement, installation,
  licence ownership and original patch parity were not tested.
