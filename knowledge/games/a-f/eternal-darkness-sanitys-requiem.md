---
game_id: GAME-0473
slug: eternal-darkness-sanitys-requiem
game_title: "Eternal Darkness: Sanity's Requiem"
analysis_status: reviewed
reviewed: 2026-10-02
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-199
    - ACT-200
    - ACT-341
    - ACT-419
  system:
    - SYS-045
    - SYS-215
    - SYS-578
    - SYS-794
    - SYS-1233
  constraint:
    - CON-282
  information:
    - INF-119
    - INF-449
  objective:
    - OBJ-164
  time:
    - TIM-003
---

# Game: Eternal Darkness: Sanity's Requiem — Ellia's tomb chapter

Use the [canonical genome vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Ellia, her necklace, the blowgun, candles and the Metal Staff are carrier parameters, not separate gene names.

## Analysis scope

- Version / ruleset: original English Nintendo GameCube *Eternal Darkness: Sanity's Requiem*, chapter two, “The Binding of the Corpse God”, controlling Ellia in the Angkor Thom tomb. This is not the opening playable Pious Augustus chapter, whose sanity meter is absent, nor the later Alex chapters. The disc revision and regional differences were not inspected.
- Structured analysis target: `PLAT-NINTENDO-GAMECUBE` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: first direct control of Ellia inside her chapter, after the prior chapter's artifact choice. That choice can change the later enemy carrier; the present record does not assume one exclusive alignment or replay Pious's selection.
- Primary decision loop: inspect the local room and Ellia's health/sanity feedback, steer around lighter trap tiles, fight or avoid reachable undead, use an aimed strike and close finish where legal, recover health from a limited necklace charge while stationary, and manipulate discovered candle, statue and item fixtures to open the next authored tomb passage. Encountering hostile creatures lowers sanity; a successful finish can restore it. Low sanity can distort the presentation, so a visual event is not automatically a reliable new world object.
- Positive terminal: after the authored tomb route, obtain the Heart of Mantorok and Metal Staff, backtrack to install the staff in its matching slot and enter the newly opened way to Mantorok's chamber. The ensuing chapter-ending scene returns control to the surrounding story. Ellia does not defeat Pious here.
- Failure and recovery: hostile attacks or triggered traps can reduce health; at zero health this chapter attempt fails. The necklace can restore health while charges remain. Sanity loss produces escalating audiovisual effects and may cause health damage at depletion; it is a different pool, not a synonym for health or a fixed chapter timer. Exact hit values, trap activation geometry, necklace charge count in every disc revision and hallucination selection were not measured.
- Included: Ellia's chamber and tomb traversal, lighter floor trap tiles, reachable zombies, aimed limb strikes and downed-enemy finishing, limited necklace healing, health and sanity, candle and statue interactions, blowgun acquisition and consequent sword break, conditional sword repair through a rescued guard, Heart and Metal Staff, staff slot and chapter exit.
- Excluded: Pious's prologue, the player choice that preceded this chapter, other playable centuries, runic spells and Tome casting unavailable to Ellia here, campaign-wide alignment endings, later Alex inventory, a compulsory guard rescue, a uniquely asserted left/right candle solution, later ports, glitches and speedrun routes.
- Reproducibility: two contemporary written walkthroughs agree on the main item-to-exit chain but conflict on exact candle states at one altar. The reproducible packet therefore asserts the need to set the authored candle state, not one unsupported universal pattern. A disc replay needs chapter entry, selected prior alignment, health, sanity, necklace charge, current weapon, fixture states, route and inputs. None were directly recorded.
- Direct-play status: no GameCube disc, console, executable, controller trace, gameplay screenshot, video or audio was inspected. Nintendo's publisher description establishes the original game identity and psychological-horror premise; written guides support the bounded chapter reconstruction. The illustration is original, not game capture.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ED-001` | The original GameCube chapter after Pious controls Ellia in an ancient Cambodian tomb | Observation | Corroborated | High | P1, S1, S2 |
| `ED-002` | Pious's first playable chapter lacks the sanity meter, whereas Ellia's route exposes the mechanic | Observation | Corroborated | High | S1, S2 |
| `ED-003` | Facing monsters lowers sanity and finishing a fallen enemy can restore it | Observation | Corroborated | Medium | S1, S2 |
| `ED-004` | Low sanity produces perceptual effects rather than a newly guaranteed physical threat | Observation | Corroborated | Medium | P1, S3 |
| `ED-005` | Lighter floor tiles signal contact-triggered traps along Ellia's tomb route | Observation | Corroborated | Medium | S1, S2 |
| `ED-006` | Ellia can aim at enemy limbs, break their capability and finish a downed foe | Observation | Corroborated | Medium | S1, S3 |
| `ED-007` | Ellia's necklace provides a finite, stationary health recovery opportunity | Observation | Limited | Medium | S2, S3 |
| `ED-008` | The first candle puzzle and necklace-statue interaction gate the next route; sources disagree about a later exact candle pattern | Observation | Corroborated | Medium | S1, S2, S3 |
| `ED-009` | Taking the blowgun causes a fall and sword loss; rescue and sword repair through a guard is optional | Observation | Corroborated | Medium | S1, S2 |
| `ED-010` | The Heart and Metal Staff are followed by a staff-slot return and chapter-ending chamber entry | Observation | Corroborated | High | S1, S2 |

## Basic data

- Release / origin: Silicon Knights / Nintendo, original GameCube release in 2002. The bounded reconstruction uses descriptions of the English original; it does not certify a specific disc revision.
- Platform or physical form: original licensed Nintendo GameCube disc and controller, one-player chapter.
- Mechanical families: `FAM-010` real-time system pressure; `FAM-013` inventory and fixture dependencies; `FAM-017` ordered dependencies. These describe causal structure, not horror genre.
- **P1**: [Nintendo's official GameCube product overview](https://www.nintendo.com/en-gb/Games/Nintendo-GameCube/Eternal-Darkness-Sanity-s-Requiem-267961.html), original platform, release and sanity presentation (checked 2026-10-02). Its promotional phrasing is not treated as a precise meter-direction rule.
- **S1**: [Ryo_Hazuki's contemporary GameCube walkthrough](https://gamefaqs.gamespot.com/gamecube/913957-eternal-darkness-sanitys-requiem/faqs/17676), Ellia chapter and sanity/finisher, traps, objects, fall, repair and staff-slot route (checked 2026-10-02).
- **S2**: [WalkerBoh's GameCube walkthrough](https://gamefaqs.gamespot.com/gamecube/913957-eternal-darkness-sanitys-requiem/faqs/30167), Pious boundary and Ellia chapter, including necklace, room progression and optional guard (checked 2026-10-02).
- **S3**: [Myke's contemporary walkthrough](https://gamefaqs.gamespot.com/gamecube/913957-eternal-darkness-sanitys-requiem/faqs/17614), Ellia's candle and recovery route and general sanity explanation (checked 2026-10-02).
- Claim IDs: `ED-001`–`ED-010`. No direct play or audiovisual inspection. A modern document labelled “official manual” but lacking an original publisher scan and containing internal inconsistencies was excluded from mechanical evidence.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: move Ellia room by room around visible trap tiles and enemies (`ED-005`).
- Reuse `ACT-161`: aim and strike a reachable hostile, including a selectable limb; the effect of detachment is System resolution (`ED-006`).
- Reuse `ACT-199`: pick up and equip the sword, blowgun, necklace or staff when compatible; acquiring an item alone does not solve the gate (`ED-007`, `ED-009`, `ED-010`).
- Reuse `ACT-200`: use the carried necklace's bounded recovery while stationary, spending its limited use rather than deleting the necklace item (`ED-007`). The exact animation interruption frame is not measured.
- Reuse `ACT-341`: set eligible candles, apply the necklace at the statue, interact with the guard and install the staff in the matching slot (`ED-008`–`ED-010`).
- Reuse `ACT-419`: perform a close finish on a vulnerable fallen hostile while it remains eligible (`ED-003`, `ED-006`).

### System Behaviour Genes

- Reuse `SYS-045`: ordinary undead continue local pursuit without a separate player order (`ED-003`).
- Reuse `SYS-215`: resolve directly commanded strikes and hostile counterattacks in live time (`ED-006`).
- Reuse `SYS-578`: apply trap/hostile injury, necklace healing and lethal zero health to Ellia's one health pool (`ED-007`).
- Reuse `SYS-794`: repeated compatible hits detach an eligible enemy limb and remove its carried capability while the enemy can remain alive (`ED-006`). This is not a claim about Dead Space's tissue layers.
- Add `SYS-1233`: hostile encounters lower Ellia's separate sanity reserve, eligible finishing raises it, and low states select misleading audiovisual effects; at depletion, health can become endangered (`ED-003`, `ED-004`). Unlike `SYS-592`, the effects do not make shadow creatures into persistent physically hostile entities.
- Resolution order: local room and meter feedback; movement or item/fixture choice; trap or hostile contact; health and sanity settlement; authored fixture gate update; exit only after the staff-slot route is complete.

### Constraint Genes

- Reuse `CON-282`: mandatory tomb progression is ordered by candle, statue, acquired item and staff-slot states; merely possessing the staff or reaching a sealed door does not end the chapter (`ED-008`–`ED-010`). Guard rescue and weapon repair are a conditional branch, not a universal gate.

### Information Genes

- Reuse `INF-119`: health, sanity and carried equipment are shown to the player, with no exact future hallucination schedule (`ED-003`, `ED-007`).
- Add `INF-449`: local stone, trap-tile, candle, statue and enemy cues help the player infer immediate affordances, but sanity-driven audiovisual alterations can make apparent events unreliable; the route must be checked against persistent fixture and inventory state (`ED-004`, `ED-005`, `ED-008`).

### Objective Genes

- Reuse `OBJ-164`: complete this chapter's authored exit event by opening the staff-slot route and entering the final chamber; the result transfers back to the surrounding story (`ED-010`).

### Time Genes

- Reuse `TIM-003`: enemies and attack/trap consequences resolve in real time; there is no evidenced chapter-wide countdown (`ED-003`, `ED-005`, `ED-006`).

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Ellia sees a lighter tile before the next room | Route around it or step on it | Avoidance preserves state; contact can trigger a trap and injure Ellia | visible risk, not an invisible universal timer | `ED-005` |
| A reachable undead is active | Aim at one eligible limb and strike | Enough compatible damage detaches the limb and removes its function, while the enemy may remain active | attack command versus body-state resolution | `ED-006` |
| A hostile is down and Ellia has lost sanity | Approach and execute a legal finish | The hostile is finished and sanity may rise | recovery is conditional on accepted combat resolution | `ED-003`, `ED-006` |
| Ellia has missing health and remaining necklace use | Stop moving and use the necklace | Health can recover while the limited reserve decreases | health and sanity are distinct resources | `ED-007` |
| The relevant room's candle/fixture condition is unmet | Change eligible candle states and apply the required item | Only the accepted authored configuration admits the next passage | local puzzle gate, not an asserted universal exact pattern | `ED-008` |
| Blowgun still rests in its pickup position | Take the blowgun | A scripted fall follows; Ellia's sword breaks and an optional repair route becomes relevant | pickup changes more than inventory | `ED-009` |
| Ellia has the Heart and Metal Staff after the lower route | Return and install the Metal Staff in its slot | The final door opens; entering resolves Ellia's chapter | ordered item-to-exit objective | `ED-010` |

## Strategic and experiential structure

- Local decision: test a safe path around lighter trap tiles; choose whether to fight a nearby enemy and target its attack-bearing limb, or preserve health by avoiding it.
- Medium-term planning: treat the healing necklace as finite, protect health separately from sanity, and compare unsettling visual events with stable room and inventory state.
- Long-term structure: solve the tomb's authored fixture order, survive the blowgun-induced fall, optionally repair the sword, secure Heart and Staff, and return to the slot before entering the ending chamber.
- Failure attribution: a low sanity value may make presentation misleading, but direct combat and trap damage affect health. Neither low sanity nor a frightening image by itself proves a new physical enemy.
- Trust boundary: the route is reconstructed from written sources, not a claimed original-disc playthrough. The conflicting later candle solutions remain unselected.

## Replay and variation

The tomb is authored. Prior alignment, health/sanity state, optional guard rescue, weapon use and encounter handling vary. That is not procedural room generation. Sanity effects vary as presentation; this record does not assert a fixed event schedule.

## Adjacent systems and history

`GAME-0186` *Don't Starve Together* also has sanity but its low thresholds can materialise hostile shadow creatures in an open survival loop. Ellia's chapter instead uses enemy-contact/finish feedback and deceptive presentation in an authored tomb. `GAME-0259` *Dead Space (2023 remake)* shares capability-changing component destruction; Ellia's targetable limbs do not inherit layered skin/flesh/bone feedback. Neither comparison transfers an entire genre package.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-199`, `ACT-200`, `ACT-341`, `ACT-419` | route, targeted strike, items, limited healing, fixtures, finish |
| System Behaviour | `SYS-045`, `SYS-215`, `SYS-578`, `SYS-794`, `SYS-1233` | enemies, combat, health, severance, sanity |
| Constraint | `CON-282` | ordered tomb gates, optional repair |
| Information | `INF-119`, `INF-449` | status, affordances and unreliable perception |
| Objective | `OBJ-164` | staff-gated chapter exit |
| Time | `TIM-003` | live encounters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `472` (`GAME-0001`–`GAME-0472`).
- Exact genome matches: none.
- Tied near matches: `GAME-0344` — Prince of Persia: The Sands of Time (`8 / 25 = 0.320000`).
- Supported combination subsets: none.
- Scan date: 2026-10-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0344` *Prince of Persia: The Sands of Time* | Direct movement and aimed strikes (`ACT-008`, `ACT-161`), stateful fixtures (`ACT-341`), live combat and health (`SYS-215`, `SYS-578`), ordered story gates (`CON-282`), visible character resources (`INF-119`) and real time (`TIM-003`). | The Prince's packet resolves sword-and-Dagger escape with rewind and sand-resource rules. Ellia's chapter instead tests encounter-driven sanity, unreliable audiovisual events, limb dismemberment, limited necklace recovery, downed-enemy finishing and a returned Metal Staff. Shared tomb traversal does not make the decision loops identical. | Sole tied-near maximum, `0.320000`; neither exact nor a verified-combination match. |

## Taxonomy impact

`TAXONOMY_CHANGE_210` separates Ellia's encounter-responsive sanity/perceptual system and the locally fallible presentation from existing continuous sanity-plus-physical-shadow rules. No earlier signature or verified combination changes.

## Negative results

- `SYS-592` and `CON-501` need sanity-gated corporeal shadow enemies. The written Ellia evidence supports misleading perception, not those physical entities.
- `INF-313` requires layered visible tissue state; Ellia's targetable enemy limbs do not establish skin/flesh/bone layers.
- A fixed exact later candle pattern is disputed across contemporaneous written routes, so it is not encoded as a gene or solved route.
- Later runic spells, Tome casting and the Pious opening cannot be attributed to Ellia's scoped chapter.

## Delta summary

## New facts

- [Observation | Corroborated | Medium] Ellia's tomb route couples sanity loss and finisher recovery with fallible audiovisual feedback, distinct from her health and from Pious's opening chapter (`ED-002`–`ED-004`).
- [Observation | Corroborated | Medium] A blowgun-triggered fall changes equipment, and a later Heart/Staff backtrack gates the chapter exit; exact candle configurations remain disputed (`ED-008`–`ED-010`).

## New genes

- [Observation | Corroborated | Medium] Two Active boundaries: `SYS-1233` and `INF-449`.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_210`; no earlier signature changed.

## New questions

- What exact hallucination selection and health effect occurs at every sanity threshold in a pinned original GameCube revision?
- Which later candle configuration is accepted by a direct original-disc trace under each prior alignment?
- What exact interruption and charge count govern Ellia's necklace in that revision?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0474` *Metroid Fusion*, original Game Boy Advance.
- Optimisation criterion: continue the approved cross-platform sequence, switching from GameCube psychological horror to handheld action exploration.
- Backlog impact: do not start until this unit's gates, one local commit and the Goal stop window.

## Why this game

- [Hypothesis | Limited | Medium] Ellia's chapter tests whether an explicit sanity state and unreliable audiovisual events can be represented without treating every hallucination as a physical enemy or borrowing later campaign spells.
