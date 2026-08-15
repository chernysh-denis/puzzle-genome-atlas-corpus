#!/usr/bin/env python3
"""Verify the bounded forced-perspective route used by GAME-0094."""

from dataclasses import dataclass
from math import isclose
from typing import Optional


BASE_HALF_EXTENT = 0.25
INITIAL_DISTANCE = 2.0
INITIAL_SCALE = 1.0
NEAR_BACKSTOP = 5.0
FAR_BACKSTOP = 10.0
TARGET_TOLERANCE = 0.05


@dataclass(frozen=True)
class Preview:
    distance: float
    scale: float
    half_extent: float
    backstop: float

    @property
    def apparent_extent(self) -> float:
        return self.scale / self.distance

    @property
    def far_edge(self) -> float:
        return self.distance + self.half_extent


def collision_bounded_preview(apparent_extent: float, backstop: float) -> Preview:
    """Maximise held distance while preserving projected extent and clearance."""
    if apparent_extent <= 0:
        raise ValueError("apparent extent must be positive")
    if backstop <= 0:
        raise ValueError("backstop must be in front of the camera")
    distance = backstop / (1.0 + BASE_HALF_EXTENT * apparent_extent)
    scale = apparent_extent * distance
    return Preview(distance, scale, BASE_HALF_EXTENT * scale, backstop)


@dataclass
class InductionRoom:
    piece_distance: float = INITIAL_DISTANCE
    piece_scale: float = INITIAL_SCALE
    held: bool = False
    apparent_extent: Optional[float] = None
    preview: Optional[Preview] = None
    piece_on_plate: bool = False
    player_at_exit: bool = False

    @property
    def door_open(self) -> bool:
        return self.piece_on_plate

    @property
    def complete(self) -> bool:
        return self.player_at_exit

    def grab_piece(self) -> None:
        if self.complete:
            raise ValueError("completed room is no longer interactive")
        if self.held:
            raise ValueError("piece is already held")
        self.held = True
        self.piece_on_plate = False
        self.apparent_extent = self.piece_scale / self.piece_distance
        self.preview = None

    def aim_at_backstop(self, backstop: float) -> Preview:
        if not self.held or self.apparent_extent is None:
            raise ValueError("piece must be held before aiming")
        self.preview = collision_bounded_preview(self.apparent_extent, backstop)
        return self.preview

    def force_unsafe_preview(self, distance: float, backstop: float) -> None:
        if not self.held or self.apparent_extent is None:
            raise ValueError("piece must be held before placement")
        scale = self.apparent_extent * distance
        far_edge = distance + BASE_HALF_EXTENT * scale
        if far_edge > backstop:
            raise ValueError("candidate placement intersects the backstop")
        raise AssertionError("unsafe test distance unexpectedly fit")

    def release_on_plate(self, plate_distance: float) -> None:
        if not self.held or self.preview is None:
            raise ValueError("piece needs a live held preview before release")
        if abs(self.preview.distance - plate_distance) > TARGET_TOLERANCE:
            raise ValueError("preview does not overlap the pressure plate")
        self.piece_distance = self.preview.distance
        self.piece_scale = self.preview.scale
        self.held = False
        self.apparent_extent = None
        self.preview = None
        self.piece_on_plate = True

    def enter_exit(self) -> None:
        if not self.door_open:
            raise ValueError("linked exit is closed")
        self.player_at_exit = True


def expect_rejection(operation, message: str) -> None:
    try:
        operation()
    except ValueError:
        return
    raise AssertionError(message)


def verify() -> None:
    room = InductionRoom()
    target = collision_bounded_preview(INITIAL_SCALE / INITIAL_DISTANCE, FAR_BACKSTOP)

    expect_rejection(
        lambda: room.aim_at_backstop(NEAR_BACKSTOP),
        "unheld piece accepted an aim update",
    )
    expect_rejection(
        lambda: room.release_on_plate(target.distance),
        "unheld piece was released",
    )
    expect_rejection(room.enter_exit, "closed exit admitted the player")

    room.grab_piece()
    near = room.aim_at_backstop(NEAR_BACKSTOP)
    far = room.aim_at_backstop(FAR_BACKSTOP)
    assert far.distance > near.distance
    assert far.scale > near.scale
    assert isclose(near.apparent_extent, far.apparent_extent)
    assert isclose(near.far_edge, NEAR_BACKSTOP)
    assert isclose(far.far_edge, FAR_BACKSTOP)
    expect_rejection(
        lambda: room.force_unsafe_preview(FAR_BACKSTOP, FAR_BACKSTOP),
        "interpenetrating placement was accepted",
    )

    room.aim_at_backstop(NEAR_BACKSTOP)
    expect_rejection(
        lambda: room.release_on_plate(target.distance),
        "near preview activated the remote plate",
    )
    room.aim_at_backstop(FAR_BACKSTOP)
    room.release_on_plate(target.distance)
    assert room.door_open
    assert room.piece_scale > INITIAL_SCALE

    room.grab_piece()
    assert not room.door_open
    expect_rejection(room.enter_exit, "door stayed open after plate vacancy")
    room.aim_at_backstop(FAR_BACKSTOP)
    room.release_on_plate(target.distance)
    room.enter_exit()
    assert room.complete and room.door_open

    print(
        "Superliminal control verified: two collision-bounded sightline "
        "previews, invariant apparent extent, one persistent fourfold-plus "
        "world-scale change, occupancy-linked exit completion and six rejected "
        "invalid transitions."
    )


if __name__ == "__main__":
    verify()
