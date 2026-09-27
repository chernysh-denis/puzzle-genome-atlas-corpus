---
game_id: GAME-0405
slug: fable-ii
game_title: Fable II
analysis_status: reviewed
reviewed: 2026-09-26
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-089
    - ACT-091
    - ACT-130
    - ACT-161
    - ACT-232
    - ACT-341
  system:
    - SYS-215
    - SYS-379
    - SYS-477
    - SYS-1084
  constraint:
    - CON-136
  information:
    - INF-117
    - INF-125
  objective:
    - OBJ-238
  time:
    - TIM-003
---

# Game: Fable II

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Rose, Murgo,
Derek, Arfur, Rex, the warrants and the music box are carrier parameters,
not gene names.

## Analysis scope

- Version / ruleset: original 2008 English-language Xbox 360 base-game
  *Fable II* childhood opening in Bowerstone Old Town. The exact disc
  revision was not inspected. Later Xbox compatibility packaging, *Fable*,
  DLC, Pub Games and sequel rules are not interchangeable evidence.
- Structured target: the five-gold music-box interval, **not** the whole
  named childhood chapter. Enter immediately after Murgo offers the box and
  Theresa supports Rose's wish, before collecting a task payment. Exit after
  buying and activating the box, before the sleep, castle audience and time
  jump. The original Xbox 360 title is the `analysisTarget` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: follow the current golden trail or map prompt to a
  local one-coin errand; collect or deliver its addressed item, choose the
  recipient or good/evil response, or resolve a small live fight; retain the
  payment and conduct/quest flags; repeat until five coins are available,
  then pay Murgo and activate the music box.
- Positive terminal: the five-gold price has been paid and the purchased box
  has been activated and vanished. The later castle invitation, Lucien scene,
  ten-year jump and adult Bowerstone response are outside this terminal.
- Negative boundary: unfinished errands or fewer than five gold keep the
  purchase unavailable. The source-bounded packet has no verified global
  fail timer or terminal child death state; exact combat damage and reload
  semantics are not inferred.
- Included: the five local payment routes—warrants, Monty's letter, Barnum's
  photograph, bottle delivery, and warehouse beetles/stock; Rex's first
  live stick fight and warehouse toy-gun choice; collection and addressed
  hand-in; helpful or exploitative branch commitment; one coin for each
  completed errand; persisted alignment and warrant/Old Town consequence
  flag; visible money, offer and navigational guidance; price gate, purchase
  and activation of the box.
- Excluded: the later town rendering or exact discounts; sleep, castle,
  Lucien, Rose's death and the adult time jump; adult melee/ranged/magic
  upgrades, health/death rules, property, marriage, jobs, renown, dog treasure,
  DLC, imported Pub Games money, side quests and later campaign endings.
- Reproducibility: start an unmodified fresh Xbox 360 base-game save with no
  imported gold. Record edition/revision, five errands and chosen branches,
  coin balance before and after each payment, alignment feedback, warrant
  recipient flag, trail/offer displays, Rex/beetle combat, box price,
  purchase and disappearance. Repeat with warrants given to Derek and to
  Arfur; the later Old Town appearance can be tested as a separate module.
- Direct-play status: no original disc, console, save, screenshot, video,
  audio or input trace was inspected. The original instruction booklet and
  two contemporary written original-game routes support this reconstruction;
  exact executable behaviour remains unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `F2-001` | The title is the original Xbox 360 *Fable II*, not the first *Fable* or a later game | Confirmed | Direct | High | P1, P2 |
| `F2-002` | Murgo's music box costs five gold and five Old Town errands each offer one coin | Observation | Corroborated | High | S1, S2 |
| `F2-003` | Warrants may go to guard Derek or criminal Arfur; both pay, but the choice changes alignment and the later Old Town state | Observation | Corroborated | High | S1, S2 |
| `F2-004` | The letter, bottle, photo and warehouse errands also admit opposed responses while retaining their payment | Observation | Corroborated | Medium | S1, S2 |
| `F2-005` | Rex is fought with a child's stick; warehouse beetles may be shot with a toy gun instead of destroying stock | Observation | Corroborated | High | S1, S2 |
| `F2-006` | A golden trail gives current route guidance, and eligible good/evil acts influence persistent appearance or reactions | Observation | Direct | High | P2 |
| `F2-007` | After five gold, the box can be bought and used; it disappears before the sleep/castle sequence | Observation | Corroborated | High | S1, S2 |
| `F2-008` | Exact child combat damage, death/reload state and the later quantitative Old Town effect were not verified | Hypothesis | Limited | Low | S1, S2 |

## Basic data

- Origin / platform: Lionhead Studios and Microsoft Game Studios, original
  2008 Xbox 360 base game; `PLAT-XBOX-360`.
- Puzzle family: ordered dependency sequencing (`FAM-017`): independent local
  errands feed a fixed purchase and activation gate, but their moral branches
  are not prerequisites for each other.
- **[P1]** [Official Xbox *Fable II* product
  page](https://www.xbox.com/en-US/games/store/Fable-II/C2WKJJ9F5936),
  accessed 2026-09-26. This identifies title, publisher and platform; its
  current distribution date is not evidence for the original retail date.
- **[P2]** [Original *Fable II* Xbox 360 instruction
  booklet](https://www.videogamemanual.com/xbox360/Fable%20II.pdf), pp. 2,
  4, 9 and 13, accessed 2026-09-26. The original Microsoft/Lionhead artifact
  is mirrored by a manual archive: it establishes control categories,
  morality and golden-trail/transaction concepts, not the exact five-errand
  sequence or an inspected executable.
- **[S1]** [GameSpot's post-release *Fable II*
  walkthrough](https://www.gamespot.com/articles/fable-2-walkthrough/1100-6201281/),
  childhood section, accessed 2026-09-26. A contemporary written route
  through the five jobs, warrants, box and subsequent chapter boundary.
- **[S2]** [Slasher424242's 2008 original Xbox 360 written
  guide](https://gamefaqs.gamespot.com/xbox360/927246-fable-ii/faqs/54637),
  childhood section, accessed 2026-09-26. Independently describes the five
  coin paths, Derek/Arfur alternatives, combat and box activation. This is a
  first-hand guide, not a captured save or source code.

## Mechanical decomposition

### Action Genes

- `ACT-008`: move through Old Town and into the alley/warehouse.
- `ACT-089`: pick up the five addressed warrants, bottle or task object.
- `ACT-091`: deliver the carried warrants, letter or bottle to an eligible
  recipient; delivery target is a consequential branch parameter.
- `ACT-130`: buy Murgo's offered music box after sufficient payment.
- `ACT-161`: strike Rex with the child's stick or shoot eligible beetles with
  the toy gun; adult weapon switching is not imported.
- `ACT-232`: commit an authored helpful/exploitative task response.
- `ACT-341`: activate the bought music box; purchase alone is not the exit.

### System Behaviour Genes

- `SYS-215`: Rex and the beetles respond during local direct combat.
- `SYS-379`: committed warrant response retains the Old Town branch flag
  that can alter the later world. This packet observes flag commitment, not
  the adult town itself.
- `SYS-477`: eligible good/evil acts change persistent moral standing; the
  exact magnitude and later appearance threshold are not fixed here.
- New `SYS-1084`: each of the five authored task slots grants its required
  coin after either accepted opposed resolution. Moral choice changes the
  retained state but does not force a different coin-funding route.

### Constraint Genes

- `CON-136`: the five-gold price is a persistent acquisition prerequisite
  for buying the box. The errands may be completed in different order;
  their individual branches are not prerequisites for each other.

### Information Genes

- `INF-117`: current gold and the box's five-gold offer are inspectable
  before buying; no future shop or adult economy is claimed.
- `INF-125`: the current golden trail/map prompt guides an available task.
  It does not reveal every later consequence before commitment.

### Objective Genes

- New `OBJ-238`: finish the bounded five-payment childhood goal by obtaining
  the fixed price from local errands, buying the named object and activating
  it. Reaching five gold alone or only buying the object is insufficient.

### Time Genes

- `TIM-003`: Rex/beetles respond in real time. There is no five-errand clock.

## Reproducible transitions

| Before | Action | Bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Five-gold offer visible, no task paid | Follow current trail to an errand | One authored local task becomes reachable | navigation, not mandatory order | `F2-002`, `F2-006` |
| Rex threatens the dog | Strike with the child's stick | The small live scuffle can clear; no adult combat loadout is assumed | local combat | `F2-005` |
| Five warrants collected | Hand them to Derek | Receive one coin, helpful alignment and retained lawful-town branch | helpful branch | `F2-003` |
| Same five warrants collected | Hand them to Arfur instead | Receive one coin, exploitative alignment and retained lawless-town branch | opposed branch, same funding | `F2-003` |
| Warehouse task active | Clear beetles without destroying stock, or accept Arfur's sabotage alternative | The accepted resolution pays one coin; moral consequence differs | alternate paid outcome | `F2-004`, `F2-005` |
| Fewer than five gold | Attempt box purchase | Price prerequisite not met; continue unfinished errands | economic gate | `F2-002` |
| Five gold available | Pay Murgo, then activate the box | Box plays/vanishes; packet ends before sleep | purchase is not activation | `F2-007` |

## Edge-case audit

- The five tasks are a finite childhood funding set. Choosing a negative
  solution does not require a sixth coin; it changes conduct and in the
  warrant case a later-world flag while preserving the payment.
- The guard and Arfur do not both receive the same warrant stack in one run.
  The illustration shows a choice before delivery, not simultaneous payment.
- The photograph and letter are not claimed to have the same later-world
  consequence as the warrants. Only their immediate payment/moral alternative
  is included.
- The music box must be used after purchase. Sleeping and the castle scene
  follow but are not required for this packet's terminal.
- The manual's adult health, spells, equipment and Purity/Corruption breadth
  cannot be read back into this child's short task packet.

## Strategic and experiential structure

- Local: decide whether to finish an errand helpfully or exploitatively while
  still obtaining the coin; handle the small fight without importing adult
  loadouts.
- Medium term: earn five separate payments before the box can be bought.
- Long term: the warrant choice marks a later town consequence, but the
  analysis does not model that later town as a completed objective.
- Player trust: the visible price and guiding trail explain what to do now;
  deferred consequences are not represented as fully disclosed in advance.

## Replay and variation

Errand order and moral recipients vary, while the fixed five-coin price and
box activation stay invariant. The exact combat timings and any incidental
randomness were not measured. A later adult-town comparison is a different
scoped module.

## Adjacent systems and history

- The first *Fable* (`GAME-0327`) also uses childhood good/evil choices and
  a fixed-gold gift purchase, but its reviewed packet continues through
  Guild training and graduation. This sequel packet tests paid opposed
  errands and a specifically retained town flag before the time jump.
- *Red Dead Redemption 2* uses the transferable conduct aggregate
  `SYS-477`, but its scoped honour band also changes disclosed prices and
  ambient responses in a different, adult-world loop. No such numeric
  response threshold is inferred here.
- *Cyberpunk 2077* supplies the general retained quest-flag boundary of
  `SYS-379`; the Old Town flag is a later-world branch, not a full ending.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-089`, `ACT-091`, `ACT-130`, `ACT-161`, `ACT-232`, `ACT-341` | warrants, letter, bottle, stick, toy gun, box |
| System Behaviour | `SYS-215`, `SYS-379`, `SYS-477`, `SYS-1084` | opposed payment, conduct, retained Old Town flag |
| Constraint | `CON-136` | five-gold price |
| Information | `INF-117`, `INF-125` | gold balance, offer, guiding trail |
| Objective | `OBJ-238` | bought-and-used box |
| Time | `TIM-003` | live small fights, no mission clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `404` (`GAME-0001`–`GAME-0404`).
- Exact genome matches: none.
- Tied near matches: `GAME-0327` — Fable (`10 / 27 = 0.370370`).
- Supported combination subsets: none.
- Scan date: 2026-09-26.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0327` — Fable | `ACT-008`, `ACT-130`, `ACT-161`, `ACT-232`, `SYS-215`, `SYS-477`, `CON-136`, `INF-117`, `INF-125`, `TIM-003` | Both childhood openings use movement, a moral response, live stick combat and an earned-gold purchase gate. The first Fable trace follows good deeds, proceeds through Guild training and graduates a retained hero; Fable II instead tests opposed one-coin errand outcomes, addressed-item delivery and a warrant flag, then stops at buying and activating the box before its adult world. Shared series vocabulary does not make these terminals or branch consequences identical. | Near, `10 / 27 = 0.370370` |

## Taxonomy impact

- Registry changes: `SYS-1084` and `OBJ-238` become Active under
  `TAXONOMY_CHANGE_143`.
- No earlier genome or verified combination changes.

## Negative results

- No adult combat, spell, property or later-world rendering enters this
  childhood box packet. Both warrant outcomes pay, so good alignment is not
  a prerequisite for the purchase. Exact later-town numeric effects and
  child death/reload behaviour remain unverified.

## Delta summary

## New facts

- [Observation | Corroborated | High] The five local one-coin errands can
  finance Murgo's box through helpful or exploitative resolutions; the
  warrant branch retains a distinct later-town consequence (`F2-002`–`F2-004`).

## New genes

- [Observation | Corroborated | High] `SYS-1084` separates equal mandatory
  payment from opposed retained outcomes; `OBJ-238` separates price assembly,
  purchase and activation from later story scenes.

## New combinations

- [Observation | Corroborated | High] None verified for this bounded packet.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_143` adds two Active
  genes without changing an earlier signature.

## New questions

- How exactly do the original 2008 disc's child scuffle damage and retry
  semantics work, and what quantitative adult Old Town change follows each
  warrant recipient?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0406` *DanceDanceRevolution*.
- Optimisation criterion: switch platform and decision loop to foot-panel
  timing after a dialogue-and-quest packet.
- Expected information gain: test rhythm input and judgement windows without
  conflating them with a moral quest branch.
- Backlog impact: no selected subject displaced.

## Why this game

- [Hypothesis | Limited | Medium] A short, reproducible childhood purchase
  tests whether equal-pay opposed errands and a deferred world flag survive
  a narrow scope without importing the famous adult open-world breadth.
