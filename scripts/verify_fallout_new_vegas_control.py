#!/usr/bin/env python3
"""Deterministic source-bounded control for GAME-0361.

This models the admitted transitions; it does not execute Fallout: New Vegas.
"""

from __future__ import annotations

from dataclasses import dataclass, replace


SPECIAL = {
    "strength": 5,
    "perception": 5,
    "endurance": 5,
    "charisma": 6,
    "intelligence": 7,
    "agility": 6,
    "luck": 6,
}
TAGS = frozenset({"explosives", "medicine", "speech"})


@dataclass(frozen=True)
class State:
    special: tuple[tuple[str, int], ...] = ()
    tags: frozenset[str] = frozenset()
    tutorial_complete: bool = False
    defended_branch: bool = False
    allies: frozenset[str] = frozenset()
    quest_complete: bool = False
    goodsprings_fame: bool = False
    powder_gangers_infamy: bool = False
    returned_control: bool = False


def commit_creation(state: State, special: dict[str, int], tags: set[str]) -> State:
    assert set(special) == set(SPECIAL)
    assert sum(special.values()) == 40
    assert all(1 <= value <= 10 for value in special.values())
    assert len(tags) == 3
    assert tags <= {"barter", "energy", "explosives", "guns", "lockpick", "medicine", "melee", "repair", "science", "sneak", "speech", "survival", "unarmed"}
    return replace(state, special=tuple(sorted(special.items())), tags=frozenset(tags))


def prepare_goodsprings(state: State) -> State:
    assert state.special and state.tags == TAGS
    state = replace(state, tutorial_complete=True, defended_branch=True)
    return replace(state, allies=frozenset({"sunny", "trudy", "easy-pete", "doc-mitchell"}))


def settle_fight(state: State) -> State:
    assert state.tutorial_complete and state.defended_branch
    assert {"sunny", "trudy", "easy-pete", "doc-mitchell"} <= state.allies
    return replace(
        state,
        quest_complete=True,
        goodsprings_fame=True,
        powder_gangers_infamy=True,
        returned_control=True,
    )


def verify() -> None:
    state = commit_creation(State(), SPECIAL, set(TAGS))
    state = prepare_goodsprings(state)
    state = settle_fight(state)
    saved = state
    reloaded = replace(saved)
    assert reloaded == saved
    assert reloaded.quest_complete
    assert reloaded.goodsprings_fame and reloaded.powder_gangers_infamy
    assert reloaded.returned_control

    for bad in ({"speech", "medicine"}, {"speech", "medicine", "explosives", "guns"}, {"speech", "speech", "medicine"}):
        try:
            commit_creation(State(), SPECIAL, set(bad))
        except AssertionError:
            pass
        else:
            raise AssertionError(f"invalid tagged-skill set accepted: {bad}")


if __name__ == "__main__":
    verify()
    print("Fallout: New Vegas source-bounded control: PASS")
