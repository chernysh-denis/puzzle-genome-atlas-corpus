# Taxonomy Change 138: Evolved score-arena control and rewards

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-09-25
- Trigger: `GAME-0400` *Geometry Wars: Retro Evolved*, original Xbox 360
  single-player Evolved score run from start to life-stock exhaustion.
- Scope: admit `ACT-536`, `SYS-1066`–`SYS-1070`, `CON-694` and `INF-398`
  as Active. No older signature or verified combination changes.

## Problem and accepted change

Microsoft's official listing separates Retro and Evolved; two independent
contemporary Xbox 360 Evolved guides describe freely moving a ship while
firing in another direction, finite bombs, a life-local kill multiplier,
changing hostile formations and repeated score awards. Existing direct
movement, aimed attack, live combat, finite-life recovery, score objective
and real-time input are reused. Eight new boundaries preserve what those
general genes do not say: the emergency action, open-ended spawn response,
per-life multiplier, gun-mode and stock awards, camera-limited scoreless bomb
response, optional bomb-stock legality and moving local view.

## Transfer and rejection test

- Independent left/right stick vectors are parameters of compatible
  `ACT-008` and `ACT-161`, not an extra gene for the controller hardware.
  Continuous right-stick fire is directly committed, unlike the automatic
  cooldown weapons in `SYS-573`.
- `SYS-572` requires authored minute-indexed survival-stage waves, and
  `SYS-908` requires a bounded reserve. Evolved's changing arrivals have
  neither source-supported exact minute schedule nor finite final reserve;
  `SYS-1066` records only supported open-ended pressure.
- `SYS-965` is one threshold awarded once. Evolved repeatedly grants a life
  every 75,000 points and a bomb every 100,000; `SYS-1069` keeps these
  schedules independent and does not assert a score payment.
- `CON-183` gates the run's failure, whereas `CON-694` limits an optional
  bomb and permits play without one. `ACT-270` places a delayed spatial bomb;
  the trigger-committed arena clear is `ACT-536`, resolved by `SYS-1070`.
- Full visibility `INF-001` would falsely imply that a bomb clears every
  current enemy. `INF-398` retains off-screen live threats without claiming
  their precise positions are known to the player.
- The original Retro mode, sequel Geoms, online board submission, the exact
  upgraded-gun selector, hostile spawn probabilities and black-hole internal
  sequence are excluded or left as source limits, not promoted as facts.

## Evidence and limits

- [Xbox official listing](https://www.xbox.com/en-us/games/store/Geometry-Wars-Evolved/BP5G8K2M71PM)
  identifies the two modes and publisher but does not supply frame-level rules.
- [Byrdpire's contemporary Xbox 360 guide](https://gamefaqs.gamespot.com/xbox360/930851-geometry-wars-retro-evolved/faqs/40235)
  documents the controls, screen-bound bomb, score awards and kill-count
  multiplier, while explicitly not resolving the gun selector.
- [sleepyjack's independent Evolved guide](https://gamefaqs.gamespot.com/xbox360/930851-geometry-wars-retro-evolved/faqs/42425)
  corroborates those central rules and describes escalating arrival groups.
- [Contemporary 2006 review](https://bjorn3d.com/2006/05/geometry-wars-retro-evolved/)
  corroborates the three starting lives and bombs and the distinct score
  award intervals. No Xbox executable or audiovisual trace was inspected.
- The generated original illustration abstracts a plausible local state:
  one craft fires right while moving up-left past different visible hostile
  shapes and a distant black hole. It is not a game screenshot or evidence
  for exact enemy coordinates or fire rate.
