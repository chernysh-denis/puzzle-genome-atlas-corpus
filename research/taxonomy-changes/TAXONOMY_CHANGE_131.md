# Taxonomy Change 131: live fighting guard is not a button label

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-24
- Trigger: `GAME-0393` original North American SNES *Mortal Kombat II*, one
  first CPU match using the original `SNS-28-USA` booklet.
- Scope: wording generalisation of existing Active `ACT-296`. No existing
  genome signature, lifecycle or verified combination changes.

## Problem and accepted change

The original definition of `ACT-296` made a hold-away direction part of the
gene identity. The SNES booklet instead gives L and R as block inputs while
the same live action is to sustain, then release, a protective guard relative
to an incoming opponent. A distinct ID merely for the controller button
would encode hardware mapping rather than an operational rule. The definition
now identifies the continuing guard request and treats hold-away versus L/R
as a carrier parameter. Standing/crouching posture and attack class remain
parameters, not proof that every attack can be blocked.

## Transfer and rejection test

Existing Street Fighter and Tekken signatures continue to denote the same
defensive action under their directional mappings. This edit does not add a
guard gene to a previously unreviewed game or claim that SNES MKII's block
window equals an arcade or modern game's timing. `ACT-202` separately owns
crouching posture; `ACT-295` owns attacks, and `SYS-215` resolves whether an
actual contact is guarded. A one-off timed parry, armour from an attack,
turn-based defend action and shooter cover stay outside `ACT-296`.

## Evidence and limits

- [Original SNES *Mortal Kombat II* booklet,
  `SNS-28-USA`](https://www.videogamemanual.com/snes/Mortal%20Kombat%20II%20%28USA%29.pdf),
  pp. 12–17, directly identifies L/R block beside directional movement and
  punch/kick controls.
- [Original arcade operations
  manual](https://r.mprd.se/MAME/manuals/arcade/mk2.pdf), p. 12, documents
  a different panel. It is contrast, not a substitute SNES control source.
- No cartridge or binary was played; exact block timing and attack
  compatibility are not imported into the gene wording.
