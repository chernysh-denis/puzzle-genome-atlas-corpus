# Taxonomy Change 152: Kinect Adventures! tracked-body leak coverage

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-09-26
- Trigger: `GAME-0414` *Kinect Adventures!*, one original Xbox 360 solo ordinary 20,000 Leaks activity.
- Scope: admit `ACT-553`, `SYS-1101`, `CON-699` and `INF-407` as Active. No earlier game signature or verified combination changes.

## Problem and accepted change

The original Microsoft manual presents a distinct player decision: put one or more tracked body parts at visible leak positions, keep every hole connected by a crack covered, then let the crack seal and earn points. A contemporary played review corroborates that later arrangements require simultaneous multi-limb poses. A conventional click, routed avatar walk, bowling release or DDR foot-panel step cannot express the live contact geometry. We separate the placement action, simultaneous-validity constraint, resulting seal-and-score system transition and time/score/leak feedback rather than one generic "Kinect" device gene.

## Transfer and rejection tests

- `ACT-553` requires a directly tracked, continuously placed physical body region matched to a current world target. It excludes a one-shot button press, virtual net sweep (`ACT-477`), bowling gesture sampled only at release (`ACT-499`) and decorative motion capture.
- `CON-699` evaluates one connected leak group: every member needs a concurrent eligible contact. Distinct unrelated cracks are not automatically one combined gate, and the exact simultaneous-frame tolerance is a parameter.
- `SYS-1101` closes the group and credits points only after the `CON-699` predicate holds. It is not the contact predicate itself; leaving one target uncovered prevents this transition.
- `INF-407` discloses active leak targets and current feedback, not future fish strikes or a fully specified schedule. The official manual's page image shows a timer and score but not universal threshold values.
- `OBJ-002` covers maximising the bounded activity score, and `TIM-003` covers real-time contact and new damage. No new objective or time gene is created merely because a visible clock and medal exist.
- Reject `SYS-004`: the manual says fish make holes but does not specify a random distribution. Reject importing Timed Adventure or Time Challenge extra-time rules into this ordinary activity. Reject `ACT-008`: there is no free navigation route in the selected loop.

## Evidence and limits

- [Microsoft's original English instruction manual](https://download.microsoft.com/download/F/9/9/F99AB8F0-5191-4EDD-B312-7A9B9E4784FA/KinectAdventures_MNL_EN-US.pdf), printed pp. 18–23, confirms the holes, eligible body parts, connected cracks, points, clock/score image, medal evaluation and distinct timed variants. Its PDF SHA-256 is recorded in the [game record](../../knowledge/games/g-l/kinect-adventures.md).
- [Microsoft's 2010 announcement](https://news.microsoft.com/source/2010/07/20/new-xbox-360-kinect-sensor-and-kinect-adventures-get-all-your-controller-free-entertainment-in-one-complete-package/) and the [ESRB description](https://www.esrb.org/ratings/29471/kinect-adventures/) anchor original Xbox 360 body-input identity.
- [Kotaku's 2010 played review](https://kotaku.com/review-kinect-adventures-5679412) corroborates simultaneous multi-leak poses. It is not a source for numerical sensor or score parameters.
- No Xbox 360 disc, Kinect play session, input trace, video or audio was inspected. Exact level, damage pattern, collision tolerance, round duration and score thresholds remain unverified.

## Decision

Accept four new typed boundaries solely for `GAME-0414`. Keep all earlier signatures unchanged. Recompute lower-ID nearest genomes and verified-combination subsets, review the bilingual definitions and validate the original-art depiction of a feasible simultaneous two-hand/one-foot seal before the local unit commit.
