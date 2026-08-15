#!/usr/bin/env python3
"""Verify the reproducible GAME-0072 Tents control and its unique solution."""

from __future__ import annotations

from functools import lru_cache

WIDTH = 8
HEIGHT = 8
DESCRIPTION = "badecbgbin_ab,1,2,1,0,3,1,2,2,3,0,3,0,2,1,1,2"


def decode() -> tuple[frozenset[int], tuple[int, ...], tuple[int, ...]]:
    grid_description, *number_text = DESCRIPTION.split(",")
    grid: list[str] = []
    for symbol in grid_description:
        if symbol == "_":
            run, cell = 0, "T"
        elif "a" <= symbol < "z":
            run, cell = ord(symbol) - ord("a") + 1, "T"
        elif symbol == "z":
            run, cell = 25, "."
        else:
            raise AssertionError(f"unsupported grid symbol: {symbol}")
        grid.extend("." * run)
        if len(grid) == WIDTH * HEIGHT:
            assert cell == "T"
            break
        if cell == "T":
            grid.append(cell)

    assert len(grid) == WIDTH * HEIGHT
    numbers = tuple(map(int, number_text))
    assert len(numbers) == WIDTH + HEIGHT
    trees = frozenset(index for index, cell in enumerate(grid) if cell == "T")
    return trees, numbers[:WIDTH], numbers[WIDTH:]


TREES, COLUMN_QUOTAS, ROW_QUOTAS = decode()


def orthogonal(first: int, second: int) -> bool:
    first_row, first_column = divmod(first, WIDTH)
    second_row, second_column = divmod(second, WIDTH)
    return abs(first_row - second_row) + abs(first_column - second_column) == 1


def touching(first: int, second: int) -> bool:
    first_row, first_column = divmod(first, WIDTH)
    second_row, second_column = divmod(second, WIDTH)
    return max(abs(first_row - second_row), abs(first_column - second_column)) <= 1


CANDIDATES = frozenset(
    cell
    for cell in range(WIDTH * HEIGHT)
    if cell not in TREES and any(orthogonal(cell, tree) for tree in TREES)
)


def has_perfect_matching(tents: frozenset[int]) -> bool:
    """Return whether every tree can be paired bijectively with one tent."""

    neighbours = {
        tree: tuple(tent for tent in tents if orthogonal(tree, tent))
        for tree in TREES
    }
    ordered_trees = tuple(sorted(TREES, key=lambda tree: len(neighbours[tree])))

    @lru_cache(maxsize=None)
    def match(index: int, used: frozenset[int]) -> bool:
        if index == len(ordered_trees):
            return True
        return any(
            tent not in used and match(index + 1, used | {tent})
            for tent in neighbours[ordered_trees[index]]
        )

    return match(0, frozenset())


def row_options(row: int) -> tuple[frozenset[int], ...]:
    candidates = sorted(cell for cell in CANDIDATES if cell // WIDTH == row)
    quota = ROW_QUOTAS[row]
    options: list[frozenset[int]] = []

    def choose(offset: int, selected: tuple[int, ...]) -> None:
        if len(selected) == quota:
            option = frozenset(selected)
            if all(not touching(first, second) for first in option for second in option if first < second):
                options.append(option)
            return
        if len(candidates) - offset < quota - len(selected):
            return
        for index in range(offset, len(candidates)):
            choose(index + 1, selected + (candidates[index],))

    choose(0, ())
    return tuple(options)


ROW_OPTIONS = tuple(row_options(row) for row in range(HEIGHT))


def solve(limit: int = 2) -> tuple[frozenset[int], ...]:
    solutions: list[frozenset[int]] = []

    def search(row: int, tents: frozenset[int], columns: tuple[int, ...]) -> None:
        if len(solutions) >= limit:
            return
        if row == HEIGHT:
            if columns == COLUMN_QUOTAS and len(tents) == len(TREES) and has_perfect_matching(tents):
                solutions.append(tents)
            return

        remaining_rows = HEIGHT - row - 1
        for option in ROW_OPTIONS[row]:
            if any(touching(tent, placed) for tent in option for placed in tents):
                continue
            next_columns = list(columns)
            for tent in option:
                next_columns[tent % WIDTH] += 1
            if any(next_columns[column] > COLUMN_QUOTAS[column] for column in range(WIDTH)):
                continue
            if any(next_columns[column] + remaining_rows < COLUMN_QUOTAS[column] for column in range(WIDTH)):
                continue
            search(row + 1, tents | option, tuple(next_columns))

    search(0, frozenset(), (0,) * WIDTH)
    return tuple(solutions)


def rows(tents: frozenset[int]) -> tuple[str, ...]:
    return tuple(
        "".join("T" if cell in TREES else "A" if cell in tents else "." for cell in range(row * WIDTH, (row + 1) * WIDTH))
        for row in range(HEIGHT)
    )


def main() -> None:
    assert len(TREES) == 12
    assert sum(ROW_QUOTAS) == sum(COLUMN_QUOTAS) == len(TREES)
    solutions = solve(limit=2)
    assert len(solutions) == 1

    solution = solutions[0]
    assert has_perfect_matching(solution)
    assert all(sum(cell // WIDTH == row for cell in solution) == ROW_QUOTAS[row] for row in range(HEIGHT))
    assert all(sum(cell % WIDTH == column for cell in solution) == COLUMN_QUOTAS[column] for column in range(WIDTH))
    assert all(not touching(first, second) for first in solution for second in solution if first < second)

    # Local adjacency alone is insufficient: this proposed set has one tent
    # beside every tree but cannot bijectively match all twelve pairs.
    ambiguous = frozenset({1, 3, 8, 14, 18, 21, 29, 32, 42, 49, 57, 60})
    assert len(ambiguous) == len(TREES)
    assert all(any(orthogonal(tree, tent) for tent in ambiguous) for tree in TREES)
    assert not has_perfect_matching(ambiguous)

    print("Tents GAME-0072 control verified")
    print("trees:", len(TREES), "tents:", len(solution), "unique solutions:", len(solutions))
    print("column quotas:", COLUMN_QUOTAS)
    print("row quotas:", ROW_QUOTAS)
    print("solution:")
    print("\n".join(rows(solution)))


if __name__ == "__main__":
    main()
