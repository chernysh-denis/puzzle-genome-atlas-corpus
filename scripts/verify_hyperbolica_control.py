#!/usr/bin/env python3
"""Verify a bounded curved-space maze control inspired by Hyperbolica."""

from __future__ import annotations

from dataclasses import dataclass, field
from math import cosh, isclose, pi, sinh
from typing import Callable, Tuple


ROUTE = ("R", "L", "R", "L", "L", "L", "L", "R", "L", "L", "R")


def boost_x(distance: float, point: tuple[float, float, float]) -> tuple[float, float, float]:
    t, x, y = point
    return (cosh(distance) * t + sinh(distance) * x,
            sinh(distance) * t + cosh(distance) * x,
            y)


def boost_y(distance: float, point: tuple[float, float, float]) -> tuple[float, float, float]:
    t, x, y = point
    return (cosh(distance) * t + sinh(distance) * y,
            x,
            sinh(distance) * t + cosh(distance) * y)


def minkowski_norm(point: tuple[float, float, float]) -> float:
    t, x, y = point
    return t * t - x * x - y * y


@dataclass
class MazeControl:
    decisions: list[str] = field(default_factory=list)
    crystal_collected: bool = False

    def turn(self, direction: str) -> None:
        if direction not in {"L", "R"}:
            raise ValueError("maze decision must be left or right")
        expected = ROUTE[len(self.decisions)] if len(self.decisions) < len(ROUTE) else None
        if direction != expected:
            raise ValueError("turn leaves the bounded verified route")
        self.decisions.append(direction)

    def collect_crystal(self) -> None:
        if tuple(self.decisions) != ROUTE:
            raise ValueError("hexahedron is not reached before the full route")
        self.crystal_collected = True


def reject(label: str, operation: Callable[[], None]) -> str:
    try:
        operation()
    except ValueError:
        return label
    raise AssertionError("invalid transition was accepted: %s" % label)


def require_five_square_vertex(face_count: int) -> None:
    interior_angle = 2.0 * pi / 5.0
    if face_count != 5 or not isclose(face_count * interior_angle, 2.0 * pi):
        raise ValueError("the scoped {4,5} vertex requires five 72-degree squares")


def require_negative_curvature(radius: float) -> None:
    hyperbolic_circumference = 2.0 * pi * sinh(radius)
    euclidean_circumference = 2.0 * pi * radius
    if radius <= 0 or hyperbolic_circumference <= euclidean_circumference:
        raise ValueError("space did not grow faster than the flat control")


def require_noncommuting_translations(distance: float) -> None:
    origin = (1.0, 0.0, 0.0)
    xy = boost_y(distance, boost_x(distance, origin))
    yx = boost_x(distance, boost_y(distance, origin))
    if all(isclose(a, b) for a, b in zip(xy, yx)):
        raise ValueError("curved translations incorrectly commute")
    if not isclose(minkowski_norm(xy), 1.0) or not isclose(minkowski_norm(yx), 1.0):
        raise AssertionError("Lorentz boosts must preserve the hyperboloid")


def verify() -> Tuple[int, float, Tuple[str, ...]]:
    rejected = []

    require_five_square_vertex(5)
    require_negative_curvature(2.0)
    require_noncommuting_translations(0.7)

    maze = MazeControl()
    for decision in ROUTE:
        maze.turn(decision)
    maze.collect_crystal()
    assert maze.crystal_collected

    rejected.append(reject("flat-four-square-vertex", lambda: require_five_square_vertex(4)))
    rejected.append(reject("zero-curvature-growth", lambda: require_negative_curvature(0.0)))
    rejected.append(reject("wrong-first-turn", lambda: MazeControl().turn("L")))
    rejected.append(reject("unknown-turn", lambda: MazeControl().turn("F")))
    rejected.append(reject("early-crystal", lambda: MazeControl().collect_crystal()))
    rejected.append(reject("truncated-route", lambda: truncated_control().collect_crystal()))

    if len(rejected) != 6 or len(set(rejected)) != 6:
        raise AssertionError("expected six distinct rejected controls")
    expansion = sinh(2.0) / 2.0
    return len(ROUTE), expansion, tuple(rejected)


def truncated_control() -> MazeControl:
    maze = MazeControl()
    for decision in ROUTE[:-1]:
        maze.turn(decision)
    return maze


if __name__ == "__main__":
    decisions, expansion_ratio, rejected_controls = verify()
    print(
        "Hyperbolica control verified: one {4,5} vertex, negative-curvature "
        "circumference %.6fx the flat control, %d maze decisions, one crystal "
        "arrival and %d rejected invalid controls."
        % (expansion_ratio, decisions, len(rejected_controls))
    )
