#!/usr/bin/env python3
"""Verify the bounded original-GameCube Metroid Prime prologue model."""

from __future__ import annotations

from dataclasses import dataclass, field


class RejectedAction(ValueError):
    """An action was attempted outside the sourced packet or current state."""


STARTING_CAPABILITIES = {
    "power-suit",
    "varia-suit",
    "power-beam",
    "charge-beam",
    "combat-visor",
    "scan-visor",
    "missiles",
    "morph-ball",
    "morph-ball-bombs",
    "grapple-beam",
    "space-jump-boots",
}
RETAINED_CAPABILITIES = {
    "power-suit",
    "power-beam",
    "combat-visor",
    "scan-visor",
}


@dataclass
class PrologueState:
    phase: str = "exterior-air-lock"
    visor: str = "combat-visor"
    energy: int = 99
    missiles: int = 5
    capabilities: set[str] = field(
        default_factory=lambda: set(STARTING_CAPABILITIES)
    )
    scans: set[str] = field(default_factory=set)
    fixtures: set[str] = field(default_factory=set)
    scan_target: str | None = None
    scan_progress: int = 0
    lock_target: str | None = None
    queen_health: int = 5
    queen_weakness_known: bool = False
    escape_seconds: int | None = None
    morph_ball: bool = False
    grapple_crossed: bool = False
    landed: bool = False


class MetroidPrimeControl:
    scan_responses = {
        "exterior-console": ("fixture", "exterior-field-released"),
        "lift-console": ("fixture", "lift-active"),
        "turret-console": ("fixture", "turret-disabled"),
        "parasite-queen": ("weak-point", "parasite-queen-head"),
        "ship-log": ("data", "ship-log"),
    }

    def __init__(self) -> None:
        self.state = PrologueState()
        self.milestones = ["fresh-new-game-control"]

    def switch_visor(self, visor: str) -> None:
        self._require_capability(visor)
        if visor not in {"combat-visor", "scan-visor"}:
            raise RejectedAction("Unsupported visor")
        self.state.visor = visor

    def begin_scan(self, target: str, *, in_range: bool = True) -> None:
        self._require_capability("scan-visor")
        if self.state.visor != "scan-visor":
            raise RejectedAction("Scan Visor is not active")
        if target not in self.scan_responses:
            raise RejectedAction("Target is not eligible")
        if not in_range:
            raise RejectedAction("Target is outside scan range")
        self.state.scan_target = target
        self.state.scan_progress = 0

    def hold_scan(self, steps: int = 3, *, remains_in_range: bool = True) -> None:
        if self.state.scan_target is None:
            raise RejectedAction("No scan target is locked")
        if steps <= 0:
            raise RejectedAction("Scan progress must be positive")
        if not remains_in_range:
            self.state.scan_target = None
            self.state.scan_progress = 0
            raise RejectedAction("Target left scan range")
        self.state.scan_progress += steps
        if self.state.scan_progress < 3:
            return
        target = self.state.scan_target
        response, value = self.scan_responses[target]
        self.state.scans.add(target)
        if response == "fixture":
            self.state.fixtures.add(value)
        elif response == "weak-point":
            self.state.queen_weakness_known = True
        elif response != "data":
            raise AssertionError("Unknown scan response")
        self.state.scan_target = None
        self.state.scan_progress = 0
        self.milestones.append(f"scan-{response}-{value}")

    def enter_ship(self) -> None:
        if "exterior-field-released" not in self.state.fixtures:
            raise RejectedAction("Exterior field remains active")
        self.state.phase = "frigate-interior"
        self.milestones.append("entered-frigate")

    def lock_target(self, target: str) -> None:
        self._require_capability("combat-visor")
        if self.state.visor != "combat-visor":
            raise RejectedAction("Combat Visor is not active")
        if target == "parasite-queen" and not self.state.queen_weakness_known:
            raise RejectedAction("Queen weak point is not disclosed")
        self.state.lock_target = target

    def orbit_or_dash(self, direction: str) -> None:
        if self.state.lock_target is None:
            raise RejectedAction("No retained combat target")
        if direction not in {"left", "right", "toward", "away"}:
            raise RejectedAction("Unsupported target-relative direction")
        self.milestones.append(f"relative-move-{direction}")

    def fire_beam(self, *, charged: bool = False) -> None:
        self._require_capability("power-beam")
        if charged:
            self._require_capability("charge-beam")
        self._damage_current_target(2 if charged else 1)

    def fire_missile(self) -> None:
        self._require_capability("missiles")
        if self.state.missiles < 1:
            raise RejectedAction("No compatible missile remains")
        self.state.missiles -= 1
        self._damage_current_target(2)

    def _damage_current_target(self, amount: int) -> None:
        if self.state.lock_target != "parasite-queen":
            return
        if not self.state.queen_weakness_known:
            raise RejectedAction("Queen head is not a legal damage target")
        self.state.queen_health = max(0, self.state.queen_health - amount)
        if self.state.queen_health == 0 and self.state.escape_seconds is None:
            self.state.escape_seconds = 420
            self.state.phase = "evacuation"
            self.milestones.append("queen-cleared-evacuation-420")

    def morph(self, enabled: bool) -> None:
        self._require_capability("morph-ball")
        self.state.morph_ball = enabled

    def cross_vent(self) -> None:
        if self.state.phase != "evacuation" or not self.state.morph_ball:
            raise RejectedAction("Evacuation vent requires Morph Ball")
        self.milestones.append("vent-crossed")

    def grapple_gap(self, *, legal_node: bool = True) -> None:
        self._require_capability("grapple-beam")
        if self.state.phase != "evacuation" or not legal_node:
            raise RejectedAction("No legal evacuation Grapple node")
        self.state.grapple_crossed = True
        self.milestones.append("grapple-gap-crossed")

    def advance_escape(self, seconds: int) -> None:
        if self.state.escape_seconds is None:
            raise RejectedAction("Evacuation has not begun")
        if seconds <= 0:
            raise RejectedAction("Time advance must be positive")
        self.state.escape_seconds = max(0, self.state.escape_seconds - seconds)
        if self.state.escape_seconds == 0:
            self.state.phase = "failed"

    def take_damage(self, amount: int) -> None:
        if amount <= 0:
            raise RejectedAction("Damage must be positive")
        self.state.energy = max(0, self.state.energy - amount)
        if self.state.energy == 0:
            self.state.phase = "failed"

    def hull_collision(self) -> None:
        if self.state.phase != "evacuation" or not self.state.grapple_crossed:
            raise RejectedAction("Authored collision is not yet reachable")
        self.state.capabilities = set(RETAINED_CAPABILITIES)
        self.state.morph_ball = False
        self.state.phase = "reduced-escape"
        self.milestones.append("advanced-capabilities-disabled")

    def exit_and_land(self) -> None:
        if self.state.phase != "reduced-escape":
            raise RejectedAction("Reduced escape state is not active")
        if self.state.escape_seconds is None or self.state.escape_seconds == 0:
            raise RejectedAction("Evacuation deadline expired")
        if self.state.capabilities != RETAINED_CAPABILITIES:
            raise RejectedAction("Reduced loadout is not authoritative")
        self.state.phase = "tallon-overworld-control"
        self.state.landed = True
        self.milestones.append("tallon-overworld-control")

    def _require_capability(self, capability: str) -> None:
        if capability not in self.state.capabilities:
            raise RejectedAction(f"Capability is unavailable: {capability}")


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid prologue transition was accepted")


def main() -> None:
    control = MetroidPrimeControl()
    expect_rejected(control.enter_ship, "field")
    control.switch_visor("scan-visor")
    expect_rejected(
        lambda: control.begin_scan("exterior-console", in_range=False), "range"
    )
    control.begin_scan("exterior-console")
    control.hold_scan(2)
    assert "exterior-field-released" not in control.state.fixtures
    control.hold_scan(1)
    control.enter_ship()

    control.begin_scan("ship-log")
    expect_rejected(
        lambda: control.hold_scan(1, remains_in_range=False), "range"
    )
    control.begin_scan("parasite-queen")
    control.hold_scan()
    assert control.state.queen_weakness_known

    control.switch_visor("combat-visor")
    control.lock_target("parasite-queen")
    control.orbit_or_dash("left")
    control.fire_missile()
    control.fire_beam(charged=True)
    control.fire_beam()
    assert control.state.queen_health == 0
    assert control.state.escape_seconds == 420

    control.morph(True)
    control.cross_vent()
    control.morph(False)
    expect_rejected(lambda: control.grapple_gap(legal_node=False), "legal")
    control.grapple_gap()
    control.advance_escape(120)
    control.hull_collision()
    assert control.state.capabilities == RETAINED_CAPABILITIES
    expect_rejected(lambda: control.morph(True), "unavailable")
    expect_rejected(control.fire_missile, "unavailable")
    control.switch_visor("scan-visor")
    control.exit_and_land()
    assert control.state.landed
    assert control.state.phase == "tallon-overworld-control"
    assert "tallon-overworld-control" in control.milestones

    timeout = MetroidPrimeControl()
    timeout.state.escape_seconds = 1
    timeout.state.phase = "evacuation"
    timeout.advance_escape(1)
    assert timeout.state.phase == "failed"

    defeated = MetroidPrimeControl()
    defeated.take_damage(99)
    assert defeated.state.phase == "failed"

    print("Metroid Prime bounded control model passed.")


if __name__ == "__main__":
    main()
