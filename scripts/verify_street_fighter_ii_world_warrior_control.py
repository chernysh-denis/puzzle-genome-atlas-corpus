#!/usr/bin/env python3
"""Deterministic source-model control for GAME-0351.

This verifies the bounded relations claimed by the research record. It does
not emulate or execute the Street Fighter II arcade program.
"""

from dataclasses import dataclass


@dataclass
class Match:
    p1_vitality: int = 100
    cpu_vitality: int = 100
    p1_rounds: int = 0
    cpu_rounds: int = 0
    timer: int = 99
    settled: bool = False

    def command_legal(self, *, actionable: bool, sequence: tuple[str, ...]) -> bool:
        return actionable and bool(sequence)

    def contact(self, *, damage: int, guarded: bool = False) -> None:
        applied = max(0, damage // 4 if guarded else damage)
        self.cpu_vitality = max(0, self.cpu_vitality - applied)

    def throw(self, *, close: bool, target_actionable: bool) -> bool:
        if not close or not target_actionable:
            return False
        self.cpu_vitality = max(0, self.cpu_vitality - 12)
        return True

    def settle_round(self) -> str:
        if self.p1_vitality == self.cpu_vitality:
            return "draw"
        winner = "p1" if self.cpu_vitality == 0 or self.p1_vitality > self.cpu_vitality else "cpu"
        if winner == "p1":
            self.p1_rounds += 1
        else:
            self.cpu_rounds += 1
        if max(self.p1_rounds, self.cpu_rounds) == 2:
            self.settled = True
        else:
            self.p1_vitality = self.cpu_vitality = 100
            self.timer = 99
        return winner


def verify() -> None:
    match = Match()
    assert match.command_legal(actionable=True, sequence=("down", "down-forward", "forward", "punch"))
    assert not match.command_legal(actionable=False, sequence=("punch",))

    match.contact(damage=20, guarded=True)
    assert match.cpu_vitality == 95
    match.contact(damage=95)
    assert match.cpu_vitality == 0
    assert match.settle_round() == "p1"
    assert (match.p1_vitality, match.cpu_vitality, match.p1_rounds) == (100, 100, 1)

    assert match.throw(close=False, target_actionable=True) is False
    assert match.throw(close=True, target_actionable=True) is True
    assert match.cpu_vitality == 88

    match.cpu_vitality = match.p1_vitality
    assert match.settle_round() == "draw"
    assert (match.p1_rounds, match.cpu_rounds, match.settled) == (1, 0, False)

    match.cpu_vitality = 0
    assert match.settle_round() == "p1"
    assert match.p1_rounds == 2 and match.settled

    defeat = Match(p1_rounds=0, cpu_rounds=1, p1_vitality=0, cpu_vitality=13)
    assert defeat.settle_round() == "cpu"
    assert defeat.cpu_rounds == 2 and defeat.settled


if __name__ == "__main__":
    verify()
    print("GAME-0351 source-model control: PASS")
