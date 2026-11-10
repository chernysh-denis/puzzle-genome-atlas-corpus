---
game_id: GAME-0475
slug: the-house-of-the-dead
game_title: The House of the Dead
analysis_status: reviewed
reviewed: 2026-10-02
combination_ids: []
gene_ids:
  action:
    - ACT-490
    - ACT-625
  system:
    - SYS-045
    - SYS-215
    - SYS-578
    - SYS-915
    - SYS-1235
    - SYS-1236
    - SYS-1237
  constraint:
    - CON-285
  information:
    - INF-119
    - INF-179
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: The House of the Dead — original arcade `Tragedy`

Use the [canonical genome vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The mansion, handgun, researcher, bridge, sewer and Chariot are carrier parameters, not separate gene names.

## Analysis scope

- Version / ruleset: original one-player Sega Model 2 *The House of the Dead* upright arcade cabinet, first chapter `Tragedy`, reconstructed from Sega's original operator manual and original-game sources. No particular board ROM revision or operator difficulty/life setting was inspected. The Saturn and Windows ports, sequel, 2022 remake and modern pointer controls are excluded.
- Structured analysis target: original arcade cabinet with display-sensing handgun; see `GAME-0475` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: one credit has started a one-player game; the first `Tragedy` encounter presents a creature attacking a scientist outside Curien Mansion. The camera begins its authored approach, the handgun is available and chapter-one choices remain unsettled.
- Primary decision loop: aim the physical gun at a current hostile, threatening object or eligible scenery; spend loaded rounds or deliberately fire outside the screen to refill; protect a visible scientist by hitting the threat without hitting the person; accept the route chosen by the encounter result, then repeat against the next live view and Chariot's changing vulnerable area.
- Positive terminal: Chariot's life meter reaches zero, the first chapter clears and the second chapter's title appears. Stop before the next playable encounter. Merely rescuing one researcher, discovering an item or reaching the boss room is not the terminal.
- Negative terminal: the one-player life-point stock reaches zero before Chariot falls and no paid continue is taken. The cabinet permits a paid continue, but it is outside this one-credit packet; the observed operator default and exact starting stock are not fixed here.
- Included: one physical arcade handgun; aimed shots, misses and off-screen refill of its six-shot magazine; autonomous enemies and projectiles; finite life points; a wrong shot at a scientist costing a life point; optional rescue and first bridge route branch; scenery-revealed special items, point/life rewards and recovery cap; authored camera progression through local fights; Chariot's protected chest target, later exposed body and boss meter; real-time threats.
- Excluded: two-player drop-in and shared judgement, coin economy after start, paid continues, chapter-two through final-chapter routes and endings, a whole-game perfect-rescue requirement, exact stage score formula, weapon upgrades of ports/remake, PC or Saturn modes, exact boss hit counts and damage constants, sensor sampling protocol, item-location table and a claim that every branch was directly played.
- Reproducible parameterisation: on a working original upright cabinet with a calibrated gun, start one-player chapter one; at each live view fire on a visible threat, point outside the screen and trigger to refill as needed, and separately record life/rounds and whether threatened scientists survive. At the first bridge rescue, compare a successful shot on the attacker with the researcher's failure: the former yields a front-door approach, the latter a lower/sewer route. Continue along either authored branch to Chariot, target its initial exposed chest region until armour changes, then the exposed body until boss health is zero; stop when the second chapter begins. These are source-reconstructed procedures, not executed test traces.
- Potential scoped modules: other first-chapter branch switches, exhaustive item and rescue census, two-player interactions, later chapters and endings, original ROM/sensor validation, operator-setting effects, and a controlled cabinet playthrough each need separate evidence.
- Direct-play status: no cabinet, game board, gun, ROM, port executable, controller trace, game screenshot, video, audio or direct play was inspected. Sega's manual was read as an HTML transcription of original pp. 16–17 after the PDF mirror denied direct download; the art is a new conceptual illustration, not a frame capture.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HD-001` | The original cabinet uses Sega Model 2 hardware and handgun controllers; trapped researchers are rescue targets and actions can change the story route. | Confirmed | Direct | High | P1 |
| `HD-002` | Current bullets and each player's life points are displayed; a shot at a hostage costs one life point and zero life points ends play absent a continue. | Confirmed | Direct | High | P2 |
| `HD-003` | Pulling the trigger with the gun pointed outside the screen reloads the limited magazine; the original gun's usual capacity is six shots. | Observation | Corroborated | High | P2, S1, S3 |
| `HD-004` | Enemy projectiles and scenery can be shot; eligible scenery may reveal a special item that is itself shot for points or life recovery, with a configurable life cap. | Confirmed | Direct | High | P2, P3 |
| `HD-005` | The first chapter's threatened bridge researcher is a consequential rescue: survival selects the mansion entrance route, failure selects a lower/sewer route. | Observation | Corroborated | Medium | P1, S1, S2 |
| `HD-006` | Chariot follows the first chapter's authored approach; its protected early state has a vulnerable chest region, then its armour changes and exposed body can be hit until the boss meter empties. | Observation | Limited | Medium | P2, S1 |
| `HD-007` | Ordinary enemy head hits are more effective; live attacks and a wrong civilian shot can deplete life before the boss terminal. | Observation | Corroborated | High | P2, P3, S1 |
| `HD-008` | The cabinet supports a paid continue and a second player joining during play, but neither is part of the bounded one-credit, one-player signature. | Confirmed | Direct | High | P3 |
| `HD-009` | Original operator settings can vary difficulty and life cap, so this unit does not claim one universal start-life count, boss-hit threshold or board revision. | Confirmed | Direct | High | P3 |

## Basic data

- Release / origin: Sega original arcade *The House of the Dead*, documented as a 1997 Sega product and a Model 2 game. This analysis is not for the 1998 Saturn/Windows port or the 2022 remake.
- Platform or physical form: original Sega upright arcade cabinet with display-sensing handgun and Model 2 board.
- Mechanical families: tactical forecast and counterplay (`FAM-009`) for aiming under threat while avoiding a civilian; real-time system pressure (`FAM-010`) for advancing threats, magazine and life decisions.
- **P1:** [Sega Amusements original-game product page](https://segaarcade.com/games/the-house-of-the-dead-1), accessed 2026-10-02. Original cabinet identity, Model 2 hardware, handgun controllers, trapped scientists and action-dependent story.
- **P2:** [Sega original upright operator manual, p. 16](https://www.manualslib.com/manual/1438193/Sega-The-House-Of-The-Dead.html?page=16), accessed 2026-10-02. Life and bullet HUD, hostage penalty, off-screen reload, defensive projectile/scenery shots, special-item capture and boss-health chapter clearance.
- **P3:** [same original manual, p. 17](https://www.manualslib.com/manual/1438193/Sega-The-House-Of-The-Dead.html?page=17), accessed 2026-10-02. Drop-in/continue availability, life-item cap, head vulnerability, action-dependent routes and repeatable enemy appearances. The mirrored PDF returned HTTP 403, so its pages were not visually inspected; the readable HTML transcription was used and this access limit remains explicit.
- **S1:** [BakaOrochi, contemporary Arcade/PC FAQ](https://gamefaqs.gamespot.com/arcade/583587-the-house-of-the-dead/faqs/8334), updated 2000, accessed 2026-10-02. First-hand arcade chapter-one sequence, threatened bridge scientist, optional route split and Chariot's chest/armour transition. PC-only modes and shortcuts are not imported.
- **S2:** [chapter-one bridge and branch documentation](https://thehouseofthedead.fandom.com/wiki/Tragedy), accessed 2026-10-02. Secondary route cross-check, not a substitute for Sega's general rule or direct cabinet play.
- **S3:** [contemporary retrospective of original cabinet gun](https://www.skooldays.com/categories/arcade/ag1063.htm), accessed 2026-10-02. Independently states six loaded bullets and off-screen trigger reload; exact board-specific capacity was not physically measured here.
- Claim IDs: `HD-001`–`HD-009`.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-490` for one physical light-gun aim/trigger request at a visible on-screen enemy, breakable fixture, projectile or revealed item. Unlike a mouse reticle, the cabinet samples gun position from its calibrated display.
- New `ACT-625` for intentionally pointing the gun outside the active screen and triggering a full reload. The action does not transfer a finite reserve (`ACT-183`) and does not require a protective pedal (`SYS-1160`).

### System Behaviour Genes

- Reuse `SYS-045` for moving/attacking hostile actors, `SYS-215` for live commanded shot versus enemy response, `SYS-578` for a single visible life-point pool reduced by damage or a civilian hit and restored by eligible rewards, and `SYS-915` for finite local hostile clearance releasing the next authored camera slice.
- New `SYS-1235` maps survival of the threatened bridge researcher to one authored front-door versus lower/sewer camera route; the player does not command a free-walking avatar at this branch.
- New `SYS-1236` resolves Chariot's initial protected chest weak point, armour change and later broader vulnerability before boss health reaches zero. Exact number of required shots or threshold is deliberately unclaimed.
- New `SYS-1237` resolves optional two-step scenery reveal and special-item shot capture for points or a capped life refill. It is not a guaranteed item from every barrel.
- Resolution order: active view → aimed hostile/civilian/fixture shot or off-screen reload → eligible hit, damage, rescue or item reveal/claim → local hostile clearance → branch-specific next view → Chariot weak-point/armour phases → boss-life terminal.

### Constraint Genes

- Reuse `CON-285` for a legal playfield shot requiring the active gun's remaining magazine rounds; after the finite six-shot load is spent, a separate off-screen trigger restores it. Gun model and cap are parameters, not a carried finite ammo stock. Shooting a civilian is not prohibited by this constraint: it is possible and penalised.

### Information Genes

- Reuse `INF-179` for current-frame enemies, endangered scientists, attack objects, breakables and Chariot's visible weak area, without exposing unseen future route contents. Reuse `INF-119` for life points and loaded-bullet count, with boss health as a current encounter parameter. The boss weak point still requires recognition; no omniscient hidden route map is claimed.

### Objective Genes

- Reuse `OBJ-080` for the authored first-chapter route, mandatory Chariot defeat and crossing into the next chapter's title state. Rescuing every researcher and maximising score are optional distinctions, not substitutes for Chariot's zero-health terminal.

### Time Genes

- Reuse `TIM-003`: enemies, projectiles, rescue opportunities and the boss act while player inputs remain available. No chapter-wide timer or Time Crisis pedal deadline is admitted.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A hostile and scientist are both visible | Aim the physical gun at the hostile and trigger | A loaded round is spent; an eligible hit can end the threat while the scientist survives | precision matters to rescue | `HD-002`, `HD-007` |
| No bullets remain during a live view | Point gun outside the screen and trigger | Full magazine returns; the current view has not become protective cover | off-screen refill is a separate command | `HD-003` |
| Scientist remains on screen | Fire at the scientist instead of the attacker | One life point is lost even though an on-screen gunshot was legal | civilian penalty is not a forbidden input | `HD-002` |
| Bridge attacker is about to throw a researcher | Defeat attacker before the researcher falls | Researcher survives; authored camera approaches mansion front route | rescue-dependent branch | `HD-005` |
| Same bridge rescue is missed | Allow attacker to throw researcher | Researcher dies; authored camera uses the lower/sewer route | failure changes route, not immediate Game Over | `HD-005` |
| Eligible scenery conceals a special item | Shoot scenery, then shoot a revealed item if present | Reveal and claim are separate; eligible life/point effect settles under cap | optional exploration by aimed shots | `HD-004` |
| Chariot remains armoured with a small chest opening | Put eligible shots into exposed chest | Boss health falls and later armour-state change broadens eligible damage area | protected-to-exposed boss transition | `HD-006` |
| Chariot's health reaches zero before player life points do | Allow chapter transition | `Tragedy` clears and next chapter appears; analysis stops | positive bounded terminal | `HD-006` |
| Player life points reach zero first | Decline any paid continue | Current one-credit attempt is over, not a chapter clear | negative bounded terminal | `HD-002`, `HD-008` |

## Strategic and experiential structure

- Local decision: aim at an immediate attacker or incoming projectile while keeping the scientist out of the shot; reload off-screen before another threat closes in. Ordinary head shots are more efficient, but Chariot's early effective region is its disclosed chest weakness.
- Medium term: saving a researcher can refill life or change the later route. Taking a different branch changes the authored camera encounters; it is not free movement through a map. Optional scenery shots may reveal resources but consume live aiming attention.
- Long term: preserve enough life points through the first chapter to beat Chariot and cross into chapter two, rather than merely rescue everyone or chase a score threshold.
- Failure attribution: depleted bullets signal a missed reload opportunity; lost life may come from enemy attack or a wrongly aimed civilian hit; the bridge result explains the visible route divergence. Operator difficulty, exact hitboxes and timings can vary and were not measured.

## Replay and variation

The authored enemy appearance order is repeatable according to Sega's manual, while aim, misses, rescue outcome, optional revealed items and operator settings can change one run's route and life budget. The first bridge has at least two evidenced forward paths that later reconverge; this packet does not claim an exhaustive branch graph or guaranteed item contents.

## Adjacent systems and history

*Time Crisis* (`GAME-0443`) also uses an arcade light gun and advancing combat views, but its pedal couples cover to refill and a running countdown; this cabinet instead reloads through an off-screen trigger, exposes vulnerable civilians and selects a route from a rescue outcome. *Duck Hunt* (`GAME-0345`) also samples a physical gun, but its target-local three-shot bird opportunities and ten-target quota do not apply here. No *The House of the Dead 2* or remake-specific rule is imported.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
|---|---|---|
| Action | `ACT-490`, `ACT-625` | on-screen target or off-screen reload |
| System Behaviour | `SYS-045`, `SYS-215`, `SYS-578`, `SYS-915`, `SYS-1235`, `SYS-1236`, `SYS-1237` | enemies, rescue branch, special items and Chariot |
| Constraint | `CON-285` | limited loaded rounds and compatible fire |
| Information | `INF-119`, `INF-179` | life/rounds, current threat and boss cue |
| Objective | `OBJ-080` | Chariot clear and next-chapter threshold |
| Time | `TIM-003` | live attack and rescue opportunities |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `474` (`GAME-0001`–`GAME-0474`).
- Exact genome matches: none.
- Tied near matches: `GAME-0318` — Battletoads (`7 / 25 = 0.280000`).
- Supported combination subsets: none.
- Scan date: 2026-10-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0318` *Battletoads* | `SYS-045`, `SYS-215`, `SYS-578`, `SYS-915`, `INF-119`, `OBJ-080`, `TIM-003` | Both sustain a live hostile sequence with visible life and a guardian-gated stage exit. *Battletoads* directly moves and attacks a side-view avatar through authored platform hazards; this cabinet fixes camera travel, requires physical-gun aim/off-screen reload, can route by a researcher's survival and changes Chariot's vulnerable area. | `0.280000`; tied nearest non-exact prior signature, with shared live-combat structure but different controls and routes. |

## Taxonomy impact

`TAXONOMY_CHANGE_212` admits four bounded new genes. Earlier signatures and verified combinations remain unchanged. `TAXONOMY_CHANGE_211`, already cited by the accepted previous game, is restored as a missing numbered decision record without changing its definition or signature.

## Negative results

- Reject `ACT-183`, `SYS-1160`, `CON-717` and `INF-428`: the first assumes finite reserve transfer, the next two require Time Crisis's protective pedal/exposure gate, and the last includes a live countdown that this chapter does not have.
- Reject `SYS-967`: NES Zapper's specific darkness/target-local light sequence was not verified for Sega Model 2's gun.
- Reject `ACT-613`: the player never physically steers an avatar into the front-door or sewer branch.
- Do not treat a shot at a scientist as an illegal action; it is a legal but costly error. No full-game ending, paid continue, port mode or later weapon is inferred.

## Delta summary

## New facts

- [Observation | Corroborated | High] Original cabinet gun reload and rescue outcome change different parts of the first-chapter decision loop (`HD-003`, `HD-005`).

## New genes

- [Observation | Corroborated | Medium] Four typed boundaries distinguish off-screen reload, rescue-dependent rail routing, Chariot's protected-to-exposed body and two-shot special-item reveal/claim.

## New combinations

- [Observation | Corroborated | Medium] No new verified combination proposed; proper-subset support is recomputed from the complete signature.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_212` adds the four new boundaries; prior `TAXONOMY_CHANGE_211` documentation is restored without changing its accepted result.

## New questions

- Would a board-revision-pinned original cabinet trace determine exact bridge rescue timing, Chariot's transition threshold and hidden-item layout without importing a port's behaviour?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0476` *Ring Fit Adventure*, original Nintendo Switch, after this unit's acceptance and Goal stop window.
- Optimisation criterion: compare embodied motion input and exercise combat against the preceding arcade gun's fixed camera and human-rescue routing.
- Expected information gain: test whether authored stage progression and live threat management survive radically different input and feedback channels.
- Backlog impact: the next selection horizon after `GAME-0477` must deliberately spread platforms beyond Nintendo.
