#!/usr/bin/env python3
"""Executable control for TUNIC's bounded fountain Holy Cross packet."""

from dataclasses import dataclass, field
from typing import List, Optional, Set


CODE = ("D", "R", "U", "L", "U", "R")
RESET_GAP = 1.0


@dataclass
class State:
    has_laurels: bool = False
    location: str = "overworld"
    pages: Set[int] = field(default_factory=set)
    buffer: List[str] = field(default_factory=list)
    last_input: Optional[float] = None
    door_open: bool = False


def collect_fountain_pages(state: State) -> bool:
    if state.has_laurels and state.location == "fountain":
        state.pages.update({42, 43})
        return True
    return False


def manual_code(state: State):
    return CODE if 43 in state.pages else None


def enter_direction(state: State, direction: str, now: float) -> bool:
    if state.location != "patterned-door" or state.door_open:
        return state.door_open
    if state.last_input is not None and now - state.last_input > RESET_GAP:
        state.buffer.clear()
    state.last_input = now
    state.buffer.append(direction)
    while state.buffer and tuple(state.buffer) != CODE[: len(state.buffer)]:
        state.buffer.pop(0)
    if tuple(state.buffer) == CODE:
        state.door_open = True
        state.buffer.clear()
    return state.door_open


def traverse_and_collect(state: State) -> bool:
    if not state.door_open or state.location != "patterned-door":
        return False
    state.location = "behind-door"
    state.pages.update({44, 45})
    return True


def enter(state: State, sequence, start=0.0, gap=0.1) -> None:
    for offset, direction in enumerate(sequence):
        enter_direction(state, direction, start + offset * gap)


def verify() -> None:
    state = State(has_laurels=True, location="fountain")
    assert collect_fountain_pages(state)
    assert manual_code(state) == CODE
    state.location = "patterned-door"
    enter(state, CODE)
    assert state.door_open
    assert traverse_and_collect(state)
    assert {42, 43, 44, 45}.issubset(state.pages)

    mirrored = State(location="patterned-door")
    enter(mirrored, ("D", "L", "U", "R", "U", "L"))
    assert not mirrored.door_open

    timed_out = State(location="patterned-door")
    enter(timed_out, CODE[:3], start=0.0)
    enter(timed_out, CODE[3:], start=2.0)
    assert not timed_out.door_open
    enter(timed_out, CODE, start=3.0)
    assert timed_out.door_open

    knowledge_only = State(location="patterned-door")
    assert manual_code(knowledge_only) is None
    enter(knowledge_only, CODE)
    assert knowledge_only.door_open

    sealed = State(location="patterned-door")
    assert not traverse_and_collect(sealed)
    assert 44 not in sealed.pages and 45 not in sealed.pages

    print("PASS: TUNIC fountain Holy Cross packet verified")


if __name__ == "__main__":
    verify()
