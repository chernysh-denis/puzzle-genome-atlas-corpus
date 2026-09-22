#!/usr/bin/env python3
"""Verify the bounded original-Xbox Splinter Cell state reconstruction."""

from dataclasses import dataclass, field
from copy import deepcopy


class RejectedAction(ValueError):
    """An action lacked one documented prerequisite."""


POLICE_OBJECTIVES = (
    "meet-contact",
    "apartment-data",
    "dead-drop",
    "enter-precinct",
    "locate-agents",
    "access-surveillance",
    "reach-wilkes-van",
)


@dataclass
class OperativeState:
    mission: str = "Training Course"
    difficulty: str = "Normal"
    location: str = "calibration"
    posture: str = "standing"
    light_exposure: int = 70
    noise: int = 0
    life: int = 100
    ammunition: int = 10
    selected_item: str = "SC pistol"
    alert: bool = False
    known_codes: set[str] = field(default_factory=set)
    opened: set[str] = field(default_factory=set)
    unconscious_bodies: dict[str, str] = field(default_factory=dict)
    carried_body: str | None = None
    restrained_actor: str | None = None
    police_index: int = 0
    checkpoint: "OperativeState | None" = None


class SplinterCellControl:
    def __init__(self) -> None:
        self.state = OperativeState()
        self.milestones = ["fresh-normal-profile"]

    def move(self, speed: int, posture: str, surface: str = "floor") -> None:
        if speed not in range(1, 4):
            raise RejectedAction("Analog speed must be between one and three")
        if posture not in {"standing", "crouched", "back-to-wall"}:
            raise RejectedAction("Unsupported posture")
        self.state.posture = posture
        base_noise = speed * 2
        if posture == "crouched":
            base_noise -= 2
        if surface == "chains":
            base_noise += 6
        elif surface == "glass":
            base_noise += 4
        self.state.noise = max(0, base_noise)

    def set_shadow(self, exposure: int) -> None:
        if not 0 <= exposure <= 100:
            raise RejectedAction("Stealth Meter exposure is out of range")
        self.state.light_exposure = exposure

    def acquire_by_observer(self, unobstructed: bool) -> None:
        if unobstructed and self.state.light_exposure + self.state.noise >= 75:
            self.state.alert = True

    def pick_training_lock(self) -> None:
        if self.state.mission != "Training Course":
            raise RejectedAction("The practice lock is unavailable")
        self.state.opened.add("training-lock")
        self.milestones.append("training-lock-picked")

    def grab_unaware(self, actor: str, aware: bool = False) -> None:
        if aware or self.state.alert:
            raise RejectedAction("Target is not unaware")
        self.state.restrained_actor = actor

    def interrogate_for_code(self, code: str) -> None:
        if self.state.restrained_actor != "code-trainee":
            raise RejectedAction("No eligible restrained speaker")
        self.state.known_codes.add(code)
        self.state.restrained_actor = None
        self.milestones.append("training-code-learned")

    def enter_code(self, fixture: str, code: str) -> None:
        if code not in self.state.known_codes:
            raise RejectedAction("The operational code is not known")
        self.state.opened.add(fixture)

    def force_retinal_cooperation(self) -> None:
        if self.state.restrained_actor != "retinal-trainee":
            raise RejectedAction("No eligible person is at the retinal scanner")
        self.state.opened.add("retinal-gate")
        self.state.restrained_actor = None
        self.milestones.append("retinal-cooperation-complete")

    def shoot_training_light(self) -> None:
        if self.state.selected_item != "SC pistol" or self.state.ammunition < 1:
            raise RejectedAction("A ready loaded pistol is required")
        self.state.ammunition -= 1
        self.state.light_exposure = 10
        self.milestones.append("camera-route-darkened")

    def neutralise(self, actor: str, aware: bool = False) -> None:
        if aware or self.state.alert:
            raise RejectedAction("Stealth neutralisation requires an unaware target")
        self.state.unconscious_bodies[actor] = "exposed"

    def pick_up_body(self, actor: str) -> None:
        if self.state.carried_body is not None:
            raise RejectedAction("Another body is already carried")
        if self.state.unconscious_bodies.get(actor) is None:
            raise RejectedAction("No eligible incapacitated body is reachable")
        self.state.carried_body = actor
        del self.state.unconscious_bodies[actor]

    def place_body(self, region: str) -> None:
        if self.state.carried_body is None:
            raise RejectedAction("No body is carried")
        actor = self.state.carried_body
        self.state.carried_body = None
        self.state.unconscious_bodies[actor] = region
        self.milestones.append(f"{actor}-placed-{region}")

    def body_check(self) -> None:
        if any(region != "shadow" for region in self.state.unconscious_bodies.values()):
            self.state.alert = True

    def complete_training(self) -> None:
        required = {"training-lock", "training-keypad", "retinal-gate"}
        if not required.issubset(self.state.opened):
            raise RejectedAction("Training access exercises are incomplete")
        if self.state.unconscious_bodies.get("training-guard") != "shadow":
            raise RejectedAction("The training body is not hidden")
        self.move(1, "crouched", "glass")
        if self.state.noise > 4:
            raise RejectedAction("The glass crossing was too loud")
        self.state.mission = "Police Station"
        self.state.location = "insertion-yard"
        self.milestones.append("training-complete")
        self.save_checkpoint()

    def complete_police_objective(self, objective: str) -> None:
        expected = POLICE_OBJECTIVES[self.state.police_index]
        if objective != expected:
            raise RejectedAction(f"Expected objective {expected}")
        if objective == "enter-precinct" and "5929" not in self.state.known_codes:
            raise RejectedAction("Precinct code 5929 is not known")
        self.state.police_index += 1
        self.state.location = objective
        self.milestones.append(objective)

    def save_checkpoint(self) -> None:
        stored = deepcopy(self.state)
        stored.checkpoint = None
        self.state.checkpoint = stored

    def fail_and_load(self) -> None:
        if self.state.checkpoint is None:
            raise RejectedAction("No saved Checkpoint exists")
        stored = deepcopy(self.state.checkpoint)
        stored.checkpoint = deepcopy(self.state.checkpoint)
        self.state = stored
        self.milestones.append("checkpoint-restored")

    def settle_police_station(self) -> None:
        if self.state.police_index != len(POLICE_OBJECTIVES):
            raise RejectedAction("Police Station mandatory objectives remain")
        if self.state.alert:
            raise RejectedAction("The fixed reproducible route is not alarm-free")
        self.state.mission = "Defense Ministry"
        self.state.location = "first-control"
        self.milestones.append("police-station-settled")
        self.save_checkpoint()


def expect_rejected(action, fragment: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert fragment in str(error)
    else:
        raise AssertionError("Invalid action was accepted")


def main() -> None:
    invalid = SplinterCellControl()
    expect_rejected(lambda: invalid.interrogate_for_code("28469"), "speaker")
    expect_rejected(lambda: invalid.enter_code("training-keypad", "28469"), "not known")
    invalid.neutralise("body")
    invalid.body_check()
    assert invalid.state.alert
    expect_rejected(lambda: invalid.grab_unaware("code-trainee"), "unaware")

    control = SplinterCellControl()
    control.pick_training_lock()
    control.grab_unaware("code-trainee")
    control.interrogate_for_code("28469")
    control.enter_code("training-keypad", "28469")
    control.grab_unaware("retinal-trainee")
    control.force_retinal_cooperation()
    ammo_before = control.state.ammunition
    control.shoot_training_light()
    assert control.state.ammunition == ammo_before - 1
    assert control.state.light_exposure == 10
    control.neutralise("training-guard")
    control.pick_up_body("training-guard")
    control.place_body("shadow")
    control.body_check()
    assert not control.state.alert
    control.complete_training()

    control.complete_police_objective("meet-contact")
    control.complete_police_objective("apartment-data")
    control.complete_police_objective("dead-drop")
    control.state.known_codes.add("5929")
    control.complete_police_objective("enter-precinct")
    control.complete_police_objective("locate-agents")
    control.complete_police_objective("access-surveillance")
    control.complete_police_objective("reach-wilkes-van")
    control.settle_police_station()
    assert control.state.mission == "Defense Ministry"

    control.state.location = "failed-transient-room"
    control.state.life = 0
    control.state.alert = True
    control.state.unconscious_bodies["transient"] = "exposed"
    control.fail_and_load()
    assert control.state.mission == "Defense Ministry"
    assert control.state.location == "first-control"
    assert control.state.life > 0
    assert not control.state.alert
    assert "transient" not in control.state.unconscious_bodies
    assert control.milestones[-1] == "checkpoint-restored"

    print(
        "Tom Clancy's Splinter Cell control verified: light and sound stealth, "
        "interrogation, lock and retinal access, body concealment, ordered "
        "Police Station settlement and successor checkpoint reload."
    )


if __name__ == "__main__":
    main()
