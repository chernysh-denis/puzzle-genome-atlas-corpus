---
game_id: GAME-0417
slug: sly-cooper-and-the-thievius-raccoonus
game_title: Sly Cooper and the Thievius Raccoonus
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
  system:
    - SYS-063
    - SYS-755
    - SYS-911
    - SYS-933
    - SYS-1106
  constraint:
    - CON-183
  information:
    - INF-410
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Sly Cooper and the Thievius Raccoonus — A Stealthy Approach

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Sly, the hooked cane, Raleigh's swamp, spotlights, signal repeaters and the treasure key are carriers or parameters, not gene names.

## Analysis scope

- Version / ruleset: the original North American English PlayStation 2 retail *Sly Cooper and the Thievius Raccoonus* (`SCUS-97198`, 2002), only the first `Tide of Terror` stage `A Stealthy Approach` after the Police Headquarters prologue. The physical disc revision was not read; the inspected US booklet and two written original-game routes bound the packet. No rule unique to a remaster or the 2024 PS4/PS5 conversion is imported.
- Structured analysis target: `PLAT-PLAYSTATION-2` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: inspect the currently sweeping security light, choose when and where to run, jump, climb or hook across an authored route, strike reachable guards or security fixtures when needed, and use the safe openings between active scan regions to reach and disable the sirens. Cross the moving water-wheel obstacles, break the final glass case, take the treasure key and pass the unlocked exit into Prowling the Grounds.
- Entry and exit: begin when control is given after the van reaches `A Stealthy Approach`; finish only after the treasure key opens the locked exit and Sly enters the successor hub. Seeing the key, collecting optional bottles, breaking one siren or reaching a checkpoint alone does not complete the packet.
- Included: direct movement, ordinary and double jumps, ladders, ropes, hooks and spinning-wheel timing; cane strikes on reachable enemies, sirens and the glass key case; moving spotlight detection and the linked siren disable; visible light footprints and alarm feedback; the one required treasure key and gate; finite lives, lethal water or hostile contact, and passed signal-repeater return anchors. The booklet establishes the rules; the original-game routes establish their placement in this stage.
- Excluded: the Police Headquarters prologue, every optional clue bottle and vault code, the Fast Attack Dive reward, 100-coin extra lives, Lucky Horseshoes and their hit buffers, Master Thief Sprint, later hub key totals, bosses, other episodes, vehicle or turret minigames, collectibles as a completion predicate, PlayStation 3 remaster, PS4/PS5 rewind and quick save, exact guard damage frames, unverified alarm reinforcement and unseen future scan timing.
- Potential scoped modules: the optional twenty-bottle vault and ability reward; the later `Prowling the Grounds` hub's multi-key gates; a separate chase or vehicle stage.
- Direct-play status: no disc, console, emulator, input trace, screenshot, gameplay video or audio was inspected. The original 40-page US instruction booklet was downloaded and visually read at relevant pages; the stage route is corroborated by a contemporary PlayStation 2 guide and an independent route description. This is a source-bounded reconstruction, not a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SC1-001` | The selected original PS2 product is the North American `SCUS-97198` release, while the current store conversion adds rewind and quick save that are outside this packet. | Confirmed | Corroborated | High | I1; P1 |
| `SC1-002` | The first `Tide of Terror` stage proceeds from the cave through spotlights, hooks and rotating water wheels to a cased treasure key and locked exit. | Confirmed | Corroborated | High | R1; R2 |
| `SC1-003` | Sly directly runs, jumps, double-jumps, climbs and grabs route hooks or ropes; cane strikes can break eligible objects or hit enemies. | Confirmed | Direct | High | M1 pp. 4, 10–11; R1 |
| `SC1-004` | Entering a working spotlight turns it red and sounds its linked alarm; destroying the red siren disables that local security system. | Confirmed | Corroborated | High | M1 p. 11; R1; R2 |
| `SC1-005` | The player can read present searchlight coverage and siren position, but the inspected sources do not establish an exact preview of future sweeps or a numeric guard-suspicion meter. | Observation | Corroborated | High | R1; R2; M1 p. 11 |
| `SC1-006` | A passed signal repeater becomes the return point after a lost finite life; the booklet starts Sly with five lives and says water costs one. | Confirmed | Direct | High | M1 pp. 12, 17; R1; R2 |
| `SC1-007` | Breaking the key's glass case and taking the treasure key permits the locked stage exit; clue-bottle vault completion is optional for that exit. | Confirmed | Corroborated | High | M1 pp. 14, 17; R1; R2 |
| `SC1-008` | The precise disc revision, frame-level spotlight detection boundary, guard reaction timing and checkpoint reset fields remain unverified without direct execution. | Observation | Limited | High | M1; R1; R2 |

## Basic data

- Release / origin: Sucker Punch Productions and Sony Computer Entertainment, original North American PlayStation 2 release in 2002; `SCUS-97198` is a product identity, not a checksum of an inspected disc.
- Platform or physical form: licensed North American English PlayStation 2 retail disc; manual rules and first-stage written routes. The modern Sony store destination is a legal product link, not evidence that its added convenience features existed in 2002.
- Mechanical families: real-time system pressure (`FAM-010`) and ordered dependency sequencing (`FAM-017`). The player times a continuous moving security-and-platform route, then obtains one required key before successor access.
- Sources accessed 2026-09-27:
  - **M1** — [original US PlayStation 2 instruction booklet scan](https://www.videogamemanual.com/PS2/Sly%20Cooper%20and%20the%20Thievius%20Raccoonus%20%28USA%29.pdf), printed pp. 4, 10–18, visually inspected; 40 PDF pages, SHA-256 `13dc8083251543419c925326392b4c9e369aa5bfdc797e7beb53adeb94ff3684`. It is a scan of publisher-authored content hosted by a manual archive, not a publisher site. Page 11 describes alarms; p. 17 describes the key and signal repeaters.
  - **R1** — [MasterVG782's original PlayStation 2 guide](https://gamefaqs.gamespot.com/ps2/561378-sly-cooper-and-the-thievius-raccoonus/faqs/20764), `A Stealthy Approach`, for the authored sequence, two security sections, checkpoint, case, key and exit. This player route is not direct play by the Atlas.
  - **R2** — [StrategyWiki's first-stage route](https://strategywiki.org/wiki/Sly_Cooper_and_the_Thievius_Raccoonus/A_Stealthy_Approach), independently corroborating spotlight-red alarm feedback, siren disable, rotating wheels, checkpoint and final key.
  - **I1** — [GameFAQs PlayStation 2 release record](https://gamefaqs.gamespot.com/ps2/561378-sly-cooper-and-the-thievius-raccoonus/data), for US product serial and original release identity.
  - **P1** — [official PlayStation product page](https://store.playstation.com/en-us/concept/10010296/), for a legal current destination and its explicit separation of the converted PS4/PS5 version's rewind, quick save and filters from the PS2 original.
- Claim IDs: `SC1-001`–`SC1-008`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: steer Sly along the fixed route, time jumps across moving wheel gaps, climb a ladder or rope and grab a reachable hook. These are direct avatar moves, not assigned waypoint orders.
- `ACT-161`: swing the currently held cane against a reachable guard, red siren or final glass key case. The case's break and any alarm disable are system results rather than separate attack inputs.
- Claim IDs: `SC1-002`, `SC1-003`, `SC1-004`, `SC1-007`.

### System Behaviour Genes

- `SYS-1106`: while its siren remains intact, each moving spotlight detects contact and alarms; smashing the linked siren disables that local scan system. No unverified reinforcement rule is inferred.
- `SYS-755`: a legal cane blow breaks the eligible glass case, exposing its key; siren destruction also uses a damageable fixture, but `SYS-1106` owns the linked scan shutdown.
- `SYS-063`: contacting the exposed key records carried key state, which the compatible locked exit consumes when the route is opened.
- `SYS-933`: crossing a signal repeater updates the current within-level return anchor for a later finite-life failure.
- `SYS-911`: when an unprotected lethal collision or water failure costs one life, the controlled body returns to the current anchor if the stock remains. Exact transient object reset at that point is unmeasured.
- Resolution order: observe a sweep → cross outside its active region or trigger the siren → reach and smash the linked siren → pass a signal repeater → time movement over hooks and rotating wheels → break the key case → take the key → open the exit. A lethal failure instead consumes one life and returns to the latest passed repeater while eligible.
- Claim IDs: `SC1-002`–`SC1-008`.

### Constraint Genes

- `CON-183`: a finite, recoverable life stock bounds how many lethal route failures can be retried before the current run fails. Five starting lives are a product parameter, not a separate gene; optional extra lives and shields are outside scope.
- Claim IDs: `SC1-006`.

### Information Genes

- `INF-410`: present spotlight footprints, their red alarm change and the physical siren expose current security risk and its reachable controller. No precise future-sweep schedule is supplied.
- Claim IDs: `SC1-004`, `SC1-005`.

### Objective and Time Genes

- `OBJ-026`: make the locked successor exit traversable by obtaining its required key, then take Sly into `Prowling the Grounds`. A vault reward is not an alternate success condition for this packet.
- `TIM-003`: spotlights, rotating wheels and threats progress in real time while Sly moves and chooses a crossing interval; there is no turn handoff or paused tactical preview.
- Claim IDs: `SC1-002`, `SC1-004`, `SC1-007`.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A searchlight and red siren are active | Wait for the beam to pass and cross outside its footprint | The local alarm stays quiet | visible timing before commitment | `SC1-004`, `SC1-005` |
| The same section is still live | Deliberately enter an active beam | The light changes red and sounds the siren; this is not automatically a stage failure | detection without invented reinforcement | `SC1-004` |
| The linked siren is reachable | Hit it with the cane | The siren breaks and linked security becomes inactive for the section | fixture-controlled risk removal | `SC1-003`, `SC1-004` |
| The path reaches a signal repeater | Pass its position, later lose one life to water | The eligible attempt returns at that passed anchor rather than from the stage beginning | finite-life checkpoint response | `SC1-006` |
| Rotating wheel gaps cross Sly's path | Time a jump or wait for a safe wheel section | Sly lands on a traversable segment or risks a fall; no grid turn is consumed | live traversal timing | `SC1-002`, `SC1-003` |
| The required key is behind glass | Strike the case, contact the exposed key and approach the locked gate | The case breaks, key is carried and the successor exit opens | required key-gate chain | `SC1-007` |
| The key-gated passage is open | Enter the exit marker | Control transfers to `Prowling the Grounds`; the selected stage has been passed | terminal scope boundary | `SC1-002`, `SC1-007` |

## Strategic and experiential structure

- Local decision: wait until a moving beam leaves a crossing, or route around its footprint to reach the linked red siren without sounding it.
- Medium-term planning: carry enough lives through the water and rotating-wheel sections; a passed repeater lowers the cost of later failed timing.
- Long-term structure: repeatedly neutralise local security and traverse authored obstacles to acquire one progression key and unlock the following hub.
- Failure attribution: a red spotlight makes detection legible; a fall or hostile hit costs the limited stock. The sources do not prove exact frame-level hitboxes or siren reset after a checkpoint retry.
- Player-trust factors: the beam footprint and siren are visible; the route does not require a hidden bottle-code reward to pass.
- Claim IDs: `SC1-002`–`SC1-008`.

## Replay and variation

- The authored route, siren positions, key case and required exit persist; spotlight phase and player timing vary without making a procedural map.
- A player may collect optional clue bottles and open the vault, but this packet deliberately tests the shortest supported key-and-gate route without that ability reward.
- The source packet does not establish a numeric guard reaction delay, future beam pattern preview or exact checkpoint restore fields; direct play could refine those parameters without silently changing the admitted genes.

## Adjacent systems and history

- *Tom Clancy's Splinter Cell* also treats exposure and security as route risk, but its illumination-weighted suspicion, body concealment and mission-data gates are not Sly's binary visible spotlight/siren passage.
- Original *Crash Bandicoot* and *Sonic the Hedgehog* provide finite-life checkpoint precedents; Sly's signal repeater is passed rather than a breakable crate or struck lamppost.
- The modern PlayStation conversion adds rewind and quick save. Those cannot be projected backward into the 2002 PS2 signature.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161` | jump, climb, hook, cane target |
| System Behaviour | `SYS-063`, `SYS-755`, `SYS-911`, `SYS-933`, `SYS-1106` | key-gate use, case break, life return, signal repeater, scan alarm |
| Constraint | `CON-183` | finite starting lives |
| Information | `INF-410` | current beam, siren and alarm state |
| Objective | `OBJ-026` | reach successor through the key-gated exit |
| Time | `TIM-003` | live security and wheel movement |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `416` (`GAME-0001`–`GAME-0416`).
- Exact genome matches: none.
- Tied near matches: `GAME-0360` — Space Invaders (`5 / 20 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Space Invaders (`GAME-0360`) | direct avatar movement and aimed strikes, finite-life body return and stock, continuous time | Sly traverses an authored 3D route around moving security beams, disables local sirens and carries a key through a locked exit; Space Invaders holds a fixed shooting base against an advancing formation, cover erosion and score pressure without stealth, checkpoints or a key gate | Near, `0.250000` |

## Taxonomy impact

- [`TAXONOMY_CHANGE_155`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_155.md) admits `SYS-1106` and `INF-410` for the local moving-scan/alarm boundary; nine genes are reused. No earlier genome is changed.

## Negative results

- `SYS-373` rejected: the moving spotlight raises a siren when crossed; no accumulating multi-cue suspicion meter is documented for this stage.
- `SYS-645` rejected: siren detection does not irreversibly convert the entire job into a lasting loud phase.
- `SYS-888` rejected: the sources establish a visible scan and a smashable siren, not a brief interception countdown after one guard spots Sly.
- `INF-298` rejected: the lights and fixture are world-visible, not avatar-centred directional suspicion indicators.
- Optional clue bottles, vault code, ability page, 100-coin life award and Lucky Horseshoe buffer rejected from the selected success route, not claimed absent from the full game.

## Delta summary

An authored PS2 stealth-platform route ties readable moving scan footprints to a destructible local alarm, then converts a broken case into a carried key that opens the successor passage. The two local security boundaries are new; direct traversal, cane strikes, breakable objects, finite-life checkpoint return, key consumption, location objective and live timing transfer from prior games.

## New facts

- [Confirmed | Corroborated | High] The first stage's locked successor route requires its treasure key but not the optional twenty-bottle vault (`SC1-007`).
- [Confirmed | Direct | High] Signal repeaters mark within-level returns after a lost finite life (`SC1-006`).

## New genes

- [Observation | Corroborated | High] `SYS-1106` isolates linked spotlight/siren risk and its local disable; `INF-410` isolates the presently visible scan footprint and alarm feedback.

## New combinations

- [Observation | Limited | High] No new verified combination is claimed from one stage's conjunction alone; existing proper-subset validation remains authoritative.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_155` records the two boundaries and explicitly excludes generic suspicion, permanent stealth-to-loud conversion and optional vault progression.

## New questions

- Which exact PS2 disc revision and frame-level scan collision rule produce the visible red warning?
- Which transient siren, guard and optional collectible states reset when a life is lost after each repeater?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0418` *FTL: Faster Than Light*, only after this unit's validation, local commit and Goal stop window.
- Optimisation criterion: move from one continuous authored stealth route to a branching ship encounter with subsystem and crew decisions.
- Expected information gain: test whether threat telegraphing, discrete jumps and continuous crew/system pressure form separable gene boundaries.
- Backlog impact: preserve the approved `GAME-0418`–`GAME-0432` order; do not start another subject in this unit.

## Why this game

- [Hypothesis | Corroborated | Medium] This classic console route contrasts Advance Wars' whole-army day with uninterrupted local detection and traversal, while a named first-stage exit keeps the mechanical scope reproducible.
