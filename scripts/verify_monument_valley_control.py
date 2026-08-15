#!/usr/bin/env python3
"""Verify the bounded snap-state route used by GAME-0093."""

from collections import deque
from dataclasses import dataclass, field
from math import cos, radians, sin
from typing import Optional


Point = tuple[float, float, float]

START: Point = (1.0, 0.0, 0.0)
GOAL: Point = (2.0, 0.0, 0.0)
PIVOT: Point = (1.5, 0.0, 2.0)
SNAP_ANGLES = (0, 90)
PROJECTION_TOLERANCE = 1e-6


def bridge_endpoints(angle_degrees: int) -> tuple[Point, Point]:
    """Rotate the two bridge endpoints about their shared world-space pivot."""
    angle = radians(angle_degrees)
    endpoints: list[Point] = []
    for offset in (-0.5, 0.5):
        endpoints.append(
            (
                PIVOT[0] + offset * cos(angle),
                PIVOT[1] + offset * sin(angle),
                PIVOT[2],
            )
        )
    return endpoints[0], endpoints[1]


def projection(point: Point) -> tuple[float, float]:
    """Return the fixed orthographic screen position used by the control."""
    return point[0], point[1]


def projected_match(left: Point, right: Point) -> bool:
    left_x, left_y = projection(left)
    right_x, right_y = projection(right)
    return (
        abs(left_x - right_x) <= PROJECTION_TOLERANCE
        and abs(left_y - right_y) <= PROJECTION_TOLERANCE
    )


def navigation_graph(angle_degrees: int) -> dict[str, set[str]]:
    if angle_degrees not in SNAP_ANGLES:
        raise ValueError("navigation graph is defined only at bridge snap states")

    bridge_left, bridge_right = bridge_endpoints(angle_degrees)
    graph = {node: set() for node in ("start", "bridge-left", "bridge-right", "goal")}
    graph["bridge-left"].add("bridge-right")
    graph["bridge-right"].add("bridge-left")

    for fixed_name, fixed_point in (("start", START), ("goal", GOAL)):
        for bridge_name, bridge_point in (
            ("bridge-left", bridge_left),
            ("bridge-right", bridge_right),
        ):
            if projected_match(fixed_point, bridge_point):
                graph[fixed_name].add(bridge_name)
                graph[bridge_name].add(fixed_name)
    return graph


def shortest_route(
    graph: dict[str, set[str]], start: str, goal: str
) -> Optional[list[str]]:
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, route = queue.popleft()
        if node == goal:
            return route
        for neighbour in sorted(graph[node]):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, route + [neighbour]))
    return None


@dataclass
class GardenPrelude:
    bridge_angle: int = 90
    settled: bool = True
    ida_node: str = "start"
    traversed: list[str] = field(default_factory=list)
    complete: bool = False

    def begin_bridge_rotation(self) -> None:
        if self.complete:
            raise ValueError("the completed bounded route is no longer editable")
        if not self.settled:
            raise ValueError("bridge is already between snap states")
        self.settled = False

    def settle_bridge(self, angle_degrees: int) -> None:
        if self.settled:
            raise ValueError("no bridge rotation is in progress")
        if angle_degrees not in SNAP_ANGLES:
            raise ValueError("bridge must settle at an authored snap angle")
        self.bridge_angle = angle_degrees
        self.settled = True

    def highlighted_destinations(self) -> set[str]:
        if not self.settled:
            return set()
        graph = navigation_graph(self.bridge_angle)
        return {
            node
            for node in graph
            if shortest_route(graph, self.ida_node, node) is not None
        }

    def step_ida(self, direction: str) -> None:
        del direction
        raise ValueError("Ida is commanded by destination, not by route step")

    def select_destination(self, destination: str) -> None:
        if not self.settled:
            raise ValueError("a destination cannot be selected during rotation")
        graph = navigation_graph(self.bridge_angle)
        if destination not in graph:
            raise ValueError("selected point is not a navigation node")
        route = shortest_route(graph, self.ida_node, destination)
        if route is None:
            raise ValueError("selected destination is not currently reachable")
        self.traversed = route
        self.ida_node = destination
        self.complete = destination == "goal"


def expect_rejection(operation, message: str) -> None:
    try:
        operation()
    except ValueError:
        return
    raise AssertionError(message)


def verify() -> None:
    control = GardenPrelude()
    initial_endpoints = bridge_endpoints(control.bridge_angle)

    assert control.highlighted_destinations() == {"start"}
    expect_rejection(lambda: control.step_ida("right"), "direct route step was accepted")
    expect_rejection(
        lambda: control.select_destination("goal"),
        "disconnected goal was accepted",
    )
    expect_rejection(
        lambda: control.select_destination("decoration"),
        "non-navigation decoration was accepted",
    )

    control.begin_bridge_rotation()
    assert control.highlighted_destinations() == set()
    expect_rejection(
        lambda: control.select_destination("goal"),
        "destination was accepted during bridge motion",
    )
    expect_rejection(
        lambda: control.settle_bridge(45),
        "unsupported intermediate angle became a decision state",
    )
    control.settle_bridge(0)

    connected_endpoints = bridge_endpoints(control.bridge_angle)
    assert connected_endpoints != initial_endpoints, "bridge geometry did not rotate"
    assert connected_endpoints[0][2] != START[2]
    assert connected_endpoints[1][2] != GOAL[2]
    assert projected_match(START, connected_endpoints[0])
    assert projected_match(GOAL, connected_endpoints[1])
    assert control.highlighted_destinations() == {
        "start",
        "bridge-left",
        "bridge-right",
        "goal",
    }

    control.select_destination("goal")
    assert control.traversed == ["start", "bridge-left", "bridge-right", "goal"]
    assert control.ida_node == "goal" and control.complete

    expect_rejection(control.begin_bridge_rotation, "completed route remained editable")

    print(
        "Monument Valley control verified: two bridge snap states, two "
        "screen-space joins across retained depth, one four-node automatic route, "
        "one highlighted reachable set and six rejected invalid transitions."
    )


if __name__ == "__main__":
    verify()
