# Taxonomy Change 176: Balance-board steering and soft gate penalties in Wii Fit

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-09-28
- Trigger: `GAME-0439` *Wii Fit*, original North American Wii Beginner Ski Slalom.
- Scope: admit `ACT-575`, `SYS-1152`, `SYS-1153`, `INF-424` and `OBJ-251` as Active. No earlier signature or verified combination changes.

## Problem and accepted change

The bounded activity does not steer a vehicle by buttons or tilt an abstract stage. The standing player continuously shifts weight across a pressure-sensing board; the system maps lateral displacement into the Mii's line and fore/aft displacement into speed during an automatic descent. The interface shows the current balance position and each gate result. A gate miss does not invalidate progress: it adds seven seconds to final effective time. The course therefore has a different success and scoring boundary from mandatory-checkpoint racing. These are distinct action, response, scoring, information and objective boundaries, not separate genes for the board's brand, the number of gates or a star grade.

## Transfer and rejection tests

- Reuse `SYS-045` for autonomous downhill continuation and `TIM-003` for live input while the clock advances.
- Reject `ACT-519`/`SYS-1028`: a stick tilts an entire virtual stage to roll a ball, rather than a user's measured balance moving the avatar's own path and pace.
- Reject `SYS-516`/`CON-438`: their missed required race checkpoint invalidates ordered race progress, whereas a missed Wii Fit gate permits a scored finish.
- Reject `CON-068`: this elapsed performance clock is not a failed-attempt deadline. The bounded activity has no independently evidenced limiting constraint gene.
- Reject `OBJ-133`: this is not a car that must pass every waypoint and retain a medal. One valid completed slope can have missed gates, and its evaluated result is lower adjusted time.
- Board calibration, 19-gate layout, seven-second price, displayed colours and exact numerical sensor response remain parameters or unknowns.

## Evidence and limits

[Nintendo's original Wii Fit booklet](https://csassets.nintendo.com/noaext/image/private/t_KA_PDF/Wii_Wii_Fit?_a=DATAg1AAZAA0), pp. 4–6 and 15–16, documents Balance Board recognition, the training categories, activity entry, final score and Retry/Quit. [Sky1993's first-hand original-game guide](https://gamefaqs.gamespot.com/wii/942009-wii-fit/faqs/53123) describes the Beginner slalom's balance-dot cue, weight steering and seven-second misses. [Jelsma et al.'s direct experimental observations](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0140470) independently report two-axis steering, fixed 19-gate easy course, immediate gate feedback and the effective-time equation. [Nintendo's developer interview](https://www.nintendo.com/en-gb/Iwata-Asks/Iwata-Asks-Wii-Fit/Volume-4-Sound-Design-and-Planning/4-Almost-like-Spinning-a-Real-Hoop/4-Almost-like-Spinning-a-Real-Hoop-204199.html) corroborates authored and repeatedly tested flag placement. No Wii disc, console or sensor was run by this repository; precise calibration and coefficient values are not asserted.

## Decision

Accept five typed boundaries with reviewed Ukrainian copy, a physically plausible original illustration and complete repository/browser gates. The game unit allows one local commit; it does not authorise push, public corpus publication or deployment.

## Advisory health review

`BASELINE_439.json` reports 2,285 single-carrier active genes of 3,085 (74.0681%), above the advisory 70% review threshold. This is a cumulative corpus concern, not evidence that any of these five game-specific boundaries is duplicate: the transfer tests above reject the closest existing genes for documented mechanical reasons. The latest nine games add 43 new genes, 4.777778 per game, below the separate 12-gene threshold. Retain the accepted boundaries and carry the singleton-share signal into the next maintainer taxonomy review; do not mutate the vocabulary merely to clear a metric.
