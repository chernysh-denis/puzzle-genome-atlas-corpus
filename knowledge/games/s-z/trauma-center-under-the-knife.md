---
game_id: GAME-0471
slug: trauma-center-under-the-knife
game_title: 'Trauma Center: Under the Knife'
analysis_status: reviewed
reviewed: 2026-10-02
combination_ids: []
gene_ids:
  action:
    - ACT-621
    - ACT-622
  system:
    - SYS-1228
    - SYS-1229
    - SYS-1230
  constraint:
    - CON-068
    - CON-740
  information:
    - INF-268
    - INF-447
  objective:
    - OBJ-267
  time:
    - TIM-003
---

# Game: Trauma Center: Under the Knife — first Standard Procedure operation

Use the [canonical vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The named patient, wound and fragment counts, five-minute limit and DS stylus are scoped parameters, not universal gene definitions.

## Analysis scope

- Version / ruleset: original English Nintendo DS *Trauma Center: Under the Knife*, first story operation, `Standard Procedure 1` (`1-1` in contemporary guides), treating Kevin Turk's injured right upper arm. The Nintendo European product page establishes the DS stylus game and timed surgery, while the English operation transcript and two contemporary DS routes establish this specific sequence. The exact North American cartridge revision and regional rule parity were not inspected. This is not Wii *Second Opinion*, *Under the Knife 2* or the entire campaign.
- Structured analysis target: `PLAT-NINTENDO-DS` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: read the current nurse instruction and visible wound, select the appropriate surgical icon, trace or drag the stylus over the correct region, observe whether the wound, shard and patient state changed, then choose the next eligible instrument before the operation clock or patient condition fails.
- Entry: first control inside the opening operation after its report, with two outer lacerations and two visible outer glass shards. The source transcript gives a five-minute operation limit; a contemporary route reports starting vitals of 80, but exact cartridge behaviour was not measured here.
- Positive terminal / evaluation: after the external cuts are sutured, outer shards removed and treated, guided incision made, inner shards removed and treated, close the incision with suture, gel and full-length bandage to reach `OPERATION SUCCESSFUL` with the patient viable before the limit. Three inner shards are reported by two contemporary routes. The game may grade execution separately; no rank tier is required for this bounded success.
- Negative terminal and partial result: deadline expiry or collapse of patient vitals prevents success. Wrong extraction direction, a failed guided incision or an incomplete bandage is rejected or costs precision; the sources do not establish exact damage amounts or that every individual mistake immediately ends the operation.
- Included: selecting the available needle, forceps, gel, scalpel and bandage; zigzag suturing; gripping, withdrawing and depositing glass in the tray; treating resulting small cuts; gel-prepared guided incision; exterior/interior camera transition; wound and patient-vital feedback; final closure; live operation clock and the assistant's current instruction.
- Excluded: stabilizer syringe, ultrasound, laser, tumors, Healing Touch, later GUILT procedures, story conversations outside this operation, Wii control mapping, later ports, grading thresholds, high-rank optimisation, multiplayer and any claim that these simulated gestures are real medical advice.
- Potential scoped modules: later tumor excision, a separate operation with the syringe or Healing Touch, and a directly measured rank formula. None is flattened into this first operation.
- Direct-play status: no DS cartridge, console, executable, touch trace, screenshot, gameplay video or audio was inspected. Nintendo's product description is publisher-supplied overview; the operation text is a third-party transcription and the routes are first-hand written accounts. Exact input tolerances, vital-loss rates and timer pause behaviour remain unmeasured. The illustration is original and schematic, not game capture.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TC-001` | The original Nintendo DS game uses a stylus and selectable tools in timed operations. | Confirmed | Direct | High | P1 |
| `TC-002` | The first operation's report requires suturing lacerations and extracting glass, with a displayed five-minute limit. | Observation | Corroborated | High | S1, S2 |
| `TC-003` | Outer lacerations are sutured first; forceps withdraw visible glass toward its entry side and the fragments are deposited in a tray before gel treats the small cuts. | Observation | Corroborated | High | S1, S2, S3 |
| `TC-004` | Gel prepares the marked incision; the scalpel follows its guide, exposing more fragments; after inner treatment the field closes with suture, gel and full-length bandage. | Observation | Corroborated | High | S1, S2, S3 |
| `TC-005` | Incorrect tool movement can fail a local step, and patient vitals and remaining time constrain the attempt; exact error penalties were not measured. | Observation | Limited | Medium | S1, S2, S3 |
| `TC-006` | The operation's success announcement follows completion of the staged treatment, not mere removal of the initially visible two shards. | Observation | Corroborated | High | S1, S2 |

## Basic data

- Release / origin: Atlus's original 2005 Nintendo DS game, English first operation; Nintendo's cited European page dates that market's release to 28 April 2006 and does not prove every English cartridge has identical inputs.
- Platform or physical form: Nintendo DS game card with lower-screen stylus control. The operation transcript is a reconstruction, not a local cartridge test.
- Mechanical family: `FAM-017` ordered dependency sequencing for exterior care, opening, inner extraction and closure; `FAM-010` real-time system pressure for the operation clock and patient condition.
- **P1**: [Nintendo UK's Nintendo DS product page](https://www.nintendo.com/en-gb/Games/Nintendo-DS/Trauma-Center-Under-the-Knife-273476.html), publisher-provided stylus, instruments, time and rankings overview (checked 2026-10-02).
- **S1**: [Original DS English operation-text transcription](https://gamefaqs.gamespot.com/ds/922120-trauma-center-under-the-knife/faqs/72051), first Kevin Turk report and operation through success (checked 2026-10-02). This is not an independently inspected cartridge or official manual.
- **S2**: [Contemporary DS Standard Procedure 1 route](https://gamefaqs.gamespot.com/ds/922120-trauma-center-under-the-knife/faqs/46450), wound counts, stylus path, shard tray and final bandage (checked 2026-10-02).
- **S3**: [Independent contemporary DS operation route](https://gamefaqs.gamespot.com/ds/922120-trauma-center-under-the-knife/faqs/43529), patient chart and failed-extraction guidance (checked 2026-10-02).
- Claim IDs: `TC-001`–`TC-006`. No audiovisual inspection or direct play.

## Mechanical decomposition

### Action Genes

- Add `ACT-621`: select a currently available surgical instrument and trace its addressed tissue gesture; the needle's zigzag, gel rub, guided scalpel cut and final bandage stroke are different parameters, not separate input-domain genes (`TC-001`, `TC-003`, `TC-004`).
- Add `ACT-622`: grip a visible shard with forceps, drag it along an acceptable withdrawal line and deposit it in the tray; removing the shard from the body without depositing it is not the complete manipulation (`TC-003`).

### System Behaviour Genes

- Add `SYS-1228`: resolve instrument-specific path contact into local wound, incision, gel or closure state; a decorative stylus mark alone changes nothing (`TC-003`, `TC-004`).
- Add `SYS-1229`: reveal the inner field only after exterior preparation, then return to the outer incision for final closure after the inner shards and cuts are handled (`TC-004`, `TC-006`).
- Add `SYS-1230`: maintain the patient's own vital condition separately from wound count and time; failed or harmful treatment can reduce it, while eligible care can stabilize it. Do not assert exact loss or recovery amounts for this unplayed cartridge (`TC-005`).

### Constraint Genes

- Reuse `CON-068`: a five-minute operation allowance terminates an unfinished attempt on expiry (`TC-002`).
- Add `CON-740`: the current stage, tool, target and path must agree for a surgical step to count; the forceps need the entry-consistent withdrawal and tray, incision follows its marked line, and bandage covers the whole closure (`TC-003`–`TC-005`).

### Information Genes

- Reuse `INF-268`: the assistant exposes the current instrument and step, then acknowledges treatment before giving the next instruction; she does not preview all later missions (`TC-003`, `TC-004`).
- Add `INF-447`: the active field shows wound and fragment positions, selectable tools, incision guide, vital status and clock, allowing local treatment choices without revealing exact future penalties (`TC-001`–`TC-005`).

### Objective Genes

- Add `OBJ-267`: complete the named staged first operation with all required outer and inner treatment and final closure while patient condition and time remain viable; a high score is optional (`TC-002`, `TC-004`, `TC-006`).

### Time Genes

- Reuse `TIM-003`: the operation clock and patient state continue under real-time stylus control; the sources do not establish identical tick behaviour during every dialogue line (`TC-001`, `TC-002`, `TC-005`).

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Two outer lacerations and two lodged outer shards are visible | Select needle and zigzag across both cuts | The cuts become sutured and the assistant requests forceps | current tool/gesture and staged acknowledgement | `TC-003` |
| One outer shard remains lodged | Grip it with forceps, withdraw toward its entry side and drop it in the tray | That shard is removed; a failed withdrawal or wrong drop does not complete this step | directed object extraction, not an automatic pickup | `TC-003`, `TC-005` |
| Both outer shards are out and small cuts remain | Rub eligible cuts with antibiotic gel | The exterior wounds are treated and an incision outline appears | local treatment precedes deeper access | `TC-003`, `TC-004` |
| The guide line is visible on the arm | Apply gel to the marked region and trace the line with scalpel | A valid cut opens the inner field; an inaccurate trace is rejected | prepared, guided incision | `TC-004`, `TC-005` |
| The inner field exposes three reported shards | Extract each with forceps and treat each resulting cut | The required hidden-object treatment is complete; the view returns outward | conditional phase change after full inner care | `TC-004`, `TC-006` |
| The incision remains open | Suture, apply gel, then bandage its full length | The operation reports success if patient condition and time remain viable | closure sequence and terminal | `TC-004`–`TC-006` |

## Strategic and experiential structure

- Local decision: match the visible wound or fragment to the currently admissible instrument and trace accurately rather than making an unrelated stylus motion.
- Medium-term planning: finish the exterior, expose and treat the inner shards, then close the incision while conserving time and patient condition.
- Long-term structure: stop at this operation's success or failure; later medical tools and the story's Healing Touch do not enter the packet.
- Common heuristic: follow the assistant's current instruction, pull shards along their entry direction, treat the residual cut, and cover the full final incision.
- Failure attribution: a wrong path gives local rejection and the visible clock/vitals constrain retries, though exact penalty amounts are not measured.
- Player-trust factor: the analysis treats these as stylus-game rules, not medical guidance, and does not promise a specific score rank.

## Replay and variation

The prescribed order and patient case are authored. Stylus path accuracy, delays and local errors vary between attempts, affecting available time and result quality. These inputs are not proof of randomly generated wounds, a different initial shard count or an unlocked later tool.

## Adjacent systems and history

`GAME-0434` *Cooking Mama* also asks for prompted touch gestures, but its state is a dish assessed across food-preparation minigames. This packet treats an injured patient through a phase-gated surgical field with tool-specific wound and shard consequences, a live patient condition and a terminal operation clock. `GAME-0370` *Theme Hospital* routes patients through staffed institutional diagnosis and rooms rather than directly tracing a procedure on one patient's tissue. Neither comparison justifies inheriting their recipe or hospital-operation genes.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-621`, `ACT-622` | selected surgical tool, touch path and shard tray |
| System Behaviour | `SYS-1228`, `SYS-1229`, `SYS-1230` | tissue response, phase, patient condition |
| Constraint | `CON-068`, `CON-740` | five-minute limit and tool/path eligibility |
| Information | `INF-268`, `INF-447` | assistant guidance, visible field and vitals |
| Objective | `OBJ-267` | viable completed operation |
| Time | `TIM-003` | live stylus procedure |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `470` (`GAME-0001`–`GAME-0470`).
- Exact genome matches: none.
- Tied near matches: `GAME-0434` — Cooking Mama (`2 / 16 = 0.125000`).
- Supported combination subsets: none.
- Scan date: 2026-10-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0434` *Cooking Mama* | `INF-268` and `TIM-003` give current-step guidance during live stylus work. | Cooking Mama prepares and scores a dish through prompted food gestures; this operation changes a patient's tissue and vital condition, reveals an inner field, transfers shards and requires viable final closure. | Sole tied-near maximum, `0.125000`; not an exact or verified-combination match. |

## Taxonomy impact

`TAXONOMY_CHANGE_208` admits eight source-bounded surgical input, response, eligibility, display and terminal boundaries while reusing the fixed deadline, current instruction and real-time clock. Earlier signatures and verified combinations remain unchanged.

## Negative results

- `ACT-211` requires a compatible carried medical item addressing an already disclosed body-region wound; this first DS procedure uses on-screen surgical instruments whose traced geometry and forceps tray transfer are part of action acceptance.
- `ACT-572` changes a food-preparation state within a cooking minigame. A similarity in touch hardware does not make patient treatment a food/utensil preparation gesture.
- `SYS-1138` settles a sequence of separately assessed recipe steps; the operation's interior reveal and final closure depend on treated wounds and fragments, not a cooking-step grade.
- `SYS-578` describes an avatar's run health; the monitored vital quantity here belongs to a patient under the player's care.

## Delta summary

## New facts

- [Observation | Corroborated | High] The first original-DS procedure requires treating outer wounds and glass, exposing the inner fragments and closing the surgical opening before success (`TC-002`–`TC-006`).

## New genes

- [Observation | Corroborated | Medium] Eight new Active boundaries isolate addressed surgical gestures, shard transfer, tissue and vital response, staged access, tool/path legality, live clinical display and operation completion.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_208`; no earlier signature changed.

## New questions

- What exact vital loss, recovery and tool-use tolerances would an original-DS touch trace establish?
- Does dialogue freeze the countdown in every instance in this cartridge revision?
- Does the first operation's ranking formula vary by original regional release?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0472` *Sonic Adventure*, original Dreamcast.
- Optimisation criterion: alternate touch surgery with fast 3D traversal on a different platform, preserving the approved cross-platform order.
- Expected information gain: distinguish route, speed, rings and hazard recovery from one timed clinical procedure.
- Backlog impact: retain the other approved subjects; begin only after this unit's gates, one local commit and the Goal stop window.

## Why this game

- [Hypothesis | Limited | Medium] A specific first operation tests whether input geometry, treatment state, staged access and patient survival require separate genes instead of being collapsed into a broad stylus-minigame label.
