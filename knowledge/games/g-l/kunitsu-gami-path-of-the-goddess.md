---
game_id: GAME-0583
slug: kunitsu-gami-path-of-the-goddess
game_title: "Kunitsu-Gami: Path of the Goddess"
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-036
    - ACT-161
    - ACT-189
    - ACT-223
    - ACT-341
    - ACT-786
  system:
    - SYS-045
    - SYS-046
    - SYS-112
    - SYS-215
    - SYS-578
    - SYS-1719
    - SYS-1720
    - SYS-1721
    - SYS-1722
  constraint:
    - CON-136
    - CON-330
  information:
    - INF-119
    - INF-554
  objective:
    - OBJ-319
  time:
    - TIM-003
    - TIM-041
    - TIM-042
---

# Game: Kunitsu-Gami: Path of the Goddess

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Spend the same crystals on the route or on defenders. Protect Yoshiro
where night finds her, then finish the route and purify the gate.

## Analysis scope

- Version / ruleset: complete US PlayStation Store release of 19 July
  2024, product UP0102-PPSA19576_00-KUNITSUGAMI00000, native PS5 base
  game and first solo campaign visit to Myoko Pass. Use the ordinary
  starting capabilities, default controls and no carried upgrade bonuses.
  The installed version and exact native input timings are unverified.
- Structured analysis target: PLAT-PLAYSTATION-5.
  See [platform coverage](../../platforms/games.json).
- Entry: select Myoko Pass immediately after the introductory mountain
  sequence. Yoshiro is alive at the near end of the pass, villagers
  remain to be freed, and the final Torii Gate is defiled. The first
  deployment offers Woodcutter as the combat role.
- Primary decision loop: directly move Soh to cleanse local sources and
  free villagers. Divide the single crystal stock between equipping
  Woodcutters and extending the Spirit Path. Choose where to leave
  Yoshiro by dusk, place defenders using the command screen, then fight
  near them as the Seethe advance. Keep the maiden alive until dawn.
  Use remaining or newly recovered crystals to finish the path and
  escort her into range of the final purification.
- Positive exit: reach the far gate with Yoshiro, perform its
  purification and obtain the Myoko Pass clear result. The first
  reconstructed clear has one night and finishes after the next dawn.
  Dawn alone only returns to preparation. Stop before the successor
  base repairs and the Gakinyudo boss encounter.
- Negative exit: Yoshiro's health reaching zero ends the attempt.
  Exhausting Soh's own health instead incurs a temporary spirit
  interval while the protected target can still be attacked. Spending
  the crystals too early can leave the route unfinished at sunset.
  The exact restart point after failure was not independently verified.
- Included: daytime purification, freeing villagers, field crystal
  and ration use, held route extension, Yoshiro's follow and hold
  commands, Woodcutter conversion and placement, ordinary blade and
  Oka Dance attacks, the phase timer, Yoshiro's survival, dawn and
  gate settlement. Full local cleanup may earn a wayshrine reward.
- Excluded: PS4, preview and promotional demo builds, bonus talismans,
  custom equipment and upgrades, Archers and later masks, the later
  boss and base repairs, New Game Plus, post-launch modes, exact
  damage, costs across other stages and save/reload claims.
- Potential scoped modules: Gakinyudo through its distinct role
  unlock, or Yuan Cavern with a lantern-dependent defence.
- Direct-play status: not conducted. The native PS5-labelled recording
  was sampled as static images, with its German interface identified
  separately from the English store and manual. A full-release Windows
  capture corroborates common mechanics and names. The first-night
  survival, final purification and result are visually corroborated.
  The zero-health branch is grounded in the official manual. No
  executable, audio, or video playback was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| KG-001 | The US full game released on 19 July 2024 with a native PS5 version. Myoko Pass is the first ordinary route stage after the prologue and its clear precedes Gakinyudo. | Confirmed | Direct | High | P1, P2, W1, W2, R1 |
| KG-002 | Approaching and purifying eligible defilement yields crystals or frees the enclosed villager. Purging the region's required spots permits local wayshrine rewards. Rations can restore Soh or villagers. | Observation | Corroborated | High | P3, W1, W2 |
| KG-003 | Holding the action at the route tip spends crystals to extend a persistent path on the fixed corridor. Yoshiro follows, stops at the tip, or waits on command. The basin shows phase time and the tip marker signals whether arrival in time for purification is feasible. | Observation | Corroborated | High | P3, W1, W2 |
| KG-004 | Assigning an eligible role spends the same balance. On first Myoko Pass the Woodcutter is the only combat role. A separate time-pausing command screen lets the player place individual villagers, who then defend autonomously when the simulation resumes. | Observation | Corroborated | High | P3, W1, W2, R1, R2 |
| KG-005 | Dusk stops Yoshiro's progress and introduces Seethe at the defiled gate. They seek Yoshiro. The player can accelerate daytime after the tutorial, independently of the tactical pause. At dawn the stage returns to the preparation phase. | Observation | Corroborated | High | P1, P3, W1, W2, R3 |
| KG-006 | In live battle Soh can move, dodge and attack while Woodcutters fight nearby threats. The Oka Dance finisher changes shape with preceding normal strikes. Defeated enemies yield crystals. Getting too close to the defiled gate's damaging area can expose Soh or villagers. | Observation | Corroborated | High | P3, W1, W2, R2 |
| KG-007 | Yoshiro's health at zero is terminal. At zero health Soh becomes a spirit for a recovery interval. Rations are for Soh or villagers, with separate rules for Yoshiro's viability. | Observation | Corroborated | High | P3, R2 |
| KG-008 | After surviving to dawn the path can be resumed and extended. When Yoshiro reaches the far gate an eligible on-site purification finishes the stage and displays its result. The boss is a separate encounter. | Observation | Corroborated | High | P3, W1, W2, R1 |

## Basic data

- Capcom. FAM-010 for the running preparation and defence clock and
  FAM-015 for individually positioning autonomous defenders along
  the moving protection problem.
- P1: [US PlayStation Store full base product](https://store.playstation.com/en-us/product/UP0102-PPSA19576_00-KUNITSUGAMI00000).
  Identifies native PS5 delivery, 19 July 2024 and the distinct
  full, demo and bundled listings.
- P2: [Capcom's dated launch notice](https://www.capcom.co.jp/ir/english/news/pdf/e240718.pdf).
  Confirms the July 19 full release and PS5 among the target carriers.
- P3: [Full-game Capcom PS5 web manual](https://game.capcom.com/manual/kunitsu-gami/en/ps5/page/3/1).
  Read the [English content served to the manual](https://game.capcom.com/manual/kunitsu-gami/locale/data/en.json):
  Stage Progression sections Basic Info, Daytime, Nighttime, Torii Gate
  Purification and Mission Rewards. These establish phase transitions,
  pay-for-path and role rules, control, ration use, failures, finishers
  and the final purification. Tutorial and release evidence constrain
  which systems and roles occur at Myoko Pass.
- W1: [Padautz's 20 July 2024 PS5 walkthrough](https://www.youtube.com/watch?v=C0qnXJJVa1A).
  German interface. Static storyboards from 12:50–16:30 show stage
  entry, purification and the Woodcutter role. At 18:20–21:00 they show
  route preparation, the shrine, acceleration tutorial and positioning.
  At 21:10–24:30 they show the defiled gate, combat, relocation and
  accumulating crystals. At 24:40–26:20 they show the return to
  preparation, gate purification and the Myoko Pass result.
- W2: [Gamer's Little Playground's full-release PC walkthrough](https://www.youtube.com/watch?v=kBzpzyBtbD8).
  The author identifies Steam. Static frames at 10:00–22:30 show the
  English stage introduction, Woodcutter, status cues, moving path and
  night change. At 22:40–26:40 they show battle, dawn and purification.
  Supports common rules only. The exact platform build parity and
  adjustment settings were not measured.
- R1: [Dayngls's July 2024 guide to first-run objectives](https://daynglsgameguides.com/2024/07/26/kunitsu-gami-path-of-the-goddess-objectives-guide/).
  Myoko Pass confirms that the multiple-role objective is for a revisit.
  Gakinyudo is separate. Optional kills and role variety do not replace
  the stage's gate terminal.
- R2: [Push Square's July PS5 review](https://www.pushsquare.com/reviews/ps5/kunitsu-gami-path-of-the-goddess).
  Corroborates the resource tension, paused placement screen and
  local field-of-view constraint. The PS5 release footage and the
  manual delimit the first-run scope more narrowly than the review.
- R3: [GamingTrend's release rules account](https://gamingtrend.com/reviews/kunitsu-gami-path-of-the-goddess-review-the-best-defense-is-a-good-offense/).
  Corroborates Yoshiro stopping at dusk and the available daytime
  acceleration. The reconstruction does not require exact timing.
- Sources accessed 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-008 moves Soh around the pass. ACT-341 purifies reachable cases,
  frees villagers and interacts with the final gate or with Yoshiro's
  wait control. ACT-786 holds the current Spirit Path tip to extend it
  (KG-002, KG-003, KG-008).
- ACT-036 assigns an available Woodcutter role. ACT-189 places
  individual defenders through destination orders. ACT-161 supplies
  the blade strikes. ACT-223 supplies an authored live dodge decision
  against attacks (KG-004, KG-006).

### System Behaviour Genes

- SYS-045 advances non-steered bodies through the level, including
  Seethe approaching Yoshiro. SYS-046 resolves autonomous Woodcutter
  strikes according to the assigned role (KG-004–KG-006).
- SYS-112 changes the connected fixture state after a proper
  purification. SYS-215 resolves directly played real-time hits.
  SYS-578 holds health damage and admitted healing distinct from
  progress toward the gate (KG-002, KG-006–KG-008).
- SYS-1719 consumes one crystal supply for both roles and route.
  SYS-1722 makes the guide walk the prepared segment and stop at
  its tip, a wait order, or the defence boundary (KG-002–KG-006).
- SYS-1720 restores Soh after a distinct spirit interval while
  Yoshiro has a separate terminal condition. SYS-1721 changes the
  dance finisher based on the count of preceding strikes (KG-006, KG-007).

### Constraint Genes

- CON-136 keeps earlier prerequisites binding. The traveller and
  reachable end of the prepared route are required for the final
  gate. CON-330 requires that the protected, mission-critical
  Yoshiro stays viable (KG-003, KG-007, KG-008).

### Information Genes

- INF-119 makes current health and supplies available before acting.
  INF-554 displays the phase horizon and the tip cue for an eligible
  gate arrival (KG-003, KG-005, KG-007).

### Objective Genes

- OBJ-319 requires preserving the living traveller until the final
  local purification. Successful defence alone returns work to the
  path on the same stage (KG-005, KG-007, KG-008).

### Time Genes

- TIM-003 covers the live timing of actions, movement and hazards.
  TIM-041 adds repeated timed preparation and assault with optional
  daytime acceleration. TIM-042 suspends the scene while giving
  positional defender orders and then resumes it (KG-004–KG-008).

## Reproducible transitions

| Before | Action or event | Bounded result | Claims |
| --- | --- | --- | --- |
| Sealed villager and nearby defilement sources | Approach and purify them | Restore control options and collect the relevant crystals | KG-002 |
| Prepared path has a visible tip and the stock is positive | Hold interact at that tip, then release | The route extends along the corridor, debits crystals and persists after release | KG-003 |
| Free villager is unassigned and crystals cover the role cost | Choose Woodcutter | Shared stock falls and the villager gains a close-range autonomous combat role | KG-004 |
| First day still has time and available guards | Open placement, order one to a position, and close the view | Tactical positioning is chosen during a pause; autonomous movement proceeds after resume | KG-004 |
| Yoshiro is on the prepared path at the end of daylight | Let dusk arrive and defend her position | Her route progress halts and Seethe emerge and approach the protected position | KG-005, KG-006 |
| A suitable target is ahead and Oka Dance is available | Compare a direct dance attack with one normal strike followed by dance | Selected finisher changes from forward attack to a rising cut | KG-006 |
| Soh or Yoshiro is threatened at low health | Resolve zero health in the respective pool | The manual distinguishes temporary spirit recovery for Soh from stage failure for Yoshiro | KG-007 |
| Yoshiro survives until dawn and the gate is still defiled | Extend the remaining path, let her reach the gate and trigger purification | The stage settles only after the final purification | KG-008 |

## Strategic and experiential structure

Every crystal can move the protected character farther or add a guard
to the current formation. More progress can therefore expose her farther
from the chosen defence without leaving enough for the role that protects
it. A good position can preserve Yoshiro without reaching the gate that
day. After surviving, the player still has to convert the time and value
gained at night into a complete route and final action.

## Replay and variation

One night is the observed first clear, not a global objective or
guarantee. Different resource decisions and pauses can change where
Yoshiro stops and whether another night is required. Record role costs
and thresholds qualitatively across routes. Returning later can enable
more masks and replay missions, outside the scoped first performance.

## Adjacent systems and history

A released introductory stage can share concepts with the earlier demo
without establishing identical setups. Only the July commercial base
game is the target. Mid-stage gate recovery, boss-only movement orders
and unlocked role combinations require separate modules.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-036, ACT-161, ACT-189, ACT-223, ACT-341, ACT-786 | Soh, assigned Woodcutters, targeted actions, blade, dodge and held path extension |
| System Behaviour | SYS-045, SYS-046, SYS-112, SYS-215, SYS-578, SYS-1719, SYS-1720, SYS-1721, SYS-1722 | autonomous movement and role, live battle, health, shared crystals, body recovery, dance and guided movement |
| Constraint | CON-136, CON-330 | prior preparation and designated traveller survival |
| Information | INF-119, INF-554 | health and supply, time and Spirit Path tip |
| Objective | OBJ-319 | protected final gate purification |
| Time | TIM-003, TIM-041, TIM-042 | live play, day and night boundaries, daytime acceleration, tactical placement pause |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `582` (`GAME-0001`–`GAME-0582`).
- Exact genome matches: none.
- Tied near matches: `GAME-0473` — Eternal Darkness: Sanity's Requiem (`8 / 32 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0473` — Eternal Darkness: Sanity's Requiem | ACT-008, ACT-161, ACT-341, INF-119, SYS-045, SYS-215, SYS-578, TIM-003 | Both put a direct fighter among moving enemies, contextual fixtures and health resources. Ellia crosses the tomb by managing sanity, selecting aimed strikes and solving a staff-and-fixture route. Soh spends crystals on positions and escort distance, with a live night defence protecting someone other than the controlled fighter. | `8 / 32 = 0.250000` |

### Preserved research notes

- New genes: ACT-786, SYS-1719–SYS-1722, INF-554, OBJ-319 and TIM-041–TIM-042.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_329](../../../research/taxonomy-changes/TAXONOMY_CHANGE_329.md)
  distinguishes resource use, route preparation, night defence and the
  separate actor and escort failure conditions.

## Negative results

- Reject SYS-416 as a substitute for the stage's timed phase contract.
  A day-night ecological spawn schedule alone does not encode the
  separate defence role, dusk stop and preserved escort progress.
- Reject TIM-027 as a substitute for positional planning. The Mass
  Effect boundary commits radial power and equipment choices rather
  than field positions for autonomous guards.
- Reject OBJ-020: dawn can end the assault while leaving the final
  goal unmet, and the stage does not require a total kill threshold.
- Reject SYS-1419: Soh's temporary absence is not a cooldown-priced
  partial revive that becomes terminal on another depletion.
- No gene for exact menu glyphs, frame timing, displayed counts from
  a single run or the colours alone. No post-launch or later role
  systems are attributed to the first visit.

## Delta summary

## New facts

- [Observation | Corroborated | High] The same earned crystals fund
  escort progress and defender conversion. Dusk freezes the escort
  position while combat runs. The final gate, not the first dawn,
  settles the stage.

## New genes

- [Observation | Corroborated | Medium] Nine additions in TAXONOMY_CHANGE_329.

## New combinations

- [Observation | Corroborated | High] No new verified combination
  proposed. Existing subsets are listed in the comparison.

## Taxonomy changes

- [Observation | Corroborated | Medium] Earlier definitions and
  signatures are retained.

## New questions

- A controlled PS5 run could measure crystal debit granularity, the
  zero-health recovery interval and outcomes from deliberately
  missing several dusk boundaries.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0584, North American Saturn
  Bomberman. Analyse one complete released battle round with clear
  starting conditions, legal bombs, item effects and terminal rules.
- Optimisation criterion: contrast the moving escort's stage clock
  with a discrete arena geometry and live opponent choices.

## Why this game

- [Hypothesis | Limited | Medium] Myoko Pass closes a full local
  preparation, defence and settlement loop with clearly recorded
  pacing, paid opportunities and different consequences of depletion.
