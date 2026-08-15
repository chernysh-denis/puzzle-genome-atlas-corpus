#!/usr/bin/env python3
"""Verify the bounded Day of the Tentacle super-battery hand-in packet."""

from __future__ import annotations

from dataclasses import dataclass, field


class RejectedAction(ValueError):
    """An observed action was attempted without its documented prerequisite."""


@dataclass
class BatteryState:
    inventory: set[str] = field(
        default_factory=lambda: {
            "patent-application",
            "oil",
            "vinegar",
            "gold-plated-quill",
        }
    )
    recipe_disclosed: bool = False
    handed_ingredients: set[str] = field(default_factory=set)
    battery_on_shelf: bool = False
    battery_collected: bool = False


class BatteryControl:
    recipe = {"oil", "vinegar", "gold-plated-quill"}

    def __init__(self) -> None:
        self.state = BatteryState()
        self.milestones: list[str] = []

    def _record(self, milestone: str) -> None:
        self.milestones.append(milestone)

    def give_patent_application(self) -> None:
        if "patent-application" not in self.state.inventory:
            raise RejectedAction("The patent application has already been handed in")
        self.state.inventory.remove("patent-application")
        self.state.recipe_disclosed = True
        self._record("recipe-disclosed")

    def give_ingredient(self, item: str) -> None:
        if not self.state.recipe_disclosed:
            raise RejectedAction("Red has not disclosed the battery recipe")
        if item not in self.recipe:
            raise RejectedAction("The item is not one of Red's requested ingredients")
        if item in self.state.handed_ingredients:
            raise RejectedAction("That ingredient has already been handed in")
        if item not in self.state.inventory:
            raise RejectedAction("The requested ingredient is not in Hoagie's inventory")
        self.state.inventory.remove(item)
        self.state.handed_ingredients.add(item)
        self._record(f"{item}-handed-in")
        if self.state.handed_ingredients == self.recipe:
            self.state.battery_on_shelf = True
            self._record("super-battery-built")

    def collect_battery(self) -> None:
        if not self.state.battery_on_shelf:
            raise RejectedAction("The super-battery has not been built on the shelf")
        if self.state.battery_collected:
            raise RejectedAction("The super-battery has already been collected")
        self.state.battery_on_shelf = False
        self.state.battery_collected = True
        self.state.inventory.add("uncharged-super-battery")
        self._record("super-battery-collected")


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid prerequisite order was accepted")


def main() -> None:
    invalid = BatteryControl()
    expect_rejected(lambda: invalid.give_ingredient("oil"), "not disclosed")
    expect_rejected(lambda: invalid.give_ingredient("spaghetti"), "not disclosed")
    expect_rejected(invalid.collect_battery, "not been built")
    invalid.give_patent_application()
    expect_rejected(invalid.give_patent_application, "already been handed in")
    expect_rejected(lambda: invalid.give_ingredient("spaghetti"), "not one")
    invalid.give_ingredient("oil")
    expect_rejected(lambda: invalid.give_ingredient("oil"), "already been handed in")
    invalid.give_ingredient("vinegar")
    assert not invalid.state.battery_on_shelf

    control = BatteryControl()
    control.give_patent_application()
    control.give_ingredient("oil")
    control.give_ingredient("vinegar")
    control.give_ingredient("gold-plated-quill")
    control.collect_battery()

    assert control.state.battery_collected
    assert control.state.handed_ingredients == control.recipe
    assert "uncharged-super-battery" in control.state.inventory
    assert control.milestones == [
        "recipe-disclosed",
        "oil-handed-in",
        "vinegar-handed-in",
        "gold-plated-quill-handed-in",
        "super-battery-built",
        "super-battery-collected",
    ]
    print(
        "Day of the Tentacle control verified: 6 ordered milestones, one exact "
        "three-ingredient hand-in set, one NPC-built battery and six rejected "
        "prerequisite violations."
    )


if __name__ == "__main__":
    main()
