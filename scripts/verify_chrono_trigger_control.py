#!/usr/bin/env python3
"""Verify the bounded Chrono Trigger Millennial Fair opening packet."""

from __future__ import annotations

from dataclasses import dataclass, field


class RejectedAction(ValueError):
    """An action was attempted without its documented prerequisite."""


@dataclass
class FairState:
    party: list[str] = field(default_factory=lambda: ["Crono"])
    hp: dict[str, int] = field(default_factory=lambda: {"Crono": 70})
    silver_points: int = 0
    gold: int = 200
    experience: int = 0
    tech_points: int = 0
    pendant_returned: bool = False
    demonstration_ready: bool = False
    candy_waited: bool = False
    crono_demonstrated: bool = False
    marle_transited: bool = False
    pendant_carried: bool = False
    gate_open: bool = False
    era: int = 1000
    location: str = "Leene Square"
    ordinary_control: bool = True


class MillennialFairControl:
    def __init__(self) -> None:
        self.state = FairState()
        self.milestones: list[str] = ["ordinary-control-bedroom", "mother-200g"]

    def return_pendant_and_invite_marle(self) -> None:
        if self.state.pendant_returned:
            raise RejectedAction("Marle already received the recovered Pendant")
        if self.state.party != ["Crono"]:
            raise RejectedAction("The opening party is not in its solo state")
        self.state.pendant_returned = True
        self.state.party.append("Marle")
        self.state.hp["Marle"] = 65
        self.milestones.extend(("pendant-returned", "marle-joined"))

    def challenge_gato(self, outcome: str) -> None:
        if "Marle" not in self.state.party:
            raise RejectedAction("Marle must have joined before this fixed-route challenge")
        if outcome not in {"win", "loss"}:
            raise RejectedAction("The challenge outcome must be win or loss")
        if outcome == "loss":
            self.state.hp["Crono"] = 1
            self.state.hp["Marle"] = 1
            self.milestones.append("gato-loss-returned-at-one-hp")
            return
        self.state.silver_points += 15
        self.state.experience += 10
        self.state.tech_points += 1
        self.milestones.append("gato-win-15sp-10exp-1tp")

    def exchange_silver_points(self) -> None:
        if self.state.silver_points < 10:
            raise RejectedAction("Ten Silver Points are required for the fixed exchange")
        self.state.silver_points -= 10
        self.state.gold += 50
        self.milestones.append("ten-silver-points-exchanged-for-50g")

    def announce_demonstration_ready(self) -> None:
        if self.state.silver_points != 5 or self.state.gold != 250:
            raise RejectedAction("The fixed challenge and exchange packet is incomplete")
        self.state.demonstration_ready = True
        self.milestones.append("lucca-demonstration-ready")

    def wait_for_candy(self) -> None:
        if not self.state.demonstration_ready:
            raise RejectedAction("The demonstration route has not opened")
        self.state.candy_waited = True
        self.milestones.append("marle-candy-wait-completed")

    def demonstrate_crono_telepod(self) -> None:
        if not self.state.candy_waited:
            raise RejectedAction("The required candy wait is unresolved")
        self.state.crono_demonstrated = True
        self.milestones.append("crono-telepod-demonstrated")

    def send_marle_through_gate(self) -> None:
        if not self.state.crono_demonstrated:
            raise RejectedAction("Crono's Telepod demonstration must occur first")
        if "Marle" not in self.state.party:
            raise RejectedAction("Marle is not available for the Telepod demonstration")
        self.state.party.remove("Marle")
        self.state.marle_transited = True
        self.state.gate_open = True
        self.milestones.extend(("marle-transited", "pendant-dropped", "gate-created"))

    def collect_dropped_pendant(self) -> None:
        if not self.state.marle_transited or not self.state.gate_open:
            raise RejectedAction("No dropped Pendant is available beside an open Gate")
        self.state.pendant_carried = True
        self.milestones.append("dropped-pendant-collected")

    def follow_marle(self) -> None:
        if not self.state.pendant_carried:
            raise RejectedAction("Crono must recover the Pendant before following")
        if not self.state.gate_open:
            raise RejectedAction("The authored era Gate is not open")
        self.state.era = 600
        self.state.location = "Truce Canyon"
        self.state.ordinary_control = True
        self.state.gate_open = False
        self.milestones.extend(("crono-transited", "ordinary-control-truce-canyon"))


def expect_rejected(action, expected: str) -> None:
    try:
        action()
    except RejectedAction as error:
        assert expected in str(error)
    else:
        raise AssertionError("Invalid opening action was accepted")


def complete_success_route(control: MillennialFairControl) -> None:
    control.return_pendant_and_invite_marle()
    control.challenge_gato("win")
    control.exchange_silver_points()
    control.announce_demonstration_ready()
    control.wait_for_candy()
    control.demonstrate_crono_telepod()
    control.send_marle_through_gate()
    control.collect_dropped_pendant()
    control.follow_marle()


def main() -> None:
    invalid = MillennialFairControl()
    expect_rejected(lambda: invalid.challenge_gato("win"), "Marle must")
    expect_rejected(invalid.exchange_silver_points, "Ten Silver Points")
    expect_rejected(invalid.announce_demonstration_ready, "incomplete")
    expect_rejected(invalid.wait_for_candy, "has not opened")
    expect_rejected(invalid.demonstrate_crono_telepod, "candy wait")
    expect_rejected(invalid.send_marle_through_gate, "must occur first")
    expect_rejected(invalid.collect_dropped_pendant, "No dropped Pendant")
    expect_rejected(invalid.follow_marle, "recover the Pendant")

    control = MillennialFairControl()
    complete_success_route(control)
    assert control.state.party == ["Crono"]
    assert control.state.silver_points == 5
    assert control.state.gold == 250
    assert control.state.experience == 10
    assert control.state.tech_points == 1
    assert control.state.era == 600
    assert control.state.location == "Truce Canyon"
    assert control.state.ordinary_control
    assert not control.state.gate_open
    assert control.milestones[-1] == "ordinary-control-truce-canyon"
    assert "blue-imp-encounter" not in control.milestones

    retry = MillennialFairControl()
    retry.return_pendant_and_invite_marle()
    retry.challenge_gato("loss")
    assert retry.state.silver_points == 0
    assert retry.state.experience == 0
    assert retry.state.tech_points == 0
    assert set(retry.state.hp.values()) == {1}
    retry.challenge_gato("win")
    retry.exchange_silver_points()
    retry.announce_demonstration_ready()
    retry.wait_for_candy()
    retry.demonstrate_crono_telepod()
    retry.send_marle_through_gate()
    retry.collect_dropped_pendant()
    retry.follow_marle()
    assert retry.state.location == "Truce Canyon"

    print(
        "Chrono Trigger control verified: Marle join, retryable Gato challenge, "
        "15 SP / 10 EXP / 1 TP reward, 10 SP to 50G exchange, ordered Telepod "
        "events, Pendant-gated era transit and pre-Blue-Imp terminal control."
    )


if __name__ == "__main__":
    main()
