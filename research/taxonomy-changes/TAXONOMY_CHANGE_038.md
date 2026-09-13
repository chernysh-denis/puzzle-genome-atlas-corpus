# Taxonomy Change 038: Separate the first service loop and retire its false carry terminal

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-08
- Trigger: independent closure review of `GAME-0278` DAVE THE DIVER.

## Current classification

- The Batch 016 candidate represented the whole restaurant half with
  `SYS-823`, treated the displayed normal carry threshold as hard excursion
  termination in `CON-618`, and kept menu selection, drink pouring, requested
  delivery, time-driven demand, individual wait expiry and result grading out of
  the signature.
- It also called the stock-producing excursion the first dive and asserted that
  no current semantic version was available.
- Existing lower-ID boundaries remained artificially narrow in four places:
  `ACT-091` named inventory gifts only; `SYS-030` named network demand only;
  `SYS-822` named a won encounter only; and `INF-117` named purchases despite
  the reviewed DREDGE carrier already using it for a sale.

## Detected problem

- Two complete independent prologue guides agree that the stock-producing route
  is a required **second** dive after the first knife/harpoon tutorial and the
  earthquake, and that it requires seven fish before the first menu and service.
- Those guides separately establish recipe-to-serving availability, explicit
  menu allocation, a release-timed drink pour, prepared-dish delivery to the
  matching requester, time-driven customer orders, individual wait expiry,
  closing sales categories and an aggregate grade.
- A complete guide and independent player evidence agree that crossing the
  displayed normal carry threshold first slows movement. It does not force the
  dive to end. A later upper pickup cutoff exists, but the corrected route stops
  at seven small starting-area fish and neither reaches nor tests it.
- The publisher's 2026-08-10 hotfix explicitly labels the current Windows build
  `v1.0.6.2087`; the candidate's semantic-version gap was therefore false.

## Evidence

- Primary product and version evidence: Valve application data and
  MINTROCKET's official Steam announcement surface, which names Windows version
  `v1.0.6.2087` in the `8/10 Hotfix`.
- Distribution observation: public branch build `24651119` in the SteamCMD info
  projection, dated to the same 2026-08-10 update.
- Complete route evidence: the independently published Rectify Gaming and Sirus
  Gaming prologue walkthroughs cited by the game record. Both distinguish the
  opening tutorial dive from the required seven-fish second dive and describe
  the first menu, drink, delivery, customer and report transitions.
- Carry-boundary counterevidence: Sirus Gaming states that approaching or
  exceeding the normal threshold slows the swimmer; the Steam Community source
  corroborates a later separate upper pickup cutoff. Neither supports the
  candidate's claimed forced-surface transition.

## Proposed change

- Generalise `ACT-091` from an inventory gift to delivery of one currently
  carried item to its addressed requester. A prepared dish and a persistent
  inventory object are carried representations; recipient matching and
  committed transfer remain the boundary.
- Generalise `SYS-030` from network-only demand to system-created visible demand
  awaiting compatible fulfilment on an operating service surface. Arrival stays
  time-driven and player placement remains excluded.
- Generalise `SYS-822` from a won encounter to a completed bounded activity that
  records an aggregate performance grade. Activity type and category vocabulary
  are parameters.
- Make the reviewed sell-side use already carried by DREDGE explicit in
  `INF-117`, and admit visible buy, sell or service-menu offers before a
  transaction or allocation decision.
- Add DAVE THE DIVER as further support to `INF-299`; a service report is another
  bounded results report with categories and aggregate evaluation, without
  changing that information boundary.
- Correct `SYS-823` to own only the cross-activity stock-to-menu-to-revenue
  conversion. It no longer claims that stock directly controls which orders may
  appear.
- Deprecate `CON-618`. Its only asserted current carrier was false, no reviewed
  scoped game carries it, and no stable ID is retyped or reused.
- Add portable new records `ACT-447`, `ACT-448`, `CON-620` and `INF-330` for the
  menu allocation, release-timed fill, individual request expiry and live
  service disclosure that the candidate omitted.

## Genome and combination impact

- Definitions rise from 2,404 to 2,408. Active genes rise from 2,356 to 2,359:
  four new Active definitions are added and `CON-618` moves from Active to
  Deprecated. Merged definitions remain 46; Deprecated definitions rise from
  two to three.
- `GAME-0278` changes while still draft from eleven to eighteen Active genes. It
  retains eight candidate genes, removes `ACT-341`, `CON-618` and `TIM-013`, and
  admits six lower-ID reuses plus four new definitions.
- Admitted gene usages rise from 5,935 to 5,942. No earlier reviewed game
  signature, lifecycle, game date or selected neighbour changes.
- `COMB-0270` records `SYS-822 + INF-299` as a strict subset of both Cuphead and
  DAVE THE DIVER: the system computes an aggregate grade and the terminal report
  exposes the contributing categories plus that aggregate. Cuphead's
  `combination_ids` gains the newly evidenced relation; its genome is unchanged.
- Combinations rise from 269 to 270. All prior combinations are rescanned.

## Decision

- Decision: `Accepted`.
- Decided by: source re-read, transition-by-transition decomposition, complete
  lower-ID scan, two-way transfer tests and independent carrier comparison.
- Rationale: the candidate confused a slowdown threshold with a terminal and
  hid several player decisions inside a product-shaped system summary. The
  reviewed form separates action, system, constraint and information roles,
  reuses lower-ID boundaries where their causal function transfers, and keeps
  fish, dishes, characters, counts and calendar labels as parameters.
- Implementation links: `ACT-091`, `ACT-447`, `ACT-448`, `SYS-030`, `SYS-822`,
  `SYS-823`, `CON-618`, `CON-620`, `INF-117`, `INF-299`, `INF-330`, `OBJ-167`,
  `COMB-0270`, `GAME-0277` and `GAME-0278`.

## Ukrainian review

- Every generalised, corrected and new Active record receives complete
  Ukrainian label, definition, inclusion and exclusion parity in this unit;
  the deprecated record is removed from the current-language registry.
- Product, mission, interface, drink, character, date, version and build names
  remain game-scoped official labels or parameters rather than gene names.

## Change history

- 2026-09-08 — created and accepted during the independent `GAME-0278` closure
  unit, before the draft was promoted to reviewed.
