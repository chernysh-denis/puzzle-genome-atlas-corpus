#!/usr/bin/env python3
"""Verify the bounded Monkey Island treasure-huntery trial packet."""

from __future__ import annotations

from dataclasses import dataclass, field


class RejectedAction(ValueError):
    """An action was attempted without its documented prerequisite."""


@dataclass
class TreasureTrialState:
    inventory: set[str] = field(default_factory=set)
    pieces_of_eight: int = 0
    trials_accepted: bool = True
    circus_paid: bool = False
    map_offer_unlocked: bool = False
    map_inspected: bool = False
    route_progress: int = 0
    treasure_clearing_reached: bool = False
    proof_acquired: bool = False


class TreasureTrialControl:
    route = (
        "back",
        "left",
        "right",
        "left",
        "right",
        "back",
        "right",
        "left",
        "back",
    )
    circus_payment = 478
    map_price = 100
    shovel_price = 75

    def __init__(self) -> None:
        self.state = TreasureTrialState()
        self.milestones: list[str] = []

    def _record(self, milestone: str) -> None:
        self.milestones.append(milestone)

    def collect_pot(self) -> None:
        if not self.state.trials_accepted:
            raise RejectedAction("The Three Trials have not been accepted")
        if "pot" in self.state.inventory or self.state.circus_paid:
            raise RejectedAction("The kitchen pot is not available to collect")
        self.state.inventory.add("pot")
        self._record("pot-collected")

    def perform_circus_stunt(self) -> None:
        if "pot" not in self.state.inventory:
            raise RejectedAction("The cannon stunt requires the pot as a helmet")
        if self.state.circus_paid:
            raise RejectedAction("The scoped circus payment was already awarded")
        self.state.inventory.remove("pot")
        self.state.pieces_of_eight += self.circus_payment
        self.state.circus_paid = True
        self._record("circus-payment-awarded")

    def answer_map_seller(self, response: str) -> None:
        if response != "barber-dominique":
            raise RejectedAction("The selected response does not unlock the map offer")
        self.state.map_offer_unlocked = True
        self._record("map-offer-unlocked")

    def buy_map(self) -> None:
        if not self.state.map_offer_unlocked:
            raise RejectedAction("The map offer is still locked")
        self._buy("treasure-map", self.map_price)
        self._record("treasure-map-bought")

    def buy_shovel(self) -> None:
        self._buy("shovel", self.shovel_price)
        self._record("shovel-bought")

    def _buy(self, item: str, price: int) -> None:
        if item in self.state.inventory:
            raise RejectedAction(f"The {item} has already been bought")
        if self.state.pieces_of_eight < price:
            raise RejectedAction(f"Insufficient Pieces o' Eight for the {item}")
        self.state.pieces_of_eight -= price
        self.state.inventory.add(item)

    def inspect_map(self) -> None:
        if "treasure-map" not in self.state.inventory:
            raise RejectedAction("The treasure map is not in inventory")
        self.state.map_inspected = True
        self._record("route-clue-read")

    def take_forest_branch(self, direction: str) -> None:
        if not self.state.map_inspected:
            raise RejectedAction("The carried route clue has not been inspected")
        if self.state.treasure_clearing_reached:
            raise RejectedAction("The treasure clearing has already been reached")
        expected = self.route[self.state.route_progress]
        if direction != expected:
            raise RejectedAction("The branch does not match the next clue direction")
        self.state.route_progress += 1
        self._record(f"branch-{self.state.route_progress}-{direction}")
        if self.state.route_progress == len(self.route):
            self.state.treasure_clearing_reached = True
            self._record("treasure-clearing-reached")

    def use_shovel_on_x(self) -> None:
        if not self.state.treasure_clearing_reached:
            raise RejectedAction("The marked treasure clearing has not been reached")
        if "shovel" not in self.state.inventory:
            raise RejectedAction("The fixed X requires the bought shovel")
        if self.state.proof_acquired:
            raise RejectedAction("The treasure-trial proof was already acquired")
        self.state.inventory.add("treasure-huntery-t-shirt")
        self.state.proof_acquired = True
        self._record("treasure-proof-acquired")


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid prerequisite or route was accepted")


def main() -> None:
    invalid = TreasureTrialControl()
    expect_rejected(invalid.perform_circus_stunt, "requires the pot")
    expect_rejected(invalid.buy_map, "still locked")
    expect_rejected(invalid.buy_shovel, "Insufficient")
    expect_rejected(invalid.inspect_map, "not in inventory")
    invalid.collect_pot()
    invalid.perform_circus_stunt()
    expect_rejected(invalid.perform_circus_stunt, "requires the pot")
    expect_rejected(
        lambda: invalid.answer_map_seller("cousin-sven"),
        "does not unlock",
    )
    invalid.answer_map_seller("barber-dominique")
    invalid.buy_map()
    invalid.buy_shovel()
    expect_rejected(invalid.use_shovel_on_x, "not been reached")
    invalid.inspect_map()
    expect_rejected(lambda: invalid.take_forest_branch("left"), "does not match")

    control = TreasureTrialControl()
    control.collect_pot()
    control.perform_circus_stunt()
    control.answer_map_seller("barber-dominique")
    control.buy_map()
    control.buy_shovel()
    control.inspect_map()
    for branch in control.route:
        control.take_forest_branch(branch)
    control.use_shovel_on_x()

    assert control.state.proof_acquired
    assert control.state.pieces_of_eight == 303
    assert control.state.inventory == {
        "treasure-map",
        "shovel",
        "treasure-huntery-t-shirt",
    }
    assert control.state.route_progress == 9
    assert len(control.milestones) == 17
    print(
        "Secret of Monkey Island control verified: 17 milestones, fixed "
        "478/100/75 economy, nine clue-ordered branches, one proof token and "
        "eight rejected prerequisite or route violations."
    )


if __name__ == "__main__":
    main()
