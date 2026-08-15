#!/usr/bin/env python3
"""Verify the reproducible GAME-0071 Slant control and its unique solution."""

from __future__ import annotations

from dataclasses import dataclass

WIDTH = 8
HEIGHT = 8
DESCRIPTION = "a0a1c1a032a1a3a1a21a222a2d21c2a2c21a1a11a11a1a12b1b113b2a12f0a11"

BACKSLASH = -1
UNKNOWN = 0
SLASH = 1


def decode_clues() -> tuple[int | None, ...]:
    clues: list[int | None] = []
    for symbol in DESCRIPTION:
        if "a" <= symbol <= "z":
            clues.extend([None] * (ord(symbol) - ord("a") + 1))
        else:
            clues.append(int(symbol))
    assert len(clues) == (WIDTH + 1) * (HEIGHT + 1)
    return tuple(clues)


CLUES = decode_clues()


def endpoints(cell: int, orientation: int) -> tuple[int, int]:
    row, column = divmod(cell, WIDTH)
    vertex_width = WIDTH + 1
    if orientation == BACKSLASH:
        return row * vertex_width + column, (row + 1) * vertex_width + column + 1
    return row * vertex_width + column + 1, (row + 1) * vertex_width + column


INCIDENT = tuple(
    tuple(
        (cell, orientation)
        for cell in range(WIDTH * HEIGHT)
        for orientation in (BACKSLASH, SLASH)
        if vertex in endpoints(cell, orientation)
    )
    for vertex in range((WIDTH + 1) * (HEIGHT + 1))
)


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, first: int, second: int) -> bool:
        first_root, second_root = self.find(first), self.find(second)
        if first_root == second_root:
            return False
        self.parent[second_root] = first_root
        return True


def graph(assignments: tuple[int, ...]) -> UnionFind | None:
    forest = UnionFind((WIDTH + 1) * (HEIGHT + 1))
    for cell, orientation in enumerate(assignments):
        if orientation:
            if not forest.union(*endpoints(cell, orientation)):
                return None
    return forest


def propagate(assignments: tuple[int, ...]) -> tuple[int, ...] | None:
    values = list(assignments)
    while True:
        forest = graph(tuple(values))
        if forest is None:
            return None
        domains = [set((BACKSLASH, SLASH)) if value == UNKNOWN else {value} for value in values]
        changed = False

        for cell, domain in enumerate(domains):
            if values[cell] != UNKNOWN:
                continue
            for orientation in tuple(domain):
                first, second = endpoints(cell, orientation)
                if forest.find(first) == forest.find(second):
                    domain.remove(orientation)
            if not domain:
                return None

        for vertex, clue in enumerate(CLUES):
            if clue is None:
                continue
            fixed = 0
            possible: list[tuple[int, int]] = []
            for cell, orientation in INCIDENT[vertex]:
                if values[cell] == orientation:
                    fixed += 1
                elif values[cell] == UNKNOWN and orientation in domains[cell]:
                    possible.append((cell, orientation))
            if fixed > clue or fixed + len(possible) < clue:
                return None
            if fixed == clue:
                for cell, orientation in possible:
                    domains[cell].discard(orientation)
            elif fixed + len(possible) == clue:
                for cell, orientation in possible:
                    domains[cell].intersection_update({orientation})

        for cell, domain in enumerate(domains):
            if not domain:
                return None
            if values[cell] == UNKNOWN and len(domain) == 1:
                values[cell] = next(iter(domain))
                changed = True
        if not changed:
            return tuple(values)


def solve(assignments: tuple[int, ...] | None = None, limit: int = 2) -> tuple[tuple[int, ...], ...]:
    state = propagate(assignments or (UNKNOWN,) * (WIDTH * HEIGHT))
    if state is None:
        return ()
    if UNKNOWN not in state:
        return (state,)

    cell = state.index(UNKNOWN)
    solutions: list[tuple[int, ...]] = []
    for orientation in (BACKSLASH, SLASH):
        branch = list(state)
        branch[cell] = orientation
        solutions.extend(solve(tuple(branch), limit - len(solutions)))
        if len(solutions) >= limit:
            break
    return tuple(solutions)


def validate(solution: tuple[int, ...]) -> None:
    assert UNKNOWN not in solution
    assert graph(solution) is not None
    for vertex, clue in enumerate(CLUES):
        if clue is not None:
            assert sum(solution[cell] == orientation for cell, orientation in INCIDENT[vertex]) == clue


def rows(solution: tuple[int, ...]) -> tuple[str, ...]:
    return tuple(
        "".join("\\" if value == BACKSLASH else "/" for value in solution[offset:offset + WIDTH])
        for offset in range(0, len(solution), WIDTH)
    )


def main() -> None:
    assert sum(clue is not None for clue in CLUES) == 39
    solutions = solve(limit=2)
    assert len(solutions) == 1
    validate(solutions[0])

    # A backslash in B2 joins B2 to C3. Adding the three other sides of that
    # four-vertex diamond produces a cycle and must be rejected.
    cycle_control = [UNKNOWN] * (WIDTH * HEIGHT)
    cycle_control[0] = SLASH
    cycle_control[1] = BACKSLASH
    cycle_control[WIDTH] = BACKSLASH
    cycle_control[WIDTH + 1] = SLASH
    assert graph(tuple(cycle_control)) is None

    print("Slant GAME-0071 control verified")
    print("clues:", 39, "cells:", WIDTH * HEIGHT, "unique solutions:", len(solutions))
    print("solution:")
    print("\n".join(rows(solutions[0])))


if __name__ == "__main__":
    main()
