---
game_id: GAME-0397
slug: command-and-conquer-red-alert-2
game_title: 'Command & Conquer: Red Alert 2'
analysis_status: reviewed
reviewed: 2026-09-25
combination_ids: []
gene_ids:
  action:
    - ACT-139
    - ACT-189
    - ACT-316
  system:
    - SYS-215
    - SYS-297
    - SYS-305
    - SYS-551
    - SYS-1060
  constraint:
    - CON-273
    - CON-292
    - CON-330
    - CON-467
  information:
    - INF-224
    - INF-225
  objective:
    - OBJ-166
  time:
    - TIM-003
---

# Game: Command & Conquer: Red Alert 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Named units,
factions, map positions and mission numbers are carrier parameters, not genes.

## Analysis scope

- Version / ruleset: Westwood's original English Windows base game, not
  *Yuri's Revenge*, its later digital packaging or a mod. This packet fixes
  the first Allied campaign mission, *Operation: Lone Guardian*, at Normal
  difficulty from a fresh campaign. The publisher booklet documents the
  original rules; written mission routes document original PC versions 1.002
  and 1.006. No exact executable revision was inspected or claimed equal.
- Structured analysis target: original Windows PC base game; see `GAME-0397`
  in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: first ordinary player control of Tanya beside the New York harbour,
  before issuing her first command while Soviet Dreadnoughts threaten the
  Statue of Liberty.
- Primary decision loop: select Tanya and allied troops, inspect sight,
  health, available commands and mission briefing; issue movement and target
  orders while hostile movement and combat continue; demolish the four ships;
  reach Fort Bradley to take command of its base; commit a Barracks production
  order and legally place it; train an Engineer; send the Engineer into the
  southeastern bridge hut to restore the ground crossing; then coordinate
  Tanya and any needed GIs against the Soviet supply base while keeping Tanya
  alive.
- Positive terminal: the declared Soviet supply-base hostile set is
  eliminated after the ships and Fort Bradley steps, while Tanya survives;
  mission victory and its campaign successor become available.
- Negative terminal: Tanya dies before victory, failing the mission. Loss of
  ordinary GIs or the Engineer requires replanning or production but is not
  itself asserted as an immediate authored failure.
- Included: four ship demolition targets; Tanya's swim and target-specific
  firearm/C4 effect; GIs and Soviet defenders; selection, movement,
  attack-move and target orders; continuous pathing, sight and combat;
  sight-limited hostile information; staged mission objectives; Fort Bradley
  base control; paid Barracks construction and placement; Engineer training,
  hut entry and repaired bridge topology; Tanya's survival condition; the
  Soviet supply-base assault and mission settlement.
- Excluded: optional capture of Soviet production buildings, the second
  Engineer and Conscript route, extra refineries and ore harvesting, extended
  build orders, later Allied missions, Soviet campaign, Boot Camp, skirmish,
  multiplayer, co-op, national special units, technology tree, superweapons,
  map editor, cheats, saves/reloads, achievements, *Yuri's Revenge* and any
  claim of directly observed frames or audio. Existing Fort Bradley power
  and credits are opening conditions; this route does not test their
  generation or shortfall dynamics.
- Reproducible parameterisation: start a new original-base-game Allied
  Normal campaign; record the actual executable revision if available; enter
  *Lone Guardian*; route Tanya to all four Dreadnoughts without losing her;
  reach Fort Bradley; place a Barracks on a legal footprint, train one
  Engineer and enter the southeastern bridge hut; cross the restored bridge,
  clear the Soviet supply base and observe mission victory. Record any GIs
  trained, C4 targets, unit losses, credits, structure placement, visible
  terrain and whether the authored terminal occurs. An optional Tanya-only
  swim or force-only assault would be a different route through this mission.
- Potential scoped modules: ore/refinery economy under pressure, Soviet
  building capture and enemy-unit production, later Allied missions and a
  fixed original-base-game skirmish.
- Direct-play status: none. The Westwood manual establishes controls, Tanya,
  Engineer, production, fog and mission-briefing mechanisms; two written
  original-game routes corroborate the authored objective chain. No original
  disc, executable, input log, save, screenshot, video or audio was inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `RA2-001` | The original Windows base game offers a separate Allied campaign and mission briefing; the expansion is a different product boundary. | Confirmed | Direct | High | P1, P2 |
| `RA2-002` | The first Allied mission begins with Tanya facing four Soviet Dreadnoughts, then requires contact with Fort Bradley and defeat of the Soviet supply base while Tanya survives. | Observation | Corroborated | High | S1, S2 |
| `RA2-003` | Tanya can swim, kill infantry with her firearm and plant C4 on ships and buildings, making her a target-dependent assault unit. | Confirmed | Direct | High | P1 |
| `RA2-004` | Selection and destination/attack orders produce autonomous movement and continuing combat; allied sight and fog limit actionable hostile positions. | Confirmed | Direct | High | P1 |
| `RA2-005` | The mission grants control of Fort Bradley after the contact step; the bounded route then builds a Barracks and trains an Engineer. | Observation | Corroborated | High | S1, S2 |
| `RA2-006` | An Engineer enters the designated repair hut to restore the broken bridge, opening a ground route into the enemy-base area. | Observation | Corroborated | High | P1, S1, S2 |
| `RA2-007` | Production spends credits and advances at a site or channel, with a completed structure placed on a legal footprint before infantry training becomes available. | Confirmed | Direct | High | P1 |
| `RA2-008` | Tanya's death fails the mission; eliminating the supply-base hostile set while she survives completes the mission. | Observation | Corroborated | High | S1, S2 |
| `RA2-009` | The written routes differ in patch, difficulty and optional tactics, so their common mission chain is supported but precise timing, available starting cash and AI reactions are not directly verified here. | Observation | Limited | Medium | S1, S2, R1 |

## Basic data

- Release / origin: Westwood Studios' original *Command & Conquer: Red Alert
  2* for Windows, released in 2000; this is the base game rather than its
  later expansion or a remaster.
- Platform or physical form: original English Windows PC, mouse/keyboard
  real-time strategy; the structured target is `PLAT-WINDOWS-PC`.
- Puzzle families: tactical forecast and counterplay (`FAM-009`), real-time
  system pressure (`FAM-010`), agent routing and coordination (`FAM-015`) and
  ordered dependency sequencing (`FAM-017`).
- Primary source, checked 2026-09-25: **[P1]** [original Westwood Red Alert 2
  instruction booklet](https://oldgamesdownload.com/manual/command-conquer-red-alert-2-windows-manual-english/),
  scanned by a third-party mirror. The booklet, not its host, is the original
  rules source; the mirror is not a second gameplay witness.
- Publisher distribution reference, checked 2026-09-25: **[P2]** [EA's
  currently sold Red Alert 2 and Yuri's Revenge bundle](https://store.steampowered.com/app/2229850/Command__Conquer_Red_Alert_2_and_Yuris_Revenge/),
  used only to distinguish current lawful availability from the original
  base-game analysis target.
- Written original-game route, checked 2026-09-25: **[S1]** [DeuceExDefcon's
  PC *Lone Guardian* route](https://gamefaqs.gamespot.com/pc/914165-command-and-conquer-red-alert-2/faqs/43153),
  for all four objective stages, Barracks, Engineer, bridge and terminal.
- Independent original-game route, checked 2026-09-25: **[S2]** [Avielh
  Tolentino's Allied campaign guide](https://gamefaqs.gamespot.com/pc/476890-command-and-conquer-red-alert-2-yuris-revenge/faqs/12650),
  explicitly written for original Red Alert 2 v1.006 on Hard in 2001. Its
  host category names the later expansion; expansion mechanics and Hard AI
  reactions are not transferred to this Normal packet.
- **[R1]** source-boundary and direct-play audit in this record. Claim IDs:
  `RA2-001`–`RA2-009`.

## Mechanical decomposition

### Action Genes

- `ACT-189` selects and orders Tanya, GIs or Engineer toward a reachable
  destination or legal target; the actor's contextual target effect is a
  parameter. `ACT-139` places the finished Barracks on a legal footprint.
  `ACT-316` commits Barracks and Engineer production orders to eligible
  channels. Claims: `RA2-003`–`RA2-007`.
- Candidate action gene: none. C4 ship/building demolition is the
  target-specific effect of Tanya's existing order, not a timed carried charge
  (`ACT-209`); this route does not require a separate ability-selection mode.

### System Behaviour Genes

- `SYS-297` executes commanded paths and attack acquisition; `SYS-215`
  settles live damage and defeat; `SYS-305` propagates allied sight and fog;
  `SYS-551` advances paid building and infantry production; new `SYS-1060`
  consumes the entered Engineer into bridge restoration and changes the
  traversable route. Claims: `RA2-003`–`RA2-007`.
- Resolution order: Tanya's ship targets resolve under live combat; Fort
  Bradley contact grants base control; a paid Barracks order finishes and is
  placed; trained Engineer reaches the hut; the bridge becomes traversable;
  surviving forces cross and resolve the final hostile-base encounter.

### Constraint Genes

- `CON-273` gates current hostile knowledge on allied sight. `CON-292`
  requires a legal clear Barracks footprint. `CON-467` requires the eligible
  production site, available order and credits. `CON-330` keeps Tanya alive
  as a mission-critical actor. Claims: `RA2-002`, `RA2-004`–`RA2-008`.
- Scarce resources: Tanya's health, finite initial troops, credits,
  production time and a ground route blocked until the bridge repair.

### Information Genes

- `INF-224` exposes selection, unit health, credits, available production
  and queue state. `INF-225` retains explored map terrain without revealing
  live hostile positions outside sight. The mission briefing exposes the
  current objectives but is not equated with a fixed pre-disclosed checklist:
  the supply-base step is staged after Fort Bradley. Claims: `RA2-001`,
  `RA2-004`, `RA2-005`.

### Objective Genes

- `OBJ-166` settles the mission after the declared hostile supply-base set
  is removed and retains the next campaign mission. Ship destruction and
  Fort Bradley contact are mandatory earlier stages, not separate global
  campaign wins. Tanya's survival is a distinct constraint. Claims:
  `RA2-002`, `RA2-008`.

### Time Genes

- `TIM-003` keeps movement, production, enemy action and combat advancing
  while the player issues new orders. No turn boundary or fixed mission timer
  is asserted. Claims: `RA2-004`, `RA2-007`.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Tanya remains alive by the harbour; four ships are active | Order her into the water and target each ship | She travels within sight and applies ship demolition when she reaches a legal target | amphibious commando route and four-target first stage | `RA2-002`, `RA2-003` |
| Ships are destroyed; Fort Bradley is not yet controlled | Move surviving forces to the fort | Contact changes base ownership/control and offers production | objective chain changes player authority | `RA2-002`, `RA2-005` |
| Fort Bradley is controlled and has enough credits | Queue Barracks, place it on clear ground, then train Engineer | Completed structure becomes a production site; Engineer appears after paid training | production and placement precede specialist route | `RA2-005`, `RA2-007` |
| Southeastern bridge is broken | Order Engineer into its repair hut | Engineer is spent, crossing becomes traversable for ground units | fixture-triggered path-topology change | `RA2-006` |
| Crossing is restored and Tanya survives | Cross, suppress defenders and remove the supply-base hostile set | Victory closes the mission and offers the successor | survival and hostile-set terminal | `RA2-008` |
| Tanya is defeated before the base falls | Continue attempt | Mission fails rather than awarding victory | mission-critical survival boundary | `RA2-008` |

## Strategic and experiential structure

- Local decision: preserve Tanya's health while choosing when to swim,
  approach a defended target or use GIs as support.
- Medium-term planning: obtain Fort Bradley before attempting Barracks and
  Engineer production; repair the ground crossing before routing GIs toward
  the enemy base.
- Long-term structure: the mission shifts from a specialist naval strike to
  base-enabled ground assault. The shift, rather than a full RTS technology
  tree, is the bounded packet's distinctive interaction.
- Failure attribution: health, credits, production icons and explored terrain
  show why an order is unavailable or dangerous; the exact AI response timing
  was not observed directly. Claims: `RA2-004`–`RA2-009`.

## Replay and variation

- Tanya path, timing, use of GIs, Barracks location and defended-base approach
  can vary. The authored map, ship count and objective order remain fixed in
  this scope. No procedural map generation or reward ranking is asserted.
- Extra mining, enemy-building capture or swimming around the bridge can
  produce alternative routes but are excluded from this reproducible one.

## Adjacent systems and history

- *Command & Conquer Remastered Collection* contains different earlier
  games; its opening GDI packet shares RTS orders, production and a hostile
  mission terminal but supplies a mobile construction vehicle rather than
  the Tanya/Fort Bradley/Engineer bridge sequence.
- *StarCraft II*'s first Wings of Liberty mission has a scripted squad and
  survival gate without player production. The comparison below owns the
  exact score and selected-neighbour interpretation.

## Normalised genome

| Type | Active genes | Parameters outside signature |
|---|---|---|
| Action | `ACT-139`, `ACT-189`, `ACT-316` | selected unit, target, building and queue |
| System | `SYS-215`, `SYS-297`, `SYS-305`, `SYS-551`, `SYS-1060` | ship count, repair hut, combat timing |
| Constraint | `CON-273`, `CON-292`, `CON-330`, `CON-467` | sight, footprint, Tanya health and credits |
| Information | `INF-224`, `INF-225` | briefing, selected unit and explored tiles |
| Objective | `OBJ-166` | hostile set and campaign successor |
| Time | `TIM-003` | command timing and production cadence |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `396` (`GAME-0001`–`GAME-0396`).
- Exact genome matches: none.
- Tied near matches: `GAME-0275` — Command & Conquer Remastered Collection (`14 / 20 = 0.700000`).
- Supported combination subsets: none.
- Scan date: 2026-09-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0275` — Command & Conquer Remastered Collection | Fourteen shared genes cover placed construction, paid unit production, direct orders, real-time combat, pathing, fog, legal footprints, credits, a declared hostile-set victory and a continuing clock. | The Remastered Collection packet begins with a scripted mobile construction vehicle that must deploy into a new construction site and manage a power dependency. Red Alert 2 begins with Tanya's ship strike, later hands over Fort Bradley, requires her survival and uses a trained Engineer to reopen a broken ground route. No Red Alert 2 ore economy or mobile construction deployment is imported into this selected mission route. | Near, `14 / 20 = 0.700000` |

## Taxonomy impact

- Registry changes: one new Active system gene, `SYS-1060`; no combination
  is asserted without an independently verified proper subset.
- Taxonomy-change record: [`TAXONOMY_CHANGE_135`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_135.md).
- No existing game signature changes.

## Negative results

- No older bridge gene combines Engineer hut entry, specialist consumption
  and restored ground topology; `SYS-097` is a different transition.
- Original Normal executable revision, exact AI timing and current digital
  wrapper equivalence are not verified and are not claimed.

## Delta summary

## New facts

- [Observation | Corroborated | High] `RA2-002`, `RA2-005`, `RA2-006` and
  `RA2-008` establish the staged first-Allied-mission route.

## New genes

- [Observation | Corroborated | High] `SYS-1060` separates Engineer-triggered
  bridge restoration from ordinary construction and passive crossing.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_135` admits `SYS-1060`.

## New questions

- Does a directly inspected Normal original binary vary the staged objective
  display or Fort Bradley starting economy from either written route?
- How does a later full-economy skirmish change the bounded signature?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0398` *WarioWare, Inc.: Mega
  Microgame$!* in the selected cross-platform horizon.
- Optimisation criterion: contrast a rapid handheld microgame schedule with
  this real-time command-and-production packet.
- Expected information gain: short instruction, microgame timing and
  between-attempt accumulation without an RTS map.
- Backlog impact: one game unit; no claim of a pre-existing WarioWare gene.

## Why this game

- [Hypothesis | Limited | Medium] The first Allied mission links a
  recognisable naval strike to a newly controlled base and a bridge-dependent
  ground assault, testing whether the Atlas can distinguish its transition
  from other RTS campaign openings without importing unplayed content.
