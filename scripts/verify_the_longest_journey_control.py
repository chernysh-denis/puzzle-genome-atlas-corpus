#!/usr/bin/env python3
"""Verify the bounded The Longest Journey subway-key tool packet for GAME-0087."""

from __future__ import annotations

from dataclasses import dataclass, field


class RejectedAction(ValueError):
    """An observed action was attempted without its documented prerequisite."""


@dataclass
class SubwayToolState:
    inventory: set[str] = field(
        default_factory=lambda: {"clamp", "clothesline", "rubber-ducky"}
    )
    duck_inspected: bool = False
    bandage_removed: bool = False
    duck_inflated: bool = False
    inflation_ticks: int = 0
    key_retrieved: bool = False


class SubwayToolControl:
    def __init__(self) -> None:
        self.state = SubwayToolState()
        self.milestones: list[str] = []
        self.expiries = 0

    def _record(self, milestone: str) -> None:
        self.milestones.append(milestone)

    def inspect_duck(self) -> None:
        if "rubber-ducky" not in self.state.inventory:
            raise RejectedAction("The rubber ducky is not available for close inspection")
        self.state.duck_inspected = True
        self._record("ducky-inspected")

    def remove_bandage(self) -> None:
        if not self.state.duck_inspected:
            raise RejectedAction("The bandage hotspot is unavailable before close inspection")
        if self.state.bandage_removed:
            raise RejectedAction("The bandage has already been removed")
        self.state.bandage_removed = True
        self.state.inventory.add("bandage")
        self._record("bandage-removed")

    def combine_clamp_and_line(self) -> None:
        if not {"clamp", "clothesline"} <= self.state.inventory:
            raise RejectedAction("The first assembly requires clamp and clothesline")
        self.state.inventory -= {"clamp", "clothesline"}
        self.state.inventory.add("clamp-line")
        self._record("clamp-line-combined")

    def inflate_duck(self) -> None:
        if "rubber-ducky" not in self.state.inventory:
            raise RejectedAction("The rubber ducky is not separately available")
        if not self.state.bandage_removed:
            raise RejectedAction("The patched duck does not provide the required timed leak")
        self.state.duck_inflated = True
        self.state.inflation_ticks = 2
        self._record("ducky-inflated")

    def combine_duck_with_clamp_line(self) -> None:
        if "clamp-line" not in self.state.inventory:
            raise RejectedAction("The second assembly requires the clamp-line composite")
        if "rubber-ducky" not in self.state.inventory or not self.state.duck_inflated:
            raise RejectedAction("The second assembly requires the inflated rubber ducky")
        self.state.inventory -= {"clamp-line", "rubber-ducky"}
        self.state.inventory.add("fishing-instrument")
        self._record("fishing-instrument-combined")

    def elapse(self) -> None:
        if not self.state.duck_inflated:
            return
        self.state.inflation_ticks -= 1
        if self.state.inflation_ticks <= 0:
            self.state.duck_inflated = False
            if "fishing-instrument" in self.state.inventory:
                self.state.inventory.remove("fishing-instrument")
                self.state.inventory |= {"clamp-line", "rubber-ducky"}
            self.expiries += 1

    def retrieve_key(self) -> None:
        if "fishing-instrument" not in self.state.inventory:
            raise RejectedAction("The track key requires the complete fishing instrument")
        if not self.state.duck_inflated or self.state.inflation_ticks <= 0:
            raise RejectedAction("The duck has deflated and the clamp is no longer held open")
        self.state.inventory.remove("fishing-instrument")
        self.state.inventory.add("iron-key")
        self.state.key_retrieved = True
        self._record("iron-key-retrieved")


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid prerequisite order was accepted")


def main() -> None:
    invalid = SubwayToolControl()
    expect_rejected(invalid.remove_bandage, "before close inspection")
    invalid.state.inventory.remove("clothesline")
    expect_rejected(invalid.combine_clamp_and_line, "clamp and clothesline")
    invalid.state.inventory.add("clothesline")
    expect_rejected(invalid.inflate_duck, "timed leak")
    invalid.combine_clamp_and_line()
    expect_rejected(invalid.combine_duck_with_clamp_line, "inflated rubber ducky")
    expect_rejected(invalid.retrieve_key, "complete fishing instrument")

    expired = SubwayToolControl()
    expired.inspect_duck()
    expired.remove_bandage()
    expired.combine_clamp_and_line()
    expired.inflate_duck()
    expired.combine_duck_with_clamp_line()
    expired.elapse()
    expired.elapse()
    assert expired.expiries == 1
    assert expired.state.inventory >= {"clamp-line", "rubber-ducky", "bandage"}
    expect_rejected(expired.retrieve_key, "complete fishing instrument")

    control = SubwayToolControl()
    control.inspect_duck()
    control.remove_bandage()
    control.combine_clamp_and_line()
    control.inflate_duck()
    control.combine_duck_with_clamp_line()
    control.elapse()
    control.retrieve_key()

    assert control.state.key_retrieved
    assert "iron-key" in control.state.inventory
    assert control.milestones == [
        "ducky-inspected",
        "bandage-removed",
        "clamp-line-combined",
        "ducky-inflated",
        "fishing-instrument-combined",
        "iron-key-retrieved",
    ]
    print(
        "The Longest Journey control verified: 6 ordered milestones, two staged "
        "inventory combinations, one transient inflation window, one expiry reset "
        "and six rejected prerequisite violations."
    )


if __name__ == "__main__":
    main()
