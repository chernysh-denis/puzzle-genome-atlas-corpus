---
game_id: GAME-0628
slug: keep-driving
game_title: "Keep Driving"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-835
  system:
    - SYS-736
    - SYS-1829
  constraint: []
  information:
    - INF-268
    - INF-583
  objective:
    - OBJ-337
  time:
    - TIM-044
---

# Game: Keep Driving

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
It bounds one taught road event to its observed return to ordinary travel.

## Analysis scope

- Version / ruleset: English commercial Windows release on Steam, app
  2756920, first released on February 6, 2025. Use the launch-period
  February 2025 opening with a fresh trip, the 1981 Sedan and its first
  Tractor tutorial. Exact installed build and input timings are unknown.
- Primary decision loop: read the indicated harms and available skills,
  align a skill with the threat row, use the extra action when earned,
  settle the unresolved warned threats and repeat until ordinary travel
  resumes.
- Entry: the sedan is already on the initial road when the Tractor title
  interrupts the ordinary itinerary view and exposes the threat strip.
- Exit: the first tractor event reports defeat and the ordinary itinerary
  returns. The sedan continues along the road without the tractor in front.
  The next event and arrival at a destination are outside the packet.
- Included: the ordered threat strip, marked pending losses, skill symbols
  and alignment, per-skill uses and displayed activation costs, the taught
  Perfect Hit and its one extra turn, Road Phase and resumed travel.
- Excluded: later events, alternate setups, repairs and supplies outside the
  road event, rewards, route optimisation, failure at an empty resource,
  a specific game-wide encounter generator, mods, console releases and
  later patches that changed the opening.
- Suggested later scope: reproduce the same tutorial on a recorded current
  Windows build and check its revised phase prompts.

## Direct-play status

No direct play was performed. Steam establishes the commercial Windows
edition and its turn-based road encounters. Static frames from a
February Windows opening show the tutorial instructions, actual symbol
removal, the extra turn, the encounter result and continued travel.
A second February opening explicitly identifies PC Steam and independently
shows the staged Tractor event, Road Phase and resumed travel. No audio
was played or inspected. The precise executable build, exact loss
amounts for each threat, full table of special warnings and zero-resource
outcomes were not established.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| KD-001 | The Windows Steam game was released February 6, 2025 and has turn-based road events. The 1981 Sedan enters a guided Tractor event during the initial drive in the February recordings. | Confirmed | Corroborated | High | P1. W1 2:00–4:30 and W2 10:50–11:50. No executable build is inferred. |
| KD-002 | The event shows an ordered row of typed threats against energy, cash or car durability. Signs over icons identify attacks due in the Road Phase. Skill cards show available uses, pattern and any activation cost. | Observation | Corroborated | High | W1 4:20–5:05 and 5:37–5:43, W2 11:45–13:35 and P1. |
| KD-003 | The player drags a skill to align its pattern with the row. Matching symbols clear the aligned threats, a star matches any type, and X is a gap with no removal. The taught Relax placement covers energy, leaves the intervening durability icon and clears cash. Have a Go shows one Energy as its cost. | Observation | Corroborated | High | W1 4:49–5:26, 5:37–5:55 and 7:54–8:00 and W2 13:15–14:30. |
| KD-004 | The guided accurate placement is acknowledged as Perfect Hit and grants one extra action. A second Perfect Hit during that extra turn does not grant another in the same player phase. | Observation | Corroborated | High | W1 5:23–5:33 and 5:54–6:08 and W2 13:50–15:36. |
| KD-005 | The Road Phase can apply the unresolved marked threats to the corresponding resources, then return the encounter to the player while threats remain. The panels introduce one rule or requested action at a time and advance after the taught selection. | Observation | Corroborated | High | W1 6:06–7:40 and W2 15:20–17:20. Exact amounts and persistence of all types are outside the packet. |
| KD-006 | After the last threat goes, the Tractor event displays defeat. The road HUD returns with its distance and time display, and the sedan continues independently of the tractor. | Observation | Corroborated | High | W1 7:54–8:18, including defeat at about 8:01 and continued travel by 8:04. W2 18:20–18:55. |
| KD-007 | The developer subsequently reported a change to the first road tutorial. These February observations do not establish later tutorials or all possible initial variants. | Confirmed | Direct | High | P2, Build 1.2.0.0 patch note. |

## Basic data

- Analysis target: `PLAT-WINDOWS-PC`.
- Developer: YCJY Games. Publishers: YCJY Games and Kepler Ghost.
- Mechanical family: `FAM-009`, tactical forecasting and counterplay.
- Checked: 2026-11-21.
- P1: [Developer and publisher Steam product page](https://store.steampowered.com/app/2756920/Keep_Driving/),
  with Windows requirements, release date and road-event description.
- P2: [Official Steam release notes](https://steamcommunity.com/app/2756920/allnews/?l=english),
  Build 1.2.0.0's change to the first road tutorial. It is later than the
  launch-period trace used for the worked example.
- W1: [DEVA GAMING's February 9 commercial PC trace](https://www.youtube.com/watch?v=M6f6tqdFMKE&t=253s).
  The opening shows a Windows desktop overlay and the initial sedan.
  It records the precise worked alignment, extra turn and route return.
- W2: [Yeahunter's February 7 PC Steam recording](https://www.youtube.com/watch?v=2QGXwljBPF0&t=664s).
  The author identifies a publisher-supplied copy. The first event
  corroborates the instructions, Road Phase and continuation. It does not
  authenticate W1's executable or every choice.

## Mechanical decomposition

### Action Genes

- ACT-835: shift an available skill pattern against the ordered threat
  row and commit a placement. A wildcard removes any aligned threat.
  A gap preserves the slot beneath it.

### System Behaviour Genes

- SYS-736: the tutorial moves to the next authored instruction when
  the required action or state is reached.
- SYS-1829: marked, unresolved road threats affect the distinct resource
  indicated by each icon during the Road Phase.

### Constraint Genes

The displayed positive use stock and activation affordability belong to
the skill action. The extra-turn limit belongs to TIM-044.

### Information Genes

- INF-268: the tutorial progressively explains the current legal action
  and acknowledges it before exposing the next instruction.
- INF-583: compare the ordered threat types and warning signs with the
  skill pattern, remaining uses and resource cost before committing.

### Objective Genes

- OBJ-337: empty the active road event's threats and return to the on-road
  itinerary with the car continuing its trip.

### Time Genes

- TIM-044: a perfect use can earn one bonus turn in the player phase.
  A perfect use during that bonus turn cannot chain a further turn.

## Reproducible transitions

| State | Input or event | Result | Evidence |
| --- | --- | --- | --- |
| The chosen sedan is already travelling | Initial Tractor event arrives | The ordinary itinerary is replaced by the threat strip and the guided player phase | KD-001 |
| Relax is shown. The line contains two adjacent energy icons, then durability and cash | Drag its energy–gap–cash pattern over the second energy icon, durability and cash | The aligned energy and cash icons disappear. Durability remains under the gap. The taught hit is perfect | KD-002–KD-004 |
| The first perfect placement has earned Extra Turn | Apply the wildcard of Have a Go to one remaining threat | The one-Energy skill removes that threat. A second perfect placement does not renew the extra turn | KD-003, KD-004 |
| Threats carrying immediate warning marks remain | The Road Phase begins | The corresponding resources are at risk and the next Player Phase appears with unresolved threats | KD-005 |
| Later in the same event, two threats remain | Use Have a Go across the remaining threats on the next available actions | The last threat is cleared. Tractor defeat registers and ordinary travel resumes | KD-003, KD-004, KD-006 |

## Strategic and experiential structure

The virtual opponent is a row of projected expenses. One placement can
neutralise multiple resource types by positioning a fixed pattern, but
slides the entire pattern together. A skill that preserves an immediate
expense may drain energy itself. The player can use the warning marks to
prioritise the next loss, weigh a good fit against the remaining uses and
take one extra action for accurate alignment. Ordinary travel resumes
after the final threat, with no claim about a particular reward.

## Replay and variation

The two February Windows traces corroborate the phase sequence and return
to travel. The recordings do not establish deterministic geography, attack
amounts or identical choices. The second opening provides an independent
trace through the same guided situation. Later releases report changing
the first road tutorial and need separate verification.

## Adjacent systems and history

Steam describes choosing supplies, skills and routes over a generated
trip. This packet does not treat a map preview as proof of a reached
destination or infer a hazard selection algorithm from the authored
opening. Later items, services and other starting vehicles are available
questions for a different packet.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-835 | Place a charged skill pattern against the threat line |
| System Behaviour | SYS-736, SYS-1829 | Advance the lesson and settle warned resource threats |
| Constraint | None | Use stocks, affordability and bonus limits are owned by their corresponding rules |
| Information | INF-268, INF-583 | Read the current lesson and compare typed threats, warnings, patterns and costs |
| Objective | OBJ-337 | Empty the threats and return to travel |
| Time | TIM-044 | One perfect-hit bonus turn per player phase |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `627` (`GAME-0001`–`GAME-0627`).
- Exact genome matches: none.
- Tied near matches: `GAME-0358` — Psychonauts (`2 / 22 = 0.090909`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Psychonauts (GAME-0358)](../m-r/psychonauts.md) | INF-268, SYS-736 | The scoped Coach obstacle lesson likewise advances contextual instructions. It uses physical traversal over a training course. Keep Driving aligns typed threats, earns a capped bonus action and returns to automatic road travel. | Near, `0.090909` |

## Taxonomy impact

[TAXONOMY_CHANGE_374](../../../research/taxonomy-changes/TAXONOMY_CHANGE_374.md)
describes the reusable distinctions between placement, damage settlement,
information, local clearance and the extra turn.

## Negative results

- SYS-164 describes acting enemies whose telegraphed combat actions
  resolve in actor order. The unresolved threats here are typed resource
  markers, and the recording does not establish an actor-order scheduler.
- TIM-005 permits a set of commands in flexible order before ending a
  planning phase. In this packet a normal skill use earns another use only
  under the taught perfect-hit predicate.
- OBJ-029 describes incapacitating required combatants. Tractor defeat is
  registered by removing resource threats before returning to travel.
- A fuel gauge is visible. The tutorial identifies energy, cash and car
  durability as its shown threat categories, so the gauge alone does not
  establish a fourth rule for threat types.

## Delta summary

Adds the commercial Windows Steam road encounter from the tutorial Tractor
arrival through the confirmed return to ordinary travel.

## New facts

- One placement can remove different symbol types with a fixed gap.
- An immediate warning identifies the next typed resource loss.
- The player can earn one extra use before the Road Phase.
- The encounter ends on the empty threat row and the sedan continues.

## New genes

ACT-835, SYS-1829, INF-583, OBJ-337 and TIM-044.

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_374](../../../research/taxonomy-changes/TAXONOMY_CHANGE_374.md).

## New questions

Which warning, cost and recovery rules differ after the documented
first-tutorial revision?

## Next recommended game

Continue with the North American PlayStation 2 release of Dark Cloud
through its first evidenced dungeon and Georama restoration cycle.

## Why this game

A road problem turns loss prevention into an ordered pattern decision.
The first tractor gives observable evidence of both resource pressure
and the consequence of a match before automatic travel resumes.
