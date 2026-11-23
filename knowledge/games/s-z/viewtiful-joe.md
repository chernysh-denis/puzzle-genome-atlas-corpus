---
game_id: GAME-0580
slug: viewtiful-joe
game_title: Viewtiful Joe
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-223
    - ACT-229
    - ACT-295
  system:
    - SYS-020
    - SYS-112
    - SYS-368
    - SYS-369
    - SYS-398
    - SYS-578
    - SYS-1702
    - SYS-1703
    - SYS-1704
    - SYS-1705
    - SYS-1706
    - SYS-1707
  constraint:
    - CON-183
    - CON-841
  information:
    - INF-119
    - INF-319
  objective:
    - OBJ-002
    - OBJ-026
    - OBJ-029
  time:
    - TIM-003
    - TIM-040
---

# Game: Viewtiful Joe

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Spend time in Slow to change what a falling drop or rising strike can do.
Learn Mach Speed and sprint under the barrel, then light the four pillars
while enough of the earlier flames are still burning.

## Analysis scope

- Version / ruleset: North American English Nintendo GameCube
  full retail release of 7 October 2003, disc DOL-GVJE-USA.
  Joe on Adults, ordinary first-run abilities and default controls.
  Exactly Episode 1, Joe the Hero, Stage 2. Disc revision and inputs
  within individual animation frames are unverified.
- Structured analysis target: PLAT-NINTENDO-GAMECUBE.
  See [platform coverage](../../platforms/games.json).
- Entry: start in the cellar immediately after clearing the helicopter
  and leaving the intervening break screen, with Slow already available.
  The first task has a dripping switch, reachable passages and an
  unlearned Mach Speed. No optional shop purchase is required or used
  to define this replay. Inherited health, points and film count may vary.
- Primary decision loop: read attack height, position and the VFX reserve.
  Dodge, strike or reposition while threats continue. Use Slow to change
  eligible objects and open attacks. Learn Mach Speed from Captain Blue,
  then switch effects to clear the barrel, outpace the hazards and ignite
  the final fixtures. Release VFX when safe enough to recover.
- Positive exit: make the four pillar flames overlap, pass the opened
  route and reach the next break. Stop before the distinct final
  Charles the 3rd boss stage; interim scene grades do not replace the
  passage checks.
- Negative exit: exhausting VFX alone removes hero affordances until
  recovery. Health loss instead costs an attempt when all life marks
  disappear. The finite L.I.V. stock permits retry. Exact restoration
  of film, grade categories or damage after an arbitrary retry is
  unverified.
- Included: embodied movement and strikes, high/low dodge, health and
  retry, the shared VFX meter, film capacity milestones, Slow and
  its local effects, scored attack chains, second Captain Blue trial,
  Mach Speed, barrel passage and chase hazards, and simultaneous ignition.
- Excluded: the preceding helicopter and reel puzzle, Charles's
  separate stage, the later Zoom ability, optional purchases,
  unlockable actors, other difficulties, the GameCube preview disc,
  Japanese Revival and PlayStation 2 ports.
- Potential scoped modules: Charles the 3rd's complete encounter or the
  Episode 2 post-Zoom sewer passage.
- Direct-play status: not conducted. The US GameCube booklet, two
  written GameCube routes and static released GameCube frames establish
  the controls, stage bounds and relevant transitions. The Adults
  recording uses a backward-compatible Wii to run the GameCube game.
  A separately labelled Kids recording corroborates only common object
  and interface details. No game executable, video playback, audio or
  native input timing trace was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| VJ-001 | Capcom's North American GameCube retail release shipped 7 October 2003. Adults is an ordinary starting difficulty. The second subdivision begins after the helicopter checkpoint and ends before the Charles stage. | Observation | Corroborated | High | P1, P2, R1, W1, W2 |
| VJ-002 | Slow and learned Mach Speed are actively requested with L and R. Active effects spend a shared gauge; off-mode play restores charge. Zero forces human Joe, temporarily losing VFX and the double jump until sufficient recovery. | Observation | Corroborated | High | P1, P3, R1, R2 |
| VJ-003 | Ordinary direction and jump inputs move Joe. The indicated high/low attack can be ducked or hopped; an eligible missed attack leaves its attacker dazed and open. Punch or kick targets under Slow for linked impacts. | Observation | Corroborated | High | P1, R1, R2, W1 |
| VJ-004 | A wave awards and grades performance separately from eligibility to pass. V-Films count toward gauge capacity milestones, and Slow attack chains can multiply points through further eligible impacts. | Observation | Corroborated | High | P1, R1, R2, W1 |
| VJ-005 | During Slow, the falling drop grows and can activate the weight-sensitive cellar switch. Passing the fixture depends on the impact, not merely holding L or placing Joe there. | Observation | Corroborated | High | P1, R1, R2, W2 |
| VJ-006 | Defeating Captain Blue in his second trial teaches Mach Speed. It accelerates Joe's movement and blows; combined inputs permit faster movement while the scene stays slowed. VFX Zoom is learned later. | Observation | Corroborated | High | P1, P3, R1, R2, W1 |
| VJ-007 | A Slow uppercut displaces the large blocking barrel upward, giving Joe time to move beneath it using Mach Speed. Other separately authored barrel and spiked-cylinder pursuits require continued movement. | Observation | Corroborated | High | R1, R2, W1, W2 |
| VJ-008 | Repeated impacts in Mach Speed kindle fire for the cellar fixtures. The final route needs the four flames to overlap before an earlier flame goes out. | Observation | Corroborated | High | P1, R1, R2, W1, W2 |
| VJ-009 | The life marks and finite retry stock are separate. Damage reduces the former, a miss consumes an attempt and a checkpoint can be restored; exact preservation of every transient resource is unknown. | Observation | Corroborated | Medium | P1, R1, R2 |

## Basic data

- Capcom Production Studio 4 / Capcom. FAM-007 for modifying the size,
  weight and trajectory of objects to pass the route. FAM-010 for acting
  during live hostility and overlapping temporary fixture states.
- P1: [Capcom 2003 US GameCube booklet scans](https://vgvisualvault.blogspot.com/2018/05/viewtiful-joe-game-cube-us-manual-scans.html).
  Visually inspected pp. 8–25 for control, Adults, life and VFX gauges,
  film, tasks and score, dodges, Slow, Mach Speed and attack chains.
  The booklet illustrates transformed double-jump and a depleted human
  form. The exact duration of reversion remains unmeasured.
- P2: [Contemporary North American release report](https://www.gamespot.com/articles/viewtiful-joe-ships/1100-6076468/)
  and [physical product identifier](https://gamefaqs.gamespot.com/gamecube/562548-viewtiful-joe/data).
  Establish the October date and DOL-GVJE-USA catalogue ID.
- P3: [Nintendo's GameCube product page](https://www.nintendo.com/en-gb/Games/Nintendo-GameCube/Viewtiful-Joe-269292.html).
  Confirms the original controller-era product, two starting difficulty
  options and the movie-power premise. Its European date is not the
  North American date.
- R1: [GameSpot's Adults GameCube walkthrough](https://www.gamespot.com/articles/viewtiful-joe-walkthrough/1100-6077222/),
  Episode 1 section after the helicopter. Establishes the drop, second
  Captain Blue, learned acceleration, uppercut, pursuit and timed
  four-flame exit. The shop section supports the distinction between
  mandatory learning and optional upgrades.
- R2: [Megaqwerty's October 2003 GameCube account](https://gamefaqs.gamespot.com/gamecube/562548-viewtiful-joe/faqs/26237)
  and [WarriorofZarona's VFX documentation](https://gamefaqs.gamespot.com/gamecube/562548-viewtiful-joe/faqs/26257).
  Corroborate the separate form, relief after release, V-Film milestones,
  chains, both tempo inputs and the cellar transitions.
- W1: [WhiteKhakis's Adults GameCube recording](https://www.youtube.com/watch?v=EBYKxWu_WE8&t=1490s).
  Sampled storyboard stills at 24:50–32:50: cellar entry, combat and
  interim grades, second Blue trial, the Mach tutorial, barrel route
  and a lit fixture before the break. GameCube disc compatibility on
  Wii is the author's reported method. No binary or timing identity
  was inferred.
- W2: [LongplayArchive's NTSC GameCube recording](https://www.youtube.com/watch?v=dLMvXi_-j2E&t=1023s).
  Sampled 17:10–22:30 of the separately labelled Kids take as common
  route evidence only, including the large drop around 17:50 and
  transition before Charles. Its health, upgrades and rank are outside
  the Adults reconstruction.
- Sources accessed 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-008 moves Joe and jumps through the cellar geometry. ACT-295 sends
  ordinary character-owned punches and kicks, including the crouched
  uppercut against the blocking barrel (VJ-003, VJ-007).
- ACT-223 supplies a live high/low dodge choice. ACT-229 deliberately
  spends VFX to hold one available mode or an eligible combination
  (VJ-002, VJ-003, VJ-006).

### System Behaviour Genes

- SYS-020 changes the position of the barrel or hit foe in a
  direction set by the strike. SYS-112 opens authored downstream
  passages after the accepted fixture operation (VJ-005, VJ-007, VJ-008).
- SYS-368 drains one finite shared reserve while using effects and
  recovers it under eligible inactive play. SYS-1704 adds the human
  fallback and affordance restoration specifically at depletion
  (VJ-002).
- SYS-398 retains the new Mach Speed traversal capability after
  the second trial. It is available for the barrel and ignition gates
  later in the same stage (VJ-006–VJ-008).
- SYS-578 keeps a distinct health pool with damage and eligible
  recovery. SYS-369 restores an authored retry boundary rather than
  resuming the failed moment (VJ-009).
- SYS-1702 increases the effective switch impact of the slowed drop.
  SYS-1703 converts repeated accelerated hits into transferable fire
  for receptive fixtures (VJ-005, VJ-008).
- SYS-1705 dazes an eligible attacker after the opposite-height dodge.
  SYS-1707 extends the linked Slow scoring sequence over different
  eligible targets. A successful dodge alone does not do counter
  damage (VJ-003, VJ-004).
- SYS-1706 grows the usable reserve's capacity after collecting the
  declared film threshold. This differs from a recovery refill
  (VJ-004).

### Constraint Genes

- CON-183 separates the finite L.I.V. retry stock from life marks.
  CON-841 requires concurrently burning fixtures to pass the
  last door, so earlier expired states no longer count (VJ-008, VJ-009).

### Information Genes

- INF-119 covers the visible health and VFX resource. INF-319 covers
  the local high/low categories communicated by the attack cue, which
  call for complementary responses (VJ-002, VJ-003).

### Objective Genes

- OBJ-029 covers the required hostile sets, including the Captain Blue
  trial. OBJ-026 covers traversing the unlocked terminal passage.
  OBJ-002 covers the optional improvement of V-Points and bonus
  results without replacing either terminal requirement
  (VJ-004–VJ-009).

### Time Genes

- TIM-003 covers the live stage with moving traps, hostiles and decay.
  TIM-040 adds the independent held changes to scene and avatar
  progression, including combined Slow and Mach Speed (VJ-002, VJ-005–VJ-008).

## Reproducible transitions

| Before | Action or event | Bounded result | Claims |
| --- | --- | --- | --- |
| Small drop above the switch | Allow a normal drop to land, then compare a drop under Slow | The ordinary drop is insufficient; the visibly enlarged drop activates the fixture | VJ-005 |
| Enemy telegraphs at head height | Duck before overlap and follow with a strike | Eligible attacker becomes dazed, creating a counter opening; the dodge itself does not hit | VJ-003 |
| Enemy telegraphs low | Use the short upward dodge | Correctly clears the low strike instead of ducking into it | VJ-003 |
| Dazed first target and another nearby | Hold Slow and connect the follow-up or launch into another eligible target | Linked bonus can increase while VFX is being spent | VJ-003, VJ-004 |
| VFX active, reserve still positive | Release the input, then compare exhaustion on a separate attempt | Release permits recovery without the zero-induced human lockout; full depletion forces it | VJ-002 |
| Film count reaches an eligible milestone | Pick up the last needed film value | One extra capacity segment becomes available | VJ-004 |
| Second Captain Blue trial still active | Defeat Blue and complete the offered lesson | Mach Speed becomes available in the same attempt, apart from any shop purchase | VJ-006 |
| Giant barrel blocks passage | Uppercut it under Slow, then use Mach Speed to run underneath | The body temporarily stops blocking traversal at ground level | VJ-007 |
| Some pillar flames are lit | Keep moving and use repeated Mach Speed impacts on the remaining fixtures | All four burning together open the exit; an earlier expired flame has to be relit | VJ-008 |
| No life marks remain | Resolve the miss and use an available retry | Return to a permitted authored checkpoint, without asserting restored transient values | VJ-009 |

## Strategic and experiential structure

Reserve use changes which actions can succeed. Slowing the falling drop
gains access; slowing a fight opens longer opportunities to chain impacts.
Spending everything can remove the double-jump and both VFX effects when
the next spatial choice needs them. After the second tutorial, the
barrel needs two different effects in sequence. The final four pillars
change the planning problem again: ignition is useful only while the
other flames survive long enough for it to overlap.

## Replay and variation

This is one authored cellar sequence on Adults. Different timings,
optional pickups and starting reserve states can change the action
window and the performance grades. An efficient route can clear it
without purchasing equipment or extending every score chain. No
frame-exact damage, resistance, maximum VFX rate or rank cutoffs are
asserted.

## Adjacent systems and history

The North American controls and two starting difficulties are in the
retail manual. The Kids capture is comparative evidence for this common
cellar route. It makes no statement about Adults damage or opponent
counts. The optional store, full episode’s later boss and Zoom remain
separate scopes.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-223, ACT-229, ACT-295 | direct movement, height dodge, character strike and VFX request |
| System Behaviour | SYS-020, SYS-112, SYS-368, SYS-369, SYS-398, SYS-578, SYS-1702, SYS-1703, SYS-1704, SYS-1705, SYS-1706, SYS-1707 | displacement, fixtures, health, meter and retry, learned movement, drop, fire, forced form, daze, film, chain |
| Constraint | CON-183, CON-841 | finite retry stock and overlapping flames |
| Information | INF-119, INF-319 | life, VFX and attack height |
| Objective | OBJ-002, OBJ-026, OBJ-029 | scene combat, route terminal and optional performance |
| Time | TIM-003, TIM-040 | live hazards and separately altered tempo |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `579` (`GAME-0001`–`GAME-0579`).
- Exact genome matches: none.
- Tied near matches: `GAME-0293` — Ori and the Will of the Wisps (`7 / 36 = 0.194444`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0293` *Ori and the Will of the Wisps* | ACT-008, ACT-223, INF-119, SYS-369, SYS-398, SYS-578 and TIM-003. Both couple live movement and evasion with current health and resources, learned route affordances and checkpoint return. | Ori opens the first Spirit Gate with carried Keystones, obtains Spirit Edge and activates a saving and healing Spirit Well in Inkwater Marsh. Joe spends a recovering VFX gauge to change scene and actor tempo, and needs a weighted droplet, barrel launch and overlapping temporary fires in one cellar stage. | `7 / 36 = 0.194444`; closest earlier match. |

### Preserved research notes

- New genes: SYS-1702–SYS-1707, CON-841 and TIM-040.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_326](../../../research/taxonomy-changes/TAXONOMY_CHANGE_326.md)
  distinguishes rate changes, depletion, object effects and temporary
  ignition from the common action and resource boundaries.

## Negative results

- Reject TIM-037: movement itself does not set the scene’s rate. The
  explicit VFX input does.
- Reject SYS-061 for the drop switch. The impact triggers the route
  mechanism without a continuously occupying crate or body.
- Reject SYS-1378 for film capacity: local collection thresholds and
  reset boundaries differ from an acquired permanent single booster.
- Reject existing rapid-kill experience chains and full-parry counter
  damage as substitutes for the specific linked VFX scoring and daze.
- No gene for the exact number or name of props, tutorial titles, game
  character, colour or camera border. No later Zoom, return drill or
  indefinite ignition is inferred.

## Delta summary

## New facts

- [Observation | Corroborated | High] One shared reserve enables two
  effects that change live objects, traversal and combat differently.
  The final route requires four overlapping temporary ignitions.

## New genes

- [Observation | Corroborated | Medium] Eight additions in
  TAXONOMY_CHANGE_326.

## New combinations

- [Observation | Corroborated | High] No new verified combination
  proposed. The comparison owns the existing proper subsets.

## Taxonomy changes

- [Observation | Corroborated | Medium] Earlier signatures and
  definitions stay intact.

## New questions

- An Adults native input trace could delimit exact activation, refill,
  collision and ignition windows under isolated and combined effects.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0581, Hardspace: Shipbreaker on
  Xbox Series X|S. Analyse a complete salvage and its material routing.
- Optimisation criterion: move from direct changes to action tempo to
  the controlled disassembly and settlement of a persistent structure.

## Why this game

- [Hypothesis | Limited | Medium] The complete second stage separates a
  slow-motion effect from its route-specific physical consequences and
  tests the later acceleration under a different persistence constraint.
