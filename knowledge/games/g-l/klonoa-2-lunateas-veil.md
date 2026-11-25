---
game_id: GAME-0692
slug: klonoa-2-lunateas-veil
game_title: "Klonoa 2: Lunatea's Veil"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-911
  system:
    - SYS-036
    - SYS-037
    - SYS-045
    - SYS-1966
  constraint: []
  information:
    - INF-192
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Klonoa 2: Lunatea's Veil

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
A nearby wandering enemy can become the single carried resource
that makes a high landing possible.

## Analysis scope

- Version / ruleset: original English North American Namco
  PlayStation 2 retail edition, SLUS-20151, July 2001. Use solo
  Klonoa in Sea of Tears: The Encounter. The recorded NTSC
  disc serial, press and executable were not independently verified.
- Structured analysis target: PLAT-PLAYSTATION-2 in
  [platform coverage](../../platforms/games.json).
- Entry: the first high ledge after the rope bridge. Begin at
  Popka's first Double Jump lesson, with the ordinary red Moo
  still active on the lower approach.
- Primary decision loop: read the ledge and the Moo's position,
  approach and hit it with a Wind Bullet, preserve the held
  enemy through takeoff, and spend it with another jump input
  while airborne. Steer onto the raised surface.
- Positive terminal: Klonoa lands and can proceed along the
  upper stone bridge. Its nearby star and Dream Stones can be
  collected on contact. The first subsequent whirlwind is
  outside this fixture.
- Failure and restart: a missed Wind Bullet leaves no cargo for
  a carried-enemy jump. An ordinary throw clears that same
  held enemy, requiring another capture to use the boost.
  The booklet documents unavailable ear hover while carrying.
  The two successful traces do not establish pit-loss, enemy
  respawn or checkpoint restoration.
- Included: lateral route movement and support, the local
  wandering Moo, Wind Bullet capture, the held body, the
  airborne release and ascent, the documented alternate throw
  and the visible contact pickups after landing.
- Excluded: the earlier bridge as a traversal objective, exact
  pulse range, impulses, collision coefficients, object spawn
  timers, alternate enemy types, directional throws into depth
  as a separate path, the next whirlwind, cave, bonus routes,
  two-player Popka, whole-Vision settlement, demos and remasters.
- Potential scoped module: use the original retail build to
  test a forward toss at this same ledge and document return
  or depletion of its local Moo.
- Direct-play status: no personal console session, disc inspection
  or input telemetry. W1 identifies NTSC PS2. W2 identifies
  original console hardware; its region is unverified.
  Both were examined as short background frame sequences without audio.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| KLV-001 | Namco's original release is a 2001 PS2 title. North American packaging and catalogue identify SLUS-20151. Neither capture establishes an exact disc press. | Confirmed | Corroborated | High | P1, P2, D1, W1, W2 |
| KLV-002 | Popka identifies the first high ledge and directs the player to capture the nearby Moo and jump again in the air. The Moo moves along the lower approach before capture. | Observation | Corroborated | High | W1 6:20–7:05, W2 5:31–5:52, H1 |
| KLV-003 | A short ring pulse hits the ordinary Moo. It visibly enlarges and moves into a hold above Klonoa, persisting into the first ascent. | Observation | Corroborated | High | P1 pp. 18–21, W1 7:05–7:06, W2 5:51–5:53 |
| KLV-004 | The held Moo moves downward as Klonoa gains height and reaches the upper surface. The avatar then continues along the bridge without the Moo. Both recordings show contact pickup on that route. | Observation | Corroborated | High | P1 pp. 20–21, W1 7:06–7:09, W2 5:53–5:56 |
| KLV-005 | The booklet separately specifies throwing the held enemy with the attack command and expelling it downward with a second jump. The holding state prevents an ear hover. The example crossing uses the downward branch. | Confirmed | Direct | High | P1 pp. 18–21, W1 7:05–7:09, W2 5:51–5:56 |

## Basic data

- Release / origin: Namco, English North American PlayStation 2
  retail disc SLUS-20151, July 2001. Catalogue entries differ on
  the exact calendar day, which is not needed to identify the ruleset.
- Mechanical families: FAM-007 for the visible supported-to-airborne
  transition and height change; FAM-010 for committing the extra
  action while the player is already airborne in live local play.
- P1: [Original North American Namco booklet scan](https://www.scribd.com/document/1058223712/Klonoa-2-Lunatea-s-Veil).
  Printed pp. 18–21 distinguish hover, Wind Bullet acquisition, a
  directed throw and the airborne Double Jump. Page 34 identifies
  the ordinary Moo. The scan carries the North American NTSC U/C
  designation.
- P2: [Bandai Namco's PS2 retrospective and remaster comparison](https://en.bandainamcoent.eu/klonoa/news/klonoa-phantasy-reverie-series-shows-graphics-improvement-catchy-trailer).
  The publisher identifies the original 2001 PlayStation 2 release.
  The remaster footage is outside this fixture.
- D1: [North American disc catalogue and packaging](https://psxdatacenter.com/psx2/games2/SLUS-20151.html)
  and [US release listing](https://gamefaqs.gamespot.com/ps2/374317-klonoa-2-lunateas-veil/data).
  Both identify SLUS-20151 and July 2001.
- W1: [LongplayArchive's NTSC PS2 recording](https://www.youtube.com/watch?v=-MQVNpa9Cwo&t=380s).
  Use 6:20–7:09 for Popka's instruction and the observed crossing.
- W2: [10min Gameplay's original PlayStation 2 recording](https://www.youtube.com/watch?v=vDbeu5tosT4&t=331s).
  Use 5:31–5:56 for the same instruction and a complete crossing.
  The author identifies original hardware and a post-capture upscale.
- H1: [Raging_DemonTEN's original PS2 route account](https://gamefaqs.gamespot.com/ps2/374317-klonoa-2-lunateas-veil/faqs/14435).
  Locates the first star on the Double Jump lesson's ledge in Sea of Tears.
- Claim IDs: KLV-001–KLV-005.

### Reproducible fixture evidence

1. Walk up from the first rope bridge until Popka points out
   the high ledge. Note the authored lesson about the ordinary
   Moo and the second input. W1 6:20–7:04; W2 5:31–5:50.
2. Once normal control returns, face the Moo on the lower
   shelf and fire a Wind Bullet from short reach. The ring
   effect makes contact and the inflated Moo comes overhead.
   W1 approximately 7:05.3–7:06.0; W2 5:51.7–5:52.7.
3. Jump while holding the Moo, then press jump again in the
   air. The Moo is ejected below as Klonoa rises above the
   high shelf. W1 approximately 7:06.0–7:06.7; W2 5:52.7–5:53.3.
4. Guide Klonoa onto the higher bridge. Read the gold star
   presentation and optional green Dream Stones on contact.
   Stop at the supported upper route before the whirlwind.
   W1 7:07–7:09; W2 5:54–5:56.
5. To separate the two possible uses, the original booklet
   describes pressing the attack command again while the Moo
   is held. That spends the same cargo on a throw and leaves
   the airborne boost unavailable without another captive.

## Mechanical decomposition

### Action Genes

- ACT-008: steer and jump along the lower approach and upper
  stone path. KLV-002–KLV-004.
- ACT-911: direct the Wind Bullet at an eligible moving Moo.
  Contact turns the target into a distinct overhead load.
  KLV-003.

### System Behaviour Genes

- SYS-036: the supported approach, jump trajectory, downward
  release and landing each use different motion and support
  states in the same live space. KLV-003–KLV-004.
- SYS-037: contact on the upper route credits the star and
  Dream Stones as Klonoa proceeds. KLV-004.
- SYS-045: the uncaptured ordinary Moo moves along the
  approach before the capture. KLV-002–KLV-003.
- SYS-1966: the second airborne jump input spends the carried
  Moo downward for upward motion. A normal throw spends the
  same held body along its directed path under the published
  rules. KLV-004–KLV-005.

### Constraint Genes

No separate constraint gene is required. The eligible target
and the mutually exclusive use of one retained body are already
part of the admitted capture and release boundaries.

### Information Genes

- INF-192: the side view shows the lower support, target,
  upper edge and later bridge only as the route opens.
  KLV-002–KLV-004.

### Objective Genes

- OBJ-026: use the extra height to make the declared first
  ledge reachable and arrive on its supported upper path.
  KLV-002–KLV-004.

### Time Genes

- TIM-003: acquisition and the jump inputs occur against live
  enemy movement and airborne progression. KLV-002–KLV-004.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Lower shelf with an uncaptured ordinary Moo | Face it and land the Wind Bullet | One inflated Moo held overhead | KLV-002–KLV-003 |
| Supported with the Moo held | Take the first jump | Airborne with the same Moo still held | KLV-003–KLV-004 |
| Airborne with the Moo held | Commit another jump input | Moo ejected below; Klonoa rises and is empty-handed | KLV-004 |
| Held Moo, before spending it on an ascent | Use the booklet's normal throw command | Directed release with no jump impulse; the held body is gone | KLV-005 |
| Elevated and approaching the ledge | Steer and make supported contact | Ordinary upper-route traversal, with optional contact pickups | KLV-004 |

## Strategic and experiential structure

The same red Moo is a moving obstacle before acquisition and a
consumable movement option afterward. The high ledge makes
retaining that option until midair useful. A horizontal throw
can solve an attack problem while forfeiting the immediate lift.

## Replay and variation

Both records acquire the Moo and spend it downward before the
upper landing. Their camera and pickup timing differ. The
captured route does not independently test which landing,
restart or offscreen movement conditions regenerate the local Moo.

## Adjacent systems and history

The original title later adds enemies with different carried
effects and separate board-riding stages. The first ledge
demonstrates an ordinary Moo and the solo base action only.
The 2022 collection is a different product.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-911 | Direct travel and contact capture through a directed pulse |
| System Behaviour | SYS-036, SYS-037, SYS-045, SYS-1966 | Support, pickups, active enemy movement and shared carried-body expenditure |
| Constraint | None | Target and release conditions remain part of the admitted rules |
| Information | INF-192 | See support, enemy and high edge in the live side view |
| Objective | OBJ-026 | Arrive on the designated upper route |
| Time | TIM-003 | Act while the Moo and jump continue moving |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `691` (`GAME-0001`–`GAME-0691`).
- Exact genome matches: none.
- Tied near matches: `GAME-0312` — ASTRO BOT (`6 / 19 = 0.315789`); `GAME-0389` — Mega Man 2 (`6 / 19 = 0.315789`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [ASTRO BOT (GAME-0312)](../a-f/astro-bot.md) | ACT-008, INF-192, SYS-036, SYS-037, SYS-045, TIM-003 | Both use live platforming, local camera exposure and contact pickups. ASTRO BOT uses a retained extension capability on the Sky Garden route. Klonoa spends the captured Moo to gain height once. | Near, `0.315789` |
| [Mega Man 2 (GAME-0389)](../m-r/mega-man-2.md) | ACT-008, INF-192, SYS-036, SYS-037, SYS-045, TIM-003 | Both time directly steered jumps around autonomous enemies and contact pickups. Metal Man's stage uses projectile combat and mechanical hazards. Klonoa captures and expels the enemy itself to reach the ledge. | Near, `0.315789` |

## Taxonomy impact

ACT-911 isolates a directed pulse producing temporary physical
carry rather than an inert pickup or acquired roster member.
SYS-1966 distinguishes object expenditure from an extra jump
whose availability returns on grounded support.

## Negative results

- Capturing the Moo does not itself increase the jump height.
  The second jump input spends the captured body.
- The ordinary throw spends the same body. It is not a second
  independent charge of propulsion.
- Hover while holding it is unavailable under the booklet rule.
- The first upper-route pickups do not establish any whole-Vision
  completion threshold.

## Delta summary

Nine genes, including new boundaries for pulse-to-carry capture
and alternative releases of the same captured enemy.

## New facts

- Ordinary Moo capture leaves a visible load carried through takeoff.
- The single body can supply either a downward release for lift
  or a separate directed throw.
- Both traces reach supported traversal above the first ledge and
  show the nearby contact pickups.

## Principles and design implications

Using an enemy as a local resource ties acquisition to the
position of the intended obstacle. A shared spend makes a
combat-use decision affect immediate traversal options.

## Puzzle or game generation potential

Build an original room around a walking energy seed, a side
target and a high platform. An acquired seed can be thrown
at the target or dropped for lift, with only one seed carried
at a time. Vary the available replenishment deliberately.

## New genes

- ACT-911
- SYS-1966

## New combinations

None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 438](../../../research/taxonomy-changes/TAXONOMY_CHANGE_438.md).

## New questions

- What restores the local Moo after throwing it away under the
  North American retail rules?
- Which additional enemy classes supply different motion under
  the same release input?

## Next recommended game

Continue Selection 059 with `GAME-0693`, Void Stranger on the
commercial English Windows Steam release.

## Why this game

The first taught ledge shows one enemy changing from autonomous
obstacle to a temporary carried movement option.
