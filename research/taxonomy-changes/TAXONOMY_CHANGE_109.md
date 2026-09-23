# Taxonomy Change 109: Staffed hospital rooms and diagnostic service flow

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-23
- Trigger: `GAME-0370` Theme Hospital, original English PC First Game level.
- Scope: eight additive Active genes; no existing lifecycle or prior game
  signature changes.

## Problem

Existing venue, finance, autonomous-worker and personal-need genes capture
shared management mechanics. A theme-park visitor's service choice cannot
stand in for a medically referred patient, however: the patient needs staffed
reception, staged diagnosis and a condition-compatible treatment. Neither a
fixed building placement nor a park attraction's station rules express the
multi-stage room blueprint with required furniture and a qualified worker.
Likewise Park Rating is not the hospital's documented care-outcome-and-price
reputation feedback, and the first level's five simultaneous quarterly bars
are not a single attendance/rating deadline.

## Accepted change

- `ACT-504` commissions a room through legal footprint, door and furniture.
- `ACT-505` changes patient queue and partial-diagnosis policy.
- `SYS-1005` routes reception and staged diagnosis.
- `SYS-1006` settles compatible staffed treatment.
- `SYS-1007` feeds care outcome and price into hospital reputation.
- `CON-672` gates service on both the prepared room and eligible staff.
- `INF-377` exposes referral, queue and five-bar status needed for intervention.
- `OBJ-213` checks all briefing targets at a quarter while avoiding loss bars.

## Lower-ID transfer test

- `ACT-006`, `ACT-139`, `ACT-487`, `ACT-488`, `SYS-045`, `SYS-154`,
  `SYS-198`, `CON-171`, `INF-058`, `INF-072` and `TIM-003` transfer at their
  documented generic management, worker, finance and personal-state bounds.
  Opening the hospital does not imply an entrance price.
- `SYS-951` chooses a visitor destination by preference and value; it does
  not reproduce a GP's diagnosis-driven referral.
- `SYS-227` is staffed, time-accumulating medical-bed recovery under heat and
  capacity rules; it does not encode the room-specific immediate cure path.
- `SYS-952` is Park Rating from rides, layout and guest experience, not this
  hospital's care-result and price reputation update.
- `CON-655` requires a ride station, queue and exit; it cannot gate a
  furnished Pharmacy on a nurse or Psychiatry on a qualified doctor.
- No previous game genome is edited and a single new carrier does not verify
  a recurring combination.

## Evidence and limits

The original Bullfrog/Electronic Arts PC manual directly documents the
first-level tutorial, room blueprints, required furnishings, staff roles,
reception and diagnostic referral, queues, treatment rooms, hospital status,
reputation inputs and quarterly win/loss checks. The GOG listing establishes
distribution identity only. No executable, direct play, exact first-level
threshold numbers or hidden formula was inspected.
