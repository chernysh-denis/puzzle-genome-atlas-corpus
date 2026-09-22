#!/usr/bin/env python3
"""Verify the bounded Sands of Time opening and first rewind packet."""

from __future__ import annotations

from dataclasses import dataclass, field


class RejectedAction(ValueError):
    """An action was attempted without its documented prerequisite."""


@dataclass
class PalaceRouteState:
    route_progress: int = 0
    life: int = 4
    max_life: int = 4
    barricade_open: bool = False
    guard_bypassed: bool = False
    dagger_acquired: bool = False
    revival_retained: bool = False
    sand_tanks: int = 0
    history_seconds: int = 0
    rewound_seconds: int = 0


class PalaceRouteControl:
    route = (
        "curtains",
        "barricade",
        "wall-run",
        "ledge-chain",
        "water-basin",
        "wall-jump-shaft",
        "spike-poles",
        "column-chain",
        "statue",
    )

    def __init__(self) -> None:
        self.state = PalaceRouteState()
        self.milestones: list[str] = []

    def _record(self, milestone: str) -> None:
        self.milestones.append(milestone)

    def strike_barricade(self) -> None:
        if self.state.route_progress != 1:
            raise RejectedAction("The scoped barricade is not the current route gate")
        if self.state.barricade_open:
            raise RejectedAction("The scoped barricade is already open")
        self.state.barricade_open = True
        self._record("barricade-opened")

    def resolve_guard(self, choice: str) -> None:
        if self.state.route_progress < 2:
            raise RejectedAction("The optional guard has not been reached")
        if choice not in {"block-and-strike", "bypass"}:
            raise RejectedAction("The guard choice is outside the sourced route")
        self.state.guard_bypassed = choice == "bypass"
        self._record(f"guard-{choice}")

    def take_damage(self, amount: int) -> None:
        if amount <= 0 or amount >= self.state.life:
            raise RejectedAction("This control models non-terminal scoped damage only")
        self.state.life -= amount
        self._record(f"life-damaged-{amount}")

    def drink_water(self) -> None:
        if self.state.route_progress != 5:
            raise RejectedAction("No scoped water fixture is currently reachable")
        if self.state.life == self.state.max_life:
            raise RejectedAction("Life is already full")
        self.state.life = self.state.max_life
        self._record("life-restored")

    def traverse(self, segment: str) -> None:
        if self.state.dagger_acquired:
            raise RejectedAction("The opening packet ended at Dagger acquisition")
        expected = self.route[self.state.route_progress]
        if segment != expected:
            raise RejectedAction("The segment does not match the next authored gate")
        if segment == "barricade" and not self.state.barricade_open:
            raise RejectedAction("The barricade must be removed before passage")
        self.state.route_progress += 1
        self._record(f"route-{segment}")

    def acquire_dagger(self) -> None:
        if self.state.route_progress != len(self.route):
            raise RejectedAction("The statue route is incomplete")
        if self.state.dagger_acquired:
            raise RejectedAction("The Dagger was already acquired")
        self.state.dagger_acquired = True
        self.state.revival_retained = True
        self.state.sand_tanks = 1
        self.state.history_seconds = 10
        self._record("dagger-acquired")
        self._record("automatic-rock-rewind-demonstrated")
        self._record("ordinary-control-returned")

    def rewind(self, seconds: int) -> None:
        if not self.state.revival_retained:
            raise RejectedAction("Power of Revival has not been retained")
        if self.state.sand_tanks < 1:
            raise RejectedAction("No filled Sand Tank funds the rewind")
        if seconds <= 0 or seconds > self.state.history_seconds:
            raise RejectedAction("The requested state is outside retained history")
        self.state.sand_tanks -= 1
        self.state.rewound_seconds = seconds
        self.state.history_seconds -= seconds
        self._record(f"rewound-{seconds}-seconds")


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid prerequisite, route or resource use was accepted")


def main() -> None:
    invalid = PalaceRouteControl()
    expect_rejected(lambda: invalid.traverse("wall-run"), "next authored gate")
    expect_rejected(invalid.strike_barricade, "not the current route gate")
    expect_rejected(lambda: invalid.rewind(3), "has not been retained")
    invalid.traverse("curtains")
    expect_rejected(lambda: invalid.traverse("barricade"), "must be removed")
    invalid.strike_barricade()
    invalid.traverse("barricade")
    expect_rejected(lambda: invalid.resolve_guard("parley"), "outside")

    control = PalaceRouteControl()
    control.traverse("curtains")
    control.strike_barricade()
    control.traverse("barricade")
    control.resolve_guard("bypass")
    control.traverse("wall-run")
    control.traverse("ledge-chain")
    control.take_damage(2)
    control.traverse("water-basin")
    control.drink_water()
    for segment in control.route[5:]:
        control.traverse(segment)
    control.acquire_dagger()
    expect_rejected(lambda: control.rewind(11), "outside retained history")
    control.rewind(6)
    expect_rejected(lambda: control.rewind(1), "No filled Sand Tank")
    expect_rejected(lambda: control.traverse("curtains"), "ended")

    assert control.state.route_progress == len(control.route)
    assert control.state.life == control.state.max_life == 4
    assert control.state.guard_bypassed
    assert control.state.dagger_acquired and control.state.revival_retained
    assert control.state.sand_tanks == 0
    assert control.state.rewound_seconds == 6
    assert control.state.history_seconds == 4
    assert len(control.milestones) == 17
    print(
        "Sands of Time control verified: nine ordered route gates, optional "
        "guard bypass, damage/water recovery, retained Dagger capability, "
        "one finite six-second rewind and eight rejected invalid actions."
    )


if __name__ == "__main__":
    main()
