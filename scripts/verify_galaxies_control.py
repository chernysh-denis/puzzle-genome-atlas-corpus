#!/usr/bin/env python3
"""Independently decode and verify the canonical GAME-0078 Galaxies control."""

from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path


CONTROL_ID = "7x7dn:iddupugwliut"


def decode_dots(description: str, width: int, height: int) -> tuple[tuple[int, int], ...]:
    stride = width * 2 - 1
    limit = stride * (height * 2 - 1)
    position = 0
    dots: list[tuple[int, int]] = []
    for token in description:
        if token == "z":
            position += 25
            continue
        run = ord(token.lower()) - ord("a")
        position += run
        if position >= limit:
            raise ValueError("dot description exceeds the doubled grid")
        dots.append((position % stride + 1, position // stride + 1))
        position += 1
    return tuple(dots)


def central_cells(dot: tuple[int, int], width: int, height: int) -> frozenset[int]:
    dx, dy = dot
    cells = set()
    for row in range(height):
        for column in range(width):
            if abs((column * 2 + 1) - dx) <= 1 and abs((row * 2 + 1) - dy) <= 1:
                cells.add(row * width + column)
    return frozenset(cells)


def opposite(cell: int, dot: tuple[int, int], width: int, height: int) -> int | None:
    row, column = divmod(cell, width)
    reflected_x = 2 * dot[0] - (column * 2 + 1)
    reflected_y = 2 * dot[1] - (row * 2 + 1)
    if reflected_x % 2 == 0 or reflected_y % 2 == 0:
        return None
    reflected_column = (reflected_x - 1) // 2
    reflected_row = (reflected_y - 1) // 2
    if not (0 <= reflected_column < width and 0 <= reflected_row < height):
        return None
    return reflected_row * width + reflected_column


def connected(region: frozenset[int], width: int, height: int) -> bool:
    pending = [next(iter(region))]
    seen = set(pending)
    while pending:
        cell = pending.pop()
        row, column = divmod(cell, width)
        for nr, nc in ((row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)):
            neighbour = nr * width + nc
            if 0 <= nr < height and 0 <= nc < width and neighbour in region and neighbour not in seen:
                seen.add(neighbour)
                pending.append(neighbour)
    return len(seen) == len(region)


def enumerate_regions(dot_index: int, dots: tuple[tuple[int, int], ...], width: int, height: int) -> tuple[frozenset[int], ...]:
    seeds = tuple(central_cells(dot, width, height) for dot in dots)
    required = seeds[dot_index]
    forbidden = frozenset().union(*(seed for index, seed in enumerate(seeds) if index != dot_index))
    allowed = set(range(width * height)) - set(forbidden)
    dot = dots[dot_index]

    orbits: set[frozenset[int]] = set()
    for cell in allowed:
        mirror = opposite(cell, dot, width, height)
        if mirror is not None and mirror in allowed:
            orbits.add(frozenset((cell, mirror)))
    if not all(any(cell in orbit for orbit in orbits) for cell in required):
        raise AssertionError(f"dot {dot_index} cannot own all central cells")

    initial = frozenset(orbit for orbit in orbits if orbit & required)
    initial_cells = frozenset().union(*initial)
    if initial_cells != required or not connected(initial_cells, width, height):
        raise AssertionError(f"dot {dot_index} has an invalid central seed")

    orbit_neighbours: dict[frozenset[int], set[frozenset[int]]] = {orbit: set() for orbit in orbits}
    for left in orbits:
        for right in orbits:
            if left == right:
                continue
            if any(
                abs((a // width) - (b // width)) + abs((a % width) - (b % width)) == 1
                for a in left
                for b in right
            ):
                orbit_neighbours[left].add(right)

    queue = deque([initial])
    seen = {initial}
    regions: set[frozenset[int]] = set()
    while queue:
        selected = queue.popleft()
        cells = frozenset().union(*selected)
        if connected(cells, width, height):
            regions.add(cells)
        frontier = set().union(*(orbit_neighbours[orbit] for orbit in selected)) - set(selected)
        for orbit in frontier:
            expanded = selected | {orbit}
            if expanded not in seen:
                seen.add(expanded)
                queue.append(expanded)
    return tuple(sorted(regions, key=lambda region: (len(region), tuple(region))))


def solve(width: int, height: int, dots: tuple[tuple[int, int], ...], limit: int = 2) -> tuple[tuple[frozenset[int], ...], ...]:
    candidates = tuple(enumerate_regions(index, dots, width, height) for index in range(len(dots)))
    solutions: list[tuple[frozenset[int], ...]] = []
    selected: list[frozenset[int] | None] = [None] * len(dots)

    def search(covered: frozenset[int]) -> None:
        if len(solutions) >= limit:
            return
        if all(region is not None for region in selected):
            if len(covered) == width * height:
                solutions.append(tuple(region for region in selected if region is not None))
            return
        best_dot = -1
        best_options: list[frozenset[int]] | None = None
        for dot_index, region in enumerate(selected):
            if region is not None:
                continue
            options = [candidate for candidate in candidates[dot_index] if not candidate & covered]
            if not options:
                return
            if best_options is None or len(options) < len(best_options):
                best_dot, best_options = dot_index, options
        assert best_options is not None
        for candidate in best_options:
            selected[best_dot] = candidate
            search(covered | candidate)
            selected[best_dot] = None

    search(frozenset())
    return tuple(solutions)


def verify_solution(
    width: int,
    height: int,
    dots: tuple[tuple[int, int], ...],
    solution: tuple[frozenset[int], ...],
) -> None:
    covered = frozenset().union(*solution)
    if covered != frozenset(range(width * height)) or sum(map(len, solution)) != width * height:
        raise AssertionError("regions do not partition every cell exactly once")
    seeds = tuple(central_cells(dot, width, height) for dot in dots)
    for index, region in enumerate(solution):
        if not connected(region, width, height):
            raise AssertionError(f"region {index} is disconnected")
        if not seeds[index] <= region:
            raise AssertionError(f"region {index} does not contain its centre dot")
        if any(region & seed for other, seed in enumerate(seeds) if other != index):
            raise AssertionError(f"region {index} contains an extraneous dot")
        reflected = frozenset(opposite(cell, dots[index], width, height) for cell in region)
        if None in reflected or reflected != region:
            raise AssertionError(f"region {index} lacks 180-degree rotational symmetry")


def boundary_edges(width: int, height: int, solution: tuple[frozenset[int], ...]) -> tuple[tuple[int, int], ...]:
    owner = {}
    for region_index, region in enumerate(solution):
        owner.update((cell, region_index) for cell in region)
    edges = set()
    for row in range(height):
        for column in range(width):
            cell = row * width + column
            if column + 1 < width and owner[cell] != owner[cell + 1]:
                edges.add((cell, cell + 1))
            if row + 1 < height and owner[cell] != owner[cell + width]:
                edges.add((cell, cell + width))
    return tuple(sorted(edges))


def export(
    path: Path,
    width: int,
    height: int,
    dots: tuple[tuple[int, int], ...],
    solution: tuple[frozenset[int], ...],
) -> None:
    payload = {
        "control_id": CONTROL_ID,
        "width": width,
        "height": height,
        "dots": [list(dot) for dot in dots],
        "regions": [sorted(region) for region in solution],
        "region_sizes": [len(region) for region in solution],
        "internal_boundary_edges": [list(edge) for edge in boundary_edges(width, height, solution)],
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--export", type=Path)
    args = parser.parse_args()
    params, description = CONTROL_ID.split(":", 1)
    size = params.split("d", 1)[0]
    width, height = (int(value) for value in size.split("x", 1))
    dots = decode_dots(description, width, height)
    solutions = solve(width, height, dots)
    if len(dots) != 12:
        raise AssertionError(f"expected 12 dots, found {len(dots)}")
    if len(solutions) != 1:
        raise AssertionError(f"expected one solution, found {len(solutions)}")
    verify_solution(width, height, dots, solutions[0])
    edges = boundary_edges(width, height, solutions[0])
    if len(edges) != 40:
        raise AssertionError(f"expected 40 internal boundary edges, found {len(edges)}")
    if args.export:
        export(args.export, width, height, dots, solutions[0])
    print(
        "Galaxies control verified: "
        f"{width}x{height}, {len(dots)} centre dots, {len(solutions[0])} connected regions, "
        f"{len(edges)} internal boundary edges, complete half-turn symmetry, unique partition."
    )


if __name__ == "__main__":
    main()
