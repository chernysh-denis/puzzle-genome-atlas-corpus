"""Small source-model controls for GAME-0369; not a played Carcassonne game.

This intentionally does not enumerate the publisher's tile mix. It tests
transition predicates isolated from the linked English rule sheets.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field


EDGE_OFFSETS = ((0, -1), (1, 0), (0, 1), (-1, 0))  # N E S W


def rotate(edges: tuple[str, str, str, str], quarter_turns: int) -> tuple[str, ...]:
    turns = quarter_turns % 4
    return edges[-turns:] + edges[:-turns] if turns else edges


def legal_placement(
    board: dict[tuple[int, int], tuple[str, ...]],
    cell: tuple[int, int],
    edges: tuple[str, ...],
) -> bool:
    if cell in board or len(edges) != 4:
        return False
    touches = False
    for direction, (dx, dy) in enumerate(EDGE_OFFSETS):
        neighbour = board.get((cell[0] + dx, cell[1] + dy))
        if neighbour is None:
            continue
        touches = True
        if edges[direction] != neighbour[(direction + 2) % 4]:
            return False
    return touches


def drawable_tile(
    board: dict[tuple[int, int], tuple[str, ...]],
    stack: list[tuple[str, ...]],
) -> tuple[tuple[str, ...], tuple[int, int], int, int] | None:
    """Return first drawable legal tile, location, rotation and forced discards."""
    frontier = {
        (x + dx, y + dy)
        for x, y in board
        for dx, dy in EDGE_OFFSETS
        if (x + dx, y + dy) not in board
    }
    discarded = 0
    while stack:
        tile = stack.pop(0)
        for cell in sorted(frontier):
            for turns in range(4):
                if legal_placement(board, cell, rotate(tile, turns)):
                    return tile, cell, turns, discarded
        discarded += 1
    return None


@dataclass
class Feature:
    kind: str
    tiles: set[int]
    emblems: int = 0
    occupied: Counter[str] = field(default_factory=Counter)
    adjacent_completed_cities: set[str] = field(default_factory=set)


def claim(feature: Feature, player: str, reserve: dict[str, int]) -> None:
    if feature.occupied or reserve[player] <= 0:
        raise ValueError("connected feature occupied or no follower in reserve")
    feature.occupied[player] += 1
    reserve[player] -= 1


def join(first: Feature, second: Feature) -> Feature:
    if first.kind != second.kind:
        raise ValueError("different feature types cannot join")
    return Feature(
        first.kind,
        first.tiles | second.tiles,
        first.emblems + second.emblems,
        first.occupied + second.occupied,
        first.adjacent_completed_cities | second.adjacent_completed_cities,
    )


def score(feature: Feature, complete: bool, reserve: dict[str, int]) -> dict[str, int]:
    if feature.kind == "road":
        value = len(feature.tiles)
    elif feature.kind == "city":
        value = (2 if complete else 1) * (len(feature.tiles) + feature.emblems)
    elif feature.kind == "monastery":
        value = len(feature.tiles)  # centre tile plus the currently surrounding tiles
    elif feature.kind == "field" and not complete:
        value = 3 * len(feature.adjacent_completed_cities)
    else:
        raise ValueError("field has no in-turn completion score")
    largest = max(feature.occupied.values(), default=0)
    awarded = {player: value for player, count in feature.occupied.items() if count == largest and largest > 0}
    if complete and feature.kind != "field":
        for player, count in feature.occupied.items():
            reserve[player] += count
    return awarded
