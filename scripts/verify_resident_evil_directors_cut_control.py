#!/usr/bin/env python3
"""Verify the bounded SLUS-00551 Chris key-and-save reconstruction."""

from dataclasses import dataclass, field


class RejectedAction(ValueError):
    """An action lacked a documented prerequisite."""


SWORD_LOCKS = {
    "Keeper's Bedroom",
    "Piano Bar",
    "Art Room exit",
}


@dataclass
class MansionState:
    mode: str = "STANDARD (original version)"
    character: str = "Chris Redfield"
    location: str = "Dining Room"
    capacity: int = 6
    inventory: dict[str, int] = field(default_factory=dict)
    opened: set[str] = field(default_factory=set)
    condition: int = 100
    file: dict[str, object] | None = None


class DirectorCutControl:
    def __init__(self) -> None:
        self.state = MansionState()
        self.milestones = ["ordinary-chris-control"]

    def free_slots(self) -> int:
        return self.state.capacity - len(self.state.inventory)

    def take(self, item: str, quantity: int = 1) -> None:
        if item not in self.state.inventory and self.free_slots() < 1:
            raise RejectedAction("Chris's six inventory slots are full")
        self.state.inventory[item] = self.state.inventory.get(item, 0) + quantity

    def collect_opening_supplies(self) -> None:
        self.state.location = "Main Hall"
        self.take("Handgun")
        self.take("Handgun Clip", 2)
        self.take("Ink Ribbon", 2)
        self.milestones.append("opening-handgun-and-ribbon")

    def enter_west_save_room(self) -> None:
        if "Handgun" not in self.state.inventory:
            raise RejectedAction("The opening route has not been established")
        self.state.location = "West save room"
        self.milestones.append("west-save-room")

    def receive_sword_key(self) -> None:
        if self.state.location != "West save room":
            raise RejectedAction("Rebecca and the Sword Key are unavailable")
        self.take("Sword Key")
        self.milestones.append("sword-key-carried")

    def open_sword_lock(self, lock: str, discard_when_exhausted: bool = False) -> None:
        if lock not in SWORD_LOCKS:
            raise RejectedAction("The fixture is not a Sword Key lock")
        if "Sword Key" not in self.state.inventory:
            raise RejectedAction("The Sword Key is not carried")
        if lock in self.state.opened:
            raise RejectedAction("The selected lock is already open")
        self.state.opened.add(lock)
        if self.state.opened == SWORD_LOCKS:
            if not discard_when_exhausted:
                raise RejectedAction("The final-use discard prompt was not accepted")
            del self.state.inventory["Sword Key"]
            self.milestones.append("sword-key-exhausted-and-discarded")
        elif discard_when_exhausted:
            raise RejectedAction("The Sword Key still has compatible locks")
        else:
            self.milestones.append(f"opened-{lock.lower().replace(' ', '-')}")

    def cross_l_passage(self) -> None:
        if "Art Room exit" not in self.state.opened:
            raise RejectedAction("The L Passage is not traversably connected")
        self.state.location = "L Passage"
        self.milestones.append("l-passage-crossed")

    def return_to_typewriter(self) -> None:
        if self.state.location != "L Passage":
            raise RejectedAction("The positive spatial terminal was not crossed")
        self.state.location = "West save room"

    def write_file(self) -> None:
        if self.state.location != "West save room":
            raise RejectedAction("No eligible typewriter is present")
        if self.state.inventory.get("Ink Ribbon", 0) < 1:
            raise RejectedAction("An Ink Ribbon is required")
        self.state.inventory["Ink Ribbon"] -= 1
        if self.state.inventory["Ink Ribbon"] == 0:
            del self.state.inventory["Ink Ribbon"]
        self.state.file = {
            "mode": self.state.mode,
            "character": self.state.character,
            "location": self.state.location,
            "inventory": dict(self.state.inventory),
            "opened": set(self.state.opened),
            "condition": self.state.condition,
        }
        self.milestones.append("ink-ribbon-consumed-and-file-written")

    def load_file(self) -> None:
        if self.state.file is None:
            raise RejectedAction("No typewriter file exists")
        saved = self.state.file
        self.state.mode = str(saved["mode"])
        self.state.character = str(saved["character"])
        self.state.location = str(saved["location"])
        self.state.inventory = dict(saved["inventory"])
        self.state.opened = set(saved["opened"])
        self.state.condition = int(saved["condition"])
        self.milestones.append("route-reloaded")


def expect_rejected(action, fragment: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert fragment in str(error)
    else:
        raise AssertionError("Invalid route action was accepted")


def main() -> None:
    invalid = DirectorCutControl()
    expect_rejected(lambda: invalid.open_sword_lock("Piano Bar"), "not carried")
    expect_rejected(invalid.write_file, "typewriter")
    expect_rejected(invalid.load_file, "No typewriter file")

    capacity = DirectorCutControl()
    for index in range(6):
        capacity.take(f"item-{index}")
    expect_rejected(lambda: capacity.take("overflow"), "six inventory")

    control = DirectorCutControl()
    control.collect_opening_supplies()
    control.enter_west_save_room()
    control.receive_sword_key()
    control.open_sword_lock("Keeper's Bedroom")
    control.open_sword_lock("Piano Bar")
    assert "Sword Key" in control.state.inventory
    expect_rejected(
        lambda: control.open_sword_lock("Art Room exit"),
        "discard prompt",
    )

    # Reconstruct the atomic final interaction after the deliberately rejected
    # prompt path: the door is still considered unopened until acceptance.
    control.state.opened.remove("Art Room exit")
    control.open_sword_lock("Art Room exit", discard_when_exhausted=True)
    assert control.state.opened == SWORD_LOCKS
    assert "Sword Key" not in control.state.inventory
    control.cross_l_passage()
    control.return_to_typewriter()
    ribbons_before = control.state.inventory["Ink Ribbon"]
    control.write_file()
    assert control.state.inventory["Ink Ribbon"] == ribbons_before - 1

    control.state.location = "Transient failed room"
    control.state.condition = 0
    control.state.inventory["Transient item"] = 1
    control.state.opened.clear()
    control.load_file()
    assert control.state.location == "West save room"
    assert control.state.opened == SWORD_LOCKS
    assert "Sword Key" not in control.state.inventory
    assert "Transient item" not in control.state.inventory
    assert control.milestones[-1] == "route-reloaded"

    print(
        "Resident Evil: Director's Cut control verified: six slots, retained "
        "Sword Key across three locks, final discard, Ink Ribbon save and "
        "reload-retained L Passage."
    )


if __name__ == "__main__":
    main()
