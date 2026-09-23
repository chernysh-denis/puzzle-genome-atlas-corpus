#!/usr/bin/env python3
"""Deterministic source-bounded transition control for GAME-0362.

This models admitted Morrowind transitions; it does not execute the game.
"""

from __future__ import annotations

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class State:
    name: str = ""
    race: str = ""
    character_class: str = ""
    birthsign: str = ""
    released: bool = False
    pick_uses: int = 25
    chest_open: bool = False
    ring_held: bool = False
    package_held: bool = False
    sellus_directions: bool = False
    balmora_reached: bool = False
    caius_directions: bool = False
    report_complete: bool = False
    blades_rank: str = ""
    gold_awarded: int = 0
    successor: str = ""
    returned_control: bool = False


def create_character(state: State) -> State:
    return replace(
        state,
        name="Atlas",
        race="Dunmer",
        character_class="Warrior",
        birthsign="The Warrior",
    )


def release(state: State) -> State:
    assert (state.name, state.race, state.character_class, state.birthsign) == (
        "Atlas",
        "Dunmer",
        "Warrior",
        "The Warrior",
    )
    return replace(state, released=True)


def attempt_lock(state: State, *, success: bool) -> State:
    assert state.released and not state.chest_open and state.pick_uses > 0
    state = replace(state, pick_uses=state.pick_uses - 1)
    return replace(state, chest_open=True) if success else state


def accept_package(state: State) -> State:
    assert state.released
    return replace(
        state,
        ring_held=True,
        package_held=True,
        sellus_directions=True,
    )


def reach_caius(state: State) -> State:
    assert state.package_held and state.sellus_directions
    return replace(state, balmora_reached=True, caius_directions=True)


def report_and_join(state: State) -> State:
    assert state.balmora_reached and state.caius_directions and state.package_held
    return replace(
        state,
        package_held=False,
        report_complete=True,
        blades_rank="Novice",
        gold_awarded=200,
    )


def accept_orders(state: State) -> State:
    assert state.report_complete and state.blades_rank == "Novice"
    return replace(
        state,
        successor="Antabolis Informant",
        returned_control=True,
    )


def verify() -> None:
    state = release(create_character(State()))
    state = attempt_lock(state, success=False)
    assert state.pick_uses == 24 and not state.chest_open
    state = attempt_lock(state, success=True)
    assert state.pick_uses == 23 and state.chest_open
    state = accept_package(state)
    state = reach_caius(state)
    state = report_and_join(state)
    state = accept_orders(state)

    saved = state
    reloaded = replace(saved)
    assert reloaded == saved
    assert not reloaded.package_held
    assert reloaded.report_complete
    assert reloaded.blades_rank == "Novice"
    assert reloaded.gold_awarded == 200
    assert reloaded.successor == "Antabolis Informant"
    assert reloaded.returned_control

    exhausted = replace(release(create_character(State())), pick_uses=0)
    try:
        attempt_lock(exhausted, success=True)
    except AssertionError:
        pass
    else:
        raise AssertionError("exhausted lockpick was accepted")


if __name__ == "__main__":
    verify()
    print("Morrowind source-bounded control: PASS")
