#!/usr/bin/env python3
"""Verify the bounded original-SNES Super Mario World Yoshi's Island 2 model."""

from __future__ import annotations

from dataclasses import dataclass, field


class RejectedAction(ValueError):
    """An action was attempted outside the sourced packet or current state."""


@dataclass
class CourseState:
    lives: int = 5
    time: int = 300
    power: str = "small"
    reserve: str | None = None
    mounted: bool = False
    yoshi_available: bool = False
    yoshi_fleeing: bool = False
    mouth: str | None = None
    mouth_timer: int = 0
    red_berries: int = 0
    dragon_coins: set[int] = field(default_factory=set)
    checkpoint: str = "course-start"
    grab_block: str = "pipe-room-origin"
    p_switch_time: int = 0
    coins_are_blocks: bool = False
    goal_settled: bool = False
    successor: str | None = None
    carried_yoshi: bool = False
    emitted: list[str] = field(default_factory=list)


class SuperMarioWorldControl:
    def __init__(self) -> None:
        self.state = CourseState()
        self.milestones = ["fresh-yoshis-island-2"]

    def hatch_and_mount(self) -> None:
        self._require_open()
        if self.state.yoshi_available or self.state.mounted:
            raise RejectedAction("Yoshi is already available")
        self.state.yoshi_available = True
        self.state.mounted = True
        self.milestones.append("yoshi-mounted")

    def dismount(self) -> None:
        self._require_mounted()
        self.state.mounted = False

    def remount(self) -> None:
        self._require_open()
        if not self.state.yoshi_available or not self.state.yoshi_fleeing:
            raise RejectedAction("No fleeing reachable Yoshi can be remounted")
        self.state.mounted = True
        self.state.yoshi_fleeing = False
        self.milestones.append("yoshi-recovered")

    def ingest(self, target: str, *, reachable: bool = True) -> None:
        self._require_mounted()
        if not reachable:
            raise RejectedAction("Target is outside tongue reach")
        if self.state.mouth is not None:
            raise RejectedAction("Yoshi's mouth is already occupied")
        if target == "red-berry":
            self.state.red_berries += 1
            if self.state.red_berries == 10:
                self.state.red_berries = 0
                self.state.emitted.append("mushroom-egg")
                self.milestones.append("ten-red-berries")
            return
        if target not in {"red-shell", "green-shell"}:
            raise RejectedAction("Target is not eligible for this packet")
        self.state.mouth = target
        self.state.mouth_timer = 4

    def expel(self) -> None:
        self._require_mounted()
        held = self.state.mouth
        if held is None:
            raise RejectedAction("No mouth-held body can be expelled")
        if held == "red-shell":
            self.state.emitted.extend(["yoshi-fireball"] * 3)
        elif held == "green-shell":
            self.state.emitted.append("moving-green-shell")
        else:
            raise RejectedAction("Unsupported held body")
        self.state.mouth = None
        self.state.mouth_timer = 0

    def advance(self, seconds: int = 1) -> None:
        self._require_open()
        if seconds <= 0:
            raise RejectedAction("Time advance must be positive")
        for _ in range(seconds):
            self.state.time -= 1
            if self.state.mouth is not None:
                self.state.mouth_timer -= 1
                if self.state.mouth_timer == 0:
                    self.state.emitted.append(f"swallowed-{self.state.mouth}")
                    self.state.mouth = None
            if self.state.p_switch_time > 0:
                self.state.p_switch_time -= 1
                if self.state.p_switch_time == 0:
                    self.state.coins_are_blocks = False
                    self.milestones.append("p-switch-restored")
            if self.state.time == 0:
                self.lose_life("time-expired")
                break

    def collect_mushroom_reward(self) -> None:
        self._require_open()
        if "mushroom-egg" not in self.state.emitted:
            raise RejectedAction("No berry reward is available")
        self.state.emitted.remove("mushroom-egg")
        self.state.power = "super"

    def mounted_hit(self) -> None:
        self._require_mounted()
        self.state.mounted = False
        self.state.yoshi_fleeing = True
        self.milestones.append("rider-separated")

    def collect_dragon_coin(self, coin: int) -> None:
        self._require_open()
        if coin not in range(1, 6):
            raise RejectedAction("Dragon Coin is outside the scoped course")
        if coin in self.state.dragon_coins:
            raise RejectedAction("Dragon Coin was already settled")
        self.state.dragon_coins.add(coin)
        if len(self.state.dragon_coins) == 5:
            self.state.lives += 1
            self.milestones.append("five-dragon-coins-life")

    def activate_midway(self) -> None:
        self._require_open()
        self.state.checkpoint = "midway-gate"
        if self.state.power == "small":
            self.state.power = "super"
        self.milestones.append("midway-active")

    def carry_grab_block(self, destination: str) -> None:
        self._require_open()
        if self.state.grab_block == "spent":
            raise RejectedAction("Grab Block is no longer available")
        self.state.grab_block = destination

    def throw_grab_block(self) -> None:
        self._require_open()
        if self.state.grab_block == "pipe-room-origin":
            raise RejectedAction("Grab Block was not carried")
        self.state.grab_block = "spent"
        self.milestones.append("grab-block-thrown")

    def press_p_switch(self, duration: int = 8) -> None:
        self._require_open()
        if duration <= 0:
            raise RejectedAction("P-Switch duration must be positive")
        self.state.p_switch_time = duration
        self.state.coins_are_blocks = True
        self.milestones.append("coin-block-exchange")

    def cross_temporary_steps(self) -> None:
        self._require_open()
        if not self.state.coins_are_blocks:
            raise RejectedAction("The coin path is not solid")
        self.milestones.append("temporary-steps-crossed")

    def lose_life(self, reason: str) -> None:
        if self.state.goal_settled:
            raise RejectedAction("The course is already settled")
        if self.state.lives < 1:
            raise RejectedAction("No finite life remains")
        anchor = self.state.checkpoint
        lives = self.state.lives - 1
        retained_checkpoint = self.state.checkpoint
        self.state = CourseState(lives=lives, checkpoint=retained_checkpoint)
        self.milestones.append(f"restart-{anchor}-{reason}")

    def goal_tape(self, *, star_height: int = 20) -> None:
        self._require_open()
        if not 0 <= star_height <= 50:
            raise RejectedAction("Goal Tape height is outside the sourced range")
        self.state.goal_settled = True
        self.state.successor = "yoshis-island-3"
        self.state.carried_yoshi = self.state.mounted
        self.milestones.append(f"goal-{star_height}")

    def _require_open(self) -> None:
        if self.state.goal_settled:
            raise RejectedAction("The course is already settled")

    def _require_mounted(self) -> None:
        self._require_open()
        if not self.state.mounted:
            raise RejectedAction("Mario is not riding Yoshi")


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid Yoshi's Island 2 action was accepted")


def main() -> None:
    control = SuperMarioWorldControl()
    expect_rejected(lambda: control.ingest("red-berry"), "not riding")
    control.hatch_and_mount()
    expect_rejected(lambda: control.ingest("red-shell", reachable=False), "reach")

    for _ in range(10):
        control.ingest("red-berry")
    assert control.state.red_berries == 0
    assert control.state.emitted == ["mushroom-egg"]
    control.collect_mushroom_reward()
    assert control.state.power == "super"

    control.ingest("red-shell")
    expect_rejected(lambda: control.ingest("green-shell"), "occupied")
    control.expel()
    assert control.state.emitted.count("yoshi-fireball") == 3
    control.ingest("green-shell")
    control.expel()
    assert "moving-green-shell" in control.state.emitted

    control.ingest("green-shell")
    control.advance(4)
    assert "swallowed-green-shell" in control.state.emitted
    assert control.state.mouth is None

    control.mounted_hit()
    assert control.state.yoshi_fleeing and not control.state.mounted
    control.remount()

    lives_before = control.state.lives
    for coin in range(1, 6):
        control.collect_dragon_coin(coin)
    assert control.state.lives == lives_before + 1
    expect_rejected(lambda: control.collect_dragon_coin(5), "already")

    control.activate_midway()
    checkpoint_lives = control.state.lives
    control.lose_life("pit")
    assert control.state.lives == checkpoint_lives - 1
    assert control.state.checkpoint == "midway-gate"
    assert "restart-midway-gate-pit" in control.milestones

    control.hatch_and_mount()
    control.carry_grab_block("pipe-room-exit")
    control.throw_grab_block()
    control.press_p_switch(3)
    control.cross_temporary_steps()
    control.advance(3)
    assert not control.state.coins_are_blocks
    expect_rejected(control.cross_temporary_steps, "not solid")

    control.press_p_switch()
    control.cross_temporary_steps()
    control.goal_tape(star_height=32)
    assert control.state.successor == "yoshis-island-3"
    assert control.state.carried_yoshi
    expect_rejected(lambda: control.advance(), "already settled")

    print(
        "Super Mario World control verified: mount, exclusive mouth state, "
        "typed shell results, berry reward, recoverable separation, Dragon "
        "Coin life, Midway restart, Grab Block, P-Switch restoration and "
        "mounted Goal Tape successor."
    )


if __name__ == "__main__":
    main()
