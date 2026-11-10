---
game_id: GAME-0485
slug: shenmue
game_title: Shenmue
analysis_status: reviewed
reviewed: 2026-10-02
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-107
    - ACT-341
    - ACT-597
    - ACT-649
    - ACT-650
  system:
    - SYS-045
    - SYS-1279
    - SYS-1280
    - SYS-1281
    - SYS-1282
  constraint:
    - CON-751
  information:
    - INF-142
    - INF-179
    - INF-372
    - INF-393
    - INF-461
  objective:
    - OBJ-274
  time:
    - TIM-003
---

# Game: Shenmue — original Dreamcast sailors-to-Charlie investigative lead

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Speaker names, addresses, opening hours and button identities are parameters, not genes per shop or cue.

## Analysis scope

- Version / ruleset: original English Dreamcast base edition, released in the West in 2000, Disc 1 Free Quest. The original Sega English booklet and written original-Dreamcast routes support the packet; exact regional disc revision, executable and save were not inspected. Area Jump is OFF, with ordinary default dialogue and control settings. This is not Shenmue II, the 2018 Shenmue I & II re-release or an asserted whole-campaign genome.
- Structured analysis target: existing `PLAT-DREAMCAST`, original English base game. Other platforms and editions remain unaudited; the authorised Steam bundle is a labelled later product link, not the analysed executable.
- Primary decision loop: physically reach available people and ask about the current lead; inspect and reuse automatically recorded information to locate the next eligible conversation or destination. The running town clock changes where people are and which businesses admit Ryo. Reach Heartbeats at night, respond to its two scripted button-prompt encounters, and obtain Charlie's identifying information as the successor lead.
- Entry and exit: enter at the first retained Free Quest control after Liu Sr's conversation has recorded the need to find sailors. End at the first retained free control after the two Heartbeats encounters and bartender's Charlie description produce the next inquiry, or abandonment. Include repeat inquiries, alternative ordinary speakers and spatial directions, waiting by ordinary passage of time, optional eligible bedroom sleep and missed/failed prompt recovery. This is a complete named investigative lead, not one dialogue or the campaign ending. Record original edition, date/hour, existing notes, Area Jump setting, conversations, admitted doors, cue responses and the successor notebook for reproduction.
- Included: direct walking/running and local held inspection; context-sensitive talk/door/read actions; autonomous townspeople and time-dependent presence/opening; authored fact acquisition and current-inquiry updates; a growing revisitable notebook, watch/calendar and local field affordances; two required QTE scenes outside and inside Heartbeats with finite displayed response windows, branch/recovery or scene retry after mistakes; eligible sleep advancing the day while investigation knowledge remains available. Nearby focus does not alter world geometry. Ordinary explicit pause is not frozen tactical orders.
- Excluded: the earlier black-car investigation; MJQ's optional single-shot billiards wager, paid Lapis fortune advice, arcade/gacha/darts, shopping and reward inventory, cat and relationship side scenes, move training and free-battle combat, Charlie's later tattoo-parlour encounter, harbor work, forklift/motorcycle/bus systems, campaign finale and postgame. The optional pool route is not a prerequisite for the Heartbeats packet. Neither fixed combat health nor a fatigue meter is inferred from QTE mistakes or bedtime wording. Shop names, hours, prompts and clue wording remain parameters.
- Exceptions and limits: the booklet describes a usual 23:30 bedroom return and sleep eligibility after 20:00, but original-Dreamcast secondary accounts explicitly report an extended-night exception while seeking Heartbeats. Its exact flag, cutoff and dependence on the optional MJQ clue were not tested; do not impose unconditional 23:30 failure on this packet. Failed QTE inputs can change the response or allow recovery; not every single mistake restarts the scene. Exact cue durations, calendar advancement during dialogue/QTE, failure persistence, collision geometry and full route timing remain unmeasured. No later-release wait/skip control is imported.
- Potential scoped modules: optional billiards and its wager require a separate complete minigame packet; free battle, move development and forklift work have distinct rules. Native play could establish the clock/pause policy, extended-night gate and exact QTE failure/retry branches without changing earlier source-supported boundaries implicitly.
- Direct-play status: no original Dreamcast disc, executable, VMU save, emulator, gameplay image/video/audio or input trace was executed or inspected. Relevant original English booklet sections for time, notebook, Free Quest, focus, QTE and bedtime were read as HTML/OCR. Independent original-Dreamcast written routes and cue/failure sections were read; a secrets-guide section supports a night exception but does not prove its exact implementation. No source-code inspection, measured successful run or direct play is claimed. Artwork is an original possible conversation scene, not a screenshot or measured bar layout.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| SH-001 | Free Quest permits direct walking/running, local held inspection and context-sensitive actions when the addressed person or fixture is eligible. | Observation | Corroborated | High | P1 pp. 12–19; S1/S2 route |
| SH-002 | Ordinary town time passes independently of movement commands; people have daily activities and bars have opening hours, constraining inquiry access. | Observation | Corroborated | High | P1 pp. 10–11; S2 sailors route |
| SH-003 | Authored conversations register learned people/places and current inquiries in the automatically updated notebook; relevant information can be reviewed later. | Observation | Corroborated | High | P1 pp. 10–11; S2 notebook leads |
| SH-004 | The sailors inquiry can use ordinary town speakers and Bar Yokosuka to discover bars; Heartbeats is physically reached by its alley stairs. MJQ billiards is an optional information route, not required completion. | Observation | Corroborated | Medium | S1/S2 sailors route; S3 original route |
| SH-005 | Alley and bar encounters display individual temporary commands during scripted action. The normal successful sequences are B,A and B,A,B,A, but an isolated miss may permit recovery or a changed cue; severe failure allows scene retry. | Observation | Corroborated | Medium | P1 pp. 22–23; S2 QTE 3/4; S3 Heartbeats |
| SH-006 | Completed Heartbeats encounters lead to the bartender's Charlie description and successor inquiry in the notebook, not victory over the whole investigation. | Observation | Corroborated | High | S1/S2/S3 sailors-to-Charlie route |
| SH-007 | Eligible bedroom sleep ends the current day and advances to the next, with the existing investigation available; the usual night return is not universal during the Heartbeats search. | Observation | Corroborated | Medium | P1 pp. 10–11, 29; S4 Staying Up Beyond The Curfew |
| SH-008 | Local view/context feedback, the notebook, watch/calendar and temporary QTE cues disclose different decision-relevant information without revealing every future schedule or lead. | Observation | Corroborated | Medium | P1 pp. 10–23; S1 menus; S2 notes |

## Basic data

- Release / origin: Sega AM2's original Dreamcast Shenmue; this packet uses the English 2000 base edition rather than the original Japanese 1999 dialogue or a remaster. Exact release day is not needed for the mechanical boundary.
- Platform or physical form: original Dreamcast single-player base game; existing platform identity, no claim that every release is reviewed.
- Mechanical families: `FAM-010` live system pressure, `FAM-012` authored fact reuse and `FAM-017` ordered dependencies. Availability changes with time, inquiry notes guide further visits, and the Heartbeats encounters precede the retained next lead.
- Sources accessed 2026-10-02:
  - **P1:** [Original Sega English instruction booklet, HTML/OCR reproduction](https://manualzz.com/doc/25127091/sega-shenmue-video-game-instruction-manual), relevant pp. 9–23 and 29 read, including Area Jump, world time, notebook, local focus, QTE and sleep. The mirror is not an independent second rule source; no native program is claimed from OCR.
  - **S1:** [AmericanArsenal original-Dreamcast guide](https://gamefaqs.gamespot.com/dreamcast/198621-shenmue/faqs/25805), sailors and successor route read; town-speaker alternatives and normal QTE inputs support the bounded lead. Its optional MJQ failure wording is not treated as a settled reward rule.
  - **S2:** [Adrenaline_SL original-Dreamcast guide](https://gamefaqs.gamespot.com/dreamcast/198621-shenmue/faqs/18346), sailors/Charlie and QTE 3/4 sections read. Notebook entries and retry tolerance are written player observations, not executable measurements.
  - **S3:** [SOng original-Dreamcast guide](https://gamefaqs.gamespot.com/dreamcast/198621-shenmue/faqs/6804), Heartbeats route and failure comments read. Its chair-hit/repeated-cue account supports recovery versus restart; exact timing and every branch remain untested.
  - **S4:** [JMcKenzie original-Dreamcast secrets guide](https://gamefaqs.gamespot.com/dreamcast/198621-shenmue/faqs/15626), section 10 read. It reports an extended-night Heartbeats exception; its unrestricted wording does not establish a precise final cutoff. Later forum descriptions suggest 04:00 and possible MJQ prerequisites, so this unit leaves both unresolved rather than adding an exact deadline.
  - **P2:** [Authorised Shenmue I & II Steam page](https://store.steampowered.com/app/758330/Shenmue_I__II/), later product link only, explicitly not rules evidence for the original disc or direct play.
- Claim IDs: `SH-001`–`SH-008`. No copyright screenshot, native trace or measured timing is imported.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for physically controlled navigation; `ACT-107` for acquired operational facts, not a dialogue stance or proof-selection game; `ACT-341` for reachable contextual door/sign interactions.
- `ACT-597` transfers its held-local-look clause unchanged: nearby inspection returns to ordinary following view and never changes geometry. First-person zoom is a view parameter, not a new world-transforming camera mechanic.
- `ACT-649` responds to the currently displayed temporary scene command, not a prior memory sequence, moving-pointer overlap or a player-chosen turn-based attack. `ACT-650` requests eligible next-day sleep without asserting a personal fatigue resource. `SH-001`, `SH-003`, `SH-005`, `SH-007`.

### System Behaviour Genes

- Reuse `SYS-045` for autonomous local people movement; do not import guard perception or hostile pursuit.
- `SYS-1279` updates people/service availability by the town clock; `SYS-1280` registers authored inquiry responses and changes later investigation topics without truth-versus-lie proof evaluation.
- `SYS-1281` resolves the active scripted cue into progress, recovery/branch or retry instead of free-battle damage. `SYS-1282` settles an eligible day ending into the next date with existing inquiry knowledge, not a newly generated town or a universal 23:30 terminal defeat. `SH-002`, `SH-003`, `SH-005`, `SH-007`.

### Constraint Genes

- `CON-751` restricts a requested conversation/service by current local presence and opening-time eligibility. It does not declare every notebook fact a necessary flag for physically finding Heartbeats or assert a universal curfew cutoff. Scripted cue identity/window belongs to `ACT-649` and its `SYS-1281` settlement, not one constraint per button. `SH-002`, `SH-004`, `SH-005`.

### Information Genes

- Reuse `INF-179` for local people/fixtures/exits, `INF-372` for the currently available contextual action, `INF-393` for the registered investigation notebook and `INF-142` for action animation/temporary prompts that cue reactive timing. This notebook does not manufacture L.A. Noire's physical-clue roster or interview judgement.
- `INF-461` exposes current clock/date for planning time-dependent visits, not an exact future routine list or campaign-deadline countdown. Information disclosure is separate from committing a prompted input or applying the learned lead. `SH-001`–`SH-008`.

### Objective Genes

- `OBJ-274` settles the named inquiry into a retained named successor after its required local interactions and scripted encounters. Unlike `OBJ-158`, physical QTE resolution is required; unlike a solved murder or campaign ending, Charlie's identity is a new question. `SH-004`–`SH-006`.

### Time Genes

- Reuse `TIM-003` for unpaused town progression and the finite live cue window. The booklet's explicit pause does not turn the running world into a move-only simulation or grant a remaster wait/skip control. Dialogue/QTE calendar scheduling remains unmeasured. `SH-002`, `SH-005`, `SH-007`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Liu Sr exchange has recorded sailors inquiry | Ask a currently available ordinary town speaker | Authored response can disclose bars or directions; accepted note remains inspectable | Learned operational lead, not a carried key | SH-003, SH-004 |
| Relevant bar is closed | Arrive and request entry before its opening | Current time gate prevents that service | Arrival alone does not ensure an eligible conversation | SH-002 |
| Bar Yokosuka is open and inquiry is current | Complete its relevant exchange | Other bar destinations become usable investigation information | Topic progression, not credibility adjudication | SH-003, SH-004 |
| Nearby reachable person or fixture | Inspect/address and use the offered action | Talk/open/read operates on that eligible target | Local contextual reach, not remote automatic travel | SH-001 |
| Notebook contains a registered address or person | Reopen the notebook | Previously registered information is available for the next visit | No omniscient future lead | SH-003, SH-008 |
| Eligible night access and alley reached | Approach Heartbeats | First scripted encounter presents its temporary button cues | Spatial/time access precedes prompted resolution | SH-004, SH-005 |
| Current QTE icon is visible | Press its indicated command before expiry | Authored response advances along an eligible success/recovery branch | Identity and time matter together; not pointer overlap | SH-005 |
| Prompt is missed or wrong | Continue the authored scene | A recoverable miss can change the response; a severe failure retries the scene | One mistake is not universally terminal | SH-005 |
| Alley scene cleared and bar entered | Complete the inside scene | Bartender supplies Charlie description and successor inquiry | Required encounters connect inquiry to retained next lead | SH-005, SH-006 |
| Sleep is eligible in Ryo's bedroom | Choose Sleep | Current day ends, date advances and existing investigation remains available | No fatigue-meter prerequisite or whole-world knowledge reset | SH-007 |
| Heartbeats investigation still active late at night | Continue eligible investigation | Written original accounts report an extended-night exception | Usual 23:30 return cannot be imposed universally; exact gate untested | SH-007 |

## Strategic and experiential structure

Choose whom to ask and whether to revisit a known address now or wait for its opening. The notebook reduces memory burden, but does not automatically transport Ryo or disclose everyone's future location. A physical route through town and the alley must meet current access conditions. During a required QTE, inquiry deliberation gives way to rapid identity/timing response; recoverable misses are different from a universally perfect sequence requirement. These are supported decision structures, not a measured optimal route or simulated routine table. `SH-001`–`SH-008`.

## Replay and variation

Different visit order, waiting and repeated questions can reach the same next inquiry. The packet does not establish random lead generation, time-travel resets, exact native-save retention or a new objective per conversation. Optional minigames and later free battles are separate excluded modules, not missing copies of the scoped QTE combat.

## Adjacent systems and history

The original booklet distinguishes Free Quest, Quick Timer Events and Free Battle. This lead connects the first two without treating the third as automatically admitted. Original Dreamcast rules are separated from later-product marketing and later wait/skip facilities; numerical corpus neighbours do not establish historical influence.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-107`, `ACT-341`, `ACT-597`, `ACT-649`, `ACT-650` | physical traversal, inquiry, doors/signs, held view, temporary scene response, eligible sleep |
| System Behaviour | `SYS-045`, `SYS-1279`–`SYS-1282` | autonomous people, availability, inquiry notes, cue branches/retry, next day |
| Constraint | `CON-751` | local presence and service hours |
| Information | `INF-142`, `INF-179`, `INF-372`, `INF-393`, `INF-461` | reactive prompts, local view, context action, registered notes, clock/date |
| Objective | `OBJ-274` | retained next investigative subject after required encounters |
| Time | `TIM-003` | independent unpaused town time and finite cue windows |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `484` (`GAME-0001`–`GAME-0484`).
- Exact genome matches: none.
- Tied near matches: `GAME-0395` — The Legend of Zelda: Majora’s Mask (`5 / 30 = 0.166667`).
- Supported combination subsets: none.
- Scan date: 2026-10-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0395` The Legend of Zelda: Majora’s Mask | `ACT-008`, `ACT-107`, `ACT-341`, `INF-179`, `TIM-003`: direct town traversal, learned actionable facts, local fixtures/view and independent running time. | The original N64 first cycle requires a learned code, magic, item exchange, scheduled tower access and a deliberately submitted Song of Time before terminal moonfall, retaining the Ocarina across a selective reset. Shenmue's named lead instead uses clocked ordinary conversations and retained notes followed by two temporary-cue scenes; its extended-night exception is unresolved and eligible sleep continues the investigation rather than resetting the world. Shared facts/time do not transfer the Ocarina, exact expiry or dialogue clock-pause policy. | Near; `5 / 30 = 0.166667`. Shared rule boundaries are not whole-game identity or historical lineage. |

## Taxonomy impact

`TAXONOMY_CHANGE_222` admits nine bounded additions and ten unchanged reuses. A named causal-role review covers all nineteen uses. No earlier canonical definition, signature, verified combination or platform identity changes.

## Negative results

- Reject compulsory MJQ billiards, universal 23:30 expiry, fatigue-meter sleep, free-battle damage and every-single-miss restart. Conflicting optional-pool reward descriptions and night-cutoff accounts are not silently settled.
- Reject prior-sequence memorisation, moving-pointer timing, turn-command modifiers, interview credibility proof and world-transforming camera rotation as transfers to the present controls.
- Reject importing Shenmue II or 2018 wait controls, exact native clock rate, QTE calendar/failure persistence and undisclosed platform parity.

## Delta summary

## New facts

- [Observation | Corroborated | Medium] Clocked town access and retained inquiry notes connect physical visits to two scripted encounters and a named successor lead. Isolated QTE misses can be recoverable. `SH-001`–`SH-008`.

## New genes

- [Observation | Corroborated | Medium] Nine bounded additions capture time-dependent service access, retained inquiry/day transitions and authored temporary-command resolution; concrete addresses, buttons and hours remain parameters.

## New combinations

- [Observation | Limited | Medium] No new verified combination; every existing proper subset is recomputed from the admitted signature.

## Taxonomy changes

- [Observation | Direct | Medium] `TAXONOMY_CHANGE_222`; no earlier definition or signature mutation.

## New questions

- Measure the original extended-night flag/cutoff, dialogue/QTE clock scheduling, cue/retry branches and native save retention in lawful direct play before strengthening these limited claims.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0486` *Final Fantasy Tactics*, original PlayStation, follows complete acceptance and the Goal stop window and closes the approved batch.
- Optimisation criterion: change platform and decision structure from situated clocked inquiry to discrete tactical party combat.

## Why this game

- [Hypothesis | Limited | Medium] The approved cross-platform batch includes Dreamcast's authored town investigation, complementing the previous C64 deadline/fragment mission without claiming experience from a genre label.
