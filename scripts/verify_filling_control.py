#!/usr/bin/env python3
"""Independently decode and verify the canonical GAME-0079 Filling control."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


CONTROL_ID = "13x9:7b424d7a4b77a4b3c4d3c7a43a6c2c5b73b646b5a47b888a6a3b7a77d8a7b8e4a2a3578e3b5e22"
EXPECTED_SOLUTION = (
    "7444244377744"
    "7477244337744"
    "7774333577433"
    "6664226554473"
    "6664666554771"
    "8884663337777"
    "8888837778888"
    "4442233578888"
    "4333555577722"
)


def decode_control(game_id: str = CONTROL_ID) -> tuple[int, int, tuple[int, ...]]:
    params, description = game_id.split(":", 1)
    width, height = (int(value) for value in params.split("x", 1))
    clues: list[int] = []
    for token in description:
        if token.isdigit():
            clues.append(int(token))
        elif "a" <= token <= "z":
            clues.extend([0] * (ord(token) - ord("a") + 1))
        else:
            raise ValueError(f"unknown description token {token!r}")
    if len(clues) != width * height:
        raise ValueError(f"decoded {len(clues)} cells, expected {width * height}")
    return width, height, tuple(clues)


def neighbours(cell: int, width: int, height: int) -> tuple[int, ...]:
    row, column = divmod(cell, width)
    result = []
    for nr, nc in ((row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)):
        if 0 <= nr < height and 0 <= nc < width:
            result.append(nr * width + nc)
    return tuple(result)


def components(board: list[int], width: int, height: int) -> tuple[tuple[int, frozenset[int]], ...]:
    seen = set()
    result = []
    for start, value in enumerate(board):
        if value == 0 or start in seen:
            continue
        region = {start}
        pending = [start]
        seen.add(start)
        while pending:
            cell = pending.pop()
            for adjacent in neighbours(cell, width, height):
                if adjacent not in seen and board[adjacent] == value:
                    seen.add(adjacent)
                    region.add(adjacent)
                    pending.append(adjacent)
        result.append((value, frozenset(region)))
    return tuple(result)


def valid_partial(board: list[int], width: int, height: int) -> bool:
    for value, region in components(board, width, height):
        if len(region) > value:
            return False
        reachable = set(region)
        pending = list(region)
        while pending and len(reachable) < value:
            cell = pending.pop()
            for adjacent in neighbours(cell, width, height):
                if adjacent not in reachable and board[adjacent] in (0, value):
                    reachable.add(adjacent)
                    pending.append(adjacent)
        if len(reachable) < value:
            return False
    return True


def domain(board: list[int], cell: int, width: int, height: int) -> tuple[int, ...]:
    options = []
    for value in range(1, 10):
        board[cell] = value
        if valid_partial(board, width, height):
            options.append(value)
    board[cell] = 0
    return tuple(options)


def solve(width: int, height: int, clues: tuple[int, ...], limit: int = 2) -> tuple[tuple[int, ...], ...]:
    board = list(clues)
    solutions: list[tuple[int, ...]] = []

    def search() -> None:
        if len(solutions) >= limit:
            return
        forced: list[tuple[int, int]] = []
        while True:
            best_cell = -1
            best_domain: tuple[int, ...] | None = None
            for cell, value in enumerate(board):
                if value:
                    continue
                options = domain(board, cell, width, height)
                if not options:
                    for changed, _ in reversed(forced):
                        board[changed] = 0
                    return
                if best_domain is None or len(options) < len(best_domain):
                    best_cell, best_domain = cell, options
                    if len(options) == 1:
                        break
            if best_domain is None:
                if all(len(region) == value for value, region in components(board, width, height)):
                    solutions.append(tuple(board))
                for changed, _ in reversed(forced):
                    board[changed] = 0
                return
            if len(best_domain) != 1:
                break
            board[best_cell] = best_domain[0]
            forced.append((best_cell, best_domain[0]))
            if not valid_partial(board, width, height):
                for changed, _ in reversed(forced):
                    board[changed] = 0
                return

        assert best_domain is not None
        for value in best_domain:
            board[best_cell] = value
            search()
            board[best_cell] = 0
        for changed, _ in reversed(forced):
            board[changed] = 0

    if not valid_partial(board, width, height):
        return ()
    search()
    return tuple(solutions)


def coordinate(cell: int, width: int) -> str:
    row, column = divmod(cell, width)
    return f"{chr(ord('A') + row)}{column + 1}"


def verified_payload() -> dict[str, object]:
    width, height, clues = decode_control()
    solutions = solve(width, height, clues)
    assert len(solutions) == 1, f"expected one solution, found {len(solutions)}"
    solution = solutions[0]
    solution_text = "".join(str(value) for value in solution)
    assert solution_text == EXPECTED_SOLUTION
    assert all(not clue or clue == solution[cell] for cell, clue in enumerate(clues))

    regions = components(list(solution), width, height)
    assert all(len(region) == value for value, region in regions)
    region_rows = []
    for value, region in regions:
        given_count = sum(bool(clues[cell]) for cell in region)
        region_rows.append(
            {
                "value": value,
                "cells": [coordinate(cell, width) for cell in sorted(region)],
                "given_count": given_count,
            }
        )
    clue_count = sum(bool(value) for value in clues)
    ghost_regions = [row for row in region_rows if row["given_count"] == 0]
    digit_region_counts = {
        str(value): sum(row["value"] == value for row in region_rows)
        for value in range(1, 10)
    }
    assert clue_count == 47
    assert len(regions) == 27
    assert len(ghost_regions) == 1
    assert ghost_regions[0]["value"] == 1
    assert ghost_regions[0]["cells"] == ["E13"]
    assert digit_region_counts == {
        "1": 1, "2": 4, "3": 6, "4": 6, "5": 2,
        "6": 2, "7": 4, "8": 2, "9": 0,
    }
    return {
        "control_id": CONTROL_ID,
        "width": width,
        "height": height,
        "clues": list(clues),
        "clue_count": clue_count,
        "solution": solution_text,
        "solution_count": len(solutions),
        "regions": region_rows,
        "region_count": len(regions),
        "digit_region_counts": digit_region_counts,
        "ghost_regions": ghost_regions,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--export", type=Path)
    args = parser.parse_args()
    payload = verified_payload()
    if args.export:
        args.export.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        "Filling control verified: 13x9, 47 immutable clues, 27 connected "
        "regions, one clue-free region, every region area equals its digit, "
        "unique solution."
    )


if __name__ == "__main__":
    main()
