#!/usr/bin/env python3
"""Verify the bounded original-PS2 Shadow of the Colossus opening model."""

from __future__ import annotations

from dataclasses import dataclass


class RejectedAction(ValueError):
    """An action was attempted outside the sourced packet or current state."""


@dataclass
class HuntState:
    phase: str = "shrine-control"
    health: int = 100
    grip: int = 100
    mounted: bool = False
    agro_near: bool = False
    direct_sunlight: bool = False
    bearing_known: bool = False
    arena_reached: bool = False
    attached_region: str | None = None
    stable_support: bool = True
    leg_wound_depleted: bool = False
    guardian_kneeling: bool = False
    crown_reached: bool = False
    crown_sigil_visible: bool = False
    guardian_health: int = 5
    returned_to_shrine: bool = False


class ShadowControl:
    def __init__(self) -> None:
        self.state = HuntState()
        self.milestones = ["fresh-shrine-control"]

    def call_agro(self) -> None:
        if self.state.phase not in {"shrine-control", "field-route"}:
            raise RejectedAction("Agro cannot enter the current region")
        self.state.agro_near = True

    def mount(self) -> None:
        if not self.state.agro_near:
            raise RejectedAction("Agro is not within mounting reach")
        self.state.mounted = True
        self.state.phase = "field-route"

    def dismount(self) -> None:
        if not self.state.mounted:
            raise RejectedAction("Wander is not mounted")
        self.state.mounted = False

    def focus_sword(self, *, in_sunlight: bool, aligned: bool) -> None:
        self.state.direct_sunlight = in_sunlight
        if not in_sunlight:
            raise RejectedAction("Guiding rays require direct sunlight")
        if not aligned:
            raise RejectedAction("The rays have not converged")
        self.state.bearing_known = True
        self.milestones.append("first-colossus-bearing")

    def reach_arena(self) -> None:
        if not self.state.bearing_known:
            raise RejectedAction("Current target bearing is unknown")
        if self.state.mounted:
            raise RejectedAction("The cliff approach requires dismounting")
        self.state.arena_reached = True
        self.state.phase = "guardian-live"

    def grip(self, region: str, *, compatible: bool = True) -> None:
        if self.state.phase != "guardian-live" or not compatible:
            raise RejectedAction("No compatible reachable grip")
        if self.state.grip <= 0:
            raise RejectedAction("No usable grip remains")
        if region == "back" and not self.state.guardian_kneeling:
            raise RejectedAction("The upward body route is not connected")
        self.state.attached_region = region
        self.state.stable_support = False

    def climb(self, cost: int) -> None:
        if self.state.attached_region is None:
            raise RejectedAction("Wander is not attached")
        if cost <= 0:
            raise RejectedAction("Grip cost must be positive")
        self.state.grip = max(0, self.state.grip - cost)
        if self.state.grip == 0:
            self.state.attached_region = None
            self.state.stable_support = False

    def rest(self, recovered: int) -> None:
        if not self.state.stable_support or self.state.attached_region is not None:
            raise RejectedAction("No stable rest surface")
        if recovered <= 0:
            raise RejectedAction("Recovery must be positive")
        self.state.grip = min(100, self.state.grip + recovered)

    def release_to_ledge(self) -> None:
        if self.state.attached_region is None:
            raise RejectedAction("No active attachment")
        self.state.attached_region = None
        self.state.stable_support = True

    def stab_leg_wound(self) -> None:
        if self.state.attached_region != "rear-left-leg":
            raise RejectedAction("Leg wound is not reachable from current grip")
        self.state.leg_wound_depleted = True
        self.state.guardian_kneeling = True
        self.milestones.append("leg-wound-kneel")

    def reach_crown(self) -> None:
        if not self.state.guardian_kneeling:
            raise RejectedAction("Guardian topology has not opened")
        if self.state.attached_region != "back":
            raise RejectedAction("Crown route requires the connected back climb")
        self.state.attached_region = "crown"
        self.state.crown_reached = True
        self.state.crown_sigil_visible = True

    def stab_crown(self, *, charged: bool) -> None:
        if self.state.attached_region != "crown" or not self.state.crown_sigil_visible:
            raise RejectedAction("Major sigil is not legally reachable")
        if not charged:
            raise RejectedAction("The bounded route uses a prepared stab")
        self.state.guardian_health = max(0, self.state.guardian_health - 2)
        if self.state.guardian_health == 0:
            self.state.phase = "automatic-return"
            self.state.attached_region = None
            self.milestones.append("first-colossus-defeated")

    def guardian_shake(self, grip_cost: int) -> None:
        if self.state.attached_region is None:
            return
        self.climb(grip_cost)

    def take_damage(self, amount: int) -> None:
        if amount <= 0:
            raise RejectedAction("Damage must be positive")
        self.state.health = max(0, self.state.health - amount)
        if self.state.health == 0:
            self.state.phase = "failed"

    def complete_return(self) -> None:
        if self.state.phase != "automatic-return":
            raise RejectedAction("Victory return has not begun")
        self.state.phase = "shrine-successor-control"
        self.state.returned_to_shrine = True
        self.milestones.append("shrine-successor-control")


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid hunt transition was accepted")


def main() -> None:
    control = ShadowControl()
    expect_rejected(control.mount, "reach")
    expect_rejected(
        lambda: control.focus_sword(in_sunlight=False, aligned=True), "sunlight"
    )
    control.call_agro()
    control.mount()
    control.focus_sword(in_sunlight=True, aligned=True)
    control.dismount()
    control.reach_arena()

    expect_rejected(lambda: control.grip("back"), "not connected")
    control.grip("rear-left-leg")
    control.climb(20)
    control.stab_leg_wound()
    control.release_to_ledge()
    control.rest(20)
    control.grip("back")
    control.climb(35)
    control.guardian_shake(10)
    control.reach_crown()
    control.stab_crown(charged=True)
    control.stab_crown(charged=True)
    control.stab_crown(charged=True)
    assert control.state.guardian_health == 0
    control.complete_return()
    assert control.state.returned_to_shrine
    assert control.state.phase == "shrine-successor-control"

    fall = ShadowControl()
    fall.state.phase = "guardian-live"
    fall.state.grip = 5
    fall.grip("rear-left-leg")
    fall.climb(5)
    assert fall.state.attached_region is None
    assert fall.state.phase == "guardian-live"

    defeated = ShadowControl()
    defeated.take_damage(100)
    assert defeated.state.phase == "failed"

    print("Shadow of the Colossus bounded control model passed.")


if __name__ == "__main__":
    main()
