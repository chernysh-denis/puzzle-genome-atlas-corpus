#!/usr/bin/env python3
"""Verify the reproducible GAME-0068 Wordle control attempt."""

from __future__ import annotations

from collections import Counter
from itertools import product

EXACT = "G"
PRESENT = "Y"
ABSENT = "B"
ANSWER = "APPLE"
VALID_WORDS = {
    "ALLEY",
    "AMPLE",
    "APPLE",
    "APPLY",
    "LEAPT",
    "PAPAL",
    "PLATE",
}


def score(answer: str, guess: str) -> str:
    """Return exact-first, duplicate-limited position feedback."""
    assert len(answer) == len(guess) == 5
    feedback = [ABSENT] * 5
    residual: Counter[str] = Counter()

    for index, (target_letter, guess_letter) in enumerate(zip(answer, guess)):
        if target_letter == guess_letter:
            feedback[index] = EXACT
        else:
            residual[target_letter] += 1

    for index, guess_letter in enumerate(guess):
        if feedback[index] == EXACT:
            continue
        if residual[guess_letter] > 0:
            feedback[index] = PRESENT
            residual[guess_letter] -= 1

    return "".join(feedback)


class Attempt:
    def __init__(self, answer: str, valid_words: set[str]) -> None:
        self.answer = answer
        self.valid_words = valid_words
        self.rows: list[tuple[str, str]] = []
        self.solved = False

    def submit(self, guess: str) -> str | None:
        guess = guess.upper()
        if self.solved or len(self.rows) == 6:
            return None
        if len(guess) != 5 or guess not in self.valid_words:
            return None
        feedback = score(self.answer, guess)
        self.rows.append((guess, feedback))
        self.solved = feedback == EXACT * 5
        return feedback


def verify_scoring_invariants() -> None:
    alphabet = "ABC"
    words = ("".join(chars) for chars in product(alphabet, repeat=5))
    all_words = tuple(words)
    for answer in all_words:
        for guess in all_words:
            feedback = score(answer, guess)
            for index, state in enumerate(feedback):
                assert (state == EXACT) == (answer[index] == guess[index])
            for letter in alphabet:
                credited = sum(
                    state in (EXACT, PRESENT)
                    for state, guessed in zip(feedback, guess)
                    if guessed == letter
                )
                assert credited == min(answer.count(letter), guess.count(letter))


def main() -> None:
    attempt = Attempt(ANSWER, VALID_WORDS)
    assert attempt.submit("ABLE") is None
    assert attempt.submit("ZZZZZ") is None
    assert len(attempt.rows) == 0

    expected = (
        ("ALLEY", "GYBYB"),
        ("PAPAL", "YYGBY"),
        ("AMPLE", "GBGGG"),
        ("APPLE", "GGGGG"),
    )
    for guess, feedback in expected:
        assert attempt.submit(guess) == feedback
    assert attempt.solved and len(attempt.rows) == 4
    assert attempt.submit("PLATE") is None

    failed = Attempt(ANSWER, VALID_WORDS)
    for guess in ("ALLEY", "PAPAL", "AMPLE", "APPLY", "PLATE", "LEAPT"):
        assert failed.submit(guess) is not None
    assert not failed.solved and len(failed.rows) == 6
    assert failed.submit("APPLE") is None

    verify_scoring_invariants()
    print(
        "Wordle control verified: APPLE solved in 4 rows; duplicate feedback "
        "is exact-first and occurrence-limited; invalid guesses spend no row; "
        "six accepted failures exhaust the attempt; 59,049 ternary-alphabet "
        "answer/guess pairs satisfy scoring invariants"
    )


if __name__ == "__main__":
    main()
