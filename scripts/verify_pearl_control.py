#!/usr/bin/env python3
"""Independently decode and verify the canonical GAME-0081 Pearl control."""

from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path


CONTROL_ID = "8x8dt:BbBaWaBeWdWWkBbBdBbBeWWkWaB"
EXPECTED_SOLUTION = "955C955CA9CA35CAAAAA956AAAA36956AA35C35CAA95600AAAA9C00A36363556"
RIGHT, UP, LEFT, DOWN = 1, 2, 4, 8
OPPOSITE = {RIGHT: LEFT, UP: DOWN, LEFT: RIGHT, DOWN: UP}
DELTAS = {RIGHT: (0, 1), UP: (-1, 0), LEFT: (0, -1), DOWN: (1, 0)}
STRAIGHTS = frozenset((RIGHT | LEFT, UP | DOWN))
CORNERS = frozenset((LEFT | UP, LEFT | DOWN, RIGHT | UP, RIGHT | DOWN))
STATES = frozenset((0, *STRAIGHTS, *CORNERS))


def decode_control(game_id: str = CONTROL_ID) -> tuple[int, int, tuple[str, ...]]:
    params, description = game_id.split(":", 1)
    dimensions = params.split("d", 1)[0]
    width, height = (int(value) for value in dimensions.split("x", 1))
    clues: list[str] = []
    for token in description:
        if "a" <= token <= "z":
            clues.extend("." for _ in range(ord(token) - ord("a") + 1))
        elif token in "BW":
            clues.append(token)
        else:
            raise ValueError(f"unknown description token {token!r}")
    if len(clues) != width * height:
        raise ValueError(f"decoded {len(clues)} cells, expected {width * height}")
    return width, height, tuple(clues)


def neighbour(cell: int, direction: int, width: int, height: int) -> int | None:
    row, column = divmod(cell, width)
    dr, dc = DELTAS[direction]
    row, column = row + dr, column + dc
    return row * width + column if 0 <= row < height and 0 <= column < width else None


def compatible(
    cell: int,
    state: int,
    adjacent: int,
    adjacent_state: int,
    direction: int,
    clues: tuple[str, ...],
) -> bool:
    linked = bool(state & direction)
    if linked != bool(adjacent_state & OPPOSITE[direction]):
        return False
    if linked and clues[cell] == "B" and adjacent_state not in STRAIGHTS:
        return False
    if linked and clues[adjacent] == "B" and state not in STRAIGHTS:
        return False
    return True


def initial_domains(width: int, height: int, clues: tuple[str, ...]) -> list[set[int]]:
    domains: list[set[int]] = []
    for cell, clue in enumerate(clues):
        domain = set(CORNERS if clue == "B" else STRAIGHTS if clue == "W" else STATES)
        for state in tuple(domain):
            if any(state & direction and neighbour(cell, direction, width, height) is None for direction in DELTAS):
                domain.remove(state)
        domains.append(domain)
    return domains


def propagate(domains: list[set[int]], width: int, height: int, clues: tuple[str, ...]) -> bool:
    changed = True
    while changed:
        changed = False
        for cell in range(width * height):
            for direction in DELTAS:
                adjacent = neighbour(cell, direction, width, height)
                if adjacent is None:
                    continue
                revised = {
                    state for state in domains[cell]
                    if any(compatible(cell, state, adjacent, other, direction, clues) for other in domains[adjacent])
                }
                if not revised:
                    return False
                if revised != domains[cell]:
                    domains[cell] = revised
                    changed = True

        for cell, clue in enumerate(clues):
            if clue != "W":
                continue
            revised = set()
            for state in domains[cell]:
                directions = [direction for direction in DELTAS if state & direction]
                if any(
                    any(
                        other in CORNERS and compatible(cell, state, adjacent, other, direction, clues)
                        for other in domains[adjacent]
                    )
                    for direction in directions
                    if (adjacent := neighbour(cell, direction, width, height)) is not None
                ):
                    revised.add(state)
            if not revised:
                return False
            if revised != domains[cell]:
                domains[cell] = revised
                changed = True
    return True


def one_cycle(solution: tuple[int, ...], width: int, height: int, clues: tuple[str, ...]) -> bool:
    used = {cell for cell, state in enumerate(solution) if state}
    if not used or any(clues[cell] != "." and cell not in used for cell in range(width * height)):
        return False
    start = next(iter(used))
    seen = {start}
    pending = [start]
    while pending:
        cell = pending.pop()
        state = solution[cell]
        if bin(state).count("1") != 2:
            return False
        for direction in DELTAS:
            if not state & direction:
                continue
            adjacent = neighbour(cell, direction, width, height)
            if adjacent is None or not solution[adjacent] & OPPOSITE[direction]:
                return False
            if adjacent not in seen:
                seen.add(adjacent)
                pending.append(adjacent)
    return seen == used


def clue_rules(solution: tuple[int, ...], width: int, height: int, clues: tuple[str, ...]) -> bool:
    for cell, clue in enumerate(clues):
        state = solution[cell]
        if clue == "B":
            if state not in CORNERS:
                return False
            for direction in DELTAS:
                if state & direction:
                    adjacent = neighbour(cell, direction, width, height)
                    if adjacent is None or solution[adjacent] not in STRAIGHTS:
                        return False
        elif clue == "W":
            if state not in STRAIGHTS:
                return False
            adjacent_states = [
                solution[adjacent]
                for direction in DELTAS
                if state & direction and (adjacent := neighbour(cell, direction, width, height)) is not None
            ]
            if not any(adjacent_state in CORNERS for adjacent_state in adjacent_states):
                return False
    return True


def solve(width: int, height: int, clues: tuple[str, ...], limit: int = 2) -> tuple[tuple[int, ...], ...]:
    solutions: list[tuple[int, ...]] = []

    def search(domains: list[set[int]]) -> None:
        if len(solutions) >= limit or not propagate(domains, width, height, clues):
            return
        undecided = [cell for cell, domain in enumerate(domains) if len(domain) > 1]
        if not undecided:
            solution = tuple(next(iter(domain)) for domain in domains)
            if one_cycle(solution, width, height, clues) and clue_rules(solution, width, height, clues):
                solutions.append(solution)
            return
        cell = min(undecided, key=lambda item: len(domains[item]))
        for state in sorted(domains[cell]):
            branch = [set(domain) for domain in domains]
            branch[cell] = {state}
            search(branch)

    search(initial_domains(width, height, clues))
    return tuple(solutions)


def coordinate(cell: int, width: int) -> str:
    row, column = divmod(cell, width)
    return f"{chr(ord('A') + row)}{column + 1}"


def verified_payload() -> dict[str, object]:
    width, height, clues = decode_control()
    solutions = solve(width, height, clues)
    assert len(solutions) == 1, f"expected one solution, found {len(solutions)}"
    solution = solutions[0]
    solution_text = "".join(f"{state:X}" for state in solution)
    assert solution_text == EXPECTED_SOLUTION
    assert one_cycle(solution, width, height, clues)
    assert clue_rules(solution, width, height, clues)
    black = [coordinate(cell, width) for cell, clue in enumerate(clues) if clue == "B"]
    white = [coordinate(cell, width) for cell, clue in enumerate(clues) if clue == "W"]
    used_cells = [coordinate(cell, width) for cell, state in enumerate(solution) if state]
    edge_count = sum(bin(state).count("1") for state in solution) // 2
    assert len(black) == 8
    assert len(white) == 7
    assert len(used_cells) == 60
    assert edge_count == 60
    return {
        "control_id": CONTROL_ID,
        "width": width,
        "height": height,
        "black_clues": black,
        "white_clues": white,
        "black_clue_count": len(black),
        "white_clue_count": len(white),
        "solution": solution_text,
        "solution_count": len(solutions),
        "used_cells": used_cells,
        "used_cell_count": len(used_cells),
        "edge_count": edge_count,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--export", type=Path)
    args = parser.parse_args()
    payload = verified_payload()
    if args.export:
        args.export.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        "Pearl control verified: 8x8 Tricky, 8 black and 7 white clues, "
        "one 60-cell/60-edge loop, unique solution."
    )


if __name__ == "__main__":
    main()
