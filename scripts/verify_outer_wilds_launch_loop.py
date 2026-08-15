#!/usr/bin/env python3
"""Executable control for Outer Wilds' bounded launch-code loop packet."""

from dataclasses import dataclass, field
from typing import Set, Tuple


LAUNCH_CODE: Tuple[str, str, str] = ("--", "-..", "-.")


@dataclass
class State:
    loop: int = 0
    location: str = "campfire"
    statue_paired: bool = False
    learned_facts: Set[str] = field(default_factory=set)
    carried_items: Set[str] = field(default_factory=set)
    lift_open: bool = False
    visited_hornfels_this_loop: bool = False


def receive_launch_codes(state: State) -> bool:
    if state.location != "observatory":
        return False
    state.learned_facts.add("launch-code")
    state.visited_hornfels_this_loop = True
    return True


def pair_with_statue(state: State) -> bool:
    if state.location != "observatory" or "launch-code" not in state.learned_facts:
        return False
    state.statue_paired = True
    return True


def activate_launch_lift(state: State) -> bool:
    if state.location != "launch-tower" or "launch-code" not in state.learned_facts:
        return False
    state.lift_open = True
    state.location = "launch-pad"
    return True


def end_loop(state: State) -> bool:
    """Resolve the post-pairing death/supernova reset.

    The control deliberately refuses a pre-pairing reset: the scoped repeating
    loop and its memory transfer are established only after statue pairing.
    """
    if not state.statue_paired:
        return False
    remembered = set(state.learned_facts)
    state.loop += 1
    state.location = "campfire"
    state.learned_facts = remembered
    state.carried_items.clear()
    state.lift_open = False
    state.visited_hornfels_this_loop = False
    return True


def verify() -> None:
    blocked = State(location="launch-tower")
    assert not activate_launch_lift(blocked)
    assert blocked.location == "launch-tower"

    first = State(location="observatory", carried_items={"probe-prop"})
    assert receive_launch_codes(first)
    assert pair_with_statue(first)
    assert LAUNCH_CODE == ("--", "-..", "-.")
    first.location = "launch-tower"
    assert activate_launch_lift(first)
    assert first.location == "launch-pad"

    assert end_loop(first)
    assert first.loop == 1
    assert first.location == "campfire"
    assert "launch-code" in first.learned_facts
    assert not first.carried_items
    assert not first.lift_open
    assert not first.visited_hornfels_this_loop

    first.location = "launch-tower"
    assert activate_launch_lift(first)
    assert first.location == "launch-pad"
    assert not first.visited_hornfels_this_loop

    unpaired = State(location="observatory")
    assert receive_launch_codes(unpaired)
    assert not end_loop(unpaired)
    assert unpaired.loop == 0

    print("PASS: Outer Wilds launch-code loop packet verified")


if __name__ == "__main__":
    verify()
