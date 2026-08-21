---
game_id: GAME-0150
slug: hollow-knight-silksong
game_title: "Hollow Knight: Silksong"
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0148
gene_ids:
  action:
    - ACT-008
    - ACT-130
    - ACT-161
    - ACT-190
    - ACT-215
    - ACT-224
  system:
    - SYS-215
    - SYS-364
    - SYS-397
    - SYS-398
    - SYS-399
    - SYS-400
  constraint:
    - CON-269
    - CON-349
    - CON-350
    - CON-351
    - CON-352
  information:
    - INF-073
    - INF-119
    - INF-125
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Hollow Knight: Silksong

## Analysis scope

- Version / ruleset: base PC game, patch `1.0.30000`, Normal mode; one fresh
  save from the opening through first entry into Act 2 after activating the
  five Act 1 Bellshrines and defeating Last Judge at the Grand Gate.
- Included: direct running, jumping and ledge movement; needle combat; health,
  Silk generation, full-spool Bind and Silk Skills; Silkspear; Swift Step,
  Drifter's Cloak, Cling Grip and Needolin; Rosaries and paid Benches; resting,
  saving, Tool replenishment and ordinary-enemy respawn; Hunter and Reaper
  Crest selection with coloured Tool slots; ordinary death, checkpoint return,
  one recoverable Cocoon and second-death loss; the Marrow, Far Fields,
  Greymoor, Bellhart and Shellwood Bellshrines; Last Judge and Citadel entry.
- Excluded: Acts 2 and 3 after the first Citadel entry; Steel Soul, easier
  post-launch balance variants and accessibility assists; exhaustive Crests,
  Tools, Skills, Wishes, bosses, maps, collectables and endings; speedrun skips,
  glitches and sequence breaks; achievements, platform features and the
  announced but unreleased Sea of Sorrow expansion.
- Direct-play status: no authenticated fresh route was played. Current official
  patch and product material, an official platform mechanics article and
  maintained community mechanics pages were reconciled into a repository-side
  deterministic transition trace; community claims remain labelled secondary.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HKS-001` | Patch 1.0.30000 is the current released PC boundary; Sea of Sorrow remains announced rather than part of the base route | Confirmed | Direct | High | P1, P2 |
| `HKS-002` | Needle hits generate Silk; Bind requires a full spool, consumes it and heals three masks, while Silk Skills spend the same resource | Confirmed | Corroborated | High | P3, S1 |
| `HKS-003` | Swift Step, Drifter's Cloak and Cling Grip permanently add dash, glide or updraft and wall-cling movement used by authored route edges | Observation | Corroborated | High | S2, S3, S4 |
| `HKS-004` | Crests replace attack form and Tool-slot topology and may modify Bind; Tools fit only compatible coloured slots | Confirmed | Corroborated | High | P3, S5 |
| `HKS-005` | Resting at a Bench saves and establishes return, restores health, can replenish Tools from Shell Shards and respawns ordinary enemies; some Benches cost Rosaries | Observation | Corroborated | High | P1, S6 |
| `HKS-006` | Ordinary death returns Hornet to the active Bench and creates one Rosary Cocoon; until recovery the spool is capped, and a second death replaces the old Cocoon and loses its stored Rosaries | Observation | Corroborated | High | P1, S7 |
| `HKS-007` | Needolin is acquired after Widow and spends Silk to activate compatible mechanisms, including the Grand Gate after the five required Bellshrines | Observation | Corroborated | High | S8, S9 |
| `HKS-008` | Act 1 requires the five regional Bellshrines, Grand Gate interaction, Last Judge defeat and first Citadel entry | Observation | Corroborated | High | S9, S10 |
| `HKS-009` | The repository trace reproduces capability gating, Crest legality, Bind trade-offs, Bench reset, both Cocoon branches and Act 1 completion | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Team Cherry; released 2025-09-04 and maintained through
  current patch `1.0.30000` at review time.
- Platform or physical form: authored single-player action-exploration game for
  PC and consoles; this scope uses the current PC base game in Normal mode.
- Puzzle family: live combat and capability-gated route sequencing through a
  persistent authored world.
- Primary sources:
  - **[P1]** [official Steam announcements](https://store.steampowered.com/oldnews/?appgroupname=Hollow+Knight%3A+Silksong&appids=1030300&feed=steam_community_announcements),
    for current patch 1.0.30000, Bench, Crest, Tool, Cocoon, Grand Gate and
    Last Judge maintenance evidence.
  - **[P2]** [Team Cherry game page](https://www.teamcherry.com.au/games), for
    released base-game status, traversal, combat, Tools and ascent framing.
  - **[P3]** [official PlayStation mechanics article](https://blog.playstation.com/2025/09/09/hollow-knight-silksong-8-ways-it-evolves-the-side-scrolling-formula/),
    for Silk, Bind, healing, Skills, Tools, Crests, Tool layouts and Needolin.
- Secondary sources:
  - **[S1]** [community Combat reference](https://hollowknight.wiki/w/Combat_(Silksong)),
    for the shared Silk-spool transitions.
  - **[S2]** [community Swift Step reference](https://hollowknight.wiki/w/Swift_Step),
    for dash and sprint acquisition.
  - **[S3]** [community Drifter's Cloak reference](https://hollowknight.wiki/w/Drifter%27s_Cloak),
    for glide and updraft traversal.
  - **[S4]** [community Cling Grip reference](https://hollowknight.wiki/w/Cling_Grip),
    for wall cling and wall jump.
  - **[S5]** [community Crest reference](https://hollowknight.wiki/w/Crests),
    for coloured Tool-slot legality and Bench configuration.
  - **[S6]** [community Bench reference](https://hollowknight.wiki/w/Bench_(Silksong)),
    for save, return, refill, enemy-respawn and price transitions.
  - **[S7]** [community Cocoon reference](https://hollowknight.wiki/w/Cocoon),
    for Rosary storage, temporary spool cap, recovery and replacement.
  - **[S8]** [community Needolin reference](https://hollowknight.wiki/w/Needolin),
    for Widow acquisition, Silk cost and mechanism interaction.
  - **[S9]** [community Grand Gate route](https://hollowknight.wiki/w/OPEN:_Grand_Gate),
    for the five Bellshrines, Needolin gate and Act 2 boundary.
  - **[S10]** [community Last Judge reference](https://hollowknight.wiki/w/Last_Judge),
    for guardian appearance, defeat and post-boss route.
- Reproducible control:
  - **[V1]** repository-side state trace derived from `P1`–`P3` and `S1`–`S10`;
    it is rules reasoning, not a claim of direct play.
- Claim IDs: `HKS-001`–`HKS-009`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, directly navigate Hornet; `ACT-130`, spend
  Rosaries on a priced Bench service; `ACT-161`, aim and strike with the Needle;
  `ACT-190`, activate a learned Silk Skill or Needolin; `ACT-224`, deliberately
  rest at an activated Bench; `ACT-215`, configure a bounded compatible combat
  loadout at a preparation point.
- Parameters: movement capability, Needle reach, Skill, Silk, Bench, price,
  Crest, Tool colour, unlocked slot and replacement.
- Claim IDs: `HKS-002`–`HKS-008`.

### System Behaviour Genes

- Existing genes: `SYS-215`, resolve live hostile combat; `SYS-364`, restore
  checkpoint resources and respawn ordinary field enemies after resting.
- New genes: `SYS-397`, turn Needle hits into Silk-funded Bind and Skills;
  `SYS-398`, retain each acquired traversal or interaction capability;
  `SYS-399`, produce checkpoint return and one recoverable death Cocoon;
  `SYS-400`, apply the active Crest to attack, Bind and Tool topology.
- Resolution order: a Needle hit may add Silk before the next action; Bind or a
  Skill validates and spends that state; lethal damage records a Cocoon and
  returns Hornet to the active Bench; a later hit on that Cocoon restores its
  stored state unless another death has already replaced it; acquired route
  capabilities and activated Bellshrines remain retained across these deaths.
- Parameters: damage, health, Silk, capacity, Crest, Tool, checkpoint, Rosaries,
  Cocoon, acquisition flag, Bellshrine and boss state.
- Claim IDs: `HKS-002`–`HKS-009`.

### Constraint Genes

- Existing gene: `CON-269`, a learned active requires its legal target, range,
  resource and readiness.
- New genes: `CON-349`, authored edges require their retained movement or
  Needolin capability; `CON-350`, Tools fit only the selected Crest's unlocked
  coloured slots; `CON-351`, Bind and Skills require their declared Silk;
  `CON-352`, only one unrecovered Cocoon persists.
- Scarce strategic resources: health masks, current Silk, safe time to Bind,
  Rosaries, Shell Shards, Tool charges, legal Crest slots, Bench access and an
  unrecovered Cocoon's route exposure.
- Claim IDs: `HKS-002`–`HKS-008`.

### Information Genes

- Existing genes: `INF-073`, expose currently equipped Tools and active combat
  state; `INF-119`, expose health, Silk, Crest and ability readiness; `INF-125`,
  expose discovered map, wishes and current authored route requirements.
- Claim IDs: `HKS-002`–`HKS-008`.

### Objective Genes

- New gene: `OBJ-080`, finish Act 1 by satisfying the five regional gates,
  playing Needolin at the Grand Gate, defeating Last Judge and entering the
  Citadel.
- Success, evaluation and failure: first Act 2 entry is the analytical success;
  ordinary death is a recoverable setback, while an unrecovered second death
  can permanently remove stored Rosaries but does not erase route acquisitions.
- Claim IDs: `HKS-006`–`HKS-009`.

### Time Genes

- Existing gene: `TIM-003`, movement, combat, Silk decisions, boss attacks and
  hazards resolve in continuous real time while the player acts.
- Parameters: simulation step, attack recovery, Bind window, Skill animation,
  Tool effect, enemy movement and hazard timing.
- Claim IDs: `HKS-002`–`HKS-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Hornet has not acquired Swift Step and faces its authored dash gap | Attempt ordinary running jump | The route edge remains unreachable | capability flags, not player knowledge alone, gate topology | `HKS-003` |
| Swift Step has been acquired in Deep Docks | Dash through the same compatible edge | Hornet crosses and the capability remains available after later deaths | movement acquisition permanently expands the save's route graph | `HKS-003` |
| Silk is below the full-spool predicate | Activate Bind | No heal commits | Bind is not a partially affordable heal | `HKS-002` |
| Silk is full and health is missing | Activate Bind in the air | The full spool is consumed and three masks are restored | attacks fund a discrete tactical heal with an all-resource cost | `HKS-002` |
| Hunter Crest and one compatible Tool are acquired at a Bench | Equip the Tool in a matching Hunter slot | The Tool becomes active with Hunter attack geometry | Crest selection and Tool assignment form one legal loadout | `HKS-004` |
| Reaper Crest replaces Hunter at the Bench | Reassign compatible Tools and leave the Bench | Attack geometry, slot layout and post-Bind modifier use Reaper rules | Crest changes more than a numeric equipment statistic | `HKS-004` |
| A priced Bench is inactive and enough Rosaries are held | Purchase and rest | Rosaries are debited; the Bench becomes the save/return point and rest refills eligible state while ordinary enemies respawn | safety and recovery trade currency for a world reset | `HKS-005` |
| Hornet carries Rosaries and dies after resting | Accept ordinary death return | Hornet returns at the Bench; one Cocoon stores the Rosaries and Silk capacity is temporarily capped | death preserves world progress but creates a recoverable liability | `HKS-006` |
| The current Cocoon remains reachable | Strike the Cocoon | Stored Rosaries and normal spool capacity return | recovery is a world interaction, not an automatic reload | `HKS-006` |
| A Cocoon remains unrecovered | Die again elsewhere | The new Cocoon replaces the old one and the old stored Rosaries are lost | repeated failure makes one recoverable loss permanent | `HKS-006` |
| Widow is defeated and Hornet binds the resulting power | Hold Needolin at a compatible mechanism with enough Silk | Silk is spent and the mechanism receives its authored musical activation | Needolin is a retained interaction capability with a resource gate | `HKS-007` |
| All five required Bellshrines are active and Needolin is acquired | Play Needolin at the Grand Gate | The gate sequence proceeds and Last Judge guards the route | regional progress composes into a boss gate | `HKS-007` |
| Last Judge is alive | Defeat the boss and survive the terminal sequence | The path into the Citadel becomes traversable | boss victory is necessary but not itself the scoped terminal state | `HKS-008` |
| Last Judge is defeated and the route is open | Cross into the Citadel | Act 2 begins and the analytical unit ends | the objective is a verified act transition | `HKS-008` |

## Strategic and experiential structure

- Local decision: attack to build Silk, preserve the full spool for Bind, spend
  it on a Skill, commit to a traversal input, change Tool, rest or risk the
  route back to an unrecovered Cocoon.
- Medium-term planning: buy useful Benches, choose a Crest/Tool layout for the
  next region, acquire movement capabilities and order Bellshrine visits so
  death recovery remains tractable.
- Long-term structure: retain the four scoped capabilities and five shrine
  flags, bring Needolin to the Grand Gate, defeat Last Judge and cross the act
  boundary.
- Common heuristics: heal only when a full-spool Bind is safe, recover a Cocoon
  before taking another high-risk route, rest when refill value exceeds enemy
  reset cost and match Crest geometry to the next boss or traversal demand.
- Failure attribution: immediate attacks and resource spending are legible;
  a lost Cocoon is deterministic, while unexplored route topology can make the
  original planning error less obvious.
- Player-trust factors: visible Silk, health, Tool and map state support causal
  learning; exact hidden boss health and external route guides are excluded.
- Claim IDs: `HKS-002`–`HKS-009`.

## Replay and variation

- What changes between sessions: regional visit order, optional acquisitions,
  Crest and Tool choices, Bench purchases, Cocoon position and the combat
  route used to satisfy the same Act 1 gate.
- Randomness or procedural generation: world geometry, Bellshrines and boss
  gates are authored; enemy timing and player execution create variation, not
  a generated map.
- Multiple viable strategies: Hunter or Reaper geometry, healing versus Skill
  spending and earlier or later Bench activation trade safety, damage and
  route efficiency.
- Typical replay motive: improve traversal/combat execution, reduce Rosary
  exposure and test another loadout or route order.
- Claim IDs: `HKS-002`–`HKS-008`.

## Adjacent systems and history

- Direct predecessor: Hollow Knight supplies the broad authored exploration,
  checkpoint and recoverable-currency lineage, but not Silksong's Crest-shaped
  Tool topology or full-spool three-mask Bind.
- Variants: Steel Soul removes ordinary same-save recovery; later acts add
  capabilities and objectives outside this boundary; Sea of Sorrow remains
  announced and excluded.
- Similar games: Hollow Knight, TUNIC, Ori, Blasphemous and other
  action-exploration games with authored ability gates and checkpoint risk.
- Important differences: the scoped route couples attack-generated healing
  resource, Crest-dependent loadout topology, one replaceable currency Cocoon
  and five retained regional gates to one guardian-controlled act transition.
- Claim IDs: `HKS-001`–`HKS-008`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-130`, `ACT-161`, `ACT-190`, `ACT-224`, `ACT-215` | bindings, exact prices and Tool identities are parameters |
| System Behaviour | `SYS-215`, `SYS-364`, `SYS-397`–`SYS-400` | damage, Silk gains and animation durations are parameters |
| Constraint | `CON-269`, `CON-349`–`CON-352` | exact gate geometry and slot counts are parameters |
| Information | `INF-073`, `INF-119`, `INF-125` | HUD position and audiovisual style are excluded |
| Objective | `OBJ-080` | regional visit order is a parameter |
| Time | `TIM-003` | admitted movement and combat remain live |

## Edge cases

- Resting is a deliberate reset trade: it restores eligible state and saves,
  but ordinary defeated enemies in the linked world return.
- A purchased Bench can be valuable even when a nearer Cocoon route becomes
  harder, because the return point and map state change together.
- Rosaries secured in strings are outside the spendable Cocoon amount until
  broken; this scope analyses ordinary spendable Rosaries, not string strategy.
- A second death without recovery does not duplicate currency: the earlier
  Cocoon is replaced and its stored Rosaries are lost.
- Switching Crest never removes acquired traversal capabilities; it changes
  combat form, Bind modifier and legal Tool topology.
- A Tool that lacks a compatible unlocked coloured slot cannot stay equipped
  merely because it is owned.
- Five Bellshrines without Needolin do not open the Grand Gate; Needolin without
  all five shrine flags also fails the route predicate.
- Defeating Last Judge during a mutually lethal terminal sequence is not
  admitted unless the route state persists and Hornet can enter the Citadel.
- Sea of Sorrow announcement material is version evidence only and contributes
  no mechanic to this base-game genome.

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-008,ACT-130,ACT-161,ACT-190,ACT-224,ACT-215; SYS-215,SYS-364,SYS-397,SYS-398,SYS-399,SYS-400; CON-269,CON-349,CON-350,CON-351,CON-352; INF-073,INF-119,INF-125; OBJ-080; TIM-003`.
- Indexed games scanned: all 149 earlier canonical games.
- Indexed combinations scanned: all 147 earlier verified combinations.
- Exact genome matches: none.
- Near match: Marvel Rivals (`GAME-0147`) at `7 / 40 = 0.175000`.
- Supported prior combination subsets: none; new `COMB-0148` is a strict
  subset of this 22-gene genome.
- Scan date: 2026-08-21.

Exhaustive prior-game ledger:

- GAME-0001: 0 / 36 = 0.000000; GAME-0002: 0 / 29 = 0.000000; GAME-0003: 0 / 31 = 0.000000; GAME-0004: 1 / 36 = 0.027778.
- GAME-0005: 0 / 29 = 0.000000; GAME-0006: 1 / 30 = 0.033333; GAME-0007: 0 / 30 = 0.000000; GAME-0008: 0 / 29 = 0.000000.
- GAME-0009: 0 / 38 = 0.000000; GAME-0010: 0 / 31 = 0.000000; GAME-0011: 0 / 35 = 0.000000; GAME-0012: 0 / 31 = 0.000000.
- GAME-0013: 0 / 35 = 0.000000; GAME-0014: 0 / 37 = 0.000000; GAME-0015: 0 / 36 = 0.000000; GAME-0016: 1 / 36 = 0.027778.
- GAME-0017: 0 / 35 = 0.000000; GAME-0018: 1 / 40 = 0.025000; GAME-0019: 0 / 32 = 0.000000; GAME-0020: 0 / 36 = 0.000000.
- GAME-0021: 1 / 30 = 0.033333; GAME-0022: 0 / 34 = 0.000000; GAME-0023: 0 / 32 = 0.000000; GAME-0024: 1 / 33 = 0.030303.
- GAME-0025: 1 / 32 = 0.031250; GAME-0026: 1 / 33 = 0.030303; GAME-0027: 1 / 33 = 0.030303; GAME-0028: 1 / 38 = 0.026316.
- GAME-0029: 2 / 32 = 0.062500; GAME-0030: 1 / 35 = 0.028571; GAME-0031: 0 / 33 = 0.000000; GAME-0032: 0 / 33 = 0.000000.
- GAME-0033: 2 / 33 = 0.060606; GAME-0034: 2 / 34 = 0.058824; GAME-0035: 2 / 38 = 0.052632; GAME-0036: 1 / 33 = 0.030303.
- GAME-0037: 0 / 31 = 0.000000; GAME-0038: 2 / 36 = 0.055556; GAME-0039: 0 / 31 = 0.000000; GAME-0040: 1 / 29 = 0.034483.
- GAME-0041: 2 / 31 = 0.064516; GAME-0042: 0 / 31 = 0.000000; GAME-0043: 1 / 35 = 0.028571; GAME-0044: 1 / 31 = 0.032258.
- GAME-0045: 1 / 35 = 0.028571; GAME-0046: 0 / 32 = 0.000000; GAME-0047: 0 / 36 = 0.000000; GAME-0048: 0 / 36 = 0.000000.
- GAME-0049: 0 / 31 = 0.000000; GAME-0050: 1 / 36 = 0.027778; GAME-0051: 1 / 37 = 0.027027; GAME-0052: 0 / 32 = 0.000000.
- GAME-0053: 1 / 30 = 0.033333; GAME-0054: 1 / 32 = 0.031250; GAME-0055: 1 / 31 = 0.032258; GAME-0056: 0 / 30 = 0.000000.
- GAME-0057: 0 / 30 = 0.000000; GAME-0058: 0 / 31 = 0.000000; GAME-0059: 0 / 29 = 0.000000; GAME-0060: 0 / 29 = 0.000000.
- GAME-0061: 0 / 32 = 0.000000; GAME-0062: 0 / 30 = 0.000000; GAME-0063: 0 / 29 = 0.000000; GAME-0064: 0 / 27 = 0.000000.
- GAME-0065: 0 / 29 = 0.000000; GAME-0066: 0 / 32 = 0.000000; GAME-0067: 0 / 30 = 0.000000; GAME-0068: 0 / 30 = 0.000000.
- GAME-0069: 0 / 30 = 0.000000; GAME-0070: 0 / 30 = 0.000000; GAME-0071: 0 / 29 = 0.000000; GAME-0072: 0 / 30 = 0.000000.
- GAME-0073: 0 / 29 = 0.000000; GAME-0074: 0 / 31 = 0.000000; GAME-0075: 0 / 31 = 0.000000; GAME-0076: 0 / 29 = 0.000000.
- GAME-0077: 0 / 29 = 0.000000; GAME-0078: 0 / 29 = 0.000000; GAME-0079: 0 / 29 = 0.000000; GAME-0080: 0 / 29 = 0.000000.
- GAME-0081: 0 / 30 = 0.000000; GAME-0082: 0 / 30 = 0.000000; GAME-0083: 0 / 30 = 0.000000; GAME-0084: 0 / 32 = 0.000000.
- GAME-0085: 0 / 33 = 0.000000; GAME-0086: 0 / 35 = 0.000000; GAME-0087: 1 / 31 = 0.032258; GAME-0088: 0 / 31 = 0.000000.
- GAME-0089: 0 / 31 = 0.000000; GAME-0090: 1 / 36 = 0.027778; GAME-0091: 2 / 29 = 0.068966; GAME-0092: 1 / 31 = 0.032258.
- GAME-0093: 0 / 31 = 0.000000; GAME-0094: 2 / 30 = 0.066667; GAME-0095: 2 / 32 = 0.062500; GAME-0096: 2 / 30 = 0.066667.
- GAME-0097: 2 / 28 = 0.071429; GAME-0098: 2 / 27 = 0.074074; GAME-0099: 1 / 29 = 0.034483; GAME-0100: 1 / 32 = 0.031250.
- GAME-0101: 0 / 32 = 0.000000; GAME-0102: 0 / 29 = 0.000000; GAME-0103: 0 / 31 = 0.000000; GAME-0104: 1 / 30 = 0.033333.
- GAME-0105: 2 / 30 = 0.066667; GAME-0106: 0 / 29 = 0.000000; GAME-0107: 1 / 29 = 0.034483; GAME-0108: 1 / 31 = 0.032258.
- GAME-0109: 0 / 38 = 0.000000; GAME-0110: 1 / 29 = 0.034483; GAME-0111: 1 / 28 = 0.035714; GAME-0112: 2 / 28 = 0.071429.
- GAME-0113: 2 / 34 = 0.058824; GAME-0114: 1 / 28 = 0.035714; GAME-0115: 0 / 28 = 0.000000; GAME-0116: 2 / 26 = 0.076923.
- GAME-0117: 1 / 29 = 0.034483; GAME-0118: 1 / 37 = 0.027027; GAME-0119: 1 / 44 = 0.022727; GAME-0120: 1 / 50 = 0.020000.
- GAME-0121: 1 / 44 = 0.022727; GAME-0122: 1 / 36 = 0.027778; GAME-0123: 1 / 59 = 0.016949; GAME-0124: 2 / 67 = 0.029851.
- GAME-0125: 1 / 63 = 0.015873; GAME-0126: 1 / 64 = 0.015625; GAME-0127: 1 / 69 = 0.014493; GAME-0128: 1 / 37 = 0.027027.
- GAME-0129: 5 / 52 = 0.096154; GAME-0130: 1 / 74 = 0.013514; GAME-0131: 4 / 64 = 0.062500; GAME-0132: 1 / 72 = 0.013889.
- GAME-0133: 1 / 66 = 0.015152; GAME-0134: 1 / 72 = 0.013889; GAME-0135: 1 / 69 = 0.014493; GAME-0136: 1 / 81 = 0.012346.
- GAME-0137: 5 / 47 = 0.106383; GAME-0138: 6 / 51 = 0.117647; GAME-0139: 6 / 70 = 0.085714; GAME-0140: 5 / 60 = 0.083333.
- GAME-0141: 5 / 68 = 0.073529; GAME-0142: 5 / 68 = 0.073529; GAME-0143: 4 / 67 = 0.059701; GAME-0144: 8 / 49 = 0.163265.
- GAME-0145: 9 / 61 = 0.147541; GAME-0146: 9 / 77 = 0.116883; GAME-0147: 7 / 40 = 0.175000; GAME-0148: 9 / 56 = 0.160714.
- GAME-0149: 8 / 49 = 0.163265.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Marvel Rivals (`GAME-0147`) | `ACT-008`, `ACT-161`, `ACT-190`, `SYS-215`, `CON-269`, `INF-119`, `TIM-003` | reconfigurable team heroes and capture-to-escort pressure versus a persistent solo route with Silk, Crests, Benches, Cocoon and authored act gates | nearest, not exact; `7 / 40 = 0.175000` |

- New genes: `SYS-397`–`SYS-400`, `CON-349`–`CON-352`, `OBJ-080`.
- Classification result: `New gene` and new combination of known and new genes.
- Evidence and reasoning: the distinctive boundary is the coupling of a shared
  attack/heal resource, permanent route capabilities, Crest-shaped loadout and
  recoverable death state to one multi-region act gate.

### Registry normalisation 006 score corrections

These recomputed values supersede the pre-normalisation fractions above:

- `GAME-0132`: `2 / 71 = 0.028169`
- `GAME-0137`: `6 / 46 = 0.130435`
- `GAME-0143`: `5 / 66 = 0.075758`
- `GAME-0149`: `9 / 48 = 0.187500`
- Current prior-corpus near match after normalisation 006: `GAME-0149`.

## Combination assessment

- `COMB-0148` is admitted as a verified interaction pattern: a persistent
  capability-gated route joins live Silk combat, checkpoint resets, one
  recoverable death liability and Crest-shaped loadout decisions to a composed
  act gate.
- It is a strict subset of this 22-gene genome and excludes parameters that do
  not define that coupling.
- Independent recurrence is unassessed; no exact set duplicate is admitted.

## Taxonomy impact

- Registry changes after normalisation: add nine bounded genes and `COMB-0148`;
  extend evidence for thirteen reused records.
- Taxonomy-change record: `TAXONOMY_CHANGE_012`.
- Candidate terms affected: exact Silk amounts, Bench prices, named regions,
  Tool identities and movement distances remain parameters.

## Negative results

- No separate negative-result record. The boundary review rejected four broad
  normalisations inside this game record: Cocoon as generic inventory drop,
  Crest as numeric equipment, traversal ability as carried key and death as
  complete checkpoint rollback.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Needle hits fund the same Silk pool used by
  full-spool Bind and learned Skills, making healing and access compete
  (`HKS-002`).
- [Observation | Corroborated | High] Five Bellshrines and Needolin jointly
  expose Last Judge before the first Citadel entry (`HKS-007`, `HKS-008`).
- [Observation | Corroborated | High] One recoverable Cocoon becomes permanent
  Rosary loss if another death replaces it (`HKS-006`).

## Нові гени

- [Observation | Corroborated | High] Ten bounded genes cover Bench-only
  Crest/Tool configuration, Silk conversion, persistent capability gates,
  Cocoon death, Crest rule replacement and the composed act objective.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0148` — Capability-gated ascent
  couples Silk, Crest loadout, checkpoint reset and recoverable death.

## Зміни таксономії

- [Observation | Direct | High] Змін таксономії немає.

## Family classification

- `FAM-009` — Tactical forecast and counterplay: Needle contact produces
  Silk that must be divided between healing and route/combat Skills.
- `FAM-010` — Real-time system pressure: live enemies and Last Judge make
  execution and health state causal.
- `FAM-017` — Ordered dependency sequencing: acquisitions, regional shrines,
  Needolin, boss victory and Citadel entry form a retained dependency graph.
- No new family is created from a single game.

## Plain-language interpretation

Silksong's early route is not just a sequence of platform rooms. Hitting enemies
fills one Silk spool, and the same resource either heals three masks through a
full-spool Bind or powers abilities such as Silkspear and Needolin. Resting at a
Bench makes a safer return point and restores useful state, but also brings
ordinary enemies back. Death keeps world progress yet moves all spendable
Rosaries into one Cocoon; failing again before reclaiming it turns that
recoverable risk into a permanent loss.

Progress changes the route graph. Swift Step opens dash edges, Drifter's Cloak
opens glide and updraft edges, Cling Grip opens wall routes, and Needolin
activates authored mechanisms. Crests separately change attack geometry, Bind
behaviour and which coloured Tool slots can be filled at a Bench. The Act 1
route composes all of those local choices: activate five regional Bellshrines,
play Needolin at the Grand Gate, defeat Last Judge and then actually cross into
the Citadel.

## Research decision

- Decision: admit `GAME-0150`, nine bounded genes and `COMB-0148`; extend
  evidence on thirteen reused records without broadening their definitions.
- Rejected normalisations: Cocoon is not generic dropped inventory; Crest is
  not a numeric equipment replacement; traversal abilities are not carried
  keys; ordinary death is not a full checkpoint rollback.
- Next recorded unit: `GAME-0151` — Monster Hunter Wilds, bounded to one current
  Low Rank hunt route and its weapon, wound, environment and preparation loop.

## Verification notes

- Source reconciliation: official patch and platform material establish the
  maintained systems; community pages supply named route transitions and are
  not promoted to primary evidence.
- Transition trace: `HKS-009` covers valid and invalid Bind, capability gate,
  Crest slot, Bench, Cocoon recovery/replacement and Grand Gate branches.
- Registry checks: generated indexes, corpus validation, Markdown lint, web
  tests, production build and responsive browser smoke are required before
  commit.

## Incremental registry updates

- Registry changes: add nine bounded genes and `COMB-0148`; extend thirteen
  existing-gene evidence lists where their definitions already fit.
- Combination changes: add one strict-subset interaction pattern; do not claim
  independent recurrence.
- Localisation changes: add reviewed Ukrainian game, gene and combination
  presentation plus a complete bilingual plain-language genome.
- Web changes: add bilingual summary, official Team Cherry link, original
  mechanically possible Act 1 gate artwork and responsive variants.
- Decision-log changes: record the scope, exhaustive comparison, rejected
  normalisations and `GAME-0151` as next.

## Missing information

- No authenticated direct-play capture was available; exact animation timing,
  damage values and speedrun-dependent skips are deliberately not claimed.
- The announced Sea of Sorrow release date and mechanics remain outside this
  review and must not silently enter the base-game boundary later.

## Next research subjects

- [Hypothesis | Limited | High] `GAME-0151` — Monster Hunter Wilds.
- [Hypothesis | Limited | High] Re-test the capability/Cocoon/Crest interaction
  against another action-exploration game only after an independently bounded
  candidate enters the plan.
