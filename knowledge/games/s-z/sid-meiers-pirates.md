---
game_id: GAME-0487
slug: sid-meiers-pirates
game_title: Sid Meier's Pirates!
analysis_status: reviewed
reviewed: 2026-10-03
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-215
    - ACT-655
    - ACT-656
    - ACT-657
    - ACT-658
    - ACT-659
    - ACT-660
  system:
    - SYS-004
    - SYS-037
    - SYS-215
    - SYS-1290
    - SYS-1291
    - SYS-1292
    - SYS-1293
    - SYS-1294
    - SYS-1295
    - SYS-1296
    - SYS-1297
    - SYS-1298
    - SYS-1299
  constraint:
    - CON-285
    - CON-754
    - CON-755
  information:
    - INF-463
    - INF-464
  objective:
    - OBJ-029
  time:
    - TIM-002
    - TIM-003
    - TIM-032
---

# Game: Sid Meier's Pirates! (2004 Windows)

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: the original 2004 Windows product's ordinary single-player sea encounter, documented by the publisher-distributed PC booklet dated June 2005. This is not the 1987 game, Pirates! Gold or a console/mobile port. The later Steam listing is a legal product destination, not proof of launch-executable or patch parity.
- Structured analysis target: existing `PLAT-WINDOWS-PC`; matching `GAME-0487` entry in `knowledge/platforms/games.json`. No new platform or cross-release parity is claimed.
- Primary decision loop: steer a wind- and condition-sensitive flagship, select canvas and available ammunition, then choose when to discharge a legal loaded broadside or close for boarding. Preserve capture value while managing damage and reload exposure; if boarding occurs, match live sword attacks and counters while reciprocal crew/initiative pressure changes tempo, then settle the complete encounter and eligible prize choices.
- Entry and exit: enter at first sea-combat control after confirming an attack on one ordinary unescorted national merchant. Use Apprentice, 1660 and a young Fencing-skilled captain. Record an actual original-game battle autosave and its declared flagship type, hull/sails, crew, guns, ordnance/upgrades, starting heading/wind, target condition, morale, existing specialists/items, fleet count and national/local relations. Fleet support and equipped ammunition are declared parameters, not inferred universal initial values. Finish at returned Navigation after a draw or victory and prize settlement, or at the recorded transition into marooning/captivity after defeat. No complete native save or successful input trace was inspected; this is a source-reproducible state contract, not a measured opening battle.
- Included: the complete sea battle and eligible boarding branch, all supplied shot types, partial automatic reload, sail state, damage, floating crew/barrels, sword preparation, three attacks and three defences, taunt, advantage/disorientation, automatic crew losses, stage and next-hit surrender, prize asset choice, fleet admission and defeat/world-opinion settlement. A full fleet's keep-vessel rejection and a missing ordnance type remain real declared-state branches. Specialist acquisition is included; later repairs or other specialist services are not executed inside this packet.
- Excluded: selecting a campaign route or initiating additional encounters, trade, port recruitment/repairs/upgrades, land battles, dancing, stealth, quests, treasure expeditions, changing flagships outside the encounter, campaign profit division, retirement scoring and playing out subsequent prison escape or rescue. Standard overhead presentation is fixed for this packet; alternative non-rule-bearing chase/zoom rendering is not silently equated with a cockpit control or admitted as a topology-changing action. This does not remove any combat outcome or ammunition/boarding choice.
- Exceptions and limits: an undermanned ship can still move/fire slowly. Every gun need not reload before firing. Raking means hitting the target's bow/stern, not firing from one's own bow/stern. Ammunition favours a component but permits collateral harm. Sail destruction may yield surrender on approach, not unconditional immediate capture. One remaining crewman requires the next received captain hit to force surrender. Nightfall might draw, not an asserted universal fixed deadline. Exact initial counts, native timing, attack precedence, damage/casualty probabilities, cargo-transfer capacity calculation and loss fractions are unmeasured; do not infer them from decorative artwork or a Max Cargo table.
- Potential scoped modules: escorted multi-ship encounters, special quest captains, campaign economy and sea travel require their complete packets. Native play can settle exact save, timing, cargo admission, simultaneous-outcome precedence and patch parity before strengthening the corresponding limits.
- Direct-play status: no executable, disc, save, emulator, game audiovisual or input trace was run or inspected. Relevant full naval and boarding booklet sections were read; the sea/duel diagrams were visually inspected. Manual rules are source-reported observations, not measured successful play. The artwork is an original possible encounter, not a screenshot or exact starting state.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| PIR-001 | Wind heading, hull/rig, full or reefed canvas, damage and manning affect steering response; undermanning degrades rather than forbids motion. | Observation | Direct | Medium | P1 19–20, 32, 34, 106–107 |
| PIR-002 | Fire uses loaded side guns toward an eligible nearest target, at most half the installed guns; crew-sensitive automatic reload permits partial readiness. | Observation | Direct | High | P1 32–33 |
| PIR-003 | Available round, chain and grape differ in reach and favoured impact; absent ordnance is not freely selectable. | Observation | Direct | High | P1 33–34, 108 |
| PIR-004 | Hits can affect hull, sails, crew or guns; raking increases harm, depleted components alter operation and zero hull sinks. | Observation | Direct | High | P1 33–35 |
| PIR-005 | Vessel contact initiates boarding, sword selection and coupled captain/automatic crew combat. | Observation | Direct | High | P1 35, 40–41 |
| PIR-006 | Typed attack/counter and sword tempo determine pushback; matching duck/jump or thrust parry avoid hits, while other parries leave one step. | Observation | Direct | High | P1 40–43 |
| PIR-007 | Crew, morale, duel progress, advantage and disorientation reciprocally affect tempo/casualties; one crewman needs the next received captain hit for surrender. | Observation | Direct | High | P1 41–44 |
| PIR-008 | Contact can rescue ejected survivors; a floating cargo barrel instead credits 50 gold immediately. | Observation | Direct | High | P1 36 |
| PIR-009 | Capture transfers gold/new eligible specialist automatically and permits selected sailors/cargo/vessel; sinking destroys target contents and eight owned vessels prevent keeping a ninth. | Observation | Direct | High | P1 22, 37 |
| PIR-010 | Sinking/capture wins, distance or possible nightfall draws, and own sinking/duel surrender loses; remaining fleet support changes defeat recovery, not previously banked wealth. | Observation | Direct | Medium | P1 36–37 |
| PIR-011 | Enemy damage, nationality/treaties and local interests determine distinct national/city responses; a damaging draw uses victory-style national opinion. | Observation | Direct | High | P1 38–39 |
| PIR-012 | Naval statistics/readiness and duel crew/advantage/position/disorientation disclose current pressure, not perfect future random results. | Observation | Direct | High | P1 32–33, 40–44 |
| PIR-013 | Combat inputs remain live with Shift-P pause; campaign time advances in naval combat but stops in duels and prize menus. | Observation | Direct | High | P1 21, 82, 134–135 |

## Basic data

- Release / origin: Firaxis's Windows reinterpretation, originally released in 2004; not a rules-equivalent copy of the earlier Pirates! editions. A dated secondary publishing report corroborates the November 2004 PC release; it is not mechanical evidence.
- Platform or physical form: original Windows single-player PC rules as documented by the publisher booklet; other releases unassessed.
- Mechanical families: `FAM-009` tactical forecast/counterplay and `FAM-010` real-time system pressure. Known side reach, shot bias and typed defence inform choices without guaranteeing hidden impact rolls. Crew combat is automatic, not independently ordered agents.
- Sources accessed 2026-10-03:
  - **P1:** [Publisher-distributed PC manual](https://cdn.akamai.steamstatic.com/steam/apps/3920/manuals/manual.pdf). Relevant printed pages 10–15, 17–23, 29–44, 48–49, 82, 106–107, relevant ammunition/specialist/commodity paragraphs 108–112 and controls 134–135 read; diagrams 32–33 and 40–41 visually inspected. Production marks date it to June 2005; its exact launch-disc/executable correspondence is untested. Local PDF SHA-256 `d335ca09a46a071206d05ccb93d80af770cc7c5c2606077f1df422cde7c640f1`. The duplicate pause/ammunition keypad label is not used to contradict the unambiguous Shift-P guidance. Full PDF extraction is not a claim that every page was read.
  - **P2:** [Authorised Steam product](https://store.steampowered.com/app/3920/Sid_Meiers_Pirates/), current legal destination and Windows identity. Its 11 July 2005 listing is not the original 2004 launch date or executable parity evidence.
  - **S1:** [GameSpot publishing report, 2 May 2005](https://www.gamespot.com/articles/2k-games-claims-pirates/1100-6123393/), article body read; records the earlier November 2004 PC release separately from the upcoming Xbox release. Not used for rules or a broader platform audit.
- Claim IDs: `PIR-001`–`PIR-013`. No source code or native success measurement is asserted.

## Mechanical decomposition

### Action Genes

`ACT-008` transfers local direct helm navigation, `ACT-161` the chosen sword
strike and `ACT-215` the pre-duel compatible sword slot. `ACT-655` retains
canvas state, `ACT-656` requests the current side battery, `ACT-657` selects
available loading type, `ACT-658` chooses typed live defence, `ACT-659` risks a
taunt and `ACT-660` selects prize assets. These are commands with distinct
causal effects, not a gene per keypad key, sword or ammunition name.
`PIR-001`–`PIR-003`, `PIR-005`–`PIR-009`.

### System Behaviour Genes

`SYS-004` transfers source-reported component chance, `SYS-037` contact gold
credit and `SYS-215` live target combat, including retreat/draw parameters.
`SYS-1290` resolves sailing, `SYS-1291` component/raking impacts,
`SYS-1292` partial crew-sensitive reload and `SYS-1293` contact boarding.
`SYS-1294` resolves typed pushback and sword tempo; `SYS-1295` is the reciprocal
captain/crew feedback and next-hit surrender, not a duelist health pool.
`SYS-1296` rescues operating people rather than scoring a barrel.
`SYS-1297` settles selected/automatic capture transfers, `SYS-1298` the own
defeat branch and `SYS-1299` separate public standing. Numeric biases, morale,
crew counts, sword speeds, wind responses and loss fractions are parameters;
their exact native equations are not supplied. `PIR-001`–`PIR-011`.

### Constraint Genes

`CON-285` transfers current compatible ordnance eligibility. `CON-754`
separates side region, ammunition reach and installed side share from legal
equipment: at most half the installed cannon can fire in one broadside, with
only the currently loaded subset available. `CON-755` suppresses retention
of a ninth owned vessel. Historically `CON-618` was deprecated under
`TAXONOMY_CHANGE_038` and is not used here. Reject a passenger cap or an
unproved mass equation for prize cargo. `PIR-002`, `PIR-003`, `PIR-009`.

### Information Genes

`INF-463` exposes current vessel statistics and loaded readiness.
`INF-464` exposes the coupled duel's position, crews, advantage and
disorientation. Neither promises a hidden future damage component or exact
casualty forecast. `PIR-012`.

### Objective Genes

`OBJ-029` transfers incapacitating the finite required enemy before own defeat.
Sinking and capture satisfy it differently; distance and possible nightfall
draws terminate without that victory. Maximum career wealth is not a hidden
mandatory encounter objective. `PIR-009`, `PIR-010`.

### Time Genes

`TIM-003` transfers live sea/duel input; manual Shift-P pause is a parameter,
not paused tactical-order scheduling. `TIM-002` transfers untimed discrete
prize choices. `TIM-032` distinguishes the campaign calendar from live duel
time. Calendar stasis is not proof of turn-based fencing. `PIR-013`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Full canvas, current wind/heading and condition | Reef, then steer | Retained canvas slows travel and tightens handling, subject to current condition | Not a temporary boost or movement prohibition | PIR-001 |
| Target directly ahead; loaded guns | Request Fire | No direct bow broadside is legal | Firing authority differs from raking impact | PIR-002 |
| Legal side target; only part of the battery loaded | Request Fire | Available loaded side guns discharge within the installed half limit | Not an all-guns readiness requirement | PIR-002 |
| Fired guns, declared crew and selected ammunition | Let live time advance | Automatic reload restores readiness at crew-sensitive rate | Crew loss changes exposure between attacks | PIR-002 |
| Vessel lacks chain equipment | Request chain selection | Missing ordnance is not admitted by its control key | Equipment availability, not universal initial types | PIR-003 |
| Eligible loaded broadside | Fire a chosen shot type | Impact uses its range/component bias and possible collateral harm | Not deterministic exclusive sail/crew targeting | PIR-003, PIR-004 |
| Target bow/stern intersects legal side shot | Resolve impact | Raking increases harm to the target | No bow-mounted firing claim | PIR-004 |
| All sails lost but hull remains | Approach the disabled vessel | Control is lost and surrender may follow | Not guaranteed immediate capture | PIR-004 |
| Ejected floating survivor or barrel | Sail through its location | Recover crew, or credit 50 gold for a barrel | Operating population differs from abstract credit | PIR-008 |
| Two live vessels reach boarding contact | Resolve contact and pick sword | Captain duel begins alongside automatic crew fight | One causally complete encounter | PIR-005 |
| Incoming chop, slash or thrust | Commit duck, jump or parry | Matching avoidance blocks; parry of chop/slash leaves one step; wrong duck/jump takes hit | Typed defence, not universal invulnerability | PIR-006 |
| Captain in a short opening | Attempt taunt | Completion shifts advantage; a received hit interrupts | Non-damaging input still risks live exposure | PIR-007 |
| Crew casualties or successful captain pushback | Continue duel | Morale/advantage feedback changes crew performance and captain tempo | Crew fight is coupled, not manual extra turns | PIR-007 |
| Own crew reaches one | Avoid attacks and land a hit | Duel can continue and still be won; next received hit forces surrender | No immediate one-crew loss | PIR-007 |
| Captain already at losing stage edge | Receive another hit | Duel terminates with surrender or overboard loss | Positional terminal, not character HP | PIR-006 |
| Captured target and eligible new specialist | Settle prize | All gold/new specialist transfer automatically; sailors/cargo/vessel follow choices | Not automatic all-assets collection | PIR-009 |
| Eight owned vessels | Capture another merchant | Keep-vessel choice is absent | Existing fleet cap affects the same settlement | PIR-009 |
| Own flagship sinks | Settle declared remaining fleet | Backup recovery with partial carried loss or solo marooning is selected | Banked wealth differs from carried wealth | PIR-010 |
| Opponent withdraws beyond sight after taking damage | Resolve draw | Victory-style national opinion is applied | Escape does not erase political consequences | PIR-010, PIR-011 |
| Live captain duel or prize menu | Continue input or deliberate | Calendar remains frozen; duel threats still advance, menu has no battle deadline | Distinct calendars and live time | PIR-013 |

Random impact and casualty outputs are source-reported conditional branches,
not asserted deterministic successful rolls. Native state/seed values must be
retained to reproduce an actual trace.

## Strategic and experiential structure

Opening the sails improves travel but can expose canvas; shortening them can
help align the side battery. Firing early spends a partial opportunity instead
of waiting exposed for a larger volley. Round, chain and grape exchange reach
and desired capture condition without guaranteeing a precise component.
Boarding protects material value but replaces sailing risk with typed response
and reciprocal crew pressure. A fast rapier, slower defence, taunt opening and
last crewman are concrete tradeoffs, not a measured optimal policy.

## Replay and variation

Declared wind, heading, ship condition, ordnance, fleet support, morale, target
and probabilistic impacts vary the packet. Campaign recruitment, repair or a
different target creates another declared entry state, not authority to import
every career mechanic. Exact draw thresholds and native timing remain open.

## Adjacent systems and history

The manual explicitly distinguishes the earlier fixed crew requirements from
the 2004 product's degraded undermanned operation. Modern ports and the Steam
store date do not establish identical rules. Numerical corpus proximity does
not imply historical influence or genre equivalence.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-215`, `ACT-655`–`ACT-660` | helm, sword, canvas, battery, ammunition, defence, taunt, prize |
| System Behaviour | `SYS-004`, `SYS-037`, `SYS-215`, `SYS-1290`–`SYS-1299` | chance, gold contact, live combat, sailing, impact, reload, boarding, duel, crew, rescue, settlement, standing |
| Constraint | `CON-285`, `CON-754`, `CON-755` | ordnance compatibility, side/reach/gun share, fleet cap |
| Information | `INF-463`, `INF-464` | ship condition/readiness, captain position/crew/advantage |
| Objective | `OBJ-029` | finite opponent sink/capture |
| Time | `TIM-002`, `TIM-003`, `TIM-032` | prize choice, live combat, separately suspended campaign calendar |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `486` (`GAME-0001`–`GAME-0486`).
- Exact genome matches: none.
- Tied near matches: `GAME-0277` — Cuphead (`5 / 40 = 0.125000`); `GAME-0360` — Space Invaders (`5 / 40 = 0.125000`); `GAME-0427` — Alan Wake (`5 / 40 = 0.125000`).
- Supported combination subsets: none.
- Scan date: 2026-10-03.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0277` Cuphead | `ACT-008`, `ACT-161`, `SYS-215`, `OBJ-029`, `TIM-003`: local movement, direct weapon attack, live hostility, finite foe defeat and live input. | Cuphead's fixed Root Pack packet uses three sequential health-gated bosses, pink contact parry, meter-paid EX and retained results. Pirates instead couples wind/canvas and partial side fire to boarding, typed pushback, reciprocal crew pressure and prize/world settlement. No pink parry, HP allowance or Super Meter transfers. | Near; `5 / 40 = 0.125000`. |
| `GAME-0360` Space Invaders | `ACT-008`, `ACT-161`, `SYS-215`, `OBJ-029`, `TIM-003`: local movement, direct weapon attack, live hostility, finite foe defeat and live input. | Space Invaders uses a single player-shot channel, descending accelerating rack, eroded fortresses, base stock and successor-rack rebuild. Pirates permits partial multi-gun side batteries and a separate boarding phase with crew/duel feedback and chosen prizes. Neither formation geometry nor arcade stock transfers. | Near; `5 / 40 = 0.125000`. |
| `GAME-0427` Alan Wake | `ACT-008`, `ACT-161`, `SYS-215`, `OBJ-029`, `TIM-003`: local movement, direct weapon attack, live hostility, finite foe defeat and live input. | Alan Wake's lone Taken packet requires light stripping before eligible revolver damage and trades boost charge against battery stock. Pirates instead uses ammunition-biased vessel damage, sailing alignment, optional contact boarding and capture settlement. No darkness barrier, charge recovery or battery refill transfers. | Near; `5 / 40 = 0.125000`. |

## Taxonomy impact

`TAXONOMY_CHANGE_224` isolates twenty-one Active additions and ten unchanged
reuses. Named causal-role review partitions all thirty-one uses and authors
their bilingual plain-language presentation. No earlier English definition,
signature, verified combination, platform or public release mapping changes.

## Negative results

- Reject bow/stern firing, fully loaded-only fire, guaranteed exclusive ammo damage and immediate capture at destroyed sails.
- Reject a captain health bar, immediate surrender at one crewman, full parry of every attack and turn-based fencing inferred from the calendar.
- Reject all-auto prize transfer, 50 cargo units per barrel, banked-wealth loss, harmless damaging draws and invented native rates or loss fractions.
- Reject embodied separate ship stations, cockpit camera, ground-vehicle instruments, deprecated carry cap and a whole campaign inferred from one encounter.

## Delta summary

## New facts

- [Observation | Direct | Medium] Complete sea-to-prize combat couples condition-sensitive sailing, partial broadsides and crew/duel pressure. `PIR-001`–`PIR-013`.

## New genes

- [Observation | Direct | Medium] Twenty-one additions isolate documented input, response, admission, disclosure and calendar boundaries; ten existing boundaries transfer unchanged.

## New combinations

- [Observation | Limited | Medium] No new verified combination; proper subsets are derived from the full accepted signature.

## Taxonomy changes

- [Observation | Direct | Medium] `TAXONOMY_CHANGE_224`; no prior canonical English or signature mutation.

## New questions

- Establish native original-build/save identity, complete success trace, cargo admission calculation, impact/casualty rates, draw thresholds and simultaneous-outcome precedence before strengthening limited claims.

## Next recommended game

- [Hypothesis | Limited | Medium] Original PlayStation wipEout, `GAME-0488`, the next approved subject after this unit's acceptance.
- Optimisation criterion: retain cross-platform and decision-structure diversity.
- Expected information gain: course traversal, acquired weapon use and bounded race settlement rather than sailing/crew capture.
- Backlog impact: eight approved subjects remain; no implicit push or publication.

## Why this game

- [Hypothesis | Limited | Medium] The source-supported partial battery and reciprocal boarding pressure add decision structures without importing the whole career or assuming port parity.
