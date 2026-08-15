#!/usr/bin/env python3
"""Independently verify the canonical Loopy control and export its loop."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path


CONTROL_ID = (
    "10x10t0:"
    "a3b2a222d12223a33b23e3a221b3a2b2c3b0b2a12a2b222a1a2c3e1b3a2b1a2d333a2002a"
)


@dataclass(frozen=True)
class Model:
    width: int
    height: int
    clues: tuple[int | None, ...]
    edges: tuple[tuple[int, int], ...]
    faces: tuple[tuple[int, int, int, int], ...]
    vertices: tuple[tuple[int, ...], ...]


def decode_control(game_id: str = CONTROL_ID) -> Model:
    params, description = game_id.split(":", 1)
    size, grid_type = params.split("t", 1)
    width, height = (int(part) for part in size.split("x", 1))
    if grid_type != "0":
        raise ValueError("the verifier intentionally supports the square control only")

    clues: list[int | None] = []
    for token in description:
        if token.isdigit():
            clues.append(int(token))
        elif "A" <= token <= "Z":
            clues.append(ord(token) - ord("A") + 10)
        elif "a" <= token <= "z":
            clues.extend([None] * (ord(token) - ord("a") + 1))
        else:
            raise ValueError(f"unknown description token: {token!r}")
    if len(clues) != width * height:
        raise ValueError(f"decoded {len(clues)} faces, expected {width * height}")

    # Horizontal edges first, then vertical edges. Vertices are row-major dots.
    edges: list[tuple[int, int]] = []
    horizontal: dict[tuple[int, int], int] = {}
    vertical: dict[tuple[int, int], int] = {}
    for y in range(height + 1):
        for x in range(width):
            horizontal[x, y] = len(edges)
            edges.append((y * (width + 1) + x, y * (width + 1) + x + 1))
    for y in range(height):
        for x in range(width + 1):
            vertical[x, y] = len(edges)
            edges.append((y * (width + 1) + x, (y + 1) * (width + 1) + x))

    faces = []
    for y in range(height):
        for x in range(width):
            faces.append(
                (
                    horizontal[x, y],
                    vertical[x + 1, y],
                    horizontal[x, y + 1],
                    vertical[x, y],
                )
            )
    incident: list[list[int]] = [[] for _ in range((width + 1) * (height + 1))]
    for edge_index, (a, b) in enumerate(edges):
        incident[a].append(edge_index)
        incident[b].append(edge_index)
    return Model(
        width,
        height,
        tuple(clues),
        tuple(edges),
        tuple(faces),
        tuple(tuple(group) for group in incident),
    )


class Solver:
    def __init__(self, model: Model) -> None:
        self.model = model
        self.edge_constraints: list[list[tuple[str, int]]] = [
            [] for _ in model.edges
        ]
        for face_index, face in enumerate(model.faces):
            if model.clues[face_index] is not None:
                for edge in face:
                    self.edge_constraints[edge].append(("f", face_index))
        for vertex_index, edges in enumerate(model.vertices):
            for edge in edges:
                self.edge_constraints[edge].append(("v", vertex_index))

    @staticmethod
    def _set(values: list[int], edge: int, value: int, queue: deque[int]) -> bool:
        current = values[edge]
        if current >= 0:
            return current == value
        values[edge] = value
        queue.append(edge)
        return True

    def _propagate(self, values: list[int], initial: list[int] | None = None) -> bool:
        queue = deque(initial if initial is not None else range(len(values)))
        pending_faces = set()
        pending_vertices = set()
        while queue or pending_faces or pending_vertices:
            while queue:
                edge = queue.popleft()
                for kind, index in self.edge_constraints[edge]:
                    (pending_faces if kind == "f" else pending_vertices).add(index)

            while pending_faces:
                face_index = pending_faces.pop()
                clue = self.model.clues[face_index]
                assert clue is not None
                face = self.model.faces[face_index]
                yes = sum(values[e] == 1 for e in face)
                unknown = [e for e in face if values[e] < 0]
                if yes > clue or yes + len(unknown) < clue:
                    return False
                if yes == clue:
                    for edge in unknown:
                        if not self._set(values, edge, 0, queue):
                            return False
                elif yes + len(unknown) == clue:
                    for edge in unknown:
                        if not self._set(values, edge, 1, queue):
                            return False

            while pending_vertices:
                vertex = pending_vertices.pop()
                incident = self.model.vertices[vertex]
                yes = sum(values[e] == 1 for e in incident)
                unknown = [e for e in incident if values[e] < 0]
                if yes > 2 or (yes == 1 and not unknown):
                    return False
                if yes == 2:
                    for edge in unknown:
                        if not self._set(values, edge, 0, queue):
                            return False
                elif yes == 1 and len(unknown) == 1:
                    if not self._set(values, unknown[0], 1, queue):
                        return False
                elif yes == 0 and len(unknown) == 1:
                    if not self._set(values, unknown[0], 0, queue):
                        return False
        return True

    def _is_one_loop(self, values: list[int]) -> bool:
        selected = [i for i, value in enumerate(values) if value == 1]
        if not selected:
            return False
        adjacency: dict[int, list[int]] = defaultdict(list)
        for edge in selected:
            a, b = self.model.edges[edge]
            adjacency[a].append(b)
            adjacency[b].append(a)
        if any(len(neighbours) != 2 for neighbours in adjacency.values()):
            return False
        reached = set()
        todo = [next(iter(adjacency))]
        while todo:
            vertex = todo.pop()
            if vertex in reached:
                continue
            reached.add(vertex)
            todo.extend(adjacency[vertex])
        return reached == set(adjacency)

    def _choose_edge(self, values: list[int]) -> int:
        best: tuple[int, int] | None = None
        for edge, value in enumerate(values):
            if value >= 0:
                continue
            pressure = 0
            for kind, index in self.edge_constraints[edge]:
                group = (
                    self.model.faces[index]
                    if kind == "f"
                    else self.model.vertices[index]
                )
                pressure += 8 - sum(values[candidate] < 0 for candidate in group)
            candidate = (pressure, edge)
            if best is None or candidate > best:
                best = candidate
        assert best is not None
        return best[1]

    def solutions(self, limit: int = 2) -> list[list[int]]:
        found: list[list[int]] = []

        def search(values: list[int]) -> None:
            if len(found) >= limit or not self._propagate(values):
                return
            if all(value >= 0 for value in values):
                if self._is_one_loop(values):
                    found.append(values)
                return
            edge = self._choose_edge(values)
            for value in (1, 0):
                branch = values.copy()
                branch[edge] = value
                search(branch)

        search([-1] * len(self.model.edges))
        return found


def verify_solution(model: Model, values: list[int]) -> None:
    for face_index, clue in enumerate(model.clues):
        if clue is not None:
            actual = sum(values[edge] for edge in model.faces[face_index])
            if actual != clue:
                raise AssertionError(f"face {face_index}: expected {clue}, got {actual}")
    degrees = [sum(values[e] for e in incident) for incident in model.vertices]
    if any(degree not in (0, 2) for degree in degrees):
        raise AssertionError("selected-edge degree is not 0 or 2 at every vertex")
    if not Solver(model)._is_one_loop(values):
        raise AssertionError("selected edges do not form exactly one connected cycle")


def export(model: Model, values: list[int], path: Path) -> None:
    def coordinate(vertex: int) -> list[int]:
        return [vertex % (model.width + 1), vertex // (model.width + 1)]

    payload = {
        "control_id": CONTROL_ID,
        "width": model.width,
        "height": model.height,
        "clues": list(model.clues),
        "selected_edges": [
            {"index": index, "a": coordinate(model.edges[index][0]), "b": coordinate(model.edges[index][1])}
            for index, value in enumerate(values)
            if value == 1
        ],
        "selected_edge_indices": [i for i, value in enumerate(values) if value == 1],
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--export", type=Path)
    args = parser.parse_args()
    model = decode_control()
    solver = Solver(model)
    solutions = solver.solutions(limit=2)
    if len(solutions) != 1:
        raise SystemExit(f"expected one solution, found {len(solutions)}")
    verify_solution(model, solutions[0])
    disconnected = [0] * len(model.edges)
    for edge in (*model.faces[0], *model.faces[-1]):
        disconnected[edge] = 1
    if solver._is_one_loop(disconnected):
        raise AssertionError("two disjoint locally closed loops were accepted")
    branched = [0] * len(model.edges)
    for edge in model.vertices[12][:3]:
        branched[edge] = 1
    if solver._is_one_loop(branched):
        raise AssertionError("a degree-three branch was accepted")
    if args.export:
        export(model, solutions[0], args.export)
    print(
        f"Loopy control verified: {model.width}x{model.height}, "
        f"{sum(clue is not None for clue in model.clues)} clues, "
        f"{sum(solutions[0])} selected edges, unique single loop."
    )


if __name__ == "__main__":
    main()
