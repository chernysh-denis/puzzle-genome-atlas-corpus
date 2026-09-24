# Taxonomy Change 128: live conveyor support and boss-weapon stage clear

## Status

- Proposal status: Accepted
- Claim status: Observation
- Evidence quality: Corroborated
- Confidence: Medium
- Date: 2026-09-24
- Trigger: `GAME-0389` Mega Man 2, original North American NES Normal,
  fresh first selection of Metal Man through his stage-clear reward.
- Scope: three additive Active genes; no earlier genome, family boundary or
  verified combination is changed.

## Problem and accepted change

The existing discrete conveyor gene transports inert assemblies during an
automatic factory run, not a player-steered avatar across a live support
surface. Generic physics and movement do not say that ground contact itself
adds directional drift. Existing guardian objectives cross a physical
threshold or close a larger campaign act; this packet ends at a stage selector
with a fixed weapon determined by the defeated Robot Master.

- `SYS-1047` isolates real-time contact-driven conveyor drift while movement
  and jumping remain player-controlled.
- `SYS-1048` turns Metal Man's defeat into the fixed Metal Blade grant and
  cleared-stage mark.
- `OBJ-230` names the bounded route, boss-clear and retained-weapon terminal.

## Transfer and rejection test

`ACT-008`, `ACT-161`, `SYS-036`, `SYS-215`, `INF-192` and `TIM-003` continue
to cover direct movement, shooting, physical motion, combat, partial side-view
lookahead and real-time advancement. `SYS-077` needs discrete automatic
assembly transport. `SYS-065` needs a switch-directed platform. `OBJ-080`
requires crossing a newly opened route threshold, absent from this terminal.
No earlier signature is retrofitted on the basis of this single packet.

## Evidence and limits

- [Original Nintendo-hosted NES manual](https://www.nintendo.co.jp/clv/manuals/en/pdf/CLV-P-NABBE.pdf)
  establishes Normal selection, first-stage controls and boss weapon grants.
- [HonestGamers' Metal Man route](https://www.honestgamers.com/guides/mega-man-2/1/read/5.html)
  and [GameFAQs' NES guide](https://gamefaqs.gamespot.com/nes/563442-mega-man-2/faqs/6451)
  independently describe conveyors, hazards, fight and reward.
- No original cartridge execution or frame trace was performed. Exact belt
  speed, reversal trigger, boss damage and checkpoint locations are not
  encoded in these genes.
