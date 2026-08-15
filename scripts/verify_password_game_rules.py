#!/usr/bin/env python3
"""Verify the bounded Rules 1-9 loop used by GAME-0102."""

from __future__ import annotations

import re
from dataclasses import dataclass, field


MONTHS = (
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december",
)
SPONSORS = ("pepsi", "starbucks", "shell")
ROMAN_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_value(token: str) -> int:
    total = 0
    previous = 0
    for character in reversed(token):
        value = ROMAN_VALUES[character]
        total += -value if value < previous else value
        previous = max(previous, value)
    return total


def roman_product(password: str) -> int:
    product = 1
    tokens = re.findall(r"[IVXLCDM]+", password)
    for token in tokens:
        product *= roman_value(token)
    return product if tokens else 0


def rule_passes(rule: int, password: str) -> bool:
    checks = {
        1: lambda: len(password) >= 5,
        2: lambda: any(character.isdigit() for character in password),
        3: lambda: any(character.isupper() for character in password),
        4: lambda: any(not character.isalnum() for character in password),
        5: lambda: sum(int(character) for character in password if character.isdigit()) == 25,
        6: lambda: any(month in password.lower() for month in MONTHS),
        7: lambda: bool(re.search(r"[IVXLCDM]", password)),
        8: lambda: any(sponsor in password.lower() for sponsor in SPONSORS),
        9: lambda: roman_product(password) == 35,
    }
    return checks[rule]()


@dataclass
class RuleWindow:
    password: str = ""
    revealed: list[int] = field(default_factory=lambda: [1])

    def edit(self, password: str) -> dict[int, bool]:
        self.password = password
        while self.revealed[-1] < 9 and all(rule_passes(rule, password) for rule in self.revealed):
            self.revealed.append(self.revealed[-1] + 1)
        return {rule: rule_passes(rule, password) for rule in self.revealed}

    @property
    def complete(self) -> bool:
        return self.revealed == list(range(1, 10)) and all(
            rule_passes(rule, self.password) for rule in self.revealed
        )


def verify() -> None:
    window = RuleWindow()
    states = window.edit("A!997maypepsiVqVII")
    assert window.revealed == list(range(1, 10))
    assert all(states.values())
    assert window.complete
    assert roman_product(window.password) == 35
    assert sum(int(character) for character in window.password if character.isdigit()) == 25

    states = window.edit("A997maypepsiVqVII")
    assert window.revealed == list(range(1, 10))
    assert not states[4]
    assert all(states[rule] for rule in states if rule != 4)
    assert not window.complete

    states = window.edit("A!997maypepsiVqVII")
    assert all(states.values())
    assert window.complete

    for broken in (
        "A!97maypepsiVqVII",
        "A!997pepsiVqVII",
        "A!997mayoVqVII",
        "A!997maypepsiVqVI",
    ):
        assert not all(rule_passes(rule, broken) for rule in range(1, 10))


if __name__ == "__main__":
    verify()
    print("Password Game control passed: Rules 1-9, persistent activation, regression, and recovery.")
