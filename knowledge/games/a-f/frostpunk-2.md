---
game_id: GAME-0504
slug: frostpunk-2
game_title: Frostpunk 2
analysis_status: reviewed
reviewed: 2026-10-06
combination_ids: []
gene_ids:
  action:
    - ACT-006
    - ACT-120
    - ACT-121
    - ACT-139
    - ACT-140
    - ACT-144
    - ACT-166
    - ACT-168
    - ACT-181
    - ACT-683
    - ACT-684
    - ACT-685
    - ACT-686
    - ACT-687
    - ACT-688
    - ACT-689
  system:
    - SYS-156
    - SYS-161
    - SYS-194
    - SYS-229
    - SYS-230
    - SYS-289
    - SYS-1396
    - SYS-1397
    - SYS-1398
    - SYS-1399
    - SYS-1400
    - SYS-1401
    - SYS-1402
    - SYS-1403
    - SYS-1404
    - SYS-1405
    - SYS-1406
    - SYS-1407
    - SYS-1408
    - SYS-1409
  constraint:
    - CON-062
    - CON-136
    - CON-173
    - CON-184
    - CON-185
    - CON-200
    - CON-258
    - CON-775
    - CON-776
    - CON-777
    - CON-778
    - CON-779
    - CON-780
    - CON-781
  information:
    - INF-059
    - INF-067
    - INF-071
    - INF-086
    - INF-113
    - INF-186
    - INF-486
    - INF-487
    - INF-488
  objective:
    - OBJ-287
  time:
    - TIM-003
---

# Game: Frostpunk 2

## Analysis scope

- Version / ruleset: original fully released Windows English base Story,
  reconstructed from 11 bit studios' release-day guide dated 2024-09-20 and
  the contemporary Chapter 1 objective sequence. The target is the original
  qualitative district-demand ruleset, not the later Heat Management redesign.
  Officer is the specified reproduction preset with Survivor off; the guide's
  captured preset and installed executable/build are not established. Exact
  costs, durations, severity coefficients and preset-specific starting stocks
  are parameters to read from that run, not facts inferred from the guide.
- Structured analysis target: existing `PLAT-WINDOWS-PC`; original released base
  Story / complete Chapter 1, publisher-guide-qualified 2024-09-20 ruleset.
  No Mac or console mechanical equivalence or complete release audit is claimed.
- Primary decision loop: inspect capital needs, finite labour, funding and
  political support; clear and allocate district footprints, research and
  install a coal-production variant, negotiate the governing vote and keep
  credible promises while the live city consumes supplies; reserve regional
  teams, discover and colonise the oil site, connect it, then balance both
  settlements and their directed shipments until the capital receives the
  chapter's required continuing oil output.
- Entry and exit: fresh ordinary Chapter 1 New London control after the
  Wanderers prologue, recording the carried prologue choice and population
  rather than pretending they are always identical. Include initial coal and
  shelter objectives, Scraping the Barrel, Council Hall and Vote of Confidence,
  western exploration, the Old Dreadnought grave decision, establishment and
  management of that colony, completed connection and at least 75 Oil Output
  incoming to New London. Exit at the resulting Chapter 2 ordinary control
  before its new choice/upgrade objectives. A single coal district, finding oil,
  founding an unconnected colony or possessing 75 stored oil units is not the
  complete packet. Loss of the capital or governing authority is a negative
  terminal before that positive exit.
- Included: all causally coupled district, footprint, expansion and building
  slots; construction-material recovery and bounded local resource stocks; workforce fractions; finite deposits; extraction and industrial
  production; housing, food, heat, materials, goods and city problems; treasury
  income and targeted community interventions; generator and available Overdrive;
  Idea Tree variants, research acceleration and prerequisites; council proposals,
  negotiations, votes, recess and promise deadlines; group relations, ideology,
  trust, tension and local protest blocking with explicitly qualified launch recovery; Frostland exploration, harvesting and relevant
  outposts; trail construction; local colony population/needs and bilateral
  rate-controlled supply. Reachable supporting research, buildings and laws are
  parameters of these systems, not omitted merely because the mandatory path
  can be short.
- Excluded: prologue as a separate gameplay packet, Utopia Builder/random maps,
  Chapter 2's Defeat/Embrace the Frost generator branches and scheduled whiteout
  challenge, later Winterhome/civil-war endings, DLC and Fractured Utopias,
  later heat-level redesign, other difficulty/preset claims, mods, achievements,
  exploitation of reported launch bugs and console or Mac execution. The
  inherited prologue choice remains an input parameter, not a retroactive union.
- Potential scoped modules: later whiteout survival; separate generator-path
  decisions; Winterhome relocation; civil-war settlement; Utopia Builder.
  No separate module IDs or unsupported product-wide genome are invented.
- Direct-play status: not conducted. The dated official transcript and actual
  muted paused frames establish source-described controls and displayed state,
  not original executable, mouse input, RNG, save writing or current parity.
  Secondary exact thresholds and failure particulars remain qualified below.
  P1 is the complete manual English transcript of the official guide published
  2024-09-20 and seven actual paused frames at 580, 670, 745, 805, 895, 1125
  and 1185 seconds. These show footprint-effect contact, distinct requirements
  and demand with local storage capacity, a research variant with labour and
  consequences, council positions, colony transition and bilateral resource
  transfers. They are not our complete chapter input trace. P2 is the
  co-director's postrelease design account; P3 confirms the actual release;
  P4 archives the publisher's 2024-10-04 protest recovery fix, qualifying
  intended behaviour rather than proving a bug-free original executable.
  S1 is the completely inspected release-day Chapter 1 guide; S2 covers
  contemporary council/negotiation rules; S3 qualifies original Overdrive
  accident and repair; S4 covers income and interventions during released
  advanced access, not the beta. S6 provides later chapter corroboration with
  qualified grave and failure details. S5 is indexed-only: stored-resource
  shipping during a production deficit remains Limited/Medium. S7–S10 are
  dated player reports, not a primary executable or exact specification.
  The universal-whiteout contradiction is neither hidden nor declared solved.
  All media inspection ran hidden, muted and paused in background processes.
  Audio was not analysed; user focus, windows, fullscreen and system sound
  were not changed, and source frames are not redistributed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FP2-001` | The Windows product fully released on 2024-09-20; the target is complete capital-to-oil Chapter 1, not Early Access or the later heat redesign | Observation | Corroborated | High | P1–P3, S1, S6 |
| `FP2-002` | Paid timed Frostbreaking opens fixed connected cell groups; districts reserve compatible cleared footprints and expansion supplies host capacity and building slots | Observation | Corroborated | High | P1 7:58–9:25/12:09–13:02; S1; frames 580/745 |
| `FP2-003` | District area effects require sufficient own-cell contact, with three affected cells in the original guide; shelter and compatible neighbours can reduce heat demand whereas incompatible proximity can increase disease | Observation | Direct | High | P1 9:26–10:24; frame 580 |
| `FP2-004` | Employment fractions scale workforce requirements, operating-resource requirements and output; hard requirements differ from soft city demand | Observation | Direct | High | P1 10:24–11:44 excluding disputed whiteout sentence; frame 670 |
| `FP2-005` | The enabled original generator burns available compatible fuel against aggregate heat demand; initial capital fuel is coal, not automatically the later oil-upgraded configuration | Observation | Corroborated | High | P1 2:36–3:43; S3; S6 |
| `FP2-006` | Unmet aggregate needs accumulate cold, disease, hunger, squalor or crime and can harm population, district condition and tension without instant universal shutdown | Observation | Direct | High | P1 3:43–5:34 |
| `FP2-007` | Construction, research and law choices move three opposing Zeitgeist axes and affect group relations through their worldviews | Observation | Direct | High | P1 7:25–7:58; P2 |
| `FP2-008` | Group interventions, promises and relations affect trust; support can produce rallies, opposition protests, and sufficiently lost trust causes deposition | Observation | Corroborated | High | P1 5:34–7:25/14:51–15:52; S2, S4, S6 |
| `FP2-009` | A Research Institute in a compatible housing slot unlocks the Idea Tree; selected community variants affect relations, more institutes speed research and Rush Researchers costs trust | Observation | Direct | High | P1 12:25–14:04; S1 |
| `FP2-010` | Finite assigned Frostland Teams explore eligible regions with disclosed cost, time and risk, revealing sites and separately staffing harvests; ordinary harvests need not have trails | Observation | Direct | High | P1 15:52–18:38; S1 |
| `FP2-011` | Paid trail construction connects discovered sites; outposts and colonies have access, team and other cost requirements distinct from simple harvesting | Observation | Corroborated | High | P1 17:48–18:58; S1 |
| `FP2-012` | Connected separately managed settlements configure directed resource rates bounded by current route capacity and available source resources | Observation | Corroborated | High | P1 19:36–20:12; frame 1185; S1 |
| `FP2-013` | Colonies have local population/workforce/needs, require manual residents instead of automatic growth, and do not replace the capital's whole-game survival authority | Observation | Direct | High | P1 18:38–19:36 |
| `FP2-014` | Weekly Heatstamp income depends on population and goods provision; faction fundraising is a separate lump sum with a relationship cost | Observation | Corroborated | Medium | S4 dated 2024-09-19; S6; P1 currency/community overview |
| `FP2-015` | Original Overdrive improves fuel efficiency while accumulating stress; its critical accident and repair consequences are secondary-source-qualified, not the first game's assumed instant explosion | Observation | Limited | Medium | S3 dated 2024-09-20; S7; SYS-1408 boundary review |
| `FP2-016` | The chapter advances only after its ordered prerequisites and required incoming 75 Oil Output; voting needs support and recess, not unilateral signing | Observation | Corroborated | Medium | S1 release-day objectives; P1 14:04–15:52; S2; S6 |
| `FP2-017` | The guide's statement that whiteouts disable all districts conflicts with dated reports of continuing housing/fuel districts; this packet exits before the Chapter 2 whiteout challenge and admits no universal shutdown rule | Observation | Conflicting | Medium | P1 10:38; S8, S9; S10 |
| `FP2-018` | Leaving the Old Dreadnought grave intact forgoes an oil locus; clearing it opens that locus with a disease consequence | Observation | Limited | Medium | S6 last updated 2024-10-25; S1 site progression; later patch parity unclaimed |
| `FP2-019` | Completed demolition returns eligible construction Prefabs, not an asserted full refund of every currency | Observation | Direct | High | P1 11:44–12:09 |
| `FP2-020` | A faction protest blocks a district; intended relation-based resolution removes the block, but a later fix proves launch recovery was not universally reliable | Observation | Corroborated | Medium | P1 6:22–6:51; P4 2024-10-04 |
| `FP2-021` | Repeating governing commitments requires applicable recess or group readiness in addition to support and cost | Observation | Corroborated | Medium | S2 council recess; S4 qualified intervention recovery |
| `FP2-022` | Resource stocks expose separate compatible finite local capacities, distinct from route-transfer capacity | Observation | Direct | High | P1 actual paused frames 670/1185 |

## Basic data

- Release / origin: 11 bit studios, full Windows release 2024-09-20. The
  primary release-day material describes the shipped sequel's expanded scale,
  district planning and politically constrained government.
- Platform or physical form: existing Windows computer target; pausable
  real-time aggregate city and colony management with simulation weeks.
- Puzzle family: spatial automation, network construction, live system pressure
  and ordered dependency sequencing. Family assignment requires checking the
  existing registry rather than deriving a genre label.
- Primary sources:
  - **[P1]** [11 bit studios: Frostpunk 2 Beginner's Guide](https://www.youtube.com/watch?v=IAqJIRw9RHE), published 2024-09-20, 1,260-second source. Complete manual English transcript inspected, plus actual paused frames at 580, 670, 745, 805, 895, 1125 and 1185 seconds. Source-specific chapter/time locators above distinguish statements from frames.
  - **[P2]** [Co-director Kuba Stokalski on the released sequel](https://news.xbox.com/en-us/2024/09/20/why-frostpunk-2-is-a-true-and-creatively-necessary-sequel/), creator guest article dated 2024-09-20; Windows launch, scale and political design, not a present-day Xbox ruleset.
  - **[P3]** [11 bit studios revenue report](https://ir.11bitstudios.com/en/news/11-bit-studios-reports-surge-in-revenue-and-earnings/), publisher confirmation of the actual 2024-09-20 PC release. The June date announcement alone would not prove that launch occurred.
- **[P4]** [Publisher release notes archived by GOG](https://www.gogdb.org/product/1728870436/releasenotes), 1.0.5_RC2 dated 2024-10-04: intended district unblock after relation-resolved protest. This qualifies an original launch bug, not a claim of corrected executable parity.
- Secondary sources:
  - **[S1]** [Game8: Chapter 1](https://game8.co/games/Frostpunk-2/archives/473603), last updated 2024-09-20 06:49, complete article inspected in a hidden muted browser despite the text-fetch payment response. Source describes the whole ordered packet and 75 Oil Output terminal; its recommendation about a mine not decreasing workforce is not adopted literally.
  - **[S2]** [Gamepressure: Council](https://www.gamepressure.com/frostpunk-2/council/zf115fb), last updated 2024-09-30; 51 ordinary votes, exceptional Rule support, automatic proposal timer, ten-week recess and negotiated promise deadlines. Later-than-launch corroboration, not build identity.
  - **[S3]** [Keenan McCall: original beginner guide](https://twinfinite.net/guides/frostpunk-2-beginners-guide-how-to-frostbreak-gather-resources-more/), updated 2024-09-20; clearing, districts and qualified Overdrive accident/repair.
  - **[S4]** [Sean Martin: Heatstamps](https://www.pcgamer.com/games/city-builder/frostpunk-2-heatstamps/), published 2024-09-19 during released advanced access; weekly population/goods income and faction costs. Its tentative forty-week cooldown is not a confirmed exact value.
  - **[S5]** [Neoseeker: Chapter 1](https://www.neoseeker.com/frostpunk-2/Chapter_1), indexed-only access; full retrieval stopped at a security challenge. Stored-resource shipping despite a production deficit is Limited/Medium corroboration, not a directly replayed flow.
  - **[S6]** [Gamepressure: Chapter 1](https://www.gamepressure.com/frostpunk-2/chapter-1/z0115de), last updated 2024-10-25; complete capital, vote, exploration, grave and colony sequence. Late corroboration retains explicit grave/failure limitations; no bug-exploitation instructions are adopted.
  - **[S7]** [Original Overdrive discussion](https://steamcommunity.com/app/1601580/discussions/0/4699035743124843431/), dated 2024-10-24; efficiency saves consumed fuel rather than creates it. Player reports are not a primary executable or exact accident specification.
  - **[S8]** [Dated whiteout district management report](https://steamcommunity.com/app/1601580/discussions/0/4851029895189299247/), 2024-09-27; qualified counterevidence to universal district shutdown.
  - **[S9]** [Dated surviving fuel/housing operation report](https://steamcommunity.com/app/1601580/discussions/0/4851030529138171224/), 2024-10-05; no import of its difficulty or later build.
  - **[S10]** [Chapter 2 whiteout timing reports](https://steamcommunity.com/app/1601580/discussions/0/4851030925562609024/), dated 2024-10-08/09; oil-delivery transition starts a later timer. Different reported weeks are parameters, not one exact global schedule.
- Claim IDs: `FP2-001`–`FP2-022`. None of these records claims our own native play.

## Mechanical decomposition

### Action Genes

- Unchanged transfers: simulation acceleration; research target; district-hosted
  ordinary building commitment and demolition; bounded persistent dilemma;
  typed cell-clearing order; district enabled state/unlocked ability; generator
  mode; industrial output recipe; law proposal, negotiation and vote.
- New admitted boundaries: connected multi-cell district/expansion commitment;
  employment fraction; regional-team assignment; trail construction;
  directed resource rates; resident relocation; targeted community intervention.
  Existing labels mentioning another game's setting do not prevent reuse when
  their unchanged operational definitions fit.
- Parameters: full-rate staffing, costs and construction time; initial/extension
  cells; actual run's unlocks, research variants and laws; current group
  intervention availability; intended oil and counter-directed supply rates.
- Claim IDs: `FP2-002`, `FP2-004`, `FP2-005`, `FP2-008`–`FP2-013`, `FP2-016`.

### System Behaviour Genes

- Unchanged transfers: supplied production; finite deposit depletion; eligible
  staffed research; authored forecast changes; event and promise-choice arcs; supported-law
  enactment. Do not add direct scout-avatar locomotion or individual medical
  bed simulation to an aggregate district model.
- New admitted boundaries: paid timed clearing/build/expansion completion;
  contact-threshold area effects; fractional operation; demand-driven fuel
  burn; aggregate deficit problems; ideology/group alignment; promise and
  political-reaction trust updates; regional exploration/harvest resolution;
  separately balanced shipment flows; distinct capital/colony population;
  periodic currency income; recoverable demolition materials; generator efficiency/stress accident and local district protest blocking. Operational boundary review accepts these distinct actors, predicates and mutations, with their explicit evidence limitations.
- Resolution order: accepted commitments reserve/pay their requirements;
  running simulation progresses work, research and exploration; completed
  sites and connections expose capabilities; operating fractions determine
  requirements and output; stocks, consumption and directed flows change
  balances; unmet demand accumulates problems; authored objectives, events,
  promises and political consequences resolve when their predicates apply.
  This is a causal partial order, not a claimed measured internal engine tick.
- Parameters: unknown internal step ordering, rounding, exact efficiencies,
  preset coefficients and injury randomness remain unmeasured.
- Claim IDs: `FP2-002`–`FP2-015`.

### Constraint Genes

- Unchanged transfers: static incompatible footprints; persistent prerequisites;
  matching extraction locus; owned design and build payment; finite workforce;
  chamber eligibility/support. Do not require the first game's permanent
  signing branch or an invented one-building-per-day rule.
- New admitted boundaries: cleared connected district cells and expansion allowance;
  compatible district host/free slot; hard requirements distinct from soft
  demand; team/site/trail requirements; source availability/connection capacity;
  continuing capital and governing authority; governing-session and intervention recovery. CON-200 is retained unchanged: compatible typed storage, remaining capacity and any declared connection apply without inventing mandatory physical hauling.
- Scarce strategic resources: Heatstamps, Prefabs, cores, available workforce,
  clear compatible cells, district slots, finite deposits, Frostland Teams,
  connection capacity, political support, deadlines and tolerable problems.
- Claim IDs: `FP2-002`, `FP2-004`, `FP2-008`–`FP2-013`, `FP2-016`.

### Information Genes

- Unchanged transfers: dependencies/recipes, objective/promise conditions,
  aggregate economy and population/workforce reports, council seats/support,
  and eligible district cells with previewed adjacency effects. A district
  lens can reuse the existing disclosure boundary with a multi-cell parameter;
  that does not reuse Civilization's distinct single-hex placement rule.
- New admitted boundaries: generator fulfilment/fuel/stress; known regional sites and
  activity costs/duration/risk; distinct ideology axes, relations, trust and
  tension. Undiscovered Frostland is not omniscient and a risk label does not
  expose an exact RNG distribution.
- Claim IDs: `FP2-002`–`FP2-013`, `FP2-015`, `FP2-016`.

### Objective Genes

- Unchanged transfers: no existing objective has yet passed the complete
  capital-preparation plus colony-incoming-rate boundary test.
- New admitted boundaries: complete the ordered chapter gates and establish the
  required incoming fuel rate while capital/government remain viable.
- Success, evaluation and failure: 75 Oil Output is an incoming-rate objective,
  not 75 inventory units. Losing the confidence vote is a reported immediate
  negative terminal, distinct from ordinary temporary tension. Capital collapse
  ends the whole attempt even with a surviving colony; colony loss alone is
  local. Stored source resources can sustain a flow for a limited period,
  so positive current net production is not imposed as an invented extra gate.
- Claim IDs: `FP2-008`, `FP2-012`, `FP2-013`, `FP2-016`.

### Time Genes

- Unchanged transfers: `TIM-003`; live pausable/accelerable simulation permits
  concurrent planning while needs, production, research, work and travel
  advance. Council recess, proposal timeout, promises and ability recovery
  are scheduling parameters with separate legality where required.
- New admitted boundaries: none on the evidence currently reviewed.
- Claim IDs: `FP2-001`–`FP2-016`.

## Reproducible transitions

These are source-reconstructed tests for the specified original ruleset, not
claims that we executed an installed build. Numeric run-specific values must
be recorded from its interface; qualitative outputs below remain bounded.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Frozen cells outside cleared city ground | Reserve a connected Frostbreaking group, pay and allow work time | Selected cells become buildable after completion, not at preview | Clearing command, cost/requirements and timed mutation differ | `FP2-002` |
| Cleared ground lacks enough free cells beside an existing district | Try to extend that district | The requested extension is unavailable rather than overwriting occupied ground | Expansion geometry and ordinary clearance are independent | `FP2-002` |
| Unexpanded housing district has no building slot | Select the base-available Research Institute | Placement still needs an expanded compatible host with a free slot | Known blueprint alone does not provide host capacity | `FP2-002/009` |
| A preview touches only two cells of an influence area | Adjust the footprint to put a third cell inside | Original guide's area effect becomes applicable at the contact threshold | Contact count is not single-tile adjacency | `FP2-003` |
| Coal district uses workers needed elsewhere | Reduce its employment fraction | Worker requirement and coal output both decrease | Reallocation sacrifices production; it is not a free worker grant | `FP2-004` |
| District requirements are fulfilled but aggregate heat demand is not | Let time advance | The supplied district can still output while cold/problem consequences develop | Soft demand differs from a hard operating requirement | `FP2-004/006` |
| Base generator enabled with finite coal and increasing city demand | Build another heated district and let time advance | Aggregate demand changes the compatible-fuel draw and fulfilment | Original demand-driven burn is not a radial fixed-output rule | `FP2-005` |
| Reachable Coal Mines topic and functioning institute | Choose one community variant and finish research | Its design becomes available and its community relation changes; the mine still requires construction | Research target, relationship and actual building are separate | `FP2-007/009` |
| More than one completed Research Institute | Research the same reachable topic | Additional institute capacity increases speed | A repeated facility is not a second independent technology target | `FP2-009` |
| Current law proposal lacks enough eligible support | Negotiate a feasible promise with a non-refusing group, then call the vote | Acquired support can change the vote; a passed proposal applies its law | Promise commitment and legislative authority differ from unilateral signing | `FP2-008/016` |
| A negotiated promise deadline remains open | Fulfil its declared research/build/law condition, or allow it to expire unmet | Group relation consequences differ between fulfilment and failure | Future obligations are real state, not flavour text | `FP2-008` |
| Known region requires more teams than currently free | Try to assign its exploration | Existing reservations prevent an unsupported simultaneous assignment | Regional team capacity differs from direct scout equipment | `FP2-010` |
| Eligible western exploration reaches completion | Inspect the revealed sites | The new oil site becomes known without making a colony or fuel flow automatically | Discovery is not extraction or delivery | `FP2-010/016` |
| Discovered ordinary harvesting area has enough eligible teams | Assign harvest without building a trail | Ordinary harvest eligibility does not require the outpost's extra trail gate | Nearby activity classes do not inherit identical connection requirements | `FP2-010/011` |
| Discovered oil colony and an incomplete connection | Set an intended capital oil flow | The requested rate cannot create a usable completed connection | Trail commitment, completion and shipment are separate | `FP2-011/012` |
| Connected colony has oil stock but current production is below intended export | Configure a supported shipment while stock remains | Stored source availability can sustain transfer until exhausted | Positive current surplus is not an additional unconditional shipping gate | `FP2-012`, S5 Limited/Medium |
| Colony residents need food while capital needs oil | Configure counter-directed food and oil rates within capacity | Separate balances change without merging local population or creating goods | Bilateral flow differs from one shared city inventory | `FP2-012/013` |
| Old Dreadnought has shelter but insufficient population | Wait without relocating residents, then explicitly relocate eligible residents | Shelter alone does not provide automatic colony growth; committed residents change local labour and needs | Manual colony population is not capital growth | `FP2-013` |
| Grave-associated oil locus remains protected | Retain the grave or commit its clearance response | The protected locus remains unavailable or opens with the qualified disease consequence | A persistent event choice changes eligible extraction | `FP2-018` Limited/Medium |
| Chapter prerequisites complete and incoming oil rate below required value | Raise supported incoming Oil Output to at least 75 | The complete chapter advances to ordinary Chapter 2 control | Rate-based successor gate, not one stored stock or first-build success | `FP2-016` |
| Colony remains viable but capital/governing authority reaches its negative terminal | Continue simulation | The surviving colony does not override whole-attempt failure | Capital authority and local colony survival are distinct | `FP2-008/013` |
| Completed obsolete district | Commit eligible demolition | District state is removed and recoverable Prefabs return; not every paid currency is presumed refunded | Material recovery differs from physical builder routing | `FP2-019` |
| Generator operating normally with available fuel | Enable available Overdrive while time advances | Fuel efficiency improves while stress accumulates; critical accident/repair remains source-qualified | No first-game permanent explosion or exact unmeasured cooling formula | `FP2-015` Limited/Medium |
| District occupied by an active faction protest | Satisfy an eligible political resolution | Intended block removal allows operation if other requirements hold; launch bug parity is not guaranteed | Protest is operational, and later bug repair is not original native evidence | `FP2-020` |
| A council vote just resolved | Attempt another proposal during recess | The next session must become ready before a new vote | A successful result does not bypass governing cadence | `FP2-021` |
| Colony and capital have separate oil stores | Inspect stock capacity and proposed transfer | Each compatible local store retains its own capacity, distinct from the connecting route limit | Local storage is not one shared resource container | `FP2-022` |

## Strategic and experiential structure

- Local decision: change district shape and employment to meet a real need
  without exhausting the labour, funding and capacity needed for the next gate.
- Medium-term planning: choose research and promises that can actually be
  fulfilled while preserving a credible coalition; reserve exploration teams
  and route costs before the coal deposits become strategically limiting.
- Long-term structure: create a second economy and connect its oil supply
  without abandoning local food, heat, workforce or capital authority.
- Common heuristics: use sufficient sheltered-area contact; compare full cost
  and side effects of mine variants rather than blindly choosing a guide's
  recommended one; distinguish incoming resource rate from stored quantity.
  These are Hypothesis/Limited/Medium heuristics, not optimal-policy proofs;
  counterexamples are adverse staffing, unmet promises or changed preset costs.
- Failure attribution: hard requirements, demand problems, trust and local
  losses expose different causes. Later bug reports and source disagreement
  prevent a guarantee of universally correct original feedback.
- Player-trust factors: previewed footprint effects and disclosed votes help
  planning, but unsourced numeric coefficients and future event outcomes must
  not be presented as knowledge available in every live state.
- Claim IDs: `FP2-002`–`FP2-017`; heuristics explicitly qualified above.

## Replay and variation

- What changes between sessions: carried prologue choice, chosen district
  shapes, mine variants, promises/laws, exploration order, grave response and
  supply allocation; preset values are held fixed to Officer for reproduction.
- Randomness or procedural generation: the fixed Story map is not the
  Utopia random-map generator. Disclosed exploration risk does not by itself
  prove a specific stochastic distribution. No unseen RNG rule is admitted.
- Multiple viable strategies: alternative coal variants and political bargains
  are disclosed; no complete optimal-route or every-ending inventory is claimed.
- Typical replay motive: Hypothesis/Limited/Medium — compare a different
  coalition or spatial economy under the same complete fuel objective; this
  expectation is weakened if the alternate choices do not change viable plans.
- Claim IDs: `FP2-007`–`FP2-018`.

## Adjacent systems and history

- Direct predecessors: original Frostpunk; its individually staffed workplaces,
  radial heat, unilateral law signing and scout cargo are not imported as
  identical sequel rules.
- Variants: later Heat Management redesign, Utopia Builder and console/Mac
  releases remain outside this original Windows Chapter 1 target.
- Similar games: mathematical neighbours are determined only by the full
  lower-ID signature scan after operational admission; theme does not select them.
- Important differences: fixed multi-cell districts and aggregate labour;
  negotiated support with future promises; region-team capacity; a separate
  manually populated colony and directed rate rather than a shared settlement.
- Claim IDs: `FP2-001`–`FP2-016`; comparison deferred to deterministic scan.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-120`, `ACT-121`, `ACT-139`, `ACT-140`, `ACT-144`, `ACT-166`, `ACT-168`, `ACT-181`, `ACT-683`, `ACT-684`, `ACT-685`, `ACT-686`, `ACT-687`, `ACT-688`, `ACT-689` | No unadmitted candidate; numeric costs, capacities, timing and executable-specific coefficients remain parameters |
| System Behaviour | `SYS-156`, `SYS-161`, `SYS-194`, `SYS-229`, `SYS-230`, `SYS-289`, `SYS-1396`, `SYS-1397`, `SYS-1398`, `SYS-1399`, `SYS-1400`, `SYS-1401`, `SYS-1402`, `SYS-1403`, `SYS-1404`, `SYS-1405`, `SYS-1406`, `SYS-1407`, `SYS-1408`, `SYS-1409` | No unadmitted candidate; numeric costs, capacities, timing and executable-specific coefficients remain parameters |
| Constraint | `CON-062`, `CON-136`, `CON-173`, `CON-184`, `CON-185`, `CON-200`, `CON-258`, `CON-775`, `CON-776`, `CON-777`, `CON-778`, `CON-779`, `CON-780`, `CON-781` | No unadmitted candidate; numeric costs, capacities, timing and executable-specific coefficients remain parameters |
| Information | `INF-059`, `INF-067`, `INF-071`, `INF-086`, `INF-113`, `INF-186`, `INF-486`, `INF-487`, `INF-488` | No unadmitted candidate; numeric costs, capacities, timing and executable-specific coefficients remain parameters |
| Objective | `OBJ-287` | No unadmitted candidate; numeric costs, capacities, timing and executable-specific coefficients remain parameters |
| Time | `TIM-003` | No unadmitted candidate; numeric costs, capacities, timing and executable-specific coefficients remain parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `503` (`GAME-0001`–`GAME-0503`).
- Exact genome matches: none.
- Tied near matches: `GAME-0130` — Frostpunk (`20 / 94 = 0.212766`).
- Supported combination subsets: none.
- Scan date: 2026-10-06.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0130` — Frostpunk | Time acceleration, building/recipe/ability commitments, finite labour and deposits, supplied production and research, forecast/event progression, resource and objective disclosures, pausable live time | The first game allocates individual workers, radial heat and medical beds, signs unilateral branch-closing laws, routes scout cargo and ends with the Great Storm. This complete sequel chapter allocates multi-cell districts and fractional labour, requires chamber support and promises, manually populates a separate colony and reaches an incoming fuel-rate successor. Its repair-qualified Overdrive and protest recovery do not inherit permanent first-game explosion or bug-free launch parity. | Sole positive non-exact maximum, `0.212766`; the canonical comparison above owns the fraction. |

### Preserved research notes

- New genes: 32 bounded additions and 29 unchanged transfers; all 274 verified combinations tested as proper subsets, none supported.
- Classification result: whole-chapter multi-city political district management, not a first-coal excerpt or a product-wide union.
- Evidence and reasoning: 503 lower-ID signatures scanned without selecting neighbours by title or theme. Five existing causal families fit regional connections, configured autonomous production, live pressure, scarce-team coordination and ordered dependencies.

## Taxonomy impact

- Registry changes: 32 Active additions; 29 existing operational definitions retained unchanged.
- Taxonomy-change record: [TAXONOMY_CHANGE_241](../../../research/taxonomy-changes/TAXONOMY_CHANGE_241.md).
- Candidate terms affected: district threshold contact, fractional staffing,
  separate demand/requirements, ideological group relation, regional teams,
  manual colony population and rate-bounded fuel delivery.

## Negative results

- No separate prior corpus claim is revised. The guide's universal whiteout
  shutdown statement is not admitted; conflict and original/corrected-build
  uncertainty remain explicit rather than fabricated into a resolved rule.

## Delta summary

## New facts

- [Observation | Corroborated | High] Dated shipped Windows district economy
  and complete capital-to-oil chapter are reconstructed with separate primary
  and secondary roles (`FP2-001`–`FP2-016`).
- [Observation | Conflicting | Medium] Universal whiteout district shutdown
  remains contradicted and outside this earlier terminal (`FP2-017`).

## New genes

- [Observation | Corroborated | Medium] Thirty-two distinct district, political, regional, supply, recovery and terminal boundaries admitted after operational review; the accident-specific SYS-1408 remains Limited/Medium. Twenty-nine definitions transfer unchanged, including optional-link storage capacity, not physical hauling.

## New combinations

- [Observation | Corroborated | High] All 274 verified combinations scanned; no proper subset applies. No single-game combination is invented.

## Taxonomy changes

- [Observation | Corroborated | Medium] TAXONOMY_CHANGE_241 accepts only this complete packet; no prior English gene or game signature changes. Full-genome salience review partitions 12 defining, 33 structural and 16 supporting genes without altering admission or comparisons.

## New questions

- Which exact original executable/preset reproduces the qualified grave and
  Overdrive particulars, and how do reported launch bugs alter recovery?
- How do later redesigned heat rules change this original aggregate-demand
  packet under a separately authorised version comparison?

## Next recommended game

- [Hypothesis | Limited | Medium] Original Sega Saturn Panzer Dragoon,
  `GAME-0505`, only after this complete unit and its sole local commit.
- Optimisation criterion: preserve the approved mixed-era, cross-platform order.
- Expected information gain: authored rail travel, reticle acquisition and
  delayed lock-on resolution versus spatial multi-city political simulation.
- Backlog impact: no push, publication, deploy or implicit next unit before acceptance.

## Why this game

- [Hypothesis | Limited | Medium] Fractional district economies and promised
  political support introduce useful counterexamples to individually staffed
  construction and unilateral laws. This expectation fails if operational
  review finds those boundaries already represented unchanged elsewhere.
