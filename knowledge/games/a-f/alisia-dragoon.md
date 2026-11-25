---
game_id: GAME-0719
slug: alisia-dragoon
game_title: "Alisia Dragoon"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-295
    - ACT-935
  system:
    - SYS-037
    - SYS-407
    - SYS-1365
    - SYS-2012
    - SYS-2013
  constraint:
    - CON-901
  information:
    - INF-192
    - INF-651
  objective:
    - OBJ-029
  time:
    - TIM-003
    - TIM-046
---

# Game: Alisia Dragoon — original Genesis Stage 1

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Individual buttons, meter ticks, enemy art and companion names identify instances.

## Analysis scope

- Version / ruleset: North American English Sega Genesis commercial
  cartridge, 1992. Use a fresh Normal game and the three-button control
  layout. The primary original-game recording identifies the US
  version and visibly selects Type 4. The corroborating Genesis
  recording shows Normal with Type 1. Exact ROM revision, cartridge
  serial, emulator and physical input trace are unverified.
- Structured analysis target: `PLAT-SEGA-GENESIS`. Start at the first
  player-controlled frame of Stage 1, traverse the forest approach,
  sealed temple and quarry, then defeat the twin opponents and reach
  ordinary control in Stage 2 near 09:54. The Stage 2 fight is outside the fixture.
- Primary decision loop: face the next threat and cast a lightning
  burst that finds targets ahead. Stop casting to restore the meter.
  Wait for the flashing full gauge when enemies are on both sides.
  Change the one autonomous helper with the selection overlay.
  Read the two status panels and cross the remaining platforms
  to defeat both twins.
- Included: direct locomotion, jumps and crouching, player-controlled
  casts, forward target acquisition, the restoring attack reserve,
  the full-charge rolling bolt, optional helper replacement, its
  separate autonomous attacks, contact item collection, sight,
  the dual HUD, live-time and selector states, and the first stage clear.
- Excluded: the title attract run, mappings inferred from a silent
  video alone, exact aim envelope, rates and damage, all secret
  placements and rankings, pause menu as a separate mechanic,
  death and continue state, observed revival, later stages,
  Japanese regional parameters, Genesis Mini system functions,
  Switch Online, cheats and save states.
- Direct-play status: no personal Genesis or emulator session,
  cartridge inspection, executable trace, direct input recording
  or frame-count measurement. The original retail instructions
  and Game Arts history support the product and rules. Two
  original-game recordings show the first stage. Only background
  silent stills and bounded video-only windows were examined.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| AD-001 | The commercial Genesis game has Normal and Hard, four controller mappings, and separate Monster Select, Thunder and Jump commands. W1 uses Normal and Type 4, W2 Normal and Type 1. | Observation | Corroborated | High | P1, P2; W1 00:58–01:04; W2 01:49–01:55 |
| AD-002 | An ordinary cast automatically bends to eligible forward targets while the avatar can move or jump. Turning changes the eligible side. Exact range and priority remain unmeasured. | Observation | Corroborated | High | P1 Options; P3 attack pages; W1 02:26–02:29 and 02:51; W2 09:03–09:07 |
| AD-003 | Continued attack spends the Thunder Power gauge, which replenishes without casting. A usable partial charge supports ordinary lightning and an empty reserve cannot sustain it. | Observation | Corroborated | High | P1 Suggestions; P3 attack pages; S1 gauge notes; W1 02:25–02:38 |
| AD-004 | Maximum reserve flashes. Using the same command from that state yields the rolling bolt, which can hit in both directions. Exact delay, depletion and damage ratio are untested. | Observation | Corroborated | High | P1, P2 and P3 Thunder; W1 02:36–02:37 and 09:22–09:26 |
| AD-005 | Monster Select stops live play. Up and down cycle candidates and the selection command commits the replacement. One helper or none can be active. W1 switches Dragon Frye to Thunder Raven in the forest. | Observation | Corroborated | High | P1 controls and companions; P3 selector; S1; W1 01:54–01:59; W2 08:08–08:12 |
| AD-006 | Alisia and the selected helper have separate portraits, HP, levels and gauges; the helper follows and resolves its own attacks. The portrait changes with the selected creature. | Observation | Corroborated | High | P1 Screen Signals and Companions; W1 01:54–02:03; W2 08:08–08:24 |
| AD-007 | Thunder can release an item from a winged receptacle before physical collection. Items improve a specified entity and do not directly complete the level. | Observation | Corroborated | High | P1 Items; P3 item rules; W1 02:44–03:12 and later level changes; S1 Stage 1 |
| AD-008 | The scripted temple meeting precedes the quarry. The required twin fight, followed by the Stage 1 clear and Stage 2 arrival, establishes the terminal. A helper choice is not itself a clear prerequisite. | Observation | Corroborated | High | P3 Stage 1 and stage ending; W1 04:44–05:44 and 09:22–10:00; W2 09:25–09:51; S1 |
| AD-009 | Normal field time advances with movement and hostile action. The selector keeps the local scene and gauge state fixed across the visible choice, and control then resumes. | Observation | Corroborated | High | S1 controls; P3 selection instructions; W1 01:55–01:57 partial gauge unchanged, 01:57.5 adding charge; W2 08:08–08:12 |

## Basic data

- Release / origin: Game Arts, with Gainax in the in-game credits.
  Sega of America published the 1992 North American Genesis
  cartridge. Sources disagree on the exact North American launch
  day, so only the year is used. The original Genesis recording
  is not asserted to be a physical capture.
- Platform or physical form: original single-player North American
  Sega Genesis retail cartridge. The booklet mirrors do not
  establish a ROM revision or claim that the Mini or Switch
  ports share every behavior.
- Mechanical families: `FAM-010`, real-time system pressure from
  enemy approach and gauge recovery, and `FAM-015`, coordination
  between direct avatar control and the selected autonomous supporter.
- Primary sources accessed 2026-11-25:
  - **P1:** [North American Genesis instruction booklet, searchable transcription](https://manuals.plus/m/178bac02eeed0cdf899470da3e7eaa4736f0ccc908e7e1f1a6b72a9a0302672f).
    Controls, Options, Screen Signals, Items and Suggestions.
    Source is a converted retail manual; icon and OCR ambiguity
    are corroborated instead of used for exact measurements.
  - **P2:** [Sega-hosted English-inclusive cartridge manual](https://manuals.sega.com/megadrivemini/pdf/ALISIA_DRAGOON.pdf).
    The archive path refers to the later Mini support site.
    The underlying booklet describes the original cartridge's
    mappings, directional attack, rolling bolt and companions.
  - **P3:** [Original Japanese Game Arts booklet, archived by Sega](https://www.sega.jp/mdmini/manual/pdf/m_jp_alisia-dragoon.pdf).
    Attack and selector illustrations, the first stage's three
    settings, twin boss identity and stage settlement. Use only
    shared boundaries corroborated in the English evidence.
  - **P4:** [Game Arts corporate history](https://www.gamearts.co.jp/en/company/corporate_profile_en.pdf),
    which credits Alisia Dragoon on Mega Drive in 1992 with Japanese
    and North American regions. Its single release date is not
    assigned to the North American cartridge.
- Secondary and recorded play evidence:
  - **S1:** [cirtemid's Genesis route and mechanics walkthrough](https://gamefaqs.gamespot.com/genesis/586021-alisia-dragoon/faqs/11091).
    Normal-only author scope, gauge and selection descriptions and
    Stage 1 from the first outdoor area through the twin arena.
    The specific damage and recharge values are not adopted.
  - **S2:** [MobyGames original Genesis release record](https://www.mobygames.com/game/12280/alisia-dragoon/releases/),
    indexed North American 1992 publishing credit, compared with
    [the separate GameFAQs release table](https://gamefaqs.gamespot.com/genesis/586021-alisia-dragoon/data).
    Day-level catalog dates were not used.
  - **W1:** [xRavenXP, US-labelled Genesis run](https://www.youtube.com/watch?v=XPl5ggKIcsU&t=102s).
    Options 00:58–01:04, playable entry near 01:48,
    companion change 01:54–01:59, forward versus full-charge
    output in 02:26–02:38, temple meeting 04:44–05:44,
    and twin settlement 09:22–10:00.
  - **W2:** [GameLog, independent English Genesis run](https://www.youtube.com/watch?v=vc1RqxPXBIs&t=480s).
    Normal Type 1, separate from the earlier title attract
    sequence. Dragon-to-orb selection 08:08–08:12, ordinary
    forward and angled lightning around 09:03–09:07, and the
    twin clear 09:25–09:51. The exact cartridge region is unknown.
- Claim IDs: `AD-001`–`AD-009`. A repeatable retail test should
  record the cartridge ID and input mapping, place the avatar with
  a live threat on each side and compare usable partial reserve
  with flashing full reserve. Capture before, during and after a
  helper switch with a partially emptied gauge.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: walk, crouch and jump through the terrain; horizontal
  intent also determines which side of the body a regular cast addresses
  (`AD-001`, `AD-002`).
- Reuse `ACT-295`: start the character-owned Thunder action with its
  mapped command. The player may use brief input or sustain the cast;
  output conditions differ with reserve (`AD-001`–`AD-004`).
- New `ACT-935`: enter the helper selector, cycle a roster or the empty
  choice and commit the result. Ordinary movement authority remains
  with Alisia (`AD-005`, `AD-006`).

### System Behaviour Genes

- Reuse `SYS-037`: collect a freed eligible item by body contact.
  Opening its container with Thunder and acquiring its contents
  are separate (`AD-007`).
- Reuse `SYS-407`: the chosen helper follows and selects its own attacks
  according to local state. The player selects the participant
  rather than commanding each discharge (`AD-005`, `AD-006`).
- Reuse `SYS-1365`: repeatedly casting draws from one bounded player
  reserve. Unspent live time away from casting restores it.
  Health and the helper's gauge remain separate (`AD-003`, `AD-006`).
- New `SYS-2012`: ordinary active lightning acquires eligible targets
  automatically on the facing side, including a visible higher
  target. Directional positioning remains a player decision
  (`AD-002`).
- New `SYS-2013`: when the reserve is full and flashing, the
  same cast command redirects the output into an all-around
  rolling bolt rather than the ordinary forward attack
  (`AD-003`, `AD-004`).

### Constraint Genes

- New `CON-901`: the support field slot allows at most one living
  eligible helper; leaving it empty still allows ordinary play.
  This is not the rule for a mandatory active battler
  (`AD-005`, `AD-006`).

### Information Genes

- Reuse `INF-192`: the following viewport exposes upcoming terrain,
  nearby enemies and obstacles before movement commitment
  (`AD-001`, `AD-002`, `AD-008`).
- New `INF-651`: player and helper panels expose separate vitality,
  level and power, with a flashing full gauge disclosing readiness
  for the all-around cast (`AD-004`, `AD-006`).

### Objective Genes

- Reuse `OBJ-029`: clear the finite pair at the end of the quarry
  while Alisia remains viable. The Stage 1 clear resolves to
  actual Stage 2 control without a collected boss token
  (`AD-008`).

### Time Genes

- Reuse `TIM-003`: ordinary traversal, enemies, helper behaviour
  and Thunder recovery run in active time (`AD-003`, `AD-006`, `AD-009`).
- Reuse `TIM-046`: the field select window suspends combat and
  accrual of the reserve shared by the ordinary and full
  Thunder attack. Selection commits without an attack charge,
  and live time resumes after closing the selector (`AD-005`, `AD-009`).

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Alisia faces a higher enemy with a usable but partial reserve | Activate Thunder | The visible arc bends forward and upward to the target | AD-002, AD-003 |
| Gauge has fallen after a sustained burst | Stop casting while play runs | The player reserve recovers independently of the helper | AD-003, AD-006 |
| Gauge has reached flashing full charge | Use the same attack command | The rolling bolt can reach targets on both sides | AD-004 |
| Dragon Frye is active in the open forest | Enter Monster Select, move to Thunder Raven, commit | The scene resumes with the new portrait and Raven body | AD-005, AD-006, AD-009 |
| An eligible winged container is present | Break it with Thunder, then touch the freed item | Contact acquires the item separately from opening the container | AD-007 |
| Temple encounter resolves by script | Continue through the first stage | The restored route enters the quarry, distinct from the twin fight | AD-008 |
| Two required opponents are active at the quarry end | Defeat the pair while remaining alive | Stage 1 clears and the game returns control in Stage 2 | AD-008 |

## Strategic and experiential structure

Facing reduces the spatial aiming problem but still matters
when enemies approach from two directions. Releasing the attack
can create a vulnerable interval while also preparing a stronger
next action. Helpers work from their own condition. The player
decides when it is useful to exchange a helper without giving up
movement control across the stage.

## Replay and variation

The same first stage supports different helper choices and
different bindings for the same commands. W1 changes from
Dragon Frye to Thunder Raven near the start and later returns
to a dragon. W2 later chooses Ball O' Fire and uses it near
the twin arena. These are two successful demonstrations, not
controlled comparisons of equal upgrade levels or optimum time.

## Adjacent systems and history

Most collectible upgrades remain optional in this slice. The
manual also specifies revival, extra continues and rankings.
The presence of those rules does not establish a first-stage
failure trace, an exact continuance snapshot or the contents
of later modes.

## Normalised genome

- Action: ACT-008, ACT-295, ACT-935.
- System Behaviour: SYS-037, SYS-407, SYS-1365, SYS-2012, SYS-2013.
- Constraint: CON-901.
- Information: INF-192, INF-651.
- Objective: OBJ-029.
- Time: TIM-003, TIM-046.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `718` (`GAME-0001`–`GAME-0718`).
- Exact genome matches: none.
- Tied near matches: `GAME-0640` — Pizza Tower (`5 / 21 = 0.238095`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Pizza Tower (GAME-0640)](../m-r/pizza-tower.md) | ACT-008, ACT-295, INF-192, SYS-037, TIM-003 | Both support direct side-view movement, player attacks and contact pickups under live progression. Pizza Tower builds movement speed and changes to an escape timer after its route fixture. Alisia Dragoon chooses an automatic lightning geometry with charge and facing, selects an independent helper, then clears a finite twin fight. | Near, `0.238095`. |

## Taxonomy impact

Reuse direct movement, character-owned attack, contact
acquisition, autonomous support, charge recovery, lookahead,
finite encounter clearance and the two time states. Admit
automatic facing-side lightning, full-charge replacement of
attack output, optional helper selection and capacity, and the
two-panel reserve feedback. Conventional resource debit is
represented by SYS-1365 rather than a duplicate definition.

## Negative results

- Ordinary casting does not require a full gauge and does not
  deliberately reach enemies behind the current facing.
- The helper choice does not transfer main control or require
  the player to time each helper attack.
- An area transition or the scripted temple meeting does
  not satisfy the final twin clear.
- The witness cannot authenticate physical input timings,
  an exact cartridge revision or a numerical recharge curve.

## Delta summary

Use an ordinary cast while there is charge and a useful target
ahead. Delay the next cast to obtain a surrounding attack when
approached from both sides. Choose an independent supporter
suited to the approach and defeat the two required opponents.

## New facts

- Ordinary lightning trades manual aim for a facing-side target rule.
- The same input can have a qualitatively different effect at full charge.
- The active companion's charge is separately visible and the choice can be empty.

## Principles and design implications

Disclose the reserve threshold that changes the attack. Give
automated support a separate state and make changing that
support independent of the player's locomotion authority.

## Puzzle or game generation potential

Create a narrow arena with opposed approach directions,
one capped attack resource and a visible full-charge branch.
Provide a small optional roster of autonomous supports. Check
that a route using a short directional cast and another using
a prepared sweep can both achieve the required clear.

## New genes

- ACT-935
- CON-901
- INF-651
- SYS-2012
- SYS-2013

## New combinations

None.

## Taxonomy changes

[Taxonomy Change 465](../../../research/taxonomy-changes/TAXONOMY_CHANGE_465.md).

## Next recommended game

Continue Selection 062 with Kaze and the Wild Masks on the
English Xbox One base release. Follow an early mask pickup through
its changed movement and a confirmed stage or checkpoint outcome.

## Why this game

Its ordinary lightning, charged sweep and companion choice
expose separate levers in one live two-sided encounter.

## Review status

Reviewed 2026-11-25 for the original Normal Stage 1 fixture.
Formal evidence and bilingual presentation refer to this bounded route.
