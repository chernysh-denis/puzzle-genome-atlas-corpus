#!/usr/bin/env python3
"""Verify a bounded observation-gated room remap inspired by Antichamber."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


ORIGINAL = "original-room"
CHANGED = "changed-room"


@dataclass
class Doorway:
    destination: str = ORIGINAL
    visible: bool = True
    cube_collected: bool = False
    remap_armed: bool = False

    def collect_cube(self) -> None:
        self.cube_collected = True
        self.remap_armed = True

    def set_view(self, doorway_visible: bool) -> None:
        self.visible = doorway_visible
        if self.remap_armed and not self.visible:
            self.destination = CHANGED
            self.remap_armed = False

    def traverse(self) -> str:
        return self.destination


def reject(label: str, operation) -> str:
    try:
        operation()
    except ValueError:
        return label
    raise AssertionError("invalid transition was accepted: %s" % label)


def require_changed(doorway: Doorway) -> None:
    if doorway.destination != CHANGED:
        raise ValueError("doorway still leads to its original room")


def force_visible_remap(doorway: Doorway) -> None:
    if doorway.visible:
        raise ValueError("authored replacement cannot resolve while watched")
    doorway.destination = CHANGED


def assign_unknown_destination(doorway: Doorway, destination: str) -> None:
    if destination not in {ORIGINAL, CHANGED}:
        raise ValueError("destination is outside the authored room graph")
    doorway.destination = destination


def require_arrival(doorway: Doorway, room: str) -> None:
    if doorway.traverse() != room or room != CHANGED:
        raise ValueError("designated changed-room arrival was not reached")


def verify() -> Tuple[str, Tuple[str, ...]]:
    rejected = []

    watched = Doorway()
    watched.collect_cube()
    watched.set_view(True)
    assert watched.traverse() == ORIGINAL
    rejected.append(reject("watched-remap", lambda: force_visible_remap(watched)))
    rejected.append(reject("early-changed-entry", lambda: require_changed(watched)))

    route = Doorway()
    route.collect_cube()
    route.set_view(False)
    assert route.destination == CHANGED
    route.set_view(True)
    assert route.destination == CHANGED
    require_arrival(route, CHANGED)

    rejected.append(reject(
        "uncollected-cube-remap",
        lambda: require_changed(unarmed_control()),
    ))
    rejected.append(reject(
        "unauthored-destination",
        lambda: assign_unknown_destination(route, "procedural-room"),
    ))
    rejected.append(reject(
        "euclidean-original-arrival",
        lambda: require_arrival(route, ORIGINAL),
    ))
    rejected.append(reject(
        "premature-goal-credit",
        lambda: require_arrival(Doorway(), CHANGED),
    ))

    if len(rejected) != 6 or len(set(rejected)) != 6:
        raise AssertionError("expected six distinct rejected transitions")
    return route.traverse(), tuple(rejected)


def unarmed_control() -> Doorway:
    doorway = Doorway()
    doorway.set_view(False)
    return doorway


if __name__ == "__main__":
    destination, rejected_transitions = verify()
    print(
        "Antichamber control verified: one watched unchanged doorway, one "
        "off-screen authored remap to %s, one designated arrival and %d "
        "rejected invalid transitions."
        % (destination, len(rejected_transitions))
    )
