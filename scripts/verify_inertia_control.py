#!/usr/bin/env python3
"""Verify the reproducible GAME-0070 Inertia control board and safe route."""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass

WIDTH = 10
HEIGHT = 8
DESCRIPTION = (
    "sggsbgsgsg"
    "mggwwmbbmm"
    "swggsmwwws"
    "bbwgmsbwgm"
    "swwbbbbwSm"
    "gsmwbwgsgw"
    "msssmmmgbw"
    "gsbbmsmbwm"
)

# Matches inertia.c: north, north-east, east, south-east, south,
# south-west, west, north-west.
DIRECTIONS = (
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
)
CONTROL_ROUTE = tuple(int(direction) for direction in "044506054661700142572222")


@dataclass(frozen=True)
class State:
    position: int
    gems: int
    dead: bool = False


def coordinates(position: int) -> str:
    return f"{chr(ord('A') + position // WIDTH)}{position % WIDTH + 1}"


def step(state: State, direction: int) -> tuple[State, tuple[int, ...]] | None:
    if state.dead:
        return None

    dx, dy = DIRECTIONS[direction]
    x, y = state.position % WIDTH, state.position // WIDTH
    next_x, next_y = x + dx, y + dy
    if not (0 <= next_x < WIDTH and 0 <= next_y < HEIGHT):
        return None
    if DESCRIPTION[next_y * WIDTH + next_x] == "w":
        return None

    gems = state.gems
    traversed: list[int] = []
    while True:
        x += dx
        y += dy
        position = y * WIDTH + x
        traversed.append(position)
        cell = DESCRIPTION[position]
        if cell == "g":
            gems &= ~(1 << position)
        if cell == "m":
            return State(position, gems, True), tuple(traversed)

        next_x, next_y = x + dx, y + dy
        blocked_ahead = (
            not (0 <= next_x < WIDTH and 0 <= next_y < HEIGHT)
            or DESCRIPTION[next_y * WIDTH + next_x] == "w"
        )
        if cell in "sS" or blocked_ahead:
            return State(position, gems), tuple(traversed)


def solve(start: State) -> tuple[int, ...]:
    queue = deque([start])
    predecessor: dict[State, tuple[State, int] | None] = {start: None}
    goal: State | None = None

    while queue:
        state = queue.popleft()
        if state.gems == 0:
            goal = state
            break
        for direction in range(len(DIRECTIONS)):
            result = step(state, direction)
            if result is None or result[0].dead:
                continue
            successor = result[0]
            if successor not in predecessor:
                predecessor[successor] = (state, direction)
                queue.append(successor)

    assert goal is not None
    route: list[int] = []
    while predecessor[goal] is not None:
        previous, direction = predecessor[goal]
        route.append(direction)
        goal = previous
    return tuple(reversed(route))


def main() -> None:
    assert len(DESCRIPTION) == WIDTH * HEIGHT
    counts = Counter(DESCRIPTION)
    assert counts == Counter({"s": 16, "g": 16, "m": 16, "w": 16, "b": 15, "S": 1})

    start_position = DESCRIPTION.index("S")
    initial_gems = sum(1 << index for index, cell in enumerate(DESCRIPTION) if cell == "g")
    initial = State(start_position, initial_gems)

    state = initial
    traversed_gems = 0
    for direction in CONTROL_ROUTE:
        result = step(state, direction)
        assert result is not None
        next_state, path = result
        assert not next_state.dead
        traversed_gems += bin(state.gems ^ next_state.gems).count("1")
        state = next_state
    assert state.gems == 0
    assert traversed_gems == 16

    shortest = solve(initial)
    assert shortest == CONTROL_ROUTE
    assert len(shortest) == 24

    # From the start at E9, north first collects the gem at D9 and stops at D9.
    first = step(initial, 0)
    assert first is not None
    assert tuple(map(coordinates, first[1])) == ("D9",)
    assert bin(first[0].gems).count("1") == 15

    # North-east from E9 immediately enters the visible mine at D10.
    fatal = step(initial, 1)
    assert fatal is not None
    assert tuple(map(coordinates, fatal[1])) == ("D10",)
    assert fatal[0].dead

    # North-west is rejected because the adjacent cell D8 is a wall.
    assert step(initial, 7) is None

    print("Inertia GAME-0070 control verified")
    print("cell counts:", dict(sorted(counts.items())))
    print("safe route length:", len(CONTROL_ROUTE))
    print("safe route:", "".join(map(str, CONTROL_ROUTE)))
    print("final position:", coordinates(state.position))


if __name__ == "__main__":
    main()
