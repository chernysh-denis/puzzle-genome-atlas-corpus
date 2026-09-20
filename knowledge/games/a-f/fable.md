---
game_id: GAME-0327
slug: fable
game_title: Fable
analysis_status: reviewed
reviewed: 2026-09-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-130
    - ACT-161
    - ACT-232
    - ACT-437
    - ACT-438
  system:
    - SYS-215
    - SYS-477
    - SYS-578
    - SYS-736
    - SYS-937
  constraint:
    - CON-136
    - CON-269
    - CON-282
  information:
    - INF-115
    - INF-117
    - INF-119
    - INF-125
    - INF-268
  objective:
    - OBJ-193
  time:
    - TIM-003
---

# Game: Fable

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Oakvale, Theresa,
Maze, Whisper, the Guildmaster, the Guild Seal and the three Hero disciplines
are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: original North American English Xbox retail *Fable*,
  product `V07-00032`, original-Xbox title ID `4D53000D` / catalogue family
  `MS-013`, fresh game from Oakvale childhood through graduation from the
  Heroes' Guild. This is the 2004 base game, not *Fable: The Lost Chapters*,
  *Fable Anniversary* or the later series and reboot.
- Structured analysis target: licensed North American original-Xbox base-game
  disc; see `GAME-0327` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: follow the current authored instruction and minimap
  marker; navigate Oakvale or the Guild; converse, choose a deed response,
  interact or purchase; during training lock to a target, strike, block, shoot
  or cast Lightning; satisfy the current lesson before explicitly advancing
  the hero into the next retained life stage.
- Entry: first ordinary control of the child hero in Oakvale after the father
  requests good deeds for the sister's birthday present.
- Positive terminal: the adult final test has accepted sword, bow and Lightning
  contact against Maze; the Chamber of Fate ceremony has awarded graduation;
  ordinary control returns to the same persistent Hero with the Guild quest map
  available. The first Wasp Menace quest is not accepted.
- Negative state: an unfinished deed or training predicate leaves the current
  instruction active. A poor timed score can be retried but is not terminal.
  Death, save restoration and campaign failure are not evidenced in this
  source-bounded tutorial packet.
- Included: three gold earned through the reproducible good-deed route; the
  teddy-bear dispute, reporting the unfaithful husband and guarding the barrels;
  buying and delivering chocolates; the scripted Oakvale raid and relocation;
  unarmed and stick dummy work; beetle clearance; explicit childhood-to-teen
  confirmation; sword attack, lock-on, held block and sparring; bow aiming,
  held-shot strength and timed target values; learned Lightning, regenerating
  Mana and its timed target lesson; explicit teen-to-adult confirmation; the
  three-part final test; graduation and retained Hero/quest access.
- Excluded: choosing the evil deed alternatives in the reproducible trace,
  attacking villagers, optional Guild exploration, the optional Whisper woods
  exercise, bonus training grades and reward weapons, accepting or completing
  Wasp Menace, Experience spending, later alignment appearance thresholds,
  Renown, boasting, property, marriage, trade beyond the chocolates, equipment
  builds, free-world travel, later quests, endings, save/load behaviour,
  Xbox Originals wrapper differences, *The Lost Chapters*, *Anniversary*,
  sequels, the later reboot, ports, emulation, cheats, glitches and mods.
- Reproducible parameterisation: start a fresh North American base-game file;
  resolve the teddy bear by confronting the bully, report the husband, guard
  the barrels until their owner returns, collect all three father payments,
  buy the three-gold chocolates and deliver them to Theresa. After the raid,
  complete the prescribed dummy and beetle lessons, confirm both life-stage
  transitions, complete the ordinary melee, ranged and Will lessons, contact
  Maze once with each discipline and accept graduation. Timed training scores,
  incidental items and dialogue timing are parameters.
- Potential scoped modules: one evil childhood route, optional training grades,
  the first accepted Quest Card, Experience spending, alignment presentation,
  Renown, free exploration and every later quest need independent terminals and
  evidence.
- Direct-play status: not conducted. No original disc, console, controller
  trace, save, screenshot, video or audio was used. Microsoft's preserved
  manual establishes controls, Guild facilities, resources, graduation and
  morality systems; two written original-Xbox routes establish the exact
  Oakvale and training sequence. This is a source-bounded reconstruction, not
  a claimed playthrough or reload test.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FAB-001` | The packet is the 2004 original Xbox base game, distinct from *The Lost Chapters* and *Anniversary* | Confirmed | Corroborated | High | P1, S1 |
| `FAB-002` | The North American retail identity uses product `V07-00032`; original title data identifies `4D53000D` / `MS-013` | Observation | Corroborated | High | S1, S2 |
| `FAB-003` | Three completed good deeds produce the three gold needed to buy and deliver the birthday chocolates | Observation | Corroborated | High | S3, S4 |
| `FAB-004` | The scoped Oakvale decisions admit helpful and exploitative alternatives whose deed valence persists in alignment state | Observation | Corroborated | High | P2, S3, S4 |
| `FAB-005` | The raid and Maze relocation are authored transitions from Oakvale to the Heroes' Guild rather than player-selected travel | Observation | Corroborated | High | S3, S4 |
| `FAB-006` | Childhood training requires dummy contact and beetle clearance before an explicit transition into adolescence | Observation | Corroborated | High | S3, S4 |
| `FAB-007` | Adolescent Guild training separately teaches sword attack/block, bow aim/charge and Lightning under staged predicates | Confirmed | Corroborated | High | P2, S3, S4 |
| `FAB-008` | Health, Mana, target lock, interaction prompts, minimap and contextual instructions expose the current actionable state | Confirmed | Direct | High | P2 |
| `FAB-009` | The player explicitly confirms leaving each earlier life stage; training state and learned combat repertoire continue into the successor body | Observation | Corroborated | High | S3, S4 |
| `FAB-010` | Sword, bow and Lightning contact against Maze precede the Chamber of Fate graduation and ordinary Quest Card access | Observation | Corroborated | High | P2, S3, S4 |

## Basic data

- Release / origin: Lionhead Studios / Big Blue Box and Microsoft Game Studios,
  original Xbox, North American retail release 2004-09-14.
- Platform or physical form: licensed North American original-Xbox retail disc,
  product `V07-00032`, title ID `4D53000D`, one-player tutorial packet.
- Puzzle family: ordered dependency sequencing inside an embodied action-RPG
  tutorial.
- Primary sources:
  - **[P1]** [Xbox Wire preservation notice linking the original Fable manual](https://news.xbox.com/en-us/2007/12/04/xbox-originals-manuals-and-controller-layouts-and-free-themes-and-picture-packs/),
    published 2007-12-04.
  - **[P2]** [preserved North American original-Xbox manual](https://nuangel.net/pcdownloads/xboxmanuals/Fable_MNL_EN-US.pdf),
    the PDF linked by Microsoft's Xbox Originals record; controls, HUD, Guild,
    training, resources, graduation, quests, alignment and Renown.
- Secondary sources:
  - **[S1]** [GameFAQs original-Xbox release data](https://gamefaqs.gamespot.com/xbox/516688-fable/data),
    product, publisher, date and one-player identity.
  - **[S2]** [Original Xbox Title ID catalogue](https://www.mobcat.zip/XboxIDs/),
    `4D53000D`, `MS-013` and base-game media-family contrast with Lost Chapters.
  - **[S3]** [Jiyu_Aifu original-Xbox walkthrough](https://gamefaqs.gamespot.com/xbox/516688-fable/faqs/32419),
    Oakvale deeds and complete Guild training order.
  - **[S4]** [Andrew Testa original-Xbox walkthrough](https://gamefaqs.gamespot.com/xbox/516688-fable/faqs/32700),
    independent route and training corroboration.
- Claim IDs: `FAB-001`–`FAB-010`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly navigate the child, apprentice and adult Hero
  through Oakvale and Guild spaces.
- Existing `ACT-130`: spend the three visible gold on the offered chocolates.
- Existing `ACT-161`: directly commit unarmed, stick, sword, bow and Lightning
  attacks against the current eligible training target.
- Existing `ACT-232`: commit an authored deed response such as reporting the
  husband or rejecting the child's request to damage the guarded barrels.
- Existing `ACT-437`: hold and release the facing-relative sword block during
  Whisper's melee lesson.
- Existing `ACT-438`: bind view and attack facing to Whisper, a dummy, beetle
  or Maze until the target becomes ineligible or lock is released.
- Bow draw duration, target value, Lightning sustain and training actor are
  parameters. Claims: `FAB-003`, `FAB-004`, `FAB-006`–`FAB-010`.

### System Behaviour Genes

- Existing `SYS-215`: resolve directly commanded real-time hits, defence,
  health change and target defeat during beetle and sparring exercises.
- Existing `SYS-477`: aggregate contextual helpful or exploitative deeds into
  the persistent good/evil alignment consequences described by the manual.
- Existing `SYS-578`: apply damage and compatible healing to one continuous
  Hero health pool; exact failure handling is excluded from this packet.
- Existing `SYS-736`: keep each tutorial instruction active until its taught
  predicate is satisfied, then reveal the next lesson or destination.
- New `SYS-937`: after the current training gate and explicit confirmation,
  replace the presented childhood or adolescent body with the next authored
  life stage while retaining the same Hero identity, admitted deed history and
  learned repertoire.
- Resolution order: current instruction and target are exposed; the player
  navigates, responds or attacks; contact/resource/deed state resolves; the
  current predicate settles; only then can confirmation trigger the next life
  stage or graduation. Claims: `FAB-003`–`FAB-010`.

### Constraint Genes

- Existing `CON-136`: later tutorial interactions require retained earlier
  deed, payment, item or training state.
- Existing `CON-269`: Lightning requires the learned spell, legal target,
  sufficient Mana and an actionable combat state.
- Existing `CON-282`: authored Oakvale, childhood, adolescent, adult and
  graduation gates occur only after their ordered prerequisites.
- Three gold, lesson counts, timed target duration and test order are
  parameters. Claims: `FAB-003`, `FAB-006`–`FAB-010`.

### Information Genes

- Existing `INF-115`: local third-person sight, sound and target response expose
  nearby people, beetles, training dummies, attacks and contact.
- Existing `INF-117`: current gold and the trader's chocolate price are visible
  before purchase.
- Existing `INF-119`: health, Mana, alignment, equipment and learned combat
  state are available through the HUD and character interfaces.
- Existing `INF-125`: the minimap and current markers expose the present
  destination or lesson, not the full future chain.
- Existing `INF-268`: Guildmaster prompts explain the current action and report
  its completion before advancing.
- Claims: `FAB-003`–`FAB-010`.

### Objective Genes

- New `OBJ-193`: complete the Oakvale deed-and-gift prologue, satisfy all
  mandatory Guild training stages, pass the adult three-discipline test and
  retain ordinary control as a graduated Hero with Quest Cards available.
- Graduation, not merely reaching adulthood or hitting Maze once, is the
  terminal. Claims: `FAB-003`, `FAB-005`–`FAB-010`.

### Time Genes

- Existing `TIM-003`: local movement, beetles, sparring attacks, block state,
  target motion, Mana regeneration and timed lessons advance continuously while
  inputs remain available; menus and authored transitions interrupt that live
  cadence.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| The child has no gold and the teddy-bear dispute is active | Confront the bully, return the bear and report to the father | the deed settles as helpful and the father grants one gold | physical quest conduct can carry moral and economic results | `FAB-003`, `FAB-004` |
| The unfaithful husband offers silence | Refuse concealment, report him to his wife and return to the father | the helpful branch settles and one father payment is added | authored response changes persistent deed state | `FAB-003`, `FAB-004` |
| The barrel owner has delegated temporary guard | Stay near the barrels and refuse to break them until he returns | the timed temptation closes as protected and the third father payment becomes claimable | abstention can satisfy a live authored predicate | `FAB-003`, `FAB-004` |
| Three gold are held and the trader offers chocolates | Purchase the chocolates and give them to Theresa | gold falls to zero, the carried gift resolves and the raid sequence begins | finite deed rewards gate the prologue transition | `FAB-003`, `FAB-005` |
| The Guildmaster presents the childhood dummy | Strike as instructed, accept the stick and repeat | the current contact counts settle and the beetle test becomes current | staged instruction governs permitted progression | `FAB-006` |
| Guild Woods beetles remain | Lock, approach and strike until the finite group is cleared | beetles lose health and are defeated; the leave-childhood choice becomes available | real-time combat clears an authored training gate | `FAB-006`, `FAB-008` |
| Childhood training is complete | Confirm leaving childhood | the presented body advances to adolescence while the same Hero and admitted history continue | explicit life-stage transition retains identity | `FAB-009` |
| Whisper is the melee lesson target | Lock on, land required sword hits, hold block through attacks and win the spar | each required predicate settles before the next one is exposed | attack and sustained guard are distinct taught actions | `FAB-007`, `FAB-008` |
| Bow training is current | Aim, hold and release arrows into the authored targets during the timed phase | shot strength and target value produce a bounded score; ordinary completion admits the next lesson | charge duration is a parameter inside direct attack | `FAB-007` |
| Lightning has been learned and Mana remains | Lock a legal dummy and sustain Lightning during the timed phase | Mana drains and later regenerates while valid contact advances the lesson | learned magic is resource- and target-gated | `FAB-007`, `FAB-008` |
| Adolescent mandatory training is complete | Confirm leaving adolescence | the Hero advances to the adult body and the final test becomes current | a second explicit retained time jump gates graduation | `FAB-009` |
| Maze's adult final test is active | Contact Maze once with sword, bow and Lightning in the requested order | each discipline is accepted, after which the Chamber of Fate ceremony awards graduation | the terminal requires the complete three-part test | `FAB-010` |

## Edge-case audit

- The three-gold route uses helpful outcomes only. Evil alternatives prove the
  choice and alignment boundary but are not silently combined into this trace.
- The raid is an authored relocation after the gift; it is not a controllable
  combat encounter or world-travel action inside this packet.
- A timed bow or Will score can improve optional rewards, but ordinary
  completion is enough to progress. Bonus grading and reward equipment are
  excluded, so they add no score/loot gene here.
- Childhood and adolescence do not pass merely because real time elapses. The
  current mandatory training predicates and an explicit player confirmation
  are both required.
- Graduation exposes the wider Quest Card system, but the terminal occurs
  before accepting Wasp Menace; quest selection, boasting and Renown therefore
  remain outside the genome.

## Strategic and experiential structure

- Local decision: follow the marker, choose one offered deed response, preserve
  the guarded barrels, buy the required gift, then position, lock, strike,
  block, aim or cast against the current lesson target.
- Medium-term planning: route three helpful deeds into exactly three gold,
  preserve the intended moral trace, and complete each discipline before
  advancing the irreversible life-stage confirmation.
- Long-term structure: convert a child with recorded deed history into the same
  graduated adult Hero whose learned sword, bow and Will repertoire is ready
  for the open campaign.
- Common heuristics: finish nearby deeds before returning to the father; do not
  spend the three gold elsewhere; follow the green marker; hold block through
  the complete requested attack count; favour farther bow targets only when
  pursuing an excluded bonus score.
- Failure attribution: missing payment, wrong response, broken barrel guard,
  unfinished dummy count, living beetle, failed block count, missed target or
  incomplete final discipline remains distinguishable through the current
  prompt and world state.
- Player trust: equivalent inputs at equivalent tutorial state must award the
  same deed value, payment, training completion and retained life-stage result;
  optional score must not block ordinary graduation.

## Replay and variation

- Oakvale and Guild geometry, lesson order and graduation are authored; no
  procedural level generation is claimed.
- The player may choose good or evil deed outcomes, vary route order and repeat
  optional training scores, but the reproducible path fixes the helpful trace
  and ordinary completion.
- The main replay motive inside this packet is comparing deed/alignment routes
  or optional training performance, not random world generation.
- Claims: `FAB-003`–`FAB-010`.

## Adjacent systems and history

- Direct predecessor: none inside the series; this is the original 2004 base
  release.
- Variants: *The Lost Chapters* extends the product; *Anniversary* remakes and
  includes that extended content. Neither is evidence for this packet.
- Similar games: Skyrim and Fallout 4 also turn a staged embodied prologue into
  retained wider-world control; Red Dead Redemption 2 aggregates conduct into
  a persistent social axis.
- Important differences: this packet makes two explicit age-stage commitments
  during training and uses a short deed economy to precede the combat tutorial;
  it ends at professional graduation rather than an escape from captivity.
- Claim IDs: `FAB-001`, `FAB-004`, `FAB-009`, `FAB-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-130`, `ACT-161`, `ACT-232`, `ACT-437`, `ACT-438` | deed branch, chocolate price, bow charge and discipline order |
| System Behaviour | `SYS-215`, `SYS-477`, `SYS-578`, `SYS-736`, `SYS-937` | deed values, training counts and retained life-stage body |
| Constraint | `CON-136`, `CON-269`, `CON-282` | three gold, learned Lightning, Mana and ordered gates |
| Information | `INF-115`, `INF-117`, `INF-119`, `INF-125`, `INF-268` | HUD layout, marker, lesson copy and hidden future chain |
| Objective | `OBJ-193` | graduation and Quest Card availability |
| Time | `TIM-003` | target motion, timers, regeneration and authored transitions |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `326` (`GAME-0001`–`GAME-0326`).
- Exact genome matches: none.
- Tied near matches: `GAME-0224` — Once Human (`9 / 26 = 0.346154`).
- Supported combination subsets: none.
- Scan date: 2026-09-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0224` — Once Human | `ACT-008`, `ACT-161`, `SYS-215`, `CON-282`, `INF-115`, `INF-119`, `INF-125`, `INF-268`, `TIM-003` | Both use direct movement and attack inside a live, locally perceived, marker-led tutorial whose current instruction and personal state stay visible until ordered gates settle. Once Human admits a fresh account to one current ruleset and rewards tutorial closure; Fable instead couples deed-funded choices to persistent alignment, purchase, held block and target lock, then requires two confirmed age transitions and a three-discipline graduation. | Near, `9 / 26 = 0.346154` |

### Preserved research notes

- New genes: `SYS-937`, `OBJ-193`.
- Classification result: `New combination of known genes` plus two bounded new
  genes.
- Evidence and reasoning: existing traversal, purchase, response, combat,
  alignment, tutorial and information genes fit without carrier-specific
  duplication. Neither existing authored progression nor ageing genes covers a
  player-confirmed childhood/adolescence body transition that retains the same
  campaign identity and learned repertoire, and no objective ends at complete
  Guild graduation into open Quest Card access.

## Taxonomy impact

- Registry changes: add `SYS-937` and `OBJ-193`.
- Taxonomy-change record: `none`; no existing boundary or lifecycle changes.
- Candidate terms affected: life-stage transition and Guild graduation are
  promoted from game-scoped candidates to bounded active genes.

## Negative results

- No standalone negative-result record. The evil childhood branches, optional
  score rewards, Wasp Menace and wider campaign were tested against the scope
  and excluded rather than rejected as mechanics of the full product.

## Delta summary

## New facts

- [Confirmed | Corroborated | High] Original Xbox *Fable* stages deed-funded
  childhood, three-discipline Guild training and graduation before ordinary
  Quest Card play (`FAB-003`–`FAB-010`).

## New genes

- [Observation | Corroborated | High] `SYS-937` retains one Hero identity and
  learned state across explicit tutorial-gated life-stage transitions.
- [Observation | Corroborated | High] `OBJ-193` completes the staged childhood
  and Guild curriculum into retained graduated-Hero control.

## New combinations

- [Observation | Corroborated | High] No new verified combination record; the
  complete signature has no existing verified combination as a proper subset.

## Taxonomy changes

- [Observation | Direct | High] No taxonomy changes.

## New questions

- Does a local save/reload immediately after graduation preserve every scoped
  deed, learned discipline, inventory and life-stage field identically on the
  original North American disc?
- Which exact optional training-score bands award the bonus sword, bow and
  Will items in the original base game rather than later editions?

## Next recommended game

- [Hypothesis | Limited | High] `GAME-0328` *Warcraft III: Reign of Chaos*,
  original English Windows base campaign opening.
- Optimisation criterion: test hero-led real-time unit orders and authored
  campaign gates after a single-character morality/training packet.
- Expected information gain: command selection, formation/pathing, fog, hero
  progression and mission settlement without importing *Reforged* balance.
- Backlog impact: advances the fixed 333-game audience-recognition horizon.

## Why this game

- [Hypothesis | Limited | High] Its unit-group command loop should produce
  substantial genome distance from Fable while reusing enough authored-gate and
  tutorial vocabulary to test current boundaries.

## Completion checklist

- [x] exact base-game product boundary, entry and terminal declared
- [x] evidence ledger separates direct manual claims from reconstructed route
- [x] complete admitted loop decomposed across six canonical gene types
- [x] reproducible transitions and edge cases recorded
- [x] lower-ID comparison and combination scan regenerated
- [x] reviewed Ukrainian, presentation, artwork and browser surfaces complete
- [x] full repository and static-first gates complete
