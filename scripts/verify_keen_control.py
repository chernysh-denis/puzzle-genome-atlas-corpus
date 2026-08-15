#!/usr/bin/env python3
"""Independently decode and verify the canonical GAME-0080 Keen control."""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass
from pathlib import Path


CONTROL_ID = "6dn:a__a__a_14ba4_a4ca__a__b__,d3a9m180d3s1d3a11a7m10s1s2d3m24a9s4m12"
EXPECTED_SOLUTION = "624513415236531624246351362145153462"


@dataclass(frozen=True)
class Cage:
    operation: str
    target: int
    cells: tuple[int, ...]


class DisjointSet:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def merge(self, left: int, right: int) -> None:
        left, right = self.find(left), self.find(right)
        if left != right:
            self.parent[max(left, right)] = min(left, right)


def decode_control(game_id: str = CONTROL_ID) -> tuple[int, tuple[Cage, ...]]:
    params, description = game_id.split(":", 1)
    width = int(params.split("d", 1)[0])
    structure, clues_text = description.split(",", 1)
    expanded: list[int] = []
    index = 0
    while index < len(structure):
        token = structure[index]
        if token != "_" and not "a" <= token <= "z":
            raise ValueError(f"invalid structure token {token!r}")
        run = 0 if token == "_" else ord(token) - ord("a") + 1
        index += 1
        start = index
        while index < len(structure) and structure[index].isdigit():
            index += 1
        repeat = int(structure[start:index]) if index > start else 1
        expanded.extend([run] * repeat)

    dsu = DisjointSet(width * width)
    position = 0
    for run in expanded:
        advance = run != 25
        for _ in range(run):
            if position >= 2 * width * (width - 1):
                raise ValueError("structure exceeds the grid")
            if position < width * (width - 1):
                row, column = divmod(position, width - 1)
                left = row * width + column
                right = left + 1
            else:
                column, row = divmod(position - width * (width - 1), width - 1)
                left = row * width + column
                right = left + width
            dsu.merge(left, right)
            position += 1
        if advance:
            position += 1
    if position != 2 * width * (width - 1) + 1:
        raise ValueError("incomplete block structure")

    members: dict[int, list[int]] = {}
    for cell in range(width * width):
        members.setdefault(dsu.find(cell), []).append(cell)

    cages: list[Cage] = []
    cursor = 0
    for root in sorted(members):
        operation = clues_text[cursor]
        if operation not in "amsd":
            raise ValueError(f"invalid clue operation {operation!r}")
        cursor += 1
        start = cursor
        while cursor < len(clues_text) and clues_text[cursor].isdigit():
            cursor += 1
        if start == cursor:
            raise ValueError("clue target is missing")
        cages.append(Cage(operation, int(clues_text[start:cursor]), tuple(members[root])))
    if cursor != len(clues_text):
        raise ValueError("unused clue text")
    return width, tuple(cages)


def cage_satisfied(cage: Cage, values: list[int]) -> bool:
    digits = [values[cell] for cell in cage.cells]
    if 0 in digits:
        return False
    if cage.operation == "a":
        return sum(digits) == cage.target
    if cage.operation == "m":
        product = 1
        for digit in digits:
            product *= digit
        return product == cage.target
    if cage.operation == "s":
        return len(digits) == 2 and abs(digits[0] - digits[1]) == cage.target
    if cage.operation == "d":
        high, low = max(digits), min(digits)
        return len(digits) == 2 and high % low == 0 and high // low == cage.target
    raise AssertionError(cage.operation)


def solve(width: int, cages: tuple[Cage, ...], limit: int = 2) -> tuple[tuple[int, ...], ...]:
    board = [0] * (width * width)
    by_cell = {cell: cage for cage in cages for cell in cage.cells}
    row_options = tuple(itertools.permutations(range(1, width + 1)))
    solutions: list[tuple[int, ...]] = []

    def partial_cage_possible(cage: Cage) -> bool:
        digits = [board[cell] for cell in cage.cells]
        assigned = [digit for digit in digits if digit]
        missing = len(digits) - len(assigned)
        if not missing:
            return cage_satisfied(cage, board)
        if cage.operation == "a":
            return sum(assigned) + missing <= cage.target <= sum(assigned) + missing * width
        if cage.operation == "m":
            product = 1
            for digit in assigned:
                product *= digit
            return product <= cage.target and cage.target % product == 0
        return True

    def search(row: int) -> None:
        if len(solutions) >= limit:
            return
        if row == width:
            if all(cage_satisfied(cage, board) for cage in cages):
                solutions.append(tuple(board))
            return
        offset = row * width
        for option in row_options:
            if any(option[column] in board[column:offset:width] for column in range(width)):
                continue
            board[offset:offset + width] = option
            affected = {by_cell[offset + column] for column in range(width)}
            if all(partial_cage_possible(cage) for cage in affected):
                search(row + 1)
            board[offset:offset + width] = [0] * width

    search(0)
    return tuple(solutions)


def coordinate(cell: int, width: int) -> str:
    row, column = divmod(cell, width)
    return f"{chr(ord('A') + row)}{column + 1}"


def verified_payload() -> dict[str, object]:
    width, cages = decode_control()
    solutions = solve(width, cages)
    assert len(solutions) == 1, f"expected one solution, found {len(solutions)}"
    solution = solutions[0]
    assert "".join(map(str, solution)) == EXPECTED_SOLUTION
    assert all(cage_satisfied(cage, list(solution)) for cage in cages)
    assert all(
        set(solution[row * width:(row + 1) * width]) == set(range(1, width + 1))
        for row in range(width)
    )
    assert all(
        {solution[row * width + column] for row in range(width)} == set(range(1, width + 1))
        for column in range(width)
    )
    operation_counts = {
        operation: sum(cage.operation == operation for cage in cages)
        for operation in "amsd"
    }
    assert len(cages) == 16
    assert operation_counts == {"a": 4, "m": 4, "s": 4, "d": 4}
    return {
        "control_id": CONTROL_ID,
        "width": width,
        "solution": "".join(map(str, solution)),
        "solution_count": len(solutions),
        "cage_count": len(cages),
        "operation_counts": operation_counts,
        "cages": [
            {
                "operation": cage.operation,
                "target": cage.target,
                "cells": [coordinate(cell, width) for cell in cage.cells],
            }
            for cage in cages
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--export", type=Path)
    args = parser.parse_args()
    payload = verified_payload()
    if args.export:
        args.export.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        "Keen control verified: 6x6 Normal, 16 connected arithmetic cages "
        "using +, ×, − and ÷, Latin rows and columns, unique solution."
    )


if __name__ == "__main__":
    main()
