# Taxonomy Change 055: Remove carrier nouns from strategic-management genes

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-10
- Trigger: `GAME-0287` — Stellaris.
- Scope: wording generalisation only; no lifecycle, existing signature,
  combination or family assignment changes.

## Problem

Five lower-ID Active genes already described the transferable mechanisms needed
by the bounded Stellaris packet, but their labels or definitions retained nouns
from the first carrier: a queued technology, a municipal budget, national
research slots, city production and an RTS view. Later reviewed carriers already
stretched some of those labels. Creating Stellaris-specific duplicates would
encode genre or map scale rather than a new rule.

## Decision

- `ACT-121` becomes **Select an active technology research target**. A queued
  target and one target assigned to each independent channel are parameters of
  the same player commitment.
- `SYS-154` becomes **Settle a recurring managed-domain budget**. City and
  interstellar polity are carriers; periodic income, upkeep and stock updates
  are the mechanism.
- `SYS-564` becomes **Advance parallel strategic research channels**. Nation
  and empire are carriers, while independent time-driven research channels are
  invariant.
- `CON-417` keeps its label but replaces `city` with `owned production site` in
  the predicate. Facilities, resources, capacity and cost remain its boundary.
- `INF-224` becomes **Strategic command view exposes economy, selection and
  production state**. RTS and grand-strategy scale are presentation parameters.

The matching Ukrainian labels and definitions receive the same portable
boundaries in `UK-GAME-0287-0287`. Existing evidence and carriers are retained,
and Stellaris is added as support.

## Checks against lower-ID meaning

- `ACT-121` remains the choice of what technology receives progress. It does
  not absorb production of research inputs (`SYS-159`), independently advancing
  channels (`SYS-564`) or automatic invention.
- `SYS-154` remains periodic accounting. It does not absorb one-time purchases,
  production or a terminal score.
- `SYS-564` remains simultaneous independent research progress. It does not
  absorb building-local queues (`SYS-552`) or staffed research sites
  (`SYS-194`).
- `CON-417` remains production eligibility and affordability. It does not absorb
  territorial or colonisation predicates introduced as `CON-626` and
  `CON-627`.
- `INF-224` remains a live owner-command surface. It does not absorb the
  star-system knowledge boundary in `INF-081`.

## Migration result

- Existing game signatures changed: `0`.
- Existing combination gene sets changed: `0`.
- Lifecycles changed: `0`.
- New aliases or merged IDs: `0`.
- Definition records generalised: `5`.
- New supporting carrier: `GAME-0287`.

## Rejection condition

Reopen this decision only if a later carrier demonstrates that any generalised
record combines separable player commitments, clocks, legality predicates or
information surfaces. A different genre label, territorial scale, UI skin or
number of channels is not sufficient.
