# Taxonomy Change 149: Level-scaled match scoring

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-26
- Trigger: `GAME-0411` *Bejeweled 3*, original PC Classic mode.
- Scope: admit `SYS-1095` as Active; no earlier signatures or verified
  combination memberships change.

## Problem and accepted change

PopCap's original PC readme explicitly awards different base values to
ordinary matches, specials and successive cascades, then multiplies all
Classic base values by the current level number. Existing match-3 genes
resolve the board but do not represent this evaluation transition.
`SYS-1095` isolates the score function while `SYS-012` retains cascade
settlement and `OBJ-002` retains the player's score-maximisation objective.

## Transfer and rejection test

- `SYS-028` requires ordered, card- and modifier-driven additive versus
  multiplicative phases; Classic has no player-reordered modifier tableau.
- `SYS-012` permits reward scaling as a parameter of a cascade, but it does
  not itself award pattern-specific points or multiply all Classic awards by
  the current level. The two boundaries are independently testable.
- The escalating overall account rank is outside the bounded session and is
  not smuggled into the level-number multiplier.
- `TIM-003` already admits player input during a live, forced resolution
  window; it applies only during falling-gem intervals here, not as a claim
  that Classic has a continuous deadline between swaps.

## Evidence and limits

- [PopCap's original PC Bejeweled 3 readme](https://bejeweled.wiki.gg/wiki/Bejeweled_3/readme.html)
  preserves the Basic Scoring (Classic and Zen) table, including cascade
  bonus and level-number multiplier, and the control note permitting matches
  while previous gems are falling. The original executable was not played;
  this is a source-bounded reconstruction.
