# Taxonomy Change 126: obstacle-stopped cardinal bomb rays

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-09-24
- Trigger: `GAME-0387` Super Bomberman, original English PAL UK SNES Normal
  Game stage 1-1.
- Scope: one additive Active gene. No older signature, lifecycle, family
  definition or verified combination changes.

## Problem and accepted change

Existing `ACT-270` already admits reusable timed bomb placement, and
`SYS-470` already resolves a bomb's bounded damage to actors and compatible
terrain. Neither determines which cells a bomb can reach when four straight
tile-grid rays stop at different wall classes. `SYS-1045` therefore records
the propagation calculation before damage resolution. Bomb capacity, fuse
and firepower are parameters, not additional genes. `SYS-755` handles a soft
block's loss of collision and any exposed contents; `CON-402` handles the
enemy-clear exit gate.

## Transfer and rejection test

A circular bomb radius through room space in The Binding of Isaac: Rebirth
still uses `SYS-470` but does not receive `SYS-1045`. Super Metroid's Morph
Ball bombs also retain `ACT-270` and `SYS-470` without proof of four
tile-aligned blocked rays. `SYS-1045` will transfer only where a future
source independently supports cardinal propagation and terrain occlusion.
No prior game is silently reclassified.

## Evidence and limits

- [Original English UK Super Nintendo
  booklet](https://www.retrogames.cz/manualy/SNES/Super_Bomberman_-_SNES_-_Manual.pdf)
  establishes the normal-stage bomb/block/exit rules and depicts the
  orthogonal blast.
- [Original-SNES first-stage written
  route](https://gamefaqs.gamespot.com/snes/588720-super-bomberman/faqs/30299)
  corroborates bomb range and soft-block passage-making.
- No PAL cartridge, executable, frame-timed collision or exact tile map was
  directly inspected. The source-bounded gene claims ray geometry and
  blocker ordering, not per-frame chain-reaction timing.
