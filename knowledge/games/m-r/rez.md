---
game_id: GAME-0526
slug: rez
game_title: Rez
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids: []
gene_ids:
  action:
    - ACT-161
    - ACT-190
    - ACT-691
  system:
    - SYS-215
    - SYS-1410
    - SYS-1411
    - SYS-1507
    - SYS-1508
    - SYS-1509
    - SYS-1510
    - SYS-1511
  constraint:
    - CON-782
    - CON-808
  information:
    - INF-510
    - INF-511
  objective:
    - OBJ-297
  time:
    - TIM-003
---

# Game: Rez

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Buttons, eight locks, the form names and variant cutoffs are parameters.

## Analysis scope

- Version / ruleset: original English North American PlayStation 2 disc,
  SLUS-20344, released in January 2002. Standard single-player Play Mode,
  Area 1, with default controls.
- Structured analysis target: PLAT-PLAYSTATION-2. One ordinary Area 1
  attempt on a fresh profile, starting in First Form before the initial
  wave with no carried Overdrive.
- Primary decision loop: follow the advancing corridor while aiming across
  hostiles, missiles and support nodes. Choose when to release a pending
  volley, how much of a volley to assign to a Network Opening and when
  to spend a collected Overdrive charge. Keep enough form levels to
  survive the varying firewall patterns.
- Entry: select Area 1 in Play Mode with no prior clear and enter first
  ordinary control. Exit: defeat the Earth firewall by attacking its
  exposed targets, settle the three result percentages and see Area 2
  available at subsystem selection. Stop before Area 2 control. A hit in
  Zero Form terminates an unsuccessful attempt.
- Included: imposed route and phase-specific viewing bounds, acquisition
  and release, shootable missiles and support, Network Openings,
  player forms, the separate Overdrive supply, first firewall variants
  and the standard successful result. Missed openings are permitted.
- Excluded: already-evolved replays and form carryover, memory-card I/O,
  precise boss-rank cutoffs, damage and timing constants, timeout
  self-destruction as a positive terminal, later areas, Travelling,
  Score Attack, Direct Assault, Beyond and optional vibration hardware.
  Audio and visual responses to actions are described without inferring
  input judgement windows or native quantisation.
- Direct-play status: no disc, console, emulator, audio or video was run.
  Sega's printed North American manual supplies the rules. Published PS2
  play accounts and written route notes supply observed examples. The
  route guide based on Dreamcast play is corroboration only. Exact disc
  checksum and original PS2 boss-variant cutoff behavior are unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| RZ-001 | Sega's US/Canada booklet and the North American product record establish the original English PS2 target SLUS-20344. | Confirmed | Corroborated | High | P1, P2, P3 |
| RZ-002 | The rail determines body position. The player aims and changes perspective within the available phase view, with broader coverage at the firewall. Incoming missiles must be shot to prevent contact. | Confirmed | Direct | High | P1 pp. 6–7, 11 |
| RZ-003 | Default Cross gives a quick aimed shot or holds acquisition for a released volley. The pending limit is eight. An acquisition mark precedes the shot and is not damage. | Confirmed | Corroborated | High | P1 pp. 9–10, S1, S2 |
| RZ-004 | A Password Protector reveals the Network Opening. The latter takes eight hits, obtainable from one full acquisition on the same opening. Successful openings change layers and contribute to Analyzation. Missing one reduces that measurement without making an ordinary first-area clear impossible. | Confirmed | Corroborated | High | P1 pp. 8, 10–11, S2, S3 |
| RZ-005 | Weapons collect supported nodes after destroying certain carriers. Progress nodes contribute one or three segments toward a form rise. Taking damage removes one form level; a hit in Zero Form ends the attempt. | Confirmed | Direct | High | P1 pp. 12–14, S1 |
| RZ-006 | A red node adds one Overdrive. Default Circle spends a charge to strike eligible on-screen threats automatically for a bounded interval. Ordinary firing requires no Overdrive. | Confirmed | Corroborated | High | P1 pp. 6–7, 9, 13–14, S1, S2 |
| RZ-007 | The Earth firewall has Mega, Giga and Tera variants selected from the regular enemy shoot-down proportion. The cutoffs and equality rules are not established on the North American disc. | Observation | Corroborated | Medium | S2, S3 |
| RZ-008 | The Earth fight has successive exposed shell or structure targets and its own attacks. Defeating it in ordinary Play Mode settles Area 1 and admits Area 2. | Confirmed | Corroborated | High | P1 pp. 8, 10–11, S2, S3 |
| RZ-009 | The reticle reports pending locks; Progress and Overdrive each have a gauge. On clearance, Analyzation, Shot Down and Support Item are distinct completion measures. | Confirmed | Direct | High | P1 pp. 8–9 |
| RZ-010 | Shoot and acquisition effects join the evolving soundtrack. The PS2 play accounts describe no beat-accuracy input judgement or extra reward for pressing in time. | Observation | Corroborated | Medium | S1, S4 |

## Basic data

- Release / origin: United Game Artists and Sega of America, North American
  PlayStation 2, January 2002. Sega's catalog also records the Japanese 2001
  release on PS2 and Dreamcast. That date does not identify this disc.
- Platform or physical form: original PlayStation 2 single-player disc,
  default DualShock 2 input.
- Mechanical family: real-time system pressure. Hostiles, missiles and
  openings arrive or leave reach while the player decides when to fire.
- Sources accessed 2026-11-17:
  - **P1** — [Sega's North American PS2 instruction booklet](https://device.report/m/9edd46a2fe33c5dbe8b346b33dbb108e7f3369200e41f8e9ce079166b9aa4f1c), original scan transcribed by the archive, printed pp. 6–15 and warranty. Button symbols and the printed view-angle OCR were cross-checked with the written PS2 play notes; an exact angle is not used as a claim.
  - **P2** — [Sega catalog for the original game](https://www.sega.jp/game/ps2/?page=7) and [SEGA annual report](https://www.segasammy.co.jp/cms/wp-content/uploads/pdf/ja/ir/sega_annual_tuuki_2002.pdf), United Game Artists entry. These establish platform and studio, not North American disc identity.
  - **P3** — [North American release and product code](https://gamefaqs.gamespot.com/ps2/517868-rez/data/1000) and [disc configuration read-out](https://github.com/libretro/RetroArch/issues/13245), Rez product row and BOOT2 excerpt. These corroborate SLUS-20344; no local disc inspection is claimed.
  - **S1** — [Jeff Gerstmann's US PS2 play account](https://www.gamespot.com/reviews/rez-review/1900-2838815/), acquisition, forms, Overdrive and audio feedback. The archived page dates the posting to 2006.
  - **S2** — [FFKonoko's original PS2 play guide](https://gamefaqs.gamespot.com/ps2/517868-rez/faqs/56850), sections 2–4, Area 1 and Earth. The author qualifies the exact cutoffs and reports possible boss auto-destruction, outside the active-defeat route.
  - **S3** — [iamradiox's original-version route notes](https://gamefaqs.gamespot.com/ps2/517868-rez/faqs/51611), Area 1 and Secrets. The author primarily used Dreamcast; only converging qualitative behavior is accepted.
  - **S4** — [Gamebits PS2 review](https://www.gamebits.net/ps2/rez/), archived 2002 account of action feedback, which corroborates that muted play need not change input eligibility.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-161`: fire a quick aimed shot at one virus or interceptable missile.
- Reuse `ACT-190`: trigger an available Overdrive without supplying a specific
  target or giving up ordinary aiming.
- Reuse `ACT-691`: keep acquisition held while sweeping eligible threats, then
  release it to commit the volley.
- Claim IDs: RZ-002, RZ-003, RZ-006.

### System Behaviour Genes

- Reuse `SYS-215`: resolve ordinary hits, enemy direct harm and shots into
  a missile before its arrival. Cross timing is against reachable threats.
- Reuse `SYS-1410`: advance the authored rail even while the player collects
  locks. Perspective input moves the aiming view rather than trading position
  for a dodge.
- Reuse `SYS-1411`: place the eligible hostile targets into the pending
  volley, then resolve aimed attacks after release.
- New `SYS-1507`: open a layer only when destroying the carrier exposes the
  separate gate and enough impacts hit the gate before it leaves reach.
  Multiple locks on the same gate can supply the required impacts.
- New `SYS-1508`: designated enemies drop shootable nodes, collected by
  hitting them with the existing attack. A drop is not yet a collected item.
- New `SYS-1509`: progress fills to an evolution threshold, but a landed hit
  immediately decreases the form one level. A hit below the recoverable
  ladder ends the attempt. No remaining-partial-progress formula is asserted.
- New `SYS-1510`: spend one banked Overdrive to run a temporary stream of
  automatic strikes against eligible visible threats.
- New `SYS-1511`: select the firewall's variant from the measured kill
  proportion at the phase boundary, independently of analyzed openings.
- Resolution order: rail exposure → acquire and release or use Overdrive
  → attacks, missiles, opening hits and drops → node collection or damage
  → form and charge changes → firewall selection → clear and settlement.
  This is causal order, not a claim about frame scheduling.
- Claim IDs: RZ-002–RZ-008.

### Constraint Genes

- Reuse `CON-782`: no more than eight pending locks fit at once. Distinct
  eligible enemies share the budget, while one opening can use all eight.
- New `CON-808`: the current phase limits the aiming panorama. Changing
  perspective broadens which threats can be targeted without granting body
  positioning or collision avoidance.
- Claim IDs: RZ-002–RZ-004.

### Information Genes

- New `INF-510`: the visible pending count and the separate evolution
  and Overdrive indicators answer different firing and survival questions.
- New `INF-511`: the stage settlement displays distinct success proportions
  for analysed openings, destroyed viruses and collected nodes.
- Claim ID: RZ-009.

### Objective Genes

- New `OBJ-297`: complete the ordinary corridor and actively beat the
  firewall, then see the settlement and the next area become selectable.
- Claim IDs: RZ-004, RZ-008, RZ-009.

### Time Genes

- Reuse `TIM-003`: targets, perspective exposure and incoming hazards advance
  while the player aims and decides. Start can suspend the live attempt.
- Claim IDs: RZ-002, RZ-003, RZ-004.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Several viruses in front | Hold Cross, sweep and release | Held marks accumulate to eight; release commits the shots | Waiting adds targets but spends live time | RZ-003 |
| Missile already coming | Aim at the missile and fire | A hit intercepts the missile; perspective alone does not remove the avatar from the rail | Defence uses the ordinary weapon | RZ-002 |
| Password Protector present | Destroy the protector | The Network Opening is now exposed, with its own hit requirement | The initial kill is not the gate clear | RZ-004 |
| Opening fully exposed | Hold all eight locks on the opening and release | The eight hits enter the next layer and count toward Analyzation | One object can occupy more than one lock slot | RZ-004 |
| Opening passes before enough hits | Let the route continue | The missed opening lowers the analysis result; the attempt can still reach Earth | Analysis and clearance are separate | RZ-004 |
| Eligible enemy killed, node exposed | Shoot the node | Collect its progress or add one banked Overdrive, depending on node type | Destruction and pickup are separate | RZ-005, RZ-006 |
| In a form with seven progress segments | Collect a normal Progress Node | Fill the gauge and advance the form | The gauge promotes the survival tier | RZ-005 |
| Player takes a hit | Let damage resolve | One form falls; from Zero Form this instead ends the attempt | Form itself is the damage ladder | RZ-005 |
| One charge and several visible threats | Press Circle | The charge is spent and automated attacks run briefly | This is time-limited protection, not ordinary ammunition | RZ-006 |
| Infiltration finished | Enter the firewall phase | The shoot-down proportion selects the reported Earth variant and a broader view becomes available | Kill rate and aim envelope change different things | RZ-002, RZ-007 |
| Earth exposes targetable panels or tips | Shoot the exposed targets and intercept its attacks | Attack resolution advances or defeats the firewall | Boss progress depends on reachable pieces | RZ-008 |
| Earth actively defeated | Finish settlement | Inspect three percentages and Area 2 access | Boss clearance is a gate to the next area, not 100% analysis | RZ-004, RZ-008, RZ-009 |

## Strategic and experiential structure

A full volley reduces the overhead of repeatedly turning aim toward safe
targets. Holding for another lock can let an incoming missile hit or let
a gate pass. A support node is another claim on the same aim and time,
even though it improves the next encounter. Keeping an Overdrive for a
dense boss sequence trades immediate margin for later emergency capacity.
Attacks and layer access shape audiovisual feedback, but voluntary
beat-matching is not needed to qualify their mechanical outputs.

## Replay and variation

- Compare an early release that intercepts one arriving missile with a longer
  hold to acquire several targets. A full set of locks on a single opening
  serves a different immediate need from distributing locks among viruses.
- The same first area survives a missed opening. Changing the share of
  destroyed ordinary enemies may select a different boss pattern.
- Claim IDs: RZ-002–RZ-004, RZ-007.

## Adjacent systems and history

- Panzer Dragoon uses an authored trajectory and held targeting too, but
  grants body placement and spends the flight result on another economy.
- Shooting follows the developing soundtrack without a separately judged
  player rhythm operation. Form evolution from acquired nodes also differs
  from the obstacle-success and mistake streaks in Vib-Ribbon.
- Possible later modules: prior-area form carryover, a timed-out firewall
  outcome, the perfect-opening gate to Area 5 and separate score modes.
  No module or cross-release equivalence is assumed.
- Claim IDs: RZ-002–RZ-010.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-161`, `ACT-190`, `ACT-691` | aim, ability button, hold and release |
| System Behaviour | `SYS-215`, `SYS-1410`, `SYS-1411`, `SYS-1507`, `SYS-1508`, `SYS-1509`, `SYS-1510`, `SYS-1511` | rail, pending targets, opening impacts, node types, form, charge and variant |
| Constraint | `CON-782`, `CON-808` | eight entries and phase envelope |
| Information | `INF-510`, `INF-511` | pending count, gauges and settlement ratios |
| Objective | `OBJ-297` | Earth defeat and Area 2 availability |
| Time | `TIM-003` | real-time progression and pause |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `525` (`GAME-0001`–`GAME-0525`).
- Exact genome matches: none.
- Tied near matches: `GAME-0505` — Panzer Dragoon (`7 / 29 = 0.241379`).
- Supported combination subsets: none.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0505` — Panzer Dragoon | `ACT-161`, `ACT-691`, `CON-782`, `SYS-215`, `SYS-1410`, `SYS-1411`, `TIM-003` | Both hold acquisition while the rail advances, then release a finite homing volley before the targets pass. Rez aims from a fixed body path and adds repeated locks on exposed openings, shootable support and a survival-form ladder. Panzer Dragoon lets the player place the dragon within the route, exposes quarter-turn sectors and awards retry credits. | Tied near (`0.241379`) |

### Preserved research notes

- New genes: `SYS-1507`–`SYS-1511`, `CON-808`, `INF-510`, `INF-511`, `OBJ-297`.
- Classification result: `New gene`.
- Evidence and reasoning: support acquisition, gate opening and form
  evolution change different state after the same attack interface.

## Taxonomy impact

- Registry changes: nine Active additions and eight unchanged transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_273](../../../research/taxonomy-changes/TAXONOMY_CHANGE_273.md).
- Candidate terms affected: shootable pickup, split gate, form ladder,
  charge-paid suppression, variant dispatch and distinct area percentages.

## Negative results

- The signature contains no verified combination as a proper subset.
- The available written sources do not establish exact North American
  variant cutoffs or a native beat-accuracy judgement mechanic.

## Delta summary

## New facts

- [Observation | Corroborated | High] An exposed gate takes eight hits;
  opening coverage, enemy destruction and support collection are distinct.
  Damage steps the avatar down the same form ladder that support improves.
  See RZ-004, RZ-005 and RZ-009.

## New genes

- [Observation | Corroborated | High] Nine definitions in
  `TAXONOMY_CHANGE_273`, with medium confidence for the variant selector.

## New combinations

- [Observation | Corroborated | High] No verified combination added.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_273`.

## New questions

- What are the original disc's exact boss cutoffs and timeout behavior
  when every target is left alone?

## Next recommended game

- [Hypothesis | Limited | Medium] Nintendo Switch *Nine Sols*.
- Optimisation criterion: contrast an incoming missile intercepted with
  ordinary fire against a close-range defence that enables retaliation.
- Backlog impact: advance Selection 041 to its fifth candidate.

## Why this game

- [Hypothesis | Limited | Medium] A single rail stage exposes acquisition,
  hit commitment and distinct outcomes under continuing time, using the
  same targeting input for damage, defence and resource recovery.
