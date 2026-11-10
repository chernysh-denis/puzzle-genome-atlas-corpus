---
game_id: GAME-0511
slug: animal-crossing-new-leaf
game_title: Animal Crossing: New Leaf
analysis_status: reviewed
reviewed: 2026-10-06
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-089
    - ACT-091
    - ACT-130
    - ACT-199
    - ACT-219
    - ACT-424
    - ACT-476
    - ACT-673
    - ACT-704
    - ACT-705
  system:
    - SYS-921
    - SYS-922
    - SYS-1279
    - SYS-1444
    - SYS-1445
    - SYS-1446
    - SYS-1447
    - SYS-1448
  constraint:
    - CON-210
    - CON-790
  information:
    - INF-117
    - INF-128
    - INF-352
    - INF-461
    - INF-497
  objective:
    - OBJ-290
  time:
    - TIM-003
    - TIM-025
---

# Game: Animal Crossing: New Leaf — original home-town fishing settlement

Use the canonical [vocabulary and signature](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Rod price, sixteen slots, species, habitat, civil hour, nibble count and premium
magnitude are parameters, not separate genes. Personal observation and public
museum credit are different state variables.

## Analysis scope

- Version / ruleset: Original released English Nintendo 3DS Animal Crossing: New Leaf, 2013
  release-period home-town rules, not the 2016 Welcome amiibo update or New
  Horizons. P1 is the original Nintendo English manual CTR-P-EGDP-EUR-00,
  copyright 2012–2013; P2 lists the original and Welcome amiibo manuals
  separately. R1 is a North-American-attributed fishing recording published
  2013-06-13. Its exact patch, checksum, hardware and modification state are not
  verified; the European manual and attributed recording do not establish
  regional binary identity. Later community pages are qualified corroboration of
  their explicitly New Leaf sections.
- Structured analysis target: PLAT-NINTENDO-3DS, original released English home-town fishing;
  knowledge/platforms/games.json is authoritative. No release-platform audit is
  implied.
- Primary decision loop: Prepare and hold a standard rod in an established solo home town, select
  eligible water and a visible shadow, cast near it, wait through nibbles and
  respond to the bite. Resolve capture or escape, personal caught-species credit
  and pocket capacity; choose retention, home display/recovery, release,
  first-species museum donation or current-price sale/paid refuse disposal.
  Inspect the separate caught and donated sets and save the accepted current
  settlement. Calendar eligibility and ordinary business hours remain causal
  throughout.
- Entry and exit: Reproducible entry is an established original-release solo town after saving
  is enabled, with an accessible house, the original museum, open Nookling
  Junction and Re-Tail, no active ordinance or external visitor, a standard rod
  offered for 500 Bells, enough starting money and available pocket capacity.
  Start before acquiring/holding that rod, not after a preselected catch. Exit
  is the first player-chosen completed settlement save after the fishing round;
  no researcher-invented fish count or mandatory sale-plus-donation quota is
  imposed. All ordinary in-scope disposition and failure alternatives are
  included, not just one successful catch.
- Included: Walking and eligible running on shore; purchasing/holding the standard rod;
  habitat/date/hour eligibility and current shadows; casting, nibbles, bite
  response, premature/late reeling and disturbance escape; caught species and
  fish/refuse items; sixteen ordinary pocket slots with a held tool separate,
  eligible item rearrangement, full-pocket swap/release; unrewarded release,
  recoverable indoor fish display, museum first-species acceptance/duplicate
  refusal and permanent public display; Re-Tail current species quote, posted
  premium, declined sale and paid trash disposal; current price/capacity/time
  disclosure; explicit current saving and later continuation under the advancing
  civil clock.
- Excluded: Initial mayor/house/debt onboarding and Isabelle’s separate first-advice
  procurement chain; island travel, rental equipment, tours, visiting towns,
  external StreetPass input, diving and sea creatures; tournaments and prizes;
  silver/gold rods, museum shop construction, cafe, bugs, fossil assessment, art
  and whole-collection completion; unrelated
  home/debt/customisation/flea-market/turnip economies; ordinances, Welcome
  amiibo/RV/MEOW changes, New Horizons crafting, tool wear, C.J., outdoor tanks
  and five-species invitation; system-clock editing, exact native bite/spawn
  coefficients, save-file byte coverage and asserted controlled reload outcomes.
- Potential scoped modules: A complete island expedition, diving activity or tournament would require
  separately dated rules and entry/exit. No module ID or future gene count is
  promised. Full-pocket, indoor-display and save-continuation transitions are
  qualified documentary reconstructions, not own hardware tests.
- Direct-play status: No own 3DS executable, hardware, controller, capture timing or save/reload was
  tested. R1 ZackScottGames fishing video was published 2013-06-13, metadata
  length 2020 seconds, actual player duration 2019.461. Actually inspected
  paused frames:
  180/420/600/780/960/1050/1080/1140/1200/1210/1290/1320/1335/1380/1390/1400/1500/1680/1700/1710/1720/1740/1750/1770/1860/1875/1890/1910/1930/1985.
  Bank casting, a held catch, Reese’s sale selection/settlement and Blathers’s
  donation sequence are distinguished from net use, the unreadable item at 1500
  and the later post-office visit. YouTube overlays sometimes obscure detail;
  blank dialogue is not a read species or exact price. Source ID, no-ad,
  paused/muted state, duration and seek checks accompany local captures. This is
  attributed frame sampling, not continuous play or proven regional/build
  parity. The original manual was read and relevant saving, pockets, item
  handling and museum pages visually inspected. All media stayed background,
  headless and muted, without fullscreen, focus or user-window/system-sound
  changes; no audio analysis or remote video download occurred. Working
  frames/prompts remain outside Git.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| NL-001 | Original released 2013 English 3DS rules are distinct from Welcome amiibo; regional/build parity is unverified. | Observation | Direct | High | P1/P2; R1 metadata |
| NL-002 | Calendar, habitat and current business hours constrain an ordinary established-town fishing round. | Observation | Corroborated | High | P1 §§4/7/10; S4/S6/S7 |
| NL-003 | Standard-rod casting, nibbles and bite response differ from premature/late/disturbance escape. | Observation | Corroborated | High | R1 water frames; S1/S4 |
| NL-004 | A successful fish capture yields an identified specimen and personal encyclopedia credit; refuse is not a fish species contribution. | Observation | Corroborated | High | P1 §7; R1 1335; S1/S3/S6 |
| NL-005 | Sixteen ordinary slots and a separate held tool constrain reception; overflow requires an eligible replacement or release. | Observation | Limited | Medium | P1 §7; S5; no native full-pocket replay |
| NL-006 | Retained fish may be released or placed indoors and recovered, distinct from an irreversible museum transfer. | Observation | Limited | Medium | P1 §§7/9; S5/S9; no controlled indoor replay |
| NL-007 | Blathers accepts an eligible first species into the permanent public collection and refuses duplicates; exhibits and board are separate from personal caught knowledge. | Observation | Corroborated | High | P1 §11; R1 1860/1875/1890; S2/S8 |
| NL-008 | Fish sales use the current species quote/premium; fishing refuse can require payment for disposal, and fish cannot be listed on the flea market. | Observation | Corroborated | High | P1 §10; R1 1750/1770; S3/S6/S7 |
| NL-009 | Explicit saving retains accepted settlement while civil time continues; exact save bytes and controlled reload are unverified. | Observation | Limited | Medium | P1 §§4/5/7/11; no own reload |
| NL-010 | The declared settlement-save evaluation is not a whole-game victory, fixed catch quota or mandatory combined sale/donation. | Observation | Corroborated | High | P1; S1; ADR-007 |
| NL-011 | Ten new boundaries and nineteen unchanged transfers cover the packet without importing New Horizons onboarding or crafting. | Observation | Direct | High | TAXONOMY_CHANGE_248; registry review |
| NL-012 | All lower-ID signatures and verified proper combination subsets are recomputed from the complete genome. | Observation | Direct | High | Corpus comparison; validator |

## Basic data

- Release / origin: Nintendo's original New Leaf, released English 3DS edition
  in the 2013 period. P1 is the original ©2012–2013 manual; no exact regional
  release day or installed patch is inferred from a video publication date.
- Structured target: PLAT-NINTENDO-3DS only. No all-platform release audit.
- Families: FAM-010 live bite response, FAM-012 retained species evidence and
  public collection, FAM-013 held tool, bounded pockets and accepted transfers.
  These reused boundaries are causal, not a new one-game fishing family.
- P1: [Original Nintendo English manual](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/nintendo_3ds_2/animal_crossing_new_leaf_2/ElectronicManual_Nintendo3DS_AnimalCrossingNewLeaf_EN.pdf),
  CTR-P-EGDP-EUR-00, ©2012–2013, 56 PDF pages, read. Sections 4/5 establish
  calendar/saving, 7 pockets/encyclopedia, 9 indoor items, 10 Re-Tail, 11 museum.
  Saving, pockets, placement and museum pages were also visually inspected.
- P2: [Nintendo manual catalogue](https://en-americas-support.nintendo.com/app/answers/detail/a_id/16903/),
  read original-versus-Welcome-amiibo entries. Product identity, not controller play.
- R1: [ZackScottGames, Part 9 Fishing](https://www.youtube.com/watch?v=XK9fZ1B9y3k),
  published 2013-06-13, metadata 2020 seconds, player 2019.461. The exact sampled
  frames and overlay limits are disclosed above. North-American description is
  attribution, not proven console/build/region; no audio was analysed.
- S1: [SuperCheats Fishing Basics](https://www.supercheats.com/animal-crossing-new-leaf/walkthrough/fishing-basics),
  Paul/vhayste, 2013-07-10, relevant body read. Bite and early/late escape;
  its mistaken adviser name is not propagated as an official name.
- S2: [GamerGuides Museum](https://www.gamerguides.com/animal-crossing-new-leaf/guide/main-street/museum),
  James Bowden, guide originally 2013-07-28, later updated, relevant body read.
  First-species acceptance and duplicate rejection; later construction excluded.
- S3: [GamerGuides Re-Tail](https://www.gamerguides.com/animal-crossing-new-leaf/guide/your-town/re-tail),
  same guide, page update 2020-12-07, relevant selling/disposal body read.
  Qualified later documentation, not proven launch-binary parity.
- S4: [Nookipedia Fishing rod](https://nookipedia.com/wiki/Fishing_rod),
  original New Leaf price and tool section plus usage read; community reference,
  not a primary binary inspection. Standard 500-Bell rod differs from upgrades.
- S5: [Nookipedia Pockets](https://nookipedia.com/wiki/Pockets),
  relevant New Leaf capacity/held-tool/overflow body read. Home placement and
  catch credit use P1/S9 as independent context, not own overflow testing.
- S6: [Nookipedia Fish/New Leaf](https://nookipedia.com/wiki/Fish/New_Leaf),
  relevant habitat/hour/price table read. Its product-wide 72 fish include
  island availability; neither all 72 nor a copied external timetable is the goal.
- S7: [Nookipedia Re-Tail](https://nookipedia.com/wiki/Re-Tail),
  original hours, quoted premium and fish flea-market restriction read. Welcome
  amiibo carpet/RV and external StreetPass multipliers are not admitted.
- S8: [Nookipedia Museum](https://nookipedia.com/wiki/Museum),
  specifically New Leaf section read: public board, donors and aquarium;
  adjacent New Horizons invitation/expansion description is excluded.
- S9: [Nookipedia Fish](https://nookipedia.com/wiki/Fish),
  fish-as-home-furniture body read and paired with P1 indoor handling.
  C.J. model requests are explicitly New Horizons, not a New Leaf transfer.
- Claim IDs: NL-001–NL-012. Community documentation accessed 2026-10-06 is
  corroboration; uncertain native details remain Limited, not invented precision.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: ACT-008/089/091/130/199/219/424/476/673.
- Added genes: ACT-704/705 for recoverable private specimen placement and
  explicit current save/continue-or-exit, not historical branch selection.
- Parameters: shop stock/price, held rod, cast position, eligible specimen,
  free indoor footprint, pocket destination, irreversible release and save menu.
  Rearranging into a free slot does not claim rotating multi-cell fish shapes.
- Claim IDs: NL-002–NL-009/011.

### System Behaviour Genes

- Existing gene IDs: SYS-921/922/1279 for habitat/calendar sampling, accepted
  capture/knowledge and current town-business admission.
- Added genes: SYS-1444–1448 distinguish nibble/bite escape, permanent public
  acceptance, capacity disposition, quote/negative disposal and saved settlement.
- Resolution order: current calendar/service state constrains preparation;
  held rod and cast lure engage a nearby eligible shadow. Mere nibbles do not
  create an item. Timely bite response captures; early/late/disturbance loses
  the target. Successful capture earns species knowledge and pending stock;
  capacity may require release or eligible replacement. Retention, indoor
  recovery, irreversible release, museum acceptance or priced sale then changes
  different state variables. A completed current save closes the round while
  future civil time still changes availability.
- Parameters: habitat, month/hour, shadow, nibble sequence, unspecified native
  response interval, slot count, owned/caught/donated sets, base quote, posted
  premium, trash cost and current save. Refuse is not catalogued as a fish.
- Claim IDs: NL-002–NL-009/011.

### Constraint Genes

- Existing gene IDs: CON-210. Added: CON-790 for first eligible public species.
- Scarce resources: compatible pocket capacity and current Bells; buying
  requires the offered price, ordinary sale requires open service, museum
  contribution requires a physically carried undonated species. Starting money
  and entry capacity are declared, not universal infinite resources. Currency
  caps and bag occupancy retain the ordinary inventory constraints; no native
  high-balance overflow execution or byte-level arithmetic is asserted.
- Claim IDs: NL-002/005/007/008/011.

### Information Genes

- Existing gene IDs: INF-117/128/352/461. Added: INF-497.
- Current prices, capacity, shadows, nibbles/bite, caught identity and local
  date/hour are visible. Personal encyclopedia and public exhibit/board answer
  different questions; donation selection/refusal supplies eligibility feedback.
  No unseen future spawn or New Horizons donation icon is asserted.
- Claim IDs: NL-002–NL-009/011.

### Objective Genes

- Added: OBJ-290, declared complete ordinary gathering-round evaluation.
- Success/evaluation: save accepted knowledge, contribution, owned stock and
  money after the player's disposition choice. No whole-game terminal or fish
  quota exists here. Each cast can fail without killing the resident or erasing
  the whole collection; a duplicate donation is rejection, not a second exhibit.
- Claim IDs: NL-003–NL-010/011.

### Time Genes

- Existing gene IDs: TIM-003/025. Live bite response and persistent civil-time
  availability are separate clocks. Menu planning is not evidence that a
  pending bite waits forever; changing system time is outside admission.
- Claim IDs: NL-002/003/009/011.

## Reproducible transitions

These are source-grounded operational predictions, not a claim of own native
execution. Native coefficients, full-pocket and save-reload branches retain
the ledger qualifications.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Open shop, offered standard rod and enough Bells | Confirm acquisition and hold it | Price is paid and the compatible tool is held | Preparation belongs to the loop, not a free assumed tool | NL-002 |
| Shadow near a reachable bank | Cast within engagement reach | Eligible fish can approach the lure | A distant or misdirected cast is not guaranteed capture | NL-003 |
| Bobber nudges without terminal bite | Reel prematurely | Target can flee, no successful specimen | Nibble is not bite | NL-003 |
| Bite in its response interval | Reel in time | Fish leaves water, carried/pending specimen and caught credit arise | Observation precedes donation | NL-003/004 |
| Bite expires or fish is disturbed | Miss response or run nearby | Target flees rather than pays or donates | Local failed attempt does not erase older collection | NL-003 |
| Completed catch, ordinary slots full | Release or free an eligible slot | New specimen is discarded or retained; observation credit remains | Capacity disposition is not a failed cast | NL-005 |
| Carried fish and eligible indoor position | Place, then pick up when capacity permits | Owned display leaves and re-enters pockets | Recoverable ownership differs from public donation | NL-006 |
| Carried fish at an eligible release context | Confirm release | Owned stock is removed without money | Release is not a sale or museum credit | NL-006 |
| Carried eligible species absent from public set | Donate to Blathers | Stock is consumed and species displayed/credited | First public contribution is separate from personal catch | NL-007 |
| Species already in public set | Offer another specimen | Duplicate is refused, not another exhibit | A known species still has item ownership | NL-007 |
| Eligible fish at open Re-Tail | Confirm or decline quoted sale | Confirm removes stock and credits current quote; decline retains it | Premium/quote is current information, not volume repricing | NL-008 |
| Fished boot, can or tire | Accept paid disposal | Refuse is removed and money charged | Not every reeled item is positively sellable | NL-008 |
| Re-Tail outside ordinary opening hours | Reach the building | Ordinary selling service is unavailable | Calendar affects settlement, not just decoration | NL-002 |
| Settled stock, money and collection | Complete enabled save | Accepted record persists; later civil time still advances | Save is not an older-history archive or frozen date | NL-009/010 |

## Strategic and experiential structure

- Local decision: approach quietly, place the lure and distinguish a nudge from
  the brief bite; choose capacity relief and specimen disposition deliberately.
- Medium-term planning: preserve undonated species, inspect the museum rather
  than rely on caught knowledge, and reach current services before closing.
- Long-term structure: persistent knowledge and contributions; whole collection,
  museum construction and mayor/debt progression are outside the round.
- Common heuristics: leave pocket room, hold the tool separately, keep a first
  species for donation if desired and compare current sale information.
- Failure attribution: scare, early/late response, full pockets, duplicate
  refusal, closed shop and paid trash disposal have distinct outcomes.
- Player trust: readable current cues help explain outcomes without guaranteeing
  a shadow's species or the next randomly eligible appearance.
- Claim IDs: NL-002–NL-010.

## Replay and variation

- Habitat/date/hour and current population change eligible opportunities;
  retained caught/donated sets change the value of later specimens.
- No seed or next-species probability is reconstructed from sampled frames.
  Choosing release, private retention, contribution or sale can remain viable
  without requiring every choice in one round. Saving does not preserve a
  claimed exact live-fish position across absence.
- Claim IDs: NL-002–NL-010.

## Adjacent systems and history

- The original 3DS museum exists in the admitted established town; the
  New Horizons initial five-species service invitation is a different packet.
- Welcome amiibo and island/tournament modules are not merged into this scope.
  Fishing resemblance alone does not prove whole-genome equivalence.
- Claim IDs: NL-001/007/010–NL-012.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | ACT-008, ACT-089, ACT-091, ACT-130, ACT-199, ACT-219, ACT-424, ACT-476, ACT-673, ACT-704, ACT-705 | No additional candidate IDs; scoped parameters above |
| System Behaviour | SYS-921, SYS-922, SYS-1279, SYS-1444, SYS-1445, SYS-1446, SYS-1447, SYS-1448 | No additional candidate IDs; scoped parameters above |
| Constraint | CON-210, CON-790 | No additional candidate IDs; scoped parameters above |
| Information | INF-117, INF-128, INF-352, INF-461, INF-497 | No additional candidate IDs; scoped parameters above |
| Objective | OBJ-290 | No additional candidate IDs; scoped parameters above |
| Time | TIM-003, TIM-025 | No additional candidate IDs; scoped parameters above |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `510` (`GAME-0001`–`GAME-0510`).
- Exact genome matches: none.
- Tied near matches: `GAME-0320` — Animal Crossing: New Horizons (`9 / 41 = 0.219512`).
- Supported combination subsets: none.
- Scan date: 2026-10-06.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| GAME-0320 — Animal Crossing: New Horizons | ACT-008, ACT-091, ACT-199, ACT-476, SYS-921, SYS-922, INF-128, INF-352, TIM-025 | Both packets move a resident, hold a catching tool, cast/reel, record a specimen and use calendar eligibility with current capacity/wildlife cues. New Horizons instead requires gathering/crafting breakable flimsy tools, five distinct Tom Nook hand-ins, a legal tent marker and next-day recipes. Original New Leaf starts in an established town and retains ordinary quote/disposal, indoor ownership/recovery, permanent museum first-species/duplicate boundaries and explicit settlement saving; these are not the later game's initial service invitation. | 9 / 41 = 0.219512 |

### Preserved research notes

- New genes: ACT-704/705, SYS-1444–1448, CON-790, INF-497 and OBJ-290.
- Classification result: New gene.
- Evidence and reasoning: complete signatures and proper verified subsets are
  computed, not ranked by franchise, genre or illustration (NL-011/012).

## Taxonomy impact

- Registry changes: ten Active additions and nineteen unchanged transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_248](../../../research/taxonomy-changes/TAXONOMY_CHANGE_248.md).
- Candidate terms affected: none. No previous signature/definition, platform
  release audit or published r000024 mapping is edited.
- Claim IDs: NL-011/012.

## Negative results

- No new structured negative-result record. Island service invitation,
  crafting/tool wear, volume market repricing and selectable historical saves
  do not transfer, without being declared globally invalid.
- Claim IDs: NL-001/007–NL-011.

## Delta summary

## New facts

- [Observation | Corroborated | High] Caught knowledge, privately owned fish
  and public contribution are separate records with different choices (NL-004/007).
- [Observation | Corroborated | High] Live response and civil-time service
  eligibility constrain different parts of the same round (NL-002/003).
- [Observation | Limited | Medium] Full-pocket, indoor recovery and save
  continuation retain documentary rather than native replay evidence (NL-005/006/009).

## New genes

- [Observation | Corroborated | High] Capture approach, public collection and
  quote/disposal boundaries are isolated without New Horizons imports (NL-003/007/008).
- [Observation | Limited | Medium] Display recovery, overflow and saved
  settlement retain disclosed native limits (NL-005/006/009).

## New combinations

- [Observation | Direct | High] No motif-selected combination is created;
  every verified proper subset is scanned (NL-012).

## Taxonomy changes

- [Observation | Direct | High] TAXONOMY_CHANGE_248 accepts ten additions
  without changing an earlier signature or English definition (NL-011).

## New questions

- [Hypothesis | Limited | Medium] Controlled original-hardware overflow,
  indoor recovery and save continuation could refine the qualified transitions.
- [Hypothesis | Limited | Medium] A pinned original build could establish
  exact regional parity and timing without borrowing later-update mechanics.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0512 released PlayStation 5 Resident
  Evil Requiem follows accepted local commitment and the stop window.
- Optimisation criterion: approved modern/retro and platform alternation.
- Expected information gain: a complete dated survival packet, not a promised
  new-gene number or a presumed undocumented patch.
- Backlog impact: next unit 17/18 of Selection 039; no push/publication/deploy.

## Why this game

- [Hypothesis | Limited | Medium] The approved original 3DS slot contrasts
  ordinary live gathering and persistent collections with authored mission
  exits; admission still depends on the complete scoped signature.
