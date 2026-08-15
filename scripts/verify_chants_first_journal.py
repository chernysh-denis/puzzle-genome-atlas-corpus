#!/usr/bin/env python3
"""Verify the bounded first-glyph journal loop used by GAME-0101."""

from __future__ import annotations

from dataclasses import dataclass, field


GLYPHS = ("G_OPEN", "G_CLOSE", "G_DOOR")
CANONICAL = {
    "G_OPEN": "open",
    "G_CLOSE": "closed",
    "G_DOOR": "door",
}
VALVE_TARGET = ("open", "open", "closed", "open", "closed", "open")


@dataclass
class FirstJournal:
    provisional: dict[str, str] = field(default_factory=dict)
    locked: bool = False
    canonical: dict[str, str] = field(default_factory=dict)

    def annotate(self, glyph: str, gloss: str) -> None:
        if self.locked or glyph not in GLYPHS or not gloss.strip():
            raise ValueError("annotation is not editable")
        self.provisional[glyph] = gloss.strip()

    def validate(self, picture_to_glyph: dict[str, str]) -> bool:
        if self.locked:
            raise ValueError("page already locked")
        if set(picture_to_glyph) != set(CANONICAL.values()):
            return False
        if set(picture_to_glyph.values()) != set(GLYPHS):
            return False
        correct = all(CANONICAL[glyph] == picture for picture, glyph in picture_to_glyph.items())
        if correct:
            self.locked = True
            self.canonical = dict(CANONICAL)
        return correct


def valves_open_path(states: tuple[str, ...]) -> bool:
    if len(states) != 6 or any(state not in {"open", "closed"} for state in states):
        return False
    return states == VALVE_TARGET


def may_progress(journal: FirstJournal, valve_states: tuple[str, ...]) -> bool:
    return valves_open_path(valve_states) and journal.locked


def verify() -> None:
    journal = FirstJournal()
    journal.annotate("G_OPEN", "lever lets water through")
    journal.annotate("G_OPEN", "open")
    journal.annotate("G_CLOSE", "closed")
    journal.annotate("G_DOOR", "door")
    assert len(journal.provisional) == 3

    assert valves_open_path(VALVE_TARGET)
    assert not valves_open_path(("closed",) * 6)
    assert not valves_open_path(VALVE_TARGET[:-1])
    assert not may_progress(journal, VALVE_TARGET)

    incomplete = {"open": "G_OPEN", "closed": "G_CLOSE"}
    assert not journal.validate(incomplete)
    duplicate = {"open": "G_OPEN", "closed": "G_OPEN", "door": "G_DOOR"}
    assert not journal.validate(duplicate)
    wrong = {"open": "G_CLOSE", "closed": "G_OPEN", "door": "G_DOOR"}
    assert not journal.validate(wrong)
    assert not journal.locked

    correct = {"open": "G_OPEN", "closed": "G_CLOSE", "door": "G_DOOR"}
    assert journal.validate(correct)
    assert journal.canonical == CANONICAL
    assert may_progress(journal, VALVE_TARGET)

    try:
        journal.annotate("G_OPEN", "changed after validation")
    except ValueError:
        pass
    else:
        raise AssertionError("validated meanings must be locked")


if __name__ == "__main__":
    verify()
    print("Chants first-journal control passed: 6 valves, 3 glyphs, and 12 assertions.")
