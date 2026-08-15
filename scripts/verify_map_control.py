#!/usr/bin/env python3
"""Independently decode and verify the canonical GAME-0077 Map control."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path


CONTROL_ID = (
    "20x15n30:"
    "ecdanaaaaalchbaabcfbabbaabdabbbaaaabaacabacbcaabbabdfabbqefcbhbedafcaacabbdddcaanaaadaadcabaaaaadacaababgdbaebecdabafaaabbbeaafbdababdcaaacbcbeeibdbaacbbdhabababfeacanabbdadaabbfeababhaaaajaaadabadaabdceacaea,"
    "01b0d2a2b2e3a1a020a32"
)


class DSU:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        a, b = self.find(left), self.find(right)
        if a != b:
            self.parent[b] = a


@dataclass(frozen=True)
class Model:
    width: int
    height: int
    region_count: int
    cells: tuple[int, ...]
    adjacency: tuple[tuple[int, int], ...]
    neighbours: tuple[frozenset[int], ...]
    givens: tuple[int | None, ...]


def decode_control(game_id: str = CONTROL_ID) -> Model:
    params, description = game_id.split(":", 1)
    geometry, clue_text = description.split(",", 1)
    size, count_text = params.split("n", 1)
    width, height = (int(value) for value in size.split("x", 1))
    region_count = int(count_text)
    cell_count = width * height
    boundary_count = width * (height - 1) + (width - 1) * height

    # The first run includes one notional non-boundary before the real stream.
    boundary_bits: list[bool] = []
    state = False
    first = True
    for token in geometry:
        run = 25 if token == "z" else ord(token) - ord("a") + 1
        for _ in range(run):
            if first:
                first = False
            else:
                boundary_bits.append(state)
        if token != "z":
            state = not state
    if len(boundary_bits) != boundary_count:
        raise ValueError(f"decoded {len(boundary_bits)} boundaries, expected {boundary_count}")

    dsu = DSU(cell_count)
    for index, boundary in enumerate(boundary_bits):
        if index < width * (height - 1):
            x, y = index % width, index // width
            left, right = y * width + x, (y + 1) * width + x
        else:
            offset = index - width * (height - 1)
            x, y = offset // height, offset % height
            left, right = y * width + x, y * width + x + 1
        if not boundary:
            dsu.union(left, right)

    labels: dict[int, int] = {}
    cells: list[int] = []
    for cell in range(cell_count):
        root = dsu.find(cell)
        labels.setdefault(root, len(labels))
        cells.append(labels[root])
    if len(labels) != region_count:
        raise ValueError(f"decoded {len(labels)} regions, expected {region_count}")

    edges = set()
    for y in range(height):
        for x in range(width):
            here = cells[y * width + x]
            if x + 1 < width and cells[y * width + x + 1] != here:
                edges.add(tuple(sorted((here, cells[y * width + x + 1]))))
            if y + 1 < height and cells[(y + 1) * width + x] != here:
                edges.add(tuple(sorted((here, cells[(y + 1) * width + x]))))
    neighbours = [set() for _ in range(region_count)]
    for left, right in edges:
        neighbours[left].add(right)
        neighbours[right].add(left)

    givens: list[int | None] = []
    for token in clue_text:
        if token in "0123":
            givens.append(int(token))
        elif "a" <= token <= "z":
            givens.extend([None] * (ord(token) - ord("a") + 1))
        else:
            raise ValueError(f"unknown clue token: {token!r}")
    if len(givens) != region_count:
        raise ValueError(f"decoded {len(givens)} region clues, expected {region_count}")

    return Model(
        width,
        height,
        region_count,
        tuple(cells),
        tuple(sorted(edges)),
        tuple(frozenset(group) for group in neighbours),
        tuple(givens),
    )


def solve(model: Model, limit: int = 2) -> list[tuple[int, ...]]:
    colours = [-1] * model.region_count
    for region, colour in enumerate(model.givens):
        if colour is not None:
            colours[region] = colour
    for left, right in model.adjacency:
        if colours[left] >= 0 and colours[left] == colours[right]:
            return []

    solutions: list[tuple[int, ...]] = []

    def search() -> None:
        if len(solutions) >= limit:
            return
        best_region = -1
        best_options: list[int] | None = None
        for region, current in enumerate(colours):
            if current >= 0:
                continue
            forbidden = {colours[n] for n in model.neighbours[region] if colours[n] >= 0}
            options = [colour for colour in range(4) if colour not in forbidden]
            if not options:
                return
            if best_options is None or len(options) < len(best_options) or (
                len(options) == len(best_options)
                and len(model.neighbours[region]) > len(model.neighbours[best_region])
            ):
                best_region, best_options = region, options
        if best_options is None:
            solutions.append(tuple(colours))
            return
        for colour in best_options:
            colours[best_region] = colour
            search()
            colours[best_region] = -1

    search()
    return solutions


def verify_solution(model: Model, solution: tuple[int, ...]) -> None:
    if len(solution) != model.region_count or any(colour not in range(4) for colour in solution):
        raise AssertionError("solution does not assign one of four colours to every region")
    for region, given in enumerate(model.givens):
        if given is not None and solution[region] != given:
            raise AssertionError(f"immutable region {region} changed colour")
    for left, right in model.adjacency:
        if solution[left] == solution[right]:
            raise AssertionError(f"boundary-adjacent regions {left} and {right} share a colour")


def diagonal_only_pairs(model: Model) -> set[tuple[int, int]]:
    corner_pairs = set()
    for y in range(model.height - 1):
        for x in range(model.width - 1):
            a = model.cells[y * model.width + x]
            b = model.cells[(y + 1) * model.width + x + 1]
            c = model.cells[y * model.width + x + 1]
            d = model.cells[(y + 1) * model.width + x]
            if a != b:
                corner_pairs.add(tuple(sorted((a, b))))
            if c != d:
                corner_pairs.add(tuple(sorted((c, d))))
    return corner_pairs - set(model.adjacency)


def export(model: Model, solution: tuple[int, ...], path: Path) -> None:
    payload = {
        "control_id": CONTROL_ID,
        "width": model.width,
        "height": model.height,
        "region_count": model.region_count,
        "cells": list(model.cells),
        "adjacency": [list(edge) for edge in model.adjacency],
        "givens": list(model.givens),
        "solution": list(solution),
        "diagonal_only_pairs": [list(pair) for pair in sorted(diagonal_only_pairs(model))],
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--export", type=Path)
    args = parser.parse_args()
    model = decode_control()
    solutions = solve(model, limit=2)
    if len(solutions) != 1:
        raise SystemExit(f"expected one solution, found {len(solutions)}")
    verify_solution(model, solutions[0])
    corner_pairs = diagonal_only_pairs(model)
    if not corner_pairs:
        raise AssertionError("control lacks a corner-only contact counterexample")
    if args.export:
        export(model, solutions[0], args.export)
    print(
        f"Map control verified: {model.width}x{model.height}, "
        f"{model.region_count} regions, {len(model.adjacency)} adjacencies, "
        f"{sum(given is not None for given in model.givens)} immutable clues, "
        f"unique four-colouring, {len(corner_pairs)} corner-only pairs ignored."
    )


if __name__ == "__main__":
    main()
