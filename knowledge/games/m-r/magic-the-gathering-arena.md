---
game_id: GAME-0185
slug: magic-the-gathering-arena
game_title: "Magic: The Gathering Arena"
analysis_status: reviewed
reviewed: 2026-08-29
combination_ids:
  - COMB-0183
gene_ids:
  action:
    - ACT-331
    - ACT-332
    - ACT-333
    - ACT-334
    - ACT-335
    - ACT-336
    - ACT-337
  system:
    - SYS-004
    - SYS-584
    - SYS-585
    - SYS-586
    - SYS-587
    - SYS-588
    - SYS-589
    - SYS-590
  constraint:
    - CON-174
    - CON-490
    - CON-491
    - CON-492
    - CON-493
    - CON-494
    - CON-495
  information:
    - INF-003
    - INF-239
  objective:
    - OBJ-109
  time:
    - TIM-019
---

# Game: Magic: The Gathering Arena

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: Windows PC live client `2026.62.30`, reviewed 2026-08-29;
  English-language `Starter Deck Duel`, one single-game player-versus-player
  match using the supplied 60-card **Arcane Aerialists** deck.
- Primary decision loop: keep or mulligan the opening hand; play at most one
  land on an eligible turn; use typed mana to cast spells or activate abilities;
  retain or pass priority around the LIFO stack; develop flying and supporting
  permanents; declare attackers or blockers; resolve card text, combat damage,
  zone changes and state-based actions; repeat until either player loses.
- Entry and exit: begins when Arcane Aerialists is selected in Starter Deck
  Duel and the client creates the opponent pairing and opening-hand state. It
  succeeds when the opponent first meets a legal loss predicate and fails when
  the controlled player does; the Arena victory, defeat or draw result overlay
  is the reproducible exit.
- Included: the exact supplied deck below; the client-presented seven-card
  opening hand and London mulligan; randomised library order without claiming a
  proprietary exact Best-of-One hand-selector distribution; 20 starting life;
  private hands and libraries; public battlefield, graveyard, exile and stack;
  land play, typed mana, spell casting, activated and triggered abilities;
  priority and consecutive passes; ordered phases and steps; flying, attacking,
  blocking and combat damage; permanent and non-permanent zone destinations;
  cleanup hand reduction; state-based lethal-creature removal; life-zero,
  empty-library draw, concession, card-defined and simultaneous terminals.
- Exact Arcane Aerialists list: `2 Healer's Hawk; 10 Plains; 1 Dawnwing Marshal;
  2 Deadly Riposte; 1 Giada, Font of Hope; 2 Helpful Hunter; 2 Inspiring
  Overseer; 3 Stasis Snare; 1 Angel of Finality; 2 Serra Angel; 1 Spectral
  Sailor; 9 Island; 2 Fog Bank; 2 Kitesail Corsair; 1 Curator of Destinies;
  2 Empyrean Eagle; 2 Cloudblazer; 4 Tranquil Cove; 1 Temple of Enlightenment;
  2 Chart a Course; 2 Goldvein Pick; 2 Faebloom Trick; 2 Dazzling Angel;
  2 Aegis Turtle`.
- Excluded: deck editing, importing, crafting, packs, wildcards and collection
  economy; Color Challenge, Sparky, ranked queues, Standard deck construction,
  Draft, Sealed, Brawl, Historic, Pioneer, Timeless and every rotating event;
  sideboards and best-of-three; quests, daily wins, achievements, season rank,
  rewards and post-match account progression; other supplied decks; tabletop
  handling, tournament policy and every rule or keyword not reachable from the
  declared deck/opponent packet; mobile input and cosmetic avatars, sleeves,
  pets and emotes.
- Potential scoped modules: another named Starter Deck Duel list; one current
  Standard constructed queue; a Draft event; digital-only Alchemy mechanics;
  sideboarding in one Traditional match; or collection/deck-construction
  economy.
- Direct-play status: not conducted. Current first-party client, product,
  starter-deck and rules material plus the bounded transition trace establish
  the packet. The client can automate passes and mana selection, but this record
  models their underlying player authority and does not claim an unpublished
  opening-hand or matchmaking algorithm.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MTGA-001` | `2026.62.30` is the current official Windows PC client boundary on the review date | Confirmed | Direct | High | P1, P2 |
| `MTGA-002` | Starter Deck Duel remains an official new-player PvP event and uses the ten Foundations supplied decks | Confirmed | Direct | High | P2–P4 |
| `MTGA-003` | Arcane Aerialists is the fixed 60-card white-blue list reproduced in this record | Confirmed | Direct | High | P4 |
| `MTGA-004` | A player begins with seven cards and may take London mulligans before the first turn | Confirmed | Direct | High | P5, P6 |
| `MTGA-005` | Ordinary land play, typed mana production and compatible cost payment bound spell availability | Confirmed | Direct | High | P2, P5, P6 |
| `MTGA-006` | Priority permits spells and abilities; consecutive passes resolve only the top LIFO stack object before priority returns | Confirmed | Direct | High | P5 |
| `MTGA-007` | Each turn has ordered beginning, main, combat, main and ending phases with untap, draw and cleanup actions | Confirmed | Direct | High | P5, P6 |
| `MTGA-008` | Attacker readiness, defender block legality, flying and power-based damage govern combat settlement | Confirmed | Direct | High | P5, P6 |
| `MTGA-009` | Resolved text routes objects among zones, creates triggers and precedes repeated state-based checks | Confirmed | Direct | High | P5 |
| `MTGA-010` | Zero life, drawing from an empty library, concession and applicable card text settle one game immediately | Confirmed | Direct | High | P5, P6 |
| `MTGA-011` | Arena exposes rules text, legal interactions and mana automation while retaining player priority and target choices | Observation | Corroborated | High | P2, P7, P8 |
| `MTGA-012` | The bounded game is a hidden-resource duel whose decisive loop is mana development into stack-aware flying combat | Observation | Corroborated | High | P2–P8, S1, V1 |

## Basic data

- Release / origin: developed by Wizards of the Coast's Digital Games Studio
  and published by Wizards of the Coast; the official maintained product title
  is **Magic: The Gathering Arena**.
- Platform or physical form: networked digital collectible-card game on PC,
  Mac and mobile; this record admits only the declared Windows PC live client.
- Puzzle family: hidden-information inference; tactical forecast and
  counterplay; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official patch notes `2026.62.30`](https://mtgarena-support.wizards.com/hc/en-us/articles/52859087044756-Patch-Notes-2026-62-30),
    dated 2026-08-24, for the current client version and Unity update.
  - **[P2]** [official MTG Arena product page](https://magic.wizards.com/en/mtgarena),
    for Windows availability, starter decks, Starter Deck Duels, five-colour
    mana, spells, abilities, online opponents and current digital presentation.
  - **[P3]** [official patch notes `2025.46.20`](https://mtgarena-support.wizards.com/hc/en-us/articles/35805365023124-Patch-Notes-2025-46-20),
    for the ten Foundations Starter Decks and their use in Starter Deck Duels.
  - **[P4]** [official Foundations starter-deck register](https://magic.wizards.com/en/news/mtg-arena/mtg-arena-announcements-november-18-2024),
    for the complete named Arcane Aerialists list.
  - **[P5]** [official Comprehensive Rules, 19 August 2026](https://media.wizards.com/2026/downloads/MagicCompRules%2020260819.txt),
    especially rules 103.1, 103.5, 104, 117, 305, 405, 500–510, 514 and 704
    for starting state, mulligan, priority, land play, stack, turns, combat,
    cleanup, state-based actions and terminals.
  - **[P6]** [official How to Play guide](https://magic.wizards.com/en/how-to-play),
    for the seven-card hand, 20-life objective, land/mana, five phases,
    attackers, blockers, damage and ordinary card destinations.
  - **[P7]** [official patch notes `2026.62.20`](https://mtgarena-support.wizards.com/hc/en-us/articles/52654279128084-Patch-Notes-2026-62-20),
    for current mana-pool highlighting and match-interface evidence.
  - **[P8]** [official Gameplay FAQ](https://mtgarena-support.wizards.com/hc/en-us/articles/360035728651-Gameplay-FAQ),
    for the maintained Arena digital format and Best-of-One/Best-of-Three
    distinction.
- Secondary reproduction source:
  - **[S1]** [TCGplayer Starter Deck Duel overview](https://www.tcgplayer.com/content/article/An-Introduction-to-Starter-Deck-Duel-on-MTG-Arena/6839d651-b67a-47f4-bf0c-f93bba2002e0/),
    used only to corroborate the free preconstructed ten-deck event and live
    random-opponent pairing; no rules claim depends on it alone.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P8` under the declared deck and exclusions; evidence-based rules
  reconstruction, not a direct-play claim.
- Claim IDs: `MTGA-001`–`MTGA-012`.

## Mechanical decomposition

### Action Genes

- New `ACT-331`: keep or mulligan the presented opening hand.
- New `ACT-332`: play one land from hand during an eligible main phase.
- New `ACT-333`: cast one visible-hand spell with its choices, targets and
  payable cost.
- New `ACT-334`: activate one controlled card ability and pay its cost.
- New `ACT-335`: pass priority without adding a new object.
- New `ACT-336`: declare any legal attacking creature subset.
- New `ACT-337`: assign legal untapped blockers to attackers.
- Parameters: hand, land allowance, spell or ability, mana, modes, targets,
  stack, priority, attacking set, blocker relation and evasion.
- Claim IDs: `MTGA-004`–`MTGA-008`, `MTGA-011`, `MTGA-012`.

### System Behaviour Genes

- Existing `SYS-004`: randomise the library and other rule-directed random
  selections without disclosing their future outcome.
- New `SYS-584`: present the opening hand and settle each London mulligan.
- New `SYS-585`: generate, spend and clear white, blue or generic-compatible
  mana.
- New `SYS-586`: advance ordered turn phases, untap, draw, cleanup and next
  active player.
- New `SYS-587`: retain spells and abilities on the LIFO stack and resolve its
  top after consecutive passes.
- New `SYS-588`: apply card text, route cards among zones and create triggers.
- New `SYS-589`: settle declared attackers, blockers and combat damage.
- New `SYS-590`: repeatedly apply state-based actions and settle the game result.
- Resolution order: establish shuffled libraries and kept opening hands;
  perform turn-based actions; give the active player priority; accept legal
  land, spell, ability or pass choices; after all players pass, resolve the top
  stack object or advance the step; check state-based actions before each new
  priority grant; use attacker/blocker declarations and response windows before
  combat damage; repeat until a result predicate ends the game immediately.
- Claim IDs: `MTGA-004`–`MTGA-012`.

### Constraint Genes

- Existing `CON-174`: a held card still requires a payable current cost and all
  required compatible targets.
- New `CON-490`: Starter Deck Duel admits the unedited supplied Arcane
  Aerialists list rather than a player-built deck.
- New `CON-491`: ordinary land play is limited to one per own turn in an
  eligible main phase with priority and empty stack.
- New `CON-492`: spell and ability timing depends on priority, card type, phase,
  step, stack and text.
- New `CON-493`: attackers must satisfy control-history, untapped, restriction
  and requirement rules.
- New `CON-494`: blocker assignments must satisfy readiness, flying/evasion and
  every current relation rule.
- New `CON-495`: an over-limit hand is reduced to the current maximum during
  cleanup, normally seven.
- Scarce strategic resources: cards in hand and library, once-per-turn land
  growth, typed mana, untapped creatures, life, priority opportunities, combat
  tempo and information about the opponent's concealed resources.
- Claim IDs: `MTGA-002`–`MTGA-010`, `MTGA-012`.

### Information Genes

- Existing `INF-003`: the opponent's hand identities and both current library
  orders exist but remain concealed until a rule reveals them.
- New `INF-239`: Arena exposes the player's hand, card text, public zones, life,
  phase, stack, prompts, legal highlights and mana forecast.
- Claim IDs: `MTGA-004`–`MTGA-012`.

### Objective Genes

- New `OBJ-109`: cause the opponent to meet a legal single-game loss condition
  before the controlled player.
- Success, evaluation and failure: ordinary play pressures life with creature
  combat, but empty-library draws, concessions and card-defined outcomes remain
  legal terminals. The first settled loss ends the game; post-match rewards and
  ranked evaluation are outside the objective.
- Claim IDs: `MTGA-010`, `MTGA-012`.

### Time Genes

- New `TIM-019`: active turns alternate, but both players act through nested
  priority windows; consecutive passes determine object or phase advancement.
- Claim IDs: `MTGA-006`–`MTGA-009`, `MTGA-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Starter Deck Duel event is open and ten supplied lists are available | Select Arcane Aerialists | The fixed 60-card list is admitted without edits or sideboard construction and pairing begins | immutable supplied-deck entry | `MTGA-002`, `MTGA-003` |
| Seven client-presented cards form the first opening hand | Choose Mulligan | A replacement seven is presented, then one card is put on the library bottom before a final keep; an unpublished selection distribution is not inferred | bounded opening-hand revision | `MTGA-004` |
| Kept hand contains Plains and a white spell; it is the player's eligible main phase | Play Plains | Plains enters the battlefield without becoming a stack object; the ordinary land allowance is consumed | land growth is separate from casting | `MTGA-005` |
| Untapped Plains is controlled and a white payment is required | Activate its mana ability or accept Arena autotap | White mana enters the pool and can pay the compatible symbol; unused ordinary mana clears at the phase/step boundary | typed renewable payment | `MTGA-005`, `MTGA-011` |
| The player has priority, sufficient mana and a creature card in hand during an eligible main phase | Cast the creature | Choices and cost are committed; the spell enters the stack rather than the battlefield | cast and resolution are separate | `MTGA-005`, `MTGA-006` |
| A creature spell is on the stack and the opponent receives priority | Opponent casts a legal instant, then both players pass | The instant, as top object, resolves first; priority returns before the creature spell can resolve | LIFO response order | `MTGA-006` |
| The creature spell becomes the top object and both players pass | Pass priority | Card text resolves and the permanent enters the battlefield; any enter trigger becomes a new stack object | type-specific zone routing and triggers | `MTGA-006`, `MTGA-009` |
| A newly entered ordinary creature lacks haste | Attempt to attack this turn | Arena rejects the declaration; on a later turn after untap and continuous control it can be selected | readiness includes control history | `MTGA-007`, `MTGA-008` |
| Several ready creatures exist at declare attackers | Select two legal flyers and confirm | The attackers tap and remain attacking through blocker declaration unless an effect removes them | simultaneous attacker subset | `MTGA-008` |
| A flying attacker is declared and defender has one ground creature and one untapped flyer | Assign the ground creature, then the flyer | The ground block is illegal; the flying block is accepted and establishes the combat relation | typed evasion gates defence | `MTGA-008`, `MTGA-011` |
| A blocked 2/2 and 2/2 assign ordinary combat damage | Pass through the damage step | They mark two damage on each other simultaneously; state-based actions destroy both before priority returns | combat and lethal checking are separate | `MTGA-008`, `MTGA-009` |
| An unblocked flyer assigns enough damage to reduce opponent life from two to zero | Complete combat damage | State-based actions make the opponent lose and Arena opens the victory overlay immediately | bounded success terminal | `MTGA-010` |
| A player must draw while their library contains no cards | Advance to that draw | The failed draw is recorded and the player loses at the next state-based check; the inverse outcome is defeat | alternate rules-level terminal | `MTGA-010` |

## Strategic and experiential structure

- Local decision: spend mana now or preserve an instant-speed response; add a
  flyer, remove a blocker, attack into disclosed defence, hold a creature back
  or pass priority without revealing whether the hand can interact.
- Medium-term planning: sequence lands and coloured sources, curve creatures
  into Empyrean Eagle or Giada support, use flying to bypass ground blockers,
  preserve Stasis Snare or Deadly Riposte for threats, and avoid overcommitting
  into unknown opposing cards.
- Long-term structure: turn a concealed finite library into a widening public
  battlefield while keeping life and cards sufficient to win the damage race
  before the opponent's deck or card advantage stabilises.
- Common heuristics: keep functional land/spell ratios; play precombat effects
  only when their information benefit exceeds surprise; attack with flyers
  when ground blockers cannot interact; leave coloured mana untapped to
  represent a response; order triggers and spells so the newest stack object
  protects or enables the older one.
- Failure attribution: own hand, public cards, stack order, life, mana and legal
  prompts are inspectable, but opponent hand identities and both future draw
  orders make intent and exact outcomes partly uncertain.
- Player-trust factors: visible card text, target highlights, priority stops and
  stack order explain legal choices; Arena's convenience automation must not be
  mistaken for removal of player authority or disclosure of its proprietary
  opening-hand probabilities.
- Claim IDs: `MTGA-004`–`MTGA-012`.

## Replay and variation

- What changes between sessions: opponent and supplied deck, shuffled library
  orders, presented hands, mulligan choices, draws, spell sequencing, targets,
  attacks, blocks and terminal route.
- Randomness or procedural generation: libraries are shuffled and Arena
  selects the pairing and presented Best-of-One opening state; this record does
  not invent probabilities the first party does not publish.
- Multiple viable strategies: yes; Arcane Aerialists can curve evasive pressure,
  trade defensively while gaining life, build flying synergies, hold removal or
  pivot around the opponent's ground/flying composition.
- Typical replay motive: learn all ten fixed starter matchups and improve
  mulligan, mana, priority and combat sequencing without collection cost.
- Claim IDs: `MTGA-002`–`MTGA-012`.

## Adjacent systems and history

- Direct predecessors: tabletop Magic supplies the maintained rules kernel;
  Arena implements it as a digital rules engine with matchmaking, visibility,
  prompts and automation.
- Variants: Standard construction, ranked Best-of-One, Traditional
  Best-of-Three, Draft, Sealed, Brawl, Historic, Pioneer, Timeless, Alchemy and
  rotating events change admitted cards, entry or match structure and remain
  outside scope.
- Similar games: Slay the Spire, Balatro, Inscryption and other digital
  adversarial card-rule engines.
- Important differences: unlike Slay the Spire, a human opponent can act inside
  either player's turn and effects queue on a response stack rather than an
  autonomous hostile phase. Unlike Balatro, cards create persistent public and
  private zones instead of one score pattern. Unlike Inscryption, combat is not
  fixed to four paired lanes or a five-point balance scale.
- Claim IDs: `MTGA-002`–`MTGA-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-331`–`ACT-337` | mulligan, land, spell, ability, priority, attacker and blocker parameters |
| System Behaviour | `SYS-004`, `SYS-584`–`SYS-590` | shuffle, hand, mana, phase, stack, text, combat and terminal parameters |
| Constraint | `CON-174`, `CON-490`–`CON-495` | supplied deck, land, timing, cost, attack, block and cleanup parameters |
| Information | `INF-003`, `INF-239` | private cards, public zones, card text, prompts and stack |
| Objective | `OBJ-109` | life, library, concession, card text and result |
| Time | `TIM-019` | active turn, phase, priority, passes and response windows |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `184` (`GAME-0001`–`GAME-0184`).
- Exact genome matches: none.
- Tied near matches: `GAME-0120` — Slay the Spire (`3 / 52 = 0.057692`).
- Supported combination subsets: `COMB-0183`.
- Scan date: 2026-08-29.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0120` — Slay the Spire | `SYS-004`, `CON-174`, `INF-003` | both conceal future draw order and gate a held card by cost and target, but Arena adds a human opponent, typed land mana, response priority, a LIFO stack, persistent blockers and rules-level player-loss terminals instead of one planning phase followed by autonomous intents | Near, `0.057692` |

### Preserved research notes

- New genes: `ACT-331`–`ACT-337`, `SYS-584`–`SYS-590`, `CON-490`–`CON-495`,
  `INF-239`, `OBJ-109` and `TIM-019`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: only random selection, cost/target compatibility and
  fixed concealed state reuse safely; turn ownership, priority, stack, land,
  mana and two-sided combat do not fit earlier solitary-deck phase genes.

## Combination status

- `COMB-0183` is a verified strict twenty-one-gene subset of the twenty-six-gene
  genome, coupling land and mana development to priority, LIFO stack resolution,
  two-sided creature combat and the first legal player-loss terminal.
- Every earlier verified combination is tested deterministically after
  registration.

## Taxonomy impact

- Registry changes: twenty-three new Active genes, links on three reused genes,
  `COMB-0183` and three existing family memberships.
- Taxonomy-change record: none; no prior lifecycle, definition or reviewed game
  signature changes.
- Candidate terms affected: opening mulligan, land play, spell casting,
  activated ability, priority pass, attacker/blocker declaration, typed mana,
  phase progression, LIFO stack, card-zone resolution, combat damage,
  state-based terminal, supplied-deck admission, timing, readiness, evasion,
  cleanup hand size, public card-rule interface and nested priority time.

## Negative results

- `ACT-125` and `SYS-163` are not reused: Slay the Spire plays a card into
  immediate single-player effect resolution, while Arena spells become
  response-capable stack objects and permanents may remain on the battlefield.
- `ACT-126`, `SYS-164` and `TIM-005` are not reused: ending a solitary planning
  phase for autonomous hostile intent is not equivalent to passes by two human
  players inside either active turn.
- `ACT-135`, `SYS-172`, `CON-180`, `CON-182` and `OBJ-057` are not reused:
  Inscryption's four fixed paired lanes and relative damage scale do not model
  freely declared attackers, many-to-one blockers or life/library terminals.
- `CON-043` is not reused because Arena may temporarily hold more than seven
  cards and forces reduction only during cleanup; it is not a hard visible-hand
  capacity throughout the turn.
- Tabletop-only handling, tournament policy, other formats and unreachable card
  mechanics are not admitted simply because the Comprehensive Rules contain
  them.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Current MTG Arena Starter Deck Duel supports one
  fixed Arcane Aerialists game whose player authority spans opening hand, mana,
  priority, stack, combat and state-based terminal (`MTGA-001`–`MTGA-012`).

## Нові гени

- [Observation | Corroborated | High] Added twenty-three genes for opening
  mulligan, land/mana, spell/ability commitment, priority, turn/stack/card-text
  resolution, attacker/blocker combat, timing, cleanup, public rules state and
  single-game terminal.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0183` isolates land-to-mana-to-stack
  development through two-sided flying combat into the first legal loss.

## Зміни таксономії

- [Observation | Corroborated | High] No lifecycle migration or signature
  change; three established generic genes remain unchanged.

## Нові питання

- Which later adversarial card game reuses nested response priority while
  replacing typed land mana, free attacker/blocker assignment or the loss
  predicates?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0186` — Don't Starve Together.
- Optimisation criterion: continue the recorded demand-led Goal in exact order.
- Expected information gain: replace a discrete hidden-card rules engine with
  cooperative embodied survival, seasonal systems and an explicit first-winter
  checkpoint.
- Backlog impact: sixth of nine authorised game units.

## Чому саме вона

- [Confirmed | Direct | High] It is the next immutable subject in
  `SEARCH_DEMAND_GAME_SELECTION_006`.

## Localisation status

- Ukrainian game, new-gene and combination entries are reviewed in this unit.
- The canonical brand title remains `Magic: The Gathering Arena`; the
  explanatory Ukrainian title is presentation-only.

## Open questions

- Recheck the live client, supplied starter-deck rotation and exact event entry
  before later review-on-touch; do not infer an unpublished Best-of-One
  opening-hand probability.
