# Taxonomy Change 124: addressable courtroom testimony and finite objections

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-09-24
- Trigger: `GAME-0385` Phoenix Wright: Ace Attorney, original English
  Nintendo DS first case The First Turnabout.
- Scope: seven additive Active genes; no previous genome, lifecycle, family
  definition or verified combination changes.

## Problem and accepted change

Existing evidence genes describe fixed memory tableaux, archive search,
document discrepancy highlighting and structured answer fields. They do not
model an authored witness statement as a revisitable *address* for a press or
evidence challenge, followed by a revised account and a finite objection
budget. The first case supplies a particularly clear boundary: its culprit is
shown, no scene investigation precedes trial, and the player must prove the
account inconsistent rather than guess an unknown killer.

- `ACT-526` isolates pressing the currently selected testimony line for
  elaboration without committing a contradiction.
- `ACT-527` isolates presenting one current record item *against that exact
  line*, not comparing two highlighted fields or choosing a final verdict.
- `SYS-1041` advances the authored testimony, follow-up and case record only
  when a supported pair or response is accepted.
- `CON-690` bounds unsupported court challenges with a finite visible mark
  allowance and guilty terminal on exhaustion.
- `INF-391` makes the changing case-local evidence/profile record inspectable;
  `INF-392` makes the current testimony version's lines individually
  addressable and revisitable.
- `OBJ-227` defines the local first-case acquittal achieved through the
  accepted contradiction sequence.

## Transfer and rejection test

`ACT-232` handles consequential offered court responses and `TIM-002` the
self-paced decision cadence. `ACT-104` needs two player-highlighted facts
inside an inspection interface; the Ace Attorney player instead addresses a
witness sentence and presents a case item. `ACT-105` stamps a whole-case
binary verdict, but the judge—not the player—delivers this case's verdict.
`INF-012`'s fixed scene-indexed evidence is not the mutable Court Record.
`SYS-1034`'s single marked puzzle answer does not represent successive
testimony revisions. No earlier game signature or verified combination is
changed by these distinctions.

## Evidence and limits

- [Nintendo's original DS publisher description](https://www.nintendo.com/en-gb/Games/Nintendo-DS/Phoenix-Wright-Ace-Attorney-272222.html)
  establishes the five-case Court/Investigation structure and testimony/
  evidence premise.
- [Capcom's creator interview](https://news.capcomusa.com/lets/browse/the-early-days-of-ace-attorney)
  confirms why a short contradiction-focused first case was written and why
  the culprit is deliberately disclosed.
- [GameSpot's 2005 DS review](https://www.gamespot.com/reviews/phoenix-wright-ace-attorney-review/1900-6135422/)
  independently describes line navigation, press/present, supplied evidence,
  five marks and guilty failure.
- [The original-DS first-case route](https://gamefaqs.gamespot.com/ds/925589-phoenix-wright-ace-attorney/faqs/47084)
  provides the reproducible sequence from autopsy and blackout challenges to
  the passport explanation and acquittal.
- No cartridge or audiovisual direct-play trace was inspected. Optional
  answer branches and region-specific bytes remain outside the claim.
