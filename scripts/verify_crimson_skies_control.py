#!/usr/bin/env python3
"""Verify the bounded original-Xbox Crimson Skies first-mission model."""

from __future__ import annotations

from dataclasses import dataclass


class RejectedAction(ValueError):
    """An action was attempted outside the sourced packet or current state."""


@dataclass
class SortieState:
    phase: str = "follow-betty"
    armour: int = 100
    special_energy: int = 100
    magnetic_missiles: int = 12
    checkpoint: str = "first-control"
    practice_zeppelins: int = 3
    training_towers: int = 3
    harbour_towers: int = 2
    current_wave_targets: int = 0
    wave: int = 0
    pandora_recaptured: bool = False
    upgrade_tokens: int = 0
    control_locus: str = "devastator"


class MorningAfterControl:
    def __init__(self) -> None:
        self.state = SortieState()
        self.milestones = ["first-devastator-control"]

    def follow_betty(self) -> None:
        if self.state.phase != "follow-betty":
            raise RejectedAction("Betty follow is not current")
        self.state.phase = "primary-practice"
        self.state.checkpoint = "training-island"
        self.milestones.append("betty-followed")

    def fire_primary(self) -> None:
        if self.state.phase not in {"primary-practice", "fighter-wave"}:
            raise RejectedAction("No eligible primary target is current")
        if self.state.phase == "primary-practice":
            self.state.practice_zeppelins -= 1
            if self.state.practice_zeppelins == 0:
                self.state.phase = "secondary-practice"
            return
        self.state.current_wave_targets -= 1
        if self.state.current_wave_targets == 0:
            if self.state.wave == 1:
                self.state.wave = 2
                self.state.current_wave_targets = 2
                self.milestones.append("second-wave-arrived")
            else:
                self.state.phase = "pandora-return"
                self.state.checkpoint = "harbour-cleared"

    def fire_magnetic_missile(self) -> None:
        if self.state.phase not in {"secondary-practice", "harbour-towers"}:
            raise RejectedAction("No eligible magnetic-missile target is current")
        if self.state.magnetic_missiles <= 0:
            raise RejectedAction("Finite secondary reserve is empty")
        self.state.magnetic_missiles -= 1
        if self.state.phase == "secondary-practice":
            self.state.training_towers -= 1
            if self.state.training_towers == 0:
                self.state.phase = "flight-lessons"
                self.state.checkpoint = "weapons-complete"
            return
        self.state.harbour_towers -= 1
        if self.state.harbour_towers == 0:
            self.state.phase = "fighter-wave"
            self.state.wave = 1
            self.state.current_wave_targets = 2

    def use_flight_lesson(self, lesson: str) -> None:
        if self.state.phase != "flight-lessons":
            raise RejectedAction("Flight lessons are not current")
        costs = {"brakes": 0, "immelmann": 20, "barrel-roll": 20, "turbo": 30}
        if lesson not in costs:
            raise RejectedAction("Unknown first-mission lesson")
        cost = costs[lesson]
        if cost > self.state.special_energy:
            raise RejectedAction("Shared special-energy reserve is insufficient")
        self.state.special_energy -= cost
        self.milestones.append(f"lesson:{lesson}")
        taught = {item.removeprefix("lesson:") for item in self.milestones if item.startswith("lesson:")}
        if taught == set(costs):
            self.state.phase = "harbour-towers"
            self.state.checkpoint = "flight-lessons-complete"

    def recover_special_energy(self, amount: int) -> None:
        if amount <= 0:
            raise RejectedAction("Recovery must be positive")
        self.state.special_energy = min(100, self.state.special_energy + amount)

    def take_damage(self, amount: int) -> None:
        if amount <= 0:
            raise RejectedAction("Damage must be positive")
        self.state.armour = max(0, self.state.armour - amount)
        if self.state.armour == 0:
            checkpoint = self.state.checkpoint
            self.state.armour = 100
            self.milestones.append(f"restored:{checkpoint}")

    def enter_pandora(self) -> None:
        if self.state.phase != "pandora-return":
            raise RejectedAction("Pandora return marker is not eligible")
        self.state.phase = "pandora-interior"
        self.state.control_locus = "pandora"
        self.state.pandora_recaptured = True
        self.state.upgrade_tokens += 1
        self.milestones.append("morning-after-settled")


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid Crimson Skies transition was accepted")


def complete_route(route: MorningAfterControl) -> None:
    expect_rejected(route.enter_pandora, "not eligible")
    route.follow_betty()
    for _ in range(3):
        route.fire_primary()
    for _ in range(3):
        route.fire_magnetic_missile()
    for lesson in ("brakes", "immelmann", "barrel-roll"):
        route.use_flight_lesson(lesson)
    assert route.state.special_energy == 60
    route.use_flight_lesson("turbo")
    assert route.state.special_energy == 30
    route.recover_special_energy(30)
    for _ in range(2):
        route.fire_magnetic_missile()
    assert route.state.phase == "fighter-wave"
    for _ in range(4):
        route.fire_primary()
    assert route.state.phase == "pandora-return"
    route.enter_pandora()


def main() -> None:
    route = MorningAfterControl()
    complete_route(route)
    assert route.state.pandora_recaptured
    assert route.state.upgrade_tokens == 1
    assert route.state.control_locus == "pandora"

    failure = MorningAfterControl()
    failure.follow_betty()
    failure.take_damage(100)
    assert failure.state.armour == 100
    assert failure.milestones[-1] == "restored:training-island"
    assert not failure.state.pandora_recaptured

    depleted = MorningAfterControl()
    depleted.follow_betty()
    depleted.state.phase = "secondary-practice"
    depleted.state.magnetic_missiles = 0
    expect_rejected(depleted.fire_magnetic_missile, "empty")
    depleted.state.phase = "flight-lessons"
    depleted.state.special_energy = 10
    expect_rejected(lambda: depleted.use_flight_lesson("immelmann"), "insufficient")

    print("Crimson Skies The Morning After bounded control model passed.")


if __name__ == "__main__":
    main()
