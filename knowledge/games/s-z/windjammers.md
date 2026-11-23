---
game_id: GAME-0564
slug: windjammers
game_title: Windjammers
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-223
    - ACT-765
  system:
    - SYS-1640
    - SYS-1641
    - SYS-1642
    - SYS-1643
    - SYS-1644
    - SYS-1645
    - SYS-1646
    - SYS-1647
  constraint:
    - CON-828
    - CON-829
  information:
    - INF-116
    - INF-178
    - INF-539
  objective:
    - OBJ-282
  time:
    - TIM-003
---

# Game: Windjammers

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Flying Power Disc, athlete names, named specials and the numeric profile are
carrier parameters rather than independent title-based genes.

## Analysis scope

- Version / ruleset: original released English international Neo Geo MVS
  arcade Windjammers, 1994, one local two-player match. Select Hiromi Mita
  against Klaus Wessel on Beach, using the displayed twelve-point target,
  thirty-second ordinary-set profile and two required set awards. This is a
  declared international rules profile, not a certified owned ROM, BIOS,
  checksum, original PCB execution or operator-DIP capture. Japanese
  fifteen-point/forty-five-second defaults, AES/CD options and modern ports
  are not silently substituted.
- Structured analysis target: original MVS entry in
  `knowledge/platforms/games.json`, supported by the original Data East flyer,
  visible original-game tutorial/court states and independently authored
  original-game/community accounts. The official later publisher pages
  identify the original product and distinguish their online/HD additions.
- Primary decision loop: read the live disc, opponent, goal sections and
  landing cue; walk or commit a slide into a receiving position; catch or
  time a toss, occupy the airborne landing point if charging is useful,
  then release a directed, curved, lob or eligible powered return. Resolve
  banking, catch, rear hit, pushback or score, reposition for the renewed
  serve, and repeat until the full match is adjudicated.
- Entry and exit: first playable serve of the declared fixed-pair Beach
  match after character/court selection. Include every ordinary set needed
  for final settlement, shared awards on tied timed sets, the required
  bounded sudden-death branch on simultaneous match qualification and its
  possible final draw. Stop at the displayed winner/loser or Draw result,
  before inserting another credit, accepting a buy-in or beginning another
  match. A single scored goal or first set is not completion.
- Reproducible setup/coverage route: choose the original international
  profile, assign Mita to the left and Wessel to the right, choose Beach
  and accept the opening serve. During complete match repetitions, compare
  direct and wall-bank throws, early/delayed returns and near/deep lobs;
  catch by walking and by a committed slide, then perform neutral and
  A-then-direction tosses. Reach an airborne landing mark early enough to
  charge and exercise the available custom, spin and rolling-lob families.
  Attempt an eligible special reversal and contrast its missed window.
  Separately cover a rear hit/recovery, a receiving push near the goal,
  a flat-drop miss, timed set awards and the draw/tiebreak branch. These are
  declared controls, not a claimed native input trace or an instruction to
  use an edited save as ordinary original hardware.
- Court and controls: both athletes remain in their own half; only the disc
  crosses the central net. The upper/lower walls reflect it; the left/right
  end boundaries have yellow outer and red middle scoring sections. Beach
  has no central obstacles or growing goal sections. Without possession,
  direction steers the athlete; direction then A requests a slide whose
  continued hold trades extra travel for longer recovery. Neutral A requests
  a short receiving block; A followed by direction permits a shifting toss.
  With possession, direction aims and A/B release the selected delivery.
  Voluntary movement is disabled, but a forceful reception may still push
  the holder. No invulnerability, jump or free disc steering is presumed.
- Included: constant live movement and disc travel; commitment/recovery of
  slides; automatic facing catches, rear-hit knockdown and recovery; timed
  upward toss, landing-marker concentration and temporary powered readiness;
  release-delay effects and eventual automatic weak release; ordinary,
  curved, lob, custom, spin and rolling-lob paths; eligible reversals and
  preserved incoming custom identity; forced receiving displacement;
  weighted goal/drop points, local serve resets, live score/clock/phase
  disclosure, full set/match and bounded tie adjudication.
- Source-sensitive parameters: the majority of inspected accounts specify
  first to twelve for this profile. BakaOrochi additionally reports a lead
  exceeding two points near the target; Prof_Rev and the community
  introduction do not include that condition. The exact native margin is
  unresolved rather than silently fixed to either formula. The published
  guide also distinguishes an already released throw at the whistle from a
  held dead disc; exact final-contact ordering is not reproduced. Community
  authors describe automatic charge, whereas an older FAQ tells players to
  mash A. Automatic standing charge is retained from the explicit current
  community account and corroborating charge descriptions; no mandatory
  mash counter is invented. Reported score-deficit widening of fastest-return
  and reversal windows remains qualitative, with no certified frame table.
- Excluded: the single-player CPU ladder, Dog Distance and disc bowling;
  another court's obstacles or Stadium's changing red zone; roster/credit
  economy, save states, operator menus during live play, account rewards,
  online rollback/ranks and later port presentation; the sequel's jump,
  slap/drop-shot and super-meter additions. Original airborne special
  returns are included; sequel-only verbs are not.
- Potential scoped modules: original solo ladder with bonus intermissions,
  obstacle courts, Stadium score-dependent goal geometry, another regional
  rules profile and separately versioned modern/sequel play.
- Direct-play status: not conducted. Visually inspected the original US Data
  East sales flyer scan, not an original operator manual or owned cartridge.
  Inspected all nine ten-second static storyboard sheets covering HIDEFACES'
  36:13 Arcade Longplay #82 at 160×90 source cells, including original
  tutorials, twelve-point/thirty-second displays, complete duels, continues
  and excluded bonus/court variants. These illustrate visible states across
  matchups, not a fresh native reproduction of the selected fixed pair.
  Inspected the one coarse 61×45-cell sheet of World of Longplays' 17:03
  recording; it is too small to certify numeric/contact timing. Its author
  explicitly discloses save-state-assisted special exchanges. No video or
  sound playback, original executable, controller trace, precise frame
  experiment, owned BIOS/ROM or native settings capture was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| WJ-001 | Data East's original 1994 Neo Geo arcade product is distinct from later console ports and the sequel; this target is international MVS local play. | Observation | Corroborated | High | P1, P2, P3, S1, S2 |
| WJ-002 | Two-button context controls distinguish free movement/sliding, automatic facing catch, a short toss attempt and immobilised held-disc release. | Observation | Corroborated | High | B1, S1, S2, S4, V2 |
| WJ-003 | One shared disc banks and changes travel family; rear hits and powerful catches can respectively expose a drop or drive a holder into a scored boundary. | Observation | Corroborated | High | P1, S1, S2, S3, V2 |
| WJ-004 | Catch-to-release delay affects speed/lob depth and indefinite holding resolves into a weak automatic throw. | Observation | Corroborated | High | S1, S2, S3, V2 |
| WJ-005 | Airborne landing preparation grants temporary powered choices; legal timed reversals preserve permitted incoming-family identity rather than requiring a fresh full charge. | Observation | Corroborated | Medium | S1, S2, S3, V1, V2 |
| WJ-006 | Beach scores yellow/red goals and flat misses differently; set awards accumulate to the complete match, with both sides credited for a timed set draw. | Observation | Corroborated | High | P1, S1, S2, S3, S4, V2 |
| WJ-007 | A claimed extra lead margin near twelve conflicts with the simpler point-target accounts; the exact native criterion is not certified. | Observation | Conflicting | Medium | S1, S3, S4 |
| WJ-008 | Simultaneous match qualification requires a bounded first-score tiebreak; no decisive score can leave a final draw. | Observation | Corroborated | Medium | S1 introduction, S3, S4 |
| WJ-009 | A guide distinguishes pending released flight at expiry from a held dead disc; exact native event ordering is untested. | Observation | Limited | Medium | S3 |
| WJ-010 | Community authors report score-sensitive return/reversal windows; no independent native deficit formula or exact frame table is reproduced. | Observation | Limited | Medium | S1, S5 |
| WJ-011 | Explicit automatic-charge guidance differs from older mash-A advice; a required button-mash resource is not established. | Observation | Conflicting | Medium | S1, S2, S3 |

## Basic data

- Release / origin: Data East, original Neo Geo MVS arcade release, 1994.
  Historical catalogues date the Japanese arcade release to 17 February;
  no exact international first-day claim is necessary for this profile.
- Platform or physical form: original joystick/two-action-button arcade
  rules; two human players, fixed pair and Beach. Mita's agility and Wessel's
  power/charge characteristics parameterise the admitted transitions.
- Puzzle family: physics/object manipulation; tactical counterplay;
  real-time pressure. No new platform or family is introduced.
- Primary artifacts and official identity sources, accessed 2026-11-20:
  - **P1** [Data East US sales flyer, 1994](https://flyers.arcade-museum.com/videogames/show/1301),
    visually inspected through the [archival scan](https://adb.arcadeitalia.net/media/mame.current/flyers/wjammers.png?release=209).
    This is an original publisher artifact hosted by an archive, not an
    official current Data East domain or a complete operator manual.
  - **B1** original in-game tutorial/court displays visible in V2, including
    sliding/receiving, curve input and the twelve-point/thirty-second profile.
    The recording does not certify a specific owned binary or region BIOS.
  - **P2** [official Windjammers game page](https://www.flyingpowerdisc.com/game/),
    identifies original Neo Geo lineage, the two scoped athletes and named
    special families while explicitly describing its later PlayStation port.
  - **P3** [Dotemu product page](https://www.dotemu.com/games/windjammers/),
    distinguishes later online modes/HD menus. Those additions are excluded.
- Independently authored corroboration, accessed 2026-11-20:
  - **S1** Windjammers France [original introduction](https://www.windjammers-france.fr/wiki/wiki-en/introduction)
    and [original-game basics](https://www.windjammers-france.fr/wiki/wiki-en/the-basics),
    controls, automatic charge, family restrictions, international/Japanese
    defaults and timed tiebreak. Its WJ2 page is not the selected rules source.
  - **S2** [Michael Plasket, Hardcore Gaming 101, 7 August 2017](https://www.hardcoregaming101.net/windjammers/),
    independently describes original catches, rear hits, receiving pushback,
    delayed release, concentration and repeated powered returns. Its dated
    unreleased-sequel statement is historical, not a present availability claim.
  - **S3** [June Kim/BakaOrochi, original-game FAQ](https://gamefaqs.gamespot.com/arcade/564208-windjammers/faqs/27027),
    indexed passages inspected for scoring, controls, margin, clock edge and
    draw. The full page is restricted; no complete-read claim is made. Later
    port notes and doubtful mandatory-mash advice are not silently imported.
  - **S4** [Prof_Rev, original-game FAQ](https://gamefaqs.gamespot.com/arcade/564208-windjammers/faqs/10804),
    indexed gameplay/score/control/court passages corroborate first-to-two,
    both-side draw awards and no-winner final draw. Full-page access is
    restricted; illustrative speed percentages are not native coefficients.
  - **S5** [Tuxosaurus, original-game teaching wiki](https://wiki-windjammers.fr/),
    full gameplay sections read, including timing, automatic charging,
    score-sensitive windows and reset-position variation. Community material
    can overlap S1; these pages are not counted as independent native tests.
  - **S6** [Dan Elektro, original MVS review](https://www.neo-geo.com/reviews/neo-reviews/windjam/windjam.html),
    corroborates two-button play, original court values, drops and short sets.
- Sparse recorded observations:
  - **V1** [World of Longplays / ScHlAuChi](https://www.youtube.com/watch?v=Eg93nPgR6rw),
    17:03. One coarse sheet inspected; disclosed save states prevent treating
    its unusual chains as an unaided native run or timing benchmark.
  - **V2** [HIDEFACES, Arcade Longplay #82](https://www.youtube.com/watch?v=btfQfLRrD6I),
    36:13. All nine 160×90-cell ten-second sheets inspected. Extra courts,
    continues and bonus games visible in this recording remain excluded.
- Claim IDs: WJ-001–WJ-011.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: steer the current athlete and request the local slide.
  Hold duration/travel commitment/recovery are movement parameters, not a
  second damage or invulnerability action. Directional recovery inputs can
  shorten the reported knockdown; no exact required mash count is certified.
- Existing `ACT-223`: time the legal receiving block/toss response against
  the approaching threat; no health loss is required for the response.
- New `ACT-765`: release the held disc with the legal directional/motion and
  normal/lob/powered family selection. The same input changes meaning with
  possession and readiness, rather than using one gene per button.
- Claims: WJ-002–WJ-005.

### System Behaviour Genes

- New `SYS-1640`: one released disc follows its authored flight family,
  redirects on the appropriate walls and can roll after a powered lob.
- New `SYS-1641`: facing contact automatically catches; a powerful receiving
  contact can push the holder, whereas a rear hit can knock down the athlete
  and pop up the disc. These are contact-class outcomes, not separate HP bars.
- New `SYS-1642`: contact in the requested short block creates an unheld
  aerial toss and a later receiving opportunity, not an immediate attack.
- New `SYS-1643`: early occupancy of the landing marker automatically builds
  temporary receiving charge and grants permitted powered families on catch.
- New `SYS-1644`: release delay sets speed/lob-depth and eligible fastest
  returns; excessive holding causes a weak automatic release. The reported
  score-dependent window remains a bounded uncertain parameter.
- New `SYS-1645`: a valid immediate powered return follows incoming-family
  restrictions, including retaining an opponent custom's identity. A later
  fresh charge is a different path to powered delivery.
- New `SYS-1646`: zone/drop result awards points and renews local serve
  state without resetting retained match progress. Possible small starting
  offsets are parameters, not a measured RNG distribution.
- New `SYS-1647`: the complete set/match scheduler records one/both set
  awards, handles simultaneous qualification and bounded sudden death/draw.
  Unknown exact lead-margin or final-contact ordering is not invented.
- Claims: WJ-003–WJ-011.

### Constraint Genes

- New `CON-828`: athletes stay in separate halves, while the disc can cross
  the center and interact with rebound walls/scoring ends.
- New `CON-829`: held possession forbids voluntary relocation and maps
  direction to aim; it does not prohibit forced receiving displacement.
- Parameters: selected court, actor bounds, goal-zone ordering, selected pair,
  held state and release. Claims: WJ-002, WJ-003.

### Information Genes

- Existing `INF-116`: side scores, set marks, clock and current match phase
  are disclosed; a one-athlete side is the relevant side parameter.
- Existing `INF-178`: the overhead playing view shows both athletes, current
  controlled side, shared disc, net, walls and marked scoring sections.
- New `INF-539`: an airborne landing mark and receiving-charge cue reveal
  the positioning/charge opportunity without exact hidden timing or future
  opponent commands. Claims: WJ-002, WJ-005, WJ-006.

### Objective Genes

- Existing `OBJ-282`: have the declared side awarded the complete fixed-pair
  match after required set awards and any simultaneous-threshold tiebreak.
  Two shared awards alone are not an automatic victory; a final Draw is a
  settled non-win. No health-based KO objective or whole tournament is added.
- Claims: WJ-006–WJ-008.

### Time Genes

- Existing `TIM-003`: both human inputs, disc motion, receiving/recovery
  windows and the applicable set clock remain live. A serve reset does not
  grant an unbounded planning pause. Exact interstitial/pending-flight
  timing is unmeasured; no unlimited overtime is inferred. Claims: WJ-002–WJ-009.

## Reproducible transitions

| Before | Action | Resolution | Distinction | Claim |
| --- | --- | --- | --- | --- |
| Empty hands in own half | Walk, or direction then A to slide | Direct movement, with committed slide travel/recovery if selected | Not a freely cancellable teleporter or an invulnerable dodge | WJ-002 |
| Incoming disc meets receiving face | Intercept by legal movement | Disc automatically becomes held | A separate timed grab is unnecessary | WJ-002 |
| Incoming disc meets back | Recover from knockdown and pursue the popup | Temporary loss of ordinary control creates a possible miss | Not ordinary HP damage | WJ-003 |
| Strong incoming reception near own goal | Catch without a qualifying reversal | Backward push can cross the scored boundary | Catching does not guarantee safety | WJ-003 |
| Held disc | Try ordinary movement then aim/release | Locomotion stays disabled until release; direction chooses delivery | No running with a carried disc | WJ-002 |
| Fresh catch | Release promptly or wait | Speed/lob depth changes; excessive holding produces a weak automatic throw | Holding longer does not simply charge more power | WJ-004 |
| Disc approaches and block is available | Neutral A, optionally followed by direction | Eligible contact sends the disc aloft | Not immediate ownership or a direct reflected attack | WJ-002, WJ-005 |
| Airborne disc with landing mark | Arrive beneath it early and wait | Temporary charge advances before reception | No mandatory persistent-meter purchase | WJ-005, WJ-011 |
| Charged receiving state | Choose custom, spin or lob input | Legal powered family is released | Rolling-lob ground contact differs from a flat miss | WJ-005 |
| Incoming powered custom | Commit eligible rapid return | The received custom or another permitted family returns | Not necessarily the defender's own custom | WJ-005 |
| Ordinary flat airborne disc unreceived | Let it reach the court | The opposite side receives two points in this profile | A powered rolling lob is a different state | WJ-006 |
| Disc reaches yellow or red goal section | Settle the legal goal | Three or five points are awarded and local serve renews | End-zone value is not a basketball shot-distance line | WJ-006 |
| Legal timed set terminal with equal score | Settle the set | Both sides receive a set award | A set draw is not always a final draw | WJ-006 |
| Both sides qualify together | Enter the bounded first-score tiebreak | First valid score settles the winner; undecided expiry can remain Draw | No unlimited Soccar overtime or reduced-life fighter round | WJ-008 |
| Near-target score or whistle-edge flight | Consult declared profile and record source limit | Exact native margin/contact ordering remains unresolved | An indexed conflicting guide is not a certified binary formula | WJ-007, WJ-009 |

## Strategic and experiential structure

- Local decision: intercept high enough upcourt to leave space against
  receiving push, then aim at a gap or choose a bank rather than chasing
  only the five-point section.
- Medium horizon: fast returns pressure movement, while a lob forces depth
  but can give the opponent charging time. A toss can trade immediate
  possession for a stronger later return.
- Resource tension: court position, release delay and short receiving windows
  matter; there is no admitted persistent super currency or health pool.
- Failure attribution: visible position, facing, landing cue and goal section
  explain most point losses. Exact native timing and the disputed margin
  remain source limits, not an invented frame-precise guarantee.
- Trust: distinguish a powerful catch from a safe catch, a set draw from a
  match draw and a later port feature from the selected original packet.
- Claims: WJ-002–WJ-011.

## Replay and variation

- Two human input streams, release timing, trajectories, positioning and
  score progression vary inside the fixed matchup/court profile.
- Small reset-position variation is reported but its exact distribution is
  not measured. No random critical hit, loot economy or procedural court is
  inferred. Other athletes/courts are potential separate scoped variants.
- Claims: WJ-002–WJ-011.

## Adjacent systems and history

- The later Dotemu ports add interfaces/online play; the sequel adds verbs.
  Neither changes which original MVS packet this record covers.
- Bonuses and the CPU ladder have separate decision/terminal structures;
  their appearance in a source recording does not admit them here.
- Claims: WJ-001, WJ-005, WJ-006.

## Normalised genome

| Type | Genes |
| --- | --- |
| Action | `ACT-008`, `ACT-223`, `ACT-765` |
| System | `SYS-1640`, `SYS-1641`, `SYS-1642`, `SYS-1643`, `SYS-1644`, `SYS-1645`, `SYS-1646`, `SYS-1647` |
| Constraint | `CON-828`, `CON-829` |
| Information | `INF-116`, `INF-178`, `INF-539` |
| Objective | `OBJ-282` |
| Time | `TIM-003` |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `563` (`GAME-0001`–`GAME-0563`).
- Exact genome matches: none.
- Tied near matches: `GAME-0163` — EA SPORTS FC 26 (`4 / 34 = 0.117647`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0163` — EA SPORTS FC 26 | `ACT-008`, `INF-116`, `INF-178`, `TIM-003` | Both expose a live shared playing surface, controlled movement, side score and clock. Football uses running ball control, teammates, passing and field-line restarts; this disc duel freezes voluntary possession movement, keeps athletes in separate halves and uses timed toss/charge/reversal plus set awards. | Tied near: 4 / 34 = 0.117647. |

### Preserved research notes

- New genes: twelve; six unchanged definitions reused.
- Classification result: New gene.

## Taxonomy impact

- Registry additions: `ACT-765`, `SYS-1640`–`SYS-1647`, `CON-828`, `CON-829`, `INF-539`.
- [Taxonomy Change 310](../../../research/taxonomy-changes/TAXONOMY_CHANGE_310.md)
  records the admitted boundaries and rejected alternatives.

## Negative results

- None as a separate prior-claim rejection. Source conflicts and missing
  native formulas remain explicit limitations instead of rewritten history.

## Delta summary

## New facts

- [Observation | Corroborated | High] WJ-002–WJ-006: automatic possession,
  positional contact consequences and timing-conditioned disc returns.
- [Observation | Conflicting | Medium] WJ-007, WJ-011: unresolved exact
  target-margin and conflicting mandatory-mash advice remain qualified.

## New genes

- [Observation | Corroborated | Medium] `ACT-765`, `SYS-1640`–`SYS-1647`,
  `CON-828`, `CON-829`, `INF-539`.

## New combinations

- [Observation | Direct | High] No new combination proposal; accepted
  proper subsets are owned by Corpus comparison.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_310`; no earlier
  signature, definition or lifecycle changes.

## New questions

- What exact native score-margin predicate governs a near-target set?
- Which pending-flight contacts can still alter score after the whistle?
- What exact score/athlete conditions set fastest-return and reversal windows?
- Which original charge/recovery events accept useful repeat inputs?

## Next recommended game

- [Hypothesis | Limited | High] Full-release Windows Dome Keeper, `GAME-0565`,
  under approved Selection 045.
- Optimisation criterion: return to modern mining/defense after an arcade duel.
- Expected information gain: inspect a complete resource-to-defense cycle
  without importing Early Access or unrelated scenario inventory.
- Backlog impact: three subjects remain; stop after GAME-0567. No push,
  publication, Actions, merge or deploy is authorised.

## Why this game

- [Hypothesis | Limited | High] The complete bounded sports duel separates
  automatic acquisition, active deflection, timed return and unsafe reception
  while extending the mixed-era, cross-platform horizon.
