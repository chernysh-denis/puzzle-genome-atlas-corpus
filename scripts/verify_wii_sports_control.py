#!/usr/bin/env python3
"""Source-bounded ten-pin transition control for original Wii Sports Bowling.

This checks the declared input, frame, score and Mii-record boundaries. Pinfall
and any revised skill level are supplied observations: no Wii executable,
controller sampling, collision engine or hidden Nintendo rating formula is
emulated here.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Delivery:
    stance: int
    aim: int
    held_b: bool
    released_b: bool
    wrist_turn: int
    pinfall: int


def commit_delivery(shot: Delivery) -> int:
    """Accept one explicitly released gesture and its externally observed pins."""
    assert shot.held_b and shot.released_b
    assert -100 <= shot.stance <= 100
    assert -100 <= shot.aim <= 100
    assert -100 <= shot.wrist_turn <= 100
    assert 0 <= shot.pinfall <= 10
    return shot.pinfall


def validate_frame(frame: tuple[int, ...], *, tenth: bool) -> None:
    assert frame and all(0 <= pins <= 10 for pins in frame)
    if not tenth:
        assert (len(frame) == 1 and frame[0] == 10) or (
            len(frame) == 2 and frame[0] < 10 and sum(frame) <= 10
        )
        return
    first = frame[0]
    if first == 10:
        assert len(frame) == 3
        if frame[1] < 10:
            assert frame[1] + frame[2] <= 10
    else:
        assert len(frame) >= 2 and first + frame[1] <= 10
        if first + frame[1] == 10:
            assert len(frame) == 3
        else:
            assert len(frame) == 2


def score_game(frames: tuple[tuple[int, ...], ...]) -> int:
    """Resolve ten completed frames, including earned final fill deliveries."""
    assert len(frames) == 10
    for index, frame in enumerate(frames):
        validate_frame(frame, tenth=index == 9)
    balls = [pins for frame in frames for pins in frame]
    score = 0
    offset = 0
    for frame in frames[:9]:
        if frame[0] == 10:
            score += 10 + balls[offset + 1] + balls[offset + 2]
        elif sum(frame) == 10:
            score += 10 + balls[offset + 2]
        else:
            score += sum(frame)
        offset += len(frame)
    return score + sum(frames[9])


@dataclass(frozen=True)
class MiiResult:
    score: int
    prior_skill: int
    revised_skill: int
    pro: bool
    saved: bool


def settle_record(
    *,
    completed_score: int,
    stored_on_console: bool,
    prior_skill: int,
    observed_revised_skill: int,
) -> MiiResult:
    """Accept an observed skill revision without inventing its formula."""
    assert 0 <= completed_score <= 300
    assert prior_skill >= 0 and observed_revised_skill >= 0
    return MiiResult(
        score=completed_score,
        prior_skill=prior_skill,
        revised_skill=observed_revised_skill,
        pro=observed_revised_skill > 1000,
        saved=stored_on_console,
    )


def verify() -> None:
    delivered = commit_delivery(
        Delivery(stance=-12, aim=8, held_b=True, released_b=True,
                 wrist_turn=4, pinfall=7)
    )
    assert delivered == 7
    game = ((7, 3), (4, 2)) + ((0, 0),) * 7 + ((10, 10, 10),)
    score = score_game(game)
    assert score == 50  # 7/ gets the next 4; tenth triple is 30.
    result = settle_record(
        completed_score=score,
        stored_on_console=True,
        prior_skill=995,
        observed_revised_skill=1001,
    )
    assert result.saved and result.pro and result.score != result.revised_skill


if __name__ == "__main__":
    verify()
    print("Wii Sports source-bounded control: PASS")
