#!/usr/bin/env python3
"""Independently decode and verify the canonical GAME-0082 Signpost control."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


CONTROL_ID = "4x4c:1dececcehbfghahc16a"
EXPECTED_SOLUTION = "S1d10e7c8e5c13c14e6h12b3f2g9h4a11h15c16a"
DIRECTIONS = (
    (0, -1), (1, -1), (1, 0), (1, 1),
    (0, 1), (-1, 1), (-1, 0), (-1, -1),
)


def decode_description(description: str, width: int, height: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    directions: list[int] = []
    givens: list[int] = []
    number = ""
    for token in description.removeprefix("S"):
        if token.isdigit():
            number += token
            continue
        if not "a" <= token <= "h":
            raise ValueError(f"unknown direction token {token!r}")
        directions.append(ord(token) - ord("a"))
        givens.append(int(number) if number else 0)
        number = ""
    if number:
        raise ValueError("number without a following direction")
    if len(directions) != width * height:
        raise ValueError(f"decoded {len(directions)} cells, expected {width * height}")
    return tuple(directions), tuple(givens)


def ray_targets(cell: int, direction: int, width: int, height: int) -> tuple[int, ...]:
    row, column = divmod(cell, width)
    dc, dr = DIRECTIONS[direction]
    targets: list[int] = []
    row += dr
    column += dc
    while 0 <= row < height and 0 <= column < width:
        targets.append(row * width + column)
        row += dr
        column += dc
    return tuple(targets)


def enumerate_solutions(
    directions: tuple[int, ...],
    givens: tuple[int, ...],
    width: int,
    height: int,
    limit: int = 2,
) -> tuple[tuple[int, ...], ...]:
    size = width * height
    fixed_by_number = {number: cell for cell, number in enumerate(givens) if number}
    if len(fixed_by_number) != sum(bool(number) for number in givens):
        raise ValueError("duplicate immutable number")
    solutions: list[tuple[int, ...]] = []

    def search(path: list[int], used: set[int]) -> None:
        if len(solutions) >= limit:
            return
        number = len(path)
        if number == size:
            solutions.append(tuple(path))
            return
        next_number = number + 1
        required = fixed_by_number.get(next_number)
        candidates = ray_targets(path[-1], directions[path[-1]], width, height)
        for candidate in candidates:
            if candidate in used or (required is not None and candidate != required):
                continue
            given = givens[candidate]
            if given and given != next_number:
                continue
            path.append(candidate)
            used.add(candidate)
            search(path, used)
            used.remove(candidate)
            path.pop()

    start = fixed_by_number.get(1)
    if start is None:
        raise ValueError("control lacks immutable 1")
    search([start], {start})
    return tuple(solutions)


def coordinate(cell: int, width: int) -> str:
    row, column = divmod(cell, width)
    return f"{chr(ord('A') + row)}{column + 1}"


def encoded_solution(path: tuple[int, ...], directions: tuple[int, ...], width: int) -> str:
    numbers = [0] * len(path)
    for number, cell in enumerate(path, 1):
        numbers[cell] = number
    return "S" + "".join(f"{numbers[cell]}{chr(ord('a') + directions[cell])}" for cell in range(len(path)))


def verified_payload() -> dict[str, object]:
    params, description = CONTROL_ID.split(":", 1)
    dimensions = params.removesuffix("c")
    width, height = (int(value) for value in dimensions.split("x", 1))
    directions, givens = decode_description(description, width, height)
    solutions = enumerate_solutions(directions, givens, width, height)
    assert len(solutions) == 1, f"expected one solution, found {len(solutions)}"
    path = solutions[0]
    assert encoded_solution(path, directions, width) == EXPECTED_SOLUTION
    assert sorted(path) == list(range(width * height))
    for number, cell in enumerate(path[:-1], 1):
        assert path[number] in ray_targets(cell, directions[cell], width, height)
    fixed = {number: coordinate(cell, width) for cell, number in enumerate(givens) if number}
    assert fixed == {1: "A1", 16: "D4"}
    return {
        "control_id": CONTROL_ID,
        "width": width,
        "height": height,
        "fixed_numbers": fixed,
        "solution": EXPECTED_SOLUTION,
        "solution_count": len(solutions),
        "path": [coordinate(cell, width) for cell in path],
        "path_length": len(path),
        "arrow_transitions": len(path) - 1,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--export", type=Path)
    args = parser.parse_args()
    payload = verified_payload()
    if args.export:
        args.export.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print("Signpost control verified: 4x4 corner-anchored, one unique 16-cell path with 15 arrow-ray transitions.")


if __name__ == "__main__":
    main()
