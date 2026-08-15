#!/usr/bin/env python3
"""Generate and exhaustively verify the exact GAME-0084 Netslide control."""

from __future__ import annotations

import random
from collections import deque

WIDTH = HEIGHT = 3
SEED = 202608140084
EXPECTED_DESCRIPTION = "cvah28cv1bv36"
EXPECTED_SOLUTION = "81cbca236"
EXPECTED_DISTANCE = 5

R, U, L, D = 1, 2, 4, 8
OPPOSITE = {R: L, U: D, L: R, D: U}
STEPS = {R: (1, 0), U: (0, -1), L: (-1, 0), D: (0, 1)}
MOVES = ("R0+", "R0-", "R2+", "R2-", "C0+", "C0-", "C2+", "C2-")


def apply_move(state: tuple[int, ...], move: str) -> tuple[int, ...]:
    values = list(state)
    index = int(move[1])
    delta = 1 if move[2] == "+" else -1
    positions = (
        [index * WIDTH + column for column in range(WIDTH)]
        if move[0] == "R"
        else [row * WIDTH + index for row in range(HEIGHT)]
    )
    old = [values[position] for position in positions]
    for destination, value in enumerate(old):
        values[positions[(destination + delta) % len(positions)]] = value
    return tuple(values)


def connected(state: tuple[int, ...], barriers: tuple[int, ...]) -> bool:
    reached = {4}
    queue = deque([4])
    while queue:
        cell = queue.popleft()
        x, y = cell % WIDTH, cell // WIDTH
        for direction, (dx, dy) in STEPS.items():
            nx, ny = x + dx, y + dy
            if not (0 <= nx < WIDTH and 0 <= ny < HEIGHT):
                continue
            neighbour = ny * WIDTH + nx
            if (
                state[cell] & direction
                and state[neighbour] & OPPOSITE[direction]
                and not barriers[cell] & direction
                and neighbour not in reached
            ):
                reached.add(neighbour)
                queue.append(neighbour)
    return len(reached) == WIDTH * HEIGHT


def reachable_solutions(
    start: tuple[int, ...], barriers: tuple[int, ...]
) -> tuple[list[tuple[int, ...]], dict[tuple[int, ...], tuple[tuple[int, ...], str] | None]]:
    parents: dict[tuple[int, ...], tuple[tuple[int, ...], str] | None] = {start: None}
    queue = deque([start])
    solutions = []
    while queue:
        state = queue.popleft()
        if connected(state, barriers):
            solutions.append(state)
        for move in MOVES:
            successor = apply_move(state, move)
            if successor not in parents:
                parents[successor] = (state, move)
                queue.append(successor)
    return solutions, parents


def path_to(
    target: tuple[int, ...],
    parents: dict[tuple[int, ...], tuple[tuple[int, ...], str] | None],
) -> list[str]:
    path = []
    while parents[target] is not None:
        target, move = parents[target]  # type: ignore[misc]
        path.append(move)
    return list(reversed(path))


def encode(tiles: tuple[int, ...], barriers: tuple[int, ...]) -> str:
    output = []
    for cell, tile in enumerate(tiles):
        output.append(format(tile, "x"))
        if barriers[cell] & R and cell % WIDTH < WIDTH - 1:
            output.append("v")
        if barriers[cell] & D and cell // WIDTH < HEIGHT - 1:
            output.append("h")
    return "".join(output)


def generate_control() -> tuple[str, str, int, list[str], int]:
    rng = random.Random(SEED)
    candidate = 0
    while True:
        candidate += 1
        edges = []
        for y in range(HEIGHT):
            for x in range(WIDTH):
                cell = y * WIDTH + x
                if x + 1 < WIDTH:
                    edges.append((cell, cell + 1, R, L))
                if y + 1 < HEIGHT:
                    edges.append((cell, cell + WIDTH, D, U))
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
        outer_tiles = [solution[cell] for cell in range(WIDTH * HEIGHT) if cell != 4]
        if len(set(outer_tiles)) != len(outer_tiles):
            continue

        barriers = [0] * (WIDTH * HEIGHT)
        for y in range(HEIGHT):
            for x in range(WIDTH):
                cell = y * WIDTH + x
                for direction in (R, D):
                    dx, dy = STEPS[direction]
                    nx, ny = x + dx, y + dy
                    if nx >= WIDTH or ny >= HEIGHT or solution[cell] & direction:
                        continue
                    neighbour = ny * WIDTH + nx
                    barriers[cell] |= direction
                    barriers[neighbour] |= OPPOSITE[direction]

        presented = tuple(solution)
        previous = ""
        for _ in range(8):
            choices = [move for move in MOVES if not (
                previous and move[:2] == previous[:2] and move[2] != previous[2]
            )]
            move = rng.choice(choices)
            presented = apply_move(presented, move)
            previous = move
        if presented == tuple(solution):
            continue

        solutions, parents = reachable_solutions(presented, tuple(barriers))
        if len(solutions) != 1 or solutions[0] != tuple(solution):
            continue
        path = path_to(solutions[0], parents)
        if len(path) < 4:
            continue
        return encode(presented, tuple(barriers)), "".join(format(tile, "x") for tile in solution), candidate, path, len(parents)


def decode(description: str) -> tuple[tuple[int, ...], tuple[int, ...]]:
    tiles = []
    barriers = [0] * (WIDTH * HEIGHT)
    cursor = 0
    while len(tiles) < WIDTH * HEIGHT:
        tiles.append(int(description[cursor], 16))
        cursor += 1
        cell = len(tiles) - 1
        while cursor < len(description) and description[cursor] in "vh":
            direction = R if description[cursor] == "v" else D
            neighbour = cell + (1 if direction == R else WIDTH)
            barriers[cell] |= direction
            barriers[neighbour] |= OPPOSITE[direction]
            cursor += 1
    assert cursor == len(description)
    return tuple(tiles), tuple(barriers)


def main() -> None:
    description, solution, candidate, path, state_count = generate_control()
    if EXPECTED_DESCRIPTION == "TO_BE_FILLED":
        print(f"description={description}")
        print(f"solution={solution}")
        print(f"candidate={candidate}")
        print(f"distance={len(path)}")
        print(f"path={','.join(path)}")
        print(f"reachable_states={state_count}")
        return

    assert description == EXPECTED_DESCRIPTION
    assert solution == EXPECTED_SOLUTION
    start, barriers = decode(EXPECTED_DESCRIPTION)
    solutions, parents = reachable_solutions(start, barriers)
    assert len(solutions) == 1
    assert "".join(format(tile, "x") for tile in solutions[0]) == EXPECTED_SOLUTION
    path = path_to(solutions[0], parents)
    assert len(path) == EXPECTED_DISTANCE
    assert len(parents) == 20_160
    assert len({solutions[0][cell] for cell in range(9) if cell != 4}) == 8
    assert connected(solutions[0], barriers)
    assert sum(bin(tile).count("1") for tile in solutions[0]) == 16
    print(
        f"Netslide control verified: 3x3 easy, {len(parents)} reachable tile "
        f"arrangements, one connected 8-edge tree at distance {len(path)}."
    )


if __name__ == "__main__":
    main()
