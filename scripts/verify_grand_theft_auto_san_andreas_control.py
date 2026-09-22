#!/usr/bin/env python3
"""Verify the bounded original-PS2 GTA: San Andreas opening model."""

from __future__ import annotations

from dataclasses import dataclass


class RejectedAction(ValueError):
    """An action was attempted outside the sourced packet or current state."""


@dataclass
class OpeningState:
    phase: str = "rollin-heights-control"
    health: int = 100
    on_bicycle: bool = False
    bicycle_available: bool = True
    cycling_progress: int = 0
    wanted_stars: int = 0
    police_perception: bool = False
    unseen_ticks: int = 0
    current_leader: str | None = None
    grove_marker_reached: bool = False
    respect_awarded: bool = False
    johnson_house_available: bool = False
    ryder_unlocked: bool = False


class SanAndreasControl:
    def __init__(self) -> None:
        self.state = OpeningState()
        self.milestones = ["fresh-rollin-heights-control"]

    def mount_bicycle(self) -> None:
        if not self.state.bicycle_available:
            raise RejectedAction("No usable bicycle is accessible")
        if self.state.health == 0:
            raise RejectedAction("CJ is Wasted")
        self.state.on_bicycle = True

    def pedal(self, effort: int = 1) -> None:
        if not self.state.on_bicycle:
            raise RejectedAction("CJ is not on a bicycle")
        if effort <= 0:
            raise RejectedAction("Pedal effort must be positive")
        self.state.cycling_progress += effort

    def collide(self, damage: int) -> None:
        if damage <= 0:
            raise RejectedAction("Collision damage must be positive")
        self.state.health = max(0, self.state.health - damage)
        self.state.on_bicycle = False
        if self.state.health == 0:
            self.state.phase = "wasted"

    def observed_offence(self, stars: int = 1) -> None:
        if stars < 1 or stars > 6:
            raise RejectedAction("Wanted tier is outside the sourced scale")
        self.state.wanted_stars = max(self.state.wanted_stars, stars)
        self.state.police_perception = True
        self.state.unseen_ticks = 0

    def evade_tick(self, *, seen: bool) -> None:
        if self.state.wanted_stars == 0:
            raise RejectedAction("No wanted level is active")
        self.state.police_perception = seen
        if seen:
            self.state.unseen_ticks = 0
            return
        self.state.unseen_ticks += 1
        if self.state.wanted_stars <= 3 and self.state.unseen_ticks >= 3:
            self.state.wanted_stars = 0
            self.state.unseen_ticks = 0

    def reach_grove_street(self) -> None:
        if not self.state.on_bicycle:
            raise RejectedAction("The opening route has not retained bicycle control")
        self.state.grove_marker_reached = True
        self.state.phase = "big-smoke-transition"
        self.milestones.append("grove-street-marker")

    def begin_sweet_and_kendl(self) -> None:
        if self.state.phase != "big-smoke-transition":
            raise RejectedAction("Big Smoke transition has not settled")
        self.state.phase = "sweet-route"
        self.state.on_bicycle = False
        self.state.current_leader = "Sweet"
        self.milestones.append("cemetery-bicycle-route")

    def follow_current_leader(self, leader: str) -> None:
        if not self.state.on_bicycle:
            raise RejectedAction("CJ must mount the supplied bicycle")
        if self.state.current_leader != leader:
            raise RejectedAction("Authored leader order was violated")
        if leader == "Sweet":
            self.state.current_leader = "Ryder"
            self.state.phase = "ryder-route"
            self.milestones.append("sweet-to-ryder-handoff")
        elif leader == "Ryder":
            self.state.current_leader = None
            self.state.phase = "final-grove-marker"
            self.milestones.append("ryder-route-complete")
        else:
            raise RejectedAction("Unknown opening leader")

    def settle_mission(self) -> None:
        if self.state.phase != "final-grove-marker" or self.state.health == 0:
            raise RejectedAction("Final Grove Street marker is not eligible")
        self.state.phase = "grove-successor-control"
        self.state.respect_awarded = True
        self.state.johnson_house_available = True
        self.state.ryder_unlocked = True
        self.milestones.append("sweet-and-kendl-settled")

    def arrested(self) -> None:
        if self.state.wanted_stars == 0:
            raise RejectedAction("No police pressure can produce arrest")
        self.state.phase = "busted"


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid opening transition was accepted")


def main() -> None:
    route = SanAndreasControl()
    expect_rejected(route.pedal, "not on")
    route.mount_bicycle()
    route.pedal(3)
    assert route.state.cycling_progress == 3
    route.reach_grove_street()
    route.begin_sweet_and_kendl()
    route.mount_bicycle()
    expect_rejected(lambda: route.follow_current_leader("Ryder"), "order")
    route.follow_current_leader("Sweet")
    route.follow_current_leader("Ryder")
    route.settle_mission()
    assert route.state.phase == "grove-successor-control"
    assert route.state.respect_awarded
    assert route.state.johnson_house_available
    assert route.state.ryder_unlocked

    law = SanAndreasControl()
    law.observed_offence(1)
    law.evade_tick(seen=False)
    law.evade_tick(seen=True)
    assert law.state.wanted_stars == 1
    for _ in range(3):
        law.evade_tick(seen=False)
    assert law.state.wanted_stars == 0

    arrested = SanAndreasControl()
    arrested.observed_offence(1)
    arrested.arrested()
    assert arrested.state.phase == "busted"

    collision = SanAndreasControl()
    collision.mount_bicycle()
    collision.collide(25)
    assert collision.state.health == 75
    assert not collision.state.on_bicycle
    collision.mount_bicycle()
    collision.collide(75)
    assert collision.state.phase == "wasted"

    print("Grand Theft Auto: San Andreas bounded control model passed.")


if __name__ == "__main__":
    main()
