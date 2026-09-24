---
game_id: GAME-0387
slug: super-bomberman
game_title: Super Bomberman
analysis_status: reviewed
reviewed: 2026-09-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-270
  system:
    - SYS-037
    - SYS-045
    - SYS-470
    - SYS-755
    - SYS-911
    - SYS-1045
  constraint:
    - CON-068
    - CON-402
  information:
    - INF-179
  objective:
    - OBJ-007
    - OBJ-164
  time:
    - TIM-003
---

# Game: Super Bomberman

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Bomberman,
Chopper, bomb capacity, fuse length and blast range are carrier parameters,
not separate gene names.

## Analysis scope

- Version / ruleset: original English PAL UK Super Nintendo release of 1993,
  one-player Normal Game, first stage 1-1 from a fresh start. The original
  UK instruction booklet establishes the core rules. A written first-stage
  route for the original SNES game corroborates stage ordering and pickups;
  its regional details are not asserted to be identical to this PAL cart.
- Structured analysis target: original UK PAL Super Nintendo cartridge in
  [`knowledge/platforms/games.json`](../../platforms/games.json), not the
  later Super Bomberman Collection's convenience wrapper.
- Primary decision loop: read the open grid, enemy position, breakable wall,
  exit possibility and live timer; move along orthogonal passages, place one
  available timed bomb, leave its impending cardinal blast lanes, then use
  the resulting enemy/terrain change to reach a newly safe corridor or pickup.
- Entry: first ordinary control of stage 1-1 with default bomb capacity and
  range, all initial stage enemies present, no acquired stage power-up and
  timer running. The exact initial tile map and timer value were not directly
  captured, so the packet does not prescribe a unique button sequence.
- Positive terminal: all required stage enemies have been eliminated, the
  concealed exit has been exposed by destroying its covering soft block, and
  the player enters that exit before stage time expires. Stop at the transition
  out of 1-1; do not analyse stage 1-2.
- Negative / recovery branches: a live enemy or own blast can kill the player;
  expiry of the displayed stage time also costs a life. If stock remains,
  the controlled body returns for a further stage attempt; exhausting stock
  ends this bounded fresh-start run. A bomb's live placement capacity is
  reusable when it explodes; the Extra Bomb power-up increases how many can
  coexist, not a consumable ammunition count.
- Included: cardinal grid movement and impassable hard/soft blocks, autonomous
  enemies, timed placed bombs, cross-shaped straight-line blast lanes stopped
  by blocking geometry, soft-block destruction revealing a pickup or hidden
  exit, contact power-up pickup, finite live-bomb capacity, enemy-clear exit
  condition, timer and life-stock failure.
- Excluded: Battle Mode, two-player Normal Game, remote bombs, punch/kick
  upgrades, later-stage enemy classes and bosses, exact frame timing,
  passwords, score optimisation, continues, and modern Collection Rewind,
  Save/Load Anytime and Boss Rush. The first-stage item route does not imply
  those later upgrades are present in 1-1.
- Reproducible parameterisation: record release/region, first-stage entry,
  controlled tile and adjacent wall classes, current live bombs and capacity,
  fuse/affected cardinal lanes, each surviving enemy, concealed-exit state,
  item pickup, timer, lives and exit transition. This is a source-bounded
  state reconstruction, not a controller trace.
- Potential scoped modules: later Normal Game stages, bosses and multiplayer
  Battle Mode require separate scope contracts.
- Direct-play status: none. The original UK manual was read and visually
  inspected as a scanned PDF, and original-SNES written routes were checked.
  No cartridge, ROM, executable, save, input trace, screenshot or play video
  was used as a direct trace of this release.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SB-001` | The D-pad moves the player; A lays a bomb, while remote detonation and punching require later power-ups | Confirmed | Direct | High | P1 |
| `SB-002` | A planted bomb explodes after a delay, destroying eligible blocks and enemies; its straight orthogonal blast lanes are limited by blocking geometry | Observation | Corroborated | Medium | P1, S1 |
| `SB-003` | Soft blocks can conceal pickups and the stage exit, which becomes traversable after the covering block is destroyed | Confirmed | Direct | High | P1 |
| `SB-004` | The exit is effective only after all required stage enemies have been eliminated | Confirmed | Direct | High | P1 |
| `SB-005` | Enemy contact, own explosion and stage-timer expiry can each cost a life; finite remaining lives allow another attempt | Confirmed | Direct | High | P1 |
| `SB-006` | Extra Bomb increases simultaneous live-bomb capacity and Explosion Expander increases blast range; neither is spent as one-shot bomb ammunition | Observation | Corroborated | Medium | P1, S1 |
| `SB-007` | An original-SNES first-stage written route places ordinary bomb and range pickups in 1-1, but regional placement and exact quantities are not transferred to the UK PAL target | Observation | Limited | Medium | S1, S2 |
| `SB-008` | No PAL cartridge, executable or direct play was inspected | Observation | Direct | High | R1 |

## Basic data

- Release / origin: Hudson Soft's Super Bomberman for Super Nintendo, first
  released in 1993; this packet follows its English PAL UK instructions.
- Platform or physical form: original PAL Super Nintendo cartridge; see the
  exact structured analysis target rather than inferring other ports.
- Puzzle family: real-time system pressure; spatial route construction
  through destructible obstacles.
- Primary source, checked 2026-09-24:
  - **[P1]** [Original UK SNES instruction
    booklet](https://www.retrogames.cz/manualy/SNES/Super_Bomberman_-_SNES_-_Manual.pdf),
    printed pp. 2–5 and 8–9. The scan establishes controls, Normal Game's
    bomb/enemy/exit/timer/life rules and Extra Bomb/Explosion Expander. Its
    illustrations depict cardinal blast geometry; the text does not supply
    exact collision frames or every wall-edge case.
- Original-SNES corroboration, checked 2026-09-24:
  - **[S1]** [First-stage written
    route](https://gamefaqs.gamespot.com/snes/588720-super-bomberman/faqs/30299),
    Level 1-1 section, for initial reusable bomb, soft blocks, pickups,
    enemies and exit. This account may represent another cartridge region.
  - **[S2]** [Independent original-SNES item
    guide](https://gamefaqs.gamespot.com/snes/588720-super-bomberman/faqs/5645),
    Level 1-1 item list; disagreements in password text are irrelevant and
    not imported.
- Official licensed destination: [Konami Super Bomberman
  Collection](https://www.konami.com/games/bomberman/collection/eu/en/),
  which includes the historical game. Its modern convenience features are
  deliberately excluded from this original-cartridge ruleset.
- **[R1]** Local evidence boundary: no measured PAL frame timing, cartridge
  bytes, exact map, direct play or audiovisual gameplay observation.
- Claim IDs: `SB-001`–`SB-008`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: move the controlled bomber through open cardinal grid passages.
- `ACT-270`: place a reusable-capability timed bomb on the current legal tile.
- Parameters: occupied tile, legal passage, live bomb count and capacity,
  current fuse and blast range.
- Claim IDs: `SB-001`, `SB-002`, `SB-006`.

### System Behaviour Genes

- `SYS-045`: stage enemies move autonomously through their available lanes.
- `SYS-470`: expired fuse resolves blast damage and removes its bomb object.
- `SYS-1045`: each detonation expands along four cardinal rays and stops at
  blocking terrain; this propagation boundary is separate from damage to
  anything reached by `SYS-470`.
- `SYS-755`: a compatible soft block breaks, losing collision and exposing
  contained pickup or exit if this block concealed one.
- `SYS-037`: contact with an exposed compatible item changes bomb capacity
  or range.
- `SYS-911`: lethal contact, own blast or timer loss consumes a stock life
  and returns the body while a further attempt remains.
- Resolution order: place → leave threatened lines → fuse expiry → cardinal
  rays stop or contact → damage/break → reveal/pickup or enemy-clear check →
  enter exit.
- Claim IDs: `SB-002`–`SB-006`.

### Constraint Genes

- `CON-402`: the exit remains unusable while a required stage enemy survives.
- `CON-068`: timer expiry fails the current stage attempt and costs a life.
- Live-bomb capacity and blast range are parameters of placement and blast
  propagation, not an additional generic ammunition resource or new gene.
- Claim IDs: `SB-004`–`SB-006`.

### Information Genes

- `INF-179`: the local arena exposes current avatar, visible enemy, obstacle,
  active bomb, blast and revealed pickup/exit state. It does not disclose
  which still-intact soft block covers the exit.
- Claim IDs: `SB-002`, `SB-003`.

### Objective Genes

- `OBJ-007`: clear the finite enemy set required for this stage.
- `OBJ-164`: uncover and enter the resulting stage exit to transition into
  the next region with eligible remaining lives/score carried forward.
- Success, evaluation and failure: killing every enemy alone is insufficient;
  an exit hidden under intact terrain cannot yet be entered. The terminal is
  the actual exit transition, not reaching a score threshold.
- Claim IDs: `SB-003`–`SB-005`.

### Time Genes

- `TIM-003`: bombs, enemies and timer continue advancing while the player
  steers. Timing is not an unlimited-turn puzzle counter.
- Claim IDs: `SB-002`, `SB-005`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| One live-bomb slot free, open tile | Lay a bomb and move around a hard corner | The bomb stays, the fuse advances, and the player can stand outside its future cardinal rays | Placement is a timed spatial commitment | `SB-001`, `SB-002` |
| A bomb ray faces an intact hard block | Wait for fuse expiry from a safe tile | The ray stops at the block; a tile behind it is not struck by that ray | Ray geometry differs from a circular radius | `SB-002` |
| A bomb ray faces a soft block | Detonate after leaving the lane | The block breaks and its former tile becomes open; a concealed pickup or exit can appear | Terrain is both obstacle and information cover | `SB-002`, `SB-003` |
| Extra Bomb is exposed and touched | Pick it up, then lay a further compatible bomb | The simultaneous live-bomb limit rises; no one-shot carried ammunition is spent | Capacity is concurrent-placement state | `SB-006` |
| One required enemy remains and exit is exposed | Enter the exit tile | The stage does not close while the enemy remains | Revealing an exit is not enough | `SB-004` |
| Last required enemy eliminated, exit revealed | Reach and enter it before timer expiry | Stage 1-1 closes and the successor begins; analysis stops | Conjunctive clear-and-exit objective | `SB-003`, `SB-004` |
| Player stands on an imminent blast ray or touches an enemy | Let the hit resolve | A life is consumed and, if stock remains, another stage attempt is available | Bombs can harm their placer | `SB-005` |
| Clock reaches zero before exit transition | Continue without completing exit | A life is consumed and the current attempt fails | Deadline is authoritative, not score-only | `SB-005` |

## Strategic and experiential structure

- Local decision: choose where a blast will reach, where a hard wall will stop
  it and where the bomber can escape before detonation.
- Medium-term planning: open soft-block passages to find useful pickups and
  hidden exit while eliminating enemies, without trapping the player.
- Long-term structure: first-stage clear and exit, then the next stage. This
  packet does not model the whole Normal Game campaign.
- Common heuristic: lay a bomb beside a soft wall with a safe perpendicular
  turn available; count live placements before trying another.
- Failure attribution: enemy contact, self-inflicted blast and elapsed timer
  are different immediate causes but share the finite-life recovery rule.
- Player-trust factors: visible fuse effects, block class, enemy positions and
  exposed exit support local planning; unopened block contents remain hidden.
- Claim IDs: `SB-001`–`SB-006`.

## Replay and variation

- What changes between attempts: placement sequence, current open corridors,
  surviving enemies, acquired capacity/range and remaining life stock.
- Randomness or procedural generation: this packet does not assert that the
  original fixed first-stage map is procedurally regenerated. Enemy motion
  and player timing can vary without implying a new level seed.
- Multiple viable strategies: different safe bomb placements can clear the
  same first stage; the cited route is not a unique solution proof.
- Typical replay motive: achieve a safer or faster clear with better score.
- Claim IDs: `SB-002`–`SB-007`.

## Adjacent systems and history

- Original Bomberman lineage explains the grid-and-bomb concept, but the
  selected game's PAL booklet is the rule authority here.
- The Collection offers a licensed destination, not proof that Rewind or
  wrapper saving existed on the 1993 cartridge.
- The Binding of Isaac: Rebirth shares timed bomb placement, blast resolution,
  destructible room geometry and enemy-gated doors. Super Bomberman's distinct
  boundary is an explicitly tile-aligned four-ray blast stopped by obstacles.
- Claim IDs: `SB-001`–`SB-006`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-270` | Tile, capacity |
| System Behaviour | `SYS-037`, `SYS-045`, `SYS-470`, `SYS-755`, `SYS-911`, `SYS-1045` | Enemy path, fuse, wall contents, range |
| Constraint | `CON-068`, `CON-402` | Timer, required enemy set |
| Information | `INF-179` | Concealed exit versus visible current field |
| Objective | `OBJ-007`, `OBJ-164` | Clear then take exit |
| Time | `TIM-003` | Live fuse and clock |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `386` (`GAME-0001`–`GAME-0386`).
- Exact genome matches: none.
- Tied near matches: `GAME-0333` — Sonic the Hedgehog (`8 / 26 = 0.307692`).
- Supported combination subsets: none.
- Scan date: 2026-09-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0333` Sonic the Hedgehog | `ACT-008`, `SYS-037`, `SYS-045`, `SYS-755`, `SYS-911`, `CON-068`, `OBJ-164` and `TIM-003` cover live movement, autonomous enemies, breakable geometry, pickups, timed stage pressure, finite-life recovery and an exit transition. | Sonic's side-view momentum, ring-buffer hit rule and signpost closeout do not lay timed bombs or calculate obstacle-stopped four-ray blast lanes. Super Bomberman's enemy-clear exit and hidden soft-block cover are not Sonic's ring-and-route rule. | `8 / 26 = 0.307692`; tied near maximum, not an equivalent traversal loop |

### Preserved research notes

- New genes: `SYS-1045`.
- Reused genes: `ACT-008`, `ACT-270`, `SYS-037`, `SYS-045`, `SYS-470`,
  `SYS-755`, `SYS-911`, `CON-068`, `CON-402`, `INF-179`, `OBJ-007`, `OBJ-164`,
  `TIM-003`.
- Classification result: one cross-ray propagation distinction while live
  bomb capacity, range, hidden item and exit conditions reuse existing genes.

## Taxonomy impact

- `TAXONOMY_CHANGE_126` accepts one additive ray-propagation gene.
- No older game signature, gene lifecycle, family definition or verified
  combination changes in this unit.

## Negative results

- A visually circular or diagonal blast is not inferred from bomb placement;
  the first-stage path uses cardinal corridors and stopped rays.
- Extra Bomb is not one disposable bomb. The upgrade increases concurrent
  placements; fuse completion restores a placement opportunity.
- The hidden exit is not a permanently available revealed door, and a cleared
  enemy set without entering it is not a completed stage.
- Item counts, exact tile placements, frame timing and passwords in guides
  are not silently transferred between SNES regions.
- Collection convenience controls do not belong to the original PAL genome.

## Delta summary

## New facts

- [Confirmed | Direct | High] The original UK instructions establish timed
  bomb placement, breakable concealment, enemy-clear exit, timer and finite
  life consequences (`SB-001`–`SB-006`).

## New genes

- [Observation | Corroborated | Medium] `SYS-1045` isolates four cardinal
  blocked blast rays from the generic damage resolution of `SYS-470`.

## New combinations

- [Observation | Corroborated | High] No verified combination is registered.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_126` adds one
  ray-propagation boundary without changing earlier signatures.

## New questions

- Which exact PAL cartridge revision and tile arrangement define 1-1's
  concealed exit and pickup locations?
- Would a direct original-cartridge trace refine soft-block propagation
  timing or life-reset persistence beyond the booklet's qualitative rules?

## Next recommended game

- [Hypothesis | Limited | Medium] No next game is selected. This is the final
  subject of the nine-game horizon; a new editorial selection is required.
- Optimisation criterion: alternate primary loops and avoid repeating a
  top-down bomb-grid image immediately after this card.
- Backlog impact: finish the current Goal at 9/9; do not start another unit.

## Why this game

- [Hypothesis | Limited | Medium] A first-stage bomb maze isolates delayed
  placement, obstacle-stopped cardinal blast propagation and a concealed exit
  after a previous three-dimensional collection-and-gating game.
