#!/usr/bin/env python3
"""Source-model transition control for GAME-0366, not PlayStation emulation."""

from dataclasses import dataclass


@dataclass
class Arcade:
    fighter: str = "Jin Kazama"
    stage: int = 1
    final_stage: int = 3  # symbolic test fixture, not a claim about Tekken 3
    p1_rounds: int = 0
    cpu_rounds: int = 0
    required_rounds: int = 2  # symbolic test fixture, not a claimed default
    timer: int = 40
    continue_offered: bool = False
    cleared: bool = False
    ended: bool = False

    @staticmethod
    def hit_result(level: str, defender: str) -> str:
        if level == "high" and defender in {"crouch", "stand_guard"}:
            return "miss" if defender == "crouch" else "block"
        if level == "mid" and defender == "stand_guard":
            return "block"
        if level == "low" and defender == "crouch_guard":
            return "block"
        return "hit"

    def round_result(self, p1_health: int, cpu_health: int) -> str:
        if p1_health == cpu_health:
            self.p1_rounds += 1
            self.cpu_rounds += 1
            outcome = "draw"
        elif cpu_health == 0 or p1_health > cpu_health:
            self.p1_rounds += 1
            outcome = "p1"
        else:
            self.cpu_rounds += 1
            outcome = "cpu"
        self.timer = 40
        if self.p1_rounds >= self.required_rounds:
            self.match_result(True)
        elif self.cpu_rounds >= self.required_rounds:
            self.match_result(False)
        return outcome

    def match_result(self, p1_wins: bool) -> None:
        if p1_wins:
            if self.stage == self.final_stage:
                self.cleared = True
                self.ended = True
            else:
                self.stage += 1
                self.p1_rounds = self.cpu_rounds = 0
        else:
            self.continue_offered = True

    def continue_choice(self, accept: bool) -> None:
        assert self.continue_offered
        self.continue_offered = False
        if accept:
            self.p1_rounds = self.cpu_rounds = 0
            self.timer = 40
        else:
            self.ended = True


def verify() -> None:
    assert Arcade.hit_result("high", "crouch") == "miss"
    assert Arcade.hit_result("high", "stand_guard") == "block"
    assert Arcade.hit_result("mid", "crouch_guard") == "hit"
    assert Arcade.hit_result("low", "stand_guard") == "hit"
    assert Arcade.hit_result("low", "crouch_guard") == "block"

    arcade = Arcade()
    assert arcade.round_result(60, 60) == "draw"
    assert (arcade.p1_rounds, arcade.cpu_rounds) == (1, 1)
    assert arcade.round_result(70, 0) == "p1"
    assert arcade.stage == 2 and arcade.fighter == "Jin Kazama"
    assert arcade.round_result(0, 40) == "cpu"
    assert arcade.round_result(0, 40) == "cpu"
    assert arcade.continue_offered and arcade.stage == 2
    arcade.continue_choice(True)
    assert arcade.stage == 2 and arcade.fighter == "Jin Kazama"
    for _ in range(2):
        arcade.round_result(40, 0)
    assert arcade.stage == 3 and not arcade.cleared
    for _ in range(2):
        arcade.round_result(40, 0)
    assert arcade.cleared and arcade.ended

    defeat = Arcade()
    defeat.match_result(False)
    defeat.continue_choice(False)
    assert defeat.ended and not defeat.cleared


if __name__ == "__main__":
    verify()
    print("GAME-0366 source-model control: PASS")
