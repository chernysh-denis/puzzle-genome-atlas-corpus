# Taxonomy Change 256 Park and attraction information panels

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-10-14
- Scope: existing `INF-362` in `GAME-0335`; no carrier or lifecycle change.

## Decision

`INF-362` covers current park and attraction information exposed across
separate management views, not one universal ride panel. In Forest Frontiers,
the Park Status window shows the objective and aggregate attendance/rating;
Rides Info shows attraction status and guest-response measures; relevant tabs
of a selected Ride window show queue, admission price and inspection policy.
Ride-test measurements become available only after a completed test run.
The current date and visible breakdown state help relate those observations
to the scenario deadline and operation.

The earlier English definition listed popularity, satisfaction, test data and
downtime, while the Ukrainian definition and game record instead listed
price, reliability, inspection and breakdown. The official manual supports
the named views and their distinct information. It does not establish a
numeric reliability or downtime field in this bounded packet, so neither is
asserted as a required display. The former pilot example about checking
reliability *before* a breakdown implied knowledge of a hidden future event;
the corrected example checks current status and inspection settings after an
observed breakdown.

## Evidence and boundaries

The official [Steam-hosted RollerCoaster Tycoon Deluxe manual](https://cdn.akamai.steamstatic.com/steam/apps/285310/manuals/rollercoaster_tycoon.pdf)
describes Rides Info status, popularity and satisfaction on printed pages
33–35; Park Status objective, attendance and rating on pages 78–79; and Ride
window controls, queue inspection, price, inspection schedule and completed
test measurements on pages 80–83. The manual distinguishes the tabs present
for different kinds of rides. The [game decomposition](../../knowledge/games/m-r/rollercoaster-tycoon-deluxe.md)
limits the carrier to the original Forest Frontiers scenario in the Deluxe
package. No direct play or installed-build parity is claimed.

`INF-072` remains the personal panel of one guest. `INF-058` remains the
itemised finance ledger. Neither replaces the park and ride operating
overview. A completed test's current measurements are information; an exact
future breakdown or scenario result remains excluded.

The sole game signature, all 274 combination sets and all pair scores stay
unchanged. The registry remains at 3769 definitions, including 3711 Active.
The four English and four Ukrainian registry fields were reviewed; the label
was retained and the other three fields corrected in each language. Four
pilot explanation/example fields were corrected while both labels were
retained. The original Ukrainian integration batch remains traceable. Exact
before/after fields and verification are in the
[canonical audit](../normalisation/P2_CANONICAL_SOURCE_REVIEW_008.json).
