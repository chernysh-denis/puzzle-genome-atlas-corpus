---
game_id: GAME-0492
slug: resistance-fall-of-man
game_title: "Resistance: Fall of Man"
analysis_status: reviewed
reviewed: 2026-10-04
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-201
    - ACT-202
    - ACT-409
    - ACT-665
  system:
    - SYS-045
    - SYS-051
    - SYS-215
    - SYS-222
    - SYS-292
    - SYS-320
    - SYS-369
    - SYS-578
    - SYS-755
    - SYS-1322
    - SYS-1323
    - SYS-1324
  constraint:
    - CON-282
    - CON-331
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Resistance: Fall of Man — original PS3 A Lone Survivor

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Names, clip sizes, projectile colours, healing quantities, enemy counts and
damage timings are carrier parameters, not new genes.

## Analysis scope

- Version / ruleset: original 2006 English PlayStation 3 single-player
  campaign, ordinary first playthrough on Normal. The bounded target is the
  complete second York chapter, `A Lone Survivor`, as documented by launch-era
  written accounts. It is not Resistance 2, Resistance 3, Burning Skies,
  multiplayer, a later collection or a second-playthrough unlock ruleset.
  No installed executable, disc region hash or exact patch parity is claimed.
  The official 2007 patch announcement lists weapon balance and single-player
  controller changes; it does not prove unchanged campaign instructions.
- Structured analysis target: existing `PLAT-PLAYSTATION-3`; original licensed
  physical PS3 campaign. Other releases and service availability are unassessed.
- Primary decision loop: read local opponents, carried weapons/ammunition and
  four-part health; move, crouch, aim, fire, melee, reload, change weapon, throw
  a frag, launch a Carbine grenade, tag a hostile or hold a Bullseye anchor;
  resolve live attacks and guided shots, collect compatible supplies and
  withdraw long enough to refill only the surviving partial health segment;
  follow the complete ravine/building route, enter and operate the Sabertooth,
  alternate its cannon and machine gun against blockers and cross the final
  road archway to complete the chapter.
- Entry and exit: first ordinary control after the preceding York infection
  scene, following the soldier up the drainage ravine. Reach it through fresh
  Normal campaign `Operation Deliverance`, collecting its ordinary Bullseye
  and retaining the M5A2 Carbine and any unspent frags/launcher ammunition.
  Exact expenditure on that prerequisite is a supplied entry parameter, not
  an invented full-ammo save. Analyse every available response from this entry
  through the leaper groups, ruined buildings and complete tank road to the
  terminal archway, or lethal failure and latest-checkpoint retry. Do not stop
  before the tank to avoid a change of control. Completion exposes `Spires`;
  no action in that successor and no disk-save/relaunch equality is admitted.
- Included: two carried ordinary firearms and their primary/alternate uses,
  finite magazines, compatible reserve/launcher/tag/frag stocks, reload and
  wheel switching without a sequel two-weapon replacement rule; directional
  walking/jump/crouch, scoped zoom as aimed-attack presentation, melee and
  weapon spotlight; enemy movement, leaper close attacks, Hybrids' fire and
  throwable threat, one autonomous allied soldier; cover and local visual
  effects, current mission/intel instructions; finite personal health,
  delayed current-segment-only recovery, yellow-cylinder healing and lethal
  checkpoint retry; tag-hit homing and held ground/surface anchor with orbiting
  shots and a later target tag; vehicle entry/exit and seat authority, live
  tank motion/damage, cannon recovery interval, secondary machine-gun fire,
  destructive fire against eligible roadside structures and anti-tank guns;
  ordered ravine, stairs, broken floors, fire escape and terminal road.
- Excluded: the prior chapter's non-regenerating health phase as current play;
  later Rossmore, Auger, Fareye, LAARK and later grenade acquisition; Reapers
  and other completion-unlocked weapons; Menial grabs and their shake escape
  introduced later, multiplayer shake-off/fire rules, partner commands and
  co-op gunner authority; purchasable progression, whole-campaign completion,
  optional intel/skill-point meta-rewards with no causal chapter gate, cheats,
  intentional exploits, exact native damage/fuse/regen/tag/cannon timings and
  numerical ammunition maxima. Generic all-campaign advice is not a guarantee
  of a pickup, enemy count or weapon in this chapter.
- Potential scoped modules: later weapon/creature encounters, original
  multiplayer, co-op, performed disc/patch identification, save/relaunch
  equality and the sequel rules each need independent evidence and terminals.
- Direct-play status: not conducted. Inspected written accounts of others'
  play and official product/patch descriptions; no PS3, disc, ROM, emulator,
  installed executable, native save, controller trace, screenshot, video or
  audio was used. No original booklet was obtained. Repository transition
  tests express sourced qualitative distinctions, not native execution.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| RF-001 | Insomniac's original Resistance launched with PS3; it is distinct from the sequels in the later collection | Confirmed | Direct | High | P1 |
| RF-002 | The 2007 patch announcement includes weapon balance changes and single-player controller support, without certifying native parity | Observation | Direct | High | P2 |
| RF-003 | Ordinary controls expose movement, crouch, jump, aimed primary/alternate fire, melee, reload, grenade throw, weapon wheel, spotlight and mission inspection | Observation | Corroborated | Medium | S1 controls, S2 weapons, S3 |
| RF-004 | After the infection transition, avoiding damage fills only a still-partly-filled one of four health segments; yellow cylinders heal additional health | Observation | Corroborated | High | S1 A Lone Survivor, S2 health FAQ, S4 |
| RF-005 | M5A2 uses a separate impact-exploding grenade-launcher mode; Bullseye hits a target with a tag before subsequent rounds home toward it | Observation | Corroborated | High | S1 weapons, S2 weapons, S3 |
| RF-006 | Holding a surface/ground tag anchors an orbiting ammunition trap; a later enemy tag redirects remaining shots | Observation | Corroborated | Medium | S1 Bullseye note, S5 |
| RF-007 | Campaign ammunition and tag stocks are finite; multiplayer tag availability is different; exact reserve counting is not admitted | Observation | Corroborated | Medium | S2 weapons, S3, S5 |
| RF-008 | The complete second York chapter passes leaper ravines and Hybrid-held buildings before its tank road | Observation | Corroborated | High | S1 6.01.02, S2 3.c |
| RF-009 | Sabertooth drive and turret aim have separate controls; cannon shots have recovery intervals during which its machine gun remains usable | Observation | Corroborated | Medium | S1 vehicle controls and 6.01.02, S2 3.c |
| RF-010 | The tank can be damaged, attack hostile emplacements and destroy eligible cover; crossing the terminal road arch completes the chapter | Observation | Corroborated | Medium | S1 6.01.02, S2 3.c |
| RF-011 | Live hostile and allied movement/attacks continue; damage, supplies and checkpoint retry affect the route without a universal enemy-count guarantee | Observation | Corroborated | Medium | S1 general tips and York, S2 basics and York |
| RF-012 | No direct play, original manual, exact patch or save-field verification was performed | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Insomniac Games / Sony Computer Entertainment, original
  PlayStation 3 launch-era product, 2006. No unsupported region-day claim.
- Platform or physical form: original English PS3 physical-disc campaign,
  source-bounded fresh Normal second York chapter.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing. All seventeen family definitions were reviewed;
  the three established memberships fit without a one-game family.
- Official sources, accessed 2026-10-04:
  - **P1:** [Insomniac Community Director James Stevenson's official
    retrospective](https://blog.playstation.com/2012/11/20/resistance-collection-lands-on-ps3-december-5th/),
    for first-product/PS3 identity and separation from collection sequels,
    not primary instruction evidence for a particular early encounter.
  - **P2:** [Sony producer's original patch
    announcement](https://blog.playstation.com/2007/10/31/incoming-from-insomniac-resistance-fall-of-man-patch/),
    for the limit on exact native-patch claims.
- Written observation sources, accessed 2026-10-04:
  - **S1:** [Daniel Acaba's own-play written
    guide](https://gamefaqs.gamespot.com/ps3/928399-resistance-fall-of-man/faqs/47473),
    controls, weapons, enemies, general tips, complete first two York chapters
    and the immediately following weapon-acquisition exclusions. Its internal
    history ends 2007-04-04 while the host header reports 2008-02-01. Neither
    is used as an exact executable revision. Later-mode notes are excluded.
  - **S2:** [David Baxley's independent Normal
    walkthrough](https://www.gamerevolution.com/guides/39237-resistance-fall-of-man-faq-walkthrough),
    2006 Version 1.0 statement, basics, M5A2/Bullseye, complete levels 1–2,
    health FAQ and second-playthrough unlock list. This is an independent
    author's observations, not the same guide counted twice.
  - **S3:** [launch-period own-play Resistance
    account](https://threespeech.com/blog/m-200611/),
    inspected indexed passage on controls, weapon selection and conditional
    homing. Full retrieval returned 403; not a manual or sole rule evidence.
  - **S4:** [contemporary GameSpot
    review](https://www.gamespot.com/reviews/resistance-fall-of-man-review/1900-6161706/),
    inspected indexed passage on four-quadrant recovery. Full page retrieval
    was unavailable; the substantive recovery rule is independently read in
    S1 and S2, not established by this passage alone.
  - **S5:** [Bullseye weapon reference, original-game
    section](https://strategywiki.org/wiki/Resistance%3A_Fall_of_Man/Weapons),
    inspected indexed passage on held anchor/retag and multiplayer separation.
    Full retrieval returned 403. S1 independently supplies the anchor rule;
    tag counts and inventory maxima are not native measurements.
- **R1:** this source-reading and repository transition audit. No downloaded
  program, unauthorized game link or execution claim. Literal source names
  are references, not copied passages or newly authored gameplay evidence.
- Claim IDs: RF-001–RF-012.

## Mechanical decomposition

### Action Genes

- Existing: `ACT-008` foot movement/jump; `ACT-161` directly aimed shots,
  melee, launcher fire and aimed tank attacks; `ACT-164` current carried
  weapon choice; `ACT-183` reload; `ACT-184` frag throw; `ACT-201` enter,
  drive/change seat/exit the available tank; `ACT-202` crouch;
  `ACT-409` weapon spotlight toggle, with no unevidenced battery debit.
- New `ACT-665`: direct target tag or held surface anchor, followed by a
  separate firing/retag decision. Aiming alone does not create a guided state.
- Parameters: gun, current mode, target, stance, tag/round/frag stock, direction,
  entered seat, aim and requested reload. Default controller mappings are
  presentation; they do not produce separate genes for every button.
- Claim IDs: RF-003, RF-005–RF-009.

### System Behaviour Genes

- Existing `SYS-045`, `SYS-051`, `SYS-215`: autonomous movement/ally fire and
  direct live combat; `SYS-222`: compatible contact supplies; `SYS-292`:
  thrown grenade flight/collision and transient effect; `SYS-320`: occupied
  tank motion/damage; `SYS-369`: latest checkpoint retry; `SYS-578`: damage,
  compatible yellow-cylinder healing and lethal health loss; `SYS-755`:
  damage-threshold removal of eligible road cover/blockers.
- New `SYS-1322`: quiet recovery stops at the surviving segment boundary,
  not the full four-segment cap. `SYS-737` explicitly excludes this partial
  supply-dependent recovery; `SYS-913` requires a shield distinct from health.
- New `SYS-1323`: accepted target tag redirects subsequent ordinary rounds;
  this is not Elite missile acquisition or universal wall penetration.
- New `SYS-1324`: a held inanimate anchor collects circling shots that can
  later travel toward a new enemy tag. It is not a persistent independently
  aimed automatic turret; exact lifetime, maximum stored shots, surface/air
  anchor equivalence and collision paths are unmeasured.
- Cannon recovery, firing cadence, launcher impact blast and grenade radius
  instantiate existing combat/throw boundaries; no unsupported tank ammunition
  depletion, detailed internal components or fuel management is imposed.
- Claim IDs: RF-004–RF-011.

### Constraint Genes

- `CON-331`: the actual retained weapon-wheel entries, finite compatible
  ammunition/tag/frag capacity and loaded-shot eligibility. Both retained
  ordinary guns remain selectable; no forced two-slot replacement.
- `CON-282`: the ordered route exposes the tank road only after the foot
  section; crossing the final connected arch is the chapter boundary.
- Scarce resources: loaded rounds, reserves, secondary ammunition, carried
  frags and missing full health segments. Partial health recovery is a system
  response, not a paid player healing command or separate shield capacity.
- Claim IDs: RF-004, RF-007–RF-010.

### Information Genes

- `INF-073`: current weapon, selectable wheel and ammunition state;
  `INF-119`: four-part personal health; `INF-115`: local hostile appearance,
  fire, guided paths and anchor confirmation sound, not an omniscient map;
  `INF-125`: Select's current chapter/objective and authored route context.
  No explored-map, enemy-health HUD, tank gauge or future exact enemy roster
  is claimed from a source that does not show it.
- Claim IDs: RF-003–RF-009.

### Objective Genes

- `OBJ-026`: survive the complete connected chapter route and drive through
  its designated final archway. Getting into the tank is not the terminal.
- Failure: zero personal health or a destroyed operated vehicle ends the
  attempt; checkpoint retry replaces the failed transient state. Clearing
  every optional enemy or collecting every intel document is not required.
- Claim IDs: RF-008–RF-011.

### Time Genes

- `TIM-003`: motion, enemies, shots, reload, cannon recovery and quiet
  health recovery advance while ordinary control remains available.
  Exact pause/menu/weapon-wheel time scaling is uninspected and not asserted.
- Claim IDs: RF-003–RF-011.

## Reproducible transitions

These are source-derived tests, not a native play log. Health uses illustrative
unit segments, not original damage-unit values or measured seconds.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Two full segments and a partly filled third remain | Avoid all new damage for the recovery interval | Only the third fills; fourth remains missing | Waiting is not full regeneration | RF-004 |
| Exactly two full segments remain and the other two are empty | Wait without damage | No empty third segment is regenerated | A completely lost segment requires a supply effect | RF-004 |
| Damaged living Hale reaches a yellow cylinder | Collect the compatible healing pickup | It adds health toward the allowed cap beyond the passive partial boundary | Item healing is separate from quiet recovery | RF-004 |
| Tag shot has missed a living target; no held anchor | Fire ordinary rounds | No enemy-target homing is installed by the miss | Aim and acquisition differ | RF-005 |
| A living Hybrid has received the tag | Fire primary Bullseye shots | Subsequent rounds guide toward that tagged target within the weapon's actual limitations | Not automatic all-target accuracy or arbitrary wall penetration | RF-005 |
| A surface tag is maintained by holding the alternate input | Fire primary rounds, then tag a hostile | Shots circle at the anchor, then remaining stored shots follow the new target | Storage and retargeting are not an auto-turret | RF-006 |
| M5A2 primary rounds remain but launcher stock is empty | Request alternate launcher fire | Primary ammunition cannot substitute for launcher ammunition | Compatible typed stocks matter | RF-005, RF-007 |
| Tank cannon has just fired | Request another cannon shot and fire the machine gun during recovery | Cannon must become ready again; the other gun is usable meanwhile | Vehicle weapons have distinct readiness | RF-009 |
| Operated tank faces eligible hostile cover | Apply sufficient cannon damage | The breakable structure ceases to protect its occupant | No universal wall destruction or Auger penetration | RF-010 |
| Tank reaches the final road arch | Cross it after the complete ordered route | A Lone Survivor ends and the next chapter becomes available | The foot section alone is incomplete | RF-008, RF-010 |
| Hale dies before chapter completion | Retry the latest checkpoint | The failed transient route state is replaced | Not permanent preservation of failed damage | RF-011 |

## Strategic and experiential structure

- Local decision: place cover between attacks, choose accurate direct fire or
  pay a tag before guidance, compare reload exposure with weapon switching,
  and choose withdrawal versus item-backed health restoration.
- Medium-term planning: retain compatible secondary stock through leaper and
  Hybrid groups rather than assuming all finite ammo refills automatically.
- Long-term structure: finish one ordered chapter; the tank changes available
  control and weapon cadence, not the game's era, scoring or whole-campaign goal.
- Heuristics: use ranged cover and bursts; separate a partial segment from a
  fully lost one; use the machine gun while the cannon recovers. These are
  sourced suggestions, not requirements that fix one exclusive winning route.
- Failure attribution: zero health, depleted shot type, a tag miss, exposure
  during reload and cannon downtime differ; no measured native hit formula.
- Player-trust factors: readable missing segments and stocked weapon choices
  matter; the original health phase must not be confused with a sequel shield
  or universal full regeneration. No payment/absence-pressure model admitted.
- Claim IDs: RF-003–RF-011.

## Replay and variation

- The route is authored. Expenditure, tag/trap timing, cover, pickup detours,
  surviving ally, tank pace and deaths vary; full enemy placement/AI paths
  and random-seed equivalence were not measured.
- Later difficulty, skill-point hunting and second-playthrough unlocks are
  potential modules, not hidden additions to this first Normal packet.
- Claim IDs: RF-007–RF-012.

## Adjacent systems and history

- The original full carried arsenal and four-segment health differ from
  sequel inventory/recovery designs; no family name proves rule equality.
- Bullseye is not Elite's arm/acquire/fire missile workflow: it attaches a
  marker that guides subsequently spent primary rounds and may anchor them.
- No external novelty or genre-origin claim follows from local first admission.
- Claim IDs: RF-001, RF-004–RF-007, RF-012.

## Normalised genome

Twenty-nine Active uses across all six types; four bounded additions and
twenty-five unchanged transfers. The frontmatter owns the typed signature.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `491` (`GAME-0001`–`GAME-0491`).
- Exact genome matches: none.
- Tied near matches: `GAME-0340` — Halo: Combat Evolved Anniversary (`16 / 41 = 0.390244`).
- Supported combination subsets: none.
- Scan date: 2026-10-04.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0340` Halo: Combat Evolved Anniversary | Direct movement, aimed attack, carried weapon choice, reload, frag throw, crouch, spotlight, live combat, compatible pickups, checkpoint retry, ordered chapters, current gun/health/mission and local-threat disclosure, real-time input | Its remastered first-ship route, shield-before-health and two-slot replacement do not imply Hale's partial-segment recovery, accepted Bullseye tags, stored anchor shots or the complete Sabertooth road; generic shooter control is not full causal equivalence or historical derivation | Tied near: `16 / 41 = 0.390244` |

## Taxonomy impact

- `ACT-665`, `SYS-1322`–`SYS-1324`;
  [TAXONOMY_CHANGE_229](../../../research/taxonomy-changes/TAXONOMY_CHANGE_229.md).
- No earlier canonical signature, combination, release mapping or published
  corpus revision changes. No lexical proposal is automatically accepted.

## Negative results

- No shield gene, full automatic recovery, two-weapon replacement, later
  Auger penetration or invisible universal homing. No waypoint-only endpoint
  before the tank, native booklet claim, measured damage values or exact
  patch/save parity. No novel mechanic is claimed absent from other games.

## Delta summary

## New facts

- [Observation | Corroborated | Medium] The complete second York route includes
  partial-only recovery, both Bullseye tag uses and the tank road; RF-003–RF-011.

## New genes

- [Observation | Corroborated | Medium] Four bounded additions and twenty-five
  unchanged transfers; `TAXONOMY_CHANGE_229`.

## New combinations

- [Observation | Direct | High] No independently recurring combination added.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_229`; no earlier genome
  or production corpus mapping changed.

## New questions

- Identify an original native build and test exact segment boundaries,
  overlapping item healing, tag/trap expiry and collision paths, vehicle
  exposure and checkpoint fields. Reject or revise these qualitative claims
  if those performed tests contradict the independent source accounts.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0493`, original iOS Where's My Water?.
  Different platform and physical cut/water routing, as approved in selection
  038. Begin only after this complete unit's local commit and Goal stop window.
