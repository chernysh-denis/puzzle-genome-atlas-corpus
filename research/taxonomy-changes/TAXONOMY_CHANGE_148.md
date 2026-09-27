# Taxonomy Change 148: Passive base-facility income

## Status

- Proposal status: Accepted
- Claim status: Confirmed
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-26
- Trigger: `GAME-0410` *Halo Wars*, original Xbox 360 Normal campaign
  mission 02, `Relic Approach`.
- Scope: admit `SYS-1094` as Active; reuse sixteen existing boundaries.
  No older signature or verified combination changes.

## Problem and accepted change

The completed UNSC Supply Pad sends supplies into a shared base stockpile
over live time without a worker, discrete delivered crate or player harvest
command. Placing more Pads uses finite base sockets that could otherwise
host production. `SYS-1094` isolates the recurrent facility-to-stockpile
transition; the socket constraint, paid training and unit commands reuse
`CON-001`, `CON-467`, `SYS-551` and `ACT-189`.

## Transfer and rejection test

- `SYS-549` requires an assigned worker, world source, carried load and
  drop-off. None exists in the Supply Pad delivery cycle.
- Finite field crates are not the source of the recurring Pad income;
  optional crate collection is outside this bounded route.
- The one-Marine queue and five-Marine gate are existing production and
  authored dependency boundaries, not newly branded Halo genes.
- `OBJ-185` covers destruction of the single designated Detonator and
  successor mission. No new objective is necessary.

## Evidence and limits

- [Microsoft's original Xbox 360 *Halo Wars*
  manual](https://download.microsoft.com/download/F/9/9/F99AB8F0-5191-4EDD-B312-7A9B9E4784FA/HaloWars_MNL_EN-US.pdf),
  printed pp. 12–13 and 22–23, directly distinguishes field supplies
  from Supply Pads and describes their resource delivery and socket trade-off.
- [Prima's official mission 02
  guide](https://primagames.com/eguides/halo-wars-eguide/campaign-act-1/02-relic-approach)
  places the Pad inside the opening base-production chain. No original
  disc execution or exact rate measurement was performed.
