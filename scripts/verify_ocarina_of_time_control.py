#!/usr/bin/env python3
"""Source-bounded first-Deku-Tree transition control for GAME-0363.

This models declared gates from Nintendo's manual and corroborating routes;
it does not execute or emulate Ocarina of Time.
"""

from __future__ import annotations

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class State:
    sword: bool = False
    shield: bool = False
    entered_tree: bool = False
    map_owned: bool = False
    first_scrub_stunned: bool = False
    first_scrub_spoken: bool = False
    slingshot: bool = False
    seeds: int = 0
    ladder_lowered: bool = False
    compass_owned: bool = False
    torch_gate: bool = False
    lower_web_broken: bool = False
    water_lowered: bool = False
    eye_switch: bool = False
    block_moved: bool = False
    final_web_burned: bool = False
    scrub_prefix: tuple[int, ...] = ()
    boss_door_open: bool = False
    gohma_stunned: bool = False
    gohma_hits: int = 0
    gohma_defeated: bool = False
    boss_exit_used: bool = False
    emerald: bool = False
    forest_control: bool = False
    left_forest: bool = False
    small_keys: int = 0
    fairy_ocarina: bool = False


def enter_tree(state: State) -> State:
    assert state.sword and state.shield
    return replace(state, entered_tree=True)


def reflect_scrub(state: State, *, guard_held: bool) -> State:
    assert state.entered_tree and state.shield and guard_held
    return replace(state, first_scrub_stunned=True)


def speak_to_scrub(state: State) -> State:
    assert state.first_scrub_stunned
    return replace(state, first_scrub_spoken=True)


def acquire_slingshot(state: State) -> State:
    assert state.first_scrub_spoken
    return replace(state, slingshot=True, seeds=30)


def shoot_ladder(state: State) -> State:
    assert state.slingshot and state.seeds > 0
    return replace(state, seeds=state.seeds - 1, ladder_lowered=True)


def enter_lower_route(state: State) -> State:
    assert state.map_owned and state.ladder_lowered and state.compass_owned
    assert state.torch_gate
    return replace(state, lower_web_broken=True)


def open_lower_gates(state: State) -> State:
    assert state.lower_web_broken and state.slingshot and state.seeds > 0
    assert state.small_keys == 0
    return replace(
        state,
        water_lowered=True,
        eye_switch=True,
        block_moved=True,
        final_web_burned=True,
        seeds=state.seeds - 1,
    )


def reflect_ordered_scrub(state: State, scrub_number: int, *, guard_held: bool) -> State:
    assert state.final_web_burned and state.shield and guard_held
    assert scrub_number in (1, 2, 3)
    expected = (2, 3, 1)
    candidate = state.scrub_prefix + (scrub_number,)
    if candidate != expected[: len(candidate)]:
        return replace(state, scrub_prefix=(), boss_door_open=False)
    return replace(
        state,
        scrub_prefix=candidate,
        boss_door_open=candidate == expected,
    )


def shoot_gohma_eye(state: State, *, eye_red: bool) -> State:
    assert state.boss_door_open and not state.gohma_defeated
    assert state.slingshot and state.seeds > 0
    return replace(state, seeds=state.seeds - 1, gohma_stunned=eye_red)


def strike_gohma(state: State) -> State:
    assert state.gohma_stunned and state.sword
    hits = state.gohma_hits + 1
    return replace(
        state,
        gohma_stunned=False,
        gohma_hits=hits,
        gohma_defeated=hits >= 3,
    )


def use_boss_exit(state: State) -> State:
    assert state.gohma_defeated
    return replace(state, boss_exit_used=True)


def receive_emerald(state: State) -> State:
    assert state.boss_exit_used and not state.left_forest
    assert not state.fairy_ocarina and state.small_keys == 0
    return replace(state, emerald=True, forest_control=True)


def positive_route() -> State:
    state = enter_tree(State(sword=True, shield=True))
    state = replace(state, map_owned=True)
    state = speak_to_scrub(reflect_scrub(state, guard_held=True))
    state = shoot_ladder(acquire_slingshot(state))
    state = enter_lower_route(replace(state, compass_owned=True, torch_gate=True))
    state = open_lower_gates(state)
    for number in (2, 3, 1):
        state = reflect_ordered_scrub(state, number, guard_held=True)
    for _ in range(3):
        state = strike_gohma(shoot_gohma_eye(state, eye_red=True))
    state = receive_emerald(use_boss_exit(state))
    assert state.emerald and state.forest_control
    assert not state.left_forest and not state.fairy_ocarina
    assert state.small_keys == 0
    return state


def verify() -> None:
    positive_route()


if __name__ == "__main__":
    verify()
    print("Ocarina of Time source-bounded control: PASS")
