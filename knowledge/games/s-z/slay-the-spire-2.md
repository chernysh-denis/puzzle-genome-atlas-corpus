---
game_id: GAME-0155
slug: slay-the-spire-2
game_title: Slay the Spire 2
analysis_status: reviewed
reviewed: 2026-08-26
combination_ids:
  - COMB-0119
  - COMB-0153
gene_ids:
  action:
    - ACT-125
    - ACT-126
    - ACT-127
    - ACT-128
    - ACT-129
    - ACT-130
    - ACT-131
    - ACT-254
  system:
    - SYS-004
    - SYS-087
    - SYS-163
    - SYS-164
    - SYS-165
    - SYS-166
    - SYS-167
    - SYS-168
    - SYS-424
    - SYS-425
    - SYS-426
  constraint:
    - CON-043
    - CON-094
    - CON-174
    - CON-175
    - CON-176
    - CON-177
    - CON-178
    - CON-373
    - CON-374
    - CON-375
  information:
    - INF-002
    - INF-003
    - INF-061
    - INF-062
  objective:
    - OBJ-029
    - OBJ-055
  time:
    - TIM-005
---

# Game: Slay the Spire 2

## Analysis scope

- Version / ruleset: PC Steam main branch `v0.107.1`, standard single-player
  Ascension 0 as the unlocked Necrobinder, from character selection through an
  ordinary Act 3 boss victory and the resulting `Spireborn` Timeline Epoch.
- Primary decision loop: inspect the route and hostile intents, convert the
  current hand and Energy into damage, Block or Osty state, then trade route,
  reward, quest, enchantment and Ancient-boon choices against persistent health
  and deck quality until the Act 3 boss and post-run Epoch settlement.
- Reproducible entry: use an unmodded profile on which the Regent has completed
  one run and the Necrobinder is therefore selectable; choose Necrobinder,
  single-player and Ascension 0 on the `v0.107.1` main branch, then begin before
  the Act 1 Ancient choice.
- Reproducible exit: defeat the ordinary Act 3 boss, reach the run-victory
  summary, reveal the `Spireborn` Epoch for the first Necrobinder Act 3 clear
  and return to the Timeline or main-menu boundary.
- Included: one randomly selected unlocked Act 1 variant; generated routes and
  ordinary node categories through three acts; mandatory Ancient relic choice
  at each act entry; Necrobinder cards, Osty, Summon, Souls and Doom; persistent
  health, deck, relics, potions and gold; card rewards, shops, rest sites,
  events, Quest cards and card Enchantments; ordinary score and milestone
  processing only where it reveals the named Epoch and expands future pools.
- Excluded: the optional beta branch and its later balance/content; co-op,
  Daily, Custom, seeded comparison and mods; other characters as controlled
  runs; Ascension modifiers above zero; score optimisation and exhaustive
  Badges; unreleased achievements; future alternate Acts 2 or 3, experimental
  modes, achievements, Act 4, true victory and every announced 1.0 feature;
  exhaustive cards, relics, potions, events, enemies, bosses and exact balance.
- Direct-play status: no paid-account run was performed for this unit. The
  version and unstable Early Access boundary were time-stamped against Mega
  Crit and Steam material; transition details were cross-checked against the
  maintained rules reference. Exact numerical balance remains parameterised.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `STS2-001` | Main branch `v0.107.1` is a three-act Early Access game whose ordinary current run ends after the Act 3 boss, while true victory remains future work | Confirmed | Corroborated | High | P1, P2, P4, S8 |
| `STS2-002` | The persistent-deck, Energy, intent, Block, route, reward, relic, potion and terminal-health loop from Slay the Spire recurs | Confirmed | Corroborated | High | P1, S1, S4, S8 |
| `STS2-003` | Each act begins with an Ancient and requires one selection from a bounded boon offer; later-act Ancient identity varies with unlocked pools | Confirmed | Corroborated | High | S1, S7 |
| `STS2-004` | An unlocked Act 1 is chosen between Overgrowth and Underdocks before its generated route, changing the act-specific encounter pool without player route selection | Confirmed | Corroborated | High | S1, S6 |
| `STS2-005` | Living Osty absorbs the Necrobinder's otherwise unblocked attack damage and can perform card-commanded attacks; dead Osty cannot attack until Summon restores it | Confirmed | Corroborated | High | S2, S3 |
| `STS2-006` | Soul tokens are generated into combat zones, draw cards at zero Energy and Exhaust; they never become persistent deck members | Confirmed | Corroborated | High | S3, S4 |
| `STS2-007` | A Quest card is an unplayable deck burden until its later predicate grants the declared reward and removes the card | Confirmed | Corroborated | High | S4, S9 |
| `STS2-008` | An Enchantment permanently changes one card object for the run; one card accepts at most one enchantment and ordinary replacement or removal is forbidden | Confirmed | Corroborated | High | P3, S5 |
| `STS2-009` | Completing Necrobinder milestones reveals Timeline Epochs that expose story and add declared cards, relics or potions to future pools | Confirmed | Corroborated | High | S2, S6 |
| `STS2-010` | Defeating Act 3 as Necrobinder reveals `Spireborn` and unlocks Potion of Doom, Bone Brew and Pot of Ghouls | Confirmed | Corroborated | High | S2, S6 |

## Basic data

- Release / origin: Mega Crit developed and published Slay the Spire 2 in
  Steam Early Access on 5 March 2026. This unit freezes the main-branch state
  after Major Update 2, `v0.107.1`, released 19 June 2026.
- Platform or physical form: digital turn-based roguelike deckbuilder on PC,
  macOS and Linux during the scoped Early Access period.
- Puzzle family: persistent combat-deck construction; telegraphed turn combat;
  branching attrition route; card-bound modifiers and milestone metaprogression.
- Primary and creator sources: **[P1]** [official Steam product and Early
  Access page](https://store.steampowered.com/app/2868840/Slay_the_Spire_2/),
  for release, five characters, solo/co-op boundary and explicit future true
  ending; **[P2]** [official Major Update 2 announcement](https://steamcommunity.com/app/2868840/announcements/),
  for main-branch `v0.107.1`, Bestiary, Workshop and current boss replacement;
  **[P3]** [Mega Crit August 2026 Neowsletter](https://www.megacrit.com/news/2026-8-14-neowsletter-issue-25/),
  for current roadmap state and the explicit one-enchantment rule; **[P4]**
  [Mega Crit April 2026 roadmap](https://www.megacrit.com/news/2026-4-17-neowsletter-issue-21/),
  for future alternate acts, character, modes and true victory exclusions.
- Reproducible rules references: **[S1]** [Slay the Spire Wiki — Acts](https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2%3AActs),
  for three acts, alternate Act 1, Ancient entry and boss exit; **[S2]**
  [Necrobinder](https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2%3ANecrobinder),
  for unlock, loadout, Osty and milestone rewards; **[S3]** [Osty](https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2%3AOsty)
  and [Soul](https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2%3ASoul), for
  proxy damage and token-card transitions; **[S4]** [Cards](https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2%3ACards),
  for card types and Quest removal; **[S5]** [Enchantments](https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2%3AEnchantments),
  for run permanence and single-slot restriction; **[S6]** [Timeline](https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2%3ATimeline),
  for Epoch predicates and rewards; **[S7]** [Ancients](https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2%3AAncients),
  for boon selection and pools; **[S8]** [Map Locations](https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2%3AMap_Locations),
  for rewards and Act 3 victory; **[S9]** [Events](https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2%3AEvents),
  for Quest sources and delayed effects.
- Claim IDs: `STS2-001`–`STS2-010`.

## Mechanical decomposition

### Action Genes

- `ACT-125`–`ACT-131` recur for card play, End Turn, route, reward, persistent
  card editing, shops and potions. `ACT-129` includes selecting a legal card for
  a run-persistent Enchantment. `ACT-254` chooses one mandatory offered Ancient
  relic at the beginning of an act.
- Candidate genes: none.
- Parameters: card identity, Necrobinder/Osty effect source, Energy, node,
  reward offer, Ancient, boon, quest predicate and enchantment.
- Claim IDs: `STS2-002`, `STS2-003`, `STS2-005`–`STS2-008`.

### System Behaviour Genes

- `SYS-004`, `SYS-087`, `SYS-163`–`SYS-168` retain seeded uncertainty, hand
  turnover, card text, intents, Block, relic triggers, persistent run state and
  generated act routes. `SYS-424` routes eligible unblocked attack damage and
  card-commanded attacks through Osty's current combat state. `SYS-425` watches
  a persistent Quest-card predicate, grants its deferred route reward and
  removes the burden. `SYS-426` converts run and character milestones into
  revealed Epochs and new future-run content-pool members.
- Resolution order: resolve each legal card completely; at End Turn apply
  Doom terminal checks and other end-turn effects, discard, execute disclosed
  enemy intents, route eligible unblocked attack damage through living Osty,
  then refresh Energy and draw. At node and act boundaries persist the run,
  test quests, select the required Ancient boon and generate the next route.
  After terminal settlement, compute milestones and reveal eligible Epochs.
- Claim IDs: `STS2-002`–`STS2-010`.

### Constraint Genes

- `CON-043`, `CON-094`, `CON-174`–`CON-178` retain hand, Energy, card target,
  health, route, potion-slot and persistent-deck boundaries. `CON-373` permits
  Osty attacks and interception only while Osty is alive and limits protection
  to eligible attack damage. `CON-374` keeps an unresolved Quest card
  unplayable and protected from ordinary removal until its predicate resolves.
  `CON-375` allows at most one non-replaceable Enchantment on one persistent
  card object.
- Scarce strategic resources: health, Osty health, Energy, hand access, deck
  consistency, gold, potion slots, route access and legal enchantment targets.
- Claim IDs: `STS2-002`, `STS2-005`, `STS2-007`, `STS2-008`.

### Information Genes

- `INF-002` hides future act, encounter and reward outcomes; `INF-003` hides
  current draw order; `INF-061` previews hostile intent; `INF-062` reveals
  route categories and connections. Visible cards and status panels disclose
  Osty health, Quest text and Enchantment marks as parameters of current state.
- Candidate genes: none.
- Claim IDs: `STS2-002`–`STS2-008`.

### Objective Genes

- `OBJ-029` clears each finite encounter and `OBJ-055` defeats the Act 3 boss
  in one continuous climb. The `Spireborn` reveal is a deterministic settlement
  consequence of the scoped victory, not a substitute victory objective.
- Success, evaluation and failure: player health reaching zero ends the run;
  an Osty death changes available defence and card effects but does not itself
  end the run. Act 3 boss defeat records ordinary victory; no true-victory
  claim is made.
- Claim IDs: `STS2-001`, `STS2-005`, `STS2-009`, `STS2-010`.

### Time Genes

- `TIM-005` retains a self-paced player phase with flexible card and potion
  actions before explicit hostile resolution.
- Candidate genes: none.
- Claim IDs: `STS2-002`, `STS2-005`–`STS2-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Necrobinder begins an act before a three-relic Ancient offer | Select one offered relic | the selected relic enters run state and progression continues; the offer cannot be skipped | act-entry choice is a mandatory bounded action | `STS2-003` |
| Osty is alive with four HP, Necrobinder has no Block and receives a six-damage Attack | End Turn and resolve the intent | Osty loses four HP and dies; the remaining two damage reduce Necrobinder health | proxy health intercepts only the eligible remainder | `STS2-005` |
| Osty is dead and `Unleash` is held | Play `Unleash`, then play a card that Summons | the first Osty attack has no effect; Summon restores Osty with its declared HP so later Osty attacks become legal | proxy-dependent card effects are state-gated | `STS2-005` |
| A generated Soul is in hand | Play Soul | no Energy is paid, cards are drawn and Soul enters Exhaust rather than the persistent deck | token circulation is combat-local | `STS2-006` |
| An unresolved Quest card is in the deck | Draw it before satisfying its named predicate | it cannot be played or ordinarily removed and therefore occupies draw access | deferred reward has a current deck cost | `STS2-007` |
| The Quest predicate is satisfied at its declared later node | Enter or complete that node | the reward resolves and the Quest card is removed from the deck | route state settles a persistent card contract | `STS2-007` |
| One eligible deck card has no Enchantment | Accept an event or relic Enchantment for it | the effect becomes part of that card object for the run; another Enchantment cannot replace or stack with it | card-object improvement is persistent and slot-limited | `STS2-008` |
| The Act 3 boss reaches zero HP while Necrobinder lives | Complete combat and settle the run | ordinary victory is recorded, `Spireborn` is revealed and three Necrobinder potions enter future pools | run victory and account-pool expansion are distinct ordered states | `STS2-009`, `STS2-010` |

## Strategic and experiential structure

- Local decision: balance direct Block against raising Osty, since surviving
  proxy health can absorb later attack damage and enable Osty-labelled attacks.
- Medium-term planning: keep deck draw quality while accepting cards, Quests
  and Enchantments whose delayed value fits the visible act route and current
  Ancient relic.
- Long-term structure: adapt to the selected Act 1 environment and generated
  routes, accumulate enough deck efficiency and persistent health to defeat
  three bosses, then convert the clear into explicit future-pool expansion.
- Common heuristics: do not treat Osty health as ordinary Block; avoid relying
  on Osty cards while dead; accept a Quest only when its delayed node is
  plausible; reserve the one Enchantment slot for a card worth repeated draws.
- Failure attribution: hand, Energy, intents, health, Osty state, route, Quest
  text and Enchantment are visible; future act identity, nodes and rewards are
  seeded but unknown.
- Player-trust factors: Early Access volatility is separated from the frozen
  main build, and future true victory is explicitly outside the current result.
- Claim IDs: `STS2-001`–`STS2-010`.

## Replay and variation

- What changes between sessions: Act 1 identity, route, enemies, bosses,
  Ancient, offers, events, Quests, Enchantments, deck and revealed Epochs.
- Randomness or procedural generation: seeded act and route selection governs
  many future states; the current draw order is concealed after shuffle.
- Multiple viable strategies: Necrobinder can emphasise Osty durability,
  Souls, Doom, Ethereal effects or mixtures conditioned by rewards.
- Typical replay motive: test another build and route, unlock more Timeline
  content and later climb excluded Ascension levels.
- Claim IDs: `STS2-002`–`STS2-010`.

## Adjacent systems and history

- Direct predecessor: Slay the Spire supplies the 29-gene persistent deck,
  telegraphed combat and branching climb substrate reused here.
- Variants: co-op adds shared targeting and multiplayer cards; Ascension adds
  cumulative difficulty; beta adds experimental balance. All are excluded.
- Similar games: Slay the Spire, Balatro and Inscryption.
- Important differences: the sequel retains the first game's run skeleton but
  adds a mandatory Ancient reward at every act, randomly selected alternate
  Act 1 content, card-bound Quests and Enchantments, Necrobinder's damage proxy
  and a shared milestone Timeline. Balatro still lacks persistent encounter
  health; Inscryption's scoped run resets through authored cabin progression
  rather than this three-act ordinary-victory settlement.
- Claim IDs: `STS2-001`–`STS2-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-125`–`ACT-131`, `ACT-254` | card, target, route, reward, Ancient and boon parameters |
| System Behaviour | `SYS-004`, `SYS-087`, `SYS-163`–`SYS-168`, `SYS-424`–`SYS-426` | proxy, quest, milestone and pool parameters |
| Constraint | `CON-043`, `CON-094`, `CON-174`–`CON-178`, `CON-373`–`CON-375` | health, proxy, Quest and Enchantment gates |
| Information | `INF-002`, `INF-003`, `INF-061`, `INF-062` | draw, intent, route and future-state disclosure |
| Objective | `OBJ-029`, `OBJ-055` | hostile set, act and boss parameters |
| Time | `TIM-005` | actions per phase and hostile order |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `154` (`GAME-0001`–`GAME-0154`).
- Exact genome matches: none.
- Tied near matches: `GAME-0120` — Slay the Spire (`29 / 36 = 0.805556`).
- Supported combination subsets: `COMB-0119`, `COMB-0153`.
- Scan date: 2026-08-26.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Slay the Spire (`GAME-0120`) | `ACT-125`–`ACT-131`, `SYS-004`, `SYS-087`, `SYS-163`–`SYS-168`, `CON-043`, `CON-094`, `CON-174`–`CON-178`, `INF-002`, `INF-003`, `INF-061`, `INF-062`, `OBJ-029`, `OBJ-055`, `TIM-005` | mandatory Ancient-boon commitment, card-commanded Osty proxy, Quest-card contracts, one-slot Enchantments and post-run Timeline pool expansion versus the predecessor's scoped Ironclad climb without those admitted boundaries | Near, `0.805556` |

### Preserved research notes

- New genes: `ACT-254`, `SYS-424`–`SYS-426`, `CON-373`–`CON-375`.
- Classification result: recurrence of `COMB-0119` plus a new combination of
  reused deck-climb rules and new proxy, delayed-contract, card-slot and
  milestone-pool boundaries.
- Evidence and reasoning: 29 predecessor genes recur exactly. New records are
  limited to decisions or transitions that cannot be expressed as a changed
  numeric card, route or reward parameter.

## Combination record

- Slay the Spire 2 becomes the second analysed supporter of
  [`COMB-0119`](../../combinations/COMB-0119.md).
- Registered [`COMB-0153`](../../combinations/COMB-0153.md), a proper subset
  centred on card-commanded proxy survival and delayed card contracts inside a
  persistent three-act climb.

## Taxonomy impact

- Registry changes: add seven active genes and `COMB-0153`; add Slay the Spire
  2 evidence to the recurring predecessor genes without changing any earlier
  game signature.
- Taxonomy-change record: none.
- Candidate terms affected: deckbuilder, archetype, build, act pool, Doom and
  Soul remain genre, strategy, named effect or parameter vocabulary.

## Negative results

- Alternate Act 1 does not add a gene beyond `SYS-004` plus `SYS-168`: it is a
  seeded act-and-pool parameter followed by the same finite route generation.
- Souls do not add a persistent-deck gene because they are generated token
  cards that Exhaust within combat and already resolve through `SYS-163`.
- Doom remains card/status effect text under `SYS-163`, not a separate global
  objective or timing gene.
- The future true ending, achievements and announced alternate Acts 2 and 3
  are not current rules and therefore cannot support genes.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Main `v0.107.1` preserves the original
  29-gene climb while adding Ancients, Osty, Quests, Enchantments and Timeline
  settlement (`STS2-001`–`STS2-010`).

## Нові гени

- [Observation | Corroborated | High] `ACT-254`, `SYS-424`–`SYS-426`,
  `CON-373`–`CON-375`.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0119` gains a second supporter;
  `COMB-0153` isolates the sequel's proxy-and-contract climb.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; жодної ранішої
  signature не змінено.

## Нові питання

- Чи Strands потребує окремої межі для пошуку слів на повній тематичній сітці,
  чи поточні word-search і exhaustive-classification genes уже достатні?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0156` — Strands.
- Optimisation criterion: continue the authorised nine-game Goal after a
  version-bounded Early Access unit with a small deterministic daily puzzle.
- Expected information gain: test theme-word discovery, spanning spangram and
  full-grid exhaustion against Wordle and other fixed-evidence puzzles.
- Backlog impact: advances the recorded order without displacing `GAME-0157`
  Split Fiction or later authorised subjects.

## Чому саме вона

- [Hypothesis | Limited | High] Strands shifts from a large stochastic run to
  a compact inspectable board, improving the next unit's evidence contrast.
