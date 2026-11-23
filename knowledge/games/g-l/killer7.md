---
game_id: GAME-0627
slug: killer7
game_title: "Killer7"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-161
    - ACT-832
    - ACT-833
    - ACT-834
  system:
    - SYS-1828
  constraint: []
  information:
    - INF-179
    - INF-582
  objective:
    - OBJ-029
  time:
    - TIM-003
---

# Game: Killer7

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The corridor, actor and difficulty identify the observed packet.

## Analysis scope

- Version / ruleset: English North American retail Nintendo GameCube release,
  DOL-GK7E-USA, July 7, 2005. New Game on Deadly. The recording identifies
  the NTSC GK7E edition and shows Deadly being selected. Exact disc revision
  and controller timing are unverified.
- Primary decision loop: follow a local route as Dan, stop for a nearby
  concealed threat, take the stationary first-person stance and scan. Aim at
  the revealed enemy, reload as needed and settle the encounter. Restore
  traversal and continue to the next junction.
- Entry: the first live hall encounter in Target 00: Angel after the
  opening Iwazaru warning and before the next assistance exchange.
  The earlier Garcian control lesson is setup rather than a live enemy
  encounter in this packet.
- Exit: the first Heaven Smile is gone and Dan has resumed the corridor
  route to the next Hallway / Iwazaru junction. Stop before another fight.
- Included: hold-to-advance route traversal and junction choice, a separate
  reversal, stationary combat stance, the source-reported sound warning,
  local scan, aimed ordinary attack, manual reload, live approach and
  return to traversal.
- Excluded: Normal's automatic critical-point indicators; optional
  close-range lock, upgrades, blood use, reserve economy outside this
  encounter, persona changes after the scoped entry, saving, death recovery,
  later corridor enemies,
  the parking encounter, bosses, later missions and other editions.
- Suggested later scope: compare the same first encounter in Normal using
  the visible weak point, with a separately authenticated trace.

## Direct-play status

No direct play was performed. The original Capcom GameCube booklet names
the controls, scan restriction and Deadly cue difference. The NTSC author
identifies GK7E. Static frames show the labelled selection, live enemy,
reload, visible defeat and restored route. A different regional recording
and two published firsthand routes corroborate the encounter context. No audio
was played or evaluated. The laugh is a reported in-game cue. Exact input
timings, installed disc revision, hit counts and the loss/retry branch
were not verified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| K7-001 | The target is the English North American GameCube retail release. The capture starts a new game on Deadly, which does not automatically show the enemy's critical point. | Confirmed | Corroborated | High | P1 printed pp. 14–15; C1 and C2; W1 1:00–1:20. The exact disc revision is not assigned. |
| K7-002 | Ordinary traversal advances along a laid-out segment while the advance control is held. A different action reverses travel. A reached junction gives a labelled branch choice. | Observation | Corroborated | High | P1 pp. 16–19; W1 6:30–6:40 and 7:00; R1 controls. |
| K7-003 | Holding the ready input changes ordinary third-person route control to stationary first-person combat. Stick aiming and the ordinary shot are available in that stance. Releasing the input allows route movement again. | Observation | Corroborated | High | P1 pp. 16–19; W1 6:40–7:00; R1 and R3. The recording is not a physical input trace. |
| K7-004 | Approaching Heaven Smiles are optically concealed. Firsthand accounts report laughter before a clean visual target. A separate scan in combat view reveals the present enemy and makes it eligible for an ordinary shot. | Observation | Corroborated | High | P1 pp. 18–19; W1 6:40–6:42 and R2–R3. Audio was not sampled. |
| K7-005 | The first threat can be neutralised using ordinary aimed fire on Deadly without displaying a Normal-mode critical marker. It can advance during the confrontation. The manual describes a dangerous close outcome, not an observed hit on Dan in this attempt. | Observation | Corroborated | High | P1 pp. 14–15 and 18–19; W1 6:42–6:58 shows aimed fire and the enemy dissolving; R2; W2 5:20–5:40 corroborates the setting. |
| K7-006 | Dan resumes traversal after the first enemy is resolved and reaches the next Hallway / Iwazaru choice. This is a local finish before the subsequent hostile. No formal encounter-clear screen or newly unlocked route is required to establish the observed return. | Observation | Corroborated | High | W1 6:57–7:02; R1 and R2 identify the continuation along the corridor before the next enemy; W2 5:20–5:50. |
| K7-007 | The active weapon is manually reloaded while the first enemy is still approaching. Ordinary aiming resumes against that same target. In the documented GameCube rules a refill costs readiness time without drawing from a finite carried ammo count. | Observation | Corroborated | High | W1 6:53–6:56 displays Reload between live aim states. P1 p. 18 establishes the manual refill and movement restriction. R4 describes the unbounded ammunition model. |

## Basic data

- Analysis target: `PLAT-NINTENDO-GAMECUBE`.
- Developer: Grasshopper Manufacture. Publisher: Capcom.
- Mechanical family: `FAM-014`, world topology and perspective.
- Checked: 2026-11-21.
- P1: [Original Capcom GameCube instruction booklet](https://www.fichier-pdf.fr/2016/04/08/killer7-manual-gc/killer7-manual-gc.pdf),
  printed pp. 14–19, Game Rules, Controller Layout and Actions.
- P2: [Nintendo's original GameCube product entry](https://www.nintendo.com/en-gb/Games/Nintendo-GameCube/Killer-7-268203.html).
  This official regional listing establishes the platform, not the US date.
- C1: [North American retail identification](https://gamefaqs.gamespot.com/gamecube/562551-killer7/data).
- C2: [North American physical release index](https://ogdb.eu/index.php?gameid=10687&section=game),
  for the stated disc family and July 7 date.
- W1: [Seahawk0027's GK7E NTSC Deadly recording](https://www.youtube.com/watch?v=2_miUTFIPf8&t=380s).
  The menu selects Deadly at 1:10. Video-only frames at one-second
  intervals show the Elevator Hall title by 6:38, the scan near 6:41,
  reload at 6:54–6:55, a visibly disintegrating defeated Smile by
  6:57–6:58 and the resumed Hallway branch by 7:00.
- W2: [DeShelly's PAL GameCube opening](https://www.youtube.com/watch?v=oXu8aiASr6E&t=316s),
  hosted by LongplayArchive. It corroborates the room sequence,
  not the North American difficulty settings or damage values.
- R1: [Aegison's release-era GameCube controls and Angel route](https://gamefaqs.gamespot.com/gamecube/562551-killer7/faqs/37829).
- R2: [Forweg's GameCube route](https://gamefaqs.gamespot.com/gamecube/562551-killer7/faqs/45693),
  opening Elevator Hall sequence and fighting notes.
- R3: [Release-era GameCube play account](https://gamefaqs.gamespot.com/gamecube/562551-killer7/reviews/99458)
  and [GameSpot's contemporary difficulty walkthrough](https://www.gamespot.com/articles/killer7-walkthrough/1100-6129060/).
  The accounts distinguish the sound warning, reveal and mode-specific marks.
- R4: [Contemporaneous GameCube reload account](https://gamefaqs.gamespot.com/gamecube/562551-killer7/reviews/90217),
  describes manual reload, the brief camera change and unbounded ammo.

## Mechanical decomposition

### Action Genes

- ACT-161: aim and commit ordinary fire at the revealed local enemy.
- ACT-832: hold advance on the current segment, reverse or choose a
  labelled path at a reached junction.
- ACT-833: hold for stationary first-person combat and release to
  resume the route controls.
- ACT-834: refill the active weapon without inventory expenditure, at the
  cost of a brief loss of readiness while the foe remains active.

### System Behaviour Genes

- SYS-1828: scan the combat view to make an existing concealed hostile
  visible and eligible for ordinary aimed damage.

### Constraint Genes

No new constraint is needed. The ordinary shot's reveal requirement is
part of SYS-1828. The mode's control restriction belongs to ACT-833.

### Information Genes

- INF-179: the traversal view exposes the current scene, NPC choices
  and local exits.
- INF-582: the reported laugh signals an already nearby enemy without
  reliably disclosing its exact aim position.

### Objective Genes

- OBJ-029: neutralise the first required threat of this scoped
  encounter and demonstrate that Dan can continue.

### Time Genes

- TIM-003: the threat can approach while stance, scan and attack
  choices are made. No exact warning window or timer is measured.

## Reproducible transitions

| State | Input or event | Result | Evidence |
| --- | --- | --- | --- |
| Dan has the authored corridor route | Advance along the segment or choose a shown branch | Player-directed traversal proceeds on the selected route | K7-002 |
| A nearby concealed foe is present | Hold the ready control | View changes to stationary first-person combat | K7-003, K7-004 |
| The target is not an ordinary hittable silhouette | Issue the scan in the current view | The present enemy becomes visible and eligible for an aimed shot | K7-004 |
| The first Smile is revealed | Commit ordinary aimed fire | Aimed attacks affect the visible threat | K7-005 |
| Reload is requested during combat | Wait for the reload to complete | Readiness returns against the same still-present target | K7-007 |
| The final aimed attack hits | Let the attack settle | The first threat disintegrates and is removed | K7-005 |
| The encounter is resolved | Release the ready control and continue | The third-person traversal reaches the following Hallway / Iwazaru junction | K7-006 |

## Strategic and experiential structure

Traversal and combat use distinct control states at the same local
position. The warning has enough information to interrupt movement
without saying precisely where to shoot. The scan changes which
hostiles are visible and hittable. A reload gives up a moment of fire readiness without spending a finite reserve.
After the resolution, the player resumes navigation.
There is no campaign completion or special reward required at this boundary.

## Replay and variation

The NTSC Deadly and separately attributed PAL openings show the same
corridor layout and return to travel. They do not establish shared
numerical attack outcomes. Capcom's mode descriptions distinguish
automatic exposure of critical points in Normal, which is not part
of the verified Deadly packet. The exact scan duration and repeated
spawn behaviour during backtracking were not tested.

## Adjacent systems and history

The printed booklet also describes close-range lock, persona
abilities and separate recovery. None is required to identify the
observed loop. The later parking chamber introduces different enemy
and route conditions. The PlayStation 2 and later PC releases do not
supply input or difficulty evidence for this GameCube record.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-161, ACT-832, ACT-833, ACT-834 | Aim and fire, move by routes, hold a combat stance and manually reload |
| System Behaviour | SYS-1828 | Expose the concealed local hostile for ordinary damage |
| Constraint | None | Reveal and mode predicates remain in their owning rules |
| Information | INF-179, INF-582 | See local choices and receive a reported warning of a concealed threat |
| Objective | OBJ-029 | Resolve the first bounded threat before continuing |
| Time | TIM-003 | Respond to live hostile approach |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `626` (`GAME-0001`–`GAME-0626`).
- Exact genome matches: none.
- Tied near matches: `GAME-0550` — Ghost of Yōtei (`3 / 15 = 0.200000`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Ghost of Yōtei (GAME-0550)](ghost-of-yotei.md) | ACT-161, OBJ-029, TIM-003 | Both use directed attacks against a finite living threat under real-time pressure and establish continuation after it is resolved. Ghost of Yōtei reads the visible Snake and alternates sustained guard with openings for sword strikes. Killer7 first interrupts held route movement for a stationary view, reveals the approaching opponent and resumes the corridor after the fight. | Near, `0.200000` |

## Taxonomy impact

[TAXONOMY_CHANGE_373](../../../research/taxonomy-changes/TAXONOMY_CHANGE_373.md)
separates path control, ready stance, scan and warning.

## Negative results

- ACT-530 commits a board junction with remaining die-counted movement.
  There is no roll allowance in the local hold-to-run rule.
- ACT-823 toggles retained fixed or mobile firing forms. Deadly uses
  a temporary stance with route movement unavailable in it.
- ACT-183 transfers from reserve ammunition into a magazine. The local
  refill here has a readiness cost but no limited inventory supply.
- INF-538 reads attributes from a selected enemy in a learned scan.
  SYS-1828 exposes the target itself and changes attack eligibility.
- The evidence does not justify a Normal-mode one-hit critical,
  a universal round terminal or a permanently unlocked passage.

## Delta summary

Adds the North American Deadly first corridor encounter from local
route movement through the reveal, actual resolution and returned movement.

## New facts

- The ready hold separates stationary first-person aim from route travel.
- A concealed active threat needs a local scan before ordinary hits.
- The first resolved threat is followed by an ordinary route choice.

## New genes

ACT-832, ACT-833, ACT-834, SYS-1828 and INF-582.

## New combinations

None.

## Taxonomy changes

[TAXONOMY_CHANGE_373](../../../research/taxonomy-changes/TAXONOMY_CHANGE_373.md).

## New questions

How does the same first encounter differ when Normal shows a critical
point after revealing the target?

## Next recommended game

Continue with Keep Driving on Windows Steam and its first evidenced
settled road event through actual resumed travel.

## Why this game

The same stretch of hallway supports two clearly different control
states. The first threat ties a warning, an explicit reveal and an
aimed response to the return to ordinary navigation.
