"""Source-bounded first-Case transition model, not Dead Rising emulation."""

from dataclasses import dataclass, field


@dataclass
class FirstCase:
    phase: str = "security"
    clock: int = 0
    case_deadline: int = 100
    photo_battery: int = 2
    photo_ready: bool = True
    photo_pp: int = 0
    recruited: set[str] = field(default_factory=set)
    delivered: set[str] = field(default_factory=set)
    reunited: bool = False
    reunion_photo: bool = False
    case_state: str = "pending"
    next_case: bool = False
    saved: bool = False

    def advance(self, steps: int) -> None:
        if steps < 0:
            raise ValueError("world time cannot reverse without a load")
        self.clock += steps
        if self.clock >= self.case_deadline and self.case_state != "closed":
            self.case_state = "expired"

    def reach_roof(self) -> None:
        if self.phase != "security":
            raise ValueError("roof follows Security Room control")
        self.phase = "roof"

    def recruit(self, person: str) -> None:
        if self.phase != "roof" or person not in {"Jeff", "Natalie"}:
            raise ValueError("recruit an available rooftop civilian")
        self.recruited.add(person)
        self.reunited = self.recruited == {"Jeff", "Natalie"}

    def photograph_reunion(self) -> None:
        if self.phase != "roof" or not self.reunited:
            raise ValueError("reunion must be visible")
        if self.photo_battery <= 0 or not self.photo_ready:
            raise ValueError("camera needs charge and processing readiness")
        self.photo_battery -= 1
        self.photo_ready = False
        self.reunion_photo = True
        self.photo_pp += 1  # qualifying credit, not an asserted game score

    def finish_processing(self) -> None:
        self.photo_ready = True

    def deliver(self, person: str) -> None:
        if self.phase != "roof" or person not in self.recruited:
            raise ValueError("only a recruited civilian can be delivered")
        self.delivered.add(person)

    def enter_mall(self) -> None:
        if self.phase != "roof":
            raise ValueError("leave the rooftop for the mall")
        self.phase = "mall"
        if self.case_state == "pending":
            self.case_state = "engaged"

    def settle_brad_encounter(self) -> None:
        if self.phase != "mall" or self.case_state != "engaged":
            raise ValueError("active Case 1-2 and Food Court access required")
        self.case_state = "closed"
        self.next_case = True

    def save_at(self, fixture: str) -> None:
        if self.case_state != "closed" or fixture != "Flexin restroom":
            raise ValueError("save this trace only at the eligible fixture")
        self.saved = True

    def positive_terminal(self) -> bool:
        return (
            self.delivered == {"Jeff", "Natalie"}
            and self.reunion_photo
            and self.case_state == "closed"
            and self.next_case
            and self.saved
        )


def fixed_trace() -> FirstCase:
    run = FirstCase()
    run.reach_roof()
    run.recruit("Jeff")
    run.recruit("Natalie")
    run.photograph_reunion()
    run.deliver("Jeff")
    run.deliver("Natalie")
    run.advance(10)
    run.enter_mall()
    run.advance(20)
    run.settle_brad_encounter()
    run.save_at("Flexin restroom")
    assert run.positive_terminal()
    return run


if __name__ == "__main__":
    run = fixed_trace()
    print(f"Dead Rising source model passed: {run.case_state}, {len(run.delivered)} survivors, saved={run.saved}")
