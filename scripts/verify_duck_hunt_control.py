#!/usr/bin/env python3
"""Verify the bounded original-NES Duck Hunt Game A first round."""

from __future__ import annotations

from dataclasses import dataclass, field


class RejectedAction(ValueError):
    """An action was attempted outside the documented round rules."""


@dataclass
class TargetOpportunity:
    colour: str
    path: tuple[tuple[int, int], ...]
    shot_limit: int = 3
    shots_used: int = 0
    elapsed_ticks: int = 0
    hit: bool = False
    settled: bool = False


@dataclass
class RoundState:
    target_index: int = 0
    hits: int = 0
    misses: int = 0
    score: int = 0
    hit_lamps: list[bool] = field(default_factory=lambda: [False] * 10)
    result: str | None = None


class DuckHuntRoundControl:
    target_count = 10
    pass_line = 6
    escape_ticks = 8
    score_by_colour = {"black": 500, "blue": 1000, "red": 1500}
    perfect_bonus = 10_000

    def __init__(self) -> None:
        self.state = RoundState()
        self.current: TargetOpportunity | None = None
        self.milestones: list[str] = []

    def release_target(
        self, colour: str, path: tuple[tuple[int, int], ...]
    ) -> None:
        if self.state.result is not None:
            raise RejectedAction("The first-round packet is already settled")
        if self.current is not None and not self.current.settled:
            raise RejectedAction("The current duck opportunity is unresolved")
        if self.state.target_index >= self.target_count:
            raise RejectedAction("All ten first-round ducks have been presented")
        if colour not in self.score_by_colour:
            raise RejectedAction("The duck colour is outside the sourced table")
        if len(path) < self.escape_ticks:
            raise RejectedAction("The flight path does not cover the opportunity")
        self.current = TargetOpportunity(colour=colour, path=path)
        self.milestones.append(f"duck-{self.state.target_index + 1}-released")

    def advance(self, ticks: int = 1) -> None:
        target = self._active_target()
        if ticks <= 0:
            raise RejectedAction("Time advance must be positive")
        target.elapsed_ticks += ticks
        if target.elapsed_ticks >= self.escape_ticks:
            self._settle_miss("timeout")

    def fire_sensor_shot(self, sampled_position: tuple[int, int] | None) -> None:
        target = self._active_target()
        if target.shots_used >= target.shot_limit:
            raise RejectedAction("No shot remains in this duck opportunity")
        target.shots_used += 1
        target_position = target.path[min(target.elapsed_ticks, self.escape_ticks - 1)]
        if sampled_position == target_position:
            target.hit = True
            target.settled = True
            self.state.hits += 1
            self.state.hit_lamps[self.state.target_index] = True
            self.state.score += self.score_by_colour[target.colour]
            self.milestones.append(
                f"duck-{self.state.target_index + 1}-hit-shot-{target.shots_used}"
            )
            self._finish_target()
        elif target.shots_used == target.shot_limit:
            self._settle_miss("shots-exhausted")
        else:
            self.milestones.append(
                f"duck-{self.state.target_index + 1}-miss-shot-{target.shots_used}"
            )

    def _active_target(self) -> TargetOpportunity:
        if self.current is None or self.current.settled:
            raise RejectedAction("No unresolved duck is currently available")
        return self.current

    def _settle_miss(self, reason: str) -> None:
        target = self._active_target()
        target.settled = True
        self.state.misses += 1
        self.milestones.append(
            f"duck-{self.state.target_index + 1}-miss-{reason}"
        )
        self._finish_target()

    def _finish_target(self) -> None:
        self.state.target_index += 1
        if self.state.target_index == self.target_count:
            if self.state.hits == self.target_count:
                self.state.score += self.perfect_bonus
                self.milestones.append("perfect-bonus")
            self.state.result = "advance" if self.state.hits >= self.pass_line else "game-over"
            self.milestones.append(f"round-{self.state.result}")


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid round action was accepted")


def path(seed: int) -> tuple[tuple[int, int], ...]:
    """Provide a reproducible eight-sample carrier path for one duck."""

    return tuple((seed + tick, seed + (tick * 2) % 5) for tick in range(8))


def main() -> None:
    invalid = DuckHuntRoundControl()
    expect_rejected(lambda: invalid.fire_sensor_shot((0, 0)), "No unresolved")
    expect_rejected(lambda: invalid.release_target("green", path(0)), "colour")
    expect_rejected(lambda: invalid.release_target("black", ((0, 0),)), "does not cover")

    passing = DuckHuntRoundControl()
    colours = ("black", "blue", "red", "black", "blue", "red", "black", "blue", "red", "black")
    for index, colour in enumerate(colours):
        target_path = path(index * 10)
        passing.release_target(colour, target_path)
        if index < 6:
            if index == 0:
                passing.fire_sensor_shot(None)
                passing.advance()
                passing.fire_sensor_shot(target_path[1])
            else:
                passing.fire_sensor_shot(target_path[0])
        elif index == 6:
            passing.fire_sensor_shot(None)
            passing.fire_sensor_shot(None)
            passing.fire_sensor_shot(None)
        else:
            passing.advance(passing.escape_ticks)

    assert passing.state.hits == passing.pass_line
    assert passing.state.misses == 4
    assert passing.state.result == "advance"
    assert passing.state.hit_lamps == [True] * 6 + [False] * 4
    assert passing.state.score == 6000
    expect_rejected(lambda: passing.release_target("black", path(100)), "already settled")

    failing = DuckHuntRoundControl()
    for index in range(10):
        target_path = path(index * 10)
        failing.release_target("black", target_path)
        if index < 5:
            failing.fire_sensor_shot(target_path[0])
        else:
            failing.advance(failing.escape_ticks)
    assert failing.state.hits == 5
    assert failing.state.result == "game-over"

    perfect = DuckHuntRoundControl()
    for index in range(10):
        target_path = path(index * 10)
        perfect.release_target("red", target_path)
        perfect.fire_sensor_shot(target_path[0])
    assert perfect.state.result == "advance"
    assert perfect.state.score == 25_000
    assert "perfect-bonus" in perfect.milestones

    print(
        "Duck Hunt control verified: ten sequential targets, three-shot or "
        "timeout settlement, six-hit PASS LINE, failure below quota, "
        "colour scoring, perfect bonus and six rejected invalid actions."
    )


if __name__ == "__main__":
    main()
