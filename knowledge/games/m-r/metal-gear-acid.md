---
game_id: GAME-0575
slug: metal-gear-acid
game_title: Metal Gear Acid
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-202
    - ACT-489
    - ACT-654
    - ACT-782
  system:
    - SYS-057
    - SYS-1686
    - SYS-1687
    - SYS-1688
    - SYS-1689
    - SYS-1690
    - SYS-588
  constraint:
    - CON-077
    - CON-330
    - CON-838
  information:
    - INF-548
  objective:
    - OBJ-026
  time:
    - TIM-038
---

# Game: Metal Gear Acid

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
One card can move Snake or perform its own command. Choosing how much
to spend now changes when the next opportunity arrives.

## Analysis scope

- Version / ruleset: March 2005 English North American PSP commercial UMD,
  reported catalogue ID ULUS-10006. First normal solo story clear, Stage 01,
  Outside Gate at Lobito Island. No physical disc, executable revision or
  native runtime was authenticated.
- Structured analysis target: PLAT-PLAYSTATION-PORTABLE in
  knowledge/platforms/games.json.
- Entry: complete the separate Stage 00 training, start Outside Gate on the
  usual first-entry story path with Snake alone and the initial deck
  unchanged. Begin before spending the first hand card. The exact initial
  hand and timing ties are not pinned.
- Primary decision loop: compare card modes, reach, guard facing and turn
  order. Commit a card to move, use or equip when allowed. Watch both
  remaining actions and pending Cost. End the turn and read the changed
  positions and next opportunity after the cost clock advances.
- Positive exit: bring Snake through the designated North Gate. Inspect the
  successful mission report before leaving for intermission. Killing the
  guard at the gate is optional; an eligible sound diversion can clear the
  route while he remains alive.
- Negative exit: reaching zero LIFE without another controllable actor
  results in Game Over rather than a successful report. The manual directs
  the player back to intermission. Save and restart behaviour for the
  original North American build was not tested.
- Included: visible hand and legal modes, ordinary move range, turn slots,
  Cost order, draw and recycling, applicable equipment, stance, directed
  vision, a wall lure, alarm phases, exit and report. The mission's optional
  pickups are distinct from its clear condition.
- Excluded: pre-mission deck edits, later actors, subsequent missions,
  persistent pack openings, harder settings, Card Link and password imports,
  Link Battle, Metal Gear Acid 2 and other regional editions as the target.
- Potential scoped modules: a later two-actor mission and the progression
  of equipment and ammunition compatibility. Neither supplies extra slots
  or another actor to this opening packet.
- Direct-play status: not conducted. Publisher material and the original
  European English manual were compared with North American launch-period
  written play accounts and a sourced English script transcription. No
  native PSP, emulation, video or audio playback was used. Exact tie-breaking,
  universal first-MOVE discounts, alarm limits in each layout and
  per-build parity remain unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| MGA-001 | Konami released the first Metal Gear Acid for North American PSP in March 2005. ULUS-10006 is the reported commercial catalogue ID. Shipment, reported retail and launch-announcement dates differ by a few days. | Observation | Corroborated | High | P1, R1, R6 |
| MGA-002 | Outside Gate is the first full story mission beyond separate training. Snake enters alone. Crossing the North Gate clears it; the gate guard can be left alive. | Observation | Corroborated | High | P2 pp. 14–15, R1, R2 |
| MGA-003 | The ordinary turn offers two card commitments at REST 2/2. Effective Cost accrues to actor delay, and common elapsed Cost determines the next ready actor at zero. The reported second-card reduction is one. Exact tie priority is unknown. | Observation | Corroborated | High | P2 pp. 16–17, R2, R3, R4 |
| MGA-004 | An ordinary card can be spent as an eligible native use or for movement of up to three cells; specialised movement has its own parameters. Equipment needs an eligible slot. Aerial mode, movement shading, stance and facing affect visible choices or legal reach. The shown effective cost is used, without assuming a universal first-MOVE discount. | Observation | Corroborated | High | P2 pp. 18–21, 26–29, P3, R2, R3 |
| MGA-005 | The starting hand has six cards; the ordinary activation draws up to two toward six. Recycling the exhausted reserve adds 10 Cost. | Observation | Corroborated | High | P2 pp. 16–17, R2 |
| MGA-006 | Directed guard sight is limited by facing and obstructions. A compatible adjacent wall knock emits a lure without a card cost and can draw a guard away on his action. Discovery raises Alert; elapsed Cost out of sight allows Evasion, Caution and Sneak in order. | Observation | Corroborated | Medium | P2 pp. 22–25, P3, R1, R2 |
| MGA-007 | A player may end an activation before the card allocation is exhausted. End without an action incurs 4 Cost. At zero LIFE the last controlled unit cannot continue. | Observation | Corroborated | High | P2 pp. 15–17, 24–25, R2 |
| MGA-008 | Konami's worked tests show side, rear and height damage factors. They establish modifiers for eligible attacks while leaving mixed factors and rounding unverified here. | Observation | Limited | Medium | P4, R1 |
| MGA-009 | The successful report separates Cost, detections, eliminations and all damage, then lists earned points and rank. Its performance fields are separate from the exit predicate. | Observation | Corroborated | High | P2 pp. 14–15, R1, R5 |

## Basic data

- Konami Computer Entertainment Japan / Konami. The first game in the
  series' card-tactics branch, for PSP. Family FAM-009, tactical forecast
  and counterplay.
- P1: [Konami's North American launch announcement](https://www.konami.com/mg/archive/mga/english/news.html)
  is dated 24 March 2005. The [21 March shipping announcement](https://m.hexus.net/gaming/items/psp/3170-konami-ships-metal-gear-acid-to-retail-stores-nationwide/)
  names the PSP launch. These are publisher events, not an installed
  binary build. R6 gives a 22 March product-table date.
- P2: [original English PSP instruction booklet](https://device.report/m/1e1f22dad84449453c8b11d81beb2c11903f3852e76506e48f786a2216709458.pdf).
  European English printing, identified by the European publisher details.
  Pages 14–29 document the turn display, first mission goal, failure, health,
  card movement, equipment, controls and alerts. Shared mechanics are compared
  with North American guides. The booklet alone does not establish the
  North American executable, deck order or regional parity.
- P3: [Konami's illustrated stealth notes](https://www.konami.com/mg/archive/mga/english/game_play_play1.html).
  Supports sound diversion and posture-dependent traversal. Its ducts and
  boxes are example situations, not mandatory features of Outside Gate.
- P4: [Konami's position and damage examples](https://www.konami.com/mg/archive/mga/english/game_play_play2.html).
  Establishes directional and elevation factors in an authored test. No
  formula for combining those factors is inferred.
- R1: [Matthew Rorie, GameSpot mission walkthrough](https://www.gamespot.com/articles/metal-gear-acid-walkthrough/1100-6122267/),
  2005. Stage 00 and Stage 01 distinguish tutorial and mission. Stage 01
  identifies the gate approach, optional pack detour, wall knock and exit.
- R2: [cnick, GameFAQs PSP guide](https://gamefaqs.gamespot.com/psp/920776-metal-gear-acid/faqs/36477),
  2005. Rules and first stages corroborate REST, hand size, shared countdown,
  recycling, guard checks and optional starter actions. Its general MOVE
  discount wording is not used to set the price of every ordinary move.
- R3: [Ryan Flaherty, GameFAQs PSP guide](https://gamefaqs.gamespot.com/psp/920776-metal-gear-acid/faqs/36654),
  April 2005. Explains additive Cost, subsequent readiness and the overview
  for inspecting enemies and legal action choices.
- R4: [AC_Kid, English in-game script transcription](https://gamefaqs.gamespot.com/psp/920776-metal-gear-acid/faqs/36634),
  2005. The training and Office briefing describe remaining commands and
  the sequence discount. The latter is an explanation of the ordinary
  mechanic, not permission to import Office progression into Stage 01.
- R5: [GameSpot's contemporary review](https://www.gamespot.com/reviews/metal-gear-acid-review/1900-6120999/).
  Corroborates command costs and completed-mission performance fields.
- R6: [GameFAQs regional product data](https://gamefaqs.gamespot.com/psp/920776-metal-gear-acid/data).
  Reports ULUS-10006 and separates the release region, catalogue ID and date.

## Mechanical decomposition

### Action Genes

- ACT-202 is the choice of posture, including standing and crawling,
  with contextual flattening at eligible geometry. Lower posture can
  change reachable cells and exposure.
- ACT-489 is the separate adjacent wall knock. It produces a local stimulus
  without using the selected hand card.
- ACT-654 rotates the inspection view while all cells, facings and
  adjacency remain authoritative.
- ACT-782 chooses whether to spend a single current card on an allowed MOVE
  or its own eligible USE or EQUIP command. A card spent to move does not
  also apply its printed effect.
- Claim IDs: MGA-004, MGA-006.

### System Behaviour Genes

- SYS-057 covers the guard leaving an ordinary patrol to inspect a
  perceived stimulus or pursue a detected actor. A sound can divert
  without being a direct visual discovery.
- SYS-588 covers eligible native card effects and card routing. An applied
  single-use effect enters the used pile, whereas suitable equipment can
  remain equipped with its own triggers. Card order scheduling belongs
  to Cost rather than a resolution stack.
- SYS-1686 adds effective command Cost to actor recovery. Resolve the card
  actions now; apply the time they imply to future readiness. Additional
  eligible card commitments can receive the reported sequence discount.
- SYS-1687 refills the hand by up to two toward six and recycles the exhausted
  reserve with a 10-Cost charge. The initial six are not the unknown deck order.
- SYS-1688 advances alarm through Evasion and a separate Caution stage after
  lost sight, before Sneak. The simulated cost clock advances these phases.
- SYS-1689 applies relative facing and elevation to damage resolution for
  eligible card attacks. Neither aim legality nor direction alone is a
  complete damage formula.
- SYS-1690 presents the successful mission's recorded cost, discoveries,
  eliminations, damage, points and rank. None is a minimum score to exit.
- Claim IDs: MGA-002–MGA-009.

### Constraint Genes

- CON-077 requires an unobstructed directed sight region for visual
  discovery. Sound investigation is a separate perception channel.
- CON-330 applies here to Snake's viability. This solo packet has no ally
  whose survival can substitute for his.
- CON-838 caps ordinary card commitments at REST 2/2 per activation and
  lets the player end with unused slots. It does not impose a limit of
  two Cost or grant separate free locomotion.
- Claim IDs: MGA-003, MGA-004, MGA-006, MGA-007.

### Information Genes

- INF-548 exposes hand options, movement shading, card cost, REST, turn
  order and inspection of facing and directed sight before commitment.
  The visible queue is conditional on actions, not a script of all
  future guard decisions.
- Claim IDs: MGA-003, MGA-004, MGA-006.

### Objective Genes

- OBJ-026 is reaching the North Gate after a traversable route is available.
  Taking a pack or removing each guard is unnecessary for that predicate.
- Claim ID: MGA-002.

### Time Genes

- TIM-038 is the shared turn-boundary advance until a pending delay reaches
  zero. A guard may gain another turn before Snake. Time does not drain
  in real seconds while the player reads a card.
- Claim IDs: MGA-003, MGA-006, MGA-007.

## Reproducible transitions

| State / precondition | Action or event | Observable transition | Boundary | Claims |
| --- | --- | --- | --- | --- |
| Training is complete and Outside Gate begins | Enter with the unchanged initial deck | Snake alone, six starting cards and the ordinary two-slot turn | No claimed fixed card order | MGA-002, MGA-003, MGA-005 |
| A Ration is in hand and a reachable cell is highlighted | Choose MOVE and confirm the cell | Snake changes position and the card is spent; one REST slot and its shown Cost are charged | The same card does not also recover LIFE | MGA-003, MGA-004 |
| Snake has a slot and a legal native card command | Choose its native use or equip it if eligible | Resolve its applicable effect or equip it; one slot is used and effective Cost accrues | The second eligible card has a reported reduction of one; no universal first-MOVE discount inferred | MGA-003, MGA-004 |
| A current turn has ended | Advance common pending Cost | An actor at zero is ready; units with delay remaining must wait | No tie or starting-order claim | MGA-003 |
| Hand is below six on the next eligible activation | Draw up to two and recycle if the reserve is exhausted | Hand grows only to its limit; recycling charges 10 Cost | No exact within-draw animation or queue precedence is claimed | MGA-005 |
| Snake is at an eligible wall near a guard | Flatten and use KNOCK, then let the guard take his action | A compatible guard can investigate the lure and leave the gate approach | No automatic relocation on the player's knock | MGA-002, MGA-006 |
| A guard directly discovers Snake | Lose sight and advance tactical time | Alert can fall through Evasion and Caution to Sneak; renewed detection can interrupt it | No real-time countdown or exact local reinforcement schedule | MGA-006 |
| Snake has taken no action this activation | End without a card action | The empty turn accrues 4 Cost and yields control | A turn with a prior paid action is a different case | MGA-007 |
| The North Gate can be crossed | Move through its exit | The mission succeeds and the performance report appears | No all-guards-dead check | MGA-002, MGA-009 |
| Snake alone reaches zero LIFE before the exit | Resolve the incapacitation | Game Over, then a route back to intermission | No exact saved-card or retry snapshot claim | MGA-007 |

## Strategic and experiential structure

- Compare immediate movement with the opportunity cost of using the same
  card for its native effect. The final cell and the timing of the next
  acting unit are separate consequences.
- Worked timing witness, illustrative pending values, not a claimed starter
  order: Snake has 8, guard A has 3 and guard B has 5. Advancing the common
  clock by 3 leaves 5, 0 and 2. A acts. If A then takes on more than 2 delay,
  the next advance of 2 leaves Snake at 3 and makes B ready.
- The gate guard's later movement creates a route-opening choice. The
  wall lure can change that guard's behaviour and open the crossing without
  needing a combat clear. Detection and optional attacks may change the
  report while preserving the same objective.
- Claim IDs: MGA-002–MGA-009.

## Replay and variation

- A new first-mission attempt can present a different hand order and expose
  different card substitutions. The North Gate objective and layout logic
  persist for this scope. Actual seeds and tie rules are unverified.
- Compare a direct gate approach after a diversion with an optional
  combat detour. Draw availability, Cost accumulated before later
  opportunities and the report can differ. No particular rank is required
  to reach the documented successful terminal.
- Claim IDs: MGA-002–MGA-009.

## Adjacent systems and history

- Later story missions add another controlled actor and different deck
  options. Cards that alter the action allowance do not redefine the
  ordinary opening turn.
- The original Metal Gear Solid has adjacent sound lures and directed
  sight too. Its continuous direct control and two-countdown alarm do
  not establish the PSP card clock or its separate Caution stage.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | ACT-202, ACT-489, ACT-654, ACT-782 | Card mode, stance, wall lure and camera |
| System Behaviour | SYS-057, SYS-1686, SYS-1687, SYS-1688, SYS-1689, SYS-1690, SYS-588 | Guard response, card zones, recovery, refill, alarm, damage and report |
| Constraint | CON-077, CON-330, CON-838 | Directed sight, viability and two REST slots |
| Information | INF-548 | Current card legality, available slots and readiness |
| Objective | OBJ-026 | Cross the designated North Gate |
| Time | TIM-038 | Shared discrete decrement to readiness |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `574` (`GAME-0001`–`GAME-0574`).
- Exact genome matches: none.
- Tied near matches: `GAME-0339` — Metal Gear Solid (`6 / 28 = 0.214286`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0339` — Metal Gear Solid | ACT-202, ACT-489, CON-077, CON-330, OBJ-026 and SYS-057 cover stance, a wall lure, directed vision, viability, reaching a location and guard reaction. | Metal Gear Solid uses live direct control and two alarm countdowns. Metal Gear Acid uses hand-card commitments and a shared tactical Cost clock, with a separate Caution phase between Evasion and Sneak. | Tied near: 6 / 28 = 0.214286 |

### Preserved research notes

- New genes: ACT-782, SYS-1686–SYS-1690, CON-838, INF-548 and TIM-038.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_321](../../../research/taxonomy-changes/TAXONOMY_CHANGE_321.md)
  distinguishes card use, slot capacity, effective cost and actor readiness
  and records the reuse and rejection boundaries.

## Negative results

- The European booklet and North American product reports do not
  authenticate a North American executable or establish every regional
  default. The general first-MOVE discount, simultaneous-readiness order,
  full direction-and-elevation formula and exact alert-phase timers stay open.
- Required lethal clearance and a required score threshold are unsupported
  for Outside Gate. Gate entry and the subsequent report are different
  transitions.
- A finite hand with a recycling charge is not a permanent loss of the
  spent cards. Replaying the mission is not proof of the same sampled hand.

## Delta summary

## New facts

- [Observation | Corroborated | High] MGA-003–MGA-005 show that current
  card slots, the hand and future recovery each change under different rules.

## New genes

- [Observation | Corroborated | Medium] Nine additions in taxonomy change 321.

## New combinations

- [Observation | Corroborated | High] No new combination proposed. Existing
  supported subsets are owned by the comparison section.

## Taxonomy changes

- [Observation | Corroborated | Medium] Historical definitions and earlier
  signatures stay unchanged.

## New questions

- An authenticated North American disc could resolve the first-MOVE price,
  readiness ties and exact alarm and retry details using matched starts.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0576, The Forgotten City for Xbox
  Series X|S.
- Optimisation criterion: alternate platform and distinguish turn-clock
  ordering from information and objects carried across a world reset.
- Backlog impact: ninth and final Selection 046 unit.

## Why this game

- [Hypothesis | Limited | Medium] A short fixed-objective mission makes
  movement, card effects and variable future access visible without
  conflating them with campaign deck construction. Verify by comparing the
  same gate route under different legal card spending and guard reactions.
