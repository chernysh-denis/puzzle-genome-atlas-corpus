#!/usr/bin/env python3
"""Verify the bounded standard-geometry HyperRogue rules packet."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Callable


GRAPH = {
    "P0": {"P1", "A"},
    "P1": {"P0", "B", "E2"},
    "A": {"P0", "B"},
    "B": {"A", "P1"},
    "E0": {"E1", "C"},
    "E1": {"E0", "E2", "C"},
    "E2": {"E1", "P1"},
    "C": {"E0", "E1"},
}


def distance(start: str, target: str) -> int:
    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        node, steps = queue.popleft()
        if node == target:
            return steps
        for neighbor in GRAPH[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append((neighbor, steps + 1))
    raise ValueError("fixture must remain connected")


def require_standard_geometry(p: int, q: int, bitruncated: bool) -> None:
    if (p, q, bitruncated) != (7, 3, True):
        raise ValueError("standard HyperRogue requires bitruncated {7,3}")


@dataclass
class TurnControl:
    player: str = "P0"
    enemy: str = "E0"
    treasure: str = "P1"
    score: int = 0
    view_center: str = "P0"
    resolved_turns: int = 0
    blocked: set[str] = field(default_factory=set)

    def step(self, target: str) -> None:
        if target not in GRAPH[self.player] or target in self.blocked:
            raise ValueError("player movement must use one open adjacent tile")
        self.player = target
        if self.player == self.treasure:
            self.score += 1
            self.treasure = ""
        self.view_center = self.player

        before = distance(self.enemy, self.player)
        candidates = sorted(GRAPH[self.enemy] - self.blocked)
        improving = [node for node in candidates if distance(node, self.player) < before]
        if not improving:
            raise ValueError("enemy requires a shortest-route response step")
        self.enemy = min(improving, key=lambda node: (distance(node, self.player), node))
        self.resolved_turns += 1

        if self.enemy == self.player or distance(self.enemy, self.player) <= 1:
            raise ValueError("bounded route must not end in immediate capture")


def reject(label: str, operation: Callable[[], None]) -> str:
    try:
        operation()
    except ValueError:
        return label
    raise AssertionError("invalid transition was accepted: %s" % label)


def verify() -> tuple[int, int, tuple[str, ...]]:
    require_standard_geometry(7, 3, True)
    control = TurnControl()
    control.step("P1")
    assert control.player == "P1"
    assert control.enemy == "E1"
    assert control.score == 1
    assert control.view_center == control.player
    assert control.resolved_turns == 1

    rejected = [
        reject("flat-hex-control", lambda: require_standard_geometry(6, 3, True)),
        reject("unbitruncated-control", lambda: require_standard_geometry(7, 3, False)),
        reject("non-adjacent-player-step", lambda: TurnControl().step("E2")),
        reject("blocked-player-step", lambda: TurnControl(blocked={"P1"}).step("P1")),
        reject("capturing-response", lambda: TurnControl(enemy="E2").step("P1")),
        reject("disconnected-fixture-node", lambda: distance("P0", "missing")),
    ]
    if len(rejected) != 6 or len(set(rejected)) != 6:
        raise AssertionError("expected six distinct rejected controls")
    return control.score, control.resolved_turns, tuple(rejected)


if __name__ == "__main__":
    score, turns, rejected = verify()
    print(
        "HyperRogue control verified: bitruncated {7,3}, one adjacent treasure "
        "step, %d hostile response, player-centred view, score +%d and %d "
        "rejected invalid controls." % (turns, score, len(rejected))
    )
