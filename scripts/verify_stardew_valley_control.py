#!/usr/bin/env python3
"""Verify Stardew Valley's standard Boiler Room bundle restoration packet."""

from __future__ import annotations

from dataclasses import dataclass, field


class RejectedAction(ValueError):
    """A contribution or transition violated the documented bundle rules."""


@dataclass(frozen=True)
class Requirement:
    item: str
    count: int = 1


@dataclass
class BoilerRoomState:
    inventory: dict[str, int] = field(
        default_factory=lambda: {
            "copper-bar": 1,
            "iron-bar": 1,
            "gold-bar": 1,
            "quartz": 1,
            "earth-crystal": 1,
            "frozen-tear": 1,
            "fire-quartz": 1,
            "slime": 99,
            "bat-wing": 10,
            "stone": 1,
        }
    )
    contributions: dict[str, set[str]] = field(
        default_factory=lambda: {
            "blacksmith": set(),
            "geologist": set(),
            "adventurer": set(),
        }
    )
    completed_bundles: set[str] = field(default_factory=set)
    room_complete: bool = False
    repair_scheduled: bool = False
    minecarts_repaired: bool = False


class BoilerRoomControl:
    requirements = {
        "blacksmith": {
            "copper-bar": Requirement("copper-bar"),
            "iron-bar": Requirement("iron-bar"),
            "gold-bar": Requirement("gold-bar"),
        },
        "geologist": {
            "quartz": Requirement("quartz"),
            "earth-crystal": Requirement("earth-crystal"),
            "frozen-tear": Requirement("frozen-tear"),
            "fire-quartz": Requirement("fire-quartz"),
        },
        "adventurer": {
            "slime": Requirement("slime", 99),
            "bat-wing": Requirement("bat-wing", 10),
            "solar-essence": Requirement("solar-essence"),
            "void-essence": Requirement("void-essence"),
        },
    }
    required_slots = {"blacksmith": 3, "geologist": 4, "adventurer": 2}

    def __init__(self) -> None:
        self.state = BoilerRoomState()
        self.milestones: list[str] = []

    def contribute(self, bundle: str, item: str) -> None:
        if bundle not in self.requirements:
            raise RejectedAction("The addressed Boiler Room bundle does not exist")
        if bundle in self.state.completed_bundles:
            raise RejectedAction("The addressed bundle is already complete")
        requirement = self.requirements[bundle].get(item)
        if requirement is None:
            raise RejectedAction("The item is not displayed by the addressed bundle")
        if item in self.state.contributions[bundle]:
            raise RejectedAction("That displayed item slot is already filled")
        if self.state.inventory.get(item, 0) < requirement.count:
            raise RejectedAction("The inventory stack is smaller than the displayed requirement")

        self.state.inventory[item] -= requirement.count
        self.state.contributions[bundle].add(item)
        self.milestones.append(f"{bundle}:{item}-contributed")

        if len(self.state.contributions[bundle]) == self.required_slots[bundle]:
            self.state.completed_bundles.add(bundle)
            self.milestones.append(f"{bundle}-bundle-complete")
            if len(self.state.completed_bundles) == 3:
                self.state.room_complete = True
                self.milestones.append("boiler-room-complete")

    def end_day(self) -> None:
        if not self.state.room_complete:
            raise RejectedAction("Minecart repair cannot be scheduled before all three bundles")
        if self.state.repair_scheduled:
            raise RejectedAction("Minecart repair is already scheduled")
        self.state.repair_scheduled = True
        self.milestones.append("minecart-repair-scheduled")

    def begin_next_day(self) -> None:
        if not self.state.repair_scheduled:
            raise RejectedAction("The overnight Junimo repair has not been scheduled")
        self.state.minecarts_repaired = True
        self.milestones.append("minecarts-available")


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid bundle transition was accepted")


def complete_fixed(control: BoilerRoomControl) -> None:
    for item in ("copper-bar", "iron-bar", "gold-bar"):
        control.contribute("blacksmith", item)
    for item in ("quartz", "earth-crystal", "frozen-tear", "fire-quartz"):
        control.contribute("geologist", item)


def main() -> None:
    invalid = BoilerRoomControl()
    expect_rejected(lambda: invalid.contribute("pantry", "copper-bar"), "does not exist")
    expect_rejected(lambda: invalid.contribute("blacksmith", "stone"), "not displayed")
    invalid.state.inventory["slime"] = 98
    expect_rejected(lambda: invalid.contribute("adventurer", "slime"), "smaller")
    invalid.state.inventory["slime"] = 99
    invalid.contribute("adventurer", "slime")
    expect_rejected(lambda: invalid.contribute("adventurer", "slime"), "already filled")
    expect_rejected(invalid.end_day, "before all three")
    expect_rejected(invalid.begin_next_day, "not been scheduled")
    assert invalid.state.contributions["adventurer"] == {"slime"}

    control = BoilerRoomControl()
    complete_fixed(control)
    control.contribute("adventurer", "slime")
    assert not control.state.room_complete
    control.contribute("adventurer", "bat-wing")
    control.end_day()
    control.begin_next_day()

    assert control.state.minecarts_repaired
    assert control.state.completed_bundles == {"blacksmith", "geologist", "adventurer"}
    assert len([m for m in control.milestones if m.endswith("-contributed")]) == 9
    assert len([m for m in control.milestones if m.endswith("bundle-complete")]) == 3
    assert control.milestones[-3:] == [
        "boiler-room-complete",
        "minecart-repair-scheduled",
        "minecarts-available",
    ]
    print(
        "Stardew Valley control verified: 9 accepted typed contributions, "
        "3 persistent bundle completions, one 2-of-4 alternative bundle, "
        "one next-day minecart repair and six rejected invalid transitions."
    )


if __name__ == "__main__":
    main()
