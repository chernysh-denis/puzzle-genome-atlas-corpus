#!/usr/bin/env python3
"""Verify the bounded Deus Ex GOTY Training and Mission 1 reconstruction."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field


class RejectedAction(ValueError):
    """An action was attempted outside the documented packet."""


@dataclass
class DeusExState:
    segment: str = "training"
    skill_points: int = 5000
    skills: dict[str, str] = field(
        default_factory=lambda: {
            "Pistols": "Trained",
            "Computers": "Untrained",
            "Electronics": "Untrained",
            "Lockpicking": "Untrained",
        }
    )
    inventory_cells: int = 30
    occupied_cells: int = 0
    credentials: dict[str, str] = field(default_factory=dict)
    nanokeys: set[str] = field(default_factory=set)
    flags: set[str] = field(default_factory=set)
    objective: str = "complete-training"
    live: bool = True


class DeusExMissionControl:
    skill_costs = {"Computers": 1125, "Electronics": 1800, "Lockpicking": 1800}

    def __init__(self) -> None:
        self.state = DeusExState()
        self.saves: dict[str, DeusExState] = {}

    def finish_training(self, demonstrations: set[str]) -> None:
        required = {"nanokey", "lockpick", "code", "multitool", "stealth", "final-test"}
        if not required <= demonstrations:
            raise RejectedAction("Mandatory Training demonstrations are incomplete")
        self.state.segment = "character-creation"
        self.state.objective = "allocate-skills"

    def buy_trained(self, skill: str) -> None:
        if self.state.segment != "character-creation":
            raise RejectedAction("Skills can be allocated only before campaign entry")
        if skill not in self.skill_costs or self.state.skills[skill] != "Untrained":
            raise RejectedAction("Only the declared next technical rank is admitted")
        cost = self.skill_costs[skill]
        if self.state.skill_points < cost:
            raise RejectedAction("Insufficient unspent skill points")
        self.state.skill_points -= cost
        self.state.skills[skill] = "Trained"

    def enter_liberty_island(self) -> None:
        required = {name for name in self.skill_costs if self.state.skills[name] == "Trained"}
        if required != set(self.skill_costs) or self.state.skill_points != 275:
            raise RejectedAction("Declared 4725-point technical build is incomplete")
        self.state.segment = "liberty-island"
        self.state.objective = "reach-leo"

    def pick_item(self, item: str, footprint: int) -> None:
        if footprint <= 0 or self.state.occupied_cells + footprint > self.state.inventory_cells:
            raise RejectedAction("Item footprint does not fit the inventory grid")
        self.state.occupied_cells += footprint
        self.state.flags.add(f"item:{item}")

    def meet_harley(self, promise_nonlethal: bool) -> None:
        if self.state.segment != "liberty-island" or not promise_nonlethal:
            raise RejectedAction("Harley key requires the declared promise")
        self.state.flags.add("harley-promise")
        self.state.nanokeys.add("statue-door")

    def read_credentials(self, login: str, password: str) -> None:
        self.state.credentials[login] = password

    def open_statue(self, method: str) -> None:
        legal = {
            "nanokey": "statue-door" in self.state.nanokeys,
            "credentials": self.state.credentials.get("NSF001") == "smashthestate",
            "lockpick": self.state.skills["Lockpicking"] == "Trained",
            "multitool": self.state.skills["Electronics"] == "Trained",
            "rear-route": True,
        }
        if not legal.get(method, False):
            raise RejectedAction("Chosen access authority or route is not available")
        self.state.flags.add(f"statue-access:{method}")

    def settle_leo(self, response: str) -> None:
        if not any(flag.startswith("statue-access:") for flag in self.state.flags):
            raise RejectedAction("Leo cannot be reached before Statue access")
        if response != "accept-surrender":
            raise RejectedAction("Fixed trace requires Leo's surrender")
        self.state.flags.add("leo-surrendered")
        self.state.objective = "report-paul"

    def report(self, actor: str) -> None:
        predecessors = {
            "Paul": "leo-surrendered",
            "Manderley": "reported-paul",
        }
        required = predecessors.get(actor)
        if required is None or required not in self.state.flags:
            raise RejectedAction("Mandatory report order is not satisfied")
        self.state.flags.add(f"reported-{actor.lower()}")
        self.state.objective = "report-manderley" if actor == "Paul" else "board-boat"

    def board_boat(self) -> None:
        if "reported-manderley" not in self.state.flags:
            raise RejectedAction("Boat requires the completed HQ chain")
        self.state.segment = "battery-park"
        self.state.objective = "battery-park"
        self.state.flags.add("mission-1-complete")

    def save(self, name: str) -> None:
        self.saves[name] = deepcopy(self.state)

    def load(self, name: str) -> None:
        if name not in self.saves:
            raise RejectedAction("Selected save does not exist")
        self.state = deepcopy(self.saves[name])


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid Deus Ex action was accepted")


def main() -> None:
    control = DeusExMissionControl()
    expect_rejected(lambda: control.finish_training({"nanokey"}), "incomplete")
    control.finish_training({"nanokey", "lockpick", "code", "multitool", "stealth", "final-test"})
    for skill in ("Computers", "Electronics", "Lockpicking"):
        control.buy_trained(skill)
    assert control.state.skill_points == 275
    control.enter_liberty_island()
    control.pick_item("mini-crossbow", 6)
    expect_rejected(lambda: control.pick_item("oversized", 25), "does not fit")
    control.meet_harley(True)
    control.read_credentials("NSF001", "smashthestate")
    control.open_statue("credentials")
    control.settle_leo("accept-surrender")
    expect_rejected(control.board_boat, "HQ chain")
    control.report("Paul")
    control.report("Manderley")
    control.board_boat()
    assert control.state.segment == "battery-park"
    retained = deepcopy(control.state)
    control.save("battery-park-entry")
    control.state.occupied_cells = 0
    control.state.flags.clear()
    control.load("battery-park-entry")
    assert control.state == retained

    alternative = DeusExMissionControl()
    alternative.finish_training({"nanokey", "lockpick", "code", "multitool", "stealth", "final-test"})
    for skill in ("Computers", "Electronics", "Lockpicking"):
        alternative.buy_trained(skill)
    alternative.enter_liberty_island()
    alternative.open_statue("rear-route")

    print(
        "Deus Ex GOTY control verified: mandatory Training, fixed 4725-point "
        "build, 30-cell inventory, credentialed and physical access, surrender, "
        "ordered HQ/boat handoff and retained Battery Park save state."
    )


if __name__ == "__main__":
    main()
