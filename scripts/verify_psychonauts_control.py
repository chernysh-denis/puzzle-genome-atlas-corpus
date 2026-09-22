#!/usr/bin/env python3
"""Verify the bounded original-Xbox Psychonauts Basic Braining model."""

from __future__ import annotations

from dataclasses import dataclass, field


class RejectedAction(ValueError):
    """An action was attempted outside the sourced packet or current state."""


@dataclass
class TrainingState:
    world: str = "real"
    phase: str = "kids-cabins"
    mental_health: int = 12
    astral_layers: int = 2
    checkpoint: str = "mind-entry"
    figment_points: int = 0
    psi_rank: int = 1
    tags: set[str] = field(default_factory=set)
    matched_baggage: set[str] = field(default_factory=set)
    gallery_score: int = 0
    gallery_open: bool = False
    course_complete: bool = False
    sasha_button: bool = False


class BasicBrainingControl:
    COURSE = (
        "kids-cabins",
        "part-one",
        "target-gallery",
        "part-two",
        "part-three",
        "white-corridor",
        "kids-cabins-successor",
    )

    def __init__(self) -> None:
        self.state = TrainingState()
        self.milestones = ["fresh-kids-cabins-control"]

    def enter_course(self) -> None:
        if self.state.phase != "kids-cabins":
            raise RejectedAction("Coach entry is not available")
        self.state.world = "mental"
        self.state.phase = "part-one"
        self.state.checkpoint = "part-one-entry"
        self.milestones.append("coach-mind-entered")

    def collect_figment(self, value: int) -> None:
        if self.state.world != "mental" or value <= 0:
            raise RejectedAction("Figment contact is not eligible")
        total = self.state.figment_points + value
        ranks, remainder = divmod(total, 100)
        self.state.psi_rank += ranks
        self.state.figment_points = remainder

    def collect_tag(self, kind: str) -> None:
        if self.state.world != "mental":
            raise RejectedAction("Luggage tags belong to a mental world")
        self.state.tags.add(kind)

    def match_baggage(self, *, tag: str, bag: str) -> None:
        if tag not in self.state.tags:
            raise RejectedAction("The matching tag has not been collected")
        if tag != bag:
            raise RejectedAction("Tag and emotional baggage types differ")
        self.state.tags.remove(tag)
        self.state.matched_baggage.add(bag)

    def reach_gallery(self) -> None:
        if self.state.phase != "part-one":
            raise RejectedAction("Part one has not reached its gallery gate")
        self.state.phase = "target-gallery"
        self.state.checkpoint = "gallery-entry"

    def strike_gallery_target(self, target_class: str) -> None:
        if self.state.phase != "target-gallery":
            raise RejectedAction("The target gallery is not active")
        if target_class == "enemy":
            self.state.gallery_score += 1
        elif target_class == "baby":
            self.state.gallery_score = max(0, self.state.gallery_score - 1)
        else:
            raise RejectedAction("Unknown gallery target class")
        if self.state.gallery_score >= 3:
            self.state.gallery_open = True

    def leave_gallery(self) -> None:
        if not self.state.gallery_open:
            raise RejectedAction("The gallery pass quota is not satisfied")
        self.state.phase = "part-two"
        self.state.checkpoint = "part-two-entry"

    def advance_course(self, expected: str, successor: str) -> None:
        if self.state.phase != expected:
            raise RejectedAction("Authored course order was violated")
        allowed = {
            ("part-two", "part-three"),
            ("part-three", "white-corridor"),
        }
        if (expected, successor) not in allowed:
            raise RejectedAction("Unknown course transition")
        self.state.phase = successor
        self.state.checkpoint = f"{successor}-entry"

    def take_damage(self, amount: int) -> None:
        if self.state.world != "mental" or amount <= 0:
            raise RejectedAction("Mental damage is not eligible")
        self.state.mental_health = max(0, self.state.mental_health - amount)
        if self.state.mental_health:
            return
        if self.state.astral_layers:
            self.state.astral_layers -= 1
            self.state.mental_health = 12
            self.milestones.append(f"returned:{self.state.checkpoint}")
            return
        self.state.world = "real"
        self.state.phase = "kids-cabins-ejected"
        self.milestones.append("ejected-from-mind")

    def settle_course(self) -> None:
        if self.state.phase != "white-corridor" or self.state.world != "mental":
            raise RejectedAction("The closing sequence is not eligible")
        self.state.world = "real"
        self.state.phase = "kids-cabins-successor"
        self.state.course_complete = True
        self.state.sasha_button = True
        self.milestones.append("basic-braining-settled")


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid Basic Braining transition was accepted")


def main() -> None:
    route = BasicBrainingControl()
    expect_rejected(lambda: route.collect_figment(5), "not eligible")
    route.enter_course()
    route.collect_figment(73)
    route.collect_figment(32)
    assert route.state.psi_rank == 2
    assert route.state.figment_points == 5
    route.collect_tag("steamer-trunk")
    expect_rejected(
        lambda: route.match_baggage(tag="steamer-trunk", bag="suitcase"),
        "differ",
    )
    route.match_baggage(tag="steamer-trunk", bag="steamer-trunk")
    assert route.state.matched_baggage == {"steamer-trunk"}
    route.reach_gallery()
    route.strike_gallery_target("enemy")
    route.strike_gallery_target("baby")
    expect_rejected(route.leave_gallery, "quota")
    for _ in range(3):
        route.strike_gallery_target("enemy")
    route.leave_gallery()
    route.advance_course("part-two", "part-three")
    route.advance_course("part-three", "white-corridor")
    route.settle_course()
    assert route.state.course_complete
    assert route.state.sasha_button
    assert route.state.world == "real"

    recover = BasicBrainingControl()
    recover.enter_course()
    recover.reach_gallery()
    recover.take_damage(12)
    assert recover.state.world == "mental"
    assert recover.state.astral_layers == 1
    assert recover.state.mental_health == 12
    assert recover.milestones[-1] == "returned:gallery-entry"

    eject = BasicBrainingControl()
    eject.enter_course()
    eject.state.astral_layers = 0
    eject.take_damage(12)
    assert eject.state.world == "real"
    assert eject.state.phase == "kids-cabins-ejected"
    assert not eject.state.course_complete

    print("Psychonauts Basic Braining bounded control model passed.")


if __name__ == "__main__":
    main()
