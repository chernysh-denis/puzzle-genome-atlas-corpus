# Taxonomy Change 171: Assessed touch-recipe steps in Cooking Mama

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-09-27
- Trigger: `GAME-0434` *Cooking Mama*, original English Nintendo DS ordinary miso-soup recipe.
- Scope: admit `ACT-572`, `SYS-1138`, `CON-710` and `OBJ-249` as Active. No earlier signature, definition or verified combination changes.

## Problem and accepted change

A stylus task acts on one visible ingredient or cooking control. The recipe then moves to another separately assessed task; at least the stock stage accepts commands in its displayed order and timing window. A final dish-quality medal follows the complete ordinary recipe, not one step or the wider game. Those action, progression, local constraint and objective boundaries are distinct from a generic craft command.

## Transfer and rejection tests

- Reuse `SYS-822` for quality-based activity grading, `INF-268` for the current instruction and `TIM-003` for live cue input.
- Reject `ACT-410`: it operates an embodied retained alchemy batch at one workstation, not discrete DS touch minigames.
- Reject `CON-068`: its expiry ends the entire attempt; a mistimed stock cue can reduce step quality without a sourced whole-recipe terminal clock.
- Reject `SYS-756`: that evaluates retained physical alchemy history, not the sequence of separately presented touch tasks.
- The optional soup branch, unjudged practice, microphone cooling in other dishes and exact medal formula are out of scope.

## Evidence and limits

[Nintendo's publisher-provided original DS description](https://www.nintendo.com/en-gb/Games/Nintendo-DS/Cooking-Mama-270330.html) establishes stylus minigames, Mama's instructions, medals and unjudged Practice. [Daniel Engel's first-hand original-DS route](https://gamefaqs.gamespot.com/ds/931435-cooking-mama/faqs/44983) and [Sean Velasco's contemporary US recipe list](https://gamefaqs.gamespot.com/ds/931435-cooking-mama/faqs/44870) independently identify the five-step miso-soup path. [ClearQuartz's firsthand mechanics guide](https://gamefaqs.gamespot.com/ds/931435-cooking-mama/faqs/45397) explains step-local timing and grade differences. Those guides were accessed through indexed excerpts because direct page loading was restricted. No cartridge, direct play, measured gesture tolerance or regional parity test was available.

## Decision

Accept four boundaries, reviewed Ukrainian copy, the complete lower-ID comparison, original mechanics-first artwork and repository/browser gates. This unit authorises one local commit only; no push, public corpus publication or deployment.
