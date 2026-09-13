---
game_id: GAME-0288
slug: sekiro-shadows-die-twice
game_title: "Sekiro™: Shadows Die Twice - GOTY Edition"
analysis_status: reviewed
reviewed: 2026-09-10
combination_ids:
  - COMB-0274
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-202
    - ACT-223
    - ACT-224
    - ACT-235
    - ACT-361
    - ACT-383
    - ACT-419
    - ACT-425
    - ACT-438
    - ACT-452
  system:
    - SYS-035
    - SYS-215
    - SYS-364
    - SYS-373
    - SYS-409
    - SYS-578
    - SYS-653
    - SYS-846
    - SYS-847
    - SYS-848
    - SYS-849
    - SYS-853
  constraint:
    - CON-282
    - CON-324
    - CON-335
    - CON-589
    - CON-628
  information:
    - INF-043
    - INF-119
    - INF-142
    - INF-295
    - INF-319
    - INF-334
    - INF-335
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Sekiro™: Shadows Die Twice - GOTY Edition

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Runtime names and
quantities parameterise the genes but do not enter their canonical labels.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `814380`, one-app package `298554`, public Build ID `5794815`, observed
  2026-09-10. FromSoftware's current official PC patch is App Ver. `1.06`,
  published 2020-11-20. Valve's numeric build and the publisher's semantic
  version are separately graded observations rather than an asserted mapping.
  The storefront title is `Sekiro™: Shadows Die Twice - GOTY Edition`; this
  packet uses only its ordinary base-game New Game route.
- Entry: choose New Game on a clean English profile and accept first ordinary
  control in Ashina Reservoir. Story delivery establishes the Kusabimaru,
  Healing Gourd and later Shinobi Prosthetic, but this packet records only the
  movement, stealth, grapple, combat, death and checkpoint rules exercised on
  the required route.
- Primary decision loop: read route geometry, green grapple anchors, hostile
  awareness, Vitality, Posture, resurrection readiness, attack motion,
  Perilous Attack warning, enemy Posture and remaining Deathblow markers;
  navigate, crouch and grapple through authored terrain; choose stealth
  Deathblows where an unaware target is reachable; lock on, strike, hold guard
  or time a deflection; answer the declared Perilous Attack form with its
  matching deflection, jump or step; use a Posture break to commit a Deathblow;
  choose whether to spend a ready Resurrection charge after lethal defeat;
  rest at Sculptor's Idols while accepting resource recovery and ordinary-enemy
  respawn; follow the required route through Gyoubu Masataka Oniwa.
- Positive terminal: defeat Gyoubu by consuming every required Deathblow marker,
  leave the arena by the ordinary successor route and commune with the nearby
  Ashina Castle Gate Sculptor's Idol. The activated idol and continuing player
  control are the bounded successor state; no reload claim is made.
- Negative terminal: when lethal defeat settles without a legal or chosen
  Resurrection, true death returns the player to the last communed idol and
  permanently removes half of current unbanked Sen and Skill Experience unless
  Unseen Aid preserves them. This closes that attempt but not the fresh save.
- Included: direct traversal; crouch and perception-driven stealth; marked
  grapple anchors; ordinary sword attacks; sustained guard and timed deflection;
  Perilous Attack response selection; player and enemy Vitality/Posture;
  health-dependent Posture recovery; stealth and Posture-break Deathblows;
  multiple required Deathblow markers; charged in-place Resurrection and its
  post-use lock; true-death checkpoint return and fractional loss; Sculptor's
  Idol rest, refill and ordinary-enemy respawn; the required boss-to-idol gate.
- Excluded: Reflection and Gauntlet of Strength, Change Form and Remnants added
  by the free GOTY update; New Game Plus, alternate endings, later regions,
  optional bosses and speedrun routing; prosthetic-tool attacks and Spirit
  Emblem economy; Combat Arts, Ninjutsu, skill purchase, Prayer Necklaces,
  Memory attack upgrades and merchants; controller and console versions; mods,
  online remnants, achievements, screenshots, official or third-party artwork,
  video and audio evidence.
- Reproducible parameterisation: use English Windows app `814380`, package
  `298554`, App Ver. `1.06`, a clean New Game and the ordinary route described
  by the two static walkthroughs. Commune with every required-route idol,
  demonstrate at least one crouched stealth Deathblow, one marked grapple, one
  held guard, one timed deflection, one matching Perilous response, one
  Posture-break Deathblow and one Resurrection before defeating Gyoubu and
  activating Ashina Castle Gate. Exact damage, timing, Sen, experience, attack
  order, optional pickups and number of ordinary deaths are parameters.
- Potential scoped modules: one prosthetic-tool route, one skill or Prayer
  Necklace progression packet, one Reflection or Gauntlet, one later boss,
  one ending route or New Game Plus each requires its own version, entry, loop,
  terminal and evidence.
- Direct-play status: not conducted. The current application was not installed
  and no local or Steam Cloud save was available. Official PC manual pages own
  the movement, stealth, grapple, posture, deflection, Deathblow,
  resurrection, death-loss and idol rules. Two fully read static written routes
  establish the ordered Ashina Reservoir and Ashina Outskirts path, Gyoubu's
  required settlement and the successor idol. This is an evidence-backed rules
  reconstruction, not a claimed playthrough or reload. No video or audio was
  opened, played, heard or analysed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SEK-001` | The admitted product is the Windows GOTY-labelled Steam app `814380` delivered alone by package `298554` | Confirmed | Direct | High | P1, P2 |
| `SEK-002` | The public branch projects Build ID `5794815`; the official current PC patch is App Ver. `1.06` | Observation | Corroborated | High | P3, P4 |
| `SEK-003` | The GOTY update's Reflection, Gauntlet, Change Form and Remnant features are separable from ordinary New Game | Confirmed | Direct | High | P5, P6 |
| `SEK-004` | Direct movement, crouch, ledge movement and marked grapple anchors support the opening route | Confirmed | Direct | High | P7, S1, S2 |
| `SEK-005` | Crouching and cover reduce detection, while completed detection changes an unaware target into combat | Confirmed | Direct | High | P7, S1, S2 |
| `SEK-006` | Sword attacks damage Vitality and Posture; guard and timed deflection differ in Posture cost and effect | Confirmed | Direct | High | P7, P8 |
| `SEK-007` | Lower Vitality slows Posture recovery, guard accelerates own recovery and continued attacks interrupt enemy recovery | Confirmed | Direct | High | P8, P9 |
| `SEK-008` | Perilous Attack forms cannot be ordinarily guarded and require a matching deflection, jump or step response | Confirmed | Direct | High | P8, P9 |
| `SEK-009` | An unaware or Posture-broken target exposes a Deathblow, and strong enemies require every displayed marker | Confirmed | Direct | High | P8, P9 |
| `SEK-010` | Confirmed Resurrection consumes one ready charge and restores control in place; it separately applies a repeat-use lock, qualifying combat progress clears that lock, ordinary enemy defeats rebuild additional charge, and rest restores the base charge | Confirmed | Direct | High | P9 |
| `SEK-011` | True death returns to the last communed idol and loses half of current Sen and Skill Experience unless Unseen Aid triggers | Confirmed | Direct | High | P9 |
| `SEK-012` | Idol rest restores declared resources and respawns eligible ordinary enemies | Confirmed | Direct | High | P9, P10 |
| `SEK-013` | The ordinary opening route proceeds through Ashina Reservoir and Outskirts to required Gyoubu, then the nearby Ashina Castle Gate idol | Observation | Corroborated | High | S1, S2 |
| `SEK-014` | No current executable or save was available, so the terminal is textually bounded rather than directly executed or reload-verified | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: FromSoftware / Activision outside Japan and Asia,
  2019-03-21; storefront currently labels the product GOTY Edition.
- Platform or physical form: lawfully available English Windows Steam
  application `814380`, package `298554`; no local entitlement or execution is
  claimed.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-10:
  - `P1` — [Valve application data](https://store.steampowered.com/api/appdetails?appids=814380&cc=ua&l=english),
    for exact title, developer, publisher, release date, Windows platform,
    single-player delivery and lawful availability.
  - `P2` — [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=298554&cc=ua&l=english),
    for the one-app package boundary.
  - `P3` — [SteamCMD public-branch projection](https://api.steamcmd.net/v1/info/814380),
    for Build ID `5794815` and its branch timestamp; secondary distribution
    observation rather than publisher-authored semantic versioning.
  - `P4` — [official App Ver. 1.06 notice](https://www.sekiro.jp/news_detail_201118_01.html),
    for the current named PC patch and publication date.
  - `P5` — [official App Ver. 1.05 notice](https://www.sekiro.jp/news_detail_201029_01.html),
    for the free-update feature boundary.
  - `P6` — [official free-update announcement](https://www.sekiro.jp/news_detail_200729_01.html),
    for Reflection, Gauntlet, Change Form and Remnants as optional additions.
  - `P7` — [official PC action manual](https://www.fromsoftware.jp/manual/sekiroshadowsdietwice/win/action1.html),
    for traversal, crouch, detection, attack, guard, deflection, lock-on and
    marked grapple anchors.
  - `P8` — [official PC advanced-action manual](https://www.fromsoftware.jp/manual/sekiroshadowsdietwice/win/action2.html),
    for stealth Deathblows, repeated markers and Perilous Attacks.
  - `P9` — [official PC mechanics manual](https://www.fromsoftware.jp/manual/sekiroshadowsdietwice/win/basic.html),
    for Vitality/Posture coupling, resurrection, true death, Unseen Aid and
    Deathblow requirements.
  - `P10` — [official PC Sculptor's Idol manual](https://www.fromsoftware.jp/manual/sekiroshadowsdietwice/win/onibotoke.html),
    for rest, refill, respawn and the separation of GOTY modes.
  - `P11` — [official PC start manual](https://www.fromsoftware.jp/manual/sekiroshadowsdietwice/win/start.html),
    for New Game, Continue, Load and autosave; it does not establish a performed
    reload.
- Corroborating textual sources, accessed 2026-09-10:
  - `S1` — [PowerPyx Ashina Reservoir route](https://www.powerpyx.com/sekiro-shadows-die-twice-ashina-reservoir-walkthrough/)
    and [Ashina Outskirts route](https://www.powerpyx.com/sekiro-shadows-die-twice-ashina-outskirts-walkthrough/),
    for the ordinary opening sequence, required obstacles, Gyoubu defeat and
    nearby successor idol.
  - `S2` — [GameFAQs GOTY Ashina Reservoir route](https://gamefaqs.gamespot.com/ps4/296954-sekiro-shadows-die-twice-game-of-the-year-edition/faqs/80265/ashina-reservoir-prologue)
    and [TrueAchievements written walkthrough](https://www.trueachievements.com/game/Sekiro-Shadows-Die-Twice/walkthrough/3),
    for independent static corroboration of the prologue, tutorial mechanics
    and ordered opening route. Platform-specific controls are not imported.
- Research record: `R1` — local preflight on 2026-09-10 found no installed app,
  local save or accessible Steam Cloud save.
- Claim IDs: `SEK-001`–`SEK-014`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008` owns direct route traversal; `ACT-161` ordinary sword
  strikes; `ACT-202` crouch; `ACT-223` the choice among timed deflection, jump
  and step responses; `ACT-224` deliberate idol rest; `ACT-383` held sword
  guard; `ACT-419` the contextual Deathblow after a Posture break; `ACT-425`
  the timed close-weapon deflection; and `ACT-438` the selected hostile lock-on.
- Generalised `ACT-235` owns a close neutralisation against an unaware reachable
  hostile without requiring the first carrier's grab and body-carry step.
  Generalised `ACT-361` owns the marked grappling-line approach without making
  the first carrier's consumable stock part of the action.
- New `ACT-452` owns the post-defeat player command that spends a ready charge
  to continue the same encounter in place.
- Rejected `ACT-200`: the Healing Gourd exists, but neither its use nor a
  completed interruptible restorative transition is required by this packet.
  Rejected `ACT-249`: true death creates no recoverable world mark. Claims:
  `SEK-004`–`SEK-012`.

### System Behaviour Genes

- Existing `SYS-215` owns directly commanded real-time combat; `SYS-364` idol
  rest and ordinary-enemy repopulation; `SYS-373` suspicion into detection and
  combat; `SYS-578` the continuous Vitality pool; generalised `SYS-409` the
  presentation-independent stability threshold into a critical opening; and
  generalised `SYS-653` grappling-line attachment and approach without folding
  availability or consumption into the resolution.
- New `SYS-846` makes lower health slow a separate stability state's recovery.
  New `SYS-847` requires sequential critical executions before a protected
  hostile is finally defeated. Narrowed `SYS-848` settles confirmed charged
  in-place recovery. Existing `SYS-035` owns combat-earned replenishment of an
  additional recovery charge, while new `SYS-853` applies and clears the
  independent consecutive-use lock. Existing `SYS-364` already owns restoration
  of the base charge at idol rest. New `SYS-849` settles true death at the
  checkpoint with fractional unbanked loss and conditional preservation.
- Resolution order: position and awareness determine stealth access; an attack,
  guard or deflection updates Vitality and Posture; health bands modify Posture
  recovery; a Posture threshold creates a Deathblow opportunity; the command
  consumes one remaining marker and either resumes the encounter or defeats the
  hostile; lethal player damage opens charged Resurrection before true death;
  chosen recovery consumes one charge and continues in place, then applies its
  separate lock; qualifying combat progress clears the lock and ordinary enemy
  defeats rebuild additional charge independently; otherwise true death returns
  to the idol with the declared loss; rest restores the base charge and other
  resources while respawning ordinary enemies; the final Gyoubu marker opens
  the successor route. Claims: `SEK-005`–`SEK-013`.

### Constraint Genes

- Existing `CON-282` owns the required authored boss gate; `CON-324` the live
  timing match for deflection, jump or step; generalised `CON-335` the unaware
  reachable predicate for stealth neutralisation; and `CON-589` the live
  reachable Posture-break window for a contextual Deathblow.
- New `CON-628` requires both a ready resurrection charge and a cleared
  consecutive-use lock.
- Rejected `CON-427`: its fixed per-mission stock does not replenish from idol
  rest or combat. Rejected `CON-533`: Sekiro grappling is a reusable capability,
  not carried hook stock. Exact timing, marker counts, loss amounts and charge
  fill are parameters. Claims: `SEK-004`–`SEK-013`.

### Information Genes

- Generalised `INF-043` owns green marking for currently reachable grapple
  anchors without requiring architectural reconfiguration. Existing `INF-119`
  owns personal Vitality, Posture and resurrection readiness; `INF-142` visible
  attack motion and prompts as timing cues; `INF-295` the temporary Deathblow
  opportunity; and `INF-319` the warning plus attack form that determines the
  legal Perilous response. No audio evidence contributes to `INF-142` here.
- Narrowed `INF-334` exposes the enemy's breakable Posture state. New
  `INF-335` separately exposes the remaining Deathblow-marker count.
- Rejected `INF-318`: a boss health bar alone does not capture the Posture and
  marker requirement. Rejected `INF-298`: the official text establishes
  detection rules but not the lower-ID awareness-display boundary. Claims:
  `SEK-004`–`SEK-013`.

### Objective Genes

- Existing `OBJ-080`: complete the bounded authored route by defeating its
  mandatory guardian and crossing into the declared successor checkpoint.
  Here success requires every Gyoubu Deathblow marker and communion with Ashina
  Castle Gate; merely entering the arena or landing one Deathblow is not enough.
  Claims: `SEK-013`, `SEK-014`.

### Time Genes

- Existing `TIM-003`: traversal, perception, attacks, Posture recovery,
  Resurrection windows and hostile behaviour advance in real time while inputs
  remain accepted. Claims: `SEK-004`–`SEK-013`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh New Game has reached first Ashina Reservoir control | Move, jump, ledge-hold and crouch through the opening | The persistent controlled body crosses only locally traversable authored geometry | fixed clean entry and traversal | `SEK-004` |
| An eligible hostile is unaware and reachable from a valid close position | Commit the displayed stealth Deathblow | The hostile is neutralised without first entering ordinary alerted combat | awareness-gated close neutralisation | `SEK-005`, `SEK-009` |
| A terrain anchor is in current grapple range | Aim until it is green and commit the grapple | The tether attaches and moves the player along its bounded path without consuming carried stock | marked reusable grapple | `SEK-004` |
| A hostile attack is incoming | Hold guard, then on another attack tap guard near contact | Sustained guard protects while increasing player Posture; the timed deflection redirects pressure into the attacker more efficiently | guard versus deflection | `SEK-006` |
| A Perilous warning appears and the attack's motion identifies its form | Choose the matching deflection, jump or step at contact | Ordinary guard is invalid; only the form-matched response can avoid or counter the attack | typed reactive legality | `SEK-008` |
| Enemy Vitality has been reduced | Stop attacking and compare its Posture recovery | Recovery is slower at lower Vitality; renewed attacks interrupt that recovery and keep the break reachable | coupled health and stability | `SEK-007` |
| Enemy Posture crosses its break threshold while the target is reachable | Commit the Deathblow during the visible opportunity | One remaining execution marker is consumed; a survivor resumes combat, while the final marker settles defeat | break, critical command and sequential markers | `SEK-009` |
| Player Vitality reaches zero and a charge is ready with no active lock | Choose Resurrection | One charge is consumed, health and control return to the same body and position in the live encounter, and a separate lock bars consecutive use | charged in-place settlement and lock application | `SEK-010` |
| A Resurrection has applied its consecutive-use lock while another charge may already be ready | Defeat qualifying hostiles or perform qualifying Deathblows | The declared combat progress clears the separate lock without itself needing to add charge | combat-earned lock clearance | `SEK-010` |
| An additional Resurrection charge is not full | Defeat ordinary hostiles and collect their declared recovery-power contribution | Earned progress fills the bounded additional charge independently of whether the post-use lock is active | combat-earned charge replenishment | `SEK-010` |
| Lethal defeat settles without a legal or chosen Resurrection | Accept true death | Control returns at the last communed idol and half of current unbanked Sen and Skill Experience is removed unless Unseen Aid triggers | checkpoint loss without a world mark | `SEK-011` |
| A Sculptor's Idol has been communed with | Rest | Declared player resources, including the base Resurrection charge, refill and eligible defeated ordinary enemies repopulate | checkpoint reset trade | `SEK-010`, `SEK-012` |
| Gyoubu's final required marker is consumed | Leave the arena and commune with Ashina Castle Gate | The required guardian remains defeated and the successor idol becomes the bounded continuing state | positive terminal | `SEK-013`, `SEK-014` |

## Strategic and experiential structure

- Planning horizon: visible Vitality, Posture, resurrection availability,
  hostile Posture and marker count turn each exchange into a choice between
  maintaining pressure, recovering stability, guarding or risking a deflection.
- Local tactics: crouch and vertical grapples preserve surprise before combat;
  once engaged, lower Vitality to slow recovery, then maintain Posture pressure
  and convert the short break window into the required Deathblow.
- Medium-term structure: idol rest restores the base charge but repopulates
  ordinary hostiles; Resurrection can preserve arena position once, while
  combat-earned additional charge and independently cleared lock state govern
  a later use.
- Reversible versus irreversible: movement, lock-on, guard and Posture pressure
  change momentary state; true death irreversibly removes a fraction of current
  unbanked measures unless protection triggers; the final guardian defeat and
  activated successor idol persist for continued routing.
- Failure attribution: attack motion, Perilous classification, both Posture
  states, marker count and resurrection readiness expose why a defence, break,
  execution or recovery was or was not available.
- Player trust: the same official rules distinguish temporary lethal defeat
  from true death and state the exceptional Unseen Aid branch rather than
  presenting every loss as deterministic.

## Replay and variation

- What changes: stealth versus alerted encounters, grapple order, pressure
  cadence, defensive response, Resurrection use, death count and incidental
  currency or experience.
- Randomness or procedural generation: route topology, required boss and idol
  are authored. Unseen Aid conditionally varies the true-death penalty; exact
  hostile move selection varies without changing the response predicates.
- Multiple strategies: ordinary enemies may be bypassed, stealth-killed or
  fought; posture pressure may come from attacks or deflections; Resurrection
  may be spent or withheld. The required Gyoubu settlement is fixed.
- Typical replay motive: reach the guardian with more recovery capacity, read
  attack forms more cleanly and complete the marker sequence without true death.

## Adjacent systems and history

- DARK SOULS III shares direct melee, lock-on, checkpoint rest, real-time
  guard pressure and a required opening boss. Its shared exertion reserve and
  recoverable death mark differ from Sekiro's Posture exchange, in-place charged
  Resurrection and immediate fractional loss.
- Elden Ring shares stability breaks, critical follow-ups and authored
  checkpoint routing. Its packet depends on equipment, levelling, open-world
  routing and a recoverable rune mark rather than sequential Deathblow markers.
- Black Myth: Wukong shares guard-free timed defence, a health pool, checkpoint
  reset and required guardian route. It retains resources on checkpoint return
  and lacks Sekiro's sustained guard, two-sided Posture and Resurrection lock.
- STAR WARS Jedi: Fallen Order shares held guard, timed close-weapon parry and
  checkpoint enemy respawn, but not the health-dependent Posture recovery,
  execution-marker sequence or charged post-defeat continuation.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-202`, `ACT-223`, `ACT-224`, `ACT-235`, `ACT-361`, `ACT-383`, `ACT-419`, `ACT-425`, `ACT-438`, `ACT-452` | named techniques, inputs, actors and positions are parameters |
| System Behaviour | `SYS-035`, `SYS-215`, `SYS-364`, `SYS-373`, `SYS-409`, `SYS-578`, `SYS-653`, `SYS-846`, `SYS-847`, `SYS-848`, `SYS-849`, `SYS-853` | damage, recovery, loss fractions, charge counts and marker counts are parameters |
| Constraint | `CON-282`, `CON-324`, `CON-335`, `CON-589`, `CON-628` | timing windows, reach, charge and route order are parameters |
| Information | `INF-043`, `INF-119`, `INF-142`, `INF-295`, `INF-319`, `INF-334`, `INF-335` | colour, icon, motion, wording and layout are parameters |
| Objective | `OBJ-080` | guardian and successor checkpoint are parameters |
| Time | `TIM-003` | animation and recovery timing are implementation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `287` (`GAME-0001`–`GAME-0287`).
- Exact genome matches: none.
- Tied near matches: `GAME-0263` — God of War (`14 / 49 = 0.285714`).
- Supported combination subsets: `COMB-0274`.
- Scan date: 2026-09-10.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0263` — God of War | `ACT-008`, `ACT-161`, `ACT-223`, `ACT-419`, `SYS-215`, `SYS-409`, `SYS-578`, `CON-282`, `CON-324`, `INF-119`, `INF-142`, `INF-295`, `INF-319`, `TIM-003` | Both routes use direct real-time melee, timed responses selected from visible attack categories, a stability break converted into a close execution and an authored guardian gate. God of War adds a thrown-and-recalled weapon, autonomous companion, checkpoint rollback and one health-threshold encounter transition. Sekiro instead adds crouched stealth, marked grappling, sustained guard and deflection, independently visible Posture and remaining Deathblow counts, charged in-place Resurrection, combat-earned charge replenishment, an independently cleared repeat-use lock and fractional true-death loss. | Near, `14 / 49 = 0.285714` |

## Preserved research notes

- Official PC textual material establishes every core combat, death and
  checkpoint rule. Static walkthroughs are used only for the route order and
  named terminal.
- The public Build ID is a secondary distribution observation and is not
  represented as an official semantic-version mapping.
- Direct play and reload verification were not available and are not claimed.
- No audiovisual evidence was used; no source image contributes to artwork.

## Taxonomy impact

- `TAXONOMY_CHANGE_056` generalises six lower-ID carrier-bound labels or
  definitions without changing any earlier signature: `ACT-235`, `ACT-361`,
  `SYS-409`, `SYS-653`, `CON-335` and `INF-043`.
- `TAXONOMY_CHANGE_067` narrows `SYS-848` to the charged in-place recovery
  settlement, reuses `SYS-035` for combat-earned additional charge and adds
  `SYS-853` for the independent post-use lock lifecycle. Existing `SYS-364`
  retains the base-charge refill at rest.
- New `COMB-0274` records the strict Posture-break, sequential-execution and
  charged-continuation interaction. Generic traversal, stealth, route gate,
  broad combat and time remain outside it.
- No earlier game signature, lifecycle, combination membership or family
  assignment changes.

## Negative results

- Lower-ID Action scan rejected `ACT-200` and `ACT-249`; the scoped route does
  not require an evidenced completed restorative cast and creates no death mark.
- Lower-ID System scan rejected `SYS-399`, `SYS-610`, `SYS-732`, `SYS-777`,
  `SYS-798` and `SYS-799`; their recoverable mark, full retention, match extra
  life, durability, shared exertion or health-phase boundaries differ.
- Lower-ID Constraint scan rejected `CON-427`, `CON-533` and `CON-604`; the
  recovery replenishes and locks separately, the grapple is not stocked and no
  stamina reserve prices offence and defence.
- The correction's complete lower-ID Information scan retains `INF-334` for
  visible enemy Posture and adds `INF-335` for remaining Deathblow requirements.
  It rejects `INF-129`, `INF-141`, `INF-156`, `INF-157`, `INF-210`, `INF-254`,
  `INF-282`, `INF-295`, `INF-313`, `INF-318` and `INF-329`: survivor totals,
  turn HUDs, breakable regions, faint allowance, round markers, stocks,
  challenge progress, brief opportunities, regional damage, guardian health
  and task completion each omit or import a defining disclosure. `INF-298`
  remains rejected because the scoped perception display is not evidenced.
- The correction's complete lower-ID System scan reuses `SYS-035` for
  performance-earned additional charge and `SYS-364` for the base charge at
  rest. It retains distinct settlement, cooldown, reserve, extra-life,
  last-chance and checkpoint-return owners; none owns a separately applied
  consecutive-use lock cleared by combat progress.
- Lower-ID Objective scan found `OBJ-080` sufficient; boss and idol names stay
  parameters. Combination subset scan found no existing Verified combination
  with the new Posture–marker–Resurrection relation.
- Prosthetic tools, Spirit Emblems, skill purchase, Memory upgrades and every
  optional GOTY mode are excluded by the declared packet.

## Delta summary

- New facts: one lawful current GOTY-labelled Windows product; one bounded
  fresh opening route; twelve reproducible transitions; one boss-to-idol
  terminal; one explicit direct-play and audiovisual boundary.
- Reused genes: `29` — `ACT-008`, `ACT-161`, `ACT-202`, `ACT-223`, `ACT-224`,
  `ACT-235`, `ACT-361`, `ACT-383`, `ACT-419`, `ACT-425`, `ACT-438`, `SYS-035`,
  `SYS-215`, `SYS-364`, `SYS-373`, `SYS-409`, `SYS-578`, `SYS-653`, `CON-282`,
  `CON-324`, `CON-335`, `CON-589`, `INF-043`, `INF-119`, `INF-142`, `INF-295`,
  `INF-319`, `OBJ-080` and `TIM-003`.
- New genes: `9` — `ACT-452`, `SYS-846`, `SYS-847`, `SYS-848`, `SYS-849`,
  `SYS-853`, `CON-628`, `INF-334` and `INF-335`.
- New combinations: `1` — `COMB-0274`.
- Taxonomy changes: `3` — `TAXONOMY_CHANGE_056`, `TAXONOMY_CHANGE_066` and
  `TAXONOMY_CHANGE_067`.
- Ukrainian review: unchanged reused meanings verified; six generalised and
  eight new records plus all game-owned presentation corrected; only official
  names, identifiers and version strings retained with reason.

## New facts

- A target's health can govern the recovery rate of a separate breakable
  stability state without becoming that state.
- A critical execution can consume one visible requirement and return the same
  hostile to combat until the final requirement is removed.
- A charged in-place continuation can remain unavailable despite stored charge
  because a second post-use lock has not cleared.
- Checkpoint return can destroy a fraction immediately, with a separately
  sampled protection exception, rather than placing value in the world.

## New genes

- `ACT-452` — Spend a ready charge to resume control after lethal defeat.
- `SYS-846` — Couple lower health to slower stability recovery.
- `SYS-847` — Require sequential critical executions to defeat a protected
  hostile.
- `SYS-848` — Resolve charged in-place self-recovery after lethal defeat.
- `SYS-849` — Return true death to a checkpoint with fractional unbanked loss.
- `SYS-853` — Apply and clear a consecutive-use self-recovery lock.
- `CON-628` — In-place resurrection requires a ready charge and cleared lock.
- `INF-334` — An engaged hostile's breakable stability state is visible.
- `INF-335` — Remaining critical executions required to defeat a protected
  hostile are visible.

## New combinations

- `COMB-0274` — Break stability into sequential executions with charged
  in-place continuation.

## Taxonomy changes

- [`TAXONOMY_CHANGE_056`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_056.md)
  removes carrier-specific grab, consumable-hook, meter-direction and
  architectural-change assumptions from six reused genes.
- [`TAXONOMY_CHANGE_066`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_066.md)
  separates the independently visible hostile-stability state from the
  discrete remaining-critical-execution count.
- [`TAXONOMY_CHANGE_067`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_067.md)
  separates the charged recovery settlement, earned charge and post-use lock
  lifecycle, reusing lower-ID owners where they transfer.

## New questions

1. Does another multi-execution boss preserve enough state between criticals
   to reuse `SYS-847` without importing a phase-change gene?
2. Which later stealth route can evidence awareness UI strongly enough to test
   the current rejection of `INF-298`?

## Next recommended game

- No further game is authorised inside Batch 017. Run the recorded full
  taxonomy audit after this game unit and its stop window.

## Why this game

Sekiro tests whether the Atlas can distinguish several superficially similar
action-RPG loops. Its bounded opening is not another stamina-and-death-mark
signature: health changes recovery of a separate Posture state, critical
openings consume visible execution requirements, and lethal defeat branches
through a player-priced in-place recovery before checkpoint loss. Those rules
create reusable boundaries while the named warrior, boss, region, currency and
interface art remain parameters.
