#!/usr/bin/env python3
"""Verify the bounded gravity-frame and world-wrap route used by GAME-0095."""

from __future__ import annotations

from dataclasses import dataclass


PERIOD = 12
GRAVITY_COLOURS = {
    (0, -1, 0): "blue",
    (0, 1, 0): "red",
    (-1, 0, 0): "orange",
    (1, 0, 0): "purple",
    (0, 0, -1): "green",
    (0, 0, 1): "yellow",
}


def add(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left + right for left, right in zip(a, b))


def wrap(position: tuple[int, int, int]) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    """Return the canonical local pose and crossed lattice-cell offset."""
    local = tuple(value % PERIOD for value in position)
    cell = tuple(value // PERIOD for value in position)
    return local, cell


@dataclass
class TutorialRoute:
    position: tuple[int, int, int] = (2, 1, 2)
    gravity: tuple[int, int, int] = (0, -1, 0)
    held_cube: str | None = None
    red_plate: bool = False
    blue_switch: bool = False
    exterior_reached: bool = False
    complete: bool = False

    @property
    def gravity_colour(self) -> str:
        return GRAVITY_COLOURS[self.gravity]

    def shift_gravity(self, surface_normal: tuple[int, int, int]) -> None:
        if surface_normal not in GRAVITY_COLOURS:
            raise ValueError("gravity must snap to one orthogonal world direction")
        self.gravity = surface_normal

    def pick_up_cube(self, colour: str) -> None:
        if self.held_cube is not None:
            raise ValueError("only one cube can be carried")
        if colour != self.gravity_colour:
            raise ValueError("cube is immovable outside its matching gravity frame")
        self.held_cube = colour

    def release_cube_on_plate(self, colour: str) -> None:
        if self.held_cube != colour:
            raise ValueError("matching held cube is required")
        if self.gravity_colour != colour:
            raise ValueError("plate placement requires the matching gravity frame")
        self.held_cube = None
        if colour == "red":
            self.red_plate = True

    def cross_periodic_gap(self, forward: tuple[int, int, int]) -> tuple[int, int, int]:
        if not self.red_plate:
            raise ValueError("tutorial door must be opened before the exterior crossing")
        unwrapped = add(add(self.position, tuple(axis * PERIOD for axis in self.gravity)), forward)
        local, cell = wrap(unwrapped)
        if cell == (0, 0, 0):
            raise ValueError("the route did not cross a periodic boundary")
        self.position = local
        self.exterior_reached = True
        return cell

    def press_blue_switch(self) -> None:
        if not self.exterior_reached or self.gravity_colour != "blue":
            raise ValueError("blue switch is reachable only after the wrapped blue-gravity crossing")
        self.blue_switch = True

    def enter_exit(self) -> None:
        if not self.blue_switch:
            raise ValueError("linked exit is closed")
        self.complete = True


def expect_rejection(operation, message: str) -> None:
    try:
        operation()
    except ValueError:
        return
    raise AssertionError(message)


def verify() -> None:
    route = TutorialRoute()

    assert len(GRAVITY_COLOURS) == 6
    assert len(set(GRAVITY_COLOURS.values())) == 6
    expect_rejection(
        lambda: route.shift_gravity((1, 1, 0)),
        "diagonal gravity frame was accepted",
    )
    expect_rejection(
        lambda: route.pick_up_cube("red"),
        "red cube moved under blue gravity",
    )
    expect_rejection(
        lambda: route.cross_periodic_gap((3, 0, 0)),
        "exterior crossing bypassed the tutorial door",
    )
    expect_rejection(route.press_blue_switch, "remote blue switch activated early")
    expect_rejection(route.enter_exit, "closed exit admitted the player")

    route.shift_gravity((0, 1, 0))
    assert route.gravity_colour == "red"
    route.pick_up_cube("red")
    route.release_cube_on_plate("red")
    assert route.red_plate

    route.shift_gravity((0, -1, 0))
    origin = route.position
    crossed_cell = route.cross_periodic_gap((3, 0, 0))
    assert crossed_cell == (0, -1, 0)
    assert route.position == (5, 1, 2)
    reverse_local, reverse_cell = wrap(add(route.position, (0, PERIOD, 0)))
    assert reverse_local == route.position
    assert reverse_cell == (0, 1, 0)
    assert origin != route.position

    expect_rejection(
        lambda: route.pick_up_cube("red"),
        "red cube remained movable after returning to blue gravity",
    )
    route.press_blue_switch()
    route.enter_exit()
    assert route.complete and route.blue_switch

    print(
        "Manifold Garden control verified: six orthogonal gravity frames, "
        "colour-gated cube handling, one lattice-preserving periodic crossing, "
        "one wrapped switch-to-exit route and six rejected invalid transitions."
    )


if __name__ == "__main__":
    verify()
