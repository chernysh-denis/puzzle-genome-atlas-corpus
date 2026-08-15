#!/usr/bin/env python3
"""Generate and verify the exact GAME-0083 Net control.

The control uses the current Simon Tatham Net 5x5 non-wrapping description
codec: one hexadecimal port mask per cell, with R=1, U=2, L=4 and D=8.  A
fixed seed produces a spanning tree, rotates every tile into its presented
orientation, and retains the first instance with exactly one accepted
orientation assignment.  The verifier then independently re-enumerates the
control to a second-solution limit.
"""

from __future__ import annotations

import random
from collections import deque

WIDTH = HEIGHT = 5
SEED = 202608140083
EXPECTED_DESCRIPTION = "1319827eb3e918b6ae4b1a326"
EXPECTED_SOLUTION = "1c8948b77cb681e35e1e15616"

R, U, L, D = 1, 2, 4, 8
OPPOSITE = {R: L, U: D, L: R, D: U}
STEPS = {R: (1, 0), U: (0, -1), L: (-1, 0), D: (0, 1)}


def rotate(mask: int) -> int:
    return ((mask << 1) & 0xF) | ((mask >> 3) & 1)


def orientations(mask: int) -> tuple[int, ...]:
    values = []
    for _ in range(4):
        if mask not in values:
            values.append(mask)
        mask = rotate(mask)
    return tuple(values)


def solved(mask_grid: list[int]) -> bool:
    edge_count = 0
    graph = [[] for _ in mask_grid]
    for index, mask in enumerate(mask_grid):
        x, y = index % WIDTH, index // WIDTH
        for direction, (dx, dy) in STEPS.items():
            if not mask & direction:
                continue
            nx, ny = x + dx, y + dy
            if not (0 <= nx < WIDTH and 0 <= ny < HEIGHT):
                return False
            neighbour = ny * WIDTH + nx
            if not mask_grid[neighbour] & OPPOSITE[direction]:
                return False
            if direction in (R, D):
                edge_count += 1
                graph[index].append(neighbour)
                graph[neighbour].append(index)

    reached = {0}
    queue = deque([0])
    while queue:
        current = queue.popleft()
        for neighbour in graph[current]:
            if neighbour not in reached:
                reached.add(neighbour)
                queue.append(neighbour)
    return len(reached) == WIDTH * HEIGHT and edge_count == WIDTH * HEIGHT - 1


def enumerate_solutions(description: str, limit: int = 2) -> list[list[int]]:
    tiles = [int(character, 16) for character in description]
    assert len(tiles) == WIDTH * HEIGHT
    domains = [orientations(tile) for tile in tiles]
    assignment = [0] * len(tiles)
    solutions: list[list[int]] = []

    def visit(index: int) -> None:
        if len(solutions) >= limit:
            return
        if index == len(tiles):
            if solved(assignment):
                solutions.append(assignment.copy())
            return

        x, y = index % WIDTH, index // WIDTH
        for mask in domains[index]:
            if x == 0 and mask & L or x == WIDTH - 1 and mask & R:
                continue
            if y == 0 and mask & U or y == HEIGHT - 1 and mask & D:
                continue
            if x and bool(mask & L) != bool(assignment[index - 1] & R):
                continue
            if y and bool(mask & U) != bool(assignment[index - WIDTH] & D):
                continue
            assignment[index] = mask
            visit(index + 1)
            if len(solutions) >= limit:
                return

    visit(0)
    return solutions


def generate_control() -> tuple[str, str, int]:
    rng = random.Random(SEED)
    candidate = 0
    while True:
        candidate += 1
        edges = []
        for y in range(HEIGHT):
            for x in range(WIDTH):
                here = y * WIDTH + x
                if x + 1 < WIDTH:
                    edges.append((here, here + 1, R, L))
                if y + 1 < HEIGHT:
                    edges.append((here, here + WIDTH, D, U))
        rng.shuffle(edges)

        parent = list(range(WIDTH * HEIGHT))
        degree = [0] * (WIDTH * HEIGHT)
        solution = [0] * (WIDTH * HEIGHT)

        def root(value: int) -> int:
            while parent[value] != value:
                parent[value] = parent[parent[value]]
                value = parent[value]
            return value

        selected = 0
        for first, second, out_dir, in_dir in edges:
            first_root, second_root = root(first), root(second)
            if first_root == second_root or degree[first] >= 3 or degree[second] >= 3:
                continue
            parent[first_root] = second_root
            degree[first] += 1
            degree[second] += 1
            solution[first] |= out_dir
            solution[second] |= in_dir
            selected += 1
            if selected == WIDTH * HEIGHT - 1:
                break
        if selected != WIDTH * HEIGHT - 1:
            continue

        presented = []
        for mask in solution:
            for _ in range(rng.randrange(4)):
                mask = rotate(mask)
            presented.append(mask)
        description = "".join(format(mask, "x") for mask in presented)
        solutions = enumerate_solutions(description)
        if len(solutions) == 1:
            encoded_solution = "".join(format(mask, "x") for mask in solutions[0])
            return description, encoded_solution, candidate


def main() -> None:
    description, solution, candidate = generate_control()
    if EXPECTED_DESCRIPTION == "TO_BE_FILLED":
        print(f"description={description}")
        print(f"solution={solution}")
        print(f"candidate={candidate}")
        return

    assert description == EXPECTED_DESCRIPTION
    assert solution == EXPECTED_SOLUTION
    solutions = enumerate_solutions(EXPECTED_DESCRIPTION)
    assert len(solutions) == 1
    assert solved(solutions[0])
    assert sum(bin(mask).count("1") for mask in solutions[0]) == 48
    print(
        "Net control verified: 5x5 non-wrapping, one unique connected "
        "24-edge tree across all 25 rotated tiles."
    )


if __name__ == "__main__":
    main()
