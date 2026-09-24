# Taxonomy Change 130: bounded four-player board economy and minigame bridge

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Direct
- Confidence: High
- Date: 2026-09-24
- Trigger: `GAME-0392` Mario Party 2, original Nintendo 64 Pirate Land
  LITE PLAY 20-turn four-human NO BONUS Adventure Board contest.
- Scope: eight additive Active genes; no older genome, lifecycle, family
  definition or verified combination is changed.

## Problem and accepted change

An ordinary random outcome, a priced purchase and alternating turns do not
describe what this board does with the rolled movement, pass/land triggers,
four landing colors, Star-vendor relocation and its finite final ranking.
The changes are separated by operational boundary:

- `ACT-530` selects an outgoing junction edge while the current die count is
  still being spent; `SYS-1050` advances the token by that count.
- `SYS-1051` distinguishes fixture transactions made in transit from effects
  on the final occupied space. Pirate Land cannon, bank, shop and colored
  spaces are typed instances, not a gene for every art variant.
- `SYS-1052` turns all four final colors into a minigame format and settles
  its result into the next board Coin balance. It does not flatten the
  controls and victory rule of every individual minigame into this signature.
- `SYS-1053` moves the next purchasable Star after an eligible purchase.
- `SYS-1054` applies the final-five rule switch to colored Coin values and
  same-space duels, not to the complete game permanently.
- `INF-394` exposes public route, current vendor and standings without
  previewing the next die or future vendor site.
- `OBJ-232` ranks Stars then Coins at a fixed horizon with a final die for
  complete ties. It is not CATAN's own-turn point threshold `OBJ-219`.

## Transfer and rejection test

`SYS-004` covers chance, `INF-002` covers its unpreviewed future, `ACT-130`
covers priced Stars/items, `ACT-131` covers eligible held-item use,
`CON-177` covers one item slot and `TIM-004` covers exclusive adversarial
turns. `ACT-127` selects one revealed next-floor encounter, not a branch
inside a still-spending die roll. `SYS-1024` converts a CATAN roll to shared
resource production without moving tokens. `OBJ-219` ends on the claimant's
point-threshold turn, not after twenty rounds of ranked Stars and Coins.
Space colors, twenty rounds, twenty-Coin price, four characters and exact
board geometry are parameters. No old signature is retrofitted from one new
source. Internal minigame rules remain possible separately scoped modules.

## Evidence and limits

- [Nintendo's original Mario Party 2 instruction
  booklet](https://www.nintendo.com/eu/media/downloads/games_8/emanuals/nintendo_8/Manual_Nintendo64_MarioParty2_EN.pdf),
  pp. 10–17, directly defines board setup, dice and junctions, pass/land
  events, minigame format and payouts, final-five modifiers and ranking.
- [Nintendo's licensed-availability
  announcement](https://www.nintendo.com/us/whatsnew/nintendo-switch-online-expansion-pack-mario-party-and-mario-party-2-are-now-available/)
  establishes the current Nintendo Switch Online distribution target only.
- No cartridge, ROM or installed Switch wrapper was played. Exact event
  probabilities, named minigame input traces, random seed and cartridge
  revision remain unverified and are not encoded as facts.
