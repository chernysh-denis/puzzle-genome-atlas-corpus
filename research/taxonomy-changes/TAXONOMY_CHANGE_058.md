# Taxonomy Change 058: Split driving-reserve accumulation from acceleration settlement

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-10
- Trigger: card `C-02` of
  [`BATCH_017_FULL_TAXONOMY_AUDIT_001`](../normalisation/BATCH_017_FULL_TAXONOMY_AUDIT_001.md).
- Scope: compound `SYS-641`, existing boundaries `SYS-765` and `SYS-691`,
  `GAME-0199` and `COMB-0197`; the five existing carriers keep their
  signatures.

## Current classification

- `SYS-641` joins two independently observable System transitions in one
  record: eligible live driving events add to the Need for Speed Unbound Burst
  Nitrous reserve, and a later activation consumes that reserve into bounded
  vehicle acceleration.
- `SYS-765` already owns only the first transition for Asphalt Legends:
  eligible drift and airborne manoeuvres add charge to its bounded nitro
  reserve.
- `SYS-691` already owns only the second transition for Need for Speed Payback,
  Need for Speed: Most Wanted (2005), Need for Speed: The Run and Asphalt
  Legends: activation debits available charge and applies bounded vehicle
  acceleration.
- The standing `Excludes` in `SYS-765` and `SYS-691` distinguish Unbound's
  branded, separately capped Burst from ordinary nitro. They encode reserve
  identity and persistence as if either changed the underlying transition.

## Evidence and boundary test

- The official [Need for Speed Unbound feature
  page](https://www.ea.com/games/need-for-speed/need-for-speed-unbound/features),
  accessed 2026-09-10, identifies Burst Nitrous as a distinct tactical speed
  boost inside the driving loop.
- EA's official [Under the Hood: Run These
  Streets](https://forums.ea.com/discussions/need-for-speed-unbound-discussion-en/need-for-speed%E2%84%A2-unbound-under-the-hood---run-these-streets/9398552),
  accessed 2026-09-10, separately establishes that grip or drift cornering and
  drafting build the Burst bar, and that activation supplies the tactical
  boost. The forum returned rate limiting on direct repeat access during this
  unit; its indexed official text and the retained `P5` claim ledger were
  therefore cross-checked rather than silently replaced by a third-party rule.
- EA's official [release
  announcement](https://news.ea.com/press-releases/press-releases-details/2022/The-Next-Generation-Street-Racing-Fantasy-Starts-Today-in-Need-for-Speed-Unbound/default.aspx),
  accessed 2026-09-10, independently describes Burst Nitrous as a style-based
  boost reflecting how the player drives.
- Gameloft's official [Asphalt Legends gameplay
  help](https://gameloft.helpshift.com/hc/en/15-asphalt-legends/section/193-gameplay-1607072985/),
  [trick rule](https://gameloft.helpshift.com/hc/en/15-asphalt-legends/faq/605-what-are-barrel-rolls-and-360s/),
  [Nitro Shockwave
  rule](https://gameloft.helpshift.com/hc/en/15-asphalt-legends/faq/606-how-do-i-perform-a-nitro-shockwave/)
  and [Perfect Nitro
  rule](https://gameloft.helpshift.com/hc/en/15-asphalt-legends/faq/639-how-do-i-perform-a-perfect-nitro/),
  accessed 2026-09-10, separately establish manoeuvre-earned charge and
  player-triggered conversion of available charge into a speed effect.
- The retained primary ledgers of the four existing `SYS-691` carriers were
  reopened. Each exposes the same resolution boundary with different vehicle,
  reserve, duration, depletion and fitted-performance parameters; none makes
  the acquisition rule part of `SYS-691`.

The two-way transfer test passes for both extracted halves:

1. Asphalt and Unbound both detect eligible live driving manoeuvres and add
   their resolved contribution to a bounded acceleration reserve. Drift,
   airborne stunt, grip cornering and drafting are eligible-event parameters.
2. Every `SYS-691` carrier and Unbound debit a currently available bounded
   driving reserve after activation and apply vehicle acceleration until a
   carrier-specific release, depletion or effect cutoff.
3. Calling a reserve ordinary nitro or Burst Nitrous, assigning a separate cap,
   and choosing when it resets alter identity and persistence parameters. They
   do not create another accumulation or settlement transition. This follows
   the parameter precedent recorded in `TAXONOMY_CHANGE_013`.
4. The player command remains `ACT-309`. Neither System gene owns button
   choice, the acquisition rule of the other half, an Information display or
   an Objective terminal.

## Decision

- Change `SYS-641` to `Split`. Preserve it as a historical alias and prohibit
  it in current signatures.
- Generalise `SYS-765` to **Convert eligible driving manoeuvres into
  acceleration-reserve charge**. It owns accumulation only and now admits both
  Asphalt Legends ordinary nitro and Need for Speed Unbound Burst Nitrous.
- Generalise `SYS-691` to **Convert a bounded driving reserve into vehicle
  acceleration**. It owns settlement only and now admits Unbound alongside its
  four existing carriers.
- Replace `SYS-641` with both `SYS-765` and `SYS-691` in `GAME-0199` and
  `COMB-0197`.
- Keep `SYS-540` unchanged. Its coupled spatial-pad pickup, pad recharge and
  directed-thrust loop was not part of confirmed card `C-02`; a future change
  would need its own all-carrier compound review.

## Genome and combination impact

- `GAME-0199` grows from 24 to 25 Active genes because one compound record is
  replaced by two independent live records. It now has four game-introduced
  Active genes and 21 reused genes.
- `COMB-0197` grows from 18 to 19 genes and remains a strict subset of the
  supporting genome. Its causal structure is unchanged; the former compound
  Burst step is simply represented by its accumulation and settlement halves.
- `GAME-0208`, `GAME-0226`, `GAME-0235` and `GAME-0242` retain `SYS-691`.
  `GAME-0242` also retains `SYS-765`. Their signatures do not change.
- Forza Horizon 6 remains the selected lower-ID neighbour of `GAME-0199`. The
  shared set stays at fifteen genes while the union grows by one, so the score
  becomes `15 / 36 = 0.416667`.
- A full comparison migration and combination-supporter recomputation are
  required. No new combination is introduced.

## Corpus accounting

- Canonical definitions remain 2,453.
- Active definitions: 2,400 → 2,399.
- Inactive definitions: 53 → 54.
- System definitions remain 850; Active Systems: 831 → 830.
- Active game-gene usages rise by one because `GAME-0199` replaces one
  compound ID with two live IDs.
- Games, combinations and families remain 288, 274 and 17.
- Earlier reviewed signatures changed: `0`; only direct owner `GAME-0199` is
  migrated.

## Localisation disposition

- `SYS-641`: removed from the current Ukrainian Active registry because it is
  now a lifecycle alias.
- `SYS-765` and `SYS-691`: `corrected` — both Ukrainian labels and boundaries
  are made reserve-neutral, and their reviewed carrier range becomes
  `GAME-0199`–`GAME-0242`.
- `GAME-0199`, `COMB-0197`, its salience partition and its plain-language cards:
  `corrected` for the split representation.
- Unchanged game-local descriptions for the five existing carriers: `verified`;
  ordinary nitro, Burst Nitrous, product names and stable IDs are
  `retained-with-reason` as carrier parameters or official identifiers.

## Rejection condition

Reopen either reuse only if a carrier demonstrates a different accumulation or
settlement transition that cannot be expressed through reserve identity, cap,
eligible manoeuvre, gain, persistence horizon, activation, spend rate,
acceleration, release, depletion or bounded-effect cutoff. A future review of
`SYS-540` must not be inferred from this decision: its spatial pad lifecycle and
directed-thrust coupling require an independently confirmed unit.

## Change history

- 2026-09-10 — accepted as `BATCH_017_TAXONOMY_CORRECTION_002` after a fresh
  all-carrier review split `SYS-641` and confirmed reuse of both existing
  transition boundaries.
