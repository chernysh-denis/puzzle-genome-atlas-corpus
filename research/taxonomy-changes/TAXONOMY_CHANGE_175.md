# Taxonomy Change 175: Landing colour, Coily transformation and disc escape in Q*bert

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-28
- Trigger: `GAME-0438` *Q*bert*, original Gottlieb arcade Level I Round 1.
- Scope: admit `SYS-1148`–`SYS-1151` as Active. No earlier signature or verified combination changes.

## Problem and accepted change

The player must visit every persistent cube top, and landing advances the addressed top toward a target colour. Unpredictably arriving balls are not all equivalent: the purple class hatches into Coily, whose live pursuit follows the avatar rather than the ball's prior descent. A side-disc jump returns Q*bert to the summit and can make the pursuing Coily leave the pyramid. These are distinct board-state, actor-role, movement-target and escape boundaries rather than four genre names for an arcade platformer.

## Transfer and rejection tests

- Reuse `ACT-008` for direct diagonal hops, `CON-001` for fixed addressable cube positions, `OBJ-004` for the all-tops target state, `INF-001` for the visible current board, `SYS-004` and `SYS-030` for unpredictable arrivals, `SYS-045` for automatic actor motion, `CON-183` for finite lives and `TIM-003` for the live clock.
- `SYS-057` requires a perception-triggered alert, which the original manual does not establish for Coily. `SYS-960` specifies multiple timed PAC-MAN ghost targeting modes, and `SYS-131` specifies a one-step response after a player turn; neither is the evidenced live Coily behaviour.
- Cube count, colours, ball timings, disc placements and score awards remain parameters. Later rounds add reversal, green freeze and sideways climbers and are outside this packet.

## Evidence and limits

[Gottlieb's original `GV-103A` instruction manual](https://arcarc.xmission.com/PDF_Arcade_Manuals_and_Schematics/Q-Bert_Instruction_Manual_%2811-82%29.pdf), section IV, directly describes target-colour landings, first-two-round ball classes, purple-ball hatch, Coily's pursuit and the disc lure; [a searchable OCR transcription](https://manualzz.com/doc/8559673/gottlieb-q-bert-arcade-game-instruction-manual) was used to inspect the scan. The scan's character-name glyphs are not reliable OCR, but the rule passages are coherent. No original cabinet, executable, direct play or frame trace was inspected. Exact arrival probabilities, movement rates and Coily path tie-breaks are not asserted.

## Decision

Accept four distinct typed boundaries with reviewed Ukrainian copy, original mechanically valid artwork and complete repository/browser gates. One local game-unit commit is authorised; no push, public publication or deployment.
