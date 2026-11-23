---
game_id: GAME-0557
slug: boktai-the-sun-is-in-your-hand
game_title: "Boktai: The Sun Is in Your Hand"
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-131
    - ACT-161
    - ACT-199
    - ACT-202
    - ACT-341
    - ACT-489
    - ACT-756
    - ACT-757
  system:
    - SYS-057
    - SYS-215
    - SYS-369
    - SYS-578
    - SYS-605
    - SYS-1344
    - SYS-1615
    - SYS-1616
    - SYS-1617
    - SYS-1618
    - SYS-1619
    - SYS-1620
    - SYS-1621
    - SYS-1622
  constraint:
    - CON-077
    - CON-571
    - CON-578
    - CON-629
    - CON-822
    - CON-823
  information:
    - INF-125
    - INF-179
    - INF-534
  objective:
    - OBJ-307
  time:
    - TIM-003
    - TIM-025
    - TIM-036
---

# Game: Boktai: The Sun Is in Your Hand

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Django, Otenko, Boks, the Count, gun parts, sensor intensity and rank thresholds
are carrier parameters, not independent per-character genes.

## Analysis scope

- Version / ruleset: original English North American Game Boy Advance retail
  release, 16 September 2003, fresh New Game, Normal 2. Properly configured
  cartridge clock and solar sensor; original hardware rules rather than a
  sunlight patch, emulator hotkeys, Boktai 2/3, Lunar Knights or New Game+.
  No cartridge, ROM checksum, installed emulator, save or owned hardware was
  inspected; the regional executable and exact numeric parity remain untested.
- Primary decision loop: move through Fog Castle while managing visible
  patrols, sight, noise, life and stored gun energy; use solar charging,
  station stock, contact-safe positioning and the acquired Knight spread to
  reach the sealed decoy; drag the coffin back, releasing it to handle threats
  or agitation; place it at the Pile Driver, prime its two generators and
  sustain the separate sunlight-powered purification until result settlement.
- Entry and exit: enter Fog Castle from Road of Encounter on the first visit,
  before the exterior Pile Driver explanation. Follow the ordinary exterior,
  station, Knight Frame, Bok/skylight and bat-guarded coffin route; include the
  complete return and first purification, result and Fool Card, then the
  revelation that this was a decoy and the handoff back toward Road of
  Encounter. Stop before playing the post-castle overheating lesson, Calm Path
  or Small Cave. Do not misidentify this as the later Bloodrust Mansion duel.
- Reproducible parameterisation: Normal 2, ordinary original Sol Lens,
  Fighter Frame and Single Battery, acquiring and equipping Knight on this
  route. Keep a calibrated positive solar reading available for purification;
  compare zero/positive readings as the documented legality edge. Clock phase,
  real weather and sensor exposure may vary and are not the same variable.
  No fixed seed, exact damage, item counts or rank formula is asserted.
- Included: direct movement, wall adhesion and wall taps; local viewing and
  discovered dungeon map; contextual chests/panels, reachable item acquisition,
  compatible gun-part equipping and admitted restorative items; short shot
  versus held damaging spread with sufficient stored solar ammunition, rear stun/knockback and local hostile response;
  Bok sight, occlusion and Klorofolun attachment with life drain, directional
  shaking or compatible sterilisation; sunlit vulnerable-hostile destruction;
  distinct live solar input, portable energy and station storage; outdoor or
  skylight passive/held charging, typed crystal occupants and lens experience;
  bat-clear route gate; persistent ground-dragged coffin, blocked run/attack,
  release on damage and agitation control; two generators, priming, live solar
  predicate, resistible beams, Darkness depletion, graded closeout and reward;
  documented exposure-induced overheat and independent thermal firing legality;
  manual area-entry saving, Continue and clock-dependent day/night behaviour.
- Excluded: the real Count's duel, sword reflections, later four-generator
  fights or claiming the tutorial decoy directly attacks during purification;
  later elemental lenses, grenades not acquired on this route, Solar Tree
  cultivation, Sun Bank/loans, passwords, link modes, Azure Sky Tower and
  New Game+ equipment. Hidden-chest hunting, repeated lens/fruit farming,
  post-reward Fool Card use, fruit cultivation/combining and extended idle
  overheating experiments are separate loops, not requirements for this
  ordinary route. The later heat lesson is not proof that heat is impossible
  earlier; its pre-clear activation and exact thresholds are not certified.
- Potential scoped modules: Bloodrust Mansion duel and extraction; extended
  sensor/overheat management; Solar Tree and banking; full lens progression;
  subsequent Immortal purification exceptions; multiplayer/link economy.
- Direct-play status: none. Rendered the USA manual scan and inspected printed
  pages 7–9, 11, 14–15, 20, 22–25, 31, 35–37 plus the page overview. Inspected eleven
  public 320×180-cell storyboard sheets at ten-second sampling, covering
  01:30–17:50 of Alexander The Pretty Good's 18:51 English tutorial recording:
  ingress, station/equipment, patrol room, bats, coffin return, two generators,
  purification, result, decoy reveal and later heat-lesson boundary. The
  recording's difficulty, physical sensor and native execution are unverified;
  night clock plus positive light is not proof of real sunlight. Static samples
  corroborate geometry/feedback, not uninterrupted observation, native damage
  timing or sensor calibration. No video/audio playback or foreground window.
  Japanese Normal 2 route, easiest-difficulty script and North American target
  remain distinguished. Restricted full-guide retrieval was not bypassed;
  public indexed excerpts serve only as additional corroboration.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BOK-001` | Konami shipped the original US GBA release on 16 September 2003; the cartridge sensor and clock supply distinct external inputs. | Observation | Direct | High | P1, P2 |
| `BOK-002` | Current sensed sunlight differs from retained gun energy; ordinary first purification needs positive current light, not merely a full gun. | Observation | Corroborated | High | P1, P2, S1, S5 |
| `BOK-003` | Outdoor/skylight charging and stored Solar Station withdrawals replenish the gun differently; station stock remains usable without current sun. | Observation | Corroborated | High | P1, S1, S2, V1 |
| `BOK-004` | Local wall taps divert Boks; sight, occlusion and eligible sunlight footprints change the safe route and hostile survival. | Observation | Corroborated | High | P1, S1, S2, S3, V1 |
| `BOK-005` | Fog Castle supplies Knight, a damaging held spread, patrols and a bat-clear gate to a pre-sealed decoy; it does not contain the real Count duel. | Observation | Corroborated | High | S1, S2, S3, S4, V1 |
| `BOK-006` | Holding the ground-dragged coffin blocks running and attacks; release or damage drops it; warning agitation can be calmed with compatible gunfire. | Observation | Corroborated | High | P1, S1, S2, S3, V1 |
| `BOK-007` | Two primed generators start a separate sunlight-scaled purification; resistance weakens beams and held spread restores them until Darkness is exhausted. The tutorial captive does not launch the later bosses' attacks. | Observation | Corroborated | High | S1, S2, S3, S4, V1 |
| `BOK-008` | Clear evaluates time, discoveries, continues and collected charge, awards the Fool Card and returns toward the next route; best rank is optional. | Observation | Corroborated | High | P1, S2, S3, S4, V1 |
| `BOK-009` | Eligible dungeon crystals can release energy-restoring, life-restoring or energy-draining bugs; no random distribution is established. | Observation | Corroborated | Medium | P1, S1, S8, V1 |
| `BOK-010` | Equipped lenses, not Django's independent character level, gain defeated-hostile experience and grow in power/spread; exact EXP and US thresholds remain undisclosed. | Observation | Corroborated | Medium | P1, S3, S6, S7 |
| `BOK-011` | The manual explicitly saves area-entry conditions and Continue returns to the area entry; this is not latest-position suspension. | Observation | Direct | High | P1 |
| `BOK-013` | Excessive sensor exposure can warn, overheat and temporarily disable the gun; the attributed first-game script adds a repeated-overheat cutoff until sunset. Exact native thresholds, pre-clear activation and reset timing are not reproduced. | Observation | Corroborated | Medium | P1, S1, S8 |
| `BOK-012` | Native sensor response, regional coefficients, every restored field, pre-clear heat behaviour and exact zero-light mid-purification response are not reproduced by this research. | Observation | Limited | Medium | P1, S1, S3, S5, V1 |

## Basic data

- Release / origin: Konami Computer Entertainment Japan; US shipment
  16 September 2003. Japanese release preceded it; this record does not replace
  the target with the Japanese speedrunning executable or European 2004 edition.
- Platform or physical form: original one-player English Game Boy Advance
  cartridge with physical solar sensor and configured internal clock;
  structured target `PLAT-GAME-BOY-ADVANCE`. No purchase or present digital availability
  is implied by the historical publisher announcement.
- Puzzle family: real-time system pressure, inventory/fixture dependency and
  ordered dependency sequencing. The ordinary mission is a linked infiltration,
  burden extraction and purification loop, not merely a genre label.
- Primary sources:
  - P1: [Konami USA instruction booklet, preserved scan](https://www.videogamemanual.com/gba/Boktai%20-%20The%20Sun%20Is%20in%20Your%20Hand%20%28USA%29.pdf),
    56 scan pages; printed 7–9 solar input/clock/mission flow and overheat, 11 controls,
    14 difficulty, 20 growing map,
    15 save/Continue, 22 result, 23–25 drag/wall/charge/view actions,
    31 gun parts/shot/spread, 35 stations and 37 crystal occupants. Fetched
    locally because the web PDF reader's size limit rejected the scan; pages
    were rendered and visually read rather than relying on its empty text layer.
  - P2: [Konami's preserved US launch announcement](https://www.nintendoworldreport.com/news/8983/boktai-can-now-be-in-your-hand),
    16 September 2003, publisher testimony about sensor, clock and stealth.
    Its marketing shorthand about Dracula is not accepted as a Fog Castle
    identity or a rule. This is a historical announcement, not a modern shop.
- Secondary sources:
  - S1: [Endz0r's game-script transcription](https://gamefaqs.gamespot.com/gba/589655-boktai-the-sun-is-in-your-hand/faqs/26038),
    29 October 2003, explicitly the easiest-difficulty script. The fetched
    Fog Castle section corroborates tutorial statements, station, Klorofolun,
    coffin, two generators and decoy reveal. The separately public-indexed
    heat passage attributes the repeated-overheat cutoff to sunset; a later
    direct retrieval was restricted and not bypassed. This is documentary evidence,
    not a reproduced Normal 2 threshold or a statement of dawn recovery. It does not establish every
    Normal 2 numerical coefficient or engine implementation.
  - S2: [Oscar C/Devis0r preserved route, ingress](https://www.gameboy-games.com/gba/boktai/sun-is-in-your-hand-walkthrough-1.htm)
    and [return/purification](https://www.gameboy-games.com/gba/boktai/sun-is-in-your-hand-walkthrough-2.htm),
    reachable path, crate tapping, coffin release, generator colours, result
    and Fool Card. These are one walkthrough, not two independent authors.
    No ROM, storefront or unrelated advertisement is treated as an authorised
    game link. Spelling and broad boss naming do not override the decoy reveal.
  - S3: [Taiyoh community Any% route](https://shenef.github.io/Boktai-Speedrunning/boktai/any.html),
    explicit Japanese Normal 2 target and emulator/clock settings. Fog Castle
    path, lens credit, return skylight and two-generator purification corroborate
    structure only; its three-tick kill, EXP total and manipulated sunlight are
    not certified US/hardware values. No speed trick is a required clear.
  - S4: [Thunderbird boss guide](https://gamefaqs.gamespot.com/gba/589655-boktai-the-sun-is-in-your-hand/faqs/29120),
    public indexed Fog Castle passage separates already sealed decoy,
    purification-only battle, two generators and no direct attack. Direct
    retrieval is restricted and was not bypassed or represented as full access.
  - S5: [Thunderbird sunlight FAQ](https://gamefaqs.gamespot.com/gba/589655-boktai-the-sun-is-in-your-hand/faqs/29108),
    public indexed ordinary live-sun requirement and separately described
    final-battle exception. Direct retrieval restricted; no bypass. It does
    not certify the exact native zero-light state machine in this first fight.
  - S6: [RPGamer original review by Michael Beckett](https://archive.rpgamer.com/games/boktai/boktai/reviews/boktairdrev1.html),
    firsthand sensor/stealth account, lens rather than character levelling and
    absent exact EXP display. Numerical ratings are not imported as Atlas data.
  - S7: [community lens account](https://boktai.fandom.com/wiki/Lenses),
    first-game equipped-lens credit, three levels and higher power/spread;
    later-series lens rules are explicitly separated. No exact threshold claim.
  - S8: [Son_Kain's later guide](https://www.neoseeker.com/boktai/faqs/67207-c.html),
    public indexed crystals, typed bugs and post-Fog heat-lesson handoff;
    direct access restricted. Broad claims about skylight safety do not
    override explicit exceptions; this record does not promise invulnerability.
  - V1: [Alexander The Pretty Good, Tutorial](https://www.youtube.com/watch?v=to452iuZCKQ),
    1,131 seconds; inspected sheets 01–11, nine 320×180 cells per sheet,
    ten-second sampling. Fog Castle starts around 02:35; purification around
    14:32; result around 16:00 and post-castle heat dialogue around 17:30.
    Native hardware, sensor provenance, patch and difficulty were not verified.
- Claim IDs: `BOK-001`–`BOK-013`.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: `ACT-008` direct movement and directional shaking;
  `ACT-048` acquire/retain/release one reachable rigid coffin at a controlled
  ground offset, not shoulder-carrying a person; `ACT-131` consume a carried
  permitted item; `ACT-161` aim and fire the solar tool; `ACT-199` collect/equip
  compatible Knight or existing gun parts; `ACT-202` flatten against a wall;
  `ACT-341` open a chest, inspect Otenko panels, draw a local station supply or
  activate the prepared fixture; `ACT-489` deliberate adjacent wall/crate tap.
- Candidate genes: accepted `ACT-756` deliberate physical light exposure and
  `ACT-757` held Solar Charge at an eligible ambient position. One A button has
  context-dependent operations; it is not one identical action in all states.
- Parameters: Control Pad orientation, held A or B, tap versus spread, wall
  contact, rigid burden offset and real sensor exposure; `BOK-002`–`BOK-007`.

### System Behaviour Genes

- Existing gene IDs: `SYS-057` perceived-target pursuit/diversion; `SYS-215`
  directly commanded live combat, rear stun/knockback and attached dark matter;
  `SYS-369` chosen Continue restores the authored area boundary; `SYS-578`
  continuous life loss/restoration and zero-life failure; `SYS-605` authored
  route flags including bat clear; `SYS-1344` local bounded stock refill.
- Candidate genes: accepted `SYS-1615` two-store solar energy protocol;
  `SYS-1616` lethal skylight footprint; `SYS-1617` retained coffin agitation;
  `SYS-1618` resistible two-beam purification; `SYS-1619` dungeon rank/reward;
  `SYS-1620` equipped-lens experience, `SYS-1621` typed crystal occupants and
  `SYS-1622` externally accumulated overheat interruption and qualified repeated
  safety cutoff. P1 documents excessive light over an interval, not merely
  heat from firing; S1 attributes repeated cutoff recovery to sunset. Neither
  an exact threshold nor a native pre-clear activation was reproduced.
- Resolution order: local action/exposure → perception, contact or compatible
  shot/charge response → resource/body/route update; all bats defeated → coffin
  available → persistent dragged return with independent agitation → receiver
  placement and generator priming → positive-sun activation → beam resistance
  and restoration until Darkness depletion → graded reward and story handoff.
- Parameters: no exact damage, agitation period, hidden occupant probability,
  lens threshold, rank cutoff or station cap is certified; `BOK-002`–`BOK-011`.

### Constraint Genes

- Existing gene IDs: `CON-077` directed occlusion-bounded hostile sight;
  `CON-571` thermal readiness, with passive recovery rather than a timed
  active-cooling minigame; `CON-578` finite compatible ammunition, here solar
  energy: an empty gun
  cannot fire, independently of whether current sunlight exists;
  `CON-629` manual saving has declared event exceptions. Hearing a wall tap
  uses a separate stimulus and is not evidence that sight ignores walls.
- Candidate genes: `CON-822` held ground burden prevents running/attack and
  drops on eligible damage; `CON-823` current physical light gates ordinary
  purification start independently of stored weapon energy.
- Scarce strategic resources: life, portable energy and stored station stock;
  route position, temporary safe sight lines and the separate current-light
  opportunity, with excessive sustained exposure adding a separate heat risk.
  No finite life stock or best-rank clear requirement is invented;
  `BOK-002`, `BOK-004`, `BOK-006`, `BOK-007`, `BOK-011`.

### Information Genes

- Existing gene IDs: `INF-125` discovered dungeon terrain, current position
  and authored markers; `INF-179` visible local room/field, threats, pickups,
  coffin and exits. Panning with held R inspects beyond the current framing
  without commanding Django to that location.
- Candidate genes: `INF-534` separately disclosed sunlight, gun energy, life,
  effects, purification Darkness/beam state and result dimensions. Exact
  lens EXP is not visible; a gun gauge is not a current-sun reading. The
  documented OVERHEAT warning is distinct from an empty gun or zero sunlight.
- Claim IDs: `BOK-002`–`BOK-010`.

### Objective Genes

- Existing gene IDs: none for the complete joined extraction/purification
  terminal. `OBJ-014` payload delivery stops too early, and killing the bats
  alone does not purify the captive.
- Candidate genes: `OBJ-307`, secure and extract the decoy, finish the
  separate purification and accept result/reward/successor handoff.
- Success, evaluation and failure: zero Darkness completes purification;
  best rank, no detection and every optional chest are not ordinary gates.
  Zero life offers Continue, not automatic deletion of the campaign. The
  actual Count's surviving speech explains why this is not his final defeat;
  `BOK-005`–`BOK-008`, `BOK-011`.

### Time Genes

- Existing gene IDs: `TIM-003` live movement/combat/beam resistance with
  explicit pause; `TIM-025` the configured real-world clock supplies day/night
  state independently of elapsed-play time and the instantaneous sensor.
- Candidate genes: `TIM-036`, requesting a save retains the current area's
  entry snapshot rather than suspending the latest live position. Native
  field-by-field persistence and clock behaviour under every pause/absence
  path were not tested; `BOK-001`, `BOK-011`, `BOK-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Same virtual position, physical sensor shaded | Expose the calibrated sensor to sunlight | Live Solar Gauge can rise independently of position or stored gun energy | Physical environmental control | BOK-002 |
| Positive sensor, missing gun charge, eligible outdoor/skylight position | Hold the charge request | Gun charge replenishes faster; its reserve remains distinct | Ambient recharge has a position predicate | BOK-003 |
| Zero sensor, nonempty station store | Draw energy at the station | Gun can refill from retained stock without creating sunlight | Dark play and stored charge remain possible | BOK-003 |
| Bok has not seen Django; a compatible wall is reachable | Flatten, tap, then hide behind an occluder | Perceived noise diverts the Bok toward that location | A lure differs from a free global route edit | BOK-004 |
| Sensor-enabled skylight lies across the Bok's path | Lure the eligible Bok across it | The lit footprint harms/destroys it | Real-input-dependent environmental lethality | BOK-004 |
| Bat guard remains at the sealed coffin | Defeat the required bat set | Coffin extraction becomes available | This is not the real Count's free-standing duel | BOK-005 |
| Coffin attached by held A | Request running or ordinary attack | Those actions remain unavailable until release; a qualifying hit drops it | Burden legality is separate from weapon ownership | BOK-006 |
| Coffin warns by shaking | Release, apply a compatible shot/spread, then reattach | Agitation can be calmed and transport resumes | Burden state persists beyond one pickup | BOK-006 |
| Coffin delivered, two generators primed, gun full but Solar Gauge zero | Request ordinary purification start | Stored ammunition does not satisfy the positive-light gate | Delivery and gun charge are insufficient | BOK-002, BOK-007 |
| Positive sunlight and active purification; one beam weakens | Apply compatible held spread to that generator | Beam strength recovers and Darkness depletion can continue | Live resource intervention, not direct tutorial boss attacks | BOK-007 |
| All purification Darkness depleted | Accept closeout and the authored dialogue | Rank dimensions, Fool Card and decoy revelation precede return | Ordinary clear differs from best-rank optimisation | BOK-008 |
| Live movement progressed after entering an area | Request a permitted Save | Persisted state follows the area-entry rule, not the current position | Save is not exact suspension | BOK-011 |
| Stored gun charge remains but sensor exposure has accumulated excessively | Respond to the documented overheat warning | Weapon can temporarily reject fire; repeated safety recovery is separately qualified | Temperature readiness differs from ammunition and current sunlight | BOK-013 |
| Life reaches zero | Choose Continue | Resume from the area-entry checkpoint | Continue differs from keeping the failed live state | BOK-011 |

## Strategic and experiential structure

- Local decision: avoid the current sight line, tap and redirect, spend charge
  on stun/spread or exploit a genuine sunlit footprint. A shot, a stored refill
  and physical exposure change different parts of the state.
- Medium-term planning: conserve enough portable energy for the return and
  generator support; release the coffin before combat or agitation control.
  The station can bridge darkness for gun use but cannot waive the final sun gate.
- Long-term structure: rank encourages cleaner, faster and sufficiently charged
  traversal; lens experience can reward eligible defeats while stealth avoids
  danger. No independently growing Django level is invented.
- Common heuristics: know the two reservoirs, the current solar reading and
  the coffin's warning; ensure real light is available before committing to
  purification. The historical manual's distinction is not replaced with a
  fictional universally usable indoor lamp.
- Failure attribution: visible patrols, light patches and coffin warning can
  explain local failure; hidden lens EXP and undisclosed rank thresholds limit
  exact planning. Save's area-entry semantics require explicit explanation.
- Player-trust factors: hardware/weather dependency is real, not an Atlas
  requirement to buy a copy or a claim of present legal download availability.
- Claim IDs: `BOK-002`–`BOK-012`.

## Replay and variation

- What changes between sessions: clock phase, actual light, exposure, chosen
  patrol timing, shot use, detections, remaining life/energy, continues and rank.
- Randomness or procedural generation: Fog Castle is authored; no random room
  generator or exact crystal-occupant distribution is inferred.
- Multiple viable strategies: avoid, stun, destroy or lure an eligible guard
  into light; use current sunlight or station stock for gun supply. Ordinary
  purification still requires current sunlight and correctly primed generators.
- Typical replay motive: improve dungeon rank and route, not claim completion
  of the entire game from one tutorial. No personal replay/save experiment.
- Claim IDs: `BOK-002`–`BOK-012`.

## Adjacent systems and history

- Direct predecessors: Kojima's stealth background is historical context,
  not evidence that this route inherits Metal Gear Solid's radar/alert phases.
- Variants: Japanese Normal 2 speed routes, easier-difficulty script, North
  American retail target and sunlight-modified recordings remain distinguished.
- Similar games: only the complete-signature scan below determines numerical
  neighbours. Solar flavour does not imply Dyson Sphere Program energy rules.
- Important differences: hauling a sealed hostile is not shoulder-carrying a
  rescued person or holding an inert treasure; the first two-beam decoy
  purification is not a later four-beam boss battle; `BOK-001`–`BOK-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-131`, `ACT-161`, `ACT-199`, `ACT-202`, `ACT-341`, `ACT-489`, `ACT-756`, `ACT-757` | reviewed bounded Fog Castle rules |
| System Behaviour | `SYS-057`, `SYS-215`, `SYS-369`, `SYS-578`, `SYS-605`, `SYS-1344`, `SYS-1615`, `SYS-1616`, `SYS-1617`, `SYS-1618`, `SYS-1619`, `SYS-1620`, `SYS-1621`, `SYS-1622` | reviewed bounded Fog Castle rules |
| Constraint | `CON-077`, `CON-571`, `CON-578`, `CON-629`, `CON-822`, `CON-823` | reviewed bounded Fog Castle rules |
| Information | `INF-125`, `INF-179`, `INF-534` | reviewed bounded Fog Castle rules |
| Objective | `OBJ-307` | reviewed bounded Fog Castle rules |
| Time | `TIM-003`, `TIM-025`, `TIM-036` | reviewed bounded Fog Castle rules |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `556` (`GAME-0001`–`GAME-0556`).
- Exact genome matches: none.
- Tied near matches: `GAME-0339` — Metal Gear Solid (`10 / 44 = 0.227273`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0339` — Metal Gear Solid | `ACT-008`, `ACT-161`, `ACT-202`, `ACT-341`, `ACT-489`, `SYS-057`, `SYS-215`, `SYS-369`, `CON-077`, `TIM-003` | Both use directly controlled movement, tool attacks, wall posture and taps, contextual fixtures, perception-driven diversion, live combat and authored retry under directed sight. Metal Gear Solid’s opening uses conditional Soliton Radar and Alert/Evasion phases to enter the Tank Hangar. Fog Castle instead separates physical sunlight, gun/station stores, a grounded resisting burden and a two-generator purification before rank/reward settlement; no radar or MGS alarm sequence is imported. | Tied near; `10 / 44 = 0.227273` |

- New genes: fifteen additions, twenty-two unchanged definitions reused.
- Classification result: `New gene`.
- Evidence and reasoning: physical sunlight, retained energy, carrying legality
  and separately evaluated purification are not one generic combat action.

### Preserved research notes

- New genes: fifteen additions, twenty-two unchanged definitions reused.
- Classification result: `New gene`.
- Evidence and reasoning: physical sunlight, retained energy, carrying legality
  and separately evaluated purification are not one generic combat action.

## Taxonomy impact

- Registry changes: ACT-756–ACT-757, SYS-1615–SYS-1622, CON-822–CON-823,
  INF-534, OBJ-307 and TIM-036.
- Taxonomy-change record: [TAXONOMY_CHANGE_303](../../../research/taxonomy-changes/TAXONOMY_CHANGE_303.md).
- Candidate terms affected: live environmental input versus reserves,
  generator resistance, sealed burden, lens-owned experience and area-entry save.

## Negative results

- No separate record. Rejected reuse boundaries are documented in the taxonomy
  decision. No previous definition, signature or historical receipt is changed.

## Delta summary

## New facts

- [Observation | Corroborated | High] Stored gun energy does not waive current
  sunlight for ordinary purification; the first captive is a decoy, not the
  later real Count encounter; BOK-002, BOK-005, BOK-007.
- [Observation | Direct | High] Manual saving retains the area-entry state
  rather than the latest position; BOK-011.

## New genes

- [Observation | Corroborated | Medium] Fifteen bounded additions; native
  coefficients, pre-clear heat and complete persistence parity remain untested.

## New combinations

- [Observation | Corroborated | High] No new combination is invented; the
  deterministic complete scan owns proper-subset support.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_303 adds definitions only.

## New questions

- [Hypothesis | Limited | Medium] Authorised native experiments could test
  sensor calibration, the exact zero-light mid-phase response, pre-clear heat,
  each saved field and regional lens/rank thresholds. Contradictory US data
  would reject parity inferred from non-US routes, not rewrite this provenance.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0558 Moss, standalone Meta Quest.
- Optimisation criterion: finish Selection 044 with a modern tracked-input target.
- Expected information gain: coordinate environmental intervention and Quill.
- Backlog impact: stop after this final approved subject and complete batch gates.

## Why this game

- [Hypothesis | Limited | Medium] A physical sensor and transport-to-purification
  loop distinguish this released GBA target from the preceding touch arcade route.
