---
game_id: GAME-0523
slug: pentiment
game_title: Pentiment
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-107
    - ACT-232
    - ACT-341
    - ACT-650
  system:
    - SYS-680
    - SYS-783
    - SYS-804
    - SYS-1282
    - SYS-1499
    - SYS-1500
  constraint:
    - CON-802
  information:
    - INF-148
    - INF-393
    - INF-506
  objective:
    - OBJ-295
  time:
    - TIM-002
---

# Game: Pentiment

## Analysis scope

- Version / ruleset: English Xbox Series X|S single-player base game under the
  15 November 2022 release-era rules. The exact installed build and subsequent
  port parity are unverified. Xbox release and design evidence anchor the target;
  a later PS5 written route supplies explicitly attributed branch detail.
- Structured analysis target: `PLAT-XBOX-SERIES`, base game's Act I inquiry.
- Primary decision loop: visit an eligible person or fixture during the current
  named hour. Learn or inspect what is freely available before spending a work
  period on one substantial inquiry or spending a meal on one host. Carry
  learned facts and consequential responses forward as further questions become
  available. At the appointed hearing, choose which grounded suspicions to
  disclose to Jacob and which to withhold, then observe his chosen verdict.
- Entry and exit: in a fresh English story start with Piero accused after
  Andreas's discovery of Rothvogel's body in the Chapter House. Earlier
  dialogue and background are already fixed; the Logician background supports
  the documented Ferenc branch. Spend the ensuing work and meal periods,
  preserve inquiry state across ordinary sleep, and reach the hearing at Nones
  on 24 April 1518. The endpoint is the disclosed judgement on the subsequent
  Day of Law and Judgement, before the June farewell or any Act II play.
- Included: local movement, clue inspection and dialogue, the investigation
  journal, phase and meal information, marked consequential responses, work
  and meal opportunities, overnight continuation, background-conditioned
  response options, named allegations and the delayed verdict. Ferenc and
  Matilda supply opposed, documented endpoints. Lucky and Ottilia supply
  route alternatives; this dossier does not exhaust every persuasion line.
- Excluded: the provisional prologue choices as actions, achievements,
  unrelated favour quests and minigame scoring, later cases, exact internal
  verdict weights or a claim of guilt proved by the verdict. The full volvelle
  puzzle and exact code path are separately bounded leads.
- Potential scoped modules: one full volvelle solution across background and
  external-knowledge routes; the Act II case with imported Act I choices.
- Direct-play status: no execution or media playback. Official release and
  director statements anchor Xbox and intent. A written Xbox route and a
  separately authored later PS5 route support the branch reconstruction.
  Exact version-specific flags, thresholds and every possible combination of
  disclosed evidence remain unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| `PEN-001` | Obsidian's released Xbox game begins this case with Andreas investigating a visitor's murder after his friend Piero is implicated. | Confirmed | Direct | High | P1, P2 |
| `PEN-002` | Routine walking, stops and local questions may fit within the current hour. Completing the chosen substantial investigation or meal advances the day to the next named phase. Meals offer different hosts and can disclose different facts. | Observation | Corroborated | High | P3, S1, S2, S3 |
| `PEN-003` | The journal exposes leads, the map marks available meal hosts, and the interaction can warn about spending time before commitment. Ordinary sleep carries inquiry state forward. | Observation | Corroborated | High | S1, S2, S3 |
| `PEN-004` | Existing background can open a marked answer. Separately, earlier remembered responses contribute to later persuasion, as when asking for access to Piero. | Observation | Corroborated | Medium | P4, S1, S2 |
| `PEN-005` | Ferenc's correspondence, examination of the body and buried objects support different propositions. The written route permits the grave search via Gernot's consent with qualifying evidence and a suitable background. | Observation | Corroborated | Medium | S1, S3 |
| `PEN-006` | Examining the marked shovel and learning of Matilda's assault provide distinct topics at the hearing. Matilda supplies an innocent use for the shovel. | Observation | Corroborated | Medium | S1, S2, S3 |
| `PEN-007` | Jacob's hearing accepts multiple named leads and evidence-bearing responses. The reported verdict can differ between the Ferenc and Matilda disclosures and is announced after the hearing. The player cannot directly select a verdict. | Observation | Corroborated | High | P2, P3, P4, S1, S3 |
| `PEN-008` | The meaningful limit is the calendar and the evidence it prevents Andreas from collecting. A verdict settles the case for the town while the available evidence leaves actual guilt uncertain. | Strong Pattern | Corroborated | High | P2, P3, S1, S2, S3 |

## Basic data

- Release / origin: Obsidian Entertainment; Xbox Game Studios;
  15 November 2022 on the declared console family.
- Platform or physical form: native single-player Xbox Series X|S release.
- Puzzle family: knowledge and evidence progression (`FAM-012`).
- Primary sources:
  - P1. [Xbox release announcement](https://news.xbox.com/en-us/2022/08/24/pentiment-releasing-on-november-15/)
    and [Obsidian product announcement](https://www.obsidian.net/news/obsidian/obsidian-entertainment-announces-pentiment).
  - P2. [Director Josh Sawyer, Xbox Wire interview transcript](https://news.xbox.com/en-us/podcast/pentiment-herman-miller-gaming/).
  - P3. [Sawyer on limited investigation time and conviction](https://www.mmorpg.com/interviews/the-rpg-files-building-obsidians-pentiment-interview-with-game-director-josh-sawyer-2000126821).
  - P4. [Sawyer on backgrounds and differing convictions](https://www.trueachievements.com/n51803/pentiment-interview).
- Secondary sources:
  - S1. Written Xbox routes for [Act I first half](https://www.trueachievements.com/game/Pentiment/walkthrough/3),
    [second half](https://www.trueachievements.com/game/Pentiment/walkthrough/4)
    and [alternate route](https://www.trueachievements.com/game/Pentiment/walkthrough/11).
  - S2. [Neoseeker Act I written walkthrough](https://www.neoseeker.com/pentiment/walkthrough/Act_I).
  - S3. Chris Williams's written guide to the
    [clock and conversations](https://gamefaqs.gamespot.com/ps5/450806-pentiment/faqs/82597),
    [Ferenc route](https://gamefaqs.gamespot.com/ps5/450806-pentiment/faqs/82597/the-baron-april-1518)
    and [Matilda route](https://gamefaqs.gamespot.com/ps5/450806-pentiment/faqs/82597/good-graces-act-1-reprise).
    The 2026 PS5 guide corroborates the shared mechanics and identifies the
    route cases; it does not independently establish Xbox launch-build details.
- Claim IDs: `PEN-001`–`PEN-008`.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: `ACT-008` move Andreas between accessible rooms;
  `ACT-107` acquire an actionable fact from a witness; `ACT-232` choose
  an offered reply, host or allegation; `ACT-341` examine an eligible
  physical clue; `ACT-650` use eligible bedroom sleep to close the day.
- Parameters: reachable location, current interlocutor, offered reply, fact,
  inspected fixture, ordinary sleeping place.
- Claim IDs: `PEN-002`–`PEN-007`.

### System Behaviour Genes

- Existing gene IDs: `SYS-680` turn related inspections into a concrete
  branch lead; `SYS-783` expose evidence-backed options at the hearing;
  `SYS-804` advance the clock through qualifying events with free travel and
  idle time; `SYS-1282` advance the day with prior leads retained.
- New genes: `SYS-1499` remembers consequential replies and evaluates
  their aggregate for later permission; `SYS-1500` commits one delayed
  official verdict from disclosed evidence and accusations.
- Resolution order: phase-appropriate opportunity, choice, event completion,
  clock or knowledge-state update; on the appointed day, hearing dialogue
  records the offered case, and a later scene reveals the verdict.
- Parameters: affair, input evidence flags, available responses, earlier
  remembered replies, authority and output branch. Numerical weights are not
  claimed.
- Claim IDs: `PEN-002`–`PEN-008`.

### Constraint Genes

- New gene: `CON-802` partitions eligible progress into authored phase
  offers. A phase-spending commitment excludes all other current
  opportunities that also spend that phase.
- Scarce strategic resources: work periods before the hearing and meals
  whose host determines the available conversation. Free movement and
  inspections do not by themselves reduce this supply.
- Claim IDs: `PEN-002`, `PEN-003`, `PEN-008`.

### Information Genes

- Existing gene IDs: `INF-148` mark contextual reply gates and
  `INF-393` expose growing inquiry leads in the journal.
- New gene: `INF-506` disclose the current calendar phase and warn before
  an offered activity spends it.
- Claim IDs: `PEN-002`–`PEN-004`, `PEN-007`.

### Objective Genes

- New gene: `OBJ-295` complete the bounded case by bringing a viable
  alternative to the authority, then reach its pronounced judgement.
- Success, evaluation and failure: the documented outcomes convict an
  alternative suspect and spare Piero. Missing a lead can weaken the case but
  does not introduce an independently confirmed game-over state. Judgement is
  the measured endpoint, with guilt still unresolved.
- Claim IDs: `PEN-001`, `PEN-007`, `PEN-008`.

### Time Genes

- Existing gene ID: `TIM-002`. Waiting before a decision does not expend an
  investigation period. The named calendar jumps on eligible completion.
- Claim IDs: `PEN-002`, `PEN-003`, `PEN-008`.

## Reproducible transitions

| Before | Action | Observed or source-reported resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Free movement before a work commitment | Traverse between eligible sites and read the letter in the Guest House | Letter knowledge is available without settling the following meal or work period | Learning a local fact can cost no period | `PEN-002`, `PEN-005` |
| One eligible work period | Complete the examination with Brother Florian | Circumstances of the wound and the note become inspectable evidence, and the next meal phase becomes current | Examination is a time-spending inquiry at this branch | `PEN-002`, `PEN-005` |
| Multiple eligible hosts at Vespers | Join the Steinauers and complete the meal conversation | The host determines the exchange and the completed meal advances to Compline | A competing host cannot be visited for a second dinner in that phase | `PEN-002`, `PEN-003` |
| Compline in the Gertner lodging | Use the bedroom's eligible sleep interaction | The next day or authored intervening night scene begins with inquiry history retained | The calendar can advance without resetting the case | `PEN-003` |
| Clue route points to Gerhard's grave | Use the source-reported Logician dialogue with the abbot after the body inspection and obtain help | Gernot may authorise the opening and a subsequent work commitment reveals the buried objects | Earlier inquiry and build can open permission to perform a different action | `PEN-004`, `PEN-005` |
| Matilda lead and shovel are accessible | Inspect the shovel and question the nun and prioress | Shovel and motive become separately reportable. The shovel also has a competing explanation | Seeing one object does not settle its role | `PEN-006` |
| Jacob asks for grounds to suspect someone other than Piero | State Matilda's motive and mention the shovel, withholding the documented Ferenc material in this branch | Matilda is announced as the convicted person on the later judgement day in the written route | A hearing strategy affects the branch and does not prove actual guilt | `PEN-006`, `PEN-007` |
| Ferenc's correspondence known | Tell Jacob about the ritual request, present the letter and conclude as in the documented route | The later scene announces Ferenc's conviction even though this route supplies no grave evidence | A witness can submit the letter without having pursued every source of support | `PEN-005`, `PEN-007` |

## Strategic and experiential structure

- Local decision: inspect or ask around before committing the expiring slot.
- Medium-term planning: reserve a work period for a costly informative action,
  and use the right meal to ask about a different lead.
- Long-term structure: choose which acquired information to give the official
  before the judgement cut. Evidence can be investigated and then withheld.
- Failure attribution: Warnings and named hours help explain missed leads.
  The official's evaluation remains partially opaque; finding an object can
  support more than one plausible account.
- Claim IDs: `PEN-002`–`PEN-008`.

## Replay and variation

- A new route can change the imported background, meal partners and costly
  inquiries, then submit different selected allegations.
- The bounded outcome variation is authored. The evidence does not establish
  a random verdict draw, a full accusation ranking or universal thresholds.
- Claim IDs: `PEN-004`–`PEN-008`.

## Adjacent systems and history

- Disco Elysium - The Final Cut shares the interaction-driven clock and
  actionable conversations. Its bounded episode tests attribute checks and
  surviving resource pools on the path to a partner encounter.
- Detroit: Become Human also registers clues as conversation advantage, but
  its opening settles a live confrontation through immediate intervention.
  Pentiment ends the investigation at an official hearing and discloses the
  consequence later.
- L.A. Noire's notebook supports presenting the matching contradiction to
  a witness. Pentiment lets Andreas disclose circumstantial support to an
  authority whose final judgement need not follow a single item.
- Claim IDs: `PEN-002`, `PEN-004`, `PEN-007`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-008`, `ACT-107`, `ACT-232`, `ACT-341`, `ACT-650` | current target, fact, response, or bed |
| System Behaviour | `SYS-680`, `SYS-783`, `SYS-804`, `SYS-1282`, `SYS-1499`, `SYS-1500` | period, remembered choices, offered evidence and verdict |
| Constraint | `CON-802` | named phase and its offers |
| Information | `INF-148`, `INF-393`, `INF-506` | journal, reply gates and spending warning |
| Objective | `OBJ-295` | case, protected person, authority, terminal |
| Time | `TIM-002` | pace of deliberation and date |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `522` (`GAME-0001`–`GAME-0522`).
- Exact genome matches: none.
- Tied near matches: `GAME-0388` — L.A. Noire (`6 / 24 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0388` — L.A. Noire | `ACT-008`, `ACT-232`, `ACT-341`, `SYS-680`, `INF-393`, `TIM-002` | Both permit moving, inspecting evidence, choosing responses and retaining leads at the player’s pace. L.A. Noire evaluates witness contradiction and advances toward apprehension. Pentiment spends calendar phases and submits a selective account to an authority that declares the verdict later. | Tied near (`0.250000`) |

### Preserved research notes

- New genes: `SYS-1499`, `SYS-1500`, `CON-802`, `INF-506`, `OBJ-295`.
- Classification result: `New gene`.
- Evidence and reasoning: voluntary phase commitment, remembered dialogue,
  evidence-bearing response and delayed judgement have separate observable
  boundaries.

## Taxonomy impact

- Registry changes: five Active definitions; twelve existing boundaries reused.
- Taxonomy-change record: [TAXONOMY_CHANGE_270](../../../research/taxonomy-changes/TAXONOMY_CHANGE_270.md).
- Candidate terms affected: canonical hours, remembered responses, hearing and
  conviction; names of food, people, tools and hours are parameters.

## Negative results

- None.

## Delta summary

## New facts

- [Observation | Corroborated | High] The hearing ends time allocation before
  a later scene announces a verdict from the submitted case (`PEN-007`).

## New genes

- [Observation | Corroborated | High] `SYS-1499`, `SYS-1500`, `CON-802`,
  `INF-506` and `OBJ-295`.

## New combinations

- [Observation | Corroborated | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_270`.

## New questions

- Which Act II permission checks read Act I disclosure independently of the
  identity of the convicted person?

## Next recommended game

- [Hypothesis | Limited | Medium] Wave Race 64, original Nintendo 64.
- Optimisation criterion: contrast a time budget spent voluntarily with a live
  action course in which moving water and gated buoy order affect progress.
- Expected information gain: clean differentiation of steering geometry,
  buoy legality and power changes.
- Backlog impact: advance Selection 041 to its second candidate.

## Why this game

- [Hypothesis | Limited | Medium] The difference between a licensed verdict
  and a proven answer tests whether investigation should be compared by
  information collection alone or by how an authority uses the disclosed facts.
