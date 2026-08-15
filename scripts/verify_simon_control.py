#!/usr/bin/env python3
"""Verify the reproducible GAME-0067 Simon control attempt."""

from __future__ import annotations

PADS = ("G", "R", "Y", "B")
STREAM = ("G", "R", "G", "Y", "B", "R")


def adjudicate(target: tuple[str, ...], response: tuple[str, ...]) -> tuple[bool, int | None]:
    """Return success and the first one-based mismatching position, if any."""
    for position, symbol in enumerate(response, start=1):
        assert symbol in PADS
        if position > len(target) or symbol != target[position - 1]:
            return False, position
    if len(response) != len(target):
        return False, len(response) + 1
    return True, None


def main() -> None:
    score = 0
    previous: tuple[str, ...] = ()

    for length in range(1, 6):
        target = STREAM[:length]
        assert target[:-1] == previous
        assert target[-1] in PADS
        success, mismatch = adjudicate(target, target)
        assert success and mismatch is None
        score += 1
        previous = target

    final_target = STREAM
    assert final_target[:-1] == previous
    wrong_response = ("G", "R", "G", "Y", "B", "B")
    success, mismatch = adjudicate(final_target, wrong_response)
    assert not success and mismatch == 6
    assert score == 5

    for pad in PADS:
        candidate = final_target[:-1] + (pad,)
        accepted, first_error = adjudicate(final_target, candidate)
        assert accepted == (pad == "R")
        assert first_error is None if pad == "R" else first_error == 6

    print(
        "Simon control verified: five exact rounds, retained-prefix extension, "
        "first mismatch at position 6, final score 5"
    )


if __name__ == "__main__":
    main()
