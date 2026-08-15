#!/usr/bin/env python3
"""Verify the reproducible GAME-0066 Black Box control field."""

from __future__ import annotations

SIZE = 8
BALLS = {(2, 0), (0, 3), (3, 5), (4, 5), (6, 7)}
SIDES = ("T", "R", "B", "L")


def left(direction: tuple[int, int]) -> tuple[int, int]:
    dx, dy = direction
    return dy, -dx


def right(direction: tuple[int, int]) -> tuple[int, int]:
    dx, dy = direction
    return -dy, dx


def entry_state(side: str, index: int) -> tuple[int, int, int, int]:
    return {
        "T": (index, -1, 0, 1),
        "R": (SIZE, index, -1, 0),
        "B": (index, SIZE, 0, -1),
        "L": (-1, index, 1, 0),
    }[side]


def exit_name(x: int, y: int) -> str:
    if y < 0:
        return f"T{x + 1}"
    if y >= SIZE:
        return f"B{x + 1}"
    if x < 0:
        return f"L{y + 1}"
    return f"R{y + 1}"


def outcome(side: str, index: int) -> str:
    x, y, dx, dy = entry_state(side, index)
    entry = f"{side}{index + 1}"

    forward = (x + dx, y + dy)
    lx, ly = left((dx, dy))
    rx, ry = right((dx, dy))
    if forward in BALLS:
        return "H"
    if (forward[0] + lx, forward[1] + ly) in BALLS:
        return "R"
    if (forward[0] + rx, forward[1] + ry) in BALLS:
        return "R"

    x, y = forward
    for _ in range(256):
        if x < 0 or x >= SIZE or y < 0 or y >= SIZE:
            exit_port = exit_name(x, y)
            return "R" if exit_port == entry else exit_port

        forward = (x + dx, y + dy)
        lx, ly = left((dx, dy))
        rx, ry = right((dx, dy))
        if forward in BALLS:
            return "H"
        if (forward[0] + lx, forward[1] + ly) in BALLS:
            dx, dy = right((dx, dy))
        elif (forward[0] + rx, forward[1] + ry) in BALLS:
            dx, dy = left((dx, dy))
        else:
            x, y = forward

    raise AssertionError(f"non-terminating ray from {entry}")


def main() -> None:
    results = {
        f"{side}{index + 1}": outcome(side, index)
        for side in SIDES
        for index in range(SIZE)
    }
    assert len(BALLS) == 5
    assert len(results) == 32
    assert results["T1"] == "H"
    assert results["T2"] == "R"
    assert results["T6"] == "R5" and results["R5"] == "T6"
    assert results["R3"] == "L2" and results["L2"] == "R3"
    assert results["B3"] == "L7" and results["L7"] == "B3"

    hits = sum(value == "H" for value in results.values())
    reflections = sum(value == "R" for value in results.values())
    endpoints = len(results) - hits - reflections
    assert (hits, reflections, endpoints) == (18, 6, 8)
    for entry, result in results.items():
        if result not in {"H", "R"}:
            assert results[result] == entry

    print("Black Box control verified: 32 rays, 18 H, 6 R, 4 paired exits")


if __name__ == "__main__":
    main()
