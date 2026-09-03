---
game_id: GAME-0213
slug: star-wars-jedi-fallen-order
game_title: "STAR WARS Jedi: Fallen Order"
analysis_status: reviewed
reviewed: 2026-09-01
combination_ids:
  - COMB-0211
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-190
    - ACT-191
    - ACT-200
    - ACT-223
    - ACT-224
    - ACT-341
    - ACT-383
  system:
    - SYS-215
    - SYS-251
    - SYS-364
    - SYS-398
    - SYS-409
    - SYS-610
    - SYS-707
  constraint:
    - CON-269
    - CON-270
    - CON-282
    - CON-286
    - CON-324
    - CON-349
    - CON-354
  information:
    - INF-119
    - INF-125
    - INF-272
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: STAR WARS Jedi: Fallen Order

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam Standard Edition,
  app `1172380`, public Build ID `10360016`, built 2023-01-19 and published
  2023-01-31, checked 2026-09-01; one fresh New Journey on Jedi Knight,
  keyboard and mouse, standard manual targeting and no enabled accessibility
  assists. The official storefront display title is `STAR WARS Jedi: Fallen
  Order™`; the canonical title omits the non-semantic trademark mark. The build
  is current despite later storefront-record edits.
- Primary decision loop: leave the Mantis on the first Bogano visit; traverse,
  jump, climb, balance, slide and swing; meet and repair BD-1; read the Holomap;
  fight local creatures by lightsaber attack, sustained block, timed parry,
  dodge and Force Slow; use finite Stims; meditate, rest and spend the taught
  skill point; relearn Wall Run; use that retained capability to reach the
  Ancient Vault; receive Eno Cordova's recording and settle the new Zeffo
  objective.
- Entry and exit: entry is first retained ordinary Cal Kestis control after
  the Mantis lands on Bogano and Cere sets `Reach the Vault`. Positive terminal
  is the saved post-recording state inside the Ancient Vault after Cordova's
  message has completed and the objective changes to searching Zeffo. Death
  and return to the last Meditation Circle fail only an attempt.
- Included: direct third-person traversal; jump, ledge, vine, slope and wall-
  run movement; lightsaber attacks; manual target choice; block stamina,
  sustained guard, parry and dodge; Force meter, Slow and attack-fed refill;
  health, two BD-1 Stims and healing; the first Meditation Circle, save, rest,
  resource refill and ordinary-enemy respawn; experience, the taught skill
  point and one legal first skill; BD-1 meeting/repair, Holomap and required
  route interactions; retained Wall Run acquisition; required Bogano creatures,
  authored traversal gates and the Ancient Vault recording terminal.
- Excluded: the Bracca prologue before the declared entry; return to the Mantis,
  planet selection and every Zeffo, Dathomir or later-planet state; optional
  Oggdo Bogdo, chests, secrets, Force Echo completion, Databank completion,
  cosmetics, lightsaber customisation and one-hundred-percent collection;
  later Force Push/Pull, Jedi Flip, Scomp Link, Overcharge, double-bladed
  lightsaber and later skill-tree branches; New Journey+, Meditation Training,
  Combat Challenges, Battle Grid, photo mode, achievements, mods, speedrun
  skips, other difficulties, assists, controllers and non-Windows platforms;
  Deluxe Crimson skins, digital art book and Director's Cut media.
- Reproducible parameterisation: choose Standard Edition, New Journey, Jedi
  Knight and keyboard/mouse; leave assists disabled. From first Bogano control,
  reach the initial Meditation Circle, meet BD-1, obtain the Holomap, perform
  one sustained block and one successful parry or dodge, spend Force Slow and
  restore Force through a successful hit, use a Stim after damage, rest once
  and observe ordinary-enemy return, spend the taught point, acquire Wall Run,
  cross one previously illegal wall-run edge and enter the Vault. Accept the
  recording-complete objective change as the only positive terminal.
- Potential scoped modules: Bracca; complete first Bogano visit through Mantis
  departure; one Zeffo tomb; one named boss packet; later ability-gated Bogano
  revisit; Journey+; Meditation Training; another fixed difficulty/platform.
- Direct-play status: not conducted. Official EA product, settings and PC text
  manual material plus two independent text walkthroughs establish the build,
  controls, route and terminal. The trace below is evidence-based rules
  reconstruction. No video or audio was opened, played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `JFO-001` | The current official product title is STAR WARS Jedi: Fallen Order and Windows Standard Edition is distinct from Deluxe extras | Confirmed | Direct | High | P1, P2 |
| `JFO-002` | Steam app `1172380` exposes the current public Windows Build `10360016` while Deluxe content remains separately packaged | Confirmed | Corroborated | High | P2, S1 |
| `JFO-003` | Jedi Knight is one of four difficulties and changes parry timing, incoming damage and enemy aggression | Confirmed | Direct | High | P3, P4 |
| `JFO-004` | Cal directly traverses and fights through attack, sustained block, timed parry, dodge, targeting and Slow | Confirmed | Direct | High | P5 |
| `JFO-005` | Blocking drains Block Stamina; empty Block Stamina exposes Cal, while Force abilities spend Force and attacks refill it | Confirmed | Direct | High | P5 |
| `JFO-006` | BD-1 Stims heal a finite number of times and rest restores Stims together with life and Force | Confirmed | Direct | High | P5 |
| `JFO-007` | Resting at a Meditation Circle saves, restores resources and respawns defeated ordinary enemies; earned skill points are spent there | Confirmed | Direct | High | P5 |
| `JFO-008` | BD-1's Holomap distinguishes unexplored orange, openable green and currently unavailable red route edges | Confirmed | Direct | High | P5 |
| `JFO-009` | The first Bogano route meets BD-1, teaches the Holomap and meditation, retains Wall Run and uses it to reach the Vault | Observation | Corroborated | High | S2, S3 |
| `JFO-010` | The completed Vault recording changes the retained objective toward Zeffo and supplies a bounded positive terminal | Observation | Corroborated | High | P1, S2, S3, V1 |
| `JFO-011` | Ordinary death returns Cal to the last Meditation Circle without creating a recoverable currency mark | Confirmed | Direct | High | P5 |
| `JFO-012` | The bounded loop couples combat recovery, checkpoint trade-offs and a newly retained traversal edge rather than merely presenting an action corridor | Observation | Corroborated | High | P5, S2, S3, V1 |

## Basic data

- Release / origin: developed by Respawn Entertainment and published by
  Electronic Arts; released 2019-11-15; current official title **STAR WARS
  Jedi: Fallen Order**.
- Platform or physical form: authored single-player third-person action-
  adventure; current Windows Steam Standard Edition only.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  spatial logic and topology; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official EA product page](https://www.ea.com/games/starwars/jedi-fallen-order),
    for current title, Standard/Deluxe boundary, single-player exploration,
    lightsaber, Force and story framing.
  - **[P2]** [official Steam product page](https://store.steampowered.com/app/1172380/STAR_WARS_Jedi_Fallen_Order/),
    for app identity, Windows, single-player and Standard-versus-Deluxe packages.
  - **[P3]** [official EA PC gameplay settings](https://www.ea.com/able/resources/star-wars-jedi-fallen-order/pc/gameplay-settings),
    for the four named difficulty choices and Jedi Knight boundary.
  - **[P4]** [official EA accessibility features](https://www.ea.com/ea-play/news/star-wars-jedi-fallen-order-accessibility-features),
    for difficulty effects and optional targeting, climbing and QTE assists.
  - **[P5]** [official EA PC text manual](https://www.ea.com/able/resources/star-wars-jedi-fallen-order/pc/text-manual),
    for keyboard/mouse controls, attack/block/parry/dodge, Block Stamina,
    Force expenditure and attack refill, Stims, death, Meditation Circles,
    rest/enemy reset, skills and Holomap colours.
- Secondary and reproducible sources:
  - **[S1]** [SteamDB depots](https://steamdb.info/app/1172380/depots/), observed
    2026-09-01, for public Build ID `10360016`, build/publish dates, Windows
    depot and separate Deluxe depot.
  - **[S2]** [Neoseeker Bogano — Visit the Vault text walkthrough](https://www.neoseeker.com/star-wars-jedi-fallen-order/walkthrough/Bogano_-_Visit_the_Vault),
    for first-visit Holomap, Wall Run and Vault-objective ordering; optional
    collectibles and later returns are excluded.
  - **[S3]** [GameFAQs Bogano first-visit text walkthrough](https://gamefaqs.gamespot.com/xboxone/240967-star-wars-jedi-fallen-order/faqs/78117/bogano-1st-visit),
    for the Meditation Point, first skill, BD-1 route and wall-run sequence.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P5` and `S1`–`S3` under the declared entry, Jedi Knight settings and
  terminal; rules reasoning, not a claimed playthrough.
- Claim IDs: `JFO-001`–`JFO-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly move, jump, climb, balance, slide, swing and
  wall-run Cal through Bogano; `ACT-161`: aim/lock and commit lightsaber
  attacks; `ACT-190`: activate Force Slow on a legal target; `ACT-191`: spend
  the taught skill point; `ACT-200`: commit an interruptible BD-1 Stim heal;
  `ACT-223`: time a dodge or parry; `ACT-224`: deliberately rest at Meditation;
  `ACT-341`: interact with BD-1 and required route objects.
- New `ACT-383`: hold or release ordinary undirected lightsaber guard while
  accepting Block Stamina and exposure consequences. It is neither Street
  Fighter's high/low guard nor Bannerlord's chosen directional block.
- Parameters: movement edge, target, strike, guard state, defensive timing,
  Force cost, Stim charge, Meditation Circle, skill point and interaction.
- Claim IDs: `JFO-004`–`JFO-012`.

### System Behaviour Genes

- Existing `SYS-215`: resolve real-time hostile combat; `SYS-251`: advance the
  authored opening objective; `SYS-364`: restore resources and respawn ordinary
  enemies on rest; `SYS-398`: retain Wall Run after the memory sequence;
  `SYS-409`: convert depleted guard stability into an exposed opening;
  `SYS-610`: return ordinary death to the latest Meditation Circle without a
  currency mark.
- New `SYS-707`: spend Force on Slow and refill the same meter through
  successful lightsaber attacks.
- Resolution order: route and visible state expose actions; traversal or combat
  input is accepted; target, stamina, Force, health and timing settle; BD-1
  heals if a Stim is legal; meditation applies save/rest/skill decisions;
  authored memory retains Wall Run; the compatible edge becomes usable; the
  Vault recording completes and writes the Zeffo objective.
- Claim IDs: `JFO-004`–`JFO-012`.

### Constraint Genes

- Existing `CON-269`: Slow requires sufficient Force, readiness and a legal
  target; `CON-270`: the first skill requires an available point and legal tree
  node; `CON-282`: Bogano story transitions follow authored gates; `CON-286`:
  Stim use needs a charge, missing life and an uninterrupted state; `CON-324`:
  parry/dodge success depends on the Jedi Knight timing window; `CON-349`:
  wall-run edges require the retained Wall Run capability; `CON-354`: attacks,
  dodge, sprint and guard depend on stamina and recovery state.
- Scarce strategic resources: life, Block Stamina, ordinary stamina, Force,
  two Stim charges, skill point, safe rest opportunity and route position.
- Claim IDs: `JFO-003`–`JFO-012`.

### Information Genes

- Existing `INF-119`: life, Force, Block Stamina, Stims, experience, skill and
  readiness are visible; `INF-125`: explored terrain, objective and authored
  gates are inspectable.
- New `INF-272`: the rotatable three-dimensional Holomap classifies known
  route edges as unexplored orange, openable green or currently unavailable
  red without revealing undiscovered content.
- Claim IDs: `JFO-005`–`JFO-012`.

### Objective Genes

- Existing `OBJ-026`: traverse one bounded authored route and settle the
  designated transition; here the transition is the completed Ancient Vault
  recording and retained change from `Reach the Vault` to the Zeffo search.
- Reaching BD-1, Wall Run or the Vault door is intermediate. Death and
  Meditation return are retries, not alternate positive terminals.
- Claim IDs: `JFO-009`, `JFO-010`, `JFO-012`.

### Time Genes

- Existing `TIM-003`: traversal, creatures, attacks, stamina, Force and route
  interactions advance continuously outside explicit map, skill and
  meditation menus or authored transitions.
- Claim IDs: `JFO-004`–`JFO-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Standard Edition, New Journey, Jedi Knight | Accept first Bogano control | `Reach the Vault` is active with no later-planet state admitted | bounded entry | `JFO-001`–`JFO-003`, `JFO-009` |
| Reachable creature attacks | Hold block, then release or time parry/dodge | Guard spends Block Stamina; valid timed defence avoids the matching strike; exhaustion exposes Cal | distinct defence choices | `JFO-004`, `JFO-005` |
| Force remains and a legal target is present | Activate Slow, then strike a hostile | Slow spends Force; a successful ordinary attack restores Force | attack-fed ability loop | `JFO-004`, `JFO-005` |
| Cal has missing life and one Stim | Request BD-1 heal | A Stim charge is consumed and life rises if the animation completes | finite companion heal | `JFO-006` |
| An activated Meditation Circle is reached | Rest and inspect Skills | Life, Force and Stims refill, ordinary enemies return and one legal point can be spent | checkpoint trade-off | `JFO-007` |
| BD-1 has joined and Holomap is available | Rotate/inspect mapped connections | Known edges are classified orange, green or red by present state | reachability information | `JFO-008` |
| The memory sequence completes | Attempt the taught wall-run edge | Wall Run persists and the compatible edge becomes traversable | retained capability gate | `JFO-009` |
| Cal reaches the Ancient Vault | Complete Cordova's recording | The Vault state settles and the saved objective redirects the campaign toward Zeffo | positive terminal | `JFO-010`, `JFO-012` |
| Life reaches zero before terminal | Accept return | Control resumes at the last Meditation Circle without a recoverable currency mark | retry boundary | `JFO-011` |

## Strategic and experiential structure

- Planning horizon: decide whether to detour, fight, conserve Stims/Force or
  rest before the next traversal gate; use Holomap reachability rather than
  treating every visible edge as currently legal.
- Local tactics: block readable pressure, parry a learned strike, dodge a less
  certain one, attack to refill Force, Slow to make an opening and heal only
  when BD-1 can finish the Stim animation.
- Long-term progression: one skill point and the retained Wall Run capability
  survive Meditation and death; optional later powers are outside this unit.
- Reversible versus irreversible: combat position, spent resources and rest
  reset are locally reversible; acquired Wall Run and the Vault objective
  transition persist in the save.
- Failure attribution: empty guard/Force/Stims, mistimed defence, interrupted
  heal, illegal red route edge or missed authored traversal can be separated
  from hidden randomness.
- Player trust: gauges, animations, Holomap colours, meditation consequences
  and explicit objective update disclose the relevant state without choosing
  the route or defensive timing for the player.

## Replay and variation

- What changes: optional Bogano detours, creature engagements, skill timing,
  resource use, rest frequency, deaths and exact wall-run approach.
- Randomness or procedural generation: the admitted planet geometry, teaching
  chain and terminal are authored; incidental combat variance does not alter
  the required objective relation.
- Multiple viable strategies: conservative block, tighter parry, dodge-heavy
  play and different Force/Stim timing can reach the same Vault terminal.
- Typical replay motive: cleaner combat/traversal execution or exploration of
  excluded secrets; Journey+ and later-ability revisits are separate modules.

## Adjacent systems and history

- Direct successors or variants: Jedi: Survivor, console ports, Deluxe and New
  Journey+ are distinct rulesets, not merged into this Standard PC packet.
- Similar games: Black Myth: Wukong, Elden Ring, Hollow Knight: Silksong and
  Tomb Raider share selected combat, checkpoint, traversal or route gates.
- Important differences: Wukong turns perfect defence and attacks into Focus,
  permits a temporary body and freely reclaims Sparks; Fallen Order instead
  restores Force through hits, sustains a breakable guard and uses BD-1's
  coloured 3D route map. Elden Ring adds rune death marks, equipment load,
  open-field preparation and a boss gate. Silksong uses Silk, Crests, Tools and
  a Cocoon rather than Force, Stims and a companion Holomap.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-191`, `ACT-200`, `ACT-223`, `ACT-224`, `ACT-341`, `ACT-383` | movement, lightsaber, Slow, skill, Stim, timed defence, rest, interaction and sustained guard |
| System Behaviour | `SYS-215`, `SYS-251`, `SYS-364`, `SYS-398`, `SYS-409`, `SYS-610`, `SYS-707` | live combat, authored opening, meditation reset, retained Wall Run, guard break, death return and Force refill |
| Constraint | `CON-269`, `CON-270`, `CON-282`, `CON-286`, `CON-324`, `CON-349`, `CON-354` | Force, skill, story, Stim, timing, traversal and stamina legality |
| Information | `INF-119`, `INF-125`, `INF-272` | personal state, objective/map and coloured route reachability |
| Objective | `OBJ-026` | complete the Vault recording and retain the Zeffo objective |
| Time | `TIM-003` | continuous traversal and combat |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `212` (`GAME-0001`–`GAME-0212`).
- Exact genome matches: none.
- Tied near matches: `GAME-0189` — Black Myth: Wukong (`20 / 37 = 0.540541`).
- Supported combination subsets: `COMB-0211`.
- Scan date: 2026-09-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0189` — Black Myth: Wukong | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-191`, `ACT-200`, `ACT-223`, `ACT-224`, `SYS-215`, `SYS-251`, `SYS-364`, `SYS-610`, `CON-269`, `CON-270`, `CON-282`, `CON-286`, `CON-324`, `CON-354`, `INF-119`, `INF-125`, `TIM-003` | Both are real-time authored action routes with ability resource, finite heal, timed defence, skill allocation, recovery checkpoint and lossless return. Wukong turns attack/Perfect Dodge into discrete Focus, can replace the body with Red Tides, freely reallocates Sparks and settles a boss chapter. Fallen Order adds sustained breakable guard, hit-refilled Force, BD-1 Stims, coloured Holomap reachability and a retained Wall Run gate before a non-boss Vault objective. | Near, `0.540541` |

### Preserved research notes

- New genes: `ACT-383`, `SYS-707`, `INF-272`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: existing movement, attack, ability, point, heal,
  defence, rest, interaction, combat, opening, reset, capability, guard-break,
  death-return, legality, map, objective and time boundaries safely absorb the
  generic layer. No lower-ID record represents undirected sustained guard,
  attack-restored Force and colour-coded route-edge reachability as these
  distinct causal boundaries.

## Combination status

- `COMB-0211` is a strict twenty-two-gene subset of the twenty-eight-gene
  genome, coupling lightsaber defence, attack-fed Force, meditation trade-off,
  retained Wall Run and Holomap-guided Vault access.
- Every earlier verified combination is tested deterministically after
  registration; none is a proper subset of this genome.

## Taxonomy impact

- Registry changes: three new Active genes, evidence links on reused genes,
  `COMB-0211` and four existing family memberships.
- Taxonomy-change record: none; no earlier reviewed signature, lifecycle or
  stable definition changes.
- Candidate terms affected: sustained melee guard, attack-restored Force and
  reachability-coloured holographic route map.

## Negative results

- `ACT-296` and `ACT-349` are not reused: Cal's ordinary block is neither
  opponent-relative high/low guard nor an aimed directional weapon block.
- `SYS-399` is not reused: death creates no recoverable currency mark.
- `SYS-609` is not reused: this packet does not establish free skill-point
  reclamation; the taught point is an ordinary persistent allocation.
- `SYS-397` is not reused: Force is spent on Slow and refilled by attacks, not
  converted into full-spool healing or Silk skills.
- Optional scans, chests, echoes and collectibles do not enter the signature
  merely because BD-1 and the Holomap exist.
