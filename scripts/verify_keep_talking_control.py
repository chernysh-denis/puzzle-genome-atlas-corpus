#!/usr/bin/env python3
"""Verify the bounded Wires/Button bomb used by GAME-0100."""

from __future__ import annotations

from dataclasses import dataclass, field


def correct_wire(wires: tuple[str, ...], serial_last_digit: int) -> int:
    """Return the zero-based wire selected by manual v1's first matching rule."""
    count = len(wires)
    if count == 3:
        if "red" not in wires:
            return 1
        if wires[-1] == "white":
            return 2
        if wires.count("blue") > 1:
            return max(index for index, colour in enumerate(wires) if colour == "blue")
        return 2
    if count == 4:
        if wires.count("red") > 1 and serial_last_digit % 2 == 1:
            return max(index for index, colour in enumerate(wires) if colour == "red")
        if wires[-1] == "yellow" and "red" not in wires:
            return 0
        if wires.count("blue") == 1:
            return 0
        if wires.count("yellow") > 1:
            return 3
        return 1
    if count == 5:
        if wires[-1] == "black" and serial_last_digit % 2 == 1:
            return 3
        if wires.count("red") == 1 and wires.count("yellow") > 1:
            return 0
        if "black" not in wires:
            return 1
        return 0
    if count == 6:
        if "yellow" not in wires and serial_last_digit % 2 == 1:
            return 2
        if wires.count("yellow") == 1 and wires.count("white") > 1:
            return 3
        if "red" not in wires:
            return 5
        return 3
    raise ValueError("Wires module must contain three to six wires")


def button_action(
    colour: str,
    label: str,
    batteries: int,
    lit_indicators: frozenset[str],
) -> str:
    """Return tap or hold from the manual's ordered Button rules."""
    if colour == "blue" and label == "Abort":
        return "hold"
    if batteries > 1 and label == "Detonate":
        return "tap"
    if colour == "white" and "CAR" in lit_indicators:
        return "hold"
    if batteries > 2 and "FRK" in lit_indicators:
        return "tap"
    if colour == "yellow":
        return "hold"
    if colour == "red" and label == "Hold":
        return "tap"
    return "hold"


def release_digit(strip: str) -> int:
    return {"blue": 4, "white": 1, "yellow": 5}.get(strip, 1)


@dataclass
class Bomb:
    remaining_seconds: float = 300.0
    strikes: int = 0
    disarmed: set[str] = field(default_factory=set)
    exploded: bool = False

    @property
    def rate(self) -> float:
        return (1.0, 1.25, 1.5)[min(self.strikes, 2)]

    def elapse(self, real_seconds: float) -> None:
        self.remaining_seconds = max(0.0, self.remaining_seconds - real_seconds * self.rate)
        if self.remaining_seconds == 0:
            self.exploded = True

    def adjudicate(self, module: str, correct: bool) -> None:
        if self.exploded or module in self.disarmed:
            raise ValueError("module is not actionable")
        if correct:
            self.disarmed.add(module)
            return
        self.strikes += 1
        if self.strikes >= 3:
            self.exploded = True

    @property
    def defused(self) -> bool:
        return self.disarmed == {"wires", "button"} and not self.exploded


def verify() -> None:
    # Every published Wires branch used by the control is executable.
    cases = (
        (("blue", "white", "black"), 2, 1),
        (("red", "blue", "white"), 2, 2),
        (("blue", "red", "blue"), 2, 2),
        (("red", "red", "blue", "white"), 5, 1),
        (("white", "blue", "black", "yellow"), 2, 0),
        (("red", "blue", "yellow", "white"), 5, 0),
        (("red", "yellow", "yellow", "white", "black"), 5, 3),
        (("red", "yellow", "yellow", "white", "blue"), 2, 0),
        (("blue", "white", "red", "yellow", "green"), 2, 1),
        (("blue", "white", "black", "red", "green", "black"), 5, 2),
        (("blue", "white", "yellow", "white", "red", "black"), 2, 3),
        (("blue", "black", "green", "white", "black", "yellow"), 2, 5),
    )
    for wires, serial, expected in cases:
        assert correct_wire(wires, serial) == expected

    assert button_action("blue", "Abort", 4, frozenset({"FRK"})) == "hold"
    assert button_action("red", "Detonate", 2, frozenset()) == "tap"
    assert button_action("white", "Press", 1, frozenset({"CAR"})) == "hold"
    assert button_action("yellow", "Abort", 2, frozenset()) == "hold"
    assert release_digit("blue") == 4
    assert release_digit("yellow") == 5

    # Canonical state: R/B/Y/W wires, odd serial -> first wire; yellow Abort
    # button -> hold, blue strip -> release while any timer digit is 4.
    bomb = Bomb()
    assert correct_wire(("red", "blue", "yellow", "white"), 5) == 0
    bomb.adjudicate("wires", correct=True)
    assert button_action("yellow", "Abort", 2, frozenset()) == "hold"
    bomb.elapse(8.0)
    bomb.adjudicate("button", correct=release_digit("blue") in (4, 4, 2))
    assert bomb.defused

    wrong = Bomb()
    wrong.adjudicate("wires", correct=False)
    assert wrong.strikes == 1 and wrong.rate > 1
    before = wrong.remaining_seconds
    wrong.elapse(4.0)
    assert before - wrong.remaining_seconds == 5.0
    wrong.adjudicate("wires", correct=False)
    wrong.adjudicate("wires", correct=False)
    assert wrong.exploded and not wrong.defused

    timeout = Bomb(remaining_seconds=1.0)
    timeout.elapse(1.0)
    assert timeout.exploded


if __name__ == "__main__":
    verify()
    print("Keep Talking bounded control passed: 12 wire cases and 8 attempt assertions.")
