# Taxonomy Change 158: Timed driving-style stash separate from race place

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-27
- Trigger: `GAME-0420` *Project Gotham Racing 2*, original Xbox offline Compact Sports first Street Race.
- Scope: admit `SYS-1114` and `INF-413` as Active. Reuse the existing finite-race, vehicle-control and real-time genes without changing earlier signatures or verified combinations.

## Problem and accepted change

A place-based race result cannot describe the separate temporary Stash, roughly two-second bank transfer and extra bonus for a second eligible style manoeuvre before that transfer. The original manual explicitly shows Stash, Bank, Combo Bonus and current position as different live fields. `SYS-1114` models the score transition; `INF-413` models the decision-relevant visible separation. The two-lap first-place objective remains distinct from optional Style Kudos.

## Transfer and rejection tests

- Reuse dedicated vehicle control, rival field, ordered race completion, event reward and position/HUD genes for their existing causal boundaries.
- Do not transfer `SYS-1103`: *Crazy Taxi* builds collision-breakable passenger tips that pay at fare completion, not a freely banked World Series style score.
- Do not infer an exact score coefficient, universal collision reset, online result or Time Attack style award. Novice car/rival parameters do not create genes.

## Evidence and limits

The [original Microsoft/Bizarre instruction manual](https://manualzz.com/doc/25186554/microsoft-project-gotham-racing-2-video-game-user-manual), printed pp. 4, 6 and 10–12, gives the Stash/Bank timing, style moves, separated display and World Series result rules. The [licensed Prima Official Strategy Guide](https://ogxbox.co.uk/media/com_eshop/attachments/Project_Gotham_Racing_2_Strategy_Guide_Book.pdf), printed pp. 6–10, identifies the first Compact Sports Street Race and corroborates combo timing. No original disc or direct play was inspected.

## Decision

Accept two typed style-score boundaries, retain earlier genomes and verified combinations, and require deterministic comparison, Ukrainian review, original artwork and all repository/browser gates before the authorised local commit.
