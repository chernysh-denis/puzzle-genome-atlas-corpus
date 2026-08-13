# Gene Registry

A **gene** is the smallest decision-relevant mechanical component that the
knowledge base can currently distinguish and reuse across puzzle analyses.
The canonical distinctions between a gene, parameter, genome, signature and
combination are defined in
[`docs/ARCHITECTURE.md`](../../docs/ARCHITECTURE.md#canonical-vocabulary).

A word is not a gene merely because it sounds mechanical. Every active gene
requires:

1. a stable type-specific ID;
2. a canonical name;
3. an operational definition;
4. inclusion and exclusion boundaries;
5. evidence and at least one analysed example;
6. lifecycle, claim-status, evidence-quality and confidence fields.

## Gene types

| Prefix | Type | Question answered |
|---|---|---|
| `ACT` | Action Gene | What does the player directly command? |
| `SYS` | System Behaviour Gene | What state transition resolves automatically? |
| `CON` | Constraint Gene | What limits legal or useful action? |
| `INF` | Information Gene | What can the player know, and when? |
| `OBJ` | Objective Gene | What state or measurement is pursued? |
| `TIM` | Time Gene | How are actions and resolution scheduled? |

These six types are the current model, not a protected truth. A seventh type may
be proposed only when repeated evidence cannot be represented without systematic
distortion. Use the taxonomy-change process; do not create an ad hoc category in
a game file.

Parameters refine a gene instance and never receive stable IDs. They remain
outside the genome signature. A recurring parameter difference that makes the
gene boundary misleading must be handled through a taxonomy change, not an
ad hoc comparison exception.

## Cross-type boundary tests

The eight-game checkpoint established these operational tests. Apply them
before admitting a new gene:

| Boundary | Classification test |
|---|---|
| Action / System Behaviour | A directly selected command is an Action; a state transition that occurs without a second player command is System Behaviour. |
| System Behaviour / Constraint | Automatic mutation or movement is System Behaviour; a legality, continuation, terminal or reachability predicate is a Constraint when it only classifies a state or attempted action. |
| Information / Constraint | What an instance discloses and when is Information; the condition that a legal or complete assignment must satisfy is a Constraint. The same clue may support one gene of each type only when these roles are independently defined. |
| Constraint / Objective | A Constraint filters legal or useful states; an Objective identifies the state or measurement the player pursues. A failure boundary does not become an Objective merely because players avoid it. |
| System Behaviour / Time | System Behaviour states what transition occurs; Time states when player input and automatic resolution may occur relative to one another. |
| Information / System Behaviour | Disclosure of a committed or scheduled future transition is Information; the transition that later mutates state is System Behaviour. Preview and execution may therefore coexist without being duplicate genes. |
| Gene / parameter | A stable decision rule is a gene; board size, count, magnitude, topology or threshold remains a parameter unless repeated evidence shows that the existing boundary hides a different decision structure. |

Empty type sets are valid. A puzzle with no automatic in-play transition must
not receive a System Behaviour gene merely to make its signature symmetrical.

## Registries

- [Action Genes](actions.md)
- [System Behaviour Genes](system-behaviours.md)
- [Constraint Genes](constraints.md)
- [Information Genes](information.md)
- [Objective Genes](objectives.md)
- [Time Genes](time.md)
- [Candidate terms inherited from the original taxonomy](CANDIDATE_TERMS.md)

## Lifecycle

- `Active` — accepted for genome encoding.
- `Deprecated` — retained for compatibility but replaced.
- `Merged` — found to be synonymous with another gene.
- `Split` — found to contain multiple decision-relevant genes.

Lifecycle is separate from claim status. `Active` means usable in the registry;
it does not mean novel or universally valid. Candidate terms have no stable ID
and remain vocabulary rather than gene records.
