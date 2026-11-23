# Taxonomy Change 297 — Throttle-return drift and individual-cut qualifying heat

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: High
- Date: 2026-11-19.
- Trigger: [GAME-0551](../../knowledge/games/m-r/ridge-racer-type-4.md),
  original North American PlayStation first complete qualifying heat.

| Addition | Reviewed boundary | Counterexample |
| --- | --- | --- |
| `SYS-1595` | Steer with released throttle, reapply it to resolve the prepared tail slide, then settle the exit. Longer released-throttle steering increases the documented slide strength. | `SYS-320` supplies ordinary motion/contact but does not state this input-sequence-dependent handling branch. `ACT-468` and `SYS-892` require a held drift charge and tiered release boost. No new action is needed for R4's ordinary steering/throttle inputs. |
| `SYS-1596` | Classified stage performance chooses the supplied machine variant or old-car tune for the next stage. Garage registration is still unavailable. | `SYS-519` transfers declared driving rewards into retained campaign/garage state; it does not choose a conditional stage machine or its tune. `SYS-822` records a grade rather than assigning driving capability, and a successful cut does not promise the best machine. |
| `CON-818` | Every immediate successor requires the preceding race's own place/time cut. | A cumulative Cup can compensate for a low finish; a shared progression pool can substitute other activities. Valid lap classification alone does not certify qualification. |
| `OBJ-304` | Complete the whole first qualifying heat and accept its successor assignment. | `OBJ-150` covers one race, `OBJ-226` one first-place points result, `OBJ-146` a retained cross-country rank and `OBJ-180` a cumulative Cup trophy. None is the complete individual-cut heat. |

Fifteen unchanged definitions cover supplied setup, direct control, viewpoint,
vehicle contact, configured rivals, lap classification, race-origin retry,
finite continuation chances, deadline, information and live timing.
`CON-183` admits an abstract encounter-chance carrier; no new body-life rule
or native off-by-one counter convention is inferred. The stated four chances
are documentary wording, not a measured fifth-attempt entitlement.

No existing definition or signature is rewritten. There is no new recurring
combination, fitted slip equation, Mini-Turbo, fuel/damage economy, mandatory
first place in both races or exact all-car unlock formula. The named GAME-0551
salience review partitions the complete nineteen-gene scope without weights.
