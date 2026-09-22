#!/usr/bin/env python3
"""Verify the bounded Ultimate DOOM v1.9 E1M1 state reconstruction."""

from __future__ import annotations

from dataclasses import dataclass, field


class RejectedAction(ValueError):
    """An action was attempted outside the documented E1M1 packet."""


@dataclass
class DoomState:
    map_name: str = "E1M1"
    skill: str = "Hurt Me Plenty"
    health: int = 100
    armour: int = 0
    armour_class: int = 0
    bullets: int = 50
    shells: int = 0
    owned_weapons: set[str] = field(default_factory=lambda: {"fist", "pistol"})
    active_weapon: str = "pistol"
    cards: set[str] = field(default_factory=set)
    awakened: set[str] = field(default_factory=set)
    mapped_lines: set[str] = field(default_factory=set)
    opened_doors: set[str] = field(default_factory=set)
    kills: int = 0
    items: int = 0
    secrets: int = 0
    live: bool = True
    terminal: str | None = None


class DoomE1M1Control:
    bullet_cap = 200
    shell_cap = 50

    def __init__(self) -> None:
        self.state = DoomState()
        self.milestones = ["fresh-hmp-e1m1"]

    def move(self, line: str) -> None:
        self._require_live()
        self.state.mapped_lines.add(line)

    def use_door(self, door: str, requires_key: str | None = None) -> None:
        self._require_live()
        if requires_key is not None and requires_key not in self.state.cards:
            raise RejectedAction("Required key card is not carried")
        self.state.opened_doors.add(door)

    def awaken(self, monster: str, *, sight: bool = False, noise: bool = False) -> None:
        self._require_live()
        if not sight and not noise:
            raise RejectedAction("No sight or noise stimulus reached the monster")
        self.state.awakened.add(monster)

    def select_weapon(self, weapon: str) -> None:
        self._require_live()
        if weapon not in self.state.owned_weapons:
            raise RejectedAction("Weapon is not owned")
        self.state.active_weapon = weapon

    def fire(self, target: str) -> None:
        self._require_live()
        weapon = self.state.active_weapon
        if weapon == "pistol":
            if self.state.bullets < 1:
                raise RejectedAction("No compatible bullet remains")
            self.state.bullets -= 1
        elif weapon == "shotgun":
            if self.state.shells < 1:
                raise RejectedAction("No compatible shell remains")
            self.state.shells -= 1
        elif weapon != "fist":
            raise RejectedAction("Weapon is outside the scoped loadout")
        self.state.awakened.add(target)

    def pick_ammo(self, ammo: str, amount: int) -> None:
        self._require_live()
        if amount <= 0:
            raise RejectedAction("Pickup amount must be positive")
        if ammo == "bullets":
            before = self.state.bullets
            self.state.bullets = min(self.bullet_cap, before + amount)
            accepted = self.state.bullets - before
        elif ammo == "shells":
            before = self.state.shells
            self.state.shells = min(self.shell_cap, before + amount)
            accepted = self.state.shells - before
        else:
            raise RejectedAction("Ammunition type is outside the scoped loadout")
        if accepted == 0:
            raise RejectedAction("Compatible ammunition reserve is already full")
        self.state.items += 1

    def pick_shotgun(self, shells_granted: int = 8) -> None:
        self._require_live()
        self.state.owned_weapons.add("shotgun")
        self.state.shells = min(self.shell_cap, self.state.shells + shells_granted)
        self.state.items += 1

    def pick_health(self, amount: int, cap: int = 100) -> None:
        self._require_live()
        if self.state.health >= cap:
            raise RejectedAction("Health state cannot accept this pickup")
        self.state.health = min(cap, self.state.health + amount)
        self.state.items += 1

    def pick_armour(self, armour_class: int, reserve: int) -> None:
        self._require_live()
        if armour_class not in {1, 2} or reserve <= 0:
            raise RejectedAction("Unsupported armour pickup")
        if armour_class < self.state.armour_class:
            raise RejectedAction("Weaker armour class does not replace current armour")
        self.state.armour_class = armour_class
        self.state.armour = reserve
        self.state.items += 1

    def receive_damage(self, damage: int) -> tuple[int, int]:
        self._require_live()
        if damage <= 0:
            raise RejectedAction("Damage must be positive")
        if self.state.armour_class == 1:
            saved = damage // 3
        elif self.state.armour_class == 2:
            saved = damage // 2
        else:
            saved = 0
        saved = min(saved, self.state.armour)
        self.state.armour -= saved
        health_damage = damage - saved
        self.state.health = max(0, self.state.health - health_damage)
        if self.state.health == 0:
            self.state.live = False
            self.state.terminal = "death"
        return saved, health_damage

    def defeat(self, monster: str) -> None:
        self._require_live()
        if monster not in self.state.awakened:
            raise RejectedAction("Monster was never acquired into live combat")
        self.state.awakened.remove(monster)
        self.state.kills += 1

    def use_exit_switch(self) -> None:
        self._require_live()
        if "exit-room" not in self.state.opened_doors:
            raise RejectedAction("Exit room is not traversably connected")
        self.state.live = False
        self.state.terminal = "intermission-e1m2"
        self.milestones.append("e1m1-complete")

    def restart(self) -> None:
        if self.state.terminal != "death":
            raise RejectedAction("Restart requires the death state")
        self.state = DoomState()
        self.milestones.append("fresh-hmp-e1m1")

    def _require_live(self) -> None:
        if not self.state.live:
            raise RejectedAction("The E1M1 attempt is already settled")


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid E1M1 action was accepted")


def main() -> None:
    control = DoomE1M1Control()
    assert control.state.health == 100
    assert control.state.armour == 0
    assert control.state.bullets == 50
    assert control.state.cards == set()
    expect_rejected(lambda: control.select_weapon("shotgun"), "not owned")
    expect_rejected(lambda: control.use_door("blue-door", "blue"), "key card")

    control.move("start-to-armour-room")
    control.pick_armour(1, 100)
    saved, health_damage = control.receive_damage(10)
    assert (saved, health_damage) == (3, 7)
    assert control.state.armour == 97
    assert control.state.health == 93
    expect_rejected(lambda: control.pick_armour(0, 100), "Unsupported")

    control.awaken("zombieman-a", sight=True)
    bullets_before = control.state.bullets
    control.fire("zombieman-a")
    assert control.state.bullets == bullets_before - 1
    control.defeat("zombieman-a")
    control.pick_shotgun()
    control.select_weapon("shotgun")
    shells_before = control.state.shells
    control.fire("imp-a")
    assert control.state.shells == shells_before - 1
    control.awaken("imp-b", noise=True)

    control.pick_health(7)
    assert control.state.health == 100
    expect_rejected(lambda: control.pick_health(10), "cannot accept")
    control.pick_ammo("bullets", 10)
    assert control.state.bullets == bullets_before - 1 + 10
    expect_rejected(lambda: control.awaken("zombieman-b"), "No sight or noise")

    control.move("ordinary-route-middle")
    control.use_door("middle-door")
    control.move("ordinary-route-exit-approach")
    expect_rejected(control.use_exit_switch, "not traversably connected")
    control.use_door("exit-room")
    control.use_exit_switch()
    assert control.state.terminal == "intermission-e1m2"
    assert control.state.secrets == 0
    expect_rejected(lambda: control.move("e1m2"), "already settled")

    failed = DoomE1M1Control()
    failed.receive_damage(100)
    assert failed.state.terminal == "death"
    failed.restart()
    assert failed.state == DoomState()

    print(
        "DOOM (1993) control verified: fresh HMP E1M1 state, direct route, "
        "sight/noise wake-up, finite ammunition, capped pickups, integer "
        "factor-split armour, zero-Health restart and exit-to-E1M2 terminal."
    )


if __name__ == "__main__":
    main()
