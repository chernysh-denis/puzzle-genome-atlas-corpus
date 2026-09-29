# Taxonomy Change 179: Delayed square clearing in original PSP Lumines

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-09-28
- Trigger: `GAME-0442` *Lumines: Puzzle Fusion*, original North American PSP Single Skin `Shinin'`.
- Scope: admit `SYS-1157`, `SYS-1158`, `SYS-1159` and `CON-716` as Active. No earlier signature or verified combination changes.

## Problem and accepted change

Superficial falling-block similarity to NES Tetris does not explain the player's decisions. Two-cell columns can settle at different heights. Four cells must first form a monochrome 2 × 2 square; a music-paced line later reaches and removes that eligible region. A marked Over block can extend its eventual clear to connected same-colour cells. The gap between forming a match and reclaiming board space is consequential under continuing gravity.

## Transfer and rejection tests

- Reuse `ACT-005`/`ACT-006` for pose and accelerated descent, `SYS-004`/`SYS-006`/`SYS-009` for incoming variation, gravity and successor introduction, and existing finite-board, preview, score, survival and live-time genes.
- Reject Tetris's rigid `SYS-007` and immediate completed-row `SYS-008`; changing their parameters would hide a different settlement and clear rule.
- Reject a separate gene for the `Shinin'` track, orange/ivory art or reported exact sweep seconds. These are edition/skin parameters. Do not import Time Attack's deadline into Single Skin.
- Duplicate queue `301` routes `SYS-1157/SYS-1158` because both first occur in this game. Keep them distinct on a two-way boundary transfer test: an ordinary square waits for and clears on the line without any marked cell, so it needs `SYS-1157` without `SYS-1158`; a marked cell extends only a square already eligible for that line, and cannot replace the general delayed sweep. Merging them would incorrectly extend every ordinary square to connected cells.
- No reviewed earlier game was found that warrants an existing-gene rewrite for these four boundaries.

## Evidence and limits

The [series owner's history](https://lumines.game/history/) identifies the original PSP release and its later editions. [Tightning's contemporary original-game guide](https://gamefaqs.gamespot.com/psp/924594-lumines/faqs/35465) and [sp0rtsfan's separate original-game guide](https://gamefaqs.gamespot.com/psp/924594-lumines/faqs/36468) describe the mode, square, line, special cell and top-out. The published [*Lumines Strategies* analysis](https://www.researchgate.net/publication/225333916_LUMINESStrategies) supports the independent two-column landing and visible grid/preview. No original UMD or direct play was available, so precise scoring, probability and frame scheduling remain open.

## Decision

Accept four boundaries with reviewed Ukrainian, original mechanics-valid art and complete repository/browser gates. This unit authorises exactly one local commit, not push, public publication or deployment.

## Advisory health review

`BASELINE_442` measures 2,297 Active singleton genes among 3,101 Active
genes (`0.740729`), above the `0.70` review threshold. The latest-nine
new-gene mean is `4.888889`, below its `12.0` threshold. Maintainer
disposition for this unit: retain the independently evidenced delayed-clear
boundaries and schedule vocabulary-transfer review at the batch audit; do not
force a merger with Tetris's immediate row clear or freeze expansion. The
duplicate and lexical queues remain suggestions, not taxonomy decisions.
