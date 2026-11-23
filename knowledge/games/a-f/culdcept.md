---
game_id: GAME-0611
slug: culdcept
game_title: "Culdcept"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-125
    - ACT-811
    - ACT-812
  system:
    - SYS-004
    - SYS-1050
    - SYS-1051
    - SYS-1797
    - SYS-1798
    - SYS-1799
    - SYS-1800
    - SYS-1801
    - SYS-1802
    - SYS-1803
    - SYS-1804
  constraint:
    - CON-174
    - CON-853
  information:
    - INF-002
    - INF-574
  objective:
    - OBJ-330
  time:
    - TIM-004
---

# Game: Culdcept

This analysis follows the
[canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Dunnan’s board, magic threshold, books and creature identities are
parameters of the sampled match.

## Analysis scope

- Version / ruleset: North American commercial PlayStation 2 Culdcept
  disc `SLUS-20774`, English, December 2003. The first Story match,
  Dunnan, Land of Destiny, against Ryvern, using the supplied starter
  Book. Omiya Soft dates its release notice 8 December. The North
  American product catalogue lists 4 December. The precise recording
  build and native console or emulator are unverified.
- Primary decision loop: read the hand, spendable magic and current
  board. Decide on a spell before rolling. Use the eventual landing
  to summon, challenge, pay toll or manage an eligible holding. Turn
  ownership, chains and laps into 5,000 G total magic and bring it
  back to the Castle before Ryvern.
- Entry: create the Cepter, inspect or retain the assigned 50-card
  Book and start the first Story stage. There is no evidence of a
  choice between both supplied deck compositions at the first cutscene.
  The observed run uses its available book named Book.
- Exit: return to the Castle with qualifying wealth, read the
  recorded winner and reward cards, then stop at the returned world
  map where Malthessburg and Dombwood become available.
- Included: assigned Book and draw limit, pre-roll spells, movement
  and checkpoints, summoning, one post-roll territory command, paid
  items in short invasions, land and support modifiers, tolls and
  land chains, both magic ledgers, lap and match settlement.
- Excluded: subsequent Story and replay battles, custom Versus rules,
  all cards and ability exceptions, temple Symbols on other boards,
  debt liquidation as a followed route, balance changes, native
  hardware timings and save/reload testing. Earlier Japanese
  Dreamcast, Japanese and Korean PS2, original Saturn and PlayStation,
  Saga, Revolt and other later editions are outside scope.
- Suggested later scope: a named branched map with Forts on distinct
  branches, showing why repeated access to the Castle alone does
  not settle a lap.

## Direct-play status

No direct play or disc execution was performed. The original North
American English manual and Omiya Soft release notice establish the
product and rules. Two independent commercial English PS2 captures
establish initial Book context, actual decisions and a complete
settlement. W1 is the main route. W2 distinguishes a listed 2003
North American PS2 series and corroborates its result sequence.
The exact loading medium, capture build, pseudo-random algorithm and
save persistence were not measured. Only written sources and static
frames were examined.

## Claim ledger

| ID | Claim | Claim status | Evidence quality | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- |
| CUL-001 | Commercial North American English PlayStation 2 Culdcept is the target, based on the Second Expansion release. Dunnan is the first Story stage and Ryvern is its opening opponent. | Confirmed | Corroborated | High | P1 and P2 fix the carrier. P3 identifies SLUS-20774. W1 2:30–2:40 and W2 12:40–14:00 show English Dunnan and Ryvern. Sources disagree on the exact December release day. |
| CUL-002 | The 50-card Book supplies four opening cards and a turn-opening draw. If the hand goes beyond six, the player discards a card. On depletion, the original Book is remade and shuffled. The first Story start offers an assigned Book to use. | Observation | Corroborated | High | P2 pp. 10–11 and 18–19; H1 sections 3–4; W1 0:20, 23:20 and 33:30; W2 10:30–11:10. Exhaustion was not reached in the sampled route. |
| CUL-003 | A turn admits one optional spell before rolling. The die supplies distance along Dunnan’s track. Passing a Fort can credit its first-pass bonus and a complete lap gives a separate Castle bonus. Ordinary land settlement is determined by the finished move. | Observation | Corroborated | High | P2 pp. 16–19; H1 sections 4–5; W1 2:50, 3:30–3:50, 5:00 and W2 41:50. W1 5:00 shows a 100 G Fort credit. |
| CUL-004 | An eligible summoned defender peacefully claims a vacant ordinary tile. Landing on rival land instead allows challenge or toll. Spending magic decreases currency while acquisition raises assessed land holdings. | Observation | Corroborated | High | P2 pp. 18–20; W1 3:00–3:10 and 4:20 show the open-land prompt and a later paid summon. H1 sections 3–5 distinguish both totals and branches. |
| CUL-005 | Both sides may choose a legal paid item before strikes. Compatible defending terrain grants health by level, and adjacent holdings separately grant strength. The usual order is attacker first, with a surviving defender replying. At 24:20 the Minotaur eliminates the Wolf; the blue territory changes control. | Observation | Corroborated | High | P2 pp. 14–15 and 20–23; H1 sections 4–6; W1 23:40–24:30. The 24:00 panel shows the two +10 ST supports, no terrain HP, and base 40/40 versus 20/40. The optional item follows the preview. |
| CUL-006 | One normally reachable owned territory can be managed after movement as an alternative to summoning. Passing or landing on one permits local access. A precise Fort or Castle landing opens wider access. Management includes level, attribute, move or exchange. | Observation | Corroborated | High | P2 pp. 16–17 and 22–23; H1 section 4; W1 13:40 shows exchange and 15:00 shows a land upgrade menu. An exact Castle landing and a Castle crossing are separate triggers. |
| CUL-007 | Raising a land level spends current G and changes its value and toll. Same-element holdings in the area form chains without requiring adjacency. Ownership changes can therefore change qualifying wealth well away from the landed tile. | Observation | Corroborated | High | P2 pp. 22–23; H1 sections 4–5; H2’s original test chart; W1 14:50 shows Ryvern’s Fire chain drop to three and 15:00 shows level costs. |
| CUL-008 | A surviving defender retains ownership when the incursion fails. Ryvern actually pays 48 G to Tritemios around 17:40. At 33:20 the displayed result separately shows his Wolf return to hand while the Wall of Stone survives. | Observation | Direct | High | W1 17:20–17:40 and 33:00–33:20; P2 pp. 20–22 for loss, retreat and both-removed branches. The visible toll is a transfer between Cepters. |
| CUL-009 | Dunnan requires at least 5,000 G total magic on returning to the Castle. The observed total exceeds the requirement before the return; the match still advances to the return event. | Observation | Corroborated | High | W1 2:40 has the named threshold; 33:30–33:50 shows the last draw, movement, Castle progress and closure. P2 pp. 10–11 and H1 sections 3–5 confirm the combined condition. |
| CUL-010 | The main run credits Tritemios with the win in 33 rounds, 5,878 G to Ryvern’s 3,178 G. It then offers nine reward cards and returns to the world map. A separate North American capture shows the same kind of result and reward handoff. | Observation | Corroborated | High | W1 34:30–35:20, with exact result at 34:40; W1 36:10–36:20 and H1 section 10 for successor access; W2 42:50–44:50 independently shows settlement. |

## Basic data

- Release / origin: Omiya Soft developed the ruleset and announced the
  North American PlayStation 2 launch. NEC Interchannel published it.
- Platform: `PLAT-PLAYSTATION-2`, North American disc SLUS-20774.
- Puzzle families: tactical forecast and counterplay (FAM-009) for
  landed invasion choices and opponents’ item responses, and matching
  and combination (FAM-004) for same-element holdings that revalue a
  chain and for compatible defenders.
- P1: [Omiya Soft's North American release notice](https://www.culdcept.com/information/announcement/news20031208/)
  and [Omiya Soft’s regional edition overview](https://www.culdcept.com/information/announcement/news20030722/).
  Commercial release in December 2003 and North American publisher.
- P2: [North American printed PlayStation 2 manual](https://www.culdceptcentral.com/culdcept-satps1/culdcept-satps1-gallery/421-media-gallery-cps2-manual),
  reproduced as scans. Printed pp. 10–11 show the objective and
  Story setup, 14–19 cards and turn flow, 20–23 invasion and territory,
  24–25 the loss and result boundaries.
- P3: [North American product catalogue entry](https://gamefaqs.gamespot.com/ps2/918917-culdcept/data)
  lists SLUS-20774 and a 4 December release. P1 records 8 December.
- W1: [Tritemios’s opening English PS2 Dunnan match](https://www.youtube.com/watch?v=O-YbsDy3_nU&t=149s).
  New Cepter and one Book at 0:10–0:20; continuous sampled match
  at 2:29–33:50; rank and rewards at 34:30–35:20. The English UI
  and title copyright support the commercial scope. The video's
  description also references the Japanese edition and date.
- W2: [Fin Ravens’s North American PS2 series, first video](https://www.youtube.com/watch?v=f5CB3a7sYFA&t=570s).
  The opening includes attract play before the real title start.
  The 9:50–11:20 section shows new-Cepter menu, starter Book context
  and Story entry. The first result and reward phase appear at
  42:50–44:50. The speaker identifies the regional collecting project
  in the description; recorded disc hashes remain unverified.
- H1: [Brian Nii’s January 2004 PlayStation 2 FAQ](https://culdceptcentral.com/ii/culdcept-ii-ps2-dc/culdcept-ps2dc-guides/culdcept-ps2dc-faq),
  sections 3–6 and 10, for basic turn order, first-stage walkthrough,
  and the matched land, adjacent support and toll branches.
- H2: [Blueworld’s Culdscience guide for PS2/DC](https://culdceptcentral.com/ii/culdcept-ii-ps2-dc/culdcept-ps2dc-guides/culdcept-ps2dc-culdscience-guide),
  the revaluation and toll table used as corroboration for this board.
  Wider parameters in that guide are not inferred as observed in W1.

### Reproducible route evidence

1. Register a new Cepter and retain its first available Book. W1 uses
   Tritemios and notes one book on the save screen at 0:20. W2
   shows the deck editor before starting Story at 10:30–11:20.
   In Dunnan the guide names the 5,000 G Castle requirement at 2:40.
2. Draw, decide whether to use a pre-roll spell, then settle distance.
   Inspect open land and choose a legal creature to claim it.
   W1 4:20 shows the Marfolk summon confirmation on the opening
   loop. The Fort at 5:00 adds 100 G before ordinary final landing.
3. Improve holdings as opportunities permit. At 13:40 W1 offers an
   exchange on owned land. At 14:50 a Fire holding change has
   shortened Ryvern’s chain. At 15:00 his land upgrade menu shows
   level choices with spendable costs.
4. Read relative stats and paid item options before challenging.
   At 17:20 both combatants consider items. At 17:40 Ryvern
   has paid 48 G to Tritemios. On a later blue-terrain invasion
   at 23:40–24:30, Tritemios’s Minotaur removes Ryvern’s Wolf;
   W1 shows the surviving invader occupying the territory.
5. Keep enough assessed magic to reach the Castle. At 33:20
   Ryvern’s Wolf returned to hand while the Wall of Stone survived.
   W1 33:30–33:50 shows Tritemios’s final Fly draw and return,
   with the match moving to the result instead of another normal turn.
6. Read the 33-round result at 34:40. Tritemios wins with 5,878 G
   against 3,178 G. The reward sequence at 35:00 displays nine card
   slots. Return at 35:20 and follow the directional map briefing
   before entering either successor. W2 corroborates the same type
   of handoff after a different match.

These recording timecodes do not fix a legal draw, roll or route length.
Claim IDs: CUL-001–CUL-010.

## Mechanical decomposition

### Action Genes

- ACT-125: play one compatible paid spell before the roll.
- ACT-811: commit an eligible creature to claim or invade the landed tile.
- ACT-812: select one reachable owned territory and its management action.
- Claim IDs: CUL-003–CUL-006.

### System Behaviour Genes

- SYS-004: resolve concealed shuffled card order and die results.
- SYS-1050: advance the token by the resolved distance.
- SYS-1051: distinguish pass fixtures from landed territory effects.
- SYS-1797: deal from the fixed Book and limit the turn hand.
- SYS-1798: combine spendable magic and property value for the objective.
- SYS-1799: pay Fort and complete-lap bonuses at separate events.
- SYS-1800: calculate land and adjacent-ownership battle modifiers.
- SYS-1801: settle the local battle into the occupied tile.
- SYS-1802: revalue holdings and tolls by levels and same-element chains.
- SYS-1803: transfer a rival’s toll when the landed holding survives.
- SYS-1804: credit cards and unlock Story destinations after settlement.
- Claim IDs: CUL-002–CUL-010.

### Constraint Genes

- CON-174: require enough current magic and compatible card targets.
- CON-853: choose one summon or one available territory operation.
- Claim IDs: CUL-003–CUL-006.

### Information Genes

- INF-002: future rolls and hidden Book order are not known in advance.
- INF-574: inspect land, G ledgers, cards and current combat contributions.
- Claim IDs: CUL-002, CUL-003, CUL-005, CUL-007.

### Objective Genes

- OBJ-330: return to the Castle with at least 5,000 G total magic before
  Ryvern meets that condition. An outlying high total can still change.
- Claim IDs: CUL-009, CUL-010.

### Time Genes

- TIM-004: the two Cepters alternate exclusive board turns; a defender’s
  item response happens within the active side’s local battle.
- Claim IDs: CUL-003, CUL-005, CUL-008.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| A new Cepter has the assigned starter Book | Enter first Story match | Opening draw and turn draws use that Book | Collection ownership and live hand contents differ | CUL-002 |
| An ordinary turn begins | Draw, discard any excess, optionally cast a legal spell and stop the die | Advance along the track by the resolved distance | Opportunity timing and movement result are separate | CUL-002, CUL-003 |
| An uncredited Fort lies on the route | Pass it, continuing to the rolled destination | Credit its Fort bonus and record passage | A pass can pay without being the landing | CUL-003 |
| A vacant compatible land is the destination | Pay to place a creature | The creature occupies it and land value contributes to the owner's total | A claim is contingent on a persistent creature | CUL-004 |
| The landing tile is occupied by a rival | Commit an eligible creature and optional item | The defender replies if eligible and the surviving result determines ownership | Actual combat can replace the owner | CUL-005 |
| The rival holding remains after a failed invasion | Settle the arrival | The available 48 G toll in the sampled case transfers from visitor to owner | Toll and battle damage affect different records | CUL-008 |
| An owned tile is accessible through the route or an exact fixture landing | Choose level-up as the territory action | Spend current magic, update land value and the toll, and end the territory opportunity | Investing is different from receiving income | CUL-006, CUL-007 |
| The Cepter owns two or more compatible lands in the same area | Gain or lose another land of that attribute | Revalue the chain and affected tolls | A distant ownership change can reprice other tiles | CUL-007 |
| The target is met before the Castle return | Continue into or across the Castle | The qualifying return settles the win | Reaching the threshold is necessary before closure, not sufficient elsewhere | CUL-009 |
| The result is settled | Continue through the reward cards | Cards enter the collection and the cleared route opens new map choices | Reward is separate from live hand and the next Book | CUL-010 |

## Strategic and experiential structure

Compare an early cheap occupation with keeping enough spendable G
for a later item, upgrade or forced toll. An elemental chain can
raise several values at once. Adjacent territory instead affects the
specific local battle. Taking one tile may both help the invader and
break the defender’s plan. Once the total is high enough, spells
that alter distance and holding valuable routes until the Castle
are more useful than spending down the lead. Claim IDs: CUL-003–CUL-009.

## Replay and variation

The sources use distinct characters and books on the same initial
Story map. W1 establishes one successful run. Its specific item,
toll, finish and power graph are examples rather than minimum
requirements. Draw and die order can change in another run. The game
allows play to continue while a qualifying total waits for return.
Claim IDs: CUL-002, CUL-003, CUL-009, CUL-010.

## Adjacent systems and history

Subsequent maps can separate Forts across branches and introduce
Symbols, other board fixtures and new opponents. Post-match editing
and Story replays change the available Book and the opponent. The
formal first-stage scope ends at the unlock and does not test the
new routes or the secret opponent.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-125, ACT-811, ACT-812 | Spell, landed summon and territory operation |
| System Behaviour | SYS-004, SYS-1050, SYS-1051, SYS-1797, SYS-1798, SYS-1799, SYS-1800, SYS-1801, SYS-1802, SYS-1803, SYS-1804 | Chance, route, triggers, Book, G ledgers, lap, fight modifiers and settlement, value, toll and reward |
| Constraint | CON-174, CON-853 | Current card eligibility and one post-move commitment |
| Information | INF-002, INF-574 | Hidden future outcomes and observable current decision data |
| Objective | OBJ-330 | Return to the Castle with the required total |
| Time | TIM-004 | Alternating adversarial board turns |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `610` (`GAME-0001`–`GAME-0610`).
- Exact genome matches: none.
- Tied near matches: `GAME-0392` — Mario Party 2 (`5 / 29 = 0.172414`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Mario Party 2 (GAME-0392)](../m-r/mario-party-2.md) | INF-002, SYS-004, SYS-1050, SYS-1051, TIM-004 | Both alternate turns, move tokens by dice and distinguish passing from stopping. In Dunnan the final tile opens a card-driven ownership fight and toll, and winning requires a qualified Castle return. Mario Party 2 awards Stars and coins through board events and minigames. | Near, `0.172414` |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_357](../../../research/taxonomy-changes/TAXONOMY_CHANGE_357.md)
  defines the new boundaries and distinguishes the earlier branches.

## Negative results

- ACT-135 plays into an open combat lane. The selected summon here
  targets a landed property and may challenge an existing defender.
- ACT-137 chooses one of multiple piles at draw time. Culdcept
  automatically draws from the fixed Book at turn opening.
- CON-490 describes an event with a supplied set of locked decks.
  New Story has an assigned Book and a broader Book editor.
- SYS-026 refills used hand slots after an action; Culdcept adds one
  draw at turn opening and can exceed its hand cap before discarding.
- SYS-857 claims a building region with an ownership core. Neither
  construction nor an ownership-core fixture is required here.
- OBJ-325 checks score and lead in a head-to-head race. Here current
  wealth is checked again at a physical return event.

## Delta summary

## New facts

- [Observation | Corroborated | High] Spendable and qualifying magic
  diverge as land values, chains and tolls change. CUL-004, CUL-007.
- [Observation | Corroborated | High] Compatible terrain and adjacency
  determine different stat bonuses. Failing to take land leaves a
  visit charge, as witnessed with the 48 G transfer. CUL-005, CUL-008.
- [Observation | Direct | High] The sampled first Story match settled
  at 5,878 G to 3,178 G in 33 rounds, after the required Castle
  return. It then awarded nine cards. CUL-009, CUL-010.

## New genes

- [Observation | Corroborated | Medium] ACT-811, ACT-812,
  SYS-1797–SYS-1804, CON-853, INF-574 and OBJ-330.

## New combinations

- [Observation | Direct | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_357.

## New questions

- What determines which starter Book composition a newly
  registered Cepter receives in this release?
- How does a named branched board settle a Castle crossing with
  enough total magic but a missing Fort flag?
- What exact accounting changes if an unaffordable toll forces
  the player to release a member of an established chain?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0612`, Pipistrello and the
  Cursed Yoyo, original Nintendo Switch commercial release.
  Trace the first complete evidenced route changed by a learned
  yo-yo action through its actual reward or exit.

## Why this game

- [Hypothesis | Limited | Medium] Culdcept asks which land ownership
  turns a route into a gain. Pipistrello asks how a new action changes
  the set of routes the player can physically reach.
