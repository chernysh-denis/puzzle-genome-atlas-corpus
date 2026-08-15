#!/usr/bin/env python3
"""Verify the bounded fixed-platform projection route used by GAME-0091."""

from dataclasses import dataclass
from enum import Enum


Point = tuple[int, int, int]


class View(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


SUPPORTS: dict[str, Point] = {
    "A": (0, 0, 0),
    "B": (1, 0, 0),
    "C": (1, 0, 1),
}


def projection(point: Point, view: View) -> tuple[int, int, int]:
    """Return screen-x, height and front-to-back depth for a cardinal view."""
    x, y, z = point
    if view is View.NORTH:
        return x, y, z
    if view is View.EAST:
        return z, y, -x
    if view is View.SOUTH:
        return -x, y, -z
    return -z, y, x


def active_supports(view: View) -> set[str]:
    """Keep the frontmost solid support at each settled screen position."""
    rows: dict[tuple[int, int], tuple[int, str]] = {}
    for name, point in SUPPORTS.items():
        screen_x, height, depth = projection(point, view)
        key = (screen_x, height)
        if key not in rows or depth < rows[key][0]:
            rows[key] = (depth, name)
    return {name for _, name in rows.values()}


def adjacent(left: str, right: str, view: View) -> bool:
    active = active_supports(view)
    if left not in active or right not in active:
        return False
    lx, ly, _ = projection(SUPPORTS[left], view)
    rx, ry, _ = projection(SUPPORTS[right], view)
    return ly == ry and abs(lx - rx) == 1


@dataclass
class ProjectionRoute:
    avatar: str = "A"
    view: View = View.NORTH
    rotating: bool = False
    reached: bool = False

    def begin_rotation(self, quarter_turns: int) -> None:
        if quarter_turns not in (-1, 1):
            raise ValueError("only one cardinal quarter-turn is legal")
        if self.rotating:
            raise ValueError("a second rotation cannot begin mid-transition")
        self.rotating = True
        self.view = View((self.view.value + quarter_turns) % 4)

    def settle_rotation(self) -> None:
        if not self.rotating:
            raise ValueError("no view transition is active")
        if self.avatar not in active_supports(self.view):
            raise ValueError("avatar has no front-layer support in the new view")
        self.rotating = False

    def move(self, destination: str) -> None:
        if self.rotating:
            raise ValueError("movement is suspended during view rotation")
        if destination not in SUPPORTS:
            raise ValueError("unknown support")
        if not adjacent(self.avatar, destination, self.view):
            raise ValueError("destination is not adjacent in the active projection")
        self.avatar = destination
        self.reached = destination == "C"

    def move_support(self, name: str, destination: Point) -> None:
        del name, destination
        raise ValueError("view rotation cannot relocate fixed world geometry")


def expect_rejection(operation, message: str) -> None:
    try:
        operation()
    except ValueError:
        return
    raise AssertionError(message)


def verify() -> None:
    assert active_supports(View.NORTH) == {"A", "B"}
    assert active_supports(View.EAST) == {"B", "C"}
    original_geometry = dict(SUPPORTS)

    route = ProjectionRoute()
    expect_rejection(lambda: route.move("C"), "hidden support accepted as reachable")
    expect_rejection(lambda: route.begin_rotation(2), "half-turn accepted atomically")
    expect_rejection(
        lambda: route.move_support("B", (1, 0, 1)),
        "camera command relocated world geometry",
    )

    route.move("B")
    route.begin_rotation(1)
    expect_rejection(lambda: route.move("C"), "movement continued mid-rotation")
    expect_rejection(
        lambda: route.begin_rotation(1),
        "second rotation began before the first settled",
    )
    route.settle_rotation()
    expect_rejection(lambda: route.move("A"), "occluded far support remained active")
    route.move("C")

    assert SUPPORTS == original_geometry, "projection route mutated fixed supports"
    assert route.reached, "projection-relinked route did not reach its target"
    assert route.view is View.EAST

    cycle = View.NORTH
    for _ in range(4):
        cycle = View((cycle.value + 1) % 4)
    assert len(View) == 4 and cycle is View.NORTH, (
        "four quarter-turns did not close the view cycle"
    )

    print(
        "Fez control verified: three fixed supports, four cardinal views, "
        "one projection-relinked route and six rejected invalid transitions."
    )


if __name__ == "__main__":
    verify()
