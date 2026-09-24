# Taxonomy Change 129: authored support loss during a bounded escape

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-09-24
- Trigger: `GAME-0391` Uncharted 2: Among Thieves, original PS3 opening
  suspended-train escape through the stable cliff ledge.
- Scope: two additive Active genes; no earlier genome, lifecycle, family
  definition or verified combination is changed.

## Problem and accepted change

Direct movement and universal falling do not encode a support that the author
breaks during an active climb, leaving a new required route. A static-location
objective does not encode the deadline to abandon a sequence of collapsing
supports before attaining safe ground.

- `SYS-1049` isolates authored pose or connection failure of a currently
  usable support; a preliminary break can redirect rather than kill.
- `OBJ-231` requires escape from that finite collapsing route to a stable
  designated exit, not chapter or campaign completion.

## Transfer and rejection test

`ACT-008`, `SYS-036` and `TIM-003` cover direct movement, gravity/collision
and real-time response. `SYS-147` models damage-driven cascading structural
loss, not an author-triggered climb redirection; `OBJ-026` fits an ordinary
spatial arrival after making a target traversable, not an active collapsing
route. Rail colour, car angle, protagonist name and event frame values are
parameters. Checkpoint behavior and later combat are not admitted without
evidence in the selected interval. No older signature is retrofitted from a
single new example.

## Evidence and limits

- [BradyGames' 2009 official guide sample](https://ptgmedia.pearsoncmg.com/images/9780744011166/samplepages/1116-6_uncharted2.pdf)
  documents the original PS3 opening climb, scripted pipe and seat failures,
  final falling car and cliff exit.
- [GameFAQs' original-PS3 route](https://gamefaqs.gamespot.com/ps3/955125-uncharted-2-among-thieves/faqs/58006)
  and [Gamepressure's Chapter 1 route](https://www.gamepressure.com/uncharted-2-among-thieves/a-rock-and-a-hard-place/zccea3)
  corroborate the qualitative order.
- No original disc or executable was played. Exact difficulty, trigger frames
  and checkpoint restoration remain unverified and are not gene parameters
  asserted as values.
