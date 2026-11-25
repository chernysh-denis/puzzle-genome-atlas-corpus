---
game_id: GAME-0681
slug: power-stone-2
game_title: "Power Stone 2"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-161
    - ACT-355
  system:
    - SYS-037
    - SYS-215
    - SYS-317
    - SYS-1478
    - SYS-1953
    - SYS-1954
  constraint:
    - CON-263
  information:
    - INF-627
    - INF-628
  objective:
    - OBJ-359
  time:
    - TIM-003
---

# Game: Power Stone 2

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The roster, arena name, pickup appearance and observed result are fixture parameters.

## Analysis scope

- Version / ruleset: original 2000 North American English Dreamcast
  retail release, Capcom product T-1211N, solo Arcade, first Blue Sky
  Area bout. W1 identifies an NTSC Dreamcast release. W2 supplies the
  full changing-arena branch and describes its difficulty as 8.
  The exact capture builds, hardware and other options are unverified.
- Structured analysis target: PLAT-DREAMCAST in
  [platform coverage](../../platforms/games.json).
- Entry: enter the Blue Sky Area airship as Falcon and start acting
  when the four-fighter introduction yields control. Three CPU fighters
  are active. W2 shows Ryoma, Pete and Galuda in the other slots.
- Primary decision loop: move around the deck and opponents, approach
  chests or take and use portable items, then contest loose stones.
  If two fighters are eliminated, settle the bout immediately. If the
  fight is still active when the ship gives way, steer during the fall,
  try to secure an umbrella before landing and resume the same fight
  in the courtyard. Use a personal three-stone power change when
  available and remain one of the two survivors at the second elimination.
- Exit: Falcon receives a stage win and stands beside the other
  survivor on Next Stage. Stop before the second arena is controllable.
- Included: real-time movement and attacks, active prop and chest use,
  independent stone holdings, power-change threshold, changing support,
  airborne object pursuit, umbrella landing, vitality and elimination
  markers, and the two-survivor result.
- Excluded: item crafting, Adventure, Original and 1-on-1 rule variants,
  local human multiplayer and cooperative rescue, other stages and bosses,
  exact movement or landing-damage formulae, minimum path to the first
  collapse, exact loot distribution, timer options and unobserved
  sudden-death and formal tie branches, and later ports.
- Potential scoped module: compare an Original team bout with the Arcade
  survivor outcome under a controlled roster.
- Direct-play status: no personal console execution or binary inspection.
  The original manual establishes the mode, item roles, powered gauge
  and normal knockout condition. All decisive visual states are grounded
  in W1 and W2. The two Dreamcast guides corroborate the airborne rules;
  one was written for the Japanese edition, used only where it agrees
  with observed Dreamcast states and the North American manual. Video
  frames were inspected in the background with audio excluded.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PS2-001 | Capcom's original North American home release is Dreamcast T-1211N. Arcade supports one to four players and fills the unjoined positions with CPU opponents. The first observed bout begins with four individually identified fighters. | Observation | Corroborated | High | P1 Game Modes, P2, W1 1:26–1:42, W2 1:48–2:03 |
| PS2-002 | Nearby treasure chests can expose items. The action input lets a fighter take an eligible object, which can change the available attack or be thrown or discarded. Loose stones are claimed separately and a qualifying hit can return a held stone to contested space. | Observation | Corroborated | High | P1 Use the Action Button and Game System, R2, W1 1:45–2:07, W2 2:06–2:16 and 4:31–4:35 |
| PS2-003 | During a still-live bout the airship progressively loses support and tips into freefall. All four named W2 fighters and their depleted bars remain in the same bout. They steer among chests while a metre count decreases. An earlier two-KO result can end the bout on the airship. | Observation | Corroborated | High | W2 3:13–3:33, W1 2:45–2:57, R1, R2 |
| PS2-004 | An umbrella is an eligible airborne object and supports a slower landing. Falcon and Ryoma are visibly descending under blue canopies in the courtyard. Unassisted landing can damage a fighter according to the guides. No damage coefficient or fixed number of available umbrellas is inferred. | Observation | Corroborated | High | P1 Use the Action Button, W2 3:30–3:42, R1, R2 |
| PS2-005 | A fighter's own third stone automatically changes its model and substitutes a power gauge. Falcon transforms around 4:34 while Ryoma retains two visible stones. The powered HUD diminishes during the later exchange. The manual distinguishes normal powered attacks and two stronger commands and says that these spend power. | Observation | Corroborated | High | P1 Game System, W2 4:32–4:41, R2 |
| PS2-006 | Pete is the first W2 fighter marked out in the courtyard. The remaining fighters continue. The second elimination marks Galuda out, credits Falcon's stage win and leaves Falcon and Ryoma on Next Stage. | Observation | Corroborated | High | W2 3:53–3:58 and 4:39–4:53, P1 Arcade Mode Rules |
| PS2-007 | The NTSC record W1 settles after two eliminations before the airship fully collapses. The final view still shows the airship underneath the winners. | Observation | Corroborated | High | W1 2:11 and 2:45–2:57, P1 Arcade Mode Rules |

## Basic data

- Release / origin: Capcom, 2000. This fixture uses the original
  North American Dreamcast Arcade mode.
- Puzzle families: FAM-009 for reading competing fighters, resources
  and recovery openings during one live exchange, and FAM-010 for
  collapsing geometry, declining altitude and finite powered time.
- P1: [Capcom North American Dreamcast manual](https://segaretro.org/images/6/62/PowerStone2_DC_US_Manual.pdf).
  See Game Modes, Game Screen, Game System and Use the Action Button.
  The cover and release text identify the home version.
- P2: [Dreamcast regional release listing](https://gamefaqs.gamespot.com/dreamcast/198333-power-stone-2/data).
  Records the original North American T-1211N identity separately
  from other regions and later releases.
- W1: [Spazbo4's NTSC Dreamcast capture](https://www.youtube.com/watch?v=stwqiXo17Lo&t=84s),
  published by LongplayArchive. The source documents the first
  bout and the short deck-only branch.
- W2: [MrCoconuts64's Dreamcast Arcade capture](https://www.youtube.com/watch?v=HIj5BMm8KZQ&t=105s).
  Blue Sky Area starts around 1:45 and the next arena begins
  around 5:05. Inspect the individual times in the claim ledger.
- R1: [Alucard's Dreamcast guide](https://gamefaqs.gamespot.com/dreamcast/198333-power-stone-2/faqs/8364).
  Blue Sky Area covers support loss, freefall, visible height,
  the umbrella and landing. The guide identifies its build as Japanese.
- R2: [Clement Chan's Dreamcast guide](https://gamefaqs.gamespot.com/dreamcast/198333-power-stone-2/faqs/10001).
  Sections 2.3, 2.7 and 5.1 cover the stone and prop handling,
  the extra stones in circulation, and the three arena segments.
- Claim IDs: PS2-001–PS2-007.

### Reproducible fixture evidence

1. Enter the airship first and allow the introduction to finish.
   Read four independent fighter displays and the introductory
   instruction that two survive. Move through the deck and approach
   an item chest. A portable object becomes available to use; loose
   stones remain independently collectible.
2. In the longer W2 bout, check the deck at about 3:16 and the fall
   at about 3:18. The same four fighter displays and their reduced
   vitality carry through. As the metre count keeps dropping, move
   toward reachable objects in the air. An umbrella is a tool for
   this landing rather than a separate win condition.
3. Around 3:36, observe Falcon and Ryoma descending under separate
   blue canopies into the courtyard. Inspect the post-landing bars.
   The first red elimination mark appears on Pete around 3:55,
   and the contest among the remaining fighters continues.
4. Watch Falcon's bottom panel at around 4:33–4:35. His two
   visible stones and ordinary model give way to the powered gauge
   and changed model after the next claim. Ryoma's separate holdings
   remain visible. Powered attacks continue in the same ground bout.
5. At about 4:41–4:43 Galuda's elimination gives Falcon a win.
   The later Next Stage screen shows exactly Falcon and Ryoma,
   near 4:52. Stop there.
6. Compare the earlier result in W1. The blue display has crossed
   out around 2:11. The second elimination around 2:45 ends the
   round on the deck and Next Stage is visible around 2:57.
   This shows that the full aerial route is conditional on the
   bout still being active.

## Mechanical decomposition

### Action Genes

- ACT-008: steer Falcon around the deck or courtyard and change
  position during the controllable drop. PS2-002–PS2-004.
- ACT-048: carry and release an eligible portable prop. PS2-002.
- ACT-161: commit an ordinary attack or supported held-item attack
  in reach. PS2-002, PS2-005.
- ACT-355: claim an available neutral arena weapon or let it go
  to regain the ordinary command set. The weapon interaction is
  distinct from automatically claiming a stone. PS2-002.

### System Behaviour Genes

- SYS-037: make a loose stone a player's resource by contact.
  PS2-002, PS2-005.
- SYS-215: resolve attacks, knockback, lost vitality and defeat
  during the live exchange. PS2-002, PS2-006.
- SYS-317: resolve steerable descent and landing, with an umbrella
  acting as the canopy in the protected branch. PS2-003, PS2-004.
- SYS-1478: a qualifying blow can release an opponent's stone
  into shared space without awarding it directly to the attacker.
  PS2-002.
- SYS-1953: the live battle moves from failing support into a
  playable fall and onto the courtyard with current vitality.
  PS2-003, PS2-004.
- SYS-1954: the personal three-stone threshold starts a powered
  form and spending gauge while separate holdings remain elsewhere.
  PS2-005.

### Constraint Genes

- CON-263: a finally eliminated fighter stops acting in the current
  bout. W2 shows Pete's crossed-out state while the other three
  continue. PS2-006.

### Information Genes

- INF-627: visible remaining height indicates how much descent
  remains to contest airborne objects. PS2-003, PS2-004.
- INF-628: each fighter's named panel reports their vitality,
  stone or power state and indicated elimination. PS2-003,
  PS2-005, PS2-006.

### Objective Genes

- OBJ-359: survive the first two eliminations of the four-entrant
  bout and become one of the two fighters allowed to continue.
  PS2-006, PS2-007.

### Time Genes

- TIM-003: combat inputs and object choices occur while
  hazards, descent and power depletion advance in real time.
  PS2-002–PS2-006.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Four fighters active on the deck | Approach or use an eligible chest or prop | Arena item becomes usable within the same fight | PS2-002 |
| Live bout on failing support | Authored deck collapse finishes | Same four contestants descend with prior vitality and a falling metre count | PS2-003 |
| Airborne before impact | Reach and acquire an umbrella | Canopy-assisted descent in the approach to the courtyard | PS2-004 |
| Low airborne segment | Reach courtyard | Same live bout on the new surface | PS2-003, PS2-004 |
| Falcon two stones, Ryoma also holds stones | Claim the next eligible stone for Falcon | Falcon enters powered form without removing Ryoma's holdings | PS2-005 |
| Four active fighters, or three after one elimination | Settle the first and then second knockout | Bout continues after one, ends after two | PS2-006, PS2-007 |
| Two remaining after second elimination | Stage result settles | Credited win and Next Stage with both survivors | PS2-006, PS2-007 |

## Strategic and experiential structure

A longer fight makes the timing of object pursuit matter in
different ways. Deck position becomes temporary, while remaining
vitality still matters after the fall. An umbrella competes with
other airborne pickups and can improve the upcoming landing.
A third stone later enables a brief stronger form. The player
only needs to be among the last two when the result settles.

## Replay and variation

W1 resolves on the intact part of the deck. W2 runs long
enough for the full three-segment route. Neither recording
establishes an invariant collapse timestamp or an exact
damage threshold for a single unassisted landing. W2's named
opponents and surviving CPU fighter specify that route only.

## Adjacent systems and history

The original Power Stone record covers the preceding game's
two-fighter Dreamcast match and the contest for the entire
three-stone supply. The sequel's Adventure shop, console
versus configurations and the later arcade-based collection
are distinct analysis targets.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-048, ACT-161, ACT-355 | Navigate, handle props and choose weapon or ordinary attacks |
| System Behaviour | SYS-037, SYS-215, SYS-317, SYS-1478, SYS-1953, SYS-1954 | Resolve pickups, attacks, descent, forced transition and personal power change |
| Constraint | CON-263 | Keep finally eliminated fighters out of active play |
| Information | INF-627, INF-628 | Expose descent and individual fighter state |
| Objective | OBJ-359 | Credit the two survivors after the second elimination |
| Time | TIM-003 | Permit action as the stage advances |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `680` (`GAME-0001`–`GAME-0680`).
- Exact genome matches: none.
- Tied near matches: `GAME-0519` — Power Stone (`8 / 31 = 0.258065`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Power Stone (GAME-0519)](power-stone.md) | ACT-008, ACT-048, ACT-161, ACT-355, SYS-037, SYS-1478, SYS-215, TIM-003 | Both steer and attack in a live arena and contest objects and dropped stones. The original fixture is a two-fighter match for the whole three-stone supply. The sequel's four-fighter Arcade scope can preserve the bout through a playable fall, admits a personal stone threshold amid concurrent holdings and advances two survivors. | Near, `0.258065` |

## Taxonomy impact

Five admissions identify playable support loss with carried
bout state, a personal stone threshold, the airborne distance
display, the individual fighting panels and the two-survivor
objective. Ordinary movement, pickup, prop and contact
behaviour can reuse earlier definitions.

## Negative results

- The first elimination does not end the bout.
- Reaching the lower arena does not award a win.
- Both qualified survivors appear in the result, rather than
  fighting again to select a single winner within this bout.
- The airship can still be present when the bout settles.
- A different fighter retains stones during Falcon's transformation.

## Delta summary

Fifteen genes, five new and ten reused. The fixture covers
both the positive fall-to-courtyard branch and the documented
shorter finish on the deck.

## New facts

- The same bout spans moving support, live descent and a new
  surface if its elimination predicate has not yet been met.
- A player's powered form can be active while other fighters
  still hold stones.
- The stage credits both survivors following the second elimination.

## Principles and design implications

Give a changing arena a cue that supports action before the
new surface arrives. Keep competitive state continuous so
item pursuit in the transition has consequences after landing.

## Puzzle or game generation potential

An original four-entrant contest can make a temporary support
give way before a shared landing. Separately verify the
early-elimination branch and the object-assisted landing branch.

## New genes

- INF-627
- INF-628
- OBJ-359
- SYS-1953
- SYS-1954

## New combinations

None admitted. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[Taxonomy Change 427](../../../research/taxonomy-changes/TAXONOMY_CHANGE_427.md).

## New questions

- Which carried item classes survive each boundary?
- Do all unassisted landing states apply the same damage?
- Which set of remaining contestants receives separate credit
  when several eliminations resolve on the same update?

## Next recommended game

Continue Selection 058 with `GAME-0682`, the commercial iOS Apple
Arcade release of Sonic Dream Team. Follow one authored mission
through a movement affordance and its retained completion result.

## Why this game

A bout stays active as its physical support changes. A choice
in the fall matters on the ground, while a sufficiently early
result can leave the entire descent unused.
