# Taxonomy Change 106: Target resistance and tactical pause in Mass Effect 2

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-09-23
- Trigger: GAME-0367 Mass Effect 2 (Legendary Edition), fresh Soldier through
  Freedom's Progress and first Normandy SR-2 control.
- Scope: three new Active boundaries; no prior signature or lifecycle changes.

## Problem

The existing corpus can represent gunfire, cover, layered damage, companion
orders and an authored dialogue choice. Its general damage-layer boundary does
not express that a ready health-affecting or incapacitating power is rejected
while a compatible shield, armour or barrier remains. A generic target health
bar does not expose those typed layers, and live-time combat alone does not
describe the player-held tactical pause of the power and weapon wheels.

## Accepted change

- Add CON-668 for protection-sensitive effect eligibility, distinct from
  damage passing through SYS-348 and ordinary target/range/cooldown legality
  in CON-269.
- Add INF-375 for visible typed target protection and contextual power
  suitability, distinct from personal status in INF-119.
- Add TIM-027 for the held command-radial pause and return to live resolution.
  This does not convert the shooter into a turn-based game.
- Reuse ACT-189 and SYS-297 for independent squad position/target orders,
  ACT-232 for the offered dialogue and interrupt, SYS-379 for the retained
  mission/custody result, and OBJ-155 for the successor-control terminal.
  No new recruitment boundary is added: the chosen terminal only exposes
  future dossiers.

## Lower-ID transfer test

- Gears of War provides cover and firearm boundaries but lacks a power wheel,
  typed power eligibility and a dialogue choice in this packet.
- Fallout: New Vegas provides conversation, action combat and a retained
  local outcome, but its opening town uses recruited allies rather than
  separately addressed two-member squad commands.
- SYS-348 covers shield and health depletion, not the legality of a distinct
  status power before the resistance layer falls. INF-119 covers a character's
  own resources, not the selected enemy's protection type. TIM-003 continues
  active time; it cannot alone encode a held pause that accepts tactical input.
- No combination is inferred from one newly analysed game. A complete
  lower-ID Jaccard and verified-subset scan is recorded in its game file.

## Evidence and limits

The official original Mass Effect 2 Xbox manual directly states separate
shield/armour/barrier target bars, the resistance rule for incapacitation and
health powers, independent squad orders, and a pause for command radials. EA's
Legendary Edition notes confirm the ME2 command baseline and identify changed
cover and ammunition tuning. No executable, save or direct audiovisual trace
was available, so exact remaster drop counts, prompt timing and numerical
damage are outside the decision.
