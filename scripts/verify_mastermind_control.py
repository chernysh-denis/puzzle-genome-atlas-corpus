#!/usr/bin/env python3
"""Verify the reproducible GAME-0065 Mastermind control attempt."""

from __future__ import annotations

from collections import Counter
from itertools import product

COLOURS = ("A", "B", "C", "D", "E", "F")
SECRET = ("A", "A", "C", "D")
GUESSES = (
    ("A", "A", "B", "B"),
    ("C", "D", "E", "F"),
    ("A", "C", "A", "D"),
)
EXPECTED_FEEDBACK = ((2, 0), (0, 2), (2, 2))
EXPECTED_REMAINING = (114, 42, 1)


def score(secret: tuple[str, ...], guess: tuple[str, ...]) -> tuple[int, int]:
    """Return exact and duplicate-limited misplaced matches."""
    assert len(secret) == len(guess) == 4
    exact = sum(target == proposed for target, proposed in zip(secret, guess))
    residual_secret = Counter(
        target
        for target, proposed in zip(secret, guess)
        if target != proposed
    )
    residual_guess = Counter(
        proposed
        for target, proposed in zip(secret, guess)
        if target != proposed
    )
    misplaced = sum((residual_secret & residual_guess).values())
    return exact, misplaced


def main() -> None:
    candidates = list(product(COLOURS, repeat=4))
    assert len(candidates) == 6**4 == 1296

    for guess, expected_feedback, expected_remaining in zip(
        GUESSES, EXPECTED_FEEDBACK, EXPECTED_REMAINING
    ):
        feedback = score(SECRET, guess)
        assert feedback == expected_feedback
        candidates = [
            candidate for candidate in candidates if score(candidate, guess) == feedback
        ]
        assert len(candidates) == expected_remaining

    assert candidates == [SECRET]
    assert score(SECRET, SECRET) == (4, 0)

    for secret in product(COLOURS, repeat=4):
        for guess in GUESSES + (SECRET,):
            exact, misplaced = score(secret, guess)
            assert 0 <= exact <= 4
            assert 0 <= misplaced <= 4 - exact
            for colour in COLOURS:
                credited = sum(
                    target == proposed == colour
                    for target, proposed in zip(secret, guess)
                )
                residual_credit = min(
                    sum(target == colour and target != proposed for target, proposed in zip(secret, guess)),
                    sum(proposed == colour and target != proposed for target, proposed in zip(secret, guess)),
                )
                assert credited + residual_credit <= min(
                    secret.count(colour), guess.count(colour)
                )

    print(
        "Mastermind control verified: 1,296 candidate codes; retained sets "
        "114, 42 and 1; duplicate-aware exact-first feedback; unique AACD secret"
    )


if __name__ == "__main__":
    main()
