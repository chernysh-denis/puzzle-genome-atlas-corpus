---
game_id: GAME-0664
slug: dicey-dungeons
game_title: "Dicey Dungeons"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-126
    - ACT-881
    - ACT-882
  system:
    - SYS-004
    - SYS-299
    - SYS-362
    - SYS-1907
    - SYS-1908
    - SYS-1909
    - SYS-1910
    - SYS-1911
  constraint:
    - CON-878
    - CON-879
  information:
    - INF-002
    - INF-612
  objective:
    - OBJ-029
  time:
    - TIM-047
---

# Game: Dicey Dungeons

Comparison uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Equipment names, die faces, counts and the threshold in this encounter
are parameters of the recorded rules.

## Analysis scope

- Version / ruleset: the full English commercial Android release for
  Google Play, first published 7 July 2022, package
  `com.terrycavanaghgames.diceydungeons`. Use the base game's first
  Warrior episode, The Warrior's Welcome, and a normal Marshmallow
  encounter on Floor 2 after the first-run tutorial. No exact APK,
  build number, device or random seed was verified.
- Structured analysis target: PLAT-ANDROID in
  `knowledge/platforms/games.json`. The public discovery link leads to
  the licensed Android package.
- Entry: after the first-run tutorial, enter the normal Floor 2
  Marshmallow fight with the level-two Warrior, three dice and
  Sword, Battle Axe, Bump and Matchstick equipped. The earlier
  fights and chests account for the carried state, and the enemy
  and floor layout are specific to the recorded route.
- Primary decision loop: read the rolled dice and equipped sockets.
  Allocate a compatible die or transform it for a later move in
  the same turn. Spend each die through the selected card, judge
  when to yield the turn, absorb the enemy's independent dice use
  and respond to any marked dice. Finish the opponent while alive
  and take the level reward triggered by the settled experience.
- Exit: the last Sword hit settles the fight with one coin and two
  experience. The Warrior reaches level three and takes Spiked Shield
  from the offered pair. Floor 2 movement resumes and the Equipment
  view opens with the shield in the backpack and the old four items
  still equipped. Stop at that actionable loadout state.
- Included: die supply and socket use, eligibility, per-card uses,
  Bump, Combat Roll, Burn and Freeze, separate player and hostile
  turns, victory, experience threshold and the resulting gear choice.
- Excluded: the tutorial battles as analysed encounters, use of Fury
  (available but not activated in the trace), the later shield swap,
  other opponents, floor-generation internals, stores, upgrades, later
  episodes, parallel rules, DLC, mods, prerelease versions and other
  ports. The published odds of the rolls and loss persistence were
  not tested.
- Potential scoped modules: a floor with an apple and a shop purchase,
  a Space Marine countdown fight, selection and use of a Fury action,
  or the same opponent under a named alternate episode.

## Direct-play status

No personal Android play, installed build, touch telemetry or device
check. The publisher's Android release listing and trailer verify the
commercial target and show the same ordinary enemy's two cards on a
different player's turn. A launch-period English mobile walkthrough
shows the entire Warrior encounter and labels the App Store in its
description. Its operating system is not independently verified,
so its exact rolls and result are mobile reference observations rather
than an authenticated Android run. A separate post-release mobile
record and the community-maintained official wiki corroborate bounded
rules. Static frames were inspected in the background without sound.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DD-001 | The full Android package shipped on 7 July 2022 beside the separate Reunion rules. The base Warrior episode has a normal Floor 2 encounter with Marshmallow. | Observation | Corroborated | High | P1 and P2 release material, P3 0:02–0:03, S1 and S2, W1 7:36–7:51. |
| DD-002 | Dragging a free die into a legal socket resolves that card; an invalid value does not satisfy its predicate. Sword takes any standard face for that much damage, Battle Axe takes at most four for twice that face and Matchstick takes an even face to mark a rival die. | Observation | Corroborated | High | S3 card rules, W1 7:51–8:07, W2 2:16–2:27 and 7:01–7:10. |
| DD-003 | Bump returns a die one higher in the observed in-range cases. Combat Roll replaces one selected die with a new face and shows a separate three-use allowance per turn. The different transformations can make the result compatible with another card in the current turn. | Observation | Corroborated | High | S1 and S3, W1 8:00–8:10 and 8:29–8:38. The documented Bump-at-six exception is not used in this fight. |
| DD-004 | Sword, Battle Axe and Bump are spent for the rest of their turn, whereas Matchstick remains reusable as long as another even die is available. End Turn passes control; the rival reveals its own dice, resolves distinct equipment and the next player turn renews the dice and ordinary card uses. | Observation | Corroborated | High | S1–S4, W1 7:51–8:27, W2 2:30–2:50 and 7:01–7:22. |
| DD-005 | The normal Marshmallow has 28 health and two dice. Its odd Snowball deals face-valued damage and freezes one next-turn die to one. Its even Fireball deals face-valued damage and burns one next-turn die. Extinguishing a marked die spends two of its owner's health before that die can be allocated. | Observation | Corroborated | High | P3 0:02–0:03, S2 and S4, W1 8:12–8:36. |
| DD-006 | The recorded opening pool is six, three and five. Sword six and Bump three to Battle Axe four leave the rival at 14. Rerolling five to six lets Matchstick burn the rival's next die. The rival pays two health to clear the burn and uses its six and five, leaving the Warrior at 13. | Observation | Direct | High | W1 7:49–8:26, exact visible instance values. |
| DD-007 | On turn two an axe four removes eight from the rival's remaining 12. Paying two health clears the Warrior's burn. Bump turns a three into four for the finishing Sword. The successful outcome credits one coin and two experience before further action. | Observation | Direct | High | W1 8:26–8:44. |
| DD-008 | The experience crosses the level-three threshold. Spiked Shield and Boomerang are offered, and taking the shield returns to Floor 2 at 32/32 health. Opening Equipment shows the shield in the backpack and the four original items still equipped. | Observation | Corroborated | High | S1 level table, W1 8:42–9:03. W2 7:25–7:37 corroborates the same offer structure after a different normal encounter. |

## Basic data

- Release / origin: the original game is from Terry Cavanagh,
  Marlowe Dobbe and Chipzel. The official launch material dates
  the full commercial Android version to July 2022.
- Puzzle families: FAM-004 (matching and combination) for matching
  a face to a numeric socket, and FAM-017 (ordered dependency
  sequencing) for transforming a die before spending its replacement.
- P1: [Google Play package](https://play.google.com/store/apps/details?id=com.terrycavanaghgames.diceydungeons).
  Identifies the authorised Android package and the mobile game.
- P2: [developer mobile announcement](https://distractionware.com/blog/2022/06/coming-soon-dicey-dungeons-reunion/)
  and [launch-day release post](https://terrycavanagh.itch.io/dicey-dungeons/devlog).
  Date the release and distinguish the base game from Reunion.
- P3: [Terry Cavanagh's Android release trailer](https://www.youtube.com/watch?v=Ij0y4oX4m5Q).
  At 0:02–0:03 a different character faces the 28-health
  Marshmallow and sees Snowball and Fireball. The edited footage
  also shows the Warrior's sockets and a different victory award.
- S1: [community-maintained official episode entry](https://wiki.diceydungeons.com/doku.php?id=episodes:warrior1).
  Describes the first Warrior episode, Combat Roll allowance, the
  level-three reward pair and ordinary encounter candidates.
- S2: [normal Marshmallow entry](https://wiki.diceydungeons.com/doku.php?id=enemies:marshmallow).
  Distinguishes normal, Super and Reunion enemy forms.
- S3: community equipment references for [Sword](https://wiki.diceydungeons.com/doku.php?id=equipment:sword),
  [Battle Axe](https://wiki.diceydungeons.com/doku.php?id=equipment:battle_axe),
  [Bump](https://wiki.diceydungeons.com/doku.php?id=equipment:bump),
  [Matchstick](https://wiki.diceydungeons.com/doku.php?id=equipment:matchstick)
  and [Combat Roll](https://wiki.diceydungeons.com/doku.php?id=equipment:combat_roll).
- S4: community references for [Snowball](https://wiki.diceydungeons.com/doku.php?id=equipment:snowball),
  [Fireball](https://wiki.diceydungeons.com/doku.php?id=equipment:fireball),
  [Frozen](https://wiki.diceydungeons.com/doku.php?id=statuses)
  and [Burn](https://wiki.diceydungeons.com/doku.php?id=statuses:burn).
  The reference describes overriding the highest face with one.
  The unmodified roll and that priority are not visible in the trace.
- W1: [App Unwrapper, Warrior Episode 1](https://www.youtube.com/watch?v=-xa6XJmQiC8&t=456s).
  The launch-period mobile recording links the App
  Store and does not establish an Android OS. Key frames are
  7:51, 8:01, 8:05–8:08, 8:13–8:26, 8:36–8:42,
  8:45 and 8:57–9:03.
- W2: [KruGames, English mobile walkthrough](https://www.youtube.com/watch?v=J10ixU5kFRk&t=420s),
  published 20 July 2022. The title names Android and iOS,
  with no verified capture OS. Earlier teaching frames show the
  same class and equipment, and its different first ordinary opponent
  also precedes an experience-triggered equipment offer.
- Claim IDs: DD-001–DD-008.

### Reproducible route evidence

1. Start the first Warrior episode. Complete its introductory
   sequence and carry the four named pieces forward while the
   Warrior is level two. On the first recorded Floor 2 layout,
   tap the route to the normal Marshmallow. The exact same
   generated floor and rolls were not reproduced on demand.
2. At 7:51 the Warrior has 24/28 health, and the rival has
   28/28. Spend a six on Sword. Put the three into Bump,
   then put the resulting four into Battle Axe. The health
   changes first to 22 and then to 14. Reroll the remaining five,
   obtaining six here, and put it into the even Matchstick.
3. End Turn. At 8:13 the rival has rolled. It pays two
   health before allocating the burned die. Snowball uses the
   odd five and Fireball the even six. The Warrior starts the
   next turn at 13/28, including a die marked for extinguishing
   and a frozen one. The rival has 12/28.
4. At 8:26 place four into Battle Axe, leaving rival health at
   four. After rerolling and extinguishing the marked die, the
   Warrior has 11/28 and the free values three and two. Use Bump
   on three. Place the resulting four into Sword at 8:39.
   The remaining two is not needed. The victory appears at 8:41.
5. Read the one-coin and two-experience award at 8:42. Select
   Spiked Shield on the reward screen. The map at 8:57 shows
   the Warrior at level three and 32/32, and opening Equipment
   shows the shield in the backpack. The next equipment
   decision is available. The following rearrangement is outside
   the selected fight.

## Mechanical decomposition

### Action Genes

- ACT-126: End Turn explicitly transfers the live player phase to
  the autonomous rival, leaving any unused dice uncommitted.
  DD-004.
- ACT-881: allocate one displayed die to a selected equipped
  socket. This also covers putting it into Combat Roll or Bump.
  DD-002, DD-003.
- ACT-882: choose one offered piece of run equipment after the
  level result; the chosen shield enters carried storage and the
  previous combat loadout stays equipped. DD-008.

### System Behaviour Genes

- SYS-004: both sides receive random faces, and Combat Roll
  can produce a new random face for the selected token. DD-003, DD-004.
- SYS-299: the fight's experience meets the level threshold.
  The level change raises maximum health, refills health and
  makes a gear choice available. DD-008.
- SYS-362: defeating the rival settles one coin and two
  experience before navigation resumes. DD-007.
- SYS-1907: a successful equipment input uses up an available
  die and resolves the effect defined by that equipment. Sword
  and Battle Axe multiply the same face by different factors.
  DD-002, DD-006.
- SYS-1908: Bump consumes the input and returns its increased value
  for another socket in the same turn. DD-003, DD-006, DD-007.
- SYS-1909: Combat Roll substitutes one rolled face using its own
  limited turn allowance without discarding the other dice. DD-003.
- SYS-1910: Burn marks a forthcoming die. Recover that die by
  paying health, or leave it unused. DD-005–DD-007.
- SYS-1911: Freeze changes a forthcoming die to face one
  rather than removing the token. DD-005.

### Constraint Genes

- CON-878: the target socket checks the chosen face; the axe
  rejects high values while Matchstick and the rival's attacks
  test parity. DD-002, DD-005.
- CON-879: individual equipment uses limit the current phase.
  Reusable equipment, once-per-turn weapons and a three-use
  reroll have separate allowances. DD-003, DD-004.

### Information Genes

- INF-002: upcoming faces are not previewed. Act with the
  displayed pool rather than a known future roll. DD-003, DD-004.
- INF-612: read visible faces, valid predicates, calculated
  effects, remaining uses, health and status markers. DD-002–DD-005.

### Objective Genes

- OBJ-029: defeat the one required enemy before the
  controlled Warrior is defeated. The final blow ends combat
  even with a die still free. DD-007.

### Time Genes

- TIM-047: both opponents take complete phases; the player
  resolves their equipment effects as they commit them and a
  surviving foe rolls and selects its own actions after End
  Turn. Repeat until a terminal result. DD-004, DD-007.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Warrior 24/28, foe 28/28, dice 6, 3 and 5 | Allocate 6 to Sword | Foe 22/28, Sword spent for the turn | DD-002, DD-006 |
| Free 3 and unused Bump | Commit 3 to Bump, then put 4 into Battle Axe | The input becomes an eligible four. Axe spends it for eight damage | DD-003, DD-006 |
| Free 5 and unused reroll | Combat Roll, then put the resulting 6 in Matchstick | Reroll allowance drops; the even value marks a rival die, and Matchstick remains available | DD-003–DD-006 |
| Warrior commits End Turn with foe at 14/28 | Rival rolls, pays to clear Burn and assigns its odd and even dice | Rival 12/28; Warrior takes eleven damage, Freeze and Burn | DD-004–DD-006 |
| Next Warrior phase, foe 12/28 | Axe 4, pay two health to clear Burn, Bump 3 into Sword 4 | Foe defeated; unused two is discarded and the fight pays one coin plus two experience | DD-007 |
| Experience meets the level threshold | Choose Spiked Shield over Boomerang | Level three, 32/32 health, map and loadout access return; shield waits in backpack | DD-008 |

## Strategic and experiential structure

Treat six as powerful Sword fuel, but not legal axe fuel. A
three can deal six through the axe now or become a four via
Bump and deal eight. A spare odd die can be rerolled for an
even Matchstick input, but no particular face is guaranteed.
The rival can pay for its marked die and still act. Clearing
the second-turn Burn costs health before the resulting die
can help make the finishing blow. Taking the level reward
changes what can be equipped in later fights.

## Replay and variation

Different generated opponents and dice change the route and
legal allocations. The trace proves one winning ordering and
one reward choice rather than an optimal policy. It does not
establish the seed, a method for guaranteeing this draw or
the effects of choosing Boomerang in that particular save.

## Adjacent systems and history

The first-run tutorial introduces the equipment and Warrior
class before this ordinary fight. The Android listing includes
other content, but alternate episodes and Reunion can change
the opponent's equipment and the character loop.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-126, ACT-881, ACT-882 | End the phase, assign a die and claim one level reward |
| System Behaviour | SYS-004, SYS-299, SYS-362, SYS-1907, SYS-1908, SYS-1909, SYS-1910, SYS-1911 | Roll, settle and level, resolve formulas, transform selected dice and apply statuses |
| Constraint | CON-878, CON-879 | Check each face and the equipment's turn allowance |
| Information | INF-002, INF-612 | See current dice and effects without a future roll preview |
| Objective | OBJ-029 | Defeat the required opponent while still alive |
| Time | TIM-047 | Alternate sequential, independently resolved combat phases |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `663` (`GAME-0001`–`GAME-0663`).
- Exact genome matches: none.
- Tied near matches: `GAME-0486` — Final Fantasy Tactics (`4 / 39 = 0.102564`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Final Fantasy Tactics (GAME-0486)](final-fantasy-tactics.md) | `OBJ-029`, `SYS-004`, `SYS-299` and `SYS-362`: defeat the bounded hostile set; allow chance in resolution and track encounter credit and experience progression. | The tactical battle assigns commands on tiles and uses chances such as hit outcomes. The Warrior allocates visible rolled inputs to fixed equipment sockets, alters those inputs, and hands off to a rival with its own roll. | Near, `0.102564` |

## Taxonomy impact

ACT-881 allocates a typed input rather than choosing a target
as in ACT-019. ACT-882 puts a level-choice item into equipment
storage; ACT-128 chooses or skips a deck addition instead.
SYS-1907 resolves the actual equipment formula. SYS-1908
and SYS-1909 preserve the chance to reassign a generated die
within the same turn, respectively through a declared change
and a reroll. SYS-1910 and SYS-1911 affect resources before
allocation, unlike a periodic health-only status. CON-878
checks value and CON-879 checks an independent use allowance.
INF-612 exposes the live facts that govern both tests. TIM-047
requires a later opposing roll rather than an already
committed intent under TIM-005.

## Negative results

- A high face is not universally better. Six cannot activate
  the base Battle Axe and five fails Matchstick's parity rule.
- Reroll does not replace the entire pool or guarantee
  improvement. Bump returns a useful new value without a
  reroll in the observed cases.
- Burn does not make a rolled resource permanently unavailable.
  Freeze preserves its token with a different value.
- A level reward enters storage. Taking it does not replace
  the current equipment in the observed return state.
- The Android build number, seeded layout, failed-run
  persistence and a simultaneous defeat were not verified.

## Delta summary

Seventeen scoped genes, eleven new boundaries and six reuses.

## New facts

- A die may power damage, become a new input or put a condition
  on the opponent's next roll, depending on the accepting socket.
- The fight ends during the player phase, with a die still free
  and before another enemy phase begins.
- The encounter settles combat credit and only then offers the
  level-dependent choice that adds a new carried item.

## Principles and design implications

Separate the input's value gate, the effect calculation and the
number of permitted uses. Show all three so a player can plan
whether to spend, change or keep a die. Let encounter settlement
present the next decision without equipping the chosen reward for
the player.

## Puzzle or game generation potential

An original small equipment puzzle could supply three valued
tokens and competing devices with upper-bound or parity tests.
Make one device transform an existing token so sequencing
matters even with no additional random roll.

## New genes

- ACT-881
- ACT-882
- CON-878
- CON-879
- INF-612
- SYS-1907
- SYS-1908
- SYS-1909
- SYS-1910
- SYS-1911
- TIM-047

## New combinations

None. None of the 274 verified combination signatures is a proper subset of the scoped genome.

## Taxonomy changes

[TAXONOMY_CHANGE_410](../../../research/taxonomy-changes/TAXONOMY_CHANGE_410.md).

## New questions

Can the same scenario be followed on a version-identified,
authenticated Android build? How do Frozen and Burn interact
on the same die across other episodes or against another
specific opponent? How does the run settle if paying to
extinguish a die consumes the owner's final health?

## Next recommended game

Sega Worldwide Soccer '97, original North American Sega
Saturn commercial release. Follow a complete ordinary match
through regulation, settlement and its next actionable state.

## Why this game

One short fight links value-gated equipment, transformation of
rolled resources, enemy retaliation and a threshold-triggered
decision that carries into the next encounter.
