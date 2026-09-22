#!/usr/bin/env python3
"""Verify the bounded Xbox 360 Jet Set Radio opening reconstruction."""

from dataclasses import dataclass, field


class RejectedAction(ValueError):
    """An action lacked a documented prerequisite."""


@dataclass
class SkaterState:
    phase: str = "gum-1"
    district: str | None = None
    time: int = 240
    stamina: int = 100
    spray: int = 0
    score: int = 0
    combo: int = 0
    attached_to: str | None = None
    completed_tags: set[str] = field(default_factory=set)
    police_wave: int = 0
    rank: str | None = None
    unlocked_stages: set[str] = field(default_factory=set)


class JetSetRadioControl:
    required_tags = {
        **{f"small-{index}": 1 for index in range(1, 5)},
        **{f"large-{index}": 3 for index in range(1, 6)},
        "xlarge-1": 7,
    }

    def __init__(self) -> None:
        self.state = SkaterState()
        self.milestones = ["fresh-new-game"]

    def complete_challenge(self, actor: str, index: int) -> None:
        expected = self.state.phase
        if expected != f"{actor.lower()}-{index}":
            raise RejectedAction(f"Expected {expected}")
        if actor == "Gum" and index < 3:
            self.state.phase = f"gum-{index + 1}"
        elif actor == "Gum" and index == 3:
            self.state.phase = "tab-1"
        elif actor == "Tab" and index < 3:
            self.state.phase = f"tab-{index + 1}"
        elif actor == "Tab" and index == 3:
            self.state.phase = "garage"
        else:
            raise RejectedAction("Unsupported introductory challenge")
        self.milestones.append(f"{actor.lower()}-{index}-complete")

    def enter_shibuya(self) -> None:
        if self.state.phase != "garage":
            raise RejectedAction("Introductory challenges remain")
        self.state.phase = "street"
        self.state.district = "Shibuya GG"
        self.milestones.append("shibuya-entered")

    def collect_spray(self, frames: int) -> None:
        if self.state.phase != "street" or frames not in {1, 5}:
            raise RejectedAction("Only one- or five-frame cans are eligible")
        self.state.spray += frames

    def attach_and_trick(self, surface: str, trick: str) -> None:
        if self.state.phase != "street" or surface not in {"rail", "wall"}:
            raise RejectedAction("No compatible traversal surface")
        self.state.attached_to = surface
        self.state.combo += 1
        self.state.score += 100 * self.state.combo
        self.milestones.append(f"{surface}-{trick}")

    def collide(self) -> None:
        self.state.attached_to = None
        self.state.combo = 0

    def spray_tag(self, tag: str, trace: tuple[str, ...] = ()) -> None:
        if self.state.phase != "street" or tag not in self.required_tags:
            raise RejectedAction("No eligible required graffiti point")
        if tag in self.state.completed_tags:
            raise RejectedAction("Graffiti point already complete")
        cost = self.required_tags[tag]
        expected_trace = () if cost == 1 else tuple("LRUD"[: min(cost, 4)])
        if self.state.spray < cost:
            raise RejectedAction("Insufficient spray frames")
        if trace != expected_trace:
            raise RejectedAction("Graffiti command trace is incomplete")
        self.state.spray -= cost
        self.state.completed_tags.add(tag)
        self.state.score += 500 * cost
        completed = len(self.state.completed_tags)
        if completed >= 3 and self.state.police_wave == 0:
            self.state.police_wave = 1
        if completed >= 8 and self.state.police_wave == 1:
            self.state.police_wave = 2

    def take_damage(self, amount: int) -> None:
        if amount <= 0:
            raise RejectedAction("Damage must be positive")
        self.state.stamina = max(0, self.state.stamina - amount)
        if self.state.stamina == 0:
            self.state.phase = "game-over"

    def elapse(self, seconds: int) -> None:
        if self.state.phase != "street" or not 0 < seconds <= self.state.time:
            raise RejectedAction("Invalid elapsed interval")
        self.state.time -= seconds
        if self.state.time == 0 and len(self.state.completed_tags) < len(self.required_tags):
            self.state.phase = "game-over"

    def settle(self) -> None:
        if self.state.phase != "street":
            raise RejectedAction("Street stage is not active")
        if set(self.required_tags) != self.state.completed_tags:
            raise RejectedAction("Required graffiti points remain")
        self.state.rank = "Nitro" if self.state.score < 30_000 else "Jet"
        self.state.phase = "results"
        self.state.unlocked_stages = {
            "Love Trap",
            "Monster of Kogane",
            "Benten Boogie",
        }
        self.milestones.append("shibuya-results")


def expect_rejected(action, fragment: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert fragment in str(error)
    else:
        raise AssertionError("Invalid action was accepted")


def main() -> None:
    invalid = JetSetRadioControl()
    expect_rejected(invalid.enter_shibuya, "challenges")
    for actor in ("Gum", "Tab"):
        for index in range(1, 4):
            invalid.complete_challenge(actor, index)
    invalid.enter_shibuya()
    expect_rejected(lambda: invalid.spray_tag("large-1", ("L", "R", "U")), "Insufficient")
    invalid.collect_spray(1)
    invalid.collect_spray(1)
    invalid.collect_spray(1)
    expect_rejected(lambda: invalid.spray_tag("large-1", ("L",)), "trace")

    control = JetSetRadioControl()
    for actor in ("Gum", "Tab"):
        for index in range(1, 4):
            control.complete_challenge(actor, index)
    assert control.state.phase == "garage"
    control.enter_shibuya()
    control.attach_and_trick("rail", "jump")
    control.attach_and_trick("wall", "ride")
    assert control.state.combo == 2
    control.collide()
    assert control.state.combo == 0

    for tag, cost in control.required_tags.items():
        while control.state.spray < cost:
            control.collect_spray(5 if cost - control.state.spray >= 5 else 1)
        trace = () if cost == 1 else tuple("LRUD"[: min(cost, 4)])
        control.spray_tag(tag, trace)
    assert control.state.police_wave == 2
    assert len(control.state.completed_tags) == 10
    control.settle()
    assert control.state.phase == "results"
    assert control.state.unlocked_stages == {
        "Love Trap",
        "Monster of Kogane",
        "Benten Boogie",
    }

    failed = JetSetRadioControl()
    for actor in ("Gum", "Tab"):
        for index in range(1, 4):
            failed.complete_challenge(actor, index)
    failed.enter_shibuya()
    failed.elapse(240)
    assert failed.state.phase == "game-over"

    print(
        "Jet Set Radio control verified: six staged introductions, rail/wall "
        "attachment, trick-chain reset, spray-stock legality, ten required "
        "tags, police escalation, deadline failure and graded successor result."
    )


if __name__ == "__main__":
    main()
