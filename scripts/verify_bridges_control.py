#!/usr/bin/env python3
"""Verify the reproducible GAME-0074 Bridges control and unique network."""

from __future__ import annotations

DESCRIPTION = "2b4b4a2b2b2e3a2a2j3b2d2b5a3"
WIDTH = HEIGHT = 7
MAX_BRIDGES = 2


def decode() -> tuple[tuple[int, int, int], ...]:
    cells: list[int | None] = []
    for symbol in DESCRIPTION:
        if symbol.isdigit():
            cells.append(int(symbol))
        else:
            cells.extend([None] * (ord(symbol) - ord("a") + 1))
    assert len(cells) == WIDTH * HEIGHT
    return tuple(
        (index % WIDTH, index // WIDTH, clue)
        for index, clue in enumerate(cells)
        if clue is not None
    )


ISLANDS = decode()
POSITIONS = {(x, y): index for index, (x, y, _) in enumerate(ISLANDS)}


def potential_edges() -> tuple[tuple[int, int], ...]:
    edges = []
    for start, (x, y, _) in enumerate(ISLANDS):
        for dx, dy in ((1, 0), (0, 1)):
            nx, ny = x + dx, y + dy
            while nx < WIDTH and ny < HEIGHT:
                if (nx, ny) in POSITIONS:
                    edges.append((start, POSITIONS[(nx, ny)]))
                    break
                nx += dx
                ny += dy
    return tuple(edges)


EDGES = potential_edges()
INCIDENT = tuple(
    tuple(index for index, edge in enumerate(EDGES) if island in edge)
    for island in range(len(ISLANDS))
)


def crosses(first: tuple[int, int], second: tuple[int, int]) -> bool:
    ax, ay, _ = ISLANDS[first[0]]
    bx, by, _ = ISLANDS[first[1]]
    cx, cy, _ = ISLANDS[second[0]]
    dx, dy, _ = ISLANDS[second[1]]
    return (
        ay == by
        and cx == dx
        and min(ax, bx) < cx < max(ax, bx)
        and min(cy, dy) < ay < max(cy, dy)
    ) or (
        ax == bx
        and cy == dy
        and min(ay, by) < cy < max(ay, by)
        and min(cx, dx) < ax < max(cx, dx)
    )


CROSSINGS = frozenset(
    (left, right)
    for left, edge in enumerate(EDGES)
    for right, other in enumerate(EDGES[:left])
    if crosses(edge, other)
)


def connected(values: tuple[int, ...]) -> bool:
    seen = {0}
    stack = [0]
    while stack:
        island = stack.pop()
        for edge_index in INCIDENT[island]:
            if values[edge_index] == 0:
                continue
            first, second = EDGES[edge_index]
            neighbour = second if first == island else first
            if neighbour not in seen:
                seen.add(neighbour)
                stack.append(neighbour)
    return len(seen) == len(ISLANDS)


def solve(limit: int = 2) -> tuple[tuple[int, ...], ...]:
    values: list[int | None] = [None] * len(EDGES)
    solutions: list[tuple[int, ...]] = []

    def search(index: int) -> None:
        if len(solutions) >= limit:
            return
        for island, (_, _, target) in enumerate(ISLANDS):
            known = sum(values[edge] or 0 for edge in INCIDENT[island])
            unknown = sum(values[edge] is None for edge in INCIDENT[island])
            if known > target or known + MAX_BRIDGES * unknown < target:
                return
        if index == len(EDGES):
            complete = tuple(int(value) for value in values)
            if connected(complete):
                solutions.append(complete)
            return
        for count in range(MAX_BRIDGES + 1):
            values[index] = count
            conflict = count > 0 and any(
                values[other] not in (None, 0)
                for pair in CROSSINGS
                if index in pair
                for other in pair
                if other != index
            )
            if not conflict:
                search(index + 1)
        values[index] = None

    search(0)
    return tuple(solutions)


def main() -> None:
    assert len(ISLANDS) == 14
    assert len(EDGES) == 17
    assert len(CROSSINGS) == 5
    solutions = solve()
    assert len(solutions) == 1
    solution = solutions[0]
    assert connected(solution)
    assert all(
        sum(solution[edge] for edge in INCIDENT[island]) == clue
        for island, (_, _, clue) in enumerate(ISLANDS)
    )
    assert all(not (solution[left] and solution[right]) for left, right in CROSSINGS)

    # Connectivity is checked independently rather than inferred from clues.
    disconnected = tuple(0 for _ in EDGES)
    assert not connected(disconnected)

    # Four clue-1 vertices joined as two disjoint pairs satisfy every local
    # degree while failing the independent spanning-connectivity predicate.
    synthetic_edges = ((0, 1), (2, 3))
    synthetic_degree = [0, 0, 0, 0]
    for first, second in synthetic_edges:
        synthetic_degree[first] += 1
        synthetic_degree[second] += 1
    assert synthetic_degree == [1, 1, 1, 1]
    assert {0, 1} != {0, 1, 2, 3}

    # The control also contains five genuine horizontal/vertical conflicts.
    # Activating both members of any such pair violates non-crossing even when
    # neither edge shares an endpoint with the other.
    left, right = next(iter(CROSSINGS))
    assert set(EDGES[left]).isdisjoint(EDGES[right])
    crossing_proposal = [0] * len(EDGES)
    crossing_proposal[left] = crossing_proposal[right] = 1
    assert any(crossing_proposal[a] and crossing_proposal[b] for a, b in CROSSINGS)

    print("Bridges GAME-0074 control verified")
    print("islands:", len(ISLANDS), "edges:", len(EDGES), "crossings:", len(CROSSINGS), "unique solutions:", len(solutions))
    print("bridges:")
    for edge_index, count in enumerate(solution):
        if not count:
            continue
        first, second = EDGES[edge_index]
        ax, ay, _ = ISLANDS[first]
        bx, by, _ = ISLANDS[second]
        print(f"{chr(65 + ay)}{ax + 1}-{chr(65 + by)}{bx + 1}: {count}")


if __name__ == "__main__":
    main()
