# Taxonomy Change 113: Open-city race settlement and destination cues

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-23
- Trigger: `GAME-0374` Burnout Paradise, original Xbox 360 offline ordinary
  Race with a Stunt-class Boost car.
- Scope: two additive Active genes; no earlier signature, lifecycle or
  verified-combination changes.

## Problem

An ordinary Burnout Paradise Race does not require a fixed course, lap or
ordered checkpoint. Existing circuit-race rules cannot explain how different
legal street choices converge on one finish banner and produce an arrival
order. Existing driving HUD boundaries likewise do not capture the compass
destination bearing, remaining distance and suggested junction turns that
inform but do not mandate a route.

## Accepted change

- `SYS-1020` settles one open-city point-to-point race by valid arrival beneath
  its named banner and relative order against autonomous rivals, without
  intermediate checkpoint or lap validation.
- `INF-381` exposes live destination bearing, vehicle heading, distance and
  junction turn suggestions while preserving street choice.

## Lower-ID transfer and rejection test

- `ACT-290`, `ACT-293` and `ACT-309` transfer direct vehicle control, event
  commitment and Boost spending. `SYS-320`, `SYS-519`, `SYS-691` and `SYS-765`
  transfer vehicle contact, retained win, acceleration and Stunt manoeuvre
  charging. `INF-206`, `OBJ-134` and `TIM-003` transfer mapped event
  disclosure, a rival-race terminal and live timing. Their definitions remain
  unchanged.
- `SYS-515` assumes rivals on a shared course, and `SYS-516` requires ordered
  checkpoints or laps. Neither is expanded to erase the documented open-city
  route freedom. `INF-204` couples route guidance with speed and gear; it does
  not isolate this destination vector and optional turn advice.
- No verified combination is a proper subset of this signature. An ordinary
  Race cannot inherit Road Rage, Marked Man or Showtime goals.

## Evidence and limits

Electronic Arts' original Xbox 360 Burnout Paradise manual, pp. 2, 4–5 and 6,
documents the map and event start, ordinary Race route freedom, compass and
distance, finish banner, licence win and class-specific Boost. No Xbox 360
disc, save, direct-play trace, exact rival path or ordinary Race crash/retry
transition was inspected.
