#!/usr/bin/env python3
"""Verify the reproducible GAME-0069 Lights Out control board over GF(2)."""

from __future__ import annotations

SIZE = 5
CELL_COUNT = SIZE * SIZE
OFF = 0
ON = 1


def index(row: int, column: int) -> int:
    return row * SIZE + column


def press_mask(row: int, column: int) -> int:
    mask = 0
    for delta_row, delta_column in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
        target_row = row + delta_row
        target_column = column + delta_column
        if 0 <= target_row < SIZE and 0 <= target_column < SIZE:
            mask ^= 1 << index(target_row, target_column)
    return mask


PRESS_MASKS = tuple(
    press_mask(row, column)
    for row in range(SIZE)
    for column in range(SIZE)
)


def apply(board: int, presses: tuple[int, ...]) -> int:
    for position in presses:
        board ^= PRESS_MASKS[position]
    return board


def row_reduce(rows: list[int], width: int) -> tuple[list[int], tuple[int, ...]]:
    rows = rows[:]
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(width):
        candidate = next(
            (row for row in range(pivot_row, len(rows)) if rows[row] >> column & 1),
            None,
        )
        if candidate is None:
            continue
        rows[pivot_row], rows[candidate] = rows[candidate], rows[pivot_row]
        for row in range(len(rows)):
            if row != pivot_row and rows[row] >> column & 1:
                rows[row] ^= rows[pivot_row]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return rows, tuple(pivot_columns)


def solve(board: int) -> tuple[int, ...]:
    """Return every press mask solving board -> all off."""
    equations = []
    for cell in range(CELL_COUNT):
        coefficients = sum(
            ((PRESS_MASKS[press] >> cell) & 1) << press
            for press in range(CELL_COUNT)
        )
        equations.append(coefficients | (((board >> cell) & 1) << CELL_COUNT))

    reduced, pivots = row_reduce(equations, CELL_COUNT)
    coefficient_mask = (1 << CELL_COUNT) - 1
    for equation in reduced:
        if equation & coefficient_mask == 0 and equation >> CELL_COUNT & 1:
            return ()

    free = tuple(column for column in range(CELL_COUNT) if column not in pivots)
    solutions: list[int] = []
    for assignment in range(1 << len(free)):
        solution = sum(
            ((assignment >> offset) & 1) << column
            for offset, column in enumerate(free)
        )
        for equation, pivot in reversed(list(zip(reduced, pivots))):
            rhs = equation >> CELL_COUNT & 1
            parity = bin(equation & coefficient_mask & solution).count("1") & 1
            if parity != rhs:
                solution ^= 1 << pivot
        solutions.append(solution)
    return tuple(
        sorted(solutions, key=lambda value: (bin(value).count("1"), value))
    )


def coordinates(mask: int) -> tuple[str, ...]:
    return tuple(
        f"{chr(ord('A') + position // SIZE)}{position % SIZE + 1}"
        for position in range(CELL_COUNT)
        if mask >> position & 1
    )


def main() -> None:
    matrix_rows = [
        sum(((PRESS_MASKS[press] >> cell) & 1) << press for press in range(CELL_COUNT))
        for cell in range(CELL_COUNT)
    ]
    _, pivots = row_reduce(matrix_rows, CELL_COUNT)
    assert len(pivots) == 23

    control_presses = tuple(
        index(row, column)
        for row, column in (
            (0, 0),
            (0, 4),
            (1, 2),
            (2, 1),
            (2, 3),
            (3, 2),
            (4, 0),
            (4, 4),
        )
    )
    control_board = apply(OFF, control_presses)
    expected_rows = (
        "11111",
        "10101",
        "11011",
        "10101",
        "11111",
    )
    expected_board = sum(
        int(value) << index(row, column)
        for row, values in enumerate(expected_rows)
        for column, value in enumerate(values)
    )
    assert control_board == expected_board
    assert apply(control_board, control_presses) == OFF
    assert apply(control_board, tuple(reversed(control_presses))) == OFF
    assert apply(control_board, (index(2, 2), index(2, 2))) == control_board

    solutions = solve(control_board)
    assert len(solutions) == 4
    assert bin(solutions[0]).count("1") == 8
    assert coordinates(sum(1 << position for position in control_presses)) in {
        coordinates(solution) for solution in solutions
    }
    assert (
        "A1", "A5", "B3", "C2", "C4", "D3", "E1", "E5"
    ) in {coordinates(solution) for solution in solutions}

    single_corner = 1 << index(0, 0)
    assert solve(single_corner) == ()
    assert 2 ** len(pivots) == 8_388_608
    assert 2 ** CELL_COUNT - 2 ** len(pivots) == 25_165_824

    print(
        "Lights Out control verified: rank 23, 8,388,608 reachable states, "
        "four control solutions, minimum 8 presses, single-corner state unreachable"
    )


if __name__ == "__main__":
    main()
