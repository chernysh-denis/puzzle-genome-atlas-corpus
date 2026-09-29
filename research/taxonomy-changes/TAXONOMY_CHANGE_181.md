# Taxonomy Change 181: First-spring field and shipment loop

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-09-28
- Trigger: `GAME-0444` *Harvest Moon: Back to Nature*, original English
  PlayStation first-Spring crop cycle through Summer 1.
- Scope: admit `ACT-578`, `ACT-579`, `SYS-1162`–`SYS-1165`, `CON-718`,
  `CON-719`, `OBJ-253` and `TIM-031` as Active. No earlier signature or
  verified combination changes.

## Problem and accepted change

The original manual separates clearing a farm patch, hoeing ordinary soil,
scattering one nine-position packet, caring for reachable crops over successive
days and shipping mature produce for money before seasonal turnover. Ordinary
outdoor time, tool stamina and the scheduled collector make the order matter;
indoor planning does not spend the same clock. A single generic “farm” gene
would erase the observable points where a seed fails to take root, a surrounded
center plant cannot be watered with a base can, or harvested produce misses
same-day pickup.

## Transfer and rejection tests

- Reuse `ACT-008` for direct movement, `ACT-130` for an offered seed purchase,
  `ACT-512` for tool-clearing one field obstruction, `ACT-213` for individual
  crop watering and harvest, `ACT-219` for committing a carried item to sale
  and `ACT-214` for sleeping into another farm day.
- Generalise `ACT-219`'s wording to distinguish the player's irreversible
  handoff from an immediate return: its existing ARC Raiders supporters still
  settle immediately, while this farm-bin sale waits for `SYS-1163`'s pickup.
  This changes no earlier game signature or supporter relation.
- Reuse `CON-311` for season/water/time crop viability, `INF-091` for weather
  and its forecast, `INF-136` for inspectable clock/farm resources and
  `TIM-003` for the running outdoor decision window.
- `ACT-578` writes prepared-soil state before `ACT-579` fixes a packet's
  multiple candidate positions. `CON-718` is the independent tile-acceptance
  predicate: one broadcast can partly fail over untilled cells. Neither the
  hoe nor the packet guarantees growth.
- `CON-719` instead concerns later reach. A fully planted dense 3 × 3 patch
  may have a living center crop that the base watering can cannot reach,
  whereas rain can water it. This is not the prepared-soil rule.
- `SYS-1162` updates growth at the day boundary when water or rain supplied
  care; `SYS-1164` changes the crop set and wilts old-season plants at a
  season boundary. The former is recurring daily progression, the latter a
  distinct calendar reset. Species, growth days and the 30-day duration are
  parameters, not separate genes.
- `ACT-219` commits produce to sale; `SYS-1163` settles eligible bin contents
  at the 5:00 pm non-holiday pickup. The player may harvest or deposit without
  earning that day's payment. `OBJ-253` names the bounded cultivated-to-paid
  outcome, not the three-year village appraisal.
- `SYS-1165` spends and restores farm-work energy, with collapse costing a
  workday rather than ending the game. `TIM-031` distinguishes automatically
  suspended interior clock time from the live outdoor `TIM-003` phase.
- Reject `SYS-344` as a whole: Project Zomboid's crop schedule is coupled to
  apocalypse utility cutoffs and food spoilage that are not evidenced here.
  Reject a generic immediate crop sale, automatic water of unreachable center
  plants, and later converted-edition rewind in the original PlayStation scope.

## Evidence and limits

The [original PlayStation instruction manual](https://oldgamesdownload.com/wp-content/uploads/manuals/harvest-moon-back-to-nature_ps1_manual_en_b8i.pdf)
directly documents the farm clock, house pause, soil preparation, nine-seed
packet, watering and reach, shipping cutoff, tool fatigue and seasonal crop
turnover. [Natsume's publisher announcement](https://www.natsume.com/news/news_pdffiles/pid_329_HM%20Back%20to%20Nature%20Coming%20Soon.pdf)
identifies the original North American PlayStation release. Two independent
[original-PlayStation crop](https://gamefaqs.gamespot.com/ps/446412-harvest-moon-back-to-nature/faqs/11583)
and [seasonal route](https://gamefaqs.gamespot.com/ps/446412-harvest-moon-back-to-nature/faqs/26294)
accounts bound the starting day and care loop. No disc, game execution, video
or audio was inspected. Exact growth arithmetic and weather probabilities
remain unmeasured.

## Decision

Accept ten typed boundaries with reviewed Ukrainian text and an original,
mechanically valid illustration after the repository and browser gates.
Approval covers one local game-unit commit only; it does not authorise push,
public publication or deployment.
