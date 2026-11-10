# Taxonomy Change 257 Cyberpunk quickhack resource cost

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-10-14
- Scope: existing `SYS-374` in `GAME-0146`; no gene, carrier or lifecycle change.

## Decision

`SYS-374` describes a quickhack's effective RAM cost, timed upload, optionally
unlocked queue, target effect and eligible hostile trace. The former English
definition called RAM *reserved*, while the carrier and Ukrainian presentation
called it *spent*. The corrected English and Ukrainian definitions describe
the normal RAM cost and the unlocked Overclock exception: when RAM is
insufficient, Health can be consumed to allow the upload. Neither definition
assigns the resource debit to a specific frame of the upload or claims a
refund after interruption.

The [official Update 2.0 notes](https://www.cyberpunk.net/en/news/49060/update-2-0)
document the cost, upload-time changes, acquired queue capability and
Overclock's Health exception. The [official Patch 2.02 notes](https://www.cyberpunk.net/en/news/49378/patch-2-02)
distinguish modified quickhack RAM cost from RAM actually spent when correcting
Data Recycler recovery. The [Cyberpunk 2077 decomposition](../../knowledge/games/a-f/cyberpunk-2077.md)
now makes the resource and queue conditions explicit in `CP-004`. The pilot
explanation of adjacent `CON-334` also reflects its already-canonical
Health-for-RAM exception rather than claiming that insufficient RAM always
blocks upload.

`GAME-0146` remains the sole carrier and `COMB-0144` retains the gene. Their
memberships, all signatures and pair scores are unchanged. Exact before/after
fields and the verification record are in the
[canonical audit](../normalisation/P2_CANONICAL_SOURCE_REVIEW_009.json).
