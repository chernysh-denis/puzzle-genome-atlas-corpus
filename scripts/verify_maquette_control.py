#!/usr/bin/env python3
"""Verify a bounded recursive-scale object route inspired by Maquette."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple


SCALE = 4
INNER = -1
NORMAL = 0
OUTER = 1
MAX_PICKUP_SIZE = 2.0


@dataclass
class RecursiveObject:
    name: str
    base_size: float
    pose: str

    def size_at(self, layer: int) -> float:
        return self.base_size * (SCALE ** layer)

    def can_pick(self, layer: int) -> bool:
        return self.size_at(layer) <= MAX_PICKUP_SIZE

    def move_replica(self, layer: int, pose: str) -> None:
        if not self.can_pick(layer):
            raise ValueError("representation is too large to manipulate")
        self.pose = pose

    def carry_between_layers(self, source: int, target: int) -> None:
        if abs(source - target) != 1:
            raise ValueError("only adjacent recursion layers may be crossed")
        if not self.can_pick(source):
            raise ValueError("source representation is too large to carry")
        self.base_size *= SCALE ** (source - target)


def reject(label: str, operation) -> str:
    try:
        operation()
    except ValueError:
        return label
    raise AssertionError("invalid transition was accepted: %s" % label)


def verify() -> Tuple[Dict[str, float], Tuple[str, ...]]:
    red_block = RecursiveObject("red block", 8.0, "garden gate")
    key = RecursiveObject("gold key", 1.0, "fortune teller")
    rejected = []

    rejected.append(reject(
        "normal-size-red-block-pickup",
        lambda: red_block.move_replica(NORMAL, "clear"),
    ))
    red_block.move_replica(INNER, "courtyard corner")
    assert red_block.pose == "courtyard corner"
    assert red_block.size_at(NORMAL) == 8.0

    key.move_replica(NORMAL, "model gap")
    key.carry_between_layers(NORMAL, INNER)
    assert key.base_size == 4.0
    assert key.size_at(NORMAL) == 4.0
    assert key.pose == "model gap"
    bridge_open = key.size_at(NORMAL) >= 4.0 and key.pose == "model gap"
    assert bridge_open

    rejected.append(reject(
        "giant-key-pickup",
        lambda: key.move_replica(NORMAL, "elsewhere"),
    ))
    rejected.append(reject(
        "non-adjacent-scale-transfer",
        lambda: key.carry_between_layers(INNER, OUTER),
    ))

    key.move_replica(INNER, "outside dome")
    key.carry_between_layers(INNER, NORMAL)
    assert key.base_size == 1.0
    key.pose = "outside dome"
    assert key.size_at(INNER) == 0.25

    key.move_replica(INNER, "house lock")
    key.carry_between_layers(INNER, NORMAL)
    assert key.base_size == 0.25
    house_unlocked = key.pose == "house lock" and key.size_at(NORMAL) <= 0.5
    assert house_unlocked

    rejected.append(reject(
        "undersized-bridge",
        lambda: require_bridge(key, "floating-house gap"),
    ))
    rejected.append(reject(
        "wrong-bridge-pose",
        lambda: require_bridge(key, "courtyard"),
    ))

    key.carry_between_layers(NORMAL, INNER)
    assert key.base_size == 1.0
    key.move_replica(NORMAL, "floating-house gap")
    key.carry_between_layers(NORMAL, INNER)
    assert key.base_size == 4.0
    require_bridge(key, "floating-house gap")

    exit_open = house_unlocked and key.pose == "floating-house gap"
    rejected.append(reject(
        "locked-house-entry",
        lambda: require_exit(False, key.pose),
    ))
    require_exit(exit_open, key.pose)

    if len(rejected) != 6 or len(set(rejected)) != 6:
        raise AssertionError("expected six distinct rejected transitions")

    return {
        "inner_key": key.size_at(INNER),
        "normal_key": key.size_at(NORMAL),
        "outer_key": key.size_at(OUTER),
    }, tuple(rejected)


def require_bridge(key: RecursiveObject, pose: str) -> None:
    if key.base_size < 4.0 or pose != "floating-house gap" or key.pose != pose:
        raise ValueError("key is not a traversable bridge")


def require_exit(unlocked: bool, bridge_pose: str) -> None:
    if not unlocked or bridge_pose != "floating-house gap":
        raise ValueError("house route is incomplete")


if __name__ == "__main__":
    sizes, rejected_transitions = verify()
    print(
        "Maquette control verified: one authoritative object across three "
        "scale-linked representations (%g, %g, %g), one oversized blocker "
        "moved through its inner replica, two key bridges, one tiny-key unlock "
        "and %d rejected invalid transitions."
        % (
            sizes["inner_key"],
            sizes["normal_key"],
            sizes["outer_key"],
            len(rejected_transitions),
        )
    )
