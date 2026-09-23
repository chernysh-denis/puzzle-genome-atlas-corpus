# Taxonomy Change 105: Separate original Tekken Arcade routing from one duel

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Date: `2026-09-23`
- Trigger: `GAME-0366` Tekken 3 original PlayStation Arcade ladder.
- Scope: three new Active boundaries; no earlier signature or lifecycle
  changes.

## Problem

Street Fighter II and modern TEKKEN 8 supply reusable four-limb combat,
guard, throw, round and HUD genes. Neither one's bounded match represents
successive CPU opponents with an optional same-stage Continue. The former's
side-view stage is corner-bounded; the latter's 3D floor is walled. Reusing
either geometry for Tekken 3 would assert a false wall or remove its lateral
axis.

## Accepted change

- Add `SYS-1000` for Arcade match-result routing: next opponent on win or
  Continue at the lost stage with the selected fighter on loss.
- Add `CON-667` for opponent-relative open-floor spacing and lateral evasion
  without modern wall or ring-out settlement. Its wall-less material clause
  remains `Limited` because direct disc observation is absent.
- Add `OBJ-212` for clearing the entire fixed-fighter CPU ladder, separate
  from `OBJ-099`'s one-match round-win objective.
- Reuse fifteen earlier genes for selection, movement, posture, attack, guard,
  throw, live combat, round settlement, legality, match bounds, visual/HUD
  information and real-time input. Super Charger, Jin's exact moves and the
  manual's default 40-second timer are parameters, not extra genes.

## Lower-ID transfer test

- `GAME-0283` TEKKEN 8 contributes the closest four-limb, sidestep, guard,
  throw and round core. Its `CON-625` requires walls, while Heat, Rage and
  recoverable health do not exist in this scoped historical ruleset.
- `GAME-0351` Street Fighter II contributes the match/guard/throw core, but
  its `CON-443` is a side-view cornered line without lateral sidestep.
- `SYS-522` ends or resets rounds inside a match; it does not choose a next
  CPU opponent or offer a stage-local Continue. `OBJ-099` ends one fixed
  opponent match, not a sequence. `CON-625` and `CON-443` fail the geometry
  boundary for opposite reasons.
- No verified combination is registered from a single newly reviewed
  carrier. The complete signature comparison is computed in the game record
  and checked by repository validation.

## Evidence and limits

Namco's original PlayStation instruction manual directly states the Arcade
opponent-clear rule, unlimited same-stage Continue, sidestep, four-limb
controls, guard matrix, draw and round rules. The open/wall-less historical
stage classification is secondary; no licensed disc was run, so `CON-667`
has lower confidence and no precise geometry, attack-tracking or opponent
order is invented. Existing genes and game signatures remain unchanged.
