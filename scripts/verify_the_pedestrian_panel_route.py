#!/usr/bin/env python3
"""Verify a synthetic early sign-panel packet from The Pedestrian.

The miniature packet models only documented rules: intact panels can be
repositioned without creating graph edges, compatible door or ladder ports can
be paired one-to-one, and the directly controlled pedestrian can traverse the
resulting links.  Names and geometry are original test fixtures, not copied
level data.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Port:
    panel: str
    kind: str
    polarity: str


@dataclass
class Packet:
    positions: dict[str, tuple[int, int]] = field(
        default_factory=lambda: {"A": (0, 0), "B": (1, 0), "C": (2, 0)}
    )
    ports: dict[str, Port] = field(
        default_factory=lambda: {
            "A-R": Port("A", "door", "right"),
            "B-L": Port("B", "door", "left"),
            "B-D": Port("B", "ladder", "down"),
            "C-U": Port("C", "ladder", "up"),
        }
    )
    links: dict[str, str] = field(default_factory=dict)
    avatar_panel: str = "A"
    avatar_marker: str = "start"

    def reposition(self, panel: str, position: tuple[int, int]) -> None:
        self.positions[panel] = position

    def compatible(self, first: str, second: str) -> bool:
        a, b = self.ports[first], self.ports[second]
        opposites = {("left", "right"), ("right", "left"), ("up", "down"), ("down", "up")}
        return a.panel != b.panel and a.kind == b.kind and (a.polarity, b.polarity) in opposites

    def connect(self, first: str, second: str) -> bool:
        if first in self.links or second in self.links or not self.compatible(first, second):
            return False
        self.links[first] = second
        self.links[second] = first
        return True

    def enter(self, port: str) -> bool:
        if self.ports[port].panel != self.avatar_panel or port not in self.links:
            return False
        destination = self.links[port]
        self.avatar_panel = self.ports[destination].panel
        self.avatar_marker = destination
        return True

def verify() -> None:
    packet = Packet()

    # Rearranging intact panels changes the edit-plane layout but does not
    # silently manufacture traversal topology.
    packet.reposition("C", (0, 1))
    assert packet.positions["C"] == (0, 1)
    assert packet.links == {}
    assert not packet.enter("A-R")

    # Ports pair only across panels, by matching type and opposite polarity,
    # and every endpoint has capacity one.
    assert not packet.connect("A-R", "C-U")
    assert not packet.connect("A-R", "A-R")
    assert packet.connect("A-R", "B-L")
    assert not packet.connect("A-R", "B-D")
    assert packet.connect("B-D", "C-U")

    # Route construction and route use remain separate.  Direct avatar input
    # enters each linked port and transfers control to its paired endpoint.
    assert packet.enter("A-R")
    assert packet.avatar_panel == "B" and packet.avatar_marker == "B-L"
    assert packet.enter("B-D")
    assert packet.avatar_panel == "C" and packet.avatar_marker == "C-U"
    packet.avatar_marker = "exit"
    assert packet.avatar_panel == "C" and packet.avatar_marker == "exit"


if __name__ == "__main__":
    verify()
    print("PASS: The Pedestrian sign-panel route packet verified")
