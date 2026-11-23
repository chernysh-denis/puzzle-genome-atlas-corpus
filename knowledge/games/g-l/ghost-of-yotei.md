---
game_id: GAME-0550
slug: ghost-of-yotei
game_title: Ghost of Yōtei
analysis_status: reviewed
reviewed: 2026-11-19
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-437
  system:
    - SYS-215
  constraint: []
  information:
    - INF-119
    - INF-235
    - INF-318
  objective:
    - OBJ-029
  time:
    - TIM-003
---

# Game: Ghost of Yōtei

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
A cinematic memory is presentation, not a player-controlled rewind. The
opening teaching encounter is not a sample of the entire unlocked arsenal.

## Analysis scope

- Version / ruleset: original English PS5 full campaign release, issued
  2 October 2025, ordinary New Game. This is the release-era opening,
  not a prerelease preview, Legends, Most Wanted or a later expansion.
  No installed executable, semantic patch, disc identifier or checksum was
  authenticated; the historical campaign packet is not assigned to a current
  Complete Edition binary merely because the live product page now sells it.
- Structured analysis target: `PLAT-PLAYSTATION-5`, original single-player campaign.
  Prescribe Medium difficulty and ordinary inputs with assists unchanged;
  the exact difficulty and accessibility configuration of the public capture
  remain unknown, so no damage coefficient or native timing is measured.
- Entry: after the opening town fights and introduction cinematic, accept
  ordinary player control in the first duel against the Snake beside the
  burning inn. The preceding inscription and outlaw encounters are setup,
  not additional objectives in this packet.
- Primary decision loop: read the opponent's distance, sword motion, own
  condition and named health bar; move within the encounter, hold the katana
  block through an incoming sequence, release it and commit light cuts in
  the ensuing opening. Repeat through the authored interruptions until the
  Snake is defeated. The designer explicitly bounds the tutorial to block
  and light attack; a guide's broader heavy/parry/dodge vocabulary is not
  imported as an independently verified opening command set.
- Positive exit: finish the Snake encounter and accept its closing story
  sequence through the handoff to horseback travel. Stop before scouting,
  returning home, shamisen, forging or training with Jubei. Removing one
  target is not completion of the six-target revenge campaign.
- Failure qualification: hostile hits visibly lower player condition, but
  this packet does not establish an ordinary zero-health death screen,
  a checkpoint reset, stock loss or a native inability to die. Scripted
  apparent defeat and subsequent recovery are story events, not evidence of
  a freely usable resurrection skill. A forced restart of New Game can
  reproduce entry; save/reload parity is untested.
- Included: local positioning, single-katana light attack and held block,
  live sword exchange, own condition, named opponent health, local attack
  motion, the finite encounter goal and authored story interruptions.
- Excluded: stealth, street sword pickup/throw, independently unlocked weapon
  switching, heavy attacks as a certified tutorial requirement, Focus attacks,
  perfect-parry grades, dodge immunity windows, Spirit-priced healing,
  player-called wolf assistance, gear/charm progression, open-world selection,
  later bosses, Jubei training, Lethal, online modes, DLC and save persistence.
  Separate packets could examine a later ordinary duel, a weapon-counter
  lesson, a bounty, or the fully evidenced Spirit economy.
- Direct-play status: no PS5, executable, local save or native input session
  was used. The combat designer's published slides and official product and
  accessibility pages were read. Eleven public storyboard sheets for a
  released first-boss capture were inspected at five-second sampling without
  audio/video playback, foreground windows or fullscreen. Those stills show
  a route, not exact timing, an authenticated patch or hidden state.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| GY-001 | The PS5 game launched as a full release on 2 October 2025; this packet targets its original campaign opening. | Confirmed | Direct | High | P1 |
| GY-002 | The lead combat designer describes the Snake as a katana-only block/light-attack tutorial with authored spectacle and a disarm introduction. That design description does not certify every later combat mechanic in this opening. | Observation | Direct | High | P2 pp. 60–62 |
| GY-003 | The live interval permits local positioning and close strikes, shows an explicit block prompt and exchanges hostile sword attacks. | Observation | Corroborated | High | P2, R1 1:15–4:25, S1, S2 |
| GY-004 | A named opponent bar, own condition and visible local sword motions expose current progress and danger. | Observation | Direct | High | R1 1:15–4:25 |
| GY-005 | The duel includes authored interruptions before its defeat sequence and horseback successor; these do not establish a freely selected rewind, resurrection or commandable wolf. | Observation | Corroborated | High | P2, R1 1:50–3:00 and 4:25–7:20, S1 |
| GY-006 | Heavy, perfect-parry, dodge, healing and zero-health retry rules are not independently certified for this tutorial by the inspected evidence. Some written guides mix opening and later training. | Observation | Conflicting | Medium | P2, S1, S2, R1; coarse stills do not measure hidden options |

## Basic data

- Release / origin: Sucker Punch Productions / Sony Interactive Entertainment,
  full PS5 release, 2 October 2025.
- Platform or physical form: prescribed original PS5 campaign with DualSense;
  no purchase, device ownership or successful native execution is claimed.
- Puzzle family: `FAM-010`, live system pressure; choosing a defensive hold
  and attack opportunity occurs while the opponent continues to act.
- Primary sources, checked 2026-11-19:
  - **P1** [SIE launch announcement](https://sonyinteractive.com/en/press-releases/2025/journey-across-the-northern-edge-of-17th-century-japan-in-ghost-of-yotei-out-now-on-playstation-5/):
    released product, developer, publisher and target platform.
  - **P2** [Theodore Fishman, Honing the Blade: Evolving Combat for Ghost of Yōtei](https://media.gdcvault.com/gdc2026/Slides/Fishman_Theodore_honing_the_blade_evolving_combat_for_ghost_of_yotei.pdf),
    GDC 2026, lead combat designer. Pages 60–62 specifically describe the Snake;
    the earlier disarm and weapon slides distinguish abandoned prototypes from
    shipped choices. Stamina-based random disarming was cut, not a release fact.
  - **P3** [Official characters and combat](https://www.playstation.com/en-us/games/ghost-of-yotei/characters-and-combat/):
    the Snake's katana role and the broader unlockable arsenal; those later
    weapon counters are not automatically present at entry.
  - **P4** [Official accessibility options](https://www.playstation.com/en-us/games/ghost-of-yotei/accessibility-options/):
    cue and input options exist. Their exact captured values are not inferred.
- Visual evidence:
  - **R1** [Published first-boss PS5 capture](https://www.youtube.com/watch?v=wIXIs0mRKT4),
    7:36. Inspected 93 public storyboard cells on eleven sheets, at five-second
    steps. The duel is live by 1:15; held-block prompts and named health are
    visible around 1:30–1:45; a memory-styled interruption occurs around 1:50;
    combat resumes before 2:40. Later exchange continues to around 4:20;
    the defeat/story sequence follows and horseback handoff appears around
    7:00. These are coarse locators, not measured hit windows or exact triggers.
- Secondary sources:
  - **S1** [PowerPyx prologue route](https://www.powerpyx.com/ghost-of-yotei-prologue-walkthrough/),
    1 October 2025, separates the initial boss, horseback travel and home
    training. Its heavy-attack advice is not promoted over P2's bounded design
    description; its later healing lesson is not imported into the Snake.
  - **S2** [Neoseeker prologue route](https://www.neoseeker.com/ghost-of-yotei/Prologue),
    search-rendered boss paragraph corroborates holding block and responding
    after attacks. Direct retrieval was blocked; no unseen page was reviewed.
    The expanded control list remains qualified under GY-006.
- Claim IDs: GY-001–GY-006.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for immediate local movement and spacing, `ACT-161` for
  the currently equipped katana's reachable light cuts and `ACT-437` for a
  held facing-relative block. There is no demonstrated separately exhaustible
  player guard meter, so `ACT-383` is not substituted merely because a sword
  provides the protective equipment.
- A timed parry, a player-selected lock-on, a generic dodge and a charged
  heavy strike are not added from the full game's control list.
- Claim IDs: GY-002, GY-003, GY-006.

### System Behaviour Genes

- Reuse `SYS-215` for the live range, cadence, defence and damage exchange.
  The held block prevents eligible incoming contact from becoming ordinary
  damage; release creates the next attack opportunity.
- The cinematic memory, gun/wolf reversal and final handoff locate the
  authored encounter; their spectacle alone creates no new gene. No
  `SYS-799` health-gated replacement attack set is certified, and no player
  resurrection, automatic combat-earned Spirit award or ordinary checkpoint
  return is inferred from the story sequence.
- Claim IDs: GY-002–GY-006.

### Constraint Genes

- No separately admitted Constraint gene. The narrow tutorial repertoire is
  a versioned scope parameter, not an invented global inventory law. Attack
  reach and block eligibility are parameters of the accepted action/system
  boundaries. No zero-vitality terminal or shared exertion price is certified
  in this exact tutorial.
- Claim IDs: GY-002, GY-006.

### Information Genes

- Reuse `INF-235` for the local combat field and sword motion, `INF-119` for
  own visible condition and `INF-318` for the named Snake health bar.
  Motion can help time a block without exposing the next exact command.
- No typed red/gold/white response map is inferred from later encounters;
  `INF-319` requires a locally evidenced response-category distinction.
- Claim IDs: GY-003, GY-004, GY-006.

### Objective Genes

- Reuse `OBJ-029` for defeating the one required hostile in this bounded
  encounter. One damaging contact or a cinematic apparent reversal is not
  the positive terminal. The completed story handoff delimits acceptance.
- Claim IDs: GY-003, GY-005.

### Time Genes

- Reuse `TIM-003` for live input between scripted interruptions. A cinematic
  pause is a noninteractive boundary, not a player-authored time-rewind
  operation, stopped planning mode or fixed action-point turn.
- Exact frame windows, animation recovery and difficulty coefficients remain
  unmeasured. Story sampling cannot establish them.
- Claim IDs: GY-002–GY-006.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Both swordsmen retain ordinary live control | Move within the local combat space | Change relative reach and next attack opportunity | Immediate movement differs from a remote travel command | GY-003 |
| An ordinary incoming sword sequence approaches | Hold the prompted block | Intercept eligible sword contact instead of leaving it wholly unguarded | Sustained defence differs from a precise parry window | GY-002, GY-003 |
| A blocked sequence leaves a close opening | Release block and request light cuts | Reachable hits reduce the opponent's remaining condition | The action and its damage result are different layers | GY-003, GY-004 |
| An attack is out of effective reach | Commit the same light cut | A valid attack request alone does not guarantee a damaging contact | Local spacing matters without a turn grid | GY-003 |
| An authored story interruption begins | Allow that sequence to settle | Ordinary combat input gives way to the staged scene before the encounter continues | No freely selected rewind or resurrection is demonstrated | GY-005 |
| The named opponent still has combat remaining | Resume live exchanges after interruption | Continue the bounded encounter rather than award an early clear | Spectacle does not replace the actual terminal | GY-004, GY-005 |
| The Snake's final encounter settlement is reached | Accept the closing scene | Hand off to horseback travel | The one-boss packet ends before open-world scouting | GY-005 |

These are documentary transition checks, not a claimed PS5 input session.
The exact trigger thresholds and failed native branches remain unmeasured.

## Strategic and experiential structure

Defensive patience trades immediate damage for a safer opening. Moving
changes reach; holding the guard through a sequence differs from releasing
it too soon to attack. The taught repetition is deliberately smaller than
the complete game's unlockable combat repertoire. A dramatic interruption
can temporarily obscure accumulated progress without becoming a new
player-controlled state-restoration tool. GY-002–GY-006 bound these observations.

## Replay and variation

The opponent and staged succession are authored. Player timing, spacing,
number of hits and duration can vary; no procedural boss generation is
claimed. Changing difficulty, assistants or unlocked equipment would require
separate parameter evidence. Exact zero-health and save restoration remain
open questions rather than asserted replay guarantees. Claim IDs: GY-003–GY-006.

## Adjacent systems and history

The official game places Atsu centuries after Ghost of Tsushima and replaces
its full arsenal progression with a different weapon repertoire. Shared
presentation does not prove identical guard costs or every predecessor's
stance, Spirit and parry rule. The lead designer's abandoned stamina and
random-disarm experiments are historical prototypes, not this release's
mechanical facts. The Snake is first; later free target choice is excluded.
Claim IDs: GY-001, GY-002, GY-006.

## Normalised genome

| Type | Active genes | Scoped role |
| --- | --- | --- |
| Action | `ACT-008`, `ACT-161`, `ACT-437` | Move, cut and hold block |
| System Behaviour | `SYS-215` | Resolve live sword exchange |
| Constraint | none | No independently certified additional restriction |
| Information | `INF-119`, `INF-235`, `INF-318` | Own condition, local field and boss health |
| Objective | `OBJ-029` | Defeat the required opponent |
| Time | `TIM-003` | Live combat between authored interruptions |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `549` (`GAME-0001`–`GAME-0549`).
- Exact genome matches: none.
- Tied near matches: `GAME-0277` — Cuphead (`6 / 17 = 0.352941`); `GAME-0427` — Alan Wake (`6 / 17 = 0.352941`).
- Supported combination subsets: none.
- Scan date: 2026-11-19.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0277` — Cuphead | `ACT-008`, `ACT-161`, `INF-119`, `OBJ-029`, `SYS-215`, `TIM-003` | Both directly move, aim attacks and resolve live combat with visible personal condition and a finite hostile objective. Cuphead adds dash, timed evasion/parry, typed pink targets, sequential boss phases and graded results; this Snake packet teaches held sword block with a named guardian bar and no admitted score or parry grade. | Near, `0.352941` |
| `GAME-0427` — Alan Wake | `ACT-008`, `ACT-161`, `INF-119`, `OBJ-029`, `SYS-215`, `TIM-003` | Both directly move, aim attacks and resolve live combat with visible personal condition and a finite hostile objective. Alan Wake must strip darkness using a charge-limited flashlight before revolver damage; this Snake packet uses held sword block and light cuts, without inherited flashlight, battery or reload rules. | Near, `0.352941` |

### Preserved research notes

- New genes: none.
- Classification result: New combination of known genes.
- Evidence and reasoning: the bounded tutorial transfers existing movement,
  held guard, direct damage and visible-condition boundaries. A cinematic
  interlude or a famous character supplies no new mechanical definition.

## Taxonomy impact

- Nine Active definitions are reused unchanged; no definition is added.
- Registry changes: none.
- Taxonomy-change record: none.
- Candidate terms affected: none.

## Negative results

- none. Scope exclusions and unresolved claims above are not registry decisions.

## Delta summary

## New facts

- [Observation | Direct | High] The designer bounds the first Snake tutorial
  to katana blocking and light attacks; later arsenal rules are not admitted.
- [Observation | Corroborated | High] The complete duel includes staged story
  interruptions before its closing horseback handoff.

## New genes

- [Observation | Corroborated | High] No new genes.

## New combinations

- [Observation | Corroborated | High] No new recurring combination is proposed.

## Taxonomy changes

- [Observation | Direct | High] No taxonomy changes.

## New questions

- Which expanded inputs are actually enabled in an authenticated launch build's
  Snake tutorial, as distinct from the following home lesson?
- What are its native zero-health and checkpoint rules on the prescribed preset?

## Next recommended game

- [Hypothesis | Limited | Medium] Ridge Racer Type 4, `GAME-0551`, from
  [Selection 044](../../../research/selection/SEARCH_DEMAND_GAME_SELECTION_044.md).
- Optimisation criterion: alternate era, platform, genre and input problem.
- Expected information gain: compare drift and racing qualification with live melee.
- Backlog impact: eight approved subjects remain; no push or publication.

## Why this game

- [Hypothesis | Limited | Medium] A recognisable modern PS5 release tests
  whether an intentionally restricted tutorial can reuse stable mechanics
  without importing a whole open-world game's systems or inflating taxonomy.
