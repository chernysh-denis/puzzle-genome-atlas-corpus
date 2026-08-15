#!/usr/bin/env python3
"""Verify the bounded projection-law route used by GAME-0092."""

from dataclasses import dataclass, field
from math import cos, radians, sin


Point = tuple[float, float, float]

START_END: Point = (1.0, 0.0, 0.0)
REMOTE_START: Point = (3.0, 0.0, 2.0)
GAP_LEFT: Point = (4.0, 0.0, 2.0)
GAP_RIGHT: Point = (5.0, 0.0, 2.0)
OCCLUDER: Point = (4.5, 0.0, 0.0)
ECHOES = ("E1", "E2")
ALIGNMENT_TOLERANCE = 1e-6


def projection(point: Point, yaw_degrees: float) -> tuple[float, float, float]:
    """Return horizontal screen position, height and camera-relative depth."""
    x, y, z = point
    angle = radians(yaw_degrees)
    screen_x = x * cos(angle) - z * sin(angle)
    depth = x * sin(angle) + z * cos(angle)
    return screen_x, y, depth


def visually_coincident(left: Point, right: Point, yaw_degrees: float) -> bool:
    lx, ly, _ = projection(left, yaw_degrees)
    rx, ry, _ = projection(right, yaw_degrees)
    return abs(lx - rx) <= ALIGNMENT_TOLERANCE and abs(ly - ry) <= ALIGNMENT_TOLERANCE


def gap_is_occluded(yaw_degrees: float, occluder: Point = OCCLUDER) -> bool:
    left_x, _, path_depth = projection(GAP_LEFT, yaw_degrees)
    right_x, _, _ = projection(GAP_RIGHT, yaw_degrees)
    cover_x, _, cover_depth = projection(occluder, yaw_degrees)
    low, high = sorted((left_x, right_x))
    return low < cover_x < high and cover_depth < path_depth


@dataclass
class PerspectiveRoute:
    yaw: float = 22.5
    paused: bool = True
    phase: str = "start"
    echoes: set[str] = field(default_factory=set)
    complete: bool = False

    def orbit(self, yaw_degrees: float) -> None:
        if not -180.0 <= yaw_degrees <= 180.0:
            raise ValueError("camera yaw is outside the bounded orbit")
        self.yaw = float(yaw_degrees)

    def steer_walker(self, destination: str) -> None:
        del destination
        raise ValueError("the Walker cannot be directly steered")

    def move_path(self, destination: Point) -> None:
        del destination
        raise ValueError("camera orbit cannot relocate fixed paths")

    def credit_echo(self, echo: str) -> None:
        del echo
        raise ValueError("echoes are credited only by Walker contact")

    def advance(self) -> None:
        if self.paused:
            raise ValueError("the Walker cannot advance in thinking mode")
        if self.phase == "start":
            if not visually_coincident(START_END, REMOTE_START, self.yaw):
                raise ValueError("remote endpoints do not coincide in projection")
            self.phase = "left"
            self.echoes.add("E1")
            return
        if self.phase == "left":
            if not gap_is_occluded(self.yaw):
                raise ValueError("the visible gap remains a discontinuity")
            self.phase = "right"
            self.echoes.add("E2")
            self.complete = self.echoes == set(ECHOES)
            return
        raise ValueError("the bounded route has no further transition")


def expect_rejection(operation, message: str) -> None:
    try:
        operation()
    except ValueError:
        return
    raise AssertionError(message)


def verify() -> None:
    fixed_geometry = (START_END, REMOTE_START, GAP_LEFT, GAP_RIGHT, OCCLUDER)
    route = PerspectiveRoute()

    unique_projections = {
        round(projection(REMOTE_START, yaw)[0], 6)
        for yaw in (0.0, 15.0, 30.0, 45.0, 60.0)
    }
    assert len(unique_projections) == 5, "orbit collapsed into four fixed views"

    expect_rejection(lambda: route.steer_walker("left"), "direct steering was accepted")
    expect_rejection(lambda: route.move_path((0.0, 0.0, 0.0)), "path relocation was accepted")
    expect_rejection(lambda: route.credit_echo("E1"), "remote echo credit was accepted")
    expect_rejection(route.advance, "Walker advanced while paused")

    route.paused = False
    expect_rejection(route.advance, "misaligned endpoints became connected")
    route.paused = True
    route.orbit(45.0)
    assert visually_coincident(START_END, REMOTE_START, route.yaw)
    route.paused = False
    route.advance()
    assert route.phase == "left" and route.echoes == {"E1"}

    expect_rejection(route.advance, "visible gap was crossed")
    assert not gap_is_occluded(0.0, (4.5, 0.0, 4.0)), (
        "an occluder behind the path hid the gap"
    )
    route.orbit(0.0)
    assert gap_is_occluded(route.yaw)
    route.advance()
    assert route.complete and route.echoes == set(ECHOES)
    assert fixed_geometry == (START_END, REMOTE_START, GAP_LEFT, GAP_RIGHT, OCCLUDER)

    incomplete = PerspectiveRoute(yaw=45.0, paused=False)
    incomplete.advance()
    assert not incomplete.complete, "one collected echo completed the route"

    print(
        "Echochrome control verified: five sampled orbit projections, one "
        "aligned-endpoint transfer, one occlusion-bridged gap, two contact "
        "echoes and six rejected invalid transitions."
    )


if __name__ == "__main__":
    verify()
