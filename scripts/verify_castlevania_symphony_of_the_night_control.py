#!/usr/bin/env python3
"""Verify the bounded original-PlayStation Symphony of the Night opening."""

from dataclasses import dataclass, field


class RejectedAction(ValueError):
    """An action lacked a documented prerequisite."""


@dataclass
class OpeningState:
    location: str = "Castle approach"
    equipment: set[str] = field(default_factory=lambda: {
        "Alucard Sword", "Alucard Shield", "Dragon Helm", "Alucard Mail",
        "Twilight Cloak", "Necklace of J",
    })
    inventory_model_available: bool = True
    cube_of_zoe: bool = False
    hp: int = 70
    max_hp: int = 70
    mp: int = 20
    max_mp: int = 20
    hearts: int = 10
    special_weapon: str | None = None
    saved: dict[str, object] | None = None
    bosses: set[str] = field(default_factory=lambda: {"Slogra", "Gaibon"})
    life_max_collected: bool = False


class SotnOpeningControl:
    def __init__(self) -> None:
        self.state = OpeningState()
        self.milestones = ["ordinary-alucard-control"]

    def meet_death(self) -> None:
        if self.state.location != "Castle approach":
            raise RejectedAction("Death's authored Entrance event is unavailable")
        self.state.location = "Entrance"
        self.state.equipment.clear()
        self.milestones.append("starting-equipment-removed")

    def collect_cube(self) -> None:
        if self.state.location != "Entrance":
            raise RejectedAction("Cube of Zoe is not reachable")
        self.state.cube_of_zoe = True
        self.milestones.append("cube-of-zoe-enabled")

    def break_candle(self) -> str:
        if not self.state.cube_of_zoe:
            raise RejectedAction("Candle item capability is unavailable")
        self.milestones.append("candle-item-exposed")
        return "heart-or-route-item"

    def activate_save_room(self) -> None:
        if self.state.location not in {"Entrance", "Alchemy Laboratory"}:
            raise RejectedAction("No eligible save-room fixture is present")
        self.state.hp = self.state.max_hp
        self.state.mp = self.state.max_mp
        self.state.saved = {
            "location": self.state.location,
            "equipment": set(self.state.equipment),
            "cube_of_zoe": self.state.cube_of_zoe,
            "max_hp": self.state.max_hp,
        }
        self.milestones.append(f"saved-{self.state.location.lower().replace(' ', '-')}")

    def enter_laboratory(self) -> None:
        if not self.state.cube_of_zoe:
            raise RejectedAction("The fixed Entrance packet is incomplete")
        self.state.location = "Alchemy Laboratory"
        self.milestones.append("alchemy-laboratory-entered")

    def equip_route_items(self) -> None:
        if self.state.location != "Alchemy Laboratory":
            raise RejectedAction("Laboratory route equipment is unreachable")
        if not self.state.inventory_model_available:
            raise RejectedAction("Equipment model unexpectedly unavailable")
        self.state.equipment.update({"Short Sword", "Leather Shield", "Cloth Tunic"})
        self.state.special_weapon = "Axe"
        self.milestones.append("route-loadout-equipped")

    def use_axe(self) -> None:
        if self.state.special_weapon != "Axe" or self.state.hearts < 1:
            raise RejectedAction("Axe and sufficient hearts are required")
        if not self.state.bosses:
            raise RejectedAction("No boss remains as a legal target")
        self.state.hearts -= 1
        self.milestones.append("axe-used")

    def defeat_bosses(self) -> None:
        if self.state.location != "Alchemy Laboratory":
            raise RejectedAction("The boss arena is unavailable")
        if "Short Sword" not in self.state.equipment:
            raise RejectedAction("The fixed route loadout is not ready")
        self.state.bosses.clear()
        self.milestones.append("slogra-gaibon-defeated")

    def collect_life_max(self) -> None:
        if self.state.bosses:
            raise RejectedAction("Life Max Up is not exposed")
        self.state.max_hp += 5
        self.state.hp += 5
        self.state.life_max_collected = True
        self.milestones.append("life-max-collected")

    def cross_to_marble_gallery(self) -> None:
        if not self.state.life_max_collected:
            raise RejectedAction("The fixed boss reward is uncollected")
        self.state.location = "Marble Gallery"
        self.milestones.append("ordinary-control-marble-gallery")

    def die_and_continue(self) -> None:
        if self.state.saved is None:
            raise RejectedAction("No save-room state exists")
        saved = self.state.saved
        self.state.location = str(saved["location"])
        self.state.equipment = set(saved["equipment"])
        self.state.cube_of_zoe = bool(saved["cube_of_zoe"])
        self.state.max_hp = int(saved["max_hp"])
        self.state.hp = self.state.max_hp
        self.state.mp = self.state.max_mp
        self.milestones.append("continued-from-save-room")


def expect_rejected(action, fragment: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert fragment in str(error)
    else:
        raise AssertionError("Invalid route action was accepted")


def main() -> None:
    invalid = SotnOpeningControl()
    expect_rejected(invalid.collect_cube, "not reachable")
    expect_rejected(invalid.break_candle, "unavailable")
    expect_rejected(invalid.enter_laboratory, "incomplete")
    expect_rejected(invalid.die_and_continue, "No save-room")

    control = SotnOpeningControl()
    control.meet_death()
    assert not control.state.equipment and control.state.inventory_model_available
    control.collect_cube()
    assert control.break_candle() == "heart-or-route-item"
    control.activate_save_room()
    control.enter_laboratory()
    control.equip_route_items()
    control.state.hp = 9
    control.state.mp = 3
    control.activate_save_room()
    assert (control.state.hp, control.state.mp) == (70, 20)
    control.use_axe()
    control.defeat_bosses()
    control.collect_life_max()
    assert (control.state.max_hp, control.state.hp) == (75, 75)
    control.cross_to_marble_gallery()
    assert control.state.location == "Marble Gallery"
    assert control.milestones[-1] == "ordinary-control-marble-gallery"

    retry = SotnOpeningControl()
    retry.meet_death()
    retry.collect_cube()
    retry.enter_laboratory()
    retry.equip_route_items()
    retry.activate_save_room()
    retry.state.hp = 0
    retry.state.equipment.add("Transient drop")
    retry.die_and_continue()
    assert retry.state.location == "Alchemy Laboratory"
    assert retry.state.hp == retry.state.max_hp
    assert "Transient drop" not in retry.state.equipment

    print("Symphony of the Night control verified: equipment reset, Cube, "
          "restorative save, Continue reload, boss pair, Life Max Up and "
          "first Marble Gallery control.")


if __name__ == "__main__":
    main()
