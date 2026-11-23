---
game_id: GAME-0571
slug: virtua-tennis
game_title: Virtua Tennis
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-774
    - ACT-775
  system:
    - SYS-146
    - SYS-1674
    - SYS-1675
    - SYS-1676
    - SYS-1677
    - SYS-1678
  constraint: []
  information:
    - INF-544
  objective:
    - OBJ-313
  time:
    - TIM-003
---

# Game: Virtua Tennis

Use the canonical [vocabulary and signature rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Positioning changes what the racket can do at contact. A chosen return
direction and the body's preparation are independent parts of each rally.

## Analysis scope

- Version / ruleset: original English North American Dreamcast release,
  July 2000. Target the NTSC-U MK-51054 V1.001 ruleset identified in the
  reconstruction, with the listed 8 June build date distinct from release.
  Use one standard Dreamcast Controller and one Normal COM opponent.
- Structured analysis target: PLAT-DREAMCAST in knowledge/platforms/games.json.
- Entry: configure Exhibition, Singles, GAME COUNT 1, DEUCE ON, COM LEVEL
  NORMAL and Australia Challenge hard court. Select base roster Mark
  Philippoussis for the human and Jim Courier for COM. Start at the first
  ready-to-serve state at love-all with the assigned server. Roster selection
  fixes parameters rather than adding a mid-match ability.
- Primary decision loop: for service, toss and time the follow-up press while
  choosing type and direction. During a live rally use direct movement to
  intercept the ball early, choose a normal hit or lob and aim before contact.
  Balance preparation against how far the ball takes the athlete from a
  recoverable position. Read the point or service decision, then settle the
  next point under the same game profile.
- Positive exit: the human wins the configured game after legal point
  adjudication. The one-game profile settles the complete match here,
  including any deuce extensions. At 40–40 a single point grants advantage,
  and two in succession from deuce settle the match.
- Negative exit: the COM wins the same complete game. A fault without a point
  or a single missed return before match point is an intermediate event.
  Deliberate abandonment to Main Menu is outside competitive settlement.
- Included: standard controller movement, one opening service per point
  with permitted retries, directional racket input, normal hit, lob,
  contextual smash and weak lunge, ball collision, legal landing, rally
  terminal, 40–40 and advantage, score display and match result.
- Time boundary: the toss gauge and ball travel continue while the player
  positions and chooses a stroke. The point sequence waits in its ready
  state before a new toss. The original manual exposes START pause, but
  there is no Arcade countdown to continue in the selected match.
- Excluded: full-set tie-break, DEUCE OFF except as documented contrast in
  ruleset selection, other court and athlete coefficients, doubles partner
  commands, additional humans, Arcade advancement, World Circuit training,
  shopping, fatigue or string maintenance, unlocked players, non-Dreamcast
  conversions and sequels.
- Potential scoped modules: full-set tiebreak and service rotation, doubles
  partner tactical policy, World Circuit trial reward and equipment economy.
- Direct-play status: not conducted. Read the original Dreamcast booklet,
  contemporaneous Dreamcast play accounts and pinned reverse-engineered
  reconstruction functions and test notes for the stated USA build. No
  retail disc, emulator or audiovisual playback was used. Timing coefficients,
  court tolerances and all per-athlete numeric parameters remain unmeasured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| VT-001 | Sega's 2000 North American Dreamcast edition is distinct from arcade and later ports. The pinned reconstruction names USA MK-51054 V1.001. | Confirmed | Direct | High | P1, P2, D1 |
| VT-002 | Exhibition selects singles, game count, deuce, COM strength, roster and court. One game is an available complete match. The full-set extension is separate. | Observation | Corroborated | High | P1, R1, R2, D2 |
| VT-003 | Press A or B to toss. The next A or B with direction hits a flat or slicing serve. Higher Serve Gauge readings yield a faster serve. | Observation | Corroborated | High | P1, R1 |
| VT-004 | Direct movement and pre-contact aim use the stick or D-pad. A requests a normal hit, B or X a lob, and aiming before contact can change horizontal direction and depth. | Observation | Corroborated | High | P1, R2 |
| VT-005 | Reaching the ball early allows stronger preparation. A stretched lunge is weak. A normal hit under a high ball can produce a smash. Forehand and backhand depend on contact context. | Observation | Corroborated | High | P1, R2, R3 |
| VT-006 | Flight and landing determine a live point. In the reconstruction, first fault retries, second fault credits the receiver and an otherwise in-bounds net serve is a let without adding a fault. A second unreturned legal rally bounce credits the striker. | Observation | Corroborated | High | P1, R1, D3 |
| VT-007 | A point changes the tennis tally. DEUCE ON distinguishes 40–40, advantage, restored deuce and win. The game tally increments at game win, and one completed game settles this match. | Observation | Corroborated | High | P1, R2, D2, D4 |
| VT-008 | The singles view shows ball and athletes, current point and game score. It distinguishes the serve attempt and gauge and shows serve speed. The booklet also permits a 1P camera change. | Observation | Direct | High | P1, printed pp. 3–5 |

## Basic data

- Hitmaker / Sega. 2000 North American Dreamcast commercial disc.
- Families FAM-007 physics and object manipulation, FAM-009 tactical
  forecast and counterplay and FAM-010 real-time system pressure.
- P1: [Sega's original North American Dreamcast booklet](https://www.digitpress.com/library/manuals/dreamcast/virtua_tennis.pdf),
  printed pp. 2–5 for controls and displays, pp. 8–9 for Exhibition and
  pp. 14–16 for original roster and regional credits. The Exhibition
  paragraph incorrectly names Arcade at its first menu step. The main menu
  on p. 5 and contemporary separate-mode accounts resolve that wording.
- P2: [Centre for Computing History North American collection item](https://www.computinghistory.org.uk/det/22374/Virtua%20Tennis/)
  and [Sega series history](https://powersmash4.sega.jp/others/about.html).
  The latter dates the Japanese Dreamcast edition. It is not the US
  street date.
- R1: [Jeff Gerstmann, Dreamcast play review](https://www.gamespot.com/reviews/virtua-tennis-review/1900-2601195/),
  10 July 2000. Distinguishes Exhibition rules, directional depth and the
  normal hit or lob input from the arcade sequence.
- R2: [Shawn Rider, Dreamcast play review](https://gamesfirst.com/articles/2000/virtua-tennis-dreamcast/),
  12 July 2000. Corroborates rule selection and responsive normal hit, lob,
  lateral/depth aim and context-dependent stroke.
- R3: [RKratz, Dreamcast play guide](https://gamefaqs.gamespot.com/dreamcast/199207-virtua-tennis/faqs/8308),
  updated 30 July 2000, and [Greg Howson and Andy Bodle](https://www.theguardian.com/technology/2000/sep/07/onlinesupplement6),
  7 September 2000. Support Australia Challenge hard court, roster choices
  and importance of approach and preparation.
- D1: [Pinned USA reconstruction metadata](https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/f0399fa6ccf4918b3f7f209fa3f94c9e3a0f6e8b/README.md).
  The source repository reports the executable identity and test boundary.
  We did not obtain the commercial executable or rerun equivalence tests.
- D2: [Exhibition rules handler](https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/f0399fa6ccf4918b3f7f209fa3f94c9e3a0f6e8b/src/gen_mi.c)
  and [match extension logic](https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/f0399fa6ccf4918b3f7f209fa3f94c9e3a0f6e8b/src/gen_ar.c#L1395).
  The full-set branch is selected separately from the one-game target.
- D3: [Court, bounce and service adjudication](https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/f0399fa6ccf4918b3f7f209fa3f94c9e3a0f6e8b/src/gen_on.c).
  Identify the fault increment, let without increment, double fault and
  live-ball point branches, without importing exact physical constants.
- D4: [Point and game settlement](https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/f0399fa6ccf4918b3f7f209fa3f94c9e3a0f6e8b/src/gen_bp.c#L631).
  The ordinary point accumulator uses a separate deuce flag and normalizes
  the tied internal counts, which is distinct from displayed score.
  Sources checked 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-008 covers movement to an intercept. ACT-774 governs the initiation
  and second commitment of service, including flat or slice selection.
- ACT-775 governs the selected normal or lob return and its pre-contact aim.
  It does not pick each movement animation or cause a second manual impact.
- Claim IDs: VT-003–VT-005.

### System Behaviour Genes

- SYS-1674 samples the service meter for speed. SYS-1675 governs how reach,
  preparation and contact condition a return. SYS-146 governs the live
  ball's flight and collision under gravity.
- SYS-1676 settles ordinary rally points by landing and unreturned bounce.
  SYS-1677 owns the separate service fault and let outcomes. SYS-1678 owns
  point accounting, deuce and the game credit.
- Claim IDs: VT-003–VT-007.

### Constraint Genes

- No separate addition. The valid receiving box, singles boundaries,
  reach and match profile constrain the named service and rally transitions.
  Physical coefficients and precise input tolerances are parameters.
- Claim IDs: VT-002, VT-005–VT-007.

### Information Genes

- INF-544 distinguishes court feedback, serve gauge, attempt indication,
  serve speed and the two score levels.
- Claim IDs: VT-003, VT-008.

### Objective Genes

- OBJ-313 settles the configured Exhibition match. Point and game awards
  are separate from the whole match terminal. Here one game suffices.
- Claim IDs: VT-002, VT-007.

### Time Genes

- TIM-003 covers the active toss and ball travel intervals. There is no
  turn exchange once a ball is live.
- Claim IDs: VT-003–VT-006.

## Reproducible transitions

| State / precondition | Action or event | Observable transition | Boundary | Claims |
| --- | --- | --- | --- | --- |
| Ready on the proper service side | Press A or B to toss | Single ball toss and changing gauge state | No shot has settled | VT-003 |
| Toss active | Press A or B with a chosen direction | Flat or slice, with sampled gauge contribution to speed | Aim, class and speed differ | VT-003 |
| First serve lands outside its box | Resolve fault | Same point starts its second attempt | No new point | VT-006 |
| Legal net-touch serve | Resolve let | Repeat the current attempt | No additional fault or point | VT-006 |
| Second attempt is also a fault | Resolve double fault | Receiver takes the point | No third attempt | VT-006 |
| Opponent has sent an available high ball | Move under it and request normal hit | Eligible contextual smash | Height and stance select contact | VT-004, VT-005 |
| Reach the ball at full stretch | Request a legal return | A weaker lunge can occur | An attempted hit does not guarantee contact or strength | VT-005 |
| A normal rally ball legally lands in and is not returned | Second bounce | Striker wins one point | Ball event feeds point ledger | VT-006, VT-007 |
| Both sides have 40 | Win one point, then let the other side win one | Advantage, then deuce | Single point alone does not win this match | VT-007 |
| One side has advantage | Same side wins the next point | Game credit and one-game Exhibition result | Complete match terminal | VT-002, VT-007 |

## Strategic and experiential structure

- Early positioning lets the player prepare a stronger ball, yet a cross-court
  pursuit can leave the other side exposed on reception.
- A deep ball, low return, lob or smash can trade pace and recovery position.
  Decide from the incoming ball's reachable geometry.
- The score and service feedback let a player distinguish a failed delivery,
  a lost live rally and a game that was still at advantage.
- Claim IDs: VT-003–VT-008.

## Replay and variation

- Same court, score rules and roster preserve comparison across attempts.
  Service meter sampling, pre-contact aim and the opponent's live returns
  vary how each run reaches the terminal. This analysis does not infer
  a seeded CPU policy or exact trajectory coefficients.
- Claim IDs: VT-002–VT-008.

## Adjacent systems and history

- The full-set profile enters additional game and tie-break logic. Changing
  the settings can also suppress deuce. These are distinct test surfaces.
- Arcade continues and World Circuit progress remain separate mode rules.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-774, ACT-775 | A/B serve, normal or lob, direction and depth |
| System Behaviour | SYS-146, SYS-1674, SYS-1675, SYS-1676, SYS-1677, SYS-1678 | Gauge speed, readiness, reach, service and point bookkeeping |
| Constraint | — | Receiving box, singles lines, legal contact, one game |
| Information | INF-544 | Gauge, attempt and speed with game and point score |
| Objective | OBJ-313 | Complete one-game Exhibition |
| Time | TIM-003 | Live serve and rally progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `570` (`GAME-0001`–`GAME-0570`).
- Exact genome matches: none.
- Tied near matches: `GAME-0391` — Uncharted 2: Among Thieves (`2 / 15 = 0.133333`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0391` — Uncharted 2: Among Thieves | ACT-008, TIM-003 | Both use direct movement while an immediate spatial situation changes. Uncharted 2 follows an authored escape and recovery route. Virtua Tennis instead intercepts a live ball, commits an aimed return and adjudicates repeated points to a winner. | Tied near: 2 / 15 = 0.133333 |

### Preserved research notes

- New genes: ACT-774, ACT-775, SYS-1674 through SYS-1678, INF-544 and OBJ-313.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_317](../../../research/taxonomy-changes/TAXONOMY_CHANGE_317.md)
  records the boundaries and comparisons to general delivery and score genes.

## Negative results

- The documented Dreamcast manual path's use of Arcade within its Exhibition
  paragraph is an instruction typo. Arcade does not own the chosen profile.
- The pinned source does not establish exact real hardware speed calibration
  or the frame window or court tolerances in another region.

## Delta summary

## New facts

- [Observation | Corroborated | High] VT-002–VT-008 distinguish two-command
  serve, gated contact and legal game/match settlement.

## New genes

- [Observation | Corroborated | Medium] Nine additions in taxonomy change 317.

## New combinations

- [Observation | Corroborated | High] No new combination proposed. Existing
  supported subsets are owned by the comparison section.

## Taxonomy changes

- [Observation | Corroborated | Medium] Predecessor definitions and
  signatures stay unchanged.

## New questions

- A version-verified native run can measure exact interception timing,
  variation in the flight arc, recovery after a weak save and ties at lines.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0572, Neon White for Nintendo Switch.
- Optimisation criterion: alternate platform and era. Contrast timing one
  racket contact with consuming a movement-card option on a timed route.
- Backlog impact: fifth Selection 046 unit.

## Why this game

- [Hypothesis | Limited | Medium] One full configurable point-to-match
  pipeline gives an observable relation between embodied commitment,
  causal ball motion and nested score states.
