#!/usr/bin/env python3
"""Source-model control for the bounded GAME-0360 Space Invaders packet.

This is a transition reconstruction from the cited Taito manual and annotated
related-program disassembly. It does not contain ROM bytes or emulate hardware.
"""

from __future__ import annotations

from dataclasses import dataclass, field


ROW_VALUES = (30, 20, 20, 10, 10)
INITIAL_INVADERS = tuple((row, column) for row in range(5) for column in range(11))


@dataclass
class State:
    invaders: set[tuple[int, int]] = field(default_factory=lambda: set(INITIAL_INVADERS))
    bases: int = 3
    score: int = 0
    bonus_awarded: bool = False
    rack: int = 1
    rack_x: int = 0
    rack_y: int = 0
    direction: int = 1
    base_x: int = 5
    player_shot_active: bool = False
    fortresses: list[set[int]] = field(
        default_factory=lambda: [set(range(44)) for _ in range(4)]
    )
    terminal: str | None = None
    control_returned: bool = True

    @property
    def effective_cycle_ticks(self) -> int:
        # The cited program services formation members in sequence; fewer live
        # members shorten the effective sweep. Exact interrupt timing is out of scope.
        return max(1, len(self.invaders))

    def move_base(self, delta: int) -> None:
        self._require_live()
        if delta not in (-1, 1):
            raise ValueError("the bounded base moves only left or right")
        self.base_x = min(10, max(0, self.base_x + delta))

    def fire(self) -> bool:
        self._require_live()
        if self.player_shot_active:
            return False
        self.player_shot_active = True
        return True

    def settle_player_shot(
        self,
        *,
        invader: tuple[int, int] | None = None,
        fortress: tuple[int, int] | None = None,
        ufo_value: int | None = None,
    ) -> None:
        if not self.player_shot_active:
            raise AssertionError("no active player projectile")
        if sum(value is not None for value in (invader, fortress, ufo_value)) > 1:
            raise ValueError("one projectile has one settlement target")

        if invader is not None:
            if invader not in self.invaders:
                raise AssertionError("invader already absent")
            self.invaders.remove(invader)
            self._add_score(ROW_VALUES[invader[0]])
        elif fortress is not None:
            fortress_index, pixel = fortress
            self.fortresses[fortress_index].discard(pixel)
        elif ufo_value is not None:
            if ufo_value not in {50, 100, 150, 300}:
                raise ValueError("unsupported sourced mystery value")
            self._add_score(ufo_value)

        self.player_shot_active = False
        if not self.invaders:
            self._rebuild_successor_rack()

    def hostile_shot_hits_fortress(self, fortress_index: int, pixel: int) -> None:
        self._require_live()
        self.fortresses[fortress_index].discard(pixel)

    def formation_contacts_fortress(self, fortress_index: int, pixels: set[int]) -> None:
        self._require_live()
        self.fortresses[fortress_index].difference_update(pixels)

    def bump_occupied_edge(self) -> None:
        self._require_live()
        self.direction *= -1
        self.rack_y += 1

    def hostile_hit_base(self) -> None:
        self._require_live()
        self.bases -= 1
        self.player_shot_active = False
        if self.bases == 0:
            self.terminal = "game-over-stock"
            self.control_returned = False
        else:
            self.base_x = 5

    def invade(self) -> None:
        self._require_live()
        self.terminal = "game-over-invasion"
        self.control_returned = False

    def _add_score(self, value: int) -> None:
        self.score += value
        if self.score >= 1500 and not self.bonus_awarded:
            self.bases += 1
            self.bonus_awarded = True

    def _rebuild_successor_rack(self) -> None:
        retained_score = self.score
        retained_bases = self.bases
        self.control_returned = False
        self.rack += 1
        self.rack_x = 0
        self.rack_y += 1
        self.direction = 1
        self.invaders = set(INITIAL_INVADERS)
        self.fortresses = [set(range(44)) for _ in range(4)]
        self.player_shot_active = False
        self.score = retained_score
        self.bases = retained_bases
        self.control_returned = True
        self.terminal = "rack-two-control"

    def _require_live(self) -> None:
        if self.terminal is not None:
            raise AssertionError(f"state already settled: {self.terminal}")


def verify_entry_and_actions() -> None:
    state = State()
    assert len(state.invaders) == 55
    assert len(state.fortresses) == 4
    assert all(len(fortress) == 44 for fortress in state.fortresses)
    assert state.bases == 3 and state.score == 0
    state.move_base(-1)
    assert state.base_x == 4
    assert state.fire()
    assert not state.fire(), "a second projectile must be rejected while one is active"
    state.settle_player_shot()
    assert state.fire(), "the channel reopens only after settlement"
    state.settle_player_shot()


def verify_formation_and_cover() -> None:
    state = State()
    first_cycle = state.effective_cycle_ticks
    direction = state.direction
    state.bump_occupied_edge()
    assert state.direction == -direction and state.rack_y == 1

    state.fire()
    state.settle_player_shot(invader=(0, 0))
    assert state.effective_cycle_ticks < first_cycle

    before = len(state.fortresses[0])
    state.fire()
    state.settle_player_shot(fortress=(0, 3))
    state.hostile_shot_hits_fortress(0, 4)
    state.formation_contacts_fortress(0, {5, 6})
    assert len(state.fortresses[0]) == before - 4


def verify_score_stock_and_failures() -> None:
    state = State(score=1490)
    state.fire()
    state.settle_player_shot(invader=(3, 0))
    assert state.score == 1500 and state.bases == 4 and state.bonus_awarded
    state._add_score(300)
    assert state.bases == 4, "the score bonus is one-time"

    stock_failure = State()
    stock_failure.hostile_hit_base()
    assert stock_failure.bases == 2 and stock_failure.terminal is None
    stock_failure.hostile_hit_base()
    assert stock_failure.bases == 1 and stock_failure.terminal is None
    stock_failure.hostile_hit_base()
    assert stock_failure.terminal == "game-over-stock"

    invasion_failure = State()
    invasion_failure.invade()
    assert invasion_failure.terminal == "game-over-invasion"
    assert invasion_failure.bases == 3, "invasion is not modelled as an ordinary hit"


def verify_first_rack_terminal() -> None:
    state = State()
    for invader in sorted(INITIAL_INVADERS):
        state.fire()
        state.settle_player_shot(invader=invader)
    assert state.terminal == "rack-two-control"
    assert state.rack == 2 and state.control_returned
    assert len(state.invaders) == 55
    assert len(state.fortresses) == 4
    assert all(len(fortress) == 44 for fortress in state.fortresses)
    assert state.score == 990
    assert state.bases == 3


def main() -> None:
    verify_entry_and_actions()
    verify_formation_and_cover()
    verify_score_stock_and_failures()
    verify_first_rack_terminal()
    print("Space Invaders source-model control: PASS")


if __name__ == "__main__":
    main()
