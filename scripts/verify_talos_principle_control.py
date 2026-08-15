#!/usr/bin/env python3
"""Verify the bounded A1 sigil-gate packet used by GAME-0090."""

from dataclasses import dataclass, field


Cell = tuple[int, int]


SHAPES: dict[str, frozenset[Cell]] = {
    "L": frozenset({(0, 0), (0, 1), (0, 2), (1, 2)}),
    "J": frozenset({(1, 0), (1, 1), (1, 2), (0, 2)}),
    "Z": frozenset({(0, 0), (1, 0), (1, 1), (2, 1)}),
}
REQUIRED = frozenset(SHAPES)
BOARD = frozenset((x, y) for x in range(4) for y in range(3))


def rotate(shape: frozenset[Cell], turns: int) -> frozenset[Cell]:
    cells = set(shape)
    for _ in range(turns % 4):
        cells = {(-y, x) for x, y in cells}
    min_x = min(x for x, _ in cells)
    min_y = min(y for _, y in cells)
    return frozenset((x - min_x, y - min_y) for x, y in cells)


@dataclass
class SigilGate:
    collected: set[str] = field(default_factory=set)
    placements: dict[str, frozenset[Cell]] = field(default_factory=dict)
    gate_open: bool = False

    def collect(self, sigil: str) -> None:
        if sigil not in REQUIRED:
            raise ValueError("sigil does not belong to this A1 gate")
        if sigil in self.collected:
            raise ValueError("sigil has already been credited")
        self.collected.add(sigil)

    def enter_arranger(self) -> None:
        if self.collected != set(REQUIRED):
            raise ValueError("all three addressed green sigils are required")

    def place(self, sigil: str, turns: int, offset: Cell) -> None:
        if sigil not in self.collected:
            raise ValueError("uncollected sigil is unavailable")
        if sigil in self.placements:
            raise ValueError("each collected identity can be placed once")
        dx, dy = offset
        footprint = frozenset((x + dx, y + dy) for x, y in rotate(SHAPES[sigil], turns))
        if not footprint <= BOARD:
            raise ValueError("complete footprint must stay inside the board")
        occupied = set().union(*self.placements.values()) if self.placements else set()
        if occupied.intersection(footprint):
            raise ValueError("sigil footprints cannot overlap")
        self.placements[sigil] = footprint
        occupied.update(footprint)
        if set(self.placements) == set(REQUIRED) and occupied == set(BOARD):
            self.gate_open = True


def expect_rejection(operation, message: str) -> None:
    try:
        operation()
    except ValueError:
        return
    raise AssertionError(message)


def verify() -> None:
    gate = SigilGate()

    expect_rejection(lambda: gate.collect("T"), "foreign shape was credited")
    gate.collect("L")
    expect_rejection(lambda: gate.collect("L"), "duplicate sigil was credited")
    expect_rejection(gate.enter_arranger, "arranger opened before its exact roster")
    gate.collect("J")
    gate.collect("Z")
    gate.enter_arranger()

    out_of_bounds = SigilGate(collected=set(REQUIRED))
    expect_rejection(
        lambda: out_of_bounds.place("L", 0, (3, 0)),
        "out-of-bounds footprint was accepted",
    )

    overlap = SigilGate(collected=set(REQUIRED))
    overlap.place("L", 0, (0, 0))
    expect_rejection(
        lambda: overlap.place("J", 2, (0, 0)),
        "overlapping footprint was accepted",
    )

    incomplete = SigilGate(collected=set(REQUIRED))
    incomplete.place("L", 0, (0, 0))
    incomplete.place("J", 3, (1, 0))
    assert not incomplete.gate_open, "partial cover opened the gate"

    # Exact 4 × 3 cover: L on the left, rotated J across the top-right and Z
    # across the remaining lower-right cells.
    gate.place("L", 0, (0, 0))
    gate.place("J", 3, (1, 0))
    gate.place("Z", 0, (1, 1))
    assert set().union(*gate.placements.values()) == set(BOARD)
    assert gate.gate_open, "gapless exact cover did not open the gate immediately"

    print(
        "The Talos Principle control verified: three distinct green sigils, "
        "one 4x3 exact-cover arranger, immediate persistent gate access and "
        "six rejected invalid transitions."
    )


if __name__ == "__main__":
    verify()
