---
game_id: GAME-0618
slug: shining-force-iii
game_title: Shining Force III
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-014
    - ACT-019
    - ACT-161
    - ACT-652
  system:
    - SYS-299
    - SYS-1814
    - SYS-1815
  constraint:
    - CON-001
    - CON-011
    - CON-269
    - CON-858
  information:
    - INF-119
    - INF-577
  objective:
    - OBJ-029
  time:
    - TIM-001
---

# Game: Shining Force III

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Names, vitality values, movement counts and weapon classes are instances.

## Analysis scope

- Version / ruleset: commercial English North American Sega Saturn
  disc MK-81383, published by Sega of America in 1998. The Western
  title covers Scenario 1. The US instruction booklet and disc record
  identify the target. The recordings show the English first encounter
  with official-localisation characters and mechanics. Neither capture
  independently documents its physical disc, checksum or patch state.
- Primary decision loop: respond to each unit's Agility-influenced
  activation. Inspect highlighted reachable squares and target status.
  Confirm the current unit's position, then choose a valid weapon strike,
  a paid spell on an eligible ally or enemy, another available command,
  or Hold. Let committed effects and interleaved hostile actions resolve.
  Preserve Synbios and incapacitate the complete required monk set.
- Entry: the first central Saraband street encounter beside the church
  and fountain, from the confrontation that switches Search into Battle.
- Exit: the last monk's defeat resolves the battle, the post-battle
  exchange runs and controllable movement returns in Saraband without a
  new battle. Victory itself does not require taking a reward token or
  reaching another square. Synbios at zero HP is the documented defeat
  condition. Withdrawal, replay and its retained state are not part of
  the positive route.
- Included: the engaged opening party, fixed cells, legal placements,
  observed physical strikes and spell choices, weapon class relations,
  active and addressed unit displays, HP and MP changes, observed
  experience and a level gain, defeat boundary and actual clear.
- Excluded: town preparation before the confrontation, next pier battle,
  recruitment, later friendship tiers or promotion, cross-disc transfer,
  later scenarios and the Premium Disc, reissues and fan translations.
  No exact initiative-tie, damage, encounter-drop or reload formula is
  established. The illustrated city readings show zero Land Effect; no
  measured nonzero terrain modifier is attributed to this route.
- Suggested later scope: the separate pier battle with its recruitable
  actor, fleeing NPC and commander-dependent result.

## Direct-play status

No direct play was performed. Sega's North American booklet establishes
the commercial rules vocabulary and turn commands, and physical
cataloguing establishes the US product. NintendoComplete's English
Western playthrough and Zedra Psyborg's English Scenario 1 trace give
independent opening combats and outcomes. The latter also shows a
separate failed attempt and later successful one. Neither verifies the
disc image, region of the capture, save method or absence of all patches.
Only written material and static frames were inspected with no
video or audio playback.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SF3-001 | The target is Sega of America's English MK-81383 commercial release for Sega Saturn. The bounded encounter is the first city fight against the masked monks, before the separate Saraband pier engagement. | Confirmed | Corroborated | High | P1, P2, S1; W1 43:10–43:30, W2 52:40–53:40. |
| SF3-002 | The rules assign individual activations with an Agility-influenced order. Allied and hostile actions can interleave; the player commits each currently active ally's commands locally. | Observation | Corroborated | High | P1 pp. 16–17; W1 43:30–44:30, W2 53:40–55:10 and 62:40–63:30. No exact tie, random modifier or projected full queue is claimed. |
| SF3-003 | The current unit's reachable squares are shown. It chooses or retains a position before the command. The menu can be cancelled back to movement before commitment. Target reach and status are separate from the movement preview. | Observation | Corroborated | High | P1 pp. 16–18; W1 43:30–44:30 and 48:00, W2 54:10–54:40 and 63:00–63:20. |
| SF3-004 | A physical attack resolves against an addressed enemy. Grace's Heal restores a selected ally's HP with MP cost; Masqurin's Blaze spends MP and removes enemy HP. The actor's command completes before further input. An independent trace also shows Dantares gain a level and attributes. | Observation | Corroborated | High | P1 pp. 14 and 16–17; W1 44:10–44:40, 45:50–46:30 and 47:10–47:50, W2 58:10–59:10 and 62:40–63:00. |
| SF3-005 | The booklet describes a weapon-class advantage that modifies damage and special-attack chance. It identifies a visible advantage cue and an independently shown Land Effect readout. City panels commonly show LE 0%; that does not establish any larger terrain bonus or exact strike coefficient here. | Observation | Corroborated | Medium | P1 pp. 19 and 21; S1's scimitar carriers, W1 44:30, 47:50 and 48:00, W2 62:30–62:50. |
| SF3-006 | The city encounter does not finish merely when the tougher monk falls. A 15-HP monk reaches zero in W1, then a 14-HP monk remains targetable. The final observed removal precedes post-battle dialogue and Search movement. | Observation | Corroborated | High | W1 47:50–49:40, W2 63:30–64:20, S1 and S2. P1 describes commander defeat for battles in general. S3 calls the 15-HP monk a boss but does not demonstrate a one-unit victory here. |
| SF3-007 | The manual identifies Synbios losing all HP or retreat as distinct from a successful clearance. The second trace shows its renamed protagonist defeated and a return to the chapel before its successful repeat. | Observation | Corroborated | Medium | P1 p. 16, W2 55:50–57:40. No restoration, checkpoint-retention or save/reload algorithm is inferred. |

## Basic data

- Origin: Camelot / Sonic Software Planning, published in the target
  region by Sega. The commercial disc title omits a scenario suffix.
- Analysis target: `PLAT-SEGA-SATURN`, English North American
  MK-81383, first Saraband street battle in Western Scenario 1.
- Mechanical families: `FAM-009`, choosing placement and a reply
  before hostile movement changes the state, and `FAM-015`, combining
  distinct agent roles within a shared position constraint.
  Final Fantasy Tactics independently illustrates both boundaries.
- Sources checked 21 November 2026.
- P1: [Sega of America retail manual scan](https://bdjogos.com.br/manuais/420-shining-force-iii-sega-saturn-manual-usa.pdf).
  The battle section describes Magic, movement, Hold, Halo cursor,
  order, Land Effect and weapon pairings for the target carrier.
- P2: [Satakore US disc record and box images](https://www.satakore.com/sega-saturn-game,,81383,,Shining-Force-III-USA.html).
  The US commercial case and product identifier distinguish
  the target from the European and Japanese entries.
- W1: [NintendoComplete's English Western playthrough](https://www.youtube.com/watch?v=XnPdZvZJIrg&t=2590s).
  At 43:20 the monk confronts the party by the fountain; 43:30 and
  43:40 show successive active allies. At 43:50 the monk and Dantares
  are in a resolved strike view. At 44:10–44:40 Grace's Heal and
  Masqurin's Blaze are separate commands. At 47:50 Dantares defeats
  the 15-HP monk. At 48:00 another monk is still a legal target.
  At 48:50 Synbios finishes the remaining opponent. Dialogue at
  49:10 and town movement at 49:40 verify the completed encounter.
- W2: [Zedra Psyborg's English Scenario 1 trace](https://www.youtube.com/watch?v=X5GumyoguXo&t=3170s).
  The first fight is underway at 53:40. The renamed leader's defeat
  message is visible at 55:50–56:40. The party returns to the fight
  by 57:40. At 58:10 and 59:10 execution shows different magic
  outcomes. Dantares's level and attributes change at 62:50. The
  dialogue at 63:50 and subsequent chapel visit confirm the successful
  clearance. Exact carrier and settings are not authenticated.
- S1: [Jumesyn Chapter 1 battlefield guide](https://studiowhitewings.com/jumesyn/guide/sc1/chapter1.html).
  Separates the city street and pier, lists four ordinary monks and
  one tougher monk, and identifies the next town sequence.
- S2: [Shining3master's Chapter 1 guide](https://geocities.ws/shining3master/s1c1.html).
  Describes removing all five first-battle monks.
- S3: [constant23's original-era scenario guide](https://gamefaqs.gamespot.com/saturn/198623-shining-force-iii/faqs/5197).
  Identifies the city fight and distinguishes the 14-HP and 15-HP
  roles, but labels the latter a boss without exhibiting the terminal.

## Mechanical decomposition

### Action Genes

- ACT-014: move the currently selected ally to a legal square.
- ACT-019: select the available spell and its eligible position or
  target, including Grace's Heal and Masqurin's Blaze.
- ACT-161: address a reachable hostile with the equipped weapon.
- ACT-652: use Hold to relinquish the combat command, including
  staying on the current square before holding.
- Claim IDs: SF3-002–SF3-005.

### System Behaviour Genes

- SYS-299: action experience can raise unit level and attributes;
  the second trace shows Dantares's increase.
- SYS-1814: schedule allied and hostile activations by Agility
  influence. The current action settles before the next eligible
  participant's own decisions.
- SYS-1815: the directed equipped-weapon classes change eligible
  strikes. The guide's displayed relation is not a hit guarantee.
- Claim IDs: SF3-002, SF3-004, SF3-005.

### Constraint Genes

- CON-001: the square street cells distinguish exact positions.
- CON-011: an occupied endpoint cannot accept another distinct
  combatant. Buildings bound the traversable spaces.
- CON-269: an eligible spell needs its target, current range and
  sufficient MP. Its reach need not match the basic attack's reach.
- CON-858: confirm position before committing a command. Backing
  out of the menu before commitment is not a second resolved move.
- Claim IDs: SF3-002–SF3-005.

### Information Genes

- INF-119: the party panels report level, HP, MP and available magic.
- INF-577: read reachable tiles, local target, Land Effect and the
  weapon relation cue without treating them as a full initiative list.
- Claim IDs: SF3-003–SF3-005.

### Objective Genes

- OBJ-029: incapacitate the complete required finite hostile set
  while keeping Synbios viable. The observed return to Search
  verifies the win rather than another objective.
- Claim IDs: SF3-006, SF3-007.

### Time Genes

- TIM-001: a discrete command resolves HP, MP, removal and any
  reward before subsequent input. This does not imply a side-wide
  plan or any real-time command deadline.
- Claim IDs: SF3-002–SF3-004.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| The party is approaching the central city confrontation | Advance the confrontation | Battle takes over and shows the first active ally | The street fight is separate from town Search | SF3-001, SF3-002 |
| An ally has an individual activation | Inspect the field and choose a highlighted legal endpoint | The command choices apply from that position | Reachable movement and eligible targets are distinct | SF3-003 |
| An injured ally is reachable and Grace has MP | Choose Heal and the ally | The ally regains HP and the casting resource is spent | A modest position change can enable support instead of a strike | SF3-004 |
| Masqurin has sufficient MP and a valid monk target | Commit Blaze | The enemy loses HP and the cast resource is debited | Local ability resolution differs from ordinary armed attack | SF3-004 |
| A 15-HP monk and another monk are still in the encounter | Defeat the tougher monk | The remaining opponent stays actionable and the battle continues | A named boss label alone does not settle this first battle | SF3-006 |
| The last required monk remains | Resolve the final damaging action | The party's conversation follows, then town movement resumes | The actual terminal belongs to the complete finite set | SF3-006 |
| Synbios is reduced to zero HP in the alternative attempt | Resolve the hostile hit and acknowledge defeat | The encounter ends as a failure and the party is shown back at the chapel | Defeat and the successful Search return are distinct | SF3-007 |

## Strategic and experiential structure

Each ally answers from its actual place in the order. A placement for
healing or magic preserves options through a monk's intervening action.
Terrain and weapon properties inform a legal move or command without
guaranteeing a hit. Clearing the complete required set is a different
condition from defeating the opponent with the most HP.
SF3-002–SF3-007.

## Replay and variation

The traces use different command orders and duration. The second includes
a defeat and return to the area before it succeeds. The repeated successful
boundary is ordinary town control after the required monks are gone.
The sources do not establish restart retention, complete encounter
seeding, or an exact initiative order for every run.

## Adjacent systems and history

The Western commercial release is the first scenario and has its own
English presentation. The later pier encounter has different objectives,
actors and local events. Its recruitments, commander and sequel save
effects are outside the first city's decision loop.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-014, ACT-019, ACT-161, ACT-652 | Place, cast, strike or hold |
| System Behaviour | SYS-299, SYS-1814, SYS-1815 | Advance experience, schedule individual activations and modify weapon strikes |
| Constraint | CON-001, CON-011, CON-269, CON-858 | Fixed spaces, exclusive occupancy, spell eligibility and movement before the command |
| Information | INF-119, INF-577 | Read resources and known local field and target properties |
| Objective | OBJ-029 | Resolve the complete required hostile set while the leader is viable |
| Time | TIM-001 | Settle each discrete command before further input |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `617` (`GAME-0001`–`GAME-0617`).
- Exact genome matches: none.
- Tied near matches: `GAME-0486` — Final Fantasy Tactics (`10 / 31 = 0.322581`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Final Fantasy Tactics (GAME-0486)](../a-f/final-fantasy-tactics.md) | ACT-014, ACT-019, ACT-652, CON-001, CON-011, CON-269, INF-119, OBJ-029, SYS-299, TIM-001 | Both position individual units, allow an unused action, gate abilities by resources and target, and defeat a finite required set. Final Fantasy Tactics permits either Move or Act first and models Speed-fed CT, chosen facing and fallen countdowns. Shining Force III requires a position decision before committing the action, orders activations by Agility and applies directed equipped-weapon matchups. | Near, `0.322581` |

## Taxonomy impact

- [TAXONOMY_CHANGE_364](../../../research/taxonomy-changes/TAXONOMY_CHANGE_364.md)
  distinguishes Agility-influenced activations, move confirmation,
  directed weapon-class modifiers and the local tactical display.

## Negative results

- SYS-356 requires an exposed upcoming initiative sequence. The
  observed current actor and the documented cursor's next-character
  hop do not establish a whole queue. SYS-1305 commits a complete
  party batch before resolving initiative; individual inputs here
  are already settled as the order advances.
- Into the Breach's CON-034 governs a side-wide phase. Final Fantasy
  Tactics' CON-752 permits acting before relocating. These boundaries
  do not replace the early Shining Force III move stage.
- Neither a post-battle map pickup nor a required physical exit
  is observed. The game resumes the original street.
- The visible LE 0% does not identify nonzero damage reduction at any
  unobserved terrain. The second battle's recruitments are separate.

## Delta summary

## New facts

- [Observation | Corroborated | High] Agility-influenced individual
  turns allocate placement before a local resolved action. SF3-002–SF3-004.
- [Observation | Corroborated | High] The first city encounter
  continues after the tougher monk falls and later returns to town
  Search after the last required opponent. SF3-006.

## New genes

- [Observation | Corroborated | Medium] SYS-1814, SYS-1815,
  CON-858 and INF-577.

## New combinations

- [Observation | Direct | High] No new combination admitted.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_364.

## New questions

- How does the original carrier settle an exact Agility tie?
- When and how do nonzero Land Effect and the weapon relation interact?
- Which parts of the first attempt can persist through a deliberate
  withdrawal under authenticated retail settings?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0619`, Donkey Kong Bananza,
  commercial Nintendo Switch 2 base game. Trace a changed terrain route
  through intentional excavation and a verified reward or exit.

## Why this game

- [Hypothesis | Limited | Medium] Saraband's walls constrain the
  fixed tactical board. An evidenced Bananza route can isolate
  directly changing that geometry to make an approach available.
