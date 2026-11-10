---
game_id: GAME-0463
slug: pokemon-gold-version
game_title: "Pokémon Gold Version"
analysis_status: reviewed
reviewed: 2026-10-01
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-019
    - ACT-089
    - ACT-130
    - ACT-194
    - ACT-199
    - ACT-258
  system:
    - SYS-004
    - SYS-299
    - SYS-307
    - SYS-362
    - SYS-854
    - SYS-921
    - SYS-954
    - SYS-955
    - SYS-956
    - SYS-957
    - SYS-1213
  constraint:
    - CON-210
    - CON-276
    - CON-277
    - CON-282
    - CON-384
    - CON-656
  information:
    - INF-123
    - INF-363
  objective:
    - OBJ-197
  time:
    - TIM-001
    - TIM-025
---

# Game: Pokémon Gold Version

Use the canonical [vocabulary and comparison rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Cyndaquil, Hoothoot, Route 29, Berry, Falkner and ZephyrBadge are carrier parameters, not new gene names.

## Analysis scope

- Version / ruleset: original North American English Pokémon Gold Version Game Boy Color cartridge. The pinned `pret/pokegold` source documents an exact Gold UE build with SHA-1 `d8b8a3600a465308c9953dfa04f0081c05bdcb94`. No cartridge, ROM or emulator was obtained or played; code and the contemporary manual are the evidence. This is not Silver, Crystal, HeartGold, a Virtual Console wrapper or a modern remake.
- Structured analysis target: `PLAT-GAME-BOY-COLOR` in [platform coverage](../../platforms/games.json), original cartridge rules through the first Violet Gym badge. No later platform's clock, trade or save-state behavior is inherited.
- Entry: first ordinary control after the opening choice of Cyndaquil, return of the Mystery Egg to Professor Elm and the aide's five Poké Balls. The single living Cyndaquil is the party; no badge is held. Those opening gates are fixed entry context, not actions newly played inside this packet. The Game Boy Color clock has been set to the local time at the start of the save.
- Reproducible route: during a night interval (18:00–03:59 in the pinned clock code), walk Route 29 grass until its eligible wild table produces Hoothoot, weaken it, spend a Ball and repeat if necessary until one capture succeeds. An ordinary Route 29 fruit tree supplies a Berry; assign one to Cyndaquil as its held item. Make one voluntary switch between the two owned party members during a later eligible battle. Heal at a reachable Pokémon Center, traverse the authored Route 29–31/Cherrygrove/Violet route, defeat Falkner's complete Gym party and retain ZephyrBadge. Extra wild samples, damage rolls, Balls and exact step counts are variable; this is a bounded analytic route, not a guaranteed one-try transcript.
- Primary decision loop: take eligible terrain steps, observe the current clock phase and battle surface, choose a legal move, party switch, item or escape, manage persistent HP, status, move PP, Balls, held Berry and money; convert wild capture and battle rewards into a viable party; recover at a Center and commit the fixed Gym battle.
- Positive terminal: after Falkner's level-7 Pidgey and level-9 Pidgeotto are defeated, his script sets `EVENT_BEAT_FALKNER` and `ENGINE_ZEPHYRBADGE`; stop when ordinary control returns with the badge retained. TM31 is offered subsequently and is not required for badge credit.
- Failure/recovery: ordinary all-party faint heals the party, halves current money and returns the Trainer to the last healing spawn. It is not the positive terminal. Failed encounter/capture attempts can be retried with sufficient legal supply; no exact success probability or finite worst-case number of samples is promised.
- Included: route movement and grass checks; cartridge-clock morning/day/night selection; Route 29's night-specific Hoothoot/Rattata slots; weighted wild species/level and random battle outcomes; two-member retained party and voluntary switching; FIGHT/PKMN/PACK/RUN, priority/Speed order, type/damage/status, PP, capture, experience/level and Center healing; one Route 29 Berry pickup, held-item assignment and its automatic once-only below-half-HP heal; authored first-Gym gate, fixed Falkner party and badge settlement.
- Excluded: choosing the starter, Elm's egg delivery and the aide handoff as played events; the optional catching tutorial, weekday gifts, Sprout Tower, other Johto/Kanto Gyms, rival detours, full Pokédex, exhaustive collection, breeding, trading, link battles, later evolution, all later badge rules, clock manipulation, glitches, cheats, ROM hacks, other language/region cartridges and ports. These exclusions do not say such content is absent from the product.
- Direct-play status: not conducted. No original cartridge, ROM, emulator, input trace, save, screenshot, video or audio was obtained or inspected. The manual and exact-build source support a documentary transition reconstruction, not a claim of successful first-hand play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PKG-001` | The chosen target is the original English Game Boy Color Gold build, not another generation or wrapper | Confirmed | Direct | High | P1, P2, R1 |
| `PKG-002` | The post-egg opening gives five Balls and permits ordinary Route 29 travel | Confirmed | Direct | High | P2, R1 |
| `PKG-003` | The cartridge clock selects morning/day/night; Route 29 night slots include Hoothoot but its next encounter is not guaranteed | Confirmed | Direct | High | P2, R1 |
| `PKG-004` | Grass checks sample eligible local wild slots before a bounded battle; FIGHT, PKMN, PACK and RUN consume ordered turns | Confirmed | Direct | High | P2, R1 |
| `PKG-005` | Balls sample catch eligibility and HP/status-dependent success; legal party switching retains each member's state | Confirmed | Direct | High | P2, R1 |
| `PKG-006` | A held Berry automatically heals its holder below half HP and is consumed rather than being a manually commanded PACK use | Confirmed | Direct | High | P1, P2, R1 |
| `PKG-007` | Battle rewards/levels persist; a Center restores the party; ordinary blackout heals, halves money and returns to the last spawn | Confirmed | Direct | High | P2, R1 |
| `PKG-008` | Falkner's two fixed birds must fall; the badge flag is set before the optional TM31 offer | Confirmed | Direct | High | P2, R1 |
| `PKG-009` | The admitted 29-gene signature represents this route, not all Pokémon Gold systems | Observation | Direct | High | P1, P2, R1, V1 |

## Basic data

- Release / origin: Game Freak, Nintendo; original Pokémon Gold Version for Game Boy Color. Regional release day is not needed to infer these rules.
- **[P1]** [official Pokémon Gold and Silver overview](https://www.pokemon.com/us/pokemon-video-games/pokemon-gold-version-and-pokemon-silver-version), for original handheld identity, day/night clock and held-item premise; accessed 2026-10-01.
- **[P2]** [original North American Gold manual](https://www.videogamemanual.com/gbc/Pokemon%20-%20Gold%20Version%20%28USA%29.pdf), visually reviewed PDF printed pp. 3, 23, 26–28, 31–32 and 36: setting the clock, held Berry, wild/trainer battle, capture, day/night Hoothoot and first Gym; accessed 2026-10-01.
- **[R1]** [`pret/pokegold` pinned commit `62388c7204e5d13aa05b4231e220b6760584d1b5`](https://github.com/pret/pokegold/tree/62388c7204e5d13aa05b4231e220b6760584d1b5), whose documented Gold UE build matches the stated SHA-1. Route 29 encounters and fruit tree, `GetTimeOfDay`, wild-step sampler, held-Berry handler, party menu, whiteout, Elm's Lab, Violet Gym and Falkner party code close the transitions; accessed 2026-10-01.
- **[V1]** Repository-side source reconstruction. No direct gameplay or audiovisual corroboration is claimed.

## Mechanical decomposition

### Action Genes

- `ACT-008`: move the Trainer across accessible authored route and town tiles.
- `ACT-019`: choose a learned move for the active Pokémon in a bounded battle.
- `ACT-089`: take the addressed Route 29 Berry from its fruit tree into the Bag.
- `ACT-130`: buy an offered refill of Poké Balls if the five entry Balls prove insufficient; this is available but not a forced expenditure.
- `ACT-194`: throw and spend a Ball at a legal wild target.
- `ACT-199`: give a carried Berry to Cyndaquil's held-item slot.
- `ACT-258`: replace the active party member with the other living owned Pokémon.

### System Behaviour Genes

- `SYS-004`: resolve bounded encounter, battle and capture random samples.
- `SYS-299`: convert participant experience into persistent levels and learned moves.
- `SYS-307`: test a wild Pokémon's capture against Ball, HP, status and catch rate, then store success in a free party slot or eligible Box.
- `SYS-362`: grant participant experience and Trainer money after eligible victories.
- `SYS-854`: apply move-type affinity, damage and faint/status transitions.
- `SYS-921`: filter the local wild table by current clock phase and Route 29 habitat; the night Hoothoot slot is eligible, not guaranteed.
- `SYS-954`: on eligible grass movement, test the encounter rate and sample a weighted slot to start one wild battle.
- `SYS-955`: order committed player/opponent commands by class, priority and Speed before resolution.
- `SYS-956`: persist party HP/status/moves/PP and restore the full party at a Center.
- `SYS-957`: resolve all-party faint into healing, half-money loss and return to the last spawn.
- New `SYS-1213`: at the between-turn held-item check, if a living holder's current HP is below half and it holds an ordinary Berry, automatically restore up to the Berry's declared HP amount once and consume that held item. The pinned handler reads current HP, not previous HP or a damage flag; a fresh threshold crossing is not required. A manual PACK command and a reusable regeneration effect are different boundaries.

### Constraint Genes

- `CON-210`: Bag and Berry/Ball stacks obey compatible finite item slots and quantities.
- `CON-276`: a compatible carried Ball and current wild target are required; trainer-owned Pokémon cannot be captured.
- `CON-277`: successful capture enters a free party slot or an eligible Box if party capacity is full.
- `CON-282`: authored Route 29–31, town and Violet Gym access must satisfy prior location/story gates.
- `CON-384`: only one living eligible party member is active; fainting forces replacement or whiteout.
- `CON-656`: a selected move needs PP and legal current status; use spends PP and exhausted selections follow the declared fallback.

### Information Genes

- `INF-123`: party screen reports owned identities, levels, status, HP and moves before switching or held-item planning.
- `INF-363`: battle menus and HUD report active identities, HP/status, command choices and selected move PP/type without revealing the next hidden sample.

### Objective Genes

- `OBJ-197`: defeat the complete first Gym Leader party and retain the badge after the reward script. The parameter here is Falkner/ZephyrBadge, not Brock/BoulderBadge.

### Time Genes

- `TIM-001`: overworld/menu input and ordered battle commands form discrete decision steps.
- `TIM-025`: the cartridge's battery-backed real-world clock continues to set local time-of-day outside active turns; route eligibility changes with the phase. No accelerated or deliberately manipulated clock is assumed.

## Reproducible transitions

| Before | Action / trigger | Bounded resolution | Claim |
|---|---|---|---|
| Elm has accepted the Mystery Egg and the aide gives the starter five Balls | enter ordinary control and travel toward Route 29 | starter and five Balls are retained; badge remains absent | `PKG-002` |
| Cartridge time is 18:00–03:59 and Route 29 grass is eligible | take grass steps | encounter check may fail; success samples the night weighted table with Hoothoot or Rattata, not day-only slots | `PKG-003`, `PKG-004` |
| One wild Hoothoot is active and a Ball remains | weaken, choose PACK and throw | Ball is consumed; catch check may fail or add Hoothoot to party | `PKG-005` |
| Route 29 tree still holds its Berry | interact and give Berry to Cyndaquil | Berry moves from tree to Bag, then to one compatible held-item slot | `PKG-006` |
| Holder has a Berry and takes enough damage to fall below half HP without fainting | complete the damaging action | Berry automatically restores 10 HP up to max and is consumed once; no extra player command | `PKG-006` |
| Cyndaquil and Hoothoot are alive | select PKMN and switch | only one becomes active; both retain their own health, moves and PP | `PKG-005` |
| Party is damaged with a Center reachable | accept nurse service | all eligible party state is restored; the Center becomes the return point | `PKG-007` |
| All owned Pokémon faint during ordinary route or Gym play | settle loss | party heals, current money halves and Trainer returns to last spawn without a badge | `PKG-007` |
| Falkner's level-7 Pidgey and level-9 Pidgeotto are both defeated | complete post-battle dialogue | victory and ZephyrBadge flags are set before optional TM31 offer; return with badge is the positive terminal | `PKG-008` |

## Strategic and experiential structure

- The meaningful difference from original Red's first-badge route is a real-time clock filtering wild eligibility, plus a held Berry whose automatic below-threshold check can protect the starter during the approach. The table still requires random sampling and the Gym still requires explicit command combat.
- The player can read HP, status and PP before spending a move or Ball. A failed Hoothoot search may be wrong phase, no encounter or another sampled night slot; those are different failure causes.

## Replay and variation

- Route and species are fixed for comparability; exact battle rolls, capture tries, clock minute, amount of money and optional refill vary. Alternate starter, day schedule, trading and later Johto systems require separate packets.
- Different night samples and successful captures produce different party levels, health and Ball reserves before the fixed first Gym party.

## Adjacent systems and history

- Original Pokémon Red shares capture, party retention, turn-command battle, Center recovery and first-badge settlement. Gold adds a battery-backed civil clock, clock-filtered wild eligibility and automatically used held items; the similar shape does not make their genomes identical.
- Silver and Crystal change version-specific species availability and/or features and require their own evidence. HeartGold is a remake, not an original Game Boy Color rule source.

## Normalised genome

The front matter is canonical: 29 Active uses (seven Action, eleven System Behaviour, six Constraint, two Information, one Objective, two Time). Species, held item name, route, clock phase and badge remain parameters. One new definition is `SYS-1213`; 28 uses reuse existing IDs.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `462` (`GAME-0001`–`GAME-0462`).
- Exact genome matches: none.
- Tied near matches: `GAME-0336` — Pokémon Red Version (`24 / 30 = 0.800000`).
- Supported combination subsets: none.
- Scan date: 2026-10-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0336` Pokémon Red Version | `ACT-008`, `ACT-019`, `ACT-130`, `ACT-194`, `ACT-258`, `SYS-004`, `SYS-299`, `SYS-307`, `SYS-362`, `SYS-854`, `SYS-954`, `SYS-955`, `SYS-956`, `SYS-957`, `CON-210`, `CON-276`, `CON-277`, `CON-282`, `CON-384`, `CON-656`, `INF-123`, `INF-363`, `OBJ-197`, `TIM-001` | Red's starting packet includes starter selection but has no real-clock wild-table filter, Route 29 Berry pickup, held-item assignment or automatic threshold healing; Gold begins after the starter/egg handoff and stops on Falkner's distinct badge flag | nearest only; `24 / 30 = 0.800000`, not equivalent |

## Taxonomy impact

- `SYS-1213` isolates automatic below-threshold held-item healing. `TAXONOMY_CHANGE_200` generalises `SYS-921` from one wildlife carrier and `TIM-025` from a host clock to the same eligibility and externally advancing civil-time boundaries on the Gold cartridge. `TAXONOMY_CHANGE_258` resolves the current-HP check versus new-crossing ambiguity for `SYS-1213`. Neither change modifies an earlier signature or any verified combination.
- `SYS-921` is eligibility, `SYS-954` is the subsequent terrain/encounter-rate/weighted-slot sample, and `SYS-004` is the admitted randomness; they are not three claims of a guaranteed Hoothoot.

## Negative results

- The Berry heal is not manual medicine use, level-up healing, continuous regeneration or a new Action gene.
- No verified combination is registered from a single new carrier. No exact capture odds, encounter count, level-grind path, clock-setting exploit or cartridge run is asserted.

## Delta summary

## New facts

- [Confirmed | Direct | High] Original manual and pinned Gold code jointly establish clock-filtered Route 29 encounters, held-Berry threshold healing and the first badge's flag-setting order.

## New genes

- [Confirmed | Direct | High] One new Active `SYS-1213`; the remaining 28 uses reuse bounded existing genes.

## New combinations

- [Observation | Direct | High] None; recurrence is not inferred from one source-bound example.

## Taxonomy changes

- [Confirmed | Direct | High] `TAXONOMY_CHANGE_200` expands the clock-source and wild-eligibility carrier examples without changing their causal tests.

## New questions

- Does another independently reviewed original handheld cartridge use a civil clock to gate encounter tables while separately sampling individual encounters?
