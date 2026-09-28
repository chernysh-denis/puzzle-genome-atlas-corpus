---
game_id: GAME-0434
slug: cooking-mama
game_title: Cooking Mama
analysis_status: reviewed
reviewed: 2026-09-27
combination_ids: []
gene_ids:
  action:
    - ACT-572
  system:
    - SYS-822
    - SYS-1138
  constraint:
    - CON-710
  information:
    - INF-268
  objective:
    - OBJ-249
  time:
    - TIM-003
---

# Game: Cooking Mama — one assessed miso-soup recipe on Nintendo DS

Use the [canonical vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The dish, tofu, stylus, five step labels and bronze/silver/gold classes are scope parameters, not universal gene names.

## Analysis scope

- Version / ruleset: original English Nintendo DS *Cooking Mama* (2006), specifically the ordinary *Let's Cook* miso-soup path as documented for the US release. The official European publisher description confirms the original DS touch-control and medal system; the contemporary US first-hand recipe guide bounds the selected route. Exact cartridge revision and regional step parity were not inspected. This is neither *Cooking Mama 2* nor the Wii or mobile edition.
- Structured analysis target: `PLAT-NINTENDO-DS` in [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: select the available miso-soup dish, read Mama's current instruction, perform the addressed food or utensil gesture on the lower touch screen, and adapt to each step's local timing or precision cue. The game settles that step and presents the next of five authored operations; completing the dish yields a graded medal result.
- Entry: the original DS *Let's Cook* menu with miso soup selectable, before any operation for that attempt. The packet does not assert that this must be a pristine save or that all regional menus have identical initial unlocks.
- Positive terminal / evaluation: finish the five-step miso-soup sequence and receive the ordinary recipe medal, regardless of which medal tier is earned. This is a dish-level result, not completion of all 76 dishes.
- Negative and partial result: a mistimed or poorly executed operation can lower its local quality; the sources do not establish that every such mistake aborts the recipe. We do not assign an invented universal fail threshold or exact medal formula.
- Included: recipe selection, Mama's current-step instruction, knife tapping/chopping, guided touch slicing, a cue-timed stock sequence, careful stylus pouring through a sieve, the final stew, per-step assessment and aggregate dish medal.
- Excluded: optional mid-recipe switch to pork-and-vegetable soup, other 75 dishes and unlock tree, recipe-combination mode, practice without grading, multiplayer/wireless sharing, microphone cooling (not evidenced for this recipe), exact seconds/points, platform emulation, later sequels and ports.
- Reproducible parameterisation: choose ordinary *Let's Cook* and miso soup; complete Chop up, Slice up, Make stock, Separate the stock and Stew in that order. For stock, respond to the scrolling Add, Mix, Low, Mix cues when they reach the action line. Tilt the pot carefully so stock lands in the sieve. Continue through stew and accept the displayed medal. The exact final stew command sequence is not needed to establish the bounded step relation and is not asserted here.
- Potential scoped modules: one measured recipe branch, microphone cooling in a recipe that actually requires it, the 15-basic-to-61-bonus unlock rule, or an independently traced medal calculation.
- Direct-play status: no original DS cartridge, save, touch trace, screenshot, video or audio was inspected. Publisher descriptions give the global rules. Two independent first-hand written original-DS guides establish the miso-soup route and general cooking input pattern; exact timing tolerance and regional parity remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CMA-001` | Original DS Cooking Mama uses stylus operations to prepare a dish across multiple minigames under Mama's instructions. | Confirmed | Direct | High | P1 |
| `CMA-002` | Ordinary completed dishes receive bronze, silver or gold according to cooking quality; Practice does not judge. | Confirmed | Direct | High | P1 |
| `CMA-003` | The original DS miso-soup path has five steps: chop, slice, make stock, separate stock, stew. | Observation | Corroborated | High | S1, S2 |
| `CMA-004` | Stock making requires actions at scrolling cue windows; for this route the documented order is Add, Mix, Low, Mix. | Observation | Limited | Medium | S1, S3 |
| `CMA-005` | The stock-separation gesture tilts the pot toward a sieve, where careless movement can spill. | Observation | Limited | Medium | S1 |
| `CMA-006` | A failed step does not justify assuming the whole recipe necessarily ends, or assigning a numeric medal threshold from these sources. | Observation | Limited | High | P1, S3 |

## Basic data

- Release / origin: original *Cooking Mama* for Nintendo DS, 2006. Nintendo's European page dates its local release to 8 December 2006; that date is not silently assigned to the US route used by the contemporary guide.
- Platform or physical form: Nintendo DS game card, lower touch screen and stylus. A microphone exists and is used elsewhere in the game, but is outside this miso-soup packet.
- Mechanical family: ordered dependency sequencing (`FAM-017`): the dish advances from one assessed preparation step to the next in an authored order. The order is not a material-crafting prerequisite graph or free-form cooking simulator.
- **P1**: [Nintendo UK's original Nintendo DS Cooking Mama product description](https://www.nintendo.com/en-gb/Games/Nintendo-DS/Cooking-Mama-270330.html), publisher-provided original DS controls, 76 dishes, medal classes and Practice mode (accessed 2026-09-27).
- **S1**: [Daniel Engel's original DS Cooking Mama written walkthrough](https://gamefaqs.gamespot.com/ds/931435-cooking-mama/faqs/44983), `D-01` Miso Soup and modes (first-hand player route, accessed via indexed text 2026-09-27). The page is currently restricted to the browsing tool, so only surfaced indexed passages were used; no unseen line was assumed.
- **S2**: [Sean Velasco's contemporary original DS recipe FAQ](https://gamefaqs.gamespot.com/ds/931435-cooking-mama/faqs/44870), 20 September 2006 US recipe tree and Miso Soup step list (first-hand recipe enumeration, indexed text accessed 2026-09-27).
- **S3**: [ClearQuartz's original DS Cooking Mechanics Guide](https://gamefaqs.gamespot.com/ds/931435-cooking-mama/faqs/45397), personally tested step controls and timing/medal distinctions (first-hand guide, indexed text accessed 2026-09-27).
- Claim IDs: `CMA-001`–`CMA-006`. No audiovisual evidence or direct play was used.

## Mechanical decomposition

### Action Genes

- Add `ACT-572`: the player performs a prompted direct touch gesture on the current food or utensil. The exact chopping and slicing shapes are parameters of the current step, not separate universal actions (`CMA-001`, `CMA-003`).

### System Behaviour Genes

- Add `SYS-1138`: the chosen recipe advances through five separately assessed authored steps. Reuse `SYS-822` for the completed dish's quality-based graded result rather than claim an exact private medal formula (`CMA-002`, `CMA-003`).

### Constraint Genes

- Add `CON-710`: stock-making commands count only for the current step and shown cue window. The recipe itself has no sourced whole-dish terminal deadline (`CMA-004`).

### Information Genes

- Reuse `INF-268`: Mama's instruction and the highlighted current operation guide one preparation task at a time, not a complete hidden future route (`CMA-001`, `CMA-003`).

### Objective Genes

- Add `OBJ-249`: complete the selected dish and retain the medal. A gold medal is an optional quality aim, not the positive endpoint's prerequisite (`CMA-002`, `CMA-003`).

### Time Genes

- Reuse `TIM-003` for real-time input within a live minigame cue window. This does not mean every step has an identical timer or that recipe-menu selection is timed (`CMA-004`).

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Miso soup is selectable in ordinary Let's Cook | Select the dish and begin | Mama presents the first preparation operation | one selected multi-step recipe | `CMA-001`, `CMA-003` |
| Chopping is active | Tap the knife against the current ingredient | Chopping settles locally; the next slicing task appears | assessed step progression | `CMA-003` |
| The slicing guide is visible | Draw along its marked cuts with the stylus | The current ingredient is sliced and this step is assessed | touch-path operation, not atomic craft | `CMA-001`, `CMA-003` |
| Stock-making bars approach the action line | Address Add, Mix, Low, Mix at their indicated windows | On-time commands are accepted for this step; off-window inputs may worsen its result | ordered, local timed response | `CMA-004` |
| The stock and sieve are shown | Drag to tilt the pot carefully toward the sieve | Successful pour separates stock; spilling is a quality risk | direct preparation gesture | `CMA-005` |
| Final stew task is available | Follow the current stew prompts until it settles | The recipe completes and awards a quality-based medal | bounded dish endpoint | `CMA-002`, `CMA-003` |

## Strategic and experiential structure

- Local decision: read the current cue before tapping, dragging or moving a cooking control, especially at the scrolling stock action line.
- Medium-term planning: maintain accuracy across several distinct preparations; a single precise chop is not the completed meal.
- Long-term structure: the packet stops when miso soup receives its medal. Recipe unlocks and the wider catalogue are outside the analysed session.
- Failure attribution: the displayed step and timing cue make a poor local result attributable to the input, but the source does not justify a universal recipe-abort rule.
- Player-trust factor: a medal is earned from the completed attempt, not a promised gold outcome or a tutorial-only practice result.

## Replay and variation

The selected recipe's five-step order is authored. Gesture accuracy and cue timing can vary between attempts and affect quality. The ingredient identities, dish branch and exact timing tolerances are not proposed as stochastic genes. Practice mode offers rehearsal, but its unjudged result is excluded from this ordinary attempt.

## Adjacent systems and history

*Kingdom Come: Deliverance II* (`GAME-0240`) also evaluates a cooking-like process, but its embodied alchemy bench retains manually manipulated batch history at one workstation; *Cooking Mama* switches between short touch-screen minigames under separate prompts. *DAVE THE DIVER* (`GAME-0278`) also grades a bounded food-service activity, but its restaurant service is not an ordered single-dish gesture chain.

## Normalised genome

| Type | Active gene IDs | Key parameters |
|---|---|---|
| Action | `ACT-572` | addressed touch gestures |
| System Behaviour | `SYS-822`, `SYS-1138` | quality grade and five-step sequence |
| Constraint | `CON-710` | current cue/order/window |
| Information | `INF-268` | current Mama instruction |
| Objective | `OBJ-249` | miso soup and retained medal |
| Time | `TIM-003` | live local cue timing |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `433` (`GAME-0001`–`GAME-0433`).
- Exact genome matches: none.
- Tied near matches: `GAME-0350` — Jet Set Radio (`3 / 22 = 0.136364`).
- Supported combination subsets: none.
- Scan date: 2026-09-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0350` *Jet Set Radio* | `SYS-822`, `INF-268`, `TIM-003` cover a graded bounded activity, a staged current instruction and live input time. | Jet Set Radio commits graffiti traces while moving through a pressured city and evading pursuers; Cooking Mama performs food/utensil gestures in separate authored recipe steps, with stock cue windows and one dish medal. Shared grade and instructional timing do not equate traversal, spray supply or pursuit with recipe progression. | Sole tied-near maximum, `0.136364`; not an exact or verified-combination match. |

## Taxonomy impact

`TAXONOMY_CHANGE_171` admits a prompted touch-step action, ordered assessed recipe progression, step-local cue legality and a dish-level medal endpoint. Existing graded activity, staged instruction and live timing boundaries are reused. No earlier signature or verified combination changes.

## Negative results

- `ACT-410` operates one embodied alchemy workstation and retained batch; this DS packet switches between evaluated touch minigames.
- `CON-068` ends a whole attempt when its clock expires; the documented stock cue is local and poor performance need not terminate the recipe.
- `SYS-756` grades a retained alchemy process history; the current packet uses distinct short tasks and a dish-level medal.
- The game's microphone cooling feature is real but not documented for the selected miso-soup sequence.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original DS game assesses completed cooking with medals while Practice does not judge (`CMA-002`).
- [Observation | Corroborated | High] Miso soup has the documented five-step preparation order (`CMA-003`).

## New genes

- [Observation | Corroborated | High] Four typed boundaries are admitted in `TAXONOMY_CHANGE_171`.

## New combinations

- [Observation | Limited | Medium] No new verified combination proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_171`; earlier signatures unchanged.

## New questions

- What exact command tolerances and medal calculation would a direct original-DS touch trace establish?
- Does the selected five-step route have identical prompt details in all original regional cartridges?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0435` *EarthBound*, original SNES release.
- Optimisation criterion: alternate a gesture-driven graded microtask chain with menu-based RPG combat and overworld traversal.
- Expected information gain: distinguish rolling HP and delayed item/PSI choices from ordinary turn settlement.
- Backlog impact: retain the approved 433–441 order; begin only after the Goal stop window.

## Why this game

- [Hypothesis | Limited | Medium] One recipe tests whether touch gestures, per-step legality, ordered preparation and a final medal remain distinct when the original game's broader catalogue and optional branches are excluded.
