#!/usr/bin/env python3
"""Verify the reproducible GAME-0075 Light Up control and unique solution."""

from __future__ import annotations

DESCRIPTION = "e0a21c0w1c2BaBe"
WIDTH = HEIGHT = 7
EXPECTED_BULBS = (0, 9, 14, 27, 29, 39, 47)


def decode(description: str) -> tuple[str, ...]:
    cells: list[str] = []
    for token in description:
        if "a" <= token <= "z":
            cells.extend("." for _ in range(ord(token) - ord("a") + 1))
        elif token == "B" or token in "01234":
            cells.append(token)
        else:
            raise ValueError(f"Unexpected token: {token}")
    assert len(cells) == WIDTH * HEIGHT
    return tuple(cells)


BOARD = decode(DESCRIPTION)
WHITE = tuple(index for index, value in enumerate(BOARD) if value == ".")


def orthogonal(index: int) -> tuple[int, ...]:
    row, column = divmod(index, WIDTH)
    result = []
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        rr, cc = row + dr, column + dc
        if 0 <= rr < HEIGHT and 0 <= cc < WIDTH:
            result.append(rr * WIDTH + cc)
    return tuple(result)


def visible(index: int) -> frozenset[int]:
    row, column = divmod(index, WIDTH)
    result = {index}
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        rr, cc = row + dr, column + dc
        while 0 <= rr < HEIGHT and 0 <= cc < WIDTH:
            candidate = rr * WIDTH + cc
            if BOARD[candidate] != ".":
                break
            result.add(candidate)
            rr, cc = rr + dr, cc + dc
    return frozenset(result)


VISIBLE = {index: visible(index) for index in WHITE}
CLUES = tuple(
    (index, int(value), tuple(adj for adj in orthogonal(index) if BOARD[adj] == "."))
    for index, value in enumerate(BOARD)
    if value.isdigit()
)


def enumerate_solutions(limit: int = 2) -> list[tuple[int, ...]]:
    solutions: list[tuple[int, ...]] = []

    def search(assignment: dict[int, int]) -> None:
        changed = True
        while changed:
            changed = False
            for index, value in tuple(assignment.items()):
                if value != 1:
                    continue
                for other in VISIBLE[index] - {index}:
                    if assignment[other] == 1:
                        return
                    if assignment[other] < 0:
                        assignment[other] = 0
                        changed = True
            for _, target, adjacent in CLUES:
                placed = sum(assignment[index] == 1 for index in adjacent)
                undecided = [index for index in adjacent if assignment[index] < 0]
                if placed > target or placed + len(undecided) < target:
                    return
                forced = 0 if placed == target else 1 if placed + len(undecided) == target else None
                if forced is not None:
                    for index in undecided:
                        assignment[index] = forced
                        changed = True
            for index in WHITE:
                if any(assignment[source] == 1 for source in VISIBLE[index]):
                    continue
                candidates = [source for source in VISIBLE[index] if assignment[source] < 0]
                if not candidates:
                    return
                if len(candidates) == 1:
                    assignment[candidates[0]] = 1
                    changed = True

        if all(value >= 0 for value in assignment.values()):
            if all(any(assignment[source] == 1 for source in VISIBLE[index]) for index in WHITE):
                solutions.append(tuple(index for index in WHITE if assignment[index] == 1))
            return

        dark = min(
            (index for index in WHITE if not any(assignment[source] == 1 for source in VISIBLE[index])),
            key=lambda index: sum(assignment[source] < 0 for source in VISIBLE[index]),
        )
        chosen = next(source for source in VISIBLE[dark] if assignment[source] < 0)
        for value in (1, 0):
            branch = assignment.copy()
            branch[chosen] = value
            search(branch)
            if len(solutions) >= limit:
                return

    search({index: -1 for index in WHITE})
    return solutions


def coordinate(index: int) -> str:
    row, column = divmod(index, WIDTH)
    return f"{chr(65 + row)}{column + 1}"


def main() -> None:
    solutions = enumerate_solutions()
    assert len(WHITE) == 41
    assert len(CLUES) == 6
    assert len(solutions) == 1
    assert solutions[0] == EXPECTED_BULBS

    bulbs = set(solutions[0])
    assert all(any(source in bulbs for source in VISIBLE[index]) for index in WHITE)
    assert all(not ((VISIBLE[index] - {index}) & bulbs) for index in bulbs)
    assert all(sum(index in bulbs for index in adjacent) == target for _, target, adjacent in CLUES)

    # A wall blocks light: A1 sees A5 but not A7 beyond clue-0 wall A6.
    assert 4 in VISIBLE[0] and 6 not in VISIBLE[0]
    # Two bulbs can occupy visible cells while violating mutual exclusion.
    assert 0 in VISIBLE[4] and {0, 4}.issubset(WHITE)
    # A numbered wall is an exact local count, independent of illumination.
    clue_zero = next(adjacent for index, target, adjacent in CLUES if index == 5 and target == 0)
    assert 4 in clue_zero and sum(index in {4} for index in clue_zero) == 1

    print("Light Up GAME-0075 control verified")
    print("white:", len(WHITE), "walls:", 49 - len(WHITE), "clues:", len(CLUES), "unique solutions:", len(solutions))
    print("bulbs:", ",".join(coordinate(index) for index in solutions[0]))


if __name__ == "__main__":
    main()
