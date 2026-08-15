#!/usr/bin/env python3
"""Verify the bounded Machinarium scrapyard dependency packet for GAME-0086."""

from __future__ import annotations

from dataclasses import dataclass, field


class RejectedAction(ValueError):
    """An observed action was attempted without its documented prerequisite."""


@dataclass
class ScrapyardState:
    inventory: set[str] = field(default_factory=set)
    body_exposed: bool = False
    torso_reachable: bool = False
    head_attached: bool = False
    tall: bool = False
    second_leg_attached: bool = False
    at_pole: bool = False
    pole_bent: bool = False
    second_arm_attached: bool = False
    exited: bool = False


class ScrapyardControl:
    def __init__(self) -> None:
        self.state = ScrapyardState()
        self.milestones: list[str] = []

    def _record(self, milestone: str) -> None:
        self.milestones.append(milestone)

    def remove_tub(self) -> None:
        self.state.body_exposed = True
        self._record("body-exposed")

    def drop_torso(self) -> None:
        if not self.state.body_exposed:
            raise RejectedAction("The torso is still covered by the tub")
        self.state.torso_reachable = True
        self._record("torso-reachable")

    def attach_head(self) -> None:
        if not self.state.torso_reachable:
            raise RejectedAction("The torso has not been dropped beside the head")
        self.state.head_attached = True
        self._record("head-attached")

    def set_height(self, tall: bool) -> None:
        if not self.state.head_attached:
            raise RejectedAction("Josef cannot change height before head and torso assembly")
        self.state.tall = tall
        self._record("body-extended" if tall else "body-contracted")

    def collect_doll(self) -> None:
        if not self.state.head_attached or not self.state.tall:
            raise RejectedAction("The high doll requires the assembled extended body")
        self.state.inventory.add("doll")
        self._record("doll-collected")

    def give_doll(self) -> None:
        if "doll" not in self.state.inventory:
            raise RejectedAction("The rodent exchange requires the doll")
        self.state.inventory.remove("doll")
        self.state.second_leg_attached = True
        self._record("second-leg-attached")

    def collect_tool_part(self, item: str) -> None:
        if not self.state.second_leg_attached:
            raise RejectedAction("Walking inventory collection requires the second leg")
        if item not in {"magnet", "string"}:
            raise RejectedAction(f"Unknown tool part: {item}")
        self.state.inventory.add(item)
        self._record(f"{item}-collected")

    def combine_magnet_and_string(self) -> None:
        if not {"magnet", "string"} <= self.state.inventory:
            raise RejectedAction("The fishing rig requires both magnet and string")
        self.state.inventory -= {"magnet", "string"}
        self.state.inventory.add("magnet-string")
        self._record("magnet-string-combined")

    def move_to_pole(self) -> None:
        if not self.state.second_leg_attached:
            raise RejectedAction("Josef cannot walk to the pole without both legs")
        self.state.at_pole = True
        self._record("pole-reached")

    def bend_pole(self) -> None:
        if not self.state.at_pole:
            raise RejectedAction("The pole is not reachable from the current position")
        self.state.pole_bent = True
        self._record("pole-bent")

    def apply_fishing_rig(self) -> None:
        if "magnet-string" not in self.state.inventory or not self.state.pole_bent:
            raise RejectedAction("Arm recovery requires the combined rig and bent pole")
        self.state.inventory.remove("magnet-string")
        self.state.second_arm_attached = True
        self._record("second-arm-attached")

    def exit_scrapyard(self) -> None:
        if not self.state.second_arm_attached:
            raise RejectedAction("The far side is unavailable before arm recovery")
        self.state.exited = True
        self._record("scrapyard-exited")


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid prerequisite order was accepted")


def main() -> None:
    invalid = ScrapyardControl()
    expect_rejected(invalid.drop_torso, "covered")
    expect_rejected(invalid.attach_head, "not been dropped")
    expect_rejected(lambda: invalid.set_height(True), "before head")
    expect_rejected(invalid.collect_doll, "extended")
    expect_rejected(invalid.give_doll, "requires the doll")
    expect_rejected(lambda: invalid.collect_tool_part("magnet"), "second leg")
    expect_rejected(invalid.combine_magnet_and_string, "both magnet and string")
    expect_rejected(invalid.bend_pole, "not reachable")
    expect_rejected(invalid.apply_fishing_rig, "combined rig and bent pole")
    expect_rejected(invalid.exit_scrapyard, "before arm recovery")

    control = ScrapyardControl()
    control.remove_tub()
    control.drop_torso()
    control.attach_head()
    control.set_height(True)
    control.collect_doll()
    control.set_height(False)
    control.give_doll()
    control.collect_tool_part("magnet")
    control.collect_tool_part("string")
    control.combine_magnet_and_string()
    control.move_to_pole()
    control.bend_pole()
    control.apply_fishing_rig()
    control.exit_scrapyard()

    assert control.state.exited
    assert control.state.second_leg_attached and control.state.second_arm_attached
    assert control.state.inventory == set()
    assert control.milestones == [
        "body-exposed",
        "torso-reachable",
        "head-attached",
        "body-extended",
        "doll-collected",
        "body-contracted",
        "second-leg-attached",
        "magnet-collected",
        "string-collected",
        "magnet-string-combined",
        "pole-reached",
        "pole-bent",
        "second-arm-attached",
        "scrapyard-exited",
    ]
    print(
        "Machinarium control verified: 14 ordered milestones, one two-part "
        "inventory combination, two restored limbs and ten rejected prerequisite violations."
    )


if __name__ == "__main__":
    main()
