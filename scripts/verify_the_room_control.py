#!/usr/bin/env python3
"""Verify the bounded Chapter 1 dependency packet used for GAME-0085."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SafeState:
    inventory: set[str] = field(default_factory=set)
    key_shape: str | None = None
    side_keyhole_visible: bool = False
    front_keyhole_visible: bool = False
    front_rings_visible: bool = False
    lens_equipped: bool = False
    ring_matches: set[str] = field(default_factory=set)
    door_unlatched: bool = False
    door_open: bool = False


class RejectedAction(ValueError):
    """An observed manipulation attempted before its documented prerequisite."""


class ChapterOneControl:
    ring_names = frozenset({"inner", "middle", "outer"})

    def __init__(self) -> None:
        self.state = SafeState()
        self.milestones: list[str] = []

    def _record(self, milestone: str) -> None:
        self.milestones.append(milestone)

    def press_fire_symbol(self) -> None:
        self.state.inventory.add("peculiar-key")
        self._record("fire-compartment-open")

    def reveal_side_keyhole(self) -> None:
        self.state.side_keyhole_visible = True
        self._record("side-keyhole-visible")

    def reshape_key(self, shape: str) -> None:
        if "peculiar-key" not in self.state.inventory:
            raise RejectedAction("The peculiar key has not been collected")
        if shape not in {"spiral", "crown"}:
            raise RejectedAction("The control supports only spiral and crown key shapes")
        self.state.key_shape = shape
        self._record(f"key-shaped-{shape}")

    def unlock_side_panel(self) -> None:
        if not self.state.side_keyhole_visible or self.state.key_shape != "spiral":
            raise RejectedAction("The side fixture requires its exposed spiral key state")
        self.state.inventory.add("metal-plate-wrench")
        self._record("metal-plate-collected")

    def remove_logo_screw(self) -> None:
        if "metal-plate-wrench" not in self.state.inventory:
            raise RejectedAction("The logo screw requires the metal plate used as a wrench")
        self.state.inventory.add("eyepiece-lens")
        self._record("eyepiece-lens-collected")

    def reveal_front_keyhole(self) -> None:
        self.state.front_keyhole_visible = True
        self._record("front-keyhole-visible")

    def unlock_front_panel(self) -> None:
        if not self.state.front_keyhole_visible or self.state.key_shape != "crown":
            raise RejectedAction("The front fixture requires its exposed crown key state")
        self.state.front_rings_visible = True
        self._record("front-rings-visible")

    def equip_eyepiece(self) -> None:
        if "eyepiece-lens" not in self.state.inventory:
            raise RejectedAction("The hidden ring trace is unavailable without the lens")
        self.state.lens_equipped = True
        self._record("hidden-trace-visible")

    def align_ring(self, ring: str) -> None:
        if not self.state.front_rings_visible or not self.state.lens_equipped:
            raise RejectedAction("Ring matching requires exposed rings and the active eyepiece")
        if ring not in self.ring_names:
            raise RejectedAction(f"Unknown ring: {ring}")
        self.state.ring_matches.add(ring)
        self._record(f"{ring}-ring-matched")
        if self.state.ring_matches == self.ring_names:
            self.state.door_unlatched = True

    def open_door(self) -> None:
        if not self.state.door_unlatched:
            raise RejectedAction("All three rings must match the hidden trace")
        self.state.door_open = True
        self._record("safe-door-open")


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid prerequisite order was accepted")


def main() -> None:
    invalid = ChapterOneControl()
    expect_rejected(invalid.unlock_side_panel, "spiral")
    expect_rejected(invalid.remove_logo_screw, "metal plate")
    expect_rejected(invalid.unlock_front_panel, "crown")
    expect_rejected(invalid.equip_eyepiece, "without the lens")
    expect_rejected(lambda: invalid.align_ring("inner"), "exposed rings")
    expect_rejected(invalid.open_door, "All three rings")

    control = ChapterOneControl()
    control.press_fire_symbol()
    control.reveal_side_keyhole()
    control.reshape_key("spiral")
    control.unlock_side_panel()
    control.remove_logo_screw()
    control.reveal_front_keyhole()
    control.reshape_key("crown")
    control.unlock_front_panel()
    control.equip_eyepiece()
    for ring in ("inner", "middle", "outer"):
        control.align_ring(ring)
    control.open_door()

    assert control.state.door_open
    assert control.state.ring_matches == control.ring_names
    assert control.milestones == [
        "fire-compartment-open",
        "side-keyhole-visible",
        "key-shaped-spiral",
        "metal-plate-collected",
        "eyepiece-lens-collected",
        "front-keyhole-visible",
        "key-shaped-crown",
        "front-rings-visible",
        "hidden-trace-visible",
        "inner-ring-matched",
        "middle-ring-matched",
        "outer-ring-matched",
        "safe-door-open",
    ]
    print(
        "The Room control verified: 13 ordered milestones, two key shapes, "
        "one lens-gated three-ring trace and six rejected prerequisite violations."
    )


if __name__ == "__main__":
    main()
