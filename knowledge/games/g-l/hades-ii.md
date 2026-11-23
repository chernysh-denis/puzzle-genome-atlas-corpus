---
game_id: GAME-0532
slug: hades-ii
game_title: Hades II
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-190
    - ACT-341
    - ACT-356
    - ACT-728
  system:
    - SYS-215
    - SYS-362
    - SYS-456
    - SYS-578
    - SYS-1534
    - SYS-1535
    - SYS-1536
    - SYS-1537
    - SYS-1538
    - SYS-1539
  constraint:
    - CON-269
    - CON-402
  information:
    - INF-119
    - INF-142
    - INF-179
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Hades II

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Life thresholds, costs, ranges and attack timings parameterise each rule.

## Analysis scope

- Version / ruleset: English digital Hades II — Nintendo Switch 2 Edition,
  standard single-player v1.0 launch rules (25 September 2025). This is
  the native Switch 2 edition. The exact console executable revision
  and frame timings were not observed.
- Structured analysis target: PLAT-NINTENDO-SWITCH-2, unmodified,
  God Mode off and no Oath of the Unseen or Fear. Use the starting
  Witch's Staff in its default aspect, without a Familiar, an Arcana
  loadout or a purchased Keepsake. The preceding rooms provide a
  reachable entry state. Boons offered there can vary. Weapon and Cast
  observations refer to their base forms, without an optional modifier
  that changes the interaction being tested or supplies Magick in battle.
- Primary decision loop: read Hecate's tells, current Life and Magick,
  move or dash into a safe position, and choose between short ordinary
  actions and a channeled Omega move. Shift to the summoned witches while
  Hecate's shield is up. Identify the real target during the split.
  Evade the homing curse or move defensively until the usual moves return.
- Entry: after reaching Hecate's authored arena through Erebus, start at
  the first controllable combat state of the standard guardian encounter.
  Positive exit: defeat Hecate, collect the resulting Cinder and take the
  onward passage into Oceanus. Stop before initiating an Oceanus fight.
  Negative exit: lose all current Life with no revival, ending the attempt.
- Included: local movement, protected Dash, Sprint, ordinary staff Attack
  and Special, base Cast and channeled Omega forms, the shared Magick budget,
  combat Life, Hecate's moving danger ring, shield intervals, hostile
  witches, decoys and tracking curse, the Cinder reward and passage.
- Excluded: decision paths and acquisition in earlier rooms, the Crossroads,
  later combat and repeated clears, other weapons and Aspects, Hexes,
  boon offers and build composition, Familiars or revivals that intercept
  the scoped transitions, difficulty variants, other platforms and mods.
- Direct-play status: no console or executable was run. The developer
  and platform holder establish the edition and release. Release-era
  written play reports, the published changes and written rules accounts
  establish the bounded fight. Media were not played. No console
  frame counts or exact damage, cost or curse duration are asserted.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| HD2-001 | Supergiant's completed v1.0 shipped digitally on native Nintendo Switch 2 on 25 September 2025. The standard game supports one local player and English text. | Confirmed | Direct | High | P1, P2 |
| HD2-002 | The initial Witch's Staff has ordinary melee Attack and projectile Special. Pressing the relevant move control briefly gives its ordinary use; holding channels the corresponding Omega form. Eligible Omega uses draw on Melinoë's shared Magick budget. | Observation | Corroborated | High | P3, S1, S2, S3 |
| HD2-003 | A base Cast lays a circular field that restrains susceptible foes. The channeled base form can add delayed damage. It does not substitute for defeating the witches that maintain Hecate's shield. | Observation | Corroborated | High | S1, S2, S3, S4 |
| HD2-004 | Melinoë can move, dash through eligible attacks during protected movement and hold into a sustained Sprint. Hecate opens with an expanding ring; observed later attacks include repeated arcs and an expanding and retracting ring. | Observation | Corroborated | High | S1, S2, S4, S5 |
| HD2-005 | At two health breaks Hecate shields herself and calls hostile witches. Attacking the warded guardian does not lower her Life. Defeating the required witches ends the shield interval. | Observation | Corroborated | High | S4, S5, S6 |
| HD2-006 | Hecate can present three attacking forms. The copies still threaten Melinoë but do not count as damage to the guardian. Impact feedback distinguishes a decoy hit from damage to the real one. | Observation | Corroborated | High | P3, S4, S5 |
| HD2-007 | The later shield interval introduces a homing curse. Protected crossings can avoid contact until it expires. If struck, Melinoë temporarily becomes a sheep. She loses normal attacks and can still use limited evasive movement before her normal moves return. | Observation | Corroborated | High | S4, S5, S6 |
| HD2-008 | Life lost in the battle persists unless restored by an eligible effect. With revival excluded, lethal damage ends the attempt. A successful guardian defeat yields a Cinder and unlocks the onward Oceanus route. | Observation | Corroborated | High | P2, S1, S5, S7 |

## Basic data

- Release / origin: Supergiant Games, Nintendo Switch 2 digital launch
  on 25 September 2025; later cartridge distribution does not establish
  an exact installed binary for this study.
- Families: tactical forecast and counterplay, real-time system pressure.
- Sources accessed 2026-11-17:
  - **P1** — [Supergiant's v1.0 release announcement](https://www.supergiantgames.com/blog/hades2-now-available/),
    edition links, release date and completed development.
  - **P2** — [Native Nintendo Switch 2 product listing](https://www.nintendo.com/us/store/products/hades-ii-nintendo-switch-2-edition-switch-2/)
    and [Nintendo's launch bulletin](https://www.nintendo.com/us/whatsnew/battle-beyond-the-underworld-in-hades-ii/),
    for native availability, language, single-player support and modes.
  - **P3** — [Supergiant's published launch notes, archived by SteamDB](https://steamdb.info/patchnotes/20125884/),
    Omega channel indicator, Magick, the normal Total Eclipse tell and
    a separately listed Unrivaled ruleset. PC patch details are used to
    corroborate shared mechanics, not as a Switch 2 executable identity.
  - **S1** — [TechRadar's launch review on Switch 2](https://www.techradar.com/gaming/hades-2-review),
    for the release platform, resource use, the Cast and progression
    from early Erebus to Oceanus.
  - **S2** — [GamesRadar's release review](https://www.gamesradar.com/games/roguelike/hades-2-review-2025/),
    ordinary and Omega approaches and the restraining Cast.
    [Shacknews's release-day controls](https://www.shacknews.com/article/146103/hades-2-controls-pc-keybindings)
    corroborate tap and hold, without establishing Switch labels.
    [GameSpot's Cast reference](https://www.gamespot.com/gallery/hades-2-tips-beginners-guide/2900-5371/)
    documents the delayed burst. It predates v1.0, so only the compatible
    Cast behaviour is used. [Nintendo Insider's Switch 2 play account](https://www.nintendo-insider.com/hades-ii-nintendo-switch-2-edition-review/)
    corroborates holding Dash for Sprint on this platform.
  - **S3** — [Witch's Staff written reference](https://hades.wiki.gg/wiki/Hades_2%3AWitch%27s_Staff)
    and [a comparative rules study](https://uu.diva-portal.org/smash/get/diva2%3A1972814/FULLTEXT01.pdf),
    for the staff and shared Magick model. The study predates launch;
    launch evidence is required for any rule admitted from it.
  - **S4** — [Dave Irwin's release-day guardian guide](https://www.pcgamesn.com/hades-2/hecate),
    for the opening wave, threshold shields, summoned witches, splits,
    ring travel, and both outcomes of the homing curse.
  - **S5** — [GamesRadar's written fight account](https://www.gamesradar.com/hades-2-hecate-boss-fight/)
    and [Prima's written Erebus route](https://primagames.com/GAMING/HADES-2-EREBUS-GUIDE-BEST-TIPS-AND-HOW-TO-BEAT-HECATE),
    used where the release-day sources confirm the same behaviour.
  - **S6** — [Release-period player reports about the curse](https://www.reddit.com/r/Hades2/comments/1nrc1oy/)
    and [the shield and add intervals](https://www.reddit.com/r/Hades2/comments/1nwgkd8/),
    useful for corroborating the movement-dependent evasion path.
  - **S7** — [Shacknews's v1.0 release-day Cinder report](https://www.shacknews.com/article/146104/farm-cinder-hades-2)
    and [GameSpot's release-era resource list](https://www.gamespot.com/gallery/hades-2-best-arcana-cards-guide/2900-5383/).
    Both associate the reward with defeat of the Erebus guardian.
- Claim IDs: HD2-001–HD2-008.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: move between the guardian, summoned witches and safe
  regions. Sprint extends unprotected movement after an allowed Dash.
- Reuse `ACT-161`: direct a basic staff strike or shot toward a hostile
  in the chosen attack geometry.
- Reuse `ACT-190`: invoke the chosen staff or Cast capability.
- Reuse `ACT-341`: collect the Cinder from the settled guardian encounter
  and use the newly available onward route.
- Reuse `ACT-356`: commit a freely timed directional dodge against the
  current danger boundary.
- New `ACT-728`: use the ordinary form with a short input, or hold the
  same command to prepare and release its powered form.
- Claim IDs: HD2-002–HD2-004, HD2-007, HD2-008.

### System Behaviour Genes

- Reuse `SYS-215`: attacks, defence and overlap resolve immediately in
  the shared space while both sides can act.
- Reuse `SYS-362`: clearing the guardian produces the declared Cinder.
- Reuse `SYS-456`: a correctly timed protected Dash can cross a moving
  damaging edge or pass through the incoming curse without being hit.
- Reuse `SYS-578`: Life damage in the fight accumulates on the carried
  resource and lethal loss without revival ends the attempt.
- New `SYS-1534`: a temporary Cast field restrains eligible hostiles in
  its footprint. Its powered form can deliver damage at a later event.
- New `SYS-1535`: crossing a boss Life threshold makes the boss
  invulnerable, summons a required hostile set and defers boss damage
  until that set has been cleared.
- New `SYS-1536`: some attacking copies impersonate the guardian without
  forwarding a hit to its Life. Ordinary damage can resume on the
  real target while copies attack.
- New `SYS-1537`: a pursuing curse that lands temporarily replaces the
  player's moves with a restricted evasive set. If successfully evaded
  until expiry, no transformation happens.
- New `SYS-1538`: multiple independent Omega moves spend one local
  Magick stock. After spending on one, reassess whether another is
  affordable while continuing to use ordinary attacks.
- New `SYS-1539`: a concentric damaging front moves relative to its
  origin. A return wave can cross the same safe-after-passage position.
- Claim IDs: HD2-002–HD2-008.

### Constraint Genes

- Reuse `CON-269`: a powered move needs sufficient Magick and a valid
  ability state. Normal staff commands must also be available in the
  current player state.
- Reuse `CON-402`: the onward exit stays unavailable while the required
  encounter is unresolved.
- Claim IDs: HD2-002, HD2-005, HD2-007, HD2-008.

### Information Genes

- Reuse `INF-119`: read remaining Life, Magick and channel progress before
  committing to another powered move.
- Reuse `INF-142`: Hecate's animation and attack previews cue a moving
  danger boundary or a safe time to begin an action.
- Reuse `INF-179`: the room shows the actor positions, telegraphs, ward
  and reward. Guardian Life and hit feedback distinguish a genuine
  damage opportunity from a decoy or an invulnerable interval.
- Claim IDs: HD2-002, HD2-004–HD2-008.

### Objective Genes

- Reuse `OBJ-080`: defeat the guardian, collect her reward and cross
  the opened threshold toward Oceanus.
- Claim IDs: HD2-005, HD2-008.

### Time Genes

- Reuse `TIM-003`: projectiles travel, channeling consumes time and
  vulnerability conditions continue changing during live input.
- Claim IDs: HD2-002–HD2-007.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| The guardian opens with an expanding ring | Move back in after its edge passes or Dash through the edge during protection | The moving edge defines the crossing window. On a later returning pattern it can pass the same position again. | A moving perimeter is different from instant damage throughout a filled disk. | HD2-004 |
| A reachable target and sufficient Magick | Use the ordinary Attack or Special, then channel an Omega variation in an opening | The brief action remains available without paying the channel's Magick cost. Spending on one Omega reduces what is available for another. | One input decision and one shared budget impose different constraints. | HD2-002 |
| Susceptible summoned foes approach | Place a Cast field, using Omega if affordable and safe | The ordinary field impedes a foe's movement. The base powered Cast can add delayed damage. Keep fighting until required hostile clearance. | Control alone does not clear the ward. | HD2-003, HD2-005 |
| Hecate reaches a warding health break | Attempt a hit on the shield, then eliminate the witches she calls | The guardian rejects damage during the ward. The last required witch's defeat restores access to damage. | The boss's invulnerability has a hostile-set exit predicate. | HD2-005 |
| Three attacking forms are present | Strike a copy and compare hit feedback with a strike on the real form | A copy has an attack but no contribution to damage on the guardian. | Apparent threat and valid target can differ. | HD2-006 |
| The later ward starts with a pursuing curse | Repeatedly Dash through its trajectory, or let it hit in a separate observation | Evading until expiry leaves the normal moves available. Contact temporarily removes the usual attacks while limited movement remains. | Spell pursuit and loss of capabilities are separate from ordinary Life damage. | HD2-007 |
| Hecate has been defeated | Take the Cinder and the following route | The collected reward and Oceanus access settle the successful encounter. | It is a regional guardian crossing, not a complete escape run. | HD2-008 |

## Strategic and experiential structure

Ordinary actions preserve the budget and limit commitment. A player with a
safe approach can spend Magick for a powered action instead. Once the ward
appears the most damaging blow on the wrong body cannot advance boss Life.
Focus moves to the required witches, and later the homing curse can make a
short defensive pause more useful than trying another attack. After the
ward, an attacking copy can still make the route dangerous even though
only the real form can suffer the needed damage.

## Replay and variation

- The arena and required guardian are authored. Timing, current Life
  and Magick, choice of spell, and earlier eligible rewards vary.
- Compare empty and affordable Magick states, a decoy and genuine hit,
  and curse evasion versus contact. A hit on the decoy is distinct from
  an attack rejected by the ward.
- Do not substitute a later Oath variant or take an exact threshold,
  frame count or ally-interception rule from an optional configuration.
- Claim IDs: HD2-002–HD2-008.

## Adjacent systems and history

- The release describes Unrivaled Hecate separately. That variant and
  launch-to-later patch differences are outside the packet.
- The original Hades has reusable Cast ammunition and a complete
  escape-attempt scope in GAME-0251. Hades II's shared budget and this
  single guardian settlement are different decision boundaries.
- Claim IDs: HD2-001–HD2-008.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-341`, `ACT-356`, `ACT-728` | locomotion, hostile aim, ability, reward interaction, dodge, channel choice |
| System Behaviour | `SYS-215`, `SYS-362`, `SYS-456`, `SYS-578`, `SYS-1534`, `SYS-1535`, `SYS-1536`, `SYS-1537`, `SYS-1538`, `SYS-1539` | combat, reward, protection, Life, field, ward, copies, curse, Magick and wavefront |
| Constraint | `CON-269`, `CON-402` | affordability and required guardian clearance |
| Information | `INF-119`, `INF-142`, `INF-179` | resources, wind-up and room-state cues |
| Objective | `OBJ-080` | cleared guardian and onward crossing |
| Time | `TIM-003` | live pursuit, attack timing and channel time |

Canonical signature:

`ACT-008,ACT-161,ACT-190,ACT-341,ACT-356,ACT-728; SYS-215,SYS-362,SYS-456,SYS-578,SYS-1534,SYS-1535,SYS-1536,SYS-1537,SYS-1538,SYS-1539; CON-269,CON-402; INF-119,INF-142,INF-179; OBJ-080; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `531` (`GAME-0001`–`GAME-0531`).
- Exact genome matches: none.
- Tied near matches: `GAME-0251` — Hades (`13 / 40 = 0.325000`).
- Supported combination subsets: none.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0251` — Hades | `ACT-008`, `ACT-161`, `ACT-190`, `ACT-356`, `CON-269`, `CON-402`, `INF-119`, `INF-179`, `SYS-215`, `SYS-362`, `SYS-456`, `SYS-578`, `TIM-003` | Both reward reading combat cues, positioning and timing a protected dodge. Hades uses reusable Cast ammunition over a complete escape attempt. The scoped Hades II duel shares one budget across channeled moves and distinguishes required witches from attacking copies before one regional crossing. | Tied near (`0.325000`) |

### Preserved research notes

- New genes: `ACT-728`, `SYS-1534`–`SYS-1539`.
- Classification result: `New gene`.
- Evidence and reasoning: the hold action selects a move form, while
  a separate shared budget couples their availability. The ward
  changes what may take damage. The doubles change what counts as
  a hit on the correct target.

## Taxonomy impact

- Registry changes: seven Active additions and sixteen transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_279](../../../research/taxonomy-changes/TAXONOMY_CHANGE_279.md).

## Negative results

- Ordinary Cast does not supply evidence that Hecate herself can be
  immobilised. Limit the restraint to eligible targets.
- A temporarily changed avatar need not acquire a separate health pool
  or be chosen by the player.
- A successful protected crossing avoids the curse; it does not prove
  a familiar-independent reflecting or destroying action.

## Delta summary

## New facts

- [Observation | Corroborated | High] In the guardian duel, the shield
  requires defeating the summoned witches. During the split, attacking
  the actual guardian matters even though the copies also attack.

## New genes

- [Observation | Corroborated | High] Seven additions in
  `TAXONOMY_CHANGE_279`.

## New combinations

- [Observation | Corroborated | High] No new combination proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_279`.

## New questions

- Which exact channel interruptions spend Magick on the native launch
  build, and which attacks preserve the base Cast's movement restraint?

## Next recommended game

- [Hypothesis | Limited | Medium] Examine the original English Nintendo DS
  Ghost Trick: Phantom Detective in the opening timed rescue packet
  selected in Selection 042.
